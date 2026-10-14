#!/bin/bash
# 지난주 동안의 Code Churn 계산
# 실행 권한 부여: chmod +x scripts/measure_churn.sh
# 실행: ./scripts/measure_churn.sh

set -euo pipefail

# --no-merges: Merge Commit의 변경 내용이 중복으로 집계되지 않도록 제외
# 바이너리 파일은 추가/삭제 줄 수가 "-"로 표시되므로 숫자인 줄만 집계
git log --since="1 week ago" --no-merges --numstat --pretty=format:"" |
  awk '$1 ~ /^[0-9]+$/ && $2 ~ /^[0-9]+$/ { added += $1; removed += $2 }
    END {
      print "Lines Added:", added + 0
      print "Lines Removed:", removed + 0
      print "Total Churn:", added + removed
    }'
