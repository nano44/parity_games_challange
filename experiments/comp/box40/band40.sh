#!/bin/bash
# L-COMP box 40 item 3 runner (resumable: climb40 OUT.state; a log with DONE is skipped; flock = one copy per tag).
# Usage: band39.sh TAG LO HI SEEDNUM C seed.json   (climb: 1 restart x 200 proposals)  |  band39.sh grow TAG LO HI SEEDNUM C seed.json
# Needs env LSI = a worktree of claude/l-si f65e0fb9 and LSIROOT = git archive of l-new fcba92fc (experiments/new, experiments/si/si.py, experiments/harness) for the second engine.
cd "$(dirname "$0")"
if [ "$1" = grow ]; then shift; T=$1; exec 9>out/.lock_$T; flock -n 9 || exit 0; grep -q DONE out/climb40_$T.log 2>/dev/null && exit 0
  python3 climb40.py grow $T $2 $3 $4 out/climb40_$T.log $5 $6; exit $?; fi
T=$1; exec 9>out/.lock_$T; flock -n 9 || exit 0; grep -q DONE out/climb40_$T.log 2>/dev/null && exit 0
python3 climb40.py $T $2 $3 1 200 $4 out/climb40_$T.log $5 $6
