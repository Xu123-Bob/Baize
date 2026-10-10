<div align="center">

<img src="image/logopage02.png" alt="白澤 Baize ロゴ" width="320" />

# 白澤 Baize

**知ることをすべて語る**

<p align="center">
  <a href="https://atomgit.com/Com_Xu/Baize">
    <img src="https://atomgit.com/Com_Xu/Baize/star/new_badge.svg" alt="AtomGit">
  </a>
  &nbsp;&nbsp;
  <a href="https://trendshift.io/repositories/233391?utm_source=trendshift-badge&amp;utm_medium=badge&amp;utm_campaign=badge-trendshift-233391" target="_blank" rel="noopener noreferrer">
    <img src="https://trendshift.io/api/badge/trendshift/repositories/233391/daily?language=JavaScript" alt="Xu123-Bob%2FBaize | Trendshift" width="250" height="55">
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
  <a href="image/抖音.png">
    <img src="https://img.shields.io/badge/抖音-扫码关注-FE2C55?style=flat-square&logo=douyin&logoColor=white" alt="抖音">
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

中国の神獣が化したVibeCodingとデータ分析の安全アシスタント。

**オープンソースの Coding Agent CLI で、強力なプライバシー保護と多言語インタラクションを備えています。複数のバックエンド（DeepSeek / OpenAI 互換 / GLM / Qwen / Kimi / ローカル Ollama）に対応し、ツール呼び出し、スキル読み込み、サブエージェント委任、コンテキスト圧縮、セキュアサンドボックスなど、完全な機能を備えています。**

----------

# 主な強み

## プライバシー保護

- **双方向かつ可逆なプライバシー保護**：機密情報は LLM に送信される前にプレースホルダーに置換され、応答受信後に自動で復元されます。ユーザーには完全に透過的で、あなたが見る履歴・ツール引数・最終回答は常に原文、LLM が見るものは常に `[[PHONE_1]]`、`[[EMAIL_1]]` のようなプレースホルダーです。
- **複数の有効化方法**：会話中の自然言語で有効化できるほか、より正確な `/privacy` コマンドも使用できます。
- **エージェントのローカル化**：本製品はリモートデータベースを持たず、完全にローカルで動作します。ユーザー情報を収集しません。

## 多言語インタラクション

- **9 言語に対応**：中文、English、日本語、한국어、Español、Français、deutsch、русский、العربية。
- **複数の言語切替方法**：`please speak with english` のように直接言語を話すと英語に切り替わり、`/lang ja` で日本語に切り替えられます。

# 特徴

- **マルチバックエンド対応**：DeepSeek、任意の OpenAI 互換 API（GLM / Qwen / Kimi / OpenAI）、ローカル Ollama をワンクリックで切り替え。

- **ゼロ設定起動**：初回実行時に設定ファイルを自動生成。ユーザーは一度だけキーを入力すればよい。

- **プライバシー脱敏**：LLM に送信する前に電話番号・メール・身分証番号・銀行カード・API Key などの個人情報を自動検出してプレースホルダーに置換し、応答受信後に自動で元に戻します。標準 / 厳格の 2 段階モードがあり、自然言語または `/privacy` コマンドで切り替え可能。

- **多言語対応**：中国語・英語・日本語・韓国語・スペイン語・フランス語・ドイツ語・ロシア語・アラビア語を自由に切替。`English` と入力するか `/lang ja` を実行するだけで、AI はその言語で思考し応答します。

- **完全なツールチェーン**：bash 実行、ファイル読み書き編集、glob/grep 検索、Web 検索と取得、バックグラウンドタスク、タスクと ToDo 管理。

- **スキルシステム（Skills）**：必要な領域知識（SKILL.md）をオンデマンドで読み込み、特定シナリオで AI をより専門的にする。

- **サブエージェント（Subagents）**：複雑なタスクを独立コンテキストのサブエージェントに委任し、メインセッションの汚染を防ぐ。

- **フック（Hooks）**：Python または Shell フック。ツール呼び出し前後のインターセプト、監査ログ、自動フォーマット、テストゲートに対応。

