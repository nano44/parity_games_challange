"""L-RED box 19 (produced on Fable 5.1): per-search piece map of a k-part union (parts = vertex ranges [0,c1), [c1,c2), ...).
For every q-search s: the depth-0 chain as (pos, |R|, rank, |V|, part letters, piece); for every transition s -> s+1: the first
changed position p0, its type N/G/O, the piece at p0 before and after with part letters; and the tangles sptl learned in search s
(position, vertices, escapes) with the parts of their vertices and escapes. Chains from L-ALG's unmodified b12_pot / b12_core
(via ../xctx/xscore.py), tangle hook as in ../xctx/tlog.py. NOTE: fixd_stealentry.run renumbers vertices by priority (stable:
sorted by (prio, v); oink: stdsort.oink_order), so the solver's sets are in solver indices; this script maps them back to FILE vertex
ids (idx[i]) before labelling. partmask.py / tlog.py print solver indices. Usage: DTL_ORDER=.. piecemap.py G.pg c1 [c2 ...]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "xctx")); sys.setrecursionlimit(100000)
import xscore as X
from comb.neststar import nest_star
B = X.B


class TL(B.CH):
    def sptl(self, V, R, p):
        t0 = len(self.tv); r = super().sptl(V, R, p)
        for t in range(t0, len(self.tv)):
            self.tl = getattr(self, "tl", []); self.tl.append((len(getattr(self, "log", [])), len(self.calls) - 1, sorted(w for w, _ in self.tv[t]), sorted(self.tout[t])))
        return r


g = X.distinct(X.pg.read(sys.argv[1])); C = X.controller(g); order = os.environ.get("DTL_ORDER", "stable")
cuts = [int(x) for x in sys.argv[2:]] + [g.n]
part = lambda v: chr(65 + next(k for k, c in enumerate(cuts) if v < c))
lab = lambda vs: "".join(sorted({part(v) for v in vs})) or "-"
saved = B.SE.SE; B.SE.SE = TL
try:
    d = B.SE.run(g, order)
finally:
    B.SE.SE = saved
if order == "oink":
    from stdsort import oink_order
    idx = oink_order(g.prio)
else:
    idx = sorted(range(g.n), key=lambda v: (g.prio[v], v))
F = lambda vs: sorted(idx[i] for i in vs)
tl = [(a, b, F(c), F(e)) for a, b, c, e in getattr(d, "tl", [])]
qs = [(s, [(R, r, V, frozenset(F(pc))) for R, r, V, pc in X.states(B.chain(calls, g.n))]) for s, (ph, calls) in enumerate(d.log) if ph[0] == 1 - C]
print(f"# {os.path.basename(sys.argv[1])} n {g.n} C {C} order {order} cuts {cuts} q-searches {len(qs)}")
L = [ch for _, ch in qs]; P = []
for i, (x, y) in enumerate(zip(L, L[1:])):
    p0 = next((p for p in range(max(len(x), len(y))) if p >= len(x) or p >= len(y) or x[p] != y[p]), None)
    if p0 is not None: P.append(p0)
print("# P =", ",".join(map(str, P)), "NEST*", nest_star(tuple(P)))
for k, (s, ch) in enumerate(qs):
    print(f"s{k} (global {s}): " + " ".join(f"{j}:{len(R)}/{'S' if r == g.n + 2 else r}/{len(V)}/{lab(pc)}{sorted(pc)}" for j, (R, r, V, pc) in enumerate(ch)))
    for t in tl:
        if t[0] == s: print(f"    learn pos {t[1]}: {lab(t[2])}{t[2]} esc {lab(t[3])}{t[3]}")
    if k + 1 < len(qs):
        y = qs[k + 1][1]; x = ch
        p0 = next((p for p in range(max(len(x), len(y))) if p >= len(x) or p >= len(y) or x[p] != y[p]), None)
        if p0 is None: print("    -> chain-keeping"); continue
        ty = "N" if p0 >= len(x) or p0 >= len(y) else ("G" if (x[p0][1], x[p0][2]) == (y[p0][1], y[p0][2]) else "O")
        bef = f"{lab(x[p0][3])}{sorted(x[p0][3])} rank {'S' if x[p0][1] == g.n + 2 else x[p0][1]}" if p0 < len(x) else "(none)"
        aft = f"{lab(y[p0][3])}{sorted(y[p0][3])} rank {'S' if y[p0][1] == g.n + 2 else y[p0][1]}" if p0 < len(y) else "(none)"
        print(f"    -> transition #{k} at p0 {p0} type {ty}: before {bef}; after {aft}")
