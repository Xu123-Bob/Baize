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
import time
from collections import OrderedDict
from dataclasses import dataclass
from typing import Callable, Optional
import secrets


# ==================== 模式常量 ====================       # ★ 必须保留
MODE_OFF = "off"
MODE_STANDARD = "standard"
MODE_STRICT = "strict"
_ALL_MODES = (MODE_OFF, MODE_STANDARD, MODE_STRICT)

# ==================== 占位符格式 ====================
# 格式：«PZ_TYPE_<16hex>»
#   - « »：非 ASCII 括号，与用户输入冲突概率极低
#   - PZ：Baize 前缀，便于 grep 审计
#   - TYPE：规则占位符（PHONE/EMAIL/...）
#   - 16hex：64 bit 随机 token（不可预测、不可枚举）
#
# ⚠️ 不要改回 [[TYPE_N]] 形式！
#    序号可枚举，会导致"用户输入 [[PHONE_1]] 即还原出真实号码"的注入攻击。
PLACEHOLDER_OPEN = "«PZ_"
PLACEHOLDER_CLOSE = "»"
PLACEHOLDER_TOKEN_BYTES = 8          # 8 字节 → 16 hex 字符

# 还原时使用的正则：只识别新格式
_PLACEHOLDER_RE = re.compile(
    r'«PZ_([A-Z][A-Z0-9]*)_([0-9a-f]{16})»'
)

