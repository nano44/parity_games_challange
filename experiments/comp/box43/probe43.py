#!/usr/bin/env python3
"""L-COMP box 43 item 2 (exploration): for chosen gates of a genome, every flip (deep or not) on MY Γ3 engine (own34): step t, face left,
charged depth, and the most relevant elements of Π_t / Π_(t+1) of that face; plus the option sequence of chosen movers.
Usage: probe43.py G.json TOPK gate:x,k ... mover:x ..."""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "box41"), os.path.join(H, "..", "box34"), os.path.join(H, "..", "box40")]
import own34, deep41
from own34 import SpecSI
G = json.load(open(sys.argv[1])); G = G.get("genome", G); K = int(sys.argv[2])
r = own34.run(G); g, V, vals, sigs, T = r["g"], r["V"], r["vals"], r["sigs"], r["T3"]
SG = SpecSI(g); sbar = [SG.evaluate_choice(list(s))[1] for s in sigs]; rk = {v: (g.prio[v], v) for v in range(g.n)}
name = {v: k for k, v in V.items()}
def nm(v):
    k = name[v]
    if isinstance(k, tuple) and isinstance(k[1], tuple): return "%s%d.%d" % (k[0], k[1][0], k[1][1])
    if isinstance(k, tuple): return "%s%s" % (k[0], k[1])
    return str(k)
def tops(val): return " ".join(nm(u) for u in sorted(val[1], key=lambda u: rk[u], reverse=True)[:K])
print("T3", T)
for a in sys.argv[3:]:
    kind, s = a.split(":")
    if kind == "mover":
        x = int(s); seq = [name[sigs[t][V[("x", x)]]][1][1] for t in range(T + 1)]
        print("mover %d lev %d options %s | option per state: %s" % (x, G["lev"][x], [(o[0], o[1]) for o in G["opts"][x]], "".join("%x" % o if o < 16 else "(%d)" % o for o in seq)))
    else:
        x, k = map(int, s.split(",")); q = (x, k); gv = V[("g", q)]
        print("gate (%d, %d) wt %d xt %d: faces per state: %s" % (x, k, G["opts"][x][k][0], G["opts"][x][k][1], "".join("e" if name[sbar[t][gv]][0] == "pe" else "b" for t in range(T + 1))))
        for t in range(T):
            if sbar[t][gv] == sbar[t + 1][gv]: continue
            a_ = sbar[t][gv]; va, vb = vals[t][a_], vals[t + 1][a_]
            d = deep41.depth(va, vb, rk) if va != vb else None
            print("   t %2d leaves %s depth %s | Λ %s -> %s | Π_t: %s | Π_t+1: %s" % (t, name[a_][0], d, nm(va[0]), nm(vb[0]), tops(va), tops(vb)))
