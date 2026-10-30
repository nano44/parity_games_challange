#!/usr/bin/env python3
r"""REFEREE-2 successor 21 (Opus 5.5, D15): own check of P-N5-GAP (docs/new/P-N5-GAP-box69.md, sha1 d67f8e04 @ l-new 28ceeadc).
State loop: my lane's R2-N5-DUAL/dual_check.Runner (SPEC N5 on si.py, read-only); helpers from my R2-N5-FRAME/frame_check.py. Lane code
(experiments/new/box66-68) is NOT imported. Definitions written from the packet's §1.
W_t := my play value of the (sigma_t, tau_t)-plays; Xi_t from si.py; Z_t := {v : Xi_t(v) != W_t(v)}.
Checks (each must be 0):
  XW    Xi_t <= W_t pointwise, every state
  WM    W-MON: at every S4a step, W^{tau_t}(sigma_{t+1}) >= W_t pointwise
  FBW   FB-W: at every tau-fixed Even fallback, W_{k+1} <= W_k pointwise (and tau kept)
  OO    OPT-OFF: (a) at every S4a step, rho := sigma_{t+1} in H_t (frame tau_t); (b) mode onep: random one-player games G_tau with rho :=
        Even's optimal reply (si.py on G^d), H := G_tau. Every Even v not its own cycle node, every (v, c) in H: Omega(c) <= Omega(rho v).
        Census of the proof's cases: OO_case1 (c's play avoids v), OO_case2 (visits v, u not on pi), OO_case2u (visits v, u ON pi: the
        sub-case the packet's Case 2 text does not cover), OO_case2u_S0_ueven (and S empty with u even: the packet's "so u is odd" is false)
  WS    W-SUCC per step inside a piece (v not its own W-cycle node at t + 1)
  LW    LATE-W: every leave s -> s+1 in a piece Q, every later state t' of Q with (v, c) blocked and v off its own W-cycle on [s+1, t']:
        W_{t'}(c) > W_{s+1}(c)
  LP    LATE-PIECE: #re-blocked late adoptions of (v, c) in Q <= 1 + WCH_Q(c) + CL_Q(v, c) (t' := the EARLIEST blocked state of the window)
  GM    GAP-MON at every tau-fixed Even fallback; SI SW-IN; ZF Z-FLAT (a)-(d); RW REOPEN-W at every in-phase S4a step; RC REOPEN-CHARGE
  GR    Theorem GAP-RED per phase: f_P <= |Z_a| + RO_P + ZF_P <= n + sum_v WCH^S4a_P(v) + ZF_P
Controls (X_*): X_OO_own (OPT-OFF at own-cycle-node v fails), X_GM_s4a (Z grows at an S4a step), X_SI_own (a switched own-Xi-cycle-node
vertex outside Z_k at a fallback), X_FBLIN (f_P > n), X_LP_nore (late adoptions that are NOT re-blocked; the corollary does not count them).
Usage: gap_check.py random N nmin nmax seed [starts] | files list.txt [runs [prefix]] | onep N nmin nmax seed"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-FRAME"))
import frame_check as F
DC, pg, Engine, dual = F.DC, F.pg, F.Engine, F.dual
play, pval, blocked_at = F.play, F.pval, F.blocked_at
MAXT = int(os.environ.get("MAXT", "3000"))
St = F.St


def Wval(E, g, sg, tu):
    nx = [sg[v] if g.owner[v] == 0 else tu[v] for v in range(g.n)]
    return [pval(E, nx, v) for v in range(g.n)]


def optoff(g, E, nx, Om, Hd, st, tag):
    """nx: successor map of the one-player play (Even rho, Odd tau); Om: its values; Hd: Even v -> allowed successors."""
    K = E.key
    for v, ys in Hd.items():
        for c in ys:
            ok = K(Om[c]) <= K(Om[nx[v]])
            if Om[v][0] == v:
                if not ok: st.inc("X_OO_own")
                continue
            st.inc("OO_checks")
            if not ok: st.bad("OO", f"{tag} v={v} c={c}")
            path, j = play(nx, c)
            if v not in path: st.inc("OO_case1"); continue
            u = Om[v][0]; pi = path[:path.index(v)]
            if u in pi:
                st.inc("OO_case2u")
                S = [y for y in pi + [v] if E.rank[y] > E.rank[u]]
                if not S and g.prio[u] % 2 == 0: st.inc("OO_case2u_S0_ueven")
            else: st.inc("OO_case2")


def run_game(g, s, t, st, name, rng):
    n = g.n; E = Engine(g); K = E.key
    states, fbs = DC.Runner(g).run(list(s), list(t), cap=MAXT)
    T = len(states) - 1; st.inc("runs"); st.inc("transitions", T)
    Even = [v for v in range(n) if g.owner[v] == 0]
    I = []
    for sg, tu in states:
        xe, _ = E.evaluate(tuple(sg[v] if g.owner[v] == 0 else -1 for v in range(n)))
        xi = [tuple(z) for z in xe]; Is = set(E.improving(tuple(sg), xe)); W = Wval(E, g, sg, tu)
        I.append(dict(sg=sg, tu=tu, xi=xi, Is=Is, W=W, Z={v for v in range(n) if xi[v] != W[v]}, lam=tuple(z[0] for z in xi)))
    for k, A in enumerate(I):
        st.inc("XW_checks")
        if any(K(A["xi"][v]) > K(A["W"][v]) for v in range(n)): st.bad("XW", f"{name}@{k}")
    tch = [I[k + 1]["tu"] != I[k]["tu"] for k in range(T)]
    s4a = [(not fbs[k]) and I[k + 1]["sg"] != I[k]["sg"] for k in range(T)]
    efb = [bool(fbs[k]) and bool(I[k]["Is"]) for k in range(T)]
    H = [{v: sorted({I[k]["sg"][v]} | {w for x, w in I[k]["Is"] if x == v}) for v in Even} for k in range(T + 1)]
    for k in range(T):
        A, B = I[k], I[k + 1]
        if s4a[k]:
            Wn = Wval(E, g, B["sg"], A["tu"]); st.inc("WM_checks")
            if any(K(Wn[x]) < K(A["W"][x]) for x in range(n)): st.bad("WM", f"{name}@{k}")
            nx = [B["sg"][v] if g.owner[v] == 0 else A["tu"][v] for v in range(n)]
            optoff(g, E, nx, Wn, H[k], st, f"{name}@{k}")
        if efb[k]:
            st.inc("FBW_checks")
            if tch[k] or any(K(B["W"][x]) > K(A["W"][x]) for x in range(n)): st.bad("FBW", f"{name}@{k}")
            # GAP-MON
            st.inc("GM_checks")
            if not B["Z"] <= A["Z"]: st.bad("GM", f"{name}@{k} Z grows")
            for v in set(range(n)) - A["Z"]:
                if B["xi"][v] != A["xi"][v] or B["W"][v] != A["W"][v]: st.bad("GM", f"{name}@{k} v={v} changes outside Z")
            # SW-IN
            for v in Even:
                if B["sg"][v] == A["sg"][v]: continue
                own = A["xi"][v][0] == v or B["xi"][v][0] == v
                if own:
                    if v not in A["Z"]: st.inc("X_SI_own")
                    continue
                st.inc("SI_checks")
                if not (K(B["xi"][v]) > K(A["xi"][v]) and v in A["Z"]): st.bad("SI", f"{name}@{k} v={v}")
            if B["Z"] == A["Z"]:
                st.inc("ZF_checks")
                if any(K(B["xi"][x]) < K(A["xi"][x]) for x in range(n)): st.bad("ZF", f"{name}@{k} Xi falls")
                if any(B["xi"][v] == B["W"][v] for v in A["Z"]): st.bad("ZF", f"{name}@{k} (d)")
        elif s4a[k] and not tch[k] and A["lam"] == B["lam"]:
            # REOPEN-W (in-phase S4a step)
            for v in B["Z"] - A["Z"]:
                st.inc("RW_checks")
                if not K(B["W"][v]) > K(A["W"][v]): st.bad("RW", f"{name}@{k} v={v}")
        if s4a[k] and (B["Z"] - A["Z"]): st.inc("X_GM_s4a")
    # pieces: W-SUCC, LATE-W, LATE-PIECE
    pieces = []; a = 0
    for k in range(T + 1):
        if k == T or not (s4a[k] and not tch[k]): pieces.append((a, k)); a = k + 1
    own = lambda t2, v: I[t2]["W"][v][0] == v
    for (qa, qb) in pieces:
        BL = {t2: blocked_at(g, E, I[t2]) for t2 in range(qa, qb + 1)}
        for t2 in range(qa, qb):
            A, B = I[t2], I[t2 + 1]
            for v in Even:
                if not own(t2 + 1, v):
                    st.inc("WS_checks")
                    if K(B["W"][B["sg"][v]]) < K(A["W"][A["sg"][v]]): st.bad("WS", f"{name}@{t2} v={v}")
        for v in Even:
            for c in sorted(set(g.succ[v])):
                leaves = [s_ for s_ in range(qa, qb) if I[s_]["sg"][v] == c and I[s_ + 1]["sg"][v] != c]
                for s_ in leaves:
                    for tp in range(s_ + 1, qb + 1):
                        if any(own(x, v) for x in range(s_ + 1, tp + 1)): break
                        if (v, c) in BL[tp]:
                            st.inc("LW_checks")
                            if not K(I[tp]["W"][c]) > K(I[s_ + 1]["W"][c]): st.bad("LW", f"{name} v={v} c={c} s={s_} t'={tp}")
                ads = [u for u in range(qa, qb) if I[u]["sg"][v] != c and I[u + 1]["sg"][v] == c]
                reb = []; nore = 0
                for u in ads:
                    if not any((v, c) in BL[x] for x in range(qa, u + 1)): continue   # not late
                    ls = [s_ for s_ in leaves if s_ + 1 <= u]
                    if not ls: reb.append((u, None)); continue
                    s_ = ls[-1]; tps = [x for x in range(s_ + 1, u + 1) if (v, c) in BL[x]]
                    if tps: reb.append((u, (s_, tps[0])))
                    else: nore += 1
                st.inc("X_LP_nore", nore)
                if not reb: continue
                wch = sum(1 for x in range(qa, qb) if I[x + 1]["W"][c] != I[x]["W"][c])
                cl = sum(1 for i, (u, w) in enumerate(reb) if i > 0 and w is not None and any(own(x, v) for x in range(w[0] + 1, w[1] + 1)))
                st.inc("LP_checks"); st.inc("LP_reblocked", len(reb))
                if len(reb) > 1 + wch + cl: st.bad("LP", f"{name} Q[{qa},{qb}] v={v} c={c} reb {len(reb)} WCH {wch} CL {cl}")
    # phases: REOPEN-CHARGE, GAP-RED
    phases = []; a = 0
    for k in range(T + 1):
        if k == T or (I[k + 1]["lam"], I[k + 1]["tu"]) != (I[a]["lam"], I[a]["tu"]): phases.append((a, k)); a = k + 1
    for (pa, pb) in phases:
        fP = sum(1 for k in range(pa, pb) if fbs[k])
        for k in range(pa, pb):
            if fbs[k] and not efb[k]: st.bad("GR", f"{name}@{k} in-phase fallback not tau-fixed Even")
            if not fbs[k] and not s4a[k]: st.bad("GR", f"{name}@{k} in-phase transition neither S4a nor fallback")
        ZF = sum(1 for k in range(pa, pb) if fbs[k] and I[k + 1]["Z"] == I[k]["Z"])
        RO = sum(len(I[k + 1]["Z"] - I[k]["Z"]) for k in range(pa, pb) if s4a[k])
        WS = sum(1 for k in range(pa, pb) if s4a[k] for v in range(n) if I[k + 1]["W"][v] != I[k]["W"][v])
        st.inc("GR_checks")
        if RO > WS: st.bad("RC", f"{name} P[{pa},{pb}] RO {RO} > {WS}")
        if not (fP <= len(I[pa]["Z"]) + RO + ZF <= n + WS + ZF): st.bad("GR", f"{name} P[{pa},{pb}] f {fP} Z_a {len(I[pa]['Z'])} RO {RO} ZF {ZF}")
        if fP > n: st.inc("X_FBLIN")
        st.mxu("max_fP", fP); st.mxu("max_ZF", ZF); st.mxu("max_RO", RO)
        st.inc("ZF_total", ZF); st.inc("inphase_fallbacks", fP)


def onep(N, nmin, nmax, seed, st):
    rng = random.Random(seed)
    for i in range(N):
        g = DC.rand_game(rng, rng.randint(nmin, nmax), "kO"); n = g.n; E = Engine(g); Ed = Engine(dual(g))
        for r in range(3):
            tu = [rng.choice(g.succ[v]) if g.owner[v] == 1 else -1 for v in range(n)]
            _, best = Ed.evaluate(tuple(tu))   # Even's optimal reply to tau (G^d-Odd optimum), si.py
            rho = [best[v] if g.owner[v] == 0 else tu[v] for v in range(n)]
            Om = [pval(E, rho, v) for v in range(n)]
            # rho optimal: check F1 against random Even strategies too
            for _ in range(3):
                alt = [rng.choice(g.succ[v]) if g.owner[v] == 0 else tu[v] for v in range(n)]
                Oa = [pval(E, alt, v) for v in range(n)]; st.inc("OO_F1_checks")
                if any(E.key(Oa[x]) > E.key(Om[x]) for x in range(n)): st.bad("OO", f"onep{seed}:{i} rho not optimal")
            optoff(g, E, rho, Om, {v: sorted(set(g.succ[v])) for v in range(n) if g.owner[v] == 0}, st, f"onep{seed}:{i}")
            st.inc("onep_games")


def main():
    st = St(); a = sys.argv[1:]; rng = random.Random(5151)
    if a[0] == "onep":
        onep(*map(int, a[1:5]), st)
    elif a[0] == "random":
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
            g = pg.read(os.path.join(DC.ROOT, pre + line[0]))
            if len(line) > 1:
                s, t = list(Engine(g).initial("best")), list(Engine(dual(g)).initial("best"))
                for l2 in open(os.path.join(DC.ROOT, pre + line[1])):
                    ps = l2.split()
                    if ps and ps[0] in ("SIGMA0", "TAU0"):
                        for kv in ps[1:]:
                            v, w = map(int, kv.split(":")); (s if ps[0] == "SIGMA0" else t)[v] = w
                if all((s if g.owner[v] == 0 else t)[v] in g.succ[v] for v in range(g.n)):
                    st.inc("starts_valid"); run_game(g, s, t, st, f"{line[0]}#start", rng)
                else: st.inc("starts_INVALID_skipped")
            if os.environ.get("STARTORS3") and len(line) > 1 and st.c.get("starts_valid"): 
                if os.environ.get("PROGRESS"): print("DONE-FILE", line[0], flush=True)
                continue
            for r in range(runs):
                if r == 0: s, t = Engine(g).initial("best"), Engine(dual(g)).initial("best")
                else: s, t = [rng.choice(g.succ[v]) for v in range(g.n)], [rng.choice(g.succ[v]) for v in range(g.n)]
                run_game(g, list(s), list(t), st, f"{line[0]}#{r}", rng)
            if os.environ.get("PROGRESS"): print("DONE-FILE", line[0], flush=True)
    print("MODE", " ".join(a), "MAXT", MAXT)
    for k in sorted(st.c): print(f"{k}: {st.c[k]}")
    for k in sorted(st.mx): print(f"max {k}: {st.mx[k]}")
    keys = ("XW", "WM", "FBW", "OO", "WS", "LW", "LP", "GM", "SI", "ZF", "RW", "RC", "GR")
    bad = sum(st.c.get(k, 0) for k in keys)
    print("RESULT", "PASS" if bad == 0 else "FAIL", "violations", bad)


if __name__ == "__main__":
    main()
