#!/bin/bash
# L-RED 56 R221 batch 2: ladder climbs (run from experiments/red/r221; logs in out/)
cd "$(dirname "$0")"
run() { [ -f out/$1.done ] && return; python3 ladclimb.py $2 > out/$1.log 2>&1 && touch out/$1.done; }
export -f run
cat <<J | xargs -P 4 -L 1 bash -c 'run "$@"' _
L10K5 "11 lad 10 0 0 5 6000 out/L10K5.json"
L12K6 "12 lad 12 0 0 6 6000 out/L12K6.json"
R63K5 "13 rnd 6 3 2 5 6000 out/R63K5.json"
R83K6 "14 rnd 8 3 2 6 6000 out/R83K6.json"
R44K4 "15 rnd 4 4 2 4 6000 out/R44K4.json"
R62K5 "16 rnd 6 2 2 5 6000 out/R62K5.json"
R102K6 "17 rnd 10 2 2 6 6000 out/R102K6.json"
R53K3b "18 rnd 5 3 2 3 6000 out/R53K3b.json"
J
