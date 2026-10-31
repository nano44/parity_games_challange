#!/usr/bin/env python3
"""L-RED successor 39 (R167): hill-climb over mk167g.py genomes. Objective on (K, m2, m3): (E3 switches inside the longest W-run, |F|),
where E3 switches = Even switches at rrr_t; the multiplying target is E3 re-armed once per E2 step in EVERY phase (~ K m2 m3 / 2).
Also reports driver switches (hs2 / hps2) and |F|. ESC is fixed per run (arg), LOW free. Usage: climb167.py K m2 m3 ESC iters seed OUT"""
import sys, os, json, random, re
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "xcn"))
import mk167g, xcn, n5b
pg = xcn.pg
K, m2, m3, ESC, IT, seed = map(int, sys.argv[1:7]); OUT = sys.argv[7]
CL = mk167g.IDX + mk167g.ONE
def score(gen):
    order, pr, own, succ, s0, t0 = mk167g.game(K, m2, m3, gen)
    g = pg.Game(pr, own, succ)
    try:
        tr, fb = xcn.trace(g, s0, t0, cap=20000); runs, W = xcn.wruns(g, tr, fb)
    except Exception as e: return (-1, 0, 0)
    F = max(runs, key=len); e3 = dr = 0
    E3 = [i for i, v in enumerate(order) if v.startswith("rrr")]; D = [order.index("hs2"), order.index("hps2")]
    for k in F[:-1]:
        s, s2 = tr[k][0], tr[k + 1][0]
        e3 += sum(1 for v in E3 if s[v] != s2[v]); dr += sum(1 for v in D if s[v] != s2[v])
    return (e3, len(F) - 1, dr)
def rnd(rng):
    return {"ESC": ESC, "LOW": rng.random() < 0.5, "mk": {c: (None if rng.random() < 0.2 else [rng.random(), rng.uniform(-3, 3), rng.randrange(2)]) for c in CL}}
def mutate(gen, rng):
    g2 = json.loads(json.dumps(gen))
    for _ in range(rng.randrange(1, 4)):
        r = rng.random()
        if r < 0.05: g2["LOW"] = not g2["LOW"]; continue
        c = rng.choice(CL); v = g2["mk"][c]
        if v is None or rng.random() < 0.1: g2["mk"][c] = None if (v is not None and rng.random() < 0.5) else [rng.random(), rng.uniform(-3, 3), rng.randrange(2)]
        else:
            q = rng.random()
            if q < 0.3: v[2] = 1 - v[2]
            elif q < 0.65: v[0] = min(1, max(0, v[0] + rng.gauss(0, 0.1)))
            else: v[1] = max(-5, min(5, v[1] + rng.gauss(0, 1)))
    return g2
if __name__ == "__main__":
    rng = random.Random(seed)
    best = json.load(open(os.environ["SEED_JSON"])) if os.environ.get("SEED_JSON") else rnd(rng)
    best["ESC"] = ESC; bs = score(best); print("start", bs, flush=True)
    for it in range(IT):
        c = mutate(best, rng); cs = score(c)
        if cs[:2] >= bs[:2]:
            if cs[:2] > bs[:2]: print(it, "best (E3, |F|, drivers)", cs, flush=True); json.dump(c, open(OUT + ".json", "w"))
            best, bs = c, cs
    print("FINAL", bs); json.dump(best, open(OUT + ".json", "w"))
