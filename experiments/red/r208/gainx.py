#!/usr/bin/env python3
"""L-RED R209 GAINX: exact gain' of R208 for ANY genome file (any mover indexing): top level U = movers of the max level; couplings =
options of non-top movers with Xi-target in U; G^-_r = G without U, coupled targets re-routed by r (X or any non-top mover, acyclic),
same start (restricted); gain' = T(G) - max_r T(G^-_r), exhaustive over all r (C <= 3). Also max_r over ALL starts of G^-_r
(T*-style, "allstart") when the lower part has <= 14 two-option movers. Usage: gainx.py file.json ..."""
import sys, os, json, itertools
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r187"), os.path.join(H, "..", "r178")]
import ideal
from coupext import acyc
def T(G): return len(ideal.traj(G, cap=100000)[0]) - 1
for f in sys.argv[1:]:
    G = json.load(open(f)); top = max(G["lev"]); U = {v for v in range(G["N"]) if G["lev"][v] == top}
    keep = [v for v in range(G["N"]) if v not in U]; mp = {v: i for i, v in enumerate(keep)}
    cs = [(i, k) for i, v in enumerate(keep) for k in range(len(G["opts"][v])) if G["opts"][v][k][1] in U]
    base = dict(N=len(keep), lev=[G["lev"][v] for v in keep], gate=[G["gate"][v] for v in keep], br=G["br"], bp=G["bp"],
                start=[G["start"][v] for v in keep],
                opts=[[[mp.get(o[0], -1) if o[0] >= 0 else -1, mp[o[1]] if o[1] in mp else -1, o[2]] for o in G["opts"][v]] for v in keep])
    t = T(G); best = (-1, None); bestall = -1
    two = [v for v in range(base["N"]) if len(base["opts"][v]) == 2]
    for r in itertools.product(list(range(base["N"])) + [-1], repeat=len(cs)):
        Hh = json.loads(json.dumps(base))
        for (i, k), y in zip(cs, r): Hh["opts"][i][k][1] = y
        if not acyc(Hh["opts"]): continue
        v = T(Hh)
        if v > best[0]: best = (v, r)
        if len(two) <= 14:
            for bits in itertools.product((0, 1), repeat=len(two)):
                s = [0] * Hh["N"]
                for w, b in zip(two, bits): s[w] = b
                Hh["start"] = s; bestall = max(bestall, T(Hh))
    print(f"{os.path.basename(f)}: d {top + 1} N {G['N']} |U| {len(U)} C {len(cs)} T {t} | best re-routing (same start) {best[0]} "
          f"via {best[1]} -> gain' {t - best[0]} | best re-routing over all starts {bestall} -> {t - bestall if bestall >= 0 else '-'}")
