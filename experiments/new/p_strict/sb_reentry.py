#!/usr/bin/env python3
"""Box 9: find a within-phase re-entry (a step whose improving edges were ALL in arenas earlier in the same λ-phase) in random
one-player games and print the trace: per step the switched edges, the improving set, λ, and the valuations of the endpoints of the
re-entering edges at both times. Usage: sb_reentry.py games seed nmax"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..")); sys.path.insert(0, os.path.join(HERE, "..", "..", "harness"))
import pg
from n5 import Engine
def trace(g, s, verbose=False):
    E = Engine(g); hist = []; U = {}; lamprev = None; k = 0; found = None
    while True:
        vs, _ = E.evaluate(tuple(s)); Is = E.improving(tuple(s), vs); lam = tuple(vs[x][0] for x in range(g.n))
        if lam != lamprev: U = {v: {s[v]} for v in range(g.n) if g.owner[v] == 0}; ph_start = k
        lamprev = lam
        if Is and k > ph_start and not any(w not in U[v] for v, w in Is): found = found or k
        hist.append((list(s), [vs[x] for x in range(g.n)], sorted(Is)))
        if not Is: break
        A = {v: {s[v]} | {w for x, w in Is if x == v} for v in range(g.n) if g.owner[v] == 0}
        for v in A: U[v] |= A[v]
        h = pg.Game(list(g.prio), list(g.owner), [sorted(A[v]) if g.owner[v] == 0 else list(g.succ[v]) for v in range(g.n)])
        Eh = Engine(h); x, _ = Eh.run(Eh.rule_switch_all, tuple(s)); s = list(x); k += 1
    return found, hist
games, seed, nmax = map(int, sys.argv[1:4]); rng = random.Random(seed)
for _ in range(games):
    n = rng.randint(3, nmax); owner = [rng.randrange(2) for _ in range(n)]; pr = rng.sample(range(2 * n), n)
    succ = [sorted(set(rng.randrange(n) for _ in range(rng.randint(1, 4)))) if owner[v] == 0 else [rng.randrange(n)] for v in range(n)]
    g = pg.Game(pr, owner, succ)
    for _ in range(3):
        s = [rng.choice(succ[v]) if owner[v] == 0 else -1 for v in range(n)]
        f, hist = trace(g, s)
        if f:
            print(pg.dumps(g)); print("re-entry at step", f)
            for k, (st, val, I) in enumerate(hist): print(k, "σ", st, "\n   I", I, "\n   Ω", val)
            sys.exit()
