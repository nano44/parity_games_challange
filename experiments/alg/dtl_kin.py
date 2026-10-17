"""L-ALG succ. 5 (produced on Opus 5.5, 2026-10-17 box 5), GAP-C candidate (K-in): a search of p with W_p(G') != {} either
finds a dominion or learns at least one new tangle INSIDE W_p(G') (W_p by Zielonka on G'). Also counts how many of the new
tangles of such a search lie inside / meet / avoid W_p. DTL_ORDER = oink | stable. Usage: dtl_kin.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_orphan as O, dtl_spp as P
D = P.X.D

class KI(P.PS):
    def search(s, p):
        s.Wp = O.winning(s, set(s.G), p) if s.G else set(); s.newt = []
        r = P.PS.search(s, p); s.trace[-1]["Wp"] = s.Wp; s.trace[-1]["newt"] = s.newt; return r
    def extractTangles(s, top, R):
        k = len(s.tv); r = D.DTL.extractTangles(s, top, R)
        for t in range(k, len(s.tv)): s.newt.append(frozenset(v for v, _ in s.tv[t]))
        return r

if __name__ == "__main__":
    sys.setrecursionlimit(100000); tab = {"searches with W_p != {}": 0, "found a dominion": 0, "learned inside W_p (no dominion)": 0, "K-in VIOLATION": 0}
    loc = {"inside": 0, "meets": 0, "avoids": 0}; shown = 0
    for f in sys.argv[1:]:
        g = pg.read(f); d0 = P.build(g); d = KI(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.run()
        for tr in d.trace:
            W = tr["Wp"]
            if not W: continue
            tab["searches with W_p != {}"] += 1
            for C in tr["newt"]: loc["inside" if C <= W else "meets" if C & W else "avoids"] += 1
            if tr["d1"] > tr["dom"]: tab["found a dominion"] += 1; continue
            if any(C <= W for C in tr["newt"]): tab["learned inside W_p (no dominion)"] += 1
            else:
                tab["K-in VIOLATION"] += 1
                if shown < 3: shown += 1; print("K-in VIOLATION", os.path.relpath(f), "p", tr["p"], "|G'|", len(tr["G"]), "|W_p|", len(W), "new tangles", [sorted(C) for C in tr["newt"]][:3])
    print(tab, "new tangles in such searches:", loc)
