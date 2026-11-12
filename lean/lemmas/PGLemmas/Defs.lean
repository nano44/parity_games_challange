/-
Definitions for the lane lemmas (L-FORMAL).  Nothing in this file is a theorem about games:
it fixes the objects that the statements in `PGLemmas/Statements.lean` talk about.

Sources (opened; section numbers in notes/L-FORMAL.md):
* [Fr]   O. Friedmann, "An exponential lower bound for the latest deterministic strategy iteration
         algorithms", arXiv 1106.0778, §2 (parity games, injective priorities) and §3 (rewards, node
         valuations, the order on node valuations, improvement).
* [VJ00] J. Vöge, M. Jurdziński, "A discrete strategy improvement algorithm for solving parity
         games", BRICS RS-00-48, §2.2 (cycle-domination games), §4.1 (play values), §4.2 (the order).
The definitions below follow [Fr] §3 line by line; each docstring quotes the line it encodes.
-/
import Mathlib.Data.Finset.SymmDiff
import Mathlib.Data.Finset.Max
import Mathlib.Data.Fintype.Pigeonhole
import Mathlib.Logic.Function.Iterate
import Mathlib.Algebra.Group.Even
import Mathlib.Algebra.Group.Int.Even
import Mathlib.Data.Nat.Find

namespace PG

open Classical
open scoped symmDiff

noncomputable section

variable {V : Type*} [Fintype V]

/-! ## Node valuations and their order ([Fr] §3; [VJ00] §4.1-§4.2) -/

