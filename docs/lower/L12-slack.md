# L12: a slack re-timing for level 8 cannot lower the bill (BOX L12, L-LOWER successor 11; decision of the Lead 17:03Z 2026-11-08)
Labels: PROVED (lane, unrefereed) / CONJECTURE / DATA / DEAD / READING. Every DATA clause names its counter (unit, set, scope).
Model, notation and tools as docs/lower/L10-design.md and L11-osc.md. Nothing here is a result in the sense of CLAUDE.md;
G-N5-TIME stays OPEN. Not a TARGET.md claim (§9).

## 0. The box, and why it stops at step 1
- Box (Lead 17:03Z): build a NON-minimal (slack) re-timing of HIT7's pairs 0-6 with T′ > 510, slack placed at core8's TOP-ONLY
  points, freeze it, rerun the C10-style search with fixed-rank questions. The premise came from L11 §5 (CONJECTURE OSC-ROOM′:
  «with slack, lower pairs can be retriggered at the slack steps»).
- Outcome: for re-timings, that premise is false (§1, PROVED). The least-bill re-timing is L10's core8 itself, byte for byte (§2).
  So no slack target that is better than core8 exists among re-timings of HIT7, and the search step was not run (SKIPPED; reason §3).
- Tools (experiments/lower/l12/): slackt.py (least-bill re-timing: per-gap bills, exact weighted interval hitting, interval
  multi-cover greedy, level-H target in l10 core format and tsat format), billfloor.py (independent lower bound).

