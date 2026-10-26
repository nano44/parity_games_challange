#!/usr/bin/env python3
r"""REFEREE-2 successor 8 (Opus 5.5, D15): mechanical check of packet P-N5-RL (docs/si/P-N5-RL-box10.md sha1 0a3c70cb @ trunk 2fb698d).
Own code on my lane's R2-N5-FRZ/frz_check.py (own N5 on C^1O, any S4a arena optimum; --rand for random optima). No lane script
(experiments/si/riselast/*.py) and no REFEREE probe is run or imported; lane .pg files are inputs only. One Odd choice vertex asserted.
Opt(G_tau) = Even's best response to tau (pointwise max, by SI); Opt(G_tau[F]) = the same on the arena of Even edges inside F.
Checks:
  BLFORM  at (h) states: every blocked edge (W-improving, not a gate) has sigma(v) in F, v in F, u in Rbar; pi_u(+)theta <= Xi(sigma v) < pi_u(+)w;
          Xi(sigma v) has cycle node c.
  BL      at in-phase S4c fallbacks with (h) and THR: (a) W != W*; (b) a blocked edge exists; (c) W = Opt(G_tau[F]) on F; (d) W(x0) < W*(x0)
          and every free exit x with o(+)Xi(x) < w deficient; (e) the computed optimal G_tau play from x0 leaves F along an Even edge into Rbar.
  FF      FREE-FREEZE: k0 as in BL, t > k0 in the phase with (h), z in F_t with its (sigma_t, tau)-play inside F_{k0}: Xi_t(z) = Xi_k0(z).
  MERGE   at (h) states, every window gate (y in R, z in F) of level l >= -1: (a) pi(sigma y) avoids H, COARSE_l equal; (b) o not in H;
          (c) the prefixes before the merge point m of z's and x0's paths to c have no H vertex.
  EQEND   scope runs with theta_t = w: later states of S are EQ; <= 1 fallback of S after t, and it is the last transition of its phase.
  ENT     the ENT setting (consecutive fallbacks k0 < k of S, M_k0 = M_k = L >= 0, r > L on [k0+1, k], a COARSE_L(theta) rise at an S4a
          step in (k0, k)); if it occurs: EV, EV+, TEV-RED (1)-(5).
  CYC     (probe for TEV-RED's "last Ev vertex"): after an in-scope fallback k0 with M >= 0, at states t in (k0, next fallback of S] of S:
          does c's honest cycle at t meet Ev = F_{k0+1} \ F_{k0}?  does the threat's play meet Ev, and only on the cycle?
Usage: rl_check.py random N nmin nmax seed [--rand] | inst game.pg [runs] [--rand]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-FRZ"))
import frz_check as FC
RC = FC.RC
INF, BOT = FC.INF, FC.BOT

def opt_F(g, S, F):
    ar = [sorted(z for z in g.succ[v] if z in F) if (g.owner[v] == 0 and v in F) else [S.f[v]] for v in range(g.n)]
    fo, val = RC.even_optimum(g, S.f, ar)
    return fo, val

def honest_cycle(fh, v):
    seen, path, x = {}, [], v
    while x not in seen: seen[x] = len(path); path.append(x); x = fh[x]
    return path[seen[x]:]

def path_to(f, v, c):
    """path from v up to (excluding) the first visit of c under f; None if c not reached"""
    p, x, seen = [], v, set()
    while x != c:
        if x in seen: return None
        seen.add(x); p.append(x); x = f[x]
    return p

def full_play(f, v):
    seen, path, x = set(), [], v
    while x not in seen: seen.add(x); path.append(x); x = f[x]
    return path

def check_run(g, o, A, fbs, st, name):
    n = g.n; T = len(fbs)
    st.c["runs"] += 1; st.c["transitions"] += T; st.c["fallbacks"] += sum(fbs)
    inph = [A[k].lamX == A[k + 1].lamX and A[k].tu[o] == A[k + 1].tu[o] for k in range(T)]
    for k, S in enumerate(A):
        if not S.hh: continue
        c = S.theta[0]; e = S.tu[o]
        # ---- BL-FORM
        for v in range(n):
            if g.owner[v] != 0: continue
            s = S.sg[v]
            for u in g.succ[v]:
                if u == s or not g.cmp(S.W[u], S.W[s]) > 0: continue
                if g.cmp(S.Xi[u], S.Xi[s]) > 0: continue          # a gate
                st.c["BLFORM_blocked_edges"] += 1
                if not (s in S.F and v in S.F and u in S.Rbar): st.bad(f"{name}@{k} BLFORM (a) ({v},{u})"); continue
                pu = S.pi.get(u, []) if u != o else []
                lo, hi = RC.prefix(g, pu, S.theta), RC.prefix(g, pu, S.w)
                if not (g.cmp(lo, S.Xi[s]) <= 0 and g.cmp(S.Xi[s], hi) < 0): st.bad(f"{name}@{k} BLFORM (b) ({v},{u})")
                if S.Xi[s][0] != c: st.bad(f"{name}@{k} BLFORM (c)")
        # ---- MERGE
        x0 = S.sbar
        for (y, z), l in S.gates.items():
            if not (y in S.Rr and z in S.F) or l >= INF: continue
            st.c["MERGE_window_gates"] += 1
            Hm = max(l, g.rank[c])
            H = {v for v in range(n) if g.rank[v] > Hm}
            sy = S.sg[y]; pi = S.pi.get(sy, []) if sy != o else []
            if set(pi) & H: st.bad(f"{name}@{k} MERGE (a) route meets H")
            if FC.coarse(g, S.Xi[z], l) != FC.coarse(g, RC.prefix(g, pi, S.theta), l): st.bad(f"{name}@{k} MERGE (a) coarse")
            if o in H: st.bad(f"{name}@{k} MERGE (b)")
            pz, px = path_to(S.fh, z, c), path_to(S.fh, x0, c)
            if pz is None or px is None: st.bad(f"{name}@{k} MERGE (c) no path to c"); continue
            common = set(pz) & set(px)
            iz = next((i for i, v in enumerate(pz) if v in common), len(pz)); ix = next((i for i, v in enumerate(px) if v in common), len(px))
            if set(pz[:iz]) & set(px[:ix]): st.bad(f"{name}@{k} MERGE (c) prefixes intersect")
            if (set(pz[:iz]) | set(px[:ix])) & H: st.bad(f"{name}@{k} MERGE (c) H vertex before m")
    # ---- BL at fallbacks, FREE-FREEZE, scope runs
    k = 0
    while k < T:
        if not inph[k]: k += 1; continue
        j = k
        while j < T and inph[j]: j += 1
        check_phase(g, o, A, fbs, k, j, st, f"{name}[{k},{j}]")
        k = j

def check_phase(g, o, A, fbs, a, b, st, name):
    n = g.n; tr = range(a, b)
    for k0 in tr:
        S = A[k0]
        if not (fbs[k0] and S.hh and S.theta != S.w): continue
        st.c["BL_THR_fallbacks"] += 1
        Wst = S.U
        if S.W == Wst: st.bad(f"{name}@{k0} BL (a) W = W*")
        blocked = [(v, u) for v in range(n) if g.owner[v] == 0 for u in g.succ[v]
                   if u != S.sg[v] and g.cmp(S.W[u], S.W[S.sg[v]]) > 0 and g.cmp(S.Xi[u], S.Xi[S.sg[v]]) <= 0]
        if not blocked: st.bad(f"{name}@{k0} BL (b) no blocked edge")
        fo, opF = opt_F(g, S, S.F)
        if any(opF[v] != S.W[v] for v in S.F): st.bad(f"{name}@{k0} BL (c)")
        x0 = S.sbar
        if not g.cmp(S.W[x0], Wst[x0]) < 0: st.bad(f"{name}@{k0} BL (d) x0 not deficient")
        for x in set(g.succ[o]):
            if x in S.F and g.cmp(RC.prefix(g, [o], S.Xi[x]), S.w) < 0 and not g.cmp(S.W[x], Wst[x]) < 0: st.bad(f"{name}@{k0} BL (d) exit {x}")
        fu, _ = RC.even_optimum(g, S.f, [g.succ[v] for v in range(n)])
        pl = full_play(fu, x0)
        out = next((i for i, v in enumerate(pl) if v not in S.F), None)
        if out is None: st.bad(f"{name}@{k0} BL (e) optimal play stays in F")
        elif g.owner[pl[out - 1]] != 0 or pl[out] not in S.Rbar: st.bad(f"{name}@{k0} BL (e) exit not Even into Rbar")
        # FREE-FREEZE
        for t in range(k0 + 1, b + 1):
            if not A[t].hh: continue
            for z in A[t].F:
                if set(full_play(A[t].f, z)) <= S.F:
                    st.c["FF_checks"] += 1
                    if A[t].Xi[z] != S.Xi[z]: st.bad(f"{name} FF k0={k0} t={t} z={z}")
    # scope runs
    insc = {k: A[k].hh and A[k + 1].H2 and A[k].w == A[k + 1].w for k in tr}
    runs, cur = [], []
    for k in tr:
        if insc[k]: cur.append(k)
        else:
            if cur: runs.append(cur)
            cur = []
    if cur: runs.append(cur)
    for R_ in runs:
        sts = R_ + [R_[-1] + 1]                    # states of S
        w = A[R_[0]].w
        # EQ-END
        teq = next((t for t in sts if A[t].theta == w), None)
        if teq is not None:
            st.c["EQEND_runs_with_eq"] += 1
            for t in sts:
                if t >= teq and A[t].theta != w: st.bad(f"{name} EQEND not EQ at {t}")
            fl = [k for k in R_ if k >= teq and fbs[k]]
            st.c["EQEND_fallbacks_after"] += len(fl)
            if len(fl) > 1: st.bad(f"{name} EQEND {len(fl)} fallbacks after t")
            for k in fl:
                if k != b - 1: st.bad(f"{name} EQEND fallback {k} not last transition of phase")
        # CYC probe and ENT setting
        fl = [k for k in R_ if fbs[k]]
        for i, k0 in enumerate(fl):
            M0 = max(A[k0].gates.values()) if A[k0].gates else BOT
            if M0 < 0: continue
            nxt = fl[i + 1] if i + 1 < len(fl) else sts[-1]
            Ev = A[k0 + 1].F - A[k0].F
            c = A[k0].theta[0]
            st.c["CYC_fallbacks_M>=0"] += 1
            if Ev: st.c["CYC_fallbacks_with_Ev"] += 1
            if not A[k0].theta[1]: st.c["CYC_precond_P(theta_k0)=empty"] += 1
            if A[k0].sg[c] != A[k0 + 1].sg[c] and A[k0 + 1].sg[c] in A[k0].Rbar: st.c["CYC_precond_c_switched_into_Rbar_k0"] += 1
            for t in range(k0 + 1, nxt + 1):
                if not A[t].hh: continue
                st.c["CYC_states"] += 1
                cyc = set(honest_cycle(A[t].fh, c))
                if cyc & Ev: st.c["CYC_c_cycle_meets_Ev"] += 1; st.ex.setdefault("CYC", f"{name} k0={k0} t={t}")
                xt = A[t].sbar; pth = path_to(A[t].fh, xt, c)
                if set(full_play(A[t].fh, xt)) & Ev:
                    st.c["CYC_threat_meets_Ev"] += 1
                    if pth is not None and not (set(pth) & Ev): st.c["CYC_threat_meets_Ev_only_on_cycle"] += 1
            if i + 1 < len(fl):
                k = fl[i + 1]
                Mk = max(A[k].gates.values()) if A[k].gates else BOT
                if Mk != M0: continue
                L = M0
                if not all(A[s].r > L for s in range(k0 + 1, k + 1)): continue
                rise = any(not fbs[s] and FC.coarse(g, A[s].theta, L) != FC.coarse(g, A[s + 1].theta, L) for s in range(k0 + 1, k))
                if not rise: continue
                st.c["ENT_settings"] += 1; st.ex.setdefault("ENT", f"{name} k0={k0} k={k}")
                check_ent(g, o, A, k0, k, L, Ev, st, name)

def check_ent(g, o, A, k0, k, L, Ev, st, name):
    S0, Sk = A[k0], A[k]; c = S0.theta[0]
    H = {v for v in range(g.n) if g.rank[v] > max(L, g.rank[c])}
    Aset, B = S0.theta[1] & H, Sk.theta[1] & H
    for (y, z), l in Sk.gates.items():
        if not (l == L and y in Sk.Rr and z in Sk.F): continue
        st.c["ENT_window_gates"] += 1
        pl = full_play(Sk.f, z)
        if not set(pl) & Ev: st.bad(f"{name} EV z={z} play avoids Ev"); continue
        if not Aset <= B: st.bad(f"{name} EV A not in B")
        xp = full_play(Sk.f, Sk.sbar)
        if not set(xp) & Ev: st.bad(f"{name} EV+ threat avoids Ev")
    for t in range(k0 + 1, k + 1):
        St = A[t]; xp = full_play(St.f, St.sbar)
        if not set(xp) & Ev: continue
        rise_before = any(FC.coarse(g, A[s].theta, L) != FC.coarse(g, A[s + 1].theta, L) for s in range(k0 + 1, t))
        if not rise_before: continue
        st.c["TEV_RED_cases"] += 1
        evs = [i for i, v in enumerate(xp) if v in Ev]
        e = xp[evs[-1]]
        if set(honest_cycle(St.fh, c)) & Ev: st.c["TEV_RED_cycle_meets_Ev (gap)"] += 1; continue
        f = St.sg[e] if g.owner[e] == 0 else None
        if f is None: st.bad(f"{name} TEV-RED (1) e Odd"); continue
        if not set(full_play(St.f, f)) <= S0.F or St.Xi[f] != S0.Xi[f]: st.bad(f"{name} TEV-RED (1)")
        if t == k:
            ue = S0.sg[e]
            if not (ue in Ev and ue in Sk.F): st.bad(f"{name} TEV-RED (5)")

def main():
    st = FC.Stats(); args = [a for a in sys.argv[1:] if a != "--rand"]; rand = "--rand" in sys.argv
    if args[0] == "random":
        N, nmin, nmax, seed = map(int, args[1:5]); rng = random.Random(seed)
        for i in range(N):
            g, o = RC.rand_game(rng, rng.randint(nmin, nmax)); assert FC.odd_vertex(g) == o
            s, t = RC.rand_start(rng, g) if rng.random() < 0.7 else FC.s3_start(g)
            A, fbs = FC.run_n5(g, o, s, t, rng, rand); check_run(g, o, A, fbs, st, f"seed{seed}#{i}")
    else:
        path = args[1]; runs = int(args[2]) if len(args) > 2 else 3
        g = RC.parse(open(path).read()); o = FC.odd_vertex(g); rng = random.Random(7)
        for r in range(runs):
            s, t = FC.s3_start(g) if r == 0 else RC.rand_start(rng, g)
            A, fbs = FC.run_n5(g, o, s, t, rng, rand); check_run(g, o, A, fbs, st, f"{os.path.basename(path)}#{r}")
    FC.report(st)
    for kk, vv in st.ex.items(): print("example", kk, vv)

if __name__ == "__main__":
    main()
