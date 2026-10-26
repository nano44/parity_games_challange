#!/bin/bash
# REFEREE-2 successor 17: all CHOSEN runs (from docs/referee-2/R2-N5-CHOSEN). Logs in logs/. Never append to this file while it runs.
cd "$(dirname "$0")"
X=../../../experiments
export BUDGET=${BUDGET:-300000}
{
python3 chosen_check.py start $X/red/rec0/instances/nep90_n40.pg $X/si/rund/instances/nep90_n40.start
python3 chosen_check.py start $X/n5-epoch/instances/nep76_n40.pg $X/n5-epoch/instances/nep76_n40.start
python3 chosen_check.py start $X/red/n5inj/instances/frz40.pg $X/red/n5inj/instances/frz40.start
python3 chosen_check.py start $X/si/rund/instances/pp_K12_n161.pg $X/si/rund/instances/pp_K12_n161.start
python3 chosen_check.py start $X/red/usplit/instances/pp_K48_n449.pg $X/red/usplit/instances/pp_K48_n449.start
for f in red/rec0/instances/nep90_n40 n5-epoch/instances/nep76_n40 red/n5inj/instances/frz40; do python3 chosen_check.py start $X/$f.pg; done
} > logs/named_instances.txt 2>&1
python3 chosen_check.py files lib2o_noref.lst 5 > logs/lib2o_x5.txt 2>&1
python3 chosen_check.py files ../R2-N5-STAU/lib41_noref.lst 3 > logs/lib41_noref_x3.txt 2>&1 &
{
python3 chosen_check.py files ../R2-N5-KW/files.lst 2 > logs/c1o_503_x2.txt 2>&1
python3 chosen_check.py random 3000 5 12 1951 2 3 > logs/rand_k2_n5-12.txt 2>&1
python3 chosen_check.py random 2000 6 14 1952 4 3 > logs/rand_k4_n6-14.txt 2>&1
python3 chosen_check.py random 1500 6 16 1953 0 3 > logs/rand_kO_n6-16.txt 2>&1
} &
wait
for M in next noH; do CH_MUT=$M python3 chosen_check.py files ../R2-N5-STAU/lib41_noref.lst 1 > logs/mut_$M.txt 2>&1; done
