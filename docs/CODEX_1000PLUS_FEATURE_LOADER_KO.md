# Codex 1000+ 기능 로더

이 문서는 Codex가 답변할 때 프로젝트 전체 기능을 빠뜨리지 않게 하기 위한 로더다.

## 반드시 기억할 점

- 지금 프로젝트는 단순한 프롬프트 수정이 아니다.
- 범위는 `math-masterbook`, `WeKnora`, `prompts.chat`, `system_prompts_leaks` 네 저장소를 포함한다.
- 핵심 기능군은 RAG, 오케스트레이션, GAN 자기검증 루프, 다중 에이전트, 하니스, 감점표, MCP, PDF 검증, Android Debian 모바일 워크플로, GitHub 운영 자동화다.
- 1000개 이상 기능은 `scripts/generate_feature_register_1000plus.py`로 생성되는 `docs/FEATURE_REGISTER_1000PLUS_KO.md`를 기준으로 관리한다.

## Codex가 작업 시작 시 해야 할 일

```bash
pwd
git branch --show-current
git rev-parse HEAD
git status --short
find . -maxdepth 3 -type f | sort
python3 scripts/generate_feature_register_1000plus.py --check || true
```

## 답변 시 적용 규칙

1. 사용자가 기능, 로드맵, 인수인계, RAG, GAN, 하니스, MCP, 다중 에이전트를 물으면 먼저 이 문서를 기준으로 분류한다.
2. 완료/대기/예정/운영규칙을 섞지 않는다.
3. 저장소에 없는 파일이나 실행하지 않은 테스트는 완료라고 말하지 않는다.
4. 다른 연결 저장소가 필요하면 직접 inspect/fetch하고 근거를 남긴다.
5. 초보자에게는 한 번에 붙여넣을 수 있는 명령을 제공한다.

## 네 저장소 역할

- `math-masterbook`: PDF 4개 소스 검증, 수능수학 마스터북 생성, PDF QA, 15회 GAN 루프, 모바일 QA, 시그마 조판 QA.
- `WeKnora`: RAG/Agent/Wiki/런타임 GPT 답변 형상, `structured_korean_kb`, MCP와 지식베이스 연계.
- `prompts.chat`: 프롬프트, 1000+ 기능 레지스터, Codex 작업 템플릿, MCP 문서, 감점표/하니스 설계의 중심 저장소.
- `system_prompts_leaks`: 시스템 프롬프트 연구/비교/품질 분석용 저장소. 민감정보나 비공개 시스템 프롬프트를 무단 저장하지 않는다.

## 12대 핵심 기능군

1. 저장소/브랜치/커밋 운영
2. math-masterbook PDF 소스 검증
3. Codex/GPT 답변 품질
4. WeKnora RAG와 런타임 답변 형상
5. 오케스트레이션
6. GAN 스타일 자기검증 루프
7. 다중 에이전트
8. 하니스
9. 감점표
10. MCP/앱 연결
11. 보안/관측/운영
12. 모바일/초보자 UX와 인수인계
