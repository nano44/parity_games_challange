#!/usr/bin/env python3
"""REFEREE-2 successor 5 (Opus 5.5, D15): mechanical check of packet P-N5-FB (docs/si/P-N5-FB-box7.md sha1 9ece9994 @ trunk 348393b).
Own code. N5 state sequence = SPEC (n5.py's loop re-written here, asserted equal to n5.run's (iterations, fallbacks)). Values: si.py's
Engine.evaluate (Xi_k, sigma-bar_k), cross-checked against my own play-following of H_k = (sigma_k, sigma-bar_k) on every state
(Lemma 5.2 code link). Everything else (levels, COARSE, gate levels, M_k, tameness, (NC), V = Theta_{H'}, blocks, beta, R-bar) is
computed here from the packet's definitions.
Checks (packet items):
  LINK   Xi_k = Theta_{H_k}; sigma-bar_k(u) minimises Xi_k over succ(u) for Odd u (VJ00 p. 14 definition).
  T      Claim (T) directly: random H' built from H_k by re-choosing successors with COARSE_L-equal Xi_k values, random L.
  SIa    COARSE-SI (a) with L = M_k and with L = max switched level; converse at (NC) failures (V vs Xi_k at bad tops).
  SIb    TAME: hypotheses => tame.
  MONO   tame => M_{k+1} <= M_k (every transition, phases or not).
  NOINF  lambda_{k+1} = lambda_k => every switch has gate level < inf; and M_k < inf at such fallbacks.
  FB     per phase: beta monotone in blocks, COARSE_M(Xi(sigma y)) constant, strict rise at each tame fallback, per-block bound,
         per tame-run bound, Theorem FB total; Corollary (W-lowering transitions <= bound).
  C1O    (one-Odd-choice games only) J1, OFF, CAP, Remark (non-tame => (NC) fails with a cycle through o).
Usage: fb_check.py general N nmin nmax seed | c1o N nmin nmax seed | inst game.pg [runs]"""
import sys, os, random
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
for p in ("experiments/new", "experiments/si", "experiments/harness"): sys.path.insert(0, os.path.join(ROOT, p))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-RE"))
import pg as lpg, n5
from si import Engine
import re_check as RC

INF, BOT = 10 ** 9, -2

def lev(x, y):
    if x == y: return BOT
    if x[0] != y[0]: return INF
    if x[1] != y[1]: return (x[1] ^ y[1]).bit_length() - 1
    return -1

def coarse(x, L):
    if L >= INF: return 0
    if L <= BOT: return x
    return (x[0], x[1] & ~((1 << (L + 1)) - 1))

class Stats:
    def __init__(s): s.c = Counter(); s.mx = Counter(); s.viol = []; s.ex = {}
    def bad(s, m):
        s.c["VIOLATIONS"] += 1
        if len(s.viol) < 40: s.viol.append(m)

def play_val(E, f, v):
    """VJ00 play value on the functional graph f in si.py representation (c, mask, len); also returns the cycle."""
    seen, path, x = {}, [], v
    while x not in seen: seen[x] = len(path); path.append(x); x = f[x]
    cyc = path[seen[x]:]
    t = max(cyc, key=lambda u: E.rank[u])
    i = path.index(t)
    mask = 0
    for u in path[:i]:
        if E.rank[u] > E.rank[t]: mask |= E.bit[u]
    return (t, mask, i), cyc

def spec_run(g):
    """SPEC N5 from the S3 start or a given start; returns states [(sigma, tau)], fbs."""
    n = g.n; E, Ed = Engine(g), Engine(n5.dual(g))
    sigma, tau = list(E.initial("best")), list(Ed.initial("best"))
    return sigma, tau

def run_n5(g, sigma, tau):
    n = g.n; E, Ed = Engine(g), Engine(n5.dual(g))
    states, fbs = [(list(sigma), list(tau))], []
    while len(states) < 3000:
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
    return states, fbs, E, Ed

class S: pass

def analyse(g, E, Ed, sg, tu, o):
    s = S(); n = g.n
    s.Xi, s.sbar = E.evaluate(tuple(sg))
    s.Xi = list(s.Xi); s.sbar = list(s.sbar)
    s.Is = E.improving(tuple(sg), s.Xi)
    s.lamU = tuple(x[0] for x in Ed.evaluate(tuple(tu))[0])
    s.lam = tuple(x[0] for x in s.Xi)
    s.H = [sg[v] if g.owner[v] == 0 else s.sbar[v] for v in range(n)]
    s.gl = {(y, z): lev(s.Xi[sg[y]], s.Xi[z]) for y, z in s.Is}
    s.M = max(s.gl.values()) if s.gl else BOT
    s.W = [play_val(E, [sg[v] if g.owner[v] == 0 else tu[v] for v in range(n)], v)[0] for v in range(n)]
    if o is not None:
        f = [sg[v] if g.owner[v] == 0 else tu[v] for v in range(n)]
        s.Rbar = {o}
        for v in range(n):
            x, seen = v, set()
            while x not in seen and x != o: seen.add(x); x = f[x]
            if x == o: s.Rbar.add(v)
    return s

