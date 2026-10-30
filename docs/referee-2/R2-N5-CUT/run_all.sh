#!/bin/bash
# REFEREE-2 successor 21: P-N5-CUT runs (from docs/referee-2/R2-N5-CUT). Logs in logs/. Pinned: check.sh l. 797-813 at l-si 2678f6c6 in a
# detached worktree under set -euo pipefail -> logs/pinned_check.txt. sbcg split at n <= 100 / n > 100 (as run; $T lists built from
# experiments/new/box59/sbcg.lst, identical to experiments/si/odd/sbcg.lst).
cd "$(dirname "$0")"; T=${TMPDIR:-/tmp}
python3 ../R2-N5-CORE/qcheck.py docs/si/P-N5-CUT-box43.md 2678f6c6 > logs/quotes.txt 2>&1; SHIFT=1 python3 ../R2-N5-CORE/qcheck.py docs/si/P-N5-CUT-box43.md 2678f6c6 > logs/quotes_shift1.txt 2>&1
python3 cut_check.py files pins.lst 1 experiments/ > logs/pins.txt 2>&1
for i in 0 1; do PROGRESS=1 python3 cut_check.py files $T/csm_0$i 1 experiments/ > logs/sbcg_small$i.txt 2>&1 & done
PROGRESS=1 OO1S=10 python3 cut_check.py files $T/cs_big 1 experiments/ > logs/sbcg_big.txt 2>&1 &
( DUMP=1 python3 cut_check.py files red.lst 1 experiments/ > logs/red.txt 2>&1; DUMP=1 python3 cut_check.py files hn.lst 1 experiments/ > logs/hn.txt 2>&1;
  DUMP=1 python3 cut_check.py files latew.lst 1 > logs/latew.txt 2>&1; python3 cut_check.py random 3000 5 14 41 2 > logs/rand_5_14.txt 2>&1;
  python3 cut_check.py random 300 15 30 42 2 > logs/rand_15_30.txt 2>&1 ) &
wait
