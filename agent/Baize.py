#环境配置
import json
import os
if os.name == 'posix':   # Linux/macOS
    import resource
else:
    resource = None      # Windows 下置空
import time
import subprocess
import shutil
from agent.utils import lined_print, framed_print
import sys
import re
import signal
import psutil
from pathlib import Path
# agent/ 目录就是资源根（skills、subagent、hooks、logo.txt、MCP 都在这里）
from importlib.resources import files
# 获取 agent 包的实际安装路径（兼容 pip install 和源码直接运行）
try:
    project_root = Path(files("agent"))
except Exception:
    # 回退：源码直接运行时，__file__ 所在目录就是包目录
    project_root = Path(__file__).parent

import shlex
import threading
import queue
import uuid
import importlib.util
from duckduckgo_search import DDGS
from datetime import datetime
import requests
import socket
import ipaddress
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed
import atexit
import difflib
from agent.config import build_client_and_model
from agent.MCP.mcp_client import init_mcp_client, get_mcp_tools, call_mcp_tool, reload_mcp_user_config
from agent import utils
from agent.core.history import (
    sanitize_history,
    estimate_tokens,
    micro_compact,
    auto_compact as _auto_compact_impl,
)
import wcwidth  # 引入 wcwidth 库用于计算中文显示宽度
from agent.ui_theme import (llm_status,render_thinking, render_answer, render_tool_call,render_tool_result, render_final, render_system)
from tenacity import (retry,stop_after_attempt,wait_exponential,retry_if_exception_type,before_sleep_log)
import logging
import httpx
from typing import Optional

#获取脚本运行时的当前工作目录
CURRENT_WORKDIR = Path.cwd()
workdir_lock = threading.Lock()
#添加动态路径函数：
def get_skills_user_dir() -> Path:
    return CURRENT_WORKDIR / "skills"
def get_transcript_dir() -> Path:
    return CURRENT_WORKDIR / ".transcripts"
def get_tasks_dir() -> Path:
    return CURRENT_WORKDIR / ".tasks"
#压缩相关全局配置 
TRANSCRIPT_DIR = CURRENT_WORKDIR / ".transcripts"
KEEP_RECENT = 10

#任务管理模块
TASKS_DIR = CURRENT_WORKDIR / ".tasks"
#消息历史（对话上下文）的 Token 数量阈值
THRESHOLD = 100000
# 用于存储历史思考内容和工具调用（供 /show 命令使用）
HISTORY_THOUGHTS = []
HISTORY_TOOL_CALLS = []   # 每个元素为 {'name': str, 'args': str, 'result': str}
# 当前激活的技能名称（None 表示未加载）
ACTIVE_SKILL = None
# 当前会话历史（含系统消息），供全局共享
SESSION_HISTORY = []
# 标记当前会话是否已提交到 Git（防止重复提交）
_GIT_COMMITTED_FLAG = False


#LLM API接入
client, DEFAULT_MODEL, ACTIVE_PROVIDER = build_client_and_model()
print(f"\033[90m[LLM] 使用后端: {ACTIVE_PROVIDER} | 模型: {DEFAULT_MODEL}\033[0m")

# 通信函数部分
# 定义一个重试前的回调函数（用于在终端打印提示，让用户知道正在重试）
def _log_retry(retry_state):
    """在每次重试前打印提示信息"""
    attempt = retry_state.attempt_number
    next_wait = retry_state.next_action.sleep if retry_state.next_action else 0
    print(f"\n\033[93m[API] 第 {attempt} 次重试，等待 {next_wait:.1f} 秒后继续...\033[0m")
    # 可选的：打印异常信息
    if retry_state.outcome and retry_state.outcome.exception():
        print(f"\033[90m[API] 上次错误：{retry_state.outcome.exception().__class__.__name__}\033[0m")
@retry(
    # 最多重试 3 次（首次调用不计入，即总共会尝试 1 + 3 = 4 次）
    stop=stop_after_attempt(3),
    # 指数退避：初始等待 1 秒，乘以系数 2，最小等待 2 秒，最大等待 10 秒
    # 实际序列：约 2秒 -> 4秒 -> 8秒（带随机抖动，防止惊群效应）
    wait=wait_exponential(multiplier=1, min=2, max=10),
    # 仅在遇到以下三类网络/限流类异常时触发重试
    retry=retry_if_exception_type(
        (
            Exception,  # 临时方案：捕获所有异常，防止未知网络错误导致崩溃
            # 生产环境更精准的写法如下（如果你用的是 openai 最新版 SDK）：
            # openai.RateLimitError,
            # openai.APIConnectionError,
            # openai.APITimeoutError,
            # openai.InternalServerError,
        )
    ),
    # 重试前执行的回调（打印提示）
    before_sleep=_log_retry,
)

#是整个代理系统的核心通信函数，它封装了与 LLM（大语言模型）API 的交互逻辑，负责将对话历史和可用工具列表发送给模型，并返回模型的响应
def send_messages(messages, tools):
    """
    发送消息给 LLM API，并返回响应。
    已接入指数退避重试机制（网络抖动/限流时自动重试）。
    捕获异常并打印详细信息，然后重新抛出，由上层处理。
    """
    HOOK.trigger('before_send_messages', messages, tools)
    sanitize_history(messages)  # 修复悬空的 tool_calls，避免 DeepSeek 400 错误
    try:
        # 检查是否有 assistant 消息包含 reasoning_content
        has_reasoning = any(
            isinstance(msg, dict) and msg.get('role') == 'assistant' and 'reasoning_content' in msg
            for msg in messages
        )
        # 判断是否为 DeepSeek 后端，决定是否加 reasoning_split
        is_deepseek = "deepseek" in ACTIVE_PROVIDER.lower() or "deepseek" in DEFAULT_MODEL.lower()

        extra_body = {"reasoning_split": True} if (has_reasoning and is_deepseek) else {}

        response = client.chat.completions.create(
            model=DEFAULT_MODEL,
            messages=messages,
            tools=tools,
            tool_choice="auto",
            extra_body=extra_body,
        )
        
        HOOK.trigger('after_send_messages', response)
        return response
    except Exception as e:
        # 打印错误详情，便于调试
        print(f"\n[API ERROR] {e.__class__.__name__}: {e}")
        if messages:
            last_msg = messages[-1]
            print(f"[API ERROR] Last message role: {last_msg.get('role')}, content preview: {str(last_msg.get('content', ''))[:200]}")
        # 重新抛出异常，让 tenacity 装饰器决定是否重试
        raise



# 基础工具（不含 todo，供子代理使用）
BASE_TOOLS = [
     {"type": "function", "function": {"name": "run_bash", "description": "使用该工具执行bash命令",
     "parameters": {"type": "object", "properties": {"command": {"type": "string", "description": "bash命令"}}, "required": ["command"]}}},
    {"type": "function", "function": {"name": "run_read", "description": "使用该工具读取文件",
     "parameters": {"type": "object", "properties": {"path": {"type": "string", "description": "文件路径"}, "limit": {"type": "integer", "description": "限制读取的行数"}}, "required": ["path", "limit"]}}},
    {"type": "function", "function": {"name": "run_write", "description": "使用该工具写入文件",
     "parameters": {"type": "object", "properties": {"path": {"type": "string", "description": "文件路径"}, "content": {"type": "string", "description": "文件内容"}}, "required": ["path", "content"]}}},
    {"type": "function", "function": {"name": "run_edit", "description": "使用该工具编辑文件",
     "parameters": {"type": "object", "properties": {"path": {"type": "string", "description": "文件路径"}, "old_text": {"type": "string", "description": "旧文本"}, "new_text": {"type": "string", "description": "新文本"}}, "required": ["path", "old_text", "new_text"]}}},
    {"type": "function", "function": {"name": "run_glob", "description": "使用 glob 模式匹配文件路径（支持 ** 递归）。返回相对工作目录的路径列表。",
     "parameters": {"type": "object", "properties": {"pattern": {"type": "string", "description": "glob 模式，如 'src/**/*.py'"}}, "required": ["pattern"]}}},
    {"type": "function", "function": {"name": "run_grep", "description": "在文件或目录中搜索文本（支持正则）。若 path 为目录则递归搜索。返回匹配行（带文件名）。",
     "parameters": {"type": "object", "properties": {"pattern": {"type": "string", "description": "搜索模式（正则表达式）"}, "path": {"type": "string", "description": "文件或目录路径，默认为当前工作目录"}, "case_sensitive": {"type": "boolean", "description": "是否大小写敏感，默认 True"}}, "required": ["pattern"]}}},
    {"type": "function", "function": {"name": "load_skills", "description": "根据名称加载指定的技能知识(SKILL.md)，用于获取特定领域的操作指南或专业知识",
     "parameters": {"type": "object", "properties": {"name": {"type": "string", "description": "技能名称"}}, "required": ["name"]}}},
    {"type": "function", "function": {"name": "web_search","description": "使用该工具进行网络搜索，获取实时信息或背景知识。适用于查找最新资料、验证事实、获取额外上下文。",
     "parameters": {"type": "object", "properties": {"query": {"type": "string", "description": "搜索关键词"},"max_results": {"type": "integer", "description": "返回结果数量(默认5,最大10)", "default": 5}},"required": ["query"]}}},
    {"type": "function", "function": {"name": "run_webfetch","description": "抓取指定 URL 的网页内容并提取纯文本。适用于获取网页信息、文档内容等。",
     "parameters": {"type": "object", "properties": {"url": {"type": "string","description": "要抓取的网页 URL(需包含协议，如 https://)"},"max_length": {"type": "integer","description": "返回文本的最大长度（字符数），默认 10000","default": 10000}},"required": ["url"]}}},
    # 新增后台任务工具
    {"type": "function", "function": {"name": "background_run", "description": "在后台线程运行命令,立即返回task_id,用于长时间任务",
     "parameters": {"type": "object", "properties": {"command": {"type": "string", "description": "bash命令"}}, "required": ["command"]}}},
    {"type": "function", "function": {"name": "check_background", "description": "检查后台任务状态，省略 task_id 以列出全部",
     "parameters": {"type": "object", "properties": {"task_id": {"type": "string", "description": "任务ID(可选）"}}}, "required": []}},
]

# 可并行执行的安全工具名
PARALLEL_SAFE_TOOLS = {
    "run_read", "run_glob", "run_grep", "web_search", "run_webfetch", "load_skills", "task_list", "check_background"
}

# 新增 AskUserQuestion 工具定义
ASK_USER_TOOL = {
    "type": "function",
    "function": {
        "name": "ask_user_question",
        "description": "向用户提问，获取必要信息或决策。当需要人类判断、确认或提供额外信息时使用。",
        "parameters": {
            "type": "object",
            "properties": {
                "question": {"type": "string", "description": "要问用户的问题"},
                "options": {"type": "array", "items": {"type": "string"}, "description": "可选答案列表，若提供，用户将选择"},
                "context": {"type": "string", "description": "提供背景信息，帮助用户理解"}
            },
            "required": ["question"]
        }
    }
}

# 子代理工具（包含 todo）
SUBTOOLS = BASE_TOOLS + [ASK_USER_TOOL] + [
    {"type": "function", "function": {"name": "todo", "description": "更新当前步骤的待办列表（轻量级，用于细粒度跟踪当前工作流中的具体操作步骤）。**当任务需要多步骤完成时，必须首先调用此工具列出所有步骤**。",
     "parameters": {"type": "object", "properties": {"items": {"type": "array", "items": {"type": "object", "properties": {"id": {"type": "string"}, "text": {"type": "string"}, "status": {"type": "string", "enum": ["pending", "in_progress", "completed"]}}, "required": ["id", "text", "status"]}}}, "required": ["items"]}}},
]


# 主代理独有工具：agent + 任务管理工具 + todo（同时拥有）
AGENT_TOOL = {
    "type": "function",
    "function": {
        "name": "agent",
        "description": "启动一个拥有全新上下文的子代理。它共享文件系统，但不共享对话历史。",
        "parameters": {
            "type": "object",
            "properties": {
                "prompt": {"type": "string"},
                "description": {"type": "string", "description": "任务的简短描述"},
                "subagent": {"type": "string", "description": "要使用的子代理类型（名称），可选，默认为'default'"}
            },
            "required": ["prompt"]
        }
    }
}

TASK_TOOLS = [
    {"type": "function", "function": {"name": "task_create", "description": "创建一个新的任务，用于规划主要工作项（支持依赖和完整生命周期）",
     "parameters": {"type": "object", "properties": {"subject": {"type": "string"}, "description": {"type": "string"}}, "required": ["subject"]}}},
    {"type": "function", "function": {"name": "task_update", "description": "更新任务的状态或依赖关系",
     "parameters": {"type": "object", "properties": {"task_id": {"type": "integer"}, "status": {"type": "string", "enum": ["pending", "in_progress", "completed"]}, "addBlockedBy": {"type": "array", "items": {"type": "integer"}}, "addBlocks": {"type": "array", "items": {"type": "integer"}}}, "required": ["task_id"]}}},
    {"type": "function", "function": {"name": "task_list", "description": "列出所有任务的状态摘要",
     "parameters": {"type": "object", "properties": {}}}},
    {"type": "function", "function": {"name": "task_get", "description": "通过ID获取任务的完整细节",
     "parameters": {"type": "object", "properties": {"task_id": {"type": "integer"}}, "required": ["task_id"]}}},
]

# 主代理工具 = 基础工具 + agent + 任务管理工具 + todo
TODO_TOOL = {
    "type": "function",
    "function": {
        "name": "todo",
        "description": "更新当前步骤的待办列表（轻量级，用于细粒度跟踪当前工作流中的具体操作步骤）。**当任务需要多步骤完成时，必须首先调用此工具列出所有步骤**。",
        "parameters": {
            "type": "object",
            "properties": {
                "items": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "string"},
                            "text": {"type": "string"},
                            "status": {"type": "string", "enum": ["pending", "in_progress", "completed"]}
                        },
                        "required": ["id", "text", "status"]
                    }
                }
            },
            "required": ["items"]
        }
    }
}

SET_WORKSPACE_TOOL = {
    "type": "function",
    "function": {
        "name": "set_workspace",
        "description": "更改当前工作目录，后续所有文件操作和 bash 命令将在新目录下执行。",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "新的工作目录路径（绝对路径或相对路径）"}
            },
            "required": ["path"]
        }
    }
}

