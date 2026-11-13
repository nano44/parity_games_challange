# R244: PAIR-ON-TOP (R243 §2) — the scheduling stall, its smallest instance (N = 10), and k = 3 at d = 5 with a hill profile (DATA + two lane lemmas + READINGS; no kill, no cap lemma)
L-RED successor 70 (session_01V5yGRVqzUx6dwT71TpkK6X, Fable 5.2 xhigh), D1 / D18 / D21 / D25. Lead brief 11:20Z + conditional go 11:29Z. Written 2026-11-13T12:15Z (date -u).
Candidate under attack: QUIET-KEY-1P / SW-POLY on 1P(G) (claude/l-new a143d406, docs/new/N5-QUIETKEY-box217.md §1-§7, A6′). Labels: PROVED (lane, unrefereed),
DATA (counter, set, scope named), READING (mine, not proved), CONSTRUCTION (instance with a checked run). Nothing here is a RESULTS entry or a TARGET.md claim.
**G-N5-TIME stays OPEN; SW-POLY stays OPEN (neither killed nor proved); no genome with k ≥ 8; no rule with three growing members.**

## 0. Answer
- **Step 1 of PAIR-ON-TOP fails in every neighbourhood screened (DATA, exact, own C engine pair244, every candidate simulated in full).** On H5PLUS_L5
  (k 6, d 20, N 41; F = mover 40, pair (A, B) = (8, 9)): one added level-5 mover y plus a re-wiring of B's two Ξ-targets with at least one = y:
  4,628,736 candidates, 1,560,896 Ξ-acyclic, 832 keep the block (levels 0-4 at 1, 3, 7, 15, 31 and sw(F) = 63); best stagger KF = 30 of the 126 a
  staggered full pair needs, no better than the control with B untouched (56,448 candidates, best KF 30, there with sw(y) = 63). (k, d, N) after
  step 1: unchanged (6, 20, 41); the best candidates are (6, 20, 42) with no key supply for level 6.
- **B is rigid (DATA, room244).** Re-wiring B's two Ξ-targets over exit + existing movers: 1,681 candidates, 841 acyclic, exactly 1 keeps the block:
  the original (6, 12). ROOM1 = ROOM2 = 1 in the base run: B moves one step after F's last arrival at A, so no second level-5 mover can visit A
  between F and B (KF ≤ 30 follows).
- **Smallest instance of the same failure (CONSTRUCTION + DATA).** LAD_d5_k3_s13 (experiments/red/r244/inst, sha1 e6ef4b0d6d6c9ba98d40c83f00ee727c911fd5b6):
  a 2-per-level ladder with k = 3 at d = 5, N = 10, T 14, per-level best switches 1, 3, 7, 7, 3; found by a blind climb (lad244, seed 13, at
  evaluation 27,272,611); N5 itself (L-NEW one217.py --check, n5v spec on Γ3): key 14 = n5 14, mism 0, control ONE217_CTRL=1 fires (mism 1);
  Howard 6, seq 6. On it (F = 5, (A, B) = (3, 2)): control best KF 4 of 14; joint screen 77,440 candidates, 13,824 acyclic, 304 intact, best KF 4;
  B rigid (1 of 36 acyclic re-wirings keeps the block), ROOM1 = ROOM2 = 1.
