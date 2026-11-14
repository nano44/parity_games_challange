#!/usr/bin/env bash
# L-SI box 88 (docs/si/box88-nest.md) self-check: leap88.py re-run on the frozen box 84-86 instances (per-bit and ALL mode), diffed with
# out/; NEST-CHARGE (chargefail), E-MON (monofail), Claim C (ascfail) and the bound (boundfail) never fail; frozen box 88 instances pinned.
set -euo pipefail
cd "$(dirname "$0")"
sha1sum -c --quiet --strict pins.sha1; bash inst/mkHPb.sh
L=$(ls ../box84/inst/HP*_mup.json ../box85/inst/*.json ../box86/inst/*.json | grep -v names)
t=$(mktemp); python3 -I -B leap88.py ../box81 $L > "$t"; diff -q "$t" out/leap88.out
ALL=1 python3 -I -B leap88.py ../box81 $L > "$t"; diff -q "$t" out/leap88_all.out
F="inst/HP3t.json inst/HP4t.json inst/HP5t.json"
{ python3 -I -B leap88.py ../box81 $F; ALL=1 python3 -I -B leap88.py ../box81 inst/NK6_cl21.json inst/ND4_hp3.json; } > "$t"; diff -q "$t" out/leap88_fast.out
python3 -I -B nest88.py ../box81 ../box84/inst/HP2_mup.json ../box84/inst/HP3_mup.json ../box84/inst/HP4_mup.json ../box84/inst/HP5_mup.json $F inst/NK6_cl21.json inst/ND4_hp3.json > "$t"; diff -q "$t" out/nest88.out; rm -f "$t"
# out/leap88_slow.out (HP6b-HP8b, ~10-30 min each) is recorded, not re-run here; its instances are pinned and rebuilt by inst/mkHPb.sh.
! grep -Ev "ascfail 0 boundfail 0 chargefail 0 monofail 0 " out/leap88.out out/leap88_all.out out/leap88_fast.out out/leap88_slow.out
echo "box 88 checks: PASS"
