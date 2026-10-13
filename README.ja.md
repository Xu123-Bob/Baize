<div align="center">

<img src="image/logopage02.png" alt="Baize 白澤 Logo" width="320" />

# Baize 白澤

**知ることはすべて語り、秘密は固く守る**

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

中国の神獣をモチーフにした、VibeCodingとデータ分析のための安全アシスタント。

**オープンソースのCoding Agent CLI。強力なプライバシー保護と多言語インタラクションを備え、複数バックエンド（DeepSeek / OpenAI互換 / 智譜 / 通義 / Kimi / Ollamaローカル）をサポート。ツール呼び出し、スキル読み込み、サブエージェント委譲、コンテキスト圧縮、セキュアサンドボックスなど、完全な機能を提供します。**

----------

# コア優位性

## プライバシー保護

- **双方向可逆プライバシー保護**：機密情報はLLMに送信される前にプレースホルダーに置き換えられ、応答を受け取った後に自動的に復元されます。このプロセスはユーザーに意識させません——あなたが見る履歴、ツールパラメータ、最終回答は常に原文であり、LLMが見るのは `«PZ_PHONE_a3f8b2c1d4e5f6a7»` のような**ランダムで推測不可能なプレースホルダー**だけです。
- **ディスク保存時の完全マスキング**：セッションファイル、圧縮トランスクリプト、監査ログは書き込み前に自動的にマスキングされます（デフォルトで有効）。ディスク上に平文PIIが残ることはありません。
- **インジェクション耐性**：プレースホルダーは64ビットの暗号学的ランダムトークンを使用し、列挙・偽造・リプレイが不可能です。セッション切り替え後、古いプレースホルダーは即座に無効になります。
- **プライバシー保護を有効にする複数の方法**：コマンドラインで自然言語を入力するか、より正確な `/privacy` コマンドを使用してプライバシー保護モードを有効にできます。
- **エージェントのローカル化**：本製品はリモートデータベースを持たず、完全にローカルで動作します。ユーザー情報を収集しません。

## 多言語インタラクション

- **9言語のインタラクションをサポート**：中国語、English、日本語、한국어、Español、Français、deutsch、русский、العربية。
- **言語切り替えの複数の方法**：`please speak with english` と直接入力して英語に切り替えるか、`/lang ja` と入力して日本語に切り替えられます。

# 特徴

- **マルチバックエンド対応**：DeepSeek、任意のOpenAI互換インターフェース（GLM / Qwen / Kimi / OpenAI）、ローカルOllama。ワンクリックで切り替え。

- **ゼロ設定起動**：初回実行時に設定ファイルを自動生成。ユーザーは一度だけキーを入力すればよい。

- **プライバシーマスキング**：LLMに送信する前に**30種類以上**の機密情報（電話番号、メール、身分証、パスポート、銀行カード、国際番号、APIキー、JWT、データベース接続文字列、MACアドレスなど）を自動識別してマスキングし、応答を受け取った後に自動復元。**ディスク保存時も同様にマスキング**され、ディスクに平文を残しません。標準/厳格の2段階モードをサポートし、自然言語または `/privacy` コマンドで切り替え可能。

- **多言語インタラクション**：中/英/日/韓/西/仏/独/露/アラビア語の9言語を自由に切り替え。`English` と言うか `/lang ja` と入力するだけで、AIは対応言語で思考し応答します。

- **完全なツールチェーン**：bash実行、ファイル読み書き編集、glob/grep検索、ウェブ検索・取得、バックグラウンドタスク、タスクとToDo管理。

- **スキルシステム（Skills）**：必要に応じて領域知識（SKILL.md）を読み込み、特定のシナリオでAIをより専門的にします。

- **サブエージェント（Subagents）**：複雑なタスクを独立したコンテキストのサブエージェントに委譲し、メインセッションを汚染しません。

- **フック（Hooks）**：PythonまたはShellフック。ツール呼び出し前後のインターセプト、監査ログ、自動フォーマット、テストゲートをサポート。

- **MCPプロトコル**：Model Context Protocolを通じて外部ツールサーバー（GitHub、Filesystemなど）に接続。

- **コンテキスト圧縮**：2段階圧縮（ツール結果の切り捨て＋LLM要約）。超長い会話をサポート。

