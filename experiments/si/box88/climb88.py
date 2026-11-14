#!/usr/bin/env python3
"""L-SI box 88: hill-climb for NESTED type-II SET flips. Score (lex) = (maxk, maxev, maxdepth) from leap88.census over EVERY SET-type
option (ALL mode: Xi-target = own mover). Mutations = L-RED 59's climb225.py mutate() (claude/l-red 9d163251,
experiments/red/r225/climb225.py; copied, not edited): Xi-target, W-target, beta rank swap, parity flip, gate swap, start.
Any genome with chargefail > 0 (EVENT-CHARGE, docs/si/box88-nest.md §2) or ascfail > 0 is saved to OUTDIR/viol_*.json.
Usage: climb88.py BOX81DIR SEED GENOME.json ITERS OUTDIR"""
import sys, os, json, random, copy
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import leap88
B81, seed, f0, IT, OUT = sys.argv[1], int(sys.argv[2]), sys.argv[3], int(sys.argv[4]), sys.argv[5]
leap88.setup(B81); rng = random.Random(seed); os.makedirs(OUT, exist_ok=True)
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
def score(G):
    try: U, T = leap88.census(G, None, True)
    except Exception: return (-1, 0, 0), None
    s = leap88.summary(U); s["T"] = T
    return (s["maxk"], s["maxev"], s["maxdepth"]), s
G = json.load(open(f0)); best, m = score(G); nv = 0
print("seed", best, m, flush=True)
for it in range(IT):
    H = mutate(G); sc, mm = score(H)
    if mm and (mm["chargefail"] or mm["ascfail"]):
        nv += 1; json.dump(H, open(os.path.join(OUT, f"viol_{seed}_{it}.json"), "w")); print("VIOL", it, mm, flush=True)
    if sc >= best:
        if sc > best: json.dump(H, open(os.path.join(OUT, f"best_{seed}.json"), "w")); print(it, sc, mm, flush=True)
        G, best = H, sc
print("final", best, "violations", nv, flush=True)
