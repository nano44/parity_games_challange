#!/bin/bash
# REFEREE-2 re-run of L-COMP box 27's 16 cubes, ISO / FREE0 / P / W explicitly unset (W defaults to R).
cd "$(dirname "$0")"
for c in $(seq 0 15); do
  cube=""; for i in 0 1 2 3; do cube="$cube$((i+2)):$(( (c>>i)&1 )),"; done
  echo "$c $cube"
done | xargs -P 4 -L 1 bash -c 'env -u ISO -u FREE0 -u P -u W -u KF SYM=1 CUBE=$1 python3 cnf.py 3 9 /dev/null > r2_$0.log 2>&1'
echo ALLDONE
