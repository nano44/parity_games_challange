#!/usr/bin/env python3
"""Box 24 checks of the (STAT) argument on o-acyclic C^1O games (canonical N5 runs):
 (L1) at every state k whose transition k -> k+1 leaves σ|X and τ unchanged ("pure"): θ_k = w_k, i.e. Ξ(o) = W(o);
 (L2) at such states Ξ = W at every vertex (so Iσ = the improving set of the one-player game G_τ);
 (L3) every maximal pure block equals the N5 run on the one-player game G_τ (Odd fixed to τ) from the block's first σ,
      for as many steps as the block has.  Usage: statcheck.py --random N nmin nmax seed [--randstart] | statcheck.py game.pg ..."""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "box21"))
from n5x import *
from h1 import wvals
from pureY import split
def onegame(g, tau):
    return pg.Game(list(g.prio), list(g.owner), [list(g.succ[v]) if g.owner[v] == 0 else [tau[v]] for v in range(g.n)])
def check(g, st, cnt):
    n = g.n; o = [v for v in range(n) if g.owner[v] == 1 and len(g.succ[v]) > 1][0]; E = Engine(g)
    Y = split(g, o); X = [v for v in range(n) if v not in Y and g.owner[v] == 0]
    pure = [all(st[k + 1][0][v] == st[k][0][v] for v in X) and st[k + 1][1] == st[k][1] for k in range(len(st) - 1)]
    for k in range(len(st) - 1):
        if not pure[k]: continue
        s, t = st[k]; Xi, _ = E.evaluate(s); _, W = wvals(g, s, t); cnt["pure"] += 1
        if Xi[o] != W[o]: cnt["L1_fail"] += 1
        if Xi != W: cnt["L2_fail"] += 1
    k = 0
    while k < len(st) - 1:
        if not pure[k]: k += 1; continue
        j = k
        while j < len(st) - 1 and pure[j]: j += 1          # transitions k..j-1 pure
        h = onegame(g, st[k][1]); s0 = st[k][0]
        hs, _ = trace(h, ({v: s0[v] for v in range(n) if h.owner[v] == 0}, {}), check=False)
        cnt["blocks"] += 1; cnt["maxblock"] = max(cnt["maxblock"], j - k)
        if [x[0] for x in hs[: j - k + 1]] != [x[0] for x in st[k: j + 1]]: cnt["L3_fail"] += 1
        k = j
if __name__ == "__main__":
    RS = "--randstart" in sys.argv
    if RS: sys.argv.remove("--randstart")
    cnt = {"pure": 0, "L1_fail": 0, "L2_fail": 0, "blocks": 0, "L3_fail": 0, "maxblock": 0, "games": 0}
    a = sys.argv[1:]
    if a[0] == "--random":
        N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        for i in range(N):
            n = rng.randint(lo, hi); owner = [0] * n; o = rng.randrange(n); owner[o] = 1
            for v in range(n):
                if v != o and rng.random() < 0.15: owner[v] = 1          # forced Odd vertices (out-degree 1 below)
            succ = [sorted(set(rng.sample(range(n), rng.choice((1, 2, 2, 3))))) for _ in range(n)]
            for v in range(n):
                if owner[v] == 1 and v != o: succ[v] = succ[v][:1]
            succ[o] = sorted(set(rng.sample(range(n), rng.choice((2, 3)))))
            g = pg.Game([rng.randrange(n + 3) for _ in range(n)], owner, succ); Ys = split(g, o)
            if any(w in Ys for w in succ[o]): continue
            start = None
            if RS:
                start = ({v: rng.choice(succ[v]) for v in range(n) if owner[v] == 0}, {o: rng.choice(succ[o])})
            cnt["games"] += 1; st, _ = trace(g, start, check=False); check(g, st, cnt)
    else:
        for p in a:
            g = load(p); st, _ = trace(g); cnt["games"] += 1; check(g, st, cnt)
    print(cnt)
