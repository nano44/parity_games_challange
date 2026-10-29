# N5-PIECE (box 25): Theorem STATIC-DEPTH′ (two-frame settling; (H3) weakened to (H3′), (H4) to (H4′), λ_W-constancy dropped); Corollary EPOCH; the uncovered pieces
L-SI successor 21 (Opus 5.5; D18, Lead reading L40). Lead's brief 2026-10-29 03:02Z, STEP 1: «CONJECTURE PIECE (unconditional): a σ̄-constant
stretch of a fallback-free in-phase S4a run has ≤ n − 1 transitions ... Aim: drop or weaken (H3) / (H4) / GEN_W with a proof, or find a piece
longer than n − 1». Working note, unrefereed, not frozen. Not a TARGET.md claim. Nothing here bounds N5's running time; G-N5-TIME stays OPEN.
Labels (D18 / L40): PROVED (lane) / CONJECTURE / OPEN / DATA / READING / DEAD. Counts are TRANSITIONS (REFEREE CORE-N1).
Tools: experiments/si/piece/ (pieceh.py, sdprime.py, epochs.py, piececlimb.py); outputs piece/*.txt, piece/out/.

## Summary
| § | item | label |
| --- | --- | --- |
| §1 | which of R77's hypotheses the 155 failing alt_all pieces break: 142 have W-cycles ≠ honest cycles at some state, 24 have cycles that change, 29 fail (H4), 41 have λ_W changing; all are short (max length 25, max length/(n − 1) = 0.81) | DATA |
| §2 | Theorem STATIC-DEPTH′: R77 (c) with (H3) replaced by (H3′) "every W-cycle of the end state is a W-cycle throughout and every honest cycle of the end state is an honest cycle throughout" (the two frames may differ), (H4) by (H4′) (a two-frame depth graph J_b is acyclic; implied by (H4) under (H3)), and without λ_W constant; bound b − a ≤ max d ≤ \|Even ∖ (T_W ∪ T_H)\| ≤ n − 1 | PROVED (lane) |
| §2 | coverage: 844 / 872 alt_all pieces (R77: 708), 914 / 943 lib41, 940 / 1,080 random 𝒞^kO; 0 violations; MUT bites | DATA |
| §3 | Corollary EPOCH: cut a piece from its end into epochs on which the epoch-end cycles persist; then \|piece\| ≤ k(n − 1) + k − 1 ≤ (CF + 1)·n − 1, CF the transitions of the piece at which a new cycle appears (needs (H4′), GEN_W at each epoch end) | PROVED (lane); a REDUCTION (CF is not bounded) |
| §4 | what is left of CONJECTURE PIECE: pieces in which a cycle of the end state forms inside the piece (24 alt_all), and 4 (H4′) failures; kill search (piececlimb.py) | DATA, OPEN |

## 0. Setting
- N5 = SPEC S1-S5 (docs/new/N5-ssi-global.md). A run S: a maximal fallback-free stretch of one phase ((λ_Ξ, τ) constant, RESULTS R38 (a)).
  A PIECE of S: a maximal stretch [a, b] of states of S with σ̄ constant (N5-RUNLIN-box24 §8). Ξ_t, W_t, D_t as in RESULTS R77's setting:
  Ξ_t(v) is the S1 valuation of v's honest play (σ_t, σ̄_t), W_t(v) that of v's (σ_t, τ)-play.
- CONJECTURE PIECE (N5-RUNLIN-box24 §8): every piece has ≤ n − 1 transitions. LANDED only under R77 (c) Theorem STATIC-DEPTH's hypotheses
  (H1) (S4a steps, τ, λ, λ_W constant), (H2) (σ̄ constant), (H3), (H4), GEN_W, through R77 (e) Corollary GCI-LEN-ρF (quoted in §2).
- Landed premises used in §2-§3 (each LANDED; nothing else): SPEC S1 (valuation, total order), S4a (arena {σ_t(v)} ∪ Iσ_t(v); Even's pointwise
  W-optimum over strategies using arena edges), S4c (fallback); RESULTS R77 (c)'s proof steps, signed there: «(W-MONO) W_{t+1} ⊵ W_t (P2),
  (Ξ-SUCC) Ξ_t(σ_t v) non-decreasing ((M2κ), (SW))», and the pointwise W-optimality used in its step (B); (SW) "every Even switch of N5 is to
  an edge of Iσ" (as listed among RESULTS R72's landed premises); RESULTS R80 (a) (C1) EVERY-SWITCH (every in-phase transition changes σ).
  GEN_W as in R77: «for every v, different W-plays from v to the same cycle have different W-valuations».

## 1. DATA: the 155 alt_all pieces outside R77 (piece/pieceh.py; log piece/pieceh_alt.txt)
- Corpus: runlin/out/alt_all_root.lst (413 files, default starts), all pieces of all runs: 872 pieces (root/staticdepth.py's 863 plus 9 from
  games without an Odd choice vertex, which staticdepth's --list skips).
- 155 pieces fail (H3) or (H4): H3W (W-cycles ≠ honest cycles at some state of the piece) 142; H3C (a cycle of either frame changes inside the
  piece) 24; H4 29; λ_W changes inside the piece 41 (so R77's (H1) fails there too).
- All are short: max length 25 (kw25_n32, [0, 25], n 32), max length / (n − 1) = 0.806 (fx2_n11, 7 of 10), min slack (n − 1) − length = 3.
  Pieces inside R77 reach 0.936 (max length 67, grow_K40_n373). PIECE holds on all 872 ("PIECE PASS").
- Per vertex, one Even vertex can switch many times in one piece (up to 16 in cxmig_k16_n138 [0, 22]); "length ≤ number of distinct
  switching Even vertices" fails on cw11_n24 [0, 3] (one vertex, 3 transitions). So no once-per-piece argument.

## 2. Theorem STATIC-DEPTH′ (PROVED, lane, unrefereed)
Hypotheses on states [a, b] of one phase:
- (H1′) every transition t → t + 1, a ≤ t < b, is an S4a step (no fallback); τ and λ constant. (λ_W need not be constant.)
- (H2) σ̄_t = σ̄_a for t ∈ [a, b].
- (H3′) every W-cycle at b (a cycle of the (σ_b, τ) successor map, as a vertex sequence) is a W-cycle at every t ∈ [a, b], and every
  honest cycle at b is an honest cycle at every t ∈ [a, b]. T_W, T_H := the vertices on the W-cycles, the honest cycles at b; T := T_W ∪ T_H.
- Depths. dW(v) := 0 on T_W, dH(v) := 0 on T_H; for Odd v: dW(v) := dW(τ v), dH(v) := dH(σ̄ v); for Even v ∈ T_H ∖ T_W: dW(v) := dW(σ_b v);
  for Even v ∈ T_W ∖ T_H: dH(v) := dH(σ_b v); for Even v ∉ T: dW(v) = dH(v) := d(v) := 1 + max(dW(y), dH(y)), y := σ_b(v).
- (H4′) the recursion is well founded, i.e. the graph J_b on the Even vertices outside T, with an edge v → v′ when v′ is the first Even
  vertex outside T after v on v's W-play at b or on v's honest play at b, is acyclic.
- GEN_W.
Claim. Every v has, at every t ∈ [a + dW(v), b], its W-play at b, and at every t ∈ [a + dH(v), b], its honest play at b. Hence σ_t = σ_b on
[a + max d, b], and b − a ≤ max_v d(v) ≤ |Even ∖ T| ≤ n − 1.
Proof. "v W-settled from s": v's W-play at every t ∈ [s, b] equals its W-play at b; "H-settled" likewise with honest plays. Induction on the
well-founded recursion.
- v ∈ T_W: v lies on a W-cycle Z at b, which is a W-cycle at every t (H3′); a vertex on a cycle of a successor map has that cycle as its
  play, so v is W-settled from a. Likewise v ∈ T_H is H-settled from a. An Even v ∈ T has σ_t(v) = its successor on that cycle = σ_b(v)
  for all t ∈ [a, b].
- Odd v ∉ T_W: v's (σ_t, τ)-successor is τ(v) at every t (τ constant). If τ(v) is W-settled from s, then at t ∈ [s, b] τ(v)'s W-play is its
  W-play at b, which does not contain v (v ∉ T_W, so v's W-play at b is v followed by τ(v)'s, simple up to a cycle not through v); so v's
  W-play at t is v followed by it, i.e. its W-play at b. v is W-settled from s = a + dW(τ v). Odd v ∉ T_H: the same with σ̄(v) (constant by
  (H2)) and honest plays.
- Even v ∈ T_H ∖ T_W: σ_t(v) = σ_b(v) = y for all t (first item), so the Odd argument applies with y: W-settled from a + dW(y). Even
  v ∈ T_W ∖ T_H: H-settled from a + dH(y), the same way.
- Even v ∉ T, y := σ_b(v), y W-settled from a + dW(y) and H-settled from a + dH(y); s := a + max(dW(y), dH(y)).
  - (A) For t ∈ [s, b], y ∈ {σ_t v} ∪ Iσ_t(v). Otherwise σ_t(v) ≠ y and Ξ_t(y) ⊴ Ξ_t(σ_t v) (S1's order is total). Since σ_b(v) = y, v
    switches to y at some t′ → t′ + 1 with t ≤ t′ < b. By (SW), Ξ_{t′}(y) ▷ Ξ_{t′}(σ_{t′} v) ⊵ Ξ_t(σ_t v) ⊵ Ξ_t(y) = Ξ_{t′}(y) (Ξ-SUCC; y
    H-settled, and a valuation is a function of the play). Contradiction.
  - (B) For t ∈ [s, b − 1], let s′ := σ_{t+1} with v's choice set to y. By (A), s′ uses arena edges of state t. y's W-play under σ_{t+1}
    is its W-play at b (y W-settled, t + 1 ≥ s), which does not contain v (v ∉ T_W); so it is also y's play under s′, and W_{s′}(v) =
    v ⊕ W_b(y) = W_b(v). S4a's pointwise optimality gives W_{t+1}(v) ⊵ W_b(v); W-MONO from t + 1 to b gives W_{t+1}(v) ⊴ W_b(v). So
    W_{t+1}(v) = W_b(v).
  - The cycle node c of W_b(v) is on a W-cycle Z at b, and Z is c's W-play at t + 1 (H3′). W_{t+1}(v) has cycle node c, so v's W-play at
    t + 1 enters c and then follows Z: it ends in the same cycle as v's W-play at b. By GEN_W the two plays are equal; so σ_{t+1}(v) = y,
    and v's honest play at t + 1 is v followed by y's honest play at t + 1, which is y's honest play at b (y H-settled) and avoids v
    (v ∉ T_H): v's honest play at b. So v is W- and H-settled from s + 1 = a + d(v).
- Length. At t ≥ a + max d, every Even v ∉ T has σ_t(v) = σ_b(v) (the first step of its W-play), and every Even v ∈ T has it by the first
  item; so σ_t = σ_b. If b > a + max d, the transition a + max d → a + max d + 1 of the phase leaves σ unchanged, against R80 (a)
  EVERY-SWITCH. So b − a ≤ max d. A longest J_b-path visits distinct Even vertices outside T (H4′), and d(v) counts the vertices of such a
  path from v, so max d ≤ |Even ∖ T| ≤ n − 1 (T ≠ ∅: every play ends in a cycle). □
Remarks.
- STATIC-DEPTH′ contains R77 (c) STATIC-DEPTH. Under (H3), T_W = T_H = the common cycle vertices, and a J_b edge v → v′ follows σ_b at Even
  vertices and τ or σ̄ at Odd ones through non-terminal vertices only, i.e. it is an H_b-path; so a J_b cycle is an H_b cycle, and (H4) gives
  (H4′). (H3) also gives λ_W constant, which STATIC-DEPTH′ does not assume.
- What is new: the W-cycles and the honest cycles may DIFFER (142 of R77's 155 failures are of this kind), and cycles of either frame that
  are not end-state cycles may come and go inside the piece; only the end-state cycles must persist. The proof never compares the two
  frames' cycles: it settles each frame along its own end-state play and uses the other frame only through (A) (honest values decide the
  arena) and (B) (W decides the step).
- The bound is |Even ∖ T|: the Even vertices off the end-state cycles of both frames.
DATA (piece/sdprime.py; MUT=1 uses d − 1 and must bite):
| corpus | pieces | (H3′) fails | (H4′) fails | checked | of which outside R77's (H3) | violations (SET / LEN / > n − 1) | pieces with a GEN_W failure (counted, not excluded) | MUT=1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| alt_all (piece/sdprime_alt.txt) | 872 | 24 | 4 | 844 | 127 (longest 25, kw25_n32) | 0 / 0 / 0 | 8 | SET_V 912 |
| lib41 (experiments/new/box41/lib41.txt; piece/sdprime_lib41.txt) | 943 | 27 | 2 | 914 | 153 (longest 25) | 0 / 0 / 0 | 14 | (not run) |
| 3,000 random 𝒞^kO games n 8-40, seed 7 (piece/sdprime_rand.txt) | 1,080 | 139 | 1 | 940 | 52 | 0 / 0 / 0 | 0 | SET_V 74 (300 games) |
- CONJECTURE STATIC-DEPTH′-TIE: the same without GEN_W. Data: 22 pieces with a GEN_W failure, conclusion intact in all.

## 3. Corollary EPOCH (PROVED, lane; a REDUCTION)
- Cut a piece [a, b] from its end: b_k := b; a_k := the least state such that every cycle (W and honest) of state b_k is a cycle of its frame
  at every state of [a_k, b_k]; then b_{k−1} := a_k − 1 and repeat down to a. This gives epochs [a_1, b_1], ..., [a_k, b_k] (an epoch may be a
  single state). Each epoch satisfies (H1′), (H2), (H3′) with end state b_i (by construction).
- Claim. If (H4′) and GEN_W hold at every epoch end, |piece| = Σ_i (b_i − a_i) + (k − 1) ≤ k(n − 1) + k − 1; and k − 1 ≤ CF, the number of
  transitions of the piece at which a cycle appears (a cycle of the state t + 1, in either frame, that is not a cycle of that frame at t).
  So |piece| ≤ (CF + 1)·n − 1.
- Proof. STATIC-DEPTH′ on each epoch. At the boundary a_i − 1 → a_i (i ≥ 2) some cycle Z of b_i is not a cycle at a_i − 1 but is one at
  a_i (minimality of a_i): Z appears at that transition. Distinct boundaries are distinct transitions. □
- This is a product again (as Lemma SPLIT, N5-RUNLIN-box24 §8): PIECE would follow from CF = 0, i.e. from (H3′). CF is not bounded here.
- DATA (piece/epochs.py; piece/epochs_alt.txt, piece/epochs_lib41.txt): alt_all 872 pieces in 911 epochs, 24 pieces with more than one
  epoch (longest 18), at most 6 epochs and CF ≤ 5 in one piece, 4 epochs failing (H4′), every other epoch within its max d (0 violations);
  lib41 943 pieces, 990 epochs, 27 multi-epoch (longest 11), k ≤ 6, CF ≤ 5, 2 (H4′) failures, 0 violations.

## 4. What is left of CONJECTURE PIECE (DATA, OPEN)
- Uncovered by STATIC-DEPTH′: pieces in which a cycle of the end state appears inside the piece ((H3′) fails; 24 alt_all, 27 lib41, 139
  random), and (H4′) failures (4, 2, 1). In alt_all the uncovered pieces have length ≤ 18 and length / (n − 1) ≤ 0.43 (frz24 [1, 11], 10 at
  n = 24); the (H4′) failures have length ≤ 6 (dl_6_8 at n = 110).
- Kill search (piece/piececlimb.py; score max over UNCOVERED pieces of length − CN·(n − 1); mutations of runlin/growclimb.py):
  - CN = 1, from frz24, frz40, cone_n69 (ONLYOUT=1) and kw25_n32 (all pieces), 20,000 / 20,000 / 8,000 / 20,000 steps: best −4 (frz24 seed,
    piece/out/pc_frz24: length 10 at n = 15, 0.71(n − 1)); −7 (frz40 seed, n 20); −22 (cone, n 44); kw25 seed −4 at n 21. No kill.
  - CN = 0.7 (score length − 0.7(n − 1), so growth pays), ONLYOUT=1, 60,000 steps each: three seeds from piece/out/pc_frz24 (n 15) never
    improved (logs piece/out/pcg1-3.log: final 0.2, i.e. 10 at n 15); from frz40 (pcg4.log) best −1.9 at n 28 (still running at this write).
    No uncovered piece above 0.71(n − 1) was found.
- READING. Within a piece the honest frame is the one-player game G_σ̄ (σ̄ fixed) and the W-frame the one-player game G_τ; S4a is a policy
  iteration in G_σ̄ whose step is chosen by optimality in G_τ. STATIC-DEPTH′ says the run settles along the end state's plays as soon as the
  end-state cycles exist. What remains is the formation of those cycles inside a piece: an end-state cycle needs all its Even vertices to
  hold their cycle edges, and the (A)/(B) argument cannot start on a cycle (each vertex waits for its successor). A proof of PIECE needs a
  separate argument that bounds the time until the end-state cycles exist (or CF), e.g. via W-MONO at the cycle node (λ_W(v) can only move up
  in the reward order); none is in hand.

## DONE / FINDINGS / NEEDS
- DONE: this note; experiments/si/piece/ (pieceh.py, sdprime.py, epochs.py, piececlimb.py) with logs; check.sh block "box 25".
- FINDINGS: (1) PROVED (lane) Theorem STATIC-DEPTH′: R77's (H3) can be weakened to (H3′) (only the end-state cycles of each frame must persist;
  W- and honest cycles may differ) and (H4) to (H4′), with λ_W free; the piece bound becomes |Even ∖ (T_W ∪ T_H)| ≤ n − 1; coverage 708 → 844 of
  872 alt_all pieces. (2) PROVED (lane) Corollary EPOCH: |piece| ≤ (CF + 1)n − 1, CF = cycle appearances inside the piece (a reduction).
  (3) DATA: what is left of PIECE are pieces in which an end-state cycle forms inside the piece (and a few (H4′) failures); all short
  (≤ 0.43(n − 1) in alt_all); climbs found none above 0.71(n − 1). CONJECTURE PIECE stays OPEN; GEN_W is still needed by the proof.
- NEEDS: none from the owner. Lead: route STATIC-DEPTH′ / EPOCH to a referee if wanted (not frozen; a packet on request).
