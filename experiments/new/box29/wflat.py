#!/usr/bin/env python3
"""Box 29: arena (S4a) steps with W unchanged at every vertex but Ξ changed (W-FLAT, honest-strict), by state type of the source.
Usage: wflat.py game.pg [start] | wflat.py --rand N lo hi seed [--randstart]"""
import sys, random
from otherx import *

def analyse(g, start, acc):
    E, Ed = Engine(g), Engine(dual(g)); o = odd_choice(g); s, t = start_pair(g, E, Ed, start)
    while True:
        Xi, sb = E.evaluate(tuple(s)); _, W = wvals(g, s, t)
        Xk = [E.key(Xi[v]) for v in range(g.n)]; Wk = [E.key(W[v]) for v in range(g.n)]
        h = (not oncycle(g, s, sb, o), not oncycle(g, s, t, o), Xi[o][0] == W[o][0])
        typ = ("OTHER" if (not all(h) and Xk != Wk) else ("EQ" if Xk == Wk else "THR"))
        r = step(g, E, Ed, s, t)
        if r is None: break
        ns, nt, fb = r[0], r[1], r[4]
        if not fb and tuple(nt) == tuple(t) and tuple(ns) != tuple(s):
            Xi2, _ = E.evaluate(tuple(ns)); _, W2 = wvals(g, ns, t)
            wf = all(E.key(W2[v]) == Wk[v] for v in range(g.n)); xc = any(E.key(Xi2[v]) != Xk[v] for v in range(g.n))
            acc[(typ, "arena steps")] = acc.get((typ, "arena steps"), 0) + 1
            if wf and xc: acc[(typ, "W-flat honest-strict")] = acc.get((typ, "W-flat honest-strict"), 0) + 1
        s, t = ns, nt

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
