#!/usr/bin/env python3
"""L-RED 61 R227 item 3: GROWTH climb for the RE-ARMING DEPTH of L-NEW 65 BOX 198 (CONJECTURE RA-LOG target) on own.py ([E-LEV], cap 600).
Score = (depth, maxP, C, -size) from ra227.census (depth = longest RA-chain in letters, maxP = max paths, C = max c_y); size N + M <= CAP.
Moves: sharp226.mutate (rewire / ranks / start) and the GROW moves of growclimb226 (add an option; add a level-0/1 mover reached by a new option).
Freezes every strict (depth, maxP, C) gain to out/dc_<CAP>_<SEED>.json and logs (depth, maxP, C, fanin, A, T, N, M).
Env ORDER=C scores (C, maxP, depth) instead (the C-EQUIV target). Resumable: RESUME=out/dc_<CAP>_<SEED>.json restarts from the frozen best. Usage: depthclimb227.py SEED CAP ITER START.json"""
import sys, os, json, random, copy
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r226"), os.path.join(H, "..", "r225"), os.path.join(H, "..", "r221")]
from sharp226 import mutate
from compose226 import add_opt, check
from ra227 import census
seed, CAP, IT, SG = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; rng = random.Random(seed)
size = lambda G: G["N"] + sum(len(o) for o in G["opts"])
def score(G):
    c = census(G, 600)
    if os.environ.get("ORDER") == "C": return (c["C"], c["maxP"], c["depth"], -size(G)), c
    return (c["depth"], c["maxP"], c["C"], -size(G)), c
def grow(G):
    G = copy.deepcopy(G); N = G["N"]; M = len(G["br"])
    if rng.random() < 0.6:
        x = rng.randrange(N); wt = -1 if G["lev"][x] == 0 else rng.choice([y for y in range(N) if G["lev"][y] == G["lev"][x] - 1])
        return add_opt(G, x, wt, rng.choice(list(range(N)) + [-1]), rng.randint(0, M), rng.randint(0, M), rng.randrange(2))
    lv = rng.choice([0, 1]); y = N; G["N"] += 1; G["lev"].append(lv); G["opts"].append([]); G["gate"].append([]); G["start"].append(0)
    wt = -1 if lv == 0 else rng.choice([z for z in range(N) if G["lev"][z] == 0])
    G = add_opt(G, y, wt, rng.choice(list(range(N)) + [-1]), rng.randint(0, M), rng.randint(0, M), rng.randrange(2)); M += 1
    x = rng.randrange(N); wx = -1 if G["lev"][x] == 0 else rng.choice([z for z in range(N) if G["lev"][z] == G["lev"][x] - 1])
    return add_opt(G, x, wx, y, rng.randint(0, M), rng.randint(0, M), rng.randrange(2))
G = json.load(open(os.environ.get("RESUME", SG))); s, c = score(G)
print("start", s, {k: c[k] for k in ("fanin", "A", "T")}, "N", G["N"], "M", len(G["br"]), flush=True)
for it in range(IT):
    Hh = grow(G) if (rng.random() < 0.3 and size(G) < CAP) else mutate(G, rng)
    if size(Hh) > CAP: continue
    try: check(Hh); s2, c2 = score(Hh)
    except Exception: continue
    if s2[:3] >= s[:3]:
        if s2[:3] > s[:3]:
            json.dump(Hh, open(f"out/dc{os.environ.get('ORDER', '')}_{CAP}_{seed}.json", "w"))
            print(it, "depth", s2[0], "maxP", s2[1], "C", s2[2], "fanin", c2["fanin"], "A", c2["A"], "T", c2["T"], "N", Hh["N"], "M", len(Hh["br"]), flush=True)
        G, s = Hh, s2
print("FINAL cap", CAP, "score", s, "N", G["N"], "M", len(G["br"]), flush=True)
