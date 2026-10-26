#!/usr/bin/env python3
"""L-SI succ. 5, box 10b: DATA for Lemma P1 (docs/si/N5-P1-box10.md): in a one-player game (every Odd vertex has out-degree 1), an Even
positional strategy with no improving edge has a valuation that dominates every Even positional strategy, pointwise. Exhaustive over all
Even positional strategies of random one-player games (engine: experiments/si/si.py valuations, read-only).
Usage: p1check.py NGAMES nmin nmax seed"""
import sys, os, random, itertools
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..")); sys.path.insert(0, os.path.join(HERE, "..", "..", "harness"))
import pg
from si import Engine

def main(N, nmin, nmax, seed):
    rng = random.Random(seed); C = {"games": 0, "strats": 0, "noimp": 0, "viol": 0, "nonopt_has_imp": 0}
    for _ in range(N):
        n = rng.randint(nmin, nmax)
        prio = [rng.randrange(n + 1) for _ in range(n)]; owner = [rng.randrange(2) for _ in range(n)]
        succ = [sorted(set(rng.sample(range(n), rng.choice((1, 2, 2, 3))))) if owner[v] == 0 else [rng.randrange(n)] for v in range(n)]
        assert all(len(set(succ[v])) == 1 for v in range(n) if owner[v] == 1)          # one-player: Odd out-degree 1
        g = pg.Game(prio, owner, succ); E = Engine(g); C["games"] += 1
        ev = [v for v in range(n) if owner[v] == 0]
        strats = []
        for ch in itertools.product(*[succ[v] for v in ev]):
            s = [-1] * n
            for v, w in zip(ev, ch): s[v] = w
            vals, _ = E.evaluate(tuple(s)); strats.append((s, vals))
        if len(strats) > 4000: continue
        best = [max(E.key(val[v]) for _, val in strats) for v in range(n)]
        for s, vals in strats:
            C["strats"] += 1
            imp = E.improving(tuple(s), vals)
            opt = all(E.key(vals[v]) == best[v] for v in range(n))
            if not imp:
                C["noimp"] += 1
                if not opt: C["viol"] += 1; print("VIOLATION", prio, owner, succ, s)
            elif not opt: C["nonopt_has_imp"] += 1
    print("TOTAL", C)

if __name__ == "__main__": main(*map(int, sys.argv[1:5]))
