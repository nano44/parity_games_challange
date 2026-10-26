#!/bin/sh
# REFEREE succ. 12: P-N5-XEP batches. Run from docs/referee/scratch.
MAXN=1000 python3 -I xep_probe.py lib > xep_logs/lib41_all_s3.txt 2>&1 &
RANDSTARTS=4 python3 -I xep_probe.py lib > xep_logs/lib41_rs4.txt 2>&1 &
RANDSTARTS=4 python3 -I xep_probe.py $(ls ../../../experiments/new/box43/instances/*.pg ../../../experiments/new/box44/instances/*.pg) > xep_logs/box4344_rs4.txt 2>&1 &
RANDSTARTS=2 python3 -I xep_probe.py rand 3000 4 14 4 72 > xep_logs/rand_s72.txt 2>&1 &
wait
