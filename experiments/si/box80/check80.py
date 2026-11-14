#!/usr/bin/env python3
"""L-SI box 80: machine checks of docs/si/N5-TOWER-box80.md (lane lemmas PULSE-NEST, ZONE; DATA tables). Deterministic.
Simulators: sim80.py Sim (own) and box76/tw.py Sim (own, earlier; cross-checked against L-NEW's box150 Gen in box 76); every run
below is computed by both and compared (counter XS).
Scopes: CORPUS = the 208 L^R_d genomes of box76/corpus_lr.json.gz (frozen P-IDEAL-MOVES corpus), every start for N <= 10, the
stored start otherwise; EXTRA = box79/inst/*.json (L-LOWER 4's RECF4_d20_F60, DBL4_d20_F30, H5_d20_F62, H6_d24_F126), stored start.
Counters (violations, must be 0; unit printed):
  XS    (run) where sim80 and tw.py give different state sequences
  PN    PULSE-NEST: (run, j >= 1, k >= 1 with levels j..j+k doubling, j-window) with pulse < k + 1
  ZONE  ZONE: (random top extension G' of a genome G, start) with s'_t|old != s_min(t,T) for some t <= T', or T' < T
Controls (must be > 0): PN_T windows with pulse = k + 1 exactly (the bound is attained); ZONE_NEG: extensions that re-target one
old option to a new mover (closure broken), runs whose old part differs from G's run.
  INSERT  INSERT-PASS: (genome, L, start) where the run with the inserted pair differs from the old run on the old movers, or the
          inserted pair moves; INSERT_F: F(L) != F(L - 1) or the other F values change. Control INSERT_NEG (> 0): the inserted
          pair split the other way (2L on 1, 2L+1 on 0, still never moving) changes the old run.
Then the slack table of the EXTRA genomes: per level j, min pulse, the PULSE-NEST bound h - j (h = capped levels), slack."""
import sys, os, json, glob, random, itertools, collections
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(H, "..", "box76")); sys.path.insert(0, H)
from tw import load_corpus, is_lr, Sim as TwSim
from sim80 import Sim, stats, keyorder, capped
def windows(sim, S):
    """per level j >= 1: list of (window start, window end, [move steps of pair j in it]); plus F, doubling flags"""
    d = sim.N // 2; T = len(S) - 1; O = [keyorder(sim, s) for s in S]
    flips = [[t for t in range(1, T + 1) if O[t][j] != O[t - 1][j]] for j in range(d)]
    F = [len(f) for f in flips]
    mvs = [[t for t in range(1, T + 1) if S[t][2 * j] != S[t - 1][2 * j] or S[t][2 * j + 1] != S[t - 1][2 * j + 1]] for j in range(d)]
    W = {}
    for j in range(1, d):
        bnd = [1] + flips[j - 1] + [T + 1]; W[j] = []
        for a, z in zip(bnd, bnd[1:]):
            if a < z: W[j].append((a, z - 1, [t for t in mvs[j] if a <= t < z]))
    dbl = [False] + [F[j] == 2 * F[j - 1] + 2 for j in range(1, d)]
    return F, dbl, W
def pulse_check(sim, S, C):
    F, dbl, W = windows(sim, S); d = sim.N // 2
    for j in range(1, d):
        k = 0
        while j + k + 1 <= d - 1 and all(dbl[j:j + k + 2]): k += 1
        if k == 0 or not dbl[j]: continue
        for (a, e, m) in W[j]:
            C["PN_units"] += 1
            if len(m) != 2 or m[1] - m[0] < k + 1: C["PN"] += 1
            elif m[1] - m[0] == k + 1: C["PN_T"] += 1
