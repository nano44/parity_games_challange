"""L-RED successor 9 (box 14, produced on Opus 5.5): class climb against (SPP) (L-ALG GAP-A-M §21a, DATA: every phase has
S <= |G′|; sharp form S <= max(1, |G′| - 1)) on 𝒞^1P. S = searches of a q-phase (b12_pot.run log, unmodified), |G′| = |R_0| of
the phase's first search. Score: (max over q-phases of S - max(1, |G′| - 1), NEST, -n); > 0 is a violation of the sharp form. Usage: sppclass.py G.pg ... | [GROW=p NMAX=m]
sppclass.py climb C START.pg STEPS SEED OUTDIR"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import xscore as X, nestclass as NC
B = X.B


def score(g, order, C):
    d = B.run(g, order); q = 1 - C; ph = {}
    for p, calls in getattr(d, "log", []):
        if p[0] == q: ph.setdefault(p, []).append(calls)
    if not ph: return (-99, 0, -g.n)
    m = max(len(L) - max(1, len(L[0][0][0]) - 1) for L in ph.values())
    P, _ = NC.positions(g, order, C)
    return (m, max([NC.nest(x) for x in P.values()] or [0]), -g.n)


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
                print(it, sh, flush=True); X.pg.write(h, os.path.join(out, f"best_C{C}_s{seed}.pg"))
                if sh[0] > 0: X.pg.write(h, os.path.join(out, f"SPP_VIOL_C{C}_n{h.n}_s{seed}_{it}.pg")); print("VIOLATION", it, flush=True)
            g, sg = h, sh
    print("final", sg)


if __name__ == "__main__":
    sys.setrecursionlimit(100000); order = os.environ.get("DTL_ORDER", "stable")
    if sys.argv[1] == "climb":
        climb(int(sys.argv[2]), sys.argv[3], int(sys.argv[4]), int(sys.argv[5]), sys.argv[6], order); sys.exit(0)
    for f in sys.argv[1:]:
        g = X.distinct(X.pg.read(f)); C = X.controller(g)
        print(os.path.basename(f), "score", score(g, order, C) if C is not None else "NOT IN CLASS")
