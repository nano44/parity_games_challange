#!/bin/bash
# REFEREE-2 successor 17: union search for non-vacuous FREEZE-G (b), (c) / RELAY-PIECE (activity inside the class during the interval).
cd "$(dirname "$0")"
X=../../../experiments
export BUDGET=100000 SAVE_DIR=union TMPDIR_UNION=${TMPDIR_UNION:-/tmp}
python3 root_check.py unionsearch $X/red/xing/instances/x32_rand64.pg 3000 6 14 4 7101 > logs/union_x64_k4.txt 2>&1 &
python3 root_check.py unionsearch $X/red/xing/instances/x32_rand48.pg 3000 6 14 6 7102 > logs/union_x48_k6.txt 2>&1 &
wait
