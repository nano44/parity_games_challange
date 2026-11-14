#!/usr/bin/env python3
"""rtest13.py COUNT SEED NMAX mode... : n13 against harness Zielonka (regions) and harness verify.py (both strategies)."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'harness'))

import gen, zielonka, verify
import n13
count, seed, nmax = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
modes = sys.argv[4:] or ['alt+']
rnd = gen.Rng('rtest13|%d' % seed)
res = {m: dict(wrong=0, badstrat=0, cap=0, jumps=0, maxj=0) for m in modes}
for i in range(count):
    n = rnd.randint(1, nmax); d = rnd.randint(1, max(1, min(n + 1, 14)))
    dmax = rnd.randint(1, min(n, 5)); peven = rnd.choice([0.2, 0.5, 0.8])
    g = gen.random_game(n, d, 1, dmax, 'r13|%d|%d' % (seed, i), peven=peven, selfloops=rnd.random() < 0.7)
    ref = zielonka.solve(g)
    for m in modes:
        R = n13.solve(g.n, g.owner, g.prio, [sorted(set(s)) for s in g.succ], m, cap=20000)
        r = res[m]
        if R.status != 'done': r['cap'] += 1; continue
        if R.win != ref: r['wrong'] += 1; continue
        if verify.check(g, R.win, R.strat): r['badstrat'] += 1; continue
        r['jumps'] += R.jumps; r['maxj'] = max(r['maxj'], R.jumps)
print('games', count, 'seed', seed, 'nmax', nmax)
for m in modes: print(m, res[m])
