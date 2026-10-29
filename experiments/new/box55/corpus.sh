#!/bin/bash
# L-NEW box 55: pcheck.py over a list file (paths relative to experiments/ or the repo root); 3 jobs; per-game timeout 600 s.
# Usage (from experiments/new): box55/corpus.sh LIST OUT
LIST=$1; OUT=$2; : > "$OUT"
one() { p=($1); X() { [ -e "../$1" ] && echo "../$1" || echo "../../$1"; }
  g=$(X "${p[0]}"); s=""; [ -n "${p[1]}" ] && s=$(X "${p[1]}")
  r=$(timeout 600 python3 -I box55/pcheck.py "$g" $s 2>&1); rc=$?
  printf '%s\n' "GAME ${p[0]} rc=$rc
$(echo "$r" | grep -E "^ROW|^CHECK|_V")"; }   # one write per game, so parallel jobs do not interleave
export -f one
grep -v '^#' "$LIST" | grep . | xargs -P 3 -I{} bash -c 'one "{}"' >> "$OUT"
echo "games $(grep -c ^GAME "$OUT") pass $(grep -c '^CHECK PASS' "$OUT") fail $(grep -c '^CHECK FAIL' "$OUT") timeout $(grep -c 'rc=124' "$OUT")" >> "$OUT"