- **セキュアサンドボックス**：コマンドホワイトリスト、パスエスケープ検出、危険コマンド遮断、機密ファイル保護、スクリプトインジェクション遮断。

- **黒金テーマCLI**：中国語幅の自動調整、コードハイライト、Diff着色、思考折りたたみ。

# 白澤CLIインターフェース

<div align="center">
白澤 CLI 起動画面
</div>

<p align="center">
  <img src="image/clipage01.jpg" alt="白澤 CLI 起動画面" width="800" />
</p>

<div align="center">
白澤 CLI 実行画面--01
</div>

<p align="center">
  <img src="image/clipage02.jpg" alt="白澤 CLI 実行画面" width="800" />
</p>

<div align="center">
白澤 CLI 実行画面--02
</div>

<p align="center">
  <img src="image/clipage03.jpg" alt="白澤 CLI 実行画面" width="800" />
</p>

# インストール

## 前提条件

- Python 3.10+（tomllibが必要。3.11+では内蔵、3.10ではtomliをインストール）

- pip

## ソースからのインストール

### ダウンロード方法は2つ

1. `pip install https://github.com/Xu123-Bob/Baize.git`

    bash -- Win+Rを押して `cmd` を入力し、次を入力：

    baize

2. リポジトリページで `<> Code` --> `Download ZIP` をクリック

(1) 解凍後、本ファイルのディレクトリに移動：

    bash -- Win+Rを押してcmdを入力

    cd 解凍後のディレクトリ

    pip install -r requirements.txt

    python -m Baize

インストール後、Win+Rを押してcmdを入力しCLIを開き、`baize` と入力すると実行できます。

(2) ZIPをダウンロードしてローカルインストール。解凍後ディレクトリに移動し、実行：

    bash -- Win+Rを押してcmdを入力

    pip install .

インストール後、Win+Rを押してcmdを入力しCLIを開き、`baize` と入力すると実行できます。

### オプション：データ接続依存関係のインストール（データ分析の重要ツール）

白澤にSPSSやSQLデータベースを操作させたい場合、追加でインストール：

```bash
pip install -r requirements-data.txt
```

`requirements-data.txt` に含まれるもの：
- `spss-studio-mcp`：SPSS統計分析MCPサーバー（本機にIBM SPSS Statisticsがインストールされている必要あり）
- `atengk-mcp-server-rdbms`：汎用リレーショナルデータベースMCPサーバー（PostgreSQL / MySQL / SQL Server / Oracle / 達夢など）
- `pyodbc`：SQL Serverに必要なODBC Pythonバインディング

または、プロジェクトが `pyproject.toml` でインストールされている場合、extrasも使用可能：

```bash
pip install -e ".[data]"          # データ接続依存関係を一括インストール
pip install -e ".[spss]"          # SPSSのみ
pip install -e ".[sql]"           # 汎用SQLのみ
pip install -e ".[sql-mssql]"     # SQL Server専用（pyodbc含む）
```

- **⚠️ SQL Serverユーザー注意：pyodbcはPythonバインディングのみです。システムレベルでMicrosoft ODBC Driver 18 for SQL Serverもインストールする必要があります。**
- **⚠️ SPSSユーザー注意：spss-studio-mcpはMCPブリッジ層のみです。本機にIBM SPSS Statistics（バージョン20–31）がインストールされ、ライセンス認証済みで、環境変数 `SPSS_INSTALL_PATH` がSPSSインストールディレクトリを指している必要があります。現在、SPSSエンジンは主にWindowsで完全な分析機能をサポートしています。Linux/macOSでは「ファイルモード」に降格できます（.savファイルの読み取り、メタデータ表示、データプレビューは可能ですが、統計分析はサポートされません）。**

# クイックスタート

1. 初回実行

```bash
baize
```

初回実行時、白澤は自動的に2つの設定ファイルを生成します：

```
~/.baize/config.toml   # バックエンド設定（DeepSeek / OpenAI / Ollamaを選択）
~/.baize/.env          # キーファイル
```

Windowsのパスは `C:\Users\あなたのユーザー名\.baize\` です。

2. バックエンドの選択

`~/.baize/config.toml` を開き、**active_provider** を変更（必ず変更）：

```toml
# 白澤設定ファイル
# active_providerを変更してバックエンドを切り替え  # 選択肢："deepseek" / "qwen" / "kimi" / "glm" / "openai" / "ollama"

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

