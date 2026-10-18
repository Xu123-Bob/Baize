<div align="center">

<img src="image/logopage02.png" alt="白澤 Baize ロゴ" width="320" />

# 白澤 Baize

**知るところは尽く語り、秘密は固く守る**

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

中国の神獣をモチーフにした、Vibe Coding とデータ分析のためのセキュリティアシスタント。

**オープンソースの Coding Agent CLI。強力なプライバシー保護と多言語インタラクションを備え、複数バックエンド（DeepSeek / OpenAI 互換 / 智譜 / 通義 / Kimi / ローカル Ollama）をサポートします。ツール呼び出し、スキル読み込み、サブエージェント委任、コンテキスト圧縮、セキュアサンドボックスなどの完全な機能を提供します。**

----------

# コア優位性

## プライバシー保護

- **双方向可逆プライバシー保護**：機密情報は LLM に送信される前にプレースホルダーへ置換され、応答を受け取った後に自動で復元されます。この処理はユーザーに意識させません。ユーザーが見る履歴、ツール引数、最終回答は常に原文であり、LLM が見るのは `«PZ_PHONE_a3f8b2c1d4e5f6a7»` のような**ランダムで推測不可能なプレースホルダー**です。
- **ディスク書き込み時の全面脱敏**：セッションファイル、圧縮トランスクリプト、監査ログは書き込み前に自動で脱敏されます（デフォルト有効）。ディスク上に平文 PII は残りません。
- **インジェクション耐性**：プレースホルダーには 64 ビット暗号学的ランダムトークンを使用し、列挙・偽造・リプレイができません。セッション切り替え後、古いプレースホルダーは即座に無効になります。
- **複数のプライバシー保護有効化方法**：CLI で自然言語入力により有効化できるほか、より正確な `/privacy` コマンドも使用できます。
- **ローカルファーストの agent**：本製品はリモートデータベースを持たず、完全にローカルで動作します。ユーザー情報を収集しません。

# 機能

- **マルチバックエンド対応**：DeepSeek、任意の OpenAI 互換インターフェース（GLM / Qwen / Kimi / OpenAI）、ローカル Ollama。設定一つで切り替え可能。

- **ゼロ設定起動**：初回実行時に設定ファイルを自動生成。ユーザーは一度だけ API キーを入力すればよい。

- **プライバシー脱敏**：LLM に送信する前に **30+ 種類**の機密情報（電話番号、メール、身分証、パスポート、銀行カード、国際番号、API Key、JWT、データベース接続文字列、MAC アドレスなど）を自動識別して脱敏し、応答後に自動復元します。**ディスク書き込み時にも同様に脱敏**し、ディスクに平文を残しません。標準 / 厳格の 2 モードをサポートし、自然言語または `/privacy` コマンドで切り替えられます。

- **多言語インタラクション**：中国語 / 英語 / 日本語 / 韓国語 / スペイン語 / フランス語 / ドイツ語 / ロシア語 / アラビア語の 9 言語を自由に切り替え可能。`English` と言うか `/lang ja` を使えば、AI はセッション全体で対応言語で思考し応答します。

- **完全なツールチェーン**：bash 実行、ファイル読み書き編集、glob/grep 検索、Web 検索・取得、バックグラウンドタスク、タスク・ToDo 管理。

- **スキルシステム（Skills）**：必要に応じてドメイン知識（`SKILL.md`）を読み込み、特定シーンで AI をより専門的にします。

- **サブエージェント（Subagents）**：複雑なタスクを独立コンテキストのサブエージェントに委任し、メインセッションの汚染を防ぎます。

- **フック（Hooks）**：Python または Shell フック。ツール呼び出し前後のインターセプト、監査ログ、自動フォーマット、テストゲートをサポート。

- **MCP プロトコル**：Model Context Protocol を通じて外部ツールサーバー（GitHub、Filesystem など）に接続。

- **コンテキスト圧縮**：2 段階圧縮（ツール結果の切り詰め + LLM 要約）により、超長い会話をサポート。

- **セキュアサンドボックス**：コマンド許可リスト、パス脱出検出、危険コマンド遮断、機密ファイル保護、スクリプトインジェクション遮断。

- **黒金テーマ CLI**：中国語幅の自動調整、コードハイライト、Diff 着色、思考の折りたたみ。

# 白澤 CLI 画面

<div align="center">
白澤 CLI 起動画面
</div>

<p align="center">
  <img src="image/clipage01.jpg" alt="白澤 CLI 起動画面" width="800" />
</p>

<div align="center">
白澤 CLI 実行画面 -- 01
</div>

