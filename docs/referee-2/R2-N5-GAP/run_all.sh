#!/bin/bash
# REFEREE-2 successor 21: P-N5-GAP runs (from docs/referee-2/R2-N5-GAP). Logs in logs/. Pinned: check.sh l. 315-332 at l-new 28ceeadc in a
# detached worktree under set -euo pipefail -> logs/pinned_check.txt. sbcg split as in R2-N5-CUT (n <= 100 / n > 100 lists in $T).
cd "$(dirname "$0")"; T=${TMPDIR:-/tmp}
python3 gquote.py > logs/quotes.txt; SHIFT=1 python3 gquote.py | tail -1 > logs/quotes_shift1.txt
python3 case2u.py 7 case2u_inst.pg > logs/case2u.txt
python3 gap_check.py onep 3000 3 9 61 > logs/onep_3_9.txt 2>&1
python3 gap_check.py onep 500 10 25 63 > logs/onep_10_25.txt 2>&1
python3 gap_check.py files named.lst 2 experiments/ > logs/named.txt 2>&1
split -n l/2 -d ../../../experiments/si/root/logs/alt_all.lst $T/ga_
for i in 0 1; do PROGRESS=1 python3 gap_check.py files $T/ga_0$i 0 experiments/ > logs/alt_all$i.txt 2>&1 & done
PROGRESS=1 python3 gap_check.py files $T/cs_small 1 experiments/ > logs/sbcg_small.txt 2>&1 &
PROGRESS=1 python3 gap_check.py files $T/cs_big 1 experiments/ > logs/sbcg_big.txt 2>&1 &
wait
python3 gap_check.py random 2000 5 14 64 2 > logs/rand_5_14.txt 2>&1
