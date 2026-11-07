#!/usr/bin/env python3
"""REFEREE-2 succ. 30: print the first instance (r2vjg.gen, seed 1, n 6) where DOM fails at a p-step with z0 = x, z1 = y sharing the
cycle node (PATH's induction step), with H0 holding at x (Λ_t(x) != x != Λ_(t+1)(x)). Usage: r2dompex.py"""
import random, r2vjg as M
rng = random.Random(1); n = 6
for _ in range(3000):
    pri, own, succ = M.gen(rng, n)
    if sum(own) > 6: continue
    s0 = [rng.choice(succ[v]) for v in range(n)]; sig = list(s0); S = []
    while True:
        vals, tau = M.evaluate(n, pri, own, succ, sig); S.append((list(sig), vals, tau)); new = list(sig)
        for v in range(n):
            if own[v]: continue
            b = sig[v]
            for w in succ[v]:
                if M.cmp(pri, vals[w], vals[b]) > 0: b = w
            new[v] = b
        if new == sig: break
        sig = new
    for t in range(len(S) - 1):
        (s, v1, t1), (s2, v2, t2) = S[t], S[t + 1]
        if any(v1[v][0] != v2[v][0] for v in range(n)) or t1 != t2: continue
        for x in range(n):
            if own[x] or v1[x][0] == x or v2[x][0] == x: continue
            for y in succ[x]:
                if v1[y][0] == v1[x][0] and M.cmp(pri, v2[x], M.ext(pri, x, v1[y])) < 0:
                    fs = lambda v: (v[0], sorted(v[1]), v[2])
                    print('priorities', pri, 'owners (0 Even, 1 Odd)', own, 'successors', succ)
                    print('state t   : sigma', s, 'sigma-bar', t1); print('state t+1 : sigma', s2, 'sigma-bar', t2, '(a p-step: no Λ, no σ̄ change)')
                    print('x', x, 'y', y, 'Ω_t(y)', fs(v1[y]), '(x in Π)' if x in v1[y][1] else '')
                    print('Ω_(t+1)(x)', fs(v2[x]), '◁ ext(x, Ω_t(y))', fs(M.ext(pri, x, v1[y])))
                    print('Ω_t(x)', fs(v1[x]), 'Ω_t(σ_(t+1)(x))', fs(v1[s2[x]]), 'Ω_t(y)', fs(v1[y]))
                    raise SystemExit
