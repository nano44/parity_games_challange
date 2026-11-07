# R196 From NEST-DEAD-ALL toward all doubling schedules: Lemma SAME-WAKER (PROVED, lane, any width / degree) kills every schedule in which one mover gets two consecutive single-woken LAG moves from the SAME waker; it does NOT give U-LIN: in all 80 genomes tested, the 162 consecutive single-woken pairs have DIFFERENT wakers (DATA), i.e. the run escapes by alternating wakers on opposite option chains (L-RED successor 46)
Started 2026-11-02 20:31Z (Lead GO (1): «abstract NEST-DEAD-ALL … any schedule in which some level responds TWICE to one lower carry needs
two Ξ-helps from π-distinct movers; show MERGE-1* plus the π constraints forbid the second help … State the exact class it covers. If
it fails, build the schedule that escapes»; date -u). Labels: PROVED (lane), DATA, READING, OPEN. Model: IDEAL-ACYC, any width / degree
(R191 notation; desc(x) = movers Ξ-reachable from x; P_y(x, s) = options of x whose chain under s contains y). Not a TARGET.md claim.
G-N5-TIME OPEN. No kill, no family.

## 0. Answer
- The abstraction works for one class and fails beyond it.
- LAG move: x moves at step t, did not move at t − 1, and the key order of x's options is the same at s_(t−1) and s_t. Then its new
  option was not available at s_(t−2) and is at s_(t−1) (R189 Corollary LAG, any degree). Its WAKERS are the desc(x) movers of step
  t − 1 (non-empty). SINGLE: exactly one waker.
- Lemma SAME-WAKER (§1, PROVED, lane, any width, any degree). Let t1 < t2 be consecutive moves of x, both SINGLE LAG moves with the
  same waker y, and let P_y(x, ·) be the same at s_(t1−2) and s_(t2−2) (no re-routing of the chain prefixes between x and y). Then
  contradiction. So a mover cannot be woken twice in a row by the same single descendant.
- The class it kills: every schedule forcing such a pair. NEST(d) is one (q is woken by p alone at steps 3 and 5 once NEST4-SHAPE
  holds; R195 NEST-DEAD-ALL is the instance). Each kill must also supply the «single» and «no re-route» conditions from the schedule's
  π constraints, as R195 did with LAG-RELEASE (NEST-PI (i)) and NEST4-SHAPE.
- It does NOT give U-LIN / DELAY-LIN. DATA (r196/wakeck.py, 80 genomes: all R188-R195 pins and genomes, every U / RANK climb
  champion at D 2-4, d 3-8): 1166 LAG moves, 760 SINGLE, 162 consecutive SINGLE pairs, SAME 0 (as the lemma says), re-routed 0,
  DIFFERENT wakers 162. The long runs never need the forbidden pair. They alternate wakers.
- The escape shape (READING, exact): from SAME-WAKER's proof, consecutive single wakes by y_1 then y_2 force the middle option o_1 into
  P_(y_1) \ P_(y_2). At degree 2 (x alternates o_0, o_1) this gives y_1 ∈ chain(o_1) \ chain(o_0) and y_2 ∈ chain(o_0) \ chain(o_1):
  the wakers sit on the two option chains, one per side, and may repeat as y_1, y_2, y_1, … So x can move once per move of either
  branch. A doubling of x's moves over its wakers' moves is not excluded by MERGE-1* and π alone; what a proof would have to bound is
  how often the two sides of x's Ξ-fork can alternate, i.e. a global count of alternations along Ξ-forks (OPEN).
- So the exact statement reached: «no IDEAL-ACYC run gives a mover two consecutive single-woken LAG moves from one waker without a
  re-route». That kills NEST at every degree. It leaves every alternating-waker schedule open, including all observed long runs.

## 1. Proof (PROVED, lane)
- Lemma SAME-WAKER. Let x make consecutive moves o_0 → o_1 at t1 and o_1 → o_2 at t2 (t1 < t2), both SINGLE LAG moves with waker y,
  and P := P_y(x, s_(t1−2)) = P_y(x, s_(t2−2)).
  - At t1: x stayed at t1 − 1 with the same key order, so o_1 ∈ A_(t1−1)(x) \ A_(t1−2)(x). The comparison of faces o_1, o_0 flipped
    between s_(t1−2) and s_(t1−1). Only y of desc(x) moved at step t1 − 1, so by R195 MERGE-1*: o_1 ∈ P and o_0 ∉ P.
  - At t2: likewise o_2 ∈ A_(t2−1) \ A_(t2−2), and only y of desc(x) moved at t2 − 1. So o_2 ∈ P and o_1 ∉ P (x is on o_1 at
    s_(t2−2), since t1 and t2 are consecutive moves).
  - o_1 ∈ P and o_1 ∉ P: contradiction. ∎
- Re-routing: P_y(x, ·) can change only if a mover on a chain prefix strictly between x and y (π-between x and y) changes its option
  between the two states. Then the lemma does not apply, and the counter wakeck REROUTE counts it (0 in the data).

## 2. DATA
- r196/wakeck.py on 80 genomes (r191/lag, r192/lag, r188/instances, r189/lag, r195/u4_d8, and the container-local champions
  r191/out/u_d*, r195/out/u4_*, r192/out/rk_*): LAG 1166, SINGLE 760, consecutive SINGLE pairs 162: SAME 0, SAME after re-route 0,
  DIFFERENT 162.
- The committed subset (check.sh «R196»: r191/lag, r192/lag, r188/instances, r189/lag, r195/u4_d8) is reproducible in-tree.

## 3. OPEN / next
- A bound on alternations along Ξ-forks (the escape shape above), e.g. «the number of times x's single wakers switch sides is at most
  the number of moves of the fork's merge part», would be the next candidate lemma. Not attempted.
- Build test: an explicit alternating-waker doubling ladder (two branches feeding one mover alternately) scored by U. Not built.

## 4. Files
experiments/red/r196/wakeck.py. check.sh block «R196».
