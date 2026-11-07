#!/bin/bash
# L-NEW box 162: reproduce the EXACT external-flip table T_k(m) (iso.py FREE0=1 ISO=1 KF=k at d = m + 1), resumable:
# a target with a RESULT line in log/ is skipped; logs are written as *.part and renamed at the end. Needs env LRED (box 160 README).
# Usage: run_tk.sh "d k t1 t2" ...   (for each item: t1 expected SAT, t2 expected UNSAT)
cd "$(dirname "$0")"
for item in "$@"; do
  set -- $item; d=$1; k=$2; shift 2
  for t in "$@"; do
    tag=kf${k}_d${d}_t${t}
    grep -q "^RESULT" log/$tag.log 2>/dev/null && continue
    [ -e log/$tag.log.part ] && continue   # running elsewhere (a stale .part after a restart: delete it)
    FREE0=1 ISO=1 KF=$k python3 ../box160/iso.py $d $t out/$tag.json > log/$tag.log.part 2>&1; mv log/$tag.log.part log/$tag.log
  done
done
