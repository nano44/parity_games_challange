/-
Box 208 §2 (K1) MONOTONE and (K5) HOWARD DOMINATES, proved for IDEAL-CYC(G):
`k1 : G.K1Statement`, `k5 : G.K5Statement` (`PGLemmas/GenomeClass.lean`).  No premise.

* `IdealCycRun.f1`  F1 (RESULTS R15 (a)) along a run: Ω_t ⊴ Ω_(t+1) pointwise (`f1_howard`).
* `k1`  off the core: F1 and (K2); on the core: the constant classes of (K3) (e).
* `k5`  with y′ the new successor of the mover x: Ω_t(y) ⊴ Ω_t(y′) (Howard) ⊴ Ω_(t+1)(y′) (F1), so
        class_t(y) ≤ class_(t+1)(y′) by (K2), and class_(t+1)(y′) = class_(t+1)(x) by (K3) (c).
        (Box 208 goes through DOM and CN2; this route needs neither.)
-/
import PGLemmas.GenomeK2
import PGLemmas.TwoPlayer

namespace PG

open Classical

noncomputable section

namespace Genome

variable {G : Genome}

/-- The movers, as a finite set. -/
def Mov (G : Genome) : Finset G.Vertex := Finset.univ.filter (fun v => ∃ x, v = Vertex.mover x)

theorem mem_Mov {v : G.Vertex} : v ∈ G.Mov ↔ ∃ x, v = Vertex.mover x := by
  unfold Mov
  rw [Finset.mem_filter]
  exact ⟨fun h => h.2, fun h => ⟨Finset.mem_univ _, h⟩⟩

/-- F1 along a run of IDEAL-CYC(G): no value falls in a step. -/
theorem IdealCycRun.f1 {σ τ : ℕ → G.Vertex → G.Vertex} {T : ℕ} (h : G.WF)
    (R : G.IdealCycRun σ τ T) {t : ℕ} (ht : t < T) (v : G.Vertex) :
    Val.le G.pr (val G.pr (nxt G.V0 σ τ t) v) (val G.pr (nxt G.V0 σ τ (t + 1)) v) := by
  have hpr := pr_injective h
  exact f1_howard hpr (Mov := G.Mov) (σ := σ t) (τ := τ t) (σ' := σ (t + 1)) (τ' := τ (t + 1))
    (R.opt t ht.le) (R.opt (t + 1) (by omega)).1
    (fun v hv hm => by
      have hnm : ∀ x, v ≠ Vertex.mover x := fun x e => hm (mem_Mov.mpr ⟨x, e⟩)
      rw [R.frozen (t + 1) (by omega) v hv hnm, R.frozen t ht.le v hv hnm])
    (fun x hx => by
      obtain ⟨x', rfl⟩ := mem_Mov.mp hx
      exact R.legal t ht.le x')
    (fun x hx => by
      obtain ⟨x', rfl⟩ := mem_Mov.mp hx
      exact R.howard t ht x') v

/-- **(K1) MONOTONE** (box 208 §2). -/
theorem k1 : G.K1Statement := by
  intro h σ τ T R t ht v
  have hs := R.isState ht.le
  have hs' := R.isState (t := t + 1) (by omega)
  have hk := R.k2 h ht.le
  have hk' := R.k2 h (t := t + 1) (by omega)
  by_cases hc : G.isCore v = false
  · exact k2 h _ _ hs hs' hk hk' v v hc hc (R.f1 h ht v)
  · refine Or.inr ?_
    have e1 := (k3 h (σ t) (τ t) (R.opt t ht.le) hs).2.2.2.2
    have e2 := (k3 h (σ (t + 1)) (τ (t + 1)) (R.opt (t + 1) (by omega)) hs').2.2.2.2
    rcases v with x | o | o | o | _ | _ | _ | _ | _ | _ <;> simp [isCore] at hc
    · exact e1.1.trans e2.1.symm
    · exact e1.2.1.trans e2.2.1.symm
    · exact e1.2.2.1.trans e2.2.2.1.symm
    · exact e1.2.2.2.1.trans e2.2.2.2.1.symm

/-- **(K5) HOWARD DOMINATES** (box 208 §2). -/
theorem k5 : G.K5Statement := by
  intro h σ τ T R t ht x y hy
  have hpr := pr_injective h
  have hs := R.isState ht.le
  have hs' := R.isState (t := t + 1) (by omega)
  have hk := R.k2 h ht.le
  have hk' := R.k2 h (t := t + 1) (by omega)
  have hb' : G.BOnly (nxt G.V0 σ τ (t + 1)) :=
    fun v hv hve o => b_only h (R.opt (t + 1) (by omega)) hs' hv hve o
  obtain ⟨k', hk''⟩ := hs'.mover x
  obtain ⟨k0, rfl⟩ := mem_E_mover.mp hy
  -- Howard: the new successor is a ⊴-best successor at `t`; F1: its value does not fall
  have hbest := (R.howard t ht x).2.1 _ hy
  rw [hk''] at hbest
  have hF := R.f1 h ht (Vertex.gate ⟨x, k'⟩)
  have hle := Val.le_trans hpr hbest hF
  have hcl := k2 h _ _ hs hs' hk hk' _ _ rfl rfl hle
  rw [cls_step h hs' hb' (v := Vertex.mover x) rfl, hk'']
  exact hcl

end Genome

end

end PG
