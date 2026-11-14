#!/usr/bin/env bash
# L-SI box 89 (docs/si/box89-multiply.md) self-check: frozen instances pinned; du89.py and nest88.py re-run and diffed with out/.
set -euo pipefail
cd "$(dirname "$0")"
sha1sum -c --quiet --strict pins.sha1
t=$(mktemp)
python3 -I -B du89.py ../box81 inst/DU9_h3.json inst/DU21_h4.json ../box84/inst/HP2_mup.json ../box84/inst/HP3_mup.json ../box84/inst/HP4_mup.json ../box84/inst/HP5_mup.json ../box88/inst/HP3t.json ../box88/inst/HP4t.json ../box88/inst/HP5t.json > "$t"; diff -q "$t" out/du89.out
python3 -I -B ../box88/nest88.py ../box81 inst/DU9_h3.json inst/DU21_h4.json > "$t"; diff -q "$t" out/nest89.out; rm -f "$t"
echo "box 89 checks: PASS"
