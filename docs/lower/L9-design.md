# L9: level 8 at d 32 (BOX L9, L-LOWER successor 9; GO from the Lead 02:06Z 2026-11-08)
Labels: PROVED (lane) / CONJECTURE / DATA / DEAD / READING. Model and notation as docs/lower/L7-design.md §0 and L8-design.md §0
(R104 IDEAL rules; pair j = movers 2j, 2j + 1; c_j = o(j − 1); j-window = maximal run of steps with c_j constant).

## 0. Instances and tools (experiments/lower/l9/)
- HIT7: frozen copy rec/LCOMP_L6_HIT7_F254_d28.txt, sha1 6a3b274d3af4d0d8f057f82c8f2919c84b7dd446 (= L8 §1g copy, = relayed);
  lifted to d 32 by lift.py (4 inert top pairs: options to the exit, ranks 112-127, constant preference = start) as
  rec/HIT7_lift_d32.txt, sha1 c76bd8c90824b52db36a801af7e8d9e2fa63c92f: T 299, F identical on levels 0-27, 0 on 28-31.
- fenc.c: a second simulator for any d ≤ 64. It decides each preference by ENC (the option of largest rank in chain(x, 0) △
  chain(x, 1)) and needs no big integers, so it is independent of sim6.py (Python big-integer sums). It agrees with sim6 and fev on
  HIT7, SL41, H6 (T and the whole F-profile, and MV).
- DATA (out/fev_vs_fenc_d32.out; unit = genome; set = 1): l5/fev.c is NOT valid at d ≥ 32. It sums ±2^rank in a signed __int128,
  and rank 127 overflows. On HIT7_lift_d32 fev reports F(31) = 1, while sim6 and fenc report 0: inert mover 63's rank-127 option
  is read as negative. From d 32 on, the two lane simulators are sim6.py and fenc.c.
  L-COMP's rclimb30.c uses 192-bit values (claude/l-comp, box30), which is not affected.
- win6.py (6-window move profile), gaps.py (o(l)-gap histograms), slack.py (PULSE-NEST / GAP-NEST room conditions for H capped levels).

