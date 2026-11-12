/-
First lemmas towards `AbsStatement` (box 208 §10; `PGLemmas/AbsStatement.lean`).  The statement is
NOT proved here.  Proved: the Bellman facts of `d` (B1) and «d never falls» (K1′).
-/
import PGLemmas.AbsStatement
import Mathlib.Tactic

namespace PG

open Classical

noncomputable section

variable {V : Type*} {G : SPGame V} {s s' : V → V}

theorem SPGame.d_le_of_path {v : V} {k : ℕ} (h : G.PathW s v k) : G.d s v ≤ (k : ℕ∞) := by
  have hex : ∃ k, G.PathW s v k := ⟨k, h⟩
  unfold SPGame.d
  rw [dite_eq_left hex]
  exact_mod_cast Nat.find_min' hex h

theorem SPGame.path_of_d_eq {v : V} {k : ℕ} (h : G.d s v = (k : ℕ∞)) : G.PathW s v k := by
  unfold SPGame.d at h
  by_cases hex : ∃ k, G.PathW s v k
  · rw [dite_eq_left hex] at h
    have e : Nat.find hex = k := by exact_mod_cast h
    rw [← e]
    exact Nat.find_spec hex
  · rw [dite_eq_right hex] at h
    exact absurd h (ENat.top_ne_natCast k)

/-- (B1) the target has value 0. -/
theorem SPGame.d_tgt : G.d s G.tgt = 0 := by
  have h := SPGame.d_le_of_path (s := s) (SPGame.PathW.nil (G := G))
  exact le_antisymm (by exact_mod_cast h) zero_le

/-- (B1) Bellman's inequality along an edge of the graph of `s`. -/
theorem SPGame.d_le_edge {v u : V} (he : G.edge s v u) :
    G.d s v ≤ (G.w v u : ℕ∞) + G.d s u := by
  by_cases htop : G.d s u = ⊤
  · rw [htop]; simp
  · obtain ⟨k, hk⟩ := ENat.ne_top_iff_exists.mp htop
    have hp := SPGame.path_of_d_eq hk.symm
    have := SPGame.d_le_of_path (SPGame.PathW.cons he hp)
    rw [← hk]
    exact_mod_cast this

/-- (B1) off the target, a finite value is attained along some edge. -/
theorem SPGame.exists_edge_eq {v : V} (hv : v ≠ G.tgt) {k : ℕ} (h : G.d s v = (k : ℕ∞)) :
    ∃ u, G.edge s v u ∧ G.d s v = (G.w v u : ℕ∞) + G.d s u := by
  have hp := SPGame.path_of_d_eq h
  cases hp with
  | nil => exact absurd rfl hv
  | @cons _ u k' he hp' =>
    refine ⟨u, he, le_antisymm (SPGame.d_le_edge he) ?_⟩
    rw [h]
    have h1 := SPGame.d_le_of_path hp'
    calc (G.w v u : ℕ∞) + G.d s u ≤ (G.w v u : ℕ∞) + (k' : ℕ∞) := by gcongr
      _ = ((G.w v u + k' : ℕ) : ℕ∞) := by push_cast; rfl

/-- (B1) a Max vertex has the value of its edge. -/
theorem SPGame.d_max (htgt : G.tgt ∉ G.Max) {z : V} (hz : z ∈ G.Max) (hs : s z ∈ G.E z) :
    G.d s z = (G.w z (s z) : ℕ∞) + G.d s (s z) := by
  have he : G.edge s z (s z) := ⟨hs, fun _ => rfl⟩
  refine le_antisymm (SPGame.d_le_edge he) ?_
  by_cases htop : G.d s z = ⊤
  · rw [htop]; exact le_top
  · obtain ⟨k, hk⟩ := ENat.ne_top_iff_exists.mp htop
    obtain ⟨u, hu, hd⟩ := SPGame.exists_edge_eq (fun e => htgt (e ▸ hz)) hk.symm
    rw [hu.2 hz] at hd
    exact le_of_eq hd.symm

/-- (K1′) a Howard step lowers no value. -/
theorem SPGame.d_le_step (htgt : G.tgt ∉ G.Max) (hs : ∀ z ∈ G.Max, s z ∈ G.E z)
    (hhow : ∀ z ∈ G.Max, G.HowardAt s s' z) (v : V) : G.d s v ≤ G.d s' v := by
  have key : ∀ v k, G.PathW s' v k → G.d s v ≤ (k : ℕ∞) := by
    intro v k hp
    induction hp with
    | nil => rw [SPGame.d_tgt]; exact zero_le
    | @cons v u k' he _ ih =>
      have hstep : G.d s v ≤ (G.w v u : ℕ∞) + G.d s u := by
        by_cases hv : v ∈ G.Max
        · rw [he.2 hv, SPGame.d_max htgt hv (hs v hv)]
          exact (hhow v hv).2.1 (s v) (hs v hv)
        · exact SPGame.d_le_edge ⟨he.1, fun h => absurd h hv⟩
      calc G.d s v ≤ (G.w v u : ℕ∞) + G.d s u := hstep
        _ ≤ (G.w v u : ℕ∞) + (k' : ℕ∞) := by gcongr
        _ = ((G.w v u + k' : ℕ) : ℕ∞) := by push_cast; rfl
  by_cases htop : G.d s' v = ⊤
  · rw [htop]; exact le_top
  · obtain ⟨k, hk⟩ := ENat.ne_top_iff_exists.mp htop
    rw [← hk]
    exact key v k (SPGame.path_of_d_eq hk.symm)

end

end PG
