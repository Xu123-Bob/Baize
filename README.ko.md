<div align="center">

<img src="image/logopage02.png" alt="백택 Baize 로고" width="320" />

# 백택 Baize

**아는 것은 모두 말하고, 비밀은 굳게 지킨다**

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

중국 신수(神獸)에서 모티프를 얻은 Vibe Coding 및 데이터 분석용 보안 어시스턴트.

**오픈소스 Coding Agent CLI로, 강력한 프라이버시 보호와 다국어 상호작용을 제공합니다. 다중 백엔드(DeepSeek / OpenAI 호환 / 智譜 / 通義 / Kimi / 로컬 Ollama)를 지원하며, 도구 호출, 스킬 로딩, 서브에이전트 위임, 컨텍스트 압축, 보안 샌드박스 등 완전한 기능을 갖추고 있습니다.**

----------

# 핵심 장점

## 프라이버시 보호

- **양방향 가역 프라이버시 보호**: 민감 정보는 LLM에 전송되기 전에 플레이스홀더로 치환되고, 응답을 받은 후 자동으로 복원됩니다. 이 과정은 사용자에게 보이지 않습니다. 사용자가 보는 기록, 도구 인자, 최종 답변은 항상 원문이며, LLM이 보는 것은 `«PZ_PHONE_a3f8b2c1d4e5f6a7»`와 같은 **무작위로 추측 불가능한 플레이스홀더**입니다.
- **디스크 저장 시 전면 마스킹**: 세션 파일, 압축 트랜스크립트, 감사 로그는 디스크에 쓰기 전에 자동으로 마스킹됩니다(기본 활성화). 디스크에 평문 PII가 남지 않습니다.
- **인젝션 저항**: 플레이스홀더는 64비트 암호학적 무작위 토큰을 사용하여 열거, 위조, 재전송이 불가능합니다. 세션 전환 후 이전 플레이스홀더는 즉시 무효화됩니다.
- **다양한 프라이버시 보호 활성화 방법**: CLI에서 자연어 입력으로 활성화할 수 있으며, 더 정밀한 `/privacy` 명령도 지원합니다.
- **로컬 우선 agent**: 본 제품은 원격 데이터베이스가 없고 완전히 로컬에서 실행됩니다. 사용자 정보를 수집하지 않습니다.

# 기능

- **다중 백엔드 지원**: DeepSeek, 임의의 OpenAI 호환 인터페이스(GLM / Qwen / Kimi / OpenAI), 로컬 Ollama. 설정 하나로 전환 가능.

- **제로 설정 시작**: 최초 실행 시 설정 파일을 자동 생성합니다. 사용자는 API 키를 한 번만 입력하면 됩니다.

- **프라이버시 마스킹**: LLM에 전송하기 전에 **30+ 종류**의 민감 정보(휴대폰 번호, 이메일, 신분증, 여권, 은행 카드, 국제 번호, API Key, JWT, 데이터베이스 연결 문자열, MAC 주소 등)를 자동 식별하여 마스킹하고, 응답 후 자동 복원합니다. **디스크 저장 시에도 동일하게 마스킹**하여 디스크에 평문을 남기지 않습니다. 표준 / 엄격 2단계 모드를 지원하며, 자연어 또는 `/privacy` 명령으로 전환할 수 있습니다.

- **다국어 상호작용**: 중국어 / 영어 / 일본어 / 한국어 / 스페인어 / 프랑스어 / 독일어 / 러시아어 / 아랍어 9개 언어를 자유롭게 전환할 수 있습니다. `English`라고 말하거나 `/lang ja`를 사용하면 AI가 세션 전체에서 해당 언어로 사고하고 응답합니다.

- **완전한 도구 체인**: bash 실행, 파일 읽기/쓰기/편집, glob/grep 검색, 웹 검색 및 가져오기, 백그라운드 작업, 작업 및 할 일 관리.

- **스킬 시스템(Skills)**: 필요에 따라 도메인 지식(`SKILL.md`)을 로드하여 특정 시나리오에서 AI를 더 전문적으로 만듭니다.

- **서브에이전트(Subagents)**: 복잡한 작업을 독립 컨텍스트의 서브에이전트에 위임하여 메인 세션 오염을 방지합니다.

- **훅(Hooks)**: Python 또는 Shell 훅. 도구 호출 전후 가로채기, 감사 로그, 자동 포맷, 테스트 게이트를 지원합니다.

- **MCP 프로토콜**: Model Context Protocol을 통해 외부 도구 서버(GitHub, Filesystem 등)에 연결합니다.

- **컨텍스트 압축**: 2단계 압축(도구 결과 잘라내기 + LLM 요약)으로 초장문 대화를 지원합니다.

- **보안 샌드박스**: 명령 허용 목록, 경로 탈출 감지, 위험 명령 차단, 민감 파일 보호, 스크립트 인젝션 차단.

- **흑금 테마 CLI**: 중국어 폭 자동 조정, 코드 하이라이트, Diff 색상, 사고 접기.

# 백택 CLI 화면

<div align="center">
백택 CLI 시작 화면
</div>

<p align="center">
  <img src="image/clipage01.jpg" alt="백택 CLI 시작 화면" width="800" />
