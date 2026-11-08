#!/usr/bin/env python3
"""L-RED 60 R226: GROWTH climb for A (max two-letter alternation of tops; ALT-EQUIV's A) under a size cap N + M <= CAP.
Mutations: sharp226.mutate (rewire / ranks / start) plus GROW moves: add an option to a mover (targets, gate rank, beta rank random),
add a level-1 or level-0 mover reached by a new option of an existing mover. Score = (A, #tops of the max-A interval, -size).
A = max(1, maxalt) when any change exists (R226-core197 §8 W-2). Engine own.py ([E-LEV]), cap 600 steps.
Freezes the best genome to out/grow_CAP_SEED.json; prints (A, T, N, M) at each strict gain. Usage: growclimb226.py SEED CAP ITER SEEDGENOME"""
import sys, os, json, random, copy
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r225"), os.path.join(H, "..", "r221")]
import own
from asc226 import alt
from sharp226 import mutate
from compose226 import add_opt, check
seed, CAP, IT, SG = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; rng = random.Random(seed)
size = lambda G: G["N"] + sum(len(o) for o in G["opts"])
def score(G):
    N = G["N"]; out, V, O, ow = own.run(G, 600); n, prio, o_, succ, _, _ = own.build(G); rk = own.VJ(prio).rk; evs = {V[("e", q)] for q in O}
    T = len(out) - 1; best = (0, 0)
    for v in range(n):
        t = 0
        while t <= T:
            u = t
            while u + 1 <= T and out[u + 1][1][v][0] == out[t][1][v][0]: u += 1
            prev = None; tops = []
            for i in range(t, u + 1):
                E = frozenset(e for e in out[i][1][v][1] if e in evs)
                if prev is not None and E != prev: tops.append(max(E ^ prev, key=lambda e: rk[e]))
                prev = E
            if tops: best = max(best, (max(1, alt(tops)), len(tops)))
            t = u + 1
    return best + (-size(G),), T
def grow(G):
    G = copy.deepcopy(G); N = G["N"]; M = len(G["br"]); r = rng.random()
    if r < 0.6:
        x = rng.randrange(N); wt = -1 if G["lev"][x] == 0 else rng.choice([y for y in range(N) if G["lev"][y] == G["lev"][x] - 1])
        return add_opt(G, x, wt, rng.choice(list(range(N)) + [-1]), rng.randint(0, M), rng.randint(0, M), rng.randrange(2))
    lv = rng.choice([0, 1]); y = N; G["N"] += 1; G["lev"].append(lv); G["opts"].append([]); G["gate"].append([]); G["start"].append(0)
    wt = -1 if lv == 0 else rng.choice([z for z in range(N) if G["lev"][z] == 0])
    G = add_opt(G, y, wt, rng.choice(list(range(N)) + [-1]), rng.randint(0, M), rng.randint(0, M), rng.randrange(2)); M += 1
    x = rng.randrange(N); wx = -1 if G["lev"][x] == 0 else rng.choice([z for z in range(N) if G["lev"][z] == G["lev"][x] - 1])
    return add_opt(G, x, wx, y, rng.randint(0, M), rng.randint(0, M), rng.randrange(2))
G = json.load(open(SG)); s, T = score(G); print("seed", s, "T", T, "N", G["N"], "size", size(G), flush=True)
for it in range(IT):
    Hh = grow(G) if (rng.random() < 0.3 and size(G) < CAP) else mutate(G, rng)
    if size(Hh) > CAP: continue
    try: check(Hh); s2, T2 = score(Hh)
    except Exception: continue
    if s2[:2] >= s[:2]:
        if s2[:2] > s[:2]:
            json.dump(Hh, open(f"out/grow_{CAP}_{seed}.json", "w")); print(it, "A", s2[0], "tops", s2[1], "T", T2, "N", Hh["N"], "M", len(Hh["br"]), flush=True)
        G, s = Hh, s2
print("FINAL cap", CAP, "A", s[0], "tops", s[1], "N", G["N"], "M", len(G["br"]), flush=True)
