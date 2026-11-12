/-
Box 208 Addendum A, Lemma PLATEAU (claude/l-new 8db300fe docs/new/N5-LEVEL-box208.md, A2): the
abstract one-player form that its steps (P5) and (P7) reduce to, as a Lean proposition.

Lane text.  (P5): «The game H: vertices Y; a mover of Y keeps all its gates; every other vertex x
of Y keeps the single successor s_u(x) […] H is a parity game in which only the movers of Y have a
choice.  […] So σ_u, σ_(u+1), …, σ_(v+1), restricted to Y, are consecutive states of the Howard run
of H from σ_u restricted to Y, as long as that run has not stopped.»  (P7): «The steps u → u + 1,
…, v − 1 → v of H's Howard run change σ (P6), change no cycle node (P1) and no Odd choice (there
is none in H): they are v − u consecutive p-steps.  […] By BR-SEG-G (a), v − u ≤ n_E(H)».

What is stated here: a set `Y` of vertices of ANY game, and a window `a..b` of states, with
(P1)-(P4) and (P6) as HYPOTHESES in the form (P5), (P7) use them:
* (P2) `Y` is closed under the successor map of every state of the window;
* (P4), (P5) a vertex of `Y` outside `Ch` keeps its successor on the window (`Ch` = the movers of Y);
* (P3) every successor of a vertex of `Ch` is in `Y`, and the states follow the edges at `Ch`;
* Howard steps at `Ch` (values and Howard's step as in `PGLemmas/Defs.lean`);
* (P1) no vertex of `Y` changes its cycle node on the window;
* (P6) every step of the window changes the state at a vertex of `Ch`.
Conclusion: `b − a ≤ |Ch|`.  Nothing is assumed about the vertices outside `Y`, and no premise
(M) / F1 is assumed.

NOT stated here (genome facts, not formalized): that a plateau of IDEAL-CYC satisfies (P1)-(P4),
(P6).  The constant: `|Ch|` is the number of movers in Y (≤ N), where A2 (P7) has
n_E(H) ≤ N + 2M + 5 from BR-SEG-G (a); the sharper count is LAM-GAP SHARP's.
-/
import PGLemmas.Defs

namespace PG

noncomputable section

/-- **PLATEAU, abstract one-player form** (box 208 Addendum A2, steps (P5) + (P7)). -/
def PlateauStatement (V : Type*) [Fintype V] : Prop :=
  ∀ (pr : V → ℕ), Function.Injective pr →
  ∀ (E : V → Finset V) (Y Ch : Finset V), Ch ⊆ Y →
  ∀ (s : ℕ → V → V) (a b : ℕ), a ≤ b →
    -- (P2) `Y` is closed under the plays of every state of the window
    (∀ t, a ≤ t → t ≤ b → ∀ x ∈ Y, s t x ∈ Y) →
    -- (P4), (P5) in `Y` only the vertices of `Ch` change their successor
    (∀ t, a ≤ t → t ≤ b → ∀ x ∈ Y, x ∉ Ch → s t x = s a x) →
    -- (P3) the successors of a vertex of `Ch` are in `Y`
    (∀ x ∈ Ch, E x ⊆ Y) →
    -- the states follow the edges at `Ch`
    (∀ t, a ≤ t → t ≤ b → ∀ x ∈ Ch, s t x ∈ E x) →
    -- Howard steps at `Ch`
    (∀ t, a ≤ t → t < b → ∀ x ∈ Ch, HowardAt pr E (s t) (s (t + 1)) x) →
    -- (P1) no vertex of `Y` changes its cycle node
    (∀ t, a ≤ t → t ≤ b → ∀ x ∈ Y, lam pr (s t) x = lam pr (s a) x) →
    -- (P6) every step changes the state at a vertex of `Ch`
    (∀ t, a ≤ t → t < b → ∃ x ∈ Ch, s (t + 1) x ≠ s t x) →
    b - a ≤ Ch.card

end

end PG
