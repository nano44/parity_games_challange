#!/bin/bash
# REFEREE s22: re-run of the 87 list lines whose first-run counts differed from the lane's (s4b_logs/rerun.lst). Lines «pg» alone:
# SPEC S3 default start forced (STARTF=/nonexistent; the first run had picked up the sibling .start). Lines «pg start»: PARTIAL=1 (lane rule).
cd "$(dirname "$0")/../../../../experiments"; P=../docs/referee/scratch/s4b_probe.py; O=../docs/referee/scratch/s4b_logs
while read a b; do f=$O/rerun/$(echo "$a $b" | tr '/ ' '__').txt
  if [ -n "$b" ]; then ( echo "GAME $a $b"; STARTF=$b PARTIAL=1 MAXN=500 CAP=4096 timeout 900 python3 -I $P $a 2>&1; echo "RC $?" ) > $f
  else ( echo "GAME $a"; STARTF=/nonexistent MAXN=500 CAP=4096 timeout 900 python3 -I $P $a 2>&1; echo "RC $?" ) > $f; fi
done < $O/rerun.lst
