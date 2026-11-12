/-
A concrete window, to show that the hypotheses of `lam_gap_sharp` can all hold together and
that its bound is attained: 4 vertices, one choice vertex, a window with `b − a = 1 = |Ch|`.

Vertices `0, 1, 2, 3` with priority = name.  `0` has a self-loop (the cycle node of every play);
`2 → 0`, `3 → 0`; the choice vertex `1` may go to `2` or to `3`.  At state 0 it goes to `3` (value
`(0, {1, 3}, 2)`), Howard's step moves it to `2` (value `(0, {1, 2}, 2)`, better: the top
difference `3` is odd and lies in the old set).
-/
import PGLemmas.LamGap

namespace PG.Example

open Classical

noncomputable section

/-- priority = name -/
def pr : Fin 4 → ℕ := fun v => v.val

theorem pr_inj : Function.Injective pr := fun _ _ h => Fin.ext h

/-- the successors of the choice vertex `1` (other vertices are not choice vertices) -/
def E : Fin 4 → Finset (Fin 4) := fun _ => {2, 3}

def Ch : Finset (Fin 4) := {1}

/-- state 0: `1 → 3` -/
def s0 : Fin 4 → Fin 4 := fun v => if v = 1 then 3 else 0

/-- state 1: `1 → 2` -/
def s1 : Fin 4 → Fin 4 := fun v => if v = 1 then 2 else 0

def s : ℕ → Fin 4 → Fin 4 := fun t => if t = 0 then s0 else s1

/-- the value of the cycle node `0` -/
def A : Val (Fin 4) := ⟨0, ∅, 0⟩

theorem le_three (v : Fin 4) : pr v ≤ pr 3 := by
  unfold pr
  have := v.isLt
  show v.val ≤ 3
  omega

section
variable {σ : Fin 4 → Fin 4}

theorem lam_zero (h0 : σ 0 = 0) : lam pr σ 0 = 0 := by
  apply lam_unique pr_inj
  · exact ⟨⟨0, rfl⟩, 1, one_pos, h0⟩
  · rintro u ⟨⟨n, hn⟩, -⟩
    rw [Function.iterate_fixed h0] at hn
    rw [← hn]

theorem lam_of_succ_zero (h0 : σ 0 = 0) {v : Fin 4} (hv : σ v = 0) : lam pr σ v = 0 := by
  rw [← lam_succ pr_inj v, hv, lam_zero h0]

theorem val_zero (h0 : σ 0 = 0) : val pr σ 0 = A := val_of_lam_eq (lam_zero h0)

theorem val_of_succ_zero (h0 : σ 0 = 0) {v : Fin 4} (hv : σ v = 0) (hne : v ≠ 0) :
    val pr σ v = ext pr v A := by
  have hl : lam pr σ v ≠ v := by rw [lam_of_succ_zero h0 hv]; exact fun e => hne e.symm
  rw [val_step pr_inj hl, hv, val_zero h0]

end

theorem ext_two_set : (ext pr 2 A).set = {2} := by
  have h : pr (0 : Fin 4) < pr 2 := by decide
  simp only [ext, A, h, ite_true]
  rfl

theorem ext_three_set : (ext pr 3 A).set = {3} := by
  have h : pr (0 : Fin 4) < pr 3 := by decide
  simp only [ext, A, h, ite_true]
  rfl

/-- `(0, {3}, 1) ◁ (0, {2}, 1)`: the vertex `3` is odd. -/
theorem three_lt_two : Val.lt pr (ext pr 3 A) (ext pr 2 A) := by
  rw [Val.lt_iff]
  refine Or.inr ⟨rfl, Or.inl ?_⟩
  rw [ext_two_set, ext_three_set]
  exact setLt_of_mem_left (d := 3) (Finset.mem_singleton_self 3) (by simp) (by decide)
    (fun x _ => le_three x)

/-- `(0, {1, 3}, 2) ◁ (0, {1, 2}, 2)`. -/
theorem old_lt_new : Val.lt pr (ext pr 1 (ext pr 3 A)) (ext pr 1 (ext pr 2 A)) := by
  apply ext_lt _ _ three_lt_two
  · rw [ext_three_set]; simp
  · rw [ext_two_set]; simp

theorem s0_zero : s0 0 = 0 := by simp [s0]
theorem s1_zero : s1 0 = 0 := by simp [s1]

theorem lam_s0 (v : Fin 4) : lam pr s0 v = 0 := by
  by_cases h1 : v = 1
  · subst h1
    have h3 : lam pr s0 3 = 0 := lam_of_succ_zero s0_zero (by simp [s0])
    rw [← lam_succ pr_inj (1 : Fin 4)]
    have : s0 1 = 3 := by simp [s0]
    rw [this, h3]
  · exact lam_of_succ_zero s0_zero (by simp [s0, h1])

