#!/usr/bin/env python3
"""REFEREE-2 successor 9 (Opus 5.5, D15): mechanical check of packet P-N5-OUT (docs/new/P-N5-OUT-box37.md sha1 9f032e61 @ trunk 719ce66).
Own code on my lane's R2-N5-FRZ/frz_check.py and R2-N5-RE/re_check.py (play values, VJ00 order, honest valuation = pointwise minimum over
Odd's choices at o, Even's one-player optimum by SI, own N5 loop). No lane script is imported in modes own / rand. Mode spec takes the
STATE SEQUENCE from experiments/new/n5.py (SPEC tie-breaks, via re_check.n5_spec) and checks it with this file's definitions; every count
is printed with its trace label (own | rand | spec). Every game asserts exactly one Odd vertex with out-degree > 1.
Phase = maximal run of states with (lambda_Xi, tau) constant (the packet's; KEY). HN state: H1 and not H2. HN stretch: maximal run of HN
states of one phase. R = R-bar minus o. Crossing: in-phase, R changes. Entry: R grows strictly; eviction: R-bar shrinks strictly.
Checks (packet items):
  SPLIT     in-phase k->k+1, HN at k: (a) non-fallback => R_k <= R_{k+1}; (b) fallback => Rbar_{k+1} <= Rbar_k; every crossing of an
            HN stretch is an S4a entry or a fallback eviction.
  EPOCH     per HN stretch: segments (cut before breaks) have entries before evictions, <= n-1 of each; X_S <= 2(n-1)(B+1);
            f_S <= K(X_S+1)+X_S. Also counts how often the SUPERSEDED f_S <= K(X_S+1) fails (record).
  FBINT     dependency: <= K fallbacks per maximal crossing-free run of a phase.
  FFLAT     in-phase Even fallback, HN at k: Xi unchanged on F_k, theta unchanged; Step 1 facts for every gate from F_k (z in F_k,
            lambda(x) = x, lambda(z) = x, level -1).
  FREEZE    in-phase t->t+1, HN at t, H1 at t+1, theta equal, no gate into Rbar_t: (i) Rbar_{t+1} <= Rbar_t and routes equal; (ii) Xi
            equal on Rbar_{t+1}; (iii) no gate into Rbar_{t+1}. TAIL: from every such t, walked to the first theta change in the stretch.
  STEPK     dependency R23 (a): at every in-phase fallback, no gate edge (y, z) has W_{sigma[y->z]}(y) > W(y).
  NEA       tau(o) = o phases: case split facts (XW reward, Omega(o) even in case A, Omega(c_theta) odd in case B); SEP-o at H1 states
            (case A); for every HN state a with an Even fallback a->a+1 and every b with theta constant on [a, b] inside the stretch:
            INV(t), no entry, Rbar shrinks, Xi_t(z) == Xi_a(z) mod levels < rank(o). INV also tested in case B (record, not claimed).
  NECOUNT   case-A tau(o) = o phases: (a) every break has an S4a theta change in (a, k], disjoint; B <= theta_S; (b), (c) bounds.
            The same break test is run on case B and tau(o) != o stretches as a record (CONJECTURE NO-ENTRY data), not a check.
  CASEB     case-B tau(o) = o, HN state a with Even fallback: every R -> Rbar gate is level -1 with z's route longer; W-SIDE Case 1/2.
  T123      (T1)-(T3) on random valuation pairs (separate mode).
Usage: out_check.py random N nmin nmax seed [own|rand|spec] | inst game.pg [runs] [own|rand|spec] | t123 N seed"""
import sys, os, random
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-FRZ"))
import frz_check as FC
RC = FC.RC
INF, BOT = FC.INF, FC.BOT
MUT = os.environ.get("OUT_MUT", "")   # mutation tests only: theta | caseB | oldfs | nohyp
lev = FC.lev

class Stats(FC.Stats):
    pass

def analyse(g, o, sg, tu):
    S = FC.analyse(g, o, sg, tu)
    S.HN = S.H1 and not S.H2
    S.lamW = tuple(S.W[v][0] for v in range(g.n))
    S.Rr = S.Rbar - {o}
    return S

