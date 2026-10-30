#!/usr/bin/env python3
"""L-SI box 53 (Lead 20:00Z, T60 §3.3): is a sbar-flip always accompanied by a change of the weak Xi-ORDER on the heads?
Inside W-runs (as topkis.py). For a transition k -> k+1 of F with a sbar-flip, no own-node flip and no CN switch, H := U'_k u U'_(k+1)
(U' := U u tau(Odd)), resp. H0 := U_k u U_(k+1); the weak order of Xi on H is the sign of every pair comparison.
ORDX: such transitions with the weak order on H unchanged; ORDX0: with the weak order on H0 unchanged. PAIRTIE: such transitions whose
root flips (non-own, old target's Xi changed) all have t1, t2 tied at k AND at k+1 (the gap in ROOT-FLIP => order change).
UMAX: max |U_k| over W-run states; UPMAX: max |U'_k|; NORD: the most distinct (sigma-restricted-to-nothing) head orders on U' in one F,
counted as distinct weak orders of Xi on the fixed set U'_p (state p = start of F); RREP: W-runs in which a weak order on U'_p recurs
after a different one (a NO-REPEAT violation for the order alone). Usage: orderchg.py GAME.pg [START]"""
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
ODD = [o for o in range(n) if own[o] == 1]
def sgn(x, y): return (x > y) - (x < y)
def worder(k, H): return tuple(sgn(XK[k][u], XK[k][w]) for i, u in enumerate(H) for w in H[i + 1:])
c = dict(RUNS=len(runs), FT=0, ORDX=0, ORDX0=0, PAIRTIE=0, UMAX=0, UPMAX=0, NORD=0, RREP=0)
for p, q in runs:
    tau = TAU[p]; C = {v for v in range(n) if Wv(p, tau)[v][0] == v}; TO = {tau[o] for o in ODD}
    def U(k):
        sb = EV[k][1]
        return {sb[o] for o in ODD if sb[o] != tau[o]} | {(S[k][x] if own[x] == 0 else sb[x]) for x in C}
    HP = sorted(U(p) | TO); seen, last, rep = set(), None, False
    for k in range(p, q + 1):
        c['UMAX'] = max(c['UMAX'], len(U(k))); c['UPMAX'] = max(c['UPMAX'], len(U(k) | TO))
        o_ = worder(k, HP)
        if o_ != last:
            if o_ in seen: rep = True
            seen.add(o_); last = o_
        if k == q: break
        b0, b1 = EV[k][1], EV[k + 1][1]
        fl = [o for o in ODD if b0[o] != b1[o]]
        if not fl: continue
        if any(EV[k][0][o][0] == o or EV[k + 1][0][o][0] == o for o in fl): continue
        if any(S[k][x] != S[k + 1][x] for x in C if own[x] == 0): continue
        c['FT'] += 1
        H = sorted(U(k) | U(k + 1) | TO); H0 = sorted(U(k) | U(k + 1))
        if worder(k, H) == worder(k + 1, H): c['ORDX'] += 1
        if worder(k, H0) == worder(k + 1, H0): c['ORDX0'] += 1
        roots = [o for o in fl if XK[k][b0[o]] != XK[k + 1][b0[o]]]
        if roots and all(XK[k][b0[o]] == XK[k][b1[o]] and XK[k + 1][b0[o]] == XK[k + 1][b1[o]] for o in roots): c['PAIRTIE'] += 1
    c['NORD'] = max(c['NORD'], len(seen)); c['RREP'] += rep
print(f"ORDCHG {os.path.basename(a[0])} n {n} " + " ".join(f"{k} {v}" for k, v in c.items()))
