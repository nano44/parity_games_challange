# Draft RESULTS R48 (Lead, 2026-10-25 21:50Z by date -u; REFEREE-2's §C FBPOLY to be cited when it lands) — to CHECKER C57

### R48 [refereed-only] N5 on one-Odd-choice games: in every phase the in-phase Even fallbacks number at most 1 + (|U| − 2)(|succ(o) ∩ Û| + |U|) ≤ 1 + (n − 2)(2n − 1), with no hypothesis on H1, H2, H3, τ(o), c_w, θ or N_HN: each fallback is a Bellman-Ford round for κ on U (κ-FB-ROUND, κ-HAT-FREEZE, κ-PFZ, κ-Y-FORM), a switched vertex exits to a terminal (EXIT-SWITCH), late fallbacks switch nothing in U ∖ T (FREEZE-EXIT), the rest are one CN-LAST fallback (CN-ONLY), and θ changes few times after the freeze (THETA-AFTER) (Theorem FB-POLY) (2026-10-25) — partial step-4 lemmas for N5 (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C57.md, checker PENDING)
- Object (packet P-N5-FBPOLY, added at l-new 4a17f8e1, pinned trunk 42d8c3a9, unchanged during review): docs/new/P-N5-FBPOLY-box41.md,
  sha1 de244dcd3592b04eca2080a0efe10a7c0b2e5301 (L-NEW successor 20, Opus 5.5). It restates in κ form, with proofs, the facts of P-N5-PFZ
  §1 and P-N5-RHO §0-§2 it uses (now RESULTS R44, R45), so it does not depend on their landing. The referees' repairs and notes are
  collected by the lane in docs/new/P-N5-FBPOLY-fixes-box41.md (l-new 5e1b5ea0, sha1 c016c1906b197b41d1be35ab64ea0908f030b2ca, L-NEW
  successor 21: FBP-1 = N-FBP-2, FBP-N1, FBP-2 = N-FBP-1, FBP-N2, FBP-N3 = N-FBP-3 (scope part), FBP-N4, N-FBP-3 (data part), N-FBP-4);
  on trunk; repairs only.
  Setting as in RESULTS R39, R44 and R45 (𝒞^1O; phase; θ, c_θ; R_k, R̄_k, F_k; H1; U := λ^{-1}(c_θ), Û := U ∖ {o}; wt; G_Û; g_1 < g_2 < …
  the in-phase Even S4c fallbacks of the phase; a θ-run Θ and its in-run fallbacks f^Θ_1 < f^Θ_2 < …). T := {o, c_θ} (the TERMINALS);
  deg_U(o) := |succ(o) ∩ U|; s_θ := +1 if Ω(c_θ) is odd, −1 if even; for z ∈ U, κ_t(z) := (M_t(z), s_θ·ℓ(Ξ_t z)), ordered
  lexicographically, with M_t(z) the signed weight of P(Ξ_t z); κwt(v) := (wt(v), s_θ), κwt(A) := Σ_{v∈A} κwt(v); κoptÛ(z) :=
  max{κwt(p ∖ {c_θ}) : p a simple path of G_Û from z to c_θ}; G_U^o: the graph on U ∖ {c_θ} in which every Even v keeps its edges into
  U ∖ {c_θ}, every Odd v ≠ o keeps its forced edge if it lies in U ∖ {c_θ}, and o is a sink; G_U as in RESULTS R44. At a fallback
  k → k+1: S_k the switched Even vertices (the gate sources), x*_v := σ_{k+1}(v), S_U := S_k ∩ (U ∖ T); Y_t := succ(o) ∩ U ∩ F_t.
