#!/usr/bin/env python3
"""L-SI box 79: wiring and fuel report of a genome run from its stored start (for L-LOWER's inductive step). Prints T, F, doubling
levels, moves per mover; for each doubling level l: each member's two Xi-targets with their level, moves, R (rises of cv) and
TOWER-NEED's bound (f - 1)/2; the upward options of the levels <= l (source -> target, target level, R(target)); and for each fuel
target the movers on its chains that sit at levels <= l (re-entry)."""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(H, "..", "box76"))
from tw import Sim, analyse, is_lr
for f in sys.argv[1:]:
    G = json.load(open(f)); assert is_lr(G); sim = Sim(G); N = G["N"]; d = N // 2; lev = G["lev"]; o = G["opts"]
    S = sim.run(tuple(G["start"])); a = analyse(sim, S); T = a["T"]
    F = [sum(1 for t in range(1, T + 1) if a["flip"][t][j]) for j in range(d)]
    mv = [sum(1 for t in range(1, T + 1) if x in a["Mv"][t]) for x in range(N)]
    R = [sum(1 for t in range(1, T + 1) if sim.val(S[t], x, S[t][x]) > sim.val(S[t - 1], x, S[t - 1][x])) for x in range(N)]
    dbl = [l for l in range(1, d) if F[l] == 2 * F[l - 1] + 2]
    reach = {}
    def rch(x):
        if x not in reach:
            r = set()
            for k in range(2):
                y = o[x][k][1]
                if y >= 0: r |= {y} | rch(y)
            reach[x] = r
        return reach[x]
    print("%s d %d T %d\n  F %s\n  doubling %s\n  moves %s" % (os.path.basename(f), d, T, F, dbl, mv))
    for l in dbl:
        fl = F[l - 1]
        print("  level %d doubling (f = F(%d) = %d; TOWER-NEED: targets need R >= %.1f)" % (l, l - 1, fl, (fl - 1) / 2))
        for x in (2 * l, 2 * l + 1):
            tg = [o[x][k][1] for k in range(2)]
            print("    mover %d (moves %d, R %d): targets %s" % (x, mv[x], R[x], ", ".join(
                "X" if y < 0 else "%d (lev %d, moves %d, R %d)" % (y, lev[y], mv[y], R[y]) for y in tg)))
        ups = [(x, k, o[x][k][1]) for x in range(N) for k in range(2) if lev[x] <= l and o[x][k][1] >= 0 and lev[o[x][k][1]] > lev[x]]
        print("    upward options of levels <= %d: %s" % (l, "; ".join("%d.%d -> %d (lev %d, R %d)" % (x, k, y, lev[y], R[y]) for x, k, y in ups)))
        U = sorted({y for _, _, y in ups})
        print("    re-entry: %s" % "; ".join("%d reaches %s" % (y, sorted(z for z in rch(y) if lev[z] <= l)) for y in U))