</p>

<div align="center">
백택 CLI 실행 화면 -- 01
</div>

<p align="center">
  <img src="image/clipage02.jpg" alt="백택 CLI 실행 화면" width="800" />
</p>

<div align="center">
백택 CLI 실행 화면 -- 02
</div>

<p align="center">
  <img src="image/clipage03.jpg" alt="백택 CLI 실행 화면" width="800" />
</p>

# 설치

## 사전 요구 사항

- Python 3.10+ (`tomllib` 필요. 3.11+는 내장, 3.10은 `tomli` 설치 필요)
- pip

## 소스에서 설치

### 다운로드 방법 두 가지

1. `pip install https://github.com/Xu123-Bob/Baize.git`

    bash -- Win+R을 누르고 `cmd`를 입력한 뒤 실행:

    baize

2. 저장소 페이지에서 `<> Code` --> `Download ZIP` 클릭.

(1) 압축 해제 후 해당 디렉터리로 이동:

    bash -- Win+R을 누르고 cmd 입력

    cd 압축을 푼 디렉터리

    pip install -r requirements.txt

    python -m Baize

설치 후 Win+R을 누르고 `cmd`를 입력해 CLI를 열고 `baize`를 입력하면 실행됩니다.

(2) ZIP을 다운로드하여 로컬 설치하는 경우, 압축 해제 후 디렉터리로 이동하여 실행:

    bash -- Win+R을 누르고 cmd 입력

    pip install .

설치 후 Win+R을 누르고 `cmd`를 입력해 CLI를 열고 `baize`를 입력하면 실행됩니다.

### 선택 사항: 데이터 연결 의존성 설치(데이터 분석에 중요)

백택이 SPSS 또는 SQL 데이터베이스를 구동하도록 하려면 추가 의존성을 설치합니다:

```bash
pip install -r requirements-data.txt
```

`requirements-data.txt`에는 다음이 포함됩니다:
- `spss-studio-mcp`: SPSS 통계 분석 MCP server(로컬에 IBM SPSS Statistics가 설치되어 있어야 함)
- `atengk-mcp-server-rdbms`: 범용 관계형 데이터베이스 MCP server(PostgreSQL / MySQL / SQL Server / Oracle / 达梦 등)
- `pyodbc`: SQL Server에 필요한 ODBC Python 바인딩

또는 프로젝트를 `pyproject.toml`로 설치한 경우 extras를 사용할 수도 있습니다:

```bash
pip install -e ".[data]"          # 데이터 연결 의존성 전체 설치
pip install -e ".[spss]"          # SPSS만
pip install -e ".[sql]"           # 범용 SQL만
pip install -e ".[sql-mssql]"     # SQL Server 전용(pyodbc 포함)
```

- **⚠️ SQL Server 사용자 주의: `pyodbc`는 Python 바인딩일 뿐입니다. 시스템 레벨에 Microsoft ODBC Driver 18 for SQL Server도 설치해야 합니다.**
- **⚠️ SPSS 사용자 주의: `spss-studio-mcp`는 MCP 브리지 계층일 뿐입니다. 로컬에 IBM SPSS Statistics(버전 20–31)가 설치되어 라이선스가 활성화되어 있어야 하며, 환경 변수 `SPSS_INSTALL_PATH`를 SPSS 설치 디렉터리로 지정해야 합니다. SPSS 엔진을 통한 완전한 분석 기능은 주로 Windows에서 지원됩니다. Linux/macOS에서는 "파일 모드"로 저하될 수 있습니다(`.sav` 파일 읽기, 메타데이터 조회, 데이터 미리보기는 가능하지만 통계 분석은 불가).**

# 빠른 시작

## LLM API 연결 실행

1. 최초 실행

```bash
baize
```

최초 실행 시 백택은 두 개의 설정 파일을 자동 생성합니다:

```
~/.baize/config.toml   # 백엔드 설정(DeepSeek / OpenAI / Ollama 선택)

~/.baize/.env          # 키 파일
```

Windows 경로는 `C:\Users\사용자이름\.baize\`입니다.

**2. 백엔드 선택**

`~/.baize/config.toml`을 열고 **active_provider**를 수정합니다(반드시 수정):

```toml
# 백택 설정 파일
# active_provider를 수정하여 백엔드 전환
# 선택 가능 값: "deepseek" / "qwen" / "kimi" / "glm" / "openai" / "ollama"

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
name = "Ollama (로컬)"
base_url = "http://localhost:11434/v1"
env_key = ""
model = "qwen2.5:7b"
```

**3. 키 입력**

`~/.baize/.env`를 편집합니다. **사용할 LLM이 있다면 해당 줄 앞의 `#`을 삭제하고, 다른 LLM 앞에 `#`을 추가하여 다른 LLM API 출력을 잠급니다. API Key를 입력한 후 반드시 저장하세요. 저장 후에만 유효합니다**:

