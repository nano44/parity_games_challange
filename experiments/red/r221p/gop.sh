#!/bin/bash
# L-RED 56 R221 post-fallback climbs (SCORE=post); needs WT, WT3 (r218/env.sh); resumable via out/<name>.done
cd "$(dirname "$0")"
run() { [ -f out/$1.done ] && return; SCORE=post python3 ladclimb.py $2 > out/$1.log 2>&1 && touch out/$1.done; }
export -f run
cat <<J | xargs -P 4 -L 1 bash -c 'run "$@"' _
P33 "51 rnd 3 3 2 0 700 out/P33.json"
P42 "52 rnd 4 2 2 0 700 out/P42.json"
P24 "53 rnd 2 4 2 0 700 out/P24.json"
P52 "54 rnd 5 2 2 0 700 out/P52.json"
J
