#!/usr/bin/env python3
"""REFEREE-2 successor 5 (Opus 5.5, D15): mechanical check of packet P-N5-U1 (docs/new/P-N5-U1-box31.md sha1 eb90788d @ trunk eee0d8a).
Own code. Definitions (play values, honest values, R, routes, (h), phases) come from my lane's R2-N5-RE/re_check.py. The N5 state
sequence is SPEC's (n5.py functions via re_check.n5_spec): Lemma TB and CASC are statements about SPEC's tie-breaks, so no
random-tie-break mode is used here. The VJ00 procedure is re-transcribed below from SPEC S1 with instrumentation (deleted edges,
final restricted graph, distances) and asserted equal to si.py's Engine.evaluate on every call.
Checks:
  LR   Lemma R on every S4a dual-arena evaluation (and on the plain Xi evaluations): every fully optimal edge survives; survivors of
       optimal length = fully optimal edges; survivors are path-set consistent. Also counts deleted edges that are optimal in
       (cycle node, path set) only (the statement's wording) and whether the deleting step had u = x.
  TB   at every non-fallback S4a transition (any state, tau_k fixed): key-min form (new choice = key-minimum among W'-optimal arena
       edges), TB-odd, TB-even as stated, and the Bellman step 2 (W'(x) = W_k(x) => W'(sigma_k x) (+) x = W'(x)), recording the case
       "x on sigma_k(x)'s W'-play".
  CASC every route-form piece: W-flat runs, a level-l R-vertex switches only at run steps <= l - 2.
  U1   every U1 piece (c_w more relevant than c_theta): (R1); kappa_w freeze index <= |R| - 1; K bound; total bound of Theorem U1.
  WC   every crossing-free interval with not-H2 (and the sub-case not-H1): w-change count bound; w = (c_w, {}, d), c_w in R; per stretch.
  MONO W non-decreasing at non-fallback transitions with tau constant.
Usage: u1_check.py random N nmin nmax seed   |   u1_check.py inst game.pg [runs]   (run 0 = SPEC S3 start; runs > 0 random starts)"""
import sys, os, random
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-RE"))
for p in ("experiments/new", "experiments/si", "experiments/harness"): sys.path.insert(0, os.path.join(ROOT, p))
import re_check as RC
import pg as lpg, n5
from si import Engine

EVEN, ODD = 0, 1

# ---------------------------------------------------------------- instrumented VJ00 procedure (SPEC S1 (i)-(vi))
def vj_eval(E, strat):
    n, rank = E.n, E.rank
    gs = [([strat[v]] if E.owner[v] == EVEN else E.succ[v]) for v in range(n)]
    gp = [[] for _ in range(n)]
    for v in range(n):
        for w in gs[v]: gp[w].append(v)
    alive = [True] * n; val = [None] * n; tau_full = [None] * n; info = []
    for v in sorted(range(n), key=lambda x: E.rew[x]):
        if not alive[v]: continue
        rv = rank[v]; seen = {v}; st = [v]; found = False
        while st and not found:
            x = st.pop()
            for y in gs[x]:
                if y == v: found = True; break
                if alive[y] and rank[y] < rv and y not in seen: seen.add(y); st.append(y)
        if not found: continue
        R = {v}; st = [v]
        while st:
            x = st.pop()
            for y in gp[x]:
                if alive[y] and y not in R: R.add(y); st.append(y)
        hs = {x: [y for y in gs[x] if y in R] for x in R}
        hp = {x: [y for y in gp[x] if y in R] for x in R}
        path = {x: 0 for x in R}; deleted = {}          # (x, y) -> u (the step that deleted it)
        def reach(start, excl):
            s = {start}; st2 = [start]
            while st2:
                x = st2.pop()
                for y in hp[x]:
                    if y != excl and y not in s: s.add(y); st2.append(y)
            return s
        def restrict(x, M, u):
            keep = [y for y in hs[x] if y in M]
            for y in hs[x]:
                if y not in M: hp[y].remove(x); deleted[(x, y)] = u
            hs[x] = keep
        for u in sorted((x for x in R if rank[x] > rv), key=lambda x: -rank[x]):
            if E.par[u] == 0:
                M = reach(v, u)
                for q in R:
                    if q not in M: path[q] |= E.bit[u]
                restrict(u, M, u)
                for q in M: restrict(q, M, u)
            else:
                M = reach(u, v)
                for q in M:
                    path[q] |= E.bit[u]
                    if q != u: restrict(q, M, u)
        dist = {}; tau = {}
        if E.par[v] == 0:
            state = {}
            def longest(x):
                if x == v: return 0
                if x in state:
                    if state[x] is None: raise RuntimeError("cycle")
                    return state[x]
                state[x] = None; best, arg = -1, None
                for y in hs[x]:
                    d = longest(y)
                    if d > best: best, arg = d, y
                state[x] = best + 1; tau[x] = arg; return best + 1
            for x in R: dist[x] = longest(x)
        else:
            dist[v] = 0; layer = [v]
            while layer:
                nxt = []
                for x in layer:
                    for y in hp[x]:
                        if y not in dist: dist[y] = dist[x] + 1; tau[y] = x; nxt.append(y)
                layer = nxt
        if E.owner[v] == ODD:
            par = {v: None}; st = [v]; cyc = None
            while st and cyc is None:
                x = st.pop()
                for y in gs[x]:
                    if y == v: cyc = x; break
                    if alive[y] and rank[y] < rv and y not in par: par[y] = x; st.append(y)
            x = cyc
            while par[x] is not v and par[x] is not None: x = par[x]
            tau[v] = x if x != v else cyc
        for x in R:
            val[x] = (v, path[x], dist[x]); alive[x] = False
            if E.owner[x] == ODD: tau_full[x] = tau[x]
        info.append((v, R, {x: list(hs[x]) for x in R}, dict(dist), deleted, {x: list(gs[x]) for x in R}))
    return val, tau_full, info

