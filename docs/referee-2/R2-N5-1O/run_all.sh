#!/bin/sh
# REFEREE-2 succ. 13: P-N5-1O batch (logs/). Usage: sh run_all.sh
cd "$(dirname "$0")"
for s in 1 2 3 4; do python3 onecheck.py random 5000 4 14 $s > logs/random_$s.txt 2>&1 & done
for s in 1 2; do python3 onecheck.py general 2500 4 9 $s > logs/general_$s.txt 2>&1 & done
python3 onecheck.py files ../R2-N5-KW/files.lst 3 > logs/files_kw.txt 2>&1 &
wait
