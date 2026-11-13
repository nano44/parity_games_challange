#!/bin/bash
# L-COMP box 46 item 1: win46.py (mine) on box 212's 5 tower genomes and the 81 frozen genomes (L-NEW records 25, corpus 53, dead 3),
# from an archive of claude/l-new 5fa64fe6 (env LNEW212). Resumable per genome. Usage: run46a.sh mine
set -u; cd "$(dirname "$0")"; export PYTHONDONTWRITEBYTECODE=1; mkdir -p out
main() {
: "${LNEW212:?set LNEW212}"; N="$LNEW212/experiments/new"
REC="$N/box203/inst/MWR4_2.json $N/box203/inst/MWR8_2.json $N/box203/inst/MWR16_2.json $N/box206/inst/CW4_n.json $N/box206/inst/CW8_n.json $N/box206/inst/CW16_n.json
$N/box206/inst/CWRR4_n.json $N/box206/inst/CWRR8_n.json $N/box206/inst/CWRR16_n.json $N/box206/inst/CWRQ8_n.json $N/box203/inst/K1F21_n48.json $N/box204/inst/K1F34_n84.json
$N/box203/inst/K1C16_n400.json $N/box206/inst/K1L7_n48.json $N/box206/inst/K1L10_n48.json $N/box206/inst/K1D4_n48.json $N/box206/inst/BLKX23_n48.json $N/box206/inst/BLKX26_n48.json
$N/box204/inst/B400_r32_a13d9661.json $N/box207/inst/CFI3_n48.json $N/box207/inst/RINT_n48.json $N/box202/k1fail_202.json $N/box205/inst/naive_k1_s71.json
$N/box203/inst/ST4_k1.json $N/box203/inst/ST8_k1.json"
DEAD="$N/box191/inst/DEAD_SEG2P_d4_N8.json $N/box191/inst/DEAD_SEG2P_d7_N14.json $N/box191/inst/DEAD_SEG2P_d9_N18.json"
per() { local out="out/$1"; shift; touch "$out"; for f in "$@"; do b=$(basename $f); grep -q "^$b " "$out" || python3 win46.py $f >> "$out" 2>> "$out.err"; done; }
case "$1" in
mine) per win46_tower.out $N/box212/inst/*.json; per win46_records.out $REC; per win46_dead.out $DEAD; per win46_corpus.out $N/box202/inst/*.json ;;
*) echo usage; exit 2 ;;
esac
echo "run46a $1 done"
}
main "$@"
