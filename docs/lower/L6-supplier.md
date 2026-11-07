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

## 4. Structural lemmas for suppliers (PROVED, lane) and the two couplings on SL41 (DATA)
- Lemma TAP (PROVED, lane; R105 ENC, movement rule). If both options of a mover x have the same Ξ-target (or both exit), x's two values
  differ by β(x, 0) − β(x, 1) only, so x's preference is constant over the run and x moves at most once. Hence a mover that moves twice
  has two different tails, and every comparison whose chain passes x reads x's whole current tail, not one bit: there is no «clean tap»
  (a state-dependent β followed by a common continuation) built from one mover.
- Lemma TRANSPARENT-LEVEL (PROVED, lane; o(l) rule). Insert a level P with members Z = 2P (first), W = 2P + 1, W fixed at 1 (both options
  exit, W:1 of higher rank, start 1) and gates with g(1) = 1. Then o(P) = c_P whenever Z = 0 (split: o = (0 ≠ c) = c) and o(P) = 1 when
  Z = 1 (joined at 1). So the level is transparent iff Z = 1 only while c_P = 1; a key-gated Z (it moves only to c_P) keeps this iff it
  prefers 0 whenever c_P drops while Z = 1. DATA (ins.py; unit = genome; set = SL41 with an idle level inserted at P = 6 and P = 7, two
  gate choices each; scope = stored start): T 290 and every old level's F unchanged; the new level copies its key's F (126 resp. 222).
- Coupling 1, RETURN-CHAIN into a capped level (DATA): 12 is upstream of pair 5's mover 10 (10:0 → 55:0 → 12; the only movers upstream of
  pair 6 are 10, 27, 55). 10's comparison is decided via 12's current tail in 120 + 32 of 291 states (deciders (81, 11, 0) ×72, (79, 11, 1) ×48
  through 12:1 → 11, and (91, 20, 0) ×32 through 12:0 → 22; dropscan_SL41.out last line); unit = state; scope = stored start. So any change of 12's tails is a change of
  level 5's fuel. DATA (copyf.py → copyf_SL41_12_13.out; unit = genome; set = 900: one option of 12 re-pointed to 13 («copy of f»,
  12 reads the first mover's state), with either option of 13 re-ranked to any tier and parity; scope = stored start): all 900 lose
  every capped level (F(0) = 0). 13 has no predecessor: its options can be changed freely (re-ranking either β of 13 to any tier keeps
  six capped levels in many cases, F(6) = 222 in all; DATA, same scope).
- Coupling 2, the RANK-LOCK of a single key-gated supplier (PROVED, lane, with the exact SL41 values of §2). Let R be one new mover at an
  inserted transparent level P = 6 (key c_6 = o(5): it rises at 240 and falls at 242, the ideal clock), R:0 → the old target (neutral
  when idle, β(R, 0) = β₀), R:1 → T (β(R, 1) = β₁). R must move to 1 at 240 (prefer 1 under s_239), make D 11b at s_240 and s_241, and move
  back at 242 (prefer 0 under s_241); v22 is constant on s_239 … s_241, and v22 − v11 = 2^91 − … at s_239, 2^87 + 2^79 + 2^68 at s_240, s_241.
  (a) R on the 22-side (12:0, 13:1 → R; R:0 → 22). «Prefer 1 at s_239» is β₁ + v(T)_239 > β₀ + v22; «11b at s_240» is
      2^26 + β₁ + v(T)_240 < −2^71 + v11_240. Together: v(T)_239 − v(T)_240 > 2^87 + 2^79 + 2^71 + 2^68 + 2^26 + β₀ − … : T's value must DROP by
      more than 2^87 in step 240. DATA (dropscan.py → dropscan_SL41.out; unit = mover × block; set = the 51 movers not upstream of 12, 13 (upstream: 10, 12, 13, 27, 55)
      × the 15 blocks; scope = stored start): no mover drops by more than THR at the step after «9 → 1» in any block; the large changes are
      rises (15 and 28, the movers that move at 240, rise by 2^96-2^97 in every block; 11 by 2^91). So T must be a new mover that moves at 240 too. At level 6 it would be W, which sits at 1 and can only move to
      c_6(240) = 1 (no drop by a move); at level 7 its key o(6) is the split indicator of pair 6 (1 at 240, 0 at 241 once 12 has moved),
      so T returns at 241 and D is 22b at s_241: 12 moves back at 242 together with 13 (a double move: o(6) does not flip twice). DEAD for
      one supplier with one helper at levels 6-7.
  (b) R on the 11-side (12:1, 13:0 → R; R:0 → 11). «11b with R = 1 at s_241» needs v(R:1)_241 > v22 + 2^71; «prefer 0 at s_241» needs
      β₀ + v11_241 > v(R:1)_241; so β₀ > v22 − v11_241 + 2^71 = 2^87 + 2^79 + 2^71 + 2^68: the idle β₀ has rank ≥ 88 and sits on the 11-side
      of D at every idle state. DATA (unit = good 6-window; set = the 79 good windows of SL41; scope = stored start): in 63 of the 79 a
      move of pair 6 reads D at a decider of rank < 88 (most common pairs (84, 79) ×16, (79, 95) ×8, (81, 101) ×8, (101, 84) ×8, (79, 96) ×7), so
      a fixed element of rank ≥ 88 in D freezes D over those windows and kills them (DOMINANCE-FREEZE (a)). DEAD.
  (c) The general shape (READING): the element that makes a key-gated supplier WANT TO LEAVE at s_241 must either be visible to D at s_241
      (then D is 22b at s_241: the supplier's own leaving signal cancels its effect) or sit on its idle side (then it is a constant
      offset on D at every idle state). This is the lock; it is what (a) and (b) compute on SL41.

