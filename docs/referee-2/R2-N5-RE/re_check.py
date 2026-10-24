#!/usr/bin/env python3
"""REFEREE-2 (Opus 5.5, D15) mechanical check of packet P-N5-RE (docs/new/P-N5-RE-box26.md @ trunk 52c7261).
Self-contained: every quantity is computed here from the definitions (play following, VJ00/SPEC S1 order, honest valuation as the
pointwise minimum over Odd's choices at o, Even's one-player optimum by switch-all SI to convergence). No lane code is imported in
the default ("own") mode. Mode "spec" takes the STATE SEQUENCE from experiments/new/n5.py's functions (SPEC tie-breaks) and checks it
with this file's definitions (each spec step is also checked to be a pointwise arena optimum by my definitions).

Own N5 (S2-S4 with RANDOM tie-breaks; the lemmas only use (F1), so they must hold for every optimum):
  S4a: Even's one-player optimum against tau in the arena {sigma(v)} u Is(v), from sigma by random-subset SI, then random
       value-preserving re-choices (another optimum); S4b: Odd's best option at o among {tau(o)} u It(o) against sigma (pointwise
       minimum, asserted to exist), random among value-identical options; S4c: fallback as SPEC (best value, ties larger index).
Checks (packet items): G(a) G(b) G(c); Wo; RM; RE (and its steps 2-3 at EVERY leave, with or without (NC)); PIECE (count, gate
identity of step 3, arena-optimum identity of step 4 on both pieces).
Usage: re_check.py random N nmin nmax seed [own|spec]   |   re_check.py inst game.pg [start] [own|spec] [runs]"""
import sys, os, random, itertools
from collections import Counter

# ---------------------------------------------------------------- game + values (SPEC S1, from the definitions)
class Game:
    def __init__(s, prio, owner, succ):
        s.n = len(prio); s.prio, s.owner, s.succ = list(prio), list(owner), [sorted(set(x)) for x in succ]
        order = sorted(range(s.n), key=lambda v: (s.prio[v], v))
        s.rank = [0] * s.n
        for i, v in enumerate(order): s.rank[v] = i
        s.even = [p % 2 == 0 for p in s.prio]

    def rel(s, u, c): return s.rank[u] > s.rank[c]          # u more relevant than c

    def play(s, f, v):
        """Value of the play from v under the full successor map f: (c, P, l) plus the path v..c (c last) and the cycle."""
        seen, path = {}, []
        x = v
        while x not in seen:
            seen[x] = len(path); path.append(x); x = f[x]
        cyc = path[seen[x]:]
        c = max(cyc, key=lambda u: s.rank[u])
        i = path.index(c)
        P = frozenset(u for u in path[:i] if s.rel(u, c))
        return (c, P, i), path[:i + 1], cyc

    def key(s, val):
        c, P, l = val
        pp = 2 * s.rank[c] + (0 if s.even[c] else 1)
        rew = pp if s.even[c] else -pp
        wt = sum((1 if s.even[u] else -1) << s.rank[u] for u in P)
        return (rew, wt, -l if s.even[c] else l)

    def cmp(s, a, b):
        ka, kb = s.key(a), s.key(b)
        return (ka > kb) - (ka < kb)

def parse(text):
    lines = [l.strip() for l in text.replace("\n", " ").split(";")]
    rows = [l for l in lines if l and not l.startswith("parity") and not l.startswith("start")]
    data = {}
    for r in rows:
        t = r.split()
        v, p, o = int(t[0]), int(t[1]), int(t[2])
        data[v] = (p, o, [int(x) for x in t[3].split(",")])
    n = max(data) + 1
    return Game([data[v][0] for v in range(n)], [data[v][1] for v in range(n)], [data[v][2] for v in range(n)])

def read_start(path):
    s, t = {}, {}
    for line in open(path):
        w = line.split()
        if not w: continue
        d = s if w[0] == "SIGMA0" else t
        for tok in w[1:]:
            a, b = tok.split(":"); d[int(a)] = int(b)
    return s, t

