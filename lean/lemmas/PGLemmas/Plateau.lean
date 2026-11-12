/-
Proof of `PlateauStatement` (`PGLemmas/PlateauStatement.lean`; box 208 Addendum A2, (P5) + (P7)).

* `val_congr`   (P5)'s «Ω_s(x) is the value of x in H»: two successor maps that agree on a set
                closed under one of them give the vertices of the set the same valuation;
* `lam_of_fixed` a vertex that is its own successor is its own cycle node;
* `plateau`     the window is carried to the one-player run `s'` that copies `s` on `Y` and makes
                every vertex outside `Y` a self-loop; `lam_gap_oneplayer_noM` (LAM-GAP SHARP on a
                one-player game, no premise) bounds it.
-/
import PGLemmas.PlateauStatement
import PGLemmas.OnePlayer

namespace PG

open Classical

noncomputable section

variable {V : Type*} [Fintype V] {pr : V → ℕ}

omit [Fintype V] in
/-- Two successor maps that agree on a set closed under one of them have the same plays there. -/
theorem iterate_congr {s s' : V → V} {Y : Finset V} (hcl : ∀ x ∈ Y, s x ∈ Y)
    (hag : ∀ x ∈ Y, s' x = s x) (n : ℕ) {x : V} (hx : x ∈ Y) :
    s'^[n] x = s^[n] x ∧ s^[n] x ∈ Y := by
  induction n with
  | zero => exact ⟨rfl, hx⟩
  | succ n ih =>
    have e : s^[n + 1] x = s (s^[n] x) := Function.iterate_succ_apply' s n x
    have e' : s'^[n + 1] x = s' (s'^[n] x) := Function.iterate_succ_apply' s' n x
    rw [e, e', ih.1, hag _ ih.2]
    exact ⟨rfl, hcl _ ih.2⟩

omit [Fintype V] in
theorem onCycle_congr {s s' : V → V} {Y : Finset V} (hcl : ∀ x ∈ Y, s x ∈ Y)
    (hag : ∀ x ∈ Y, s' x = s x) {x : V} (hx : x ∈ Y) (u : V) :
    OnCycle s' x u ↔ OnCycle s x u := by
  constructor
  · rintro ⟨⟨n, hn⟩, p, hp0, hp⟩
    have hn' : s^[n] x = u := by rw [← (iterate_congr hcl hag n hx).1]; exact hn
    have hu : u ∈ Y := hn' ▸ (iterate_congr hcl hag n hx).2
    exact ⟨⟨n, hn'⟩, p, hp0, by rw [← (iterate_congr hcl hag p hu).1]; exact hp⟩
  · rintro ⟨⟨n, hn⟩, p, hp0, hp⟩
    have hu : u ∈ Y := hn ▸ (iterate_congr hcl hag n hx).2
    exact ⟨⟨n, by rw [(iterate_congr hcl hag n hx).1]; exact hn⟩, p, hp0,
      by rw [(iterate_congr hcl hag p hu).1]; exact hp⟩

/-- The cycle node of a vertex of a closed set depends only on the successor map on the set. -/
theorem lam_congr (hpr : Function.Injective pr) {s s' : V → V} {Y : Finset V}
    (hcl : ∀ x ∈ Y, s x ∈ Y) (hag : ∀ x ∈ Y, s' x = s x) {x : V} (hx : x ∈ Y) :
    lam pr s' x = lam pr s x := by
  apply lam_unique hpr
  · exact (onCycle_congr hcl hag hx _).mpr (lam_spec pr s x).1
  · intro u hu
    exact (lam_spec pr s x).2 u ((onCycle_congr hcl hag hx u).mp hu)

/-- (P5): the valuation of a vertex of a closed set depends only on the successor map on the
set. -/
theorem val_congr (hpr : Function.Injective pr) {s s' : V → V} {Y : Finset V}
    (hcl : ∀ x ∈ Y, s x ∈ Y) (hag : ∀ x ∈ Y, s' x = s x) {x : V} (hx : x ∈ Y) :
    val pr s' x = val pr s x := by
  have hl := lam_congr hpr hcl hag hx
  have hp : plen pr s' x = plen pr s x := by
    unfold plen
    rw [Nat.find_eq_iff]
    refine ⟨?_, fun n hn => ?_⟩
    · rw [(iterate_congr hcl hag _ hx).1, hl]
      exact iterate_plen pr s x
    · rw [(iterate_congr hcl hag n hx).1, hl]
      exact iterate_ne_lam_of_lt_plen hn
  unfold val
  refine Val.ext hl ?_ hp
  dsimp only
  ext u
  rw [mem_pset, mem_pset, hl, hp]
  constructor
  · rintro ⟨h1, j, hj, hju⟩
    exact ⟨h1, j, hj, by rw [← (iterate_congr hcl hag j hx).1]; exact hju⟩
  · rintro ⟨h1, j, hj, hju⟩
    exact ⟨h1, j, hj, by rw [(iterate_congr hcl hag j hx).1]; exact hju⟩

/-- A vertex that is its own successor is its own cycle node. -/
theorem lam_of_fixed {s : V → V} {x : V} (h : s x = x) : lam pr s x = x := by
  obtain ⟨n, hn⟩ := (lam_spec pr s x).1.1
  rw [Function.iterate_fixed h n] at hn
  exact hn.symm

/-- **PLATEAU, abstract one-player form** (box 208 Addendum A2, (P5) + (P7)). -/
theorem plateau : PlateauStatement V := by
  intro pr hpr E Y Ch hChY s a b hab hcl hfix hEY hleg hhow hlam hmov
  -- the one-player run: `s` on `Y`, a self-loop at every vertex outside `Y`
  have hs' : ∃ s' : ℕ → V → V, (∀ t, ∀ x ∈ Y, s' t x = s t x) ∧ (∀ t x, x ∉ Y → s' t x = x) :=
    ⟨fun t x => if x ∈ Y then s t x else x, fun t x hx => ite_eq_left hx,
      fun t x hx => ite_eq_right hx⟩
  obtain ⟨s', hin, hout⟩ := hs'
  -- its edges: those of `E` at `Ch`, the one successor elsewhere
  have hE' : ∃ E' : V → Finset V, (∀ x ∈ Ch, E' x = E x) ∧ (∀ x, x ∉ Ch → E' x = {s' a x}) :=
    ⟨fun x => if x ∈ Ch then E x else {s' a x}, fun x hx => ite_eq_left hx,
      fun x hx => ite_eq_right hx⟩
  obtain ⟨E', hEin, hEout⟩ := hE'
  -- values on `Y` are those of the given run
  have hval : ∀ t, a ≤ t → t ≤ b → ∀ x ∈ Y, val pr (s' t) x = val pr (s t) x :=
    fun t hat htb x hx => val_congr hpr (hcl t hat htb) (hin t) hx
  refine lam_gap_oneplayer_noM pr hpr E' Ch s' a b hab ?_ ?_ ?_ ?_ ?_
  · -- one-player
    exact fun v hv => ⟨s' a v, hEout v hv⟩
  · -- every state follows the edges
    intro t hat htb v
    by_cases hv : v ∈ Ch
    · rw [hEin v hv, hin t v (hChY hv)]
      exact hleg t hat htb v hv
    · rw [hEout v hv, Finset.mem_singleton]
      by_cases hvY : v ∈ Y
      · rw [hin t v hvY, hin a v hvY]
        exact hfix t hat htb v hvY hv
      · rw [hout t v hvY, hout a v hvY]
  · -- Howard steps at `Ch`
    intro t hat htb v hv
    have hvY := hChY hv
    obtain ⟨h1, h2, h3⟩ := hhow t hat htb v hv
    have hsub := hEY v hv
    have hv1 : s (t + 1) v ∈ Y := hsub h1
    have hv0 : s t v ∈ Y := hsub (hleg t hat htb.le v hv)
    unfold HowardAt
    rw [hEin v hv, hin (t + 1) v hvY, hin t v hvY, hval t hat htb.le _ hv1,
      hval t hat htb.le _ hv0]
    refine ⟨h1, fun w hw => ?_, fun hk => h3 ⟨hk.1, fun w hw => ?_⟩⟩
    · rw [hval t hat htb.le w (hsub hw)]
      exact h2 w hw
    · have := hk.2 w hw
      rw [hval t hat htb.le w (hsub hw)] at this
      exact this
  · -- no cycle node changes
    intro t hat htb v
    by_cases hvY : v ∈ Y
    · rw [lam_congr hpr (hcl t hat htb) (hin t) hvY,
        lam_congr hpr (hcl a le_rfl hab) (hin a) hvY]
      exact hlam t hat htb v hvY
    · rw [lam_of_fixed (hout t v hvY), lam_of_fixed (hout a v hvY)]
  · -- every step changes the state
    intro t hat htb e
    obtain ⟨x, hx, hne⟩ := hmov t hat htb
    apply hne
    have := congrFun e x
    rwa [hin (t + 1) x (hChY hx), hin t x (hChY hx)] at this

end

end PG
