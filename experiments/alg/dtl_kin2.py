"""L-ALG succ. 5 (produced on Opus 5.5, 2026-10-17 box 5), GAP-C structure behind (K-in): for every tangle learned inside
W_p(G') in a search with W_p(G') != {}, where was it learned: depth of the piece, and the piece's context R relative to
W_p (R inside W_p / R meets both). For the FIRST such tangle of each search as well. DTL_ORDER = oink | stable.
Usage: dtl_kin2.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_kin as K
D = K.D

class KI2(K.KI):
    def search_rec(s, R, p, depth):
        old = getattr(s, "dep", -1); s.dep = depth; r = D.DTL.search_rec(s, R, p, depth); s.dep = old; return r
    def sptl(s, V, R, p):
        s.ctx = frozenset(R); return D.DTL.sptl(s, V, R, p)
    def extractTangles(s, top, R):
        k = len(s.tv); r = D.DTL.extractTangles(s, top, R)
        for t in range(k, len(s.tv)): s.newt.append((frozenset(v for v, _ in s.tv[t]), s.dep, s.ctx))
        return r

if __name__ == "__main__":
    sys.setrecursionlimit(100000); allt = {}; first = {}
    for f in sys.argv[1:]:
        g = pg.read(f); d0 = K.P.build(g); d = KI2(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.run()
        for tr in d.trace:
            W = tr["Wp"]
            if not W: continue
            fst = True
            for C, dep, ctx in tr["newt"]:
                if not C <= W: continue
                key = (f"depth {min(dep, 3)}{'+' if dep >= 3 else ''}", "context inside W_p" if ctx <= W else "context meets both")
                allt[key] = allt.get(key, 0) + 1
                if fst: first[key] = first.get(key, 0) + 1; fst = False
    print("all tangles learned inside W_p:"); [print(" ", v, k) for k, v in sorted(allt.items(), key=lambda kv: -kv[1])]
    print("first such tangle per search:"); [print(" ", v, k) for k, v in sorted(first.items(), key=lambda kv: -kv[1])]
