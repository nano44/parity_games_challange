#!/bin/bash
# REFEREE-2 successor 19: all CORE runs (from docs/referee-2/R2-N5-CORE). Logs in logs/. ~2 min in parallel.
cd "$(dirname "$0")"; X=../../../experiments
python3 qcheck.py ../../si/P-N5-CORE-box23.md > logs/quotes.txt 2>&1; SHIFT=1 python3 qcheck.py ../../si/P-N5-CORE-box23.md > logs/quotes_shift1.txt 2>&1
python3 core_check.py pairs $X/si/root/logs/alt_all.lst $X > logs/alt_all.txt 2>&1 &
python3 core_check.py files ../R2-N5-STAU/lib41_noref.lst 3 > logs/lib41_x3.txt 2>&1 &
python3 core_check.py pairs named.lst $X > logs/named.txt 2>&1 &
python3 core_check.py random 3000 6 16 1901 2 3 > logs/rand_k2_n6-16.txt 2>&1 &
python3 core_check.py random 1500 8 20 1902 0 3 > logs/rand_kO_n8-20.txt 2>&1 &
python3 core_check.py random 400 20 36 1903 5 2 > logs/rand_k5_n20-36.txt 2>&1 &
RULE=rand python3 core_check.py files ../R2-N5-STAU/lib41_noref.lst 3 > logs/lib41_x3_rand.txt 2>&1 &
wait
