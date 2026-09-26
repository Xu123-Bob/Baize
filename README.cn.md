<div align="center">

<img src="image/logopage02.png" alt="白泽 Baize Logo" width="320" />

# 白泽 Baize

**通晓万物，陪你直觉编程。**

<p align="center">
  <a href="https://atomgit.com/Com_Xu/Baize">
    <img src="https://atomgit.com/Com_Xu/Baize/star/new_badge.svg" alt="AtomGit">
  </a>
</p>

<p align="center">
  <a href="https://github.com/Xu123-Bob/Baize/stargazers">
    <img src="https://img.shields.io/github/stars/Xu123-Bob/Baize?style=flat-square&logo=github" alt="GitHub stars">
  </a>
  <a href="https://github.com/Xu123-Bob/Baize/forks">
    <img src="https://img.shields.io/github/forks/Xu123-Bob/Baize?style=flat-square&logo=github" alt="GitHub forks">
  </a>
  <a href="https://github.com/Xu123-Bob/Baize/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/Xu123-Bob/Baize?style=flat-square" alt="License">
  </a>
    <a href="https://github.com/Xu123-Bob/Baize/pulls?q=is%3Apr+is%3Aclosed">
    <img src="https://img.shields.io/github/issues-pr-closed/Xu123-Bob/Baize?style=flat-square&logo=github&label=Closed%20PRs" alt="GitHub Closed Pull Requests">
  </a>
  <a href="https://github.com/Xu123-Bob/Baize/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/Xu123-Bob/Baize?style=flat-square&logo=github&label=Contributors" alt="GitHub Contributors">
  </a>
</p>

<p align="center">
  <a href="https://github.com/Xu123-Bob/Baize/releases">
    <img src="https://img.shields.io/github/v/release/Xu123-Bob/Baize?style=flat-square&logo=github&label=Release&include_prereleases" alt="GitHub release">
  </a>
  <a href="https://www.python.org/downloads/">
    <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python 3.10+">
  </a>
  
</p>

<p align="center">
  <a href="README.cn.md">简体中文</a> |
  <a href="README.en.md">English</a> |
  <a href="README.ja.md">日本語</a> |
  <a href="README.ko.md">한국어</a> |
  <a href="README.es.md">Español</a> |
  <a href="README.fr.md">Français</a>
</p>

</div>

----------

白泽 —— 中国古代神话中通晓万物的瑞兽，如今化身为 Vibe Coding 助手。

**一个开源的 AI Coding Agent CLI，Claude Code CLI的平替产品，支持多后端（DeepSeek / OpenAI 兼容 / 智谱 / 通义 / Kimi/ Ollama 本地），具备工具调用、技能加载、子代理委派、上下文压缩、安全沙箱等完整能力。在终端即可与 AI 结对编程。**

----------


# 特性

- **多后端支持**：DeepSeek、任意 OpenAI 兼容接口（GLM / Qwen / Kimi/ OpenAI）、本地 Ollama，一键切换。

- **零配置启动**：首次运行自动生成配置文件，用户只需填一次密钥。

- **完整工具链**：bash 执行、文件读写编辑、glob/grep 搜索、网页搜索抓取、后台任务、任务与待办管理。

- **技能系统（Skills）**：按需加载领域知识（SKILL.md），让 AI 在特定场景下更专业。

- **子代理（Subagents）**：把复杂任务委派给独立上下文的子代理，避免污染主会话。

- **钩子（Hooks）**：Python 或 Shell 钩子，支持工具调用前后拦截、审计日志、自动格式化、测试门控。

- **MCP 协议**：通过 Model Context Protocol 接入外部工具服务器（GitHub、Filesystem 等）。

- **上下文压缩**：两级压缩（工具结果截断 + LLM 摘要），支持超长对话。

- **安全沙箱**：命令白名单、路径逃逸检测、危险命令拦截、敏感文件保护、脚本注入拦截。

- **多语言交互**：中/英/日/韩/西/法/德/俄/阿 九种语言自由切换，说一句 `English` 或 `/lang ja` 即可，AI 全程用对应语言思考与回复。

- **黑金主题 CLI**：中文宽度自适应，代码高亮、Diff 着色、思考折叠。


# 安装

## 前置要求

- Python 3.10+（需要 tomllib，3.11+ 内置；3.10 需安装 tomli）

- pip

## 从源码安装
### 下载方式两个
1.pip install https://github.com/Xu123-Bob/Baize.git

