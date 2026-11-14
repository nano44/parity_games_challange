#!/usr/bin/env python3
"""L-RED R179 SHRINK: greedy reduction keeping xich >= 1 (odxi, real N5, default start): try deleting a vertex (edges into it are
redirected to its first successor, or dropped if another edge remains), deleting edges, lowering priorities. Usage: shrink.py in.pg out.pg seed"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "..", "new", "box21"))
import odxi, pg, climb179
from n5x import load
def ok(g):
    try: return odxi.analyse(g, None, cap=400)["xich"] >= 1
    except Exception: return False
def delv(g, v):
    n = g.n; tgt = g.succ[v][0] if g.succ[v][0] != v else (g.succ[v][1] if len(g.succ[v]) > 1 else None)
    if tgt is None: return None
    mp = {u: (u if u < v else u - 1) for u in range(n) if u != v}
    su = []
    for u in range(n):
        if u == v: continue
        s = sorted(set(mp[tgt] if w == v else mp[w] for w in g.succ[u]))
        su.append(s)
    return pg.Game([g.prio[u] for u in range(n) if u != v], [g.owner[u] for u in range(n) if u != v], su)
g = load(sys.argv[1]); out = sys.argv[2]; rng = random.Random(int(sys.argv[3])); assert ok(g)
changed = True
while changed:
    changed = False
    for v in rng.sample(range(g.n), g.n):
        if v >= g.n: continue
        h = delv(g, v)
        if h is not None and ok(h): g = h; changed = True; climb179.write(g, out); print("n", g.n, flush=True)
    for v in range(g.n):
        for w in list(g.succ[v]):
            if len(g.succ[v]) > 1:
                su = [list(x) for x in g.succ]; su[v].remove(w); h = pg.Game(list(g.prio), list(g.owner), su)
                if ok(h): g = h; changed = True
    climb179.write(g, out)
print("FINAL n", g.n, "edges", sum(len(x) for x in g.succ))
