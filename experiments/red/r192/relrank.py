#!/usr/bin/env python3
"""L-RED R192 RELRANK: for each unchained step t (r192/rkclimb definitions) the frozen movers above y_t (unstable at s_(t-1), pi > pi(y_t),
not moving at t), split into RELEASED-LATER (move at some later step) and PADDING (never move again). Prints per genome: U, the RANK
list, the RELRANK list (1 + #released-later), and the number of distinct padding movers. Usage: relrank.py genome.json ..."""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H]
import rkclimb, ideal
for f in sys.argv[1:]:
    G = json.load(open(f)); S, why = ideal.traj(G, cap=5000); N = G["N"]; pi = G["pi"]; lev = G["lev"]
    US = [rkclimb.unst(G, s) for s in S]; T = len(S) - 1
    mv = [None] + [set(v for v in range(N) if S[t][v] != S[t - 1][v]) for t in range(1, T + 1)]
    last = {v: max([t for t in range(1, T + 1) if v in mv[t]], default=0) for v in range(N)}
    least = [[v for v in mv[t] if lev[v] == min(lev[u] for u in mv[t])] for t in range(1, T + 1)]
    unch = [t for t in range(2, T + 1) if not (set(least[t - 2]) & set().union(*[rkclimb.chain(G, S[t - 1], h, S[t][h]) for h in least[t - 1]]))]
    R = []; RR = []; pad = set()
    for t in unch:
        y = max(mv[t], key=lambda v: pi[v]); fr = [x for x in range(N) if US[t - 1][x] and pi[x] > pi[y]]
        R.append(1 + len(fr)); RR.append(1 + sum(1 for x in fr if last[x] > t)); pad |= {x for x in fr if last[x] <= t}
    print(f"{os.path.basename(f)}: N {N} L {T} U {len(unch)} RANK {R} RELRANK {RR} padding movers {len(pad)}")
