#!/usr/bin/env python3
"""Box 22: o-acyclic C^1O games. X = vertices with no path to o (L-RED R58 §9), Y = the rest. Along the canonical N5 run (or from a
start file) measure the longest block of consecutive iterations in which σ|X does not change (a 'pure-Y block': θ, w and all X
values are frozen), and compare with |Y|. Usage: pureY.py --random N nmin nmax seed | pureY.py game.pg [start]"""
import sys, os, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "box21"))
from n5x import *
def split(g, o):
    n = g.n; pred = [[] for _ in range(n)]
    for v in range(n):
        for w in g.succ[v]: pred[w].append(v)
    Y = {o}; stack = [o]
    while stack:
        x = stack.pop()
        for y in pred[x]:
            if y not in Y: Y.add(y); stack.append(y)
    return Y
def blocks(g, st, o):
    Y = split(g, o); X = [v for v in range(g.n) if v not in Y and g.owner[v] == 0]
    best = cur = 0
    for k in range(1, len(st)):
        same = all(st[k][0][v] == st[k - 1][0][v] for v in X)
        cur = cur + 1 if same else 0; best = max(best, cur)
    return best, len(Y), Y
if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] == "--random":
        N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed); worst = (-99, None); cnt = 0
        for i in range(N):
            n = rng.randint(lo, hi); owner = [0] * n; o = rng.randrange(n); owner[o] = 1
            succ = [sorted(set(rng.sample(range(n), rng.choice((1, 2, 2, 3))))) for _ in range(n)]
            succ[o] = sorted(set(rng.sample(range(n), rng.choice((2, 3)))))
            g = pg.Game([rng.randrange(n + 3) for _ in range(n)], owner, succ)
            Yset = split(g, o)
            if any(w in Yset for w in succ[o]): continue          # o on a cycle: not o-acyclic
            cnt += 1; st, _ = trace(g, check=False); b, ny, _ = blocks(g, st, o)
            if b - ny > worst[0]: worst = (b - ny, (i, n, b, ny, len(st) - 1))
        print(f"o-acyclic games {cnt}: worst (longest pure-Y block - |Y|) = {worst}")
    else:
        g = load(a[0]); st0 = readstart(a[1]) if len(a) > 1 else None
        o = [v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) > 1][0]; st, _ = trace(g, st0)
        b, ny, Y = blocks(g, st, o); print(f"{a[0]}: iterations {len(st)-1}, |Y| = {ny}, longest pure-Y block {b}, o-acyclic = {not any(w in Y for w in g.succ[o])}")