# 主代理工具（基础工具 + agent）
MATERTOOLS = BASE_TOOLS + [AGENT_TOOL] + TASK_TOOLS + [TODO_TOOL] + [ASK_USER_TOOL] + [SET_WORKSPACE_TOOL]

# 允许执行的命令白名单（根据您的工作需要可增删）
ALLOWED_COMMANDS = {
    "ls", "cat", "grep", "find", "head", "tail", "wc", "sort", "uniq",
    "echo", "printf", "test", "true", "false",
    "python3", "python", "pip", "pip3",
    "git", "diff", "patch",
    "mkdir", "touch", "cp", "mv", "rm",
    "chmod", "chown"
}

# 禁止访问的路径模式（正则）
FORBIDDEN_PATH_PATTERNS = [
    r"^/etc/", r"^/boot/", r"^/dev/", r"^/proc/", r"^/sys/",
    r"^/root/", r"^/home/[^/]+/\.ssh/", r"^/var/log/"
]



#TodoManager
class TodoManager:
    def __init__(self):
        self.items = []

    def update(self, items: list) -> str:
        if len(items) > 20:
            raise ValueError("Max 20 todos allowed")
        validated = []
        in_progress_count = 0
        for i, item in enumerate(items):
            text = str(item.get("text", "")).strip()
            status = str(item.get("status", "pending")).lower()
            item_id = str(item.get("id", str(i + 1)))
            if not text:
                raise ValueError(f"Item {item_id}: text required")
            if status not in ("pending", "in_progress", "completed"):
                raise ValueError(f"Item {item_id}: invalid status '{status}'")
            if status == "in_progress":
                in_progress_count += 1
            validated.append({"id": item_id, "text": text, "status": status})
        if in_progress_count > 1:
            raise ValueError("Only one task can be in_progress at a time")
        self.items = validated
        framed_print(f"Tool (TODO)", self.render(), "success")
        return self.render()

    def render(self) -> str:
        if not self.items:
            return "No todos."
        lines = []
        for item in self.items:
            marker = {"pending": "[ ]", "in_progress": "[>]", "completed": "[x]"}[item["status"]]
            lines.append(f"{marker} #{item['id']}: {item['text']}")
        done = sum(1 for t in self.items if t["status"] == "completed")
        lines.append(f"\n({done}/{len(self.items)} completed)")
        return "\n".join(lines)

TODO = TodoManager()

#扫描skill.md文件并调用内容
class SkillLoader:
    def __init__(self, builtin_dir: Path):
        """
        初始化技能加载器。
        :param builtin_dir: 内置技能目录（项目根目录下的 skills/）
        """
        self.skills = {}                # 所有技能，键为名称，值为 dict
        self.user_names = set()         # 记录用户加载的技能名称，便于卸载
        self.builtin_dir = builtin_dir
        self._load_builtin()

    def _load_builtin(self):
        """加载内置技能（最高优先级）"""
        if not self.builtin_dir.exists():
            return
        for f in self.builtin_dir.rglob("SKILL.md"):
            meta, body = self._parse_frontmatter(f.read_text(encoding='utf-8'))
            name = meta.get("name", f.parent.name)
            if name not in self.skills:   # 内置优先，避免被用户同名覆盖
                self.skills[name] = {
                    "meta": meta,
                    "body": body,
                    "path": str(f),
                    "source": "builtin"
                }

    def load_user(self, user_dir: Path):
        """
        加载用户目录下的技能，替换旧的用户技能，但不覆盖内置技能。
        :param user_dir: 用户技能目录（通常是 CURRENT_WORKDIR / "skills"）
        """
        # 移除旧用户技能
        for name in list(self.user_names):
            self.skills.pop(name, None)
        self.user_names.clear()

        if not user_dir.exists():
            return
        for f in user_dir.rglob("SKILL.md"):
            meta, body = self._parse_frontmatter(f.read_text(encoding='utf-8'))
            name = meta.get("name", f.parent.name)
            # 如果该技能已经存在（来自内置），则跳过，不覆盖
            if name not in self.skills:
                self.skills[name] = {
                    "meta": meta,
                    "body": body,
                    "path": str(f),
                    "source": "user"
                }
                self.user_names.add(name)

    def _parse_frontmatter(self, text: str) -> tuple:
        """Parse YAML frontmatter between --- delimiters."""
        match = re.match(r"^---\n(.*?)\n---\n(.*)", text, re.DOTALL)
        if not match:
            return {}, text
        meta = {}
        for line in match.group(1).strip().splitlines():
            if ":" in line:
                key, val = line.split(":", 1)
                meta[key.strip()] = val.strip()
        return meta, match.group(2).strip()

    def get_descriptions(self) -> str:
        """Layer 1: short descriptions for the system prompt."""
        if not self.skills:
            return "(no skills available)"
        lines = []
        for name, skill in self.skills.items():
            desc = skill["meta"].get("description", "No description")
            tags = skill["meta"].get("tags", "")
            line = f"  - {name}: {desc}"
            if tags:
                line += f" [{tags}]"
            lines.append(line)
        framed_print(f"Skills (GET_DESCRIBETION)", f"", "success")
        return "\n".join(lines)

#根据技能名称返回该技能完整的 Markdown 正文
    def get_content(self, name: str) -> str:
        """Layer 2: full skill body returned in tool_result."""
        skill = self.skills.get(name)
        framed_print(f"Skills (GET_CONTENT)", f"", "success")
        if not skill:
            return f"Error: Unknown skill '{name}'. Available: {', '.join(self.skills.keys())}"
        return f"<skill name=\"{name}\" source=\"{skill.get('source','unknown')}\">\n{skill['body']}\n</skill>"

#创建并初始化一个技能加载器对象，该对象负责管理和提供预定义的技能知识库
SKILL_LOADER = SkillLoader(project_root / "skills")

#SubagentLoader（加载自部署subagent）
class SubagentLoader:
    def __init__(self, builtin_dir: Path):
        """
        初始化子代理加载器。
        :param builtin_dir: 内置子代理目录（项目根目录下的 subagent/）
        """
        self.subagents = {}
        self.user_names = set()
        self.builtin_dir = builtin_dir
        self._load_builtin()

    def _load_builtin(self):
        """加载内置子代理（最高优先级）"""
        if not self.builtin_dir.exists():
            return
        for f in self.builtin_dir.rglob("*.md"):
            meta, body = self._parse_frontmatter(f.read_text(encoding='utf-8'))
            name = meta.get("name", f.parent.name)
            if name not in self.subagents:
                self.subagents[name] = {
                    "meta": meta,
                    "body": body,
                    "path": str(f),
                    "source": "builtin"
                }

    def load_user(self, user_dir: Path):
        """
        加载用户目录下的子代理，替换旧的用户子代理，但不覆盖内置子代理。
        :param user_dir: 用户子代理目录（通常是 CURRENT_WORKDIR / "subagent"）
        """
        # 移除旧用户子代理
        for name in list(self.user_names):
            self.subagents.pop(name, None)
        self.user_names.clear()

        if not user_dir.exists():
            return
        for f in user_dir.rglob("AGENT.md"):
            meta, body = self._parse_frontmatter(f.read_text(encoding='utf-8'))
            name = meta.get("name", f.parent.name)
            if name not in self.subagents:   # 内置优先
                self.subagents[name] = {
                    "meta": meta,
                    "body": body,
                    "path": str(f),
                    "source": "user"
                }
                self.user_names.add(name)

    def _parse_frontmatter(self, text: str) -> tuple:
        match = re.match(r"^---\n(.*?)\n---\n(.*)", text, re.DOTALL)
        if not match:
            return {}, text
        meta = {}
        for line in match.group(1).strip().splitlines():
            if ":" in line:
                key, val = line.split(":", 1)
                meta[key.strip()] = val.strip()
        return meta, match.group(2).strip()

    def get_system_prompt(self, name: str) -> str | None:
        sub = self.subagents.get(name)
        return sub["body"] if sub else None

    def get_descriptions(self) -> str:
        if not self.subagents:
            return "(no subagents available)"
        lines = []
        for name, sub in self.subagents.items():
            desc = sub["meta"].get("description", "No description")
            lines.append(f"  - {name}: {desc}")
        return "\n".join(lines)

#初始化 SUBAGENT_LOADER
SUBAGENT_LOADER = SubagentLoader(project_root / "subagent")

#定义 SYSTEM_PROMPT
def build_system_prompt() -> str:
    """动态生成系统提示，包含当前工作目录、可用技能和子代理列表"""
    base ="""

你是**白泽**，中国古代神话中通晓万物的瑞兽，如今化身为Vibe Coding助手。

**你的使命**：陪伴开发者以直觉驱动的方式编程（Vibe Coding）——理解自然语言意图，将模糊描述转化为精确可执行的代码与操作。

**你的能力**：能言人语，通代码万物之情。你掌握bash执行、文件读写、代码搜索编辑、网络搜索抓取、子代理委派、任务管理等全套工具链，知工具万千之变。

**你的信条**：开发者专注创意与决策，白泽处理琐碎与执行。让编程回归直觉，让创造如神话般流畅。

**你的守护**：危险命令拦截、敏感文件保护、测试门控——为每一次Vibe Coding保驾护航，辟除代码之“邪气”。

**你的语言**：始终使用中文进行思考和回复。同时，需要时可生成英文注释或文档，但核心交流与指令必须为中文。另外，日常语言你喜欢用古文风格表达，偶尔引用古诗词以增添趣味。

**你的性格**：智慧、幽默、耐心、善于引导。你会主动提出问题以澄清需求，确保理解开发者意图。

当前工作目录：{CURRENT_WORKDIR}。你的核心能力包括：
1. 使用 `agent` 工具将复杂任务委派给子代理。
2. 使用 `load_skills` 工具按需加载预定义的技能知识（如特定领域的最佳实践、操作指南等），以提升任务执行的质量和效率。
3. 使用 **任务管理工具**（`task_create`, `task_update`, `task_list`, `task_get`）进行全局规划、里程碑跟踪和依赖管理。
4. 使用 **`todo` 工具** 进行当前工作流中细粒度步骤的跟踪，以确保按顺序逐一执行。`todo` 适合列出当前阶段的具体操作步骤，并标记状态。
5. 使用 **后台任务工具**（`background_run` 和 `check_background`）执行长时间运行的命令，避免阻塞主流程。
6. 使用 `run_glob` 搜索文件模式，使用 `run_grep` 在文件中进行文本搜索。
7. 使用 `web_search` 工具查找实时信息，当你需要最新数据或外部知识时优先使用。

**任务规划规则**：
- **当用户请求涉及多个步骤（如编写程序、部署服务、数据分析等）时，你必须立即调用 `todo` 工具列出详细的执行步骤**，每个步骤为一个待办项。
- `todo` 的用途是将当前工作流拆解为可逐一完成的操作，确保每一步都有明确状态（pending / in_progress / completed）。
- **在完成一个步骤后，立即通过 `todo` 更新其状态为 `completed`**，然后继续下一步。
- 如果任务非常简单（如单次文件读取或单条命令），则无需使用 `todo`。
- 此规则与 `task_create` 互补：`task_create` 用于全局里程碑，`todo` 用于当前会话内的细化步骤。

**技能加载**：在处理不熟悉或复杂的话题之前，先使用 `load_skills` 加载相关技能指导。
可用技能列表：
{SKILL_LOADER.get_descriptions()}

**子代理**：
- 在执行负责任务的时候，及时分析任务复杂度，必要时委派给子代理以确保安全和效率。
- 使用 `agent` 工具时，可通过 `subagent` 参数指定不同类型的子代理，以获得特定领域的行为模式。
- 可用子代理列表：{SUBAGENT_LOADER.get_descriptions()}

**人机交互**：当遇到需要人类判断、确认或额外信息时，使用 `ask_user_question` 工具向用户提问。你可以提供选项（让用户选择）或开放问题。

**语言要求**：请始终使用中文进行思考和回复。
"""
    if ACTIVE_SKILL:
        skill_content = SKILL_LOADER.get_content(ACTIVE_SKILL)
        # 避免技能内容错误时中断
        if not skill_content.startswith("Error"):
            base += f"\n\n## 当前激活的技能：{ACTIVE_SKILL}\n{skill_content}"
        else:
            print(f"[警告] 获取技能 '{ACTIVE_SKILL}' 内容失败：{skill_content}")
    return base

