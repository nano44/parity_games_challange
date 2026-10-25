#!/usr/bin/env python3
"""REFEREE-2 successor 5 (Opus 5.5, D15): mechanical check of packet P-N5-U23 (docs/new/P-N5-U23-box31.md sha1 ee3e5d1e @ trunk 7666336).
Own code on my lane's R2-N5-RE/re_check.py definitions (play values, Xi, W, R, routes) and my R2-N5-U1 SPEC runner (n5.py's loop,
cross-checked against re_check.n5_spec). Every game asserts exactly one Odd vertex with out-degree > 1.
Per stretch (phase = lambda_Xi, lambda_U, tau constant; stretch = maximal run with R, theta, w constant; transitions with both ends in it):
  class  U2: not H1, c_theta != o, W frame in route form (H2 or c_w = o).  U3: not H2, c_w != o, honest frame in route form.
         U23: not H1, not H2, c_theta != o, c_w != o.
  U2     W(v) = pi_v (+) w on R; Xi(v) = (prefix of pi_v to the first of {c_theta, o}) (+) const; CASC-U2 (switch steps <= level - 2);
         Corollary bound.
  U3/23  C_W decomposition (A1, A2), kinds, W formulas per kind, Xi formula; events; event-free sub-runs; (i), (ii) literally (L_B =
         max |pi| over kind B, empty max = 0) and in the corrected form (T = max(L_B - 1, 0)); (iii); Corollary bound.
Usage: u23_check.py random N nmin nmax seed | inst game.pg [runs]"""
import sys, os, random
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-U1"))
import u1_check as U
RC = U.RC

def ext_path(g, path, T):      # path (list, first..last) (+) T
    return RC.prefix(g, path, T)

def check_run(g, o, states, fbs, st, name):
    A = [RC.analyse(g, o, s, t) for s, t in states]
    for S in A: S.H1, S.H2 = U.H12(g, o, S)
    T = len(fbs)
    inphase = [A[k].lamX == A[k + 1].lamX and A[k].lamU == A[k + 1].lamU and states[k][1] == states[k + 1][1] for k in range(T)]
    k = 0
    while k <= T:
        j = k
        while j < T and inphase[j] and A[j].R == A[j + 1].R and A[j].theta == A[j + 1].theta and A[j].w == A[j + 1].w: j += 1
        stretch(g, o, A, states, fbs, k, j, st, name)
        k = j + 1

def cls(S, o):
    ct, cw = S.theta[0], S.w[0]
    if not S.H1 and ct != o and not S.H2 and cw != o: return "U23"
    if not S.H1 and ct != o and (S.H2 or cw == o): return "U2"
    if not S.H2 and cw != o and (S.H1 or ct == o): return "U3"
    return None

def stretch(g, o, A, states, fbs, p0, p1, st, name):
    c = cls(A[p0], o)
    if c is None: return
    for k in range(p0, p1 + 1):
        if cls(A[k], o) != c: st.bad(f"{name} class not constant on stretch [{p0},{p1}]"); return
    R = A[p0].R; r = len(R); ct, cw = A[p0].theta[0], A[p0].w[0]
    st.c[f"stretch_{c}"] += 1
    if p1 > p0: st.c[f"stretch_{c}_nontrivial"] += 1
    Ev = [v for v in R if g.owner[v] == 0 and v != o]
    # ---- value formulas
    for k in range(p0, p1 + 1):
        S = A[k]
        for v in R:
            if v == o: continue
            pi = S.pi[v]
            # honest: prefix of pi to first of {c_theta, o}
            if c in ("U2", "U23") or (c == "U3" and not S.H1):
                if ct in pi: pre = pi[:pi.index(ct)]; Tm = (ct, frozenset(), 0)
                else: pre = pi; Tm = S.theta
            else: pre, Tm = pi, S.theta
            if S.Xi[v] != ext_path(g, pre, Tm): st.bad(f"{name} {c} Xi formula k={k} v={v}"); break
            if c == "U2":
                if S.W[v] != ext_path(g, pi, S.w): st.bad(f"{name} U2 W formula k={k} v={v}"); break
            else:
                if cw in pi:   # kind A: W(v) = (path to c_w) (+) (c_w, {}, 0)
                    if S.W[v] != ext_path(g, pi[:pi.index(cw)], (cw, frozenset(), 0)): st.bad(f"{name} {c} W kind-A k={k} v={v}"); break
                else:
                    if S.W[v] != ext_path(g, pi, S.w): st.bad(f"{name} {c} W kind-B k={k} v={v}"); break
        if c != "U2":
            cwv, P, d = S.w
            if P or cwv not in R: st.bad(f"{name} {c} w shape {S.w}")
    st.c[f"formula_states_{c}"] += p1 - p0 + 1
    # ---- counting per stretch
    f = sum(fbs[p0:p1]); KW = 0; E = 0; Rch = 0
    kind = lambda S, v: "A" if cw in S.pi[v] else "B"
    for k in range(p0, p1):
        S0, S1 = A[k], A[k + 1]
        if any(S0.Xi[v] != S1.Xi[v] or S0.W[v] != S1.W[v] or states[k][0][v] != states[k + 1][0][v] for v in R): Rch += 1
        if not fbs[k] and any(S0.W[v] != S1.W[v] for v in R): KW += 1
        if c != "U2" and not fbs[k] and all(S0.W[v] == S1.W[v] for v in R):
            if any(states[k][0][v] != states[k + 1][0][v] and (v == cw or kind(S0, v) != kind(S1, v)) for v in Ev): E += 1
    if c == "U2": bound = f + KW + (KW + f + 1) * (r - 2)
    else: bound = f + KW + E + (KW + f + E + 1) * (2 * r - 4)
    if Rch > bound: st.bad(f"{name} {c} corollary Rch={Rch} > {bound}")
    st.mx[f"max_Rch_{c}"] = max(st.mx[f"max_Rch_{c}"], Rch); st.c[f"events_{c}"] += E; st.c[f"KW_{c}"] += KW
    # ---- W-flat runs
    t = p0
    while t < p1:
        if fbs[t] or any(A[t].W[v] != A[t + 1].W[v] for v in R): t += 1; continue
        u = t
        while u < p1 and not fbs[u] and all(A[u].W[v] == A[u + 1].W[v] for v in R): u += 1
        st.c[f"wflat_runs_{c}"] += 1
        if c == "U2": u2_run(g, o, A, states, R, Ev, t, u, st, name)
        else: u3_run(g, o, A, states, R, Ev, cw, t, u, st, name, c)
        t = u

