/-
`BrSegGNoH0Statement`: RESULTS R118 (i) clause (a) with H0 weakened to «every step changes σ at
some Even vertex» (Lead ruling 2026-11-12 11:49Z, item 8: a separate statement, so that
`BrSegGStatement` stays the landed text).  Theorem: `brsegG_noH0'` (`PGLemmas/NoH0.lean`).
-/
import PGLemmas.Statements

namespace PG

noncomputable section

/-- BR-SEG-G clause (a) without H0: a run of `r` consecutive p-steps of Howard at every Even
vertex has `r ≤ n_E`, if every step changes `σ` at some Even vertex.  F1 is a hypothesis. -/
def BrSegGNoH0Statement (V : Type*) [Fintype V] : Prop :=
  ∀ (pr : V → ℕ), Function.Injective pr →
  ∀ (E : V → Finset V) (V0 : Finset V) (σ τ : ℕ → V → V) (a r : ℕ),
    (∀ t, a ≤ t → t < a + r → ∀ x ∈ V0,
      HowardAt pr E (nxt V0 σ τ t) (nxt V0 σ τ (t + 1)) x) →
    (∀ t, a ≤ t → t < a + r → ∀ v,
      Val.le pr (val pr (nxt V0 σ τ t) v) (val pr (nxt V0 σ τ (t + 1)) v)) →
    (∀ t, a ≤ t → t ≤ a + r → ∀ v, lam pr (nxt V0 σ τ t) v = lam pr (nxt V0 σ τ a) v) →
    (∀ t, a ≤ t → t ≤ a + r → ∀ v, v ∉ V0 → τ t v = τ a v) →
    -- every step changes `σ` at some Even vertex (this replaces H0)
    (∀ t, a ≤ t → t < a + r → ∃ x ∈ V0, σ (t + 1) x ≠ σ t x) →
    r ≤ V0.card

end

end PG
