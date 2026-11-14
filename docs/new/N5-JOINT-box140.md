# Box 140 N5-JOINT: the two sides couple move by move (ALTERNATION), and in the 2-wide ladder movers only move toward the key-smaller strand (TOWARD-L); per-level accounting from both ends still allows an exponential middle, so a joint potential must use time causality; the LADDERBF-up shape stays linear in climbs (5 / 7 / 11 / 13 at d 3-6)
L-NEW successor 47, 2026-11-02 (date -u: see the commit). Lead GO 00:02Z (box 140: the joint potential). Labels: PROVED (lane), CONJECTURE,
READING, DATA, DEAD, OPEN. G-N5-TIME stays OPEN; IDEAL-ACYC-POLY stays OPEN. Not a TARGET.md claim.
Model and notation: box 139 (docs/new/N5-IDEAL-box139.md), i.e. L-RED R178 §1 with an acyclic Ξ-graph.
- A step t − 1 → t reads faces at state t − 1 and keys from σ_t.
- LADDER := the 2-wide complete deg-2 ladder: movers u_l = 2l and v_l = 2l + 1 at level l = 0..d − 1; option k of a level-l mover has
  W-target mover 2(l − 1) + k (c_W at level 0).
- UP-LADDER := a LADDER whose Ξ-targets are all movers of strictly higher level, or T (the LADDERBF-up recipe of box 139 §3).

## 0. Answer
- No polynomial joint potential was found, and IDEAL-ACYC-POLY stays OPEN. What was found:
- PROVED (lane):
  - Lemma ALTERNATION (any deg-2 mover x). Between two consecutive moves of x, BOTH the face order and the key order of x's two options
    reverse. Hence moves(x) ≤ 1 + min{face-order reversals, key-order reversals}. This sharpens PATHS for deg 2: it counts reversals
    of one pair, not values.
  - Lemma TOWARD-L (LADDER). A level-l ≥ 1 mover only ever moves to the option whose W-target is L_(l−1), the key-smaller of u_(l−1),
    v_(l−1) at the new state. So moves(x) ≤ 1 + flips(L_(l−1)).
  - Lemma L-ACCOUNT (LADDER). flips(L_l) ≤ flips(L_(l−1)) + moves at level l. If u_l and v_l point at different targets, L_l is the
    one pointing at L_(l−1); if they point at the same target, L_l is fixed by their two gate indices.
  - Lemma TOP-STATIC (UP-LADDER). The top movers' faces are static, so each top mover moves ≤ 1 time. A level-l mover's face-order
    reversals are ≤ the value changes of its two Ξ-targets, all at higher levels.
- Proposition TWO-SIDED (PROVED, lane). In the UP-LADDER, moves at level l are bounded from below by a recursion growing ×3 per level
  (TOWARD-L, L-ACCOUNT) and from above by one growing ×3 per level (TOP-STATIC, ALTERNATION).
  - The best these accounting identities give is min{bottom bound, top bound}, which is exponential at the middle level, of order 3^(d/2).
  - So bottom-up and top-down counting, even combined pointwise, cannot prove IDEAL-ACYC-POLY (READING with proof: §2).
  - The missing ingredient is TIME. A Ξ-reversal at level l at step t needs a move above l at step t − 1. A move above needs an
    L-reversal below it at the same step (keys are read from σ_t). §3 states this as the precise target for a joint potential.
- DATA (§4): hill-climbs restricted to the UP-LADDER (the shape most favourable to a double counter, 30 min each) reach FL length
  5 / 7 / 11 / 13 at d = 3 / 4 / 5 / 6. LADDERBF's ceiling (TB with adversarial availability) is 22 / 52 / 114 / 240.
  - Moves per level peak in the middle (2, 5, 7, 4, 2 at d = 5; 2, 4, 7, 7, 3, 2 at d = 6), which is the two-sided shape.
  - L-flips grow additively per level, not multiplicatively.
- CONJECTURE UP-LIN (DATA only, weak: four 30-minute climbs): UP-LADDER runs have O(d) steps.
- Genome shape that would defeat a joint potential (READING, recipe for L-RED R188): a MIDDLE-OUT counter.
  - The lower half must double L-flips per level going up: levels split, so flips propagate, and Ξ blocks exactly one strand per flip.
  - The upper half must double Ξ-reversals per level going down.
  - The two waves must meet in step at the middle, one step apart (§3).
  - None of the climbs found doubling on either side.

## 1. Proofs (PROVED, lane)
- Lemma ALTERNATION. Let x have options a, b and move a → b at step t1 and next b → a at step t2 > t1. By the rule:
  - face_(t1−1)(b) ▷ face_(t1−1)(a) and key_(t1)(b) < key_(t1)(a);
  - face_(t2−1)(a) ▷ face_(t2−1)(b) and key_(t2)(a) < key_(t2)(b).
  Both orders are reversed between the two decision states. ∎
  - Corollary: moves(x) ≤ 1 + min{R_Ξ(x), R_W(x)}, the numbers of reversals of the two orders along the run.
- Lemma TOWARD-L. Let x be at level l ≥ 1 in a LADDER. Its option keys are key(u_(l−1))·g_0 and key(v_(l−1))·g_1. These first differ
  inside key(u_(l−1)) vs key(v_(l−1)), which have equal length and distinct last entries. So the key order of x's options is the order of
  L_(l−1). A move goes to the key-least available option ≠ current, which must be the option toward L_(l−1) at the new state.
  - After a move, x points at L_(l−1). Another move needs L_(l−1) to change first, so moves(x) ≤ 1 + flips(L_(l−1)). ∎
