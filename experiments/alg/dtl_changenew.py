"""L-ALG succ. 7 (produced on Opus 5.5, 2026-10-18 box 9), GAP-A-M §23s: (CHANGE-NEW) "at every consecutive visit pair of a
context whose best_vertices computations differ, some tangle born between the two visits fires at the context in the later
visit (region step or threshold loop)", and D_R ≤ #fired⁺(R). Same model as dtl_rootmono.RM (RM_EXCL=1). Per call, the set-level
signature is the sequence of its tattr log entries (caller, depth, Z in, Z out, threshold), from dtl_fdlcheck.CK. used⁺ =
the tangles used in those entries. A tangle is NEW at visit y if its index is ≥ ntv of the previous visit x (tangles are
only appended).
Printed: CHANGE-NEW holds/FAILS per differing pair; max D_R, max #fired⁺(R); max D_R/#fired⁺; and whether N*_R ≤ D_R.
Usage: RM_EXCL=1 RM_LIGHT=1 RM_DV=0 DTL_ORDER=oink|stable dtl_changenew.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import dtl_rootmono as RMM, dtl_step5stats as ST
FD = RMM.FD


def sig_used(r, rc):
    es = [e for e in r["log"][rc["start"]:rc["end"]] if e[0] in ("bv-reg", "bv-thr")]
    return tuple((e[0], e[1], e[2], e[3], e[4]) for e in es), frozenset().union(*[e[5] for e in es]) if es else frozenset()


if __name__ == "__main__":
    sys.setrecursionlimit(100000); tot = {}; shown = 0; mx = (0, 0, ""); worst_ratio = 0.0
    for f, g in ST.games(sys.argv[1:]):
        d0 = FD.P.X.build(g); d = RMM.RM(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx; d.run()
        nm = f if f.startswith(("union", "random")) else os.path.relpath(f)
        if not all(w is not None for w in d.win): print("INCOMPLETE", nm, flush=True)
        for ph in FD.phase_rows(d):
            visits = {}
            for r_ in ph:
                for rc in r_["recs"]: visits.setdefault(rc["key"], []).append((r_, rc))
            for key_, vl in visits.items():
                if len(vl) < 2: continue
                DR = 0; firedp = set(); nstar = 0
                for r_, rc in vl: firedp |= sig_used(r_, rc)[1]
                for (ra, x), (rb, y) in zip(vl, vl[1:]):
                    sa, _ = sig_used(ra, x); sb, ub = sig_used(rb, y)
                    if sa == sb: continue
                    DR += 1
                    new = {t for t in ub if t >= x["ntv"]}
                    kc = "CHANGE-NEW (a differing pair has a new tangle firing at R in the later visit): " + ("holds" if new else "FAILS"); tot[kc] = tot.get(kc, 0) + 1
                    if not new and shown < 20:
                        shown += 1; print("CHANGE-NEW FAILS", nm, "depth", key_[0], "|R|", len(key_[1]), "ntv", x["ntv"], y["ntv"], flush=True)
                    ex_, ey_, fx_ = x.get("excl", {}), y.get("excl", {}), x.get("fired", {})
                    if any(t < x["ntv"] and t not in ex_.get(k_, frozenset()) and t in fx_.get(k_, frozenset()) for k_ in ey_ if k_ in ex_ for t in ey_[k_]): nstar += 1
                kd = "D_R ≤ #fired⁺(R): " + ("holds" if DR <= len(firedp) else "FAILS"); tot[kd] = tot.get(kd, 0) + 1
                kn = "N*_R ≤ D_R: " + ("holds" if nstar <= DR else "FAILS"); tot[kn] = tot.get(kn, 0) + 1
                if DR > mx[0]: mx = (DR, len(firedp), f"{nm} depth {key_[0]} |R| {len(key_[1])} visits {len(vl)}")
                if firedp: worst_ratio = max(worst_ratio, DR / len(firedp))
    print("max D_R (with its #fired⁺, context):", mx, "; max D_R/#fired⁺:", round(worst_ratio, 3))
    for k in sorted(tot): print(f"{tot[k]:7d}  {k}")
