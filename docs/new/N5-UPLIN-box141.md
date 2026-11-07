# Box 141 N5-UPLIN: UP-LIN not proved; per-arrival charging is box 140's per-level counting and cannot close; data strengthened to d 8 (FL 19, linear, ~2.4 per level; at most 5 moves per mover)
L-NEW successor 47, 2026-11-02 (date -u: see the commit). Lead GO 01:24Z (box 141: prove UP-LIN on the 2-wide UP-LADDER with §3's step
causality). Labels: PROVED (lane), CONJECTURE, READING, DATA, OPEN. G-N5-TIME, IDEAL-ACYC-POLY and UP-LIN stay OPEN. Not a TARGET.md
claim. Model and notation: boxes 139-140 (docs/new/N5-IDEAL-box139.md, N5-JOINT-box140.md).

## 0. Answer
- UP-LIN is NOT proved. The suggested charge does not go through, for this reason (PROVED, lane, §1):
  - charging each move at level l to one W-arrival (an L_(l−1) flip since the mover's previous move) and one Ξ-arrival (a face reversal
    since its previous move) gives exactly moves_l ≤ 2 + min{2·flips(L_(l−1)), Σ face reversals};
  - those are box 140's per-level counts, whose pointwise minimum TWO-SIDED shows to be exponential in the middle;
  - so «arrivals interleave O(1) times per level» is not implied by the step causality alone. It needs a cross-level statement: how many
    levels one Ξ-wave can serve.
