#!/usr/bin/env python3
"""REFEREE-2 succ. 30: own brute-force VJ (Voege-Jurdzinski) valuation + Howard strategy improvement on small random parity games.
No lane or fleet code. Priorities are a permutation of 0..n-1 (injective). Odd's optimal counterstrategy = the first (lexicographic)
positional tau that attains the pointwise ⊴-minimum (VJ00: one exists); asserted.
Checks, per P-N5-XICYC §5 (BR-SEG-G) and §3-§4:
  F4X   : steps where ext(x, .) is applied by DOM to a value whose Π already contains x (the case F4's proof does not cover)
  DOMF  : DOM fails: Ω_(t+1)(x) ⊵ ext(x, Ω_t(y)) false, for Even x with Λ_t(x) != x and Λ_(t+1)(x) != x, y a successor
  PRUN  : longest maximal run of p-steps; violation if > n_E, counted only on runs whose steps all satisfy H0
Usage: r2vjg.py SEED COUNT N"""
import sys, random, itertools
def play_val(n, pri, succ_of, v):
    seen = {}; path = []
    while v not in seen:
        seen[v] = len(path); path.append(v); v = succ_of[v]
    cyc = path[seen[v]:]; L = max(cyc, key=lambda u: pri[u]); i = path.index(L)
    pre = path[:i]
    return (L, frozenset(u for u in pre if pri[u] > pri[L]), len(pre))
def rew(pri, u): return pri[u] if pri[u] % 2 == 0 else -pri[u]
def cmp(pri, a, b):   # +1 if a better for Even than b, -1 worse, 0 equal
    if a[0] != b[0]: return 1 if rew(pri, a[0]) > rew(pri, b[0]) else -1
    D = a[1] ^ b[1]
    if D:
        u = max(D, key=lambda z: pri[z]); s = 1 if pri[u] % 2 == 0 else -1
        return s if u in a[1] else -s
    if a[2] == b[2]: return 0
    if pri[a[0]] % 2 == 0: return 1 if a[2] < b[2] else -1
    return 1 if a[2] > b[2] else -1
def ext(pri, v, a): return (a[0], a[1] | ({v} if pri[v] > pri[a[0]] else set()), a[2] + 1)
def addv(pri, a):   # value with cycle node w -> (signed weight of Π, ±k): VJ's order for a fixed w (+2^p even, -2^p odd; shorter better iff w even)
    W = sum((1 if pri[u] % 2 == 0 else -1) << pri[u] for u in a[1]); return (W, -a[2] if pri[a[0]] % 2 == 0 else a[2])
def extplus(pri, v, a):   # ext⁺: add v's weight whenever v is more relevant than w, even if v is already in Π
    W, kk = addv(pri, a); w = a[0]
    if pri[v] > pri[w]: W += (1 if pri[v] % 2 == 0 else -1) << pri[v]
    return (W, kk - 1 if pri[w] % 2 == 0 else kk + 1)
def evaluate(n, pri, own, succ, sigma):
    odd = [v for v in range(n) if own[v] == 1]
    best = None
    for ch in itertools.product(*[succ[v] for v in odd]):
        tau = dict(zip(odd, ch)); so = [sigma[v] if own[v] == 0 else tau[v] for v in range(n)]
        vals = [play_val(n, pri, so, v) for v in range(n)]
        if best is None or all(cmp(pri, vals[v], best[0][v]) <= 0 for v in range(n)) and any(cmp(pri, vals[v], best[0][v]) < 0 for v in range(n)):
            best = (vals, tau)
    vals, tau = best
    # assert pointwise min: no other tau gives a strictly smaller value anywhere
    for ch in itertools.product(*[succ[v] for v in odd]):
        t2 = dict(zip(odd, ch)); so = [sigma[v] if own[v] == 0 else t2[v] for v in range(n)]
        for v in range(n): assert cmp(pri, play_val(n, pri, so, v), vals[v]) >= 0, 'no pointwise optimum'
    return vals, tau
