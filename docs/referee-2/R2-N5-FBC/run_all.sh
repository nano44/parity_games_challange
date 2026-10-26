#!/bin/bash
# REFEREE-2 successor 17: all FBC runs (from docs/referee-2/R2-N5-FBC). Logs in logs/. Never append to this file while it runs.
cd "$(dirname "$0")"
X=../../../experiments
export BUDGET=${BUDGET:-3000000}
{
for f in red/so/instances/s4c8_n13 red/xing/instances/j5_n16 red/xing/instances/j10_n24 red/xing/instances/j7_n32 red/xing/instances/j8_n32 \
         red/so/instances/farrise25_n32 si/xing/instances/zcl_rx_n32 new/box25/instances/wd16_s2 new/box25/laps/lap_n6_s1_110421 \
         si/orlens/instances/lev_l_x red/so/instances/rise_thin51_n40 n5-exhaustive/instances/b5_o11; do
  python3 fbc_check.py start $X/$f.pg; done
for f in ffin12_n32 ffin5_n32 ffin4_n24; do python3 fbc_check.py start $X/n5-epoch/instances/$f.pg $X/n5-epoch/instances/$f.start; done
python3 fbc_check.py start $X/new/box46/instances/immp_cex_n11.pg $X/new/box46/instances/immp_cex_n11.start
BUDGET=30000000 python3 fbc_check.py start $X/red/fbr/instances/fr39_q4_n48.pg $X/new/box47/instances/fr39_q4_n48.start
} > logs/named_instances.txt 2>&1 &
python3 fbc_check.py files ../R2-N5-STAU/lib41_noref.lst 3 > logs/lib41_noref_x3.txt 2>&1 &
python3 fbc_check.py files ../R2-N5-KW/files.lst 2 > logs/c1o_503_x2.txt 2>&1 &
{
python3 fbc_check.py random 3000 5 12 1741 2 3 > logs/rand_k2_n5-12.txt 2>&1
python3 fbc_check.py random 2000 6 14 1742 4 3 > logs/rand_k4_n6-14.txt 2>&1
python3 fbc_check.py random 1500 6 16 1743 0 3 > logs/rand_kO_n6-16.txt 2>&1
} &
wait
for M in plus2 tau sat; do FBC_MUT=$M python3 fbc_check.py files ../R2-N5-STAU/lib41_noref.lst 1 > logs/mut_$M.txt 2>&1; done
