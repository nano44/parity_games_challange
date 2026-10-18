"""i1check.py restricted to one-player games (all vertices owner 0 = (+)), for comparison with REFEREE n5t_i1.py (2,270)."""
import sys, os, itertools; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vjbf import *
cnt = 0; games = 0
subsets = [s for r in (1, 2, 3) for s in itertools.combinations(range(3), r)]
for par in itertools.product((0, 1), repeat=3):
    prio = [2 * i + par[i] for i in range(3)]
    for succ in itertools.product(subsets, repeat=3):
        g = Game(prio, [0, 0, 0], [list(s) for s in succ]); games += 1
        S = list(strategies(g)); OM = {tuple(sorted(s.items())): omega(g, s) for s in S}
        for s in S:
            Om = OM[tuple(sorted(s.items()))]
            if all(all(pv_le(g, OM[k][u], Om[u]) for u in range(3)) for k in OM): continue
            for (v, w) in improvements(g, s, Om):
                sp = dict(s); sp[v] = w
                if OM[tuple(sorted(sp.items()))] == Om: cnt += 1
print('one-player games', games, 'non-maximum sigma with a single flat improvement:', cnt)
