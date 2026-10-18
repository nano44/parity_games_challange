#!/usr/bin/env python3
"""L-RED box 11 (produced on Opus 5.5): per phase (maximal run of searches between dominion solves, same player), the tangles
learned in it (vertex sets), and the WIDTH of that family under inclusion (largest antichain; Dilworth: |F| - maximum matching
in the strict-inclusion DAG). Reference model dtl_pyref UNMODIFIED via a subclass hook. Usage: width.py G.pg ..."""
import sys, os
A = os.path.join(os.environ["LALG_DIR"], "experiments", "alg"); sys.path.insert(0, A); sys.path.insert(0, os.path.join(A, "..", "harness"))
import pg, dtl_deficit as X_
D = X_.D
def width(F):
    F = list(F); n = len(F); adj = [[j for j in range(n) if i != j and F[i] < F[j]] for i in range(n)]; match = [-1] * n
    def aug(u, seen):
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                if match[v] == -1 or aug(match[v], seen): match[v] = u; return True
        return False
    return n - sum(1 for u in range(n) if aug(u, set()))
class L(D.DTL):
    def search(s, p):
        k = len(s.tv); dm = s.dominions; r = D.DTL.search(s, p)
        new = [frozenset(v for v, _ in s.tv[t]) for t in range(k, len(s.tv))]
        if not s.ph or s.ph[-1]["p"] != p or s.ph[-1]["closed"]: s.ph.append({"p": p, "T": [], "S": 0, "closed": False})
        s.ph[-1]["T"] += new; s.ph[-1]["S"] += 1
        if s.dominions != dm: s.ph[-1]["closed"] = True
        return r
for f in sys.argv[1:]:
    g = pg.read(f); d0 = X_.build(g); d = L(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.ph = []
    sys.setrecursionlimit(100000); d.run()
    print(os.path.basename(f), f"n {g.n}", " | ".join(f"p{x['p']} S {x['S']} tangles {len(x['T'])} width {width(set(x['T']))}" for x in d.ph if x["S"] > 1))
