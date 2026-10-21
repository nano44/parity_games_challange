#!/usr/bin/env python3
"""Box 10: direct check of fact (F1) as used in Lemma P: on one-player games, after a switch-best step rho_k -> rho_{k+1}, for every improving
edge (x,z) of rho_k the single-switch strategy rho_k[x->z] is dominated pointwise by rho_{k+1} (Omega_{k+1} >= val_{rho_k[x->z]} at every
vertex), and Omega_{k+1} >= Omega_k pointwise (F2). Usage: f1_check.py games seed nmax"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..")); sys.path.insert(0, os.path.join(HERE, "..", "..", "harness"))
import pg
from n5 import Engine
from phase_trace import sbstep
games, seed, nmax = map(int, sys.argv[1:4]); rng = random.Random(seed); checks = viol = steps = 0
for _ in range(games):
    n = rng.randint(3, nmax); owner = [0 if rng.random() < 0.75 else 1 for _ in range(n)]; pr = rng.sample(range(2 * n), n)
    succ = [sorted(set(rng.randrange(n) for _ in range(rng.randint(1, 4)))) if owner[v] == 0 else [rng.randrange(n)] for v in range(n)]
    g = pg.Game(pr, owner, succ); E = Engine(g)
    for _ in range(2):
        s = [rng.choice(succ[v]) if owner[v] == 0 else -1 for v in range(n)]
        while True:
            vs, _ = E.evaluate(tuple(s)); Is = E.improving(tuple(s), vs)
            ns, _, _ = sbstep(g, E, s)
            if ns is None: break
            vs2, _ = E.evaluate(tuple(ns)); steps += 1
            for v in range(n):
                checks += 1
                if E.key(vs2[v]) < E.key(vs[v]): viol += 1; print("F2 VIOLATION", g.prio, g.owner, g.succ, s)
            for (x, z) in Is:
                h = list(s); h[x] = z; vh, _ = E.evaluate(tuple(h))
                for v in range(n):
                    checks += 1
                    if E.key(vs2[v]) < E.key(vh[v]): viol += 1; print("F1 VIOLATION", dict(x=x, z=z, v=v), g.prio, g.owner, g.succ, s)
            if ns == s: break
            s = ns
print(f"games={games} nmax={nmax} steps={steps} checks={checks} violations={viol}")
