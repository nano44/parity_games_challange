#!/usr/bin/env python3
"""L-LOWER 11: TOP-ONLY change points. Core = pairs 0..h-1 (h = capped levels of a genome's run, or a target file). For each core mover
x of pairs 0..h-2 and each two consecutive free pre-states a < b of x with different required preferences (pref(s_a) = s_(a+1)(x)),
list the core movers y != x that change at a step in (a, b] (FUEL-DOUBLING / the retrigger rule: some mover of closure(x) must
change there). The point is TOP-ONLY if every such y is in pair h-1. Prints per run: change points, TOP-ONLY points, and the
slack steps (o(h-1) unchanged). Usage: topstarve.py (G GENOME | T TARGET | C CORE8FILE GATESGENOME H) ..."""
import sys, os
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(here, '../l6')); sys.path.insert(0, here)
from sim6 import rd, run, Fprof, caps, okeys
from tsat import rdtarget
def analyse(LS, g, h, name):
    K = 2 * h; T = len(LS) - 1; O = [okeys({'d': h, 'gate': g}, list(s)) for s in LS]
    slack = sum(1 for t in range(1, T + 1) if O[t][h - 1] == O[t - 1][h - 1]); pts = top = 0; byx = {}
    for x in range(K - 2):
        l = x // 2; req = []
        for t in range(1, T + 1):
            s = LS[t - 1]; free = (g[2 * x + 1 - s[x]] < g[2 * x + s[x]]) if l == 0 else (s[x] != O[t][l - 1])
            if free: req.append((t - 1, LS[t][x]))
        for (a, p), (b, q) in zip(req, req[1:]):
            if p == q: continue
            ys = [y for y in range(K) if y != x and any(LS[u][y] != LS[u - 1][y] for u in range(a + 1, b + 1))]
            pts += 1
            if ys and all(y >= K - 2 for y in ys): top += 1; byx[x] = byx.get(x, 0) + 1
    print(f'{name}: h {h} T {T} slack {slack} | lower change points {pts}, TOP-ONLY {top} ({100 * top / max(pts, 1):.0f}%) by mover {byx}')
args = sys.argv[1:]; i = 0
while i < len(args):
    k = args[i]
    if k == 'G':
        D = rd(args[i + 1]); S, O = run(D); h = caps(Fprof(D, O)); analyse([s[:2 * h] for s in S], D['gate'][:4 * h], h, os.path.basename(args[i + 1])); i += 2
    elif k == 'T':
        LS, g = rdtarget(args[i + 1]); analyse(LS, g, len(g) // 4, os.path.basename(args[i + 1])); i += 2
    else:
        rows = open(args[i + 1]).read().split(); n1, K = int(rows[0]), int(rows[1]); LS = [tuple(int(ch) for ch in r) for r in rows[2:2 + n1]]
        D = rd(args[i + 2]); h = int(args[i + 3]); g = list(D['gate'][:4 * (h - 1)]) + [4 * (h - 1) + 1000 + k for k in range(4)]
        analyse(LS, g, h, os.path.basename(args[i + 1])); i += 4
