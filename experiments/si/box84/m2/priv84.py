#!/usr/bin/env python3
"""L-SI box 84 milestone 2: own check of L-RED's PRIV-FLIP quantity (R222 §3) and of what PRIV FAILURE buys. Runner: box81/ref idealcyc.
Unit: (mover B, SET-type option S = (w, Xi-target B, even beta), maximal interval I with every cycle node constant and Lambda(B) in {K1, K2}).
flips = #consecutive pairs in I where [sigma(B) = S] changes; bound = 1 + (D(w) - 1) + sum_(o != S) (D(g_o) - 1), D = distinct e-sets on I;
PRIV(I) = at no state of I does the play from w or from any g_o (o != S) pass B. excess = flips - bound.
Prints per genome: units, PRIV units, max excess over PRIV units (must be <= 0), max excess over non-PRIV units, max flips (PRIV / non-PRIV).
Usage: priv84.py BOX81DIR GENOME.json ...  |  as a module: measure(G) -> dict"""
import sys, os, json
B81 = sys.argv[1] if __name__ == "__main__" else os.environ.get("BOX81", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "box81"))
sys.path[:0] = [B81, os.path.join(B81, "ref", "experiments", "new", "box191"), os.path.join(B81, "ref", "experiments", "new", "box189")]
import idealcyc, gamma3
def measure(G, cap=3000):
    h, s0, movers, inv = idealcyc.build(G); E = idealcyc.Engine(h); st = idealcyc.run(G, cap=cap)
    _, _, _, V = gamma3.build(G, set()); N = G["N"]; ev = {V[("e", (x, k))] for x in range(N) for k in range(len(G["opts"][x]))}
    K12 = {V[("K", 1)], V[("K", 2)]}
    units = [(x, k) for x in range(N) for k, o in enumerate(G["opts"][x]) if o[1] == x and G["bp"][o[2]] == 0]
    rows = []
    for s in st:
        cur = list(s0)
        for x in range(N): cur[movers[x]] = V[("g", (x, s[x]))]
        vs, sb = E.evaluate(tuple(cur)); lam = tuple(vs[v][0] for v in range(h.n))
        nxt = lambda v: cur[v] if h.owner[v] == 0 else sb[v]
        def walk(v, stop=None):
            seen = []; es = set(); hit = False
            while v not in seen:
                if v == stop: hit = True
                seen.append(v)
                if v in ev: es.add(v)
                v = nxt(v)
            return frozenset(es), hit
        info = {}
        for (x, k) in units:
            w = h.succ[V[("e", (x, k))]][0]; Ew, pw = walk(w, movers[x]); others = []; priv = not pw
            for k2 in range(len(G["opts"][x])):
                if k2 == k: continue
                Eg, pg = walk(V[("g", (x, k2))], movers[x]); others.append(Eg); priv = priv and not pg
            info[(x, k)] = (s[x] == k, Ew, tuple(others), priv)
        rows.append((lam, info))
    res = dict(units=0, priv=0, maxex_priv=None, maxex_nopriv=None, maxfl_priv=0, maxfl_nopriv=0, T=len(st) - 1)
    t0 = 0
    for t in range(1, len(rows) + 1):
        if t < len(rows) and rows[t][0] == rows[t - 1][0]: continue
        seg = rows[t0:t]; lamB = None
        for (x, k) in units:
            if seg[0][0][movers[x]] not in K12: continue
            fl = sum(seg[i][1][(x, k)][0] != seg[i - 1][1][(x, k)][0] for i in range(1, len(seg)))
            Dw = len({r[1][(x, k)][1] for r in seg}); no = len(seg[0][1][(x, k)][2])
            Dg = [len({r[1][(x, k)][2][j] for r in seg}) for j in range(no)]
            ex = fl - (1 + (Dw - 1) + sum(d - 1 for d in Dg)); pv = all(r[1][(x, k)][3] for r in seg)
            res["units"] += 1
            if pv:
                res["priv"] += 1; res["maxex_priv"] = ex if res["maxex_priv"] is None else max(res["maxex_priv"], ex); res["maxfl_priv"] = max(res["maxfl_priv"], fl)
            else:
                res["maxex_nopriv"] = ex if res["maxex_nopriv"] is None else max(res["maxex_nopriv"], ex); res["maxfl_nopriv"] = max(res["maxfl_nopriv"], fl)
        t0 = t
    return res
if __name__ == "__main__":
    for f in sys.argv[2:]:
        r = measure(json.load(open(f))); print(os.path.basename(f), " ".join(f"{k} {v}" for k, v in r.items()))
