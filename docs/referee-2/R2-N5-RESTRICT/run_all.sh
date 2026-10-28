#!/bin/bash
# REFEREE-2 successor 18: all RESTRICT runs (from docs/referee-2/R2-N5-RESTRICT). Logs in logs/.
cd "$(dirname "$0")"
X=../../../experiments
st() { if [ -f "${1%.pg}.start" ]; then python3 restrict_check.py start "$1" "${1%.pg}.start"; else python3 restrict_check.py start "$1"; fi; }
{
python3 restrict_check.py start $X/red/rec0/instances/nep90_n40.pg $X/si/rund/instances/nep90_n40.start
python3 restrict_check.py start $X/n5-epoch/instances/nep76_n40.pg $X/n5-epoch/instances/nep76_n40.start
python3 restrict_check.py start $X/new/box48/instances/long121_n40.pg $X/new/box48/instances/long121_n40.start
for f in $X/n5-epoch/results/climb/*.pg $X/red/ul/instances/*.pg; do st "$f"; done
} > logs/named.txt 2>&1 &
python3 restrict_check.py files ../R2-N5-STAU/lib41_noref.lst 3 > logs/lib41_x3.txt 2>&1 &
{
python3 restrict_check.py files ../R2-N5-ROOT/lib2o_noref.lst 5 > logs/lib2o_x5.txt 2>&1
python3 restrict_check.py files ../R2-N5-KW/files.lst 2 > logs/c1o_503_x2.txt 2>&1
} &
{
python3 restrict_check.py random 3000 6 14 4811 2 3 > logs/rand_k2_n6-14.txt 2>&1
python3 restrict_check.py random 2000 8 16 4812 4 3 > logs/rand_k4_n8-16.txt 2>&1
python3 restrict_check.py random 1500 8 18 4813 0 3 > logs/rand_kO_n8-18.txt 2>&1
} &
wait
