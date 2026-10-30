#!/usr/bin/env python3
r"""REFEREE-2 successor 22 (Opus 5.5, D15): own check of P-N5-WCH (docs/new/P-N5-WCH-box79.md, sha1 31caa72e @ l-new 2ad78f51).
N5 loop: my lane's R2-N5-DUAL/dual_check.Runner (SPEC S1-S5 on si.py's Engine, read-only). N5-LZC loop: the same loop with S4a's sigma*
replaced by sigma' of packet §7.1 (written here from the packet text). Play values: my R2-N5-FRAME/frame_check.pval. The lane's
experiments/new/box79/*.py, box78/*.py are NOT imported. Definitions follow the packet's §1 text.
Frames: W^tau_t := pval of the (sigma_t, tau)-plays; W_t := W^{tau_t}_t. Xi_t from Engine.evaluate(sigma_t). Z_t := {v : Xi_t != W_t}.
Checks (each must be 0):
  LEX     Fact LEX: CS order = SPEC key order on every pair of distinct values met at a state (sampled); REW R1 / R2 on all vertex pairs
  TIEa/TIEb  Lemma TIE at every S4a step (any tau change), sigma+ = sigma_{t+1}, W' := W^{tau_t}(sigma_{t+1}): (a) v ⊕ W'(d) = W'(v) and
          d's sigma+-path avoids v; (b) W'(d) has cycle node v and empty path set
  NB      NEW-BOUND |F| <= m_E + sum RET_F;  RW / RW1  RET-WCH per (F, v, e), and every return whose leave changes W(v) has a W(e) change in
          [k, u] (distinct choices);  RUN / REP  RUN-WCH and REP-WCH (REP_F with R88's late adoptions, FIRST / REPEAT of R90 (g))
  SZa/SZb/SZc  SIL-Z on every class-S re-entry (R90 (e) classes computed from the definitions; smallest anchor);  SCG  every class-S
          re-entry not in NC / NT is a GXC event (v, j-1);  SC  SIL_R <= GXC_R + NC_R + NT_R <= (B_R + 1) max_P GXC_P + NC_R + NT_R
  GC / GS  GXC-CLOSE, GXC-SPLIT per phase;  LM  LEVEL-MON on every pair t < t' of a phase (v in Z at both, no S4a W(v)-change between);
  DP      DROP-PAID;  F56 / FS / ZS  FBO-R56, FBO-SPLIT, ZF-SPLIT;  GR  R91 GAP-RED's f_P <= n + sum WCH^S4a_P + ZF_P (consistency)
  LZO / LZS / LZT / LZR  N5-LZC: LZ-OPT (val(sigma', tau_t) = W*), LZ-STRICT, TIE = TT = 0, RUN-WCH_LZ / REP-WCH_LZ;  LZN  class-S
          re-entries of N5-LZC (LZ-NOSIL's conclusion; expected 0)
Counters: returns, paid-W, TT, TIE, GXC, CL, FBO, DROP, ZF, NZ, ZFS, FBOS, classes, max WCH_S(e) per tau-stretch (the premise's w).
Controls: X_TIE_noeq (Lemma TIE's (a) conclusion at switched v WITHOUT the hypothesis W'(v) = W(v): must fail somewhere), X_LM_s4a
(LEVEL-MON read across an S4a W(v)-change: decreases exist), TT_paid (returns charged to TT).
Usage: wch_check.py random N nmin nmax seed [starts] | files list.txt [runs [prefix]]   (LZC=1: run N5-LZC instead of N5)"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-FRAME"))
import frame_check as F
DC, pg, Engine, dual, pval, play = F.DC, F.pg, F.Engine, F.dual, F.pval, F.play
MAXT = int(os.environ.get("MAXT", "5000")); LZC = os.environ.get("LZC") == "1"; LEXS = int(os.environ.get("LEXS", "200"))
St = F.St


class LZRunner(DC.Runner):
    """N5-LZC: S4a's sigma* replaced by sigma' (packet §7.1); S4b, S4c (on sigma') unchanged."""
    def run(s, sg, tu, cap=100000, st=None, name=""):
        g, n = s.g, s.n
        sg, tu = list(sg), list(tu)
        states, fbs = [(tuple(sg), tuple(tu))], []
        while len(fbs) < cap:
            vs, Is, vt, It = s.info(sg, tu)
            if not Is and not It: break
            ns, nt = list(sg), list(tu)
            if Is:
                opt = {v: {sg[v]} for v in range(n) if g.owner[v] == 0}
                for v, w in Is: opt[v].add(w)
                succ = [sorted(opt[v]) if g.owner[v] == 0 else [tu[v]] for v in range(n)]
                _, best = Engine(dual(pg.Game(list(g.prio), list(g.owner), succ))).evaluate(
                    tuple(tu[v] if g.owner[v] == 1 else -1 for v in range(n)))
                star = [best[v] if g.owner[v] == 0 else tu[v] for v in range(n)]
                Ws = [pval(s.E, star, v) for v in range(n)]
                for v in range(n):
                    if g.owner[v] != 0: continue
                    d = sg[v]; wv = Ws[v]; keep = False
                    if wv[2] >= 1 and s.E.extend(v, Ws[d]) == wv: keep = True
                    if wv == (v, 0, 0) and Ws[d][0] == v and Ws[d][1] == 0: keep = True
                    ns[v] = d if keep else star[v]
                if st is not None:   # LZ-OPT
                    nx = [ns[v] if g.owner[v] == 0 else tu[v] for v in range(n)]
                    st.inc("LZO_checks")
                    if any(pval(s.E, nx, v) != Ws[v] for v in range(n)): st.bad("LZO", f"{name}@{len(fbs)}")
            if It:
                opt = {v: {tu[v]} for v in range(n) if g.owner[v] == 1}
                for v, w in It: opt[v].add(w)
                succ = [sorted(opt[v]) if g.owner[v] == 1 else [sg[v]] for v in range(n)]
                _, best = Engine(pg.Game(list(g.prio), list(g.owner), succ)).evaluate(
                    tuple(sg[v] if g.owner[v] == 0 else -1 for v in range(n)))
                for v in range(n):
                    if g.owner[v] == 1: nt[v] = best[v]
            fb = 0
            if ns == sg and nt == tu:
                fb = 1 if not (Is and It) else 2
                if Is:
                    for v in {v for v, _ in Is}: ns[v] = max((w for x, w in Is if x == v), key=lambda w: (s.E.key(vs[w]), w))
                else:
                    for v in {v for v, _ in It}: nt[v] = max((w for x, w in It if x == v), key=lambda w: (s.Ed.key(vt[w]), w))
            sg, tu = ns, nt
            states.append((tuple(sg), tuple(tu))); fbs.append(fb)
        return states, fbs


def CS(E, g, x):
    c, m, l = x; n = g.n
    s = [0] * n
    for r in range(n):
        if m >> r & 1: s[r] = 1 if E.rankpar[r] == 0 else -1
    return (E.rew[c],) + tuple(s[r] for r in range(n - 1, -1, -1)) + ((l if E.par[c] == 1 else -l),)


def lev(E, g, a, b):
    A, B = CS(E, g, a), CS(E, g, b)
    for i in range(len(A)):
        if A[i] != B[i]: return i + 1
    return None


def Wv(E, g, sg, tu):
    nx = [sg[v] if g.owner[v] == 0 else tu[v] for v in range(g.n)]
    return [pval(E, nx, v) for v in range(g.n)], nx


def run_game(g, s, t, st, name, rng):
    n = g.n; E = Engine(g); K = E.key
    if LZC: states, fbs = LZRunner(g).run(list(s), list(t), cap=MAXT, st=st, name=name)
    else: states, fbs = DC.Runner(g).run(list(s), list(t), cap=MAXT)
    T = len(states) - 1; st.inc("runs"); st.inc("transitions", T)
    if T >= MAXT: st.inc("runs_capped")
    Even = [v for v in range(n) if g.owner[v] == 0]; Odd = [v for v in range(n) if g.owner[v] == 1]
    nE = len(Even); mE = sum(len(set(g.succ[v])) for v in Even); dE = [0] * n
    for v in Even:
        for z in set(g.succ[v]): dE[z] += 1
    Qodd = [o for o in Odd if len(set(g.succ[o])) >= 2]
    I = []
    for sg, tu in states:
        xe, sb = E.evaluate(tuple(sg[v] if g.owner[v] == 0 else -1 for v in range(n)))
        xi = [tuple(z) for z in xe]; Is = set(E.improving(tuple(sg), xe))
        W, nxW = Wv(E, g, sg, tu)
        I.append(dict(sg=sg, tu=tu, xi=xi, Is=Is, W=W, nxW=nxW, lam=tuple(z[0] for z in xi), lamW=tuple(z[0] for z in W),
                      Z={v for v in range(n) if xi[v] != W[v]}))
    # ---- REW / LEX
    for x in range(n):
        for u in range(n):
            if u == x: continue
            if E.par[u] == 0 and E.pp[u] > E.pp[x] and not E.rew[u] > E.rew[x]: st.bad("LEX", f"{name} R1 {u},{x}")
            if E.par[x] == 1 and E.pp[u] < E.pp[x] and not E.rew[u] > E.rew[x]: st.bad("LEX", f"{name} R2 {u},{x}")
    for k in range(0, T + 1, max(1, (T + 1) // 5)):
        vals = sorted(set(I[k]["xi"]) | set(I[k]["W"]))
        for _ in range(min(LEXS, len(vals) * len(vals))):
            a, b = rng.choice(vals), rng.choice(vals)
            if a == b: continue
            st.inc("LEX_pairs")
            if (K(a) < K(b)) != (CS(E, g, a) < CS(E, g, b)): st.bad("LEX", f"{name} {a} {b}")
    # ---- transition kinds
    tch = [I[k + 1]["tu"] != I[k]["tu"] for k in range(T)]
    s4a = [(not fbs[k]) and bool(I[k]["Is"]) and I[k + 1]["sg"] != I[k]["sg"] for k in range(T)]
    evfb = [bool(fbs[k]) and bool(I[k]["Is"]) for k in range(T)]
    bnd = [evfb[k] or tch[k] for k in range(T)]
    Wn = [None] * T   # W^{tau_t}_{t+1}
    for k in range(T):
        if s4a[k]: Wn[k] = Wv(E, g, I[k + 1]["sg"], I[k]["tu"])[0]
    # ---- Lemma TIE (and LZ-STRICT for N5-LZC) at every S4a step
    for k in range(T):
        if not s4a[k]: continue
        A, B = I[k], I[k + 1]; Wp = Wn[k]; nxp = [B["sg"][v] if g.owner[v] == 0 else A["tu"][v] for v in range(n)]
        for v in Even:
            d = A["sg"][v]
            if B["sg"][v] == d: continue
            if Wp[v] != A["W"][v]:
                st.inc("X_TIE_noeq_tries")
                if Wp[v][0] != v and E.extend(v, Wp[d]) != Wp[v]: st.inc("X_TIE_noeq")
                continue
            st.inc("TIE_hyp")
            if LZC: st.bad("LZS", f"{name}@{k} v={v}")
            if Wp[v][0] != v:
                path, j = play(nxp, d); pre = path[:path.index(Wp[v][0])] if Wp[v][0] in path else path
                if E.extend(v, Wp[d]) != Wp[v] or v in pre: st.bad("TIEa", f"{name}@{k} v={v}")
            else:
                if not (Wp[d][0] == v and Wp[d][1] == 0): st.bad("TIEb", f"{name}@{k} v={v}")
    # ---- tau-stretches, W-runs, phases, lambda-runs
    cutW = [k for k in range(T) if fbs[k] or tch[k] or I[k + 1]["lamW"] != I[k]["lamW"]]
    a = 0; cs = set(cutW); wruns = []
    for k in list(range(T)) + [T]:
        if k == T or k in cs: wruns.append((a, k)); a = k + 1
    a = 0; stretches = []
    for k in list(range(T)) + [T]:
        if k == T or tch[k]: stretches.append((a, k)); a = k + 1
    for (a, b) in stretches:
        for e in range(n):
            w = sum(1 for t in range(a, b) if s4a[t] and I[t + 1]["W"][e] != I[t]["W"][e]); st.mxu("max_WCH_S(e)", w)
    TIEstar = 0; REPstar = 0
    for (a, b) in wruns:
        tf, rp = wrun(g, E, I, a, b, st, name, Even, mE, dE, s4a); TIEstar = max(TIEstar, tf); REPstar = max(REPstar, rp)
    st.mxu("TIE*", TIEstar); st.mxu("REP*", REPstar)
    if LZC and TIEstar: st.bad("LZT", f"{name} TIE* {TIEstar}")
    a = 0; phases = []
    for k in list(range(T)) + [T]:
        if k == T or tch[k] or I[k + 1]["lam"] != I[k]["lam"]: phases.append((a, k)); a = k + 1
    a = 0; lruns = []
    for k in list(range(T)) + [T]:
        if k == T or I[k + 1]["lam"] != I[k]["lam"]: lruns.append((a, k)); a = k + 1
    GXCev = set()
    for k in range(T):
        A, B = I[k], I[k + 1]
        if A["tu"] != B["tu"] or A["lam"] != B["lam"]: continue
        for v in Even:
            if B["sg"][v] != A["sg"][v] and v in A["Z"] and K(B["xi"][v]) > K(A["xi"][v]) and K(B["W"][v]) <= K(A["W"][v]): GXCev.add((v, k))
    gxcP = {}
    if not LZC:
        for P in phases: gxcP[P] = phase(g, E, I, P, st, name, Even, Qodd, nE, s4a, fbs, GXCev)
    for R in lruns: lrun(g, E, I, R, st, name, Even, s4a, fbs, tch, bnd, GXCev, phases, gxcP)


def wrun(g, E, I, a, b, st, name, Even, mE, dE, s4a):
    n = g.n; K = E.key; st.inc("wruns"); L = b - a
    for t in range(a, b):
        if not s4a[t]: st.bad("NB", f"{name} F[{a},{b}] transition {t} not an S4a step")
    WCH = [sum(1 for t in range(a, b) if I[t + 1]["W"][e] != I[t]["W"][e]) for e in range(n)]
    TIE = sum(1 for t in range(a, b) for v in Even if I[t + 1]["sg"][v] != I[t]["sg"][v] and I[t + 1]["W"][v] == I[t]["W"][v])
    RET = {}; TT = {}; held = {}
    for v in Even: held[(v, I[a]["sg"][v])] = True
    lastleave = {}; used = {}
    for u in range(a, b):
        A, B = I[u], I[u + 1]
        for v in Even:
            if B["sg"][v] == A["sg"][v]: continue
            old, e = A["sg"][v], B["sg"][v]
            lastleave[(v, old)] = u
            if I[u + 1]["W"][v] == I[u]["W"][v]: TT[(v, old)] = TT.get((v, old), 0) + 1   # leave of old with W(v) unchanged
            if held.get((v, e)):
                RET[(v, e)] = RET.get((v, e), 0) + 1; st.inc("returns")
                k = lastleave[(v, e)]
                if I[k + 1]["W"][v] != I[k]["W"][v]:
                    ch = [s for s in range(k, u + 1) if I[s + 1]["W"][e] != I[s]["W"][e]]
                    if not ch: st.bad("RW1", f"{name} F[{a},{b}] v={v} e={e} k={k} u={u}")
                    else:
                        st.inc("paid-W")
                        if used.get((v, e), -1) >= ch[0]: st.inc("RW1_reuse_checked")
                        used[(v, e)] = ch[-1]
                else: st.inc("TT_paid")
            held[(v, e)] = True
    for (v, e), r in RET.items():
        if r > WCH[e] + TT.get((v, e), 0): st.bad("RW", f"{name} F[{a},{b}] ({v},{e}) RET {r} WCH {WCH[e]} TT {TT.get((v, e), 0)}")
    sret = sum(RET.values())
    if L > mE + sret: st.bad("NB", f"{name} F[{a},{b}] |F| {L} > m_E {mE} + RET {sret}")
    if L > mE + sum(dE[e] * WCH[e] for e in range(n)) + TIE: st.bad("RUN", f"{name} F[{a},{b}]")
    # REP_F (R88 late adoptions, R90 (g) FIRST / REPEAT)
    def blocked(t, y, z):
        J = I[t]; r = J["sg"][y]
        return z != r and (y, z) not in J["Is"] and K(J["W"][z]) > K(J["W"][r])
    REP = 0; latebefore = set()
    for u in range(a, b):
        for y in Even:
            if I[u + 1]["sg"][y] == I[u]["sg"][y]: continue
            z = I[u + 1]["sg"][y]
            if any(blocked(t, y, z) for t in range(a, u)):
                if (y, z) in latebefore: REP += 1
                latebefore.add((y, z))
    if REP > sum(dE[e] * WCH[e] for e in range(n)) + TIE: st.bad("REP", f"{name} F[{a},{b}] REP {REP}")
    if LZC and (TIE or sum(TT.values())): st.bad("LZT", f"{name} F[{a},{b}] TIE {TIE} TT {sum(TT.values())}")
    st.inc("TIE_F_sum", TIE); st.inc("REP_sum", REP); st.mxu("max_|F|", L); st.mxu("max_REP_F", REP)
    st.mxu("max_returns_per_edge", max(RET.values(), default=0))
    return TIE, REP


def phase(g, E, I, P, st, name, Even, Qodd, nE, s4a, fbs, GXCev):
    n = g.n; K = E.key; a, b = P; st.inc("phases")
    WCHs = [sum(1 for t in range(a, b) if s4a[t] and I[t + 1]["W"][v] != I[t]["W"][v]) for v in range(n)]
    fP = sum(1 for t in range(a, b) if fbs[t])
    ZF = [t for t in range(a, b) if fbs[t] and I[t + 1]["Z"] == I[t]["Z"]]
    for t in range(a, b):
        if not (s4a[t] or (fbs[t] and I[t]["Is"])): st.bad("GS", f"{name} P[{a},{b}] transition {t} neither S4a nor Even fallback")
    G = [(v, t) for (v, t) in GXCev if a <= t < b]
    TIE = sum(1 for t in range(a, b) if s4a[t] for v in Even if I[t + 1]["sg"][v] != I[t]["sg"][v] and I[t + 1]["W"][v] == I[t]["W"][v])
    CL = [(v, t) for (v, t) in G if fbs[t] and v not in I[t + 1]["Z"]]
    FBO = [(v, t) for (v, t) in G if fbs[t] and v in I[t + 1]["Z"]]
    za = len(I[a]["Z"])
    if len(CL) > za + sum(WCHs): st.bad("GC", f"{name} P[{a},{b}]")
    for (v, t) in G:
        if s4a[t] and I[t + 1]["W"][v] != I[t]["W"][v]: st.bad("GS", f"{name} GXC at S4a step not TIE")
    if len(G) > TIE + len(CL) + len(FBO) or len(G) > TIE + za + sum(WCHs) + len(FBO): st.bad("GS", f"{name} P[{a},{b}]")
    # LEV, LEVEL-MON (all pairs), DROP
    LEV = [{v: lev(E, g, I[t]["xi"][v], I[t]["W"][v]) for v in I[t]["Z"]} for t in range(a, b + 1)]
    DROP = [0] * n
    for v in range(n):
        for t in range(a, b + 1):
            if v not in I[t]["Z"]: continue
            for t2 in range(t + 1, b + 1):
                if s4a[t2 - 1] and I[t2]["W"][v] != I[t2 - 1]["W"][v]:
                    if v in I[t2]["Z"] and LEV[t2 - a][v] < LEV[t - a][v]: st.inc("X_LM_s4a")
                    break
                if v in I[t2]["Z"]:
                    st.inc("LM_checks")
                    if LEV[t2 - a][v] < LEV[t - a][v]: st.bad("LM", f"{name} P[{a},{b}] v={v} t={t} t2={t2}")
        for k in range(a, b):
            if s4a[k] and I[k + 1]["W"][v] != I[k]["W"][v]: continue
            if v in I[k]["Z"] and v in I[k + 1]["Z"] and LEV[k + 1 - a][v] > LEV[k - a][v]: DROP[v] += 1
        if DROP[v] > (n + 1) * (1 + WCHs[v]): st.bad("DP", f"{name} P[{a},{b}] v={v}")
    # rho_P: Xi-changes at Odd choice vertices in the phase
    rho = sum(1 for t in range(a, b) for o in Qodd if I[t + 1]["xi"][o] != I[t]["xi"][o])
    if fP > 1 + (n - 1) * (2 + rho): st.bad("F56", f"{name} P[{a},{b}] f {fP} rho {rho} (R56 premise)")
    if len(FBO) > nE * fP: st.bad("F56", f"{name} P[{a},{b}]")
    FBOS = [(v, t) for (v, t) in FBO if LEV[t + 1 - a][v] == LEV[t - a][v]]
    if len(FBO) > sum(DROP) + len(FBOS): st.bad("FS", f"{name} P[{a},{b}]")
    def own(v, t): return I[t]["lam"][v] == v
    NZ = ZFS = 0
    for k in ZF:
        sw = [v for v in Even if I[k + 1]["sg"][v] != I[k]["sg"][v]]
        nonown = [v for v in sw if not own(v, k) and not own(v, k + 1)]
        if not nonown: NZ += 1
        elif all(LEV[k + 1 - a].get(v) == LEV[k - a].get(v) for v in nonown):
            ZFS += 1
            if any(v not in I[k]["Z"] for v in nonown): st.bad("ZS", f"{name} SW-IN premise fails at {k}")
    if len(ZF) > NZ + sum(DROP) + ZFS: st.bad("ZS", f"{name} P[{a},{b}]")
    if fP > n + sum(WCHs) + len(ZF): st.bad("GR", f"{name} P[{a},{b}] (R91 GAP-RED)")
    for k_, v_ in (("GXC", len(G)), ("CL", len(CL)), ("FBO", len(FBO)), ("FBOS", len(FBOS)), ("DROP", sum(DROP)), ("ZF", len(ZF)),
                   ("NZ", NZ), ("ZFS", ZFS), ("f_P", fP), ("TIE_P", TIE)): st.inc(k_, v_)
    return len(G)


def lrun(g, E, I, R, st, name, Even, s4a, fbs, tch, bnd, GXCev, phases, gxcP):
    n = g.n; K = E.key; a0, b0 = R; T = len(I) - 1
    def piece(t):   # tau*-piece containing state t (tau = tau_t, inside transitions S4a steps)
        lo = t
        while lo > 0 and s4a[lo - 1] and I[lo - 1]["tu"] == I[t]["tu"]: lo -= 1
        hi = t
        while hi < T and s4a[hi] and I[hi + 1]["tu"] == I[t]["tu"]: hi += 1
        return lo, hi
    cls = {"F": 0, "FR": 0, "C": 0, "P": 0, "S": 0}; SIL = NC = NT = 0
    for v in Even:
        leave_of = {}
        for t in range(a0, b0):
            A, B = I[t], I[t + 1]
            if B["sg"][v] == A["sg"][v]: continue
            c = B["sg"][v]
            if c in leave_of:
                s, j = leave_of.pop(c), t + 1
                if evfb := (fbs[j - 1] and I[j - 1]["Is"]): cls["F"] += 1
                else:
                    tau = I[j - 1]["tu"]; pa, pb = piece(j - 1)
                    q = None
                    for qq in range(max(s, pa) + 1, j):
                        J = I[qq - 1]
                        if J["sg"][v] == c or (v, c) in J["Is"]: q = qq; break
                    if q is None: cls["FR"] += 1
                    else:
                        Ws = {x: Wv(E, g, I[x]["sg"], tau)[0] for x in range(q - 1, j + 1)}
                        if any(Ws[x][v][0] == v for x in range(q, j + 1)): cls["C"] += 1
                        elif any(Ws[x][c] != Ws[q][c] for x in range(q, j + 1)): cls["P"] += 1
                        else:
                            cls["S"] += 1; SIL += 1; d = I[j - 1]["sg"][v]
                            if not (Ws[j - 1][d] == Ws[j][d] == Ws[j][c] == Ws[j - 1][c] and Ws[j][v] == Ws[j - 1][v]): st.bad("SZa", f"{name} v={v} j={j}")
                            if LZC: st.bad("LZN", f"{name} class-S re-entry v={v} j={j}")
                            owna, ownb = I[j - 1]["lam"][v] == v, I[j]["lam"][v] == v
                            if not owna:
                                Xi = I[j - 1]["xi"]
                                if not (Xi[d] != Ws[j - 1][d] and Xi[v] != Ws[j - 1][v]): st.bad("SZb", f"{name} v={v} j={j}")
                            if not owna and not ownb and not K(I[j]["xi"][v]) > K(I[j - 1]["xi"][v]): st.bad("SZc", f"{name} v={v} j={j}")
                            if owna or ownb: NC += 1
                            elif I[j]["tu"] != I[j - 1]["tu"]: NT += 1
                            elif (v, j - 1) not in GXCev: st.bad("SCG", f"{name} v={v} j={j}")
                            if (owna or ownb) and I[j]["tu"] != I[j - 1]["tu"]: st.inc("NC_and_NT")
            leave_of[A["sg"][v]] = t
    for k_, v_ in cls.items(): st.inc("class_" + k_, v_)
    G = sum(1 for (v, t) in GXCev if a0 <= t < b0)
    BR = sum(1 for t in range(a0, b0) if bnd[t])
    Ps = [P for P in phases if a0 <= P[0] and P[1] <= b0]
    if len(Ps) > BR + 1: st.bad("SC", f"{name} R[{a0},{b0}] phases {len(Ps)} > B_R+1")
    mx = max((gxcP.get(P, 0) for P in Ps), default=0)
    if SIL > G + NC + NT: st.bad("SC", f"{name} R[{a0},{b0}] SIL {SIL} GXC {G} NC {NC} NT {NT}")
    if not LZC and G + NC + NT > (BR + 1) * mx + NC + NT: st.bad("SC", f"{name} R[{a0},{b0}] (B_R+1) max")
    st.inc("SIL", SIL); st.inc("NC", NC); st.inc("NT", NT)


def read_start(g, path):
    s, t = list(Engine(g).initial("best")), list(Engine(dual(g)).initial("best"))
    for l2 in open(path):
        ps = l2.split()
        if ps and ps[0] in ("SIGMA0", "TAU0"):
            for kv in ps[1:]:
                v, w = map(int, kv.split(":")); (s if ps[0] == "SIGMA0" else t)[v] = w
    return s, t, all((s if g.owner[v] == 0 else t)[v] in g.succ[v] for v in range(g.n))


def main():
    st = St(); a = sys.argv[1:]; rng = random.Random(2223)
    if a[0] == "random":
        N, nmin, nmax, seed = map(int, a[1:5]); ns = int(a[5]) if len(a) > 5 else 2; rng = random.Random(seed)
        for i in range(N):
            g = DC.rand_game(rng, rng.randint(nmin, nmax), "kO")
            for r in range(ns + 1):
                if r == 0: s, t = Engine(g).initial("best"), Engine(dual(g)).initial("best")
                else: s, t = [rng.choice(g.succ[v]) for v in range(g.n)], [rng.choice(g.succ[v]) for v in range(g.n)]
                run_game(g, list(s), list(t), st, f"rand{seed}:{i}#{r}", rng)
    elif a[0] == "files":
        runs = int(a[2]) if len(a) > 2 else 1; pre = a[3] if len(a) > 3 else ""
        for line in [l.split() for l in open(a[1]) if l.strip() and not l.startswith("#")]:
            g = pg.read(os.path.join(DC.ROOT, pre + line[0]))
            if len(line) > 1:
                s, t, ok = read_start(g, os.path.join(DC.ROOT, pre + line[1]))
                if ok: st.inc("starts_valid"); run_game(g, s, t, st, f"{line[0]}#start", rng)
                else: st.inc("starts_INVALID_skipped")
            for r in range(runs):
                if r == 0: s, t = Engine(g).initial("best"), Engine(dual(g)).initial("best")
                else: s, t = [rng.choice(g.succ[v]) for v in range(g.n)], [rng.choice(g.succ[v]) for v in range(g.n)]
                run_game(g, list(s), list(t), st, f"{line[0]}#{r}", rng)
            if os.environ.get("PROGRESS"): print("DONE-FILE", line[0], flush=True)
    print("MODE", " ".join(a), "MAXT", MAXT, "LZC", LZC)
    for k in sorted(st.c): print(f"{k}: {st.c[k]}")
    for k in sorted(st.mx): print(f"max {k}: {st.mx[k]}")
    keys = ("LEX", "TIEa", "TIEb", "NB", "RW", "RW1", "RUN", "REP", "SZa", "SZb", "SZc", "SCG", "SC", "GC", "GS", "LM", "DP", "F56", "FS",
            "ZS", "GR", "LZO", "LZS", "LZT", "LZR", "LZN")
    bad = sum(st.c.get(k, 0) for k in keys)
    print("RESULT", "PASS" if bad == 0 else "FAIL", "violations", bad)


if __name__ == "__main__":
    main()