bash  --win+R 输入cmd，然后输入：

    baize

2、在仓库页面点击 <>Code  --> Download ZIP

(1)解压后进入本文件目录：

bash  --win+R 输入cmd

    cd 解压后的目录

    pip install -r requirements.txt    

    python -m Baize             

下载完成后win+R 输入cmd，打开CLI界面，输入baize，即可运行

(2)下载 ZIP 后本地安装，解压后进入目录，执行：

bash --win+R 输入cmd

    pip install .

下载完成后win+R 输入cmd，打开CLI界面，输入baize，即可运行

# 快速开始
1. 首次运行

bash

    baize

首次运行时，白泽会自动生成两个配置文件：

```
~/.baize/config.toml   # 后端配置（选 DeepSeek / OpenAI / Ollama）

~/.baize/.env          # 密钥文件>
```
Windows 用户路径为 C:\Users\你的用户名\.baize\。


2. 选择后端

打开 ~/.baize/config.toml，修改 active_provider：

toml
```
active_provider = "deepseek"    # 或 "openai" / "ollama"

[model_providers.deepseek]
name = "DeepSeek"
base_url = "https://api.deepseek.com"
env_key = "DEEPSEEK_API_KEY"
model = "deepseek-v4-pro"

[model_providers.openai]
name = "OpenAI"
base_url = "https://api.openai.com/v1"
env_key = "OPENAI_API_KEY"
model = "gpt-4o-mini"

[model_providers.ollama]
name = "Ollama (本地)"
base_url = "http://localhost:11434/v1"
env_key = ""
model = "qwen2.5:7b">
```

3. 填入密钥

编辑 ~/.baize/.env：

env
```
#DeepSeek 后端必填

DEEPSEEK_API_KEY=sk-你的密钥


#OpenAI 兼容接口必填(GLM / Qwen / Kimi/ OpenAI)

#OPENAI_API_KEY=你的密钥

#Ollama 本地无需密钥
```

4. 重新启动

bash

    baize

看到黑金 Logo 和欢迎信息即启动成功。


# 使用示例

启动后在 >>> 降旨： 提示符下用自然语言描述需求即可：

```
>>>降旨：用 Python 写一个爬取豆瓣 Top250 的脚本，保存为 CSV

>>>降旨：帮我检查 src/ 下所有 Python 文件的类型错误

>>>降旨：在这个仓库里找一下所有用到 requests 的地方，改成 httpx
```

## 多语言交互

白泽支持**六种语言**：中文、English、日本語、한국어、Español、Français。

有两种切换方式：

### 方式一：直接说话（自动检测）

白泽会自动识别你输入的语言并切换：

```
>>> 降旨：Hello, help me write a Python script
[系统] 已检测到输入语言为 English，白泽已切换为 English 交互。
（白泽用英文回复）

>>> 降旨：日本語で答えてください
[系统] 已检测到输入语言为 日本語，白泽已切换为 日本語 交互。
（白泽用日文回复）
```

### 方式二：手动命令

```
>>> 降旨：/lang                # 查看当前语言和可用列表
[系统] 当前语言：中文 (zh)
[系统] 可用语言：
    zh    中文 ←
    en    English
    ja    日本語
    ko    한국어
    es    Español
    fr    Français

>>> 降旨：/lang English        # 用语言名切换
>>> 降旨：/lang ja             # 用语言代码切换
>>> 降旨：/lang 西班牙语        # 中文名也可以
```

支持**语言名 / 语言代码 / 中文名 / 原文名**四种写法。例如切换英文时，`English`、`en`、`英语`、`英文` 任意一种都可以。


## 白泽CLI界面
<div align="center">
白泽 CLI 启动界面
</div>

<p align="center">
  <img src="image/clipage01.jpg" alt="白泽 CLI 启动界面" width="800" />
</p>

<div align="center">
白泽 CLI 运行界面
</div>

<p align="center">
  <img src="image/clipage02.jpg" alt="白泽 CLI 运行界面" width="800" />
</p>


## 内置命令
- /exit、/quit --> 退出白泽
- /clear	--> 清空对话历史、待办、思考记录和工具记录
- /compact	--> 手动压缩上下文（对话过长时使用）
- /commit	--> 保存当前会话并提交到 Git（若在 Git 仓库内）
- /lang → 查看当前语言；/lang en 切换为英文（支持语言代码或语言名）
- /skills	--> 列出所有可用技能
- /skills reload	--> 重新加载用户技能目录
- /unload	--> 卸载当前激活的技能
- /show thought	--> 查看完整思考记录
- /show tool	--> 查看工具调用记录
- /show all	--> 查看全部会话历史
- /技能名	--> 加载指定技能（支持模糊匹配）


