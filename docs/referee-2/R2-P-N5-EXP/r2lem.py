#!/usr/bin/env python3
"""REFEREE-2 successor 42: own checker for Addendum 2 of R2-P-N5-EXP.md (fixes-file check of P-N5-EXP; the L41 cross-check of
LEMMA′, CAUSAL and STABLE in step form as printed in docs/red-b/P-N5-EXP-fixes.md entry 4 at claude/l-red-b 24f4d436). r2exp.py
lineage: the genome is r2exp.build (written from §3's TABLE), the model is r2unit217.M1P (= R104's IDEAL model, R2-key-preread
Addendum 3). Nothing of the lane is imported; docs/referee/ was not read when this file was written.

Objects (entry 4.1's standing assumptions). State: every wire and u_0 at option 0. Φ(s) = s⁺ := the IDEAL step's s′, defined at
EVERY state (s′(x) := the key-least element of A_s(x), level by level; s⁺ = s iff the run stops at s, by «opt» or by «stuck»).
For a start σ: S[τ] := Φ^τ(σ) (constant after the stop); reach[τ] := «the run reaches s_τ» = [S[i] ≠ S[i − 1] for 1 ≤ i ≤ τ].
C_j(s), E_j(s): the MODEL'S OWN key / value comparison of v_j against u_j (never a formula). U_j: the movers of the units j..k − 1.
sched(j, a): the move list of a response of unit j from rest a, written from the frozen cases (i), (ii): offset → set of (mover,
new option) over U_j.

Statements, each evaluated as «hypothesis ⇒ conclusion» exactly as printed:
  FROZEN   the RESPONSE LEMMA of the frozen packet (350d84eb l. 192-204): (H1) under s_(t−1); (H2) the input is (c, c) under s_τ
           for every τ in [t, t + P_j − 1] THAT THE RUN REACHES; conclusion: the run reaches the last step, the listed moves, the
           E(j) clause, the rest states.
  PREFIX   my lane's form (R2-P-N5-EXP.md §2.4) at every cut τ_0 in [t, last]: (H1); C_(j−1)(S[τ]) = c for t ≤ τ ≤ τ_0 (S[τ] =
           (s_(τ−1))⁺); E_(j−1)(S[τ]) = c for t ≤ τ ≤ τ_0 − 1; conclusion: reach[τ_0] and the listed moves in the steps t..τ_0.
  LEMMA′   entry 4.4 at every horizon T in [t − 1, last]: the run reaches s_(t−1), (H1), and (H2′_T) WITH ITS GUARDS: for t ≤ τ ≤ T,
           if reach[τ − 1] then C_(j−1)((s_(τ−1))⁺) = c; for t ≤ τ ≤ T − 1, if reach[τ] then E_(j−1)(s_τ) = c. Conclusion (R1) the
           moves of U_j in the steps t..T are the list's, (R2) reach[T] (so every step changes a mover), and for T = last (R3):
           s_τ(E(j)) = a for t − 1 ≤ τ < last, E(j) at c under s_last (j ≥ 2), REST_j(c) and REST_i(0), i > j, under s_last.
  STABLE   entry 4.2: REST_i(b) under s, E_(i−1)(s) = b, C_(i−1)(s⁺) = b ⇒ s⁺ = s on unit i; «hence» REST_i(b) under s⁺, C_i(s⁺) =
           0, E_i(s) = 0; «consequently», with REST_m(0) under s for every m > i, s⁺ = s on U_i.
  CAUSAL   entry 4.3: s⁺ on U_j is a function of (s on U_j, E_(j−1)(s), C_(j−1)(s⁺)).
Universes:
  U1  the run of G_k from the packet's start: every triple (j, a, t), 1 ≤ t ≤ 2^k, at which the run reaches s_(t−1).
  U2  EVERY state σ that satisfies (H1) for (j, a) — exhaustive over the part below U_j when it has at most 2^CAP states, else
      SAMPLE random lower parts — taken as s_(t−1) with t = 1 (the genome with another start column; the proofs use only MOVE-2,
      V1-V4, K1-K4, which hold at every state). This is where truncated inputs occur on real trajectories.
  U3  DRIVEN inputs (not a run of G_k): from the run's s_(t−1) at a window of the recursion, the part below U_j is disturbed by
      hand at a random step and after; U_j must follow the list for as long as the two bits it reads are (c, a), then (c, c).
  causal: every state at k = 3, 4 (2^9, 2^16); for larger k random states that share large parts.
Counters (must 0):
  tfail             the run does not stop at exactly 2^k − 2
  pre_u1, pre_u2    PREFIX fails at a cut (hypothesis true, conclusion false)
  lp_u1, lp_u2      LEMMA′ fails at a horizon ((H2′_T) true, (R1) or (R2) false); r3_u1, r3_u2: (R3) fails at T = last
  conc_u1, conc_u2  the concordance «PREFIX at τ_0 = LEMMA′ at T = τ_0»: at some T ≥ t the two hypotheses differ in truth, or both
                    hold and the two conclusions ((R1) ∧ (R2) on LEMMA′'s side) differ
  lp_corner         at a triple where FROZEN fails, (H2′_T) holds for some T ≥ t (entry 4.4's Remark 1 says it never does)
  stab_u1, stab_u2, stab_hence, stab_cons   STABLE: its first sentence, its «hence» clause, its «consequently» clause
  causal            two states with the same triple (s on U_j, E_(j−1)(s), C_(j−1)(s⁺)) have different s⁺ on U_j
  standing          s⁺ has a wire or u_0 off option 0, or C_0(s) ≠ s(v_0), or E_0(s) ≠ s(v_0) (entry 4.1 (S1))
  drive             U3: a step whose two input bits are as the hypothesis says moves U_j otherwise than the list
  frozen_noncorner  FROZEN fails at a triple whose (H2) window holds at least one reached state (i.e. NOT by vacuity)
CONTROL that must fire: frozen_fail (FROZEN fails; on U1 the triples are printed) and frozen_at_111 = 1 per k (it fails at (j, a,
t) = (1, 1, 2^k − 1)). INFO: the numbers of true hypotheses (h1_*, cuts_*, lp_hyp_*, r3_hyp_*, stab_hyp_*, stab_cons_hyp), how
each (H1) triple's input ends (full / trunc_C / trunc_E / none), the longest proper prefix (maxproper_*), causal classes and hits.
Controls (--ctrl NAME): sched (the list shifted by one step: pre, lp, drive), noE (the input hypotheses without their E half:
pre_u2, lp_u2: the E half is needed), noC (without their C half: also conc and lp_corner fire: without the key clause the guards
matter), late (the conclusion demanded one step beyond the cut: pre_u2, lp_u2, drive: the cut is tight), stab (STABLE without
C_(i−1)(s⁺) = b), causalE / causalC (CAUSAL's triple without one input bit), unit (U_(j+1) with the inputs of unit j).
Usage: r2lem.py [--ctrl NAME] [--cap BITS] [--sample COUNT] [--tries COUNT] [--u1only | --u2only | --u3only | --causalonly] K..."""
import sys, os, random
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [HERE, os.path.join(HERE, "..", "R2-key"), os.path.join(HERE, "..", "R2-P-N5-END")]
import r2exp as X
import r2unit217 as U


