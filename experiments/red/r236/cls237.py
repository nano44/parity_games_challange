#!/usr/bin/env python3
"""L-RED 66 R237: classify the wr237 json rows whose (T, iterations) differ from box 104's: run n5x236 and n5v (box 190, xi) on W(H, s0)
from S3, find the first differing state t, and test at every Even vertex of H whose successor differs at t whether BOTH choices are best
successors by H's own valuation at state t - 1 (tie rule) or not (divergence); also report whether t is a fallback step or the start.
Env as wr237 (BOX104, LNEW, LRED). Usage: cls237.py FILE.json I..."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.environ["BOX104"])
import n5x236 as X, wrap104 as WR, wr237, pg, n5v
D = json.load(open(sys.argv[1])); C = {}
for i in map(int, sys.argv[2:]):
    d = D["games"][i]; H = pg.Game(d["prio"], d["owner"], d["succ"]); g, std_s, std_t, mp, inv = WR.wrap(H, d["s0"])
    tr = []; fbt = []; X.run(list(g.prio), list(g.owner), [list(s) for s in g.succ], "xi", trace=tr, fbtrace=fbt)
    st, fbs, E = n5v.run(g, "xi")
    ev = [v for v in range(H.n) if H.owner[v] == 0]
    mine = [tuple(inv[a[v]] for v in ev) for a, b in tr]; theirs = [tuple(inv[s[v]] for v in ev) for s, t in st]
    t = next((k for k in range(min(len(mine), len(theirs))) if mine[k] != theirs[k]), None)
    if t is None: kind = "H-states equal (difference elsewhere)"
    elif t == 0: kind = "start"
    else:
        sH = [inv[tr[t - 1][0][v]] if H.owner[v] == 0 else None for v in range(H.n)]; V, vals = wr237.hval(H, sH)
        kinds = []
        for j, v in enumerate(ev):
            if mine[t][j] != theirs[t][j]:
                bv = max((vals[w] for w in H.succ[v]), key=lambda x: 0)
                isbest = lambda w: not any(V.better(vals[u], vals[w]) for u in H.succ[v])
                kinds.append("tie" if isbest(mine[t][j]) and isbest(theirs[t][j]) else "DIVERGENCE")
        kind = ("fallback-step " if t in fbt else "") + ",".join(sorted(set(kinds)))
    C[kind] = C.get(kind, 0) + 1; print("game", i, "first differing H-state", t, kind, flush=True)
print("TOTAL", C)
