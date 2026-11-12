/-
The statements, as Lean propositions.  Each `…Statement` below is the exact type of the theorem
that proves it, so the text diffed against the lane lemmas is the text Lean checks.

* `LamGapSharpStatement`     Lemma LAM-GAP in its SHARP form (b − a ≤ |Ch|):
                             claude/l-si docs/si/box101-lamgap.md §2 (bound |Ch| + 1) with
                             claude/l-red docs/red/R234-lamgap.md §3 (Lemma SHARP).
* `LamGapOnePlayerStatement` the same, in the literal one-player wording of box 101 §2.
* `BrSegStatement`           RESULTS R118 (d), Theorem BR-SEG, without the genome: any game, any
                             set of movers, Odd's reply and every non-mover frozen on the window.
* `BrSegGStatement`          RESULTS R118 (i) clause (a), Theorem BR-SEG-G under H0.
* `OneCrossStatement`        claude/l-red docs/red/R231-onecross.md §2, Lemma ONE-CROSS, from its
                             three premises (F1, NO-TIE, LOC-GATE) over any preorder of values.
-/
import PGLemmas.Defs

namespace PG

noncomputable section

variable {V : Type*} [Fintype V]

/-- Lemma LAM-GAP, SHARP form.  A window `a..b` of a Howard run on which every vertex keeps its
cycle node has `b − a ≤ |Ch|`.  The hypotheses are the fields of `Window` (`PGLemmas/Defs.lean`):
only `Ch` moves, Howard steps at `Ch`, premise (M), every `Λ` constant, the run not stopped. -/
def LamGapSharpStatement (V : Type*) [Fintype V] : Prop :=
  ∀ (pr : V → ℕ), Function.Injective pr →
  ∀ (E : V → Finset V) (Ch : Finset V) (s : ℕ → V → V) (a b : ℕ),
    Window pr E Ch s a b → b - a ≤ Ch.card

/-- The same in box 101 §2's one-player wording: `E` is the edge relation of a game in which
every vertex outside `Ch` has exactly one successor, and every state is a strategy of that game. -/
def LamGapOnePlayerStatement (V : Type*) [Fintype V] : Prop :=
  ∀ (pr : V → ℕ), Function.Injective pr →
  ∀ (E : V → Finset V) (Ch : Finset V) (s : ℕ → V → V) (a b : ℕ),
    a ≤ b →
    -- one-player: a vertex outside `Ch` has one successor
    (∀ v, v ∉ Ch → ∃ u, E v = {u}) →
    -- every state follows the edges
    (∀ t, a ≤ t → t ≤ b → ∀ v, s t v ∈ E v) →
    -- Howard steps at `Ch`
    (∀ t, a ≤ t → t < b → ∀ v ∈ Ch, HowardAt pr E (s t) (s (t + 1)) v) →
    -- premise (M)
    (∀ t, a ≤ t → t < b → ∀ v, Val.le pr (val pr (s t) v) (val pr (s (t + 1)) v)) →
    -- `Λ_t(v) = Λ_a(v)` for every vertex `v` and `a ≤ t ≤ b`
    (∀ t, a ≤ t → t ≤ b → ∀ v, lam pr (s t) v = lam pr (s a) v) →
    -- `a..b` are states of the run: none of them before `b` is its last state
    (∀ t, a ≤ t → t < b → s (t + 1) ≠ s t) →
    b - a ≤ Ch.card

