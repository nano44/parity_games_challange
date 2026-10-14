#!/usr/bin/env bash
cd "$(dirname "$0")"
for case in "1 1" "1 2" "1 3" "1 4" "2 1" "2 2" "2 3" "2 4" "2 5" "2 6" "3 1" "3 2" "3 3" "3 4" "3 5" "3 6" "4 1" "4 2" "4 3" "4 4" "5 1" "5 2"; do
  set -- $case; python3 compute.py $1 $2 E strong > out/strong_E_n$1_d$2.log 2>&1
done
