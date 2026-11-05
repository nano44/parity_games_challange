#!/bin/bash
# L-NEW box 160: external k-flip maxima (iso.py FREE0=1 ISO=1 KF=k), resumable; stops at the first UNSAT. Usage: run_kf.sh d k t ...
cd "$(dirname "$0")"/..
d="$1"; k="$2"; shift 2
for t in "$@"; do
  tag=kf${k}_d${d}_t${t}
  if grep -q "^RESULT" box160/log/$tag.log 2>/dev/null; then grep -q UNSAT box160/log/$tag.log && break; continue; fi
  FREE0=1 ISO=1 KF=$k python3 box160/iso.py $d $t box160/out/$tag.json > box160/log/$tag.log.part 2>&1; mv box160/log/$tag.log.part box160/log/$tag.log
  grep -q "UNSAT" box160/log/$tag.log && break
done
