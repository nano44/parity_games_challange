#!/usr/bin/env python3
"""REFEREE-2 (Opus 5.5, D15) mechanical check of packet P-N5-X (docs/new/P-N5-X-box28.md @ trunk afc88b0).
Definitions and own N5 (random tie-breaks) from ../R2-N5-RE/re_check.py (REFEREE-2 code); "spec" mode takes n5.py's state sequence.
Phase = maximal run of states with lambda_Xi, lambda_U and tau constant across each transition. State types: EQ (Xi = W),
THR ((h) and Xi != W), OTHER (not (h) and Xi != W). Value-changing = Xi or W changes somewhere.
Checks: XW, XW1, Lemma EQ, FBL-N (i)-(iii), NF, F1, F2 (both claims), TF (my supplement: in an F-interval, a theta-change at a THR->THR
transition comes with a Xi-change on F), PIECE theta-free with flat fallbacks (sub-blocks of Theorem X step 4, split bounds),
Theorem X (value-changing count and transition count per phase), the (w,u*)-run rows used by FB-W (Lemma C, CR) and FB-W itself.
Usage: x_check.py random N nmin nmax seed [own|spec] | x_check.py inst game.pg [start] [own|spec] [runs]"""
import sys, os, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2-N5-RE"))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2-N5-XA"))
import re_check as rc
from xa_check import coarse, ccmp

def _cyc(f, v):
    seen, path, x = {}, [], v
    while x not in seen: seen[x] = len(path); path.append(x); x = f[x]
    return path[seen[x]:]

def check_run(g, o, states, fbs, st, name):
    n = g.n; T = len(states) - 1
    A = [rc.analyse(g, o, *s) for s in states]
    st.c["runs"] += 1; st.c["transitions"] += T
    H2 = [o not in _cyc(A[k].f, o) for k in range(T + 1)]
    typ = []
    for k in range(T + 1):
        S = A[k]
        for v in range(n):                                     # Lemma XW
            if g.cmp(S.Xi[v], S.W[v]) > 0: st.bad(f"{name} k={k} XW v={v}")
        eq = S.Xi == S.W
        if S.h and (eq != (S.theta == S.w)): st.bad(f"{name} k={k} XW1")
        typ.append("EQ" if eq else ("THR" if S.h else "OTHER"))
        st.c["type_" + typ[-1]] += 1
    vc = [A[k].Xi != A[k + 1].Xi or A[k].W != A[k + 1].W for k in range(T)]
    cross = [A[k].R != A[k + 1].R for k in range(T)]
    inph = [A[k].lamX == A[k + 1].lamX and A[k].lamU == A[k + 1].lamU and states[k][1][o] == states[k + 1][1][o] for k in range(T)]
    Fch = [any(A[k].Xi[v] != A[k + 1].Xi[v] for v in range(n) if v not in A[k].R) for k in range(T)]
    # ---- fallbacks: FBL-N, NF
    for k in range(T):
        if not (fbs[k] and inph[k]): continue
        S0, S1 = A[k], A[k + 1]
        st.c["fb_in_phase"] += 1
        for x, z in S0.Is:
            if x not in S0.R:
                st.c["FBLN_ii_checks"] += 1
                if not (S0.W[x][0] == x and S0.W[z][0] == x): st.bad(f"{name} k={k} FBL-N (ii) ({x},{z})")
                if not H2[k] and z in S0.R: st.bad(f"{name} k={k} FBL-N (iii) ({x},{z})")
        if typ[k] != "OTHER" and typ[k + 1] != "OTHER":
            st.c["NF_checks"] += 1
            if vc[k] and not cross[k]: st.bad(f"{name} k={k} NF: non-flat fallback without crossing")
            if vc[k]: st.c["NF_nonflat_fb_crossing"] += 1
        elif vc[k]:
            st.c["control_nonflat_fb_touching_OTHER"] += 1
            if not cross[k]: st.c["control_nonflat_fb_OTHER_no_crossing"] += 1
    # ---- phases
    k = 0
    while k <= T:
        k0 = k
        while k < T and inph[k]: k += 1
        phase(g, o, A, states, fbs, typ, vc, cross, Fch, H2, k0, k, st, name)
        k += 1

