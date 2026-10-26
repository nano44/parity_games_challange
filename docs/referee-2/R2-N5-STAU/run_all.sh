#!/bin/bash
# REFEREE-2 succ. 15: batch for P-N5-STAU (stau_check.py); logs in logs/
cd "$(dirname "$0")"
python3 stau_check.py files ../R2-N5-KW/files.lst 3 > logs/kw503.txt 2>&1 &
python3 stau_check.py files lib41_noref.lst 3 > logs/lib41.txt 2>&1 &
python3 stau_check.py random 3000 5 20 22 1O 2 > logs/rand1O.txt 2>&1 &
python3 stau_check.py random 2000 4 16 31 kO 2 > logs/randkO.txt 2>&1 &
wait
python3 stau_check.py start ../../../experiments/new/box45/instances/div_n8.pg ../R2-N5-EPR/instances/div_n8_conv.start > logs/div_n8.txt 2>&1
ST_MUT=keep python3 stau_check.py random 300 5 16 41 kO 2 > logs/mut_keep.txt 2>&1 &
ST_MUT=sig python3 stau_check.py random 1500 5 16 41 kO 2 > logs/mut_sig.txt 2>&1 &
wait
touch logs/ALLDONE