3. キーの入力

`~/.baize/.env` を編集。**使用するLLMがある場合、その行の先頭の `# ` を削除し、他のLLMの先頭に `# ` を追加してAPI出力をロックします。API Keyを入力したら、必ず保存してください。保存後のみ有効になります**：

```env
# ============================================================
# 白澤キーファイル
# ============================================================
# 使用するバックエンドのキーのみ入力し、他はコメントのままにします。
# 変数名は config.toml の env_key フィールドと一致させる必要があります。
#
# 場所：
#   Linux / macOS: ~/.baize/.env
#   Windows:       C:\Users\あなたのユーザー名\.baize\.env
# ============================================================

# ---------- DeepSeek（デフォルトバックエンド） ----------
# 取得先：https://platform.deepseek.com/api_keys
DEEPSEEK_API_KEY=

# ---------- OpenAIまたは任意のOpenAI互換インターフェース（オプション） ----------
# Groq、通義、Moonshot、智譜、OpenAIなどに適用
# 注意：base_urlは config.toml の [model_providers.xxx] で設定し、ここではありません
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
# Ollamaが localhost:11434 で動作していることを確認するだけです。ここでの設定は不要です。
```

4. 再起動

```bash
baize
```

黒金のロゴとウェルカムメッセージが表示されれば起動成功です。

# 使用例

起動後、`>>> 降旨：` プロンプトで自然言語で要望を記述するだけです：

```
>>> 降旨：Douban Top250をスクレイピングしてCSVに保存するPythonスクリプトを書いて

>>> 降旨：src/ 以下のすべてのPythonファイルの型エラーをチェックして

>>> 降旨：このリポジトリでrequestsを使っている箇所をすべて探し、httpxに変更して
```

## 多言語インタラクション

白澤は**9言語**をサポート：中国語、English、日本語、한국어、Español、Français、deutsch、русский、العربية。

切り替え方法は2つ：

### 方法1：直接話す（自動検出）

白澤は入力言語を自動認識して切り替えます：

```
>>> 降旨：Hello, help me write a Python script
[システム] 入力言語をEnglishと検出しました。白澤はEnglishインタラクションに切り替えました。
（白澤が英語で返信）

>>> 降旨：日本語で答えてください
[システム] 入力言語を日本語と検出しました。白澤は日本語インタラクションに切り替えました。
（白澤が日本語で返信）
```

### 方法2：手動コマンド

```
>>> 降旨：/lang                # 現在の言語と利用可能なリストを表示
[システム] 現在の言語：中国語 (zh)
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

**言語名 / 言語コード / 中国語名 / 原語名**の4つの書き方をサポート。たとえば英語に切り替える場合、`English`、`en`、`英语`、`英文` のいずれでも可能です。

## 内蔵コマンド

- `/exit, /quit` --> 白澤を終了
- `/clear` --> 会話履歴、ToDo、思考記録、ツール記録をクリア
- `/compact` --> 手動でコンテキストを圧縮（会話が長すぎる場合に使用）
- `/commit` --> 現在のセッションを保存しGitにコミット（Gitリポジトリ内の場合）
- `/lang` --> 現在の言語を表示；`/lang en` で英語に切り替え（言語コードまたは言語名をサポート）
- `/skills` --> 利用可能なすべてのスキルを一覧表示
- `/skills reload` --> ユーザースキルディレクトリを再読み込み
- `/unload` --> 現在アクティブなスキルをアンロード
- `/show thought` --> 完全な思考記録を表示
- `/show tool` --> ツール呼び出し記録を表示
- `/show all` --> すべてのセッション履歴を表示
- `/技能名` --> 指定したスキルを読み込み（曖昧マッチ対応）
- `/privacy` --> プライバシーマスキング制御（on / off / strict / status / rules / test / clear）
- `/privacy rule-off <name>` --> 特定のマスキングルールを無効化（例：`/privacy rule-off phone_intl`）
- `/privacy rule-on  <name>` --> ルールを再有効化

## データ接続の使用例

SPSS / SQLを設定後、自然言語で直接操作できます：

```text
>>> 降旨：SPSSでdata.savを開き、変数リストとサンプルサイズを教えて

