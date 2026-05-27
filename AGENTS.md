# AGENTS.md

## Purpose

This file defines mandatory operating rules for Codex and AI agents working in this repository. The goal is to make every answer evidence-based, reproducible, and safe for beginners.

## Rule priority

1. Follow system, developer, and user instructions first.
2. Follow this `AGENTS.md` for repository-level behavior.
3. Follow `docs/CODEX_ANSWER_QUALITY_POLICY.md` for answer quality, verification, and reporting.
4. Follow supporting policy files under `docs/` when they apply.
5. If rules overlap, follow the stricter rule.
6. If a referenced file is missing or unreadable, report it as `검수하지 못함` and do not pretend it was applied.

## Mandatory startup check

Before changing files or giving a final technical conclusion, run or otherwise verify the equivalent of:

```bash
pwd
git branch --show-current
git rev-parse HEAD
git status --short
git ls-files | sort | sed -n '1,240p'
```

Use `git ls-files` as the default repository inventory source. Use `find` only as a supplemental check when untracked files or generated outputs matter.

## Required memory files

Read these files when the task involves Codex, MCP, automation, RAG, repository policy, or answer quality:

- `docs/CODEX_ANSWER_QUALITY_POLICY.md`
- `docs/CODEX_OPERATION_CHECKLIST_KO.md`
- `docs/MCP_SECURITY_CHECKLIST_KO.md`
- `docs/RAG_ORCHESTRATION_GAN_HARNESS_ROADMAP_KO.md`
- `docs/CODEX_1000PLUS_FEATURE_LOADER_KO.md`
- `docs/FEATURE_REGISTER_1000PLUS_KO.md`

If any file is not present, say exactly which one was not checked.

## Evidence-first answer rule

Do not claim that code, tests, files, branches, builds, logs, or deployments exist unless they were actually inspected. Mention the evidence used, such as file paths, commands, test names, or output summaries.

## Completion rule

Only say a task is complete when all expected artifacts exist and the relevant checks have passed. If checks were skipped, blocked, or unavailable, use one of these labels:

- `완료`
- `부분 완료`
- `검수하지 못함`
- `차단됨`

## Safety rule

Never print, commit, or ask users to expose secrets such as API keys, tokens, cookies, passwords, private keys, or production credentials. If a secret may be present, stop and request rotation/removal guidance without repeating the secret.

## Language rule

Default to Korean for user-facing explanations unless the user asks for another language. Keep beginner-facing answers concrete, step-by-step, and based on the repository state.
