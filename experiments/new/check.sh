#!/usr/bin/env bash
# L-NEW self-check (< 1 min), run by scripts/verify.sh: N1 (anneal.py, no merging) agrees with Zielonka and passes the
# strategy check on 40 seeded random games; integer-scaled values equal the Fraction values (--xcheck) on a pinned
# instance whose N1 count is pinned (switchallexp N=3: 42 Even iterations); renum.cpp reproduces vjfast's zadeh count on
# L-SI's pinned zadehexp_N5 (271) at the identity numbering; the C++ port anneal.cpp equals anneal.py on 30 random games.
set -euo pipefail
cd "$(dirname "$0")"
tmp=$(mktemp -d)
python3 -I anneal_random.py "$tmp/r" 40 5 | grep -q "AGREE 40/40" && echo "N1 vs Zielonka, 40 random games: PASS"
got=$(python3 -I anneal.py instances/switchallexp_N3.pg --nocompress --xcheck --check)
echo "$got" | grep -q "even_iters=42 " && echo "$got" | grep -q "zielonka OK strategies verified" && echo "N1 pinned switchallexp N=3 (42), xcheck: PASS"
if command -v g++ >/dev/null; then
  g++ -O2 -std=c++17 -o "$tmp/renum" renum.cpp
  g++ -O2 -std=c++17 -o anneal_c_check anneal.cpp
  ANNEAL_C=./anneal_c_check python3 -I xcheck_c.py "$tmp/xc" 30 9 | grep -q "XCHECK-C PASS 30/30" && echo "anneal_c vs anneal.py (30 games): PASS"
  rm -f anneal_c_check
  "$tmp/renum" zadeh ../si/instances/zadehexp_N5.pg --restarts 0 --steps 0 | grep -q "identity=271 " && echo "renum identity = vjfast zadeh (271): PASS"
else
  echo "g++ not found: renum check skipped"
fi
rm -rf "$tmp"
