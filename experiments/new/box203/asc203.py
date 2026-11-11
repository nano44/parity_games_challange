#!/usr/bin/env python3
"""Box 203 part 2 (L-NEW successor 68): ascents of e-sequences on IDEAL-CYC, by Xi-feedback number k.
seq_t(v) := the e-vertices of Pi_t(v) in play order (RESULTS R121); an ascent := a step of seq_t(v) to a MORE relevant e-vertex.
Per genome: k (box202 fvs202.kfvs), U(G), maxasc := max over states t and vertices v of #ascents of seq_t(v), and the same restricted to
gate faces (e_g, beta_g); also maxasc_f := max ascents counted only between consecutive e's whose connecting play segment passes the
single feedback vertices (k = 1 only; F := every mover whose removal leaves the Xi-graph acyclic; 0 for k != 1) — box 203 §5's CONJECTURE K1-ASC asks maxasc <= 2 at k = 1.
Usage: asc203.py G.json ...  | asc203.py --rand MODE SEED COUNT (MODE: k1, k2 = box202 k1srch202.mk with K1_MODE; rand = rand191.rgen)."""
import sys, os, json, random, collections
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import gfc203
sys.path.insert(0, os.path.join(gfc203.ROOT, "experiments/new/box191"))
import idealcyc, fvs202

def asc(G):
    H, n, E, V, gates = gfc203.hist_ideal(G)
    h, s0, movers, inv = idealcyc.build(G); st = idealcyc.run(G, cap=20000); gi = {}
    for x in range(G["N"]):
        for v in h.succ[movers[x]]: gi[(x, inv[v])] = v
    isE = {V[k] for k in V if isinstance(k, tuple) and k[0] == "e"}
    faces = {v for (q, a, b) in gates.values() for v in (a, b)}
    k = fvs202.kfvs(G)[0]; F = set()
    if k == 1:            # every single feedback vertex (removal leaves the Xi-graph acyclic)
        adj = fvs202.xigraph(G); nodes = set(adj)
        for f in nodes:
            a2 = {x: [y for y in adj[x] if y != f] for x in nodes if x != f}
            if not fvs202.cyclic_parts(a2, set(a2)): F.add(movers[f])
    mx = mxf = 0; via = 0
    for t, s in enumerate(st):
        cur = list(s0)
        for x in range(G["N"]): cur[movers[x]] = gi[(x, s[x])]
        vs, sb = H[t]
        for v0 in range(n):
            v = v0; seen = set(); seq = []; w = vs[v0][0]; passf = False
            while v not in seen:
                seen.add(v)
                if v in F: passf = True
                if v in isE and E.rank[v] > E.rank[w]: seq.append((E.rank[v], passf)); passf = False
                v = cur[v] if h.owner[v] == 0 else sb[v]
            a = sum(1 for i in range(1, len(seq)) if seq[i][0] > seq[i - 1][0])
            mx = max(mx, a)
            if v0 in faces: mxf = max(mxf, a)
            via = max(via, sum(1 for i in range(1, len(seq)) if seq[i][0] > seq[i - 1][0] and seq[i][1]))
    return dict(k=k, U=gfc203.UG(G), T=len(st) - 1, maxasc=mx, maxasc_faces=mxf, maxasc_viaF=via)

if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] == "--rand":
        mode, seed, cnt = a[1], int(a[2]), int(a[3]); rng = random.Random(seed); c = collections.Counter(); hist = collections.Counter()
        import rand191
        os.environ["K1_MODE"] = "2" if mode == "k2" else "1"
        import k1srch202
        while c["genomes"] < cnt:
            if mode == "rand": G = rand191.rgen(rng, rng.randint(1, 6), rng.randint(1, 3), rng.randint(2, 3))
            else:
                G = k1srch202.mk(rng)
                if G is None or fvs202.kfvs(G)[0] != (2 if mode == "k2" else 1): continue
            r = asc(G); c["genomes"] += 1; hist[(r["k"] if r["k"] <= 3 else ">3", r["maxasc"])] += 1
            for kk in ("maxasc", "maxasc_faces", "maxasc_viaF", "T"): c[kk] = max(c[kk], r[kk])
        print(mode, "seed", seed, dict(c), "hist(k,maxasc)", sorted(hist.items(), key=str), flush=True)
    else:
        for f in a:
            G = json.load(open(f)); r = asc(G)
            print(os.path.basename(f), " ".join(f"{k} {v}" for k, v in r.items()), flush=True)