# ---------------------------------------------------------------- one-player machinery
def vals_of(g, f):
    out = [g.play(f, v) for v in range(g.n)]
    return [o[0] for o in out], [o[1] for o in out], [o[2] for o in out]

def even_optimum(g, f, arena, rng=None, perturb=0):
    """Even's pointwise-optimal strategy in the one-player arena (Odd fixed as in f; Even v may use arena[v]), by SI from f.
    Returns (f_opt, values). rng: random improving subsets; perturb: number of random value-preserving re-choices tried."""
    f = list(f)
    while True:
        val = vals_of(g, f)[0]
        imp = [(v, z) for v in range(g.n) if g.owner[v] == 0 for z in arena[v]
               if z != f[v] and g.cmp(val[z], val[f[v]]) > 0]
        if not imp: break
        if rng is None:
            sw = imp
        else:
            sw = [e for e in imp if rng.random() < 0.5] or [rng.choice(imp)]
        done = set()
        for v, z in sw:
            if v in done: continue
            best = max((zz for vv, zz in sw if vv == v), key=lambda zz: g.key(val[zz])) if rng is None else z
            f[v] = best; done.add(v)
    if rng is not None:
        for _ in range(perturb):
            v = rng.choice([x for x in range(g.n) if g.owner[x] == 0])
            z = rng.choice(sorted(arena[v]))
            if z == f[v]: continue
            f2 = list(f); f2[v] = z
            if vals_of(g, f2)[0] == val: f = f2
    return f, val

def odd_points(g, f, o, options):
    """Odd's best option at o against the rest of f: the option whose value vector is pointwise minimal (asserted)."""
    res = []
    for e in options:
        f2 = list(f); f2[o] = e; res.append((e, vals_of(g, f2)[0]))
    mins = [e for e, val in res if all(all(g.cmp(val[v], v2[v]) <= 0 for v in range(g.n)) for _, v2 in res)]
    assert mins, "no pointwise-minimal Odd option"
    return mins, dict(res)

# ---------------------------------------------------------------- per-state quantities
class State:
    pass

def analyse(g, o, sigma, tau):
    """sigma, tau: full maps (Even entries / Odd entries used). Returns a State with Xi, honest choice, W, U-cycle nodes, R, (h)."""
    S = State(); n = g.n
    f = [sigma[v] if g.owner[v] == 0 else tau[v] for v in range(n)]
    S.f = f
    mins, table = odd_points(g, f, o, g.succ[o])
    S.sbar = min(mins)                          # any pointwise-minimal choice gives the same Xi
    S.Xi = table[S.sbar]
    fh = list(f); fh[o] = S.sbar; S.fh = fh
    S.Xi_path = [g.play(fh, v)[1] for v in range(n)]
    S.W, S.W_path, _ = vals_of(g, f)
    # Odd's honest valuation U_tau = Even's best response to tau (pointwise max), read in G's order (Lemma R, R18 (d)).
    fu, S.U = even_optimum(g, f, [g.succ[v] for v in range(n)])
    S.lamX = tuple(S.Xi[v][0] for v in range(n)); S.lamU = tuple(S.U[v][0] for v in range(n))
    # R = vertices whose (sigma, tau)-path reaches o
    S.R = set()
    for v in range(n):
        x, seen = v, set()
        while x not in seen and x != o:
            seen.add(x); x = f[x]
        if x == o: S.R.add(v)
    S.pi = {}
    for v in S.R:
        p, x = [], v
        while x != o: p.append(x); x = f[x]
        S.pi[v] = p
    S.h = (not _returns(fh, o)) and (not _returns(f, o)) and S.Xi[o][0] == S.W[o][0]
    S.theta, S.w = S.Xi[o], S.W[o]
    # Odd's improving set at o (in G's order: smaller U is better for Odd)
    S.It = [z for z in g.succ[o] if z != tau[o] and g.cmp(S.U[z], S.U[tau[o]]) < 0]
    S.Is = [(v, z) for v in range(n) if g.owner[v] == 0 for z in g.succ[v]
            if z != sigma[v] and g.cmp(S.Xi[z], S.Xi[sigma[v]]) > 0]
    return S

