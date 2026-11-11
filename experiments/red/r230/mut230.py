#!/usr/bin/env python3
"""L-RED 64 R230: genome mutation operators (copied from climb230.py, so that other climbs can import them). set_rng(r), mutate(G)."""
import copy, os, random
rng = random.Random(0); NMAX, DMAX = int(os.environ.get("NMAX", "16")), int(os.environ.get("DMAX", "3"))
def set_rng(r):
    global rng
    rng = r
def renum(G):                                       # keep option ids o[2] = global index, gates a permutation of 0..M-1
    i = 0
    for x in range(G["N"]):
        for o in G["opts"][x]: o[2] = i; i += 1
    M = i; g = [k for x in range(G["N"]) for k in G["gate"][x]]
    order = sorted(range(M), key=lambda j: g[j]); rk = {j: r for r, j in enumerate(order)}; j = 0
    for x in range(G["N"]):
        G["gate"][x] = [rk[j + k] for k in range(len(G["opts"][x]))]; j += len(G["opts"][x])
    G["br"] = (G["br"] + list(range(len(G["br"]), M)))[:M]; br = G["br"]; o2 = sorted(range(M), key=lambda j: br[j])
    G["br"] = [0] * M
    for r, j in enumerate(o2): G["br"][j] = r
    G["bp"] = (G["bp"] + [0] * M)[:M]; return G
def wtgt(G, x):
    lw = [y for y in range(G["N"]) if G["lev"][y] == G["lev"][x] - 1]
    return rng.choice(lw) if G["lev"][x] and lw else -1
def mutate(G):
    G = copy.deepcopy(G); N = G["N"]; r = rng.random(); x = rng.randrange(N); k = rng.randrange(len(G["opts"][x]))
    if r < 0.2: G["opts"][x][k][0] = wtgt(G, x)
    elif r < 0.45: G["opts"][x][k][1] = rng.choice(list(range(N)) + [-1])
    elif r < 0.6:
        y = rng.randrange(N); l = rng.randrange(len(G["opts"][y])); G["gate"][x][k], G["gate"][y][l] = G["gate"][y][l], G["gate"][x][k]
    elif r < 0.7:
        o = G["opts"][x][k][2]; G["bp"][o] ^= 1; M = len(G["br"]); j = rng.randrange(M); G["br"][o], G["br"][j] = G["br"][j], G["br"][o]
    elif r < 0.8: G["start"][x] = rng.randrange(len(G["opts"][x]))
    elif r < 0.88 and len(G["opts"][x]) < DMAX:
        G["opts"][x].append([wtgt(G, x), rng.choice(list(range(N)) + [-1]), 0]); G["gate"][x].append(10 ** 6 + rng.random())
    elif r < 0.94 and len(G["opts"][x]) > 1:
        del G["opts"][x][k]; del G["gate"][x][k]; G["start"][x] = min(G["start"][x], len(G["opts"][x]) - 1)
    elif N < NMAX:
        lv = rng.choice(sorted(set(G["lev"])) + [max(G["lev"]) + 1]); G["N"] += 1; G["lev"].append(lv); G["opts"].append([]); G["gate"].append([])
        G["opts"][N].append([wtgt(G, N), rng.choice(list(range(N + 1)) + [-1]), 0]); G["gate"][N].append(10 ** 6 + rng.random()); G["start"].append(0)
    return renum(G)
