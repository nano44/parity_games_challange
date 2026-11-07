# R189 The LAG mechanism by hand: lag EXISTS (one lower key flip releases two same-level movers at different steps; lag once per lower carry, twice), but the doubling schedule NEST(d) is DEAD for every d ≥ 3 (Proposition NEST-DEAD, PROVED, lane; z3-exact at d 3): lag releases run FORWARD in the Ξ-order, and the top mover's next face reversal would have to read BACK (L-RED successor 45)
Started 2026-11-02 02:46Z (Lead brief STEP 2, date -u). Brief: «the LAG mechanism by hand (R188 §READING). On the 2-wide IDEAL-ACYC ladder,
build two same-level vertices released by one lower key flip that move at different steps, i.e. Ξ-targets that leapfrog once per lower
carry. L-NEW 47 box 142 is trying to prove NO-LAG at the same time.»
Labels: PROVED (lane), EXACT (z3, machine-checked, not Lean), DATA, READING. Model: the IDEAL model of R178 §1 / P-N5-REALIZE §2 with an
acyclic Ξ-graph (IDEAL-ACYC); every genome here is realised as a real N5 FL run by Theorem REALIZE (P-N5-REALIZE, frozen e609c5d2), and
every pin below is checked that way. LADDER (box 140): movers u_l = 2l, v_l = 2l + 1 at level l, deg 2, option k of a level-l ≥ 1 mover
has W-target 2(l − 1) + k; L_l := the key-smaller of u_l, v_l. π := a topological order of the Ξ-graph (Ξ-edges go forward). Not a
TARGET.md claim. G-N5-TIME OPEN. No kill.

## 0. Answer
- LAG EXISTS, built by hand (§1). lag1 (d 3): the level-0 flip at step 1 moves y1 = u_1 at step 1 and y2 = v_1 at step 2 (y2's new face
  reads y1); the top mover z moves twice (steps 1, 2) on that ONE lower flip. lag1u: the same with y2's face reading the top mover
  (UP-LADDER form): y2 lags, but z moves once (box 140 TOP-STATIC). Both realised: one real FL run each, lemck 0 violations, pinck OK.
- Lag once per lower carry, for two carries (DATA): lag2c_d4 (climb, d 4): the two level-0 flips (steps 3, 8) each release the level-1
  pair at different steps (3 then 4; 8 then 9).
- What does NOT happen: compounding. Lag events per level (climbs scoring lags, 150k mutations, 2 seeds): ≤ 3 at every level for d 3-6
  (§3). The doubling schedule NEST(d) — u_l moves at the flip, the levels above respond, then v_l moves, then they respond again — is
  DEAD for every d ≥ 3 (§2, Proposition NEST-DEAD, PROVED, lane; z3: NEST(3) prefix of 4 steps SAT (one full doubled level-1 response,
  pin nest_d3_L4_n48), prefix of 5 steps UNSAT).
- The obstruction (§2): Lemma LAG-RELEASE (PROVED, lane): a mover that wants an option at step t (by key) but gets it only at t + 1 was
  released by a Ξ-DESCENDANT that moved at step t. So every lag is a forward π-edge. In NEST the lags chain v_(d−2) → v_(d−1) → u_(d−1)
  forward in π, and u_(d−1)'s next face reversal needs a Ξ-descendant that moved after its last move — but only v_(d−2), v_(d−1) moved,
  both EARLIER in π.
- For L-NEW box 142: «NO-LAG» in the literal form (no two same-level movers released by one flip move at different steps) is FALSE
  (lag1, lag2c, nest_d3_L4). The statement the data supports is about RE-REVERSAL after a lag (§4).

## 1. The gadgets (DATA: exact IDEAL runs, realised; hand-made genomes)
- lag1 (r189/lag/lag1.py; genome r189/lag/lag1.json; 6 movers, deg 2, d 3): movers 0 a0, 1 a1 (level 0), 2 y1, 3 y2 (level 1), 4 z,
  5 z′ (level 2; z′ static). Option = (W-target, Ξ-target, gate, β rank:parity):
  - a0: (−, X, 10, 7o), (−, X, 0, 8e), start 0. a1: (−, X, 5, 6e), (−, X, 6, 5o), start 0 (static).
  - y1: P1 (a0, X, 8, 11e), Q1 (a1, X, 7, 10o), start Q1. y2: P2 (a0, y1, 3, 3e), Q2 (a1, X, 1, 2e), start Q2.
  - z: Z1 (y1, X, 2, 9e), Z2 (y2, y1, 4, 4e), start Z2. z′: (y1, X, 9, 1e), (y1, X, 11, 0o), start 0.
  - Run: step 1 moves a0, y1, z; step 2 moves y2, z; then stop («opt»). Why, by hand: at step 1 a0's key drops 10 → 0 < 5 (the lower
    flip, L_0 = a0); y1 has P1 available (11e > 10o) and takes it; y2's P2 = {3e, 10o (via y1 on Q1)} is worse than Q2 = {2e}, so y2
    stays; z takes Z1 (key (0, 8, 2) < (5, 1, 4)). At state 1 y1 sits on P1, so P2 = {3e, 11e} beats Q2: y2 moves at step 2; Z2 =
    {4e, 11e} beats Z1 = {9e}, and key(y2) = (0, 3) < key(y1) = (0, 8), so z moves back to Z2.
