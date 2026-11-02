# R195 NEST(d) at degree 4, the open point of R191: CLOSED, and at every degree. Proposition NEST-DEAD-ALL (PROVED, lane): for every d ≥ 3 and EVERY degree D, no width-2 IDEAL-ACYC ladder realises NEST(d)'s first 7 steps. The case NEST-DEAD-3 left open (a = u_(d−2) on b's Ξ-chain before q) dies at step 6 by the descendant form of MERGE-1 applied to q; z3: that case + 6 steps UNSAT at d 3 (D 3: 2 s, D 4: 23 s); U at degree 4 stays LINEAR (L-RED successor 46)
Started 2026-11-02 18:46Z (Lead GO 18:37Z; un-parked 19:47Z for queue item (1), date -u). Brief: «R195 = NEST(d) at degree 4 … Either
extend NEST-DEAD to degree 4 (a proof attempt in the NEST-DEAD-3 style, with MERGE-1), or build the escape … Score U against d at
degree 4 … If degree 4 also stays linear, state precisely which lemma caps it.» Labels: PROVED (lane), EXACT (z3), DATA, READING, OPEN.
Model and notation: R191 (width-2 ladders, degree D, option k → W-target 2(l − 1) + (k mod 2); NEST(d) of R189 §2; b = v_(d−2),
q = v_(d−1), p = u_(d−1), a = u_(d−2), c = v_(d−3); desc(x) = movers Ξ-reachable from x). Not a TARGET.md claim. G-N5-TIME OPEN. No
kill, no family.

## 0. Answer
- NEST(d) is dead at every degree: Proposition NEST-DEAD-ALL (§1, PROVED, lane). With R189 NEST-DEAD (step 5 at D = 2) and R191
  NEST-DEAD-3 (step 7 at D ≤ 3), the doubling schedule of R189 §2 is now excluded for all degrees, so the degree-4 key-alone rotation
  (R191 ROT-CAP: k ≤ D − 2) does not rescue it. The obstruction is on the Ξ side, at q = v_(d−1): q is woken alone by p at steps 3 and
  5, and each such wake must move q INTO the set of options whose chain reaches p; q cannot do that twice in a row.
- New lemma: MERGE-1* (descendant form of R191 MERGE-1): if exactly one mover y of desc(x) moves at step t, a comparison of two faces
  of x can change only if exactly one of the two chains contains y, and that face gains. Checked on 53 genomes (1830 order changes):
  0 violations (r195/mergeck2.py).
- EXACT (z3, r191/nestbmc.py LEM=1 PIFIX=4 = the lemma clauses of R193 + the NEST4-SHAPE order): NEST(3) prefix 6 with the shape
  imposed is UNSAT at D 3 (2 s) and D 4 (23 s), as step (B) of the proof predicts; prefix 7 with the shape at D 4: UNSAT
  (exact 21 s, relaxation 11 s). Every climbed 6-step NEST(3) genome (4 at D 3, 3 at
  D 4, the pin nest3_D3_p6) has a π-after q, i.e. lies outside the shape (DATA); the climb with the shape forced stops at 5 (DATA).
- U at degree 4 (§2, DATA): best 9 / 10 / 19 / 18 / 27 at d 3 / 4 / 5 / 6 / 8, linear (≈ 3.5 per level).
- Which lemma caps the degree freedom (READING): R191 ROT-CAP / ROT-BUDGET, moves(x) ≤ (D − 1)(1 + H_x): a fixed degree is a constant
  factor. Compounding needs the Ξ-helps H_x to double along the ladder; for the NEST schedule MERGE-1 / MERGE-1* show the helps cannot
  be arranged (NEST-DEAD-ALL). Other doubling schedules are not covered.
- d 4 exact (R193 fold-in): the second relaxation model (L 13, no LAG, 5391 s) does not lift either (FIX exact UNSAT, 12 s). Bound
  still 12 ≤ max(d 4).

## 1. Proofs (PROVED, lane)
- Lemma MERGE-1*. Let exactly one mover y ∈ desc(x) move at step t (other movers may move). If the order of face(x, k), face(x, k′)
  differs between V_(t−1) and V_t, then exactly one of their chains under s_(t−1) contains y, and that face is the one that gains.
  - Proof. R191 MERGE-1's proof verbatim: the chains of x's faces contain only desc(x) movers, so under s_(t−1) and s_t they agree up to
    y; a chain without y keeps its value; two chains with y keep their difference; one chain with y changes by cur_t(y) − cur_(t−1)(y)
    ▷ 0 (Ξ monotone, R178 (ii)). ∎
