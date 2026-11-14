#!/bin/bash
# L-RED R214 (b) support query as resumable r200/cubes.py runs: level-l Xi-target (z = 2l) moves >= r within horizon H, TMIN 0, SYM0.
# Usage: run_support_cubes.sh d H l r  (env TL, P). Rerun = resume. UNSAT exact only for runs of <= H steps.
cd "$(dirname "$0")"; d=$1; H=$2; l=$3; r=$4
MOVEZ=$((2*l)) MOVEMIN=$r TMIN=0 SYM0=1 TL=${TL:-1800} P=${P:-1} python3 ../r200/cubes.py $d $H cubes/sup_d${d}_l${l}_r${r}_H${H} >> out/cubes_sup_d${d}_l${l}_r${r}_H${H}.log 2>&1
