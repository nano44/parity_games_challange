"""L-RED successor 9 (box 14, produced on Opus 5.5): tangle births per search_rec depth in the q-phase of 𝒞^1P games, and the
(CHAIN-CHANGE) climb fitness that rewards depth >= 1 learning. Wraps b12_pot.CH (unmodified) by subclassing.
Usage: DTL_ORDER=.. deep.py G.pg ... | deep.py climb C START.pg STEPS SEED OUTDIR"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import xscore as X, chainchg as CC
B = X.B


class DCH(B.CH):
    def sptl(self, V, R, p):
        t0 = self.tangles; r = super().sptl(V, R, p)
        if self.tangles != t0 and hasattr(self, "phase"):
            self.births = getattr(self, "births", []); self.births.append((self.phase, len(getattr(self, "log", [])), getattr(self, "_dep", 0), self.tangles - t0))
        return r


def run(g, order):
    saved = B.SE.SE; B.SE.SE = DCH
    try:
        return B.SE.run(g, order)
    finally:
        B.SE.SE = saved


def score(g, order, C):
    d = run(g, order); q = 1 - C; phases = {}
    for ph, calls in getattr(d, "log", []): phases.setdefault(ph, []).append(X.states(X.B.chain(calls, g.n)))
    D = []
    for ph, L in phases.items():
        if ph[0] == q: D += [CC.dist(L[s], L[s + 1], g.n) for s in range(len(L) - 1)]
    deep = sum(k for ph, s, dep, k in getattr(d, "births", []) if ph[0] == q and dep >= 1)
    D.sort()
    return (sum(1 for x in D if x == 0), deep, -round(D[0], 3) if D else -99, len(D)), d


def climb(C, start, steps, seed, out, order):
    rnd = random.Random(seed); g = X.distinct(X.pg.read(start)); P = g.n + 2; os.makedirs(out, exist_ok=True)
    sg = score(g, order, C)[0]; print("start", sg, flush=True)
    for it in range(steps):
        h = X.mutate(g, C, P, rnd)
        if h is None: continue
        h = X.distinct(h)
        try:
            sh = score(h, order, C)[0]
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
        if C is None: print(os.path.basename(f), "NOT IN CLASS"); continue
        sc, d = score(g, order, C)
        print(os.path.basename(f), "n", g.n, "C", C, order, "score", sc, "births(depth>=1, all phases)", [(ph, s, dep, k) for ph, s, dep, k in getattr(d, "births", []) if dep >= 1][:6])
