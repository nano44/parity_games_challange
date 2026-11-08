#!/usr/bin/env bash
# L-SI box 87 LEAPFROG-ASC (docs/si/box87-leapfrog.md) self-check: leap87.py re-run on the frozen box 84-86 instances, diffed with
# out/leap87.out; Claim C (ascfail) and the bound (boundfail) never fail.
set -euo pipefail
cd "$(dirname "$0")"
sha1sum -c --quiet --strict pins.sha1
L=$(ls ../box84/inst/HP*_mup.json ../box85/inst/*.json ../box86/inst/*.json | grep -v names)
t=$(mktemp); python3 -I -B leap87.py ../box81 $L > "$t"; diff -q "$t" out/leap87.out; rm -f "$t"
! grep -Ev "ascfail 0 boundfail 0$" out/leap87.out
echo "box 87 checks: PASS"
