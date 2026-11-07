#!/usr/bin/env python3
"""L-RED 53, R215 (b): resumable, seeded xi climb on Xi-cyclic Gamma3 genomes (same genome / mutation / Gamma3 pads as xiclimb.py).
Object under test: box190/n5v.py run(g, "xi") imported UNMODIFIED from a read-only worktree of claude/l-new acdbd28b (env WT).
Seeds: a genome JSON at the same d (resume), or one at d-1 lifted by one top level (new vertices 2d-2, 2d-1; 4 new gates/branches
inserted at random positions of br). Score = xi iterations (+ spec/1000 tiebreak) unless SCORE=gap (xi - spec, + xi/1000).
Acceptance: >= (plateau walk); every RESTART iterations without a new best the walk returns to the best. Every new best is checked
(regions vs harness zielonka, harness verify.check of the strategies); WRONG instances are kept.
Usage: xiclimb2.py d seed iters outprefix [seedjson]"""
import sys, os, json, random, copy
WT = os.environ["WT"]
sys.path[:0] = [os.path.join(WT, "experiments/new/box190"), os.path.join(WT, "experiments/new/box189"), os.path.join(WT, "experiments/harness")]
import n5v, pg, zielonka, verify, gamma3
d, seed, iters, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
seedf = sys.argv[5] if len(sys.argv) > 5 else None
SCORE = os.environ.get("SCORE", "xi"); RESTART = int(os.environ.get("RESTART", "3000"))
rng = random.Random(seed)
def run(g, m):
    st, fb, E = n5v.run(g, m, cap=5000); return len(st) - 1, st, E
def check(g, st, E):
    win, strat = n5v.solution(g, st, E); ref = zielonka.solve(g); e = verify.check(g, win, strat)
    return win == ref and not e
def rgen():
    N = 2 * d; M = 2 * N; lev = [v // 2 for v in range(N)]
    opts = [[[2 * (lev[v] - 1) + k if lev[v] else -1, rng.choice([w for w in range(-1, N) if w != v]), 2 * v + k] for k in range(2)] for v in range(N)]
    br = list(range(M)); rng.shuffle(br); bp = [rng.randrange(2) for _ in range(M)]
    gt = list(range(M)); rng.shuffle(gt); gate = [[gt[2 * v], gt[2 * v + 1]] for v in range(N)]
    return dict(N=N, lev=lev, opts=opts, gate=gate, br=br, bp=bp, start=[rng.randrange(2) for _ in range(N)])
def lift(G):
    G = copy.deepcopy(G); N = G["N"]; M = 2 * N; L = N // 2
    for v in (N, N + 1):
        G["lev"].append(L)
        G["opts"].append([[2 * (L - 1) + k, rng.choice([w for w in range(-1, N + 2) if w != v]), 2 * v + k] for k in range(2)])
    G["gate"] += [[M, M + 1], [M + 2, M + 3]]
    for b in range(M, M + 4):
        G["br"].insert(rng.randrange(len(G["br"]) + 1), b); G["bp"].append(rng.randrange(2))
    G["start"] += [rng.randrange(2), rng.randrange(2)]; G["N"] = N + 2
    return G
def mgen(G):
    G = copy.deepcopy(G); N = G["N"]; M = 2 * N; r = rng.random(); v = rng.randrange(N); k = rng.randrange(2)
    if r < 0.35: G["opts"][v][k][1] = rng.choice([w for w in range(-1, N) if w != v])
    elif r < 0.6: i, j = rng.randrange(M), rng.randrange(M); G["br"][i], G["br"][j] = G["br"][j], G["br"][i]
    elif r < 0.7: G["bp"][rng.randrange(M)] ^= 1
    elif r < 0.9: a, c, ka, kc = rng.randrange(N), rng.randrange(N), rng.randrange(2), rng.randrange(2); G["gate"][a][ka], G["gate"][c][kc] = G["gate"][c][kc], G["gate"][a][ka]
    else: G["start"][v] ^= 1
    return G
def toG(G): return gamma3.build(G, {"K", "pe", "pb", "m"})[0]
def score(G):
    g = toG(G); a, st, E = run(g, "xi"); b, _, _ = run(g, "spec")
    s = a + b / 1000.0 if SCORE == "xi" else (a - b) + a / 1000.0
    return s, a, b, g, st, E
cur = None
if seedf and os.path.exists(seedf):
    S = json.load(open(seedf)); cur = S if S["N"] == 2 * d else (lift(S) if S["N"] == 2 * d - 2 else None)
if cur is None: cur = rgen()
cs = score(cur); best, bestG, since = cs[0], cur, 0
print(f"start n {cs[3].n} xi {cs[1]} spec {cs[2]}", flush=True)
for it in range(iters):
    c = mgen(cur)
    for _ in range(rng.choice([0, 0, 1, 2])): c = mgen(c)
    try: sc = score(c)
    except Exception: continue
    since += 1
    if sc[0] >= cs[0]:
        cur, cs = c, sc
        if sc[0] > best:
            best, bestG, since = sc[0], cur, 0; ok = check(sc[3], sc[4], sc[5])
            json.dump(cur, open(out + ".json", "w")); pg.write(sc[3], out + ".pg")
            print(f"it {it} n {sc[3].n} xi {sc[1]} spec {sc[2]} {'OK' if ok else 'WRONG'}", flush=True)
            if not ok: json.dump(cur, open(out + f"_WRONG_{it}.json", "w")); pg.write(sc[3], out + f"_WRONG_{it}.pg")
    if since >= RESTART: cur, cs, since = bestG, score(bestG), 0
print(f"FINAL best {best:.3f}", flush=True)
