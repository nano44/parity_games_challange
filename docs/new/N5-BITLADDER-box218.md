# Box 218 (D18): the landed IDEAL library against UPWARD ladders — no landed lemma forbids k = d/2; the counting ceiling k ≤ (d + 1)/2 and what is forced on it; classes in which a mover's two options read ONE pair are dead already at k = 2 (READING, one PROVED-lane corollary, DATA; nothing decided; QUIET-KEY-1P stays OPEN; not a bound; not M3, not M4)
L-NEW successor 77 (session_01V5yGRaRvmT6aAyZLgMCHoW), D1 / D14 / D18 / D21 / D25. Item 2 of the Lead's brief («pick ONE route that the two
… lanes are not on and state it first»). Route sent to the Lead 2026-11-13 12:32Z (date -u) before any run; Lead 12:07Z (crossing):
«the best own route is the one that uses the landed IDEAL library (R105-R116, R119, R120) against the upward ladders L-SI 55 found
(k = d/2 at d = 4, 6): which landed lemma, if any, forbids k = d/2 for all d?» Written from 13:02Z (date -u).
**DROPPED on the Lead's word (13:49Z, quoted): «box 218 and the k ≤ d/2 question are DROPPED; commit what exists of box 218 as it
is, labelled».** Reason: QUIET-KEY-1P has a kill candidate that does not use ladders at all (L-RED-B 5's family G_k, packet P-N5-EXP,
claude/l-red-b 350d84eb: L(G_k) = 2^k − 2, a half-rate family with k(G_k) = 1), so how deep full enumeration can go on upward
ladders no longer bears on G-N5-TIME. What follows is the record of the box as it stood; nothing in it is routed to a referee.
Labels: READING (what landed text says) / PROVED lane (unrefereed) / DATA (not to sign) / DEAD (with numbers; a lane record, L43) /
WITHDRAWN. Scope: the model 1P(G) = R104's IDEAL model on Ξ-acyclic genomes (packet P-N5-KEY1P, docs/new/P-N5-KEY1P.md, frozen at
l-new 44775605, unsigned), on the 2-wide ladders 𝓛^R_d of RESULTS R110. Nothing here is a TARGET.md claim. **G-N5-TIME stays OPEN.**
Credit: the class UPWARD LADDERS, its two instances and the exact SAT answers are L-SI 55's (claude/l-si 06f072f1,
docs/si/box107-timing.md §6, §7); this box reads landed text against that class and adds climbs (search, not exact).

## 0. Answer
1. **No landed lemma forbids k = d/2 on upward ladders (READING, §1).** The landed ladder results bound counts from above (R113
   T-BOUND), give necessary supplies (R113 PATH-RISE, R119 HIT / TOWER-NEED) and necessary delays (R120 PULSE-NEST, GAP-NEST); on an
   upward ladder they add up to the ceiling k ≤ (d + 1)/2 and to T_key < 2^(⌈d/2⌉ + 3), and nothing below that ceiling.
2. **UP-CEIL (PROVED lane; a corollary of A2 of P-N5-KEY1P, §2).** On an upward genome with d levels and degree ≤ D,
   sw(x) ≤ D^(min(lev(x) + 1, d − lev(x))) − 1 for every mover; on an upward ladder a mover of level l that switches through all its
   2^(l+1) keys needs l ≤ (d − 1)/2, so k ≤ (d + 1)/2, and T_key < 2^(⌈d/2⌉ + 3). Upward ladders are exponential in d only if the
   ceiling is reached up to an additive constant, and then by a factor 2^(d/2), never 2^d.
3. **What is forced at d = 2k with a full mover x of level k − 1 (PROVED lane, counting only, §2).** Both Ξ-targets of x are movers
   of level k or k + 1, each with at least 2^(k−1) − 1 rises of its value; a target of level k + 1 must take every one of its
   2^(k−1) path values, so above it every option goes to a mover of the next level (the upper block is then a complete dual
   ladder). At d = 2k − 1 both targets are the two movers of level k and both are of that complete kind.
