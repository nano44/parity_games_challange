#!/bin/bash
# L-RED R214 task (3): exact d 4 top level, any mover (MOVEANY: Xi-target or not) z 6 moves >= 8 within horizon 13 = T^R(4), TMIN 0.
# r200/cubes.py partition (first-move times of movers 0,1 then 2,3 then 4,5), SYM0=1 (sigma_0 swaps 0,1, fixes z 6). Rerun = resume.
# A SAT cube's genome is re-checked by mvck.py (moves of z) before any claim.
cd "$(dirname "$0")"
MOVEZ=6 MOVEMIN=${R:-8} MOVEANY=1 TMIN=0 SYM0=1 TL=${TL:-1200} P=${P:-1} python3 ../r200/cubes.py 4 13 cubes/d4_any_z6_r${R:-8} >> out/cubes_d4_any_z6_r${R:-8}.log 2>&1
