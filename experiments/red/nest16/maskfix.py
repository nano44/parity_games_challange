"""L-RED box 19 correction (produced on Opus 5.5): R50 §6's partmask statistics, recomputed with solver indices mapped back to file
ids (as in piecemap.py) next to the unmapped values partmask.py used. Per instance and order: fraction of depth-0 pieces (over all
q-searches) that mix >= 2 parts; fraction of chain-changing transitions whose changed pieces touch ALL parts. Chains from L-ALG's
unmodified b12_pot / b12_core via ../xctx/xscore.py. Usage: maskfix.py G.pg cut1 [cut2 ...]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "xctx")); sys.setrecursionlimit(100000)
import xscore as X
B = X.B
g = X.distinct(X.pg.read(sys.argv[1])); C = X.controller(g); cuts = [int(x) for x in sys.argv[2:]] + [g.n]; K = len(cuts)
part = lambda v: next(k for k, c in enumerate(cuts) if v < c)
for order in ("stable", "oink"):
    d = B.run(g, order)
    idx = __import__("stdsort").oink_order(g.prio) if order == "oink" else sorted(range(g.n), key=lambda v: (g.prio[v], v))
    L = [X.states(B.chain(c, g.n)) for ph, c in d.log if ph[0] == 1 - C]
    out = []
    for name, F in (("unmapped", lambda vs: set(vs)), ("mapped", lambda vs: {idx[i] for i in vs})):
        pcs = [F(st[3]) for ch in L for st in ch if st[3]]
        mixed = sum(1 for pc in pcs if len({part(v) for v in pc}) >= 2)
        tr = allp = 0
        for x, y in zip(L, L[1:]):
            ch = [p for p in range(max(len(x), len(y))) if p >= len(x) or p >= len(y) or x[p] != y[p]]
            if not ch: continue
            tr += 1; ps = set()
            for p in ch:
                for z in (x, y):
                    if p < len(z): ps |= {part(v) for v in F(z[p][3])}
            allp += (len(ps) == K)
        out.append(f"{name}: mixed pieces {mixed}/{len(pcs)} = {mixed/len(pcs):.2f}, transitions touching all {K} parts {allp}/{tr}")
    print(f"{os.path.basename(sys.argv[1])} {order}: " + " | ".join(out), flush=True)
