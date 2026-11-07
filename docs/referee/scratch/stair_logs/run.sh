#!/bin/bash
# REFEREE s21: stair_probe over box 59 sbcg.lst (best-reward start) and alt_all.lst (listed start), MAXN 100; one file per run.
cd "$(dirname "$0")/../../../../experiments"
P=../docs/referee/scratch/stair_probe.py; O=../docs/referee/scratch/stair_logs
one() { f=$O/runs/$(echo "$1" | tr '/' '_').txt; ( echo "GAME $1"; timeout 1800 python3 -I $P $1 2>&1; echo "RC $?" ) > $f; }
export -f one; export P O; mkdir -p $O/runs
{ grep -v '^#' new/box59/sbcg.lst | grep . | awk '{print $1}'; awk '{print $1}' si/root/logs/alt_all.lst; } | sort -u | xargs -P 4 -L 1 bash -c 'one "$@"' _
cat $O/runs/*.txt | awk '/^[A-Za-z_]+ [0-9]+$/{ if($1 ~ /max/){ if($2>m[$1]) m[$1]=$2 } else s[$1]+=$2 } /^RC /{rc[$2]++} END{for(k in s)print k,s[k]; for(k in m)print k,m[k]; for(k in rc)print "RC"k,rc[k]}' | sort > $O/sum.txt
grep -h '^EX' $O/runs/*.txt | head -20 >> $O/sum.txt; echo DONE >> $O/sum.txt
