/-
Optimal counterstrategies exist ([Fr] Lemma 3.1, the existence part; VJ00 §5): for every Even
strategy `σ` of a game whose Odd vertices all have a successor there is `τ` with
`OptCounter pr E V0 σ τ`.  So the hypothesis «σ̄_t is an optimal counterstrategy» of `f1`,
`brseg_opt` and `tcyc_opt` can always be met.

Proof: among the Odd strategies that follow the edges take one whose valuation is minimal in the
pointwise order (finitely many strategies).  If one of its Odd edges `u → w` were not
under-progressive, then `w` is worth strictly less than the current successor
(`underProgAt_of_le`), so switching `u` to `w` lowers no value (`val_mono_dual`) and lowers the
value of `u` (`underProgAt_of_opt`): a smaller valuation.  And a strategy all of whose Odd edges
are under-progressive is optimal (`val_le_of_underProg`).
-/
import PGLemmas.TwoPlayer

namespace PG

open Classical

noncomputable section

variable {V : Type*} [Fintype V] {pr : V → ℕ}

/-- [Fr] Lemma 3.1 (existence): «An optimal counterstrategy for player 1 w.r.t. σ exists». -/
def OptCounterExistsStatement (V : Type*) [Fintype V] : Prop :=
  ∀ (pr : V → ℕ), Function.Injective pr →
  ∀ (E : V → Finset V) (V0 : Finset V) (σ : V → V),
    (∀ u, u ∉ V0 → (E u).Nonempty) → ∃ τ, OptCounter pr E V0 σ τ

/-- A counterstrategy all of whose Odd edges are under-progressive is optimal. -/
theorem optCounter_of_underProg (hpr : Function.Injective pr) {E : V → Finset V}
    {V0 : Finset V} {σ τ : V → V} (hτ : ∀ u, u ∉ V0 → τ u ∈ E u)
    (h : ∀ u, u ∉ V0 → ∀ w ∈ E u, UnderProgAt pr (pair V0 σ τ) u w) :
    OptCounter pr E V0 σ τ := by
  refine ⟨hτ, fun τ₂ hτ₂ v => ?_⟩
  apply val_le_of_underProg hpr
  intro u
  by_cases hu : u ∈ V0
  · apply underProgAt_of_le hpr
    have e : pair V0 σ τ₂ u = pair V0 σ τ u := by
      unfold pair; rw [ite_eq_left hu, ite_eq_left hu]
    rw [e]
    exact Val.le_refl _
  · have e : pair V0 σ τ₂ u = τ₂ u := by unfold pair; rw [ite_eq_right hu]
    rw [e]
    exact h u hu (τ₂ u) (hτ₂ u hu)

/-- **Optimal counterstrategies exist.** -/
theorem optCounter_exists : OptCounterExistsStatement V := by
  intro pr hpr E V0 σ hne
  -- the strict pointwise order on the valuations of Odd's strategies
  let r : (V → V) → (V → V) → Prop := fun τ₂ τ =>
    (∀ v, Val.le pr (val pr (pair V0 σ τ₂) v) (val pr (pair V0 σ τ) v)) ∧
      ∃ v, Val.lt pr (val pr (pair V0 σ τ₂) v) (val pr (pair V0 σ τ) v)
  have : IsTrans (V → V) r := ⟨by
    rintro a b c ⟨h1, v, hv⟩ ⟨h2, -⟩
    exact ⟨fun x => Val.le_trans hpr (h1 x) (h2 x), v, Val.lt_of_lt_of_le hpr hv (h2 v)⟩⟩
  have : Std.Irrefl r := ⟨by
    rintro a ⟨-, v, hv⟩
    exact Val.lt_irrefl _ hv⟩
  have hwf : WellFounded r := Finite.wellFounded_of_trans_of_irrefl r
  -- some Odd strategy follows the edges
  have hS : ({τ : V → V | ∀ u, u ∉ V0 → τ u ∈ E u} : Set (V → V)).Nonempty :=
    ⟨fun u => if h : u ∉ V0 then (hne u h).choose else u, fun u hu => by
      simp only [hu, not_false_eq_true, dite_true]
      exact (hne u hu).choose_spec⟩
  obtain ⟨τ, hτ, hmin⟩ := hwf.has_min _ hS
  refine ⟨τ, optCounter_of_underProg hpr hτ fun u hu w hw => ?_⟩
  by_contra hnot
  -- the edge `u → w` is not under-progressive: switch `u` to `w`
  have hupd : Function.update (pair V0 σ τ) u w = pair V0 σ (Function.update τ u w) := by
    funext x
    by_cases hx : x = u
    · subst hx
      rw [Function.update_self]
      unfold pair
      rw [ite_eq_right hu, Function.update_self]
    · rw [Function.update_of_ne hx]
      unfold pair
      by_cases hx0 : x ∈ V0
      · rw [ite_eq_left hx0, ite_eq_left hx0]
      · rw [ite_eq_right hx0, ite_eq_right hx0, Function.update_of_ne hx]
  have hlt : Val.lt pr (val pr (pair V0 σ τ) w) (val pr (pair V0 σ τ) (pair V0 σ τ u)) :=
    Val.lt_of_not_le hpr (fun hle => hnot (underProgAt_of_le hpr hle))
  have hdown : ∀ v, Val.le pr (val pr (pair V0 σ (Function.update τ u w)) v)
      (val pr (pair V0 σ τ) v) := by
    intro v
    rw [← hupd]
    apply val_mono_dual hpr (pair V0 σ τ) (Function.update (pair V0 σ τ) u w)
    intro x
    by_cases hx : x = u
    · right
      rw [hx, Function.update_self]
      exact hlt
    · left
      exact Function.update_of_ne hx w (pair V0 σ τ)
  have hstrict : Val.lt pr (val pr (pair V0 σ (Function.update τ u w)) u)
      (val pr (pair V0 σ τ) u) := by
    rw [← hupd]
    exact Val.lt_of_not_le hpr (fun hle => hnot (underProgAt_of_opt hpr hle))
  refine hmin (Function.update τ u w) ?_ ⟨hdown, u, hstrict⟩
  intro x hx
  by_cases hxu : x = u
  · subst hxu
    rw [Function.update_self]
    exact hw
  · rw [Function.update_of_ne hxu]
    exact hτ x hx

end

end PG
