#!/usr/bin/env python3
"""box 156: hill-climbing search (DATA, lower bounds only) for deg <= 2 IDEAL-ACYC genomes with N movers maximising
OBJ = T (default) or M2 over ALL starts. Genome as in zmax.py (xorder = identity, ranks / gates over 2N options).
Usage: climb.py N SEED ITERS [OBJ] -> prints best and writes best_<OBJ>_N<N>_s<SEED>.json"""
import sys, json, random, itertools, copy
from val import ns
Gen = ns["Gen"]
N, seed, iters = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); OBJ = sys.argv[4] if len(sys.argv) > 4 else "T"
rng = random.Random(seed)
def rand_genome():
    while True:
        lev = [rng.randint(0, N - 1) for _ in range(N)]
        if set(lev) == set(range(max(lev) + 1)): break
    G = {"N": N, "lev": lev, "deg": [2] * N, "wt": [[-1, -1] for _ in range(N)], "xt": [[-1, -1] for _ in range(N)],
         "rk": rng.sample(range(2 * N), 2 * N), "sg": [rng.randint(0, 1) for _ in range(2 * N)], "gt": rng.sample(range(2 * N), 2 * N)}
    for x in range(N):
        for k in range(2): fix(G, x, k, True)
    return G
def fix(G, x, k, re=False):
    low = [v for v in range(N) if G["lev"][v] == G["lev"][x] - 1]
    if G["lev"][x] == 0: G["wt"][x][k] = -1
    elif re or G["wt"][x][k] not in low: G["wt"][x][k] = rng.choice(low)
    if re: G["xt"][x][k] = rng.choice([-1] + list(range(x + 1, N)))
def build(G):
    opts, gate, br, bp, idx = [], [], [], [], 0
    for x in range(N):
        o, g = [], []
        for k in range(G["deg"][x]):
            o.append([G["wt"][x][k], G["xt"][x][k], idx]); g.append(G["gt"][2 * x + k]); br.append(G["rk"][2 * x + k]); bp.append(G["sg"][2 * x + k]); idx += 1
        opts.append(o); gate.append(g)
    return {"N": N, "lev": list(G["lev"]), "opts": opts, "gate": gate, "br": br, "bp": bp, "start": [0] * N, "xorder": list(range(N))}
def score(G):
    H = build(G); g = Gen(H); best = (-1, None)
    for st in itertools.product(*[range(len(o)) for o in H["opts"]]):
        S, _ = g.run(list(st)); T = len(S) - 1
        mv = [sum(1 for v in range(N) if S[t][v] != S[t + 1][v]) for t in range(T)]
        M2 = sum(1 for c in mv[:-1] if c >= 2)
        val = (T, M2) if OBJ == "T" else (M2, T)
        if val > best[0] if best[0] != -1 else True: best = (val, list(st))
    return best
def mutate(G):
    G = copy.deepcopy(G); r = rng.random()
    if r < 0.15:
        x = rng.randrange(N); G["lev"][x] = rng.randint(0, N - 1)
        if set(G["lev"]) != set(range(max(G["lev"]) + 1)): return None
        for y in range(N):
            for k in range(2): fix(G, y, k)
    elif r < 0.3: x = rng.randrange(N); k = rng.randrange(2); G["xt"][x][k] = rng.choice([-1] + list(range(x + 1, N)))
    elif r < 0.45:
        x = rng.randrange(N); k = rng.randrange(2); low = [v for v in range(N) if G["lev"][v] == G["lev"][x] - 1]
        if low: G["wt"][x][k] = rng.choice(low)
    elif r < 0.6: i, j = rng.sample(range(2 * N), 2); G["rk"][i], G["rk"][j] = G["rk"][j], G["rk"][i]
    elif r < 0.7: i = rng.randrange(2 * N); G["sg"][i] ^= 1
    elif r < 0.85: i, j = rng.sample(range(2 * N), 2); G["gt"][i], G["gt"][j] = G["gt"][j], G["gt"][i]
    else: x = rng.randrange(N); G["deg"][x] = 3 - G["deg"][x]
    return G
cur = rand_genome(); cs = score(cur); best, bs = cur, cs
for it in range(iters):
    if it % 3000 == 2999 and rng.random() < 0.3: cur = rand_genome(); cs = score(cur)
    H = mutate(cur)
    if H is None: continue
    s = score(H)
    if s[0] >= cs[0] or rng.random() < 0.02: cur, cs = H, s
    if s[0] > bs[0]:
        best, bs = H, s; print(it, OBJ, "best (T,M2)" if OBJ == "T" else "best (M2,T)", bs[0], flush=True)
        B = build(best); B["start"] = bs[1]; json.dump(B, open(f"wit/best_{OBJ}_N{N}_s{seed}.json", "w"))
print("FINAL", N, OBJ, bs[0])
