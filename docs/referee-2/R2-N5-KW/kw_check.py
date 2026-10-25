#!/usr/bin/env python3
r"""REFEREE-2 successor 12 (Opus 5.5, D15): mechanical check of packet P-N5-KW (docs/si/P-N5-KW-box15.md sha1 c0b0111f, with
docs/si/P-N5-KW-addendum-box15.md sha1 8d6bfb3c). Own code on R2-N5-OUT/out_check.py (traces own | rand | spec), R2-N5-FRZ, R2-N5-RE.
No lane script (experiments/si/kw15/*.py) is run or imported; lane .pg files are inputs only. One Odd choice vertex asserted.
Objects (packet §1): phase = run of states with (lambda_Xi, tau) constant; R = Rbar (o included), r = |R|; stretch = maximal run of states
of a phase with R, theta, w constant; run = maximal run of consecutive non-fallback transitions of a stretch (states k0..kT);
pi_v = v's (sigma, tau)-path before o (as a set); m* = the more relevant of c_theta, c_w; kappa(S) = S & V_{>m*}; kind (under not H2,
c_w != o): A iff c_w in pi_v. W-flat segment: consecutive non-fallback transitions of a stretch with W unchanged on R.
Checks:
  WONCE   consecutive in-phase S4a transitions k->k+1->k+2 with Xi_{k+1} = Xi_k: W_{k+2} = W_{k+1}.
  A0      at every stretch state, for v in R \ {o}: Xi(v) and W(v) equal the packet's prefix (+) terminal formulas.
  FACTA   (A-Xi), (A-W) above m*.   FACTB  every pair y, z in R with kappa(pi_y) != kappa(pi_z): Xi order = W order = kappa order.
  MON     kappa_k(x) <= kappa_{k+1}(x) along a run.   FRZU  kappa_t = kappa_{k0+r-1} for t >= k0 + r - 1 (records the freeze delay).
  LEN     after f0: (m* = c_theta) P(Xi) frozen on R, each v <= r-2 Xi-changes; (m* = c_w) P(W) frozen, each v <= r-2 W-changes;
          per run Xi-changing (resp. W-changing) transitions on R <= (r-1)^2.
  PAR     c_w more relevant than c_theta => c_w even (every state).      HPATH  c_w in P(Xi v) iff kind A (setting of H-PATH).
  KMONO   after f0 each v changes kind at most once, B -> A (setting of KIND-MONO).
  CASCB   in a W-flat segment of a not-H2, c_w != o stretch with no kind change, a kind-B Even v switches only at steps <= |pi_v| - 2.
  CWINT   between cut transitions (kind change or kind-B switch) of a run (not H2, c_w != o), c_w switches <= deg(c_w) - 1 times.
  ESEG    per W-flat segment Q after f0 (c_w > c_theta, not H2, c_w != o): (i') N_B outside kind-change transitions <= (e+1)(r-2) and
          the literal N_B (all kind-B-switch transitions) recorded; (ii) c_w switches <= Delta (N_cut + 1) with N_cut the union count;
          (iii) E <= (e+1)(Delta r + 1) - 1; (iv) switch transitions <= (E+1)(2r-3); (v) sum e(Q) <= r - 2 per run.
  RUN     per run, Xi-changing transitions on R <= the case bound ((a) (r-1)^2, (b) <= r^3, (c) <= 3 Delta r^4).
  KWS     per stretch, non-fallback W-changing transitions on R <= (f_st + 1)(1 + (r-1)^2 + |F| - 1).
  PHASE   per phase: T <= (m-n+1)(T_rel+1); T_rel <= S_o + N_Xi; N_Xi <= f + (N_st-1) + (X+1)(n-1) + (N_st+f) 3 Delta n^4;
          N_st <= 1 + X + Theta + W_ch; X <= (f+1)(n-1) + f + X_SN; W_ch <= (f+X+1) n^2; S_o <= d_o (Theta+1); the final bound.
Records: post-freeze kind changes, post-freeze c_w switches, kind-B switches in W-flat segments, max freeze delay, CASC-B slack.
Mutations (KW_MUT): frz0 (freeze index k0 instead of k0+r-1), casc (CASC-B bound |pi_v| - 3), par (PAR asks for c_w odd).
Usage: kw_check.py random N nmin nmax seed [own|rand|spec] | inst game.pg [runs] [own|rand|spec]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-OUT"))
import out_check as OC
FC = OC.FC; RC = FC.RC
INF, BOT, lev = FC.INF, FC.BOT, FC.lev
MUT = os.environ.get("KW_MUT", "")

def route(S, v, o):
    p, x, seen = [], v, set()
    while x != o:
        if x in seen: return None
        seen.add(x); p.append(x); x = S.f[x]
    return p

def oplus_path(g, path, term):
    """iterated (V1): path (list, first vertex first) (+) terminal value"""
    c, P, l = term
    P = set(P)
    for u in reversed(path):
        if g.rank[u] > g.rank[c]: P.add(u)
        l += 1
    return (c, frozenset(P), l)

def korder_le(g, A, B):
    """A <= B in SPEC S1's path-set order (top of the symmetric difference decides)"""
    if A == B: return True
    t = max(A ^ B, key=lambda u: g.rank[u])
    return (t in B) == bool(g.even[t])

