# Codex Operation Checklist

Codex must use this checklist before and after repository work.

## 1. Start

- Confirm repository root.
- Confirm branch.
- Confirm current commit.
- Confirm working tree status.
- List tracked files with `git ls-files`.
- Read `AGENTS.md` and task-relevant policy files.

## 2. Plan

- Identify requested outcome.
- Identify files that must change.
- Identify files that must not change.
- Choose the smallest safe change.
- Avoid unrelated refactors.

## 3. Edit

- Keep changes focused.
- Do not commit generated files, caches, virtual environments, build outputs, or nested clones unless explicitly required.
- Preserve existing style and language unless the task asks otherwise.
- Use clear file names and headings.

## 4. Verify

Run the most relevant available checks. Examples:

```bash
git diff --check
git status --short
```

When the project has tests, run the smallest relevant test first. If tests cannot be run, report why.

## 5. Report

Final report must include:

- status label: `완료`, `부분 완료`, `검수하지 못함`, or `차단됨`;
- changed files;
- commands/checks performed;
- checks not performed;
- risks or follow-up actions.

## 6. Stop conditions

Stop and ask for guidance before:

- deleting user data;
- changing authentication or production secrets;
- rewriting public history;
- making broad architectural changes unrelated to the task;
- exposing suspected credentials.
