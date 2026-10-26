#!/bin/bash
# REFEREE-2 successor 17: second union search, larger components.
cd "$(dirname "$0")"
X=../../../experiments
export BUDGET=100000 SAVE_DIR=union TMPDIR_UNION=${TMPDIR_UNION:-/tmp}
python3 root_check.py unionsearch $X/red/xing/instances/x32_rand64.pg 3000 10 18 6 7201 > logs/union2_x64_k6.txt 2>&1 &
python3 root_check.py unionsearch $X/red/so/instances/xsnf52_n64.pg 3000 8 16 4 7202 > logs/union2_xsnf52_k4.txt 2>&1 &
wait
