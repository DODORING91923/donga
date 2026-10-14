
import json
import os
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

TOKEN = os.environ["GH_TOKEN"]
REPOSITORY = os.environ["GITHUB_REPOSITORY"]
API = f"https://api.github.com/repos/{REPOSITORY}"
NOW = datetime.now(timezone.utc)
SINCE = NOW - timedelta(days=30)


def parse_date(value):
    if not value:
        return None
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def get_json(url):
    request = urllib.request.Request(
        url,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def get_all(url):
    results = []
    page = 1
    while True:
        separator = "&" if "?" in url else "?"
        batch = get_json(f"{url}{separator}per_page=100&page={page}")
        if not isinstance(batch, list) or not batch:
            break
        results.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    return results


def get_first_commit_date(pr_number):
    commits = get_all(f"{API}/pulls/{pr_number}/commits")
    dates = []
    for commit in commits:
        data = commit.get("commit", {})
        author = data.get("author") or {}
        committer = data.get("committer") or {}
        value = author.get("date") or committer.get("date")
        parsed = parse_date(value)
        if parsed:
            dates.append(parsed)
    return min(dates) if dates else None


def main():
    # Lead Time: 최근 30일 내 병합된 PR의 첫 커밋부터 병합까지
    prs = get_all(f"{API}/pulls?state=closed")
    lead_times_hours = []

    for pr in prs:
        merged = parse_date(pr.get("merged_at"))
        if not merged or merged < SINCE:
            continue

        first_commit = get_first_commit_date(pr["number"])
        if first_commit and merged >= first_commit:
            lead_times_hours.append(
                (merged - first_commit).total_seconds() / 3600
            )

    # 배포 목록과 각 배포의 최종 상태 조회
    deployments = get_all(f"{API}/deployments")
    records = []

    for deployment in deployments:
        created = parse_date(deployment.get("created_at"))
        if not created or created < SINCE:
            continue

        statuses = get_all(
            f"{API}/deployments/{deployment['id']}/statuses"
        )
        if not statuses:
            continue

        # API는 보통 최신 상태부터 반환하므로 updated_at으로 정렬
        statuses.sort(
            key=lambda item: item.get("updated_at") or "",
            reverse=True,
        )
        final_status = statuses[0].get("state")
        if final_status not in ("success", "failure", "error"):
            continue

        records.append({
            "id": deployment["id"],
            "environment": deployment.get("environment") or "unknown",
            "sha": deployment.get("sha"),
            "created_at": created,
            "status": final_status,
            "status_at": parse_date(
                statuses[0].get("updated_at")
            ) or created,
        })

    successful = [r for r in records if r["status"] == "success"]
    failed = [r for r in records if r["status"] in ("failure", "error")]

    # MTTR 대리 지표: 실패한 배포 이후 같은 환경의 다음 성공 배포까지
    recovery_hours = []
    for failure in failed:
        recoveries = [
            success for success in successful
            if success["environment"] == failure["environment"]
            and success["status_at"] >= failure["status_at"]
        ]
        if recoveries:
            recovery = min(recoveries, key=lambda item: item["status_at"])
            recovery_hours.append(
                (recovery["status_at"] - failure["status_at"]).total_seconds()
                / 3600
            )

    result = {
        "generated_at": NOW.isoformat(),
        "period_days": 30,
        "repository": REPOSITORY,
        "metrics": {
            "lead_time": {
                "value_hours": (
                    round(sum(lead_times_hours) / len(lead_times_hours), 2)
                    if lead_times_hours else None
                ),
                "sample_count": len(lead_times_hours),
                "definition": (
                    "Average first commit to PR merge; "
                    "proxy, not production deployment lead time"
                ),
            },
            "deployment_frequency": {
                "successful_deployments": len(successful),
                "per_30_days": len(successful),
                "definition": "Successful GitHub deployments in the last 30 days",
            },
            "mttr": {
                "value_hours": (
                    round(sum(recovery_hours) / len(recovery_hours), 2)
                    if recovery_hours else None
                ),
                "recovered_failure_count": len(recovery_hours),
                "definition": (
                    "Proxy: failed deployment status to next successful "
                    "deployment in the same environment"
                ),
            },
            "change_failure_rate": {
                "value_percent": (
                    round(100 * len(failed) / len(records), 2)
                    if records else None
                ),
                "failed_deployments": len(failed),
                "finalized_deployments": len(records),
                "definition": (
                    "Failed/error deployments divided by finalized "
                    "deployments; proxy for change failure rate"
                ),
            },
        },
    }

    output = Path("reports/dora-metrics.json")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    try:
        main()
    except (urllib.error.URLError, urllib.error.HTTPError, KeyError, ValueError) as error:
        print(f"::error::DORA collection failed: {error}")
        raise
