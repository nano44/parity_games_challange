/-
Facts about the order on node valuations (`PGLemmas/Defs.lean`): under an injective priority
function, `Val.lt` is a strict total order and `Val.le` a total order on ALL triples; `ext`
(prepending a vertex to a path value) is strictly monotone on values whose path component does
not contain the vertex (the fleet's F4′, P-N5-XICYC-fixes l. 33-41; box 101 §2 (P2)).
-/
import PGLemmas.Defs
import Mathlib.Tactic

namespace PG

open Classical
open scoped symmDiff

noncomputable section

variable {V : Type*} {pr : V → ℕ}

/-! ### Rewards -/

theorem rew_injective (hpr : Function.Injective pr) : Function.Injective (rew pr) := by
  intro u v h
  apply hpr
  unfold rew at h
  by_cases hu : Even (pr u) <;> by_cases hv : Even (pr v) <;> simp only [hu, hv, ite_true, ite_false] at h
  · exact_mod_cast h
  · have h0 : pr v = 0 := by omega
    rw [h0] at hv
    exact absurd ⟨0, rfl⟩ hv
  · have h0 : pr u = 0 := by omega
    rw [h0] at hu
    exact absurd ⟨0, rfl⟩ hu
  · omega

/-! ### The order on path components -/

theorem setLt_irrefl (M : Finset V) : ¬ setLt pr M M := by
  rintro ⟨d, hd, -⟩
  rw [Finset.mem_symmDiff] at hd
  tauto

theorem setLt_asymm (hpr : Function.Injective pr) {M N : Finset V} (h : setLt pr M N) :
    ¬ setLt pr N M := by
  rintro ⟨d', hd', hmax', hside'⟩
  obtain ⟨d, hd, hmax, hside⟩ := h
  have hd'' : d' ∈ M ∆ N := by rw [symmDiff_comm]; exact hd'
  have hdN : d ∈ N ∆ M := by rw [symmDiff_comm]; exact hd
  have e : d = d' := hpr (le_antisymm (hmax' d hdN) (hmax d' hd''))
  subst e
  rw [Finset.mem_symmDiff] at hd
  tauto

theorem setLt_trans (hpr : Function.Injective pr) {M N K : Finset V} (h₁ : setLt pr M N)
    (h₂ : setLt pr N K) : setLt pr M K := by
  obtain ⟨d₁, hd₁, hmax₁, hside₁⟩ := h₁
  obtain ⟨d₂, hd₂, hmax₂, hside₂⟩ := h₂
  have hsub : ∀ x ∈ M ∆ K, x ∈ M ∆ N ∨ x ∈ N ∆ K := by
    intro x hx
    simp only [Finset.mem_symmDiff] at hx ⊢
    tauto
  rw [Finset.mem_symmDiff] at hd₁ hd₂
  rcases lt_trichotomy (pr d₁) (pr d₂) with hlt | heq | hgt
  · -- `d₂` is the maximum of `M ∆ K`; `M` and `N` agree at `d₂`
    have hagree : (d₂ ∈ M ↔ d₂ ∈ N) := by
      by_contra hne
      have : d₂ ∈ M ∆ N := by rw [Finset.mem_symmDiff]; tauto
      exact absurd (hmax₁ d₂ this) (not_le.mpr hlt)
    refine ⟨d₂, ?_, ?_, ?_⟩
    · rw [Finset.mem_symmDiff]; tauto
    · intro x hx
      rcases hsub x hx with hx | hx
      · exact (hmax₁ x hx).trans hlt.le
      · exact hmax₂ x hx
    · tauto
  · -- impossible: `d₁ = d₂` lies on opposite sides
    have e : d₁ = d₂ := hpr heq
    subst e
    tauto
  · -- `d₁` is the maximum of `M ∆ K`; `N` and `K` agree at `d₁`
    have hagree : (d₁ ∈ N ↔ d₁ ∈ K) := by
      by_contra hne
      have : d₁ ∈ N ∆ K := by rw [Finset.mem_symmDiff]; tauto
      exact absurd (hmax₂ d₁ this) (not_le.mpr hgt)
    refine ⟨d₁, ?_, ?_, ?_⟩
    · rw [Finset.mem_symmDiff]; tauto
    · intro x hx
      rcases hsub x hx with hx | hx
      · exact hmax₁ x hx
      · exact (hmax₂ x hx).trans hgt.le
    · tauto

theorem setLt_total {M N : Finset V} (hne : M ≠ N) : setLt pr M N ∨ setLt pr N M := by
  have hnonempty : (M ∆ N).Nonempty := by
    rw [Finset.nonempty_iff_ne_empty]
    intro h
    apply hne
    ext x
    have hx : x ∉ M ∆ N := by rw [h]; exact Finset.notMem_empty x
    rw [Finset.mem_symmDiff] at hx
    tauto
  obtain ⟨d, hd, hmax⟩ := Finset.exists_max_image (M ∆ N) pr hnonempty
  have hd' := hd
  rw [Finset.mem_symmDiff] at hd'
  have hmax' : ∀ x ∈ N ∆ M, pr x ≤ pr d := by
    intro x hx; rw [symmDiff_comm] at hx; exact hmax x hx
  have hdN : d ∈ N ∆ M := by rw [symmDiff_comm]; exact hd
  by_cases hev : Even (pr d)
  · rcases hd' with ⟨hM, hN⟩ | ⟨hN, hM⟩
    · exact Or.inr ⟨d, hdN, hmax', Or.inl ⟨hM, hev⟩⟩
    · exact Or.inl ⟨d, hd, hmax, Or.inl ⟨hN, hev⟩⟩
  · rcases hd' with ⟨hM, hN⟩ | ⟨hN, hM⟩
    · exact Or.inl ⟨d, hd, hmax, Or.inr ⟨hM, hev⟩⟩
    · exact Or.inr ⟨d, hdN, hmax', Or.inr ⟨hN, hev⟩⟩

/-- `M ≺ N` from a witness: `d` lies in `M` only, is odd, and is the most relevant vertex of the
symmetric difference. -/
theorem setLt_of_mem_left {M N : Finset V} {d : V} (hM : d ∈ M) (hN : d ∉ N)
    (hodd : ¬ Even (pr d)) (hmax : ∀ x, (x ∈ M ∧ x ∉ N) ∨ (x ∈ N ∧ x ∉ M) → pr x ≤ pr d) :
    setLt pr M N := by
  refine ⟨d, ?_, ?_, Or.inr ⟨hM, hodd⟩⟩
  · rw [Finset.mem_symmDiff]; exact Or.inl ⟨hM, hN⟩
  · intro x hx
    rw [Finset.mem_symmDiff] at hx
    exact hmax x hx

/-! ### The order on node valuations -/

theorem Val.lt_iff {x y : Val V} : Val.lt pr x y ↔
    rew pr x.top < rew pr y.top ∨ (x.top = y.top ∧ (setLt pr x.set y.set ∨
      (x.set = y.set ∧ ((x.len < y.len ∧ ¬ Even (pr x.top)) ∨
        (y.len < x.len ∧ Even (pr x.top)))))) := by
  unfold Val.lt
  tauto

theorem Val.lt_irrefl (x : Val V) : ¬ Val.lt pr x x := by
  rw [Val.lt_iff]
  rintro (h | ⟨-, h | ⟨-, h | h⟩⟩)
  · exact _root_.lt_irrefl _ h
  · exact setLt_irrefl _ h
  · exact _root_.lt_irrefl _ h.1
  · exact _root_.lt_irrefl _ h.1

theorem Val.lt_trans (hpr : Function.Injective pr) {x y z : Val V} (h₁ : Val.lt pr x y)
    (h₂ : Val.lt pr y z) : Val.lt pr x z := by
  rw [Val.lt_iff] at h₁ h₂ ⊢
  rcases h₁ with h₁ | ⟨e₁, h₁⟩
  · rcases h₂ with h₂ | ⟨e₂, -⟩
    · exact Or.inl (h₁.trans h₂)
    · exact Or.inl (e₂ ▸ h₁)
  · rcases h₂ with h₂ | ⟨e₂, h₂⟩
    · exact Or.inl (e₁ ▸ h₂)
    · refine Or.inr ⟨e₁.trans e₂, ?_⟩
      rcases h₁ with h₁ | ⟨s₁, h₁⟩
      · rcases h₂ with h₂ | ⟨s₂, -⟩
        · exact Or.inl (setLt_trans hpr h₁ h₂)
        · exact Or.inl (s₂ ▸ h₁)
      · rcases h₂ with h₂ | ⟨s₂, h₂⟩
        · exact Or.inl (s₁ ▸ h₂)
        · refine Or.inr ⟨s₁.trans s₂, ?_⟩
          rw [← e₁] at h₂
          rcases h₁ with ⟨l₁, p₁⟩ | ⟨l₁, p₁⟩ <;> rcases h₂ with ⟨l₂, p₂⟩ | ⟨l₂, p₂⟩
          · exact Or.inl ⟨l₁.trans l₂, p₁⟩
          · exact absurd p₂ p₁
          · exact absurd p₁ p₂
          · exact Or.inr ⟨l₂.trans l₁, p₁⟩

theorem Val.lt_asymm (hpr : Function.Injective pr) {x y : Val V} (h : Val.lt pr x y) :
    ¬ Val.lt pr y x := fun h' => Val.lt_irrefl x (Val.lt_trans hpr h h')

