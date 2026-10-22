#!/usr/bin/env bash
cd "$(dirname "$0")"
for mode in weak strong; do for case in "1 1" "1 2" "1 3" "1 4" "2 1" "2 2" "2 3" "2 4" "2 5" "2 6" "3 1" "3 2" "3 3" "3 4" "3 5" "3 6" "4 1" "4 2" "4 3" "4 4"; do
  set -- $case; python3 compute.py $1 $2 V $mode > out/${mode}_V_n$1_d$2.log 2>&1
done; done
