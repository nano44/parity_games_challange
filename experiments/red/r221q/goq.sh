#!/bin/bash
# L-RED 56 R221 quiet-window climbs (SCORE=quiet: longest quiet window W, after QUIET-counter failures); resumable via out/<name>.done
cd "$(dirname "$0")"
run() { [ -f out/$1.done ] && return; SCORE=quiet python3 ladclimb.py $2 > out/$1.log 2>&1 && touch out/$1.done; }
export -f run
cat <<J | xargs -P 4 -L 1 bash -c 'run "$@"' _
Q33 "41 rnd 3 3 2 9 2500 out/Q33.json"
Q42 "42 rnd 4 2 2 9 2500 out/Q42.json"
Q24 "43 rnd 2 4 2 9 2500 out/Q24.json"
Q43 "44 rnd 4 3 2 9 2500 out/Q43.json"
J