def ctx(g, o, S):
    """per-state objects of §1"""
    C = {}
    R = S.Rbar; C["R"] = R
    C["pi"] = {v: route(S, v, o) for v in R}
    C["cth"] = S.theta[0]; C["cw"] = S.W[o][0]
    C["mstar"] = C["cth"] if g.rank[C["cth"]] >= g.rank[C["cw"]] else C["cw"]
    hi = lambda X: frozenset(u for u in X if g.rank[u] > g.rank[C["mstar"]])
    C["hi"] = hi
    C["kap"] = {v: hi(C["pi"][v]) for v in R}
    C["kindset"] = (not S.H2) and C["cw"] != o
    C["kind"] = {v: ("A" if C["cw"] in C["pi"][v] else "B") for v in R if v != o} if C["kindset"] else {}
    return C

def check_state(g, o, S, C, st, name):
    R, pi, cth, cw = C["R"], C["pi"], C["cth"], C["cw"]
    st.c["states_checked"] += 1
    # PAR
    if g.rank[cw] > g.rank[cth]:
        st.c["PAR_states_cw_above_cth"] += 1
        if (not g.even[cw]) != (MUT == "par"): st.bad(f"{name} PAR c_w odd")
    # A0 / FACTA
    for v in R:
        if v == o: continue
        p = pi[v]
        # honest: prefix of pi_v up to the first vertex in {o, c_theta}
        if cth in p and cth != o:
            pre = p[:p.index(cth)]; tX = (cth, frozenset(), 0)
        else:
            pre = p; tX = S.theta
        if oplus_path(g, pre, tX) != S.Xi[v]: st.bad(f"{name} A0(Xi) at {v}")
        if cw in p and cw != o:
            preW = p[:p.index(cw)]; tW = (cw, frozenset(), 0)
        else:
            preW = p; tW = S.w
        if oplus_path(g, preW, tW) != S.W[v]: st.bad(f"{name} A0(W) at {v}")
        CX = C["hi"](S.theta[1]) if S.H1 else frozenset()
        CW = C["hi"](S.w[1]) if S.H2 else frozenset()
        if C["hi"](S.Xi[v][1]) != C["kap"][v] | CX or C["kap"][v] & CX: st.bad(f"{name} FACTA(Xi) at {v}")
        if C["hi"](S.W[v][1]) != C["kap"][v] | CW or C["kap"][v] & CW: st.bad(f"{name} FACTA(W) at {v}")
        st.c["A0_checks"] += 1
        # HPATH
        if C["kindset"] and g.rank[cw] > g.rank[cth]:
            st.c["HPATH_checks"] += 1
            if (cw in S.Xi[v][1]) != (C["kind"][v] == "A"): st.bad(f"{name} HPATH at {v}")
    # FACTB
    Rl = sorted(R)
    for i, y in enumerate(Rl):
        for z in Rl[i + 1:]:
            if C["kap"][y] == C["kap"][z]: continue
            st.c["FACTB_pairs"] += 1
            a = g.cmp(S.Xi[y], S.Xi[z]); b = g.cmp(S.W[y], S.W[z])
            k = -1 if korder_le(g, C["kap"][y], C["kap"][z]) else 1
            if not (a == b == k): st.bad(f"{name} FACTB {y},{z}")

