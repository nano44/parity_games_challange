# L10: the inductive rule STRETCH-AND-STACK, and level 8 by hand (BOX L10, L-LOWER successor 10; GO from the Lead 07:02Z 2026-11-08)
Labels: PROVED (lane, unrefereed) / CONJECTURE / DATA / DEAD / READING. Every DATA clause names its counter (unit, set, scope).
Model and notation as docs/lower/L7-design.md §0, L8-design.md §0 and L9-design.md (R104 IDEAL rules; pair j = movers 2j, 2j + 1;
f_j = 2j + 1, q_j = 2j; c_j = o(j − 1); j-window = maximal run of steps with c_j constant). Nothing here is a result in the sense
of CLAUDE.md; G-N5-TIME stays OPEN. Not a TARGET.md claim (§9).

## 0. Instances and tools (experiments/lower/l10/)
- HIT7: experiments/lower/l9/rec/LCOMP_L6_HIT7_F254_d28.txt, sha1 6a3b274d3af4d0d8f057f82c8f2919c84b7dd446 (= L8 §1g, L9 §0).
- stretch.py: the minimal pure STRETCH of a run (difference constraints, longest path). stmap.py: the stretched core target on the
  new time axis. need.py: the retrigger bill of the stretch. trig.py: trigger map (who changed on a mover's chain at the step
  before its move). Simulators: l6/sim6.py and l9/fenc.c (exact for d ≤ 64).
- out/target_HIT7_H8.txt: the stretched core target of §1 (states of movers 0-13 per step, idle steps marked). The first print
  (sha1 e031533adca196a246625ecc54b98a8f438380f2, commit 1802a93f) is BROKEN, see §1c. The corrected print has sha1
  90b3b0f9bc0125463315122b6378e906890f1cb5.

## 1. The inductive rule (item 1)
### 1a. Two exact facts the rule rests on
- Lemma STRETCH (PROVED, lane; okeys in sim6 / R104). For l < h, o(l) at a state is a function of the states of pairs 0..l only.
  Hence F(0), …, F(h − 1) of a run depend only on the sequence of DISTINCT consecutive states of pairs 0..h − 1. Inserting steps at
  which no mover of pairs 0..h − 1 moves (idle steps) leaves F(0..h − 1) unchanged, so it keeps every cap below h. ∎
- Lemma ROOM-TIGHT on HIT7 (DATA; stretch.py; unit = core step; set = the 289 steps of HIT7's run at which a mover of pairs 0-6
  moves; scope = stored start). Give each core step t a new time τ(t), strictly increasing, subject to P-TOWER-FUEL Lemmas 2, 3 at
  h = 8 (PULSE_j ≥ 8 − j and GAP_j ≥ 8 − j for j = 1..6, every two o(6) changes ≥ 2 apart, the first at τ ≥ 2). The least τ has
  T′ = 510 = 2·255, the Lemma 3 lower bound, met exactly. It inserts one idle step in 219 of the 289 gaps, and none elsewhere.
  On the new axis (stmap.py) the 7-windows have lengths 2 (254) and 3 (1). 219 idle steps lie right after an o(6) change (the
  second step of a 7-window); the other 2 are the tail. F(0..6) of the target = 2 6 14 30 62 126 254 (re-measured).
  The same minimal stretch for h = 7 needs T′ 259 on HIT7's own pairs 0-5, 254 on SL41 and 256 on H6 (DATA, same tool).
- The retrigger bill (DATA; need.py → out/need_HIT7_H8.out; unit = (idle step, mover of pairs 0-6); set = the 219 idle steps;
  scope = the stretched target). At an idle step the core is unchanged. So a core mover that is free there and moves at the next
  step must have its preference flipped by a NON-core mover on its chain that changes AT the idle step. Every idle step needs
  ≥ 1 such retrigger: 177 need exactly 1, and 42 need 2.
  | mover | 12 (q6) | 10 (q5) | 11 (f5) | 9 (q4) | 4, 6 | 8 | 3 | 5 | 13 |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  | retriggers | 127 | 63 | 24 | 23 | 7 each | 4 | 3 | 2 | 1 |
  So q6 must be retriggered in all 127 6-windows (= L8 §4's «PULSE_6 = 2»), and q5 in all 63 5-windows. Free-and-holding movers at
  idle steps (they must NOT flip): out/need_HIT7_H8.out, e.g. mover 3 155, 6 118, 4 117, 9 101, 10 89.

### 1b. CONJECTURE STRETCH-AND-STACK (the rule G_h → G_(h+1); stated for h ≥ 7, instance h = 7 → 8)
Given a capped G_h (levels 0..h − 1 exact) at d with run S, build G_(h+1) at d + 4 as follows.
- (R1) ROOM target. The core (pairs 0..h − 1) follows σ(S), the minimal stretch of S under Lemmas 2, 3 at h + 1 (§1a). On HIT7 this
  is out/target_HIT7_H8.txt: T′ = 510, one idle step after 219 of the o(6) changes.
- (R2) New pair h. f_h is key-fired at the first step of every h-window and q_h moves at the second step. Since every h-window of
  σ(S) has length 2 (one has length 3), q_h moves exactly at the idle steps. Wiring as in HIT7's top pair (q6 = 12 reads f6 = 13
  with a one-step lag; trig.py: 126 of 127 q6 moves have wait 1, triggered by 13).
