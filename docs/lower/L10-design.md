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
- out/target_HIT7_H8.txt (sha1 e031533adca196a246625ecc54b98a8f438380f2): the stretched core target of §1 (states of movers 0-13 per
  step, idle steps marked).

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

## 9. Diff against TARGET.md
No statement mentions a parity game, a winning region, an algorithm's running time or a complexity class. All are about the IDEAL
model's step sequence (R104's definition) on 𝓛^R_d and its F-profile. Not M3, not a step-4 pass, not a TARGET.md claim.