def extend(G, rng, m, neg=False):
    """random top extension by m levels: new movers' options W-point by R110's rule, Xi-targets uniform over old/new movers or X
    (acyclic by construction: a new mover targets only movers of smaller index or X), new distinct ranks among unused integers,
    random signs, new distinct gates, random start bits. neg: re-target one old option to a new mover (closure broken)."""
    N = G["N"]; d = N // 2; G2 = json.loads(json.dumps(G))
    used = set(G["br"]); free = [r for r in range(0, 2 * (max(used) + 4 * m + 4)) if r not in used]; rng.shuffle(free)
    gmax = max(max(g) for g in G["gate"]) + 1
    for l in range(d, d + m):
        for q in range(2):
            x = 2 * l + q; row = []; grow = []
            for k in range(2):
                e = len(G2["br"]); G2["br"].append(free.pop()); G2["bp"].append(rng.randint(0, 1))
                y = rng.randint(-1, x - 1); row.append([2 * (l - 1) + k, y, e])
            G2["opts"].append(row)
            G2["gate"].append([gmax + 4 * (l - d) + 2 * q + rng.randint(0, 1) * 0, gmax + 4 * (l - d) + 2 * q + 1])
            G2["start"].append(rng.randint(0, 1))
        a, b = 2 * l, 2 * l + 1   # shuffle the four gates of the level
        gs = G2["gate"][a] + G2["gate"][b]; rng.shuffle(gs); G2["gate"][a] = gs[:2]; G2["gate"][b] = gs[2:]
    G2["N"] = N + 2 * m; G2["lev"] = [v // 2 for v in range(N + 2 * m)]
    if neg:
        x = rng.randrange(N); k = rng.randint(0, 1); G2["opts"][x][k][1] = rng.randrange(N, N + 2 * m)
        try: Sim(G2)
        except RuntimeError: return None
    return G2
def insert_pass(G, L, inv=False):
    """insert80.py as a function: shift levels >= L up, insert a never-moving split pair (2L on 0, 2L+1 on 1, Xi-targets X)"""
    N = G["N"]; ren = lambda y: y if y < 2 * L else y + 2
    opts = []; gate = []; br = list(G["br"]); bp = list(G["bp"]); st = []
    for x in range(N):
        if x == 2 * L:
            mx = max(br) + 1; gm = max(max(g) for g in G["gate"]) + 1
            for q in range(2):
                row = []
                for k in range(2):
                    e = len(br); good = (k == (1 - q if inv else q)); br.append(mx + 2 * q + (1 if good else 0)); bp.append(0 if good else 1)
                    row.append([2 * (L - 1) + k, -1, e])
                opts.append(row); gate.append([gm + 2 * q, gm + 2 * q + 1]); st.append(1 - q if inv else q)
        lv = x // 2 + (1 if x // 2 >= L else 0)
        opts.append([[2 * (lv - 1) + k if lv > 0 else -1, ren(G["opts"][x][k][1]) if G["opts"][x][k][1] >= 0 else -1, G["opts"][x][k][2]] for k in range(2)])
        gate.append(list(G["gate"][x])); st.append(G["start"][x])
    return {"N": N + 2, "lev": [v // 2 for v in range(N + 2)], "deg": 2, "opts": opts, "gate": gate, "br": br, "bp": bp, "start": st}
def main():
    C = collections.Counter(); I = collections.Counter(); rng = random.Random(80)
    items = [(p, G, s0) for p, G in load_corpus() if is_lr(G)
             for s0 in (itertools.product((0, 1), repeat=G["N"]) if G["N"] <= 10 else [tuple(G["start"])])]
    extra = [(p, json.load(open(p)), None) for p in sorted(glob.glob(os.path.join(H, "..", "box79", "inst", "*.json")))]
    for scope, its in (("CORPUS", items), ("EXTRA", extra)):
        C = collections.Counter(); I = collections.Counter()
        for p, G, s0 in its:
            sim = Sim(G); s0 = tuple(G["start"]) if s0 is None else tuple(s0); S = sim.run(s0); I["runs"] += 1; I["steps"] += len(S) - 1
            if [tuple(z) for z in TwSim(G).run(s0)] != S: C["XS"] += 1
            pulse_check(sim, S, C)
        print("%s INFO %s" % (scope, " ".join("%s %d" % kv for kv in sorted(I.items()))))
        print("%s XS %d PN %d (units: %d (run, level j, j-window) with k >= 1) PN_T %d" % (scope, C["XS"], C["PN"], C["PN_units"], C["PN_T"]))
    # ZONE: every corpus genome, stored start + up to 4 other starts, 3 extensions each (m = 1, 2, 3); NEG one per genome and start
    C = collections.Counter()
    for p, G in load_corpus() + [(q, G) for q, G, _ in extra]:
        if not is_lr(G): continue
        sim = Sim(G); N = G["N"]
        starts = [tuple(G["start"])] + [tuple(rng.randint(0, 1) for _ in range(N)) for _ in range(4)]
        for s0 in starts:
            S = sim.run(s0); T = len(S) - 1
            for m in (1, 2, 3):
                G2 = extend(G, rng, m); sim2 = Sim(G2); s2 = tuple(s0) + tuple(G2["start"][N:]); S2 = sim2.run(s2); C["ZONE_units"] += 1
                if len(S2) - 1 < T or any(S2[t][:N] != S[min(t, T)] for t in range(len(S2))): C["ZONE"] += 1
            G3 = extend(G, rng, 2, neg=True)
            if G3 is None: continue
            s3 = tuple(s0) + tuple(G3["start"][N:]); S3 = Sim(G3).run(s3); C["ZONE_NEG_units"] += 1
            if len(S3) - 1 < T or any(S3[t][:N] != S[min(t, T)] for t in range(len(S3))): C["ZONE_NEG"] += 1
    print("ZONE %d (units: %d (extension, start)) ZONE_NEG %d of %d" % (C["ZONE"], C["ZONE_units"], C["ZONE_NEG"], C["ZONE_NEG_units"]))
    # INSERT-PASS: every corpus/EXTRA genome, every level L in 1..d-1, stored start + 2 random starts: insert80's pair at level L
    import subprocess
    sys.path.insert(0, H); import importlib
    C = collections.Counter()
    for p, G in load_corpus() + [(q, G) for q, G, _ in extra]:
        if not is_lr(G): continue
        N = G["N"]; d = N // 2; sim = Sim(G)
        for L in range(1, d):
            G2 = insert_pass(G, L); sim2 = Sim(G2)
            for s0 in [tuple(G["start"])] + [tuple(rng.randint(0, 1) for _ in range(N)) for _ in range(2)]:
                S = sim.run(s0); s2 = s0[:2 * L] + (0, 1) + s0[2 * L:]; S2 = sim2.run(s2); C["INS_units"] += 1
                old = lambda z: z[:2 * L] + z[2 * L + 2:]
                if len(S2) != len(S) or any(old(S2[t]) != S[t] or S2[t][2 * L:2 * L + 2] != (0, 1) for t in range(len(S))): C["INS"] += 1
                Fo = stats(sim, S)[1]; Fn = stats(sim2, S2)[1]
                if Fn[L] != Fn[L - 1] or Fn[:L] + Fn[L + 1:] != Fo: C["INS_F"] += 1
                G3 = insert_pass(G, L, inv=True); S3 = Sim(G3).run(s0[:2 * L] + (1, 0) + s0[2 * L:])
                if len(S3) != len(S) or any(old(S3[t]) != S[t] for t in range(len(S))): C["INS_NEG"] += 1
    print("INSERT %d INSERT_F %d (units: %d (genome, level L, start)) INSERT_NEG %d" % (C["INS"], C["INS_F"], C["INS_units"], C["INS_NEG"]))
    # slack table
    for p, G, _ in extra:
        sim = Sim(G); S = sim.run(); F, dbl, W = windows(sim, S); h = capped(F)
        row = []
        for j in range(1, min(h + 1, sim.N // 2)):
            pl = [m[1] - m[0] for (a, e, m) in W[j] if len(m) == 2]
            if len(pl) == len(W[j]) and dbl[j]: row.append("j%d:min %d need %d slack %d" % (j, min(pl), h - j, min(pl) - (h - j)))
        print("SLACK %s capped %d T %d %s" % (os.path.basename(p), h, len(S) - 1, "; ".join(row)))
if __name__ == "__main__":
    main()