4. **DATA (climbs; search, not exact; §3).** Templates in which both options of a mover read the two movers of ONE pair: k = 1 in
   all 28 runs (d = 4, 6). Upward ladders: k = 2 in all 9 runs at d = 4 and in all 9 at d = 6 under the objective k; k = 3 at d = 6
   in one run under the other objective; at d = 8, k = 3 in 1 of 2 runs (best level-3 mover 7 of 15 switches); seeded with L-SI's
   instances plus two middle levels: k = 2 (d = 6, 3 runs), k = 2 and 3 (d = 8). Hill-climbing does not decide d = 8.
5. **WITHDRAWN:** the «parity obstruction» of my 12:32Z message (two consecutive fully enumerating levels of a nearest-level upward
   ladder). The paper argument assumed that the value order above returns after each window; it need not (the order may flip an even
   number of extra times inside a window). No lemma is claimed. The class it was about (both Ξ-targets on the pair one level up) is
   dead by L-SI's exact SAT (BI-LADDER: longest runs 2, 3, 6, 8, 11 for d = 2..6) and in my climbs (§3).
6. **Not reached:** a rule for a family, or a bound. The next exact query is L-SI's (k = 4 at d = 8).

## 1. The landed ladder results read on upward ladders (READING; quoted by script, quotes218.out)
An UPWARD ladder: 𝓛^R_d (two movers per level, option j of a level-l mover with W-target the j-th mover of level l − 1) in which every
Ξ-target is a mover of a strictly higher level or the exit. F(l), doubling, windows, P(z), R(y) as in the quoted entries; a level is
CAPPED when F(l) = 2^(l+2) − 2 (both its movers switch 2^(l+1) − 1 times).
- R113. [Q R113] «(T-BOUND) on 𝓛^R_d, F(l) ≤ 2^(l+2) − 2 and T ≤ 2d + 2(F(0) + … + F(d − 2)) ≤ 2^(d+2) − 2d − 4»; «(PATH-RISE) at any
  degree, the current value cv(z) of every mover z rises at most P(z) − 1 times in a run». Reading: T-BOUND is the key-side ceiling
  (met by capped levels); PATH-RISE is the value-side ceiling. On an upward ladder P(z) ≤ 2^(d − lev(z)), so the two ceilings cross
  at the middle level: this is UP-CEIL (§2). Neither forbids the crossing point.
- R119. [Q R119] «(HIT) at any degree, cv(y) rises at step t iff some mover of y's old chain moves at t, so R(y) ≥ moves(y)»;
  «(TOWER-NEED) at a doubling level l with f = F(l − 1), each member x moves f + 1 times, P(x) ≥ f + 2, and for f ≥ 2 both Ξ-targets
  of x are movers with R ≥ (f − 1)/2». Reading: for capped levels 0..h − 1 on an upward ladder, P(x) ≥ 2^(l+1) at level l forces
  l ≤ (d − 1)/2, and the targets' R ≥ 2^l − 1 forces their level ≤ d − l. Supplies, not obstructions: at l = d/2 − 1 they leave
  the targets two levels (§2).
- R120. [Q R120] «(PULSE-NEST) if levels j, …, j + k are doubling then PULSE ≥ k + 1 on every j-window»; «(GAP-NEST) if moreover
  k ≥ 1 then GAP ≥ k + 1, so with levels 0, …, h − 1 capped (F(l) = 2^(l+2) − 2) PULSE and GAP are ≥ h − j for 1 ≤ j ≤ h − 2».
  Reading: with h capped levels a run has at least about 2^(h+1) steps (level h − 2 alone has 2^(h−1) − 1 windows of at least 4
  steps); UP-CEIL allows T_key up to about 2^(d/2 + 3). At h = d/2 the delays fit with a factor 4 to spare: no contradiction.
