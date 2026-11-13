#!/bin/bash
# Box 208 (L-NEW successor 72): further DATA runs, resumable like run208.sh. Run from experiments/new/box208:  bash run208b.sh H | I
# H: the SECOND ENGINE: L-RED 54's independent IDEAL-CYC implementation (claude/l-red 72e2c5dc experiments/red/r221q/own.py, read by
#    `git show` into a temporary directory, not copied into this lane), its history fed to level208.py --hist: the 25 k = 1 records
#    and the 53 corpus genomes. Needs the l-red commit in the local git objects.
# I: Addendum A's plateau counters on mutants of genomes with long plateaus.
set -u
export PYTHONDONTWRITEBYTECODE=1
REC="../box203/inst/MWR4_2.json ../box203/inst/MWR8_2.json ../box203/inst/MWR16_2.json ../box206/inst/CW4_n.json ../box206/inst/CW8_n.json ../box206/inst/CW16_n.json
../box206/inst/CWRR4_n.json ../box206/inst/CWRR8_n.json ../box206/inst/CWRR16_n.json ../box206/inst/CWRQ8_n.json ../box203/inst/K1F21_n48.json ../box204/inst/K1F34_n84.json
../box203/inst/K1C16_n400.json ../box206/inst/K1L7_n48.json ../box206/inst/K1L10_n48.json ../box206/inst/K1D4_n48.json ../box206/inst/BLKX23_n48.json ../box206/inst/BLKX26_n48.json
../box204/inst/B400_r32_a13d9661.json ../box207/inst/CFI3_n48.json ../box207/inst/RINT_n48.json ../box202/k1fail_202.json ../box205/inst/naive_k1_s71.json
../box203/inst/ST4_k1.json ../box203/inst/ST8_k1.json"
case "${1:-H}" in
H)
  t=$(mktemp -d); git show 72e2c5dcbefa50cf9f61f25d54582b055fcf02ca:experiments/red/r221q/own.py > "$t/own.py" || { echo "l-red commit not available"; exit 1; }
  echo "$(sha1sum < "$t/own.py" | cut -c1-40)  own.py (claude/l-red 72e2c5dc experiments/red/r221q/own.py)" > out/own208_engine.sha1
  for set in records corpus; do
    touch out/own208_$set.out
    for f in $([ $set = records ] && echo $REC || ls ../box202/inst/*.json); do
      b=$(basename $f .json)
      grep -q "^$b.json " out/own208_$set.out && continue
      python3 ownhist208.py "$t/own.py" $f "$t/$b.json" > /dev/null 2>&1 && python3 level208.py --hist "$t/$b.json" >> out/own208_$set.out 2>&1
      rm -f "$t/$b.json"
    done
  done
  rm -rf "$t" ;;
I)
  [ -s out/plat208_mut2_s2093.out ] || { for b in ../box203/inst/MWR4_2.json ../box206/inst/CW4_n.json ../box206/inst/BLKX26_n48.json ../box203/inst/K1F21_n48.json; do python3 plat208.py --mut 2093 150 $b; done > out/plat208_mut2_s2093.out.tmp 2>&1 && mv out/plat208_mut2_s2093.out.tmp out/plat208_mut2_s2093.out; } ;;
esac
echo "run208b ${1:-H} finished"