>>> 降旨：data.savに対して記述統計を実行し、線形回帰を実行して

>>> 降旨：salesテーブルで先月の売上が10万を超える注文を顧客ごとに集計して

>>> 降旨：SPSS分析結果をCSVにエクスポートし、SQLで顧客マスタと結合して
```

# Ollamaローカルモデル（ゼロコスト）

クラウドAPIを使いたくない場合は、ローカルOllamaを使用：

```bash
# 1. Ollamaをインストール：https://ollama.com/download
# 2. モデルを取得
ollama pull qwen2.5:7b

# 3. Ollamaサービスを起動
ollama serve

# 4. ~/.baize/config.toml を変更
active_provider = "ollama"

# 5. 白澤を起動
baize
```

推奨モデル：`qwen2.5:7b`（中国語に強い）、`llama3.1:8b`、`deepseek-r1:7b`。

# 拡張メカニズム

白澤は4つの拡張方法をサポート。現在の作業ディレクトリに置くだけで有効になります。

## スキル（Skills）

`./skills/スキル名/SKILL.md` に領域知識を記述。AIは複雑なタスクに遭遇すると主動的に読み込みます。

```markdown
---
name: pandas-eda
description: pandasによる探索的データ分析のベストプラクティス
tags: data,python
---

# Pandas EDAガイド

## コアステップ
1. df.info() でフィールド型と欠損を確認
2. df.describe() で記述統計
...
```

会話中に `/pandas-eda` で手動読み込みも可能。

## サブエージェント（Subagents）

`./subagent/ロール名/AGENT.md` に専用サブエージェントを定義。メインエージェントはagentツールでタスクを委譲できます。

```markdown
---
name: code-reviewer
description: 厳格なコードレビュアー
---

あなたはシニアコードレビュアーです。レビュー時は以下を優先：
1. 境界条件と例外処理
2. リソースリーク
3. 並行安全性
...
```

## フック（Hooks）

`./hooks/` に配置：

- `PreToolUse-*.sh`
- `PostToolUse-*.sh`
- `Stop-*.sh`

JSON入力を受け取り、決定を返します：

```bash
#!/bin/bash

# PreToolUse-guard.sh

read -r input

if echo "$input" | grep -q "rm -rf"; then
  echo '{"hookSpecificOutput":{"permissionDecision":"block","permissionDecisionReason":"Deletion prohibited"}}'
fi
```

Pythonフックは内蔵APIを直接呼び出せます（`Baize.py` の `hook_*` 関数を参照）。

## MCPサーバー

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

# セキュリティ設計（コア）

白澤はデフォルトで以下のセキュリティ機構を有効にします：

- **コマンドホワイトリスト**：`ls`、`cat`、`grep`、`git`、`python3` などの一般的なコマンドのみ許可。
- **パスエスケープ検出**：すべてのファイル操作は現在の作業ディレクトリと `/tmp` 内に制限。
- **危険コマンド遮断**：`rm -rf /`、フォーク爆弾、`curl | sh`、`git push --force` などを遮断。
- **機密ファイル保護**：`.env`、`.ssh/`、`id_rsa`、`*.pem` などの変更を禁止。
- **スクリプトインジェクション遮断**：`python -c "os.system(...)"` などのバイパスを検出。
- **プロセスリソース制限**：Linux/macOSでCPU、メモリ、プロセス数を制限。
- **プライバシーマスキング（双方向可逆）**：送信時にPIIをランダムプレースホルダーに置換、受信時に復元；ディスク保存時は独立してマスキング。
- **プレースホルダーインジェクション耐性**：64ビット暗号学的ランダムトークン＋入力側中和＋セッション分離。
- **監査ログマスキング**：`hook_audit_log` は書き込み前にマスキング＋切り捨て＋失敗時は書き込み拒否。

信頼できるプロジェクトで制限を緩和したい場合、`Baize.py` の `ALLOWED_COMMANDS` と `FORBIDDEN_PATH_PATTERNS` を変更できます。

# プライバシーマスキング（コア）

白澤には**双方向可逆＋ディスク保存時マスキング**のプライバシー保護機構が内蔵され、入力からディスクまでの完全な経路をカバーします：

- **送信**：LLMに送信する前に、PIIは推測不可能なプレースホルダーに置換
- **受信**：LLM応答内のプレースホルダーを原文に復元
- **ディスク保存**：セッションファイル、圧縮トランスクリプト、監査ログは書き込み前に**独立してマスキング**され、ディスクに平文を残さない

**デフォルトでは無効**。必要時に有効化。

## 有効化の2つの方法

### 方法1：自然言語

会話中に直接言う：

```
>>> 降旨：プライバシーマスキングを有効にして
[システム] プライバシーマスキングが有効になりました（標準モード）。

