#!/usr/bin/env python3
"""L-NEW box 132 ANCHOR: test of Theorem FL-ANCHOR on every maximal FL run (W unchanged on consecutive non-fallback transitions of one
tau-stretch; same run detection as box131/dcyc.py).
Gating data at state j: G_j = (sbar_j on Odd vertices, Xi_j on ODIFF_j = {o Odd : sbar_j(o) != tau(o)}, Xi_j on the W-cycle NODES
CN (vertices of W-length 0)). An EPOCH is a maximal set of consecutive transitions j-1 -> j of the run whose gating states j-1 carry the
same G. Theorem FL-ANCHOR predicts, for an epoch with first gating state s0: (i) a non-cycle-node Even vertex x of level l(x) (= length
of its W-play to its cycle node) moves only at transitions j with j - s0 <= l(x) - 1 (VIOL), always to an option of level l(x) - 1
(LVLVIOL); (ii) after j - s0 > lmax - 1 every move of a cycle node c strictly raises Xi_(j-1)(sigma(c)) (CMNORISE among CMLATE); (iii)
epoch length <= CAP := (lmax - 1) + sum_c (|T_c| - 1), T_c = successors of c whose W-cycle node is c (EPVIOL); (iv) FL run length <=
CAP * (1 + GCH), GCH = number of gating changes inside the run (BOUNDVIOL). Boundary causes: XIB (Xi change at an ODIFF vertex), SBB
(sbar change), CYB (Xi change at a cycle node only). CMOVES = cycle-node moves, CMXICH = those with Xi_j(c) != Xi_(j-1)(c).
Usage: anchor.py G.pg [START|-]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "box21")); sys.path.insert(0, os.path.join(HERE, "..", "..", "red", "r170"))
from n5x import load, start_pair, readstart, Engine, dual
import pg
from freeze import run
g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] != "-" else None
E0, Ed0 = Engine(g), Engine(dual(g)); s, t = start_pair(g, E0, Ed0, st)
S, T, F, E = run(g, s, t); n, own, pr = g.n, g.owner, g.prio
Wc = {}
def weng(tau):
    if tau not in Wc: Wc[tau] = Engine(pg.Game(list(pr), list(own), [list(g.succ[v]) if own[v] == 0 else [tau[v]] for v in range(n)]))
    return Wc[tau]
def wval(j):
    return weng(T[j]).evaluate(tuple(S[j][v] if own[v] == 0 else -1 for v in range(n)))[0]
runs = []; cur = None
for j in range(1, len(S)):
    if not F[j] and T[j] == T[j - 1] and S[j] != S[j - 1] and wval(j) == wval(j - 1):
        if cur and cur[1] == j - 1: cur[1] = j
        else: cur = [j - 1, j]; runs.append(cur)
def cycles(sig, tau):
    succ1 = [sig[v] if own[v] == 0 else tau[v] for v in range(n)]
    oncyc = set(); col = [0] * n
    for v0 in range(n):
        if col[v0]: continue
        path = []; v = v0
        while not col[v]: col[v] = 1; path.append(v); v = succ1[v]
        if col[v] == 1 and v in path: oncyc.update(path[path.index(v):])
        for u in path: col[u] = 2
    return frozenset(oncyc), frozenset((v, succ1[v]) for v in oncyc)
R = dict(runs=len(runs), fl=0, epochs=0, gch=0, viol=0, lvlviol=0, cmoves=0, cmnorise=0, cmlate=0, maxep=0, epviol=0, boundviol=0,
         xib=0, sbb=0, cyb=0, maxlen=0, cmxich=0)
ex = []
for a, b in runs:
    tau = T[a]; W = wval(a); lvl = [W[v][2] for v in range(n)]
    CN = [v for v in range(n) if lvl[v] == 0]
    Tc = {c: [y for y in g.succ[c] if W[y][0] == c] for c in CN if own[c] == 0}
    lm = max([lvl[x] for x in range(n) if own[x] == 0 and lvl[x] > 0] + [1])
    cap = (lm - 1) + sum(max(len(v) - 1, 0) for v in Tc.values())
    gat, XI = {}, {}
    for j in range(a, b + 1):
        vs, sb = E.evaluate(S[j]); XI[j] = vs
        od = tuple(sorted(o for o in range(n) if own[o] == 1 and sb[o] != tau[o]))
        gat[j] = (tuple(sb[o] for o in range(n) if own[o] == 1), tuple((o, vs[o]) for o in od), tuple((c, vs[c]) for c in CN))
    R["fl"] += b - a; R["maxlen"] = max(R["maxlen"], b - a)
    s0 = a; eplen = 0; nep = 1; ng = 0
    for j in range(a + 1, b + 1):
        if gat[j - 1] != gat[s0]:
            g0, g1 = gat[s0], gat[j - 1]
            R["sbb"] += g0[0] != g1[0]; R["xib"] += g0[0] == g1[0] and g0[1] != g1[1]; R["cyb"] += g0[:2] == g1[:2] and g0[2] != g1[2]
            R["maxep"] = max(R["maxep"], eplen); R["epviol"] += eplen > cap
            s0 = j - 1; eplen = 0; nep += 1
        if gat[j - 1] != gat[j - 2 if j - 2 >= a else j - 1]: ng += 1
        eplen += 1
        for x in range(n):
            if own[x] != 0 or S[j][x] == S[j - 1][x]: continue
            if lvl[x] == 0:
                R["cmoves"] += 1; R["cmxich"] += XI[j][x] != XI[j - 1][x]
                if j - s0 > lm - 1:
                    R["cmlate"] += 1
                    if not E.key(XI[j - 1][S[j][x]]) > E.key(XI[j - 1][S[j - 1][x]]): R["cmnorise"] += 1
                continue
            l = lvl[x]
            if j - s0 > l - 1:
                R["viol"] += 1
                if len(ex) < 5: ex.append((a, b, j, s0, x, l))
            if lvl[S[j][x]] != l - 1: R["lvlviol"] += 1
    R["maxep"] = max(R["maxep"], eplen); R["epviol"] += eplen > cap
    R["epochs"] += nep; R["gch"] += ng
    R["boundviol"] += (b - a) > cap * (1 + ng)
print(f"ANCHOR {os.path.basename(sys.argv[1])} n {n} " + " ".join(f"{k.upper()} {v}" for k, v in R.items()) + (f" EX {ex}" if ex else ""))
