# N8d-R2: gauntlet step 4, written proofs (L-NEW successor 6, Opus 5.5; box 17 (b))
Started 2026-10-23 10:49Z (date -u), on the Lead's GO of 10:19Z. Object: N8d-R2 = docs/new/N8d-single.md §0 (rules frozen at d7fadfbf)
together with §0b (C1-C5 pinned at bb9f64f5) and §0c (C1 corrected to the COMPRESSED map, Lead reading 10:48Z). Under D1 every statement here is wrong until refereed. Each one carries a label:
- **PROVED**: a full proof is written here; it still needs two referees.
- **READING**: an argument or interpretation, not a proof.
- **OPEN**: not known.
- **DATA**: measured, with the committed file named.

**No running-time claim is made. R2 has no polynomial bound, expected or otherwise (§3). Correctness is §2.**

## 0. Sources opened in this box
- Koh-Loho, "Beyond value iteration for parity games: strategy iteration with universal trees", arXiv 2108.13338**v5** (LMCS version),
  e-print fetched 2026-10-23 10:23Z (file mtime, date -r), sha256 7189eb2f673866257dd887bdfe0d660aa76ba821dd9ba830d85bb2105a5c816c (the same file as L-COMP's
  experiments/n8d-second/README.md). Read in the LaTeX source.
  - Numbering: lmcs.cls l.685-699 numbers every theorem-like environment on one counter per section.
  - §1 intro.tex l.13: positional determinacy, citing Martin 1975 and Emerson-Jutla FOCS 1991. Those two papers were NOT opened; I use
    only Koh-Loho's statement of the result.
  - §2 prelim.tex: [d], positional strategies τ: V_1 -> V, the graph G_τ, p-truncation, ⊤ with ⊤|_p = ⊤, feasibility, violated / tight /
    loose arcs, Tighten and lift, Prop 2.5 (Knaster-Tarski variant, parts (i)-(iii)), the operators Lift_v (Even v) and Lift_vw (Odd v).
    Also the sentence "a node labeling is a fixed point of H↑ if and only if it is feasible in H".
  - Theorem 2.3: "Given an (n, d/2)-universal tree T, let µ* be a node labeling which is feasible in G and has maximal finite support.
    Then Even wins from v iff µ*(v) ≠ ⊤" (cited there to Jurdziński STACS 2000).
  - Lemma 2.4 (Cycle Lemma): if µ is feasible in a cycle C and µ(v) ≠ ⊤ for some v in C, then C is even.
  - The sentence "the perfect ℓ-ary tree of height h" is "(ℓ, h)-universal" (§2.1).
  - §3 strategy-iteration.tex: Algorithm 1; "admissible" = a violated arc vw with v ∈ V_1; the invariants (1) µ feasible in G_τ and
    (2) no loose arcs in G_τ; Theorem 3.1 with its proof (quoted in §2.3 below).
  - §4 label-setting.tex: Algorithm 3 (its caption requires "G_τ does not contain loose arcs"), Theorem 4.5 ("Algorithm 3 returns
    µ^{G_τ↑}"), Corollary 4.4, Theorem 4.3 with its proof (uses |V(P)| ≤ n), Remark 4.6.
- Kelner-Spielman, "A randomized polynomial-time simplex algorithm for linear programming", STOC 2006. Author PDF
  math.mit.edu/~kelner/publications/SimplexStoc.pdf, fetched 10:35Z (file mtime, date -r), sha256 3b5f68fe88c9cd46…. Read: the abstract, §1-2 (shadow-vertex
  method on a polytope {x : Ax ≤ b} with a random right-hand side), Theorem 3.2 (expected shadow size for a perturbed polytope in isotropic
  position) and Theorem 6.3 (CheckBoundedness in O(n³L) iterations w.h.p.). Used in §3.4 only.
- Reused, not re-opened: Friedmann's thesis Thm 4.76 / Lemma 4.75 / Thm 4.78, via N8d-barrier.md §0 and §4 and L-LIT T26. Also L-RED R55 §3
  and R56 §1 (mechanisms M1, M2).

## 1. Setting (from §0 and §0b)
- Input: a parity game with n vertices, max-parity, priorities p(v) ≥ 0. Write V_0 for Even's vertices and V_1 for Odd's.
- Priority map (C1, canonical per §0c): π = the order- and parity-preserving compression of p into [d], d even (kl.py Game.__init__), so
  d ≤ 2n and h ≤ n. The tested variant π = p + 2 (kl2.py) is covered by every statement of §2 as well. Both maps preserve order and
  parity, so every infinite play has the same winner under π as under p.
- Tree T (C2): the perfect n-ary tree of height h = d/2, M = {0, ..., n-1}. Leaves are h-tuples (ξ_{d-1}, ξ_{d-3}, ..., ξ_1). L̄ = L(T)
  ∪ {⊤} is ordered lexicographically, with ⊤ on top. ℒ is the lattice of labellings µ: V -> L̄, ordered pointwise.
- Algorithm 1 with the single-switch rule R2. Start: µ_0 = min L(T) at every node and τ_1 = the first successor (C3). Initial step:
  µ ← µ_0^{G_τ↑}. While some Odd node v has an admissible arc:
  - draw such a v uniformly at random;
  - set τ(v) to its admissible arc with the largest Tighten (ties: smallest successor id);
  - set µ ← µ^{G_τ↑}.
  Here G_τ↑ = {Lift_v : v ∈ V_0} ∪ {Lift_{vτ(v)} : v ∈ V_1}, and G↑ = {Lift_v : v ∈ V_0} ∪ {Lift_vw : v ∈ V_1, vw ∈ E}.
- Least fixed point step: µ^{G_τ↑} is computed by Algorithm 3 (base-node lifts, then Algorithm 2). Theorem 4.5 makes this exact when
  the input µ has no loose arcs in G_τ. Lemma 2.1 (i) below shows the input always satisfies this.
- Dual run (C4): owners swapped, priorities p + 1, then C1's compression. C5 reads Even's strategy off the final labels.
- Throughout, "single admissible switch rule" means ANY rule that changes τ at exactly one Odd node v, to an admissible arc vw. R1, and R2
  under every seed, are such rules. The arc choice inside the node is irrelevant to §2.

Two facts used repeatedly; both are immediate from the definitions in §2.2 of the paper:
- (T1) Truncation is monotone: ξ ≤ ζ implies ξ|_p ≤ ζ|_p. A lexicographic order restricts to an order on prefixes, and ⊤|_p = ⊤.
- (T2) For an arc vw with p = π(v), the arc is violated w.r.t. µ iff:
  - p even: µ(v)|_p < µ(w)|_p;
  - p odd: µ(v)|_p ≤ µ(w)|_p and not µ(v) = µ(w) = ⊤.
  In particular an arc out of a ⊤-labelled vertex is never violated. Also lift(µ, vw) = µ(v) iff vw is not violated, and lift(µ, vw) > µ(v)
  iff vw is violated.

## 2. Correctness (gauntlet step 4, first half)

### Lemma 2.1 (one admissible switch keeps Algorithm 1's invariants and forces an increase). PROVED
Let µ be a fixed point of G_τ↑ with no loose arc in G_τ. Let τ' differ from τ only at v ∈ V_1, with τ'(v) = w and vw admissible
(violated) w.r.t. µ. Let µ' = µ^{G_τ'↑}. Then:
- (i) µ has no loose arc in G_τ'. So Algorithm 3's precondition holds, and Algorithm 3 returns µ' (Theorem 4.5).
- (ii) µ' ≥ µ pointwise, and µ'(v)|_{π(v)} > µ(v)|_{π(v)}. In particular µ'(v) > µ(v).
- (iii) µ' is feasible in G_τ' and has no loose arc in G_τ'.

