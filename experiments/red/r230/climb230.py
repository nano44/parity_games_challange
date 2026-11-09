#!/usr/bin/env python3
"""L-RED 64 R230: hill climb for a REACH3-CYC / [STD3] failure of N5'-xi on Gamma3 (std230.measure; score lexicographic
(nstd + nonhow + t3, offimp, taui, mtie)), Xi-cyclic genomes, size N <= NMAX, degree <= DMAX. Mutations: re-draw an option's W-target
(level below, or c_W at level 0), its Xi-target (any mover or none), swap two gate indices, re-draw br / bp of an option, flip a start
choice, add or drop an option, add a mover. Accept if score >= current (plateau moves allowed). Checkpoint every 50 evaluations to
OUT/best_<tag>.json + OUT/climb_<tag>.log; RESUME=1 restarts from the checkpoint. A hard failure is frozen at once to OUT/FAIL_<tag>_<k>.json.
Usage: climb230.py TAG SEED EVALS [START.json]   env LNEW, NMAX (16), DMAX (3), OUT (out/climb)"""
import sys, os, json, random, copy, time
from std230 import measure, score
from bonly3_230 import rgen
tag, seed, evals = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]); rng = random.Random(seed)
NMAX, DMAX, OUT = int(os.environ.get("NMAX", "16")), int(os.environ.get("DMAX", "3")), os.environ.get("OUT", "out/climb")
os.makedirs(OUT, exist_ok=True); ck = os.path.join(OUT, f"best_{tag}.json"); lg = open(os.path.join(OUT, f"climb_{tag}.log"), "a")
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
if os.environ.get("RESUME") == "1" and os.path.exists(ck): cur = json.load(open(ck)); done0 = cur.pop("_evals", 0)
elif len(sys.argv) > 4: cur = json.load(open(sys.argv[4])); done0 = 0
else: cur = rgen(rng, 2, 2, 2); done0 = 0
cur = renum(cur); cs = score(measure(cur)); fails = 0; t0 = time.time()
for e in range(done0, evals):
    nG = mutate(cur)
    try: c = measure(nG)
    except Exception as ex: print("ERR", e, repr(ex)[:120], file=lg, flush=True); continue
    s = score(c)
    if s[0] > 0:
        fails += 1; json.dump(nG, open(os.path.join(OUT, f"FAIL_{tag}_{fails}.json"), "w")); print("FAIL", tag, e, c, flush=True); print("FAIL", e, c, file=lg, flush=True)
    if s >= cs:
        if s > cs: print(e, "score", s, "N", c["N"], "M", c["M"], "states", c["states"], file=lg, flush=True)
        cur, cs = nG, s
    if e % 50 == 49: json.dump(dict(cur, _evals=e + 1), open(ck, "w"))
json.dump(dict(cur, _evals=evals), open(ck, "w"))
print(f"END {tag} evals {evals} best score {cs} N {cur['N']} fails {fails} secs {time.time() - t0:.0f}", flush=True)
print(f"END evals {evals} best {cs} fails {fails}", file=lg, flush=True)