class Ctx:
    def __init__(self, k):
        self.k = k; G, names, ix, _ = X.build(k); self.G, self.names, self.ix = G, names, ix
        self.m = U.M1P(G); self.N = G["N"]; self.P = {k - 1: 3}
        for j in range(k - 2, 0, -1): self.P[j] = 2 * self.P[j + 1] + 1
        self.u = [ix[f"u{j}"] for j in range(k)]; self.v = [ix[f"v{j}"] for j in range(k)]
        self.unit = {}
        for j in range(1, k):
            mem = [f"u{j}", f"v{j}", f"y{j}", f"yb{j}"] + ([f"e{j}", f"yp{j}", f"ypb{j}"] if 2 <= j <= k - 2 else [])
            self.unit[j] = [ix[n] for n in mem]
        self.upper = {j: sorted(x for i in range(j, k) for x in self.unit[i]) for j in range(1, k + 1)}
        self.wires = [ix[n] for n in names if n[0] == "w"]
        self.Ef = {j: ix[f"e{j}"] if j <= k - 2 else ix[f"u{j}"] for j in range(2, k)}       # the END-FOLLOWER E(j)
        self.cache = {}; self.rel = {}; self.pcache = {}

    def phi(self, s):
        r = self.pcache.get(s)
        if r is None:
            r = self.m.step(s)
            if r is None: r = s
            if len(self.pcache) < 300000: self.pcache[s] = r
        return r

    def bits(self, s):
        r = self.cache.get(s)
        if r is None:
            mu, _ = self.m.keys(s); _, Xv = self.m.vals(s)
            C = tuple(int(mu[self.v[j]] < mu[self.u[j]]) for j in range(self.k))
            E = tuple(int(Xv[(self.v[j], s[self.v[j]])] > Xv[(self.u[j], s[self.u[j]])]) for j in range(self.k))
            r = (C, E)
            if len(self.cache) < 300000: self.cache[s] = r
        return r

    def Cb(self, s, j): return self.bits(s)[0][j]
    def Eb(self, s, j): return self.bits(s)[1][j]
    def inp(self, s, j): b = self.bits(s); return (b[0][j - 1], b[1][j - 1])

    def rest(self, s, j, a):
        ix = self.ix
        ok = s[ix[f"u{j}"]] == a and s[ix[f"v{j}"]] == a and (s[ix[f"y{j}"]], s[ix[f"yb{j}"]]) == (a, 1 - a)
        if 2 <= j <= self.k - 2:
            ok = ok and s[ix[f"e{j}"]] == a and (s[ix[f"yp{j}"]], s[ix[f"ypb{j}"]]) == (a, 1 - a)
        return ok

    def h1(self, s, j, a):
        return self.rest(s, j, a) and all(self.rest(s, i, 0) for i in range(j + 1, self.k)) and self.inp(s, j) == (a, a)

    def last_off(self, j):                    # offset of the last step of a response of unit j (step t + last_off)
        return self.P[j] - 1 if j >= 2 else self.P[1] - 2

    def sched(self, j, a):
        """the lemma's move list of a response (j, a): list over offsets 0..last_off of frozensets of (mover, new option)"""
        r = self.rel.get((j, a))
        if r is not None: return r
        k, ix, P = self.k, self.ix, self.P; c = 1 - a; n = self.last_off(j) + 1; mv = [set() for _ in range(n)]
        F, B = (f"yb{j}", f"y{j}") if a == 0 else (f"y{j}", f"yb{j}")
        if j == k - 1:                                                     # case (i)
            mv[0].add((ix[f"v{j}"], c)); mv[1].add((ix[B], 1)); mv[2].add((ix[f"u{j}"], c)); mv[2].add((ix[F], 0))
        else:                                                              # case (ii)
            o1 = P[j + 1] - 1; o2 = o1 + P[j + 1]                          # t_1 − t, t_2 − t
            mv[0].add((ix[f"v{j}"], c)); mv[1].add((ix[F], 0)); mv[o1].add((ix[B], 1)); mv[o1 + 1].add((ix[f"u{j}"], c))
            for off, a2 in ((0, 0), (o1 + 1, 1)):                          # the two responses of unit j + 1: from rest 0, then from rest 1
                sub = self.sched(j + 1, a2); assert len(sub) == P[j + 1]
                for i, st in enumerate(sub): mv[off + i] |= st
            if j >= 2:
                Fp, Bp = (f"ypb{j}", f"yp{j}") if a == 0 else (f"yp{j}", f"ypb{j}")
                mv[o1 + 1].add((ix[Fp], 0)); mv[o2].add((ix[Bp], 1)); mv[o2 + 1].add((ix[f"e{j}"], c)); assert o2 + 1 == n - 1
            else: assert o2 == n - 1
        r = self.rel[(j, a)] = [frozenset(x) for x in mv]
        return r

    def moved(self, S, tau, j):               # the moves of the units ≥ j in the step S[τ − 1] → S[τ]
        p, q = S[tau - 1], S[tau]
        return frozenset((x, q[x]) for x in self.upper[j] if q[x] != p[x])

    def traj(self, sigma, n):
        S = [sigma]; reach = [True]
        for _ in range(n):
            S.append(self.phi(S[-1])); reach.append(reach[-1] and S[-1] != S[-2])
        return S, reach


