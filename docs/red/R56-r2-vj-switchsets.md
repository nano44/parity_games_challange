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

## 2. A counter R2 does not escape: R53's H_k with z-separated delay lanes (item 2; 2026-10-23 10:20-10:55Z, date -u)
Code. Every pivot count comes from experiments/n8d-second/kl2fast.py. Paths:
- Verified runs go through experiments/n8d-second/bench.py (L-COMP; read-only; `--impl kl2fast --no-r1`). It runs the primal and
  dual R2 solve, checks regions against Oink zlk @ 8fbf0a7, and checks both strategies with experiments/harness/verify.py.
- Exploration rows use experiments/red/kl24/r2mean.py (KLFast dual .run('r2', seed), the same call kl2.solve makes) and ktr.py
  (switch-all trace, kl2 functions).
- Cross-check against L-NEW's own experiments/new/kl/kl_single.py --rule r2 (unmodified): HL88_0 seeds 1-3 give 1380 / 1378 / 1390,
  and HL88_1 seed 1 gives 63,686, all "verified". kl2fast gives the same numbers.

### 2a. The gadget (fixes M2 in label space)
experiments/red/kl24/lanegen.py G V L Z: node V (Even in G = the dual's Odd, R2's improver) with exit x and inward target y becomes
the far end of a lane l_1 .. l_{L-1}, V. Each l_j has arcs {x, z_j}; z_j is a one-successor node of priority Z with arc to l_{j-1};
l_1 has arcs {x, y}.
- In the dual, z is a truncation at Z + 1. Z is chosen ABOVE the priority at which the exit rises at the lap's reset and BELOW the
  counted component.
- Once the exit rises, every lane node's direct exit beats its chain through z (the chain loses the rise), so ALL L nodes switch
  out. The lane resets fully, as VJ's lanes do (§1b). Closing then runs as a frontier, one node per pivot.
- Contrast: a plain lane (no z) does not reset (M2). On H_0 with a plain lane, R2 means are 32.7 / 39.7 at L = 4 / 8; with z
  (Z = 23) they are 55.0 / 187.8 (30 seeds each).

### 2b. Where R2 killed R53's counter, and the two lanes
R53's 13-vertex H_0 (klmin_n13) laps with the dual period {3, 4, 8 -> 6}, {7: 2 -> 3}, {3: 6 -> 11, 7: 3 -> 2, 8: 6 -> 1},
{4: 6 -> 8}. Its R2 failures:
- (i) 7's lap move before phase A is complete (R55 §2). Fix: a lane on 7 (exit 2, target 3, open at the start, Z = 23).
  - Z = 23 sits between the exit's reset rise (2's own priority 22) and the counted priority 28.
  - With this lane alone, laps grow only linearly in L: on H_2, mean laps 7.5 / 12.5 / 24.0 at L = 8 / 16 / 24, 20 seeds.
- (ii) found here (ktr.py, H2_L16 seed 3, iteration 21): in phase C, R2 picks 8: 6 -> 1 before any of 7's L lane nodes resets.
  The closed lap then stands and µ jumps to TOP. Probability ≈ 1/(L+1) per lap, which matches the linear laps.
  - Fix: a second lane on 8 (exit 6, target 1, closed at the start, Z = 23).
  - With both lanes, every one of 20 seeds runs H_0's full counter: 7-lane 16 / 8-lane 4 gives 2008-2058 R2 pivots, against
    switch-all 2132.
- Family HL_k = experiments/red/kl24/hlgen.sh k 8 8: H_k (famgen.py H k) plus the lane of length 8 on 7 and the lane of length 8 on 8.
  n = 41 + 2k.