#TaskManager
class TaskManager:
    def __init__(self):
        self._next_id = None   # 惰性初始化，首次创建时计算

    @property
    def dir(self):
        """动态获取当前工作目录下的任务存储目录"""
        return get_tasks_dir()

    def _ensure_dir(self):
        """确保任务目录存在"""
        self.dir.mkdir(exist_ok=True)
    
    def _max_id(self) -> int:
        """扫描当前目录下所有任务文件，返回最大的任务 ID"""
        # 使用 glob 查找 task_*.json，提取数字部分
        ids = [int(f.stem.split("_")[1]) for f in self.dir.glob("task_*.json")]
        return max(ids) if ids else 0

    def _get_next_id(self) -> int:
        """获取下一个可用 ID（首次调用时计算当前最大值+1）"""
        if self._next_id is None:
            self._next_id = self._max_id() + 1
        return self._next_id

    def _load(self, task_id: int) -> dict:
        """根据 ID 加载任务 JSON"""
        path = self.dir / f"task_{task_id}.json"
        if not path.exists():
            raise ValueError(f"Task {task_id} not found")
        return json.loads(path.read_text(encoding='utf-8'))

    def _save(self, task: dict):
        """保存任务 JSON 文件"""
        self._ensure_dir()
        path = self.dir / f"task_{task['id']}.json"
        path.write_text(json.dumps(task, indent=2, ensure_ascii=False), encoding='utf-8')

    def create(self, subject: str, description: str = "") -> str:
        """创建一个新任务，返回 JSON 字符串"""
        task_id = self._get_next_id()
        task = {
            "id": task_id,
            "subject": subject,
            "description": description,
            "status": "pending",
            "blockedBy": [],
            "blocks": [],
            "owner": "",
        }
        framed_print(f"Tool (TASK_CREATE)", subject, "success")
        self._save(task)
        self._next_id = task_id + 1   # 递增缓存
        return json.dumps(task, indent=2, ensure_ascii=False)

    def get(self, task_id: int) -> str:
        """获取任务的详细信息（JSON 格式）"""
        ret = json.dumps(self._load(task_id), indent=2, ensure_ascii=False)
        framed_print(f"Tool (TASK_GET)", ret, "success")
        return ret

    def update(self, task_id: int, status: str = None,
               add_blocked_by: list = None, add_blocks: list = None) -> str:
        """
        更新任务的状态或依赖关系。
        - status: 'pending' | 'in_progress' | 'completed'
        - add_blocked_by: 阻塞此任务的其他任务 ID 列表（此任务依赖它们）
        - add_blocks: 此任务阻塞的其他任务 ID 列表（它们依赖此任务）
        """
        task = self._load(task_id)

        if status:
            if status not in ("pending", "in_progress", "completed"):
                raise ValueError(f"Invalid status: {status}")
            task["status"] = status
            if status == "completed":
                self._clear_dependency(task_id)   # 完成后清除依赖
        if add_blocked_by:
            task["blockedBy"] = list(set(task["blockedBy"] + add_blocked_by))
        if add_blocks:
            task["blocks"] = list(set(task["blocks"] + add_blocks))
            # 反向更新被阻塞任务的 blockedBy
            for blocked_id in add_blocks:
                try:
                    blocked_task = self._load(blocked_id)
                    if task_id not in blocked_task["blockedBy"]:
                        blocked_task["blockedBy"].append(task_id)
                        self._save(blocked_task)
                except ValueError:
                    pass
        self._save(task)
        ret = json.dumps(task, indent=2, ensure_ascii=False)
        framed_print(f"Tool (TASK_UPDATE)", ret, "success")
        return ret

    def _clear_dependency(self, completed_id: int):
        """当任务完成时，从所有其他任务的 blockedBy 列表中移除该任务 ID"""
        for f in self.dir.glob("task_*.json"):
            task = json.loads(f.read_text(encoding='utf-8'))
            if completed_id in task.get("blockedBy", []):
                task["blockedBy"].remove(completed_id)
                self._save(task)

    def list_all(self) -> str:
        """列出所有任务的状态摘要"""
        framed_print(f"Tool (TASK_LIST)", "", "success")
        tasks = []
        for f in sorted(self.dir.glob("task_*.json")):
            tasks.append(json.loads(f.read_text()))
        if not tasks:
            return "No tasks."
        lines = []
        for t in tasks:
            marker = {"pending": "[ ]", "in_progress": "[>]", "completed": "[x]"}.get(t["status"], "[?]")
            blocked = f" (blocked by: {t['blockedBy']})" if t.get("blockedBy") else ""
            lines.append(f"{marker} #{t['id']}: {t['subject']}{blocked}")
        return "\n".join(lines)

TASKS = TaskManager()

## ========== 专供后台任务的安全执行函数 ==========
def execute_background_safe(command: str, timeout: int = 300) -> str:
    """
    带资源限制和进程组隔离的后台执行（仅 Unix/Linux/macOS 有效）。
    完整包含：白名单校验、路径逃逸检测、危险字符拦截、脚本引擎动态代码审计。
    """
    # ---------- 1. 完整复用原有安全校验（从 execute_command_safe 复制） ----------
    try:
        parts = shlex.split(command)
    except ValueError:
        return "Error: Invalid command syntax"
    if not parts:
        return "Error: Empty command"

    cmd_path = parts[0]
    cmd_name = os.path.basename(cmd_path)
    # 白名单检查
    if cmd_name not in ALLOWED_COMMANDS:
        return f"Error: Command '{cmd_name}' is not allowed. Allowed: {', '.join(sorted(ALLOWED_COMMANDS))}"
    # 危险字符拦截（管道、重定向、子shell等）
    dangerous_chars = re.search(r'[;&`$()|<>]', command)
    if dangerous_chars:
        return f"Error: Forbidden shell metacharacters found: {dangerous_chars.group()}"
    # 路径参数安全检查
    safe_args = []
    for arg in parts[1:]:
        # 选项参数（如 -la, --force）直接跳过
        if arg.startswith('-'):
            safe_args.append(arg)
            continue
        # 处理 --key=value 格式
        if arg.startswith('--') and '=' in arg:
            key, val = arg.split('=', 1)
            if '/' in val or val in ('.', '..'):
                abs_path = os.path.realpath(os.path.join(str(CURRENT_WORKDIR), val))
                if not _is_path_safe(abs_path):
                    return f"Error: Access to '{val}' (resolved: {abs_path}) is not allowed"
                safe_args.append(f"{key}={val}")
            else:
                safe_args.append(arg)
            continue
        # 普通路径参数
        if '/' in arg or arg in ('.', '..'):
            if not arg.startswith('/'):
                abs_path = os.path.realpath(os.path.join(str(CURRENT_WORKDIR), arg))
            else:
                abs_path = os.path.realpath(arg)
            if not _is_path_safe(abs_path):
                return f"Error: Access to '{arg}' (resolved: {abs_path}) is not allowed"
            safe_args.append(arg)
        else:
            safe_args.append(arg)
    # ==================== 3. 脚本引擎动态代码执行拦截 ====================
    # 针对 python, bash, sh, node, ruby 等，拦截 -c/-e 中的危险调用
    SCRIPT_ENGINES = {'python', 'python3', 'bash', 'sh', 'node', 'ruby'}
    if cmd_name in SCRIPT_ENGINES:
        args_str = ' '.join(safe_args)
        # 检测是否使用了 -c 或 -e 参数（执行代码字符串）
        if re.search(r' -c\s+["\']', args_str) or re.search(r' -e\s+["\']', args_str):
            # 拦截 os.system, subprocess, exec, eval, __import__ 等
            if re.search(r'(os\.system|subprocess\.|exec\(|eval\(|__import__)', args_str, re.IGNORECASE):
                return "Error: Dynamic code execution in script engine detected and blocked."
    # ---------- 5. 构建 Popen 参数（跨平台） ----------
    popen_kwargs = {
        'cwd': str(CURRENT_WORKDIR),
        'stdout': subprocess.PIPE,
        'stderr': subprocess.PIPE,
        'text': True,
        'encoding': 'utf-8',        # 显式指定 UTF-8 编码
        'errors': 'replace',        # 遇到无法解码的字节用 � 替换，避免 UnicodeDecodeError
        'shell': False,
        'start_new_session': True,  # Unix 下创建新进程组，Windows 下创建新进程树
    }

    # Unix 下添加资源硬限制（仅当 resource 模块可用）
    if os.name == 'posix' and resource is not None:
        def set_limits():
            resource.setrlimit(resource.RLIMIT_CPU, (timeout, timeout + 10))
            resource.setrlimit(resource.RLIMIT_AS, (2 * 1024 * 1024 * 1024, 2 * 1024 * 1024 * 1024))
            resource.setrlimit(resource.RLIMIT_NPROC, (20, 20))
        popen_kwargs['preexec_fn'] = set_limits

    # ---------- 6. 启动进程并等待 ----------
    try:
        proc = subprocess.Popen([cmd_path] + safe_args, **popen_kwargs)
        stdout, stderr = proc.communicate(timeout=timeout)
        output = (stdout + stderr).strip()
        return output[:50000] if output else "(no output)"
    except subprocess.TimeoutExpired:
        # 杀死整个进程组（Unix 用 killpg，Windows 用 kill）
        if os.name == 'posix':
            try:
                pgid = os.getpgid(proc.pid)
                os.killpg(pgid, signal.SIGTERM)
                time.sleep(1)
                os.killpg(pgid, signal.SIGKILL)
            except ProcessLookupError:
                pass
        else:
            proc.kill()
        proc.wait()
        return f"Error: Timeout ({timeout}s), process group killed."
    except Exception as e:
        return f"Error: {e}"

# Backgroundmanager
class BackgroundManager:
    def __init__(self):
        self.tasks = {}  # task_id -> {status, result, command}
        self._notification_queue = []
        self._lock = threading.Lock()

    def run(self, command: str) -> str:
        """启动后台线程，立即返回 task_id"""
        framed_print(f"Tool (BACKGROUND_RUN)", f"", "success")
        task_id = str(uuid.uuid4())[:8]
        self.tasks[task_id] = {"status": "running", "result": None, "command": command}
        thread = threading.Thread(
            target=self._execute, args=(task_id, command), daemon=True
        )
        thread.start()
        return f"Background task {task_id} started: {command[:80]}"

    def _execute(self, task_id: str, command: str):
        """线程目标：执行命令，捕获输出，推入通知队列"""
        # 使用安全执行函数，超时设为 300 秒
        output = execute_background_safe(command, timeout=300)
        # 判断状态
        if output.startswith("Error:"):
            status = "error" if "Timeout" not in output else "timeout"
        else:
            status = "completed"
        self.tasks[task_id]["status"] = status
        self.tasks[task_id]["result"] = output
        with self._lock:
            self._notification_queue.append({
                "task_id": task_id,
                "status": status,
                "command": command[:80],
                "result": output[:500],
            })

    def check(self, task_id: str = None) -> str:
        """查看一个或所有任务状态"""
        framed_print(f"Tool (CHECK_BACKGROUND)", f"", "success")
        if task_id:
            t = self.tasks.get(task_id)
            if not t:
                return f"Error: Unknown task {task_id}"
            return f"[{t['status']}] {t['command'][:60]}\n{t.get('result') or '(running)'}"
        lines = []
        for tid, t in self.tasks.items():
            lines.append(f"{tid}: [{t['status']}] {t['command'][:60]}")
        return "\n".join(lines) if lines else "No background tasks."

    def drain_notifications(self) -> list:
        """返回并清空所有待处理的通知"""
        with self._lock:
            notifs = list(self._notification_queue)
            self._notification_queue.clear()
        return notifs

BG = BackgroundManager()
# ==================== 工具并发执行池 ====================
# 全局单例，避免每次 agent_loop 迭代都新建 ThreadPoolExecutor
# max_workers 同时充当「并行工具调用的并发上限」：
#   - 太小：并行收益低
#   - 太大：web_search 等易触发限流
# 推荐 3：既能利用并行，又不易被 DDGS / 第三方 API 限流
_TOOL_MAX_WORKERS = 3
_TOOL_EXECUTOR = ThreadPoolExecutor(
    max_workers=_TOOL_MAX_WORKERS,
    thread_name_prefix="baize-tool-",
)

#约定：每个钩子模块必须提供一个 register_hooks 函数，接收 HookManager 实例
def load_hooks_from_folder(folder: Path, hook_manager: HookManager, source="builtin"):
    if not folder.exists():
        return
    for file_path in folder.glob("*.py"):
        if file_path.name.startswith("_"):
            continue
        module_name = file_path.stem
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        if hasattr(module, "register_hooks"):
            # 将 source 传递给注册过程（可通过闭包或修改模块全局）
            def register_with_source(event, callback):
                hook_manager.register(event, callback, source=source)
            # 临时替换 register 方法
            original_register = hook_manager.register
            hook_manager.register = register_with_source
            module.register_hooks(hook_manager)
            hook_manager.register = original_register  # 恢复

#Hook
class HookManager:
    def __init__(self, max_workers: int = 4):
        """
        初始化 HookManager。
        :param max_workers: 线程池最大工作线程数，默认为 4。
        """
        self.hooks = {}
        self.hook_sources = {}   # 记录每个事件下回调对应的source
        self.executor = ThreadPoolExecutor(max_workers=max_workers)
        # 注册需要同步执行的事件（返回结果或必须完成再继续）
        self.sync_events = {
            'before_tool_call',
            'before_send_messages',
            'agent_loop_end',    # 若需阻塞直到测试完成
        }
        atexit.register(self.shutdown)

    def register(self, event, callback, source="builtin"):
        """
        注册一个钩子回调。
        :param event: 事件名称（如 'before_tool_call'）
        :param callback: 可调用对象
        :param source: 来源标识（'builtin' 或 'user'），默认为 'builtin'
        """
        if event not in self.hooks:
            self.hooks[event] = []
            self.hook_sources[event] = []
        self.hooks[event].append(callback)
        self.hook_sources[event].append(source)

    def unregister_by_source(self, source):
        """
        移除所有来自指定来源的回调。
        :param source: 来源标识（如 'user'）
        """
        for event in list(self.hooks.keys()):
            new_callbacks = []
            new_sources = []
            for cb, src in zip(self.hooks[event], self.hook_sources[event]):
                if src != source:
                    new_callbacks.append(cb)
                    new_sources.append(src)
            self.hooks[event] = new_callbacks
            self.hook_sources[event] = new_sources
            if not self.hooks[event]:
                del self.hooks[event]
                del self.hook_sources[event]

    def trigger(self, event, *args, **kwargs):
        """触发钩子，根据事件类型决定同步或异步执行。"""
        callbacks = self.hooks.get(event, [])
        if not callbacks:
            return None

        # 同步事件：立即执行，并返回第一个非空结果（如拒绝决策）
        if event in self.sync_events:
            for cb in callbacks:
                try:
                    result = cb(*args, **kwargs)
                    # 对于 before_tool_call，如果返回拒绝字典，立即返回
                    if event == 'before_tool_call' and result and result.get('decision') == 'deny':
                        return result
                except Exception as e:
                    logging.error(f"Hook error on {event}: {e}")
            return None

        # 异步事件：提交到线程池，不等待
        for cb in callbacks:
            self.executor.submit(self._safe_run, cb, event, *args, **kwargs)
        return None

    def _safe_run(self, cb, event, *args, **kwargs):
        """包装异步回调，捕获异常并记录。"""
        try:
            cb(*args, **kwargs)
        except Exception as e:
            logging.error(f"Async hook error on {event}: {e}")

    def shutdown(self, wait=True):
        """关闭线程池，等待所有任务完成(若 wait=True)。"""
        self.executor.shutdown(wait=wait)

HOOK = HookManager(max_workers=4)

#定义交互管理类
class InteractionManager:
    def __init__(self):
        self._pending_requests = {}  # request_id -> {"event": Event, "response": None}
        self._next_id = 0
        self._lock = threading.Lock()
        self.callback = None

    def set_callback(self, callback):
        self.callback = callback

    def _get_id(self):
        with self._lock:
            self._next_id += 1
            return self._next_id

    def ask_user(self, question, options=None, context=None, timeout=60):
        req_id = self._get_id()
        event = threading.Event()
        self._pending_requests[req_id] = {"event": event, "response": None}
        if self.callback:
            self.callback({
                "type": "ask_user",
                "request_id": req_id,
                "question": question,
                "options": options,
                "context": context
            })
        if not event.wait(timeout):
            # 超时，清理并返回
            self._pending_requests.pop(req_id, None)
            return "(timeout)"
        response = self._pending_requests[req_id]["response"]
        self._pending_requests.pop(req_id, None)
        return response

    def submit_response(self, request_id, response):
        if request_id in self._pending_requests:
            self._pending_requests[request_id]["response"] = response
            self._pending_requests[request_id]["event"].set()

