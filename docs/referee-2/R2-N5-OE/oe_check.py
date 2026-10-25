#!/usr/bin/env python3
"""REFEREE-2 successor 6 (Opus 5.5, D15): mechanical check of packet P-N5-OE (docs/new/P-N5-OE-box32.md sha1 adeccd89 @ trunk 361d18c).
Own code on my lane's R2-N5-LP/lp_check.py and R2-N5-FB/fb_check.py (SPEC run asserted = n5.run; Xi_k from si.py's Engine; W, R, levels,
COARSE, gate levels, M_k computed from the definitions). No lane box32 script is run or imported.
PHASE = a maximal run of transitions with lambda_Xi and tau constant (the packet's definition). C^1O inputs assert exactly one Odd vertex
with out-degree > 1 (fb_check.one_odd).
Checks:
  ULOC  Lemma U-loc at every (in-phase transition, v), with the SMALLEST admissible L (max level of the relevant changes on v's
        H_{k+1}-path before its first visit of c = lambda(v); BOT if none); also on general games.
  CAP1  at every state: lambda(o) != o => sigma-bar(o) is a full Xi-minimiser over succ(o); lambda(o) = o: non-minimiser cases counted.
  OE    in-phase transitions with R_k = R_{k+1}: O_k <= E_k. Literal "in particular": E_k = BOT => no relevant sigma-bar(o) change at all
        (level-BOT tie moves counted separately). At crossings: O_k > E_k counted.
  STEPS the proof's intermediate facts at every relevant sigma-bar(o) change (crossings included where the hypotheses hold):
        S2 x1's H_{k+1}-path to c avoids o; S3 (H1) x0 in F_k and x0's H_{k+1}-play avoids o; S4 (not H1) P(Xi_k(x0)) = P(Xi_{k+1}(x1)) = 0.
  OX    per C^1O phase: (i) eps <= X and every eps transition is a crossing; (ii) J <= X and every non-tame transition is a crossing;
        (iii) rho <= 2f + 2X + K; (iv) f <= n_E(2n-1)(X+1) + X; (v) T <= (m-n+1)((n+1)(2f+2X+K+1)n(n-1) + X + 1).
Usage: oe_check.py general N nmin nmax seed | c1o N nmin nmax seed | inst game.pg [runs]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-LP"))
import lp_check as LP
F = LP.F; RC = F.RC; lpg = F.lpg; INF, BOT, lev, coarse = F.INF, F.BOT, F.lev, F.coarse

def path_to(Hf, v, c):
    """v's play in the functional graph Hf up to (excluding) its first visit of c."""
    out, x, seen = [], v, set()
    while x != c:
        if x in seen: return None
        seen.add(x); out.append(x); x = Hf[x]
    return out

def play_visits(Hf, v, o):
    x, seen = v, set()
    while x not in seen:
        if x == o: return True
        seen.add(x); x = Hf[x]
    return False

def is_min(E, Xi, x, succ):
    kx = E.key(Xi[x])
    return all(kx <= E.key(Xi[y]) for y in succ)

def check_run(g, s, t, st, name, o):
    states, fbs, E, Ed = F.run_n5(g, s, t)
    if (len(fbs), sum(fbs)) != F.n5.run(g, "n5", ({v: s[v] for v in range(g.n) if g.owner[v] == 0},
                                                   {v: t[v] for v in range(g.n) if g.owner[v] == 1}))[:2]:
        st.bad(f"{name} run differs from n5.run")
    A = [F.analyse(g, E, Ed, a, b, o) for a, b in states]
    for k, S in enumerate(A): LP.extra(g, E, S, states[k][0], states[k][1], o)
    T = len(fbs)
    st.c["runs"] += 1; st.c["transitions"] += T
    if o is not None:
        so = sorted(set(g.succ[o]))
        for k, S in enumerate(A):
            m_ = is_min(E, S.Xi, S.sbar[o], so)
            if S.lam[o] != o:
                st.c["CAP1_checks(lam(o)!=o)"] += 1
                if not m_: st.bad(f"{name} CAP1: sbar(o) not a full minimiser at state {k}")
            else:
                st.c["CAP1_info_states(lam(o)=o)"] += 1
                if not m_: st.c["CAP1_info_nonminimiser(lam(o)=o)"] += 1
    inph = [A[k].lam == A[k + 1].lam and states[k][1] == states[k + 1][1] for k in range(T)]
    k = 0
    while k < T:
        if not inph[k]: k += 1; continue
        j = k
        while j < T and inph[j]: j += 1
        phase(g, E, A, states, fbs, k, j, st, f"{name}[{k},{j})", o)
        k = j

