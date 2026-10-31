#!/usr/bin/env python3
"""L-SI box 54: checks for Lemmas OLD-PLAY, ODD-STEP and ODD-ADD (note docs/si/N5-SRC-box54.md §2) inside W-runs (R89 / R97), and
the PROP / PFX split of source events at Odd sources.
  OLD-PLAY: Xi_(k+1)(x) != Xi_k(x)  =>  some Even vertex of x's (sigma_k, sigmabar_k)-lasso switches at k.        (violations: VOLD)
  ODD-STEP: Odd o, Xi_(k+1)(o) != Xi_k(o) and o is not the cycle node of Xi_k(o)  =>  Xi_(k+1)(x) != Xi_k(x) for x := sigmabar_k(o).
                                                                                                                  (violations: VSTEP)
  For an Odd source o (o in D_k u D_(k+1)) whose Xi changes at k, with x := sigmabar_k(o): the OLD PREFIX of x is x's
  (sigma_k, sigmabar_k)-play from x up to (excluding) its first vertex u in D_k u C (u := None if the play closes first).
    PROP: u exists, no Even vertex of the old prefix switches at k, no Odd vertex of it is in D_(k+1), and Xi(u) changes at k.
    PFX : otherwise (an Even switch or a D-entry on the old prefix, or no u).
  ODD-ADD's mechanism predicts: prefix unchanged and u exists  =>  Xi(u) changes (violations: VADD).
Per W-run maxima: HXS (max over Odd sources of Xi-changes while a source), PFX (max over Odd sources of PFX events).
MUT=1 is a control (switches ignored in OLD-PLAY): VOLD must become positive.
Usage: oddadd.py GAME.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "new", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
MUT = os.environ.get('MUT') == '1'   # control: ignore switches in the OLD-PLAY test, so VOLD must bite
g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 else None; n = g.n; own = g.owner
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, st); S, TAU, FB = [tuple(s)], [tuple(t)], []
while True:
    r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
    if r is None: break
    S.append(tuple(r[0])); TAU.append(tuple(r[1])); FB.append(r[4])
Wc, WX, XX = {}, {}, {}
def Wv(k, tau):
    if (k, tau) not in WX:
        if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(own), [[tau[v]] if own[v] == 1 else g.succ[v] for v in range(n)]))
        WX[(k, tau)] = Wc[tau].evaluate(S[k])[0]
    return WX[(k, tau)]
def Xv(k):
    if k not in XX: XX[k] = E.evaluate(S[k])
    return XX[k]
runs = []; cur = None
for k in range(len(S) - 1):
    if TAU[k + 1] != TAU[k] or FB[k] or [x[0] for x in Wv(k, TAU[k])] != [x[0] for x in Wv(k + 1, TAU[k])]:
        cur = None; continue
    if cur is None: cur = []; runs.append(cur)
    cur.append(k)
T = dict(WRUNS=len(runs), XCHALL=0, VOLD=0, ODDCH=0, VSTEP=0, VSTEPB=0, OSRC=0, PROP=0, PFX=0, PFXSW=0, PFXDIN=0, PFXNOU=0, VADD=0, MAXHXS=0, MAXPFX=0)
for run in runs:
    tau = TAU[run[0]]; C = {v for v in range(n) if Wv(run[0], tau)[v][0] == v}
    hx = [0] * n; pf = [0] * n
    for k in run:
        X0, sb0 = Xv(k); X1, sb1 = Xv(k + 1); s0, s1 = S[k], S[k + 1]
        D0 = {o for o in range(n) if own[o] == 1 and sb0[o] != tau[o]}; D1 = {o for o in range(n) if own[o] == 1 and sb1[o] != tau[o]}
        nxt = lambda v: s0[v] if own[v] == 0 else sb0[v]
        for x in range(n):
            if X0[x] == X1[x]: continue
            T['XCHALL'] += 1
            y, seen, sw = x, set(), False
            while y not in seen:
                seen.add(y)
                if own[y] == 0 and s0[y] != s1[y] and not MUT: sw = True
                y = nxt(y)
            T['VOLD'] += not sw
            if own[x] != 1: continue
            T['ODDCH'] += 1
            if X0[x][0] != x and X0[sb0[x]] == X1[sb0[x]]:
                y, seen = sb0[x], set()
                while y not in seen and y != x: seen.add(y); y = s1[y] if own[y] == 0 else sb1[y]
                T['VSTEPB' if y == x else 'VSTEP'] += 1
            if x not in D0 and x not in D1: continue
            T['OSRC'] += 1; hx[x] += 1
            y, seen, u, pchg, din = sb0[x], set(), None, False, False
            while y not in seen:
                if y in D0 or y in C: u = y; break
                seen.add(y)
                if own[y] == 0 and s0[y] != s1[y]: pchg = True
                if own[y] == 1 and y in D1: din = True
                y = nxt(y)
            if u is not None and not pchg and not din:
                if X0[u] != X1[u]: T['PROP'] += 1
                else: T['VADD'] += 1
            else:
                T['PFX'] += 1; pf[x] += 1; T['PFXSW'] += pchg; T['PFXDIN'] += din and not pchg; T['PFXNOU'] += u is None
    T['MAXHXS'] = max(T['MAXHXS'], max(hx)); T['MAXPFX'] = max(T['MAXPFX'], max(pf))
print(f"ODDADD {os.path.basename(sys.argv[1])} n {n} iters {len(S) - 1} " + " ".join(f"{a} {b}" for a, b in T.items()))