- (R3) FUEL from the new pair. At every idle step i, o(h) flips (q_h moves), so every mover of level h + 1 whose preference already
  points to the new key moves at i (key-fired, no trigger needed). Each retrigger event (x, i) of the bill is supplied by such a
  key-fired mover y (level h + 1 or above, keyed through o(h)), placed on x's chain. By ONE-READ XOR (L8 §3, PROVED) x cannot read
  the phase from two movers alone, so between x and y sits a context SELECTOR σ_x (level ≥ h + 2). σ_x routes x's chain to y in
  the idle steps where x must move, and to a non-moving branch where x must hold. This is HIT7's τ / σ / ρ form (L8 §1g: τ = 17,
  σ = 23, ρ = 19), now with the trigger moved INTO the lower levels' chains. For q_(h−1) the bill is 2^h − 1 events, one per
  (h − 1)-window: the selector must separate «first idle step of the window» from «second» (q_(h−1) is not free in the second).
- (R4) Caps. Levels 0..h − 1: by Lemma STRETCH, kept if the realized run projects onto σ(S). Level h: capped iff pair h moves
  twice in every h-window, which R2 prescribes (windows of length ≥ 2: f at the first step, q at the second).
- (R5) Size. d(h + 1) = d(h) + 4 (DATA, three points: H5 d 20, H6 d 24, HIT7 d 28), T(h + 1) = 2·(2^(h+1) − 1) when σ is tight
  (HIT7 → 510, measured).
- What is CONJECTURED: that R1-R3 are realizable in the IDEAL model with 4 added levels, i.e. that the 261 retrigger events
  (h = 8) can all be routed through key-fired movers of levels ≥ 8 and selectors without breaking the free-and-holding movers.
  Not claimed: anything asymptotic; that σ(S) stays tight for every h; that the selectors fit in 4 levels.
- What would refute it at h = 8 (the level-8 build, item 2): a retrigger event whose mover has no admissible selector route
  (ranksolve infeasibility core on the clamped target) that persists under every re-wiring of the levels ≥ 8.

### 1c. Correction and addendum after L-RED 58's attack (R224, relayed by the Lead 07:38Z; appended 07:4xZ, date -u)
- CORRECTION (DATA). stretch.py bounded the first o(6) change by τ ≥ 2. That leaves the first 7-window ONE step long ([1, 1]), and
  pair 7 cannot double in it (L-RED: Lemma 1 E1, E3, E4). My «lengths 2 (254) and 3 (1)» counted states from s_0, not steps; in
  steps the first print has 1 (1), 2 (253), 3 (1), as L-RED measured. Fix: the bound is τ ≥ 3, and the last window gets exactly its
  second step (stretch.py, now in the repository). Re-measured (unit = 7-window, in steps; set = all 255; scope = the
  corrected target): all 255 windows have length 2 (L-RED's experiments/red/r224/out/target_fix.txt at claude/l-red ebae21d5, sha1
  12642daa…, equals my print in all 511 data lines; only the header comment differs, hence the different sha1); T′ = 510; 221 idle steps (steps 1 and 2 before the first core move; 219 after
  an o(6) change); retrigger bill unchanged (need.py runs on the stretch, not the print). The
  frozen print is replaced (sha1 90b3b0f9…, §0). The level-8 build target build.core8 was ALREADY correct: it prepended one idle step
  to the old print and cut the last tail step. Its file out/core8_HIT7.txt (sha1 c6e19673…) is regenerated byte for byte by the
  corrected tools (core8 no longer prepends). So the item-2 searches started 07:19Z ran on the right target.
- R2 exception: at idle step 1, f7 makes its first move (the first 7-window is steps 1-2: f7 at 1, q7 at 2). So the idle steps are
  even except step 1 (DATA: 220 even, 1 odd; the 219 bill-carrying ones all even), and q7 moves at every even step.
