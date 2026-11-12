/-
ClassOrder: the order on classes of box 208 §1 (claude/l-new docs/new/N5-LEVEL-box208.md) is a
strict total order, with an order-embedding into `ℤ ×ₗ ℤ`.  DEFINITION AND STATEMENT ONLY; asked
for by the Lead (2026-11-12 15:50Z, 17:22Z); PROPOSED for the diff.

Lane text, §1: «ORDER ON CLASSES: (Λ, E) < (Λ′, E′) iff reward(Λ) < reward(Λ′), or Λ = Λ′ and
E <lex E′ (the most relevant element of E Δ E′ lies in E′).  It is a strict total order on the
classes that occur: the cycle nodes are β-vertices, K1, K2, c_X or c_W (B-ONLY and its two
exceptions), with pairwise different priorities (R104: «a distinct β-rank»), hence different
rewards; the lex order is total (box 207 Addendum B).»

DEVIATION, named: the statement below is STRONGER than the lane's sentence.  It is about ALL pairs
`(Λ, E)` of a vertex and a finite set of vertices, not only about the classes that occur: under
`G.WF` the priority `G.pr` is injective (`pr_injective`), so distinct vertices have distinct
rewards and a non-empty symmetric difference has exactly one most relevant element.  B-ONLY is
not used.

The key `clsKey (Λ, E) = (rew Λ, Σ_{x ∈ E} 2^(pr x))`, ordered lexicographically, is what gives
`level_count` (`PGLemmas/LevelCount.lean`) its `LinearOrder`: take `α := ℤ ×ₗ ℤ` and
`c t v := G.clsKey (G.cls (nxt G.V0 σ τ t) v)`.
-/
import PGLemmas.GenomeClass
import PGLemmas.Weights
import Mathlib.Order.Prod.Lex.Basic

namespace PG

open Classical

noncomputable section

namespace Genome

variable (G : Genome)

/-- The key of a class `(Λ, E)`: the reward of `Λ`, then the weight `Σ_{x ∈ E} 2^(pr x)` of `E`
(`pw`, `PGLemmas/Weights.lean`), in the lexicographic order of `ℤ ×ₗ ℤ`. -/
def clsKey (c : G.Vertex × Finset G.Vertex) : ℤ ×ₗ ℤ := toLex (rew G.pr c.1, pw G.pr c.2)

/-- **ClassOrder** (box 208 §1: «It is a strict total order on the classes that occur»), for all
pairs `(Λ, E)`: `clsLt` is irreflexive, transitive and total, and `clsKey` is an order-embedding
for `clsLt` and for `clsLe`. -/
def ClassOrderStatement : Prop :=
  G.WF →
    -- irreflexive
    (∀ c : G.Vertex × Finset G.Vertex, ¬ G.clsLt c c) ∧
    -- transitive
    (∀ c c' c'' : G.Vertex × Finset G.Vertex, G.clsLt c c' → G.clsLt c' c'' → G.clsLt c c'') ∧
    -- total
    (∀ c c' : G.Vertex × Finset G.Vertex, G.clsLt c c' ∨ c = c' ∨ G.clsLt c' c) ∧
    -- the order-embedding
    (∀ c c' : G.Vertex × Finset G.Vertex, G.clsLt c c' ↔ G.clsKey c < G.clsKey c') ∧
    (∀ c c' : G.Vertex × Finset G.Vertex, G.clsLe c c' ↔ G.clsKey c ≤ G.clsKey c')

end Genome

end

end PG
