#!/usr/bin/env python3
"""L-SI box 55: how a deviator's first segment evolves inside a W-run (note docs/si/N5-FSEG-box55.md §2). For Odd o in D_k n D_(k+1),
Q_k(o) := the (sigma_k, sigmabar_k)-play from o up to (excluding) its first vertex in D_k u C other than o (o itself first), so Q_k(o) =
[o] + FS_k(o). Transition classes for o: SAME (Q unchanged), PEEL (the new FS is a proper suffix of the old one: o's choice jumped
forward along its own segment, or the tail end was cut), GROW (anything else: the segment re-grows or re-routes). Trivially, PEELs between
two GROWs (of one o in one W-run) are at most n. Counts: PEEL, GROW, SAME, MAXPEEL / MAXGROW (per o and W-run), MAXHXS (box 54).
Usage: peel.py GAME.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "new", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
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
T = dict(WRUNS=len(runs), SAME=0, PEEL=0, GROW=0, MAXPEEL=0, MAXGROW=0, MAXHXS=0)
def fs(k, o, tau, C):
    X, sb = Xv(k); D = {z for z in range(n) if own[z] == 1 and sb[z] != tau[z]}
    y, out, seen = sb[o], [], set()
    while y not in seen and y not in D and y not in C and y != o:
        seen.add(y); out.append(y); y = S[k][y] if own[y] == 0 else sb[y]
    return tuple(out)
for run in runs:
    tau = TAU[run[0]]; C = {v for v in range(n) if Wv(run[0], tau)[v][0] == v}
    pe = [0] * n; gr = [0] * n; hx = [0] * n
    for k in run:
        (X0, b0), (X1, b1) = Xv(k), Xv(k + 1)
        for o in range(n):
            if own[o] != 1: continue
            if (b0[o] != tau[o] or b1[o] != tau[o]) and X0[o] != X1[o]: hx[o] += 1
            if b0[o] == tau[o] or b1[o] == tau[o]: continue
            q0, q1 = fs(k, o, tau, C), fs(k + 1, o, tau, C)
            if q0 == q1: T['SAME'] += 1
            elif len(q1) < len(q0) and q0[len(q0) - len(q1):] == q1: T['PEEL'] += 1; pe[o] += 1
            else: T['GROW'] += 1; gr[o] += 1
    T['MAXPEEL'] = max(T['MAXPEEL'], max(pe)); T['MAXGROW'] = max(T['MAXGROW'], max(gr)); T['MAXHXS'] = max(T['MAXHXS'], max(hx))
print(f"PEEL {os.path.basename(sys.argv[1])} n {n} iters {len(S) - 1} " + " ".join(f"{a} {b}" for a, b in T.items()))
