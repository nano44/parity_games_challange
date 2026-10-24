#!/usr/bin/env python3
"""REFEREE-2 (Opus 5.5, D15) mechanical check of packet P-N5-Z (docs/si/P-N5-Z-box5.md @ trunk fba7177).
Definitions and own N5 (random tie-breaks) from ../R2-N5-RE/re_check.py; "spec" = n5.py's state sequence.
Convention of the packet: R excludes o (my re_check R includes o; I remove it here). Phase = lambda_Xi, lambda_U, tau constant.
Checks: Step (K) (at a fallback in a phase, no arena single switch raises W at its vertex); ACT (i)/(ii) at tau-constant transitions;
LOOP (H1 at k, in phase: no new o-free cycle inside R_k); NOFE strong form; NOFL-E; GAP; WM; LV' per phase (and the packet's literal
run claim, runs = maximal runs of equal pure signs IGNORING '+-' transitions, tested separately); Corollary Z bound per phase.
Usage: z_check.py random N nmin nmax seed [own|spec] | z_check.py inst game.pg [start] [own|spec] [runs]"""
import sys, os, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2-N5-RE"))
import re_check as rc

def cyc(f, v):
    seen, path, x = {}, [], v
    while x not in seen: seen[x] = len(path); path.append(x); x = f[x]
    return path[seen[x]:]

def oplay(f, o):
    """vertices of o's play (o first, until the first repeat)."""
    seen, x, out = set(), o, []
    while x not in seen: seen.add(x); out.append(x); x = f[x]
    return out

def check_run(g, o, states, fbs, st, name):
    n = g.n; T = len(states) - 1
    A = [rc.analyse(g, o, *s) for s in states]
    st.c["runs"] += 1; st.c["transitions"] += T
    for S in A:
        S.Rx = S.R - {o}; S.Fx = set(range(n)) - S.R
        S.H1 = o not in cyc(S.fh, o); S.H2 = o not in cyc(S.f, o)
        S.typ = "EQ" if S.Xi == S.W else ("THR" if S.h else "OTHER")
    inph = [A[k].lamX == A[k + 1].lamX and A[k].lamU == A[k + 1].lamU and states[k][1][o] == states[k + 1][1][o] for k in range(T)]
    for k in range(T):
        S0, S1 = A[k], A[k + 1]
        tauc = states[k][1][o] == states[k + 1][1][o]
        Sw = {v for v in range(n) if g.owner[v] == 0 and S0.f[v] != S1.f[v]}
        if tauc:                                   # ACT
            if S1.Rx - S0.Rx:
                st.c["ACT_i"] += 1
                if not any(s in S0.Fx and S1.f[s] in S0.R and s in S1.Rx for s in Sw): st.bad(f"{name} ACT (i) at {k}")
            if S0.Rx - S1.Rx:
                st.c["ACT_ii"] += 1
                a1 = any(s in S0.Rx and S1.f[s] in S0.Fx and s not in S1.Rx for s in Sw)
                cyc_alt = False
                for s in Sw & S0.Rx:
                    C = cyc(S1.f, s)
                    if o not in C and set(C) <= S0.Rx and s in C: cyc_alt = True
                if not (a1 or cyc_alt): st.bad(f"{name} ACT (ii) at {k}")
                if not a1: st.c["ACT_ii_cycle_alternative"] += 1
                if inph[k] and S0.H1:              # LOOP
                    st.c["LOOP_checks"] += 1
                    if not a1: st.bad(f"{name} LOOP at {k}")
        if not inph[k]: continue
        # WM
        if not fbs[k]:
            st.c["WM_checks"] += 1
            if any(g.cmp(S1.W[v], S0.W[v]) < 0 for v in range(n)): st.bad(f"{name} WM at {k}")
        else:
            st.c["fb_in_phase"] += 1
            if any(g.cmp(S1.W[v], S0.W[v]) < 0 for v in range(n)): st.c["W_lowering_fallbacks"] += 1
            # Step (K): no arena edge (v, z) whose single switch raises W at v
            arena = {v: {S0.f[v]} | {z for x, z in S0.Is if x == v} for v in range(n) if g.owner[v] == 0}
            for v, zs in arena.items():
                for z in zs:
                    if z == S0.f[v]: continue
                    f2 = list(S0.f); f2[v] = z
                    st.c["StepK_checks"] += 1
                    if g.cmp(g.play(f2, v)[0], S0.W[v]) > 0: st.bad(f"{name} Step (K) at {k} ({v},{z})")
            op = set(oplay(S0.f, o))
            for y in Sw:
                z = S1.f[y]
                if y in S0.Fx and z in S0.R:       # NOFE
                    st.c["NOFE_edges"] += 1
                    if y not in op: st.bad(f"{name} NOFE at {k} ({y},{z})")
                    if S0.W[y][0] == y: st.c["NOFE_tail_is_W_cycle_node"] += 1
                if y in S0.Rx and z in S0.Fx:      # NOFL-E, GAP
                    if S0.Xi == S0.W and S0.H2:
                        st.c["NOFLE_violations_candidates"] += 1; st.bad(f"{name} NOFL-E at {k} ({y},{z})")
                    if S0.h:
                        st.c["GAP_edges"] += 1
                        sy = S0.f[y]
                        if not (g.cmp(S0.Xi[sy], S0.Xi[z]) < 0 and g.cmp(S0.Xi[z], S0.W[sy]) <= 0): st.bad(f"{name} GAP at {k} ({y},{z})")
                        pre = rc.prefix(g, S0.pi[sy], S0.theta), rc.prefix(g, S0.pi[sy], S0.w)
                        if pre != (S0.Xi[sy], S0.W[sy]): st.bad(f"{name} GAP pi'-form at {k}")
            if S0.Xi == S0.W and S0.H1 and S0.H2:
                st.c["NOFLE_cor_checks"] += 1
                if S0.Rx - S1.Rx: st.bad(f"{name} NOFL-E corollary: leave at {k}")
    # phases: LV', Corollary Z
    k = 0
    while k <= T:
        p0 = k
        while k < T and inph[k]: k += 1
        phase(g, o, A, p0, k, st, name)
        k += 1