def check_lemma_R(E, strat, st, name):
    val, tf, info = vj_eval(E, strat)
    ref = E.evaluate(tuple(strat))
    if (val, tf) != (list(ref[0]), list(ref[1])): st.bad(f"{name} LR transcription != si.py evaluate")
    for v, R, hs, dist, deleted, gs in info:
        for x in R:
            if x == v: continue
            for y in gs[x]:
                if y not in R: continue
                full = val[x] == E.extend(x, val[y])
                ext = E.extend(x, val[y])
                setopt = ext[0] == val[x][0] and ext[1] == val[x][1]
                surv = y in hs[x]
                st.c["LR_edges"] += 1
                if E.owner[x] == ODD: st.c["LR_edges_optimiser"] += 1
                if full and not surv: st.bad(f"{name} LR full-optimal edge {x}->{y} deleted (u={deleted.get((x, y))})")
                if surv and not setopt: st.bad(f"{name} LR survivor {x}->{y} not path-set consistent")
                if surv and (dist[y] == dist[x] - 1) != full: st.bad(f"{name} LR survivor-of-optimal-length != full-optimal {x}->{y}")
                if full: st.c["LR_full_optimal"] += 1
                if setopt and not surv:
                    u = deleted[(x, y)]
                    st.c[f"LR_setopt_deleted u==x:{u == x} owner_x:{E.owner[x]}"] += 1
                    if x != y: st.c["LR_setopt_deleted_xney"] += 1; st.ex("LR_setopt_deleted_xney", f"{name} cyclenode={v} x={x} y={y} u={u}")
                    st.ex("LR_setopt_deleted", f"{name} cyclenode={v} x={x} y={y} u={u} val[x]={val[x]} ext={ext}")
    return val, tf