def phase(g, E, A, states, fbs, k0, k1, st, name, o):
    n = g.n; m = sum(len(E.succ[v]) for v in range(n)); nE = [v for v in range(n) if g.owner[v] == 0]
    st.c["phases"] += 1
    Ls, rel, epsk = [], [], []
    for k in range(k0, k1):
        A0, A1 = A[k], A[k + 1]
        R = LP.relevant(g, A0, A1, states[k], states[k + 1])
        L = max([x[1] for x in R], default=BOT)
        Ls.append(L); rel.append(L != BOT)
        st.c["transitions_in_phase"] += 1
        # ---- U-loc with the smallest admissible L, every v
        rl = {}
        for v, lv_, kind in R: rl[v] = max(rl.get(v, BOT), lv_)
        for v in range(n):
            c = A0.lam[v]
            p = path_to(A1.H, v, c)
            if p is None: st.bad(f"{name} ULOC: no path from {v} to c={c} at {k}"); continue
            # every changed successor on the prefix must be a relevant change (own cycle nodes are never on it)
            for x in p:
                if A1.H[x] != A0.H[x] and x not in rl: st.bad(f"{name} ULOC: non-relevant change on prefix at {k} v={v} x={x}")
            Lv = max([rl[x] for x in p if x in rl], default=BOT)
            st.c["ULOC_checks"] += 1
            if Lv < L: st.c["ULOC_strictly_below_L_k"] += 1
            if coarse(A1.Xi[v], Lv) != coarse(A0.Xi[v], Lv): st.bad(f"{name} ULOC at {k} v={v} Lv={Lv}")
        if R and all(x[2] == "O" for x in R if x[1] == L) and L != BOT: epsk.append(k)
        if o is None: continue
        # ---- OE
        cross = A0.Rbar != A1.Rbar
        Ek = max([x[1] for x in R if x[2] == "E"], default=BOT)
        Oc = [x for x in R if x[2] == "O"]
        assert all(x[0] == o for x in Oc)
        Ok = Oc[0][1] if Oc else BOT
        if cross:
            st.c["OE_crossings"] += 1
            if Ok > Ek: st.c["OE_crossings_with_O>E"] += 1
        else:
            st.c["OE_checks(no crossing)"] += 1
            if Oc: st.c["OE_relevant_sbar(o)_changes(no crossing)"] += 1
            if Ok > Ek: st.bad(f"{name} OE: O_k={Ok} > E_k={Ek} at {k} (no crossing)")
            if Ek == BOT and Oc:
                st.c["OE_in_particular_literal_fails(level-BOT tie move)"] += 1
                st.ex.setdefault("tie", f"{name} k={k}")
        # ---- proof steps
        if Oc:
            x0, x1 = A0.sbar[o], A1.sbar[o]; c = A0.lam[o]
            p1 = path_to(A1.H, x1, c)
            st.c["S2_checks"] += 1
            if p1 is None or o in p1: st.bad(f"{name} S2: x1's H_k+1-path to c visits o at {k}")
            if A0.H1:
                st.c["S3_checks(H1 at k)"] += 1
                if not cross and not A1.H1: st.bad(f"{name} TC(i): H1 changes off a crossing at {k}")
                if x0 in A0.Rbar or play_visits(A0.H, x0, o): st.bad(f"{name} S3: x0 in R_k or H_k-play visits o at {k}")
                if not cross and play_visits(A1.H, x0, o): st.bad(f"{name} S3: x0's H_k+1-play visits o at {k}")
            else:
                st.c["S4_checks(not H1 at k)"] += 1
                if not cross: st.c["S4_checks_offcross"] += 1
                if A0.Xi[x0][1] != 0: st.bad(f"{name} S4: P(Xi_k(x0)) nonempty at {k}")
                if not cross:
                    if A1.H1: st.bad(f"{name} TC(i): H1 changes off a crossing at {k}")
                    if A1.Xi[x1][1] != 0: st.bad(f"{name} S4: P(Xi_k+1(x1)) nonempty at {k}")
    if o is None: return
    # ---- Corollary OX
    Tp = k1 - k0; Trel = sum(rel)
    crossk = {k for k in range(k0, k1) if A[k].Rbar != A[k + 1].Rbar}
    X = len(crossk); f = sum(fbs[k0:k1]); nEc = len(nE)
    relk = [k0 + i for i in range(Tp) if rel[i]]
    rho = sum(1 for i in range(len(relk) - 1) if Ls[relk[i + 1] - k0] > Ls[relk[i] - k0])
    K = 0
    for i in range(len(relk) - 1):
        k, kp = relk[i], relk[i + 1]
        if any(fbs[x] for x in range(k, kp + 1)) or any(x in crossk for x in range(k, kp + 1)): continue
        Lk = Ls[k - k0]
        if any(kind == "E" and lv_ > Lk for y, lv_, kind in LP.relevant(g, A[kp], A[kp + 1], states[kp], states[kp + 1])): K += 1
    nontame = [k for k in range(k0, k1) if any(coarse(A[k + 1].Xi[v], A[k].M) != coarse(A[k].Xi[v], A[k].M) for v in range(n))]
    J = len(nontame); eps = len(epsk)
    st.c["OX_phases"] += 1
    for k in epsk:
        if k not in crossk: st.bad(f"{name} OX(i): eps transition {k} is not a crossing")
    for k in nontame:
        st.c["nontame_transitions"] += 1
        if k not in crossk: st.bad(f"{name} OX(ii): non-tame transition {k} is not a crossing")
    if eps > X: st.bad(f"{name} OX(i) eps {eps} > X {X}")
    if J > X: st.bad(f"{name} OX(ii) J {J} > X {X}")
    if rho > 2 * f + 2 * X + K: st.bad(f"{name} OX(iii) rho {rho} > {2 * f + 2 * X + K}")
    if f > nEc * (2 * n - 1) * (X + 1) + X: st.bad(f"{name} OX(iv) f {f}")
    if Tp > (m - n + 1) * ((n + 1) * (2 * f + 2 * X + K + 1) * n * (n - 1) + X + 1): st.bad(f"{name} OX(v) T {Tp}")
    st.c["eps_total"] += eps; st.c["J_total"] += J; st.c["rises_total"] += rho; st.c["K_total"] += K; st.c["f_total"] += f
    st.mx["max_J"] = max(st.mx["max_J"], J); st.mx["max_X"] = max(st.mx["max_X"], X); st.mx["max_eps"] = max(st.mx["max_eps"], eps)
    st.mx["max_T_phase"] = max(st.mx["max_T_phase"], Tp); st.mx["max_rho"] = max(st.mx["max_rho"], rho)
    if J and J == X: st.c["phases_J_eq_X>0"] += 1
    st.mx["max(J-X)+1000"] = max(st.mx["max(J-X)+1000"], J - X + 1000); st.mx["max(eps-X)+1000"] = max(st.mx["max(eps-X)+1000"], eps - X + 1000)

def main():
    st = F.Stats(); mode = sys.argv[1]
    if mode in ("general", "c1o"):
        N, nmin, nmax, seed = map(int, sys.argv[2:6]); rng = random.Random(seed)
        for i in range(N):
            if mode == "general": g = F.rand_general(rng, rng.randint(nmin, nmax)); o = None
            else:
                rg, o = RC.rand_game(rng, rng.randint(nmin, nmax), cyc=rng.random() < 0.7); g = F.to_lpg(rg); assert F.one_odd(g) == o
            s, t = F.start(g, rng, rng.random() < 0.6)
            check_run(g, s, t, st, f"{mode}{seed}#{i}", o)
    else:
        path = sys.argv[2]; runs = int(sys.argv[3]) if len(sys.argv) > 3 else 1
        g = lpg.parse("".join(l for l in open(path) if not l.lstrip().startswith("%"))); o = F.one_odd(g); rng = random.Random(7)
        for r in range(runs):
            s, t = F.start(g, rng, r > 0); check_run(g, s, t, st, f"{os.path.basename(path)}#{r}", o)
    F.report(st)
    for k, v in st.ex.items(): print("example", k, v)

if __name__ == "__main__":
    main()
