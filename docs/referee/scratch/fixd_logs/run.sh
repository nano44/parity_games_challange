#!/bin/bash
# REFEREE s20: fixd_probe over box 77's run set: new/box59/sbcg.lst (best-reward start) and si/root/logs/alt_all.lst (the listed start, if any), N5 and N5-LZC.
cd "$(dirname "$0")/../../../../experiments"
P=../docs/referee/scratch/fixd_probe.py; O=../docs/referee/scratch/fixd_logs
one() { for e in "" --lzc; do o=$( (echo "GAME $1 ${e:-N5} ${2:-best}"; if [ -n "$2" ]; then STARTF=$2 ONLYSTART=1 timeout 1800 python3 -I $P $1 $e; else NOSTART=1 timeout 1800 python3 -I $P $1 $e; fi 2>&1; echo "RC $?") | grep -E '^(GAME|RC|CH|FLATTR|FSW|krise|trans|maxit|VIOL|STAT|EX|[A-Z0-9]+_V) '); f=$O/runs/$(echo "$1 ${e:-N5}" | tr '/ ' '__').txt; printf '%s\n' "$o" > $f; done; }; export -f one; export P O; rm -rf $O/runs; mkdir -p $O/runs
grep -v '^#' new/box59/sbcg.lst | grep . | xargs -P 4 -L 1 bash -c 'one "$@"' _ ; cat $O/runs/*.txt > $O/sbcg.txt; mkdir -p $O/runs_sbcg; mv $O/runs/*.txt $O/runs_sbcg/
xargs -P 4 -L 1 bash -c 'one "$@"' _ < si/root/logs/alt_all.lst; cat $O/runs/*.txt > $O/alt.txt
echo DONE
