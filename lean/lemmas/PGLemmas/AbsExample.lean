/-
The hypotheses of `AbsStatement` (`PGLemmas/AbsStatement.lean`) are satisfiable with `T = 1`:
a shortest-path game on three vertices and a Howard run of one step.

Vertices: `0` (Max), `1` (Min), `2` (the target).  Edges and weights: `0 → 1` (0), `0 → 2` (1),
`1 → 2` (3).  Start: Max plays `0 → 2`, so d(0) = 1.  Howard moves it to `0 → 1`, where
w + d = 0 + 3; then d(0) = 3 and the run stops.

`hyps` proves every hypothesis of `AbsStatement` for this run; `d_start`, `d_end` give d(0)
before and after the step.
-/
import PGLemmas.Abs

namespace PG

namespace AbsExample

/-- The game. -/
def G : SPGame (Fin 3) where
  E := fun v => if v = 0 then {1, 2} else if v = 1 then {2} else ∅
  w := fun v u => if v = 0 then (if u = 1 then 0 else 1) else 3
  Max := {0}
  tgt := 2

/-- The run `s 0, s 1`: Max's vertex `0` goes to `2`, then to `1`; a Min vertex carries no choice. -/
def s : ℕ → Fin 3 → Fin 3 := fun t v => if v = 0 then (if t = 0 then 2 else 1) else v

theorem d2 (σ : Fin 3 → Fin 3) : G.d σ 2 = 0 := SPGame.d_tgt (G := G)

theorem d1 (σ : Fin 3 → Fin 3) : G.d σ 1 = 3 := by
  have he : G.edge σ 1 2 := ⟨by decide, fun h => absurd h (by decide)⟩
  have hle : G.d σ 1 ≤ (G.w 1 2 : ℕ∞) + G.d σ 2 := SPGame.d_le_edge he
  have hfin : G.d σ 1 ≠ ⊤ := by
    intro e
    rw [e, d2] at hle
    exact absurd hle (by simp)
  obtain ⟨k, hk⟩ := ENat.ne_top_iff_exists.mp hfin
  obtain ⟨u, hu, hd⟩ := SPGame.exists_edge_eq (by decide : (1 : Fin 3) ≠ G.tgt) hk.symm
  have key : ∀ u : Fin 3, u ∈ G.E 1 → u = 2 := by decide
  rw [key u hu.1, d2] at hd
  rw [hd]
  have hw : G.w 1 2 = 3 := rfl
  rw [hw]
  norm_num

theorem d_start : G.d (s 0) 0 = 1 := by
  have h := SPGame.d_max (G := G) (s := s 0) (by decide) (by decide : (0 : Fin 3) ∈ G.Max)
    (by decide)
  have e : s 0 0 = 2 := rfl
  have hw : G.w 0 2 = 1 := rfl
  rw [e, d2, hw] at h
  rw [h]
  norm_num

theorem d_end : G.d (s 1) 0 = 3 := by
  have h := SPGame.d_max (G := G) (s := s 1) (by decide) (by decide : (0 : Fin 3) ∈ G.Max)
    (by decide)
  have e : s 1 0 = 1 := rfl
  have hw : G.w 0 1 = 0 := rfl
  rw [e, d1, hw] at h
  rw [h]
  norm_num

/-- Every hypothesis of `AbsStatement` holds for the game `G` and the run `s 0, s 1` (`T = 1`). -/
theorem hyps :
    G.NoZeroCycle ∧ G.tgt ∉ G.Max ∧
    (∀ t, t ≤ 1 → ∀ z ∈ G.Max, s t z ∈ G.E z) ∧
    (∀ t, t ≤ 1 → ∀ v, v ∉ G.Max → s t v = s 0 v) ∧
    (∀ t, t < 1 → ∀ z ∈ G.Max, G.HowardAt (s t) (s (t + 1)) z) ∧
    (∀ t, t < 1 → s (t + 1) ≠ s t) := by
  have hmax : ∀ z : Fin 3, z ∈ G.Max → z = 0 := by decide
  refine ⟨?_, by decide, ?_, ?_, ?_, ?_⟩
  · -- the only edge of weight 0 is `0 → 1`: weight-0 edges go up
    have hup : ∀ a b : Fin 3, b ∈ G.E a ∧ G.w a b = 0 → a < b := by decide
    have hlt : ∀ a b : Fin 3,
        Relation.TransGen (fun a b => b ∈ G.E a ∧ G.w a b = 0) a b → a < b := by
      intro a b h
      induction h with
      | single h => exact hup _ _ h
      | tail _ h ih => exact lt_trans ih (hup _ _ h)
    exact fun v h => lt_irrefl v (hlt v v h)
  · intro t ht z hz
    rw [hmax z hz]
    have ht' : t = 0 ∨ t = 1 := by omega
    rcases ht' with rfl | rfl <;> decide
  · intro t _ v hv
    have hv0 : v ≠ 0 := fun e => hv (e ▸ (by decide : (0 : Fin 3) ∈ G.Max))
    unfold s
    rw [ite_eq_right hv0, ite_eq_right hv0]
  · intro t ht z hz
    rw [hmax z hz]
    obtain rfl : t = 0 := by omega
    have e1 : s (0 + 1) 0 = 1 := rfl
    have e0 : s 0 0 = 2 := rfl
    have w01 : G.w 0 1 = 0 := rfl
    have w02 : G.w 0 2 = 1 := rfl
    have hE : ∀ y : Fin 3, y ∈ G.E 0 → y = 1 ∨ y = 2 := by decide
    unfold SPGame.HowardAt
    rw [e1, e0]
    refine ⟨by decide, fun y hy => ?_, fun hk => ?_⟩
    · rcases hE y hy with rfl | rfl
      · exact le_rfl
      · rw [d1, d2, w01, w02]
        norm_num
    · exfalso
      have h := hk.2 1 (by decide)
      rw [d1, d2, w01, w02] at h
      norm_num at h
  · intro t ht e
    obtain rfl : t = 0 := by omega
    have h := congrFun e 0
    revert h
    decide

end AbsExample

end PG
