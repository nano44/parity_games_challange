#!/usr/bin/env python3
"""Box 206 Addendum A (L-NEW successor 70): Lemma DIV counters on IDEAL-CYC. For every step t and vertex v with Lambda fixed and E changed:
p := the first vertex of v's play at t-1 whose successor at t differs. Must-0 (TOTALS, unit (v, t)): nop (no such p before the first w),
lamp (Lambda(p) != w at t-1 or t), symp (E(p) symmetric difference != E(v)'s), dep (p's depth > v's), kind (p neither a switching mover
nor a flipping gate). cases = number of (v, t) checked. Control DIV_CTRL=1: p := the vertex after p on the old play (symp/kind must fire).
Usage: div206.py G.json ... | div206.py --rand {k1,rand} SEED COUNT"""
import sys, os, json, random, collections
HERE = os.path.dirname(os.path.abspath(__file__)); R = os.path.abspath(os.path.join(HERE, ".."))
sys.path[:0] = [R + "/box203", R + "/box191", R + "/box202"]
import gfc203, idealcyc
CTRL = os.environ.get("DIV_CTRL", "0")

def census(G, c):
    H, n, E, V, gates = gfc203.hist_ideal(G); T = len(H) - 1
    h, s0, movers, inv = idealcyc.build(G); st = idealcyc.run(G, cap=20000); gi = {}
    for x in range(G["N"]):
        for v in h.succ[movers[x]]: gi[(x, inv[v])] = v
    emask = 0
    for k, v in V.items():
        if isinstance(k, tuple) and k[0] == "e": emask |= E.bit[v]
    def succ_of(t):
        cur = list(s0)
        for x in range(G["N"]): cur[movers[x]] = gi[(x, st[t][x])]
        sb = H[t][1]
        return [cur[v] if h.owner[v] == 0 else sb[v] for v in range(n)]
    S = [succ_of(t) for t in range(T + 1)]; mset = set(movers)
    def ch(v, t):
        e0, e1 = H[t - 1][0][v][1] & emask, H[t][0][v][1] & emask
        z = (e0 ^ e1).bit_length() - 1; return e0 ^ e1, z, bin((e0 | e1) >> (z + 1)).count("1")
    for t in range(1, T + 1):
        for v in range(n):
            w = H[t - 1][0][v][0]
            if H[t][0][v][0] != w or (H[t - 1][0][v][1] & emask) == (H[t][0][v][1] & emask): continue
            c["cases"] += 1; u = v; seen = set(); p = None
            while u not in seen and u != w:
                seen.add(u)
                if S[t][u] != S[t - 1][u]: p = u; break
                u = S[t - 1][u]
            if p is None: c["nop"] += 1; continue
            if CTRL == "1": p = S[t - 1][p]
            if H[t - 1][0][p][0] != w or H[t][0][p][0] != w: c["lamp"] += 1; continue
            dv, zv, d = ch(v, t)
            if (H[t - 1][0][p][1] & emask) == (H[t][0][p][1] & emask): c["symp"] += 1; continue
            dp, zp, d2 = ch(p, t)
            if dp != dv: c["symp"] += 1
            if d2 > d: c["dep"] += 1
            if not ((p in mset and S[t][p] != S[t - 1][p]) or (p in gates and S[t][p] != S[t - 1][p])): c["kind"] += 1
    c["genomes"] += 1

KEYS = ("genomes", "cases", "nop", "lamp", "symp", "dep", "kind")
if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] == "--rand":
        mode, seed, cnt = a[1], int(a[2]), int(a[3]); rng = random.Random(seed); c = collections.Counter()
        import rand191, fvs202
        os.environ["K1_MODE"] = "1"
        import k1srch202
        while c["genomes"] < cnt:
            if mode == "rand": G = rand191.rgen(rng, rng.randint(1, 6), rng.randint(1, 3), rng.randint(2, 3))
            else:
                G = k1srch202.mk(rng)
                if G is None or fvs202.kfvs(G)[0] != 1: continue
            census(G, c)
        print(mode, "seed", seed, "ctrl", CTRL, " ".join(f"{k} {c[k]}" for k in KEYS), flush=True)
    else:
        for f in a:
            c = collections.Counter(); census(json.load(open(f)), c)
            print(os.path.basename(f), "ctrl", CTRL, " ".join(f"{k} {c[k]}" for k in KEYS), flush=True)