```env
# ============================================================
# 백택 키 파일
# ============================================================
# 사용할 백엔드의 키만 입력하고 나머지는 주석으로 유지하세요.
# 변수 이름은 config.toml의 env_key 필드와 일치해야 합니다.
#
# 위치:
#   Linux / macOS: ~/.baize/.env
#   Windows:       C:\Users\사용자이름\.baize\.env
# ============================================================

# ---------- DeepSeek(기본 백엔드) ----------
# 발급: https://platform.deepseek.com/api_keys
DEEPSEEK_API_KEY=

# ---------- OpenAI 또는 임의의 OpenAI 호환 인터페이스(선택) ----------
# Groq, 通義, Moonshot, 智譜, OpenAI 등에 적용
# 참고: base_url은 config.toml의 [model_providers.xxx]에서 설정하며 여기서는 설정하지 않습니다
# OPENAI_API_KEY=

# ---------- 通義千問(선택) ----------
# 발급: https://dashscope.console.aliyun.com/
# DASHSCOPE_API_KEY=

# ---------- Kimi / Moonshot(선택) ----------
# 발급: https://platform.moonshot.cn/console/api-keys
# MOONSHOT_API_KEY=

# ---------- 智譜 GLM(선택) ----------
# 발급: https://open.bigmodel.cn/usercenter/apikeys
# ZHIPUAI_API_KEY=

# ---------- 사용자 지정 게이트웨이(선택) ----------
# CUSTOM_API_KEY=

# ---------- Ollama(로컬 모델, 키 불필요) ----------
# Ollama가 localhost:11434에서 실행 중이면 여기서 설정할 필요가 없습니다
```

4. 재시작

```bash
baize
```

흑금 로고와 환영 메시지가 보이면 시작 성공입니다.

## Ollama 로컬 모델(제로 비용)

클라우드 API를 사용하고 싶지 않다면 로컬 Ollama를 사용하세요:

    bash

    # 1. Ollama 설치: https://ollama.com/download
    # 2. 모델 가져오기
    ollama pull qwen2.5:7b

    # 3. Ollama 서비스 시작
    ollama serve

    # 4. ~/.baize/config.toml 수정
    active_provider = "ollama"

    # 5. 백택 시작
    baize

추천 모델: `qwen2.5:7b`(중국어 강함), `llama3.1:8b`, `deepseek-r1:7b`.

# 사용 예시

시작 후 `>>> 降旨：` 프롬프트에서 자연어로 요구 사항을 설명합니다:

```
>>> 降旨：Python으로 Douban Top250을 크롤링하는 스크립트를 작성하고 CSV로 저장하세요

>>> 降旨：src/ 아래 모든 Python 파일의 타입 오류를 확인하세요

>>> 降旨：이 저장소에서 requests를 사용하는 모든 곳을 찾아 httpx로 변경하세요
```

## 다국어 상호작용

백택은 **9개 언어**를 지원합니다: 중국어, English, 日本語, 한국어, Español, Français, deutsch, русский, العربية.

전환 방법은 두 가지입니다:

### 방법 1: 직접 말하기(자동 감지)

백택은 입력 언어를 자동 인식하여 전환합니다:

```
>>> 降旨：Hello, help me write a Python script
[시스템] 입력 언어를 English로 감지했습니다. 백택이 English 상호작용으로 전환했습니다.
(백택이 영어로 응답)

>>> 降旨：日本語で答えてください
[시스템] 입력 언어를 日本語로 감지했습니다. 백택이 日本語 상호작용으로 전환했습니다.
(백택이 일본어로 응답)
```

### 방법 2: 수동 명령

```
>>> 降旨：/lang                # 현재 언어 및 사용 가능 목록 보기
[시스템] 현재 언어: 中文 (zh)
[시스템] 사용 가능 언어:
    zh    中文 ←
    en    English
    ja    日本語
    ko    한국어
    es    Español
    fr    Français

>>> 降旨：/lang English        # 언어 이름으로 전환
>>> 降旨：/lang ja             # 언어 코드로 전환
>>> 降旨：/lang 西班牙语        # 중국어 이름도 가능
```

**언어 이름 / 언어 코드 / 중국어 이름 / 원어 이름** 네 가지를 지원합니다. 예를 들어 영어로 전환할 때 `English`, `en`, `英语`, `英文` 중 어느 것이든 가능합니다.

## 내장 명령

- `/exit`, `/quit` --> 백택 종료
- `/clear` --> 대화 기록, 할 일, 사고 기록, 도구 기록 지우기
- `/compact` --> 수동으로 컨텍스트 압축(대화가 너무 길 때 사용)
- `/commit` --> 현재 세션 저장 및 Git에 커밋(Git 저장소 내인 경우)
- `/lang` --> 현재 언어 보기; `/lang en`은 영어로 전환(언어 코드 또는 이름 지원)
- `/skills` --> 사용 가능한 모든 스킬 나열
- `/skills reload` --> 사용자 스킬 디렉터리 다시 로드
- `/unload` --> 현재 활성화된 스킬 언로드
- `/show thought` --> 전체 사고 기록 보기
- `/show tool` --> 도구 호출 기록 보기
- `/show all` --> 모든 세션 기록 보기
- `/스킬이름` --> 지정 스킬 로드(퍼지 매칭 지원)
- `/privacy` --> 프라이버시 마스킹 제어(`on / off / strict / status / rules / test / clear`)
- `/privacy rule-off <name>` --> 특정 마스킹 규칙 비활성화(예: `/privacy rule-off phone_intl`)
- `/privacy rule-on <name>` --> 규칙 다시 활성화

