#!/bin/bash
# L-NEW box 56: exit.py over a list (paths relative to experiments/ or repo root). Usage (from experiments/new): box56/libexit.sh LIST OUT
: > "$2"
while read -r g s; do [ -z "$g" ] && continue; X() { [ -e "../$1" ] && echo "../$1" || echo "../../$1"; }
  a=$(X "$g"); b=""; [ -n "$s" ] && b=$(X "$s"); echo "GAME $g $(timeout 600 python3 -I box56/exit.py "$a" $b 2>&1 | tail -1)" >> "$2"; done < "$1"
