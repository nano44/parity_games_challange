#!/usr/bin/env python3
r"""REFEREE-2 successor 22 (Opus 5.5, D15): own check of P-N5-LATEP (L-SI boxes 51-52: LATE', FW-R*', LATE-SPLIT', GAP-CLIMB,
GXC <= TXC <= ZXC, TXC-DESCENT, TXC-RED). State loop: my lane's R2-N5-DUAL/dual_check.Runner (SPEC N5 on si.py, read-only); play values
from my R2-N5-FRAME/frame_check.pval. The lane's odd/latep.py, odd/txcd.py, odd/tied.py and new/box21/n5x.py are NOT imported.
Every definition is written from the packet text.
Frames. Xi_t, sbar_t := si.py's Engine.evaluate(sigma_t) (checked: Xi_t = my play value of the (sigma_t, sbar_t)-plays, XIPLAY);
W_t := my play value of the (sigma_t, tau_t)-plays; Z_t := {v : Xi_t(v) != W_t(v)}; D_t := {Odd u : sbar_t(u) != tau_t(u)}.
W-run F = [a, b]: maximal, every transition inside has no fallback, keeps tau and keeps lambda_W (R89).
BLOCKED at t (R88 §3): (y, z) Even edge, z != sigma_t(y), W_t(z) > W_t(sigma_t y), (y, z) not in I_sigma_t.
Adoption of (y, z) at u: sigma_{u+1}(y) = z != sigma_u(y). p := previous adoption transition of (y, z) in F.
  LATE88: blocked at some t in [a, u).   LATE': blocked at some t in [max(a, p + 1), u).
  REP' := LATE' adoptions with an earlier LATE' adoption of the edge in F (frozen packet §2); REPA := LATE' with p defined (the tool's REPP). Box-50 REPEAT := LATE88 adoption with an earlier LATE88 adoption of the edge in F;
  re-blocked := blocked at some state of [k + 1, u - 1] (k = y's last leave of z before u); STALE := box-50 REPEAT not re-blocked.
Checks (each must be 0):
  XIPLAY  Xi_t(v) = play value of (sigma_t, sbar_t) from v          XW     Xi_t <= W_t pointwise       XIMON  Xi non-decreasing (whole run)
  LCT     whole run: lambda_Xi changes per vertex <= n - 1 and lambda_Xi-changing transitions <= n(n - 1)
  WMON    W non-decreasing on every W-run                           RSUB   every LATE' adoption is LATE88
  FWR / FWP   FW-R* (WCH <= (n-1)(R*_T + 1)) and FW-R*' (WCH <= (n-1)(R*'_T + 1)) on every W-run
  A2      every box-50 re-blocked REPEAT is a REP' (A1 = REP' that are not box-50 REPEATs: counted, informative)
  C0      no STALE REPEAT is LATE'
  LSP     LATE-SPLIT' (b): every REP' at u, y off-cycle (lambda_W(y) != y), every blocked state t_b in [k+1, u-1]: W_{t_b}(z) > W_{k+1}(z)
          (proof steps counted: LSP_opt  W_{k+1}(sigma_{k+1} y) >= W_{k+1}(z);  LSP_succ  W_{t_b}(sigma_{t_b} y) >= W_{k+1}(sigma_{k+1} y))
  REPSUB  every REPEAT' is a P-N5-CUT §6 REPEAT, and REP'_F <= REP_F per W-run
  XSIL    a W-silent REP' (no W(z) change on [k+1, u-1]) whose y is off-cycle
  CIR1..CIR3  CIRCLE': REP' <= n_E R*'_T;  R*'_T <= m_E + REP';  REP' <= X' + sum_z d_E(z) WCH_F(z)   (X' := own-cycle REP')
  GC      GAP-CLIMB: t_b := last blocked state in [max(a, p+1), u); s := first transition of [t_b, u-1] with Xi(z) change: exists, strict
          rise, z in Z_s.  GTOK  tokens (edge, s) distinct.  GCE  LATE'_F(y, z) <= ZXC_F(z).  GCS  LATE'_F <= sum_z d_E(z) ZXC_F(z)
  INC     GXC_F subset TXC_F subset ZXC_F; every ZXC \ TXC event changes W(z) (WZ); WZ_F(z) <= WCH_F(z)
  DESC    TXC-DESCENT: along z's (sigma_{s+1}, sbar_{s+1})-play every vertex before the terminal is a TXC event, no repeat before a terminal
          (CYC), a T2 terminal at a lambda_Xi-fixed transition is a GXC event (T2G)
  RED     TXC-RED: TXC_F <= n (GXC_F + GATE_F + CNW_F) + n^2 LCT_F
Controls (X_*, expected nonzero somewhere): X_noT3 / X_noT2 / X_noT4 (continue the descent through that terminal kind: next vertex
not TXC), X_GXCstrict / X_TXCstrict (strict inclusions), X_LSP_own (LATE-SPLIT' conclusion fails at an own-cycle y),
X_A3 (box-50 re-blocked REPEATs that are not REPEAT'), X_REPA_gt_REPP_wruns (W-runs where the tool's REPP exceeds REP').
BF=n: at every state of games with n <= BF, Xi_t(v) = min over ALL positional Odd strategies of the play value (independent of si.py).
Usage: latep_check.py random N nmin nmax seed [starts] | files list.txt [runs [prefix]]   (DUMP=1 prints one line per W-run)"""
import sys, os, random, itertools
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-FRAME"))
import frame_check as F
DC, pg, Engine, dual, pval = F.DC, F.pg, F.Engine, F.dual, F.pval
MAXT = int(os.environ.get("MAXT", "5000")); BF = int(os.environ.get("BF", "0")); BFPROD = int(os.environ.get("BFPROD", "4096"))
St = F.St


