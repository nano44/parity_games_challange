# N5-R1 (box 81): the ladder dies under the Ξ-offer FORM (k rises, not 2^k), but CONJECTURE R1-POLY is DEAD: private gates restore 2^k (gl_8: 256 W-values at one vertex, n 48). The missing law is CONSISTENCY: Ξ is a valuation, so its freedom lives only at Odd choice vertices
L-NEW successor 37 (Opus 5.5), D14 / D18, Lead reading L40. Lead 09:49Z: «BOX 81, R1-POLY: GO. Test first that the ladder is NOT reachable
under N5's Ξ-offer rule; TWIN-SYNC says the lead step dies. Then attempt the bound, or give the exact obstruction with an instance.»
Written 2026-10-30 09:50Z-10:05Z (date -u). Working note, unrefereed, not a TARGET.md claim. G-N5-TIME OPEN.
- Definitions: docs/new/N5-WCHT-box80.md (R0, ladder_k, Proposition LADDER, Lemma TWIN-SYNC, R1). Restated: R1 = R0 plus the offer FORM of
  [S2]: the offers at t are Of_t := {(v, w) : X_t(w) ▷ X_t(σ_t v)} for a potential X_t with X_t ⊴ W_t pointwise and X_t non-decreasing in
  t; σ_{t+1} := the one-player optimum of σ_t ∪ Of_t. N5's Ξ is one such X (XW, R15), with more laws.
- Tools in experiments/new/box81: ladder_r1.py (part 1), gladder.py (part 2); instances inst/gl_{2,3,4,6,8}.pg.

## 1. The ungated ladder is not reachable under the offer form (DATA, exhaustive; Lead's step 1)
- R1⁻ (WEAKER than R1: X need not be monotone nor below W): at each step ANY ranking of the vertices; Even v is offered every w with
  rank(w) > rank(σ_t v). In ladder_k all choosers of one level share the successor set {u(j, 0), u(j, 1)}, so a ranking acts per level as
  a direction (none, 0 → 1, 1 → 0), offered to every holder of the lower copy at once (TWIN-SYNC's mechanism).
- ladder_r1.py: exhaustive DP over all states and all per-level directions, from the all-copy-0 start and from EVERY start:
  | k | n | max W(T)-rises under R1⁻ | under R0 (box 80) |
  | --- | --- | --- | --- |
  | 2 | 6 | 2 | 3 |
  | 3 | 8 | 3 | 7 |
  | 4 | 10 | 4 | 15 |
  | 5 | 12 | 5 | 31 |
- So under any ranking-offer rule the ungated ladder gives exactly k rises (linear): the lead-follow step is impossible, as TWIN-SYNC
  predicts. Since R1 ⊆ R1⁻, the same holds under R1 and under N5.

## 2. DEAD: CONJECTURE R1-POLY (Proposition GATED-LADDER, PROVED (lane) with DATA)
- gl_k: ladder_k with every choice edge v → u(j, b) subdivided by a PRIVATE gate g(v, b) (Even, one successor u(j, b)). Gates are less
  relevant than every ladder vertex (priorities 2 … 4k − 1, ladder 4k + 2 …, sink 0, T 1), so path comparisons are decided by the ladder
  part exactly as in ladder_k. n = 2k + 2 + 2(2k − 1) = 6k.
- Statement. For every k there is an R1 run on gl_k (X monotone, X ⊴ W, offers of the [S2] form, each step the one-player optimum of
  σ_t ∪ Of_t) in which W(T) takes 2^k values.
- Construction. Replay box 80's lead-follow schedule (v → u(j, b) becomes v → g(v, b)) with
  X_t(g) := W_s(g), s the last state ≤ t at which g was its owner's current successor or the scheduled target (BOTTOM, the least value,
  if never); X_t(x) := W_t(x) for every non-gate x.