- **Fuel at the low end (DATA).** (k, d, N) = (3, 5, 10) here (the Lead's scratch value N = 10 reproduced by an independent engine and checked on N5),
  against the towers' d = 4k. The profile 1, 3, 7, 7, 3 is a HILL: rates double up to the top of the full block and halve above it (§3).
- Blind climbs do not get further (DATA): d 5: seeds 11, 12 stop at k 2 after 150,000,000 evaluations each; d 7 (annealing): 4 seeds × 100,000,000, k 2.
  Seeded lifts of the k = 3 instance to d 7 (two new levels on top / above the block, 1.5e9 evaluations each) were running when this was written; see §5.

## 1. Two lane lemmas (PROVED lane; model 1P(G) of box 217 §6.1, degree-2 mover x with options a, b)
Notation: κ_t(x) := the key-least option of x under s_t (unique, box 217 Lemma 0 (a)); ξ_t(x) := the Ξ-better option of x under s_t (unique, Lemma 0 (c)).
**Lemma C (C-ELEMENT).** s_(t+1)(x) = κ_(t+1)(x) if κ_(t+1)(x) = ξ_t(x), and s_(t+1)(x) = s_t(x) otherwise.
Proof. A_t(x) = {s_t(x)} ∪ {k : Ξ_t(x, k) > Ξ_t(x, s_t(x))} = {s_t(x), ξ_t(x)}. If ξ_t(x) = s_t(x), A_t(x) is a singleton and x stays; the formula gives
s_t(x) in both cases. If ξ_t(x) ≠ s_t(x), A_t(x) = {a, b} and the rule picks the key-least option under s_(t+1), i.e. κ_(t+1)(x): equal to ξ_t(x), x moves
to it; equal to s_t(x), x stays. (κ_(t+1)(x) reads s_(t+1) at lower levels only, so the rule is well defined level by level.) ∎
So every degree-2 mover is a Muller C-element of a key comparison read with lag 0 (new state) and a value comparison read with lag 1 (old state):
it moves when both agree on the other option and HOLDS otherwise.
**Lemma VL (VALUE-LAST EXACTNESS).** Let x hold c̄ on states τ₀ − 1, …, τ − 1, move to c at step τ, and be key-ready on the whole interval (κ_t(x) = c
for τ₀ ≤ t ≤ τ). Then ξ_t(x) = c̄ for τ₀ − 1 ≤ t ≤ τ − 2 and ξ_(τ−1)(x) = c; and (if τ₀ ≤ τ − 1) some mover on the Ξ-path of xt(x, c) under s_(τ−2) switches
at step τ − 1 (the step from s_(τ−2) to s_(τ−1)).
Proof. Lemma C at each t + 1 ∈ [τ₀, τ − 1]: x stays although κ_(t+1) = c ≠ s_t(x), so ξ_t(x) ≠ c. At τ it moves, so ξ_(τ−1)(x) = κ_τ(x) = c. Then
Ξ_(τ−2)(x, c) < Ξ_(τ−2)(x, c̄) and Ξ_(τ−1)(x, c) > Ξ_(τ−1)(x, c̄); by A1 (MONO-1P) target values never fall, so V(xt(x, c)) rose at step τ − 1, and a value
changes only if a mover on its current Ξ-path switches (A7's argument). ∎
Use: a second mover that must WAIT is value-last at every switch, so each of its switches names a Ξ-descendant that switched exactly one step
earlier; cause244.py lists them (out/k3_structure.out for the N = 10 instance).

## 2. What step 1 demands of B (READING; premises: L-SI 55's ABANDON / ONE-AHEAD / simultaneity rule, lane, unrefereed, as relayed by the Lead 11:29Z)
Setting: F full at the top level over the pair (A, B), A key-last (rides), B value-last. A staggered second top mover y must read A's new key after F
and before B moves, and B's new key after F and before A moves again. With F riding at lag 0 and y following F at lag 1, B is key-ready from the
step τ at which A moved, must hold at the pre-state s_τ (F at A, y still at B), go at s_(τ+1) (F and y at A), and hold again at the last pre-state of
the pass (F and y at B, A = B). In terms of states: **ξ(B) = s(A) ⊕ [y is behind F]**. The first and third pre-states agree on (s(A), s(y)) and
need different values, so B's preference is not a function of (s(A), s(y)): it needs the state of a lag-0 key-rider of the pair (F itself or a
mover in step with it) XOR-ed with s(A). This is the Gray-code law of the odometer (second-mover state = first-mover state delayed by one pass),
and it matches L-LOWER's exact data on HIT7's top cluster (claude/l-lower b6887eff, docs/lower/L17-around.md §1: «f6 = XNOR(q6, q7) 0 errors»).
- Why one added mover cannot supply it (READING, with the DATA of §0): a Ξ-comparison is decided by the top-ranked β of the symmetric difference of two
  chains; a mover in step with F whose Ξ-targets decode s(A) has a preference that is a function of s(A) only, so it cannot alternate at F's rate
  (A3 / Lemma C); a mover that follows F at lag 1 carries F's old state, which is y's own.
- MEMORY (READING). By Lemma C «hold» is free only for a C-element; a preference function has no memory. In the towers the memory sits in half-rate
  SHADOWS: movers one level ABOVE a pair (they read its alignment by key at lag 0) whose Ξ-pair reads a lower pair (H5PLUS_L5: mover 11 = W-pair (8, 9),
  Ξ-targets 6, 7; mover 10 = W-pair (8, 9), Ξ-targets 8, 9), and the next level reads the shadows' alignment by key again (mover 12, W-pair (10, 11)), and
  B reads that mover by value (B's option 1 has Ξ-target 12; cause244: 15 of B's 31 switches are caused by 12, 15 by 6). Signals go UP by key (lag 0)
  and come DOWN by value (lag 1); Ξ-acyclicity forbids the return by value through any mover B feeds.

## 3. The hill (DATA + READING)
- DATA: per-level best switch counts: LAD_d5_k3_s13: 1, 3, 7 | 7, 3. H5PLUS_L5: 1, 3, 7, 15, 31, 63 | 31, 15, 16, 8, 8, 4, 3, 5, 4, 4, 2, 4, 4, 3.
  HIT7: 1, 3, 7, 15, 31, 63, 127 | 33, 62, 96, 32, 47, 8, 9, 16, 32, 17, 16, 8, 4, 3, 3, 3, 3, 2, 1, 0, 1 (sim244.py; equal to r187 ideal.traj on all six).
- READING: sw(x) ≤ min(|K(x)|, |PΞ(x)|) − 1 (A2) is two odometers, one in keys (root = level 0) and one in values (root = the Ξ-minimal movers). In
  the N = 10 instance the Ξ-minimal movers are the hill top (movers by Ξ-height 0, 1, 2, 3, 4, 4, 5, 6, 7, 8: 9, 4, 8, 3, 0, 2, 1, 7, 5, 6; W-levels 4, 2, 4, 1, 0, 1, 0, 3, 2, 3):
  the slow movers of the hill are the roots of the value order and the full top mover 5 is near its top. A design with d ≈ 2k levels is
  therefore not excluded by counting (as A7′ says); whether the signal of §2 can be supplied at every level is the open step.
- Negative DATA for the naive form (Ξ-targets exactly one level up, β rank groups by level): all 589,824 homogeneous templates (dual244): max T = 4,
  6, 8 at d = 4, 6, 8 with at most 1 switch per mover (top level's β highest), T ≤ 1 with the bottom level's β highest (d 4, 6). Non-homogeneous
  climbs (dualclimb244; 12 or 8 restarts × 300,000 evaluations): hill score 16 / 22 (one level up) and 18 / 22 (one or two up) at d 6; 27 / 52 and 29 / 52
  at d 8. No full hill in this restricted shape.

## 4. Tools (experiments/red/r244; own engines)
sim244.py (Python engine; trajectories equal to r187 ideal.traj on the five towers + H5PLUS_L5), show244 / trace244 / cause244 (structure, trace, key-last /
value-last classification with the causing movers), dump244 / dumpseed244 (text dumps for the C tools), pair244.c (joint screen, 192-bit values),
room244.py, lad244.c (climb on general ladders, ~1e6 evaluations / s at d 5; seeded lifts), dual244.c / dualclimb244.c (Ξ-up ladders), prune244.py
(greedy core: RECF4 loses only 2 of 40 movers before k drops: the towers have no small core by deletion). Outputs in out/; the N5 check in
out/one217_check.out (run from a read-only copy of claude/l-new a143d406).

## 5. Seeded lifts (filled in at the end of the session)
(see the addendum below, written after the two runs ended)

## 6. For the lower-bound side (through the Lead to L-SI 55)
- Lemma C and Lemma VL are short and checkable; with ODOMETER they give, for every waiting second mover, the exact pre-states at which its
  preference is prescribed (hold … hold, go) and a named Ξ-descendant switching one step before each of its moves.
- The missing lemma, as the failure states it: bound the number of levels through which the «go» of §2 (an XOR of a lag-0 rider's state with the
  first mover's state, held by C-elements above the pair) can be relayed by key and returned by value under Ξ-acyclicity. Both instances of the
  failure are in this lane's files: H5PLUS_L5 (N 41) and LAD_d5_k3_s13 (N 10).