<p align="center">
  <img src="image/clipage02.jpg" alt="白澤 CLI 実行画面" width="800" />
</p>

<div align="center">
白澤 CLI 実行画面 -- 02
</div>

<p align="center">
  <img src="image/clipage03.jpg" alt="白澤 CLI 実行画面" width="800" />
</p>

# インストール

## 前提条件

- Python 3.10+（`tomllib` が必要。3.11+ では標準搭載、3.10 では `tomli` をインストール）
- pip

## ソースからインストール

### ダウンロード方法は 2 つ

1. `pip install https://github.com/Xu123-Bob/Baize.git`

    bash -- Win+R を押して `cmd` を入力し、次を実行：

    baize

2. リポジトリページで `<> Code` --> `Download ZIP` をクリック。

(1) 解凍後、ディレクトリに移動：

    bash -- Win+R を押して cmd を入力

    cd 解凍後のディレクトリ

    pip install -r requirements.txt

    python -m Baize

インストール後、Win+R を押して `cmd` を入力し、CLI を開いて `baize` と入力すれば実行できます。

(2) ZIP をダウンロードしてローカルインストールする場合、解凍後にディレクトリへ移動して実行：

    bash -- Win+R を押して cmd を入力

    pip install .

インストール後、Win+R を押して `cmd` を入力し、CLI を開いて `baize` と入力すれば実行できます。

### オプション：データ接続依存関係をインストール（データ分析に重要）

白澤に SPSS や SQL データベースを操作させたい場合は、追加依存関係をインストールします：

```bash
pip install -r requirements-data.txt
```

`requirements-data.txt` には以下が含まれます：

- `spss-studio-mcp`：SPSS 統計分析 MCP server（ローカルに IBM SPSS Statistics がインストール済みである必要あり）
- `atengk-mcp-server-rdbms`：汎用リレーショナルデータベース MCP server（PostgreSQL / MySQL / SQL Server / Oracle / 達夢など）
- `pyodbc`：SQL Server に必要な ODBC Python バインディング

または、プロジェクトを `pyproject.toml` でインストールしている場合、extras も使用できます：

```bash
pip install -e ".[data]"          # データ接続依存関係をすべてインストール
pip install -e ".[spss]"          # SPSS のみ
pip install -e ".[sql]"           # 汎用 SQL のみ
pip install -e ".[sql-mssql]"     # SQL Server 専用（pyodbc を含む）
```

- **⚠️ SQL Server ユーザー注意：`pyodbc` は Python バインディングのみです。システム側に Microsoft ODBC Driver 18 for SQL Server もインストールする必要があります。**
- **⚠️ SPSS ユーザー注意：`spss-studio-mcp` は MCP ブリッジ層のみです。ローカルに IBM SPSS Statistics（バージョン 20–31）がインストールされ、ライセンス認証済みである必要があり、環境変数 `SPSS_INSTALL_PATH` を SPSS インストールディレクトリに設定する必要があります。SPSS エンジンによる完全な分析機能は主に Windows でサポートされます。Linux/macOS では「ファイルモード」に降格できます（`.sav` ファイルの読み取り、メタデータ確認、データプレビューは可能ですが、統計分析はできません）。**

# クイックスタート

## LLM API に接続して実行

1. 初回実行

```bash
baize
```

初回実行時、白澤は 2 つの設定ファイルを自動生成します：

```
~/.baize/config.toml   # バックエンド設定（DeepSeek / OpenAI / Ollama を選択）

~/.baize/.env          # キーファイル
```

Windows のパスは `C:\Users\ユーザー名\.baize\` です。

**2. バックエンドを選択**

`~/.baize/config.toml` を開き、**active_provider** を変更します（必ず変更）：

```toml
# 白澤設定ファイル
# active_provider を変更してバックエンドを切り替え
# 選択可能値："deepseek" / "qwen" / "kimi" / "glm" / "openai" / "ollama"

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

**3. キーを入力**

`~/.baize/.env` を編集します。**使用する LLM がある場合、その行の先頭の `#` を削除し、他の LLM の先頭に `#` を追加して他の LLM API 出力をロックします。API Key を入力したら必ず保存してください。保存後にのみ有効になります**：

