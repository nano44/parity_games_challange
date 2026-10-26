# Draft RESULTS R62 (Lead, 2026-10-26 06:28Z by date -u; both §Cs and the fixes file filled) (rev. 2026-10-26 06:44Z: limit (iii) added after L-SI finding) (rev. 2026-10-26 07:04Z: C71 E-1, E-2, N-1, N-2) (rev. 2026-10-26 07:25Z: C71 E-3, N-3) — to CHECKER C71 — LANDED in RESULTS Results 2026-10-26 07:47Z (CHECKER C71 Add. 3 2a5da1ac PASS), after R64

### R62 [refereed-only] N5 on EVERY game: R55's factorisation holds under (NC) "no disagreement vertex on its own cycle" (G_D-NC), every vertex has the cycle nodes of its first disagreement vertex so terminal changes stay inside one honest class (TC-CLASS), the honest and W-valuations agree in coarse form above M_D under (h3_D) alone (C2-H3), W never drops at an in-phase S4a step (WM-G), and on every fallback-free in-phase run with (h3_D) throughout the coarse values freeze from state k_0 + n − 1 on (P^c_L, CR-D, FRZ-U_H3) (2026-10-26) — structural lemmas for N5 beyond one Odd choice vertex (no count; not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C71.md, checker PENDING)
- Object (packet P-N5-H3, added at l-si 10b11167, pinned trunk d096e404, unchanged during review): docs/si/P-N5-H3-box16.md, sha1
  680e45287aed82ea3d9ac05ed9decdf9c260e849 (L-SI successor 11, Opus 5.5). It supersedes P-N5-NC (sha1 2036e7c8, l-si eeb08be7), WITHDRAWN
  unreviewed by the Lead (REFEREE-2's report on it, 4d54b6a5, is VOID by its author, 9a482c93). The referees' notes are collected by the lane
  in docs/si/P-N5-H3-fixes-box16.md (l-si beb1e803, sha1 5666b4a5f71fabbf10cdd3b5bba796acdcdf6240, L-SI successor 12: H3-N4 = N-H3-6,
  H3-N2 = N-H3-4, N-H3-1, H3-N1, N-H3-2 / N-H3-3, data); on trunk; repairs only, no signed statement changes.
  Setting (every game): as in RESULTS R55 (state k = (σ_k, τ_k); σ̄_k; Ξ_k; G_τ; W_k; λ_Ξ, λ_W; D_k; u(v); R_D, F_D; π_v; (h_D); (h3_D);
  lev, COARSE_L, (C2), (C4) of RESULTS R25; M_D, ⊥ if D_k = ∅). (NC) at k: no vertex of D_k lies on its own honest cycle, and none lies on
  its own W-cycle; (h_D) implies (NC). A run S: consecutive states k_0, …, k_1 inside one phase, all of whose transitions are S4a steps (no
  fallback); Ω_k := W_k, the valuation of σ_k in the fixed one-player game G_τ; COARSE := COARSE_L for a level −1 ≤ L < ∞.
- Claims signed (both referees "(Opus 5.5, D15)", L37), on every game; no item uses (P); premises LANDED: RESULTS R55 (a), (b) (its proof,
  whose one use of (h_D) is replaced), R17 (a) (F1), R25 (C1)-(C4), R38 (a), SPEC S1, S4a; WM-G rests on the standing SPEC premise that S1
  returns the arena optimum, as 1E-N3 in RESULTS R57 (H3-N1, REFEREE; a landing note):
  (a) Lemma G_D-NC (b′): under (NC) at k, for v ∈ R_D with u := u(v), Ξ_k(v) = π_v ⊕ Ξ_k(u) and W_k(v) = π_v ⊕ W_k(u), and the honest and the
      W-play from u avoid π_v. R55 (b)'s proof uses (h_D) exactly once, and (NC) closes that step (N-H3-2 = REFEREE §1).
  (b) Lemma TC-CLASS (no hypothesis): at every state k and for every v ∈ R_D, λ_Ξ(v) = λ_Ξ(u(v)) and λ_W(v) = λ_W(u(v)); hence inside a phase,
      if v ∈ R_D at k and at k + 1 and u_k(v) ≠ u_{k+1}(v), then λ_Ξ(u_k(v)) = λ_Ξ(v) = λ_Ξ(u_{k+1}(v)).
  (c) Lemma C2-H3: if (h3_D) holds at k and M_D ≤ L < ∞, L ≥ −1 (L = −1 when M_D = ⊥), then COARSE_L(Ξ_k(v)) = COARSE_L(W_k(v)) for every v;
      no (h_D) and no (NC). The path set above the common cycle node factors through u(v) by the lasso fact (N-H3-3 = REFEREE §3).
  (d) Lemma WM-G: for every transition k → k+1 of a run S, Ω_{k+1} ⊵ Ω_k pointwise.
  (e) Lemma P^c_L and Lemma CR-D: if at every state of S (i) COARSE(Ξ_k(v)) = COARSE(W_k(v)) for every v and (ii) the map v ↦ λ_W(v) is the
      same, then COARSE(Ω_t) = COARSE(Ω_{k_0+n−1}) for every t ∈ S with t ≥ k_0 + n − 1 (Lemma P^c_L: for every j with k_0 + j ∈ S and every
      simple path r of G_τ from x to a W-cycle node u with at most j edges, Ω^c_{k_0+j}(x) ⪰ COARSE(value(r))). CR-D's statement is L-SI
      successor 10's (docs/si/N5-FRONTIER-box15.md §2, l-si 0bd6fb23); the proof is written out in the packet. In P^c_L's case B1 with x on
      c′'s W-cycle, the new cycle is simple because π meets the old arc only at c′ (π's part on the cycle and the arc c′ → x are disjoint,
      since x ∉ π): a sentence the packet omits (H3-N2 = N-H3-4, found independently by both referees).
  (f) Corollary FRZ-U_H3: on a run S inside one phase with (h3_D) at every state, for max_S M_D ≤ L < ∞, L ≥ −1, COARSE_L(W) = COARSE_L(Ξ)
      on V at every state of S, and it is constant on S FROM STATE k_0 + n − 1 ON. This is the 0-based reading, which the proof gives (P^c_L
      at k_0 + j covers paths with ≤ j edges, and simple paths have ≤ n − 1 edges); the packet's §0 phrase "(n − 1)-th state" is read so, a
      non-vacuous check needs a run of ≥ n + 1 states, and the stronger 1-based reading is NOT signed (H3-N4 = N-H3-6, both referees and the
      author). Scope: any number and any cycle configuration of the disagreement vertices (¬(h_D) by routing or by a gate on its own cycle).
