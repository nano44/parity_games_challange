#!/usr/bin/env python3
"""Box 218 (L-NEW successor 77): upward 2-wide ladders in the IDEAL model (= 1P(G), packet P-N5-KEY1P): a fast simulator and a climb.
Ladder L^R_d: movers 2l, 2l+1 at level l; option j of a level-l mover has W-target 2(l-1)+j (none at level 0). UPWARD: every Xi-target
is a mover of a strictly higher level or the exit (-1), so the Xi-graph is acyclic. Genome JSON as box 217 (N, lev, opts [wt, xt, b],
gate, br, bp, start), so one217.py / key1p.py read the records.
sim(G) -> (T, sw[x]) by the key rule (same rule as one217.OneP; cross-checked by --xcheck).
Climb: mutations = one Xi-target (kept upward; with NEAR=1 only one level up or exit), a swap of two beta ranks (with LEVR=1 only
inside one level, ranks staying level-respecting: higher level = higher rank), one parity, a gate swap, one start bit.
Objective LAD218_OBJ=k (default): (k, the largest sw at level k, the sum of all sw, T) compared lexicographically, k = 1 + the largest
level with a mover with sw = 2^(l+1) - 1 = |K| - 1; LAD218_OBJ=both: the tuple (c_0, ..., c_(d-1)), c_l = min(sw(2l), 2^(l+1)-1) +
min(sw(2l+1), 2^(l+1)-1) (both members of every level full, from the bottom), then T.
Usage: lad218.py climb D SEED ITERS OUTDIR | lad218.py show G.json ... | lad218.py xcheck SEED COUNT D | lad218.py xfiles G.json ..."""
import sys, os, json, random, time
NEAR = os.environ.get("LAD218_NEAR") == "1"; LEVR = os.environ.get("LAD218_LEVR", "1") == "1"
PURE = os.environ.get("LAD218_PURE") == "1"   # the pure crossed bi-ladder: member 0 of pair l parallel (option j -> mover 2(l+1)+j), member 1
                                              # crossed (option j -> mover 2(l+1)+1-j), top level -> exit; level-respecting ranks, all
                                              # parities even; only ranks inside a level, gates and the start are mutated

TPL = os.environ.get("LAD218_TPL", "")       # wiring template: the Xi-targets of pair l are the two movers of level tlev(d, l) (exit if
                                              # tlev = d); member types (parallel / crossed) are mutated, the levels are not. Templates:
                                              # mirror: l < d/2 -> d-1-l, else l+1;  mirror1: l < d/2 -> d-l, else l+1;  up2: l+2 (l+1 at d-2)
def tlev(d, l):
    if TPL == "mirror": return d - 1 - l if l < d // 2 else l + 1
    if TPL == "mirror1": return d - l if l < d // 2 else l + 1
    if TPL == "up2": return min(l + 2, d) if l < d - 2 else l + 1
    if TPL == "mid": return d // 2 if l < d // 2 else l + 1            # every lower pair reads the first upper pair
    if TPL == "down": return l - 1 if l >= 1 else d                    # DOWNWARD bi-ladder: Xi-targets = the pair one level below
    raise SystemExit("unknown template")

def sim(G, cap=200000):
    N, lev, opts, gate = G["N"], G["lev"], G["opts"], G["gate"]
    M = len(G["br"]); pr = [6 + 2 * G["br"][b] + G["bp"][b] for b in range(M)]
    order = sorted(range(M), key=lambda b: (pr[b], b)); rank = [0] * M
    for r, b in enumerate(order): rank[b] = r
    bw = [(1 << rank[b]) if pr[b] % 2 == 0 else -(1 << rank[b]) for b in range(M)]
    topo = []; seen = [0] * N                               # any acyclic Xi-graph: targets first (DFS post-order)
    def visit(x):
        seen[x] = 1
        for (_, y, _) in opts[x]:
            if y >= 0 and not seen[y]: visit(y)
        topo.append(x)
    for x in range(N):
        if not seen[x]: visit(x)
    bylev = sorted(range(N), key=lambda x: lev[x])
    s = list(G["start"]); sw = [0] * N; T = 0
    mv = [0] * N; ov = [None] * N
    while T < cap:
        for x in topo:
            o = opts[x]; ov[x] = [bw[b] + (mv[y] if y >= 0 else 0) for (_, y, b) in o]; mv[x] = ov[x][s[x]]
        new = s[:]; key = [None] * N; ch = False
        for x in bylev:
            o = opts[x]; cur = ov[x][s[x]]; best = None; bk = None
            for k in range(len(o)):
                if k == s[x] or ov[x][k] > cur:
                    wt = o[k][0]; kk = (key[wt] if wt >= 0 else ()) + (gate[x][k],)
                    if bk is None or kk < bk: bk = kk; best = k
            key[x] = bk
            if best != s[x]: new[x] = best; sw[x] += 1; ch = True
        if not ch: break
        s = new; T += 1
    return T, sw

