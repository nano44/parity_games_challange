"""L-ALG succ. 6 (produced on Opus 5.5, 2026-10-17 box 7), GAP-A angle (GAP-C §18p): is the ROOT call's pruning vector
pointwise monotone across consecutive searches s → s+1 of a phase? Root call = the first best_vertices call of a search
(depth 0, R = G'). RV(s)[v], for each p-priority vertex v of G', = the round (1, 2, ...) at which the root call drops v,
INF if v survives to a round that returns 1 (in a −1 call every vertex is dropped at some round). Claim (RMONO): RV(s+1) ≥
RV(s) pointwise. Transitions are classified by where the first difference e* of the reduced logs (dtl_fdlcheck.py) lies:
root call (threshold loop / regions, with the round of e*), or later. For a failure, the first vertex whose RV falls and
its rounds are printed. ROOT-SPLIT rows (root-call transitions): does RV fall / move, does DV* (dtl_dvstar.py, T at search start) move,
does either root call have a deficit round (U ≠ Û, dtl_ideal.py). RM_DV=0 skips DV*. RM_ROUNDS=1 also prints the round of e*. DTL_ORDER = oink | stable. Usage: dtl_rootmono.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_fdlcheck as FC, dtl_ideal as I, dtl_dvstar as DS
FD = FC.FD; D = FD.D; INF = 10 ** 9; tab = {}


class RM(FC.CK):
    def search(s, p):
        s.root = None
        G = set(s.G); tl = [(frozenset(v for v, _ in s.tv[i]), tuple(s.tout[i])) for i in range(len(s.tv))
                           if s.tpr[i] != -1 and s.tpr[i] % 2 == p and all(v in G for v, _ in s.tv[i])]
        dv = DS.dvstar(s, G, p, tl) if os.environ.get("RM_DV", "1") == "1" else None
        r = FC.CK.search(s, p); s.trace[-1]["root"] = s.root; s.trace[-1]["dvstar"] = dv; return r

    def best_vertices(s, V, R, p):
        if s.root is not None: return D.DTL.best_vertices(s, V, R, p)
        # dtl_pyref.DTL.best_vertices verbatim, recording the round of each drop and the log span of each round
        rv = {}; spans = []; psi = []; pos = []; s.root = dict(rv=rv, spans=spans, start=len(s.log), psi=psi, pos=pos)
        V.clear(); V.update(v for v in R if s.pr[v] % 2 == p)
        allV = set(V)
        def fin(res, Vlast):
            for v in allV:
                if v not in rv: rv[v] = INF
            s.root["end"] = len(s.log); s.root["res"] = res; return res
        if not V: return fin(0, V)
        rnd = 0
        while True:
            rnd += 1; a0 = len(s.log)
            prevV = set(V)
            tli = [t for t in range(len(s.tv)) if I.alive(s, t, p)]
            if I.actual_union(s, p, V, R, tli)[0] != I.ideal_union(s, p, V, R, tli): s.root["deficit"] = True
            Z = set(); CurR = set(R); regs = []
            for top in range(s.n - 1, -1, -1):
                if top not in V or top in Z: continue
                CurZ = {top}; s.Q = [top]
                s.tattr(p, CurZ, CurR, CurR, s.pr[top], CurR)
                Z |= CurZ; regs.append(frozenset(CurZ))
            a1 = len(s.log); psi.append(frozenset(Z)); pos.append(sum(i * len(c) for i, c in enumerate(regs)))
            cand = [v for v in sorted(V, reverse=True) if not s.attracts(p, v, Z, R)]
            if not cand: spans.append((rnd, a0, a1, len(s.log))); return fin(1, V)
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
                V.clear(); V.update(prevV); return fin(-1, V)


def where(root, k_full):
    """Position k_full in the full (reduced, with extracts) log → class."""
    if root is None or k_full < root["start"] or k_full >= root["end"]: return "after the root call"
    for rnd, a0, a1, a2 in root["spans"]:
        if a0 <= k_full < a1: return f"root regions, round {rnd}"
        if a1 <= k_full < a2: return f"root threshold loop, round {rnd}"
    return "root call (other)"


if __name__ == "__main__":
    sys.setrecursionlimit(100000); st = {"dropped": 0, "kept: differs": 0, "kept: identical but extracts": 0}; shown = 0
    for f in sys.argv[1:]:
        g = pg.read(f); d0 = FD.P.X.build(g); d = RM(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx; d.run()
        for ph in FD.phase_rows(d):
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
                    print("RV != DV* without deficit", os.path.relpath(f), f"p={r['p']}", [(d.idx[v], r["root"]["rv"][v], r["dvstar"].get(v)) for v in dif[:4]], flush=True)
            for a, b in zip(ph, ph[1:]):
                la = [i for i, e in enumerate(a["log"]) if e[0] not in ("extract", "pass")]
                lb = [i for i, e in enumerate(b["log"]) if e[0] not in ("extract", "pass")]
                k = 0
                while k < min(len(la), len(lb)) and a["log"][la[k]][:4] == b["log"][lb[k]][:4]: k += 1
                cls = "no difference" if k == min(len(la), len(lb)) else where(b["root"], lb[k])
                ra, rb = a["root"]["rv"], b["root"]["rv"]
                fall = [v for v in ra if v in rb and rb[v] < ra[v]]
                key = f"{cls}: " + ("RMONO FAILS" if fall else "RMONO holds")
                if cls.startswith("root"):
                    dvm = a["dvstar"] != b["dvstar"]; dfc = a["root"].get("deficit", False) or b["root"].get("deficit", False)
                    rvm = ra != rb
                    if not rvm and not dfc:
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
                    k2 = f"ROOT-SPLIT: RV {'falls' if fall else 'moves' if rvm else 'same'}, DV* {'moves' if dvm else 'same'}, deficit {'yes' if dfc else 'no'}"
                    tab[k2] = tab.get(k2, 0) + 1
                tab[key] = tab.get(key, 0) + 1
                if fall and shown < 6:
                    shown += 1; v = max(fall)
                    print("RMONO FAILS", os.path.relpath(f), f"p={a['p']}", cls, "vertex", d.idx[v], "pr", d.pr[v],
                          "round", ra[v], "->", rb[v], "| falls:", len(fall), flush=True)
    coarse = {}
    for k, v in tab.items():
        c = k if k.startswith(("ROOT-SPLIT", "RV = DV*", "PSI")) else k.split(",")[0].split(":")[0] + ": " + k.split(": ")[-1]; coarse[c] = coarse.get(c, 0) + v
    print({k: coarse[k] for k in sorted(coarse)})
    if os.environ.get("RM_ROUNDS"): print({k: tab[k] for k in sorted(tab)})
