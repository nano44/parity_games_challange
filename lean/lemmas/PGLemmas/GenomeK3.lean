/-
Box 208 §2 (K3) ALONG THE PLAY, proved for IDEAL-CYC(G): `k3 : G.K3Statement`
(`PGLemmas/GenomeClass.lean`).  No premise: B-ONLY is `b_only`, LOC-K2 is `loc_k2`.

The lemmas are stated for a successor map `s` with the B-ONLY property (`BOnly`), so that they
can be used at every state of a run.
-/
import PGLemmas.GenomeClass

namespace PG

open Classical
open scoped symmDiff

noncomputable section

namespace Genome

variable {G : Genome} {s : G.Vertex → G.Vertex}

/-- The B-ONLY property of a successor map (RESULTS R123 B-ONLY; `b_only`). -/
def BOnly (G : Genome) (s : G.Vertex → G.Vertex) : Prop :=
  ∀ v, v ≠ Vertex.cW → (∀ o, v = Vertex.eface o → G.wt o ≠ none) →
    ∀ o, G.pr (lam G.pr s v) < G.pr (Vertex.eface o)

theorem isE_iff {u : G.Vertex} : G.isE u = true ↔ ∃ o, u = Vertex.eface o := by
  rcases u with x | o | o | o | _ | _ | _ | _ | _ | _ <;> simp [isE]

/-- Off its cycle node, a vertex that is not an e-vertex has the e-set of its successor. -/
theorem eset_step (hpr : Function.Injective G.pr) {v : G.Vertex} (hne : lam G.pr s v ≠ v)
    (hv : G.isE v = false) : G.eset s v = G.eset s (s v) := by
  unfold eset
  have e : pset G.pr s v = (ext G.pr v (val G.pr s (s v))).set :=
    congrArg Val.set (val_step hpr hne)
  rw [e]
  unfold ext
  dsimp only
  split_ifs with hlt
  · rw [Finset.filter_insert, ite_eq_right (by rw [hv]; exact Bool.false_ne_true)]
    rfl
  · rfl

/-- Off its cycle node, a vertex that is not more relevant than its cycle node has the e-set of
its successor. -/
theorem eset_step_ge (hpr : Function.Injective G.pr) {v : G.Vertex} (hne : lam G.pr s v ≠ v)
    (hge : ¬ G.pr (lam G.pr s v) < G.pr v) : G.eset s v = G.eset s (s v) := by
  unfold eset
  have e : pset G.pr s v = (ext G.pr v (val G.pr s (s v))).set :=
    congrArg Val.set (val_step hpr hne)
  rw [e]
  unfold ext
  dsimp only
  have hc : ¬ G.pr (val G.pr s (s v)).top < G.pr v := by
    show ¬ G.pr (lam G.pr s (s v)) < G.pr v
    rw [lam_succ hpr]
    exact hge
  rw [ite_eq_right hc]
  rfl

/-- An e-vertex more relevant than its cycle node adds itself to the e-set of its successor. -/
theorem eset_step_e (hpr : Function.Injective G.pr) {v : G.Vertex} (hne : lam G.pr s v ≠ v)
    (hv : G.isE v = true) (hlt : G.pr (lam G.pr s v) < G.pr v) :
    G.eset s v = insert v (G.eset s (s v)) := by
  unfold eset
  have e : pset G.pr s v = (ext G.pr v (val G.pr s (s v))).set :=
    congrArg Val.set (val_step hpr hne)
  rw [e]
  unfold ext
  dsimp only
  have hc : G.pr (val G.pr s (s v)).top < G.pr v := by
    show G.pr (lam G.pr s (s v)) < G.pr v
    rw [lam_succ hpr]
    exact hlt
  rw [ite_eq_left hc]
  ext u
  simp only [Finset.mem_insert, Finset.mem_filter]
  constructor
  · rintro ⟨rfl | hu, hE⟩
    · exact Or.inl rfl
    · exact Or.inr ⟨hu, hE⟩
  · rintro (rfl | ⟨hu, hE⟩)
    · exact ⟨Or.inl rfl, hv⟩
    · exact ⟨Or.inr hu, hE⟩