```env
# ============================================================
# 白澤キーファイル
# ============================================================
# 使用するバックエンドのキーだけを入力し、他はコメントのままにします。
# 変数名は config.toml の env_key フィールドと一致させる必要があります。
#
# 場所：
#   Linux / macOS: ~/.baize/.env
#   Windows:       C:\Users\ユーザー名\.baize\.env
# ============================================================

# ---------- DeepSeek（デフォルトバックエンド） ----------
# 取得先：https://platform.deepseek.com/api_keys
DEEPSEEK_API_KEY=

# ---------- OpenAI または任意の OpenAI 互換インターフェース（オプション） ----------
# Groq、通義、Moonshot、智譜、OpenAI などに適用
# 注意：base_url は config.toml の [model_providers.xxx] で設定し、ここでは設定しません
# OPENAI_API_KEY=

# ---------- 通義千問（オプション） ----------
# 取得先：https://dashscope.console.aliyun.com/
# DASHSCOPE_API_KEY=

# ---------- Kimi / Moonshot（オプション） ----------
# 取得先：https://platform.moonshot.cn/console/api-keys
# MOONSHOT_API_KEY=

# ---------- 智譜 GLM（オプション） ----------
# 取得先：https://open.bigmodel.cn/usercenter/apikeys
# ZHIPUAI_API_KEY=

# ---------- カスタムゲートウェイ（オプション） ----------
# CUSTOM_API_KEY=

# ---------- Ollama（ローカルモデル、キー不要） ----------
# Ollama が localhost:11434 で動作していれば、ここでの設定は不要です
```

4. 再起動

```bash
baize
```

黒金のロゴとウェルカムメッセージが表示されれば起動成功です。

## Ollama ローカルモデル（ゼロコスト）

クラウド API を使いたくない場合は、ローカル Ollama を使用します：

    bash

    # 1. Ollama をインストール：https://ollama.com/download
    # 2. モデルを取得
    ollama pull qwen2.5:7b

    # 3. Ollama サービスを起動
    ollama serve

    # 4. ~/.baize/config.toml を変更
    active_provider = "ollama"

    # 5. 白澤を起動
    baize

推奨モデル：`qwen2.5:7b`（中国語に強い）、`llama3.1:8b`、`deepseek-r1:7b`。

# 使用例

起動後、`>>> 降旨：` プロンプトで自然言語により要件を記述します：

```
>>> 降旨：Python で Douban Top250 をスクレイピングするスクリプトを書き、CSV として保存してください

>>> 降旨：src/ 以下のすべての Python ファイルの型エラーを確認してください

>>> 降旨：このリポジトリ内で requests を使っている箇所をすべて探し、httpx に変更してください
```

## 多言語インタラクション

白澤は **9 言語**をサポートします：中国語、English、日本語、한국어、Español、Français、deutsch、русский、العربية。

切り替え方法は 2 つあります：

### 方法 1：直接話す（自動検出）

白澤は入力言語を自動認識して切り替えます：

```
>>> 降旨：Hello, help me write a Python script
[システム] 入力言語を English と検出しました。白澤は English インタラクションに切り替えました。
（白澤は英語で応答）

>>> 降旨：日本語で答えてください
[システム] 入力言語を 日本語 と検出しました。白澤は 日本語 インタラクションに切り替えました。
（白澤は日本語で応答）
```

### 方法 2：手動コマンド

```
>>> 降旨：/lang                # 現在の言語と利用可能リストを表示
[システム] 現在の言語：中文 (zh)
[システム] 利用可能な言語：
    zh    中文 ←
    en    English
    ja    日本語
    ko    한국어
    es    Español
    fr    Français

>>> 降旨：/lang English        # 言語名で切り替え
>>> 降旨：/lang ja             # 言語コードで切り替え
>>> 降旨：/lang 西班牙语        # 中国語名でも可能
```

**言語名 / 言語コード / 中国語名 / 原語名**の 4 種類をサポートします。たとえば英語に切り替える場合、`English`、`en`、`英语`、`英文` のいずれでも可能です。

## 内蔵コマンド

- `/exit`、`/quit` --> 白澤を終了
- `/clear` --> 会話履歴、ToDo、思考記録、ツール記録をクリア
- `/compact` --> 手動でコンテキストを圧縮（会話が長すぎる場合に使用）
- `/commit` --> 現在のセッションを保存し Git にコミット（Git リポジトリ内の場合）
- `/lang` --> 現在の言語を表示；`/lang en` で英語に切り替え（言語コードまたは言語名をサポート）
- `/skills` --> 利用可能なすべてのスキルを一覧表示
- `/skills reload` --> ユーザースキルディレクトリを再読み込み
- `/unload` --> 現在アクティブなスキルをアンロード
- `/show thought` --> 完全な思考記録を表示
- `/show tool` --> ツール呼び出し記録を表示
- `/show all` --> すべてのセッション履歴を表示
- `/スキル名` --> 指定スキルを読み込み（曖昧一致をサポート）
- `/privacy` --> プライバシー脱敏制御（`on / off / strict / status / rules / test / clear`）
- `/privacy rule-off <name>` --> 特定の脱敏ルールを無効化（例：`/privacy rule-off phone_intl`）
- `/privacy rule-on <name>` --> ルールを再度有効化

