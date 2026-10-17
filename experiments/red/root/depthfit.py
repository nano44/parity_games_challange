#!/usr/bin/env python3
"""L-RED box 8 (produced on Opus 5.5), Lead 20:11Z: re-steal DEPTH (GAP-A-M §23g, Lemma CHARGE, (STEAL-DEPTH_D)). Runs L-ALG's
experiments/alg/dtl_stealdepth.py analyze() UNMODIFIED (LALGR_DIR >= 931fc221; RM_EXCL=1 RM_PREF=1 RM_LIGHT=1 RM_DV=0) on one
order datum (DTL_ORDER). Score: 1e12 incomplete + 1e9 min(max depth, 999) + 1e6 min(max k, 999) + 1e3 min(#re-steals, 999)
+ min(#relevant steals, 999). Usage: depthfit.py G.pg ... (prints max k, max depth, no-cause, re-steals, steals)"""
import sys, os
for k, v in (("RM_DV", "0"), ("RM_LIGHT", "1"), ("RM_EXCL", "1"), ("RM_PREF", "1")): os.environ[k] = v
sys.path.insert(0, os.path.join(os.environ["LALGR_DIR"], "experiments", "alg"))
sys.path.insert(0, os.path.join(os.environ["LALGR_DIR"], "experiments", "harness"))
import pg, dtl_stealdepth as SD


def measure_game(g, order):
    d = SD.run_game(g, order); tot = {}
    maxk, maxd, noc = SD.analyze(d, "", tot, [])
    rs = sum(v for k, v in tot.items() if k.startswith("RE-STEAL depth"))
    st = sum(v for k, v in tot.items() if k.startswith("k per context"))
    return dict(incomplete=int(not all(w is not None for w in d.win)), maxk=maxk, maxd=maxd, nocause=noc, resteals=rs, ctxs=st, tot=tot)


def score(path):
    sys.setrecursionlimit(100000); m = measure_game(pg.read(path), os.environ.get("DTL_ORDER", "stable"))
    return int(1e12 * m["incomplete"] + 1e9 * min(m["maxd"], 999) + 1e6 * min(m["maxk"], 999) + 1e3 * min(m["resteals"], 999) + min(m["ctxs"], 999))


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    for f in sys.argv[1:]:
        m = measure_game(pg.read(f), os.environ.get("DTL_ORDER", "stable")); m.pop("tot"); print(os.path.relpath(f), m, flush=True)