def run_trace(g, o, s, t, rng, mode):
    if mode == "spec":
        states, fbs = RC.n5_spec(g, o, s, t)
        return [analyse(g, o, sg, tu) for sg, tu in states], fbs
    A, fbs = FC.run_n5(g, o, s, t, rng, mode == "rand")
    return [analyse(g, o, S.sg, S.tu) for S in A], fbs

def key(S, o): return (S.lamX, S.tu[o])

def eqv(g, o, x, y): return lev(g, x, y) < g.rank[o]

def reward(g, c):
    p = 2 * g.rank[c] + (0 if g.even[c] else 1)
    return p if g.even[c] else -p

def gates_into(S, tgt): return [(y, z) for (y, z) in S.Is if z in tgt]

def wval_switch(g, S, y, z):
    f2 = list(S.f); f2[y] = z
    return g.play(f2, y)[0]

def check_run(g, o, A, fbs, st, name):
    n = g.n; nE = sum(1 for v in range(n) if g.owner[v] == 0); K = nE * (2 * n - 1)
    st.c["runs"] += 1; st.c["states"] += len(A)
    # phases
    phases, a = [], 0
    for k in range(1, len(A) + 1):
        if k == len(A) or key(A[k], o) != key(A[k - 1], o):
            phases.append((a, k - 1)); a = k
    inph = lambda k: key(A[k], o) == key(A[k + 1], o)
    # ---------------- per transition
    for k in range(len(A) - 1):
        S, T, fb = A[k], A[k + 1], fbs[k]
        if fb and inph(k):
            st.c["inphase_fallbacks"] += 1
            if S.tu != T.tu: st.bad(f"{name} in-phase fallback changed tau at {k}")
            # STEPK
            for (y, z) in S.Is:
                st.c["STEPK_gate_edges"] += 1
                if g.cmp(wval_switch(g, S, y, z), S.W[y]) > 0: st.bad(f"{name} STEPK edge {y}->{z} raises W at {k}")
        if not (inph(k) and S.HN): continue
        st.c["HN_inphase_transitions"] += 1
        if not fb:
            st.c["SPLIT_a_cases"] += 1
            if not S.Rr <= T.Rr: st.bad(f"{name} SPLIT(a) R shrank at S4a {k}: lost {sorted(S.Rr - T.Rr)}")
        else:
            st.c["SPLIT_b_cases"] += 1
            if not T.Rbar <= S.Rbar: st.bad(f"{name} SPLIT(b) Rbar gained at fallback {k}: {sorted(T.Rbar - S.Rbar)}")
            # FFLAT
            st.c["FFLAT_cases"] += 1
            for v in S.F:
                if T.Xi[v] != S.Xi[v]: st.bad(f"{name} FFLAT Xi changed at F-vertex {v}, transition {k}")
            if T.theta != S.theta: st.bad(f"{name} FFLAT theta changed at fallback {k}")
            for (x, z) in S.Is:
                if x not in S.F: continue
                st.c["FFLAT_step1_gates_from_F"] += 1
                if z not in S.F: st.bad(f"{name} FFLAT step1 target {z} of {x} not in F at {k}")
                if S.lamX[x] != x or S.lamX[z] != x or S.lamW[x] != x or S.lamW[z] != x: st.bad(f"{name} FFLAT step1 cycle nodes {x}->{z} at {k}")
                if lev(g, S.Xi[S.sg[x]], S.Xi[z]) != -1: st.bad(f"{name} FFLAT step1 level {lev(g, S.Xi[S.sg[x]], S.Xi[z])} != -1 at {k}")
        # FREEZE-STEP
        if T.H1 and T.theta == S.theta:
            hyp = not gates_into(S, S.Rbar) or MUT == "nohyp"
            st.c["FREEZE_H1_theta_equal_steps"] += 1
            if hyp:
                st.c["FREEZE_hyp_cases" + ("_fb" if fb else "_s4a")] += 1
                if not T.Rbar <= S.Rbar: st.bad(f"{name} FREEZE(i) Rbar grew at {k}")
                for z in T.Rbar:
                    if T.pi[z] != S.pi.get(z): st.bad(f"{name} FREEZE(i) route of {z} changed at {k}"); break
                for z in T.Rbar:
                    if T.Xi[z] != S.Xi[z]: st.bad(f"{name} FREEZE(ii) Xi({z}) changed at {k}"); break
                if gates_into(T, T.Rbar): st.bad(f"{name} FREEZE(iii) gate into Rbar at {k + 1}")
            else:
                # negative control: without the hypothesis, does some conclusion fail?
                ok = T.Rbar <= S.Rbar and all(T.pi[z] == S.pi.get(z) and T.Xi[z] == S.Xi[z] for z in T.Rbar) and not gates_into(T, T.Rbar)
                st.c["FREEZE_control_no_hyp"] += 1
                if not ok: st.c["FREEZE_control_no_hyp_conclusion_fails"] += 1
    # ---------------- per phase / stretch
    for (p0, p1) in phases:
        S0 = A[p0]; tauo = S0.tu[o]
        stretches, s = [], None
        for k in range(p0, p1 + 1):
            if A[k].HN and s is None: s = k
            if (not A[k].HN or k == p1) and s is not None:
                e = k if A[k].HN else k - 1
                stretches.append((s, e)); s = None
        if not stretches: continue
        cth = S0.theta[0]
        selfloop = (tauo == o)
        case = None
        if selfloop:
            st.c["tau_o_eq_o_phases_with_HN"] += 1
            if cth == o: st.bad(f"{name} NEA c_theta = o in a phase with an H1 state")
            if not reward(g, cth) < reward(g, o): st.bad(f"{name} NEA reward(c_theta) >= reward(o)")
            if g.rank[o] > g.rank[cth] or MUT == "caseB":
                case = "A"
                if not g.even[o] and MUT != "caseB": st.bad(f"{name} NEA case A with odd o")
            else:
                case = "B"
                if g.even[cth]: st.bad(f"{name} NEA case B with even c_theta")
            st.c[f"case{case}_phases"] += 1
        # phase-level numbers for NE-COUNT (c)
        T_ph = sum(1 for k in range(p0, p1) if A[k].H1 != A[k + 1].H1)
        th_ph = sum(1 for k in range(p0, p1) if A[k].theta != A[k + 1].theta)
        f_HN = sum(1 for k in range(p0, p1) if fbs[k] and A[k].HN)
        X_HN = 0
        for (s0, s1) in stretches:
            st.c["HN_stretches"] += 1
            tr = range(s0, s1)
            ent = lambda k: A[k].Rr < A[k + 1].Rr
            evi = lambda k: A[k + 1].Rbar < A[k].Rbar
            cross = lambda k: A[k].Rr != A[k + 1].Rr
            X_S = sum(1 for k in tr if cross(k)); f_S = sum(1 for k in tr if fbs[k]); X_HN += X_S
            for k in tr:
                if cross(k) and not ((ent(k) and not fbs[k]) or (evi(k) and fbs[k])): st.bad(f"{name} SPLIT crossing {k} neither S4a entry nor fallback eviction")
            # breaks
            breaks, seen_evi = [], False
            for k in tr:
                if ent(k):
                    if seen_evi: breaks.append(k)
                    seen_evi = False
                elif evi(k): seen_evi = True
            B = len(breaks)
            cuts = [s0] + breaks + [s1]
            for i in range(len(cuts) - 1):
                seg = range(cuts[i], cuts[i + 1]); E_ = [k for k in seg if ent(k)]; V_ = [k for k in seg if evi(k)]
                if E_ and V_ and max(E_) > min(V_): st.bad(f"{name} EPOCH entry after eviction inside a segment")
                if len(E_) > n - 1 or len(V_) > n - 1: st.bad(f"{name} EPOCH segment counts {len(E_)}/{len(V_)}")
            st.mxu("max_X_S", X_S); st.mxu("max_f_S", f_S); st.mxu("max_breaks_per_stretch", B)
            st.c["breaks"] += B
            if X_S > 2 * (n - 1) * (B + 1): st.bad(f"{name} EPOCH X_S {X_S} > 2(n-1)(B+1)")
            if f_S > K * (X_S + 1) + X_S: st.bad(f"{name} EPOCH f_S {f_S} > K(X_S+1)+X_S")
            if f_S > K * (X_S + 1):
                st.c["RECORD_superseded_fS_formula_fails"] += 1
                if MUT == "oldfs": st.bad(f"{name} MUT superseded f_S formula fails")
            st.c["fallbacks_in_stretches"] += f_S
            st.c["fallbacks_in_stretches_that_are_crossings"] += sum(1 for k in tr if fbs[k] and cross(k))
            # NE-COUNT (a) / break theta-separation record
            th_S = sum(1 for k in tr if A[k].theta != A[k + 1].theta)
            prev_entry = s0 - 1; last_end = -1; sep_all = True
            for k in tr:
                if not ent(k): continue
                if k in breaks:
                    a_ = next(j for j in range(prev_entry + 1, k) if evi(j))
                    js = [j for j in range(a_, k + 1) if A[j].theta != A[j + 1].theta]
                    good = bool(js) and all(not fbs[j] for j in js) and min(js) > a_ and a_ >= last_end
                    if not good: sep_all = False
                    lbl = f"{case}" if selfloop else "tau_ne_o"
                    st.c[f"breaks_{lbl}"] += 1
                    if not js: st.c[f"RECORD_breaks_{lbl}_not_theta_separated"] += 1
                    if case == "A" and not good: st.bad(f"{name} NECOUNT(a) break at {k} (eviction {a_}) theta changes {js}")
                    last_end = k + 1
                prev_entry = k
            if case == "A":
                st.c["NECOUNT_caseA_stretches"] += 1
                if B > th_S: st.bad(f"{name} NECOUNT(a) B {B} > theta_S {th_S}")
                if X_S > 2 * (n - 1) * (th_S + 1): st.bad(f"{name} NECOUNT(b) X_S")
            # NO-ENTRY-A and CASE-B-LEN
            if selfloop:
                check_nea(g, o, A, fbs, s0, s1, case, st, name)
        if case == "A":
            N_HN = len(stretches); Tstar = len([v for v in range(n) if A[p0].lamX[v] == cth]) * (n + 1) + n - 1
            if N_HN > T_ph // 2 + 1: st.bad(f"{name} NECOUNT(c) N_HN {N_HN} > T/2+1 ({T_ph})")
            if T_ph > Tstar: st.bad(f"{name} TOGGLE-COUNT {T_ph} > {Tstar}")
            if f_HN > (K + 1) * (2 * (n - 1) * th_ph + (2 * n - 1) * N_HN): st.bad(f"{name} NECOUNT(c) f_HN")
            if X_HN > 2 * (n - 1) * (th_ph + N_HN): st.bad(f"{name} NECOUNT(c) X_HN")
            st.mxu("max_f_HN_caseA_phase", f_HN); st.mxu("max_theta_ph_caseA", th_ph)
    # FB-INT (dependency) per maximal crossing-free run of each phase
    for (p0, p1) in phases:
        cnt = 0
        for k in range(p0, p1 + 1):
            if k == p1 or A[k].Rr != A[k + 1].Rr:
                st.mxu("max_fallbacks_per_crossing_free_run", cnt)
                if cnt > K: st.bad(f"{name} FBINT {cnt} > K")
                cnt = 0
            elif fbs[k]: cnt += 1
    # TAIL
    for (p0, p1) in phases:
        for t in range(p0, p1 + 1):
            if not A[t].HN or gates_into(A[t], A[t].Rbar): continue
            st.c["TAIL_starts"] += 1
            for u in range(t, p1):
                if not (A[u + 1].HN and A[u + 1].theta == A[t].theta): break
                st.c["TAIL_steps"] += 1
                if A[u].Rr < A[u + 1].Rr or not A[u + 1].Rbar <= A[u].Rbar: st.bad(f"{name} TAIL entry/growth at {u}")
                if any(A[u + 1].Xi[z] != A[t].Xi[z] for z in A[u + 1].Rbar): st.bad(f"{name} TAIL Xi on Rbar changed at {u}")

