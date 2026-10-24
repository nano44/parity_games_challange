#!/usr/bin/env python3
"""Box 21: data check of Theorem B (a)-(b): in plain N5 runs, every maximal tau-constant block's sigma sequence is a prefix of
the frozen run F_tau (climb_fix.even_only's step, i.e. S4a against tau + S4c Even fallback) from the block's first sigma.
Usage: blockcheck.py N nmax seed"""
import sys, random
from n5x import *
def fstep(g, E, sigma, tau):
    n = g.n; vs, _ = E.evaluate(tuple(sigma)); Is = E.improving(tuple(sigma), vs)
    if not Is: return None
    opt = {v: {sigma[v]} for v in range(n) if g.owner[v] == 0}
    for v, w in Is: opt[v].add(w)
    succ = [sorted(opt[v]) if g.owner[v] == 0 else [tau[v]] for v in range(n)]
    Er = Engine(dual(pg.Game(list(g.prio), list(g.owner), succ)))
    _, best = Er.evaluate(tuple(tau[v] if g.owner[v] == 1 else -1 for v in range(n)))
    ns = [best[v] if g.owner[v] == 0 else sigma[v] for v in range(n)]
    if ns == list(sigma):
        for v in {v for v, _ in Is}: ns[v] = max((w for x, w in Is if x == v), key=lambda w: (E.key(vs[w]), w))
    return ns
N, nmax, seed = map(int, sys.argv[1:]); rng = random.Random(seed); blocks = bad = 0
for _ in range(N):
    n = rng.randint(3, nmax)
    g = pg.Game([rng.randrange(n) for _ in range(n)], [rng.randrange(2) for _ in range(n)], [sorted(set(rng.sample(range(n), rng.choice((1, 2, 2, 3))))) for _ in range(n)])
    E = Engine(g); st, _ = trace(g, check=False); k = 0
    while k < len(st) - 1:
        j = k
        while j < len(st) - 1 and st[j + 1][1] == st[k][1]: j += 1      # states k..j share tau; j -> j+1 changes tau (or run ends)
        sig = list(st[k][0]); tau = st[k][1]
        for i in range(k, j):
            nxt = fstep(g, E, sig, tau)
            if nxt is None or tuple(nxt) != st[i + 1][0]: bad += 1; break
            sig = nxt
        blocks += 1; k = j + 1 if j > k else k + 1
print(f"tau-constant blocks {blocks}, mismatches with the frozen run {bad}")
