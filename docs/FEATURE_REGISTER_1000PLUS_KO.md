# 1000+ 기능 레지스터

- 총 항목 수: 1200
- 생성 기준: `scripts/generate_feature_register_1000plus.py`
- 목적: Codex가 RAG, GAN 루프, 하니스, 다중 에이전트, 감점표, MCP, PDF 검증, Android Debian, GitHub 운영 기능을 놓치지 않게 하는 기준표.

## 핵심 기능군

1. 저장소/브랜치
2. PDF
3. Codex
4. RAG
5. 오케스트레이션
6. GAN루프
7. 다중에이전트
8. 하니스
9. 감점표
10. MCP
11. 보안
12. 모바일
13. 인수인계

## 대표 항목

| ID | 분류 | 기능 | 상태 | 설명 |
|---:|---|---|---|---|
| F0001 | 저장소 | 브랜치확인 | 운영규칙 | 실제 파일, 로그, 명령 출력, MCP 조회 결과 중 하나로 확인한다. |
| F0002 | PDF | 소스검증 | 대기 | PDF 4개 업로드와 검증 전에는 완료라고 말하지 않는다. |
| F0003 | Codex | 답변품질 | 운영규칙 | AGENTS.md와 CODEX_ANSWER_QUALITY_POLICY.md를 우선 적용한다. |
| F0004 | RAG | 문서검색 | 예정 | 원본, 파싱, 청킹, 임베딩, 검색, 근거 표시를 포함한다. |
| F0005 | 오케스트레이션 | 도구순서 | 예정 | GitHub MCP, Context7, RAG, Playwright 순서를 관리한다. |
| F0006 | GAN루프 | 생성비판수정 | 예정 | Generator, Critic, Refiner, Judge, Evidence Checker를 포함한다. |
| F0007 | 다중에이전트 | 역할분리 | 예정 | Planner, Research, GitHub, RAG, Coder, Reviewer, Security, Tester, Docs, Ops Agent를 포함한다. |
| F0008 | 하니스 | 자동검사 | 예정 | Prompt, RAG, Codex, CLI, PDF, MCP, UI, Regression, Security, Handoff Harness를 포함한다. |
| F0009 | 감점표 | 품질점수 | 예정 | 근거 없음, 완료 과장, 명령 오류, 보안 위험, 누락을 감점한다. |
| F0010 | MCP | 연결확인 | 대기 | GitHub, Context7, Google Drive, Notion, Airtable, Playwright, Filesystem, WeKnora MCP를 구분한다. |
| F1000 | 전체 | 1000번째 기능 기준선 | 예정 | 1000개 이상 기능이 존재함을 검증하는 기준 항목이다. |
| F1200 | 전체 | 1200번째 기능 기준선 | 예정 | 생성기 기본 항목 수의 마지막 기준 항목이다. |

## 생성/검증 명령

```bash
python3 scripts/generate_feature_register_1000plus.py --check
grep -n '총 항목 수' docs/FEATURE_REGISTER_1000PLUS_KO.md
grep -n 'F1000' docs/FEATURE_REGISTER_1000PLUS_KO.md
```

## 중요한 원칙

- 이 파일은 기능 기억 기준이다.
- 완료 증거는 실제 파일, 로그, 테스트, PDF, QA JSON, MCP 결과, health report로 따로 확인해야 한다.
- 대응 증거가 없으면 RAG, GAN 루프, 하니스, 다중 에이전트, 감점표는 `예정`으로 보고한다.