def inv(g, o, S):
    """INV(t): (i) no gate F -> Rbar; (ii) every R -> Rbar gate has level < rank(o)."""
    i_ok = not any(y in S.F and z in S.Rbar for (y, z) in S.Is)
    bad2 = [(v, z) for (v, z) in S.Is if v in S.Rr and z in S.Rbar and lev(g, S.Xi[S.sg[v]], S.Xi[z]) >= g.rank[o]]
    return i_ok, bad2

def check_nea(g, o, A, fbs, s0, s1, case, st, name):
    for t in range(s0, s1 + 1):
        S = A[t]
        if case == "A":
            st.c["SEPo_states"] += 1
            for z in S.Rbar:
                if o not in S.Xi[z][1]: st.bad(f"{name} SEPo o not in P(Xi {z}) at {t}")
            for f in S.F:
                if o in S.Xi[f][1]: st.bad(f"{name} SEPo o in P(Xi {f}) at {t}")
    for a in range(s0, s1 + 1):
        if a >= len(fbs) or not fbs[a] or A[a].tu != A[a + 1].tu: continue
        S = A[a]
        st.c[f"NEA_fallback_states_case{case}"] += 1
        i_ok, bad2 = inv(g, o, S)
        if case == "A":
            if not i_ok: st.bad(f"{name} NEA INV(i) at base {a}")
            if bad2: st.bad(f"{name} NEA INV(ii) at base {a}: {bad2[:3]}")
            st.c["NEA_base_RR_gates"] += sum(1 for (v, z) in S.Is if v in S.Rr and z in S.Rbar)
            for b in range(a + 1, s1 + 1):
                T = A[b]
                if T.theta != S.theta and MUT != "theta": break
                st.c["NEA_ab_pairs"] += 1
                i_ok, bad2 = inv(g, o, T)
                if not i_ok or bad2: st.bad(f"{name} NEA INV at {b} (base {a})")
                if A[b - 1].Rr < T.Rr or not T.Rbar <= A[b - 1].Rbar: st.bad(f"{name} NEA entry/growth at {b - 1}->{b} (base {a})")
                for z in T.Rbar:
                    if not eqv(g, o, T.Xi[z], S.Xi[z]): st.bad(f"{name} NEA value class of {z} changed (base {a}, t {b})")
                st.c["NEA_value_class_checks"] += len(T.Rbar)
                if T.Xi != A[b - 1].Xi: st.c["NEA_steps_with_Xi_change"] += 1
        else:
            # record: does INV hold in case B as well?
            if not i_ok or bad2: st.c["RECORD_caseB_INV_fails_at_fallback"] += 1
            # CASE-B-LEN and W-SIDE
            for (v, z) in S.Is:
                if not (v in S.Rr and z in S.Rbar): continue
                st.c["CASEB_RR_gates"] += 1
                sv = S.sg[v]
                if lev(g, S.Xi[sv], S.Xi[z]) != -1: st.bad(f"{name} CASEB gate {v}->{z} level {lev(g, S.Xi[sv], S.Xi[z])} at {a}")
                if not len(S.pi[z]) > len(S.pi[sv]): st.bad(f"{name} CASEB gate {v}->{z} route not longer at {a}")
                pz = S.pi[z]
                if v not in pz:
                    st.c["WSIDE_case1"] += 1
                    D = (set(pz) ^ set(S.pi[sv]))
                    D = {u for u in D if g.rank[u] > g.rank[o]}
                    if D:
                        u = max(D, key=lambda x: g.rank[x])
                        fav = (u in pz) == g.even[u]
                        if fav: st.bad(f"{name} WSIDE case1 top {u} favours z at {a}")
                        if not g.rank[u] < g.rank[S.theta[0]]: st.bad(f"{name} WSIDE case1 top above c_theta")
                    else:
                        st.c["WSIDE_case1_empty"] += 1
                        if not g.even[o]: st.bad(f"{name} WSIDE case1 empty with odd o at {a}")
                else:
                    st.c["WSIDE_case2"] += 1
                    q = pz[:pz.index(v) + 1]
                    tt = max(q, key=lambda x: g.rank[x])
                    if reward(g, tt) > reward(g, o): st.bad(f"{name} WSIDE case2 cycle node {tt} beats o at {a}")

