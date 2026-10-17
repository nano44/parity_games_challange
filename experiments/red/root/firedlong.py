#!/usr/bin/env python3
"""L-RED box 7 (produced on Opus 5.5), Lead 16:22Z target: many distinct tangles FIRING at ONE context over a LONG phase
(GAP-A-M §22u/§22w (FIRED-R); only phases with S >= 2|R| count, S = searches in the phase). Same model and same fired-set
union as L-ALG's experiments/alg/dtl_firedclimb.fitness (dtl_rootmono.RM UNMODIFIED with RM_EXCL=1, RM_LIGHT=1, RM_DV=0;
LALGR_DIR = l-alg >= 43302c11), plus the long-phase filter. Per context visited >= 2 times in a phase with S >= 2|R|:
fired = distinct tangles fired over the phase. Score: 1e12 incomplete + 1e7 * (max fired/|R| per mille) + 1e4 * that
context's fired + max S/|R| (x10) over the counted contexts. Usage: firedlong.py G.pg ... (order from DTL_ORDER)"""
import sys, os
for k, v in (("RM_DV", "0"), ("RM_LIGHT", "1"), ("RM_EXCL", "1")): os.environ.setdefault(k, v)
sys.path.insert(0, os.path.join(os.environ["LALGR_DIR"], "experiments", "alg"))
sys.path.insert(0, os.path.join(os.environ["LALGR_DIR"], "experiments", "harness"))
import pg, dtl_rootmono as RMo
FD = RMo.FD


def measure_game(g, order):
    os.environ["DTL_ORDER"] = order
    d0 = FD.P.X.build(g); d = RMo.RM(d0.pr, d0.ow, d0.outs, ins_desc=(order == "oink")); d.idx = d0.idx; d.run()
    m = dict(incomplete=int(not all(w is not None for w in d.win)), ratio=0.0, fired=0, R=0, S=0, SR=0.0, maxS=0)
    for ph in FD.phase_rows(d):
        S = len(ph); m["maxS"] = max(m["maxS"], S); visits = {}
        for r in ph:
            for rc in r["recs"]: visits.setdefault(rc["key"], []).append(rc)
        for key_, vl in visits.items():
            R = len(key_[1])
            if len(vl) < 2 or R == 0 or S < 2 * R: continue
            fired = set()
            for rc in vl:
                for fs in rc.get("fired", {}).values(): fired |= fs
            cand = (round(len(fired) / R, 3), len(fired))
            if cand > (m["ratio"], m["fired"]): m.update(ratio=cand[0], fired=cand[1], R=R, S=S)
            m["SR"] = max(m["SR"], S / R)
    return m


def score(path):
    sys.setrecursionlimit(100000); m = measure_game(pg.read(path), os.environ.get("DTL_ORDER", "stable"))
    return int(1e12 * m["incomplete"] + 1e7 * min(int(1000 * m["ratio"]), 9999) + 1e4 * min(m["fired"], 999) + min(int(10 * m["SR"]), 9999))


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    for f in sys.argv[1:]:
        m = measure_game(pg.read(f), os.environ.get("DTL_ORDER", "stable")); print(os.path.relpath(f), m, flush=True)