def run_game(g, s, t, st, name):
    n = g.n; E = Engine(g); K = E.key
    states, fbs = DC.Runner(g).run(list(s), list(t), cap=MAXT)
    T = len(states) - 1; st.inc("runs"); st.inc("transitions", T)
    if T >= MAXT: st.inc("runs_capped")
    Even = [v for v in range(n) if g.owner[v] == 0]; Odd = [v for v in range(n) if g.owner[v] == 1]
    nE = len(Even); mE = sum(len(set(g.succ[v])) for v in Even); dE = [0] * n
    for v in Even:
        for z in set(g.succ[v]): dE[z] += 1
    info = []
    for sg, tu in states:
        xe, sb = E.evaluate(tuple(sg[v] if g.owner[v] == 0 else -1 for v in range(n)))
        xi = [tuple(z) for z in xe]; Is = set(E.improving(tuple(sg), xe))
        sbar = tuple(sb[v] if g.owner[v] == 1 else -1 for v in range(n))
        nxX = [sg[v] if g.owner[v] == 0 else sbar[v] for v in range(n)]
        nxW = [sg[v] if g.owner[v] == 0 else tu[v] for v in range(n)]
        W = [pval(E, nxW, v) for v in range(n)]
        for v in range(n):
            st.inc("XIPLAY_checks")
            if pval(E, nxX, v) != xi[v]: st.bad("XIPLAY", f"{name} v={v}")
            if K(xi[v]) > K(W[v]): st.bad("XW", f"{name} v={v}")
        info.append(dict(sg=sg, tu=tu, xi=xi, Is=Is, sbar=sbar, nxX=nxX, W=W, lam=tuple(z[0] for z in xi),
                         lamW=tuple(z[0] for z in W), Z={v for v in range(n) if xi[v] != W[v]},
                         D={u for u in Odd if sbar[u] != tu[u]}))
        if BF and n <= BF: bfcheck(g, E, sg, xi, st, name)
    lamch = [0] * n; lct = 0
    for k in range(T):
        A, B = info[k], info[k + 1]
        if any(K(B["xi"][v]) < K(A["xi"][v]) for v in range(n)): st.bad("XIMON", f"{name}@{k}")
        ch = [v for v in range(n) if A["lam"][v] != B["lam"][v]]
        for v in ch: lamch[v] += 1
        lct += bool(ch)
    if max(lamch, default=0) > n - 1 or lct > n * (n - 1): st.bad("LCT", f"{name} per-vertex {max(lamch)} transitions {lct}")
    st.mxu("max_LCT_run", lct)
    cut = [k for k in range(T) if fbs[k] or info[k + 1]["tu"] != info[k]["tu"] or info[k + 1]["lamW"] != info[k]["lamW"]]
    a = 0; cs = set(cut)
    for k in list(range(T)) + [T]:
        if k == T or k in cs:
            wrun(g, E, info, a, k, st, name, Even, nE, mE, dE)
            a = k + 1


