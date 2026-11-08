#!/usr/bin/env bash
# L-LOWER 8: run the h = 3 helper-schedule SAT instances through hsat_run.py (resumable). Usage: sat_all.sh WORKER NWORKERS
cd "$(dirname "$0")"; i=0
for inst in "3 4 1,1,1 -" "3 5 1,0,0 0" "3 5 1,0,1 0" "3 5 1,1,0 0" "3 5 1,1,1 0" "3 5 1,0,0 1" "3 5 1,0,1 1" "3 5 1,1,0 1" "3 5 1,1,1 1" "3 5 1,0,0 2" "3 5 1,0,1 2" "3 5 1,1,0 2" "3 5 1,1,1 2" "3 5 1,0,0 3" "3 5 1,0,1 3" "3 5 1,1,0 3" "3 5 1,1,1 3"; do
  if [ $((i % $2)) -eq "$1" ]; then python3 hsat_run.py $inst 1500; fi; i=$((i+1))
done
