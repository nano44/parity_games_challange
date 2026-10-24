#!/usr/bin/env python3
"""REFEREE-2: Lemma TB (P-N5-U1 §2) and Lemma R (§1) directly on one-player arenas, independent of N5's state sequence.
Random game, random Odd strategy tau, random Even strategy sigma_k, random arena A(v) containing sigma_k(v) (sorted, as n5.py passes
sorted(opt[v])). sigma_{k+1} = the optimiser's counterstrategy of ONE Engine.evaluate call on the dual of the arena (exactly n5.py's
S4a call). Checks TB-key, TB-odd, TB-even, step 2, Lemma R; transitions are all "non-fallback" (sigma_{k+1} != sigma_k required
only for the switch clauses). Odd-mode bias: priorities drawn so that odd cycle nodes are frequent.
Usage: tb_arena.py N nmin nmax seed"""
import sys, random
from collections import Counter
import u1_check as U
RC = U.RC; lpg = U.lpg; n5 = U.n5; Engine = U.Engine
N, nmin, nmax, seed = map(int, sys.argv[1:5]); rng = random.Random(seed)
st = RC.Stats(); st.mx = Counter()
for i in range(N):
    n = rng.randint(nmin, nmax)
    owner = [1 if rng.random() < 0.3 else 0 for _ in range(n)]
    prio = [rng.randrange(0, 2 * n) | (1 if rng.random() < 0.6 else 0) for _ in range(n)]
    succ = [rng.sample(range(n), rng.randint(1, 4)) for _ in range(n)]
    g = RC.Game(prio, owner, succ)
    tau = [rng.choice(g.succ[v]) for v in range(n)]; sig = [rng.choice(g.succ[v]) for v in range(n)]
    A = {v: sorted({sig[v]} | set(rng.sample(g.succ[v], rng.randint(0, len(g.succ[v]))))) for v in range(n) if owner[v] == 0}
    hs = [A[v] if owner[v] == 0 else [tau[v]] for v in range(n)]
    Er = Engine(n5.dual(lpg.Game(list(prio), list(owner), hs)))
    strat = tuple(tau[v] if owner[v] == 1 else -1 for v in range(n))
    _, best = U.check_lemma_R(Er, strat, st, f"ar{seed}#{i}")
    s1 = [best[v] if owner[v] == 0 else sig[v] for v in range(n)]
    U.check_TB(g, None, [(sig, tau), (s1, tau)], [0], [A], st, f"ar{seed}#{i}")
    st.c["arenas"] += 1
U.report(st)
