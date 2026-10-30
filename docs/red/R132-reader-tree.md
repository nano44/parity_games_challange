# R132: target (A), a binary causal reader tree inside one W-run, is NOT built. Obstruction: every reader needs TWO private rising streams (Lemma TWO-SOURCE, Lemma PREFIX, lane proofs), so a tree of devices adds (REP = (K − 1)·#devices) and a doubling needs a desynchronising gate per pair and per event, which is R108 §4's reused waiting gate. Also Lemma DAG-τ* (lane proof). DATA + READING; no kill
L-RED successor 32 (Opus 5.5; D1/D18). Scripts named "scratch" are in experiments/red/tree/scratch/ (mkrt.py and dagtest.py gated in check.sh). Lead 2026-10-30 05:28Z, target (A): "a BINARY CAUSAL READER TREE inside one W-run ... Your R130
(wdepth, branching 1) and R127/R128 (latew, depth 1) are the two halves. Combine them ... If it is impossible, give the exact
obstruction. That is what L-SI needs for a proof." Written 2026-10-30 from 06:00Z (date -u). Labels: PROVED (lane) / DATA / READING /
OPEN. Not a TARGET.md claim; G-N5-TIME OPEN; nothing here is super-quadratic.

## 1. What a kill would have to be (READING)
- REP_F is at most the length of the λ-run, so REP_F = 2^Θ(n) in one W-run is an exponential λ-run: a kill of G-N5-TIME, as the Lead
  says.
- The nodes of a causal tree are adoptions of EDGES, and there are at most m_E Even edges. So 2^Θ(n) REPEATs need some edges re-armed
  2^Θ(n) times. The causal tree must therefore reconverge: a DAG on O(n) edges with exponentially many causal paths, each re-arm a new
  path. A literal tree (distinct edges per node) only gives REP ≈ (number of nodes) × (re-arms per node), which is linear in its size.
  §3 (a) measures exactly this.

## 2. Two lemmas (PROVED, lane; one W-run F, τ fixed, λ_W fixed, no fallback)
Facts used:
- (F1) W_(t+1) ⊵ W_t pointwise. σ_t lies in the arena H_t = σ_t ∪ Iσ_t, and σ_(t+1) is the one-player W-optimum of H_t in G_τ (S4a).
- (F2) σ_(t+1) has no W_(t+1)-improving switch inside H_t. In particular, for x = σ_t(y): W_(t+1)(x) ⊴ W_(t+1)(σ_(t+1) y), in the
  successor order used for improving switches.

### Lemma TWO-SOURCE
- Statement. Let y be Even, and let u₁ < u₂ be two transitions of F at which y switches INTO z. Then
  W_(u₁+1)(z) ⊴ W_(u₂+1)(z). Equality forces W_(u₂+1)(z) = W_(u₂+1)(σ_(u₂) y), a tie of two distinct successors (box 50's W-silent
  case; X_F = 0 in all data).
  - So switches into z ≤ 1 + WCH_F(z) + ties. This is box 42 (ii), stated for every switch.
  - Hence, for a binary y alternating between z and a: S_F(y) ≤ 2 + 2·min(WCH_F(z), WCH_F(a)) + ties.
- Proof. y's own W is monotone (F1), so W(σ_t y) is non-decreasing in t. Then
  W_(u₁+1)(z) = W_(u₁+1)(σ y) ⊴ W_(u₂)(σ_(u₂) y) ⊴ W_(u₂+1)(σ_(u₂) y) ⊴ W_(u₂+1)(z).
  The steps are: monotonicity of y's value; (F1) at the vertex σ_(u₂) y; and (F2) at u₂ with x = σ_(u₂) y, since y moved to z. □
- Reading. A reader y re-armed k times needs BOTH its target and its alternative to rise k times. The alternative's rises are what make
  y leave, by a W-overtake or by a Ξ-release of a W-better alternative; the latter needs that alternative to have risen past z before.
  In the Lead's tree picture the target side is fed by the parent's adoption. The alternative side needs a second stream of equal size,
  through a different route (Lemma PREFIX).

### Lemma PREFIX
- Statement. Let the W_t-plays from z and a first meet at a vertex x (their merge point), with private prefixes P_z(t), P_a(t) (the play
  vertices before x). Then the W-order of z and a at t + 1 equals the order at t, unless some vertex of P_z(t) ∪ P_a(t) ∪ P_z(t + 1) ∪
  P_a(t + 1) switches at t.
- Proof. In G_τ every play is a path; λ_W is fixed in F. Suppose no prefix vertex switches. Then the prefixes and the merge point are
  unchanged, and both plays continue with the same tail from x. Path sets: P(z) = pre_z ∪ T and P(a) = pre_a ∪ T, with T disjoint from
  both prefixes. Their symmetric difference is pre_z Δ pre_a, independent of T. Lengths: |pre_z| + L against |pre_a| + L, so the
  comparison is independent of L. □