def _cycle(g, f, v):
    seen, path, x = {}, [], v
    while x not in seen: seen[x] = len(path); path.append(x); x = f[x]
    return path[seen[x]:]

def _returns(f, o):
    x, seen = f[o], set()
    while x not in seen:
        if x == o: return True
        seen.add(x); x = f[x]
    return False

def prefix(g, pi, T):
    """pi (list of vertices, first to last before o) ⊕ T, T = value at o; requires pi to avoid T's path."""
    c, P, l = T
    return (c, P | frozenset(u for u in pi if g.rel(u, c)), l + len(pi))

# ---------------------------------------------------------------- N5 runs
def n5_own(g, o, sigma, tau, rng, cap=400):
    states = [(list(sigma), list(tau))]; fbs = []
    while len(states) <= cap:
        sg, tu = states[-1]
        S = analyse(g, o, sg, tu)
        if not S.Is and not S.It: break
        f = S.f
        ns, nt = list(sg), list(tu); fb = 0
        if S.Is:
            arena = [sorted({sg[v]} | {z for x, z in S.Is if x == v}) if g.owner[v] == 0 else [f[v]] for v in range(g.n)]
            fo, _ = even_optimum(g, f, arena, rng, perturb=rng.randint(0, 6))
            for v in range(g.n):
                if g.owner[v] == 0: ns[v] = fo[v]
        if S.It:
            mins, table = odd_points(g, f, o, [tu[o]] + S.It)
            vecs = {}
            for e in mins: vecs.setdefault(tuple(table[e]), []).append(e)
            assert len(vecs) == 1
            nt[o] = rng.choice(mins)
        if ns == sg and nt == tu:
            fb = 1
            if S.Is:
                for v in {v for v, _ in S.Is}:
                    ns[v] = max((z for x, z in S.Is if x == v), key=lambda z: (g.key(S.Xi[z]), z))
            else:
                nt[o] = min(S.It, key=lambda z: (g.key(S.U[z]), -z))   # best for Odd = smallest; ties larger index
        states.append((ns, nt)); fbs.append(fb)
    return states, fbs

def n5_spec(g, o, sigma, tau):
    """State sequence of SPEC N5 (experiments/new/n5.py functions, read-only)."""
    root = os.environ.get("R2_ROOT") or os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
    for p in ("experiments/new", "experiments/si", "experiments/harness"): sys.path.insert(0, os.path.join(root, p))
    import pg as lpg, n5
    from si import Engine
    lg = lpg.Game(list(g.prio), list(g.owner), [list(s) for s in g.succ])
    E, Ed = Engine(lg), Engine(n5.dual(lg)); n = g.n
    states, fbs = [(list(sigma), list(tau))], []
    while True:
        sg, tu = states[-1]
        vs, _ = E.evaluate(tuple(sg)); Is = E.improving(tuple(sg), vs)
        vt, _ = Ed.evaluate(tuple(tu)); It = Ed.improving(tuple(tu), vt)
        if not Is and not It: break
        ns, nt = list(sg), list(tu)
        if Is:
            opt = {v: {sg[v]} for v in range(n) if g.owner[v] == 0}
            for v, w in Is: opt[v].add(w)
            succ = [sorted(opt[v]) if g.owner[v] == 0 else [tu[v]] for v in range(n)]
            Er = Engine(n5.dual(lpg.Game(list(g.prio), list(g.owner), succ)))
            _, best = Er.evaluate(tuple(tu[v] if g.owner[v] == 1 else -1 for v in range(n)))
            for v in range(n):
                if g.owner[v] == 0: ns[v] = best[v]
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
        states.append((ns, nt)); fbs.append(fb)
    return states, fbs

