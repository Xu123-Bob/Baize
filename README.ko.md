<div align="center">

<img src="image/logopage02.png" alt="백택 Baize 로고" width="320" />

# 백택 Baize

**만물을 통달하여, 당신의 직관적 프로그래밍을 함께합니다.**

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
  </a>
  
</p>

<p align="center">
  <a href="README.md">简体中文</a> |
  <a href="README.en.md">English</a> |
  <a href="README.ja.md">日本語</a> |
  <a href="README.ko.md">한국어</a> |
  <a href="README.es.md">Español</a> |
  <a href="README.fr.md">Français</a>
</p>

</div>

----------

백택(Baize) —— 고대 중국 신화에서 만물을 통달한 상서로운 짐승이 이제 Vibe Coding 어시스턴트로 환생했습니다.

**오픈소스 AI Coding Agent CLI로, Claude Code CLI의 대체품입니다. 다중 백엔드(DeepSeek / OpenAI 호환 / GLM / Qwen / Kimi / Ollama 로컬)를 지원하며, 도구 호출, 스킬 로딩, 서브에이전트 위임, 컨텍스트 압축, 보안 샌드박스 등 완전한 기능을 갖추고 있습니다. 터미널에서 바로 AI와 페어 프로그래밍을 즐기세요.**

----------


# 주요 기능

- **다중 백엔드 지원**: DeepSeek, 모든 OpenAI 호환 인터페이스(GLM / Qwen / Kimi / OpenAI), 로컬 Ollama, 원클릭 전환.

- **제로 설정 시작**: 첫 실행 시 자동으로 설정 파일을 생성하며, 사용자는 키만 한 번 입력하면 됩니다.

- **완전한 도구 체인**: bash 실행, 파일 읽기/쓰기/편집, glob/grep 검색, 웹 검색 및 크롤링, 백그라운드 작업, 작업 및 할 일 관리.

- **스킬 시스템(Skills)**: 필요 시 도메인 지식(SKILL.md)을 로드하여 특정 시나리오에서 AI가 더 전문적으로 동작합니다.

- **서브에이전트(Subagents)**: 복잡한 작업을 독립적인 컨텍스트의 서브에이전트에 위임하여 메인 세션 오염을 방지합니다.

- **훅(Hooks)**: Python 또는 Shell 훅으로 도구 호출 전후 가로채기, 감사 로그, 자동 포맷팅, 테스트 게이팅을 지원합니다.

- **MCP 프로토콜**: Model Context Protocol을 통해 외부 도구 서버(GitHub, Filesystem 등)에 연결합니다.

- **컨텍스트 압축**: 2단계 압축(도구 결과 자르기 + LLM 요약)으로 초장문 대화를 지원합니다.

- **보안 샌드박스**: 명령 화이트리스트, 경로 이탈 감지, 위험 명령 차단, 민감 파일 보호, 스크립트 주입 차단.

- **다국어 상호작용**: 중국어·영어·일본어·한국어·스페인어·프랑스어 자유 전환. `English`라고 말하거나 `/lang ja`만 입력하면 AI가 해당 언어로 사고하고 응답합니다.

- **블랙 골드 테마 CLI**: 중국어 폭 자동 조정, 코드 하이라이트, Diff 색상, 사고 접기.

# 설치

## 사전 요구 사항

- Python 3.10+ (tomllib 필요, 3.11+ 내장; 3.10은 tomli 설치 필요)

- pip

## 소스에서 설치
### 다운로드 방법 두 가지
1. pip install https://github.com/Xu123-Bob/Baize.git

bash --win+R 입력 후 cmd

    baize

2. <>Code --> Download ZIP

(1) 압축 해제 후 본 파일 디렉토리로 이동:

bash --win+R 입력 후 cmd

    cd 압축해제한_디렉토리 # 본 파일 디렉토리에서 이미 win+R로 cmd를 열었다면 이 단계는 불필요

    pip install -r requirements.txt    

    python -m Baize             

다운로드 완료 후 win+R로 cmd를 열고 CLI 인터페이스에서 baize를 입력하면 실행됩니다.

(2) ZIP 다운로드 후 로컬 설치, 압축 해제 후 디렉토리로 이동하여 실행:

bash --win+R 입력 후 cmd

    pip install .

다운로드 완료 후 win+R로 cmd를 열고 CLI 인터페이스에서 baize를 입력하면 실행됩니다.

# 빠른 시작
1. 첫 실행

bash

    baize

첫 실행 시 백택은 자동으로 두 개의 설정 파일을 생성합니다:

text

    ~/.baize/config.toml   # 백엔드 설정 (DeepSeek / OpenAI / Ollama 선택)

    ~/.baize/.env          # 키 파일>

Windows 사용자 경로는 C:\Users\사용자이름\.baize\ 입니다.


2. 백엔드 선택

