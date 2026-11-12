/-
`tcyc : TCycStatement V` (`PGLemmas/Statements5.lean`): RESULTS R118 (f) T-CYC and (i)(b), (c)
without the genome, from `lam_gap_sharp` (a p-run has at most |Mov| steps), `lam_count` (each
vertex changes its cycle node at most n − 1 times) and `steps_le_of_breaks`.
-/
import PGLemmas.Counting
import PGLemmas.Statements5

namespace PG

open Classical

noncomputable section

variable {V : Type*} [Fintype V]

/-- Along states whose values never fall, at most `n(n − 1)` steps change some cycle node. -/
theorem lam_steps_le (pr : V → ℕ) (hpr : Function.Injective pr) (s : ℕ → V → V) (T : ℕ)
    (hmono : ∀ t, t < T → ∀ v, Val.le pr (val pr (s t) v) (val pr (s (t + 1)) v)) :
    ((Finset.range T).filter (fun t => ∃ v, lam pr (s t) v ≠ lam pr (s (t + 1)) v)).card ≤
      Fintype.card V * (Fintype.card V - 1) := by
  let Bv : V → Finset ℕ := fun v =>
    (Finset.range T).filter (fun t => lam pr (s t) v ≠ lam pr (s (t + 1)) v)
  have hBv : ∀ v ∈ (Finset.univ : Finset V), (Bv v).card ≤ Fintype.card V - 1 := by
    intro v _
    have := lam_count pr hpr (fun t => val pr (s t) v) T (fun t ht => hmono t ht v)
    have e : (Bv v).card =
        ((Finset.range T).filter (fun t => (val pr (s t) v).top ≠ (val pr (s (t + 1)) v).top)).card :=
      rfl
    omega
  have hsub : (Finset.range T).filter (fun t => ∃ v, lam pr (s t) v ≠ lam pr (s (t + 1)) v) ⊆
      Finset.univ.biUnion Bv := by
    intro t ht
    obtain ⟨htr, v, hv⟩ := Finset.mem_filter.mp ht
    exact Finset.mem_biUnion.mpr ⟨v, Finset.mem_univ _, Finset.mem_filter.mpr ⟨htr, hv⟩⟩
  have := Finset.card_biUnion_le_card_mul (Finset.univ : Finset V) Bv (Fintype.card V - 1) hBv
  rw [Finset.card_univ] at this
  exact (Finset.card_le_card hsub).trans this

/-- **R118 (f) T-CYC and (i)(b), (c)**, without the genome. -/
theorem tcyc : TCycStatement V := by
  intro pr hpr E V0 Mov hsub σ τ T hfrozen hhow hF1 hchg C R
  -- the C-steps and the R-steps
  let BC : Finset ℕ := (Finset.range T).filter (fun t =>
    ∃ v, lam pr (nxt V0 σ τ t) v ≠ lam pr (nxt V0 σ τ (t + 1)) v)
  let BR : Finset ℕ := (Finset.range T).filter (fun t =>
    (∀ v, lam pr (nxt V0 σ τ t) v = lam pr (nxt V0 σ τ (t + 1)) v) ∧
      ∃ v, v ∉ V0 ∧ τ t v ≠ τ (t + 1) v)
  have hC : BC.card = C := rfl
  have hR : BR.card = R := rfl
  have hCle : C ≤ Fintype.card V * (Fintype.card V - 1) :=
    lam_steps_le pr hpr (nxt V0 σ τ) T hF1
  refine ⟨?_, hCle⟩
  -- `|Mov| + 1` consecutive steps contain a C-step or an R-step
  have hbreak : ∀ a, a + Mov.card < T → ∃ t ∈ BC ∪ BR, a ≤ t ∧ t ≤ a + Mov.card := by
    intro a ha
    by_contra hnone
    have hquiet : ∀ t, a ≤ t → t ≤ a + Mov.card →
        (∀ v, lam pr (nxt V0 σ τ t) v = lam pr (nxt V0 σ τ (t + 1)) v) ∧
          ∀ v, v ∉ V0 → τ t v = τ (t + 1) v := by
      intro t h1 h2
      have hlam : ∀ v, lam pr (nxt V0 σ τ t) v = lam pr (nxt V0 σ τ (t + 1)) v := by
        intro v
        by_contra hne
        exact hnone ⟨t, Finset.mem_union_left _ (Finset.mem_filter.mpr
          ⟨Finset.mem_range.mpr (by omega), v, hne⟩), h1, h2⟩
      refine ⟨hlam, fun v hv => ?_⟩
      by_contra hne
      exact hnone ⟨t, Finset.mem_union_right _ (Finset.mem_filter.mpr
        ⟨Finset.mem_range.mpr (by omega), hlam, v, hv, hne⟩), h1, h2⟩
    have hconst : ∀ d, d ≤ Mov.card + 1 →
        (∀ v, lam pr (nxt V0 σ τ (a + d)) v = lam pr (nxt V0 σ τ a) v) ∧
          ∀ v, v ∉ V0 → τ (a + d) v = τ a v := by
      intro d
      induction d with
      | zero => intro _; exact ⟨fun v => rfl, fun v _ => rfl⟩
      | succ d ih =>
        intro hd
        obtain ⟨ih1, ih2⟩ := ih (by omega)
        obtain ⟨q1, q2⟩ := hquiet (a + d) (by omega) (by omega)
        exact ⟨fun v => (q1 v).symm.trans (ih1 v), fun v hv => (q2 v hv).symm.trans (ih2 v hv)⟩
    have W : Window pr E Mov (nxt V0 σ τ) a (a + Mov.card + 1) := by
      refine ⟨by omega, ?_, ?_, ?_, ?_, ?_⟩
      · intro t h1 h2 v hv
        unfold nxt pair
        by_cases hv0 : v ∈ V0
        · simp only [hv0, ite_true]
          rw [hfrozen t (by omega) v hv0 hv, hfrozen a (by omega) v hv0 hv]
        · simp only [hv0, ite_false]
          have := (hconst (t - a) (by omega)).2 v hv0
          have e : a + (t - a) = t := by omega
          rwa [e] at this
      · intro t _ ht v hv
        exact hhow t (by omega) v hv
      · intro t _ ht v
        exact hF1 t (by omega) v
      · intro t h1 h2 v
        have := (hconst (t - a) (by omega)).1 v
        have e : a + (t - a) = t := by omega
        rwa [e] at this
      · intro t _ ht hstop
        obtain ⟨x, hx0, hx⟩ := hchg t (by omega)
        apply hx
        have := congrFun hstop x
        unfold nxt pair at this
        simpa only [hx0, ite_true] using this
    have := lam_gap_sharp pr hpr E Mov (nxt V0 σ τ) a (a + Mov.card + 1) W
    omega
  have hT := steps_le_of_breaks (BC ∪ BR) Mov.card T hbreak
  have hcard : (BC ∪ BR).card ≤ C + R := by
    rw [← hC, ← hR]
    exact Finset.card_union_le _ _
  have h1 : (BC ∪ BR).card * (Mov.card + 1) ≤ (C + R) * (Mov.card + 1) :=
    Nat.mul_le_mul_right _ hcard
  have h2 : (C + R) * (Mov.card + 1) + Mov.card = C + R + (C + R + 1) * Mov.card := by ring
  omega

end

end PG
