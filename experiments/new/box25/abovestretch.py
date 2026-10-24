#!/usr/bin/env python3
"""Box 25: o-cyclic C^1O, A := V \\ Z (vertices that reach o but are not reachable from o; Z = X ∪ Reach(o)).
Longest stretch of transitions with σ|Z and τ unchanged (only A moves), vs |A|; also whether Ξ = W on Z at those states (θ = w).
Usage: abovestretch.py --random N nmin nmax seed [--randstart]"""
from common import *
from propz import reach
if __name__ == "__main__":
    RS = "--randstart" in sys.argv
    if RS: sys.argv.remove("--randstart")
    N, lo, hi, seed = map(int, sys.argv[2:6]); rng = random.Random(seed)
    worst = (-99, None); cnt = {"runs": 0, "stretch_states": 0, "throttled_states": 0}
    for i in range(N):
        g = rand_c1o(rng, lo, hi)
        if g is None: continue
        o = odd_choice(g); Y = split(g, o); Z = set(range(g.n)) - Y | reach(g, o); A = [v for v in range(g.n) if v not in Z]
        if not A: continue
        start = ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                 {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) if RS else None
        st, _ = trace(g, start, check=False); cnt["runs"] += 1; E = Engine(g)
        ZE = [v for v in Z if g.owner[v] == 0]; best = cur = 0
        for k in range(len(st) - 1):
            frozen = all(st[k + 1][0][v] == st[k][0][v] for v in ZE) and st[k + 1][1] == st[k][1]
            if frozen:
                cnt["stretch_states"] += 1; Xi, _ = E.evaluate(st[k][0]); _, W = wvals(g, *st[k])
                if E.key(Xi[o]) != E.key(W[o]): cnt["throttled_states"] += 1
            cur = cur + 1 if frozen else 0; best = max(best, cur)
        if best - len(A) > worst[0]: worst = (best - len(A), (i, g.n, len(A), best))
    print(cnt, "worst (stretch - |A|, (i, n, |A|, stretch))", worst)
