#!/bin/sh
# REFEREE-2 succ. 13: P-N5-FBRED batch (logs/, climb/). Usage: sh run_all.sh
cd "$(dirname "$0")"
python3 fbred_check.py files ../../../experiments/new/box41/lib41.txt 3 > logs/lib41.txt 2>&1 &
python3 fbred_check.py files ../R2-N5-KW/files.lst 2 > logs/files_kw.txt 2>&1 &
python3 fbred_check.py files box4344.lst 5 > logs/box4344.txt 2>&1 &
python3 fbred_check.py random 20000 4 12 71 > logs/rand_71.txt 2>&1 &
wait
for M in fex red yf cno; do FB_MUT=$M python3 fbred_check.py files ../../../experiments/new/box41/lib41.txt 1 > logs/mut_$M.txt 2>&1 & done
wait
