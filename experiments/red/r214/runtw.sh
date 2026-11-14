#!/bin/bash
# L-RED R214 resumable tw T-climb queue (TSC=1). Job line: "m seed iters anneal seedfile". A job whose log has FINAL is skipped.
# Usage: runtw.sh jobs.txt P   (cwd experiments/red/r214). Logs out/tT_<tag>.log, genomes out/tT_<tag>.txt
cd "$(dirname "$0")"; JOBS=$1; P=${2:-1}
grep -v '^#' "$JOBS" | while read -r m seed it an sf; do
  [ -z "$m" ] && continue; tag="m${m}_r${seed}_a${an}"
  grep -q FINAL "out/tT_$tag.log" 2>/dev/null && continue
  while [ "$(pgrep -fc "tw climb")" -ge "$P" ]; do sleep 10; done
  TSC=1 ANNEAL=$an nohup nice -n 19 ./tw climb "$m" "$seed" "$it" "out/tT_$tag.txt" "$sf" > "out/tT_$tag.log" 2>&1 &
  sleep 1
done; wait
