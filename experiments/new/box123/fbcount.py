#!/usr/bin/env python3
"""L-NEW box 123: the fallbacks of TWO-FIX windows (tau and sbar fixed; box 121 / 122). For each window with >= 1 fallback:
FB; REPW := pairs of states of the window with equal W-vectors (W := valuation in G_tau; Xi strictly rises, so states never repeat);
REPWF := equal W-vectors among the post-fallback states only; PEAKMON / TROUGHMON := the W-vectors just before (peaks) / just after
(troughs) the fallbacks are pointwise non-decreasing in window order (counts of violating consecutive pairs; 0 = monotone);
SWD := fallback switches whose Even vertex lies in D_j (play through an ODIFF vertex), of SW all fallback switches; WDROP := vertices where
W falls at a fallback (total); WDROPD := of those, vertices in D_j or D_(j+1); GAPF := |{Xi != W}| just after each fallback (list); NOTDESC := consecutive fallback pairs where GAPF does not
strictly fall; NOTDESC_NOXO := those with no Xi-change at an ODIFF vertex at a transition j, f <= j < f' (the first fallback included); XOBETWEEN := pairs with one; XOALL := window
transitions changing Xi at an ODIFF vertex.
Usage: fbcount.py G.pg [START|-]   one FBW line per window with FB >= 1."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] != "-" else None
n = g.n; own = g.owner; E, Ed = Engine(g), Engine(dual(g))
s, t = start_pair(g, E, Ed, st); S, T, FB = [tuple(s)], [tuple(t)], []
while True:
    r = step(g, E, Ed, list(S[-1]), list(T[-1]))
    if r is None: break
    S.append(tuple(r[0])); T.append(tuple(r[1])); FB.append(r[4])
K = len(S) - 1
SB = [tuple(-1 if own[v] == 0 else E.evaluate(x)[1][v] for v in range(n)) for x in S]
Wc = {}
def eng(o):
    if o not in Wc: Wc[o] = Engine(pg.Game(list(g.prio), list(own), [[o[v]] if own[v] == 1 else g.succ[v] for v in range(n)]))
    return Wc[o]
key = E.key
def geq(A, B): return all(key(A[v]) >= key(B[v]) for v in range(n))
k = 0
while k < K:
    if T[k + 1] != T[k] or SB[k + 1] != SB[k]: k += 1; continue
    a = k
    while k < K and T[k + 1] == T[k] and SB[k + 1] == SB[k]: k += 1
    b = k; fbs = [j for j in range(a, b) if FB[j]]
    if not fbs: continue
    o = SB[a]; tau = T[a]; O = {v for v in range(n) if own[v] == 1 and o[v] != tau[v]}
    et = eng(tau); W = {j: et.evaluate(S[j])[0] for j in range(a, b + 1)}; X = {j: E.evaluate(S[j])[0] for j in range(a, b + 1)}
    f = lambda j, v: S[j][v] if own[v] == 0 else o[v]
    def D(j):
        out = set()
        for x in range(n):
            y = x; seen = set()
            while y not in seen:
                if y in O: out.add(x); break
                seen.add(y); y = f(j, y)
        return out
    seenW = {}; rep = 0
    for j in range(a, b + 1):
        kw = tuple(W[j]); rep += seenW.get(kw, 0); seenW[kw] = seenW.get(kw, 0) + 1
    post = [tuple(W[j + 1]) for j in fbs]; repf = len(post) - len(set(post))
    peaks = [W[j] for j in fbs]; troughs = [W[j + 1] for j in fbs]
    pm = sum(not geq(peaks[i + 1], peaks[i]) for i in range(len(fbs) - 1)); tm = sum(not geq(troughs[i + 1], troughs[i]) for i in range(len(fbs) - 1))
    sw = swd = wd = wdd = 0; gapf = []
    for j in fbs:
        Dj, Dj1 = D(j), D(j + 1); chg = [v for v in range(n) if S[j][v] != S[j + 1][v]]
        sw += len(chg); swd += sum(v in Dj for v in chg)
        dr = [v for v in range(n) if key(W[j + 1][v]) < key(W[j][v])]; wd += len(dr); wdd += sum(v in Dj | Dj1 for v in dr)
        gapf.append(sum(X[j + 1][v] != W[j + 1][v] for v in range(n)))
    # GAP-DESC test: consecutive fallbacks f < f'; XOC := Xi changes at an ODIFF vertex at some transition j, f <= j < f'
    xoc = [any(X[j][v] != X[j + 1][v] for v in O for j in range(fbs[i], fbs[i + 1])) for i in range(len(fbs) - 1)]
    gd_bad = sum(1 for i in range(len(fbs) - 1) if not xoc[i] and gapf[i + 1] >= gapf[i])
    gd_inc = sum(1 for i in range(len(fbs) - 1) if gapf[i + 1] >= gapf[i]); nx = sum(xoc)
    xo_all = sum(any(X[j][v] != X[j + 1][v] for v in O) for j in range(a, b))
    print(f"FBW {os.path.basename(sys.argv[1])} n {n} [{a}, {b}] L {b - a} ODIFF {len(O)} FB {len(fbs)} REPW {rep} REPWF {repf} PEAKMON {pm} "
          f"TROUGHMON {tm} SW {sw} SWD {swd} WDROP {wd} WDROPD {wdd} GAPF {gapf} NOTDESC {gd_inc} NOTDESC_NOXO {gd_bad} XOBETWEEN {nx} XOALL {xo_all}")
