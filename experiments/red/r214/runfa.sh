#!/bin/bash
# L-RED R214 resumable climb driver for fa (SCORE=M ALLM=1: max moves over ALL movers). Job line: "m seed iters anneal seedfile".
# A job whose log has FINAL is skipped. Usage: runfa.sh jobs.txt P   (cwd experiments/red/r214). Logs out/c_<tag>.log, genomes out/c_<tag>.txt
cd "$(dirname "$0")"; JOBS=$1; P=${2:-1}
grep -v '^#' "$JOBS" | while read -r m seed it an sf; do
  [ -z "$m" ] && continue
  tag="m${m}_r${seed}_a${an}_$(basename "$sf" .txt)"
  grep -q FINAL "out/c_$tag.log" 2>/dev/null && continue
  while [ "$(pgrep -fc "fa climb")" -ge "$P" ]; do sleep 5; done
  echo "$m $seed $it $an $sf -> $tag"
  SCORE=M ALLM=1 ANNEAL=$an ./fa climb "$m" 0 0 "$seed" "$it" "out/c_$tag.txt" "$sf" > "out/c_$tag.log" 2>&1 &
  sleep 1
done
wait
