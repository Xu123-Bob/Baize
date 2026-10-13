<div align="center">

<img src="image/logopage02.png" alt="Baize Logo" width="320" />

# Baize 白泽

**Speak all you know; keep all secrets.**

<p align="center">
  <a href="https://atomgit.com/Com_Xu/Baize">
    <img src="https://atomgit.com/Com_Xu/Baize/star/new_badge.svg" alt="AtomGit">
  </a>
  &nbsp;&nbsp;
  <a href="https://trendshift.io/repositories/233391?utm_source=trendshift-badge&amp;utm_medium=badge&amp;utm_campaign=badge-trendshift-233391" target="_blank" rel="noopener noreferrer">
    <img src="https://trendshift.io/api/badge/trendshift/repositories/233391/daily?language=JavaScript" alt="Xu123-Bob%2FBaize | Trendshift" width="250" height="55"/>
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
</p>

<p align="center">
  <a href="https://github.com/Xu123-Bob/Baize/releases">
    <img src="https://img.shields.io/github/v/release/Xu123-Bob/Baize?style=flat-square&logo=github&label=Release&include_prereleases" alt="GitHub release">
  </a>
  <a href="https://www.python.org/downloads/">
    <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python 3.10+">
  </a>
  <a href="image/抖音.png">
    <img src="https://img.shields.io/badge/Douyin-Scan%20to%20Follow-FE2C55?style=flat-square&logo=douyin&logoColor=white" alt="Douyin">
  </a>
</p>

<p align="center">
  <a href="README.cn.md">简体中文</a> |
  <a href="README.en.md">English</a> |
  <a href="README.ja.md">日本語</a> |
  <a href="README.ko.md">한국어</a> |
  <a href="README.es.md">Español</a> |
  <a href="README.fr.md">Français</a> |
  <a href="README.ru.md">Русский</a>
</p>

</div>

----------

A secure assistant for Vibe Coding and data analysis, inspired by the Chinese mythical beast Baize.

**An open-source Coding Agent CLI with strong privacy protection and multilingual interaction. It supports multiple backends (DeepSeek / OpenAI-compatible / Zhipu / Qwen / Kimi / Ollama local) and provides a complete set of capabilities including tool calling, skill loading, subagent delegation, context compression, and secure sandboxing.**

----------

# Core Advantages

## Privacy Protection

- **Bidirectional reversible privacy protection**: Sensitive information is replaced with placeholders before being sent to the LLM, and automatically restored after receiving the response. The whole process is transparent to the user — the history, tool parameters, and final answers you see are always the original text, while the LLM only ever sees random unguessable placeholders such as `«PZ_PHONE_a3f8b2c1d4e5f6a7»`.
- **Full redaction at rest**: Session files, compressed transcripts, and audit logs are automatically redacted before being written to disk (enabled by default). Plaintext PII never appears on disk.
- **Injection resistance**: Placeholders use 64-bit cryptographic random tokens, making them impossible to enumerate, forge, or replay. Old placeholders become invalid immediately after switching sessions.
- **Multiple ways to enable privacy protection**: You can enable privacy protection by entering natural language in the command line, or use the more precise `/privacy` command.
- **Local-first agent**: This product has no remote database and runs fully locally. It does not collect user information.

## Multilingual Interaction

- **Supports nine languages**: Chinese, English, Japanese, Korean, Spanish, French, German, Russian, Arabic.
- **Multiple ways to switch languages**: You can directly say `please speak with english` to switch to English, or use `/lang ja` to switch to Japanese.

# Features

- **Multi-backend support**: DeepSeek, any OpenAI-compatible endpoint (GLM / Qwen / Kimi / OpenAI), and local Ollama. One-click switching.

- **Zero-config startup**: Automatically generates configuration files on first run. Users only need to fill in the key once.

- **Privacy redaction**: Automatically identifies and redacts **30+ categories** of sensitive information before sending to the LLM (phone numbers, emails, ID cards, passports, bank cards, international numbers, API keys, JWTs, database connection strings, MAC addresses, etc.), and automatically restores them after receiving the response. **Redaction also applies at rest**, leaving no plaintext on disk. Supports Standard / Strict two-level modes, switchable via natural language or `/privacy`.

- **Multilingual interaction**: Freely switch among Chinese / English / Japanese / Korean / Spanish / French / German / Russian / Arabic. Just say `English` or use `/lang ja`, and the AI will think and reply in the corresponding language throughout the session.

