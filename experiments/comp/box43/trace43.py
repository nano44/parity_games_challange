#!/usr/bin/env python3
"""L-COMP box 43 item 2: per-gate trace of the DEEP internal flips (box41/deep41.py's DeepInt: flips of INTERNAL gates at steps t >= t0(C)
charged by TWO-CROSS to a change of depth > CMAX; L-SI box 100 §2-§4) on MY Γ3 engine (box34/own34.py, N5'-xi from S3, states 0..T3).
For every gate with at least one such flip: mover x, option k, level, W-target, Ξ-target, the in-edges of x (options with W- or
Ξ-target x), and each deep flip as (t, depth, face left, z) with z = the most relevant vertex of the charged change Π_t Δ Π_(t+1) of
the face Odd leaves (named by my vertex key). Summary: deep flips per step, per mover, per z.
Usage: trace43.py G.json   (env CMAX, default 3)"""
import sys, os, json, collections
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "box41"), os.path.join(H, "..", "box34"), os.path.join(H, "..", "box40")]
import own34, scc40, deep41
from own34 import SpecSI
CMAX = deep41.CMAX


def trace(G):
    r = own34.run(G); g, V, vals, sigs, T = r["g"], r["V"], r["vals"], r["sigs"], r["T3"]
    SG = SpecSI(g); sbar = [SG.evaluate_choice(list(s))[1] for s in sigs]; rk = {v: (g.prio[v], v) for v in range(g.n)}
    name = {v: k for k, v in V.items()}
    adj = scc40.dgraph(G); comp, comps = scc40.sccs(adj); K = len(comps); f = [0] * K
    for t in range(1, T + 1):
        for x in range(G["N"]):
            if sigs[t - 1][V[("x", x)]] != sigs[t][V[("x", x)]]: f[comp[x]] = t
    succ = [set() for _ in range(K)]
    for x in range(G["N"]):
        for y in adj[x]:
            if comp[y] != comp[x]: succ[comp[x]].add(comp[y])
    reach = {}
    def R(c):
        if c not in reach:
            s = set()
            for d in succ[c]: s.add(d); s |= R(d)
            reach[c] = s
        return reach[c]
    t0 = [max((f[d] for d in R(c)), default=0) for c in range(K)]
    rows = []; bystep = collections.Counter(); byz = collections.Counter(); bymover = collections.Counter()
    for x in range(G["N"]):
        for k, (wt, xt, _) in enumerate(G["opts"][x]):
            q = (x, k); gv = V[("g", q)]
            if not (wt >= 0 and xt >= 0 and comp[wt] == comp[x] and comp[xt] == comp[x]): continue
            fl = []
            for t in range(T):
                if sbar[t][gv] == sbar[t + 1][gv] or t < t0[comp[x]]: continue
                a = sbar[t][gv]; va, vb = vals[t][a], vals[t + 1][a]
                if va == vb: continue
                d = deep41.depth(va, vb, rk)
                if d > CMAX:
                    D = va[1] ^ vb[1]; z = max(D, key=lambda u: rk[u]) if D else None
                    fl.append((t, d, name[a][0], name.get(z)))
                    bystep[t] += 1; byz[str(name.get(z))] += 1; bymover[x] += 1
            if fl: rows.append((x, k, G["lev"][x], wt, xt, fl))
    ins = lambda x: [(y, j, "W" if o[0] == x else "", "X" if o[1] == x else "") for y in range(G["N"]) for j, o in enumerate(G["opts"][y]) if x in (o[0], o[1])]
    return dict(T3=T, rows=rows, bystep=bystep, byz=byz, bymover=bymover, ins=ins, comp=comp, comps=comps, t0=t0)


if __name__ == "__main__":
    G = json.load(open(sys.argv[1])); G = G.get("genome", G); r = trace(G)
    print(os.path.basename(sys.argv[1]), "N", G["N"], "M", sum(map(len, G["opts"])), "T3", r["T3"], "deep internal flips", sum(len(x[5]) for x in r["rows"]), "gates", len(r["rows"]),
          "SCC sizes", sorted((len(c) for c in r["comps"]), reverse=True)[:4])
    for x, k, lv, wt, xt, fl in r["rows"]:
        print("gate (%d, %d) lev %d deg %d wt %d xt %d | in-edges of %d: %s | deep flips %s" % (x, k, lv, len(G["opts"][x]), wt, xt, x, r["ins"](x), fl))
    print("deep flips per step:", sorted(r["bystep"].items())); print("per mover:", sorted(r["bymover"].items()))
    print("per z:", sorted(r["byz"].items(), key=lambda kv: -kv[1]))
