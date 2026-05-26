# Codex 컨텍스트 로드 순서

Codex가 이 저장소에서 답변하거나 수정할 때 아래 순서로 읽는다.

1. `codex-protect/README_KO.md`
2. `codex-protect/ANSWER_PLAYBOOK_KO.md`
3. `AGENTS.md`
4. `docs/CODEX_ANSWER_QUALITY_POLICY.md`
5. `docs/CODEX_1000PLUS_FEATURE_LOADER_KO.md`
6. `scripts/generate_feature_register_1000plus.py`
7. `docs/FEATURE_REGISTER_1000PLUS_KO.md`가 있으면 읽고, 없으면 생성 대상으로 보고한다.

## 필수 원칙

- 실제 파일, 로그, 테스트가 없으면 완료라고 말하지 않는다.
- RAG, GAN 루프, 하니스, 다중 에이전트, 감점표는 대응 파일, 로그, 테스트가 있을 때만 완료로 표시한다.
- 1000+ 기능 레지스터는 기능 기억 기준이며 완료 증거가 아니다.
- GitHub Actions 실패는 과거 실패와 현재 새 실패를 분리해서 판단한다.
