#!/usr/bin/env python3
r"""REFEREE-2 successor 16 (Opus 5.5, D15): mechanical check of packet P-N5-RUND (docs/si/P-N5-RUND-box17.md sha1 71e198f3 @ 94910ed3).
State sequence: succ. 13's own SPEC loop (R2-N5-DUAL/dual_check.Runner on si.py = SPEC S1's own implementation, read-only).
Values written here from the definitions (not taken from the engine): Xi_k(v) := the value of the (sigma_k, sigmabar_k)-PLAY from v (sigmabar
= S1's counterstrategy as returned), W_k(v) := the value of the (sigma_k, tau_k)-play; both as (cycle node, rank mask of P, length).
The engine's Xi is compared with the play value (premise data, ENGXI). The lane's experiments/si/rund/*.py are NOT run or imported.
Run S: maximal fallback-free run inside a phase ((lambda_Xi, tau) constant), cut further where needed:
  h3-runs   = maximal sub-runs with (h3_D) at every state (for §3, SPLIT-RED); every sub-run of them for TWIN-GAP (TWSUB=1)
  ii-runs   = maximal sub-runs with lambda_W constant (for §2, §4 (b), §5, §6)
Checks (L ranges over LEVELS: every level -1..n-1 if n <= LALL, else {-1, 0, n//2, n-2, max M_D}):
  CRREL   §2: on maximal sub-runs of an ii-run with (i_rel) at L at every state: COARSE_L(W) constant from k0 + n - 1
  OFFa    λ_Xi = λ_W at every state of an h3-run, constant; s^Xi, s^W non-decreasing
  OFFb    Δ_k(v) = 0 on F_D and on R_D with λ(v) in pi_v; else Δ_k(v) = δ_k(u(v))
  OFFc    δ_k(u) = Σ ±2^r over P(Xi(u)) Δ P(W(u)), ranks <= L*; every offset a multiple of 2^{ℓ_S}
  MERGE   same λ and same Δ => s^Xi(y) - s^Xi(z) = s^W(y) - s^W(z)
  TG      TWIN-GAP (i) at each offset change; (ii) tail count <= (2^{L*+2} - 2) / 2^{ℓ_S}; (iii) N_v <= (n - 1) + 2^{B+1}
  PDa     PIECE_D (a): aligned state => I_sigma (engine) = improving set of sigma in G_tau (from W); sigma_{k+1} a G_tau arena optimum
          (brute force over arena strategies when their number <= BRUTE)
  PDb     PIECE_D (b): maximal blocks of aligned-source transitions inside an ii-run: length < n + m_tau
  SPR     SPLIT-RED on h3-runs: transitions <= N_split + (N_split + 1)(n + m - 1)
  PSCH    P^c_sch: clean schedule of r at k => COARSE_L(W_k(r_0)) >= COARSE_L(value(r)); paths: every W-play prefix at every state,
          every simple path if n <= PATHCAP, else RANDP random simple paths per (k, x)
  FRZS    FRZ-SCH: every s <= t, x: r_t clean at s => COARSE_L(W(x)) constant on [s, t] (FRZS_content: s < t and x's
          COARSE_L(W) changes somewhere on the run)
  CHG     CHARGE: every change of COARSE_L(W(x)) is WINDOW or CHARGED; K_F consequence
  FZ      every forbidden (x, z) at every state, every L: Xi(z) < W(z) and z in R_D. Premise data FZP: Xi <= W pointwise (F1 in G_sigma)
  UNF     every charge (q, e, f) of a charged change: k' as in the proof exists, f < k' <= s - 1 <= f + n - 1, e in I_sigma_{k'},
          e not forbidden at k'
  CHU     CHARGE-U: per x, changes of COARSE_L(W(x)) <= (n - 1)(1 + |U_L(S)|), on the ii-run and on all its sub-runs (CHUSUB=1)
Mutations RD_MUT: shift (schedule looks at k - q), noforb (forbidden-ness ignored), crrel1 (CRREL freeze from k0 + 1), tg4 (TG (ii)
bound / 4), fz (FZ for every coarse-W-improving edge, forbidden or not), piece (PDb with < n), unf (forbidden e never switched into
within n - 1 states), chu0 (CHU with (n - 1)|U|), tgr (TG proof step: tail rise <= 2^{L*} - 1).
Also TGii_rise / TGii_cons (the proof's two steps) and premise data P1 / P2 (brute force, small arenas).
Usage: rund_check.py files list.txt [runs] | start game.pg game.start | random N nmin nmax seed [k] [starts]"""
import sys, os, random, itertools
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-DUAL"))
import dual_check as DC
pg, Engine, Stats = DC.pg, DC.Engine, DC.Stats
MUT = os.environ.get("RD_MUT", "")
PATHCAP = int(os.environ.get("PATHCAP", "9"))
LALL = int(os.environ.get("LALL", "12"))
RANDP = int(os.environ.get("RANDP", "3"))
BRUTE = int(os.environ.get("BRUTE", "4096"))
TWSUB = int(os.environ.get("TWSUB", "1"))
CHUSUB = int(os.environ.get("CHUSUB", "1"))
SUBCAP = int(os.environ.get("SUBCAP", "80"))
BOT = -2