### 2c. Verified R2 runs (bench.py, kl2fast; results/hl88_k012.csv; every row status OK = regions == Oink zlk, strategies verified)
| k | instance (experiments/red/kl24/instances/) | sha1 | n | R2 dual pivots, seeds 1-5 | mean | mean / n^{k+1} |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | HL88_0.pg | 8f710aef7abdcb1315da01ef52da4a25afabe144 | 41 | 1380, 1378, 1390, 1392, 1400 | 1,388 | 33.9 |
| 1 | HL88_1.pg | d0b41ff986f4b1e365ce8027487b93590e679de6 | 43 | 63686, 63580, 63684, 63734, 63746 | 63,686 | 34.4 |
| 2 | HL88_2.pg | 1c3c78895df68fd10690fd5ab5467f7f01546ee7 | 45 | 3139182, 3139646, 1230538, 3138968, 3139556 | 2,759,578 | 30.3 |
| 3 | HL88_3.pg | 7a178aadf13e20e02c3d246e26fbaad41b6664b1 | 47 | running (bench, 2 jobs; ≈ 150M pivots per seed) | — | — |
- Primal pivots are 0 on every row.
- Ratios of the means: ×45.9 (k 0 -> 1) and ×43.3 (k 1 -> 2), about n per step of k.
- A full counter run costs ≈ 34.4·n^{k+1} dual pivots: 1,388, 63,6xx and 3,139,xxx. R2 completes it on 14 of 15 runs; seed 3 at
  k = 2 stops early (1.23M).
- Law (DATA, k = 0..2): mean R2 dual pivots ≈ 34·n^{k+1} with n = 41 + 2k, i.e. n^{(n−39)/2}. That is SUPER-POLYNOMIAL growth of the
  mean over 5 seeds, every output verified: the kill criterion's first clause, as data.

### 2d. Caveats (what this does NOT yet show)
- The lanes have FIXED length (8, 8). Some per-lap failure probability ε > 0 remains: one early stop in about 3.6·10^5 laps at k = 2.
  - So for fixed lanes the expected count is eventually capped near 34/ε pivots. The super-polynomial law holds over k = 0..2 and
    is expected to bend at larger k.
  - A family that is super-polynomial for all k needs lane lengths growing with k, so that ε(L)·n^{k+1} → 0.
  - L = O(k log n) suffices IF ε(L) decays exponentially in L. That is NOT measured: only L = 4 vs 8 for the 8-lane at k = 2
    (L7 = 8: at L8 = 4, HL_2 with n 37 stopped early on 5/5 seeds, 61,582-254,556 pivots against a full ≈ 34·37^3 ≈ 1.7M, all verified, results/hl_k012.csv; at L8 = 8, 1/5).
- Not shown: the remaining failure events and their exact probabilities (no proof); k = 3 is running.
- Faithfulness: the candidate is run unmodified (kl2fast and kl_single agree seed for seed). The games are ordinary parity games
  (Oink solves them).

## 3. ε(L) settled structurally, and the growing-lane family (Lead 11:02Z / 11:20Z; 2026-10-23 11:05-11:40Z, date -u)
### 3a. Full-run estimates (DATA; r2mean.py / bench rows; "early stop" = a run below 99% of the full count)
| lanes L = L7 = L8 | game | seeds | early stops | laps observed | ε (ML) | 95% CI |
| --- | --- | --- | --- | --- | --- | --- |
| 5 | HL_1 (n 31) | 20 | 8 | 1.68e4 | 4.8e-4 | [2.1e-4, 9.4e-4] |
| 6 | HL_1 (n 35) | 20 | 1 | 2.42e4 | 4.1e-5 | [1.0e-6, 2.3e-4] |
| 7 | HL_1 (n 39) | 20 | 0 | 3.03e4 | 0 | [0, 1.2e-4] |
| 6 | HL_2 (n 37) | 10 | 8 | 1.99e5 | 4.0e-5 | [1.7e-5, 7.9e-5] |
| 7 | HL_2 (n 41) | 10 | 1 | 6.7e5 | 1.5e-6 | [3.8e-8, 8.3e-6] |
| 8 | HL_2 (n 45) | 5 | 1 | 4.0e5 | 2.5e-6 | [6.3e-8, 1.4e-5] |
- Over L = 5..8, a Poisson fit gives ε ≈ exp(4.50 − 2.44 L) (×11.5 per +1 of L; 95% profile CI ×6.2 to ×22.4).
- A power law ε ∝ L^−14.4 fits as well (Δ log-likelihood 0.29). Statistics on this range cannot separate them, hence §3b.