def frozen(cx, S, reach, j, a, t):
    """the RESPONSE LEMMA as frozen: (hypothesis, conclusion, number of reached states in (H2)'s window)"""
    c = 1 - a; P = cx.P
    if not reach[t - 1] or not cx.h1(S[t - 1], j, a): return (False, None, 0)
    win = [tau for tau in range(t, t + P[j]) if reach[tau]]
    if not all(cx.inp(S[tau], j) == (c, c) for tau in win): return (False, None, len(win))
    last = t + cx.last_off(j); sc = cx.sched(j, a)
    ok = reach[last] and all(cx.moved(S, tau, j) == sc[tau - t] for tau in range(t, last + 1))
    if ok and j >= 2:
        e = cx.Ef[j]; ok = all(S[tau][e] == a for tau in range(t - 1, last)) and S[last][e] == c
    ok = ok and cx.rest(S[last], j, c) and all(cx.rest(S[last], i, 0) for i in range(j + 1, cx.k))
    return (True, ok, len(win))


def window(cx, S, reach, j, a, t, ctrl, C, tag):
    """one triple (j, a, t) at which the run reaches s_(t−1) and (H1) holds: PREFIX at every cut τ_0 in [t, last], LEMMA′ at every
    horizon T in [t − 1, last], and their concordance at τ_0 = T. One pass; every clause is evaluated as printed (the guards of
    (H2′_T) included), nothing is inferred from an earlier cut."""
    c = 1 - a; last = t + cx.last_off(j); sc = cx.sched(j, a); sh = 1 if ctrl == "sched" else 0
    Cok = lambda tau: ctrl == "noC" or cx.Cb(S[tau], j - 1) == c            # C_(j−1)((s_(τ−1))⁺) = c: S[τ] = Φ(S[τ − 1])
    Eok = lambda tau: ctrl == "noE" or cx.Eb(S[tau], j - 1) == c            # E_(j−1)(s_τ) = c
    Mok = lambda tau: cx.moved(S, tau, j) == (sc[tau - t + sh] if tau - t + sh < len(sc) else frozenset())
    C["lp_hyp_" + tag] += 1                                                 # LEMMA′ at T = t − 1: nothing to show (reach[t − 1] is given)
    ph = True; pc = True                                                    # PREFIX: hypothesis and conclusion, running over τ_0
    lh = True; lc = True                                                    # LEMMA′: (H2′_T) and (R1) ∧ (R2), running over T
    tau0 = t - 1; why = ""; mok = {}
    for T in range(t, last + 1):
        mok[T] = Mok(T)
        if ph:                                                              # (H2[τ_0]): C at t..τ_0, E at t..τ_0 − 1
            if not Cok(T): ph = False; why = "C"
            elif T - 1 >= t and not Eok(T - 1): ph = False; why = "E"
        if ph: tau0 = T
        pc = pc and reach[T] and mok[T]
        if lh:                                                              # (H2′_T), with its guards «if the run reaches»
            if reach[T - 1] and not Cok(T): lh = False
            elif T - 1 >= t and reach[T - 1] and not Eok(T - 1): lh = False
        lc = lc and reach[T] and mok[T]
        end = min(T + 1, last) if ctrl == "late" else T
        pcc = pc and (ctrl != "late" or (reach[end] and Mok(end))); lcc = lc and (ctrl != "late" or (reach[end] and Mok(end)))
        if ph:
            C["cuts_" + tag] += 1
            if not pcc: C["pre_" + tag] += 1
        if lh:
            C["lp_hyp_" + tag] += 1
            if not lcc: C["lp_" + tag] += 1
            if T == last:                                                   # (R3)
                r3 = cx.rest(S[last], j, c) and all(cx.rest(S[last], i, 0) for i in range(j + 1, cx.k))
                if j >= 2:
                    e = cx.Ef[j]; r3 = r3 and all(S[tau][e] == a for tau in range(t - 1, last)) and S[last][e] == c
                C["r3_hyp_" + tag] += 1
                if not r3: C["r3_" + tag] += 1
        if (ph, pcc if ph else None) != (lh, lcc if lh else None): C["conc_" + tag] += 1
    kind = "full" if tau0 == last else "none" if tau0 == t - 1 else "trunc_" + why
    C[tag + "_" + kind] += 1
    if kind.startswith("trunc"): C["maxproper_" + tag] = max(C["maxproper_" + tag], tau0 - t + 1)
    return tau0