def run(n, pri, own, succ, s0, C):
    sig = list(s0); S = []
    while True:
        vals, tau = evaluate(n, pri, own, succ, sig); S.append((list(sig), vals, tau))
        new = list(sig)
        for v in range(n):
            if own[v]: continue
            b = sig[v]
            for w in succ[v]:
                if cmp(pri, vals[w], vals[b]) > 0: b = w
            new[v] = b
        if new == sig or len(S) > 500: break
        sig = new
    T = len(S) - 1; labels = []
    for t in range(T):
        (s, v1, t1), (s2, v2, t2) = S[t], S[t + 1]
        lab = 'C' if any(v1[v][0] != v2[v][0] for v in range(n)) else 'R' if t1 != t2 else 'p'
        sw = [x for x in range(n) if own[x] == 0 and s[x] != s2[x]]
        h0 = any(v1[x][0] != x and v2[x][0] != x for x in sw)
        labels.append((lab, h0))
        for x in range(n):
            if own[x] or v1[x][0] == x or v2[x][0] == x: continue
            for y in succ[x]:
                if x in v1[y][1]: C['F4X'] += 1
                C['DOMcases'] += 1
                if lab in 'pR' and v1[y][0] == v1[x][0]:    # REPAIR test (Λ constant on the step): Ω_(t+1)(x) ⊵ ext⁺(x, Ω_t(y))
                    C['DOMplus_cases'] += 1
                    if addv(pri, v2[x]) < extplus(pri, x, v1[y]): C['DOMplus_F'] += 1
                    if (addv(pri, v2[x]) > addv(pri, v1[x])) != (cmp(pri, v2[x], v1[x]) > 0): C['ISO_F'] += 1
                if lab == 'p' and v1[y][0] == v1[x][0]:     # PATH's use: p-step, z0 = x and z1 = y share the cycle node
                    C['DOMPcases'] += 1
                    if cmp(pri, v2[x], ext(pri, x, v1[y])) < 0: C['DOMPF'] += 1
                if cmp(pri, v2[x], ext(pri, x, v1[y])) < 0:
                    C['DOMF'] += 1
                    if x not in v1[y][1]: C['DOMF_noF4X'] += 1
            if s[x] != s2[x]:
                C['STRICTcases'] += 1
                if cmp(pri, v2[x], v1[x]) <= 0: C['STRICTF'] += 1
    # maximal p-runs
    r = 0; h = True
    for lab, h0 in labels + [('C', True)]:
        if lab == 'p': r += 1; h = h and h0
        else:
            if r > C['maxp']: C['maxp'] = r
            nE = sum(1 for v in range(n) if own[v] == 0)
            if r > nE and h: C['PRUNviol'] += 1
            r = 0; h = True
    C['runs'] += 1; C['steps'] += T; C['R'] += sum(l == 'R' for l, _ in labels); C['noH0'] += sum(not h0 for _, h0 in labels)
def gen(rng, n):
    pri = list(range(n)); rng.shuffle(pri); own = [rng.randint(0, 1) for _ in range(n)]
    succ = [sorted(set(rng.sample(range(n), rng.randint(1, min(3, n))))) for _ in range(n)]
    return pri, own, succ
if __name__ == '__main__':
    seed, cnt, n = map(int, sys.argv[1:4]); rng = random.Random(seed)
    C = dict(DOMplus_cases=0, DOMplus_F=0, ISO_F=0, DOMPcases=0, DOMPF=0, DOMF_noF4X=0, STRICTcases=0, STRICTF=0, runs=0, steps=0, R=0, noH0=0, DOMcases=0, DOMF=0, F4X=0, maxp=0, PRUNviol=0)
    for _ in range(cnt):
        pri, own, succ = gen(rng, n)
        if sum(own) > 6: continue
        s0 = [rng.choice(succ[v]) for v in range(n)]
        run(n, pri, own, succ, s0, C)
    print('seed', seed, 'n', n, C)
