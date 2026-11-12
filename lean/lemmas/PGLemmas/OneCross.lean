/-
Lemma ONE-CROSS (claude/l-red docs/red/R231-onecross.md §2): a gate with a constant face flips
at most once.  Proved from its three premises (F1, NO-TIE, LOC-GATE) over any preorder of values;
`one_cross_vj` is the instance for node valuations under an injective priority function.
-/
import PGLemmas.Order
import PGLemmas.Statements

namespace PG

/-- **Lemma ONE-CROSS**, abstract form. -/
theorem one_cross (α : Type*) [Preorder α] (F : Type*) : OneCrossStatement α F := by
  intro a b T face Ω c hface hconst hF1 hnotie hloc
  -- F1 along the run: the value of `b` never falls
  have hmono : ∀ d t, t + d ≤ T → Ω t b ≤ Ω (t + d) b := by
    intro d
    induction d with
    | zero => intro t _; exact le_rfl
    | succ d ih =>
      intro t ht
      exact (ih t (by omega)).trans (hF1 (t + d) (by omega))
  -- the states taking `b` are an initial segment
  have hseg : ∀ t t', t ≤ t' → t' ≤ T → face t = a → face t' = a := by
    intro t t' htt' ht' hta
    rcases hface t' ht' with h | hb
    · exact h
    · exfalso
      have h1 : Ω t' b < Ω t' a := (hloc t' ht').2 hb (hnotie t' ht').symm
      have h2 : Ω t a < Ω t b := (hloc t (by omega)).1 hta (hnotie t (by omega))
      have h3 : Ω t b ≤ Ω t' b := by
        have := hmono (t' - t) t (by omega)
        have e : t + (t' - t) = t' := by omega
        rwa [e] at this
      rw [hconst t' ht'] at h1
      rw [hconst t (by omega)] at h2
      exact lt_irrefl c (h2.trans_le (h3.trans h1.le))
  -- a change goes from `b` to `a`
  have hchange : ∀ t, t < T → face (t + 1) ≠ face t → face t = b ∧ face (t + 1) = a := by
    intro t ht hne
    rcases hface t (by omega) with ha | hb
    · exact absurd (by rw [hseg t (t + 1) (by omega) (by omega) ha, ha]) hne
    · refine ⟨hb, ?_⟩
      rcases hface (t + 1) (by omega) with ha' | hb'
      · exact ha'
      · exact absurd (by rw [hb', hb]) hne
  refine ⟨hseg, hchange, ?_⟩
  -- two changes at different times would give a state taking both `a` and `b`
  have hab : a ≠ b := by
    intro e
    exact hnotie 0 (by omega) (by rw [e])
  have key : ∀ t t', t < t' → t' < T → face (t + 1) ≠ face t → face (t' + 1) ≠ face t' →
      False := by
    intro t t' htt' ht' h h'
    have h1 := (hchange t (by omega) h).2
    have h2 := (hchange t' ht' h').1
    exact hab ((hseg (t + 1) t' (by omega) (by omega) h1).symm.trans h2)
  intro t t' ht ht' h h'
  rcases lt_trichotomy t t' with hlt | heq | hgt
  · exact absurd (key t t' hlt ht' h h') id
  · exact heq
  · exact absurd (key t' t hgt ht h' h) id

/-- The order on node valuations as a preorder, under an injective priority function. -/
@[reducible] def valPreorder {V : Type*} (pr : V → ℕ) (hpr : Function.Injective pr) :
    Preorder (Val V) where
  le := Val.le pr
  lt := Val.lt pr
  le_refl := Val.le_refl
  le_trans := fun _ _ _ h₁ h₂ => Val.le_trans hpr h₁ h₂
  lt_iff_le_not_ge := by
    intro x y
    constructor
    · intro h
      exact ⟨Val.le_of_lt h, Val.not_le_of_lt hpr h⟩
    · rintro ⟨h | rfl, hn⟩
      · exact h
      · exact absurd (Val.le_refl _) hn

/-- **Lemma ONE-CROSS** for node valuations: `⊴` is `Val.le pr`, `◁` is `Val.lt pr`. -/
theorem one_cross_vj {V : Type*} (pr : V → ℕ) (hpr : Function.Injective pr) (F : Type*) :
    @OneCrossStatement (Val V) (valPreorder pr hpr) F :=
  @one_cross (Val V) (valPreorder pr hpr) F

end PG
