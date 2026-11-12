#!/bin/bash
# L-COMP box 43 item 1: MY counters on random genomes of this lane's law and on mutants (this lane's move set) of frozen genomes (rand43.py).
# Resumable per line. env LNEW208 = archive of claude/l-new 8db300fe (for the mutant bases). Usage: run43c.sh
set -u; cd "$(dirname "$0")"; export PYTHONDONTWRITEBYTECODE=1; : "${LNEW208:?set LNEW208}"; N="$LNEW208/experiments/new"; O=out/rand43.out; touch $O
one() { grep -q "^$1 " $O || python3 rand43.py "${@:2}" >> $O 2>> out/run43c.err; }
one "rand 4311 1000 60 0.6" rand 4311 1000 60 0.6
one "rand 4312 1000 60 0.3" rand 4312 1000 60 0.3
one "rand 4313 1000 60 0.0" rand 4313 1000 60 0.0
one "rand 4314 300 160 0.5" rand 4314 300 160 0.5
for b in $N/box207/inst/CFI3_n48.json $N/box206/inst/K1L10_n48.json $N/box203/inst/K1F21_n48.json $N/box203/inst/MWR4_2.json $N/box206/inst/CW4_n.json $N/box202/inst/DSALT6_n108.json ../box40/inst/C6G8_n54.json ../box40/inst/RWX_n95.json ../box40/inst/DHIB26_2804.json; do
  grep -q "^mut $(basename $b) seed 4320 " $O || python3 rand43.py mut 4320 150 $b >> $O 2>> out/run43c.err
done
LV43_CTRL=1 python3 rand43.py mut 4321 30 $N/box207/inst/CFI3_n48.json > out/rand43_ctrl1.out 2>> out/run43c.err
LV43_CTRL=2 python3 rand43.py mut 4321 30 $N/box207/inst/CFI3_n48.json > out/rand43_ctrl2.out 2>> out/run43c.err
echo "run43c done: $(wc -l < $O) lines"
