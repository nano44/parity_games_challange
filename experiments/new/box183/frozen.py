#!/usr/bin/env python3
"""L-NEW box 183: FROZEN FRAMES. G in L^R_d with the two level-0 movers frozen (one option each: their option q; W-target none) and
arbitrary acyclic Xi-targets (non-ISO: upper options may have Xi-target 0 or 1, and the frozen options' Xi-targets may be upper movers).
By R110 W-ONLY (first clause) and F0, a non-ISO run of L^R_d is, between the <= 2 steps moving 0 or 1, a run of such a frozen genome.
ISO frames (no option with Xi-target 0 or 1) are the frames of R110's T_0. Hill-climb max over all starts of T, ISO vs non-ISO.
Usage: [FULL=1] frozen.py d seed iters mode(iso|non)"""
import os, sys, json, random, copy, itertools
H = os.path.dirname(os.path.abspath(__file__)); P0 = os.path.join(H, "..", "box150", "check.py")
ns = {"__file__": P0, "__name__": "lib"}; exec(open(P0).read().split("\nif __name__")[0], ns); Gen, topo = ns["Gen"], ns["topo"]
d, seed, iters, mode = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; rng = random.Random(seed); N = 2 * d
FULL = os.environ.get("FULL") == "1"  # FULL=1: the level-0 movers keep two options (a full L^R_d ladder, ISO or not)
def rand():
    order = list(range(N)); rng.shuffle(order); M = 0; opts = []
    for x in range(N):
        o = []
        for k in range(1 if (x < 2 and not FULL) else 2):
            o.append([2 * (x // 2 - 1) + k if x >= 2 else -1, -1, M]); M += 1
        opts.append(o)
    G = {"N": N, "lev": [x // 2 for x in range(N)], "opts": opts, "xorder": order, "M": M}
    g = list(range(M)); rng.shuffle(g); it = iter(g); G["gate"] = [[next(it) for _ in o] for o in opts]
    G["br"] = rng.sample(range(M), M); G["bp"] = [rng.randint(0, 1) for _ in range(M)]
    for x in range(N):
        for o in opts[x]: o[1] = pick(G, x)
    G["start"] = [0] * N; return G
def pick(G, x):
    pos = {v: i for i, v in enumerate(G["xorder"])}
    later = [v for v in range(N) if pos[v] > pos[x] and (mode == "non" or v >= 2)]
    return rng.choice(later + [-1]) if later and rng.random() < 0.85 else -1
def score(G):
    g = Gen(G); best = (0, None)
    for s in itertools.product(*[range(len(o)) for o in G["opts"]]):
        try: S, _ = g.run(s, cap=2000)
        except RuntimeError: return (-1, None)
        if len(S) - 1 > best[0]: best = (len(S) - 1, s)
    return best
def mutate(G):
    G = copy.deepcopy(G); m = rng.randrange(4); M = G["M"]
    if m == 0:
        x = rng.randrange(N); k = rng.randrange(len(G["opts"][x])); G["opts"][x][k][1] = pick(G, x)
    elif m == 1: a, b = rng.sample(range(M), 2); G["br"][a], G["br"][b] = G["br"][b], G["br"][a]
    elif m == 2: G["bp"][rng.randrange(M)] ^= 1
    else:
        x, y = rng.randrange(N), rng.randrange(N); i, j = rng.randrange(len(G["opts"][x])), rng.randrange(len(G["opts"][y]))
        G["gate"][x][i], G["gate"][y][j] = G["gate"][y][j], G["gate"][x][i]
    return G
G = rand(); cur = score(G); best = (cur, copy.deepcopy(G))
for it in range(iters):
    H2 = mutate(G); sc = score(H2)
    if sc[0] >= cur[0]:
        G, cur = H2, sc
        if sc[0] > best[0][0]: best = (sc, copy.deepcopy(G))
B = best[1]; B["start"] = list(best[0][1]); B.pop("M")
iso = all(o[1] not in (0, 1) for oo in B["opts"] for o in oo)
tag = ("full" if FULL else "frozen") + "_%s_d%d_s%d_T%d" % (mode, d, seed, best[0][0]); json.dump(B, open(os.path.join(H, "out", tag + ".json"), "w"))
print("%s: max T %d (ISO %s)" % (tag, best[0][0], iso))
