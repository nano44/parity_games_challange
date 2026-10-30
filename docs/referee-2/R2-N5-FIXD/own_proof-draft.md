### Lemma OWN (REFEREE-2's own; not in the packet; one referee only)
Let σ, σ′ be Even strategies that differ only on a set X of Even vertices, and let every x ∈ X be its own Ξ-cycle node under σ and under σ′
(λ_σ(x) = λ_σ′(x) = x). Then Ξ_σ = Ξ_σ′ (and S1's procedure returns the same σ̄ on every Odd vertex).
Proof (SPEC S1 procedure, read at l. 26-46 of docs/new/N5-ssi-global.md). Run the procedure for σ and for σ′ side by side. The loop order
(increasing reward) does not depend on the strategy. Induction hypothesis: at the start of the turn of v, the alive sets are equal and every
dead vertex has the same valuation and Odd choice in both runs.
- Fact 0. λ(x) = x holds iff x is alive at its own turn and passes test (i) (else x dies inside some R(c), c ≠ x, or later). So in both runs
  every x ∈ X is alive until its own turn and dies exactly at it.
- Fact 1. At the turn of v, no alive x ∈ X ∖ {v} reaches v in G_σ or in G_σ′ (through alive vertices): if v becomes a cycle node, x would lie
  in R(v) and get cycle node v ≠ x; if v is skipped but a DFS from v returns through x, that same walk makes v pass test (i) in that run,
  the same contradiction. Hence G_σ and G_σ′ have the same walks to v (a walk to v that uses an out-edge of some x ∈ X ∖ {v} would make x
  reach v; the out-edges of v itself are never used by a walk that ends at its first visit of v).
- (i) The DFS test for v ∉ X: a return walk through some x ∈ X is excluded by Fact 1 in either run, so the test has the same outcome. For
  v ∈ X it passes in both runs (Fact 0).
- (ii) R(v) is the same set in both runs (Fact 1).
- (iii)-(iv) The restricted graph on R(v) differs at most at the out-edges of v (X ∩ R(v) ⊆ {v}). Even u: M = vertices of R reaching v
  without passing u; Odd u: M = vertices reaching u without passing v; neither uses an out-edge of v (walks stop at v, or may not pass v).
  The deletions then remove the same edges outside v's out-edges. Longest path to v: length(v) = 0 is the base of the recursion; BFS from v
  over predecessors starts at v (already visited). Path sets, lengths and Odd's choices on R(v) ∖ {v} are equal.
- (v) Odd's own cycle-node choice (v Odd, so v ∉ X): a DFS-found return walk to v through some x ∈ X is excluded by Fact 1.
- (vi) Equal valuations and choices on R(v); the alive sets stay equal. □
Remark: no improvement hypothesis is used. The hypothesis «own under σ′» cannot be dropped (own_check.py control X_ONE: 8,104 / 8,104 pairs
differ).

### Corollary FLAT-SW (REFEREE-2's own proof of the packet's CONJECTURE; one referee only)
At every in-phase transition k → k + 1 of N5 or of N5-LZC with Ξ_{k+1} ≠ Ξ_k there is a switched Even x with Ξ_{k+1}(x) ▷ Ξ_k(x). In
particular every flat transition (FLATTR) contains a flat Even switch: FLAT-SW holds, and PHASE-RED′ is unconditional.
Proof. Ξ is a function of σ, so σ_{k+1} ≠ σ_k; let X be the switched Even vertices. λ_Ξ is constant on the phase (RESULTS R38 (a)), so each
x ∈ X is its own Ξ-cycle node at both states or at neither. If at both for every x ∈ X, Lemma OWN gives Ξ_{k+1} = Ξ_k, contrary to
assumption. So some x ∈ X is its own Ξ-cycle node at neither state. Its new target w has (x, w) ∈ Iσ_k (S4a: σ_new(x) ∈ A(x); S4c: by
definition; N5-LZC: box 73 §4 (a)). From here the proof of RESULTS R91 (i) SW-IN applies verbatim (it uses only (x, w) ∈ Iσ_k, R15 (a),
[V1], [V2]; not that the step is a fallback): Ξ_{k+1}(x) = x ⊕ Ξ_{k+1}(w) ▷ x ⊕ Ξ_k(σ_k x) = Ξ_k(x). In a transition without a DEPTH rise
this change is flat. □
