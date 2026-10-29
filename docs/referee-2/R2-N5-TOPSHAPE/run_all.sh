#!/bin/bash
# REFEREE-2 successor 19: all TOPSHAPE runs (from docs/referee-2/R2-N5-TOPSHAPE). Logs in logs/.
cd "$(dirname "$0")"; X=../../../experiments
python3 ../R2-N5-CORE/qcheck.py docs/new/P-N5-TOPSHAPE-box49.md 4c2ea43e > logs/quotes.txt 2>&1; SHIFT=1 python3 ../R2-N5-CORE/qcheck.py docs/new/P-N5-TOPSHAPE-box49.md 4c2ea43e > logs/quotes_shift1.txt 2>&1
python3 topshape_check.py pairs $X/si/root/logs/alt_all.lst $X > logs/alt_all.txt 2>&1 &
python3 topshape_check.py files ../R2-N5-STAU/lib41_noref.lst 3 > logs/lib41_x3.txt 2>&1 &
python3 topshape_check.py pairs named.lst $X > logs/named.txt 2>&1 &
python3 topshape_check.py random 5000 8 20 4901 0 3 > logs/rand_kO.txt 2>&1 &
python3 topshape_check.py random 5000 6 16 4902 2 3 > logs/rand_k2.txt 2>&1 &
wait
