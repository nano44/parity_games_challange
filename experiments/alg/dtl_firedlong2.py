"""L-ALG succ. 7 (produced on Opus 5.5, 2026-10-17 box 8), GAP-A-M §23d: (FIRED-R) on LONG phases only. Same model
(dtl_rootmono.RM with RM_EXCL=1; fired sets per best_vertices region step) and the same filter as L-RED's
experiments/red/root/firedlong.py (l-red 2486288): a context counts in a phase with S searches if it is visited >= 2 times
and S >= 2|R|. Per counted context: fired = distinct tangles fired at it over the phase, split into tangles born before
the phase (index < k0, k0 = tangle count at the phase's first search) and born in the phase; for the latter, where they were
born: the sptl arena R' of the extraction (R' ⊆ R, R' ⊋ R, or incomparable). Per step (round, top): NO-RETURN (a tangle
that fired at the step at visit i, did not fire there at a later visit j, never fires there again) and the max number of
distinct tangles fired at one step. FL_ALL=1 drops the long-phase filter (every context visited >= 2 times). Usage: RM_EXCL=1 RM_LIGHT=1 RM_DV=0 DTL_ORDER=oink|stable dtl_firedlong2.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import dtl_rootmono as RMM, dtl_step5stats as ST
FD = RMM.FD; D = FD.D


class FL(RMM.RM):
    def sptl(s, V, R, p):
        s._spR = frozenset(R); return RMM.RM.sptl(s, V, R, p)

    def extractTangles(s, top, R):
        k = len(s.tv); r = RMM.RM.extractTangles(s, top, R)
        if not hasattr(s, "born"): s.born = {}
        for t in range(k, len(s.tv)): s.born[t] = getattr(s, "_spR", None)
        return r


if __name__ == "__main__":
    assert os.environ.get("RM_EXCL"), "set RM_EXCL=1"
    sys.setrecursionlimit(100000); tot = {}; rows = []
    for f, g in ST.games(sys.argv[1:]):
        d0 = FD.P.X.build(g); d = FL(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx; d.run()
        nm = f if f.startswith(("union", "random")) else os.path.relpath(f)
        if not all(w is not None for w in d.win): print("INCOMPLETE", nm, flush=True)
        for ph in FD.phase_rows(d):
            S = len(ph); k0 = min(rc["ntv"] for r_ in ph for rc in r_["recs"]) if any(r_["recs"] for r_ in ph) else 0
            visits = {}
            for r_ in ph:
                for rc in r_["recs"]: visits.setdefault(rc["key"], []).append(rc)
            for key_, rcs in visits.items():
                R = key_[1]
                if len(rcs) < 2 or not R or (S < 2 * len(R) and os.environ.get("FL_ALL") != "1"): continue
                fired = set(); per = {}; seq = {}
                for i, rc in enumerate(rcs):
                    for k_, fs in rc.get("fired", {}).items():
                        fired |= fs; per.setdefault(k_, set()).update(fs)
                        for t in fs: seq.setdefault((k_, t), []).append(i)
                ret = 0
                for (k_, t), ivs in seq.items():
                    pres = [i for i, rc in enumerate(rcs) if k_ in rc.get("fired", {})]      # visits where the step exists
                    on = [i in ivs for i in pres]
                    # a return: on, then off at a visit where the step exists, then on again
                    st_ = 0
                    for b in on:
                        if st_ == 0 and b: st_ = 1
                        elif st_ == 1 and not b: st_ = 2
                        elif st_ == 2 and b: ret += 1; break
                kq = "NO-RETURN per (step, tangle): " + ("FAILS" if ret else "holds"); tot[kq] = tot.get(kq, 0) + 1
                old = {t for t in fired if t < k0}; new = fired - old
                bw = {"inside R": 0, "strictly larger arena": 0, "incomparable": 0, "unknown": 0}
                for t in new:
                    b = getattr(d, "born", {}).get(t)
                    bw["unknown" if b is None else "inside R" if b <= R else "strictly larger arena" if b > R else "incomparable"] += 1
                mstep = max((len(v) for v in per.values()), default=0)
                rows.append((round(len(fired) / len(R), 3), len(fired), len(old), len(new), bw["inside R"], bw["strictly larger arena"], bw["incomparable"], mstep, len(R), S, len(rcs), ret, nm))
    rows.sort(reverse=True)
    print("ratio fired old new | born: inside R, larger, incomparable | max per step | |R| S visits returns | game")
    for r in rows[:25]: print(*r)
    if rows:
        print(f"contexts {len(rows)}; max ratio {rows[0][0]}; max fired {max(r[1] for r in rows)}; contexts with returns {sum(1 for r in rows if r[11])}")
        print(f"new tangles born inside R: {sum(r[4] for r in rows)}, in a strictly larger arena: {sum(r[5] for r in rows)}, incomparable: {sum(r[6] for r in rows)}; old: {sum(r[2] for r in rows)}")
        ms = max(r[7] for r in rows); print(f"max distinct tangles fired at one step (round, top) in a phase: {ms}; contexts with that max: {sum(1 for r in rows if r[7] == ms)}")
        print("top per-step rows:", *sorted(rows, key=lambda r: -r[7])[:5], sep="\n  ")
    for k in sorted(tot): print(f"{tot[k]:7d}  {k}")