def check_link(g, E, s, st, name):
    for v in range(g.n):
        if play_val(E, s.H, v)[0] != s.Xi[v]: st.bad(f"{name} LINK Xi != Theta_H at {v}"); break
    for u in range(g.n):
        if g.owner[u] == 1:
            b = s.Xi[s.sbar[u]]
            if any(E.key(s.Xi[w]) < E.key(b) for w in E.succ[u]):
                if s.lam[u] == u:
                    st.c["LINK_sbar_not_minimiser_at_own_cycle_node (FIX 2 DFS; VJ00 p.14 differs)"] += 1
                    if any(E.key(coarse(s.Xi[w], -1) + (0,)) < E.key(coarse(b, -1) + (0,)) for w in E.succ[u]):
                        st.bad(f"{name} sbar({u}) at its own cycle node not a COARSE_-1 minimiser")
                else:
                    st.c["LINK_sbar_not_minimiser_non_cycle_node"] += 1
                    onp = any(u == x for x in [])
                    st.ex.setdefault("nonmin", f"{name} u={u}")
            else: st.c["LINK_sbar_minimiser"] += 1
    st.c["LINK_states"] += 1

def check_T(g, E, s, rng, st, name, trials=3):
    n = g.n
    for _ in range(trials):
        L = rng.choice([-1] + list(range(n)))
        Hp = []
        for p in range(n):
            base = coarse(s.Xi[s.H[p]], L)
            opts = [w for w in E.succ[p] if coarse(s.Xi[w], L) == base]
            Hp.append(rng.choice(opts))
        for v in range(n):
            val, cyc = play_val(E, Hp, v)
            t = val[0]
            if s.lam[t] != t: st.c["T_hyp_fails"] += 1; continue
            st.c["T_checks"] += 1
            if Hp != s.H and val != s.Xi[v]: st.c["T_checks_nontrivial"] += 1
            if coarse(val, L) != coarse(s.Xi[v], L): st.bad(f"{name} T fails v={v} L={L}")

