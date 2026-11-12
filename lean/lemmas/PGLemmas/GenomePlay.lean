/-
Plays of IDEAL-CYC(G) (`PGLemmas/Genome.lean`): facts that hold for every state, with no premise.

* `IsState`          a successor map of IDEAL-CYC(G): it follows the edges, and every Even vertex that
                     is not a mover is at its start successor; `IdealCycRun.isState`: every state of
                     a run is one;
* `cn2`              RESULTS R123 CN2: «the cycle node of v's play has priority ≥ 2.  So no gate
                     (priority 1) and no mover (priority 0) is ever a cycle node»;
* `loc_k2`           RESULTS R123 LOC-K2, first half: «At every state σ̄_t(K2) = K1»;
* `lam_K1`, `lam_K2`, `lam_K3`, `lam_K0`, `lam_cX`, `lam_cW`
                     the cycle nodes of the core and of the two self-loops (box 208 (K3) (e)).
-/
import PGLemmas.GenomeBasic
import PGLemmas.Plateau
import PGLemmas.Mono

namespace PG

open Classical

noncomputable section

section Generic

variable {V : Type*}

theorem pair_of_mem {V0 : Finset V} {σ τ : V → V} {v : V} (h : v ∈ V0) :
    pair V0 σ τ v = σ v := by
  unfold pair
  rw [ite_eq_left h]

theorem pair_of_notMem {V0 : Finset V} {σ τ : V → V} {v : V} (h : v ∉ V0) :
    pair V0 σ τ v = τ v := by
  unfold pair
  rw [ite_eq_right h]

/-- The successor of a vertex of the cycle of a play is on that cycle. -/
theorem onCycle_step {s : V → V} {v w : V} (h : OnCycle s v w) : OnCycle s v (s w) := by
  obtain ⟨⟨n, hn⟩, p, hp0, hp⟩ := h
  refine ⟨⟨n + 1, ?_⟩, p, hp0, ?_⟩
  · have e : s^[n + 1] v = s (s^[n] v) := Function.iterate_succ_apply' s n v
    rw [e, hn]
  · have e1 : s^[p] (s w) = s^[p + 1] w := (Function.iterate_succ_apply s p w).symm
    have e2 : s^[p + 1] w = s (s^[p] w) := Function.iterate_succ_apply' s p w
    rw [e1, e2, hp]

end Generic

namespace Genome

variable {G : Genome}

theorem mem_V0 {v : G.Vertex} : v ∈ G.V0 ↔ G.isOdd v = false := by
  unfold V0
  rw [Finset.mem_filter]
  exact ⟨fun h => h.2, fun h => ⟨Finset.mem_univ _, h⟩⟩

theorem mem_E_mover {x : Fin G.N} {u : G.Vertex} :
    u ∈ G.E (Vertex.mover x) ↔ ∃ k, u = Vertex.gate ⟨x, k⟩ := by
  simp only [E, Finset.mem_image, Finset.mem_univ, true_and]
  exact ⟨fun ⟨k, hk⟩ => ⟨k, hk.symm⟩, fun ⟨k, hk⟩ => ⟨k, hk.symm⟩⟩

theorem mem_E_gate {o : G.Opt} {u : G.Vertex} :
    u ∈ G.E (Vertex.gate o) ↔ u = Vertex.eface o ∨ u = Vertex.beta o := by
  simp only [E, Finset.mem_insert, Finset.mem_singleton]

/-- A state of IDEAL-CYC(G) as one successor map: it follows the edges, and «every Even vertex that
is not a mover [is] frozen at its start successor». -/
structure IsState (G : Genome) (s : G.Vertex → G.Vertex) : Prop where
  edge : ∀ v, s v ∈ G.E v
  frozen : ∀ v ∈ G.V0, (∀ x, v ≠ Vertex.mover x) → s v = G.start0 v

/-- The start successor of an Even vertex that is not a mover is one of its edges. -/
theorem start0_mem_E (v : G.Vertex) : G.start0 v ∈ G.E v := by
  rcases v with x | o | o | o | _ | _ | _ | _ | _ | _
  · exact mem_E_mover.mpr ⟨G.start x, rfl⟩
  · exact mem_E_gate.mpr (Or.inl rfl)
  · simp only [start0, E]
    cases G.xt o <;> simp
  · simp only [start0, E]
    cases G.wt o <;> simp
  all_goals simp [start0, E]

