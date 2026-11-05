#!/usr/bin/env bash
# L-SI box 71 self-check (~20 s; needs python-sat and gcc, skipped without them): the box 70 frame's k-flip mode reproduces L-COMP's exact
# m = 2 values T_1 = 5, T_2 = 7, T_inf = 9; a DIMACS + DRUP dump of «m 2, T_1 >= 6» is RUP-verified by L-COMP's drup.c (ref/).
set -euo pipefail
cd "$(dirname "$0")"
# INF-2 kill at m = 3 (pin/inf18_m3.json): T_inf = 18 > 2 T^R(3) + 1 = 17, by flipdp.py (all self-checks 0)
sha1sum -c --quiet pin/pins.sha1
python3 -I - <<'PY'
import sys, json; sys.path.insert(0, '../box64'); from flipdp import analyse
r = analyse(json.load(open('pin/inf18_m3.json')), K=3); assert r['Tinf'] == 18 and r['T'] == [3, 5, 6, 8] and not r['bad'], r
PY
echo "box 71 INF-2 kill pin: PASS"
python3 -I -c "import pysat" 2>/dev/null && command -v gcc >/dev/null || { echo "box 71: python-sat or gcc missing, skipped"; exit 0; }
r() { local o; o=$(K=$1 python3 -I ../box70/frame.py 2 tk $2); printf '%s\n' "$o" | grep -o -- "-> [A-Z]*" | head -n 1; }
[ "$(r 2 7)" = "-> SAT" ]; [ "$(r 2 8)" = "-> UNSAT" ]; [ "$(r -1 9)" = "-> SAT" ]; [ "$(r -1 10)" = "-> UNSAT" ]
d=$(mktemp -d); gcc -O2 -o "$d/drup" ref/drup.c
K=1 DUMP="$d" python3 -I ../box70/frame.py 2 tk 6 > "$d/out.txt"
grep -q -- "-> UNSAT" "$d/out.txt"
"$d/drup" "$d/m2_tk_T6_T20_K1_NOIM0.cnf" "$d/m2_tk_T6_T20_K1_NOIM0.drup" | grep -q "s VERIFIED"
rm -rf "$d"
echo "box 71 k-flip frame + DRUP: PASS"
