#!/usr/bin/env python3
"""L-NEW box 107 (finer potential below the first difference). Template: L-SI experiments/si/sb53/ceilpot.py (claude/l-si c7f00306,
read only); same W-run detection (TAU constant, no fallback, W cycle nodes constant). Per W-run transition k -> k+1 (W under TAU[k]):
  A      := sum_v lcp(CS Xi(v), CS W(v))                       (L-SI's ceiling agreement; reference)
  RKW    := sum_v |{z : W(z) <= Xi(v)}|                         (rank of Xi(v) among the n current ceiling values; range [0, n^2])
  RKX    := sum_v |{z : Xi(z) <= W(v)}|                         (dual rank)
  PAG    := sum_v (common prefix length of the Xi-play and the W-play from v)   (path agreement below the first difference)
  LCM    := sum_v lcp(CS Xi(v) without the cycle coordinate, same for W)
  DS     := |D| = |{Odd o : sbar(o) != tau(o)}|
  NG     := number of distinct values in {Xi(v)} u {W(v)}
Counts rises / falls / flats of each over all W-run transitions, and over RES := source-free transitions at which A does not fall
(L-SI box 53d's residue). XDEC: transitions at which some Xi(v) strictly decreases (should be 0, R15). WDEC: some W(v) decreases.
Lexicographic test LEX_X: on RES, transitions where X is flat (so (A, X) does not move).  Usage: finpot.py GAME.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 else None; n = g.n; own = g.owner
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, st); S, TAU, FB = [tuple(s)], [tuple(t)], []
while True:
    r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
    if r is None: break
    S.append(tuple(r[0])); TAU.append(tuple(r[1])); FB.append(r[4])
Wc = {}
def Weng(tau):
    if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(own), [[tau[v]] if own[v] == 1 else g.succ[v] for v in range(n)]))
    return Wc[tau]
def Wv(k, tau): return Weng(tau).evaluate(S[k])[0]
def cs(v):
    c, m, l = v
    return (E.rew[c],) + tuple(((1 if E.rankpar[r] == 0 else -1) if (m >> r) & 1 else 0) for r in range(n - 1, -1, -1)) + ((l if E.par[c] == 1 else -l),)
def lcp(a, b):
    i = 0
    while i < len(a) and a[i] == b[i]: i += 1
    return i
def play(sig, odd, v):
    seq, seen = [], set()
    while v not in seen:
        seen.add(v); seq.append(v); v = sig[v] if own[v] == 0 else odd[v]
    return seq
K = E.key
NAMES = ["A", "RKW", "RKX", "PAG", "LCM", "DS", "NG"]
def pots(q, tau):
    X, sb = E.evaluate(S[q]); W = Wv(q, tau); sig = S[q]
    kx = [K(x) for x in X]; kw = [K(w) for w in W]
    sx = sorted(kw); sxx = sorted(kx)
    import bisect
    A = sum(lcp(cs(X[v]), cs(W[v])) for v in range(n))
    RKW = sum(bisect.bisect_right(sx, kx[v]) for v in range(n))
    RKX = sum(bisect.bisect_right(sxx, kw[v]) for v in range(n))
    PAG = 0
    for v in range(n):
        a, b = play(sig, sb, v), play(sig, tau, v); i = 0
        while i < len(a) and i < len(b) and a[i] == b[i]: i += 1
        PAG += i
    LCM = sum(lcp(cs(X[v])[1:], cs(W[v])[1:]) for v in range(n))
    DS = sum(1 for o in range(n) if own[o] == 1 and sb[o] != tau[o])
    NG = len(set(kx) | set(kw))
    return dict(A=A, RKW=RKW, RKX=RKX, PAG=PAG, LCM=LCM, DS=DS, NG=NG), kx, kw
NAMES += ["AF", "BW", "LS"]
c = {"WT": 0, "RES": 0, "XDEC": 0, "WDEC": 0, "WOX": 0, "RES3": 0, "AFDEC": 0, "BWDEC": 0, "LSDEC": 0, "T1": 0, "T2": 0, "T3": 0, "T4": 0, "T4SRC": 0, "MAXT4RUN": 0, "AUPBWF": 0}
for nm in NAMES:
    for suf in ("UP", "DN", "EQ", "UPR", "DNR", "EQR"): c[nm + suf] = 0
XF = E.evaluate(S[-1])[0]
runs = []
for k in range(len(S) - 1):
    if TAU[k + 1] != TAU[k] or FB[k] or [x[0] for x in Wv(k, TAU[k])] != [x[0] for x in Wv(k + 1, TAU[k])]: continue
    if runs and runs[-1][-1] == k - 1: runs[-1].append(k)
    else: runs.append([k])
Oeng = {}
def WO(q, tau):
    # best-response value of sigma_q when Odd is restricted to O = {tau} u It(tau)
    if tau not in Oeng:
        vt, _ = Ed.evaluate(tau); It = Ed.improving(tau, vt); opt = {o: {tau[o]} for o in range(n) if own[o] == 1}
        for o, w in It: opt[o].add(w)
        Oeng[tau] = Engine(pg.Game(list(g.prio), list(own), [sorted(opt[v]) if own[v] == 1 else g.succ[v] for v in range(n)]))
    return Oeng[tau].evaluate(S[q])[0]
for run in runs:
    t4 = 0
    tau = TAU[run[0]]; q = run[-1] + 1; WQ = Wv(q, tau)
    for k in run:
        c["WT"] += 1
        P0, kx0, kw0 = pots(k, tau); P1, kx1, kw1 = pots(k + 1, tau)
        for P, j in ((P0, k), (P1, k + 1)):
            X = E.evaluate(S[j])[0]; W = Wv(j, tau)
            P["AF"] = sum(lcp(cs(X[v]), cs(WQ[v])) for v in range(n)); P["BW"] = sum(lcp(cs(W[v]), cs(WQ[v])) for v in range(n))
            P["LS"] = sum(lcp(cs(X[v]), cs(XF[v])) for v in range(n))
        c["WOX"] += Wv(k, tau) != WO(k, tau)
        c["XDEC"] += any(kx1[v] < kx0[v] for v in range(n)); c["WDEC"] += any(kw1[v] < kw0[v] for v in range(n))
        for nm in ("AF", "BW", "LS"): c[nm + "DEC"] += P1[nm] < P0[nm]
        X0, sb0 = E.evaluate(S[k]); X1, sb1 = E.evaluate(S[k + 1]); Wk = Wv(k, tau); C = {v for v in range(n) if Wk[v][0] == v}
        Sk = {o for o in range(n) if own[o] == 1 and (sb0[o] != tau[o] or sb1[o] != tau[o])} | C
        src = any(X0[v] != X1[v] for v in Sk); res = (not src) and P1["A"] >= P0["A"]; c["RES"] += res
        wc = Wv(k, tau) != Wv(k + 1, tau); bwf = P1["BW"] == P0["BW"]
        cat = "T1" if not wc else "T2" if not bwf else "T3" if P1["A"] < P0["A"] else "T4"
        c[cat] += 1; t4 += cat == "T4"; c["T4SRC"] += cat == "T4" and src; c["AUPBWF"] += bwf and P1["A"] > P0["A"]
        c["MAXT4RUN"] = max(c["MAXT4RUN"], t4)
        c["RES3"] += res and all(P1[x] == P0[x] for x in ("AF", "BW", "LS"))
        for nm in NAMES:
            d = "UP" if P1[nm] > P0[nm] else "DN" if P1[nm] < P0[nm] else "EQ"
            c[nm + d] += 1
            if res: c[nm + d + "R"] += 1
print(f"FINPOT {os.path.basename(sys.argv[1])} n {n} " + " ".join(f"{a} {b}" for a, b in c.items()))