/-- Every state of a run of IDEAL-CYC(G) is a state. -/
theorem IdealCycRun.isState {σ τ : ℕ → G.Vertex → G.Vertex} {T : ℕ} (R : G.IdealCycRun σ τ T)
    {t : ℕ} (ht : t ≤ T) : G.IsState (nxt G.V0 σ τ t) := by
  refine ⟨fun v => ?_, fun v hv hnm => ?_⟩
  · unfold nxt
    by_cases hv : v ∈ G.V0
    · rw [pair_of_mem hv]
      by_cases hm : ∃ x, v = Vertex.mover x
      · obtain ⟨x, rfl⟩ := hm
        exact R.legal t ht x
      · rw [R.frozen t ht v hv (fun x e => hm ⟨x, e⟩)]
        exact start0_mem_E v
    · rw [pair_of_notMem hv]
      exact (R.opt t ht).1 v hv
  · unfold nxt
    rw [pair_of_mem hv]
    exact R.frozen t ht v hv hnm

section State

variable {s : G.Vertex → G.Vertex}

theorem IsState.mover (hs : G.IsState s) (x : Fin G.N) :
    ∃ k, s (Vertex.mover x) = Vertex.gate ⟨x, k⟩ :=
  mem_E_mover.mp (hs.edge _)

theorem IsState.gate (hs : G.IsState s) (o : G.Opt) :
    s (Vertex.gate o) = Vertex.eface o ∨ s (Vertex.gate o) = Vertex.beta o :=
  mem_E_gate.mp (hs.edge _)

theorem IsState.K1 (hs : G.IsState s) : s Vertex.K1 = Vertex.K1 :=
  hs.frozen _ (mem_V0.mpr rfl) (fun _ e => by cases e)

theorem IsState.K0 (hs : G.IsState s) : s Vertex.K0 = Vertex.K3 :=
  hs.frozen _ (mem_V0.mpr rfl) (fun _ e => by cases e)

theorem IsState.K3 (hs : G.IsState s) : s Vertex.K3 = Vertex.K2 :=
  hs.frozen _ (mem_V0.mpr rfl) (fun _ e => by cases e)

theorem IsState.cX (hs : G.IsState s) : s Vertex.cX = Vertex.cX :=
  hs.frozen _ (mem_V0.mpr rfl) (fun _ e => by cases e)

theorem IsState.cW (hs : G.IsState s) : s Vertex.cW = Vertex.cW :=
  hs.frozen _ (mem_V0.mpr rfl) (fun _ e => by cases e)

theorem IsState.K2 (hs : G.IsState s) : s Vertex.K2 = Vertex.K1 ∨ s Vertex.K2 = Vertex.K2 := by
  have h := hs.edge Vertex.K2
  simp only [E, Finset.mem_insert, Finset.mem_singleton] at h
  exact h

theorem IsState.beta (hs : G.IsState s) (o : G.Opt) :
    s (Vertex.beta o) = G.start0 (Vertex.beta o) :=
  hs.frozen _ (mem_V0.mpr rfl) (fun _ e => by cases e)

theorem IsState.eface (hs : G.IsState s) (o : G.Opt) :
    s (Vertex.eface o) = G.start0 (Vertex.eface o) :=
  hs.frozen _ (mem_V0.mpr rfl) (fun _ e => by cases e)

/-- A β and an e-vertex have priority at least 6. -/
theorem six_le_eprio (o : G.Opt) : 6 ≤ G.eprio o := by
  have := six_le_bprio o
  have := bprio_lt_eprio o o
  omega

