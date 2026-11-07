#!/usr/bin/env python3
"""box 80: why is level j not doubling? On a genome (stored start), for level j: DBL-EQ (a)'s five conditions, and per j-window the
number of moves of each member of the pair j, the pulse, and for a window where member x does not move: whether pi(x) ever equals the
window's c during it (value side missing) or never reaches c (fuel missing)."""
import json, sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "box76"))
from sim80 import Sim, keyorder
from check80 import windows
G = json.load(open(sys.argv[1])); j = int(sys.argv[2]); sim = Sim(G); S = sim.run(); T = len(S) - 1
F, dbl, W = windows(sim, S); p, q = 2 * j, 2 * j + 1
O = [keyorder(sim, s) for s in S]
c = [None if j == 0 else (0 if O[t][j - 1] else 1) for t in range(T + 1)]
Phi = [sum(S[t][x] != c[t] for x in (p, q)) for t in range(T + 1)]
cv = [sim.cv(s) for s in S]
pi = [[0 if sim.v(cv[t], x, 0) > sim.v(cv[t], x, 1) else 1 for x in (p, q)] for t in range(T + 1)]
bsteps = [t for t in range(1, T + 1) if O[t][j - 1] != O[t - 1][j - 1]]
both = sum(1 for t in range(1, T + 1) if S[t][p] != S[t - 1][p] and S[t][q] != S[t - 1][q])
flipnomove = sum(1 for t in range(1, T + 1) if O[t][j] != O[t - 1][j] and S[t][p] == S[t - 1][p] and S[t][q] == S[t - 1][q])
print("level %d F %d (doubling needs %d) F(j-1) %d T %d" % (j, F[j], 2 * F[j - 1] + 2, F[j - 1], T))
print("  Phi(0) %d Phi(T) %d b-steps with Phi(t-1) != 0: %d of %d; steps moving both: %d; flips without a move: %d"
      % (Phi[0], Phi[T], sum(Phi[t - 1] != 0 for t in bsteps), len(bsteps), both, flipnomove))
kind = collections.Counter()
for (a, e, m) in W[j]:
    cc = c[a]
    for i, x in enumerate((p, q)):
        mv = sum(1 for t in range(a, e + 1) if S[t][x] != S[t - 1][x])
        if mv == 1: kind[("moves once", x)] += 1; continue
        if mv > 1: kind[("moves >1", x)] += 1; continue
        if S[a - 1][x] == cc: kind[("already on c", x)] += 1; continue
        seen = any(pi[t][i] == cc for t in range(a - 1, e))
        kind[("no move, pi reaches c (key/timing)" if seen else "no move, pi never c (fuel)", x)] += 1
for k, n in sorted(kind.items()): print("  %-40s mover %d: %d windows" % (k[0], k[1], n))
