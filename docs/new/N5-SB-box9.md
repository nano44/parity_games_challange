# Box 9: one-player switch-best, in-phase structure (L-NEW successor 3; Lead brief 2026-10-21 21:06Z; committed 53da244 at 21:15Z, date -u)
Target: G-N5-TIME, K8's constant case = switch-best (= N5) on one-player games with cycles. Status: NO bound proved. One fact is proved,
one lemma is transferred to phases, and two conjectures are REFUTED with instances. Builds on N5-K8-box8.md §3b-§3d.

## 1. Proved: the next improving set avoids the previous arena
Fact A. Let ρ_{k+1} be the optimum of the arena H_k = {ρ_k-edges} ∪ I_k. Then I_{k+1} ∩ H_k = ∅.
Proof: ρ_{k+1} is optimal in H_k, so (VJ00 §5) no edge of H_k is an improvement of ρ_{k+1}. Improvements are computed in H with the
same valuation, because H_k's plays are H's plays. □
Check: p_strict/sb_union.py, 903 runs, 0 violations.

## 2. Refuted bounds (instances)
- "Every step brings an edge never seen in any earlier arena" (it would give ≤ |E| steps): FALSE in 42 of 903 runs (sb_union.txt).
- With the union reset at every λ-phase change (it would give ≤ (|E| + 1)(n(n−1) + 1)): FALSE in 2 of 903 runs (sb_union_phase.txt).
- Conjecture R, "within a phase only cycle-closing edges re-enter": FALSE in 4 of 4,508 runs (sb_conjR.txt).
- R2, "a step whose improving edges were all seen earlier in its phase is followed by a λ change": FALSE in 1 of 4,508 runs.
- Instance for both (n = 14; game and start in sb_conjR.txt):
  - Vertex 10 goes 11 → 9 (step 0) and back → 11 (step 2) inside one phase. The edge (10, 11) is not cycle-closing.
  - Successor 11's value overtook 9's after 11 itself switched at step 1: a plain leapfrog of two successors' values, as in CDAG.
  - Steps 2 and 3 bring only old edges; λ changes after step 3.
- So inside a phase, edges can re-enter freely. No edge-counting potential works.

## 3. Lemma T inside a phase (L-NEW reading, unrefereed)
Setting: a λ-phase; K_u = the vertices whose current cycle node is u; H^ph_u = the subgame on K_u with u given a self-loop. Inside
the phase:
- H-values on K_u equal H^ph_u-values: the plays stay in K_u, and u's real cycle has top u.
- An arena move that leaves K_u changes λ, which ends the phase.
Let ρ^ph be optimal in H^ph_u.
Lemma T^ph. If x ∈ K_u, λ^ph(x) = u, and y = ρ^ph(x) has reached its H^ph_u-optimal value, then x reaches its H^ph_u-optimal value one
step later, or the phase ends.
Proof: Lemma T (N5-K8-box8.md §3c), applied in H^ph_u. Case (iii) uses only that no cycle inside K_u is better for x than u, which
λ^ph(x) = u gives. The arena optimum in H dominates ρ_k[x → y] pointwise. □
Consequence: in each phase, the ρ^ph-forest into u is optimal within its depth. The only part a phase can drag out is BUILDING A
BETTER CYCLE inside K_u: the vertices with λ^ph ≠ u. Data: the build runs backward along the new cycle, one vertex per step
(n = 10 counterexample trace, box 8), but leapfrogs like the one in §2 can stall the front.
So K8's constant case reduces exactly to a bound on in-phase cycle building, as in box 8. This box adds no bound on it.

## 4. Files
p_strict/sb_union.py, sb_union_phase.py, sb_conjR.py, sb_reentry.py (+ .txt outputs).
