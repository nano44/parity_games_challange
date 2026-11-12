#!/bin/bash
# experiments/red-b self-check (L-RED-B; run by scripts/verify.sh). Fast (a few seconds): the engine against brute force on
# 200 small genomes, the counters on three frozen genomes (must be 0), both controls (must fire), and the pinned outputs.
set -u
cd "$(dirname "$0")"
export PYTHONDONTWRITEBYTECODE=1
fail=0
x=$(python3 xcheck.py 200 7 8 | tail -n 1); case "$x" in *"naive-walk value mismatches 0 mismatches 0") ;; *) echo "red-b: xcheck FAILED: $x"; fail=1;; esac
t=$(python3 lev.py --all inst/CFI3_n48.json inst/RINT_n48.json ../new/box203/inst/MWR4_2.json | tail -n 1)
z=$(echo "$t" | sed 's/^.*| //' | tr ' ' '\n' | grep -E '^[0-9]+$' | grep -cv '^0$')
[ "$z" = "0" ] || { echo "red-b: lev counters not all 0: $t"; fail=1; }
c1=$(RB_CTRL=1 python3 lev.py inst/CFI3_n48.json | tail -n 1); case "$c1" in *" l3 0 "*) echo "red-b: control 1 did not fire"; fail=1;; esac
c2=$(RB_CTRL=2 python3 lev.py inst/CFI3_n48.json | tail -n 1); case "$c2" in *" p1 0 "*) echo "red-b: control 2 did not fire"; fail=1;; esac
if [ -f out/SHA1SUMS ]; then (cd out && sha1sum -c --quiet SHA1SUMS) || { echo "red-b: out/SHA1SUMS mismatch"; fail=1; }; fi
(cd inst && echo "d55b20b8f00d0e4e08c606879c8c6ec44283e114  CFI3_n48.json
35b48913a615d4c88f0eb69afc38e42ecb0ab0b0  RINT_n48.json" | sha1sum -c --quiet) || { echo "red-b: inst sha1 mismatch"; fail=1; }
[ $fail -eq 0 ] && echo "red-b check PASS" || echo "red-b check FAILED"
exit $fail
