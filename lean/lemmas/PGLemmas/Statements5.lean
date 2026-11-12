/-
The run-length bound of RESULTS R118 (f) Theorem T-CYC and (i) clauses (b), (c), as one statement
without the genome (proposed to the Lead; same convention).

R118 (a) labels a step `t → t+1` «C if Λ_t(v) ≠ Λ_(t+1)(v) for some vertex v; else R if
σ̄_t(v) ≠ σ̄_(t+1)(v) for some Odd vertex v; else p».  R118 (f): «T_CYC ≤ C + R + (C + R + 1)·N»;
(i)(b) «C ≤ n(n − 1)»; (i)(c) «T ≤ C + R + (C + R + 1)·n_E» (the case `Mov = V0`).
-/
import PGLemmas.Statements

namespace PG

open Classical

noncomputable section

/-- A two-player Howard run `0, …, T`: Even's vertices `V0`, movers `Mov ⊆ V0`, the other Even
vertices frozen, Howard steps at the movers, F1 as a hypothesis, every step changing `σ`.  With
`C` the number of C-steps and `R` the number of R-steps: `T ≤ C + R + (C + R + 1)·|Mov|` and
`C ≤ n(n − 1)`. -/
def TCycStatement (V : Type*) [Fintype V] : Prop :=
  ∀ (pr : V → ℕ), Function.Injective pr →
  ∀ (E : V → Finset V) (V0 Mov : Finset V), Mov ⊆ V0 →
  ∀ (σ τ : ℕ → V → V) (T : ℕ),
    -- every Even vertex that is not a mover is frozen
    (∀ t, t ≤ T → ∀ v ∈ V0, v ∉ Mov → σ t v = σ 0 v) →
    -- Howard steps at the movers
    (∀ t, t < T → ∀ x ∈ Mov, HowardAt pr E (nxt V0 σ τ t) (nxt V0 σ τ (t + 1)) x) →
    -- F1: `Ω_t ⊴ Ω_(t+1)` pointwise
    (∀ t, t < T → ∀ v,
      Val.le pr (val pr (nxt V0 σ τ t) v) (val pr (nxt V0 σ τ (t + 1)) v)) →
    -- every step changes `σ` (the run has not stopped before `T`)
    (∀ t, t < T → ∃ x ∈ V0, σ (t + 1) x ≠ σ t x) →
    (let C := ((Finset.range T).filter (fun t =>
        ∃ v, lam pr (nxt V0 σ τ t) v ≠ lam pr (nxt V0 σ τ (t + 1)) v)).card
     let R := ((Finset.range T).filter (fun t =>
        (∀ v, lam pr (nxt V0 σ τ t) v = lam pr (nxt V0 σ τ (t + 1)) v) ∧
          ∃ v, v ∉ V0 ∧ τ t v ≠ τ (t + 1) v)).card
     T ≤ C + R + (C + R + 1) * Mov.card ∧
       C ≤ Fintype.card V * (Fintype.card V - 1))

end

end PG
