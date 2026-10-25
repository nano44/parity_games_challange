#!/usr/bin/env python3
"""Box 41: hill-climb against CONJECTURE INTO (into17.analyse). Fitness = (INTO_FAIL + CASE1 + CASE2, INTO_FAIL_NOGATE,
−min_into (fewest gates into R̄ at a post-rise state with r > L), post-rise states). Mutations: soclimb.mutate on the game; with START=1
the start pair (σ0, τ0) is part of the genome (mutated with probability 1/3; recorded with every save). Hits saved as OUT_hit*.pg/.json.
Usage: intoclimb17.py seed secs OUT seed.pg   (env START=1 for start-pair search)"""
import sys, os, random, time, json, io, contextlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "so"))
import sox, pg, into17
from soclimb import mutate, dump
NEG = (-10 ** 9,) * 4
def fit(G, st):
    if any(not s for s in G[2]): return NEG, None
    try:
        g = pg.Game(*G)
        if len(sox.oddchoice(g)) != 1: return NEG, None
        if st is not None and any(st[v] not in g.succ[v] for v in range(g.n)): return NEG, None
        C, ex, N = into17.analyse(g, st)
    except AssertionError: raise
    except Exception: return NEG, None
    if not C.get("rises"): return (0, 0, -10 ** 6, 0), (C, ex)
    return (C.get("INTO_FAIL", 0) + C.get("CASE1", 0) + C.get("CASE2", 0), C.get("INTO_FAIL_NOGATE", 0), -C.get("min_into", 10 ** 6), C.get("post_states_r>L", 0)), (C, ex)
if __name__ == "__main__":
    seed, secs, out, f0 = int(sys.argv[1]), float(sys.argv[2]), sys.argv[3], sys.argv[4]; rng = random.Random(seed)
    g = sox.load(f0); G = [list(g.prio), list(g.owner), [list(x) for x in g.succ]]
    st = [rng.choice(g.succ[v]) for v in range(g.n)] if os.environ.get("START") == "1" else None
    f, r = fit(G, st); print("start", f, flush=True); t0 = time.time(); it = 0; nh = 0
    while time.time() - t0 < secs:
        it += 1
        if st is not None and rng.random() < 1 / 3: H = G; st2 = list(st); v = rng.randrange(len(st2)); st2[v] = rng.choice(G[2][v])
        else:
            H = mutate(rng, G); st2 = None if st is None else [x if x in H[2][v] else rng.choice(H[2][v]) for v, x in enumerate(st)]
        fh, rh = fit(H, st2)
        if fh != NEG and (fh[0] > 0 or fh[1] > 0) and nh < 6:
            nh += 1; dump(H, f"{out}_hit{nh}.pg"); json.dump(dict(start=st2, C=rh[0], ex=[str(e) for e in rh[1][:8]]), open(f"{out}_hit{nh}.json", "w"))
            print("HIT", nh, it, fh, rh[0], [e for e in rh[1] if e[0] != "x"][:3], flush=True)
        if fh >= f:
            if fh > f:
                print(f"{time.time()-t0:6.0f}s it {it} fit {fh}", flush=True); dump(H, out + ".pg")
                json.dump(dict(start=st2), open(out + ".json", "w"))
            G, f, st = H, fh, st2
    print("FINAL", f, it, flush=True)
