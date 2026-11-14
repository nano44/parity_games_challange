#!/usr/bin/env python3
"""L-SI box 89: hill-climb for D_U at a real bit's waiting hub w (du89.du). Score (lex) = (max_l D_U(w_l), T). Mutations = L-RED 59's
climb225.py mutate() (claude/l-red 9d163251, experiments/red/r225/climb225.py; copied): Xi-targets anywhere (downward = carry routes),
W-targets, beta ranks / parities, gate swaps (e-relevance), start. The names file is kept, so du89 finds B_l and its SET option.
Usage: climb89.py BOX81DIR SEED GENOME.json ITERS OUTDIR"""
import sys, os, json, random, copy
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
B81, seed, f0, IT, OUT = sys.argv[1], int(sys.argv[2]), sys.argv[3], int(sys.argv[4]), sys.argv[5]
sys.argv = sys.argv[:2]; import du89
rng = random.Random(seed); os.makedirs(OUT, exist_ok=True)
def mutate(G):
    G = copy.deepcopy(G); N = G["N"]; lev = G["lev"]; r = rng.random()
    x = rng.randrange(N); k = rng.randrange(len(G["opts"][x]))
    if r < 0.3: G["opts"][x][k][1] = rng.choice(list(range(N)) + [-1, x])
    elif r < 0.45 and lev[x] >= 1: G["opts"][x][k][0] = rng.choice([y for y in range(N) if lev[y] == lev[x] - 1])
    elif r < 0.65:
        i, j = rng.randrange(len(G["br"])), rng.randrange(len(G["br"])); G["br"][i], G["br"][j] = G["br"][j], G["br"][i]
    elif r < 0.75: i = rng.randrange(len(G["bp"])); G["bp"][i] ^= 1
    elif r < 0.9:
        y = rng.randrange(N); k2 = rng.randrange(len(G["opts"][y])); G["gate"][x][k], G["gate"][y][k2] = G["gate"][y][k2], G["gate"][x][k]
    else: G["start"][x] = rng.randrange(len(G["opts"][x]))
    return G
nm = json.load(open(f0[:-5] + ".names.json"))
def score(G):
    try: T, NM, res = du89.du(G, nm)
    except Exception: return (-1, 0), None
    return (max(d for d, _ in res.values()), T), res
G = json.load(open(f0)); best, m = score(G); print("seed", best, m, flush=True); stem = os.path.basename(f0)[:-5]
for it in range(IT):
    H = mutate(G); sc, mm = score(H)
    if sc >= best:
        if sc > best:
            print(it, sc, mm, flush=True); json.dump(H, open(os.path.join(OUT, f"{stem}_du_{seed}.json"), "w")); json.dump(nm, open(os.path.join(OUT, f"{stem}_du_{seed}.names.json"), "w"))
        G, best = H, sc
print("final", best, flush=True)
