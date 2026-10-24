#!/usr/bin/env python3
"""Box 29: THROTTLED edges := Even edges (x, z) that are W-improving (W(z) ▷ W(σ x)) but not in the gate Iσ (Ξ-improving).
Counts states with ≥ 1 throttled edge, by state type (EQ / THR / OTHER + clause pattern), and the λ_W-map changes inside OTHER blocks.
Usage: throttle.py game.pg [start] | throttle.py --rand N lo hi seed [--randstart]"""
import sys, random
from otherx import *

def analyse(g, start, acc):
    E, Ed = Engine(g), Engine(dual(g)); o = odd_choice(g); s, t = start_pair(g, E, Ed, start); prev = None
    while True:
        Xi, sb = E.evaluate(tuple(s)); _, W = wvals(g, s, t)
        Xk = [E.key(Xi[v]) for v in range(g.n)]; Wk = [E.key(W[v]) for v in range(g.n)]
        h = (not oncycle(g, s, sb, o), not oncycle(g, s, t, o), Xi[o][0] == W[o][0])
        typ = ("O" + clause(h)) if (not all(h) and Xk != Wk) else ("E" if Xk == Wk else "T")
        gate = set(E.improving(tuple(s), Xi))
        thr = [(x, z) for x in range(g.n) if g.owner[x] == 0 for z in g.succ[x] if z != s[x] and Wk[z] > Wk[s[x]] and (x, z) not in gate]
        key = (typ, "throttled" if thr else "none"); acc[key] = acc.get(key, 0) + 1
        lamW = tuple(W[v][0] for v in range(g.n))
        if prev and prev[0].startswith("O") and typ.startswith("O") and prev[1] != lamW: acc["lamW_change_in_OTHER"] = acc.get("lamW_change_in_OTHER", 0) + 1
        prev = (typ, lamW)
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
    for k, v in sorted(acc.items(), key=lambda kv: str(kv[0])): print(k, v)
