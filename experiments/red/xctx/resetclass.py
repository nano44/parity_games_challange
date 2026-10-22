"""L-RED successor 9 (box 15, produced on Opus 5.5): R45 (N3b) regrowth detector and climb on 𝒞^1P. For a q-phase, at each
transition s -> s+1 with first changed position l (b12_pot.chain / b12_core.states, unmodified) whose context R_l is unchanged:
  A   = piece_l(s+1) - piece_l(s)  (absorbed: a carry, (N1))
  Rel = piece_l(s) - piece_l(s+1)  (RELEASED to lower positions: regrowth (N3b); needs an outcome change at l)
The release is PRODUCTIVE if, before the next transition at a position <= l, a tangle containing a released vertex is learned at a
position > l (the lower level re-learns on the returned vertex: a reset that is not mere extension of a shrinking set).
Score: (#productive releases, NEST, S, -n) over the q-phases (max). Usage: DTL_ORDER=.. resetclass.py G.pg ... |
[GROW=p NMAX=m] resetclass.py climb C START.pg STEPS SEED OUTDIR"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import xscore as X, nestclass as NC
B = X.B


class TL(B.CH):
    def sptl(self, V, R, p):
        t0 = len(self.tv); r = super().sptl(V, R, p)
        for t in range(t0, len(self.tv)):
            self.tl = getattr(self, "tl", []); self.tl.append((len(getattr(self, "log", [])), len(self.calls) - 1, frozenset(w for w, _ in self.tv[t])))
        return r


def analyse(g, order, C):
    saved = B.SE.SE; B.SE.SE = TL
    try:
        d = B.SE.run(g, order)
    finally:
        B.SE.SE = saved
    q = 1 - C; tl = getattr(d, "tl", []); out = []
    idx = [s for s, (ph, _) in enumerate(d.log) if ph[0] == q]
    byph = {}
    for s in idx: byph.setdefault(d.log[s][0], []).append(s)
    for ph, S in byph.items():
        L = [X.states(B.chain(d.log[s][1], g.n)) for s in S]; P = []; ev = []
        for i in range(len(L) - 1):
            x, y = L[i], L[i + 1]
            l = next((p for p in range(max(len(x), len(y))) if p >= len(x) or p >= len(y) or x[p] != y[p]), None)
            if l is None: continue
            P.append(l)
            if l >= len(x) or l >= len(y) or x[l][0] != y[l][0]: continue
            A = y[l][3] - x[l][3]; Rel = x[l][3] - y[l][3]
            if not A and not Rel: continue
            nxt = next((j for j in range(i + 1, len(L) - 1) if _first(L[j], L[j + 1]) is not None and _first(L[j], L[j + 1]) <= l), len(L) - 1)
            prod = sum(1 for (s, pos, t) in tl if s in S[i + 1:nxt + 1] and pos > l and t & Rel)
            ev.append(dict(i=i, l=l, A=len(A), rel=len(Rel), prod=prod))
        out.append((ph, P, ev, len(L)))
    return out, d


def _first(x, y):
    return next((p for p in range(max(len(x), len(y))) if p >= len(x) or p >= len(y) or x[p] != y[p]), None)


def score(g, order, C):
    A = analyse(g, order, C)[0]
    if not A: return (0, 0, 0, -g.n)
    best = (0, 0, 0)
    for ph, P, ev, S in A:
        best = max(best, (sum(1 for e in ev if e["prod"] > 0), NC.nest(P), S))
    return best + (-g.n,)


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
            if sh > sg: print(it, sh, flush=True); X.pg.write(h, os.path.join(out, f"rel_C{C}_s{seed}_{sh[0]}_{sh[1]}_{sh[2]}.pg"))
            g, sg = h, sh
    print("final", sg)


if __name__ == "__main__":
    sys.setrecursionlimit(100000); order = os.environ.get("DTL_ORDER", "stable")
    if sys.argv[1] == "climb":
        climb(int(sys.argv[2]), sys.argv[3], int(sys.argv[4]), int(sys.argv[5]), sys.argv[6], order); sys.exit(0)
    for f in sys.argv[1:]:
        g = X.distinct(X.pg.read(f)); C = X.controller(g)
        if C is None: print(os.path.basename(f), "NOT IN CLASS"); continue
        A, d = analyse(g, order, C)
        print(os.path.basename(f), "n", g.n, order, "score", score(g, order, C))
        for ph, P, ev, S in A:
            print("  phase", ph, "S", S, "positions", P, "events (i, l, |A|, |Rel|, productive)", [(e["i"], e["l"], e["A"], e["rel"], e["prod"]) for e in ev])
