# Draft RESULTS R21 (Lead, 2026-10-24 18:5xZ by date -u) (rev.: REFEREE §C 865eadd; rev. 19:10Z: C30 E-1..E-4, N-1) — awaits CHECKER C30 Addendum 1; lands in "## Results" after R20, before "## Dead ends"

### R21 [refereed-only] N5 on one-Odd-choice games: inside one joint λ-phase, transitions are bounded by crossings and OTHER states (Theorem X), with Lemmas XW, EQ, FBL-N, NF, F1, F2, FB-W, and a clarification of R19 (f) (2026-10-24) — partial step-4 lemmas for N5 on a subclass (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C30.md, checker PENDING)
- Object (packet P-N5-X, pinned trunk afc88b0, unchanged during review): docs/new/P-N5-X-box28.md, sha1
  b21d2d0638d08d750f26ae4dda2faaca7891fa23 (L-NEW successor 10, Opus 5.5). The referees' repairs are collected by the lane in
  docs/new/P-N5-X-fixes-box29.md (l-new 331ad0c, on trunk; sha1 dd467be05462b17ef5744d4e1019afeada95588c, L-NEW successor 10; a record of
  the reports, not itself refereed text).
  Setting as in R19 (𝒞^1O, θ, w, R, (h)). A PHASE is a joint λ-phase with τ constant. F := V \ R. A CROSSING transition changes R.
  State types: EQ (Ξ = W pointwise), THR ((h) and Ξ ≠ W), OTHER ((h) fails and Ξ ≠ W); an OTHER-touching transition has an OTHER
  endpoint. VALUE-CHANGING: Ξ or W changes at some vertex.
- Claims signed (both referees "(Opus 5.5, D15)", L37):
  (a) Lemma XW: Ξ_k ⊴ W_k pointwise at every state (Odd's best reply σ̄_k is pointwise optimal in G_{σ_k}).
  (b) Lemma EQ: a run of consecutive EQ states inside one phase has ≤ n − 1 value-changing transitions; (h) not assumed.
  (c) Lemma FBL-N: at an S4c fallback with τ unchanged, (i) it is Even's and σ_k is a pointwise arena optimum in G_τ; (ii) every gate
      edge from F is flat for W; (iii) if H2 fails, no gate edge goes from F to R.
  (d) Lemma NF: a value-changing S4c fallback inside a phase with neither endpoint OTHER is a crossing.
  (e) Lemma F1: on an F-interval (a maximal run of a phase with no crossing and no OTHER-touching transition; F constant), Ξ changes
      on F at ≤ max(0, |F| − 1) transitions (X-2); w, θ and (h) at EQ states never enter (step 2 needs only Lemma G (a), N-X-1).
  (f) Lemma F2: inside an F-interval, an EQ → THR transition changes Ξ(τ(o)), and at a THR → THR transition a w-change is a change of
      Ξ(τ(o)).
  (g) Theorem X: inside one phase, with X := #crossing transitions and O := #OTHER-touching transitions, the phase has at most
      (3n²(1 + X + O) + X + O + 1)(4n(n − 1) + 1) = O(n⁴(1 + X + O)) transitions. Step 4 uses PIECE (R19 (f)) with θ free in the form
      of item (i) below (X-1 = G-X-1), and re-derives "flat fallbacks pass PIECE" from NF outside u* ≠ none stretches instead of citing
      R20 (f) (X-4 = N-X-3). (FBRE-F) is not used.
  (h) Lemma FB-W, given the CR row of the (w, u*)-run table: in a (w, u*)-run, a vertex evicted by a fallback at L ≥ k_0 + n − 1 to a
      target with w's status at u* never re-enters R in that run. (DATA vacuous: 0 qualifying evictions in REFEREE-2's sample.)
  (i) Clarification of R19 (f) (landed text frozen; docs/agents/R19-note-X1.md): R19 (f) holds with θ free in this form: the R-part
      bound counts route (𝓡*, i.e. W on R) changes; a θ-change at a transition with H1 at its start and R constant changes W on F
      (REFEREE X-1, via Lemma S (a) and R15 (a); REFEREE-2 Lemma TF as a second proof) and is charged to the F-part; the total
      (|R| − 1) + (|F| − 1) counts transitions at which Ξ or W changes. Read with Ξ on R counted in the R-part, the per-part bound fails
      with θ varying (fbref_n48, transition 56 → 57, R = {o}). (Wording: REFEREE-2 §C.4; REFEREE §C3 confirms its content.) A
      POST-LANDING NOTE under R19 points here.
