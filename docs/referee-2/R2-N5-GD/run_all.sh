#!/bin/sh
# REFEREE-2 succ. 13: P-N5-GD batch (logs/). Usage: sh run_all.sh
cd "$(dirname "$0")"
python3 gd_check.py files ../../../experiments/new/box41/lib41.txt 3 > logs/lib41.txt 2>&1 &
python3 gd_check.py files ../R2-N5-KW/files.lst 2 > logs/files_kw.txt 2>&1 &
python3 gd_check.py files box43.lst 5 > logs/box43.txt 2>&1 &
python3 gd_check.py random 20000 4 14 61 > logs/rand_61.txt 2>&1 &
wait
for M in gda c2 f1 wo; do GD_MUT=$M python3 gd_check.py files ../../../experiments/new/box41/lib41.txt 1 > logs/mut_$M.txt 2>&1 & done
wait
