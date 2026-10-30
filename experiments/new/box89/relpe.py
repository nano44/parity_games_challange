#!/usr/bin/env python3
"""L-NEW box 89 (CONJECTURE REL-EDGE): per W-run F of N5, LATE_F(y, z) := late adoptions (releases) of the Even edge (y, z) (R88: y switches
to z, (y, z) BLOCKED at an earlier state of F). Also per FROZEN stretch (maximal sub-run of F with sigmabar constant): max releases of one edge (CONJECTURE BIP-REL-1: <= 1).
Prints max_(F, y, z) LATE_F, max R*_F, m_E, and max over F of R*_F / m_E.
Usage: relpe.py GAME.pg [START]"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
STRICT = os.environ.get("STRICT") == "1"
g = load(sys.argv[1]); start = readstart(sys.argv[2]) if len(sys.argv) > 2 else None; n = g.n
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); S = [tuple(s)]; TAU = [tuple(t)]; FB = []
while True:
    r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
    if r is None: break
    S.append(tuple(r[0])); TAU.append(tuple(r[1])); FB.append(r[4])
T = len(S) - 1; ev = [v for v in range(n) if g.owner[v] == 0]; mE = sum(len(g.succ[v]) for v in ev)
Wc = {}
def Wv(k, tau):
    if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(g.owner), [[tau[v]] if g.owner[v] == 1 else g.succ[v] for v in range(n)]))
    return Wc[tau].evaluate(S[k])[0]
runs = []; cur = None
for k in range(T):
    ok = TAU[k + 1] == TAU[k] and not FB[k] and S[k + 1] != S[k] and [x[0] for x in Wv(k, TAU[k])] == [x[0] for x in Wv(k + 1, TAU[k])]
    if not ok: cur = None; continue
    if cur is None: cur = [k, k]; runs.append(cur)
    cur[1] = k + 1
mx = dict(late_edge=0, rstar=0, F=0, frozen_edge=0); arg = None; SB = [E.evaluate(x)[1] for x in S]
for a, b in runs:
    W = [Wv(q, TAU[a]) for q in range(a, b + 1)]; blocked = set(); late = Counter(); rstar = 0; fz = Counter()
    for q in range(a, b):
        if q > a and SB[q] != SB[q - 1]:
            fz = Counter()
            if STRICT: blocked = set()
        xi = E.evaluate(S[q])[0]; Is = set(E.improving(S[q], xi)); hit = False
        for y in ev:
            z = S[q + 1][y]
            if z != S[q][y] and (y, z) in blocked:
                late[(y, z)] += 1; hit = True
                if SB[q + 1] == SB[q]: fz[(y, z)] += 1; mx['frozen_edge'] = max(mx['frozen_edge'], fz[(y, z)])
        rstar += hit
        for y in ev:
            for z in g.succ[y]:
                if z != S[q][y] and E.key(W[q - a][z]) > E.key(W[q - a][S[q][y]]) and (y, z) not in Is: blocked.add((y, z))
    le = max(late.values()) if late else 0
    if le > mx['late_edge']: arg = max(late, key=late.get)
    mx['late_edge'] = max(mx['late_edge'], le); mx['rstar'] = max(mx['rstar'], rstar); mx['F'] = max(mx['F'], b - a)
print(f"RELPE n {n} mE {mE} runs {len(runs)} maxima {mx} argmax-edge {arg}")
