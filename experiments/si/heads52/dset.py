#!/usr/bin/env python3
"""L-SI box 52 (Lead 16:59Z): the deviation ("defect") set D_k = {Odd o : sbar_k(o) != tau(o)} inside one W-run F (as si/gate/heads.py:
tau fixed, no S4c fallback, sigma moves, lambda_W constant). Per (F, o): ENT entries of o into D, EXT exits, REN re-entries (an entry
after an exit inside F), SBF sbar(o)-changes. Per deviation edge (g, h = sbar(g)) at a state: INIT whether (g, h) is in I_tau, and
the dual comparison of W*(h) with W*(tau g) (W* = Xi^U, the dual valuation of tau, constant on F): WSB h strictly better for Odd,
WSE equal, WSW strictly worse for Odd. Prints maxima / totals.  Usage: dset.py GAME.pg [START]"""
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
T = len(S) - 1; EV = [E.evaluate(x) for x in S]
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
c = dict(RUNS=len(runs), LMAX=0, DMAX=0, ENT=0, EXT=0, REN=0, SBF=0, SUMREN=0, INIT=0, WSB=0, WSE=0, WSW=0, DEVS=0)
for p, q in runs:
    c['LMAX'] = max(c['LMAX'], q - p); tau = TAU[p]
    vt, _ = Ed.evaluate(tau); It = set(Ed.improving(tau, vt))
    ent, ext, ren, sbf, left = {}, {}, {}, {}, set()
    prevD, prevsb = None, None
    for k in range(p, q + 1):
        sb = EV[k][1]; D = {o for o in range(n) if own[o] == 1 and sb[o] != tau[o]}
        c['DMAX'] = max(c['DMAX'], len(D))
        for o in D:
            h = sb[o]; c['DEVS'] += 1
            if (o, h) in It: c['INIT'] += 1
            kh, kt = Ed.key(vt[h]), Ed.key(vt[tau[o]])
            if kh > kt: c['WSB'] += 1
            elif kh == kt: c['WSE'] += 1
            else: c['WSW'] += 1
        if prevD is not None:
            for o in D - prevD:
                ent[o] = ent.get(o, 0) + 1
                if o in left: ren[o] = ren.get(o, 0) + 1
            for o in prevD - D: ext[o] = ext.get(o, 0) + 1; left.add(o)
            for o in range(n):
                if own[o] == 1 and sb[o] != prevsb[o]: sbf[o] = sbf.get(o, 0) + 1
        prevD, prevsb = D, sb
    for key, d in (('ENT', ent), ('EXT', ext), ('REN', ren), ('SBF', sbf)):
        if d: c[key] = max(c[key], max(d.values()))
    c['SUMREN'] += sum(ren.values())
print(f"DSET {os.path.basename(a[0])} n {n} " + " ".join(f"{k} {v}" for k, v in c.items()))
