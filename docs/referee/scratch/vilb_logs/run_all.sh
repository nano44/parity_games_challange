#!/bin/sh
# REFEREE succ. 12: P-N5-VILB batches. Run from docs/referee/scratch.
RANDSTARTS=2 python3 -I vilb_probe.py lib > vilb_logs/lib41_rs2.txt 2>&1 &
RANDSTARTS=4 python3 -I vilb_probe.py $(ls ../../../experiments/new/box43/instances/*.pg ../../../experiments/new/box44/instances/*.pg) > vilb_logs/box4344_rs4.txt 2>&1 &
RANDSTARTS=2 python3 -I vilb_probe.py rand 2000 5 14 4 31 > vilb_logs/rand_s31.txt 2>&1 &
VILB_MUT=oddmax python3 -I vilb_probe.py lib > vilb_logs/mut_oddmax_lib41.txt 2>&1 &
wait
