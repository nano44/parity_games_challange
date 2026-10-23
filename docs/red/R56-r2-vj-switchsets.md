# R56: N8d-R2 admissible sets vs VJ improving sets on G_zeta, state by state (box 24; L-RED successor 12; produced on Opus 5.5, D15 / L37)
Status: DATA plus readings, unrefereed. Lead GO 2026-10-23 10:19Z (date -u). Target N8d-R2 (docs/new/N8d-single.md §0).
Code that produced every row (all imported read-only, unmodified):
- R2: experiments/n8d-second/kl2fast.py (L-COMP; equal to kl_single.py seed for seed). Dual run only (G_zeta's improver = player 0 =
  the dual's Odd). The replay loop in cmp.py / lanes.py is KLFast.run's loop with the same rng calls; at the end of every R2 run
  the scripts assert the same pivot count and final tau as KLFast.run itself (all runs below passed).
- VJ: experiments/si/si.py Engine (L-SI), improving() and rule_random_edge(), as in experiments/red/gzeta/vj_re.py.
- Games: experiments/red/gzeta/gz{1,2,3}.pg (R55 §3; sha1 c29864c792e0…, d502e9eebc3e…, 7ab7a133ae3c…), all-0 start (first successor).
- New tools: experiments/red/gzeta/cmp.py (per-state comparison), lanes.py (lane timeline). Logs: experiments/red/gzeta/box24/.

## 0. Numbering check (the box-19 trap)
Both engines get ONE parsed game object (harness pg.read), so vertex ids are shared by construction. cmp.py asserts per vertex
that kl2's dual successor set equals si.Engine's (sorted, deduplicated) and that kl2's dual Odd nodes are exactly si's EVEN nodes.
It also asserts at every R2 state that kl2fast's C candidate set (kl_adm) equals the nodes of the Python admissible set computed
from the C labels. All runs below passed every assertion.

Notation. A(τ, µ) = admissible arcs of R2 = violated arcs of the dual's Odd nodes w.r.t. µ (kl2 admissible()). I(σ) = VJ improving
arcs of σ = τ. Arc classes are named by node letters: 'b->s' = some b_{i,j} -> s, etc.

## 1. Where the switch sets first differ
### 1a. At the start, on every game and seed: A ⊋ I
State 0 (the common start τ_1 = σ_0) already differs, so the first differing state is state 0 on gz1, gz2 and gz3:
- gz1: A − I = {w1->A1, a1,1->A1}, I − A = ∅ (|A| 3, |I| 1).
- gz2: A − I = {w1->A1, a1,1->A1, w2->A2, a2,1->A2}, I − A = ∅ (|A| 6, |I| 2). gz3: the same pattern for i = 1, 2, 3.
- On gz2, R2's first pick is in A − I with probability 4/6. Seed 1 picks a1,1->A1. Seed 2 picks w1->A1 at pivot 1.

Mechanism M1 (label truncation hides odd costs). Example: gz1, state 0, node w1. The arc w1->w2 is current; w1->A1 is the extra arc.
- Labels. µ(w2) = 0.0.0.0.1.0.0, µ(A1) = 0.0.0.1.0.0.0, Tighten(w1->A1) = 0.0.0.1.1.0.0 > µ(w1) = 0.0.0.0.2.0.0, so the arc is
  violated, i.e. admissible.
  - Label component 3 is A1's own priority 4, counted (even for the improver, odd in the dual). Component 4 is priority 2.
- VJ. The play from A1 is A1(4) d1(9) B1(4) b1,25(3) s(2) u1(2) u2(2) t(1). From w2 it is w2(2) t(1).
  - The odd 9 makes val(A1) far below val(w2), so w1->A1 is VJ-worsening.
- Why they disagree. In the dual, d1's priority 9 + 1 = 10 is EVEN, i.e. a truncation. A truncation zeroes the label components
  below 10 that come from beyond d1. It never makes a label smaller than that of a path avoiding d1.
  - So an odd (for the improver) vertex counts only by erasing lower counts, and here there is nothing to erase.
  - A1's own counted 4 then decides the comparison: 4 beats w2's counted 2.
  - VJ instead charges every odd vertex on the play by its relevance.
- Reading: on G_zeta, every arc into an even "entry" node (A_i, B_i, priority 4) whose play continues through higher odd nodes looks
  better to the labels than to VJ.

### 1b. Along VJ's own run, A ⊇ I until a lane-tail shortcut (the first VJ step R2 cannot take)
History labels were tracked along VJ Random-Edge, with µ_t = lfp(G_σ_t, µ_{t−1}) after each VJ switch. This is Algorithm 1 line 6
applied to VJ's choice; it is legal while VJ's switch is admissible. Results:
- Up to the step below, I ⊆ A at every state: every VJ switch is KL-admissible, and A − I consists only of a->A and w->A arcs
  (gz1 also has c->r).
- The first VJ switch that is NOT admissible is always a b-lane tail shortcut 'b->s':

| game | seed | step | VJ switch | A − I at that state | I − A |
| --- | --- | --- | --- | --- | --- |
| gz1 | 1 | — (never: all 57 VJ switches admissible) | — | a->A, w->A, c->r | ∅ |
| gz2 | 1 | 196 | b2,25->s | w2->A2, a2,1->A2 | b2,20..b2,96 -> s (77 arcs) |
| gz2 | 2 | 178 | b2,71->s | w2->A2, a2,1->A2 | b2,39.. -> s (37) |
| gz2 | 3 | 209 | b2,110->s | w2->A2, a2,1->A2 | b2,32.. -> s (80) |
| gz2 | 4 | 199 | b2,51->s | w2->A2, a2,1->A2 | b2,14.. -> s (85) |
| gz2 | 5 | 207 | b2,40->s | w2->A2, a2,1->A2 | b2,14.. -> s (97) |
| gz3 | 1 | 420 | b3,96->s | w2->A2, a2,1->A2, w3->A3, a3,1->A3 | b2,32.. -> s and b3,.. -> s (220) |

- At each of these states the history labels equal the FRESH least fixed point lfp(G_σ, 0) on every printed node. The fresh labels
  make the same arcs inadmissible. So the departure is NOT a ratchet (history) effect. It is the label order itself.

Mechanism M2 (truncation is idempotent, so lanes do not unwind). Example: gz2 seed 1, step 196. Lane B2 has been cut at b2,19:
b2,19 -> s, while b2,20 .. b2,200 still point inward (b2,j -> b2,j−1) and so reach s through b2,19.
- VJ. b2,25 -> s skips the odd b2,24 .. b2,19, each charged separately (si's relevance order is a total order, as in Friedmann's
  thesis), so the shortcut improves. VJ unwinds the whole tail; the lane resets completely.
- Labels. The b's are dual-even (3 + 1 = 4) truncations. Truncating twice at the same level is truncating once, so
  µ(b2,j) = trunc(µ(s)) = 0.0.1.0.0.0.0.0.0 for every j ≥ 19, whether b2,j points inward or to s directly. The shortcut is tight,
  not violated.
- The tail never unwinds in label space. Re-closing the lane later needs only the cut nodes switched back, not the ℓ_i lane nodes.

### 1c. Along R2's own run
At every R2 state (gz1 seed 1, gz2 seeds 1-5, gz3 seed 1), A ≠ I. I − A is large: VJ wants to unwind tails (b->s, c->c, a->x) that
labels do not see. About half of R2's picks are VJ-worsening:

| game | seed | pivots | picks not in I | picks lowering the VJ value of the node | picks NOT admissible under the fresh lfp of the same τ |
| --- | --- | --- | --- | --- | --- |
| gz1 | 1 | 63 | 41 | 41 | — (not measured) |
| gz2 | 1 | 405 | 203 | 200 (b->b 147, a->a 30, …) | 6 (all c->r) |
| gz2 | 2 | 421 | 190 | 188 | 14 |
| gz2 | 3 | 389 | 201 | 200 | 8 |
| gz3 | 1 | 1432 | 475 | 467 (b->b 338, a->a 69, …) | 28 |

So R2's departure from Random-Edge is mostly label structure (M1, M2): only 1.5-3.3% of picks (6/405, 14/421, 8/389, 28/1432) are history (the ratchet: picks that are
admissible only because µ remembers an earlier higher label).

