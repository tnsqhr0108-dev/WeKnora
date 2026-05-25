]0;echo "# Codex Cloud Runbook"# Codex Cloud Runbook
]0;echo ""
]0;echo "Repository: tnsqhr0108-dev/$REPO"Repository: tnsqhr0108-dev/WeKnora
]0;echo "Branch: $BRANCH"Branch: main
]0;echo ""
]0;echo "먼저 실행할 명령:"먼저 실행할 명령:
]0;echo ""
]0;echo "pwd"pwd
]0;echo "git branch --show-current"git branch --show-current
]0;echo "git rev-parse HEAD"git rev-parse HEAD
]0;echo "git status --short"git status --short
]0;echo "find . -maxdepth 3 -type f | sort"find . -maxdepth 3 -type f | sort
]0;echo ""
]0;echo "캐시 문제:"캐시 문제:
]0;echo ""
]0;echo "Codex Cloud에서 오래된 파일, 잘못된 브랜치, 누락된 의존성이 보이면 environment cache를 reset하고 새 작업을 시작한다."Codex Cloud에서 오래된 파일, 잘못된 브랜치, 누락된 의존성이 보이면 environment cache를 reset하고 새 작업을 시작한다.
]0;echo ""
]0;echo "완료 규칙:"완료 규칙:
]0;echo ""
]0;echo "예상 파일, 생성 결과, 테스트 결과가 실제로 존재하지 않으면 완료라고 말하지 않는다."예상 파일, 생성 결과, 테스트 결과가 실제로 존재하지 않으면 완료라고 말하지 않는다.
