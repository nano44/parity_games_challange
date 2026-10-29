#!/usr/bin/env python3
"""L-RED successor 30: DONE-set profile of N5 tau-stretches (R119 §2). In a stretch with tau fixed, W_k(v) := value of v under
(sigma_k, tau); Xi_tau(v) := value under (T, tau), T = tau-bar. v is DONE at k iff W_k(v) = Xi_tau(v). Prints, per stretch of
length >= 2: length, |DONE| at start and end, number of steps that add a DONE vertex, and asserts DONE never shrinks inside a stretch
and W_k never decreases (in SPEC S1's order). Usage: done.py GAME.pg [START]"""
import sys, os
R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
sys.path.insert(0, R + "/experiments/n5-second"); sys.path.insert(0, R + "/experiments/hard-families"); sys.path.insert(0, R + "/experiments/harness")
import n5b, pg
from mgcheck import playval

g = pg.read(sys.argv[1]); s0, t0 = n5b.read_start(sys.argv[2], g) if len(sys.argv) > 2 else (None, None)
N = n5b.N5(g, mode="spec"); tr = []; N.run(s0, t0, trace=tr)
rank = {v: r for r, v in enumerate(sorted(range(g.n), key=lambda v: (g.prio[v], v)))}
SG = N.SG
def W(sig, tau):
    f = lambda x: sig[x] if g.owner[x] == 0 else tau[x]
    return [playval(g, f, u, rank)[0] for u in range(g.n)]
i = 0; rows = []
while i < len(tr):
    j = i
    while j + 1 < len(tr) and tr[j + 1][1] == tr[i][1]: j += 1
    tau = list(tr[i][1]); vt, tbd = N.opt(N.SD, tau)
    T = [tbd[v] if g.owner[v] == 0 else -1 for v in range(g.n)]
    X = W(T, tau); prev = None; adds = 0; sizes = []
    for k in range(i, j + 1):
        w = W(list(tr[k][0]), tau); d = {v for v in range(g.n) if w[v] == X[v]}
        if prev is not None:
            pw, pd = prev
            assert pd <= d, ("DONE shrank", k)
            assert all(SG.nvo(pw[v], w[v]) <= 0 for v in range(g.n)), ("W decreased", k)
            if d - pd: adds += 1
        prev = (w, d); sizes.append(len(d))
    if j - i >= 2: rows.append((i, j - i, sizes[0], sizes[-1], adds))
    i = j + 1
print(f"{sys.argv[1]} n {g.n} states {len(tr)} stretches>=2 {len(rows)}")
for r in sorted(rows, key=lambda r: -r[1])[:5]:
    print(f"  start {r[0]} length {r[1]} DONE {r[2]} -> {r[3]} (of {g.n}) adding-steps {r[4]}")
