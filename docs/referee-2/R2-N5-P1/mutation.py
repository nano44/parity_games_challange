#!/usr/bin/env python3
"""REFEREE-2 succ. 8: sensitivity of p1_check.py. (1) flip the odd-multiplicity rule in the extended order -> Lemma B must fail;
(2) CAV-style coarse 'improving' (lengths ignored) -> P1 must fail somewhere (the packet's §4 remark: P1 needs lengths at cycle nodes)."""
import sys, random, itertools
import p1_check as P
RC = P.RC
orig = P.xcmp
def flipped(g, a, b):
    (c, mu, l), (c2, mu2, l2) = a, b
    if c == c2:
        diff = [h for h in set(mu) | set(mu2) if mu.get(h, 0) != mu2.get(h, 0)]
        if diff:
            h = max(diff, key=lambda v: g.rank[v])
            if not g.even[h]: return -1 if mu[h] < mu2[h] else 1      # wrong direction for odd h
    return orig(g, a, b)
rng = random.Random(1); bad1 = 0
for _ in range(300):
    g = P.rand_one_player(rng, rng.randint(3, 8)); f = [rng.choice(s) for s in g.succ]; vals = RC.vals_of(g, f)[0]
    f2 = [rng.choice(s) for s in g.succ]; v2 = RC.vals_of(g, f2)[0]
    for a, b in zip(vals, v2):
        if flipped(g, P.ext(a), P.ext(b)) != g.cmp(a, b): bad1 += 1
print("mutation 1 (flipped odd rule): Lemma B mismatches", bad1)
bad2 = 0
for _ in range(3000):
    n = rng.randint(3, 7); g = P.rand_one_player(rng, n); E = [v for v in range(n) if g.owner[v] == 0]
    strats = []
    for pick in itertools.product(*[g.succ[v] for v in E]):
        f = [g.succ[v][0] for v in range(n)]
        for v, z in zip(E, pick): f[v] = z
        strats.append((f, RC.vals_of(g, f)[0]))
    ck = lambda x: g.key(x)[:2]
    for f, val in strats:
        if any(ck(val[z]) > ck(val[f[v]]) for v in E for z in g.succ[v]): continue
        if not all(all(g.cmp(val[v], v2[v]) >= 0 for v in range(n)) for _, v2 in strats): bad2 += 1
print("mutation 2 (coarse 'improving', lengths dropped): strategies with no coarse-improving edge that are not optimal", bad2)
