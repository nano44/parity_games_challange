#!/bin/bash
# REFEREE-2 successor 19: all FBCK runs (from docs/referee-2/R2-N5-FBCK). Logs in logs/.
cd "$(dirname "$0")"; X=../../../experiments
python3 ../R2-N5-CORE/qcheck.py ../../new/P-N5-FBCK-box49.md > logs/quotes.txt 2>&1; SHIFT=1 python3 ../R2-N5-CORE/qcheck.py ../../new/P-N5-FBCK-box49.md > logs/quotes_shift1.txt 2>&1
BUDGET=3000000 python3 fbck_check.py pairs named.lst $X > logs/named.txt 2>&1 &
python3 fbck_check.py files ../R2-N5-STAU/lib41_noref.lst 3 > logs/lib41_x3.txt 2>&1 &
python3 fbck_check.py dress 20000 8 18 11 4 6 3 > logs/dress_k4.txt 2>&1 &
python3 fbck_check.py dress 20000 8 18 12 0 6 3 > logs/dress_kO.txt 2>&1 &
python3 fbck_check.py random 20000 6 16 13 2 3 > logs/rand_k2.txt 2>&1 &
python3 fbck_check.py random 10000 8 20 14 0 3 > logs/rand_kO.txt 2>&1 &
for M in plus2 tau open1 nk1; do
  FBCK_MUT=$M python3 fbck_check.py dress 20000 8 18 11 4 6 3 > logs/mut_${M}_dress_k4.txt 2>&1 &
  FBCK_MUT=$M python3 fbck_check.py random 10000 8 20 14 0 3 > logs/mut_${M}_rand_kO.txt 2>&1 &
done
wait
