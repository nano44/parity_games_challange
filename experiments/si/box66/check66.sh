#!/usr/bin/env bash
# L-SI box 66 self-check (~5 s): bff.c (box 65 bfg.c + FRONTIER hook) reproduces the m = 1 pair set; the committed m = 2 enumeration
# (4 parts) gives exactly {(pre, post): post <= 4, pre + post <= 5} and T_1(2) = 5.
set -euo pipefail
cd "$(dirname "$0")"
want1="0 0;0 1;0 2;1 0;1 1;1 2;2 0;"
if command -v gcc >/dev/null; then
  gcc -O2 -DKMAX=1 -o bff_check bff.c
  got1=$(./bff_check 1 0 1 2>/dev/null | awk '/^PAIR/{print $3" "$5}' | sort -u -n -k1 -k2 | tr '\n' ';'); rm -f bff_check
  [ "$got1" = "$want1" ] || { echo "box 66 m 1 pairs: $got1"; exit 1; }
fi
got2=$(awk '/^PAIR/{print $3" "$5}' out/bff_m2_p0.txt out/bff_m2_p1.txt out/bff_m2_p2.txt out/bff_m2_p3.txt | sort -u -n -k1 -k2 | tr '\n' ';')
want2=$(for a in 0 1 2 3 4; do for c in 0 1 2 3 4; do [ $c -le 4 ] && [ $((a + c)) -le 5 ] && printf '%d %d;' $a $c; done; done)
[ "$got2" = "$want2" ] || { echo "box 66 m 2 pairs: $got2"; exit 1; }
[ "$(grep -h '^T_1(2)' out/bff_m2_p*.txt | sort -u)" = "T_1(2) 5" ]
echo "box 66 frontier: PASS"
