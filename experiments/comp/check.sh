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
