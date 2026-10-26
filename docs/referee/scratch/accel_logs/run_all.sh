#!/bin/sh
# REFEREE succ. 12: P-N5-ACCEL batches. Run from docs/referee/scratch.
RANDSTARTS=2 python3 -I accel_probe.py lib > accel_logs/lib41_rs2.txt 2>&1 &
RANDSTARTS=4 python3 -I accel_probe.py $(ls ../../../experiments/new/box43/instances/*.pg ../../../experiments/new/box44/instances/*.pg) ../../../experiments/new/box25/laps/lap_n6_s1_110421.pg > accel_logs/box4344_rs4.txt 2>&1 &
RANDSTARTS=2 python3 -I accel_probe.py rand 2000 4 12 4 41 > accel_logs/rand_s41.txt 2>&1 &
wait
