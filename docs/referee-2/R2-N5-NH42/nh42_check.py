#!/usr/bin/env python3
r"""REFEREE-2 successor 13 (Opus 5.5, D15): mechanical check of packet P-N5-NH-box42 (docs/new/P-N5-NH-box42.md sha1 93d19be8 @ 54ac72e6).
Definitions from ../R2-N5-RE/re_check.py (play values, SPEC S1 order, honest valuation = pointwise minimum over Odd's choices at o).
Traces: spec (SPEC state sequence, experiments/new/n5.py read-only) | own (re_check.n5_own: random arena optima, every lemma uses (F1)).
Phase = (lambda_Xi, tau) constant; R = vertices whose (sigma, tau)-play reaches o, o in R (R22 convention); F = V \ R; interval = maximal
run of a phase with R constant; stretch = maximal run with R, theta, w constant. EQ: Xi = W; THR: (h) and Xi != W; OTHER: else.
Classes of a stretch: route forms hon := H1 or c_theta = o, wf := H2 or c_w = o; P3' / U1 (both, c_theta resp. c_w more relevant), U2
(not hon, wf), U3 (hon, not wf), U23 (neither). Kind (U3 / U23): v in R \ {o} is A iff c_w in pi_v. Event: E_broad = transition with a
kind change of some R-vertex or a switch of c_w; E_narrow = a switching Even R-vertex whose own kind changes, or a switch of c_w.
Checks: SW (b); ST (a)-(c); CL (a), (b); STR-COUNT (a)-(d) (with the H1 / H2 F-change facts); F1° per interval; NR per OTHER stretch
(signed class bound and the crude n^3(1 + f_S) + 2n(K_S + E_S), with E_broad); the R15d run bound per OTHER stretch; Theorem NH (a), (b),
(c) per phase. Records: class counts, maxima of O, X, f^O, K_W, E, N_R per class; NR with E_narrow (record).
Mutations NH_MUT: sw (SW (b) asks for NO switch), run (R15d bound 1), stc (stretches <= Theta_I + WC_I), nr (P3' / U1 / U2 / U3 bound - 2).
Usage: nh42_check.py random N nmin nmax seed [spec|own] | files list.txt [runs] [spec|own]"""
import sys, os, random
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-RE"))
import re_check as rc
MUT = os.environ.get("NH_MUT", "")
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))

class Stats:
    def __init__(s): s.c = Counter(); s.mx = {}; s.viol = []
    def bad(s, k, msg):
        s.c["VIOLATIONS"] += 1; s.c["V_" + k] += 1
        if len(s.viol) < 30: s.viol.append(f"{k}: {msg}")
    def mxr(s, k, v, name):
        if k not in s.mx or v > s.mx[k][0]: s.mx[k] = (v, name)

def per_state(g, o, S):
    S.H1 = not rc._returns(S.fh, o); S.H2 = not rc._returns(S.f, o)
    S.cth, S.cw = S.Xi[o][0], S.W[o][0]
    S.EQ = all(S.Xi[v] == S.W[v] for v in range(g.n))
    S.typ = "EQ" if S.EQ else ("THR" if S.h else "OTHER")
    hon = S.H1 or S.cth == o; wf = S.H2 or S.cw == o
    if hon and wf:
        S.cls = "P3" if g.rank[S.cth] > g.rank[S.cw] else ("U1" if g.rank[S.cw] > g.rank[S.cth] else "EQC")
    elif wf: S.cls = "U2"
    elif hon: S.cls = "U3"
    else: S.cls = "U23"
    S.Rs = frozenset(S.R)
    S.kind = {v: (S.cw in S.pi[v]) for v in S.R if v != o}

