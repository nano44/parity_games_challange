#!/usr/bin/env bash
# M2 regression (fast): the recorded counterexample CE1 still reproduces (avh says Odd wins all, the reference says Even).
set -euo pipefail
cd "$(dirname "$0")"
python3 -I - <<'PY'
import sys; sys.path.insert(0, "../harness"); sys.path.insert(0, ".")
import pg, zielonka, avh
g = pg.read("counterexamples/ce1_4v.pg")
ref, got = zielonka.brute_force(g), avh.Solver(g).solve()[0]
assert ref == [0, 0, 0, 0] and got == [1, 1, 1, 1], (ref, got)
print("CE1 reproduces: reference", ref, "avh", got)
PY
