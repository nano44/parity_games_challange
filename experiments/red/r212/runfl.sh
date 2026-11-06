#!/bin/bash
# L-RED R212 resumable climb driver: each job "m K score seed iters [seedfile]"; a job whose log has FINAL is skipped.
# Usage: run.sh jobs.txt P     (cwd experiments/red/r212). Logs out/<tag>.log, genomes out/<tag>.txt
cd "$(dirname "$0")"; JOBS=$1; P=${2:-2}
grep -v '^#' "$JOBS" | while read -r m K sc seed it sf; do
  [ -z "$m" ] && continue
  tag="L${ISO:-0}_m${m}_K${K}_s${sc}_r${seed}${sf:+_$(basename "$sf" .txt)}"
  grep -q FINAL "out/$tag.log" 2>/dev/null && continue
  while [ "$(pgrep -fc "f[kl] climb")" -ge "$P" ]; do sleep 5; done
  echo "$m $K $sc $seed $it $sf -> $tag"
  ANNEAL=${ANNEAL:-0} ISO=${ISO:-0} ./fl climb "$m" "$K" "$sc" "$seed" "$it" "out/$tag.txt" $sf > "out/$tag.log" 2>&1 &
  sleep 1
done
wait