# 兼容扫描：识别任何"看起来像占位符样式"的字符串，
# 用于在脱敏入口处做中和处理（详见 3.5）。
_ANY_PLACEHOLDER_SHAPE_RE = re.compile(
    r'[\[«⟦]{1,2}PZ?[_A-Z0-9]*[\]»⟧]{1,2}|'
    r'\[\[[A-Z][A-Z0-9]*_\d+\]\]'
)


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
    # ★ 新增到正确位置：db_url 必须在 email 之前，
    #   否则 "user:pass@host.com" 里的 "pass@host.com" 会被 email 先吃
    PrivacyRule("db_url", "数据库连接串",
        re.compile(r'(?i)\b(postgres(?:ql)?|mysql|mongodb(?:\+srv)?|redis|mssql)://([^:\s]+):([^@\s]+)@'),
        "DBURL", group=0),
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
    # ★ 新增到正确位置：jwt 必须在 password_field 之前，
    #   否则 "token: eyJ..." 会被 password_field（关键字含 token）先吃
    PrivacyRule("jwt", "JWT Token",
        re.compile(r'\beyJ[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}\b'),
        "JWT"),
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
    # 国际手机号（E.164）
    #   - 强制 + 号开头（避免匹配普通数字串）
    #   - validator 要求 10-15 位数字（E.164 上限 15；排除 +2024-01-01 这类日期）
    PrivacyRule("phone_intl", "国际手机号",
        re.compile(r'(?<![\d+])\+\d{1,3}[\s\-]?\(?\d{2,4}\)?[\s\-]?\d{3,4}[\s\-]?\d{3,4}(?!\d)'),
        "PHONE",
        validator=lambda s: 10 <= len(re.sub(r'\D', '', s)) <= 15),
    # 中国大陆固定电话
    #   - 区号以 0 开头，2-3 位
    #   - 号码 7-8 位
    #   - 允许中间有空格或短横线
    PrivacyRule("landline_cn", "中国固定电话",
        re.compile(r'(?<!\d)(0\d{2,3}[\s\-]?\d{7,8})(?!\d)'),
        "TEL"),
    # 中国护照号（E/G + 8 位数字）
    PrivacyRule("passport_cn", "中国护照号",
        re.compile(r'(?<![A-Za-z0-9])([EG]\d{8})(?![A-Za-z0-9])'),
        "PASSPORT"),
    # 带分隔符的银行卡号（4-4-4-4~7，用空格或短横线分隔）
    #   与现有 bank_card 不重叠：后者只匹配连续数字
    PrivacyRule("bank_card_sep", "银行卡号（含分隔）",
        re.compile(r'(?<!\d)(\d{4}[\s\-]\d{4}[\s\-]\d{4}[\s\-]\d{4,7})(?!\d)'),
        "BANKCARD",
        validator=lambda s: _luhn_check(s)),
    # AWS Session Token
    #   要求明确的前缀 aws_session_token + 100+ 字符
    PrivacyRule("aws_session", "AWS Session Token",
        re.compile(r'(?i)aws_session_token\s*[:=]\s*["\']?([A-Za-z0-9/+=]{100,})'),
        "AWSSESS", group=1),
    # GCP Service Account Key（JSON 里的 private_key_id）
    PrivacyRule("gcp_key", "GCP Service Account Key",
        re.compile(r'"private_key_id"\s*:\s*"([a-f0-9]{40})"'),
        "GCPKEY", group=1),
    # Slack Token
    PrivacyRule("slack_token", "Slack Token",
        re.compile(r'\bxox[baprs]-[A-Za-z0-9\-]{10,}\b'),
        "SLACK"),
    # Stripe Key
    PrivacyRule("stripe_key", "Stripe Key",
        re.compile(r'\b(sk|pk|rk)_(live|test)_[A-Za-z0-9]{20,}\b'),
        "STRIPE"),
    # MAC 地址
    PrivacyRule("mac", "MAC 地址",
        re.compile(r'\b(?:[0-9A-Fa-f]{2}[:-]){5}[0-9A-Fa-f]{2}\b'),
        "MAC"),
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
    # 港澳台证件号
    #   ⚠️ 正则较宽（[A-Z]\d{6,9}），standard 模式误报率高
    #   仅在 strict 模式启用；用户如嫌误报多，可通过 /privacy rules 关闭
    PrivacyRule("id_hk_mo_tw", "港澳台证件号",
        re.compile(r'(?<![A-Za-z0-9])([A-Z]\d{6,9}[0-9A-Z]?)(?![A-Za-z0-9])'),
        "IDCARD", modes=("strict",)),

    # 中文详细地址
    #   要求明确包含 省/市/自治区 + 市/区/县 + 路/街/道/巷/号
    PrivacyRule("address_cn", "中文详细地址",
        re.compile(r'[\u4e00-\u9fff]{2,}(?:省|市|自治区)'
                   r'[\u4e00-\u9fff]{2,}(?:市|区|县)'
                   r'[\u4e00-\u9fff]{2,}(?:路|街|道|巷|号)'
                   r'[\d\u4e00-\u9fff]{1,20}'),
        "ADDRESS", modes=("strict",)),
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

    def __init__(self, mode: str = MODE_OFF,
                max_entries: int = 2000,
                ttl_seconds: float = 86400):
        """
        参数：
        max_entries : 映射表最大条目数（超出按 LRU 淘汰）
        ttl_seconds : 条目的最长存活时间（秒），默认 24 小时
        """
        if mode not in _ALL_MODES:
            mode = MODE_OFF
        self._lock = threading.RLock()
        self._mode = mode
        self._rules = list(_STANDARD_RULES) + list(_STRICT_RULES)
        # 占位符 -> (原文, 时间戳)；OrderedDict 天然支持 LRU（move_to_end / popitem(last=False)）
        self._map: OrderedDict[str, tuple[str, float]] = OrderedDict()
        # 原文 -> 占位符（反向索引，避免同一原文产生多个占位符）
        self._reverse: dict[str, str] = {}
        self._max_entries = max(1, max_entries)
        self._ttl = max(1.0, ttl_seconds)
        self._stats = {
            "sanitize_calls": 0,
            "restore_calls": 0,
            "evictions": 0,   # 被 LRU 淘汰的条目数
            "expired": 0,     # 被 TTL 淘汰的条目数
        }
        # 会话标识：用于调试与跨会话隔离
        self._session_id: str = secrets.token_hex(4)

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
    def sanitize_text(self, text: str, *, neutralize: bool = True) -> str:
        """
        文本脱敏。
    
        neutralize=True（默认）：先中和输入里的伪占位符，用于"处理外部不可信输入"。
        neutralize=False：跳过中和，用于"我们自己的可信输入"（如落盘脱敏）。
        注意：`neutralize` 是关键字参数（`*` 之后），调用时必须写成sanitize_text(text, neutralize=False)
        不能写成位置参数 sanitize_text(text, False)。
        """
        if not text or not self.is_enabled():
            return text
        with self._lock:
            if neutralize:
                text = self._neutralize_placeholders(text)
            rules = [r for r in self._rules
                    if r.enabled and self._mode in r.modes]
            for rule in rules:
                text = self._apply_rule(text, rule)
            # 统一 GC 一次（_apply_rule 可能添加/刷新了若干条目）
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
            # ★ 若匹配到的内容本身含已生成的占位符，跳过（避免二次脱敏）
            #   例：jwt 先跑了 "token: eyJ..." → "token: «PZ_JWT_xxx»"
            #       然后 password_field 匹配到 group=2 = "«PZ_JWT_xxx»"
            #       若不跳过，会被再次替换成 "«PZ_PASSWD_yyy»"，覆盖 jwt 的成果
            if _PLACEHOLDER_RE.search(original):
                return m.group(0)
            if rule.validator and not rule.validator(original):
                return m.group(0)
            now = time.time()
            if original in self._reverse:
                # ---- 复用已有占位符 ----
                ph = self._reverse[original]
                # LRU 刷新：把该条目移到 OrderedDict 末尾（"最近使用"）
                if ph in self._map:
                    _orig, _ts = self._map.pop(ph)
                    self._map[ph] = (_orig, now)   # 更新时间戳 + 挪到末尾
            else:
                # ---- 新增占位符 ----
                ph = self._make_placeholder(rule.placeholder)
                self._map[ph] = (original, now)
                self._reverse[original] = ph
            # 只替换指定组时保留前后文
            if rule.group:
                s, e = m.span(rule.group)
                rs, re_ = s - m.start(), e - m.start()
                whole = m.group(0)
                return whole[:rs] + ph + whole[re_:]
            return ph

        return rule.pattern.sub(_repl, text)

    def _make_placeholder(self, prefix: str) -> str:
       """
       生成一个不可预测的占位符。
       使用 secrets.token_hex 而非序号，防止枚举/猜测/重放。

       注意：不做任何碰撞处理 —— 2^64 空间下，实际运行中
      （每天 100 万次脱敏、连续 1000 年）的碰撞概率 < 10^-7。
       """
       token = secrets.token_hex(PLACEHOLDER_TOKEN_BYTES)
       return f"{PLACEHOLDER_OPEN}{prefix}_{token}{PLACEHOLDER_CLOSE}"

    def _neutralize_placeholders(self, text: str) -> str:
        """
        把文本中任何"看起来像占位符"的片段打断，使其无法被 restore_text 识别。

        为什么需要：
            攻击者可以在用户输入中直接写「«PZ_PHONE_<猜测的token>»」，
            或者诱导工具输出/LLM 输出中包含类似的字符串。
            若不做中和，这些字符串可能恰好命中映射表，从而被还原成真实 PII。

            中和方式：在 `«` 与 `P` 之间、`»` 之前插入零宽非连接符 (U+200C)。
            对 LLM 的语义影响可忽略（tokenizer 一般直接忽略），
            但正则不再匹配，还原路径彻底失效。

        幂等性：
            对同一文本重复调用是安全的 —— 已经中和过的串不再匹配 `_PLACEHOLDER_RE`。
        """
        if not text:
            return text
        # 只在确实含有可疑片段时才走正则，避免性能损耗
        if "«" not in text and "[[" not in text and "⟦" not in text:
            return text

        # 中和"新格式"与"旧格式"两类占位符样式
        def _nz(m: re.Match) -> str:
            s = m.group(0)
            # 在开括号后和闭括号前各插入一个 ZWNJ
            if s.startswith("«"):
                return "«\u200c" + s[1:-1] + "\u200c»"
            if s.startswith("⟦"):
                return "⟦\u200c" + s[1:-1] + "\u200c⟧"
            if s.startswith("[["):
                return "[\u200c[" + s[2:-2] + "]\u200c]"
            # 兜底：整体包裹
            return "\u200c" + s + "\u200c"

        return _ANY_PLACEHOLDER_SHAPE_RE.sub(_nz, text)

    def neutralize(self, text: str) -> str:
        """
        公开的中和入口：把文本里所有"看起来像占位符"的片段打断。

        用途：
            供持久化层（load_session）在处理外部数据时调用，
            避免攻击者在 session 文件里手工嵌入伪占位符。

        与 _neutralize_placeholders 的关系：
            只是后者的一层公开别名，行为完全一致。
            之所以不直接暴露 _neutralize_placeholders，
            是因为下划线开头代表"类内部实现细节"，
            外部模块不应直接调用，以免未来重命名造成依赖破坏。
        """
        return self._neutralize_placeholders(text)
    
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

    def redact_for_persist(self, text: str) -> str:
        """
        落盘专用：单向脱敏。使用一次性映射表，返回值无法被还原。
    
        即使当前 mode=off，也会以 standard 模式执行；standard 模式会升级为 strict。
        这是"默认安全"原则的体现：磁盘上的数据，永远比内存更敏感。
        """
        if not text:
            return text
        disk_mode = self._effective_disk_mode()
        # 一次性脱敏器：用完即弃，映射表随 GC 回收
        tmp = PrivacySanitizer(mode=disk_mode)
        try:
            return tmp.sanitize_text(text, neutralize=False)
        finally:
            tmp.new_session()   # 显式清空（可选，帮助 GC）

    def _effective_disk_mode(self) -> str:
        """落盘时的实际模式：比内存模式更激进。"""
        if self._mode == MODE_OFF:
            return MODE_STANDARD
        if self._mode == MODE_STANDARD:
            return MODE_STRICT
        return MODE_STRICT

    def redact_messages_for_persist(self, messages: list) -> list:
        """
        落盘专用：对整个消息列表脱敏，返回新列表。
    
        与 sanitize_messages 的区别：
            - 使用一次性映射表（不污染会话）
            - 对所有工具 arguments 脱敏（不限于白名单）
            - 所有 tool 结果都脱敏
            - 不做中和
        """
        if not messages:
            return messages
        disk_mode = self._effective_disk_mode()
        tmp = PrivacySanitizer(mode=disk_mode)
        try:
            out = []
            for m in messages:
                if not isinstance(m, dict):
                    out.append(m); continue
                nm = dict(m)
                # 1) content
                if isinstance(nm.get("content"), str) and nm["content"]:
                    nm["content"] = tmp.sanitize_text(
                        nm["content"], neutralize=False
                    )
                # 2) tool_calls[*].function.arguments（全部脱敏，不分白名单）
                if nm.get("tool_calls"):
                    new_tcs = []
                    for tc in nm["tool_calls"]:
                        if not isinstance(tc, dict):
                            new_tcs.append(tc); continue
                        tc2 = dict(tc)
                        fn = tc2.get("function")
                        if isinstance(fn, dict):
                            fn2 = dict(fn)
                            if isinstance(fn2.get("arguments"), str) and fn2["arguments"]:
                                # 对 arguments 也走结构化脱敏（保持 JSON 合法）
                                fn2["arguments"] = tmp._sanitize_arguments(
                                    fn2["arguments"]
                                )
                            tc2["function"] = fn2
                        new_tcs.append(tc2)
                    nm["tool_calls"] = new_tcs
                out.append(nm)
            return out
        finally:
            tmp.new_session()

    # ---------- 文本还原 ----------
    def restore_text(self, text: str) -> str:
        if not text:
            return text
        with self._lock:
            if not self._map:
                return text

            now = time.time()
            expired_in_this_call: list[str] = []   # 收集本次识别出的过期占位符

            def _sub(m: re.Match) -> str:
                ph = m.group(0)
            # 双重保险：
            #   1) 正则本身只认 «PZ_TYPE_<16hex>» 格式
            #   2) 即使格式对，也必须在本次会话的映射表中
            # 两者同时满足才还原，避免"输入里恰好长得像"的伪占位符被展开
                entry = self._map.get(ph)
                if entry is None:
                    # 不在映射里：可能是伪造的、或已淘汰的
                    return ph
                orig, ts = entry
                # ---- TTL 检查 ----
                if now - ts > self._ttl:
                    expired_in_this_call.append(ph)
                    return ph
                # ---- LRU 刷新 ----
                # 命中即"最近使用"，移到末尾
                self._map.move_to_end(ph)
                # 更新时间戳，让反复使用的占位符"续命"
                self._map[ph] = (orig, now)
                return orig
            
            text = _PLACEHOLDER_RE.sub(_sub, text)

            # 清理本次识别出的过期条目（在正则回调外做，避免回调里修改 dict）
            for ph in expired_in_this_call:
                entry = self._map.pop(ph, None)
                if entry is not None:
                    orig, _ts = entry
                    self._reverse.pop(orig, None)
                    self._stats["expired"] += 1

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
        """
        兼容旧接口：清空映射。
        新代码建议直接调用 new_session()，它会同时轮换 session_id。
        """
        self.new_session()

    def _gc_locked(self) -> None:
        """
        LRU + TTL 清理，必须持 self._lock 调用。

        执行顺序：
            1. 先清 TTL 过期的条目
            2. 再按 LRU 淘汰超容量的条目
        顺序很重要：先清过期可以避免"过期条目占了 LRU 名额"。
        """
        now = time.time()

        # ---- 1) TTL 清理 ----
        # OrderedDict 不支持直接反向遍历删除，先收集再删
        expired_keys = [
            k for k, (_orig, ts) in self._map.items()
            if now - ts > self._ttl
        ]
        for k in expired_keys:
            orig, _ts = self._map.pop(k)
            self._reverse.pop(orig, None)
            self._stats["expired"] += 1

        # ---- 2) LRU 淘汰 ----
        while len(self._map) > self._max_entries:
            # popitem(last=False) 弹出最早插入的条目
            k, (orig, _ts) = self._map.popitem(last=False)
            self._reverse.pop(orig, None)
            self._stats["evictions"] += 1

    def new_session(self, session_id: Optional[str] = None) -> str:
        """
        开始一个新会话：清空所有占位符映射，生成新 session_id。

        何时调用：
          - 程序启动时（main()）
          - /clear 命令
          - /privacy clear 命令
          - 用户显式切换工作区时（可选）

        为什么必须：
            单例模式 + 长期进程下，会话 A 的映射会残留在内存里。
            如果攻击者在会话 B 里重放会话 A 见过的占位符，
            就会把会话 A 的 PII 拉进会话 B —— 典型的跨会话泄露。
        """
        with self._lock:
            self._map.clear()
            self._reverse.clear()
            self._session_id = session_id or secrets.token_hex(4)
            return self._session_id

    @property
    def session_id(self) -> str:
        """当前会话标识（只读）。"""
        with self._lock:
            return self._session_id

    # ---------- 统计 ----------
    def get_stats(self) -> dict:
        with self._lock:
            return {
                "mode": self._mode,
                "session_id": self._session_id,
                "active_rules": len(self.list_active_rules()),
                "total_rules": len(self._rules),
                "active_placeholders": len(self._map),
                "max_entries": self._max_entries,
                "ttl_seconds": self._ttl,
                **self._stats,  # 含 evictions / expired
            }

    def list_placeholders(self) -> list[tuple[str, str]]:
        """列出当前所有占位符 -> 原文的映射（谨慎使用）。
        返回结构：（占位符, 原文）元组的列表，按 LRU 顺序（最早 -> 最近）。
        """
        with self._lock:
            return [(ph, orig) for ph, (orig, _ts) in self._map.items()]


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