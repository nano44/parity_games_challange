# L6: building the fuel supplier for the seventh level (L-LOWER successor 6, BOX L6)

Box: Lead brief (L-LOWER successor 6; D1 / D14 / D18), BOX L6 «CONSTRUCTIVE TEST of CONJECTURE L5-TYPE»: build the fuel supplier for
the crossed pair 6 of rec/SL41_d28.txt explicitly instead of perturbing SL41. GO 2026-11-07 14:08Z. Written from 14:50Z (date -u).
Labels: PROVED (lane, unrefereed) / CONJECTURE / DATA / DEAD / READING. Every DATA clause names its counter (unit, set, scope).
Nothing here is a result in the sense of CLAUDE.md; G-N5-TIME stays OPEN. Not a TARGET.md claim (§9).

## 0. Instance, notation, tools
- Instance: experiments/lower/l5/rec/SL41_d28.txt (sha1 c1b46c319fd614e5bcb0909b616a9f2833e0dfee, frozen in P-TOWER-FUEL; d 28,
  T 290, F 2 6 14 30 62 126 222 158 …; levels 0-5 capped). Pair j = movers 2j, 2j + 1. Option m = 2x + k: Ξ-target xt[m], β rank br[m],
  parity bp[m] (1 = odd = negative). Model, key c_l = o(l − 1), windows, CROSS, DOMINANCE-FREEZE, CROSS-ECONOMY: docs/lower/L5-rule.md
  §0, §6 and the packet docs/lower/P-TOWER-FUEL.md §2.
- Tools (experiments/lower/l6/): sim6.py (text-genome simulator in Python big integers, written from l5/fev.c's rules; agrees with
  fev on SL41: T 290 and the whole F-profile identical), win.py (J-windows, key, own / parent type, pair-J moves, deciders per step),
  topadd.py (TOP-ADD clock test), cross2.py (CROSS-preserving re-pointing), gad.c (gadget search, §5).
- D := the shared comparison of pair 6 (12 → (22, 11), 13 → (11, 22)); «11b» at a state = the 11-side is better (12 prefers option 1,
  13 prefers option 0); «22b» = the opposite.

## 1. The exact requirement (DATA; win.py → win6_SL41_verbose.out; unit = 6-window; scope = stored start)
- The 48 failing 6-windows come in 15 blocks (one per move «9 → 1» of pair 4, at steps 20, 39, 57, 75, 93, 112, 130, 148, 166, 185,
  203, 221, 239, 258, 276) plus the first windows. Block at 239: W105 [240, 241] key 1 own (11, 1), W106 [242, 243] key 0 own (10, 1)
  (both parent (9, 1)), W107 [244, 245] key 1 own (11, 0) parent (8, 0). 13 is the first mover (key-gated) in every window.
- Needed D along s_239 … s_244 for these three windows to double (pair 6 moves 13 at u₁, 12 at u₁ + 1): 22b, 11b, 11b, 22b, 22b, 11b.
  Present: 22b, 22b, 22b, 22b, 22b, 11b. So exactly two states are wrong per block: s_240 and s_241 must be 11b.