- Also checked, not a claim: the (w, u*)-run table (which R20 lemmas survive θ-changes: all except FBF), checked by both as a READING.
- Consequence (READING, not signed): with Lemma Φ (≤ 2n(n − 1) + 1 joint λ-phases; box 21, PROVED by the lane, UNREFEREED) and
  τ-changes ≤ d − 1 (R15 (c) on G^d, checked by REFEREE), N5 on o-cyclic 𝒞^1O is polynomial if (X) and (NH') hold: X and O are poly(n)
  per phase.
- Honest limits: (i) SUBCLASS 𝒞^1O, polynomial by other means; a bound on N5 itself. (ii) Theorem X moves the open part of G-N5-TIME on
  𝒞^1O to two counts, and both exceed n in data: X = 54 at n 32 and 70 at n 48 (L-NEW climbs, Lead re-run); O = 11 at n 10 (L-COMP
  experiments/n5-exhaustive/instances/b5_o11.pg, l-comp 67471f7b, on trunk; sha1 db4fe55a…; Lead re-run) and 19 at n 24 (L-NEW). (X) and (NH') are OPEN; no growth law beyond linear is established either way.
  (iii) The phase count (Lemma Φ) is unrefereed. (iv) (FBRE-F) is FALSE (L-RED fbref_cex_n32; L-NEW fbref_n48); not used here.
- Data (DATA, not proof): REFEREE x_probe.py: 42 named instances + 8,731 random runs, 1,947 phases (max length 110, X up to 70, O up to
  19), 0 failures of XW, NF (121), F1 (1,592 intervals), F2 (33), EQ (1,464 blocks), sub-block ≤ n − 2 (136), θ-change ⇒ F-change (176),
  or the Theorem X bound. REFEREE-2 x_check.py (own code): 15,378 runs, 37,235 phases, 3,558 F-intervals, 753 sub-blocks (211 with θ
  varying), 1,735 (w, u*)-runs, 0 violations of any packet statement; the per-part R19 (f) reading with Ξ on R fails in 111 sub-blocks
  (item (i)). Lane eqcheck.py: 0 failures (Lead re-run, seed 2832, 1,296 runs).
- Signatures: REFEREE docs/referee/R-N5-X.md (referee 53c0c68; §C 865eadd): F1 SIGNED WITH GAPS (X-2); NF SIGNED WITH GAPS (X-3);
  Theorem X SIGNED WITH GAPS, all closed (X-1 closed in §3.2, X-4 valid as re-derivation); XW, EQ, FBL-N, F2, FB-W SIGNED; table
  checked as a READING; §C: no disagreement of substance, N-X-2 accepted, X-1 and TF equivalent, its "R19 (f) as landed TRUE" withdrawn for the wording, item (i) wording confirmed (precision: R_{k+1} = R_k, (h) at k suffices). REFEREE-2 docs/referee-2/R2-N5-X.md (referee-2 059f492; §C 3a581a5): F1, NF SIGN; Theorem X SIGN WITH GAPS
  (G-X-1 closed by Lemma TF); XW, EQ, FBL-N, F2, FB-W SIGN; table agreed; §C: no disagreement, X-2 and X-3 accepted, X-1 accepted as a
  substitute for TF, item (i) wording proposed. Joint gap map: X-1 = G-X-1 (closed); X-2, X-3 wording; X-4 = N-X-3 (re-derivation);
  N-X-1 = REFEREE §1 remark; N-X-2 = REFEREE §3.3 R19 (b) row. Nothing open in the packet.
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.