/-- Trichotomy: `Val.lt` is total on all triples. -/
theorem Val.lt_trichotomy (hpr : Function.Injective pr) (x y : Val V) :
    Val.lt pr x y ∨ x = y ∨ Val.lt pr y x := by
  rcases _root_.lt_trichotomy (rew pr x.top) (rew pr y.top) with h | h | h
  · exact Or.inl (Val.lt_iff.mpr (Or.inl h))
  · have et : x.top = y.top := rew_injective hpr h
    by_cases es : x.set = y.set
    · rcases _root_.lt_trichotomy x.len y.len with hl | hl | hl
      · by_cases hev : Even (pr x.top)
        · exact Or.inr (Or.inr (Val.lt_iff.mpr
            (Or.inr ⟨et.symm, Or.inr ⟨es.symm, Or.inr ⟨hl, et ▸ hev⟩⟩⟩)))
        · exact Or.inl (Val.lt_iff.mpr (Or.inr ⟨et, Or.inr ⟨es, Or.inl ⟨hl, hev⟩⟩⟩))
      · exact Or.inr (Or.inl (Val.ext et es hl))
      · by_cases hev : Even (pr x.top)
        · exact Or.inl (Val.lt_iff.mpr (Or.inr ⟨et, Or.inr ⟨es, Or.inr ⟨hl, hev⟩⟩⟩))
        · exact Or.inr (Or.inr (Val.lt_iff.mpr
            (Or.inr ⟨et.symm, Or.inr ⟨es.symm, Or.inl ⟨hl, et ▸ hev⟩⟩⟩)))
    · rcases setLt_total (pr := pr) es with hs | hs
      · exact Or.inl (Val.lt_iff.mpr (Or.inr ⟨et, Or.inl hs⟩))
      · exact Or.inr (Or.inr (Val.lt_iff.mpr (Or.inr ⟨et.symm, Or.inl hs⟩)))
  · exact Or.inr (Or.inr (Val.lt_iff.mpr (Or.inl h)))

