"""L-RED box 17 (produced on Opus 5.5): per q-phase, the number of distinct depth-0 positions at which sptl learns a tangle within
one search ("learning pools"): max and histogram over searches. Uses ../xctx/tlog.py's sptl hook (L-ALG's b12_pot unmodified).
Usage: DTL_ORDER=.. learnpos.py G.pg ..."""
import sys, os, collections
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "xctx"))
sys.setrecursionlimit(100000)
import xscore as X
B = X.B


class TL(B.CH):
    def sptl(self, V, R, p):
        t0 = len(self.tv); r = super().sptl(V, R, p)
        for t in range(t0, len(self.tv)):
            self.tl = getattr(self, "tl", []); self.tl.append((len(getattr(self, "log", [])), len(self.calls) - 1))
        return r


def pools(g, order):
    C = X.controller(g); saved = B.SE.SE; B.SE.SE = TL
    try:
        d = B.SE.run(g, order)
    finally:
        B.SE.SE = saved
    tl = getattr(d, "tl", []); qs = [s for s, (ph, calls) in enumerate(d.log) if ph[0] == 1 - C]
    per = [len({c for s2, c in tl if s2 == s}) for s in qs]
    return per


if __name__ == "__main__":
    order = os.environ.get("DTL_ORDER", "stable")
    for f in sys.argv[1:]:
        g = X.distinct(X.pg.read(f)); per = pools(g, order)
        print(os.path.basename(f), order, "max learning positions per search", max(per or [0]), "per search", per)
