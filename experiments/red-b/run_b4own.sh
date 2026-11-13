#!/bin/bash
# B4 (a) continued (L-RED-B successor 3): own-guide phases at larger n, to test the 5-point fits. Usage: run_b4own.sh B3ROOT
cd "$(dirname "$0")"; mkdir -p work; R="$1"
[ -f work/b4phase_own2_hn.out ] && tail -1 work/b4phase_own2_hn.out | grep -q SUMMARY || python3 b4phase.py "$R" work/b4pg spec fam hn 6 7 > work/b4phase_own2_hn.out 2>&1
[ -f work/b4phase_own2_fried.out ] && tail -1 work/b4phase_own2_fried.out | grep -q SUMMARY || python3 b4phase.py "$R" work/b4pg spec fam fried 7 8 9 10 > work/b4phase_own2_fried.out 2>&1
[ -f work/b4phase_own2_lmcs.out ] && tail -1 work/b4phase_own2_lmcs.out | grep -q SUMMARY || python3 b4phase.py "$R" work/b4pg spec fam lmcs 7 8 9 10 > work/b4phase_own2_lmcs.out 2>&1
