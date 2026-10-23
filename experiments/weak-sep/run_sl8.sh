#!/usr/bin/env bash
cd "$(dirname "$0")"
for conv in E V; do
  for c in "2 2 2" "2 2 3" "2 2 4" "2 3 3" "2 3 4" "3 3 5" "3 3 6" "3 4 5" "3 4 6"; do
    set -- $c; timeout 3600 python3 enumerate_weak.py $1 $2 $conv $3 3 5000 >> out/sl8.log 2>&1
  done
done
echo ALLDONE >> out/sl8.log
