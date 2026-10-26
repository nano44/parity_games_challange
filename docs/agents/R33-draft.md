# Draft RESULTS R33 (Lead, 2026-10-25 10:12Z by date -u) (rev. 10:27Z: C42 E-1, E-2, N-1, N-2) — to CHECKER C42 — LANDED in RESULTS Results 10:37Z (CHECKER C42 e8a1daf + Addendum 639ff523 PASS), after R32

### R33 [refereed-only] N5 on one-Odd-choice games: how (h)-runs end and restart (H3-CONST, H2-STICK), the frames at H3 states without H1 (Lemma G′), the freeze through ¬H1 states (FREEZE′), R̄ constant at ¬H1 states (R-CONST), the single empty-path interval (H1-INT), and crossings per fallback-free run without an H1 hypothesis (Theorem X-RUN′) (2026-10-25) — partial step-4 lemmas for N5 (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C42.md, checker PENDING)
- Object (packet P-N5-L2, added at l-new 1afccb5, pinned trunk 04b3f48, unchanged during review): docs/new/P-N5-L2-box34.md, sha1
  cbea07392521bcdfbce137ba361bb581f9df11d7 (L-NEW successor 14, Opus 5.5). The referees' repairs are collected by the lane in
  docs/new/P-N5-L2-fixes-box34.md (l-new 97c3b4e, sha1 7a110bca8d52b532d531c0836547b2d22b7437cd, L-NEW successor 15: L2-1, L2-2) and
  docs/new/P-N5-L2-fixes2-box34.md (l-new ea78e9b, sha1 e343d74e1502e7c75ca5c40fd79350a3b8662b26, L-NEW successor 15: N-L2-1 = L2-1;
  N-L2-2 as Lemma X-RUN°: any set of consecutive (h) states of one fallback-free run has ≤ 13(d_o+1)n³ crossing transitions with both
  ends in it); both on trunk; repairs only.
  Setting as in RESULTS R30-R32 (𝒞^1O; phase with λ_Ξ and τ constant; R, R̄, F, θ, w, c_θ, c_w, H1-H3, (h), r, SN prefix, windows,
  FREEZE, X-RUN). U := λ^{-1}(c_θ) (a phase constant). An H1-TOGGLE is a transition at which H1 changes.
- Claims signed (both referees "(Opus 5.5, D15)", L37):
  (a) Lemma H3-CONST: in a phase, at every H2 state c_w = λ(τ(o)); so H3 holds at all H2 states of the phase or at none, and if the
      phase has an (h) state, then (h) ⟺ H1 ∧ H2 at every state of the phase.
  (b) Lemma H2-STICK: at an S4a transition s → s+1 of a phase with H1 and ¬H2 at s, ¬H2 holds at s+1 (the case τ(o) = o, where
      "τ(o) ∈ R_s" is false since R excludes o, is trivial: L2-1 = N-L2-1, wording, closed).
  (c) Lemma G′: at a phase state with H3 and ¬H1 (c := c_θ = c_w): ¬H2 holds and c ∈ R̄; a vertex of R̄ whose (σ, τ)-play visits c
      before o has Ξ = W; any other has Ξ = π_v ⊕ θ and W = π_v ⊕ w, with π_v disjoint from P(θ), P(w) and c.
  (d) Theorem FREEZE′ (premise RESULTS R32 FREEZE, with FRZ-1, FRZ-2): FREEZE holds with "(h)" replaced by "H3" in the window and "H2"
      replaced by "H2 or H3" in the conclusion (b) and in the range of t.
  (e) Lemma R-CONST: at every ¬H1 state of a phase, R̄ = U; so no transition between two ¬H1 states of a phase is a crossing.
  (f) Lemma H1-INT: in a phase, the states with P(θ) = ∅ form one interval I_∅; every ¬H1 state lies in I_∅, and so does every state k
      such that k → k+1 is a transition of the phase with H1 at k and ¬H1 at k+1 (the packet's reading with k+1 outside the phase is
      FALSE: docs/referee/R-N5-L2/exitdrop_n3.pg, sha1 73c7a21b…, n 3; L2-2, wording, closed); on I_∅, θ changes only in length,
      monotonically, at most n − 1 times.
  (g) Theorem X-RUN′ (premise RESULTS R32 X-RUN, with FRZ-3): for a fallback-free run Q of a phase with SN prefix P and t_Q H1-toggles
      with both ends in P, P has ≤ 13(d_o + 1)n³(t_Q + 1) + t_Q crossing transitions with both ends in P, and REL_Q ≤ d_o(C + 1) with C
      that number; no hypothesis on H1. X-RUN's proof uses only "consecutive (h) states of one fallback-free run" (N-L2-2, accepted by
      REFEREE; Lemma X-RUN° in fixes2).
