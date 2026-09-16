# Repository Rules

> 이 문서는 Repository를 일관되고 효율적으로 관리하기 위한 기본 규칙을 정의합니다.
>
> 프로젝트, 과제, 공부 및 기타 작업은 아래 규칙을 기본으로 관리합니다.

---

# 1. 기본 원칙

1. 모든 작업은 가능한 한 기록으로 남긴다.
2. 작업의 목적과 내용을 명확하게 작성한다.
3. 작업 단위가 명확한 경우 Issue를 생성하여 관리한다.
4. 작업의 진행 상황은 GitHub Projects에서 관리한다.
5. 코드 변경사항은 Commit으로 기록한다.
6. 작업의 성격에 따라 적절한 Branch를 사용한다.
7. 완료된 작업은 관련 Issue, Project 및 문서를 가능한 한 함께 정리한다.
8. 공부한 내용과 과제 결과물은 가능한 한 Repository에 기록한다.
9. 문서와 실제 작업 내용이 서로 다르지 않도록 주기적으로 확인한다.
10. 현재 상황에 맞지 않는 규칙은 필요에 따라 수정할 수 있다.

---

# 2. Repository 구조

Repository는 다음과 같은 기본 구조를 사용한다.

    Repository
    │
    ├── README.md
    ├── RULES.md
    ├── GOALS.md
    ├── ASSIGNMENTS.md
    │
    ├── docs/
    │   └── study/
    │
    └── [프로젝트 파일]

## 파일 및 폴더의 역할

| 파일/폴더 | 역할 |
|---|---|
| `README.md` | Repository 및 프로젝트 소개 |
| `RULES.md` | Repository 사용 및 관리 규칙 |
| `GOALS.md` | 학기 목표 및 장기 계획 |
| `ASSIGNMENTS.md` | 주차별 과제 기록 |
| `docs/study/` | 공부한 내용 및 학습 기록 |
| 프로젝트 폴더 | 실제 프로젝트 코드 및 리소스 |

---

# 3. Branch 규칙

Branch는 작업의 종류에 따라 구분한다.

## 기본 Branch 구조

    main
    └── dev
        ├── feature/[기능명]
        ├── assignment/[과제명]
        └── study/[공부내용]

## 3.1 `main`

최종적으로 안정된 상태의 코드를 관리하는 Branch.

- 직접 작업하지 않는다.
- 충분히 검증된 작업만 Merge한다.
- 프로젝트의 안정적인 버전을 유지한다.

## 3.2 `dev`

개발 중인 작업을 통합하는 Branch.

- 각 작업 Branch에서 완료된 내용을 Merge한다.
- 개발 과정의 기준 Branch로 사용한다.
- 작업 중인 기능은 가능한 한 개인 작업 Branch에서 개발한다.

## 3.3 `feature/[기능명]`

새로운 기능을 개발할 때 사용한다.

예:

    feature/login
    feature/player-movement
    feature/inventory
    feature/save-system

- 하나의 기능 단위로 Branch를 생성한다.
- 기능 개발이 끝나면 `dev`에 Merge한다.
- 기능 개발이 끝난 Branch는 더 이상 필요하지 않은 경우 정리한다.

## 3.4 `assignment/[과제명]`

수업 과제를 진행할 때 사용한다.

예:

    assignment/week01
    assignment/week02
    assignment/data-analysis

- 하나의 과제 또는 과제 단위로 Branch를 생성한다.
- 과제가 완료되면 필요한 Branch에 Merge한다.
- 과제 결과물은 해당 과제와 연결될 수 있도록 관리한다.

## 3.5 `study/[공부내용]`

개인 공부 및 실습을 진행할 때 사용한다.

예:

    study/git
    study/github
    study/csharp
    study/unity

- 공부 또는 실습의 목적에 맞게 Branch를 생성한다.
- 공부한 내용은 가능한 한 `docs/study/`에도 기록한다.
- 단순한 메모나 문서 수정만 필요한 경우 별도의 Branch가 필요하지 않을 수 있다.

---

# 4. Branch 생성 및 작업 규칙

작업을 시작하기 전에 현재 Branch를 확인한다.

    git branch

