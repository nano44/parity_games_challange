#!/usr/bin/env python3
"""L-NEW box 86 (R*-POLY; docs/new/N5-RSTAR-box86.md). Per W-run F of N5 (R89; as box85/xirise.py): R*_F (R88: transitions at which some
Even y adopts an edge (y, z) BLOCKED at an earlier state of F: W_q(z) > W_q(sigma_q y), (y, z) not in I_sigma_q) and the Odd DEVIATION
edges DEV_t := {(o, sigmabar_t(o)) : o Odd, sigmabar_t(o) != tau(o)}. Checks Lemma GAP-DEV (a blocked target z has W(z) > Xi(z) and its
sigmabar-play meets DEV_t). Prints per game max R*_F, max |union of DEV_t over F| (distinct deviation edges), transitions where DEV changes,
and the CANDIDATE inequality R*_F <= |union DEV| (DEV-CAP; data only). Usage: rstar.py GAME.pg [START]"""
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
T = len(S) - 1; ev = [v for v in range(n) if g.owner[v] == 0]; od = [v for v in range(n) if g.owner[v] == 1]
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
c = dict(gapdev_viol=0, cap_viol=0, blocked=0); mx = dict(rstar=0, dev=0, devch=0, F=0, n=n)
for a, b in runs:
    tau = TAU[a]; blocked = set(); rstar = 0; devu = set(); devch = 0; prev = None
    for q in range(a, b + 1):
        xi, sbar = E.evaluate(S[q]); W = Wv(q, tau); Is = set(E.improving(S[q], xi))
        dev = frozenset((o, sbar[o]) for o in od if sbar[o] != tau[o]); devu |= dev
        if prev is not None and dev != prev: devch += 1
        prev = dev
        if q > a and any((y, S[q][y]) in blocked for y in ev if S[q][y] != S[q - 1][y]): rstar += 1
        if q == b: break
        for y in ev:
            for z in g.succ[y]:
                if z != S[q][y] and E.key(W[z]) > E.key(W[S[q][y]]) and (y, z) not in Is:
                    blocked.add((y, z)); c['blocked'] += 1
                    ok = E.key(W[z]) > E.key(xi[z])
                    seen, x, meet = set(), z, False
                    while x not in seen:
                        seen.add(x)
                        if g.owner[x] == 1 and sbar[x] != tau[x]: meet = True; break
                        x = S[q][x] if g.owner[x] == 0 else sbar[x]
                    if not (ok and meet): c['gapdev_viol'] += 1
    if rstar > len(devu): c['cap_viol'] += 1
    mx['rstar'] = max(mx['rstar'], rstar); mx['dev'] = max(mx['dev'], len(devu)); mx['devch'] = max(mx['devch'], devch); mx['F'] = max(mx['F'], b - a)
print(f"RSTAR n {n} runs {len(runs)} {c} maxima {mx}")