>>> 降旨：厳格マスキングを有効にして
[システム] プライバシーマスキングが有効になりました（厳格モード）。

>>> 降旨：プライバシー保護を無効にして
[システム] プライバシーマスキングが無効になりました。
```

### 方法2：スラッシュコマンド

- `/privacy on` 標準モードを有効化
- `/privacy strict` 厳格モードを有効化
- `/privacy off` 無効化
- `/privacy status` 状態、セッションID、ルール数、LRU/TTL統計を表示
- `/privacy rules` すべてのルールを一覧表示（有効状態含む）
- `/privacy rule-off <name>` 特定のルールを無効化
- `/privacy rule-on  <name>` ルールを再有効化
- `/privacy test <text>` マスキング効果をテスト
- `/privacy clear` プレースホルダーマッピングをクリアし、**セッションIDをローテート**

## 2段階モード

**標準**：中国本土の携帯電話番号、身分証番号、銀行カード番号（Luhnチェック）、メール、IPv4/IPv6、OpenAI/Anthropic/GitHub/AWS APIキー、Bearerトークン、秘密鍵ブロック、パスワードフィールド、URL資格情報

**厳格**：標準モードのすべて＋中国語姓名、QQ番号、WeChat ID、中国本土のナンバープレート

## 動作原理

ユーザー入力（実際のPIIを含む）→ messagesに原文を保存

↓ `sanitize_messages()`

LLMに送信されるのは `[[PHONE_1]]`、`[[EMAIL_1]]`

↓ LLM応答

返されたプレースホルダー → `restore_message()`

原文に復元 → ディスク保存 / 表示 / ツール実行

- **プライバシーマスキング（双方向可逆）**：送信時にPIIをランダムプレースホルダーに置換、受信時に復元；ディスク保存時は独立してマスキング。
- **プレースホルダーインジェクション耐性**：64ビット暗号学的ランダムトークン＋入力側中和＋セッション分離。
- **監査ログマスキング**：`hook_audit_log` は書き込み前にマスキング＋切り捨て＋失敗時は書き込み拒否。

## ツールパラメータのスマート分级

**マスキングされる**（純粋なテキストパラメータで、実際の実行に関与しない）：
- `todo`、`ask_user_question`、`task_create`、`task_update`

**マスキングされない**（パス/コマンド/URLが実際に使用される）：
- `run_read` / `run_write` / `run_edit` / `run_glob` / `run_grep`（パスはIOに使用）
- `run_bash` / `background_run`（コマンドは実行される）
- `run_webfetch` / `web_search`（URLは実際にネットワークに送信される）
- `set_workspace`（パスは `chdir` に使用）
- `load_skills`（スキル名は列挙）
- `agent`（サブエージェントコンテキストは独立してマスキング）
- `mcp_*`（未知のセマンティクス、保守的に処理）

**ディスク保存時はすべてマスキング**（保存内容は再実行されないため、安全性優先）。

## ディスク保存時マスキング

**デフォルトで有効**。メモリ内マスキングとは独立。`/privacy off`（メモリ内マスキングなし）でも、ディスク保存時は少なくとも標準ルールでマスキングされます。

**主な特徴**：
- ディスク保存時マスキングは**独立した、一度限りのマッピングテーブル**を使用——ディスクに書き込まれたプレースホルダーは**復元不可能**（マッピングテーブルは破棄されるため）
- ディスク保存時マスキングが**失敗した場合、平文の書き込みを拒否**（降格なし、静かなスキップなし）
- 旧バージョンのセッションファイルに平文が含まれる場合、初回保存時に自動マスキングして書き換え

**無効化方法**（非推奨）：`Baize.py` の `PERSIST_REDACT_ENABLED = False` を変更。

## 例

```
>>> 降旨：/privacy test 私の電話番号は 13812345678、メールは a@b.com
原文：私の電話番号は 13812345678、メールは a@b.com
マスキング：私の電話番号は [[PHONE_1]]、メールは [[EMAIL_1]]
復元：私の電話番号は 13812345678、メールは a@b.com

