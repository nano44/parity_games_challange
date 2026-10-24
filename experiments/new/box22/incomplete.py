#!/usr/bin/env python3
"""Box 24, C^1O (o-cyclic allowed): at every state k with a PURE outgoing transition and θ ◁ w, check Lemma 2':
a := σ̄(o) lies in Y (has a path to o) and is INCOMPLETE: Ξ_k(a) ◁ U_τ(a) (U = Odd's honest dual value of a, read in G's order).
Also report, per run, how many exits are incomplete over time. Usage: incomplete.py --random N nmin nmax seed | incomplete.py game.pg"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "box21"))
from n5x import *
from h1 import wvals
from pureY import split
def run(g, st, cnt, verbose=False):
    n = g.n; o = [v for v in range(n) if g.owner[v] == 1 and len(g.succ[v]) > 1][0]; E, Ed = Engine(g), Engine(dual(g))
    Y = split(g, o); X = [v for v in range(n) if v not in Y and g.owner[v] == 0]
    for k in range(len(st) - 1):
        s, t = st[k]; Xi, sb = E.evaluate(s); _, W = wvals(g, s, t); U, _ = Ed.evaluate(t)
        inc = [e for e in g.succ[o] if E.key(Xi[e]) < E.key(U[e])]
        if verbose: print(f"state {k}: θ◁w={E.key(Xi[o]) < E.key(W[o])} σ̄(o)={sb[o]} incomplete exits={inc}")
        pure = all(st[k + 1][0][v] == st[k][0][v] for v in X) and st[k + 1][1] == st[k][1]
        if pure and E.key(Xi[o]) < E.key(W[o]):
            cnt["pure_strict"] += 1; a = sb[o]
            if a not in Y: cnt["a_in_X"] += 1
            if not E.key(Xi[a]) < E.key(U[a]): cnt["a_complete"] += 1
if __name__ == "__main__":
    a = sys.argv[1:]; cnt = {"pure_strict": 0, "a_in_X": 0, "a_complete": 0, "games": 0}
    if a[0] == "--random":
        N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        for i in range(N):
            n = rng.randint(lo, hi); owner = [0] * n; o = rng.randrange(n); owner[o] = 1
            succ = [sorted(set(rng.sample(range(n), rng.choice((1, 2, 2, 3))))) for _ in range(n)]
            succ[o] = sorted(set(rng.sample(range(n), rng.choice((2, 3)))))
            g = pg.Game([rng.randrange(n + 3) for _ in range(n)], owner, succ); cnt["games"] += 1
            st, _ = trace(g, check=False); run(g, st, cnt)
    else:
        g = load(a[0]); st, _ = trace(g); cnt["games"] = 1; run(g, st, cnt, verbose=True)
    print(cnt)
