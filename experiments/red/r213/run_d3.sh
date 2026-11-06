#!/bin/bash
# L-RED R213: exact RISE queries at d 3, horizon 8 (= T^R(3), R197 exact). Resumable: a finished log (SAT/UNSAT line) is skipped.
cd "$(dirname "$0")"; P=${P:-2}
jobs="5:0 7:0 7:1 7:2 7:3 7:4 7:5 6:0 6:1 6:2 6:3 6:4 6:5"
for j in $jobs; do r=${j%:*}; z=${j#*:}; log=out/d3_z${z}_r${r}.log
  grep -qE "SAT|UNSAT" $log 2>/dev/null && continue
  while [ "$(pgrep -fc 'rise.py 3 ')" -ge "$P" ]; do sleep 5; done
  nohup python3 rise.py 3 8 $z $r out/d3_z${z}_r${r}.json > $log 2>&1 &
  sleep 1
done; wait
