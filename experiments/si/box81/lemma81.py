#!/usr/bin/env python3
"""L-SI box 81: DATA for Lemma BETA-ACYC / Theorem ACYC-LIN (docs/si/box81-bridge.md §3). On Xi-ACYCLIC genomes, along the IDEAL-CYC
Howard run (ref/ idealcyc.py + si.py Engine), count: states; (state, gate) pairs where sigma-bar is NOT the beta-face (lemma: 0);
(state, gate) pairs where the beta-face is not STRICTLY better for Odd (lemma: 0); C, R (lemma: 0, 0); runs with T > N (theorem: 0).
Genomes: rand191.rgen(rng, d, w, deg) (L-NEW's generator, byte copy), d 1-6, w 1-3, deg 2-3, kept only if Xi-acyclic; plus FILES.
Mode agen: own Xi-acyclic generator agen (same shape, Xi-targets earlier in a random order). Usage: lemma81.py [agen|rgen] COUNT SEED [FILES.json]"""
import sys, os, json, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [HERE, os.path.join(HERE, "ref", "experiments", "new", "box191"), os.path.join(HERE, "ref", "experiments", "new", "box189")]
import idealcyc, gamma3, rand191, census81


def agen(rng, d, w, D, pX=0.2):
    """Xi-ACYCLIC variant of rand191.rgen (own code): Xi-targets only to movers earlier in a random order pi (or X)."""
    N = d * w; lev = [v // w for v in range(N)]; pi = list(range(N)); rng.shuffle(pi); pos = {x: i for i, x in enumerate(pi)}
    opts = []; M = 0
    for v in range(N):
        o = []
        for k in range(rng.randint(2, D)):
            wt = rng.choice([y for y in range(N) if lev[y] == lev[v] - 1]) if lev[v] else -1
            cand = [y for y in range(N) if pos[y] < pos[v]]
            xt = -1 if (not cand or rng.random() < pX) else rng.choice(cand)
            o.append([wt, xt, M]); M += 1
        opts.append(o)
    br = list(range(M)); rng.shuffle(br); bp = [rng.randrange(2) for _ in range(M)]
    gt = list(range(M)); rng.shuffle(gt); it = iter(gt); gate = [[next(it) for _ in o] for o in opts]
    return dict(N=N, lev=lev, opts=opts, gate=gate, br=br, bp=bp, start=[rng.randrange(len(o)) for o in opts])


def check(G):
    h, s0, movers, inv = idealcyc.build(G); E = idealcyc.Engine(h); st = idealcyc.run(G)
    _, _, _, V = gamma3.build(G, set()); N = G["N"]
    gates = [(V[("g", (x, k))], V[("b", (x, k))]) for x in range(N) for k in range(len(G["opts"][x]))]
    gi = {}
    for x in range(N):
        for v in h.succ[movers[x]]: gi[(x, inv[v])] = v
    notb = nonstrict = C = R = 0; prev = None
    for s in st:
        cur = list(s0)
        for x in range(N): cur[movers[x]] = gi[(x, s[x])]
        vals, sb = E.evaluate(tuple(cur))
        for g, b in gates:
            e = [w for w in h.succ[g] if w != b][0]
            if sb[g] != b: notb += 1
            if not E.key(vals[b]) < E.key(vals[e]): nonstrict += 1
        key = ([vals[v][0] for v in range(h.n)], [sb[v] for v in range(h.n) if h.owner[v] == 1])
        if prev is not None:
            if key[0] != prev[0]: C += 1
            elif key[1] != prev[1]: R += 1
        prev = key
    return len(st) - 1, N, notb, nonstrict, C, R


if __name__ == "__main__":
    MODE = sys.argv.pop(1) if sys.argv[1] in ("agen", "rgen") else "rgen"
    cnt, seed = int(sys.argv[1]), int(sys.argv[2]); rng = random.Random(seed)
    tot = dict(genomes=0, tried=0, states=0, notbeta=0, nonstrict=0, C=0, R=0, T_gt_N=0, maxT_over_N=0.0)
    gl = [json.load(open(f)) for f in sys.argv[3:]]
    target = cnt + len(gl)
    while tot["genomes"] < target:
        if gl: G = gl.pop(0)
        else:
            tot["tried"] += 1
            gen = agen if MODE == "agen" else rand191.rgen
            G = gen(rng, rng.randint(1, 6), rng.randint(1, 3), rng.randint(2, 3))
            if not census81.xi_acyclic(G): continue
        T, N, nb, ns, C, R = check(G)
        tot["genomes"] += 1; tot["states"] += T + 1; tot["notbeta"] += nb; tot["nonstrict"] += ns; tot["C"] += C; tot["R"] += R
        tot["T_gt_N"] += T > N; tot["maxT_over_N"] = max(tot["maxT_over_N"], round(T / N, 3))
    print(f"lemma81 {MODE} count {cnt} seed {seed} files {len(sys.argv) - 3}:", " ".join(f"{k} {v}" for k, v in tot.items()))