- Lemma L-ACCOUNT.
  - If u_l, v_l point at targets p ≠ q, their keys are key(p)·g vs key(q)·g′, so L_l is the one pointing at the key-smaller of p, q,
    i.e. at L_(l−1).
  - If both point at p, their keys are key(p)·g_u vs key(p)·g_v, so L_l is decided by the two (static) gate indices.
  - So L_l changes only at a step where L_(l−1) changes or a level-l mover moves. ∎
- Lemma TOP-STATIC. In an UP-LADDER, the Ξ-targets of top movers are T, so their faces are constant. By VAL-MONO (box 139), a move
  strictly raises the current face within a constant 2-element set: ≤ 1 move.
  - For a level-l mover, face(x, k) = β_k ⊕ val(xt_k) with xt_k higher, so a face-order reversal needs a value change of xt_0 or xt_1. ∎

## 2. Proposition TWO-SIDED, and why it is not enough (PROVED, lane; the «not enough» part is a computation on the bounds, not a game)
- From below (TOWARD-L, L-ACCOUNT, level-0 keys static): with F_l := flips(L_l), moves at level l ≤ 2(1 + F_(l−1)) and
  F_l ≤ F_(l−1) + 2(1 + F_(l−1)). F_0 ≤ 2, so F_l ≤ 3^(l+1) − 1.
- From above (TOP-STATIC, ALTERNATION): with C_l := the maximum number of value changes of a level-l mover, the value of x changes only
  when x moves or the value of its current Ξ-target changes. So C_l ≤ moves(x) + 2 C_(>l) ≤ 1 + 4 C_(>l), and moves(x) ≤ 1 + 2 C_(>l).
  This grows ×4-ish per level downward from C_(d−1) ≤ 1.
- Combined pointwise: moves at level l ≤ min{2·3^l, c·4^(d−1−l)}. The maximum over l is at l ≈ d/2, where it is exponential in d.
  - So any proof that only combines the per-level bottom-up and top-down counts, however tightly, ends at an exponential bound.
  - A joint potential must couple the two counts through the order of events in time (§3).

## 3. The precise target for a joint potential (READING)
- Causality per step (from the rule):
  - (K) keys at step t are read from σ_t, so an L-reversal at level l − 1 and the move it allows at level l happen at the SAME step;
    the W-wave climbs any number of levels in one step, through split levels only.
  - (Ξ) faces at step t are read from state t − 1, so a Ξ-reversal at level l at step t needs a value change above l at step t − 1;
    the Ξ-wave goes down one Ξ-edge per step.
  - A level-l move at step t needs both: an L-reversal at level l − 1 (since its previous move) and a face reversal at level l (since its
    previous move).
- A middle-level mover making M moves needs M L-reversals below and M face reversals, i.e. M value changes above. With
  steps ≥ (number of Ξ-waves), the run length is at least the number of distinct Ξ-reversals at the busiest level, divided by the number
  of levels a single upper move can feed in one step.
- Target statement (OPEN): «every step of an IDEAL-ACYC run that is not stuck strictly increases Ψ := Σ_x (Ξ-topological rank of x's
  current Ξ-target) − (W-level of the lowest split level), and Ψ has polynomial range». It is formulated from the data shape (middle peak,
  additive L-flips) and NOT proved. It is the kind of statement a joint potential must be. It is listed so that L-RED can aim R188 at
  breaking it: a step that lowers both.

## 4. DATA
Tools (experiments/new/box140/): upclimb.py (UP-LADDER hill-climb; simulator = box139/paths.py run, the R178 §1 rule), alt.py
(ALTERNATION, TOWARD-L, L-ACCOUNT checks; per-level moves and L-flips). Genomes out/up_d3..6.json, logs out/up_d*.log.

| genome | d | steps (FL) | LADDERBF ceiling | moves per level | L-flips per level | ALT / TOWARD / L-ACC violations | PATHS bound violations |
| --- | --- | --- | --- | --- | --- | --- | --- |
| up_d3 | 3 | 5 | 22 | 2, 2, 2 | 1, 2, 3 | 0 / 0 / 0 | 0 |
| up_d4 | 4 | 7 | 52 | 2, 3, 3, 2 | 1, 2, 2, 3 | 0 / 0 / 0 | 0 |
| up_d5 | 5 | 11 | 114 | 2, 5, 7, 4, 2 | 2, 5, 5, 3, 2 | 0 / 0 / 0 | 0 |
| up_d6 | 6 | 13 | 240 | 2, 4, 7, 7, 3, 2 | 2, 3, 7, 6, 6, 5 | 0 / 0 / 0 | 0 |
- Climbs: 30 min each on 1 core (timeout), single seed per d (seed = d), up to 400,000 mutations, restart from best every 5,000. R187's
  ACYC climbs (all shapes, W 2, deg 2) reached 9 at d 4; this restricted shape reaches 7.
- R178 champions (deg 3, so ALTERNATION is vacuous there): TOWARD-L / L-ACCOUNT do not apply (not ladders); alt.py reports 0 violations of
  what applies.

## 5. Status
- PROVED (lane): ALTERNATION, TOWARD-L, L-ACCOUNT, TOP-STATIC, TWO-SIDED (including the computation that pointwise two-sided counting is
  exponential at the middle).
- CONJECTURE UP-LIN (DATA only, weak). OPEN: IDEAL-ACYC-POLY; the target statement of §3 (not proved, not tested beyond the shape it
  came from).
- READING: §3 causality; the middle-out counter recipe (§0) for L-RED R188.
