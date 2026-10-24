# Referee packet P-N5-1OA: N5 on o-acyclic one-Odd-choice games makes polynomially many iterations (box 24)
L-NEW successor 8 (Opus 5.5, D15). Lead GO for box 24 at 2026-10-24 03:05Z. The argument was found and checked 03:00-03:08Z,
reported to the Lead at 03:09Z (before any write-up), and this packet was written at 03:16Z (date -u).
Status:
- READING with a full proof. Unrefereed. NOT landed (D1).
- It is a bound on the candidate N5 on a SUBCLASS that is polynomial by other means (d one-player games), in the sense of
  RESULTS R17. It is not a TARGET.md claim and not a gauntlet step-4 pass. G-N5-TIME stays OPEN.
- It depends on Proposition X (L-RED, unrefereed) and on premise (P). Both are listed in §4 with exact locations.

## 1. Definitions
- N5: docs/new/N5-ssi-global.md, SPEC S1-S5. The code is experiments/new/n5.py; L-COMP's independent n5b.py agrees in SPEC mode.
  - σ is Even's strategy; τ is Odd's.
  - Ξσ is Even's honest valuation: the S1 valuation against Odd's optimal counterstrategy σ̄.
  - Iσ is Even's set of improving edges (S2). Iτ is Odd's, on the dual game G^d.
  - An iteration is one pass of S4 with Iσ ∪ Iτ ≠ ∅.
- V_{σ,τ}(v) is the S1 valuation (c, P, ℓ) of the play from v under the pair (σ, τ).
- 𝒞^1O: the games in which exactly one Odd vertex, called o, has out-degree d > 1. Every other Odd vertex has out-degree 1.
- o-acyclic: o lies on no cycle of the game graph. Then no successor of o can reach o.
- X := {v : there is no path from v to o in the game graph}. Y := V \ X. So o ∈ Y, and in an o-acyclic game every successor of
  o lies in X.
  - X is closed under successors.
  - Every Odd vertex in X has out-degree 1, so G[X] (the game restricted to X) is a one-player game for Even.
  - n_X := |X|, and m_X := the number of edges inside X.
- θ := Ξσ(o), Odd's honest value at o. W := V_{σ,τ}, the play values against the current τ. w := W(o).
- G_τ: G with every Odd vertex v restricted to its edge τ(v). This is a one-player game for Even.
- A transition k → k+1 of an N5 run is PURE if σ_{k+1}|X = σ_k|X and τ_{k+1} = τ_k.
- A block is a maximal run of consecutive pure transitions.
- C_X := (n_X² − n_X + 1)(n_X + m_X).
- B := (n² − n + 1)(n + m), the bound of RESULTS R17 Corollary 2 for G.

## 2. Theorem
Let G be an o-acyclic game in 𝒞^1O, with n vertices and m edges, where o has out-degree d. Assume (P) (§4). Then every N5 run on
G, from any start pair (σ_0, τ_0), has fewer than (C_X + d)·(B + 1) iterations.

## 3. Proof
### Step 1: non-pure transitions are few
- Prop X (§4, item 1): along any N5 run on G, the sequence of distinct values of σ|X is an N5 run on the one-player game G[X].
  By R17 Corollary 2 it has fewer than C_X steps, so σ|X changes in fewer than C_X transitions.
- τ is determined by τ(o), which has d possible values.
  - By RESULTS R15 (c), every change of τ is a nonempty switch of Odd improvements on G^d, or Odd's S4c fallback, and goes
    strictly up in the strict partial order ≺ of G^d. So no τ value repeats.
  - Hence τ changes at most d − 1 times.
- Non-pure transitions therefore number at most (C_X − 1) + (d − 1) < C_X + d − 1.