- **Complete toolchain**: bash execution, file read/write/edit, glob/grep search, web search and fetch, background tasks, task and todo management.

- **Skills system**: Load domain knowledge (SKILL.md) on demand, making the AI more professional in specific scenarios.

- **Subagents**: Delegate complex tasks to subagents with independent contexts to avoid polluting the main session.

- **Hooks**: Python or Shell hooks. Supports pre/post tool-call interception, audit logs, automatic formatting, and test gating.

- **MCP protocol**: Connect external tool servers through Model Context Protocol (GitHub, Filesystem, etc.).

- **Context compression**: Two-level compression (tool result truncation + LLM summarization). Supports ultra-long conversations.

- **Secure sandbox**: Command allowlist, path escape detection, dangerous command interception, sensitive file protection, and script injection interception.

- **Black-gold themed CLI**: Adaptive Chinese width, code highlighting, diff coloring, and thinking folding.

# Baize CLI Interface

<div align="center">
Baize CLI startup screen
</div>

<p align="center">
  <img src="image/clipage01.jpg" alt="Baize CLI startup screen" width="800" />
</p>

<div align="center">
Baize CLI running screen — 01
</div>

<p align="center">
  <img src="image/clipage02.jpg" alt="Baize CLI running screen" width="800" />
</p>

<div align="center">
Baize CLI running screen — 02
</div>

<p align="center">
  <img src="image/clipage03.jpg" alt="Baize CLI running screen" width="800" />
</p>

# Installation

## Prerequisites

- Python 3.10+ (requires tomllib, built into 3.11+; for 3.10 install tomli)

- pip

## Install from Source

### Two Download Methods

1. `pip install https://github.com/Xu123-Bob/Baize.git`

    bash -- Press Win+R, enter `cmd`, then enter:

    baize

2. On the repository page, click `<> Code` --> `Download ZIP`

(1) After unzipping, enter the file directory:

    bash -- Press Win+R, enter cmd

    cd path/to/extracted-directory

    pip install -r requirements.txt

    python -m Baize

After installation, press Win+R, enter `cmd` to open the CLI, then enter `baize` to run.

(2) Download the ZIP and install locally. After unzipping, enter the directory and run:

    bash -- Press Win+R, enter cmd

    pip install .

After installation, press Win+R, enter `cmd` to open the CLI, then enter `baize` to run.

### Optional: Install Data Access Dependencies (Important Tools for Data Analysis)

If you need Baize to drive SPSS or SQL databases, install the extra dependencies:

```bash
pip install -r requirements-data.txt
```

`requirements-data.txt` includes:
- `spss-studio-mcp`: SPSS statistical analysis MCP server (requires IBM SPSS Statistics installed locally)
- `atengk-mcp-server-rdbms`: General relational database MCP server (PostgreSQL / MySQL / SQL Server / Oracle / DM, etc.)
- `pyodbc`: ODBC Python binding required by SQL Server

Alternatively, if the project is installed via `pyproject.toml`, you can also use extras:

```bash
pip install -e ".[data]"          # Install all data access dependencies at once
pip install -e ".[spss]"          # Install only SPSS
pip install -e ".[sql]"           # Install only general SQL
pip install -e ".[sql-mssql]"     # SQL Server only (including pyodbc)
```

- **⚠️ SQL Server users: `pyodbc` is only the Python binding. You also need to install Microsoft ODBC Driver 18 for SQL Server at the system level.**
- **⚠️ SPSS users: `spss-studio-mcp` is only an MCP bridge layer. IBM SPSS Statistics (version 20–31) must already be installed locally and properly licensed, and the `SPSS_INSTALL_PATH` environment variable must point to the SPSS installation directory. Currently, the SPSS engine mainly supports full analysis on Windows; on Linux/macOS it can fall back to "file mode" (read .sav files, view metadata, preview data, but no statistical analysis).**

# Quick Start

1. First Run

```bash
baize
```

On first run, Baize automatically generates two configuration files:

```
~/.baize/config.toml   # Backend configuration (choose DeepSeek / OpenAI / Ollama)
~/.baize/.env          # Secrets file
```

Windows path: `C:\Users\YourUserName\.baize\`.

2. Choose a Backend

Open `~/.baize/config.toml` and modify **active_provider** (must be modified):

```toml
# Baize configuration file
# Modify active_provider to switch backend  # Options: "deepseek" / "qwen" / "kimi" / "glm" / "openai" / "ollama"

