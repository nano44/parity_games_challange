#!/usr/bin/env bash
# runs the grid in the background; logs in out/
cd "$(dirname "$0")"
for conv in E V; do for mode in weak strong; do
  for case in "1 1" "1 2" "1 3" "1 4" "2 1" "2 2" "2 3" "2 4" "2 5" "2 6" "3 1" "3 2" "3 3" "3 4" "3 5" "3 6" "4 1" "4 2" "4 3" "4 4" "4 5" "4 6"; do
    set -- $case
    python3 compute.py $1 $2 $conv $mode > out/${mode}_${conv}_n$1_d$2.log 2>&1
  done
done; done
