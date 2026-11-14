#!/bin/bash
# REFEREE s22: s4b_probe over L-SI's corpus list (anc58/corpus_fixed.lst at l-si 68fa36619; arg 1), «pg [start]» per line;
# MAXN 500, CAP 4096, 900 s per game; one file per game; summary in s4b_logs/sum.txt.
L=$(readlink -f "$1"); cd "$(dirname "$0")/../../../../experiments"
P=../docs/referee/scratch/s4b_probe.py; O=../docs/referee/scratch/s4b_logs
one() { f=$O/runs/$(echo "$1 $2" | tr '/ ' '__').txt
  if [ ! -f "$1" ]; then echo "MISSING $1" > $f; return; fi
  ( echo "GAME $1 $2"; if [ -n "$2" ]; then STARTF=$2 timeout 900 python3 -I $P $1 2>&1; else timeout 900 python3 -I $P $1 2>&1; fi; echo "RC $?" ) > $f; }
export -f one; export P O; mkdir -p $O/runs
grep -v '^#' "$L" | grep . | xargs -P 4 -L 1 bash -c 'one "$@"' _
cat $O/runs/*.txt | awk '/^[A-Za-z_]+ [0-9]+$/{ s[$1]+=$2 } /^RC /{rc[$2]++} /^MISSING/{mi++} END{for(k in s)print k,s[k]; for(k in rc)print "RC"k,rc[k]; print "MISSING",mi+0}' | sort > $O/sum.txt
grep -h '^EX' $O/runs/*.txt | head -20 >> $O/sum.txt; echo DONE >> $O/sum.txt