## 데이터 연결 사용 예시

SPSS / SQL을 설정한 후 자연어로 직접 구동할 수 있습니다:

```text
>>> 降旨：SPSS로 data.sav를 열고 변수 목록과 샘플 수를 알려주세요

>>> 降旨：data.sav에 대해 기술 통계를 실행한 후 선형 회귀를 실행하세요

>>> 降旨：sales 테이블에서 지난달 매출이 10만을 초과하는 주문을 고객별로 그룹화하여 조회하세요

>>> 降旨：SPSS 분석 결과를 CSV로 내보내고 SQL로 고객 마스터 데이터와 조인하세요
```

# 확장 메커니즘

백택은 네 가지 확장 방법을 지원합니다. 현재 작업 디렉터리에 배치하면 활성화됩니다.

## 스킬(Skills)

`./skills/스킬이름/SKILL.md`에 도메인 지식을 작성합니다. AI는 복잡한 작업을 만나면 자발적으로 로드합니다.

    markdown

    ---
    name: pandas-eda

    description: pandas를 이용한 탐색적 데이터 분석 모범 사례

    tags: data,python
    ---

    # Pandas EDA 가이드

    ## 핵심 단계
    1. df.info()로 필드 타입과 결측 확인
    2. df.describe()로 통계 기술
    ...

대화 중 `/pandas-eda`로 수동 로드할 수도 있습니다.

## 서브에이전트(Subagents)

`./subagent/역할이름/AGENT.md`에 전용 서브에이전트를 정의합니다. 메인 에이전트는 `agent` 도구로 작업을 위임할 수 있습니다.

    markdown

    ---
    name: code-reviewer

    description: 엄격한 코드 리뷰어
    ---

    당신은 시니어 코드 리뷰어입니다. 리뷰 시 다음을 우선합니다:
    1. 경계 조건과 예외 처리
    2. 리소스 누수
    3. 동시성 안전성
    ...

## 훅(Hooks)

`./hooks/` 아래에 `PreToolUse-*.sh`, `PostToolUse-*.sh`, `Stop-*.sh`를 배치합니다. JSON 입력을 받고 결정을 반환합니다:

```bash
#!/bin/bash
# PreToolUse-guard.sh
read -r input
if echo "$input" | grep -q "rm -rf"; then
  echo '{"hookSpecificOutput":{"permissionDecision":"block","permissionDecisionReason":"Deletion prohibited"}}'
fi
```

Python 훅은 내장 API를 직접 호출할 수 있습니다(`Baize.py`의 `hook_*` 함수 참조).

## MCP 서버

`./MCP/mcp_config.json`에서 외부 도구 서버를 설정합니다:

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

# 보안 설계(핵심)

백택은 기본적으로 다음 보안 메커니즘을 활성화합니다:

- **명령 허용 목록**: `ls`, `cat`, `grep`, `git`, `python3` 등 일반 명령만 허용.
- **경로 탈출 감지**: 모든 파일 작업을 현재 작업 디렉터리와 `/tmp` 내로 제한.
- **위험 명령 차단**: `rm -rf /`, fork bomb, `curl | sh`, `git push --force` 등 패턴 차단.
- **민감 파일 보호**: `.env`, `.ssh/`, `id_rsa`, `*.pem` 등 수정 금지.
- **스크립트 인젝션 차단**: `python -c "os.system(...)"` 같은 우회 감지.
- **프로세스 리소스 제한**: Linux/macOS에서 CPU, 메모리, 프로세스 수 제한.
- **프라이버시 마스킹(양방향 가역)**: 전송 시 PII를 무작위 플레이스홀더로 치환하고 수신 시 복원; 디스크 저장 시 독립적으로 마스킹.
- **플레이스홀더 인젝션 저항**: 64비트 암호학적 무작위 토큰 + 입력 측 중화 + 세션 격리.
- **감사 로그 마스킹**: `hook_audit_log`는 저장 전 마스킹하고, 잘라내며, 실패 시 쓰기를 거부합니다.

신뢰할 수 있는 프로젝트에서 제한을 완화해야 하는 경우 `Baize.py`의 `ALLOWED_COMMANDS`와 `FORBIDDEN_PATH_PATTERNS`를 수정할 수 있습니다.

# 프라이버시 마스킹(핵심)

백택에는 **양방향 가역 + 디스크 마스킹** 프라이버시 보호 메커니즘이 내장되어 입력부터 디스크까지 전체 경로를 커버합니다:

- **전송 시**: LLM에 보내기 전에 PII를 추측 불가능한 플레이스홀더로 치환.
- **수신 시**: LLM 응답 내 플레이스홀더를 원문으로 복원.
- **디스크 저장 시**: 세션 파일, 압축 트랜스크립트, 감사 로그를 저장 전에 **독립적으로 마스킹**. 디스크에 평문을 남기지 않음.

**기본적으로 비활성화**되어 있으며 필요할 때 활성화합니다.

## 활성화 방법 두 가지

