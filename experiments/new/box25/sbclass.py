#!/usr/bin/env python3
"""Box 25: classify σ̄(o) changes a -> a' inside one (τ, joint-λ)-phase of o-cyclic C^1O runs:
  DOWN   a' lies on a's σ_{k+1}-path (the new minimum is downstream of the old one: the ring walk)
  INR    a ∈ R_{k+1} (the old minimum now routes through o)
  OTHER  neither.
Usage: sbclass.py game.pg | sbclass.py --random N nmin nmax seed"""
from common import *
from thtrace import Rset
def path(g, s, t, a, o):
    nxt = [s[v] if g.owner[v] == 0 else t[v] for v in range(g.n)]; out, x = [], a
    while x not in out and x != o: out.append(x); x = nxt[x]
    return out
def classify(g, st, cnt, ex):
    E, Ed = Engine(g), Engine(dual(g)); o = odd_choice(g); prev = None
    for k, (s, t) in enumerate(st):
        Xi, sb = E.evaluate(s); U, _ = Ed.evaluate(t)
        lam = (tuple(x[0] for x in Xi), tuple(y[0] for y in U), t[o])
        if prev and prev[0] == lam and prev[1] != sb[o]:
            a, a2 = prev[1], sb[o]; R = Rset(g, s, t, o)
            if a2 in path(g, s, t, a, o): cnt["DOWN"] += 1
            elif a in R: cnt["INR"] += 1
            else:
                cnt["OTHER"] += 1
                if ex is not None and not ex: ex.append((g, k))
        prev = (lam, sb[o])
if __name__ == "__main__":
    a = sys.argv[1:]; cnt = {"DOWN": 0, "INR": 0, "OTHER": 0}; ex = []
    if a[0] == "--random":
        N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        for i in range(N):
            g = rand_c1o(rng, lo, hi, forced=0.0)
            if g is None: continue
            st, _ = trace(g, check=False); classify(g, st, cnt, ex)
        print(cnt)
        if ex: g, k = ex[0]; print("OTHER example n", g.n, "state", k, g.prio, g.owner, g.succ)
    else:
        g = load(a[0]); st, _ = trace(g); classify(g, st, cnt, None); print(cnt)
