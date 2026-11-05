#!/usr/bin/env bash
# L-SI box 68 self-check (~20 s): Lemma COMPOSE on 30 random (K, G) pairs (KPART 0, GPART 0); negative control (schedule negated) fails.
set -euo pipefail
cd "$(dirname "$0")"
python3 -I compose.py 30 7 | grep -q "KPART 0 GPART 0"
if NEG=1 python3 -I compose.py 10 8 >/dev/null; then echo "box 68 negative control not caught"; exit 1; fi
echo "box 68 COMPOSE: PASS"
sha1sum -c --quiet pin/pins.sha1
python3 -I - <<'PY'
import sys, json; sys.path.insert(0, '../box64'); from flipdp import analyse
for f, T in (('pin/k1_m4_s2.json', [8, 14, 15]), ('pin/k2_m4_s1.json', [6, 11, 15]), ('pin/k2_m4_s2.json', [8, 13, 15])):
    r = analyse(json.load(open(f)), K=2); assert r['T'] == T and not r['bad'], (f, r['T'])
PY
echo "box 68 m 4 pins: PASS"
