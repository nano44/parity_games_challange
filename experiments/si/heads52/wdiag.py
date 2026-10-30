#!/usr/bin/env python3
"""L-SI box 52 diagnostic (rwin.py's windows): per event-free window of a W-run, SWW = most switches of one Even vertex, XWW = most
Xi-changes of one vertex, WCW = W-changing transitions, LEN = window length. Prints the per-game maxima and the window shape of the
longest window.  Usage: wdiag.py GAME.pg [START]"""
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
best = dict(LEN=0, SWW=0, XWW=0, WCW=0); shape = None
for p, q in runs:
    tau = TAU[p]; C = {x for x in range(n) if Wv(p, tau)[x][0] == x}
    def U(k):
        sb = EV[k][1]
        return {sb[o] for o in range(n) if own[o] == 1 and sb[o] != tau[o]} | {(S[k][x] if own[x] == 0 else sb[x]) for x in C}
    wins, curw = [], []
    for k in range(p, q):
        ev = EV[k][1] != EV[k + 1][1] or any(S[k][x] != S[k + 1][x] for x in C if own[x] == 0) or \
             any(XK[k][u] != XK[k + 1][u] for u in U(k) | U(k + 1))
        if ev:
            if curw: wins.append(curw)
            curw = []
        else: curw.append(k)
    if curw: wins.append(curw)
    for w in wins:
        sw, xc, wc = {}, {}, 0
        for k in w:
            for v in range(n):
                if own[v] == 0 and S[k][v] != S[k + 1][v]: sw[v] = sw.get(v, 0) + 1
                if XK[k][v] != XK[k + 1][v]: xc[v] = xc.get(v, 0) + 1
            wc += Wv(k, tau) != Wv(k + 1, tau)
        best['SWW'] = max(best['SWW'], max(sw.values()) if sw else 0); best['XWW'] = max(best['XWW'], max(xc.values()) if xc else 0)
        if len(w) > best['LEN']:
            best['LEN'] = len(w); best['WCW'] = wc
            shape = [sorted(v for v in range(n) if own[v] == 0 and S[k][v] != S[k + 1][v]) for k in w]
print(f"WDIAG {os.path.basename(a[0])} n {n} " + " ".join(f"{k} {v}" for k, v in best.items()))
print("SHAPE", shape)