~/.baize/config.toml을 열고 active_provider를 수정하세요:

toml

    active_provider = "deepseek"    # 또는 "openai" / "ollama"

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
    name = "Ollama (로컬)"
    base_url = "http://localhost:11434/v1"
    env_key = ""
    model = "qwen2.5:7b">


3. 키 입력

~/.baize/.env 편집:

env

    #DeepSeek 백엔드 필수

    DEEPSEEK_API_KEY=sk-당신의_키


    #OpenAI 호환 인터페이스 필수(GLM / Qwen / Kimi / OpenAI)

    #OPENAI_API_KEY=당신의_키

    #Ollama 로컬은 키 불필요


4. 재시작

bash

    baize

블랙 골드 로고와 환영 메시지가 보이면 시작 성공입니다.


# 사용 예시

시작 후 >>> 降旨: 프롬프트에서 자연어로 요구사항을 설명하면 됩니다:

text

    >>>降旨：Python으로 더우반 Top250을 크롤링하는 스크립트를 작성하고 CSV로 저장해줘

    >>>降旨：src/ 아래 모든 Python 파일의 타입 오류를 확인해줘

    >>>降旨：이 저장소에서 requests를 사용하는 모든 곳을 찾아 httpx로 바꿔줘

## 다국어 상호작용

백택은 **6개 언어**를 지원합니다: 中文, English, 日本語, 한국어, Español, Français.

전환 방법 두 가지:

### 방법 1: 그냥 말하기 (자동 감지)

입력 언어를 자동으로 감지해 전환합니다:

```
>>> 降旨：안녕, Python 스크립트 하나 써 줘
[system] 입력 언어를 한국어로 감지했습니다. 백택이 한국어로 전환합니다.
(한국어로 응답)

>>> 降旨：Hello, write me a script
[system] 입력 언어를 English로 감지했습니다. 백택이 English로 전환합니다.
(영어로 응답)
```

### 방법 2: 수동 명령

```
>>> 降旨：/lang                # 현재 언어와 목록 확인
[system] 현재 언어: 한국어 (ko)
[system] 사용 가능한 언어:
    zh    中文
    en    English
    ja    日本語
    ko    한국어 ←
    es    Español
    fr    Français

>>> 降旨：/lang English        # 언어명으로 전환
>>> 降旨：/lang ja             # 언어 코드로 전환
>>> 降旨：/lang 西班牙语        # 중국어 이름도 가능
```

**언어명 / 언어 코드 / 현지 표기 / 중국어 표기** 모두 지원합니다. 예를 들어 영어로 전환하려면 `English`, `en`, `英语`, `英文` 중 아무거나 입력하면 됩니다.


## 백택 CLI 인터페이스
<div align="center">
백택 CLI 시작 화면
</div>

<p align="center">
  <img src="image/clipage01.jpg" alt="백택 CLI 시작 화면" width="800" />
</p>

<div align="center">
백택 CLI 실행 화면
</div>

<p align="center">
  <img src="image/clipage02.jpg" alt="백택 CLI 실행 화면" width="800" />
</p>


## 내장 명령어
- /exit, /quit --> 백택 종료
- /clear	--> 대화 기록, 할 일, 사고 기록, 도구 기록 지우기
- /compact	--> 수동 컨텍스트 압축 (대화가 너무 길 때 사용)
- /commit	--> 현재 세션 저장 및 Git에 커밋 (Git 저장소 내부인 경우)
- /lang → 현재 언어 표시; /lang en은 영어로 전환 (코드 또는 이름 허용)
- /skills	--> 사용 가능한 모든 스킬 나열
- /skills reload	--> 사용자 스킬 디렉토리 다시 로드
- /unload	--> 현재 활성화된 스킬 언로드
- /show thought	--> 전체 사고 기록 보기
- /show tool	--> 도구 호출 기록 보기
- /show all	--> 전체 세션 기록 보기
- /스킬명	--> 지정된 스킬 로드 (퍼지 매칭 지원)


# Ollama 로컬 모델 (제로 비용)

클라우드 API를 사용하고 싶지 않으신가요? 로컬 Ollama를 사용해 보세요:

bash

    #1. Ollama 설치: https://ollama.com/download
    #2. 모델 다운로드
    ollama pull qwen2.5:7b

    #3. Ollama 서비스 시작
    ollama serve

    #4. ~/.baize/config.toml 수정
    active_provider = "ollama"

    #5. 백택 시작
    baize

추천 모델: qwen2.5:7b (중국어 우수), llama3.1:8b, deepseek-r1:7b.


# 확장 메커니즘

백택은 네 가지 확장 방식을 지원하며, 모두 현재 작업 디렉토리에 배치하면 적용됩니다.

## 스킬(Skills)
./skills/스킬명/SKILL.md에 도메인 지식을 작성하면, AI가 복잡한 작업을 만났을 때 자동으로 로드합니다.

