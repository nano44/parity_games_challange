#!/bin/sh
# REFEREE-2 succ. 13: climbs toward the late regime (in-phase fallbacks per phase > n). Usage: sh run_climbs.sh
cd "$(dirname "$0")"
for s in 81 82 83 84; do timeout 2400 python3 fbred_check.py climb 4000 4 8 $s climb/late_$s > logs/climb_$s.txt 2>&1 & done
wait
