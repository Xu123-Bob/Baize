# agent/core/privacy.py
"""
隐私脱敏核心模块。

设计目标：
  - 出站（发给 LLM）时把 PII 替换为占位符 [[TYPE_N]]
  - 入站（LLM 响应）时把占位符还原为原文
  - 支持多级模式：off / standard / strict
  - 会话级可逆，同一原文复用同一占位符
  - 完全无外部依赖，可单测

典型用法：
    s = PrivacySanitizer(mode="off")
    s.set_mode("standard")
    outbound = s.sanitize_messages(messages)   # 不修改原列表
    response = send_messages(outbound, tools)
    s.restore_message(response.choices[0].message)  # 原地还原
"""
from __future__ import annotations

import json
import re
import threading
from collections import OrderedDict
from dataclasses import dataclass
from typing import Callable, Optional


# ==================== 模式常量 ====================
MODE_OFF = "off"
MODE_STANDARD = "standard"
MODE_STRICT = "strict"
_ALL_MODES = (MODE_OFF, MODE_STANDARD, MODE_STRICT)

# 占位符正则：全局共享，用于还原时一次性扫描替换
_PLACEHOLDER_RE = re.compile(r'\[\[([A-Z][A-Z0-9]*)_(\d+)\]\]')


# ==================== 工具函数 ====================
def _luhn_check(number: str) -> bool:
    """Luhn 校验：验证银行卡/信用卡号合法性，避免误伤普通长数字串。"""
    digits = [int(c) for c in number if c.isdigit()]
    if len(digits) < 13:
        return False
    total = 0
    for i, d in enumerate(reversed(digits)):
        if i % 2 == 1:
            d *= 2
            if d > 9:
                d -= 9
        total += d
    return total % 10 == 0


# ==================== 规则定义 ====================
@dataclass
class PrivacyRule:
    """一条脱敏规则。"""
    name: str                                    # 内部标识
    label: str                                   # 人类可读标签
    pattern: re.Pattern                          # 匹配正则
    placeholder: str                             # 占位符前缀
    group: int = 0                               # 只替换第 N 组（0=整体）
    validator: Optional[Callable[[str], bool]] = None  # 二次校验
    enabled: bool = True
    modes: tuple = ("standard", "strict")        # 生效的模式


# ---------- 标准模式：常见 PII ----------
_STANDARD_RULES = [
    PrivacyRule("phone_cn", "中国大陆手机号",
        re.compile(r'(?<!\d)(1[3-9]\d{9})(?!\d)'), "PHONE"),
    PrivacyRule("id_card_cn", "中国大陆身份证号",
        re.compile(r'(?<!\d)([1-9]\d{5}(?:19|20)\d{2}'
                   r'(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01])\d{3}[\dXx])(?!\d)'),
        "IDCARD"),
    PrivacyRule("bank_card", "银行卡号",
        re.compile(r'(?<!\d)(\d{16,19})(?!\d)'), "BANKCARD",
        validator=_luhn_check),
    PrivacyRule("email", "电子邮箱",
        re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'),
        "EMAIL"),
    PrivacyRule("ipv4", "IPv4 地址",
        re.compile(r'\b(?:(?:25[0-5]|2[0-4]\d|1?\d?\d)\.){3}'
                   r'(?:25[0-5]|2[0-4]\d|1?\d?\d)\b'),
        "IPV4"),
    PrivacyRule("ipv6", "IPv6 地址",
        re.compile(r'\b(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}\b'),
        "IPV6"),
    PrivacyRule("openai_key", "OpenAI/DeepSeek API Key",
        re.compile(r'\bsk-[A-Za-z0-9_-]{20,}\b'), "APIKEY"),
    PrivacyRule("anthropic_key", "Anthropic API Key",
        re.compile(r'\bsk-ant-[A-Za-z0-9_-]{20,}\b'), "APIKEY"),
    PrivacyRule("github_token", "GitHub Token",
        re.compile(r'\b(gh[pousr]_[A-Za-z0-9]{30,})\b'), "GHTOKEN"),
    PrivacyRule("aws_access_key", "AWS Access Key ID",
        re.compile(r'\b(AKIA[0-9A-Z]{16})\b'), "AWSKEY"),
    PrivacyRule("aws_secret_key", "AWS Secret Access Key",
        re.compile(r'(?i)aws_secret_access_key\s*[:=]\s*["\']?'
                   r'([A-Za-z0-9/+=]{40})["\']?'),
        "AWSSECRET", group=1),
    PrivacyRule("bearer_token", "Bearer Token",
        re.compile(r'(?i)\bBearer\s+([A-Za-z0-9._\-]{20,})'),
        "BEARER", group=1),
    PrivacyRule("private_key", "私钥块",
        re.compile(r'-----BEGIN [A-Z ]*PRIVATE KEY-----[\s\S]*?'
                   r'-----END [A-Z ]*PRIVATE KEY-----'),
        "PRIVKEY"),
    PrivacyRule("password_field", "密码/密钥字段",
        re.compile(r'(?i)\b(password|passwd|pwd|secret|token)\s*[:=]\s*'
                   r'["\']?([^\s"\']{6,})["\']?'),
        "PASSWD", group=2),
    PrivacyRule("url_credential", "URL 中的凭证",
        re.compile(r'(?<=://)([^/\s:@]{1,64}):([^/\s@]{1,64})@'),
        "URLCRE"),
]

