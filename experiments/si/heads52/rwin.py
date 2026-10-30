#!/usr/bin/env python3
"""L-SI box 52: L-RED R143's events and windows, taken over a WHOLE W-run F (as si/gate/heads.py), not one W-constant interval.
U_k := {sbar_k(g) : Odd g, sbar_k(g) != tau(g)} u {Xi-successor of c (sigma_k(c) or sbar_k(c)) : lambda_W(c) = c} (R143 §0).
EVENT at k -> k+1: (i) sbar changes, (ii) sigma changes at an Even c with lambda_W(c) = c, (iii) Xi changes at a vertex of U_k u U_(k+1).
A window is a maximal run of event-free transitions. Prints per game: |F| max (LMAX), events E of that run, the longest window WMAX,
WN := WMAX / n, and EI / EII / EIII (transitions with an event of each kind, summed over runs; a transition may count in several).
Usage: rwin.py GAME.pg [START]"""
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
c = dict(LMAX=0, E=0, WMAX=0, WN=0.0, EI=0, EII=0, EIII=0, WALL=0)
for p, q in runs:
    tau = TAU[p]; C = {x for x in range(n) if Wv(p, tau)[x][0] == x}
    def U(k):
        sb = EV[k][1]
        return {sb[o] for o in range(n) if own[o] == 1 and sb[o] != tau[o]} | {(S[k][x] if own[x] == 0 else sb[x]) for x in C}
    ev, w, wmax = 0, 0, 0
    for k in range(p, q):
        e1 = EV[k][1] != EV[k + 1][1]
        e2 = any(S[k][x] != S[k + 1][x] for x in C if own[x] == 0)
        e3 = any(XK[k][u] != XK[k + 1][u] for u in U(k) | U(k + 1))
        c['EI'] += e1; c['EII'] += e2; c['EIII'] += e3
        if e1 or e2 or e3: ev += 1; w = 0
        else: w += 1; wmax = max(wmax, w)
    c['WALL'] = max(c['WALL'], wmax)
    if q - p > c['LMAX']: c['LMAX'] = q - p; c['E'] = ev; c['WMAX'] = wmax
c['WN'] = round(c['WALL'] / n, 3)
print(f"RWIN {os.path.basename(a[0])} n {n} " + " ".join(f"{k} {v}" for k, v in c.items()))