def play_value(E, nx, v):
    """S1 value of the play from v under the full successor map nx: (cycle node c, rank mask of P, steps to c)."""
    seen, path, x = {}, [], v
    while x not in seen:
        seen[x] = len(path); path.append(x); x = nx[x]
    cyc = path[seen[x]:]
    c = max(cyc, key=lambda y: E.pp[y])
    i = path.index(c)
    m = 0
    for y in path[:i]:
        if E.rank[y] > E.rank[c]: m |= E.bit[y]
    return (c, m, i)


def lasso(nx, v):
    seen, path, x = set(), [], v
    while x not in seen: seen.add(x); path.append(x); x = nx[x]
    return path, x


class Ctx:
    def __init__(s, g):
        s.g, s.n, s.E = g, g.n, Engine(g)
        s.m = sum(len(set(x)) for x in g.succ)

    def ck(s, val, L):
        return (s.E.rew[val[0]], s.E.weight(val[1] >> (L + 1) << (L + 1)))

    def key(s, val):
        return s.E.key(val)

    def w(s, val):
        return s.E.weight(val[1])

    def lev(s, x, y):
        if x[0] != y[0]: return float("inf")
        d = x[1] ^ y[1]
        if d: return d.bit_length() - 1
        return -1 if x[2] != y[2] else BOT


def state_info(ctx, sg, tu, st, name):
    g, n, E = ctx.g, ctx.n, ctx.E
    xe, tf = E.evaluate(tuple(sg[v] if g.owner[v] == 0 else -1 for v in range(n)))
    hn = [sg[v] if g.owner[v] == 0 else tf[v] for v in range(n)]
    wn = [sg[v] if g.owner[v] == 0 else tu[v] for v in range(n)]
    xi = [play_value(E, hn, v) for v in range(n)]
    wv = [play_value(E, wn, v) for v in range(n)]
    st.inc("ENGXI_checks")
    if any(xi[v] != tuple(xe[v]) for v in range(n)): st.bad("ENGXI", f"{name}: engine Xi != play value of (sigma, sigmabar)")
    D = frozenset(u for u in range(n) if g.owner[u] == 1 and hn[u] != tu[u])
    uv, pi = {}, {}
    for v in range(n):
        path, _ = lasso(wn, v)
        for i, x in enumerate(path):
            if x in D: uv[v] = x; pi[v] = path[:i]; break
    h3 = all(xi[u][0] == wv[u][0] for u in D)
    MD = max((ctx.lev(xi[u], wv[u]) for u in D), default=BOT)
    Is = set(E.improving(tuple(sg), xe))
    Is_own = set((x, z) for x in range(n) if g.owner[x] == 0 for z in set(g.succ[x])
                 if z != sg[x] and ctx.key(xi[z]) > ctx.key(xi[sg[x]]))
    if Is != Is_own: st.bad("ISIG", f"{name}: engine I_sigma != own")
    Iw = set((x, z) for x in range(n) if g.owner[x] == 0 for z in set(g.succ[x])
             if z != sg[x] and ctx.key(wv[z]) > ctx.key(wv[sg[x]]))
    return dict(sg=sg, tu=tu, xi=xi, w=wv, hn=hn, wn=wn, D=D, u=uv, pi=pi, h3=h3, MD=MD, Is=Is, Iw=Iw,
                lamX=tuple(x[0] for x in xi), lamW=tuple(x[0] for x in wv))


def forbidden(ctx, S, L, x, z):
    a = S["sg"][x]
    if z == a: return False
    return ctx.ck(S["w"][z], L) > ctx.ck(S["w"][a], L) and not ctx.key(S["xi"][z]) > ctx.key(S["xi"][a])


