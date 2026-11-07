#!/usr/bin/env python3
"""L-SI box 78: RESULTS R105 RANK on given genomes (stored start). pi := Kahn topological order of the Xi-graph from the sources
(pi(x) < pi(xt(x, k)): a mover's value depends on its targets, so by R105 DECREMENT no mover with larger pi than y_t changes),
y_t := the largest-pi mover of step t, unstable := c_s(x) >= 1, RANK_t := 1 + #(unstable movers with pi > pi(y_t) before step t).
Prints T, max RANK, the RANK histogram, and R105 RANK-BOUND's bound sum_(j <= Rmax) C(N, j) - 1 (over all steps, a weaker use)."""
import sys, os, json, collections
from math import comb
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(H, "..", "box76"))
from tw import Sim, analyse, is_lr
for f in sys.argv[1:]:
    G = json.load(open(f)); assert is_lr(G); N = G["N"]; sim = Sim(G)
    indeg = [0] * N
    for x in range(N):
        for k in range(2):
            y = G["opts"][x][k][1]
            if y >= 0: indeg[y] += 1
    order = []; av = sorted(x for x in range(N) if indeg[x] == 0)
    while av:
        x = av.pop(0); order.append(x)
        for k in range(2):
            y = G["opts"][x][k][1]
            if y >= 0:
                indeg[y] -= 1
                if indeg[y] == 0: av.append(y)
    pi = {x: i for i, x in enumerate(order)}
    S = sim.run(tuple(G["start"])); T = len(S) - 1
    hist = collections.Counter(); R = []
    for t in range(1, T + 1):
        s = S[t - 1]; mv = [x for x in range(N) if S[t][x] != s[x]]; y = max(mv, key=lambda x: pi[x])
        unst = [x for x in range(N) if any(sim.val(s, x, k) > sim.val(s, x, s[x]) for k in range(2))]
        r = 1 + sum(1 for x in unst if pi[x] > pi[y]); R.append(r); hist[r] += 1
    rm = max(R) if R else 0
    print("%s N %d T %d maxRANK %d hist %s RANK-BOUND sum_(j<=%d) C(N,j)-1 = %d" % (os.path.basename(f), N, T, rm, dict(sorted(hist.items())), rm, sum(comb(N, j) for j in range(1, rm + 1)) - 1))
