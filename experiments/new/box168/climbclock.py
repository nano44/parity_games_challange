#!/usr/bin/env python3
"""climb an IDEAL genome (box165 seedpm mutations: ranks, parities, gates, start, W-targets, Xi-targets in a topological order) to
maximize the best pair excess flips(p, q) - |W(r)| (r a reader of (p, q)), tie-break flips. Usage: climbclock.py seed.json iters seed"""
import os, sys, json, random, itertools
H = os.path.dirname(os.path.abspath(__file__))
_H = H; H = os.path.join(_H, "..", "box165")
exec(open(os.path.join(H, "seedpm.py")).read().split("\nif __name__")[0].replace('H = os.path.dirname(os.path.abspath(__file__)); ', ''))
H = _H
def wclos(G):
    N = G["N"]; adj = [set(o[0] for o in G["opts"][x] if o[0] >= 0) for x in range(N)]; R = []
    for x in range(N):
        seen, st = set(), list(adj[x])
        while st:
            y = st.pop()
            if y not in seen: seen.add(y); st.extend(adj[y])
        R.append(seen)
    return R
def sc(G):
    try: g = Gen(G); S, _ = g.run(G["start"])
    except RuntimeError: return (-99, 0, None)
    W = wclos(G); keys = [g.keys(s) for s in S]; best = (-99, 0, None)
    for L in set(G["lev"]):
        ms = [v for v in range(G["N"]) if G["lev"][v] == L]
        for p, q in itertools.combinations(ms, 2):
            o = [k[p] < k[q] for k in keys]; fl = sum(a != b for a, b in zip(o, o[1:])); w = len({p, q} | W[p] | W[q])
            if (fl - w, fl) > best[:2]: best = (fl - w, fl, (p, q, w, len(S) - 1))
    return best
f, iters, seed = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]); rng = random.Random(seed); G = json.load(open(f)); G["xorder"] = topo(G)
s = sc(G); best = s; print("seed", os.path.basename(f), s, flush=True)
for it in range(iters):
    G2 = mutate(G, rng); s2 = sc(G2)
    if s2[:2] >= s[:2]:
        G, s = G2, s2
        if s[:2] > best[:2]:
            best = s; print("it", it, s, flush=True); json.dump(G, open(os.path.join(H, "out", "clock_%s_s%d.json" % (os.path.basename(f)[:-5], seed)), "w"))
print("FINAL", best)