def levels(ctx, I, a, b):
    n = ctx.n
    if n <= LALL: return list(range(-1, n))
    fin = [I[k]["MD"] for k in range(a, b + 1) if I[k]["MD"] != float("inf")]
    md = min(int(max(fin + [-1])), n - 1)
    return sorted(set([-1, 0, n // 2, n - 2, md]))


def check_run(gp, states, fbs, st, name):
    ctx = Ctx(gp); g, n = gp, gp.n
    I = [state_info(ctx, s, t, st, f"{name}@{k}") for k, (s, t) in enumerate(states)]
    st.inc("runs"); st.inc("states", len(I))
    for k, S in enumerate(I):
        st.inc("FZP_checks")
        if any(ctx.key(S["xi"][v]) > ctx.key(S["w"][v]) for v in range(n)): st.bad("FZP", f"{name}@{k}: Xi > W somewhere")
    tauk = [tuple(t[v] for v in range(n) if g.owner[v] == 1) for _, t in states]
    key = [(I[k]["lamX"], tauk[k]) for k in range(len(states))]
    k0 = 0
    while k0 < len(states):
        k1 = k0
        while k1 + 1 < len(states) and key[k1 + 1] == key[k0]: k1 += 1
        a = k0
        while a <= k1:
            b = a
            while b < k1 and not fbs[b]: b += 1
            if b > a: check_ffrun(ctx, I, a, b, st, name)
            a = b + 1
        k0 = k1 + 1


def maximal_subruns(a, b, ok_state, same=None):
    """maximal [p, q] within [a, b] with ok_state at every state and same(p, k) for every k in [p, q]"""
    out, k = [], a
    while k <= b:
        if not ok_state(k): k += 1; continue
        e = k
        while e + 1 <= b and ok_state(e + 1) and (same is None or same(k, e + 1)): e += 1
        out.append((k, e)); k = e + 1
    return out


def check_ffrun(ctx, I, a, b, st, name):
    n = ctx.n
    st.inc("ff_runs"); st.inc("ff_transitions", b - a)
    st.mxr("max_ff_run_transitions", (b - a, f"{name}@{a} n {n}"))
    # PIECE_D (a) at every state with a successor in the run (S4a transition)
    for k in range(a, b):
        check_pda(ctx, I, k, st, name)
    for k in range(a, b + 1):
        brute_premises(ctx, I, k, st, name, k == b)
    for p, q in maximal_subruns(a, b, lambda k: I[k]["h3"]):
        if q > p: check_h3run(ctx, I, p, q, st, name)
    for p, q in maximal_subruns(a, b, lambda k: True, lambda k, e: I[k]["lamW"] == I[e]["lamW"]):
        if q > p: check_iirun(ctx, I, p, q, st, name)


def split_edges(ctx, S):
    g, n = ctx.g, ctx.n
    out = []
    for x in range(n):
        if g.owner[x] != 0: continue
        a = S["sg"][x]
        for z in set(g.succ[x]):
            if z == a: continue
            if (ctx.key(S["xi"][z]) > ctx.key(S["xi"][a])) != (ctx.key(S["w"][z]) > ctx.key(S["w"][a])): out.append((x, z))
    return out


def gtau_values(ctx, sg, tu):
    g, n = ctx.g, ctx.n
    nx = [sg[v] if g.owner[v] == 0 else tu[v] for v in range(n)]
    return [play_value(ctx.E, nx, v) for v in range(n)]


def brute_premises(ctx, I, k, st, name, last):
    """P1: S1's sigmabar is Odd's pointwise optimum in G_sigma; P2: S4a's sigma_(k+1) is Even's pointwise optimum in H_k (G_tau arena
    with sigma_k(x) and I_sigma_k(x)); brute force when the strategy count <= BRUTE"""
    g, n = ctx.g, ctx.n
    S = I[k]
    odd = [v for v in range(n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1]
    tot = 1
    for v in odd: tot *= len(set(g.succ[v]))
    if tot <= BRUTE:
        st.inc("P1_brute_states"); st.inc("P1_brute_strategies", tot)
        xk = [ctx.key(v) for v in S["xi"]]
        for combo in itertools.product(*[sorted(set(g.succ[v])) for v in odd]):
            tu = list(S["tu"])
            for v, z in zip(odd, combo): tu[v] = z
            vals = gtau_values(ctx, S["sg"], tu)
            if any(ctx.key(vals[v]) < xk[v] for v in range(n)): st.bad("P1", f"{name}@{k}: sigmabar not Odd-optimal"); break
    if last: return
    T = I[k + 1]
    ch = {x: sorted({S["sg"][x]} | {z for (y, z) in S["Is"] if y == x}) for x in range(n) if g.owner[x] == 0}
    choosers = [x for x in ch if len(ch[x]) > 1]
    tot = 1
    for x in choosers: tot *= len(ch[x])
    if tot > BRUTE: return
    st.inc("P2_brute_transitions"); st.inc("P2_brute_strategies", tot)
    best = [ctx.key(v) for v in T["w"]]
    for combo in itertools.product(*[ch[x] for x in choosers]):
        sg = list(S["sg"])
        for x, z in zip(choosers, combo): sg[x] = z
        vals = gtau_values(ctx, sg, S["tu"])
        if any(ctx.key(vals[v]) > best[v] for v in range(n)): st.bad("P2", f"{name}@{k}: sigma_(k+1) not an H_k optimum"); return


def check_pda(ctx, I, k, st, name):
    g, n = ctx.g, ctx.n
    S, T = I[k], I[k + 1]
    if split_edges(ctx, S): return
    st.inc("PDa_aligned_states")
    if S["Is"] != S["Iw"]: st.bad("PDa", f"{name}@{k}: aligned but I_sigma != G_tau improving set")
    # arena of G_tau: Even x may use sigma_k(x) or an improving edge
    ch = {x: sorted({S["sg"][x]} | {z for (y, z) in S["Iw"] if y == x}) for x in range(n) if g.owner[x] == 0}
    choosers = [x for x in ch if len(ch[x]) > 1]
    tot = 1
    for x in choosers: tot *= len(ch[x])
    for x in ch:
        if T["sg"][x] not in ch[x]: st.bad("PDa", f"{name}@{k}: sigma_(k+1)({x}) outside the arena")
    if tot > BRUTE: st.inc("PDa_arena_too_big"); return
    st.inc("PDa_brute_arenas"); st.inc("PDa_brute_strategies", tot)
    best = [ctx.key(v) for v in T["w"]]
    for combo in itertools.product(*[ch[x] for x in choosers]):
        sg = list(S["sg"])
        for x, z in zip(choosers, combo): sg[x] = z
        vals = gtau_values(ctx, sg, S["tu"])
        if any(ctx.key(vals[v]) > best[v] for v in range(n)):
            st.bad("PDa_opt", f"{name}@{k}: sigma_(k+1) not a G_tau arena optimum"); return


def check_h3run(ctx, I, p, q, st, name):
    g, n, E = ctx.g, ctx.n, ctx.E
    st.inc("h3_runs"); st.inc("h3_transitions", q - p)
    st.mxr("max_h3_run_transitions", (q - p, f"{name}@{p} n {n}"))
    # OFFSET (a)
    for k in range(p, q + 1):
        if I[k]["lamX"] != I[k]["lamW"]: st.bad("OFFa", f"{name}@{k}: lambda_Xi != lambda_W")
        if I[k]["lamW"] != I[p]["lamW"]: st.bad("OFFa", f"{name}@{k}: lambda not constant on S")
    sX = [[ctx.w(I[k]["xi"][v]) for v in range(n)] for k in range(p, q + 1)]
    sW = [[ctx.w(I[k]["w"][v]) for v in range(n)] for k in range(p, q + 1)]
    for j in range(q - p):
        st.inc("OFFa_transitions")
        for v in range(n):
            if sX[j + 1][v] < sX[j][v] or sW[j + 1][v] < sW[j][v]: st.bad("OFFa", f"{name}@{p + j}: score drops at {v}")
    Dl = [[sW[j][v] - sX[j][v] for v in range(n)] for j in range(q - p + 1)]
    # OFFSET (b), (c), per state; collect the rank sets of U_S per state
    Urank = []
    for j in range(q - p + 1):
        S = I[p + j]; ranks = set()
        dl = {}
        for u in S["D"]:
            sd = S["xi"][u][1] ^ S["w"][u][1]
            rs = [r for r in range(n) if sd >> r & 1]
            ranks |= set(rs)
            val = sum((1 if E.rankpar[r] == 0 else -1) * (1 << r) * (1 if S["w"][u][1] >> r & 1 else -1) for r in rs)
            dl[u] = ctx.w(S["w"][u]) - ctx.w(S["xi"][u])
            st.inc("OFFc_checks")
            if val != dl[u]: st.bad("OFFc", f"{name}@{p + j}: delta({u}) != signed sum over the symmetric difference")
            if rs and max(rs) > max(S["MD"], -1): st.bad("OFFc", f"{name}@{p + j}: rank above M_D in delta({u})")
        Urank.append(ranks)
        for v in range(n):
            st.inc("OFFb_checks")
            if v not in S["u"]: exp = 0
            elif S["lamW"][v] in S["pi"][v]: exp = 0
            else: exp = dl[S["u"][v]]
            if Dl[j][v] != exp: st.bad("OFFb", f"{name}@{p + j}: v {v} offset {Dl[j][v]} expected {exp}")
        # MERGE-B
        cls = {}
        for v in range(n): cls.setdefault((S["lamW"][v], Dl[j][v]), []).append(v)
        for vs in cls.values():
            for y in vs[1:]:
                st.inc("MERGE_checks")
                if sX[j][y] - sX[j][vs[0]] != sW[j][y] - sW[j][vs[0]]: st.bad("MERGE", f"{name}@{p + j}")
    # TWIN-GAP on every sub-run (or only the maximal one)
    subs = [(p, q)]
    if TWSUB and q - p <= SUBCAP: subs = [(x, y) for x in range(p, q + 1) for y in range(x + 1, q + 1)]
    for x0, x1 in subs:
        tg_check(ctx, I, p, x0, x1, sX, sW, Dl, Urank, st, name, x0 == p and x1 == q)
    # SPLIT-RED
    nsplit = sum(1 for k in range(p, q) if split_edges(ctx, I[k]))
    bound = nsplit + (nsplit + 1) * (n + ctx.m - 1)
    st.inc("SPR_runs"); st.mxr("SPR_max_ratio_x1000", (1000 * (q - p) // bound, f"{name}@{p} T {q - p} Nsplit {nsplit} n {n}"))
    if q - p > bound: st.bad("SPR", f"{name}@{p}: {q - p} transitions > {bound}")


def tg_check(ctx, I, p, x0, x1, sX, sW, Dl, Urank, st, name, maximal):
    n = ctx.n
    st.inc("TG_subruns")
    Ls = int(max(max(I[k]["MD"] for k in range(x0, x1 + 1)), -1))
    U = set().union(*[Urank[k - p] for k in range(x0, x1 + 1)])
    for k in range(x0, x1 + 1):
        for v in range(n):
            if not U:
                if Dl[k - p][v] != 0: st.bad("OFFc", f"{name}@{k}: U_S empty, offset nonzero")
            elif Dl[k - p][v] % (1 << min(U)) != 0: st.bad("OFFc", f"{name}@{k}: offset not a multiple of 2^l_S")
    if not U:
        for k in range(x0, x1):
            for v in range(n):
                if Dl[k + 1 - p][v] != Dl[k - p][v]: st.bad("TG", f"{name}: U_S empty, offset changes")
        return
    lS = min(U); B = Ls - lS + 1
    tailb = (2 ** (Ls + 2) - 2) // (2 ** lS)
    if MUT == "tg4": tailb //= 4
    for v in range(n):
        Nv = tail = 0; cons = 0
        t0 = x0 + n - 1
        if t0 < x1:
            rW = sW[x1 - p][v] - sW[t0 - p][v]; rX = sX[x1 - p][v] - sX[t0 - p][v]
            cap = 2 ** (Ls + 1) - 1 if MUT != "tgr" else 2 ** Ls - 1
            st.inc("TGii_rise_checks")
            if rW > cap or rX > cap: st.bad("TGii_rise", f"{name}@{x0}..{x1}: v {v} rises {rW}, {rX} > {cap}")
            if rW + rX: st.inc("TGii_rise_nonzero"); st.mxr("TGii_max_rise_over_cap_x1000", (1000 * max(rW, rX) // max(cap, 1), f"{name}@{x0}..{x1} v {v}"))
        for k in range(x0, x1):
            d = Dl[k + 1 - p][v] - Dl[k - p][v]
            if d == 0: continue
            Nv += 1
            if k >= x0 + n - 1: tail += 1; cons += abs(d)
            st.inc("TG_changes")
            if d > 0 and sW[k + 1 - p][v] - sW[k - p][v] < d: st.bad("TGi", f"{name}@{k}: v {v}")
            if d < 0 and sX[k + 1 - p][v] - sX[k - p][v] < -d: st.bad("TGi", f"{name}@{k}: v {v}")
        if t0 < x1 and cons > (sW[x1 - p][v] - sW[t0 - p][v]) + (sX[x1 - p][v] - sX[t0 - p][v]):
            st.bad("TGii_cons", f"{name}@{x0}..{x1}: v {v}")
        if tail > tailb: st.bad("TGii", f"{name}@{x0}..{x1}: v {v} tail {tail} > {tailb}")
        if Nv > (n - 1) + 2 ** (B + 1): st.bad("TGiii", f"{name}@{x0}..{x1}: v {v}")
        if maximal:
            st.mxr("TG_max_Nv", (Nv, f"{name}@{x0} v {v} B {B} n {n}"))
            st.mxr("TG_max_B", (B, f"{name}@{x0} n {n}"))
        if tail: st.inc("TG_tail_changes", tail); st.mxr("TG_max_tail", (tail, f"{name}@{x0}..{x1} v {v} bound {tailb}"))


def simple_paths_to(ctx, tu, cyc, x, rng, exhaustive):
    """simple paths of G_tau from x ending at a vertex of cyc (stop at the first cyc vertex)"""
    g = ctx.g
    def nexts(y): return [tu[y]] if g.owner[y] == 1 else sorted(set(g.succ[y]))
    out = []
    if exhaustive:
        def dfs(y, vis, path):
            if y in cyc: out.append(tuple(path)); return
            for z in nexts(y):
                if z not in vis:
                    vis.add(z); path.append(z); dfs(z, vis, path); path.pop(); vis.discard(z)
        dfs(x, {x}, [x])
        return out
    for _ in range(RANDP):
        path, vis, y = [x], {x}, x
        while y not in cyc:
            cand = [z for z in nexts(y) if z not in vis]
            if not cand: path = None; break
            y = rng.choice(cand); path.append(y); vis.add(y)
        if path: out.append(tuple(path))
    return out


def value_of(ctx, r):
    E = ctx.E; u = r[-1]; m = 0
    for y in r[:-1]:
        if E.rank[y] > E.rank[u]: m |= E.bit[y]
    return (u, m, len(r) - 1)


def clean(ctx, I, F, r, k, k0):
    """schedule of r at k clean; F[(t, L)] = set of forbidden edges at t"""
    g = ctx.g
    m = len(r) - 1
    if k - m < k0: return False
    if MUT == "noforb": return True
    for qq in range(m):
        if g.owner[r[qq]] == 0:
            t = k - 1 - qq if MUT != "shift" else k - qq
            if (r[qq], r[qq + 1]) in F[t]: return False
    return True


def check_iirun(ctx, I, p, q, st, name):
    g, n, E = ctx.g, ctx.n, ctx.E
    st.inc("ii_runs"); st.inc("ii_transitions", q - p)
    rng = random.Random(hash((name, p)) & 0xffffffff)
    tu = I[p]["tu"]
    cyc = frozenset(v for v in range(n) if I[p]["lamW"][v] == v)
    mtau = sum(1 if g.owner[v] == 1 else len(set(g.succ[v])) for v in range(n))
    # PIECE_D (b)
    al = [not split_edges(ctx, I[k]) for k in range(p, q)]
    j = 0
    while j < len(al):
        if not al[j]: j += 1; continue
        e = j
        while e + 1 < len(al) and al[e + 1]: e += 1
        ln = e - j + 1
        st.inc("PDb_blocks"); st.mxr("PDb_max_block", (ln, f"{name}@{p + j} n {n} m_tau {mtau}"))
        lim = n if MUT == "piece" else n + mtau
        if ln >= lim: st.bad("PDb", f"{name}@{p + j}: block {ln} >= {lim}")
        j = e + 1
    wplay = {}
    for k in range(p, q + 1):
        for x in range(n):
            path, _ = lasso(I[k]["wn"], x)
            c = I[k]["lamW"][x]
            wplay[(k, x)] = tuple(path[:path.index(c) + 1])
    for L in levels(ctx, I, p, q):
        F = {}
        for k in range(p, q + 1):
            F[k] = set((x, z) for x in range(n) if g.owner[x] == 0 for z in set(g.succ[x]) if forbidden(ctx, I[k], L, x, z))
            # FZ
            for (x, z) in F[k]:
                st.inc("FZ_checks")
                if not ctx.key(I[k]["xi"][z]) < ctx.key(I[k]["w"][z]) or z not in I[k]["u"]:
                    st.bad("FZ", f"{name}@{k}: L {L} edge {(x, z)}")
            if MUT == "fz":
                for x in range(n):
                    if g.owner[x] != 0: continue
                    a = I[k]["sg"][x]
                    for z in set(g.succ[x]):
                        if z != a and ctx.ck(I[k]["w"][z], L) > ctx.ck(I[k]["w"][a], L) and z not in I[k]["u"]:
                            st.bad("FZmut", f"{name}@{k}")
        Wc = [[ctx.ck(I[k]["w"][x], L) for x in range(n)] for k in range(p, q + 1)]
        # CR-REL: (i_rel) at L = no forbidden edge
        for x0, x1 in maximal_subruns(p, q, lambda k: not F[k]):
            frz = 1 if MUT == "crrel1" else n - 1
            st.inc("CRREL_subruns")
            if x1 - x0 >= frz + 1:
                st.inc("CRREL_freeze_checks")
                if any(I[k]["D"] for k in range(x0, x1 + 1)): st.inc("CRREL_freeze_checks_D_nonempty")
                for k in range(x0 + frz, x1 + 1):
                    if Wc[k - p] != Wc[x0 + frz - p]: st.bad("CRREL", f"{name}@{k}: L {L}")
        # P^c_sch
        for k in range(p, q + 1):
            for x in range(n):
                paths = set(wplay[(t, x)] for t in range(p, q + 1))
                paths |= set(simple_paths_to(ctx, tu, cyc, x, rng, n <= PATHCAP))
                for r in paths:
                    if not clean(ctx, I, F, r, k, p): continue
                    st.inc("PSCH_clean_checks")
                    if Wc[k - p][x] < ctx.ck(value_of(ctx, r), L): st.bad("PSCH", f"{name}@{k}: L {L} x {x} r {r}")
        # FRZ-SCH over all s <= t
        for t in range(p, q + 1):
            for x in range(n):
                r = wplay[(t, x)]
                for s in range(p, t + 1):
                    if not clean(ctx, I, F, r, s, p): continue
                    st.inc("FRZS_checks")
                    if s < t and len(set(Wc[k2 - p][x] for k2 in range(p, q + 1))) > 1: st.inc("FRZS_content")
                    if any(Wc[s2 - p][x] != Wc[s - p][x] for s2 in range(s, t + 1)):
                        st.bad("FRZS", f"{name}: L {L} x {x} [{s}, {t}]")
        # CHARGE, UNF, K_F
        KF = set(k for k in range(p, q + 1) if F[k])
        if L == -1: st.inc("KF_states_Lm1", len(KF)); st.inc("forbidden_pairstates_Lm1", sum(len(F[k]) for k in range(p, q + 1)))
        charges = {}   # (x, s) -> list of (q, e, f)
        for x in range(n):
            nch = 0
            for s in range(p + 1, q + 1):
                if Wc[s - p][x] == Wc[s - 1 - p][x]: continue
                nch += 1; st.inc("CHG_changes")
                r = wplay[(s, x)]; m = len(r) - 1
                if s - 1 - m < p: st.inc("CHG_window"); continue
                ch = [(qq, (r[qq], r[qq + 1]), s - 2 - qq) for qq in range(m)
                      if g.owner[r[qq]] == 0 and (r[qq], r[qq + 1]) in F[s - 2 - qq]]
                if not ch: st.bad("CHG", f"{name}: L {L} x {x} change at {s - 1}->{s} neither window nor charged"); continue
                st.inc("CHG_charged"); charges[(x, s)] = ch
                for qq, e, f in ch: check_unf(ctx, I, F, p, q, s, qq, e, f, st, name, L)
            if nch > (n - 1) + (n - 1) * len(KF): st.bad("CHGKF", f"{name}: L {L} x {x}")
        # U_L(S) on the run and (optionally) every sub-run
        sw = [(k, (y, I[k + 1]["sg"][y])) for k in range(p, q) for y in range(n)
              if g.owner[y] == 0 and I[k + 1]["sg"][y] != I[k]["sg"][y]]
        subs = [(p, q)]
        if CHUSUB and q - p <= SUBCAP: subs = [(x0, x1) for x0 in range(p, q + 1) for x1 in range(x0 + 1, q + 1)]
        for x0, x1 in subs:
            Uev = [(k, e) for (k, e) in sw if x0 <= k < x1 and any(e in F[f] for f in range(max(k - n + 1, x0), k))]
            if (x0, x1) == (p, q):
                st.inc("CHU_U_events", len(Uev)); st.mxr("CHU_max_U_per_run", (len(Uev), f"{name}@{p} L {L} n {n}"))
                pv = {}
                for k, e in Uev: pv[e[0]] = pv.get(e[0], 0) + 1
                if pv: st.mxr("CHU_max_U_per_vertex", (max(pv.values()), f"{name}@{p} L {L}"))
            for x in range(n):
                nch = sum(1 for s in range(x0 + 1, x1 + 1) if Wc[s - p][x] != Wc[s - 1 - p][x])
                lim = (n - 1) * (1 + len(Uev)) if MUT != "chu0" else (n - 1) * len(Uev)
                st.inc("CHU_checks")
                if nch > lim: st.bad("CHU", f"{name}: L {L} x {x} [{x0}, {x1}] changes {nch} > {lim}")


def check_unf(ctx, I, F, p, q, s, qq, e, f, st, name, L):
    n = ctx.n
    y, z = e
    st.inc("UNF_checks")
    if I[s]["sg"][y] != z or I[f]["sg"][y] == z: st.bad("UNF", f"{name}: L {L} setup"); return
    kp = max(k for k in range(f, s) if I[k]["sg"][y] != z)
    ok = f < kp <= s - 1 <= f + n - 1 and I[kp + 1]["sg"][y] == z and e in I[kp]["Is"] and e not in F[kp]
    if not ok: st.bad("UNF", f"{name}: L {L} e {e} f {f} k' {kp} s {s}")
    if MUT == "unf": st.bad("UNFmut", f"{name}: forbidden edge switched into")


def run_game(gp, s, t, st, name):
    states, fbs = DC.Runner(gp).run(s, t)
    check_run(gp, states, fbs, st, name)


def read_start(gp, path):
    s, t = [x[0] for x in gp.succ], [x[0] for x in gp.succ]
    for line in open(path):
        parts = line.split()
        if not parts or parts[0] not in ("SIGMA0", "TAU0"): continue
        tgt = s if parts[0] == "SIGMA0" else t
        for kv in parts[1:]:
            v, w = map(int, kv.split(":")); tgt[v] = w
    return s, t


def starts(gp, r, rng):
    if r == 0: return list(Engine(gp).initial("best")), list(Engine(DC.dual(gp)).initial("best"))
    return [rng.choice(gp.succ[v]) for v in range(gp.n)], [rng.choice(gp.succ[v]) for v in range(gp.n)]


def main():
    st = Stats(); a = sys.argv[1:]
    if a[0] == "files":
        runs = int(a[2]) if len(a) > 2 else 3; rng = random.Random(1616)
        for path in [l.strip() for l in open(a[1]) if l.strip()]:
            gp = pg.read(os.path.join(DC.ROOT, path))
            for r in range(runs):
                s, t = starts(gp, r, rng); run_game(gp, s, t, st, f"{path}#{r}")
    elif a[0] == "random":
        N, nmin, nmax, seed = map(int, a[1:5]); k = int(a[5]) if len(a) > 5 else 2; ns = int(a[6]) if len(a) > 6 else 2
        rng = random.Random(seed)
        sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-H3")); import h3_check as H
        for i in range(N):
            nn = rng.randint(nmin, nmax)
            gp = DC.rand_game(rng, nn, "kO") if k == 0 else H.rand_kO(rng, nn, k)
            for r in range(1, ns + 1):
                s, t = starts(gp, r, rng); run_game(gp, s, t, st, f"random{seed}:{i}#{r}")
    elif a[0] == "start":
        gp = pg.read(a[1])
        if len(a) > 2:
            s, t = read_start(gp, a[2]); run_game(gp, s, t, st, os.path.basename(a[1]) + "#start")
        else:
            s, t = starts(gp, 0, None); run_game(gp, s, t, st, os.path.basename(a[1]) + "#S3")
    print("MODE", " ".join(a), "MUT", MUT or "-", "PATHCAP", PATHCAP, "LALL", LALL, "RANDP", RANDP)
    for k in sorted(st.c): print(f"{k}: {st.c[k]}")
    for k in sorted(st.mx): print(f"{k}: {st.mx[k]}")
    for v in st.viol: print("VIOLATION", v)
    print("RESULT", "FAIL" if st.c.get("VIOLATIONS") else "OK", f"violations={st.c.get('VIOLATIONS', 0)}")


if __name__ == "__main__":
    main()