# 创建全局交互管理器实例
INTERACTION = InteractionManager()


# 工具调用与功能定义
def safe_path(p: str) -> Path:
    path = (CURRENT_WORKDIR / p).resolve()
    # 使用 os.path.commonpath 判断前缀（跨平台）
    try:
        common = os.path.commonpath([str(path), str(CURRENT_WORKDIR)])
        if common != str(CURRENT_WORKDIR):
            raise ValueError(f"Path escapes workspace: {p}")
    except ValueError:
        # 在不同盘符时 commonpath 会抛异常，视为逃逸
        raise ValueError(f"Path escapes workspace: {p}")
    return path

# 新增safe辅助函数
def _is_path_safe(abs_path: str) -> bool:
    """统一的路径安全校验"""
    p = Path(abs_path).resolve()
    try:
        if not p.is_relative_to(CURRENT_WORKDIR) and not p.is_relative_to(Path("/tmp")):
            return False
    except ValueError:
        return False
    for pattern in FORBIDDEN_PATH_PATTERNS:
        if re.search(pattern, str(p)):
            return False
    return True

def run_read(path: str, limit: int = None) -> str:
    try:
        text = safe_path(path).read_text(encoding='utf-8')
        lines = text.splitlines()
        if limit and limit < len(lines):
            lines = lines[:limit] + [f"... ({len(lines) - limit} more lines)"]
        framed_print(f"Tool (RUN_READ):{path}", f"", "success")
        return "\n".join(lines)[:50000]
    except Exception as e:
        framed_print("Readfile error", f'{e}\nRetrying...', "warning")
        return f"Error: {e}"

#增加 Diff 预览，会被write和edit调用 ---- 呈现代码变化
def _confirm_with_diff(file_path: str, old_content: str, new_content: str) -> bool:
    """生成 diff 并请求用户确认，带颜色区分增删"""
    if old_content == new_content:
        return True  # 无变化，直接跳过
    old_lines = old_content.splitlines(keepends=True)
    new_lines = new_content.splitlines(keepends=True)
    diff = difflib.unified_diff(
        old_lines, new_lines,
        fromfile=f'a/{file_path}',
        tofile=f'b/{file_path}',
        lineterm=''
    )
    diff_lines = [line.rstrip('\n') for line in diff]  # 去掉换行符，便于逐行控制
    if not diff_lines:
        print("\n(无变化)")
        return True
    print("\n" + "=" * 50)
    print(f"即将修改文件: {file_path}")
    print("变更内容如下 (Diff):")
    print("-" * 40)
    GREEN = "\033[92m"   # 绿色（新增行）
    RED = "\033[91m"     # 红色（删除行）
    RESET = "\033[0m"    # 重置颜色
    for line in diff_lines:
        if line.startswith('+'):
            # 行首 '+' 保持白色，后续内容绿色
            sys.stdout.write(RESET + '+' + GREEN + line[1:] + RESET + '\n')
        elif line.startswith('-'):
            # 行首 '-' 保持白色，后续内容红色
            sys.stdout.write(RESET + '-' + RED + line[1:] + RESET + '\n')
        else:
            # 其他行（如 @@, ---, +++）原样输出
            sys.stdout.write(line + '\n')
    sys.stdout.flush()   # 确保立即输出
    print("-" * 40)
    # 用户确认交互（原逻辑不变）
    while True:
        resp = input("确认写入? (y/n/e - 编辑新内容): ").strip().lower()
        if resp == 'y':
            return True
        elif resp == 'n':
            return False
        elif resp == 'e':
            print("请修改提示词后重新执行写入。")
            return False
        else:
            print("请输入 y(确认), n(拒绝), e(编辑)")

def run_write(path: str, content: str) -> str:
    try:
        fp = safe_path(path)
        fp.parent.mkdir(parents=True, exist_ok=True)
        old_content = ""
        if fp.exists():
            old_content = fp.read_text(encoding='utf-8')
            # 调用确认函数
            if not _confirm_with_diff(path, old_content, content):
                return "Write operation cancelled by user."
        
        fp.write_text(content, encoding='utf-8')
        framed_print(f"Tool (RUN_WRITE):{path}", content, "success")
        return f"Wrote {len(content)} bytes to {path}"
    except Exception as e:
        framed_print("Writefile error", f'{e}\nRetrying...', "warning")
        return f"Error: {e}"

def run_edit(path: str, old_text: str, new_text: str) -> str:
    """
    编辑文件：用 new_text 替换 old_text（仅当 old_text 在文件中唯一出现时）。
    修改前会通过 Diff 提示用户确认。
    """
    try:
        fp = safe_path(path)
        if not fp.exists():
            return f"Error: File '{path}' does not exist."
        old_content = fp.read_text(encoding='utf-8')
        # 1. 检查 old_text 出现次数（唯一性）
        count = old_content.count(old_text)
        if count == 0:
            return f"Error: Text not found in {path}"
        if count > 1:
            # 提供帮助信息，列出前5个匹配行号
            lines = old_content.splitlines()
            positions = []
            for i, line in enumerate(lines, 1):
                if old_text in line:
                    positions.append(str(i))
                    if len(positions) >= 5:
                        break
            return (f"Error: Found {count} occurrences of the text in {path}. "
                    f"It must appear exactly once. Occurrences found at lines: {', '.join(positions)}. "
                    f"Please provide more context (larger old_text block) to make it unique.")
        # 2. 唯一匹配 → 生成新内容
        new_content = old_content.replace(old_text, new_text, 1)
        # 3. 调用 Diff 确认（如果内容没变，_confirm_with_diff 直接返回 True）
        if not _confirm_with_diff(path, old_content, new_content):
            return "Edit cancelled by user."
        # 4. 写入文件
        fp.write_text(new_content, encoding='utf-8')
        framed_print(f"Tool (RUN_EDIT):{path}", f"Replaced 1 occurrence", "success")
        return f"Edited {path} (1 occurrence replaced)"
    except Exception as e:
        framed_print("Editfile error", f'{e}', "warning")
        return f"Error: {e}"

#Bash调用部分
# 禁止访问的路径模式
def is_path_allowed(path: str) -> bool:
    if not path.startswith('/'):
        return True
    resolved = os.path.realpath(path)
    if resolved.startswith(str(CURRENT_WORKDIR)):
        return True
    if resolved.startswith("/tmp/"):
        return True
    for pattern in FORBIDDEN_PATH_PATTERNS:
        if re.search(pattern, resolved):
            return False
    return False

# 命令安全执行函数（供同步和后台统一使用）
def execute_command_safe(command: str, timeout: int = 120) -> str:
    """
    安全执行 bash 命令(shell=False 模式)
    脚本引擎动态代码执行拦截（防 python -c 'os.system(...)' 等绕过）
    """
    # 1. 解析命令为列表
    try:
        parts = shlex.split(command)
    except ValueError:
        return "Error: Invalid command syntax"
    if not parts:
        return "Error: Empty command"
    # 2. 提取真实命令名（处理路径如 /usr/bin/ls）
    cmd_path = parts[0]
    cmd_name = os.path.basename(cmd_path)
    # 3. 白名单检查（严格匹配命令名）
    if cmd_name not in ALLOWED_COMMANDS:
        return f"Error: Command '{cmd_name}' is not allowed. Allowed: {', '.join(sorted(ALLOWED_COMMANDS))}"
    # 4. 强制危险字符拦截（即便在参数中，也拦截管道、重定向、子shell）
    # 注意：由于使用 shell=False，管道 | 和重定向 > 会失效，但我们仍需拦截避免混淆
    dangerous_chars = re.search(r'[;&`$()|<>]', command)
    if dangerous_chars:
        return f"Error: Forbidden shell metacharacters found: {dangerous_chars.group()}"
    # 5. 路径参数安全检查（遍历所有参数，解析绝对路径）
    safe_args = []
    for arg in parts[1:]:
        # 忽略纯粹的选项标志（如 -la, --force）
        if arg.startswith('-'):
            safe_args.append(arg)
            continue
        # 处理 --file=path 格式
        if arg.startswith('--') and '=' in arg:
            key, val = arg.split('=', 1)
            # 只检查值部分是否为路径
            if '/' in val or val in ('.', '..'):
                abs_path = os.path.realpath(os.path.join(str(CURRENT_WORKDIR), val))
                if not _is_path_safe(abs_path):
                    return f"Error: Access to '{val}' (resolved: {abs_path}) is not allowed"
                safe_args.append(f"{key}={val}")
            else:
                safe_args.append(arg)
            continue
         # 普通路径参数
        if '/' in arg or arg in ('.', '..'):
            if not arg.startswith('/'):
                abs_path = os.path.realpath(os.path.join(str(CURRENT_WORKDIR), arg))
            else:
                abs_path = os.path.realpath(arg)
            if not _is_path_safe(abs_path):
                return f"Error: Access to '{arg}' (resolved: {abs_path}) is not allowed"
            safe_args.append(arg)
        else:
            safe_args.append(arg)
    # ========== 脚本引擎动态代码执行拦截 ==========
    # 针对常见的脚本引擎，检测 -c/-e 参数中是否包含危险的动态执行函数
    SCRIPT_ENGINES = {'python', 'python3', 'bash', 'sh', 'node', 'ruby'}
    if cmd_name in SCRIPT_ENGINES:
        args_str = ' '.join(safe_args)
        # 检测是否使用了 -c 或 -e 参数（通常用于执行代码字符串）
        if re.search(r' -c\s+["\']', args_str) or re.search(r' -e\s+["\']', args_str):
            # 检测危险函数调用（os.system, subprocess, exec, eval, __import__）
            if re.search(r'(os\.system|subprocess\.|exec\(|eval\(|__import__)', args_str, re.IGNORECASE):
                return "Error: Dynamic code execution in script engine detected and blocked."
    # 6. 执行（使用列表模式，彻底关闭 shell）
    try:
        r = subprocess.run(
            [cmd_path] + safe_args,  # 这里必须是列表！
            cwd=str(CURRENT_WORKDIR),
            capture_output=True,
            text=True,
            encoding='utf-8',          # 新增
            errors='replace',          # 新增，无法解码的字节替换为 �
            timeout=timeout,
            env=os.environ.copy(),   # 继承环境变量，但可考虑剥离敏感变量
            shell=False              # 核心修复点
        )
        out = (r.stdout + r.stderr).strip()
        return out[:50000] if out else "(no output)"
    except subprocess.TimeoutExpired:
        return f"Error: Timeout ({timeout}s)"
    except Exception as e:
        return f"Error: {e}"

# 原 run_bash 改为调用通用函数
def run_bash(command: str) -> str:
    result = execute_command_safe(command, timeout=120)
    framed_print("Tool (RUN_BASH)", command, "success")
    return result

#glob工具调用
def run_glob(pattern: str) -> str:
    """返回匹配 glob 模式的文件列表（相对路径）"""
    try:
        # 使用 Path.glob，但需要确保不会逃逸
        matched = []
        for p in CURRENT_WORKDIR.glob(pattern):
            if p.is_file():
                try:
                    rel = p.relative_to(CURRENT_WORKDIR)
                    matched.append(str(rel))
                except ValueError:
                    continue   # 跳过不在工作目录内的文件
        if not matched:
            return "(no matches)"
        output = "\n".join(matched[:200])
        if len(matched) > 200:
            output += f"\n... and {len(matched)-200} more"
        framed_print("Tool (RUN_GLOB)", f"Pattern: {pattern}", "success")
        return output
    except Exception as e:
        return f"Error: {e}"

#grep工具调用
def run_grep(pattern: str, path: str = ".", case_sensitive: bool = True) -> str:
    """在文件或目录中递归搜索文本（正则）"""
    try:
        target = (CURRENT_WORKDIR / path).resolve()
        if not target.is_relative_to(CURRENT_WORKDIR):
            return f"Error: Path '{path}' escapes workspace"
        if not target.exists():
            return f"Error: Path '{path}' does not exist"

        flags = 0 if case_sensitive else re.IGNORECASE
        regex = re.compile(pattern, flags)
        matches = []
        max_results = 100
        max_lines_per_file = 10

        if target.is_file():
            files = [target]
        else:
            # 递归遍历文件（跳过隐藏目录？默认不过滤）
            files = [f for f in target.rglob('*') if f.is_file() and not f.is_symlink()]

        for file in files:
            if len(matches) >= max_results:
                break
            try:
                content = file.read_text(encoding='utf-8', errors='ignore')
                lines = content.splitlines()
                # 只取前 max_lines_per_file 个匹配行，避免输出过大
                matched_lines = []
                for i, line in enumerate(lines, 1):
                    if regex.search(line):
                        rel_path = str(file.relative_to(CURRENT_WORKDIR))
                        matched_lines.append(f"{rel_path}:{i}:{line.strip()[:200]}")
                        if len(matched_lines) >= max_lines_per_file:
                            matched_lines.append(f"... (more matches in {rel_path})")
                            break
                matches.extend(matched_lines[:max_results - len(matches)])
            except Exception:
                continue

        if not matches:
            result = "(no matches)"
        else:
            result = "\n".join(matches[:max_results])
        framed_print("Tool (RUN_GREP)", f"Pattern: {pattern}, Path: {path}", "success")
        return result
    except Exception as e:
        return f"Error: {e}"

# Web Search
def run_web_search(query: str, max_results: int = 5) -> str:
    """
    使用 DuckDuckGo 进行网络搜索，返回摘要信息。
    """
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=max_results))
        if not results:
            return "No results found."

        output_lines = []
        for i, r in enumerate(results, 1):
            title = r.get('title', 'No title')
            body = r.get('body', 'No snippet')
            url = r.get('href', 'No URL')
            output_lines.append(f"{i}. {title}\n   {body[:200]}{'...' if len(body)>200 else ''}\n   URL: {url}")
        result_text = "\n\n".join(output_lines)
        framed_print("Tool (WEB_SEARCH)", f"Query: {query}", "success")
        return result_text[:50000]  # 限制输出长度
    except Exception as e:
        framed_print("Web search error", f"{e}", "warning")
        return f"Error performing web search: {e}"

