#!/usr/bin/env python3
"""Box 5: box4.measure_ph's per-phase X and O against L-NEW's box28 xcount.phases_x (fbre.reach_o, nhprof.profile) on pinned
instances: per-phase (first, last, X, O) lists must be equal, and box4's trace_fb state sequence must equal nhprof's.
Usage: xo_validate.py game.pg [...]"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
import box4  # noqa: E402  (puts box25/box21/box22 on the path)
sys.path.insert(0, os.path.join(ROOT, "experiments/new/box28"))
import xcount  # noqa: E402
from nhprof import profile, load  # noqa: E402

ok = True
for f in sys.argv[1:]:
    g = load(f); st, _ = box4.trace_fb(g, None); rows, _ = profile(g, None)
    same_states = [tuple(s) for s, _ in st] == [r["s"] for r in rows] and [tuple(t) for _, t in st] == [r["t"] for r in rows]
    m, per = box4.measure_ph(g, st)
    ref = [(p["phase"][0], p["phase"][1], p["X"], p["O"]) for p in xcount.phases_x(g, None)]
    eq = per == ref; ok &= eq and same_states
    print(f"{os.path.basename(f)} n {g.n} iterations {len(st) - 1} states-equal {same_states} phases {len(per)} per-phase-equal {eq} "
          f"max X {m['X']} (phase length {m['Xplen']}) max O {m['O']} (phase length {m['Oplen']}) | xcount max X "
          f"{max(r[2] for r in ref)} max O {max(r[3] for r in ref)}")
print("ALL EQUAL" if ok else "MISMATCH")
sys.exit(0 if ok else 1)
