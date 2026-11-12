/-
Box 208 §2 (K4) GATES, proved for IDEAL-CYC(G): `k4 : G.K4Statement`
(`PGLemmas/GenomeClass.lean`).  No premise.

* `le_of_underProgAt`   the converse of `underProgAt_of_le` (`PGLemmas/Mono.lean`) at a vertex
                        that is not its own cycle node: an under-progressive edge `u → w` has
                        Ξ(s u) ⊴ Ξ(w).
* `OptCounter.le_succ`  RESULTS R123 LOC-GATE in ⊴ form, for any game: an optimal counterstrategy
                        sends an Odd vertex `u` that is not its own cycle node to a successor of
                        ⊴-least value.  (From optimality against `Function.update τ u w` and
                        `underProgAt_of_opt`.)  NO-TIE is not used.
* `k4`                  the class of a gate is the class of its chosen face (`cls_step`), and the
                        chosen face is ⊴ the other one, so (K2) compares their classes.
-/
import PGLemmas.GenomeK15

namespace PG

open Classical

noncomputable section

section Generic

variable {V : Type*} [Fintype V] {pr : V → ℕ}

/-- At a vertex `u` that is not its own cycle node, an under-progressive edge `u → w` leads to a
value at least the value of the current successor of `u`. -/
theorem le_of_underProgAt (hpr : Function.Injective pr) {s : V → V} {u w : V}
    (hu : lam pr s u ≠ u) (h : UnderProgAt pr s u w) :
    Val.le pr (val pr s (s u)) (val pr s w) := by
  obtain ⟨h1, h2, -⟩ := h
  have htop : (val pr s (s u)).top = lam pr s u := lam_succ hpr u
  rcases lt_or_eq_of_le h1 with hlt | heq
  · apply Val.le_of_lt
    apply Val.lt_of_rew_lt
    show rew pr (lam pr s (s u)) < rew pr (lam pr s w)
    rw [lam_succ hpr]
    exact hlt
  · have hcls : lam pr s w = lam pr s u := (rew_injective hpr heq).symm
    have hlex := h2 hu hcls
    have hw : wt pr (val pr s u).set = wt pr (val pr s (s u)).set + dw pr (lam pr s u) u := by
      rw [val_step hpr hu, wt_ext (notMem_pset_succ hpr hu), htop]
    have hs : sl pr (val pr s u) = sl pr (val pr s (s u)) + ds pr (lam pr s u) := by
      rw [val_step hpr hu, sl_ext, htop]
    have htops : (val pr s (s u)).top = (val pr s w).top := htop.trans hcls.symm
    apply (Val.le_iff_lex hpr htops).mpr
    unfold LexLe at hlex ⊢
    omega

/-- **RESULTS R123 LOC-GATE in ⊴ form**, for any game.  Let `τ` be an optimal counterstrategy
against `σ` and `u` an Odd vertex that is not its own cycle node.  Then the value of the successor
that `τ` chooses at `u` is ⊴ the value of every successor of `u`. -/
theorem OptCounter.le_succ (hpr : Function.Injective pr) {E : V → Finset V} {V0 : Finset V}
    {σ τ : V → V} (hopt : OptCounter pr E V0 σ τ) {u w : V} (hu : u ∉ V0) (hw : w ∈ E u)
    (hne : lam pr (pair V0 σ τ) u ≠ u) :
    Val.le pr (val pr (pair V0 σ τ) (pair V0 σ τ u)) (val pr (pair V0 σ τ) w) := by
  apply le_of_underProgAt hpr hne
  apply underProgAt_of_opt hpr
  have hτ₂ : ∀ v, v ∉ V0 → Function.update τ u w v ∈ E v := by
    intro v hv
    by_cases e : v = u
    · rw [e, Function.update_self]
      exact hw
    · rw [Function.update_of_ne e]
      exact hopt.1 v hv
  have hpair : pair V0 σ (Function.update τ u w) = Function.update (pair V0 σ τ) u w := by
    funext v
    by_cases e : v = u
    · rw [e, Function.update_self, pair_of_notMem hu, Function.update_self]
    · rw [Function.update_of_ne e]
      unfold pair
      rw [Function.update_of_ne e]
  have h := hopt.2 _ hτ₂ u
  rw [hpair] at h
  exact h

end Generic

namespace Genome

variable {G : Genome}

/-- **(K4) GATES** (box 208 §2). -/
theorem k4 : G.K4Statement := by
  intro h σ τ hopt hs o
  have hpr := pr_injective h
  have hb : G.BOnly (pair G.V0 σ τ) := fun v hv hve o => b_only h hopt hs hv hve o
  have hk : pair G.V0 σ τ Vertex.K2 = Vertex.K1 := by
    rw [pair_of_notMem K2_notMem_V0]
    exact loc_k2 h hopt hs
  have hstep : G.cls (pair G.V0 σ τ) (Vertex.gate o) =
      G.cls (pair G.V0 σ τ) (pair G.V0 σ τ (Vertex.gate o)) := cls_step h hs hb rfl
  have hface : G.isCore (pair G.V0 σ τ (Vertex.gate o)) = false := by
    rcases hs.gate o with e | e <;> rw [e] <;> rfl
  have hle : ∀ w ∈ G.E (Vertex.gate o), G.isCore w = false →
      G.clsLe (G.cls (pair G.V0 σ τ) (Vertex.gate o)) (G.cls (pair G.V0 σ τ) w) := by
    intro w hw hc
    rw [hstep]
    exact k2 h _ _ hs hs hk hk _ _ hface hc
      (OptCounter.le_succ hpr hopt (gate_notMem_V0 o) hw (lam_ne_gate h hs _ o))
  refine ⟨?_, hle _ (mem_E_gate.mpr (Or.inl rfl)) rfl, hle _ (mem_E_gate.mpr (Or.inr rfl)) rfl⟩
  rcases hs.gate o with e | e
  · exact Or.inl (by rw [hstep, e])
  · exact Or.inr (by rw [hstep, e])

end Genome

end

end PG
