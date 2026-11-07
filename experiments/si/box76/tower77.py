#!/usr/bin/env python3
"""L-SI box 77: per-mover profile of a genome run from its stored start: level, Xi-targets of options 0/1, P (maximal Xi-paths,
R113 PATH-RISE), R (rises of cv, HIT), moves, PF; plus per level F. Usage: tower77.py FILE..."""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H)
from tw import Sim, analyse, is_lr
for f in sys.argv[1:]:
    G = json.load(open(f)); assert is_lr(G); sim = Sim(G); N = G["N"]; d = N // 2
    S = sim.run(tuple(G["start"])); a = analyse(sim, S); T = a["T"]
    memo = {}
    def P(x):
        if x < 0: return 1
        if x not in memo: memo[x] = sum(P(G["opts"][x][k][1]) for k in range(2))
        return memo[x]
    print("%s d %d T %d F %s" % (os.path.basename(f), d, T, [sum(1 for t in range(1, T + 1) if a["flip"][t][j]) for j in range(d)]))
    for x in range(N):
        mv = sum(1 for t in range(1, T + 1) if x in a["Mv"][t])
        R = sum(1 for t in range(1, T + 1) if sim.val(S[t], x, S[t][x]) > sim.val(S[t - 1], x, S[t - 1][x]))
        PF = sum(1 for t in range(1, T + 1) if a["pi"][t][x] != a["pi"][t - 1][x])
        xt = [G["opts"][x][k][1] for k in range(2)]
        print("  x %2d lev %d xt %s P %d R %d moves %d PF %d" % (x, G["lev"][x], ["X" if y < 0 else y for y in xt], P(x), R, mv, PF))
