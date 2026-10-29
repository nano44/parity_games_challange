#!/bin/bash
# REFEREE-2 successor 20: all COMPOSE runs (from docs/referee-2/R2-N5-COMPOSE). Logs in logs/. Pinned lane re-runs: logs/pinned_check.txt
# (detached worktree at l-si 3ca0932d, python3 -I). Runtimes: random ~2-5 min, alt_all ~3 min, named ~5 min, lib41 ~15 min.
cd "$(dirname "$0")"
python3 ../R2-N5-CORE/qcheck.py docs/si/P-N5-COMPOSE-box28.md 3ca0932d > logs/quotes.txt 2>&1; SHIFT=1 python3 ../R2-N5-CORE/qcheck.py docs/si/P-N5-COMPOSE-box28.md 3ca0932d > logs/quotes_shift1.txt 2>&1
python3 compose_check.py random 3000 4 14 11 3 > logs/rand_4_14.txt 2>&1 &
python3 compose_check.py random 500 15 30 12 2 > logs/rand_15_30.txt 2>&1 &
python3 compose_check.py files ../R2-N5-STAU/lib41_noref.lst 2 > logs/lib41.txt 2>&1 &
python3 compose_check.py files ../../../experiments/si/root/logs/alt_all.lst 0 experiments/ > logs/alt_all.txt 2>&1 &
python3 compose_check.py files named.lst 2 > logs/named.txt 2>&1 &
wait
