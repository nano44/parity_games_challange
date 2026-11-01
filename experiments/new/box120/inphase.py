#!/usr/bin/env python3
"""L-NEW box 120 fixes (GATE-L1): the most W-changing transitions in one lambda_W-phase of a tau-stretch, under two phase definitions.
IN-PHASE (the packet's / line's definition): a transition k -> k+1 of a tau-stretch belongs to a phase iff lambda_W is the same at BOTH
states k and k+1; a phase is a maximal run of consecutive such transitions with one lambda. FIRST-STATE (box118/gate.py's grouping): a
transition belongs to the phase of lambda at its FIRST state k only (so a phase's closing transition, where lambda changes, is counted).
lambda_W(state) := v -> cycle node of W(v), W := the (sigma, tau)-valuation (= sigma's valuation in G_tau). Same engine as gate.py (n5x).
Usage: inphase.py G.pg [START|-]   prints one line: INPHASE <game> n K maxFirst maxInPhase stretch-of-max (first, last transition)."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] != "-" else None
n = g.n; own = g.owner; E, Ed = Engine(g), Engine(dual(g))
s, t = start_pair(g, E, Ed, st); S, T = [tuple(s)], [tuple(t)]
while True:
    r = step(g, E, Ed, list(S[-1]), list(T[-1]))
    if r is None: break
    S.append(tuple(r[0])); T.append(tuple(r[1]))
K = len(S) - 1
Wc = {}
def W(k, tau):
    if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(own), [[tau[v]] if own[v] == 1 else g.succ[v] for v in range(n)]))
    return Wc[tau].evaluate(S[k])[0]
mf = mi = 0; where = None
k = 0
while k < K:
    if T[k + 1] != T[k]: k += 1; continue
    a = k                                    # stretch: transitions a .. b-1 with T constant
    while k < K and T[k + 1] == T[k]: k += 1
    b = k; tau = T[a]
    Ws = [W(j, tau) for j in range(a, b + 1)]; lam = [tuple(w[0] for w in x) for x in Ws]
    ch = [Ws[j - a + 1] != Ws[j - a] for j in range(a, b)]
    # FIRST-STATE grouping
    c = 0
    for j in range(a, b):
        if j > a and lam[j - a] != lam[j - a - 1]: c = 0
        c += ch[j - a]; mf = max(mf, c)
    # IN-PHASE grouping
    c = 0; f = None
    for j in range(a, b):
        if lam[j - a] != lam[j - a + 1]: c = 0; f = None; continue
        if j > a and lam[j - a] != lam[j - a - 1]: c = 0; f = None
        if f is None: f = j
        c += ch[j - a]
        if c > mi: mi = c; where = (f, j)
print(f"INPHASE {os.path.basename(sys.argv[1])} n {n} K {K} maxFirst {mf} maxInPhase {mi} at {where}")