- **MCP プロトコル**：Model Context Protocol 経由で外部ツールサーバー（GitHub、Filesystem など）に接続。

- **コンテキスト圧縮**：二段階圧縮（ツール結果の切り詰め + LLM 要約）で、超長い会話に対応。

- **安全サンドボックス**：コマンドホワイトリスト、パス脱出検知、危険コマンド遮断、機密ファイル保護、スクリプトインジェクション遮断。

- **黒金テーマ CLI**：中国語幅の自動調整、コードハイライト、Diff 着色、思考の折りたたみ。

# 白澤 CLI 界面

<div align="center">
白澤 CLI 起動画面
</div>

<p align="center">
  <img src="image/clipage01.jpg" alt="白澤 CLI 起動画面" width="800" />
</p>

白澤 CLI 実行画面 -- 01

<p align="center">
  <img src="image/clipage02.jpg" alt="白澤 CLI 実行画面" width="800" />
</p>

白澤 CLI 実行画面 -- 02

<p align="center">
  <img src="image/clipage03.jpg" alt="白澤 CLI 実行画面" width="800" />
</p>

# インストール

## 前提条件

- Python 3.10+（tomllib が必要。3.11+ では標準搭載。3.10 では tomli をインストール）
- pip

## ソースからのインストール

### ダウンロード方法は2つ

1. `pip install https://github.com/Xu123-Bob/Baize.git`

bash -- Win+R を押して cmd と入力し、次を実行：

```bash
baize
```

2. リポジトリページで `<>Code` --> Download ZIP をクリック

(1) 解凍後、このファイルのディレクトリへ移動：

bash -- Win+R を押して cmd と入力

```bash
cd 解凍後のディレクトリ
pip install -r requirements.txt
python -m Baize
```

インストール後、Win+R で cmd を開き、CLI 界面で `baize` と入力すれば実行できる。

(2) ZIP をダウンロードしてローカルインストールする場合、解凍後にディレクトリへ入り、実行：

bash -- Win+R を押して cmd と入力

```bash
pip install .
```

インストール後、Win+R で cmd を開き、CLI 界面で `baize` と入力すれば実行できる。

### 任意：データ接続依存関係のインストール

白澤から SPSS や SQL データベースを操作する場合は、追加でインストールします：

```bash
pip install -r requirements-data.txt
```

`requirements-data.txt` には以下が含まれます：

- `spss-studio-mcp`：SPSS 統計分析 MCP server（本機に IBM SPSS Statistics がインストール済みである必要があります）
- `atengk-mcp-server-rdbms`：汎用リレーショナルデータベース MCP server（PostgreSQL / MySQL / SQL Server / Oracle / 達夢など）
- `pyodbc`：SQL Server に必要な ODBC Python バインディング

または、`pyproject.toml` でインストール済みの場合は extras を使えます：

```bash
pip install -e ".[data]"          # データ接続依存関係をすべてインストール
pip install -e ".[spss]"          # SPSS のみ
pip install -e ".[sql]"           # 汎用 SQL のみ
pip install -e ".[sql-mssql]"     # SQL Server 専用（pyodbc 含む）
```

- **⚠️ SQL Server ユーザー注意：`pyodbc` は Python バインディングのみです。システム側に Microsoft ODBC Driver 18 for SQL Server も必要です。**
- **⚠️ SPSS ユーザー注意：`spss-studio-mcp` は MCP ブリッジ層にすぎません。本機に IBM SPSS Statistics（バージョン 20–31）がインストールされ、ライセンス認証済みである必要があります。また、環境変数 `SPSS_INSTALL_PATH` を SPSS インストールディレクトリに設定してください。完全な統計分析機能は主に Windows でサポートされます。Linux/macOS では「ファイルモード」に降格できます（`.sav` の読み取り、メタデータ確認、データプレビューは可能ですが、統計分析はできません）。**

# クイックスタート

1. 初回実行

```bash
baize
```

初回実行時、白澤は2つの設定ファイルを自動生成する：

```text
~/.baize/config.toml   # バックエンド設定（DeepSeek / OpenAI / Ollama を選択）
~/.baize/.env          # キーファイル
```