active_provider = "deepseek"

[model_providers.deepseek]
name = "DeepSeek"
base_url = "https://api.deepseek.com"
env_key = "DEEPSEEK_API_KEY"
model = "deepseek-flash"

[model_providers.qwen]
name = "Qwen"
base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1"
env_key = "DASHSCOPE_API_KEY"
model = "qwen-plus"

[model_providers.kimi]
name = "Kimi"
base_url = "https://api.moonshot.cn/v1"
env_key = "MOONSHOT_API_KEY"
model = "kimi-k2.7-code"

[model_providers.glm]
name = "GLM"
base_url = "https://open.bigmodel.cn/api/paas/v4"
env_key = "ZHIPUAI_API_KEY"
model = "glm-4-plus"

[model_providers.openai]
name = "OpenAI"
base_url = "https://api.openai.com/v1"
env_key = "OPENAI_API_KEY"
model = "gpt-4o"

[model_providers.ollama]
name = "Ollama (local)"
base_url = "http://localhost:11434/v1"
env_key = ""
model = "qwen2.5:7b"
```

3. Fill in the API Key

Edit `~/.baize/.env`. **If you need to use a certain LLM, remove the leading `# ` for it, and add `# ` before other LLMs to lock their API output. After entering the API Key, be sure to save. It only takes effect after saving**:

```env
# ============================================================
# Baize secrets file
# ============================================================
# Only fill in the key for the backend you use; keep others commented out.
# Variable names must match the env_key field in config.toml.
#
# Location:
#   Linux / macOS: ~/.baize/.env
#   Windows:       C:\Users\YourUserName\.baize\.env
# ============================================================

# ---------- DeepSeek (default backend) ----------
# Get it at: https://platform.deepseek.com/api_keys
DEEPSEEK_API_KEY=

# ---------- OpenAI or any OpenAI-compatible endpoint (optional) ----------
# For Groq, Qwen, Moonshot, Zhipu, OpenAI, etc.
# Note: base_url is configured in config.toml under [model_providers.xxx], not here
# OPENAI_API_KEY=

# ---------- Qwen (optional) ----------
# Get it at: https://dashscope.console.aliyun.com/
# DASHSCOPE_API_KEY=

# ---------- Kimi / Moonshot (optional) ----------
# Get it at: https://platform.moonshot.cn/console/api-keys
# MOONSHOT_API_KEY=

# ---------- Zhipu GLM (optional) ----------
# Get it at: https://open.bigmodel.cn/usercenter/apikeys
# ZHIPUAI_API_KEY=

# ---------- Custom gateway (optional) ----------
# CUSTOM_API_KEY=

# ---------- Ollama (local model, no key required) ----------
# Just make sure Ollama is running at localhost:11434. No configuration needed here.
```

4. Restart

```bash
baize
```

If you see the black-gold logo and welcome message, startup was successful.

# Usage Examples

After startup, describe your needs in natural language at the `>>> Prompt:` prompt:

```
>>> Prompt: Write a Python script to scrape Douban Top250 and save it as CSV

>>> Prompt: Help me check type errors in all Python files under src/

>>> Prompt: Find all places in this repository that use requests, and change them to httpx
```

## Multilingual Interaction

Baize supports **nine languages**: Chinese, English, Japanese, Korean, Spanish, French, German, Russian, Arabic.

There are two ways to switch:

### Option 1: Just Speak (Auto-detect)

Baize automatically detects the language of your input and switches:

```
>>> Prompt: Hello, help me write a Python script
[System] Input language detected as English. Baize has switched to English interaction.
(Baize replies in English)

>>> Prompt: 日本語で答えてください
[System] Input language detected as 日本語. Baize has switched to 日本語 interaction.
(Baize replies in Japanese)
```

### Option 2: Manual Command

```
>>> Prompt: /lang                # View current language and available list
[System] Current language: Chinese (zh)
[System] Available languages:
    zh    Chinese ←
    en    English
    ja    日本語
    ko    한국어
    es    Español
    fr    Français

>>> Prompt: /lang English        # Switch by language name
>>> Prompt: /lang ja             # Switch by language code
>>> Prompt: /lang 西班牙语        # Chinese names are also supported
```

Supports four forms: **language name / language code / Chinese name / native name**. For example, to switch to English, any of `English`, `en`, `英语`, or `英文` works.

## Built-in Commands

