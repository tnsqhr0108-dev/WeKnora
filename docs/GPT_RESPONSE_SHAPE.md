# GPT 답변 형상 적용 문서

이 문서는 WeKnora 저장소 전체에서 사용할 GPT/Codex/AI 에이전트 답변 형상을 설명한다.

## 적용 대상

- 저장소 루트 전체
- 모든 하위 디렉터리와 파일
- 코드 리뷰, 오류 해결, 배포 안내, 문서 작성, CLI 사용 안내

## 답변 형상

```text
핵심 결론
적용한 내용
실행 방법
검증 방법
남은 작업
```

## 사용 규칙

1. 한국어 요청에는 한국어로 답한다.
2. 실제 확인한 내용과 추정 내용을 분리한다.
3. 터미널 명령은 복사/붙여넣기 가능한 단일 코드 블록으로 제공한다.
4. 저장소 작업은 브랜치, 변경 파일, 커밋 SHA 또는 PR 번호를 포함한다.
5. 완료하지 못한 항목은 이유와 다음 조치를 적는다.
6. 시크릿, 토큰, 비밀번호, 쿠키는 출력하거나 커밋하지 않는다.

## 동기화 파일

동일한 규칙은 아래 파일에도 적용되어 있다.

- `AGENTS.md`
- `.github/copilot-instructions.md`
- `.cursor/rules/gpt-response-shape.mdc`

## 검증 명령

```bash
gh api repos/tnsqhr0108-dev/WeKnora/contents/AGENTS.md --jq '.name + " / " + .sha'
gh api repos/tnsqhr0108-dev/WeKnora/contents/.github/copilot-instructions.md --jq '.name + " / " + .sha'
gh api repos/tnsqhr0108-dev/WeKnora/contents/docs/GPT_RESPONSE_SHAPE.md --jq '.name + " / " + .sha'
gh api repos/tnsqhr0108-dev/WeKnora/contents/.cursor/rules/gpt-response-shape.mdc --jq '.name + " / " + .sha'
```
