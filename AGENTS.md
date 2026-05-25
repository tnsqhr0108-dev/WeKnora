# AGENTS.md

Repository: `tnsqhr0108-dev/WeKnora`
Primary branch: `main`

## Mandatory startup checks

Before answering, editing, claiming status, or saying a task is complete, inspect or run:

```bash
pwd
git branch --show-current
git rev-parse HEAD
git status --short
find . -maxdepth 3 -type f | sort
```

Also read and apply these repository policy files when they exist:

- `docs/CODEX_CLOUD_RUNBOOK.md`
- `docs/CODEX_ANSWER_QUALITY_POLICY.md`

## Actual application rule

These rules apply when the Codex task is opened with repository `tnsqhr0108-dev/WeKnora` and branch `main` selected.
If another repository is needed, inspect that repository directly and cite the evidence.

## Answer quality rules

- 실제 저장소 파일과 터미널 결과를 기준으로 답변한다.
- 브랜치명, 파일명, 출력물, 로그, 완료 여부를 추측하지 않는다.
- 예상 파일, 로그, 테스트 결과, 산출물이 실제로 존재하지 않으면 완료라고 말하지 않는다.
- 검사하지 않은 항목은 통과가 아니라 `검수하지 못함`으로 보고한다.
- 중첩 clone 저장소, `.venv`, 캐시, 임시파일은 커밋하지 않는다.
- 큰 변경보다 작고 검증 가능한 변경을 우선한다.
- 사용자에게 설명할 때는 기본적으로 한국어로 답변한다.

## Completion rule

A task is complete only when the expected changed files, logs, generated outputs, or test results actually exist in this repository.