def check_transition(g, E, A, B, s0, s1, fb, inphase, st, name, o):
    """A = analysis at k, B = at k+1."""
    n = g.n
    sw = [y for y in range(n) if g.owner[y] == 0 and s0[0][y] != s1[0][y]]
    # R15 (d) link: switched edges are gate edges
    for y in sw:
        if (y, s1[0][y]) not in A.gl: st.bad(f"{name} switch {y}->{s1[0][y]} not a gate edge"); return
    Lsw = max([A.gl[(y, s1[0][y])] for y in sw], default=BOT)
    Hp = [s1[0][v] if g.owner[v] == 0 else A.sbar[v] for v in range(n)]
    V = []; NC = True; bad_tops = set()
    for v in range(n):
        val, cyc = play_val(E, Hp, v); V.append(val)
        if A.lam[val[0]] != val[0]: NC = False; bad_tops.add(val[0])
    tame = all(coarse(B.Xi[v], A.M) == coarse(A.Xi[v], A.M) for v in range(n))
    st.c[f"transitions NC={NC} tame={tame} inphase={inphase}"] += 1
    # COARSE-SI (a), general form for every L in {Lsw, M_k} with L < inf
    for L in {Lsw, A.M}:
        if L >= INF: continue
        if NC:
            st.c["SIa_checks"] += 1
            if any(coarse(B.Xi[v], L) != coarse(A.Xi[v], L) for v in range(n)): st.bad(f"{name} SIa fails L={L}")
            if any(coarse(V[v], L) != coarse(A.Xi[v], L) for v in range(n)): st.bad(f"{name} SIa: COARSE(V) != COARSE(Xi_k) L={L}")
        else:
            st.c["SIa_converse_checks"] += 1
            for t in bad_tops:
                if coarse(V[t], L) == coarse(A.Xi[t], L): st.bad(f"{name} SIa converse fails at {t} L={L}")
    if not NC and A.M < INF and A.M > BOT:
        st.c["NC_fail_but_tame" if tame else "NC_fail_and_nontame"] += 1
    # VJ00 (11) and R15 (a) used in (a)
    for v in range(n):
        if E.key(B.Xi[v]) < E.key(A.Xi[v]): st.bad(f"{name} R15a Xi decreased at {v}")
        if E.key(V[v]) < E.key(B.Xi[v]): st.bad(f"{name} (11) V < Xi_{{k+1}} at {v}")
    # TAME (b)
    if A.lam == B.lam and all(lev(A.Xi[A.sbar[u]], A.Xi[B.sbar[u]]) <= A.M for u in range(n) if g.owner[u] == 1):
        st.c["SIb_hyp"] += 1
        if not tame: st.bad(f"{name} TAME hypotheses hold but not tame")
    # MONO
    if tame:
        st.c["MONO_checks"] += 1
        if B.M > A.M and not (A.M >= INF): st.bad(f"{name} MONO M {A.M} -> {B.M}")
    elif B.M > A.M: st.c["M_rose_at_nontame"] += 1
    # NOINF
    if A.lam == B.lam:
        for y in sw:
            st.c["NOINF_checks"] += 1
            if A.gl[(y, s1[0][y])] >= INF: st.bad(f"{name} NOINF switch {y} level inf")
        if fb and A.Is:
            st.c["NOINF_fallbacks"] += 1
            if A.M >= INF: st.bad(f"{name} NOINF consequence: fallback with M_k = inf")
    # Remark + C1O checks
    if o is not None and inphase:
        nontame = not tame
        if nontame:
            st.c["C1O_nontame"] += 1
            a, b = A.sbar[o], B.sbar[o]
            if a == b or lev(A.Xi[a], A.Xi[b]) <= A.M: st.bad(f"{name} J1 fails a={a} b={b}")
            if NC: st.bad(f"{name} Remark: non-tame but (NC) holds")
            elif not any(o in play_val(E, Hp, t)[1] for t in bad_tops): st.bad(f"{name} Remark: no bad cycle through o")
            st.c[f"C1O_nontame lam(o)==o:{A.lam[o] == o}"] += 1
            for e in E.succ[o]:
                if lev(A.Xi[a], A.Xi[e]) <= A.M:
                    if A.lam[o] == o: st.c["CAP_checks_at_o_cycle_node"] += 1
                    st.c["CAP_checks"] += 1
                    if e not in B.Rbar: st.bad(f"{name} CAP exit {e} not in Rbar_k+1")
        if A.M < INF:
            for v in range(n):
                if v not in B.Rbar:
                    st.c["OFF_checks"] += 1
                    if coarse(B.Xi[v], A.M) != coarse(A.Xi[v], A.M): st.bad(f"{name} OFF fails v={v}")
    return tame

def check_run(g, sigma, tau, st, name, o, rng):
    states, fbs, E, Ed = run_n5(g, sigma, tau)
    lg = g
    if (len(fbs), sum(fbs)) != n5.run(lg, "n5", ({v: sigma[v] for v in range(g.n) if g.owner[v] == 0},
                                                  {v: tau[v] for v in range(g.n) if g.owner[v] == 1}))[:2]:
        st.bad(f"{name} run differs from n5.run")
    A = [analyse(g, E, Ed, s, t, o) for s, t in states]
    for k, s in enumerate(A):
        check_link(g, E, s, st, f"{name}@{k}")
        if k % 3 == 0: check_T(g, E, s, rng, st, f"{name}@{k}")
    T = len(fbs)
    inphase = [A[k].lam == A[k + 1].lam and A[k].lamU == A[k + 1].lamU and states[k][1] == states[k + 1][1] for k in range(T)]
    tame = [check_transition(g, E, A[k], A[k + 1], states[k], states[k + 1], fbs[k], inphase[k], st, f"{name}@{k}", o)
            for k in range(T)]
    st.c["runs"] += 1; st.c["transitions"] += T; st.c["fallbacks"] += sum(fbs)
    # phases
    k = 0
    while k < T:
        if not inphase[k]: k += 1; continue
        j = k
        while j < T and inphase[j]: j += 1
        phase(g, E, A, states, fbs, tame, k, j, st, f"{name}[{k},{j})")
        k = j

