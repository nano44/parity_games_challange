#!/bin/bash
# REFEREE-2 successor 20: all P-N5-SF runs (from docs/referee-2/R2-N5-SF). Logs in logs/. Pinned lane re-runs: logs/pinned_check.txt
# (check.sh box 55 commands in a detached worktree at l-new 95a7a581, python3 -I). hard.lst is a copy of experiments/new/box55/hard.lst @ 95a7a581.
cd "$(dirname "$0")"
python3 ../R2-N5-CORE/qcheck.py docs/new/P-N5-SF-box55.md 95a7a581 > logs/quotes.txt 2>&1; SHIFT=1 python3 ../R2-N5-CORE/qcheck.py docs/new/P-N5-SF-box55.md 95a7a581 > logs/quotes_shift1.txt 2>&1
# the three pins one at a time (ROW figures compared by hand with the lane's in the report)
for l in 1 2 3; do sed -n "${l}p" pins.lst > /tmp/sf_pin_$l.lst; echo "== pin $l: $(cat /tmp/sf_pin_$l.lst)"; python3 sf_check.py files /tmp/sf_pin_$l.lst $([ $l = 2 ] && echo 1 || echo 0); done > logs/pins.txt 2>&1
python3 sf_check.py random 3000 4 14 11 3 > logs/rand_4_14.txt 2>&1 &
python3 sf_check.py random 400 15 30 12 2 > logs/rand_15_30.txt 2>&1 &
python3 sf_check.py files ../R2-N5-STAU/lib41_noref.lst 2 > logs/lib41.txt 2>&1 &
python3 sf_check.py files ../../../experiments/si/root/logs/alt_all.lst 0 experiments/ > logs/alt_all.txt 2>&1 &
python3 sf_check.py files fam.lst 1 experiments/ > logs/fam.txt 2>&1 &
python3 sf_check.py files hard.lst 1 experiments/ > logs/hard.txt 2>&1 &
wait