/-- A node valuation `(w₁, M, k)`.  [Fr] §3: «we refer to w₁ as the cycle component, to
{vᵢ > w₁ | 1 ≤ i ≤ k} as the path component, and to k as the length component».
([VJ00] §4.1: the play value `(λ(P), (π(P), #(P)))`.) -/
@[ext] structure Val (V : Type*) where
  /-- the cycle component (the fleet's `Λ`) -/
  top : V
  /-- the path component (the fleet's `Π`) -/
  set : Finset V
  /-- the length component (the fleet's `k` / `len`) -/
  len : ℕ

/-- [Fr] §3: «the reward of node v is defined as follows: rew(v) := Ω(v) if Ω(v) ≡₂ 0 and
rew(v) := −Ω(v) otherwise».  ([VJ00] §4.2: `Reward(v)`.)  `pr` is the priority function `Ω`. -/
def rew (pr : V → ℕ) (v : V) : ℤ := if Even (pr v) then (pr v : ℤ) else -(pr v : ℤ)

/-- The order on path components.  [Fr] §3:
«M ≺ N :⟺ M △ N ≠ ∅ and max_<(M △ N) ∈ ((N ∩ V⊕) ∪ (M ∩ V⊖))», where `<` is the relevance
ordering `v < u :⟺ Ω(v) < Ω(u)`, `V⊕` the nodes of even and `V⊖` the nodes of odd priority.
Here `d` is that maximum.  ([VJ00] §4.2: `B ≺ C` via `MaxDiff(B, C)`.) -/
def setLt (pr : V → ℕ) (M N : Finset V) : Prop :=
  ∃ d ∈ M ∆ N, (∀ x ∈ M ∆ N, pr x ≤ pr d) ∧ ((d ∈ N ∧ Even (pr d)) ∨ (d ∈ M ∧ ¬ Even (pr d)))

/-- The strict order `≺` on node valuations (the fleet's `◁`).  [Fr] §3:
«(u, M, e) ≺ (v, N, f) :⟺ (u ≺ v) or (u = v and M ≺ N) or (u = v and M = N and e < f and u ∈ V⊖)
or (u = v and M = N and e > f and u ∈ V⊕)», with the reward ordering `u ≺ v :⟺ rew(u) < rew(v)`. -/
def Val.lt (pr : V → ℕ) (x y : Val V) : Prop :=
  rew pr x.top < rew pr y.top ∨
  (x.top = y.top ∧ setLt pr x.set y.set) ∨
  (x.top = y.top ∧ x.set = y.set ∧ x.len < y.len ∧ ¬ Even (pr x.top)) ∨
  (x.top = y.top ∧ x.set = y.set ∧ y.len < x.len ∧ Even (pr x.top))

/-- The non-strict order (the fleet's `⊴`): `≺` or equal. -/
def Val.le (pr : V → ℕ) (x y : Val V) : Prop := Val.lt pr x y ∨ x = y

/-! ## The valuation of a positional play ([Fr] §3; [VJ00] §2.2, §4.1)

A map `s : V → V` gives every vertex its one chosen successor (a positional strategy pair
`(σ, τ)` read as one map, or the strategy of a one-player game).  The play from `v` is
`v, s v, s (s v), …`.  [Fr] §3: «this path can be uniquely written as π = v₁ … v_k (w₁ … w_l)^ω
with v₁ = v, vᵢ ≠ w₁ for all 1 ≤ i ≤ k and Ω(w₁) > Ω(w_j) for all 1 < j ≤ l», and
«ϑ := (w₁, {vᵢ > w₁ | 1 ≤ i ≤ k}, k)». -/

/-- `u` is on the cycle `w₁ … w_l` of the play from `v`: the play reaches `u`, and `u` recurs. -/
def OnCycle (s : V → V) (v u : V) : Prop :=
  (∃ n, s^[n] v = u) ∧ ∃ p, 0 < p ∧ s^[p] u = u

/-- The play from `v` has a cycle, and the cycle has a vertex of largest priority. -/
theorem exists_cycleNode (pr : V → ℕ) (s : V → V) (v : V) :
    ∃ w, OnCycle s v w ∧ ∀ u, OnCycle s v u → pr u ≤ pr w := by
  have hne : (Finset.univ.filter (fun u => OnCycle s v u)).Nonempty := by
    obtain ⟨i, j, hij, h⟩ := Finite.exists_ne_map_eq_of_infinite (fun n : ℕ => s^[n] v)
    have key : ∀ i j : ℕ, i < j → s^[i] v = s^[j] v → OnCycle s v (s^[i] v) := by
      intro i j hlt h
      refine ⟨⟨i, rfl⟩, j - i, Nat.sub_pos_of_lt hlt, ?_⟩
      rw [← Function.iterate_add_apply, Nat.sub_add_cancel hlt.le]
      exact h.symm
    rcases Nat.lt_or_gt_of_ne hij with hlt | hgt
    · exact ⟨s^[i] v, Finset.mem_filter.mpr ⟨Finset.mem_univ _, key i j hlt h⟩⟩
    · exact ⟨s^[j] v, Finset.mem_filter.mpr ⟨Finset.mem_univ _, key j i hgt h.symm⟩⟩
  obtain ⟨w, hw, hmax⟩ := Finset.exists_max_image _ pr hne
  exact ⟨w, (Finset.mem_filter.mp hw).2,
    fun u hu => hmax u (Finset.mem_filter.mpr ⟨Finset.mem_univ _, hu⟩)⟩

/-- The cycle component `w₁` of the play from `v` under `s` (the fleet's `Λ(v)`): a vertex of the
play's cycle of largest priority.  It is unique when `pr` is injective. -/
def lam (pr : V → ℕ) (s : V → V) (v : V) : V := Classical.choose (exists_cycleNode pr s v)

theorem lam_spec (pr : V → ℕ) (s : V → V) (v : V) :
    OnCycle s v (lam pr s v) ∧ ∀ u, OnCycle s v u → pr u ≤ pr (lam pr s v) :=
  Classical.choose_spec (exists_cycleNode pr s v)

/-- The play from `v` visits its cycle node. -/
theorem exists_hit (pr : V → ℕ) (s : V → V) (v : V) : ∃ n, s^[n] v = lam pr s v :=
  (lam_spec pr s v).1.1

/-- The length component `k`: the number of nodes `v₁ … v_k` of the play before its first visit
of `w₁` («vᵢ ≠ w₁ for all 1 ≤ i ≤ k»).  ([VJ00] §4.1: `#(P) = |Prefix(P)|`.) -/
def plen (pr : V → ℕ) (s : V → V) (v : V) : ℕ := Nat.find (exists_hit pr s v)

/-- The path component `{vᵢ > w₁ | 1 ≤ i ≤ k}`: the nodes `vᵢ = s^[i-1] v` before the first visit
of `w₁` that are more relevant than `w₁`.  ([VJ00] §4.1: `π(P) = Prefix(P) ∩ V_{>λ(P)}`.) -/
def pset (pr : V → ℕ) (s : V → V) (v : V) : Finset V :=
  Finset.univ.filter (fun u => pr (lam pr s v) < pr u ∧ ∃ j, j < plen pr s v ∧ s^[j] v = u)

/-- The node valuation `ϑ` of `v` under `s` (the fleet's `Ω(v) = (Λ, Π, k)`). -/
def val (pr : V → ℕ) (s : V → V) (v : V) : Val V :=
  ⟨lam pr s v, pset pr s v, plen pr s v⟩

/-! ## Howard's switch-all step -/

/-- A Howard step at the vertex `v`, from `σ` to `σ'`, with successor set `E v` and values taken
under `σ`.  RESULTS R118 (a): «every mover x goes to a successor of ⊴-largest Ω_t value, and keeps
σ_t(x) if σ_t(x) is such a successor».  (Box 101 §2: «every v ∈ Ch with a successor of strictly
larger value moves to a ⊴-best successor; otherwise it keeps its current one (any tie
resolution)».)  Ties among best successors are not resolved here: any choice is a Howard step. -/
def HowardAt (pr : V → ℕ) (E : V → Finset V) (σ σ' : V → V) (v : V) : Prop :=
  σ' v ∈ E v ∧
  (∀ w ∈ E v, Val.le pr (val pr σ w) (val pr σ (σ' v))) ∧
  ((σ v ∈ E v ∧ ∀ w ∈ E v, Val.le pr (val pr σ w) (val pr σ (σ v))) → σ' v = σ v)

/-- A window `a..b` of a Howard run on which every cycle node is constant.
* `Ch`: the vertices that may switch; `E v`: the successors of a vertex `v ∈ Ch`.
* `s t : V → V`: the state at time `t`, one successor per vertex.
The fields are the hypotheses of Lemma LAM-GAP (box 101 §2) and of Lemma SHARP (R234 §3). -/
structure Window (pr : V → ℕ) (E : V → Finset V) (Ch : Finset V) (s : ℕ → V → V) (a b : ℕ) :
    Prop where
  /-- the window is `a, a+1, …, b` -/
  le : a ≤ b
  /-- a vertex outside `Ch` never changes its successor (one successor only, or frozen) -/
  fixed : ∀ t, a ≤ t → t ≤ b → ∀ v, v ∉ Ch → s t v = s a v
  /-- every step of the window is a Howard step at every vertex of `Ch` -/
  howard : ∀ t, a ≤ t → t < b → ∀ v ∈ Ch, HowardAt pr E (s t) (s (t + 1)) v
  /-- premise (M): no value falls in a step (RESULTS R15 (a), pointwise) -/
  mono : ∀ t, a ≤ t → t < b → ∀ v, Val.le pr (val pr (s t) v) (val pr (s (t + 1)) v)
  /-- every vertex keeps its cycle node on the window -/
  lamConst : ∀ t, a ≤ t → t ≤ b → ∀ v, lam pr (s t) v = lam pr (s a) v
  /-- the run has not stopped before `b`: every step of the window changes the state -/
  moves : ∀ t, a ≤ t → t < b → s (t + 1) ≠ s t

/-- A positional pair read as one successor map: `σ` on the vertices of `V0` (Even's), `τ` on
the others (Odd's).  [Fr] §3: «there is exactly one path π_{σ,τ,v} that conforms to σ and τ». -/
def pair (V0 : Finset V) (σ τ : V → V) : V → V := fun v => if v ∈ V0 then σ v else τ v

end

end PG
