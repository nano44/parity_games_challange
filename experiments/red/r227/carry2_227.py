#!/usr/bin/env python3
"""L-RED 61 R227: SECOND-CARRY search. From a base genome add: a level-1 mover c with gate rank TOP (its e is the most relevant e, above the
base's carry e8), W-target w (an existing level-0 mover, or a NEW level-0 mover z with one option Xi -> a2), Xi-target a; plus one NEW option
at an existing mover m with Xi-target c (gate rank p, beta rank q, bp). Random samples; score ascore226 (A, #tops, T) on own.py ([E-LEV]).
Freezes every strict (A, #tops) gain to out/c2_<TAG>_<SEED>.json. Usage: carry2_227.py BASE.json TAG SEED SAMPLES"""
import sys, os, json, random, copy
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r226"), os.path.join(H, "..", "r225"), os.path.join(H, "..", "r221")]
from compose226 import add_opt, check
from ascore226 import ascore
B = json.load(open(sys.argv[1])); TAG = sys.argv[2]; seed = int(sys.argv[3]); S = int(sys.argv[4]); rng = random.Random(seed)
def newmover(G, lv, wt, xt, gpos, bpos, bp):
    G = copy.deepcopy(G); y = G["N"]; G["N"] += 1; G["lev"].append(lv); G["opts"].append([]); G["gate"].append([]); G["start"].append(0)
    return add_opt(G, y, wt, xt, gpos, bpos, bp), y
def sample():
    G = B; N = G["N"]; L0 = [x for x in range(N) if G["lev"][x] == 0]
    newz = rng.random() < 0.5
    if newz:
        M = len(G["br"]); G, z = newmover(G, 0, -1, rng.choice(list(range(N)) + [-1]), rng.randint(0, M), rng.randint(0, M), rng.randrange(2)); w = z
    else: w = rng.choice(L0)
    M = len(G["br"]); G, c = newmover(G, 1, w, rng.choice(list(range(G["N"])) + [-1]), M, rng.randint(0, M), rng.randrange(2))
    M = len(G["br"]); m = rng.randrange(N); wm = -1 if G["lev"][m] == 0 else rng.choice([y for y in range(N) if G["lev"][y] == G["lev"][m] - 1])
    return add_opt(G, m, wm, c, rng.randint(0, M - 1), rng.randint(0, M), rng.randrange(2))
s0 = ascore(B); best = s0; print("base", s0, flush=True); hist = {}
for i in range(S):
    G = sample()
    try: check(G); a = ascore(G)
    except Exception: continue
    hist[a[0]] = hist.get(a[0], 0) + 1
    if a[:2] > best[:2]:
        best = a; json.dump(G, open(f"out/c2_{TAG}_{seed}.json", "w")); print(i, "GAIN", a, "N", G["N"], "M", len(G["br"]), flush=True)
    if i % 2000 == 0: print(i, "hist", sorted(hist.items()), flush=True)
print("FINAL", best, "hist", sorted(hist.items()), flush=True)