/-- The state at time `t` of a two-player run as one successor map: Even's `σ t` on `V0`, Odd's
counterstrategy `τ t` (the fleet's `σ̄_t`) elsewhere.  Its valuation `val pr (nxt V0 σ τ t)` is the
fleet's `Ω_t`, its cycle nodes `lam pr (nxt V0 σ τ t)` are `Λ_t`. -/
def nxt (V0 : Finset V) (σ τ : ℕ → V → V) (t : ℕ) : V → V := pair V0 (σ t) (τ t)

/-- RESULTS R118 (d), Theorem BR-SEG: «If Λ and σ̄ are constant on the states a, a+1, …, a+j+1 and
the step a+j → a+j+1 changes σ, then j ≤ N − 1.»  Here `V0` are Even's vertices, `Mov ⊆ V0` the
`N` movers, every other Even vertex is frozen, every step is a Howard step at every mover, and
F1 (RESULTS R15 (a), pointwise) is a hypothesis.  The conclusion `j + 1 ≤ N` is `j ≤ N − 1`. -/
def BrSegStatement (V : Type*) [Fintype V] : Prop :=
  ∀ (pr : V → ℕ), Function.Injective pr →
  ∀ (E : V → Finset V) (V0 Mov : Finset V), Mov ⊆ V0 →
  ∀ (σ τ : ℕ → V → V) (a j : ℕ),
    -- every Even vertex that is not a mover is frozen
    (∀ t, a ≤ t → t ≤ a + j + 1 → ∀ v ∈ V0, v ∉ Mov → σ t v = σ a v) →
    -- Howard steps at the movers
    (∀ t, a ≤ t → t ≤ a + j → ∀ x ∈ Mov,
      HowardAt pr E (nxt V0 σ τ t) (nxt V0 σ τ (t + 1)) x) →
    -- F1: `Ω_t ⊴ Ω_(t+1)` pointwise
    (∀ t, a ≤ t → t ≤ a + j → ∀ v,
      Val.le pr (val pr (nxt V0 σ τ t) v) (val pr (nxt V0 σ τ (t + 1)) v)) →
    -- `Λ` is constant on the states `a, …, a+j+1`
    (∀ t, a ≤ t → t ≤ a + j + 1 → ∀ v, lam pr (nxt V0 σ τ t) v = lam pr (nxt V0 σ τ a) v) →
    -- `σ̄` is constant on the states `a, …, a+j+1`
    (∀ t, a ≤ t → t ≤ a + j + 1 → ∀ v, v ∉ V0 → τ t v = τ a v) →
    -- the step `a+j → a+j+1` changes `σ`
    (∃ x ∈ V0, σ (a + j + 1) x ≠ σ (a + j) x) →
    j + 1 ≤ Mov.card

/-- RESULTS R118 (i), Theorem BR-SEG-G, clause (a): «every maximal run of p-steps has at most n_E
steps», for Howard at every Even vertex of any game, under «H0: every step t → t+1 switches some
Even x with Λ_t(x) ≠ x and Λ_(t+1)(x) ≠ x.»  A run of `r` consecutive p-steps `a → … → a+r` has
`Λ` and `σ̄` constant on its `r + 1` states.  F1 is a hypothesis. -/
def BrSegGStatement (V : Type*) [Fintype V] : Prop :=
  ∀ (pr : V → ℕ), Function.Injective pr →
  ∀ (E : V → Finset V) (V0 : Finset V) (σ τ : ℕ → V → V) (a r : ℕ),
    -- Howard steps at every Even vertex
    (∀ t, a ≤ t → t < a + r → ∀ x ∈ V0,
      HowardAt pr E (nxt V0 σ τ t) (nxt V0 σ τ (t + 1)) x) →
    -- F1: `Ω_t ⊴ Ω_(t+1)` pointwise
    (∀ t, a ≤ t → t < a + r → ∀ v,
      Val.le pr (val pr (nxt V0 σ τ t) v) (val pr (nxt V0 σ τ (t + 1)) v)) →
    -- the steps are p-steps: `Λ` and `σ̄` are constant on the states `a, …, a+r`
    (∀ t, a ≤ t → t ≤ a + r → ∀ v, lam pr (nxt V0 σ τ t) v = lam pr (nxt V0 σ τ a) v) →
    (∀ t, a ≤ t → t ≤ a + r → ∀ v, v ∉ V0 → τ t v = τ a v) →
    -- H0
    (∀ t, a ≤ t → t < a + r → ∃ x ∈ V0, σ (t + 1) x ≠ σ t x ∧
      lam pr (nxt V0 σ τ t) x ≠ x ∧ lam pr (nxt V0 σ τ (t + 1)) x ≠ x) →
    r ≤ V0.card

/-- Lemma ONE-CROSS (R231 §2), from its three premises.  A gate has two faces `a`, `b`; `face t` is
the face `σ̄_t(g)` taken at state `t ≤ T`; `Ω t x` is the value of face `x` at state `t`, in any
preorder `α` (for the VJ order: `Val.le`, `Val.lt` under an injective priority function).  If
face `a` has the constant value `c`, then once the gate takes `a` it keeps `a`:
«σ̄_t(g) changes at most once over the run, and if it changes, it changes from the other face b
to a». -/
def OneCrossStatement (α : Type*) [Preorder α] (F : Type*) : Prop :=
  ∀ (a b : F) (T : ℕ) (face : ℕ → F) (Ω : ℕ → F → α) (c : α),
    -- the gate takes one of its two faces
    (∀ t, t ≤ T → face t = a ∨ face t = b) →
    -- the face `a` has a constant value
    (∀ t, t ≤ T → Ω t a = c) →
    -- F1 at the other face: `Ω_t(b) ⊴ Ω_(t+1)(b)`
    (∀ t, t < T → Ω t b ≤ Ω (t + 1) b) →
    -- NO-TIE: «Ω_t(e_g) ≠ Ω_t(β_g)»
    (∀ t, t ≤ T → Ω t a ≠ Ω t b) →
    -- LOC-GATE: the face taken has the smaller value, if the values differ
    (∀ t, t ≤ T → (face t = a → Ω t a ≠ Ω t b → Ω t a < Ω t b) ∧
                  (face t = b → Ω t b ≠ Ω t a → Ω t b < Ω t a)) →
    -- the states taking `b` are an initial segment, the rest takes `a`
    (∀ t t', t ≤ t' → t' ≤ T → face t = a → face t' = a) ∧
    -- at most one change, and it goes from `b` to `a`
    (∀ t, t < T → face (t + 1) ≠ face t → face t = b ∧ face (t + 1) = a) ∧
    (∀ t t', t < T → t' < T → face (t + 1) ≠ face t → face (t' + 1) ≠ face t' → t = t')

end

end PG
