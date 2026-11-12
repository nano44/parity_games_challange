/-
Premise F1 for two-player games, as a statement (proposed to the Lead; same convention).

* `OptCounter`       [Fr] §3: «A strategy τ is an optimal counterstrategy w.r.t. σ iff for every
                     opponent strategy τ′ and for every node v we have: ϑ_{σ,τ,v} ⪯ ϑ_{σ,τ′,v}».
* `F1Statement`      RESULTS R15 (a) Lemma A = VJ00 Lemma 5.7 («Ωσ ⊴ Ω_{Switch_I(σ)}» for a set I
                     of improvements), in Friedmann's form: Ω_σ is the valuation of σ with an
                     optimal counterstrategy.
* `BrSegOptStatement`, `TCycOptStatement`: BR-SEG (R118 (d)) and T-CYC (R118 (f), (i)(b),(c))
                     with F1 replaced by «σ̄_t is an optimal counterstrategy against σ_t».
-/
import PGLemmas.Statements
import PGLemmas.Statements5

namespace PG

open Classical

noncomputable section

variable {V : Type*} [Fintype V]

/-- `τ` is an optimal counterstrategy against `σ`: it follows the edges at Odd's vertices
(those outside `V0`), and no Odd strategy gives any vertex a smaller value. -/
def OptCounter (pr : V → ℕ) (E : V → Finset V) (V0 : Finset V) (σ τ : V → V) : Prop :=
  (∀ u, u ∉ V0 → τ u ∈ E u) ∧
  ∀ τ₂ : V → V, (∀ u, u ∉ V0 → τ₂ u ∈ E u) →
    ∀ v, Val.le pr (val pr (pair V0 σ τ) v) (val pr (pair V0 σ τ₂) v)

/-- **F1 = RESULTS R15 (a) Lemma A.**  Let `τ` be an optimal counterstrategy against `σ`, and
let `σ'` arise from `σ` by improvements: every Even vertex keeps its successor or moves to one
whose value `Ω_σ` is strictly larger.  Then `Ω_σ(v) ⊴` the value of `v` under `σ'` and ANY Odd
strategy `τ'`; in particular `Ω_σ ⊴ Ω_σ'` (`τ'` an optimal counterstrategy against `σ'`). -/
def F1Statement (V : Type*) [Fintype V] : Prop :=
  ∀ (pr : V → ℕ), Function.Injective pr →
  ∀ (E : V → Finset V) (V0 : Finset V) (σ τ σ' τ' : V → V),
    OptCounter pr E V0 σ τ →
    (∀ u, u ∉ V0 → τ' u ∈ E u) →
    (∀ v ∈ V0, σ' v = σ v ∨
      Val.lt pr (val pr (pair V0 σ τ) (σ v)) (val pr (pair V0 σ τ) (σ' v))) →
    ∀ v, Val.le pr (val pr (pair V0 σ τ) v) (val pr (pair V0 σ' τ') v)

/-- BR-SEG (RESULTS R118 (d)) with no premise F1: `σ̄_t = τ t` is an optimal counterstrategy
against `σ t` at every state of the window, and the movers follow the edges at the first state. -/
def BrSegOptStatement (V : Type*) [Fintype V] : Prop :=
  ∀ (pr : V → ℕ), Function.Injective pr →
  ∀ (E : V → Finset V) (V0 Mov : Finset V), Mov ⊆ V0 →
  ∀ (σ τ : ℕ → V → V) (a j : ℕ),
    (∀ t, a ≤ t → t ≤ a + j + 1 → ∀ v ∈ V0, v ∉ Mov → σ t v = σ a v) →
    (∀ x ∈ Mov, σ a x ∈ E x) →
    (∀ t, a ≤ t → t ≤ a + j → ∀ x ∈ Mov,
      HowardAt pr E (nxt V0 σ τ t) (nxt V0 σ τ (t + 1)) x) →
    -- `σ̄_t` is an optimal counterstrategy
    (∀ t, a ≤ t → t ≤ a + j + 1 → OptCounter pr E V0 (σ t) (τ t)) →
    (∀ t, a ≤ t → t ≤ a + j + 1 → ∀ v, lam pr (nxt V0 σ τ t) v = lam pr (nxt V0 σ τ a) v) →
    (∀ t, a ≤ t → t ≤ a + j + 1 → ∀ v, v ∉ V0 → τ t v = τ a v) →
    (∃ x ∈ V0, σ (a + j + 1) x ≠ σ (a + j) x) →
    j + 1 ≤ Mov.card

/-- T-CYC (RESULTS R118 (f), (i)(b), (c)) with no premise F1. -/
def TCycOptStatement (V : Type*) [Fintype V] : Prop :=
  ∀ (pr : V → ℕ), Function.Injective pr →
  ∀ (E : V → Finset V) (V0 Mov : Finset V), Mov ⊆ V0 →
  ∀ (σ τ : ℕ → V → V) (T : ℕ),
    (∀ t, t ≤ T → ∀ v ∈ V0, v ∉ Mov → σ t v = σ 0 v) →
    (∀ x ∈ Mov, σ 0 x ∈ E x) →
    (∀ t, t < T → ∀ x ∈ Mov, HowardAt pr E (nxt V0 σ τ t) (nxt V0 σ τ (t + 1)) x) →
    -- `σ̄_t` is an optimal counterstrategy
    (∀ t, t ≤ T → OptCounter pr E V0 (σ t) (τ t)) →
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
