#!/bin/bash
# Box 215 (L-NEW successor 75): keyside215.py on box 212's frozen set (run212.sh's ALL list, read from it), the 5 towers and
# inst/*.json; resumable; 600 s per genome. Usage: bash run215.sh TOOL OUTFILE   (TOOL = keyside215)
cd "$(dirname "$0")"; TOOL=$1; OUT=$2; touch "$OUT"
ALL=$(cd ../box212 && bash -c 'source <(sed -n "/^REC=/,/^ALL=/p" run212.sh); echo $ALL')
for b in $ALL ../box212/inst/*.json ../box213/inst/*.json; do
  n=$(basename "$b"); grep -q "^$n \|^TIMEOUT $n$" "$OUT" && continue
  timeout 600 python3 $TOOL.py "$b" >> "$OUT" || echo "TIMEOUT $n" >> "$OUT"
done
echo DONE >> "$OUT"
