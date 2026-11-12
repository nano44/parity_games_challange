/-
Box 208 §3, Lemma LEVEL on the genome: `l2 : G.L2Statement`, `l3 : G.L3Statement`,
`l5 : G.L5Statement` (`PGLemmas/GenomeLevelStatement.lean`).  No premise.

* `ck_eq_iff`, `ck_le_iff`, `ck_lt_iff`   keys against classes (ClassOrder).
* `IdealCycRun.ck_mono`                   (K1) on keys, over any number of steps.
* `cls_succ_le`                           (K3) (c), (d), (e): the class does not rise along the play.
* `IdealCycRun.cls_const`                 (K3) (e) and the β-vertices with successor u: classes that
                                          are the same at every state.
* `l2`  the constant classes never lag; an e-vertex with a mover successor w either has its class of
        b (w does not lag) or is above w (w lags), so it is not in the front.
* `l3`  along the play of a front vertex the classes do not rise, so a lagging play vertex is in the
        front.  If some play vertex does not lag, the last lagging one before it is a mover ((K4) at b
        excludes a gate, the frozen successor excludes a β): case (α).  Otherwise the whole play lags,
        and its cycle node is a β-vertex of class (c, ∅): case (β).
* `l5`  from `l3` and `l2`.
-/
import PGLemmas.GenomeLevelStatement
import PGLemmas.GenomeOrder
import PGLemmas.GenomeK4
import PGLemmas.LevelCount

namespace PG

open Classical

noncomputable section

namespace Genome

variable {G : Genome} {σ τ : ℕ → G.Vertex → G.Vertex} {T : ℕ}

/-! ### Keys and classes -/

