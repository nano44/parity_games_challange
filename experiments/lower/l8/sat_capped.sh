#!/usr/bin/env bash
# L-LOWER 9: the h = 3, d = 5 helper-schedule SAT instances whose TARGET is capped. sched.py's sequential target is capped only when
# alpha_(h-2) = 1 (for h = 3: alpha_1 = 1, i.e. alpha strings 1,1,0 and 1,1,1; 1,0,x give F(2) = 12 < 14, see docs/lower/L9-design.md §3).
# Resumable through hsat_run.py (decided cubes skipped). Usage: sat_capped.sh WORKER NWORKERS
cd "$(dirname "$0")"; i=0
for inst in "3 5 1,1,0 0" "3 5 1,1,1 0" "3 5 1,1,0 1" "3 5 1,1,1 1" "3 5 1,1,0 2" "3 5 1,1,1 2" "3 5 1,1,0 3" "3 5 1,1,1 3"; do
  if [ $((i % $2)) -eq "$1" ]; then python3 hsat_run.py $inst 1500; fi; i=$((i+1))
done
