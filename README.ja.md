<div align="center">

<img src="image/logopage02.png" alt="白澤 Baize ロゴ" width="320" />

# 白澤 Baize

**万物に通じ、安全にコーディングを共に。**

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

中国古代神話に登場し、万物に通じる瑞獣。今はエンタープライズ向けデータ分析と VibeCoding アシスタントへ。

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

# インストール

## 前提条件

- Python 3.10+（tomllib が必要。3.11+ では標準搭載。3.10 では tomli をインストール）
- pip

## ソースからのインストール

### ダウンロード方法は2つ

1. `pip install https://github.com/Xu123-Bob/Baize.git`

bash -- Win+R を押して cmd と入力し、次を実行：

    baize

2. リポジトリページで `<>Code` --> Download ZIP をクリック

(1) 解凍後、このファイルのディレクトリへ移動：

bash -- Win+R を押して cmd と入力

    cd 解凍後のディレクトリ

    pip install -r requirements.txt

    python -m Baize

インストール後、Win+R で cmd を開き、CLI 界面で `baize` と入力すれば実行できる。

(2) ZIP をダウンロードしてローカルインストールする場合、解凍後にディレクトリへ入り、実行：

bash -- Win+R を押して cmd と入力

    pip install .

インストール後、Win+R で cmd を開き、CLI 界面で `baize` と入力すれば実行できる。

# クイックスタート

1. 初回実行

bash

    baize

初回実行時、白澤は2つの設定ファイルを自動生成する：

```
~/.baize/config.toml   # バックエンド設定（DeepSeek / OpenAI / Ollama を選択）

~/.baize/.env          # キーファイル>
```

Windows のパスは `C:\Users\ユーザー名\.baize\`。

2. バックエンドを選択

`~/.baize/config.toml` を開き、`active_provider` を変更：

toml
```
active_provider = "deepseek"    # または "openai" / "ollama"

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
name = "Ollama（ローカル）"
base_url = "http://localhost:11434/v1"
env_key = ""
model = "qwen2.5:7b">
```

3. キーを入力

`~/.baize/.env` を編集：

env
```
# DeepSeek バックエンドでは必須

DEEPSEEK_API_KEY=sk-あなたのキー


# OpenAI 互換 API では必須（GLM / Qwen / Kimi / OpenAI）

#OPENAI_API_KEY=あなたのキー

#Ollama ローカルはキー不要
```

4. 再起動

bash

    baize

黒金のロゴとウェルカムメッセージが表示されれば起動成功。

# 使用例

起動後、`>>> 降旨：` プロンプトで自然言語で要件を記述する：

```
>>>降旨：Python で Douban Top250 をスクレイピングし、CSV として保存するスクリプトを書いて

>>>降旨：src/ 以下のすべての Python ファイルの型エラーをチェックして

>>>降旨：このリポジトリ内で requests を使っている箇所をすべて探し、httpx に変更して
```

## 多言語インタラクション

白澤は **9 言語** をサポートします：中文、English、日本語、한국어、Español、Français、deutsch、русский、العربية。

切り替え方法は二通り：

### 方法 1：そのまま話す（自動検出）

入力を自動で言語判定して切り替えます：

```
>>> 降旨：こんにちは、Python スクリプトを書いてください
[system] 入力言語を 日本語 と判定しました。白澤を 日本語 に切り替えました。
（日本語で応答）

>>> 降旨：Hello, write me a script
[system] 入力言語を English と判定しました。白澤を English に切り替えました。
（英語で応答）
```

### 方法 2：手動コマンド

```
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

## 白澤 CLI 界面

<div align="center">
白澤 CLI 起動画面
</div>

<p align="center">
  <img src="image/clipage01.jpg" alt="白澤 CLI 起動画面" width="800" />
</p>

<div align="center">
白澤 CLI 実行画面
</div>

<p align="center">
  <img src="image/clipage02.jpg" alt="白澤 CLI 実行画面" width="800" />
</p>

## 組み込みコマンド

- `/exit`、`/quit` --> 白澤を終了
- `/clear` --> 会話履歴、ToDo、思考記録、ツール記録をクリア
- `/compact` --> 手動でコンテキストを圧縮（会話が長すぎる場合に使用）
- `/commit` --> 現在のセッションを保存し、Git にコミット（Git リポジトリ内の場合）
- `/lang` → 現在の言語を表示；`/lang en` で英語に切替（コードまたは名前）
- `/skills` --> 利用可能なすべてのスキルを一覧表示
- `/skills reload` --> ユーザースキルディレクトリを再読み込み
- `/unload` --> 現在有効なスキルをアンロード
- `/show thought` --> 完全な思考記録を表示
- `/show tool` --> ツール呼び出し記録を表示
- `/show all` --> すべてのセッション履歴を表示
- `/スキル名` --> 指定スキルを読み込み（あいまい一致対応）
- `/privacy` --> プライバシー脱敏の制御（下記「プライバシー脱敏」章を参照）

# Ollama ローカルモデル（ゼロコスト）

クラウド API を使いたくない？ローカル Ollama を使う：

