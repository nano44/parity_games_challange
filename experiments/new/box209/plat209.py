#!/usr/bin/env python3
"""Box 209 (L-NEW successor 72): Lemma PLATEAU3 (CANDIDATE) on HOW3(G), state by state. Counters p1 ... p5 are box 208's plat208.plateaus
(same code, same units) on a Gamma3 history; added here, for the TAIL [b', T3] (b' = the first state at which no vertex lags, reference
the last state):
  t1 (unit (Odd vertex, step inside [b', T3])): it changes its successor                                         [(P4) on the tail]
  t2 (unit genomes): T3 - b' > the number of Even vertices                                                       [(P7) on the tail]
  t3 (unit genomes): the run has more than (P3 + 1)(n_E3 + 1) - 1 steps, P3 = 2M(N + 4M), n_E3 = #Even vertices  [T3-ALL]
Descriptive: plateaus, maxlen, maxpct (as plat208), tail (largest T3 - b'), T (largest T3).
Engine: level208.prep(G, True) = N5'-xi from S3 on Gamma3(G) up to its first fallback; or --hist HIST.json (any engine; level208's format).
Control PL_CTRL=1 (plat208's: Y := FRONT_u only).
Usage: plat209.py G.json ... | plat209.py --hist HIST.json ... | plat209.py --rand SEED COUNT MODE | plat209.py --mut SEED COUNT BASE.json"""
import sys, os, json, random, collections
HERE = os.path.dirname(os.path.abspath(__file__))
B208 = os.environ.get("B208") or os.path.join(HERE, "..", "box208"); sys.path.insert(0, B208)
import level208, plat208, fvs202
KEYS = ("p1", "pclos", "p2", "p3", "p4", "p5", "t1", "t2", "t3", "plateaus", "maxlen", "maxpct", "tail", "T")
def one(P, c):
    plat208.plateaus(P, c)
    n, T, cls, nxt, owner = P["n"], P["T"], P["cls"], P["nxt"], P["owner"]; G = P["genome"]
    N = G["N"]; M = sum(len(o) for o in G["opts"]); nE = sum(1 for v in range(n) if owner[v] == 0)
    bp = next(t for t in range(T + 1) if all(cls[t][x] == cls[T][x] for x in range(n)))
    for s in range(bp, T): c["t1"] += sum(1 for g in range(n) if owner[g] == 1 and nxt[s][g] != nxt[s + 1][g])
    if T - bp > nE: c["t2"] += 1
    if T > (2 * M * (N + 4 * M) + 1) * (nE + 1) - 1: c["t3"] += 1
    c["tail"] = max(c["tail"], T - bp); c["T"] = max(c["T"], T)
if __name__ == "__main__":
    a = sys.argv[1:]; c = collections.Counter(); CTRL = plat208.CTRL
    if a[0] == "--rand":
        seed, cnt, mode = int(a[1]), int(a[2]), a[3]; rng = random.Random(seed); g = 0
        if mode == "k1":
            os.environ["K1_MODE"] = "1"; import k1srch202
            mk = lambda: k1srch202.mk(rng)
        else:
            import eg195
            mk = lambda: eg195.gen(rng, mode)
        while g < cnt:
            G = mk()
            if G is None or G["N"] < 2 or (mode == "k1" and fvs202.kfvs(G)[0] != 1): continue
            g += 1; one(level208.prep(G, True), c)
        print("plat3 rand", mode, "ctrl", CTRL, "seed", seed, "genomes", g, " ".join("%s %d" % (k, c[k]) for k in KEYS), flush=True)
    elif a[0] == "--mut":
        sys.path.insert(0, os.path.join(B208, "..", "box203")); os.environ["AC_FREE"] = "1"; import aclimb203
        seed, cnt, base = int(a[1]), int(a[2]), a[3]; rng = random.Random(seed); G0 = json.load(open(base))
        for i in range(cnt):
            G = G0
            for _ in range(rng.randint(1, 6)): G = aclimb203.mutate(G, -1, rng)
            one(level208.prep(G, True), c)
        print("plat3 mut", os.path.basename(base), "ctrl", CTRL, "seed", seed, "samples", cnt, " ".join("%s %d" % (k, c[k]) for k in KEYS), flush=True)
    elif a[0] == "--hist":
        for fn in a[1:]:
            c = collections.Counter(); one(level208.load(fn), c)
            print("plat3 hist", os.path.basename(fn), "ctrl", CTRL, " ".join("%s %d" % (k, c[k]) for k in KEYS), flush=True)
    else:
        for fn in a:
            c = collections.Counter(); one(level208.prep(json.load(open(fn)), True), c)
            print("plat3", os.path.basename(fn), "ctrl", CTRL, " ".join("%s %d" % (k, c[k]) for k in KEYS), flush=True)
