#!/usr/bin/env python3
"""L-RED (box 6, produced on Opus 5.5): graded (K4-B) fitness, GAP-C.md §13. At the FIRST stable piece of a search of p
with W_p(G') != {} and no dominion (L-ALG's unmodified dtl_k4b.K4B, imported read-only from LALG5_DIR >= 31fdd98), let
R be the piece's context and X = G' \\ R (removed before it; at depth 1 this includes the parent's X). Edges from an
opponent vertex of a region into X are IGNORED by the region attractor (attracts/attractVertices judge escapes in CurR).
  viol = |regions ∩ W_{1-p}| + |V* ∩ W_{1-p}|            ((K4-B) violated iff > 0)
  esc1 = opponent region vertices with an edge into X ∩ W_{1-p}   (each such vertex is in W_{1-p}: a violation)
  esc  = opponent region vertices with an edge into X
  xw1  = |X ∩ W_{1-p}| in mixed searches
Also (K-in) violations and run completeness from the same run. Order from DTL_ORDER. Usage: k4bp.py G.pg ..."""
import sys, os
ld = os.path.join(os.environ["LALG5_DIR"], "experiments", "alg")
sys.path.insert(0, ld); sys.path.insert(0, os.path.join(ld, "..", "harness"))
import pg, dtl_k4b as KB

def measure_game(g, order=None):
    order = order or os.environ.get("DTL_ORDER", "stable")
    d0 = KB.K.P.build(g); d = KB.K4B(d0.pr, d0.ow, d0.outs, ins_desc=(order == "oink")); d.run()
    m = dict(incomplete=len(d.G), kin=0, viol=0, esc1=0, esc=0, xw1=0, mixed=0, checked=0)
    for tr in d.trace:
        W = tr["Wp"]
        if not W or tr["d1"] > tr["dom"]: continue
        m["checked"] += 1
        if not any(C <= W for C in tr["newt"]): m["kin"] += 1
        if "first" not in tr: continue
        G = set(tr["G"]); mixed = W != G; m["mixed"] += mixed
        V, Z, R = tr["first"]; X = G - set(R); W1 = G - W; p = tr["p"]
        m["viol"] += len(Z & W1) + len(V & W1)
        if not mixed: continue
        m["xw1"] = max(m["xw1"], len(X & W1))
        for v in Z:
            if d.ow[v] == p: continue
            outs = set(d.outs[v])
            if outs & X: m["esc"] += 1
            if outs & X & W1: m["esc1"] += 1
    return m

def measure(path): return measure_game(pg.read(path))

def score(path):
    m = measure(path)
    return (10 ** 12 * (m["incomplete"]) + 10 ** 11 * m["kin"] + 10 ** 10 * min(m["viol"], 9) + 10 ** 8 * min(m["esc1"], 9)
            + 10 ** 6 * min(m["esc"], 9) * (m["xw1"] > 0) + 10 ** 4 * min(m["esc"], 9) + 10 ** 2 * min(m["xw1"], 20) + min(m["mixed"], 20))

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    for f in sys.argv[1:]:
        print(os.path.basename(f), os.environ.get("DTL_ORDER", "stable"), measure(f))
