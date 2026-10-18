"""L-ALG succ. 8 (produced on Opus 5.5, 2026-10-18 box 10), GAP-A-M §24b: split the consecutive visit pairs of a context into
QUIET (no grid entry/exit, §23w), ENTRY-ONLY (entries, no exit), USHRINK (some vertex leaves some U_r; by Lemma DEF-SHRINK the
later visit has a deficit round) and RECUT (a grid exit but no U_r shrinks). Grid incl. the virtual end-of-round step as in
dtl_drthr DR_VIRT. Per context: D_R, #DEF_R (visits after the first with rec["deficit"]), #USHRINK, #RECUT, #ENTRY-ONLY.
Printed: totals; max D_R / (1 + #USHRINK + #RECUT); max #DEF_R, #USHRINK, #RECUT per context; checks USHRINK ⇒ deficit in y.
Needs RM_LIGHT unset (ideal checks). Usage: RM_DV=0 DTL_ORDER=oink|stable [UNIONS=..] dtl_defsplit.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import dtl_drthr as DT, dtl_changenew as CN, dtl_step5stats as ST
FD = DT.FD

if __name__ == "__main__":
    sys.setrecursionlimit(100000); tot = {}; mx = {}
    def upd(k, v, ctx):
        if v > mx.get(k, (-1, ""))[0]: mx[k] = (v, ctx)
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
                nr = len(R) + 1; gs = [DT.grid_tops(rc, nr) for _, rc in vl]; c = dict(D=0, US=0, RC=0, EO=0, Q=0)
                for i in range(len(vl) - 1):
                    (ra, x), (rb, y) = vl[i], vl[i + 1]; gx, gy = gs[i], gs[i + 1]
                    if CN.sig_used(ra, x)[0] != CN.sig_used(rb, y)[0]: c["D"] += 1
                    ent = ex = ush = False
                    for r in range(nr):
                        for w in set(gx[r]) | set(gy[r]):
                            tx, ty = gx[r].get(w, -1), gy[r].get(w, -1)
                            if ty > tx and (tx != -1 or any(t < ty for t in grid) or True): ent = True     # incl. virtual step: ⊥ → any region is an entry
                            if tx > ty:
                                ex = True
                                if ty == -1: ush = True
                    if ush:
                        c["US"] += 1
                        r1 = min(r for r in range(nr) if any(w not in gy[r] for w in gx[r]))
                        Vx = {v for v in grid if x["rv"].get(v, 0) >= r1 + 1}; Vy = {v for v in grid if y["rv"].get(v, 0) >= r1 + 1}
                        kv = "USHRINK pairs, first shrinking round input: " + ("V_r EQUAL (U-MONO_DTL FAILS)" if Vx == Vy else ("V_r(x) ⊊ V_r(y)" if Vx < Vy else "V_r(x) ⊄ V_r(y) (EXIT-ORIGIN (a) FAILS?)")); tot[kv] = tot.get(kv, 0) + 1
                        if Vx == Vy and tot[kv] <= 3: print("U-MONO_DTL FAILS", nm, "depth", key_[0], "|R|", len(R), "pair", i, "round", r1 + 1, flush=True)
                        k = "USHRINK pairs: deficit in y " + ("yes" if y.get("deficit") else "NO (DEF-SHRINK FAILS)"); tot[k] = tot.get(k, 0) + 1
                    elif ex: c["RC"] += 1
                    elif ent: c["EO"] += 1
                    else: c["Q"] += 1
                ndef = sum(1 for _, rc in vl[1:] if rc.get("deficit"))
                ctx = f"{nm} depth {key_[0]} |R| {len(R)} visits {len(vl)} D {c['D']} US {c['US']} RC {c['RC']} EO {c['EO']} DEFvisits {ndef}"
                for k_ in ("D", "US", "RC", "EO"): tot["sum " + k_] = tot.get("sum " + k_, 0) + c[k_]; upd("max " + k_, c[k_], ctx)
                upd("max DEF visits", ndef, ctx); upd("max D/(1+US+RC)", round(c["D"] / (1 + c["US"] + c["RC"]), 2), ctx)
    for k in sorted(mx): print(k, mx[k])
    for k in sorted(tot): print(f"{tot[k]:7d}  {k}")