def bfcheck(g, E, sg, xi, st, name):
    n = g.n; K = E.key; Odd = [v for v in range(n) if g.owner[v] == 1]
    ch = [sorted(set(g.succ[v])) for v in Odd]; prod = 1
    for c in ch: prod *= len(c)
    if prod > BFPROD: st.inc("BF_skipped_states"); return
    best = [None] * n
    for choice in itertools.product(*ch):
        tu = dict(zip(Odd, choice)); nx = [sg[v] if g.owner[v] == 0 else tu[v] for v in range(n)]
        for v in range(n):
            pv = pval(E, nx, v)
            if best[v] is None or K(pv) < K(best[v]): best[v] = pv
    st.inc("BF_states")
    for v in range(n):
        if K(best[v]) != K(xi[v]): st.bad("BF", f"{name} v={v} bf={best[v]} xi={xi[v]}")


def wrun(g, E, info, a, b, st, name, Even, nE, mE, dE):
    n = g.n; K = E.key; st.inc("wruns"); st.mxu("max_wrun", b - a)
    lamW = info[a]["lamW"]
    for t in range(a, b):
        if any(K(info[t + 1]["W"][v]) < K(info[t]["W"][v]) for v in range(n)): st.bad("WMON", f"{name}@{t}")
    def blocked(t, y, z):
        I = info[t]; r = I["sg"][y]
        return z != r and (y, z) not in I["Is"] and K(I["W"][z]) > K(I["W"][r])
    Wch = [[info[t + 1]["W"][v] != info[t]["W"][v] for v in range(n)] for t in range(a, b)]
    WCH = sum(any(r) for r in Wch); WCHz = [sum(Wch[i][z] for i in range(b - a)) for z in range(n)]
    def wchg(t, z): return Wch[t - a][z]
    def climb(t, z): return K(info[t + 1]["xi"][z]) > K(info[t]["xi"][z])
    ZXC, TXC, GXC = set(), set(), set()
    for t in range(a, b):
        A, B = info[t], info[t + 1]; lamfix = A["lam"] == B["lam"]
        for v in range(n):
            if not climb(t, v): continue
            if v in A["Z"]: ZXC.add((v, t))
            if B["W"][v] == A["W"][v]: TXC.add((v, t))
            if g.owner[v] == 0 and B["sg"][v] != A["sg"][v] and B["tu"] == A["tu"] and lamfix and v in A["Z"] and K(B["W"][v]) <= K(A["W"][v]):
                GXC.add((v, t))
    # ---- inclusions
    st.inc("INC_checks")
    if not GXC <= TXC or not TXC <= ZXC: st.bad("INC", f"{name} F[{a},{b}] GXC-TXC {sorted(GXC - TXC)[:3]} TXC-ZXC {sorted(TXC - ZXC)[:3]}")
    WZ = ZXC - TXC
    for (z, t) in WZ:
        if not wchg(t, z): st.bad("INC", f"{name} WZ event without W change z={z} t={t}")
    for z in range(n):
        if sum(1 for (x, t) in WZ if x == z) > WCHz[z]: st.bad("INC", f"{name} WZ_F({z}) > WCH_F({z})")
    st.inc("ZXC", len(ZXC)); st.inc("TXC", len(TXC)); st.inc("GXC", len(GXC)); st.inc("WZ", len(WZ))
    if TXC - GXC: st.inc("X_GXCstrict")
    if ZXC - TXC: st.inc("X_TXCstrict")
    # ---- adoptions
    lastad, lastlate88, lastleave, lastlateP = {}, {}, {}, {}
    RT = RTP = REPP = XP = LP = REPA = REP88 = 0; lateP = {}; tok = set()
    for u in range(a, b):
        A, B = info[u], info[u + 1]; is88 = isP = False
        for y in Even:
            if B["sg"][y] == A["sg"][y]: continue
            lastleave[(y, A["sg"][y])] = u
            z = B["sg"][y]; e = (y, z); p = lastad.get(e)
            lo = a if p is None else p + 1
            bl88 = [t for t in range(a, u) if blocked(t, y, z)]
            blP = [t for t in bl88 if t >= lo]
            L88, LP_ = bool(bl88), bool(blP)
            is88 |= L88; isP |= LP_
            if LP_ and not L88: st.bad("RSUB", f"{name} {e}@{u}")
            k = lastleave.get(e) if p is not None else None   # y's last leave of z before u (exists if p exists)
            rep50 = L88 and e in lastlate88
            REP88 += rep50
            if rep50:
                k50 = lastleave[e]; reblk = any(blocked(t, y, z) for t in range(k50 + 1, u))
                st.inc("REP50"); st.inc("REP50_reblocked" if reblk else "REP50_stale")
                if reblk and not (LP_ and p is not None): st.bad("A2", f"{name} {e}@{u}")
                if reblk and e not in lastlateP: st.inc("X_A3_reblk_not_REPEATprime")
                if not reblk and LP_: st.bad("C0", f"{name} {e}@{u}")
            if LP_:
                LP += 1; lateP[e] = lateP.get(e, 0) + 1
                tb = max(blP)
                sc = [s for s in range(tb, u) if info[s + 1]["xi"][z] != info[s]["xi"][z]]
                st.inc("GC_checks")
                if not sc or not climb(sc[0], z) or z not in info[sc[0]]["Z"]: st.bad("GC", f"{name} {e}@{u} tb={tb} sc={sc[:2]}")
                else:
                    if (e, sc[0]) in tok: st.bad("GTOK", f"{name} {e} s={sc[0]}")
                    tok.add((e, sc[0]))
                    st.inc("GC_tied" if not wchg(sc[0], z) else "GC_WZ")
                if p is not None: REPA += 1   # the tool's REPP: LATE' with ANY earlier adoption
                if e in lastlateP:              # REPEAT' (frozen packet §2): an earlier LATE' adoption of e in F
                    REPP += 1
                    if not rep50: st.bad("REPSUB", f"{name} {e}@{u} REPEAT' not a P-N5-CUT REPEAT")
                    own = lamW[y] == y
                    silent = not any(wchg(t, z) for t in range(k + 1, u))
                    if own: XP += 1
                    if silent:
                        st.inc("REPP_silent")
                        if not own: st.bad("XSIL", f"{name} {e}@{u} k={k}")
                    for tbb in [t for t in range(k + 1, u) if blocked(t, y, z)]:
                        st.inc("LSP_checks")
                        Wk, Wt = info[k + 1]["W"], info[tbb]["W"]
                        concl = K(Wt[z]) > K(Wk[z])
                        if own:
                            if not concl: st.inc("X_LSP_own")
                            continue
                        if not concl: st.bad("LSP", f"{name} {e}@{u} k={k} tb={tbb}")
                        if K(Wk[info[k + 1]["sg"][y]]) < K(Wk[z]): st.bad("LSP_opt", f"{name} {e}@{u}")
                        if K(Wt[info[tbb]["sg"][y]]) < K(Wk[info[k + 1]["sg"][y]]): st.bad("LSP_succ", f"{name} {e}@{u}")
            if L88: lastlate88[e] = u
            if LP_: lastlateP[e] = u
            lastad[e] = u
        RT += is88; RTP += isP
    st.inc("FWR_checks")
    if WCH > (n - 1) * (RT + 1): st.bad("FWR", f"{name} F[{a},{b}] WCH {WCH} RT {RT}")
    if WCH > (n - 1) * (RTP + 1): st.bad("FWP", f"{name} F[{a},{b}] WCH {WCH} RTP {RTP}")
    if REPP > nE * RTP: st.bad("CIR1", f"{name} F[{a},{b}]")
    if RTP > mE + REPP: st.bad("CIR2", f"{name} F[{a},{b}]")
    if REPP > XP + sum(dE[z] * WCHz[z] for z in range(n)): st.bad("CIR3", f"{name} F[{a},{b}]")
    if REPP > REP88: st.bad("REPSUB", f"{name} F[{a},{b}] REP' {REPP} > REP {REP88}")
    st.inc("REPA_sum", REPA); st.inc("REP88_sum", REP88); st.mxu("REPA", REPA)
    if REPA > REPP: st.inc("X_REPA_gt_REPP_wruns")
    zxcz = [sum(1 for (x, t) in ZXC if x == z) for z in range(n)]
    for (y, z), c in lateP.items():
        st.inc("GCE_checks")
        if c > zxcz[z]: st.bad("GCE", f"{name} F[{a},{b}] ({y},{z}) {c} > ZXC {zxcz[z]}")
    if LP > sum(dE[z] * zxcz[z] for z in range(n)): st.bad("GCS", f"{name} F[{a},{b}]")
    for k_, v_ in (("WCH", WCH), ("RT", RT), ("RTP", RTP), ("REPP", REPP)): st.mxu(k_, v_)
    st.inc("LP", LP); st.inc("XP", XP); st.inc("RT_sum", RT); st.inc("RTP_sum", RTP); st.inc("REPP_sum", REPP)
    # ---- TXC-DESCENT and TXC-RED
    term = {}; GATE, CNW = set(), set()
    for (z, s) in TXC:
        A, B = info[s], info[s + 1]
        if g.owner[z] == 1 and (z in A["D"] or z in B["D"]): GATE.add((z, s))
        if lamW[z] == z: CNW.add((z, s))
    LCTF = sum(1 for t in range(a, b) if info[t + 1]["lam"] != info[t]["lam"])
    def kind(x, s, drop=""):
        A, B = info[s], info[s + 1]
        if A["lam"][x] != B["lam"][x]: return "T1"
        if g.owner[x] == 0 and B["sg"][x] != A["sg"][x] and "T2" not in drop: return "T2"
        if g.owner[x] == 1 and (x in A["D"] or x in B["D"]) and "T3" not in drop: return "T3"
        if lamW[x] == x and "T4" not in drop: return "T4"
        return None
    for (z, s) in TXC:
        nx = info[s + 1]["nxX"]; x = z; seen = set(); st.inc("DESC_checks")
        while True:
            if (x, s) not in TXC: st.bad("DESC", f"{name} F[{a},{b}] z={z} s={s} at x={x}"); break
            if x in seen: st.bad("CYC", f"{name} z={z} s={s}"); break
            seen.add(x); kd = kind(x, s)
            if kd:
                st.inc("DESC_" + kd)
                if kd == "T2" and info[s]["lam"] == info[s + 1]["lam"] and (x, s) not in GXC: st.bad("T2G", f"{name} x={x} s={s}")
                if kd == "T2" and info[s]["lam"] != info[s + 1]["lam"]: st.inc("DESC_T2_lamchg")
                term[(x, s, kd)] = term.get((x, s, kd), 0) + 1
                for dk in ("T2", "T3", "T4"):
                    if kd == dk and kind(x, s, dk) is None:
                        y = nx[x]; st.inc(f"X_no{dk}_tries")
                        if (y, s) not in TXC: st.inc(f"X_no{dk}")
                break
            x = nx[x]
    RHS = n * (len(GXC) + len(GATE) + len(CNW)) + n * n * LCTF
    st.inc("RED_checks")
    if len(TXC) > RHS: st.bad("RED", f"{name} F[{a},{b}] TXC {len(TXC)} RHS {RHS}")
    st.inc("GATE", len(GATE)); st.inc("CNW", len(CNW)); st.inc("LCT_F", LCTF)
    st.inc("gate_terminals", sum(1 for (x, s, kd) in term if kd == "T3"))
    st.mxu("most_TXC_per_terminal", max(term.values(), default=0))
    if os.environ.get("DUMP"):
        print(f"WRUN {name} [{a},{b}] WCH {WCH} RT {RT} RTP {RTP} REPP {REPP} XP {XP} LP {LP} ZXC {len(ZXC)} TXC {len(TXC)} "
              f"GXC {len(GXC)} GATE {len(GATE)} CNW {len(CNW)} LCT {LCTF}", flush=True)


