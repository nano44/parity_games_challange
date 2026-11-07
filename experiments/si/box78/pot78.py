#!/usr/bin/env python3
"""L-SI box 78: landed potentials on given genomes (stored start). PHI_K(s_0) of RESULTS R114 (w_l = 2^(d-l) - 1 on movers off KP)
and its smallest per-step drop; R105 EXACT-ENERGY E(s) = sum_x c_s(x) 2^pi(x) (pi: Kahn order from the sources, as rank78.py) at s_0
and its smallest per-step drop; T. Both potentials must fall by >= 1 at every step (checked)."""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(H, "..", "box76"))
from tw import Sim, is_lr
for f in sys.argv[1:]:
    G = json.load(open(f)); assert is_lr(G); N = G["N"]; d = N // 2; sim = Sim(G); lev = G["lev"]
    indeg = [0] * N
    for x in range(N):
        for k in range(2):
            y = G["opts"][x][k][1]
            if y >= 0: indeg[y] += 1
    order = []; av = sorted(x for x in range(N) if indeg[x] == 0)
    while av:
        x = av.pop(0); order.append(x)
        for k in range(2):
            y = G["opts"][x][k][1]
            if y >= 0:
                indeg[y] -= 1
                if indeg[y] == 0: av.append(y)
    pi = {x: i for i, x in enumerate(order)}
    S = sim.run(tuple(G["start"])); T = len(S) - 1
    def phik(s):
        K = sim.keys(s); return sum((2 ** (d - lev[x]) - 1) * (s[x] != min(range(2), key=lambda k: sim.okey(K, x, k))) for x in range(N))
    def energy(s):
        return sum(sum(1 for k in range(2) if sim.val(s, x, k) > sim.val(s, x, s[x])) * 2 ** pi[x] for x in range(N))
    P = [phik(s) for s in S]; E = [energy(s) for s in S]
    dp = [P[t - 1] - P[t] for t in range(1, T + 1)]; de = [E[t - 1] - E[t] for t in range(1, T + 1)]
    assert min(dp) >= 1 and min(de) >= 1, f
    print("%s d %d T %d PHI_K(s0) %d (bound 2^(d+2)-2d-4 = %d) min drop %d | ENERGY(s0) %d (2^N - 1 = %d) min drop %d" % (
        os.path.basename(f), d, T, P[0], 2 ** (d + 2) - 2 * d - 4, min(dp), E[0], 2 ** N - 1, min(de)))
