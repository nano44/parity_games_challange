#!/usr/bin/env python3
"""REFEREE-2 succ. 30: cross-validate si.py Engine (VJ values + Odd optimal counter) against my brute-force VJ (r2vjg.py: enumerate
every Odd positional strategy, take the pointwise ⊴-minimum, asserted to exist) on Γ(G) of small random Ξ-cyclic genomes, at random
mover states. Priorities made injective by rank (Ω, index), as si.py. Compares (Λ, Π, k) at every vertex. Usage: r2xval.py SEED COUNT"""
import sys, random
import r2vjg as B, r2howcyc as H
seed, cnt = map(int, sys.argv[1:3]); rng = random.Random(seed); C = dict(states=0, vertices=0, mismatch=0, skipped=0)
while C['states'] < cnt:
    G = H.R.rand_genome(rng, 4, 2, acyclic=False)
    g, sig, tau, m = H.R.build(G, esc=True); n = g.n; N = G['N']
    if m['M'] > 7: C['skipped'] += 1; continue
    succ = [list(s) if (g.owner[v] == 1 or v < N) else [sig[v]] for v, s in enumerate(g.succ)]
    h = H.pg.Game(list(g.prio), list(g.owner), succ); E = H.Engine(h)
    rank = {v: r for r, v in enumerate(sorted(range(n), key=lambda v: (h.prio[v], v)))}
    pri = [2 * rank[v] + h.prio[v] % 2 for v in range(n)]          # injective, parity kept (si.py's p')
    s = [rng.choice(succ[v]) if v < N else (sig[v] if h.owner[v] == 0 else -1) for v in range(n)]
    vE, _ = E.evaluate(tuple(s)); vB, _ = B.evaluate(n, pri, list(h.owner), succ, s)
    for v in range(n):
        C['vertices'] += 1
        bmask = sum(1 << rank[u] for u in vB[v][1])
        if (vE[v][0], vE[v][1], vE[v][2]) != (vB[v][0], bmask, vB[v][2]): C['mismatch'] += 1
    C['states'] += 1
print('seed', seed, C)