markdown

    ---
    name: pandas-eda

    description: pandas를 사용한 탐색적 데이터 분석 모범 사례

    tags: data,python
    ---

    #Pandas EDA 가이드

    ##핵심 단계
    1. df.info()로 필드 타입과 결측 확인
    2. df.describe() 통계 설명
    ...
    대화 중 /pandas-eda로 수동 로드할 수도 있습니다.


## 서브에이전트(Subagents)

./subagent/역할명/AGENT.md에 전용 서브에이전트를 정의하면, 메인 에이전트가 agent 도구로 작업을 위임할 수 있습니다.

markdown

    ---
    name: code-reviewer

    description: 엄격한 코드 리뷰어
    ---

    당신은 시니어 코드 리뷰어입니다. 리뷰 시 우선 관심사:
    1. 경계 조건과 예외 처리
    2. 리소스 누수
    3. 동시성 안전
    ...


## 훅(Hooks)

./hooks/ 아래에 
- PreToolUse-*.sh
- PostToolUse-*.sh
- Stop-*.sh
를 배치하면 JSON 입력을 받아 결정을 반환합니다:

bash

    #!/bin/bash

    #PreToolUse-guard.sh

    read -r input

    if echo "$input" | grep -q "rm -rf"; then

    echo '{"hookSpecificOutput":{"permissionDecision":"block","permissionDecisionReason":"삭제 금지"}}'

    fi

Python 훅은 내장 API를 직접 호출할 수 있습니다 (Baize.py의 hook_* 함수 참조).


## MCP 서버

./MCP/mcp_config.json에 외부 도구 서버를 설정:

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


# 보안 설계

백택은 기본적으로 다음 보안 메커니즘을 활성화합니다:

- **명령 화이트리스트**: ls, cat, grep, git, python3 등 일반 명령만 허용.

- **경로 이탈 감지**: 모든 파일 작업은 현재 작업 디렉토리와 /tmp 내로 제한.

- **위험 명령 차단**: rm -rf /, fork bomb, curl | sh, git push --force 등 패턴 차단.

- **민감 파일 보호**: .env, .ssh/, id_rsa, *.pem 등 수정 금지.

- **스크립트 주입 차단**: python -c "os.system(...)" 같은 우회 감지.

- **프로세스 리소스 제한**: Linux/macOS에서 CPU, 메모리, 프로세스 수 제한.

신뢰할 수 있는 프로젝트에서 제한을 완화하려면 Baize.py의 ALLOWED_COMMANDS와 FORBIDDEN_PATH_PATTERNS를 수정하세요.


# 디렉토리 구조
text

    baize-agent/
    ├── pyproject.toml              # 패키징 설정
    ├── README.md
    ├── tests/                      # 테스트 (패키지에 미포함)
    |   ├── __init__.py
    |   ├── test_history.py
    |   └── test_skill_loader.py 
    ├── .env.example                # 환경 변수 예시
    ├── .gitignore
    └── agent/                      # 메인 패키지
        ├── __init__.py
        ├── Baize.py                # 메인 프로그램 및 Agent Loop
        ├── config.py               # 다중 백엔드 설정 로딩
        ├── ui_theme.py             # CLI 렌더링 테마
        ├── utils.py                # 공통 유틸리티
        ├── logo.txt
        ├── skills/                 # 내장 스킬
        ├── subagent/               # 내장 서브에이전트
        ├── core/                   # 핵심 로직 (부작용 없음, 단위 테스트 가능)
        |   ├── __init__.py
        |   └── history.py          # 세션 기록 정리 / 토큰 추정 / 압축
        ├── hooks/                  # 내장 훅
        └── MCP/                    # MCP 클라이언트 및 설정
            ├── __init__.py
            ├── mcp_client.py
            └── mcp_config.json


# 환경 변수 참고
		
- 변수: DEEPSEEK_API_KEY  설명: DeepSeek API  기본값: 키	—

- 변수: DEEPSEEK_BASE_URL  설명: DeepSeek 인터페이스 주소  기본값: https://api.deepseek.com

- 변수: OPENAI_API_KEY  설명: OpenAI  기본값: 호환 인터페이스 키	—

- 변수: OPENAI_BASE_URL	 설명: OpenAI 호환 인터페이스 주소	 기본값: https://api.openai.com/v1

- 변수: OLLAMA_BASE_URL	 설명: Ollama 서비스 주소	 기본값: http://localhost:11434

변수는 ~/.baize/.env에 작성하면 되며, shell 설정 파일을 수정할 필요가 없습니다.


# 개발

## 테스트 실행

본 프로젝트는 pytest를 사용합니다. 개발 전 편집 가능 모드로 패키지와 개발 의존성을 설치하세요:

    pip install -e ".[dev]"