Windows のパスは `C:\Users\ユーザー名\.baize\`。

2. バックエンドを選択

`~/.baize/config.toml` を開き、**`active_provider` を変更**：

```toml
# 白沢設定ファイル
# active_provider を変更してバックエンドを切り替える
# 選択可能な値："deepseek" / "qwen" / "kimi" / "glm" / "openai" / "ollama"

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
name = "Ollama (ローカル)"
base_url = "http://localhost:11434/v1"
env_key = ""
model = "qwen2.5:7b"
```

3. キーを入力

`~/.baize/.env` を編集。**どの LLM を使用するかは、前の `#` を削除し、他の LLM の前に `#` を追加して、その他の LLM API の出力をロックしてください。API キーを入力した後は、必ず保存することを忘れないでください。保存して初めて有効になります**：

```env
# ============================================================
# 白沢鍵ファイル
# ============================================================
# 使用するバックエンドの鍵のみを記入し、それ以外はコメントで保持してください。
# 変数名は config.toml の env_key フィールドと一致している必要があります。
#
# 場所：
#   Linux / macOS: ~/.baize/.env
#   Windows:       C:\Users\あなたのユーザー名\.baize\.env
# ============================================================

# ---------- DeepSeek（デフォルトバックエンド） ----------
# 取得先：https://platform.deepseek.com/api_keys
DEEPSEEK_API_KEY=

# ---------- OpenAI または任意の OpenAI 対応インターフェース（オプション） ----------
# Groq、通義、Moonshot、智譜、OpenAI などに適用可能
# 注意：base_url は config.toml の [model_providers.xxx] で設定されており、ここでは使用しない
# OPENAI_API_KEY=

# ---------- Qwen（オプション） ----------
# 取得先：https://dashscope.console.aliyun.com/
# DASHSCOPE_API_KEY=

# ---------- Kimi / Moonshot（オプション） ----------
# 取得先：https://platform.moonshot.cn/console/api-keys
# MOONSHOT_API_KEY=

# ---------- GLM（オプション） ----------
# 取得先：https://open.bigmodel.cn/usercenter/apikeys
# ZHIPUAI_API_KEY=

# ---------- カスタムゲートウェイ（オプション） ----------
# CUSTOM_API_KEY=

# ---------- Ollama（ローカルモデル、鍵不要） ----------
# Ollama が localhost:11434 で動作していることを確認するだけで、ここに設定は不要です。
```

4. 再起動

```bash
baize
```

黒金のロゴとウェルカムメッセージが表示されれば起動成功。

# 使用例

起動後、`>>> 降旨：` プロンプトで自然言語で要件を記述する：

```text
>>> 降旨：Python で Douban Top250 をスクレイピングし、CSV として保存するスクリプトを書いて

>>> 降旨：src/ 以下のすべての Python ファイルの型エラーをチェックして

>>> 降旨：このリポジトリ内で requests を使っている箇所をすべて探し、httpx に変更して
```

## 多言語インタラクション

白澤は **9 言語** をサポートします：中文、English、日本語、한국어、Español、Français、deutsch、русский、العربية。

切り替え方法は二通り：

### 方法 1：そのまま話す（自動検出）

入力を自動で言語判定して切り替えます：

```text
>>> 降旨：こんにちは、Python スクリプトを書いてください
[system] 入力言語を 日本語 と判定しました。白澤を 日本語 に切り替えました。
（日本語で応答）

>>> 降旨：Hello, write me a script
[system] 入力言語を English と判定しました。白澤を English に切り替えました。
（英語で応答）
```

### 方法 2：手動コマンド

```text
>>> 降旨：/lang                # 現在の言語と利用可能リストを表示
[system] 現在の言語：中文 (zh)
[system] 利用可能：
    zh    中文 ←
    en    English
    ja    日本語
    ko    한국어
    es    Español
    fr    Français
    de    Deutsch
    ru    Русский
    ar    العربية

>>> 降旨：/lang English        # 言語名で切替
>>> 降旨：/lang ja             # 言語コードで切替
>>> 降旨：/lang 西班牙语        # 中国語名も可
```

