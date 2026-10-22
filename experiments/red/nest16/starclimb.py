"""L-RED successor 10 (box 16, produced on Opus 5.5): graded climb toward NEST* >= 4 on 𝒞^1P (R48 §4).
Positions P per q-phase come from ../xctx/nestclass.py positions() (b12_pot.chain / b12_core.states, unmodified); NEST* from
../xctx/comb/neststar.py. Score: (max NEST*, MASS, S, -n); FIT=seg: see segscore(); FIT=wrap: see wrapscore(); FIT=pool: see poolscore(), MASS = sum over positions p of the phase of (1 + NEST*(window_p))^2,
window_p = elements > p strictly between p's first and last occurrence (rewards nesting inside windows, which NEST* alone does not).
Usage: DTL_ORDER=.. starclimb.py G.pg ... | [GROW=p NMAX=m] starclimb.py climb C START.pg STEPS SEED OUTDIR"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "xctx"))
import xscore as X
import nestclass as NC
from comb.neststar import nest_star


def wnest(P, p):
    i0 = P.index(p); i1 = len(P) - 1 - P[::-1].index(p)
    gap = tuple(x for x in P[i0 + 1:i1] if x > p)
    return 1 + nest_star(gap) if gap else (1 if i1 > i0 else 0)


def mass(P):
    return sum(wnest(P, p) ** 2 for p in set(P))


def segscore(g, order, C):
    """FIT=seg: (NEST*, max segment NEST* after an O-rise at b > min(P), 0, MASS, S, -n)."""
    import segstat as S
    best = (0, 0, 0, 0, 0, -g.n)
    for ph, T in S.trans(g, order, C):
        P = [b for b, _ in T]
        if not P: continue
        so = max([s for (b, t, s) in S.segs(T) if t == "O" and b > min(P)] or [0])
        best = max(best, (nest_star(tuple(P)), so, 0, mass(P), len(P) + 1, -g.n))
    return best


def wrapscore(g, order, C):
    """FIT=wrap: (NEST*, W, MASS, S, -n). W = max over positions b with window NEST* wnest(P, b) = max_b wnest of
    [a position < b rises before b's first occurrence] + [a position < b rises after b's last occurrence] (2 means NEST* + 1)."""
    best = (0, 0, 0, 0, -g.n)
    Ps, d = NC.positions(g, order, C)
    for P in Ps.values():
        if not P: continue
        top = max(wnest(P, b) for b in set(P)); W = 0
        for b in set(P):
            if wnest(P, b) != top: continue
            i0 = P.index(b); i1 = len(P) - 1 - P[::-1].index(b)
            W = max(W, int(any(x < b for x in P[:i0])) + int(any(x < b for x in P[i1 + 1:])))
        best = max(best, (nest_star(tuple(P)), W, mass(P), len(P) + 1, -g.n))
    return best


def poolscore(g, order, C):
    """FIT=pool: (NEST*, max learning positions in one search, searches with >= 2 learning positions, MASS, S, -n)."""
    import learnpos as LP
    Ps, d = NC.positions(g, order, C)
    if not Ps: return (0, 0, 0, 0, 0, -g.n)
    P = max(Ps.values(), key=lambda P: (nest_star(tuple(P)), mass(P), len(P)))
    per = LP.pools(g, order)
    return (nest_star(tuple(P)), max(per or [0]), sum(1 for x in per if x >= 2), mass(P), len(P) + 1, -g.n)


def score(g, order, C):
    if os.environ.get("FIT") == "pool": return poolscore(g, order, C)
    if os.environ.get("FIT") == "seg": return segscore(g, order, C)
    if os.environ.get("FIT") == "wrap": return wrapscore(g, order, C)
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
