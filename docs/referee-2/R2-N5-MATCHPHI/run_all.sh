#!/bin/bash
# REFEREE-2 successor 19: all MATCHPHI runs (from docs/referee-2/R2-N5-MATCHPHI). Logs in logs/. The pinned lane re-runs are in logs/pinned_check.txt
# (run in a detached worktree at 12b7d12a: python3 -I docs/lit/T33-match-phi-check.py; quotecheck quotes=5 bad=0; mutated-quote control bad=1).
cd "$(dirname "$0")"; X=../../../experiments
python3 ../R2-N5-CORE/qcheck.py docs/lit/P-N5-MATCHPHI.md 12b7d12a > logs/quotes.txt 2>&1; SHIFT=1 python3 ../R2-N5-CORE/qcheck.py docs/lit/P-N5-MATCHPHI.md 12b7d12a > logs/quotes_shift1.txt 2>&1
python3 mphi_check.py comb 6 > logs/comb6.txt 2>&1 &
BF=6 python3 mphi_check.py comb 7 > logs/comb7.txt 2>&1 &
python3 mphi_check.py seq 20000 8 400 3301 > logs/seq_K8.txt 2>&1 &
python3 mphi_check.py seq 5000 16 2000 3302 > logs/seq_K16.txt 2>&1 &
python3 mphi_check.py n5 pairs $X/si/root/logs/alt_all.lst $X > logs/n5_alt_all.txt 2>&1 &
python3 mphi_check.py n5 files ../R2-N5-STAU/lib41_noref.lst 3 > logs/n5_lib41_x3.txt 2>&1 &
python3 mphi_check.py n5 pairs named.lst $X > logs/n5_named.txt 2>&1 &
python3 mphi_check.py n5 random 3000 8 20 3303 0 3 > logs/n5_rand_kO.txt 2>&1 &
wait
