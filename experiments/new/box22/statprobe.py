#!/usr/bin/env python3
"""Box 24 (STAT) probe: o-acyclic C^1O games, canonical N5. In pure-Y blocks (σ|X and τ fixed) with θ ◁ w strictly, record per
Even Y-vertex: F->O entries, O->F exits (R = o's σ-reach set), and the block length, plus the number of iterations per block
whose step changes some vertex's type. Usage: statprobe.py --random N nmin nmax seed | statprobe.py game.pg"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "box21"))
from n5x import *
from h1 import wvals
from lemmaG import reach
from pureY import split
def probe(g, st):
    n = g.n; o = [v for v in range(n) if g.owner[v] == 1 and len(g.succ[v]) > 1][0]; E = Engine(g)
    Y = split(g, o); X = [v for v in range(n) if v not in Y and g.owner[v] == 0]; YE = [v for v in Y if g.owner[v] == 0]
    out = []; k = 1
    while k < len(st):
        # extend a block from state k-1
        j = k
        while j < len(st) and all(st[j][0][v] == st[k - 1][0][v] for v in X) and st[j][1] == st[k - 1][1]: j += 1
        blk = list(range(k - 1, j))                      # states in the block
        if len(blk) >= 2:
            s0, t0 = st[blk[0]]; X0, _ = E.evaluate(s0); _, W0 = wvals(g, s0, t0)
            strict = E.key(X0[o]) < E.key(W0[o])
            types = [reach(g, st[i][0], o) for i in blk]
            ent = {v: 0 for v in YE}; ext = {v: 0 for v in YE}
            for a, b in zip(types, types[1:]):
                for v in YE:
                    if v not in a and v in b: ent[v] += 1
                    if v in a and v not in b: ext[v] += 1
            out.append((len(blk) - 1, strict, max(ent.values(), default=0), max(ext.values(), default=0), len(YE)))
        k = j + 1 if j > k else k + 1
    return out
if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] == "--random":
        N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed); agg = []
        for i in range(N):
            n = rng.randint(lo, hi); owner = [0] * n; o = rng.randrange(n); owner[o] = 1
            succ = [sorted(set(rng.sample(range(n), rng.choice((1, 2, 2, 3))))) for _ in range(n)]
            succ[o] = sorted(set(rng.sample(range(n), rng.choice((2, 3)))))
            g = pg.Game([rng.randrange(n + 3) for _ in range(n)], owner, succ); Yset = split(g, o)
            if any(w in Yset for w in succ[o]): continue
            st, _ = trace(g, check=False); agg += [(i,) + r for r in probe(g, st)]
        s = [r for r in agg if r[2]]
        print(f"blocks {len(agg)}, strict (θ◁w) blocks {len(s)}; max block len strict {max((r[1] for r in s), default=0)}; "
              f"max entries/vertex {max((r[3] for r in s), default=0)}; max exits/vertex {max((r[4] for r in s), default=0)}")
        for r in sorted(s, key=lambda r: -r[1])[:5]: print("  ", r)
    else:
        g = load(a[0]); st, _ = trace(g); print(probe(g, st))
