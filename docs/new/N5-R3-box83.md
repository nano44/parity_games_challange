# N5-R3 (box 83): CONJECTURE R3-POLY (R2 + Odd optimality = N5 inside a W-run from any start pair) stays OPEN. DATA: per-vertex W-changes per W-run ≤ 0.33n (corpus max 48 at n 156; random n ≤ 14: ≤ 2). No proof; the exact remaining requirement is box 82's escape clock
L-NEW successor 37 (Opus 5.5), D14 / D18, Lead reading L40. Lead 10:53Z: «BOX 83: R3-POLY, R2 plus Odd optimality, GO. It is now the sharpest
form of the open question.» Written 2026-10-30 11:15Z-11:35Z (date -u), short box before parking. Working note, unrefereed, not a TARGET.md
claim. G-N5-TIME OPEN.
- R3 := R2 (docs/new/N5-R2-box82.md) with ρ_t := σ̄_t, Odd's pointwise-optimal counterstrategy to σ_t ([S1-Xi]). Inside a W-run of N5 the
  offers are Iσ_t ([S2]) and the step is S4a's one-player optimum, so an N5 W-run IS an R3 run; R3 differs from N5 only in allowing any
  start pair (σ_0, τ) and in having no S4c / τ-steps (excluded from W-runs anyway). So R3-POLY ⇔ [P-WCHτ] restricted to W-runs, for all
  start pairs.
- Tools in experiments/new/box83: r3rand.py (random games and random start pairs), wchmax.py + run.sh (corpus; box79/wchpk.py plus the
  max of WCH_F(e)); outputs wchmax_*.txt.

## 1. DATA
- Corpus (719 + 413 runs, N5 from the corpus starts): max over W-runs and vertices of WCH_F(e) is 48 (red/ul ladderd0_k48_n156 and
  ladderent_k48_n156, n 156: 0.31n); the largest ratio is 0.33n (red/xing x31_cu24). Growth on L-RED's ul ladder family is linear in its
  parameter (k 48 → 48).
- Random search (r3rand.py, 3000 games each, out-degree 1-3, random owners / priorities / start pairs): max WCH_F(e) = 1, 2, 2, 2 at
  n = 6, 8, 10, 14.
- So no super-linear per-vertex W-change count is known for R3 (= N5 W-runs). Boxes 80-82 show every weaker model (R0, R1, R2) reaches 2^k.

## 2. What a proof of R3-POLY must use, and what a kill must build (READING)
- Kill side: by box 82 §3 (GATE-COLLAPSE and the design spec), an R3 counter needs at every lead-follow gate a private escape whose Ξ sits
  ⊴ the owner's current Ξ while the gate is blocked and ⊵ the target's Ξ while it is open, alternating once per counter step, monotone, in one
  W-run. The escape is itself a W-run vertex of the same game, so its Ξ-climb is again an R3 count: a kill needs an escape clock that is
  cheaper than the counter it serves.
- Proof side: R3-POLY would follow from a bound "each Odd choice vertex's σ̄-routing can switch between two successors whose Ξ-order flips
  only poly(n) times per W-run", because GATE-COLLAPSE shows that desynchronisation needs such flips. That bound is the Odd-side analogue of
  [P-WCHτ] (L-RED's PREFIX / TWO-SOURCE on G^d) and is NOT proved here; box 76's SBQ data (σ̄-changes at Odd choice vertices per W-run up to
  5.4n, mostly RETURNS) says the Odd side's flips are breadth, not depth.
- CONJECTURE R3-POLY stays OPEN; it is the sharpest form of [P-WCHτ] on W-runs.

## DONE / FINDINGS / NEEDS
- DONE: experiments/new/box83/r3rand.py, wchmax.py, run.sh, wchmax_*.txt; this note.
- FINDINGS:
  1. DATA: max per-vertex W-changes per W-run 48 at n 156 (0.31n), max ratio 0.33n on the corpus; ≤ 2 on random games n ≤ 14.
  2. READING: R3 = N5 W-runs from any start; a kill needs a cheaper escape clock (box 82 spec); a proof needs an Odd-side flip bound.
  3. CONJECTURE R3-POLY OPEN (no proof, no kill).
- NEEDS: none from the owner. I park after this box (context ~470k).
