#!/bin/bash
# REFEREE-2 successor 19: all SDPRIME runs (from docs/referee-2/R2-N5-SDPRIME). Logs in logs/.
cd "$(dirname "$0")"; X=../../../experiments
python3 ../R2-N5-CORE/qcheck.py docs/si/P-N5-SDPRIME-box25.md edc14c51 > logs/quotes.txt 2>&1; SHIFT=1 python3 ../R2-N5-CORE/qcheck.py docs/si/P-N5-SDPRIME-box25.md edc14c51 > logs/quotes_shift1.txt 2>&1
python3 sdprime_check.py pairs $X/si/root/logs/alt_all.lst $X > logs/alt_all.txt 2>&1 &
python3 sdprime_check.py files ../R2-N5-STAU/lib41_noref.lst 3 > logs/lib41_x3.txt 2>&1 &
python3 sdprime_check.py pairs named.lst $X > logs/named.txt 2>&1 &
python3 sdprime_check.py random 3000 8 20 2501 0 3 > logs/rand_kO.txt 2>&1 &
python3 sdprime_check.py random 3000 6 16 2502 2 3 > logs/rand_k2.txt 2>&1 &
python3 sdprime_check.py random 2000 8 20 2503 4 3 > logs/rand_k4.txt 2>&1 &
for M in dm1 onlyW onlyH; do
  SD_MUT=$M python3 sdprime_check.py files ../R2-N5-STAU/lib41_noref.lst 3 > logs/mut_${M}_lib41.txt 2>&1 &
  SD_MUT=$M python3 sdprime_check.py random 3000 8 20 2501 0 3 > logs/mut_${M}_rand_kO.txt 2>&1 &
done
wait
