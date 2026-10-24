#!/usr/bin/env python3
"""REFEREE-2: DATA for the §3 READING note. Per crossing-free interval (in phase, R constant) under not-H1: number of theta-changes,
and how many of them happen at transitions with no F-change (so neither TF nor F1 counts them). Usage: theta_notH1.py N nmin nmax seed"""
import sys, random
from collections import Counter
import u23_check as Z
U, RC = Z.U, Z.RC
N, nmin, nmax, seed = map(int, sys.argv[1:5]); rng = random.Random(seed); c = Counter(); mx = 0
for i in range(N):
    g, o = RC.rand_game(rng, rng.randint(nmin, nmax)); U.one_odd(g)
    s, t = RC.rand_start(rng, g) if rng.random() < 0.5 else U.br_start(g)
    st = RC.Stats(); st.mx = Counter()
    states, fbs, _ = U.spec_run(g, o, s, t, st, "x", lemmaR=False)
    A = [RC.analyse(g, o, a, b) for a, b in states]
    for S in A: S.H1, S.H2 = U.H12(g, o, S)
    T = len(fbs); k = 0
    while k <= T:
        j = k
        while j < T and A[j].lamX == A[j + 1].lamX and A[j].lamU == A[j + 1].lamU and states[j][1] == states[j + 1][1] and A[j].R == A[j + 1].R: j += 1
        if not A[k].H1 and A[k].theta[0] != o:
            F = [v for v in range(g.n) if v not in A[k].R]
            th = sum(1 for x in range(k, j) if A[x].theta != A[x + 1].theta)
            thnoF = sum(1 for x in range(k, j) if A[x].theta != A[x + 1].theta and all(A[x].Xi[v] == A[x + 1].Xi[v] for v in F))
            c["intervals_notH1_cth_ne_o"] += 1; c["theta_changes"] += th; c["theta_changes_without_F_change"] += thnoF; mx = max(mx, th)
        k = j + 1
print(dict(c), "max theta-changes in one interval", mx)
