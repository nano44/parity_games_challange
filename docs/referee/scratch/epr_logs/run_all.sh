#!/bin/sh
# REFEREE succ. 12: P-N5-EPR batches. Run from docs/referee/scratch.
RANDSTARTS=2 python3 -I epr_probe.py lib > epr_logs/lib41_rs2.txt 2>&1 &
RANDSTARTS=4 python3 -I epr_probe.py $(ls ../../../experiments/new/box43/instances/*.pg ../../../experiments/new/box44/instances/*.pg) > epr_logs/box4344_rs4.txt 2>&1 &
RANDSTARTS=4 python3 -I epr_probe.py rand 3000 5 18 2 4 92 > epr_logs/randk_s92.txt 2>&1 &
wait
