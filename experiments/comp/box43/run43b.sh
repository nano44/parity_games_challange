#!/bin/bash
# L-COMP box 43 item 1: MY counters (lev43.py genome mode, my engine box37/ideal37.py) on the genome sets of run43a.sh. Resumable per genome.
# env LNEW208 = archive of claude/l-new 8db300fe. Usage: run43b.sh records|corpus|mine
set -u; cd "$(dirname "$0")"; export PYTHONDONTWRITEBYTECODE=1
: "${LNEW208:?set LNEW208}"; N="$LNEW208/experiments/new"; mkdir -p out
case "$1" in
records) L="$N/box203/inst/MWR4_2.json $N/box203/inst/MWR8_2.json $N/box203/inst/MWR16_2.json $N/box206/inst/CW4_n.json $N/box206/inst/CW8_n.json $N/box206/inst/CW16_n.json
$N/box206/inst/CWRR4_n.json $N/box206/inst/CWRR8_n.json $N/box206/inst/CWRR16_n.json $N/box206/inst/CWRQ8_n.json $N/box203/inst/K1F21_n48.json $N/box204/inst/K1F34_n84.json
$N/box203/inst/K1C16_n400.json $N/box206/inst/K1L7_n48.json $N/box206/inst/K1L10_n48.json $N/box206/inst/K1D4_n48.json $N/box206/inst/BLKX23_n48.json $N/box206/inst/BLKX26_n48.json
$N/box204/inst/B400_r32_a13d9661.json $N/box207/inst/CFI3_n48.json $N/box207/inst/RINT_n48.json $N/box202/k1fail_202.json $N/box205/inst/naive_k1_s71.json
$N/box203/inst/ST4_k1.json $N/box203/inst/ST8_k1.json" ;;
corpus) L="$(ls $N/box202/inst/*.json)" ;;
mine) L="$(ls ../box39/inst/*.json ../box40/inst/*.json ../box42/inst/CL0.json ../box42/inst/CL30.json)" ;;
*) echo "usage"; exit 2 ;;
esac
touch out/lev43_$1.out
for f in $L; do
  b=$(basename $f)
  grep -q "^$b " out/lev43_$1.out || FIRST=1 python3 lev43.py genome $f >> out/lev43_$1.out 2>> out/run43b_$1.err
done
echo "run43b $1 done: $(grep -c ' genome n ' out/lev43_$1.out) genomes"
