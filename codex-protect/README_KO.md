# Codex Protect 컨텍스트 폴더

이 폴더는 Codex Protect 또는 Codex 작업 컨텍스트에 등록하기 위한 기준 폴더다.

## 목적

- Codex가 답변할 때 흩어진 정책, 로드맵, 기능표를 놓치지 않게 한다.
- `AGENTS.md`와 `docs/CODEX_ANSWER_QUALITY_POLICY.md`만 읽고 끝내지 말고, 1000+ 기능 로더와 RAG, GAN, 하니스, MCP 규칙까지 따라가게 한다.
- 실제 완료된 것, 대기 중인 것, 예정 기능을 혼동하지 않게 한다.

## 등록 권장 폴더

```text
codex-protect/
docs/
scripts/
AGENTS.md
```

## 주의

- 이 폴더는 시크릿 저장소가 아니다.
- API 키, 토큰, 비밀번호, 쿠키를 넣지 않는다.
- 1000+ 기능 레지스터는 기능 기억용이며, 실제 완료 여부는 파일, 로그, 테스트로 검증해야 한다.
