#!/bin/bash
# L-COMP box 34: the cross-check batch (item 3) and the N = 3 sample (item 2), sequential, one CPU.
# Needs LNEW_OLD (claude/l-new b61c2029 tree) and LNEW_FIX (f98e93ee tree). Each line writes out/<name>.txt; skips files that have a SUMMARY.
cd "$(dirname "$0")" || exit 1
L=$LNEW_FIX/experiments/new
run() { local out=out/$1.txt; shift; grep -q '^SUMMARY' "$out" 2>/dev/null && { echo "skip $out"; return; }; python3 cmp34.py "$@" "$out.tmp" > /dev/null; mv "$out.tmp" "$out"; tail -1 "$out" | cut -c1-260; }
runf() { local out=out/$1.txt; shift; local fl=$1; shift; grep -q '^SUMMARY' "$out" 2>/dev/null && { echo "skip $out"; return; }; python3 cmp34.py 0 0 0 0 "$out.tmp" $fl --files "$@" > /dev/null; mv "$out.tmp" "$out"; tail -1 "$out" | cut -c1-260; }
case "$1" in
xcheck)
  runf argmax_noelev --noelev ../box33/out/ARGMAX_*.json
  runf pinned_rest_elev "" $(ls $L/box19[1-5]/inst/*.json $L/box197/hfam/H[0-9][ABC].json | grep -v DEAD_SEGT_n20)   # genome files only (DEAD_SEGT_n20 and hfam *.names.json are not genomes)
  for NM in "1 1" "1 2" "1 3" "1 4" "2 2" "2 3" "2 4"; do set -- $NM
    run x_N$1M$2_elev $1 $2 2000 34$1$2
    run x_N$1M$2_noelev $1 $2 2000 34$1$2 --noelev
  done ;;
n3)
  for M in 3 4 5 6 7; do
    run n3_M${M}_elev 3 $M 20000 343$M
    run n3_M${M}_noelev 3 $M 20000 343$M --noelev
  done ;;
esac
