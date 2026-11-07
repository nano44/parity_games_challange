#!/bin/bash
# L-COMP box 28: every 10 min, refresh log/cnf2_d4_status.txt; if it changed and no push is running: fetch + merge origin/claude/l-comp,
# commit it (and box28 split-split files are NOT tracked), then run scripts/push.sh synchronously (pushes chained, never two at once).
# Output: log/commit_loop.out (local). A non-fast-forward is retried next round after fetch + merge.
cd "$(dirname "$0")"; R=$(cd ../../.. && pwd)
while true; do
  python3 status_d4.py > /dev/null 2>&1
  if ! pgrep -f "scripts/push.sh" > /dev/null; then
    cd "$R"
    if [ -n "$(git status --porcelain experiments/comp/box28/log/cnf2_d4_status.txt experiments/comp/box28/log/q2)" ] || [ "$(git rev-list --count origin/claude/l-comp..HEAD 2>/dev/null)" != 0 ]; then
      git fetch -q origin claude/l-comp && git merge -q --no-edit origin/claude/l-comp >> experiments/comp/box28/log/commit_loop.out 2>&1
      git add experiments/comp/box28/log/cnf2_d4_status.txt experiments/comp/box28/log/q2
      git diff --cached --quiet || git commit -qm "L-COMP box 28: cnf2 d 4 per-cube verdicts (DATA, cnf2 not audited): $(head -1 experiments/comp/box28/log/cnf2_d4_status.txt | grep -o 'leaves.*'); $(grep '^TAG R4' experiments/comp/box28/log/cnf2_d4_status.txt | grep -o 'leaves.*')

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01V5yGRYZ366UeNYojLQPsMh" >> experiments/comp/box28/log/commit_loop.out 2>&1
      if [ "$(git rev-list --count origin/claude/l-comp..HEAD)" != 0 ]; then
        scripts/push.sh > experiments/comp/box28/log/commit_loop_push.out 2>&1; echo "$(date -u +%FT%TZ) push exit $? head $(git rev-parse --short HEAD)" >> experiments/comp/box28/log/commit_loop.out
      fi
    fi
    cd - > /dev/null
  fi
  sleep 600
done