작업 목적에 맞는 Branch로 이동한 후 작업한다.

    git switch feature/login

새로운 Branch를 생성하면서 이동할 경우:

    git switch -c feature/login

작업 Branch에서는 해당 작업과 관련된 변경사항을 중심으로 작업한다.

---

# 5. Commit 규칙

Commit 메시지는 변경 내용을 명확하게 알 수 있도록 작성한다.

## 기본 형식

    type: 작업 내용

## Commit Type

| Type | 의미 |
|---|---|
| `feat` | 새로운 기능 추가 |
| `fix` | 버그 및 오류 수정 |
| `docs` | 문서 수정 |
| `study` | 공부 및 실습 |
| `assignment` | 과제 관련 작업 |
| `refactor` | 코드 구조 개선 |
| `test` | 테스트 관련 작업 |
| `chore` | 설정, 정리 및 기타 작업 |

## Commit 예시

    feat: 플레이어 이동 기능 구현
    feat: 로그인 기능 추가
    fix: 플레이어 충돌 오류 수정
    docs: README 수정
    study: Git Branch 학습 내용 추가
    assignment: 3주차 과제 추가
    refactor: 플레이어 코드 구조 개선
    test: 로그인 기능 테스트 추가
    chore: 프로젝트 설정 파일 정리

## Commit 작성 원칙

1. 하나의 Commit에는 가능한 한 하나의 작업을 담는다.
2. Commit 메시지만 보고 변경 내용을 이해할 수 있도록 작성한다.
3. 의미 없는 Commit 메시지는 사용하지 않는다.

### 잘못된 예

    수정
    수정함
    완료
    최종
    진짜 최종

### 좋은 예

    fix: 플레이어 점프 오류 수정
    feat: 인벤토리 아이템 추가 기능 구현
    docs: Git 사용 규칙 추가

---

# 6. Push 규칙

Commit한 작업은 필요한 경우 원격 Repository에 Push한다.

    git push origin [Branch 이름]

예:

    git push origin feature/login

작업 Branch를 Push할 때는 현재 작업 중인 Branch를 확인한 후 Push한다.

    git branch

---

# 7. Issue 규칙

새로운 작업이나 해결해야 할 문제가 생기면 가능한 한 Issue로 관리한다.

## Issue를 생성해야 하는 경우

- 새로운 기능을 개발할 때
- 버그를 발견했을 때
- 과제가 새로 나왔을 때
- 공부할 주제가 생겼을 때
- 프로젝트에서 해결해야 할 문제가 생겼을 때
- 문서를 작성하거나 수정해야 할 때
- 테스트가 필요한 작업이 생겼을 때

## Issue 제목 규칙

Issue 제목은 작업 내용을 짧고 명확하게 작성한다.

좋은 예:

    로그인 기능 구현
    플레이어 이동 오류 수정
    인벤토리 시스템 구현
    3주차 과제 작성
    C# 클래스 공부
    프로젝트 데모 버전 제작

## Issue 내용

필요한 경우 다음 내용을 포함한다.

    ## 작업 내용

    [무엇을 해야 하는지 작성]

    ## 목적

    [왜 이 작업이 필요한지 작성]

    ## 해야 할 일

    - [ ] 작업 1
    - [ ] 작업 2
    - [ ] 작업 3

    ## 완료 조건

    [어떤 상태가 되면 작업이 완료된 것으로 판단하는지 작성]

작업의 규모가 작다면 모든 항목을 작성할 필요는 없다.

---

# 8. Label 규칙

Label은 Issue의 성격을 구분하기 위해 사용한다.

기본 Label은 다음과 같이 사용한다.

| Label | 의미 |
|---|---|
| `feature` | 새로운 기능 |
| `bug` | 버그 및 오류 |
| `assignment` | 수업 과제 |
| `study` | 공부 및 학습 |
| `design` | 디자인 및 UI/UX |
| `documentation` | 문서 작성 |
| `refactor` | 코드 구조 개선 |
| `test` | 테스트 |
| `question` | 질문 및 논의 |

## Label 사용 원칙

