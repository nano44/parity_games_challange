#!/usr/bin/env python3
"""L-NEW box 166: PM in the ONE-BIT key model. Every mover of the violator V gets an orientation o(x) in {0,1,2,3}: KP_t(x) = c_t,
1-c_t, 0 or 1 (= a level-1 mover whose two options W-point to the two level-0 movers in either order, or to the same one; P-IDEAL-FLIP
c-step at level 1). Dynamics: s_t(x) = KP_t(x) if x is Xi-unhappy at s_(t-1), else s_(t-1)(x); c_t free (unlimited flips; T_inf-style
forced model) or with <= k flips. Exact DP: max moves(x0) over orientations, starts, bit sequences. Usage: onebit.py vfile x0 [k]"""
import os, sys, json, itertools
H = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(H, "..", "box165", "permover.py")).read().split("\nif __name__")[0])
sys.setrecursionlimit(100000)
V = json.load(open(sys.argv[1])); x0 = int(sys.argv[2]); K = int(sys.argv[3]) if len(sys.argv) > 3 else 10 ** 6
g = Gen(V); N = V["N"]; states = list(itertools.product((0, 1), repeat=N)); unh = {s: [x for x in range(N) if len(g.avail(s, x)) == 2] for s in states}
def step(s, c, o):
    t = list(s)
    for x in unh[s]:
        kp = (c, 1 - c, 0, 1)[o[x]]; t[x] = kp
    return tuple(t)
best = (0, None)
for o in itertools.product(range(4), repeat=N):
    memo = {}
    def f(s, c, j):
        key = (s, c, j)
        if key in memo: return memo[key]
        v = 0
        for cc in (c, 1 - c):
            jj = j - (cc != c)
            if jj < 0: continue
            t = step(s, cc, o)
            if t != s: v = max(v, (t[x0] != s[x0]) + f(t, cc, jj))
        memo[key] = v; return v
    m = max(f(s, c, min(K, 64)) for s in states for c in (0, 1))
    if m > best[0]: best = (m, o)
R = reach(V)
print("ONEBIT", os.path.basename(sys.argv[1]), "x0", x0, "desc", len(R[x0]), "k", "inf" if K >= 10 ** 6 else K, "max moves(x0)", best[0], "orientation", best[1])
