#!/usr/bin/env python3
"""L-RED 56 R221 (copy in r221p with SCORE=post): hill-climb toward LADDER genomes. Score (lexicographic) = (min(asc, K), R, T) with asc = max ascents of any play
over the run (lad221.meas), R = sigma-bar change steps (own.py labels). Mutations: Xi-target -> any mover or X (-1) (upward allowed),
W-target -> a mover one level lower (or -1 at level 0), swap two beta ranks, flip a beta parity, swap two gate indices, change a start.
Seed: lad221.lad(k) (mode lad) or random levels 0..d-1 with w movers each and D options (mode rnd).
Env SCORE=post (r221p): score = (#fallbacks, post-fallback iterations, post-fallback mover changes, xi) of N5'-xi on Gamma3 (post221).
Env SCORE=rho: score = (RHO-SET + RHO-E violations, max rho at a SET gate, R, T) (rho221.census).
Env SCORE=reent: score = (max re-entries at one (v, Lambda-interval), min(asc, K), T) instead.
Usage: ladclimb.py SEED MODE(lad|rnd) k_or_d w D K ITER OUT.json"""
import sys, os, random, json, copy
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lad221
seed, mode, p1, w, D, K, IT, OUT = int(sys.argv[1]), sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]), int(sys.argv[7]), sys.argv[8]
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
    try: m = lad221.meas(G, cap=3000)
    except Exception: return (-1, 0, 0, 0), None
    if os.environ.get("SCORE") == "post":
        import post221
        try: r = post221.post(G, cap=3000)
        except Exception: return (-1, 0, 0, 0), None
        m.update(r); return (r["fb"], sum(r["phases"][1:]), r["Mpost"], r["xi"]), m
    if os.environ.get("SCORE") == "rho":
        import rho221
        try: r = rho221.census(G)
        except Exception: return (-1, 0, 0, 0), None
        m.update(r); return (r["gapv"] + r["viol"], r["maxset"], m["R"], m["T"]), m
    if os.environ.get("SCORE") == "reent": return (m["reent"], min(m["asc"], K), m["T"]), m
    return (min(m["asc"], K), m["R"], m["T"]), m
def mutate(G):
    G = copy.deepcopy(G); N = G["N"]; lev = G["lev"]; r = rng.random()
    x = rng.randrange(N); k = rng.randrange(len(G["opts"][x]))
    if r < 0.3: G["opts"][x][k][1] = x if (os.environ.get("SCORE") == "rho" and rng.random() < 0.3) else rng.choice(list(range(N)) + [-1])
    elif r < 0.45 and lev[x] >= 1: G["opts"][x][k][0] = rng.choice([y for y in range(N) if lev[y] == lev[x] - 1])
    elif r < 0.65:
        i, j = rng.randrange(len(G["br"])), rng.randrange(len(G["br"])); G["br"][i], G["br"][j] = G["br"][j], G["br"][i]
    elif r < 0.75: i = rng.randrange(len(G["bp"])); G["bp"][i] ^= 1
    elif r < 0.9:
        y = rng.randrange(N); k2 = rng.randrange(len(G["opts"][y])); G["gate"][x][k], G["gate"][y][k2] = G["gate"][y][k2], G["gate"][x][k]
    else: G["start"][x] = rng.randrange(len(G["opts"][x]))
    return G
G = lad221.lad(p1) if mode == "lad" else rnd(p1, w, D); best, m = score(G)
for it in range(IT):
    H = mutate(G); s, mm = score(H)
    if s >= best:
        if s > best: json.dump(H, open(OUT, "w")); print(it, s, mm, flush=True)
        G, best = H, s
print("final", best, flush=True)
