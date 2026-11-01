#!/usr/bin/env python3
r"""REFEREE-2 successor 25 (Opus 5.5, D15): own check of P-N5-ANCHOR (docs/new/P-N5-ANCHOR-box134.md @ l-new f009a9a1, sha1 ad97ad88).
Engine: my DC.Runner / Engine / dual / pval (R2-N5-FRAME via R2-N5-LATEP); starts via R2-N5-WRUN read_start (validated). Lane box130-134
scripts are NOT imported. Checks (each must be 0):
  RULE   at EVERY non-fallback S4a transition j-1 -> j (Is_(j-1) nonempty), every Even x not its own W'-cycle node (W' := (sigma_j, tau_(j-1))
         valuation): sigma_j(x) = kappa-least element of TIE (fully W'-optimal options in H_(j-1)(x)); movers and non-movers counted apart;
         options whose sigma_j/tau play passes x ("corners") counted, and the rule checked with them included.
  per FL run [a, b]: TIGHT (FL-TIGHT), OPT (W*_j = W_(j-1)), BRIDGE, ANCH_i (sigma on Even non-CN of level <= l constant on [s0+l-1, s1]),
         ANCH_ii (moves of Even c in CN after s0+l*-1 <= |T_c|-1), ANCH_iii (epoch <= CAP; run <= CAP(1+GCH)), CIRC (GCH <= FL-1), CAPNM.
Counters: FL runs / transitions / epochs, GCH, ODIFF Xi-changes over run states, max per ODIFF vertex.
Usage: anchor_check.py files list.txt [runs [prefix]] | random N nmin nmax seed [starts]   (DUMP=1 per FL run)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-LATEP")); sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-WRUN"))
import latep_check as L
import wrun_check as WR
DC, pg, Engine, dual, pval = L.DC, L.pg, L.Engine, L.dual, L.pval
DUMP = os.environ.get("DUMP")


def run_game(g, s, t, st, name):
    n = g.n; m = sum(len(set(x)) for x in g.succ); E = Engine(g); K_ = E.key
    states, fbs = DC.Runner(g).run(list(s), list(t), cap=L.MAXT)
    K = len(states) - 1; st.inc("runs")
    Ev = [g.owner[v] == 0 for v in range(n)]
    def oplus(x, val):
        c, msk, l = val
        return (c, msk | (1 << E.rank[x]) if E.rank[x] > E.rank[c] else msk, l + 1)
    S = []
    for sg, tu in states:
        xe, sb = E.evaluate(tuple(sg[v] if Ev[v] else -1 for v in range(n)))
        xi = [tuple(z) for z in xe]; Is = set(E.improving(tuple(sg), xe))
        sbar = [sb[v] if not Ev[v] else -1 for v in range(n)]
        nxW = [sg[v] if Ev[v] else tu[v] for v in range(n)]
        S.append(dict(sg=sg, tu=tu, xi=xi, Is=Is, sbar=sbar, W=[pval(E, nxW, v) for v in range(n)]))
    def play(nx, y):
        seen = []; s_ = set(); u = y
        while u not in s_: s_.add(u); seen.append(u); u = nx[u]
        return seen
    # RULE at every non-fallback S4a transition
    for j in range(1, K + 1):
        A, B = S[j - 1], S[j]
        if fbs[j - 1] or not A["Is"]: continue
        nx = [B["sg"][v] if Ev[v] else A["tu"][v] for v in range(n)]
        Wp = [pval(E, nx, v) for v in range(n)]
        for x in range(n):
            if not Ev[x] or Wp[x][0] == x: continue
            c = Wp[x][0]
            H = {A["sg"][x]} | {w for (u, w) in A["Is"] if u == x}
            tie = [y for y in sorted(H) if oplus(x, Wp[y]) == Wp[x]]
            if not tie: st.bad("RULE", f"{name}@{j} x={x} empty tie"); continue
            def key(y):
                if E.par[c] == 1: return (y,)
                p = []; u = y
                while u != c: p.append(u); u = nx[u]
                return tuple(reversed(p))
            corner = any(x in play(nx, y) for y in tie)
            mover = B["sg"][x] != A["sg"][x]
            st.inc("RULE_checks_" + ("mover" if mover else "nonmover"))
            if len(tie) > 1: st.inc("RULE_multi_" + ("mover" if mover else "nonmover"))
            if corner: st.inc("RULE_with_corner")
            if B["sg"][x] != min(tie, key=key): st.bad("RULE", f"{name}@{j} x={x} corner={corner} mover={mover}")
    # FL runs
    fl = [j for j in range(1, K + 1) if not fbs[j - 1] and S[j]["tu"] == S[j - 1]["tu"] and S[j]["sg"] != S[j - 1]["sg"] and S[j]["W"] == S[j - 1]["W"]]
    fs = set(fl); runs_ = []; j = 1
    while j <= K:
        if j in fs:
            a = j - 1
            while j in fs: j += 1
            runs_.append((a, j - 1))
        else: j += 1
    for (a, b) in runs_:
        FL = b - a; st.inc("FL_runs"); st.inc("FL_transitions", FL)
        W = S[a]["W"]; tau = S[a]["tu"]; lev = [W[v][2] for v in range(n)]
        CN = {v for v in range(n) if lev[v] == 0}
        T = {}
        for x in range(n):
            if not Ev[x]: continue
            sx = set(g.succ[x])
            T[x] = {y for y in sx if oplus(x, W[y]) == W[x]} if x not in CN else {y for y in sx if W[y][0] == x}
        lstar = max([lev[x] for x in range(n) if Ev[x] and x not in CN], default=1)
        CAP = (lstar - 1) + sum(len(T[c]) - 1 for c in CN if Ev[c])
        if CAP > n + m: st.bad("CAPNM", name)
        for j in range(a, b + 1):
            for x in range(n):
                if Ev[x] and S[j]["sg"][x] not in T[x]: st.bad("TIGHT", f"{name}@{j} x={x}")
        for j in range(a + 1, b + 1):
            if S[j - 1]["W"] != S[j]["W"]: st.bad("OPT", f"{name}@{j}")
            for h in range(n):
                if Ev[h] and h not in CN:
                    o, w = S[j - 1]["sg"][h], S[j]["sg"][h]
                    if oplus(h, W[o]) != W[h] or oplus(h, W[w]) != W[h]: st.bad("BRIDGE", f"{name}@{j} h={h}")
        def G(j):
            od = frozenset(o for o in range(n) if not Ev[o] and S[j]["sbar"][o] != tau[o])
            return (tuple(S[j]["sbar"]), tuple((o, S[j]["xi"][o]) for o in sorted(od)), tuple(S[j]["xi"][c] for c in sorted(CN)))
        Gs = {j: G(j) for j in range(a, b)}
        GCH = sum(1 for j in range(a + 1, b) if Gs[j] != Gs[j - 1])
        if GCH > FL - 1: st.bad("CIRC", name)
        if FL > CAP * (1 + GCH): st.bad("ANCH_iii", f"{name} run {a}-{b} FL {FL} CAP {CAP} GCH {GCH}")
        st.inc("GCH", GCH)
        # epochs: maximal blocks of gating states a..b-1 with equal G; epoch = transitions j-1 -> j, j-1 in block
        blocks = []; s0 = a
        for j in range(a + 1, b):
            if Gs[j] != Gs[j - 1]: blocks.append((s0, j)); s0 = j
        blocks.append((s0, b))
        for (s0, s1) in blocks:
            st.inc("epochs")
            if s1 - s0 > CAP: st.bad("ANCH_iii", f"{name} epoch {s0}-{s1} > CAP {CAP}")
            for l in range(1, lstar + 1):
                X = [x for x in range(n) if Ev[x] and x not in CN and lev[x] <= l]
                lo = s0 + l - 1
                for jj in range(lo + 1, s1 + 1):
                    for x in X:
                        if S[jj]["sg"][x] != S[lo]["sg"][x]: st.bad("ANCH_i", f"{name} epoch {s0}-{s1} l={l} x={x} j={jj}")
            st0 = s0 + lstar - 1
            for c in CN:
                if not Ev[c]: continue
                mv = sum(1 for jj in range(st0 + 1, s1 + 1) if jj > st0 and S[jj]["sg"][c] != S[jj - 1]["sg"][c] and jj - 1 >= st0)
                if mv > len(T[c]) - 1: st.bad("ANCH_ii", f"{name} c={c}")
        # ODIFF Xi changes over run states
        od_all = {o for j in range(a, b + 1) for o in range(n) if not Ev[o] and S[j]["sbar"][o] != tau[o]}
        per = {o: sum(1 for j in range(a + 1, b + 1) if S[j]["xi"][o] != S[j - 1]["xi"][o]) for o in od_all}
        st.inc("ODIFF_xi_changes", sum(per.values())); st.mxu("max_ODIFF_xi_changes_one_vertex_one_run", max(per.values(), default=0))
        if DUMP: print("FLRUN", name, a, b, "n", n, "FL", FL, "CAP", CAP, "GCH", GCH, "epochs", len(blocks), "ODIFF", sorted(od_all),
                       "ODIFFxi", per, flush=True)


L.run_game = run_game; L.read_start = WR.read_start
KEYS = ("RULE", "TIGHT", "OPT", "BRIDGE", "ANCH_i", "ANCH_ii", "ANCH_iii", "CIRC", "CAPNM")
if __name__ == "__main__":
    import io, contextlib, re
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf): L.main()
    bad = 0
    for l in buf.getvalue().splitlines():
        if not l.startswith("RESULT"): print(l)
        m = re.match(r"(\S+): (\d+)$", l)
        if m and m[1] in KEYS: bad += int(m[2])
    print("RESULT", "PASS" if bad == 0 else "FAIL", "violations", bad)