# ---------------------------------------------------------------- (T1)-(T3)
def t123(N, seed):
    st = Stats(); rng = random.Random(seed)
    for _ in range(N):
        n = rng.randint(3, 9)
        g = RC.Game([rng.randrange(0, n + 2) for _ in range(n)], [0] * n, [[0]] * n)
        o = rng.randrange(n)
        def rv():
            c = rng.randrange(n); P = frozenset(u for u in range(n) if u != c and g.rank[u] > g.rank[c] and rng.random() < 0.5)
            return (c, P, rng.randint(0, 4))
        def near(x):
            c, P, l = x
            low = [u for u in range(n) if u != c and g.rank[c] < g.rank[u] < g.rank[o]]
            P2 = frozenset(u for u in P if g.rank[u] >= g.rank[o]) | frozenset(u for u in low if rng.random() < 0.5)
            return (c, P2, rng.randint(0, 4))
        x, y = rv(), rv()
        if rng.random() < 0.3: y = (x[0], y[1], y[2])
        x2, y2 = near(x), near(y)
        assert eqv(g, o, x, x2) and eqv(g, o, y, y2)
        if lev(g, x, y) >= g.rank[o]:
            st.c["T1_cases"] += 1
            if lev(g, x2, y2) != lev(g, x, y) or (g.cmp(x2, y2) < 0) != (g.cmp(x, y) < 0): st.bad(f"T1 {x} {y} {x2} {y2}")
        # T2: x <= y <= x' with x == x'
        a, b, c = sorted([x, x2, rv()], key=g.key)
        if eqv(g, o, a, c):
            st.c["T2_cases"] += 1
            if not eqv(g, o, a, b): st.bad(f"T2 {a} {b} {c}")
        # T3
        z = rng.randrange(n)
        if z != x[0] and z != x2[0]:
            def op(z, v): return (v[0], v[1] | ({z} if g.rank[z] > g.rank[v[0]] else set()), v[2] + 1)
            st.c["T3_cases"] += 1
            if not eqv(g, o, op(z, x), op(z, x2)): st.bad("T3")
    FC.report(st)

