#!/usr/bin/env python3
"""climb.py n d seed evals mode: hill-climb games with n vertices for the number of jumps of alt.py; prints best and saves it."""
import sys, random
import os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'harness'))
import zielonka, pg, n13
n, d, seed, evals, mode = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
rnd = random.Random(seed)
def rand_game():
    prio = [rnd.randrange(d) for _ in range(n)]; owner = [rnd.randrange(2) for _ in range(n)]
    succ = [sorted(rnd.sample(range(n), rnd.randint(1, 3))) for _ in range(n)]
    return prio, owner, succ
def fit(G):
    prio, owner, succ = G
    R = n13.solve(n, owner, prio, succ, mode, cap=5000)
    return (10 ** 9 if R.status != 'done' else R.jumps), R.win, R.status
def mutate(G):
    prio, owner, succ = list(G[0]), list(G[1]), [list(s) for s in G[2]]
    for _ in range(rnd.randint(1, 3)):
        v = rnd.randrange(n); r = rnd.random()
        if r < 0.3: prio[v] = rnd.randrange(d)
        elif r < 0.4: owner[v] ^= 1
        elif r < 0.7:
            u = rnd.randrange(n)
            if u in succ[v]:
                if len(succ[v]) > 1: succ[v].remove(u)
            else: succ[v] = sorted(succ[v] + [u])
        else:
            i = rnd.randrange(len(succ[v])); u = rnd.randrange(n)
            if u not in succ[v]: succ[v][i] = u; succ[v].sort()
    return prio, owner, succ
best = rand_game(); bf, _, _ = fit(best)
for e in range(evals):
    c = mutate(best); f, win, st = fit(c)
    if f >= bf:
        if f > bf: print('eval', e, 'jumps', f, flush=True)
        best, bf = c, f
    if e % 500 == 499 and rnd.random() < 0.0: pass
g = pg.Game(best[0], best[1], best[2])
ref = zielonka.solve(g); f, win, st = fit(best)
pg.write(g, 'c13_n%d_d%d_s%d_%s.pg' % (n, d, seed, mode.replace('+', 'p').replace('-', 'm')))
print('BEST n', n, 'd', d, 'seed', seed, mode, 'jumps', bf, st, 'regions', 'OK' if win == ref else 'MISMATCH')