## 5. Gadget searches (DATA; gad.c, gad2.c; two simulators agree: gad's fev core and sim6.py give identical T and F on every frozen
## best genome)
- gad (one inserted level at P ∈ {7, 8, 9}; Z, W options: Ξ-target from 19 candidates + Z, W, X, rank at 32 tiers among the old ranks,
  parity; start bits; gate order; NW ∈ {2, 3} re-points of the D-chain options 12:0, 12:1, 13:0, 13:1, 11:0, 11:1, 9:0, 9:1, 22:0, 22:1,
  54:0, 54:1 to Z or W; score 1000 · min(caps, 6) + good 6-windows; simulated annealing, 3·10^6 steps × 4 runs; unit = genome; scope =
  stored start): best 95 good 6-windows of 127 (SL41: 79) at P = 7, 8 with six capped levels; F(6) ≤ 222 in every best genome.
- gad2 (as gad plus free edits of 12's and 13's options (target any mover, rank tier, parity), the gate order of level 6, and P = 0 (no
  inserted level) or P = 6 (directly below pair 6, key o(5)); 3·10^6 steps × 4 runs and 4·10^6 steps × 3 runs at P = 6, all completed (gad_runs.out; one
  NW = 4 run discarded: no acyclic start)): the same plateau,
  95 good windows; F(old 6) ≤ 222; P = 0 with edits of the options of 12, 13, 54, 11, 9 only: no genome better than SL41 itself.
- Frozen best: rec/GAD95_P8_d29.txt (sha1 d0de3499043d47ba6930b0d0fda323f8eb1e123c; d 29; T 289; F 2 6 14 30 62 126 220 158 159 …; 6
  capped; win6_GAD95.out: 32 failing 6-windows = two per (9, 1) block + the first ones). Its gadget: 12:0 and 13:1 → Z = 16 (CROSS kept),
  Z:0 → 10 (rank 41, +), Z:1 → old 20 (rank 90, −). It repairs the third window of each block (13 stays in phase) but not the two
  windows under parent (9, 1): 12 still never moves there. DATA (negative), not a cap: annealing over a structured space, not exhaustive.

## 5b. How the capped levels of the records fuel their second mover (DATA, for the rule question)
- tight.py → tight_records.out (unit = J-window with two staggered pair-J moves; set = H5 J = 4, H6 J = 4, 5, SL41 J = 5, 6; scope =
  stored start; H5 is l4/rec/H5_d20_F62.json through l4/j2t.py, sha1 of the text 5968fe42…): at the TOP capped level the decider of
  the second mover q under s_(u2−1) is the FIRST mover f's own option, moved at u1 (H6 J = 5: 62 of 63 windows, 31 key-gated + 31 Ξ;
  SL41 J = 5: 47 of 63). Below the top (H5 J = 4, H6 J = 4) the decider's mover did not move in the window (the turn comes from a change
  of the chains' shape, the CROSS mechanism).
