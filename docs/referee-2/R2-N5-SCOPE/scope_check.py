#!/usr/bin/env python3
r"""REFEREE-2 successor 8 (Opus 5.5, D15): mechanical check of packet P-N5-SCOPE (docs/new/P-N5-SCOPE-box36.md sha1 c3f5ed37 @ trunk 8998ee6).
Own code on my lane's R2-N5-FRZ/frz_check.py (own N5 on C^1O, S4a = ANY arena optimum: deterministic switch-all SI, or --rand random-subset
SI + random value-preserving re-choices; S4b Odd's pointwise best at o; S4c as SPEC) and, for CN-LAST on GENERAL games, an own general N5
below (honest valuation = pointwise minimum over Odd strategies by Odd one-player SI; Odd side = Even's best response to tau, read in G's
order = the dual order reversed, R18 (d) Lemma R). No lane script (scopecnt.py, lenrun.py, outclimb.py) and no REFEREE probe is run or
imported; lane .pg files are inputs only. Every C^1O game asserts exactly one Odd vertex with out-degree > 1. Phase key (lambda_Xi, tau).
Checks:
  KEY    lambda_U constant across every transition with tau unchanged (so (lambda_Xi, tau)-phases = joint lambda-phases).
  TC     statewise: H2 <=> tau(o) in F.
  WCH    at H2 states: w = o (+) Xi(tau(o)); at in-phase H2->H2 transitions with w changing: Xi(tau(o)) changes (always, crossing or not);
         per crossing-free interval: non-crossing WCH <= max(0,|F|-1); per phase #WCH <= (n-2)(X+1)+X.
  SCOPE  scope runs per phase <= #(h)-runs + #WCH (case 1 / case 2 classified, case-2 injection checked) and <= (1+T+f)+(n-2)(X+1)+X,
         with T, f, X the actual counts of the phase.
  FBINT  every non-tame in-phase transition is a crossing; fallbacks per maximal crossing-free run of in-phase transitions <= n_E(2n-1);
         also per tame run (FB).
  NH1    R-CONST (Rbar = lambda^{-1}(c_theta) at every not-H1 state); fallbacks with not-H1 at k <= n_E(2n-1)(ceil(T/2)+1)+T, case A per
         maximal not-H1 run <= n_E(2n-1), #runs <= drops + 1, case B <= T.
  CNL    at every Even S4c fallback whose gates all have an own-cycle-node tail and level -1: Setup facts, (i) Xi_{k+1} = Xi_k,
         (ii) Is_{k+1} = {}, (iii) the run stops at k+1 or tau changes at k+1 -> k+2; at most one per phase, and it is the last transition.
         Control: level -1 Even fallbacks with a non-cycle-node tail (outside the hypothesis) are counted with (i)-(iii) outcomes.
  CLS    (DATA) the packet's section 7.1 classes of in-phase fallbacks, for MY N5.
Usage: scope_check.py random N nmin nmax seed [--rand] | inst game.pg [runs] [--rand] | general N nmin nmax seed [--rand] | ginst game.pg [runs]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-FRZ"))
import frz_check as FC
RC = FC.RC
INF, BOT = FC.INF, FC.BOT

def oplus(g, u, x):
    return RC.prefix(g, [u], x)

def tame(g, A, B, M):
    if M == INF: return True
    return all(FC.coarse(g, A.Xi[v], M) == FC.coarse(g, B.Xi[v], M) for v in range(g.n))

# ------------------------------------------------------------------ CN-LAST (shared by C^1O and general runs)
def check_cnlast(g, Xs, Iss, lams, sgs, tus, fbs, k, st, name, inph_next_end):
    """k: an Even fallback transition. Xs/Iss/lams/sgs/tus: per-state lists. inph_next_end: True if k+1 is the last state of its phase
    (run stops at k+1 or tau changes at k+1 -> k+2)."""
    X0, Is0, lam0, sg0 = Xs[k], Iss[k], lams[k], sgs[k]
    levs = {(y, z): FC.lev(g, X0[sg0[y]], X0[z]) for y, z in Is0}
    allcn = all(lam0[y] == y for y, _ in Is0); alll1 = all(L == -1 for L in levs.values())
    if not alll1: return None
    st.c["CNL_level-1_Even_fallbacks"] += 1
    ok_i = Xs[k + 1] == X0; ok_ii = not Iss[k + 1]; ok_iii = inph_next_end
    if allcn:
        st.c["CNL_hypothesis_cases"] += 1
        tails = sorted({y for y, _ in Is0})
        for c in tails:
            zc = sgs[k + 1][c]
            if X0[sg0[c]][0] != c or X0[sg0[c]][1]: st.bad(f"{name} CNL setup Xi(sigma c) not (c,{{}},.) c={c}")
            if X0[zc][0] != c or X0[zc][1]: st.bad(f"{name} CNL setup Xi(z) not (c,{{}},.) c={c}")
        if not ok_i: st.bad(f"{name} CNL (i) Xi changed at {k}")
        if not ok_ii: st.bad(f"{name} CNL (ii) Is nonempty at {k + 1}")
        if not ok_iii: st.bad(f"{name} CNL (iii) phase continues past {k + 1}")
        if len(fbs) > k + 1: st.c["CNL_hyp_followed_by_tau_change"] += 1
        else: st.c["CNL_hyp_followed_by_stop"] += 1
        return True
    st.c[f"CNL_control_noncycle_tail (i)={ok_i} (ii)={ok_ii} (iii)={ok_iii}"] += 1
    return False

# ------------------------------------------------------------------ C^1O run checks
def check_run(g, o, A, fbs, st, name):
    n = g.n; T = len(fbs); nE = sum(1 for v in range(n) if g.owner[v] == 0)
    st.c["runs"] += 1; st.c["transitions"] += T; st.c["fallbacks"] += sum(fbs)
    for k, S in enumerate(A):
        t0 = S.tu[o]
        if S.H2 != (t0 in S.F): st.bad(f"{name}@{k} TC H2 <=> tau(o) in F")
        if S.H2:
            st.c["WCH_H2_states"] += 1
            if S.w != oplus(g, o, S.Xi[t0]): st.bad(f"{name}@{k} WCH w != o (+) Xi(tau o)")
    for k in range(T):
        if A[k].tu[o] == A[k + 1].tu[o]:
            st.c["KEY_tau_const_transitions"] += 1
            if A[k].lamU != A[k + 1].lamU: st.bad(f"{name}@{k} KEY lambda_U changed with tau constant")
    inph = [A[k].lamX == A[k + 1].lamX and A[k].tu[o] == A[k + 1].tu[o] for k in range(T)]
    # phase ends (for CN-LAST): k+1 last state of its phase iff k+1 == T or not inph[k+1]
    Xs = [S.Xi for S in A]; Iss = [S.Is for S in A]; lams = [S.lamX for S in A]; sgs = [S.sg for S in A]; tus = [S.tu for S in A]
    k = 0
    while k < T:
        if not inph[k]:
            # phase-exit Even fallbacks are outside "transitions of the phase"; CN-LAST says its fallback is in-phase ((i) keeps lambda)
            if fbs[k] and A[k].Is:
                r = check_cnlast(g, Xs, Iss, lams, sgs, tus, fbs, k, st, f"{name}@{k}", True)
                if r: st.bad(f"{name}@{k} CNL hypothesis fallback leaves the phase")
            k += 1; continue
        j = k
        while j < T and inph[j]: j += 1
        check_phase(g, o, A, fbs, k, j, st, f"{name}[{k},{j}]", inph, Xs, Iss, lams, sgs, tus, nE)
        k = j

def check_phase(g, o, A, fbs, a, b, st, name, inph, Xs, Iss, lams, sgs, tus, nE):
    n = g.n; st.c["phases"] += 1
    tr = range(a, b)                                   # transitions k -> k+1 of the phase
    cross = {k: A[k].Rr != A[k + 1].Rr for k in tr}
    X = sum(cross.values()); f = sum(fbs[k] for k in tr)
    togs = [k for k in tr if A[k].H1 != A[k + 1].H1]; Tt = len(togs); drops = sum(1 for k in togs if A[k].H1)
    t0 = A[a].tu[o]; cth = A[a].lamX[o]
    U = {v for v in range(n) if A[a].lamX[v] == cth}
    # ---- WCH
    wch = [k for k in tr if A[k].H2 and A[k + 1].H2 and A[k].w != A[k + 1].w]
    for k in wch:
        st.c["WCH_transitions"] += 1
        if cross[k]: st.c["WCH_at_crossings"] += 1
        if A[k].Xi[t0] == A[k + 1].Xi[t0]: st.bad(f"{name} WCH w changed, Xi(tau o) not, at {k}")
    for k in tr:   # control: w changes without H2 at both ends and Xi(t0) unchanged
        if A[k].w != A[k + 1].w and not (A[k].H2 and A[k + 1].H2) and A[k].Xi[t0] == A[k + 1].Xi[t0]: st.c["WCH_control_w_change_noH2_Xi(t0)_same"] += 1
    # per crossing-free interval (maximal runs of states with R constant)
    s = a
    while s <= b:
        e = s
        while e < b and not cross[e]: e += 1
        nw = sum(1 for k in range(s, e) if k in wch)
        Fs = len(A[s].F)
        if nw > max(0, Fs - 1): st.bad(f"{name} WCH interval [{s},{e}] {nw} > max(0,|F|-1)={max(0, Fs - 1)}")
        st.mxu("max_WCH_per_crossing_free_interval", nw)
        s = e + 1
    if len(wch) > (n - 2) * (X + 1) + X: st.bad(f"{name} WCH {len(wch)} > (n-2)(X+1)+X")
    st.mxu("max_WCH_per_phase", len(wch))
    # ---- SCOPE-COUNT
    insc = {k: A[k].hh and A[k + 1].H2 and A[k].w == A[k + 1].w for k in tr}
    starts = [k for k in tr if insc[k] and not (k > a and insc[k - 1])]
    hruns = sum(1 for t in range(a, b + 1) if A[t].hh and not (t > a and A[t - 1].hh))
    c1 = c2 = 0; img = set()
    for k in starts:
        if k == a or not A[k - 1].hh: c1 += 1
        else:
            c2 += 1
            if not (k - 1 in wch): st.bad(f"{name} SCOPE case 2 start {k}: {k-1}->{k} not WCH")
            img.add(k - 1)
    if c1 > hruns: st.bad(f"{name} SCOPE case 1 {c1} > (h)-runs {hruns}")
    if len(img) != c2: st.bad(f"{name} SCOPE case-2 map not injective")
    if len(starts) > hruns + len(wch): st.bad(f"{name} SCOPE {len(starts)} > (h)-runs + WCH")
    if hruns > 1 + Tt + f: st.bad(f"{name} RESTARTS {hruns} > 1+T+f")
    if len(starts) > (1 + Tt + f) + (n - 2) * (X + 1) + X: st.bad(f"{name} SCOPE full bound")
    st.c["SCOPE_scope_runs"] += len(starts); st.c["SCOPE_case1"] += c1; st.c["SCOPE_case2"] += c2
    st.mxu("max_scope_runs_per_phase", len(starts)); st.mxu("max_h_runs_per_phase", hruns); st.mxu("max_scope_case2_per_phase", c2)
    # ---- FB-INT
    M = {}
    for k in tr:
        gl = list(A[k].gates.values()); M[k] = max(gl) if gl else BOT
    tm = {k: tame(g, A[k], A[k + 1], M[k]) for k in tr}
    for k in tr:
        if not tm[k]:
            st.c["FBINT_nontame"] += 1
            if not cross[k]: st.bad(f"{name} FBINT non-tame transition {k} is not a crossing")
    bound = nE * (2 * n - 1)
    def runs_of(pred):
        out, cur = [], []
        for k in tr:
            if pred(k): cur.append(k)
            else:
                if cur: out.append(cur)
                cur = []
        if cur: out.append(cur)
        return out
    for Q in runs_of(lambda k: not cross[k]):
        fq = sum(fbs[k] for k in Q)
        st.mxu("max_fallbacks_per_crossing_free_run", fq)
        if fq > bound: st.bad(f"{name} FBINT {fq} fallbacks in crossing-free run {Q[0]}..{Q[-1]} > {bound}")
    for Q in runs_of(lambda k: tm[k]):
        fq = sum(fbs[k] for k in Q)
        if fq > bound: st.bad(f"{name} FB {fq} fallbacks in a tame run")
    # ---- NH1-FB and R-CONST
    for t in range(a, b + 1):
        if not A[t].H1:
            st.c["RCONST_notH1_states"] += 1
            if A[t].Rbar != U: st.bad(f"{name} RCONST at {t}")
    nh1 = [k for k in tr if fbs[k] and not A[k].H1]
    cA = [k for k in nh1 if not A[k + 1].H1]; cB = [k for k in nh1 if A[k + 1].H1]
    nruns = 0
    t = a
    while t <= b:
        if A[t].H1: t += 1; continue
        e = t
        while e < b and not A[e + 1].H1: e += 1
        nruns += 1
        fs = sum(fbs[k] for k in range(t, e))
        st.mxu("max_caseA_fallbacks_per_notH1_run", fs)
        if fs > bound: st.bad(f"{name} NH1 case A run {fs} > {bound}")
        if any(cross[k] for k in range(t, e)): st.bad(f"{name} NH1 crossing inside a not-H1 run")
        t = e + 1
    if nruns > drops + 1: st.bad(f"{name} NH1 {nruns} not-H1 runs > drops+1")
    if cth == o and Tt: st.bad(f"{name} NH1 toggle with c_theta = o")
    if len(cB) > Tt: st.bad(f"{name} NH1 case B")
    if len(nh1) > bound * (-(-Tt // 2) + 1) + Tt: st.bad(f"{name} NH1 total {len(nh1)}")
    st.c["NH1_fallbacks"] += len(nh1); st.c["NH1_caseA"] += len(cA); st.c["NH1_caseB"] += len(cB)
    st.mxu("max_NH1_fallbacks_per_phase", len(nh1))
    # ---- CN-LAST (in-phase Even fallbacks)
    ncn = 0
    for k in tr:
        if fbs[k] and A[k].Is:
            last = (k + 1 == b)
            r = check_cnlast(g, Xs, Iss, lams, sgs, tus, fbs, k, st, f"{name}@{k}", last and (k + 1 == len(fbs) or A[k + 1].tu != A[k + 2].tu))
            if r:
                ncn += 1
                if k != b - 1: st.bad(f"{name} CNL fallback {k} not the last transition of its phase")
    if ncn > 1: st.bad(f"{name} CNL {ncn} per phase")
    # ---- CLS (DATA): section 7.1 classes, my N5
    for k in tr:
        if not fbs[k]: continue
        S0, S1 = A[k], A[k + 1]
        if insc[k]: cls = "IN"
        elif not S0.H1: cls = "NH1"
        elif not S0.H2: cls = "H1_notH2"
        elif not S0.H3: cls = "OTHER"
        elif not S1.H2: cls = "END_notH2"
        else: cls = "END_w_change"
        st.c["CLS_" + cls] += 1
    st.mxu("max_out_of_SN_fallbacks_per_phase", sum(1 for k in tr if fbs[k] and A[k].H1 and not (A[k].H2 and A[k].H3)))

# ------------------------------------------------------------------ own general N5 (every game), for CN-LAST
def vals(g, f): return RC.vals_of(g, f)[0]

def odd_optimum(g, f, arena):
    """Odd's pointwise-optimal (minimising) strategy in the one-player arena, Even fixed as in f; by switch-all SI from f."""
    f = list(f)
    while True:
        val = vals(g, f)
        imp = {}
        for v in range(g.n):
            if g.owner[v] != 1: continue
            for z in arena[v]:
                if z != f[v] and g.cmp(val[z], val[f[v]]) < 0:
                    if v not in imp or g.key(val[z]) < g.key(val[imp[v]]): imp[v] = z
        if not imp: return f, val
        for v, z in imp.items(): f[v] = z

