#!/bin/bash
# L-COMP box 44 item 2: box 209's must-0 counters (lev44.py: my Γ3 builder own34 + my engine n5xi44) on L-NEW's frozen genomes and on
# random genomes / mutants. Resumable per genome. env LNEW209 = an archive of claude/l-new 311bbf81 (experiments/new/box191, box202-207).
# Usage: run44b.sh records | corpus | dead | mine | big | rand | mut | ctrl
set -u; cd "$(dirname "$0")"; export PYTHONDONTWRITEBYTECODE=1
: "${LNEW209:?set LNEW209}"; N="$LNEW209/experiments/new"; mkdir -p out
main() {
per() { # per OUT file... : one line per genome, skipped when present
  local out="out/$1"; shift; touch "$out"
  for f in "$@"; do b=$(basename $f); grep -q "^$b " "$out" || FIRST=1 python3 lev44.py $f >> "$out" 2>> "$out.err"; done
}
REC="$N/box203/inst/MWR4_2.json $N/box203/inst/MWR8_2.json $N/box203/inst/MWR16_2.json $N/box206/inst/CW4_n.json $N/box206/inst/CW8_n.json $N/box206/inst/CW16_n.json
$N/box206/inst/CWRR4_n.json $N/box206/inst/CWRR8_n.json $N/box206/inst/CWRR16_n.json $N/box206/inst/CWRQ8_n.json $N/box203/inst/K1F21_n48.json $N/box204/inst/K1F34_n84.json
$N/box203/inst/K1C16_n400.json $N/box206/inst/K1L7_n48.json $N/box206/inst/K1L10_n48.json $N/box206/inst/K1D4_n48.json $N/box206/inst/BLKX23_n48.json $N/box206/inst/BLKX26_n48.json
$N/box204/inst/B400_r32_a13d9661.json $N/box207/inst/CFI3_n48.json $N/box207/inst/RINT_n48.json $N/box202/k1fail_202.json $N/box205/inst/naive_k1_s71.json
$N/box203/inst/ST4_k1.json $N/box203/inst/ST8_k1.json"
case "$1" in
records) BREF=${BREF:-k:3} per lev44_records.out $REC ;;
corpus)  BREF=${BREF:-k:3} per lev44_corpus.out $N/box202/inst/*.json ;;
dead)    BREF=all per lev44_dead.out $N/box191/inst/DEAD_SEG2P_d4_N8.json $N/box191/inst/DEAD_SEG2P_d7_N14.json $N/box191/inst/DEAD_SEG2P_d9_N18.json ;;
mine)    BREF=${BREF:-k:3} per lev44_mine.out ../box39/inst/*.json ../box40/inst/*.json ../box42/inst/CL0.json ../box42/inst/CL30.json ;;
rand)    for px in 0.6 0.3 0.0; do BREF=all python3 rand44.py rand 4411 300 60 $px out/lev44_rand.out; done
         BREF=all python3 rand44.py rand 4412 100 160 0.3 out/lev44_rand.out ;;
mut)     for b in $N/box207/inst/CFI3_n48.json $N/box206/inst/K1L10_n48.json $N/box203/inst/K1F21_n48.json $N/box203/inst/MWR4_2.json $N/box206/inst/CW4_n.json $N/box206/inst/K1D4_n48.json; do
           BREF=all python3 rand44.py mut 4420 100 $b out/lev44_mut.out; done ;;
big)     BREF=T per lev44_big.out ../box43/inst/TMWR4.json ../box43/inst/TMWR8.json ../box43/inst/TMWR16.json ../box43/inst/TMWR32.json ../box43/inst/MWR32_2.json \
           ../box43/inst/TREC.json ../box43/inst/TC6G8.json ../box43/inst/TDHIB26.json ../box43/inst/D10_k128.json ../box43/inst/D18_k32.json ../box43/inst/D80_k128.json \
           ../box42/inst/CL131.json ../box43/inst/MWR48_2.json ../box43/inst/TMWR48.json ;;
ctrl)    for c in 1 2 3 4 5 6; do LV44_CTRL=$c python3 lev44.py $N/box207/inst/CFI3_n48.json $N/box203/inst/MWR4_2.json $N/box191/inst/DEAD_SEG2P_d4_N8.json > out/lev44_ctrl$c.out; done ;;
*) echo usage; exit 2 ;;
esac
echo "run44b $1 done"
}
main "$@"
