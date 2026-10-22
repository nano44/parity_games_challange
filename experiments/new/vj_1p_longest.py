#!/usr/bin/env python3
"""Box 7: check VJ00 Prop. 7.4 (O(n^3) improvement steps on one-player parity games, stated without proof in BRICS RS-00-48 §7)
by computer. On random ONE-PLAYER games (every Odd vertex has out-degree 1; Even = the improver), compute the LONGEST improvement
sequence over ALL policies: the longest path in the DAG σ -> Switch_I(σ), I any non-empty unambiguous set of improvements
(si.py Engine valuations = VJ00 Ω, cross-checked by REFEREE-2 R2-N5T §5). Usage: vj_1p_longest.py games seed nmin nmax"""
import sys, os, random, itertools, functools
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from n5 import pg, Engine
sys.setrecursionlimit(100000)
games, seed, nmin, nmax = map(int, sys.argv[1:5]); rng = random.Random(seed); worst = {}
for _ in range(games):
    n = rng.randint(nmin, nmax); prio = [rng.randrange(2 * n) for _ in range(n)]; owner = [rng.randrange(2) for _ in range(n)]
    succ = [sorted(set(rng.randrange(n) for _ in range(rng.randint(1, 3)))) if owner[v] == 0 else [rng.randrange(n)] for v in range(n)]
    g = pg.Game(prio, owner, succ); E = Engine(g)
    @functools.lru_cache(maxsize=None)
    def longest(s):
        vs, _ = E.evaluate(s); I = E.improving(s, vs)
        if not I: return 0
        byv = {}
        for v, w in I: byv.setdefault(v, []).append(w)
        vsl = list(byv); best = 0
        for choice in itertools.product(*[[None] + byv[v] for v in vsl]):
            if all(c is None for c in choice): continue
            t = list(s)
            for v, c in zip(vsl, choice):
                if c is not None: t[v] = c
            best = max(best, 1 + longest(tuple(t)))
        return best
    L = max(longest(tuple(st)) for st in itertools.islice(itertools.product(*[succ[v] if owner[v] == 0 else [-1] for v in range(n)]), 2000))
    worst[n] = max(worst.get(n, 0), L)
print(f"games={games} seed={seed}: longest improvement sequence over all policies and all starts, by n:", dict(sorted(worst.items())))