### Step 2 (Lemma 1): at a pure transition from state k, σ_k|X has G[X]'s optimal valuation
Write ρ := σ_k|X and Ω := the valuation of ρ in G[X]. By Prop X step 1, the valuations of X-vertices in G equal Ω, and the X-part
of N5's S4a step on G is G[X]'s S4a step at ρ. Since the transition is pure, σ|X did not change. So G[X]'s S4a arena optimum
returned ρ, or there was no S4a step on X because Iσ|X = ∅. (Any global S4c fallback would have switched X's improving edges and
changed σ|X.)
- Case (a): I(ρ) = ∅ in G[X]. By (P) applied to G[X], ρ is optimal. □
- Case (b): I(ρ) ≠ ∅, and the optimum ρ' of the arena H in which x may use {ρ(x)} ∪ I(x) satisfies ρ' = ρ.
  - (F1) (RESULTS R17 claim (a); VJ00 (11) on the dual): the arena optimum dominates every arena strategy pointwise.
  - So for every (x, z) ∈ I(ρ), with ρ̂ := ρ[x → z] (an arena strategy): Ω(x) = val_ρ'(x) ⪰ val_ρ̂(x).   (★)
  - Let c := λ(z) be z's cycle node, and π := the ρ-path from z to c. (x, z) ∈ I means Ω(z) ≻ Ω(ρ(x)).
  We go through the cases of R17's Lemma P, Case B (docs/new/N5-phase-bound-box10.md §2), without its induction hypothesis.
  - B1, x ∉ π and x not on c's cycle. The ρ̂-play from x is x, π, then c's cycle, so val_ρ̂(x) = x ⊕ Ω(z).
    - If x is not its own cycle node, then Ω(x) = x ⊕ Ω(ρ(x)) by (V1). Strict (V2) gives x ⊕ Ω(z) ≻ x ⊕ Ω(ρ(x)), contradicting (★).
    - If x is its own cycle node, then Ω(x) = (x, ∅, 0), and Ω(ρ(x)) has cycle node x. Ω(z) ≻ Ω(ρ(x)) with cycle node c ≠ x
      forces c to be a better cycle node than x. So val_ρ̂(x) ≻ Ω(x), contradicting (★).
  - B1, x ∉ π and x on c's cycle. Then λ(x) = c, and P(Ω(ρ(x))) = ∅ (cycle vertices are less relevant than c). Improvement means
    one of two things.
    - P(π) ≠ ∅ with an even most relevant vertex. Then the new cycle x, π, (arc back to x) has a better top than c, so
      val_ρ̂(x) ≻ Ω(x). This contradicts (★).
    - P(π) = ∅, c odd and |π| longer. Then val_ρ̂(x) = (c, ∅, |π| + 1) ≻ Ω(x). This contradicts (★).
  - B2, x ∈ π. Then λ(x) = c. Let D := P(π[z..x)) ∪ ({x} if x is more relevant than c), the symmetric difference of the path
    sets of Ω(z) and Ω(ρ(x)). The ρ̂-play from x is the cycle Z = x, z, π[z..x).
    - D ≠ ∅ (its top even, by improvement): top(Z) is better than c, so val_ρ̂(x) ≻ Ω(x). This contradicts (★).
    - D = ∅ and top(Z) ≠ c: top(Z) is less relevant than the odd c and better for Even, so val_ρ̂(x) ≻ Ω(x). This contradicts (★).
    - D = ∅ and top(Z) = c: then c = x, and val_ρ̂(x) = (x, ∅, 0) = Ω(x). This is the only case left: the edge is FLAT, and x is
      its own cycle node.
  So every improving edge of ρ is flat: x = λ(x), and z lies in x's region (z's ρ-path ends at x).
- Flat switches change no valuation, and there are finitely many.
  - Let F ⊆ I(ρ) be a set containing at most one edge per vertex, and let ρ₁ := ρ switched on F.
    - Each switched x is its own cycle node, and its new cycle consists of x and vertices of cycle node x. So different switched
      vertices do not interact.
    - Every vertex whose play met x still meets x, along the same path, and x's new cycle has top x (D = ∅). So Ω_{ρ₁} = Ω.
      This is R17 Theorem PH's proof, last paragraph.
  - The improving sets of ρ₁:
    - For y not switched, I_{ρ₁}(y) = I_ρ(y). The valuations are unchanged.
    - For a switched x with new successor z, I_{ρ₁}(x) = {u ∈ I_ρ(x) : Ω(u) ≻ Ω(z)}. This is a strict subset of I_ρ(x), since
      z ∉ I_{ρ₁}(x).
    - Every edge of I_{ρ₁} is still flat. The paths of its heads lie in regions of cycle node y = λ(y) and avoid the switched
      vertices, so B2 with D = ∅ and top = y still applies.
  - Repeating at most Σ_x |I_ρ(x)| ≤ m_X times gives a strategy ρ* of G[X] with Ω_{ρ*} = Ω and I(ρ*) = ∅.
  - By (P), ρ* is optimal in G[X]. So Ω is G[X]'s optimal valuation. □
