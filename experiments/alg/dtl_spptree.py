"""L-ALG succ. 5 (produced on Opus 5.5, 2026-10-17 box 5), queue item (2): the full piece tree of every search.
Records each best_vertices call in call order as (depth, R, result, V) and each new tangle as (depth, top, vertex set), all in
ORIGINAL vertex ids. Prints, per phase of player SPPT_P (default: the longest phase), each search's call list compactly and
the first call where consecutive searches differ. DTL_ORDER=oink | stable. Usage: dtl_spptree.py G.pg"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_spp as P
D = P.X.D

class TR(P.PS):
    def search(s, p):
        s.calls = []; r = P.PS.search(s, p); s.trace[-1]["calls"] = s.calls; return r
    def search_rec(s, R, p, depth):
        s.depth = depth; s.calls.append(("enter", depth, frozenset(R)))
        r = D.DTL.search_rec(s, R, p, depth); s.depth = depth - 1; return r
    def best_vertices(s, V, R, p):
        Rin = frozenset(R); res = D.DTL.best_vertices(s, V, R, p)
        s.calls.append(("bv", s.depth, Rin, res, frozenset(V))); return res
    def extractTangles(s, top, R):
        k = len(s.tv); r = D.DTL.extractTangles(s, top, R)
        for t in range(k, len(s.tv)): s.calls.append(("tangle", s.depth, top, frozenset(v for v, _ in s.tv[t])))
        if s.dominions and not s.calls or True: pass
        return r

def run(f):
    g = pg.read(f); d0 = P.X.build(g)
    d = TR(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx
    sys.setrecursionlimit(100000); d.run(); return g, d

def phase_list(d):
    rows, cur = [], []
    for t in d.trace:
        if cur and (t["p"] != cur[-1]["p"] or t["dom"] != cur[-1]["dom"]): rows.append(cur); cur = []
        cur.append(t)
    if cur: rows.append(cur)
    return rows

if __name__ == "__main__":
    g, d = run(sys.argv[1]); idx = d.idx; o = lambda S: sorted(idx[v] for v in S)
    ph = max(phase_list(d), key=len)
    for si, tr in enumerate(ph):
        out = []
        for c in tr["calls"]:
            if c[0] == "bv": out.append(f"{'.' * c[1]}bv|R|{len(c[2])}:{c[3]}:{o(c[4])}")
            elif c[0] == "tangle": out.append(f"{'.' * c[1]}T@{idx[c[2]]}{o(c[3])}")
        print(si, "  ".join(out))