def stable_step(cx, p, q, C, tag, ctrl=""):
    """STABLE in step form (4.2) at the step p → q = p⁺, every unit i and bit b"""
    k = cx.k
    for i in range(1, k):
        for b in (0, 1):
            if not (cx.rest(p, i, b) and cx.Eb(p, i - 1) == b and (ctrl == "stab" or cx.Cb(q, i - 1) == b)): continue
            C["stab_hyp_" + tag] += 1
            if any(q[x] != p[x] for x in cx.unit[i]): C["stab_" + tag] += 1; continue
            if not (cx.rest(q, i, b) and cx.Cb(q, i) == 0 and cx.Eb(p, i) == 0): C["stab_hence"] += 1       # «hence REST_i(b) under s⁺, C_i(s⁺) = 0 and E_i(s) = 0»
            if all(cx.rest(p, m, 0) for m in range(i + 1, k)):                                            # «Consequently … s⁺ = s on U_i»
                C["stab_cons_hyp"] += 1
                if any(q[x] != p[x] for x in cx.upper[i]): C["stab_cons"] += 1


def u1(cx, C, ctrl, lp):
    k = cx.k; T = 2 ** k - 2; S, reach = cx.traj(tuple(cx.G["start"]), T + cx.P[1] + 6)
    if not (reach[T] and not reach[T + 1]): C["tfail"] += 1
    fz = []
    for t in range(1, T + 3):
        for j in range(1, k):
            for a in (0, 1):
                C["triples_u1"] += 1
                if not reach[t - 1] or not cx.h1(S[t - 1], j, a): continue
                C["h1_u1"] += 1
                h, ok, nwin = frozen(cx, S, reach, j, a, t)
                if h:
                    C["frozen_hyp_u1"] += 1
                    if not ok:
                        C["frozen_fail"] += 1; fz.append((j, a, t))
                        if nwin > 0: C["frozen_noncorner"] += 1
                before = C["lp_hyp_u1"]; window(cx, S, reach, j, a, t, ctrl, C, "u1")
                if h and not ok and C["lp_hyp_u1"] - before != 1: C["lp_corner"] += 1   # at a triple where FROZEN fails, (H2′_T) must fail for every T ≥ t
        stable_step(cx, S[t - 1], S[t], C, "u1", ctrl)
    if (1, 1, T + 1) in fz: C["frozen_at_111"] += 1
    return fz


