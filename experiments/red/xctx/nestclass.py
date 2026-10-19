"""L-RED successor 9 (box 14, produced on Opus 5.5): class climb toward a COMPOUNDING counter on 𝒞^1P (Lead 22:30Z: (CTX⁺) directly).
For each q-phase the positions p0 of the transitions' first changed depth-0 positions (b12_pot.chain / b12_core.states, unmodified)
give NEST (experiments/red/tcpert/carryclimb.py nest(): nested counter depth) and CARRIES. Score: (max NEST, max CARRIES,
max q-phase length, -n). Usage: DTL_ORDER=.. nestclass.py G.pg ... | [GROW=p NMAX=m] nestclass.py climb C START.pg STEPS SEED OUTDIR"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import xscore as X
B = X.B


def nest(pos):
    if not pos: return 0
    best = 1
    for p in set(pos):
        idx = [i for i, x in enumerate(pos) if x == p]
        for i0, i1 in zip(idx, idx[1:]):
            gap = [x for x in pos[i0 + 1:i1] if x > p]
            if gap: best = max(best, 1 + nest(gap))
    return best


def carries(pos):
    best = 0
    for p in set(pos):
        idx = [i for i, x in enumerate(pos) if x == p]
        best = max(best, sum(1 for i0, i1 in zip(idx, idx[1:]) if sum(1 for x in pos[i0 + 1:i1] if x > p) >= 2))
    return best


def positions(g, order, C):
    d = B.run(g, order); q = 1 - C; phases = {}
    for ph, calls in getattr(d, "log", []): phases.setdefault(ph, []).append(X.states(B.chain(calls, g.n)))
    out = {}
    for ph, L in phases.items():
        if ph[0] != q: continue
        P = []
        for x, y in zip(L, L[1:]):
            p0 = next((p for p in range(max(len(x), len(y))) if p >= len(x) or p >= len(y) or x[p] != y[p]), None)
            if p0 is not None: P.append(p0)
        out[ph] = P
    return out, d


def score(g, order, C):
    P, d = positions(g, order, C)
    if not P: return (0, 0, 0, -g.n)
    if os.environ.get("STAR") == "1":   # R46: rank by NEST* (comb/neststar.py) instead of NEST
        from comb.neststar import nest_star
        return (max(nest_star(tuple(p)) for p in P.values()), max(carries(p) for p in P.values()), max(len(p) + 1 for p in P.values()), -g.n)
    return (max(nest(p) for p in P.values()), max(carries(p) for p in P.values()), max(len(p) + 1 for p in P.values()), -g.n)


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
            if sh > sg: print(it, sh, flush=True); X.pg.write(h, os.path.join(out, f"nest_C{C}_s{seed}_{sh[0]}_{sh[2]}.pg"))
            g, sg = h, sh
    X.pg.write(g, os.path.join(out, f"final_C{C}_s{seed}.pg")); print("final", sg)


if __name__ == "__main__":
    sys.setrecursionlimit(100000); order = os.environ.get("DTL_ORDER", "stable")
    if sys.argv[1] == "climb":
        climb(int(sys.argv[2]), sys.argv[3], int(sys.argv[4]), int(sys.argv[5]), sys.argv[6], order); sys.exit(0)
    for f in sys.argv[1:]:
        g = X.distinct(X.pg.read(f)); C = X.controller(g)
        if C is None: print(os.path.basename(f), "NOT IN CLASS"); continue
        P, d = positions(g, order, C); print(os.path.basename(f), "n", g.n, "C", C, order, "score", score(g, order, C), "positions", P)
