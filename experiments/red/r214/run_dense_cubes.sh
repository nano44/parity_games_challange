#!/bin/bash
# L-RED R214 DENSE(d, l, H) as resumable r200/cubes.py runs: MOVEZ=2l MOVEMIN=H horizon H TMIN 0 SYM0=1 (sigma_0 fixes z). Rerun = resume.
# Usage: run_dense_cubes.sh d l H   (env TL, P). A SAT cube's genome is then certified by certM.py.
cd "$(dirname "$0")"; d=$1; l=$2; H=$3
MOVEZ=$((2*l)) MOVEMIN=$H TMIN=0 SYM0=1 TL=${TL:-1200} P=${P:-1} python3 ../r200/cubes.py $d $H cubes/dense_d${d}_l${l}_H${H} >> out/cubes_dense_d${d}_l${l}_H${H}.log 2>&1
