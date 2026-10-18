#!/usr/bin/env bash
# L-NEW self-check (< 1 min), run by scripts/verify.sh: N1 (anneal.py, no merging) agrees with Zielonka and passes the
# strategy check on 40 seeded random games; integer-scaled values equal the Fraction values (--xcheck) on a pinned
# instance whose N1 count is pinned (switchallexp N=3: 42 Even iterations); renum.cpp reproduces vjfast's zadeh count on
# L-SI's pinned zadehexp_N5 (271) at the identity numbering.
set -euo pipefail
cd "$(dirname "$0")"
tmp=$(mktemp -d)
python3 -I anneal_random.py "$tmp/r" 40 5 | grep -q "AGREE 40/40" && echo "N1 vs Zielonka, 40 random games: PASS"
got=$(python3 -I anneal.py instances/switchallexp_N3.pg --nocompress --xcheck --check)
echo "$got" | grep -q "even_iters=42 " && echo "$got" | grep -q "zielonka OK strategies verified" && echo "N1 pinned switchallexp N=3 (42), xcheck: PASS"
if command -v g++ >/dev/null; then
  g++ -O2 -std=c++17 -o "$tmp/renum" renum.cpp
  "$tmp/renum" zadeh ../si/instances/zadehexp_N5.pg --restarts 0 --steps 0 | grep -q "identity=271 " && echo "renum identity = vjfast zadeh (271): PASS"
else
  echo "g++ not found: renum check skipped"
fi
rm -rf "$tmp"
