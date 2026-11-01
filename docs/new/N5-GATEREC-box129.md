# Box 129 N5-GATEREC: the recursive gate charge (each class is an Even pivot), with L-RED 41's PHASE-PORTAL / SELF
L-NEW successor 45, 2026-11-01 09:12-09:3xZ (date -u). Lead GO 09:15Z (his clock). Input: docs/red/R174-zroute.md at claude/l-red 5d27d366.
Code: experiments/new/box129/ (gatechg.py, runcorp.sh, c_corpus.txt). check.sh block «box 129 GATECHG». Pin: topfix_n10 (box 128
pincheck.txt: Oink --zlk / --tl verified, n5b identical). Labels: PROVED (lane), DATA, READING, DEAD.

## 0. Answer
- The recursion is stated and solved (Theorem GATE-REC, §2): non-first W-strict moves ≤ roots × (F + F² + … + F^D), where D is the
  depth of the charge relation and F its fan-in. This is polynomial if D = O(1) (F ≤ poly), or if the charge is additive (F = 1:
  ≤ D × roots).
- Exact obstruction (DATA, §3): neither holds.
  - D is a TIME depth, not a gate depth: 52 on topfix_n10 in a 58-transition window.
  - The vertex-level charge graph has cycles (mutual payment; SCCs up to 18 at ODIFF 0, up to 5 at ODIFF ≥ 1), so «gate depth» is not
    defined.
  - The charge is multiplicative: fan-in up to 30 (s3quad_K8_m30, ODIFF ≥ 1).
  - The roots include flat moves (TF-RED's open F term).
- On ODIFF ≥ 1 windows the corpus shows only D ≤ 4. READING: ODIFF ≥ 1 is not a structural restriction, so I do not conjecture
  D = O(1) there. One idle ODIFF vertex added to an ODIFF-0 window of topfix type would plausibly keep depth 52 (not built).

## 1. Review of PHASE-PORTAL and SELF (non-author)
- PHASE-PORTAL is correct.
  - It is STATIC-TIE (box 128) specialised to one portal class. With θ fixed, (P1) makes the W-order of the two options static, so W
    need not be constant; and Ξ-constancy is replaced by «i_2 already in h's arena at j_1».
  - NRW includes h at the W-plays at j_1 and j_2. That is exactly the comparison-corner condition of box 128 W2. Good.
  - Only transitions j_1 and j_2 need to be fallback-free (as box 128 W5).
- PP-1: correct. With ZC and NR (R173), the Ξ-order of i_0, i_1, i_2 is static, so i_2 ∈ I_{j_1−1}(h). This is the P3/P4 step of PORTAL.
- SELF: correct as stated; it needs cls(h, i_0) = X too (it is in the premises).
  - Weak point: (H) is a condition on the top vertex of K_Z(i_0) Δ K_Z(i_2) only, at the single time j_1 − 1. It says nothing when that
    symmetric difference is empty above Z; then Ξ(i_2) vs Ξ(i_0) is decided by length. That case is outside SELF.
  - §3's «kills the natural ping-pong» is a READING built on «a pivot's level-x cycle node is the top of its own prefix_x».
- R88 vs TWO-FIX: L-RED is right that R88's frozen W-phase holds λ_Ξ constant by definition, and a TWO-FIX stretch need not. My box
  128 Fact ZC-COUNT spoke only of frozen W-phases; no correction needed.

## 2. PROVED (lane)
- Lemma ORIGIN. Inside a TWO-FIX window (τ and σ̄ constant), if Ξ(x) or W(x) changes at transition k, some Even vertex on x's play at
  state k − 1 in that world (Odd following σ̄ for Ξ, τ for W) is switched at k.
  - Proof: Odd's choices are fixed. If no Even vertex of the play (path and cycle) switches, the play is the same at state k, and so
    is its value. ∎
  - DATA: CYC 0 in all 813 runs.
- Definition (charge). For a non-first W-strict move m = (h, j_2) outside the comparison corner, STRICT-PAY (box 128) gives change
  events. Take the earliest, (x, k, world), and let the payer p(m) := (v, k), with v the first vertex of x's state-(k − 1) play
  switched at k (ORIGIN). p(m) is a move at a transition ≤ j_2.
- Theorem GATE-REC.
  - Setting: one fallback-free stretch. C := the charged moves. Suppose the move-level relation m → p(m) is acyclic. Let:
    - D := its longest chain;
    - F := the most charged moves with one payer;
    - R := the payers outside C (first moves of a vertex in the stretch, flat or weak moves).
  - Then |C| ≤ |R|·(F + F² + … + F^D) ≤ |R|·D·F^D.
  - Proof: following p from any m ∈ C reaches a root in R in at most D steps. Each root has at most F^d moves of C at distance d. ∎
  - With |R| ≤ #movers + #flat moves of the stretch:
    - polynomial when D = O(1) and F ≤ poly(n);
    - when F = 1, |C| ≤ D·|R| with D ≤ stretch length (additive; a count of flat moves would then finish it).
  - Neither premise holds in the data (§3).

## 3. DATA (813 distinct (game, start) pairs, Erratum E-1; c_corpus.txt; 0 errors)
| quantity | ODIFF 0 windows | ODIFF ≥ 1 windows |
| --- | --- | --- |
| windows (≥ 1 transition) | 410 | 883 |
| W-strict moves / charged (non-first strict) | 7,971 / 2,592 | 10,605 / 1,268 |
| payer via Ξ / via W | 1,388 / 1,204 | 632 / 636 |
| payer kind first / strict / flat / weak | 1,136 / 1,456 / 0 / 0 | 773 / 494 / 1 / 0 |
| self-payment (payer = h: route (C)) | 18 | 38 |
| CYC (no switched vertex on the play) | 0 | 0 |
| max chain depth D | 52 (topfix_n10) | 4 (kw25_n32) |
| max fan-in F | 11 (xsnf42_n48) | 30 (s3quad_K8_m30) |
| max mutual-payment SCC (games with one) | 18 (block_bk32; 17 games) | 5 (ffin5_n32; 31 games) |
| chains revisiting a vertex (games) | 592 (9) | 1 (1) |
- Pin: topfix_n10, window [6, 64], ODIFF 0. Depth 52, fan-in 9. Eleven 3-vertex mutual-payment SCCs of Even vertices
  ({120, 121, 122}, {129, 130, 131}, {138, 139, 140}, …; out-degrees (4, 2, 3), (6, 4, 5), …).

## 4. Exact obstruction (READING over §2-§3)
- A gate's payment to its pivot comes back. Inside one stretch the pivot's move changes the gate's option values (the pivot is on the
  gate's play), and the gate's move changes the pivot's. The charge relation over VERTICES is cyclic, so a recursion «each gate is a
  pivot, PHASE-PORTAL at each level» has no base. Over MOVES it is acyclic, but its depth tracks time.
- This is the same mechanism as route (C) (self-cycles) one level up: mutual cycles among Even pivots in place of a pivot on its own
  portal's play.

## 5. Not done
- A size-indexed ODIFF ≥ 1 family with growing D: that is L-RED's.
- A count of flat moves: TF-RED's F.
- The optional availability item.

## DONE / FINDINGS / NEEDS: in the Lead message and notes/L-NEW.md.