- Corollary. Each order flip between y's two options is paid by a switch on a private prefix. Each switch of y back INTO z (after
  leaving it) needs a rise of z that changes the order, so a switch on z's private prefix, and symmetrically for a. So
  S_F(y) ≤ 2 + 2·min(PS_z, PS_a), where PS_b counts the switches on b's private prefix at the time they happen.

### What the lemmas do NOT exclude (READING)
- A 2-wide LADDER on O(n) vertices: u_j, u′_j → {u_(j−1), u′_(j−1)} (with markers). When u_(j−1) and u′_(j−1) point to the same child,
  the private prefixes of u_j's options are {u_(j−1)} and {u′_(j−1)}. The counting then allows S_j ≈ 2·S_(j−1).
- So there is no counting obstruction. The obstruction is dynamic:
  - when both u_(j−1) and u′_(j−1) are unblocked, S4a sends them to the same W-best child at the same transition, and then the order of
    u_j's options is fixed by their own markers (PREFIX);
  - a flip at level j needs a DESYNCHRONISATION at level j − 1: one of the pair switches while the other is held by a Ξ-gate (a late
    adoption pending) or reads another route.
  - So every one of the 2^(j−1) events at level j − 1 needs its own gate episode on the same pair. That is one gate, re-closed and
    re-opened 2^(j−1) times inside one W-run, where W cannot fall: R108 §4's reused waiting gate (the closed option must W-follow the
    newest source, its Ξ then sits in the older band, and the gated link's honest value drops into that band). R124 §3 met the same wall
    at three factors; the ladder needs it at every level.
- I found no way around it. This is NOT a proof that none exists. Routes (A), (B), (C) of R108 §6 are still untried.

## 3. DATA
### (a) R127 × R130 combined: a branching device tree (scratch mkrt.py = span/mkrw.py with TREE=D, BR=2; not pinned)
- Devices v_x → {d_x → θ → h′, c_x}, c_x → {r_(2δ+1) honest, yh_x τ}, yh_x → v_(parent(x)) (root: h). So each device's W-route passes
  through its parent (R130's chaining) and every node has 2 children (R127's breadth). δ is the depth of x.
  | depth D | devices | n (K 4, m 16) | iterations | REP (tiedlib = tied.py counts) | (K − 1)·devices | repchain causal maxdepth | windag BETA / LONG |
  | --- | --- | --- | --- | --- | --- | --- | --- |
  | 1 | 1 | 116 | 76 | 3 | 3 | not run | not run |
  | 2 | 3 | 126 | 76 | 9 | 9 | not run | not run |
  | 3 | 7 | 146 | 76 | 21 | 21 | not run | not run |
  | 4 | 15 | 186 | 76 | 45 | 45 | 4 | 1 / 4 |
  | 5 | 31 | 266 | 76 | 93 | 93 | not run | not run |
- So the causal tree exists (repchain parR 42, depth 4 = D), but the counts ADD: REP = (K − 1)·(2^D − 1). Siblings read the same
  reactor and are released at the same transition, so the window DAG is a path.
- Why, by TWO-SOURCE: each device's alternative d_x → θ → h′ rises only at h′'s steps (WCH ≤ K). So every device has ≤ K adoptions,
  whatever its ancestors do.

### (b) R131's family (tree/mktied.py)
- This is the first data with window-DAG INDEG 2 (pin tiedrb_K8_m16: INDEG 2, NPATH 14, LONG 15). Its readers z_J alternate between two
  live streams (the reactor chain a_(J+1) and the device c_(J+1)), which is TWO-SOURCE's requirement met once. REP is still quadratic
  (196 at n 270): both streams are clocked by the same pivots.

### (c) Friedmann's switch-best family, with τ started optimal (scratch sbtest.py)
- switchbestsubexp N (PGSolver port, sf/pgports.py), with σ0 = engine default and τ0 = N5's own final τ (optimal; I_τ = ∅, so τ never
  moves).
- Result: one W-run of 7N + 3 iterations (17 / 24 / 31 / 38 / 45 at N 2..6), REP 0.
- Default start: 27 / 37 / 44 / 52 / 62 iterations, 6 to 10 W-runs, REP ≤ 5.
- The S4a rule against a fixed optimal τ does not follow the switch-best counter.

### (c′) Plain Even ladders on R131's readers (scratch ladder.py; not pinned)
- Base: mktied.py 6 8. Layers ℓ = 1..4: X_(ℓ,i) (Even) → {X_(ℓ−1,i), X_(ℓ−1,i+1)} (layer 0 = the readers y_J), plus random priorities
  and, with probability 0.3, a third option. 60 random draws.
- Most switches of one vertex per layer: 12 / 12 / 13 / 13 / 13 (layers 0..4), with 68 to 69 iterations. That is flat.
- Each layer switches in step with the layer below, one hop later. With no gate between the two members of a pair, there is no
  desynchronisation (§2), so no flips are added.

