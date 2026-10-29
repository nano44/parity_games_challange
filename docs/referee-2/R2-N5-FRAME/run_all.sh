#!/bin/bash
# REFEREE-2 successor 21: all P-N5-FRAME runs (from docs/referee-2/R2-N5-FRAME). Logs in logs/.
cd "$(dirname "$0")"
T=${TMPDIR:-/tmp}
python3 fquote.py > logs/quotes.txt 2>&1; SHIFT=1 python3 fquote.py > logs/quotes_shift1.txt 2>&1
BF=8 python3 frame_check.py random 1500 3 8 21 3 > logs/rand_bf_3_8.txt 2>&1 &
python3 frame_check.py random 2000 6 14 22 3 > logs/rand_6_14.txt 2>&1 &
python3 frame_check.py random 300 15 30 23 2 > logs/rand_15_30.txt 2>&1 &
python3 frame_check.py files mkr.lst 2 experiments/ > logs/mkr.txt 2>&1 &
python3 frame_check.py files dual.lst 2 experiments/ > logs/dual.txt 2>&1 &
split -n l/8 -d ../../../experiments/new/box59/sbcg.lst $T/frsb_; for i in 0 1 2 3 4 5 6 7; do PROGRESS=1 python3 frame_check.py files $T/frsb_0$i 1 experiments/ > logs/sbcg_part$i.txt 2>&1 & done
wait