**言語名 / 言語コード / 中国語名 / 現地語名** をサポート。英語に切り替える場合、`English`、`en`、`英语`、`英文` のいずれでも可。

## 組み込みコマンド

- `/exit`、`/quit` --> 白澤を終了
- `/clear` --> 会話履歴、ToDo、思考記録、ツール記録をクリア
- `/compact` --> 手動でコンテキストを圧縮（会話が長すぎる場合に使用）
- `/commit` --> 現在のセッションを保存し、Git にコミット（Git リポジトリ内の場合）
- `/lang` --> 現在の言語を表示；`/lang en` で英語に切替（コードまたは名前）
- `/skills` --> 利用可能なすべてのスキルを一覧表示
- `/skills reload` --> ユーザースキルディレクトリを再読み込み
- `/unload` --> 現在有効なスキルをアンロード
- `/show thought` --> 完全な思考記録を表示
- `/show tool` --> ツール呼び出し記録を表示
- `/show all` --> すべてのセッション履歴を表示
- `/スキル名` --> 指定スキルを読み込み（あいまい一致対応）
- `/privacy` --> プライバシー脱敏の制御（下記「プライバシー脱敏」章を参照）

## データ接続の使用例

SPSS / SQL を設定した後は、自然言語で操作できます：

```text
>>> 降旨：SPSS で data.sav を開き、変数リストとサンプルサイズを教えて

>>> 降旨：data.sav に対して記述統計を実行し、その後線形回帰を実行して

>>> 降旨：sales テーブルで先月の売上が 10 万を超える注文を顧客ごとに集計して

>>> 降旨：SPSS の分析結果を CSV に出力し、SQL で顧客マスタと結合して
```

# Ollama ローカルモデル（ゼロコスト）

クラウド API を使いたくない？ローカル Ollama を使う：

```bash
# 1. Ollama をインストール：https://ollama.com/download
# 2. モデルを取得
ollama pull qwen2.5:7b

# 3. Ollama サービスを起動
ollama serve

# 4. ~/.baize/config.toml を変更
active_provider = "ollama"

# 5. 白澤を起動
baize
```

推奨モデル：`qwen2.5:7b`（中国語に強い）、`llama3.1:8b`、`deepseek-r1:7b`。

# 拡張機構

白澤は4種類の拡張方法をサポート。すべて現在の作業ディレクトリに置けば有効になる。

## スキル（Skills）

`./skills/スキル名/SKILL.md` に領域知識を書く。AI は複雑なタスクに遭遇すると主動的に読み込む。

```markdown
---
name: pandas-eda
description: pandas による探索的データ分析のベストプラクティス
tags: data,python
---

# Pandas EDA ガイド

## 核心ステップ
1. df.info() でフィールド型と欠損を確認
2. df.describe() で統計記述
...
```

会話中に `/pandas-eda` で手動読み込みもできる。

## サブエージェント（Subagents）

`./subagent/役割名/AGENT.md` に専用サブエージェントを定義。メインエージェントは `agent` ツールでタスクを委任できる。

```markdown
---
name: code-reviewer
description: 厳格なコードレビュアー
---

あなたはシニアコードレビュアーです。レビューでは以下を優先：
1. 境界条件と例外処理
2. リソースリーク
3. 並行安全性
...
```

## フック（Hooks）

`./hooks/` の下に配置：

- `PreToolUse-*.sh`
- `PostToolUse-*.sh`
- `Stop-*.sh`

JSON 入力を受け取り、判断を返す：

```bash
#!/bin/bash

# PreToolUse-guard.sh

read -r input

if echo "$input" | grep -q "rm -rf"; then
  echo '{"hookSpecificOutput":{"permissionDecision":"block","permissionDecisionReason":"削除禁止"}}'
fi
```

Python フックは組み込み API を直接呼び出せる（`Baize.py` の `hook_*` 関数を参照）。

## MCP サーバー

`./MCP/mcp_config.json` で外部ツールサーバーを設定：

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

# セキュリティ設計

白澤はデフォルトで以下のセキュリティ機構を有効にする：