### 3b. Exact per-lap failure probability (DATA; experiments/red/kl24/exactlap.py)
Method:
- Snapshot. A lap-start snapshot is taken in a base R2 run: seed S, after W pivots, at the J-th increase of dual node 1's label (one
  increase per lap).
- Chain. From the snapshot, R2 is a finite absorbing Markov chain on states (laps done, τ, µ). Every transition uses kl2fast's own
  candidate set (kl_adm) and arcs, then the C least fixed point. States are merged on equal (τ, µ) and lap count.
- Order. µ strictly increases at every pivot, so states are processed in increasing order of Σ_v enc(µ(v)), a topological order,
  and the result is exact. Fractions and doubles (FLOAT=1) agree to all printed digits at L = 4, 5.
- FAIL = a new TOP label, no candidate, or node 1 not raised. SUCCESS (LAPS = m) = node 1's label has risen m times.
- One-lap is not enough. A lap can end "successfully" in a CORRUPTED state, which then fails in a later lap.
  - Example: HL88_2 seed 3 failed at pivot 1,230,538. Its lap 35,724 has exact one-lap ε = 2.05e-8.
  - But in that lap the 8-lane closed while one 7-lane node (21) was still unreset, and 7 then closed early.
  - The next lap (35,725) starts from that state and fails with exact probability 0.0731.
- Remedy: the steady per-lap ε is the increment P(fail within m laps) − P(fail within m − 1 laps), once it is constant in m.

HL_2 with L7 = L8 = L, base seed 3, W 300, J 1 (P_m = P(fail within m laps)):
| L | n | P_1 (one lap) | P_2 | P_3 | increments P_2 − P_1, P_3 − P_2 | steady ε | ratio | full-run ε (§3a) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4 | 29 | 4.35311e-3 | 1.06561e-2 | 1.68925e-2 | 6.30e-3, 6.24e-3 (P_4 − P_3 = 6.20e-3) | 6.2e-3 | — | — |
| 5 | 33 | 3.90822e-4 | 9.73922e-4 | 1.54919e-3 | 5.83e-4, 5.75e-4 | 5.75e-4 | ×10.8 | 4.8e-4 [2.1e-4, 9.4e-4] |
| 6 | 37 | 2.75358e-5 | 6.7596e-5 | 1.06804e-4 | 4.01e-5, 3.92e-5 | 3.92e-5 | ×14.7 | 4.0e-5 [1.7e-5, 7.9e-5] |
| 7 | 41 | 4.54663e-7 | 2.4664e-6 | 4.6071e-6 | 2.01e-6, 2.14e-6 | 2.1e-6 | ×18.3 | 1.5e-6 [3.8e-8, 8.3e-6] |
| 8 | 45 | 7.89835e-8 | 1.80943e-7 | 2.79919e-7 | 1.02e-7, 0.99e-7 | 1.0e-7 | ×21 | 2.5e-6 [6.3e-8, 1.4e-5] |
| 9 | 49 | 8.19561e-10 (one lap only, 793,088 states) | — | — | — | — | — | — |
- States: L = 3..8 one-lap chains have 224 / 832 / 3,248 / 12,736 / 50,432 / 199,168 states (×4 per +1 of L). m-lap chains have
  about m times as many.