### 방법 1: 자연어

대화에서 직접 말합니다:

```
>>> 降旨：프라이버시 마스킹 활성화
[시스템] 프라이버시 마스킹이 활성화되었습니다(표준 모드).

>>> 降旨：엄격 마스킹 활성화
[시스템] 프라이버시 마스킹이 활성화되었습니다(엄격 모드).

>>> 降旨：프라이버시 보호 비활성화
[시스템] 프라이버시 마스킹이 비활성화되었습니다.
```

### 방법 2: 슬래시 명령

- `/privacy on` 표준 모드 활성화
- `/privacy strict` 엄격 모드 활성화
- `/privacy off` 비활성화
- `/privacy status` 상태, 세션 ID, 규칙 수, LRU/TTL 통계 보기
- `/privacy rules` 모든 규칙(활성화 상태 포함) 나열
- `/privacy rule-off <name>` 특정 규칙 비활성화
- `/privacy rule-on <name>` 규칙 다시 활성화
- `/privacy test <텍스트>` 마스킹 효과 테스트
- `/privacy clear` 플레이스홀더 매핑을 지우고 **세션 ID 회전**

## 두 가지 모드

**표준**: 중국 본토 휴대폰 번호, 신분증 번호, 은행 카드 번호(Luhn 검사), 이메일, IPv4/IPv6, OpenAI/Anthropic/GitHub/AWS API Key, Bearer Token, 개인 키 블록, 비밀번호 필드, URL 자격 증명.

**엄격**: 표준 모드 전체 + 중국어 이름, QQ 번호, WeChat ID, 중국 본토 번호판 번호.

## 작동 방식

사용자 입력(실제 PII 포함) → messages는 원문 저장

↓ `sanitize_messages()`

LLM에 전송되는 것은 `[[PHONE_1]]`, `[[EMAIL_1]]`

↓ LLM 응답

반환된 플레이스홀더 → `restore_message()`

원문으로 복원 → 디스크 저장 / 표시 / 도구 실행

- **프라이버시 마스킹(양방향 가역)**: 전송 시 PII를 무작위 플레이스홀더로 치환하고 수신 시 복원; 디스크 저장 시 독립적으로 마스킹.
- **플레이스홀더 인젝션 저항**: 64비트 암호학적 무작위 토큰 + 입력 측 중화 + 세션 격리.
- **감사 로그 마스킹**: `hook_audit_log`는 저장 전 마스킹하고, 잘라내며, 실패 시 쓰기를 거부합니다.

## 도구 인자 지능형 등급

**마스킹됨**(순수 텍스트 인자로 실제 실행에 참여하지 않음):

- `todo`, `ask_user_question`, `task_create`, `task_update`

**마스킹되지 않음**(경로/명령/URL이 실제로 사용됨):

- `run_read` / `run_write` / `run_edit` / `run_glob` / `run_grep`(경로는 IO에 사용)
- `run_bash` / `background_run`(명령이 실행됨)
- `run_webfetch` / `web_search`(URL이 실제로 네트워크로 전송됨)
- `set_workspace`(경로는 `chdir`에 사용)
- `load_skills`(스킬 이름은 열거형)
- `agent`(서브에이전트 컨텍스트는 독립적으로 마스킹)
- `mcp_*`(의미를 알 수 없어 보수적으로 처리)

**디스크 저장 시 모두 마스킹**(디스크 내용은 재실행되지 않으므로 안전성 우선).

## 디스크 마스킹

**기본 활성화**되며 메모리 내 마스킹과 독립적입니다. `/privacy off`(메모리 내 마스킹 없음)여도 디스크 저장 시에는 최소한 표준 규칙을 적용합니다.

**주요 특징**:

- 디스크 마스킹은 **독립적이고 일회성인 매핑 테이블**을 사용합니다. 디스크에 기록된 플레이스홀더는 **복원할 수 없습니다**. 매핑 테이블이 폐기되기 때문입니다.
- 디스크 마스킹이 **실패하면 평문 쓰기를 거부**합니다(저하 없음, 조용히 건너뛰지 않음).
- 이전 버전 세션 파일에 평문이 포함된 경우 최초 저장 시 자동으로 마스킹하여 다시 씁니다.

**비활성화 방법**(권장하지 않음): `Baize.py`의 `PERSIST_REDACT_ENABLED = False`로 수정합니다.

## 예시

```
>>> 降旨：/privacy test 제 전화번호는 13812345678, 이메일은 a@b.com입니다
원문: 제 전화번호는 13812345678, 이메일은 a@b.com입니다
마스킹: 제 전화번호는 [[PHONE_1]], 이메일은 [[EMAIL_1]]입니다
복원: 제 전화번호는 13812345678, 이메일은 a@b.com입니다

>>> 降旨：/privacy status
[프라이버시 마스킹]
현재 모드 : 표준 모드 (standard)
세션 ID : 7d2f5e91
활성 규칙 수 : 34 / 41
활성 플레이스홀더 : 2
매핑 용량 : 2 / 2000
TTL : 86400초
LRU 제거 : 0
TTL 제거 : 0
마스킹 호출 횟수: 3
복원 호출 횟수: 3

>>> 降旨：/privacy rules
[프라이버시 마스킹 규칙 목록] 총 41개
【표준+엄격】
[✓] phone_cn 중국 본토 휴대폰 번호 (standard,strict)
[✓] id_card_cn 중국 본토 신분증 번호 (standard,strict)
[✓] jwt JWT Token (standard,strict)
...
【엄격 전용】
[✓] name_cn 중국어 이름 (strict)
[✓] address_cn 중국어 상세 주소 (strict)
...
사용법:
/privacy rule-off <name> 규칙 비활성화
/privacy rule-on <name> 규칙 다시 활성화
```

