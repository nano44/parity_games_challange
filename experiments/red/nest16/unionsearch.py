"""L-RED box 16 (produced on Opus 5.5): DISJOINT UNION search toward NEST* >= 4 on 𝒞^1P. The base B (a NEST*-3 class game) is kept
unchanged; a random component A on K in KMIN..KMAX new vertices (random owner, priority up to max(B)+12; a q-vertex gets one successor,
a C-vertex 1-3 successors, all inside A) is added with no edges between A and B. Scored by starclimb.score (FIT honoured).
Saves NEST* > base and every new best. Usage: DTL_ORDER=.. [KMIN=2 KMAX=6] unionsearch.py BASE.pg TRIALS SEED OUTDIR"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "xctx"))
import xscore as X, starclimb as SC


def union(g, C, rnd, kmin, kmax):
    n0 = g.n; k = rnd.randint(kmin, kmax); n = n0 + k; top = max(g.prio)
    prio = list(g.prio) + [rnd.randrange(top + 13) for _ in range(k)]
    owner = list(g.owner) + [rnd.randint(0, 1) for _ in range(k)]
    succ = [list(s) for s in g.succ]
    for v in range(n0, n):
        succ.append([rnd.randrange(n0, n)] if owner[v] != C else sorted(set(rnd.sample(range(n0, n), rnd.randint(1, min(3, k))))))
    h = X.pg.Game(prio, owner, succ)
    return X.distinct(h) if X.inclass(h, C) else None


if __name__ == "__main__":
    sys.setrecursionlimit(100000); order = os.environ.get("DTL_ORDER", "stable")
    kmin, kmax = int(os.environ.get("KMIN", "2")), int(os.environ.get("KMAX", "6"))
    base, trials, seed, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    rnd = random.Random(seed); g = X.distinct(X.pg.read(base)); C = X.controller(g); os.makedirs(out, exist_ok=True)
    sb = SC.score(g, order, C); best = sb; print("base", sb, flush=True)
    for it in range(trials):
        h = union(g, C, rnd, kmin, kmax)
        if h is None: continue
        try:
            sh = SC.score(h, order, C)
        except RecursionError:
            continue
        if sh[0] > sb[0] or sh[:2] > best[:2]:
            print(it, sh, flush=True); X.pg.write(h, os.path.join(out, f"union_s{seed}_{it}_{sh[0]}_{sh[1]}.pg"))
        if sh[:2] > best[:2]: best = sh
        if it % 500 == 0: print("hb", it, best, flush=True)
    print("final", best)
