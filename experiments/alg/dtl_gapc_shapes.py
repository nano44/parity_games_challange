"""L-ALG succ. 5 (produced on Opus 5.5, 2026-10-17 box 5), GAP-C: near misses and failing-shape frequencies on A_DTL runs.
For every search s of a run (order datum DTL_ORDER):
  Wp      = |W_p(G')| by Zielonka on the current subgame G' (p = the searched player);
  prod    = new tangles + dominions found by s;
  per extractTangles call (closed sptl region at top tau, piece context R): every nontrivial SCC reachable from tau is
    NEW / DOM / DUP-X (a stored tangle all of whose escapes lie outside R: shape (beta') of DTL-proof.md §2.3 K6) /
    DUP-IN (a stored tangle with an escape inside R).
Reports: searches with Wp > 0, no dominion and exactly one new tangle (NEAR MISS: one extraction stands between the run and
incompleteness), and totals of DUP-X / DUP-IN outcomes in searches with Wp > 0.
Usage: dtl_gapc_shapes.py G.pg ...   (GS_V=1 prints every near miss)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, zielonka, dtl_spp as P
D = P.X.D

class GS(P.PS):
    def search(s, p):
        s.ev = []; r = P.PS.search(s, p); s.trace[-1]["ev"] = s.ev; return r
    def sptl(s, V, R, p):
        s.ctx = frozenset(R); return D.DTL.sptl(s, V, R, p)
    def extractTangles(s, top, R):
        k, dm = len(s.tv), s.dominions
        keys_before = {tuple(kk): i for i, kk in enumerate(s.tkeys)}
        r = D.DTL.extractTangles(s, top, R)
        # classify every nontrivial SCC reachable from top again (same restricted graph) to find duplicates
        p = s.pr[top] % 2; st = s.str
        def succ(v):
            if s.ow[v] == p:
                x = st[v]; return [x] if x != -1 and x in R else []
            return [w for w in s.outs[v] if w in R]
        for C in s.pearce(top, succ):
            if len(C) == 1 and not (st[C[0]] == C[0] or (st[C[0]] == -1 and C[0] in s.outs[C[0]])): continue
            key = tuple(sorted(C))
            if key in keys_before:
                t = keys_before[key]; esc = s.tout[t]
                s.ev.append("DUP-X" if all(e not in s.ctx for e in esc) else "DUP-IN")
        s.ev += ["NEW"] * (len(s.tv) - k) + ["DOM"] * (s.dominions - dm)
        return r

def subgame_win(g, d, G, p):
    idx = sorted(G); new = {v: i for i, v in enumerate(idx)}
    sub = pg.Game([d.pr[v] for v in idx], [d.ow[v] for v in idx], [[new[w] for w in d.outs[v] if w in G] for v in idx])
    w = zielonka.solve(sub); return sum(1 for x in w if x == p)

if __name__ == "__main__":
    sys.setrecursionlimit(100000); tot = {"searches": 0, "Wp>0": 0, "near": 0, "DUP-X": 0, "DUP-IN": 0, "lastWp>0": 0}; kinds = {}
    for f in sys.argv[1:]:
        g = pg.read(f); d = P.build(g); d = GS(d.pr, d.ow, d.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.run()
        for tr in d.trace:
            G = set(tr["G"])
            if not G: continue
            tot["searches"] += 1; wp = subgame_win(g, d, G, tr["p"]); prod = (tr["t1"] - tr["t0"]) + (tr["d1"] - tr["dom"])
            if wp == 0: continue
            tot["Wp>0"] += 1; tot["DUP-X"] += tr["ev"].count("DUP-X"); tot["DUP-IN"] += tr["ev"].count("DUP-IN")
            if prod == 0: tot["lastWp>0"] += 1; print("INCOMPLETE SEARCH (Wp > 0, nothing learned):", os.path.relpath(f), flush=True)
            dom = tr["d1"] - tr["dom"]; tot["dom"] = tot.get("dom", 0) + (dom > 0)
            if dom == 0 and prod == 1:
                tot["near"] += 1; kd = "NEW"; kinds[kd] = kinds.get(kd, 0) + 1
                if os.environ.get("GS_V"): print("NEAR MISS", os.path.relpath(f), f"p={tr['p']} |G'|={len(G)} |Wp|={wp} only {kd}; other outcomes {[e for e in tr['ev'] if e not in ('NEW', 'DOM')]}")
    print(tot, "near-miss kinds", kinds)
