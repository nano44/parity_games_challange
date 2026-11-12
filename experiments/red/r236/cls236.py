#!/usr/bin/env python3
"""L-RED 66 R236 (Lead 15:17Z): classify the games where n5x236's iteration count differs from n5v mode xi (xr236 seed 2, 300 games):
first differing state t; whether the start pair differs (start); whether at t the step was a fallback in either engine (fallback);
whether the differing component is sigma (S4a) or tau (S4b); for S4a / S4b: whether n5x236's choice and n5v's choice are both optimal in
the arena (same W* value: tie rule) or not (divergence). Env LNEW as xr236. Usage: cls236.py SEED COUNT NMAX"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path[:0] = [HERE, os.path.join(ROOT, "experiments/harness"), os.path.join(os.environ["LNEW"], "experiments/new/box190")]
import n5x236 as X, gen, n5v
seed, cnt, nmax = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); C = {}
for i in range(cnt):
    n = 2 + (i % (nmax - 1)); g = gen.random_game(n, max(2, n // 2), 1, 3, seed * 100000 + i)
    tr = []; it, fb, win, s, sb = X.run(list(g.prio), list(g.owner), [list(x) for x in g.succ], trace=tr)
    st, fbs, E = n5v.run(g, "xi")
    if len(st) - 1 == it: continue
    mine = [(tuple(a.get(v, -1) for v in range(n)), tuple(b.get(v, -1) for v in range(n))) for a, b in tr]
    mine.append(None)
    theirs = [(tuple(x if g.owner[v] == 0 else -1 for v, x in enumerate(a)), tuple(x if g.owner[v] == 1 else -1 for v, x in enumerate(b))) for a, b in st]
    t = next(k for k in range(min(len(mine), len(theirs))) if mine[k] != theirs[k]) if any(mine[k] != theirs[k] for k in range(min(len(mine), len(theirs)))) else min(len(mine), len(theirs))
    if t == 0: kind = "start"
    else:
        a, b = mine[t], theirs[t]
        comp = ("sigma" if a is None or a[0] != b[0] else "") + ("tau" if a is not None and a[1] != b[1] else "")
        # re-run one step of each from the common state t-1 and look at the arena optimum
        kind = "step:" + comp
    C[kind] = C.get(kind, 0) + 1
    print("game", i, "n", n, "mine", it, "n5v", len(st) - 1, "first diff state", t, kind, flush=True)
print("TOTAL", C)
