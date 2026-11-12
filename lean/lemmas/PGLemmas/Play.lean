/-
Facts about the valuation of a positional play (`PGLemmas/Defs.lean`), all read off the
definition by plays:
* `lam_succ`       Λ(s v) = Λ(v)                      (a play and its tail share the cycle);
* `val_of_lam_eq`  Λ(v) = v ⇒ val v = (v, ∅, 0)        (box 101 §2 (P3); VJ00 (8));
* `val_step`       Λ(v) ≠ v ⇒ val v = ext(v, val(s v)) (box 101 §2 (P1); P-N5-XICYC §3 F3);
* `iterate_succ_ne_self`  Λ(v) ≠ v ⇒ v is not on the play of `s v` up to its cycle node
                   (the prefix of a play is a simple path).
-/
import PGLemmas.Order

namespace PG

open Classical

noncomputable section

variable {V : Type*} [Fintype V] {pr : V → ℕ} {s : V → V}

omit [Fintype V] in
/-- A play and its tail have the same cycle. -/
theorem onCycle_succ_iff (s : V → V) (v u : V) : OnCycle s (s v) u ↔ OnCycle s v u := by
  constructor
  · rintro ⟨⟨n, hn⟩, hp⟩
    exact ⟨⟨n + 1, by rw [Function.iterate_succ_apply]; exact hn⟩, hp⟩
  · rintro ⟨⟨n, hn⟩, p, hp0, hp⟩
    refine ⟨?_, p, hp0, hp⟩
    cases n with
    | zero =>
      -- `u = v` recurs with period `p`, so the tail reaches it after `p - 1` steps
      simp only [Function.iterate_zero, id_eq] at hn
      subst hn
      refine ⟨p - 1, ?_⟩
      rw [← Function.iterate_succ_apply, Nat.succ_eq_add_one, Nat.sub_add_cancel hp0]
      exact hp
    | succ n => exact ⟨n, by rw [← Function.iterate_succ_apply]; exact hn⟩

/-- The cycle node is the only largest-priority vertex of the cycle. -/
theorem lam_unique (hpr : Function.Injective pr) {v w : V} (hw : OnCycle s v w)
    (hmax : ∀ u, OnCycle s v u → pr u ≤ pr w) : lam pr s v = w :=
  hpr (le_antisymm (hmax _ (lam_spec pr s v).1) ((lam_spec pr s v).2 w hw))

/-- `Λ(s v) = Λ(v)`. -/
theorem lam_succ (hpr : Function.Injective pr) (v : V) : lam pr s (s v) = lam pr s v := by
  apply lam_unique hpr
  · exact (onCycle_succ_iff s v _).mpr (lam_spec pr s v).1
  · intro u hu
    exact (lam_spec pr s v).2 u ((onCycle_succ_iff s v u).mp hu)

