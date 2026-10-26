#!/bin/sh
# REFEREE-2 succ. 13: P-N5-DUAL batch (logs/). Usage: sh run_all.sh
cd "$(dirname "$0")"
python3 dual_check.py files ../../../experiments/new/box41/lib41.txt 2 > logs/lib41.txt 2>&1 &
python3 dual_check.py files ../R2-N5-KW/files.lst 2 > logs/files_kw.txt 2>&1 &
python3 dual_check.py random 2000 4 14 51 kO > logs/rand_kO.txt 2>&1 &
python3 dual_check.py random 2000 4 14 52 1E > logs/rand_1E.txt 2>&1 &
wait
python3 dual_check.py random 2000 4 14 53 1O > logs/rand_1O.txt 2>&1 &
for M in plain phi endg; do DU_MUT=$M python3 dual_check.py files ../../../experiments/new/box41/lib41.txt 1 > logs/mut_$M.txt 2>&1 & done
wait
