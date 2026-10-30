#!/usr/bin/env python3
"""L-SI box 51b §13 (Lead 16:36Z; L-RED R143 Lemma SETTLE): heads at state k: HD_k := {sbar_k(g) : g in D_k} (deviation targets) and
{sigma_k(c) : Even c with lambda_W(c) = c} (successors of W-cycle nodes). In every W-run F (as retx.py), per vertex h: HX_F(h) := the
transitions k -> k+1 of F with h in HD_k and Xi(h) changing; XX_F(h) := all transitions of F changing Xi(h). Prints maxima over (F, h)
of HX and XX, the max over F of the number of distinct heads, of sum_h HX_F(h), and the longest W-run.
Usage: heads.py GAME.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "new", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
a = sys.argv[1:]; g = load(a[0]); n = g.n; own = g.owner
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, readstart(a[1]) if len(a) > 1 else None)
S, TAU, FB = [tuple(s)], [tuple(t)], []
while True:
    r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
    if r is None: break
    S.append(tuple(r[0])); TAU.append(tuple(r[1])); FB.append(r[4])
T = len(S) - 1; EV = [E.evaluate(x) for x in S]; XK = [[E.key(y) for y in e[0]] for e in EV]
Wc = {}
def Wv(k, tau):
    if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(own), [[tau[v]] if own[v] == 1 else g.succ[v] for v in range(n)]))
    return Wc[tau].evaluate(S[k])[0]
runs, cur = [], None
for k in range(T):
    ok = TAU[k + 1] == TAU[k] and not FB[k] and S[k + 1] != S[k] and [x[0] for x in Wv(k, TAU[k])] == [x[0] for x in Wv(k + 1, TAU[k])]
    if not ok: cur = None; continue
    if cur is None: cur = [k, k]; runs.append(cur)
    cur[1] = k + 1
c = dict(HX=0, XX=0, NHEAD=0, SUMHX=0, LMAX=0, HXV='-')
for p, q in runs:
    c['LMAX'] = max(c['LMAX'], q - p); hx, xx, heads = {}, {}, set()
    for k in range(p, q):
        sb = EV[k][1]; W = Wv(k, TAU[k])
        hd = {sb[o] for o in range(n) if own[o] == 1 and sb[o] != TAU[k][o]} | {S[k][x] for x in range(n) if own[x] == 0 and W[x][0] == x}
        heads |= hd
        for h in range(n):
            if XK[k + 1][h] != XK[k][h]:
                xx[h] = xx.get(h, 0) + 1
                if h in hd: hx[h] = hx.get(h, 0) + 1
    if hx and max(hx.values()) > c['HX']: c['HX'] = max(hx.values()); c['HXV'] = max(hx, key=hx.get)
    c['XX'] = max([c['XX']] + list(xx.values())); c['NHEAD'] = max(c['NHEAD'], len(heads)); c['SUMHX'] = max(c['SUMHX'], sum(hx.values()))
print(f"HEADS {os.path.basename(a[0])} n {n} " + " ".join(f"{k} {v}" for k, v in c.items()))
