#!/bin/sh
# REFEREE succ. 12: P-N5-1E batches (fixed seeds; file starts seeded by relative path). Run from docs/referee/scratch.
RANDSTARTS=2 python3 -I onee_probe.py lib > onee_logs/lib41_rs2.txt 2>&1 &
RANDSTARTS=2 python3 -I onee_probe.py rand 3000 4 14 21 1e > onee_logs/rand1e_4_14_s21.txt 2>&1 &
RANDSTARTS=1 python3 -I onee_probe.py rand 1000 15 30 22 1e > onee_logs/rand1e_15_30_s22.txt 2>&1 &
RANDSTARTS=2 python3 -I onee_probe.py rand 3000 4 14 23 any > onee_logs/randany_4_14_s23.txt 2>&1 &
wait