/-- **RESULTS R123 CN2**: «the cycle node of v's play has priority ≥ 2». -/
theorem cn2 (h : G.WF) (hs : G.IsState s) (v : G.Vertex) : 2 ≤ G.prio (lam G.pr s v) := by
  have hcyc := (lam_spec G.pr s v).1
  have hmax := (lam_spec G.pr s v).2 _ (onCycle_step hcyc)
  -- the successor of the cycle node is on the cycle, so it is not more relevant
  have hnot : ¬ G.prio (lam G.pr s v) < G.prio (s (lam G.pr s v)) :=
    fun hlt => absurd (pr_lt_of_prio_lt h hlt) (not_lt.mpr hmax)
  generalize lam G.pr s v = w at hnot ⊢
  rcases w with x | o | o | o | _ | _ | _ | _ | _ | _
  · exfalso
    obtain ⟨k, hk⟩ := hs.mover x
    rw [hk] at hnot
    exact hnot (by simp [prio])
  · exfalso
    rcases hs.gate o with hk | hk
    · rw [hk] at hnot
      have := six_le_eprio o
      exact hnot (by simp only [prio]; omega)
    · rw [hk] at hnot
      have := six_le_bprio o
      exact hnot (by simp only [prio]; omega)
  · have := six_le_bprio o
    simp only [prio]
    omega
  · have := six_le_eprio o
    simp only [prio]
    omega
  · simp [prio]
  · have := two_le_pmax (G := G)
    have := pmax_lt_top (G := G)
    simp only [prio]
    omega
  · simp only [prio]
    omega
  · simp [prio]
  · simp [prio]
  · simp only [prio]
    omega

/-- No mover is a cycle node. -/
theorem lam_ne_mover (h : G.WF) (hs : G.IsState s) (v : G.Vertex) (x : Fin G.N) :
    lam G.pr s v ≠ Vertex.mover x := by
  intro e
  have := cn2 h hs v
  rw [e] at this
  simp [prio] at this

/-- No gate is a cycle node. -/
theorem lam_ne_gate (h : G.WF) (hs : G.IsState s) (v : G.Vertex) (o : G.Opt) :
    lam G.pr s v ≠ Vertex.gate o := by
  intro e
  have := cn2 h hs v
  rw [e] at this
  simp [prio] at this

theorem lam_K1 (hs : G.IsState s) : lam G.pr s Vertex.K1 = Vertex.K1 := lam_of_fixed hs.K1

theorem lam_cX (hs : G.IsState s) : lam G.pr s Vertex.cX = Vertex.cX := lam_of_fixed hs.cX

theorem lam_cW (hs : G.IsState s) : lam G.pr s Vertex.cW = Vertex.cW := lam_of_fixed hs.cW

end State

