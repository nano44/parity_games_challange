#!/bin/bash
# Box 213 (L-NEW successor 75): keymu213.py and g2_213.py on box 212's frozen set (run212.sh's ALL list, read from it), the 5 towers and
# inst/*.json; resumable; 600 s per genome. Usage: bash run213m.sh TOOL OUTFILE   (TOOL = keymu213 | g2_213; env KM_MODE / KM_CTRL passed)
cd "$(dirname "$0")"; TOOL=$1; OUT=$2; touch "$OUT"
ALL=$(cd ../box212 && bash -c 'source <(sed -n "/^REC=/,/^ALL=/p" run212.sh); echo $ALL')
for b in $ALL ../box212/inst/*.json inst/*.json; do
  n=$(basename "$b"); grep -q "^$n \|^TIMEOUT $n$" "$OUT" && continue
  timeout 600 python3 $TOOL.py "$b" >> "$OUT" || echo "TIMEOUT $n" >> "$OUT"
done
echo DONE >> "$OUT"