# ---------------------------------------------------------------- SPEC run with arena records
def spec_run(g, o, sigma, tau, st, name, lemmaR=True):
    lg = lpg.Game(list(g.prio), list(g.owner), [list(s) for s in g.succ])
    E, Ed = Engine(lg), Engine(n5.dual(lg)); n = g.n
    states, fbs, arenas = [(list(sigma), list(tau))], [], []
    while len(states) < 2000:
        sg, tu = states[-1]
        vs, _ = E.evaluate(tuple(sg)); Is = E.improving(tuple(sg), vs)
        vt, _ = Ed.evaluate(tuple(tu)); It = Ed.improving(tuple(tu), vt)
        if not Is and not It: break
        ns, nt = list(sg), list(tu); arena = None
        if Is:
            opt = {v: {sg[v]} for v in range(n) if g.owner[v] == 0}
            for v, w in Is: opt[v].add(w)
            succ = [sorted(opt[v]) if g.owner[v] == 0 else [tu[v]] for v in range(n)]
            Er = Engine(n5.dual(lpg.Game(list(g.prio), list(g.owner), succ)))
            strat = tuple(tu[v] if g.owner[v] == 1 else -1 for v in range(n))
            if lemmaR: _, best = check_lemma_R(Er, strat, st, f"{name}@{len(states) - 1}")
            else: _, best = Er.evaluate(strat)
            for v in range(n):
                if g.owner[v] == 0: ns[v] = best[v]
            arena = opt
        if It:
            opt = {v: {tu[v]} for v in range(n) if g.owner[v] == 1}
            for v, w in It: opt[v].add(w)
            succ = [sorted(opt[v]) if g.owner[v] == 1 else [sg[v]] for v in range(n)]
            Er = Engine(lpg.Game(list(g.prio), list(g.owner), succ))
            _, best = Er.evaluate(tuple(sg[v] if g.owner[v] == 0 else -1 for v in range(n)))
            for v in range(n):
                if g.owner[v] == 1: nt[v] = best[v]
        fb = 0
        if ns == sg and nt == tu:
            fb = 1
            if Is:
                for v in {v for v, _ in Is}: ns[v] = max((w for x, w in Is if x == v), key=lambda w: (E.key(vs[w]), w))
            else:
                for v in {v for v, _ in It}: nt[v] = max((w for x, w in It if x == v), key=lambda w: (Ed.key(vt[w]), w))
        states.append((ns, nt)); fbs.append(fb); arenas.append(arena)
    # cross-check with re_check.n5_spec (an independent copy of the same loop)
    s2, f2 = RC.n5_spec(g, o, sigma, tau)
    if s2 != states or f2 != fbs: st.bad(f"{name} spec_run differs from re_check.n5_spec")
    return states, fbs, arenas

# ---------------------------------------------------------------- helpers on G (play values, my definitions)
def fmap(g, s, t): return [s[v] if g.owner[v] == 0 else t[v] for v in range(g.n)]

def ext(g, x, val):
    c, P, l = val
    return (c, P | (frozenset([x]) if g.rel(x, c) else frozenset()), l + 1)

def pk(g, path):        # root-first index sequence of a play path v..c (c last), c excluded
    return list(reversed(path[:-1]))

def H12(g, o, S):
    return (not RC._returns(S.fh, o)), (not RC._returns(S.f, o))

# ---------------------------------------------------------------- TB at every non-fallback S4a transition
def check_TB(g, o, states, fbs, arenas, st, name):
    for k in range(len(fbs)):
        if fbs[k] or arenas[k] is None: continue
        (s0, t0), (s1, _) = states[k], states[k + 1]
        f0, f1 = fmap(g, s0, t0), fmap(g, s1, t0)
        W0, P0, _ = RC.vals_of(g, f0); W1, P1, _ = RC.vals_of(g, f1)
        for x in range(g.n):          # F1: W' dominates W_k pointwise
            if g.cmp(W1[x], W0[x]) < 0: st.bad(f"{name} k={k} F1 W'<W at {x}")
        for v in range(g.n):
            if g.owner[v] != 0: continue
            c = W1[v][0]
            if c == v: continue
            A = arenas[k][v]
            O = [z for z in A if ext(g, v, W1[z]) == W1[v]]
            st.c["TB_key_checks"] += 1
            if s1[v] not in O: st.bad(f"{name} k={k} TBkey new choice of {v} not W'-optimal"); continue
            if g.even[c]: kmin = min(O, key=lambda z: pk(g, P1[z]))
            else: kmin = min(O)
            if kmin != s1[v]: st.bad(f"{name} k={k} TBkey v={v} chose {s1[v]} key-min {kmin} c={c} even={g.even[c]}")
            if len(O) > 1: st.c["TB_key_nontrivial"] += 1
            # Bellman step 2 at v (x := v) and the case "x on sigma_k(x)'s W'-play"
            if W1[v] == W0[v]:
                y = s0[v]; onp = v in P1[y][:-1]; onc = (not onp) and v in RC._cycle(g, f1, y)
                st.c[f"TB_step2 x_on_play:{onp or onc}"] += 1
                if onp: st.c["TB_step2 x_on_path_before_c"] += 1; st.ex("TB_step2_on_path", f"{name} k={k} x={v} y={y}")
                if onc: st.c["TB_step2 x_on_cycle_only"] += 1
                if ext(g, v, W1[y]) != W1[v]: st.bad(f"{name} k={k} TB step2 fails at {v} (on play {on})")
            if s1[v] == s0[v] or W1[v] != W0[v]: continue
            if not g.even[c]:
                st.c["TB_odd"] += 1
                if not s1[v] < s0[v]: st.bad(f"{name} k={k} TB-odd v={v} {s0[v]}->{s1[v]}")
            else:
                along = P0[v][:-1]
                if all(W1[x] == W0[x] for x in along):
                    st.c["TB_even"] += 1
                    a, b = pk(g, P1[v]), pk(g, P0[v])
                    if not a < b: st.bad(f"{name} k={k} TB-even v={v} new {a} old {b}")
                else: st.c["TB_even_hyp_fails"] += 1

