#!/bin/bash
# REFEREE-2 succ. 12: mutation controls (own trace, whole library; the witness for b0). Output logs_mut/<MUT>.txt
cd "$(dirname "$0")"; mkdir -p logs_mut
for m in otc otf xg; do
  ( while read f; do NB_MUT=$m timeout 900 python3 needb_check.py inst ../../../$f 3 own; done < files.lst ) > logs_mut/$m.raw 2>&1
  grep -c "^VIOLATION" logs_mut/$m.raw > logs_mut/$m.txt; grep "^VIOLATION" logs_mut/$m.raw | head -5 >> logs_mut/$m.txt; rm logs_mut/$m.raw
done
NB_MUT=b0 python3 needb_check.py inst ../R2-N5-LV2/climb/block_9501.pg 3 own > logs_mut/b0.txt 2>&1
echo DONE > logs_mut/ALLDONE
