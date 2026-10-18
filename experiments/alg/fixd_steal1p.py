"""L-ALG succ. 9 (box 11, produced on Opus 5.5), GAP-A-M §27: relevant steals in ONE-PLAYER games. Class C: player C owns every
vertex with >= 2 successors. Steals are counted with dtl_stealdepth.analyze (RM_EXCL=1 RM_PREF=1 RM_LIGHT=1 RM_DV=0 model, the
tool that measured lagfam's depth); max k >= 1 means some (step, tangle) has a relevant steal in some context and phase.
Modes:
  scan  C NMIN NMAX COUNT SEED ORDER          random class-C games; prints how many have max k >= 1, and the max (k, depth)
  climb C N P STEPS SEED ORDER OUTDIR         hill-climb in class C for (max k, max depth, searches)
Every game with max k >= 1 is written to OUTDIR (climb) or ./steal1p_found/ (scan) with its seed."""
import sys, os, random
os.environ.setdefault("RM_EXCL", "1"); os.environ.setdefault("RM_PREF", "1"); os.environ.setdefault("RM_LIGHT", "1"); os.environ.setdefault("RM_DV", "0")
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, zielonka, dtl_stealdepth as SD
from fixd_oneplayer import start, mutate


def measure(g, order):
    d = SD.run_game(g, order)
    W = [None] * g.n
    for i, w in enumerate(d.win): W[d.idx[i]] = w          # d.idx maps the model's index to the input id
    ok = W == list(zielonka.solve(g))
    mk, md, nc = SD.analyze(d, "", {}, None)
    return (mk, md, d.iterations), ok


def main():
    sys.setrecursionlimit(100000)
    mode = sys.argv[1]
    if mode == "scan":
        C, nmin, nmax, count, seed, order = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]), sys.argv[7]
        rnd = random.Random(seed); hit = 0; best = (0, 0, 0); bad = 0
        for i in range(count):
            N = rnd.randint(nmin, nmax); P = rnd.choice([2, 3, 4, 6, N])
            g = start(C, N, P, rnd); sc, ok = measure(g, order)
            if not ok: bad += 1
            if sc[0] >= 1:
                hit += 1; os.makedirs("steal1p_found", exist_ok=True); pg.write(g, f"steal1p_found/C{C}_{order}_s{seed}_{i}.pg")
            best = max(best, sc)
        print(f"scan C={C} n={nmin}..{nmax} games={count} seed={seed} order={order}: with a steal {hit}, best (k, depth, searches) {best}, model != Zielonka {bad}")
    else:
        C, N, P, steps, seed, order, out = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]), sys.argv[7], sys.argv[8]
        rnd = random.Random(seed); g = start(C, N, P, rnd); best, ok = measure(g, order)
        for s in range(steps):
            h = mutate(g, C, P, rnd)
            if h is None: continue
            sc, ok = measure(h, order)
            if not ok: print("MODEL != ZIELONKA", s, flush=True); continue
            if sc >= best:
                if sc > best: print(s, sc, flush=True)
                best, g = sc, h
        os.makedirs(out, exist_ok=True); pg.write(g, os.path.join(out, f"steal1p_C{C}_n{N}_P{P}_s{seed}_{order}.pg")); print("best", best)


if __name__ == "__main__":
    main()
