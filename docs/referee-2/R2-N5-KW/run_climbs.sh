#!/bin/bash
# REFEREE-2 succ. 12: climbs against P-N5-KW (run from this directory); seed games are inputs only. All four start together, after
# the N-KW-4 (r = 1) checker fix; an earlier set (22:2xZ) was discarded: it stopped on that checker artifact.
cd "$(dirname "$0")"; rm -rf climb; mkdir -p climb
python3 kw_climb.py kw 13001 8 16 1200 ../../../experiments/si/kw15/climb/best_kind3_1541.pg > climb/kw_13001.txt 2>&1 &
python3 kw_climb.py kw 13002 8 16 1200 ../../../experiments/si/kw15/climb/best_kind2_1521.pg > climb/kw_13002.txt 2>&1 &
python3 kw_climb.py casc 13003 8 16 1200 ../../../experiments/si/kw15/climb/best_long_1513.pg > climb/casc_13003.txt 2>&1 &
python3 kw_climb.py kw 13004 10 18 1200 > climb/kw_13004.txt 2>&1 &
wait
./run_mut.sh
python3 kw_check.py random 3000 6 16 13100 own > logs/random_own_13100.log 2>&1
echo DONE > climb/ALLDONE
