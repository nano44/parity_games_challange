#!/bin/bash
# REFEREE-2 succ. 9: four 1200 s climbs against P-N5-NEB (run from this directory); lane instances are inputs only.
mkdir -p climb
R=../../..; I=$R/experiments/new/box38/instances
python3 neb_climb.py brk 9301 8 14 1200 $I/nebc_cex_n14.pg > climb/brk_9301.txt 2>&1 &
python3 neb_climb.py brk 9302 8 14 1200 $I/tauw_A_cex_n24.pg > climb/brk_9302.txt 2>&1 &
python3 neb_climb.py cwo 9303 8 14 1200 $I/tauw_B_cex_n24.pg > climb/cwo_9303.txt 2>&1 &
python3 neb_climb.py cwo 9304 8 14 1200 $I/nebc_cex_n14.pg > climb/cwo_9304.txt 2>&1 &
wait