/-- (K3) (b): no e-vertex lies on the cycle of a play. -/
theorem no_e_cycle (h : G.WF) (hs : G.IsState s) (hb : G.BOnly s) (v : G.Vertex) (o : G.Opt) :
    ¬ OnCycle s v (Vertex.eface o) := by
  intro hcyc
  have hpr := pr_injective h
  have hmax : G.pr (Vertex.eface o) ≤ G.pr (lam G.pr s v) := (lam_spec G.pr s v).2 _ hcyc
  obtain ⟨⟨n, hn⟩, p, hp0, hp⟩ := hcyc
  -- its successor is not `c_W`: from `c_W` the play never comes back
  have hw : G.wt o ≠ none := by
    intro hw
    have hsucc : s (Vertex.eface o) = Vertex.cW := by
      rw [hs.eface o]
      simp only [start0, hw]
    obtain ⟨p', rfl⟩ : ∃ p', p = p' + 1 := ⟨p - 1, by omega⟩
    rw [Function.iterate_succ_apply, hsucc, Function.iterate_fixed hs.cW] at hp
    cases hp
  have h1 := hb (Vertex.eface o) (fun e => by cases e)
    (fun o' e => by cases e; exact hw) o
  have h3 : lam G.pr s (Vertex.eface o) = lam G.pr s v := by
    rw [← hn]
    exact lam_iterate hpr v n
  rw [h3] at h1
  omega

/-- (K3) (c): a vertex that is not an e-vertex has the class of its successor. -/
theorem cls_step (h : G.WF) (hs : G.IsState s) (hb : G.BOnly s) {v : G.Vertex}
    (hv : G.isE v = false) : G.cls s v = G.cls s (s v) := by
  have hpr := pr_injective h
  unfold cls
  rw [lam_succ (s := s) hpr v]
  congr 1
  by_cases hne : lam G.pr s v = v
  · -- `v` is its own cycle node: both e-sets are empty
    have hv0 : pset G.pr s v = ∅ := congrArg Val.set (val_of_lam_eq hne)
    have hl : G.eset s v = ∅ := by
      unfold eset
      rw [hv0, Finset.filter_empty]
    rw [hl]
    symm
    unfold eset
    rw [Finset.filter_eq_empty_iff]
    intro u hu hE
    -- `u` is on the cycle of `v`
    obtain ⟨-, j, -, hju⟩ := mem_pset.mp hu
    obtain ⟨-, p, hp0, hp⟩ := (lam_spec G.pr s v).1
    rw [hne] at hp
    have e1 : s^[j + 1] v = u := by
      rw [Function.iterate_succ_apply]
      exact hju
    have e2 : s^[p] (s^[j + 1] v) = s^[j + 1] (s^[p] v) := by
      rw [← Function.iterate_add_apply, ← Function.iterate_add_apply, Nat.add_comm]
    have hcyc : OnCycle s v u := by
      refine ⟨⟨j + 1, e1⟩, p, hp0, ?_⟩
      rw [← e1, e2, hp]
    obtain ⟨o, rfl⟩ := isE_iff.mp hE
    exact no_e_cycle h hs hb v o hcyc
  · exact eset_step hpr hne hv

/-- (K3) (d): an e-vertex whose successor is a mover `y` has the class `(Λ(y), {e} ∪ E(y))`,
with `e ∉ E(y)`; so its class is above the class of `y`. -/
theorem cls_eface (h : G.WF) (hs : G.IsState s) (hb : G.BOnly s) {o : G.Opt} {y : Fin G.N}
    (hw : G.wt o = some y) :
    G.cls s (Vertex.eface o) =
        (lam G.pr s (Vertex.mover y), insert (Vertex.eface o) (G.eset s (Vertex.mover y))) ∧
      Vertex.eface o ∉ G.eset s (Vertex.mover y) ∧
      G.clsLt (G.cls s (Vertex.mover y)) (G.cls s (Vertex.eface o)) := by
  have hpr := pr_injective h
  have hsucc : s (Vertex.eface o) = Vertex.mover y := by
    rw [hs.eface o]
    simp only [start0, hw]
  have hlt := hb (Vertex.eface o) (fun e => by cases e)
    (fun o' e => by cases e; rw [hw]; exact fun e' => by cases e') o
  have hne : lam G.pr s (Vertex.eface o) ≠ Vertex.eface o := fun e => by
    rw [e] at hlt
    exact lt_irrefl _ hlt
  have hl : lam G.pr s (Vertex.eface o) = lam G.pr s (Vertex.mover y) := by
    rw [← hsucc]
    exact (lam_succ (s := s) hpr _).symm
  have hes : G.eset s (Vertex.eface o) = insert (Vertex.eface o) (G.eset s (Vertex.mover y)) := by
    rw [eset_step_e hpr hne rfl hlt, hsucc]
  have hnm : Vertex.eface o ∉ G.eset s (Vertex.mover y) := by
    intro hm
    have hnot := notMem_pset_succ (s := s) hpr hne
    rw [hsucc] at hnot
    exact hnot (Finset.mem_filter.mp hm).1
  refine ⟨?_, hnm, ?_⟩
  · unfold cls
    rw [hl, hes]
  · unfold clsLt cls
    dsimp only
    refine Or.inr ⟨hl.symm, Vertex.eface o, ?_, ?_, ?_⟩
    · rw [hes, Finset.mem_symmDiff]
      exact Or.inr ⟨Finset.mem_insert_self _ _, hnm⟩
    · intro x hx
      rw [hes, Finset.mem_symmDiff] at hx
      rcases hx with ⟨h1, h2⟩ | ⟨h1, h2⟩
      · exact absurd (Finset.mem_insert_of_mem h1) h2
      · rcases Finset.mem_insert.mp h1 with rfl | h1
        · exact le_rfl
        · exact absurd h1 h2
    · rw [hes]
      exact Finset.mem_insert_self _ _

/-- A self-loop has the class `(v, ∅)`. -/
theorem cls_fixed {v : G.Vertex} (hv : s v = v) : G.cls s v = (v, ∅) := by
  have hl := lam_of_fixed (pr := G.pr) hv
  have hp : pset G.pr s v = ∅ := congrArg Val.set (val_of_lam_eq hl)
  unfold cls eset
  rw [hl, hp, Finset.filter_empty]

/-- (K3) (e): an e-vertex whose successor is `c_W` has the class `(c_W, ∅)`. -/
theorem cls_eface_none (h : G.WF) (hs : G.IsState s) {o : G.Opt} (hw : G.wt o = none) :
    G.cls s (Vertex.eface o) = (Vertex.cW, ∅) := by
  have hpr := pr_injective h
  have hsucc : s (Vertex.eface o) = Vertex.cW := by
    rw [hs.eface o]
    simp only [start0, hw]
  have hl : lam G.pr s (Vertex.eface o) = Vertex.cW := by
    have e := lam_succ (s := s) hpr (Vertex.eface o)
    rw [hsucc, lam_cW hs] at e
    exact e.symm
  have hne : lam G.pr s (Vertex.eface o) ≠ Vertex.eface o := by
    rw [hl]
    exact fun e => by cases e
  have hge : ¬ G.pr (lam G.pr s (Vertex.eface o)) < G.pr (Vertex.eface o) := by
    rw [hl]
    exact not_lt.mpr (le_of_lt (pr_lt_of_prio_lt h (eprio_lt_top o)))
  have hc := cls_fixed (G := G) hs.cW
  unfold cls at hc ⊢
  rw [hl, eset_step_ge hpr hne hge, hsucc]
  exact congrArg (fun e => (Vertex.cW, e)) (congrArg Prod.snd hc)

/-- **(K3) ALONG THE PLAY** (box 208 §2). -/
theorem k3 : G.K3Statement := by
  intro h σ τ hopt hs
  have hpr := pr_injective h
  have hb : G.BOnly (pair G.V0 σ τ) := fun v hv hve o => b_only h hopt hs hv hve o
  have hk : pair G.V0 σ τ Vertex.K2 = Vertex.K1 := by
    rw [pair_of_notMem K2_notMem_V0]
    exact loc_k2 h hopt hs
  refine ⟨fun v => (lam_succ hpr v).symm, no_e_cycle h hs hb, fun v hv => cls_step h hs hb hv,
    fun o y hw => cls_eface h hs hb hw, ?_⟩
  have c1 : G.cls (pair G.V0 σ τ) Vertex.K1 = (Vertex.K1, ∅) := cls_fixed hs.K1
  have c2 : G.cls (pair G.V0 σ τ) Vertex.K2 = (Vertex.K1, ∅) := by
    rw [cls_step h hs hb rfl, hk]
    exact c1
  have c3 : G.cls (pair G.V0 σ τ) Vertex.K3 = (Vertex.K1, ∅) := by
    rw [cls_step h hs hb rfl, hs.K3]
    exact c2
  have c0 : G.cls (pair G.V0 σ τ) Vertex.K0 = (Vertex.K1, ∅) := by
    rw [cls_step h hs hb rfl, hs.K0]
    exact c3
  exact ⟨c0, c1, c2, c3, cls_fixed hs.cW, cls_fixed hs.cX, fun o hw => cls_eface_none h hs hw⟩

end Genome

end

end PG
