#!/usr/bin/env python3
"""Box 25: on o-cyclic C^1O runs, while τ is fixed, is W = V_{σ,τ} pointwise non-decreasing at every transition (arena steps:
Lemma W, proved; fallback steps: open)? Usage: wmono_cyc.py N nmin nmax seed [--randstart]"""
from common import *
if __name__ == "__main__":
    RS = "--randstart" in sys.argv
    if RS: sys.argv.remove("--randstart")
    N, lo, hi, seed = map(int, sys.argv[1:5]); rng = random.Random(seed); cnt = {"runs": 0, "steps": 0, "fb_steps": 0, "W_drop_arena": 0, "W_drop_fb": 0}
    for i in range(N):
        g = rand_c1o(rng, lo, hi, forced=0.1)
        if g is None: continue
        start = ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0}, {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) if RS else None
        E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); cnt["runs"] += 1
        while True:
            r = step(g, E, Ed, s, t)
            if r is None: break
            ns, nt, Is, It, fb, _, _ = r
            if list(nt) == list(t):
                cnt["steps"] += 1; cnt["fb_steps"] += fb
                Eg, W0 = wvals(g, s, t); _, W1 = wvals(g, ns, t)
                if any(Eg.key(W1[v]) < Eg.key(W0[v]) for v in range(g.n)): cnt["W_drop_fb" if fb else "W_drop_arena"] += 1
            s, t = ns, nt
    print(cnt)
