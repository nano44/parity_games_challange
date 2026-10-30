#!/usr/bin/env python3
"""L-SI box 53 (Lead 18:55Z, D18 Topkis angle): is Odd's reply sbar monotone in some FIXED partial order while Xi rises inside one
W-run F (as si/heads52/flipc.py: tau fixed, no S4c fallback, sigma moves, lambda_W constant)?
PROFREV: W-runs in which the whole profile sbar returns to an earlier profile after changing (sbar_a = sbar_b != sbar_(a+1), a < b).
  One such run kills every fixed partial order (antisymmetry). PVREV: the most returns of one sbar(o) to a successor it held earlier
  in F (kills every order whose restriction to o is a fixed order on succ(o), e.g. products of chains). FIRST: the first PROFREV
  witness (a, b, k-range). ROOT-FLIP (the box-52 reading, measured): ROOTX = transitions with a sbar-flip at which NO flipping Odd o is
  its own Xi-cycle node (at k or k+1) and NO flipping o has Xi of its old target sbar_k(o) changed. EVX2: transitions with a sbar-flip,
  no CN switch, no own-node flip and no Xi-change on U_k u U_(k+1) u tau(Odd). TXR: the most Xi-changes of one tau(o) (o Odd) in one F.
Usage: topkis.py GAME.pg [START]"""
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
c = dict(RUNS=len(runs), PROFREV=0, PVREV=0, FLIPT=0, ROOTX=0, EVX2=0, TXR=0)
first = None
for p, q in runs:
    tau = TAU[p]; C = {v for v in range(n) if Wv(p, tau)[v][0] == v}
    seen = {}; pv = {}; held = {o: {EV[p][1][o]} for o in ODD}; txr = {}
    prof = tuple(EV[p][1][o] for o in ODD); seen[prof] = p; rev = False
    for k in range(p, q):
        sb0, sb1 = EV[k][1], EV[k + 1][1]
        fl = [o for o in ODD if sb0[o] != sb1[o]]
        for o in ODD:
            w = tau[o]
            if XK[k][w] != XK[k + 1][w]: txr[o] = txr.get(o, 0) + 1
        if fl:
            c['FLIPT'] += 1
            ownf = [o for o in fl if EV[k][0][o][0] == o or EV[k + 1][0][o][0] == o]
            oldx = [o for o in fl if XK[k][sb0[o]] != XK[k + 1][sb0[o]]]
            if not ownf and not oldx: c['ROOTX'] += 1
            U = {sb0[o] for o in ODD if sb0[o] != tau[o]} | {sb1[o] for o in ODD if sb1[o] != tau[o]} | {tau[o] for o in ODD}
            cn = any(S[k][v] != S[k + 1][v] for v in C if own[v] == 0)
            if not ownf and not cn and not any(XK[k][w] != XK[k + 1][w] for w in U): c['EVX2'] += 1
            for o in fl:
                if sb1[o] in held[o]: pv[o] = pv.get(o, 0) + 1
                held[o].add(sb1[o])
            prof = tuple(sb1[o] for o in ODD)
            if prof in seen and not rev:
                rev = True; c['PROFREV'] += 1
                if first is None: first = (seen[prof], k + 1, p, q)
            seen.setdefault(prof, k + 1)
    if pv: c['PVREV'] = max(c['PVREV'], max(pv.values()))
    if txr: c['TXR'] = max(c['TXR'], max(txr.values()))
print(f"TOPKIS {os.path.basename(a[0])} n {n} " + " ".join(f"{k} {v}" for k, v in c.items()) + (f" FIRST {first[0]} {first[1]} F {first[2]} {first[3]}" if first else ""))