theorem ck_eq_iff (h : G.WF) {t t' : ℕ} {v v' : G.Vertex} :
    G.ck σ τ t v = G.ck σ τ t' v' ↔
      G.cls (nxt G.V0 σ τ t) v = G.cls (nxt G.V0 σ τ t') v' :=
  ⟨fun e => clsKey_injective h e, fun e => by unfold ck; rw [e]⟩

theorem ck_le_iff (h : G.WF) {t t' : ℕ} {v v' : G.Vertex} :
    G.ck σ τ t v ≤ G.ck σ τ t' v' ↔
      G.clsLe (G.cls (nxt G.V0 σ τ t) v) (G.cls (nxt G.V0 σ τ t') v') :=
  (clsKey_le_iff h).symm

theorem ck_lt_iff (h : G.WF) {t t' : ℕ} {v v' : G.Vertex} :
    G.ck σ τ t v < G.ck σ τ t' v' ↔
      G.clsLt (G.cls (nxt G.V0 σ τ t) v) (G.cls (nxt G.V0 σ τ t') v') :=
  (clsKey_lt_iff h).symm

/-- B-ONLY at every state of a run. -/
theorem IdealCycRun.bOnly (h : G.WF) (R : G.IdealCycRun σ τ T) {t : ℕ} (ht : t ≤ T) :
    G.BOnly (nxt G.V0 σ τ t) :=
  fun _ hv hve o => b_only h (R.opt t ht) (R.isState ht) hv hve o

/-- (K1) on keys. -/
theorem IdealCycRun.ck_step (h : G.WF) (R : G.IdealCycRun σ τ T) {t : ℕ} (ht : t < T)
    (v : G.Vertex) : G.ck σ τ t v ≤ G.ck σ τ (t + 1) v :=
  (ck_le_iff h).mpr (k1 h σ τ T R t ht v)

/-- (K1) on keys, over any number of steps. -/
theorem IdealCycRun.ck_mono (h : G.WF) (R : G.IdealCycRun σ τ T) {t t' : ℕ} (htt : t ≤ t')
    (ht' : t' ≤ T) (v : G.Vertex) : G.ck σ τ t v ≤ G.ck σ τ t' v :=
  lc_mono (c := G.ck σ τ) (a := 0) (b := T) (fun _ _ ht u => R.ck_step h ht u) (Nat.zero_le _)
    htt ht' v

/-- The successor of a mover in the state of a run is Even's choice. -/
theorem nxt_mover (x : Fin G.N) (t : ℕ) :
    nxt G.V0 σ τ t (Vertex.mover x) = σ t (Vertex.mover x) :=
  pair_of_mem (mem_V0.mpr rfl)

/-! ### Classes along the play -/

section State

variable {s : G.Vertex → G.Vertex}

/-- (K3) (c), (d), (e): the class of the successor is at most the class of the vertex. -/
theorem cls_succ_le (h : G.WF) (hs : G.IsState s) (hb : G.BOnly s) (v : G.Vertex) :
    G.clsLe (G.cls s (s v)) (G.cls s v) := by
  cases hE : G.isE v with
  | false => exact Or.inr (cls_step h hs hb hE).symm
  | true =>
    obtain ⟨o, rfl⟩ := isE_iff.mp hE
    cases hw : G.wt o with
    | none =>
      have hsucc : s (Vertex.eface o) = Vertex.cW := by
        rw [hs.eface o]
        simp only [start0, hw]
      rw [hsucc, cls_eface_none h hs hw, cls_fixed hs.cW]
      exact Or.inr rfl
    | some y =>
      have hsucc : s (Vertex.eface o) = Vertex.mover y := by
        rw [hs.eface o]
        simp only [start0, hw]
      rw [hsucc]
      exact Or.inl (cls_eface h hs hb hw).2.2

/-- A cycle node has the class `(v, ∅)`. -/
theorem cls_of_lam_eq {v : G.Vertex} (hl : lam G.pr s v = v) : G.cls s v = (v, ∅) := by
  have hp : pset G.pr s v = ∅ := congrArg Val.set (val_of_lam_eq hl)
  unfold cls eset
  rw [hl, hp, Finset.filter_empty]

end State

/-- The vertices whose class is the same at every state: the core, `c_W`, `c_X`, the e-vertices
with successor `c_W` and the β-vertices with successor `u`. -/
def isConst (G : Genome) : G.Vertex → Prop
  | .mover _ => False
  | .gate _ => False
  | .beta o => G.xt o = none
  | .eface o => G.wt o = none
  | _ => True

/-- (K3) (e), and the β-vertices whose frozen successor is `u`: these classes never change. -/
theorem IdealCycRun.cls_const (h : G.WF) (R : G.IdealCycRun σ τ T) {t b : ℕ} (ht : t ≤ T)
    (hb : b ≤ T) {v : G.Vertex} (hv : G.isConst v) :
    G.cls (nxt G.V0 σ τ t) v = G.cls (nxt G.V0 σ τ b) v := by
  have e1 := (k3 h (σ t) (τ t) (R.opt t ht) (R.isState ht)).2.2.2.2
  have e2 := (k3 h (σ b) (τ b) (R.opt b hb) (R.isState hb)).2.2.2.2
  have key : ∀ t', t' ≤ T → ∀ o, G.xt o = none →
      G.cls (nxt G.V0 σ τ t') (Vertex.beta o) = G.cls (nxt G.V0 σ τ t') Vertex.K0 := by
    intro t' ht' o hx
    have hs := R.isState ht'
    rw [cls_step h hs (R.bOnly h ht') (v := Vertex.beta o) rfl]
    have hsucc : nxt G.V0 σ τ t' (Vertex.beta o) = Vertex.K0 := by
      rw [hs.beta o]
      simp only [start0, hx]
    rw [hsucc]
  rcases v with x | o | o | o | _ | _ | _ | _ | _ | _
  · exact absurd hv id
  · exact absurd hv id
  · rw [key t ht o hv, key b hb o hv]
    exact e1.1.trans e2.1.symm
  · exact (e1.2.2.2.2.2.2 o hv).trans (e2.2.2.2.2.2.2 o hv).symm
  · exact e1.2.2.2.2.2.1.trans e2.2.2.2.2.2.1.symm
  · exact e1.2.2.2.2.1.trans e2.2.2.2.2.1.symm
  · exact e1.1.trans e2.1.symm
  · exact e1.2.1.trans e2.2.1.symm
  · exact e1.2.2.1.trans e2.2.2.1.symm
  · exact e1.2.2.2.1.trans e2.2.2.2.1.symm

/-! ### (L2) -/

/-- **(L2)** (box 208 §3). -/
theorem l2 : G.L2Statement := by
  intro h σ τ T R b t htb hbT v hF
  have ht : t ≤ T := htb.trans hbT
  have hlag : G.cls (nxt G.V0 σ τ t) v ≠ G.cls (nxt G.V0 σ τ b) v :=
    fun e => hF.1 ((ck_eq_iff h).mpr e)
  rcases v with x | o | o | o | _ | _ | _ | _ | _ | _
  · exact Or.inl ⟨x, rfl⟩
  · exact Or.inr (Or.inl ⟨o, rfl⟩)
  · cases hx : G.xt o with
    | none => exact absurd (R.cls_const h ht hbT (v := Vertex.beta o) hx) hlag
    | some y => exact Or.inr (Or.inr ⟨o, y, rfl, hx⟩)
  · exfalso
    cases hw : G.wt o with
    | none => exact hlag (R.cls_const h ht hbT (v := Vertex.eface o) hw)
    | some y =>
      by_cases hy : G.ck σ τ t (Vertex.mover y) = G.ck σ τ b (Vertex.mover y)
      · -- the successor does not lag: the e-vertex has its class of state `b`
        have e1 := (cls_eface h (R.isState ht) (R.bOnly h ht) hw).1
        have e2 := (cls_eface h (R.isState hbT) (R.bOnly h hbT) hw).1
        have hy' := (ck_eq_iff h).mp hy
        have h1 : lam G.pr (nxt G.V0 σ τ t) (Vertex.mover y) =
            lam G.pr (nxt G.V0 σ τ b) (Vertex.mover y) := congrArg Prod.fst hy'
        have h2 : G.eset (nxt G.V0 σ τ t) (Vertex.mover y) =
            G.eset (nxt G.V0 σ τ b) (Vertex.mover y) := congrArg Prod.snd hy'
        apply hlag
        rw [e1, e2, h1, h2]
      · -- the successor lags and is lower: the e-vertex is not in the front
        have hlt := (cls_eface h (R.isState ht) (R.bOnly h ht) hw).2.2
        exact absurd ((ck_lt_iff h).mpr hlt) (not_lt.mpr (hF.2 (Vertex.mover y) hy))
  all_goals exact (hlag (R.cls_const h ht hbT trivial)).elim

/-! ### (L3) -/

/-- **(L3)** (box 208 §3). -/
theorem l3 : G.L3Statement := by
  intro h σ τ T R b t htb hbT hlag
  have ht : t ≤ T := htb.trans hbT
  have hpr := pr_injective h
  have hs := R.isState ht
  have hbo := R.bOnly h ht
  have hsb := R.isState hbT
  have hbb := R.bOnly h hbT
  obtain ⟨v, hv⟩ := lc_front_exists (c := G.ck σ τ) (b := b) hlag
  -- the classes do not rise along the play of `v`
  have hplay : ∀ n, G.ck σ τ t ((nxt G.V0 σ τ t)^[n] v) ≤ G.ck σ τ t v := by
    intro n
    induction n with
    | zero => exact le_rfl
    | succ n ih =>
      rw [Function.iterate_succ_apply']
      exact ((ck_le_iff h).mpr (cls_succ_le h hs hbo _)).trans ih
  -- a lagging vertex of the play is in the front
  have hfront : ∀ n, G.ck σ τ t ((nxt G.V0 σ τ t)^[n] v) ≠ G.ck σ τ b ((nxt G.V0 σ τ t)^[n] v) →
      FrontAt (G.ck σ τ) b t ((nxt G.V0 σ τ t)^[n] v) :=
    fun n hl => ⟨hl, fun u hu => (hplay n).trans (hv.2 u hu)⟩
  by_cases hall : ∀ n, G.ck σ τ t ((nxt G.V0 σ τ t)^[n] v) ≠ G.ck σ τ b ((nxt G.V0 σ τ t)^[n] v)
  · -- (β): the whole play lags
    right
    obtain ⟨n, hn⟩ := exists_hit G.pr (nxt G.V0 σ τ t) v
    have hc := hfront n (hall n)
    rw [hn] at hc
    have hkind := l2 h σ τ T R b t htb hbT _ hc
    rcases hkind with ⟨x, hx⟩ | ⟨o, ho⟩ | ⟨o, y, ho, -⟩
    · exact absurd hx (lam_ne_mover h hs v x)
    · exact absurd ho (lam_ne_gate h hs v o)
    · refine ⟨v, o, ho, fun u hu => ?_, ?_⟩
      · obtain ⟨m, hm⟩ := hu.1
        have hfu := hfront m (hall m)
        rw [hm] at hfu
        refine ⟨hfu, ?_⟩
        rcases l2 h σ τ T R b t htb hbT _ hfu with ⟨x, hx⟩ | ⟨o', ho'⟩ | ⟨o', y', ho', -⟩
        · exact Or.inl ⟨x, hx⟩
        · exact Or.inr (Or.inl ⟨o', ho'⟩)
        · exact Or.inr (Or.inr ⟨o', ho'⟩)
      · apply cls_of_lam_eq
        have hll := lam_lam (s := nxt G.V0 σ τ t) hpr v
        rw [ho] at hll
        exact hll
  · -- (α): the last lagging vertex before the first one that does not lag
    left
    have hex : ∃ n, G.ck σ τ t ((nxt G.V0 σ τ t)^[n] v) = G.ck σ τ b ((nxt G.V0 σ τ t)^[n] v) := by
      by_contra hno
      exact hall (fun n e => hno ⟨n, e⟩)
    have hn0 := Nat.find_spec hex
    have hmin := fun m (hm : m < Nat.find hex) => Nat.find_min hex hm
    cases hk : Nat.find hex with
    | zero =>
      rw [hk] at hn0
      exact absurd hn0 hv.1
    | succ m =>
      rw [hk] at hn0
      have hzlag := hmin m (by omega)
      have hz := hfront m hzlag
      rw [Function.iterate_succ_apply'] at hn0
      -- z := the m-th vertex of the play; its successor does not lag
      generalize (nxt G.V0 σ τ t)^[m] v = z at hz hzlag hn0
      have hyeq := (ck_eq_iff h).mp hn0
      rcases l2 h σ τ T R b t htb hbT z hz with ⟨x, rfl⟩ | ⟨o, rfl⟩ | ⟨o, y, rfl, hxt⟩
      · -- a mover
        refine ⟨x, hz, ?_, ?_⟩
        · rw [← nxt_mover (σ := σ) (τ := τ) x t]
          exact hn0
        · rw [cls_step h hs hbo (v := Vertex.mover x) rfl, hyeq, nxt_mover]
      · -- a gate: (K4) at `b` pins it
        exfalso
        have hface : nxt G.V0 σ τ t (Vertex.gate o) ∈ G.E (Vertex.gate o) := hs.edge _
        have hk4 := k4 h (σ b) (τ b) (R.opt b hbT) hsb o
        have hle : G.clsLe (G.cls (nxt G.V0 σ τ b) (Vertex.gate o))
            (G.cls (nxt G.V0 σ τ b) (nxt G.V0 σ τ t (Vertex.gate o))) := by
          rcases mem_E_gate.mp hface with e | e
          · rw [e]; exact hk4.2.1
          · rw [e]; exact hk4.2.2
        rw [← hyeq, ← cls_step h hs hbo (v := Vertex.gate o) rfl] at hle
        have h1 : G.ck σ τ b (Vertex.gate o) ≤ G.ck σ τ t (Vertex.gate o) := (ck_le_iff h).mpr hle
        have h2 := R.ck_mono h htb hbT (Vertex.gate o)
        exact hzlag (le_antisymm h2 h1)
      · -- a β-vertex: its successor is frozen
        exfalso
        have e1 := cls_step h hs hbo (v := Vertex.beta o) rfl
        have e2 := cls_step h hsb hbb (v := Vertex.beta o) rfl
        rw [hsb.beta o, ← hs.beta o] at e2
        apply hzlag
        apply (ck_eq_iff h).mpr
        rw [e1, e2]
        exact hyeq

/-! ### (L5) -/

/-- **(L5)**, as its two factors (box 208 §3). -/
theorem l5 : G.L5Statement := by
  intro h σ τ T R b t htb hbT
  have ht : t ≤ T := htb.trans hbT
  constructor
  · intro v hv
    rcases l3 h σ τ T R b t htb hbT ⟨v, hv.1⟩ with ⟨x, hx, -, hcls⟩ | ⟨v0, o, hc, hcyc, hcls⟩
    · obtain ⟨k, hk⟩ := (R.isState ht).mover x
      have hσ : σ t (Vertex.mover x) = Vertex.gate ⟨x, k⟩ := by
        rw [← hk, nxt_mover]
      refine Or.inl ⟨⟨x, k⟩, ?_⟩
      rw [(ck_eq_iff h).mp (FrontAt.val_eq hv hx), hcls, hσ]
    · have hon : OnCycle (nxt G.V0 σ τ t) v0 (Vertex.beta o) := by
        rw [← hc]
        exact (lam_spec G.pr _ v0).1
      refine Or.inr ⟨o, ?_⟩
      rw [(ck_eq_iff h).mp (FrontAt.val_eq hv (hcyc _ hon).1), hcls]
  · -- a front has at most N + 2M vertices
    have hmem : ∀ v, FrontAt (G.ck σ τ) b t v →
        v ∈ Finset.univ.image (Vertex.mover : Fin G.N → G.Vertex) ∪
          (Finset.univ.image (Vertex.gate : G.Opt → G.Vertex) ∪
            Finset.univ.image (Vertex.beta : G.Opt → G.Vertex)) := by
      intro v hF
      rcases l2 h σ τ T R b t htb hbT v hF with ⟨x, rfl⟩ | ⟨o, rfl⟩ | ⟨o, y, rfl, -⟩
      · exact Finset.mem_union.mpr (Or.inl (Finset.mem_image.mpr ⟨x, Finset.mem_univ _, rfl⟩))
      · exact Finset.mem_union.mpr (Or.inr (Finset.mem_union.mpr
          (Or.inl (Finset.mem_image.mpr ⟨o, Finset.mem_univ _, rfl⟩))))
      · exact Finset.mem_union.mpr (Or.inr (Finset.mem_union.mpr
          (Or.inr (Finset.mem_image.mpr ⟨o, Finset.mem_univ _, rfl⟩))))
    have h1 : (Finset.univ.image (Vertex.mover : Fin G.N → G.Vertex)).card ≤ G.N := by
      refine Finset.card_image_le.trans ?_
      rw [Finset.card_univ, Fintype.card_fin]
    have h2 : (Finset.univ.image (Vertex.gate : G.Opt → G.Vertex)).card ≤ G.M := by
      refine Finset.card_image_le.trans ?_
      rw [Finset.card_univ]
      rfl
    have h3 : (Finset.univ.image (Vertex.beta : G.Opt → G.Vertex)).card ≤ G.M := by
      refine Finset.card_image_le.trans ?_
      rw [Finset.card_univ]
      rfl
    refine (Finset.card_le_card (fun v hv => hmem v (Finset.mem_filter.mp hv).2)).trans ?_
    refine (Finset.card_union_le _ _).trans ?_
    have h4 := Finset.card_union_le (Finset.univ.image (Vertex.gate : G.Opt → G.Vertex))
      (Finset.univ.image (Vertex.beta : G.Opt → G.Vertex))
    omega

end Genome

end

end PG