- lag1u (lag1 with y2's P2 reading z, Z2 reading X; ranks re-tuned; r189/lag/lag1u.json): step 1 a0, y1, z; step 2 y2 (released by z's
  step-1 move); z cannot follow (its faces are static, TOP-STATIC).
- lag2c_d4 (climb result, r189/lag/lag2c_d4.json, d 4): steps [2,4,7], [5], [0,3], [2], [5,6], [4], [7], [1,2,5], [3]; level-0 flips at
  steps 3 and 8; level-1 lag after each (3 → 2 at step 4; 2 → 3 at step 9). Lag events per level [0, 2, 2, 1].
- nest_d3_L4 (z3 model, r189/lag/nest_d3_L4.json): steps [0,2,4], [5], [3,4], [5] = NEST(3)'s first doubled level-1 response: one
  level-0 flip gives 2 level-1 moves (u_1 at 1, v_1 at 3) and 4 level-2 moves.
- Pins (r189/instances, pins.sha1; built by r187/stab.py; each: lemck 0 violations, startck, Oink --zlk + verify, --tl + verify, xeng):

| pin | n | L_FL | sha1 .pg |
| --- | --- | --- | --- |
| lag1_n48 | 48 | 2 | aed8620b95e0854db3cb679f949e0319b3f33936 |
| lag1u_n48 | 48 | 2 | 4db88f5b00f1b000e06c4e766838e016ccb618df |
| lag2c_d4_n62 | 62 | 9 | c3a530fddb4331cc97af154cea5c2cbc0b09b508 |
| nest_d3_L4_n48 | 48 | 4 | af8c37c98d6f0430f57fc7729451ca21505339a0 |