- Remark: ρ itself need not be maximal in R15's order ≺. The R15 side-finding instance, prio [0, 2, 4], has a non-maximal ρ
  whose valuation is optimal. Only the valuation is claimed optimal.

### Step 3 (Lemma 2): at a pure transition from state k, θ_k = w_k
- Let e be any successor (exit) of o. Then e ∈ X (o-acyclic).
- Odd's honest valuation at e, read in G's order, is U_τ(e) = max over σ' of V_{σ',τ}(e). This is Lemma S (a) together with
  Lemma R (§4, item 3).
- Plays from e stay in X, where Odd has no choice. So U_τ(e) is G[X]'s optimal value at e, which by Lemma 1 equals Ξ_k(e).
- Let a := σ̄(o) and b := τ_k(o).
  - σ̄ is pointwise optimal (VJ00 (11)). So θ = o ⊕ Ξ(a) ⊴ o ⊕ Ξ(e) for every exit e, and w = W(o) = o ⊕ Ξ(b). Here
    W(b) = Ξ(b) because b ∈ X.
  - The prefix by o is strictly monotone, because the plays from the exits avoid o.
- Suppose θ ◁ w.
  - Then Ξ(a) ◁ Ξ(b), so U_τ(a) ◁ U_τ(b): a is strictly better for Odd than b in Odd's honest order. So (o, a) ∈ Iτ (S2 on G^d).
  - Then S4b runs. It computes Odd's optimal counterstrategy τ' in the arena where o may use {b} ∪ Iτ(o) and Even is fixed to σ_k.
  - Pointwise optimality (F1 on the dual) gives the value at o under τ' ⊴ o ⊕ Ξ(a) ◁ o ⊕ Ξ(b). Hence τ'(o) ≠ b, and S4b changes τ.
  - If the iteration's S4a also changes σ, τ still changes, since both are applied (A6).
  - So τ_{k+1} ≠ τ_k, and the transition is not pure. This is a contradiction.
- Hence θ = w. □

### Step 4 (Lemma 3): at a pure transition from state k, Ξ_k(v) = W_k(v) for every v
- If the σ_k-path from v (following forced Odd edges) avoids o, the plays under (σ, σ̄) and (σ, τ) coincide.
- Otherwise both plays are π_v, the path from v to o with o excluded, followed by o's continuation. The continuation goes via a
  under σ̄ and via b under τ; in both cases it then stays in X.
  - π_v ⊆ Y, since every vertex on it reaches o. The continuations lie in {o} ∪ X. So they are disjoint from π_v.
  - The two continuations have equal valuations at o (Lemma 2), so the same cycle node, the same path set and the same length.
  - S1's valuation of the whole play is (c, P(π_v) ∪ P(continuation), |π_v| + ℓ), with P restricted to vertices more relevant
    than c. This is equal for both plays. □

### Step 5: a block is a segment of N5's run on the one-player game G_τ
Let k → k+1 be pure, and τ := τ_k.
- By Lemma 3, Iσ_k (computed on G) equals the improving set of σ_k in G_τ, since S2 compares the same valuations.
- S4a on G is the arena optimum against τ over {σ(x)} ∪ Iσ(x). That is literally N5's S4a step on G_τ.
- S4b on G returned τ unchanged, since the transition is pure. On G_τ, Odd has no choice, so Iτ = ∅ and S4b is void.
- S4c fires on G iff S4a returns σ_k and S4b returns τ_k, i.e. iff S4a returns σ_k (S4b did). On G_τ it fires iff S4a returns σ_k.
  The rule is the same: Even's switch-all on Iσ by (key, index), with the same keys (Lemma 3).
- Iσ_k ≠ ∅. Otherwise S4c would have fallen back on Odd, or S4b would have moved τ.
So the states of a block form a segment of N5's run on G_τ.
- RESULTS R17 Corollary 2 bounds N5 runs on one-player games by fewer than B iterations.
- Its proof (Lemma P, Theorem PH, phase count n(n−1) + 1) starts from an arbitrary strategy ρ_0, so the bound holds for every
  segment. Every block has fewer than B transitions. □

