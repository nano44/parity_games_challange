#!/usr/bin/env python3
r"""REFEREE-2 successor 21 (Opus 5.5, D15): own check of P-N5-CUT (docs/si/P-N5-CUT-box43.md, sha1 d6519d3d @ l-si 2678f6c6).
State loop: my lane's R2-N5-DUAL/dual_check.Runner (SPEC N5 on si.py, read-only); helpers from my R2-N5-FRAME/frame_check.py
(play values, blocked edges). Every definition below is written from the packet's text; the lane's odd/*.py and box64/*.py are NOT imported.
Frames: W^tau(sigma) := my play value of the (sigma, tau)-plays. W_t := W^{tau_t}(sigma_t); Wn_t := W^{tau_t}(sigma_{t+1}) (the old-tau frame
of state t + 1). Off-cycle for tau at a state: the cycle node of v's W^tau-value is not v.
Checks (each must be 0):
  FB      Fact B: every transition is an S4a step with tau kept, or a BOUNDARY (Even S4c fallback or tau-change)
  OO1     OPT-OFF (i): at every S4a step, Wn_t >= W^{tau_t}(sigma'') pointwise for every single-switch sigma'' = sigma_{t+1}[v -> y],
          (v, y) in H_t (all of them if n <= OO1N, else OO1S sampled), and for RANDH random strategies inside H_t
  OO2     OPT-OFF (ii): at every S4a step, every Even v off-cycle (old-tau frame) at t + 1, every (v, y) in H_t: Wn_t(y) <= Wn_t(sigma_{t+1} v)
  WM      W-MON': Wn_t >= W_t pointwise at every S4a step
  WS      W-SUCC (per step): inside a tau*-piece, v off-cycle at t + 1: W_{t+1}(sigma_{t+1} v) >= W_t(sigma_t v)
  WRG     W-RETURN-G: every re-entry j-1 -> j (S4a step) of (v, c) in a lambda-run, EVERY anchor q with v off-cycle for tau* on [q, j] and
          W*(c) constant on [q, j]: W*_j(sigma_{j-1} v) = W*_j(c)
  CC1/CC2/CC3  CUT-CHARGE: classes F/FR/C/P/S partition the re-entries; every P owns a WCH* transition in its window, every FR a boundary in
          [s, j], every F is a boundary; ENT_R(v, c) <= 1 + FC + WCH* + SIL + CYC; FC <= B_R; Remark: #FR <= 1 per (pair, tau*-piece)
  FS      FRESH-SPLIT: the five cases partition FR; (LATE) => (v, c) BLOCKED at j - 2 (old frame = W_{j-2}); the section-5 ENT bound
  LS1/LS2/LS3  LATE-SPLIT on every W-run: #FIRST <= m_E; for consecutive late adoptions u1 < u2 of (y, z): the leave k is unique in (u1, u2);
          if y off-cycle on [k+1, u2+1]: W(z) changes there or W_{u2+1}(sigma_{u2} y) = W_{u2+1}(z); (iii) blocked at t in (k, u2] =>
          W_t(z) > W_{k+1}(z); Consequence #REPEAT(y, z) <= WCH_F(z) + SIL_F + CYC_F
  RREP    R*-REP: R*_T(F) <= #late adoptions <= m_E + REP_F
  WV      WV-R per guided stretch Q: Lambda_Q <= n(n-1); WCH_Q(w) <= L + (L+1)(n-1)(R*_Q+1) <= L + (L+1)(n-1)(m_E+REP*_Q+1);
          the W-runs inside Q are exactly Q's pieces between its lambda_W-changes
  CR      Theorem CUT-RED per run (and its two intermediate inequalities per lambda-run: E bound, WCH* <= B_R + (B_R+1)K)
Controls (X_*, expected to bite somewhere): X_OO2_own (OPT-OFF (ii) at own-cycle-node v), X_WRG_cut (anchor taken across a boundary: q-1 = s
< a, conclusion fails), X_LS_own (LATE-SPLIT (ii) without the off-cycle hypothesis fails), X_REP_silent / X_REP_cyc / X_REP_rise (REPEAT
census: silent and own-cycle REPEATs exist?).
Usage: cut_check.py random N nmin nmax seed [starts] | files list.txt [runs [prefix]]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-FRAME"))
import frame_check as F
DC, pg, Engine, dual = F.DC, F.pg, F.Engine, F.dual
play, pval, blocked_at = F.play, F.pval, F.blocked_at
OO1N = int(os.environ.get("OO1N", "60")); OO1S = int(os.environ.get("OO1S", "30")); RANDH = int(os.environ.get("RANDH", "2"))
MAXT = int(os.environ.get("MAXT", "3000"))


class St(F.St):
    pass


def Wval(E, g, sg, tu):
    nx = [sg[v] if g.owner[v] == 0 else tu[v] for v in range(g.n)]
    return [pval(E, nx, v) for v in range(g.n)]


def run_game(g, s, t, st, name, rng):
    n = g.n; E = Engine(g); Ed = Engine(dual(g)); K = E.key
    states, fbs = DC.Runner(g).run(list(s), list(t), cap=MAXT)
    T = len(states) - 1; st.inc("runs"); st.inc("transitions", T)
    Even = [v for v in range(n) if g.owner[v] == 0]
    mE = sum(len(set(g.succ[v])) for v in Even)
    I = []
    for sg, tu in states:
        xe, _ = E.evaluate(tuple(sg[v] if g.owner[v] == 0 else -1 for v in range(n)))
        Is = set(E.improving(tuple(sg), xe))
        ue, _ = Ed.evaluate(tuple(tu[v] if g.owner[v] == 1 else -1 for v in range(n)))
        W = Wval(E, g, sg, tu)
        I.append(dict(sg=sg, tu=tu, Is=Is, W=W, lam=tuple(z[0] for z in xe), lamU=tuple(z[0] for z in ue), lamW=tuple(z[0] for z in W)))
    Wn = [Wval(E, g, I[k + 1]["sg"], I[k]["tu"]) for k in range(T)]
    H = [{v: sorted({I[k]["sg"][v]} | {w for x, w in I[k]["Is"] if x == v}) for v in Even} for k in range(T + 1)]
    # ---- Fact B, transition kinds
    evfb = [bool(fbs[k]) and bool(I[k]["Is"]) for k in range(T)]
    tch = [I[k + 1]["tu"] != I[k]["tu"] for k in range(T)]
    s4a = [(not fbs[k]) and I[k + 1]["sg"] != I[k]["sg"] for k in range(T)]
    bnd = [evfb[k] or tch[k] for k in range(T)]
    for k in range(T):
        st.inc("FB_checks")
        if not ((s4a[k] and not tch[k]) or bnd[k]): st.bad("FB", f"{name}@{k}")
        if s4a[k] and not I[k]["Is"]: st.bad("FB", f"{name}@{k} S4a step with empty I_sigma")
        if fbs[k] and not I[k]["Is"] and not tch[k]: st.bad("FB", f"{name}@{k} Odd fallback keeps tau")
    # tau*-pieces: maximal runs whose inside transitions are S4a steps with tau kept
    piece = [None] * (T + 1); a = 0
    for k in range(T + 1):
        if k == T or not (s4a[k] and not tch[k]):
            for q in range(a, k + 1): piece[q] = (a, k)
            a = k + 1
    def offc(W, v): return W[v][0] != v
    # ---- OPT-OFF (i), (ii), W-MON', W-SUCC
    for k in range(T):
        if not s4a[k]: continue
        A = I[k]; Wp = Wn[k]; sp = I[k + 1]["sg"]; tu = A["tu"]
        st.inc("WM_checks")
        if any(K(Wp[x]) < K(A["W"][x]) for x in range(n)): st.bad("WM", f"{name}@{k}")
        devs = [(v, y) for v in Even for y in H[k][v] if y != sp[v]]
        if n > OO1N and len(devs) > OO1S: devs = rng.sample(devs, OO1S); st.inc("OO1_sampled_steps")
        for v, y in devs:
            s2 = list(sp); s2[v] = y; W2 = Wval(E, g, s2, tu); st.inc("OO1_checks")
            if any(K(W2[x]) > K(Wp[x]) for x in range(n)): st.bad("OO1", f"{name}@{k} v={v} y={y}")
        for _ in range(RANDH):
            s2 = list(sp)
            for v in Even: s2[v] = rng.choice(H[k][v])
            W2 = Wval(E, g, s2, tu); st.inc("OO1_checks")
            if any(K(W2[x]) > K(Wp[x]) for x in range(n)): st.bad("OO1", f"{name}@{k} random H_t strategy")
        for v in Even:
            for y in H[k][v]:
                bad = K(Wp[y]) > K(Wp[sp[v]])
                if offc(Wp, v):
                    st.inc("OO2_checks")
                    if bad: st.bad("OO2", f"{name}@{k} v={v} y={y}")
                elif bad: st.inc("X_OO2_own")
        if piece[k] == piece[k + 1]:
            B = I[k + 1]
            for v in Even:
                if offc(B["W"], v):
                    st.inc("WS_checks")
                    if K(B["W"][B["sg"][v]]) < K(A["W"][A["sg"][v]]): st.bad("WS", f"{name}@{k} v={v}")
    # frame helper: W* at state t for tau* = tau_{j-1}, j-1 the last piece state used: t <= j-1 -> W_t ; t = j -> Wn_{j-1}
    def Wstar(t, j): return I[t]["W"] if t <= j - 1 else Wn[j - 1]
    # ---- lambda-runs: re-entries, classes, CUT-CHARGE, FRESH-SPLIT, W-RETURN-G
    lruns = []; a = 0
    for k in range(T + 1):
        if k == T or I[k + 1]["lam"] != I[a]["lam"]: lruns.append((a, k)); a = k + 1
    Kfun = lambda r: n * (n - 1) + (n * (n - 1) + 1) * (n - 1) * (mE + r + 1)
    Estar = 0; SCstar = 0; Bstar = 0; per_pair_terms = []
    for (ra, rb) in lruns:
        BR = sum(bnd[k] for k in range(ra, rb)); Bstar = max(Bstar, BR)
        Esum = 0; SCR = 0
        for v in Even:
            for c in sorted(set(g.succ[v])):
                ent = [k for k in range(ra, rb) if I[k]["sg"][v] != c and I[k + 1]["sg"][v] == c]
                Esum += len(ent)
                leaves = [k for k in range(ra, rb) if I[k]["sg"][v] == c and I[k + 1]["sg"][v] != c]
                re = []   # (s, j)
                for s_ in leaves:
                    nxt = [k for k in ent if k >= s_ + 1]
                    if nxt: re.append((s_, nxt[0] + 1))
                cnt = dict(F=0, FR=0, C=0, P=0, S=0); usedW = set(); usedB = set(); frpieces = {}
                fsc = dict(WC=0, G0=0, CY=0, LATE=0, SAME=0)
                for (s_, j) in re:
                    st.inc("reentries")
                    if j - 1 < s_ + 1: st.bad("CC1", f"{name} re-entry window empty"); continue
                    if evfb[j - 1]:
                        cnt["F"] += 1
                        if (j - 1) in usedB: st.bad("CC2", f"{name} F boundary reused")
                        usedB.add(j - 1); continue
                    if not s4a[j - 1]: st.bad("CC1", f"{name}@{j-1} re-entry neither S4a nor Even fallback"); continue
                    pa, pb = piece[j - 1]
                    anchors = [q for q in range(max(s_, pa) + 1, j) if c in H[q - 1][v]]
                    # W-RETURN-G for every anchor
                    for q in anchors:
                        off = all(offc(Wstar(t2, j), v) for t2 in range(q, j + 1))
                        const = all(Wstar(t2, j)[c] == Wstar(q, j)[c] for t2 in range(q, j + 1))
                        if off and const:
                            st.inc("WRG_checks")
                            if Wn[j - 1][I[j - 1]["sg"][v]] != Wn[j - 1][c]: st.bad("WRG", f"{name} v={v} c={c} q={q} j={j}")
                    # control: anchor across a cut (q - 1 = s < pa): frame tau* still, states before pa read in tau* frame
                    if s_ < pa and not anchors:
                        q = s_ + 1
                        Wq = [Wval(E, g, I[t2]["sg"], I[j - 1]["tu"]) for t2 in range(q, j)] + [Wn[j - 1]]
                        if all(Wq[i][v][0] != v for i in range(len(Wq))) and all(Wq[i][c] == Wq[0][c] for i in range(len(Wq))):
                            if Wn[j - 1][I[j - 1]["sg"][v]] != Wn[j - 1][c]: st.inc("X_WRG_cut")
                    if not anchors:
                        cnt["FR"] += 1
                        frpieces[(pa, pb)] = frpieces.get((pa, pb), 0) + 1
                        if pa <= s_: st.bad("CC2", f"{name} FR with a <= s")
                        bk = pa - 1
                        if not (s_ <= bk <= j - 1 and bnd[bk]) or bk in usedB: st.bad("CC2", f"{name} FR boundary {bk} s={s_} j={j}")
                        usedB.add(bk)
                        # FRESH-SPLIT
                        Ws = [Wstar(t2, j) for t2 in range(pa, j + 1)]
                        const = all(w_[c] == Ws[0][c] for w_ in Ws)
                        gain = K(Wn[j - 1][c]) > K(Wn[j - 1][I[j - 1]["sg"][v]])
                        if not const: case = "WC"
                        elif not gain: case = "SAME"
                        elif j - 1 == pa: case = "G0"
                        elif (not offc(I[j - 1]["W"], v)) or (not offc(Wn[j - 1], v)): case = "CY"
                        else: case = "LATE"
                        fsc[case] += 1; st.inc("FS_" + case)
                        if case == "LATE":
                            st.inc("FS_late_checks")
                            A2 = I[j - 2]
                            if not (K(A2["W"][c]) > K(A2["W"][A2["sg"][v]]) and (v, c) not in A2["Is"]): st.bad("FS", f"{name} LATE not blocked v={v} c={c} j={j}")
                        continue
                    q = anchors[0]
                    if any(not offc(Wstar(t2, j), v) for t2 in range(q, j + 1)): cnt["C"] += 1; continue
                    ch = [t2 for t2 in range(q, j) if Wstar(t2 + 1, j)[c] != Wstar(t2, j)[c]]
                    if ch:
                        cnt["P"] += 1
                        t2 = ch[0]
                        if not (s_ + 1 <= t2 and t2 + 1 <= j) or t2 in usedW: st.bad("CC2", f"{name} P witness")
                        if Wn[t2][c] == I[t2]["W"][c]: st.bad("CC2", f"{name} P witness not a WCH* transition")
                        usedW.add(t2)
                    else:
                        cnt["S"] += 1
                if not re and not ent: continue
                # span and WCH*
                if leaves and re:
                    sp0, sp1 = leaves[0], re[-1][1]
                    wch = sum(1 for k in range(sp0, sp1) if Wn[k][c] != I[k]["W"][c])
                else: wch = 0
                FC = cnt["F"] + cnt["FR"]
                st.inc("CC3_checks")
                if len(ent) > 1 + FC + wch + cnt["S"] + cnt["C"]: st.bad("CC3", f"{name} R[{ra},{rb}] v={v} c={c} ENT {len(ent)} {cnt} WCH* {wch}")
                if FC > BR: st.bad("CC3", f"{name} FC {FC} > B_R {BR}")
                if any(x > 1 for x in frpieces.values()): st.bad("CC3", f"{name} two FR re-entries in one piece v={v} c={c}")
                if len(ent) > 1 + (fsc["F"] if False else 0) + cnt["F"] + fsc["G0"] + fsc["SAME"] + wch + fsc["LATE"] + cnt["S"] + cnt["C"] + fsc["CY"]:
                    st.bad("FS", f"{name} section-5 ENT bound v={v} c={c}")
                for k2, x in cnt.items(): st.inc("CL_" + k2, x)
                SCR += cnt["S"] + cnt["C"]
                # WCH* <= B_R + (B_R + 1) K(REP*): REP* checked globally later; record
                if len(ent): per_pair_terms.append((BR, wch))
                st.mxu("max_ENT", len(ent)); st.mxu("max_WCHstar", wch)
        Estar = max(Estar, Esum); SCstar = max(SCstar, SCR)
    # ---- W-runs: LATE-SPLIT, R*-REP; guided stretches: WV-R
    REPstar = 0; wr_of = {}
    pieces = sorted(set(piece))
    for (pa, pb) in pieces:
        cuts = [k for k in range(pa, pb) if I[k + 1]["lamW"] != I[k]["lamW"]]
        LQ = len(cuts); RsQ = 0; REPQ = 0
        if LQ > n * (n - 1): st.bad("WV", f"{name} Lambda_Q {LQ}")
        fa = pa
        for k in cuts + [pb]:
            fb_ = k
            RT, rep = wrun(g, E, I, fa, fb_, st, name, mE)
            RsQ = max(RsQ, RT); REPQ = max(REPQ, rep); fa = k + 1
        REPstar = max(REPstar, REPQ)
        for w in range(n):
            wc = sum(1 for k in range(pa, pb) if I[k + 1]["W"][w] != I[k]["W"][w]); st.inc("WV_checks")
            if wc > LQ + (LQ + 1) * (n - 1) * (RsQ + 1) or LQ + (LQ + 1) * (n - 1) * (RsQ + 1) > LQ + (LQ + 1) * (n - 1) * (mE + REPQ + 1):
                st.bad("WV", f"{name} Q[{pa},{pb}] w={w} WCH {wc}")
    # global W-runs (definition: maximal runs in a tau-stretch, no fallback, no lambda_W change) == pieces cut at lambda_W changes
    a = 0; gw = []
    for k in range(T + 1):
        if k == T or fbs[k] or tch[k] or I[k + 1]["lamW"] != I[k]["lamW"]: gw.append((a, k)); a = k + 1
    mine = []
    for (pa, pb) in pieces:
        fa = pa
        for k in [k for k in range(pa, pb) if I[k + 1]["lamW"] != I[k]["lamW"]] + [pb]: mine.append((fa, k)); fa = k + 1
    if sorted(gw) != sorted(mine): st.bad("WV", f"{name} W-runs differ from pieces cut at lambda_W ({len(gw)} vs {len(mine)})")
    # ---- CUT-RED
    lamUruns = []; a = 0
    for k in range(T + 1):
        if k == T or I[k + 1]["lamU"] != I[a]["lamU"]: lamUruns.append((a, k)); a = k + 1
    Ostar = max(sum(tch[k] for k in range(ra, rb)) for ra, rb in lamUruns)
    Kv = Kfun(REPstar)
    for BR, wch in per_pair_terms:
        st.inc("CR_pair_checks")
        if wch > BR + (BR + 1) * Kv: st.bad("CR", f"{name} WCH* {wch} B_R {BR}")
    if Estar > mE * (1 + 2 * Bstar + (Bstar + 1) * Kv) + SCstar: st.bad("CR", f"{name} E* {Estar}")
    bound = 2 * n * (n - 1) + (n * (n - 1) + 1) * (mE * (1 + 2 * Bstar + (Bstar + 1) * Kv) + SCstar + Ostar)
    st.inc("CR_checks")
    if T > bound: st.bad("CR", f"{name} T {T} > bound {bound}")
    st.mxu("max_Bstar", Bstar); st.mxu("max_REPstar", REPstar); st.mxu("max_SCstar", SCstar); st.mxu("max_Ostar", Ostar); st.mxu("max_T", T)
    if os.environ.get("DUMP"): print(f"RUN {name} n {n} mE {mE} T {T} B* {Bstar} REP* {REPstar} SC* {SCstar} O* {Ostar} E* {Estar}", flush=True)


def wrun(g, E, I, a, b, st, name, mE):
    """one W-run [a, b] (fallback-free, tau and lambda_W constant): late adoptions, LATE-SPLIT, R*-REP. Returns (R*_T, REP_F)."""
    n = g.n; K = E.key; st.inc("wruns")
    BL = {t: blocked_at(g, E, I[t]) for t in range(a, b)}
    everbl = set(); RT = 0; late = {}
    for t in range(a, b):
        ad = [(y, I[t + 1]["sg"][y]) for y in range(n) if g.owner[y] == 0 and I[t + 1]["sg"][y] != I[t]["sg"][y]]
        L = [e for e in ad if e in everbl]
        if L: RT += 1
        for e in L: late.setdefault(e, []).append(t)
        everbl |= BL[t]
    first = len(late); rep = sum(len(u) - 1 for u in late.values()); nl = sum(len(u) for u in late.values())
    st.inc("RREP_checks"); st.inc("late_adoptions", nl); st.inc("late_first", first); st.inc("late_repeat", rep)
    if first > mE: st.bad("LS1", f"{name} FIRST {first}")
    if not (RT <= nl <= mE + rep): st.bad("RREP", f"{name} F[{a},{b}] R*_T {RT} late {nl} REP {rep}")
    off = lambda t, v: I[t]["W"][v][0] != v
    for (y, z), us in late.items():
        wchz = sum(1 for t in range(a, b) if I[t + 1]["W"][z] != I[t]["W"][z]); sil = cyc = 0
        for u1, u2 in zip(us, us[1:]):
            ks = [k for k in range(u1 + 1, u2) if I[k]["sg"][y] == z and I[k + 1]["sg"][y] != z]
            st.inc("LS2_checks")
            if len(ks) != 1: st.bad("LS2", f"{name} leaves between consecutive late adoptions: {ks}"); continue
            k = ks[0]
            changes = any(I[t + 1]["W"][z] != I[t]["W"][z] for t in range(k + 1, u2 + 1))
            silent = I[u2 + 1]["W"][I[u2]["sg"][y]] == I[u2 + 1]["W"][z]
            alloff = all(off(t, y) for t in range(k + 1, u2 + 2))
            if alloff:
                if not (changes or silent): st.bad("LS2", f"{name} REPEAT ({y},{z}) at {u2}")
                if changes: st.inc("X_REP_rise")
                else: st.inc("X_REP_silent"); sil += 1
                for t in range(k + 1, u2 + 1):
                    if (y, z) in BL[t]:
                        st.inc("LS3_checks")
                        if not K(I[t]["W"][z]) > K(I[k + 1]["W"][z]): st.bad("LS3", f"{name} ({y},{z}) t={t}")
            else:
                cyc += 1; st.inc("X_REP_cyc")
                if not (changes or silent): st.inc("X_LS_own")
        if len(us) - 1 > wchz + sil + cyc: st.bad("LS2", f"{name} Consequence ({y},{z})")
    return RT, rep


def main():
    st = St(); a = sys.argv[1:]; rng = random.Random(4343)
    if a[0] == "random":
        N, nmin, nmax, seed = map(int, a[1:5]); ns = int(a[5]) if len(a) > 5 else 2; rng = random.Random(seed)
        for i in range(N):
            g = DC.rand_game(rng, rng.randint(nmin, nmax), "kO")
            for r in range(ns + 1):
                if r == 0: s, t = Engine(g).initial("best"), Engine(dual(g)).initial("best")
                else: s, t = [rng.choice(g.succ[v]) for v in range(g.n)], [rng.choice(g.succ[v]) for v in range(g.n)]
                run_game(g, list(s), list(t), st, f"rand{seed}:{i}#{r}", rng)
    elif a[0] == "files":
        runs = int(a[2]) if len(a) > 2 else 2; pre = a[3] if len(a) > 3 else ""
        for line in [l.split() for l in open(a[1]) if l.strip()]:
            p0 = line[0] if line[0].startswith("/") else os.path.join(DC.ROOT, pre + line[0])
            g = pg.read(p0)
            if len(line) > 1:
                p1 = line[1] if line[1].startswith("/") else os.path.join(DC.ROOT, pre + line[1])
                s, t = list(Engine(g).initial("best")), list(Engine(dual(g)).initial("best"))
                for l2 in open(p1):
                    ps = l2.split()
                    if ps and ps[0] in ("SIGMA0", "TAU0"):
                        for kv in ps[1:]:
                            v, w = map(int, kv.split(":")); (s if ps[0] == "SIGMA0" else t)[v] = w
                if all((s if g.owner[v] == 0 else t)[v] in g.succ[v] for v in range(g.n)):
                    st.inc("starts_valid"); run_game(g, s, t, st, f"{line[0]}#start", rng)
                else: st.inc("starts_INVALID_skipped")
            for r in range(runs):
                if r == 0: s, t = Engine(g).initial("best"), Engine(dual(g)).initial("best")
                else: s, t = [rng.choice(g.succ[v]) for v in range(g.n)], [rng.choice(g.succ[v]) for v in range(g.n)]
                run_game(g, list(s), list(t), st, f"{line[0]}#{r}", rng)
            if os.environ.get("PROGRESS"): print("DONE-FILE", line[0], flush=True)
    print("MODE", " ".join(a), "OO1N", OO1N, "OO1S", OO1S, "RANDH", RANDH, "MAXT", MAXT)
    for k in sorted(st.c): print(f"{k}: {st.c[k]}")
    for k in sorted(st.mx): print(f"max {k}: {st.mx[k]}")
    keys = ("FB", "OO1", "OO2", "WM", "WS", "WRG", "CC1", "CC2", "CC3", "FS", "LS1", "LS2", "LS3", "RREP", "WV", "CR")
    bad = sum(st.c.get(k, 0) for k in keys)
    print("RESULT", "PASS" if bad == 0 else "FAIL", "violations", bad)


if __name__ == "__main__":
    main()
