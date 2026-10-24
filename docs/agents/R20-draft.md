# Draft RESULTS R20 (Lead, 2026-10-24 16:32Z by date -u) — awaits CHECKER C29; lands in "## Results" after R19, before "## Dead ends"

### R20 [refereed-only] N5 on one-Odd-choice games, throttled stretches with a top difference (u* ≠ none): coarse monotonicity (C), fallbacks only evict (FBL), no entry after a fallback (FBF), coarse R17 (CR), strict re-entry (XA), and O(n³) value changes per stretch (2026-10-24) — partial step-4 lemmas for N5 on a subclass (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C29.md, checker PENDING)
- Object (packet P-N5-XA, pinned trunk b70aa59, unchanged during review): docs/new/P-N5-XA-box27.md, sha1
  832d0da2b45bcc0850929b0f614bb1d9b19ed7b3 (L-NEW successor 9, Opus 5.5). The referees' repairs are collected by the lane in
  docs/new/P-N5-XA-fixes-box28.md (sha1 a7022bf5…, L-NEW successor 10; a record of the reports, not itself refereed text).
  Setting as in R19 (𝒞^1O, θ, w, R, (h)); a throttled stretch S: τ, joint λ-phase, θ, w constant, θ ◁ w, (h) at every state of S;
  u* := the most relevant vertex of P(θ) Δ P(w); COARSE(v) := (cycle node, path vertices more relevant than u*).
- Claims signed (both referees "(Opus 5.5, D15)", L37):
  (a) Lemma C: in S, COARSE(Ξ) = COARSE(W) at every vertex, and it is non-decreasing along S, fallbacks included.
  (b) Lemma FBL, FOR u* ≠ none only, in the strong form: at a throttled S4c fallback state there is no F→R and no R→R gate edge, so
      the fallback switches only leaves (R→F edges), apart from flat cycle-node switches. For u* = none FBL is UNPROVED (a switched
      F→R edge whose target's route leaves R in the same fallback is not excluded; no instance known; G-XA-1 (b), found by REFEREE-2,
      accepted by REFEREE).
  (c) Lemma FBF, for every u*: after a throttled fallback at L, for the rest of S no vertex enters R and no vertex in R changes its
      route (base: c ∉ R_t on S, REFEREE-2; inductive step: best-key choice of S4c, REFEREE).
  (d) Lemma CR: R17's Lemma P / Theorem PH transcribed to the coarse order (B1/B2 in full; the omitted case "P(π) = ∅, c′ even,
      shorter" (XA-3) and Odd vertices in Case A (XA-4) added); coarse values change only in the first n − 1 transitions of S. CR does
      not depend on FBL: the fallback case is vacuous (N-XA-1).
  (e) Theorem XA: a re-entry into R after an arena (non-fallback) leave inside S is a strict coarse increase; ≤ n − 1 such re-entries
      per vertex (N-XA-2), ≤ n(n − 1) per stretch.
  (f) Corollary, for u* ≠ none with (h) at every state of S: pieces (PIECE, R19 (f)) pass through value-flat fallbacks (σ_{k+1} is
      another optimum of the arena; REFEREE §C5 = REFEREE-2 §C.5/§C2.2), hence S has O(n³) crossings, non-flat fallbacks and
      value-changing transitions, and O(n⁵) transitions in all (value-preserving runs ≤ 4n(n−1), R15 (d), N-XA-3).
- Honest limits: (i) SUBCLASS 𝒞^1O, polynomial by other means; a bound on N5 itself. (ii) This bounds ONE throttled stretch with
  u* ≠ none. Open for G-N5-TIME on 𝒞^1O: the number of (θ, w)-stretches per joint λ-phase ((CYC'): θ- and w-changes; climbs reach 43
  θ-changes in one phase at n 32, linear so far), non-(h) transitions ((NH)), stretches with u* = none, and FBL for u* = none. (iii)
  "Value-changing" in (f): the lane's fixes file §6 defines it as "Ξ or W changes" (a crossing can change Ξ with W flat); that
  definition is the lane's, not checked by a referee; inside a piece the two readings coincide. (iv) No data for (e): 0 re-entries
  inside throttled stretches in every sample (lane, both referees); the claim rests on the proof.
- Data (DATA, not proof): REFEREE xa_probe.py: 25 named instances + 26,483 random runs, 43 throttled stretches, 41 throttled fallbacks
  (all u* ≠ none), 151 post-fallback states, 0 failures of C, coarse monotonicity, CR, FBL, FBF; random samples nearly vacuous (~1
  throttled stretch per 1,000 runs). REFEREE-2 xa_check.py (own code): 16,672 runs, 707 throttled stretches (longest 56), 576 fallbacks
  in S, 921 switched edges (all leaves), 0 violations; piece_flatfb.py: 1,052 pieces, 64 with a flat fallback, 0 violations (weak: 10
  value-changing steps in those 64).
- Signatures: REFEREE docs/referee/R-N5-XA.md (referee f39972d; §C 1123baf): C SIGNED; FBL SIGNED for u* ≠ none, unproved for
  u* = none; FBF SIGNED WITH GAPS (closed); CR SIGNED; XA SIGNED; Corollary closed by §C5 pending REFEREE-2. REFEREE-2
  docs/referee-2/R2-N5-XA.md (referee-2 9d3f1fb; §C 4df15e6; §C2 38af0df): §1, C, FBF, CR, XA SIGN; FBL SIGN WITH GAPS (u* = none
  unproved); Corollary SIGNED in §C2 for u* ≠ none via §C5. Joint gap map: XA-1 = G-XA-1 (a), (b) REFEREE-2 only (accepted); XA-2 =
  G-XA-2 (closed); XA-3, XA-4 wording (accepted by REFEREE-2); XA-5 closed by §C5 (both); N-XA-1..3 accepted.
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.
