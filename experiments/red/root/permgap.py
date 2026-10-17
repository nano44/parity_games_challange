#!/usr/bin/env python3
"""L-RED box 8 (produced on Opus 5.5), Lead plan item (1): graded fitness toward a (STOLEN-PERM) failure (GAP-A-M §23b).
Same model, visits and relevant-steal notion as L-ALG's dtl_rootmono.py / dtl_stealtrace.py (dtl_rootmono.RM imported
UNMODIFIED from LALGR_DIR, RM_EXCL=1 RM_PREF=1 RM_LIGHT=1 RM_DV=0; RM_LIGHT changes no pref/regset/excl/fired set, §23b).
For each relevant steal (context, step σ, tangle t) at visit pair (i, i+1), W = t ∩ P_{i+1}(σ), and each later visit z
(j > i+1) where σ exists: lost = P_{i+1}(σ) − P_z(σ).
  hit   : lost ∩ W ≠ ∅  (= dtl_rootmono "STOLEN-PERM ...: FAILS"; a hit is only reported after the unmodified judge agrees)
  near2 : lost meets a stealing region of the steal (a region (round σ, earlier top) at visit i+1 meeting W)
  near1 : lost ≠ ∅
  pairs : (steal, later visit with σ) pairs
Score: 1e12 hit + 1e9 min(near2, 999) + 1e6 min(near1, 999) + 1e3 min(pairs, 999) + min(relevant steals, 999).
PERMFIT=stealk: (STEAL-ONCE*) growth after R35: score 1e9 min(maxk, 999) + 1e6 min(hit, 999) + 1e3 min(near1, 999) + steals,
maxk = max relevant steals per (context, round, top, tangle) over the phase (dtl_stealtrace's count).
PERMFIT=firedstep: (FIRED-STEP) growth (GAP-A-M §23d): score 1e9 min(maxstep, 999) + 1e6 min(maxk, 999) + 1e3 min(hit, 999) + steals,
maxstep = max distinct tangles fired at one step (context, round, top) over a phase, every context (contexts visited >= 2 times, as dtl_firedlong2 FL_ALL=1).
Usage: permgap.py G.pg ... (order from DTL_ORDER); prints the counts."""
import sys, os
for k, v in (("RM_DV", "0"), ("RM_LIGHT", "1"), ("RM_EXCL", "1"), ("RM_PREF", "1")): os.environ[k] = v
sys.path.insert(0, os.path.join(os.environ["LALGR_DIR"], "experiments", "alg"))
sys.path.insert(0, os.path.join(os.environ["LALGR_DIR"], "experiments", "harness"))
import pg, dtl_rootmono as RMo
FD = RMo.FD


def rel_steals(x, y):
    ex_, ey_, fx_ = x.get("excl", {}), y.get("excl", {}), x.get("fired", {})
    return [(k_, t) for k_ in ey_ if k_ in ex_ for t in ey_[k_] if t < x["ntv"] and t not in ex_[k_] and t in fx_.get(k_, frozenset())]


def measure_game(g, order):
    os.environ["DTL_ORDER"] = order
    d0 = FD.P.X.build(g); d = RMo.RM(d0.pr, d0.ow, d0.outs, ins_desc=(order == "oink")); d.idx = d0.idx; d.run()
    m = dict(incomplete=int(not all(w is not None for w in d.win)), hit=0, near2=0, near1=0, pairs=0, steals=0, maxk=0, maxstep=0, ex=None)
    for ph in FD.phase_rows(d):
        visits = {}
        for r_ in ph:
            for rc in r_["recs"]: visits.setdefault(rc["key"], []).append(rc)
        for key_, rcs in visits.items():
            trip = {}; fst = {}
            for rc in rcs:
                for k_, fs in rc.get("fired", {}).items(): fst.setdefault(k_, set()).update(fs)
            if fst and len(rcs) >= 2: m["maxstep"] = max(m["maxstep"], max(len(v) for v in fst.values()))
            for i in range(len(rcs) - 1):
                x, y = rcs[i], rcs[i + 1]
                for k_, t in rel_steals(x, y):
                    m["steals"] += 1; trip[(k_, t)] = trip.get((k_, t), 0) + 1; m["maxk"] = max(m["maxk"], trip[(k_, t)])
                    Py = y["pref"].get(k_, frozenset()); W = frozenset(v for v, _ in d.tv[t] if v in Py)
                    rsy = y["regset"]; stl = frozenset().union(*[rsy[kk] for kk in rsy if kk[0] == k_[0] and kk[1] > k_[1] and rsy[kk] & W])
                    for z in rcs[i + 2:]:
                        if k_ not in z.get("pref", {}): continue
                        m["pairs"] += 1; lost = Py - z["pref"][k_]
                        if lost: m["near1"] += 1
                        if lost & stl: m["near2"] += 1
                        if lost & W:
                            m["hit"] += 1
                            if m["ex"] is None: m["ex"] = (len(key_[1]), k_, t, sorted(d.idx[v] for v in lost & W))
    return m


def score(path):
    sys.setrecursionlimit(100000); m = measure_game(pg.read(path), os.environ.get("DTL_ORDER", "stable"))
    if m["incomplete"]: return int(2e12)
    if os.environ.get("PERMFIT") == "firedstep":
        return int(1e9 * min(m["maxstep"], 999) + 1e6 * min(m["maxk"], 999) + 1e3 * min(m["hit"], 999) + min(m["steals"], 999))
    if os.environ.get("PERMFIT") == "stealk":
        return int(1e9 * min(m["maxk"], 999) + 1e6 * min(m["hit"], 999) + 1e3 * min(m["near1"], 999) + min(m["steals"], 999))
    return int(1e12 * (m["hit"] > 0) + 1e9 * min(m["near2"], 999) + 1e6 * min(m["near1"], 999) + 1e3 * min(m["pairs"], 999) + min(m["steals"], 999))


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    for f in sys.argv[1:]:
        print(os.path.relpath(f), measure_game(pg.read(f), os.environ.get("DTL_ORDER", "stable")), flush=True)
