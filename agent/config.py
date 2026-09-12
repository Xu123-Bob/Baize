# agent/config.py
import os
import tomllib          # Python 3.11+ 内置
from pathlib import Path
from openai import OpenAI
import httpx
from dotenv import load_dotenv

BAIZE_HOME = Path.home() / ".baize"
CONFIG_PATH = BAIZE_HOME / "config.toml"
ENV_PATH = BAIZE_HOME / ".env"


DEFAULT_CONFIG = {
    "active_provider": "deepseek",
    "model_providers": {
        "deepseek": {
            "name": "DeepSeek",
            "base_url": "https://api.deepseek.com",
            "env_key": "DEEPSEEK_API_KEY",
            "model": "deepseek-v4-pro",
        },
        "ollama": {
            "name": "Ollama (本地)",
            "base_url": "http://localhost:11434/v1",
            "env_key": "",
            "model": "qwen2.5:7b",
        },
    },
}


def load_config() -> dict:
    """读取 ~/.baize/config.toml，不存在则写入默认配置并返回"""
    BAIZE_HOME.mkdir(parents=True, exist_ok=True)
    if not CONFIG_PATH.exists():
        _write_default_config()
        return DEFAULT_CONFIG

    # 用 utf-8-sig 读取，自动剥离 BOM（兼容 Windows 记事本保存的文件）
    try:
        text = CONFIG_PATH.read_text(encoding="utf-8-sig")
        return tomllib.loads(text)
    except tomllib.TOMLDecodeError as e:
        print(f"\033[91m[配置] {CONFIG_PATH} 格式错误：{e}\033[0m")
        print(f"\033[93m[配置] 请删除该文件让白泽重新生成，或手动检查语法。\033[0m")
        raise
    except UnicodeDecodeError:
        # 极端情况：文件不是 UTF-8（比如 GBK 保存的）
        print(f"\033[91m[配置] {CONFIG_PATH} 编码不是 UTF-8，请用 UTF-8 重新保存。\033[0m")
        raise
    


def _write_default_config():
    """首次运行时生成默认配置，方便用户编辑"""
    content = '''# 白泽配置文件
# 修改 active_provider 切换后端，然后在 shell 中设置对应的环境变量

active_provider = "deepseek"

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
model = "qwen2.5:7b"
'''
    # 用 utf-8（不带 BOM）写入
    CONFIG_PATH.write_text(content, encoding="utf-8")
    print(f"\033[90m[配置] 已生成默认配置文件：{CONFIG_PATH}\033[0m")

def _write_env_template():
    """首次运行时生成 ~/.baize/.env 模板"""
    BAIZE_HOME.mkdir(parents=True, exist_ok=True)
    if ENV_PATH.exists():
        return
    template = '''# 白泽密钥文件
# 只填你要用的后端的密钥，其余保持注释

# DeepSeek（active_provider = "deepseek" 时必填）
# 获取地址：https://platform.deepseek.com/api_keys
DEEPSEEK_API_KEY=

# OpenAI 或任意 OpenAI 兼容接口
# OPENAI_API_KEY=

# 自定义网关
# CUSTOM_API_KEY=

# Ollama 本地无需密钥
'''
    ENV_PATH.write_text(template, encoding="utf-8")
    print(f"\033[90m[配置] 已生成密钥模板：{ENV_PATH}\033[0m")


def build_client_and_model():
    """
    根据 active_provider 构建 OpenAI client 和模型名。
    返回 (client, model_name, provider_name)
    """
    config = load_config()
    load_dotenv(dotenv_path=ENV_PATH, override=False, encoding="utf-8-sig")
    active = config.get("active_provider", "deepseek")
    providers = config.get("model_providers", {})
    _write_env_template() 

    if active not in providers:
        raise RuntimeError(
            f"配置文件中 active_provider = '{active}' 未在 [model_providers] 中定义。\n"
            f"可用后端：{', '.join(providers.keys())}\n"
            f"请编辑 {CONFIG_PATH}"
        )

    prov = providers[active]
    env_key_name = prov.get("env_key", "")
    api_key = os.getenv(env_key_name) if env_key_name else "not-needed"

    if env_key_name and not api_key:
        print("\n" + "=" * 60)
        print("  白泽 · 首次配置向导")
        print("=" * 60)
        print(f"\n已生成配置文件：")
        print(f"  后端配置：{CONFIG_PATH}")
        print(f"  密钥文件：{ENV_PATH}")
        print(f"\n请编辑密钥文件，填入你的 {env_key_name}：")
        print(f"  {ENV_PATH}")
        print(f"\n在该文件中找到：")
        print(f"  {env_key_name}=")
        print(f"改成：")
        print(f"  {env_key_name}=你的真实密钥")
        print(f"\n保存后重新运行 baize。")
        print(f"\n或改为使用本地 Ollama（免费、无需密钥）：")
        print(f"  编辑 {CONFIG_PATH}，把 active_provider 改为 \"ollama\"")
        print("=" * 60)
        import sys
        sys.exit(0)

    client = OpenAI(
        api_key=api_key,
        base_url=prov["base_url"],
        timeout=httpx.Timeout(300.0, connect=10.0),
    )
    return client, prov["model"], prov["name"]

def _write_default_config():
    content = '''# 白泽配置文件
# 修改 active_provider 切换后端

active_provider = "deepseek"

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
model = "qwen2.5:7b"
'''
    CONFIG_PATH.write_text(content, encoding="utf-8", newline="\n")
    print(f"\033[90m[配置] 已生成默认配置文件：{CONFIG_PATH}\033[0m")
    
    # ===== 新增：同时生成 .env 模板 =====
    if not ENV_PATH.exists():
        env_template = '''# 白泽密钥文件
# 只填你要用的后端的密钥，其余保持注释即可
# 对应 config.toml 里的 env_key 字段

# DeepSeek（active_provider = "deepseek" 时必填）
DEEPSEEK_API_KEY=

# OpenAI 或任意 OpenAI 兼容接口（active_provider = "openai" 时必填）
# OPENAI_API_KEY=

# 自定义网关
# CUSTOM_API_KEY=

# Ollama 本地无需密钥，不用填
'''
        ENV_PATH.write_text(env_template, encoding="utf-8")
        print(f"\033[90m[配置] 已生成密钥模板：{ENV_PATH}\033[0m")
        print(f"\033[93m[配置] 请编辑该文件填入密钥，或按 Ctrl+C 退出后重新运行。\033[0m")

