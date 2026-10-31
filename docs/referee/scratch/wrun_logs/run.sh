#!/bin/bash
# REFEREE s20: wrun_probe over box 83's run set (new/box59/sbcg.lst best-reward start; si/root/logs/alt_all.lst listed start), MAXN 100; then MUT=1.
cd "$(dirname "$0")/../../../../experiments"
P=../docs/referee/scratch/wrun_probe.py; O=../docs/referee/scratch/wrun_logs
one() { f=$O/runs$MUT/$(echo "$1" | tr '/' '_').${2:+st}.txt; ( echo "GAME $1 ${2:-best}"; if [ -n "$2" ]; then STARTF=$2 ONLYSTART=1 MAXN=100 timeout 3600 python3 -I $P $1; else NOSTART=1 MAXN=100 timeout 3600 python3 -I $P $1; fi 2>&1; echo "RC $?" ) > $f; }
export -f one; export P O
for M in 0 1; do export MUT=$M; mkdir -p $O/runs$M
grep -v '^#' new/box59/sbcg.lst | grep . | xargs -P 4 -L 1 bash -c 'one "$@"' _
xargs -P 4 -L 1 bash -c 'one "$@"' _ < si/root/logs/alt_all.lst
cat $O/runs$M/*.txt | grep -E '^(EX|[A-Z0-9]+_V |RC [^0]|maxit|skip_big)' | sort | uniq -c | sort -rn | head -40 > $O/sum$M.txt; echo "DONE $M" >> $O/sum$M.txt
done
