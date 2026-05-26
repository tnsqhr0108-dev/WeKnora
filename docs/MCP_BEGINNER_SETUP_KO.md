# MCP 초보자 연결 가이드

이 문서는 WeKnora 저장소에서 MCP를 처음 연결하는 사용자를 위한 안내서다.

## MCP를 쉽게 말하면

MCP는 AI에게 도구를 꽂아 주는 방식이다. 예를 들어 AI가 GitHub를 읽고, 로컬 파일을 보고, 웹 화면을 테스트하고, 최신 라이브러리 문서를 찾아볼 수 있게 해준다.

## 먼저 연결하면 좋은 MCP 4개

### 1. WeKnora MCP

용도: WeKnora 지식베이스와 문서를 AI 도구에서 직접 검색하고 다루기 위한 연결.

언제 유용한가:
- WeKnora에 올린 문서를 AI가 찾아보게 할 때
- 지식베이스 기반 답변을 만들 때
- WeKnora API를 AI 도구에서 쓰고 싶을 때

기본 설정 예시:

```json
{
  "mcpServers": {
    "weknora": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/WeKnora/mcp-server",
        "run",
        "run_server.py"
      ],
      "env": {
        "WEKNORA_BASE_URL": "http://localhost:8080/api/v1",
        "WEKNORA_API_KEY": "put-your-api-key-here"
      }
    }
  }
}
```

주의: WeKnora 앱을 실제로 실행 중이어야 한다. 서버나 PC에서 WeKnora가 켜져 있지 않으면 연결만 해도 답변을 가져올 곳이 없다.

### 2. GitHub MCP

용도: AI가 GitHub 저장소, 이슈, PR, Actions 상태를 더 잘 읽고 관리하게 하는 연결.

언제 유용한가:
- 저장소 구조를 파악할 때
- 이슈/PR을 만들거나 정리할 때
- Actions 실패 원인을 볼 때
- Codex나 Copilot이 GitHub 작업을 더 정확히 하게 하고 싶을 때

추천 방식:
- 초보자는 원격 GitHub MCP 또는 VS Code/Copilot 내장 연결을 우선 사용한다.
- 토큰을 직접 파일에 저장하지 않는다.

### 3. Filesystem MCP

용도: AI가 내 컴퓨터의 지정된 폴더 안 파일만 읽고 쓰게 하는 연결.

언제 유용한가:
- 로컬 프로젝트 폴더를 AI에게 보여줄 때
- 폰 Debian이나 PC의 작업 폴더를 제한적으로 열어줄 때
- GitHub에 올리기 전 파일을 점검할 때

초보자 원칙:
- 전체 홈 폴더를 열지 말고 프로젝트 폴더 하나만 허용한다.
- 예: `~/work/WeKnora`만 허용한다.

설정 예시:

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/home/droid/work/WeKnora"
      ]
    }
  }
}
```

### 4. Playwright MCP

용도: AI가 웹 브라우저를 열어 화면을 확인하고 버튼을 눌러 테스트하게 하는 연결.

언제 유용한가:
- WeKnora 웹 UI가 잘 뜨는지 확인할 때
- 로그인/업로드/검색 화면을 테스트할 때
- 화면 오류를 재현할 때

설정 예시:

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": [
        "@playwright/mcp@latest"
      ]
    }
  }
}
```

## 선택 후보: Context7 MCP

Context7은 최신 라이브러리 문서를 AI에게 찾아 주는 도구다. 코딩 질문이 많아지면 GitHub MCP나 Playwright MCP 다음으로 연결하면 좋다.

## Android Debian 사용자의 현실적인 순서

1. 지금은 GitHub CLI와 GitHub 저장소 정리부터 한다.
2. PC나 서버가 생기면 WeKnora 앱을 Docker로 실행한다.
3. 그 다음 WeKnora MCP를 연결한다.
4. 로컬 프로젝트를 많이 다루면 Filesystem MCP를 연결한다.
5. 웹 UI 테스트가 필요하면 Playwright MCP를 연결한다.

## 보안 주의

- API 키나 토큰은 GitHub에 커밋하지 않는다.
- MCP 서버는 필요한 것만 켠다.
- Filesystem MCP는 꼭 허용 폴더를 제한한다.
- 모르는 MCP 서버는 바로 설치하지 말고 공식 저장소와 문서를 확인한다.

## 확인 체크리스트

- MCP 클라이언트가 무엇인지 정했다. 예: Cursor, Claude Desktop, VS Code, Codex CLI
- Node.js 또는 uv가 설치되어 있다.
- WeKnora 앱을 실제로 실행할 PC나 서버가 있는지 확인했다.
- 토큰과 API 키를 안전하게 보관했다.
