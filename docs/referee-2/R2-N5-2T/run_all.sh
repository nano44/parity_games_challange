#!/bin/sh
# REFEREE-2 succ. 14: P-N5-2T batch (logs/). Usage: sh run_all.sh
cd "$(dirname "$0")"
L41=../../../experiments/new/box41/lib41.txt; KW=../R2-N5-KW/files.lst; B=../R2-N5-FBRED/box4344.lst; L2O=lib2o_noref.lst
python3 tt_check.py files $L41 2 > logs/lib41.txt 2>&1 &
python3 tt_check.py files $KW 2 > logs/files_kw.txt 2>&1 &
python3 tt_check.py files $B 5 > logs/box4344.txt 2>&1 &
python3 tt_check.py files $L2O 3 > logs/lib2o.txt 2>&1 &
python3 tt_check.py random 20000 4 12 141 > logs/rand_141.txt 2>&1 &
for G in g3 g4 g4b g5 g5c; do python3 tt_check.py union $B $G 3 > logs/union_box_$G.txt 2>&1 & done
wait
for M in pfz2 dircyc sat0 satcyc satalpha; do TT_MUT=$M python3 tt_check.py union $B g4 3 > logs/mut_${M}_g4.txt 2>&1 & done
for G in g5 g5c; do for M in satalpha satcyc sat0 dircyc; do TT_MUT=$M python3 tt_check.py union $B $G 3 > logs/mut_${M}_$G.txt 2>&1 & done; done
wait
python3 tt_check.py files witness.lst 1 > logs/witness.txt 2>&1
for M in sat0 satalpha; do TT_MUT=$M python3 tt_check.py files witness.lst 1 > logs/witness_mut_$M.txt 2>&1; done