전체 테스트 실행:

    python -m pytest tests/ -v

단일 파일만 실행:

    python -m pytest tests/test_history.py -v

## 코드 구조 규칙

- `agent/`: 패키지와 함께 배포되는 메인 패키지. 모든 런타임 로직과 리소스(skills, subagent, hooks, MCP)가 여기에 있습니다.
- `agent/core/`: 순수 로직 모듈, 외부 부작용 없음, **반드시 개별 테스트 가능해야 함**. 이러한 로직을 추가할 때는 여기에 배치하고 테스트를 함께 작성하세요.
- `tests/`: `agent/` 아래 소스 파일과 일대일 대응, `test_<모듈명>.py`로 명명.
- 외부 의존성(네트워크, 디스크, 전역 상태)이 있는 함수는 매개변수로 의존성을 주입하여 테스트에서 대체 가능하게 하세요.

# ❓ 자주 묻는 질문
- Q: 키는 어디에 입력하나요?

A: ~/.baize/.env이며, 프로젝트 루트의 .env가 아닙니다.

- Q: 백엔드를 바꾸려면 재설치해야 하나요?

A: 아닙니다. ~/.baize/config.toml의 active_provider만 변경하면 됩니다.

- Q: 로컬 Ollama는 키가 필요한가요?

A: 필요 없습니다. active_provider = "ollama"로 설정하고 env_key는 비워두세요.

- Q: 작업 디렉토리를 어떻게 바꾸나요?

A: 대화에서 "switch to /path/to/project"라고 말하면 백택이 set_workspace 도구를 호출합니다.

- Q: 컨텍스트가 너무 길어지면 어떻게 되나요?

A: 백택은 자동으로 2단계 압축합니다: 먼저 오래된 도구 결과를 자르고, 그 다음 LLM에 요약을 요청합니다. 수동으로 /compact도 가능합니다.

- Q: 제 파일을 실수로 삭제하나요?

A: 기본 명령 화이트리스트가 rm -rf / 같은 위험 작업을 차단하며, 파일 쓰기 전 Diff를 표시하고 확인을 요청합니다.

# 🤝 기여
Issue와 PR을 환영합니다. 먼저 Baize.py의 agent_loop 함수를 읽고 Agent 메인 루프를 이해한 후 확장하는 것을 권장합니다.
### PR을 제출해 주신 모든 기여자에게 감사드립니다
- Github Contributor：
[@anupamme](https://github.com/anupamme)
[@wangyipeng0724](https://github.com/wangyipeng0724)

[![Contributors](https://contrib.rocks/image?repo=Xu123-Bob/Baize&v=2)](https://github.com/Xu123-Bob/Baize/graphs/contributors)

# 라이선스
MIT License

# 감사의 글
- 본 프로젝트는 중국 내 AtomGit에 호스팅되어 있습니다. 프로젝트 링크: https://atomgit.com/Com_Xu/Baize

- AtomGit이 본 프로젝트를 G-star 인큐베이션 프로젝트로 선정해 주신 것에 감사드립니다

- PR 기여자, 더우인 팬, 저를 팔로우하는 학생들에게 감사드립니다

- Claude Code, Codex 등 우수한 AI Coding 도구에서 영감을 받았습니다

- DeepSeek, OpenAI SDK, MCP를 기반으로 구축되었습니다

- Vibe Coding 여정을 함께하는 모든 개발자에게 감사드립니다

- 개발자는 창의성과 의사결정에 집중하고, 백택은 잡무와 실행을 처리합니다. 프로그래밍을 직관으로 되돌리고, 창조를 신화처럼 유려하게 만드세요.

# ☕ 후원
백택이 유용하다면 후원을 환영합니다. 독립 개발에도 많은 시간이 소요됩니다. 후원은 제품 업데이트 일정을 바꾸지 않습니다. 감사합니다!
<p align="center">
  <img src="image/support.jpg" alt="위챗 QR코드" width="200" />
</p>

# 연락처
- 백택에 관심이 있거나 오픈소스 협업에 참여하고 싶으시다면 다음 방법으로 연락해 주세요
- **현재 구직 중입니다. 저는 시장 조사와 사용자 리서치 업무를 수행해 왔으며 Agent에 대해서도 어느 정도 이해하고 있습니다. 제 역량이 귀사의 요구에 부합한다면 함께 일하고 싶습니다 (희망 직무: AI 제품 운영 / 사용자 리서치 / 시장 조사)**

<p align="center">
  <img src="image/weixin.jpg" alt="위챗 QR코드" width="200" />
</p>

<p align="center">위챗 스캔, Baize 오픈소스 협업 또는 기업 채용 명시</p>

<p align="center">
  <img src="image/抖音.png" alt="더우인 QR코드" width="200" />
</p>

<p align="center">더우인 스캔 팔로우</p>