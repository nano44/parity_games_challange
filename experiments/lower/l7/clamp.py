#!/usr/bin/env python3
"""L-LOWER 7 (BOX L7): clamped completion and the ideal pair-6 target. runclamp(D, tgt, M) runs D's rules (sim6) except that the
movers in M follow the target states tgt[t][x] (t = 0..len(tgt) - 1); returns the full state sequence. ideal6(S, a, b): from a run
S of a genome with levels 0-5 capped, the pair-6 target in which, in every 6-window [t0, t1) (between consecutive pair-5 moves),
the first mover f = 13 moves at t0 + a and the second q = 12 at t0 + a + b (clipped into the window), both to c_6."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'l6'))
from sim6 import okeys, topo, bv
def runclamp(D, tgt, M):
    d = D['d']; N = 2 * d; order = topo(D); g = D['gate']; s = list(tgt[0]); S = [tuple(s)]
    for t in range(1, len(tgt)):
        v = {}
        for x in order:
            m = 2 * x + s[x]; y = D['xt'][m]; v[x] = bv(D, m) + (v[y] if y >= 0 else 0)
        av = []
        for x in range(N):
            m = 2 * x + 1 - s[x]; y = D['xt'][m]; ov = bv(D, m) + (v[y] if y >= 0 else 0); av.append(ov > v[x])
        ns = list(s); c = 0
        for l in range(d):
            for q in (0, 1):
                x = 2 * l + q
                if x in M: ns[x] = tgt[t][x]
                elif l == 0:
                    if av[x] and g[2 * x + 1 - s[x]] < g[2 * x + s[x]]: ns[x] = 1 - s[x]
                elif av[x] and s[x] != c: ns[x] = c
            if l == 0: ol = int(g[0 + ns[0]] > g[2 + ns[1]])
            else:
                a_, b_ = ns[2 * l], ns[2 * l + 1]; ol = int(a_ != c) if a_ != b_ else int(g[4 * l + a_] > g[4 * l + 2 + a_])
            c = ol
        s = ns; S.append(tuple(s))
    return S
def ideal6(D, S, a=0, b=1, f=13, q=12, extra=3):
    T = len(S) - 1; mv = [t for t in range(1, T + 1) if S[t][10:12] != S[t - 1][10:12]]
    W = list(zip([1] + mv, mv + [T + 1 + extra]))
    tg = [list(x) + [0] * 0 for x in S] + [list(S[-1]) for _ in range(extra)]
    for t in range(len(tg)):
        tg[t][f] = tg[t][q] = None
    cur = {f: S[0][f], q: S[0][q]}
    for (t0, t1) in W:
        c = okeys(D, S[min(t0, T)])[5]   # o(5) depends on pairs 0-5 only (unchanged)
        u1 = min(t0 + a, t1 - 2) if t1 - t0 >= 2 else t0; u2 = min(u1 + b, t1 - 1)
        for t in range(t0, min(t1, len(tg))):
            if t >= u1: cur[f] = c
            if t >= u2 and u2 > u1: cur[q] = c
            tg[t][f] = cur[f]; tg[t][q] = cur[q]
    tg[0][f] = S[0][f]; tg[0][q] = S[0][q]
    for t in range(1, len(tg)):
        for x in (f, q):
            if tg[t][x] is None: tg[t][x] = tg[t - 1][x]
    return [tuple(x) for x in tg]
