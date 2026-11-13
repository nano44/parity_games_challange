#!/bin/bash
# Box 208 Addendum B (L-NEW successor 72): DATA runs of the THIRD implementation rv208.py (own builder, valuation, Odd response, Howard
# run and counters; every reference state b), resumable. Run from experiments/new/box208:  bash run208c.sh J | K
#   J: every b, on the 25 k = 1 records, the 53 corpus genomes and the 3 genomes of RESULTS R118 (m), genome by genome;
#   K: --xcheck against box191 idealcyc / si.Engine on the same files (state by state), own mutants of eight frozen bases, own random
#      genomes, and the control RV_CTRL=1.
# Outputs in out/.
set -u
export PYTHONDONTWRITEBYTECODE=1
main() {   # one function: bash has read the whole script before it runs anything
REC="../box203/inst/MWR4_2.json ../box203/inst/MWR8_2.json ../box203/inst/MWR16_2.json ../box206/inst/CW4_n.json ../box206/inst/CW8_n.json ../box206/inst/CW16_n.json
../box206/inst/CWRR4_n.json ../box206/inst/CWRR8_n.json ../box206/inst/CWRR16_n.json ../box206/inst/CWRQ8_n.json ../box203/inst/K1F21_n48.json ../box204/inst/K1F34_n84.json
../box203/inst/K1C16_n400.json ../box206/inst/K1L7_n48.json ../box206/inst/K1L10_n48.json ../box206/inst/K1D4_n48.json ../box206/inst/BLKX23_n48.json ../box206/inst/BLKX26_n48.json
../box204/inst/B400_r32_a13d9661.json ../box207/inst/CFI3_n48.json ../box207/inst/RINT_n48.json ../box202/k1fail_202.json ../box205/inst/naive_k1_s71.json
../box203/inst/ST4_k1.json ../box203/inst/ST8_k1.json"
ALL="$REC $(ls ../box202/inst/*.json) ../box191/inst/DEAD_SEG2P_d4_N8.json ../box191/inst/DEAD_SEG2P_d7_N14.json ../box191/inst/DEAD_SEG2P_d9_N18.json"
one() { local out="out/$1"; shift; [ -s "$out" ] && return 0; "$@" > "$out.tmp" 2>&1 && mv "$out.tmp" "$out"; }
case "${1:-J}" in
J)
  touch out/rv208_frozen.out
  for f in $ALL; do grep -q "^$(basename $f) " out/rv208_frozen.out || timeout 6000 python3 rv208.py $f >> out/rv208_frozen.out 2>&1; done ;;
K)
  one rv208_xcheck.out python3 rv208.py --xcheck $ALL
  one rv208_mut_s2094.out python3 rv208.py --mut 2094 60 ../box206/inst/K1L10_n48.json ../box207/inst/CFI3_n48.json ../box207/inst/RINT_n48.json ../box203/inst/MWR4_2.json ../box206/inst/CW4_n.json ../box206/inst/BLKX26_n48.json ../box206/inst/K1D4_n48.json ../box202/inst/DSALT6_n108.json
  one rv208_rand_s2095.out bash -c 'python3 rv208.py --rand 2095 2000 rand,cyc,self,up,down,dense,flat; TIE=min python3 rv208.py --rand 2096 1000 rand,cyc,self,up,down,dense,flat | sed "s/^/tiemin /"; python3 rv208.py --rand 2097 300 big'
  RV_CTRL=1 one rv208_ctrl1.out bash -c 'python3 rv208.py --T ../box203/inst/MWR4_2.json ../box207/inst/CFI3_n48.json 2>&1 | grep -v "^VIOLATION"' ;;
esac
echo "run208c ${1:-J} finished"
}
main "$@"; exit $?