- **コマンドホワイトリスト**：`ls`、`cat`、`grep`、`git`、`python3` などの一般的なコマンドのみ許可。
- **パス脱出検知**：すべてのファイル操作を現在の作業ディレクトリと `/tmp` 内に制限。
- **危険コマンド遮断**：`rm -rf /`、fork bomb、`curl | sh`、`git push --force` などのパターンを遮断。
- **機密ファイル保護**：`.env`、`.ssh/`、`id_rsa`、`*.pem` などの変更を禁止。
- **スクリプトインジェクション遮断**：`python -c "os.system(...)"` のような回避を検知。
- **プロセスリソース制限**：Linux/macOS では CPU、メモリ、プロセス数を制限。

信頼できるプロジェクトで制限を緩めたい場合は、`Baize.py` の `ALLOWED_COMMANDS` と `FORBIDDEN_PATH_PATTERNS` を変更する。

# プライバシー脱敏

白澤は**双方向かつ可逆**のプライバシー脱敏機構を内蔵しています。LLM に送信する前に機密情報をプレースホルダーに置換し、応答受信後に自動で元に戻します。ユーザーには完全に透過的で、あなたが見る履歴・ツール引数・最終回答は常に原文、LLM が見るものは常に `[[PHONE_1]]`・`[[EMAIL_1]]` のようなプレースホルダーです。

**デフォルトは無効**。必要時に有効化します。

## 有効化する 2 つの方法

### 方法 1：自然言語

```text
>>> 降旨：プライバシー脱敏を有効にして
[system] プライバシー脱敏を有効にしました（標準モード）。

>>> 降旨：厳格な脱敏を有効にして
[system] プライバシー脱敏を有効にしました（厳格モード）。

>>> 降旨：プライバシー保護を無効にして
[system] プライバシー脱敏を無効にしました。
```

### 方法 2：スラッシュコマンド

- `/privacy on` 標準モードを有効化
- `/privacy strict` 厳格モードを有効化（氏名・ナンバープレート・QQ・WeChat を含む）
- `/privacy off` 無効化
- `/privacy status` 現在の状態と統計を表示
- `/privacy rules` 全ルールを表示
- `/privacy test` <テキスト> 脱敏効果をテスト
- `/privacy clear` プレースホルダーマップをクリア

## 2 段階モード

**標準**：中国本土の携帯番号、身分証番号、銀行カード（Luhn 検証）、メール、IPv4/IPv6、OpenAI/Anthropic/GitHub/AWS API Key、Bearer Token、秘密鍵ブロック、パスワードフィールド、URL 資格情報

**厳格**：標準のすべて + 中国語氏名、QQ 番号、WeChat ID、中国本土ナンバープレート

## 動作原理

ユーザー入力（本物の PII を含む）→ messages は原文を保存

↓ sanitize_messages()

LLM が見るのは [[PHONE_1]]、[[EMAIL_1]]

↓ LLM 応答

プレースホルダー → restore_message()

原文に復元 → 保存・表示・ツール実行

**同じ原文は同じプレースホルダーを再利用**するため、1 つの電話番号はセッション全体で `[[PHONE_1]]` のままです。

**ツール引数は機密性で階層化**：`todo`・`ask_user_question`・`task_*` のような純粋テキストツールの引数は脱敏されますが、`run_read`・`run_bash`・`run_webfetch` のようなパス / コマンド / URL を扱うツールの引数は脱敏されません（パスが置換されると実行に失敗するため）。

**サブエージェントも保護対象**：メインエージェントから委任されたタスクも同じ脱敏 / 復元パイプラインを通ります。

## 例

```text
>>> 降旨：/privacy test 私の電話は 13812345678、メールは a@b.com
原文：私の電話は 13812345678、メールは a@b.com
脱敏：私の電話は [[PHONE_1]]、メールは [[EMAIL_1]]
復元：私の電話は 13812345678、メールは a@b.com

>>> 降旨：/privacy status
[プライバシー脱敏]
現在のモード: 標準モード (standard)
有効ルール : 15 / 19
プレースホルダー: 2
脱敏呼び出し: 3
復元呼び出し: 3
```

# データ接続

