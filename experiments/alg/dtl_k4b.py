"""L-ALG succ. 5 (produced on Opus 5.5, 2026-10-17 box 5), GAP-K' (Case B): at the FIRST stable piece of a search of p with
W_p(G') != {} (no dominion), is the union of its final-round regions inside W_p(G')? (K4 says yes at X = {}.) Also V* itself.
Regions are recomputed from the returned V* exactly as best_vertices' last round does (dtl_pyref primitives, consuming CurR).
DTL_ORDER = oink | stable. Usage: dtl_k4b.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_kin as K
D = K.D

class K4B(K.KI):
    def search(s, p):
        s.first = None; return K.KI.search(s, p)
    def best_vertices(s, V, R, p):
        res = D.DTL.best_vertices(s, V, R, p)
        if res == 1 and s.first is None:
            Z = set(); CurR = set(R)
            for top in range(s.n - 1, -1, -1):
                if top not in V or top in Z: continue
                CurZ = {top}; s.Q = [top]; s.tattr(p, CurZ, CurR, CurR, s.pr[top], CurR); Z |= CurZ
            s.first = (frozenset(V), frozenset(Z), frozenset(R))
            s.trace[-1]["first"] = s.first
        return res

if __name__ == "__main__":
    sys.setrecursionlimit(100000); tab = {}; shown = 0
    for f in sys.argv[1:]:
        g = pg.read(f); d0 = K.P.build(g); d = K4B(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.run()
        for tr in d.trace:
            W = tr["Wp"]
            if not W or tr["d1"] > tr["dom"] or "first" not in tr: continue
            V, Z, R = tr["first"]; mixed = W != set(tr["G"])
            key = ("mixed" if mixed else "W_p = G'", "V* inside W_p" if V <= W else "V* meets W_{1-p}", "regions inside W_p" if Z <= W else "regions meet W_{1-p}")
            tab[key] = tab.get(key, 0) + 1
            if mixed and not Z <= W and shown < 3: shown += 1; print("REGIONS OUTSIDE", os.path.relpath(f), "|V*|", len(V), "outside", len(Z - W))
    for k, v in sorted(tab.items(), key=lambda kv: -kv[1]): print(v, k)
