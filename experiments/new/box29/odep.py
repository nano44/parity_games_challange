#!/usr/bin/env python3
"""Box 29: at OTHER states, classify throttled edges (W-improving, not in the gate) as INTO-o (z = o), FROM-o-successor (σ(x) = o),
or GENUINE (z ≠ o and σ(x) ≠ o); and count o-DEPENDENT vertices: x ≠ o whose W-path to its W-cycle node λ_W(x) passes through o.
Usage: odep.py game.pg [start] | odep.py --rand N lo hi seed [--randstart]"""
import sys, random
from otherx import *

def wpath_hits_o(g, s, t, x, cyc, o):
    nxt = [s[v] if g.owner[v] == 0 else t[v] for v in range(g.n)]; v, seen = x, set()
    while v != cyc and v not in seen:
        if v == o: return True
        seen.add(v); v = nxt[v]
    return False

def analyse(g, start, acc):
    E, Ed = Engine(g), Engine(dual(g)); o = odd_choice(g); s, t = start_pair(g, E, Ed, start)
    while True:
        Xi, sb = E.evaluate(tuple(s)); _, W = wvals(g, s, t)
        Xk = [E.key(Xi[v]) for v in range(g.n)]; Wk = [E.key(W[v]) for v in range(g.n)]
        h = (not oncycle(g, s, sb, o), not oncycle(g, s, t, o), Xi[o][0] == W[o][0])
        if not all(h) and Xk != Wk:
            pat = clause(h); gate = set(E.improving(tuple(s), Xi))
            for x in range(g.n):
                if g.owner[x] != 0: continue
                for z in g.succ[x]:
                    if z != s[x] and Wk[z] > Wk[s[x]] and (x, z) not in gate:
                        kind = "INTO-o" if z == o else ("FROM-σ=o" if s[x] == o else "GENUINE")
                        acc[(pat, kind)] = acc.get((pat, kind), 0) + 1
            dep = sum(1 for x in range(g.n) if x != o and W[x][0] != x and wpath_hits_o(g, s, t, x, W[x][0], o))
            acc[(pat, "states")] = acc.get((pat, "states"), 0) + 1
            acc[(pat, "states with o-dependent vertices")] = acc.get((pat, "states with o-dependent vertices"), 0) + (dep > 0)
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
