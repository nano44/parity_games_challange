#!/usr/bin/env python3
"""Cross-check of honff.lev's optimistic-completion prune: LEV with and without the prune on every state of random C^kO runs (n 5-14),
plus a brute-force LEV (enumerate every simple G_tau path) for n <= 9. Usage: levcheck.py GAMES SEED"""
import random, sys
import census as C, honff as H
from census import SpecSI
ng, seed = int(sys.argv[1]), int(sys.argv[2]); rng = random.Random(seed); cmp_ = bad = 0


def brute(g, SG, Xi, lam, tau):
    n = g.n; succ = H.gtau_succ(g, tau); best = n
    cyc = {c for c in range(n) if lam[c] == c}
    def dfs(x, v, path, L):
        nonlocal best
        if v in cyc:
            rc = (g.prio[v], v); P = frozenset(w for w in path[:-1] if (g.prio[w], w) > rc)
            if SG.nvo(Xi[x], (v, P, L)) < 0: best = min(best, L)
        for w in succ[v]:
            if w not in path: dfs(x, w, path + [w], L + 1)
    for x in range(n): dfs(x, x, [x], 0)
    return min(n - 1, best - 1)


for i in range(ng):
    n = rng.randint(5, 14); g = C.rand_ckO(rng, n, rng.randint(1, min(4, n)))
    states, fbs = C.run_states(g, *C.rand_start(g, rng)); SG = SpecSI(g)
    for s, t in states:
        A = C.state_info(g, SG, s, t)
        H.PRUNE = True; a = H.lev(g, SG, A["Xi"], A["lam"], t)
        H.PRUNE = False; b = H.lev(g, SG, A["Xi"], A["lam"], t)
        c = brute(g, SG, A["Xi"], A["lam"], t) if n <= 9 else b
        cmp_ += 1
        if not (a == b == c):
            bad += 1; print("MISMATCH", n, a, b, c)
print(f"states compared {cmp_}, mismatches {bad}")
