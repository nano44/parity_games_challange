/-
The order of `PGLemmas/Defs.lean` (Friedmann arXiv 1106.0778 §3) against VJ00 (BRICS RS-00-48)
§4.2 as printed.  VJ00 compares the path components after cutting them down to the vertices
more relevant than the cycle node (`B ∩ V_{>ℓ}`), and uses `≤` on lengths.  On play values, whose
path component already lies in `V_{>ℓ}` (VJ00 (1)), the two orders are the same relation
(`vj00Le_iff`), and every `val pr s v` is such a value (`val_proper`).
-/
import PGLemmas.Play

namespace PG

open Classical

noncomputable section

variable {V : Type*} {pr : V → ℕ}

/-- `B ∩ V_{>ℓ}` (VJ00 §4.1: `V_{>w} = {v ∈ V : v > w}`). -/
def above (pr : V → ℕ) (ℓ : V) (B : Finset V) : Finset V := B.filter (fun u => pr ℓ < pr u)

/-- VJ00 §4.2, as printed.  «(ℓ, (B, k)) ⊴ (ℓ′, (B′, k′)) if and only if either ℓ ≺ ℓ′, or ℓ = ℓ′
and (B, k) ⊴_ℓ (B′, k′)», where «(B, k) ⊴_ℓ (B′, k′) if and only if either B ≺_ℓ B′, or B =_ℓ B′ and
either ℓ ∈ R− and k ≤ k′, or ℓ ∈ R+ and k′ ≤ k», `B ⪯_ℓ C` means `B ∩ V_{>ℓ} ⪯ C ∩ V_{>ℓ}`,
`B =_ℓ C` means `B ⪯_ℓ C` and `C ⪯_ℓ B`, `B ≺_ℓ C` means `B ⪯_ℓ C` and not `C ⪯_ℓ B`, and
`B ⪯ C` means `B ≺ C` or `B = C`; and `ℓ ≺ ℓ′` means `Reward(ℓ) ≤ Reward(ℓ′)` and `ℓ ≠ ℓ′`. -/
def vj00Le (pr : V → ℕ) (x y : Val V) : Prop :=
  let setLe : Finset V → Finset V → Prop := fun B C =>
    setLt pr (above pr x.top B) (above pr x.top C) ∨ above pr x.top B = above pr x.top C
  (rew pr x.top ≤ rew pr y.top ∧ x.top ≠ y.top) ∨
  (x.top = y.top ∧
    ((setLe x.set y.set ∧ ¬ setLe y.set x.set) ∨
     ((setLe x.set y.set ∧ setLe y.set x.set) ∧
       ((¬ Even (pr x.top) ∧ x.len ≤ y.len) ∨ (Even (pr x.top) ∧ y.len ≤ x.len)))))

/-- A triple is a possible play value if its path component lies above its cycle node
(VJ00 (1): `PlayValues ⊆ {(v, (B, k)) : B ⊆ V_{>v}}`). -/
def Proper (pr : V → ℕ) (x : Val V) : Prop := ∀ u ∈ x.set, pr x.top < pr u

theorem above_eq_self {x : Val V} (h : Proper pr x) : above pr x.top x.set = x.set := by
  unfold above
  exact Finset.filter_true_of_mem h

/-- On play values, VJ00 §4.2's order as printed is the order of `Defs.lean`. -/
theorem vj00Le_iff (hpr : Function.Injective pr) {x y : Val V} (hx : Proper pr x)
    (hy : Proper pr y) : vj00Le pr x y ↔ Val.le pr x y := by
  unfold vj00Le Val.le
  dsimp only
  rw [Val.lt_iff]
  constructor
  · rintro (⟨hle, hne⟩ | ⟨et, h⟩)
    · exact Or.inl (Or.inl (lt_of_le_of_ne hle (fun e => hne (rew_injective hpr e))))
    · have hy' : above pr x.top y.set = y.set := by rw [et]; exact above_eq_self hy
      rw [above_eq_self hx, hy'] at h
      rcases h with ⟨h1 | h1, h2⟩ | ⟨⟨h1, h2⟩, h3⟩
      · exact Or.inl (Or.inr ⟨et, Or.inl h1⟩)
      · exact absurd (Or.inr h1.symm) h2
      · -- equal path components: the lengths decide
        have es : x.set = y.set := by
          rcases h1 with h1 | h1
          · rcases h2 with h2 | h2
            · exact absurd h2 (setLt_asymm hpr h1)
            · exact h2.symm
          · exact h1
        rcases h3 with ⟨hp, hl⟩ | ⟨hp, hl⟩
        · rcases Nat.lt_or_ge x.len y.len with hlt | hge
          · exact Or.inl (Or.inr ⟨et, Or.inr ⟨es, Or.inl ⟨hlt, hp⟩⟩⟩)
          · exact Or.inr (Val.ext et es (by omega))
        · rcases Nat.lt_or_ge y.len x.len with hlt | hge
          · exact Or.inl (Or.inr ⟨et, Or.inr ⟨es, Or.inr ⟨hlt, hp⟩⟩⟩)
          · exact Or.inr (Val.ext et es (by omega))
  · rintro ((h | ⟨et, h⟩) | rfl)
    · exact Or.inl ⟨h.le, fun e => by rw [e] at h; exact lt_irrefl _ h⟩
    · have hy' : above pr x.top y.set = y.set := by rw [et]; exact above_eq_self hy
      refine Or.inr ⟨et, ?_⟩
      rw [above_eq_self hx, hy']
      rcases h with h | ⟨es, h⟩
      · refine Or.inl ⟨Or.inl h, ?_⟩
        rintro (h' | h')
        · exact setLt_asymm hpr h h'
        · rw [h'] at h; exact setLt_irrefl _ h
      · refine Or.inr ⟨⟨Or.inr es, Or.inr es.symm⟩, ?_⟩
        rcases h with ⟨hl, hp⟩ | ⟨hl, hp⟩
        · exact Or.inl ⟨hp, hl.le⟩
        · exact Or.inr ⟨hp, hl.le⟩
    · refine Or.inr ⟨rfl, Or.inr ⟨⟨Or.inr rfl, Or.inr rfl⟩, ?_⟩⟩
      by_cases hp : Even (pr x.top)
      · exact Or.inr ⟨hp, le_rfl⟩
      · exact Or.inl ⟨hp, le_rfl⟩

/-- Every node valuation of a positional play is a play value in VJ00's sense (1). -/
theorem val_proper [Fintype V] (s : V → V) (v : V) : Proper pr (val pr s v) := by
  intro u hu
  exact (mem_pset.mp hu).1

end

end PG
