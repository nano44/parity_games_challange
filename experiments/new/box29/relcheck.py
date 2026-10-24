#!/usr/bin/env python3
"""Box 29: at OTHER states with H2 whose honest values on R have route form (pattern "3", or pattern "13" with λ_Ξ(o) = o):
is c_θ = λ_Ξ(o) more relevant (Engine rank) than c_w = λ_W(o)? Lemma P3' covers exactly the "c_θ higher" case.
Usage: relcheck.py game.pg [start] | relcheck.py --rand N lo hi seed [--randstart]"""
import sys, random
from otherx import *

def analyse(g, start, acc):
    E, Ed = Engine(g), Engine(dual(g)); o = odd_choice(g); s, t = start_pair(g, E, Ed, start)
    while True:
        Xi, sb = E.evaluate(tuple(s)); _, W = wvals(g, s, t)
        h = (not oncycle(g, s, sb, o), not oncycle(g, s, t, o), Xi[o][0] == W[o][0])
        Xk = [E.key(Xi[v]) for v in range(g.n)]; Wk = [E.key(W[v]) for v in range(g.n)]
        if not all(h) and Xk != Wk:
            pat = clause(h); cth, cw = Xi[o][0], W[o][0]
            if h[1] and (h[0] or cth == o):
                key = (pat + ("(cθ=o)" if cth == o else ""), "cθ higher" if E.rank[cth] > E.rank[cw] else "cw higher")
            else:
                key = (pat, "not route form / H2 fails")
            acc[key] = acc.get(key, 0) + 1
        r = step(g, E, Ed, s, t)
        if r is None: break
        s, t = r[0], r[1]

if __name__ == "__main__":
    a = sys.argv[1:]; acc = {}
    if a[0] != "--rand":
        g = load(a[0]); analyse(g, readstart(a[1]) if len(a) > 1 else None, acc)
    else:
        RS = "--randstart" in a; N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        for i in range(N):
            g = rand_c1o(rng, lo, hi, forced=0.0)
            if g is None: continue
            start = ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                     {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) if RS else None
            analyse(g, start, acc)
    for k, v in sorted(acc.items()): print(k, v)
