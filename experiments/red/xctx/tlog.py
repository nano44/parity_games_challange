"""Per q-search: depth-0 chain (|R|, rank, |V|, piece) and the tangles sptl learns (search, position, vertices, escapes).
Usage: DTL_ORDER=.. tlog.py G.pg"""
import sys, os
sys.setrecursionlimit(100000); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import xscore as X
B = X.B


class TL(B.CH):
    def sptl(self, V, R, p):
        t0 = len(self.tv); r = super().sptl(V, R, p)
        for t in range(t0, len(self.tv)):
            self.tl = getattr(self, "tl", []); self.tl.append((len(getattr(self, "log", [])), len(self.calls) - 1, sorted(w for w, _ in self.tv[t]), self.tout[t]))
        return r


g = X.distinct(X.pg.read(sys.argv[1])); C = X.controller(g); order = os.environ.get("DTL_ORDER", "stable")
saved = B.SE.SE; B.SE.SE = TL
try:
    d = B.SE.run(g, order)
finally:
    B.SE.SE = saved
tl = getattr(d, "tl", [])
for s, (ph, calls) in enumerate(d.log):
    if ph[0] != 1 - C: continue
    ch = X.states(B.chain(calls, g.n))
    print(f"s{s}", [(len(R), r, len(V), sorted(pc)) for R, r, V, pc in ch])
    for x in tl:
        if x[0] == s: print(f"    learns at pos {x[1]}: {x[2]} esc {x[3]}")