### 테스트 화면

<div align="center">
프라이버시 보호 테스트 화면 -- 01
</div>

<p align="center">
  <img src="image/privary01.jpg" alt="프라이버시 보호 테스트 화면" width="800" />
</p>

<div align="center">
프라이버시 보호 테스트 화면 -- 02
</div>

<p align="center">
  <img src="image/privary02.jpg" alt="프라이버시 보호 테스트 화면" width="800" />
</p>

# 데이터 연결(핵심)

백택은 **MCP(Model Context Protocol)** 를 통해 기업 데이터 분석 소프트웨어와 연결합니다. 메인 프로그램은 수정할 필요가 없으며 `MCP/mcp_config.json`에 server를 등록하기만 하면 됩니다.

## SPSS 연결

### 사전 조건

- 로컬에 IBM SPSS Statistics 설치(버전 20–31, Windows 권장)
- SPSS 라이선스가 활성화되어 정상 시작 가능

### 설정 단계

1. **SPSS 설치 디렉터리 확인**: 기본 경로는 보통 `C:\Program Files\IBM\SPSS Statistics\` 뒤에 버전 번호(예: `31`)가 붙습니다.

2. **환경 변수 설정**(`.env` 또는 시스템 환경 변수):

```text
SPSS_INSTALL_PATH=C:\Program Files\IBM\SPSS Statistics\31
```

3. **상태 확인**:

```bash
spss-studio-mcp status
```

예상 출력:

```text
=== SPSS MCP Capability Status ===
pyreadstat : OK v1.3.6
pandas     : OK v3.0.2
SPSS batch : OK
```

4. **`MCP/mcp_config.json`에 등록**:

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

### `SPSS batch: NOT FOUND`인 경우

`spss-studio-mcp`가 SPSS 엔진을 찾지 못했지만 `pyreadstat` + `pandas`는 정상이라는 뜻입니다. 이 경우 **파일 모드**로 진입합니다:

- `.sav` 읽기, 메타데이터 조회, 데이터 미리보기, CSV ↔ SAV 변환 가능
- 통계 분석(t 검정, 회귀, ANOVA 등) 실행 불가

해결 방법: `MCP/mcp_config.json`의 `SPSS_INSTALL_PATH`를 올바르게 설정하거나 파일 모드 저하를 수용합니다.

## SQL 연결

### 지원 데이터베이스

PostgreSQL, MySQL, MariaDB, SQL Server, Oracle, 达梦, 人大金仓, TiDB, OceanBase 등(SQLAlchemy 2.0 드라이버 기반).

### 설정 단계

1. **읽기 전용 데이터베이스 계정 준비**(강력 권장):

```sql
CREATE USER baize_ro WITH PASSWORD 'xxx';
GRANT SELECT ON ALL TABLES IN SCHEMA public TO baize_ro;
```

2. **연결 문자열 준비**:

- PostgreSQL --> `postgresql+psycopg://user:pwd@host:5432/db`
- MySQL --> `mysql+pymysql://user:pwd@host:3306/db`
- SQL Server --> `mssql+pyodbc://user:pwd@host:1433/db?driver=ODBC+Driver+18+for+SQL+Server`
- Oracle --> `oracle+oracledb://user:pwd@host:1521/?service_name=ORCL`

3. **`MCP/mcp_config.json`에 등록**:

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

### 내장 보안 가드레일

`atengk-mcp-server-rdbms`는 다층 보호를 제공합니다:

- **AST 레벨 SELECT 가드**: `sqlglot`로 구문 트리를 분석하여 `DELETE/UPDATE/DROP/TRUNCATE` 등 쓰기 작업을 물리적으로 차단.
- **자동 LIMIT 주입**: 행 수를 지정하지 않은 쿼리에 강제로 `LIMIT 100`을 추가하여 전체 테이블 조회로 인한 메모리 고갈 방지.
- **기본 읽기 전용**: 쓰기 작업은 `--allow-dml` / `--allow-ddl`로 명시적 허가 필요.
- **SQL 인젝션 차단**: AST 계층에서 문자열 연결로 구성된 악성 문장 거부.

### 여러 데이터베이스를 한 번에 설정

여러 데이터베이스에 동시에 연결하려면 여러 server를 등록할 수 있습니다:

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

백택은 이들의 모든 도구를 `MATERTOOLS`에 자동 통합하며, LLM이 작업에 따라 자동 선택합니다.

# 디렉터리 구조

