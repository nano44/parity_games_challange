#!/bin/bash
# Box 209 (L-NEW successor 72): the DATA runs of docs/new/N5-LEVEL3-box209.md §6, resumable (a set is skipped when its output exists;
# per-genome sets are appended genome by genome). Run from experiments/new/box209:  bash run209.sh A | B | C | D | E
#   A: level208.py --g3 and plat209.py on the 25 k = 1 records, the 53 corpus genomes and the 3 genomes of RESULTS R118 (m) (engine:
#      N5'-xi from S3 on Gamma3(G), n5v); struct209.py (the construction readings) on the same files and on random genomes;
#   B: random sets;  C: mutation sweeps;  D: controls;
#   E: the SECOND ENGINE: L-RED 65's own HOW3 engine (claude/l-red 707c0e82 experiments/red/r232/how3_232.py with r230, r221q; read by
#      `git archive` into a temporary directory, not copied into this lane) through own3hist209.py, level208.py --hist, plat209.py --hist.
# Outputs in out/.
set -u
export PYTHONDONTWRITEBYTECODE=1
main() {   # the whole script is one function, so bash has read all of it before it runs anything (safe against edits while running)
L=../box208/level208.py
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
per() { # per OUT PREFIX-of-line cmd... file : append one genome's line unless present
  local out="out/$1" pre="$2" f="${@: -1}"; shift 2
  touch "$out"; grep -q "^$pre$(basename $f) " "$out" || timeout 6000 "$@" >> "$out" 2>&1
}
case "${1:-A}" in
A)
  for f in $REC; do per level3_records.out "" python3 $L --g3 $f; per plat3_records.out "plat3 " python3 plat209.py $f; done
  for f in ../box202/inst/*.json; do per level3_corpus.out "" python3 $L --g3 $f; per plat3_corpus.out "plat3 " python3 plat209.py $f; done
  for f in ../box191/inst/DEAD_SEG2P_d4_N8.json ../box191/inst/DEAD_SEG2P_d7_N14.json ../box191/inst/DEAD_SEG2P_d9_N18.json; do per level3_dead.out "" python3 $L --g3 $f; per plat3_dead.out "plat3 " python3 plat209.py $f; done
  one struct3.out bash -c 'python3 struct209.py $0 ../box202/inst/*.json ../box191/inst/DEAD_SEG2P_*.json; for m in k1 rand dense deep noesc esc lvl0; do python3 struct209.py --rand 2106 300 $m; done' "$REC" ;;
B)
  one level3_rand_k1_s2101.out python3 $L --g3 --rand 2101 1000 k1
  for m in rand dense deep noesc esc lvl0; do one level3_rand_${m}_s2102.out python3 $L --g3 --rand 2102 300 $m; done
  one plat3_rand_s2103.out bash -c 'for m in k1 rand dense deep noesc esc lvl0; do python3 plat209.py --rand 2103 400 $m; done' ;;
C)
  one plat3_mut_s2104.out bash -c 'for b in ../box206/inst/K1L10_n48.json ../box207/inst/CFI3_n48.json ../box206/inst/K1D4_n48.json ../box203/inst/K1F21_n48.json ../box206/inst/BLKX26_n48.json ../box203/inst/MWR4_2.json ../box206/inst/CW4_n.json ../box207/inst/RINT_n48.json; do python3 plat209.py --mut 2104 150 $b; done' ;;
D)
  LV_CTRL=1 one level3_ctrl1.out python3 $L --g3 ../box207/inst/CFI3_n48.json ../box207/inst/RINT_n48.json ../box206/inst/K1L10_n48.json ../box203/inst/MWR4_2.json
  LV_CTRL=2 one level3_ctrl2.out python3 $L --g3 ../box207/inst/CFI3_n48.json ../box203/inst/MWR4_2.json ../box202/inst/WC8_2.json
  PL_CTRL=1 one plat3_ctrl1.out python3 plat209.py ../box207/inst/CFI3_n48.json ../box206/inst/K1D4_n48.json ../box202/inst/DSALT6_n108.json ;;
E)
  t=$(mktemp -d); R=707c0e82bd514e8f76b7ba8a6d67b1e0ccca045c
  git -C "$(git rev-parse --show-toplevel)" archive $R experiments/red/r230 experiments/red/r221q experiments/red/r232 | tar -x -C "$t" || { echo "l-red commit not available"; exit 1; }
  t="$t/experiments/red"
  ( cd "$t" && sha1sum r232/how3_232.py r230/elev230.py r230/bonly3_230.py r221q/own.py ) | sed "s/\$/ (claude\/l-red ${R:0:8})/" > out/own3_engine.sha1
  export LNEW=$(cd ../../.. && pwd)
  for set in records corpus dead; do
    touch out/own3_level_$set.out out/own3_plat_$set.out
    for f in $(case $set in records) echo $REC;; corpus) ls ../box202/inst/*.json;; dead) ls ../box191/inst/DEAD_SEG2P_*.json;; esac); do
      b=$(basename $f .json)
      grep -q "^$b.json " out/own3_level_$set.out && grep -q "^plat3 hist $b.json " out/own3_plat_$set.out && continue
      timeout 6000 python3 own3hist209.py "$t" $f "$t/$b.json" > /dev/null 2>&1 || { echo "$b.json ENGINE FAILED" >> out/own3_fail.out; continue; }
      grep -q "^$b.json " out/own3_level_$set.out || python3 $L --hist "$t/$b.json" >> out/own3_level_$set.out 2>&1
      grep -q "^plat3 hist $b.json " out/own3_plat_$set.out || python3 plat209.py --hist "$t/$b.json" >> out/own3_plat_$set.out 2>&1
      rm -f "$t/$b.json"
    done
  done
  rm -rf "$(dirname "$(dirname "$t")")" ;;
esac
echo "run209 ${1:-A} finished"
}
main "$@"; exit $?
