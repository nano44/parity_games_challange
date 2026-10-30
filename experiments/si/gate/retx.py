#!/usr/bin/env python3
"""L-SI box 51b §11: Lemma RETURN-CHARGE' over the WHOLE N5 run (every transition: S4a, tau-changes, S4c fallbacks). For Even v:
MONO_V: Xi_{j+1}(sigma_{j+1}(v)) < Xi_j(sigma_j(v)) at some j (must be 0); IMP_V: a switch of v to an edge not in Isigma_j (must be 0);
RET: returns of v to d (left at k1, re-adopted at k2); RCV: returns with NOT Xi_{k2}(d) |> Xi_{k1}(d) (must be 0).
Per W-run F (as gate.py: tau fixed, no fallback, lambda_W fixed): FB_V: W-runs with |F| > m_E + sum_d d_E(d) XCH_F(d) (must be 0);
SLACK: min over W-runs of that bound minus |F|; LMAX: longest W-run. Odd side (dual valuation Xi^U_t := Ed.evaluate(tau_t), improving
set It): OMONO_V, OIMP_V, ORET, ORCV as above. TB_V: runs with T > m_E(1 + XE) + m_O(1 + XO) (XE / XO the most Xi / Xi^U changes of one
vertex over the run; must be 0). Usage: retx.py GAME.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "new", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
a = sys.argv[1:]; g = load(a[0]); n = g.n; own = g.owner
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, readstart(a[1]) if len(a) > 1 else None)
S, TAU, FB, IS, IT = [tuple(s)], [tuple(t)], [], [], []
while True:
    r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
    if r is None: break
    S.append(tuple(r[0])); TAU.append(tuple(r[1])); FB.append(r[4]); IS.append(set(r[2])); IT.append(set(r[3]))
T = len(S) - 1; XK = [[E.key(x) for x in E.evaluate(st)[0]] for st in S]
mE = sum(len(g.succ[v]) for v in range(n) if own[v] == 0); dE = [0] * n
for v in range(n):
    if own[v] == 0:
        for w in set(g.succ[v]): dE[w] += 1
c = dict(T=T, MONO_V=0, IMP_V=0, RET=0, RCV=0, FB_V=0, SLACK=None, LMAX=0, OMONO_V=0, OIMP_V=0, ORET=0, ORCV=0, TB_V=0)
UK = [[Ed.key(x) for x in Ed.evaluate(tt)[0]] for tt in TAU]
for v in range(n):
    if own[v] != 1: continue
    leave = {}
    for j in range(T):
        if UK[j + 1][TAU[j + 1][v]] < UK[j][TAU[j][v]]: c['OMONO_V'] += 1
        if TAU[j + 1][v] == TAU[j][v]: continue
        d = TAU[j + 1][v]
        if (v, d) not in IT[j]: c['OIMP_V'] += 1
        if d in leave:
            c['ORET'] += 1
            if not UK[j][d] > UK[leave[d]][d]: c['ORCV'] += 1
        leave[TAU[j][v]] = j
mO = sum(len(g.succ[v]) for v in range(n) if own[v] == 1)
XE = max(sum(1 for j in range(T) if XK[j + 1][u] != XK[j][u]) for u in range(n)) if T else 0
XO = max(sum(1 for j in range(T) if UK[j + 1][u] != UK[j][u]) for u in range(n)) if T else 0
c['TB_V'] = int(T > mE * (1 + XE) + mO * (1 + XO))
for v in range(n):
    if own[v] != 0: continue
    leave = {}
    for j in range(T):
        if XK[j + 1][S[j + 1][v]] < XK[j][S[j][v]]: c['MONO_V'] += 1
        if S[j + 1][v] == S[j][v]: continue
        d = S[j + 1][v]
        if (v, d) not in IS[j]: c['IMP_V'] += 1
        if d in leave:
            c['RET'] += 1
            if not XK[j][d] > XK[leave[d]][d]: c['RCV'] += 1
        leave[S[j][v]] = j
Wc = {}
def Wl(k, tau):
    if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(own), [[tau[v]] if own[v] == 1 else g.succ[v] for v in range(n)]))
    return [x[0] for x in Wc[tau].evaluate(S[k])[0]]
runs, cur = [], None
for k in range(T):
    ok = TAU[k + 1] == TAU[k] and not FB[k] and S[k + 1] != S[k] and Wl(k, TAU[k]) == Wl(k + 1, TAU[k])
    if not ok: cur = None; continue
    if cur is None: cur = [k, k]; runs.append(cur)
    cur[1] = k + 1
for p, q in runs:
    bound = mE + sum(dE[d] * sum(1 for j in range(p, q) if XK[j + 1][d] != XK[j][d]) for d in range(n))
    c['LMAX'] = max(c['LMAX'], q - p); c['FB_V'] += q - p > bound
    c['SLACK'] = bound - (q - p) if c['SLACK'] is None else min(c['SLACK'], bound - (q - p))
print(f"RETX {os.path.basename(a[0])} n {n} " + " ".join(f"{k} {v}" for k, v in c.items()))