```
    baize-agent/
    ├── pyproject.toml              # 패키징 설정
    ├── requirements-data.txt       # 데이터 연결 의존성(선택)
    ├── requirements-data           # 연결 의존성
    ├── README.md
    ├── tests/                      # 테스트(패키지에 포함되지 않음)
    |   ├── __init__.py
    |   ├── test_history.py
    |   └── test_skill_loader.py
    ├── .env.example                # 환경 변수 예시
    ├── .gitignore
    └── agent/                      # 메인 패키지
        ├── logo_*                  # 로그인 화면 로고
        ├── LOGO和启动交互界面       # 로그인 화면 로고 이미지
        ├── __init__.py             # 버전
        ├── Baize.py                # 메인 프로그램 및 Agent Loop
        ├── config.py               # 다중 백엔드 설정 로딩
        ├── ui_theme.py             # CLI 렌더링 테마
        ├── utils.py                # 범용 유틸리티
        ├── logo.txt
        ├── skills/                 # 내장 스킬
        ├── subagent/               # 내장 서브에이전트
        ├── core/                   # 핵심 로직(부작용 없음, 단위 테스트 가능)
        |   ├── __init__.py
        |   ├── history.py          # 세션 기록 정리 / token 추정 / 압축
        |   └── privacy.py          # 프라이버시 마스킹: PII 식별 / 플레이스홀더 치환 / 가역 복원
        ├── hooks/                  # 내장 훅
        └── MCP/                    # MCP 클라이언트 및 설정
            ├── __init__.py
            ├── mcp_client.py       # MCP 클라이언트
            └── mcp_config.json     # MCP 설정
```

# 환경 변수 참고

- 변수: `DEEPSEEK_API_KEY` — 설명: DeepSeek API 키 — 기본값: —(비밀)
- 변수: `DEEPSEEK_BASE_URL` — 설명: DeepSeek 엔드포인트 URL — 기본값: `https://api.deepseek.com`
- 변수: `OPENAI_API_KEY` — 설명: OpenAI 호환 API 키 — 기본값: —(비밀)
- 변수: `OPENAI_BASE_URL` — 설명: OpenAI 호환 엔드포인트 URL — 기본값: `https://api.openai.com/v1`
- 변수: `OLLAMA_BASE_URL` — 설명: Ollama 서비스 URL — 기본값: `http://localhost:11434`

**위 변수는 `~/.baize/.env`에 작성하면 되며, shell 설정 파일을 수정할 필요가 없습니다.**

- 데이터 분석 변수: `SPSS_INSTALL_PATH` — 설명: IBM SPSS Statistics 설치 디렉터리 — 기본값: —(설정하지 않으면 파일 모드로 저하)
- 데이터 분석 변수: `DATABASE_URL` — 설명: SQL MCP의 데이터베이스 연결 문자열 — 기본값: —(MCP server가 읽음)

**위 변수는 `MCP/mcp_config.json`에 작성합니다.**

# 개발

## 테스트 실행

본 프로젝트는 pytest를 사용합니다. 개발 전에 패키지와 개발 의존성을 편집 가능 모드로 설치하세요:

    pip install -e ".[dev]"

모든 테스트 실행:

    python -m pytest tests/ -v

단일 파일만:

    python -m pytest tests/test_history.py -v

## 코드 구조 규칙

- `agent/`: 패키지로 배포되는 메인 패키지. 모든 런타임 로직과 리소스(skills, subagent, hooks, MCP)가 여기에 있습니다.
- `agent/core/`: 외부 부작용이 없는 순수 로직 모듈. **반드시 단독으로 테스트 가능해야 합니다.** 이러한 새 로직은 여기에 두고 테스트를 함께 작성하세요.
- `tests/`: `agent/` 아래 소스 파일과 1:1 대응하며 `test_<모듈명>.py`로 명명합니다.
- 외부 의존성(네트워크, 디스크, 전역 상태)이 있는 함수는 테스트에서 교체할 수 있도록 인자를 통해 의존성을 주입하세요.

# ❓ FAQ

- Q: API 키는 어디에 입력하나요?

A: `~/.baize/.env`입니다. 프로젝트 루트의 `.env`가 아닙니다.

- Q: 백엔드를 변경하면 재설치해야 하나요?

A: 아니요. `~/.baize/config.toml`의 `active_provider`만 변경하면 됩니다.

- Q: 로컬 Ollama에 키가 필요한가요?

A: 아니요. `active_provider = "ollama"`를 선택하고 `env_key`를 비워 두면 됩니다.

- Q: 작업 디렉터리를 어떻게 전환하나요?

A: 대화에서 "/path/to/project로 전환"이라고 말하면 백택이 `set_workspace` 도구를 호출합니다.

- Q: 컨텍스트가 너무 길면 어떻게 되나요?

A: 백택은 자동으로 2단계 압축합니다. 먼저 이전 도구 결과를 잘라내고, 다음으로 LLM에 요약을 요청합니다. 수동으로 `/compact`를 사용할 수도 있습니다.

- Q: 실수로 파일을 삭제하지 않나요?

A: 기본 명령 허용 목록이 `rm -rf /` 등 위험 작업을 차단합니다. 파일 쓰기 전에는 Diff를 표시하고 확인을 요청합니다.