# ---------------------------------------------------------------- checks
class Stats:
    def __init__(s): s.c = Counter(); s.mx = Counter(); s.viol = []; s.examples = {}
    def bad(s, msg):
        s.c["VIOLATIONS"] += 1
        if len(s.viol) < 30: s.viol.append(msg)
    def ex(s, k, msg):
        s.examples.setdefault(k, msg)

def check_run(g, o, states, fbs, st, name, spec=False):
    n = g.n; T = len(states) - 1
    A = [analyse(g, o, *states[k]) for k in range(T + 1)]
    st.c["runs"] += 1; st.c["transitions"] += T; st.c["fallbacks"] += sum(fbs)
    # sanity of my own definitions: R15 (a) Xi non-decreasing; Xi <= W <= U (R18 (d) Lemma S (b))
    for k in range(T + 1):
        S = A[k]
        for v in range(n):
            if g.cmp(S.Xi[v], S.W[v]) > 0 or g.cmp(S.W[v], S.U[v]) > 0: st.bad(f"{name} k={k} sandwich v={v}")
        if k < T:
            for v in range(n):
                if g.cmp(A[k + 1].Xi[v], S.Xi[v]) < 0: st.bad(f"{name} k={k} R15(a) v={v}")
            if spec and not fbs[k] and S.Is:   # spec step: sigma_{k+1} must be a pointwise arena optimum against tau_k
                arena = [sorted({states[k][0][v]} | {z for x, z in S.Is if x == v}) if g.owner[v] == 0 else [S.f[v]] for v in range(n)]
                _, opt = even_optimum(g, S.f, arena)
                f1 = [states[k + 1][0][v] if g.owner[v] == 0 else S.f[v] for v in range(n)]
                if vals_of(g, f1)[0] != opt: st.bad(f"{name} k={k} spec step not an arena optimum")
                st.c["spec_steps_checked"] += 1
    inphase = [A[k].lamX == A[k + 1].lamX and A[k].lamU == A[k + 1].lamU for k in range(T)]
    tauc = [states[k][1][o] == states[k + 1][1][o] for k in range(T)]
    for k in range(T + 1):
        S = A[k]
        st.c["states"] += 1
        # ---- Lemma G (a): no hypothesis
        for v in range(n):
            if v not in S.R:
                st.c["Ga_checks"] += 1
                if S.Xi[v] != S.W[v]: st.bad(f"{name} k={k} G(a) v={v}")
        if not S.h: continue
        st.c["h_states"] += 1
        # ---- Lemma G (b), (c)
        for v in S.R:
            st.c["Gb_checks"] += 1
            if set(S.pi[v]) & set(S.Xi_path[o]) or set(S.pi[v]) & set(S.W_path[o]): st.bad(f"{name} k={k} G(b) avoid v={v}")
            if S.Xi[v] != prefix(g, S.pi[v], S.theta) or S.W[v] != prefix(g, S.pi[v], S.w): st.bad(f"{name} k={k} G(b) v={v}")
        Rl = sorted(S.R)
        for y in Rl:
            for z in Rl:
                st.c["Gc_checks"] += 1
                if g.cmp(prefix(g, S.pi[y], S.theta), prefix(g, S.pi[z], S.theta)) != \
                   g.cmp(prefix(g, S.pi[y], S.w), prefix(g, S.pi[z], S.w)): st.bad(f"{name} k={k} G(c) {y},{z}")
    # ---- Lemma Wo
    for k in range(T):
        if tauc[k] and A[k].h and A[k + 1].h:
            st.c["Wo_checks"] += 1
            if g.cmp(A[k + 1].w, A[k].w) < 0: st.bad(f"{name} k={k} Wo")
        elif tauc[k] and not (A[k].h and A[k + 1].h) and g.cmp(A[k + 1].w, A[k].w) < 0:
            st.c["Wo_drop_nonh(control)"] += 1
    # ---- Lemma RM
    for k in range(T):
        if inphase[k] and tauc[k] and A[k].theta == A[k + 1].theta and A[k].h and A[k + 1].h:
            for x in A[k].R & A[k + 1].R:
                st.c["RM_checks"] += 1
                if g.cmp(prefix(g, A[k + 1].pi[x], A[k].theta), prefix(g, A[k].pi[x], A[k].theta)) < 0:
                    st.bad(f"{name} k={k} RM x={x}")
    # ---- RE steps 2-3 at EVERY leave L (phase at L -> L+1, tau constant, (h) at L); (NC) classified, not assumed
    for L in range(T):
        if not (inphase[L] and tauc[L] and A[L].h): continue
        S0, S1 = A[L], A[L + 1]
        sw = {v for v in range(n) if g.owner[v] == 0 and S0.f[v] != S1.f[v]}
        for x in S0.R - S1.R:
            st.c["leaves_checked"] += 1
            y = next(u for u in S0.pi[x] if u in sw)
            ci = y in _cycle(g, S1.fh, y)                 # (i) on the honest play
            ci_w = y in _cycle(g, S1.f, y)                # (i) on the W-play
            cii = len(S0.Xi[y][1]) == 0                   # (ii) empty path set above c
            cls = ("i" if ci else "-") + ("w" if ci_w else "-") + ("ii" if cii else "--")
            st.c["leave_class " + cls] += 1
            if ci and cii: st.c["NC_FAILS(honest)"] += 1; st.ex("NC_fail_honest", f"{name} L={L} x={x} y={y}")
            if ci_w and cii: st.c["NC_FAILS(W)"] += 1; st.ex("NC_fail_W", f"{name} L={L} x={x} y={y}")
            if g.cmp(S1.Xi[y], S0.Xi[y]) <= 0: st.bad(f"{name} L={L} RE step2 x={x} y={y} cls={cls}")
            if g.cmp(S1.Xi[x], S0.Xi[x]) <= 0: st.bad(f"{name} L={L} RE step3 x={x} y={y} cls={cls}")
            # z's L-path through y (the case the packet's caveat sends to (i))
            z = S1.f[y]
            if y in S0.Xi_path[z][:-1] or (z == y):
                st.c["z_Lpath_through_y"] += 1
                if not ci: st.c["z_Lpath_through_y_and_not(i)"] += 1; st.ex("caveat_gap", f"{name} L={L} x={x} y={y} z={z}")
        # my strengthened form: every switched y in R_L gains strictly (in phase, (h) at L)
        for y in sw & S0.R:
            st.c["switched_in_R_checks"] += 1
            if g.cmp(S1.Xi[y], S0.Xi[y]) <= 0: st.bad(f"{name} L={L} switched y={y} in R_L no strict gain")
    # negative control: leaves at non-(h) or out-of-phase transitions without strict gain
    for L in range(T):
        if not tauc[L]: continue
        if A[L].h and inphase[L]: continue
        for x in A[L].R - A[L + 1].R:
            st.c["leaves_control"] += 1
            if g.cmp(A[L + 1].Xi[x], A[L].Xi[x]) <= 0:
                st.c["leaves_control_no_gain"] += 1
                st.c[f"leaves_control_no_gain h={A[L].h} inphase={inphase[L]}"] += 1
                st.ex("control_no_gain", f"{name} L={L} x={x} h={A[L].h} inphase={inphase[L]}")
    # ---- Lemma RE proper (re-entries)
    for x in range(n):
        k = 0
        while k < T:
            if x in A[k].R and x not in A[k + 1].R:
                L = k; E1 = L + 1
                while E1 <= T and x not in A[E1].R: E1 += 1
                if E1 > T: break
                ok = all(inphase[j] and tauc[j] for j in range(L, E1)) and A[L].h and A[E1].h
                if ok:
                    st.c["RE_reentries"] += 1
                    if A[E1].theta == A[L].theta:
                        st.c["RE_theta_equal"] += 1
                        if g.cmp(prefix(g, A[E1].pi[x], A[L].theta), prefix(g, A[L].pi[x], A[L].theta)) <= 0:
                            st.bad(f"{name} RE x={x} L={L} E+1={E1}")
                    else:
                        st.c["RE_theta_changed"] += 1
                        if g.cmp(prefix(g, A[E1].pi[x], A[L].theta), prefix(g, A[L].pi[x], A[L].theta)) <= 0:
                            st.c["RE_theta_changed_route_not_better"] += 1
                            st.ex("theta_re", f"{name} RE x={x} L={L} E+1={E1}")
                k = E1
            else:
                k += 1
    # ---- Lemma PIECE: maximal stretches
    def good(k):   # transition k -> k+1 allowed inside a piece
        return (inphase[k] and tauc[k] and A[k].theta == A[k + 1].theta and A[k].w == A[k + 1].w and A[k].h and A[k + 1].h
                and not fbs[k] and A[k].R == A[k + 1].R)
    k = 0
    while k < T:
        if not good(k): k += 1; continue
        k0 = k
        while k < T and good(k): k += 1
        k1 = k                                       # transitions k0..k1-1
        R = A[k0].R; F = set(range(n)) - R
        vcR = vcF = vc = 0
        for j in range(k0, k1):
            chR = any(A[j].Xi[v] != A[j + 1].Xi[v] or A[j].W[v] != A[j + 1].W[v] for v in R)
            chF = any(A[j].Xi[v] != A[j + 1].Xi[v] or A[j].W[v] != A[j + 1].W[v] for v in F)
            vcR += chR; vcF += chF; vc += chR or chF
            piece_step(g, o, A[j], A[j + 1], states[j], states[j + 1], R, F, st, f"{name} j={j}")
        st.c["PIECE_stretches"] += 1; st.mx["PIECE_max_vc"] = max(st.mx["PIECE_max_vc"], vc)
        st.mx["PIECE_max_len"] = max(st.mx["PIECE_max_len"], k1 - k0)
        if vc > (len(R) - 1) + (len(F) - 1): st.bad(f"{name} PIECE count {vc} > {len(R)-1}+{len(F)-1} at {k0}..{k1}")
        if vcR > max(len(R) - 1, 0): st.bad(f"{name} PIECE R-count {vcR} > |R|-1 at {k0}..{k1}")
        if vcF > max(len(F) - 1, 0): st.bad(f"{name} PIECE F-count {vcF} > |F|-1 at {k0}..{k1}")
        st.mx["PIECE_max_(vc-bound+100)"] = max(st.mx["PIECE_max_(vc-bound+100)"], vc - (len(R) + len(F) - 2) + 100)
        if vcR == len(R) - 1 and vcR > 0: st.c["PIECE_R_tight"] += 1
        if vcF == len(F) - 1 and vcF > 0: st.c["PIECE_F_tight"] += 1

