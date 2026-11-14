#!/bin/bash
# Box 208 (L-NEW successor 72): the DATA runs of docs/new/N5-LEVEL-box208.md §6, resumable (a set is skipped when its output exists;
# the corpus is appended genome by genome). Run from experiments/new/box208:  bash run208.sh A | B | C | D | E | F | G   (A: records + controls + corpus;
# B: random sets on IDEAL-CYC; C: Gamma3 runs, DATA only; D: mutation sweeps around frozen k = 1 genomes, long runs; E: the abstract shortest-path game, own engine; F, G: Addendum A's plateau counters, plat208.py). Outputs in out/.
set -u
export PYTHONDONTWRITEBYTECODE=1
REC="../box203/inst/MWR4_2.json ../box203/inst/MWR8_2.json ../box203/inst/MWR16_2.json ../box206/inst/CW4_n.json ../box206/inst/CW8_n.json ../box206/inst/CW16_n.json
../box206/inst/CWRR4_n.json ../box206/inst/CWRR8_n.json ../box206/inst/CWRR16_n.json ../box206/inst/CWRQ8_n.json ../box203/inst/K1F21_n48.json ../box204/inst/K1F34_n84.json
../box203/inst/K1C16_n400.json ../box206/inst/K1L7_n48.json ../box206/inst/K1L10_n48.json ../box206/inst/K1D4_n48.json ../box206/inst/BLKX23_n48.json ../box206/inst/BLKX26_n48.json
../box204/inst/B400_r32_a13d9661.json ../box207/inst/CFI3_n48.json ../box207/inst/RINT_n48.json ../box202/k1fail_202.json ../box205/inst/naive_k1_s71.json
../box203/inst/ST4_k1.json ../box203/inst/ST8_k1.json"
one() { # one OUT cmd...
  local out="out/$1"; shift
  [ -s "$out" ] && return 0
  "$@" > "$out.tmp" 2>&1 && mv "$out.tmp" "$out"
}
case "${1:-A}" in
A)
  one level208_records.out python3 level208.py $REC
  LV_CTRL=1 one level208_ctrl1.out python3 level208.py ../box207/inst/CFI3_n48.json ../box207/inst/RINT_n48.json ../box206/inst/K1L10_n48.json ../box203/inst/MWR4_2.json
  LV_CTRL=2 one level208_ctrl2.out python3 level208.py ../box207/inst/CFI3_n48.json ../box203/inst/MWR4_2.json ../box202/inst/WC8_2.json
  touch out/level208_corpus.out
  for f in ../box202/inst/*.json; do
    grep -q "^$(basename $f) " out/level208_corpus.out || timeout 3000 python3 level208.py $f >> out/level208_corpus.out 2>&1
  done ;;
B)
  one level208_rand_k1_s2081.out python3 level208.py --rand 2081 2000 k1
  for m in rand dense deep noesc esc lvl0; do one level208_rand_${m}_s2082.out python3 level208.py --rand 2082 500 $m; done
  LV_CTRL=1 one level208_ctrl1_rand_k1_s2083.out python3 level208.py --rand 2083 300 k1 ;;
C)
  one level208_g3_records.out python3 level208.py --g3 ../box203/inst/MWR4_2.json ../box203/inst/MWR8_2.json ../box207/inst/CFI3_n48.json ../box207/inst/RINT_n48.json ../box206/inst/K1L10_n48.json ../box206/inst/CW8_n.json ../box202/k1fail_202.json ../box202/inst/WC8_2.json
  one level208_g3_rand_k1_s2084.out python3 level208.py --g3 --rand 2084 500 k1
  one level208_g3_rand_rand_s2085.out python3 level208.py --g3 --rand 2085 300 rand ;;
D)
  for b in ../box206/inst/K1L10_n48.json ../box207/inst/CFI3_n48.json ../box207/inst/RINT_n48.json ../box203/inst/MWR4_2.json ../box206/inst/CW4_n.json ../box206/inst/BLKX26_n48.json ../box206/inst/K1L7_n48.json ../box203/inst/K1F21_n48.json; do
    one mut208_$(basename $b .json)_s2086.out python3 mut208.py 2086 250 6 $b
  done ;;
E)
  one abs208.out bash -c 'python3 abs208.py 11 30000 9 0; python3 abs208.py 12 20000 30 0; python3 abs208.py 13 20000 30 1; python3 abs208.py 14 3000 120 0; ABS_CTRL=1 python3 abs208.py 3 500 8 0' ;;
F)
  one plat208_records.out python3 plat208.py $REC
  touch out/plat208_corpus.out
  for f in ../box202/inst/*.json; do
    grep -q "^plat $(basename $f) " out/plat208_corpus.out || timeout 3000 python3 plat208.py $f >> out/plat208_corpus.out 2>&1
  done ;;
G)
  one plat208_rand_s2091.out bash -c 'for m in k1 rand dense deep noesc lvl0; do python3 plat208.py --rand 2091 600 $m; done'
  one plat208_mut_s2092.out bash -c 'for b in ../box206/inst/K1L10_n48.json ../box207/inst/CFI3_n48.json ../box206/inst/K1D4_n48.json ../box202/inst/DSALT6_n108.json; do python3 plat208.py --mut 2092 150 $b; done'
  PL_CTRL=1 one plat208_ctrl1.out python3 plat208.py ../box207/inst/CFI3_n48.json ../box206/inst/K1D4_n48.json ../box202/inst/DSALT6_n108.json ;;
esac
echo "run208 ${1:-A} finished"
