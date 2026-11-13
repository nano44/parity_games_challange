#!/bin/bash
# Box 212: second worker of run212a2.sh (rule oneleast only, same settings). Continuation of run212.sh A (stopped 21:33Z by the lane: 1200 s per (genome, rule) was too slow for the single-switch rules on
# the large genomes). Same set, same rules, same command; timeout 300 s per (genome, rule), written «TIMEOUT300 <genome> RULE <rule>»
# (NOT checked). Lines already in out/rf212_frozen.out are skipped. Run from experiments/new/box212.
set -u
export PYTHONDONTWRITEBYTECODE=1
main() {
REC="../box203/inst/MWR4_2.json ../box203/inst/MWR8_2.json ../box203/inst/MWR16_2.json ../box206/inst/CW4_n.json ../box206/inst/CW8_n.json ../box206/inst/CW16_n.json
../box206/inst/CWRR4_n.json ../box206/inst/CWRR8_n.json ../box206/inst/CWRR16_n.json ../box206/inst/CWRQ8_n.json ../box203/inst/K1F21_n48.json ../box204/inst/K1F34_n84.json
../box203/inst/K1C16_n400.json ../box206/inst/K1L7_n48.json ../box206/inst/K1L10_n48.json ../box206/inst/K1D4_n48.json ../box206/inst/BLKX23_n48.json ../box206/inst/BLKX26_n48.json
../box204/inst/B400_r32_a13d9661.json ../box207/inst/CFI3_n48.json ../box207/inst/RINT_n48.json ../box202/k1fail_202.json ../box205/inst/naive_k1_s71.json
../box203/inst/ST4_k1.json ../box203/inst/ST8_k1.json"
ALL="$REC $(ls ../box202/inst/*.json) ../box191/inst/DEAD_SEG2P_d4_N8.json ../box191/inst/DEAD_SEG2P_d7_N14.json ../box191/inst/DEAD_SEG2P_d9_N18.json"
for r in oneleast; do for f in $ALL; do
  b=$(basename $f)
  grep -q "^$b RULE $r \|^TIMEOUT[0-9]* $b RULE $r$" out/rf212_frozen.out && continue
  RULE=$r SEED=212 timeout 300 python3 -I rf212.py $f > out/one4.tmp 2>&1; rc=$?
  if [ $rc -eq 124 ]; then echo "TIMEOUT300 $b RULE $r" >> out/rf212_frozen.out; else cat out/one4.tmp >> out/rf212_frozen.out; fi
done; done; rm -f out/one4.tmp
echo "run212a4 finished"
}
main "$@"; exit $?