def main():
    args = sys.argv[1:]
    if args[0] == "t123": return t123(int(args[1]), int(args[2]))
    st = Stats()
    if args[0] == "random":
        N, nmin, nmax, seed = map(int, args[1:5]); mode = args[5] if len(args) > 5 else "own"; rng = random.Random(seed)
        for i in range(N):
            g, o = RC.rand_game(rng, rng.randint(nmin, nmax)); assert FC.odd_vertex(g) == o
            s, t = RC.rand_start(rng, g) if rng.random() < 0.7 else FC.s3_start(g)
            A, fbs = run_trace(g, o, s, t, rng, mode)
            check_run(g, o, A, fbs, st, f"{mode}:seed{seed}#{i}")
    else:
        path = args[1]; runs = int(args[2]) if len(args) > 2 else 3; mode = args[3] if len(args) > 3 else "own"
        g = RC.parse(open(path).read()); o = FC.odd_vertex(g); rng = random.Random(7)
        for r in range(runs):
            s, t = FC.s3_start(g) if r == 0 else RC.rand_start(rng, g)
            A, fbs = run_trace(g, o, s, t, rng, mode)
            check_run(g, o, A, fbs, st, f"{mode}:{os.path.basename(path)}#{r}")
    print("TRACE", args[3] if args[0] == "inst" and len(args) > 3 else (args[5] if args[0] == "random" and len(args) > 5 else "own"))
    FC.report(st)

if __name__ == "__main__":
    main()
