"""L-ALG succ. 5 (produced on Opus 5.5, 2026-10-17 box 5), GAP-C (K-first) case split: in a search of p with W_p(G') != {}
and no dominion, is the first stable piece the ROOT call (depth 0, first best_vertices call, X = {}: Case A, where only (alpha)
is open) or a later piece (Case B: after -1 pieces at depth 0, or inside a recursion)? Counts mixed searches separately.
DTL_ORDER = oink | stable. Usage: dtl_kfirst_case.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_kin as K
D = K.D

class KC(K.KI):
    def search(s, p):
        s.bvn = 0; s.first_stable = None; s.dep = 0; return K.KI.search(s, p)
    def search_rec(s, R, p, depth):
        old = s.dep; s.dep = depth; r = D.DTL.search_rec(s, R, p, depth); s.dep = old; return r
    def best_vertices(s, V, R, p):
        res = D.DTL.best_vertices(s, V, R, p); s.bvn += 1
        if res == 1 and s.first_stable is None: s.first_stable = (s.bvn, s.dep)
        s.trace[-1]["first_stable"] = s.first_stable; return res

if __name__ == "__main__":
    sys.setrecursionlimit(100000); tab = {}
    for f in sys.argv[1:]:
        g = pg.read(f); d0 = K.P.build(g); d = KC(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.run()
        for tr in d.trace:
            W = tr["Wp"]
            if not W or tr["d1"] > tr["dom"]: continue
            fs = tr.get("first_stable"); mixed = W != set(tr["G"])
            case = "none" if fs is None else ("A (root call stable)" if fs == (1, 0) else f"B (first stable = call {min(fs[0], 9)}{'+' if fs[0] >= 9 else ''} at depth {fs[1]})")
            key = (case, "mixed" if mixed else "W_p = G'"); tab[key] = tab.get(key, 0) + 1
    for k, v in sorted(tab.items(), key=lambda kv: -kv[1]): print(v, k)
