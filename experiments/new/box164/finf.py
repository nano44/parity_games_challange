#!/usr/bin/env python3
"""L-NEW box 164: record multiplicity in the external-flip model with UNLIMITED flips (T_inf, P-IDEAL-FLIP §1, box 163 §1).
Graph: U-states u (level 0 fixed, ISO) -> Step^c(u) for c in {0,1} when it moves (acyclic by MONO-FLIP). For each record r = (x,
decisive beta of the A-comparison under u), DP = largest number of r-moves on one path; mu_inf = max over r. Also T_inf of the genome.
Usage: finf.py rand m count seed | finf.py climb m iters restarts seed | finf.py file.json ..."""
import os, sys, json, random, itertools, copy
H = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(H, "rec.py")).read().split("\nif __name__")[0])
cstep = fns["cstep"]; mutate = None
exec(open(os.path.join(H, "climb.py")).read().split("def score")[0].split("exec(open")[0])  # nothing
src = open(os.path.join(H, "climb.py")).read(); mstart = src.index("def mutate"); mend = src.index("def score")
exec(src[mstart:mend])

def analyse(G):
    g = Gen(G); N = g.N; U = [x for x in range(N) if g.lev[x] >= 1]
    base = tuple(G["start"][x] if g.lev[x] == 0 else 0 for x in range(N))
    states = []
    for bits in itertools.product((0, 1), repeat=len(U)):
        s = list(base)
        for x, b in zip(U, bits): s[x] = b
        states.append(tuple(s))
    succ = {}
    for s in states:
        out = []
        for c in (0, 1):
            t = cstep(g, s, c)
            if t != s:
                rs = [(x, decisive(g, chain(g, s, x, t[x]), chain(g, s, x, s[x]))) for x in U if t[x] != s[x]]
                out.append((t, rs))
        succ[s] = out
    memo = {}
    def lp(s):
        if s not in memo: memo[s] = max([1 + lp(t) for t, _ in succ[s]], default=0)
        return memo[s]
    Tinf = max(lp(s) for s in states)
    recs = set(r for s in states for _, rs in succ[s] for r in rs); mu = 0; arg = None
    for r in recs:
        m2 = {}
        def f(s):
            if s not in m2: m2[s] = max([(r in rs) + f(t) for t, rs in succ[s]], default=0)
            return m2[s]
        v = max(f(s) for s in states)
        if v > mu: mu, arg = v, r
    return Tinf, mu, arg

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    if sys.argv[1] == "rand":
        m, cnt, seed = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]); rng = random.Random(seed); best = (0, 0)
        for i in range(cnt):
            G = rand_lr(m + 1, rng, iso=True); T, mu, arg = analyse(G)
            if (mu, T) > best: best = (mu, T); json.dump(G, open(os.path.join(H, "out", "finf_m%d_mu%d_T%d.json" % (m, mu, T)), "w"))
        print("FINF rand m %d count %d: max (mu_inf, T_inf) %s" % (m, cnt, best))
    elif sys.argv[1] == "climb":
        m, iters, restarts, seed = map(int, sys.argv[2:6]); rng = random.Random(seed); best = (0, 0)
        for rs in range(restarts):
            G = rand_lr(m + 1, rng, iso=True); T, mu, _ = analyse(G); s = (mu, T)
            for it in range(iters):
                G2 = mutate(G, rng); T2, mu2, _ = analyse(G2)
                if (mu2, T2) >= s: G, s = G2, (mu2, T2)
            if s > best: best = s; json.dump(G, open(os.path.join(H, "out", "finfclimb_m%d_mu%d_T%d.json" % (m, s[0], s[1])), "w"))
            print("restart %d (mu_inf, T_inf) %s best %s" % (rs, s, best), flush=True)
    else:
        for f in sys.argv[1:]:
            G = json.load(open(f)); print(os.path.basename(f), "T_inf %d mu_inf %d record %s" % analyse(G))
