# Codex Cloud Runbook

Repository: tnsqhr0108-dev/WeKnora
Branch: main

먼저 실행할 명령:
pwd
git branch --show-current
git rev-parse HEAD
git status --short
find . -maxdepth 3 -type f | sort

캐시 문제:
Codex Cloud에서 오래된 파일, 잘못된 브랜치, 누락된 의존성이 보이면 environment cache를 reset하고 새 작업을 시작한다.

완료 규칙:
예상 파일, 생성 결과, 테스트 결과가 실제로 존재하지 않으면 완료라고 말하지 않는다.
