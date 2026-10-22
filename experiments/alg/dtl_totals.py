"""L-ALG succ. 8 (produced on Opus 5.5, 2026-10-18 box 10): the POLYNOMIAL-TOTAL statements per context and phase, for growth
tables (GAP-A-M §24g): D_R (differing consecutive visit pairs, dtl_changenew.sig_used), Σ_q k_q (relevant-steal events: pair i,
step k present in both visits, t ∈ fired_x[k] ∩ excl_y[k], as in dtl_changenew's N*_R), X_R and N_ent on the §23t grid
(dtl_drthr conventions), max exits per (step, vertex) (grid plus the virtual end-of-round step), #fired⁺(R) (tangles used
in the context's set-level computations over the phase). Printed per file: the ROOT context of the longest phase, and the
max of each quantity over all contexts. Usage: RM_EXCL=1 RM_LIGHT=1 RM_DV=0 DTL_ORDER=oink|stable dtl_totals.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import dtl_drthr as DT, dtl_changenew as CN, dtl_step5stats as ST
FD = DT.FD


def ctx_totals(d, vl):
    R = vl[0][1]["key"][1]; p = vl[0][1]["p"]; grid = sorted(v for v in R if d.pr[v] % 2 == p)
    nr = len(R) + 1; gs = [DT.grid_tops(rc, nr) for _, rc in vl]
    o = dict(R=len(R), visits=len(vl), D=0, K=0, X=0, E=0, mx=0, F=0); ex = {}; fp = set()
    for r_, rc in vl: fp |= CN.sig_used(r_, rc)[1]
    o["F"] = len(fp)
    for i in range(len(vl) - 1):
        (ra, x), (rb, y) = vl[i], vl[i + 1]
        if CN.sig_used(ra, x)[0] != CN.sig_used(rb, y)[0]: o["D"] += 1
        exx, exy, fx = x.get("excl", {}), y.get("excl", {}), x.get("fired", {})
        o["K"] += sum(1 for k in fx if k in exy for t in fx[k] if t in exy[k])
        for r in range(nr):
            for w in set(gs[i][r]) | set(gs[i + 1][r]):
                tx, ty = gs[i][r].get(w, -1), gs[i + 1][r].get(w, -1)
                if tx > ty:
                    for t in grid:
                        if ty <= t < tx: ex[(r, t, w)] = ex.get((r, t, w), 0) + 1; o["X"] += 1
                    if ty == -1: ex[(r, "U", w)] = ex.get((r, "U", w), 0) + 1
                elif ty > tx: o["E"] += sum(1 for t in grid if tx <= t < ty)
    o["mx"] = max(ex.values()) if ex else 0
    return o


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    for f, g in ST.games(sys.argv[1:]):
        d0 = FD.P.X.build(g); d = DT.DR(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx; d.run()
        inc = not all(w is not None for w in d.win); root = None; mx = {}; nph = 0; maxS = 0
        for ph in FD.phase_rows(d):
            nph += 1; visits = {}
            for r_ in ph:
                for rc in r_["recs"]: visits.setdefault(rc["key"], []).append((r_, rc))
            for key_, vl in visits.items():
                if len(vl) < 2 or not key_[1]: continue
                o = ctx_totals(d, vl)
                if key_[0] == 0 and len(ph) > maxS and o["R"] == len(ph[0]["G"]): maxS = len(ph); root = o
                for k_, v in o.items(): mx[k_] = max(mx.get(k_, 0), v)
        print(os.path.basename(f), "n", len(d.pr), "INCOMPLETE" if inc else "complete", "phases", nph, "longest phase S", maxS, "| ROOT", root, "| MAX over contexts", mx, flush=True)
