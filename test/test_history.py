# tests/test_history.py
import json
from pathlib import Path

import pytest

from agent.core.history import (
    sanitize_history,
    estimate_tokens,
    micro_compact,
    auto_compact,
)


# ---------- sanitize_history ----------
class TestSanitizeHistory:

    def test_removes_dangling_tool_call(self):
        """assistant 有文本 + 悬空 tool_calls → 剥离调用，保留消息。"""
        msgs = [
            {"role": "user", "content": "hi"},
            {"role": "assistant", "content": "让我执行",     # ← 关键：有文本
            "tool_calls": [{"id": "c1", "function": {"name": "run_bash", "arguments": "{}"}}]},
            {"role": "assistant", "content": "done"},
        ]
        sanitize_history(msgs)
        assert len(msgs) == 3                              # 消息保留
        assert "tool_calls" not in msgs[1]                 # 调用剥离
        assert msgs[1]["content"] == "让我执行"            # 文本还在

    def test_removes_dangling_tool_result(self):
        """tool 结果没有对应的 tool_calls → 该结果被丢弃。"""
        msgs = [
            {"role": "user", "content": "hi"},
            {"role": "tool", "tool_call_id": "c1", "content": "out"},
        ]
        sanitize_history(msgs)
        assert len(msgs) == 1
        assert msgs[0]["role"] == "user"

    def test_valid_pair_preserved(self):
        msgs = [
            {"role": "assistant", "content": None,
             "tool_calls": [{"id": "c1", "function": {"name": "run_bash", "arguments": "{}"}}]},
            {"role": "tool", "tool_call_id": "c1", "content": "out"},
        ]
        sanitize_history(msgs)
        assert len(msgs) == 2
        assert msgs[0]["tool_calls"][0]["id"] == "c1"

    def test_keeps_text_when_tool_calls_dropped(self):
        """assistant 同时有文本和悬空 tool_calls → 保文本，丢调用。"""
        msgs = [
            {"role": "assistant", "content": "我思考了",
             "tool_calls": [{"id": "c1", "function": {"name": "x", "arguments": "{}"}}]},
        ]
        sanitize_history(msgs)
        assert len(msgs) == 1
        assert msgs[0]["content"] == "我思考了"
        assert "tool_calls" not in msgs[0]

    def test_drops_assistant_with_only_dangling_calls(self):
        """assistant 无文本、只有悬空 tool_calls → 整条丢弃。"""
        msgs = [
            {"role": "user", "content": "hi"},
            {"role": "assistant", "content": None,
             "tool_calls": [{"id": "c1", "function": {"name": "x", "arguments": "{}"}}]},
        ]
        sanitize_history(msgs)
        assert len(msgs) == 1
        assert msgs[0]["role"] == "user"


# ---------- estimate_tokens ----------
class TestEstimateTokens:

    def test_positive(self):
        msgs = [{"role": "user", "content": "你好，请帮我写一个 Python 函数"}]
        assert estimate_tokens(msgs) > 0

    def test_monotonic(self):
        short = [{"role": "user", "content": "hi"}]
        long = [{"role": "user", "content": "hi " * 500}]
        assert estimate_tokens(long) > estimate_tokens(short)

    def test_accepts_openai_message_objects(self):
        """兼容 OpenAI 响应对象（有 role/content 属性）。"""
        class M:
            role = "assistant"
            content = "ok"
        assert estimate_tokens([M()]) > 0


# ---------- micro_compact ----------
class TestMicroCompact:

    def _make_tool_pair(self, call_id: str, payload: str) -> list:
        return [
            {"role": "assistant", "content": "",
             "tool_calls": [{"id": call_id,
                             "function": {"name": "run_read", "arguments": "{}"}}]},
            {"role": "tool", "tool_call_id": call_id, "content": payload},
        ]

    def test_truncates_old_ones(self):
        msgs = []
        for i in range(12):
            msgs.extend(self._make_tool_pair(f"c{i}", "x" * 500))
        micro_compact(msgs, keep_recent=10)
        tool_msgs = [m for m in msgs if m["role"] == "tool"]
        assert tool_msgs[0]["content"].startswith("[Previous: used run_read")
        assert tool_msgs[-1]["content"] == "x" * 500

    def test_noop_when_below_threshold(self):
        msgs = []
        for i in range(3):
            msgs.extend(self._make_tool_pair(f"c{i}", "x" * 500))
        micro_compact(msgs, keep_recent=10)
        assert all("truncated" not in m["content"]
                   for m in msgs if m["role"] == "tool")

    def test_short_content_not_truncated(self):
        msgs = []
        for i in range(12):
            msgs.extend(self._make_tool_pair(f"c{i}", "short"))
        micro_compact(msgs, keep_recent=10)
        tool_msgs = [m for m in msgs if m["role"] == "tool"]
        assert tool_msgs[0]["content"] == "short"


# ---------- auto_compact ----------
class TestAutoCompact:

    class _FakeResponse:
        class _Msg:
            content = "这是摘要"
        choices = [type("C", (), {"message": _Msg()})()]

    def test_replaces_with_summary(self, tmp_path: Path):
        msgs = [
            {"role": "system", "content": "sys"},
            {"role": "user", "content": "hi"},
            {"role": "assistant", "content": "hello"},
        ]

        calls = []

        def fake_send(messages, tools):
            calls.append(messages)
            return self._FakeResponse()

        new = auto_compact(
            msgs,
            send_fn=fake_send,
            transcript_dir=tmp_path,
        )
        assert new[0]["role"] == "system"
        assert new[0]["content"] == "sys"
        assert "这是摘要" in new[1]["content"]
        assert new[2]["role"] == "assistant"
        # transcript 已落盘
        assert any(p.name.startswith("transcript_") for p in tmp_path.iterdir())

    def test_send_failure_keeps_original(self, tmp_path: Path):
        msgs = [
            {"role": "system", "content": "sys"},
            {"role": "user", "content": "hi"},
        ]

        def failing_send(messages, tools):
            raise RuntimeError("boom")

        out = auto_compact(msgs, send_fn=failing_send, transcript_dir=tmp_path)
        # 失败时保持原 messages 不变
        assert out is msgs

    def test_callback_invoked(self, tmp_path: Path):
        msgs = [
            {"role": "system", "content": "sys"},
            {"role": "user", "content": "hi"},
        ]
        events = []

        def cb(level, data):
            events.append((level, data.get("content", "")))

        auto_compact(
            msgs,
            send_fn=lambda m, t: self._FakeResponse(),
            transcript_dir=tmp_path,
            callback=cb,
        )
        # 契约：callback 至少被调用过（开始/保存/完成都算）
        assert len(events) >= 1
        # 契约：每次调用都是 (level, content) 结构
        assert all(isinstance(e, tuple) and len(e) == 2 for e in events)
        # 契约：level 是字符串
        assert all(isinstance(level, str) for level, _ in events)