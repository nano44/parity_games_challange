#!/usr/bin/env python3
"""L-SI box 84 milestone 2: adversarial climb for PRIV FAILURE. Genomes: rand191.rgen (cycles allowed) with every mover given a SET-type
option (Xi-target = itself, even beta). Score (lex): (max excess over non-PRIV units, max flips over non-PRIV units, T). Mutations: retarget
a Xi-target (any mover incl. self, or X), retarget a W-target (level - 1), swap two beta ranks, flip a beta parity, swap two gate
indices, change a start. Excess = flips - PRIV-FLIP's bound (priv84.measure); > 0 on a non-PRIV unit = PRIV failure beats the formula.
Usage: climb84.py SEED ITERS d w D OUT.json   (prints the best score as it improves)"""
import sys, os, json, random, copy
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
os.environ.setdefault("BOX81", os.path.join(HERE, "..", "..", "box81"))
import priv84, rand191
seed, iters, d, w, D, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
r = random.Random(seed)
def withset(G):
    M = sum(len(o) for o in G["opts"])
    for x in range(G["N"]):
        G["opts"][x].append([r.choice([y for y in range(G["N"]) if G["lev"][y] == G["lev"][x] - 1]) if G["lev"][x] else -1, x, M])
        G["br"].append(M); G["bp"].append(0); G["gate"][x].append(M); M += 1
    return G
def score(G):
    try: m = priv84.measure(G, cap=2000)
    except Exception: return (-99, 0, 0)
    return (m["maxex_nopriv"] if m["maxex_nopriv"] is not None else -99, m["maxfl_nopriv"], m["T"])
def mutate(G):
    G = copy.deepcopy(G); N = G["N"]; kind = r.randrange(6); x = r.randrange(N); k = r.randrange(len(G["opts"][x]))
    if kind == 0: G["opts"][x][k][1] = r.choice(list(range(N)) + [-1])
    elif kind == 1 and G["lev"][x]: G["opts"][x][k][0] = r.choice([y for y in range(N) if G["lev"][y] == G["lev"][x] - 1])
    elif kind == 2:
        i, j = r.randrange(len(G["br"])), r.randrange(len(G["br"])); G["br"][i], G["br"][j] = G["br"][j], G["br"][i]
    elif kind == 3: b = r.randrange(len(G["bp"])); G["bp"][b] ^= 1
    elif kind == 4:
        y = r.randrange(N); k2 = r.randrange(len(G["opts"][y])); G["gate"][x][k], G["gate"][y][k2] = G["gate"][y][k2], G["gate"][x][k]
    else: G["start"][x] = r.randrange(len(G["opts"][x]))
    return G
G = withset(rand191.rgen(r, d, w, D)); best = score(G)
for i in range(iters):
    H = mutate(G); s = score(H)
    if s >= best:
        if s > best: print(i, s, flush=True)
        G, best = H, s
json.dump(G, open(out, "w")); print("final", best)