- R120. [Q R120] «(CROSS-ECONOMY) if level j is doubling and pair j is crossed onto two movers A_0 ≠ A_1 outside it (xt(2j, k) = A_k =
  xt(2j + 1, 1 − k)), then with D := cv(A_0) − cv(A_1)»: it constrains the signs of D inside every j-window for that wiring; it is a
  condition on the wiring of one pair, not on how many levels can be capped. (I did not test it on L-SI's instances.)
- R105-R112, R114-R116. Their bounds are exponential (R105 EXACT-ENERGY, R111 LADDER) or equivalences (R105 U-EQ, KEYFLIP;
  R114-R116 as their titles state); read under 1P = IDEAL they hold on upward ladders and none is a bound in d below UP-CEIL. I
  read their titles for this; I did not re-derive each on the class.

## 2. UP-CEIL and the forced shape on the ceiling (PROVED lane)
**UP-CEIL.** Let G be a Ξ-acyclic genome with levels 0..d − 1 and degree ≤ D in which every Ξ-target has a strictly higher level than
the mover of its option (or is the exit). Then hΞ(x) ≤ d − 1 − lev(x), so by A2 and Lemma 0 of P-N5-KEY1P
sw(x) ≤ D^(min(lev(x) + 1, d − lev(x))) − 1. On an upward ladder (D = 2, two movers per level): a mover of level l with
sw(x) = 2^(l+1) − 1 has l + 1 ≤ d − l, so k(G) ≤ (d + 1)/2; and T_key ≤ Σ_x sw(x) ≤ 2·Σ_l (2^(min(l+1, d−l)) − 1) < 2^(⌈d/2⌉ + 3). ∎
**CEIL-SHAPE.** Let x be a mover of degree 2 and level k − 1 on an upward ladder with sw(x) = 2^k − 1, Ξ-targets y_0, y_1. (i) The
sign of v(x, 0) − v(x, 1) changes at least 2^k − 2 times (A4 (iii)), alternately in the two directions; a change in favour of
option i needs V(y_i) to rise in between (values never fall, A1), so y_0, y_1 are movers, y_0 ≠ y_1 (A3 (ii)), and each V(y_i)
rises at least 2^(k−1) − 1 times. (ii) By Lemma 0 (b) and A1 a mover y of level m has at most |PΞ(y)| − 1 ≤ 2^(d−m) − 1 rises. So
lev(y_i) ≤ d − k + 1. (iii) If d = 2k: lev(y_i) ∈ {k, k + 1}; if lev(y_i) = k + 1 then |PΞ(y_i)| = 2^(k−1) and V(y_i) takes every
path value, so every mover on a Ξ-path from y_i has both options on movers of the next level (exit at the top). (iv) If d = 2k − 1:
y_0, y_1 are the two movers of level k, both as in (iii), and every rise of V(y_0) or V(y_1) changes the sign: their 2^(k−1) + 2^(k−1)
path values interleave strictly (the value-side mirror of the key interleaving of two W-targets of a full mover). ∎
Reading (no claim): on the ceiling the block above the full mover is a second odometer, in values, whose supply has no slack; the
key-side facts landed for capped levels (R119 DBL-EQ, R120 DOUBLE-EQ) have exact mirrors there. Whether the two odometers can be
made to drive each other for every k is the open question; L-SI's exact answers are «yes» at d = 4, 6 (k = d/2) and «no within 12
steps» at d = 5 (k = 3), so at the sizes measured the truth is ⌊d/2⌋, one below UP-CEIL at odd d. CONJECTURE (untested beyond
that): k ≤ d/2 on every upward ladder.

## 3. DATA (search, not exact; experiments/new/box218: lad218.py, run218.sh, outputs out/, instances inst/)
lad218.py: the key run on a ladder (cross-checked against one217.OneP: counter simdiff, must be 0), a hill-climb with restarts over
Ξ-targets, β ranks and parities, gate order and start, objective (k, the largest sw at level k, the sum of all sw); classes by
environment: upward with free ranks, upward with ranks by level, nearest-level upward, PURE (member 0 parallel and member 1 crossed
onto the pair one level up), templates in which both options of a mover read the two movers of ONE pair (mirror: level l reads
level d − 1 − l in the lower half and l + 1 above; mirror1; mid; up2; down: the pair one level below), and seeded starts (L-SI's
instance with two new middle levels). A climb gives a lower bound on what a class can do, never an upper bound.
Every number below is from the pinned files (out/SHA1SUMS; the «sec» field of a climb line is wall time and is not compared).
- Simulator: simdiff 0 on 800 random genomes (out/xcheck218.out; runs of at most 3 steps) and on 70 genomes with long runs (the five
  towers, box 217's 63 climbed records, L-SI's two instances; largest T_key 340; out/xfiles218.out).
- L-SI's instances replayed (inst/, byte copies, SOURCE.txt): up_k2_d4 T 3, switches per level (1, 1), (3, 1), (2, 2), (1, 1), k 2;
  up_k3_d6 T 8, (1, 1), (3, 3), (7, 1), (3, 3), (3, 2), (1, 1), k 3. Counters upceil, shape (§2) 0 on both; the control (the shape test
  on every degree-2 mover) fires 5 and 7 times (out/shape218.out).
- Templates (out/climb218_templates.out; 150,000 proposals, d = 4 and 6, seeds 1, 2; 28 runs): PURE, mirror, mirror1, mid, up2, down
  (ranks by level), down (free ranks): k = 1 in every run; the best level-1 mover has 2 of 3 switches (1 of 3 in mirror1 and down).
- Upward classes (out/climb218_upward.out; 250,000 proposals, seeds 1-3): ranks by level, free ranks, nearest-level with ranks by
  level: k = 2 at d = 4 in all 9 runs (both level-1 movers full: (3, 3)); k = 2 at d = 6 in all 9 runs (best level-2 mover 6 of 7).
  Free ranks at d = 8 (600,000 proposals, seeds 1, 2): k = 2 and k = 3 (level 2 (7, 7), level 3 (7, 7): 7 of 15).
- The other objective (out/climb218_both.out: LAD218_OBJ=both, free ranks, d = 6, seed 1, 185,000 proposals): k = 3, T 8, switches
  (1, 1), (3, 3), (7, 3), (3, 3), (2, 2), (1, 1): a second k = 3 ladder at d = 6, found by search (record out/rec/lad_up_d6_s1.json at
  that run; later runs with the same class, d and seed overwrite the record file, the line is the pinned evidence).
- Seeded (out/climb218_seeded.out): from up_k2_d4 with two new middle levels, d = 6, seeds 1-3: k = 2 (best level-2 mover 6 of 7);
  from up_k3_d6, d = 8, seeds 11, 12 (600,000 proposals): k = 2 and k = 3 (best level-3 mover 7 and 5 of 15).
- Reading: the nearest-level class does reach k = 2 at d = 4 once a mover may send an option to the exit or both options to one
  mover; what stays at k = 1 is the fixed template «two options on the two movers of one pair». This agrees with L-SI's PAIR NETWORKS
  dead end and adds nothing exact to it.

## 4. Not claimed; what a successor should not redo
No bound and no family. The classes of §3 marked dead are dead only as far as these climbs and L-SI's exact answers go. The
route's remaining content is §2's shape on the ceiling: an exact search at d = 8 can add CEIL-SHAPE (iii) as hard constraints (the
full mover of level 3 reads levels 4 and 5 only; a level-5 target has a complete ladder above it). TARGET.md diff: statements about
one candidate's IDEAL model on a subclass of ladders; not M3, not M4. **G-N5-TIME stays OPEN.**
