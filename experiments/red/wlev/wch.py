#!/usr/bin/env python3
"""L-RED R154: per-vertex W-changes in one W-run (n5b SPEC; W as red/xcn/xcn.py). For the longest W-run F prints |F|, the max over v of
WCH_F(v) (transitions of F at which W(v) changes), its vertex, and the max over Even v of the number of W-ORDER FLIPS between two
successors a, b of v (times the strict W-order of W(a), W(b) reverses inside F): the ladder bottom of R148 §3 needs both rails to
leapfrog in W. Usage: wch.py GAME.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "xcn"))
import xcn, n5b
pg = xcn.pg
g = pg.read(sys.argv[1]); st = n5b.read_start(sys.argv[2], g) if len(sys.argv) > 2 else (None, None)
tr, fb = xcn.trace(g, *st); runs, W = xcn.wruns(g, tr, fb); F = max(runs, key=len); t = tr[F[0]][1]; SG = n5b.SpecSI(g)
Ws = [W(tr[k][0], t) for k in F]
wch = [sum(Ws[i][v] != Ws[i - 1][v] for i in range(1, len(F))) for v in range(g.n)]
v0 = max(range(g.n), key=lambda v: wch[v])
best = (0, None)
for v in range(g.n):
    if g.owner[v] != 0: continue
    s = sorted(set(g.succ[v]))
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            a, b = s[i], s[j]; last = 0; fl = 0
            for Wk in Ws:
                if Wk[a][0] != Wk[b][0]: continue
                c = SG.nvo(Wk[a], Wk[b]); sg = (c > 0) - (c < 0)
                if sg and last and sg != last: fl += 1
                if sg: last = sg
            if fl > best[0]: best = (fl, (v, a, b))
print(f"WCH {os.path.basename(sys.argv[1])} n {g.n} |F| {len(F) - 1} maxWCH {wch[v0]} (v {v0}, owner {g.owner[v0]}) maxWflip {best[0]} {best[1]}")
