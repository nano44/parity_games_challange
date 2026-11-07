#!/usr/bin/env python3
"""L-SI box 77: fuel profile (L-LOWER's FEEDBACK notation, docs/lower/L3-families.md §4 at claude/l-lower 4d747490): for each level l,
Up_l = Xi-targets of upward options (Xi-target of higher level) of movers of level <= l; E_l = steps where cv of some y in Up_l changes;
max moves of a level-l mover vs the FEEDBACK bound 2 l (1 + |E_l|); doubling levels. Usage: fuel77.py FILE..."""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H)
from tw import Sim, analyse, is_lr
for f in sys.argv[1:]:
    G = json.load(open(f)); assert is_lr(G); sim = Sim(G); N = G["N"]; d = N // 2; lev = G["lev"]
    S = sim.run(tuple(G["start"])); a = analyse(sim, S); T = a["T"]
    F = [sum(1 for t in range(1, T + 1) if a["flip"][t][j]) for j in range(d)]
    cv = [[sim.val(S[t], y, S[t][y]) for y in range(N)] for t in range(T + 1)]
    mv = [sum(1 for t in range(1, T + 1) if y in a["Mv"][t]) for y in range(N)]
    up = [(x, k, G["opts"][x][k][1]) for x in range(N) for k in range(2) if G["opts"][x][k][1] >= 0 and lev[G["opts"][x][k][1]] > lev[x]]
    print("%s d %d T %d F %s doubling %s; upward options (x,k->y) %s" % (os.path.basename(f), d, T, F,
          [l for l in range(1, d) if F[l] == 2 * F[l - 1] + 2], [(x, k, y) for x, k, y in up]))
    for l in range(1, d):
        Up = sorted({y for x, k, y in up if lev[x] <= l})
        E = [t for t in range(1, T + 1) if any(cv[t][y] != cv[t - 1][y] for y in Up)]
        m = max(mv[2 * l], mv[2 * l + 1])
        print("  level %d: max moves %d, |E_l| %d, FEEDBACK bound %d, Up_l %s (levels %s)" % (l, m, len(E), 2 * l * (1 + len(E)), Up, [lev[y] for y in Up]))