## データ接続使用例

SPSS / SQL を設定した後、自然言語で直接操作できます：

```text
>>> 降旨：SPSS で data.sav を開き、変数リストとサンプルサイズを教えてください

>>> 降旨：data.sav に対して記述統計を実行し、その後線形回帰を実行してください

>>> 降旨：sales テーブルで先月の売上が 10 万を超える注文を検索し、顧客ごとにグループ化してください

>>> 降旨：SPSS の分析結果を CSV にエクスポートし、SQL で顧客マスタデータと結合してください
```

# 拡張機構

白澤は 4 種類の拡張方法をサポートします。現在の作業ディレクトリに配置すれば有効になります。

## スキル（Skills）

`./skills/スキル名/SKILL.md` にドメイン知識を記述します。AI は複雑なタスクに遭遇したとき自発的に読み込みます。

    markdown

    ---
    name: pandas-eda

    description: pandas による探索的データ分析のベストプラクティス

    tags: data,python
    ---

    # Pandas EDA ガイド

    ## コア手順
    1. df.info() でフィールド型と欠損を確認
    2. df.describe() で統計記述
    ...

会話中に `/pandas-eda` で手動読み込みすることもできます。

## サブエージェント（Subagents）

`./subagent/ロール名/AGENT.md` に専用サブエージェントを定義します。メインエージェントは `agent` ツールでタスクを委任できます。

    markdown

    ---
    name: code-reviewer

    description: 厳格なコードレビュアー
    ---

    あなたはシニアコードレビュアーです。レビュー時は以下を優先してください：
    1. 境界条件と例外処理
    2. リソースリーク
    3. 並行安全性
    ...

## フック（Hooks）

`./hooks/` の下に `PreToolUse-*.sh`、`PostToolUse-*.sh`、`Stop-*.sh` を配置します。JSON 入力を受け取り、判断を返します：

```bash
#!/bin/bash
# PreToolUse-guard.sh
read -r input
if echo "$input" | grep -q "rm -rf"; then
  echo '{"hookSpecificOutput":{"permissionDecision":"block","permissionDecisionReason":"Deletion prohibited"}}'
fi
```

Python フックは内蔵 API を直接呼び出せます（`Baize.py` の `hook_*` 関数を参照）。

## MCP サーバー

`./MCP/mcp_config.json` で外部ツールサーバーを設定します：

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

# セキュリティ設計（コア）

白澤はデフォルトで以下のセキュリティ機構を有効にします：

- **コマンド許可リスト**：`ls`、`cat`、`grep`、`git`、`python3` などの一般的なコマンドのみ許可。
- **パス脱出検出**：すべてのファイル操作を現在の作業ディレクトリと `/tmp` 内に制限。
- **危険コマンド遮断**：`rm -rf /`、fork bomb、`curl | sh`、`git push --force` などのパターンを遮断。
- **機密ファイル保護**：`.env`、`.ssh/`、`id_rsa`、`*.pem` などの変更を禁止。
- **スクリプトインジェクション遮断**：`python -c "os.system(...)"` のようなバイパスを検出。
- **プロセスリソース制限**：Linux/macOS で CPU、メモリ、プロセス数を制限。
- **プライバシー脱敏（双方向可逆）**：送信時に PII をランダムプレースホルダーへ置換し、受信時に復元。ディスク書き込み時は独立して脱敏。
- **プレースホルダーインジェクション耐性**：64 ビット暗号学的ランダムトークン + 入力側中和 + セッション分離。
- **監査ログ脱敏**：`hook_audit_log` は書き込み前に脱敏し、切り詰め、失敗時は書き込みを拒否。

信頼済みプロジェクトで制限を緩和する必要がある場合、`Baize.py` の `ALLOWED_COMMANDS` と `FORBIDDEN_PATH_PATTERNS` を変更できます。

# プライバシー脱敏（コア）

白澤には **双方向可逆 + ディスク脱敏** のプライバシー保護機構が内蔵され、入力からディスクまでの全経路をカバーします：

- **送信時**：LLM に送信する前に PII を推測不可能なプレースホルダーへ置換。
- **受信時**：LLM 応答内のプレースホルダーを原文へ復元。
- **ディスク書き込み時**：セッションファイル、圧縮トランスクリプト、監査ログを書き込み前に**独立して脱敏**。ディスクに平文を残さない。