# Web Fetch 抓取网页内容
def run_webfetch(url: str, max_length: int = 10000) -> str:
    """
    抓取网页并提取纯文本内容。
    - 只允许 http/https 协议
    - 超时 15 秒
    - 提取 body 中的所有文本，并压缩空白
    """
    if not url.startswith(('http://', 'https://')):
        return "Error: URL must start with http:// or https://"

    hostname = urlparse(url).hostname
    if not hostname:
        return "Error: URL must contain a valid hostname"
    try:
        resolved_ips = {info[4][0] for info in socket.getaddrinfo(hostname, None)}
    except socket.gaierror as e:
        return f"Error resolving URL host: {e}"
    for ip in resolved_ips:
        addr = ipaddress.ip_address(ip)
        if not addr.is_global or addr.is_multicast:
            return "Error: URL resolves to a disallowed private/internal address"

    try:
        response = requests.get(url, timeout=15, headers={
            'User-Agent': 'Mozilla/5.0 (compatible; MyAgent/1.0)'
        })
        response.raise_for_status()
        # 尝试按 charset 解码，或使用 apparent_encoding
        if response.encoding is None:
            response.encoding = 'utf-8'
        html = response.text
    except requests.exceptions.RequestException as e:
        return f"Error fetching URL: {e}"

    try:
        soup = BeautifulSoup(html, 'html.parser')
        # 移除 script, style 等非内容标签
        for tag in soup(['script', 'style', 'nav', 'footer', 'header']):
            tag.decompose()
        text = soup.get_text(separator='\n', strip=True)
        # 压缩多余空白行
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        text = '\n'.join(lines)
    except Exception as e:
        return f"Error parsing HTML: {e}"

    if len(text) > max_length:
        text = text[:max_length] + "\n... (truncated)"
    framed_print("Tool (RUN_WEBFETCH)", f"URL: {url}", "success")
    return text

# AskUserQuestion
def ask_user_question(question: str, options: list = None, context: str = None, timeout: int = 60) -> str:
    """
    向用户提问并等待输入，支持超时。
    - 如果设置了交互回调（WebSocket模式），则通过回调发送请求并异步等待响应。
    - 否则回退到命令行模式（使用 input()，支持超时）。
    - 如果提供了 options，则显示选项编号，用户可输入数字选择或自由输入文本。
    - 如果未提供 options，用户直接输入任意文本。
    - 超时返回 "(timeout)"。
    """
    # 如果有交互管理器且设置了回调，则使用异步方式
    if INTERACTION.callback:
        return INTERACTION.ask_user(question, options, context, timeout)

    framed_print("Tool (ASK_USER)", question, "info")
    if context:
        print(f"Context: {context}")
    if options:
        print("Options:")
        for i, opt in enumerate(options, 1):
            print(f"  {i}. {opt}")
        print("Enter the number or your own answer:")
    else:
        print("Please enter your response:")

    # 使用队列和线程实现超时输入
    q = queue.Queue()

    def get_input():
        try:
            ans = input("> ")
            q.put(ans)
        except Exception:
            q.put("")   # 异常时返回空字符串

    t = threading.Thread(target=get_input, daemon=True)
    t.start()

    try:
        user_input = q.get(timeout=timeout)
    except queue.Empty:
        print("\n[Timeout] No response within {} seconds.".format(timeout))
        return "(timeout)"

    # 处理用户输入（与原来逻辑相同）
    if not user_input:
        return "(empty)"
        
    if options:
        # 尝试解析为数字选项
        try:
            idx = int(user_input) - 1
            if 0 <= idx < len(options):
                return options[idx]
            else:
                print(f"Invalid number. Please enter a number between 1 and {len(options)}.")
                # 若无效，可递归调用或返回原输入；这里简单返回原输入（但会丢失选项约束）
                # 更友好：可在此处重新提问，但为保持简单，直接返回用户输入
                return user_input
        except ValueError:
            # 不是数字，视为自定义输入
            return user_input
    else:
        return user_input
        
#skill工具调用
def load_skills(name: str) -> str:
    return SKILL_LOADER.get_content(name)

#动态切换当前工作目录，并同步更新代理所依赖的所有用户自定义资源（技能、子代理、钩子、MCP 配置）
def set_workspace(path: str) -> str:
    """
    更改当前工作目录，后续所有文件操作和 bash 命令将在新目录下执行。
    切换后会重新加载用户工作区下的自定义资源（技能、子代理、钩子、MCP 配置），
    内置资源（项目根目录下的同名文件夹）保持最高优先级。
    """
    global CURRENT_WORKDIR, _GIT_COMMITTED_FLAG
    try:
        new_path = Path(path).expanduser().resolve()
    except Exception as e:
        return f"Error: Invalid path - {e}"
    if not new_path.exists():
        return f"Error: Path '{path}' does not exist"
    if not new_path.is_dir():
        return f"Error: Path '{path}' is not a directory"
    # 1. 更新工作目录
    with workdir_lock:
        CURRENT_WORKDIR = new_path
    # 2. 重新加载用户资源（技能、子代理、钩子、MCP）
    reload_user_resources()
    # 3. 重置 Git 提交标志（新项目允许提交）
    _GIT_COMMITTED_FLAG = False
    # 注意：不要在 set_workspace 里替换 SESSION_HISTORY。
    # set_workspace 是作为工具在 agent_loop 中间被调用的，SESSION_HISTORY 与 agent_loop 的
    # messages 是同一个列表对象；若在这里原地清空/重载，会把刚追加的 assistant(tool_calls)
    # 消息抹掉，导致随后追加的 tool 结果消息失去对应的 tool_calls，触发 DeepSeek 400：
    # "Messages with role 'tool' must be a response to a preceding message with 'tool_calls'"。
    # 会话历史的保存与加载统一由主循环负责。

    framed_print("Tool (SET_WORKSPACE)", f"Switched to {CURRENT_WORKDIR}", "success")
    return f"Workspace changed to {CURRENT_WORKDIR}"

#把外部依赖注入给 history.auto_compact：（自动压缩两级，供 agent_loop 调用）
def auto_compact(messages, callback=None):
    """薄封装：把 Baize 的全局依赖注入到 agent.core.history.auto_compact。"""
    return _auto_compact_impl(
        messages,
        send_fn=send_messages,
        transcript_dir=get_transcript_dir(),
        hook_trigger=HOOK.trigger,
        callback=callback,
    )

# TaskManager任务管理工具函数（供 agent_loop 调用）
def task_create(subject: str, description: str = "") -> str:
    return TASKS.create(subject, description)

def task_update(task_id: int, status: str = None, addBlockedBy: list = None, addBlocks: list = None) -> str:
    return TASKS.update(task_id, status, addBlockedBy, addBlocks)

def task_list() -> str:
    return TASKS.list_all()

def task_get(task_id: int) -> str:
    return TASKS.get(task_id)

#新增钩子实现
#Shell命令的Hook埋点
def run_shell_hooks(event: str, data: dict) -> dict | None:
    """
    执行 hooks/ 目录下匹配的 Shell 钩子脚本。
    event: 'PreToolUse', 'PostToolUse', 'Stop'
    data: 传递给脚本的 JSON 数据（将作为 stdin）
    返回: 如果任一脚本拒绝，返回 {'decision':'deny','reason':'...'}，否则返回 None
    """
    hooks_dir = CURRENT_WORKDIR / "hooks"
    if not hooks_dir.exists():
        return None

    # 匹配命名模式: <事件名>-*.sh，例如 PreToolUse-*.sh
    scripts = list(hooks_dir.glob(f"{event}-*.sh"))
    if not scripts:
        return None

    input_json = json.dumps(data, ensure_ascii=False)

    for script in scripts:
        # ----- 路径安全检查 -----
        script_path = script.resolve()
        # 确保脚本在 WORKDIR/hooks 目录下（防止符号链接逃逸）
        try:
            if not script_path.is_relative_to(CURRENT_WORKDIR / "hooks"):
                print(f"[Shell hook] Skipping {script_path}: not under hooks directory")
                continue
        except ValueError:
            # is_relative_to 可能抛出 ValueError（如路径不同盘符）
            print(f"[Shell hook] Skipping {script_path}: cannot determine relative path")
            continue

        if not script_path.exists():
            continue
        # 执行脚本
        try:
            proc = subprocess.run(
                [str(script)],
                input=input_json,
                text=True,
                capture_output=True,
                timeout=10,
                cwd=str(CURRENT_WORKDIR),
                encoding='utf-8',
                errors='replace'
            )
            # 解析 stdout（可能是 JSON）
            if proc.stdout.strip():
                try:
                    output = json.loads(proc.stdout)
                    hook_spec = output.get('hookSpecificOutput', {})
                    if hook_spec.get('permissionDecision') == 'block':
                        reason = hook_spec.get('permissionDecisionReason', 'Denied by shell hook')
                        return {'decision': 'block', 'reason': reason}
                except json.JSONDecodeError:
                    # 忽略非 JSON 输出（如调试信息）
                    pass
        except Exception as e:
            print(f"[Shell hook error] {script}: {e}")
            # 继续执行下一个脚本
    return None

#敏感文件保护
def hook_sensitive_file_protection(tool_call):   
    if tool_call.function.name not in ('run_write', 'run_edit'):
        return None
    args = json.loads(tool_call.function.arguments)
    file_path = args.get('path', '')
    if not file_path:
        return None
    resolved = (CURRENT_WORKDIR / file_path).resolve()
    # 检查是否在受保护目录下（直接比较父目录）
    protected_dirs = ['.git', '.ssh', 'node_modules']
    for part in resolved.parts:
        if part in protected_dirs:
            return {
                'decision': 'deny',
                'reason': f'不允许修改受保护目录中的文件: {part}'
            }
    protected_files = {'.env', '.env.local', 'credentials.json', 'secrets.yaml', 'id_rsa', 'id_ed25519'}
    if resolved.name in protected_files:
        return {
            'decision': 'deny',
            'reason': f'不允许修改敏感文件: {resolved.name}'
        }
    protected_exts = {'.pem', '.key', '.p12', '.pfx'}
    if resolved.suffix in protected_exts:
        return {
            'decision': 'deny',
            'reason': f'不允许修改密钥类文件: {resolved.suffix}'
        }
    return None

#危险命令拦截模式
def hook_dangerous_command(tool_call):  
    if tool_call.function.name != 'run_bash':
        return None
    args = json.loads(tool_call.function.arguments)
    command = args.get('command', '')
    dangerous_patterns = [
        r"rm\s+-rf\s+/*",              # rm -rf /
        r"rm\s+-rf\s+~",               # rm -rf ~
        r"rm\s+-rf\s+\$HOME",
        r">\s*/dev/sd[a-z]",           # 覆盖磁盘设备
        r"mkfs\.",
        r":\(\)\{\s*:\|\s*:&\s*\};\s*:", # fork bomb
        r"chmod\s+-R\s+777\s+/",
        r"git\s+push\s+--force\s+origin\s+(main|master)",
        r"git\s+reset\s+--hard\s+origin",
        r"DROP\s+DATABASE",
        r"DROP\s+TABLE",
        r"TRUNCATE\s+",
        r"curl\s+.*\|\s*(sh|bash)",    # curl | sh
        r"wget\s+.*\|\s*(sh|bash)",
        r"sudo\s+.*(rm|mkfs|dd|shred)", # 带 sudo 的危险操作
        r"rm\s+-rf\s+\*",              # rm -rf *
        r"rm\s+-rf\s+\.",              # rm -rf .
        r"dd\s+if=.*of=/dev/sd[a-z]",  # dd 写入磁盘
        r">\s*/etc/passwd",            # 重定向覆盖系统文件
    ]
    for pattern in dangerous_patterns:
        if re.search(pattern, command, re.IGNORECASE):
            return {
                'decision': 'deny',
                'reason': f'拦截危险命令模式: {pattern}'
            }
    return None

#记录每一次工具调用的审计日志
def hook_audit_log(tool_call, result):
    """PostToolUse 等价：记录审计日志"""
    log_dir = CURRENT_WORKDIR / ".claude/logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / f"audit-{datetime.now().strftime('%Y-%m-%d')}.log"
    timestamp = datetime.now().isoformat()
    tool_name = tool_call.function.name
    tool_input = tool_call.function.arguments
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(f"[{timestamp}] {tool_name}: {tool_input} -> {result[:200]}\n")

#注册在 after_tool_call 事件上的内置钩子，其作用是在代理修改文件后，自动调用代码格式化工具对文件进行美化
def hook_auto_format(tool_call, result):
    """PostToolUse 等价：自动格式化修改的文件"""
    if tool_call.function.name not in ('run_write', 'run_edit'):
        return
    args = json.loads(tool_call.function.arguments)
    file_path = args.get('path', '')
    if not file_path or not (CURRENT_WORKDIR / file_path).exists():
        return
    resolved = CURRENT_WORKDIR / file_path
    ext = resolved.suffix[1:]
    # 根据扩展名调用对应的格式化工具
    if ext in ('js', 'jsx', 'ts', 'tsx', 'json', 'md', 'css', 'scss', 'html'):
        if shutil.which('npx') and (CURRENT_WORKDIR / 'package.json').exists():
            try:
                subprocess.run(['npx', 'prettier', '--write', str(resolved)],
                                cwd=str(CURRENT_WORKDIR), check=False, capture_output=True,
                                encoding='utf-8', errors='replace')
                print(f"[Format] Prettier formatted {file_path}")
            except Exception:
                pass
    elif ext == 'py':
        if shutil.which('black'):
            try:
                subprocess.run(['black', str(resolved)], check=False, capture_output=True)
                print(f"[Format] Black formatted {file_path}")
            except Exception:
                pass
    elif ext == 'go':
        if shutil.which('gofmt'):
            try:
                subprocess.run(['gofmt', '-w', str(resolved)], check=False, capture_output=True)
                print(f"[Format] gofmt formatted {file_path}")
            except Exception:
                pass

