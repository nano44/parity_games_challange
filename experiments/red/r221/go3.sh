#!/bin/bash
# L-RED 56 R221 batch 3: climbs scored by max re-entries at one (v, Lambda-interval) (SCORE=reent); waits for batch 2.
cd "$(dirname "$0")"
while pgrep -f "go2.sh" > /dev/null; do sleep 20; done
run() { [ -f out/$1.done ] && return; SCORE=reent python3 ladclimb.py $2 > out/$1.log 2>&1 && touch out/$1.done; }
export -f run
cat <<J | xargs -P 4 -L 1 bash -c 'run "$@"' _
E22 "21 rnd 2 4 2 2 4000 out/E22.json"
E32 "22 rnd 3 4 2 2 4000 out/E32.json"
E33 "23 rnd 3 4 2 3 4000 out/E33.json"
E43 "24 rnd 4 4 2 3 4000 out/E43.json"
E24 "25 rnd 2 6 2 2 4000 out/E24.json"
EL6 "26 lad 6 0 0 3 4000 out/EL6.json"
E34 "27 rnd 3 6 2 3 4000 out/E34.json"
E28 "28 rnd 2 8 2 2 4000 out/E28.json"
J