- The exact steady ε agrees with the independent full-run estimates (§3a) wherever both exist.
- Lap-to-lap variation (one-lap ε along base seed 3, W 0; SCAN mode over 20 laps at L = 4; J list at L = 5):
  - Only a few values occur. L = 4: {1.78, 3.05, 3.38, 3.81, 4.35}e-3. L = 5: {1.39, 3.06, 3.91}e-4.
  - The snapshot used above (J 1, W 300) is the maximum among them.
  - The FIRST lap after the start (W 0, J 1) is not worse: 3.05e-3 at L = 4, 1.39e-4 at L = 5.
  - NOT covered: lap types near level-2 carries (every n² laps). The scan did not reach them, and the multi-lap chain was run from
    one snapshot per L.

### 3b'. Two-lap exact ε at EVERY lap start of one long run (L = 4; 2026-10-23 12:19-13:01Z, date -u)
Runs: exactlap.py with SCAN, LAPS=2, on HL_2 with L = 4 (n 29), base seed 3. Files: results/eps/scan4_laps2_cond900.txt and
scan4_laps2_show260.txt.
- Laps 1-900 (with COND = the base run redraws a pick that would fail at once; the first 260 laps needed 0 redraws):
  - 745 of 900 lap starts have P(fail within 2 laps) = 7.65e-3 or 1.066e-2. The latter equals the steady snapshot of §3b.
  - 66 have 0.9e-2 to 2.2e-2.
  - 26 are BAD: 0.032 to 0.243. Examples: lap 204 (node 1 = 0.7.2) 0.2431; lap 251 (0.8.20) 0.1435; laps 45 and 156 0.044.
  - These are not carry laps (node 1's low digit is 2, 20, 17, 12). They occur in the natural run (0 redraws before them) as lap
    starts already partly corrupted (an opposite-lane node left unreset).
  - The average over all 900 lap starts is 1.32e-2, against 1.07e-2 at the steady snapshot; the BAD laps contribute 3.5e-3 of it.
- Natural runs, no redraws (base seeds 1, 2, 4, 5; results/eps/scan4_laps2_natural.txt):
  - The base runs died at laps 46, 130, 4 and 75.
  - Two of the deaths came right after a BAD lap start: seed 1, 0.1615 at lap 45, died at 46; seed 5, 0.2431 at lap 74, died at 75.
  - So BAD lap starts are the main failure route at L = 4.
  - Four runs are too few for a rate. The full-run estimates of §3a (L = 5-7), which include every route, agree with the steady
    increments of §3b within their CIs.
- So at L = 4 the natural per-lap ε is about 25% above the snapshot value.
- L = 5 (2026-10-23 13:01-13:42Z; same scan, laps 1-300, 0 redraws; results/eps/scan5_laps2_cond300.txt):
  - Distinct two-lap values: 6.74e-4 (129 laps), 9.74e-4 (141), and 30 laps between 8.0e-4 and 2.3e-3. Worst: 3.85e-3 at lap 137.
  - Average over all 300 lap starts: 9.0e-4, at or below the snapshot value 9.74e-4.
  - The worst lap shrinks from 0.243 (L 4) to 3.85e-3 (L 5), ×63, faster than the steady value (×11).
  - So at L = 5 the BAD lap starts no longer dominate.
- Not scanned: L ≥ 6. The trend from L = 4 to 5 says BAD laps decay faster than the steady ε; this is DATA at two points, not a
  bound. In §4 it is gap G1.

### 3c. The mechanism (READING; the chain is the DATA)
- MAXPATH=1 prints the most probable failing path. At L = 5 (one lap) it has probability 6^−5 = 1.286e-4 exactly:
    25->1 of [7, 17, 19, 21, 23, 25]; 27->26 of [7, 17, 19, 21, 23, 27]; 29->28 of [7, 17, 19, 21, 23, 29];
    31->30 of [7, 17, 19, 21, 23, 31]; 8->32 of [7, 8, 17, 19, 21, 23]
  - The 8-lane (25 .. 31, then 8) closes toward 1 while all of 7's lane (17 .. 23 and 7) waits to reset.
  - Any one of those, picked first, breaks the closed lap (R56 §2b (ii)).
  - Each of the L + 1 fatal picks comes from a set of size L + 1.
- The corrupted-state route (HL88_2 lap 35,724) is the same race, but late in the reset phase. When only r of 7's lane nodes are
  still unreset, the 8-lane frontier competes with r rescuers, so a lane-length run of frontier picks costs about (r+1)^−L.
  With r = 1 that is only about 2^−L. Such runs are rarer at the start of the window and dominate as L grows; this is why the
  multi-lap ε exceeds the one-lap ε by a growing factor: 1.4 / 1.5 / 1.4 / 4.7 at L = 4..7.
- Reading:
  - ε(L) decays at least exponentially in L. The base is between 2 (the r = 1 race) and L + 1 (the full race).
  - The measured ratio per +1 of L grows: ×10.8, ×14.7, ×18.3, ×21. That rules out a power law on this range, since the ratio of
    L^−a, ((L+1)/L)^a, DEcreases toward 1.
  - This is a reading of the chain, not a proof. The "≥ 2^−L" floor for the late-window race is the conservative case if the
    measured ratios ever stop growing.

### 3d. Growing-lane family HLg_k = hlgen.sh k L(k) L(k); n = 9 + 2k + 4L
| k | L | n | sha1 (experiments/red/kl24/instances/HLg_k.pg) | R2 dual pivots, seeds 1-5 (verified) | mean | steady ε(L) · n^{k+1} |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 5 | 29 | d2b96b4558248bf8f9248a5a6f0c20b569f8881c | 633, 623, 639, 643, 611 | 630 | 5.75e-4 · 29 = 0.017 |
| 1 | 6 | 35 | 2366cbadd9d592986143df8df1557b89b98bd59b | 32170, 32232, 32156, 32214, 32232 | 32,201 | 3.92e-5 · 1225 = 0.048 |
| 2 | 8 | 45 | 1c3c78895df68fd10690fd5ab5467f7f01546ee7 (= HL88_2) | 3139182, 3139646, 1230538, 3138968, 3139556 | 2,759,578 | 1.0e-7 · 91,125 = 0.009 (observed: 1 early stop in 5 runs; P ≈ 4.5% under ε = 1e-7) |
| 3 | 10 | 55 | 9918e9b8463507401cf73a73a2945aa9bf5f23ac | 388766970, 388771694 (seeds 1-2) | 388,769,332 | ≤ 9.4e-10 · 9.15e6 = 0.009 (ε(10) extrapolated from ε(8) with the smallest measured ratio 10.8; not computed) |
- Verification:
  - k = 0, 1: bench.py, results/hlg_k01.csv.
  - k = 2: results/hl88_k012.csv.
  - k = 3: results/hlg_k3.csv, from solvecheck.py, which is bench.py's check in-process; kl2's built-in 10^7 pivot cap stops
    bench at k = 3.
- Counter length: n^{k+1} laps. Pivots per lap from the full runs: 630/29 = 21.7, 32,201/35² = 26.3, 3,139,4xx/45³ = 34.4, about 4L + 2.
- Schedule: L(k) = the least L ≥ 5 with ε̂(L)·n^{k+1} ≤ 0.05, where ε̂(L) = 2.2e-6·10^{−(L−7)} (the L = 7 value, extrapolated
  with the smallest measured ratio). This gives 5, 6, 8, 10 for k = 0..3.
- Asymptotics (READING):
  - With any fixed ratio r per +1 of L, the schedule needs L(k) ≈ (k+1)·log_r(n) = Θ(k log k). Then n = 9 + 2k + 4L(k) =
    Θ(k log k), polynomial in k.
  - Mean pivots ≥ (1 − ε̂·n^{k+1})·(4L+2)·n^{k+1} = exp(Θ(k log k)) = exp(Θ(n)): super-polynomial.
  - (L = 2k + 4 alone suffices only while r^2 > 10k + 25, i.e. up to k ≈ 30 at r = 18.)
- Fixed lanes (8, 8) at k = 3 (HL88_3, n 47; results/hl88_k3.csv):
  - Seeds 1-2 ended in "ERROR: pivot cap 10000000 reached". That is kl2's built-in cap, NOT an incorrect output.
  - Seed 3 stopped early at 1,230,538, verified OK. That is the same pivot as at k = 2, since both runs are identical up to the
    first level-2 carry.
  - The solvecheck re-runs of seeds 1-2 (hl88_k3_solvecheck.csv, header only) were stopped at 11:17Z in favour of HLg_3.

## 4. Dead-end packet: N8d-R2 (written 2026-10-23 15:06Z by date -u; k = 3 row filled 2026-10-23 15:31Z by date -u)
Candidate: N8d-R2 (docs/new/N8d-single.md §0, frozen 03:21Z). Koh-Loho Algorithm 1 over the perfect (n, d/2)-universal tree; each
step takes a uniformly random Odd node with an admissible arc and switches it to its largest-Tighten arc.
Code: experiments/n8d-second/kl2fast.py (L-COMP; equal to L-NEW's kl_single.py seed for seed, checked here on HL88_0 seeds 1-3 and
HL88_1 seed 1), run unmodified. The counted quantity is R2's dual pivots; primal pivots are 0 on every row.

### 4a. The family (DATA; regenerable)
- HLg_k = `experiments/red/kl24/hlgen.sh k L(k) L(k)`. It is R53's H_k (experiments/red/kl/famgen.py H k: klmin_n13 plus 2k
  isolated self-loops with new top priorities) plus two z-separated delay lanes (experiments/red/kl24/lanegen.py):
  - on node 7: length L, exit 2, inward target 3, open at the start;
  - on node 8: length L, exit 6, inward target 1, closed at the start.
  - z nodes: priority 23, owner Odd, one successor. Lane nodes: priority 1, owner Even.