- Refuted (§8, not signed; lane and referee instances, each re-run by the Lead: n5, Oink zlk OK strategies verified, one Odd choice
  vertex): CONJECTURE ONE-H ("the (h) states of a phase are consecutive") FALSE, experiments/new/box34/instances/oneh_cex_n32.pg (sha1
  51dab086…); CONJECTURE ONE-DROP ("≤ 1 H1 → ¬H1 transition per phase") FALSE, experiments/new/box34/instances/onedrop_cex_n32.pg
  (5793d5a3…, n5 6/1); CONJECTURE DROP-LEN ("θ changes between two drops of a phase") FALSE, docs/referee/R-N5-L2/droplen_cex_n12.pg
  (REFEREE; a6af26db…, n 12, n5 4/0, one phase, θ constant, drops at 1→2 and 3→4); its weaker form "≤ 1 drop per fallback-free run"
  FALSE, experiments/new/box35/instances/onerun_cex_n32.pg (L-NEW successor 15; 70832fcb…, n5 8/0). The open item "(h) restarted by a
  fallback at an H1 ∧ ¬H2 state that moves τ(o) out of R" OCCURS: experiments/new/box35/instances/fbrestart_cex_n12.pg (35223b6c…, n5
  5/2) and fbrestart_cex_n24.pg (a0aacfba…, 23/3) (L-NEW successor 15, SPEC trace); REFEREE-2 also saw it with its own N5 (j5_n16).
- Honest limits: (i) SUBCLASS 𝒞^1O, inside a phase. (ii) FREEZE′ and X-RUN′ rest on R32. (iii) X-RUN′ is per fallback-free run and
  in terms of t_Q; the H1-toggle count, f per phase, (L1) and fallbacks outside scope runs are OPEN here, so G-N5-TIME stays open.
  (iv) DATA is thin for FREEZE′'s new content: no n-state H3 window containing a ¬H1 state with a later state of its phase was found by
  either referee (REFEREE-2's climbs reached 668,549 such windows at n ≤ 10, all ending at the phase end; REFEREE's FIT=frz climbs (random starts and three library seeds)
  reached none). (v) Lane work after the pin (P-N5-TOG, CN-LAST, box 36) is not part of the claims; its box-35 instances appear only as
  DATA under Refuted.
- Data (DATA, not proof; one Odd choice vertex asserted on every game): REFEREE l2_probe.py and companions (own code): library 258
  files (319 phases, 7,155 states) and random 30,000 + 15,000 games, 0 failures of §1-§7; P^c_ℓ on windows containing ¬H1 states:
  library 491 windows / 2,097 checks, random 267,221 windows / 641,105 checks, 0 failures. REFEREE-2 (own code): 27,444 batch runs and
  6 climbs (2,416,844 runs), 0 violations; G′ frames checked per vertex at H3 ∧ ¬H1 states; P^c_ℓ on H3 windows with ¬H1 states about
  17 M path comparisons (11.3 M exhaustive).
- Signatures: REFEREE docs/referee/R-N5-L2.md (referee 7626354, successor 7; addenda 524d93f (climbs), d3ccb9c (fixes 7a110bca
  checked); §C ce24106 + 0363a7b): H3-CONST, G′, FREEZE′, R-CONST, X-RUN′ SIGNED; H2-STICK SIGNED WITH GAP L2-1; H1-INT SIGNED WITH GAP
  L2-2; both closed. REFEREE-2 docs/referee-2/R2-N5-L2.md (referee-2 388caf6, successor 7; §C 21429c9): H3-CONST, H2-STICK
  (N-L2-1), G′, FREEZE′, R-CONST, H1-INT, X-RUN′ (N-L2-2) SIGN; notes N-L2-1..3; in §C adopts REFEREE's labels and accepts L2-2 (missed).
  §C: no verdict differs. Joint gap map (REFEREE §C, REFEREE-2 §C), 4 rows: L2-1 = N-L2-1 (wording, closed); L2-2 (wording, closed;
  REFEREE only); N-L2-2 (X-RUN°, accepted); N-L2-3 (DATA thin, FREEZE′).
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.
