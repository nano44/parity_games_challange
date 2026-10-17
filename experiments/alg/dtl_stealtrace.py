"""L-ALG succ. 7 (produced on Opus 5.5, 2026-10-17 box 8), GAP-A-M §23b: trace every (STEALER-MONO) failure.
Same model, order datum and visit notion as dtl_rootmono.py with RM_EXCL=1 RM_PREF=1 (it imports dtl_rootmono.RM; set
both flags). For each relevant steal (context, step σ = (round, top), fired tangle t) at visit pair (i, i+1), with
stealing vertices W = t ∩ P_{i+1}(σ) and stealing regions (same round, earlier top) meeting W, print the first later visit
j > i+1 at which a stealing region lacks some of its visit-(i+1) vertices (the dtl_rootmono test): the lost vertices, whether any is in W (STOLEN-PERM), which
relevant steals happen at visit pair (j-1, j) (step, tangle, stealing tops), and whether the losing region's own fired
tangles at visit j-1 are among them. Also per relevant triple: count and whether t refires / is later unmet.
Usage: RM_EXCL=1 RM_PREF=1 RM_LIGHT=1 RM_DV=0 DTL_ORDER=oink|stable dtl_stealtrace.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import dtl_rootmono as RMM, dtl_step5stats as ST
FD = RMM.FD


def rel_steals(x, y):
    """Relevant steals between consecutive visits x -> y: list of (step, tangle)."""
    ex_, ey_, fx_ = x.get("excl", {}), y.get("excl", {}), x.get("fired", {})
    return [(k_, t) for k_ in ey_ if k_ in ex_ for t in ey_[k_] if t < x["ntv"] and t not in ex_[k_] and t in fx_.get(k_, frozenset())]


if __name__ == "__main__":
    assert os.environ.get("RM_EXCL") and os.environ.get("RM_PREF"), "set RM_EXCL=1 RM_PREF=1"
    sys.setrecursionlimit(100000); tot = {}
    for f, g in ST.games(sys.argv[1:]):
        d0 = FD.P.X.build(g); d = RMM.RM(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx; d.run()
        nm = f if f.startswith(("union", "random")) else os.path.relpath(f); X = d.idx
        for phn, ph in enumerate(FD.phase_rows(d)):
            visits = {}
            for si, r_ in enumerate(ph):
                for rc in r_["recs"]: visits.setdefault(rc["key"], []).append((si, rc))
            for key_, vl in visits.items():
                rcs = [rc for _, rc in vl]; sis = [si for si, _ in vl]; trip = {}
                for i in range(len(rcs) - 1):
                    x, y = rcs[i], rcs[i + 1]
                    for k_, t in rel_steals(x, y):
                        trip[(k_, t)] = trip.get((k_, t), 0) + 1
                        later = rcs[i + 1:]
                        unmet = any(k_ in z.get("excl", {}) and t not in z["excl"][k_] and
                                    not any(v in z["pref"].get(k_, frozenset()) for v, _ in d.tv[t]) for z in later)
                        refire = any(t in z.get("fired", {}).get(k_, frozenset()) for z in rcs[i + 2:])
                        W = frozenset(v for v, _ in d.tv[t] if v in y["pref"].get(k_, frozenset()))
                        rsy = y["regset"]; stealers = [kk for kk in rsy if kk[0] == k_[0] and kk[1] > k_[1] and rsy[kk] & W]
                        kk_ = "STAYS-MET (t never unmet at σ later): " + ("FAILS" if unmet else "holds"); tot[kk_] = tot.get(kk_, 0) + 1
                        kk_ = "NO-REFIRE: " + ("FAILS" if refire else "holds"); tot[kk_] = tot.get(kk_, 0) + 1
                        bad = False
                        for kk in stealers:
                            for j in range(i + 2, len(rcs)):
                                z = rcs[j]; cur = z["regset"].get(kk)
                                if cur is None: continue
                                lost = rsy[kk] - cur
                                if lost:
                                    bad = True; zp = rcs[j - 1]
                                    rs = rel_steals(zp, z)
                                    own = zp.get("fired", {}).get(kk, frozenset())
                                    print(f"STEALER LOSS {nm} phase {phn} ctx depth {key_[0]} |R| {len(key_[1])} | steal at visits {i}->{i+1} (searches {sis[i]}->{sis[i+1]}) step (round {k_[0]}, top {X[k_[1]]}) tangle {t} W {sorted(X[v] for v in W)}",
                                          f"| stealing region (round {kk[0]}, top {X[kk[1]]}) loses {sorted(X[v] for v in lost)} at visit {j} (search {sis[j]}); lost ∩ W = {sorted(X[v] for v in lost & W)}",
                                          f"| relevant steals at visits {j-1}->{j}: {sorted((s_[0], X[s_[1]], tt) for s_, tt in rs)}; own fired tangles of the region stolen: {sorted(tt for s_, tt in rs if tt in own)}",
                                          f"| region tops at visit {j-1}: {[X[kk2[1]] for kk2 in sorted(zp['regset'], key=lambda q: (q[0], -q[1])) if kk2[0] == kk[0]]}", flush=True)
                                    break
                        kk_ = "STEALER-MONO: " + ("FAILS" if bad else "holds"); tot[kk_] = tot.get(kk_, 0) + 1
                if trip:
                    m = max(trip.values()); kk_ = f"STEAL-ONCE* per (context, round, top, tangle): max {m}"; tot[kk_] = tot.get(kk_, 0) + 1
                    for (k_, t), c in trip.items():
                        if c > 1: print(f"STEAL-ONCE* VIOLATION {nm} phase {phn} ctx |R| {len(key_[1])} step (round {k_[0]}, top {X[k_[1]]}) tangle {t}: {c} relevant steals", flush=True)
    for k in sorted(tot): print(f"{tot[k]:6d}  {k}")
