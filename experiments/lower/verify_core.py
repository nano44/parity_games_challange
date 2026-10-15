#!/usr/bin/env python3
"""Re-solve a successor-closed UNSAT core (sat2/cegar5two output, key subset_games, with Q_3 prepended) with other solvers.
Usage: verify_core.py core.json k solver[,solver...]"""
import sys, os, json, time
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "harness"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pysat.solvers as PS
import sat2
from quotient import build

if __name__ == "__main__":
    d = json.load(open(sys.argv[1])); k = int(sys.argv[2]); names = sys.argv[3].split(",")
    q3 = build(3, owners_set=(0, 1), verbose=True); sub = sat2.Sub(q3)
    sub.games = [tuple((tuple(g[0]), tuple(g[1]), tuple(tuple(x) for x in g[2]))) for g in d["subset_games"]]
    S, W = sub.struct(); cap = []
    class Capture:
        def __init__(self, bootstrap_with=None): cap.extend(bootstrap_with)
    orig = sat2.Cadical153; sat2.Cadical153 = Capture; sat2.encode2(S, W, list(range(S.N)), k); sat2.Cadical153 = orig
    print(f"{len(sub.games)} games + Q_3: {S.N} nodes, {len(cap)} clauses, k = {k}", flush=True)
    for nm in names:
        t0 = time.time(); s = getattr(PS, nm)(bootstrap_with=cap); r = s.solve(); s.delete()
        print(f"{nm}: {'SAT' if r else 'UNSAT'} [{time.time()-t0:.1f}s]", flush=True)