白澤は **MCP（Model Context Protocol）** を通じて企業向けデータ分析ソフトウェアと接続します。本体プログラムに変更は不要で、`MCP/mcp_config.json` に server を登録するだけです。

## SPSS 接続

### 前提条件

- 本機に IBM SPSS Statistics がインストール済み（バージョン 20–31、Windows 推奨）
- SPSS がライセンス認証済みで正常に起動できる

### 設定手順

1. **SPSS インストールディレクトリを確認：** 通常は `C:\Program Files\IBM\SPSS Statistics\` の後にバージョン番号（例：31）が付きます。

2. **環境変数を設定**（`.env` またはシステム環境変数）：

```text
SPSS_INSTALL_PATH=C:\Program Files\IBM\SPSS Statistics\31
```

3. **状態を確認：**

```bash
spss-studio-mcp status
```

期待される出力：

```text
=== SPSS MCP Capability Status ===
pyreadstat : OK v1.3.6
pandas     : OK v3.0.2
SPSS batch : OK
```

4. **`MCP/mcp_config.json` に登録：**

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

### `SPSS batch: NOT FOUND` の場合

`spss-studio-mcp` が SPSS エンジンを見つけられませんでしたが、`pyreadstat` + `pandas` は正常です。この場合、**ファイルモード**になります：

- `.sav` の読み取り、メタデータ確認、データプレビュー、CSV ↔ SAV 変換が可能
- t 検定、回帰、ANOVA などの統計分析は不可

解決方法：`MCP/mcp_config.json` の `SPSS_INSTALL_PATH` を正しく設定するか、ファイルモードへの降格を受け入れてください。

## SQL 接続

### 対応データベース

PostgreSQL、MySQL、MariaDB、SQL Server、Oracle、達夢、人大金倉、TiDB、OceanBase など（SQLAlchemy 2.0 ドライバー使用）。

### 設定手順

1. **読み取り専用データベースアカウントを準備**（強く推奨）：

```sql
CREATE USER baize_ro WITH PASSWORD 'xxx';
GRANT SELECT ON ALL TABLES IN SCHEMA public TO baize_ro;
```

2. **接続文字列を準備：**

- PostgreSQL --> `postgresql+psycopg://user:pwd@host:5432/db`
- MySQL --> `mysql+pymysql://user:pwd@host:3306/db`
- SQL Server --> `mssql+pyodbc://user:pwd@host:1433/db?driver=ODBC+Driver+18+for+SQL+Server`
- Oracle --> `oracle+oracledb://user:pwd@host:1521/?service_name=ORCL`

3. **`MCP/mcp_config.json` に登録：**

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

### セキュリティガードレール（内蔵）

`atengk-mcp-server-rdbms` は多層防御を提供します：

- **AST レベルの SELECT ガード**：`sqlglot` で構文木を解析し、`DELETE/UPDATE/DROP/TRUNCATE` などの書き込み操作を物理的にブロック。
- **自動 LIMIT 注入**：行数未指定のクエリには強制的に `LIMIT 100` を追加し、全表取得によるメモリ溢れを防止。
- **デフォルト読み取り専用**：書き込み操作は `--allow-dml` / `--allow-ddl` で明示的に許可が必要。
- **SQL インジェクション遮断**：文字列連結で構築された悪意ある文を AST 層で拒否。

### 複数データベースの同時設定

複数のデータベースに同時接続したい場合は、複数の server を登録できます：

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

白澤はそれらのすべてのツールを自動的に `MATERTOOLS` に統合し、LLM がタスクに応じて自動選択します。

# ディレクトリ構成