## 1. What an 8th capped level needs, measured on HIT7 (PROVED part + DATA)
- PROVED (P-TOWER-FUEL Lemmas 2, 3, PULSE-NEST and GAP-NEST, with h = 8; WINDOW-CAP, L7 §2). With levels 0-7 capped:
  - every j-window has PULSE ≥ 8 − j and GAP ≥ 8 − j (1 ≤ j ≤ 6);
  - every gap between consecutive changes of o(6) (and the first and the last) is ≥ 2, so T ≥ 2·255 = 510.
  The §4 recipe of L8 («keep movers 0-13, HIT7's run plus PULSE_6 = 2», T ≈ 299 + 127) checks only the PULSE half at j = 6. It
  misses GAP at j = 6, and both conditions at j = 4, 5.
- DATA (slack.py, gaps.py; unit = j-window, or o(6)-gap; set = all windows; scope = stored start; out/slack8_HIT7.out, gaps_HIT7.out):
  | j | need (8 − j) | windows | PULSE < need | GAP < need | PULSE values | GAP values |
  | --- | --- | --- | --- | --- | --- | --- |
  | 1-3 | 7, 6, 5 | 3, 7, 15 | 0 | 0 | | |
  | 4 | 4 | 31 | 15 | 0 | 3 (15), 4 (8), 5 (8) | 5 (11), 6 (19) |
  | 5 | 3 | 63 | 63 | 27 | 2 (63) | 2 (27), 3 (27), 4 (8) |
  | 6 | 2 | 127 | 127 | 90 | 1 (127) | 1 (90), 2 (27), 3 (9) |
  HIT7's 6-windows (o(5)-gaps; o(5) is a function of pairs 0-5 only) have lengths 2 (91), 3 (27), 4 (9), summing to 299. Each
  6-window holds two o(6) changes, and these must be ≥ 2 steps apart, also across window boundaries. So the 6-windows average
  ≥ 4 steps, and the run of pairs 0-5 itself must be stretched from 299 to ≥ 510 steps.
- Counting convention (Lead 02:20Z reconciliation). On HIT7, o(6) flips already at step 1, so the first 7-window holds only s_0 and
  no step: length 0. The 255 7-windows are therefore 1 of length 0, 218 of length 1 and 36 longer (gaps.py: hist (0, 1), (1, 218)).
  A length-0 window admits no change of o(7), so it is a violation as well: 219 violations in all. L-COMP 12's n1_7 = 218 counts the
  length-1 windows only, and both counts are right for what they count. A level-7 cap needs both removed: the first o(6) flip at a
  step ≥ 3, and no length-1 window. My 02:11Z «127 + 90 = 217» counted only gaps between consecutive flips, missing the last window
  [299, 300) and the empty first one.
- Exact obstruction to L8 §4 as written (PROVED by the counting above). No construction that keeps HIT7's trajectory of movers 0-11
  (with any change at levels ≥ 6) reaches F(7) = 510. At least 211 steps must be inserted into the run of pairs 0-5. At each
  inserted step a free lower mover must hold although under the same pair-0-5 state it moved in HIT7, so its chain must read a
  mover (necessarily of level ≥ 7) that changes at that step. That is §1d's need (i), now at levels 4, 5 and 6.
- The same pattern one level down (DATA, out/slack7_H6.out, slack7_SL41.out; same units). H6 (6 caps) against seven levels:
  - j = 4: 15 PULSE violations; j = 5: 63 PULSE and 9 GAP violations. So 7 caps could not be added to H6 directly.
  - SL41 (L-LOWER 5's room climb from G7_best, P-TOWER-FUEL §4 «I-FUEL») has 0 violations at j = 1-5, and HIT7 descends from it.
  READING: the 7th level came in two stages, ROOM (re-time the lower levels until Lemmas 2, 3 hold) then FUEL (the triggers of
  pair 6, L8 §1g). The 8th needs the same two stages, with a larger ROOM deficit: 322 violations at j = 4-6, against 87 at j = 4-5
  for H6 → 7.

## 2. Delay maps: how each capped level waits (DATA; delays.py; unit = move of a mover of pairs 1-6; set = all moves; scope = stored start)
- wait w := t − (the last step ≤ t at which the mover's key c_l changed). So w = 0 means key-fired, and w ≥ 1 means the mover held
  while free and its preference turned at step t − 1 (PULSE-TRIGGER). Full tables: out/delays_HIT7_SL41_H6.out.
  | genome (caps) | top capped level: f, q | one below: f, q | two below: the two members |
  | --- | --- | --- | --- |
  | H6 (6) | level 5: 11 {0: 31, 1: 32}, 10 {1: 31, 2: 32} | level 4: 8 {0: 30, 3: 1}, 9 {2: 15, 3: 14, 4: 1, 6: 1} | level 3: 7 {1: 11, …}, 6 {6: 7, 7: 4, …} |
  | SL41 (6, room for 7) | level 5: 11 {0: 31, 1: 31, 3: 1}, 10 {2: 31, 3: 31, 5: 1} | level 4: 8 {0: 8, 1: 15, 2: 7, 6: 1}, 9 {4: 15, 5: 8, 8: 7, 12: 1} | level 3: 7 {0: 11, …}, 6 {6: 7, 8: 4, …} |
  | HIT7 (7) | level 6: 13 {0: 126, 1: 1}, 12 {1: 126, 2: 1} | level 5: 11 {0: 15, 1: 47, 5: 1}, 10 {2: 15, 3: 47, 7: 1} | level 4: 8 {0: 8, 1: 15, 4: 7, 9: 1}, 9 {4: 15, 5: 8, 8: 7, 13: 1} |
- READING. Going from 6 to 7 caps (H6 → SL41 → HIT7), the waits of each lower level moved toward those of the level below it in the
  smaller tower. In H6 the top capped level (5) has q waiting 1-2; in HIT7 level 5 has q waiting 2-3 and the new top level (6) has
  q waiting 1. SL41, the ROOM stage, already had level 5 at 2-3: the lower levels were re-timed before level 6 was fuelled.
- What 8 caps need (PROVED: Lemmas 2, 3 with h = 8; f key-fired assumed for the reading): at level 6, q waits ≥ 2 in all 127 6-windows
  (HIT7: 1), and the pair-5 move that closes a 6-window comes ≥ 2 steps after q₆ (HIT7: 1 in 90 windows). At level 5, PULSE ≥ 3 in
  all 63 windows (HIT7: 2) and GAP ≥ 3 (HIT7: 2 in 27). At level 4, PULSE ≥ 4 (HIT7: 3 in 15). Each extra unit of wait needs a
  trigger: a mover of the waiting mover's closure that changes at the step before its move.
- CONJECTURE SHIFT (lane; DATA = the three genomes above, two transitions, one of them H6 → HIT7 through SL41; not a mechanism).
  An (h + 1)-capped tower from an h-capped one re-times every capped level j ≥ 2 so that its wait profile takes the place of
  level j + 1's profile in the h-tower, and puts the new top level at (f 0, q 1). In the tight form (the binary counter with every
  first mover key-fired) q_j waits 2^(h−1−j) in an h-tower. SL41 and HIT7 are not tight: T 290 and 299 against the lower bound 254.

## 3. The counter target is sched.py's sequential target; which alpha patterns are capped (DATA + READING)
- The tight form of §1 is a binary counter. Every first mover is key-fired and q_l moves one step after the last move of the levels
  above. That is l7/sched.py's sequential target, the one the L8 §2 helper searches (hsched*, hsat) were run on (Lead 02:13Z question:
  yes, it is the same target). So the inductive question «level h + 1 from level h» is exactly: for which d is sched(h, α) realizable,
  and how does the least d grow with h.
- DATA (sched.py, all α ∈ {0, 1}^(h−1) for h = 2..5, plus α = (0, …, 0) for h = 6..8; unit = target; scope = the stored schedule):
  - the target is capped (F(l) = 2^(l+2) − 2 for l < h) iff α_(h−2) = 1 (h ≥ 3): 2 of 2 at h = 3, 4 of 8 at h = 4, 8 of 16 at h = 5;
  - with α_(h−2) = 0 it has F(h − 1) < cap and idle core steps (all-zero α: F(h − 1) = 12, 26, 56, 118, 244, 498 for h = 3..8, and
    h − 2 idle steps). The loss comes from the initial nested windows (sched.py starts every pair joined at 1 with key 0).
- Consequence for L8 §2. At h = 3 only α = (α₁, α₂) ∈ {(1, 0), (1, 1)} (strings «1,1,0», «1,1,1») are capped targets. The h = 3,
  d = 4 «NONE in all four α» row therefore matters only for a110 and a111. Their status from STATUS_at_park.txt:
  - a110: UNSAT by hsat, DRUP NOT VERIFIED in default mode;
  - a111: UNSAT by 4 cubes, not DRUP-checked.
  So «h = 3 needs d ≥ 5» is NOT verified (a101, the one DRUP-verified instance, has an uncapped target). The h3d5 runs now go
  through sat_capped.sh (the 8 capped instances only: a110, a111 × gate cases 0-3); the a100/a101 runs of sat_all.sh were stopped
  at 02:5xZ (no cube decided).

## 4. The phase argument for the counter target (Lead 02:46Z decision (a))
- Setting: a realization of a capped sched(h, α) target (§3). Pairs 0..h−1 follow the target (f_l = 2l + 1, q_l = 2l, joined gate
  value 0); helpers are the movers of levels ≥ h.
- Lemma UPPER-BLIND (PROVED, lane; sched.py's job/init recursion, R104 keys). At every move pre-state of q_l (l ≥ 1), the core movers
  above level l are in the same state: pair l + 1 is joined at 1 and every pair k ≥ l + 2 is joined at 0.
  Proof. In sched.py q_l moves at e₁ + 1, where e₁ is the end of job(l + 1, ·). That job ends with every pair above l joined at its
  key (each job moves q_k to c_k after the jobs above it end). At that pre-state pair l is split, so c_(l+1) = o(l) = 1. Each pair
  k ≥ l + 1 is joined, so o(k) = 0 (joined gate value) and c_(k+1) = 0. ∎
  DATA check (phase.py → out/phase_sched.out; unit = two consecutive moves of one mover; set = all q_l of the capped targets
  h = 3 (two α), 4 (two α), 5, 6, 7): 0 pairs with any difference above l.
  For key-fired first movers (α_l = 0) the same holds at their move pre-states, except in windows touched by sched.py's initial
  nesting (DATA: 14 of 307 consecutive move pairs differ above l, all at the start; e.g. h 5, l 2, moves 15 and 25).
- Lemma PHASE-DAG (PROVED, lane; Lemma 4 (b) of P-TOWER-FUEL, UPPER-BLIND, acyclicity). In such a realization, take l ≥ 1 and two
  consecutive moves of q_l. dec(q_l) differs at their pre-states, so closure(q_l) contains a mover whose state differs there, and by
  UPPER-BLIND that mover is f_l, a core mover below level l, or a helper. If α_l = 0 the same holds for f_l (outside the initial
  windows), with q_l in place of f_l. Since the wiring is acyclic, f_l ∉ closure(q_l) or q_l ∉ closure(f_l). So for at least one
  member of each doubling pair, the alternation of its preference is witnessed only by movers below level l or by helpers. The pair's
  own phase c_l = o(l − 1) = [q_(l−1) ≠ f_(l−1)] is an XOR of two lower movers (when pair l − 1 has a key-fired f), which no
  two-input reader computes (ONE-READ XOR, L8 §3).
- What this does NOT give. It does not prove that helpers are needed: lower core movers do differ between consecutive move
  pre-states in every case (DATA, same file, column «below»), and a three-input reader can be a selector. The exhaustive h = 2,
  d = 2 result (L7 §7: 0 of 5,941 wirings) is still the only proof that helpers are needed, and only at h = 2.

## 9. Diff against TARGET.md
No statement mentions a parity game, a winning region, an algorithm's running time or a complexity class. All are about the IDEAL
model's step sequence on 𝓛^R_d and its F-profile. Not M3, not a step-4 pass, not a TARGET.md claim.
