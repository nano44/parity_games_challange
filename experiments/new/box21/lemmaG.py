#!/usr/bin/env python3
"""Box 21, Lemma G check (games with one Odd choice vertex o; frozen tau = tau*): R = Even's sigma-reach set of o (vertices whose
sigma-path reaches o). Claim: every W-improving edge (x, z) outside the honest gate Iσ has sigma(x) not in R and z in R, and every
gated edge that is not W-improving has sigma(x) in R and z not in R (when the cycle nodes of Ξ(o) and W(o) agree and o is on no
cycle of either play). Usage: lemmaG.py game.pg [more.pg ...] | lemmaG.py --random N n seed"""
import sys, random
from n5x import *
from h1 import wvals
def reach(g, s, o):
    R = set()
    for v in range(g.n):
        x, seen = v, set()
        while x not in seen and x != o:
            seen.add(x)
            if g.owner[x] == 1: break
            x = s[x]
        if x == o: R.add(v)
    return R
def check(g, states, t, out):
    E = Engine(g); n = g.n; odd = [v for v in range(n) if g.owner[v] == 1 and len(g.succ[v]) > 1]
    if len(odd) != 1: return
    o = odd[0]
    for s, _ in states:
        X, _ = E.evaluate(s); Eg, W = wvals(g, s, t); Is = set(E.improving(s, X))
        if X[o][0] != W[o][0]: out["skip_cyc"] += 1; continue
        R = reach(g, s, o)
        if any(x in R for x in range(n) if X[x][0] in R or W[x][0] in R): out["skip_ocycle"] += 1; continue
        for x in range(n):
            if g.owner[x] != 0: continue
            for z in g.succ[x]:
                if z == s[x]: continue
                wi = Eg.key(W[z]) > Eg.key(W[s[x]]); hi = (x, z) in Is
                if wi and not hi:
                    out["withheld"] += 1
                    if not (s[x] not in R and z in R): out["bad_withheld"] += 1
                if hi and not wi:
                    out["extra"] += 1
                    if not (s[x] in R and z not in R): out["bad_extra"] += 1
        out["states"] += 1
if __name__ == "__main__":
    out = {k: 0 for k in ("states", "withheld", "bad_withheld", "extra", "bad_extra", "skip_cyc", "skip_ocycle")}
    if sys.argv[1] == "--random":
        N, n0, seed = map(int, sys.argv[2:5]); rng = random.Random(seed)
        for _ in range(N):
            n = rng.randint(5, n0); owner = [0] * n; o = rng.randrange(n); owner[o] = 1
            succ = [sorted(set(rng.sample(range(n), rng.choice((1, 2, 2, 3))))) for _ in range(n)]
            succ[o] = sorted(set(rng.sample(range(n), rng.choice((2, 3, 4)))))
            g = pg.Game([rng.randrange(n) for _ in range(n)], owner, succ)
            st, _ = trace(g, check=False); s0, ts = st[0][0], st[-1][1]
            fs, _ = trace(g, ({v: s0[v] for v in range(n) if owner[v] == 0}, {o: ts[o]}), check=False)
            check(g, fs, ts, out)
    else:
        for p in sys.argv[1:]:
            g = load(p); st, _ = trace(g); check(g, st, st[0][1], out)
    print(out)
