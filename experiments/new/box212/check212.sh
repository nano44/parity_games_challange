#!/bin/bash
# Box 212 RF-LEVEL (L-NEW successor 74): rule-free must-0 counters on a small check set under two improving rules (rf212.py, IDEAL-CYC)
# and under N5's key rule on Gamma3 (rfd212.py), the two firing controls of each tool. Run from experiments/new/box212; output diffed
# against check212.out.
set -e
export PYTHONDONTWRITEBYTECODE=1
RULE=howard SEED=1 python3 -I rf212.py --rand 2170 30 rand,cyc,self | grep -v '^VIOLATION'
RULE=onerand SEED=1 python3 -I rf212.py --rand 2171 30 rand,cyc,self | grep -v '^VIOLATION'
RF_CTRL=1 RULE=onerand SEED=1 python3 -I rf212.py --rand 2140 10 cyc,self | grep -v '^VIOLATION' | sed 's/^/ctrl /'
RFD_MODE=spec python3 -I rfd212.py inst/DBL4_d20_F30.json
RFD_MODE=spec python3 -I rfd212.py --rand 2172 30 rand
RFD_CTRL=1 python3 -I rfd212.py --rand 2160 10 rand | sed 's/^/ctrlimp /'
LV_CTRL=2 python3 -I rfd212.py --rand 2161 20 rand | sed 's/^/ctrllv /'
