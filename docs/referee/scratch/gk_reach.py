#!/usr/bin/env python3
"""REFEREE successor 35: REACH3 replay on Gamma3(G) with this lane's own N5 engine (rl_engine.py, written from SPEC by REFEREE 8),
my own Gamma3 builder (gk_gamma3.py), my own IDEAL simulator (gk_ideal.py) and my own Zielonka (below).
Named counters (must be 0): S3START (state 0 != standard state for s_0), STD (state j <= L not the standard state for s_j),
FLFB (a transition 1..L is a fallback), FLTAU (tau changes at a transition 1..L), FLSIG (sigma unchanged at a transition 1..L),
LASTFB (transition L+1 not a fallback), WIN (N5's winner != Zielonka's at some vertex).
usage: gk_reach.py <engine dir> genome.json ...   (lanes' JSON genome format)"""
import sys
import time


def zielonka(prio, owner, succ):
    """plain recursive Zielonka (max-parity, Even = owner 0); returns the set of vertices won by Even."""
    n = len(prio)
    pred = [[] for _ in range(n)]
    for v in range(n):
        for w in succ[v]: pred[w].append(v)

    def attr(V, T, p):
        A = set(T); cnt = {}
        q = list(T)
        while q:
            w = q.pop()
            for v in pred[w]:
                if v not in V or v in A: continue
                if owner[v] == p: A.add(v); q.append(v)
                else:
                    c = cnt.get(v)
                    if c is None: c = sum(1 for y in succ[v] if y in V)
                    c -= 1; cnt[v] = c
                    if c == 0: A.add(v); q.append(v)
        return A

    sys.setrecursionlimit(100000)

    def solve(V):
        if not V: return set(), set()
        d = max(prio[v] for v in V); p = d % 2
        U = {v for v in V if prio[v] == d}
        A = attr(V, U, p)
        W = solve(V - A)
        if not W[1 - p]:
            res = [None, None]; res[p] = set(V); res[1 - p] = set(); return res[0], res[1]
        B = attr(V, W[1 - p], 1 - p)
        W2 = solve(V - B)
        res = [None, None]; res[p] = W2[p]; res[1 - p] = W2[1 - p] | B
        return res[0], res[1]
    return solve(set(range(n)))[0]


def replay(G, eng, ideal, g3, zl=True, verbose=False, control=False):
    L, why, S = ideal.run(G, keep=True)
    prio, owner, succ, names, idx = g3.build3_revE(G) if control else g3.build3(G)
    n3 = len(prio)
    g = eng.Game(prio, owner, succ)
    t0 = time.time()
    out = eng.run(g, maxit=10 ** 7)
    dt = time.time() - t0
    iters = len(out) - 1
    fbs = [j + 1 for j in range(iters) if out[j]['fb']]             # transition numbers that are fallbacks
    c = dict(S3START=0, STD=0, FLFB=0, FLTAU=0, FLSIG=0, LASTFB=0, WIN=0)

    def is_std(st, s):
        sig, tau = g3.standard(G, idx, s, n3)
        for v in range(n3):                     # «forced choices elsewhere» (P-N5-REACH §3): one successor
            if owner[v] == 0 and sig[v] is None:
                assert len(succ[v]) == 1, names[v]
                sig[v] = succ[v][0]
        assert all(tau[v] is not None for v in range(n3) if owner[v] == 1)
        return all(st['s'][v] == sig[v] for v in range(n3) if owner[v] == 0) and all(st['t'][v] == tau[v] for v in range(n3) if owner[v] == 1)
    if not is_std(out[0], S[0]): c['S3START'] += 1
    for j in range(0, min(L, iters) + 1):
        if not is_std(out[j], S[j]): c['STD'] += 1
    if iters < L + 1: c['STD'] += 1
    for j in range(1, min(L, iters) + 1):
        if out[j - 1]['fb']: c['FLFB'] += 1
        if out[j]['t'] != out[j - 1]['t']: c['FLTAU'] += 1
        if out[j]['s'] == out[j - 1]['s']: c['FLSIG'] += 1
    if iters >= L + 1 and not out[L]['fb']: c['LASTFB'] += 1
    if zl:
        WE = zielonka(prio, owner, succ)
        Xi = out[-1]['Xi']
        for v in range(n3):
            n5even = (prio[Xi[v][0]] % 2 == 0)
            if n5even != (v in WE): c['WIN'] += 1
        nwe = len(WE)
    else: nwe = -1
    return dict(N=G['N'], M=sum(G['deg']), L=L, stop=why, n3=n3, iters=iters, fallbacks=fbs, counters=c, secs=dt, even_won=nwe)


if __name__ == '__main__':
    sys.path.insert(0, sys.argv[1])
    import rl_engine as eng
    import gk_ideal as ideal
    import gk_gamma3 as g3
    for p in sys.argv[2:]:
        G = ideal.from_r178_json(p)
        r = replay(G, eng, ideal, g3)
        print('%s N %d M %d L %d n3 %d iterations %d (L+3 = %d) fallback transitions %s counters %s Even wins %d of %d  %.1fs' % (
            p.split('/')[-1], r['N'], r['M'], r['L'], r['n3'], r['iters'], r['L'] + 3, r['fallbacks'], r['counters'], r['even_won'], r['n3'], r['secs']))
        sys.stdout.flush()
