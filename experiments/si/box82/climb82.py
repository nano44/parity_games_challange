#!/usr/bin/env python3
"""L-SI box 82 (draft): hill-climb on L^R_d genomes (2 movers per level, degree 2, R104 / R110 layout, Xi-targets ANY mover or X, cycles
allowed) maximising (R, T) of the IDEAL-CYC Howard run (R118 labels; ref/ idealcyc + si.py Engine). Mutations: one Xi-target, a swap of
two beta-ranks, a parity bit, a swap of two gate indices, a start bit. Accept if (R, T) does not decrease.
Usage: climb82.py d SEED ITERS BOX81DIR [START.json]   prints the best (R, T) per improvement and writes best_d<d>_s<SEED>.json"""
import sys, os, json, random, copy
d, seed, iters, B81 = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
sys.path[:0] = [B81, os.path.join(B81, "ref", "experiments", "new", "box191")]
import idealcyc
rng = random.Random(seed)


def rand_genome(d):
    N = 2 * d; M = 2 * N; opts = []
    for x in range(N):
        l = x // 2; row = []
        for k in range(2):
            w = 2 * (l - 1) + k if l >= 1 else -1
            xt = -1 if rng.random() < 0.25 else rng.choice([y for y in range(N) if y != x])
            row.append([w, xt, 2 * x + k])
        opts.append(row)
    br = list(range(M)); rng.shuffle(br); bp = [rng.randrange(2) for _ in range(M)]
    g = list(range(M)); rng.shuffle(g)
    return dict(N=N, lev=[x // 2 for x in range(N)], deg=2, opts=opts, gate=[[g[2 * x], g[2 * x + 1]] for x in range(N)], br=br, bp=bp,
                start=[rng.randrange(2) for _ in range(N)])


OBJ = os.environ.get("OBJ", "R")


def kflips(G, st):
    N = G["N"]; d = N // 2
    def order(s):
        K = [None] * N
        for x in range(N):
            w = G["opts"][x][s[x]][0]; g = G["gate"][x][s[x]]; K[x] = (g,) if w < 0 else K[w] + (g,)
        return [int(K[2 * j] < K[2 * j + 1]) for j in range(d)]
    O = [order(s) for s in st]
    return [sum(O[t][j] != O[t - 1][j] for t in range(1, len(O))) for j in range(d)]


def capped(F):
    h = 0
    while h < len(F) and F[h] == 2 ** (h + 2) - 2: h += 1
    return h


def score(G):
    h, s0, movers, inv = idealcyc.build(G); E = idealcyc.Engine(h); st = idealcyc.run(G, cap=5000)
    gi = {}
    for x in range(G["N"]):
        for v in h.succ[movers[x]]: gi[(x, inv[v])] = v
    prev = None; R = C = 0
    for s in st:
        cur = list(s0)
        for x in range(G["N"]): cur[movers[x]] = gi[(x, s[x])]
        vs, sb = E.evaluate(tuple(cur)); key = ([vs[v][0] for v in range(h.n)], [sb[v] for v in range(h.n) if h.owner[v] == 1])
        if prev is not None:
            if key[0] != prev[0]: C += 1
            elif key[1] != prev[1]: R += 1
        prev = key
    if OBJ == "kf":
        F = kflips(G, st); h = capped(F)
        nxt = F[h] if h < len(F) else 0
        return (h, min(nxt, 2 ** (h + 2) - 2), R, len(st) - 1), C
    return (R, len(st) - 1), C


def mutate(G):
    H = copy.deepcopy(G); N = H["N"]; M = 2 * N; c = rng.randrange(5)
    if c == 0:
        x, k = rng.randrange(N), rng.randrange(2); H["opts"][x][k][1] = -1 if rng.random() < 0.2 else rng.choice([y for y in range(N) if y != x])
    elif c == 1:
        a, b = rng.sample(range(M), 2); H["br"][a], H["br"][b] = H["br"][b], H["br"][a]
    elif c == 2:
        a = rng.randrange(M); H["bp"][a] ^= 1
    elif c == 3:
        xa, ka, xb, kb = rng.randrange(N), rng.randrange(2), rng.randrange(N), rng.randrange(2)
        H["gate"][xa][ka], H["gate"][xb][kb] = H["gate"][xb][kb], H["gate"][xa][ka]
    else:
        x = rng.randrange(N); H["start"][x] ^= 1
    return H


G = json.load(open(sys.argv[5])) if len(sys.argv) > 5 else rand_genome(d)
best, C = score(G)
print("start", best, "C", C, flush=True)
for i in range(iters):
    H = mutate(G); s, c = score(H)
    if s >= best:
        if s > best: print("iter", i, "score", s, "C", c, flush=True)
        G, best = H, s
json.dump(G, open(f"best_{OBJ}_d{d}_s{seed}.json", "w"))
print("final d", d, "seed", seed, "OBJ", OBJ, "score", best)
