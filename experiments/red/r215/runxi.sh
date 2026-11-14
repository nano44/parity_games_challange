#!/bin/bash
# L-RED 53 R215 (b): staged xi chain. usage: runxi.sh tag seed d0 d1 iters [initial seed json for d0]
# resumable: a finished stage (FINAL in log) is skipped; an unfinished one restarts from its own best json.
tag=$1; seed=$2; d0=$3; d1=$4; it=$5; init=$6
for d in $(seq $d0 $d1); do
  o=out/${tag}_d$d; log=$o.log
  grep -q FINAL $log 2>/dev/null && continue
  s=""; [ -f $o.json ] && s=$o.json
  [ -z "$s" ] && [ -f out/${tag}_d$((d-1)).json ] && s=out/${tag}_d$((d-1)).json
  [ -z "$s" ] && [ $d = $d0 ] && s=$init
  echo "== $(date -u +%H:%MZ) d $d seed-file $s" >> $log
  python3 xiclimb2.py $d $((seed*100+d)) $it $o $s >> $log 2>&1
done
