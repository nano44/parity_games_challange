#!/bin/bash
# REFEREE-2 successor 17: all ROOT runs (from docs/referee-2/R2-N5-ROOT). Logs in logs/. Never append to this file while it runs.
cd "$(dirname "$0")"
X=../../../experiments
export BUDGET=${BUDGET:-200000}
{
python3 root_check.py start $X/red/rec0/instances/nep90_n40.pg $X/si/rund/instances/nep90_n40.start
python3 root_check.py start $X/n5-epoch/instances/nep76_n40.pg $X/n5-epoch/instances/nep76_n40.start
python3 root_check.py start $X/red/n5inj/instances/frz40.pg $X/red/n5inj/instances/frz40.start
python3 root_check.py start $X/new/box48/instances/long121_n40.pg $X/new/box48/instances/long121_n40.start
} > logs/named_instances.txt 2>&1 &
python3 root_check.py files lib2o_noref.lst 5 > logs/lib2o_x5.txt 2>&1 &
python3 root_check.py files ../R2-N5-STAU/lib41_noref.lst 3 > logs/lib41_noref_x3.txt 2>&1 &
{
python3 root_check.py random 3000 5 12 1931 2 3 > logs/rand_k2_n5-12.txt 2>&1
python3 root_check.py random 2000 6 14 1932 4 3 > logs/rand_k4_n6-14.txt 2>&1
python3 root_check.py random 1500 6 16 1933 0 3 > logs/rand_kO_n6-16.txt 2>&1
python3 root_check.py files ../R2-N5-KW/files.lst 2 > logs/c1o_503_x2.txt 2>&1
} &
wait
for M in gs0 fa1 fg1 early; do ROOT_MUT=$M python3 root_check.py files ../R2-N5-STAU/lib41_noref.lst 1 > logs/mut_$M.txt 2>&1; done
