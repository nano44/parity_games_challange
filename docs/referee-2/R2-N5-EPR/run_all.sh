#!/bin/sh
# REFEREE-2 succ. 14: P-N5-EPR batch (logs/). Usage: sh run_all.sh
cd "$(dirname "$0")"
L41=../../../experiments/new/box41/lib41.txt; KW=../R2-N5-KW/files.lst; B=../R2-N5-FBRED/box4344.lst; L2O=../R2-N5-2T/lib2o_noref.lst
python3 epr_check.py files $L41 3 > logs/lib41.txt 2>&1 &
python3 epr_check.py files $KW 3 > logs/files_kw.txt 2>&1 &
python3 epr_check.py files $B 6 > logs/box4344.txt 2>&1 &
python3 epr_check.py files $L2O 4 > logs/lib2o.txt 2>&1 &
python3 epr_check.py random 10000 4 12 223 3 > logs/rand_223.txt 2>&1 &
WITOUT=instances/lamend python3 epr_check.py random 3000 4 8 222 2 > logs/rand_222.txt 2>&1 &
wait
EP_MUT=d1 python3 epr_check.py files $L41 1 > logs/mut_d1_lib41.txt 2>&1
for w in D0 D1; do python3 epr_check.py start instances/lamend_$w.pg instances/lamend_$w.start > logs/witness_$w.txt 2>&1; done
for S in 231 232 233 234; do python3 epr_check.py climb 1500 5 9 $S climb/div_$S > logs/climb_$S.txt 2>&1 & done; wait
for S in 241 242 243 244; do python3 twin_search.py 3000 $S 4 9 6 instances/div_$S > logs/twin_$S.txt 2>&1 & done; wait
python3 epr_check.py start ../../../experiments/new/box45/instances/div_n8.pg instances/div_n8_conv.start > logs/div_n8.txt 2>&1
