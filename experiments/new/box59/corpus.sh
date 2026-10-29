#!/bin/bash
# L-NEW box 59: frec.py over a list (paths relative to experiments/ or the repo root), SPEC S3 default start, 3 jobs, 600 s per game.
# Usage (from experiments/new): box59/corpus.sh LIST OUT
LIST=$1; OUT=$2; : > "$OUT"
one() { X() { [ -e "../$1" ] && echo "../$1" || echo "../../$1"; }; g=$(X "$1")
  r=$(timeout 600 python3 -I box59/frec.py "$g" 2>&1 | tail -1); printf '%s\n' "GAME $1 rc=$? $r"; }
export -f one
grep -v '^#' "$LIST" | grep . | xargs -P 3 -I{} bash -c 'one "{}"' >> "$OUT"
