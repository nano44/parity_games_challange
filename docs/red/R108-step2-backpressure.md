# R108: STEP 2 (a2), counter clock, progress note. OPEN. A super-polynomial total must sit inside one joint λ-run (R47 Lemma Φ). mkr's clock consumes W-cycle-node changes, which are monotone within a phase. Super-quadratic growth needs backpressure (a link that waits for a sub-process). The first gated-chain attempt (mk3 v1) fails, and its failure points to a structural obstruction for pivot-pair clocks
L-RED successor 26 (Opus 5.5; D15/D18; Lead 2026-10-29 11:07Z STEP 2: «(a2) the counter clock for super-quadratic or super-polynomial
runs ... a counter would run ACROSS phases. Its target count is the total iterations across phases ... reported as DATA, never as a
theorem»). Labels: DATA / READING / OPEN. Not a TARGET.md claim. G-N5-TIME stays OPEN. Nothing super-quadratic was found.

## Summary
| item | label |
| --- | --- |
| Reduction: by R47 Lemma Φ (every game) a run has ≤ 2n(n − 1) + 1 joint λ-runs. So total iterations ≤ (2n(n − 1) + 1) · (max iterations of one joint λ-run). A counter whose ticks change λ (T34's odd-top route) gets O(n²) ticks. A super-polynomial total needs super-polynomially many iterations inside ONE joint λ-run. | READING (from landed R47) |
| In mkr (R106/R107) every pivot tick is a change of the pivot's W-cycle node to a lower odd loop. Within a phase W is non-decreasing (R18 (d) Lemma S (c) + R17 (a) F1), so a vertex's W-cycle-node reward only rises: ≤ n such ticks per vertex per phase. mkr's whole execution is one phase. | READING + DATA (trace §2) |
| Super-quadratic within a phase needs BACKPRESSURE: a link of the delay chain that waits for a sub-process, so that a wave is longer than the chain. Since Ξ ⊴ W pointwise (R18 (d) Lemma S (b)), a closed link needs its CURRENT option to carry the high W (W(b) ≥ W(a) ⪰ Ξ(a) > Ξ(b)), as h's current option does in mkr. | READING |
| Obstruction for gates reused across pivot ticks in a pivot-pair clock (§4): the gate's closed option must W-follow h′. So its Ξ is at most h′'s world, the opening threshold lives in h′'s world, and the gated link's honest value drops into that band. That breaks the chain's later comparisons, or it makes readers' honest plays re-enter the delay chain (Ξ-cycles, λ changes). | READING (not a proof) |
| mk3.py v1 (gated chain, K 2, m 4, D 0..8): D = 0 gives 14 iterations (= mkr K 2 m 4). For every D ≥ 1: 8 iterations, 1 fallback. τ is NOT stable: at state 0 every gated a_j and every reader ρ_k has an I_τ edge, τ moves to the honest choice, W = Ξ there, and the links do not wait. | DATA |
| Ways out still open: (A) one τ change per pivot tick, so a gate can re-close across a phase boundary, inside one λ-run (needs an Odd-side clock); (B) thresholds carried by play LENGTHS, not markers; (C) a clock that is not a pivot pair. | OPEN |

## 1. The reduction (READING, elementary from landed results)
- R47 (a) Lemma Φ (c): along a run, at most n(n − 1) transitions change λ (Ξ's cycle nodes) and at most n(n − 1) change λ^U. A run is
  a concatenation of ≤ 2n(n − 1) + 1 joint λ-runs, so total ≤ (2n(n − 1) + 1) · max_r |r|. A super-polynomial total forces a
  super-polynomial joint λ-run.
- T34 (R2): an odd-top sequencing vertex escapes GATE-SHUT, but "such a cycle is Odd-won when closed, which changes a cycle node". Each
  such closing is one of the ≤ 2n(n − 1) λ-changes. So odd-top closings can only be polynomially many ticks of a counter. The counter's
  fast digits must tick without λ changes.
- Inside a joint λ-run, what is left to move:
  - τ (phases = τ-constant stretches);
  - Ξ (non-decreasing pointwise, R15);
  - U (non-increasing, R18 (d) Lemma S (b));
  - W = V(σ, τ), with Ξ ⊴ W ⊴ U. W is non-decreasing inside a phase (S4a's arena optimum dominates σ_k, R17 (a) F1 applied to the
    one-player game G_τ, Lemma S (c)), and it can fall only at a τ change.

## 2. What mkr's clock consumes (DATA + READING)
- Trace of mkr K 2 m 2 (n 36; experiments/red/seg/tr.py). Pivot h: z → C1 (t 0), C1 → C2 (t 5, jointly with gate w1: O → T1). Its W-play
  ends first in the loop L1 (τ(C1) = C1), then in the loop T1 (τ(C2) = MP2 → w1 → T1). h′: Cp0 → Cp1 (t 3), Cp1 → Cp2 (t 8), its
  W-cycle going Lp0 → Tp1 → Tp2. The loops are odd self-loops with L′0 > L1 > T′1 > T1 > T′2 (odd), so each tick moves the pivot's
  W-cycle node to a strictly better reward.
- Within a phase W is non-decreasing (§1), so the W-cycle-node reward of a vertex only rises. Hence ≤ (number of loops) ticks per
  pivot per phase. mkr's run is Θ(K · m): K ticks, each a wave of m one-step reactor flips. The whole execution is one phase (R107 §2;
  successor 25's addendum).
- R107 §4: max Ξ-changes per vertex = 2K − 1 = (number of pivot ticks) − 1. So, by L-SI's chain run ≤ Σ_v switches(v) ≤
  Σ_v Σ_succ (Ξ-changes + 1), a pivot-tick clock caps the run at O(n · (#ticks)) = O(n²) inside a phase.

## 3. Backpressure (READING)
- A super-quadratic phase needs a vertex with super-linearly many Ξ-changes. Ξ-changes propagate additively (a two-option vertex
  changes at most as often as its two successors together, plus lag). Events must happen at distinct times, and the run ends when the
  clock's last tick has propagated.
- So the clock must WAIT. A link r_j of the delay chain must not flip until a sub-process (a second chain's wave) has finished. Then a
  wave of the first chain lasts (chain length) × (sub-wave length), and nesting multiplies.
- Gate condition at r_j, options a (towards the wave), b (current): Ξ(a) > Ξ(b) (a is S2-improving: the wave has arrived) but
  W(a) ≤ W(b) (S4a keeps b) until the sub-process is done. With Ξ ⊴ W at every vertex: W(b) ≥ W(a) ⪰ Ξ(a) > Ξ(b). So the closed link's
  CURRENT option must have W far above its Ξ, through an Odd vertex with τ ≠ σ̄ (in mkr: τ(C_i) = MP_i → w_{i−1} → loop, σ̄(C_i) =
  Bq_i).

## 4. The obstruction met by pivot-pair clocks (READING; the reason mk3 cannot be repaired by marker choice alone)
Setting: mkr's pivots h, h′ alternate. During an h-wave every value in "h's world" (plays reaching h's current option) is above every
value in "h′'s world", and the other way round after an h′-rise (H_1 < V_1 < H_2 < …).
- A gate g_j at link j has a closed option GB and an open option GA. Its W must follow h′ when closed and h when open: W(GA) through h,
  W(GB) through h′.
- It must re-close after every h′-rise. Inside a phase this cannot be a W decrease, so W(GB) must be at least W(GA) at that moment.
  That means GB's W-play follows the newest pivot, here h′.
- GB's honest value is the minimum over GB's options (Odd), or GB's single successor. One option is the h′-route, so Ξ(GB) ≤ h′'s world
  plus GB's own markers. During an h-wave that is below h's world.
- The opening threshold is the comparison Ξ(GA) vs Ξ(GB). It must therefore be decided below h's world: GA's threshold route must
  carry values in h′'s band (readers exiting to h′). Otherwise g_j opens as soon as anything in h's world appears, i.e. at once.
- Then Ξ(GA) = min(h-route, threshold) = the threshold (h′ band). The gated link's honest value R_j = BA_j ⊕ min(R_{j−1}, Ξ(g_j)) drops
  to the h′ band and runs through the threshold route (delay chain → reader → …):
  - (i) every later link compares R_j-based values with b-routes in the same band, so the wave condition "r_{j+1} improves only after
    r_j flipped" must be re-encoded by markers in that band;
  - (ii) any reader whose honest play reaches a flipped gated link re-enters the delay chain. That is a Ξ-cycle through the reader,
    hence a λ change, unless every reader exits before the flipped link. That needs flipped values above the readers' exits, which
    (i) has just pushed down.
- I found no marker assignment that meets (i) and (ii) together. This is NOT a proof that none exists. Lengths (odd z: longer is
  better) are an unused degree of freedom.

## 5. DATA: mk3.py v1 (experiments/red/seg/mk3.py K m D; explicit start; n5b SPEC via r107.py --noxeng)
| K | m | D | n | iterations | fallbacks | longest run |
| --- | --- | --- | --- | --- | --- | --- |
| 2 | 4 | 0 | 42 | 14 | 0 | 13 |
| 2 | 4 | 1 | 67 | 8 | 1 | 4 |
| 2 | 4 | 2 | 70 | 8 | 1 | 4 |
| 2 | 4 | 4 | 76 | 8 | 1 | 4 |
| 2 | 4 | 8 | 88 | 8 | 1 | 4 |
Trace of D = 2 (tr.py):
- At state 0, I_τ = {a2: r1, a4: r3, ρ1..ρ4: r_k}. Transition 0 moves τ to σ̄ at all six vertices. τ(a_j) = g_j and τ(ρ_k) = e_k are
  not U-optimal.
- From state 1, W = Ξ at those vertices. r2 flips at t 2 without waiting (its W-route now goes through r1), and d1, d2 flip at t 2
  (c already reads r1).
- The h-wave reaches r4 at t 4, but u1 never becomes improving (r4's value now runs through a4's honest choice). A fallback at t 5
  pushes both pivots to the top, and λ changes at t 6.
- So v1 dies first on τ-stability. §4 says that fixing τ-stability alone will not be enough.

## 6. Next (OPEN, in order)
- (A) τ-ticks. Make each pivot tick also change τ at one Odd vertex (U-improving), so that every pivot cycle is a new phase inside one
  joint λ-run. A gate's W may then drop at the phase boundary and re-close without contradicting §1. This needs an Odd-side clock whose
  U-values leapfrog (the dual of a reactor). λ^U must stay fixed.
- (B) Length thresholds: equal path sets, decided by play length (S1: longest vs shortest by the cycle node's parity). Markers then
  stay free for the chain.
- (C) A clock that is not a pivot pair. For example, the two "worlds" could be the two parities of one counter digit, so that a gate's
  closed option can follow the digit's own world.

## DONE / FINDINGS / NEEDS
- DONE: mk3.py (v1, failed, kept for the record); this note; R107's embedded rows K 9-13 (the addendum in R107 §3).
- FINDINGS:
  1. READING: a super-polynomial total needs a super-polynomial joint λ-run (R47 Lemma Φ); odd-top ticks are ≤ 2n(n − 1).
  2. READING + DATA: mkr's ticks are W-cycle-node changes, monotone within a phase, so O(n²) per phase for pivot-tick clocks.
  3. READING: backpressure needs the closed link's current option to carry the high W (Ξ ⊴ W). For pivot-pair clocks, reusable gates
     force the threshold into h′'s band (§4).
  4. DATA: mk3 v1 fails on τ-stability (I_τ ≠ ∅ at state 0 at all gate and reader vertices).
- NEEDS: none from the owner.