- `/exit, /quit` --> Exit Baize
- `/clear` --> Clear conversation history, todos, thinking records, and tool records
- `/compact` --> Manually compress context (use when the conversation is too long)
- `/commit` --> Save the current session and commit to Git (if inside a Git repository)
- `/lang` --> View current language; `/lang en` switches to English (supports language code or language name)
- `/skills` --> List all available skills
- `/skills reload` --> Reload the user skills directory
- `/unload` --> Unload the currently active skill
- `/show thought` --> View full thinking records
- `/show tool` --> View tool call records
- `/show all` --> View all session history
- `/技能名` --> Load the specified skill (supports fuzzy matching)
- `/privacy` --> Privacy redaction control (on / off / strict / status / rules / test / clear)
- `/privacy rule-off <name>` --> Disable a redaction rule (e.g. `/privacy rule-off phone_intl`)
- `/privacy rule-on  <name>` --> Re-enable a rule

## Data Access Usage Examples

After configuring SPSS / SQL, you can drive them directly with natural language:

```text
>>> Prompt: Use SPSS to open data.sav and tell me the variable list and sample size

>>> Prompt: Run descriptive statistics on data.sav, then run a linear regression

>>> Prompt: Query orders in the sales table with sales amount over 100,000 last month, grouped by customer

>>> Prompt: Export the SPSS analysis results to CSV, then join with customer master data using SQL
```

# Local Ollama Models (Zero Cost)

Don't want to use a cloud API? Use local Ollama:

```bash
# 1. Install Ollama: https://ollama.com/download
# 2. Pull a model
ollama pull qwen2.5:7b

# 3. Start the Ollama service
ollama serve

# 4. Modify ~/.baize/config.toml
active_provider = "ollama"

# 5. Start Baize
baize
```

Recommended models: `qwen2.5:7b` (strong Chinese), `llama3.1:8b`, `deepseek-r1:7b`.

# Extension Mechanisms

Baize supports four extension methods. Put them in the current working directory and they will take effect.

## Skills

Write domain knowledge in `./skills/skill-name/SKILL.md`. The AI will proactively load them when encountering complex tasks.

```markdown
---
name: pandas-eda
description: Best practices for exploratory data analysis with pandas
tags: data,python
---

# Pandas EDA Guide

## Core Steps
1. Use df.info() to inspect field types and missing values
2. Use df.describe() for descriptive statistics
...
```

You can also manually load it in conversation with `/pandas-eda`.

## Subagents

Define dedicated subagents in `./subagent/role-name/AGENT.md`. The main agent can delegate tasks through the agent tool.

```markdown
---
name: code-reviewer
description: Strict code reviewer
---

You are a senior code reviewer. When reviewing, prioritize:
1. Boundary conditions and exception handling
2. Resource leaks
3. Concurrency safety
...
```

## Hooks

Place the following under `./hooks/`:

- `PreToolUse-*.sh`
- `PostToolUse-*.sh`
- `Stop-*.sh`

They receive JSON input and return decisions:

```bash
#!/bin/bash

# PreToolUse-guard.sh

read -r input

if echo "$input" | grep -q "rm -rf"; then
  echo '{"hookSpecificOutput":{"permissionDecision":"block","permissionDecisionReason":"Deletion prohibited"}}'
fi
```

Python hooks can directly call built-in APIs (see the `hook_*` functions in `Baize.py`).

## MCP Servers

Configure external tool servers in `./MCP/mcp_config.json`:

```json
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
```

# Security Design (Core)

Baize enables the following security mechanisms by default:

- **Command allowlist**: Only common commands such as `ls`, `cat`, `grep`, `git`, `python3`, etc. are allowed.
- **Path escape detection**: All file operations are restricted to the current working directory and `/tmp`.
- **Dangerous command interception**: Intercepts patterns such as `rm -rf /`, fork bombs, `curl | sh`, `git push --force`, etc.
- **Sensitive file protection**: Prohibits modification of `.env`, `.ssh/`, `id_rsa`, `*.pem`, etc.
- **Script injection interception**: Detects bypasses such as `python -c "os.system(...)"`.
- **Process resource limits**: Limits CPU, memory, and process count on Linux/macOS.
- **Privacy redaction (bidirectional reversible)**: PII is replaced with random placeholders outbound and restored inbound; independent redaction at rest.
- **Placeholder injection resistance**: 64-bit cryptographic random tokens + input-side neutralization + session isolation.
- **Audit log redaction**: `hook_audit_log` redacts before writing to disk + truncates + refuses to write on failure.