- Because both windows have length 2, the second mover must move at u₁ + 1, so D must turn at s_240 itself: the turn must come
  from a mover that MOVES AT STEP 240, the same step as the b-step (11's move 0 → 1). At 240 the movers are 11, 13, 15, 28; at 242:
  10, 16, 26, 27 (unit = step; set = steps 239-244; DATA). Keys that change at 240: o(5), o(6) only (levels 6, 7); at 242: o(5) … o(8).

## 2. Why no supplier on 22's chain can work: the merge at 22 (DATA, exact chains at s_239, s_240, s_242)
- While 9 is on option 1 and 54 on option 0, 11's option-1 chain is 11:1 (79, −) → 9:1 (87, −) → 54:0 (68, −) → 22:0 (45, +) → 20:0 (91, +)
  → …, i.e. it RUNS INTO 22 and from there coincides with 22's chain. So the symmetric difference of D is only {12:0 (26, +)} vs
  {12:1 (71, −), 11:1 (79, −), 9:1 (87, −), 54:0 (68, −)}: every β on 22's chain cancels. This is the mechanism behind the
  DOMINANCE-FREEZE instance (87, 9, 1) of L5 §6: not a missing supplier on 22's chain, but a merge that hides 22's chain from D.
- Consequences (PROVED, lane; from R105 ENC: only the symmetric difference matters): while 9 = 1, 54 = 0 and 11 = 1, a change of D
  needs a change of 12, 11, 9 or 54, or of a mover inserted on the segment 12:0 → 22, 13:1 → 22, 11:1 → 9 → 54 → 22. 11 and 9 are
  capped-level movers with their own schedules (11 moves at 240 and 244, 9 at 239 and 248); 54 (level 27) moves once in the run.
- DATA (cross2.py → cross2_SL41.out; unit = genome; set = 1,458: both 22-side options (12:0, 13:1) or both 11-side options (12:1, 13:0)
  or the merge link 54:0 re-pointed to each mover Y, with Y's two ranks unchanged or swapped to the two top ranks with all parities;
  scope = stored start): 1,314 acyclic; 5 keep six capped levels, all with F(6) = 222 (Y ∈ {11, 22, 45}: no change of the merge);
  every top-rank swap loses levels 1-5. A CROSS-preserving re-pointing to an existing mover does not supply the fuel.

## 3. TOP-ADD cannot clock a supplier on SL41 without ≥ 5 added levels (PROVED, lane; DATA)
- Lemma TOP-CLOCK (PROVED, lane; R104 movement rule as in fev: a level-l mover, l ≥ 1, moves at step t only to c_l(t) and only if it
  is not already there; o(l) at step t is a function of the new states of pair l and of c_l(t)). Let K(l) be the number of steps at
  which c_l changes and M(l) the number of moves of pair l. Then (a) each mover of level l ≥ 1 moves at most K(l) + 1 times;
  (b) K(l + 1) ≤ K(l) + M(l) ≤ 3K(l) + 2.
  Proof. (a) After a move at t the mover sits on c_l(t); its next move at t′ > t needs s_(t′−1)(x) = c_l(t) ≠ c_l(t′), so c_l changes
  in (t, t′]. (b) o(l) can change at t only if c_l(t) ≠ c_l(t − 1) or a member of pair l moves at t; by (a) M(l) ≤ 2(K(l) + 1). ∎
- On SL41, F(27) = 0, so a TOP-ADD level 28 has K(28) = 0: its movers move at most once; K(29) ≤ 2, K(30) ≤ 8, K(31) ≤ 26, K(32) ≤ 80.
  A supplier must be active at s_240, s_241 and inactive at s_239, s_242 in each of the 15 blocks: ≥ 2 moves per block, ≥ 29 moves in
  all, so it must sit at an added level ≥ 32 (d ≥ 33), with every added level below it moving at its maximum: a five-level clock built
  on top from nothing. DATA (topadd.py → topadd_SL41_K2.out, topadd_SL41_K3.out; unit = genome; set = 200 random TOP-ADD genomes with
  K = 2 and K = 3 added levels, new ranks ≥ 80, two existing options re-pointed to new movers; scope = stored start): the busiest new
  mover moves at most 2 times.
- Consequence for the design: the supplier must sit INSIDE the key cascade (levels ≤ 16, where K(l) ≥ 31: F(15) = 32), and by §1 its
  key must change at step 240 or its preference at s_239: a supplier at a level whose key flips at 240 (levels 6, 7) or a Ξ-mover
  triggered by a move at 239 (9 → 1 itself, or 12 at 239).

## 4. The coupling a supplier must beat (READING, with the exact inequalities on the instance)
- A supplier Z on D's chain enters D only through its current option; Z's own preference compares both of its options. For Z
  inserted on the 22-side (12:0 → Z, 13:1 → Z, Z:0 → 22 with a tiny β: neutral when inactive), with Z:1 → A: «11b at s_240» and «Z
  prefers 1 at s_239» together need v(A) to DROP by more than 2^87 + 2^79 + 2^71 + 2^68 + 2^26 at step 240. A = 11 gives a rise (11's
  option-1 chain passes 20:0 (91, +)); A = 9, 54 do not change at 240. For Z on the 11-side (12:1 → Z, 13:0 → Z, Z:0 → 11), «11b with
  Z = 1» and «Z prefers 0 at s_241» contradict each other at once (both compare against the same 11-chain, which is 2^87 below 22's).
  So a one-mover supplier needs a trigger whose value falls by ~2^87 in the same step as 11's move: a second mover (a delay line of
  length ≥ 1 below the supplier), i.e. the supplier is itself a small clocked circuit.

## 5. Gadget search (running; DATA to follow)
- gad.c: insert ONE new level at position P inside the cascade (old levels P … 27 shift up by one; d 29), with two new movers Z, W:
  Ξ-targets from a candidate list (pairs 4, 5, 7-10 members, 22, 50, 52, 54, 7, 34, 35, 45, Z, W, X), ranks at tiers between the old
  ranks, parities, start bits, the new level's gate order; up to NW re-points of D-chain options (12:0, 12:1, 13:0, 13:1, 11:0, 11:1,
  9:0, 9:1, 22:0, 22:1, 54:0, 54:1) to Z or W. Score = 1000 · min(caps, 6) + good 6-windows (+ 10^5 if F(6) = 254). Annealing.
