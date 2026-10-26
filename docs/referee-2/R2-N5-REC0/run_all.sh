#!/bin/bash
# REFEREE-2 succ. 15: batch for P-N5-REC0 (rec0_check.py); logs in logs/
cd "$(dirname "$0")"
python3 rec0_check.py random 5000 4 11 51 kO 3 > logs/randkO.txt 2>&1 &
python3 rec0_check.py random 5000 5 11 52 1O 3 > logs/rand1O.txt 2>&1 &
python3 rec0_check.py files ../R2-N5-KW/files.lst 3 > logs/kw503.txt 2>&1 &
python3 rec0_check.py files ../R2-N5-STAU/lib41_noref.lst 3 > logs/lib41.txt 2>&1 &
wait
RC_MUT=step2 python3 rec0_check.py random 500 4 10 53 kO 2 > logs/mut_step2.txt 2>&1
RC_MUT=full python3 rec0_check.py random 500 4 10 53 kO 2 > logs/mut_full.txt 2>&1
RC_MUT=nosat python3 rec0_check.py random 500 4 10 53 kO 2 > logs/mut_nosat.txt 2>&1
touch logs/ALLDONE
