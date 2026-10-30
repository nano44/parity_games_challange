#!/usr/bin/env python3
"""L-NEW box 89 (BIP-POLY; docs/new/N5-BIP-box89.md). On the frozen-sigmabar stretches of each W-run (sigmabar constant = rho), for every
EVEN release (late adoption (y, z) at t -> t + 1, last block state q, no Odd change on z's rho-play since q; box88/release.py): the LIFTERS
are the Even vertices x on z's (sigma_q, rho)-play with sigma_t(x) != sigma_q(x). Each lifter is located BEFORE the first deviation
(rho(o) != tau(o)) on that play, AFTER it, or the play has NO deviation (impossible by GAP-DEV). Also: is the lifter's own last switch a
release (late adoption) or not; SINGLE/MULTI deviation on the play; DRIVER_W = W(rho(o0)) changed in [q, t] (o0 the first deviation);
DEPTH = release-dependency depth (1 + max depth of the lifters' last switches that were releases); the number of distinct Xi(z) values between q and t; per stretch |S| and releases.
Usage: bipprobe.py GAME.pg [START]"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
g = load(sys.argv[1]); start = readstart(sys.argv[2]) if len(sys.argv) > 2 else None; n = g.n
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); S = [tuple(s)]; TAU = [tuple(t)]; FB = []
while True:
    r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
    if r is None: break
    S.append(tuple(r[0])); TAU.append(tuple(r[1])); FB.append(r[4])
T = len(S) - 1; ev = [v for v in range(n) if g.owner[v] == 0]; od = [v for v in range(n) if g.owner[v] == 1]
EV = [E.evaluate(x) for x in S]
Wc = {}
def Wv(k, tau):
    if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(g.owner), [[tau[v]] if g.owner[v] == 1 else g.succ[v] for v in range(n)]))
    return Wc[tau].evaluate(S[k])[0]
runs = []; cur = None
for k in range(T):
    ok = TAU[k + 1] == TAU[k] and not FB[k] and S[k + 1] != S[k] and [x[0] for x in Wv(k, TAU[k])] == [x[0] for x in Wv(k + 1, TAU[k])]
    if not ok: cur = None; continue
    if cur is None: cur = [k, k]; runs.append(cur)
    cur[1] = k + 1
c = Counter(); mx = dict(stretch=0, rel=0, nvals=0)
for a, b in runs:
    tau = TAU[a]; W = [Wv(q, tau) for q in range(a, b + 1)]
    # frozen stretches: maximal [u, w] inside F with sigmabar constant
    segs = []; u = a
    for q in range(a, b):
        if EV[q + 1][1] != EV[q][1]: segs.append((u, q)); u = q + 1
    segs.append((u, b))
    for (u, w) in segs:
        if w - u < 1: continue
        rho = EV[u][1]; lastblk = {}; rel = 0; relsw = set(); reldepth = {}
        for q in range(u, w):
            xi = EV[q][0]; Is = set(E.improving(S[q], xi))
            for y in ev:
                z = S[q + 1][y]
                if z != S[q][y] and (y, z) in lastblk:
                    rel += 1; relsw.add((y, q)); q0 = lastblk[(y, z)]
                    pl, x = [], z
                    while x not in pl: pl.append(x); x = S[q0][x] if g.owner[x] == 0 else rho[x]
                    devi = [i for i, x in enumerate(pl) if g.owner[x] == 1 and rho[x] != tau[x]]
                    if not devi: c['nodev'] += 1; continue
                    d0 = devi[0]; aa = rho[pl[d0]]
                    c['single_dev' if len(devi) == 1 else 'multi_dev'] += 1
                    c['driver_W' if any(W[k - a][aa] != W[k + 1 - a][aa] for k in range(q0, q)) else 'no_driver_W'] += 1
                    dep = 1 + max([reldepth.get((pl[i], max(k for k in range(q0, q) if S[k + 1][pl[i]] != S[k][pl[i]])), 0)
                                   for i, x in enumerate(pl) if g.owner[x] == 0 and S[q][x] != S[q0][x]] + [0])
                    reldepth[(y, q)] = dep; mx['depth'] = max(mx.get('depth', 0), dep)
                    lif = [i for i, x in enumerate(pl) if g.owner[x] == 0 and S[q][x] != S[q0][x]]
                    if not lif: c['nolifter'] += 1
                    for i in lif:
                        c['lift_before' if i < d0 else 'lift_after'] += 1
                        x = pl[i]; lastsw = max(k for k in range(q0, q) if S[k + 1][x] != S[k][x])
                        c['lifter_is_release' if (x, lastsw) in relsw else 'lifter_plain'] += 1
                    mx['nvals'] = max(mx['nvals'], len({EV[k][0][z] for k in range(q0, q + 1)}))
            for y in ev:
                for z in g.succ[y]:
                    if z != S[q][y] and E.key(W[q - a][z]) > E.key(W[q - a][S[q][y]]) and (y, z) not in Is: lastblk[(y, z)] = q
        mx['stretch'] = max(mx['stretch'], w - u); mx['rel'] = max(mx['rel'], rel)
print(f"BIPPROBE n {n} {dict(c)} maxima {mx}")
