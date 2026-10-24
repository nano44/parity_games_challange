#!/usr/bin/env python3
"""Box 25: Even fallbacks with τ fixed, classified by (h) and by θ ◁ w; under (h) ∧ θ ◁ w, count gate edges of type d2 (leaving R).
Usage: fbh.py N nmin nmax seed [--randstart]"""
from common import *
from wdrop_h import oncycle
from thtrace import Rset
if __name__ == "__main__":
    a = sys.argv[1:]; RS = "--randstart" in a; OUT = a[a.index("--write") + 1] if "--write" in a else None; N, lo, hi, seed = map(int, a[0:4]); rng = random.Random(seed)
    cnt = {"fb": 0, "fb_h": 0, "fb_h_thr": 0, "fb_h_thr_d2": 0, "fb_h_drop": 0}
    for i in range(N):
        g = rand_c1o(rng, lo, hi, forced=0.0)
        if g is None: continue
        start = ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0}, {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) if RS else None
        E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); o = odd_choice(g)
        ST = ({v: s[v] for v in range(g.n) if g.owner[v] == 0}, {v: t[v] for v in range(g.n) if g.owner[v] == 1})
        while True:
            r = step(g, E, Ed, s, t)
            if r is None: break
            ns, nt, Is, It, fb, vs, _ = r
            if fb and list(nt) == list(t):
                cnt["fb"] += 1; _, sb = E.evaluate(tuple(s)); Eg, W0 = wvals(g, s, t)
                if not oncycle(g, s, sb, o) and not oncycle(g, s, t, o) and vs[o][0] == W0[o][0]:
                    cnt["fb_h"] += 1
                    if E.key(vs[o]) < Eg.key(W0[o]):
                        cnt["fb_h_thr"] += 1; R = Rset(g, s, t, o)
                        if OUT and cnt["fb_h_thr"] == 1:
                            from abovefind import write
                            write(g, ST, OUT); print("wrote", OUT, "n", g.n, "sigma", s, "tau", t, "Is", Is, "R", sorted(R), flush=True)
                        if any(v in R and w not in R for v, w in Is): cnt["fb_h_thr_d2"] += 1
                    _, W1 = wvals(g, ns, t)
                    if any(Eg.key(W1[v]) < Eg.key(W0[v]) for v in range(g.n)): cnt["fb_h_drop"] += 1
            s, t = ns, nt
    print(cnt)