def u2_run(g, o, A, states, R, Ev, t, u, st, name):
    for x in range(t, u):
        for v in Ev:
            if states[x][0][v] != states[x + 1][0][v]:
                l = len(A[x].pi[v]); s = x - t; st.c["U2_wflat_switches"] += 1
                st.mx["U2_max(step-level+2)"] = max(st.mx.get("U2_max(step-level+2)", -99), s - l + 2)
                if s > l - 2: st.bad(f"{name} CASC-U2 run[{t},{u}) step {s} v={v} level {l}")

def u3_run(g, o, A, states, R, Ev, cw, t, u, st, name, c):
    kind = lambda S, v: "A" if cw in S.pi[v] else "B"
    # split at events
    sub = []; s0 = t
    for x in range(t, u):
        ev = any(states[x][0][v] != states[x + 1][0][v] and (v == cw or kind(A[x], v) != kind(A[x + 1], v)) for v in Ev)
        if ev:
            st.c[f"U3_event_transitions_{c}"] += 1
            if s0 < x: sub.append((s0, x))
            s0 = x + 1
    if s0 < u: sub.append((s0, u))
    r = len(R)
    for a, b in sub:
        st.c[f"U3_subruns_{c}"] += 1
        S = A[a]
        kinds = {v: kind(S, v) for v in R if v != o}
        for x in range(a, b + 1):
            if any(kind(A[x], v) != kinds[v] for v in kinds): st.bad(f"{name} kinds not constant on event-free sub-run"); break
        LBs = [len(S.pi[v]) for v in kinds if kinds[v] == "B"]
        LB = max(LBs) if LBs else 0
        if not LBs: st.c[f"U3_subruns_kindB_empty_{c}"] += 1
        Tc = max(LB - 1, 0)
        for x in range(a, b):
            for v in Ev:
                if states[x][0][v] == states[x + 1][0][v]: continue
                s = x - a
                if kinds[v] == "B":
                    l = len(S.pi[v]); st.c[f"U3_switch_B_{c}"] += 1
                    st.mx["U3_B_max(step-|pi|+2)"] = max(st.mx.get("U3_B_max(step-|pi|+2)", -99), s - l + 2)
                    if s > l - 2: st.bad(f"{name} CASC-U3 (i) step {s} v={v} |pi| {l}")
                else:
                    lam = S.pi[v].index(cw)    # steps from v to c_w
                    st.c[f"U3_switch_A_{c}"] += 1
                    if s > LB + lam - 3:
                        st.c[f"U3_(ii)_literal_fails_{c}"] += 1
                        st.examples.setdefault("ii_literal", f"{name} sub[{a},{b}) step {s} v={v} lam {lam} L_B {LB} kindB_empty={not LBs}")
                    if not LBs: st.mx["U3_A_emptyB_max(step-(lam-3))"] = max(st.mx.get("U3_A_emptyB_max(step-(lam-3))", -99), s - (lam - 3))
                    if s > Tc + lam - 2: st.bad(f"{name} CASC-U3 (ii) corrected step {s} v={v} lam {lam} L_B {LB}")
                    st.mx["U3_A_max(step-(T+lam-2))"] = max(st.mx.get("U3_A_max(step-(T+lam-2))", -99), s - (Tc + lam - 2))
                if s >= 2 * r - 4: st.bad(f"{name} CASC-U3 (iii) step {s} |R| {r}")

def run_one(g, o, s, t, st, name, lemmaR=False):
    states, fbs, arenas = U.spec_run(g, o, s, t, st, name, lemmaR=lemmaR)
    check_run(g, o, states, fbs, st, name)
    st.c["runs"] += 1; st.c["transitions"] += len(fbs)
    return states, fbs

def main():
    st = RC.Stats(); st.mx = Counter()
    if sys.argv[1] == "random":
        N, nmin, nmax, seed = map(int, sys.argv[2:6]); rng = random.Random(seed)
        for i in range(N):
            g, o = RC.rand_game(rng, rng.randint(nmin, nmax)); U.one_odd(g)
            s, t = RC.rand_start(rng, g) if rng.random() < 0.5 else U.br_start(g)
            run_one(g, o, s, t, st, f"seed{seed}#{i}")
    else:
        path = sys.argv[2]; runs = int(sys.argv[3]) if len(sys.argv) > 3 else 1
        g = RC.parse(open(path).read()); o = U.one_odd(g); rng = random.Random(1)
        for r in range(runs):
            s, t = U.br_start(g) if r == 0 else RC.rand_start(rng, g)
            run_one(g, o, s, t, st, f"{os.path.basename(path)}#{r}")
    U.report(st)

if __name__ == "__main__":
    main()
