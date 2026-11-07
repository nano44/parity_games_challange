#!/usr/bin/env python3
"""L-RED 55 R219: hill-climb over NOUP genomes (every Xi-target is X (-1) or a mover of level <= the option's mover level), score = max
flips at one gate of level >= 1 (own.py run), ties broken by T. Mutations keep NOUP: retarget a Xi-target (same/lower level or X),
retarget a W-target (a mover of level lev - 1), swap two beta ranks, flip a beta parity, swap two gate indices, change a start.
Start: a random NOUP genome (L-NEW noup193.rgen_noup). Writes the best genome to OUT.json after each improvement.
Usage: WT193=<dir> noupclimb.py SEED d w D ITER OUT.json"""
import sys, os, random, json, copy
W = os.environ["WT193"]
for sub in ("box193", "box191", "box189"): sys.path.insert(0, os.path.join(W, "experiments/new", sub))
import noup193
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import own
seed, d, w, D, IT, OUT = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
rng = random.Random(seed)
def score(G):
    try: out, V, O, ow = own.run(G, cap=5000)
    except Exception: return (-1, 0)
    fl = max([sum(out[t][2][V[("g", q)]] != out[t - 1][2][V[("g", q)]] for t in range(1, len(out))) for q in O if G["lev"][q[0]] >= 1] or [0])
    return (fl, len(out) - 1)
def mutate(G):
    G = copy.deepcopy(G); N = G["N"]; lev = G["lev"]; r = rng.random()
    xs = [x for x in range(N) if G["opts"][x]]; x = rng.choice(xs); k = rng.randrange(len(G["opts"][x]))
    if r < 0.3:
        c = [y for y in range(N) if lev[y] <= lev[x]] + [-1]; G["opts"][x][k][1] = rng.choice(c)
    elif r < 0.45 and lev[x] >= 1:
        c = [y for y in range(N) if lev[y] == lev[x] - 1]
        if c: G["opts"][x][k][0] = rng.choice(c)
    elif r < 0.65:
        i, j = rng.randrange(len(G["br"])), rng.randrange(len(G["br"])); G["br"][i], G["br"][j] = G["br"][j], G["br"][i]
    elif r < 0.75:
        i = rng.randrange(len(G["bp"])); G["bp"][i] ^= 1
    elif r < 0.9:
        y = rng.choice(xs); k2 = rng.randrange(len(G["opts"][y])); G["gate"][x][k], G["gate"][y][k2] = G["gate"][y][k2], G["gate"][x][k]
    else:
        G["start"][x] = rng.randrange(len(G["opts"][x]))
    return G
G = noup193.rgen_noup(rng, d, w, D); best = score(G)
for it in range(IT):
    H = mutate(G); s = score(H)
    if s >= best:
        if s > best: json.dump(H, open(OUT, "w")); print(it, s, H["N"], flush=True)
        G, best = H, s
print("final", best, G["N"], flush=True)
