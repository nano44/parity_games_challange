#!/usr/bin/env bash
# L-SI box 68 self-check (~20 s): Lemma COMPOSE on 30 random (K, G) pairs (KPART 0, GPART 0); negative control (schedule negated) fails.
set -euo pipefail
cd "$(dirname "$0")"
python3 -I compose.py 30 7 | grep -q "KPART 0 GPART 0"
if NEG=1 python3 -I compose.py 10 8 >/dev/null; then echo "box 68 negative control not caught"; exit 1; fi
echo "box 68 COMPOSE: PASS"
