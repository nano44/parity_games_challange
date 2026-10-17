#!/usr/bin/env python3
"""L-RED box 8 (produced on Opus 5.5): design tracer for hand-built (STOLEN-PERM) / (FIRED-R) gadgets. Runs L-ALG's
dtl_rootmono.RM UNMODIFIED (LALGR_DIR; RM_EXCL=1 RM_PREF=1 RM_LIGHT=1 RM_DV=0) and prints, per phase and per context
visited >= MINV times (default 2): for each visit (search index) and each step (round, top) the region, the fired
tangles and the excluded tangles; then the tangles (vertices, escapes) by id. Ids are FILE ids.
Usage: steptrace.py G.pg [MINV] (order from DTL_ORDER)"""
import sys, os
for k, v in (("RM_DV", "0"), ("RM_LIGHT", "1"), ("RM_EXCL", "1"), ("RM_PREF", "1")): os.environ[k] = v
sys.path.insert(0, os.path.join(os.environ["LALGR_DIR"], "experiments", "alg"))
sys.path.insert(0, os.path.join(os.environ["LALGR_DIR"], "experiments", "harness"))
import pg, dtl_rootmono as RMo
FD = RMo.FD

if __name__ == "__main__":
    sys.setrecursionlimit(100000); order = os.environ.get("DTL_ORDER", "stable"); minv = int(sys.argv[2]) if len(sys.argv) > 2 else 2
    g = pg.read(sys.argv[1]); d0 = FD.P.X.build(g); d = RMo.RM(d0.pr, d0.ow, d0.outs, ins_desc=(order == "oink")); d.idx = d0.idx; d.run()
    X = d.idx; S = lambda vs: sorted(X[v] for v in vs)
    print("complete:", all(w is not None for w in d.win), "tangles:", len(d.tv))
    used = set()
    for phn, ph in enumerate(FD.phase_rows(d)):
        visits = {}
        for si, r_ in enumerate(ph):
            for rc in r_["recs"]: visits.setdefault(rc["key"], []).append((si, rc))
        print(f"== phase {phn}: {len(ph)} searches, |G'| {len(ph[0]['G'])}")
        for key_, vl in sorted(visits.items(), key=lambda kv: (kv[0][0], -len(kv[0][1]))):
            if len(vl) < minv: continue
            print(f"-- ctx depth {key_[0]} |R| {len(key_[1])} R {S(key_[1])} visits {[si for si, _ in vl]}")
            for si, rc in vl:
                print(f"   search {si}: res {rc.get('res')}")
                for k_ in sorted(rc.get("regset", {}), key=lambda q: (q[0], -q[1])):
                    f_ = sorted(rc["fired"].get(k_, ())); e_ = sorted(rc["excl"].get(k_, ())); used |= set(f_) | set(e_)
                    print(f"     ({k_[0]}, top {X[k_[1]]}) region {S(rc['regset'][k_])} fired {f_} excl {e_}")
    print("== tangles (id: vertices | escapes | priority)")
    for t in sorted(used):
        print(f"   {t}: {S([v for v, _ in d.tv[t]])} | {S(d.tout[t])} | {d.tpr[t]}")
