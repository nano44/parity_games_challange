/-
ClassOrder (`PGLemmas/GenomeOrderStatement.lean`), proved: `class_order : G.ClassOrderStatement`.
No premise.

* `pw_lt_of_max`   if the most relevant vertex of `A \ B` is below a vertex of `B \ A`, then
                   `Σ_{x ∈ A} 2^(pr x) < Σ_{x ∈ B} 2^(pr x)` (injective priorities).
* `clsLt_iff`      `clsLt` with the symmetric difference spelled out by membership (no decidable
                   equality instance in the statement).
* `clsKey_lt_iff`, `clsKey_le_iff`, `clsKey_injective`: the order-embedding.
-/
import PGLemmas.GenomeOrderStatement
import PGLemmas.GenomeK15

namespace PG

open Classical
open scoped symmDiff

noncomputable section

section Weights

variable {V : Type*} {pr : V → ℕ}

theorem pw_split (A B : Finset V) : pw pr (A ∩ B) + pw pr (A \ B) = pw pr A := by
  have h := Finset.sum_sdiff (f := fun u => (2 : ℤ) ^ pr u)
    (Finset.inter_subset_left : A ∩ B ⊆ A)
  rw [Finset.sdiff_inter_self_left] at h
  unfold pw
  linarith

/-- If a vertex `d` of `B \ A` is at least as relevant as every vertex of `A \ B`, then `B` is
heavier than `A`. -/
theorem pw_lt_of_max (hpr : Function.Injective pr) {A B : Finset V} {d : V} (hB : d ∈ B)
    (hA : d ∉ A) (hmax : ∀ x, x ∈ A → x ∉ B → pr x ≤ pr d) : pw pr A < pw pr B := by
  have h1 := pw_split (pr := pr) A B
  have h2 := pw_split (pr := pr) B A
  rw [Finset.inter_comm B A] at h2
  have h3 : pw pr (A \ B) < (2 : ℤ) ^ pr d := by
    apply pw_lt hpr
    intro u hu
    have hu' := Finset.mem_sdiff.mp hu
    exact lt_of_le_of_ne (hmax u hu'.1 hu'.2) (fun e => hA (hpr e ▸ hu'.1))
  have h4 : (2 : ℤ) ^ pr d ≤ pw pr (B \ A) := by
    unfold pw
    exact Finset.single_le_sum (f := fun u => (2 : ℤ) ^ pr u) (fun u _ => by positivity)
      (Finset.mem_sdiff.mpr ⟨hB, hA⟩)
  linarith

end Weights

namespace Genome

variable {G : Genome}

/-- `clsLt`, with the symmetric difference spelled out. -/
theorem clsLt_iff {c c' : G.Vertex × Finset G.Vertex} : G.clsLt c c' ↔
    rew G.pr c.1 < rew G.pr c'.1 ∨ (c.1 = c'.1 ∧ ∃ d, d ∈ c'.2 ∧ d ∉ c.2 ∧
      ∀ x, (x ∈ c.2 ∧ x ∉ c'.2) ∨ (x ∈ c'.2 ∧ x ∉ c.2) → G.pr x ≤ G.pr d) := by
  unfold clsLt
  simp only [Finset.mem_symmDiff]
  constructor
  · rintro (h | ⟨h1, d, hd, hmax, hd'⟩)
    · exact Or.inl h
    · refine Or.inr ⟨h1, d, hd', ?_, hmax⟩
      rcases hd with ⟨_, h2⟩ | ⟨_, h2⟩
      · exact absurd hd' h2
      · exact h2
  · rintro (h | ⟨h1, d, hd', hdA, hmax⟩)
    · exact Or.inl h
    · exact Or.inr ⟨h1, d, Or.inr ⟨hd', hdA⟩, hmax, hd'⟩

theorem clsLt_irrefl (c : G.Vertex × Finset G.Vertex) : ¬ G.clsLt c c := by
  rw [clsLt_iff]
  rintro (h | ⟨-, d, hd, hd', -⟩)
  · exact lt_irrefl _ h
  · exact hd' hd

theorem clsKey_lt_of_clsLt (h : G.WF) {c c' : G.Vertex × Finset G.Vertex}
    (hlt : G.clsLt c c') : G.clsKey c < G.clsKey c' := by
  have hpr := pr_injective h
  unfold clsKey
  rw [Prod.Lex.toLex_lt_toLex]
  rcases clsLt_iff.mp hlt with h1 | ⟨h1, d, hd', hdA, hmax⟩
  · exact Or.inl h1
  · refine Or.inr ⟨by rw [h1], ?_⟩
    exact pw_lt_of_max hpr hd' hdA (fun x hx hx' => hmax x (Or.inl ⟨hx, hx'⟩))

/-- Two classes are equal or comparable. -/
theorem clsLt_total (h : G.WF) (c c' : G.Vertex × Finset G.Vertex) :
    G.clsLt c c' ∨ c = c' ∨ G.clsLt c' c := by
  have hpr := pr_injective h
  by_cases h1 : c.1 = c'.1
  · by_cases h2 : c.2 = c'.2
    · exact Or.inr (Or.inl (Prod.ext h1 h2))
    · -- the most relevant vertex of the symmetric difference decides
      have hne : ((c.2 \ c'.2) ∪ (c'.2 \ c.2)).Nonempty := by
        by_contra hemp
        rw [Finset.not_nonempty_iff_eq_empty] at hemp
        apply h2
        ext x
        constructor
        · intro hx
          by_contra hx'
          have hm : x ∈ (c.2 \ c'.2) ∪ (c'.2 \ c.2) :=
            Finset.mem_union.mpr (Or.inl (Finset.mem_sdiff.mpr ⟨hx, hx'⟩))
          rw [hemp] at hm
          exact absurd hm (Finset.notMem_empty _)
        · intro hx
          by_contra hx'
          have hm : x ∈ (c.2 \ c'.2) ∪ (c'.2 \ c.2) :=
            Finset.mem_union.mpr (Or.inr (Finset.mem_sdiff.mpr ⟨hx, hx'⟩))
          rw [hemp] at hm
          exact absurd hm (Finset.notMem_empty _)
      obtain ⟨d, hd, hmax⟩ := Finset.exists_max_image _ G.pr hne
      have hmax' : ∀ x, (x ∈ c.2 ∧ x ∉ c'.2) ∨ (x ∈ c'.2 ∧ x ∉ c.2) → G.pr x ≤ G.pr d := by
        intro x hx
        apply hmax
        rcases hx with hx | hx
        · exact Finset.mem_union.mpr (Or.inl (Finset.mem_sdiff.mpr hx))
        · exact Finset.mem_union.mpr (Or.inr (Finset.mem_sdiff.mpr hx))
      rcases Finset.mem_union.mp hd with hd | hd
      · have hd' := Finset.mem_sdiff.mp hd
        exact Or.inr (Or.inr (clsLt_iff.mpr (Or.inr ⟨h1.symm, d, hd'.1, hd'.2,
          fun x hx => hmax' x hx.symm⟩)))
      · have hd' := Finset.mem_sdiff.mp hd
        exact Or.inl (clsLt_iff.mpr (Or.inr ⟨h1, d, hd'.1, hd'.2, hmax'⟩))
  · rcases lt_or_gt_of_ne (fun e => h1 (rew_injective hpr e)) with hlt | hgt
    · exact Or.inl (Or.inl hlt)
    · exact Or.inr (Or.inr (Or.inl hgt))

/-- `clsKey` is an order-embedding for `clsLt`. -/
theorem clsKey_lt_iff (h : G.WF) {c c' : G.Vertex × Finset G.Vertex} :
    G.clsLt c c' ↔ G.clsKey c < G.clsKey c' := by
  refine ⟨clsKey_lt_of_clsLt h, fun hk => ?_⟩
  rcases clsLt_total h c c' with h1 | h1 | h1
  · exact h1
  · rw [h1] at hk
    exact absurd hk (lt_irrefl _)
  · exact absurd hk (lt_asymm (clsKey_lt_of_clsLt h h1))

theorem clsKey_injective (h : G.WF) : Function.Injective G.clsKey := by
  intro c c' e
  rcases clsLt_total h c c' with h1 | h1 | h1
  · exact absurd e (ne_of_lt (clsKey_lt_of_clsLt h h1))
  · exact h1
  · exact absurd e.symm (ne_of_lt (clsKey_lt_of_clsLt h h1))

/-- `clsKey` is an order-embedding for `clsLe`. -/
theorem clsKey_le_iff (h : G.WF) {c c' : G.Vertex × Finset G.Vertex} :
    G.clsLe c c' ↔ G.clsKey c ≤ G.clsKey c' := by
  unfold clsLe
  rw [le_iff_lt_or_eq, clsKey_lt_iff h]
  exact or_congr Iff.rfl ⟨fun e => by rw [e], fun e => clsKey_injective h e⟩

theorem clsLt_trans (h : G.WF) {c c' c'' : G.Vertex × Finset G.Vertex} (h1 : G.clsLt c c')
    (h2 : G.clsLt c' c'') : G.clsLt c c'' :=
  (clsKey_lt_iff h).mpr (lt_trans ((clsKey_lt_iff h).mp h1) ((clsKey_lt_iff h).mp h2))

/-- **ClassOrder** (box 208 §1), for all pairs `(Λ, E)`. -/
theorem class_order : G.ClassOrderStatement := by
  intro h
  exact ⟨clsLt_irrefl, fun _ _ _ h1 h2 => clsLt_trans h h1 h2, clsLt_total h,
    fun _ _ => clsKey_lt_iff h, fun _ _ => clsKey_le_iff h⟩

end Genome

end

end PG
