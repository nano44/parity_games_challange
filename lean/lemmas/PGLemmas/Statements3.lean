/-
Premise (M) for one-player games, as a statement (proposed to the Lead; same convention).

* `ValMonoStatement`  RESULTS R15 (a) Lemma A = VJ00 Lemma 5.7 («σ ⊑ Improve(σ)») in the case
                      where the opponent has no choice: if every vertex keeps its successor or
                      moves to a successor of strictly larger value, no value falls.
* `HowardRunOnePlayerStatement`, `LamGapOnePlayerNoMStatement`: the Howard run bound and
                      LAM-GAP SHARP for one-player games with NO premise (M).
-/
import PGLemmas.Defs

namespace PG

noncomputable section

/-- **(M), one-player.**  `s` and `s'` give every vertex its successor.  If every vertex either
keeps its successor or moves to one whose value under `s` is strictly larger (VJ00 §4.4 (2): an
improvement; `s' = Switch_I(s)` for a set `I` of improvements), then every value under `s'` is
`⊵` its value under `s`. -/
def ValMonoStatement (V : Type*) [Fintype V] : Prop :=
  ∀ (pr : V → ℕ), Function.Injective pr → ∀ (s s' : V → V),
    (∀ v, s' v = s v ∨ Val.lt pr (val pr s (s v)) (val pr s (s' v))) →
    ∀ v, Val.le pr (val pr s v) (val pr s' v)

/-- LAM-GAP, SHARP form, for a one-player game, with no premise (M): `E` is the edge relation,
every vertex outside `Ch` has exactly one successor, every state follows the edges, every step is
a Howard step at `Ch`. -/
def LamGapOnePlayerNoMStatement (V : Type*) [Fintype V] : Prop :=
  ∀ (pr : V → ℕ), Function.Injective pr →
  ∀ (E : V → Finset V) (Ch : Finset V) (s : ℕ → V → V) (a b : ℕ),
    a ≤ b →
    (∀ v, v ∉ Ch → ∃ u, E v = {u}) →
    (∀ t, a ≤ t → t ≤ b → ∀ v, s t v ∈ E v) →
    (∀ t, a ≤ t → t < b → ∀ v ∈ Ch, HowardAt pr E (s t) (s (t + 1)) v) →
    (∀ t, a ≤ t → t ≤ b → ∀ v, lam pr (s t) v = lam pr (s a) v) →
    (∀ t, a ≤ t → t < b → s (t + 1) ≠ s t) →
    b - a ≤ Ch.card

/-- Howard's algorithm on a one-player game, with no premise: a run `s 0, …, s T` in which every
state follows the edges, every vertex outside `Ch` has exactly one successor, every step is a
Howard step at `Ch` and changes the state, has `T ≤ n(n − 1) + (n(n − 1) + 1)·|Ch|` steps. -/
def HowardRunOnePlayerStatement (V : Type*) [Fintype V] : Prop :=
  ∀ (pr : V → ℕ), Function.Injective pr →
  ∀ (E : V → Finset V) (Ch : Finset V) (s : ℕ → V → V) (T : ℕ),
    (∀ v, v ∉ Ch → ∃ u, E v = {u}) →
    (∀ t, t ≤ T → ∀ v, s t v ∈ E v) →
    (∀ t, t < T → ∀ v ∈ Ch, HowardAt pr E (s t) (s (t + 1)) v) →
    (∀ t, t < T → s (t + 1) ≠ s t) →
    T ≤ Fintype.card V * (Fintype.card V - 1) +
      (Fintype.card V * (Fintype.card V - 1) + 1) * Ch.card

end

end PG