# Ollama 本地模型（零成本）

不想用云 API？用本地 Ollama：

bash

    #1. 安装 Ollama：https://ollama.com/download
    #2. 拉取模型
    ollama pull qwen2.5:7b

    #3. 启动 Ollama 服务
    ollama serve

    #4. 修改 ~/.baize/config.toml
    active_provider = "ollama"

    #5. 启动白泽
    baize

推荐模型：qwen2.5:7b（中文强）、llama3.1:8b、deepseek-r1:7b。


# 扩展机制

白泽支持四种扩展方式，全部放在当前工作目录下即可生效。

## 技能（Skills）
在 ./skills/技能名/SKILL.md 中编写领域知识，AI 遇到复杂任务时会主动加载。

markdown

    ---
    name: pandas-eda

    description: 使用 pandas 进行探索性数据分析的最佳实践

    tags: data,python
    ---

    #Pandas EDA 指南

    ##核心步骤
    1. df.info() 查看字段类型和缺失
    2. df.describe() 统计描述
    ...
    也可以在对话中用 /pandas-eda 手动加载。


## 子代理（Subagents）

在 ./subagent/角色名/AGENT.md 中定义专用子代理，主代理可通过 agent 工具委派任务。

markdown

    ---
    name: code-reviewer

    description: 严格的代码审查员
    ---

    你是资深代码审查员。审查时优先关注：
    1. 边界条件与异常处理
    2. 资源泄漏
    3. 并发安全
    ...


## 钩子（Hooks）

在 ./hooks/ 下放置 
- PreToolUse-*.
- sh、PostToolUse-*.
- sh、Stop-*.sh
接收 JSON 输入，返回决策：

bash

    #!/bin/bash

    #PreToolUse-guard.sh

    read -r input

    if echo "$input" | grep -q "rm -rf"; then

    echo '{"hookSpecificOutput":{"permissionDecision":"block","permissionDecisionReason":"禁止删除"}}'

    fi

Python 钩子可直接调用内置 API（见 Baize.py 中的 hook_* 函数）。


## MCP 服务器

在 ./MCP/mcp_config.json 中配置外部工具服务器：

json

    {

      "mcpServers": [

        {

          "name": "filesystem",

          "command": "npx",

          "args": ["-y", "@modelcontextprotocol/server-filesystem", "."],

          "env": {},

          "enabled": true

        }

      ]

     }


# 安全设计

白泽默认启用以下安全机制：

- **命令白名单**：仅允许 ls、cat、grep、git、python3 等常用命令。

- **路径逃逸检测**：所有文件操作限制在当前工作目录和 /tmp 内。

- **危险命令拦截**：拦截 rm -rf /、fork bomb、curl | sh、git push --force 等模式。

- **敏感文件保护**：禁止修改 .env、.ssh/、id_rsa、*.pem 等。

- **脚本注入拦截**：检测 python -c "os.system(...)" 类绕过。

- **进程资源限制**：Linux/macOS 下限制 CPU、内存、进程数。

如果你需要在受信任的项目中放宽限制，可修改 Baize.py 中的 ALLOWED_COMMANDS 和 FORBIDDEN_PATH_PATTERNS。


# 目录结构
```
    baize-agent/
    ├── pyproject.toml              # 打包配置
    ├── README.md
    ├── tests/                      # 测试（不随包发布）
    |   ├── __init__.py
    |   ├── test_history.py
    |   └── test_skill_loader.py 
    ├── .env.example                # 环境变量示例
    ├── .gitignore
    └── agent/                      # 主包
        ├── __init__.py
        ├── Baize.py                # 主程序与 Agent Loop
        ├── config.py               # 多后端配置加载
        ├── ui_theme.py             # CLI 渲染主题
        ├── utils.py                # 通用工具
        ├── logo.txt
        ├── skills/                 # 内置技能
        ├── subagent/               # 内置子代理
        ├── core/                   # 核心逻辑（无副作用，可单测）
        |   ├── __init__.py
        |   └── history.py          # 会话历史清洗 / token 估算 / 压缩
        ├── hooks/                  # 内置钩子
        └── MCP/                    # MCP 客户端与配置
            ├── __init__.py
            ├── mcp_client.py
            └── mcp_config.json
```

