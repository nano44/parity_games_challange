#!/usr/bin/env python3
"""L-RED R154: abstract SHARED-GATE selector. One Even h with options 1..K; option j has a static W-value Omega_j = j (distinct), a
static branch value Lambda_j (a permutation), and a gate signal a(j) in {1..r}. Xi(option j) = min(Lambda_j, s_a(j)); the r signals are
nondecreasing and chosen ADVERSARIALLY over time (any raise of any subset at each step). Step: open = {j : Xi(j) > Xi(cur)}; if open
is nonempty h moves to the W-max of open + {cur} (ARENA-MAX). Exhaustive over Lambda, the signal map a and the start; DP over
(cur, signal levels). Prints the max number of switches of h. Usage: gates_abs.py K r"""
import sys, itertools, functools
K, r = int(sys.argv[1]), int(sys.argv[2])
LV = [x + 0.5 for x in range(-1, K)]           # signal levels between the Lambda values (0..K-1)
best = (0, None)
for lam in itertools.permutations(range(K)):
    for amap in itertools.product(range(r), repeat=K):
        if amap[0] != 0: continue               # symmetry
        @functools.lru_cache(None)
        def go(cur, lev):
            b = 0
            for nl in itertools.product(range(len(LV)), repeat=r):
                if any(nl[i] < lev[i] for i in range(r)): continue
                s = [LV[i] for i in nl]; xi = lambda j: min(lam[j], s[amap[j]])
                op = [j for j in range(K) if xi(j) > xi(cur)]
                if not op: continue
                nxt = max(op + [cur])
                if nxt != cur: b = max(b, 1 + go(nxt, nl))
            return b
        for c0 in range(K):
            v = go(c0, tuple([0] * r))
            if v > best[0]: best = (v, (lam, amap, c0))
print("K", K, "r", r, "max switches", best[0], "witness (Lambda, signal map, start)", best[1])
