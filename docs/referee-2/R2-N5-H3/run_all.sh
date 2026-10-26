#!/bin/sh
# REFEREE-2 succ. 14: P-N5-H3 batch (logs/). Usage: sh run_all.sh
cd "$(dirname "$0")"
L41=../../../experiments/new/box41/lib41.txt; KW=../R2-N5-KW/files.lst; B=../R2-N5-FBRED/box4344.lst; L2O=../R2-N5-2T/lib2o_noref.lst
X=../../../experiments/n5-exhaustive/instances
python3 h3_check.py files $L41 3 > logs/lib41.txt 2>&1 &
python3 h3_check.py files $KW 3 > logs/files_kw.txt 2>&1 &
python3 h3_check.py files $B 6 > logs/box4344.txt 2>&1 &
python3 h3_check.py files $L2O 4 > logs/lib2o.txt 2>&1 &
python3 h3_check.py random 20000 5 12 191 k2 2 > logs/rand_k2.txt 2>&1 &
python3 h3_check.py random 10000 5 12 192 k3 2 > logs/rand_k3.txt 2>&1 &
python3 h3_check.py random 20000 2 6 193 kO 3 > logs/rand_small.txt 2>&1 &
python3 h3_check.py start $X/frz1_n24.pg $X/frz1_n24.start > logs/frz1_n24.txt 2>&1 &
wait
for M in b0 pc1 crd1 c2l; do NC_MUT=$M python3 h3_check.py random 20000 2 6 193 kO 3 > logs/mut_${M}_small.txt 2>&1 & done
NC_MUT=c2l python3 h3_check.py files $L41 3 > logs/mut_c2l_lib41.txt 2>&1 &
wait
W=instances/pft34_h3u_P32
python3 h3_check.py start $W.pg ${W}_t33.start > logs/witness_h3u.txt 2>&1
for M in crd1 c2l; do NC_MUT=$M python3 h3_check.py start $W.pg ${W}_t33.start > logs/witness_mut_$M.txt 2>&1; done
