#!/bin/sh
# REFEREE-2 succ. 14: P-N5-NC batch (logs/). Usage: sh run_all.sh
cd "$(dirname "$0")"
L41=../../../experiments/new/box41/lib41.txt; KW=../R2-N5-KW/files.lst; B=../R2-N5-FBRED/box4344.lst; L2O=../R2-N5-2T/lib2o_noref.lst
python3 nc_check.py files $L41 3 > logs/lib41.txt 2>&1 &
python3 nc_check.py files $KW 3 > logs/files_kw.txt 2>&1 &
python3 nc_check.py files $B 6 > logs/box4344.txt 2>&1 &
python3 nc_check.py files $L2O 4 > logs/lib2o.txt 2>&1 &
python3 nc_check.py random 20000 5 12 191 k2 2 > logs/rand_k2.txt 2>&1 &
python3 nc_check.py random 10000 5 12 192 k3 2 > logs/rand_k3.txt 2>&1 &
python3 nc_check.py random 20000 2 5 193 kO 3 > logs/rand_small.txt 2>&1 &
wait
for M in b0 pc1 crd1; do NC_MUT=$M python3 nc_check.py random 20000 2 5 193 kO 3 > logs/mut_${M}_small.txt 2>&1 & done
NC_MUT=b0 python3 nc_check.py files $L41 3 > logs/mut_b0_lib41.txt 2>&1 &
wait