def gstate(g, sg, tu):
    n = g.n
    f = [sg[v] if g.owner[v] == 0 else tu[v] for v in range(n)]
    fh, Xi = odd_optimum(g, f, [g.succ[v] for v in range(n)])
    _, Uv = RC.even_optimum(g, f, [g.succ[v] for v in range(n)])
    Is = [(v, z) for v in range(n) if g.owner[v] == 0 for z in g.succ[v] if z != sg[v] and g.cmp(Xi[z], Xi[sg[v]]) > 0]
    It = [(v, z) for v in range(n) if g.owner[v] == 1 for z in g.succ[v] if z != tu[v] and g.cmp(Uv[z], Uv[tu[v]]) < 0]
    return dict(f=f, Xi=Xi, U=Uv, Is=Is, It=It, lam=tuple(x[0] for x in Xi), sg=list(sg), tu=list(tu))

def run_general(g, s, t, rng, rand, cap=400):
    A = [gstate(g, s, t)]; fbs = []
    while len(A) <= cap:
        S = A[-1]; sg, tu = S["sg"], S["tu"]
        if not S["Is"] and not S["It"]: break
        ns, nt = list(sg), list(tu)
        if S["Is"]:
            ar = [sorted({sg[v]} | {z for x, z in S["Is"] if x == v}) if g.owner[v] == 0 else [S["f"][v]] for v in range(g.n)]
            fo, _ = RC.even_optimum(g, S["f"], ar, rng if rand else None, perturb=rng.randint(0, 6) if rand else 0)
            for v in range(g.n):
                if g.owner[v] == 0: ns[v] = fo[v]
        if S["It"]:
            ar = [sorted({tu[v]} | {z for x, z in S["It"] if x == v}) if g.owner[v] == 1 else [S["f"][v]] for v in range(g.n)]
            fo, _ = odd_optimum(g, S["f"], ar)
            for v in range(g.n):
                if g.owner[v] == 1: nt[v] = fo[v]
        fb = 0
        if ns == sg and nt == tu:
            fb = 1
            if S["Is"]:
                for v in {v for v, _ in S["Is"]}:
                    ns[v] = max((z for x, z in S["Is"] if x == v), key=lambda z: (g.key(S["Xi"][z]), z))
            else:
                for v in {v for v, _ in S["It"]}:
                    nt[v] = min((z for x, z in S["It"] if x == v), key=lambda z: (g.key(S["U"][z]), -z))
        A.append(gstate(g, ns, nt)); fbs.append(fb)
    return A, fbs

