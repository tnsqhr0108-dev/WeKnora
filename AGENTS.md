# AGENTS.md

## 목적

이 파일은 이 저장소에서 작업하는 Codex와 AI 에이전트의 필수 운영 규칙을 정의한다. 모든 답변은 근거 기반, 재현 가능, 초보자 친화, 보안 우선이어야 한다.

## 규칙 우선순위

1. 시스템, 개발자, 사용자 지시를 가장 먼저 따른다.
2. 저장소 전체 규칙은 이 `AGENTS.md`를 따른다.
3. 답변 품질, 검증, 보고 방식은 `docs/CODEX_ANSWER_QUALITY_POLICY.md`를 따른다.
4. 작업 성격에 맞는 `docs/` 하위 정책 문서를 함께 따른다.
5. 규칙이 겹치면 더 엄격한 규칙을 따른다.
6. 참조 문서가 없거나 읽을 수 없으면 `검수하지 못함: <path>`로 보고하고, 읽은 척하지 않는다.

## 필수 시작 체크

파일을 수정하거나 기술 결론을 내리기 전에 다음과 동등한 확인을 수행한다.

```bash
pwd
git branch --show-current
git rev-parse HEAD
git status --short
git ls-files | sort | sed -n '1,240p'
```

기본 파일 목록 확인은 `git ls-files`를 사용한다. 미추적 파일, 생성물, 임시 파일 확인이 필요한 경우에만 `find`를 보조로 사용한다.

원격 MCP 환경처럼 터미널 실행이 불가능한 경우에는 GitHub MCP/API로 브랜치, HEAD, 파일 목록, 파일 내용을 확인하고 `검수하지 못함: 로컬 터미널 명령 직접 실행`이라고 명시한다.

## 필수 메모리 파일

Codex, MCP, 자동화, RAG, 저장소 정책, 답변 품질과 관련된 작업에서는 다음 파일을 읽는다.

- `docs/CODEX_ANSWER_QUALITY_POLICY.md`
- `docs/CODEX_OPERATION_CHECKLIST_KO.md`
- `docs/MCP_SECURITY_CHECKLIST_KO.md`
- `docs/RAG_ORCHESTRATION_GAN_HARNESS_ROADMAP_KO.md`
- `docs/CODEX_1000PLUS_FEATURE_LOADER_KO.md`
- `docs/FEATURE_REGISTER_1000PLUS_KO.md`
- `docs/CODEX_TASK_PROMPT_TEMPLATE_KO.md`

## 증거 기반 답변 규칙

실제로 확인하지 않은 코드, 테스트, 파일, 브랜치, 빌드, 로그, 배포 상태를 사실처럼 말하지 않는다. 답변에는 확인한 파일 경로, 명령, 테스트 이름, 출력 요약 중 최소 하나를 포함한다.

## 완료 판정 규칙

예상 산출물이 존재하고 관련 검증이 통과했을 때만 완료라고 말한다. 검증이 생략, 차단, 불가한 경우 다음 라벨 중 하나를 사용한다.

- `완료`
- `부분 완료`
- `검수하지 못함`
- `차단됨`

## 보안 규칙

민감한 인증 정보나 운영 접근 정보를 출력, 커밋, 요청하지 않는다. 그런 값이 있을 가능성이 있으면 값을 반복하지 말고 파일/경로와 조치만 보고한다.

## 언어 규칙

사용자가 다른 언어를 요청하지 않으면 사용자 대상 설명은 한국어로 작성한다. 초보자 대상 답변은 구체적 단계와 이유를 함께 제공한다.