- ADDENDUM to R3 (L-RED Lemma PARITY-8, PROVED, lane L-RED; checked here on the target: o(7) changes at every step). With every
  7-window two steps long, c8 = o(7) flips every step. So a level-8 mover can move only to 1 at odd steps and only to 0 at even
  steps. A pair-8 supplier that changes at an even idle step therefore also makes an odd «shadow» move before its next supply. L-RED
  counts ≥ 217 such moves, ≥ 147 of them right before an idle step at which every free core mover must hold. R3 is revised to
  (R3′). Each retrigger at idle step i comes from q7 itself (it moves at every even step, and is the one non-trivial essential
  input of 10 core movers, §2b), from a pair-8 mover whose odd shadow moves are absorbed (they flip no free core mover), or
  from levels ≥ 9. The item-2 search already enforces this. It clamps only pairs 0-7 and simulates pair 8 by the genome's own
  rules, and the constraint set holds every free core mover at every step, shadow steps included. A score-0 genome therefore
  has its pair-8 alternation built in.

## 2. The level-8 target at d 32, and what any realization must contain (item 2; PROVED parts + DATA)
### 2a. The target
- build.core8 (DATA, re-measured; unit = step; scope = derived from HIT7, sha1 6a3b274d): §1's stretched core with ONE idle step
  prepended and the last tail step cut. Without that step the first 7-window holds only step 1, and pair 7 cannot move twice in it.
  Then pair 7 is added: f7 = 15 moves to c7 = o(6) at the first step of every 7-window, and q7 = 14 at the second step. The gates
  of level 7 are set to joined value 0 (1028 1029 1030 1031; the seed's 1029 1031 1028 1030 has joined value 1).
  Result: T = 510; o(6) changes at 3, 5, …, 509 and o(7) at every step; F(0..7) = 2 6 14 30 62 126 254 510, an 8-capped core
  trajectory, tight (T = 2·255).
- q7's required preference at its free pre-states equals o(6) at that pre-state in 509 of 510 (the miss is step 1), and f7's
  equals 1 − o(6) in 254 of 255 (DATA; unit = free pre-state of the mover; scope = the target).
### 2b. Reader tables (DATA; readers.py, minset.py, essential.py → out/essential_H8.out; unit = free pre-state of the mover, initial
step dropped; set = all of them; scope = the target, core = movers 0..15)
- y is ESSENTIAL for x if the states of all core movers except x and y do not determine x's required preference. Every x of
  2..15 has its required preference determined by all core states. Essential sets:
  | x | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 (q6) | 13 (f6) | 14 (q7) | 15 (f7) |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  | essential | 3 | 1 2 14 | 2 5 7 14 | 14 | 4 5 7 14 | 6 | 14 | 6 7 8 14 | 8 11 14 | 10 14 | 13 14 15 | 12 14 | none | none |
- For 14: every determining core set contains 15 or both 12 and 13 (all core except {15, 12}, resp. {15, 13}, do not determine);
  the only consistent single reader is 15, and the pair (12, 13) is XOR. For 15: symmetrically 14, or both 12 and 13.
  No pair of core movers determines 9, 10, 11, 12 (minset.py: 12 needs 3 = {13, 14, 15}; 9, 10 none up to 4).
### 2c. Lemma HELPERS-EVERYWHERE (PROVED, lane; from the tables of 2b, R104 / R105: pref_x is a function of the states of the
movers in closure(x); acyclic wiring)
- Statement. In every realization of the level-8 target (any d, wiring, ranks, signs, gates and helper behaviour), the closure of
  EVERY mover 2..15 contains a helper (a mover of level ≥ 8).
- Proof. Let H = core movers whose closure contains a helper. If x ∉ H, closure(x) ⊆ core, so every essential y of x lies in
  closure(x), and y ∉ H (closure(y) ⊆ closure(x)).
  (1) 12 ∈ H: else 13 ∈ closure(12) and 13 ∉ H, so 12 ∈ closure(13), a cycle.
  (2) 14 ∈ H: else closure(14) ⊆ core holds a determining set: 15, or 12 and 13; 12 is excluded by (1), so 15 ∈ closure(14)
  and 15 ∉ H; then closure(15) holds 14 (a cycle) or 12 (excluded by (1)).
  (3) 15 ∈ H: closure(15) ⊆ core would hold 14 or 12, both in H.
  (4) 14 is essential for 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, so these are in H; 2 (essential 3) and 7 (essential 6) follow. ∎
