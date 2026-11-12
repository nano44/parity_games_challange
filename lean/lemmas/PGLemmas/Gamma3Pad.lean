/-
`Genome.pad : G.PadStatement`: RESULTS R117's Lemma PAD (a), (b) on Γ3(G) and on every Γ3*(G*) whose
carriers have Ω ≥ 3 (PGLemmas/Gamma3Statement.lean).

Route (P-N5-REACH §5's proof, read on the Lean definitions):
* `depth`: every vertex other than c_X of Ω ≤ 2 (movers, gates, pads) steps, in at most four steps of any
  legal successor map, to a vertex of Ω ≥ 3: mover → m → gate → pe / pβ → e / β; core pads and pb → K0,
  K1 or K3 (`reach_high`).  The carriers have Ω ≥ 3 by hypothesis, c_W has top ≥ 4, the core K0, K1, K2,
  K3 has Ω ≥ 3.
* c_X has no in-edge but its own loop (`eq_cX_of_iterate`), so the cycle of v's play is c_X's loop only
  for v = c_X.
* p' orders by Ω first (`pr3_lt_of_prio_lt`): the cycle node, having the largest p' on its cycle, has
  Ω ≥ 3 unless it is c_X; every pad has Ω ≤ 2 (`prio3_pad_le`), so it is neither the cycle node nor in the
  P-set (whose elements have p' above the cycle node's).
-/
import PGLemmas.Gamma3Statement
import PGLemmas.GenomePlay
import Mathlib.Tactic

namespace PG

namespace Genome

variable {G : Genome}

/-- p' orders by Ω first: a larger Ω gives a larger rank. -/
theorem rk3_lt_of_prio_lt {π : G.Carrier} {u v : G.Vertex3} (h : G.prio3 π u < G.prio3 π v) :
    G.rk3 π u < G.rk3 π v := by
  unfold rk3
  apply Finset.card_lt_card
  rw [Finset.ssubset_iff_of_subset]
  · refine ⟨u, Finset.mem_filter.mpr ⟨Finset.mem_univ _, Or.inl h⟩, fun hu => ?_⟩
    have h1 := (Finset.mem_filter.mp hu).2
    omega
  · intro w hw
    have hw' := (Finset.mem_filter.mp hw).2
    refine Finset.mem_filter.mpr ⟨Finset.mem_univ _, ?_⟩
    omega

theorem pr3_lt_of_prio_lt {π : G.Carrier} {u v : G.Vertex3} (h : G.prio3 π u < G.prio3 π v) :
    G.pr3 π u < G.pr3 π v := by
  have := rk3_lt_of_prio_lt h
  unfold pr3
  have h1 : G.prio3 π u % 2 < 2 := Nat.mod_lt _ (by norm_num)
  have h2 : G.prio3 π v % 2 < 2 := Nat.mod_lt _ (by norm_num)
  omega

/-- Every pad has Ω ≤ 2. -/
theorem prio3_pad_le {π : G.Carrier} {p : G.Vertex3} (hp : Vertex3.isPad G p = true) :
    G.prio3 π p ≤ 2 := by
  cases p with
  | old v => simp [Vertex3.isPad] at hp
  | m o =>
    simp only [prio3]
    split <;> omega
  | _ => simp [prio3]

theorem top3_ge (π : G.Carrier) : 4 ≤ G.top3 π := by
  unfold top3 pmax3
  have : 2 ≤ max 2 (max (Finset.univ.sup π.pb) (Finset.univ.sup π.pe)) := le_max_left _ _
  omega

/-- Only c_X steps to c_X. -/
theorem eq_cX_of_mem_E3 {w : G.Vertex3} (hw : Vertex3.old Vertex.cX ∈ G.E3 w) :
    w = .old .cX := by
  cases w with
  | old v =>
    cases v with
    | mover x => simp [E3] at hw
    | beta o =>
      simp only [E3] at hw
      split at hw <;> simp at hw
    | eface o =>
      simp only [E3] at hw
      split at hw <;> simp at hw
    | cX => rfl
    | _ => simp [E3] at hw
  | _ => simp [E3] at hw

theorem eq_cX_of_iterate {s : G.Vertex3 → G.Vertex3} (hs : ∀ v, s v ∈ G.E3 v) :
    ∀ (n : ℕ) (v : G.Vertex3), s^[n] v = .old .cX → v = .old .cX := by
  intro n
  induction n with
  | zero => intro v h; simpa using h
  | succ n ih =>
    intro v h
    rw [Function.iterate_succ_apply] at h
    have h1 := ih _ h
    exact eq_cX_of_mem_E3 (h1 ▸ hs v)

/-- Steps to a vertex of Ω ≥ 3 (0 on such vertices and on c_X). -/
def depth3 : G.Vertex3 → ℕ
  | .old (.mover _) => 4
  | .old (.gate _) => 2
  | .m _ => 3
  | .pe _ => 1
  | .pbeta _ => 1
  | .pA => 1
  | .pS => 1
  | .pQ => 1
  | .pR => 1
  | .pb _ => 1
  | _ => 0

theorem high_of_depth_zero {π : G.Carrier} (hb : ∀ o, 3 ≤ π.pb o) (he : ∀ o, 3 ≤ π.pe o)
    {w : G.Vertex3} (hw : w ≠ .old .cX) (hd : depth3 w = 0) : 3 ≤ G.prio3 π w := by
  have ht := top3_ge (G := G) π
  cases w with
  | old v =>
    cases v with
    | beta o => exact hb o
    | eface o => exact he o
    | cX => exact absurd rfl hw
    | cW => simp only [prio3]; omega
    | K0 => simp only [prio3]; omega
    | K1 => simp [prio3]
    | K2 => simp [prio3]
    | K3 => simp only [prio3]; omega
    | _ => simp [depth3] at hd
  | _ => simp [depth3] at hd

theorem depth3_step {s : G.Vertex3 → G.Vertex3} (hs : ∀ v, s v ∈ G.E3 v) {w : G.Vertex3}
    (hd : depth3 w ≠ 0) : s w ≠ .old .cX ∧ depth3 (s w) < depth3 w := by
  have h := hs w
  cases w with
  | old v =>
    cases v with
    | mover x =>
      simp only [E3, Finset.mem_image, Finset.mem_univ, true_and] at h
      obtain ⟨k, hk⟩ := h
      rw [← hk]
      exact ⟨by simp, by simp [depth3]⟩
    | gate o =>
      simp only [E3, Finset.mem_insert, Finset.mem_singleton] at h
      rcases h with h | h <;> rw [h] <;> exact ⟨by simp, by simp [depth3]⟩
    | _ => simp [depth3] at hd
  | m o =>
    simp only [E3, Finset.mem_singleton] at h
    rw [h]; exact ⟨by simp, by simp [depth3]⟩
  | pe o =>
    simp only [E3, Finset.mem_singleton] at h
    rw [h]; exact ⟨by simp, by simp [depth3]⟩
  | pbeta o =>
    simp only [E3, Finset.mem_singleton] at h
    rw [h]; exact ⟨by simp, by simp [depth3]⟩
  | pA =>
    simp only [E3, Finset.mem_singleton] at h
    rw [h]; exact ⟨by simp, by simp [depth3]⟩
  | pS =>
    simp only [E3, Finset.mem_singleton] at h
    rw [h]; exact ⟨by simp, by simp [depth3]⟩
  | pQ =>
    simp only [E3, Finset.mem_singleton] at h
    rw [h]; exact ⟨by simp, by simp [depth3]⟩
  | pR =>
    simp only [E3, Finset.mem_singleton] at h
    rw [h]; exact ⟨by simp, by simp [depth3]⟩
  | pb o =>
    simp only [E3, Finset.mem_singleton] at h
    rw [h]; exact ⟨by simp, by simp [depth3]⟩

/-- Every vertex other than c_X reaches a vertex of Ω ≥ 3. -/
theorem reach_high {π : G.Carrier} (hb : ∀ o, 3 ≤ π.pb o) (he : ∀ o, 3 ≤ π.pe o)
    {s : G.Vertex3 → G.Vertex3} (hs : ∀ v, s v ∈ G.E3 v) :
    ∀ (d : ℕ) (w : G.Vertex3), depth3 w = d → w ≠ .old .cX → ∃ j, 3 ≤ G.prio3 π (s^[j] w) := by
  intro d
  induction d using Nat.strong_induction_on with
  | _ d ih =>
    intro w hd hw
    by_cases h0 : depth3 w = 0
    · exact ⟨0, by simpa using high_of_depth_zero hb he hw h0⟩
    · obtain ⟨hne, hlt⟩ := depth3_step hs h0
      obtain ⟨j, hj⟩ := ih _ (hd ▸ hlt) (s w) rfl hne
      exact ⟨j + 1, by rw [Function.iterate_succ_apply]; exact hj⟩

/-- **Lemma PAD** (RESULTS R117; P-N5-REACH §5 (a), (b)). -/
theorem pad : G.PadStatement := by
  intro π hb he s hs v
  have hc := lam_spec (G.pr3 π) s v
  have hlam : lam (G.pr3 π) s v ≠ .old .cX → 3 ≤ G.prio3 π (lam (G.pr3 π) s v) := by
    intro hne
    obtain ⟨⟨n, hn⟩, p, hp0, hp⟩ := hc.1
    obtain ⟨j, hj⟩ := reach_high hb he hs _ _ rfl hne
    have hcyc : OnCycle s v (s^[j] (lam (G.pr3 π) s v)) := by
      refine ⟨⟨j + n, ?_⟩, p, hp0, ?_⟩
      · rw [Function.iterate_add_apply, hn]
      · rw [← Function.iterate_add_apply, add_comm, Function.iterate_add_apply, hp]
    have hmax := hc.2 _ hcyc
    by_contra hlt
    have := pr3_lt_of_prio_lt (π := π) (u := lam (G.pr3 π) s v)
      (v := s^[j] (lam (G.pr3 π) s v)) (by omega)
    omega
  refine ⟨hlam, ?_, ?_⟩
  · by_cases hc' : lam (G.pr3 π) s v = .old .cX
    · rw [hc']; rfl
    · have h3 := hlam hc'
      cases hpad : Vertex3.isPad G (lam (G.pr3 π) s v)
      · rfl
      · have := prio3_pad_le (π := π) hpad
        omega
  · intro p hp
    obtain ⟨hgt, j, hj, -⟩ := mem_pset.mp hp
    by_cases hc' : lam (G.pr3 π) s v = .old .cX
    · exfalso
      obtain ⟨n, hn⟩ := (hc.1).1
      have hv : v = .old .cX := eq_cX_of_iterate hs n v (hn.trans hc')
      have h0 : plen (G.pr3 π) s v = 0 := by
        subst hv
        exact plen_eq_zero_of_lam_eq hc'
      omega
    · have h3 := hlam hc'
      cases hpad : Vertex3.isPad G p
      · rfl
      · have := prio3_pad_le (π := π) hpad
        have := pr3_lt_of_prio_lt (π := π) (u := p) (v := lam (G.pr3 π) s v) (by omega)
        omega

end Genome

end PG
