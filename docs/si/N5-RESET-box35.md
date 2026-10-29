# N5-RESET (box 35): a reset-progress potential? None survives; the needed law, stated
L-SI successor 29 (Opus 5.5), D15 / D18, Lead reading L40. Lead's brief 2026-10-29 20:07Z (BOX 35). Working note, unrefereed, not a
TARGET.md claim. G-N5-TIME OPEN. Labels: PROVED (lane) / CONJECTURE / DATA / DEAD / READING.
- Setting: box 34 (docs/si/N5-CARX-box34.md). A RESET is a MATCHED P-change of one vertex's valuation inside one λ-run (λ^U-run on
  G^d for Odd). #MAT_R(x) counts them. Tool: experiments/si/odd/carx.py with PHID = 1, 2, 3 (Φ_d: signed positions to the power d) or
  w (S1's exact weight). Kills as in box 34: wide_h16 (Odd side, vertex 2, run from 13) and fc_3 (Even side, vertex 6, run from 0).
- The Lead's 20:00Z question (is R85 per vertex?) is answered in box 34 §5 (l-si bf5518ed): per vertex per phase verbatim, R85 (c)
  l. 5108-5109; the per-vertex λ-run form is R86 (e)'s signed premise.

## 1. Candidates (DEAD unless stated)
- (λ, Φ) lexicographic: DEAD by the box 34 kills.
  - Both kills lie inside one λ-run (λ^U-run), where the vertex's cycle node is fixed, so the pair is Φ there (PROVED, lane: trivial).
- Φ only at the vertex's own cycle-node changes: NOT a reset potential.
  - Within a λ-run there are none, so it says nothing about resets inside a run, which is where the problem is.
  - Across runs, cycle-node changes of one vertex are ≤ n − 1 already (R47 (a) Φ (c)).
- Φ_d, d = 2, 3 (positions^d; range O(n^{d+1})): DEAD on fc_3.
  - Φ_2 goes 11587 → 5786 and Φ_3 goes 872765 → 373618 at the same pair of resets (t 0, 23).
  - Both PASS on wide_h16, so wide_h16 only kills d = 1.
- S1's exact weight: monotone at EVERY P-change (LEN-MONO's proof). Its range is 2^K, so it bounds nothing.
- MATCH-Φ directly (count resets against MATCHED events): circular with CARRY-SEG (box 34 §3).
  - #MAT ≤ W(1 + NM) and NM ≤ (#MAT + 1)(n − 1).
- What fc_3 shows (DATA, SHOW of vertex 6, t 0-25): the resets there are trivial (a single low even rank enters: "in [6]").
  - In between, carries bring in a high even rank with a block of odd ranks just below it, e.g. t 2: in {+40, −39, −37}; t 5: out {+40}
    in {+46, −45, −43, −41}.
  - Each such carry raises S1's weight (top of Δ even, entering) and lowers every polynomial-range potential. That is the
    binary-counter shape. Its entering tops are not monotone either: 84 at t 22, then 77 at t 24 (cf. CARRY-CLIMB, dead).
- Conclusion: no potential of polynomial range tried here is monotone across resets. A proof cannot come from the P-set sequence alone,
  because MATCH-Φ is sharp for abstract subset sequences (R85, citing REFEREE R-N5-MATCHPHI MATCH-N4: "attained by abstract all-matched chains (§3); the bound is sharp as a statement about subset sequences"). It has to use the
  game: which plays can produce the carry shapes above.

## 2. The needed law (CONJECTURE RESET-LIN, with data) and what it gives (PROVED lane, arithmetic)
- CONJECTURE RESET-LIN: for every N5 run, every vertex x and every λ-run R (λ^U-run on G^d for Odd), #MAT_R(x) ≤ n.
  - DATA (box 34 corpus, 718 Odd + 716 Even runs, S3): max #MAT / n = 0.17 (Odd, thetaA_n6) and 0.75 (Even, x31_cu16: 12 at n 16).
    The largest absolute count is 29 (Even, rise_thin51_n40, n 40).
  - d_hntop: #MAT = N − 1 at n = 21N.
- PROVED (lane, arithmetic): CARRY-SEG + RESET-LIN ⇒ PCH_R(x) ≤ n + (n + 1)(n − 1) < n² + n per vertex per λ-run.
  - With R86 (d): T ≤ 2n(n − 1) + (n(n − 1) + 1)·n·(m_E + m_O)·(n² + n + 1) = O(n⁶·m) on every game, with no frame premise.
  - Equivalently, the single law PCH-QUAD (PCH_R(x) ≤ n² + n per vertex per λ-run) suffices. Box 34's corpus data are consistent
    with it; it is not separately measured here.
- Weaker forms that still suffice: any polynomial in place of n in RESET-LIN, with CARRY-SEG's n − 1 relaxed to any polynomial.
- With L-NEW 35's COMPOSE-FREEZE only the targets of unprotected Odd edges need the Odd half (box 34 §5).

## 3. Composition toward G-N5-TIME (one line)
- G-N5-TIME ⇐ CARRY-SEG + RESET-LIN (both CONJECTURES, 0 failures on the corpus), via R86 (d) and the per-vertex premise of R86 (e).
- The next step is a game-structural lemma that limits carry shapes "even top + odd block below" between resets.

## DONE / FINDINGS / NEEDS
- DONE: carx.py PHID option; this note; check.sh «box 35» (fc_3 Φ_2 / Φ_3 kills, Φ_2 pass on wide_h16, exact-weight sanity).
- FINDINGS:
  1. DEAD: (λ, Φ) lexicographic (same kills, in-run); Φ_d for d = 2, 3 (fc_3).
  2. Not a reset potential: Φ at cycle-node changes only.
  3. Circular: MATCH-Φ counting with CARRY-SEG.
  4. CONJECTURE RESET-LIN (#MAT ≤ n per vertex per λ-run; data ≤ 0.75n).
  5. PROVED (lane, arithmetic): CARRY-SEG + RESET-LIN ⇒ O(n⁶ m) iterations.
- NEEDS: none from the owner.