theorem Val.le_refl (x : Val V) : Val.le pr x x := Or.inr rfl

theorem Val.le_of_lt {x y : Val V} (h : Val.lt pr x y) : Val.le pr x y := Or.inl h

theorem Val.le_trans (hpr : Function.Injective pr) {x y z : Val V} (h₁ : Val.le pr x y)
    (h₂ : Val.le pr y z) : Val.le pr x z := by
  rcases h₁ with h₁ | rfl
  · rcases h₂ with h₂ | rfl
    · exact Or.inl (Val.lt_trans hpr h₁ h₂)
    · exact Or.inl h₁
  · exact h₂

theorem Val.lt_of_lt_of_le (hpr : Function.Injective pr) {x y z : Val V} (h₁ : Val.lt pr x y)
    (h₂ : Val.le pr y z) : Val.lt pr x z := by
  rcases h₂ with h₂ | rfl
  · exact Val.lt_trans hpr h₁ h₂
  · exact h₁

theorem Val.lt_of_le_of_lt (hpr : Function.Injective pr) {x y z : Val V} (h₁ : Val.le pr x y)
    (h₂ : Val.lt pr y z) : Val.lt pr x z := by
  rcases h₁ with h₁ | rfl
  · exact Val.lt_trans hpr h₁ h₂
  · exact h₂

theorem Val.le_antisymm (hpr : Function.Injective pr) {x y : Val V} (h₁ : Val.le pr x y)
    (h₂ : Val.le pr y x) : x = y := by
  rcases h₁ with h₁ | rfl
  · exact absurd (Val.lt_of_lt_of_le hpr h₁ h₂) (Val.lt_irrefl x)
  · rfl

theorem Val.not_le_of_lt (hpr : Function.Injective pr) {x y : Val V} (h : Val.lt pr x y) :
    ¬ Val.le pr y x := fun h' => Val.lt_irrefl x (Val.lt_of_lt_of_le hpr h h')

