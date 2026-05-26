# Codex Answer Quality Policy

Repository: `tnsqhr0108-dev/prompts.chat`
Primary branch: `main`

## Actual application rule

This policy applies when a Codex task is opened with this repository and branch selected. Connected repositories are not automatically injected into every Codex answer; if another repository is needed, Codex must explicitly fetch or inspect it and cite the evidence.

## Required pre-answer checks

Before claiming status, editing files, or saying a task is complete, run or inspect:

```bash
pwd
git branch --show-current
git rev-parse HEAD
git status --short
find . -maxdepth 3 -type f | sort
```

If the user asks about roadmap, features, GAN loops, harnesses, MCP, RAG, orchestration, multi-agent, scoring rubrics, or handoff, also run or inspect:

```bash
python3 scripts/generate_feature_register_1000plus.py --check || true
sed -n '1,220p' docs/CODEX_1000PLUS_FEATURE_LOADER_KO.md
```

## Mandatory project memory files

Read and apply these files when they exist:

- `docs/CODEX_1000PLUS_FEATURE_LOADER_KO.md`
- `docs/FEATURE_REGISTER_1000PLUS_KO.md`
- `docs/RAG_ORCHESTRATION_GAN_HARNESS_ROADMAP_KO.md`
- `docs/MCP_SECURITY_CHECKLIST_KO.md`
- `docs/CODEX_OPERATION_CHECKLIST_KO.md`

If a listed file does not exist, report it as `검수하지 못함`; do not pretend it was read.

## Response shape for user-facing answers

For repository, terminal, deployment, debugging, setup, MCP, RAG, orchestration, feature planning, and handoff tasks, answer in this order:

```text
핵심 결론
적용한 내용
실행 방법
검증 방법
남은 작업
```

Do not force all five sections for a very small question. If the user is a beginner or using Android Debian, prefer one copy-paste-ready command block and explain only what each major step does.

## Evidence and verification rules

- Answer from repository files, command output, generated artifacts, MCP results, and logs only.
- Do not guess branch names, file names, test results, generated outputs, PDF source status, or completion status.
- If a file, log, test, PDF, image, or artifact does not exist, say it does not exist.
- If a check was not run, report `검수하지 못함` rather than passing it.
- If a command fails, include the important error line and the next corrective command.
- If a change is committed, report the commit SHA and changed files.
- If a task depends on a server, secret, browser login, PDF upload, Git LFS, or external account, say exactly what the user must do.
- Treat RAG, orchestration, GAN loop, harness, multi-agent, and scoring-rubric items as `예정` unless matching code, logs, tests, or docs exist.

## Answer quality rules

- Keep user-facing answers in Korean unless the user asks otherwise.
- Prefer small, reversible, verifiable commits.
- Prefer the safest path for beginners over the shortest path.
- Do not commit nested repositories, `.venv`, caches, build artifacts, or temporary files unless explicitly requested.
- Do not print or commit tokens, API keys, cookies, passwords, or private credentials.
- Avoid saying `완료` until verification is complete.
- When referring to the 1000+ feature set, cite the generated feature register and use feature IDs when available.

## Completion rule

A task is complete only when the expected changed files, logs, generated outputs, tests, PDFs, rendered images, QA JSON, MCP results, or health reports actually exist in the repository.
