"""L-ALG succ. 8 (produced on Opus 5.5, 2026-10-18 box 10), toward (EXIT_c) / (D-POLY): (NET-GROWTH) "at every non-quiet consecutive
visit pair of a context, the grid entries outnumber the grid exits", i.e. Φ_grid = Σ_{r,τ} |P_r(τ⁺)| (§23t grid, dtl_drthr
conventions) rises strictly at every non-quiet pair. Φ_grid ≤ (|R|+1)|R|², so NET-GROWTH would give M_R ≤ (|R|+1)|R|².
Printed: counts of non-quiet pairs with ΔΦ_grid > 0 / = 0 / < 0; worst ΔΦ_grid; examples (NG_SHOW, default 3).
Usage: RM_LIGHT=1 RM_DV=0 DTL_ORDER=oink|stable [UNIONS=..] dtl_netgrowth.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import dtl_drthr as DT, dtl_step5stats as ST
FD = DT.FD

if __name__ == "__main__":
    sys.setrecursionlimit(100000); tot = {}; worst = (0, ""); shown = 0; nshow = int(os.environ.get("NG_SHOW", "3"))
    for f, g in ST.games(sys.argv[1:]):
        d0 = FD.P.X.build(g); d = DT.DR(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx; d.run()
        nm = f if f.startswith(("union", "random")) else os.path.relpath(f)
        if not all(w is not None for w in d.win): print("INCOMPLETE", nm, flush=True)
        for ph in FD.phase_rows(d):
            visits = {}
            for r_ in ph:
                for rc in r_["recs"]: visits.setdefault(rc["key"], []).append((r_, rc))
            for key_, vl in visits.items():
                if len(vl) < 2: continue
                R = key_[1]; p = vl[0][1]["p"]; grid = sorted(v for v in R if d.pr[v] % 2 == p)
                if not grid: continue
                nr = len(R) + 1; gs = [DT.grid_tops(rc, nr) for _, rc in vl]
                for i in range(len(gs) - 1):
                    ent = ex = 0
                    for r in range(nr):
                        for w in set(gs[i][r]) | set(gs[i + 1][r]):
                            tx, ty = gs[i][r].get(w, -1), gs[i + 1][r].get(w, -1)
                            if ty > tx: ent += sum(1 for t in grid if tx <= t < ty)
                            elif tx > ty: ex += sum(1 for t in grid if ty <= t < tx)
                    if ent == 0 and ex == 0: continue
                    dl = ent - ex; k = "non-quiet pairs: dPhi_grid " + (">0" if dl > 0 else ("=0" if dl == 0 else "<0 (NET-GROWTH FAILS)")); tot[k] = tot.get(k, 0) + 1
                    if dl < worst[0]: worst = (dl, f"{nm} depth {key_[0]} |R| {len(R)} pair {i} entries {ent} exits {ex}")
                    if dl <= 0 and shown < nshow: shown += 1; print("NET-GROWTH", "FAILS" if dl < 0 else "TIES", nm, "depth", key_[0], "|R|", len(R), "pair", i, "entries", ent, "exits", ex, flush=True)
    print("worst dPhi_grid:", worst)
    for k in sorted(tot): print(f"{tot[k]:7d}  {k}")