>>> 降旨：/privacy status
[プライバシーマスキング]
現在のモード : 標準モード (standard)
セッションID : 7d2f5e91
有効ルール数 : 34 / 41
アクティブプレースホルダー : 2
マッピング容量 : 2 / 2000
TTL : 86400 秒
LRU淘汰 : 0
TTL淘汰 : 0
マスキング呼び出し回数: 3
復元呼び出し回数: 3

>>> 降旨：/privacy rules
[プライバシーマスキングルール一覧] 全41件
【標準+厳格】
[✓] phone_cn 中国本土携帯電話番号 (standard,strict)
[✓] id_card_cn 中国本土身分証番号 (standard,strict)
[✓] jwt JWT Token (standard,strict)
...
【厳格のみ】
[✓] name_cn 中国語姓名 (strict)
[✓] address_cn 中国語詳細住所 (strict)
...
使用方法：
/privacy rule-off <name> ルールを無効化
/privacy rule-on <name> ルールを再有効化
```

### テスト例

<div align="center">
プライバシー保護テスト画面--01
</div>

<p align="center">
  <img src="image/privary01.jpg" alt="プライバシー保護テスト画面" width="800" />
</p>

<div align="center">
プライバシー保護テスト画面--02
</div>

<p align="center">
  <img src="image/privary02.jpg" alt="プライバシー保護テスト画面" width="800" />
</p>

# データ接続（コア）

白澤は**MCP（Model Context Protocol）**を通じて企業データ分析ソフトウェアと接続します。メインプログラムの変更は不要——`MCP/mcp_config.json` にサーバーを登録するだけです。

## SPSS接続

### 前提条件

- 本機にIBM SPSS Statisticsがインストール済み（バージョン20–31、Windows推奨）
- SPSSがライセンス認証され正常に起動できる

### 設定手順

1. **SPSSインストールディレクトリを確認：** デフォルトパスは通常 `C:\Program Files\IBM\SPSS Statistics\` の後にバージョン番号（例：31）。

2. **環境変数を設定**（`.env` またはシステム環境変数）：

```text
SPSS_INSTALL_PATH=C:\Program Files\IBM\SPSS Statistics\31
```

3. **状態を検証**：

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

`spss-studio-mcp` がSPSSエンジンを見つけられなかったが、`pyreadstat` + `pandas` は正常な場合、**ファイルモード**になります：

- `.sav` の読み取り、メタデータ表示、データプレビュー、CSV ↔ SAV変換が可能
- 統計（t検定、回帰、ANOVAなど）は実行不可

解決策：`MCP/mcp_config.json` の `SPSS_INSTALL_PATH` を正しく設定するか、ファイルモード降格を受け入れる。

## SQL接続

### サポートされるデータベース

PostgreSQL、MySQL、MariaDB、SQL Server、Oracle、達夢、人大金倉、TiDB、OceanBaseなど（SQLAlchemy 2.0ドライバベース）。

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

### セキュリティガードレール（内蔵）

`atengk-mcp-server-rdbms` は多層保護を提供：

- **ASTレベルSELECTガード**：`sqlglot` で構文木を解析し、`DELETE/UPDATE/DROP/TRUNCATE` などの書き込み操作を物理的に遮断。
- **自動LIMIT注入**：行数未指定のクエリに強制的に `LIMIT 100` を追加し、全表取得によるメモリオーバーフローを防止。
- **デフォルト読み取り専用**：書き込み操作は `--allow-dml` / `--allow-ddl` で明示的に許可する必要あり。
- **SQLインジェクション遮断**：AST層で文字列結合による悪意ある文を拒否。

### 複数データベースの同時設定

複数のデータベースに同時接続したい場合、複数のサーバーを登録：

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

白澤は自動的にすべてのツールを `MATERTOOLS` にマージし、LLMがタスクに応じて自動選択します。

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
    ├── __init__.py
    ├── Baize.py                # メインプログラムとAgent Loop
    ├── config.py               # マルチバックエンド設定読み込み
    ├── ui_theme.py             # CLIレンダリングテーマ
    ├── utils.py                # 汎用ユーティリティ
    ├── logo.txt
    ├── skills/                 # 内蔵スキル
    ├── subagent/               # 内蔵サブエージェント
    ├── core/                   # コアロジック（副作用なし、単体テスト可能）
    |   ├── __init__.py
    |   ├── history.py          # セッション履歴クリーニング / トークン推定 / 圧縮
    |   └── privacy.py          # プライバシーマスキング：PII識別 / プレースホルダー置換 / 可逆復元
    ├── hooks/                  # 内蔵フック
    └── MCP/                    # MCPクライアントと設定
        ├── __init__.py
        ├── mcp_client.py
        └── mcp_config.json
```