- Not signed (packet §7, §8): ¬(h3_D) (M_D = ∞; on 𝒞^1O this is R50's ¬H3 case, which needs kinds); the fine route order below L inside
  one honest class with two or more disagreement vertices (Δ-RT; on 𝒞^1O R50's LEN), which by TC-CLASS is the only place where terminals
  can change; R55's Wo_D, not ported; the data. The packet's quotes of R55's proof and of (C1)-(C4) are content-verbatim, with joined
  bullets and some parentheticals dropped without "…" (N-H3-1, accepted by REFEREE).
- Honest limits: (i) Structural lemmas: they bound no count. (ii) The freeze is exercised only on runs of ≥ n + 1 states: lib41 3 runs,
  L-COMP's frz1_n24 and frz3_n24 (frz3_n24 also run by REFEREE-2, Addendum A 9a5692ad); pftheta34_n32 (L-RED) (all in the (h_D) regime or (NC) ∧ ¬(h_D)), and REFEREE-2's constructed witness
  pft34_h3u_P32 (¬(NC) at every state, (h3_D) holding; a disjoint union, so the cycling disagreement vertex is decoupled from the
  freezing part), re-run by REFEREE on its engine; natural freezes with ¬(NC) are not reached. Both referees' first freeze counts included
  vacuous n-state runs; both corrected them in addenda (REFEREE ead5fdb3, REFEREE-2 d449d72b).
  (iii) Content (DATA, L-SI successor 12, experiments/si/rund/rel.py, l-si d61b3cf0): on frz1_n24, frz3_n24,
  pftheta34_n32 and pft34_h3u_P32 the level max_S M_D is the top rank, and no W path set at any state of the run has a vertex above it;
  so on every long run known the frozen COARSE_L(W) is only the cycle node, and the freeze there is non-vacuous by length but
  content-free by level (it says nothing beyond hypothesis (ii)). Confirmed by REFEREE Addendum B (e18b4370; all its non-vacuous
  freezes, the 3 lib41 runs included) and REFEREE-2 Addendum A (9a5692ad). The signed statements are unaffected.
- Data (DATA, not proof): REFEREE (successor 12, own engine, random starts and given start pairs): 29,174 runs, 0 failures; C2-H3 1.22M
  checks, 5,773 states with (h3_D) ∧ ¬(NC); (b′) 153k checks; TC-CLASS 528 terminal changes (the sum of its logs, as its §C C.3 states), all inside one class; WM-G 679k checks;
  mutation (L = M_D − 1) fails 76,353 times. REFEREE-2 (successor 14, own h3_check.py reusing its NC checker; lane code not run): 0
  violations; C2-H3 201,701 checks at (h3_D) ∧ ¬(NC) states; TC-CLASS 1,664 in-phase terminal changes, none across classes; mutations c2l,
  b0, pc1, crd1 bite. L-COMP (independent checker; not a referee check): C2-H3 151,611 checks, 10,487 at ¬(NC) states, on the library frontier (l-comp
  56d42105), and 1,131,485 checks, 115,640 at ¬(NC) states, on 50,000 random runs (l-comp 785c38d3), 0 violations.
- Signatures: REFEREE docs/referee/R-N5-H3.md (referee 7c2d9b49, successor 12; Addendum A ead5fdb3; §C 6b17eb58; Addendum B e18b4370): all SIGNED; notes
  H3-N1..N4; no gap. REFEREE-2 docs/referee-2/R2-N5-H3.md (referee-2 5b251bed, N-H3-6 d449d72b, §C b7b04fad + 723909be, Addendum A 9a5692ad, successor 14): all
  SIGN; notes N-H3-1..6; no gap. §C (both): verdicts identical, FRZ-U_H3 signed in the 0-based reading; joint gap map empty; H3-N2 = N-H3-4;
  N-H3-1 accepted by REFEREE (partly missed by it); H3-N1, H3-N4 REFEREE's; nothing open.
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (structural; no running time). GAPS G-N5-TIME: open.