theorem Val.lt_of_not_le (hpr : Function.Injective pr) {x y : Val V} (h : ¬ Val.le pr x y) :
    Val.lt pr y x := by
  rcases Val.lt_trichotomy hpr x y with h' | h' | h'
  · exact absurd (Or.inl h') h
  · exact absurd (Or.inr h') h
  · exact h'

/-- `x ⊴ y` puts the cycle components in reward order. -/
theorem Val.top_of_le {x y : Val V} (h : Val.le pr x y) :
    x.top = y.top ∨ rew pr x.top < rew pr y.top := by
  rcases h with h | rfl
  · rw [Val.lt_iff] at h
    rcases h with h | ⟨e, -⟩
    · exact Or.inr h
    · exact Or.inl e
  · exact Or.inl rfl

theorem Val.lt_of_rew_lt {x y : Val V} (h : rew pr x.top < rew pr y.top) : Val.lt pr x y :=
  Val.lt_iff.mpr (Or.inl h)

/-! ### `ext`: prepending a vertex to a path value -/

/-- `ext(v, (Λ, Π, k)) := (Λ, Π ∪ {v if v is more relevant than Λ}, k + 1)` (P-N5-XICYC §3 F3;
box 101 §2 (P1)). -/
def ext (pr : V → ℕ) (v : V) (x : Val V) : Val V :=
  ⟨x.top, if pr x.top < pr v then insert v x.set else x.set, x.len + 1⟩

@[simp] theorem ext_top (v : V) (x : Val V) : (ext pr v x).top = x.top := rfl

@[simp] theorem ext_len (v : V) (x : Val V) : (ext pr v x).len = x.len + 1 := rfl

theorem ext_set_subset (v : V) (x : Val V) : (ext pr v x).set ⊆ insert v x.set := by
  unfold ext
  dsimp only
  split_ifs
  · exact Finset.Subset.refl _
  · exact Finset.subset_insert _ _

theorem symmDiff_insert_insert {v : V} {M N : Finset V} (hM : v ∉ M) (hN : v ∉ N) :
    insert v M ∆ insert v N = M ∆ N := by
  ext a
  simp only [Finset.mem_symmDiff, Finset.mem_insert]
  by_cases ha : a = v
  · subst ha; tauto
  · tauto

theorem setLt_insert {v : V} {M N : Finset V} (hM : v ∉ M) (hN : v ∉ N) (h : setLt pr M N) :
    setLt pr (insert v M) (insert v N) := by
  obtain ⟨d, hd, hmax, hside⟩ := h
  refine ⟨d, ?_, ?_, ?_⟩
  · rw [symmDiff_insert_insert hM hN]; exact hd
  · rw [symmDiff_insert_insert hM hN]; exact hmax
  · rcases hside with ⟨h1, h2⟩ | ⟨h1, h2⟩
    · exact Or.inl ⟨Finset.mem_insert_of_mem h1, h2⟩
    · exact Or.inr ⟨Finset.mem_insert_of_mem h1, h2⟩

/-- F4′, strict form: `ext(v, ·)` is strictly monotone on values whose path components do not
contain `v`. -/
theorem ext_lt {v : V} {x y : Val V} (hx : v ∉ x.set) (hy : v ∉ y.set) (h : Val.lt pr x y) :
    Val.lt pr (ext pr v x) (ext pr v y) := by
  rw [Val.lt_iff] at h ⊢
  rcases h with h | ⟨et, h⟩
  · exact Or.inl h
  · refine Or.inr ⟨et, ?_⟩
    rcases h with h | ⟨es, h⟩
    · left
      unfold ext
      dsimp only
      rw [← et]
      split_ifs
      · exact setLt_insert hx hy h
      · exact h
    · right
      refine ⟨?_, ?_⟩
      · unfold ext
        dsimp only
        rw [← et, es]
      · simp only [ext_top, ext_len]
        rcases h with ⟨hl, hp⟩ | ⟨hl, hp⟩
        · exact Or.inl ⟨by omega, hp⟩
        · exact Or.inr ⟨by omega, hp⟩

/-- F4′: `ext(v, ·)` is monotone on values whose path components do not contain `v`. -/
theorem ext_le {v : V} {x y : Val V} (hx : v ∉ x.set) (hy : v ∉ y.set) (h : Val.le pr x y) :
    Val.le pr (ext pr v x) (ext pr v y) := by
  rcases h with h | rfl
  · exact Or.inl (ext_lt hx hy h)
  · exact Or.inr rfl

end

end PG
