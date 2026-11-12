#!/usr/bin/env python3
"""Box 208 Addendum A (L-NEW successor 72): Lemma PLATEAU (CANDIDATE) on IDEAL-CYC, state by state; engine = level208.prep.
Reference b = the last state. A PLATEAU is a maximal interval [u, v], u < v, of states of constant Phi = (m, -|FRONT|) (level208.py);
Y := {x : class_u(x) <= m}. Must-0 counters:
  p1    (unit (vertex, state of [u, v])): a vertex of Y changes class, or a vertex outside Y has class <= m                  [(P1)]
  pclos (unit (vertex of Y, state)): its successor on the play is outside Y                                                  [(P2)]
  p2    (unit (mover of Y, gate, state)): the gate has a higher class than the mover                                         [(P3)]
  p3    (unit (Odd vertex of Y, step inside [u, v])): it changes its successor                                               [(P4)]
  p4    (unit steps s -> s+1, u <= s <= v): no mover of Y switches                                                           [(P6)]
  p5    (unit plateaus): v - u > the number of Even vertices in Y                                                            [(P7)]
Descriptive: plateaus, maxlen (longest v - u), maxpct (largest 100 (v - u) / (number of movers in Y + 1)).
Control PL_CTRL=1: Y := FRONT_u only (pclos, p2 or p4 must fire where there is a plateau).
Usage: plat208.py G.json ... | plat208.py --rand SEED COUNT MODE | plat208.py --mut SEED COUNT BASE.json"""
import sys, os, json, random, collections
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import level208, fvs202
CTRL = os.environ.get("PL_CTRL", "0")
def plateaus(P, c):
    n, T, cls, nxt, owner, succ, mv = P["n"], P["T"], P["cls"], P["nxt"], P["owner"], P["succ"], P["movers"]
    phis = []
    for t in range(T):
        lag = [x for x in range(n) if cls[t][x] != cls[T][x]]
        if not lag: phis.append(None); continue
        m = min(cls[t][x] for x in lag); phis.append((m, frozenset(x for x in lag if cls[t][x] == m)))
    t = 0
    while t < T:
        if phis[t] is None: t += 1; continue
        u = t
        while t + 1 < T and phis[t + 1] == phis[u]: t += 1
        v = t; t += 1
        if v == u: continue
        m, J = phis[u]; Y = set(J) if CTRL == "1" else set(x for x in range(n) if cls[u][x] <= m); c["plateaus"] += 1
        for s in range(u, v + 1):
            for x in range(n):
                if CTRL != "1" and ((x in Y) != (cls[s][x] <= m) or (x in Y and cls[s][x] != cls[u][x])): c["p1"] += 1
                if x in Y and nxt[s][x] not in Y: c["pclos"] += 1
            for x in mv:
                if x in Y: c["p2"] += sum(1 for y in succ[x] if cls[s][y] > cls[s][x])
        for s in range(u, v): c["p3"] += sum(1 for g in Y if owner[g] == 1 and nxt[s][g] != nxt[s + 1][g])
        for s in range(u, v + 1):
            if not any(nxt[s][x] != nxt[s + 1][x] for x in mv if x in Y): c["p4"] += 1
        nm = sum(1 for x in mv if x in Y); ne = sum(1 for x in Y if owner[x] == 0)
        if v - u > ne: c["p5"] += 1
        c["maxlen"] = max(c["maxlen"], v - u); c["maxpct"] = max(c["maxpct"], (100 * (v - u)) // (nm + 1))
KEYS = ("p1", "pclos", "p2", "p3", "p4", "p5", "plateaus", "maxlen", "maxpct")
if __name__ == "__main__":
    a = sys.argv[1:]; c = collections.Counter()
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
            g += 1; plateaus(level208.prep(G), c)
        print("plat rand", mode, "ctrl", CTRL, "seed", seed, "genomes", g, " ".join("%s %d" % (k, c[k]) for k in KEYS), flush=True)
    elif a[0] == "--mut":
        sys.path.insert(0, os.path.join(HERE, "..", "box203")); os.environ["AC_FREE"] = "1"; import aclimb203
        seed, cnt, base = int(a[1]), int(a[2]), a[3]; rng = random.Random(seed); G0 = json.load(open(base))
        for i in range(cnt):
            G = G0
            for _ in range(rng.randint(1, 6)): G = aclimb203.mutate(G, -1, rng)
            plateaus(level208.prep(G), c)
        print("plat mut", os.path.basename(base), "ctrl", CTRL, "seed", seed, "samples", cnt, " ".join("%s %d" % (k, c[k]) for k in KEYS), flush=True)
    else:
        for fn in a:
            c = collections.Counter(); plateaus(level208.prep(json.load(open(fn))), c)
            print("plat", os.path.basename(fn), "ctrl", CTRL, " ".join("%s %d" % (k, c[k]) for k in KEYS), flush=True)
