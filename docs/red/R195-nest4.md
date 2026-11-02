# R195 NEST(d) at degree 4, the open point of R191: NEST-DEAD-3's proof breaks at exactly one place (a = u_(d−2) may lie on b's Ξ-chain before q), no contradiction found in that shape, no escape found either (climbs: NEST(3) prefix 6 unforced, 5 in the forced escape order); U stays LINEAR at degree 4 (best 9 / 10 / 19 / 18 / 27 at d 3 / 4 / 5 / 6 / 8) (L-RED successor 46)
Started 2026-11-02 18:46Z (Lead GO 18:37Z, date -u). Brief: «R195 = NEST(d) at degree 4 … Either extend NEST-DEAD to degree 4 (a proof
attempt in the NEST-DEAD-3 style, with MERGE-1), or build the escape … Score U against d at degree 4 … If degree 4 also stays linear,
state precisely which lemma caps it.» Labels: PROVED (lane), DATA, READING, OPEN. Model and notation: R191 (width-2 ladders, degree D,
option k → W-target 2(l − 1) + (k mod 2); NEST(d) of R189 §2; b = v_(d−2), q = v_(d−1), p = u_(d−1), a = u_(d−2), c = v_(d−3)).
Not a TARGET.md claim. G-N5-TIME OPEN. No kill, no family.

## 0. Answer
- Not decided. NEST-DEAD-3 does not extend as it stands, and no degree-4 realisation of NEST(d)'s first 7 steps was found.
- Where the proof breaks (PROVED, lane: everything below except the last bullet holds at every degree):
  - NEST-PI (i), (ii) and NEST-DEAD-3 steps (1), (3) are degree-free. So for a run whose steps 1-7 are NEST(d)'s:
    - the chain of b's middle option (b, n) contains q at state 1 and not at state 5;
    - c = v_(d−3) is NOT on its state-1 prefix before q (NEST-DEAD-3 (2)-(3) apply verbatim to c).
  - Hence (Lemma NEST4-SHAPE, PROVED, lane) a = u_(d−2) lies on that prefix: π(b) < π(a) < π(q) < π(p). The chain of a's old option
    contains q at states 1-4, the chain of a's new option (step 5) does not at state 5, and a's move at 5 is not woken by q alone (c
    moves at 5, so a's key order may change). MERGE-1 gives nothing there.
  - At D ≤ 3 this shape is excluded by NEST-PI (iii) (ROT-CAP: p's moves at 3, 5, 7 need a desc(p) move at 5 or 6, i.e. a after p).
    At D = 4, p's moves at 3, 5, 7 can be key-alone with p visiting all four options, and NEST-PI (iii) is not forced.
- DATA (search):
  - r191/nestclimb.py d 3, D 4: unforced 6 / 6 / 6 (3 seeds × 300,000, R191 §2); with the NEST4-SHAPE order forced (PI=nest4:
    v_0 … v_(d−2) < a < q < p < other u; 2 seeds × 400,000): 5 / 5. The forced order is HARDER for the climber, not easier.
  - U climbs at degree 4 (r190/delclimb.py SCORE=U, width 2, 80,000 mutations, seeds 1 / 2): see §1. Linear, ≈ 3.5 per level.
- Which lemma caps the degree-4 freedom (READING, the precise statement): R191 ROT-CAP. Per Ξ-help a degree-D mover makes ≤ D − 1
  moves (≤ D − 2 of them key-alone), so ROT-BUDGET moves(x) ≤ (D − 1)(1 + H_x) at every degree. A fixed degree multiplies by a
  constant and cannot compound. Compounding needs H_x itself to double along the ladder (Ξ-side helps), which is what NEST-DEAD /
  NEST-DEAD-3 kill at degree 2 / 3 for the NEST schedule. At degree 4 that last step is OPEN; the data show no escape.

## 1. DATA: U at degree 4 (width 2)

| d | U seed 1 / 2 | L seed 1 / 2 | best U |
| --- | --- | --- | --- |
| 3 | 9 / 7 | 12 / 9 | 9 |
| 4 | 10 / 10 | 12 / 12 | 10 |
| 5 | 18 / 19 | 19 / 23 | 19 |
| 6 | 18 / 18 | 22 / 20 | 18 |
| 8 | 27 / 22 | 31 / 24 | 27 |
- Against degree 3 (R191 §3: best 6 / 9 / 16 / 16 / 21 at d 3 / 4 / 5 / 6 / 8) and degree 2 (R190: 10 at d 6): larger constants, same
  additive growth.

## 2. OPEN / next
- Close or escape the NEST4-SHAPE case. A proof would need a contradiction from a's two moves (1, 5) with a's old chain through q and
  its new chain avoiding q, combined with b's second move at 7 (whose new option's chain contains q at state 5, MERGE-1 at step 6).
- An exact check: r191/nestbmc.py LEM=1 at D 4 with the NEST4-SHAPE order (not run; at D 3 the prefix-7 runs timed out).

## 3. Files
r191/nestclimb.py PI=nest4 (forced NEST4-SHAPE order). Outputs in r195/out (gitignored).
