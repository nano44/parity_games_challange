/-
One-player games with no premise: (M) is `val_mono` (`PGLemmas/Mono.lean`), so
* `lam_gap_oneplayer_noM`  LAM-GAP SHARP in box 101 §2's one-player setting, premise-free;
* `howard_run_oneplayer`   Howard's algorithm with VJ valuations on a one-player game makes at
                           most n(n−1) + (n(n−1)+1)·|Ch| steps.
-/
import PGLemmas.Mono
import PGLemmas.Corollaries
import PGLemmas.Counting

namespace PG

open Classical

noncomputable section

variable {V : Type*} [Fintype V]

/-- In a one-player game a Howard step between two states that follow the edges consists of
improving switches. -/
theorem howard_improves {pr : V → ℕ} (hpr : Function.Injective pr) {E : V → Finset V}
    {Ch : Finset V} {σ σ' : V → V} (hone : ∀ v, v ∉ Ch → ∃ u, E v = {u})
    (hσ : ∀ v, σ v ∈ E v) (hσ' : ∀ v, σ' v ∈ E v)
    (hhow : ∀ v ∈ Ch, HowardAt pr E σ σ' v) : Improves pr σ σ' := by
  intro v
  by_cases hv : v ∈ Ch
  · obtain ⟨-, hbest, hkeep⟩ := hhow v hv
    by_cases hsame : σ' v = σ v
    · exact Or.inl hsame
    · right
      -- the old successor was not best, the new one is
      have hnot : ∃ w ∈ E v, ¬ Val.le pr (val pr σ w) (val pr σ (σ v)) := by
        by_contra h
        exact hsame (hkeep ⟨hσ v, fun w hw => by
          by_contra hw'
          exact h ⟨w, hw, hw'⟩⟩)
      obtain ⟨w, hw, hwnot⟩ := hnot
      exact Val.lt_of_lt_of_le hpr (Val.lt_of_not_le hpr hwnot) (hbest w hw)
  · left
    obtain ⟨u, hu⟩ := hone v hv
    have h1 := hσ v
    have h2 := hσ' v
    rw [hu, Finset.mem_singleton] at h1 h2
    rw [h1, h2]

/-- **LAM-GAP, SHARP form, on a one-player game, with no premise (M).** -/
theorem lam_gap_oneplayer_noM : LamGapOnePlayerNoMStatement V := by
  intro pr hpr E Ch s a b hab hone hedge hhow hlam hmoves
  refine lam_gap_oneplayer pr hpr E Ch s a b hab hone hedge hhow ?_ hlam hmoves
  intro t hat htb v
  exact val_mono pr hpr (s t) (s (t + 1))
    (howard_improves hpr hone (hedge t hat (by omega)) (hedge (t + 1) (by omega) (by omega))
      (hhow t hat htb)) v

/-- **Howard's algorithm on a one-player game**: at most `n(n−1) + (n(n−1)+1)·|Ch|` steps. -/
theorem howard_run_oneplayer : HowardRunOnePlayerStatement V := by
  intro pr hpr E Ch s T hone hedge hhow hmoves
  refine howard_run pr hpr E Ch s T ?_ hhow ?_ hmoves
  · intro t ht v hv
    obtain ⟨u, hu⟩ := hone v hv
    have h1 := hedge t ht v
    have h2 := hedge 0 (by omega) v
    rw [hu, Finset.mem_singleton] at h1 h2
    rw [h1, h2]
  · intro t ht v
    exact val_mono pr hpr (s t) (s (t + 1))
      (howard_improves hpr hone (hedge t (by omega)) (hedge (t + 1) (by omega)) (hhow t ht)) v

end

end PG
