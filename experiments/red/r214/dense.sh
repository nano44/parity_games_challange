#!/bin/bash
# L-RED R214 DENSE(d, l, H) (Lead 19:52Z, L-NEW box 185): some Xi-target mover of level l moves at EACH step 1..H. Every state is a
# start, so a dense window can be shifted to step 1: DENSE <=> move.py d H z=2l r=H (sigma_l covers z=2l+1). Resumable: answered skip.
# Usage (cwd experiments/red/r213): dense.sh d "l list" "H list" cap
d=$1; for H in $3; do for l in $2; do z=$((2*l)); log=../r214/out/dense_d${d}_l${l}_H${H}.log
  grep -q "SAT solve" "$log" 2>/dev/null && continue
  timeout ${4:-7200} python3 move.py $d $H $z $H ../r214/out/dense_d${d}_l${l}_H${H}.json >> "$log" 2>&1 || echo "rc $? (124 = TIMEOUT cap ${4:-7200})" >> "$log"
done; done
