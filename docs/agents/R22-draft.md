# Draft RESULTS R22 (Lead, 2026-10-24 20:1xZ by date -u) — awaits REFEREE-2 §C on R2-N5-NH, then CHECKER C31; lands in "## Results" after R21, before "## Dead ends"

### R22 [refereed-only] N5 on one-Odd-choice games: crossing-free intervals with OTHER states (F1°), the clauses of (h) on them (TC), and route frames with the honest cycle node higher (P3′) (2026-10-24) — partial step-4 lemmas for N5 on a subclass (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C31.md, checker PENDING)
- Object (packet P-N5-NH, pinned trunk c7981ee, unchanged during review): docs/new/P-N5-NH-box30.md, sha1
  382c514300fe056d5d95b836f359b78b1374eabe (L-NEW successor 10, Opus 5.5). The referees' repairs are collected by the lane in
  docs/new/P-N5-NH-fixes-box30.md (l-new b4fc3a4, on trunk; sha1 2d7e366a2e9782d98ff1598c6eb460af8f46ac57, L-NEW successor 11; a record
  of the reports, not itself refereed text).
  Setting as in R21 (𝒞^1O; a PHASE is a joint λ-phase with τ constant; R, F := V \ R; (h) = H1 ∧ H2 ∧ H3; EQ / THR / OTHER). A
  CROSSING-FREE INTERVAL I is a maximal run of states of a phase with R constant.
- Claims signed (both referees "(Opus 5.5, D15)", L37):
  (a) Lemma F1°: on a crossing-free interval I, OTHER states included, Ξ changes at some vertex of F at ≤ max(0, |F| − 1) transitions
      (R21 (e) extended; FBL-N (ii) and Lemma G (a) need no (h)).
  (b) Lemma TC: on a crossing-free interval I, (i) H1 ⟺ λ_Ξ(o) ∈ F and H2 ⟺ τ(o) ∈ F, both constant on I; (ii) under H2, λ_W(o) =
      λ_Ξ(τ(o)) is fixed in the phase, so H3 and (h) are constant on I, and I is all OTHER or has no OTHER state; (iii) under H1 ∧ ¬H2,
      every state of I is OTHER; (iv) under ¬H1 ∧ ¬H2, a state of I is EQ iff θ = w, and every EQ → OTHER transition inside I changes w.
  (c) Lemma P3′: let J ⊆ I be a (θ, w)-piece (both frames in route form: honest by H1 or λ_Ξ(o) = o, W by H2 or λ_W(o) = o; θ, w
      constant) with c_θ = λ_Ξ(o) strictly more relevant than c_w = λ_W(o). Then the transitions of J with a Ξ-change at some vertex of
      R number at most (n + 1)|R| (REFEREE: also ≤ |R| + (|R| − 2)(|R| − 1)). Step 1 (coarse freeze, R20 (d) CR run on the route game
      𝓡*_w) uses only B1's single-switch inequality at κ-strict cases, proved directly by both referees; the packet's sentence "S4a's
      optimum restricted to R is an optimum of 𝓡*_w's arena" is UNPROVED under ¬H2 with λ_W(o) = o, not refuted, and not needed
      (P3-1 = G-NH-1; for x on o's W-cycle a κ-strict edge would move x's W cycle node off o inside J, so that case is vacuous).
  (d) Corollary: under H2 on I, I has ≤ max(1, |F|) pieces (θ via R21 (i) / X-1, w via R19 (b) under H2, F1°).
- Reduction (READING, checked by both referees, not signed): inside one phase, the transitions number at most
  poly(n) · (1 + X + Σ_I (ROI(I) + WC(I))), with X = crossings, ROI(I) = R-only value-changing transitions in OTHER blocks of I, WC(I) =
  w-changes in I under ¬H1 ∧ ¬H2 (the ≤ 2(1 + WC(I)) OTHER-block boundary transitions are counted, NH-1 = N-NH-3; an R-only W-change
  raises Ξ on R by (SG), NH-2). With R21, N5 on o-cyclic 𝒞^1O is polynomial if X, ROI and WC are poly(n) per phase. P3′ bounds ROI on
  its pieces.
- Honest limits: (i) SUBCLASS 𝒞^1O; a bound on N5 itself. (ii) Open: (X); ROI outside P3′'s case, i.e. U1 (route form, c_w higher), U2
  (honest frame not in route form), U3 (W frame not in route form); W-CYC. CONJECTURES (OB), (OB_R), (NFB-O), (U1-T) (L-NEW, data only);
  WF0 FALSE (wf0_cex_n16). (iii) P3′'s data is thin: REFEREE 901 qualifying pieces, longest 6 transitions; REFEREE-2 1,017 nontrivial
  pieces from climbs, 1,871 S4a steps under ¬H2 with 0 mismatches. P3′ rests on the proof. (iv) DATA on O (not signed): L-COMP's chain
  of whole-OTHER phases reaches O = 77 at n 40 (≈ 2n; pattern 23, crossings + F-changes + R-only ≤ |R|; Lead re-run).
- Data (DATA, not proof): REFEREE nh_probe.py: ~100 named instances + 8,784 random runs, 20,840 crossing-free intervals, 0 failures of
  F1°, TC, the Corollary (11,213 intervals) or (SG) (6,942). REFEREE-2 nh_check.py (own code): 12,064 runs, 34,842 crossing-free
  intervals (184 with OTHER states), 39,250 TC state checks, 151,926 (R1) checks, 0 violations.
- Signatures: REFEREE docs/referee/R-N5-NH.md (referee 78d61b1; §C 68e314c): P3′ step 1 SIGNED WITH GAP P3-1 (closed by vacuity), step 2
  and count SIGNED, Corollary SIGNED, TC SIGNED, F1° SIGNED, reduction checked (NH-1, NH-2); §C: no verdict differs, P3-1 = G-NH-1 (same
  argument, each a substitute), N-NH-2 accepted, R2's §1.3 W ⇔ Ξ remark should cite (SG). REFEREE-2 docs/referee-2/R2-N5-NH.md
  (referee-2 48da84a; §C PENDING): P3′ step 1 SIGN WITH GAPS (G-NH-1, closed by a direct single-switch proof), steps 2-3 SIGN, Corollary
  SIGN, TC SIGN, F1° SIGN, reduction correct as a READING (N-NH-1..3). Joint gap map: P3-1 = G-NH-1 (CLOSED); NH-1 = N-NH-3 (wording);
  NH-2 ((SG) step); N-NH-1 (cite X-1 / R21 (i)); N-NH-2 (THR remark needs (h)).
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.
