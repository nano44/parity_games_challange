#!/usr/bin/env python3
"""L-SI box 54: test CONJECTURE ASC-W inside W-runs (R89 / R97). For a vertex v and a Xi(v)-change at k (Xi_k(v) != Xi_(k+1)(v)) put
key = (2, rank-of-c-change) if the cycle node changes, (1, r) if the path set changes with r the top rank of the symmetric difference,
(0, 0) if only the length changes. ASC-W: if v's consecutive Xi-changes at k1 < k2 (same W-run) have key(k2) <= key(k1), then W(v)
changes at some transition k in (k1, k2] (W_k(v) != W_(k+1)(v)).
Counts per W-run and vertex: XCH (Xi(v)-changes), WCH (W(v)-changes), NA (non-ascents), BAD (non-ascents with no W(v)-change in
(k1, k2]), and the same restricted to SOURCES (v in S_k at the later change; R97). Also checks XCH <= (WCH + 1) * (n + 1) * 2 implicitly
via the max ratio. Flags: -s sources only in BAD listing. Usage: ascw.py GAME.pg [START]"""
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
Wc, Xc = {}, {}
def Wv(k, tau):
    key = (k, tau)
    if key not in Xc:
        if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(own), [[tau[v]] if own[v] == 1 else g.succ[v] for v in range(n)]))
        Xc[key] = Wc[tau].evaluate(S[k])[0]
    return Xc[key]
XX = {}
def Xv(k):
    if k not in XX: XX[k] = E.evaluate(S[k])
    return XX[k]
runs = []; cur = None
for k in range(len(S) - 1):
    if TAU[k + 1] != TAU[k] or FB[k] or [x[0] for x in Wv(k, TAU[k])] != [x[0] for x in Wv(k + 1, TAU[k])]:
        cur = None; continue
    if cur is None: cur = []; runs.append(cur)
    cur.append(k)
def ckey(a, b):
    if a[0] != b[0]: return (2, 0)
    if a[1] != b[1]: return (1, (a[1] ^ b[1]).bit_length() - 1)
    return (0, 0)
T = dict(TURN=0, TURNBAD=0, SRCTURNBAD=0, WRUNS=len(runs), XCH=0, NA=0, BAD=0, SRCXCH=0, SRCNA=0, SRCBAD=0, MAXX=0, MAXW=0, MAXRATIO=0.0, MAXASC=0)
bads = []
for run in runs:
    tau = TAU[run[0]]; W0 = Wv(run[0], tau); C = {v for v in range(n) if W0[v][0] == v}
    hist = [[] for _ in range(n)]; last = [None] * n; wsince = [False] * n; xch = [0] * n; wch = [0] * n; asc = [0] * n
    for k in run:
        X0, sb0 = Xv(k); X1, sb1 = Xv(k + 1); Wa, Wb = Wv(k, tau), Wv(k + 1, tau)
        for v in range(n):
            if Wa[v] != Wb[v]: wch[v] += 1; wsince[v] = True
            if X0[v] == X1[v]: continue
            src = v in C or (own[v] == 1 and (sb0[v] != tau[v] or sb1[v] != tau[v]))
            kk = ckey(X0[v], X1[v]); xch[v] += 1; T['XCH'] += 1; T['SRCXCH'] += src
            if last[v] is not None:
                if kk <= last[v][1]:
                    T['NA'] += 1; T['SRCNA'] += src; asc[v] = 1
                    if not wsince[v]:
                        T['BAD'] += 1; T['SRCBAD'] += src
                else: asc[v] += 1; T['MAXASC'] = max(T['MAXASC'], asc[v])
            else: asc[v] = 1
            last[v] = (k, kk); wsince[v] = False; hist[v].append((k, kk, src))
    WCHK = {}
    for v in range(n):
        h = [x for x in hist[v] if x[1][0] == 1]
        for i in range(1, len(h) - 1):
            d1 = h[i][1][1] - h[i - 1][1][1]; d2 = h[i + 1][1][1] - h[i][1][1]
            if d1 * d2 < 0:
                T['TURN'] += 1
                if not any(Wv(k, tau)[v] != Wv(k + 1, tau)[v] for k in range(h[i - 1][0] + 1, h[i + 1][0] + 1)):
                    T['TURNBAD'] += 1; T['SRCTURNBAD'] += h[i][2]
                    if len(bads) < 12: bads.append((h[i][0], v, own[v], h[i][2], h[i - 1][1], h[i + 1][1]))
    for v in range(n):
        T['MAXX'] = max(T['MAXX'], xch[v]); T['MAXW'] = max(T['MAXW'], wch[v])
        if xch[v]: T['MAXRATIO'] = max(T['MAXRATIO'], round(xch[v] / (wch[v] + 1), 2))
for b in bads: print("BAD k %d v %d own %d src %d prev %s now %s" % b)
print(f"ASCW {os.path.basename(sys.argv[1])} n {n} iters {len(S) - 1} " + " ".join(f"{a} {b}" for a, b in T.items()))