- Proof. (i) X ⊴ W: a frozen W_s(g) ⊴ W_t(g) (W monotone, box 80); BOTTOM is least. (ii) X non-decreasing: a gate's X is frozen or
  tracks W (current gates), or jumps from a frozen value to the current W (target): all ⊴ moves. (iii) Of_t is exactly the scheduled edge
  (v, g_t): the target's X is raised to W_t(g_t) ▷ W_t(σ_t v) = X_t(σ_t v) (the switch is W-improving, and gates do not change the ladder
  comparison); every other chooser y holds a current gate with X = W_t(σ_t y), and its other gate g′ (private to y) has X = BOTTOM or the
  value frozen when y last LEFT g′ for an improving successor, so X(g′) ⊴ W_{s}(g′) ◁ W_{s}(σ_{s+1} y) ⊴ W_t(σ_t y) (y's current value
  only rises while y stays). So nothing else is offered. (iv) A single offered improving edge: the one-player optimum is that switch
  (R15 (a)). Box 80's induction then gives 2^k values at T. □
- DATA (gladder.py, fleet Engine): k = 2, 3, 4, 6, 8: T-values 4, 8, 16, 64, 256 = 2^k at n = 12, 18, 24, 36, 48; X > W 0, X decreases 0,
  offer mismatches 0, non-improving 0, W decreases 0. Pinned: inst/gl_8.pg (749 steps, 256 values).
- So R1-POLY is DEAD. Exact obstruction: R1 lets X move independently at a private single-successor vertex. Then every edge gets its own
  offer switch, and R1 collapses to R0 (box 80).

## 3. What N5 has that R1 lacks: CONSISTENCY (READING, with the one-line reason)
- N5's Ξ_t is the valuation of a PAIR (σ_t, σ̄_t) ([S1-Xi]). So at every Even vertex x that is not its own Ξ-cycle node,
  Ξ_t(x) = x ⊕ Ξ_t(σ_t x) ([V1]); at an Odd vertex o likewise with σ̄_t(o). A single-successor gate g has Ξ(g) = g ⊕ Ξ(child): it cannot
  be raised on its own. In gl_k under N5 the two gates of v compare as g(v, 0) ⊕ Ξ(u_0) against g(v, 1) ⊕ Ξ(u_1), i.e. by the children's Ξ
  (the ladder part dominates): the gates are transparent and §1's synchronisation returns.
- The only place where Ξ departs from a function of σ's choices is an Odd CHOICE vertex o with σ̄_t(o) ≠ τ(o) (there Ξ(o) ≠ W-side
  structure; P-N5-WCH's TXC sources SBAR / WIT; R56's ρ). So a counter in N5 must place an Odd choice vertex as the gate on every
  lead-follow edge, and must re-open it (σ̄ flips back and forth, Ξ monotone) once per counter step. That is exactly R132's / R108's
  "reused desynchronising gate", now derived: R0 → (offer form) R1⁻ kills ladders → (private gates) R1 revives them → (consistency) only
  Odd-choice gates remain.
- CONJECTURE R2-POLY (OPEN, the next precise target): R2 := R1 with X_t = val(σ_t, ρ_t) for some Odd strategy ρ_t (any, not necessarily
  optimal), X_t ⊴ W_t, X monotone. Claim: per-vertex W-changes per W-run are polynomial in R2. If FALSE, the instance is a design for L-RED
  (it would still need ρ_t = σ̄_t, Odd's optimum, to be an N5 run). If TRUE, it implies [P-WCHτ] on W-runs (N5 is an R2 run).

## DONE / FINDINGS / NEEDS
- DONE: experiments/new/box81/ladder_r1.py, gladder.py, inst/gl_{2,3,4,6,8}.pg; this note; check.sh "box 81" (gl_6 replay, ladder_r1 k 4).
- FINDINGS:
  1. DATA (exhaustive, k ≤ 5): the ungated ladder under ANY ranking-offer rule gives exactly k W-rises at T (2^k − 1 under R0). Not
     reachable under N5's offer rule: confirmed.
  2. DEAD: CONJECTURE R1-POLY. Proposition GATED-LADDER (lane-PROVED, DATA k ≤ 8): private single-successor gates plus a monotone X ⊴ W
     give 2^k W-values at one vertex (gl_8: 256 at n 48). Obstruction: R1 lets X move alone at a gate.
  3. READING: N5's consistency (Ξ is a pair valuation) makes single-successor gates transparent; the only free gates are Odd choice vertices
     with σ̄ ≠ τ, re-opened once per counter step (R132's reused gate). CONJECTURE R2-POLY is the next precise target.
- NEEDS: none from the owner. Lead: go / no-go on R2-POLY (box 82); context ~380k.
