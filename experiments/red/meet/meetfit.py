#!/usr/bin/env python3
"""L-RED box 7 (produced on Opus 5.5): graded screen for L-ALG's (MEET) / (PHASE-IN) / (PHASE-IN-MEET) (GAP-C §18r).
Same predicates as L-ALG experiments/alg/dtl_meetd.py (imported model dtl_step5 from LALGM_DIR, unmodified); this file is a
SCREEN only: every hit is re-judged by running dtl_meetd.py itself and pinned Oink. Per search(p) with D = W_p(G') != {}:
  meet = new tangles meeting D (0 and no dominion = MEET fails); lag = same-p same-G' searches from this one until one
  learns inside D or finds a dominion (None = PHASE-IN fails). Score: 1e12 incomplete + 1e11 failure + 1e8 max lag +
  1e6 * (#searches with meet <= 1 and no dominion) + 1e3 * max outside-D tangles (score_old). score_m: MEET-focused.
Usage: meetfit.py G.pg ... (order from DTL_ORDER)"""
import sys, os
sys.path.insert(0, os.path.join(os.environ["LALGM_DIR"], "experiments", "alg"))
sys.path.insert(0, os.path.join(os.environ["LALGM_DIR"], "experiments", "harness"))
import pg, dtl_step5 as S5


def measure_game(g, order):
    os.environ["DTL_ORDER"] = order
    d = S5.build(g); d.run(); tr = d.trace
    m = dict(incomplete=int(not all(w is not None for w in d.win)), meetfail=0, phasefail=0, maxlag=0, lowmeet=0,
             maxout=0, searches=len(tr), wsearch=0, first=None, meet1=0, near=0)
    for i, t in enumerate(tr):
        D = t["Wp"]
        if not D: continue
        m["wsearch"] += 1; new = t["newt"]; dom = t["dom"]
        meet = sum(1 for C in new if C & D)
        if not dom:
            if meet == 0: m["meetfail"] += 1; m["first"] = m["first"] or ("MEET", i)
            if meet <= 1: m["lowmeet"] += 1
            if meet == 1:
                m["meet1"] += 1
                if not any(C <= D for C in new): m["near"] += 1      # the one meeting tangle straddles D (kin_viol_n29 shape)
            m["maxout"] = max(m["maxout"], sum(1 for C in new if not C & D))
        lag, ok = 0, False
        for u in tr[i:]:
            if u["p"] != t["p"] or u["G"] != t["G"]:
                if u["p"] == t["p"]: break
                continue
            if u["dom"] or any(C <= D for C in u["newt"]): ok = True; break
            lag += 1
        if not ok: m["phasefail"] += 1; m["first"] = m["first"] or ("PHASE-IN", i)
        else: m["maxlag"] = max(m["maxlag"], lag)
    return m


def score_m(m):
    """MEET-focused: 1e12 incomplete + 1e11 MEET failure + 1e9 near (meet = 1, straddling) + 1e7 meet1 + 1e4 maxout + searches."""
    return (1e12 * m["incomplete"] + 1e11 * (m["meetfail"] > 0) + 1e9 * min(m["near"], 9) + 1e7 * min(m["meet1"], 9)
            + 1e4 * min(m["maxout"], 99) + min(m["searches"], 999))


def score(path):
    """dtl_search.py --fitness meet entry point (order from DTL_ORDER)."""
    sys.setrecursionlimit(100000)
    return int(score_m(measure_game(pg.read(path), os.environ.get("DTL_ORDER", "stable"))))


def score_old(m):
    return (1e12 * m["incomplete"] + 1e11 * (m["meetfail"] + m["phasefail"] > 0) + 1e8 * min(m["maxlag"], 999)
            + 1e6 * min(m["lowmeet"], 99) + 1e3 * min(m["maxout"], 999) + min(m["searches"], 999))


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    for f in sys.argv[1:]:
        m = measure_game(pg.read(f), os.environ.get("DTL_ORDER", "stable")); print(f, int(score_m(m)), m)
