#!/usr/bin/env python3
"""random agreement test for n12.py: rtest.py COUNT SEED NMAX variant...  variant = policy[+flags], flags: n61 n62 n64 nopeel lazy literal"""
import sys
import os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'harness'))
import gen, zielonka, verify, pg
import n12 as n12e
count, seed, nmax = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
variants = sys.argv[4:] or ['duet']
rnd = gen.Rng('rtest|%d' % seed)
bad = {v: 0 for v in variants}; tot = {v: [0, 0, 0] for v in variants}
for i in range(count):
    n = rnd.randint(1, nmax); d = rnd.randint(1, max(1, min(n + 1, 12)))
    dmax = rnd.randint(1, min(n, 4)); peven = rnd.choice([0.2, 0.5, 0.8])
    g = gen.random_game(n, d, 1, dmax, 'r%d|%d' % (seed, i), peven=peven, selfloops=rnd.random() < 0.7)
    ref = zielonka.solve(g)
    for var in variants:
        parts = var.split('+')
        kw = dict(policy=parts[0], opt61='n61' not in parts, opt62='n62' not in parts, opt64='n64' not in parts,
                  peel='nopeel' not in parts, lazy='lazy' in parts, literal='literal' in parts)
        S = n12e.Solver(g.n, g.owner, g.prio, [sorted(set(s)) for s in g.succ], **kw)
        try:
            plus, minus, strat = S.solve()
        except AssertionError as e:
            bad[var] += 1; print('FAIL', var, i); continue
        win = [0 if v in plus else 1 for v in range(g.n)]
        if win != ref:
            bad[var] += 1; print('FAIL', var, i); continue
        errs = verify.check(g, win, [s if s >= 0 else None for s in strat])
        if errs:
            bad[var] += 1; print('FAIL', var, i); continue
        tot[var][0] += S.st.calls; tot[var][1] = max(tot[var][1], S.st.calls); tot[var][2] += S.st.work
print('games', count, 'bad', bad)
print({v: tuple(t) for v, t in tot.items()})
