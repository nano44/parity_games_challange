"""L-ALG succ. 7 (produced on Opus 5.5, 2026-10-17 box 8), GAP-A-M §23g: re-steal chains toward (STEAL-POLY).
Same model and visits as dtl_rootmono.py with RM_EXCL=1 RM_PREF=1 (dtl_rootmono.RM unmodified). Per context and phase,
EVENTS are the relevant steals (pair i → i+1, step k = (round, top), tangle t), i.e. t ∈ F_k at visit i and t
met-not-contained by P_{i+1}(k). For q = (k, t), the first event has depth 0. A later event of q at pair i, with the
previous event of q at pair j, is a RE-STEAL. Its CAUSES are the events at pairs m (j < m < i) where t ∩ P(k) loses a
vertex (P_m(k) ∩ t ⊄ P_{m+1}(k)), at a step strictly EARLIER than k (round smaller, or same round and higher top).
PREFIX-MONO-X* says such a cause exists, unless the shrink comes from a change of V in an earlier round; "no cause" is
printed. depth = 1 + min over causes of depth. Printed: max k_q, max depth, number of re-steals by depth, and each
re-steal with its causes.
Usage: RM_EXCL=1 RM_PREF=1 RM_LIGHT=1 RM_DV=0 DTL_ORDER=oink|stable dtl_stealdepth.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import dtl_rootmono as RMM, dtl_step5stats as ST
FD = RMM.FD


def earlier(a, b):
    """step a precedes step b in the step order (rounds ascending, tops descending)"""
    return a[0] < b[0] or (a[0] == b[0] and a[1] > b[1])


if __name__ == "__main__":
    assert os.environ.get("RM_EXCL") and os.environ.get("RM_PREF"), "set RM_EXCL=1 RM_PREF=1"
    sys.setrecursionlimit(100000); tot = {}; shown = 0; maxk = 0; maxd = 0
    for f, g in ST.games(sys.argv[1:]):
        d0 = FD.P.X.build(g); d = RMM.RM(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx; d.run()
        nm = f if f.startswith(("union", "random")) else os.path.relpath(f); X = d.idx
        if not all(w is not None for w in d.win): print("INCOMPLETE", nm, flush=True)
        for ph in FD.phase_rows(d):
            visits = {}
            for r_ in ph:
                for rc in r_["recs"]: visits.setdefault(rc["key"], []).append(rc)
            for key_, rcs in visits.items():
                ev = []                                         # (pair i, step k, tangle t)
                for i in range(len(rcs) - 1):
                    x, y = rcs[i], rcs[i + 1]
                    ex, ey, fx = x.get("excl", {}), y.get("excl", {}), x.get("fired", {})
                    for k in ey:
                        if k not in ex: continue
                        for t in ey[k]:
                            if t < x["ntv"] and t not in ex[k] and t in fx.get(k, frozenset()): ev.append((i, k, t))
                if not ev: continue
                depth = {}; last = {}; kq = {}
                for e in ev:                                    # ev is in pair order
                    i, k, t = e; q = (k, t); kq[q] = kq.get(q, 0) + 1
                    if q not in last: depth[e] = 0; last[q] = i; continue
                    j = last[q]; last[q] = i; tv = {v for v, _ in d.tv[t]}
                    shr = [m for m in range(j + 1, i) if k in rcs[m]["pref"] and k in rcs[m + 1]["pref"] and (rcs[m]["pref"][k] & tv) - rcs[m + 1]["pref"][k]]
                    causes = [c for c in ev if c[0] in shr and earlier(c[1], k) and c in depth]
                    if not causes:
                        depth[e] = None; kc = "RE-STEAL with no cause event (V change or tool gap)"; tot[kc] = tot.get(kc, 0) + 1
                        if shown < 30: shown += 1; print(f"NO CAUSE {nm} |R| {len(key_[1])} re-steal pair {i} step (r{k[0]}, top {X[k[1]]}) t {t}; previous pair {j}; shrink pairs {shr}", flush=True)
                        continue
                    ds = [depth[c] for c in causes if depth[c] is not None]
                    depth[e] = 1 + min(ds) if ds else None
                    kd = f"RE-STEAL depth {depth[e]}"; tot[kd] = tot.get(kd, 0) + 1
                    if shown < 30:
                        shown += 1
                        print(f"RE-STEAL {nm} |R| {len(key_[1])} pair {i} step (r{k[0]}, top {X[k[1]]}) t {t} k {kq[q]} depth {depth[e]} | previous {j} | causes (pair, step, tangle, depth): {[(c[0], (c[1][0], X[c[1][1]]), c[2], depth[c]) for c in causes][:5]}", flush=True)
                mk = max(kq.values()); maxk = max(maxk, mk)
                md = max((v for v in depth.values() if v is not None), default=0); maxd = max(maxd, md)
                kk = f"k per context (max over q): {mk}"; tot[kk] = tot.get(kk, 0) + 1
    print(f"max k {maxk}; max depth {maxd}")
    for k in sorted(tot): print(f"{tot[k]:7d}  {k}")