# 环境变量参考
		
- 变量：DEEPSEEK_API_KEY  说明：DeepSeek API  默认值：密钥	—

- 变量：DEEPSEEK_BASE_URL  说明：DeepSeek 接口地址  默认值：https://api.deepseek.com

- 变量：OPENAI_API_KEY  说明：OpenAI  默认值：兼容接口密钥	—

- 变量：OPENAI_BASE_URL	 说明：OpenAI 兼容接口地址	 默认值：https://api.openai.com/v1

- 变量：OLLAMA_BASE_URL	 说明：Ollama 服务地址	 默认值：http://localhost:11434

变量写入 ~/.baize/.env 即可，无需修改 shell 配置文件。


# 开发

## 运行测试

本项目使用 pytest。开发前请以可编辑模式安装包与开发依赖：

    pip install -e ".[dev]"

运行全部测试：

    python -m pytest tests/ -v

只跑单个文件：

    python -m pytest tests/test_history.py -v

## 代码结构约定

- `agent/`：随包发布的主包。所有运行时逻辑与资源（skills、subagent、hooks、MCP）都在这里。
- `agent/core/`：纯逻辑模块，无外部副作用，**必须能被单独测试**。新增此类逻辑请放这里，并配套测试。
- `tests/`：与 `agent/` 下的源文件一一对应，命名为 `test_<模块名>.py`。
- 任何有外部依赖（网络、磁盘、全局状态）的函数，请通过参数注入依赖，便于在测试中替换。

# ❓ 常见问题
- Q：密钥应该填在哪里？

A：~/.baize/.env，不是项目根目录的 .env。

- Q：换了后端要重装吗？

A：不用。改 ~/.baize/config.toml 里的 active_provider 即可。

- Q：本地 Ollama 需要填密钥吗？

A：不需要。选 active_provider = "ollama" 即可，env_key 留空。

- Q：如何切换工作目录？

A：在对话中直接说"切换到 /path/to/project"，白泽会调用 set_workspace 工具。

- Q：上下文太长会怎样？

A：白泽会自动两级压缩：先截断旧工具结果，再请求 LLM 生成摘要。也可手动 /compact。

- Q：会误删我的文件吗？

A：默认命令白名单会拦截 rm -rf / 等危险操作；写文件前会显示 Diff 并请求确认。

# 🤝 贡献
欢迎提交 Issue 和 PR。建议先阅读 Baize.py 中的 agent_loop 函数，理解 Agent 主循环后再做扩展。
### Thank you for every Contributor to Submit PR
- Github Contributor：
[@anupamme](https://github.com/anupamme)
[@wangyipeng0724](https://github.com/wangyipeng0724)

[![Contributors](https://contrib.rocks/image?repo=Xu123-Bob/Baize&v=2)](https://github.com/Xu123-Bob/Baize/graphs/contributors)

# 许可证
MIT License

# 致谢
- 本项目在国内AtomGit托管，项目链接：https://atomgit.com/Com_Xu/Baize

- 感谢AtomGit将本项目已纳入G-star孵化项目

- 感谢PR的贡献者、抖音的粉丝、关注我的学生们

- 灵感来自 Claude Code、Codex 等优秀 AI Coding 工具

- 基于 DeepSeek、OpenAI SDK、MCP 构建

- 感谢所有在 Vibe Coding 路上同行的开发者

- 开发者专注创意与决策，白泽处理琐碎与执行。让编程回归直觉，让创造如神话般流畅。

# ☕ 赞助支持
如果白泽对你有用，欢迎赞助打赏。独立开发也花费很多时间，赞助不会改变产品更新的排期，谢谢支持！
<p align="center">
  <img src="image/support.jpg" alt="微信二维码" width="200" />
</p>

# 联系我
- 如果你对白泽感兴趣，或者想参与开源合作，可以通过以下方式联系我
- **目前，本人在求职状态，本人从事过市场研究与用户研究工作，对Agent也有一定了解，如果我的能力符合您的需求，也希望与您共事（意向岗位：AI产品运营/用户研究/市场调研）**

<p align="center">
  <img src="image/weixin.jpg" alt="微信二维码" width="200" />
</p>

<p align="center">微信扫码，请注明Baize开源合作或者企业招聘</p>

<p align="center">
  <img src="image/抖音.png" alt="抖音二维码" width="200" />
</p>

<p align="center">抖音扫码关注</p>