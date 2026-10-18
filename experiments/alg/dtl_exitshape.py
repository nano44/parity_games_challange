"""L-ALG succ. 8 (produced on Opus 5.5, 2026-10-18 box 10), GAP-A-M §23r gap G23r, toward (EXIT_c): the shape of exits on the
fixed §23t grid. Model and grid as dtl_drthr.py (rec["rtop"] with the §23t round convention). For each consecutive visit pair
x → y of a context R and each grid round r:
  FALLS: per (r, w), the number of pairs at which top_r(w) falls (any level; ⊥ = -1). (DOWN_c) "top_r(w) falls at most c
         times per phase" implies (EXIT_c) with the same c.
  exit causes, per exit pair (x, y, r): 'Vloss' if V_r(y) misses a top of V_r(x) that is processed in x above the exit level
         (only possible when an earlier round differs), else 'steal' (by local PREFIX-MONO-X* a relevant steal at a higher
         step of round r is then needed; the tool records only the label).
  per round index: exits in round 1 vs later rounds.
Printed: histogram of falls per (r, w); exits by round class and cause; examples of (r, w) with ≥ 2 falls (top sequences).
Usage: RM_LIGHT=1 RM_DV=0 DTL_ORDER=oink|stable [UNIONS=.. SEED=.. UM_CROSS=.. NMAX=..] dtl_exitshape.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import dtl_drthr as DT, dtl_step5stats as ST
FD = DT.FD

if __name__ == "__main__":
    sys.setrecursionlimit(100000); tot = {}; shown = 0; nshow = int(os.environ.get("EX_SHOW", "6")); hist = {}
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
                falls = {}; seqs = {}
                for i in range(len(gs) - 1):
                    gx, gy = gs[i], gs[i + 1]
                    for r in range(nr):
                        Vx = set(gx[r].values()); Vy = set(gy[r].values())
                        for w in set(gx[r]) | set(gy[r]):
                            tx, ty = gx[r].get(w, -1), gy[r].get(w, -1)
                            if tx > ty:
                                falls[(r, w)] = falls.get((r, w), 0) + 1
                                if any(ty <= t < tx for t in grid):            # an exit at some grid level
                                    cause = "Vloss" if any(u not in Vy and u > ty for u in Vx) else "steal"
                                    k = f"exits: round {'1 ' if r == 0 else '2+'} cause {cause}"; tot[k] = tot.get(k, 0) + 1
                for (r, w), c in falls.items():
                    hist[c] = hist.get(c, 0) + 1
                    if c >= 2 and shown < nshow:
                        shown += 1
                        print("FALLS", c, nm, "depth", key_[0], "|R|", len(R), "round", r + 1, "w", w, "top sequence", [gg[r].get(w, -1) for gg in gs], flush=True)
    print("falls per (round, vertex) with ≥ 1 fall: histogram", dict(sorted(hist.items())))
    for k in sorted(tot): print(f"{tot[k]:7d}  {k}")
