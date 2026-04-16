#!/usr/bin/env python3
"""
Automatically makes commits on pre-defined dates to create
"Hello World" pixel art in the GitHub contribution graph.

Each target date receives 10 commits so the square appears dark green.
Run via the GitHub Actions workflow (.github/workflows/auto_commit.yml).
"""

import subprocess
from datetime import date

# ---------------------------------------------------------------------------
# Target dates for "Hello World" pixel art (DD.MM.YYYY → date objects)
# ---------------------------------------------------------------------------
TARGET_DATES = {
    # H
    date(2026, 4, 16), date(2026, 4, 20), date(2026, 4, 21), date(2026, 4, 22), date(2026, 4, 23), date(2026, 4, 24),
    date(2026, 4, 29),
    # e
    date(2026, 5, 4), date(2026, 5, 5), date(2026, 5, 6), date(2026, 5, 7), date(2026, 5, 8),
    date(2026, 5, 18), date(2026, 5, 19), date(2026, 5, 20), date(2026, 5, 21), date(2026, 5, 22),
    date(2026, 5, 25),
    date(2026, 5, 27),
    date(2026, 5, 29),
    # l
    date(2026, 6, 8), date(2026, 6, 9), date(2026, 6, 10), date(2026, 6, 11), date(2026, 6, 12),
    date(2026, 6, 19),
    # l
    date(2026, 6, 29), date(2026, 6, 30), date(2026, 7, 1), date(2026, 7, 2), date(2026, 7, 3),
    date(2026, 7, 10),
    # o
    date(2026, 7, 20), date(2026, 7, 21), date(2026, 7, 22), date(2026, 7, 23), date(2026, 7, 24),
    date(2026, 7, 31),
    date(2026, 8, 3), date(2026, 8, 4), date(2026, 8, 5), date(2026, 8, 6), date(2026, 8, 7),
    date(2026, 8, 17), date(2026, 8, 18), date(2026, 8, 19), date(2026, 8, 20),
    date(2026, 8, 28),
    # (space)
    # W
    date(2026, 9, 3),
    date(2026, 9, 11),
    date(2026, 9, 14), date(2026, 9, 15), date(2026, 9, 16), date(2026, 9, 17),
    date(2026, 9, 28), date(2026, 9, 29), date(2026, 9, 30), date(2026, 10, 1), date(2026, 10, 2),
    date(2026, 10, 9),
    date(2026, 10, 12), date(2026, 10, 13), date(2026, 10, 14), date(2026, 10, 15), date(2026, 10, 16),
    # o
    date(2026, 10, 26), date(2026, 10, 27), date(2026, 10, 28), date(2026, 10, 29), date(2026, 10, 30),
    date(2026, 11, 4),
    date(2026, 11, 9), date(2026, 11, 10),
    date(2026, 11, 12), date(2026, 11, 13),
    date(2026, 11, 23), date(2026, 11, 24), date(2026, 11, 25), date(2026, 11, 26), date(2026, 11, 27),
    # r
    date(2026, 12, 4),
    date(2026, 12, 14), date(2026, 12, 15), date(2026, 12, 16), date(2026, 12, 17), date(2026, 12, 18),
    date(2026, 12, 25),
    # l (d)
    date(2026, 12, 29), date(2026, 12, 30), date(2026, 12, 31),
}

# Number of commits per target day – 10 ensures a dark-green square.
COMMITS_PER_DAY = 10


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True)


def make_commits(today: date) -> None:
    date_str = today.isoformat()
    print(f"Making {COMMITS_PER_DAY} commits for {date_str} …")
    for i in range(1, COMMITS_PER_DAY + 1):
        with open("activity.txt", "a", encoding="utf-8") as fh:
            fh.write(f"{date_str} – commit {i}/{COMMITS_PER_DAY}\n")
        run(["git", "add", "activity.txt"])
        run(["git", "commit", "-m", f"pixel art – {date_str} ({i}/{COMMITS_PER_DAY})"])
    print("Done.")


def main() -> None:
    today = date.today()
    if today in TARGET_DATES:
        make_commits(today)
    else:
        print(f"{today} is not a target date – nothing to do.")


if __name__ == "__main__":
    main()