def h1_states(cx, j, a, cap, sample, rng):
    """the states σ (wires and u_0 at 0) with REST_j(a), REST_i(0) for i > j; the lower part free (all of it, or a sample)"""
    N = cx.N; fixed = set(cx.wires) | {cx.ix["u0"]} | set(cx.upper[j]); free = [x for x in range(N) if x not in fixed]
    base = [0] * N; ix = cx.ix
    for i in range(j, cx.k):
        b = a if i == j else 0
        for n in (f"u{i}", f"v{i}", f"y{i}"): base[ix[n]] = b
        base[ix[f"yb{i}"]] = 1 - b
        if 2 <= i <= cx.k - 2:
            base[ix[f"e{i}"]] = b; base[ix[f"yp{i}"]] = b; base[ix[f"ypb{i}"]] = 1 - b
    if len(free) <= cap:
        for bitsv in range(2 ** len(free)):
            s = list(base)
            for i, x in enumerate(free): s[x] = (bitsv >> i) & 1
            yield tuple(s), True
    else:
        for _ in range(sample):
            s = list(base)
            for x in free: s[x] = rng.randrange(2)
            yield tuple(s), False


def u2(cx, C, ctrl, lp, cap, sample):
    k = cx.k; rng = random.Random(4200 + k)
    for j in range(1, k):
        for a in (0, 1):
            for sigma, exh in h1_states(cx, j, a, cap, sample, rng):
                C["u2_states_exh" if exh else "u2_states_rnd"] += 1
                if cx.inp(sigma, j) != (a, a): continue
                C["h1_u2"] += 1; t = 1; S, reach = cx.traj(sigma, cx.P[j] + 2)
                h, ok, nwin = frozen(cx, S, reach, j, a, t)
                if h and not ok:
                    C["frozen_fail_u2"] += 1
                    if nwin > 0: C["frozen_noncorner"] += 1
                window(cx, S, reach, j, a, t, ctrl, C, "u2")
                for tau in range(1, min(len(S) - 1, cx.P[j] + 1) + 1): stable_step(cx, S[tau - 1], S[tau], C, "u2", ctrl)


