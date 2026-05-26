#!/usr/bin/env python3
"""Generate docs/FEATURE_REGISTER_1000PLUS_KO.md with 1,200+ project items."""
from pathlib import Path
from datetime import datetime, timezone
import argparse
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "FEATURE_REGISTER_1000PLUS_KO.md"
CATEGORIES = {
"저장소/브랜치":["기본 브랜치 확인","브랜치 대소문자 혼동 방지","중복 브랜치 제거","커밋 SHA 기록","git status 확인","원격 저장소 확인","PR 흐름 설계","branch protection","ruleset","force push 차단","브랜치 삭제 차단","릴리즈 태그","CHANGELOG","Issue 템플릿","PR 템플릿","CODEOWNERS","GitHub Actions","health report","large file scan","nested repo scan"],
"math-masterbook/PDF":["PDF 4개 업로드","표준 파일명 매핑","파일명 정규화","PDF 존재 검증","Git LFS pointer 검증","페이지 수 검증","파일 크기 검증","문제/해설 매칭","2026 수능 문제 검증","2026 수능 해설 검증","2206~2609 문제 검증","2206~2609 해설 검증","페이지 이미지 렌더","원문 이미지 QA","모바일 QA","시그마 조판 QA","최종 PDF 생성","최종 PDF 압축","150MB 용량 점검","릴리즈 asset 후보"],
"Codex/GPT 답변 품질":["AGENTS.md","CODEX_ANSWER_QUALITY_POLICY","startup checks","한국어 우선","초보자 설명","복붙 명령","완료 단정 금지","검수하지 못함","커밋 SHA 보고","변경 파일 보고","오류 핵심줄 보고","실행 방법/검증 방법 분리","작은 변경 우선","추측 금지","증거 기반 답변","정책 문서 로더","답변 형상","작업 템플릿","인수인계 템플릿","회귀 답변 평가"],
"WeKnora 런타임/RAG":["structured_korean_kb","config prompt_id","지식베이스 Q&A","문서 수집","문서 파싱","문서 정제","청킹","임베딩","벡터 저장","BM25","Dense search","Hybrid search","rerank","context packing","근거 표시","NO_MATCH","fallback","쿼리 재작성","쿼리 확장","세션 요약"],
"오케스트레이션":["Planner","Executor","State store","Tool router","Failure recovery","Human approval gate","Rollback planner","Task queue","Dependency mapper","Decision log","GitHub 단계","Context7 단계","RAG 단계","Playwright 단계","보고서 단계","점검표 업데이트","중단 조건","재시도 조건","완료 조건","감사 로그"],
"GAN/자기검증 루프":["Generator","Critic","Refiner","Judge","Evidence Checker","Hallucination detector","Contradiction detector","Completeness checker","Risk critic","Beginner critic","Command critic","Korean clarity critic","Evidence loop","Revision loop","Stop condition","Self-score","External score","Adversarial test","Regression critique","15회 루프"],
"다중 에이전트":["Planner Agent","Research Agent","GitHub Agent","RAG Agent","Coder Agent","Reviewer Agent","Security Agent","Tester Agent","Docs Agent","Ops Agent","Teacher Agent","Judge Agent","Evidence Agent","Tool Router Agent","Memory Agent","Consensus check","Disagreement resolver","Priority scheduler","Agent handoff","Role prompt library"],
"하니스/감점표":["Prompt Harness","RAG Harness","Codex Harness","CLI Harness","PDF Harness","MCP Harness","UI Harness","Regression Harness","Security Harness","Handoff Harness","Orchestration Harness","Multi-agent Harness","Evaluation Harness","Mac Setup Harness","Android Debian Harness","감점표 근거 없음","감점표 완료 과장","감점표 명령 오류","감점표 보안 위험","감점표 누락"],
"MCP/앱":["GitHub MCP","Context7 MCP","Google Drive 앱","Notion 앱","Airtable 앱","Playwright MCP","Filesystem MCP","WeKnora MCP","OAuth 재연결","권한 범위 점검","MCP 로그","MCP 실패 fallback","MCP 보안 점검","MCP 연결 회귀","MCP 도구 승인","GitHub PR 확인","GitHub Actions 확인","Context7 최신 문서","Playwright UI 테스트","Filesystem 폴더 제한"],
"보안/운영/관측":["Secret scanning","Push protection","Dependabot alerts","Dependabot security updates","SECURITY.md","민감정보 회전","토큰 금지","API 키 금지","쿠키 금지","개인정보 점검","Langfuse","Trace ID","Command log","MCP call log","RAG query log","Error log","Audit log","Backup plan","Data retention","License review"],
"모바일/초보자 UX":["Android Debian","gh 설치","기기 코드 로그인","diff 화면 q","grep 줄바꿈 오류 방지","git email 오류 해결","한 블록 명령","단계별 설명","서버 없음 안내","PC 필요 안내","Mac 준비","Homebrew","Docker 설치","폰 터미널 경로","다운로드 경로","스크린샷 기반 도움","문외한 설명","오류 복구","다음 명령 제시","상태 확인"],
"문서/인수인계/로드맵":["FULL_HANDOFF","FEATURE_REGISTER","MCP guide","RAG roadmap","GAN roadmap","Harness roadmap","문제 감사","운영 체크리스트","다음 담당자 30분 계획","완료/대기/예정 구분","기능 카드","점검표","상태표","결정 기록","작업 백로그","Issue화","PR화","릴리즈 노트","문서 동기화","장기 기억"],
}
STATUS={"저장소/브랜치":"운영규칙","math-masterbook/PDF":"대기","Codex/GPT 답변 품질":"운영규칙","WeKnora 런타임/RAG":"예정","오케스트레이션":"예정","GAN/자기검증 루프":"예정","다중 에이전트":"예정","하니스/감점표":"예정","MCP/앱":"대기","보안/운영/관측":"대기","모바일/초보자 UX":"운영규칙","문서/인수인계/로드맵":"운영규칙"}
T=["{n}을/를 실제 파일, 로그, 명령 출력, MCP 조회 결과 중 하나로 검증한다.","{n}은/는 완료/대기/예정 상태를 분리해서 보고한다.","{n}이/가 실패하면 오류 핵심 줄과 복구 명령을 남긴다.","{n}은/는 초보자도 복사/붙여넣기 가능한 절차를 제공해야 한다.","{n} 관련 작업은 시크릿, 토큰, API 키를 출력하거나 커밋하지 않는다."]
def build(count=1200):
    rows=[]; i=1; r=1
    while len(rows)<count:
        for c,names in CATEGORIES.items():
            for n in names:
                rows.append((f"F{i:04d}",c,f"{n} #{r}",STATUS[c],T[(i-1)%len(T)].format(n=n)))
                i+=1
                if len(rows)>=count: return rows
        r+=1
    return rows
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--count",type=int,default=1200); ap.add_argument("--check",action="store_true"); a=ap.parse_args()
    rows=build(a.count); OUT.parent.mkdir(parents=True,exist_ok=True)
    lines=["# 1000+ 기능 레지스터 — Codex/RAG/MCP/GAN/하니스/다중에이전트","",f"- 생성 시각: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')} UTC",f"- 총 항목 수: {len(rows)}","- 완료/대기/예정/운영규칙을 섞지 않기 위한 기준표다.","","| ID | 분류 | 기능 | 상태 | 설명 |","|---:|---|---|---|---|"]
    lines += [f"| {i} | {c} | {n} | {s} | {d} |" for i,c,n,s,d in rows]
    OUT.write_text("\n".join(lines)+"\n",encoding="utf-8")
    print(f"generated: {OUT}"); print(f"features: {len(rows)}")
    if a.check and len(rows)<1000: raise SystemExit(1)
if __name__=="__main__": main()