/-- Every vertex of a play has the play's cycle node. -/
theorem lam_iterate (hpr : Function.Injective pr) (v : V) (n : ℕ) :
    lam pr s (s^[n] v) = lam pr s v := by
  induction n with
  | zero => rfl
  | succ n ih => rw [Function.iterate_succ_apply', lam_succ hpr, ih]

theorem iterate_plen (pr : V → ℕ) (s : V → V) (v : V) : s^[plen pr s v] v = lam pr s v :=
  Nat.find_spec (exists_hit pr s v)

theorem iterate_ne_lam_of_lt_plen {v : V} {j : ℕ} (h : j < plen pr s v) :
    s^[j] v ≠ lam pr s v :=
  Nat.find_min (exists_hit pr s v) h

theorem plen_eq_zero_of_lam_eq {v : V} (h : lam pr s v = v) : plen pr s v = 0 := by
  unfold plen
  rw [Nat.find_eq_zero]
  simpa using h.symm

/-- A cycle node is its own cycle node. -/
theorem lam_lam (hpr : Function.Injective pr) (v : V) : lam pr s (lam pr s v) = lam pr s v := by
  have := lam_iterate (s := s) hpr v (plen pr s v)
  rw [iterate_plen] at this
  exact this

theorem lam_eq_of_plen_eq_zero {v : V} (h : plen pr s v = 0) : lam pr s v = v := by
  have := iterate_plen pr s v
  rw [h] at this
  simpa using this.symm

/-- Off its cycle node, a vertex is one step further from the cycle node than its successor. -/
theorem plen_succ (hpr : Function.Injective pr) {v : V} (h : lam pr s v ≠ v) :
    plen pr s v = plen pr s (s v) + 1 := by
  unfold plen
  rw [Nat.find_eq_iff]
  refine ⟨?_, ?_⟩
  · rw [Function.iterate_succ_apply]
    have := iterate_plen pr s (s v)
    rw [lam_succ hpr] at this
    exact this
  · intro j hj
    cases j with
    | zero =>
      simp only [Function.iterate_zero, id_eq]
      exact fun e => h e.symm
    | succ j =>
      rw [Function.iterate_succ_apply, ← lam_succ hpr v]
      exact iterate_ne_lam_of_lt_plen (by
        have : j < Nat.find (exists_hit pr s (s v)) := by omega
        exact this)

theorem mem_pset {v u : V} :
    u ∈ pset pr s v ↔ pr (lam pr s v) < pr u ∧ ∃ j, j < plen pr s v ∧ s^[j] v = u := by
  unfold pset
  simp only [Finset.mem_filter, Finset.mem_univ, true_and]

/-- (P3): the cycle node has the valuation `(v, ∅, 0)`. -/
theorem val_of_lam_eq {v : V} (h : lam pr s v = v) : val pr s v = ⟨v, ∅, 0⟩ := by
  have h0 := plen_eq_zero_of_lam_eq h
  unfold val
  refine Val.ext h ?_ h0
  ext u
  simp only [mem_pset, h0, Nat.not_lt_zero, false_and, exists_false, and_false,
    Finset.notMem_empty]

/-- (P1): off its cycle node, the valuation of `v` is `ext(v, ·)` of its successor's. -/
theorem val_step (hpr : Function.Injective pr) {v : V} (h : lam pr s v ≠ v) :
    val pr s v = ext pr v (val pr s (s v)) := by
  have hl := lam_succ (s := s) hpr v
  have hp := plen_succ hpr h
  unfold val ext
  dsimp only
  refine Val.ext hl.symm ?_ hp
  dsimp only
  ext u
  rw [mem_pset, hp]
  have key : (∃ j, j < plen pr s (s v) + 1 ∧ s^[j] v = u) ↔
      (u = v ∨ ∃ i, i < plen pr s (s v) ∧ s^[i] (s v) = u) := by
    constructor
    · rintro ⟨j, hj, hju⟩
      cases j with
      | zero => left; simpa using hju.symm
      | succ i =>
        right
        exact ⟨i, by omega, by rw [← Function.iterate_succ_apply]; exact hju⟩
    · rintro (rfl | ⟨i, hi, hiu⟩)
      · exact ⟨0, by omega, rfl⟩
      · exact ⟨i + 1, by omega, by rw [Function.iterate_succ_apply]; exact hiu⟩
  rw [key, hl]
  split_ifs with hv
  · rw [Finset.mem_insert, mem_pset, hl]
    constructor
    · rintro ⟨hu, rfl | hi⟩
      · exact Or.inl rfl
      · exact Or.inr ⟨hu, hi⟩
    · rintro (rfl | ⟨hu, hi⟩)
      · exact ⟨hv, Or.inl rfl⟩
      · exact ⟨hu, Or.inr hi⟩
  · rw [mem_pset, hl]
    constructor
    · rintro ⟨hu, rfl | hi⟩
      · exact absurd hu hv
      · exact ⟨hu, hi⟩
    · rintro ⟨hu, hi⟩
      exact ⟨hu, Or.inr hi⟩

/-- Off its cycle node, `v` does not occur on the play of `s v` up to the cycle node: the
prefix of a play is a simple path. -/
theorem iterate_succ_ne_self (hpr : Function.Injective pr) {v : V} (h : lam pr s v ≠ v)
    {j : ℕ} (hj : j ≤ plen pr s (s v)) : s^[j] (s v) ≠ v := by
  intro e
  -- `v` recurs with period `j + 1 ≤ plen v`, so the play is at its cycle node earlier
  have hp := plen_succ hpr h
  have hper : s^[j + 1] v = v := by rw [Function.iterate_succ_apply]; exact e
  have hlt : plen pr s v - (j + 1) < plen pr s v := by omega
  apply iterate_ne_lam_of_lt_plen hlt
  have hsplit : plen pr s v = (plen pr s v - (j + 1)) + (j + 1) := by omega
  have := iterate_plen pr s v
  rw [hsplit, Function.iterate_add_apply, hper] at this
  exact this

/-- Off its cycle node, `v` is not in the path component of its successor's valuation. -/
theorem notMem_pset_succ (hpr : Function.Injective pr) {v : V} (h : lam pr s v ≠ v) :
    v ∉ (val pr s (s v)).set := by
  intro hv
  change v ∈ pset pr s (s v) at hv
  rw [mem_pset] at hv
  obtain ⟨-, j, hj, hjv⟩ := hv
  exact iterate_succ_ne_self hpr h hj.le hjv

end

end PG
