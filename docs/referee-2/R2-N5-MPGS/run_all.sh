#!/bin/bash
# REFEREE-2 successor 19: all MPGS (Part B) runs (from docs/referee-2/R2-N5-MPGS). Logs in logs/. Pinned lane re-runs: logs/pinned_*.txt
# (detached worktree at a23179b0, python3 -I). Part (A) checks: ../R2-N5-MATCHPHI (identical mathematics; logs there).
cd "$(dirname "$0")"; X=../../../experiments
python3 ../R2-N5-CORE/qcheck.py docs/lit/P-N5-MPGS.md a23179b0 > logs/quotes.txt 2>&1; SHIFT=1 python3 ../R2-N5-CORE/qcheck.py docs/lit/P-N5-MPGS.md a23179b0 > logs/quotes_shift1.txt 2>&1
python3 gateshut_check.py pairs hn.lst $X > logs/hn.txt 2>&1 &
python3 gateshut_check.py files ../R2-N5-STAU/lib41_noref.lst 3 > logs/lib41_x3.txt 2>&1 &
python3 gateshut_check.py pairs $X/si/root/logs/alt_all.lst $X > logs/alt_all.txt 2>&1 &
python3 gateshut_check.py random 5000 8 20 3401 0 3 > logs/rand_kO.txt 2>&1 &
python3 gateshut_check.py random 5000 6 16 3402 2 3 > logs/rand_k2.txt 2>&1 &
wait