# 環境変数リファレンス

| 変数 | 説明 | デフォルト |
| --- | --- | --- |
| `DEEPSEEK_API_KEY` | DeepSeek APIキー | — |
| `DEEPSEEK_BASE_URL` | DeepSeekエンドポイント | `https://api.deepseek.com` |
| `OPENAI_API_KEY` | OpenAI互換エンドポイントキー | — |
| `OPENAI_BASE_URL` | OpenAI互換エンドポイント | `https://api.openai.com/v1` |
| `OLLAMA_BASE_URL` | Ollamaサービスアドレス | `http://localhost:11434` |

**上記変数は `~/.baize/.env` に記述してください。シェル設定ファイルの変更は不要です。**

データ分析変数：

| 変数 | 説明 | デフォルト |
| --- | --- | --- |
| `SPSS_INSTALL_PATH` | IBM SPSS Statisticsインストールディレクトリ | —（未設定の場合はファイルモードに降格） |
| `DATABASE_URL` | SQL MCPのデータベース接続文字列 | —（MCPサーバーが読み取り） |

**上記変数は `MCP/mcp_config.json` に記述してください。**

# 開発

## テストの実行

本プロジェクトはpytestを使用。開発前に編集可能モードでパッケージと開発依存関係をインストール：

```bash
pip install -e ".[dev]"
```

すべてのテストを実行：

```bash
python -m pytest tests/ -v
```

単一ファイルのみ：

```bash
python -m pytest tests/test_history.py -v
```

## コード構造の規約

- `agent/`：パッケージに含まれるメインパッケージ。すべての実行時ロジックとリソース（skills、subagent、hooks、MCP）がここにあります。
- `agent/core/`：純粋なロジックモジュール。外部副作用なし。**単独でテスト可能でなければならない。** この種のロジックを追加する場合はここに置き、テストを添付。
- `tests/`：`agent/` 下のソースファイルと1対1に対応し、`test_<モジュール名>.py` と命名。
- 外部依存（ネットワーク、ディスク、グローバル状態）を持つ関数は、テストで置き換えられるようパラメータ経由で依存を注入してください。

# ❓ よくある質問

- Q：キーはどこに入力しますか？

A：`~/.baize/.env` です。プロジェクトルートの `.env` ではありません。

- Q：バックエンドを変更したら再インストールが必要ですか？

A：不要です。`~/.baize/config.toml` の `active_provider` を変更するだけです。

- Q：ローカルOllamaにキーは必要ですか？

A：不要です。`active_provider = "ollama"` を選択し、`env_key` を空にします。

- Q：作業ディレクトリを切り替えるには？

A：会話中に直接「/path/to/projectに切り替えて」と言うと、白澤が `set_workspace` ツールを呼び出します。

- Q：コンテキストが長すぎるとどうなりますか？

A：白澤は自動的に2段階圧縮します：まず古いツール結果を切り捨て、次にLLMに要約を要求。手動で `/compact` も可能。

- Q：ファイルを誤って削除しませんか？

A：デフォルトのコマンドホワイトリストが `rm -rf /` などの危険操作を遮断；ファイル書き込み前にDiffを表示し確認を求めます。

- Q：白澤をSPSSに接続するには？

A：1. `pip install -r requirements-data.txt` をインストール；2. 環境変数 `SPSS_INSTALL_PATH` をSPSSインストールディレクトリに設定；3. `MCP/mcp_config.json` でspssサーバーを有効化。詳細は「データ接続（SPSS / SQL）」セクション参照。