- Q: 백택을 SPSS에 연결하려면 어떻게 하나요?

A: 1. `pip install -r requirements-data.txt` 설치; 2. 환경 변수 `SPSS_INSTALL_PATH`를 SPSS 설치 디렉터리로 설정; 3. `MCP/mcp_config.json`에서 spss server 활성화. 자세한 내용은 "데이터 연결(SPSS / SQL)" 장을 참조하세요.

- Q: `SPSS batch: NOT FOUND`는 어떻게 하나요?

A: SPSS 엔진을 찾지 못했다는 뜻입니다. `SPSS_INSTALL_PATH`가 `stats.exe`가 포함된 디렉터리를 올바르게 가리키는지 확인하세요. `.sav` 파일만 처리한다면 이 경고를 무시해도 됩니다(파일 모드로 저하).

- Q: SQL 데이터베이스에 연결하려면 무엇을 추가로 설치해야 하나요?

A: Python 계층에서는 `atengk-mcp-server-rdbms`를 설치합니다(`pip install`로 자동 완료). **SQL Server 사용자는 시스템 계층에 Microsoft ODBC Driver 18도 설치해야 하며**, 이는 pip로 설치할 수 없습니다.

- Q: 백택이 데이터베이스 데이터를 실수로 삭제하지 않나요?

A: 아니요. SQL MCP는 기본적으로 SELECT만 허용하며 AST 구문 트리 레벨에서 모든 쓰기 작업을 차단합니다. 그래도 백택 전용 **읽기 전용 데이터베이스 계정**을 생성하는 것을 강력히 권장합니다.

- Q: SPSS 분석 결과의 데이터가 LLM에 유출되지 않나요?

A: 프라이버시 마스킹이 활성화된 경우(`/privacy on`), 도구 반환 결과는 LLM에 전송되기 전에 전화번호, 이메일, 신분증 등 PII가 자동으로 마스킹됩니다. **다만 읽기 전용 데이터베이스 계정 + 데이터 샘플링**(필요한 필드만 조회)도 함께 사용하여 위험을 낮추는 것을 권장합니다.

- Q: SPSS/SQL을 추가하면 백택의 매 대화가 느려지고 token도 늘어나는 이유는 무엇인가요?

A: MCP server가 노출하는 도구 정의가 매 턴 LLM에 전송되기 때문입니다. SPSS에는 60+ 도구가 있어 약 6,000–12,000 token의 고정 오버헤드가 추가됩니다. 자주 쓰는 워크플로에 SPSS가 포함되지 않는다면 해당 `enabled`를 `false`로 설정하고 필요할 때 활성화할 수 있습니다.

# 🤝 기여

Issue와 PR을 환영합니다. PR을 제출하기 전에 `CONTRIBUTOR.md`를 읽어 보시기 바랍니다.

**PR을 제출해 주시는 모든 Contributor께 감사드립니다.**

- GitHub Contributor:
[@anupamme](https://github.com/anupamme)
[@wangyipeng0724](https://github.com/wangyipeng0724)

[![Contributors](https://contrib.rocks/image?repo=Xu123-Bob/Baize&v=2)](https://github.com/Xu123-Bob/Baize/graphs/contributors)

# 라이선스

MIT License

# 감사의 글

- 본 프로젝트는 중국 AtomGit에서 호스팅됩니다: https://atomgit.com/Com_Xu/Baize
- AtomGit이 본 프로젝트를 G-star 인큐베이션 프로젝트로 선정해 주신 것에 감사드립니다.
- PR 기여자, Douyin 팔로워, 저를 팔로우해 주시는 학생 여러분께 감사드립니다.
- Claude Code, Codex 등 우수한 AI Coding 도구에서 영감을 받았습니다.
- DeepSeek, OpenAI SDK, MCP를 기반으로 구축되었습니다.
- Vibe Coding의 길을 함께 걷는 모든 개발자에게 감사드립니다.

# ☕ 후원

백택이 유용하다면 후원과 응원을 환영합니다. 개인 개발에도 많은 시간이 듭니다. 후원은 제품 업데이트 일정을 변경하지 않습니다. 지원해 주셔서 감사합니다!

<p align="center">
  <img src="image/support.jpg" alt="WeChat QR 코드" width="200" />
</p>

# 연락처

- 백택에 관심이 있거나 오픈소스 협력에 참여하고 싶다면 다음 방법으로 연락할 수 있습니다.
- **현재 구직 중입니다. 시장 조사와 사용자 리서치 경험이 있으며 Agent에 대해서도 어느 정도 이해하고 있습니다. 제 역량이 귀사의 요구에 부합한다면 함께 일하고 싶습니다(희망 직무: AI 제품 운영 / 사용자 리서치 / 마켓 리서치).**

<p align="center">
  <img src="image/weixin.jpg" alt="WeChat QR 코드" width="200" />
</p>

<p align="center">WeChat QR 코드를 스캔하고 "Baize 오픈소스 협력" 또는 "기업 채용"을 명시해 주세요.</p>

<p align="center">
  <img src="image/抖音.png" alt="Douyin QR 코드" width="200" />
</p>

<p align="center">Douyin QR 코드를 스캔하여 팔로우하세요.</p>