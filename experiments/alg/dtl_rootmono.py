"""L-ALG succ. 6 (produced on Opus 5.5, 2026-10-17 box 7), GAP-A angle (GAP-C §18p): is the ROOT call's pruning vector
pointwise monotone across consecutive searches s → s+1 of a phase? Root call = the first best_vertices call of a search
(depth 0, R = G'). RV(s)[v], for each p-priority vertex v of G', = the round (1, 2, ...) at which the root call drops v,
INF if v survives to a round that returns 1 (in a −1 call every vertex is dropped at some round). Claim (RMONO): RV(s+1) ≥
RV(s) pointwise. Transitions are classified by where the first difference e* of the reduced logs (dtl_fdlcheck.py) lies:
root call (threshold loop / regions, with the round of e*), or later. For a failure, the first vertex whose RV falls and
its rounds are printed. ROOT-SPLIT rows (root-call transitions): does RV fall / move, does DV* (dtl_dvstar.py, T at search start) move,
does either root call have a deficit round (U ≠ Û, dtl_ideal.py). RM_DV=0 skips DV*. Games and env as dtl_step5stats.games (UNIONS, UM_CROSS, SEED, NMAX, RANDOM). RM_EXCL=1 records excluded tangles per region step (PREFIX-MONO-X test). RM_LIGHT=1 skips the ideal and step-deficit checks (deficit/stepdef flags are then never set). RM_ROUNDS=1 also prints the round of e*. DTL_ORDER = oink | stable. Usage: dtl_rootmono.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_fdlcheck as FC, dtl_ideal as I, dtl_dvstar as DS, dtl_step5stats as ST
FD = FC.FD; D = FD.D; INF = 10 ** 9; tab = {}
LIGHT = os.environ.get("RM_LIGHT") == "1"          # skip the ideal / step-deficit checks (for climbs that only count contexts)


class RM(FC.CK):
    def search(s, p):
        s.root = None; s.ctx0 = []; s.d0recs = []; s.allrecs = []
        G = set(s.G); tl = [(frozenset(v for v, _ in s.tv[i]), tuple(s.tout[i])) for i in range(len(s.tv))
                           if s.tpr[i] != -1 and s.tpr[i] % 2 == p and all(v in G for v, _ in s.tv[i])]
        dv = DS.dvstar(s, G, p, tl) if os.environ.get("RM_DV", "1") == "1" else None
        r = FC.CK.search(s, p); s.trace[-1]["root"] = s.root; s.trace[-1]["dvstar"] = dv; s.trace[-1]["ctx0"] = list(s.ctx0); s.trace[-1]["d0clean"] = not any(r_.get("stepdef") for r_ in s.d0recs); s.trace[-1]["recs"] = list(s.allrecs); return r

    def best_vertices(s, V, R, p):
        if s.dep == 0: s.ctx0.append(frozenset(R))
        # dtl_pyref.DTL.best_vertices verbatim, recording the round of each drop and the log span of each round
        rv = {}; spans = []; psi = []; pos = []; rk = []; rec = dict(rv=rv, spans=spans, start=len(s.log), psi=psi, pos=pos, rk=rk, ntv=len(s.tv))
        if s.root is None: s.root = rec
        rec["key"] = (s.dep, frozenset(R)); s.allrecs.append(rec)
        if s.dep == 0: s.d0recs.append(rec)
        V.clear(); V.update(v for v in R if s.pr[v] % 2 == p)
        allV = set(V)
        def fin(res, Vlast):
            for v in allV:
                if v not in rv: rv[v] = INF
            rec["end"] = len(s.log); rec["res"] = res; return res
        if not V: return fin(0, V)
        rnd = 0
        while True:
            rnd += 1; a0 = len(s.log)
            prevV = set(V)
            tli = [t for t in range(len(s.tv)) if I.alive(s, t, p)]
            if not LIGHT and I.actual_union(s, p, V, R, tli)[0] != I.ideal_union(s, p, V, R, tli): rec["deficit"] = True
            Z = set(); CurR = set(R); regs = []; rtops = []
            CurR = set(R)
            for top in range(s.n - 1, -1, -1):
                if top not in V or top in Z: continue
                CurZ = {top}; s.Q = [top]
                if os.environ.get("RM_PREF"): rec.setdefault("pref", {})[(rnd, top)] = frozenset(Z)
                if os.environ.get("RM_EXCL"):
                    rec.setdefault("excl", {})[(rnd, top)] = frozenset(t for t in tli if any(v in Z for v, _ in s.tv[t]) and not all(v in Z for v, _ in s.tv[t]))
                s.tattr(p, CurZ, CurR, CurR, s.pr[top], CurR)
                if os.environ.get("RM_EXCL"): rec.setdefault("fired", {})[(rnd, top)] = frozenset(getattr(s, "used", set()))
                cl = (Z | CurZ) if LIGHT else I.lfp(s, p, Z | {top}, R, s.pr[top], tli)
                if cl != Z | CurZ:
                    miss0 = cl - Z - CurZ
                    rec.setdefault("wits", {})[(rnd, top)] = frozenset(t for t in tli if any(v in Z for v, _ in s.tv[t]) and any(v in miss0 for v, _ in s.tv[t]))
                    rec["stepdef"] = True
                    vt = {v: tp for tp, c in zip(rtops, regs) for v in c}
                    det = rec.setdefault("witdet", {})
                    for t_ in rec["wits"][(rnd, top)]:
                        det[(rnd, top, t_)] = frozenset(vt.get(v) for v, _ in s.tv[t_] if v in Z)
                    if "wit" not in rec:
                        miss = cl - Z - CurZ
                        strad = [t for t in tli if any(v in Z for v, _ in s.tv[t]) and any(v in miss for v, _ in s.tv[t])]
                        rec["wit"] = (rnd, top, frozenset(miss), tuple(strad))
                Z |= CurZ; regs.append(frozenset(CurZ)); rtops.append(top)
            a1 = len(s.log); psi.append(frozenset(Z)); pos.append(sum(i * len(c) for i, c in enumerate(regs)))
            rk.append({v: i for i, c in enumerate(regs) for v in c})
            rec.setdefault("rtop", []).append({v: tp for tp, c in zip(rtops, regs) for v in c})
            # level-wise deficit: the code's union after the tops of priority >= q vs the ideal Û_{>=q} (dtl_ideal.lfp)
            Uh = set()
            for q in ([] if LIGHT else sorted({s.pr[v] for v in V}, reverse=True)):
                Uh = I.lfp(s, p, Uh | {v for v in V if s.pr[v] == q}, R, q, tli)
                Aq = set().union(*[c for tp, c in zip(rtops, regs) if s.pr[tp] >= q])
                if Aq != Uh: rec["leveldef"] = True
            cand = [v for v in sorted(V, reverse=True) if not s.attracts(p, v, Z, R)]
            if not cand:
                # G-d1 / G-Ψ convention (R-P4, R2-P4): a round returning at 716 has no threshold loop; Ψ uses W_{r,t} := Cl_t(U_r)
                W_ = set(Z)
                for t in [0] + [q for q in s.prios if q > 0 and q <= s.maxpr]:
                    W_ = I.lfp(s, p, W_, R, t, tli); psi.append(frozenset(W_))
                spans.append((rnd, a0, a1, len(s.log))); return fin(1, V)
            for t in [0] + [q for q in s.prios if q > 0 and q <= s.maxpr]:
                s.Q = sorted(Z)
                s.tattr(p, Z, R, R, t, None); psi.append(frozenset(Z))
                keep = []
                for i, u in enumerate(cand):
                    if s.pr[u] <= t:
                        keep += cand[i:]; break
                    if not s.attracts(p, u, Z, R): keep.append(u)
                cand = keep
            spans.append((rnd, a0, a1, len(s.log)))
            V -= set(cand)
            if not cand: return fin(1, V)
            for u in cand: rv[u] = rnd                          # dropped at this round (also the last round of a −1 call)
            if not V:
                rec["lastV"] = frozenset(prevV)
                V.clear(); V.update(prevV); return fin(-1, V)


def where(root, k_full):
    """Position k_full in the full (reduced, with extracts) log → class."""
    if root is None or k_full < root["start"] or k_full >= root["end"]: return "after the root call"
    for rnd, a0, a1, a2 in root["spans"]:
        if a0 <= k_full < a1: return f"root regions, round {rnd}"
        if a1 <= k_full < a2: return f"root threshold loop, round {rnd}"
    return "root call (other)"


if __name__ == "__main__":
    phrows = []; badrows = []; seqrows = []; ctxrows = []; fdcrows = []; descrows = []; recrows = []; succrows = []; ifdrows = []; nsrows = []; rsrows = []; firedrows = []
    sys.setrecursionlimit(100000); st = {"dropped": 0, "kept: differs": 0, "kept: identical but extracts": 0}; shown = 0
    for f, g in ST.games(sys.argv[1:]):
        d0 = FD.P.X.build(g); d = RM(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx; d.run()
        for ph in FD.phase_rows(d):
            nd = nr = 0; wl = []; nbad = 0; seq = []; fdc = set(); kseq = []; desc = {}; ifd = set(); victim = {}; vfall = {}; nsteal = {}; rsteal = {}; trip = {}; rtrip = {}
            for r in ph:
                full = r["log"]; red = FC.reduce_log(full, st)
                # map root spans onto the reduced log: the root call precedes every sptl pass, so its positions shift only
                # by the "pass" markers, of which there are none before it
                r["log"] = red
            for r in ph:
                if r["root"] is None or r["dvstar"] is None: continue
                k3 = "RV = DV* on a root call " + ("with" if r["root"].get("deficit") else "without") + " deficit: " + ("yes" if r["root"]["rv"] == r["dvstar"] else "NO")
                tab[k3] = tab.get(k3, 0) + 1
                if r["root"]["rv"] != r["dvstar"] and not r["root"].get("deficit") and shown < 12:
                    shown += 1; dif = [v for v in r["root"]["rv"] if r["root"]["rv"][v] != r["dvstar"].get(v)]
                    print("RV != DV* without deficit", (f if f.startswith(('union', 'random')) else os.path.relpath(f)), f"p={r['p']}", [(d.idx[v], r["root"]["rv"][v], r["dvstar"].get(v)) for v in dif[:4]], flush=True)
            for a, b in zip(ph, ph[1:]):
                la = [i for i, e in enumerate(a["log"]) if e[0] not in ("extract", "pass")]
                lb = [i for i, e in enumerate(b["log"]) if e[0] not in ("extract", "pass")]
                k = 0
                while k < min(len(la), len(lb)) and a["log"][la[k]][:4] == b["log"][lb[k]][:4]: k += 1
                cls = "no difference" if k == min(len(la), len(lb)) else where(b["root"], lb[k])
                seq.append("R" if cls.startswith("root") else "N" if cls == "after the root call" else "=")
                def mmass(r_):
                    c0 = r_["ctx0"]; rr = [x for x in r_["recs"] if x["key"][0] == 0]
                    return sum(len(c0[i_] - (c0[i_ + 1] if i_ + 1 < len(c0) else frozenset())) for i_, x in enumerate(rr) if x.get("res") == -1)
                ma_, mb_ = mmass(a), mmass(b)
                if mb_ > ma_ and cls != "no difference":
                    pos_ = lb[k]; rb3 = next((r_ for r_ in b["recs"] if r_["start"] <= pos_ < r_["end"]), None)
                    if rb3 is None: why = "e* not in a best_vertices call"
                    else:
                        ra3 = next((r_ for r_ in a["recs"] if r_["key"] == rb3["key"]), None)
                        rvch = ra3 is not None and ra3["rv"] != rb3["rv"]
                        why = f"e* in a {'−1' if rb3.get('res') == -1 else 'stable' if rb3.get('res') == 1 else 'other'} call, RV {'changed' if rvch else 'same'}"
                    km = "DISTRACTION MASS rises: " + why; tab[km] = tab.get(km, 0) + 1
                elif cls != "no difference":
                    km = "DISTRACTION MASS " + ("falls" if mb_ < ma_ else "same"); tab[km] = tab.get(km, 0) + 1
                # e* caller (any position) and the weak STR-DET check: does s+1 create a tangle before e*?
                if cls == "no difference":
                    kx = "E* CALLER: no set-level difference at all"
                else:
                    kx = "E* CALLER: " + b["log"][lb[k]][0]
                    e_ = b["log"][lb[k]]; ifd.add((e_[0], e_[1], e_[2], e_[4], e_[7], e_[8]))
                    pre = any(e_[0] == "extract" for e_ in b["log"][:lb[k]])
                    kw = "STR-DET weak (s+1 creates no tangle before e*): " + ("FAILS" if pre else "holds"); tab[kw] = tab.get(kw, 0) + 1
                tab[kx] = tab.get(kx, 0) + 1
                if cls != "no difference":
                    pos_ = lb[k]; rb2 = next((r_ for r_ in b["recs"] if r_["start"] <= pos_ < r_["end"]), None)
                    if rb2 is None: kc = "ANY-CONTEXT e*: not in a best_vertices call (search_rec −1 attractor)"; kseq.append("T")
                    else:
                        ra2 = next((r_ for r_ in a["recs"] if r_["key"] == rb2["key"]), None)
                        if ra2 is None: kc = "ANY-CONTEXT e*: in a call whose context s did not visit (impossible by FDL)"
                        else:
                            fa = [v for v in ra2["rv"] if rb2["rv"].get(v, INF) < ra2["rv"][v]]
                            if fa: kc = "ANY-CONTEXT e*: RV falls"
                            elif ra2["rv"] != rb2["rv"]: kc = "ANY-CONTEXT e*: Π rises (RV)"
                            else:
                                qa, qb = ra2["psi"], rb2["psi"]
                                if not (len(qa) == len(qb) and all(x <= y for x, y in zip(qa, qb))):
                                    kc = "ANY-CONTEXT e*: Ψ NOT monotone"
                                    print("G-F1 CASE (Ψ not monotone at e*)", f, f"p={a['p']}", "depth", rb2["key"][0], "|R|", len(rb2["key"][1]), "rounds", len(qa), len(qb), "dirty" if rb2.get("stepdef") else "clean", flush=True)
                                elif qa != qb: kc = "ANY-CONTEXT e*: Π rises (Ψ)"
                                else:
                                    fa_ = sum(d.n - t_ for m in ra2.get("rtop", []) for t_ in m.values()); fb_ = sum(d.n - t_ for m in rb2.get("rtop", []) for t_ in m.values())
                                    kc = "ANY-CONTEXT e*: Π rises (Φ_top)" if fb_ < fa_ else "ANY-CONTEXT e*: Π DOES NOT RISE"
                            kc += " | depth " + ("0" if rb2["key"][0] == 0 else ">0") + (" | later call dirty" if rb2.get("stepdef") else " | later call clean")
                            fdc.add(rb2["key"])
                            # depth-0 position of the first-difference call: index of the last depth-0 call at or before it
                            d0pos = max(i_ for i_, r_ in enumerate(b["recs"]) if r_["start"] <= rb2["start"] and r_["key"][0] == 0)
                            d0i = sum(1 for r_ in b["recs"][:d0pos + 1] if r_["key"][0] == 0)
                            kseq.append(f"{d0i}" + ("" if rb2["key"][0] == 0 else "+"))
                    tab[kc] = tab.get(kc, 0) + 1
                pa_ = {v: sum(v in c for c in a["ctx0"]) for v in a["G"]}; pb_ = {v: sum(v in c for c in b["ctx0"]) for v in b["G"]}
                mv = any(pb_[v] > pa_[v] for v in pa_)
                kab = f"ABS-pw (no vertex to a later depth-0 piece), later search {'CLEAN at depth 0' if b['d0clean'] else 'dirty at depth 0'}: " + ("FAILS" if mv else "holds")
                tab[kab] = tab.get(kab, 0) + 1
                if mv and b["d0clean"] and shown < 12:
                    shown += 1; mvs = [v for v in pa_ if pb_[v] > pa_[v]]
                    ra0 = [r_ for r_ in a["recs"] if r_["key"][0] == 0]; rb0 = [r_ for r_ in b["recs"] if r_["key"][0] == 0]
                    print("ABS-pw FAILS on a clean search", (f if f.startswith(('union', 'random')) else os.path.relpath(f)), f"p={a['p']}", "e*:", cls,
                          "| moved (vertex, piece s -> s+1):", [(d.idx[v], pa_[v], pb_[v]) for v in mvs[:5]],
                          "| depth-0 results s:", [r_.get("res") for r_ in ra0], "s+1:", [r_.get("res") for r_ in rb0],
                          "| root prevV s:", sorted(d.idx[v] for v in ra0[0].get("lastV", [])), "s+1:", sorted(d.idx[v] for v in rb0[0].get("lastV", [])),
                          "| piece-1 removal s:", sorted(d.idx[v] for v in a["ctx0"][0] - (a["ctx0"][1] if len(a["ctx0"]) > 1 else frozenset())),
                          "s+1:", sorted(d.idx[v] for v in b["ctx0"][0] - (b["ctx0"][1] if len(b["ctx0"]) > 1 else frozenset())), flush=True)
                if cls == "after the root call":
                    e_ = b["log"][lb[k]]; kd = f"after-root e*: caller {e_[0]}, depth {e_[1]}"; tab[kd] = tab.get(kd, 0) + 1
                ra, rb = a["root"]["rv"], b["root"]["rv"]
                fall = [v for v in ra if v in rb and rb[v] < ra[v]]
                key = f"{cls}: " + ("RMONO FAILS" if fall else "RMONO holds")
                if cls.startswith("root"):
                    dvm = a["dvstar"] != b["dvstar"]; dfc = a["root"].get("deficit", False) or b["root"].get("deficit", False)
                    rvm = ra != rb
                    if not rvm and not dfc:
                        lv = a["root"].get("leveldef") or b["root"].get("leveldef")
                        k5 = "LEVEL-DEF in a deficit-free same-RV transition: " + ("yes" if lv else "no"); tab[k5] = tab.get(k5, 0) + 1
                        later = any(v in rb_ and v in ra_ and rb_[v] > ra_[v] for ra_, rb_ in zip(a["root"]["rk"], b["root"]["rk"]) for v in ra_)
                        k6 = "NO-LATER (deficit-free, same RV): " + ("FAILS" if later else "holds"); tab[k6] = tab.get(k6, 0) + 1
                        pa, pb = a["root"]["psi"], b["root"]["psi"]
                        ok = len(pa) == len(pb) and all(x <= y for x, y in zip(pa, pb))
                        strict = ok and any(x != y for x, y in zip(pa, pb))
                        k4 = "PSI (RV same, no deficit): " + ("grows strictly" if strict else "equal" if ok else "NOT monotone")
                        if ok and not strict:
                            qa, qb = a["root"]["pos"], b["root"]["pos"]
                            k4 += " | e* in " + cls.split(",")[0] + " | PHIpos " + ("falls strictly" if sum(qb) < sum(qa) else "equal" if sum(qb) == sum(qa) else "RISES")
                        elif strict:
                            qa, qb = a["root"]["pos"], b["root"]["pos"]
                            if len(qa) == len(qb): k4 += " | PHIpos " + ("falls" if sum(qb) < sum(qa) else "equal" if sum(qb) == sum(qa) else "rises")
                        tab[k4] = tab.get(k4, 0) + 1
                    sda = a["root"].get("stepdef", False); sdb = b["root"].get("stepdef", False)
                    k7 = f"STEP-DEF (root, either side): {'yes' if sda or sdb else 'no'}; final deficit: {'yes' if dfc else 'no'}"; tab[k7] = tab.get(k7, 0) + 1
                    if not rvm and not (sda or sdb):
                        later = any(v in rb_ and v in ra_ and rb_[v] > ra_[v] for ra_, rb_ in zip(a["root"]["rk"], b["root"]["rk"]) for v in ra_)
                        k8 = "NO-LATER (step-deficit-free, same RV): " + ("FAILS" if later else "holds"); tab[k8] = tab.get(k8, 0) + 1
                    wa = a["root"].get("wits", {}); wb = b["root"].get("wits", {})
                    # NEWX: at some region step (round, top) of s+1, a tangle of T_s (id < k0 of s) is excluded and fires in the
                    # closure, but was not so at the same step of s
                    newx = any(t < a["k0"] and t not in wa.get(k_, frozenset()) for k_ in wb for t in wb[k_])
                    if sdb:
                        bad2 = []
                        if fall: bad2.append("RV falls")
                        if not rvm:
                            pa, pb = a["root"]["psi"], b["root"]["psi"]
                            okp = len(pa) == len(pb) and all(x <= y for x, y in zip(pa, pb))
                            if not okp: bad2.append("PSI not monotone")
                        k10 = ("DIRTY with NEWX: " if newx else "DIRTY without NEWX: ") + ("predictions hold" if not bad2 else "FAILS " + "+".join(bad2)); tab[k10] = tab.get(k10, 0) + 1
                    # PI-RISE: (RV pointwise up, then Ψ ⊆ up, then Φ_top down), strictly, at this root-e* transition?
                    def phit(r_): return sum(d.n - t_ for m in r_["root"]["rtop"] for t_ in m.values())
                    if fall: pir = "RV falls"
                    elif rvm: pir = "rises (RV)"
                    else:
                        pa, pb = a["root"]["psi"], b["root"]["psi"]
                        if not (len(pa) == len(pb) and all(x <= y for x, y in zip(pa, pb))): pir = "Ψ NOT monotone"
                        elif pa != pb: pir = "rises (Ψ)"
                        elif phit(b) < phit(a): pir = "rises (Φ_top)"
                        else: pir = "DOES NOT RISE"
                    kp = "PI at root-e* transitions: " + pir; tab[kp] = tab.get(kp, 0) + 1
                    if pir in ("RV falls", "Ψ NOT monotone", "DOES NOT RISE"): nbad += 1
                    if not sdb:                                    # CLEAN: the later root call has no step deficit
                        bad = []
                        if fall: bad.append("RV falls")
                        if not rvm:
                            pa, pb = a["root"]["psi"], b["root"]["psi"]
                            okp = len(pa) == len(pb) and all(x <= y for x, y in zip(pa, pb))
                            if not okp: bad.append("PSI not monotone")
                            elif pa == pb:
                                fa = sum(s_.n - t_ for m in a["root"]["rtop"] for t_ in m.values() for s_ in [d])
                                fb = sum(d.n - t_ for m in b["root"]["rtop"] for t_ in m.values())
                                if not fb < fa: bad.append("PHItop does not fall")
                            lt = any(v in mb and mb[v] < ma[v] for ma, mb in zip(a["root"]["rtop"], b["root"]["rtop"]) for v in ma)
                            if lt: bad.append("a vertex moves to a lower-index top")
                        k9 = "CLEAN root transition: " + ("ALL HOLD" if not bad else "FAILS " + "+".join(bad)); tab[k9] = tab.get(k9, 0) + 1
                    else:
                        tab["DIRTY root transition (later root call has a step deficit)"] = tab.get("DIRTY root transition (later root call has a step deficit)", 0) + 1
                        nd += 1
                        w = b["root"]["wit"]; wl.append(w)
                    nr += 1
                    k2 = f"ROOT-SPLIT: RV {'falls' if fall else 'moves' if rvm else 'same'}, DV* {'moves' if dvm else 'same'}, deficit {'yes' if dfc else 'no'}"
                    tab[k2] = tab.get(k2, 0) + 1
                tab[key] = tab.get(key, 0) + 1
                if fall and shown < 6:
                    shown += 1; v = max(fall)
                    print("RMONO FAILS", (f if f.startswith(('union', 'random')) else os.path.relpath(f)), f"p={a['p']}", cls, "vertex", d.idx[v], "pr", d.pr[v],
                          "round", ra[v], "->", rb[v], "| falls:", len(fall), flush=True)
            if wl:
                tops_ = [w[1] for w in wl]; tg = [w[3] for w in wl]
                kt = "DIRTY witness top repeats within the phase: " + ("yes" if len(set(tops_)) < len(tops_) else "no"); tab[kt] = tab.get(kt, 0) + 1
                kg = "DIRTY witness tangle set repeats within the phase: " + ("yes" if len(set(tg)) < len(tg) else "no"); tab[kg] = tab.get(kg, 0) + 1
                ke = "DIRTY witness has a straddling tangle: " + ("all" if all(tg) else "NOT all"); tab[ke] = tab.get(ke, 0) + 1
                if os.environ.get("RM_WIT") and len(wl) >= 8:
                    print("WITNESSES", (f if f.startswith(('union', 'random')) else os.path.relpath(f)), [(w[0], d.idx[w[1]], len(w[2]), w[3]) for w in wl], flush=True)
            if len(ph) > 1:
                allc = set(c for r_ in ph for c in r_["ctx0"]); pos = max(len(r_["ctx0"]) for r_ in ph)
                ctxrows.append(((f if f.startswith(('union', 'random')) else os.path.relpath(f)), len(allc), len(ph), pos, len(ph[0]["G"])))
            # Π_R along the phase: compare consecutive visits of every context (any depth); count descents / incomparables
            visits = {}
            for si, r_ in enumerate(ph):
                for rc in r_["recs"]: visits.setdefault(rc["key"], []).append((si, rc))
            for key_, vl in visits.items():
                for (s1, x), (s2, y) in zip(vl, vl[1:]):
                    fa = [v for v in x["rv"] if y["rv"].get(v, INF) < x["rv"][v]]
                    for v in fa: vfall[(key_, v)] = vfall.get((key_, v), 0) + 1
                    if fa and os.environ.get("RM_FALLDET"):
                        print("FALLING VERTICES", (f if f.startswith(('union', 'random')) else os.path.relpath(f)), "ctx |R|", len(key_[1]), "visits", s1, "->", s2,
                              [(d.idx[v], x["rv"][v], y["rv"].get(v)) for v in sorted(fa)][:12], flush=True)
                    if fa: c_ = "RV falls"
                    elif x["rv"] != y["rv"]: c_ = "rises (RV)"
                    else:
                        qa, qb = x["psi"], y["psi"]
                        if not (len(qa) == len(qb) and all(u <= w for u, w in zip(qa, qb))): c_ = "Ψ NOT monotone"
                        elif qa != qb: c_ = "rises (Ψ)"
                        else:
                            fa_ = sum(d.n - t_ for m in x.get("rtop", []) for t_ in m.values()); fb_ = sum(d.n - t_ for m in y.get("rtop", []) for t_ in m.values())
                            c_ = "rises (Φ_top)" if fb_ < fa_ else "equal" if fb_ == fa_ else "Φ_top RISES (descent)"
                    kv = "VISITS of a context (consecutive): " + c_ + (" | later call dirty" if y.get("stepdef") else ""); tab[kv] = tab.get(kv, 0) + 1
                    if os.environ.get("RM_EXCL"):
                        ex_, ey_ = x.get("excl", {}), y.get("excl", {})
                        newst = any(t < x["ntv"] and t not in ex_.get(k_, frozenset()) for k_ in ey_ if k_ in ex_ for t in ey_[k_])
                        kns = "PREFIX-MONO-X: " + ("new steal" if newst else "no new steal") + " | " + ("DESCENT" if c_ in ("RV falls", "Ψ NOT monotone", "Φ_top RISES (descent)") else "no descent")
                        if newst: nsteal[key_] = nsteal.get(key_, 0) + 1
                        fx_ = x.get("fired", {})
                        relst = any(t < x["ntv"] and t not in ex_.get(k_, frozenset()) and t in fx_.get(k_, frozenset()) for k_ in ey_ if k_ in ex_ for t in ey_[k_])
                        kre = "PREFIX-MONO-X*: " + ("relevant new steal" if relst else "no relevant new steal") + " | " + ("DESCENT" if c_ in ("RV falls", "Ψ NOT monotone", "Φ_top RISES (descent)") else "no descent")
                        tab[kre] = tab.get(kre, 0) + 1
                        if relst: rsteal[key_] = rsteal.get(key_, 0) + 1
                        for k_ in ey_:
                            if k_ not in ex_: continue
                            for t in ey_[k_]:
                                if t < x["ntv"] and t not in ex_[k_]:
                                    trip[(key_, k_[0], k_[1], t)] = trip.get((key_, k_[0], k_[1], t), 0) + 1
                                    if t in fx_.get(k_, frozenset()): rtrip[(key_, k_[0], k_[1], t)] = rtrip.get((key_, k_[0], k_[1], t), 0) + 1
                        tab[kns] = tab.get(kns, 0) + 1
                    if c_ in ("RV falls", "Ψ NOT monotone", "Φ_top RISES (descent)"):
                        desc[key_] = desc.get(key_, 0) + 1
                        wids = set().union(*y.get("wits", {}).values()) if y.get("wits") else set()
                        k1, k2 = ph[s1]["k0"], ph[s2]["k0"]
                        new_ = {t for t in wids if t >= k1}
                        for t in wids: victim[(key_, t)] = victim.get((key_, t), 0) + 1
                        if os.environ.get("RM_FALLDET"):
                            print("FALL DETAIL", (f if f.startswith(('union', 'random')) else os.path.relpath(f)), "ctx |R|", len(key_[1]), "depth", key_[0], "visits", s1, "->", s2,
                                  "| (round, failing top, victim) -> stealing region tops:",
                                  sorted((r_, d.idx[tp_], t_, sorted(d.idx[x] for x in st_)) for (r_, tp_, t_), st_ in y.get("witdet", {}).items())[:6], flush=True)
                        kf = "FALL witness straddling tangle: " + ("none recorded" if not wids else "some created since the previous visit" if new_ else "ALL older than the previous visit")
                        tab[kf] = tab.get(kf, 0) + 1
                        if not new_ and wids and shown < 30:
                            shown += 1; print("FALL with only old witnesses", (f if f.startswith(('union', 'random')) else os.path.relpath(f)), "visits", s1, s2, "witnesses", sorted(wids), "k0", k1, k2, flush=True)
            # recurrence: a context visited in search i, absent in some search j > i, visited again in a later search
            rec_n = 0
            for key_, vl in visits.items():
                ids = [si for si, _ in vl]
                rec_n += sum(1 for u, w in zip(ids, ids[1:]) if w > u + 1)
            if len(ph) > 1:
                kr = "CONTEXT RECURRENCES in a phase: " + ("none" if rec_n == 0 else "some"); tab[kr] = tab.get(kr, 0) + 1
                recrows.append(((f if f.startswith(('union', 'random')) else os.path.relpath(f)), rec_n, len(visits), len(ph) - 1, len(ph[0]["G"])))
            succ_ = {}
            for r_ in ph:
                c0 = r_["ctx0"]
                for u, w in zip(c0, c0[1:]): succ_.setdefault(u, set()).add(w)
            if succ_:
                ms = max(len(v_) for v_ in succ_.values()); succrows.append(((f if f.startswith(('union', 'random')) else os.path.relpath(f)), ms, len(succ_), len(ph) - 1, len(ph[0]["G"])))
            if os.environ.get("RM_EXCL"):
                if os.environ.get("RM_PREF"):
                    for key_, vl in visits.items():
                        rcs = [rc for _, rc in vl]
                        for x, y in zip(rcs, rcs[1:]):
                            px, py = x.get("pref", {}), y.get("pref", {})
                            shr = [k_ for k_ in px if k_ in py and not px[k_] <= py[k_]]
                            stolen_lost = False
                            kp = "PREFIX between consecutive visits: " + ("SHRINKS at some step" if shr else "never shrinks")
                            tab[kp] = tab.get(kp, 0) + 1
                # NO-REFIRE: after a relevant steal of (step, t) at visit pair (i, i+1), does t fire again at that step later?
                for key_, vl in visits.items():
                    rcs = [rc for _, rc in vl]
                    for i in range(len(rcs) - 1):
                        x, y = rcs[i], rcs[i + 1]
                        ex_, ey_, fx_ = x.get("excl", {}), y.get("excl", {}), x.get("fired", {})
                        for k_ in ey_:
                            if k_ not in ex_: continue
                            for t in ey_[k_]:
                                if t < x["ntv"] and t not in ex_[k_] and t in fx_.get(k_, frozenset()):
                                    later = rcs[i + 1:]
                                    refire = any(t in z.get("fired", {}).get(k_, frozenset()) for z in later)
                                    unmet = any(k_ in z.get("excl", {}) and t not in z["excl"][k_] for z in later)
                                    kq = "NO-REFIRE after a relevant steal: " + ("REFIRES later" if refire else "never refires") + (" | prefix later unmeets t" if unmet else " | stays met (or step absent)")
                                    tab[kq] = tab.get(kq, 0) + 1
                                    if refire and shown < 40:
                                        shown += 1; print("REFIRE", (f if f.startswith(('union', 'random')) else os.path.relpath(f)), "ctx |R|", len(key_[1]), "step", k_, "tangle", t, "visit", i, flush=True)
                for key_, vl in visits.items():
                    fired_all = set().union(*[set().union(*rc.get("fired", {}).values()) for _, rc in vl]) if vl else set()
                    if len(vl) >= 2: firedrows.append(((f if f.startswith(('union', 'random')) else os.path.relpath(f)), len(fired_all), len(key_[1]), len(vl), len(ph) - 1))
            if trip:
                kt3 = f"NEW STEALS per (context, round, top, tangle): max {max(trip.values())}"; tab[kt3] = tab.get(kt3, 0) + 1
            if rtrip:
                kt4 = f"RELEVANT STEALS per (context, round, top, tangle): max {max(rtrip.values())}"; tab[kt4] = tab.get(kt4, 0) + 1
            if rsteal: rsrows.append(((f if f.startswith(('union', 'random')) else os.path.relpath(f)), max(rsteal.values()), sum(rsteal.values()), len(ph) - 1, len(ph[0]["G"])))
            if nsteal: nsrows.append(((f if f.startswith(('union', 'random')) else os.path.relpath(f)), max(nsteal.values()), sum(nsteal.values()), len(ph) - 1, len(ph[0]["G"])))
            if vfall:
                mvf = max(vfall.values()); kvf = f"FALLS per (context, vertex): max {mvf}"; tab[kvf] = tab.get(kvf, 0) + 1
                # shape of RV sequences of vertices that fall somewhere: what happens after the fall?
                for (key_, v), _ in vfall.items():
                    seqv = [rc["rv"].get(v) for _, rc in visits[key_] if v in rc["rv"]]
                    i0 = next(i for i in range(1, len(seqv)) if seqv[i] < seqv[i - 1])
                    after = seqv[i0:]
                    shp = "constant after the fall" if all(x == after[0] for x in after) else ("rises after the fall" if any(after[j] > after[j - 1] for j in range(1, len(after))) else "falls again")
                    before = seqv[:i0]
                    shb = "non-decreasing before" if all(before[j] >= before[j - 1] for j in range(1, len(before))) else "not monotone before"
                    ksh = f"RV SHAPE of a falling vertex: {shb}, {shp}"; tab[ksh] = tab.get(ksh, 0) + 1
            if victim:
                mv_ = max(victim.values()); kvv = f"FALLS per (context, victim tangle): max {mv_}"; tab[kvv] = tab.get(kvv, 0) + 1
            if desc: descrows.append(((f if f.startswith(('union', 'random')) else os.path.relpath(f)), max(desc.values()), sum(desc.values()), len(ph) - 1, len(ph[0]["G"])))
            if len(ph) > 1: ifdrows.append(((f if f.startswith(('union', 'random')) else os.path.relpath(f)), len(ifd), len(ph) - 1, len(ph[0]["G"])))
            for dep_ in (0, 1):
                cs = [c for (dd, c) in fdc if (dd == 0) == (dep_ == 0)]
                if len(cs) >= 2:
                    chain = all(a_ <= b_ or b_ <= a_ for a_ in cs for b_ in cs)
                    kch = f"CHAIN of first-difference contexts at depth {'0' if dep_ == 0 else '>0'}: " + ("holds" if chain else "FAILS"); tab[kch] = tab.get(kch, 0) + 1
                    if not chain and dep_ == 0 and shown < 20:
                        shown += 1; print("CHAIN FAILS", (f if f.startswith(('union', 'random')) else os.path.relpath(f)), "contexts (sizes):", sorted(len(c) for c in cs), flush=True)
            if fdc:
                nroot = sum(1 for x in kseq if x == "1")
                kr2 = "CTX-ROOT (distinct first-difference contexts ≤ 1 + #root transitions): " + ("holds" if len(fdc) <= 1 + nroot else "FAILS")
                tab[kr2] = tab.get(kr2, 0) + 1
                if len(fdc) > 1 + nroot and shown < 40:
                    shown += 1; print("CTX-ROOT FAILS", (f if f.startswith(('union', 'random')) else os.path.relpath(f)), "contexts", len(fdc), "root transitions", nroot, "kseq", " ".join(kseq), flush=True)
            if fdc: fdcrows.append(((f if f.startswith(('union', 'random')) else os.path.relpath(f)), len(fdc), len(ph) - 1, len(ph[0]["G"]), " ".join(kseq)))
            if seq:
                runs = [len(x) for x in "".join(seq).replace("=", "R").split("R") if x]
                mr = max(runs) if runs else 0; seqrows.append(((f if f.startswith(('union', 'random')) else os.path.relpath(f)), mr, "".join(seq), len(ph[0]["G"])))
            if nbad: badrows.append(((f if f.startswith(('union', 'random')) else os.path.relpath(f)), nbad, len(ph) - 1, len(ph[0]["G"])))
            if len(ph) > 1 and nd: phrows.append(((f if f.startswith(('union', 'random')) else os.path.relpath(f)), nd, nr, len(ph) - 1, len(ph[0]["G"]) if "G" in ph[0] else d.n))
    if phrows:
        phrows.sort(key=lambda r: -r[1])
        print("phases with dirty root transitions (file, dirty, root transitions, transitions, |G'|):", phrows[:8])
        print("phases with a dirty root transition:", len(phrows), "max dirty per phase:", max(r[1] for r in phrows), "max dirty/|G'|:", round(max(r[1] / r[4] for r in phrows), 3))
    if firedrows:
        firedrows.sort(key=lambda r: -r[1] / max(1, r[2])); print("distinct tangles fired at a context over a phase (file, tangles, |R|, visits, transitions):", firedrows[:8])
        print("max tangles/|R|:", round(max(r[1] / max(1, r[2]) for r in firedrows), 2), "max tangles/visits:", round(max(r[1] / r[3] for r in firedrows), 2), "max tangles:", max(r[1] for r in firedrows))
    if rsrows:
        rsrows.sort(key=lambda r: -r[1]); print("RELEVANT new-steal visits per context (file, max per context, total, transitions, |G'|):", rsrows[:10])
    if nsrows:
        nsrows.sort(key=lambda r: -r[1]); print("new-steal visits per context (file, max per context, total, transitions, |G'|):", nsrows[:10])
    if ifdrows:
        ifdrows.sort(key=lambda r: -r[1]); print("distinct first-difference tattr inputs per phase (file, inputs, transitions, |G'|):", ifdrows[:8])
        print("max inputs/transitions:", round(max(r[1] / max(1, r[2]) for r in ifdrows), 3), "max inputs/|G'|:", round(max(r[1] / r[3] for r in ifdrows), 3))
    if succrows:
        succrows.sort(key=lambda r: -r[1]); print("distinct successor contexts of a depth-0 context (file, max successors, depth-0 contexts, transitions, |G'|):", succrows[:8])
    if recrows:
        recrows.sort(key=lambda r: -r[2]); print("contexts per phase, all depths (file, recurrences, distinct contexts, transitions, |G'|):", recrows[:8])
        print("total recurrences:", sum(r[1] for r in recrows), "max distinct contexts/|G'|:", round(max(r[2] / r[4] for r in recrows), 2), "max distinct contexts/(transitions+1):", round(max(r[2] / (r[3] + 1) for r in recrows), 2))
    if descrows:
        descrows.sort(key=lambda r: -r[1]); print("descents of Π_R per context (file, max per context, total, transitions, |G'|):", descrows[:8], "phases:", len(descrows))
    if fdcrows:
        fdcrows.sort(key=lambda r: -r[1]); print("distinct first-difference contexts per phase (file, contexts, transitions, |G'|):", [r[:4] for r in fdcrows[:8]], "max contexts/|G'|:", round(max(r[1] / r[3] for r in fdcrows), 3))
        if os.environ.get("RM_KSEQ"):
            for r in sorted(fdcrows, key=lambda r: -r[2])[:10]: print("KSEQ", r[0], "transitions", r[2], "|G'|", r[3], ":", r[4])
    if ctxrows:
        ctxrows.sort(key=lambda r: -r[1] / r[4])
        print("distinct depth-0 contexts per phase (file, contexts, searches, max depth-0 calls per search, |G'|):", ctxrows[:8])
        print("max contexts/|G'|:", round(max(r[1] / r[4] for r in ctxrows), 3), "max contexts/searches:", round(max(r[1] / r[2] for r in ctxrows), 3), "max contexts:", max(r[1] for r in ctxrows))
    if seqrows:
        seqrows.sort(key=lambda r: -r[1]); print("longest runs of after-root transitions (file, run, sequence R/N, |G'|):", [(a_, b_, c_[:60], d_) for a_, b_, c_, d_ in seqrows[:8]])
    if badrows:
        badrows.sort(key=lambda r: -r[1]); print("phases where PI fails to rise (file, failures, transitions, |G'|):", badrows[:8], "phases:", len(badrows))
    coarse = {}
    for k, v in tab.items():
        c = k if k.startswith(("ROOT-SPLIT", "RV = DV*", "PSI", "LEVEL-DEF", "NO-LATER", "STEP-DEF", "CLEAN", "DIRTY", "PI at", "after-root e*", "ABS-pw", "ANY-CONTEXT", "VISITS", "CONTEXT RECURRENCES", "E* CALLER", "STR-DET", "CHAIN", "FALL witness", "FALLS per", "CTX-ROOT", "DISTRACTION", "RV SHAPE", "PREFIX-MONO-X", "NEW STEALS per", "RELEVANT STEALS per", "NO-REFIRE", "PREFIX between")) else k.split(",")[0].split(":")[0] + ": " + k.split(": ")[-1]; coarse[c] = coarse.get(c, 0) + v
    print({k: coarse[k] for k in sorted(coarse)})
    if os.environ.get("RM_ROUNDS"): print({k: tab[k] for k in sorted(tab)})