- Gated variant (scratch gladder.py, 3 seeds, 15 min each, 2251 draws): every option of a layer vertex goes, with probability 0.6,
  through a fresh Odd gate (τ = the option; honest = a random reactor, pivot, device or earlier-layer vertex; random priorities).
  - No draw both kept a single W-run and switched at layer 3. The random gates are not τ-stable, so they end the W-run.
  - This is weak evidence. It shows only that the gates have to be designed; it shows nothing about whether one exists.

### (d) Lemma DAG-τ* (PROVED, lane) and its check
- Statement. Let G be acyclic except for self-loops at sinks, let τ₀ be an SI-optimal Odd strategy (I_τ₀ = ∅), and let σ₀ be any start.
  Then N5 stops after at most h + 1 iterations, h being the largest height, with no fallback and τ never changing.
- Proof (induction on height):
  - Let V* be the optimal values.
  - Claim: after step i, every Even vertex of height ≤ i plays an argmax of V*. It keeps one from then on, because its W already equals
    the maximum V*, and by (F1) it cannot drop.
  - Then W = Ξ = V* on heights ≤ i: there σ is optimal on the subgame below, and τ₀ is optimal.
  - Take a suboptimal Even v of height i + 1. Its best edge (v, w*) is Ξ-improving, so it lies in H. In H the W-optimum gives v an option
    with W = V*(w*), which is an argmax.
  - I_τ = ∅ throughout, so τ stays and the step is never empty while σ is suboptimal (no fallback). □
- DATA: 3000 random DAG games (n 4..14, out-degree ≤ 3, random σ₀, τ₀ = N5's final τ). Iterations ≤ height on every game, 0 fallbacks,
  τ constant (scratch dagtest.py seed 1).
- Reading: stable Ξ/W gaps need cycles. In mkrw the gap is held by the EQ / EQp pair, whose Ξ-routes run through each other's pivot.

## 4. READING for L-SI (what a proof could use)
- TWO-SOURCE and PREFIX are the exact local constraints: a reader is re-armed at most as often as the RARER of its two private streams
  changes order-relevantly.
- A super-polynomial REP in one W-run therefore needs a structure whose two private streams per reader are each super-polynomial.
  On O(n) vertices that means streams shared across levels (a ladder), and a ladder needs a reused desynchronising gate per pair.
- So a proof could aim at the gate: in one W-run (W monotone, τ fixed), bound the number of desynchronisations of two Even vertices with
  a common option set (episodes where exactly one of them is held by a Ξ-gate on an edge the other has taken). Each such episode is a
  late adoption on the held vertex, so this is again a REP count. The step that would break the circle is a bound on episodes per pair
  that does not go through W-changes.
- OPEN: R108 §6 (A) τ-ticks (would leave the W-run, but not the λ-run), (B) length thresholds, (C) digit-parity worlds.

## DONE / FINDINGS / NEEDS
- DONE: Lemmas TWO-SOURCE, PREFIX, DAG-τ* (lane proofs); device-tree probe (D 1..5); switch-best τ*-start probe; plain and gated ladder probes; DAG check (3000 games);
  this note.
- FINDINGS:
  1. NO KILL of G-N5-TIME. A device tree of depth D gives REP = (K − 1)(2^D − 1), additive (causal depth D, the window DAG a path).
  2. PROVED (lane): TWO-SOURCE, S(y) ≤ 2 + 2·min(WCH(z), WCH(a)) for an alternating reader; PREFIX, order flips need private-prefix
     switches.
  3. READING: the exact obstruction to a doubling ladder is the desynchronising gate per pair per event, which is R108 §4's reused
     waiting gate. Counting alone allows doubling.
  4. PROVED (lane) + DATA: on acyclic games with τ₀ optimal, N5 stops in ≤ height + 1 iterations (3000 random games).
  5. DATA: switch-best family with τ₀ optimal gives one linear W-run (7N + 3), REP 0.
- NEEDS: none from the owner.

## Addendum (Lead 05:49Z: LATE′ and Lemma GAP-CLIMB, L-SI box 51; READING, written 06:40Z)
- With GAP-CLIMB, a counter must make one target z's Ξ climb 2^Θ(n) times inside one W-run while z stays in the gap.
- Inside a W-run every Even step switches only Ξ-improving edges, so the W-run is a standard SI run with the S4a selection rule, and Ξ
  is strictly monotone. Each Ξ-climb of z is a switch on z's Ξ-play (its BR-play). §2's PREFIX argument applies verbatim to Ξ (fixed
  cycle nodes assumed): a climb of z that changes the order of z against a competitor needs a switch on z's private Ξ-prefix.
- So the exponential count needs a switcher on z's Ξ-play with 2^Θ(n) switches. Each of its switches is a W-optimum choice, so
  TWO-SOURCE applies to it, and the regress is again a ladder whose pairs must desynchronise once per event. That is §2's wall, now on
  the Ξ side.
- Not tried in this box: a design aimed directly at Ξ-climbs of one gap vertex (the R131 readers z_J climb 2 times per pivot cycle,
  2(K − 1) in total).
