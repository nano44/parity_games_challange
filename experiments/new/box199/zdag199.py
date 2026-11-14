#!/usr/bin/env python3
"""Box 199 Addendum 2 (L-NEW successor 66).
Ascent DAG Z: z in Z(y) iff z more relevant than y and z in E_t(wt(y)) for some state t (Lambda of wt(y) arbitrary). Records depth (letters),
max fan-out, and the path count P_Z(y) = 1 + sum P_Z(z)."""
import sys, os, json, functools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import split199 as S
for fn in sys.argv[1:]:
    G = json.load(open(fn)); G = G.get("genome", G)
    g0, _, _, V = S.gamma3.build(G, S.eg195.PADS); g = S.eg195.topg(g0); n = g.n; name = {v: k for k, v in V.items()}
    E, Ed = S.n5v.Engine(g), S.n5v.Engine(S.n5v.dual(g)); sigma, tau = S.n5x.start_pair(g, E, Ed, None)
    evs = [v for v in range(n) if isinstance(name[v], tuple) and name[v][0] == "e"]
    Z = {y: set() for y in evs}
    while True:
        vs, _ = E.evaluate(tuple(sigma))
        for y in evs:
            m = g.succ[y][0]; msk = vs[m][1]
            for z in evs:
                if msk & E.bit[z] and E.rank[z] > E.rank[y]: Z[y].add(z)
        r = S.n5v.step(g, E, Ed, sigma, tau, "xi")
        if r is None or r[4]: break
        sigma, tau = r[0], r[1]
    @functools.lru_cache(None)
    def dep(y): return 1 + max((dep(z) for z in Z[y]), default=0)
    @functools.lru_cache(None)
    def P(y): return 1 + sum(P(z) for z in Z[y])
    print(os.path.basename(fn), "Zdepth", max(dep(y) for y in evs), "Zfan", max(len(Z[y]) for y in evs), "maxPZ", max(P(y) for y in evs), "letters", len(evs), flush=True)
