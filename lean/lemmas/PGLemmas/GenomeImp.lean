/-
RF-A, the rule-free part of box 208 on the genome (`PGLemmas/GenomeImpStatement.lean`), proved.
No premise.

* `IdealImpRun.toPre`   a run under any improvement rule is an `IdealPreRun`: F1 (`f1`) needs only
                        «kept or strictly improved».
* `IdealCycRun.toImp`   a Howard run is a run under an improvement rule.
* `imp_k1`, `imp_l2`, `imp_l3`, `imp_l5`   from `IdealPreRun.k1`, `l2_pre`, `l3_pre`, `l5_pre`.
* `non_stall_count`     on the lagging non-stall steps the pair (class of the front, size of the
                        front) takes each value once: the class of the front never falls, and
                        where it stays the later front lies in the earlier one and has lost the
                        vertex that changed its class.
* `imp_non_stall`       from `non_stall_count` with the 2M front classes and fronts ≤ N + 2M.
* `imp_k5_new`          F1 at the new gate, (K2), (K3) (c).
-/
import PGLemmas.GenomeImpStatement
import PGLemmas.GenomeLevel

namespace PG

open Classical

noncomputable section

/-- **The count of non-stall steps** (box 208 §4 (C1), (C2)). -/
theorem non_stall_count (V : Type*) [Fintype V] (α : Type*) [LinearOrder α] :
    NonStallCountStatement V α := by
  intro c a b M F hK hM hF
  have hfacts : ∀ t, a ≤ t → t ≤ b → (∃ v, c t v ≠ c b v) →
      ∃ x, FrontAt c b t x ∧
        (Finset.univ.filter (FrontAt c b t)).image (c t) = {c t x} ∧
        1 ≤ (Finset.univ.filter (FrontAt c b t)).card ∧
        (Finset.univ.filter (FrontAt c b t)).card ≤ F := by
    intro t hat htb hl
    obtain ⟨x, hx⟩ := lc_front_exists hl
    refine ⟨x, hx, ?_, Finset.card_pos.mpr ⟨x, Finset.mem_filter.mpr ⟨Finset.mem_univ _, hx⟩⟩,
      hF t hat htb⟩
    ext m
    simp only [Finset.mem_image, Finset.mem_filter, Finset.mem_univ, true_and,
      Finset.mem_singleton]
    constructor
    · rintro ⟨y, hy, rfl⟩
      exact FrontAt.val_eq hy hx
    · rintro rfl
      exact ⟨x, hx, rfl⟩
  -- two different non-stall steps have different pairs
  have key : ∀ t t', a ≤ t → t < t' → t' < b → (∃ v, c t v ≠ c b v) → ¬ StallAt c b t →
      (∃ v, c t' v ≠ c b v) →
      ((Finset.univ.filter (FrontAt c b t)).image (c t),
          (Finset.univ.filter (FrontAt c b t)).card - 1) ≠
        ((Finset.univ.filter (FrontAt c b t')).image (c t'),
          (Finset.univ.filter (FrontAt c b t')).card - 1) := by
    intro t t' hat hlt ht'b hl hns hl' e
    obtain ⟨x, hx, himg, h1, -⟩ := hfacts t hat (by omega) hl
    obtain ⟨y, hy, himg', h1', -⟩ := hfacts t' (by omega) (by omega) hl'
    have e1 : c t x = c t' y := by
      have := congrArg Prod.fst e
      simp only [himg, himg'] at this
      exact Finset.singleton_inj.mp this
    have e2 : (Finset.univ.filter (FrontAt c b t)).card =
        (Finset.univ.filter (FrontAt c b t')).card := by
      have := congrArg Prod.snd e
      simp only at this
      omega
    obtain ⟨v, hv, hv2⟩ : ∃ v, FrontAt c b t v ∧ c (t + 1) v ≠ c t v := by
      by_contra hno
      exact hns ⟨hl, fun v hv => by
        by_contra hv'
        exact hno ⟨v, hv, hv'⟩⟩
    have hsub : Finset.univ.filter (FrontAt c b t') ⊆ Finset.univ.filter (FrontAt c b t) := by
      intro y' hy'
      have hy'' := (Finset.mem_filter.mp hy').2
      exact Finset.mem_filter.mpr ⟨Finset.mem_univ _,
        lc_front_of_eq hK hat hlt.le ht'b.le hx hy'' ((FrontAt.val_eq hy'' hy).trans e1.symm)⟩
    have hvnot : v ∉ Finset.univ.filter (FrontAt c b t') := by
      intro hm
      have hm' := (Finset.mem_filter.mp hm).2
      have h3 : c t' v = c t v := (FrontAt.val_eq hm' hy).trans (e1.symm.trans (FrontAt.val_eq hx hv))
      have h4 : c t v < c (t + 1) v := lt_of_le_of_ne (hK t hat (by omega) v) (Ne.symm hv2)
      have h5 : c (t + 1) v ≤ c t' v := lc_mono hK (by omega) (by omega) ht'b.le v
      exact absurd (lt_of_lt_of_le h4 h5) (by rw [h3]; exact lt_irrefl _)
    have hlt' := Finset.card_lt_card ((Finset.ssubset_iff_of_subset hsub).mpr
      ⟨v, Finset.mem_filter.mpr ⟨Finset.mem_univ _, hv⟩, hvnot⟩)
    omega
  refine (Finset.card_le_card_of_injOn
    (t := (M.image (fun m => ({m} : Finset α))) ×ˢ Finset.range F)
    (fun t => ((Finset.univ.filter (FrontAt c b t)).image (c t),
      (Finset.univ.filter (FrontAt c b t)).card - 1)) ?_ ?_).trans ?_
  · intro t ht
    obtain ⟨hI, hl, -⟩ := Finset.mem_filter.mp ht
    obtain ⟨hat, htb⟩ := Finset.mem_Ico.mp hI
    obtain ⟨x, hx, himg, h1, h2⟩ := hfacts t hat htb.le hl
    refine Finset.mem_product.mpr ⟨?_, Finset.mem_range.mpr (by
      show (Finset.univ.filter (FrontAt c b t)).card - 1 < F
      omega)⟩
    exact Finset.mem_image.mpr ⟨c t x, hM t hat htb.le x hx, himg.symm⟩
  · intro t ht t' ht' e
    obtain ⟨hI, hl, hns⟩ := Finset.mem_filter.mp ht
    obtain ⟨hI', hl', hns'⟩ := Finset.mem_filter.mp ht'
    obtain ⟨hat, htb⟩ := Finset.mem_Ico.mp hI
    obtain ⟨hat', ht'b⟩ := Finset.mem_Ico.mp hI'
    by_contra hne
    rcases lt_or_gt_of_ne hne with hlt | hgt
    · exact key t t' hat hlt ht'b hl hns hl' e
    · exact key t' t hat' hgt htb hl' hns' hl e.symm
  · rw [Finset.card_product, Finset.card_range]
    exact Nat.mul_le_mul_right _ Finset.card_image_le

namespace Genome

variable {G : Genome} {σ τ : ℕ → G.Vertex → G.Vertex} {T : ℕ}

/-- A run under any improvement rule is an `IdealPreRun`: F1 holds. -/
theorem IdealImpRun.toPre (h : G.WF) (R : G.IdealImpRun σ τ T) : G.IdealPreRun σ τ T := by
  refine ⟨R.frozen, R.legal, R.opt, fun t ht v => ?_⟩
  refine f1 G.pr (pr_injective h) G.E G.V0 (σ t) (τ t) (σ (t + 1)) (τ (t + 1)) (R.opt t ht.le)
    (R.opt (t + 1) (by omega)).1 (fun u hu => ?_) v
  by_cases hm : ∃ x, u = Vertex.mover x
  · obtain ⟨x, rfl⟩ := hm
    exact R.improve t ht x
  · have hnm : ∀ x, u ≠ Vertex.mover x := fun x e => hm ⟨x, e⟩
    left
    rw [R.frozen (t + 1) (by omega) u hu hnm, R.frozen t ht.le u hu hnm]

/-- A Howard run is a run under an improvement rule. -/
theorem IdealCycRun.toImp (h : G.WF) (R : G.IdealCycRun σ τ T) : G.IdealImpRun σ τ T := by
  have hpr := pr_injective h
  refine ⟨R.frozen, R.legal, R.opt, fun t ht x => ?_, fun t ht => ?_⟩
  · by_cases e : σ (t + 1) (Vertex.mover x) = σ t (Vertex.mover x)
    · exact Or.inl e
    · right
      obtain ⟨-, hbest, hkeep⟩ := R.howard t ht x
      rw [nxt_mover] at hbest
      rw [nxt_mover, nxt_mover] at hkeep
      have hin := R.legal t ht.le x
      obtain ⟨w, hw, hnle⟩ : ∃ w ∈ G.E (Vertex.mover x), ¬ Val.le G.pr
          (val G.pr (nxt G.V0 σ τ t) w) (val G.pr (nxt G.V0 σ τ t) (σ t (Vertex.mover x))) := by
        by_contra hno
        exact e (hkeep ⟨hin, fun w hw => by
          by_contra hw'
          exact hno ⟨w, hw, hw'⟩⟩)
      exact Val.lt_of_lt_of_le hpr (Val.lt_of_not_le hpr hnle) (hbest w hw)
  · obtain ⟨x, y, hy, hlt⟩ := R.moves t ht
    refine ⟨x, fun e => ?_⟩
    have hbest := (R.howard t ht x).2.1 y hy
    rw [nxt_mover, e] at hbest
    exact Val.not_le_of_lt hpr hlt hbest

/-- **(K1) MONOTONE**, rule-free. -/
theorem imp_k1 : G.ImpK1Statement := fun h _ _ _ R _ ht v => (R.toPre h).k1 h ht v

/-- **(L2)**, rule-free. -/
theorem imp_l2 : G.ImpL2Statement := fun h σ τ T R => l2_pre h σ τ T (R.toPre h)

/-- **(L3)**, rule-free. -/
theorem imp_l3 : G.ImpL3Statement := fun h σ τ T R => l3_pre h σ τ T (R.toPre h)

/-- **(L5)**, rule-free. -/
theorem imp_l5 : G.ImpL5Statement := fun h σ τ T R => l5_pre h σ τ T (R.toPre h)

/-- **At most P = 2M(N + 2M) non-stall steps**, for every improvement rule and every reference
state. -/
theorem imp_non_stall : G.ImpNonStallStatement := by
  intro h σ τ T R b hbT
  have P := R.toPre h
  obtain ⟨S, hS, hSmem⟩ : ∃ S : Finset (ℤ ×ₗ ℤ), S.card ≤ 2 * G.M ∧
      ∀ t, t ≤ b → ∀ v, FrontAt (G.ck σ τ) b t v → G.ck σ τ t v ∈ S := by
    refine ⟨Finset.univ.image (fun o : G.Opt => G.ck σ τ b (Vertex.gate o)) ∪
      Finset.univ.image (fun o : G.Opt => G.clsKey (Vertex.beta o, ∅)), ?_, ?_⟩
    · refine (Finset.card_union_le _ _).trans ?_
      have h1 : (Finset.univ.image (fun o : G.Opt => G.ck σ τ b (Vertex.gate o))).card ≤ G.M := by
        refine Finset.card_image_le.trans ?_
        rw [Finset.card_univ]
        rfl
      have h2 : (Finset.univ.image
          (fun o : G.Opt => G.clsKey (Vertex.beta o, ∅))).card ≤ G.M := by
        refine Finset.card_image_le.trans ?_
        rw [Finset.card_univ]
        rfl
      omega
    · intro t ht v hv
      rcases (l5_pre h σ τ T P b t ht hbT).1 v hv with ⟨o, ho⟩ | ⟨o, ho⟩
      · exact Finset.mem_union.mpr (Or.inl (Finset.mem_image.mpr
          ⟨o, Finset.mem_univ _, ((ck_eq_iff h).mpr ho).symm⟩))
      · refine Finset.mem_union.mpr (Or.inr (Finset.mem_image.mpr ⟨o, Finset.mem_univ _, ?_⟩))
        show G.clsKey (Vertex.beta o, ∅) = G.clsKey (G.cls (nxt G.V0 σ τ t) v)
        rw [ho]
  have hc := non_stall_count G.Vertex (ℤ ×ₗ ℤ) (G.ck σ τ) 0 b S (G.N + 2 * G.M)
    (fun t _ ht v => P.ck_step h (lt_of_lt_of_le ht hbT) v)
    (fun t _ ht v hv => hSmem t ht v hv)
    (fun t _ ht => (l5_pre h σ τ T P b t ht hbT).2)
  rw [← Finset.range_eq_Ico] at hc
  exact hc.trans (Nat.mul_le_mul_right _ hS)

/-- **The rule-free remnant of (K5)**: the class at `t` of the new gate of a mover is at most the
class of the mover at `t + 1`. -/
theorem imp_k5_new : G.ImpK5NewStatement := by
  intro h σ τ T R t ht x
  have P := R.toPre h
  have hs := P.isState ht.le
  have hs' := P.isState (t := t + 1) (by omega)
  obtain ⟨k, hk⟩ := hs'.mover x
  have hσ : σ (t + 1) (Vertex.mover x) = Vertex.gate ⟨x, k⟩ := by
    rw [← hk, nxt_mover]
  rw [hσ, cls_step h hs' (P.bOnly h (t := t + 1) (by omega)) (v := Vertex.mover x) rfl, hk]
  exact Genome.k2 h _ _ hs hs' (P.k2 h ht.le) (P.k2 h (t := t + 1) (by omega)) _ _ rfl rfl
    (P.mono t ht _)

end Genome

end

end PG
