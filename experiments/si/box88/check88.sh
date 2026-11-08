#!/usr/bin/env bash
# L-SI box 88 (docs/si/box88-nest.md) self-check: leap88.py re-run on the frozen box 84-86 instances (per-bit and ALL mode), diffed with
# out/; NEST-CHARGE (chargefail), E-MON (monofail), Claim C (ascfail) and the bound (boundfail) never fail; frozen box 88 instances pinned.
set -euo pipefail
cd "$(dirname "$0")"
[ -f pins.sha1 ] && sha1sum -c --quiet --strict pins.sha1
L=$(ls ../box84/inst/HP*_mup.json ../box85/inst/*.json ../box86/inst/*.json | grep -v names)
t=$(mktemp); python3 -I -B leap88.py ../box81 $L > "$t"; diff -q "$t" out/leap88.out
ALL=1 python3 -I -B leap88.py ../box81 $L > "$t"; diff -q "$t" out/leap88_all.out; rm -f "$t"
! grep -Ev "ascfail 0 boundfail 0 chargefail 0 monofail 0 " out/leap88.out out/leap88_all.out
echo "box 88 checks: PASS"