If you need to relax restrictions in trusted projects, you can modify `ALLOWED_COMMANDS` and `FORBIDDEN_PATH_PATTERNS` in `Baize.py`.

# Privacy Redaction (Core)

Baize has a built-in **bidirectional reversible + at-rest redaction** privacy protection mechanism, covering the full path from input to disk:

- **Outbound**: Before sending to the LLM, PII is replaced with unguessable placeholders
- **Inbound**: Placeholders in LLM responses are restored to the original text
- **At rest**: Session files, compressed transcripts, and audit logs are **independently redacted** before being written to disk. No plaintext remains on disk

**Disabled by default**, enable when needed.

## Two Ways to Enable

### Option 1: Natural Language

Say directly in the conversation:

```
>>> Prompt: Enable privacy redaction
[System] Privacy redaction enabled (Standard mode).

>>> Prompt: Enable strict redaction
[System] Privacy redaction enabled (Strict mode).

>>> Prompt: Disable privacy protection
[System] Privacy redaction disabled.
```

### Option 2: Slash Commands

- `/privacy on` Enable Standard mode
- `/privacy strict` Enable Strict mode
- `/privacy off` Disable
- `/privacy status` View status, session ID, rule count, LRU/TTL statistics
- `/privacy rules` List all rules (including enabled status)
- `/privacy rule-off <name>` Disable a rule
- `/privacy rule-on  <name>` Re-enable a rule
- `/privacy test <text>` Test redaction effect
- `/privacy clear` Clear placeholder mapping and **rotate session ID**

## Two Levels

**Standard**: Mainland China mobile phone numbers, ID card numbers, bank card numbers (Luhn check), emails, IPv4/IPv6, OpenAI/Anthropic/GitHub/AWS API keys, Bearer tokens, private key blocks, password fields, URL credentials.

**Strict**: Everything in Standard + Chinese names, QQ numbers, WeChat IDs, Mainland China license plate numbers.

## How It Works

User input (containing real PII) → messages store original text

↓ `sanitize_messages()`

What is sent to the LLM is `[[PHONE_1]]`, `[[EMAIL_1]]`

↓ LLM response

Returned placeholders → `restore_message()`

Restored to original text → written to disk / displayed / tool execution

- **Privacy redaction (bidirectional reversible)**: PII is replaced with random placeholders outbound and restored inbound; independent redaction at rest.
- **Placeholder injection resistance**: 64-bit cryptographic random tokens + input-side neutralization + session isolation.
- **Audit log redaction**: `hook_audit_log` redacts before writing to disk + truncates + refuses to write on failure.

## Smart Grading of Tool Parameters

**Will be redacted** (plain text parameters, not involved in actual execution):
- `todo`, `ask_user_question`, `task_create`, `task_update`

**Not redacted** (paths/commands/URLs are actually used):
- `run_read` / `run_write` / `run_edit` / `run_glob` / `run_grep` (paths are used for IO)
- `run_bash` / `background_run` (commands are executed)
- `run_webfetch` / `web_search` (URLs are actually sent to the network)
- `set_workspace` (path is used for `chdir`)
- `load_skills` (skill names are enumerations)
- `agent` (subagent context is independently redacted)
- `mcp_*` (unknown semantics, handled conservatively)

**All redacted when persisted** (because persisted content will not be re-executed; security first).

## Redaction at Rest

**Enabled by default**, independent of in-memory redaction. Even if `/privacy off` is used (no in-memory redaction), at-rest redaction still follows at least the Standard rules.

**Key features**:
- At-rest redaction uses an **independent, one-time mapping table** — placeholders written to disk **cannot be restored**, because the mapping table is discarded
- If at-rest redaction **fails, it refuses to write plaintext** (no downgrade, no silent skip)
- If old session files contain plaintext, they are automatically redacted and rewritten on first save

**How to disable** (not recommended): Modify `PERSIST_REDACT_ENABLED = False` in `Baize.py`.

## Example