# ---------- 严格模式：容易误伤，需显式开启 ----------
# 中文百家姓（节选，覆盖 95%+）
_SURNAMES = (
    "赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜"
    "戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐"
    "费廉岑薛雷贺倪汤滕殷罗毕郝邬安常乐于时傅皮卞齐康伍余元卜顾孟平黄"
    "和穆萧尹姚邵湛汪祁毛禹狄米贝明臧计伏成戴谈宋茅庞熊纪舒屈项祝董梁"
    "杜阮蓝闵席季麻强贾路娄危江童颜郭梅盛林刁钟徐邱骆高夏蔡田樊胡凌霍"
    "虞万支柯昝管卢莫经房裘缪干解应宗丁宣贲邓郁单杭洪包诸左石崔吉钮龚"
    "程嵇邢滑裴陆荣翁荀羊於惠甄曲家封芮羿储靳汲邴糜松井段富巫乌焦巴弓"
    "牧隗山谷车侯宓蓬全郗班仰秋仲伊宫宁仇栾暴甘钭厉戎祖武符刘景詹束龙"
    "叶幸司韶郜黎蓟薄印宿白怀蒲邰从鄂索咸籍赖卓蔺屠蒙池乔阴郁胥能苍双"
    "闻莘党翟谭贡劳逄姬申扶堵冉宰郦雍却璩桑桂濮牛寿通边扈燕冀郏浦尚农"
    "温别庄晏柴瞿阎充慕连茹习宦艾鱼容向古易慎戈廖庾终暨居衡步都耿满弘"
    "匡国文寇广禄阙东欧殳沃利蔚越夔隆师巩厍聂晁勾敖融冷訾辛阚那简饶空"
    "曾毋沙乜养鞠须丰巢关蒯相查后荆红游竺权逯盖益桓公"
)

_STRICT_RULES = [
    PrivacyRule("name_cn", "中文姓名",
        re.compile(
            r'(?<![\u4e00-\u9fff])(?:[' + _SURNAMES + r'])'
            r'[\u4e00-\u9fff]{1,2}(?![\u4e00-\u9fff])'
        ),
        "NAME", modes=("strict",)),
    PrivacyRule("qq_number", "QQ 号",
        re.compile(r'(?i)\bqq\s*[:=]?\s*([1-9]\d{4,10})\b'),
        "QQ", group=1, modes=("strict",)),
    PrivacyRule("wechat_id", "微信号",
        re.compile(r'(?i)\b(?:wechat|weixin|微信)\s*[:=]?\s*'
                   r'([A-Za-z][A-Za-z0-9_-]{5,19})\b'),
        "WECHAT", group=1, modes=("strict",)),
    PrivacyRule("car_plate_cn", "中国大陆车牌号",
        re.compile(
            r'(?<![\u4e00-\u9fff])'
            r'[京津冀晋蒙辽吉黑沪苏浙皖闽赣鲁豫鄂湘粤桂琼渝川贵云藏陕甘青宁新]'
            r'[A-Z][A-Z0-9]{5,6}(?![\u4e00-\u9fffA-Z0-9])'
        ),
        "CARPLATE", modes=("strict",)),
]

# ==================== 工具参数脱敏策略 ====================
# 白名单：这些工具的 arguments 会被脱敏
# 特征：参数是"给人看的文本"，不参与任何实际执行（不碰文件系统/网络/子进程）
# 
# 反面清单（不脱敏，特此记录以便日后审计）：
#   - run_read/run_write/run_edit/run_glob/run_grep：路径会被用于实际 IO
#   - run_bash/background_run：命令会被执行
#   - run_webfetch/web_search：会真的发到网络，脱敏后无法工作
#   - set_workspace：路径会被 os.chdir
#   - load_skills：技能名是枚举，脱敏后查不到
#   - agent：prompt 会进入子代理上下文，让子代理统一脱敏
#   - mcp_*：未知语义，默认保守
_SANITIZE_ARGS_TOOLS = frozenset({
    "todo",
    "ask_user_question",
    "task_create",
    "task_update",
})


