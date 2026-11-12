/-
The dual of premise (M): for the minimising player.  Shifting every priority by one keeps the
relevance order and swaps the parities, so it keeps every node valuation and reverses the order
on node valuations (`val_shift`, `Val.lt_shift`).  `val_mono` for the shifted priorities is then
`val_mono_dual`: if every vertex keeps its successor or moves to one of strictly SMALLER value,
no value rises.
-/
import PGLemmas.Mono

namespace PG

open Classical
open scoped symmDiff

noncomputable section

variable {V : Type*} {pr : V → ℕ}

/-- the priorities shifted by one -/
def shift (pr : V → ℕ) : V → ℕ := fun v => pr v + 1

theorem shift_injective (hpr : Function.Injective pr) : Function.Injective (shift pr) :=
  fun _ _ h => hpr (Nat.add_right_cancel h)

theorem even_shift (v : V) : Even (shift pr v) ↔ ¬ Even (pr v) := by
  unfold shift
  rw [Nat.even_add_one]

/-- The shift reverses the reward order. -/
theorem rew_shift_lt (u v : V) : rew (shift pr) u < rew (shift pr) v ↔ rew pr v < rew pr u := by
  unfold rew
  simp only [even_shift]
  unfold shift
  by_cases hu : Even (pr u) <;> by_cases hv : Even (pr v) <;>
    simp only [hu, hv, not_true_eq_false, not_false_eq_true, ite_true, ite_false] <;>
    push_cast
  · omega
  · have : pr v ≠ 0 := fun h => hv (h ▸ ⟨0, rfl⟩)
    omega
  · have : pr u ≠ 0 := fun h => hu (h ▸ ⟨0, rfl⟩)
    omega
  · omega

/-- The shift reverses the order on path components. -/
theorem setLt_shift (M N : Finset V) : setLt (shift pr) M N ↔ setLt pr N M := by
  unfold setLt
  constructor
  · rintro ⟨d, hd, hmax, hside⟩
    refine ⟨d, by rw [symmDiff_comm]; exact hd, ?_, ?_⟩
    · intro x hx
      rw [symmDiff_comm] at hx
      have := hmax x hx
      unfold shift at this
      omega
    · simp only [even_shift] at hside
      tauto
  · rintro ⟨d, hd, hmax, hside⟩
    refine ⟨d, by rw [symmDiff_comm]; exact hd, ?_, ?_⟩
    · intro x hx
      rw [symmDiff_comm] at hx
      have := hmax x hx
      unfold shift
      omega
    · simp only [even_shift]
      tauto

/-- The shift reverses the order on node valuations. -/
theorem Val.lt_shift (x y : Val V) : Val.lt (shift pr) x y ↔ Val.lt pr y x := by
  unfold Val.lt
  rw [rew_shift_lt, setLt_shift]
  simp only [even_shift]
  constructor
  · rintro (h | ⟨e, h⟩ | ⟨e, es, hl, hp⟩ | ⟨e, es, hl, hp⟩)
    · exact Or.inl h
    · exact Or.inr (Or.inl ⟨e.symm, h⟩)
    · exact Or.inr (Or.inr (Or.inr ⟨e.symm, es.symm, hl, by rw [← e]; exact not_not.mp hp⟩))
    · exact Or.inr (Or.inr (Or.inl ⟨e.symm, es.symm, hl, by rw [← e]; exact hp⟩))
  · rintro (h | ⟨e, h⟩ | ⟨e, es, hl, hp⟩ | ⟨e, es, hl, hp⟩)
    · exact Or.inl h
    · exact Or.inr (Or.inl ⟨e.symm, h⟩)
    · exact Or.inr (Or.inr (Or.inr ⟨e.symm, es.symm, hl, by rw [← e]; exact hp⟩))
    · exact Or.inr (Or.inr (Or.inl ⟨e.symm, es.symm, hl, by rw [← e]; exact not_not.mpr hp⟩))

theorem Val.le_shift (x y : Val V) : Val.le (shift pr) x y ↔ Val.le pr y x := by
  unfold Val.le
  rw [Val.lt_shift]
  constructor
  · rintro (h | h)
    · exact Or.inl h
    · exact Or.inr h.symm
  · rintro (h | h)
    · exact Or.inl h
    · exact Or.inr h.symm

variable [Fintype V]

/-- The shift keeps every cycle node. -/
theorem lam_shift (hpr : Function.Injective pr) (s : V → V) (v : V) :
    lam (shift pr) s v = lam pr s v := by
  apply lam_unique (shift_injective hpr) (lam_spec pr s v).1
  intro u hu
  have := (lam_spec pr s v).2 u hu
  unfold shift
  omega

/-- The shift keeps every node valuation. -/
theorem val_shift (hpr : Function.Injective pr) (s : V → V) (v : V) :
    val (shift pr) s v = val pr s v := by
  have hl := lam_shift hpr s v
  have hp : plen (shift pr) s v = plen pr s v := by
    unfold plen
    congr 1
    · funext n; rw [hl]
  unfold val
  refine Val.ext hl ?_ hp
  ext u
  show u ∈ pset (shift pr) s v ↔ u ∈ pset pr s v
  rw [mem_pset, mem_pset, hl, hp]
  unfold shift
  constructor
  · rintro ⟨h1, h2⟩; exact ⟨by omega, h2⟩
  · rintro ⟨h1, h2⟩; exact ⟨by omega, h2⟩

/-- **Premise (M), dual form**: if every vertex keeps its successor or moves to one of strictly
smaller value, no value rises. -/
theorem val_mono_dual (hpr : Function.Injective pr) (s s' : V → V)
    (himp : ∀ v, s' v = s v ∨ Val.lt pr (val pr s (s' v)) (val pr s (s v))) :
    ∀ v, Val.le pr (val pr s' v) (val pr s v) := by
  intro v
  have h := val_mono (shift pr) (shift_injective hpr) s s' (by
    intro u
    rcases himp u with e | hlt
    · exact Or.inl e
    · right
      rw [val_shift hpr, val_shift hpr, Val.lt_shift]
      exact hlt) v
  rw [val_shift hpr, val_shift hpr, Val.le_shift] at h
  exact h

end

end PG
