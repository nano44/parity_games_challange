#!/usr/bin/env python3
"""Box 25, data for (TRUST): per (τ, joint-λ)-phase, the number of TRUST EVENTS = (state, vertex) pairs where a vertex z enters the
trust set T_k = {z ∈ R_k Even : some honest-improving edge (z, y) with y ∉ R_k} (type d2, box 21 Lemma G). Reports the max per
phase, and the phase length. Usage: trustcount.py game.pg [start] | trustcount.py --random N nmin nmax seed"""
from common import *
from thtrace import Rset
def count(g, st):
    E, Ed = Engine(g), Engine(dual(g)); o = odd_choice(g); prevT, prevlam = set(), None; per = best = 0; plen = bestlen = 0
    for s, t in st:
        Xi, _ = E.evaluate(s); U, _ = Ed.evaluate(t); lam = (tuple(x[0] for x in Xi), tuple(y[0] for y in U), t[o])
        R = Rset(g, s, t, o); T = {v for v, w in E.improving(s, Xi) if v in R and w not in R}
        if lam != prevlam: per, plen, prevT = 0, 0, set()
        per += len(T - prevT); plen += 1; prevT, prevlam = T, lam
        if per > best: best = per
        bestlen = max(bestlen, plen)
    return best, bestlen
if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] == "--random":
        N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed); worst = {}
        for i in range(N):
            g = rand_c1o(rng, lo, hi, forced=0.0)
            if g is None: continue
            st, _ = trace(g, check=False); b, _ = count(g, st); worst[g.n] = max(worst.get(g.n, 0), b)
        print("max trust events per phase, by n:", dict(sorted(worst.items())))
    else:
        g = load(a[0]); st, _ = trace(g, readstart(a[1]) if len(a) > 1 else None); print(a[0], "n", g.n, "(max trust events/phase, longest phase states)", count(g, st))
