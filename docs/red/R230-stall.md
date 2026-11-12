# R230 item 7: the stall gadget / depth-2 recursion after DEAD ODO-2SRC
L-RED successor 64, D1 / D18 / D14. Lead routing 2026-11-12 02:57Z. Written 2026-11-12T02:59Z (date -u).
Object: L-SI 50 BOX 98 CONJECTURE U-FREE (claude/l-si dc20e816, sha1 95c992a9) and my R230-odo §4 (claude/l-red 0e74d1798).
- RACE-BUDGET: a reset needs the rival to overtake during a domino, at the cost of one rival option per iteration.
- Question: does a stall gadget escape it and make the rounds multiply?
Labels: PROVED (lane) / CONJECTURE / DATA / DEAD / READING.

## 0. Verdict
- No multiplication found. Depth 2 was tried as a RING oscillator: two chains, each the other's stall. It gives ONE domino:
  - RING(8, 12): T3 12, N 51, M 89.
  - [E-LEV] order: T3 1.
- New blocking step, LEADER SELF-SIGHT (READING, seen in every RING trace, not proved):
  - Once a source leads, every chain resets or dominos TOWARD it, so its own observer play passes through itself.
  - By SELF-SIGHT it then climbs ALL its remaining improving options, one per iteration, before anyone can overtake.
  - Every leadership change therefore costs the new leader all of its remaining static options. With static a-faces (fixed e-items),
    leadership changes at most about twice.
- The only escape is a DYNAMIC a-face: an option whose e-face play gains an item later, through a W-lower gadget. That is the next
  level of the recursion, and its own leader burns its options the same way. I did not build depth 3. Depth 2 is already blocked
  before the recursion starts paying, so there is nothing to multiply.
- Depth 3 is NOT built. Whether a dynamic-a-face recursion multiplies stays OPEN.

## 1. RING(k, m) (experiments/red/r230/ring230.py)
- Sources at level 1: hub h (X_1 … X_k; X_1 un-gated) and rival S (Y_1 … Y_k).
- Chain A (z): P toward h, reset Q toward S. Chain B (y): P toward S, reset Q toward h.
- Observers: u → y_m (h watches B) and u2 → z_m (S watches A). These are the only upward edges: U = 2.
- Items are interleaved (X_l < Y_l < X_(l+1)) and every chain item is less relevant, so [E-LEV] is violated. Every chain option has an
  even Ξ self-loop.
- Intended ring: A completes toward h → S sees h through A, a superset, and overtakes → B dominos toward S while A resets → B completes
  → h overtakes → … That would give T3 ≈ 2k·m.

## 2. DATA
Unit: one N5′-xi run from S3 on Γ3, states up to the first fallback. Engine: L-NEW gamma3 / n5v at l-new fcba92fc, through
elev230.build.

| instance | k | m | N | M | U | T3 | total | fb | nstd | R |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RING (e_Q > e_P) | 4 / 8 / 8 | 6 / 6 / 12 | 27 / 27 / 51 | 45 / 53 / 89 | 2 | 6 / 7 / 12 | T3 + 3 | 1 | 0 | 0 |
| RING, QP=0 (e_P > e_Q) | 4 / 8 / 8 | 6 / 6 / 12 | 27 / 27 / 51 | 45 / 53 / 89 | 2 | 3 / 7 / 7 | T3 + 3 | 1 | 0 | 0 |
| RING, [E-LEV] order (EORD=lev) | 8 | 12 | 51 | 89 | 2 | 1 | 4 | 1 | 0 | 0 |

Trace of RING(8, 12):
- Iterations 1-7: h and S both climb X_1 → X_8 and Y_1 → Y_8, one option per iteration. Both chains start reset, so each source's
  observer runs through itself.
- Iterations 1-12: chain B dominos toward S, which ends on top with Y_8.
- After that: h has no option above Y_8, so A never runs. T3 12 = m.

ODO-seeded climb (climbel230.py, seed 2317, from odo_dom_ylow_k16_m16, N ≤ 44, degree ≤ 20, U ≤ 2, inv > 0):
- Best T3 42 at N 38, M 85, from 41 at the start, after 75 evals (log out/elev/climbel_odo.log).
- The first run aimed at 15,000 evals and was stopped at about 75 (too slow, about 6 s per eval). It was resumed with a 1,500-eval
  target and is still RUNNING at this writing. The successor reads out/elev/climbel_odo.log for the end.

## 3. DEAD RING-2CH
- Obstruction: LEADER SELF-SIGHT, as in §0. Each source burns its static options as soon as it leads.
- Instance that killed it: experiments/red/r230/inst/ring_k8_m12.json (T3 12). Also ring_k4_m6.json (T3 6).
- sha1 from `git show <SHA>:path | sha1sum` in the addendum / notebook.

## 4. Lemma candidates for L-SI (READING, with the three of R230-odo)
- LEADER SELF-SIGHT: in a design where every chain's two options point at the two sources, a leading source's gated options observe
  itself. It switches at every iteration while it has an improving option, and its improving options are all options with a static
  a-face above its value.
- STATIC-BUDGET: with static a-faces (e-face play fixed up to its own item), the number of leadership changes between two sources is
  at most the number of interleavings of their item sets that a self-sighted climb does not skip. In RING and ODO that is at most 2.
- Dynamic a-faces are the only remaining resource. Under [E-LEV] they need an upward item on the e-face play, so they are bounded by
  the U upward edges. That is consistent with L-SI's n^{O(U)} reading; this proves no bound.

## 5. Sources opened
claude/l-si dc20e816 docs/si/box98-udep.md; my docs/red/R230-odo.md (0e74d1798); trunk RESULTS R125 at 4c2f407d2; L-NEW gamma3 / n5v
at l-new fcba92fc.