def check_run(g, o, A, fbs, st, name):
    n = g.n; T = len(fbs); m = sum(len(set(g.succ[v])) for v in range(n)); Delta = max(len(set(g.succ[v])) for v in range(n))
    d_o = len(set(g.succ[o]))
    st.c["runs"] += 1; st.c["states"] += len(A)
    Cs = [ctx(g, o, S) for S in A]
    ph = [OC.key(S, o) for S in A]
    for k in range(len(A)): check_state(g, o, A[k], Cs[k], st, f"{name}@{k}")
    # WONCE
    for k in range(T - 1):
        if fbs[k] or fbs[k + 1] or not (ph[k] == ph[k + 1] == ph[k + 2]): continue
        if A[k + 1].Xi == A[k].Xi:
            st.c["WONCE_checks"] += 1
            if A[k + 2].W != A[k + 1].W: st.bad(f"{name} WONCE at {k}")
    # phases
    k = 0
    while k < len(A):
        e = k
        while e + 1 < len(A) and ph[e + 1] == ph[k]: e += 1
        check_phase(g, o, A, fbs, Cs, k, e, n, m, Delta, d_o, st, name)
        k = e + 1

def sw(A, k):
    """Even vertices switched at k -> k+1"""
    return {v for v in range(len(A[k].sg)) if A[k].sg[v] != A[k + 1].sg[v]}

def check_phase(g, o, A, fbs, Cs, a, b, n, m, Delta, d_o, st, name):
    st.c["phases"] += 1
    def stkey(t): return (frozenset(A[t].Rbar), A[t].theta, A[t].w)
    # stretches
    stretches = []; s = a
    while s <= b:
        e = s
        while e + 1 <= b and stkey(e + 1) == stkey(s): e += 1
        stretches.append((s, e)); s = e + 1
    f = sum(fbs[t] for t in range(a, b))
    for (s0, s1) in stretches:
        check_stretch(g, o, A, fbs, Cs, s0, s1, n, Delta, st, name)
    # PHASE quantities
    Tn = b - a
    X = sum(1 for t in range(a, b) if A[t].Rbar != A[t + 1].Rbar)
    Theta = sum(1 for t in range(a, b) if A[t].theta != A[t + 1].theta)
    Wch = sum(1 for t in range(a, b) if A[t].w != A[t + 1].w)
    Nst = len(stretches)
    XSN = sum(1 for t in range(a, b) if not fbs[t] and A[t].Rbar != A[t + 1].Rbar and Cs[t]["cw"] == Cs[t]["cth"])
    NXi = sum(1 for t in range(a, b) if A[t].Xi != A[t + 1].Xi)
    # relevant transitions (R27 setting)
    Trel = 0; So = 0
    for t in range(a, b):
        S, S1 = A[t], A[t + 1]; levs = []; oddrel = False
        for y in sw(A, t):
            if S.lamX[y] != y: levs.append(lev(g, S.Xi[S.sg[y]], S.Xi[S1.sg[y]]))
        if S.sbar != S1.sbar and S.lamX[o] != o:
            l_ = lev(g, S.Xi[S.sbar], S.Xi[S1.sbar]); levs.append(l_)
            if l_ != BOT: oddrel = True
        Lk = max(levs, default=BOT)
        if Lk != BOT:
            Trel += 1
            if oddrel: So += 1
    TH = n * n + 2 * n - 1
    st.c["PHASE_checked"] += 1
    if Tn > (m - n + 1) * (Trel + 1): st.bad(f"{name} PHASE LP")
    if Trel > So + NXi: st.bad(f"{name} PHASE T_rel")
    if NXi > f + (Nst - 1) + (X + 1) * (n - 1) + (Nst + f) * 3 * Delta * n ** 4: st.bad(f"{name} PHASE N_Xi")
    if Nst > 1 + X + Theta + Wch: st.bad(f"{name} PHASE N_st")
    if X > (f + 1) * (n - 1) + f + XSN: st.bad(f"{name} PHASE X")
    if XSN > 13 * (d_o + 1) * n ** 3 * (f + 1 + TH) + TH: st.bad(f"{name} PHASE X_SN")
    if Wch > (f + X + 1) * n * n: st.bad(f"{name} PHASE W_ch")
    if So > d_o * (Theta + 1): st.bad(f"{name} PHASE S_o")
    if Cs[a]["cth"] == o and Theta: st.bad(f"{name} PHASE Theta at c_theta = o")
    st.mxu("max_T_per_phase", Tn); st.mxu("max_Trel_per_phase", Trel); st.mxu("max_f_per_phase", f); st.mxu("max_stretches_per_phase", Nst)

