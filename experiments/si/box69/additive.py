#!/usr/bin/env python3
"""L-SI box 69: ADDITIVE realisability at m = 2. For every acyclic ISO Xi-graph on the 4 upper movers (option o = 2z + k -> target
mover or X) and random real rewards r(o) (Gaussian, so no ties), the improvement table C_z(s) = [r(2z+1) + V(t1) > r(2z) + V(t0)],
V(w) = r(2w + s_w) + V(target of that option), V(X) = 0 (a deterministic acyclic total-reward MDP, longest path). ENC (RESULTS R105) is
the special case r = +-2^rank. Collects the distinct tables, compares with tabs_m2.txt (ENC tables), and runs the box 69 abstract
dynamics (mine.py) on tables outside the ENC set.  Usage: additive.py samples_per_graph seed"""
import sys, random, itertools
from mine import t01
S, seed = int(sys.argv[1]), int(sys.argv[2]); rng = random.Random(seed)
enc = set(int(l.split()[1], 16) for l in open("tabs_m2.txt"))
graphs = []
for xt in itertools.product([-1, 0, 1, 2, 3], repeat=8):
    if any(xt[o] == o // 2 for o in range(8)): continue
    adj = {z: {xt[2 * z], xt[2 * z + 1]} - {-1} for z in range(4)}
    seen, ok = {}, True
    def dfs(z):
        if seen.get(z) == 1: return False
        if seen.get(z) == 2: return True
        seen[z] = 1
        for w in adj[z]:
            if not dfs(w): return False
        seen[z] = 2; return True
    if all(dfs(z) for z in range(4)): graphs.append(xt)
print("acyclic ISO Xi-graphs", len(graphs))
add = set()
for xt in graphs:
    for _ in range(S):
        r = [rng.gauss(0, 1) for _ in range(8)]; C = 0
        for s in range(16):
            def V(w, s=s):
                tot = 0.0
                while w >= 0:
                    o = 2 * w + ((s >> w) & 1); tot += r[o]; w = xt[o]
                return tot
            for z in range(4):
                v0 = r[2 * z] + (V(xt[2 * z]) if xt[2 * z] >= 0 else 0.0)
                v1 = r[2 * z + 1] + (V(xt[2 * z + 1]) if xt[2 * z + 1] >= 0 else 0.0)
                if v1 > v0: C |= 1 << (s * 4 + z)
        add.add(C)
new = add - enc
print("additive tables", len(add), "of which in ENC", len(add & enc), "outside ENC", len(new))
best = {}
for C in new:
    for c1 in ((0, 0), (0, 1), (1, 0), (1, 1)):
        T0, T1 = t01(C, c1); best[T0] = max(best.get(T0, -1), T1)
print("D(2, tau) on additive tables outside ENC:", dict(sorted(best.items())))