### 1d. What this does to the counter (lane timelines, lanes.py)
"Close L" means every node of lane L points inward (the cycle through A_i / B_i is closed).

| run | steps | switches per lane (A1, A2, B1, B2, C1, C2; lengths 16, 16, 50, 200, 44, 44) | first events |
| --- | --- | --- | --- |
| VJ gz2 s1 | 824 | 48, 16, 150, 392, 132, 78 | 105 close B1, 189 close C1, 194 u1->d1, 271 w1->A1, 321 close A1, … |
| R2 gz2 s1 | 405 | 16, 16, 50, 212, 54, 47 | 3 w1->A1, 4 w2->A2, 62 close A1, 72 close A2, 145 close B1, … |
| R2 gz2 s2 | 421 | 22, 16, 60, 210, 53, 50 | 1 w1->A1, 4 w2->A2, 61 close A2, 94 close A1, 139 close B1, … |

- M1 in effect: R2 closes both A-lanes first, in about 70 steps. VJ closes A1 only after bit 1 is set (step 321) and A2 at step 667.
- M2 in effect: under VJ every re-closing of a lane costs its full length again (B1 3 × 50, C1 3 × 44). Under R2 a lane is
  re-closed in a few switches.
  - Example: R2 gz2 s1 re-closes C1 (44 nodes) at step 393, 5 steps after the counter reset at step 388.
- The lane delays ℓ_i that separate the bits in Friedmann's analysis are paid once, not once per increment.
- Reading: this is why R55 found R2 pivots ≈ #cycle vertices.

### 1e. Answer to item (1)
The switch sets differ from the very first state. Two mechanisms are responsible, and neither is history:
- (M1) Labels count only the improver's even priorities and truncate at its odd ones. An even entry node followed by higher odd
  nodes (A_i -> d_i, B_i -> lanes) therefore looks better to labels than to VJ. Result: extra admissible arcs w->A, a->A, b->B and
  early lane closing.
- (M2) A truncation is idempotent, so a lane tail that reaches the exit through a cut node is tight with the direct exit.
  Result: VJ's tail shortcuts (b->s) are inadmissible, lanes do not unwind, and the per-increment lane delay collapses to the
  number of cuts.
These are the per-state content of the Lemma 4.75 gap (T26 §2(b)(iii)): no tree-label analogue of "valuations ≈ potentials" can
hold on G_zeta, because the label order differs from the VJ order at state 0 and at every lane reset.
