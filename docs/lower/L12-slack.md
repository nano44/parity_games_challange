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
- Round 3 (ended 22:20Z, date -u): R5 from l9/rec/HIT7_lift_d32 (d 32, N + M 192; 4 more helper levels): best A 198, T 320,
  C 309, share 0.780, floor 227 (0.89 F(6)); frozen rec/ROOM_R5_d32.txt e6435e21 (sim6, fenc, replay30 agree: 7 caps, T 320).
  R6 (from R3, temp 2.5): no gain (187). Depth did not buy room within this budget (DATA, one run).
- Side DATA (sim6 = fenc = replay30): ROOM_R4 has F(7) = 252 (HIT7: 190; an eighth cap needs 510). The climb never scored level 7.
- Outcome of (a): the adjacency share falls from 0.86 to 0.74 at d 28 and plateaus over 3 rounds (6 runs, ~8.5 CPU-h). The floor
  falls from 262 to 210, i.e. 0.83 F(6), not below 0.7 F(6). So no level-8 target was built. Status for OSC-ROOM″'s question
  «share bounded below 1»: below 1 yes (0.74 at h = 7, 0.66 at h = 6, both DATA). No share near H6's 0.66 found at h = 7. No law.

## 5. ROOM_R2's level-8 target and fixed-rank exact questions (Lead 22:45Z decision (b); DATA, exact)
- Target: slackt.py on rec/ROOM_R2_A190_d28.txt (55ecfc2e), H = 8: least bill 210 (= billfloor's bound), T′ 510, 192 idle steps in
  191 gaps, F(0..7) = 2 6 14 30 62 126 254 510, slack 0. out/S8_R2_core.txt sha1 fd5b112c73fd16c9569aa43459e5cd4969b10f81 (tsat
  format out/S8_R2_tsat.txt 7ad35167). Core gates of levels 0-6 are semantically equal to HIT7's and the bases' (same joined bits);
  level 7 joined 0 as in core8. It agrees with core8 (c6e19673) on rows 0-20; the first differing row is 21.
- Encoder: L-COMP 13's enc32.py, read-only copy l12/enc32_lcomp.py (from claude/l-comp b63119fc, sha1 a8c4f5e3). Question «W0-R»:
  wiring and ranks of the base genome FIXED; signs, helper gates, helper starts and helper states free; core start = row 0; core
  gates from the base. --prefix t: rows 0..t only. fscan.sh finds the first UNSAT prefix (CaDiCaL); drupcheck.py re-solves it with
  Glucose4 + proof, runs l8/sat/drup.c, then deletes proof and CNF (CNF sha1 kept; same command regenerates it).
- Bases (d 32): seed rec/LCOMP_seed_W0_d32.txt (L-COMP's W0 seed, sha1 c0b65c48), C4 l10/rec/L10_C4_final_score144_solved.txt
  (42fef4dd), C10 l10/rec/L10_C10_osc_final_solved.txt (3ef36801), and SEED_R2 rec/SEED_R2_d32.txt (bb30e201: ROOM_R2 lifted to d 32
  by l9/lift.py, then the same 28 entries changed as L-COMP's seed differs from HIT7_lift_d32: level-7 gates, top helpers' signs /
  gates / starts).
  | base | target | first UNSAT prefix t | DRUP (S8_R2 target) | single-mover drops that make it SAT |
  | --- | --- | --- | --- | --- |
  | seed | core8 | 5 (= L-COMP's) | (L-COMP: VERIFIED) | — |
  | seed | S8_R2 | 5 | VERIFIED, 6,194 lemmas; CNF 9c32c5f6 | 11, 12, 13, 14, 15 |
  | C4 | core8 / S8_R2 | 7 / 7 | VERIFIED, 25 lemmas; CNF 0a73a1d7 | 13 (f6) |
  | C10 | core8 / S8_R2 | 7 / 7 (= L-COMP's) | VERIFIED, 0 lemmas (unit propagation); CNF 91937d79 | 11 (f5; = L-COMP's) |
  | SEED_R2 | core8 / S8_R2 | 1 / 1 | VERIFIED, 367 lemmas; CNF 5be5839f | 12, 13 (q6, f6) |
  Scope of every UNSAT: that base's wiring and ranks, the stated target's rows 0..t, enc32's model (R104 rules, validated by L-COMP
  against fenc / sim6 / replay30). Nothing is claimed about other wirings or ranks. No SAT model at full length: no HIT.
- Comparison core8 vs ROOM_R2: NO measurable difference. Every base dies at t ≤ 7, inside the 21 rows the two targets share, with
  the same culprit. The lower floor (210 vs 262) concerns retriggers spread over the whole run; fixed-wiring bases built for HIT7 /
  core8 fail at the start-up holds (rows 1-7: idle steps where pair 6 must wait) before any of that matters. SEED_R2 fails earlier
  (t 1): ROOM_R2's own ranks move q6 / f6 at step 1, where the target holds them.
- Reading. The fixed-rank tests confirm that the binding obstruction is in the first window (the f6 / f5 start-up holds of L10 §2f,
  §3d), and it is the same for both targets. A comparison of the targets needs a base that realizes their common prefix (rows
  0-20); none exists. So the floor reduction is untested by exact means. It is neither refuted nor supported.

## 9. Diff against TARGET.md
No statement mentions a parity game, a winning region, an algorithm's running time or a complexity class. All are about the IDEAL
model's step sequence (R104's definition) on 𝓛^R_d and its F-profile. Not M3, not a step-4 pass, not a TARGET.md claim.
