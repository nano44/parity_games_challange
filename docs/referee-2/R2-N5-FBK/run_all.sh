#!/bin/sh
# REFEREE-2 succ. 14: P-N5-FBK batch (logs/). Usage: sh run_all.sh
cd "$(dirname "$0")"
L41=../../../experiments/new/box41/lib41.txt; KW=../R2-N5-KW/files.lst; B=../R2-N5-FBRED/box4344.lst; L2O=../R2-N5-2T/lib2o_noref.lst
python3 fbk_check.py files $L41 2 > logs/lib41.txt 2>&1 &
python3 fbk_check.py files $KW 2 > logs/files_kw.txt 2>&1 &
python3 fbk_check.py files $B 5 > logs/box4344.txt 2>&1 &
python3 fbk_check.py files $L2O 3 > logs/lib2o.txt 2>&1 &
python3 fbk_check.py random 20000 4 12 161 > logs/rand_161.txt 2>&1 &
for G in k3 g5 g5c; do python3 fbk_check.py union $B $G 3 > logs/union_box_$G.txt 2>&1 & done
wait
for M in satk0 shift altstrict; do FK_MUT=$M python3 fbk_check.py union $B k3 3 > logs/mut_${M}_k3.txt 2>&1 & done
FK_MUT=altstrict python3 fbk_check.py files $L41 1 > logs/mut_altstrict_lib41.txt 2>&1 &
wait
python3 fbk_check.py files witness.lst 1 > logs/witness.txt 2>&1
