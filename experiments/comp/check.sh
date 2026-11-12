#!/bin/bash
# L-COMP experiments/comp self-check (fast): every stored box-27 witness replays under box27/sim.py to at least its stated length.
cd "$(dirname "$0")/box27" || exit 1
python3 -I - <<'PY' || exit 1
import json, glob, sys
sys.path.insert(0, ".")
import sim
bad = 0; n = 0
for f in sorted(glob.glob("out/*.json")):
    G = json.load(open(f)); S, why = sim.run(G); n += 1
    need = len(G["states"]) - 1 if "states" in G else int(G.get("T", 0))
    if len(S) - 1 < need: bad += 1; print("FAIL", f, len(S) - 1, "<", need)
print(f"box27 witnesses replayed: {n}, failures: {bad}")
sys.exit(1 if bad else 0)
PY

# BOX 44 (fast): the frozen outputs match out/SHA1SUMS, and the first 30 of L-SI's 300 random wrapper games replay to the frozen rows
# (my builder wrap44 + my engine n5xi44: WRAP's counters 0, T / iterations / |W| equal to the frozen JSON).
cd ../box44 || exit 1
(cd out && sha1sum -c --quiet SHA1SUMS) || { echo "box44: out/SHA1SUMS mismatch"; exit 1; }
t=$(mktemp) && rm -f "$t"
PYTHONDONTWRITEBYTECODE=1 VALB=1 python3 -I wchk44.py json inst/rand300.json "$t" 0 30 || exit 1
head -30 out/wrap44_rand300.out | cmp -s - "$t" || { echo "box44: wrapper replay differs from out/wrap44_rand300.out"; rm -f "$t"; exit 1; }
rm -f "$t"; echo "box44: SHA1SUMS ok, 30 wrapper games replayed"