- Reading. q7 is the clock: it is the only core mover that changes at the idle steps, so every mover that must act differently at an
  idle step and the step after it needs q7 in its closure; q7 itself cannot read the phase from pair 6 without a third input. This
  extends L7 §7 («helpers needed», h = 2, d = 2 only) to the level-8 target. It does NOT say how many helpers, or at which levels.

### 2d. The exact-target search (method; running at the time of writing)
- Score of a d 32 genome: movers 0..15 are clamped to the target, and the helpers follow the genome's rules (l7/clamp.runclamp). All
  constraints of the full trajectory (l7/ranksolve.constraints) are collected, and l10/gsolve.py (a greedy decision list that
  tolerates errors) counts the violations. Score 0 ⇔ the exact greedy (ranksolve, complete for this form) succeeds ⇔ the genome
  with the solved ranks REPRODUCES the target, so it has 8 caps by construction (re-checked by sim6 + fenc before any report).
  Ranks and signs are solved, not mutated; the search is over wiring, helper gates and helper starts (plus rank swaps for the helper
  dynamics). Unlike L-COMP's LJ climbs, the target is fixed and exact (tight, T 510).
- ann.c: a C port (128-bit chain masks, ENC). It agrees with anneal.py on the seed (score 1286, 7,351 constraints; unit =
  constraint) and on a C-saved genome (825 = 825). Seed = L-COMP's seed_HIT7_d32 (frozen rec/seed_HIT7_d32.txt, sha1 ad9a39d4).
  Core target file out/core8_HIT7.txt (sha1 c6e19673cbda12ba2ec8f7e70da4436cab8ed922).

### 2e. What the key-fired first movers must compute, and where the search stalls (DATA + READING; 08:0xZ, date -u)
- DATA (unit = free pre-state of the mover; set = all of them; scope = the target build.core8): the required preference of f_j
  equals 1 − o(j − 1) at the pre-state (i.e. «leave the current key») at:
  | mover | 15 (f7) | 13 (f6) | 11 (f5) | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  | agree / free | 254 / 255 | 128 / 129 | 44 / 139 | 261 / 322 | 67 / 112 | 90 / 105 | 271 / 300 | 112 / 115 | 269 / 282 | 365 / 370 | 226 / 229 |
  So f7 and f6 are exactly «not my key» except at one initial step each (step 1 for f7, step 3 for f6: a hold inherited from HIT7's
  first window). In HIT7's lower levels the first mover of a pair is not always the odd one; the table lists the raw movers.
- READING. o(j − 1) is a nested XOR over pairs 0..j − 1 (split: [q ≠ key], joined: the gate value). A chain realizes it only as a
  branching program with selectors (ONE-READ XOR), which needs copies of the lower movers' states. Together with 2b this gives the
  dependency loop the search keeps hitting: f6 needs pairs 0..5 (or q6 and q7, through the one initial hold); pairs 0..5 need q7
  (essential, 2b); q7 needs f7 or pair 6; f7 needs q7 or pair 6; pair 6 contains f6. Helpers must cut this loop, and a helper
  that carries the clock or the pair-6 phase without reading 13 can get its timing only from keys (o(7) flips every step).
- DATA (search; unit = violated constraint; scope = the exact target; runs from seed ad9a39d4). C1 (T 1.5): 1286 → 180 at 07:58Z.
  Movers 9, 10, 12, 14, 15 at 0 violations; the rest is on f6 (64 = all 63 moves 0 → 1 plus 1), f5 (11) 32, f4 (8) 35, 4 19,
  others ≤ 8. In C1 helper 18 carries f6's required preference at all 128 free pre-states, and 16, 17, 19 at 127. But all four
  read 13, so f6 cannot read them (every re-pointing of f6 to them is cyclic). The search instead made f6 a near-sink with a
  constant preference. In C4 (cold restart from C1) f6's options both exit, every other mover reaches 13, and f6 has nothing left
  to read. This is the local optimum: f6 is sacrificed.
- Test running: C5 is the same search with the order constraint «movers 0-11, 14, 15 must not reach 13» (ann.c optional argument).
  So f6 may read pairs 0-5 and q7 / f7, and the clock and the pair-6 information must come through helpers.

