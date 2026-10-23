"""L-RED box 21 (produced on Opus 5.5): greedy shrink of an N8a counter gadget with kl.py UNMODIFIED (KL_DIR). Repeatedly tries to delete a
vertex (edges into it removed; rejected if some vertex loses all successors) or an edge, keeping CRIT: dual pivots under RULE >= A*n^B
(n = current size). Writes OUT.pg after every accepted deletion. Usage: KL_DIR=.. kshrink.py G.pg RULE A B OUT.pg"""
import sys, os, importlib.util
KL = os.environ["KL_DIR"]; sys.path.insert(0, os.path.join(KL, "..", "..", "harness")); sys.setrecursionlimit(100000)
spec = importlib.util.spec_from_file_location("kl", os.path.join(KL, "kl.py")); kl = importlib.util.module_from_spec(spec); spec.loader.exec_module(kl)
import pg
g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%"))); rule, A, B, out = sys.argv[2], float(sys.argv[3]), float(sys.argv[4]), sys.argv[5]


def score(h):
    try: return kl.solve(h, rule)["it_dual"]
    except Exception: return -1


def ok(h): return score(h) >= A * h.n ** B


def delv(h, v):
    keep = [u for u in range(h.n) if u != v]; m = {u: i for i, u in enumerate(keep)}
    su = [[m[w] for w in h.succ[u] if w != v] for u in keep]
    if any(not s for s in su): return None
    return pg.Game([h.prio[u] for u in keep], [h.owner[u] for u in keep], su)


assert ok(g), ("start fails", score(g)); print("start n", g.n, "pivots", score(g), flush=True)
changed = True
while changed:
    changed = False
    for v in range(g.n - 1, -1, -1):
        h = delv(g, v)
        if h is not None and ok(h): g = h; changed = True; pg.write(g, out); print("del vertex", v, "-> n", g.n, "pivots", score(g), flush=True)
    for v in range(g.n):
        for w in list(g.succ[v]):
            if len(g.succ[v]) < 2: break
            su = [list(s) for s in g.succ]; su[v].remove(w); h = pg.Game(list(g.prio), list(g.owner), su)
            if ok(h): g = h; changed = True; pg.write(g, out); print("del edge", v, w, "pivots", score(g), flush=True)
print("final n", g.n, "edges", sum(len(s) for s in g.succ), "pivots", score(g)); pg.write(g, out)
