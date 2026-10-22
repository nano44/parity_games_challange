#!/usr/bin/env python3
"""L-RED box 10 (produced on Opus 5.5): hill climb for a REGION CLOCK: a game whose root context (depth 0, R = G') has
round-1 step prefixes that change at every consecutive visit pair of one phase (the clock a lag gadget needs; chainfam's
clock changes only the threshold loop). Fitness = (changing pairs, visits) of the best phase, by the UNMODIFIED L-ALG model
(dtl_stealdepth.run_game). Mutations: re-draw one vertex's edges / priority / owner. Usage: rclock.py SEED N STEPS OUT.pg [START.pg]"""
import sys, os, random
A = os.path.join(os.environ["LALG_DIR"], "experiments", "alg"); sys.path.insert(0, A); sys.path.insert(0, os.path.join(A, "..", "harness"))
for k_ in ("RM_EXCL", "RM_PREF", "RM_LIGHT"): os.environ.setdefault(k_, "1")
os.environ.setdefault("RM_DV", "0")
import pg, dtl_stealdepth as SD
sys.setrecursionlimit(100000)
def fit(g):
    try: d = SD.run_game(g, os.environ.get("DTL_ORDER", "stable"))
    except Exception: return (-1, 0)
    if not all(w is not None for w in d.win): return (-2, 0)
    best = (0, 0)
    for ph in SD.FD.phase_rows(d):
        rcs = [rc for r in ph for rc in r["recs"] if rc["key"][0] == 0 and len(rc["key"][1]) == len(ph[0]["G"])]
        ch = 0
        for a, b in zip(rcs, rcs[1:]):
            pa = {k: v for k, v in a.get("pref", {}).items() if k[0] == 1}; pb = {k: v for k, v in b.get("pref", {}).items() if k[0] == 1}
            ch += pa != pb
        best = max(best, (ch, len(rcs)))
    return best
def rand_game(rng, n):
    pr = [rng.randrange(2 * n) for _ in range(n)]; ow = [rng.randrange(2) for _ in range(n)]
    sc = [sorted(set(rng.sample(range(n), rng.randint(1, 3)))) for _ in range(n)]
    return pg.Game(pr, ow, sc)
def mutate(rng, g):
    pr, ow, sc = list(g.prio), list(g.owner), [list(s) for s in g.succ]; n = len(pr); v = rng.randrange(n); r = rng.random()
    if r < 0.5: sc[v] = sorted(set(rng.sample(range(n), rng.randint(1, 3))))
    elif r < 0.75: pr[v] = rng.randrange(2 * n)
    else: ow[v] ^= 1
    return pg.Game(pr, ow, sc)
if __name__ == "__main__":
    seed, n, steps, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; rng = random.Random(seed)
    g = pg.read(sys.argv[5]) if len(sys.argv) > 5 else rand_game(rng, n); f = fit(g)
    for it in range(steps):
        h = mutate(rng, g) if rng.random() < 0.97 else rand_game(rng, n); fh = fit(h)
        if fh >= f:
            if fh > f: print(it, fh, flush=True); pg.write(h, out)
            g, f = h, fh
    print("final", f)
