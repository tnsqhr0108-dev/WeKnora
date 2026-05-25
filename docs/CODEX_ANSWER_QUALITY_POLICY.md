# Codex Answer Quality Policy

Repository: `tnsqhr0108-dev/WeKnora`
Primary branch: `main`

## Actual application rule

This policy applies when a Codex task is opened with this repository and branch selected.
Connected repositories are not automatically injected into every Codex answer; if another repository is needed, Codex must explicitly fetch or inspect it and cite the evidence.

## Required pre-answer checks

Before claiming status, editing files, or saying a task is complete, run or inspect:

```bash
pwd
git branch --show-current
git rev-parse HEAD
git status --short
find . -maxdepth 3 -type f | sort
```

## Answer quality rules

- Answer from repository files, command output, and generated artifacts only.
- Do not guess branch names, file names, test results, generated outputs, or completion status.
- If a file, log, test, or artifact does not exist, say it does not exist.
- If a check was not run, report `검수하지 못함` rather than passing it.
- Keep user-facing answers in Korean unless the user asks otherwise.
- Prefer small, reversible, verifiable commits.
- Do not commit nested repositories, `.venv`, caches, build artifacts, or temporary files unless explicitly requested.

## Completion rule

A task is complete only when the expected changed files, logs, generated outputs, or test results actually exist in the repository.
