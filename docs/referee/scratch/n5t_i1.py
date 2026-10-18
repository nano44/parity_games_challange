#!/usr/bin/env python3
"""R-N5T §C: REFEREE-2's VJ00 postulate I1 instance, checked with n5t_probe (VJ00 §4 brute force), plus an exhaustive
one-player n = 3 count of (sigma not maximum, single improvement I, Omega unchanged). Run from the repo root."""
import sys, os, itertools
sys.path.insert(0, os.path.join(os.getcwd(), "docs/referee/scratch"))
from n5t_probe import omega, improvements, from_pg, key_le
def all_strats(n, owner, succ):
    ev = [v for v in range(n) if owner[v] == 0]
    for ch in itertools.product(*[succ[v] for v in ev]):
        s = [None] * n
        for v, w in zip(ev, ch): s[v] = w
        yield s
def is_max(n, owner, succ, plus, Om):
    return all(all(key_le(Ok[v], Om[v], plus) for v in range(n)) for Ok in (omega(n, owner, succ, plus, k) for k in all_strats(n, owner, succ)))
o, s, p, r = from_pg([0, 2, 4], [0, 0, 0], [[1], [0, 1], [0, 1]])
assert r == {0: 0, 1: 1, 2: 2}
sig = [1, 0, 0]; Om = omega(3, o, s, p, sig); imp = improvements(3, o, s, p, sig, Om)
sig2 = [1, 1, 0]; Om2 = omega(3, o, s, p, sig2)
print("Omega(sigma) =", Om, "improvements =", imp)
print("Omega after (1,1) =", Om2, "equal:", Om == Om2, "| sigma maximum:", is_max(3, o, s, p, Om))
print("=> I1 fails for I = {(1,1)}:", (not is_max(3, o, s, p, Om)) and Om == Om2)
cnt = 0
for plus in itertools.product([False, True], repeat=3):
    for succ in itertools.product(*[[c for k in (1, 2, 3) for c in itertools.combinations(range(3), k)]] * 3):
        succ = [list(x) for x in succ]; owner = [0, 0, 0]
        for sg in all_strats(3, owner, succ):
            Om = omega(3, owner, succ, list(plus), sg); imp = improvements(3, owner, succ, list(plus), sg, Om)
            if not imp or is_max(3, owner, succ, list(plus), Om): continue
            for v, ws in imp.items():
                for w in ws:
                    s2 = list(sg); s2[v] = w
                    if omega(3, owner, succ, list(plus), s2) == Om: cnt += 1
print("one-player n=3 (all 8 parity maps x 343 successor maps): (sigma not max, single flat improvement) =", cnt)
