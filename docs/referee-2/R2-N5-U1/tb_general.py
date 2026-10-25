#!/usr/bin/env python3
"""REFEREE-2: Lemma R and Lemma TB (P-N5-U1 §1-§2) on GENERAL random games (any number of Odd choice vertices; TB is stated for any
game). SPEC state sequence; Lemma R checked on every S4a dual-arena evaluation; TB at every non-fallback S4a transition.
Usage: tb_general.py N nmin nmax seed"""
import sys, random
from collections import Counter
import u1_check as U
RC = U.RC
def rand_general(rng, n):
    owner = [rng.randrange(2) for _ in range(n)]
    prio = [rng.randrange(0, n + 1) for _ in range(n)]
    succ = [rng.sample(range(n), rng.randint(1, 3)) for _ in range(n)]
    return RC.Game(prio, owner, succ)
N, nmin, nmax, seed = map(int, sys.argv[1:5]); rng = random.Random(seed)
st = RC.Stats(); st.mx = Counter()
for i in range(N):
    g = rand_general(rng, rng.randint(nmin, nmax))
    s, t = RC.rand_start(rng, g) if rng.random() < 0.5 else U.br_start(g)
    states, fbs, arenas = U.spec_run(g, None, s, t, st, f"gen{seed}#{i}")
    U.check_TB(g, None, states, fbs, arenas, st, f"gen{seed}#{i}")
    st.c["runs"] += 1; st.c["transitions"] += len(fbs); st.c["odd_choice_vertices"] += sum(1 for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) > 1)
U.report(st)
