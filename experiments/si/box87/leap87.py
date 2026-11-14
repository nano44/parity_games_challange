#!/usr/bin/env python3
"""L-SI box 87: census for Lemma LEAPFROG-ASC (docs/si/box87-leapfrog.md). Unit: (real bit B_l, its SET option S, maximal interval I with
every cycle node constant and Lambda(B_l) in {K1, K2}). Events = steps t -> t+1 in I where [sigma(B_l) = S] changes. At state t:
a_t = pi({e_S} u E_t(w)), b_t = max_lex over the other gates g_o with B's cycle node of pi(E_t(g_o)) (pi = e's at least as relevant
as e_S); z_t = max(a_t sym-diff b_t); TYPE i if no e of a_t & b_t is more relevant than z_t, else TYPE ii. For type ii the play
holding z_t (from w, or from the maximising g_o) must visit z_t before a more relevant e (an ASCENT): checked (ascfail must be 0).
Bound checked per unit: #events <= |E_U| + 2 k + 1, |E_U| = #e-vertices at least as relevant as e_S, k = #type-ii events.
Usage: leap87.py BOX81DIR GENOME.json ..."""
import sys, os, json
B81 = sys.argv[1]; sys.path[:0] = [B81, os.path.join(B81, "ref", "experiments", "new", "box191"), os.path.join(B81, "ref", "experiments", "new", "box189")]
import idealcyc, gamma3
K = lambda X, rank: sorted((rank(v) for v in X), reverse=True)
for f in sys.argv[2:]:
    G = json.load(open(f)); nm = json.load(open(f[:-5] + ".names.json")); N = G["N"]
    h, s0, movers, inv = idealcyc.build(G); E = idealcyc.Engine(h); st = idealcyc.run(G, cap=3000); _, _, _, V = gamma3.build(G, set())
    ev = {V[("e", (x, k))] for x in range(N) for k in range(len(G["opts"][x]))}; rank = lambda v: (h.prio[v], v)
    K12 = {V[("K", 1)], V[("K", 2)]}
    bits = sorted((int(n[1:]), i) for i, n in enumerate(nm["movers"]) if n[0] == "B" and n[1:].isdigit())
    S = {x: nm["opts"][x].index("SET") for _, x in bits}
    rows = []
    for s in st:
        cur = list(s0)
        for x in range(N): cur[movers[x]] = V[("g", (x, s[x]))]
        vs, sb = E.evaluate(tuple(cur)); rows.append((s, cur, sb, tuple(vs[v][0] for v in range(h.n))))
    t1 = t2 = asc_fail = bound_fail = units = 0; maxk = 0
    t0 = 0
    for t in range(1, len(rows) + 1):
        if t < len(rows) and rows[t][3] == rows[t - 1][3]: continue
        seg = range(t0, t); t0s = t0; t0 = t
        for l, x in bits:
            lam = rows[t0s][3][movers[x]]
            if lam not in K12: continue
            eS = V[("e", (x, S[x]))]; r0 = rank(eS); EU = sum(1 for v in ev if rank(v) >= r0)
            nev = k = 0
            for u in seg:
                if u + 1 >= t: break
                s, cur, sb, lm = rows[u]
                if (s[x] == S[x]) == (rows[u + 1][0][x] == S[x]): continue
                nxt = lambda v: cur[v] if h.owner[v] == 0 else sb[v]
                def seq(v):
                    seen = set(); out = []
                    while v not in seen: seen.add(v); out += [v] if v in ev else []; v = nxt(v)
                    return out
                sw = [eS] + seq(h.succ[eS][0]); A = {v for v in sw if rank(v) >= r0}
                best = None
                for k2 in range(len(G["opts"][x])):
                    if k2 == S[x]: continue
                    g = V[("g", (x, k2))]
                    if lm[g] != lam: continue
                    sg = seq(g); Bs = {v for v in sg if rank(v) >= r0}
                    if best is None or K(Bs, rank) > K(best[1], rank): best = (sg, Bs)
                if best is None: continue
                nev += 1; sg, Bs = best; d = A ^ Bs; z = max(d, key=rank)
                if any(rank(v) > rank(z) for v in A & Bs):
                    k += 1; t2 += 1; pl = sw if z in A else sg; i = pl.index(z)
                    asc_fail += not any(rank(v) > rank(z) for v in pl[i + 1:])
                else: t1 += 1
            if nev:
                units += 1; maxk = max(maxk, k); bound_fail += nev > EU + 2 * k + 1
    print(os.path.basename(f), "units", units, "typeI", t1, "typeII", t2, "maxk", maxk, "ascfail", asc_fail, "boundfail", bound_fail)