theorem lam_s1 (v : Fin 4) : lam pr s1 v = 0 := by
  by_cases h1 : v = 1
  · subst h1
    have h2 : lam pr s1 2 = 0 := lam_of_succ_zero s1_zero (by simp [s1])
    rw [← lam_succ pr_inj (1 : Fin 4)]
    have : s1 1 = 2 := by simp [s1]
    rw [this, h2]
  · exact lam_of_succ_zero s1_zero (by simp [s1, h1])

theorem val_s0_two : val pr s0 2 = ext pr 2 A :=
  val_of_succ_zero s0_zero (by simp [s0]) (by decide)

theorem val_s0_three : val pr s0 3 = ext pr 3 A :=
  val_of_succ_zero s0_zero (by simp [s0]) (by decide)

theorem val_s0_one : val pr s0 1 = ext pr 1 (ext pr 3 A) := by
  have hl : lam pr s0 1 ≠ 1 := by rw [lam_s0]; decide
  have : s0 1 = 3 := by simp [s0]
  rw [val_step pr_inj hl, this, val_s0_three]

theorem val_s1_one : val pr s1 1 = ext pr 1 (ext pr 2 A) := by
  have hl : lam pr s1 1 ≠ 1 := by rw [lam_s1]; decide
  have : s1 1 = 2 := by simp [s1]
  rw [val_step pr_inj hl, this, val_of_succ_zero s1_zero (by simp [s1]) (by decide)]

/-- off the choice vertex the two states have the same values -/
theorem val_eq_off_one {v : Fin 4} (h1 : v ≠ 1) : val pr s0 v = val pr s1 v := by
  by_cases h0 : v = 0
  · subst h0
    rw [val_zero s0_zero, val_zero s1_zero]
  · rw [val_of_succ_zero s0_zero (by simp [s0, h1]) h0,
      val_of_succ_zero s1_zero (by simp [s1, h1]) h0]

theorem s_zero : s 0 = s0 := by simp [s]
theorem s_one : s 1 = s1 := by simp [s]

/-- The window `0..1` of the run `s0, s1, s1, …`. -/
theorem window : Window pr E Ch s 0 1 := by
  refine ⟨by omega, ?_, ?_, ?_, ?_, ?_⟩
  · -- only the choice vertex moves
    intro t _ ht v hv
    have hv1 : v ≠ 1 := by simpa [Ch] using hv
    have ht' : t = 0 ∨ t = 1 := by omega
    rcases ht' with rfl | rfl
    · rfl
    · rw [s_one, s_zero]; simp [s0, s1, hv1]
  · -- the step `0 → 1` is a Howard step at the choice vertex
    intro t _ ht v hv
    have hv1 : v = 1 := by simpa [Ch] using hv
    have ht0 : t = 0 := by omega
    subst hv1 ht0
    rw [s_zero, s_one]
    have h1 : s1 1 = 2 := by simp [s1]
    have h0 : s0 1 = 3 := by simp [s0]
    refine ⟨by rw [h1]; simp [E], ?_, ?_⟩
    · intro w hw
      rw [h1, val_s0_two]
      have hw' : w = 2 ∨ w = 3 := by simpa [E] using hw
      rcases hw' with rfl | rfl
      · rw [val_s0_two]; exact Val.le_refl _
      · rw [val_s0_three]; exact Val.le_of_lt three_lt_two
    · rintro ⟨-, hbest⟩
      have := hbest 2 (by simp [E])
      rw [h0, val_s0_two, val_s0_three] at this
      exact absurd this (Val.not_le_of_lt pr_inj three_lt_two)
  · -- premise (M)
    intro t _ ht v
    have ht0 : t = 0 := by omega
    subst ht0
    rw [s_zero, s_one]
    by_cases h1 : v = 1
    · subst h1
      rw [val_s0_one, val_s1_one]
      exact Val.le_of_lt old_lt_new
    · rw [val_eq_off_one h1]
      exact Val.le_refl _
  · -- every cycle node is `0` in both states
    intro t _ ht v
    have ht' : t = 0 ∨ t = 1 := by omega
    rcases ht' with rfl | rfl
    · rfl
    · rw [s_one, s_zero, lam_s1, lam_s0]
  · -- the step changes the state
    intro t _ ht
    have ht0 : t = 0 := by omega
    subst ht0
    rw [s_zero, s_one]
    intro h
    have := congrFun h 1
    simp [s0, s1] at this

/-- The hypotheses of `lam_gap_sharp` are satisfiable, and its bound is attained:
here `b − a = 1 − 0 = 1 = |Ch|`. -/
theorem window_example : ∃ (pr : Fin 4 → ℕ) (E : Fin 4 → Finset (Fin 4)) (Ch : Finset (Fin 4))
    (s : ℕ → Fin 4 → Fin 4), Function.Injective pr ∧ Window pr E Ch s 0 1 ∧ 1 - 0 = Ch.card :=
  ⟨pr, E, Ch, s, pr_inj, window, by simp [Ch]⟩

end

end PG.Example