# ---------------------------------------------------------------- pieces, CASC, U1, WC
def check_run(g, o, states, fbs, st, name):
    A = [RC.analyse(g, o, s, t) for s, t in states]
    T = len(states) - 1
    for S in A: S.H1, S.H2 = H12(g, o, S)
    inphase = [A[k].lamX == A[k + 1].lamX and A[k].lamU == A[k + 1].lamU and states[k][1] == states[k + 1][1] for k in range(T)]
    # MONO
    for k in range(T):
        if inphase[k] and not fbs[k]:
            for v in range(g.n):
                if g.cmp(A[k + 1].W[v], A[k].W[v]) < 0: st.bad(f"{name} MONO k={k} v={v}")
    # crossing-free intervals
    k = 0
    while k <= T:
        j = k
        while j < T and inphase[j] and A[j].R == A[j + 1].R: j += 1
        interval(g, o, A, states, fbs, k, j, st, name)
        k = j + 1

def rf(S, o): return (S.H1 or S.lamX[o] == o) and (S.H2 or S.W[o][0] == o)

def interval(g, o, A, states, fbs, i0, i1, st, name):
    R = A[i0].R; r = len(R)
    st.c["intervals"] += 1
    # ---- WC
    if not A[i0].H2:
        st.c["WC_intervals(notH2)"] += 1
        if not A[i0].H1: st.c["WC_intervals(notH1notH2)"] += 1
        wc = sum(1 for k in range(i0, i1) if A[k].W[o] != A[k + 1].W[o]); fI = sum(fbs[i0:i1])
        for k in range(i0, i1):          # fallbacks inside the interval: state type and effect on w (for the §6 reading)
            if not fbs[k]: continue
            typ = "EQ" if A[k].Xi == A[k].W else ("THR" if A[k].h else "OTHER")
            d = g.cmp(A[k + 1].W[o], A[k].W[o])
            st.c[f"WC_fallback_in_I type={typ} notH1={not A[i0].H1} w_change={d}"] += 1
            if d < 0: st.ex(f"WC_fallback_w_down_{typ}", f"{name} k={k} interval [{i0},{i1}] w {A[k].W[o]} -> {A[k + 1].W[o]}")
        st.mx["WC_max"] = max(st.mx["WC_max"], wc)
        if wc > (fI + 1) * (r * r - 1) + fI: st.bad(f"{name} WC bound [{i0},{i1}] wc={wc} f={fI} |R|={r}")
        for k in range(i0, i1 + 1):
            if A[k].H2: st.bad(f"{name} WC H2 not constant")
            cw, P, d = A[k].W[o]
            if P or cw not in R or d > r - 1: st.bad(f"{name} WC shape k={k} w={A[k].W[o]}")
        # per stretch: monotone, c_w changes <= r-1, d changes per c_w <= r-1
        k = i0
        while k <= i1:
            j = k
            while j < i1 and not fbs[j]: j += 1
            cwch = 0; dch = Counter()
            for t in range(k, j):
                a, b = A[t].W[o], A[t + 1].W[o]
                if g.cmp(b, a) < 0: st.bad(f"{name} WC w decreased at non-fallback k={t}")
                if a[0] != b[0]: cwch += 1
                elif a != b: dch[a[0]] += 1
            if cwch > r - 1 or any(x > r - 1 for x in dch.values()): st.bad(f"{name} WC per-stretch counts")
            st.mx["WC_cw_changes_per_stretch"] = max(st.mx["WC_cw_changes_per_stretch"], cwch)
            k = j + 1
    # ---- pieces
    k = i0
    while k <= i1:
        if not rf(A[k], o): k += 1; continue
        j = k
        while j < i1 and rf(A[j + 1], o) and A[j + 1].theta == A[k].theta and A[j + 1].w == A[k].w: j += 1
        piece(g, o, A, states, fbs, R, k, j, st, name)
        k = j + 1

