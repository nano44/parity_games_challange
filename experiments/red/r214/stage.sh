#!/bin/bash
# L-RED R214 staged T climbs: for d = 9..14, seed = top-extension of the best tT/keep genome at d-1 (max T), climb TSC=1 200M.
# Usage: stage.sh wave   (cwd experiments/red/r214). Resumable: a finished log (FINAL) is skipped.
cd "$(dirname "$0")"; w=$1
best() { # best tw text at level count d (m = d-1) among out/tT_m<m>_*.txt and keep/tw_d<d>_*.tw, by tw eval T
  local m=$(( $1 - 1 )); local bf=""; local bt=-1
  for f in out/tT_m${m}_*.txt keep/tw_d$1_*.tw; do [ -f "$f" ] || continue; t=$(TSC=1 ./tw eval $m < "$f" | awk '{print $2}'); [ "$t" -gt "$bt" ] && { bt=$t; bf=$f; }; done; echo "$bf"; }
for d in 9 10 11 12 13 14; do
  m=$((d-1)); tag="m${m}_rs${w}${d}_a1500"; grep -q FINAL "out/tT_$tag.log" 2>/dev/null && continue
  p=$(best $((d-1))); [ -z "$p" ] && continue
  python3 ../r212/extend.py "$p" top $((w*100+d)) out/stg_${w}_d$d.tw && echo "$(grep ^start "$p") 0 0" >> out/stg_${w}_d$d.tw
  b=$(best $d); [ -n "$b" ] && [ "$(TSC=1 ./tw eval $m < "$b" | awk '{print $2}')" -gt "$(TSC=1 ./tw eval $m < out/stg_${w}_d$d.tw | awk '{print $2}')" ] && cp "$b" out/stg_${w}_d$d.tw
  TSC=1 ANNEAL=1500 nice -n 19 ./tw climb $m $((w*1000+d)) 200000000 out/tT_$tag.txt out/stg_${w}_d$d.tw > out/tT_$tag.log 2>&1
done
