#!/usr/bin/env python3
"""L-SI box 52: sbar-flips inside W-runs (as si/gate/heads.py). For an Odd o with sbar_(k+1)(o) != sbar_k(o) =: h at transition k -> k+1:
OLDX: Xi(h) changes at the transition (Xi_(k+1)(h) != Xi_k(h)); NOX: it does not (a tie-break flip, Xi(h) fixed).
Split by kind: ENT (h = tau(o): o enters D), EXI (new target tau(o): o leaves D), MOV (both != tau(o)). NONE: flips with neither the old nor the new target's Xi changing; ENTX: ENT flips at a transition with no Xi-change at a head
(of U_k u U_(k+1)) among o's successors. PERO: the most flips of one o
in one W-run; PEROX: the most flips of one o in one W-run minus 2 x (Xi-changes of o's successors that are heads at that transition).
Usage: flipc.py GAME.pg [START]"""
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
c = dict(FLIPS=0, OLDX=0, NOX=0, ENT=0, EXI=0, MOV=0, NOXENT=0, NONE=0, ENTX=0, PERO=0, PEROX=-10 ** 9)
for p, q in runs:
    tau = TAU[p]; fl, hc = {}, {}
    for k in range(p, q):
        sb0, sb1 = EV[k][1], EV[k + 1][1]
        U = {sb0[o] for o in range(n) if own[o] == 1 and sb0[o] != tau[o]} | {sb1[o] for o in range(n) if own[o] == 1 and sb1[o] != tau[o]}
        for o in range(n):
            if own[o] != 1: continue
            for w in set(g.succ[o]):
                if w in U and XK[k][w] != XK[k + 1][w]: hc[o] = hc.get(o, 0) + 1
            if sb0[o] == sb1[o]: continue
            h = sb0[o]; c['FLIPS'] += 1; fl[o] = fl.get(o, 0) + 1
            x = XK[k][h] != XK[k + 1][h]; c['OLDX' if x else 'NOX'] += 1
            kind = 'ENT' if h == tau[o] else ('EXI' if sb1[o] == tau[o] else 'MOV'); c[kind] += 1
            if not x and kind == 'ENT': c['NOXENT'] += 1
            if not x and XK[k][sb1[o]] == XK[k + 1][sb1[o]]: c['NONE'] += 1
            if kind == 'ENT' and not any(w in U and XK[k][w] != XK[k + 1][w] for w in set(g.succ[o])): c['ENTX'] += 1
    if fl:
        c['PERO'] = max(c['PERO'], max(fl.values())); c['PEROX'] = max(c['PEROX'], max(fl[o] - 2 * hc.get(o, 0) for o in fl))
print(f"FLIPC {os.path.basename(a[0])} n {n} " + " ".join(f"{k} {v}" for k, v in c.items()))
