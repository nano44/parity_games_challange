#!/usr/bin/env python3
"""L-NEW box 108: carriers of the level-2 digits (box 107 hier.py, W-only). For each W-run with a level-2 stretch B2 (P1-flat), and each
vertex v whose W changes inside B2: c1 = lcp(W v, ref1 v) (constant on B2; the pending top digit), the change positions inside B2, and the
transition k1 after B2 at which v's c1-digit is fixed (lcp with ref1 rises). The rank position c1 is named by its vertex u1 (CS position
p in 1..n = rank n - p; n + 1 = length). At k1: the switched Even vertices, which of their new edges were NEW in the arena (not in
H_(k1-1)), and whether k1 is a source event (R97). Summary line CARRIER ... Usage: carrier.py GAME.pg [START] [VERBOSE]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2].endswith(".start") else None
VERB = "v" in sys.argv[3:] or (len(sys.argv) > 2 and sys.argv[-1] == "v")
n = g.n; own = g.owner; E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, st); S, TAU, FB, IS = [tuple(s)], [tuple(t)], [], []
while True:
    r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
    if r is None: break
    S.append(tuple(r[0])); TAU.append(tuple(r[1])); FB.append(r[4]); IS.append(set(r[2]))
Wc = {}
def Wv(k, tau):
    if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(own), [[tau[v]] if own[v] == 1 else g.succ[v] for v in range(n)]))
    return Wc[tau].evaluate(S[k])[0]
def cs(v):
    c, m, l = v
    return (E.rew[c],) + tuple(((1 if E.rankpar[r] == 0 else -1) if (m >> r) & 1 else 0) for r in range(n - 1, -1, -1)) + ((l if E.par[c] == 1 else -l),)
byrank = {E.rank[v]: v for v in range(n)}
def posname(p): return "len" if p == n + 1 else "cyc" if p == 0 else f"u{byrank[n - p]}"
def lcp(a, b):
    i = 0
    while i < len(a) and a[i] == b[i]: i += 1
    return i
def arena(k): return {(y, S[k][y]) for y in range(n) if own[y] == 0} | IS[k]
runs = []
for k in range(len(S) - 1):
    if TAU[k + 1] != TAU[k] or FB[k] or [x[0] for x in Wv(k, TAU[k])] != [x[0] for x in Wv(k + 1, TAU[k])]: continue
    if runs and runs[-1][-1] == k - 1: runs[-1].append(k)
    else: runs.append([k])
NB2 = NCAR = SAMEU = FIXNEW = FIXSRC = 0; SHAPES = {}
for run in runs:
    tau = TAU[run[0]]; ks = [k for k in run if Wv(k, tau) != Wv(k + 1, tau)]
    if not ks: continue
    W = {j: [cs(x) for x in Wv(j, tau)] for j in range(run[0], run[-1] + 2)}; ref = W[ks[-1] + 1]
    P = lambda j: [lcp(W[j][v], ref[v]) for v in range(n)]
    stretches, cur = [], []
    for k in ks:
        if sum(P(k + 1)) > sum(P(k)):
            if cur: stretches.append(cur); cur = []
        else: cur.append(k)
    for B in stretches:
        NB2 += 1; e = B[-1] + 1
        vs = sorted({v for k in B for v in range(n) if W[k][v] != W[k + 1][v]})
        for v in vs:
            c1 = lcp(W[B[0]][v], ref[v]); chg = [lcp(W[k][v], W[k + 1][v]) for k in B if W[k][v] != W[k + 1][v]]
            k1 = next(k for k in ks if k >= e and lcp(W[k + 1][v], ref[v]) > c1)
            sw = [y for y in range(n) if S[k1][y] != S[k1 + 1][y]]
            new = [(y, S[k1 + 1][y]) for y in sw if (y, S[k1 + 1][y]) not in arena(k1 - 1)] if k1 > 0 else []
            X0, sb0 = E.evaluate(S[k1]); X1, sb1 = E.evaluate(S[k1 + 1]); C = {x for x in range(n) if Wv(k1, tau)[x][0] == x}
            Sk = {o for o in range(n) if own[o] == 1 and (sb0[o] != tau[o] or sb1[o] != tau[o])} | C
            src = any(X0[x] != X1[x] for x in Sk)
            NCAR += 1; FIXNEW += bool(new); FIXSRC += src
            shape = (posname(c1), tuple(sorted(set(posname(p) for p in chg))))
            SHAPES[shape] = SHAPES.get(shape, 0) + 1
            if VERB: print(f"B2 {B[0]}..{e} v {v} c1 {c1}={posname(c1)} chg {[posname(p) for p in chg]} fixed at {k1} sw {sw} new {new} src {int(src)}")
top = sorted(SHAPES.items(), key=lambda x: -x[1])[:6]
print(f"CARRIER {os.path.basename(sys.argv[1])} n {n} B2 {NB2} carriers {NCAR} fix_by_new_edge {FIXNEW} fix_at_source {FIXSRC} shapes {top}")
