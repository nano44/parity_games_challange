"""L-ALG succ. 7 (produced on Opus 5.5, 2026-10-17 box 8), GAP-A-M §23c: the shrink-vertex analysis with an attraction
forest. Same model and visits as dtl_rootmono.py with RM_EXCL=1 RM_PREF=1 (dtl_rootmono.RM, plus parent recording only).
In every best_vertices REGION step (round, top) each attracted vertex gets one parent: ('v', v) if it was added by
attractVertices while v was popped, ('t', t) if tangle t fired to add it (the chain continues from the popped vertex that triggered t); the top is the root. path(w) = the fired tangles
on w's parent chain to its region's top (a single-parent forest: an opponent vertex is charged to the last successor that
entered Z, not to the escapes that left Gx).
(1) SHRINK: at consecutive visits x → y of a context and a step σ in both, every w ∈ P_x(σ) \\ P_y(σ) is classified:
    A  some tangle of path_x(w) is relevantly stolen at x → y at its own step (met-not-contained at y, fired at x);
    A' some tangle of path_x(w) is met-not-contained at y at its step, not fired there at x (plain steal);
    B  w's region top is no region top at y (left V, or absorbed);
    C  none of these.
(2) DEP-SAFE: for every relevant steal (σ, t) at x → y with stealing vertices W = t ∩ P_y(σ), no tangle of path_y(w),
    w ∈ W, is relevantly stolen at its step at any later visit pair of the context.
Usage: RM_EXCL=1 RM_PREF=1 RM_LIGHT=1 RM_DV=0 DTL_ORDER=oink|stable dtl_shrinkdep.py G.pg ... (games/unions as dtl_step5stats)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import dtl_rootmono as RMM, dtl_step5stats as ST
FD = RMM.FD; D = FD.D


class SD(RMM.RM):
    def _key(s):
        if not getattr(s, "allrecs", None): return None
        rec = s.allrecs[-1]; pf = rec.get("pref")
        if not pf: return None
        k = next(reversed(pf))
        return None if k in rec.get("fired", {}) else (rec, k)

    def attractVertices(s, p, v, R, Z, Gx, maxpr):
        kk = s._key()
        if kk is None: return RMM.RM.attractVertices(s, p, v, R, Z, Gx, maxpr)
        b = set(Z); RMM.RM.attractVertices(s, p, v, R, Z, Gx, maxpr)
        par = kk[0].setdefault("par", {}).setdefault(kk[1], {})
        for u in Z - b: par[u] = ("v", v)

    def attractTangle(s, t, p, R, Z, Gx, maxpr):
        kk = s._key()
        if kk is None: return RMM.RM.attractTangle(s, t, p, R, Z, Gx, maxpr)
        b = set(Z); r = RMM.RM.attractTangle(s, t, p, R, Z, Gx, maxpr)
        par = kk[0].setdefault("par", {}).setdefault(kk[1], {})
        for u in Z - b: par[u] = ("t", t, getattr(s, "_popv", None))
        return r

    def attractTangles(s, p, v, R, Z, Gx, maxpr):
        s._popv = v; return RMM.RM.attractTangles(s, p, v, R, Z, Gx, maxpr)


def region_of(rc, k, w):
    for kk, reg in rc["regset"].items():
        if kk[0] == k[0] and w in reg: return kk
    return None


def path(rc, kk, w):
    par = rc.get("par", {}).get(kk, {}); out = set(); seen = set()
    while w != kk[1] and w in par and w not in seen:
        seen.add(w); e = par[w]
        if e[0] == "t": out.add(e[1]); w = e[2]      # continue from the popped vertex that triggered the tangle
        else: w = e[1]
    return out


def stolen_at(x, y, kk, t, relevant):
    ex, ey, fx = x.get("excl", {}), y.get("excl", {}), x.get("fired", {})
    if kk not in ey or kk not in ex: return False
    if t not in ey[kk] or t in ex[kk] or t >= x["ntv"]: return False
    return (t in fx.get(kk, frozenset())) == relevant


if __name__ == "__main__":
    assert os.environ.get("RM_EXCL") and os.environ.get("RM_PREF"), "set RM_EXCL=1 RM_PREF=1"
    sys.setrecursionlimit(100000); tot = {}; shown = 0
    for f, g in ST.games(sys.argv[1:]):
        d0 = FD.P.X.build(g); d = SD(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx; d.run()
        nm = f if f.startswith(("union", "random")) else os.path.relpath(f); X = d.idx
        if not all(w is not None for w in d.win): print("INCOMPLETE", nm, flush=True)
        for ph in FD.phase_rows(d):
            visits = {}
            for si, r_ in enumerate(ph):
                for rc in r_["recs"]: visits.setdefault(rc["key"], []).append(rc)
            for key_, rcs in visits.items():
                for i in range(len(rcs) - 1):
                    x, y = rcs[i], rcs[i + 1]
                    for k in x.get("pref", {}):
                        if k not in y.get("pref", {}): continue
                        for w in x["pref"][k] - y["pref"][k]:
                            kk = region_of(x, k, w)
                            pt = path(x, kk, w) if kk else set()
                            if kk and any(stolen_at(x, y, kk, t, True) for t in pt): c = "A (path tangle relevantly stolen)"
                            elif kk and any(stolen_at(x, y, kk, t, False) for t in pt): c = "A' (path tangle plainly stolen)"
                            elif kk is None or kk not in y["regset"]: c = "B (region top gone)"
                            else: c = "C (other)"
                            kc = "SHRINK vertex: " + c; tot[kc] = tot.get(kc, 0) + 1
                            if c.startswith("C") and shown < 25:
                                shown += 1
                                print(f"SHRINK C {nm} ctx |R| {len(key_[1])} visits {i}->{i+1} step (r{k[0]}, top {X[k[1]]}) w {X[w]} region top {X[kk[1]]} path {sorted(pt)} parent {x.get('par', {}).get(kk, {}).get(w)}", flush=True)
                    ex, ey, fx = x.get("excl", {}), y.get("excl", {}), x.get("fired", {})
                    for k in ey:
                        if k not in ex: continue
                        for t in ey[k]:
                            if not stolen_at(x, y, k, t, True): continue
                            W = [v for v, _ in d.tv[t] if v in y["pref"].get(k, frozenset())]
                            bad = []
                            for w in W:
                                kk = region_of(y, k, w)
                                for t2 in (path(y, kk, w) if kk else ()):
                                    for j in range(i + 1, len(rcs) - 1):
                                        if stolen_at(rcs[j], rcs[j + 1], kk, t2, True): bad.append((X[w], t2, j))
                            kd = "DEP-SAFE (stealing vertices' path tangles never relevantly stolen later): " + ("FAILS" if bad else "holds"); tot[kd] = tot.get(kd, 0) + 1
                            if bad and shown < 50:
                                shown += 1; print(f"DEP-SAFE FAILS {nm} ctx |R| {len(key_[1])} steal visits {i}->{i+1} step (r{k[0]}, top {X[k[1]]}) t {t}: (w, path tangle, later pair) {bad[:4]}", flush=True)
    for k in sorted(tot): print(f"{tot[k]:7d}  {k}")