def phase(g, o, A, p0, p1, st, name):
    n = g.n
    signs = []
    for k in range(p0, p1):
        a, b = A[k].Rx, A[k + 1].Rx
        if a == b: continue
        signs.append("+" if a < b else ("-" if b < a else "pm"))
    X = len(signs)
    Z = sum(1 for s in signs if s == "pm")
    prev = None
    for s in signs:
        if s == "pm": continue
        if prev is not None and s != prev: Z += 1
        prev = s
    st.c["phases"] += 1; st.mx["phase_max_X"] = max(st.mx["phase_max_X"], X); st.mx["phase_max_Z"] = max(st.mx["phase_max_Z"], Z)
    if X > (n - 1) * (Z + 1) + Z or Z > X: st.bad(f"{name} LV' phase {p0}..{p1}: X={X} Z={Z}")
    st.c["pm_transitions"] += sum(1 for s in signs if s == "pm")
    # the packet's literal run claim: runs of equal pure signs ignoring 'pm'
    pure = [s for s in signs if s != "pm"]
    j = 0
    while j < len(pure):
        i = j
        while j + 1 < len(pure) and pure[j + 1] == pure[i]: j += 1
        L = j - i + 1
        st.mx["literal_run_max"] = max(st.mx["literal_run_max"], L)
        if L > n - 1:
            st.c["literal_run_exceeds_n-1"] += 1
            st.ex("literal_run", f"{name} phase {p0}..{p1}: pure-sign run of {L} > n-1 = {n - 1} (with '+-' inside)")
        j += 1
    O = sum(1 for k in range(p0, p1) if A[k].typ == "OTHER" or A[k + 1].typ == "OTHER")
    if p1 - p0 > (3 * n * n * (1 + X + O) + X + O + 1) * (4 * n * (n - 1) + 1): st.bad(f"{name} Corollary Z bound")

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
        oc = [v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) > 1]
        if len(oc) != 1:
            print(f"SKIPPED: not C^1O (Odd choice vertices {oc}); the packet's lemmas do not apply"); print("RESULT OK violations=0 (skipped)"); return
        o = oc[0]
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
