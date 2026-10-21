"""L-RED successor 10 (box 16, produced on Opus 5.5): graded climb toward NEST* >= 4 on 𝒞^1P (R48 §4).
Positions P per q-phase come from ../xctx/nestclass.py positions() (b12_pot.chain / b12_core.states, unmodified); NEST* from
../xctx/comb/neststar.py. Score: (max NEST*, MASS, S, -n), MASS = sum over positions p of the phase of (1 + NEST*(window_p))^2,
window_p = elements > p strictly between p's first and last occurrence (rewards nesting inside windows, which NEST* alone does not).
Usage: DTL_ORDER=.. starclimb.py G.pg ... | [GROW=p NMAX=m] starclimb.py climb C START.pg STEPS SEED OUTDIR"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "xctx"))
import xscore as X
import nestclass as NC
from comb.neststar import nest_star


def wnest(P, p):
    i0 = P.index(p); i1 = len(P) - 1 - P[::-1].index(p)
    gap = tuple(x for x in P[i0 + 1:i1] if x > p)
    return 1 + nest_star(gap) if gap else (1 if i1 > i0 else 0)


def mass(P):
    return sum(wnest(P, p) ** 2 for p in set(P))


def score(g, order, C):
    Ps, d = NC.positions(g, order, C)
    if not Ps: return (0, 0, 0, -g.n)
    best = max(Ps.values(), key=lambda P: (nest_star(tuple(P)), mass(P), len(P)))
    return (nest_star(tuple(best)), mass(best), len(best) + 1, -g.n)


def climb(C, start, steps, seed, out, order):
    rnd = random.Random(seed); g = X.distinct(X.pg.read(start)); os.makedirs(out, exist_ok=True)
    sg = score(g, order, C); print("start", sg, flush=True); GROW = float(os.environ.get("GROW", "0")); NMAX = int(os.environ.get("NMAX", "60"))
    for it in range(steps):
        h = X.grow(g, C, rnd) if GROW and g.n < NMAX and rnd.random() < GROW else X.mutate(g, C, g.n + 2, rnd)
        if h is None: continue
        h = X.distinct(h)
        try:
            sh = score(h, order, C)
        except RecursionError:
            continue
        if sh >= sg:
            if sh > sg:
                print(it, sh, flush=True)
                if sh[0] >= 4 or sh[:2] > sg[:2]: X.pg.write(h, os.path.join(out, f"star_C{C}_s{seed}_{sh[0]}_{sh[1]}_{sh[2]}.pg"))
            g, sg = h, sh
        if it % 200 == 0: print("hb", it, sg, g.n, flush=True)
    X.pg.write(g, os.path.join(out, f"final_C{C}_s{seed}.pg")); print("final", sg)


if __name__ == "__main__":
    sys.setrecursionlimit(100000); order = os.environ.get("DTL_ORDER", "stable")
    if sys.argv[1] == "climb":
        climb(int(sys.argv[2]), sys.argv[3], int(sys.argv[4]), int(sys.argv[5]), sys.argv[6], order); sys.exit(0)
    for f in sys.argv[1:]:
        g = X.distinct(X.pg.read(f)); C = X.controller(g)
        if C is None: print(os.path.basename(f), "NOT IN CLASS"); continue
        Ps, d = NC.positions(g, order, C); print(os.path.basename(f), "n", g.n, "C", C, order, "score", score(g, order, C), "P", Ps)
