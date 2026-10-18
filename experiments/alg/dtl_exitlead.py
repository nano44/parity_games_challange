"""L-ALG succ. 8 (produced on Opus 5.5, 2026-10-18 box 10), toward (EXIT_c), GAP-A-M §24e: (EXIT-LEAD-DISTINCT) "the exits of one
(step, vertex) on the §23t grid never share the LEADING key of their pairs", where the leading key of a pair x → y is (r0, τ0):
r0 = the first grid round whose top map differs, τ0 = the highest top whose round-r0 region differs (as a set; a new top
counts). It would give exits(σ, w) ≤ (|R| + 1)|R|, hence X_R polynomial. Printed: (σ, w) with ≥ 2 exits: keys distinct /
repeated; examples (EL_SHOW, default 4). Usage: RM_LIGHT=1 RM_DV=0 DTL_ORDER=oink|stable [UNIONS=..] dtl_exitlead.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import dtl_drthr as DT, dtl_step5stats as ST
FD = DT.FD


def lead(gx, gy, nr):
    for r in range(nr):
        if gx[r] != gy[r]:
            rx, ry = {}, {}
            for w, t in gx[r].items(): rx.setdefault(t, set()).add(w)
            for w, t in gy[r].items(): ry.setdefault(t, set()).add(w)
            for t in sorted(set(rx) | set(ry), reverse=True):
                if rx.get(t) != ry.get(t): return (r, t)
    return None


if __name__ == "__main__":
    sys.setrecursionlimit(100000); tot = {}; shown = 0; nshow = int(os.environ.get("EL_SHOW", "4"))
    for f, g in ST.games(sys.argv[1:]):
        d0 = FD.P.X.build(g); d = DT.DR(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx; d.run()
        nm = f if f.startswith(("union", "random")) else os.path.relpath(f)
        if not all(w is not None for w in d.win): print("INCOMPLETE", nm, flush=True)
        for ph in FD.phase_rows(d):
            visits = {}
            for r_ in ph:
                for rc in r_["recs"]: visits.setdefault(rc["key"], []).append(rc)
            for key_, vl in visits.items():
                if len(vl) < 2: continue
                R = key_[1]; p = vl[0]["p"]; grid = sorted(v for v in R if d.pr[v] % 2 == p)
                if not grid: continue
                nr = len(R) + 1; gs = [DT.grid_tops(rc, nr) for rc in vl]; keys = {}
                for i in range(len(gs) - 1):
                    gx, gy = gs[i], gs[i + 1]; L = None
                    for r in range(nr):
                        for w in gx[r]:
                            tx, ty = gx[r][w], gy[r].get(w, -1)
                            if tx > ty:
                                if L is None: L = lead(gx, gy, nr)
                                for t in grid:
                                    if ty <= t < tx: keys.setdefault((r, t, w), []).append((i, L))
                for k, lst in keys.items():
                    if len(lst) < 2: continue
                    ls = [l for _, l in lst]; dist = len(set(ls)) == len(ls)
                    kk = "(step, vertex) with ≥ 2 exits: leading keys " + ("distinct" if dist else "REPEATED (EXIT-LEAD-DISTINCT FAILS)"); tot[kk] = tot.get(kk, 0) + 1
                    if shown < nshow and (not dist or shown < 2):
                        shown += 1; print("EXIT-LEAD", "distinct" if dist else "REPEATED", nm, "depth", key_[0], "|R|", len(R), "step", (k[0] + 1, k[1]), "w", k[2], "exits at pairs/keys", [(i, (l[0] + 1, l[1]) if l else None) for i, l in lst], flush=True)
    for k in sorted(tot): print(f"{tot[k]:7d}  {k}")