def read_start(g, path):
    s, t = list(Engine(g).initial("best")), list(Engine(dual(g)).initial("best"))
    for l2 in open(path):
        ps = l2.split()
        if ps and ps[0] in ("SIGMA0", "TAU0"):
            for kv in ps[1:]:
                v, w = map(int, kv.split(":")); (s if ps[0] == "SIGMA0" else t)[v] = w
    ok = all((s if g.owner[v] == 0 else t)[v] in g.succ[v] for v in range(g.n))
    return s, t, ok


def main():
    st = St(); a = sys.argv[1:]; rng = random.Random(2222)
    if a[0] == "random":
        N, nmin, nmax, seed = map(int, a[1:5]); ns = int(a[5]) if len(a) > 5 else 2; rng = random.Random(seed)
        for i in range(N):
            g = DC.rand_game(rng, rng.randint(nmin, nmax), "kO")
            for r in range(ns + 1):
                if r == 0: s, t = Engine(g).initial("best"), Engine(dual(g)).initial("best")
                else: s, t = [rng.choice(g.succ[v]) for v in range(g.n)], [rng.choice(g.succ[v]) for v in range(g.n)]
                run_game(g, list(s), list(t), st, f"rand{seed}:{i}#{r}")
    elif a[0] == "files":
        runs = int(a[2]) if len(a) > 2 else 1; pre = a[3] if len(a) > 3 else ""
        for line in [l.split() for l in open(a[1]) if l.strip() and not l.startswith("#")]:
            g = pg.read(os.path.join(DC.ROOT, pre + line[0]))
            if len(line) > 1:
                s, t, ok = read_start(g, os.path.join(DC.ROOT, pre + line[1]))
                if ok: st.inc("starts_valid"); run_game(g, s, t, st, f"{line[0]}#start")
                else: st.inc("starts_INVALID_skipped")
            for r in range(runs):
                if r == 0: s, t = Engine(g).initial("best"), Engine(dual(g)).initial("best")
                else: s, t = [rng.choice(g.succ[v]) for v in range(g.n)], [rng.choice(g.succ[v]) for v in range(g.n)]
                run_game(g, list(s), list(t), st, f"{line[0]}#{r}")
            if os.environ.get("PROGRESS"): print("DONE-FILE", line[0], flush=True)
    print("MODE", " ".join(a), "MAXT", MAXT, "BF", BF)
    for k in sorted(st.c): print(f"{k}: {st.c[k]}")
    for k in sorted(st.mx): print(f"max {k}: {st.mx[k]}")
    keys = ("XIPLAY", "XW", "XIMON", "LCT", "WMON", "RSUB", "FWR", "FWP", "A2", "C0", "LSP", "LSP_opt", "LSP_succ", "XSIL", "CIR1", "CIR2",
            "CIR3", "REPSUB", "GC", "GTOK", "GCE", "GCS", "INC", "DESC", "CYC", "T2G", "RED", "BF")
    bad = sum(st.c.get(k, 0) for k in keys)
    print("RESULT", "PASS" if bad == 0 else "FAIL", "violations", bad)


if __name__ == "__main__":
    main()