1. Issue의 성격에 맞는 Label을 지정한다.
2. 하나의 Issue에 여러 Label을 지정할 수 있다.
3. 필요 이상의 Label을 만들지 않는다.
4. 기존 Label로 구분하기 어려운 경우 새로운 Label을 추가한다.

예:

    Issue: 로그인 기능 구현
    Label: feature

    Issue: 로그인 버튼이 작동하지 않는 문제
    Label: bug

    Issue: C# 클래스 학습
    Label: study

---

# 9. Milestone 규칙

Milestone은 여러 Issue를 하나의 큰 목표 또는 기간으로 묶을 때 사용한다.

예:

    1차 개발
    2차 개발
    데모 버전
    최종 버전

또는 학기 단위의 목표:

    2026 2학기
    중간 목표
    기말 목표

## Milestone 사용 원칙

1. 여러 작업이 하나의 큰 목표에 포함되는 경우 Milestone을 사용한다.
2. 가능하면 완료 기한을 지정한다.
3. Milestone의 목적이 명확하도록 이름을 작성한다.
4. Milestone에 연결된 Issue가 완료되면 진행률을 확인한다.

---

# 10. Project / Kanban 규칙

GitHub Projects의 Kanban Board를 사용하여 작업 진행 상황을 관리한다.

## 기본 상태

    Todo → In Progress → Review → Done

## Todo

아직 시작하지 않은 작업.

예:

    로그인 구현
    인벤토리 구현
    3주차 과제
    Git 공부

## In Progress

현재 작업 중인 작업.

작업을 실제로 시작하면 `Todo`에서 `In Progress`로 이동한다.

## Review

작업은 완료했지만 확인 또는 검토가 필요한 상태.

예:

- 코드 검토가 필요한 경우
- 테스트가 필요한 경우
- Pull Request 검토 중인 경우
- 결과물을 확인해야 하는 경우

## Done

작업이 최종적으로 완료된 상태.

완료 조건을 만족하고 추가 작업이 필요하지 않은 경우 `Done`으로 이동한다.

---

# 11. Pull Request 규칙

Branch에서 작업한 내용을 다른 Branch에 반영할 때 Pull Request를 사용한다.

기본적인 흐름:

    작업 Branch
        ↓
    Commit
        ↓
    Push
        ↓
    Pull Request
        ↓
    Review
        ↓
    Merge

## Pull Request 제목

Pull Request에서 어떤 작업을 했는지 명확하게 작성한다.

예:

    feat: 로그인 기능 구현
    fix: 플레이어 이동 오류 수정
    assignment: 3주차 과제 추가

## Pull Request 내용

필요한 경우 다음 내용을 포함한다.

    ## 작업 내용

    [무엇을 구현했는지 작성]

    ## 변경 사항

    - [변경 사항 1]
    - [변경 사항 2]
    - [변경 사항 3]

    ## 테스트

    - [ ] 기능 테스트
    - [ ] 오류 확인

    ## 관련 Issue

    Closes #[Issue 번호]

---

# 12. Merge 규칙

기본적인 작업 흐름은 다음과 같이 유지한다.

    feature
       ↓
      dev
       ↓
      main

작업 Branch에서 완료한 기능은 필요한 검토 후 `dev`에 Merge한다.

`dev`에서 충분히 검증된 안정적인 버전은 `main`에 Merge한다.

---

# 13. 과제 관리 규칙

매주 새로운 과제가 주어지는 경우 다음과 같이 관리한다.

1. 과제가 나오면 Issue를 생성한다.
2. `assignment` Label을 지정한다.
3. 필요한 경우 해당 주차의 Milestone을 지정한다.
4. 필요한 경우 `assignment/[과제명]` Branch를 생성한다.
5. 과제를 진행한다.
6. 결과물을 Repository에 반영한다.
7. 과제가 완료되면 Issue를 정리한다.
8. Project에서 작업을 `Done`으로 이동한다.
9. `ASSIGNMENTS.md`에 과제를 기록한다.

---

# 14. 공부 관리 규칙

공부 계획과 실제 공부 내용을 구분한다.

## 공부 계획

`GOALS.md`에 기록한다.

예:

    Git Branch를 9월 20일까지 공부한다.

## 실제 공부 내용

