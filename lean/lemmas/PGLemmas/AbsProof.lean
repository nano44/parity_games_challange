/-
Proof of `AbsStatement` (box 208 §10, Statement ABS; `PGLemmas/AbsStatement.lean`).

The proof follows §10 («the same five facts, then §3 word for word»), with reference state the
last state `T`:
* (K1′) `SPGame.Run.mono`         d never falls along the run (`SPGame.d_le_step`, Abs.lean);
* (K5′) `SPGame.Run.k5`           after a step, d(z) ≥ w(z, y) + (old d)(y) for every edge of a Max z;
* (A)   `SPGame.Run.exists_rise`  every step of the run raises d somewhere, so some vertex lags;
* (F)   `SPGame.front_zero_edge`  from a vertex of the front, an edge that attains its value and
                                  leads to a lagging vertex has weight 0 and ends in the front;
* (L3)  `SPGame.Run.front_level`  the lowest lagging value is w(z, y) + d_T(y) for an edge of a Max
                                  vertex: one value per such edge;
* (L4)  `SPGame.Run.front_rises`  no stall: every step raises d at a vertex of the front;
* (L1)  `SPGame.Run.phi_step`     Φ = (lowest lagging value, −|front|) rises at every step;
* (C)   `abs_statement`           t ↦ (lowest lagging value, |front|) is injective: the bound.
The cycle argument of (L3) and (L4) is `SPGame.no_closed`: a non-empty set in which every vertex
has a weight-0 edge into the set gives a closed walk of weight 0, which `NoZeroCycle` excludes.

Clause (2) is proved for EVERY step `t < T`, the last one included: in this encoding every step of
the run changes the state (hypothesis `moves`), and a step that changes the state raises `d`
somewhere (`exists_rise`), so the front is not empty at any `t < T`.
-/
import PGLemmas.Abs

namespace PG

open Classical

noncomputable section

variable {V : Type*} {G : SPGame V} {s : ℕ → V → V} {T : ℕ}

/-- The hypotheses of `AbsStatement` on a run `s 0, …, s T`, as one structure. -/
structure SPGame.Run (G : SPGame V) (s : ℕ → V → V) (T : ℕ) : Prop where
  nz : G.NoZeroCycle
  tgt : G.tgt ∉ G.Max
  legal : ∀ t, t ≤ T → ∀ z ∈ G.Max, s t z ∈ G.E z
  fixed : ∀ t, t ≤ T → ∀ v, v ∉ G.Max → s t v = s 0 v
  howard : ∀ t, t < T → ∀ z ∈ G.Max, G.HowardAt (s t) (s (t + 1)) z
  moves : ∀ t, t < T → s (t + 1) ≠ s t

theorem SPGame.Run.mono_add (R : G.Run s T) (t k : ℕ) (h : t + k ≤ T) (v : V) :
    G.d (s t) v ≤ G.d (s (t + k)) v := by
  induction k with
  | zero => exact le_rfl
  | succ k ih =>
    exact (ih (by omega)).trans
      (SPGame.d_le_step R.tgt (R.legal (t + k) (by omega)) (R.howard (t + k) (by omega)) v)