```
>>> Prompt: /privacy test My phone number is 13812345678, email is a@b.com
Original: My phone number is 13812345678, email is a@b.com
Redacted: My phone number is [[PHONE_1]], email is [[EMAIL_1]]
Restored: My phone number is 13812345678, email is a@b.com

>>> Prompt: /privacy status
[Privacy Redaction]
Current mode : Standard mode (standard)
Session ID : 7d2f5e91
Enabled rules : 34 / 41
Active placeholders : 2
Mapping capacity : 2 / 2000
TTL : 86400 seconds
LRU evictions : 0
TTL evictions : 0
Redaction calls: 3
Restore calls: 3

>>> Prompt: /privacy rules
[Privacy Redaction Rule List] Total 41
[Standard + Strict]
[✓] phone_cn Mainland China mobile phone number (standard,strict)
[✓] id_card_cn Mainland China ID card number (standard,strict)
[✓] jwt JWT Token (standard,strict)
...
[Strict only]
[✓] name_cn Chinese name (strict)
[✓] address_cn Chinese detailed address (strict)
...
Usage:
/privacy rule-off <name> Disable a rule
/privacy rule-on <name> Re-enable a rule
```

### Test Examples

<div align="center">
Privacy protection test screen — 01
</div>

<p align="center">
  <img src="image/privary01.jpg" alt="Privacy protection test screen" width="800" />
</p>

<div align="center">
Privacy protection test screen — 02
</div>

<p align="center">
  <img src="image/privary02.jpg" alt="Privacy protection test screen" width="800" />
</p>

# Data Access (Core)

Baize connects to enterprise data analysis software through **MCP (Model Context Protocol)**. The main program requires no modification — simply register the server in `MCP/mcp_config.json`.

## SPSS Integration

### Prerequisites

- IBM SPSS Statistics installed locally (version 20–31; Windows recommended)
- SPSS is licensed and can start normally

### Configuration Steps

1. **Find the SPSS installation directory:** The default path is usually `C:\Program Files\IBM\SPSS Statistics\` followed by the version number (e.g. 31).

2. **Set the environment variable** (can be in `.env` or system environment variables):

```text
SPSS_INSTALL_PATH=C:\Program Files\IBM\SPSS Statistics\31
```

3. **Verify status**:

```bash
spss-studio-mcp status
```

Expected output:

```text
=== SPSS MCP Capability Status ===
pyreadstat : OK v1.3.6
pandas     : OK v3.0.2
SPSS batch : OK
```

4. **Register in `MCP/mcp_config.json`**:

```json
{
  "mcpServers": [
    {
      "name": "spss",
      "command": "spss-studio-mcp",
      "args": ["serve", "--transport", "stdio"],
      "env": {
        "SPSS_INSTALL_PATH": "C:\\Program Files\\IBM\\SPSS Statistics\\31"
      },
      "enabled": true
    }
  ]
}
```

### If `SPSS batch: NOT FOUND`

This means `spss-studio-mcp` did not find the SPSS engine, but `pyreadstat` + `pandas` are working. In this case it enters **file mode**:

- Can read `.sav`, view metadata, preview data, and convert CSV ↔ SAV
- Cannot run statistics (t-test, regression, ANOVA, etc.)

Solution: correctly set `SPSS_INSTALL_PATH` in `MCP/mcp_config.json`, or accept file mode fallback.

## SQL Integration

### Supported Databases

PostgreSQL, MySQL, MariaDB, SQL Server, Oracle, DM, KingbaseES, TiDB, OceanBase, etc. (based on SQLAlchemy 2.0 drivers).

### Configuration Steps

1. **Prepare a read-only database account** (strongly recommended):

```sql
CREATE USER baize_ro WITH PASSWORD 'xxx';
GRANT SELECT ON ALL TABLES IN SCHEMA public TO baize_ro;
```

2. **Prepare the connection string**:

- PostgreSQL --> `postgresql+psycopg://user:pwd@host:5432/db`
- MySQL --> `mysql+pymysql://user:pwd@host:3306/db`
- SQL Server --> `mssql+pyodbc://user:pwd@host:1433/db?driver=ODBC+Driver+18+for+SQL+Server`
- Oracle --> `oracle+oracledb://user:pwd@host:1521/?service_name=ORCL`

3. **Register in `MCP/mcp_config.json`**:

```json
{
  "mcpServers": [
    {
      "name": "sql",
      "command": "atengk-mcp-server-rdbms",
      "args": ["--transport", "stdio"],
      "env": {
        "DATABASE_URL": "postgresql+psycopg://baize_ro:pwd@localhost:5432/prod"
      },
      "enabled": true
    }
  ]
}
```

### Security Guardrails (Built-in)

`atengk-mcp-server-rdbms` provides multiple layers of protection:

- **AST-level SELECT guard**: Parses the syntax tree with `sqlglot` and physically blocks write operations such as `DELETE/UPDATE/DROP/TRUNCATE`.
- **Automatic LIMIT injection**: Queries without a specified row count are forced to append `LIMIT 100` to prevent full-table scans from causing memory overflow.
- **Read-only by default**: Write operations must be explicitly authorized via `--allow-dml` / `--allow-ddl`.
- **SQL injection interception**: Rejects malicious statements constructed through string concatenation at the AST layer.

### Configure Multiple Databases at Once

If you want to connect to multiple databases at the same time, register multiple servers:

```json
{
  "mcpServers": [
    {
      "name": "sql_prod",
      "command": "atengk-mcp-server-rdbms",
      "args": ["--transport", "stdio"],
      "env": { "DATABASE_URL": "postgresql+psycopg://ro:pwd@prod:5432/db" },
      "enabled": true
    },
    {
      "name": "sql_warehouse",
      "command": "atengk-mcp-server-rdbms",
      "args": ["--transport", "stdio"],
      "env": { "DATABASE_URL": "mysql+pymysql://ro:pwd@dw:3306/analytics" },
      "enabled": true
    }
  ]
}
```

Baize will automatically merge all their tools into `MATERTOOLS`, and the LLM will automatically choose based on the task.

# Directory Structure

```
baize-agent/
├── pyproject.toml              # Packaging configuration
├── requirements-data.txt       # Data access dependencies (optional)
├── requirements-data           # Data access dependencies
├── README.md
├── tests/                      # Tests (not published with the package)
|   ├── __init__.py
|   ├── test_history.py
|   └── test_skill_loader.py
├── .env.example                # Environment variable example
├── .gitignore
└── agent/                      # Main package
    ├── __init__.py
    ├── Baize.py                # Main program and Agent Loop
    ├── config.py               # Multi-backend configuration loading
    ├── ui_theme.py             # CLI rendering theme
    ├── utils.py                # General utilities
    ├── logo.txt
    ├── skills/                 # Built-in skills
    ├── subagent/               # Built-in subagents
    ├── core/                   # Core logic (side-effect free, unit-testable)
    |   ├── __init__.py
    |   ├── history.py          # Session history cleanup / token estimation / compression
    |   └── privacy.py          # Privacy redaction: PII detection / placeholder replacement / reversible restore
    ├── hooks/                  # Built-in hooks
    └── MCP/                    # MCP client and configuration
        ├── __init__.py
        ├── mcp_client.py
        └── mcp_config.json
```

# Environment Variables Reference

| Variable | Description | Default |
| --- | --- | --- |
| `DEEPSEEK_API_KEY` | DeepSeek API key | — |
| `DEEPSEEK_BASE_URL` | DeepSeek endpoint | `https://api.deepseek.com` |
| `OPENAI_API_KEY` | OpenAI-compatible endpoint key | — |
| `OPENAI_BASE_URL` | OpenAI-compatible endpoint | `https://api.openai.com/v1` |
| `OLLAMA_BASE_URL` | Ollama service address | `http://localhost:11434` |

**Write the above variables into `~/.baize/.env`; no need to modify shell configuration files.**

Data analysis variables:

| Variable | Description | Default |
| --- | --- | --- |
| `SPSS_INSTALL_PATH` | IBM SPSS Statistics installation directory | — (falls back to file mode if unset) |
| `DATABASE_URL` | Database connection string for SQL MCP | — (read by the MCP server) |

**Write the above variables into `MCP/mcp_config.json`.**

# Development

## Run Tests

This project uses pytest. Before development, install the package in editable mode with development dependencies:

```bash
pip install -e ".[dev]"
```

Run all tests:

```bash
python -m pytest tests/ -v
```

Run a single file:

```bash
python -m pytest tests/test_history.py -v
```

## Code Structure Conventions

- `agent/`: The main package published with the package. All runtime logic and resources (skills, subagent, hooks, MCP) are here.
- `agent/core/`: Pure logic modules with no external side effects. **They must be independently testable.** Add new logic of this kind here, with tests.
- `tests/`: One-to-one correspondence with source files under `agent/`, named `test_<module>.py`.
- Any function with external dependencies (network, disk, global state) should inject dependencies through parameters so they can be replaced in tests.

# ❓ FAQ

- Q: Where should I put the API key?

A: `~/.baize/.env`, not the `.env` in the project root.

- Q: Do I need to reinstall when switching backends?