def piece_step(g, o, S0, S1, s0, s1, R, F, st, name):
    """PIECE step 3 (gate identity) and step 4 (each restriction is the optimum of its piece's arena)."""
    n = g.n; sg = s0[0]
    Is = set(S0.Is)
    for x in range(n):
        if g.owner[x] != 0: continue
        for z in g.succ[x]:
            if z == sg[x]: continue
            if x in R and z in R:
                st.c["PIECE_gateR"] += 1
                if ((x, z) in Is) != (g.cmp(S0.W[z], S0.W[sg[x]]) > 0): st.bad(f"{name} PIECE gate R ({x},{z})")
            if x in F and z in F:
                st.c["PIECE_gateF"] += 1
                if ((x, z) in Is) != (g.cmp(S0.W[z], S0.W[sg[x]]) > 0): st.bad(f"{name} PIECE gate F ({x},{z})")
    # piece arenas: x keeps sigma(x) and gate edges inside its own piece; the other piece is frozen at state k's map
    f = S0.f
    for part in (R, F):
        arena = [sorted({f[v]} | {z for xx, z in S0.Is if xx == v and z in part}) if (g.owner[v] == 0 and v in part)
                 else [f[v]] for v in range(n)]
        # R's piece: o keeps tau(o) and F is frozen at state k (w is constant over the step); F's piece: R frozen (F is closed)
        _, opt = even_optimum(g, f, arena)
        st.c["PIECE_opt_checks"] += 1
        for v in part:
            if S1.W[v] != opt[v]: st.bad(f"{name} PIECE step4 {'R' if part is R else 'F'} v={v}"); break

