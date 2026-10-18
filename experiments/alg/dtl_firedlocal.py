"""L-ALG succ. 8 (produced on Opus 5.5, 2026-10-18 box 10), (FIRED⁺-R) BELOW the root (GAP-A-M §23s; at G′ it is (SPP)): where are
the tangles that fire at a non-root context R born? A tangle is born in sptl at a context B (dtl_rootmono bornR: (depth, arena)).
Classes per fired tangle t of #fired⁺(R) (dtl_changenew.sig_used over all visits of R in the phase): LOCAL (B ⊆ R), ANCESTOR
(B ⊋ R), OTHER (B incomparable with R), OLD (born before the phase). Printed: counts per class over depth ≥ 1 contexts with ≥ 2
visits; max #fired⁺(R)/|R| and max #LOCAL/|R| at depth ≥ 1, with contexts.
Usage: RM_LIGHT=1 RM_DV=0 DTL_ORDER=oink|stable [UNIONS=..] dtl_firedlocal.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import dtl_drthr as DT, dtl_changenew as CN, dtl_step5stats as ST
FD = DT.FD

if __name__ == "__main__":
    sys.setrecursionlimit(100000); tot = {}; mxF = (0.0, ""); mxL = (0.0, "")
    for f, g in ST.games(sys.argv[1:]):
        d0 = FD.P.X.build(g); d = DT.DR(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx; d.run()
        nm = f if f.startswith(("union", "random")) else os.path.relpath(f)
        if not all(w is not None for w in d.win): print("INCOMPLETE", nm, flush=True)
        born = getattr(d, "bornR", {})
        for ph in FD.phase_rows(d):
            visits = {}
            for r_ in ph:
                for rc in r_["recs"]: visits.setdefault(rc["key"], []).append((r_, rc))
            ntv0 = min(rc["ntv"] for r_ in ph for rc in r_["recs"]) if ph and any(r_["recs"] for r_ in ph) else 0
            for key_, vl in visits.items():
                if key_[0] == 0 or len(vl) < 2 or not key_[1]: continue
                R = key_[1]; fp = set()
                for r_, rc in vl: fp |= CN.sig_used(r_, rc)[1]
                loc = 0
                for t in fp:
                    b = born.get(t)
                    if t < ntv0 or b is None: c = "OLD (born before the phase)"
                    elif b[1] <= R: c = "LOCAL (born in a context ⊆ R)"; loc += 1
                    elif b[1] >= R: c = "ANCESTOR (born in a context ⊋ R)"
                    else: c = "OTHER (born in an incomparable context)"
                    tot[c] = tot.get(c, 0) + 1
                tot["contexts (depth ≥ 1, ≥ 2 visits)"] = tot.get("contexts (depth ≥ 1, ≥ 2 visits)", 0) + 1
                if len(fp) / len(R) > mxF[0]: mxF = (round(len(fp) / len(R), 3), f"{nm} depth {key_[0]} |R| {len(R)} fired⁺ {len(fp)} visits {len(vl)}")
                if loc / len(R) > mxL[0]: mxL = (round(loc / len(R), 3), f"{nm} depth {key_[0]} |R| {len(R)} local {loc} visits {len(vl)}")
    print("max #fired⁺/|R| (depth ≥ 1):", mxF); print("max #LOCAL/|R| (depth ≥ 1):", mxL)
    for k in sorted(tot): print(f"{tot[k]:7d}  {k}")
