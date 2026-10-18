"""L-ALG succ. 8 (produced on Opus 5.5, 2026-10-18 box 10), toward (EXIT_c): how often does the number of rounds of a context's
best_vertices call (len(rec["rtop"])) fall across consecutive visits in one phase? Each fall of a res = -1 call's round count
empties its last rounds on the §23t grid (P = ∅ after a V = ∅ stop), i.e. exits for every vertex there. (EXIT_c) therefore
needs the round count of a context to fall O(c) times per phase. Printed: histogram of round-count falls per context (contexts
with ≥ 2 visits), the max, and its context. Usage: RM_LIGHT=1 RM_DV=0 DTL_ORDER=oink|stable [UNIONS=..] dtl_roundfalls.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import dtl_drthr as DT, dtl_step5stats as ST
FD = DT.FD

if __name__ == "__main__":
    sys.setrecursionlimit(100000); hist = {}; mx = (0, "")
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
                seq = [(len(rc.get("rtop", [])), rc["res"]) for _, rc in vl]
                fl = sum(1 for a, b in zip(seq, seq[1:]) if b[0] < a[0])
                hist[fl] = hist.get(fl, 0) + 1
                if fl > mx[0]: mx = (fl, f"{nm} depth {key_[0]} |R| {len(key_[1])} rounds/res {seq}")
    print("round-count falls per context: histogram", dict(sorted(hist.items())))
    print("max:", mx)
