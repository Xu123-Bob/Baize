# agent/core/history.py
"""
会话历史的核心操作：清洗悬空 tool 消息、token 估算、两级压缩。
所有依赖外部副作用（LLM 调用、磁盘写入、hooks）的都通过参数注入，
方便单测和替换实现。
"""
from __future__ import annotations
import json
import re
import time
from pathlib import Path
from typing import Callable, Optional


# ==================== Token 估算 ====================

# 中英文混排的字符→token 换算系数（经验值）
_CJK_RE = re.compile(r'[\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]')

def _count_cjk(s: str) -> int:
    """统计字符串中的中日韩字符数。（惰性迭代，避免大字符串分配列表）。"""
    return sum(1 for _ in _CJK_RE.finditer(s))

def _msg_to_dict(msg) -> dict:
    """把 OpenAI 响应对象或 dict 统一转成 dict。"""
    if isinstance(msg, dict):
        return msg
    d = {"role": getattr(msg, "role", "")}
    if hasattr(msg, "content"):
        d["content"] = getattr(msg, "content")
    if hasattr(msg, "tool_calls") and getattr(msg, "tool_calls"):
        d["tool_calls"] = [
            {
                "id": t.id,
                "function": {
                    "name": t.function.name,
                    "arguments": t.function.arguments,
                },
            }
            for t in msg.tool_calls
        ]
    if hasattr(msg, "tool_call_id"):
        d["tool_call_id"] = getattr(msg, "tool_call_id")
    return d


def estimate_tokens(messages: list) -> int:
    """
    快速估算：按字符类型加权，误差 ±20%。
    比 tiktoken 快约 1000 倍，用于触发压缩阈值足够。
    """
    total_chars = 0
    cjk_chars = 0
    for m in messages:
        d = _msg_to_dict(m)
        # 只统计 content 和 tool_calls.arguments 的字符
        content = d.get("content") or ""
        if isinstance(content, str):
            total_chars += len(content)
            cjk_chars += _count_cjk(content)
        for tc in d.get("tool_calls") or []:
            args = (tc.get("function") or {}).get("arguments", "")
            if isinstance(args, str):
                total_chars += len(args)
                cjk_chars += _count_cjk(args)

    # 中文字符 ~1.5 字符/token，其余 ~3.5 字符/token
    non_cjk = total_chars - cjk_chars
    return int(cjk_chars / 1.5 + non_cjk / 3.5) + len(messages) * 4


# ==================== 悬空 tool 消息清洗 ====================
def sanitize_history(messages: list) -> list:
    """
    修复悬空的 tool_calls / tool results：
      - assistant 带 tool_calls，但后面没有对应 tool 结果 → 丢弃该调用
      - tool 结果前面没有对应 tool_calls → 丢弃该结果
    就地修改 messages 并返回。
    """
    called_ids: set = set()
    for m in messages:
        if isinstance(m, dict) and m.get("role") == "assistant" and m.get("tool_calls"):
            for tc in m["tool_calls"]:
                if isinstance(tc, dict) and tc.get("id") is not None:
                    called_ids.add(str(tc["id"]))

    answered_ids: set = set()
    for m in messages:
        if isinstance(m, dict) and m.get("role") == "tool":
            tcid = m.get("tool_call_id")
            if tcid is not None:
                answered_ids.add(str(tcid))

    cleaned = []
    for m in messages:
        if not isinstance(m, dict):
            cleaned.append(m)
            continue
        role = m.get("role")
        if role == "assistant" and m.get("tool_calls"):
            kept = [tc for tc in m["tool_calls"]
                    if str((tc or {}).get("id", "")) in answered_ids]
            if not kept and not m.get("content"):
                continue
            new_m = dict(m)
            if kept:
                new_m["tool_calls"] = kept
            else:
                new_m.pop("tool_calls", None)
            cleaned.append(new_m)
        elif role == "tool":
            if str(m.get("tool_call_id", "")) in called_ids:
                cleaned.append(m)
        else:
            cleaned.append(m)

    messages[:] = cleaned
    return messages