# ==================== 主体类 ====================
class PrivacySanitizer:
    """
    隐私脱敏器。全局单例使用即可。

    双向可逆：
        outbound_text = sanitizer.sanitize_text(user_input)
        original_text = sanitizer.restore_text(outbound_text)

    消息级：
        outbound_msgs = sanitizer.sanitize_messages(messages)
        sanitizer.restore_message(resp_msg)
    """

    def __init__(self, mode: str = MODE_OFF):
        if mode not in _ALL_MODES:
            mode = MODE_OFF
        self._lock = threading.RLock()
        self._mode = mode
        self._rules = list(_STANDARD_RULES) + list(_STRICT_RULES)
        # 占位符 -> 原文（保持插入顺序，便于审计）
        self._map: OrderedDict[str, str] = OrderedDict()
        # 原文 -> 占位符（避免同一原文产生多个占位符）
        self._reverse: dict[str, str] = {}
        # 每个前缀的当前序号，避免每次 sum 遍历
        self._counters: dict[str, int] = {}
        self._stats = {"sanitize_calls": 0, "restore_calls": 0}

    # ---------- 模式控制 ----------
    @property
    def mode(self) -> str:
        return self._mode

    def set_mode(self, mode: str) -> bool:
        if mode not in _ALL_MODES:
            return False
        with self._lock:
            self._mode = mode
        return True

    def is_enabled(self) -> bool:
        return self._mode != MODE_OFF

    # ---------- 规则查询 ----------
    def list_active_rules(self) -> list[PrivacyRule]:
        with self._lock:
            mode = self._mode
        return [r for r in self._rules if r.enabled and mode in r.modes]

    def list_all_rules(self) -> list[PrivacyRule]:
        return list(self._rules)

    def set_rule_enabled(self, name: str, enabled: bool) -> bool:
        with self._lock:
            for r in self._rules:
                if r.name == name:
                    r.enabled = enabled
                    return True
        return False

    # ---------- 文本脱敏 ----------
    def sanitize_text(self, text: str) -> str:
        if not text or not self.is_enabled():
            return text
        with self._lock:
            rules = [r for r in self._rules
                     if r.enabled and self._mode in r.modes]
            for rule in rules:
                text = self._apply_rule(text, rule)
            self._stats["sanitize_calls"] += 1
            return text

    def _apply_rule(self, text: str, rule: PrivacyRule) -> str:
        def _repl(m: re.Match) -> str:
            try:
                original = m.group(rule.group) if rule.group else m.group(0)
            except IndexError:
                return m.group(0)
            if not original:
                return m.group(0)
            if rule.validator and not rule.validator(original):
                return m.group(0)
            # 复用占位符
            if original in self._reverse:
                ph = self._reverse[original]
            else:
                idx = self._counters.get(rule.placeholder, 0) + 1
                self._counters[rule.placeholder] = idx
                ph = f"[[{rule.placeholder}_{idx}]]"
                self._map[ph] = original
                self._reverse[original] = ph
            # 只替换指定组时保留前后文
            if rule.group:
                s, e = m.span(rule.group)
                rs, re_ = s - m.start(), e - m.start()
                whole = m.group(0)
                return whole[:rs] + ph + whole[re_:]
            return ph

        return rule.pattern.sub(_repl, text)

    # 新增私有方法 _sanitize_arguments
    def _sanitize_arguments(self, args_str: str) -> str:
        """
        对工具参数 JSON 字符串做脱敏。

        为什么不能直接用正则：
            正则会误伤 JSON 结构。例如 {"phone": 13812345678}
            被替换成 {"phone": [[PHONE_1]]} 后不再是合法 JSON。

        策略：
            1. 先尝试 json.loads
            2. 递归遍历，只对 str 类型的值调用 sanitize_text
            3. 重新 json.dumps
            4. 若解析失败（LLM 流式输出损坏等），回退到正则
        """
        if not args_str:
            return args_str

        try:
            obj = json.loads(args_str)
        except (json.JSONDecodeError, TypeError, ValueError):
            # 解析失败 → 回退正则（可能不是合法 JSON，但至少尽力脱敏）
            return self.sanitize_text(args_str)

        def _walk(node):
            if isinstance(node, str):
                return self.sanitize_text(node)
            if isinstance(node, list):
                return [_walk(x) for x in node]
            if isinstance(node, dict):
                return {k: _walk(v) for k, v in node.items()}
            # int / float / bool / None 原样保留
            # 注意：数字类型的手机号（不带引号）不会被脱敏，
            # 但实践中 LLM 生成的参数值绝大多数是带引号的字符串
            return node

        sanitized = _walk(obj)
        # separators 去掉多余空格，节省 token；ensure_ascii=False 保留中文
        return json.dumps(sanitized, ensure_ascii=False, separators=(",", ":"))

    # ---------- 文本还原 ----------
    def restore_text(self, text: str) -> str:
        if not text:
            return text
        with self._lock:
            if not self._map:
                return text

            def _sub(m: re.Match) -> str:
                return self._map.get(m.group(0), m.group(0))

            text = _PLACEHOLDER_RE.sub(_sub, text)
            self._stats["restore_calls"] += 1
            return text

    # ---------- 消息级脱敏 ----------
    def sanitize_messages(self, messages: list, *, 
                      sanitize_tool_args: bool = True,
                      sanitize_tool_results: bool = True) -> list:
        """
        对 messages 列表做脱敏，返回**新列表**（不修改入参）
        参数：
        sanitize_tool_args=True（默认）：
            按 _SANITIZE_ARGS_TOOLS 白名单，只脱敏语义上"纯文本"的工具参数。
            路径/命令/URL/搜索词类工具的 arguments 原样保留，
            否则工具执行时会因路径被替换而失败。
        sanitize_tool_results=True（默认）：
            对 role='tool' 的消息 content 脱敏，
            防止工具读到的文件内容 / 命令输出里的 PII 回流给 LLM。
        覆盖范围：
        - user / assistant / system：content 脱敏
        - assistant.tool_calls[*].function.arguments：白名单工具脱敏
        - tool：content 脱敏（可通过开关关闭）
        """
        if not self.is_enabled():
            return messages
        out = []
        for m in messages:
            if not isinstance(m, dict):
                out.append(m)
                continue
            new_m = dict(m)
            role = new_m.get("role")
            # 文本内容：user / assistant / system / tool 都脱敏
            content = new_m.get("content")
            if isinstance(content, str) and content:
                if role == "tool" and not sanitize_tool_results:
                    # tool 结果按开关决定是否脱敏
                    pass
                else:
                    nc = self.sanitize_text(content)
                    if nc != content:
                        new_m["content"] = nc
            # ---------- tool_calls.arguments 脱敏（默认关闭） ----------
            if sanitize_tool_args and new_m.get("tool_calls"):
                new_tcs = []
                changed = False
                for tc in new_m["tool_calls"]:
                    if not isinstance(tc, dict):
                        new_tcs.append(tc)
                        continue
                    fn = tc.get("function")
                    if not isinstance(fn, dict):
                        new_tcs.append(tc)
                        continue
                    tool_name = fn.get("name", "")
                    # 白名单过滤：非白名单工具的 arguments 原样保留
                    if tool_name not in _SANITIZE_ARGS_TOOLS:
                        new_tcs.append(tc)
                        continue
                    args = fn.get("arguments")
                    if not isinstance(args, str) or not args:
                        new_tcs.append(tc)
                        continue
                    na = self._sanitize_arguments(args)
                    if na != args:
                        new_fn = dict(fn)
                        new_fn["arguments"] = na
                        new_tc = dict(tc)
                        new_tc["function"] = new_fn
                        new_tcs.append(new_tc)
                        changed = True
                    else:
                        new_tcs.append(tc)
                if changed:
                    new_m["tool_calls"] = new_tcs
            out.append(new_m)
        return out

    # ---------- 消息级还原 ----------
    def restore_message(self, msg) -> None:
        """
        原地还原 pydantic 响应对象或 dict 中的占位符。

        返回是否全部成功：
          - dict：调用 restore_dict，一定成功，返回 True
          - pydantic：属性赋值，失败返回 False（调用方应记录日志/断言）
          - PRIVACY 关闭时：直接返回 True

        调用方惯例（agent_loop / run_subagent）：
            if PRIVACY.is_enabled() and not PRIVACY.restore_message(msg):
                print("[privacy] 警告：pydantic 对象还原失败")
        """
        if not self.is_enabled():
            return True 

        # ---------- dict 分支 ----------
        if isinstance(msg, dict):
            self.restore_dict(msg)
            return True
        # ---------- pydantic 分支 ----------
        ok = True
        # 1) content
        try:
            v = getattr(msg, "content", None)
            if isinstance(v, str):
                msg.content = self.restore_text(v)
        except Exception:
            ok = False
        # 2) reasoning_content（可能是 model_extra）
        try:
            v = getattr(msg, "reasoning_content", None)
            if isinstance(v, str):
                restored = self.restore_text(v)
                # 优先直接 setattr；失败则退回 model_extra
                try:
                    msg.reasoning_content = restored
                except Exception:
                    extra = getattr(msg, "model_extra", None)
                    if isinstance(extra, dict):
                        extra["reasoning_content"] = restored
                    else:
                        ok = False
        except Exception:
            ok = False
        # 3) tool_calls[*].function.arguments
        try:
            for tc in (getattr(msg, "tool_calls", None) or []):
                try:
                    args = tc.function.arguments
                    if isinstance(args, str):
                        tc.function.arguments = self.restore_text(args)
                except Exception:
                    ok = False
        except Exception:
            ok = False
        return ok

    def _restore_dict(self, d: dict) -> None:
        c = d.get("content")
        if isinstance(c, str):
            d["content"] = self.restore_text(c)
        tcs = d.get("tool_calls")
        if tcs:
            for tc in tcs:
                fn = (tc or {}).get("function")
                if isinstance(fn, dict) and isinstance(fn.get("arguments"), str):
                    fn["arguments"] = self.restore_text(fn["arguments"])

    # ---------- 会话管理 ----------
    def clear(self):
        with self._lock:
            self._map.clear()
            self._reverse.clear()
            self._counters.clear()

    # ---------- 统计 ----------
    def get_stats(self) -> dict:
        with self._lock:
            return {
                "mode": self._mode,
                "active_rules": len(self.list_active_rules()),
                "total_rules": len(self._rules),
                "active_placeholders": len(self._map),
                **self._stats,
            }

    def list_placeholders(self) -> list[tuple[str, str]]:
        """列出当前所有占位符 -> 原文的映射（谨慎使用）。"""
        with self._lock:
            return list(self._map.items())


