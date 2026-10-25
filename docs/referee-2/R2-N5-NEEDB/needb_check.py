#!/usr/bin/env python3
r"""REFEREE-2 successor 12 (Opus 5.5, D15): mechanical check of packet P-N5-NEEDB (docs/si/P-N5-NEEDB-box13.md sha1 7471aef3 @ trunk
e6ee6130). Own code on my lane's R2-N5-OUT/out_check.py (traces own | rand | spec), R2-N5-FRZ/frz_check.py, R2-N5-RE/re_check.py and
R2-N5-ENT/ent_check.py. No lane script (experiments/si/lv/*.py, experiments/si/lv13/*.py) is run or imported; lane .pg files are inputs.
Every game asserts exactly one Odd vertex with out-degree > 1. Scope run, (h), r, M, gates as in ent_check.py.
U := Opt(G_tau) (S.U); sigma* := an optimal G_tau strategy (re_check.even_optimum; several random optima per state, each asserted to
have valuation U).
Checks (packet items):
  XG      at in-phase THR S4c fallbacks with (h): every Even y in R_k with z := sigma*(y) in F_k and z's sigma*-play inside F_k:
          (i) U(z) = W(z) = Xi(z); (ii) U(z) >= W(s); (y, z) is a gate of level >= r_k.
  ANTI    general lemma on random one-player games (Odd out-degree 1): sigma' choosing at every Even v an edge with V(u) <= V(sigma v)
          or a V-exceptional edge has V_sigma' <= V pointwise. Instances at every analysed state: ANTI-Xi (H = G_sigmabar, V = Xi) and
          ANTI-W (H = G_tau, V = W). Also: at in-phase THR fallbacks every W-improving edge is a blocked edge or a W-exceptional gate.
  NEEDB   setting (LV+) (in-scope S4c fallback, THR, r >= 0, M = -1): (F-a), (F-b), (F-c); LV-SHAPE kinds; the sigma*-play P from x0
          uses a (beta) gate; P's case (B / A1 / A2' / A2'' / A2*) recorded.
  OT      OLD-THREAT at every post-rise state t (rise setting of R2-N5-ENT rise_end.py): every exit x != o of o with x in F_k0 and
          COARSE_L(o (+) Xi_k0 x) = COARSE_L(theta_k0) lies in R_t; FZt (FZ with t in place of k): x in F_t => COARSE_L(Xi_t x) = COARSE_L(Xi_k0 x).
  CASEI   the next fallback k of S after a rise, if it is a post-rise state with r_k > L (case (i)): FBL strong form (no gate into Rbar_k).
Records (not checks): INTO at post-rise states with r > L (CONJECTURE); in-scope THR r >= 0 fallbacks with M >= 0: does P use a
(beta)-type gate (y in R, z in F)?
Mutations (NB_MUT, controls only): nob (NEEDB evaluated at every in-scope THR r >= 0 fallback, any M), anti (ANTI allows one improving
non-exceptional edge), otc (OLD-THREAT without the COARSE condition), otf (without x in F_k0), xg (XG without "play inside F_k"), b0 (NEEDB asks for an (alpha) gate on P instead).
Usage: needb_check.py random N nmin nmax seed [own|rand|spec] | inst game.pg [runs] [own|rand|spec] | anti N nmin nmax seed"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-ENT"))
import ent_check as EC
OC, FC, RC = EC.OC, EC.FC, EC.RC
INF, BOT, lev, cl = FC.INF, FC.BOT, FC.lev, FC.coarse
M = EC.M
MUT = os.environ.get("NB_MUT", "")
NOPT = int(os.environ.get("NB_NOPT", "4"))      # random optima per state, besides the deterministic one

def oplus(g, u, val):
    c, P, l = val
    return (c, P | {u} if g.rank[u] > g.rank[c] else P, l + 1)

def play(f, v):
    seen, path, x = {}, [], v
    while x not in seen: seen[x] = len(path); path.append(x); x = f[x]
    return path, path[seen[x]:]

def le(g, a, b): return g.cmp(a, b) <= 0

def exceptional(g, f, V, v, u):
    """V-exceptional Even edge (v, u) for the one-player strategy f with valuation V"""
    return V[v][0] == v and u != f[v] and V[u][0] == v and not V[u][1]

def anti_one(g, f, V, rng, st, tag):
    """one random sigma' per ANTI's hypothesis on the one-player game with full successor map f (Odd entries fixed)"""
    n = g.n; f2 = list(f); nex = 0; mut_used = False
    for v in range(n):
        if g.owner[v] != 0: continue
        allowed = [u for u in g.succ[v] if le(g, V[u], V[f[v]]) or exceptional(g, f, V, v, u)]
        ex = [u for u in g.succ[v] if exceptional(g, f, V, v, u)]
        nex += len(ex)
        if MUT == "anti" and not mut_used:
            imp = [u for u in g.succ[v] if u not in allowed]
            if imp: allowed = imp; mut_used = True
        pick = rng.choice(ex) if ex and rng.random() < 0.6 else rng.choice(allowed)
        f2[v] = pick
    V2 = RC.vals_of(g, f2)[0]
    st.c[f"ANTI_{tag}_checks"] += 1
    if nex: st.c[f"ANTI_{tag}_with_exceptional_edges"] += 1
    if any(f2[v] != f[v] and exceptional(g, f, V, v, f2[v]) for v in range(n)): st.c[f"ANTI_{tag}_exceptional_used"] += 1
    if not all(le(g, V2[v], V[v]) for v in range(n)): st.bad(f"{tag} ANTI violated")

def optima(g, S, rng):
    arena = [list(g.succ[v]) if g.owner[v] == 0 else [S.f[v]] for v in range(g.n)]
    out = [RC.even_optimum(g, S.f, arena)]
    for _ in range(NOPT):
        out.append(RC.even_optimum(g, S.f, arena, rng, perturb=rng.randint(0, 8)))
    res = []
    for fo, val in out:
        assert val == S.U, "even_optimum value differs from S.U"
        if fo not in res: res.append(fo)
    return res

def kind(S, y, z):
    s = S.sg[y]
    if s in S.F and z in S.F: return "alpha"
    if s in S.F and z in S.Rbar: return "gamma"
    if s in S.Rbar and z in S.F: return "beta"
    return "RbarRbar"

def check_state_fb(g, o, A, k, insc, st, name, rng):
    S = A[k]; n = g.n
    thr = S.hh and g.cmp(S.theta, S.w) < 0
    if not thr: return
    st.c["THR_inphase_fallbacks"] += 1
    opts = optima(g, S, rng)
    st.c["THR_optima_tested"] += len(opts)
    # ANTI-W instance claim: W-improving edges are blocked edges or W-exceptional gates
    for v in range(n):
        if g.owner[v] != 0: continue
        for u in g.succ[v]:
            if u != S.sg[v] and g.cmp(S.W[u], S.W[S.sg[v]]) > 0:
                if (v, u) in S.gates:
                    if not exceptional(g, S.f, S.W, v, u): st.bad(f"{name} ANTI-W W-improving gate not exceptional at {k}")
                    st.c["ANTIW_W_improving_exceptional_gates"] += 1
                else: st.c["ANTIW_blocked_edges"] += 1
    for fo in opts:
        # XG
        for y in S.Rr:
            if g.owner[y] != 0: continue
            z = fo[y]
            if z not in S.F: continue
            pz, _ = play(fo, z)
            inside = all(x in S.F for x in pz)
            st.c["XG_R_to_F_optimal_edges"] += 1
            if not inside and MUT != "xg": continue
            st.c["XG_hypothesis"] += 1
            s = S.sg[y]
            if MUT != "xg" and not (S.U[z] == S.W[z] == S.Xi[z]): st.bad(f"{name} XG(i) at {k}")
            if g.cmp(S.U[z], S.W[s]) < 0: st.bad(f"{name} XG(ii) at {k}")
            if (y, z) not in S.gates or S.gates[(y, z)] < S.r: st.bad(f"{name} XG gate/level at {k} y={y} z={z}")
    # NEED-beta
    Mk = M(S)
    lvplus = insc[k] and S.r >= 0 and Mk == -1
    if insc[k] and S.r >= 0 and Mk >= 0: st.c["RECORD_inscope_THR_r>=0_M>=0"] += 1
    if not (lvplus or (MUT == "nob" and insc[k] and S.r >= 0)):
        if insc[k] and S.r >= 0:
            for fo in opts[:1]:
                p, _ = play(fo, S.sbar)
                if any(g.owner[y] == 0 and y in S.Rr and (y, fo[y]) in S.gates and fo[y] in S.F for y in p):
                    st.c["RECORD_M>=0_P_uses_R_to_F_gate"] += 1
                else: st.c["RECORD_M>=0_P_no_R_to_F_gate"] += 1
        return
    st.c["NEEDB_LVplus_states" if lvplus else "MUT_nob_states"] += 1
    x0, t = S.sbar, S.tu[o]
    U, W, Xi = S.U, S.W, S.Xi
    if g.cmp(U[x0], U[t]) < 0: st.bad(f"{name} F-a at {k}")
    if not (g.cmp(W[t], Xi[x0]) > 0 and lev(g, Xi[x0], W[t]) == S.r): st.bad(f"{name} F-b at {k}")
    if not (g.cmp(U[x0], Xi[x0]) > 0 and lev(g, Xi[x0], U[x0]) >= S.r): st.bad(f"{name} F-c at {k}")
    for (y, z) in S.Is:
        kd = kind(S, y, z); st.c[f"NEEDB_gates_{kd}"] += 1
        if lvplus and kd not in ("alpha", "beta"): st.bad(f"{name} LV-SHAPE kind {kd} at {k}")
    for fo in opts:
        p, cyc = play(fo, x0)
        if o not in p: case = "B"
        elif o not in cyc: case = "A1"
        else:
            mp = max(cyc, key=lambda u: g.rank[u]); lam = p[:p.index(o)] + [o]
            mK = max(lam, key=lambda u: g.rank[u])
            case = "A2'" if mp in lam else ("A2''" if g.rank[mp] < g.rank[mK] else "A2*")
        st.c[f"NEEDB_case_{case}"] += 1
        hasb = any(g.owner[y] == 0 and (y, fo[y]) in S.gates and kind(S, y, fo[y]) == "beta" for y in p)
        if MUT == "b0": hasb = any(g.owner[y] == 0 and (y, fo[y]) in S.gates and kind(S, y, fo[y]) == "alpha" for y in p)
        if not hasb:
            if lvplus: st.bad(f"{name} NEEDB no (beta) gate on P at {k} (case {case})")
            else: st.c[f"MUT_nob_no_beta_case_{case}"] += 1
        else: st.c["NEEDB_beta_on_P"] += 1

def check_run(g, o, A, fbs, st, name, rng):
    n = g.n; T = len(fbs)
    inph = [OC.key(A[k], o) == OC.key(A[k + 1], o) for k in range(T)]
    insc = [inph[k] and A[k].hh and A[k + 1].H2 and A[k].w == A[k + 1].w for k in range(T)]
    st.c["runs"] += 1; st.c["states"] += len(A)
    # ANTI instances at every state (sampled)
    for k in range(len(A)):
        if rng.random() < 0.3:
            S = A[k]
            anti_one(g, S.fh, S.Xi, rng, st, "Xi")
            anti_one(g, S.f, S.W, rng, st, "W")
    for k in range(T):
        if fbs[k] and inph[k] and A[k].hh: check_state_fb(g, o, A, k, insc, st, name, rng)
    # OLD-THREAT / FZt / INTO / case (i)
    for k0 in range(T):
        if not (insc[k0] and fbs[k0]): continue
        L = M(A[k0])
        if L < 0: continue
        j = None
        for s_ in range(k0 + 1, T):
            if not insc[s_] or fbs[s_] or A[s_].r <= L: break
            if cl(g, A[s_ + 1].theta, L) != cl(g, A[s_].theta, L): j = s_; break
        if j is None: continue
        st.c["OT_rises"] += 1
        S0 = A[k0]
        cand = [x for x in set(g.succ[o]) - {o}
                if (x in S0.F or MUT == "otf") and (MUT == "otc" or ((x in S0.F or MUT == "otf") and cl(g, oplus(g, o, S0.Xi[x]), L) == cl(g, S0.theta, L)))]
        if S0.sbar not in cand and MUT == "": st.bad(f"{name} OT x_k0 not a candidate at {k0}")
        t = j + 1
        while t < len(A):
            St = A[t]; st.c["OT_post_rise_states"] += 1
            for x in cand:
                st.c["OT_exit_checks"] += 1
                if x not in St.Rr: st.bad(f"{name} OT exit {x} not in R_t at t={t} (k0={k0}, L={L})")
            for x in St.F:
                if x in S0.F and cl(g, St.Xi[x], L) != cl(g, S0.Xi[x], L): st.bad(f"{name} FZt at {x} t={t}")
            if St.r > L:
                st.c["INTO_states_r>L"] += 1
                if any(z in St.Rbar for (y, z) in St.Is): st.c["INTO_holds"] += 1
                else: st.c["RECORD_INTO_fails"] += 1
            if t < T and fbs[t] and insc[t]:
                if St.r > L:
                    st.c["CASEI_occurrences"] += 1
                    if any(z in St.Rbar for (y, z) in St.Is): st.bad(f"{name} CASEI FBL gate into Rbar at {t}")
                break
            if t >= T or not insc[t] or fbs[t] or St.r <= L: break
            t += 1

def anti_random(N, nmin, nmax, seed, st):
    rng = random.Random(seed)
    for i in range(N):
        g, o = RC.rand_game(rng, rng.randint(nmin, nmax))
        f = [rng.choice(g.succ[v]) for v in range(g.n)]          # Odd entries = the one-player game's fixed edges
        V = RC.vals_of(g, f)[0]
        for _ in range(3): anti_one(g, f, V, rng, st, "rand")
        # exceptional-heavy variant: start from an optimum, where own-cycle-node switches are common
        fo, V2 = RC.even_optimum(g, f, [list(g.succ[v]) if g.owner[v] == 0 else [f[v]] for v in range(g.n)])
        for _ in range(3): anti_one(g, fo, V2, rng, st, "rand_opt")

def main():
    a = sys.argv[1:]; st = OC.Stats()
    if a[0] == "anti":
        anti_random(int(a[1]), int(a[2]), int(a[3]), int(a[4]), st)
    elif a[0] == "random":
        N, nmin, nmax, seed = map(int, a[1:5]); mode = a[5] if len(a) > 5 else "own"; rng = random.Random(seed)
        for i in range(N):
            g, o = RC.rand_game(rng, rng.randint(nmin, nmax)); assert FC.odd_vertex(g) == o
            s, t = RC.rand_start(rng, g) if rng.random() < 0.7 else FC.s3_start(g)
            A, fbs = OC.run_trace(g, o, s, t, rng, mode); check_run(g, o, A, fbs, st, f"{mode}:seed{seed}#{i}", rng)
    else:
        path = a[1]; runs = int(a[2]) if len(a) > 2 else 3; mode = a[3] if len(a) > 3 else "own"
        g = RC.parse(open(path).read()); o = FC.odd_vertex(g); rng = random.Random(7)
        starts = []
        sp = os.path.splitext(path)[0] + ".txt"
        if os.path.exists(sp):                       # saved witness start pair (sigma0 = [...], tau0 = [...])
            d = {}
            for line in open(sp):
                if line.startswith(("sigma0 =", "tau0 =")): k_, v_ = line.split("=", 1); d[k_.strip()] = eval(v_)
            if len(d) == 2: starts.append((d["sigma0"], d["tau0"]))
        starts.append(FC.s3_start(g))
        while len(starts) < runs + (1 if len(starts) > 1 else 0): starts.append(RC.rand_start(rng, g))
        for r, (s, t) in enumerate(starts):
            A, fbs = OC.run_trace(g, o, s, t, rng, mode); check_run(g, o, A, fbs, st, f"{mode}:{os.path.basename(path)}#{r}", rng)
    FC.report(st)

if __name__ == "__main__":
    main()
