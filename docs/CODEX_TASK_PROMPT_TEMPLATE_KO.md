# Codex 작업 프롬프트 템플릿

아래 명령문을 Codex에 붙여 넣으면 저장소 문제 탐지, 수정, 검증, 보고를 한 번에 수행하도록 지시할 수 있다.

## 표준 명령문

```text
이 저장소에서 작업하기 전에 AGENTS.md와 다음 문서를 모두 읽고 적용해.

- docs/CODEX_ANSWER_QUALITY_POLICY.md
- docs/CODEX_OPERATION_CHECKLIST_KO.md
- docs/MCP_SECURITY_CHECKLIST_KO.md
- docs/RAG_ORCHESTRATION_GAN_HARNESS_ROADMAP_KO.md
- docs/CODEX_1000PLUS_FEATURE_LOADER_KO.md
- docs/FEATURE_REGISTER_1000PLUS_KO.md
- docs/CODEX_TASK_PROMPT_TEMPLATE_KO.md

먼저 아래 명령으로 현재 상태를 확인해.

pwd
git branch --show-current
git rev-parse HEAD
git status --short
git ls-files | sort | sed -n '1,240p'

그 다음 저장소 전체에서 다음 문제를 찾아서 해결해.

1. 문서에서 참조하는 파일 경로가 실제로 존재하지 않는 문제
2. KO 파일인데 본문이 영어로 되어 있거나 언어가 섞여 초보자가 이해하기 어려운 문제
3. 테스트를 실행하지 않았는데 통과했다고 말하게 만들 수 있는 지시
4. 검증하지 않은 결과를 완료로 보고하게 만들 수 있는 지시
5. MCP, API, 커넥터, 민감 정보 처리와 관련된 보안 누락
6. 캐시, 빌드 산출물, 가상환경, 중첩 clone 저장소가 커밋될 위험
7. RAG, 오케스트레이션, 하네스, 자동화 기능을 실제 구현 없이 구현된 것처럼 오해하게 만드는 표현
8. 초보자가 바로 실행할 수 없는 모호한 명령문
9. AGENTS.md와 docs/ 정책 문서 사이의 우선순위 충돌
10. 최종 답변에 상태 라벨, 변경 파일, 검증 결과, 미검수 항목이 빠지는 문제

수정은 가장 작은 안전한 범위로 해. 요청과 무관한 리팩터링은 하지 마.

수정 후 가능한 검증을 실행해.

- git diff --check
- git status --short
- 관련 테스트가 있으면 가장 작은 관련 테스트

테스트나 검증을 실행할 수 없으면 이유를 `검수하지 못함`으로 적어.

최종 답변은 반드시 한국어로 쓰고, 아래 형식을 지켜.

결론: 완료 / 부분 완료 / 차단됨 / 검수하지 못함
확인한 근거:
변경 사항:
검증 결과:
검수하지 못한 항목:
남은 위험 또는 다음 조치:

확인하지 않은 파일, 브랜치, 테스트, 로그, 배포 상태를 사실처럼 말하지 마. 민감 정보는 절대 출력하지 마.
```

## 짧은 명령문

```text
AGENTS.md와 docs/CODEX_ANSWER_QUALITY_POLICY.md를 먼저 읽고, 관련 정책 문서를 모두 적용해. 저장소의 문서/정책/보안/검증 지시 문제를 전부 찾아 최소 범위로 고친 뒤, git diff --check와 가능한 관련 테스트로 검증해. 최종 답변은 한국어로 `결론`, `확인한 근거`, `변경 사항`, `검증 결과`, `검수하지 못한 항목`, `남은 위험` 형식으로 보고해. 확인하지 않은 것은 반드시 `검수하지 못함`으로 표시하고, 민감 정보는 출력하지 마.
```
