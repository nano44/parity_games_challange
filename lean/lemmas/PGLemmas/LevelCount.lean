/-
Proof of `LevelCountStatement` (`PGLemmas/LevelCountStatement.lean`; box 208 §3 (L1), §4 (C1), (C2)).

* `lc_front_le`     the lowest lagging class never falls (first half of (L1));
* `lc_front_of_eq`  where it stays, the front only shrinks (second half of (L1));
* `lc_fiber`        the states with one value of (lowest lagging class, |front|) form a run of
                    consecutive stalls, so there are at most L + 1 of them ((C2));
* `level_count`     at most |M|·F values, each on at most L + 1 states.
-/
import PGLemmas.LevelCountStatement
import Mathlib.Tactic

namespace PG

open Classical

noncomputable section

variable {V : Type*} {α : Type*} [LinearOrder α] {c : ℕ → V → α} {a b : ℕ}

/-- (K1) over several steps. -/
theorem lc_mono (hK : ∀ t, a ≤ t → t < b → ∀ v, c t v ≤ c (t + 1) v) {t t' : ℕ} (hat : a ≤ t)
    (h : t ≤ t') (ht' : t' ≤ b) (v : V) : c t v ≤ c t' v := by
  obtain ⟨k, rfl⟩ := Nat.exists_eq_add_of_le h
  induction k with
  | zero => exact le_rfl
  | succ k ih =>
    exact (ih (by omega) (by omega)).trans (hK (t + k) (by omega) (by omega) v)

/-- LAG only shrinks. -/
theorem lc_lag_of_lag (hK : ∀ t, a ≤ t → t < b → ∀ v, c t v ≤ c (t + 1) v) {t t' : ℕ}
    (hat : a ≤ t) (h : t ≤ t') (ht' : t' ≤ b) {v : V} (hv : c t' v ≠ c b v) : c t v ≠ c b v :=
  ne_of_lt (lt_of_le_of_lt (lc_mono hK hat h ht' v)
    (lt_of_le_of_ne (lc_mono hK (hat.trans h) ht' le_rfl v) hv))

theorem lc_front_exists [Fintype V] {t : ℕ} (h : ∃ v, c t v ≠ c b v) :
    ∃ v, FrontAt c b t v := by
  obtain ⟨z, hz⟩ := h
  have hne : (Finset.univ.filter (fun v => c t v ≠ c b v)).Nonempty :=
    ⟨z, Finset.mem_filter.mpr ⟨Finset.mem_univ _, hz⟩⟩
  obtain ⟨v, hv, hmin⟩ := Finset.exists_min_image _ (c t) hne
  exact ⟨v, (Finset.mem_filter.mp hv).2,
    fun u hu => hmin u (Finset.mem_filter.mpr ⟨Finset.mem_univ _, hu⟩)⟩

/-- Two vertices of one front have one class. -/
theorem FrontAt.val_eq {t : ℕ} {x y : V} (hx : FrontAt c b t x) (hy : FrontAt c b t y) :
    c t x = c t y :=
  le_antisymm (hx.2 y hy.1) (hy.2 x hx.1)

/-- (L1), first half: the lowest lagging class never falls. -/
theorem lc_front_le (hK : ∀ t, a ≤ t → t < b → ∀ v, c t v ≤ c (t + 1) v) {t t' : ℕ}
    (hat : a ≤ t) (h : t ≤ t') (ht' : t' ≤ b) {x y : V} (hx : FrontAt c b t x)
    (hy : FrontAt c b t' y) : c t x ≤ c t' y :=
  (hx.2 y (lc_lag_of_lag hK hat h ht' hy.1)).trans (lc_mono hK hat h ht' y)

/-- (L1), second half: where the lowest lagging class stays, a later front lies in the earlier. -/
theorem lc_front_of_eq (hK : ∀ t, a ≤ t → t < b → ∀ v, c t v ≤ c (t + 1) v) {t t' : ℕ}
    (hat : a ≤ t) (h : t ≤ t') (ht' : t' ≤ b) {x y : V} (hx : FrontAt c b t x)
    (hy : FrontAt c b t' y) (e : c t' y = c t x) : FrontAt c b t y := by
  have hl := lc_lag_of_lag hK hat h ht' hy.1
  have h1 : c t y ≤ c t x := (lc_mono hK hat h ht' y).trans (le_of_eq e)
  have h2 : c t y = c t x := le_antisymm h1 (hx.2 y hl)
  exact ⟨hl, fun u hu => (le_of_eq h2).trans (hx.2 u hu)⟩

/-- The pair (lowest lagging class, size of the front) at state `t`; `fv t` is a vertex of the
front. -/
def lcKey [Fintype V] (c : ℕ → V → α) (b : ℕ) (fv : ℕ → V) (t : ℕ) : α × ℕ :=
  (c t (fv t), (Finset.univ.filter (FrontAt c b t)).card)

/-- (C2): states with one value of the pair form a run of consecutive stalls. -/
theorem lc_fiber [Fintype V] (hK : ∀ t, a ≤ t → t < b → ∀ v, c t v ≤ c (t + 1) v) {t0 : ℕ}
    (ht0b : t0 ≤ b) {fv : ℕ → V} (hfv : ∀ t, a ≤ t → t ≤ t0 → FrontAt c b t (fv t)) {L : ℕ}
    (hP : ∀ u v, a ≤ u → u ≤ v → v ≤ b → (∀ t, u ≤ t → t < v → StallAt c b t) → v - u ≤ L)
    (A : Finset ℕ) (hA : ∀ t ∈ A, a ≤ t ∧ t ≤ t0)
    (hkey : ∀ t ∈ A, ∀ t' ∈ A, lcKey c b fv t = lcKey c b fv t') : A.card ≤ L + 1 := by
  rcases A.eq_empty_or_nonempty with rfl | hne
  · simp
  obtain ⟨u, hu, hmin⟩ : ∃ u ∈ A, ∀ t ∈ A, u ≤ t :=
    ⟨A.min' hne, A.min'_mem hne, fun t ht => A.min'_le t ht⟩
  obtain ⟨v, hv, hmax⟩ : ∃ v ∈ A, ∀ t ∈ A, t ≤ v :=
    ⟨A.max' hne, A.max'_mem hne, fun t ht => A.le_max' t ht⟩
  have huv : u ≤ v := hmin v hv
  obtain ⟨hau, hut0⟩ := hA u hu
  obtain ⟨hav, hvt0⟩ := hA v hv
  have e : lcKey c b fv u = lcKey c b fv v := hkey u hu v hv
  obtain ⟨e1, e2⟩ := Prod.mk.inj e
  have hmem : ∀ t w, w ∈ Finset.univ.filter (FrontAt c b t) ↔ FrontAt c b t w := fun t w => by
    rw [Finset.mem_filter]
    exact ⟨fun h => h.2, fun h => ⟨Finset.mem_univ _, h⟩⟩
  -- where the lowest lagging class is the same, the later front lies in the earlier one
  have hsub : ∀ t t', a ≤ t → t ≤ t' → t' ≤ t0 → c t' (fv t') = c t (fv t) →
      ∀ w, FrontAt c b t' w → FrontAt c b t w := by
    intro t t' hat htt' ht't0 e w hw
    exact lc_front_of_eq hK hat htt' (ht't0.trans ht0b) (hfv t hat (htt'.trans ht't0)) hw
      ((hw.val_eq (hfv t' (hat.trans htt') ht't0)).trans e)
  -- the fronts at `u` and `v` are the same set
  have hFeq : Finset.univ.filter (FrontAt c b v) = Finset.univ.filter (FrontAt c b u) :=
    Finset.eq_of_subset_of_card_le
      (fun w hw => (hmem u w).mpr (hsub u v hau huv hvt0 e1.symm w ((hmem v w).mp hw)))
      (le_of_eq e2)
  have hstall : ∀ t, u ≤ t → t < v → StallAt c b t := by
    intro t hut htv
    have hat : a ≤ t := hau.trans hut
    have htt0 : t ≤ t0 := by omega
    have h1t0 : t + 1 ≤ t0 := by omega
    have hx := hfv t hat htt0
    have hy := hfv (t + 1) (by omega) h1t0
    have hxu := hfv u hau hut0
    have hxv := hfv v hav hvt0
    have l1 : c u (fv u) ≤ c t (fv t) := lc_front_le hK hau hut (htt0.trans ht0b) hxu hx
    have l2 : c t (fv t) ≤ c (t + 1) (fv (t + 1)) :=
      lc_front_le hK hat (Nat.le_add_right t 1) (h1t0.trans ht0b) hx hy
    have l3 : c (t + 1) (fv (t + 1)) ≤ c v (fv v) :=
      lc_front_le hK (by omega) (by omega) (hvt0.trans ht0b) hy hxv
    have et : c t (fv t) = c u (fv u) :=
      le_antisymm (l2.trans (l3.trans (le_of_eq e1.symm))) l1
    have et1 : c (t + 1) (fv (t + 1)) = c t (fv t) :=
      le_antisymm (l3.trans (le_of_eq (e1.symm.trans et.symm))) l2
    refine ⟨⟨fv t, hx.1⟩, fun w hw => ?_⟩
    -- a vertex of the front at `t` is in the front at `u`, hence at `v`, hence at `t + 1`
    have hwu : FrontAt c b u w := hsub u t hau hut htt0 et w hw
    have hwv : FrontAt c b v w := by
      have h := (hmem u w).mpr hwu
      rw [← hFeq] at h
      exact (hmem v w).mp h
    have hw1 : FrontAt c b (t + 1) w :=
      hsub (t + 1) v (by omega) (by omega) hvt0 (e1.symm.trans (et.symm.trans et1.symm)) w hwv
    exact (hw1.val_eq hy).trans (et1.trans (hx.val_eq hw))
  have hle : v - u ≤ L := hP u v hau huv (hvt0.trans ht0b) hstall
  have hsubA : A ⊆ Finset.Icc u v := fun t ht => Finset.mem_Icc.mpr ⟨hmin t ht, hmax t ht⟩
  have hc := Finset.card_le_card hsubA
  rw [Nat.card_Icc] at hc
  omega

/-- **LEVEL, the counting** (box 208 §3 (L1) + §4 (C1), (C2), abstract). -/
theorem level_count (V : Type*) [Fintype V] (α : Type*) [LinearOrder α] :
    LevelCountStatement V α := by
  intro c a b M F L hK hM hF hP t0 hat0 ht0b hlag0
  obtain ⟨v0, hv0⟩ := hlag0
  -- a vertex of the front for every state up to `t0`
  have hfv : ∀ t, ∃ x, a ≤ t → t ≤ t0 → FrontAt c b t x := by
    intro t
    by_cases h : a ≤ t ∧ t ≤ t0
    · obtain ⟨x, hx⟩ := lc_front_exists ⟨v0, lc_lag_of_lag hK h.1 h.2 ht0b hv0⟩
      exact ⟨x, fun _ _ => hx⟩
    · exact ⟨v0, fun h1 h2 => absurd ⟨h1, h2⟩ h⟩
  choose fv hfv using hfv
  have hcard : (Finset.Icc a t0).card ≤
      (L + 1) * ((Finset.Icc a t0).image (lcKey c b fv)).card := by
    apply Finset.card_le_mul_card_image
    intro φ _
    apply lc_fiber hK ht0b hfv hP
    · intro t ht
      exact Finset.mem_Icc.mp (Finset.mem_filter.mp ht).1
    · intro t ht t' ht'
      exact (Finset.mem_filter.mp ht).2.trans (Finset.mem_filter.mp ht').2.symm
  have himg : (Finset.Icc a t0).image (lcKey c b fv) ⊆ M ×ˢ Finset.Icc 1 F := by
    intro φ hφ
    obtain ⟨t, ht, rfl⟩ := Finset.mem_image.mp hφ
    obtain ⟨hat, htt0⟩ := Finset.mem_Icc.mp ht
    have hx := hfv t hat htt0
    refine Finset.mem_product.mpr ⟨hM t hat (htt0.trans ht0b) _ hx,
      Finset.mem_Icc.mpr ⟨?_, hF t hat (htt0.trans ht0b)⟩⟩
    exact Finset.card_pos.mpr ⟨fv t, Finset.mem_filter.mpr ⟨Finset.mem_univ _, hx⟩⟩
  have h2 := Finset.card_le_card himg
  rw [Finset.card_product, Nat.card_Icc, Nat.add_sub_cancel] at h2
  rw [Nat.card_Icc] at hcard
  have h3 : (L + 1) * ((Finset.Icc a t0).image (lcKey c b fv)).card ≤ (L + 1) * (M.card * F) :=
    Nat.mul_le_mul_left _ h2
  have h4 : M.card * F * (L + 1) = (L + 1) * (M.card * F) := by ring
  have h5 : t0 + 1 - a ≤ M.card * F * (L + 1) := by
    rw [h4]
    exact hcard.trans h3
  omega

end

end PG
