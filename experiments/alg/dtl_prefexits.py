"""L-ALG succ. 7 (produced on Opus 5.5, 2026-10-17 box 8), GAP-A-M §23p: vertex exits from one prefix, toward a direct bound
on Σ_q k_q (§23o idea (c)). Same model and visits as dtl_rootmono.py with RM_EXCL=1 RM_PREF=1. For each context, step
k = (round, top) and vertex v: EXITS = the visit pairs m with v ∈ P_m(k) and v ∉ P_{m+1}(k). Here P is pref[k], the prefix
BEFORE the top (P(τ⁺)). Printed: the max exits per (context, step, vertex), its distribution, and the max total exits per
context relative to |R|.
Usage: RM_EXCL=1 RM_PREF=1 RM_LIGHT=1 RM_DV=0 DTL_ORDER=oink|stable dtl_prefexits.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import dtl_stealdepth as SD, dtl_step5stats as ST
FD = SD.FD

if __name__ == "__main__":
    sys.setrecursionlimit(100000); dist = {}; worst = []; maxtot = (0, 0, "")
    for f, g in ST.games(sys.argv[1:]):
        d = SD.run_game(g, os.environ.get("DTL_ORDER", "stable")); nm = f if f.startswith(("union", "random")) else os.path.relpath(f)
        if not all(w is not None for w in d.win): print("INCOMPLETE", nm, flush=True)
        for ph in FD.phase_rows(d):
            visits = {}
            for r_ in ph:
                for rc in r_["recs"]: visits.setdefault(rc["key"], []).append(rc)
            for key_, rcs in visits.items():
                ex = {}
                for m in range(len(rcs) - 1):
                    a, b = rcs[m].get("pref", {}), rcs[m + 1].get("pref", {})
                    for k in a:
                        if k in b:
                            for v in a[k] - b[k]: ex[(k, v)] = ex.get((k, v), 0) + 1
                for c in ex.values(): dist[c] = dist.get(c, 0) + 1
                if ex:
                    mx = max(ex.values()); worst.append((mx, len(key_[1]), nm))
                    tot = sum(ex.values())
                    if tot / len(key_[1]) > maxtot[0]: maxtot = (round(tot / len(key_[1]), 2), tot, f"{nm} |R| {len(key_[1])} visits {len(rcs)}")
    worst.sort(reverse=True)
    print("exits per (context, step, vertex): distribution", dict(sorted(dist.items())))
    print("max exits per (context, step, vertex), top 5:", worst[:5])
    print("max total exits per context / |R|:", maxtot)