def phase(g, o, A, states, fbs, typ, vc, cross, Fch, H2, p0, p1, st, name):
    n = g.n
    st.c["phases"] += 1
    trans = range(p0, p1)
    X = sum(cross[k] for k in trans)
    O = sum(1 for k in trans if typ[k] == "OTHER" or typ[k + 1] == "OTHER")
    nvc = sum(vc[k] for k in trans)
    bound_vc = 3 * n * n * (1 + X + O) + X + O
    if nvc > bound_vc: st.bad(f"{name} phase {p0}..{p1} vc {nvc} > {bound_vc}")
    if p1 - p0 > (bound_vc + 1) * (4 * n * (n - 1) + 1): st.bad(f"{name} phase {p0}..{p1} length")
    st.mx["phase_max_len"] = max(st.mx["phase_max_len"], p1 - p0)
    st.mx["phase_max_X"] = max(st.mx["phase_max_X"], X); st.mx["phase_max_O"] = max(st.mx["phase_max_O"], O)
    # Lemma EQ: maximal EQ runs
    k = p0
    while k <= p1:
        if typ[k] != "EQ": k += 1; continue
        q0 = k
        while k < p1 and typ[k + 1] == "EQ": k += 1
        c = sum(vc[j] for j in range(q0, k))
        st.c["EQ_runs"] += 1; st.mx["EQ_max_vc"] = max(st.mx["EQ_max_vc"], c)
        if c > n - 1: st.bad(f"{name} EQ run {q0}..{k} vc {c}")
        for j in range(q0, k):
            if fbs[j] and vc[j]: st.bad(f"{name} EQ fallback value-changing at {j}")
        k += 1
    wurun(g, o, A, fbs, typ, p0, p1, st, name)   # (w, u*)-runs span crossings: one call per phase
    # F-intervals
    cut = lambda j: cross[j] or typ[j] == "OTHER" or typ[j + 1] == "OTHER"
    k = p0
    while k <= p1:
        i0 = k
        while k < p1 and not cut(k): k += 1
        finterval(g, o, A, states, fbs, typ, vc, Fch, H2, i0, k, st, name)
        k += 1

def finterval(g, o, A, states, fbs, typ, vc, Fch, H2, i0, i1, st, name):
    n = g.n
    if i1 == i0: return
    st.c["F_intervals"] += 1
    F = set(range(n)) - A[i0].R
    nf = sum(Fch[j] for j in range(i0, i1))
    st.mx["F1_max"] = max(st.mx["F1_max"], nf)
    if nf > max(len(F) - 1, 0): st.bad(f"{name} F1 interval {i0}..{i1}: {nf} F-changes, |F|={len(F)}")
    to = states[i0][1][o]
    for j in range(i0, i1):
        if typ[j] == "EQ" and typ[j + 1] == "THR":
            st.c["F2_EQ_THR"] += 1
            if to in A[j].R or A[j].Xi[to] == A[j + 1].Xi[to]: st.bad(f"{name} F2 at {j}")
        if typ[j] == "THR" and typ[j + 1] == "THR":
            if A[j].w != A[j + 1].w:
                st.c["F2_wchange"] += 1
                if A[j].Xi[to] == A[j + 1].Xi[to]: st.bad(f"{name} F2 second claim at {j}")
            if A[j].theta != A[j + 1].theta:
                st.c["TF_theta_change"] += 1
                if not Fch[j]: st.bad(f"{name} TF: theta change without F change at {j}")
    # sub-blocks: THR runs with w constant (Theorem X step 4); PIECE theta-free, flat fallbacks inside
    j = i0
    while j <= i1:
        if typ[j] != "THR": j += 1; continue
        s0 = j
        while j < i1 and typ[j + 1] == "THR" and A[j].w == A[j + 1].w: j += 1
        R = A[s0].R; Fs = set(range(n)) - R
        # R-part counted by W (routes against the constant terminal w); Xi on R moves also with theta (counted in the F-part, TF)
        vR = sum(1 for t in range(s0, j) if any(A[t].W[v] != A[t + 1].W[v] for v in R))
        vRx = sum(1 for t in range(s0, j) if any(A[t].Xi[v] != A[t + 1].Xi[v] or A[t].W[v] != A[t + 1].W[v] for v in R))
        if vRx > max(len(R) - 1, 0):
            st.c["R19f_literal_split_fails(Xi on R counted)"] += 1
            st.ex("R19f_literal", f"{name} sub-block {s0}..{j}: |R|={len(R)} R-changes incl. Xi={vRx}")
        vF = sum(1 for t in range(s0, j) if any(A[t].Xi[v] != A[t + 1].Xi[v] or A[t].W[v] != A[t + 1].W[v] for v in Fs))
        vv = sum(vc[t] for t in range(s0, j))
        nth = sum(1 for t in range(s0, j) if A[t].theta != A[t + 1].theta)
        st.c["subblocks"] += 1; st.c["subblocks_theta_varying"] += nth > 0
        st.c["subblock_flat_fb"] += sum(fbs[t] for t in range(s0, j))
        if vR > max(len(R) - 1, 0) or vF > max(len(Fs) - 1, 0) or vv > len(R) + len(Fs) - 2:
            st.bad(f"{name} PIECE sub-block {s0}..{j}: vR={vR} vF={vF} vc={vv}")
        # R-side Xi-changes without a route change and without an F-change (the theta-free gap): must not exist
        for t in range(s0, j):
            rch = any(A[t].W[v] != A[t + 1].W[v] for v in R)
            xich = any(A[t].Xi[v] != A[t + 1].Xi[v] for v in R)
            if xich and not rch:
                st.c["R_Xi_change_without_route_change"] += 1
                if not Fch[t]: st.bad(f"{name} sub-block {s0}: R Xi-change with no route and no F change at {t}")
        j += 1

