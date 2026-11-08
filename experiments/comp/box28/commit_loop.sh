#!/bin/bash
# L-COMP box 28: every 10 min, refresh log/cnf2_d4_status.txt; if it changed and no push is running: fetch + merge origin/claude/l-comp,
# commit it with box28/log/q2 and box30/out (lane logs, bests, HITS; unit files are excluded locally), then run scripts/push.sh synchronously (pushes chained, never two at once).
# Live lane files (box30/out/*.log, *_best.txt) are kept skip-worktree between rounds (so the tree reads clean) and snapshotted here.
# Output: log/commit_loop.out (local). A non-fast-forward is retried next round after fetch + merge.
cd "$(dirname "$0")"; R=$(cd ../../.. && pwd)
while true; do
  python3 status_d4.py > /dev/null 2>&1
  if ! pgrep -f '^(/usr/bin/env )?(/bin/|/usr/bin/)?(bash )?(\./)?scripts/push\.sh' > /dev/null; then   # L-COMP 12 (Lead 02:20Z): anchored alternation; matches «bash scripts/push.sh», «bash ./scripts/push.sh», «./scripts/push.sh», «/bin/bash ./scripts/push.sh», not wrapper shells or waiting jobs that merely CONTAIN the string (live test 02:2xZ, notebook)
    cd "$R"
    if true || [ "$(git rev-list --count origin/claude/l-comp..HEAD 2>/dev/null)" != 0 ]; then
      git fetch -q origin claude/l-comp && git merge -q --no-edit origin/claude/l-comp >> experiments/comp/box28/log/commit_loop.out 2>&1
      LIVE=$(git ls-files experiments/comp/box30/out experiments/comp/box31/out | grep -E "\.log$|_best\.txt$")
      [ -n "$LIVE" ] && git update-index --no-skip-worktree $LIVE
      git add experiments/comp/box28 experiments/comp/box29 experiments/comp/box30 experiments/comp/box31 notes/L-COMP.md   # all lane files (excluded paths stay out)
      git diff --cached --quiet || git commit -qm "L-COMP box 28-31: periodic snapshot of the lane files (box 31 level-7 climb logs, bests, FROZEN, HITS; box 28-30 records; notebook; DATA)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01V5yGRWSBYFKQNfXo1SpJHh" >> experiments/comp/box28/log/commit_loop.out 2>&1
      LIVE=$(git ls-files experiments/comp/box30/out experiments/comp/box31/out | grep -E "\.log$|_best\.txt$"); [ -n "$LIVE" ] && git update-index --skip-worktree $LIVE
      if [ "$(git rev-list --count origin/claude/l-comp..HEAD)" != 0 ]; then
        scripts/push.sh > experiments/comp/box28/log/commit_loop_push.out 2>&1; echo "$(date -u +%FT%TZ) push exit $? head $(git rev-parse --short HEAD)" >> experiments/comp/box28/log/commit_loop.out
      fi
    fi
    cd - > /dev/null
  fi
  sleep 600
done
