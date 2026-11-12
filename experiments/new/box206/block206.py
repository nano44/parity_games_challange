#!/usr/bin/env python3
"""Box 206 Addendum B (L-NEW successor 70): TOP-BLOCK e-sets on IDEAL-CYC. Top block := the e-vertices of the gates of the movers of the
highest level L (b of them, the b most relevant e-vertices under the e-order of gamma3.build). For each mover x: Dtop(x) := the number of
distinct E_t(x) ∩ block over the run. CONJECTURE BLOCK-DESC (tested here): Dtop(x) <= F0(b) := 1 + b(b + 1)/2 (RESULTS R121's DESC-POLY
value, the no-ascent bound) at every mover. Counters: excess := max over movers of Dtop - F0(b) (BLOCK-DESC: <= 0), Dtop (max), b,
pfall (unit (mover, step): the block part falls lexicographically at fixed Lambda; must be 0, R121 E-MON). Usage: block206.py G.json ... |
block206.py --rand {k1,rand} SEED COUNT [dump.json: first genome with excess > 0]"""
import sys, os, json, random, collections
HERE = os.path.dirname(os.path.abspath(__file__)); R = os.path.abspath(os.path.join(HERE, ".."))
sys.path[:0] = [R + "/box203", R + "/box191", R + "/box202"]
import gfc203

def census(G):
    H, n, E, V, gates = gfc203.hist_ideal(G); T = len(H) - 1
    L = max(G["lev"]); top = [V[("e", (x, k))] for x in range(G["N"]) if G["lev"][x] == L for k in range(len(G["opts"][x]))]
    tm = 0
    for v in top: tm |= E.bit[v]
    b = len(top); F0 = 1 + b * (b + 1) // 2; best = 0; pfall = 0
    for x in range(G["N"]):
        v = V[("x", x)]; s = [H[t][0][v][1] & tm for t in range(T + 1)]
        for t in range(1, T + 1):
            if H[t][0][v][0] == H[t - 1][0][v][0] and s[t] != s[t - 1] and not ((s[t] ^ s[t - 1]) & s[t]) > ((s[t] ^ s[t - 1]) & s[t - 1]): pfall += 1
        best = max(best, len(set(s)))
    return dict(T=T, L=L, b=b, Dtop=best, F0=F0, excess=best - F0, pfall=pfall)

if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] == "--rand":
        mode, seed, cnt = a[1], int(a[2]), int(a[3]); dump = a[4] if len(a) > 4 else None
        rng = random.Random(seed); c = collections.Counter(); c["excess"] = -10 ** 9
        import rand191, fvs202
        os.environ["K1_MODE"] = "1"
        import k1srch202
        while c["genomes"] < cnt:
            if mode == "rand": G = rand191.rgen(rng, rng.randint(1, 6), rng.randint(1, 3), rng.randint(2, 3))
            else:
                G = k1srch202.mk(rng)
                if G is None or fvs202.kfvs(G)[0] != 1: continue
            r = census(G); c["genomes"] += 1; c["pfall"] += r["pfall"]; c["Dtop"] = max(c["Dtop"], r["Dtop"])
            if r["excess"] > c["excess"]: c["excess"] = r["excess"]; c["at_b"] = r["b"]
            if dump and r["excess"] > 0 and not os.path.exists(dump): json.dump(G, open(dump, "w"))
        print(mode, "seed", seed, dict(c), flush=True)
    else:
        for f in a: print(os.path.basename(f), census(json.load(open(f))), flush=True)
