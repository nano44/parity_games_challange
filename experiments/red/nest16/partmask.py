"""L-RED box 17 (produced on Opus 5.5): masking diagnostic for a union whose parts are vertex ranges [0,n1), [n1,n2), ...
Per transition: the part owning the first changed depth-0 piece (the only one P records), and the parts with ANY changed piece.
Usage: DTL_ORDER=.. partmask.py G.pg n1 [n2 ...]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "xctx")); sys.setrecursionlimit(100000)
import xscore as X
B = X.B; order = os.environ.get("DTL_ORDER", "stable")
g = X.distinct(X.pg.read(sys.argv[1])); cuts = [int(x) for x in sys.argv[2:]] + [g.n]; C = X.controller(g)
part = lambda v: next(k for k, c in enumerate(cuts) if v < c)
lab = lambda pc: "".join(sorted({chr(65 + part(v)) for v in pc})) or "-"
d = B.run(g, order); L = [X.states(B.chain(c, g.n)) for ph, c in d.log if ph[0] == 1 - C]
for i, (x, y) in enumerate(zip(L, L[1:])):
    ch = [p for p in range(max(len(x), len(y))) if p >= len(x) or p >= len(y) or x[p] != y[p]]
    if not ch: continue
    pcs = lambda p: set((x[p][3] if p < len(x) else ())) | set((y[p][3] if p < len(y) else ()))
    print(f"s{i}->{i+1} first {ch[0]}:{lab(pcs(ch[0]))}  changed parts", "".join(sorted(set("".join(lab(pcs(p)) for p in ch)))))
