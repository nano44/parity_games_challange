#!/usr/bin/env python3
"""L-RED 59 R225: hill-climb for long N5'-xi runs on IDEAL-CYC (own.py Howard, [E-LEV]); score = (T, SD1) with SD1 =
Sigma_v (D^tot_E(v) - 1) (sig225.sig). By Lemma EQUIV (R225 §1) T and SD1 are polynomially equivalent, so T is the score.
Mutations as R221 ladclimb (Xi-target -> any mover or X, upward and cyclic allowed; W-target; beta rank swap / parity flip; gate swap;
start). Seed: random genome, levels 0..d-1, w movers per level, D options; or a JSON genome (mode file:PATH).
Usage: climb225.py SEED MODE(rnd|file:PATH) d w D ITER OUT.json"""
import sys, os, random, json, copy
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sig225
seed, mode, d, w, D, IT, OUT = int(sys.argv[1]), sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]), sys.argv[7]
rng = random.Random(seed)
def rnd(d, w, D):
    N = d * w; lev = [x // w for x in range(N)]; opts = []
    for x in range(N):
        opts.append([[(rng.choice([y for y in range(N) if lev[y] == lev[x] - 1]) if lev[x] else -1), rng.choice(list(range(N)) + [-1]), 0] for _ in range(D)])
    M = N * D; perm = list(range(M)); rng.shuffle(perm); gate = []; i = 0
    for x in range(N):
        gate.append([])
        for o in opts[x]: o[2] = i; gate[x].append(perm[i]); i += 1
    br = list(range(M)); rng.shuffle(br)
    return {"N": N, "lev": lev, "opts": opts, "gate": gate, "br": br, "bp": [rng.randrange(2) for _ in range(M)], "start": [rng.randrange(D) for _ in range(N)]}
def score(G):
    try: r, _ = sig225.sig(G, cap=3000)
    except Exception: return (-1, 0), None
    return (r["T"], r["SD1"]), r
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
G = json.load(open(mode[5:])) if mode.startswith("file:") else rnd(d, w, D); best, m = score(G)
print("seed", best, m, flush=True)
for it in range(IT):
    H = mutate(G); s, mm = score(H)
    if s >= best:
        if s > best: json.dump(H, open(OUT, "w")); print(it, s, mm, flush=True)
        G, best = H, s
print("final", best, flush=True)
