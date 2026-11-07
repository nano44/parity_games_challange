#!/bin/bash
# L-RED 53 R215 (Lead 10:05Z): R_mov-scored IDEAL-CYC climbs at fixed d, growing width. usage: runm.sh tag d D seed slices [seedjson] -- w...
tag=$1; d=$2; D=$3; seed=$4; sl=$5; sj=$6; shift 6
for w in "$@"; do
  o=out/${tag}_d${d}_w$w
  while :; do
    k=$(grep -c "SLICE end" $o.log 2>/dev/null); k=${k:-0}; [ "$k" -ge $sl ] && break
    echo "== $(date -u +%H:%MZ) d $d w $w slice $k" >> $o.log
    SCORE=M python3 rclimb.py $d $w $D $((seed*1000+w*10+k)) $o $sj >> $o.log 2>&1
  done
done