**デフォルトでは無効**です。必要時に有効化します。

## 有効化方法は 2 つ

### 方法 1：自然言語

会話中で直接言います：

```
>>> 降旨：プライバシー脱敏を有効化
[システム] プライバシー脱敏を有効化しました（標準モード）。

>>> 降旨：厳格脱敏を有効化
[システム] プライバシー脱敏を有効化しました（厳格モード）。

>>> 降旨：プライバシー保護を無効化
[システム] プライバシー脱敏を無効化しました。
```

### 方法 2：スラッシュコマンド

- `/privacy on` 標準モードを有効化
- `/privacy strict` 厳格モードを有効化
- `/privacy off` 無効化
- `/privacy status` 状態、セッション ID、ルール数、LRU/TTL 統計を表示
- `/privacy rules` すべてのルール（有効状態を含む）を一覧表示
- `/privacy rule-off <name>` 特定ルールを無効化
- `/privacy rule-on <name>` ルールを再度有効化
- `/privacy test <テキスト>` 脱敏効果をテスト
- `/privacy clear` プレースホルダーマッピングをクリアし、**セッション ID をローテーション**

## 2 つのモード

**標準**：中国大陸の携帯番号、身分証番号、銀行カード番号（Luhn チェック）、メール、IPv4/IPv6、OpenAI/Anthropic/GitHub/AWS API Key、Bearer Token、秘密鍵ブロック、パスワードフィールド、URL 認証情報。

**厳格**：標準モードのすべて + 中国語氏名、QQ 番号、WeChat ID、中国大陸のナンバープレート番号。

## 仕組み

ユーザー入力（実際の PII を含む）→ messages は原文を保存

↓ `sanitize_messages()`

LLM に送信されるのは `[[PHONE_1]]`、`[[EMAIL_1]]`

↓ LLM 応答

返されたプレースホルダー → `restore_message()`

原文へ復元 → ディスク書き込み / 表示 / ツール実行

- **プライバシー脱敏（双方向可逆）**：送信時に PII をランダムプレースホルダーへ置換し、受信時に復元。ディスク書き込み時は独立して脱敏。
- **プレースホルダーインジェクション耐性**：64 ビット暗号学的ランダムトークン + 入力側中和 + セッション分離。
- **監査ログ脱敏**：`hook_audit_log` は書き込み前に脱敏し、切り詰め、失敗時は書き込みを拒否。

## ツール引数のインテリジェント分级

**脱敏される**（純テキスト引数で、実際の実行には参加しない）：

- `todo`、`ask_user_question`、`task_create`、`task_update`

**脱敏されない**（パス/コマンド/URL が実際に使用される）：

- `run_read` / `run_write` / `run_edit` / `run_glob` / `run_grep`（パスは IO に使用）
- `run_bash` / `background_run`（コマンドは実行される）
- `run_webfetch` / `web_search`（URL は実際にネットワークへ送信される）
- `set_workspace`（パスは `chdir` に使用）
- `load_skills`（スキル名は列挙）
- `agent`（サブエージェントコンテキストは独立して脱敏）
- `mcp_*`（意味が未知のため保守的に処理）

**ディスク書き込み時はすべて脱敏**（ディスク内容は再実行されないため、安全性を優先）。

## ディスク脱敏

**デフォルト有効**で、メモリ内脱敏とは独立しています。`/privacy off`（メモリ内脱敏なし）でも、ディスク書き込み時は少なくとも標準ルールを通します。

**主な特徴**：

- ディスク脱敏は**独立した一回限りのマッピングテーブル**を使用します。ディスクに書き込まれたプレースホルダーは**復元できません**。マッピングテーブルは破棄されるためです。
- ディスク脱敏が**失敗した場合、平文の書き込みを拒否**します（降格なし、サイレントスキップなし）。
- 旧バージョンのセッションファイルに平文が含まれる場合、初回保存時に自動で脱敏して書き換えます。

**無効化方法**（非推奨）：`Baize.py` の `PERSIST_REDACT_ENABLED = False` を変更します。

## 例

