#!/bin/bash
# REFEREE-2 succ. 9: four 1200 s climbs against P-N5-ENT (run from this directory), seeded with L-RED's TEV instances (inputs only).
mkdir -p climb
R=../../..; I=$R/experiments/red/so/instances
python3 ent_climb.py rise 9201 8 14 1200 $I/tevlast7_n32.pg > climb/rise_9201.txt 2>&1 &
python3 ent_climb.py rise 9202 8 14 1200 $I/tevlast_cex_n40.pg > climb/rise_9202.txt 2>&1 &
python3 ent_climb.py rise 9203 8 14 1200 $I/tev_cex_n40.pg > climb/rise_9203.txt 2>&1 &
python3 ent_climb.py blk 9204 8 14 1200 $I/tev_cex_n40.pg > climb/blk_9204.txt 2>&1 &
wait