- Lemma NEST4-SHAPE (PROVED, lane; any degree). In a run whose steps 1-7 are NEST(d)'s (d ≥ 3), the chain of b's middle option (b, n)
  under s_1 contains a = u_(d−2) before q. In particular π(b) < π(a) < π(q).
  - Proof. R191 NEST-DEAD-3 step (1) (degree-free): (b, n)'s chain contains q under s_1 and not under s_5, so some mover π-between b
    and q on its s_1-prefix moved during steps 2-5; the candidates are c and a (q, b are the ends, p is π-after q by NEST-PI (ii)).
    If c were on it, NEST-DEAD-3 steps (2)-(3) (degree-free: c's move at 5 is woken by q alone at 4, MERGE-1) give a contradiction.
    So the re-routing mover is a. ∎
- Proposition NEST-DEAD-ALL. For every d ≥ 3 and every degree D, no width-2 IDEAL-ACYC ladder has a run whose steps 1-7 move exactly
  NEST(d)'s sets {u_0 … u_(d−1)}, {q}, {b, p}, {q}, {c, a, p}, {q}, {b, p}.
  - Proof. (A) By NEST4-SHAPE, π(a) < π(q); by NEST-PI (i), π(c) < π(q) and π(b) < π(q). So the only mover of desc(q) that moves at
    step 3 (movers b, p) and at step 5 (movers c, a, p) is p.
    (B) Let P := the options of q whose chain contains p. The prefix of such a chain (movers π-between q and p) contains no mover that
    moves at steps 2-5 (those are q, b, p, c, a: b, c, a are π-before q, p is the end), so P is the same under s_2, s_3, s_4, s_5.
    q moves at 4 (w_2 → w_4) and at 6 (w_4 → w_6) and not at 3, 5; only q moves at 4 and at 6, so q's key order is the same at s_3 and
    s_4, and at s_5 and s_6. As in Corollary LAG: w_4 ∈ A_3(q) \ A_2(q) and w_6 ∈ A_5(q) \ A_4(q). By MERGE-1* (only p in desc(q)
    moves at 3, resp. 5): w_4 ∈ P and w_2 ∉ P; and w_6 ∈ P and w_4 ∉ P. Contradiction (w_4 ∈ P and w_4 ∉ P). ∎
  - Remarks. (i) Step 7 is used only to get the shape (A); with the shape, steps 1-6 already die (z3 above). (ii) Outside the shape
    (a π-after q, as in every realised 6-step genome) step 5 wakes q twice (p and a), and MERGE-1* gives nothing; NEST-DEAD-3 kills that
    case at step 7 when D ≤ 3, and NEST4-SHAPE (via c) at every degree. (iii) It kills one schedule, like R189 / R191; doubling
    schedules with longer lags or other interleavings are not covered.

## 2. DATA: U at degree 4 (width 2; r190/delclimb.py SCORE=U, 80,000 mutations, seeds 1 / 2)

| d | U seed 1 / 2 | L seed 1 / 2 | best U |
| --- | --- | --- | --- |
| 3 | 9 / 7 | 12 / 9 | 9 |
| 4 | 10 / 10 | 12 / 12 | 10 |
| 5 | 18 / 19 | 19 / 23 | 19 |
| 6 | 18 / 18 | 22 / 20 | 18 |
| 8 | 27 / 22 | 31 / 24 | 27 |
- Against degree 3 (R191 §3: best 6 / 9 / 16 / 16 / 21) and degree 2 (R190: 10 at d 6): larger constants, same additive growth.
  Champion genome r195/u4_d8.json (d 8, U 27, L 31).
- NEST(3) prefix climbs at D 4 (r191/nestclimb.py): unforced 6 / 6 / 6 (R191 §2); with the shape forced (PI=nest4) 5 / 5.

## 3. OPEN / next
- Doubling schedules other than NEST (e.g. lags of length > 1 between u_l and v_l, or a third mover per level as a clock, R190) at
  degree ≥ 3; a general potential instead of schedule-by-schedule kills; U-LIN (box 144) itself.

## 4. Files
r195/mergeck2.py (MERGE-1* checker), r195/u4_d8.json (degree-4 U champion), r191/nestclimb.py PI=nest4, r191/nestbmc.py PIFIX=4.
Outputs in r195/out (gitignored). check.sh block «R195».
