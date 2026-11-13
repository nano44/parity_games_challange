#!/bin/bash
# L-COMP box 45 item (b): the per-gate quiet-flip maximum on the second engine (qsec45.py, L-RED 65's HOW3) for every climb best and the frozen
# family members with the largest qmax. Resumable per genome. env RED, LNEW as qsec45.py; LNEW209 = an archive of claude/l-new 311bbf81.
set -u; cd "$(dirname "$0")"; export PYTHONDONTWRITEBYTECODE=1
main() {
O=out/qsec45.out; touch $O
N="$LNEW209/experiments/new"
for f in out/climb45/BEST_*.json $N/box202/inst/MW4_2.json $N/box202/inst/MW8_2.json $N/box202/inst/MW16_2.json $N/box202/inst/MW32_2.json \
         ../box43/inst/MWR4_2.json ../box43/inst/MWR8_2.json ../box43/inst/MWR16_2.json $N/box206/inst/CW4_n.json $N/box206/inst/CW8_n.json $N/box206/inst/CW16_n.json; do
  [ -f "$f" ] || { echo "MISSING $f" >> $O.err; continue; }
  b=$(basename $f); grep -q "^$b " $O || python3 -I qsec45.py $f >> $O 2>> $O.err
done
echo "run45c done: $(wc -l < $O) rows"
}
main "$@"
