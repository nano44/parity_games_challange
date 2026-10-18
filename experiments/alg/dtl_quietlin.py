"""L-ALG succ. 8 (produced on Opus 5.5, 2026-10-18 box 10), sharpening Lemma QUIET-BLOCK (GAP-A-M §23w): inside a maximal run of
consecutive QUIET pairs of a context (no grid entry or exit, dtl_drthr conventions), let A_i be the set of vertices that join some
U_r or some W_{r,t} at differing pair i (rec["psi"] = per round [U_r, W_{r,t} ...]). (QUIET-LIN) "each vertex is in A_i for at
most one differing pair i of a block" (KILLED, §23z) and the weaker (QUIET-NEWV) "every A_i has a vertex not in an earlier A_j of
its block" would each give block length ≤ |R| (linear). Printed: max over vertices of #pairs per block
containing it; max block length / |R|; examples (QL_SHOW, default 3).
Usage: RM_LIGHT=1 RM_DV=0 DTL_ORDER=oink|stable [UNIONS=..] dtl_quietlin.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import dtl_drthr as DT, dtl_changenew as CN, dtl_step5stats as ST
FD = DT.FD

if __name__ == "__main__":
    sys.setrecursionlimit(100000); tot = {}; mxv = (0, ""); mxr = (0.0, ""); shown = 0; nshow = int(os.environ.get("QL_SHOW", "3"))
    for f, g in ST.games(sys.argv[1:]):
        d0 = FD.P.X.build(g); d = DT.DR(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx; d.run()
        nm = f if f.startswith(("union", "random")) else os.path.relpath(f)
        if not all(w is not None for w in d.win): print("INCOMPLETE", nm, flush=True)
        for ph in FD.phase_rows(d):
            visits = {}
            for r_ in ph:
                for rc in r_["recs"]: visits.setdefault(rc["key"], []).append((r_, rc))
            for key_, vl in visits.items():
                if len(vl) < 2: continue
                R = key_[1]; p = vl[0][1]["p"]; grid = sorted(v for v in R if d.pr[v] % 2 == p)
                if not grid: continue
                nr = len(R) + 1; gs = [DT.grid_tops(rc, nr) for _, rc in vl]
                cnt = {}; blen = 0
                def close():
                    global mxv, mxr, shown
                    if cnt and max(cnt.values()) > mxv[0]: mxv = (max(cnt.values()), f"{nm} depth {key_[0]} |R| {len(R)} block {blen}")
                    if blen / len(R) > mxr[0]: mxr = (round(blen / len(R), 3), f"{nm} depth {key_[0]} |R| {len(R)} block {blen}")
                for i in range(len(vl) - 1):
                    (ra, x), (rb, y) = vl[i], vl[i + 1]
                    quiet = all(not (gs[i + 1][r].get(w, -1) > gs[i][r].get(w, -1) and any(gs[i][r].get(w, -1) <= t < gs[i + 1][r].get(w, -1) for t in grid))
                                and not (gs[i][r].get(w, -1) > gs[i + 1][r].get(w, -1) and any(gs[i + 1][r].get(w, -1) <= t < gs[i][r].get(w, -1) for t in grid))
                                for r in range(nr) for w in set(gs[i][r]) | set(gs[i + 1][r]))
                    if not quiet:
                        close(); cnt = {}; blen = 0; continue
                    if CN.sig_used(ra, x)[0] == CN.sig_used(rb, y)[0]: continue
                    px, py = x["psi"], y["psi"]; A = set()
                    for j in range(min(len(px), len(py))): A |= set(py[j] - px[j])
                    blen += 1
                    kn = "quiet differing pairs: QUIET-NEWV (a vertex never advanced before in the block) " + ("holds" if any(v not in cnt for v in A) else "FAILS"); tot[kn] = tot.get(kn, 0) + 1
                    if not any(v not in cnt for v in A) and shown < nshow: shown += 1; print("QUIET-NEWV FAILS", nm, "depth", key_[0], "|R|", len(R), "pair", i, "A", sorted(A)[:8], flush=True)
                    for v in A:
                        cnt[v] = cnt.get(v, 0) + 1
                    k = "quiet differing pairs: |A_i| " + ("0 (!)" if not A else ("1" if len(A) == 1 else "≥ 2")); tot[k] = tot.get(k, 0) + 1
                    if any(cnt[v] >= 2 for v in A):
                        tot["quiet differing pairs re-advancing a vertex (QUIET-LIN FAILS)"] = tot.get("quiet differing pairs re-advancing a vertex (QUIET-LIN FAILS)", 0) + 1
                        if shown < nshow: shown += 1; print("QUIET-LIN FAILS", nm, "depth", key_[0], "|R|", len(R), "pair", i, "re-advanced", sorted(v for v in A if cnt[v] >= 2)[:8], flush=True)
                close()
    print("max #pairs per block advancing one vertex:", mxv); print("max quiet block length / |R|:", mxr)
    for k in sorted(tot): print(f"{tot[k]:7d}  {k}")
