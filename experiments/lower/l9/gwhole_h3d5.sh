#!/usr/bin/env bash
# L-LOWER 9: the 8 capped h = 3, d = 5 instances, whole, by Glucose4 (gwhole.py). Usage: gwhole_h3d5.sh WORKER NWORKERS TLIMIT OUTDIR
cd "$(dirname "$0")"; i=0
for inst in "3 5 1,1,0 0" "3 5 1,1,1 0" "3 5 1,1,0 1" "3 5 1,1,1 1" "3 5 1,1,0 2" "3 5 1,1,1 2" "3 5 1,1,0 3" "3 5 1,1,1 3"; do
  if [ $((i % $2)) -eq "$1" ]; then python3 gwhole.py $inst $3 $4; fi; i=$((i+1))
done
