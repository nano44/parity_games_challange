#!/bin/bash
# Box 216 (L-NEW successor 76): run one tool on box 212's frozen set (run212.sh's ALL list, read from it), the 5 towers (box212/inst) and
# box213/inst; resumable (a genome with a line or a TIMEOUT line in OUTFILE is skipped); 600 s per genome.
# Usage: bash run216.sh OUTFILE CMD [ARGS...]   (the genome path is appended to CMD ARGS; env vars pass through)
cd "$(dirname "$0")"; OUT=$1; shift; touch "$OUT"
ALL=$(cd ../box212 && bash -c 'source <(sed -n "/^REC=/,/^ALL=/p" run212.sh); echo $ALL')
for b in $ALL ../box212/inst/*.json ../box213/inst/*.json; do
  n=$(basename "$b"); grep -q "^$n \|^TIMEOUT $n$\|[ /]$n " "$OUT" && continue
  timeout 600 "$@" "$b" >> "$OUT" || echo "TIMEOUT $n" >> "$OUT"
done
tail -1 "$OUT" | grep -qx DONE || echo DONE >> "$OUT"
