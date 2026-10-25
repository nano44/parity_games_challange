#!/bin/bash
# REFEREE-2 succ. 12: mutation controls for P-N5-KW (own trace, whole list). Output logs_mut/<MUT>.txt (violation-line count + 3 samples)
cd "$(dirname "$0")"; mkdir -p logs_mut
for m in frz0 casc par; do
  ( while read f; do KW_MUT=$m timeout 900 python3 kw_check.py inst ../../../$f 3 own; done < files.lst ) > logs_mut/$m.raw 2>&1
  grep -c "^VIOLATION " logs_mut/$m.raw > logs_mut/$m.txt; grep "^VIOLATION " logs_mut/$m.raw | head -3 >> logs_mut/$m.txt; rm logs_mut/$m.raw
done
echo DONE > logs_mut/ALLDONE
