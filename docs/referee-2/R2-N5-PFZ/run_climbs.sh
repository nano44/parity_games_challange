#!/bin/bash
# REFEREE-2 succ. 9: four 1200 s climbs against P-N5-PFZ (run from this directory); lane instances are inputs only.
mkdir -p climb
R=../../..
python3 pfz_climb.py pfz 9501 6 10 1200 > climb/pfz_9501.txt 2>&1 &
python3 pfz_climb.py pfz 9502 6 10 1200 $R/experiments/new/box25/instances/wd16_s2.pg > climb/pfz_9502.txt 2>&1 &
python3 pfz_climb.py pfz 9503 8 12 1200 $R/experiments/n5-exhaustive/instances/b5_os_n16.pg > climb/pfz_9503.txt 2>&1 &
python3 pfz_climb.py pfz 9504 6 9 1200 > climb/pfz_9504.txt 2>&1 &
wait
