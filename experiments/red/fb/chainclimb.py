#!/usr/bin/env python3
"""L-RED successor 24: structured climb for FB-LIN (f <= n per phase). Game = a small mutable gadget (K vertices) + a chain of m Even
vertices c_1..c_m (edges: c_{i-1} if FWD, c_{i+1} if BWD, every gadget vertex in S; c_0 = gadget X0, c_{m+1} = gadget X1; priorities in
the lowest band, pattern genes). Gadget edges may point at c_1 or c_m. Start pair = genes (full start; every entry is an existing edge).
Fitness = 100*(f(m2) - f(m1)) + f(m2): a slope above (m2 - m1) means more than one fallback wave per chain vertex.
Usage: chainclimb.py seed secs OUTPREFIX [K] [m1 m2]"""
import sys, os, random, time, json, copy
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "sel"))
import trace as T
from fbphase import fstats

def build(G, m):
    K = len(G["own"]); n = K + m
    C = lambda i: K + i - 1                      # chain vertex c_i, i = 1..m
    def tgt(x):                                  # gadget edge target token
        return C(1) if x == "c1" else C(m) if x == "cm" else x
    prio = [0] * n; owner = [0] * n; succ = [None] * n
    for v in range(K):
        owner[v] = G["own"][v]; prio[v] = G["pr"][v] if G["pr"][v] <= 1 else 2 * m + 4 + G["pr"][v]; succ[v] = sorted(set(tgt(x) for x in G["succ"][v]))
    for i in range(1, m + 1):
        v = C(i); owner[v] = 0
        par = G["cpar"] if G["cpar"] < 2 else i % 2
        prio[v] = 2 * (i if G["cinc"] else m + 1 - i) + par
        s = set(G["S"])
        if G["fwd"]: s.add(G["X0"] if i == 1 else C(i - 1))
        if G["bwd"]: s.add(G["X1"] if i == m else C(i + 1))
        succ[v] = sorted(s)
    sig, tau = {}, {}
    for v in range(K):
        if len(succ[v]) > 1:
            w = tgt(G["st"][v]) if G["st"][v] is not None else None
            if w in succ[v]: (sig if owner[v] == 0 else tau)[v] = w
    for i in range(1, m + 1):
        v = C(i); c = G["cst"]
        w = (G["X0"] if i == 1 else C(i - 1)) if c == "f" else (G["X1"] if i == m else C(i + 1)) if c == "b" else c
        if w in succ[v]: sig[v] = w
    return T.pg.Game(prio, owner, succ), (sig, tau)

def valid(G):
    K = len(G["own"])
    if not all(G["succ"][v] for v in range(K)): return False
    if not (G["S"] or G["fwd"] or G["bwd"]): return False
    return True

TAUSTAR = "--taustar" in sys.argv
def fval(G, m):
    g, st = build(G, m)
    try:
        if TAUSTAR:
            it, fb, ph, mp, s, t, h = T.run(g, st, cap=4000, log=lambda *a: None)
            st = (st[0], {v: t[v] for v in range(g.n) if g.owner[v] == 1})
        if "--total" in sys.argv:
            it, fb, ph, mp, s2, t2, h = T.run(g, st, cap=3000, log=lambda *a: None)
            if it >= 3000: return -1
            return 1000 * fstats(g, st, cap=3000)[0] + fb
        return fstats(g, st, cap=3000)[0]
    except Exception: return -1

def fit(G, m1, m2):
    if not valid(G): return -10 ** 6, 0, 0
    a = fval(G, m1)
    if a < 0: return -10 ** 6, 0, 0
    b = fval(G, m2)
    if b < 0: return -10 ** 6, 0, 0
    if "--total" in sys.argv:
        fa, fb_, ta, tb = a // 1000, b // 1000, a % 1000, b % 1000
        return 100 * min(fa - m1, fb_ - m2) + 10 * (fb_ - m2) + 3 * min(ta - m1, tb - m2) + (tb - m2), a, b
    return 100 * (b - a) + b, a, b

