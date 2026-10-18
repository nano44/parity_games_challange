"""L-RED successor 9 (box 14, produced on Opus 5.5): graded fitness and climb against (XCTX@p0) on 𝒞^1P (L-ALG GAP-A-M §35a,
l-alg 9ab9a3e6). Uses L-ALG's modules UNMODIFIED from $LALG_DIR/experiments/alg (b12_pot.run / chain, b12_core.states,
fixd_oneplayer.mutate / inclass, fixd_ctx1p.distinct).
For every transition s -> s+1 of a q-phase (q = 1 - C, C the controller) with first changed depth-0 position p0, context R, new set
N (case O: piece_{s+1}(p0); case P: piece_{s+1}(p0) minus piece_s(p0)), and every earlier s' <= s with R' := R_{p0}(s') != R:
  f1  |R'| = |R|                          (same-size different context at p0)
  f2  f1 and sig_{s'}(p0) = sig_{s+1}(p0) (the pairs (XCTX@p0) quantifies over)
  ov2 |N ∩ union of f2 pieces|; ov1 |N ∩ piece_{s'}(p0)| over f1 pairs (any signature)
A VIOLATION of (XCTX@p0) is a transition with N ⊆ union of f2 pieces (N nonempty).
Score (lexicographic): (violations, max ov2/|N|, Σov2, Σf2, Σov1, Σf1, transitions).
Usage: [LALG_DIR=..] DTL_ORDER=stable|oink xscore.py G.pg ...            (report per file)
       DTL_ORDER=.. xscore.py climb C START.pg STEPS SEED OUTDIR          (class-preserving climb; DIST after every move)"""
import sys, os, random
LALG = os.environ.get("LALG_DIR", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))   # default: the in-tree experiments/alg copy
A = os.path.join(LALG, "experiments", "alg"); sys.path.insert(0, A); sys.path.insert(0, os.path.join(A, "..", "harness"))
import pg, b12_pot as B
from b12_core import states
from fixd_oneplayer import mutate, inclass
from fixd_ctx1p import distinct


def controller(g):
    return 0 if inclass(g, 0) else (1 if inclass(g, 1) else None)


def analyse(g, order, C):
    d = B.run(g, order); q = 1 - C
    phases = {}
    for ph, calls in getattr(d, "log", []): phases.setdefault(ph, []).append(states(B.chain(calls, g.n)))
    out = []
    for ph, L in phases.items():
        if ph[0] != q: continue
        for s in range(len(L) - 1):
            x, y = L[s], L[s + 1]
            p0 = next((p for p in range(max(len(x), len(y))) if p >= len(x) or p >= len(y) or x[p] != y[p]), None)
            if p0 is None or p0 >= len(y): continue
            R, r, V, piece = y[p0]; sg = (r, len(R), len(V))
            caseO = not (p0 < len(x) and x[p0][0] == R and (x[p0][1], x[p0][2]) == (r, V))
            N = piece if caseO else piece - x[p0][3]
            f1 = f2 = ov1 = 0; U2 = set()
            for z in L[:s + 1]:
                if p0 >= len(z) or z[p0][0] == R or len(z[p0][0]) != len(R): continue
                f1 += 1; ov1 += len(N & z[p0][3])
                if (z[p0][1], len(z[p0][0]), len(z[p0][2])) == sg: f2 += 1; U2 |= z[p0][3]
            out.append(dict(ph=ph, s=s, p0=p0, case="O" if caseO else "P", N=N, f1=f1, f2=f2, ov1=ov1, ov2=len(N & U2),
                            viol=bool(N) and N <= U2))
    return out, d


def score(g, order, C):
    T = analyse(g, order, C)[0]
    return (sum(t["viol"] for t in T), round(max([t["ov2"] / len(t["N"]) for t in T if t["N"]] or [0]), 3),
            sum(t["ov2"] for t in T), sum(t["f2"] for t in T), sum(t["ov1"] for t in T), sum(t["f1"] for t in T), len(T))


def grow(g, C, rnd):
    """class-preserving move: add one vertex (random owner, priority, successors; a q-vertex gets one successor) and one edge
    into it from a random C-vertex (if any)."""
    n = g.n; prio, owner, succ = list(g.prio) + [rnd.randrange(n + 2)], list(g.owner) + [rnd.randint(0, 1)], [list(x) for x in g.succ]
    succ.append([rnd.randrange(n + 1)] if owner[n] != C else sorted(set(rnd.sample(range(n + 1), min(n + 1, rnd.randint(1, 3))))))
    cs = [v for v in range(n) if owner[v] == C]
    if cs: v = rnd.choice(cs); succ[v] = sorted(set(succ[v] + [n]))
    h = pg.Game(prio, owner, succ)
    return h if inclass(h, C) else None


def climb(C, start, steps, seed, out, order):
    rnd = random.Random(seed); g = distinct(pg.read(start)); P = g.n + 2; os.makedirs(out, exist_ok=True)
    sg = score(g, order, C); print("start", sg, flush=True); GROW = float(os.environ.get("GROW", "0")); NMAX = int(os.environ.get("NMAX", "60"))
    for it in range(steps):
        h = grow(g, C, rnd) if GROW and g.n < NMAX and rnd.random() < GROW else mutate(g, C, g.n + 2, rnd)
        if h is None: continue
        h = distinct(h)
        try:
            sh = score(h, order, C)
        except RecursionError:
            continue
        if sh >= sg:
            if sh > sg:
                print(it, sh, flush=True); pg.write(h, os.path.join(out, f"best_C{C}_s{seed}.pg"))
                if sh[0] > 0: pg.write(h, os.path.join(out, f"XCTX_VIOL_C{C}_n{h.n}_s{seed}_{it}.pg")); print("VIOLATION", it, flush=True)
            g, sg = h, sh
    print("final", sg)


if __name__ == "__main__":
    sys.setrecursionlimit(100000); order = os.environ.get("DTL_ORDER", "stable")
    if sys.argv[1] == "climb":
        climb(int(sys.argv[2]), sys.argv[3], int(sys.argv[4]), int(sys.argv[5]), sys.argv[6], order); sys.exit(0)
    for f in sys.argv[1:]:
        g = distinct(pg.read(f)); C = controller(g)
        if C is None: print(os.path.basename(f), "NOT IN CLASS"); continue
        print(os.path.basename(f), "n", g.n, "C", C, "order", order, "score", score(g, order, C))
