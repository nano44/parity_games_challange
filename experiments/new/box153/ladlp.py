#!/usr/bin/env python3
"""L-NEW box 153: longest improving (single-switch) path in the decomposable AUSO of a 2-wide Xi-LADDER (pairs j = 0..K-1; each mover of
pair j has its two options to the two movers of pair j+1; last pair to X), climbing over ranks, parities, start (structure fixed).
Usage: ladlp.py K ITERS SEED"""
import sys, os, json, random
H = os.path.dirname(os.path.abspath(__file__)); sys.argv_ = sys.argv; K, IT, SEED = map(int, sys.argv[1:4])
sys.argv = [sys.argv[0]]; ns = {"__file__": os.path.join(H, "longpath.py")}
exec(open(os.path.join(H, "longpath.py")).read().split("if os.environ.get(\"CLIMB\")")[0], ns); analyse = ns["analyse"]
rng = random.Random(SEED); N = 2 * K; M = 2 * N
def mk():
    opts = []; m = 0
    for x in range(N):
        j = x // 2
        t = [2 * j + 2, 2 * j + 3] if j < K - 1 else [-1, -1]
        if rng.random() < 0.5: t = t[::-1]
        opts.append([[-1, t[0], m], [-1, t[1], m + 1]]); m += 2
    return {"N": N, "lev": [0] * N, "opts": opts, "gate": [[2 * x, 2 * x + 1] for x in range(N)], "br": rng.sample(range(M), M),
            "bp": [rng.randint(0, 1) for _ in range(M)], "start": [rng.randint(0, 1) for _ in range(N)], "xorder": list(range(N))}
G = mk(); sc = analyse(G)[1]
for it in range(IT):
    H2 = json.loads(json.dumps(G)); r = rng.random()
    if r < 0.5: i, j = rng.sample(range(M), 2); H2["br"][i], H2["br"][j] = H2["br"][j], H2["br"][i]
    elif r < 0.75: H2["bp"][rng.randrange(M)] ^= 1
    else: H2["start"][rng.randrange(N)] ^= 1
    s2 = analyse(H2)[1]
    if s2 >= sc: G, sc = H2, s2
print(f"LADLP K {K} n {N} longest {sc}"); json.dump(G, open(f"/tmp/claude-0/ladlp_{K}.json", "w"))
