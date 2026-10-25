# Draft RESULTS R29 (Lead, 2026-10-25 03:16Z by date -u) — awaits CHECKER C38; lands in "## Results" after R28, before "## Dead ends"

### R29 [refereed-only] N5 on one-Odd-choice games: gates into F never exceed the gate level (OFFGATE), cycle-node switches are length-only (CN), values off R̄ freeze at S4a steps above a gap (NL), and fallback levels never rise along a scope run at THR fallbacks (Theorem CLS1) (2026-10-25) — partial step-4 lemmas for N5 (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C38.md, checker PENDING)
- Object (packet P-N5-CLS, pinned trunk 486107a, unchanged during review): docs/si/P-N5-CLS-box8.md, sha1
  5bbfd872383d9b2c2d3caaf902b174d0aa54e4ae (L-SI successor 3, Opus 5.5). The referees' repairs are collected by the lane in
  docs/si/P-N5-CLS-fixes-box8.md (l-si 2c5e57c, on trunk; sha1 92f79dc98628159a1ef328b76a1672851eb0dda1, L-SI successor 3; a record, not
  itself refereed text; it holds CLS-1..CLS-4 and N-CLS-1; the wording row N-CLS-2 is in both referees' §C only).
  Setting: N5 as in RESULTS R25 (gates, gate levels, M_k, lev, COARSE_L, (C1)-(C4), Ξ_k = Θ_{H_k}, ENG-1). PHASE: a joint λ-phase with
  τ constant. On 𝒞^1O, R, R̄ := R ∪ {o}, F, (h), EQ / THR, u* as in R19-R23. SCOPE RUN: a maximal run of consecutive in-phase transitions
  k → k+1 with (h) at k, H2 at k+1 and w_{k+1} = w_k. r_k := lev(θ_k, w_k) (< ∞ under (h)).
- Claims signed (both referees "(Opus 5.5, D15)", L37):
  (a) Elementary facts (C5) (a ◁ b ⊴ c ⇒ lev(a, b) ≤ lev(a, c)), (C6) (lev(a, c) ≤ max(lev(a, b), lev(b, c))), (C7) (a prefix disjoint
      from both path sets and cycle nodes preserves lev and order); Fact R (r is non-increasing along a scope run); Lemma CLU (at an
      in-phase S4c fallback k with (h) and θ_k ◁ w_k, every switched y → z with y ∈ R_k, z ∈ F_k has level ≤ r_k; re-proved from R23 (f)).
  (b) Lemma TRANSFER (every game): for an in-phase k → k+1, L < ∞ and z with COARSE_L(Ξ_{k+1} z) = COARSE_L(Ξ_k z), a gate (y, z) at
      k+1 of level > L is a gate at k of level > L.
  (c) Lemma OFFGATE (𝒞^1O): at every in-phase transition, tame or not, every gate (y, z) at k+1 with z ∉ R̄_{k+1} has level ≤ M_k. (M_k ≥ −1
      at every in-phase transition, since no gate means σ unchanged and so τ changes: CLS-1, wording; R̄ is R25 OFF's honest
      reachability, equal to the (σ, τ) one on 𝒞^1O: N-CLS-1.)
  (d) Lemma CN (every game, inside a phase): if λ_{k+1} = λ_k and an Even y with λ_k(y) = y switches to z, the gate level of (y, z) at k
      is −1 (CLS-2, wording).
  (e) Lemma NL (𝒞^1O): at an S4a transition j → j+1 inside a phase with (h) at j, L < ∞, r_j > L and (A_j) (every gate at j into F_j has
      level ≤ L): (i) COARSE_L(Ξ) is unchanged on every v ∉ R̄_{j+1}; (ii) R_j ⊆ R̄_{j+1} (no leave); (iii) (A_{j+1}) holds.
  (f) Theorem CLS1 (𝒞^1O): in a scope run S, at an S4c fallback k1 at a THR state with r_{k1} ≥ 0 (u* ≠ none),
      M_{k1} ≤ min{M_k : k < k1 an S4c fallback of S}. Its case r_{k1} ≤ L uses FBL in its u* ≠ none strong gate form at the single state
      k1 (no F → R and no R → R gate edge; R-N5-XA §3, R2-N5-XA §2), not "a single fallback state is a stretch of length 1"
      (CLS-3 = G-CLS-1, citation, closed); every in-scope fallback is THR or EQ, since under (h) θ = w ⟺ EQ (N-CLS-2, wording).
      Corollary: along a scope run, the levels of its THR fallbacks with u* ≠ none are non-increasing; these are all its fallbacks
      before the first EQ / u* = none state (Fact R) ("evicting" dropped: CLS-4, wording).
- Refuted (both referees, own code): OG′ "gates into F at k+1 have level ≤ MF_k (the max level of the gates at k into F_k)" is FALSE:
  experiments/red/xing/instances/x31_re24.pg (sha1 49eaf50e…), transition 1 → 2, an S4a step: MF_1 = −1, gate (4, 8) at state 2 of level
  22 into F, |R| 21 → 1; OFFGATE holds there (M_1 = 23). REFEREE found 17 more violations in random games. The data counter MF_up in the
  lane's cls2.py is this OG′ counter, not a rise of a fallback level.
- Honest limits: (i) TRANSFER, CN and (C5)-(C7) hold on every game; Fact R, CLU, OFFGATE, NL, CLS1 are on 𝒞^1O. (ii) CLS1 bounds the
  levels, not the number, of fallbacks per scope run: the per-level count ("≤ n_E fallbacks per level") is OPEN, as are fallbacks at EQ
  states or with u* = none ((H-EQ)) and θ-changes per scope run without X; G-N5-TIME stays open. (iii) No fallback with u* = none occurs in
  any data, so CLS1's (β) case rests on Fact R alone; CN has few library cases (48; 711 random). (iv) Random games are nearly vacuous for
  CLS1 (≤ 1 fallback per scope run); the evidence is the named set, the library and REFEREE-2's climbs.
- Data (DATA, not proof; one Odd choice vertex asserted on every game): REFEREE cls_probe.py (own trace = n5.run, phase key
  (λ_Ξ, λ_U, τ)): named 65 / library 234 / random 5,500 games, 0 failures of every check; its named counts equal the packet's §8
  (OFFGATE 6,645; CN 7; 70 scope runs; in-scope fallbacks 252 THR u* ≠ none / 4 EQ / 0 u* = none); no rise of M at any in-scope
  fallback (named 256, library 534). REFEREE-2 (own code): 234 files × 3 starts + 12,000 random + 12,400 climb runs, 913 in-scope
  fallbacks (890 THR u* ≠ none, 23 EQ, 0 u* = none), 0 failures; TRANSFER 442,864, OFFGATE 26,464, CLU 1,948 checks; NL tested at every
  admissible L (40,516 library + 20,283 climb checks); CLS1's case r > L 678 library comparisons with (A_j) asserted at all 1,731
  intermediate states, + 20,544 in climbs. Lead re-ran experiments/si/coarse/run_cls.sh: the packet's logs regenerate byte-identically.
- Signatures: REFEREE docs/referee/R-N5-CLS.md (referee a0b92ec; §C 8af6347): (C5)-(C7), Fact R, CLU, TRANSFER, NL SIGNED; OFFGATE
  SIGNED WITH GAP CLS-1; CN SIGNED WITH GAP CLS-2; CLS1 SIGNED WITH GAP CLS-3 (closed); Corollary SIGNED WITH GAP CLS-4; OG′ FALSE
  confirmed. REFEREE-2 docs/referee-2/R2-N5-CLS.md (referee-2 ffe10e1; §C 848839e): (C5)-(C7), Fact R, CLU, TRANSFER, CN, NL SIGN; OFFGATE
  SIGN (N-CLS-1); CLS1 + Corollary SIGN WITH GAPS G-CLS-1 (closed), N-CLS-2; OG′ refutation reproduced. §C: no verdict differs. Joint
  gap map (REFEREE §C, REFEREE-2 §C): CLS-3 = G-CLS-1 (closed, REFEREE-2's form adopted); CLS-1, CLS-2, CLS-4, N-CLS-1, N-CLS-2 (wording).
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.
