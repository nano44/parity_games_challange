#!/usr/bin/env python3
"""L-SI box 69: EXACT additive-realisability test of an m = 2 improvement table (bit s*4+z = C_z(s)): for every acyclic ISO Xi-graph,
LP feasibility of rewards r (8 options) with sign constraints (r(2z+1) + V_s(t1) - r(2z) - V_s(t0)) * (+1 if C_z(s) else -1) >= 1 for all
s, z (strict inequalities, scaled; V_s = sum of r along the chain under s, linear in r). Feasible for some graph <=> the table is the
improvement table of an acyclic deterministic total-reward MDP (generic rewards). Uses scipy.optimize.linprog (HiGHS).
Usage: lpreal.py <hex table> ...   (also: --enc N  re-checks N tables of tabs_m2.txt as a positive control)"""
import sys, itertools
from scipy.optimize import linprog
graphs = []
for xt in itertools.product([-1, 0, 1, 2, 3], repeat=8):
    if any(xt[o] == o // 2 for o in range(8)): continue
    adj = {z: {xt[2 * z], xt[2 * z + 1]} - {-1} for z in range(4)}; seen = {}
    def dfs(z):
        if seen.get(z) == 1: return False
        if seen.get(z) == 2: return True
        seen[z] = 1
        if not all(dfs(w) for w in adj[z]): return False
        seen[z] = 2; return True
    if all(dfs(z) for z in range(4)): graphs.append(xt)
def chainvec(xt, s, w):
    v = [0] * 8
    while w >= 0:
        o = 2 * w + ((s >> w) & 1); v[o] += 1; w = xt[o]
    return v
def realisable(C):
    for xt in graphs:
        A, b = [], []
        for s in range(16):
            for z in range(4):
                d = [0] * 8; d[2 * z + 1] += 1; d[2 * z] -= 1
                for k, sg in ((1, 1), (0, -1)):
                    t = xt[2 * z + k]
                    if t >= 0:
                        cv = chainvec(xt, s, t); d = [d[i] + sg * cv[i] for i in range(8)]
                sign = 1 if (C >> (s * 4 + z)) & 1 else -1
                A.append([-sign * x for x in d]); b.append(-1)
        r = linprog([0] * 8, A_ub=A, b_ub=b, bounds=[(None, None)] * 8, method="highs")
        if r.status == 0: return xt
    return None
if __name__ == "__main__":
    if sys.argv[1] == "--enc":
        tabs = [int(l.split()[1], 16) for l in open("tabs_m2.txt")][: int(sys.argv[2])]
        print("positive control: ENC tables realisable", sum(1 for C in tabs if realisable(C)), "of", len(tabs))
    else:
        for h in sys.argv[1:]:
            xt = realisable(int(h, 16)); print(h, "additive-realisable" if xt else "NOT additive-realisable (no acyclic ISO Xi-graph, LP infeasible)", xt or "")
