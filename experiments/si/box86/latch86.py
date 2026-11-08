#!/usr/bin/env python3
"""L-SI box 86: census for Lemma ACCESS-LATCH (docs/si/box86-lagtower.md §2). Unit: a step t -> t+1 (cycle nodes constant) at which a
real bit B_l (mover B<l>) goes OFF its SET. Records w_l's option label at t (w_l = mover w<l>, SET's W-target) and whether
E_t(w_l) >=lex E_t(g_o) for every other option o of B_l with the same cycle node and PRIV at t; ACCESS-LATCH predicts that this never
holds at an OFF step. Prints per genome: OFF events, OFF events with w_l on 'real', latch-violations (must be 0).
Usage: latch86.py BOX81DIR GENOME.json ..."""
import sys, os, json
B81 = sys.argv[1]; sys.path[:0] = [B81, os.path.join(B81, "ref", "experiments", "new", "box191"), os.path.join(B81, "ref", "experiments", "new", "box189")]
import idealcyc, gamma3
for f in sys.argv[2:]:
    G = json.load(open(f)); nm = json.load(open(f[:-5] + ".names.json")); N = G["N"]
    h, s0, movers, inv = idealcyc.build(G); E = idealcyc.Engine(h); st = idealcyc.run(G, cap=3000); _, _, _, V = gamma3.build(G, set())
    ev = {V[("e", (x, k))] for x in range(N) for k in range(len(G["opts"][x]))}; rank = lambda v: (h.prio[v], v)
    ix = {n: i for i, n in enumerate(nm["movers"])}
    bits = sorted((int(n[1:]), i) for i, n in enumerate(nm["movers"]) if n[0] == "B" and n[1:].isdigit())
    offs = onreal = viol = 0; prev = None
    for t in range(len(st)):
        cur = list(s0)
        for x in range(N): cur[movers[x]] = V[("g", (x, st[t][x]))]
        vs, sb = E.evaluate(tuple(cur)); lam = tuple(vs[v][0] for v in range(h.n))
        if prev is not None and prev[0] == lam:
            plam, ps, pcur, psb, pvs = prev; nxt = lambda v: pcur[v] if h.owner[v] == 0 else psb[v]
            def walk(v, stop):
                seen = set(); out = []; hit = False
                while v not in seen:
                    hit |= v == stop; seen.add(v); out += [v] if v in ev else []; v = nxt(v)
                return sorted((rank(u) for u in out), reverse=True), hit
            for l, x in bits:
                k = nm["opts"][x].index("SET")
                if not (ps[x] == k and st[t][x] != k): continue
                offs += 1; w = ix.get(f"w{l}")
                if w is not None and nm["opts"][w][ps[w]] == "real": onreal += 1
                eS = V[("e", (x, k))]; Ew, pw = walk(h.succ[eS][0], movers[x]); latch = not pw
                for k2 in range(len(G["opts"][x])):
                    if k2 == k: continue
                    g = V[("g", (x, k2))]; Eg, pg = walk(g, movers[x]); latch &= not pg
                    if pvs[g][0] == plam[movers[x]] and Eg > Ew: latch = False
                viol += latch
        prev = (lam, st[t], cur, sb, vs)
    print(os.path.basename(f), "OFF", offs, "OFF with w on real", onreal, "latch-violations", viol)