def wurun(g, o, A, fbs, typ, i0, i1, st, name):
    """(w, u*)-runs inside the phase [i0, i1] (THR, w and u* constant, u* != none): Lemma C, CR, FB-W."""
    n = g.n
    def ustar(k):
        D = A[k].theta[1] ^ A[k].w[1]
        return max(D, key=lambda u: g.rank[u]) if D else None
    j = i0
    while j <= i1:
        if typ[j] != "THR" or ustar(j) is None: j += 1; continue
        k0 = j; u = ustar(j)
        while j < i1 and typ[j + 1] == "THR" and A[j + 1].w == A[k0].w and ustar(j + 1) == u: j += 1
        k1 = j; j += 1
        st.c["wu_runs"] += 1
        if k1 > k0 and any(A[t].theta != A[k0].theta for t in range(k0, k1 + 1)): st.c["wu_runs_theta_varying"] += 1
        C = lambda val: coarse(g, val, u)
        last = None
        for t in range(k0, k1 + 1):
            for v in range(n):
                if C(A[t].Xi[v]) != C(A[t].W[v]): st.bad(f"{name} (w,u*) Lemma C eq t={t} v={v}")
                if t < k1 and ccmp(g, C(A[t + 1].Xi[v]), C(A[t].Xi[v])) < 0: st.bad(f"{name} (w,u*) Lemma C mono t={t}")
            if t < k1 and any(C(A[t].Xi[v]) != C(A[t + 1].Xi[v]) for v in range(n)): last = t - k0 + 1
        if last is not None and last > n - 1: st.bad(f"{name} (w,u*) CR: coarse change at {last} > n-1")
        winw = u in A[k0].w[1]
        st.mx["wu_run_max_len"] = max(st.mx["wu_run_max_len"], k1 - k0)
        for L in range(k0 + n - 1, k1):
            if not fbs[L]: continue
            for x in A[L].R - A[L + 1].R:
                z = A[L + 1].f[x]
                if A[L].f[x] == z or z not in (set(range(n)) - A[L + 1].R): continue
                if (u in A[L].Xi[z][1]) != winw:
                    st.c["FBW_theta_status_evictions(not covered)"] += 1
                    if any(x in A[t].R for t in range(L + 1, k1 + 1)): st.c["FBRE-F_reentries(theta status)"] += 1
                    continue
                st.c["FBW_checks"] += 1
                if any(x in A[t].R for t in range(L + 1, k1 + 1)): st.bad(f"{name} FB-W x={x} L={L}")

def main():
    st = rc.Stats()
    if sys.argv[1] == "random":
        N, nmin, nmax, seed = map(int, sys.argv[2:6]); mode = sys.argv[6] if len(sys.argv) > 6 else "own"
        rng = random.Random(seed)
        for i in range(N):
            g, o = rc.rand_game(rng, rng.randint(nmin, nmax)); s, t = rc.rand_start(rng, g)
            states, fbs = rc.n5_spec(g, o, s, t) if mode == "spec" else rc.n5_own(g, o, s, t, rng)
            check_run(g, o, states, fbs, st, f"seed{seed}#{i}")
    else:
        path = sys.argv[2]; g = rc.parse(open(path).read())
        o = [v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) > 1][0]
        mode, start, runs = "own", None, 20
        for a in sys.argv[3:]:
            if a in ("own", "spec"): mode = a
            elif a.isdigit(): runs = int(a)
            else: start = a
        rng = random.Random(1)
        for r in range(1 if mode == "spec" else runs):
            if start:
                s0, t0 = rc.read_start(start)
                s = [s0.get(v, g.succ[v][0]) for v in range(g.n)]; t = [t0.get(v, g.succ[v][0]) for v in range(g.n)]
            elif r == 0:
                def br(v, dual):
                    def rr(w_):
                        p = g.prio[w_] + (1 if dual else 0); r_ = p if p % 2 == 0 else -p
                        return (r_, w_ if r_ % 2 == 0 else -w_)
                    return max(g.succ[v], key=rr)
                s = [br(v, False) for v in range(g.n)]; t = [br(v, True) for v in range(g.n)]
            else:
                s, t = rc.rand_start(rng, g)
            states, fbs = rc.n5_spec(g, o, s, t) if mode == "spec" else rc.n5_own(g, o, s, t, rng)
            check_run(g, o, states, fbs, st, f"{os.path.basename(path)}#{r}")
    for k in sorted(st.c): print(f"{k}: {st.c[k]}")
    for k in sorted(st.mx): print(f"{k}: {st.mx[k]}")
    for k, v in st.examples.items(): print(f"example {k}: {v}")
    for v in st.viol: print("VIOLATION", v)
    print("RESULT", "FAIL" if st.c["VIOLATIONS"] else "OK", f"violations={st.c['VIOLATIONS']}")

if __name__ == "__main__":
    main()
