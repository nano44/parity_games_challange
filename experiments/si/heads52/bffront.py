#!/usr/bin/env python3
"""L-SI box 52: Bellman-Ford front (also MINW1 / BADW: the same with the W-length of x at k+1 in place of delta; SWB: violating
changes at a switched Even vertex) inside rwin.py's event-free windows of a W-run. Gates G_k := D_k u C (D_k = {Odd o : sbar_k(o) !=
tau(o)}, C = W-cycle nodes). delta_k(x) := number of edges of the (sigma_k, sbar_k)-play from x before its first vertex of G_k (0 on
G_k; None if the play closes a cycle first). For a window with first state k0 and a Xi-change of x at transition k -> k+1 (offset
j = k - k0), FRONT_k := delta_k(x) - j and FRONT_k1 := delta_(k+1)(x) - j. Prints the minima (MINF0 / MINF1), the number of changes with
a None delta (NOD), and the count of changes with delta_(k+1)(x) <= j (BAD1).  MUT=1: count l_(k+1)(x) <= j + 1 in BADW (control).  Usage: bffront.py GAME.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "new", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
MUT = int(os.environ.get('MUT', '0'))   # control: MUT=1 tests l <= j + 1, which must find cases where the bound is tight
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
c = dict(CH=0, MINF0=10 ** 9, MINF1=10 ** 9, NOD=0, BAD1=0, BAD0=0, MINW1=10 ** 9, BADW=0, SWB=0)
for p, q in runs:
    tau = TAU[p]; C = {x for x in range(n) if Wv(p, tau)[x][0] == x}
    def gates(k):
        sb = EV[k][1]; return {o for o in range(n) if own[o] == 1 and sb[o] != tau[o]} | C
    def U(k):
        sb = EV[k][1]
        return {sb[o] for o in range(n) if own[o] == 1 and sb[o] != tau[o]} | {(S[k][x] if own[x] == 0 else sb[x]) for x in C}
    def delta(k):
        G = gates(k); sb = EV[k][1]; d = [None] * n
        for x in range(n):
            y, seen, i = x, set(), 0
            while y not in G and y not in seen:
                seen.add(y); y = S[k][y] if own[y] == 0 else sb[y]; i += 1
            d[x] = i if y in G else None
        return d
    k0 = p; dl = {p: delta(p)}
    for k in range(p, q):
        ev = EV[k][1] != EV[k + 1][1] or any(S[k][x] != S[k + 1][x] for x in C if own[x] == 0) or \
             any(XK[k][u] != XK[k + 1][u] for u in U(k) | U(k + 1))
        dl[k + 1] = delta(k + 1)
        if ev: k0 = k + 1; continue
        j = k - k0
        for x in range(n):
            if XK[k][x] != XK[k + 1][x]:
                c['CH'] += 1; d0, d1 = dl[k][x], dl[k + 1][x]
                if d0 is None or d1 is None: c['NOD'] += 1; continue
                c['MINF0'] = min(c['MINF0'], d0 - j); c['MINF1'] = min(c['MINF1'], d1 - j)
                c['BAD1'] += d1 <= j; c['BAD0'] += d0 <= j
                lw = Wv(k + 1, tau)[x][2]; c['MINW1'] = min(c['MINW1'], lw - j); c['BADW'] += lw <= j + MUT
                if own[x] == 0 and S[k][x] != S[k + 1][x] and d1 <= j: c['SWB'] += 1
print(f"BFF {os.path.basename(a[0])} n {n} " + " ".join(f"{k} {v}" for k, v in c.items()))