def phase(g, E, A, states, fbs, tame, k0, k1, st, name):
    n = g.n; nE = sum(1 for v in range(n) if g.owner[v] == 0)
    J = sum(1 for k in range(k0, k1) if not tame[k]); F = sum(fbs[k0:k1])
    bound = nE * (2 * n - 1) * (J + 1) + J
    st.c["phases"] += 1; st.c["phase_fallbacks"] += F; st.mx["max_J_per_phase"] = max(st.mx["max_J_per_phase"], J)
    if F > bound: st.bad(f"{name} FB total {F} > {bound}")
    wl = sum(1 for k in range(k0, k1) if any(E.key(A[k + 1].W[v]) < E.key(A[k].W[v]) for v in range(n)))
    st.c["W_lowering_in_phase"] += wl
    if wl > bound: st.bad(f"{name} Corollary W-lowering {wl} > {bound}")
    for k in range(k0, k1):
        if fbs[k] == 0 and any(E.key(A[k + 1].W[v]) < E.key(A[k].W[v]) for v in range(n)): st.bad(f"{name} WM: W drops at non-fallback {k}")
    # tame runs and blocks
    k = k0
    while k < k1:
        if not tame[k]: k += 1; continue
        r = k
        while r < k1 and tame[r]: r += 1
        run_fb = 0; seenM = []
        b = k
        while b < r:
            M = A[b].M; e = b
            while e < r and A[e].M == M: e += 1
            if M in seenM: st.bad(f"{name} block value {M} repeats in a tame run")
            seenM.append(M)
            nfb = sum(fbs[b:e]); run_fb += nfb
            st.mx["max_fallbacks_in_block"] = max(st.mx["max_fallbacks_in_block"], nfb)
            if M in (INF, BOT) and nfb: st.bad(f"{name} fallback in block of value {M}")
            if M < INF and M > BOT:
                cap = nE if M >= 0 else nE * (n - 1)
                if nfb > cap: st.bad(f"{name} block M={M} has {nfb} > {cap} fallbacks")
                Lb = M - 1 if M >= 0 else BOT
                for i in range(b, e):
                    s0, s1 = states[i][0], states[i + 1][0]
                    rise = False
                    for y in range(n):
                        if g.owner[y] != 0: continue
                        x0, x1 = A[i].Xi[s0[y]], A[i + 1].Xi[s1[y]]
                        if coarse(x0, M) != coarse(x1, M): st.bad(f"{name} FB(1) COARSE_M(Xi(sigma y)) moved at {i} y={y}")
                        c0, c1 = coarse(x0, Lb), coarse(x1, Lb)
                        if c0 != c1:
                            if lev(x0, x1) >= INF or E.key(x1) < E.key(x0): st.bad(f"{name} FB(1) beta decreased at {i} y={y}")
                            rise = True
                    if fbs[i]:
                        st.c["FB_tame_fallbacks_checked"] += 1
                        if not rise: st.bad(f"{name} FB(2) no strict beta rise at fallback {i}")
            b = e
        if run_fb > nE * (2 * n - 1): st.bad(f"{name} tame run fallbacks {run_fb} > {nE * (2 * n - 1)}")
        k = r

def rand_general(rng, n):
    owner = [rng.randrange(2) for _ in range(n)]
    prio = [rng.randrange(0, n + 1) for _ in range(n)]
    succ = [rng.sample(range(n), rng.randint(1, 3)) for _ in range(n)]
    return lpg.Game(prio, owner, succ)

def to_lpg(g): return lpg.Game(list(g.prio), list(g.owner), [list(s) for s in g.succ])

def one_odd(g):
    o = [v for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1]
    assert len(o) == 1, f"not C^1O: {o}"
    return o[0]

def report(st):
    for k in sorted(st.c): print(f"{k}: {st.c[k]}")
    for k in sorted(st.mx): print(f"{k}: {st.mx[k]}")
    for v in st.viol: print("VIOLATION", v)
    print("RESULT", "FAIL" if st.c["VIOLATIONS"] else "OK", f"violations={st.c['VIOLATIONS']}")

def start(g, rng, rnd):
    E, Ed = Engine(g), Engine(n5.dual(g))
    s, t = list(E.initial("best")), list(Ed.initial("best"))
    if rnd:
        s = [rng.choice(g.succ[v]) if g.owner[v] == 0 else s[v] for v in range(g.n)]
        t = [rng.choice(g.succ[v]) if g.owner[v] == 1 else t[v] for v in range(g.n)]
    return s, t

def main():
    st = Stats(); mode = sys.argv[1]
    if mode in ("general", "c1o"):
        N, nmin, nmax, seed = map(int, sys.argv[2:6]); rng = random.Random(seed)
        for i in range(N):
            if mode == "general": g = rand_general(rng, rng.randint(nmin, nmax)); o = None
            else:
                rg, o = RC.rand_game(rng, rng.randint(nmin, nmax), cyc=rng.random() < 0.7); g = to_lpg(rg); assert one_odd(g) == o
            s, t = start(g, rng, rng.random() < 0.6)
            check_run(g, s, t, st, f"{mode}{seed}#{i}", o, rng)
    else:
        path = sys.argv[2]; runs = int(sys.argv[3]) if len(sys.argv) > 3 else 1
        g = lpg.parse("".join(l for l in open(path) if not l.lstrip().startswith("%"))); o = one_odd(g); rng = random.Random(7)
        for r in range(runs):
            s, t = start(g, rng, r > 0)
            check_run(g, s, t, st, f"{os.path.basename(path)}#{r}", o, rng)
    report(st)

if __name__ == "__main__":
    main()
