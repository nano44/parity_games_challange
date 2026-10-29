#!/bin/bash
# REFEREE-2 successor 20: all MPGS runs (from docs/referee-2/R2-N5-MPGS-s20). Logs in logs/. Pinned lane re-runs: logs/pinned_check.txt (detached
# worktree at a23179b0, python3 -I). Runtimes: random/files/hn ~1-3 min; tau_5_10 ~10 min; alltau ~10-20 min.
cd "$(dirname "$0")"
python3 ../R2-N5-CORE/qcheck.py docs/lit/P-N5-MPGS.md a23179b0 > logs/quotes.txt 2>&1; SHIFT=1 python3 ../R2-N5-CORE/qcheck.py docs/lit/P-N5-MPGS.md a23179b0 > logs/quotes_shift1.txt 2>&1
python3 gs_check.py random 3000 5 14 11 3 > logs/rand_5_14.txt 2>&1 &
python3 gs_check.py random 600 15 24 12 2 > logs/rand_15_24.txt 2>&1 &
python3 gs_check.py files ../R2-N5-STAU/lib41_noref.lst 2 > logs/lib41.txt 2>&1 &
python3 gs_check.py files hn.lst 4 > logs/hn.txt 2>&1 &
python3 gs_check.py tau 40000 5 10 31 10 0.7 > logs/tau_5_10.txt 2>&1 &
python3 gs_check.py tau 20000 8 14 32 5 0.6 > logs/tau_8_14.txt 2>&1 &
FB1=0 python3 gs_check.py alltau 60000 4 8 42 0.7 > logs/alltau_4_8.txt 2>&1 &
FB1=0 python3 gs_check.py alltau 20000 8 11 43 0.75 > logs/alltau_8_11.txt 2>&1 &
python3 b1_general.py 400 7 > logs/b1_general.txt 2>&1 &
(cd ../R2-N5-MATCHPHI && python3 mphi_check.py comb 6 > ../R2-N5-MPGS-s20/logs/carry_comb6.txt 2>&1) &
wait
