#!/usr/bin/env bash
# L-SI box 75 (packet P-IDEAL-IM) self-check (~15 s): pins (frozen encoder, witness), imcheck.py (IM, BIT-CHAIN, KEY-DIR, VALUE-MONO,
# FRAME step; each with a negative control) reproduces imcheck.out, the witness kf1_d4_t10 has T_1 = 10 (flipdp), and the frozen
# encoder regenerates the certified CNF «m 3 t1 11» with sha1 7e611c8b... (needs python-sat; skipped without it).
set -euo pipefail
cd "$(dirname "$0")"
sha1sum -c --quiet --strict pins.sha1
t=$(mktemp -d)
python3 -I imcheck.py 400 75 > "$t/imc"
diff -q "$t/imc" imcheck.out
python3 -I - <<'PY'
import sys, json; sys.path.insert(0, '../box64'); from flipdp import analyse
r = analyse(json.load(open('../box64/wit/kf1_d4_t10.json')), K=1); assert r['T'] == [5, 10] and not r['bad'], r
PY
# fixes entry 1 (W-2): the COMPOSE DATA of line L-2, seed 68, and its negative control, exact counts
[ "$(cd ../box68 && python3 -I compose.py 200 68 | tail -n 1)" = "COMPOSE random pairs 200 KPART 0 GPART 0" ]
[ "$(cd ../box68 && NEG=1 python3 -I compose.py 200 68 | tail -n 1)" = "COMPOSE random pairs 200 KPART 21234 GPART 54433" ]
# fixes entry 2 (CHECKER C128 E-1..E-5): line L-3 = L-2 with exactly R1-R5 (mkL3.py), pinned with L-2, the fixes file and the script
sha1sum -c --quiet --strict pins_fix2.sha1
python3 -I mkL3.py ../../../docs/si/P-IDEAL-IM-line-L2.txt "$t/L3" > /dev/null
cmp "$t/L3" ../../../docs/si/P-IDEAL-IM-line-L3.txt
[ "$(sha1sum < "$t/L3" | cut -c1-40)" = "cf510950a7feaf3e8d5f3c316acc2601e2ed17e7" ]
echo "box 75 P-IDEAL-IM checks + witness + COMPOSE seed 68: PASS"
python3 -I -c "import pysat" 2>/dev/null || { rm -rf "$t"; echo "box 75: python-sat missing, CNF regeneration skipped"; exit 0; }
o=$(DUMP="$t" DUMPONLY=1 python3 -I frame_P-IDEAL-IM.py 3 t1 11 | grep -o "sha1 [0-9a-f]*")
rm -rf "$t"
[ "$o" = "sha1 7e611c8bdf53a70a398e9e1ec3b220a1b79e2507" ]
echo "box 75 certified CNF regenerated: PASS"
