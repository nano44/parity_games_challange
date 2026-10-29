#!/usr/bin/env python3
"""L-RED successor 24: priority/edge search on a fixed two-wave topology (FB-LIN attack). Gadget vertex priorities and optional
edges are genes; chain c_1..c_m (odd priorities 1..2m+1 unless gene) with edges {q1, c_{i-1}, c_{i+1}}, c_0 = s1, c_{m+1} = R.
Fitness = 100*(f(m2)-f(m1)) + f(m2). Usage: topo2.py seed secs OUT [m1 m2]"""
import sys, random, json, time, copy
from dsl import build
from fbphase import fstats
GV = ["T", "q1", "T1", "x1", "Y", "s1", "Z1", "qp", "Tp", "xp", "Xp", "y", "A", "R", "B", "Pz"]
OWN = dict(T=1, q1=1, T1=0, x1=0, Y=1, s1=0, Z1=1, qp=1, Tp=0, xp=0, Xp=1, y=0, A=0, R=1, B=0, Pz=1)
# candidate edges per vertex (base edges always present marked by first entries in BASE)
BASE = dict(T=["T"], q1=["T1", "x1"], T1=["T"], x1=["Y", "CM"], Y=["T"], s1=["Z1", "qp"], Z1=["T"], qp=["Tp", "xp"], Tp=["T"],
            xp=["Xp"], Xp=["T"], y=["A", "CM"], A=["q1"], R=["y", "B"], B=["T"], Pz=["T"])
OPT = dict(s1=["q1"], xp=["CM", "C1", "s1", "Pz"], A=["Pz", "T"], B=["Pz", "qp"], Tp=["Pz"], T1=["Pz"], y=["Pz"], Xp=["Pz"],
           x1=["Pz"], Z1=["Pz"], Y=["Pz"])
def spec(G, m):
    S = []
    for v in GV:
        succ = list(BASE[v]) + [e for e in OPT.get(v, []) if G["opt"].get(v + ">" + e)]
        succ = ["c%d" % m if e == "CM" else "c1" if e == "C1" else e for e in succ]
        st = G["st"].get(v)
        if st == "CM": st = "c%d" % m
        if st == "C1": st = "c1"
        if st not in succ: st = succ[0]
        S.append((v, OWN[v], G["pr"][v], succ, st if len(succ) > 1 else None))
    for i in range(1, m + 1):
        succ = ["q1", "s1" if i == 1 else "c%d" % (i - 1), "R" if i == m else "c%d" % (i + 1)]
        S.append(("c%d" % i, 0, 2 * i + 1, succ, "q1"))
    return S
import trace as T
def taustar(g, st):
    it, fb, ph, mp, s, t, h = T.run(g, st, cap=4000, log=lambda *a: None)
    return (st[0], {v: t[v] for v in range(g.n) if g.owner[v] == 1})
def f(G, m):
    try:
        g, st, nm = build(spec(G, m)); st = taustar(g, st); return fstats(g, st, cap=2000)[0]
    except AssertionError: return -1
    except RuntimeError: return -1
def fit(G, m1, m2):
    a = f(G, m1); b = f(G, m2)
    if a < 0 or b < 0: return (-10 ** 6, a, b)
    return (100 * (b - a) + b, a, b)
SEEDPR = dict(T=1, q1=105, T1=120, x1=104, Y=131, s1=126, Z1=129, qp=107, Tp=124, xp=106, Xp=109, y=128, A=110, R=111, B=122, Pz=113)
def rnd(rng):
    G = {"pr": dict(SEEDPR), "opt": {}, "st": {"q1": "T1", "x1": "Y", "s1": "Z1", "qp": "Tp", "y": "A", "R": "B"}}
    return G
def mutate(rng, G):
    G = copy.deepcopy(G); r = rng.randrange(10)
    if r < 6:
        v = rng.choice(GV[1:]); G["pr"][v] = rng.randrange(100, 160)
    elif r < 8:
        v = rng.choice(list(OPT)); e = rng.choice(OPT[v]); k = v + ">" + e; G["opt"][k] = not G["opt"].get(k)
    else:
        v = rng.choice([x for x in GV if len(BASE[x]) > 1 or x in OPT]); G["st"][v] = rng.choice(BASE[v] + OPT.get(v, []))
    ps = [G["pr"][v] for v in GV]
    if len(set(ps)) < len(ps): return mutate(rng, G)
    return G
if __name__ == "__main__":
    seed, secs, out = int(sys.argv[1]), float(sys.argv[2]), sys.argv[3]
    m1, m2 = (int(sys.argv[4]), int(sys.argv[5])) if len(sys.argv) > 5 else (6, 12)
    rng = random.Random(seed); t0 = time.time()
    cur = rnd(rng); cf = fit(cur, m1, m2); best, bf = cur, cf; print("start", cf, flush=True)
    while time.time() - t0 < secs:
        H = cur
        for _ in range(rng.choice((1, 1, 2, 3))): H = mutate(rng, H)
        F = fit(H, m1, m2)
        if F[0] >= cf[0] or rng.random() < 0.01:
            cur, cf = H, F
            if F[0] > bf[0]:
                best, bf = H, F; print("%.0fs" % (time.time() - t0), F, flush=True); json.dump(best, open(out, "w"))
    print("BEST", bf)