PR = 64
def lvl1(rng, K):
    """Seed: level-1 template (lvl1.py) + K - 7 free vertices pointing at T."""
    G = {"own": [1, 1, 0, 0, 1, 0, 1], "pr": [1, 25, 40, 24, 51, 46, 49],
         "succ": [[0], [2, 3], [0], [4, "cm"], [0], [6, 1], [0]], "st": [0, 2, 0, 4, 0, 6, 0],
         "S": [1], "X0": 5, "X1": 5, "fwd": True, "bwd": False, "cpar": 1, "cinc": 1, "cst": 1}
    for v in range(7, K):
        G["own"].append(rng.randrange(2)); G["pr"].append(rng.randrange(PR)); G["succ"].append([0]); G["st"].append(0)
    return G
def rnd(rng, K):
    toks = list(range(K)) + ["c1", "cm"]
    G = {"own": [rng.randrange(2) for _ in range(K)], "pr": [rng.randrange(PR) for _ in range(K)],
         "succ": [rng.sample(toks, rng.choice((1, 2, 2, 3))) for _ in range(K)],
         "S": rng.sample(range(K), rng.choice((0, 1, 1, 2))), "X0": rng.randrange(K), "X1": rng.randrange(K),
         "fwd": rng.random() < 0.8, "bwd": rng.random() < 0.5, "cpar": rng.randrange(3), "cinc": rng.randrange(2), "cst": "f"}
    G["st"] = [rng.choice(s) for s in G["succ"]]
    G["cst"] = rng.choice(["f", "b"] + G["S"])
    return G

def mutate(rng, G):
    G = copy.deepcopy(G); K = len(G["own"]); toks = list(range(K)) + ["c1", "cm"]
    r = rng.randrange(12); v = rng.randrange(K)
    if r == 0: G["own"][v] ^= 1
    elif r == 1: G["pr"][v] = rng.randrange(PR)
    elif r in (2, 3):
        s = G["succ"][v]; x = rng.choice(toks)
        if x in s and len(s) > 1: s.remove(x)
        elif x not in s: s.append(x)
    elif r == 4: G["st"][v] = rng.choice(G["succ"][v])
    elif r == 5:
        if v in G["S"]: G["S"].remove(v)
        else: G["S"].append(v)
    elif r == 6: G["X0"] = v
    elif r == 7: G["X1"] = v
    elif r == 8: G["fwd"] = not G["fwd"]
    elif r == 9: G["bwd"] = not G["bwd"]
    elif r == 10: G["cpar"] = rng.randrange(3); G["cinc"] = rng.randrange(2)
    else: G["cst"] = rng.choice(["f", "b"] + G["S"])
    for u in range(K):
        if G["st"][u] not in G["succ"][u]: G["st"][u] = G["succ"][u][0] if G["succ"][u] else None
    if G["cst"] not in ("f", "b") and G["cst"] not in G["S"]: G["cst"] = "f"
    return G

if __name__ == "__main__":
    seed, secs, out = int(sys.argv[1]), float(sys.argv[2]), sys.argv[3]
    K = int(sys.argv[4]) if len(sys.argv) > 4 else 9
    m1, m2 = (int(sys.argv[5]), int(sys.argv[6])) if len(sys.argv) > 6 else (5, 10)
    rng = random.Random(seed); t0 = time.time()
    best, bf = None, (-10 ** 9,)
    while time.time() - t0 < secs:
        if best is None:
            G = lvl1(rng, K) if "--lvl1" in sys.argv else rnd(rng, K); F = fit(G, m1, m2)
            if best is None or F[0] > bf[0]: best, bf = G, F
            cur, cf = G, F
        for _ in range(rng.choice((1, 1, 2, 3))): H = mutate(rng, cur)
        F = fit(H, m1, m2)
        if F[0] >= cf[0]:
            cur, cf = H, F
            if F[0] > bf[0]:
                best, bf = H, F
                print("%.0fs fit=%d f(%d)=%d f(%d)=%d" % (time.time() - t0, F[0], m1, F[1], m2, F[2]), flush=True)
                json.dump(best, open(out + ".json", "w"))
    print("BEST", bf)
