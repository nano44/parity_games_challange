#!/bin/bash
# REFEREE-2 successor 18: all GCX runs (from docs/referee-2/R2-N5-GCX). Logs in logs/.
cd "$(dirname "$0")"
X=../../../experiments
st() { if [ -f "${1%.pg}.start" ]; then python3 gcx_check.py start "$1" "${1%.pg}.start"; else python3 gcx_check.py start "$1"; fi; }
{
for f in $X/red/ul/instances/*.pg $X/si/root/instances/cone_n69.pg $X/red/so/instances/so_th_n32.pg $X/red/n5inj/instances/phase2_pk48.pg \
         $X/red/xing/instances/x32_waves48.pg $X/red/fbr/instances/twowave_L16.pg $X/si/rund/instances/*.pg; do st "$f"; done
python3 gcx_check.py start $X/red/rec0/instances/nep90_n40.pg $X/si/rund/instances/nep90_n40.start
python3 gcx_check.py start $X/n5-epoch/instances/nep76_n40.pg $X/n5-epoch/instances/nep76_n40.start
} > logs/named.txt 2>&1 &
{ for f in $X/red/usplit/instances/gate_K16_n197.pg; do st "$f"; done; } > logs/named_big.txt 2>&1 &
python3 gcx_check.py files ../R2-N5-STAU/lib41_noref.lst 5 > logs/lib41_x5.txt 2>&1 &
{
python3 gcx_check.py files ../R2-N5-ROOT/lib2o_noref.lst 5 > logs/lib2o_x5.txt 2>&1
python3 gcx_check.py random 3000 6 16 2111 2 3 > logs/rand_k2_n6-16.txt 2>&1
python3 gcx_check.py random 2000 8 20 2112 4 3 > logs/rand_k4_n8-20.txt 2>&1
python3 gcx_check.py random 1500 8 20 2113 0 3 > logs/rand_kO_n8-20.txt 2>&1
python3 gcx_check.py random 400 20 36 2114 5 2 > logs/rand_k5_n20-36.txt 2>&1
} &
wait