def piece(g, o, A, states, fbs, R, p0, p1, st, name):
    S0 = A[p0]; ct, cw = S0.theta[0], S0.w[0]; r = len(R)
    U1 = g.rank[cw] > g.rank[ct]
    kind = "U1" if U1 else ("P3" if g.rank[ct] > g.rank[cw] else "EQc")
    st.c[f"pieces_{kind}"] += 1
    if p1 > p0: st.c[f"pieces_{kind}_nontrivial"] += 1
    # (R1)
    for k in range(p0, p1 + 1):
        S = A[k]
        for v in R:
            if v == o: continue
            if S.Xi[v] != RC.prefix(g, S.pi[v], S.theta) or S.W[v] != RC.prefix(g, S.pi[v], S.w):
                st.bad(f"{name} R1 k={k} v={v}"); break
    # CASC on every route-form piece
    Ev = [v for v in R if g.owner[v] == 0 and v != o]
    t = p0
    while t < p1:
        if fbs[t] or any(A[t].W[v] != A[t + 1].W[v] for v in R): t += 1; continue
        u = t
        while u < p1 and not fbs[u] and all(A[u].W[v] == A[u + 1].W[v] for v in R): u += 1
        # run = transitions t..u-1, step s = x - t
        st.c[f"CASC_runs_{kind}"] += 1
        st.mx[f"CASC_run_len_{kind}"] = max(st.mx[f"CASC_run_len_{kind}"], u - t)
        sw = Counter()
        for x in range(t, u):
            for v in Ev:
                if states[x][0][v] != states[x + 1][0][v]:
                    l = len(A[x].pi[v]); s = x - t; sw[v] += 1
                    st.c[f"CASC_switches_{kind}"] += 1
                    st.mx["CASC_max(step-level+2)"] = max(st.mx.get("CASC_max(step-level+2)", -99), s - l + 2)
                    if s > l - 2: st.bad(f"{name} CASC run[{t},{u}) step {s} v={v} level {l} kind {kind}")
        if sw: st.mx["CASC_max_switches_one_vertex_in_run"] = max(st.mx["CASC_max_switches_one_vertex_in_run"], max(sw.values()))
        t = u
    if not U1: return
    # ---- Theorem U1
    f = sum(fbs[p0:p1]); L = p1 - p0
    kap = lambda S, v: frozenset(x for x in S.pi[v] if g.rank[x] > g.rank[cw])
    last = -1
    for k in range(p0, p1):
        if any(kap(A[k], v) != kap(A[k + 1], v) for v in R if v != o): last = k - p0; st.c["U1_kappa_w_change_transitions"] += 1
    st.mx["U1_last_kappa_w_change_minus_R"] = max(st.mx.get("U1_last_kappa_w_change_minus_R", -99), last - r)
    if last > r - 1: st.bad(f"{name} U1 freeze: last kappa_w change at transition {last}, |R|={r}")
    Rch = sum(1 for k in range(p0, p1) if any(A[k].Xi[v] != A[k + 1].Xi[v] or A[k].W[v] != A[k + 1].W[v]
                                             or states[k][0][v] != states[k + 1][0][v] for v in R))
    st.c["U1_W_change_transitions"] += sum(1 for k in range(p0, p1) if any(A[k].W[v] != A[k + 1].W[v] for v in R))
    K = sum(1 for k in range(p0 + r, p1) if not fbs[k] and any(A[k].W[v] != A[k + 1].W[v] for v in R))
    Kb = (f + 1) * (r - 1) * (r - 2)
    bound = r + f + Kb + (Kb + f + 1) * (r - 2)
    if K > Kb: st.bad(f"{name} U1 K={K} > {Kb}")
    if Rch > bound: st.bad(f"{name} U1 bound Rch={Rch} > {bound}")
    st.c["U1_pieces_checked"] += 1
    if L > r: st.c["U1_pieces_longer_than_R (post-freeze part nonempty)"] += 1
    if L > 0: st.c["U1_nontrivial"] += 1
    if f: st.c["U1_with_fallback"] += 1
    st.mx["U1_max_Rch"] = max(st.mx["U1_max_Rch"], Rch)
    st.mx["U1_max_len"] = max(st.mx["U1_max_len"], L)
    st.mx["U1_max_K"] = max(st.mx["U1_max_K"], K)
    st.ex(f"U1_long", f"{name} piece [{p0},{p1}] |R|={r} c_theta={ct} c_w={cw} Rch={Rch} f={f}") if L >= 3 else None
    # U1-T style per-vertex counts after the freeze (context)
    xc = Counter()
    for k in range(p0 + max(last + 1, 0), p1):
        for v in R:
            if A[k].Xi[v] != A[k + 1].Xi[v]: xc[v] += 1
    if xc: st.mx["U1_postfreeze_max_Xi_changes_one_vertex"] = max(st.mx["U1_postfreeze_max_Xi_changes_one_vertex"], max(xc.values()))