/-- **RESULTS R123 LOC-K2**, first half: «At every state σ̄_t(K2) = K1».  For any optimal
counterstrategy `τ` against `σ` whose pair is a state of IDEAL-CYC(G). -/
theorem loc_k2 (h : G.WF) {σ τ : G.Vertex → G.Vertex} (hopt : OptCounter G.pr G.E G.V0 σ τ)
    (hs : G.IsState (pair G.V0 σ τ)) : τ Vertex.K2 = Vertex.K1 := by
  have hpr := pr_injective h
  have hK2 : (Vertex.K2 : G.Vertex) ∉ G.V0 := fun hm => by
    have := mem_V0.mp hm
    simp [isOdd] at this
  have hK1 : (Vertex.K1 : G.Vertex) ∈ G.V0 := mem_V0.mpr rfl
  rcases hs.K2 with hk | hk
  · rw [pair_of_notMem hK2] at hk
    exact hk
  · exfalso
    -- under `τ`, `K2` is its own cycle node
    have hv : val G.pr (pair G.V0 σ τ) Vertex.K2 = ⟨Vertex.K2, ∅, 0⟩ :=
      val_of_lam_eq (lam_of_fixed hk)
    -- Odd's other strategy: `K2 → K1`
    have hτ₂ : ∀ u, u ∉ G.V0 → Function.update τ Vertex.K2 Vertex.K1 u ∈ G.E u := by
      intro u hu
      by_cases e : u = Vertex.K2
      · subst e
        rw [Function.update_self]
        simp [E]
      · rw [Function.update_of_ne e]
        exact hopt.1 u hu
    have hle := hopt.2 _ hτ₂ Vertex.K2
    -- under it, the cycle node of `K2` is `K1`
    have hs₂K2 : pair G.V0 σ (Function.update τ Vertex.K2 Vertex.K1) Vertex.K2 = Vertex.K1 := by
      rw [pair_of_notMem hK2, Function.update_self]
    have hs₂K1 : pair G.V0 σ (Function.update τ Vertex.K2 Vertex.K1) Vertex.K1 = Vertex.K1 := by
      have e := hs.K1
      rw [pair_of_mem hK1] at e ⊢
      exact e
    have hl : lam G.pr (pair G.V0 σ (Function.update τ Vertex.K2 Vertex.K1)) Vertex.K2
        = Vertex.K1 := by
      have e := lam_succ (s := pair G.V0 σ (Function.update τ Vertex.K2 Vertex.K1)) hpr Vertex.K2
      rw [hs₂K2, lam_of_fixed hs₂K1] at e
      exact e.symm
    -- but `K1` has the smaller reward
    have hlt : G.pr Vertex.K2 < G.pr Vertex.K1 := pr_lt_of_prio_lt h (by simp [prio])
    have ho1 : ¬ Even (G.pr Vertex.K1) := fun he => by
      have := even_pr.mp he
      simp [prio] at this
      exact absurd this (by decide)
    have ho2 : ¬ Even (G.pr Vertex.K2) := fun he => by
      have := even_pr.mp he
      simp [prio] at this
      exact absurd this (by decide)
    have hrew : rew G.pr Vertex.K1 < rew G.pr Vertex.K2 := by
      rw [rew_of_odd ho1, rew_of_odd ho2]
      omega
    rw [hv] at hle
    have htop : (val G.pr (pair G.V0 σ (Function.update τ Vertex.K2 Vertex.K1)) Vertex.K2).top
        = Vertex.K1 := hl
    rcases hle with hlt' | heq
    · rcases hlt' with h1 | ⟨h1, -⟩ | ⟨h1, -⟩ | ⟨h1, -⟩
      · rw [htop] at h1
        exact absurd hrew (not_lt.mpr h1.le)
      · rw [htop] at h1
        cases h1
      · rw [htop] at h1
        cases h1
      · rw [htop] at h1
        cases h1
    · have := congrArg Val.top heq
      rw [htop] at this
      cases this

section Core

variable {s : G.Vertex → G.Vertex}

theorem lam_K2 (h : G.WF) (hs : G.IsState s) (hk : s Vertex.K2 = Vertex.K1) :
    lam G.pr s Vertex.K2 = Vertex.K1 := by
  have e := lam_succ (s := s) (pr_injective h) Vertex.K2
  rw [hk, lam_K1 hs] at e
  exact e.symm

theorem lam_K3 (h : G.WF) (hs : G.IsState s) (hk : s Vertex.K2 = Vertex.K1) :
    lam G.pr s Vertex.K3 = Vertex.K1 := by
  have e := lam_succ (s := s) (pr_injective h) Vertex.K3
  rw [hs.K3, lam_K2 h hs hk] at e
  exact e.symm

theorem lam_K0 (h : G.WF) (hs : G.IsState s) (hk : s Vertex.K2 = Vertex.K1) :
    lam G.pr s Vertex.K0 = Vertex.K1 := by
  have e := lam_succ (s := s) (pr_injective h) Vertex.K0
  rw [hs.K0, lam_K3 h hs hk] at e
  exact e.symm

end Core

/-- `σ̄_t(K2) = K1` at every state of a run. -/
theorem IdealCycRun.k2 {σ τ : ℕ → G.Vertex → G.Vertex} {T : ℕ} (h : G.WF)
    (R : G.IdealCycRun σ τ T) {t : ℕ} (ht : t ≤ T) :
    nxt G.V0 σ τ t Vertex.K2 = Vertex.K1 := by
  have hK2 : (Vertex.K2 : G.Vertex) ∉ G.V0 := fun hm => by
    have := mem_V0.mp hm
    simp [isOdd] at this
  have := loc_k2 h (R.opt t ht) (R.isState ht)
  unfold nxt
  rw [pair_of_notMem hK2]
  exact this

end Genome

end

end PG