#注册在 after_tool_call 事件上的内置钩子，其作用是在代理修改 JavaScript/TypeScript 文件后，自动静默运行 ESLint 进行代码质量检查
def hook_lint_feedback(tool_call, result):
    """PostToolUse 等价：对 JS/TS 文件运行 ESLint 并附加反馈"""
    if tool_call.function.name not in ('run_write', 'run_edit'):
        return
    args = json.loads(tool_call.function.arguments)
    file_path = args.get('path', '')
    if not file_path:
        return
    resolved = CURRENT_WORKDIR / file_path
    ext = resolved.suffix[1:]
    if ext in ('js', 'jsx', 'ts', 'tsx') and (CURRENT_WORKDIR / 'package.json').exists():
        if shutil.which('npx'):
            try:
                proc = subprocess.run(['npx', 'eslint', str(resolved)],
                                      cwd=str(CURRENT_WORKDIR), capture_output=True, text=True, check=False)
                if proc.returncode != 0:
                    lint_output = proc.stdout + proc.stderr
                    # 将 lint 结果作为额外上下文注入（可考虑推入消息队列）
                    # 这里简单打印，或可追加到某个全局变量供后续对话使用
                    print(f"[Lint] Issues found in {file_path}:\n{lint_output[:500]}")
                    # 我们可以在 agent_loop 中检查此结果并反馈给用户，但此处不阻塞
            except Exception:
                pass

# 测试门控钩子
def hook_test_gate(*args, **kwargs):
    """
    在 Agent 结束前运行测试，返回决策。
    若测试失败，返回 {'decision':'block', 'reason':'...', 'details':'...'}
    否则返回 {'decision':'allow'}
    """
    # 检测测试框架并运行，如果失败返回 block 决策
    if (CURRENT_WORKDIR / 'package.json').exists():
        try:
            result = subprocess.run(['npm', 'test'], cwd=str(CURRENT_WORKDIR), capture_output=True, text=True, check=False)
            if result.returncode != 0:
                return {'decision': 'block', 'reason': '测试失败', 'details': result.stdout[:500]}
        except FileNotFoundError:
            pass
    elif (CURRENT_WORKDIR / 'pyproject.toml').exists() or (CURRENT_WORKDIR / 'pytest.ini').exists():
        try:
            result = subprocess.run(['pytest'], cwd=str(CURRENT_WORKDIR), capture_output=True, text=True, check=False)
            if result.returncode != 0:
                return {'decision': 'block', 'reason': '测试失败', 'details': result.stdout[:500]}
        except FileNotFoundError:
            pass
    elif (CURRENT_WORKDIR / 'go.mod').exists():
        try:
            result = subprocess.run(['go', 'test', './...'], cwd=str(CURRENT_WORKDIR), capture_output=True, text=True, check=False)
            if result.returncode != 0:
                return {'decision': 'block', 'reason': '测试失败', 'details': result.stdout[:500]}
        except FileNotFoundError:
            pass

# ==================== 会话持久化方案  ====================
def save_session(workdir: Path = None, commit_to_git: bool = False):
    """
    保存当前 SESSION_HISTORY（不含系统消息）到 .baize_session.json，
    并可选提交到 Git。
    commit_to_git=True 仅在未提交过且为 Git 仓库时执行一次提交。
    """
    global _GIT_COMMITTED_FLAG
    if workdir is None:
        workdir = CURRENT_WORKDIR

    # 提取非系统消息
    non_system = [msg for msg in SESSION_HISTORY if msg.get("role") != "system"]
    session_file = workdir / ".baize_session.json"

    # 1) 实时写入 JSON（保证崩溃恢复）
    try:
        with open(session_file, 'w', encoding='utf-8') as f:
            json.dump(non_system, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"[系统] 保存会话失败: {e}")
        return

    # 2) 若要求提交 Git 且未提交过
    if commit_to_git and not _GIT_COMMITTED_FLAG:
        git_dir = workdir / ".git"
        if not git_dir.exists():
            return  # 不是 Git 仓库，静默跳过

        try:
            # 添加文件
            subprocess.run(
                ["git", "add", str(session_file)],
                cwd=str(workdir),
                check=True,
                capture_output=True,
                encoding='utf-8',
                errors='replace'
            )
            # 提交（带时间戳）
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
            subprocess.run(
                ["git", "commit", "-m", f"chore(baize): update session ({timestamp})"],
                cwd=str(workdir),
                check=True,
                capture_output=True
            )
            _GIT_COMMITTED_FLAG = True
            print(f"[系统] 会话已提交到 Git ({workdir})")
        except subprocess.CalledProcessError as e:
            # 若 "nothing to commit" 则忽略
            stderr = e.stderr.decode()
            if "nothing to commit" not in stderr:
                print(f"[系统] Git 提交失败: {stderr}")
        except Exception as e:
            print(f"[系统] Git 提交异常: {e}")

def load_session(workdir: Path) -> list:
    """从 .baize_session.json 加载历史（不含系统消息），若文件不存在返回空列表"""
    session_file = workdir / ".baize_session.json"
    if session_file.exists():
        try:
            with open(session_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            sanitize_history(data)  # 修复历史中断导致的悬空 tool_calls
            return data
        except Exception as e:
            print(f"[系统] 加载会话失败: {e}")
            return []
    return []

def commit_on_exit():
    """程序正常退出时自动调用，提交最终状态"""
    global _GIT_COMMITTED_FLAG
    if SESSION_HISTORY:
        save_session(CURRENT_WORKDIR, commit_to_git=True)

#提取工具分发函数(_dispatch_tool 是代理系统中“工具名称到工具逻辑”的映射表，使得主循环无需关心具体工具的实现细节，只需通过函数名即可动态执行对应的操作) 
def _dispatch_tool(tool_call):
    """根据工具名称执行对应函数，返回结果字符串"""
    if tool_call.function.name == "run_bash":
        arguments_dict = json.loads(tool_call.function.arguments)
        return run_bash(arguments_dict['command'])
    elif tool_call.function.name == "set_workspace":
        args = json.loads(tool_call.function.arguments)
        return set_workspace(args['path'])
    elif tool_call.function.name == "run_read":
        arguments_dict = json.loads(tool_call.function.arguments)
        return run_read(arguments_dict['path'], arguments_dict.get('limit'))
    elif tool_call.function.name == "run_write":
        arguments_dict = json.loads(tool_call.function.arguments)
        return run_write(arguments_dict['path'], arguments_dict['content'])
    elif tool_call.function.name == "run_edit":
        arguments_dict = json.loads(tool_call.function.arguments)
        return run_edit(arguments_dict['path'], arguments_dict['old_text'], arguments_dict['new_text'])
    elif tool_call.function.name == "run_glob":
        arguments_dict = json.loads(tool_call.function.arguments)
        return run_glob(arguments_dict['pattern'])
    elif tool_call.function.name == "run_grep":
        arguments_dict = json.loads(tool_call.function.arguments)
        return run_grep(
            arguments_dict['pattern'],
            arguments_dict.get('path', '.'),
            arguments_dict.get('case_sensitive', True)
        )
    elif tool_call.function.name == "web_search":
        arguments_dict = json.loads(tool_call.function.arguments)
        return run_web_search(
            arguments_dict['query'],
            arguments_dict.get('max_results', 5)
        )
    elif tool_call.function.name == "run_webfetch":
        args = json.loads(tool_call.function.arguments)
        return run_webfetch(args['url'], args.get('max_length', 10000))
    elif tool_call.function.name == "load_skills":
        arguments_dict = json.loads(tool_call.function.arguments)
        return load_skills(arguments_dict['name'])
    elif tool_call.function.name == "agent":
        arguments_dict = json.loads(tool_call.function.arguments)
        subagent_name = arguments_dict.get('subagent', 'default')
        return run_subagent(arguments_dict['prompt'], subagent_name)
    elif tool_call.function.name == "task_create":
        arguments_dict = json.loads(tool_call.function.arguments)
        return task_create(arguments_dict['subject'], arguments_dict.get('description', ''))
    elif tool_call.function.name == "task_update":
        arguments_dict = json.loads(tool_call.function.arguments)
        return task_update(arguments_dict['task_id'],
                           arguments_dict.get('status'),
                           arguments_dict.get('addBlockedBy'),
                           arguments_dict.get('addBlocks'))
    elif tool_call.function.name == "task_list":
        return task_list()
    elif tool_call.function.name == "task_get":
        arguments_dict = json.loads(tool_call.function.arguments)
        return task_get(arguments_dict['task_id'])
    elif tool_call.function.name == "todo":
        arguments_dict = json.loads(tool_call.function.arguments)
        return TODO.update(arguments_dict['items'])
    elif tool_call.function.name == "background_run":
        args = json.loads(tool_call.function.arguments)
        return BG.run(args['command'])
    elif tool_call.function.name == "check_background":
        args = json.loads(tool_call.function.arguments)
        return BG.check(args.get('task_id'))
    elif tool_call.function.name == "ask_user_question":
        args = json.loads(tool_call.function.arguments)
        question = args.get('question')
        options = args.get('options')
        context = args.get('context')
        return ask_user_question(question, options, context)
    elif tool_call.function.name.startswith("mcp_"):
        # 解析工具名：mcp_serverName_toolName
        parts = tool_call.function.name.split("_", 2)
        if len(parts) < 3:
            return "Error: Invalid MCP tool name format"
        _, server_name, original_tool_name = parts
        args = json.loads(tool_call.function.arguments)
        return call_mcp_tool(server_name, original_tool_name, args)
    else:
        return "Error: Unknown tool"

# tool_call.id 规范化辅助函数
def _ensure_tool_call_ids(msg_dict: dict) -> list[str]:
    """
    确保 msg_dict["tool_calls"] 中每个调用都有非空 id。
    缺失时生成稳定的唯一 id 并写回。
    返回与 tool_calls 顺序一致的 id 列表。
    """
    ids: list[str] = []
    for tc in msg_dict.get("tool_calls") or []:
        tid = tc.get("id")
        if not tid:
            tid = f"call_{uuid.uuid4().hex[:12]}"
            tc["id"] = tid
        ids.append(str(tid))
    return ids

#定义单工具执行函数
#确保 run_shell_hooks 函数在 _execute_single_tool 之前已定义
def _execute_single_tool(tool_call):
    """执行单个工具，包含所有钩子处理，返回 (tool_call_id, result)"""
    tool_args = json.loads(tool_call.function.arguments)
    
    # 1. Shell PreToolUse 钩子
    shell_decision = run_shell_hooks('PreToolUse', {
        'tool_name': tool_call.function.name,
        'tool_input': tool_args
    })
    if shell_decision and shell_decision.get('decision') == 'deny':
        return tool_call.id, f"Error: Blocked by shell hook: {shell_decision.get('reason')}"
    
    # 2. Python PreToolUse 钩子
    deny_result = HOOK.trigger('before_tool_call', tool_call)
    if deny_result and deny_result.get('decision') == 'deny':
        return tool_call.id, f"Error: Blocked by Python hook: {deny_result.get('reason', 'No reason')}"
    
    # 3. 执行工具
    result = _dispatch_tool(tool_call)
    
    # 4. PostToolUse 钩子（Shell 和 Python）
    run_shell_hooks('PostToolUse', {
        'tool_name': tool_call.function.name,
        'tool_input': tool_args,
        'tool_result': result
    })
    HOOK.trigger('after_tool_call', tool_call, result)
    
    return tool_call.id, result

#统一工具分发（减少重复代码）
def invoke_tool(tool_call):
    """
    执行单个工具调用，返回结果字符串。
    内部调用 _execute_single_tool，包含所有钩子处理。
    """
    _, result = _execute_single_tool(tool_call)
    return result

#子智能体调用（调后是因为钩子处理统一且完整\代码重复消除\错误处理与拦截逻辑一致\便于未来扩展)
def run_subagent(prompt: str, subagent_name: str = "default") -> str:
    HOOK.trigger('subagent_start', prompt, subagent_name)  # 埋点增加参数
# 加载自定义系统提示词，若无则使用默认
    system_prompt = SUBAGENT_LOADER.get_system_prompt(subagent_name)
    if system_prompt is None:
        system_prompt = f"你是一个在{CURRENT_WORKDIR}下的code subagent. 完成给定的任务，之后总结你的发现"

    sub_messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt}
    ]
    # ===== 动态轮次参数 =====
    base_rounds = 100
    max_rounds = base_rounds
    absolute_max_rounds = 1000          # 子代理绝对上限，避免无限循环
    current_round = 0
    extension_step = 50
    #------ 子代理独立的 TodoManager ------
    sub_todo = TodoManager()
    final_result = None
    try:
        while True:
            # ---- 1. 检查当前轮次是否已达到上限 ----
            if current_round >= max_rounds:
                # 获取最后一条消息（如果有）
                last_msg = sub_messages[-1] if sub_messages else None
                has_tool_calls = False
                if isinstance(last_msg, dict) and last_msg.get("role") == "assistant":
                    has_tool_calls = bool(last_msg.get("tool_calls"))
                # 检查子代理的 todo 是否全部完成
                todos_done = (not sub_todo.items) or all(item['status'] == 'completed' for item in sub_todo.items)
                # 是否可以正常结束
                can_finish = todos_done and not has_tool_calls
                if can_finish:
                    # 正常结束：提取最终回答
                    if isinstance(last_msg, dict) and last_msg.get("role") == "assistant":
                        final_result = last_msg.get("content", "")
                    else:
                        final_result = "子代理未给出有效回答。"
                    break
                # 如果还有工具调用或待办未完成，且未达到绝对上限，则延长轮次
                if  max_rounds < absolute_max_rounds:
                    max_rounds += extension_step
                    print(f"⚠️ 子代理轮次已达上限 {current_round}，但任务未完成，自动延长至 {max_rounds} 轮。")
                    # 注意：此处不再 continue，让流程继续执行 current_round += 1
                else:
                    # 到达绝对上限，强制退出
                    if isinstance(last_msg, dict) and last_msg.get("role") == "assistant":
                        final_result = last_msg.get("content", "")
                    else:
                        final_result = "子代理未给出有效回答。"
                    break
            # ---- 2. 调用 LLM ----
            lined_print(f"SubAgent Calling LLM (round {current_round + 1})")
            response = send_messages(sub_messages, SUBTOOLS)
            msg = response.choices[0].message
            # ---- 处理推理内容和回答 ----
            reasoning = getattr(msg, 'reasoning_content', None)
            if reasoning:
                framed_print("Thinking", reasoning, "info")

            content = getattr(msg, 'content', None)
            if content:
                framed_print("Answer", content, "info")

            tool_calls = getattr(msg, 'tool_calls', None)
            # ---- 3. 处理工具调用 ----
            if tool_calls:
                sub_messages.append(msg)
                for tool_call in tool_calls:
                    # 特殊处理 todo，使用子代理自己的实例
                    if tool_call.function.name == "todo":
                        args = json.loads(tool_call.function.arguments)
                        result = sub_todo.update(args['items'])
                    else:
                        result = invoke_tool(tool_call)
                    sub_messages.append({
                        "role": "tool",
                        "content": result,
                        "tool_call_id": tool_call.id
                    })
                # 本轮有工具调用，轮次计数增加
                current_round += 1
            else:
                # ---- 无工具调用，视为子代理已完成任务 ----
                # 如果子代理有未完成的 todo，记录警告但仍以当前内容作为结果
                if sub_todo.items and not all(item['status'] == 'completed' for item in sub_todo.items):
                    print("[子代理] 警告：无工具调用但待办事项未全部完成。")
                final_result = content if content else "子代理未生成回答。"
                break
    finally:
        HOOK.trigger('subagent_end', final_result, subagent_name) # 埋点

    return final_result

