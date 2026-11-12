#!/bin/bash
# L-COMP box 39 item 2 runner (resumable: climb39 OUT.state; a log with DONE is skipped; flock = one copy per tag).
# Usage: band39.sh TAG LO HI SEEDNUM C seed.json   (climb: 1 restart x 200 proposals)  |  band39.sh grow TAG LO HI SEEDNUM C seed.json
# Needs env LNEW = a worktree of claude/l-new (second engine for every new best; git worktree add --detach <dir> origin/claude/l-new).
cd "$(dirname "$0")"
if [ "$1" = grow ]; then shift; T=$1; exec 9>out/.lock_$T; flock -n 9 || exit 0; grep -q DONE out/climb39_$T.log 2>/dev/null && exit 0
  python3 climb39.py grow $T $2 $3 $4 out/climb39_$T.log $5 $6; exit $?; fi
T=$1; exec 9>out/.lock_$T; flock -n 9 || exit 0; grep -q DONE out/climb39_$T.log 2>/dev/null && exit 0
python3 climb39.py $T $2 $3 1 200 $4 out/climb39_$T.log $5 $6
