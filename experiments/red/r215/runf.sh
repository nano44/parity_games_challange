#!/bin/bash
# L-RED 53 R215 (OVT, box 192): max-flips-at-one-gate (SCORE=F) climbs at fixed d, growing width. usage: runf.sh tag d D seed slices w...
tag=$1; d=$2; D=$3; seed=$4; sl=$5; shift 5
for w in "$@"; do
  o=out/${tag}_d${d}_w$w
  while :; do
    k=$(grep -c "SLICE end" $o.log 2>/dev/null); k=${k:-0}; [ "$k" -ge $sl ] && break
    echo "== $(date -u +%H:%MZ) d $d w $w slice $k" >> $o.log
    SCORE=F python3 rclimb.py $d $w $D $((seed*1000+w*10+k)) $o >> $o.log 2>&1
  done
done
