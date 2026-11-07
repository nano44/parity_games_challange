#!/bin/bash
# L-RED 53 R215 (2): R-scored IDEAL-CYC chains. usage: runr.sh tag w D seed slices d...   (each stage = SLICES slices of SECS s;
# resumable: stage logs count finished slices; a killed slice restarts from out/<tag>_d<d>.json)
tag=$1; w=$2; D=$3; seed=$4; sl=$5; shift 5
for d in "$@"; do
  o=out/${tag}_d$d
  while :; do
    k=$(grep -c "SLICE end" $o.log 2>/dev/null); k=${k:-0}; [ "$k" -ge $sl ] && break
    echo "== $(date -u +%H:%MZ) d $d slice $k" >> $o.log
    python3 rclimb.py $d $w $D $((seed*1000+d*10+k)) $o >> $o.log 2>&1
  done
done
