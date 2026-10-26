#!/bin/sh
# REFEREE-2 succ. 13: P-N5-NH-box42 batch (logs/). Usage: sh run_all.sh
cd "$(dirname "$0")"
python3 nh42_check.py files ../R2-N5-KW/files.lst 3 spec > logs/files_spec.txt 2>&1 &
python3 nh42_check.py files ../R2-N5-KW/files.lst 2 own > logs/files_own.txt 2>&1 &
python3 nh42_check.py random 4000 6 16 4213 spec > logs/random_spec.txt 2>&1 &
python3 nh42_check.py random 3000 6 16 4214 own > logs/random_own.txt 2>&1 &
wait
for M in sw run stc nr; do NH_MUT=$M python3 nh42_check.py files ../R2-N5-KW/files.lst 1 spec > logs/mut_$M.txt 2>&1 & done
wait