- readpath.py → readpath_records.out (same unit; q's moving option followed until f): H6 J = 5: q 10 reads f 11 directly (10 → 11) in 31
  of 63 windows; SL41 J = 5: 10 → 55 → 12 → 11 in 31 of 63, i.e. pair 5's read path runs THROUGH pair 6's member 12; SL41 J = 6: 12 never
  reads 13 (79 of 79 good windows «no f»). READING: the top capped level is fuelled by «q reads f» («copy of f»); SL41's level 6 cannot
  copy that without re-routing 12, and 12 carries level 5's read path (§4 coupling 1). A rule G_h → G_(h+1) would have to provide, for
  the new top pair, a read path q_h → f_h that does not pass through a mover on q_(h−1)'s read path, or re-route q_(h−1)'s read path.
  CONJECTURE (READ-NEST, untested): this is the missing step; a test is a construction of SL41′ with 10's read path re-routed around 12.

## 5c. After the milestone (Lead 15:53Z routing): READ-NEST by hand, the climb predicate, the GAD95 xcheck
- xcheck (l3/xcheck.py against L-NEW box150 Gen and box187 movescheck, L-NEW tree claude/l-new a8555576; xcheck_GAD95_SL41.out; unit =
  run; set = GAD95_P8_d29 (d 29), SL41_d28; scope = stored start): SIM-MISMATCH 0, every movescheck counter 0. With gad's fev core and
  sim6.py, GAD95 is checked by three simulators.
- READ-NEST, by hand (readnest.py → readnest_SL41.out; unit = genome; scope = stored start; DATA):
  - Step 1, re-route 10's read path around 12: every single re-point of 55:0 or 10:0 to another mover or X (112 genomes, 109 acyclic)
    loses a capped level except 10:0 → 12, which still reads 12. So 10's fuel needs 12's state itself (RETURN-CHAIN x₂_5 ← 12), not
    any other single relay.
  - Step 2, 12 reads 13 (12:1 → 13 or 12:0 → 13) on SL41 and on the one kept re-route, with either option of 13 re-ranked to 57
    tiers × 2 parities: 912 genomes, all acyclic, all with 0 capped levels.
  - Step 3, PARALLEL 13 (13:0 → 22, 13:1 → 11, so that 10 → 55 → 12 → 13 reaches the original target whenever pair 6 is joined) with
    12:1 → 13 and both options of 13 re-ranked (20 tiers × 2 parities each): 1,600 genomes, all with 0 capped levels.
  - Mechanism: the stored start has pair 6 joined at 1, so 12:1's new tail changes v(12) at s_0; the run diverges from SL41 at step 1
    (movers 10, 12, 27, 28) and stops at T = 3. Parallel 13 moreover moves the fuel need to 13 (it must prefer c before each b-step,
    i.e. D must still turn once per window, now by the window's end): under (9, 1) D is 22b on s_239 … s_243, so 13 cannot open W105.
  - CONJECTURE READ-NEST: DEAD on SL41 in these families (single re-route of 10's path; 12 reads 13 with any re-rank; parallel 13). It
    is not tested on a different lower tower.
- Climb predicate for L-COMP (Lead routing (b); guard_l6.py, importable, pure): guard(D, mode) with mode «nomerge91» (no pre-state of a
  6-window under parent (9, 1) at which the chain of A_1's current option passes A_0 or vice versa, pair 6 crossed onto (A_0, A_1)),
  «pulse3» (PULSE_5 ≥ 3 in every 5-window of type (9, 1)) or «either». DATA (unit = genome; stored start): SL41_d28: merge pre-states
  64 in all 6-windows, 45 under parent (9, 1); PULSE_5 min 2 under (9, 1): fails all modes. G7_best_d28: no merge, PULSE_5 min 1:
  passes «nomerge91», so the predicate must be combined with the room condition (slack.py H = 7: 0 violations at levels 1-5) and
  GUARD 0-5. Seed: rec/SL41_d28.txt (sha1 c1b46c31…).

## 5d. The «48 of 127» plateau across four genomes (Lead 16:31Z question; DATA + READING)
- struct48.py → struct48.out (unit = genome; scope = stored start; genomes: SL41_d28 c1b46c31…, G7_best_d28 b995fff2…, and L-SI 42's
  claude/l-si 38f08152 experiments/si/box80/out/climb_s2_snapshot.txt (sha1 0d67617919cc830d791a256a2e232cb6d9f4ab41) and
  climb_w1_P0.json (sha1 622f68e5783e16eddc47e6b46d2bc65071af88cd; read as text through l4/j2t.py)): all four have levels 0-5 capped,
  F(6) = 222 and the SAME level-6 move profile: 79 windows with one move of each of 12, 13; 16 with only 12; 16 with only 13; 16 with
  no move (48 failing of 127).
- Pair 6 is crossed in SL41 and G7_best only; in snapshot and w1 it is NOT crossed (12:0 → 13: 12 reads 13 directly, in 48 of the 79
  good windows, readpath.py). So «≥ 48 failing whenever levels 0-5 are capped and level 6 is crossed» does not describe the plateau:
  the plateau occurs without CROSS, and with the «copy of f» read that READ-NEST asked for.
- Common to all four (DATA): pair 5's second mover 10 is graph-upstream of 12 (its Ξ-closure reaches 12: RETURN-CHAIN), and 11 is not.
  In no capped record (H5, H6, SL41, G7_best) is a capped pair crossed.
- READING (information flow; not proved): for level 6 to double, 12's preference must change once per 6-window, in step with o(5),
  which for the reachable states of a doubling level 5 is 1 exactly between the moves of 11 and 10 in a 5-window: it needs s₁₀.
  If 10 is graph-upstream of 12, no Ξ-chain read by 12 can pass 10 (acyclicity), so s₁₀ can reach 12's comparison only through
  movers keyed by o(5) or later keys (13, levels ≥ 7) or through proxies in the lower pairs' states. CONJECTURE RC-PLATEAU: if levels
  0-5 are capped and 10 is graph-upstream of 12, then F(6) ≤ 222. Role form (Lead 16:44Z; replaces the mover names): in a genome of
  𝓛^R_d (d ≥ 7) with levels 0, …, 5 capped, let q₅ be the member of pair 5 that moves second in its 5-windows (one member, by DOUBLE-EQ
  (E5)); if there is a Ξ-path (any options) from q₅ to a member of pair 6, then F(6) ≤ 222 (= 2^8 − 2 − 32). General form, to be
  tested before any proof: with levels 0, …, j − 1 capped, a Ξ-path from q_(j−1) into pair j forces F(j) < 2^(j+2) − 2.
  Guard for the test: guard_l6.py mode 'noreturn' (role-based: q₅ from the run; npaths(D, q₅, pair 6) = 0 and levels 0-5 capped) and
  score(D) = (min(caps, 6), −npaths(q₅, pair 6), F(6)), lexicographic. DATA (unit = genome; stored start): no record with levels 0-5
  capped meets it (SL41, G7_best, snapshot, w1: npaths 1; H6: 8; H5 has 5 capped levels, npaths 2). SL41's single path is
  10:0 → 55:0 → 12, and none of the 112 single re-routes of 10:0 or 55:0 keeps six capped levels (readnest.py step 1), so a seed needs
  ≥ 2 edits. Test proposed: a climb that forbids the RETURN-CHAIN (guard: 10 not
  graph-upstream of 12, 13) while keeping levels 0-5 capped; a genome with F(6) > 222 kills the conjecture, and a plateau at ≤ 222
  supports it.

## 6. The D18 analogy used, and its test: synchronous circuits (register vs combinational paths; carry-lookahead)
- Dictionary (READING). A Ξ-preference is a REGISTER: a mover's move at t uses its preference under s_(t−1), one clock of delay. The
  key cascade is the only COMBINATIONAL path: within one step c_l = o(l − 1) is computed bottom-up from the new states (a ripple-carry
  chain). A j-window of length L is a clock budget: the second mover must move by u₁ + L − 1, so its fuel path may contain at most L − 1
  registers. In SL41's (9, 1) blocks L = 2 (PULSE_5 = GAP_5 = 2 = h − j for h = 7, j = 5, the tight case of GAP-NEST / PULSE-NEST), so
  the fuel path for 12 has ZERO registers: a SETUP-TIME constraint. Its only legal sources are the combinational ones (key-gated movers
  at levels whose key flips at 240: levels 6, 7) or a register loaded at 239 from the level-5 b-step (9 → 1).
- Carry-lookahead (the classical fix for ripple delay): predict the carry from lower bits. Here the level-5 b-step types cycle (8, 0),
  (9, 0), (8, 1), (9, 1) (DATA: parents of W99 … W107 in win6_SL41_verbose.out; a Gray-code walk of the two members of pair 4), so «the
  next level-6 window is under (9, 1)» is predictable from (s_8, s_9) = (1, 0) one window early. Test (design, READING + DATA): a lookahead
  supplier needs a mover y that goes «off» before the (9, 1) block (reading s_8 = 1, s_9 = 0) and «on» in the same step as R (240). By
  TAP y has two different tails and by the lock of §4 (c) y's own leaving/arming signal is visible to whatever reads y; with y read by R,
  y's arming element enters R's comparison and, when R is active, D. The gad / gad2 spaces contain such wirings (W reading 8 or 9, Z
  reading W, ranks at all tiers), and the annealing found none above the 95-window plateau. So the analogy's prediction («a lookahead
  path fixes the setup violation») FAILS here, for a reason the analogy does not have: in a circuit a gate reads a wire's bit; here a
  path reads the whole downstream sum (TAP), so a lookahead wire carries the weight of everything it reads.

## 7. Outcome of BOX L6 (labels as stated)
- Success criterion (seven capped levels, F(6) = 254) NOT met. No genome with F(6) > 222 and six capped levels was found by any designed
  construction or gadget search in this box.
- The exact reason, at the instance (SL41_d28, sha1 c1b46c31…), in four parts: (i) MERGE (DATA, §2): under parent (9, 1) 11's chain runs
  into 22, so D's difference is {12:0} vs {12:1, 11:1, 9:1, 54:0}; no supplier on 22's chain can act. (ii) TOP-CLOCK (PROVED, §3): a TOP-ADD
  supplier on SL41 needs ≥ 5 added levels before it can move 29 times. (iii) SAME-STEP (DATA + movement rule, §1): the two windows have
  length 2, so D must turn at s_240 by a mover moving at step 240. (iv) The two couplings (§4): 12 feeds capped pair 5 (RETURN-CHAIN
  10 → 55 → 12), and a single key-gated supplier on either side of D is RANK-LOCKED (PROVED with the instance's values; DATA counters as
  stated): 22-side needs a 2^87 drop at 240 that no mover has; 11-side needs an idle offset of rank ≥ 88 that freezes 63 good windows.
- CONJECTURE L5-TYPE: not confirmed and not refuted. What this box adds against its simple form: on SL41 the fuel for the new level
  cannot be one supplier per type placed on the crossed pair's chains; any supplier must come with at least one helper whose own
  signal is hidden from D, and such hiding is not available from single movers (TAP). A constructive test therefore needs either a
  different lower tower (one where the (9, 1) chain does not merge into 22, or where PULSE_5 ≥ 3 under (9, 1), giving the fuel a register)
  or a multi-mover gadget outside the searched spaces.
- H5 → H6 repeat: NOT RUN (it was conditional on a working construction).

## 8. Files (experiments/lower/l6/)
sim6.py, win.py, topadd.py, cross2.py, copyf.py, ins.py, dropscan.py, tight.py, readpath.py, readnest.py, guard_l6.py, struct48.py, gad.c, gad2.c;
outputs struct48.out, readnest_SL41.out, xcheck_GAD95_SL41.out, tight_records.out,
readpath_records.out, dropscan_SL41.out, win6_SL41_verbose.out, cross2_SL41.out,
topadd_SL41_K2.out, topadd_SL41_K3.out, copyf_SL41_12_13.out, win6_GAD95.out, gad_runs.out; rec/GAD95_P8_d29.txt.

## 9. Diff against TARGET.md
No statement mentions a parity game, a winning region, an algorithm's running time or a complexity class; all are about the IDEAL
model's step sequence (R104's definition) on 𝓛^R_d and its F-profile. Not M3, not a gauntlet step.
