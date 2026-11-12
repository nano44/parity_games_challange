/-
Box 208 §10, Statement ABS (claude/l-new 8db300fe docs/new/N5-LEVEL-box208.md): the LEVEL potential
argument without parity games, for shortest-path games.  DEFINITIONS AND STATEMENT ONLY: NOT PROVED.
(The statement is a `def … : Prop`; no theorem of this type exists in the tree yet.)

Lane text (§10): «a SHORTEST-PATH GAME: a finite graph, every vertex owned by Max or Min, a target,
an integer weight ≥ 0 on every edge, and no cycle of total weight 0.  For a positional Max strategy
s, d_s(v) := the least weight of a path from v to the target in the graph where every Max vertex
keeps only its edge s(v) (∞ if there is none).  HOWARD: every Max vertex moves to an edge (z, y) of
largest w(z, y) + d_s(y), keeping its edge if that is one of them.»  «Statement ABS.  From every
positional start, Howard makes at most (number of edges of Max vertices)·(number of vertices)
steps, and every step before the last one raises d at a vertex of the lowest lagging value.»
-/
import Mathlib.Data.ENat.Basic
import Mathlib.Logic.Relation
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Fintype.Card
import Mathlib.Data.Nat.Find

namespace PG

open Classical

noncomputable section

/-- A shortest-path game: successor sets `E`, a weight `w v u ≥ 0` on every edge `v → u`, Max's
vertices `Max` (the others are Min's), and a target. -/
structure SPGame (V : Type*) where
  E : V → Finset V
  w : V → V → ℕ
  Max : Finset V
  tgt : V

variable {V : Type*}

/-- An edge of «the graph where every Max vertex keeps only its edge s(v)». -/
def SPGame.edge (G : SPGame V) (s : V → V) (v u : V) : Prop :=
  u ∈ G.E v ∧ (v ∈ G.Max → u = s v)

/-- `G.PathW s v k`: that graph has a path from `v` to the target of total weight `k`. -/
inductive SPGame.PathW (G : SPGame V) (s : V → V) : V → ℕ → Prop
  | nil : SPGame.PathW G s G.tgt 0
  | cons {v u : V} {k : ℕ} : G.edge s v u → SPGame.PathW G s u k → SPGame.PathW G s v (G.w v u + k)

/-- `d_s(v)`: the least weight of a path from `v` to the target, `∞` if there is none. -/
def SPGame.d (G : SPGame V) (s : V → V) (v : V) : ℕ∞ :=
  if h : ∃ k, G.PathW s v k then ((Nat.find h : ℕ) : ℕ∞) else ⊤

/-- Howard's step at a Max vertex `z`: «moves to an edge (z, y) of largest w(z, y) + d_s(y),
keeping its edge if that is one of them». -/
def SPGame.HowardAt (G : SPGame V) (s s' : V → V) (z : V) : Prop :=
  s' z ∈ G.E z ∧
  (∀ y ∈ G.E z, (G.w z y : ℕ∞) + G.d s y ≤ (G.w z (s' z) : ℕ∞) + G.d s (s' z)) ∧
  ((s z ∈ G.E z ∧ ∀ y ∈ G.E z, (G.w z y : ℕ∞) + G.d s y ≤ (G.w z (s z) : ℕ∞) + G.d s (s z)) →
    s' z = s z)

/-- «no cycle of total weight 0»: no closed walk along edges of weight 0. -/
def SPGame.NoZeroCycle (G : SPGame V) : Prop :=
  ∀ v, ¬ Relation.TransGen (fun a b => b ∈ G.E a ∧ G.w a b = 0) v v

/-- **Statement ABS** (box 208 §10; CANDIDATE in the lane; NOT PROVED in Lean).  A Howard run
`s 0, …, s T` of a shortest-path game without weight-0 cycle, whose target is not a Max vertex:
every state a positional Max strategy, Howard steps at every Max vertex, every step changing the
state.  Then (1) `T ≤ (number of edges of Max vertices)·(number of vertices)`, and (2) at every
step some vertex `v` that lags behind the last state (`d_t(v) ≠ d_T(v)`), of the lowest lagging
value, has its value raised by the step. -/
def AbsStatement (V : Type*) [Fintype V] : Prop :=
  ∀ (G : SPGame V), G.NoZeroCycle → G.tgt ∉ G.Max →
  ∀ (s : ℕ → V → V) (T : ℕ),
    -- every state is a positional Max strategy
    (∀ t, t ≤ T → ∀ z ∈ G.Max, s t z ∈ G.E z) →
    -- a state carries a choice only at Max's vertices
    (∀ t, t ≤ T → ∀ v, v ∉ G.Max → s t v = s 0 v) →
    -- Howard steps at every Max vertex
    (∀ t, t < T → ∀ z ∈ G.Max, G.HowardAt (s t) (s (t + 1)) z) →
    -- every step changes the state (the run has not stopped before `T`)
    (∀ t, t < T → s (t + 1) ≠ s t) →
    T ≤ (∑ z ∈ G.Max, (G.E z).card) * Fintype.card V ∧
    ∀ t, t < T → ∃ v, G.d (s t) v ≠ G.d (s T) v ∧
      (∀ u, G.d (s t) u ≠ G.d (s T) u → G.d (s t) v ≤ G.d (s t) u) ∧
      G.d (s t) v < G.d (s (t + 1)) v

end

end PG
