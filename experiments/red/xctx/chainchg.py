"""L-RED successor 9 (box 14, produced on Opus 5.5): climb against (CHAIN-CHANGE) on 𝒞^1P (L-ALG GAP-A-M §33a, l-alg 9ab9a3e6):
"every transition of a q-phase changes the depth-0 states". A violation is a transition s -> s+1 of a q-phase (q = 1 - C) whose
depth-0 chains (R_j, rank_j, V_j, piece_j) are identical (b12_pot.run / chain, b12_core.states, unmodified).
Graded score: (violations, -min dist, -Σ dist over the 3 closest transitions, transitions), dist(x, y) = #positions whose state
differs + Σ |piece symmetric difference| / n (positions missing in one chain count as differing, piece = all).
Usage: DTL_ORDER=.. chainchg.py G.pg ... | chainchg.py climb C START.pg STEPS SEED OUTDIR"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import xscore as X


def dist(x, y, n):
    m = max(len(x), len(y)); d = 0.0
    for p in range(m):
        a = x[p] if p < len(x) else None; b = y[p] if p < len(y) else None
        if a == b: continue
        d += 1 + len((a[3] if a else frozenset()) ^ (b[3] if b else frozenset())) / n
    return d


def score(g, order, C):
    d = X.B.run(g, order); q = 1 - C; phases = {}
    for ph, calls in getattr(d, "log", []): phases.setdefault(ph, []).append(X.states(X.B.chain(calls, g.n)))
    D = []
    for ph, L in phases.items():
        if ph[0] != q: continue
        D += [dist(L[s], L[s + 1], g.n) for s in range(len(L) - 1)]
    D.sort()
    return (sum(1 for x in D if x == 0), -round(D[0], 3) if D else -99, -round(sum(D[:3]), 3), len(D))


def climb(C, start, steps, seed, out, order):
    rnd = random.Random(seed); g = X.distinct(X.pg.read(start)); P = g.n + 2; os.makedirs(out, exist_ok=True)
    sg = score(g, order, C); print("start", sg, flush=True)
    for it in range(steps):
        h = X.mutate(g, C, P, rnd)
        if h is None: continue
        h = X.distinct(h)
        try:
            sh = score(h, order, C)
        except RecursionError:
            continue
        if sh >= sg:
            if sh > sg:
                print(it, sh, flush=True); X.pg.write(h, os.path.join(out, f"best_C{C}_s{seed}.pg"))
                if sh[0] > 0: X.pg.write(h, os.path.join(out, f"CHG_VIOL_C{C}_n{h.n}_s{seed}_{it}.pg")); print("VIOLATION", it, flush=True)
            g, sg = h, sh
    print("final", sg)


if __name__ == "__main__":
    sys.setrecursionlimit(100000); order = os.environ.get("DTL_ORDER", "stable")
    if sys.argv[1] == "climb":
        climb(int(sys.argv[2]), sys.argv[3], int(sys.argv[4]), int(sys.argv[5]), sys.argv[6], order); sys.exit(0)
    for f in sys.argv[1:]:
        g = X.distinct(X.pg.read(f)); C = X.controller(g)
        print(os.path.basename(f), "n", g.n, "C", C, "order", order, "score", score(g, order, C) if C is not None else "NOT IN CLASS")