# ==================== 自然语言意图识别 ====================
_ENABLE_KW = [
    "开启脱敏", "启用脱敏", "打开脱敏", "启动脱敏",
    "开启隐私", "启用隐私", "打开隐私", "启动隐私",
    "开启隐私保护", "启用隐私保护", "打开隐私保护",
    "开启隐私模式", "启用隐私模式",
    "开启隐私脱敏", "启用隐私脱敏",
    "开启敏感信息保护", "启用敏感信息保护",
    "隐私模式开启", "隐私保护开启",
    "enable privacy", "enable sanitize", "turn on privacy",
    "privacy on", "sanitize on", "enable pii",
]
_DISABLE_KW = [
    "关闭脱敏", "禁用脱敏", "关掉脱敏", "停止脱敏",
    "关闭隐私", "禁用隐私", "关掉隐私", "停止隐私",
    "关闭隐私保护", "禁用隐私保护", "关闭隐私模式",
    "关闭隐私脱敏", "禁用隐私脱敏",
    "关闭敏感信息保护", "禁用敏感信息保护",
    "脱敏关闭", "隐私保护关闭", "隐私模式关闭",
    "disable privacy", "disable sanitize", "turn off privacy",
    "privacy off", "sanitize off",
]
_STRICT_KW = [
    "严格脱敏", "严格隐私", "严格隐私模式", "严格模式脱敏",
    "开启严格脱敏", "启用严格脱敏", "严格脱敏模式",
    "strict privacy", "strict sanitize", "privacy strict",
]


def detect_privacy_intent(text: str) -> Optional[tuple[str, str]]:
    """
    检测用户输入中是否包含隐私功能控制意图。
    返回 (action, value)：
      ("set_mode", "off") / ("set_mode", "standard") / ("set_mode", "strict")
      ("show_status", "")
    未识别到返回 None。
    """
    if not text:
        return None
    t = text.lower()
    for kw in _STRICT_KW:
        if kw.lower() in t:
            return ("set_mode", MODE_STRICT)
    for kw in _DISABLE_KW:
        if kw.lower() in t:
            return ("set_mode", MODE_OFF)
    for kw in _ENABLE_KW:
        if kw.lower() in t:
            return ("set_mode", MODE_STANDARD)
    # 单纯"查看隐私状态"类
    if any(k in t for k in ["隐私状态", "脱敏状态", "privacy status"]):
        return ("show_status", "")
    return None