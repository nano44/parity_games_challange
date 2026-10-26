#!/bin/sh
# REFEREE-2 succ. 14: climbs for a FRZ-U_H3 freeze in the not-(h_D) regime. Usage: sh run_climbs.sh
cd "$(dirname "$0")"
for S in 211 212 213 214; do python3 h3_check.py climb 3000 3 7 $S climb/frz_$S > logs/climb_$S.txt 2>&1 & done
wait
