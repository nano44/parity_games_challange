"""L-ALG succ. 8 (produced on Opus 5.5, 2026-10-18 box 10), GAP-A-M §23u gap G23u: which DIFFERING consecutive visit pairs of a
context have NO entry on the fixed §23t grid? Same model as dtl_changenew.py (dtl_rootmono.RM; RM_LIGHT=1 RM_DV=0 suffice; no
RM_PREF needed: the grid is read from rec["rtop"], the per-round map vertex -> top of its region).
Grid (§23t, G10-a1): steps (r, τ) for every round r ≤ |R| + 1 and every p-vertex τ of R; w ∈ P_i(r, τ⁺) iff top_r^i(w) > τ
(⊥ = -1). Round convention: after a res = 1 stop the last round repeats; after a res = -1 (V = ∅) stop, later rounds are ∅.
ENTRY of w at (r, τ) for x → y: top_r^x(w) ≤ τ < top_r^y(w); EXIT: the reverse.
Per differing pair (set-level tattr signatures differ, dtl_changenew.sig_used): has an entry or not; first difference type
  reg      : a region step that is not at the lowest grid top of R,
  reg-low  : a region step at the lowest grid top,
  thr      : a threshold-loop tattr;
the round of the first difference; and the RV comparison (rec["rv"]: drop round per p-vertex, INF if it survives): RV rises
somewhere / falls somewhere / equal.
Printed: counts per (first-difference type, entry?) and per (no-entry, RV pattern); max D_R, max D_R^noent per context; max
exits per (step, vertex) on the grid (the §23t-convention EXIT_c count). Examples of no-entry pairs (DR_SHOW=k, default 5).
Usage: RM_LIGHT=1 RM_DV=0 DTL_ORDER=oink|stable [UNIONS=.. SEED=.. UM_CROSS=.. NMAX=..] dtl_drthr.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import dtl_rootmono as RMM, dtl_step5stats as ST, dtl_changenew as CN
FD = RMM.FD; INF = RMM.INF; VIRT = os.environ.get("DR_VIRT") == "1"   # DR_VIRT=1: also count exits at the virtual end-of-round step (P = U_r)


class DR(RMM.RM):
    def best_vertices(s, V, R, p):
        res = RMM.RM.best_vertices(s, V, R, p); s.allrecs[-1]["p"] = p; return res


def grid_tops(rec, nrounds):
    """list over rounds 1..nrounds of dict w -> top (absent = ⊥), with the §23t round convention."""
    rt = rec.get("rtop", []); out = []
    for r in range(nrounds):
        if r < len(rt): out.append(rt[r])
        elif rec["res"] == 1 and rt: out.append(rt[-1])
        else: out.append({})
    return out


def first_diff(r_, rec, ra, x):
    """(type, round) of the first differing tattr between visit x (log of run row ra) and rec (row r_)."""
    def ents(row, rc):
        return [(i, e) for i, e in enumerate(row["log"][rc["start"]:rc["end"]], rc["start"]) if e[0] in ("bv-reg", "bv-thr")]
    ex, ey = ents(ra, x), ents(r_, rec)
    for k in range(max(len(ex), len(ey))):
        a = ex[k][1][:5] if k < len(ex) else None; b = ey[k][1][:5] if k < len(ey) else None
        if a != b:
            i, e = ey[k] if k < len(ey) else ex[k]; rc = rec if k < len(ey) else x
            for (rnd, a0, a1, end) in rc["spans"]:
                if a0 <= i < end:
                    if e[0] == "bv-thr": return "thr", rnd
                    j = sum(1 for (i2, e2) in (ey if rc is rec else ex) if a0 <= i2 < i and e2[0] == "bv-reg")
                    tops = sorted(set(rc["rtop"][rnd - 1].values()), reverse=True)
                    return ("reg-low" if j < len(tops) and tops[j] == rc["lowgrid"] else "reg"), rnd
            return e[0], -1
    return "none", -1


if __name__ == "__main__":
    sys.setrecursionlimit(100000); tot = {}; shown = 0; nshow = int(os.environ.get("DR_SHOW", "5"))
    mxD = (0, ""); mxN = (0, ""); mxX = (0, ""); mxB = (0, "")
    for f, g in ST.games(sys.argv[1:]):
        d0 = FD.P.X.build(g); d = DR(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx; d.run()
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
                low = grid[0]; nr = len(R) + 1
                for _, rc in vl: rc["lowgrid"] = low
                DRc = 0; NE = 0; exits = {}; blk = 0; mxblk_c = 0
                for (ra, x), (rb, y) in zip(vl, vl[1:]):
                    gx, gy = grid_tops(x, nr), grid_tops(y, nr)
                    has_ent = False; mch = False; vis = False
                    for r in range(nr):
                        for w in set(gx[r]) | set(gy[r]):
                            tx, ty = gx[r].get(w, -1), gy[r].get(w, -1)
                            if tx != ty:
                                mch = True
                                if not ((tx == -1 and ty == low) or (ty == -1 and tx == low)): vis = True
                            if VIRT and tx != -1 and ty == -1: exits[(r, "U", w)] = exits.get((r, "U", w), 0) + 1   # exit from U_r (virtual step ⊥)
                            if ty > tx and any(tx <= t < ty for t in grid): has_ent = True
                            if tx > ty:
                                for t in grid:
                                    if ty <= t < tx: exits[(r, t, w)] = exits.get((r, t, w), 0) + 1
                    km = "grid map change: " + ("none" if not mch else ("visible (an entry or exit)" if vis else "INVISIBLE only (w <-> lowest region)")); tot[km] = tot.get(km, 0) + 1
                    if mch: blk = 0
                    if CN.sig_used(ra, x)[0] == CN.sig_used(rb, y)[0]:
                        if has_ent: tot["IDENTICAL pair WITH an entry (should not happen)"] = tot.get("IDENTICAL pair WITH an entry (should not happen)", 0) + 1
                        continue
                    DRc += 1; typ, rnd = first_diff(rb, y, ra, x)
                    if not mch:
                        # THR-BLOCK: grid maps equal => U_r equal => W_{r,t} = Cl_t(U_r; T) can only grow; psi = [U_r, W_{r,t}...] per round
                        px, py = x["psi"], y["psi"]; L_ = min(len(px), len(py))
                        mono = all(px[i] <= py[i] for i in range(L_)); strict = any(px[i] < py[i] for i in range(L_))
                        kb = f"map-constant differing pairs: W grows {'yes' if mono else 'NO '} strict {'yes' if strict else 'NO '} psi-len {'same' if len(px) == len(py) else 'DIFF'}"; tot[kb] = tot.get(kb, 0) + 1
                        blk += 1; mxblk_c = max(mxblk_c, blk)
                    k = f"differing pairs: first diff {typ:7s} entry {'yes' if has_ent else 'NO '}"; tot[k] = tot.get(k, 0) + 1
                    if not has_ent:
                        NE += 1
                        up = any(y["rv"].get(v, INF) > x["rv"].get(v, INF) for v in grid); dn = any(y["rv"].get(v, INF) < x["rv"].get(v, INF) for v in grid)
                        kr = f"no-entry pairs: RV {'rises' if up else '-----'} {'falls' if dn else '-----'}"; tot[kr] = tot.get(kr, 0) + 1
                        if shown < nshow:
                            shown += 1
                            print("NO-ENTRY", nm, "depth", key_[0], "|R|", len(R), "first diff", typ, "round", rnd, "res", x["res"], y["res"],
                                  "rounds", len(x.get("rtop", [])), len(y.get("rtop", [])), "RV up/down", up, dn, flush=True)
                if mxblk_c > mxB[0]: mxB = (mxblk_c, f"{nm} depth {key_[0]} |R| {len(R)} visits {len(vl)}")
                if DRc > mxD[0]: mxD = (DRc, f"{nm} depth {key_[0]} |R| {len(R)} visits {len(vl)}")
                if NE > mxN[0]: mxN = (NE, f"{nm} depth {key_[0]} |R| {len(R)} visits {len(vl)}")
                if exits and max(exits.values()) > mxX[0]: mxX = (max(exits.values()), f"{nm} depth {key_[0]} |R| {len(R)}")
    print("max differing pairs in one map-constant block:", mxB)
    print("max D_R:", mxD, "; max D_R^noent:", mxN, "; max exits per (step, vertex) on the grid:", mxX)
    for k in sorted(tot): print(f"{tot[k]:7d}  {k}")
