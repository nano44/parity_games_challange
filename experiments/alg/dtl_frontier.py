"""L-ALG (produced on Opus 5.5, 2026-10-16), GAP-A-M.md §10.3. (F) frontier test: for each transition s -> s+1 whose first depth-0 difference is at piece i (same context, result
changed), the drivers = tangles learned in s that FIRE in piece i's best_vertices in s+1. Record where each driver was
learned in s: depth-0 piece index j (or 'rec<j>' = inside the recursion of cut piece j), and the index f of the first
stable depth-0 piece after i in s. (F) says: drivers learned at piece f."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import dtl_pyref as D, pg, gen
def mk(base):
    class F(base):
        def __init__(s, *a, **k):
            super().__init__(*a, **k); s.ns = 0; s.depth = 0; s.trace = []; s.born = {}; s.piece = -1; s.recpiece = None
        def search(s, p):
            s.ns += 1; s.piece = -1; s.trace.append({"p": p, "pieces": [], "dom": s.dominions}); return super().search(p)
        def search_rec(s, R, p, depth):
            od, orp = s.depth, s.recpiece
            if depth == 1:
                s.recpiece = s.piece
                s.trace[-1].setdefault("cuts", set()).add(s.piece)     # a recursion follows only a cut (-1, Q nonempty)
            s.depth = depth; r = super().search_rec(R, p, depth); s.depth = od; s.recpiece = orp; return r
        def best_vertices(s, V, R, p):
            if s.depth == 0:
                s.piece += 1; s._fired = set(); s._inbv = True
            Rin = frozenset(R); res = super().best_vertices(V, R, p)
            if s.depth == 0:
                s._inbv = False
                s.trace[-1]["pieces"].append((Rin, res, frozenset(V), frozenset(s._fired)))
            return res
        def attractTangle(s, t, p, R, Z, Gx, maxpr):
            r = super().attractTangle(t, p, R, Z, Gx, maxpr)
            if r and getattr(s, "_inbv", False): s._fired.add(t)
            return r
        def extractTangles(s, top, R):
            b = len(s.tv); r = super().extractTangles(top, R)
            for t in range(b, len(s.tv)):
                s.born[t] = (s.ns, s.piece if s.depth == 0 else ("rec", s.recpiece))
            return r
    return F
def analyse(d, out, name=''):
    for k, (a, b) in enumerate(zip(d.trace, d.trace[1:])):
        if a["p"] != b["p"] or b["dom"] != a["dom"]: continue
        pa, pb = a["pieces"], b["pieces"]
        i = 0
        while i < min(len(pa), len(pb)) and pa[i][:3] == pb[i][:3]: i += 1
        if i >= min(len(pa), len(pb)) or pa[i][0] != pb[i][0]: continue
        if pa[i][1] != -1: continue                      # (F) is about -1 / cut pieces
        sa = k + 1                                        # search number of a (trace entries can be equal dicts)
        drivers = [t for t in pb[i][3] if d.born.get(t, (None,))[0] == sa]
        kind = "cut" if i in a.get("cuts", set()) else "domfirst"
        out.setdefault(kind + "_changes", 0); out[kind + "_changes"] += 1
        f = next((j for j in range(i + 1, len(pa)) if pa[j][1] == 1), None)
        for t in drivers:
            where = d.born[t][1]
            out["drivers"] += 1
            out.setdefault(kind + "_drivers", 0); out[kind + "_drivers"] += 1
            if where != f and not isinstance(where, tuple):
                out.setdefault(kind + "_later", 0); out[kind + "_later"] += 1
            if where == f: out["at_first_stable"] += 1
            elif isinstance(where, tuple):
                out["in_recursion"] += 1
                out.setdefault("rec_before_f", 0); out["rec_before_f"] += (f is None or where[1] < f)
            else:
                out["deeper_depth0"] += 1
                if len(out["ex"]) < 6: out["ex"].append((name, sa, i, f, where, len(pa), t, sorted(v for v, _ in d.tv[t]), [pp[1] for pp in pa], [pp[1] for pp in pb]))
        if not drivers: out["no_driver_found"] += 1
for base, nm in ((D.DTL, "DTL"),):
    out = {"drivers": 0, "at_first_stable": 0, "deeper_depth0": 0, "in_recursion": 0, "no_driver_found": 0, "ex": []}
    rnd = gen.Rng("frontier"); games = [(f.split('/')[-1], pg.read(f)) for f in sys.argv[1:]]
    for i in range(500):
        n = rnd.randint(8, 24); games.append((f'r{i}', gen.random_game(n, rnd.randint(2, n+1), 1, rnd.randint(1, 3), rnd.next64())))
    sys.setrecursionlimit(100000)
    for name, g in games:
        idx = sorted(range(g.n), key=lambda v: (g.prio[v], v)); new = {v: i for i, v in enumerate(idx)}
        d = mk(base)([g.prio[v] for v in idx], [g.owner[v] for v in idx], [[new[w] for w in g.succ[v]] for v in idx]); d.run()
        analyse(d, out, name)
    print(nm, out)