def u3(cx, C, ctrl, tries):
    """DRIVEN inputs (not a run of G_k): from the run's own s_(t−1) at a window (j, a, t), z_τ := (z′_(τ−1))⁺ where z′ is z with 1-3
    movers BELOW unit j flipped (never a wire, u_0 or a mover of U_j) at a random step d of the window and after it at every step
    with probability 0.2. The inputs of step τ are C_(j−1)(z_τ) and E_(j−1)(z′_(τ−1)); while they are (c, a) at τ = t and (c, c)
    after, the moves of U_j must be the list's. Tests CAUSAL and the list together, with long proper prefixes."""
    k = cx.k; T = 2 ** k - 2; S, reach = cx.traj(tuple(cx.G["start"]), T + 2); rng = random.Random(9100 + k)
    wins = [(j, a, t) for t in range(1, T + 1) for j in range(1, k) for a in (0, 1)
            if cx.rest(S[t - 1], j, a) and cx.h1(S[t - 1], j, a) and cx.Cb(S[t], j - 1) == 1 - a]
    sh = 1 if ctrl == "sched" else 0
    for _ in range(tries):
        j, a, t = rng.choice(wins); c = 1 - a; last = t + cx.last_off(j); sc = cx.sched(j, a)
        low = [x for x in range(cx.N) if x not in cx.wires and x != cx.ix["u0"] and x not in set(cx.upper[j])]
        d = rng.randint(t, last); z = S[t - 1]; good = 0; C["u3_windows"] += 1
        for tau in range(t, last + 1):
            zp = list(z)
            if tau == d or (tau > d and rng.random() < 0.2):
                for x in rng.sample(low, min(len(low), rng.randint(1, 3))): zp[x] = 1 - zp[x]
            zp = tuple(zp); q = cx.phi(zp)
            okin = cx.Cb(q, j - 1) == c and cx.Eb(zp, j - 1) == (a if tau == t else c)
            if ctrl == "late" and not okin and tau > t: okin = True; C["u3_late"] += 1
            if not okin: break
            C["u3_steps"] += 1; good += 1
            mv = frozenset((x, q[x]) for x in cx.upper[j] if q[x] != zp[x])
            if mv != (sc[tau - t + sh] if tau - t + sh < len(sc) else frozenset()): C["drive"] += 1
            z = q
        if good == last - t + 1: C["u3_full"] += 1
        else: C["u3_proper"] += 1; C["maxproper_u3"] = max(C["maxproper_u3"], good)


