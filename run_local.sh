#!/usr/bin/env bash
# run_local.sh – Runs commit_script.py locally and pushes new commits.
# Schedule via launchd (see README) or run manually: bash run_local.sh

set -euo pipefail

# Resolve the directory this script lives in (= repo root)
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$REPO_DIR"

echo "=== Pixel Art Auto-Commit ($(date '+%Y-%m-%d %H:%M:%S')) ==="

# Pull latest changes to avoid push conflicts
git pull --rebase --autostash

# Run the commit script
python3 commit_script.py

# Push if new commits were created
if ! git diff --quiet "origin/$(git branch --show-current)"..HEAD 2>/dev/null; then
    echo "Pushing new commits…"
    git push
else
    echo "No new commits – nothing to push."
fi
