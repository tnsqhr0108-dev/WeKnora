# AI Agent Response Quality Guide

This guide defines the response shape for AI assistants working on this repository.

## Standard Shape

For repository, terminal, deployment, debugging, and setup tasks, answer in this order:

1. 핵심 결론
2. 적용한 내용
3. 실행 방법
4. 검증 방법
5. 남은 작업

Use fewer sections for very simple questions.

## Work Rules

- Use Korean when the user writes in Korean.
- State the target repository, branch, changed files, and commit SHA when a change is made.
- Keep commands copy-paste-ready.
- Separate verified results from assumptions.
- Say what could not be checked instead of guessing.
- For Android Debian or mobile terminal users, provide one pasteable command block when possible.
- For code changes, keep the diff small and explain the verification command.

## Runtime Prompt

The structured runtime answer template is stored at:

- `config/prompt_templates/gpt_answer_shape.yaml`

To use it as the default knowledge-base answer prompt, configure:

```yaml
conversation:
  summary:
    prompt_id: "structured_korean_kb"
```

Restart the app container or redeploy the service after changing the config.
