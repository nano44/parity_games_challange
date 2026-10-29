#!/bin/bash
# REFEREE-2 successor 19: all REL runs (from docs/referee-2/R2-N5-REL). Logs in logs/.
cd "$(dirname "$0")"; X=../../../experiments
python3 ../R2-N5-CORE/qcheck.py docs/si/P-N5-REL-box25.md 07f19760 > logs/quotes.txt 2>&1; SHIFT=1 python3 ../R2-N5-CORE/qcheck.py docs/si/P-N5-REL-box25.md 07f19760 > logs/quotes_shift1.txt 2>&1
python3 rel_check.py pairs $X/si/root/logs/alt_all.lst $X > logs/alt_all.txt 2>&1 &
python3 rel_check.py files ../R2-N5-STAU/lib41_noref.lst 3 > logs/lib41_x3.txt 2>&1 &
python3 rel_check.py pairs ../R2-N5-SDPRIME/named.lst $X > logs/named.txt 2>&1 &
python3 rel_check.py pairs grun.lst inst > logs/grun_inst.txt 2>&1 &
python3 rel_check.py random 3000 8 20 2601 0 3 > logs/rand_kO.txt 2>&1 &
python3 rel_check.py random 3000 6 16 2602 2 3 > logs/rand_k2.txt 2>&1 &
for M in y2rise thru tie cyc dm1 nosbar qonly; do
  REL_MUT=$M python3 rel_check.py files ../R2-N5-STAU/lib41_noref.lst 3 > logs/mut_${M}_lib41.txt 2>&1 &
done
wait
