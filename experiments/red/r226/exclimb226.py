#!/usr/bin/env python3
"""L-RED 60 R226: adversarial climb against CONJECTURE SHARP2: in every LEAPFROG-ASC unit (PRIV + NODE) with |E_U| >= 2,
#events <= |E_U| - 1. Score = (max over such units of ev - |E_U|, max ev). Mutations = climb225's. Restarts from latch225.rgen.
Freezes any genome with score >= 0 to out/sharp2wit_SEED_R.json. Usage: exclimb226.py SEED RESTARTS ITER"""
import sys, os, json, random, copy
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r225"), os.path.join(H, "..", "r221")]
import exshow226 as ex, latch225
ex.THR = -10 ** 9
seed, R, IT = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); rng = random.Random(seed)
def score(G):
    ex.DUMP.clear()
    try: ex.census(G, 400)
    except Exception: return (-99, 0)
    u = [d for d in ex.DUMP if len(d["EU"]) >= 2]
    return max(((len(d["ev"]) - len(d["EU"]), len(d["ev"])) for d in u), default=(-99, 0))
def score2(G):    # DUMP holds only units with excess >= 0; compute excess for all hyp units via a lowered threshold
    return score(G)
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
best_all = (-99, 0)
for rr in range(R):
    G = latch225.rgen(rng); s = score(G)
    for it in range(IT):
        Hh = mutate(G); s2 = score(Hh)
        if s2 >= s: G, s = Hh, s2
        if s[0] >= 0: break
    if s > best_all: best_all = s
    if s[0] >= 0: json.dump(G, open(f"out/sharp2wit_{seed}_{rr}.json", "w")); print("WIT", rr, s, flush=True)
    print("R", rr, s, "best", best_all, flush=True)
print("FINAL", seed, best_all, flush=True)
