#!/bin/bash
# REFEREE-2 succ. 8 R2-N5-SCOPE climbs (run from this directory; seconds per climb = $1, default 1200). Two waves of 4.
S=${1:-1200}; mkdir -p climb; R=../../..
python3 scope_climb.py scope 91 8 16 $S > climb/scope_91.txt 2>&1 &
python3 scope_climb.py fb 92 8 14 $S > climb/fb_92.txt 2>&1 &
python3 scope_climb.py fb 93 0 0 $S $R/experiments/new/box25/instances/wd12_s1.pg > climb/fb_93.txt 2>&1 &
python3 scope_climb.py cnl 94 6 12 $S > climb/cnl_94.txt 2>&1 &
wait
python3 scope_climb.py scope 95 0 0 $S $R/experiments/new/box25/instances/sc24.pg > climb/scope_95.txt 2>&1 &
python3 scope_climb.py fb 96 0 0 $S $R/experiments/new/box28/out/oc12_s1.pg > climb/fb_96.txt 2>&1 &
python3 scope_climb.py cnl 97 8 14 $S > climb/cnl_97.txt 2>&1 &
python3 scope_climb.py scope 98 10 20 $S > climb/scope_98.txt 2>&1 &
wait
