#!/usr/bin/env python3
"""L-NEW box 93 (docs/new/N5-ELIM-box93.md): CONJECTURE ELIM-WIN (L-LIT T58 §4) per W-run F = [a, b] of N5.
HW_F(t) := min over edges e = (v, sigma_t(v)) with sigma_t(v) != sigma_b(v) of (last state of F with e in sigma) + 1 - t; HW_F := max_t
(states t with sigma_t = sigma_b are skipped). Checks |F| <= (m_E + 1) HW_F (HMZ counting) and HW_F <= |F| + 1 (ELIM-EQ). For the window
[t*, t* + HW) of the maximising t*: REVISIT = Even vertices that switch in the window and hold sigma_t*(v) again at some later state of F
(every one does, by ELIM-EQ (ii)); XIW = max over the targets sigma_t*(v) of the switching vertices of the Xi changes in the window;
CERT = edges retired in F (left, never held again) that ELIM-ORD-beta certifies at the end (beta_b(v) >= Xi_b(w)); NCERT the others.
W-run segmentation as box85/xirise.py. Usage: elimwin.py GAME.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
g = load(sys.argv[1]); start = readstart(sys.argv[2]) if len(sys.argv) > 2 else None; n = g.n
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); S = [tuple(s)]; TAU = [tuple(t)]; FB = []
while True:
    r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
    if r is None: break
    S.append(tuple(r[0])); TAU.append(tuple(r[1])); FB.append(r[4])
T = len(S) - 1; ev = [v for v in range(n) if g.owner[v] == 0]
mE = sum(len(g.succ[v]) for v in ev)
Wc = {}
def Wv(k, tau):
    if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(g.owner), [[tau[v]] if g.owner[v] == 1 else g.succ[v] for v in range(n)]))
    return Wc[tau].evaluate(S[k])[0]
runs = []; cur = None
for k in range(T):
    ok = TAU[k + 1] == TAU[k] and not FB[k] and [x[0] for x in Wv(k, TAU[k])] == [x[0] for x in Wv(k + 1, TAU[k])]
    if not ok: cur = None; continue
    if cur is None: cur = [k, k]; runs.append(cur)
    cur[1] = k + 1
XI = [E.evaluate(x)[0] for x in S]; key = E.key
c = dict(viol_count=0, viol_eq=0, cert=0, ncert=0); mx = dict(F=0, HW=0, revisit=0, xiw=0); arg = None
for a, b in runs:
    F = b - a
    last = {}
    for k in range(a, b + 1):
        for v in ev: last[(v, S[k][v])] = k
    hw = 0; tstar = None
    for k in range(a, b + 1):
        nf = [v for v in ev if S[k][v] != S[b][v]]
        if not nf: continue
        h = min(last[(v, S[k][v])] + 1 - k for v in nf)
        if h > hw: hw, tstar = h, k
    if hw == 0: continue
    if F > (mE + 1) * hw: c['viol_count'] += 1
    if hw > F + 1: c['viol_eq'] += 1
    sw = {v for k in range(tstar, min(tstar + hw, b)) for v in ev if S[k + 1][v] != S[k][v]}
    rev = sum(1 for v in sw if any(S[k][v] == S[tstar][v] for k in range(tstar + 1, b + 1)))
    xiw = max([0] + [sum(1 for k in range(tstar, min(tstar + hw, b)) if XI[k + 1][S[tstar][v]] != XI[k][S[tstar][v]]) for v in sw])
    for (v, w), k in last.items():
        if k < b and S[b][v] != w:
            if key(XI[b][S[b][v]]) >= key(XI[b][w]): c['cert'] += 1
            else: c['ncert'] += 1
    if hw > mx['HW']: arg = (a, b, tstar)
    mx['F'] = max(mx['F'], F); mx['HW'] = max(mx['HW'], hw); mx['revisit'] = max(mx['revisit'], rev); mx['xiw'] = max(mx['xiw'], xiw)
print(f"ELIMWIN n {n} mE {mE} runs {len(runs)} {c} maxima {mx} argmax {arg}")
