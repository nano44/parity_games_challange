/-
Premise (M) on one-player games (`ValMonoStatement`, `PGLemmas/Statements3.lean`): VJ00 Lemma 5.7
when the opponent has no choice.

Proof (the shortest-path / potential argument of VJ00 §5.1-§5.3, with integer weights in place of
VJ00's multisets; `PGLemmas/Weights.lean`).  Write Ξ for the values under `s`, Λ for its cycle
nodes, and let `s'` arise from `s` by improving switches.
* `UnderProgAt`    the three conditions on one edge `u → w` (VJ00 §5.3 «locally under-progressive»,
                   in keys); `underProgAt_of_le`: they hold when Ξ(s u) ⊴ Ξ(w);
* `rew_lam_step`   along an edge of `s'` the reward of Λ does not fall;
* `edge_key`       along an edge `u → s' u` inside one Λ-class, off the cycle node, the key of Ξ(u)
                   is at most the key of Ξ(s' u) plus the step weight of `u`;
* `telescope`      the same along a walk of `s'`;
* `rew_cycle`      the cycle node λ′ of a play of `s'` has a larger reward than the common Λ of
                   its cycle, or is that Λ (a cycle of `s'` has non-negative total weight);
* `prefix_key`     if all Λ along the play of `s'` equal λ′, the keys compare along the prefix;
* `val_le_of_underProg`  VJ00 Lemma 5.5 for one successor map; `val_mono` the statement.
-/
import PGLemmas.Weights
import PGLemmas.Statements3
import Mathlib.Dynamics.PeriodicPts.Defs

namespace PG

open Classical

noncomputable section

variable {V : Type*} [Fintype V] {pr : V → ℕ} {s s' : V → V}

/-! ### Rewards -/

omit [Fintype V] in
theorem rew_le_pr (u : V) : rew pr u ≤ (pr u : ℤ) := by
  unfold rew
  split_ifs <;> omega

omit [Fintype V] in
theorem neg_pr_le_rew (u : V) : -(pr u : ℤ) ≤ rew pr u := by
  unfold rew
  split_ifs <;> omega

omit [Fintype V] in
theorem rew_of_even {u : V} (h : Even (pr u)) : rew pr u = (pr u : ℤ) := by
  unfold rew
  rw [ite_eq_left h]

omit [Fintype V] in
theorem rew_of_odd {u : V} (h : ¬ Even (pr u)) : rew pr u = -(pr u : ℤ) := by
  unfold rew
  rw [ite_eq_right h]

/-- The successor of a cycle node has an empty path component: its path runs on the cycle. -/
theorem pset_succ_of_lam_eq (hpr : Function.Injective pr) {ℓ : V} (hℓ : lam pr s ℓ = ℓ) :
    (val pr s (s ℓ)).set = ∅ := by
  ext u
  simp only [Finset.notMem_empty, iff_false]
  intro hu
  change u ∈ pset pr s (s ℓ) at hu
  rw [mem_pset, lam_succ hpr, hℓ] at hu
  obtain ⟨hlt, j, -, hj⟩ := hu
  obtain ⟨-, p, hp, hper⟩ := (lam_spec pr s ℓ).1
  rw [hℓ] at hper
  have hcyc : OnCycle s ℓ u := by
    refine ⟨⟨j + 1, by rw [Function.iterate_succ_apply]; exact hj⟩, p, hp, ?_⟩
    rw [← hj, ← Function.iterate_succ_apply, ← Function.iterate_add_apply, Nat.add_comm,
      Function.iterate_add_apply, hper]
  have hle := (lam_spec pr s ℓ).2 u hcyc
  rw [hℓ] at hle
  omega

/-! ### Under-progressive edges (VJ00 §5.3) -/

/-- Every vertex keeps its successor or moves to one of strictly larger value. -/
def Improves (pr : V → ℕ) (s s' : V → V) : Prop :=
  ∀ v, s' v = s v ∨ Val.lt pr (val pr s (s v)) (val pr s (s' v))

/-- The edge `u → w` is under-progressive for the valuation Ξ of `s` (VJ00 §5.3, in keys):
(1) the reward of Λ does not fall along it; (2) inside one Λ-class, at a vertex `u` that is not
the cycle node, the key of Ξ(u) is at most the key of Ξ(w) plus the step weight of `u`; (3) at a
cycle node `u`, a successor `w` in its class has a path of non-negative weight. -/
def UnderProgAt (pr : V → ℕ) (s : V → V) (u w : V) : Prop :=
  rew pr (lam pr s u) ≤ rew pr (lam pr s w) ∧
  (lam pr s u ≠ u → lam pr s w = lam pr s u →
    LexLe (wt pr (val pr s u).set) (sl pr (val pr s u))
      (wt pr (val pr s w).set + dw pr (lam pr s u) u)
      (sl pr (val pr s w) + ds pr (lam pr s u))) ∧
  (lam pr s u = u → lam pr s w = u → 0 ≤ wt pr (val pr s w).set)

/-- The valuation of `s` is locally under-progressive along the edges of `s'`. -/
def UnderProg (pr : V → ℕ) (s s' : V → V) : Prop := ∀ u, UnderProgAt pr s u (s' u)

/-- An edge `u → w` whose end is worth at least the current successor of `u` is
under-progressive. -/
theorem underProgAt_of_le (hpr : Function.Injective pr) {u w : V}
    (hle : Val.le pr (val pr s (s u)) (val pr s w)) : UnderProgAt pr s u w := by
  have htop : (val pr s (s u)).top = lam pr s u := lam_succ hpr u
  refine ⟨?_, ?_, ?_⟩
  · rcases Val.top_of_le hle with e | h
    · have e' : lam pr s (s u) = lam pr s w := e
      rw [← e', lam_succ hpr]
    · have h' : rew pr (lam pr s (s u)) < rew pr (lam pr s w) := h
      rw [lam_succ hpr] at h'
      exact h'.le
  · intro hu hcls
    have hw : wt pr (val pr s u).set = wt pr (val pr s (s u)).set + dw pr (lam pr s u) u := by
      rw [val_step hpr hu, wt_ext (notMem_pset_succ hpr hu), htop]
    have hs : sl pr (val pr s u) = sl pr (val pr s (s u)) + ds pr (lam pr s u) := by
      rw [val_step hpr hu, sl_ext, htop]
    have htops : (val pr s (s u)).top = (val pr s w).top := htop.trans hcls.symm
    have hlex := (Val.le_iff_lex hpr htops).mp hle
    unfold LexLe at hlex ⊢
    omega
  · intro hu hw
    have htops : (val pr s (s u)).top = (val pr s w).top := htop.trans (hu.trans hw.symm)
    have hlex := (Val.le_iff_lex hpr htops).mp hle
    rw [pset_succ_of_lam_eq hpr hu, wt_empty] at hlex
    unfold LexLe at hlex
    omega

theorem underProg_of_improves (hpr : Function.Injective pr) (himp : Improves pr s s') :
    UnderProg pr s s' := by
  intro u
  apply underProgAt_of_le hpr
  rcases himp u with e | hlt
  · rw [e]; exact Val.le_refl _
  · exact Val.le_of_lt hlt

/-! ### The old cycle nodes along the new strategy -/

/-- Along an edge of `s'` the reward of the old cycle node does not fall. -/
theorem rew_lam_step (h : UnderProg pr s s') (u : V) :
    rew pr (lam pr s u) ≤ rew pr (lam pr s (s' u)) := (h u).1

theorem rew_lam_iterate (h : UnderProg pr s s') (u : V) (n : ℕ) :
    rew pr (lam pr s u) ≤ rew pr (lam pr s (s'^[n] u)) := by
  induction n with
  | zero => exact le_rfl
  | succ n ih =>
    rw [Function.iterate_succ_apply']
    exact ih.trans (rew_lam_step h _)

/-- On a cycle of `s'` all vertices have the same old cycle node. -/
theorem lam_orbit (hpr : Function.Injective pr) (h : UnderProg pr s s') {c : V} {p : ℕ}
    (hp : 0 < p) (hc : s'^[p] c = c) (n : ℕ) : lam pr s (s'^[n] c) = lam pr s c := by
  apply rew_injective hpr
  apply le_antisymm
  · have h1 := rew_lam_iterate h (s'^[n] c) (p * n - n)
    rw [← Function.iterate_add_apply] at h1
    have e : p * n - n + n = p * n := by
      have : n ≤ p * n := Nat.le_mul_of_pos_left n hp
      omega
    have h2 : s'^[p * n] c = c := Function.IsPeriodicPt.mul_const hc n
    rw [e, h2] at h1
    exact h1
  · exact rew_lam_iterate h c n

/-! ### Keys along the edges of `s'` -/

/-- One edge `u → s' u` inside one Λ-class, `u` not the cycle node: the key of `Ξ(u)` is at most
the key of `Ξ(s' u)` plus the step weight of `u`. -/
theorem edge_key (h : UnderProg pr s s') {u : V}
    (hu : lam pr s u ≠ u) (hcls : lam pr s (s' u) = lam pr s u) :
    LexLe (wt pr (val pr s u).set) (sl pr (val pr s u))
      (wt pr (val pr s (s' u)).set + dw pr (lam pr s u) u)
      (sl pr (val pr s (s' u)) + ds pr (lam pr s u)) := (h u).2.1 hu hcls

/-- The same along a walk `s'^[a] c, …, s'^[b] c` inside the Λ-class of `ℓ` that avoids `ℓ`
before its end. -/
theorem telescope (h : UnderProg pr s s') {c ℓ : V}
    (hcls : ∀ j, lam pr s (s'^[j] c) = ℓ) (a : ℕ) :
    ∀ b, a ≤ b → (∀ j, a ≤ j → j < b → s'^[j] c ≠ ℓ) →
      LexLe (wt pr (val pr s (s'^[a] c)).set) (sl pr (val pr s (s'^[a] c)))
        (wt pr (val pr s (s'^[b] c)).set + ∑ j ∈ Finset.Ico a b, dw pr ℓ (s'^[j] c))
        (sl pr (val pr s (s'^[b] c)) + ∑ _j ∈ Finset.Ico a b, ds pr ℓ) := by
  intro b hab
  induction b, hab using Nat.le_induction with
  | base =>
    intro _
    simp only [Finset.Ico_self, Finset.sum_empty, add_zero]
    exact Or.inr ⟨rfl, le_rfl⟩
  | succ b hab ih =>
    intro hne
    have ih' := ih (fun j h1 h2 => hne j h1 (by omega))
    have hu : lam pr s (s'^[b] c) ≠ s'^[b] c := by
      rw [hcls b]
      exact (hne b hab (by omega)).symm
    have hsucc : s' (s'^[b] c) = s'^[b + 1] c := (Function.iterate_succ_apply' s' b c).symm
    have hc2 : lam pr s (s' (s'^[b] c)) = lam pr s (s'^[b] c) := by
      rw [hsucc, hcls, hcls]
    have hedge := edge_key h hu hc2
    rw [hcls b, hsucc] at hedge
    rw [Finset.sum_Ico_succ_top hab, Finset.sum_Ico_succ_top hab]
    unfold LexLe at ih' hedge ⊢
    omega

omit [Fintype V] in
/-- The step weights along distinct vertices add up to the weight of a set. -/
theorem sum_dw_eq_wt {c ℓ : V} {a q : ℕ}
    (hinj : Set.InjOn (fun j => s'^[j] c) (Finset.Ico a q : Set ℕ)) :
    ∑ j ∈ Finset.Ico a q, dw pr ℓ (s'^[j] c) =
      wt pr (((Finset.Ico a q).image (fun j => s'^[j] c)).filter (fun u => pr ℓ < pr u)) := by
  unfold wt
  rw [Finset.sum_filter, Finset.sum_image hinj]
  rfl

omit [Fintype V] in
theorem sum_ds (ℓ : V) (a q : ℕ) :
    ∑ _j ∈ Finset.Ico a q, ds pr ℓ = ((q - a : ℕ) : ℤ) * ds pr ℓ := by
  rw [Finset.sum_const, Nat.card_Ico, nsmul_eq_mul]

/-! ### The cycle of a play of `s'` -/

/-- The cycle node `λ′` of a play of `s'` and the common old cycle node `ℓ*` of its cycle:
`rew(ℓ*) < rew(λ′)`, or `λ′ = ℓ*`.  (A cycle of `s'` has non-negative total weight.) -/
theorem rew_cycle (hpr : Function.Injective pr) (h : UnderProg pr s s') (v : V) :
    rew pr (lam pr s (lam pr s' v)) < rew pr (lam pr s' v) ∨
      lam pr s (lam pr s' v) = lam pr s' v := by
  obtain ⟨⟨n0, hn0⟩, p, hp, hper⟩ := (lam_spec pr s' v).1
  -- every vertex of the cycle is less relevant than `λ′`
  have hmaxorb : ∀ n, pr (s'^[n] (lam pr s' v)) ≤ pr (lam pr s' v) := by
    intro n
    apply (lam_spec pr s' v).2
    refine ⟨⟨n + n0, by rw [Function.iterate_add_apply, hn0]⟩, p, hp, ?_⟩
    rw [← Function.iterate_add_apply, Nat.add_comm, Function.iterate_add_apply, hper]
  have hcls : ∀ j, lam pr s (s'^[j] (lam pr s' v)) = lam pr s (lam pr s' v) :=
    lam_orbit hpr h hp hper
  by_cases hA : ∃ n, s'^[n] (lam pr s' v) = lam pr s (lam pr s' v)
  · -- Case A: the old cycle node `ℓ*` lies on the new cycle
    obtain ⟨n, hn⟩ := hA
    by_cases heq : lam pr s (lam pr s' v) = lam pr s' v
    · exact Or.inr heq
    left
    have hlt : pr (lam pr s (lam pr s' v)) < pr (lam pr s' v) := by
      have h1 := hmaxorb n
      rw [hn] at h1
      exact lt_of_le_of_ne h1 (fun e => heq (hpr e))
    by_cases hev : Even (pr (lam pr s' v))
    · have h1 := rew_le_pr (pr := pr) (lam pr s (lam pr s' v))
      rw [rew_of_even hev]
      have : (pr (lam pr s (lam pr s' v)) : ℤ) < pr (lam pr s' v) := by exact_mod_cast hlt
      omega
    exfalso
    -- write `ℓ*` for the old cycle node; it is periodic under `s'`, with minimal period `q`
    set ℓ := lam pr s (lam pr s' v) with hℓdef
    have hℓℓ : lam pr s ℓ = ℓ := lam_lam hpr _
    have hperℓ : s'^[p] ℓ = ℓ := by
      rw [← hn, ← Function.iterate_add_apply, Nat.add_comm, Function.iterate_add_apply, hper]
    have hq : 0 < Function.minimalPeriod s' ℓ := Function.IsPeriodicPt.minimalPeriod_pos hp hperℓ
    have hcq : s'^[Function.minimalPeriod s' ℓ] ℓ = ℓ := Function.iterate_minimalPeriod
    have hclsℓ : ∀ j, lam pr s (s'^[j] ℓ) = ℓ := by
      intro j
      rw [lam_orbit hpr h hp hperℓ j, hℓℓ]
    have hneℓ : ∀ j, 1 ≤ j → j < Function.minimalPeriod s' ℓ → s'^[j] ℓ ≠ ℓ := by
      intro j h1 h2 e
      have := Function.IsPeriodicPt.minimalPeriod_le (by omega : 0 < j) e
      omega
    -- telescope from `s' ℓ` round to `ℓ`
    have T := telescope h hclsℓ 1 (Function.minimalPeriod s' ℓ) hq hneℓ
    rw [hcq, val_of_lam_eq hℓℓ] at T
    -- the weight of `Ξ(s' ℓ)` is non-negative
    have hlow : 0 ≤ wt pr (val pr s (s'^[1] ℓ)).set := by
      rw [Function.iterate_one]
      have h1 := hclsℓ 1
      rw [Function.iterate_one] at h1
      exact (h ℓ).2.2 hℓℓ h1
    -- the weights met on the way are those of a set whose top `λ′` is odd
    have hinj : Set.InjOn (fun j => s'^[j] ℓ)
        (Finset.Ico 1 (Function.minimalPeriod s' ℓ) : Set ℕ) := by
      intro i hi j hj h
      have hi' := Finset.mem_Ico.mp (Finset.mem_coe.mp hi)
      have hj' := Finset.mem_Ico.mp (Finset.mem_coe.mp hj)
      exact Function.iterate_injOn_Iio_minimalPeriod (Set.mem_Iio.mpr hi'.2)
        (Set.mem_Iio.mpr hj'.2) h
    rw [sum_dw_eq_wt hinj] at T
    -- `λ′` is on the walk
    have hk : s'^[p * n - n] ℓ = lam pr s' v := by
      rw [← hn, ← Function.iterate_add_apply]
      have e : p * n - n + n = p * n := by
        have : n ≤ p * n := Nat.le_mul_of_pos_left n hp
        omega
      rw [e]
      exact Function.IsPeriodicPt.mul_const hper n
    have hi : s'^[(p * n - n) % Function.minimalPeriod s' ℓ] ℓ = lam pr s' v := by
      rw [Function.iterate_mod_minimalPeriod_eq, hk]
    have hi0 : (p * n - n) % Function.minimalPeriod s' ℓ ≠ 0 := by
      intro e
      rw [e] at hi
      exact heq hi
    have hmem : lam pr s' v ∈ ((Finset.Ico 1 (Function.minimalPeriod s' ℓ)).image
        (fun j => s'^[j] ℓ)).filter (fun u => pr ℓ < pr u) := by
      rw [Finset.mem_filter, Finset.mem_image]
      refine ⟨⟨(p * n - n) % Function.minimalPeriod s' ℓ, ?_, hi⟩, hlt⟩
      rw [Finset.mem_Ico]
      exact ⟨by omega, Nat.mod_lt _ hq⟩
    have hmaxS : ∀ u ∈ ((Finset.Ico 1 (Function.minimalPeriod s' ℓ)).image
        (fun j => s'^[j] ℓ)).filter (fun u => pr ℓ < pr u), pr u ≤ pr (lam pr s' v) := by
      intro u hu
      obtain ⟨j, -, rfl⟩ := Finset.mem_image.mp (Finset.mem_filter.mp hu).1
      have := hmaxorb (j + n)
      rw [Function.iterate_add_apply, hn] at this
      exact this
    have hneg := wt_neg_of_max_odd hpr hmem hmaxS hev
    simp only [wt_empty] at T
    unfold LexLe at T
    omega
  · -- Case B: the old cycle node `ℓ*` is not on the new cycle
    left
    set ℓ := lam pr s (lam pr s' v) with hℓdef
    have hq : 0 < Function.minimalPeriod s' (lam pr s' v) :=
      Function.IsPeriodicPt.minimalPeriod_pos hp hper
    have hcq : s'^[Function.minimalPeriod s' (lam pr s' v)] (lam pr s' v) = lam pr s' v :=
      Function.iterate_minimalPeriod
    have hne : ∀ j, 0 ≤ j → j < Function.minimalPeriod s' (lam pr s' v) →
        s'^[j] (lam pr s' v) ≠ ℓ := fun j _ _ e => hA ⟨j, e⟩
    have T := telescope h hcls 0 (Function.minimalPeriod s' (lam pr s' v))
      (Nat.zero_le _) hne
    rw [hcq, Function.iterate_zero, id_eq] at T
    have hinj : Set.InjOn (fun j => s'^[j] (lam pr s' v))
        (Finset.Ico 0 (Function.minimalPeriod s' (lam pr s' v)) : Set ℕ) := by
      intro i hi j hj h
      have hi' := Finset.mem_Ico.mp (Finset.mem_coe.mp hi)
      have hj' := Finset.mem_Ico.mp (Finset.mem_coe.mp hj)
      exact Function.iterate_injOn_Iio_minimalPeriod (Set.mem_Iio.mpr hi'.2)
        (Set.mem_Iio.mpr hj'.2) h
    rw [sum_dw_eq_wt hinj, sum_ds] at T
    have hmaxS : ∀ u ∈ ((Finset.Ico 0 (Function.minimalPeriod s' (lam pr s' v))).image
        (fun j => s'^[j] (lam pr s' v))).filter (fun u => pr ℓ < pr u),
        pr u ≤ pr (lam pr s' v) := by
      intro u hu
      obtain ⟨j, -, rfl⟩ := Finset.mem_image.mp (Finset.mem_filter.mp hu).1
      exact hmaxorb j
    have hneq : lam pr s' v ≠ ℓ := fun e => hA ⟨0, e⟩
    by_cases hlt : pr ℓ < pr (lam pr s' v)
    · -- `λ′` is the top of the set and must be even
      have hmem : lam pr s' v ∈ ((Finset.Ico 0 (Function.minimalPeriod s' (lam pr s' v))).image
          (fun j => s'^[j] (lam pr s' v))).filter (fun u => pr ℓ < pr u) := by
        rw [Finset.mem_filter, Finset.mem_image]
        exact ⟨⟨0, Finset.mem_Ico.mpr ⟨le_rfl, hq⟩, rfl⟩, hlt⟩
      by_cases hev : Even (pr (lam pr s' v))
      · have h1 := rew_le_pr (pr := pr) ℓ
        rw [rew_of_even hev]
        have : (pr ℓ : ℤ) < pr (lam pr s' v) := by exact_mod_cast hlt
        omega
      · exfalso
        have hneg := wt_neg_of_max_odd hpr hmem hmaxS hev
        unfold LexLe at T
        omega
    · -- no vertex of the cycle is above `ℓ*`: the cycle is weightless, so `ℓ*` is odd
      have hlt' : pr (lam pr s' v) < pr ℓ :=
        lt_of_le_of_ne (not_lt.mp hlt) (fun e => hneq (hpr e))
      have hempty : ((Finset.Ico 0 (Function.minimalPeriod s' (lam pr s' v))).image
          (fun j => s'^[j] (lam pr s' v))).filter (fun u => pr ℓ < pr u) = ∅ := by
        rw [Finset.filter_eq_empty_iff]
        intro u hu
        obtain ⟨j, -, rfl⟩ := Finset.mem_image.mp hu
        have := hmaxorb j
        omega
      rw [hempty, wt_empty] at T
      have hodd : ¬ Even (pr ℓ) := by
        intro hev
        unfold LexLe at T
        have hds : ds pr ℓ = -1 := by unfold ds; rw [ite_eq_left hev]
        rw [hds] at T
        have : (0 : ℤ) < ((Function.minimalPeriod s' (lam pr s' v) - 0 : ℕ) : ℤ) := by
          exact_mod_cast (by omega : 0 < Function.minimalPeriod s' (lam pr s' v) - 0)
        omega
      rw [rew_of_odd hodd]
      have h1 := neg_pr_le_rew (pr := pr) (lam pr s' v)
      have : (pr (lam pr s' v) : ℤ) < pr ℓ := by exact_mod_cast hlt'
      omega

/-! ### The prefix of a play of `s'` -/

/-- If the play of `s'` from `u` stays in the Λ-class of its own cycle node `ℓ`, the key of
`Ξ(u)` is at most the key of the new value of `u`. -/
theorem prefix_key (hpr : Function.Injective pr) (h : UnderProg pr s s') {ℓ : V} :
    ∀ k u, plen pr s' u = k → lam pr s' u = ℓ → (∀ n, n ≤ k → lam pr s (s'^[n] u) = ℓ) →
      LexLe (wt pr (val pr s u).set) (sl pr (val pr s u))
        (wt pr (val pr s' u).set) (sl pr (val pr s' u)) := by
  intro k
  induction k with
  | zero =>
    intro u hk hl hcls
    have hu' : lam pr s' u = u := lam_eq_of_plen_eq_zero hk
    have hu : lam pr s u = u := by
      have := hcls 0 le_rfl
      rw [Function.iterate_zero, id_eq] at this
      rw [this, ← hl, hu']
    rw [val_of_lam_eq hu, val_of_lam_eq hu']
    exact Or.inr ⟨rfl, le_rfl⟩
  | succ k ih =>
    intro u hk hl hcls
    have hl' : lam pr s' u ≠ u := by
      intro h
      rw [plen_eq_zero_of_lam_eq h] at hk
      omega
    have hp := plen_succ hpr hl'
    have h0 : lam pr s u = ℓ := by
      have := hcls 0 (by omega)
      rwa [Function.iterate_zero, id_eq] at this
    have h1 : lam pr s (s' u) = ℓ := by
      have := hcls 1 (by omega)
      rwa [Function.iterate_one] at this
    have hu : lam pr s u ≠ u := by rw [h0, ← hl]; exact hl'
    have hedge := edge_key h hu (h1.trans h0.symm)
    rw [h0] at hedge
    have hih := ih (s' u) (by omega) ((lam_succ hpr u).trans hl) (by
      intro n hn
      rw [← Function.iterate_succ_apply]
      exact hcls (n + 1) (by omega))
    have htop' : (val pr s' (s' u)).top = ℓ := (lam_succ hpr u).trans hl
    have hw : wt pr (val pr s' u).set = wt pr (val pr s' (s' u)).set + dw pr ℓ u := by
      rw [val_step hpr hl', wt_ext (notMem_pset_succ hpr hl'), htop']
    have hs : sl pr (val pr s' u) = sl pr (val pr s' (s' u)) + ds pr ℓ := by
      rw [val_step hpr hl', sl_ext, htop']
    unfold LexLe at hedge hih ⊢
    omega

/-- **VJ00 Lemma 5.5** for one successor map: if the valuation of `s` is locally
under-progressive along the edges of `s'`, it is pointwise below the valuation of `s'`. -/
theorem val_le_of_underProg (hpr : Function.Injective pr) (h : UnderProg pr s s') (v : V) :
    Val.le pr (val pr s v) (val pr s' v) := by
  have h0 : rew pr (lam pr s v) ≤ rew pr (lam pr s (lam pr s' v)) := by
    have := rew_lam_iterate h v (plen pr s' v)
    rwa [iterate_plen] at this
  rcases rew_cycle hpr h v with hlt | heq
  · exact Val.le_of_lt (Val.lt_of_rew_lt (h0.trans_lt hlt))
  · rw [heq] at h0
    rcases h0.lt_or_eq with hlt | he
    · exact Val.le_of_lt (Val.lt_of_rew_lt hlt)
    · -- equal cycle nodes: compare the path components along the prefix
      have hℓ : lam pr s v = lam pr s' v := rew_injective hpr he
      have hcls : ∀ n, n ≤ plen pr s' v → lam pr s (s'^[n] v) = lam pr s' v := by
        intro n hn
        apply rew_injective hpr
        apply le_antisymm
        · have h1 := rew_lam_iterate h (s'^[n] v) (plen pr s' v - n)
          rw [← Function.iterate_add_apply] at h1
          have e : plen pr s' v - n + n = plen pr s' v := by omega
          rw [e, iterate_plen, heq] at h1
          exact h1
        · have h1 := rew_lam_iterate h v n
          rw [hℓ] at h1
          exact h1
      exact (Val.le_iff_lex hpr hℓ).mpr (prefix_key hpr h (plen pr s' v) v rfl rfl hcls)

/-- **Premise (M) on one-player games** (VJ00 Lemma 5.7 with no choice for the opponent). -/
theorem val_mono : ValMonoStatement V := by
  intro pr hpr s s' himp v
  exact val_le_of_underProg hpr (underProg_of_improves hpr himp) v

end

end PG
