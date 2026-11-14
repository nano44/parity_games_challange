#!/usr/bin/env python3
"""L-SI box 85: POOL census for Lemma POOL-ALT (docs/si/box85-twocopies.md §3). Unit: (real bit B_l = mover named B<l>, its option
SET, maximal interval I with every cycle node constant and Lambda(B_l) in {K1, K2}). Runner: box81/ref idealcyc. pool_a = e_S and the
e's at least as relevant as e_S on the plays from w on I; pool_b = the same for the plays from B's other gates; shared = |pool_a & pool_b|;
ON = #adoptions of SET on I; PRIV = no play from w or another gate passes B on I. POOL-ALT (under PRIV, disjoint pools):
2 ON - 1 <= |pool_a| + |pool_b| + 1. Usage: pool85.py BOX81DIR GENOME.json ..."""
import sys, os, json
B81 = sys.argv[1]; sys.path[:0] = [B81, os.path.join(B81, "ref", "experiments", "new", "box191"), os.path.join(B81, "ref", "experiments", "new", "box189")]
import idealcyc, gamma3
for f in sys.argv[2:]:
    G = json.load(open(f)); nm = json.load(open(f[:-5] + ".names.json")); N = G["N"]
    h, s0, movers, inv = idealcyc.build(G); E = idealcyc.Engine(h); st = idealcyc.run(G, cap=3000); _, _, _, V = gamma3.build(G, set())
    ev = {V[("e", (x, k))] for x in range(N) for k in range(len(G["opts"][x]))}; rank = lambda v: (h.prio[v], v); K12 = {V[("K", 1)], V[("K", 2)]}
    bits = sorted((int(n[1:]), i) for i, n in enumerate(nm["movers"]) if n[0] == "B" and n[1:].isdigit())
    rows = []
    for s in st:
        cur = list(s0)
        for x in range(N): cur[movers[x]] = V[("g", (x, s[x]))]
        vs, sb = E.evaluate(tuple(cur)); nxt = lambda v: cur[v] if h.owner[v] == 0 else sb[v]
        def walk(v, stop):
            seen = set(); out = set(); hit = False
            while v not in seen:
                hit |= v == stop; seen.add(v); out |= {v} if v in ev else set(); v = nxt(v)
            return out, hit
        info = {}
        for l, x in bits:
            k = nm["opts"][x].index("SET"); eS = V[("e", (x, k))]; r0 = rank(eS)
            Ew, pw = walk(h.succ[eS][0], movers[x]); A = {v for v in Ew if rank(v) >= r0} | {eS}; Bs = set(); priv = not pw
            for k2 in range(len(G["opts"][x])):
                if k2 == k: continue
                Eg, pg = walk(V[("g", (x, k2))], movers[x]); Bs |= {v for v in Eg if rank(v) >= r0}; priv &= not pg
            info[l] = (s[x] == k, A, Bs, priv)
        rows.append((tuple(vs[v][0] for v in range(h.n)), info))
    out = []; t0 = 0; worst = None
    for t in range(1, len(rows) + 1):
        if t < len(rows) and rows[t][0] == rows[t - 1][0]: continue
        seg = rows[t0:t]; t0 = t
        for l, x in bits:
            if seg[0][0][movers[x]] not in K12: continue
            pa = set().union(*(r[1][l][1] for r in seg)); pb = set().union(*(r[1][l][2] for r in seg))
            on = sum(seg[i][1][l][0] and not seg[i - 1][1][l][0] for i in range(1, len(seg))) + int(seg[0][1][l][0])
            pv = all(r[1][l][3] for r in seg); sh = len(pa & pb)
            out.append(f"B{l}:ON{on}/pa{len(pa)}/pb{len(pb)}/sh{sh}{'' if pv else '/nopriv'}")
            if pv and sh == 0 and 2 * on - 1 > len(pa) + len(pb) + 1: worst = (l, on, len(pa), len(pb))
    print(os.path.basename(f), " ".join(out), "POOL-ALT violations", 0 if worst is None else worst)
