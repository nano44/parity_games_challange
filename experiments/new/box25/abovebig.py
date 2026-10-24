#!/usr/bin/env python3
"""Box 25: stress test with a planted 'above' part: core = random o-cyclic C^1O game on m vertices; then k Even vertices with
edges into the core and among themselves (any direction). Measures (a) longest stretch with σ|Z, τ unchanged vs |A|,
(b) states in such stretches with θ ◁ w, (c) whether every such stretch equals N5's run on the one-player game G_τ restricted to
A with Z frozen (checked as: Ξ = W on all vertices at those states). Usage: abovebig.py N m k seed [--randstart]"""
from common import *
from propz import reach
if __name__ == "__main__":
    RS = "--randstart" in sys.argv
    if RS: sys.argv.remove("--randstart")
    N, m, k, seed = map(int, sys.argv[1:5]); rng = random.Random(seed)
    cnt = {"runs": 0, "frozen": 0, "throttled": 0, "xi_ne_w": 0, "maxstretch": 0, "max_minus_A": -99}
    while cnt["runs"] < N:
        c = rand_c1o(rng, m, m, forced=0.1)
        if c is None: continue
        n = m + k; prio = list(c.prio) + [rng.randrange(n + 3) for _ in range(k)]; owner = list(c.owner) + [0] * k
        succ = [list(s) for s in c.succ] + [sorted(set(rng.sample(range(n), rng.choice((1, 2, 3))))) for _ in range(k)]
        o = odd_choice(c)
        for v in range(m, n):
            if not any(w < m for w in succ[v]): succ[v] = sorted(set(succ[v] + [rng.randrange(m)]))
        g = pg.Game(prio, owner, succ); Y = split(g, o); Z = set(range(n)) - Y | reach(g, o); A = [v for v in range(n) if v not in Z]
        start = ({v: rng.choice(g.succ[v]) for v in range(n) if g.owner[v] == 0}, {v: rng.choice(g.succ[v]) for v in range(n) if g.owner[v] == 1}) if RS else None
        st, _ = trace(g, start, check=False); cnt["runs"] += 1; E = Engine(g); ZE = [v for v in Z if owner[v] == 0]; cur = 0
        for j in range(len(st) - 1):
            fr = all(st[j + 1][0][v] == st[j][0][v] for v in ZE) and st[j + 1][1] == st[j][1]
            if fr:
                cnt["frozen"] += 1; Xi, _ = E.evaluate(st[j][0]); _, W = wvals(g, *st[j])
                if E.key(Xi[o]) != E.key(W[o]): cnt["throttled"] += 1
                if any(E.key(Xi[v]) != E.key(W[v]) for v in range(n)): cnt["xi_ne_w"] += 1
            cur = cur + 1 if fr else 0; cnt["maxstretch"] = max(cnt["maxstretch"], cur); cnt["max_minus_A"] = max(cnt["max_minus_A"], cur - len(A))
    print(cnt)
