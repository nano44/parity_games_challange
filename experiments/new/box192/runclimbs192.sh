#!/bin/bash
# Box 192 climbs (resumable: each restarts from its best OUT.json). Run from experiments/new/box192. 40-min slices.
cd "$(dirname "$0")"
for spec in "R 2 4 2" "R 2 8 2" "D 6 2 2" "R 3 4 2"; do set -- $spec
  timeout 2400 python3 climb192.py $1 $2 $3 $4 7$2$3 100000 out/c$1_d$2_w$3 >> out/c$1_d$2_w$3.log 2>&1 &
done
wait
