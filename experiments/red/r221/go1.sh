#!/bin/bash
# L-RED 56 R221 batch 1: ladder climbs (run from experiments/red/r221; logs in out/)
cd "$(dirname "$0")"
run() { [ -f out/$1.done ] && return; python3 ladclimb.py $2 > out/$1.log 2>&1 && touch out/$1.done; }
export -f run
cat <<J | xargs -P 4 -L 1 bash -c 'run "$@"' _
L4K3 "1 lad 4 0 0 3 3000 out/L4K3.json"
L6K4 "2 lad 6 0 0 4 3000 out/L6K4.json"
L8K5 "3 lad 8 0 0 5 3000 out/L8K5.json"
R33K3 "4 rnd 3 3 2 3 3000 out/R33K3.json"
R43K4 "5 rnd 4 3 2 4 3000 out/R43K4.json"
R53K5 "6 rnd 5 3 2 5 3000 out/R53K5.json"
J