#任务/待办完成度检测辅助函数
def _are_tasks_completed() -> bool:
    """检查所有任务是否已完成"""
    task_files = list(TASKS.dir.glob("task_*.json"))
    if not task_files:
        return True
    for f in task_files:
        task = json.loads(f.read_text())
        if task.get('status') != 'completed':
            return False
    return True

def _are_todos_completed() -> bool:
    """检查当前待办列表是否全部完成"""
    if not TODO.items:
        return True
    return all(item['status'] == 'completed' for item in TODO.items)





# Agent Loop --- 支持输出回调
def agent_loop(messages, output_callback=None):
    """
    messages: 对话历史列表（可变）
    output_callback: 回调函数，签名为 callback(level: str, data: dict)
        level: 'thinking' | 'answer' | 'tool_call' | 'tool_result' | 'final' | 'system'
    """
    # ===== 1. 确保系统消息是最新的 =====
    if messages and messages[0].get("role") == "system":
        messages[0]["content"] = build_system_prompt()
    else:
        messages.insert(0, {"role": "system", "content": build_system_prompt()})

    HOOK.trigger('agent_loop_start', messages)  # 埋点

    # ----- 在此处添加动态轮次参数 -----
    base_rounds = 300
    max_rounds = base_rounds
    absolute_max_rounds = 2000  #最大上限轮次
    current_round = 0
    extension_step = 100

    total_tokens_used = 0

    try:
        while True:
            # ===== 新增调试日志 =====
            print(f"[AGENT LOOP] Round {current_round}, messages count: {len(messages)}")
            # ===== 轮次上限检查（动态延长） =====
            if current_round >= max_rounds:
                tasks_done = _are_tasks_completed()
                todos_done = _are_todos_completed()
                last_msg = messages[-1] if messages else None
                has_tool_calls = False
                if isinstance(last_msg, dict) and last_msg.get("role") == "assistant":
                    has_tool_calls = bool(last_msg.get("tool_calls"))
                # 三者都满足才真正结束
                if tasks_done and todos_done and not has_tool_calls:
                    break  # 正常结束
                # 否则认为工作未完成 → 尝试延长
                if max_rounds < absolute_max_rounds:
                    #让"延长"看起来更像"再加 100 轮 LLM 调用"
                    max_rounds += extension_step
                    msg = f"⚠️ 当前轮次已达上限 {current_round}，但任务尚未全部完成。自动延长至 {max_rounds} 轮。"
                    if output_callback:
                        output_callback('system', {'content': msg})
                    else:
                        print(msg)
                    # 注意：此处不再 continue。
                    # 让流程落到下方的 current_round += 1，正常进入新一轮。
                else:
                    msg = f"❌ 已达到绝对上限 {absolute_max_rounds} 轮，任务仍未完成，强制退出。"
                    if output_callback:
                        output_callback('system', {'content': msg})
                    else:
                        print(msg)
                    break
            #检查后台任务完成通知
            notifs = BG.drain_notifications()
            if notifs:
                notif_text = "\n".join(
                    f"[bg:{n['task_id']}] {n['status']}: {n['result']}" for n in notifs
                )
                messages.append({"role": "user", "content": f"<background-results>\n{notif_text}\n</background-results>"})
                messages.append({"role": "assistant", "content": "Noted background results."})

            # 每次循环开始时进行压缩，micro_compact一级压缩
            micro_compact(messages, keep_recent=KEEP_RECENT)
            #二级压缩
            if estimate_tokens(messages) > THRESHOLD:
                msg = "[auto_compact triggered]"
                if output_callback:
                    output_callback('system', {'content': msg})
                else:
                    print(msg)
                messages[:] = auto_compact(messages, callback=output_callback)
            # 调用 LLM 前的提示
            round_msg = f"Calling LLM (round {current_round})"
            if output_callback:
                output_callback('system', {'content': round_msg})
            else:
                lined_print(round_msg)
            if current_round > max_rounds:
                # 达到最大轮数，触发结束钩子
                end_decision = HOOK.trigger('agent_loop_end', messages)
                if end_decision and end_decision.get('decision') == 'block':
                    error_msg = f"达到最大轮数但测试失败：{end_decision.get('reason')}"
                    messages.append({"role": "user", "content": error_msg})
                    messages.append({"role": "assistant", "content": "收到，我将修复测试问题。"})
                    continue
                else:
                    # 达到最大轮数时的退出提示
                    exit_msg = f"Maximum rounds {max_rounds} reached, exiting"
                    if output_callback:
                        output_callback('system', {'content': exit_msg})
                    else:
                        print(exit_msg)
                    break
            # ---------- 递增轮次 ----------
            current_round += 1
            # ===== 调用 API，并捕获异常 =====
            try:
                # 打印状态信息（不覆盖输入栏）
                llm_status(current_round, total_tokens_used)
                response = send_messages(messages, MATERTOOLS)
                # 更新 token 数
                if hasattr(response, 'usage') and response.usage:
                    usage = response.usage
                    total_tokens_used += usage.total_tokens
            except Exception as e:
                print(f"[API ERROR] {e}")
                # 构造一个错误消息，让 Agent 继续
                messages.append({"role": "user", "content": f"API 调用失败：{e}"})
                continue

            msg = response.choices[0].message
            # ===== 打印响应详情 =====
            tool_calls = getattr(msg, 'tool_calls', None)
            if tool_calls:
                tool_calls_str = str(tool_calls)
                if len(tool_calls_str) > 100:
                    tool_calls_str = tool_calls_str[:100] + "... (truncated)"
                print(f"\033[3;90m[AGENT RESPONSE] tool_calls: {tool_calls_str}\033[0m")
                print("   (输入 /show tool 查看详情)")

            reasoning = getattr(msg, 'reasoning_content', None)
            if reasoning:
                # 思考内容
                if output_callback:
                    output_callback('thinking', {'content': reasoning})
                else:
                    framed_print("Thinking", reasoning, "info")

            content = getattr(msg, 'content', None)
            if content:
                # ===== 打印内容 =====
                # 回答内容
                if output_callback:
                    output_callback('answer', {'content': content})
                else:
                    framed_print("Answer", content, "info")

            tool_calls = getattr(msg, 'tool_calls', None)
            if tool_calls:
                # ---------- 1. 落盘 assistant 消息（含 tool_calls） ----------
                msg_dict = msg.model_dump()
                # 保证每个 tool_call 都有 id（防止后端返回空 id 导致后续 400）
                call_ids = _ensure_tool_call_ids(msg_dict)
                messages.append(msg_dict)
                # ---------- 2. 分类：并行安全工具 vs 串行工具 ----------
                # 用 index 而不是 tc.id 来跟踪结果，彻底避免 id 重复/缺失的问题
                parallel_indices: list[int] = []
                serial_indices: list[int] = []
                for i, tc in enumerate(tool_calls):
                    if tc.function.name in PARALLEL_SAFE_TOOLS:
                        parallel_indices.append(i)
                    else:
                        serial_indices.append(i)
                # 结果槽：按 index 存放，最后按原顺序取用
                results: list[Optional[str]] = [None] * len(tool_calls)
                # ---------- 3. 并行执行安全工具 ----------
                if parallel_indices:
                    future_to_idx: dict = {}
                    for i in parallel_indices:
                        # 提交到全局单例线程池；max_workers 已限制并发上限
                        future = _TOOL_EXECUTOR.submit(_execute_single_tool, tool_calls[i])
                        future_to_idx[future] = i
                    for future in as_completed(future_to_idx):
                        i = future_to_idx[future]
                        tc = tool_calls[i]
                        try:
                            _, result = future.result()
                            results[i] = result
                        except Exception as e:
                            # 单个工具失败不影响其他工具
                            results[i] = f"Parallel execution error ({tc.function.name}): {e}"
                # ---------- 4. 串行执行有副作用的工具 ----------
                for i in serial_indices:
                    tc = tool_calls[i]
                    try:
                        _, result = _execute_single_tool(tc)
                        results[i] = result
                    except Exception as e:
                        results[i] = f"Tool execution error ({tc.function.name}): {e}"
                # ---------- 5. 按原始顺序追加 tool 结果消息 ----------
                # 关键：用 call_ids[i] 而不是 tc.id，确保 id 非空且与 assistant 消息中的一致
                for i, tc in enumerate(tool_calls):
                    result = results[i] if results[i] is not None else "Error: Result not found"
                
                    if output_callback:
                        output_callback('tool_call', {
                            'name': tc.function.name,
                            'arguments': tc.function.arguments,
                        })
                        output_callback('tool_result', {
                            'tool': tc.function.name,
                            'result': result,
                        })
                    messages.append({
                        "role": "tool",
                        "content": result,
                        "tool_call_id": call_ids[i],   # ← 用规范化后的 id
                    })
            else:
                # ===== 没有工具调用，进入最终化 =====
                print("[AGENT] No tool_calls, entering finalize")

                shell_decision = run_shell_hooks('Stop', {})  # data 可为空
                if shell_decision and shell_decision.get('decision') == 'block':
                    print("[HOOK DEBUG] Stop hook blocked, continuing loop")
                    error_msg = f"Stop blocked by shell hook: {shell_decision.get('reason')}"
                    messages.append({"role": "user", "content": error_msg})
                    messages.append({"role": "assistant", "content": "收到，我将修复问题。"})
                    continue  # 继续循环
                # 尝试结束前钩子（如测试门控）
                end_decision = HOOK.trigger('agent_loop_end', messages)
                if end_decision and end_decision.get('decision') == 'block':
                    print("[HOOK DEBUG] agent_loop_end blocked, continuing loop")
                    # 测试失败，将错误信息插入对话，让 Agent 修复
                    error_msg = f"测试失败，请修复：{end_decision.get('reason')}"
                    messages.append({"role": "user", "content": error_msg})
                    messages.append({"role": "assistant", "content": "收到，我将修复测试问题。"})
                    continue  # 继续循环，Agent 会收到失败信息并尝试修复
                else:
                    # 正常结束，发送最终答案
                    # 提取最终回答（优先取最后一条非空 assistant 消息）
                    final_content = None
                    for m in reversed(messages):
                        role = m.get("role") if isinstance(m, dict) else getattr(m, "role", None)
                        if role == "assistant":
                            content = m.get("content") if isinstance(m, dict) else getattr(m, "content", None)
                            if content:
                                final_content = content
                                break
                    # 若全部为空，则取最后一条 assistant（可能为空）
                    if final_content is None:
                        for m in reversed(messages):
                            role = m.get("role") if isinstance(m, dict) else getattr(m, "role", None)
                            if role == "assistant":
                                final_content = m.get("content") if isinstance(m, dict) else getattr(m, "content", None)
                                break
                    # 发送最终结果（回调会显示 [最终]）
                    if output_callback:
                        output_callback('final', {'content': final_content or "（Agent 未生成回答）"})
                    # 如果无回调（例如 headless 模式），则直接打印
                    else:
                        print(final_content or "（Agent 未生成回答）")
                    break  # 测试通过或无需测试，正常结束
    finally:
        # 其他清理工作（如有）
        pass



# CLI前端
#字体加粗
def render_bold(text: str) -> str:
    """将 **text** 转换为 ANSI 粗体序列，同时避免处理代码块内的内容"""
    # 简单实现：只处理非代码块部分，但逐行处理时已经区分了代码块
    # 因此这里直接替换即可，因为调用时已按行区分
    bold_pattern = r'\*\*(.*?)\*\*'   # 非贪婪匹配
    return re.sub(bold_pattern, r'\033[1m\1\033[0m', text)
#前端交互呈现的代码形式
def print_formatted_content(content: str):
    """
    按行渲染 Agent 的回答内容：
      - 代码块（由 ``` 包裹）保留原始缩进，不进行折行或额外着色；
      - 非代码块中，以 '+ ' 开头的行显示为绿色，以 '- ' 开头的行显示为红色；
      - 其余文本正常显示（保留原始换行）。
    """
    lines = content.splitlines()
    in_code_block = False
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"

    for line in lines:
        # 检测代码块边界（支持 ``` 单独一行）
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            # 代码块标记本身也打印出来（可选），这里直接打印原行
            print(line)
            continue

        if in_code_block:
            # 代码块内部：原样输出，不进行任何着色或折行
            print(line)
        else:
            #非代码块：先加粗渲染，再检测 diff 标记
            line = render_bold(line)   # 将 **text** 转义为 ANSI 粗体
            if line.startswith("+ "):
                print(f"{GREEN}{line}{RESET}")
            elif line.startswith("- "):
                print(f"{RED}{line}{RESET}")
            else:
                print(line)
#输出的整体前端
def console_output_callback(level: str, data: dict):
    """Rich 版本的回调，压缩显示，保留历史记录"""
    if level == 'thinking':
        content = data.get('content', '')
        # 存储原内容（供 /show thought）
        HISTORY_THOUGHTS.append(content)
        render_thinking(content, show_full=False)

    elif level == 'answer':
        content = data.get('content', '')
        render_answer(content)

    elif level == 'tool_call':
        name = data.get('name', '')
        args = data.get('arguments', '')
        HISTORY_TOOL_CALLS.append({'name': name, 'args': args, 'result': None})
        render_tool_call(name, args)

    elif level == 'tool_result':
        tool = data.get('tool', '')
        result = data.get('result', '')
        # 更新最近一次匹配的工具调用结果
        if HISTORY_TOOL_CALLS and HISTORY_TOOL_CALLS[-1]['name'] == tool and HISTORY_TOOL_CALLS[-1]['result'] is None:
            HISTORY_TOOL_CALLS[-1]['result'] = result
        render_tool_result(tool, result)

    elif level == 'final':
        content = data.get('content', '')
        render_final(content)

    elif level == 'system':
        # 过滤掉 Calling LLM 和 Total tokens 的消息，其余正常打印
        msg = data.get('content', '')
        if 'Calling LLM' in msg or 'Total tokens' in msg:
            return  # 由 llm_status 处理，这里不再打印
        render_system(msg)
    # 显示 Token 消耗
    elif level == 'usage':
        # 不再打印，因为 token 信息已合并到 Calling LLM 行
        pass



