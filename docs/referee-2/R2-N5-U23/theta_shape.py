#!/usr/bin/env python3
"""REFEREE-2 §C: REFEREE's R-1 closure. Under not-H1 with c_theta != o, theta = (c_theta, {}, d) with d <= |R| - 1, and d moves
monotonically inside a phase, so a phase has <= n - 1 theta-changes there. Usage: theta_shape.py N nmin nmax seed [inst ...]"""
import sys, random
from collections import Counter
import u23_check as Z
U, RC = Z.U, Z.RC
c = Counter(); bad = []
def scan(g, o, s, t, name):
    st = RC.Stats(); st.mx = Counter()
    states, fbs, _ = U.spec_run(g, o, s, t, st, name, lemmaR=False)
    A = [RC.analyse(g, o, a, b) for a, b in states]
    for S in A: S.H1, S.H2 = U.H12(g, o, S)
    T = len(fbs); dirs = {}
    for k in range(T + 1):
        S = A[k]
        if not S.H1 and S.theta[0] != o:
            c["states"] += 1
            if S.theta[1] or S.theta[2] > len(S.R) - 1: bad.append((name, k, S.theta))
        if k < T and A[k].lamX == A[k + 1].lamX and A[k].lamU == A[k + 1].lamU and states[k][1] == states[k + 1][1] \
                and not A[k].H1 and not A[k + 1].H1 and A[k].theta[0] != o and A[k].theta != A[k + 1].theta:
            c["theta_changes"] += 1
            if A[k].theta[0] != A[k + 1].theta[0]: bad.append((name, k, "c_theta moved"))
            if g.cmp(A[k + 1].theta, A[k].theta) < 0: bad.append((name, k, "theta decreased"))
N, nmin, nmax, seed = map(int, sys.argv[1:5]); rng = random.Random(seed)
for i in range(N):
    g, o = RC.rand_game(rng, rng.randint(nmin, nmax)); U.one_odd(g)
    s, t = RC.rand_start(rng, g) if rng.random() < 0.5 else U.br_start(g); scan(g, o, s, t, f"r{i}")
for p in sys.argv[5:]:
    g = RC.parse(open(p).read()); o = U.one_odd(g); r2 = random.Random(3)
    for r in range(10):
        s, t = U.br_start(g) if r == 0 else RC.rand_start(r2, g); scan(g, o, s, t, p)
print(dict(c), "violations", bad[:10]); print("RESULT", "FAIL" if bad else "OK")
