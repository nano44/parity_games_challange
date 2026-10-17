"""L-ALG succ. 5 (produced on Opus 5.5, 2026-10-17 box 5), GAP-C candidate (LOW-W): every search of p with W_p(G') != {}
that finds no dominion has a stable piece (best_vertices result 1, any depth) whose LOWEST top with a region (the last top that gets a
region in an sptl pass) learns a tangle inside W_p(G'). Also counts, among tangles learned inside W_p, how many came from the
lowest top of their pass. DTL_ORDER = oink | stable. Usage: dtl_loww.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_kin as K
D = K.D

class LW(K.KI):
    def sptl(s, V, R, p):
        """dtl_pyref.sptl verbatim, recording the tops that get a region (top still in R at its turn)."""
        s.pass_tops = []; s.pass_ev = []; changes = False
        for top in range(s.n - 1, -1, -1):
            if top not in V or top not in R: continue
            s.pass_tops.append(top)
            Z = {top}; s.str[top] = -1; s.Q = [top]
            s.tattr(p, Z, R, R, s.pr[top], R)
            closed = (s.str[top] != -1) if s.ow[top] == p else not any(w in R for w in s.outs[top])
            if closed and top not in s.W:
                s.W.add(top)
                if s.extractTangles(top, Z): changes = True
        s.passes.append((list(s.pass_tops), list(s.pass_ev))); return changes
    def extractTangles(s, top, R):
        k = len(s.tv); r = D.DTL.extractTangles(s, top, R)
        for t in range(k, len(s.tv)): s.newt.append(frozenset(v for v, _ in s.tv[t])); s.pass_ev.append((top, frozenset(v for v, _ in s.tv[t])))
        return r
    def search(s, p):
        s.passes = []; r = K.KI.search(s, p); s.trace[-1]["passes"] = s.passes; return r

if __name__ == "__main__":
    sys.setrecursionlimit(100000); tab = {"searches W_p != {}, no dominion": 0, "LOW-W holds": 0, "LOW-W VIOLATION": 0}; tl = {"from lowest top": 0, "from a higher top": 0, "lowest-top tangle OUTSIDE W_p": 0}; shown = 0
    for f in sys.argv[1:]:
        g = pg.read(f); d0 = K.P.build(g); d = LW(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.run()
        for tr in d.trace:
            W = tr["Wp"]
            if not W: continue
            ok = False
            for tops, ev in tr["passes"]:
                low = tops[-1] if tops else None
                for top, C in ev:
                    if top == low and not C <= W: tl["lowest-top tangle OUTSIDE W_p"] += 1
                    if C <= W:
                        tl["from lowest top" if top == low else "from a higher top"] += 1
                        if top == low: ok = True
            if tr["d1"] > tr["dom"]: continue
            tab["searches W_p != {}, no dominion"] += 1
            if ok: tab["LOW-W holds"] += 1
            else:
                tab["LOW-W VIOLATION"] += 1
                if shown < 3: shown += 1; print("LOW-W VIOLATION", os.path.relpath(f), "p", tr["p"])
    print(tab, tl)