# ==================== 一级压缩：截断旧工具结果 ====================
def micro_compact(messages: list, keep_recent: int = 10) -> list:
    """
    把较早的工具结果替换为简短占位符，只保留最近 keep_recent 个。
    直接修改 messages。
    """
    tool_results: list[tuple[int, dict]] = []
    for idx, msg in enumerate(messages):
        if isinstance(msg, dict) and msg.get("role") == "tool" \
                and isinstance(msg.get("content"), str):
            tool_results.append((idx, msg))

    if len(tool_results) <= keep_recent:
        return messages

    # 构建 tool_call_id -> tool_name 映射
    tool_name_map: dict[str, str] = {}
    for msg in messages:
        if not isinstance(msg, dict) or msg.get("role") != "assistant":
            continue
        for tc in msg.get("tool_calls") or []:
            if isinstance(tc, dict):
                tcid = tc.get("id")
                tname = (tc.get("function") or {}).get("name")
                if tcid and tname:
                    tool_name_map[str(tcid)] = str(tname)

    for _, result in tool_results[:-keep_recent]:
        content = result.get("content")
        if isinstance(content, str) and len(content) > 200:
            tname = tool_name_map.get(str(result.get("tool_call_id", "")), "unknown")
            result["content"] = (
                f"[Previous: used {tname}, result truncated]\n{content[:200]}..."
            )
    return messages


# ==================== 二级压缩：整段摘要 ====================
def auto_compact(
    messages: list,
    *,
    send_fn: Callable,
    transcript_dir: Path,
    hook_trigger: Optional[Callable] = None,
    callback: Optional[Callable] = None,
) -> list:
    """
    把对话压缩为一段摘要，并把完整对话落盘到 transcript_dir。

    参数（全部显式注入，便于测试与复用）：
      send_fn        : (messages, tools) -> response 的 LLM 调用
      transcript_dir : 转写文件落盘目录
      hook_trigger   : 可选，(event_name, payload) -> Any 的钩子触发器
      callback       : 可选，进度回调 (level, data)
    """
    def _emit(level: str, content: str):
        if callback:
            callback(level, {"content": content})
        else:
            print(content)

    _emit("system", "[压缩] 开始压缩对话上下文...")

    system_msgs = [m for m in messages
                   if (m.get("role") if isinstance(m, dict)
                       else getattr(m, "role", None)) == "system"]
    other_msgs = [m for m in messages
                  if (m.get("role") if isinstance(m, dict)
                      else getattr(m, "role", None)) != "system"]

    transcript_dir.mkdir(parents=True, exist_ok=True)
    transcript_path = transcript_dir / f"transcript_{int(time.time())}.jsonl"
    with open(transcript_path, "w", encoding="utf-8") as f:
        for msg in messages:
            f.write(json.dumps(_msg_to_dict(msg), default=str) + "\n")
    _emit("system", f"[transcript saved: {transcript_path}]")

    conversation_text = json.dumps(
        [_msg_to_dict(m) for m in other_msgs], default=str
    )[:80000]
    summary_prompt = f"""Summarize this conversation for continuity. Include:
1) What was accomplished, 2) Current state, 3) Key decisions made.
Be concise but preserve critical details.

{conversation_text}
"""

    _emit("system", "[压缩] 正在请求 LLM 生成摘要...")
    try:
        response = send_fn([{"role": "user", "content": summary_prompt}], tools=[])
        summary = response.choices[0].message.content
        _emit("system", "[压缩] 摘要生成完成。")
    except Exception as e:
        _emit("system", f"[压缩] 失败：{e}，跳过压缩。")
        return messages

    new_messages = system_msgs + [
        {"role": "user",
         "content": f"[Conversation compressed. Transcript: {transcript_path}]\n\n{summary}"},
        {"role": "assistant",
         "content": "Understood. I have the context from the summary. Continuing."},
    ]
    if hook_trigger:
        hook_trigger("compact_end", new_messages)
    _emit("system", "[压缩] 上下文已替换为摘要，对话继续。")
    return new_messages