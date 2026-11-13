#!/bin/bash
# Box 213 (L-NEW successor 75): key213.py on box 212's frozen set (run212.sh's ALL list, read from it) and the 5 towers; resumable
# (a genome already in the output is skipped); 600 s per genome. Usage: bash run213.sh OUTFILE [KEY_CTRL]
cd "$(dirname "$0")"; OUT=$1; export KEY_CTRL=${2:-0}; touch "$OUT"
ALL=$(cd ../box212 && bash -c 'source <(sed -n "/^REC=/,/^ALL=/p" run212.sh); echo $ALL')
for b in $ALL ../box212/inst/*.json; do
  n=$(basename "$b"); grep -q "^$n \|^TIMEOUT $n$" "$OUT" && continue
  timeout 600 python3 key213.py "$b" >> "$OUT" || echo "TIMEOUT $n" >> "$OUT"
done
echo DONE >> "$OUT"
