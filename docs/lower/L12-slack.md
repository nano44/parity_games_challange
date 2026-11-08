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

## 9. Diff against TARGET.md
No statement mentions a parity game, a winning region, an algorithm's running time or a complexity class. All are about the IDEAL
model's step sequence (R104's definition) on 𝓛^R_d and its F-profile. Not M3, not a step-4 pass, not a TARGET.md claim.
