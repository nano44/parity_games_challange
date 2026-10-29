#!/bin/bash
# L-NEW box 64: frozen.py --wrun over a list (from experiments/new), 3 jobs, 600 s per game. Usage: box64/wrun.sh LIST OUT
LIST=$1; OUT=$2; : > "$OUT"
one() { X() { [ -e "../$1" ] && echo "../$1" || echo "../../$1"; }; g=$(X "$1")
  r=$(timeout 600 python3 -I box64/frozen.py "$g" --wrun 2>&1 | tail -1); printf '%s\n' "GAME $1 rc=$? $r"; }
export -f one
grep -v '^#' "$LIST" | grep . | xargs -P 3 -I{} bash -c 'one "{}"' >> "$OUT"
