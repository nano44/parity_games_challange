#!/usr/bin/env python3
"""B5: replay of b5lemma.py rand seed 5101 item 313 (the NULL second fallback instance of the DEAD END in docs/red-b/B5-second-fb.md),
written to data/b5/null2_s5101_i313_n3.pg. Run from experiments/red-b with work/b3 built (B3-guide.md §6); CORE high (default)."""
import sys, os, random
sys.argv=[sys.argv[0],'work/b3']
sys.path.insert(0,os.getcwd())
import b5lemma as L
rng = random.Random(5101)
for i in range(314):
    n = rng.randint(2, 10); H = L.rand_H(rng, n)
    s0 = [rng.choice(H.succ[v]) if H.owner[v] == 0 else -1 for v in range(n)]
    rho0 = {v: (rng.choice(H.succ[v]) if rng.random() < 0.5 else rng.randrange(n)) for v in range(n) if H.owner[v] == 1}
    gamma = {(v, w): rng.randrange(n) for v in range(n) if H.owner[v] == 0 for w in H.succ[v] if rng.random() < 0.3}
    copy = rng.random() < 0.5
g = L.build(H, s0, rho0, gamma, copy)[0]
L.pg.write(g, 'data/b5/null2_s5101_i313_n3.pg')
