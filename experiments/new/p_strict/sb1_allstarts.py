#!/usr/bin/env python3
"""Box 8: Conjecture SB1 at small n: switch-best on random one-player games (Odd out-degree 1, cycles allowed) from ALL ⊕ starts;
reports max steps by n and any run with steps > n - 1. Usage: sb1_allstarts.py games seed nmax"""
import sys, os, random, itertools, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..")); sys.path.insert(0, os.path.join(HERE, "..", "..", "harness"))
import pg
from n5 import Engine
def sbsteps(g, s, E):
    k = 0
    while True:
        vs, _ = E.evaluate(tuple(s)); Is = E.improving(tuple(s), vs)
        if not Is: return k
        A = {v: {s[v]} | {w for x, w in Is if x == v} for v in range(g.n) if g.owner[v] == 0}
        h = pg.Game(list(g.prio), list(g.owner), [sorted(A[v]) if g.owner[v] == 0 else list(g.succ[v]) for v in range(g.n)])
        Eh = Engine(h); sb, _ = Eh.run(Eh.rule_switch_all, tuple(s)); s = list(sb); k += 1
games, seed, nmax = map(int, sys.argv[1:4]); rng = random.Random(seed); worst = {}; over = []
for _ in range(games):
    n = rng.randint(2, nmax); owner = [rng.randrange(2) for _ in range(n)]; pr = rng.sample(range(2 * n), n)
    succ = [sorted(set(rng.randrange(n) for _ in range(rng.randint(1, 3)))) if owner[v] == 0 else [rng.randrange(n)] for v in range(n)]
    g = pg.Game(pr, owner, succ); E = Engine(g)
    for st in itertools.product(*[succ[v] if owner[v] == 0 else [-1] for v in range(n)]):
        k = sbsteps(g, list(st), E); worst[n] = max(worst.get(n, 0), k)
        if k > n - 1: over.append((n, k, pg.dumps(g)))
print("max switch-best steps over all starts, by n:", dict(sorted(worst.items())), "; runs with steps > n-1:", len(over))
if over: print(over[0])