- Claims signed (both referees "(Opus 5.5, D15)", L37); no item uses (P); no hypothesis on H1, H2, H3, τ(o), c_w or N_HN:
  (a) Lemma κ-FB-ROUND: at an in-phase Even fallback k → k+1, κ_{k+1}(v) ≥ κwt(v) + κ_k(x) for every Even v ∈ U ∖ {c_θ} and every
      successor x ∈ U of v.
  (b) Lemma κ-HAT-FREEZE: in a phase, (a) for j ≥ 0, every state t > g_j, z ∈ Û and simple path p of G_Û from z to c_θ with ≤ j edges,
      κ_t(z) ≥ κwt(p ∖ {c_θ}); (b) for every state t and z ∈ F_t ∩ U, κoptÛ(z) is defined and κ_t(z) ≤ κoptÛ(z); (c) if |U| ≥ 2,
      κ_t(y) = κoptÛ(y) for every state t > g_{|U|−2} and every y ∈ F_t ∩ U.
  (c) Lemma κ-PFZ: if o ≠ c_θ and Θ is a θ-run of the phase, then for j ≥ 0, every t ∈ Θ with t > f^Θ_j (every t ∈ Θ if j = 0), every
      z ∈ U ∖ {c_θ} and every simple path p of G_U^o from z to o with ≤ j edges, κ_t(z) ≥ κwt(p ∖ {o}) + κ_t(o).
  (d) Lemma κ-Y-FORM: at an H1 state t, σ̄_t(o) ∈ Y_t and κ_t(o) = κwt(o) + min_{y∈Y_t} κ_t(y).
  (e) Lemma EXIT-SWITCH: at an in-phase Even fallback k → k+1 with S_U ≠ ∅, some u ∈ S_U has the property that the honest play at k
      from x*_u visits a vertex of T before it visits u; with e the first such vertex and p_u := u · (that play up to e), p_u is a
      simple path from u to e, a path of G_Û if e = c_θ and of G_U^o if e = o, and κ_k(x*_u) = κwt(p_u ∖ {u, e}) + κ_k(e). (The
      excluded "loop" branch DOES occur for some switched vertices, N-FBP-4: witness docs/referee-2/R2-N5-FBPOLY/climb/loop_4102.pg,
      sha1 016473b4, re-run by REFEREE; the lemma's "some u exits" is what holds.)
  (f) Lemma FREEZE-EXIT: if o ≠ c_θ and k = g_j is an in-phase Even fallback that is the i-th fallback of its θ-run (k = f^Θ_i), with
      j ≥ |U| − 1 and i ≥ |U| − 1, then S_U = ∅.
  (g) Lemma CN-ONLY: at an in-phase Even fallback with S_U = ∅, every gate (y, z) ∈ Iσ_k has λ_k(y) = y and lev(Ξ_k(σ_k y), Ξ_k(z)) = −1;
      hence (CN-LAST, RESULTS R38 (f)) k + 1 is the last state of its phase, and a phase has at most one such fallback.
  (h) Lemma THETA-AFTER: if o ≠ c_θ and the phase has at least |U| − 2 in-phase Even fallbacks, at most deg_U(o) + |U| − 2 of its
      transitions t → t+1 with t > g_{|U|−2} change θ, so at most deg_U(o) + |U| − 1 θ-runs of the phase contain a state t > g_{|U|−2}.
      Its proof ranges over y ∈ succ(o) ∩ Û, so it holds with |succ(o) ∩ Û| ≤ |U| − 1 in place of deg_U(o) (FBP-N1).
  (i) Theorem FB-POLY: with f the number of in-phase Even S4c fallbacks of a phase of N5 on 𝒞^1O, (a) if o ≠ c_θ, f ≤ 1 + (|U| − 2)·
      (deg_U(o) + |U|), and f ≤ 1 + (|U| − 2)(|succ(o) ∩ Û| + |U|) ≤ 1 + (n − 2)(2n − 1); (b) if |U| = 2, f ≤ 1; (c) if o = c_θ, f ≤ |U|;
      (d) at most one fallback has S_U = ∅, and it is followed by the last state of the phase. The packet's end bound used deg_U(o) ≤
      n − 1, false when o has a self-loop and succ(o) ⊇ U = V; the repair replaces deg_U(o) by |succ(o) ∩ Û| (FBP-1 = N-FBP-2, both
      referees, independently). The packet's proof of (b) covers only o ≠ c_θ; for o = c_θ and |U| = 2 the other vertex v has next(v) = o
      at every state and can never switch, so S_U = ∅ and (d) gives f ≤ 1 (FBP-2 = N-FBP-1, both referees, independently).
- Not signed (packet §7, §8, §6 Remarks): CONJECTURE FB-CAP (L-RED successor 17: f ≤ max(1, |U| − 2) in every phase), proved here only
  for |U| ≤ 2, OPEN for |U| ≥ 3, with its routes (FB-CAP-1), (FB-CAP-2) OPEN; §7's question whether EXIT-SWITCH's excluded branch can occur
  for SOME switched vertex is answered by data: it does (N-FBP-4; the packet's "never occurs in data" is out of date); the Remarks' consequences (f removed from
  SCOPE-COUNT, EPOCH, X-SN-PHASE) are READINGS (FBP-N3 = N-FBP-3).
- Honest limits: (i) SUBCLASS 𝒞^1O, inside a phase. (ii) FB-POLY bounds fallbacks per phase; S4a steps, crossings, OTHER-touching
  transitions and wakes K are not bounded here, so G-N5-TIME stays open. (iii) UNTESTED BY DATA: the hypotheses of FREEZE-EXIT and
  THETA-AFTER (a fallback g_j with j ≥ |U| − 1 at |U| ≥ 3) never occur in the data of either referee or the lane (REFEREE: 3.82 M climb
  candidates, best one fallback short; REFEREE-2: 1,484 batch logs and 1.92 M climb runs; L-RED R71), so FREEZE-EXIT, THETA-AFTER and
  FB-POLY (a) beyond FB-CAP rest on their proofs; max f per phase in data 37 (|U| 48).
- Data (DATA, not proof; one Odd choice vertex asserted on every game): REFEREE (own fbpoly_probe.py, fbpoly_climb.py on rl_engine):
  P-N5-RHO's 412-file list (253 𝒞^1O), 990 phases, 660 fallbacks (21 with S_U = ∅, 639 with S_U ≠ ∅), the packet's §8 (L) figures
  reproduced; with 4 random start pairs 5,240 phases, 1,313 fallbacks; climbs 3,822,173 candidates (2,815,066 fully checked:
  κ-HAT-FREEZE (a) 4,646,931, (c) 3,140,099, κ-PFZ 1,197,169 exact checks); 0 failures. REFEREE-2 (own fbpoly_check.py): 4,428 library
  runs and 64,000 random 𝒞^1O runs, 159,383 phases (7,357 with o = c_θ and |U| = 2, max f 1), 8,643 fallbacks, (Aκ) 3,001,987,
  κ-Y-FORM 139,928, κ-PFZ 104,199 exact checks; climbs 1,922,112 runs (31 loop-kind switched vertices); 0 violations. Lane fbpoly.py:
  (L) and 13,364 random runs, 0 failures.
- Signatures: REFEREE docs/referee/R-N5-FBPOLY.md (referee 3de7cab, successor 10; §C d6248f7b): κ-FB-ROUND, κ-HAT-FREEZE (a)-(c),
  κ-PFZ, κ-Y-FORM, EXIT-SWITCH, FREEZE-EXIT, CN-ONLY, THETA-AFTER, FB-POLY (a) first bound, (c), (d) SIGNED; FB-POLY (a) end bound
  SIGNED WITH GAP FBP-1 and (b) SIGNED WITH GAP FBP-2, each repaired in one line; in §C, with both repairs in the fixes file, FB-POLY (a)
  and (b) SIGNED without a gap; notes FBP-N1..N4. REFEREE-2 docs/referee-2/R2-N5-FBPOLY.md (referee-2 2fef7c4a, successor 11; §C
  R2C-PENDING): all SIGN, no gap; notes N-FBP-1 ((b) at o = c_θ), N-FBP-2 ((a)'s end bound with a self-loop), N-FBP-3, N-FBP-4. §C
  (REFEREE): verdicts identical in substance; FBP-1 = N-FBP-2 and FBP-2 = N-FBP-1, found independently with the same repairs; joint gap
  map one row, closed by the agreed repair; N-FBP-4 accepted and re-run.
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.
