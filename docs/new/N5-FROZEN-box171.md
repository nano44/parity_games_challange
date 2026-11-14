# Box 171 N5-FROZEN: frozen-interval accounting for SLOT-TRADE — top-only intervals are few on every genome we have (≤ 6, about d + 1), but on the T^R-type maxima they come after roughly half of the lower steps; every top-only interval is renewed by a Ξ-rise from the lower step before it (RENEW, a corollary of R105 XI-NEW/RISE), and the count of renewals is not bounded by anything proved: no proof, no kill
L-NEW successor 54, 2026-11-05 (date -u: see the commit). Lead brief BOX 171 (22:08Z). Labels: PROVED (lane, unrefereed) / DATA /
CONJECTURE / READING. Model: RESULTS R104; R105 (XI-NEW, RISE) and R108/R109 (SEG, SEG-ONCE) as landed. Not a TARGET.md claim.
G-N5-TIME and SLOT-TRADE stay OPEN.

## 0. Answer
- Definitions:
  - top := the largest level.
  - A step is LOWER if some mover below the top level moves, else TOP-ONLY.
  - I := the number of maximal runs of consecutive top-only steps (frozen intervals that contain a top move).
  - L := the number of lower steps.
- (1) Measurement (box171/frozen.py, fsum.py; 267 file paths: all L-RED JSON at 002f7cd1, all L-NEW box 160-170 genomes):
  - I ≤ 6 on every file, and every top-only run has length ≤ 2.
  - Max I by (degree, d): deg 2: d 1-8 → 1, 2, 4, 4, 6, 2, 0, 2; deg 3: d 2-8 → 2, 4, 6, 5, 6, 3, 2.
  - L reaches 63 (grow_top_N24: L 63, I 1). Long runs have FEW top-only intervals: grow_top_N24, N21, N18 have I = 1, 3, 6 at L =
    63, 49, 40.
  - On the T^R-type maxima, however, I/L is large: max_d4_L13 (T 13 = T^R(4)): L 9, I 4, pattern LTLTLLLLLTLTL; g5_a (deg 2, d 5,
    T 18): L 12, I 6, pattern TLLLTLTLLLTLTL….
  - «T(d − 1) of the restriction» is not defined on these files: in every one some lower option Ξ-targets a top mover, so the
    genome without its top level is not autonomous. L is used in its place.
  - Hill-climbs on I (box171/climbI.py, d 3-6, widths 2-3, 3,000 steps × 4 restarts): I ≤ 3. Weak, like every random-start climb.
- (2) Mechanism, PROVED (lane) RENEW (a corollary of landed R105 XI-NEW and RISE, applied to a step whose least-level movers are
  top movers). If step t ≥ 2 is top-only and h moves at t to option w, then:
  - w ∉ A_(s_(t−2))(h): h did not prefer w before step t − 1;
  - Ξ_(s_(t−1))(h, w) rose strictly at step t − 1;
  - some strict Ξ-descendant of h on w's chain under s_(t−2) moved at step t − 1.
  Moreover, in a top-only interval the keys of top movers are constant: they depend only on the states below the top (LOCAL-KP),
  and those do not change. So:
  - every top-only interval that starts at t ≥ 2 begins right after a step t − 1 that is a LOWER step (definition of an interval's
    start), and at that step a strict Ξ-descendant y of a top mover h moved (y may be at any level, top included);
  - the renewal is Ξ-side (a value rise), never W-side: a key flip alone cannot start a top-only interval.
  The answer to (2) is yes: a top move «uses up» a Ξ-rise, and a new interval needs a new rise from a lower step.
- (3) Counting renewals. I ≤ 1 + #{lower steps that move a strict Ξ-descendant of a top mover on the chain of the option it then
  takes}. Nothing proved bounds that count by O(d): each top mover can be renewed once per own move, and its moves are bounded only by
  1 + KF (KEYFLIP), i.e. by T(d − 1)-type quantities again. Data: I/L ≈ 0.44-0.5 on the two T^R-type maxima, ≤ 0.15 on L-RED's long
  grow/big runs.
  - READING: if the T^R maxima keep I ≈ L/2, then I is of the order of T(d − 1) there, and SLOT-TRADE's needed «I = O(d)» fails on
    exactly the extremal family; the long-run families avoid top-only steps instead. Nothing here kills or proves it: the d ≤ 5
    maxima are too small to tell L/2 from d + 1 (max_d4_L13: L/2 = 4.5, d + 1 = 5).
- Verdict: no lane proof; no kill. The precise open statement is CONJECTURE RENEW-COUNT: on every IDEAL-ACYC run, the lower steps
  that renew a top mover (RENEW's step t − 1) number O(d) (or poly(d), for the polynomial version of SLOT-TRADE).

## 1. Files (experiments/new/box171/)
- frozen.py (per-file I, L, pattern), fsum.py (max I by degree and d), climbI.py (climb on I); log/frozen.txt; out/climbI_*.json.

## 2. Next (for the Lead; this lane parks after this box)
- The decisive data are T^R(5)/T*(5) maxima: their I against L and d + 1 (L-RED's cube driver, d 5). I ≈ L/2 there would make
  RENEW-COUNT the wrong target.
