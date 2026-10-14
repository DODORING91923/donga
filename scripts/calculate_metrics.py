import os
import sys
from datetime import datetime

import requests

API_URL = "https://api.github.com"
REPOSITORY = os.environ.get("GITHUB_REPOSITORY", "DODORING91923/donga")
IN_PROGRESS_LABEL = "In Progress"


def _headers():
    headers = {"Accept": "application/vnd.github+json"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def _parse_time(value):
    # GitHub API는 "2026-10-14T03:21:00Z" 형식의 UTC 시간을 반환
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def _get_events(issue_number):
    # 이벤트가 100개를 넘을 수 있으므로 모든 페이지 조회
    url = f"{API_URL}/repos/{REPOSITORY}/issues/{issue_number}/events"
    params = {"per_page": 100}
    events = []
    while url:
        response = requests.get(url, headers=_headers(), params=params, timeout=10)
        response.raise_for_status()
        events.extend(response.json())
        url = response.links.get("next", {}).get("url")
        params = None
    return events


def calculate_cycle_time(issue_number):
    """"In Progress" 라벨이 처음 추가된 시점부터 Issue가 닫힌 시점까지의 시간을 반환한다.

    아직 작업을 시작하지 않았거나 닫히지 않은 Issue는 None을 반환한다.
    """
    # Issue 정보 가져오기
    url = f"{API_URL}/repos/{REPOSITORY}/issues/{issue_number}"
    response = requests.get(url, headers=_headers(), timeout=10)
    response.raise_for_status()
    issue = response.json()

    if not issue.get("closed_at"):
        return None

    # "In Progress" 라벨 추가 시간 찾기 (Issue 응답에는 이벤트가 없어 별도 조회)
    start_time = None
    for event in _get_events(issue_number):
        if event["event"] == "labeled" and event["label"]["name"] == IN_PROGRESS_LABEL:
            start_time = event["created_at"]
            break

    if start_time is None:
        return None

    return _parse_time(issue["closed_at"]) - _parse_time(start_time)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python calculate_metrics.py <issue_number>")

    cycle_time = calculate_cycle_time(int(sys.argv[1]))
    if cycle_time is None:
        print("Cycle time unavailable: issue is still open or was never labeled 'In Progress'.")
    else:
        print(f"Cycle Time: {cycle_time} ({cycle_time.total_seconds() / 3600:.1f} hours)")