def check_general(g, A, fbs, st, name):
    T = len(fbs); st.c["gen_runs"] += 1; st.c["gen_transitions"] += T; st.c["gen_fallbacks"] += sum(fbs)
    for k in range(T):   # sanity: R15 (a)
        for v in range(g.n):
            if g.cmp(A[k + 1]["Xi"][v], A[k]["Xi"][v]) < 0: st.bad(f"{name}@{k} R15(a) v={v}")
    inph = [A[k]["lam"] == A[k + 1]["lam"] and A[k]["tu"] == A[k + 1]["tu"] for k in range(T)]
    Xs = [S["Xi"] for S in A]; Iss = [S["Is"] for S in A]; lams = [S["lam"] for S in A]; sgs = [S["sg"] for S in A]; tus = [S["tu"] for S in A]
    perphase = {}
    pid = 0
    for k in range(T):
        if k > 0 and not inph[k - 1]: pid += 1
        if fbs[k] and A[k]["Is"]:
            last = (k + 1 == T) or (A[k + 1]["tu"] != A[k + 2]["tu"])
            r = check_cnlast(g, Xs, Iss, lams, sgs, tus, fbs, k, st, f"{name}@{k}", last)
            if r:
                if not inph[k]: st.bad(f"{name}@{k} CNL fallback not in-phase")
                perphase[pid] = perphase.get(pid, 0) + 1
    if any(c > 1 for c in perphase.values()): st.bad(f"{name} CNL >1 per phase")