def check_run(g, o, states, fbs, st, name):
    n = g.n; A = [rc.analyse(g, o, *s) for s in states]
    for S in A: per_state(g, o, S)
    st.c["runs"] += 1; st.c["transitions"] += len(fbs)
    D = 4 * n * (n - 1) + 1
    key = [(S.lamX, tuple(states[k][1])) for k, S in enumerate(A)]
    phases, cur = [], [0]
    for k in range(1, len(A)):
        if key[k] == key[k - 1]: cur.append(k)
        else: phases.append(cur); cur = [k]
    phases.append(cur)
    for ph in phases:
        st.c["phases"] += 1
        tr = ph[:-1]                                  # transitions k -> k+1 inside the phase
        X = sum(1 for k in tr if A[k].Rs != A[k + 1].Rs)
        O = sum(1 for k in tr if A[k].typ == "OTHER" or A[k + 1].typ == "OTHER")
        fO = sum(1 for k in tr if fbs[k] and A[k].typ == "OTHER")
        T = len(tr)
        # intervals and stretches
        ivs, cur = [], [ph[0]]
        for k in ph[1:]:
            if A[k].Rs == A[cur[-1]].Rs: cur.append(k)
            else: ivs.append(cur); cur = [k]
        ivs.append(cur)
        N = 0; KW = EB = EN = 0
        for I in ivs:
            S0 = A[I[0]]; R = S0.Rs; F = set(range(n)) - R
            for k in I:
                if A[k].H1 != S0.H1 or A[k].H2 != S0.H2: st.bad("TC", f"{name}: H1/H2 not constant on I at {k}")
            itr = I[:-1]
            # F1°
            fch = [k for k in itr if any(A[k].Xi[v] != A[k + 1].Xi[v] for v in F)]
            if len(fch) > max(0, len(F) - 1): st.bad("F1", f"{name}: F1° {len(fch)} > |F|-1 at I {I[0]}")
            th = [k for k in itr if A[k].theta != A[k + 1].theta]
            wc = [k for k in itr if A[k].w != A[k + 1].w]
            fOI = sum(1 for k in itr if fbs[k] and A[k].typ == "OTHER")
            # STR-COUNT (a)
            if len(th) > n - 1: st.bad("STRa", f"{name}: Theta_I {len(th)} > n-1")
            if not S0.H1:
                if len(th) > len(R) - 1: st.bad("STRa", f"{name}: not H1, Theta_I {len(th)} > |R|-1")
                for k in I:
                    if A[k].theta[1] or A[k].theta[0] != S0.cth: st.bad("STRa", f"{name}: not H1, theta not (c, {{}}, d) at {k}")
            else:
                for k in th:
                    if k not in fch: st.bad("STRa", f"{name}: H1 theta-change without Xi-change on F at {k}")
            # STR-COUNT (b)
            if S0.H2:
                for k in wc:
                    if k not in fch: st.bad("STRb", f"{name}: H2 w-change without Xi-change on F at {k}")
                if len(wc) > n - 1: st.bad("STRb", f"{name}: H2 WC_I {len(wc)} > n-1")
            elif len(wc) > (fOI + 1) * (len(R) ** 2 - 1) + fOI: st.bad("STRb", f"{name}: WC_I {len(wc)} > R24 (e)")
            # stretches
            sts, cs = [], [I[0]]
            for k in I[1:]:
                if (A[k].theta, A[k].w) == (A[cs[-1]].theta, A[cs[-1]].w): cs.append(k)
                else: sts.append(cs); cs = [k]
            sts.append(cs)
            lim = 1 + len(th) + len(wc) if MUT != "stc" else len(th) + len(wc)
            if len(sts) > lim: st.bad("STRc", f"{name}: stretches {len(sts)} > 1 + Theta + WC {lim}")
            if 1 + len(th) + len(wc) > n - 1 + (fOI + 1) * n * n: st.bad("STRc", f"{name}: 1 + Theta + WC over n-1+(f+1)n^2")
            N += 1 + len(th) + len(wc)
            # ST (a), (b)
            others = [A[k].typ == "OTHER" for k in I]
            if not (not S0.H1 and not S0.H2):
                if len(set(others)) > 1: st.bad("STa", f"{name}: OTHER status varies on I (H1 {S0.H1}, H2 {S0.H2})")
            else:
                for k in I:
                    if (A[k].typ == "OTHER") != (A[k].theta != A[k].w): st.bad("STb", f"{name}: not H1 not H2: OTHER != (theta != w) at {k}")
            for S in sts:
                ss = [A[k] for k in S]
                if len({x.typ == "OTHER" for x in ss}) > 1: st.bad("STc", f"{name}: OTHER status varies on a stretch")
                strn = S[:-1]
                # SW (b)
                for k in strn:
                    chg = any(A[k].Xi[v] != A[k + 1].Xi[v] or A[k].W[v] != A[k + 1].W[v] for v in R)
                    sw = any(states[k][0][v] != states[k + 1][0][v] for v in R if g.owner[v] == 0)
                    if chg and (sw == (MUT == "sw")): st.bad("SW", f"{name}: Xi/W change on R without switch on R at {k}")
                if ss[0].typ != "OTHER": continue
                st.c["other_stretches"] += 1
                c0 = ss[0]
                if any((x.H1, x.H2, x.cth, x.cw, x.cls) != (c0.H1, c0.H2, c0.cth, c0.cw, c0.cls) for x in ss): st.bad("CLa", f"{name}: class varies")
                if c0.cls == "EQC": st.bad("CLb", f"{name}: OTHER route-form stretch with c_theta = c_w"); continue
                st.c["cls_" + c0.cls] += 1
                r = len(R); fS = sum(1 for k in strn if fbs[k])
                NR = sum(1 for k in strn if any(A[k].Xi[v] != A[k + 1].Xi[v] for v in R))
                KS = sum(1 for k in strn if not fbs[k] and any(A[k].W[v] != A[k + 1].W[v] for v in R)) if c0.cls in ("U2", "U3", "U23") else 0
                ESb = ESn = 0
                if c0.cls in ("U3", "U23"):
                    for k in strn:
                        a, b = A[k], A[k + 1]; sg0, sg1 = states[k][0], states[k + 1][0]
                        cwsw = g.owner[c0.cw] == 0 and sg0[c0.cw] != sg1[c0.cw]
                        broad = any(a.kind[v] != b.kind[v] for v in a.kind)
                        narrow = any(a.kind[v] != b.kind[v] for v in a.kind if g.owner[v] == 0 and sg0[v] != sg1[v])
                        ESb += (broad or cwsw); ESn += (narrow or cwsw)
                KW += KS; EB += ESb; EN += ESn
                d = 2 if MUT == "nr" else 0
                if c0.cls == "P3": b = (n + 1) * r - d
                elif c0.cls == "U1":
                    K = (fS + 1) * (r - 1) * (r - 2); b = r + fS + K + (K + fS + 1) * (r - 2) - d
                elif c0.cls == "U2": b = fS + KS + (KS + fS + 1) * (r - 2) - d
                else: b = fS + KS + ESb + (KS + fS + ESb + 1) * (2 * r - 4) - d
                if NR > b: st.bad("NR", f"{name}: class {c0.cls} N_R {NR} > signed bound {b}")
                if NR > n ** 3 * (1 + fS) + 2 * n * (KS + ESb): st.bad("NR", f"{name}: crude NR bound")
                if c0.cls in ("U3", "U23"):
                    bn = fS + KS + ESn + (KS + fS + ESn + 1) * (2 * r - 4)
                    if NR > bn: st.c["REC_NR_fails_with_E_narrow"] += 1
                st.mxr("max_NR_" + c0.cls, NR, name)
                # R15d run bound
                run = 0
                for k in strn:
                    if A[k].Xi == A[k + 1].Xi: run += 1
                    else: run = 0
                    if run > (4 * n * (n - 1) if MUT != "run" else 1): st.bad("R15d", f"{name}: Xi-flat run {run}"); break
        if N > n * n * (2 * X + 2 + fO): st.bad("STRd", f"{name}: N {N} > n^2(2X+2+f^O)")
        a = X + N + D * (n * (X + 1) + (n ** 3 + 1) * N + n ** 3 * fO + 2 * n * (KW + EB))
        Q = 1 + X + fO
        if O > a: st.bad("NHa", f"{name}: O {O} > (a) {a}")
        if O > 11 * n ** 7 * Q + 8 * n ** 3 * (KW + EB): st.bad("NHb", f"{name}: O {O} > (b)")
        if T > 156 * n ** 11 * Q + 104 * n ** 7 * (KW + EB): st.bad("NHc", f"{name}: T {T} > (c)")
        if O: st.c["phases_with_O"] += 1; st.c["sum_O"] += O
        for k_, v_ in (("O", O), ("X", X), ("fO", fO), ("KW", KW), ("E_broad", EB), ("E_narrow", EN), ("T", T)):
            st.mxr("max_" + k_, v_, name)
        if O: st.mxr("O_over_NHa_x1e6", int(1e6 * O / a), name)

