/-
RESULTS R123 B-ONLY for IDEAL-CYC(G), with no premise:
«In IDEAL-CYC(G), for every genome G, every state t and every vertex v other than c_W and the
e-vertices whose successor is c_W, Λ_t(v) is less relevant than every e-vertex (it is a β-vertex,
K1, K2 or the unused loop).»

Proof (mine; the landed proof is in R123's packet, not opened here).  Let Odd answer by the
ALL-β strategy `tauBeta` (every gate on its Ξ-face, K2 → K1).  Under it no e-vertex has a
predecessor, so no e-vertex is on a cycle, and only c_W and the e-vertices with successor c_W
reach c_W; so the cycle node of every other vertex is a β, c_X or K1 (`lam_tauBeta`), of smaller
reward than every e-vertex.  The optimal counterstrategy gives no vertex a larger value, so the
reward of its cycle node is below that of every e-vertex too.  A vertex at least as relevant as an
e-vertex is an e-vertex, c_W, K0 (even: reward too large) or K3 (never a cycle node) by E-DOM.
-/
import PGLemmas.GenomePlay

namespace PG

open Classical

noncomputable section

/-- `⊴` on node valuations does not lower the reward of the cycle component. -/
theorem Val.rew_top_le {V : Type*} {pr : V → ℕ} {x y : Val V} (h : Val.le pr x y) :
    rew pr x.top ≤ rew pr y.top := by
  rcases h with h | rfl
  · rcases h with h | ⟨h, -⟩ | ⟨h, -⟩ | ⟨h, -⟩
    · exact h.le
    all_goals rw [h]
  · exact le_rfl

/-- A reward is at most the priority. -/
theorem rew_le {V : Type*} {pr : V → ℕ} (u : V) : rew pr u ≤ (pr u : ℤ) := by
  by_cases h : Even (pr u)
  · rw [rew_of_even h]
  · rw [rew_of_odd h]
    omega

namespace Genome

variable {G : Genome}

/-- Odd's all-β strategy: every gate on its Ξ-face, `K2 → K1`. -/
def tauBeta (G : Genome) : G.Vertex → G.Vertex
  | .gate o => .beta o
  | .K2 => .K1
  | v => v

theorem tauBeta_legal (u : G.Vertex) (hu : u ∉ G.V0) : G.tauBeta u ∈ G.E u := by
  have hodd : G.isOdd u = true := by
    by_contra hne
    exact hu (mem_V0.mpr (by simpa using hne))
  rcases u with x | o | o | o | _ | _ | _ | _ | _ | _ <;> simp [isOdd] at hodd
  · exact mem_E_gate.mpr (Or.inr rfl)
  · simp [tauBeta, E]

theorem gate_notMem_V0 (o : G.Opt) : (Vertex.gate o : G.Vertex) ∉ G.V0 := fun hm => by
  have := mem_V0.mp hm
  simp [isOdd] at this

theorem K2_notMem_V0 : (Vertex.K2 : G.Vertex) ∉ G.V0 := fun hm => by
  have := mem_V0.mp hm
  simp [isOdd] at this

/-- With Even's part of a state and the all-β strategy, the pair is again a state. -/
theorem isState_tauBeta {σ τ : G.Vertex → G.Vertex} (hs : G.IsState (pair G.V0 σ τ)) :
    G.IsState (pair G.V0 σ G.tauBeta) := by
  refine ⟨fun v => ?_, fun v hv hnm => ?_⟩
  · by_cases hv : v ∈ G.V0
    · have := hs.edge v
      rw [pair_of_mem hv] at this ⊢
      exact this
    · rw [pair_of_notMem hv]
      exact tauBeta_legal v hv
  · have := hs.frozen v hv hnm
    rw [pair_of_mem hv] at this ⊢
    exact this

section AllBeta

variable {s : G.Vertex → G.Vertex}

/-- Under a state with every gate on its Ξ-face, no vertex has an e-vertex as successor. -/
theorem succ_ne_eface (hs : G.IsState s) (hg : ∀ o, s (Vertex.gate o) = Vertex.beta o)
    (hk : s Vertex.K2 = Vertex.K1) (v : G.Vertex) (o : G.Opt) : s v ≠ Vertex.eface o := by
  rcases v with x | o' | o' | o' | _ | _ | _ | _ | _ | _
  · obtain ⟨k, hk'⟩ := hs.mover x
    rw [hk']
    exact fun e => by cases e
  · rw [hg o']
    exact fun e => by cases e
  · rw [hs.beta o']
    simp only [start0]
    cases G.xt o' <;> exact fun e => by cases e
  · rw [hs.eface o']
    simp only [start0]
    cases G.wt o' <;> exact fun e => by cases e
  · rw [hs.cX]
    exact fun e => by cases e
  · rw [hs.cW]
    exact fun e => by cases e
  · rw [hs.K0]
    exact fun e => by cases e
  · rw [hs.K1]
    exact fun e => by cases e
  · rw [hk]
    exact fun e => by cases e
  · rw [hs.K3]
    exact fun e => by cases e

/-- Under such a state, the vertices with successor `c_W` are `c_W` and the e-vertices without
W-target. -/
theorem succ_eq_cW (hs : G.IsState s) (hg : ∀ o, s (Vertex.gate o) = Vertex.beta o)
    (hk : s Vertex.K2 = Vertex.K1) {v : G.Vertex} (hv : s v = Vertex.cW) :
    v = Vertex.cW ∨ ∃ o, v = Vertex.eface o ∧ G.wt o = none := by
  rcases v with x | o' | o' | o' | _ | _ | _ | _ | _ | _
  · obtain ⟨k, hk'⟩ := hs.mover x
    rw [hk'] at hv
    cases hv
  · rw [hg o'] at hv
    cases hv
  · rw [hs.beta o'] at hv
    simp only [start0] at hv
    cases hx : G.xt o' <;> rw [hx] at hv <;> cases hv
  · right
    refine ⟨o', rfl, ?_⟩
    rw [hs.eface o'] at hv
    simp only [start0] at hv
    cases hw : G.wt o' with
    | none => rfl
    | some y =>
      rw [hw] at hv
      cases hv
  · rw [hs.cX] at hv
    cases hv
  · exact Or.inl rfl
  · rw [hs.K0] at hv
    cases hv
  · rw [hs.K1] at hv
    cases hv
  · rw [hk] at hv
    cases hv
  · rw [hs.K3] at hv
    cases hv

/-- Under such a state, only `c_W` and the e-vertices without W-target reach `c_W`. -/
theorem reach_cW (hs : G.IsState s) (hg : ∀ o, s (Vertex.gate o) = Vertex.beta o)
    (hk : s Vertex.K2 = Vertex.K1) (n : ℕ) (v : G.Vertex) (hv : s^[n] v = Vertex.cW) :
    v = Vertex.cW ∨ ∃ o, v = Vertex.eface o ∧ G.wt o = none := by
  induction n generalizing v with
  | zero => exact Or.inl hv
  | succ n ih =>
    have e : s^[n + 1] v = s^[n] (s v) := Function.iterate_succ_apply s n v
    rw [e] at hv
    rcases ih (s v) hv with h1 | ⟨o, h1, -⟩
    · exact succ_eq_cW hs hg hk h1
    · exact absurd h1 (succ_ne_eface hs hg hk v o)

/-- Under a state with every gate on its Ξ-face and `K2 → K1`, the cycle node of every vertex
other than `c_W` and the e-vertices without W-target is a β, `c_X` or `K1`. -/
theorem lam_allBeta (h : G.WF) (hs : G.IsState s) (hg : ∀ o, s (Vertex.gate o) = Vertex.beta o)
    (hk : s Vertex.K2 = Vertex.K1) {v : G.Vertex} (hv : v ≠ Vertex.cW)
    (hve : ∀ o, v = Vertex.eface o → G.wt o ≠ none) :
    (∃ o, lam G.pr s v = Vertex.beta o) ∨ lam G.pr s v = Vertex.cX ∨
      lam G.pr s v = Vertex.K1 := by
  have hpr := pr_injective h
  obtain ⟨⟨n, hn⟩, p, hp0, hp⟩ := (lam_spec G.pr s v).1
  have hll := lam_lam (s := s) hpr v
  have hm := lam_ne_mover h hs v
  have hgt := lam_ne_gate h hs v
  generalize lam G.pr s v = w at hn hp hll hm hgt ⊢
  rcases w with x | o | o | o | _ | _ | _ | _ | _ | _
  · exact absurd rfl (hm x)
  · exact absurd rfl (hgt o)
  · exact Or.inl ⟨o, rfl⟩
  · -- an e-vertex has no predecessor, so it is on no cycle
    exfalso
    obtain ⟨p', rfl⟩ : ∃ p', p = p' + 1 := ⟨p - 1, by omega⟩
    have e : s^[p' + 1] (Vertex.eface o) = s (s^[p'] (Vertex.eface o)) :=
      Function.iterate_succ_apply' s p' _
    rw [e] at hp
    exact succ_ne_eface hs hg hk _ o hp
  · exact Or.inr (Or.inl rfl)
  · exfalso
    rcases reach_cW hs hg hk n v hn with h1 | ⟨o, h1, h2⟩
    · exact hv h1
    · exact hve o h1 h2
  · exfalso
    rw [lam_K0 h hs hk] at hll
    cases hll
  · exact Or.inr (Or.inr rfl)
  · exfalso
    rw [lam_K2 h hs hk] at hll
    cases hll
  · exfalso
    rw [lam_K3 h hs hk] at hll
    cases hll

end AllBeta

theorem even_pr_eface (o : G.Opt) : Even (G.pr (Vertex.eface o)) :=
  even_pr.mpr (Nat.even_iff.mpr (eprio_even o))

/-- A vertex less relevant than an e-vertex has a smaller reward. -/
theorem rew_lt_eface {u : G.Vertex} {o : G.Opt} (hu : G.pr u < G.pr (Vertex.eface o)) :
    rew G.pr u < rew G.pr (Vertex.eface o) := by
  have := rew_le (pr := G.pr) u
  rw [rew_of_even (even_pr_eface o)]
  omega

/-- **RESULTS R123 B-ONLY.**  For an optimal counterstrategy `τ` against `σ` whose pair is a state
of IDEAL-CYC(G), and every vertex `v` other than `c_W` and the e-vertices whose successor is
`c_W`: the cycle node of `v` is less relevant than every e-vertex. -/
theorem b_only (h : G.WF) {σ τ : G.Vertex → G.Vertex} (hopt : OptCounter G.pr G.E G.V0 σ τ)
    (hs : G.IsState (pair G.V0 σ τ)) {v : G.Vertex} (hv : v ≠ Vertex.cW)
    (hve : ∀ o, v = Vertex.eface o → G.wt o ≠ none) (o : G.Opt) :
    G.pr (lam G.pr (pair G.V0 σ τ) v) < G.pr (Vertex.eface o) := by
  have hpr := pr_injective h
  -- the all-β answer
  have hsβ := isState_tauBeta hs
  have hgβ : ∀ o, pair G.V0 σ G.tauBeta (Vertex.gate o) = Vertex.beta o := fun o => by
    rw [pair_of_notMem (gate_notMem_V0 o)]
    rfl
  have hkβ : pair G.V0 σ G.tauBeta Vertex.K2 = Vertex.K1 := by
    rw [pair_of_notMem K2_notMem_V0]
    rfl
  have hle : rew G.pr (lam G.pr (pair G.V0 σ τ) v) ≤ rew G.pr (lam G.pr (pair G.V0 σ G.tauBeta) v) :=
    Val.rew_top_le (hopt.2 G.tauBeta tauBeta_legal v)
  -- its cycle node is below every e-vertex
  have hβ : ∀ o', rew G.pr (lam G.pr (pair G.V0 σ G.tauBeta) v) < rew G.pr (Vertex.eface o') := by
    intro o'
    apply rew_lt_eface
    rcases lam_allBeta h hsβ hgβ hkβ hv hve with ⟨o'', e⟩ | e | e
    · rw [e]
      exact pr_lt_of_prio_lt h (bprio_lt_eprio o'' o')
    · rw [e]
      have := six_le_eprio o'
      exact pr_lt_of_prio_lt h (by simp only [prio]; omega)
    · rw [e]
      have := six_le_eprio o'
      exact pr_lt_of_prio_lt h (by simp only [prio]; omega)
  have hstar : ∀ o', rew G.pr (lam G.pr (pair G.V0 σ τ) v) < rew G.pr (Vertex.eface o') :=
    fun o' => lt_of_le_of_lt hle (hβ o')
  -- `K2 → K1` under the optimal counterstrategy, so `K3` is not a cycle node
  have hk : pair G.V0 σ τ Vertex.K2 = Vertex.K1 := by
    rw [pair_of_notMem K2_notMem_V0]
    exact loc_k2 h hopt hs
  have hll := lam_lam (s := pair G.V0 σ τ) hpr v
  generalize lam G.pr (pair G.V0 σ τ) v = w at hstar hll ⊢
  by_contra hnot
  rcases lt_or_eq_of_le (not_lt.mp hnot) with hlt | heq
  · -- more relevant than an e-vertex: E-DOM
    have hbig : ∀ (u : G.Vertex), Even (G.pr u) → G.pr (Vertex.eface o) < G.pr u →
        ¬ rew G.pr u < rew G.pr (Vertex.eface o) := by
      intro u hev hlt' hc
      rw [rew_of_even hev, rew_of_even (even_pr_eface o)] at hc
      omega
    rcases e_dom h hlt with he | rfl | rfl | rfl
    · rcases w with x | o' | o' | o' | _ | _ | _ | _ | _ | _ <;> simp [isE] at he
      exact lt_irrefl _ (hstar o')
    · exact hbig _ (even_pr.mpr (Nat.even_iff.mpr (by simp only [prio]; exact top_even))) hlt
        (hstar o)
    · exact hbig _ (even_pr.mpr (Nat.even_iff.mpr (by
        have := top_even (G := G)
        simp only [prio]
        omega))) hlt (hstar o)
    · rw [lam_K3 h hs hk] at hll
      cases hll
  · have : Vertex.eface o = w := hpr heq
    subst this
    exact lt_irrefl _ (hstar o)

end Genome

end

end PG
