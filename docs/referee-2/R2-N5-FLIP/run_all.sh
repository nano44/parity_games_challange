#!/bin/bash
# REFEREE-2 successor 16: all FLIP runs (from docs/referee-2/R2-N5-FLIP). Logs in logs/.
cd "$(dirname "$0")"
X=../../../experiments
{
python3 flip_check.py start $X/red/n5inj/instances/frz40.pg $X/red/n5inj/instances/frz40.start
python3 flip_check.py start $X/si/rund/instances/pp_K12_n161.pg $X/si/rund/instances/pp_K12_n161.start
python3 flip_check.py start $X/red/usplit/instances/pp_K48_n449.pg $X/red/usplit/instances/pp_K48_n449.start
python3 flip_check.py start $X/red/so/instances/so_th_n32.pg
} > logs/instances.txt 2>&1
echo $X/red/tcpert/instances/leanT_N6.pg | sed 's|^\.\./\.\./\.\./||' > logs/leanT.lst
python3 flip_check.py files logs/leanT.lst 5 > logs/leanT_N6_x5.txt 2>&1
python3 flip_check.py files ../R2-N5-STAU/lib41_noref.lst 3 > logs/lib41_noref_x3.txt 2>&1 &
python3 flip_check.py files ../R2-N5-KW/files.lst 2 > logs/c1o_503_x2.txt 2>&1 &
python3 flip_check.py random 3000 5 12 1631 2 3 > logs/rand_k2_n5-12.txt 2>&1 &
python3 flip_check.py random 2000 6 12 1632 4 3 > logs/rand_k4_n6-12.txt 2>&1 &
wait
for M in root cost lev; do FL_MUT=$M python3 flip_check.py start $X/si/rund/instances/pp_K12_n161.pg $X/si/rund/instances/pp_K12_n161.start > logs/mut_${M}_ppK12.txt 2>&1; done
for M in cost lev; do FL_MUT=$M python3 flip_check.py random 3000 5 12 1631 2 3 > logs/mut_${M}_rand.txt 2>&1; FL_MUT=$M python3 flip_check.py files ../R2-N5-STAU/lib41_noref.lst 1 > logs/mut_${M}_lib41.txt 2>&1; done
