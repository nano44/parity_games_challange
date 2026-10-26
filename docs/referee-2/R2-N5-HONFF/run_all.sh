#!/bin/bash
# REFEREE-2 successor 16: all HONFF runs (from docs/referee-2/R2-N5-HONFF). Logs in logs/.
cd "$(dirname "$0")"
X=../../../experiments
export BUDGET=${BUDGET:-3000000}
{
for f in j10_n24 j7_n32 j8_n32; do python3 honff_check.py start $X/red/xing/instances/$f.pg; done
for f in ffin12_n32 ffin5_n32 ffin4_n24; do python3 honff_check.py start $X/n5-epoch/instances/$f.pg $X/n5-epoch/instances/$f.start; done
python3 honff_check.py start $X/n5-exhaustive/instances/b5_o11.pg
python3 honff_check.py start $X/new/box46/instances/immp_cex_n11.pg $X/new/box46/instances/immp_cex_n11.start
} > logs/gap_instances.txt 2>&1
python3 honff_check.py files ../R2-N5-STAU/lib41_noref.lst 3 > logs/lib41_noref_x3.txt 2>&1 &
python3 honff_check.py files ../R2-N5-KW/files.lst 2 > logs/c1o_503_x2.txt 2>&1 &
python3 honff_check.py random 3000 5 12 1641 2 3 > logs/rand_k2_n5-12.txt 2>&1 &
python3 honff_check.py random 2000 6 14 1642 4 3 > logs/rand_k4_n6-14.txt 2>&1 &
wait
for M in ctrl b2; do HF_MUT=$M python3 honff_check.py files ../R2-N5-STAU/lib41_noref.lst 1 > logs/mut_$M.txt 2>&1; done
# the three gap instances over the default budget, at 3e7 (as the packet's §3)
BUDGET=30000000 python3 honff_check.py start $X/red/xing/instances/j7_n32.pg > logs/big_j7.txt 2>&1
BUDGET=30000000 python3 honff_check.py start $X/red/xing/instances/j8_n32.pg > logs/big_j8.txt 2>&1
BUDGET=30000000 python3 honff_check.py start $X/n5-epoch/instances/ffin12_n32.pg $X/n5-epoch/instances/ffin12_n32.start > logs/big_ffin12.txt 2>&1
BUDGET=150000000 python3 honff_check.py start $X/red/xing/instances/j7_n32.pg > logs/huge_j7.txt 2>&1
BUDGET=150000000 python3 honff_check.py start $X/red/xing/instances/j8_n32.pg > logs/huge_j8.txt 2>&1
BUDGET=150000000 python3 honff_check.py start $X/n5-epoch/instances/ffin12_n32.pg $X/n5-epoch/instances/ffin12_n32.start > logs/huge_ffin12.txt 2>&1