# ---------------------------------------------------------------- games
def rand_game(rng, n, cyc=True):
    while True:
        owner = [0] * n; o = rng.randrange(n); owner[o] = 1
        for v in range(n):
            if v != o and rng.random() < 0.25: owner[v] = 1
        prio = [rng.randrange(0, n + 1) for _ in range(n)]
        succ = []
        for v in range(n):
            if owner[v] == 1 and v != o: k = 1
            elif v == o: k = rng.randint(2, 3)
            else: k = rng.randint(1, 3)
            succ.append(rng.sample(range(n), k))
        g = Game(prio, owner, succ)
        if len(g.succ[o]) < 2: continue
        # o-cyclic: o reachable from one of its exits (the case box 26 is about; o-acyclic is R18)
        reach, stck = set(), list(g.succ[o])
        while stck:
            x = stck.pop()
            if x in reach: continue
            reach.add(x); stck.extend(g.succ[x])
        if cyc and o not in reach: continue
        return g, o

def rand_start(rng, g):
    return [rng.choice(g.succ[v]) for v in range(g.n)], [rng.choice(g.succ[v]) for v in range(g.n)]

def main():
    st = Stats()
    if sys.argv[1] == "random":
        N, nmin, nmax, seed = map(int, sys.argv[2:6]); mode = sys.argv[6] if len(sys.argv) > 6 else "own"
        rng = random.Random(seed)
        for i in range(N):
            g, o = rand_game(rng, rng.randint(nmin, nmax))
            s, t = rand_start(rng, g)
            if mode == "spec": states, fbs = n5_spec(g, o, s, t)
            else: states, fbs = n5_own(g, o, s, t, rng)
            check_run(g, o, states, fbs, st, f"seed{seed}#{i}", spec=(mode == "spec"))
    else:
        path = sys.argv[2]
        g = parse(open(path).read())
        o = [v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) > 1]
        assert len(o) == 1, "not C^1O"; o = o[0]
        rest = sys.argv[3:]
        mode = "own"; start = None; runs = 20
        for a in rest:
            if a in ("own", "spec"): mode = a
            elif a.isdigit(): runs = int(a)
            else: start = a
        rng = random.Random(1)
        for r in range(1 if mode == "spec" else runs):
            if start:
                s0, t0 = read_start(start)
                s = [s0.get(v, g.succ[v][0]) for v in range(g.n)]; t = [t0.get(v, g.succ[v][0]) for v in range(g.n)]
            elif r == 0:   # SPEC S3 best-reward start
                def br(v, dual):
                    def rr(w):
                        p = g.prio[w] + (1 if dual else 0)
                        r_ = p if p % 2 == 0 else -p
                        return (r_, w if r_ % 2 == 0 else -w)
                    return max(g.succ[v], key=rr)
                s = [br(v, False) for v in range(g.n)]; t = [br(v, True) for v in range(g.n)]
            else:
                s, t = rand_start(rng, g)
            if mode == "spec": states, fbs = n5_spec(g, o, s, t)
            else: states, fbs = n5_own(g, o, s, t, rng)
            check_run(g, o, states, fbs, st, f"{os.path.basename(path)}#{r}", spec=(mode == "spec"))
    for k in sorted(st.c): print(f"{k}: {st.c[k]}")
    for k in sorted(st.mx): print(f"{k}: {st.mx[k]}")
    for k, v in st.examples.items(): print(f"example {k}: {v}")
    for v in st.viol: print("VIOLATION", v)
    print("RESULT", "FAIL" if st.c["VIOLATIONS"] else "OK", f"violations={st.c['VIOLATIONS']}")

if __name__ == "__main__":
    main()
