#!/usr/bin/env python3
"""L-LOWER 6: structure of the «48 of 127» level-6 plateau across genomes: T, caps, F(6), level-6 window move profile, pair 6's
Ξ-targets (crossed or not), the movers graph-upstream of 12, 13 (whose Ξ-closure reaches pair 6), and whether 10 (pair 5's
second mover) is among them (RETURN-CHAIN). Usage: struct48.py genome.txt ..."""
import sys
from collections import Counter
from sim6 import rd, run, Fprof, caps
for p in sys.argv[1:]:
    D = rd(p); xt = D['xt']; N = 2 * D['d']; S, O = run(D); T = len(S) - 1; F = Fprof(D, O)
    b = [t for t in range(1, T + 1) if O[t][5] != O[t-1][5]]; cuts = [1] + b + [T + 1]
    prof = Counter(tuple(sorted(x for t in range(a, e) for x in (12, 13) if S[t][x] != S[t-1][x])) for a, e in zip(cuts, cuts[1:]))
    pred = {y: [m // 2 for m in range(2 * N) if xt[m] == y] for y in range(N)}; U = {12, 13}; st = [12, 13]
    while st:
        y = st.pop()
        for x in pred[y]:
            if x not in U: U.add(x); st.append(x)
    cr = xt[24] == xt[27] and xt[25] == xt[26] and xt[24] != xt[25]
    print(p.split('/')[-1], f"T {T} caps {caps(F)} F6 {F[6]} windows {len(cuts)-1} profile {dict(prof)} pair6 12->{xt[24:26]} 13->{xt[26:28]} "
          f"crossed {cr} upstream(12,13) {sorted(U)} 10-upstream {10 in U} 11-upstream {11 in U}")