def main():
    st = Stats(); a = sys.argv[1:]
    def go(g, o, s, t, name, mode, rng):
        states, fbs = rc.n5_spec(g, o, s, t) if mode == "spec" else rc.n5_own(g, o, s, t, rng)
        check_run(g, o, states, fbs, st, name)
    if a[0] == "random":
        N_, nmin, nmax, seed = map(int, a[1:5]); mode = a[5] if len(a) > 5 else "spec"; rng = random.Random(seed)
        for i in range(N_):
            g, o = rc.rand_game(rng, rng.randint(nmin, nmax), cyc=rng.random() < 0.8)
            s, t = rc.rand_start(rng, g)
            go(g, o, s, t, f"random{seed}:{i}", mode, rng)
    else:
        runs = int(a[2]) if len(a) > 2 else 2; mode = a[3] if len(a) > 3 else "spec"; rng = random.Random(4213)
        for path in [l.strip() for l in open(a[1]) if l.strip()]:
            g = rc.parse(open(os.path.join(ROOT, path)).read())
            oc = [v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) > 1]
            if len(oc) != 1: st.c["skipped_not_1O"] += 1; continue
            o = oc[0]
            for r in range(runs):
                s, t = s3(g) if r == 0 else rc.rand_start(rng, g)
                go(g, o, s, t, f"{path}#{r}", mode, rng)
    print("MODE", " ".join(a), "MUT", MUT or "-")
    for k in sorted(st.c): print(f"{k}: {st.c[k]}")
    for k in sorted(st.mx): print(f"{k}: {st.mx[k]}")
    for v in st.viol: print("VIOLATION", v)
    print("RESULT", "FAIL" if st.c["VIOLATIONS"] else "OK", f"violations={st.c['VIOLATIONS']}")

def s3(g):
    def br(v, dual):
        def rr(w):
            p = g.prio[w] + (1 if dual else 0)
            r_ = p if p % 2 == 0 else -p
            return (r_, w if r_ % 2 == 0 else -w)
        return max(g.succ[v], key=rr)
    return [br(v, False) for v in range(g.n)], [br(v, True) for v in range(g.n)]

if __name__ == "__main__":
    main()
