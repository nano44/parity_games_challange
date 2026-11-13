#!/bin/bash
# Box 212 Addendum A: rf212.py on rv208's MUTANTS (approved DATA plan (a)) and the control «one non-improving switch» (RULE=worsen).
# Resumable per (rule, base). Run from experiments/new/box212.
set -u
export PYTHONDONTWRITEBYTECODE=1
main() {
mkdir -p out
BASES="../box206/inst/K1L10_n48.json ../box207/inst/CFI3_n48.json ../box207/inst/RINT_n48.json ../box203/inst/MWR4_2.json ../box206/inst/CW4_n.json ../box206/inst/BLKX26_n48.json ../box206/inst/K1D4_n48.json ../box191/inst/DEAD_SEG2P_d7_N14.json"
touch out/rf212_mut.out
for r in howard onebest oneleast allleast; do for f in $BASES; do
  b=$(basename $f)
  grep -q "^mut $b 2190 20 RULE $r \|^TIMEOUT $b RULE $r$" out/rf212_mut.out && continue
  RULE=$r SEED=2191 timeout 1800 python3 -I rf212.py --mut 2190 20 $f > out/onem.tmp 2>&1; rc=$?
  if [ $rc -eq 124 ]; then echo "TIMEOUT $b RULE $r" >> out/rf212_mut.out; else cat out/onem.tmp >> out/rf212_mut.out; fi
done; done; rm -f out/onem.tmp
o=out/rf212_ctrlw.out
[ -s $o ] || { RULE=worsen python3 -I rf212.py --rand 2180 30 rand,cyc,self | grep -v '^VIOLATION' > $o.tmp 2>&1 && mv $o.tmp $o; }
echo "run212m finished"
}
main "$@"; exit $?
