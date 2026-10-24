#!/usr/bin/env python3
"""Box 25: per state, the set of COMPLETE vertices K_k = {v : Ξ_k(v) = U_τk(v)} (U = Odd's honest dual valuation, G's order).
While τ is fixed, K only grows (Ξ ↑, U fixed, Ξ ⊴ U). Report the longest stretch of transitions with τ fixed and K unchanged.
Usage: complete.py game.pg [start] [-v] | complete.py --random N nmin nmax seed"""
from common import *
def gaps(g, st, verbose=False):
    E, Ed = Engine(g), Engine(dual(g)); Ks = []
    for s, t in st:
        Xi, _ = E.evaluate(s); U, _ = Ed.evaluate(t)
        Ks.append(frozenset(v for v in range(g.n) if vset(E, Xi[v]) == vset(Ed, U[v])))
    best = cur = 0
    for k in range(1, len(st)):
        if st[k][1] == st[k - 1][1] and Ks[k] == Ks[k - 1]: cur += 1
        else: cur = 0
        best = max(best, cur)
        if verbose: print(k, len(Ks[k]), sorted(set(range(g.n)) - Ks[k]))
    return best
if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] == "--random":
        N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed); worst = (0, None)
        for i in range(N):
            g = rand_c1o(rng, lo, hi)
            if g is None: continue
            st, _ = trace(g, check=False); b = gaps(g, st)
            if b - g.n > worst[0] - (worst[1][0] if worst[1] else 0): worst = (b, (g.n, i))
        print("worst (gap, (n, i))", worst)
    else:
        g = load(a[0]); st, _ = trace(g); print("longest K-constant stretch", gaps(g, st, "-v" in a), "n", g.n, "its", len(st) - 1)
