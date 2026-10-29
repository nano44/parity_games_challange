#!/usr/bin/env python3
"""L-NEW box 56 probe: per (lambda-interval, sigma-bar value s), total F-steps from states with sigma-bar = s (GSTEP) and how many change Xi
(GVC), summed over all stretches of s in the interval. Tests the 'distinct best replies' route (GVC <= n - 1 per group?). Usage: grp.py GAME [START] | --list FILE"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box54")); sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
import n5sf
from collections import Counter
from n5x import load, readstart
def run(g, st, name):
    E, T = n5sf.trace(g, st); T = [x for x in T if "lam" in x]; n = g.n
    seq = []
    for x in T:
        s = [x["s"][v] if g.owner[v] == 0 else -1 for v in range(n)]
        if not seq or seq[-1] != s: seq.append(s)
    VS = [E.evaluate(tuple(s)) for s in seq]
    key = lambda j: (tuple(x[0] for x in VS[j][0]), tuple(VS[j][1][v] if g.owner[v] == 1 else -1 for v in range(n)))
    gs, gv, gstr = Counter(), Counter(), Counter()
    for j in range(len(seq) - 1):
        k = key(j); gs[k] += 1; gv[k] += list(VS[j][0]) != list(VS[j + 1][0])
        if j == 0 or key(j - 1) != k: gstr[k] += 1
    m = sum(len(set(s)) for s in g.succ)
    kv = max(gv, key=lambda k: gv[k], default=None)
    print("ROW", name, "n", n, "m", m, "values", len(seq), "groups", len(gs), "GVCmax", gv[kv] if kv else 0, "stretches_of_it", gstr[kv] if kv else 0,
          "GSTEPmax", max(gs.values(), default=0), "GVC>n-1", sum(1 for k in gv if gv[k] > n - 1), "GSTEP>=n+m", sum(1 for k in gs if gs[k] >= n + m), flush=True)
if __name__ == "__main__":
    a = sys.argv[1:]
    L = [l.split() for l in open(a[1]) if l.strip() and not l.startswith("#")] if a[0] == "--list" else [a]
    for p in L:
        X = lambda q: q if os.path.exists(q) else (os.path.join(ROOT, q) if os.path.exists(os.path.join(ROOT, q)) else os.path.join(ROOT, "experiments", q))
        try: run(load(X(p[0])), readstart(X(p[1])) if len(p) > 1 else None, p[0])
        except Exception as e: print("SKIP", p[0], repr(e)[:60])
