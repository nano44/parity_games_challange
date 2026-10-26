#!/bin/sh
# REFEREE-2 succ. 13: P-N5-1E batch (logs/). Usage: sh run_all.sh
cd "$(dirname "$0")"
python3 onee_check.py random 6000 4 14 91 1E > logs/rand_1E_4-14.txt 2>&1 &
python3 onee_check.py random 1500 15 30 92 1E > logs/rand_1E_15-30.txt 2>&1 &
python3 onee_check.py random 4000 4 12 93 kO > logs/rand_any_4-12.txt 2>&1 &
python3 onee_check.py files ../../../experiments/new/box41/lib41.txt 2 > logs/lib41.txt 2>&1 &
wait
for M in flip sbar early; do ONE_MUT=$M python3 onee_check.py random 500 4 12 94 1E > logs/mut_$M.txt 2>&1 & done
wait