- Q：`SPSS batch: NOT FOUND` の場合は？

A：SPSSエンジンが見つからないことを示します。`SPSS_INSTALL_PATH` が `stats.exe` を含むディレクトリを正しく指しているか確認；`.sav` ファイルのみを扱う場合はこの警告を無視できます（ファイルモードに降格）。

- Q：SQLデータベースに接続するには何をインストールする必要がありますか？

A：Pythonレベルでは `atengk-mcp-server-rdbms` をインストール（`pip install` で自動完了）。**SQL ServerユーザーはシステムレベルでMicrosoft ODBC Driver 18もインストールする必要があります**。これはpipではインストールできません。

- Q：白澤はデータベースデータを誤って削除しませんか？

A：しません。SQL MCPはデフォルトでSELECTのみ許可し、AST構文木レベルですべての書き込み操作を遮断。さらに白澤専用の**読み取り専用データベースアカウント**を作成することを強く推奨します。

- Q：SPSS分析結果のデータはLLMに漏れませんか？

A：プライバシーマスキングが有効な場合（`/privacy on`）、ツール戻り結果はLLMに送信される前に電話番号、メール、身分証などのPIIが自動マスキングされます。**ただし、読み取り専用データベースアカウント＋データサンプリング**（必要なフィールドのみクエリ）も併用してリスクを低減することを推奨。

- Q：SPSS/SQLを追加すると、毎回の会話が遅くなりトークンも増えるのはなぜ？

A：MCPサーバーが公開するツール定義が毎回の会話に含まれてLLMに送信されるためです。SPSSには60以上のツールがあり、約6,000–12,000トークンの固定オーバーヘッドが増加します。よく使うワークフローがSPSSに関係ない場合、`enabled` を `false` にして必要時に有効化できます。

# 🤝 コントリビュート

IssueとPRを歓迎します。PRを提出する前に `CONTRIBUTOR.md` を読むことを推奨します。

### PRを提出してくださったすべてのコントリビューターに感謝

- GitHubコントリビューター：
[@anupamme](https://github.com/anupamme)
[@wangyipeng0724](https://github.com/wangyipeng0724)

[![Contributors](https://contrib.rocks/image?repo=Xu123-Bob/Baize&v=2)](https://github.com/Xu123-Bob/Baize/graphs/contributors)

# ライセンス

MIT License

# 謝辞

- 本プロジェクトは中国のAtomGitでホストされています。プロジェクトリンク：https://atomgit.com/Com_Xu/Baize

- AtomGitが本プロジェクトをG-starインキュベーションプロジェクトに採用してくださったことに感謝します。

- PRコントリビューター、抖音のフォロワー、フォローしてくださる学生の皆さんに感謝します。

- インスピレーションはClaude Code、Codexなどの優れたAI Codingツールから。

- DeepSeek、OpenAI SDK、MCPをベースに構築。

- Vibe Codingの道を共に歩むすべての開発者に感謝します。

# ☕ スポンサー

白澤が役に立ったら、スポンサーとして支援していただけると嬉しいです。個人開発にも多くの時間がかかります。スポンサーは製品アップデートのスケジュールを変更するものではありません。ご支援ありがとうございます！

<p align="center">
  <img src="image/support.jpg" alt="WeChat QRコード" width="200" />
</p>

# お問い合わせ

- 白澤に興味がある方、またはオープンソース協力に参加したい方は、以下の方法でご連絡ください。
- **現在、求職中です。市場調査とユーザーリサーチに従事した経験があり、Agentについてもある程度理解しています。私の能力がご要望に合致する場合、ぜひ一緒に働きたいです（希望職種：AIプロダクト運営 / ユーザーリサーチ / 市場調査）。**

<p align="center">
  <img src="image/weixin.jpg" alt="WeChat QRコード" width="200" />
</p>

<p align="center">WeChat QRコードをスキャンしてください。Baizeオープンソース協力または企業採用と明記してください。</p>

<p align="center">
  <img src="image/抖音.png" alt="抖音QRコード" width="200" />
</p>

<p align="center">抖音QRコードをスキャンしてフォロー</p>