### 2f. Item 2 outcome so far: no 8-capped genome; the exact obstruction (DATA; 08:4xZ, date -u)
- Search result (unit = violated constraint; set = the constraints of the clamped full trajectory, about 11,000-13,000 depending on
  the helper runs; scope = the exact target out/core8_HIT7.txt):
  - unconstrained runs from seed ad9a39d4: C1 (T 1.5) 1286 → 169; C2 (T 3) → 210 (stopped 08:0xZ); C3 (T 6) → 344 (stopped);
    C4 (T 0.7, from C1's 07:58Z best) → 167;
  - order-constrained C5 («0-11, 14, 15 must not reach 13») → 554, far worse.
  - The plateau since ~08:20Z is ~167-170 in every unconstrained run.
- Frozen best: rec/L10_C4_best_score167.txt, sha1 b550bc4a1d67ace2c0b60d371bdc3222e4f69870. With gsolve's ranks it is
  rec/L10_C4_best_score167_solved.txt, sha1 57454ff800ee4d396da1a5fc9127433dd724dac4.
  Violations by mover (out/viol_C4_best.out): 13 (f6) 64, 8 35, 11 (f5) 31, 4 10, 6 8, 7 8, ≤ 3 elsewhere; 9, 10, 12, 14, 15 at 0.
- What a non-zero score means: the solved genome run freely (sim6; fenc agrees, T 5) leaves the target at the first violated
  constraint. Here that is step 3, movers 13 and 15; the run dies at T 5 with caps 0. The score measures distance to an exact
  realization; it does not give a partial tower.
- THE OBSTRUCTION, measured (target lines 0-8, unit = state):
  - Pair 6 starts at 11 with key o(5) = 0, so f6 is free from step 1. In HIT7 it moved at step 1.
  - The two idle steps that R224's correction prepends (needed so the first 7-window has two steps) make f6 HOLD at steps 1-2
    and move at step 3. That needs a trigger at step 2, a mover on f6's chain that changes at step 2 (q7 moves there).
  - Everywhere else f6 must prefer «not my key» (= 1 − o(5); 2e). Every mover that carries that signal in the runs (helpers 16-19
    in C1) reads 13.
  - So f6 needs, below itself in the DAG: (i) a one-shot step-2 trigger and (ii) a copy of 1 − o(5). Neither may depend on f6. Every
    unconstrained run gives up instead: f6 becomes a sink with a constant preference (64 = all its 0 → 1 moves violated). Forcing
    the order (C5) leaves the rest of the tower without the information it needs (score 554).
- Status: the level-8 build at d 32 is NOT achieved (DATA, this search); not DEAD (a heuristic search, not exhaustive).
  CONJECTURE STRETCH-AND-STACK stays open. The exact sub-problem the next attempt must solve is the f6 gadget above.

- C5 dissected at 08:39Z (rec/L10_C5_order_snap0839.txt, sha1 362b793820e80be72f5e12ba36138a2ec4a7cd87; out/viol_C5_snap0839.out;
  score 553; unit = violated constraint). Here q7 (14) is the one sacrificed: 252 violations, about half its constraints, because
  q7 needs o(6) and may not reach 13. f6 drops to 41; q5 86, q4 52, f5 40. So the loop f6 → pairs 0-5 → clock q7 → pair 6 ∋ f6
  (2e) is where every run fails: cutting it at any link sacrifices the mover at the cut. READING: a cut needs an idle-step clock
  for pairs 0-5 that does not reach 13. That means a helper oscillator driven only by the key timing o(7) (which flips every
  step): a hidden helper counter below the core in the DAG order. Not built.

- Final bests (runs ended 09:2x-09:33Z; unit = violated constraint; scope = the exact target; both files carry level-7 joined-0 gates):
  - C4: 144. rec/L10_C4_final_score144.txt, sha1 9e7b99d40e199dac6cf262f491d6d0a8f16ab417; solved ranks
    rec/L10_C4_final_score144_solved.txt, sha1 42fef4dd0aa98242653858acff192878e90a2d5f. Violations: f6 (13) 64, 8 35, 4 10, 6/7 8,
    f5 (11) 7, ≤ 4 elsewhere. Free run T 4, caps 0.
  - C5 (order-constrained): 538. rec/L10_C5_order_final.txt, sha1 0cf9a48ef18151c74ba92cdbb11902e663338b58; solved ranks
    rec/L10_C5_order_final_solved.txt, sha1 b0997bc7248fd8c761ee7e27b5bea0fb99fd1c37. Violations: q7 (14) 250, q5 62, q4 53, f6 49,
    f5 40. Free run T 2, caps 0.
  - C1 ended at 169; C6 (T 0.5 from C4 at 09:00Z) at 151.
  - The obstruction is unchanged: f6 is sacrificed when the order is free, and q7 when the order is forced.

## 9. Diff against TARGET.md
No statement mentions a parity game, a winning region, an algorithm's running time or a complexity class. All are about the IDEAL
model's step sequence (R104's definition) on 𝓛^R_d and its F-profile. Not M3, not a step-4 pass, not a TARGET.md claim.
