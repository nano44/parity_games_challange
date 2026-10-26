#!/bin/bash
# REFEREE-2 successor 17: all EPC runs (from docs/referee-2/R2-N5-EPC). Logs in logs/. Never append to this file while it runs.
cd "$(dirname "$0")"
X=../../../experiments
export BUDGET=${BUDGET:-3000000}
{
python3 epc_check.py start $X/new/box48/instances/long121_n40.pg $X/new/box48/instances/long121_n40.start
python3 epc_check.py start $X/red/rec0/instances/nep90_n40.pg $X/si/rund/instances/nep90_n40.start
python3 epc_check.py start $X/n5-epoch/instances/nep76_n40.pg $X/n5-epoch/instances/nep76_n40.start
for r in 0 1 2 3 4 5 6 7; do python3 epc_check.py start $X/red/fbr/instances/rho3_253_n32.pg $r 17$r; done
for f in new/esc/instances/cond_stuck_symsi3_YE red/carry/instances/gapb_dup_n20; do for r in 0 1 2; do python3 epc_check.py start $X/$f.pg $r 27$r; done; done
} > logs/named_instances.txt 2>&1 &
python3 epc_check.py files ../R2-N5-STAU/lib41_noref.lst 3 > logs/lib41_noref_x3.txt 2>&1 &
python3 epc_check.py files ../R2-N5-KW/files.lst 2 > logs/c1o_503_x2.txt 2>&1 &
{
python3 epc_check.py random 3000 5 14 1841 2 3 > logs/rand_k2_n5-14.txt 2>&1
python3 epc_check.py random 2000 6 16 1842 4 3 > logs/rand_k4_n6-16.txt 2>&1
python3 epc_check.py random 1500 6 18 1843 0 3 > logs/rand_kO_n6-18.txt 2>&1
} &
wait
for M in plus2 nonC last noR0; do EPC_MUT=$M python3 epc_check.py files ../R2-N5-STAU/lib41_noref.lst 1 > logs/mut_$M.txt 2>&1; done