A: No. Just change `active_provider` in `~/.baize/config.toml`.

- Q: Does local Ollama require an API key?

A: No. Set `active_provider = "ollama"` and leave `env_key` empty.

- Q: How do I switch the working directory?

A: In conversation, directly say "switch to /path/to/project", and Baize will call the `set_workspace` tool.

- Q: What happens when the context is too long?

A: Baize automatically performs two-level compression: first truncates old tool results, then requests the LLM to generate a summary. You can also manually use `/compact`.

- Q: Will it accidentally delete my files?

A: The default command allowlist intercepts dangerous operations such as `rm -rf /`; before writing files, it shows a Diff and requests confirmation.

- Q: How do I let Baize connect to SPSS?

A: 1. Install `pip install -r requirements-data.txt`; 2. Set the `SPSS_INSTALL_PATH` environment variable to point to the SPSS installation directory; 3. Enable the spss server in `MCP/mcp_config.json`. See the "Data Access (SPSS / SQL)" section for details.

- Q: What should I do about `SPSS batch: NOT FOUND`?

A: This means the SPSS engine was not found. Check whether `SPSS_INSTALL_PATH` correctly points to the directory containing `stats.exe`; if you only process `.sav` files, you can ignore this warning (it will fall back to file mode).

- Q: What extra things do I need to install to connect to a SQL database?

A: At the Python level, install `atengk-mcp-server-rdbms` (`pip install` handles it automatically). **SQL Server users also need to install Microsoft ODBC Driver 18 at the system level**, which cannot be installed with pip.

- Q: Will Baize accidentally delete my database data?

A: No. SQL MCP only allows SELECT by default, and blocks all write operations at the AST syntax-tree level. It is still strongly recommended to create a separate **read-only database account** for Baize as a double safeguard.

- Q: Will data in SPSS analysis results be leaked to the LLM?

A: If privacy redaction is enabled (`/privacy on`), tool return results are automatically redacted for PII such as phone numbers, emails, and ID cards before being sent to the LLM. **However, it is recommended to also use a read-only database account + data sampling** (query only necessary fields) to reduce risk.

- Q: Why does Baize become slower and use more tokens in every conversation after adding SPSS/SQL?

A: Because the tool definitions exposed by MCP servers are sent to the LLM with every round of conversation. SPSS has 60+ tools, adding about 6,000–12,000 tokens of fixed overhead. If your common workflow does not involve SPSS, you can set its `enabled` to `false` and turn it on when needed.

# 🤝 Contributing

Issues and PRs are welcome. It is recommended to read `CONTRIBUTOR.md` before submitting a PR.

### Thank you for every Contributor to Submit PR

- GitHub Contributors:
[@anupamme](https://github.com/anupamme)
[@wangyipeng0724](https://github.com/wangyipeng0724)

[![Contributors](https://contrib.rocks/image?repo=Xu123-Bob/Baize&v=2)](https://github.com/Xu123-Bob/Baize/graphs/contributors)

# License

MIT License

# Acknowledgements

- This project is hosted on AtomGit in China. Project link: https://atomgit.com/Com_Xu/Baize

- Thanks to AtomGit for including this project in the G-star incubation program.

- Thanks to PR contributors, Douyin followers, and students who follow me.

- Inspired by excellent AI Coding tools such as Claude Code and Codex.

- Built on DeepSeek, OpenAI SDK, and MCP.

- Thanks to all developers walking the Vibe Coding path together.

# ☕ Sponsor

If Baize is useful to you, welcome to sponsor and support. Independent development also takes a lot of time. Sponsorship will not change the product update schedule. Thank you for your support!

<p align="center">
  <img src="image/support.jpg" alt="WeChat QR code" width="200" />
</p>

# Contact Me

- If you are interested in Baize, or want to participate in open-source collaboration, you can contact me through the following ways.
- **Currently, I am job hunting. I have worked in market research and user research, and I also have some understanding of Agents. If my abilities match your needs, I hope to work with you (target roles: AI Product Operations / User Research / Market Research).**

<p align="center">
  <img src="image/weixin.jpg" alt="WeChat QR code" width="200" />
</p>

<p align="center">Scan the WeChat QR code. Please indicate Baize open-source collaboration or corporate recruitment.</p>

<p align="center">
  <img src="image/抖音.png" alt="Douyin QR code" width="200" />
</p>

<p align="center">Scan the Douyin QR code to follow.</p>