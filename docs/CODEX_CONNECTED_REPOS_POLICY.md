# Codex Connected Repositories Policy

## Scope

This repository is one of the user's Codex-ready repositories.

Connected repositories:

| Repository | Branch | Status |
|---|---|---|
| `tnsqhr0108-dev/WeKnora` | `main` | Codex policy applied |
| `tnsqhr0108-dev/math-masterbook` | `Main` | Codex policy applied |
| `tnsqhr0108-dev/system_prompts_leaks` | `main` | Codex policy applied |
| `tnsqhr0108-dev/prompts.chat` | `main` | Codex policy applied |

Excluded repository:

| Repository | Branch | Status |
|---|---|---|
| `tnsqhr0108-dev/AutoGPT` | `master` | excluded unless the user explicitly asks |

## Practical rule

Codex does not automatically load every connected repository into every workspace.
When the task is about this repository, apply this repository's local files first:

- `AGENTS.md`
- `docs/CODEX_CLOUD_RUNBOOK.md`
- `docs/CODEX_ANSWER_QUALITY_POLICY.md`
- `docs/CODEX_CONNECTED_REPOS_POLICY.md`

When the user asks about all connected repositories, inspect each repository directly and report evidence per repository.
Do not claim global application without checking the target repositories.

## No false completion

A repository is treated as applied only if the expected policy files exist on the expected branch.
