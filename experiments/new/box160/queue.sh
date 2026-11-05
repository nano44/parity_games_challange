#!/bin/bash
# L-NEW box 160: start each command line of box160/queue.txt (in order) when fewer than 4 iso.py processes run; done lines are
# recorded in box160/log/queue.done (resumable after a container restart: re-run this script; finished targets are skipped by the
# run_*.sh drivers themselves).
cd "$(dirname "$0")"/..
while read -r line; do
  [ -z "$line" ] && continue
  grep -qxF "$line" box160/log/queue.done 2>/dev/null && continue
  while [ "$(ps -eo args | grep -c '^python3 box160/iso.py')" -ge 4 ]; do sleep 20; done
  echo "$line" >> box160/log/queue.done
  nohup sh -c "$line" > /dev/null 2>&1 &
  sleep 5
done < box160/queue.txt