def rand_genome(rng, d):
    N = 2 * d; lev = [x // 2 for x in range(N)]; opts = []; i = 0
    for x in range(N):
        oo = []
        for j in range(2):
            wt = 2 * (lev[x] - 1) + j if lev[x] else -1
            hi = [y for y in range(N) if (lev[y] == lev[x] + 1 if NEAR else lev[y] > lev[x])]
            xt = rng.choice(hi) if hi and rng.random() < 0.85 else -1
            if PURE: xt = 2 * (lev[x] + 1) + (j if x % 2 == 0 else 1 - j) if lev[x] < d - 1 else -1
            if TPL:
                tl = tlev(d, lev[x]); xt = 2 * tl + (j if x % 2 == 0 else 1 - j) if tl < d else -1
            oo.append([wt, xt, i]); i += 1
        opts.append(oo)
    M = 2 * N; g = list(range(M)); rng.shuffle(g); gate = [[g[2 * x], g[2 * x + 1]] for x in range(N)]
    if LEVR:
        br = [0] * M
        for l in range(d):
            ids = [4 * l + i for i in range(4)]; rr = ids[:]; rng.shuffle(rr)
            for b, r in zip(ids, rr): br[b] = r
    else: br = list(range(M)); rng.shuffle(br)
    return {"N": N, "lev": lev, "opts": opts, "gate": gate, "br": br, "bp": [0 if PURE else rng.randrange(2) for _ in range(M)],
            "start": [rng.randrange(2) for _ in range(N)]}

def mutate(rng, G):
    H = {"N": G["N"], "lev": G["lev"], "opts": [[o[:] for o in oo] for oo in G["opts"]], "gate": [g[:] for g in G["gate"]],
         "br": G["br"][:], "bp": G["bp"][:], "start": G["start"][:]}
    N, lev = H["N"], H["lev"]; M = 2 * N; r = rng.random(); x = rng.randrange(N); k = rng.randrange(2)
    if PURE: r = 0.35 + r * 0.2 if r < 0.4 else (0.7 + (r - 0.4) * 0.5)      # ranks 40 %, gates 36 %, start 24 %
    if TPL and r < 0.35:                                                     # template: swap the mover's two Xi-targets (its type)
        o = H["opts"][x]
        if r < 0.3: o[0][1], o[1][1] = o[1][1], o[0][1]
        else:                                                                # or point both options at one member / restore
            tl = tlev(N // 2, lev[x])
            if tl < N // 2: o[k][1] = 2 * tl + rng.randrange(2)
        return H
    if r < 0.35:
        hi = [y for y in range(N) if (lev[y] == lev[x] + 1 if NEAR else lev[y] > lev[x])]
        H["opts"][x][k][1] = rng.choice(hi + [-1]) if hi else -1
    elif r < 0.55:
        a = rng.randrange(M)
        if LEVR: l = a // 4; b = 4 * l + rng.randrange(4)
        else: b = rng.randrange(M)
        H["br"][a], H["br"][b] = H["br"][b], H["br"][a]
    elif r < 0.7: b = rng.randrange(M); H["bp"][b] ^= 1
    elif r < 0.88:
        y, l = rng.randrange(N), rng.randrange(2); H["gate"][x][k], H["gate"][y][l] = H["gate"][y][l], H["gate"][x][k]
    else: H["start"][x] ^= 1
    return H

OBJ = os.environ.get("LAD218_OBJ", "k")
def score(G):
    T, sw = sim(G); d = G["N"] // 2
    if OBJ == "both":                      # both members of every level full, level by level from the bottom
        c = tuple(min(sw[2 * l], (1 << (l + 1)) - 1) + min(sw[2 * l + 1], (1 << (l + 1)) - 1) for l in range(d))
        return c + (T,), T, sw
    k = kdepth(G, sw)                      # OBJ = k: enumeration depth, then progress of the best mover of level k, then all switches
    p = max(sw[2 * k], sw[2 * k + 1]) if k < d else 0
    return (k, p, sum(sw), T), T, sw

def kdepth(G, sw):
    d = G["N"] // 2; full = [l for l in range(d) if max(sw[2 * l], sw[2 * l + 1]) == (1 << (l + 1)) - 1]
    return 1 + max(full) if full else 0

def insert_mid(G, rng, at):
    """two new pairs at levels at, at + 1 of an upward ladder (old levels >= at rise by 2): W-ladder kept, old Xi-targets follow
    their movers, new movers get random upward Xi-targets, ranks stay level-respecting (old order kept inside each level)"""
    N, lev = G["N"], G["lev"]; d = N // 2; new = lambda x: x if lev[x] < at else x + 4
    M = len(G["br"]); pr = [6 + 2 * G["br"][b] + G["bp"][b] for b in range(M)]
    old_rank = {b: r for r, b in enumerate(sorted(range(M), key=lambda b: (pr[b], b)))}
    N2 = N + 4; d2 = d + 2; lev2 = [x // 2 for x in range(N2)]; opts = [None] * N2; gate = [None] * N2; start = [0] * N2
    bp = [0] * (2 * N2); key = [0.0] * (2 * N2)
    for x in range(N):
        y = new(x); opts[y] = []
        for j, (wt, xt, b) in enumerate(G["opts"][x]):
            nb = 2 * y + j; opts[y].append([2 * (lev2[y] - 1) + j if lev2[y] else -1, new(xt) if xt >= 0 else -1, nb])
            bp[nb] = G["bp"][b]; key[nb] = old_rank[b]
        gate[y] = [g + (10000 if lev[x] >= at else 0) for g in G["gate"][x]]; start[y] = G["start"][x]
    for y in range(2 * at, 2 * at + 4):
        opts[y] = []
        for j in range(2):
            hi = [z for z in range(N2) if lev2[z] > lev2[y]]; nb = 2 * y + j
            opts[y].append([2 * (lev2[y] - 1) + j if lev2[y] else -1, rng.choice(hi + [-1]), nb]); bp[nb] = rng.randrange(2); key[nb] = rng.random() * M
        gate[y] = [5000 + 10 * y + rng.randrange(10) for _ in range(2)]
        if gate[y][0] == gate[y][1]: gate[y][1] += 1
        start[y] = rng.randrange(2)
    order = sorted(range(2 * N2), key=lambda b: (lev2[b // 2], key[b], b)); br = [0] * (2 * N2)
    for r, b in enumerate(order): br[b] = r
    return {"N": N2, "lev": lev2, "opts": opts, "gate": gate, "br": br, "bp": bp, "start": start}

SEED = os.environ.get("LAD218_SEED", "")      # a genome JSON: every (re)start is insert_mid(seed genome) at its middle level
def climb(d, seed, iters, outdir):
    rng = random.Random(seed); best = None; bestG = None; t0 = time.time(); cur = None; curG = None; stall = 0
    S0 = None
    if SEED: S0 = json.load(open(SEED)); S0 = S0.get("genome", S0); assert S0["N"] // 2 + 2 == d
    for it in range(iters):
        if curG is None or stall > int(os.environ.get("LAD218_STALL", "4000")):
            curG = insert_mid(S0, rng, S0["N"] // 4) if S0 else rand_genome(rng, d); cur = score(curG)[0]; stall = 0
        H = mutate(rng, curG)
        if rng.random() < 0.3: H = mutate(rng, H)
        sc, T, sw = score(H)
        if sc >= cur:
            if sc > cur: stall = 0
            cur, curG = sc, H
            if best is None or sc > best:
                best, bestG = sc, H; k = kdepth(H, sw)
                print(f"it {it} d {d} k {k} T {T} c {sc[:-1]} sw {[(sw[2 * l], sw[2 * l + 1]) for l in range(d)]} sec {time.time() - t0:.0f}", flush=True)
                os.makedirs(outdir, exist_ok=True)
                tag = TPL or ("pure" if PURE else ("near" if NEAR else "up") + ("_levr" if LEVR else "")) + ("_seeded" if SEED else "")
                json.dump({"d": d, "seed": seed, "k": k, "T": T, "genome": H}, open(os.path.join(outdir, f"lad_{tag}_d{d}_s{seed}.json"), "w"))
        stall += 1
    return best

if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] == "climb": climb(int(a[1]), int(a[2]), int(a[3]), a[4])
    elif a[0] == "show":
        for fn in a[1:]:
            G = json.load(open(fn)); G = G.get("genome", G); sc, T, sw = score(G); d = G["N"] // 2
            print(os.path.basename(fn), "d", d, "T", T, "k", kdepth(G, sw), "sw", [(sw[2 * l], sw[2 * l + 1]) for l in range(d)])
    elif a[0] == "xfiles":                                   # sim against one217.OneP on genome files (long runs: towers, records)
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "box217")); import one217
        bad = 0; mx = 0; n = 0
        for fn in a[1:]:
            G = json.load(open(fn)); G = G.get("genome", G); T, sw = sim(G); S = one217.OneP(G).run("key"); mx = max(mx, T); n += 1
            sw2 = [sum(1 for t in range(len(S) - 1) if S[t + 1][x] != S[t][x]) for x in range(G["N"])]
            bad += int(T != len(S) - 1 or sw != sw2)
        print(f"xfiles genomes {n} maxT {mx} simdiff {bad}")
    elif a[0] == "xcheck":
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "box217")); import one217
        rng = random.Random(int(a[1])); bad = 0; n = int(a[2]); d = int(a[3]); mx = 0
        for _ in range(n):
            G = rand_genome(rng, d)
            for _ in range(rng.randrange(0, 30)): G = mutate(rng, G)
            T, sw = sim(G); S = one217.OneP(G).run("key"); mx = max(mx, T)
            sw2 = [sum(1 for t in range(len(S) - 1) if S[t + 1][x] != S[t][x]) for x in range(G["N"])]
            bad += int(T != len(S) - 1 or sw != sw2)
        print(f"xcheck seed {a[1]} genomes {n} d {d} maxT {mx} simdiff {bad}")
