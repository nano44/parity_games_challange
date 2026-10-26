#!/bin/sh
# REFEREE-2 succ. 13: P-N5-VILB + P-N5-ACCEL batch (logs/), then epoch climbs (climb/). Usage: sh run_all.sh
cd "$(dirname "$0")"
python3 va_check.py files ../../../experiments/new/box41/lib41.txt 3 > logs/lib41.txt 2>&1 &
python3 va_check.py files ../R2-N5-KW/files.lst 2 > logs/files_kw.txt 2>&1 &
python3 va_check.py files box4344.lst 5 > logs/box4344.txt 2>&1 &
python3 va_check.py random 20000 4 12 101 > logs/rand_101.txt 2>&1 &
wait
for M in vi sg ep kk; do VA_MUT=$M python3 va_check.py files ../../../experiments/new/box41/lib41.txt 1 > logs/mut_$M.txt 2>&1 & done
wait
for s in 111 112 113 114; do timeout 1800 python3 va_check.py climb 3000 4 7 $s climb/ep_$s > logs/climb_$s.txt 2>&1 & done
wait