def check_stretch(g, o, A, fbs, Cs, s0, s1, n, Delta, st, name):
    st.c["stretches"] += 1
    r = len(A[s0].Rbar); F = n - r
    fst = sum(fbs[t] for t in range(s0, s1))
    kw = sum(1 for t in range(s0, s1) if not fbs[t] and any(A[t].W[v] != A[t + 1].W[v] for v in A[t].Rbar))
    st.c["KWS_stretches"] += 1
    if kw > (fst + 1) * (1 + (r - 1) ** 2 + F - 1): st.bad(f"{name} KWS stretch {s0}")
    st.mxu("max_KW_per_stretch", kw)
    # runs
    t = s0
    while t < s1:
        if fbs[t]: t += 1; continue
        e = t
        while e + 1 < s1 and not fbs[e + 1]: e += 1
        check_srun(g, o, A, fbs, Cs, t, e + 1, r, Delta, st, name)   # states t .. e+1
        t = e + 1

def check_srun(g, o, A, fbs, Cs, k0, kT, r, Delta, st, name):
    st.c["RUNS_runs"] += 1
    R = A[k0].Rbar; C0 = Cs[k0]; cth, cw = C0["cth"], C0["cw"]
    hi = C0["hi"]
    f0 = k0 + (0 if MUT == "frz0" else r - 1)
    # MON and FRZU
    for t in range(k0, kT):
        for x in R:
            if not korder_le(g, hi(Cs[t]["pi"][x]), hi(Cs[t + 1]["pi"][x])): st.bad(f"{name} MON at {t} x={x}")
    delay = 0
    for x in R:
        for t in range(k0, kT):
            if hi(Cs[t]["pi"][x]) != hi(Cs[t + 1]["pi"][x]): delay = max(delay, t + 1 - k0)
    st.mxu("max_freeze_delay", delay)
    for t in range(f0, kT + 1):
        for x in R:
            st.c["FRZU_checks"] += 1
            if hi(Cs[t]["pi"][x]) != hi(Cs[f0]["pi"][x]): st.bad(f"{name} FRZU at {t} x={x} (k0={k0}, r={r})"); break
    # LEN
    mstar_th = C0["mstar"] == cth
    if f0 <= kT:
        cnt = {}
        for t in range(f0, kT):
            for v in R:
                if v in (o, cth if mstar_th else cw): continue
                if mstar_th:
                    if A[t].Xi[v][1] != A[f0].Xi[v][1]: st.bad(f"{name} LEN-Xi path set moved at {t} v={v}")
                    if A[t].Xi[v] != A[t + 1].Xi[v]: cnt[v] = cnt.get(v, 0) + 1
                else:
                    if A[t].W[v][1] != A[f0].W[v][1]: st.bad(f"{name} LEN-W path set moved at {t} v={v}")
                    if A[t].W[v] != A[t + 1].W[v]: cnt[v] = cnt.get(v, 0) + 1
        if cnt and max(cnt.values()) > r - 2: st.bad(f"{name} LEN per-vertex {max(cnt.values())} > r-2")
        st.c["LEN_runs_after_f0"] += 1
    xich = sum(1 for t in range(k0, kT) if any(A[t].Xi[v] != A[t + 1].Xi[v] for v in R))
    wch = sum(1 for t in range(k0, kT) if any(A[t].W[v] != A[t + 1].W[v] for v in R))
    if mstar_th and xich > (r - 1) ** 2: st.bad(f"{name} LEN/RUN(a) {xich}")
    if not mstar_th and wch > (r - 1) ** 2: st.bad(f"{name} LEN-W count {wch}")
    # RUN bound
    if mstar_th: case = "a"; B = (r - 1) ** 2
    elif not C0["kindset"]:     # the explicit sum is -1 at r = 1 (R = {o}); the stated bound is r^3 (N-KW-3)
        case = "b"; B = (r - 1) ** 2 + ((r - 1) * (r - 2) + 1) * (r - 2) if r >= 2 else r ** 3
        if r == 1: st.c["RECORD_RUN_case_b_r=1"] += 1
    else: case = "c"; B = 3 * Delta * r ** 4
    st.c[f"RUN_case_{case}"] += 1
    if xich > B: st.bad(f"{name} RUN({case}) {xich} > {B}")
    st.mxu(f"max_RUN_ratio_case_{case}_x1000", (1000 * xich) // max(B, 1))
    # kinds, CASC-B, CW-INT, E-SEG (setting: not H2, c_w != o)
    if not C0["kindset"]: return
    kind = lambda t: Cs[t]["kind"]
    kchg = [kind(t) != kind(t + 1) for t in range(k0, kT)]
    up = "_cw_above" if g.rank[cw] > g.rank[cth] else ""
    if up: st.c["RECORD_runs_cw_above_notH2"] += 1
    for t in range(k0, kT):
        if kchg[t - k0]:
            st.c["RECORD_kind_change_transitions" + up] += 1
            if t >= f0: st.c["RECORD_kind_change_after_freeze" + up] += 1
        if cw in sw(A, t):
            st.c["RECORD_cw_switches" + up] += 1
            if t >= f0: st.c["RECORD_cw_switches_after_freeze" + up] += 1
    if g.rank[cw] > g.rank[cth] and f0 < kT:      # KIND-MONO
        seen = {}
        for t in range(f0, kT):
            for v, kd in kind(t).items():
                if kind(t + 1)[v] != kd:
                    seen[v] = seen.get(v, 0) + 1
                    if not (kd == "B" and kind(t + 1)[v] == "A") or seen[v] > 1: st.bad(f"{name} KMONO v={v} at {t}")
        st.c["KMONO_runs"] += 1
    isB = lambda t, v: v != o and kind(t).get(v) == "B"
    kBsw = [any(g.owner[v] == 0 and isB(t, v) for v in sw(A, t)) for t in range(k0, kT)]
    # W-flat segments of the run
    wflat = [all(A[t].W[v] == A[t + 1].W[v] for v in R) for t in range(k0, kT)]
    t = k0
    while t < kT:
        if not wflat[t - k0]: t += 1; continue
        e = t
        while e + 1 < kT and wflat[e + 1 - k0]: e += 1
        seg = list(range(t, e + 1))
        # CASC-B on kind-change-free parts
        parts, cur = [], []
        for u in seg:
            if kchg[u - k0]:
                if cur: parts.append(cur)
                cur = []
            else: cur.append(u)
        if cur: parts.append(cur)
        for P in parts:
            for j, u in enumerate(P):
                for v in sw(A, u):
                    if g.owner[v] == 0 and isB(u, v):
                        st.c["CASCB_kindB_switches"] += 1
                        bound = len(Cs[u]["pi"][v]) - (3 if MUT == "casc" else 2)
                        st.mxu("CASCB_max_step_minus_bound_plus100", j - bound + 100)
                        if j > bound: st.bad(f"{name} CASCB v={v} step {j} > {bound}")
        # E-SEG for segments after f0 with c_w > c_theta
        if g.rank[cw] > g.rank[cth] and t >= f0:
            ee = sum(kchg[u - k0] for u in seg)
            NBlit = sum(kBsw[u - k0] for u in seg)
            NBout = sum(kBsw[u - k0] and not kchg[u - k0] for u in seg)
            cut = [u for u in seg if kchg[u - k0] or kBsw[u - k0]]
            cws = sum(1 for u in seg if cw in sw(A, u))
            ev = sum(1 for u in seg if kchg[u - k0] or cw in sw(A, u))
            swr = sum(1 for u in seg if sw(A, u) & R)
            st.c["ESEG_segments"] += 1
            if NBout > (ee + 1) * (r - 2): st.bad(f"{name} ESEG(i') {NBout}")
            if NBlit > (ee + 1) * (r - 2): st.c["RECORD_ESEG_literal_(i)_exceeded"] += 1
            if cws > Delta * (len(cut) + 1): st.bad(f"{name} ESEG(ii)")
            if ev > (ee + 1) * (Delta * r + 1) - 1: st.bad(f"{name} ESEG(iii)")
            if swr > (ev + 1) * (2 * r - 3): st.bad(f"{name} ESEG(iv)")
        # CW-INT on gaps between cut transitions inside this W-flat segment (any cut-free sub-run of the run works)
        gap = 0
        for u in seg:
            if kchg[u - k0] or kBsw[u - k0]:
                gap = 0; continue
            if cw in sw(A, u):
                gap += 1; st.c["CWINT_cw_switches_checked"] += 1
                if gap > len(set(g.succ[cw])) - 1: st.bad(f"{name} CWINT {gap}")
        t = e + 1
    if g.rank[cw] > g.rank[cth] and f0 < kT:
        tot = sum(kchg[u - k0] for u in range(f0, kT))
        if tot > r - 2: st.bad(f"{name} ESEG(v) {tot}")

def main():
    a = sys.argv[1:]; st = OC.Stats()
    if a[0] == "random":
        N, nmin, nmax, seed = map(int, a[1:5]); mode = a[5] if len(a) > 5 else "own"; rng = random.Random(seed)
        for i in range(N):
            g, o = RC.rand_game(rng, rng.randint(nmin, nmax)); assert FC.odd_vertex(g) == o
            s, t = RC.rand_start(rng, g) if rng.random() < 0.7 else FC.s3_start(g)
            A, fbs = OC.run_trace(g, o, s, t, rng, mode); check_run(g, o, A, fbs, st, f"{mode}:seed{seed}#{i}")
    else:
        path = a[1]; runs = int(a[2]) if len(a) > 2 else 3; mode = a[3] if len(a) > 3 else "own"
        g = RC.parse(open(path).read()); o = FC.odd_vertex(g); rng = random.Random(7)
        for r_ in range(runs):
            s, t = FC.s3_start(g) if r_ == 0 else RC.rand_start(rng, g)
            A, fbs = OC.run_trace(g, o, s, t, rng, mode); check_run(g, o, A, fbs, st, f"{mode}:{os.path.basename(path)}#{r_}")
    FC.report(st)

if __name__ == "__main__":
    main()
