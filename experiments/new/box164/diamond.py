#!/usr/bin/env python3
"""control: longest SINGLE-switch improving path (no keys) on the 2-wide diamond Xi-DAG (layers 1..n, movers a_i, b_i, both options of a
layer-i mover point to a_(i+1) resp. b_(i+1); layer n to the exit), hill-climbed over ranks / parities. Prints longest path L and mu_free.
Usage: diamond.py n iters seed"""
import os, sys, json, random, copy
H = os.path.dirname(os.path.abspath(__file__)); os.environ["SINGLE"] = "1"
exec(open(os.path.join(H, "keyless.py")).read().split("\nif __name__")[0])
sys.setrecursionlimit(100000)
n, iters, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); rng = random.Random(seed); N = 2 * n
opts = []; M = 0
for x in range(N):
    i = x // 2; o = []
    for k in range(2):
        o.append([-1, 2 * (i + 1) + k if i + 1 < n else -1, M]); M += 1
    opts.append(o)
G = {"N": N, "lev": [0] * N, "opts": opts, "gate": [[0, 1]] * N, "br": list(range(M)), "bp": [rng.randint(0, 1) for _ in range(M)],
     "start": [0] * N, "xorder": list(range(N))}
rng.shuffle(G["br"]); L, mu, _ = analyse(G); best = (L, mu)
for it in range(iters):
    G2 = copy.deepcopy(G)
    if rng.random() < 0.5: i, j = rng.sample(range(M), 2); G2["br"][i], G2["br"][j] = G2["br"][j], G2["br"][i]
    else: G2["bp"][rng.randrange(M)] ^= 1
    L2, mu2, _ = analyse(G2)
    if (L2, mu2) >= best: G, best = G2, (L2, mu2)
json.dump(G, open(os.path.join(H, "out", "diamond_n%d_L%d.json" % (n, best[0])), "w"))
print("DIAMOND n %d N %d records<=N*M=%d : longest single-switch path %d, mu_free %d" % (n, N, N * M, best[0], best[1]))
