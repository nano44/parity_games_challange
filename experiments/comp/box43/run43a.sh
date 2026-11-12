#!/bin/bash
# L-COMP box 43 item 1 (a): MY engine's history (hist43.py on box37/ideal37.py) through L-NEW 72's counters: level208.py --hist (the 16
# must-0 counters) and plat208.plateaus (plathist43.py). Resumable: a genome whose line exists in the output is skipped.
# env LNEW208 = archive of claude/l-new 8db300fe (experiments/new, experiments/si/si.py, experiments/harness); TMPD = a scratch directory.
# Usage: run43a.sh records|corpus|mine     (records = the 25 k = 1 genomes of box 208 §7; corpus = box202/inst; mine = box39/inst + box40/inst)
set -u; cd "$(dirname "$0")"; export PYTHONDONTWRITEBYTECODE=1
: "${LNEW208:?set LNEW208}"; : "${TMPD:?set TMPD}"; mkdir -p "$TMPD" out
N="$LNEW208/experiments/new"
case "$1" in
records) L="$N/box203/inst/MWR4_2.json $N/box203/inst/MWR8_2.json $N/box203/inst/MWR16_2.json $N/box206/inst/CW4_n.json $N/box206/inst/CW8_n.json $N/box206/inst/CW16_n.json
$N/box206/inst/CWRR4_n.json $N/box206/inst/CWRR8_n.json $N/box206/inst/CWRR16_n.json $N/box206/inst/CWRQ8_n.json $N/box203/inst/K1F21_n48.json $N/box204/inst/K1F34_n84.json
$N/box203/inst/K1C16_n400.json $N/box206/inst/K1L7_n48.json $N/box206/inst/K1L10_n48.json $N/box206/inst/K1D4_n48.json $N/box206/inst/BLKX23_n48.json $N/box206/inst/BLKX26_n48.json
$N/box204/inst/B400_r32_a13d9661.json $N/box207/inst/CFI3_n48.json $N/box207/inst/RINT_n48.json $N/box202/k1fail_202.json $N/box205/inst/naive_k1_s71.json
$N/box203/inst/ST4_k1.json $N/box203/inst/ST8_k1.json" ;;
corpus) L="$(ls $N/box202/inst/*.json)" ;;
mine) L="$(ls ../box39/inst/*.json ../box40/inst/*.json)" ;;
*) echo "usage"; exit 2 ;;
esac
touch out/level43_$1.out out/plat43_$1.out
for f in $L; do
  b=$(basename $f .json)
  if ! grep -q "^$b.json " out/level43_$1.out; then
    python3 hist43.py $f "$TMPD/$b.json" > /dev/null 2>> out/run43a_$1.err || { echo "HIST FAILED $b" >> out/run43a_$1.err; continue; }
    (cd "$N/box208" && python3 level208.py --hist "$TMPD/$b.json") >> out/level43_$1.out 2>> out/run43a_$1.err
  fi
  if ! grep -q "^plat $b.json " out/plat43_$1.out; then
    [ -s "$TMPD/$b.json" ] || python3 hist43.py $f "$TMPD/$b.json" > /dev/null 2>> out/run43a_$1.err
    python3 plathist43.py "$TMPD/$b.json" >> out/plat43_$1.out 2>> out/run43a_$1.err
  fi
  rm -f "$TMPD/$b.json"
done
echo "run43a $1 done: $(wc -l < out/level43_$1.out) level lines, $(wc -l < out/plat43_$1.out) plat lines"
