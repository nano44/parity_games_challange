#!/usr/bin/env python3
"""L-NEW box 88 (|F| of one W-run vs the one-player tau-arena; docs/new/N5-ONEP-box88.md). Per W-run F of N5 (R89): every LATE ADOPTION
(Even y switches to z at t -> t + 1 with (y, z) BLOCKED at an earlier state of F; R88) is classified by its LAST block state q < t + 1:
  ODD  : some Odd vertex on z's (sigma_q, sigmabar_q)-play has sigmabar_t != sigmabar_q (Odd re-routed on the poisoned play);
  EVEN : otherwise (only Even switches on that play lifted Xi(z));
and POISON-KEPT if every deviation o (sigmabar_q(o) != tau(o)) on that play still has sigmabar_t(o) = sigmabar_q(o).
Also: |F|, R*_F, SB_F = transitions at which sigmabar changes at some Odd vertex, DV_F = transitions at which the deviation set
{(o, sigmabar(o)) : sigmabar(o) != tau(o)} changes, W-changing transitions. Usage: release.py GAME.pg [START]"""
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
EV = [E.evaluate(x) for x in S]
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
def play(q, z):
    sig, sb = S[q], EV[q][1]; seen = []; x = z
    while x not in seen: seen.append(x); x = sig[x] if g.owner[x] == 0 else sb[x]
    return seen
tot = dict(late=0, ODD=0, EVEN=0, kept=0); mx = dict(F=0, rstar=0, sb=0, dv=0, wch_tr=0, n=n)
for a, b in runs:
    tau = TAU[a]; W = [Wv(q, tau) for q in range(a, b + 1)]; lastblk = {}; rstar = 0
    sb = sum(1 for q in range(a, b) if any(EV[q][1][o] != EV[q + 1][1][o] for o in od))
    devs = [frozenset((o, EV[q][1][o]) for o in od if EV[q][1][o] != tau[o]) for q in range(a, b + 1)]
    dv = sum(1 for i in range(b - a) if devs[i] != devs[i + 1])
    for q in range(a, b):
        xi, sbar = EV[q]; Is = set(E.improving(S[q], xi)); late_here = False
        for y in ev:
            z = S[q + 1][y]
            if z != S[q][y] and (y, z) in lastblk:
                late_here = True; tot['late'] += 1; q0 = lastblk[(y, z)]; pl = play(q0, z)
                odd = any(g.owner[x] == 1 and EV[q][1][x] != EV[q0][1][x] for x in pl)
                tot['ODD' if odd else 'EVEN'] += 1
                if all(EV[q][1][x] == EV[q0][1][x] for x in pl if g.owner[x] == 1 and EV[q0][1][x] != tau[x]): tot['kept'] += 1
        rstar += late_here
        for y in ev:
            for z in g.succ[y]:
                if z != S[q][y] and E.key(W[q - a][z]) > E.key(W[q - a][S[q][y]]) and (y, z) not in Is: lastblk[(y, z)] = q
    mx['F'] = max(mx['F'], b - a); mx['rstar'] = max(mx['rstar'], rstar); mx['sb'] = max(mx['sb'], sb); mx['dv'] = max(mx['dv'], dv)
    mx['wch_tr'] = max(mx['wch_tr'], sum(1 for i in range(b - a) if W[i + 1] != W[i]))
print(f"RELEASE n {n} runs {len(runs)} {tot} maxima {mx}")