- Size n = 9 + 2k + 4L(k).
- Schedule: L(k) = the least L ≥ 5 with ε̂(L)·n^{k+1} ≤ 0.05, where ε̂(L) = 2.2e-6·10^{−(L−7)}. Explicitly L = 5, 6, 8, 10 for
  k = 0..3; asymptotically L(k) = Θ(k log k) (§3d).

| k | L | n | sha1 |
| --- | --- | --- | --- |
| 0 | 5 | 29 | d2b96b4558248bf8f9248a5a6f0c20b569f8881c |
| 1 | 6 | 35 | 2366cbadd9d592986143df8df1557b89b98bd59b |
| 2 | 8 | 45 | 1c3c78895df68fd10690fd5ab5467f7f01546ee7 |
| 3 | 10 | 55 | 9918e9b8463507401cf73a73a2945aa9bf5f23ac |

### 4b. Verified runs (DATA)
Check on every row: regions == Oink zlk @ 8fbf0a7 (-w 1), and both players' strategies pass experiments/harness/verify.py. Rows come
from bench.py (--impl kl2fast --no-r1), except k = 3, which uses solvecheck.py (the same check in-process, without kl2's 10^7 pivot cap).

| k | n | R2 dual pivots per seed | mean | full counter (≈ (4L+2)·n^{k+1}) | file |
| --- | --- | --- | --- | --- | --- |
| 0 | 29 | 633, 623, 639, 643, 611 | 630 | 630 | results/hlg_k01.csv |
| 1 | 35 | 32170, 32232, 32156, 32214, 32232 | 32,201 | 32,2xx | results/hlg_k01.csv |
| 2 | 45 | 3139182, 3139646, 1230538, 3138968, 3139556 | 2,759,578 | 3,139,4xx | results/hl88_k012.csv |
| 3 | 55 | 388766970, 388771694 (seeds 1-2 only: runtime ≈ 4.2 h per seed, Lead 11:20Z / 15:05Z) | 388,769,332 | ≈ 42·55^4 ≈ 3.84e8; both runs complete it | results/hlg_k3.csv |
- Growth of the mean: 630 → 32,201 → 2,759,578 → 388,769,332 (×51, ×86, ×141 per step of k; n 29 → 35 → 45 → 55). Every run at k = 3 completes the full counter; mean / n^{k+1} = 21.7, 26.3, 30.3, 42.5 pivots per lap (≈ 4L + 2; k = 2 is lowered by its one early stop).
- Lead re-runs: HL88_0 / HLg rows (11:02Z), exactlap L = 5, 6 (12:25Z).

### 4c. ε(L), the per-lap failure probability (DATA: exact chain; coverage caveats)
- Steady per-lap ε (exact m-lap chain increments, HL_2, base seed 3, W 300, J 1): 6.2e-3, 5.75e-4, 3.92e-5, 2.1e-6, 1.0e-7 at
  L = 4..8. Ratios ×10.8, ×14.7, ×18.3, ×21 (§3b).
- One-lap values for L = 3..9: 1.70e-2, 4.35e-3, 3.91e-4, 2.75e-5, 4.55e-7, 7.90e-8, 8.2e-10.
- Agreement with the full-run Poisson estimates wherever both exist (§3a).
- Coverage caveats:
  - one snapshot lap per L for the multi-lap chain;
  - lap types: few distinct one-lap values at L = 4, 5, and the first lap after the start is not worse;
  - every lap start scanned (two-lap chain) only at L = 4 (900 laps; average 1.32e-2 against the snapshot's 1.07e-2; 26 BAD starts
    up to 0.24) and L = 5 (300 laps; average 9.0e-4 ≤ snapshot; worst 3.85e-3), §3b';
  - L ≥ 9: one-lap only (L = 9) or extrapolated (L = 10).

### 4d. Mechanism (READING)
- R53's H_k is a lapping counter in label space: each period raises one label component by one, with a base-n carry through k + 1
  levels. That gives n^{k+1} laps.
- R2 killed it by two fatal early moves: 7's lap move before phase A, and 8's 6 -> 1 before 7 opens.
- A delay lane on each fatal move makes the move need a lane-length run of sequential frontier picks.
- The z truncations (priority 23, between the exit's reset rise 22 and the counted 28) make each lane reset fully every lap. This
  repairs M2 (§1b): label-space truncation is idempotent, so without z a lane tail is tight with the shortcut and the lane never
  unwinds.
- A lap fails only if a frontier run of length L beats every remaining rescuer in the opposite lane. That costs (r+1)^−L with r
  ≥ 1 rescuers, so ε(L) decays at least like 2^−L. The data show ratios that grow with L.
- Hence choosing L(k) = Θ(k log k) keeps the expected number of failing laps ≤ 0.05 over n^{k+1} laps. The mean is then at least
  0.95·(4L+2)·n^{k+1} = exp(Θ(n)).

### 4e. Status labels
- PROVED: nothing new. The family's correctness is checked per run, not proved. No theorem about R2 is claimed.
- DATA (verified): the 4b table; the exact chains of 4c (deterministic computations from kl2fast's own functions); the full-run
  ε estimates; the M1 / M2 per-state comparisons of §1.
- READING: the mechanism 4d; the at-least-exponential decay of ε(L) beyond L = 8; the asymptotic schedule
  L(k) = Θ(k log k); "mean = exp(Θ(n))" for k beyond the measured range.
- Gaps for a proof:
  - (G1) a bound ε(L) ≤ c·2^−L for EVERY lap type reachable in HLg_k, not just the sampled ones. BAD (partly corrupted) lap
    starts dominate at L = 4 and no longer at L = 5; L ≥ 6 is not scanned;
  - (G2) that lap failures are the only way R2 leaves the counter, which would give expected pivots ≥ (1 − Σ ε)·counter length.