## 2. Lemma LAG-RELEASE and Proposition NEST-DEAD (PROVED, lane)
- Lemma LAG-RELEASE (IDEAL-ACYC, any genome). Let x be a mover with s_(t−1)(x) = s_t(x) =: c and k an option of x with (x, k) ▷_(s_t)
  (x, c) but not (x, k) ▷_(s_(t−1)) (x, c). Then some mover y ≠ x that is Ξ-reachable from x moved at step t (s_t(y) ≠ s_(t−1)(y)).
  - Proof. The chain of a face (x, j) is (x, j), then (xt, s(xt)), …; every mover on it after x is Ξ-reachable from x, and x does not
    recur (acyclic). If no such mover moved at step t, both chains of (x, k) and (x, c) are the same under s_(t−1) and s_t, so are their
    values and the comparison. ∎ (No monotonicity of values is used. It is box 140's ALTERNATION ingredient, stated per step.)
- Corollary LAG (deg 2). If x moves at step t + 1 to option k, its key order under s_t already preferred k, and x did not move at step
  t, then a Ξ-descendant of x moved at step t. (At step t x chose the key-least option of A_(s_(t−1))(x); it stayed, so k was not
  available at s_(t−1); it is at s_t; apply LAG-RELEASE.)
- Corollary RE-REVERSAL (deg 2). If x moves at step t1 and next at step t2 > t1, some Ξ-descendant of x moved at a step in
  [t1, t2 − 1]. Proof: let x move from k′ to k at t1 and back to k′ at t2. Then (x, k) ▷ (x, k′) under s_(t1−1) and (x, k′) ▷ (x, k)
  under s_(t2−1). If no Ξ-descendant of x moved at steps t1, …, t2 − 1, the two states agree on every Ξ-descendant of x, so both faces
  have the same chains and values under both states, and ▷ would hold both ways. ∎
- The schedule NEST(d) (r189/lag/schedbmc.py nest()): R_l(t) := u_l moves at t, then R_(l+1)(t), then v_l moves at t + D_(l+1), then
  R_(l+1)(t + D_(l+1)); D_d := 1, D_l := 2 D_(l+1); level 0: R_0(1). So L = 2^d, moves per level 2, 4, …, 2^d (a binary counter in which
  each lower flip makes the level above flip twice, with the lag growing downward). For d ≥ 3 its first five steps are: step 1
  {u_0, …, u_(d−1)}; step 2 {v_(d−1)}; step 3 {v_(d−2), u_(d−1)}; step 4 {v_(d−1)}; step 5 {v_(d−3), u_(d−2), u_(d−1)}.
- Proposition NEST-DEAD. For d ≥ 3, no 2-wide deg-2 IDEAL-ACYC LADDER has a run whose steps 2-5 move exactly these sets (step 5 need only
  contain u_(d−1)). Write b := v_(d−2), p := u_(d−1), q := v_(d−1).
  - Proof. Keys of a level-l mover's options depend only on levels < l (TOWARD-L, box 140), and no mover of level ≤ d − 3 moves at steps
    2-4.
    - (1) b moves at step 3 and not at step 2. Its key preference is the same under s_2 and s_3 (levels ≤ d − 3 unchanged), and b was
      not on its new option at state 1 or 2. By Corollary LAG a Ξ-descendant of b moved at step 2; the only mover at step 2 is q. So
      π(b) < π(q).
    - (2) q moves at step 4 and not at step 3. Its key preference is the same under s_3 and s_4 (no mover of level ≤ d − 2 moves at step
      4). By Corollary LAG a Ξ-descendant of q moved at step 3; the movers at step 3 are b and p; b precedes q in π. So π(q) < π(p).
    - (3) p moves at step 3 and again at step 5, not at step 4. By Corollary RE-REVERSAL a Ξ-descendant of p moved at step 3 or 4; the
      movers there are b, p, q; p is not its own descendant and b, q precede p in π. Contradiction. ∎
  - EXACT (z3, r189/lag/schedbmc.py, the R188 bmc3 encoding with the move set of every step fixed): d 2: NEST(2) (4 steps) SAT. d 3:
    prefix 3 SAT, prefix 4 SAT (nest_d3_L4), prefix 5 UNSAT (11 s), the full 8 steps UNSAT. Step-5 variants after the 4-step prefix:
    {v_0, u_1} SAT, {v_0} SAT, {v_0}, then {u_1} SAT; {v_0, u_1, u_2}, {v_0, u_2}, {v_0, u_1, v_2} UNSAT; {v_0}, then {u_1, u_2} UNSAT.
    So the run can go on, but u_2 = p cannot move again until something after it in π moves. d 4 / d 5 prefix 5: z3 runs still going
    at this commit (the proof above covers every d ≥ 3); their outcome is appended when they end.
- What NEST-DEAD does NOT say: it kills one schedule. Other doubling schedules (longer lags, different interleavings, a third mover per
  level as a clock) are not covered; 2-wide is used (the movers at steps 2-4 are exactly b, p, q).

## 3. DATA: lag events per level (r189/lag/lagclimb.py)
A LAG EVENT at level l ≥ 1: a flip of L_(l−1) after which both level-l movers move, at different steps, before the next flip of L_(l−1).
Climb on the 2-wide deg-2 LADDER, acyclic Ξ (forward in a mutable π), score Σ_l 4^l · events_l (then L), 150,000 mutations, 2 seeds:

| d | best L | lag events per level (seed 1) | (seed 2) |
| --- | --- | --- | --- |
| 3 | 6 | [0, 1, 2] | [0, 1, 1] |
| 4 | 9 | [0, 1, 1, 2] | [0, 2, 2, 1] |
| 5 | 12 / 10 | [0, 2, 2, 1, 3] | [0, 1, 2, 2, 2] |
| 6 | 14 / 14 | [0, 2, 2, 1, 3, 2] | [0, 1, 2, 3, 3, 2] |
- The exact d 3 optimum x3_L8 (R188) has [0, 0, 3] and g4_L12 [0, 0, 3, 1]. A counter needs about 2^(l−1) events at level l.
- Flat: no doubling of lag events anywhere (DATA).

## 4. READING (for L-NEW box 142 and the Lead)
- Lag itself is cheap: one Ξ-read of the lagging mover onto its partner (lag1) or onto any mover that moves one step later. NO-LAG as
  «no lag» is false; a NO-LAG statement that could hold has to be about what follows a lag.
- The cost is in π: every lag adds a forward π-edge (Corollary LAG), every repeated move of a mover needs a descendant move in between
  (RE-REVERSAL). A doubling counter needs, at every level, a lagging partner AND a re-reversing head; in the nested schedule the release
  chain v_(d−2) → v_(d−1) → u_(d−1) runs forward and the head's re-reversal must read further forward, where nothing moves.
- A candidate lemma for the proof side (OPEN, not proved): «in the 2-wide LADDER, between two consecutive flips of L_(l−1), at most one
  level-l mover re-reverses after a lag» or a π-potential: the π-position of the last mover released in a window is increasing. Any
  such lemma must allow lag2c (two lags at level 1, one per carry) and nest_d3_L4.
- For the attack side: escaping NEST-DEAD needs a mover after the head in π that moves inside the window. In the 2-wide ladder every
  move is caused by a key flip from below, so that mover must itself be a lagging or re-reversing mover; a third mover per level (3-wide)
  could act as a clock. Not tried here.

## 5. Files (experiments/red/r189/)
- lemck.py (P-N5-REALIZE per-lemma checks), lag/lag1.py, lag/*.json (genomes), lag/show.py (moves per step), lag/trace.py (faces and
  keys per state), lag/lagclimb.py, lag/schedbmc.py (schedule / COUNT z3), instances/ (4 pins + pins.sha1). check.sh block «R189».