bash

    #1. Ollama をインストール：https://ollama.com/download
    #2. モデルを取得
    ollama pull qwen2.5:7b

    #3. Ollama サービスを起動
    ollama serve

    #4. ~/.baize/config.toml を変更
    active_provider = "ollama"

    #5. 白澤を起動
    baize

推奨モデル：`qwen2.5:7b`（中国語に強い）、`llama3.1:8b`、`deepseek-r1:7b`。

# 拡張機構

白澤は4種類の拡張方法をサポート。すべて現在の作業ディレクトリに置けば有効になる。

## スキル（Skills）

`./skills/スキル名/SKILL.md` に領域知識を書く。AI は複雑なタスクに遭遇すると主動的に読み込む。

markdown

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

会話中に `/pandas-eda` で手動読み込みもできる。

## サブエージェント（Subagents）

`./subagent/役割名/AGENT.md` に専用サブエージェントを定義。メインエージェントは `agent` ツールでタスクを委任できる。

markdown

    ---
    name: code-reviewer

    description: 厳格なコードレビュアー
    ---

    あなたはシニアコードレビュアーです。レビューでは以下を優先：
    1. 境界条件と例外処理
    2. リソースリーク
    3. 並行安全性
    ...

## フック（Hooks）

`./hooks/` の下に配置：

- `PreToolUse-*.sh`
- `PostToolUse-*.sh`
- `Stop-*.sh`

JSON 入力を受け取り、判断を返す：

bash

    #!/bin/bash

    #PreToolUse-guard.sh

    read -r input

    if echo "$input" | grep -q "rm -rf"; then

    echo '{"hookSpecificOutput":{"permissionDecision":"block","permissionDecisionReason":"削除禁止"}}'

    fi

Python フックは組み込み API を直接呼び出せる（`Baize.py` の `hook_*` 関数を参照）。

## MCP サーバー

`./MCP/mcp_config.json` で外部ツールサーバーを設定：

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

```
>>>降旨：プライバシー脱敏を有効にして
[system] プライバシー脱敏を有効にしました（標準モード）。

>>>降旨：厳格な脱敏を有効にして
[system] プライバシー脱敏を有効にしました（厳格モード）。

>>>降旨：プライバシー保護を無効にして
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

```
>>>降旨：/privacy test 私の電話は 13812345678、メールは a@b.com
原文：私の電話は 13812345678、メールは a@b.com
脱敏：私の電話は [[PHONE_1]]、メールは [[EMAIL_1]]
復元：私の電話は 13812345678、メールは a@b.com

>>>降旨：/privacy status
[プライバシー脱敏]
現在のモード: 標準モード (standard)
有効ルール : 15 / 19
プレースホルダー: 2
脱敏呼び出し: 3
復元呼び出し: 3
```

# ディレクトリ構成

```
baize-agent/
├── pyproject.toml              # パッケージ設定
├── README.md
├── tests/                      # テスト（パッケージには含まれない）
|   ├── __init__.py
|   ├── test_history.py
|   └── test_skill_loader.py
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
    |   ├── __init__.py
    |   ├── history.py          # セッション履歴クリーニング / token 推定 / 圧縮
    |   └── privacy.py          # プライバシー脱敏：PII 検出 / プレースホルダー置換 / 可逆復元
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

# 開発

## テスト実行

本プロジェクトは pytest を使用。開発前にパッケージと開発依存を編集可能モードでインストール：

    pip install -e ".[dev]"

全テスト実行：

    python -m pytest tests/ -v

単一ファイルのみ：

    python -m pytest tests/test_history.py -v

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

- Q：英語や日本語で回答させるには？

A：`English` または `日本語` と言えば自動で切り替わります。`/lang en`（または `/lang ja`）も使えます。以降の思考と回答はその言語になります。中国語に戻すには `中文` と言うか `/lang zh` と入力します。

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

- 開発者はアイデアと意思決定に集中し、白澤が雑務と実行を処理する。プログラミングを直感に戻し、創造を神話のように流暢に。

# ☕ サポート

もし白沢があなたに役立つなら、ぜひスポンサーとしてご支援ください。独立開発には多くの時間と労力がかかりますので、ご支援は製品の更新スケジュールを変えるものではありません。ありがとうございます！

<p align="center">
  <img src="image/support.jpg" alt="WeChat QR" width="200" />
</p>

# 連絡先

- 白澤に興味がある方、オープンソース協力に参加したい方、または私の更新を継続的に知りたい方は、以下の方法で連絡できます。
- **現在、私は求人中であります。これまで市場調査やユーザーリサーチの業務に従事しており、Agentについても一定の知識を持っています。私のスキルが貴社のニーズに合致する場合、ぜひご一緒に働きたいと思います（意向ポジション：AI製品運営／ユーザーリサーチ／マーケティングリサーチ）。**

<p align="center">
  <img src="image/weixin.jpg" alt="WeChat QR コード" width="200" />
</p>

<p align="center">微信でQRコードをスキャンしてください。「Baizeオープンソース協力」または「企業採用」と明記してください。</p>

<p align="center">
  <img src="image/抖音.png" alt="Douyin QR コード" width="200" />
</p>

<p align="center">Douyin でスキャンしてフォロー</p>