```
>>> 降旨：/privacy test 私の電話番号は 13812345678、メールは a@b.com
原文：私の電話番号は 13812345678、メールは a@b.com
脱敏：私の電話番号は [[PHONE_1]]、メールは [[EMAIL_1]]
復元：私の電話番号は 13812345678、メールは a@b.com

>>> 降旨：/privacy status
[プライバシー脱敏]
現在のモード : 標準モード (standard)
セッション ID : 7d2f5e91
有効ルール数 : 34 / 41
アクティブプレースホルダー : 2
マッピング容量 : 2 / 2000
TTL : 86400 秒
LRU 淘汰 : 0
TTL 淘汰 : 0
脱敏呼び出し回数: 3
復元呼び出し回数: 3

>>> 降旨：/privacy rules
[プライバシー脱敏ルール一覧] 全 41 件
【標準+厳格】
[✓] phone_cn 中国大陸携帯番号 (standard,strict)
[✓] id_card_cn 中国大陸身分証番号 (standard,strict)
[✓] jwt JWT Token (standard,strict)
...
【厳格のみ】
[✓] name_cn 中国語氏名 (strict)
[✓] address_cn 中国語詳細住所 (strict)
...
使い方：
/privacy rule-off <name> ルールを無効化
/privacy rule-on <name> ルールを再度有効化
```

### テスト画面

<div align="center">
プライバシー保護テスト画面 -- 01
</div>

<p align="center">
  <img src="image/privary01.jpg" alt="プライバシー保護テスト画面" width="800" />
</p>

<div align="center">
プライバシー保護テスト画面 -- 02
</div>

<p align="center">
  <img src="image/privary02.jpg" alt="プライバシー保護テスト画面" width="800" />
</p>

# データ接続（コア）

白澤は **MCP（Model Context Protocol）** を通じて企業データ分析ソフトウェアと接続します。メインプログラムの変更は不要で、`MCP/mcp_config.json` に server を登録するだけです。

## SPSS 接続

### 前提条件

- ローカルに IBM SPSS Statistics がインストール済み（バージョン 20–31、Windows 推奨）
- SPSS がライセンス認証済みで正常起動できること

### 設定手順

1. **SPSS インストールディレクトリを確認**：デフォルトパスは通常 `C:\Program Files\IBM\SPSS Statistics\` の後にバージョン番号（例：`31`）が付きます。

2. **環境変数を設定**（`.env` またはシステム環境変数）：

```text
SPSS_INSTALL_PATH=C:\Program Files\IBM\SPSS Statistics\31
```

3. **状態を確認**：

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

4. **`MCP/mcp_config.json` に登録**：

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

`spss-studio-mcp` が SPSS エンジンを見つけられなかったが、`pyreadstat` + `pandas` は正常という意味です。この場合 **ファイルモード** になります：

- `.sav` の読み取り、メタデータ確認、データプレビュー、CSV ↔ SAV 変換が可能
- 統計分析（t 検定、回帰、ANOVA など）は実行不可

解決方法：`MCP/mcp_config.json` の `SPSS_INSTALL_PATH` を正しく設定するか、ファイルモードへの降格を受け入れます。

## SQL 接続

### 対応データベース

PostgreSQL、MySQL、MariaDB、SQL Server、Oracle、達夢、人大金倉、TiDB、OceanBase など（SQLAlchemy 2.0 ドライバーベース）。

### 設定手順

1. **読み取り専用データベースアカウントを準備**（強く推奨）：

```sql
CREATE USER baize_ro WITH PASSWORD 'xxx';
GRANT SELECT ON ALL TABLES IN SCHEMA public TO baize_ro;
```

2. **接続文字列を準備**：

- PostgreSQL --> `postgresql+psycopg://user:pwd@host:5432/db`
- MySQL --> `mysql+pymysql://user:pwd@host:3306/db`
- SQL Server --> `mssql+pyodbc://user:pwd@host:1433/db?driver=ODBC+Driver+18+for+SQL+Server`
- Oracle --> `oracle+oracledb://user:pwd@host:1521/?service_name=ORCL`

3. **`MCP/mcp_config.json` に登録**：

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

### 内蔵セキュリティガードレール

`atengk-mcp-server-rdbms` は多層保護を提供します：

- **AST レベル SELECT ガード**：`sqlglot` で構文木を解析し、`DELETE/UPDATE/DROP/TRUNCATE` などの書き込み操作を物理的に遮断。
- **自動 LIMIT 注入**：行数未指定のクエリには強制的に `LIMIT 100` を追加し、全表取得によるメモリ枯渇を防止。
- **デフォルト読み取り専用**：書き込み操作は `--allow-dml` / `--allow-ddl` で明示的に許可する必要あり。
- **SQL インジェクション遮断**：AST 層で文字列連結により構築された悪意ある文を拒否。

### 複数データベースを一度に設定

複数のデータベースに同時接続したい場合、複数の server を登録できます：

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

白澤はそれらのすべてのツールを `MATERTOOLS` に自動統合し、LLM がタスクに応じて自動選択します。

# ディレクトリ構造

