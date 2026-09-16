# Repository Rules

> 이 문서는 Repository를 일관되게 관리하기 위한 기본 규칙을 정의합니다.

---

# 1. 기본 원칙

1. 모든 작업은 가능한 한 기록으로 남긴다.
2. 작업의 목적과 내용을 명확하게 작성한다.
3. 작업을 시작하기 전에 필요한 경우 Issue를 생성한다.
4. 작업 상태는 GitHub Projects에서 관리한다.
5. 중요한 변경사항은 Commit으로 기록한다.
6. 공부한 내용과 과제 결과물은 가능한 한 Repository에 남긴다.
7. 학기 중 계획이 변경될 경우 관련 문서를 함께 업데이트한다.

---

# 2. Branch 규칙

Branch는 작업의 종류에 따라 구분한다.

## Branch

```text
main
└── dev
    ├── feature/[기능명]
    ├── assignment/[과제명]
    └── study/[공부내용]

main
최종적으로 안정된 코드만 존재하는 Branch.

직접 작업하지 않는다.
검증된 작업을 Merge한다.

dev
개발 중인 작업을 통합하는 Branch.

각 작업 Branch에서 완료된 내용을 Merge한다.
개발 과정의 기준 Branch로 사용한다.

feature/[기능명]
새로운 기능을 개발할 때 사용한다.

예:
feature/login
feature/inventory
feature/player-movement
assignment/[과제명]

수업 과제를 진행할 때 사용한다.

예:
assignment/week01
assignment/week02
study/[공부내용]

개인 공부 및 실습을 진행할 때 사용한다.

예:
study/git
study/csharp
study/unity
