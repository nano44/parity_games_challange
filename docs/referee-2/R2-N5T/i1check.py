"""Does VJ00 postulate I1 fail for Improve = Switch_I with an arbitrary nonempty I (VJ00 4.4)? Count (game, sigma, I) with
sigma NOT a maximum of (Strategies, pointwise E on Omega) and Omega_{Switch_I(sigma)} = Omega_sigma. Exhaustive n = 3."""
import sys, os, itertools; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vjbf import *
cnt = 0; ex = None; games = 0
subsets = [s for r in (1, 2, 3) for s in itertools.combinations(range(3), r)]
for par in itertools.product((0, 1), repeat=3):
    prio = [2 * i + par[i] for i in range(3)]
    for owner in itertools.product((0, 1), repeat=3):
        for succ in itertools.product(subsets, repeat=3):
            g = Game(prio, list(owner), [list(s) for s in succ]); games += 1
            S = list(strategies(g)); OM = {tuple(sorted(s.items())): omega(g, s) for s in S}
            for s in S:
                Om = OM[tuple(sorted(s.items()))]
                ismax = all(all(pv_le(g, OM[k][u], Om[u]) for u in range(g.n)) for k in OM)
                if ismax: continue
                for (v, w) in improvements(g, s, Om):
                    sp = dict(s); sp[v] = w
                    if OM[tuple(sorted(sp.items()))] == Om:
                        cnt += 1; ex = ex or (prio, owner, succ, s, (v, w))
print('games', games, 'non-maximum sigma with a single flat improvement (I1 fails for I = {(v,w)}):', cnt)
print('example', ex)
