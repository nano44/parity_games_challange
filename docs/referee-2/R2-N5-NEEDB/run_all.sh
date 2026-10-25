#!/bin/bash
# REFEREE-2 succ. 12: batch for P-N5-NEEDB. Usage: run_all.sh MODE (own|spec|rand) -> logs/MODE/<n>.log
cd "$(dirname "$0")"; mode=$1; mkdir -p logs/$mode; i=0
while read f; do i=$((i+1)); timeout 900 python3 needb_check.py inst ../../../$f 3 $mode > logs/$mode/$i.log 2>&1; echo "$f exit $?" >> logs/$mode/$i.log; done < files.lst
echo DONE > logs/$mode/ALLDONE