```text
baize-agent/
├── pyproject.toml              # パッケージ設定
├── requirements-data.txt       # データ接続依存関係（オプション）
├── requirements-data           # データ接続依存関係
├── README.md
├── tests/                      # テスト（パッケージには含まれない）
│   ├── __init__.py
│   ├── test_history.py
│   └── test_skill_loader.py
├── .env.example                # 環境変数例
├── .gitignore
└── agent/                      # メインパッケージ
    ├── __init__.py
    ├── Baize.py                # メインプログラムと Agent Loop
    ├── config.py               # マルチバックエンド設定読み込み
    ├── ui_theme.py             # CLI レンダリングテーマ
    ├── utils.py                # 汎用ユーティリティ
    ├── logo.txt
    ├── skills/                 # 組み込みスキル
    ├── subagent/               # 組み込みサブエージェント
    ├── core/                   # コアロジック（副作用なし、単体テスト可能）
    │   ├── __init__.py
    │   ├── history.py          # セッション履歴クリーニング / token 推定 / 圧縮
    │   └── privacy.py          # プライバシー脱敏：PII 検出 / プレースホルダー置換 / 可逆復元
    ├── hooks/                  # 組み込みフック
    └── MCP/                    # MCP クライアントと設定
        ├── __init__.py
        ├── mcp_client.py
        └── mcp_config.json
```

# 環境変数リファレンス

- 変数：`DEEPSEEK_API_KEY`  説明：DeepSeek API  デフォルト：キー  —
- 変数：`DEEPSEEK_BASE_URL`  説明：DeepSeek エンドポイント  デフォルト：`https://api.deepseek.com`
- 変数：`OPENAI_API_KEY`  説明：OpenAI  デフォルト：互換 API キー  —
- 変数：`OPENAI_BASE_URL`  説明：OpenAI 互換エンドポイント  デフォルト：`https://api.openai.com/v1`
- 変数：`OLLAMA_BASE_URL`  説明：Ollama サービスアドレス  デフォルト：`http://localhost:11434`

変数は `~/.baize/.env` に書けばよく、shell 設定ファイルを変更する必要はない。

- データ分析変数：`SPSS_INSTALL_PATH` 説明：IBM SPSS Statistics インストールディレクトリ デフォルト：—（未設定ならファイルモードに降格）
- データ分析変数：`DATABASE_URL` 説明：SQL MCP のデータベース接続文字列 デフォルト：—（MCP server が読み取る）

これらの変数は `MCP/mcp_config.json` に書きます。

# 開発

## テスト実行

本プロジェクトは pytest を使用。開発前にパッケージと開発依存を編集可能モードでインストール：

```bash
pip install -e ".[dev]"
```

全テスト実行：

```bash
python -m pytest tests/ -v
```

単一ファイルのみ：

```bash
python -m pytest tests/test_history.py -v
```

## コード構成の約束

- `agent/`：パッケージに含まれるメインパッケージ。すべての実行時ロジックとリソース（skills、subagent、hooks、MCP）はここにある。
- `agent/core/`：純粋なロジックモジュール。外部副作用なし。**単独でテスト可能でなければならない**。新しいこの種のロジックはここに置き、テストを添える。
- `tests/`：`agent/` 以下のソースファイルと一対一に対応し、`test_<モジュール名>.py` と命名。
- 外部依存（ネットワーク、ディスク、グローバル状態）を持つ関数は、テストで差し替えられるよう依存を引数で注入すること。

# ❓ よくある質問

- Q：キーはどこに書く？

A：`~/.baize/.env` です。プロジェクトルートの `.env` ではありません。

- Q：バックエンドを変えたら再インストールが必要？

A：不要です。`~/.baize/config.toml` の `active_provider` を変更するだけです。

- Q：ローカル Ollama にキーは必要？

A：不要です。`active_provider = "ollama"` を選び、`env_key` は空にします。

- Q：作業ディレクトリを切り替えるには？

A：会話で「/path/to/project に切り替えて」と言えば、白澤が `set_workspace` ツールを呼び出します。

- Q：コンテキストが長くなりすぎたら？

A：白澤は自動で二段階圧縮します。まず古いツール結果を切り詰め、次に LLM に要約を生成させます。手動で `/compact` も使えます。

- Q：ファイルを誤って削除しない？

A：デフォルトのコマンドホワイトリストが `rm -rf /` などの危険操作を遮断します。ファイル書き込み前には Diff を表示し、確認を求めます。

- Q：白澤を SPSS に接続するには？

A：1. `pip install -r requirements-data.txt` を実行；2. 環境変数 `SPSS_INSTALL_PATH` を SPSS インストールディレクトリに設定；3. `MCP/mcp_config.json` で spss server を有効化。詳細は「データ接続（SPSS / SQL）」章を参照。

