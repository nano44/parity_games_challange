"""L-ALG succ. 5 (produced on Opus 5.5, 2026-10-17 box 5), GAP-C / GAP-K: WHICH stable piece supplies the productive
lowest-region candidate of (K-low)? For every search of p with W_p(G') != {} and no dominion, list its stable pieces (any
depth) in call order; a piece is GOOD if, in some sptl pass, the lowest top with a region lies in W_p and extracts a new
tangle inside W_p. Tests rules: FIRST (the first stable piece is good), FIRST-W (the first stable piece having a top in W_p
is good), LAST (the last stable piece), ANY (some piece; = LOW-W). DTL_ORDER = oink | stable. Usage: dtl_whichpiece.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_loww as L
D = L.D

class WP(L.LW):
    def best_vertices(s, V, R, p):
        res = D.DTL.best_vertices(s, V, R, p)
        if res == 1: s.pieces.append({"V": frozenset(V), "passes_from": len(s.passes)})
        return res
    def search(s, p):
        s.pieces = []; r = L.LW.search(s, p); s.trace[-1]["pieces"] = s.pieces; return r

if __name__ == "__main__":
    sys.setrecursionlimit(100000); tab = {"searches": 0, "mixed (W_p != G')": 0, "FIRST": 0, "FIRST in mixed": 0, "FIRST-W": 0, "LAST": 0, "ANY": 0, "no stable piece": 0}; shown = 0
    for f in sys.argv[1:]:
        g = pg.read(f); d0 = L.K.P.build(g); d = WP(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.run()
        for tr in d.trace:
            W = tr["Wp"]
            if not W or tr["d1"] > tr["dom"]: continue
            pcs = tr["pieces"]; passes = tr["passes"]; tab["searches"] += 1
            good = []
            for i, pc in enumerate(pcs):
                lo, hi = pc["passes_from"], (pcs[i + 1]["passes_from"] if i + 1 < len(pcs) else len(passes))
                ok = False
                for tops, ev in passes[lo:hi]:
                    low = tops[-1] if tops else None
                    if low is not None and low in W and any(top == low and C <= W for top, C in ev): ok = True
                good.append(ok)
            mixed = W != set(tr["G"]); tab["mixed (W_p != G')"] += mixed
            if not good: tab["no stable piece"] += 1; continue
            tab["ANY"] += any(good); tab["FIRST"] += good[0]; tab["LAST"] += good[-1]; tab["FIRST in mixed"] += good[0] and mixed
            if not good[0] and shown < 3: shown += 1; print("FIRST fails", os.path.relpath(f), "pieces", len(pcs), "good", good)
            fw = next((i for i, pc in enumerate(pcs) if pc["V"] & W), None)
            tab["FIRST-W"] += fw is not None and good[fw]
            if fw is not None and not good[fw] and shown < 3: shown += 1; print("FIRST-W fails", os.path.relpath(f), "pieces", len(pcs), "good", good)
    print(tab)
