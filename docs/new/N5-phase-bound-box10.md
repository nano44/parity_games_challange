# Box 10 (ii): a λ-phase of one-player switch-best has at most n steps, so switch-best (= N5 on one-player games) is polynomial: O(n²·m) steps, ≤ n³ value-changing (L-NEW successor 4, Fable 5.1; written 2026-10-21 22:45Z by date -u)
Status: L-NEW READING with computer checks, NOT refereed. This is the "in-phase cycle-building bound" that N5-K8-box8.md §3c-§3d and
N5-SB-box9.md §3 left open. It closes K8's constant case for every one-player game (not only acyclic G_c, Lemma S) and gives
"N5 is polynomial on one-player games". It says nothing about two-player N5 runs (G-N5-TIME stays open); it is not a TARGET.md claim.

## 1. Setting and notation (as in N5-K8-box8.md §3c)
- H: a one-player parity game (⊖ out-degree 1; so a strategy ρ of ⊕ fixes every play), injective priorities (rank), VJ00 valuation
  Ω_ρ(x) = (c, P, ℓ): c = the most relevant vertex of the cycle the ρ-play from x ends in (the cycle node, λ_ρ(x) := c), P = the set of
  vertices on the ρ-path from x to c that are more relevant than c, ℓ = the length of that path. Order (better for ⊕): reward of c, then P by
  the most relevant vertex of the symmetric difference, then ℓ (longer better iff c is odd). Prefix: x ⊕ (c, P, ℓ) := (c, P ∪ {x if x more
  relevant than c}, ℓ + 1); this is the value of a play that steps from x to a vertex of value (c, P, ℓ) whose path to c avoids x.
- Switch-best: ρ_{k+1} = the optimal strategy of the arena H_k in which every vertex x may use {ρ_k(x)} ∪ I_k(x), I_k(x) = {z : Ω_k(z) ≻ Ω_k(ρ_k(x))}
  (VJ00 improving edges). Facts used: (F1) the optimum of a one-player game dominates every strategy of that game pointwise (VJ00 §5; Lemma F
  of N5-K10-box8.md), hence (F2) Ω_{k+1} ⪰ Ω_k pointwise because ρ_k ∈ H_k. Nothing else about the rule is used.
- λ-phase: a maximal run of steps during which no vertex changes its cycle node. Since values only rise and the cycle node is compared first,
  each vertex changes λ at most n − 1 times, so a run has at most n(n − 1) + 1 phases.
- Two elementary facts about values: (V1) if x is not its own cycle node then Ω_ρ(x) = x ⊕ Ω_ρ(ρ(x)) and the ρ-path from ρ(x) to λ(x)
  avoids x. (V2) PREFIX MONOTONICITY: if a ⪯ b are values whose paths both avoid x (or whose cycle nodes differ), then x ⊕ a ⪯ x ⊕ b, and
  strictly if a ≺ b. (Different cycle nodes: decided before the prefix. Same cycle node c: x is added to both sets or to neither, the
  symmetric difference is unchanged, both lengths grow by one.)

## 2. Lemma P (phase progress)
Let ρ_0, …, ρ_k be consecutive switch-best steps with λ_{ρ_j} = λ_{ρ_0} for all j ≤ k (one phase, k steps). Let u be a cycle node of ρ_0
(u = λ_0(u)). For a simple path r = (x = r_0, r_1, …, r_L = u) in H with L ≤ k edges let value(r) := (u, P(r), L), P(r) = {r_i : i < L, r_i more
relevant than u} (the value of a play that follows r and then any cycle through u with top u). Then
    Ω_k(x) ⪰ value(r)   for every vertex x and every such path r.