## 1. Lemma BILL-FLOOR (PROVED, lane; R104 movement rule, Lemma STRETCH's re-timing as in l10/stretch.py)
- Setting. S is a capped run; its core steps are the steps where a mover of pairs 0..H − 2 moves (states s_0, …, s_n). A re-timing
  inserts n_i ≥ 0 idle steps (pairs 0..H − 2 unchanged) before core step i and must satisfy the difference constraints of
  P-TOWER-FUEL Lemmas 2, 3 at H (stretch.py; «hard interval» (a, b] = a constraint that needs ≥ 1 idle step in gaps a + 1..b).
  The bill of gap i, b(i) = number of movers of pairs 0..H − 2 that are free at s_(i−1) and move at step i (level 0: the gate
  allows the switch; level ≥ 1: s_x ≠ c_x at s_(i−1)'s keys). If n_i ≥ 1, each of them holds at the idle steps and moves at i. So its
  preference changes between the last idle pre-state and the one before it, where pairs 0..H − 2 are unchanged: a mover of pair
  H − 1 or a helper on its chain must change at the last idle step (L10 §1a's retrigger rule, with level 0 included).
- Claim 1: b(i) ≥ 1 for every i. Let x be a mover of the lowest level l that moves at step i. If l = 0, x moved, so the gate allowed
  it at s_(i−1), and x is free there. If l ≥ 1, c_x = o(l − 1) depends only on pairs 0..l − 1 (Lemma STRETCH), which do not move at
  step i, so c_x(s_(i−1)) = c_x(s_i) ≠ s_(i−1)(x): x is free at s_(i−1). ∎
- Claim 2: every re-timing pays at least Σ over m pairwise disjoint hard intervals of the least bill inside each. Disjoint
  intervals need idle steps in distinct gaps. ∎ With Claim 1 the bill is ≥ m.
- Consequence. The bill is fixed by the base run's state sequence, not by T′. Adding slack (more idle steps, T′ > F(H − 1)) never
  lowers it. Within one gap, extra idle steps make the last one a step where nothing in the core changes (pair H − 1 holds after
  its two moves), so its retriggers must then come from helpers alone. Slack can only make the bill harder to serve.

## 2. DATA (billfloor.py, slackt.py; unit = retrigger event (gap, mover); set = all re-timings of the stored run's core sequence
satisfying Lemmas 2, 3 at H; scope = the stored start)
| base run (caps h) | H = h + 1 | core gaps | gaps with bill 0 | hard intervals | disjoint | bill floor | o(h − 1) changes at adjacent core steps |
| --- | --- | --- | --- | --- | --- | --- | --- |
| HS2_d3 (2) | 3 | 6 | 0 | 6 | 6 | 6 | 5 of 6 |
| REC_d10_tower (4) | 5 | 32 | 0 | 39 | 28 | 32 | 27 of 30 |
| H5_d20 (5) | 6 | 64 | 0 | 87 | 60 | 60 | 59 of 62 |
| H6_d24 (6) | 7 | 170 | 0 | 114 | 84 | 88 | 83 of 126 |
| HIT7 (7) | 8 | 289 | 0 | 324 | 219 | 262 | 218 of 254 |
- For HIT7 → 8 the exact least bill (slackt.py: weighted hitting DP over the 324 hard intervals, every one hard since no gap has
  bill 0) is 262 = the lower bound, with T′ = 510. The resulting level-8 core target out/S8_HIT7_core.txt has sha1
  c6e19673cbda12ba2ec8f7e70da4436cab8ed922 = l10/out/core8_HIT7.txt: the least-bill re-timing IS L10's minimal stretch.
  F(0..7) = 2 6 14 30 62 126 254 510, slack steps 0.
- READING. The bill floor counts the base run's o(h − 1) changes at adjacent core steps: each such pair forces an idle step, and
  each idle step costs ≥ 1 retrigger. H6 has room (126 changes over 170 core steps, floor 88 = 0.70 F(5)). HIT7 has little
  (254 over 289, floor 262 = 1.03 F(6)). This is a measured reason why level 8 on HIT7 is harder than level 7 was.

## 3. Corrections to L11 §5, and what remains
- CONJECTURE OSC-ROOM′ (L11 §5) is DEAD as stated for re-timings. Instance: HIT7 → 8. Every re-timing has bill ≥ 262 (§1), and the
  least-bill one is core8 (c6e19673). The slack of the realized towers (L11 §3: steps where o(h − 1) holds) is a different thing:
  steps where LOWER pairs move without changing o(h − 1). A re-timing cannot create those, since it only adds idle steps.
- The L11 DATA stand: the tight targets' TOP-ONLY shares, no realized h ≥ 3 tower is tight, and shared helpers in every realized
  tower. What changes is the reading: the root of the recursion is the bill of the base sequence, not tightness as such.
- CONJECTURE OSC-ROOM″ (replaces OSC-ROOM′; READING-level support). Extending a capped tower by RE-TIMING its run costs a retrigger
  bill of at least the number of adjacent o(h − 1) changes in its core sequence. Each event must be served at an exact idle step by
  q_h or by a helper that does not read the level it retriggers. If the base runs keep adjacent changes at a share near 1 (HIT7:
  218 / 254), each new level needs a helper clock of size comparable to the level below. That is the per-level reading again,
  with d super-linear. If a tower family keeps the share bounded below 1 by giving its lower pairs room (H6: 83 / 126), one shared
  cascade can plausibly serve the bill. Not proved either way.
- The search step was SKIPPED (no slack target better than core8 exists among re-timings). Fixed-rank questions on core8 itself
  are L-COMP 13's line (C10: UNSAT from t 7, b4942bef).
- Next options: (a) a level-8 target from a DIFFERENT lower sequence (not a re-timing of HIT7) with fewer adjacent o(6) changes,
  e.g. by climbing HIT7's levels 0-6 for room while keeping 7 caps (a «room climb»: objective = adjacent-change share, constraint =
  caps 7); (b) accept bill 262 on core8 and test exactly, with fixed ranks, the helper clocks that serve it (L-COMP's encoders).

## 4. ROOM CLIMB (Lead 18:02Z choice (a); DATA unless labelled)
- Lemma ADJ-COUNT (PROVED, lane; counting). Let a capped run have C core steps (a mover of pairs 0..h − 1 moves) and k changes of
  o(h − 1), all at core steps (o(h − 1) depends only on pairs 0..h − 1). Of the k − 1 gaps between consecutive changes, each
  non-adjacent one holds ≥ 1 of the C − k core steps without a change. So A = #adjacent pairs ≥ 2k − 1 − C. Also
  C ≤ M_core = total moves of pairs 0..h − 1, and M_core = 2·Σ_(l<h) (2^(l+1) − 1) = 494 at h = 7 (pair l: 2^(l+1) − 1 moves per mover) in both HIT7 and the climbed
  genomes (R113 MOVES with equality, measured). Hence at h = 7: A ≥ 507 − C ≥ 13. Lowering A means spreading the core moves
  over more steps (fewer simultaneous core moves). ∎
- Tool: l12/room.c (l9/fenc.c's ENC rules; a mutation is kept only if F(0..6) = 2 6 14 30 62 126 254 exactly; score A; tie-break
  smaller T; simulated annealing). adj.py is an independent Python count (sim6); billfloor.py gives the floor.
- Runs (unit = genome; scope = HIT7 6a3b274d's neighbourhood under room.c's moves, d 28; 85 min each, ~1,200 it/s, ~28% of the
  mutations keep 7 caps):
  | run | start | temp | best A | T | C | share A/k | bill floor (H = 8) | floor / F(6) | frozen (sha1) |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  | (HIT7) | — | — | 218 | 299 | 289 | 0.858 | 262 | 1.03 | 6a3b274d |
  | R1 | HIT7 | 0.5 | 187 | 331 | 320 | 0.736 | 214 | 0.84 | rec/ROOM_R1_A187_d28.txt 0d7d29e6 |
  | R2 | HIT7 | 1.5 | 190 | 317 | 317 | 0.748 | 210 | 0.83 | rec/ROOM_R2_A190_d28.txt 55ecfc2e |
  | R3 | R1 | 0.7 | 187 (no gain) | 331 | 320 | 0.736 | 214 | 0.84 | = R1 |
  | R4 | R2 | 1.0 | 189 | 331 | 327 | 0.744 | 217 | 0.85 | rec/ROOM_R4_A189_d28.txt 516857e3 |
  Every best meets ADJ-COUNT with equality (A = 507 − C). sim6, fenc and L-COMP's replay30 (read-only copy, l12/README-lcomp.txt)
  agree on R1 and R2: 7 caps, T 331 / 317, F(0..6) exact.
- Share A/k against size (DATA; unit = o(h − 1) change; scope = stored start of each genome):
  | genome | caps h | d | N + M = 6d | k = F(h − 1) | A | share | floor (H = h + 1) / F(h − 1) |
  | --- | --- | --- | --- | --- | --- | --- | --- |
  | HS2_d3 | 2 | 3 | 18 | 6 | 5 | 0.83 | 1.00 |
  | REC_d10_tower | 4 | 10 | 60 | 30 | 27 | 0.90 | 1.07 |
  | H5_d20 | 5 | 20 | 120 | 62 | 59 | 0.95 | 0.97 |
  | H6_d24 | 6 | 24 | 144 | 126 | 83 | 0.66 | 0.70 |
  | HIT7 | 7 | 28 | 168 | 254 | 218 | 0.86 | 1.03 |
  | ROOM_R1 | 7 | 28 | 168 | 254 | 187 | 0.74 | 0.84 |
- Reading. The climb lowers the floor from 262 to 210-214 (−19%) and then plateaus in two rounds. That is above the 0.7·F(6) ≈ 178
  threshold, so no level-8 target was built from it. H6 shows a share of 0.66 is reachable at h = 6, but the h = 7 climbs here
  stall at 0.74. Not a bound: ADJ-COUNT allows A down to 13.
- Round 3 (running at the time of writing): R5 from HIT7_lift_d32 (d 32, 4 extra helper levels: does depth buy room?), R6 from R3 at
  temp 2.5.

## 9. Diff against TARGET.md
No statement mentions a parity game, a winning region, an algorithm's running time or a complexity class. All are about the IDEAL
model's step sequence (R104's definition) on 𝓛^R_d and its F-profile. Not M3, not a step-4 pass, not a TARGET.md claim.
