#!/usr/bin/env bash
cd "$(dirname "$0")"
for mode in weak strong; do for conv in E V; do for d in 1 2 3 4; do
  python3 compute.py 5 $d $conv $mode > out/${mode}_${conv}_n5_d$d.log 2>&1
done; done; done
