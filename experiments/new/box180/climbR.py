#!/usr/bin/env python3
"""L-NEW box 180: adversarial hill-climb for ONE option's value rises R(x, k) in a single IDEAL run (box150 simulator).
Genomes: 2-wide ladders L^R_d (seeded from a file or random, box162 rand_lr) whose Xi-targets may be any later mover in xorder (IDEAL-ACYC).
Moves: re-target an option's Xi-target (acyclic by xorder), swap two beta ranks, flip a parity, swap two gates, flip a start bit.
Objective: (max_(x,k) R(x, k), T) lexicographic; accept ties (plateau walk). Writes the best genome to out/.
Usage: [ALLSTARTS=1] climbR.py d seed iters [seedfile]   (ALLSTARTS=1: score = best over all starts)"""
import os, sys, json, random, copy
H = os.path.dirname(os.path.abspath(__file__)); P0 = os.path.join(H, "..", "box150", "check.py")
ns = {"__file__": P0, "__name__": "lib"}; exec(open(P0).read().split("\nif __name__")[0], ns); Gen = ns["Gen"]
fl = {"__file__": os.path.join(H, "..", "box162", "flipcheck.py"), "__name__": "lib"}; exec(open(fl["__file__"]).read().split("\nif __name__")[0], fl)
d, seed, iters = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); rng = random.Random(seed)
if len(sys.argv) > 4:
    G = json.load(open(sys.argv[4])); d = G["N"] // 2
    if "xorder" not in G: G["xorder"] = ns["topo"](G)
else: G = fl["rand_lr"](d, rng, iso=False)
N = G["N"]
ALL = os.environ.get("ALLSTARTS") == "1"
def score1(g, start):
    try: S, _ = g.run(start, cap=5000)
    except RuntimeError: return (-1, -1, None, None)
    T = len(S) - 1; best = (0, None)
    for x in range(N):
        for k in (0, 1):
            v = [g.face(s, x, k) for s in S]; r = sum(1 for t in range(1, T + 1) if v[t] > v[t - 1])
            if r > best[0]: best = (r, (x, k))
    return (best[0], T, best[1], tuple(start))
def score(G):
    g = Gen(G)
    if not ALL: return score1(g, G["start"])
    import itertools
    return max(score1(g, st) for st in itertools.product((0, 1), repeat=N))
def mutate(G):
    G = copy.deepcopy(G); pos = {v: i for i, v in enumerate(G["xorder"])}; m = rng.randrange(5)
    if m == 0:
        x = rng.randrange(N); k = rng.randrange(2); later = [v for v in range(N) if pos[v] > pos[x]]
        G["opts"][x][k][1] = rng.choice(later + [-1]) if later else -1
    elif m == 1:
        a, b = rng.sample(range(2 * N), 2); G["br"][a], G["br"][b] = G["br"][b], G["br"][a]
    elif m == 2: a = rng.randrange(2 * N); G["bp"][a] ^= 1
    elif m == 3:
        x, y = rng.randrange(N), rng.randrange(N); i, j = rng.randrange(2), rng.randrange(2)
        G["gate"][x][i], G["gate"][y][j] = G["gate"][y][j], G["gate"][x][i]
    else: x = rng.randrange(N); G["start"][x] ^= 1
    return G
cur = score(G); best = (cur, copy.deepcopy(G))
for it in range(iters):
    H2 = mutate(G); sc = score(H2)
    if sc[:2] >= cur[:2]:
        G, cur = H2, sc
        if sc[:2] > best[0][:2]: best = (sc, copy.deepcopy(G))
os.makedirs(os.path.join(H, "out"), exist_ok=True)
if best[0][3] is not None: best[1]["start"] = list(best[0][3])
tag = "climbR_d%d_s%d" % (d, seed) + ("_all" if ALL else ""); json.dump(best[1], open(os.path.join(H, "out", tag + ".json"), "w"))
print("%s: best maxR %d at %s with T %d (N %d)" % (tag, best[0][0], best[0][2], best[0][1], N))
