#!/bin/bash
# L-COMP box 34 (a): cross-check own34 vs asc197 (f98e93ee, b61c2029) on L-NEW's pinned genomes (box191-195/inst, box197/hfam H*[ABC];
# DEAD_SEGT_n20 and *.names.json are not genomes), ONE genome per cmp34 call with a per-genome timeout T (default 600 s; a timeout is
# recorded as TIMEOUT, not as a pass). Resumable: genomes already in OUT are skipped. Usage: LNEW_OLD=.. LNEW_FIX=.. pin34.sh OUT [T]
cd "$(dirname "$0")" || exit 1
OUT=$1; T=${2:-600}; L=$LNEW_FIX/experiments/new; touch "$OUT"
for f in $(ls $L/box19[1-5]/inst/*.json $L/box197/hfam/H[0-9][ABC].json | grep -v DEAD_SEGT_n20); do
  nm=${f#$L/}; grep -q " $nm " "$OUT" && continue
  tmp=$(mktemp); timeout "$T" python3 cmp34.py 0 0 0 0 "$tmp" --files "$f" > /dev/null 2>&1; rc=$?
  if [ $rc -eq 124 ]; then echo "TIMEOUT $nm $T s" >> "$OUT"
  else line=$(grep -E '^(OK|MISMATCH|GAME-MISMATCH|REF-ERR)' "$tmp" | head -1); echo "${line%% *} $nm ${line#* * }" | cut -c1-400 >> "$OUT"; fi
  rm -f "$tmp" "$tmp.tmp"
done
echo "DONE $(grep -c '^OK' "$OUT") OK, $(grep -c 'MISMATCH' "$OUT") MISMATCH, $(grep -c '^TIMEOUT' "$OUT") TIMEOUT, $(grep -c '^REF-ERR' "$OUT") REF-ERR" >> "$OUT"