```
    baize-agent/
    ├── pyproject.toml              # パッケージ設定
    ├── requirements-data.txt       # データ接続依存関係（オプション）
    ├── requirements-data           # 接続依存関係
    ├── README.md
    ├── tests/                      # テスト（パッケージには含まれない）
    |   ├── __init__.py
    |   ├── test_history.py
    |   └── test_skill_loader.py
    ├── .env.example                # 環境変数例
    ├── .gitignore
    └── agent/                      # メインパッケージ
        ├── logo_*                  # ログイン画面ロゴ
        ├── LOGO和启动交互界面       # ログイン画面ロゴ画像
        ├── __init__.py             # バージョン
        ├── Baize.py                # メインプログラムと Agent Loop
        ├── config.py               # マルチバックエンド設定読み込み
        ├── ui_theme.py             # CLI レンダリングテーマ
        ├── utils.py                # 汎用ユーティリティ
        ├── logo.txt
        ├── skills/                 # 内蔵スキル
        ├── subagent/               # 内蔵サブエージェント
        ├── core/                   # コアロジック（副作用なし、単体テスト可能）
        |   ├── __init__.py
        |   ├── history.py          # セッション履歴クリーニング / token 見積り / 圧縮
        |   └── privacy.py          # プライバシー脱敏：PII 識別 / プレースホルダー置換 / 可逆復元
        ├── hooks/                  # 内蔵フック
        └── MCP/                    # MCP クライアントと設定
            ├── __init__.py
            ├── mcp_client.py       # MCP クライアント
            └── mcp_config.json     # MCP 設定
```

# 環境変数リファレンス

- 変数：`DEEPSEEK_API_KEY` — 説明：DeepSeek API キー — デフォルト：—（秘密）
- 変数：`DEEPSEEK_BASE_URL` — 説明：DeepSeek エンドポイント URL — デフォルト：`https://api.deepseek.com`
- 変数：`OPENAI_API_KEY` — 説明：OpenAI 互換 API キー — デフォルト：—（秘密）
- 変数：`OPENAI_BASE_URL` — 説明：OpenAI 互換エンドポイント URL — デフォルト：`https://api.openai.com/v1`
- 変数：`OLLAMA_BASE_URL` — 説明：Ollama サービス URL — デフォルト：`http://localhost:11434`

**上記変数は `~/.baize/.env` に書き込めばよく、shell 設定ファイルの変更は不要です。**

- データ分析変数：`SPSS_INSTALL_PATH` — 説明：IBM SPSS Statistics インストールディレクトリ — デフォルト：—（未設定の場合はファイルモードへ降格）
- データ分析変数：`DATABASE_URL` — 説明：SQL MCP のデータベース接続文字列 — デフォルト：—（MCP server が読み取る）

**上記変数は `MCP/mcp_config.json` に書き込みます。**

# 開発

## テスト実行

本プロジェクトは pytest を使用します。開発前にパッケージと開発依存関係を編集可能モードでインストールしてください：

    pip install -e ".[dev]"

すべてのテストを実行：

    python -m pytest tests/ -v

単一ファイルのみ：

    python -m pytest tests/test_history.py -v

## コード構造規約

- `agent/`：パッケージとして配布されるメインパッケージ。すべての実行時ロジックとリソース（skills、subagent、hooks、MCP）はここにあります。
- `agent/core/`：外部副作用のない純粋ロジックモジュール。**単独でテスト可能でなければなりません。** 新しいこの種のロジックはここに置き、テストを添付してください。
- `tests/`：`agent/` 下のソースファイルと 1 対 1 対応し、`test_<モジュール名>.py` と命名します。
- 外部依存（ネットワーク、ディスク、グローバル状態）を持つ関数は、テストで置換できるよう引数を通じて依存性を注入してください。

# ❓ FAQ

- Q：API キーはどこに記入しますか？

A：`~/.baize/.env` です。プロジェクトルートの `.env` ではありません。

- Q：バックエンドを変更したら再インストールが必要ですか？

A：不要です。`~/.baize/config.toml` の `active_provider` を変更するだけです。

- Q：ローカル Ollama にキーは必要ですか？

A：不要です。`active_provider = "ollama"` を選択し、`env_key` を空にしてください。

- Q：作業ディレクトリを切り替えるには？

A：会話中で「/path/to/project に切り替えて」と言うと、白澤が `set_workspace` ツールを呼び出します。

- Q：コンテキストが長すぎるとどうなりますか？

A：白澤は自動で 2 段階圧縮します。まず古いツール結果を切り詰め、次に LLM に要約を依頼します。手動で `/compact` も使用できます。

