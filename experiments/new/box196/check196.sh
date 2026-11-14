#!/bin/bash
# Box 196 machine check (L-NEW successor 64): re-runs qt3_196.py on a fixed set; prints to stdout (check.sh diffs it with check196.out).
# Fail counters must be 0 on every line except the «ctrl» lines (controls must fire) and the «spec» line (N5 is not Howard: nohoward > 0).
cd "$(dirname "$0")"
for fam in rand esc noesc deep dense lvl0 late acyc; do python3 qt3_196.py $fam 1964 100; done
for c in 1 2 3; do Q196_TAG="ctrl$c " Q196_CTRL=$c python3 qt3_196.py rand 1963 50; done
Q196_TAG="spec " Q196_MODE=spec python3 qt3_196.py rand 1963 100
python3 qt3_196.py --files inst/RT_n1.json ../box194/inst/LEAP_k64.json ../box194/inst/RS2_L32M6.json ../box194/inst/rd3_d4.json ../box191/inst/cyc_d8.json
