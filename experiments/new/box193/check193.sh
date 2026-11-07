#!/bin/bash
# Box 193 ASC (L-NEW successor 61): DATA behind CHAIN-DECOMP, TAIL-MON, E-DOM, UP-JUMP, ASC-GATE (asc193.py), the exact values of the
# abstract chain system CS(M, A) for M <= 5 (chain193.py) and Construction ASC-EXP (ascexp193.py). Run from experiments/new/box193.
# M = 6, 7 values come from dp193.c (data/cs_dp.txt); they are not re-run here (minutes of C).
set -e
cd "$(dirname "$0")"
python3 asc193.py inst/CLR_k8s16.json inst/FPORT_n2.json inst/FPORT_n3.json inst/LEAP_k8.json inst/RS2.json inst/RS2_L8M6.json \
  inst/RS3.json inst/RSG_K4.json
python3 asc193.py ../box192/inst/cR_d2_w8_R22.json ../box192/inst/rd2_d9.json ../box192/inst/rd2_d10.json ../box192/inst/rd3_d7.json \
  ../box192/inst/rf_d5.json
for a in 0 1 99; do for m in 1 2 3 4; do python3 chain193.py $m $a; done; done
python3 chain193.py 5 0
python3 chain193.py 5 1
python3 ascexp193.py 10
python3 noup193.py 300 1