def rand_general(rng, n):
    owner = [rng.randint(0, 1) for _ in range(n)]
    prio = [rng.randrange(0, n + 1) for _ in range(n)]
    succ = [rng.sample(range(n), rng.randint(1, min(3, n))) for _ in range(n)]
    return RC.Game(prio, owner, succ)

def main():
    st = FC.Stats(); args = [a for a in sys.argv[1:] if a != "--rand"]; rand = "--rand" in sys.argv
    if args[0] == "random":
        N, nmin, nmax, seed = map(int, args[1:5]); rng = random.Random(seed)
        for i in range(N):
            g, o = RC.rand_game(rng, rng.randint(nmin, nmax)); assert FC.odd_vertex(g) == o
            s, t = RC.rand_start(rng, g) if rng.random() < 0.7 else FC.s3_start(g)
            A, fbs = FC.run_n5(g, o, s, t, rng, rand); check_run(g, o, A, fbs, st, f"seed{seed}#{i}")
    elif args[0] == "inst":
        path = args[1]; runs = int(args[2]) if len(args) > 2 else 3
        g = RC.parse(open(path).read()); o = FC.odd_vertex(g); rng = random.Random(7)
        for r in range(runs):
            s, t = FC.s3_start(g) if r == 0 else RC.rand_start(rng, g)
            A, fbs = FC.run_n5(g, o, s, t, rng, rand); check_run(g, o, A, fbs, st, f"{os.path.basename(path)}#{r}")
    elif args[0] == "general":
        N, nmin, nmax, seed = map(int, args[1:5]); rng = random.Random(seed)
        for i in range(N):
            g = rand_general(rng, rng.randint(nmin, nmax))
            s, t = RC.rand_start(rng, g) if rng.random() < 0.7 else FC.s3_start(g)
            A, fbs = run_general(g, s, t, rng, rand); check_general(g, A, fbs, st, f"gseed{seed}#{i}")
    elif args[0] == "ginst":
        path = args[1]; runs = int(args[2]) if len(args) > 2 else 3
        g = RC.parse(open(path).read()); rng = random.Random(7)
        for r in range(runs):
            s, t = FC.s3_start(g) if r == 0 else RC.rand_start(rng, g)
            A, fbs = run_general(g, s, t, rng, rand or r >= 2); check_general(g, A, fbs, st, f"{os.path.basename(path)}#{r}")
    FC.report(st)

if __name__ == "__main__":
    main()