/-- (K1′) along the run: `d` never falls. -/
theorem SPGame.Run.mono (R : G.Run s T) {t t' : ℕ} (h : t ≤ t') (ht' : t' ≤ T) (v : V) :
    G.d (s t) v ≤ G.d (s t') v := by
  obtain ⟨k, rfl⟩ := Nat.exists_eq_add_of_le h
  exact R.mono_add t k ht' v

/-- (K5′) after a step, the value of a Max vertex is at least `w(z, y) + (old d)(y)` for every one
of its edges. -/
theorem SPGame.Run.k5 (R : G.Run s T) {t : ℕ} (ht : t < T) {z y : V} (hz : z ∈ G.Max)
    (hy : y ∈ G.E z) : (G.w z y : ℕ∞) + G.d (s t) y ≤ G.d (s (t + 1)) z := by
  rw [SPGame.d_max R.tgt hz (R.legal (t + 1) (by omega) z hz)]
  calc (G.w z y : ℕ∞) + G.d (s t) y
      ≤ (G.w z (s (t + 1) z) : ℕ∞) + G.d (s t) (s (t + 1) z) := (R.howard t ht z hz).2.1 y hy
    _ ≤ (G.w z (s (t + 1) z) : ℕ∞) + G.d (s (t + 1)) (s (t + 1) z) := by
        gcongr
        exact R.mono (Nat.le_add_right t 1) (by omega) _

/-- (A) every step of the run raises the value of some vertex. -/
theorem SPGame.Run.exists_rise (R : G.Run s T) {t : ℕ} (ht : t < T) :
    ∃ z, G.d (s t) z < G.d (s (t + 1)) z := by
  have hne := R.moves t ht
  obtain ⟨z, hz⟩ : ∃ z, s (t + 1) z ≠ s t z := by
    by_contra hcon
    exact hne (funext fun z => by_contra fun h => hcon ⟨z, h⟩)
  have hzM : z ∈ G.Max := by
    by_contra hzM
    exact hz ((R.fixed (t + 1) (by omega) z hzM).trans (R.fixed t (by omega) z hzM).symm)
  have hleg := R.legal t (by omega) z hzM
  have hkeep := (R.howard t ht z hzM).2.2
  have hex : ∃ y ∈ G.E z,
      (G.w z (s t z) : ℕ∞) + G.d (s t) (s t z) < (G.w z y : ℕ∞) + G.d (s t) y := by
    by_contra hcon
    exact hz (hkeep ⟨hleg, fun y hy => not_lt.mp fun h => hcon ⟨y, hy, h⟩⟩)
  obtain ⟨y, hy, hlt⟩ := hex
  refine ⟨z, ?_⟩
  rw [SPGame.d_max R.tgt hzM hleg]
  exact lt_of_lt_of_le hlt (R.k5 ht hzM hy)

/-- `v` is in the FRONT at state `t`, with reference the last state `T`: it lags
(`d_t(v) ≠ d_T(v)`) and has the lowest lagging value. -/
def SPGame.Front (G : SPGame V) (s : ℕ → V → V) (T t : ℕ) (v : V) : Prop :=
  G.d (s t) v ≠ G.d (s T) v ∧ ∀ u, G.d (s t) u ≠ G.d (s T) u → G.d (s t) v ≤ G.d (s t) u

/-- (F) from a vertex `v` of the front, an edge `v → u` with `w(v, u) + d_t(u) ≤ d_t(v)` to a
lagging vertex `u` has weight 0, and `u` is in the front. -/
theorem SPGame.front_zero_edge {t : ℕ} {v u : V} (hv : G.Front s T t v)
    (hfin : G.d (s t) v ≠ ⊤) (hu : G.d (s t) u ≠ G.d (s T) u)
    (hle : (G.w v u : ℕ∞) + G.d (s t) u ≤ G.d (s t) v) :
    G.w v u = 0 ∧ G.Front s T t u := by
  obtain ⟨k, hk⟩ := ENat.ne_top_iff_exists.mp hfin
  have h1 : G.d (s t) v ≤ G.d (s t) u := hv.2 u hu
  have h2 : G.d (s t) u ≤ G.d (s t) v := le_trans le_add_self hle
  have h3 : G.d (s t) u = G.d (s t) v := le_antisymm h2 h1
  have hw : G.w v u = 0 := by
    rw [h3, ← hk] at hle
    have : G.w v u + k ≤ k := by exact_mod_cast hle
    omega
  exact ⟨hw, hu, fun u' hu' => h3 ▸ hv.2 u' hu'⟩

/-- A front vertex of Min's has a weight-0 edge into the front (no stall needed): a best edge to
a non-lagging vertex would pin its value by Bellman's inequality at `T`. -/
theorem SPGame.Run.front_min (R : G.Run s T) {t : ℕ} (ht : t ≤ T) {o : V} (ho : o ∉ G.Max)
    (hf : G.Front s T t o) : ∃ u, G.Front s T t u ∧ u ∈ G.E o ∧ G.w o u = 0 := by
  have hlt : G.d (s t) o < G.d (s T) o := lt_of_le_of_ne (R.mono ht le_rfl o) hf.1
  have hfin : G.d (s t) o ≠ ⊤ := ne_top_of_lt hlt
  have hne : o ≠ G.tgt := by
    intro e
    apply hf.1
    rw [e, SPGame.d_tgt, SPGame.d_tgt]
  obtain ⟨k, hk⟩ := ENat.ne_top_iff_exists.mp hfin
  obtain ⟨u, hu, hd⟩ := SPGame.exists_edge_eq hne hk.symm
  have hulag : G.d (s t) u ≠ G.d (s T) u := by
    intro e
    have hT : G.d (s T) o ≤ (G.w o u : ℕ∞) + G.d (s T) u :=
      SPGame.d_le_edge ⟨hu.1, fun h => absurd h ho⟩
    rw [← e, ← hd] at hT
    exact absurd hlt (not_lt.mpr hT)
  obtain ⟨hw, hfu⟩ := SPGame.front_zero_edge hf hfin hulag (le_of_eq hd.symm)
  exact ⟨u, hfu, hu.1, hw⟩

/-- A front vertex of Max's whose current edge leads to a lagging vertex has that edge of
weight 0 into the front. -/
theorem SPGame.Run.front_max_lag (R : G.Run s T) {t : ℕ} (ht : t ≤ T) {z : V} (hz : z ∈ G.Max)
    (hf : G.Front s T t z) (hlag : G.d (s t) (s t z) ≠ G.d (s T) (s t z)) :
    G.w z (s t z) = 0 ∧ G.Front s T t (s t z) := by
  have hlt : G.d (s t) z < G.d (s T) z := lt_of_le_of_ne (R.mono ht le_rfl z) hf.1
  exact SPGame.front_zero_edge hf (ne_top_of_lt hlt) hlag
    (le_of_eq (SPGame.d_max R.tgt hz (R.legal t ht z hz)).symm)

/-- A front vertex of Max's that the step `t → t + 1` does not raise has its edge at `T` of
weight 0 into the front: Howard would otherwise have lifted it (K5′). -/
theorem SPGame.Run.front_max_stall (R : G.Run s T) {t : ℕ} (ht : t < T) {z : V} (hz : z ∈ G.Max)
    (hf : G.Front s T t z) (hst : ¬ G.d (s t) z < G.d (s (t + 1)) z) :
    G.w z (s T z) = 0 ∧ G.Front s T t (s T z) := by
  have hy : s T z ∈ G.E z := R.legal T le_rfl z hz
  have hlt : G.d (s t) z < G.d (s T) z := lt_of_le_of_ne (R.mono ht.le le_rfl z) hf.1
  have hle : (G.w z (s T z) : ℕ∞) + G.d (s t) (s T z) ≤ G.d (s t) z :=
    (R.k5 ht hz hy).trans (not_lt.mp hst)
  have hlag : G.d (s t) (s T z) ≠ G.d (s T) (s T z) := by
    intro e
    have hle' := hle
    rw [e, ← SPGame.d_max R.tgt hz hy] at hle'
    exact absurd hlt (not_lt.mpr hle')
  exact SPGame.front_zero_edge hf (ne_top_of_lt hlt) hlag hle

/-- A non-empty set of vertices in which every vertex has a weight-0 edge into the set gives a
closed walk of weight 0. -/
theorem SPGame.no_closed [Finite V] (hnz : G.NoZeroCycle) (P : V → Prop) (hne : ∃ v, P v)
    (hstep : ∀ v, P v → ∃ u, P u ∧ u ∈ G.E v ∧ G.w v u = 0) : False := by
  obtain ⟨v0, hv0⟩ := hne
  have hV : Nonempty V := ⟨v0⟩
  choose! f hf using hstep
  have hP : ∀ n, P (f^[n] v0) := by
    intro n
    induction n with
    | zero => exact hv0
    | succ n ih =>
      have e : f^[n + 1] v0 = f (f^[n] v0) := Function.iterate_succ_apply' f n v0
      rw [e]
      exact (hf _ ih).1
  have hstep' : ∀ n, f^[n + 1] v0 ∈ G.E (f^[n] v0) ∧ G.w (f^[n] v0) (f^[n + 1] v0) = 0 := by
    intro n
    have e : f^[n + 1] v0 = f (f^[n] v0) := Function.iterate_succ_apply' f n v0
    rw [e]
    exact (hf _ (hP n)).2
  have hR : ∀ i k, Relation.TransGen (fun a b => b ∈ G.E a ∧ G.w a b = 0)
      (f^[i] v0) (f^[i + k + 1] v0) := by
    intro i k
    induction k with
    | zero => exact Relation.TransGen.single (hstep' i)
    | succ k ih => exact Relation.TransGen.tail ih (hstep' (i + k + 1))
  obtain ⟨i, j, hij, h⟩ := Finite.exists_ne_map_eq_of_infinite (fun n : ℕ => f^[n] v0)
  have h' : f^[i] v0 = f^[j] v0 := h
  rcases Nat.lt_or_gt_of_ne hij with hlt | hgt
  · obtain ⟨k, rfl⟩ : ∃ k, j = i + k + 1 := ⟨j - i - 1, by omega⟩
    have hc := hR i k
    rw [← h'] at hc
    exact hnz _ hc
  · obtain ⟨k, rfl⟩ : ∃ k, i = j + k + 1 := ⟨i - j - 1, by omega⟩
    have hc := hR j k
    rw [h'] at hc
    exact hnz _ hc

/-- Before the last state the front is not empty. -/
theorem SPGame.Run.front_exists [Fintype V] (R : G.Run s T) {t : ℕ} (ht : t < T) :
    ∃ v, G.Front s T t v := by
  obtain ⟨z, hz⟩ := R.exists_rise ht
  have hzlag : G.d (s t) z ≠ G.d (s T) z :=
    ne_of_lt (lt_of_lt_of_le hz (R.mono (by omega : t + 1 ≤ T) le_rfl z))
  have hne : (Finset.univ.filter (fun v => G.d (s t) v ≠ G.d (s T) v)).Nonempty :=
    ⟨z, Finset.mem_filter.mpr ⟨Finset.mem_univ _, hzlag⟩⟩
  obtain ⟨v, hv, hmin⟩ := Finset.exists_min_image _ (G.d (s t)) hne
  exact ⟨v, (Finset.mem_filter.mp hv).2,
    fun u hu => hmin u (Finset.mem_filter.mpr ⟨Finset.mem_univ _, hu⟩)⟩

/-- (L4) no stall: every step raises the value of a vertex of the front. -/
theorem SPGame.Run.front_rises [Fintype V] (R : G.Run s T) {t : ℕ} (ht : t < T) :
    ∃ v, G.Front s T t v ∧ G.d (s t) v < G.d (s (t + 1)) v := by
  by_contra hcon
  apply SPGame.no_closed R.nz (G.Front s T t) (R.front_exists ht)
  intro v hv
  by_cases hvM : v ∈ G.Max
  · obtain ⟨hw, hf⟩ := R.front_max_stall ht hvM hv (fun h => hcon ⟨v, hv, h⟩)
    exact ⟨_, hf, R.legal T le_rfl v hvM, hw⟩
  · exact R.front_min ht.le hvM hv

/-- (L3) the lowest lagging value is `w(z, y) + d_T(y)` for the current edge `(z, y)` of a Max
vertex `z` of the front. -/
theorem SPGame.Run.front_level [Fintype V] (R : G.Run s T) {t : ℕ} (ht : t < T) :
    ∃ z ∈ G.Max, G.Front s T t z ∧
      G.d (s t) z = (G.w z (s t z) : ℕ∞) + G.d (s T) (s t z) := by
  by_contra hcon
  apply SPGame.no_closed R.nz (G.Front s T t) (R.front_exists ht)
  intro v hv
  by_cases hvM : v ∈ G.Max
  · have hlag : G.d (s t) (s t v) ≠ G.d (s T) (s t v) := by
      intro e
      apply hcon
      refine ⟨v, hvM, hv, ?_⟩
      rw [← e]
      exact SPGame.d_max R.tgt hvM (R.legal t ht.le v hvM)
    obtain ⟨hw, hf⟩ := R.front_max_lag ht.le hvM hv hlag
    exact ⟨_, hf, R.legal t ht.le v hvM, hw⟩
  · exact R.front_min ht.le hvM hv

/-! ## The potential Φ = (lowest lagging value, −|front|) and the count -/

/-- The lowest lagging value at state `t` (`⊤` if nothing lags). -/
def SPGame.lagMin [Fintype V] (G : SPGame V) (s : ℕ → V → V) (T t : ℕ) : ℕ∞ :=
  (Finset.univ.filter (fun v => G.d (s t) v ≠ G.d (s T) v)).inf (G.d (s t))

/-- The front at state `t`, as a finite set. -/
def SPGame.frontSet [Fintype V] (G : SPGame V) (s : ℕ → V → V) (T t : ℕ) : Finset V :=
  Finset.univ.filter (G.Front s T t)

theorem SPGame.lagMin_le [Fintype V] {t : ℕ} {u : V} (hu : G.d (s t) u ≠ G.d (s T) u) :
    G.lagMin s T t ≤ G.d (s t) u :=
  Finset.inf_le (Finset.mem_filter.mpr ⟨Finset.mem_univ _, hu⟩)

theorem SPGame.Front.val_eq [Fintype V] {t : ℕ} {v : V} (hv : G.Front s T t v) :
    G.d (s t) v = G.lagMin s T t :=
  le_antisymm (Finset.le_inf fun u hu => hv.2 u (Finset.mem_filter.mp hu).2)
    (SPGame.lagMin_le hv.1)

theorem SPGame.front_of_val [Fintype V] {t : ℕ} {v : V} (hlag : G.d (s t) v ≠ G.d (s T) v)
    (h : G.d (s t) v = G.lagMin s T t) : G.Front s T t v :=
  ⟨hlag, fun _ hu => h ▸ SPGame.lagMin_le hu⟩

theorem SPGame.mem_frontSet [Fintype V] {t : ℕ} {v : V} :
    v ∈ G.frontSet s T t ↔ G.Front s T t v := by
  unfold SPGame.frontSet
  rw [Finset.mem_filter]
  exact ⟨fun h => h.2, fun h => ⟨Finset.mem_univ _, h⟩⟩

/-- (L1) Φ rises at every step between two states before the last: the lowest lagging value
does not fall, and where it stays the front loses a vertex. -/
theorem SPGame.Run.phi_step [Fintype V] (R : G.Run s T) {t : ℕ} (ht : t + 1 < T) :
    G.lagMin s T t ≤ G.lagMin s T (t + 1) ∧
    (G.lagMin s T (t + 1) = G.lagMin s T t →
      (G.frontSet s T (t + 1)).card < (G.frontSet s T t).card) := by
  have hstep : ∀ v, G.d (s t) v ≤ G.d (s (t + 1)) v :=
    fun v => R.mono (Nat.le_add_right t 1) ht.le v
  have hlag : ∀ v, G.d (s (t + 1)) v ≠ G.d (s T) v → G.d (s t) v ≠ G.d (s T) v := by
    intro v hv
    have h1 : G.d (s (t + 1)) v < G.d (s T) v := lt_of_le_of_ne (R.mono ht.le le_rfl v) hv
    exact ne_of_lt (lt_of_le_of_lt (hstep v) h1)
  have hmono : G.lagMin s T t ≤ G.lagMin s T (t + 1) := by
    obtain ⟨v', hv'⟩ := R.front_exists ht
    rw [← hv'.val_eq]
    exact (SPGame.lagMin_le (hlag v' hv'.1)).trans (hstep v')
  refine ⟨hmono, fun heq => ?_⟩
  obtain ⟨v, hv, hrise⟩ := R.front_rises (by omega : t < T)
  have hsub : G.frontSet s T (t + 1) ⊆ G.frontSet s T t := by
    intro v' hv'
    have hf' : G.Front s T (t + 1) v' := SPGame.mem_frontSet.mp hv'
    have hl := hlag v' hf'.1
    have h1 : G.d (s t) v' ≤ G.lagMin s T t := by
      rw [← heq, ← hf'.val_eq]
      exact hstep v'
    exact SPGame.mem_frontSet.mpr
      (SPGame.front_of_val hl (le_antisymm h1 (SPGame.lagMin_le hl)))
  refine Finset.card_lt_card ((Finset.ssubset_iff_of_subset hsub).mpr
    ⟨v, SPGame.mem_frontSet.mpr hv, fun hmem => ?_⟩)
  have hf' : G.Front s T (t + 1) v := SPGame.mem_frontSet.mp hmem
  have e : G.d (s (t + 1)) v = G.d (s t) v := by rw [hf'.val_eq, heq, hv.val_eq]
  rw [e] at hrise
  exact lt_irrefl _ hrise

/-- Φ at two states `t < t + k + 1` before the last. -/
theorem SPGame.Run.phi_lt [Fintype V] (R : G.Run s T) (t k : ℕ) (h : t + k + 1 < T) :
    G.lagMin s T t ≤ G.lagMin s T (t + k + 1) ∧
    (G.lagMin s T (t + k + 1) = G.lagMin s T t →
      (G.frontSet s T (t + k + 1)).card < (G.frontSet s T t).card) := by
  induction k with
  | zero => exact R.phi_step h
  | succ k ih =>
    obtain ⟨h1, h2⟩ := ih (by omega)
    obtain ⟨h3, h4⟩ := R.phi_step (t := t + k + 1) h
    refine ⟨h1.trans h3, fun heq => ?_⟩
    have h5 : G.lagMin s T (t + k + 1) ≤ G.lagMin s T t := h3.trans (le_of_eq heq)
    have e1 : G.lagMin s T (t + k + 1) = G.lagMin s T t := le_antisymm h5 h1
    have e2 : G.lagMin s T (t + k + 1 + 1) = G.lagMin s T (t + k + 1) := heq.trans e1.symm
    exact (h4 e2).trans (h2 e1)

/-- The values `w(z, y) + d_T(y)` over the edges `(z, y)` of Max's vertices. -/
def SPGame.levelVals (G : SPGame V) (s : ℕ → V → V) (T : ℕ) : Finset ℕ∞ :=
  G.Max.biUnion (fun z => (G.E z).image (fun y => (G.w z y : ℕ∞) + G.d (s T) y))

theorem SPGame.card_levelVals_le (G : SPGame V) (s : ℕ → V → V) (T : ℕ) :
    (G.levelVals s T).card ≤ ∑ z ∈ G.Max, (G.E z).card :=
  Finset.card_biUnion_le.trans (Finset.sum_le_sum fun _ _ => Finset.card_image_le)

/-- **Statement ABS** (box 208 §10), as stated in `PGLemmas/AbsStatement.lean`. -/
theorem abs_statement (V : Type*) [Fintype V] : AbsStatement V := by
  intro G hnz htgt s T hleg hfix hhow hmov
  have R : G.Run s T := ⟨hnz, htgt, hleg, hfix, hhow, hmov⟩
  refine ⟨?_, fun t ht => ?_⟩
  · -- (C) `t ↦ (lowest lagging value, |front| − 1)` is injective on the steps
    have hpos : ∀ t, t < T → 0 < (G.frontSet s T t).card := by
      intro t ht
      obtain ⟨v, hv⟩ := R.front_exists ht
      exact Finset.card_pos.mpr ⟨v, SPGame.mem_frontSet.mpr hv⟩
    have hne : ∀ t1 t2, t1 < t2 → t2 < T →
        (G.lagMin s T t1, (G.frontSet s T t1).card - 1) ≠
          (G.lagMin s T t2, (G.frontSet s T t2).card - 1) := by
      intro t1 t2 h12 h2 e
      obtain ⟨k, rfl⟩ : ∃ k, t2 = t1 + k + 1 := ⟨t2 - t1 - 1, by omega⟩
      obtain ⟨e1, e2⟩ := Prod.mk.inj e
      have hlt := (R.phi_lt t1 k h2).2 e1.symm
      have hp := hpos (t1 + k + 1) h2
      omega
    have hcard : (Finset.range T).card ≤
        (G.levelVals s T ×ˢ Finset.range (Fintype.card V)).card := by
      apply Finset.card_le_card_of_injOn
        (fun t => (G.lagMin s T t, (G.frontSet s T t).card - 1))
      · intro t ht
        have ht' : t < T := Finset.mem_range.mp (Finset.mem_coe.mp ht)
        obtain ⟨z, hz, hf, hd⟩ := R.front_level ht'
        rw [Finset.mem_coe, Finset.mem_product]
        refine ⟨?_, Finset.mem_range.mpr ?_⟩
        · refine Finset.mem_biUnion.mpr ⟨z, hz, Finset.mem_image.mpr
            ⟨s t z, R.legal t ht'.le z hz, ?_⟩⟩
          rw [← hd]
          exact hf.val_eq
        · have h1 := hpos t ht'
          have h2 : (G.frontSet s T t).card ≤ Fintype.card V := Finset.card_le_univ _
          show (G.frontSet s T t).card - 1 < Fintype.card V
          omega
      · intro t1 h1 t2 h2 e
        have e' : (G.lagMin s T t1, (G.frontSet s T t1).card - 1) =
            (G.lagMin s T t2, (G.frontSet s T t2).card - 1) := e
        by_contra hne'
        rcases Nat.lt_or_gt_of_ne hne' with h | h
        · exact hne t1 t2 h (Finset.mem_range.mp (Finset.mem_coe.mp h2)) e'
        · exact hne t2 t1 h (Finset.mem_range.mp (Finset.mem_coe.mp h1)) e'.symm
    rw [Finset.card_range, Finset.card_product, Finset.card_range] at hcard
    exact hcard.trans (Nat.mul_le_mul_right _ (G.card_levelVals_le s T))
  · -- (L4) clause (2): the step raises a vertex of the front
    obtain ⟨v, hv, hrise⟩ := R.front_rises ht
    exact ⟨v, hv.1, hv.2, hrise⟩

end

end PG
