#!/usr/bin/env python3
"""Box 27: at Even fallbacks at throttled (h)-states (θ ◁ w), classify every switched edge (x: σ(x) → z): D2 = x ∈ R, z ∉ R (a leave);
FLATF = x, z ∈ F with x its own cycle node and W unchanged at x; OTHER. Usage: fbedges.py game.pg [start] | --random N lo hi seed [--randstart]"""
from common import *
from thtrace import Rset
from wdrop_h import oncycle
from collections import Counter
def run(g, start, cnt):
    E, Ed = Engine(g), Engine(dual(g)); o = odd_choice(g); s, t = start_pair(g, E, Ed, start)
    while True:
        r = step(g, E, Ed, s, t)
        if r is None: break
        ns, nt, Is, It, fb, vs, _ = r
        if fb and list(nt) == list(t):
            _, sb = E.evaluate(tuple(s)); Eg, W = wvals(g, s, t)
            h = not oncycle(g, s, sb, o) and not oncycle(g, s, t, o) and vs[o][0] == W[o][0]
            if h and E.key(vs[o]) < Eg.key(W[o]):
                cnt["fb_thr_h"] += 1; R = Rset(g, s, t, o); _, W1 = wvals(g, ns, t); leaves = 0
                for x in range(g.n):
                    if g.owner[x] != 0 or ns[x] == s[x]: continue
                    z = ns[x]
                    if x in R and z not in R: cnt["D2"] += 1; leaves += 1
                    elif x not in R and z not in R and vs[x][0] == x and Eg.key(W1[x]) == Eg.key(W[x]): cnt["FLATF"] += 1
                    else: cnt["OTHER"] += 1
                if leaves == 0: cnt["fb_without_leave"] += 1
        s, t = list(ns), list(nt)
if __name__ == "__main__":
    a = sys.argv[1:]; cnt = Counter()
    if a[0] == "--random":
        RS = "--randstart" in a; N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        for i in range(N):
            g = rand_c1o(rng, lo, hi, forced=0.1)
            if g is None: continue
            st = ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0}, {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) if RS else None
            run(g, st, cnt)
        print(dict(cnt))
    else:
        g = load(a[0]); run(g, readstart(a[1]) if len(a) > 1 else None, cnt); print(a[0], dict(cnt))
