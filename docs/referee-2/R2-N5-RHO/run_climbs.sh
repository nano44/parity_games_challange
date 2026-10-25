#!/bin/bash
# REFEREE-2 succ. 10: three 1200 s climbs against P-N5-RHO (run from this directory); seeds are inputs only.
mkdir -p climb
R=../../..
python3 rho_climb.py rho 9701 6 10 1200 > climb/rho_9701.txt 2>&1 &
python3 rho_climb.py rho 9702 6 10 1200 $R/experiments/new/box40/out/rhc_rhc_oneodd_c16_2_5.pg > climb/rho_9702.txt 2>&1 &
python3 rho_climb.py rho 9703 6 10 1200 $R/experiments/new/box40/out/rhc_rhc_block_bk20_3_4.pg > climb/rho_9703.txt 2>&1 &
wait
