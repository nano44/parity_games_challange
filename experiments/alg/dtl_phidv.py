"""L-ALG succ. 5 (produced on Opus 5.5, 2026-10-17 box 5), candidate (PHI-DV): the depth-0 removal-index sum PHI0
(dtl_idx0.py) rises only at transitions where the root ideal distance DV* (dtl_dvstar.py, PROVED monotone) moves. If true,
the pair (DV*, -PHI0) rises lexicographically at every transition where either moves, so the transitions where PHI0 or DV*
moves are at most (n(n+1) + 1)(n^2 + 1) per phase. Reports the cross-table (DV* moves?, PHI0 falls/same/rises) and the
first counterexamples. DTL_ORDER=oink | stable. Usage: dtl_phidv.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_settle as SL, dtl_idx0 as I0
from dtl_dvstar import dvstar

if __name__ == "__main__":
    sys.setrecursionlimit(100000); tab = {}; shown = 0
    for f in sys.argv[1:]:
        g = pg.read(f); d0 = SL.P.X.build(g); d = SL.SL(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx
        born = {}; orig = d.extractTangles
        def ext(top, R, d=d, orig=orig, born=born):
            k = len(d.tv); r = orig(top, R)
            for i in range(k, len(d.tv)): born[i] = (frozenset(v for v, _ in d.tv[i]), tuple(d.tout[i]), d.tpr[i] % 2)
            return r
        d.extractTangles = ext; d.run()
        rows, cur = [], []
        for t in d.trace:
            if cur and (t["p"] != cur[-1]["p"] or t["dom"] != cur[-1]["dom"]): rows.append(cur); cur = []
            cur.append(t)
        if cur: rows.append(cur)
        for ph in rows:
            p, G = ph[0]["p"], set(ph[0]["G"])
            dv = [dvstar(d, G, p, [(C, e) for i, (C, e, pa) in born.items() if i < tr["t0"] and pa == p and C <= G]) for tr in ph]
            phi = [sum(I0.idx0(tr["calls"], G).get(v, 0) for v in G) for tr in ph]
            for s in range(len(ph) - 1):
                mv = dv[s] != dv[s + 1]; dp = "falls" if phi[s + 1] < phi[s] else "same" if phi[s + 1] == phi[s] else "RISES"
                tab[(mv, dp)] = tab.get((mv, dp), 0) + 1
                if dp == "RISES" and not mv and shown < 3:
                    shown += 1; print("COUNTER (PHI0 rises, DV* still):", os.path.relpath(f), f"p={p} search {s} -> {s + 1}, PHI0 {phi[s]} -> {phi[s + 1]}")
    for (mv, dp), v in sorted(tab.items(), key=lambda kv: -kv[1]): print(v, "DV* moves" if mv else "DV* still", "PHI0", dp)
