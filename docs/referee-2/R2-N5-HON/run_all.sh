#!/bin/bash
# REFEREE-2 successor 16: all HON runs (from docs/referee-2/R2-N5-HON). Logs in logs/.
cd "$(dirname "$0")"
X=../../../experiments
{
python3 hon_check.py start $X/new/box46/instances/immp_cex_n11.pg $X/new/box46/instances/immp_cex_n11.start
for f in $X/new/box46/instances/immfail_n14.pg $X/n5-exhaustive/instances/b5_o11.pg $X/n5-exhaustive/instances/b4_n5_other_0.pg \
         $X/si/orlens/instances/thclimb_n12_s11.pg $X/red/so/instances/so_th_n32.pg $X/red/so/instances/exitr_cex_n16.pg; do python3 hon_check.py start $f; done
python3 hon_check.py start $X/new/box45/instances/div_n8.pg $X/new/box45/instances/div_n8.start
} > logs/instances.txt 2>&1
python3 hon_check.py files ../R2-N5-STAU/lib41_noref.lst 3 > logs/lib41_noref_x3.txt 2>&1 &
python3 hon_check.py files ../R2-N5-KW/files.lst 2 > logs/c1o_503_x2.txt 2>&1 &
python3 hon_check.py random 3000 5 11 1621 2 3 > logs/rand_k2_n5-11.txt 2>&1 &
python3 hon_check.py random 2000 6 11 1622 3 3 > logs/rand_k3_n6-11.txt 2>&1 &
wait
python3 hon_check.py random 1500 8 11 1623 4 3 > logs/rand_k4_n8-11.txt 2>&1
python3 hon_check.py random 800 12 20 1624 0 2 > logs/rand_kO_n12-20.txt 2>&1
for M in hon fb4 ru r1 s1; do HN_MUT=$M python3 hon_check.py files ../R2-N5-STAU/lib41_noref.lst 1 > logs/mut_$M.txt 2>&1; done
