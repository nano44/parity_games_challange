#!/usr/bin/env bash
# L-SI box 70 self-check (~10 s; needs python-sat, skipped without it): the SAT frame ABS-m + IM reproduces the exact m = 2 values
# (T_0 = 4, T_1 = 5, T_0 + T_1 = 9; without IM T_1 = 7 = ABS-2 of box 69).
set -euo pipefail
cd "$(dirname "$0")"
python3 -I -c "import pysat" 2>/dev/null || { echo "box 70: python-sat not installed, frame check skipped"; exit 0; }
r() { local o; o=$(python3 -I frame.py "$@"); printf '%s\n' "${o%%$'\n'*}" | grep -o -- "-> [A-Z]*"; }
[ "$(r 2 t0 4)" = "-> SAT" ]; [ "$(r 2 t0 5)" = "-> UNSAT" ]
[ "$(r 2 t1 5)" = "-> SAT" ]; [ "$(r 2 t1 6)" = "-> UNSAT" ]
[ "$(r 2 sum 4 5)" = "-> SAT" ]; [ "$(r 2 sum 4 6)" = "-> UNSAT" ]
[ "$(NOIM=1 r 2 t1 7)" = "-> SAT" ]; [ "$(NOIM=1 r 2 t1 8)" = "-> UNSAT" ]
echo "box 70 frame m = 2 validation: PASS"