- Q：誤ってファイルを削除しませんか？

A：デフォルトのコマンド許可リストが `rm -rf /` などの危険操作を遮断します。ファイル書き込み前には Diff を表示し確認を求めます。

- Q：白澤を SPSS に接続するには？

A：1. `pip install -r requirements-data.txt` をインストール；2. 環境変数 `SPSS_INSTALL_PATH` を SPSS インストールディレクトリに設定；3. `MCP/mcp_config.json` で spss server を有効化。詳細は「データ接続（SPSS / SQL）」章を参照。

- Q：`SPSS batch: NOT FOUND` の場合は？

A：SPSS エンジンが見つからないことを意味します。`SPSS_INSTALL_PATH` が `stats.exe` を含むディレクトリを正しく指しているか確認してください。`.sav` ファイルのみを扱う場合はこの警告を無視できます（ファイルモードへ降格）。

- Q：SQL データベースに接続するには何を追加インストールしますか？

A：Python 層では `atengk-mcp-server-rdbms` をインストールします（`pip install` で自動完了）。**SQL Server ユーザーはシステム層に Microsoft ODBC Driver 18 もインストールする必要があり**、これは pip ではインストールできません。

- Q：白澤がデータベースデータを誤って削除しませんか？

A：しません。SQL MCP はデフォルトで SELECT のみ許可し、AST 構文木レベルですべての書き込み操作を遮断します。さらに、白澤専用の**読み取り専用データベースアカウント**を作成することを強く推奨します。

- Q：SPSS 分析結果のデータが LLM に漏れませんか？

A：プライバシー脱敏が有効（`/privacy on`）の場合、ツール返却結果は LLM に送信される前に電話番号、メール、身分証などの PII が自動脱敏されます。**ただし、読み取り専用データベースアカウント + データサンプリング**（必要なフィールドのみクエリ）も併用してリスクを下げることを推奨します。

- Q：SPSS/SQL を追加すると、白澤の毎回の会話が遅くなり token も増えるのはなぜですか？

A：MCP server が公開するツール定義が毎ターン LLM に送信されるためです。SPSS には 60+ のツールがあり、約 6,000–12,000 token の固定オーバーヘッドが増えます。よく使うワークフローに SPSS が含まれない場合、その `enabled` を `false` にし、必要時に有効化できます。

# 🤝 貢献

Issue と PR を歓迎します。PR を提出する前に `CONTRIBUTOR.md` を読むことをおすすめします。

**PR を提出してくださるすべての Contributor に感謝します。**

- GitHub Contributor：
[@anupamme](https://github.com/anupamme)
[@wangyipeng0724](https://github.com/wangyipeng0724)

[![Contributors](https://contrib.rocks/image?repo=Xu123-Bob/Baize&v=2)](https://github.com/Xu123-Bob/Baize/graphs/contributors)

# ライセンス

MIT License

# 謝辞

- 本プロジェクトは中国の AtomGit でホストされています：https://atomgit.com/Com_Xu/Baize
- AtomGit が本プロジェクトを G-star 孵化プロジェクトに採用してくださったことに感謝します。
- PR 貢献者、Douyin フォロワー、私をフォローしてくれる学生の皆さんに感謝します。
- Claude Code、Codex などの優れた AI Coding ツールからインスピレーションを得ています。
- DeepSeek、OpenAI SDK、MCP を基盤に構築されています。
- Vibe Coding の道を共に歩むすべての開発者に感謝します。

# ☕ スポンサー

白澤が役に立つ場合、スポンサー・投げ銭を歓迎します。個人開発には多くの時間がかかります。スポンサーは製品アップデートのスケジュールを変更しません。ご支援ありがとうございます！

<p align="center">
  <img src="image/support.jpg" alt="WeChat QR コード" width="200" />
</p>

# 連絡先

- 白澤に興味がある、またはオープンソース協力に参加したい場合は、以下の方法で連絡できます。
- **現在、求職中です。市場調査とユーザーリサーチの経験があり、Agent についてもある程度理解しています。私の能力が貴社のニーズに合う場合、一緒に働けることを願っています（希望職種：AI プロダクト運営 / ユーザーリサーチ / マーケットリサーチ）。**

<p align="center">
  <img src="image/weixin.jpg" alt="WeChat QR コード" width="200" />
</p>

<p align="center">WeChat QR コードをスキャンし、「Baize オープンソース協力」または「企業採用」と明記してください。</p>

<p align="center">
  <img src="image/抖音.png" alt="Douyin QR コード" width="200" />
</p>

<p align="center">Douyin QR コードをスキャンしてフォローしてください。</p>