#!/bin/sh
# REFEREE-2 succ. 14: P-N5-XEP batch (logs/). Usage: sh run_all.sh
cd "$(dirname "$0")"
L41=../../../experiments/new/box41/lib41.txt; KW=../R2-N5-KW/files.lst; B=../R2-N5-FBRED/box4344.lst; L2O=../R2-N5-2T/lib2o_noref.lst
python3 xep_check.py files $L41 3 > logs/lib41.txt 2>&1 &
python3 xep_check.py files $L41 1 > logs/lib41_s3.txt 2>&1 &
python3 xep_check.py files $KW 3 > logs/files_kw.txt 2>&1 &
python3 xep_check.py files $B 6 > logs/box4344.txt 2>&1 &
python3 xep_check.py files $L2O 4 > logs/lib2o.txt 2>&1 &
python3 xep_check.py random 10000 4 12 181 2 > logs/rand_181.txt 2>&1 &
wait
for M in rstick_all xsn0; do XP_MUT=$M python3 xep_check.py files $L41 3 > logs/mut_$M.txt 2>&1 & done
wait
