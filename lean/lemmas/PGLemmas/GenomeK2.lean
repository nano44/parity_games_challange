/-
Box 208 §2 (K2) COARSE, proved for Γ(G): `k2 : G.K2Statement` (`PGLemmas/GenomeClass.lean`).
No premise.

Proof (box 208's): let Ω ⊴ Ω′ with the same cycle node and Π ≠ Π′, and let d be the most
relevant vertex of Π Δ Π′.  If E ≠ E′, the most relevant e-vertex z of E Δ E′ is in Π Δ Π′.  A
vertex more relevant than z is an e-vertex, c_W, K0 or K3 (`e_dom`); c_W is in no Π
(`cW_notMem_pset`); K0 and K3 are in both of Π, Π′ or in neither, because a play from outside the
core has cycle node K1 iff it runs K0 → K3 → K2 → K1 (`core_path`, `lam_of_K0_mem`,
`lam_of_K3_mem`).  So d = z, an even vertex, and by the order on path sets z ∈ Π′.
-/
import PGLemmas.GenomeK3

namespace PG

open Classical
open scoped symmDiff

noncomputable section

namespace Genome

variable {G : Genome} {s : G.Vertex → G.Vertex}

/-- The predecessors of `K1`. -/
theorem succ_eq_K1 (hs : G.IsState s) {w : G.Vertex} (hw : s w = Vertex.K1) :
    w = Vertex.K1 ∨ w = Vertex.K2 := by
  rcases w with x | o | o | o | _ | _ | _ | _ | _ | _
  · obtain ⟨k, hk⟩ := hs.mover x
    rw [hk] at hw
    cases hw
  · rcases hs.gate o with hk | hk <;> rw [hk] at hw <;> cases hw
  · rw [hs.beta o] at hw
    simp only [start0] at hw
    cases hx : G.xt o <;> rw [hx] at hw <;> cases hw
  · rw [hs.eface o] at hw
    simp only [start0] at hw
    cases hx : G.wt o <;> rw [hx] at hw <;> cases hw
  · rw [hs.cX] at hw
    cases hw
  · rw [hs.cW] at hw
    cases hw
  · rw [hs.K0] at hw
    cases hw
  · exact Or.inl rfl
  · exact Or.inr rfl
  · rw [hs.K3] at hw
    cases hw

/-- The predecessor of `K2` (when `K2 → K1`). -/
theorem succ_eq_K2 (hs : G.IsState s) (hk2 : s Vertex.K2 = Vertex.K1) {w : G.Vertex}
    (hw : s w = Vertex.K2) : w = Vertex.K3 := by
  rcases w with x | o | o | o | _ | _ | _ | _ | _ | _
  · obtain ⟨k, hk⟩ := hs.mover x
    rw [hk] at hw
    cases hw
  · rcases hs.gate o with hk | hk <;> rw [hk] at hw <;> cases hw
  · rw [hs.beta o] at hw
    simp only [start0] at hw
    cases hx : G.xt o <;> rw [hx] at hw <;> cases hw
  · rw [hs.eface o] at hw
    simp only [start0] at hw
    cases hx : G.wt o <;> rw [hx] at hw <;> cases hw
  · rw [hs.cX] at hw
    cases hw
  · rw [hs.cW] at hw
    cases hw
  · rw [hs.K0] at hw
    cases hw
  · rw [hs.K1] at hw
    cases hw
  · rw [hk2] at hw
    cases hw
  · rfl

/-- The predecessor of `K3` (when `K2 → K1`). -/
theorem succ_eq_K3 (hs : G.IsState s) (hk2 : s Vertex.K2 = Vertex.K1) {w : G.Vertex}
    (hw : s w = Vertex.K3) : w = Vertex.K0 := by
  rcases w with x | o | o | o | _ | _ | _ | _ | _ | _
  · obtain ⟨k, hk⟩ := hs.mover x
    rw [hk] at hw
    cases hw
  · rcases hs.gate o with hk | hk <;> rw [hk] at hw <;> cases hw
  · rw [hs.beta o] at hw
    simp only [start0] at hw
    cases hx : G.xt o <;> rw [hx] at hw <;> cases hw
  · rw [hs.eface o] at hw
    simp only [start0] at hw
    cases hx : G.wt o <;> rw [hx] at hw <;> cases hw
  · rw [hs.cX] at hw
    cases hw
  · rw [hs.cW] at hw
    cases hw
  · rfl
  · rw [hs.K1] at hw
    cases hw
  · rw [hk2] at hw
    cases hw
  · rw [hs.K3] at hw
    cases hw

theorem pr_K1_lt_K0 (h : G.WF) : G.pr Vertex.K1 < G.pr Vertex.K0 := by
  apply pr_lt_of_prio_lt h
  have := two_le_pmax (G := G)
  have := pmax_lt_top (G := G)
  simp only [prio]
  omega

theorem pr_K1_lt_K3 (h : G.WF) : G.pr Vertex.K1 < G.pr Vertex.K3 := by
  apply pr_lt_of_prio_lt h
  have := two_le_pmax (G := G)
  have := pmax_lt_top (G := G)
  simp only [prio]
  omega

/-- A play from outside the core with cycle node `K1` runs `K0 → K3 → K2 → K1`: `K0` and `K3`
are in its path component. -/
theorem core_path (h : G.WF) (hs : G.IsState s) (hk : s Vertex.K2 = Vertex.K1) {u : G.Vertex}
    (hu : G.isCore u = false) (hl : lam G.pr s u = Vertex.K1) :
    Vertex.K0 ∈ pset G.pr s u ∧ Vertex.K3 ∈ pset G.pr s u := by
  have hhit := iterate_plen G.pr s u
  rw [hl] at hhit
  have hfirst : ∀ j, j < plen G.pr s u → s^[j] u ≠ Vertex.K1 := fun j hj => by
    have := iterate_ne_lam_of_lt_plen (pr := G.pr) (s := s) hj
    rwa [hl] at this
  have hn0 : plen G.pr s u ≠ 0 := by
    intro h0
    rw [h0] at hhit
    have e : u = Vertex.K1 := hhit
    subst e
    simp [isCore] at hu
  obtain ⟨n1, hn1⟩ := Nat.exists_eq_succ_of_ne_zero hn0
  rw [hn1] at hhit
  have e1 : s (s^[n1] u) = Vertex.K1 := by
    rw [← Function.iterate_succ_apply' s n1 u]
    exact hhit
  have w1 : s^[n1] u = Vertex.K2 := by
    rcases succ_eq_K1 hs e1 with h1 | h1
    · exact absurd h1 (hfirst n1 (by omega))
    · exact h1
  have hn1' : n1 ≠ 0 := by
    intro h0
    rw [h0] at w1
    have e : u = Vertex.K2 := w1
    subst e
    simp [isCore] at hu
  obtain ⟨n2, hn2⟩ := Nat.exists_eq_succ_of_ne_zero hn1'
  rw [hn2] at w1
  have e2 : s (s^[n2] u) = Vertex.K2 := by
    rw [← Function.iterate_succ_apply' s n2 u]
    exact w1
  have w2 : s^[n2] u = Vertex.K3 := succ_eq_K2 hs hk e2
  have hn2' : n2 ≠ 0 := by
    intro h0
    rw [h0] at w2
    have e : u = Vertex.K3 := w2
    subst e
    simp [isCore] at hu
  obtain ⟨n3, hn3⟩ := Nat.exists_eq_succ_of_ne_zero hn2'
  rw [hn3] at w2
  have e3 : s (s^[n3] u) = Vertex.K3 := by
    rw [← Function.iterate_succ_apply' s n3 u]
    exact w2
  have w3 : s^[n3] u = Vertex.K0 := succ_eq_K3 hs hk e3
  constructor
  · rw [mem_pset, hl]
    exact ⟨pr_K1_lt_K0 h, n3, by omega, w3⟩
  · rw [mem_pset, hl]
    exact ⟨pr_K1_lt_K3 h, n3.succ, by omega, w2⟩

/-- `c_W` is in no path component. -/
theorem cW_notMem_pset (h : G.WF) (hs : G.IsState s) (u : G.Vertex) :
    Vertex.cW ∉ pset G.pr s u := by
  intro hm
  obtain ⟨hlt, j, -, hj⟩ := mem_pset.mp hm
  have e := lam_iterate (s := s) (pr_injective h) u j
  rw [hj, lam_cW hs] at e
  rw [← e] at hlt
  exact lt_irrefl _ hlt

theorem lam_of_K0_mem (h : G.WF) (hs : G.IsState s) (hk : s Vertex.K2 = Vertex.K1)
    {u : G.Vertex} (hm : Vertex.K0 ∈ pset G.pr s u) : lam G.pr s u = Vertex.K1 := by
  obtain ⟨-, j, -, hj⟩ := mem_pset.mp hm
  have e := lam_iterate (s := s) (pr_injective h) u j
  rw [hj, lam_K0 h hs hk] at e
  exact e.symm

theorem lam_of_K3_mem (h : G.WF) (hs : G.IsState s) (hk : s Vertex.K2 = Vertex.K1)
    {u : G.Vertex} (hm : Vertex.K3 ∈ pset G.pr s u) : lam G.pr s u = Vertex.K1 := by
  obtain ⟨-, j, -, hj⟩ := mem_pset.mp hm
  have e := lam_iterate (s := s) (pr_injective h) u j
  rw [hj, lam_K3 h hs hk] at e
  exact e.symm

theorem mem_eset {u z : G.Vertex} :
    z ∈ G.eset s u ↔ z ∈ pset G.pr s u ∧ G.isE z = true := by
  unfold eset
  rw [Finset.mem_filter]

/-- **(K2) COARSE** (box 208 §2). -/
theorem k2 : G.K2Statement := by
  intro h s s' hs hs' hk hk' u v hu hv hle
  have hpr := pr_injective h
  have hsame : lam G.pr s u = lam G.pr s' v → pset G.pr s u = pset G.pr s' v →
      G.clsLe (G.cls s u) (G.cls s' v) := by
    intro e1 e2
    refine Or.inr ?_
    unfold cls eset
    rw [e1, e2]
  rcases hle with hlt | heq
  · rcases hlt with h1 | ⟨h1, h2⟩ | ⟨h1, h2, -⟩ | ⟨h1, h2, -⟩
    · exact Or.inl (Or.inl h1)
    · -- the same cycle node, different path components
      have h1' : lam G.pr s u = lam G.pr s' v := h1
      obtain ⟨d, hd, hmax, hside⟩ := h2
      by_cases hE : G.eset s u = G.eset s' v
      · exact Or.inr (Prod.ext h1 hE)
      · have hne : (G.eset s u ∆ G.eset s' v).Nonempty := Finset.symmDiff_nonempty.mpr hE
        obtain ⟨z, hz, hzmax⟩ := Finset.exists_max_image _ G.pr hne
        have hzE : G.isE z = true := by
          rcases Finset.mem_symmDiff.mp hz with ⟨a, -⟩ | ⟨a, -⟩ <;> exact (mem_eset.mp a).2
        have hzP : z ∈ pset G.pr s u ∧ z ∉ pset G.pr s' v ∨
            z ∈ pset G.pr s' v ∧ z ∉ pset G.pr s u := by
          rcases Finset.mem_symmDiff.mp hz with ⟨a, b⟩ | ⟨a, b⟩
          · exact Or.inl ⟨(mem_eset.mp a).1, fun c => b (mem_eset.mpr ⟨c, hzE⟩)⟩
          · exact Or.inr ⟨(mem_eset.mp a).1, fun c => b (mem_eset.mpr ⟨c, hzE⟩)⟩
        -- (the symmetric difference inside `setLt` carries the classical decidable equality)
        have hzd : G.pr z ≤ G.pr d := hmax z (by
          simp only [Finset.mem_symmDiff]
          exact hzP)
        obtain ⟨o, rfl⟩ := isE_iff.mp hzE
        have hdmem : d ∈ pset G.pr s u ∧ d ∉ pset G.pr s' v ∨
            d ∈ pset G.pr s' v ∧ d ∉ pset G.pr s u := by
          simp only [Finset.mem_symmDiff] at hd
          exact hd
        have hdz : d = Vertex.eface o := by
          by_contra hne'
          have hlt : G.pr (Vertex.eface o) < G.pr d :=
            lt_of_le_of_ne hzd (fun e => hne' (hpr e).symm)
          rcases e_dom h hlt with he | rfl | rfl | rfl
          · -- an e-vertex of Π Δ Π′ is in E Δ E′: against the choice of z
            have hdE : d ∈ G.eset s u ∆ G.eset s' v := by
              rw [Finset.mem_symmDiff]
              rcases hdmem with ⟨a, b⟩ | ⟨a, b⟩
              · exact Or.inl ⟨mem_eset.mpr ⟨a, he⟩, fun c => b (mem_eset.mp c).1⟩
              · exact Or.inr ⟨mem_eset.mpr ⟨a, he⟩, fun c => b (mem_eset.mp c).1⟩
            have := hzmax d hdE
            omega
          · rcases hdmem with ⟨a, -⟩ | ⟨a, -⟩
            · exact cW_notMem_pset h hs u a
            · exact cW_notMem_pset h hs' v a
          · rcases hdmem with ⟨a, b⟩ | ⟨a, b⟩
            · have e := lam_of_K0_mem h hs hk a
              exact b (core_path h hs' hk' hv (h1'.symm.trans e)).1
            · have e := lam_of_K0_mem h hs' hk' a
              exact b (core_path h hs hk hu (h1'.trans e)).1
          · rcases hdmem with ⟨a, b⟩ | ⟨a, b⟩
            · have e := lam_of_K3_mem h hs hk a
              exact b (core_path h hs' hk' hv (h1'.symm.trans e)).2
            · have e := lam_of_K3_mem h hs' hk' a
              exact b (core_path h hs hk hu (h1'.trans e)).2
        subst hdz
        have hin : Vertex.eface o ∈ pset G.pr s' v := by
          rcases hside with ⟨a, -⟩ | ⟨-, b⟩
          · exact a
          · exact absurd (even_pr_eface o) b
        exact Or.inl (Or.inr ⟨h1, Vertex.eface o, hz, hzmax, mem_eset.mpr ⟨hin, rfl⟩⟩)
    · exact hsame h1 h2
    · exact hsame h1 h2
  · exact hsame (congrArg Val.top heq) (congrArg Val.set heq)

end Genome

end

end PG
