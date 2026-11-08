#!/usr/bin/env bash
# L-SI box 80 (docs/si/N5-TOWER-box80.md) self-check (~30 s): pins --strict; check80.py reproduces check80.out (PULSE-NEST, ZONE,
# INSERT-PASS counters 0, controls > 0, slack table); delay80.py reproduces delay80.out.
set -euo pipefail
cd "$(dirname "$0")"
sha1sum -c --quiet --strict pins.sha1
t=$(mktemp -d)
python3 -I -B check80.py > "$t/c"
diff -q "$t/c" check80.out
for f in H5_d20_F62:3 H5_d20_F62:4 H6_d24_F126:3 H6_d24_F126:4; do
  g=${f%%:*}; j=${f##*:}
  echo "== $g j $j" >> "$t/d"
  python3 -I -B delay80.py ../box79/inst/$g.json $j >> "$t/d"
done
diff -q "$t/d" delay80.out
rm -rf "$t"
grep -q "^CORPUS XS 0 PN 0 " check80.out
grep -q "^EXTRA XS 0 PN 0 " check80.out
grep -q "^ZONE 0 " check80.out
grep -q "^INSERT 0 INSERT_F 0 " check80.out
echo "box 80 checks: PASS"
