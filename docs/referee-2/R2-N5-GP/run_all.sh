#!/bin/bash
# REFEREE-2 successor 20: all P-N5-GP runs (from docs/referee-2/R2-N5-GP). Logs in logs/. Pinned lane re-runs: logs/pinned_check.txt
# (check.sh l. 699-710 in a detached worktree at l-si d072bb28, python3 -I). lib41 runs in 8 chunks (split -n l/8), PROGRESS=1 prints DONE-FILE.
cd "$(dirname "$0")"
python3 ../R2-N5-CORE/qcheck.py docs/si/P-N5-GP-box31.md d072bb28 > logs/quotes.txt 2>&1; SHIFT=1 python3 ../R2-N5-CORE/qcheck.py docs/si/P-N5-GP-box31.md d072bb28 > logs/quotes_shift1.txt 2>&1
python3 gp_check.py random 3000 4 14 11 3 > logs/rand_4_14.txt 2>&1 &
python3 gp_check.py random 400 15 30 12 2 > logs/rand_15_30.txt 2>&1 &
python3 gp_check.py files ../../../experiments/si/root/logs/alt_all.lst 0 experiments/ > logs/alt_all.txt 2>&1 &
sed -n 1p named.lst > /tmp/gp1.lst; python3 gp_check.py files /tmp/gp1.lst 1 > logs/ccl.txt 2>&1 &
sed -n 2p named.lst > /tmp/gp2.lst; python3 gp_check.py files /tmp/gp2.lst 0 > logs/rlin.txt 2>&1 &
python3 gp_check.py files named.lst 1 > logs/named.txt 2>&1 &
split -n l/8 -d ../R2-N5-STAU/lib41_noref.lst /tmp/gplib_; for i in 0 1 2 3 4 5 6 7; do PROGRESS=1 python3 gp_check.py files /tmp/gplib_0$i 2 > logs/lib41_part$i.txt 2>&1 & done
wait