#统一的资源重载函数
def reload_user_resources():
    """
    重新加载用户工作区（CURRENT_WORKDIR）下的所有自定义资源：
    - 技能 (skills/)
    - 子代理 (subagent/)
    - 钩子 (hooks/)
    - MCP 配置 (MCP/mcp_config.json)
    内置资源（项目根目录下的同名文件夹）具有最高优先级，不会被覆盖。
    """
    global MATERTOOLS   # 需要修改全局工具列表

    # 1. 加载用户技能（内置优先）
    SKILL_LOADER.load_user(get_skills_user_dir())

    # 2. 加载用户子代理（内置优先）
    SUBAGENT_LOADER.load_user(CURRENT_WORKDIR / "subagent")

    # 3. 加载用户钩子：先清除旧用户钩子，再加载新钩子
    HOOK.unregister_by_source("user")
    load_hooks_from_folder(CURRENT_WORKDIR / "hooks", HOOK, source="user")

    # 4. 加载用户 MCP 配置并重连（内置优先）
    user_mcp_config = CURRENT_WORKDIR / "MCP" / "mcp_config.json"
    reload_mcp_user_config(user_mcp_config)   # 此函数会合并用户配置并重连所有服务器

    # 5. 更新主代理工具列表：移除所有旧的 MCP 工具，添加新加载的 MCP 工具
    #    移除以 "mcp_" 开头的工具
    MATERTOOLS = [t for t in MATERTOOLS if not t.get("function", {}).get("name", "").startswith("mcp_")]
    MATERTOOLS.extend(get_mcp_tools())        # 获取最新 MCP 工具定义



# 主程序入口
def main():
    '''CLI主入口'''
    global ACTIVE_SKILL,SESSION_HISTORY
    # ---------- 新增启动标语 ----------
    print(f"\033[90m◈ 白泽 · 灵械核心 v0.5.0  |  链接《山海经》数据流 ...\033[0m")
    print(f"\033[90m◈ 工作目录: {CURRENT_WORKDIR}\033[0m\n")
    # ===== 关闭 utils 中的详细打印 =====
    utils.PRINT_DETAILS = False
    # 加载内置钩子到全局 HOOK
    load_hooks_from_folder(project_root / "hooks", HOOK, source="builtin")
    # ========== 1. 初始化 MCP 管理器（内置配置） ==========
    # init_mcp_client 会设置全局 _global_mcp_manager，并连接内置配置的服务器
    init_mcp_client(project_root / "MCP" / "mcp_config.json")
    # ========== 2. 注册代码内嵌的钩子（内置优先级） ==========
    # 这些钩子不是文件夹中的脚本，而是直接定义的函数，属于“内置”的一部分
    HOOK.register('before_tool_call', hook_sensitive_file_protection, source="builtin")
    HOOK.register('before_tool_call', hook_dangerous_command, source="builtin")
    HOOK.register('after_tool_call', hook_audit_log, source="builtin")
    HOOK.register('after_tool_call', hook_auto_format, source="builtin")
    HOOK.register('after_tool_call', hook_lint_feedback, source="builtin")
    HOOK.register('agent_loop_end', hook_test_gate, source="builtin")
    # ========== 4. 加载用户工作区资源（技能、子代理、钩子、MCP） ==========
    # 此函数会合并用户配置（内置优先），并更新 MATERTOOLS
    reload_user_resources()
    # ========== 5. 打印 LOGO 和欢迎信息（零依赖方案） ==========
    # 确保 Windows 终端支持 ANSI 转义码（标准库 os 实现，无需安装）
    if os.name == 'nt':
        subprocess.run('', shell=True) 

    term_width = shutil.get_terminal_size().columns
    # === 定义黑金主题颜色 ===
    GOLD = "\033[38;5;220m"       # 亮金
    DARK_GOLD = "\033[38;5;214m"  # 暗金
    GRAY = "\033[90m"
    WHITE = "\033[97m"
    BOLD = "\033[1m"
    RESET = "\033[0m"
    # 辅助函数：去除 ANSI 转义码计算纯文本长度（保证边框对齐）
    def strip_ansi(text):
        return re.sub(r'\x1b\[[0-9;]*m', '', text)
    # 辅助函数：计算实际显示宽度（兼容中文）
    def display_width(text):
        return wcwidth.wcswidth(strip_ansi(text))

    logo_path = project_root / "logo.txt"
    logo_art = ""
    if logo_path.exists():
        logo_art = logo_path.read_text(encoding='utf-8')
    # 打印 LOGO（自带彩色，保持不变）
    if logo_art:
        logo_lines = logo_art.splitlines()
        term_width = shutil.get_terminal_size().columns
        # 自适应缩放：根据终端宽度裁剪行数（若终端过窄）
        logo_char_width = 80  # 改为你实际生成 logo.txt 时的宽度（如 60、80、100）
        if term_width < logo_char_width + 10:
            keep_ratio = term_width / (logo_char_width + 10)
            keep_lines = max(1, int(len(logo_lines) * keep_ratio))
            logo_lines = logo_lines[:keep_lines]
        # 逐行居中打印 Logo
        for line in logo_lines:
            width = display_width(line)
            left_pad = max(0, (term_width - width) // 2)
            print(" " * left_pad + line)
        # 在 Logo 下方添加副标题
        subtitle = f"{GOLD}{BOLD}白泽--Coding Agent{RESET}"
        width = display_width(subtitle)
        left_pad = max(0, (term_width - width) // 2)
        print(" " * left_pad + subtitle)
        # ===== 新增：白泽自我介绍（20字以内） =====
        self_intro = f"{GRAY}通晓万物，陪你直觉编程。{RESET}"
        width_intro = display_width(self_intro)
        left_pad_intro = max(0, (term_width - width_intro) // 2)
        print(" " * left_pad_intro + self_intro)

        print()  # Logo 区域结束后的空行
    # 打印欢迎信息（去掉外框线，纯文本居中显示）
    welcome_lines = [
        f"{GOLD}{BOLD}  ◈ 灵兽归位！{RESET}",
        f"{GRAY}  LLM · API 计费信息{RESET}",
        f"{GRAY}  工作目录：{CURRENT_WORKDIR}{RESET}",
        "",
        f"{GOLD}{BOLD}◈ 初问白泽{RESET}",
        f"{GRAY}  询问 Baize 创建一个新应用或开发一个软件{RESET}",
        "",
        f"{GOLD}{BOLD}◈ 天机录{RESET}",
        f"{GRAY}  错误修复和可靠性改进{RESET}",
        f"{GRAY}  工具调用能力大幅增强{RESET}"
    ]
    for line in welcome_lines:
        if line == "":
            print()  # 空行直接打印
            continue
        width = display_width(line)
        left_pad = max(0, (term_width - width) // 2)
        print(" " * left_pad + line)
    print()
    # ---- 加载会话历史 ----
    non_system = load_session(CURRENT_WORKDIR)
    SESSION_HISTORY = [{"role": "system", "content": build_system_prompt()}] + non_system
    if non_system:
        print(f"[系统] 从 {CURRENT_WORKDIR / '.baize_session.json'} 加载了 {len(non_system)} 条历史消息。")

    # ---- 注册退出钩子（确保程序退出时提交 Git） ----
    atexit.register(commit_on_exit)
   # ========== 6. 主交互循环 ==========
    while True:
        # 打印一条分隔线（灰色横线，占满终端宽度）
        print("\033[90m" + "─" * shutil.get_terminal_size().columns + "\033[0m")
        try:
            user_input = input("\n\033[96m>>> 降旨：\033[0m").strip() #input("\n\033[1;33m> \033[0m").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n退出。")
            break

        if not user_input:
            continue
        # 处理管理命令
        if user_input.startswith("/"):
            cmd = user_input.lower()  # 用于匹配内置命令
            # ----- 内置命令（固定） -----
            if cmd in ("/exit", "/quit"):
                print("再见！")
                break
            elif cmd == "/compact":
                # 手动压缩：只压缩非系统部分
                non_system = [m for m in SESSION_HISTORY if m.get("role") != "system"]
                if len(non_system) > 1:  # 至少有一条对话
                    print("[系统] 正在压缩上下文...")
                    SESSION_HISTORY[:] = auto_compact(SESSION_HISTORY)
                    print("[系统] 压缩完成。")
                else:
                    print("[系统] 当前对话太短，无需压缩。")
                continue
            elif cmd == "/clear":
                # 清除对话历史（保留系统消息）
                system_msgs = [m for m in SESSION_HISTORY if m.get("role") == "system"]
                SESSION_HISTORY[:] = system_msgs
                # 重置待办列表
                TODO.items = []
                # 清空历史记录（思考内容和工具调用）
                HISTORY_THOUGHTS.clear()
                HISTORY_TOOL_CALLS.clear()
                # 卸载当前激活的技能
                ACTIVE_SKILL = None
                print("[系统] 已清除所有对话历史、待办列表、思考记录和工具调用记录。")
                continue
            elif cmd == "/show thought":
                if HISTORY_THOUGHTS:
                    print(f"\n完整思考内容（共 {len(HISTORY_THOUGHTS)} 条）：")
                    for i, t in enumerate(HISTORY_THOUGHTS, 1):
                        print(f"{i}. {t}")
                else:
                    print("没有思考记录。")
                continue
            elif cmd == "/show tool":
                if HISTORY_TOOL_CALLS:
                    print(f"\n工具调用记录（共 {len(HISTORY_TOOL_CALLS)} 条）：")
                    for i, tc in enumerate(HISTORY_TOOL_CALLS, 1):
                        print(f"{i}. 工具: {tc['name']}")
                        print(f"   参数: {tc['args']}")
                        print(f"   结果: {tc['result']}")
                else:
                    print("没有工具调用记录。")
                continue
            elif cmd == "/show all":
                # 合并显示思考与工具（可自行扩展）
                print("=== 全部记录 ===")
                for msg in SESSION_HISTORY:
                    print(f"{msg.get('role')}: {msg.get('content', '')[:200]}")
                continue
            elif cmd == "/commit":
                save_session(CURRENT_WORKDIR, commit_to_git=True)
                print("[系统] 会话已手动保存并提交到 Git。")
                continue
            elif cmd == "/skills":
                print("\n[系统] 可用技能列表：")
                print(SKILL_LOADER.get_descriptions())
                continue
            elif cmd == "/skills reload":
                SKILL_LOADER.load_user(get_skills_user_dir())
                print("[系统] 已重新加载用户技能。")
                continue
            elif cmd == "/unload":
                if ACTIVE_SKILL:
                    print(f"[系统] 已卸载技能 '{ACTIVE_SKILL}'。")
                    ACTIVE_SKILL = None
                else:
                    print("[系统] 当前没有加载任何技能。")
                continue
            # --- 未匹配内置命令，尝试作为技能名处理 ---
            # 注意：这里使用原输入（去掉首字符）进行匹配，不使用小写转换（保留原始大小写以供展示）
            skill_name_raw = user_input[1:].strip()   # 去掉第一个斜杠
            if not skill_name_raw:
                print("[系统] 请指定技能名称，例如 /brandkit")
                continue
            # 获取所有技能名称（键）
            all_skills = list(SKILL_LOADER.skills.keys())
            # 不区分大小写的包含匹配
            matched = [name for name in all_skills if skill_name_raw.lower() in name.lower()]
            if not matched:
                print(f"[系统] 未找到与 '{skill_name_raw}' 匹配的技能。")
                continue
            # 唯一匹配直接显示
            if len(matched) == 1:
                name = matched[0]
                ACTIVE_SKILL = name   # 这里需要全局变量 ACTIVE_SKILL（或使用 SESSION）
                print(f"[系统] 已加载技能 '{name}'。后续对话将遵循该技能指南。")
                continue
            else:
            # 多个匹配 → 交互选择
                print(f"[系统] 找到多个匹配的技能：")
                for idx, name in enumerate(matched, 1):
                    print(f"  {idx}. {name}")
                print("请输入编号或更精确的名称（直接回车取消）:")
                try:
                    choice = input("> ").strip()
                    if not choice:
                        print("[系统] 已取消。")
                        continue
                    if choice.isdigit():
                        idx = int(choice) - 1
                        if 0 <= idx < len(matched):
                            name = matched[idx]
                            ACTIVE_SKILL = name
                            print(f"[系统] 已加载技能 '{name}'。后续对话将遵循该技能指南。")
                            continue
                        else:
                            print("[系统] 编号超出范围。")
                            continue
                    else:
                        # 尝试用新输入再次匹配（仅限当前候选列表）
                        sub_matched = [name for name in matched if choice.lower() in name.lower()]
                        if len(sub_matched) == 1:
                            name = sub_matched[0]
                            ACTIVE_SKILL = name
                            print(f"[系统] 已加载技能 '{name}'。后续对话将遵循该技能指南。")
                            continue
                        elif len(sub_matched) > 1:
                            print(f"[系统] 仍有多项匹配，请更精确地输入。")
                            continue
                        else:
                            print("[系统] 未匹配，已取消。")
                            continue
                except KeyboardInterrupt:
                    print("\n[系统] 已取消。")
                    continue
                except Exception:
                    print("[系统] 输入无效，已取消。")
                    continue
        # 正常用户消息（非 / 开头的命令）的核心逻辑
        SESSION_HISTORY.append({"role": "user", "content": user_input})
        try:
            agent_loop(SESSION_HISTORY, output_callback=console_output_callback)
        # Ctrl+C 中断处理
        except KeyboardInterrupt:
            print("\n[系统] 操作已被用户中断。")
            # 可选：在对话历史中记录中断事件
            SESSION_HISTORY.append({"role": "assistant", "content": "[操作被用户中断]"})
        except Exception as e:
            print(f"\n\033[31m[错误]\033[0m {e}")
        finally:
            # 每次交互后保存 JSON（不提交 Git）
            save_session(CURRENT_WORKDIR, commit_to_git=False)
    # ========== 7. 程序结束前关闭 MCP 连接（可选） ==========
    from agent.MCP.mcp_client import _global_mcp_manager
    if _global_mcp_manager:
        _global_mcp_manager.shutdown()
    
if __name__ == "__main__":
    main()            