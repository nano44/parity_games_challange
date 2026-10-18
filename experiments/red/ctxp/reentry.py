#!/usr/bin/env python3
"""L-RED box 13 (produced on Opus 5.5): RE-ENTRIES. For each phase and vertex v, a re-entry is a transition where v's rank CLASS
(stable / -1 / 0) changes to a class v held earlier in the phase. For each re-entry: is v's new K-v-all key (rank, j, |R_j|, |V_j|)
an exact earlier key ("return"), else which components differ from the nearest earlier key of the same class. Uses
b12_pot.run / chain / keys / sig UNMODIFIED. Usage: DTL_ORDER=... reentry.py G.pg ..."""
import sys, os
from collections import Counter
A = os.path.join(os.environ["LALG_DIR"], "experiments", "alg"); sys.path.insert(0, A); sys.path.insert(0, os.path.join(A, "..", "harness"))
import pg, b12_pot as B
sys.setrecursionlimit(100000); order = os.environ.get("DTL_ORDER", "stable")
cls = lambda r, n: "S" if r == n + 2 else ("0" if r == 0 else "-1")
for f in sys.argv[1:]:
    g = pg.read(f); d = B.run(g, order); C = Counter(); prevph = None; hist = {}; last = {}
    for ph, calls in getattr(d, "log", []):
        ch = B.chain(calls, g.n); cur = {x[0]: x[1:] for x in B.keys(ch)["K-v-all"]}
        if ph != prevph: hist = {}; last = {}
        else:
            for v, key in cur.items():
                c = cls(key[0], g.n)
                if v in last and cls(last[v][0], g.n) != c and any(cls(k[0], g.n) == c for k in hist.get(v, ())):
                    same = [k for k in hist[v] if cls(k[0], g.n) == c]
                    if key in same: C["return"] += 1
                    else:
                        best = min(same, key=lambda k: sum(a != b for a, b in zip(k, key)))
                        C["differs in " + "".join(nm for nm, a, b in zip("rjRV", best, key) if a != b)] += 1
        for v, key in cur.items(): hist.setdefault(v, set()).add(key); last[v] = key
        prevph = ph
    print(os.path.basename(f), order, dict(C) or "no re-entries")
