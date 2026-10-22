#!/usr/bin/env python3
"""L-RED box 10 (produced on Opus 5.5): Σ_q k_q per (context, phase) = number of relevant-steal EVENTS, with exactly the event
definition of L-ALG's dtl_stealdepth.analyze (t fired at step k in visit i, not excluded there, excluded at k in visit i+1;
copied here as a count only), on the unmodified model run (dtl_stealdepth.run_game). Prints max over contexts of Σ_q k_q,
that context's |R| and visits, and the number of distinct q. Usage: DTL_ORDER=stable|oink sumk.py G.pg"""
import sys, os
A = os.path.join(os.environ["LALG_DIR"], "experiments", "alg"); sys.path.insert(0, A); sys.path.insert(0, os.path.join(A, "..", "harness"))
for k_, v_ in (("RM_DV", "0"), ("RM_LIGHT", "1"), ("RM_EXCL", "1"), ("RM_PREF", "1")): os.environ[k_] = v_
import pg, dtl_stealdepth as SD
sys.setrecursionlimit(100000)
d = SD.run_game(pg.read(sys.argv[1]), os.environ.get("DTL_ORDER", "stable")); best = (0, 0, 0, 0)
for ph in SD.FD.phase_rows(d):
    vis = {}
    for r_ in ph:
        for rc in r_["recs"]: vis.setdefault(rc["key"], []).append(rc)
    for key, rcs in vis.items():
        ev = []
        for i in range(len(rcs) - 1):
            x, y = rcs[i], rcs[i + 1]; ex, ey, fx = x.get("excl", {}), y.get("excl", {}), x.get("fired", {})
            for k in ey:
                if k in ex:
                    for t in ey[k]:
                        if t < x["ntv"] and t not in ex[k] and t in fx.get(k, frozenset()): ev.append((k, t))
        best = max(best, (len(ev), len(key[1]), len(rcs), len(set(ev))))
print(f"max sum_q k_q {best[0]} (|R| {best[1]}, visits {best[2]}, distinct q {best[3]})")
