"""L-RED box 16 (produced on Opus 5.5): random WRAPPER search toward NEST* >= 4 on 𝒞^1P (R48 §4).
Adds K in 1..KMAX new vertices to a base class game (random priority up to max+8, random owner; a q-vertex gets one successor,
a C-vertex 1-3 successors among all vertices) and E in 0..3 edges from random base C-vertices into the new vertices; keeps class
membership (xscore.inclass). Scores with starclimb.score. Saves every game with NEST* > base or (NEST*, MASS) > best.
Usage: DTL_ORDER=.. [KMAX=3] wrapsearch.py BASE.pg TRIALS SEED OUTDIR"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "xctx"))
import xscore as X
import starclimb as SC


def wrap(g, C, rnd, kmax):
    n0 = g.n; k = rnd.randint(1, kmax); n = n0 + k; top = max(g.prio)
    prio = list(g.prio) + [rnd.randrange(top + 9) for _ in range(k)]
    owner = list(g.owner) + [rnd.randint(0, 1) for _ in range(k)]
    succ = [list(s) for s in g.succ]
    for v in range(n0, n):
        succ.append([rnd.randrange(n)] if owner[v] != C else sorted(set(rnd.sample(range(n), rnd.randint(1, 3)))))
    cs = [v for v in range(n0) if owner[v] == C]
    for _ in range(rnd.randint(0, 3)):
        if cs: v = rnd.choice(cs); succ[v] = sorted(set(succ[v] + [rnd.randrange(n0, n)]))
    h = X.pg.Game(prio, owner, succ)
    return X.distinct(h) if X.inclass(h, C) else None


if __name__ == "__main__":
    sys.setrecursionlimit(100000); order = os.environ.get("DTL_ORDER", "stable"); kmax = int(os.environ.get("KMAX", "3"))
    base, trials, seed, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    rnd = random.Random(seed); g = X.distinct(X.pg.read(base)); C = X.controller(g); os.makedirs(out, exist_ok=True)
    sb = SC.score(g, order, C); best = sb; print("base", sb, flush=True)
    for it in range(trials):
        h = wrap(g, C, rnd, kmax)
        if h is None: continue
        try:
            sh = SC.score(h, order, C)
        except RecursionError:
            continue
        if sh[0] > sb[0] or sh[:2] > best[:2] or (os.environ.get("FIT") == "wrap" and sh[1] >= 2):
            print(it, sh, flush=True); X.pg.write(h, os.path.join(out, f"wrap_s{seed}_{it}_{sh[0]}_{sh[1]}.pg"))
        if sh[:2] > best[:2]: best = sh
        if it % 500 == 0: print("hb", it, best, flush=True)
    print("final", best)