### Step 6: counting
The run consists of blocks separated by non-pure transitions.
- There are fewer than C_X + d − 1 separators (Step 1), so at most C_X + d − 1 blocks.
- Total: < (C_X + d − 1) + (C_X + d − 1)·B < (C_X + d)(B + 1). □

## 4. Dependencies, with exact locations
1. Proposition X (L-RED successor 13, unrefereed): docs/red/R58-n5-width.md §9.
   - Used for Step 1, and for Step 2's identification of X-valuations and of X's S4a step.
   - I checked its proof sketch (locality of S1's procedure; S4c on X equals G[X]'s fallback). No gap found. The BFS-discovery-
     order point in its step 1 is taken from L-RED's text.
2. (P): Vöge-Jurdziński, BRICS RS-00-48 (Dec 2000; pdf sha256 485a12de…, as cited in RESULTS R15), Lemma 5.8, direction
   "1 ⇒ 2": no improvement implies σ is maximal (optimal).
   - Per RESULTS R15 (G-N5T-3) this rests on VJ00's unproved Lemma 5.9 and Prop. 5.10, and both referees left it outside their
     packet.
   - Used only for the one-player game G[X], in Step 2 cases (a) and (b).
   - R58's Theorem W uses the same premise.
3. Lemma R and Lemma S (a): docs/new/N5-time-box21.md §2.1 and §2.2 (L-NEW successor 8, unrefereed).
   - Lemma R: G^d's order is the reverse of G's on plays.
   - Lemma S (a): Odd's honest valuation, read in G's order, is the pointwise maximum over Even strategies of V_{·,τ} (VJ00 (11) on
     G^d).
   - Used in Step 3. DATA: sandwich_check.py, 1,610 brute-force checks, 0 mismatches.
4. RESULTS R17 (docs/RESULTS.md, entry "### R17", line 730):
   - claim (a), i.e. (F1)/(F2);
   - claim (b), Lemma P;
   - claim (c), Theorem PH, and its proof's flat-step paragraph;
   - claim (e), Corollary 2: N5 on one-player games < (n² − n + 1)(n + m).
   - The proof text is docs/new/N5-phase-bound-box10.md §2-§3, frozen. Used in Steps 1, 2 and 5.
5. RESULTS R15 (docs/RESULTS.md, entry "### R15", line 624), claims (c)-(d): no strategy of either player repeats. Used in Step 1.
6. VJ00 (11) (pointwise optimality of σ̄), as signed in R15 and R17. Used in Steps 2 and 3.

## 5. Checks (DATA; experiments/new/box22/statcheck.py)
It tests:
- L1 (Lemma 2): θ = w at every state with a pure outgoing transition;
- L2 (Lemma 3): Ξ = W at every vertex there;
- L3 (Step 5): every block equals N5's run on G_τ from its first σ.
Runs:
- `python3 statcheck.py --random 8000 5 18 11`: canonical starts; 1,352 o-acyclic games (forced Odd vertices included), 81 pure
  states, 74 blocks; 0 failures.
- `python3 statcheck.py --random 8000 5 18 12 --randstart`: random start pairs; 1,417 games, 103 pure states, 95 blocks;
  0 failures.
- `python3 statcheck.py instances/statY_12.pg`: one block of 7; 0 failures. The climbY n 20 / 28 bests (scratch, not
  committed) gave 0 failures with 0 pure states.
- Negative control (must FAIL): `python3 statcheck.py ../box21/instances/fts_best16.pg`. o is on a cycle, X = ∅; L1 and L2
  fail at 24 of 28 states, and L3 fails.
- Random games give short blocks (max 3), so the checks test the lemmas, not the tightness of the bound.

## 6. Scope and what is not claimed
- o-CYCLIC 𝒞^1O is not covered. There o's exits can route back through o, Lemma 1 has no analogue (X may be empty), and θ ◁ w
  can survive pure steps (fts_best16).
- Box 22's per-path invariants I1-I4 fail on o-acyclic games too (i4_hand). The proof avoids them. On o-acyclic games every
  throttled stretch contains a non-pure transition, and i4_hand's lane lies in X.
- The bound is O(n^6 m^2)-type and certainly not tight. The data stays linear.