- The step causality that is PROVED (lane) is R178's Lemma XI-NEW, restated for the UP-LADDER (Lemma DESCENT, §1):
  - at every step t ≥ 2, the least-level mover's new option had a strict face rise at step t − 1, caused by a move strictly ABOVE it
    (on its option's Ξ-play) at step t − 1;
  - so every step's lowest move is fed from above one step earlier, while W-arrivals climb within a step.
  - A linear bound would follow if one Ξ-wave (a chain of steps whose lowest movers descend) could carry only O(1) W-arrivals per level
    it passes. That is OPEN, and it is the precise missing lemma.
- DATA (§2) strengthened: the UP-LADDER climbs (now 6 depths, 2 seeds at d 5-6) give the best FL length 5 / 7 / 11 / 13 / 16 / 19 at
  d = 3..8. The second seeds give 10 (d 5) and 13 (d 6). This is linear, about 2.4 per level, against LADDERBF's 22 / … / 1004.
  - The max moves of one mover is ≤ 5 at d 8. Moves and L-flips per level peak mid-ladder (d 8: moves 2, 6, 8, 9, 8, 4, 4, 2; L-flips
    2, 6, 8, 9, 7, 6, 6, 5).
- CONJECTURE UP-LIN (DATA only): UP-LADDER runs have O(d) steps. Data now cover d ≤ 8, with growth ~2.4 d; still climbs only.
- Ψ (box 140 §3) is not tested: L-RED's middle-out counter does not exist yet. On the climb champions Ψ is not evaluated, because it
  was formulated for that counter.
- The synchronisation that would break UP-LIN (READING): a mid-level mover needs M W-arrivals (L-flips below, each climbing within one
  step through SPLIT levels) and M Ξ-arrivals (each fed by a move above one step earlier).
  - A family must keep ~d/2 consecutive levels split while flips pass, and let each Ξ-wave reverse faces at a level exactly at the steps
    when the W-wave has just flipped L there.
  - In every climb the split runs break: L-flips grow additively per level, by at most a few per level.

## 1. Proofs (PROVED, lane)
- Charging identity. Let x at level l ≥ 1 move at steps t_1 < … < t_M.
  - By TOWARD-L, some flip of L_(l−1) lies in (t_i, t_(i+1)].
  - By ALTERNATION, some reversal of x's face order lies between the decision states t_i − 1 and t_(i+1) − 1.
  - Distinct moves of x get distinct flips and distinct reversals.
  - So M ≤ 1 + min{flips(L_(l−1)), face reversals of x}. Summed over the two movers of the level, this is box 140 §2's pair of counts.
  - Box 140 TWO-SIDED: with only these, the maximum over l is exponential in d. ∎
- Lemma DESCENT (R178 Lemma XI-NEW, PROVED there for the IDEAL model; here only its UP-LADDER reading). At a step t ≥ 2 that is not
  stuck, let h be a least-level mover and w its new option.
  - Then w ∉ A_(t−2)(h) and w ∈ A_(t−1)(h), so face(h, w) rose strictly at step t − 1 (R178 consequence (ii)).
  - In an UP-LADDER the Ξ-play of face(h, w) visits only movers of level > lev(h) (Ξ-targets point up), so some mover of level > lev(h)
    moved at step t − 1. ∎
- Corollary. Steps whose least mover has level d − 1 number ≤ 1 (the first step): there is nothing above. Steps whose least mover has
  level d − 2 need a top move at the previous step, so there are ≤ 2 + 1 of them (each top mover moves ≤ 1 time, TOP-STATIC). The same
  argument one level further down needs a count of moves above, which is the circular part: it is box 140's top-down recursion.

## 2. DATA
Tools: box140/upclimb.py (climbs), box140/alt.py, box139/paths.py, box141/trace.py (per-state pairs, L_l, face preferences, movers).
Genomes and logs: box141/out/up_d{5,6,7,8}_s*.json / .log (30 min each, 1 core; d 7 and d 8 were ended by the timeout before printing
BEST; their last IT line is the best).

| d | seed | best FL | LADDERBF | moves per level | L-flips per level | max moves of one mover | checks (ALT / TOWARD / L-ACC / PATHS) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | 3 (box 140) | 5 | 22 | 2, 2, 2 | 1, 2, 3 | 2 | 0 / 0 / 0 / 0 |
| 4 | 4 (box 140) | 7 | 52 | 2, 3, 3, 2 | 1, 2, 2, 3 | 2 | 0 / 0 / 0 / 0 |
| 5 | 5 (box 140) / 15 | 11 / 10 | 114 | 2, 5, 7, 4, 2 / 2, 2, 4, 4, 2 | 2, 5, 5, 3, 2 / 2, 3, 4, 4, 3 | 4 / 2 | 0 each |
| 6 | 6 (box 140) / 16 | 13 / 13 | 240 | 2, 4, 7, 7, 3, 2 / 2, 5, 4, 5, 4, 2 | 2, 3, 7, 6, 6, 5 / 2, 5, 4, 3, 3, 4 | 4 / 3 | 0 each |
| 7 | 7 | 16 | 494 | 2, 6, 6, 6, 5, 3, 1 | 2, 6, 6, 5, 4, 2, 1 | 4 | 0 each |
| 8 | 8 | 19 | 1004 | 2, 6, 8, 9, 8, 4, 4, 2 | 2, 6, 8, 9, 7, 6, 6, 5 | 5 | 0 each |
- LADDERBF ceiling 2(2^(d+1) − d − 2) (R177): 494 at d 7, 1004 at d 8.
- Trace of up_d8_s8 (trace.py): steps move 2-4 movers each. Level-0 moves occur once, mid-run (step 11: movers 0, 2, 5), followed by a
  second wave up the ladder, as in box 140's d 6 trace.

## 3. Status
- PROVED (lane): the charging identity (equal to box 140's counts, hence insufficient); Lemma DESCENT (R178 XI-NEW read on the UP-LADDER)
  and its top-two-levels corollary.
- OPEN: the cross-level lemma «one Ξ-wave carries O(1) W-arrivals per level»; UP-LIN; IDEAL-ACYC-POLY.
- CONJECTURE UP-LIN (DATA only, d ≤ 8, ~2.4 d).
- Next (Lead decides): wait for L-RED R188's middle-out counter (it either breaks UP-LIN or shows where synchronisation fails), then
  test box 140's Ψ on it.