# ---------------------------------------------------------------- main
def run_one(g, o, s, t, st, name):
    states, fbs, arenas = spec_run(g, o, s, t, st, name)
    check_TB(g, o, states, fbs, arenas, st, name)
    check_run(g, o, states, fbs, st, name)
    st.c["runs"] += 1; st.c["transitions"] += len(fbs); st.c["fallbacks"] += sum(fbs)
    return states, fbs

def br_start(g):
    def br(v, dual):
        def rr(w):
            p = g.prio[w] + (1 if dual else 0); r_ = p if p % 2 == 0 else -p
            return (r_, w if r_ % 2 == 0 else -w)
        return max(g.succ[v], key=rr)
    return [br(v, False) for v in range(g.n)], [br(v, True) for v in range(g.n)]

def one_odd(g):
    o = [v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) > 1]
    assert len(o) == 1, f"not C^1O: Odd choice vertices {o}"
    return o[0]

def report(st):
    for k in sorted(st.c): print(f"{k}: {st.c[k]}")
    for k in sorted(st.mx): print(f"{k}: {st.mx[k]}")
    for k, v in st.examples.items(): print(f"example {k}: {v}")
    for v in st.viol: print("VIOLATION", v)
    print("RESULT", "FAIL" if st.c["VIOLATIONS"] else "OK", f"violations={st.c['VIOLATIONS']}")

def main():
    st = RC.Stats(); st.mx = Counter()
    if sys.argv[1] == "random":
        N, nmin, nmax, seed = map(int, sys.argv[2:6]); rng = random.Random(seed)
        for i in range(N):
            g, o = RC.rand_game(rng, rng.randint(nmin, nmax)); one_odd(g)
            s, t = RC.rand_start(rng, g) if rng.random() < 0.5 else br_start(g)
            run_one(g, o, s, t, st, f"seed{seed}#{i}")
    else:
        path = sys.argv[2]; runs = int(sys.argv[3]) if len(sys.argv) > 3 else 1
        g = RC.parse(open(path).read()); o = one_odd(g); rng = random.Random(1)
        for r in range(runs):
            s, t = br_start(g) if r == 0 else RC.rand_start(rng, g)
            run_one(g, o, s, t, st, f"{os.path.basename(path)}#{r}")
    report(st)

if __name__ == "__main__":
    main()
