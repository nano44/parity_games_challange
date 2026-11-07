#!/bin/bash
# L-RED 53 R215 (a): PAD-class climbs, resumable (finished stages skipped; unfinished restart from own best). usage: rung.sh tag seed iters n...
tag=$1; seed=$2; it=$3; shift 3
for n in "$@"; do
  o=out/${tag}_n$n; grep -q FINAL $o.log 2>/dev/null && continue
  s=""; [ -f $o.json ] && s=$o.json
  echo "== $(date -u +%H:%MZ) n $n seed-file $s" >> $o.log
  python3 gclimb.py $n $((seed*1000+n)) $it $o $s >> $o.log 2>&1
done