- Q：`SPSS batch: NOT FOUND` 怎么办？

A：SPSS エンジンが見つかっていません。`SPSS_INSTALL_PATH` が `stats.exe` を含むディレクトリを正しく指しているか確認してください。`.sav` ファイルだけを扱う場合は、この警告を無視しても構いません（ファイルモードに降格します）。

- Q：SQL データベースに接続するには何を追加でインストール？

A：Python 層では `atengk-mcp-server-rdbms` をインストールします（`pip install` で自動完了）。**SQL Server ユーザーはシステム層に Microsoft ODBC Driver 18 も必要**で、これは pip ではインストールできません。

- Q：白澤がデータベースデータを誤って削除しない？

A：しません。SQL MCP はデフォルトで SELECT のみ許可し、AST 構文木レベルですべての書き込み操作を遮断します。さらに、白澤専用の**読み取り専用データベースアカウント**を作成することを強く推奨します。

- Q：SPSS 分析結果のデータが LLM に漏れない？

A：プライバシー脱敏を有効（`/privacy on`）にすると、ツール戻り値は LLM に送信される前に電話番号・メール・身分証などの PII が自動脱敏されます。**ただし、読み取り専用データベースアカウント + データサンプリング**（必要なフィールドのみ照会）も併用してリスクを下げることを推奨します。

- Q：SPSS/SQL を追加すると、白澤の毎回の会話が遅くなり、token も増えるのはなぜ？

A：MCP server が公開するツール定義が毎ターン LLM に送信されるためです。SPSS には 60+ のツールがあり、約 6000–12000 token の固定オーバーヘッドが増えます。常用ワークフローで SPSS を使わない場合は、その `enabled` を `false` にし、必要時に開けばよいです。

# 🤝 コントリビューション

Issue と PR を歓迎します。まず `Baize.py` の `agent_loop` 関数を読み、Agent メインループを理解してから拡張することを推奨します。

### Thank you for every Contributor to Submit PR

- GitHub Contributor：
[@anupamme](https://github.com/anupamme)
[@wangyipeng0724](https://github.com/wangyipeng0724)

[![Contributors](https://contrib.rocks/image?repo=Xu123-Bob/Baize&v=2)](https://github.com/Xu123-Bob/Baize/graphs/contributors)

# ライセンス

MIT License

# 謝辞

- 本プロジェクトは中国国内の AtomGit でホストされています：https://atomgit.com/Com_Xu/Baize

- AtomGit が本プロジェクトを G-star インキュベーションプロジェクトに採択したことに感謝

- PR 貢献者、Douyin フォロワー、フォローしてくれている学生たちに感謝

- Claude Code、Codex などの優れた AI Coding ツールにインスピレーションを受けた

- DeepSeek、OpenAI SDK、MCP を基に構築

- Vibe Coding の道を共に歩むすべての開発者に感謝

# ☕ サポート

もし白澤があなたに役立つなら、ぜひスポンサーとしてご支援ください。独立開発には多くの時間と労力がかかりますので、ご支援は製品の更新スケジュールを変えるものではありません。ありがとうございます！

<p align="center">
  <img src="image/support.jpg" alt="WeChat QR" width="200" />
</p>

# 連絡先

- 白澤に興味がある方、オープンソース協力に参加したい方、または私の更新を継続的に知りたい方は、以下の方法で連絡できます。
- **現在、私は求人中であります。これまで市場調査やユーザーリサーチの業務に従事しており、Agent についても一定の知識を持っています。私のスキルが貴社のニーズに合致する場合、ぜひご一緒に働きたいと思います（意向ポジション：AI 製品運営／ユーザーリサーチ／マーケティングリサーチ）。**

<p align="center">
  <img src="image/weixin.jpg" alt="WeChat QR コード" width="200" />
</p>

<p align="center">微信で QR コードをスキャンしてください。「Baize オープンソース協力」または「企業採用」と明記してください。</p>

<p align="center">
  <img src="image/抖音.png" alt="Douyin QR コード" width="200" />
</p>

<p align="center">Douyin でスキャンしてフォロー</p>