def causal(cx, C, ctrl, cap, sample):
    """CAUSAL (4.3): Φ(s) on U_j is a function of (s on U_j, E_(j−1)(s), C_(j−1)(Φ(s)))"""
    k = cx.k; N = cx.N; rng = random.Random(7700 + k); fixed = set(cx.wires) | {cx.ix["u0"]}; free = [x for x in range(N) if x not in fixed]
    if len(free) <= cap:
        def gen():
            for bitsv in range(2 ** len(free)):
                s = [0] * N
                for i, x in enumerate(free): s[x] = (bitsv >> i) & 1
                yield tuple(s)
        states = gen(); C["causal_exh"] += 1
    else:
        def gen():                      # states that share large parts: a random state, then 7 variants with about half of its movers redrawn
            for _ in range(sample // 8):
                up = [rng.randrange(2) for _ in range(N)]
                for _ in range(8):
                    s = list(up)
                    for x in free:
                        if rng.random() < 0.5: s[x] = rng.randrange(2)
                    for x in fixed: s[x] = 0
                    yield tuple(s)
        states = gen()
    seen = {j: {} for j in range(1, k)}
    for s in states:
        q = cx.m.step(s); q = s if q is None else q; C["causal_states"] += 1
        Cq = cx.bits(q)[0]; Es = cx.bits(s)[1]
        if any(q[x] != 0 for x in fixed): C["standing"] += 1               # (S1): s⁺ again has every wire and u_0 at 0
        if Cq[0] != q[cx.ix["v0"]] or Es[0] != s[cx.ix["v0"]]: C["standing"] += 1   # C_0(s) = E_0(s) = s(v_0) under (S1)
        for j in range(1, k):
            up = cx.upper[j + 1] if ctrl == "unit" else cx.upper[j]
            key = (tuple(s[x] for x in up), None if ctrl == "causalE" else Es[j - 1], None if ctrl == "causalC" else Cq[j - 1])
            img = tuple(q[x] for x in up); old = seen[j].get(key)
            if old is None: seen[j][key] = img
            elif old != img: C["causal"] += 1
            else: C["causal_hits"] += 1
    C["causal_classes"] += sum(len(d) for d in seen.values())


MUST0 = ["tfail", "pre_u1", "pre_u2", "lp_u1", "lp_u2", "r3_u1", "r3_u2", "conc_u1", "conc_u2", "lp_corner", "stab_u1", "stab_u2", "stab_hence",
         "stab_cons", "causal", "standing", "drive", "frozen_noncorner"]
INFO = ["frozen_fail", "frozen_at_111", "frozen_fail_u2", "frozen_hyp_u1", "triples_u1", "h1_u1", "u1_full", "u1_trunc_C", "u1_trunc_E", "u1_none", "cuts_u1",
        "lp_hyp_u1", "r3_hyp_u1", "stab_hyp_u1", "u2_states_exh", "u2_states_rnd", "h1_u2", "u2_full", "u2_trunc_C", "u2_trunc_E", "u2_none",
        "maxproper_u2", "cuts_u2", "lp_hyp_u2", "r3_hyp_u2", "stab_hyp_u2", "stab_cons_hyp", "u3_windows", "u3_full", "u3_proper", "maxproper_u3",
        "u3_steps", "u3_late", "causal_exh", "causal_states", "causal_classes", "causal_hits"]


def main(a):
    ctrl = ""; cap = 14; sample = 4000; tries = 2000; ks = []; i = 0
    only = [x for x in a if x in ("--u1only", "--u2only", "--u3only", "--causalonly")]; a = [x for x in a if x not in only]
    while i < len(a):
        if a[i] == "--ctrl": ctrl = a[i + 1]; i += 2
        elif a[i] == "--cap": cap = int(a[i + 1]); i += 2
        elif a[i] == "--sample": sample = int(a[i + 1]); i += 2
        elif a[i] == "--tries": tries = int(a[i + 1]); i += 2
        else: ks.append(int(a[i])); i += 1
    C = defaultdict(int)
    for k in ks:
        cx = Ctx(k); before = dict(C); fz = []
        if not only or "--u1only" in only: fz = u1(cx, C, ctrl, True)
        if not only or "--u2only" in only: u2(cx, C, ctrl, True, cap, sample)
        if not only or "--u3only" in only: u3(cx, C, ctrl, tries)
        if not only or "--causalonly" in only: causal(cx, C, ctrl, cap + 2, sample * 4)
        d = lambda c: C[c] - before.get(c, 0)
        print(f"k {k} N {cx.N} T {2 ** k - 2} | must0: " + (" ".join(f"{c} {d(c)}" for c in MUST0 if d(c)) or "all 0")
              + " | " + " ".join(f"{c} {C[c] if c.startswith('maxproper') else d(c)}" for c in INFO if d(c)) + (f" | FROZEN fails at (j, a, t) = {fz}" if fz else ""), flush=True)
    print(f"TOTAL ctrl {ctrl or '-'}: " + " ".join(f"{c} {C[c]}" for c in MUST0))
    print("INFO " + " ".join(f"{c} {C[c]}" for c in INFO))
    print("FIRED " + (" ".join(c for c in MUST0 if C[c]) or "none"))


if __name__ == "__main__":
    main(sys.argv[1:])