Proof by induction on k. k = 0: the only paths have L = 0, x = u, and Ω_0(u) = (u, ∅, 0) = value(r).
Step k → k + 1 (the phase still holds at k + 1): let r = x → z → r' with |r'| ≤ k, r' a simple path from z to u avoiding x. IH: Ω_k(z) ⪰ value(r').
Case A: (x, z) ∉ I_k, i.e. Ω_k(z) ⪯ Ω_k(ρ_k(x)). So value(r') ⪯ Ω_k(ρ_k(x)) (transitivity).
  A1: x is not its own cycle node. By (V1) and (V2) (both paths avoid x; or cycle nodes differ): value(r) = x ⊕ value(r') ⪯ x ⊕ Ω_k(ρ_k(x)) = Ω_k(x)
      ⪯ Ω_{k+1}(x) by (F2). (If the cycle node c of Ω_k(ρ_k(x)) differs from u, then value(r') ⪯ Ω_k(ρ_k(x)) forces c better than u, and the
      prefixed values are ordered the same way.)
  A2: x = λ_k(x) (its own cycle node), so Ω_k(x) = (x, ∅, 0). If x is better than u, Ω_k(x) ≻ value(r). If x is worse than u: Ω_k(ρ_k(x)) has cycle
      node x and value(r') has cycle node u, so value(r') ≻ Ω_k(ρ_k(x)), contradicting value(r') ⪯ Ω_k(ρ_k(x)).
Case B: (x, z) ∈ I_k, i.e. Ω_k(z) ≻ Ω_k(ρ_k(x)). Then ρ̂ := ρ_k[x → z] is a strategy of the arena H_k, so by (F1) Ω_{k+1}(x) ⪰ val_ρ̂(x).
  Let c := λ_k(z) and π := the ρ_k-path from z to c (simple, z first, c last).
  B1: x ∉ π. Sub-case x not on c's ρ_k-cycle: the ρ̂-play from x is x, π, then c's unchanged cycle, so val_ρ̂(x) = x ⊕ Ω_k(z) ⪰ x ⊕ value(r')
      = value(r) by (V2) (π and r' avoid x). Sub-case x on c's ρ_k-cycle (so λ_k(x) = c and, as cycle vertices are less relevant than c,
      P(Ω_k(ρ_k(x))) = ∅): the ρ̂-play from x is the cycle Z = x, π, then the arc of the old cycle from c back to x. Improvement means
      Ω_k(z) = (c, P(π), |π|) ≻ (c, ∅, ·): either P(π) ≠ ∅ with its most relevant vertex EVEN, or P(π) = ∅, c odd, |π| longer. In the first
      case top(Z) is that even vertex, more relevant than c, so val_ρ̂(x) has a cycle node better than c, hence by (F1) λ_{k+1}(x) ≠ c: the
      phase ended at step k + 1, contrary to the assumption. In the second case top(Z) = c and val_ρ̂(x) = (c, ∅, |π| + 1) = x ⊕ Ω_k(z) ⪰ value(r).
  B2: x ∈ π. Then the ρ̂-play from x is the cycle Z = x, z, π[z..x) (π up to but excluding x), and λ_k(x) = c (x lies on z's path to c).
      P(Ω_k(z)) = P(π[z..x)) ∪ P(Ω_k(x)) and P(Ω_k(ρ_k(x))) = P(Ω_k(x)) \ {x}, the two parts disjoint, so the symmetric difference is
      D = P(π[z..x)) ∪ ({x} if x is more relevant than c). Improvement means: D ≠ ∅ with its most relevant vertex even, or D = ∅, c odd, longer.
      If D ≠ ∅: every vertex of Z more relevant than c lies in D, so top(Z) is that even vertex, better than c, and as in B1 the phase ends at
      step k + 1: contradiction. If D = ∅: no vertex of Z is more relevant than c. If top(Z) ≠ c then top(Z) is less relevant than the odd c,
      so its reward is better for ⊕ (even: positive; odd: −p' larger), and again the phase ends: contradiction. If top(Z) = c then c ∈ Z ⊆
      {x} ∪ π[z..x), and since π is a simple path ending at c, c = x: x is its own cycle node and Ω_k(x) = (x, ∅, 0) = val_ρ̂(x) (the flat
      cycle-closing switch of N5-killer-box4.md §3). Then: if x is better than u, Ω_{k+1}(x) ⪰ Ω_k(x) ≻ value(r). If x is worse than u, then
      Ω_k(z) has cycle node c = x (z's path ends at x) while value(r') has cycle node u, contradicting IH Ω_k(z) ⪰ value(r'). □

## 3. Theorem (phase length) and corollaries
Theorem PH. In a λ-phase of switch-best on a one-player game with n vertices and m edges, after n − 1 steps every further step inside the
phase is value-flat (changes no valuation), and there are fewer than m such steps. So a phase has fewer than n + m steps.
Proof. Suppose ρ_0, …, ρ_{n−1} lie in one phase (n − 1 steps). Every simple path has at most n − 1 edges, so Lemma P with k = n − 1 gives
Ω_{n−1}(x) ⪰ value(r) for every vertex x, every cycle node u and every simple path r from x to u. Let (x, z) ∈ I_{n−1}, c := λ(z), π := the
path from z to c.
- If x ∉ π and x is not on c's cycle: r := x, π is a simple path to the cycle node c, so Ω_{n−1}(x) ⪰ x ⊕ Ω_{n−1}(z). If x is not its own
  cycle node, (V1) and strict (V2) give Ω_{n−1}(ρ(x)) ⪰ Ω_{n−1}(z): not improving. If x is its own cycle node, Ω_{n−1}(x) = (x, ∅, 0) ⪰
  (c, …) with x ≠ c forces x better than c, so Ω_{n−1}(ρ(x)) (cycle node x) ≻ Ω_{n−1}(z) (cycle node c): not improving. Contradiction.
- Otherwise the switch closes a cycle Z, and the case analysis B1/B2 of Lemma P applies verbatim to k = n − 1: either val_ρ̂(x) has a cycle
  node better than λ(x), so step n changes λ(x) (by (F1)) and the phase ends; or (B1, second case) val_ρ̂(x) = x ⊕ Ω_{n−1}(z) ≻ Ω_{n−1}(x)
  with r = x, π simple, contradicting Lemma P; or (B2, D = ∅, top(Z) = x) the switch is value-flat: x is its own cycle node and every option
  of x in the arena gives x the value (x, ∅, 0).
So every improving edge of ρ_{n−1} is λ-changing or value-flat. If some λ-changing one exists, step n ends the phase. Otherwise step n is
value-flat: it switches only vertices x that are their own cycle nodes, each to some z ∈ I(x), i.e. with Ω(z) ≻ Ω(ρ(x)) (the arena at x is
{ρ(x)} ∪ I(x) and all options tie in x's value, so the engine's tie-break decides); no valuation changes (every play that met x still meets x
with the same path set), so every improving set is unchanged except I(x) ⊆ {w : Ω(w) ≻ Ω(z)}, which lost z and everything below it. The same
holds at ρ_{n+1}, …: as long as the phase lasts, every step is flat and strictly raises Ω(ρ(x)) at each switched x within x's fixed successor
values. So there are at most Σ_x (deg(x) − 1) < m flat steps, after which no improving edge is left and the run stops (or a λ change ends
the phase first). □
Remark. Value-flat steps are the cycle-closing switches of N5-killer-box4.md §3 (Ξ unchanged); switch-best's engine may or may not take them
(N5 takes them in its fallback, S4c, which switches each such x to its Ω-best improving successor at once, after which I = ∅).
Tightness (23:11Z by date -u). The bound n − 1 value-changing steps per phase is attained: phase_climb.py with FIT=rel (fitness = phase
length − n, growth allowed) found phases of exactly n − 1 steps, all value-changing, at n = 12 and n = 16 (instances/phase/rel_g12.pg,
rel_g16.pg; phase_vc.py), and 46 at n = 48 (ph_n48.pg). No climb exceeded n − 1 (tail/logs/rel_*.log, phase_vc.txt: 17 instances, 0 violations). Note: phase_climb.py's "maxphase" is the number of
λ-observations in the phase = steps + 1, so a logged "maxphase − n = 0" (rel_g12, sha1 20db1b22…) is a phase of n − 1 = 11 steps; phase_vc.py
counts steps and is the reference (11 steps, 11 value-changing; Lemma P checked on it: 525 checks, 0 violations).
Corollary 1 (switch-best is polynomial on one-player games). At most n(n − 1) + 1 phases of fewer than n + m steps: fewer than
(n² − n + 1)(n + m) steps, i.e. O(n²·m) (≤ n³ − n² + n value-changing steps in all).
Corollary 2 (N5 on one-player games). On a game in which one player has out-degree 1 everywhere, N5's step for the other player is
switch-best (N5-K9-Pstrict-counter.md §5); N5's fallback fires only when the arena optimum returns σ unchanged although Iσ ≠ ∅, which by the
Theorem's argument happens only in the value-flat situation, and the fallback then leaves no improving edge. So N5 makes fewer than
(n² − n + 1)(n + m) iterations on one-player games. This closes K8's constant case (τ = τ_sb(k) = c constant, Even's steps = switch-best on
G_c; N5-K8-box6.md §1, N5-K9-Pstrict-counter.md §5) for EVERY G_c, cyclic or not, and the "cycle tops" part of SB1' (N5-K8-box8.md §3c): the
O(n) conjecture SB1' itself stays open; the bound proved is n − 1 value-changing steps per phase.
Corollary 3 (VJ00 Prop. 7.4). BRICS RS-00-48 Prop. 7.4 states O(n³) improvement steps on one-player games without proof (L-LIT T22 asked for
which rule). For the arena-optimum (switch-best) rule, Corollary 1 gives O(n³) value-changing steps (O(n²·m) with flat steps); for arbitrary
single switches the statement is false (CDAG_n, N5-K9-Pstrict-counter.md). Not an attribution claim: VJ00's intended rule is L-LIT's question.
What this does NOT give: a bound for N5 on two-player games. There Even's step is the optimum against Odd's CURRENT τ_k with the honest
improving set, which is switch-best on G_c only when τ_k = c (N5-K10-box8.md §4 (d)); the frozen-σ tail (N5-tail-box10.md) is Odd's
switch-best on G_σ only when τ̄ = σ, which never happens on the long instances (N5-SB-box9.md §5). G-N5-TIME stays open.

## 4. Computer checks (experiments/new/tail/)
- lemmaP_check.py: for every in-phase step k, every vertex x and every cycle node u of ρ_0, the best value over all simple paths from x to u
  with at most k edges (DFS enumeration) is compared with Ω_k(x) (L-SI's engine, read-only). Random one-player games: 2,000 games × 2 starts
  at n ≤ 7 (1,837 checks), 300 × 2 at n ≤ 8 (288), 150 × 2 at n ≤ 9 (100), 400 × 2 at n ≤ 10 (463): 0 violations. Climbed long-phase
  instances (sb1_counter_n10/n16, phase/fl_n16, ph_n16, ph_g16, fl_g16; a 12-step phase at n = 16): 1,317 checks, 0 violations
  (tail/logs/lemmaP_inst.txt, lemmaP_rand.txt). Also checked there: no phase longer than n. Re-run with EVERY phase of a run checked (the table
  of simple paths is rebuilt at each λ change; lemmaP_inst_allphases.txt): rel_g12, rel_g16 (the tight n − 1 phases), fl_n16, ph_n16,
  sb1_counter_n10/n16: 3,239 checks, 0 violations; random n ≤ 9, 500 games × 2 starts: 613 checks, 0 violations.
- phase_climb.py (fitness = longest phase; or FIT=flips = most switches of one vertex inside a phase): longest phase 46 steps at n = 48
  (instances/phase/ph_n48.pg, the whole run but one step; the phase builds a 47-vertex cycle backwards, one vertex per step; n5.run gives the
  same 47 iterations, regions = Zielonka, verify.py OK); 13 at n = 16 and n = 24; 46 at n = 49 with growth. Never above n − 2.
  Most switches of one vertex inside one phase: 6 at n = 16 (fl_n16: 0→5→4→0→13→5→0, the whole run is one phase that ends optimal, so the
  vertex is simply deep in the optimal tree), 7 at n = 32, 8 at n = 18 with growth. Consistent with ≤ depth ≤ n per vertex per phase.
- f1_check.py: the two facts used, (F1) the arena optimum dominates every single-switch arena strategy ρ_k[x → z] pointwise and (F2)
  Ω_{k+1} ⪰ Ω_k pointwise, checked directly with the engine on random one-player games: 1,500 games (n ≤ 12) and 300 games (n ≤ 20), 2 starts
  each, 4,769 steps, 209,732 vertex comparisons, 0 violations.
- phase_trace.py: per-phase traces (sb1_counter_n48: the 17-step phase is the backward build of the cycle 30..47, each vertex once, 31 twice).

## 5. The two-player bridge: Lemma P's statement is FALSE for N5's Even moves inside a σ̄-segment (instances; written 22:57Z by date -u)
K9 (N5-oneplayer-box7.md, referee-signed conditional on a one-player premise) bounds N5's iterations by the number of best-reply changes
times a per-segment bound. Inside a σ̄-segment (Odd's best reply σ̄ = c constant) Even's honest values Ξσ are the values in the one-player game
G_c, so the natural bridge is (P-N5): Lemma P's conclusion for N5's Even-moving iterations inside one λ-phase of one segment, with simple paths
of G_c. Test: experiments/new/tail/segP_check.py (DFS over simple paths of G_c, honest values from the engine, N5's loop unmodified).
- Random two-player games n ≤ 9 (300 games): 109 checks, 0 violations, but segments are short (≤ 2 Even moves).
- Lane instances n ≤ 16 and DLM modules: 239 checks, 0 violations; longest in-phase Even-move count 7 (seg_n16).
- Climbed instances (tail/seg_climb.py, fitness = Even moves inside one λ-phase of one segment): (P-N5) FALSE. instances/seg10/seg_r16.pg
  (n = 16, sha1 a4d7333ed40674cd5d06800eaf2ee6f32db25258): at k = 4 Even moves, vertex 1 (Even) has Ξ(1) = (12, {15 only…}, 3) while the simple
  path 1 → 15 → 10 → 14 → 12 (4 edges, Odd-forced after the first hop, so its value is constant in the segment) is better; the first hop (1, 15)
  is honest-improving at every step of the segment and is never taken: Even's arena optimum against the CURRENT τ_k prefers 10, then 13.
  instances/seg10/seg_n24.pg (sha1 1c5c6f22…): already at k = 1, vertex 1 has cycle node 12 while its direct edge to the cycle node 11 (better)
  is honest-improving and not taken (x does not move at all: a K1 stall). 204 violations over the three climbed instances; 0 (SEG-LEN) violations.
- Diagnosis: the induction step of Lemma P uses (F1) in Case B: the arena optimum dominates the single honest switch ρ̂ = σ[x → z]. In N5 the
  arena optimum maximises V_{σ,τ_k} (against Odd's current τ_k) while the gate and the progress measure are honest (against c). A K1 stall
  (N5-killer-box4.md) is exactly a vertex where the honest switch is available and the τ_k-optimum refuses it; stalls lasting ≥ 4 Even moves
  exist (seg_r16). So the one-player argument does not transfer; this is the obstruction with an instance.
- What survives on data, (SEG-LEN): Even moves inside one λ-phase of one σ̄-segment ≤ n − 1. Climbs: 12 at n = 16 (three seeds), 11 at n = 16
  (grown from 12), 17 at n = 20, 8 at n = 24 (seeded from best_n24), all < n − 1; every improved best re-run through n5.run, regions = Zielonka,
  verify.py OK (tail/logs/seg_*.log). Together with K9's structure, (SEG-LEN) plus a polynomial bound on best-reply changes would bound N5;
  neither is proved, and K9's remaining premise is now (SEG-LEN) for Even and its dual for Odd, not the one-player bound (which is Theorem PH).
- UPDATE (23:12Z by date -u): with the climb fitness restricted to VALUE-CHANGING Even moves (FIT=vc; an Even-moving iteration counts iff Ξσ
  changes somewhere; Ξσ does not depend on τ), the two-player count EXCEEDS the one-player bound: instances/seg10/vc_g25.pg (n = 25, 15 Even
  vertices, sha1 0ffe46db056823a82b1f72f0fd78dfec774a7b9d): one σ̄-segment λ-phase spans the whole run (iterations 0..26) with 27 Even-moving
  iterations, 25 of them value-changing (> n − 1 = 24) and 2 value-flat; vc_g17.pg (n = 21, sha1 813cfeed…): 20 value-changing (= n − 1).
  Both re-run through n5.run: regions = Zielonka, verify.py OK (tail/logs/vc_*.log; tail/segtrace.py shows the per-iteration moves: vertex 4
  oscillates 5 → 2 → 5 → 2 inside the segment, up to 10 Even vertices stalled at once). So no statement of the form "Even moves per segment
  λ-phase ≤ n − 1" holds for two-player N5 even in value-changing form; the K1 stalls cost real steps. On all data the count stays ≈ n
  (climb maxima 25 at n = 25, 20 at n = 21, 17 at n = 20, 14 at n = 16/24/32); no growth beyond linear was found, and no bound is proved.
- FINAL climb numbers (23:24Z by date -u; every climb finished; tail/box10_instances.sha1 pins every instance): value-changing Even moves in one
  σ̄-segment λ-phase: 26 at n = 25 (vc_g25.pg, sha1 243f890d34cad9991cc7e11cc73d7b718f885ff0; 27 Even-moving iterations, 26 value-changing, 1 flat,
  n5.run 27 iterations, Zielonka + verify.py OK), 20 at n = 21 (vc_g17), 18 at n = 24 (vc_g20, all value-changing), 17 at n = 24 (vc_r24), 13 at
  n = 16 (vc_r16). One-player phases (phase_vc.py over all 20 phase instances): 0 violations of Theorem PH, maximum exactly n − 1.
