# Codex Answer Quality Policy

This policy is mandatory for Codex and AI agents working in this repository.

## Quality target

A 10/10 answer is:

- grounded in inspected repository files, commands, logs, or test results;
- explicit about what was checked and what was not checked;
- safe with secrets and destructive actions;
- useful for beginners without hiding uncertainty;
- concise enough to act on, but detailed enough to reproduce.

## Mandatory preflight

Before finalizing a technical answer or committing a change, verify the repository context:

```bash
pwd
git branch --show-current
git rev-parse HEAD
git status --short
git ls-files | sort | sed -n '1,240p'
```

For generated files, also check the exact output path. For tests, include the test command and whether it passed, failed, or was not run.

## Required policy files

Read and apply these files when relevant:

- `AGENTS.md`
- `docs/CODEX_OPERATION_CHECKLIST_KO.md`
- `docs/MCP_SECURITY_CHECKLIST_KO.md`
- `docs/RAG_ORCHESTRATION_GAN_HARNESS_ROADMAP_KO.md`
- `docs/CODEX_1000PLUS_FEATURE_LOADER_KO.md`
- `docs/FEATURE_REGISTER_1000PLUS_KO.md`

If one is missing, say `검수하지 못함: <path>` and continue with the best safe answer.

## Evidence hierarchy

Use this priority order:

1. Actual command output from the current repository.
2. Current repository files read during the task.
3. Current GitHub MCP/API results for this repository.
4. Clearly marked inference.
5. General knowledge, only when repository evidence is unnecessary.

Never promote inference to fact.

## Answer structure

For repository tasks, final answers should include:

1. **결론**: 완료, 부분 완료, 차단됨, or 검수하지 못함.
2. **확인한 근거**: files, commands, branches, commits, tests, or logs.
3. **변경 사항**: changed files and why.
4. **검증 결과**: tests/checks run and their result.
5. **남은 위험**: anything not checked or not possible to verify.

## Forbidden answer patterns

Do not say:

- "완료했습니다" when no artifact was verified.
- "테스트 통과" when tests were not run.
- "문제 없습니다" when only a partial inspection was done.
- "아마", "대충", "보통" without labeling it as inference.
- file names, branch names, or logs that were not inspected.

## Required uncertainty labels

Use these labels exactly:

- `확인됨`: directly inspected and verified.
- `추론`: likely based on evidence, but not directly verified.
- `검수하지 못함`: not checked, unavailable, or blocked.
- `주의`: risk that may need user or maintainer review.

## Completion checklist

Before reporting completion, confirm:

- expected files exist;
- changed files are intentional;
- no obvious generated/cache files are included;
- tests or validation commands were run when available;
- skipped checks are named;
- secret exposure risk was considered.

## Secret handling

Never reveal or commit secrets. Do not quote suspected credentials. If secret scanning or manual inspection finds sensitive material, report only the file/path and remediation steps.

## Beginner mode

When the user appears to be a beginner, include:

- the exact next command or action;
- a short explanation of why it matters;
- no unexplained jargon.
