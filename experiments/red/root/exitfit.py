#!/usr/bin/env python3
"""L-RED box 8 (produced on Opus 5.5), Lead 22:48Z: (EXIT_c) target (GAP-A-M §23p): EXITS per (context, step k, vertex v) =
visit pairs m with v in P_m(k) and v not in P_{m+1}(k), exactly as L-ALG's experiments/alg/dtl_prefexits.py (l-alg f1b3ba0b;
dtl_stealdepth.run_game records, unmodified). Score: 1e12 incomplete + 1e9 max exits + 1e6 #(k, v) at the max + 1e3 #(k, v)
with >= 2 exits + total exits (capped). Judge every hit with the unmodified dtl_prefexits.py. Usage: exitfit.py G.pg ..."""
import sys, os
for k, v in (("RM_DV", "0"), ("RM_LIGHT", "1"), ("RM_EXCL", "1"), ("RM_PREF", "1")): os.environ[k] = v
sys.path.insert(0, os.path.join(os.environ["LALGR_DIR"], "experiments", "alg"))
sys.path.insert(0, os.path.join(os.environ["LALGR_DIR"], "experiments", "harness"))
import pg, dtl_stealdepth as SD
FD = SD.FD


def measure_game(g, order):
    d = SD.run_game(g, order); m = dict(incomplete=int(not all(w is not None for w in d.win)), maxex=0, atmax=0, two=0, tot=0)
    allc = []
    for ph in FD.phase_rows(d):
        visits = {}
        for r_ in ph:
            for rc in r_["recs"]: visits.setdefault(rc["key"], []).append(rc)
        for key_, rcs in visits.items():
            ex = {}
            for i in range(len(rcs) - 1):
                a, b = rcs[i].get("pref", {}), rcs[i + 1].get("pref", {})
                for k in a:
                    if k in b:
                        for v in a[k] - b[k]: ex[(k, v)] = ex.get((k, v), 0) + 1
            allc += list(ex.values())
    if allc:
        m["maxex"] = max(allc); m["atmax"] = allc.count(m["maxex"]); m["two"] = sum(1 for c in allc if c >= 2); m["tot"] = sum(allc)
    return m


def score(path):
    sys.setrecursionlimit(100000); m = measure_game(pg.read(path), os.environ.get("DTL_ORDER", "stable"))
    return int(1e12 * m["incomplete"] + 1e9 * min(m["maxex"], 999) + 1e6 * min(m["atmax"], 999) + 1e3 * min(m["two"], 999) + min(m["tot"], 999))


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    for f in sys.argv[1:]: print(os.path.relpath(f), measure_game(pg.read(f), os.environ.get("DTL_ORDER", "stable")), flush=True)
