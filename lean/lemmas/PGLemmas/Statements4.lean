/-
DEPTH-COUNT3's count of shallow changes, as a statement (proposed to the Lead; same convention).

Source: claude/l-si docs/si/box100-scclin.md §3 (Lemma DEPTH-COUNT3: definition of depth, S_c),
with the gap D1 and its fix from claude/l-red docs/red/R234-lamgap.md §0 and §4 (a length-only
change with |Π| ≤ c is a change of depth in [0, c] that the count S_c(n) − 1 misses; corrected
bound n·(S_c(n) − 1) + n·(n − 1)·S′_c(n)).
-/
import PGLemmas.Defs
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Nat.Choose.Basic

namespace PG

open Classical
open scoped symmDiff

noncomputable section

variable {V : Type*}

/-- The depth of a change `x ≠ y` that keeps the cycle node (box 100 §3): «the number of
elements of Π_t (equivalently of Π_(t+1)) more relevant than z, the most relevant element of
Π_t Δ Π_(t+1); |Π_t| if Π_t = Π_(t+1) (a length-only change)».  (A change of the cycle node has
depth −1 there; it is excluded in the statement below instead.) -/
def depth (pr : V → ℕ) (x y : Val V) : ℕ :=
  if x.set = y.set then x.set.card
  else (x.set.filter (fun u => ∀ z ∈ x.set ∆ y.set, pr z < pr u)).card

/-- `S_c(n) := Σ_(j=0..c+1) C(n, j)` (box 100 §3). -/
def Sc (c n : ℕ) : ℕ := ∑ j ∈ Finset.range (c + 2), n.choose j

/-- `S′_c(n) := Σ_(j=0..c) C(n, j)` (R234 §0). -/
def Sc' (c n : ℕ) : ℕ := ∑ j ∈ Finset.range (c + 1), n.choose j

/-- DEPTH-COUNT3, corrected (R234 D1): a sequence of node valuations that never falls, with
lengths below `n` (as every play value has), makes at most `n·(S_c(n) − 1) + n·(n − 1)·S′_c(n)`
changes of depth in `[0, c]`, i.e. changes that keep the cycle node and have depth `≤ c`. -/
def DepthCountStatement (V : Type*) [Fintype V] : Prop :=
  ∀ (pr : V → ℕ), Function.Injective pr → ∀ (x : ℕ → Val V) (T c : ℕ),
    (∀ t, t < T → Val.le pr (x t) (x (t + 1))) →
    (∀ t, t ≤ T → (x t).len < Fintype.card V) →
    ((Finset.range T).filter (fun t => x t ≠ x (t + 1) ∧ (x t).top = (x (t + 1)).top ∧
        depth pr (x t) (x (t + 1)) ≤ c)).card ≤
      Fintype.card V * (Sc c (Fintype.card V) - 1) +
        Fintype.card V * (Fintype.card V - 1) * Sc' c (Fintype.card V)

/-- The length component of a play value is below the number of vertices (so
`DepthCountStatement` applies to `x t := val pr (s t) v`). -/
def PlenLtStatement (V : Type*) [Fintype V] : Prop :=
  ∀ (pr : V → ℕ), Function.Injective pr → ∀ (s : V → V) (v : V), plen pr s v < Fintype.card V

end

end PG
