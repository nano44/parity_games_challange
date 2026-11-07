#!/bin/bash
# L-RED 56 R221 batch 4: adversarial climbs vs RHO-SET / RHO-E (SCORE=rho: violations first, then max rho at a SET gate); waits for batch 3.
cd "$(dirname "$0")"
while pgrep -f "go[23].sh" > /dev/null; do sleep 20; done
run() { [ -f out/$1.done ] && return; SCORE=rho python3 ladclimb.py $2 > out/$1.log 2>&1 && touch out/$1.done; }
export -f run
cat <<J | xargs -P 4 -L 1 bash -c 'run "$@"' _
H23 "31 rnd 2 3 2 2 4000 out/H23.json"
H33 "32 rnd 3 3 2 2 4000 out/H33.json"
H34 "33 rnd 3 4 2 2 4000 out/H34.json"
H43 "34 rnd 4 3 2 2 4000 out/H43.json"
H25 "35 rnd 2 5 2 2 4000 out/H25.json"
H333 "36 rnd 3 3 3 2 4000 out/H333.json"
H44 "37 rnd 4 4 2 2 4000 out/H44.json"
H26 "38 rnd 2 6 2 2 4000 out/H26.json"
J
