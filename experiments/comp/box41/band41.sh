#!/bin/bash
# L-COMP box 41 items 2-3 runner (resumable: climb41 OUT.state; a log with DONE is skipped; flock = one copy per tag).
# Usage: band39.sh TAG LO HI SEEDNUM C seed.json   (climb: 1 restart x 200 proposals)  |  band39.sh grow TAG LO HI SEEDNUM C seed.json
# Second engine env: SCORE=deep: LSI100 (worktree claude/l-si 23d39400), RED (worktree claude/l-red 59daaef2), LNEW (git archive of l-new fcba92fc); SCORE=sccfloor: LSI, LSIROOT as box 40.
cd "$(dirname "$0")"
if [ "$1" = grow ]; then shift; T=$1; exec 9>out/.lock_$T; flock -n 9 || exit 0; grep -q DONE out/climb41_$T.log 2>/dev/null && exit 0
  python3 climb41.py grow $T $2 $3 $4 out/climb41_$T.log $5 $6; exit $?; fi
T=$1; exec 9>out/.lock_$T; flock -n 9 || exit 0; grep -q DONE out/climb41_$T.log 2>/dev/null && exit 0
python3 climb41.py $T $2 $3 1 200 $4 out/climb41_$T.log $5 $6
