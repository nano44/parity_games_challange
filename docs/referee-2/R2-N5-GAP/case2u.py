#!/usr/bin/env python3
"""REFEREE-2 succ. 21: find a smallest one-player configuration for P-N5-GAP OPT-OFF Case 2 with u ON pi (v on its cycle, c's play reaches
u before v), S empty and u even; write it as a .pg and print rho, v, c, the values and the length relation. Usage: case2u.py seed out.pg"""
import sys, os, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2-N5-FRAME"))
import frame_check as F
rng = random.Random(int(sys.argv[1])); best = None
for i in range(20000):
    g = F.DC.rand_game(rng, rng.randint(3, 5), "kO"); n = g.n; E = F.Engine(g); Ed = F.Engine(F.dual(g))
    tu = [rng.choice(g.succ[v]) if g.owner[v] == 1 else -1 for v in range(n)]
    _, b = Ed.evaluate(tuple(tu)); rho = [b[v] if g.owner[v] == 0 else tu[v] for v in range(n)]
    Om = [F.pval(E, rho, v) for v in range(n)]
    for v in range(n):
        if g.owner[v] != 0 or Om[v][0] == v: continue
        for c in sorted(set(g.succ[v])):
            if c == rho[v]: continue
            path, _ = F.play(rho, c)
            if v not in path: continue
            u = Om[v][0]; pi = path[:path.index(v)]
            if u in pi and not [y for y in pi + [v] if E.rank[y] > E.rank[u]] and g.prio[u] % 2 == 0:
                if best is None or n < best[0].n: best = (g, tu, rho, Om, v, c, u, pi)
    if best and best[0].n <= 3: break
g, tu, rho, Om, v, c, u, pi = best
with open(sys.argv[2], "w") as f:
    f.write(f"parity {g.n - 1};\n")
    for x in range(g.n): f.write(f"{x} {g.prio[x]} {g.owner[x]} {','.join(map(str, g.succ[x]))};\n")
print("n", g.n, "prio", g.prio, "owner", g.owner, "succ", g.succ)
print("tau", tu, "rho (Even optimal reply; Odd = tau)", rho)
print("v", v, "c", c, "u = cycle node of v", u, "pi (c's play before v)", pi, "u in pi:", u in pi)
print("Omega(c)", Om[c], "Omega(rho v)", Om[rho[v]], "len diff", Om[c][2] - Om[rho[v]][2], "|pi|+1", len(pi) + 1)
print("conclusion Omega(c) <= Omega(rho v):", E.key(Om[c]) <= E.key(Om[rho[v]]) if (E := F.Engine(g)) else None)