`docs/study/`에 기록한다.

예:

    docs/study/git.md

공부 기록에는 가능한 경우 다음 내용을 포함한다.

- 공부한 개념
- 사용 방법
- 예제
- 직접 실습한 내용
- 발생한 오류
- 오류 해결 방법
- 배운 점

---

# 15. 프로젝트 관리 규칙

프로젝트의 실제 코드와 리소스는 Repository의 프로젝트 영역에서 관리한다.

프로젝트에서 해야 할 작업은 GitHub Issue와 Project를 이용하여 관리한다.

예:

    프로젝트 목표
        ↓
    Milestone
        ↓
    Issue
        ↓
    Project / Kanban
        ↓
    Branch
        ↓
    Commit
        ↓
    Pull Request
        ↓
    Merge

프로젝트의 장기적인 목표는 `GOALS.md`에 기록한다.

---

# 16. 문서 관리 규칙

문서는 가능한 한 Markdown(`.md`) 형식으로 작성한다.

각 문서는 목적에 맞는 위치에 저장한다.

    README.md
    → Repository 및 프로젝트 소개

    RULES.md
    → Repository 관리 규칙

    GOALS.md
    → 학기 목표 및 계획

    ASSIGNMENTS.md
    → 과제 기록

    docs/study/
    → 공부 내용

문서의 내용이 변경되면 필요한 경우 Commit으로 기록한다.

예:

    docs: 공부 기록 업데이트
    docs: Repository 규칙 수정

---

# 17. 주간 관리 규칙

매주 최소 한 번 Repository의 전체적인 진행 상황을 확인한다.

## 확인 목록

- [ ] 이번 주 과제를 Issue로 등록했는가?
- [ ] 해야 할 작업을 Issue로 등록했는가?
- [ ] Project의 작업 상태를 업데이트했는가?
- [ ] 완료한 작업을 `Done`으로 이동했는가?
- [ ] 공부한 내용을 기록했는가?
- [ ] `GOALS.md`의 목표 진행 상황을 확인했는가?
- [ ] `ASSIGNMENTS.md`의 과제 기록을 업데이트했는가?
- [ ] 필요하지 않은 작업이나 Issue를 정리했는가?

---

# 18. 완료된 작업 관리

작업이 완료되면 다음 사항을 확인한다.

- [ ] 작업 내용이 실제로 완료되었는가?
- [ ] 필요한 테스트를 진행했는가?
- [ ] Commit이 정상적으로 기록되었는가?
- [ ] 원격 Repository에 Push했는가?
- [ ] 필요한 경우 Pull Request를 생성했는가?
- [ ] 관련 Issue를 업데이트했는가?
- [ ] Project 상태를 `Done`으로 변경했는가?
- [ ] 필요한 문서를 업데이트했는가?

---

# 19. 규칙 수정

이 문서의 규칙은 학기 동안 실제 사용 환경에 맞게 수정할 수 있다.

새로운 규칙이 필요하거나 기존 규칙이 불필요하다고 판단되는 경우 내용을 수정한다.

규칙을 수정한 경우 변경 내용을 Commit으로 기록한다.

예:

    docs: Repository 관리 규칙 수정

규칙을 수정할 때는 기존 작업 흐름에 불필요한 복잡성을 추가하지 않는 것을 원칙으로 한다.

---

# 20. 최종 원칙

> Repository는 기록 자체를 목적으로 사용하는 것이 아니라,
> 프로젝트와 학습을 효율적으로 관리하기 위해 사용한다.

다음 원칙을 가장 중요하게 유지한다.

1. 작업을 명확하게 기록한다.
2. 작은 작업이라도 필요한 경우 Issue로 관리한다.
3. 작업 상태를 최신 상태로 유지한다.
4. Commit 내용을 명확하게 작성한다.
5. Branch를 목적에 맞게 사용한다.
6. 공부와 과제의 결과를 가능한 한 기록으로 남긴다.
7. 문서를 실제 작업 내용과 일치하도록 유지한다.
8. 불필요하게 복잡한 규칙은 만들지 않는다.
9. 학기 동안 실제 사용하면서 규칙을 개선한다.
