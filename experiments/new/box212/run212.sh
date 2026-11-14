#!/bin/bash
# Box 212 RF-LEVEL (L-NEW successor 74): DATA runs of rf212.py (any improving rule on IDEAL-CYC(G); rv208.py's builder, valuation and
# Odd reply). Resumable: a finished (genome, rule) line or output file is skipped. Run from experiments/new/box212:  bash run212.sh A | B | C | D
#   A: the frozen set of box 208 Addendum B (25 k = 1 records, 53 corpus genomes, 3 DEAD genomes of RESULTS R118 (m)) under every rule,
#      one (genome, rule) at a time, timeout 1200 s each (a timeout is written as a TIMEOUT line, i.e. NOT checked);
#   B: rv208's random genomes (seeds 2121-2127, 300 each, modes rand,cyc,self,up,down,dense,flat), one seed per rule;
#   C: random mover start states (5 per genome) on eight frozen bases under every rule;
#   D: control RF_CTRL=1 (must fire L-counters).
#   E: rfd212.py (N5 itself on Gamma3(G) up to its first fallback; RFD_MODE spec, then seq and idx) on the same frozen set, one genome at
#      a time, timeout 1200 s each (TIMEOUT line = NOT checked);
#   F: rfd212.py --rand on eg195 genomes (modes rand, dense, deep, noesc; 300 each; seed 2150 + i) under spec, seq, idx;
#   G: controls of rfd212.py (RFD_CTRL=1: imp3 must fire; LV_CTRL=2: l3fail must fire).
# Outputs in out/.
set -u
export PYTHONDONTWRITEBYTECODE=1
main() {   # one function: bash has read the whole script before it runs anything
mkdir -p out
REC="../box203/inst/MWR4_2.json ../box203/inst/MWR8_2.json ../box203/inst/MWR16_2.json ../box206/inst/CW4_n.json ../box206/inst/CW8_n.json ../box206/inst/CW16_n.json
../box206/inst/CWRR4_n.json ../box206/inst/CWRR8_n.json ../box206/inst/CWRR16_n.json ../box206/inst/CWRQ8_n.json ../box203/inst/K1F21_n48.json ../box204/inst/K1F34_n84.json
../box203/inst/K1C16_n400.json ../box206/inst/K1L7_n48.json ../box206/inst/K1L10_n48.json ../box206/inst/K1D4_n48.json ../box206/inst/BLKX23_n48.json ../box206/inst/BLKX26_n48.json
../box204/inst/B400_r32_a13d9661.json ../box207/inst/CFI3_n48.json ../box207/inst/RINT_n48.json ../box202/k1fail_202.json ../box205/inst/naive_k1_s71.json
../box203/inst/ST4_k1.json ../box203/inst/ST8_k1.json"
ALL="$REC $(ls ../box202/inst/*.json) ../box191/inst/DEAD_SEG2P_d4_N8.json ../box191/inst/DEAD_SEG2P_d7_N14.json ../box191/inst/DEAD_SEG2P_d9_N18.json"
RULES="howard allrand allleast onebest onerand oneleast subrand"
case "${1:-A}" in
A)
  touch out/rf212_frozen.out
  for r in $RULES; do for f in $ALL; do
    b=$(basename $f)
    grep -q "^$b RULE $r \|^TIMEOUT $b RULE $r$" out/rf212_frozen.out && continue
    RULE=$r SEED=212 timeout 1200 python3 -I rf212.py $f > out/one.tmp 2>&1; rc=$?
    if [ $rc -eq 124 ]; then echo "TIMEOUT $b RULE $r" >> out/rf212_frozen.out; else cat out/one.tmp >> out/rf212_frozen.out; fi
  done; done; rm -f out/one.tmp ;;
B)
  s=2121
  for r in $RULES; do
    o=out/rf212_rand_$r.out
    [ -s $o ] || { RULE=$r SEED=$s python3 -I rf212.py --rand $s 300 rand,cyc,self,up,down,dense,flat > $o.tmp 2>&1 && mv $o.tmp $o; }
    s=$((s + 1))
  done ;;
C)
  BASES="../box206/inst/K1L10_n48.json ../box207/inst/CFI3_n48.json ../box207/inst/RINT_n48.json ../box203/inst/MWR4_2.json ../box206/inst/CW4_n.json ../box206/inst/BLKX26_n48.json ../box206/inst/K1D4_n48.json ../box191/inst/DEAD_SEG2P_d7_N14.json"
  for r in $RULES; do
    o=out/rf212_rstart_$r.out
    [ -s $o ] || { RULE=$r SEED=2130 timeout 5400 python3 -I rf212.py --rstart 2131 5 $BASES > $o.tmp 2>&1 && mv $o.tmp $o; }
  done ;;
D)
  o=out/rf212_ctrl.out
  [ -s $o ] || { for r in howard onerand; do RF_CTRL=1 RULE=$r python3 -I rf212.py --rand 2140 30 cyc,self | grep -v '^VIOLATION'; done > $o.tmp 2>&1 && mv $o.tmp $o; } ;;
E)
  touch out/rfd212_frozen.out
  for r in spec seq idx; do for f in $ALL; do
    b=$(basename $f)
    grep -q "^$b RFD_MODE $r \|^TIMEOUT $b RFD_MODE $r$" out/rfd212_frozen.out && continue
    RFD_MODE=$r timeout 1200 python3 -I rfd212.py $f > out/oneE.tmp 2>&1; rc=$?
    if [ $rc -eq 124 ]; then echo "TIMEOUT $b RFD_MODE $r" >> out/rfd212_frozen.out; else cat out/oneE.tmp >> out/rfd212_frozen.out; fi
  done; done; rm -f out/oneE.tmp ;;
F)
  for r in spec seq idx; do i=0; for m in rand dense deep noesc; do
    o=out/rfd212_rand_${r}_$m.out
    [ -s $o ] || { RFD_MODE=$r timeout 5400 python3 -I rfd212.py --rand $((2150 + i)) 300 $m > $o.tmp 2>&1 && mv $o.tmp $o; }
    i=$((i + 1))
  done; done ;;
G)
  o=out/rfd212_ctrl.out
  [ -s $o ] || { { RFD_CTRL=1 python3 -I rfd212.py --rand 2160 50 rand; LV_CTRL=2 python3 -I rfd212.py --rand 2161 50 rand; } > $o.tmp 2>&1 && mv $o.tmp $o; } ;;
esac
echo "run212 ${1:-A} finished"
}
main "$@"; exit $?