Proof.
- (i) E(G_τ') = (E(G_τ) \ {vτ(v)}) ∪ {vw}. Every arc of E(G_τ) is not loose w.r.t. µ, by hypothesis. vw is violated, hence not loose:
  loose means non-violated and not tight.
- (ii) µ' ≥ µ: µ' is the least fixed point of G_τ'↑ that is AT LEAST µ (Prop 2.5 (i)).
  Let p = π(v). Since µ' is a fixed point of Lift_vw, the arc vw is not violated w.r.t. µ' (T2). The arc is violated w.r.t. µ, so
  µ(v) ≠ ⊤ (T2). If µ'(v) = ⊤, then µ'(v)|_p = ⊤ > µ(v)|_p and we are done. Otherwise µ'(v) is finite and:
  - p odd: µ'(v)|_p > µ'(w)|_p ≥ µ(w)|_p ≥ µ(v)|_p. The steps are, in order: non-violation w.r.t. µ' (the clause "both ⊤" is excluded
    because µ'(v) ≠ ⊤); then µ' ≥ µ and T1; then violation w.r.t. µ.
  - p even: µ'(v)|_p ≥ µ'(w)|_p ≥ µ(w)|_p > µ(v)|_p, by the same three steps.
  Either way µ'(v)|_p > µ(v)|_p. By T1 this forces µ'(v) > µ(v).
- (iii) A fixed point of G_τ'↑ is exactly a labelling feasible in G_τ' (paper §2.3), so µ' is feasible in G_τ'.
  Suppose some arc xy of G_τ' were loose w.r.t. µ': xy is not violated and µ'(x) > t := Tighten(µ', xy). Then t ≠ ⊤ and µ'(y) ≠ ⊤.
  - Case µ'(x) = µ(x). Then xy is an arc of G_τ (the new arc vw is excluded, because µ'(v) > µ(v) by (ii)), and xy is not loose w.r.t. µ.
    So µ(x) ≤ Tighten(µ, xy): if violated, µ(x) < Tighten; if tight, equal. Tighten(µ, xy) depends only on µ(y) and π(x), and is monotone
    in µ(y). Hence µ'(x) = µ(x) ≤ Tighten(µ, xy) ≤ Tighten(µ', xy) = t, a contradiction.
  - Case µ'(x) > µ(x). Define µ'' = µ' except µ''(x) = max(µ(x), t) < µ'(x). We check that µ'' is a fixed point of G_τ'↑:
    - At x: lift(µ'', xy) = max(µ''(x), Tighten(µ'', xy)) = max(µ''(x), t) = µ''(x). Here Tighten(µ'', xy) = t because Tighten depends
      only on the head's label and µ''(y) = µ'(y) when y ≠ x (self-loops below).
      - If x ∈ V_1, its single operator Lift_{xy} fixes µ''(x).
      - If x ∈ V_0, then Lift_x(µ'', x) = min_z lift(µ'', xz) ≤ µ''(x). Every lift is ≥ µ''(x) (lift is inflationary), so equality holds.
    - At any z ≠ x: lift(µ'', zu) ≤ lift(µ', zu) for every arc zu, by monotonicity of lift in the labels of heads. Also µ''(z) = µ'(z) is
      a fixed point value, so Lift_z(µ'', z) ≤ Lift_z(µ', z) = µ'(z) = µ''(z) (resp. Lift_{zτ'(z)}). Inflation gives ≥. So z is fixed too.
    Self-loop y = x: an odd self-loop is never loose, since Tighten(µ, xx) > µ(x) when π(x) is odd. For an even one, t is the least leaf
    below µ'(x)|_{π(x)}. Then t ≤ µ''(x) ≤ µ'(x) gives µ''(x)|_{π(x)} = µ'(x)|_{π(x)} (T1), so Tighten(µ'', xx) = t, as used above.
    Thus µ'' is a fixed point of G_τ'↑ with µ ≤ µ'' < µ', contradicting the minimality of µ' (Prop 2.5 (i)).
∎

The paper states (2) without proof ("due to the minimality of µ^{G_τ'↑}"); (iii) is that proof. The initial state also qualifies: µ_0 =
min L(T) everywhere has no loose arc (looseness needs µ_0(x) > Tighten ≥ min L(T)). So by Theorem 4.5, µ_0^{G_τ1↑} is computed exactly,
and (iii) applies to it with τ = τ' = τ_1.

### Lemma 2.2 (every iterate is below µ*). PROVED
Let µ* be the least fixed point of G↑ (exists by Prop 2.5 (i), starting from µ_0). Every labelling µ_k computed by Algorithm 1, under any
single admissible switch rule, satisfies µ_k ≤ µ*.

Proof. G_τ↑ ⊆ G↑ for every τ, because the Even operators coincide and each Lift_{vτ(v)} is one of the Lift_vw. Induct on k.
- µ_0 = min ≤ µ*.
- If µ_k ≤ µ*, then µ_{k+1} = µ_k^{G_τ↑} ≤ µ*^{G_τ↑} by Prop 2.5 (iii). Also µ*^{G_τ↑} = µ*, because µ* is fixed by every operator of
  G↑ and hence of G_τ↑, so the least fixed point above µ* is µ* itself.
∎

### Theorem 2.3 (termination, output, iteration bound, for every single admissible switch rule). PROVED
Algorithm 1 with any single admissible switch rule terminates after at most n·n^h pivots (≤ n^{n+1} under the canonical C1, h ≤ n),
whatever the random choices. It returns µ*, the
pointwise least labelling feasible in G.

Proof.
- Bound. Let r(ξ) be the rank of ξ in L̄ (0 for min L(T), n^h for ⊤), and R(µ) = Σ_v r(µ(v)) ∈ [0, n·n^h]. By Lemma 2.1 (ii), each pivot
  gives µ' ≥ µ and µ'(v) > µ(v). So R increases by at least 1 per pivot, and there are at most n·n^h pivots.
- At termination no Odd arc is violated. Every Lift_vw (v ∈ V_1) fixes µ (T2), and the Even operators fix µ by Lemma 2.1 (iii). So µ is
  a fixed point of G↑ that is ≥ µ_0, hence µ ≥ µ*. Lemma 2.2 gives µ ≤ µ*. So µ = µ*.
- Pointwise least feasible labelling: feasible in G = fixed point of G↑ (paper §2.3), and every fixed point is ≥ µ_0, hence ≥ µ*.
∎

On the paper's own proof: Theorem 3.1 says "The node labeling µ is monotone increasing in every iteration. Since ℒ is finite and the
all-top node labeling is feasible in G, the algorithm terminates." Termination needs a STRICT increase per iteration. For a single switch
that is Lemma 2.1 (ii). (For switching several arcs at once the same argument applies at any one switched node.) The rest of its proof is
Lemma 2.2 plus the fixed-point identification, as above. §0 of N8d-single.md wrote "termination ≤ n·|L(T)| iterations"; that bound is the
R-argument here (|L(T)| = n^h), not a sentence of the paper.

### Corollary 2.4 (winning regions). PROVED (modulo Theorem 2.3 of the paper)
Let W_0 = {v : µ*(v) ≠ ⊤}. Then W_0 is exactly the set from which Even wins.

Proof. µ* is feasible in G (Thm 2.3 above). Every feasible µ' satisfies µ' ≥ µ*, so its finite support is contained in µ*'s. So µ* has
maximal finite support. T is (n, d/2)-universal (paper §2.1: the perfect n-ary tree of height h = d/2). The paper's Theorem 2.3 applies,
with the same winner under π as under p (§1). ∎

### Lemma 2.5 (Even's strategy, C5). PROVED
For v ∈ V_0 ∩ W_0, let σ(v) be any successor w with vw not violated w.r.t. µ*; C5 takes the one with the least label, ties smallest id.
Such a w exists, and σ (extended arbitrarily outside W_0) is a positional strategy winning for Even from every vertex of W_0.

Proof.
- Existence. µ* is a fixed point of Lift_v, so min_w lift(µ*, vw) = µ*(v). Some arc attains lift = µ*(v), i.e. is not violated (T2).
- Closure.
  - If µ*(x) ≠ ⊤ and xy is not violated, then µ*(y) ≠ ⊤. For odd π(x): µ*(x)|_p > µ*(y)|_p with µ*(x)|_p finite. For even π(x):
    µ*(x)|_p ≥ µ*(y)|_p. In both cases µ*(y)|_p ≠ ⊤, i.e. µ*(y) ≠ ⊤.
  - At x ∈ V_1 ∩ W_0 every arc is non-violated, since Algorithm 1 stopped with no admissible arc.
  - At x ∈ V_0 ∩ W_0 the arc xσ(x) is non-violated.
  So every play from W_0 consistent with σ stays in W_0 and uses only non-violated arcs. Call that arc set H.
- Cycles of H. Let C be a cycle in H. Every vertex of C has its one C-arc non-violated, so µ* is feasible in C (feasibility in C needs a
  single out-arc per vertex). µ* is finite on C, so C is even by the paper's Cycle Lemma 2.4.
- Plays. Let ρ be an infinite play from W_0 consistent with σ, and q its largest priority seen infinitely often. Pick a vertex x of
  priority q visited infinitely often, and a time t after which no priority > q occurs. Take two visits of x after t. The walk between them
  is closed. Deleting internal repetitions gives a simple cycle through x, all of whose vertices lie on the walk. So it is a cycle of H with
  top priority exactly q. It is even, so q is even and Even wins ρ.
∎

### Lemma 2.6 (Odd's strategy and region via the dual run, C4). PROVED (determinacy cited)
Let G^d have owners swapped and priorities p + 1. Run Algorithm 1 on G^d, getting µ*_d, W^d_0 = {µ*_d ≠ ⊤} and σ^d (Lemma 2.5 on G^d).
Then:
- σ^d is a positional strategy for Odd in G, winning from W^d_0;
- W^d_0 is exactly Odd's winning region in G;
- W^d_0 = V \ W_0, so the assertion "primal and dual regions disagree" in kl.py / kl_single.py / kl2.py can never fire on a correct run.

Proof.
- Correspondence. Strategies of Even in G^d are exactly strategies of Odd in G, and plays are the same sequences. The largest priority seen
  infinitely often under p + 1 is (that under p) + 1. It is even iff the one under p is odd. So Even^d wins a play iff Odd wins it in G.
- Lemma 2.5 and Corollary 2.4 applied to G^d (any single admissible switch rule, any seed) give that σ^d wins for Odd from W^d_0, and that
  W^d_0 is Odd's winning region.
- W_0 ∩ W^d_0 = ∅: at a common vertex, the play consistent with σ and σ^d would be won by both players.
- W_0 ∪ W^d_0 = V: positional determinacy (Koh-Loho §1, l.13, citing Martin 1975 and Emerson-Jutla 1991; those two were not opened).
  Independently, the harness checks it on every instance: verify.py checks both strategies on their regions.
∎

### Remark 2.7 (what step 4's correctness half does NOT cover). READING
- Fidelity: that kl_single.py / kl.py and kl2.py implement §1 is a referee and CHECKER question (TARGET §6, D2 change 2).
  - kl2's selfcheck compares Algorithm 3 with naive lifting at every pivot; kl's fidelity.txt runs 850 cross-checks.
  - The C1 difference between the two codes is §0b's. Lemmas 2.1-2.6 hold verbatim for kl.py's compressed map too. Nothing above uses
    which order- and parity-preserving map into [d] was chosen, except the value of h in the bound of Theorem 2.3.
- Arithmetic cost per pivot (TARGET §3): labels are h-tuples over {0..n-1}, i.e. O(d log n) bits. Algorithm 3 costs O(d(m + n log n))
  tuple-component operations (Theorem 4.5), so each pivot is polynomial at bit cost. Polynomial total time is equivalent to a polynomial
  number of pivots. That is §3.

## 3. Expected number of pivots (gauntlet step 4, second half): attempts and where each breaks
Target statement, **OPEN**: for some polynomial q, for every game, E_seed[#pivots of R2] ≤ q(n), with C1 the canonical compressed map
(d ≤ 2n), as for the TARGET.md §1 input (priorities in {0..n}). This is an M4-R statement (D2 change 4).
I do not believe I have it; nothing below comes close. Each attempt is written as the claim it would need, the PROVED part, and the exact
break with the instance that shows it.

### 3.0 Facts any argument can use. PROVED
For any single admissible switch rule, along any run:
- (a) µ_k is pointwise non-decreasing and µ_k ≤ µ* (Lemma 2.1 (ii), Lemma 2.2).
- (b) For each vertex v and each j ≤ h, the length-j prefix of µ_k(v) is non-decreasing in k (T1 applied to (a)). If it ever equals
  µ*(v)'s length-j prefix, it stays equal: it is squeezed between itself and µ*'s prefix, by (a) and T1.
- (c) Each switch at v strictly raises µ(v)|_{π(v)} (Lemma 2.1 (ii)). A vertex labelled ⊤ is never a candidate (T2).
  Hence **v switches at most n^{k(v)} times** (a strict chain in the n^{k(v)} + 1 values of the truncation, ⊤ included), where k(v) is the number of label components kept by the π(v)-truncation, i.e. the
  number of odd indices in [π(v), d-1]. In particular, an Odd vertex with π(v) = d - 1 switches at most n times, and one with
  π(v) = d at most once (straight to ⊤). Checked on every switch of 18 runs (experiments/new/kl/step4/switches.out, column lemma_c_viol = 0).
- (d) At most n pivots turn some vertex to ⊤ for the first time; ⊤ is absorbing.
- (e) Expected pivots ≤ n·n^h ≤ n^{n+1} (Theorem 2.3, canonical C1). This is exponential, and the trivial bound.

### 3.1 Attempt A: a rank-gap potential dropping by an expected 1/poly fraction per pivot
- Claim needed: Ψ(µ) = Σ_v (r(µ*(v)) − r(µ(v))) satisfies E[Ψ_{k+1} | past] ≤ (1 − 1/q(n)) Ψ_k. Then E[#pivots] ≤ q(n)·ln(n·n^h) + 1
  = q(n)·O(d log n).
- PROVED part: Ψ ≥ 0, Ψ decreases by ≥ 1 per pivot, and Ψ = 0 exactly at µ* (3.0 (a)).
- **Break (DATA, experiments/new/kl/step4/mlemma.out).** Even the BEST candidate's pivot can remove only a tiny fraction of Ψ. Measured as
  the minimum over the states of an R2 run of (largest Ψ-drop among all candidates)/Ψ, on switchallexp (dual, seed 1):
  2.8·10⁻⁴, 4.4·10⁻⁸, 3.3·10⁻¹², 6.8·10⁻¹⁶ at N = 1, 2, 3, 4 (n = 21, 35, 49, 63). That is a factor ≈ 10⁻⁴ per +14 vertices,
  exponentially small in n. Instances: pgsolver_port.py switchallexp N (sha1 in the .out file; N = 2 is ca6e0b7d4745…).
- Why (READING): Ψ is dominated by the ⊤-gaps (rank n^h) of Odd-won vertices. A pivot that does not yet close an odd cycle raises labels
  only in low components. The runs are short anyway (34 to 100 pivots), so Ψ is just the wrong measure. Any rank-weighted potential
  inherits this: an exponential range with additive steps.

### 3.2 Attempt B: a lock-in potential with polynomial range (the strongest candidate I found)
- Definition: M(µ) = #{(v, j) : 0 ≤ j ≤ h, prefix_j(µ(v)) = prefix_j(µ*(v))}, where prefix_0 records only "⊤ or not". M is
  non-decreasing (3.0 (b)) and lies in [0, n(h+1)], with M = n(h+1) exactly at µ*.
- Claim needed (Lemma M): at every reachable non-final state, at least one candidate's pivot strictly raises M. Since R2 picks each
  candidate with probability ≥ 1/n given the past, Lemma M would give **E[#pivots] ≤ n·n(h+1) = O(n²d)**: an M4-R result.
- **Break 1 (DATA): Lemma M is FALSE.** switchallexp N = 2 (sha1 ca6e0b7d4745…), dual run, seed 1, state 1: none of the 9 candidates
  {5, 11, 13, 15, 17, 19, 20, 26, 29}, each pivoted to its R2 arc and recomputed, raises M. 17 of the 34 states of that run are like this.
  Such states occur on all 10 instances tried that have at least one pivot (famL k = 2 has none in the dual run). See mlemma.out, column
  states_without_M_raise.
- Weakened claim (Lemma M_w): from every reachable state, the expected number of R2 pivots until M rises is ≤ w(n) for a polynomial w.
  It gives E[#pivots] ≤ n(h+1)·w(n).
- **Break 2: Lemma M_w is not easier than the target.** Conversely, the state-wise form of the target (expected remaining R2 pivots ≤ q(n)
  from every reachable state, which is the form any potential proof yields) implies M_w with w = q, because M is maximal at the end. So M_w
  is equivalent to the state-wise target up to the factor n(h+1). The potential buys a localisation, not a proof.
- DATA on M_w: the longest stretch without an M rise on the actual R2 run is 14, 42, 62 pivots on switchbestexp N = 1, 2, 3 (n = 35, 60,
  85), roughly linear in n. On famG (R53's G_k, k = 1) M rises once in 53 pivots (mlemma.out). So any per-state progress event that is
  monotone and of polynomial range must be "rare and late" on such runs. That is the shape an adversary would exploit, and HL_k does
  (§3.7): on HL88_0, M rises 18 times in 1,380 pivots, and the longest stretch without a rise is 1,354.

### 3.3 Attempt C: few switches per vertex (the G_ζ observation; R56 M2)
- Claim needed: every vertex switches at most s(n) times in expectation, s polynomial. Then E[#pivots] ≤ n·s(n).
- PROVED part: 3.0 (c). This is polynomial for Odd vertices whose priority is near the top of [d], and n^{k(v)} in general.
- The mechanism behind the G_ζ observation (R55 §3: 354 of 374 switching vertices switch exactly once; R56 §1b M2): truncation at an even
  dual priority is idempotent, so a lane tail's label equals its exit's truncation and the lane never needs to unwind. That is 3.0 (c)
  seen from the other side: once µ(v)|_{π(v)} has risen, a switch-back requires a successor whose label rose past it.
- **Break (DATA, experiments/new/kl/step4/switches.out, R2 dual, seeds 1-2).** Off G_ζ, vertices switch more and more as n grows:
  - switchallexp N = 2, 4, 6, 8, 10 (n = 35 .. 147): max switches per vertex 6/6, 11/8, 10/7, 15/17, 15/19.
  - switchbestexp N = 2, 4, 6, 8 (n = 60 .. 210): max 10/9, 11/14, 28/15, 27/24; mean over switching vertices 3.0 → 7-9.
  On L-RED's HL88_0 (§3.7) the max is 81 and the mean 73 per switching vertex at n = 41. "About once" is specific to G_ζ.
  What a proof would need instead: a bound on how many DISTINCT values of µ(v)|_{π(v)} a vertex visits. These are base-n numbers with
  k(v) digits, and under switch-all on L_k a vertex visits n^k of them (N8a §6).
- **OPEN**: whether R2's randomness bounds the visited values by a polynomial. This is the crawl question U3 of N8d-barrier.md §3 in
  per-vertex form.

### 3.4 Attempt D: Random-Edge-type and Kelner-Spielman-type analyses
- Kelner-Spielman (opened, §0): the polynomial bound is for the shadow-vertex simplex method on a polytope {x : Ax ≤ b}. The randomness
  is a perturbation of b, and the count is the number of edges of a 2-dimensional shadow (Thm 3.2), turned into O(n³L) iterations
  (Thm 6.3).
  - **Break**: Koh-Loho pivots are not edges of a polytope. There is no LP whose feasible region the run walks: a strategy may recur with a
    larger µ (paper §3), so the run is not even a walk on a fixed graph of strategies. No polynomial-size LP whose simplex paths are parity
    strategy iteration is known (BARRIERS B15 and RANKING row 7, as cited in N8d-barrier.md §1).
  - Also, the shadow bound needs the objective and right-hand side to be perturbable reals. R2's randomness is a node choice; the input
    is not perturbed.
- Random-Edge upper bounds: I know of none for general unique-sink or game-induced structures. Every result recorded in the fleet's
  barrier rows is a LOWER bound: Friedmann Thm 4.76 / 4.78 for VJ valuations; Matoušek-Szabó and Hansen-Zwick on abstract cubes (via
  N8d-barrier.md §4).
  - **Break**: there is no template to port. The cube results cannot even be stated for Koh-Loho runs, which are not cube walks (B14 row).
- Random-Facet-type subexponential arguments (recursion on facets with a random facet) are out of model for the same reason. R2 is not
  facet-recursive.

### 3.5 Where this leaves R2 (READING)
- The only PROVED bounds are 3.0 (c)-(e): exponential in the number of distinct odd priorities below a vertex.
- Lemma M is the cleanest sufficient statement with a polynomial range, and it is false at a state. The windowed version is equivalent to
  the target.
- What separates R2 from the dead rules, in every instance seen, is that a random single switch closes the odd cycle a crawl needs to keep
  open (R54, R55 §2, R56 M1-M2). Turning that into a proof needs a statement of this form (**OPEN**): from every reachable state, with
  probability ≥ 1/poly the next poly(n) R2 pivots raise M or raise some vertex's prefix at its top unmatched level.
  - I have no candidate argument for it. An adversary needs only one gadget that keeps an odd cycle open under every admissible single
    switch (U3), or one in which the cycle-closing candidates are an exponentially small fraction for exponentially long. The second is
    possible in principle, because R2 is node-uniform: delay lanes with many candidate vertices dilute the closers. L-RED has since built
    exactly this: HL_k (R56 §2, §3.7 below), R2 mean ≈ 34·n^{k+1}.
- **Correction by §3.6 (DATA):** the cycle-closing escape does NOT explain R2 on Friedmann's families. There the long dual runs have
  µ* finite everywhere, so no odd cycle is ever closed, yet R2's counts there are far below R1's 2^Θ(n).
- **No growth-rate framing.** The earlier fits (≈ n^2 on switchbestexp, N8d-single.md §5) are DATA on those families only. HL_k gives R2
  mean dual pivots ≈ 34·n^{k+1} (§3.7), so any expected-polynomial argument must fail on HL_k, up to the cap that fixed-length lanes
  impose.
- Step 4's running-time half is therefore **not passed**. N8d-R2 stays a step-2 / step-3 survivor with correctness PROVED (unrefereed),
  under D1.

### 3.6 Attempt E: split at the ⊤-set (Lemma T), and one-player games
- Phases: phase 1 runs until the ⊤-set equals µ*'s; phase 2 is the rest. By 3.0 (d), phase 1 has at most n ⊤-creating pivots.
- Lemma T (claim needed): at every state of phase 1, some candidate's R2 pivot creates a new ⊤. With R2's ≥ 1/n per-candidate
  probability it would give E[phase-1 pivots] ≤ n².
- **Break 1 (DATA, experiments/new/kl/step4/tlemma.out): Lemma T is FALSE.**
  - famG = R53's G_1 (sha1 cb9004b7af4b), dual, seed 1: 51 of 53 states violate it, from state 1 on.
  - famF dual: 8 of 13 states. famH dual: 4 of 5.
  - The one-player game climb_r1_n8.pg (below) violates it at 7 of 10 states.
- **Break 2 (DATA, same file): on Friedmann's families phase 1 is empty and phase 2 is the whole cost.**
  - switchallexp N = 2, 4 and switchbestexp N = 2, 3, dual runs (34-180 pivots): µ* has NO ⊤ vertex (top_in_mustar = 0).
  - The primal runs (2-4 pivots) make everything ⊤.
  - Also at larger sizes (topcount.out, seed 1): µ* has no ⊤ in the dual runs of switchallexp N = 6, 8, 10 and switchbestexp N = 4, 6, 8,
    where R1 takes 615 / 2,361 / 9,291 and 237 / 691 / 2,297 pivots and R2 142 / 283 / 500 and 264 / 830 / 879.
  - So the expensive runs are entirely runs in which Odd (the dual's improver) wins nowhere and no odd cycle ever closes. R1 is 2^Θ(n)
    exactly there (N8d-single.md §3), and R2 stays far below it on those families (DATA).
  - A proof must therefore explain R2 on games where the improver loses everywhere. This is the cleanest OPEN sub-target: **E[R2
    pivots] ≤ poly(n) on games with µ* finite everywhere.** On those games every label stays finite and only Even-type truncation /
    counting happens (R56 M1).
- **One-player games (DATA, experiments/new/kl/step4/oneplayer.py; Even out-degree 1, so only the improver chooses).** I asked whether a
  rule-independent polynomial bound could hold there, as a first PROVED case (cf. RESULTS R17 for N5). Data says no cheap one:
  - Random one-player games, n ≤ 80, 3,000 games (oneplayer_random.out): max primal pivots ≤ 29 (R1) and ≤ 32 (R2).
  - Hill-climbs on the game maximising R1 primal pivots, 480 s each (op/*.out), reach 36, 124 and 209 pivots at n = 8, 12, 16. That is
    superlinear, and up to 13 per vertex.
    - n = 8 is an all-Odd game: op/climb_r1_n8.pg, sha1 a32b4cdfb2b5.
    - n = 12: sha1 271dbd3a459b. n = 16: sha1 d9e0ef883716.
    - Each verified by verify.py. Oink is not built in this container, so there is no zlk cross-check.
  - On the same three games R2 takes 8.4, 13.1 and 8.1 primal pivots on average over seeds 1-30, max 16 / 23 / 16 (op/r2_on_climbs.out).
  - A climb maximising R2 (seed 1) at n = 12 reached 33.
  - Reading: even with one player, single-switch Koh-Loho SI is not polynomial for every admissible rule, as far as climbs show. A
    one-player theorem would have to use R2's randomness too.

### 3.7 L-RED's HL_k (R56 §2, merged on trunk): which candidates it breaks
- Family: R53's H_k plus two z-separated delay lanes of length 8; n = 41 + 2k (experiments/red/kl24/hlgen.sh k 8 8).
- R2 mean dual pivots, seeds 1-5, verified (R56 §2c): 1,388 / 63,686 / 2,759,578 for k = 0, 1, 2, i.e. ≈ 34·n^{k+1}. k is the number
  of extra high priorities.
- Reading (L-RED / Lead): not a kill yet. With fixed lanes a per-lap failure probability ε caps the expectation, and L-RED is measuring
  ε(L) and building growing lanes.
- My probes on HL88_0 (sha1 8f710aef7abd), dual, seed 1, 1,380 pivots (experiments/new/kl/step4/hl88.out; switches on HL88_1 in
  hl88_1.out):

| candidate | HL88_0 result | broken by HL_k? |
| --- | --- | --- |
| A rank-gap fraction (§3.1) | min best-gain/Ψ = 6.0·10⁻⁴; µ* is ⊤ everywhere, so Ψ is dominated by ⊤-gaps | already broken (§3.1); HL_k adds nothing |
| B Lemma M (§3.2) | 1,354 of 1,380 states have no M-raising candidate | yes, at almost every state |
| B Lemma M_w | M rises 18 times; longest stretch without a rise = 1,354 pivots (all but the 26 rising or initial states) | yes: w would have to be ≈ the whole run, i.e. ≈ 34·n^{k+1} |
| C switches per vertex (§3.3) | max 81, mean 72.6 per switching dual-Odd vertex (n = 41); 3.0 (c) holds at every switch | yes for any s(n) bound independent of k (data for k = 1 in hl88_1.out) |
| E Lemma T (§3.6) | µ* = ⊤ on all 41 vertices, so the whole run is phase 1; 1,354 states violate Lemma T | yes; HL_k is the opposite case to Friedmann's families (all-⊤ vs all-finite µ*), and both are slow for some rule |
| D KS / Random-Edge (§3.4) | no template to begin with | n/a |

- Consequence (READING): every potential I tried fails on HL_0 already, at a fixed n = 41. The per-k growth then shows that none of them
  can be repaired by a polynomial window.
- What any surviving argument must use: the cap that ε(L) puts on laps, i.e. that a lane of FIXED length is escaped with constant
  probability per lap. A bound of that kind would be in terms of the longest lane the game can host. Growing lanes (L-RED's next step)
  would test exactly that. **OPEN**.

## 4. Files
- experiments/new/kl/step4/mlemma.py → mlemma.out: Lemma M per state; Ψ fractions; longest stretches without an M rise. Each run is
  asserted to have the same pivot count as kl_single.strategy_iteration.
- experiments/new/kl/step4/switches.py → switches.out: per-vertex switch counts; 3.0 (c) checked on every switch.
- topcount.out: ⊤-count of µ* on the larger Friedmann dual runs (R1 and R2).
- hl88.out, hl88_1.out: probes on L-RED's HL88_0 / HL88_1 (experiments/red/kl24/instances/, read-only).
- experiments/new/kl/step4/tlemma.py → tlemma.out (Lemma T, phases); oneplayer.py → oneplayer_random.out, op/ (climbs and R2 on them).
- experiments/new/kl/step4/c1diff.py, carry.py → c1diff.out, carry.out: §0b's C1 comparison (kl_single.py vs kl2.py).
- Instances: generated by experiments/hard-families/pgsolver_port.py, experiments/red/kl/famgen.py and experiments/new/kl/gen_lk.py
  (sha1 printed in each .out file).
