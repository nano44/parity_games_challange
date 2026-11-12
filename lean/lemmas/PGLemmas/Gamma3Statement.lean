/-
STATEMENTS ONLY on Γ3(G) / Γ3*(G*) (PGLemmas/Gamma3.lean, accepted by the Lead 2026-11-12 22:22Z).
ACCEPTED by the Lead (2026-11-12 22:56Z): «PadStatement: ACCEPT, with deviations (i)-(iii) as you named them …
Your form is STRONGER in two ways: it holds for every legal successor map, not only states on the run; carriers
need only Ω ≥ 3.  Both are fine.»  «Record (iii) clearly: PAD (c), the value transport, is not stated.»
«Gamma3OldStatement: ACCEPT.»  «Gamma3CardStatement: ACCEPT.»  Proofs: `pad` (PGLemmas/Gamma3Pad.lean),
`gamma3_old`, `gamma3_card` (PGLemmas/Gamma3Basic.lean).

* `PadStatement`  RESULTS R117's Lemma PAD, (a) and (b), in the wording of P-N5-REACH §5 (claude/l-new
  e7dff7d1): «(a) Every cycle of Γ3 other than the self-loop of c_X contains a vertex of Ω ≥ 3. (b) Hence,
  for every pair of positional strategies and every vertex v ≠ c_X, the cycle node c of v's play has
  Ω(c) ≥ 3 > Ω(p) for every pad p: no pad is a cycle node and no pad is in a P-set.»
  Reading: a pair of positional strategies is one successor map `s` with `s v ∈ E3 v` at every vertex
  (as `pair` in Defs.lean); the cycle node is `lam (pr3 π) s v`, the P-set `pset (pr3 π) s v`
  (Defs.lean).  (a) is stated through the cycle node: «the cycle of v's play, unless it is c_X's loop,
  has a vertex of Ω ≥ 3» is «Ω(lam v) ≥ 3 unless lam v = c_X», since lam v has the largest p' on the
  cycle and p' orders by Ω first.
  DEVIATIONS: (i) the carriers need only Ω ≥ 3 (the text: ≥ 6, [FREE]: ≥ 6); the statement assumes
  `3 ≤ π.pb o`, `3 ≤ π.pe o` and nothing else (no `G.WF`, no `Carrier.WF`), so it covers Γ3(G)
  (`π = G.r104`) and every Γ3*(G*); (ii) «no pad is a cycle node» and «no pad is in a P-set» are stated for
  EVERY vertex v, c_X included (c_X's play is its loop: cycle node c_X, empty P-set); (iii) PAD (c) (values
  in Γ3 = values in Γ with padded lengths) is NOT stated: it needs the transport of strategies Γ ↔ Γ3,
  which Gamma3.lean does not define (its deviation (e)).  PAD (c), THE VALUE TRANSPORT, IS NOT STATED.
* `Gamma3OldStatement`  (i) Γ inside Γ3, [REACH] §3: «Γ3(G) is Γ(G) ([DEF], with its vertex indices,
  priorities and owners unchanged) with these pads»: for every vertex v of Γ, idx3, prio3 (π = G.r104)
  and the owner of `old v` are those of v; and «A PAD on an edge a → b is a new Even vertex p with the
  single edge p → b, the edge a → b being replaced by a → p»: b ∈ E a iff `old a` has the edge to `old b`
  or to a pad whose only successor is `old b`; and every successor of `old a` is of one of these two kinds.
* `Gamma3CardStatement`  (ii) the vertex count, R117: «n = N + 7M + 10»: card Vertex3 = N + 7M + 10, and
  under `G.WF` the index `idx3` is a bijection onto {0, …, N + 7M + 9} (injective, below n).
-/
import PGLemmas.Gamma3

namespace PG

namespace Genome

variable (G : Genome)

/-- The pads of Γ3(G). -/
def Vertex3.isPad : G.Vertex3 → Bool
  | .old _ => false
  | _ => true

/-- **Lemma PAD** (RESULTS R117; P-N5-REACH §5 (a), (b)). -/
def PadStatement : Prop :=
  ∀ π : G.Carrier, (∀ o, 3 ≤ π.pb o) → (∀ o, 3 ≤ π.pe o) →
    ∀ s : G.Vertex3 → G.Vertex3, (∀ v, s v ∈ G.E3 v) → ∀ v,
      (lam (G.pr3 π) s v ≠ .old .cX → 3 ≤ G.prio3 π (lam (G.pr3 π) s v)) ∧
      Vertex3.isPad G (lam (G.pr3 π) s v) = false ∧
      ∀ p ∈ pset (G.pr3 π) s v, Vertex3.isPad G p = false

/-- **Γ inside Γ3** ([REACH] §3: indices, priorities and owners unchanged; pads on edges). -/
def Gamma3OldStatement : Prop :=
  (∀ v : G.Vertex, G.idx3 (.old v) = G.idx v ∧ G.prio3 G.r104 (.old v) = G.prio v ∧
      G.isOdd3 (.old v) = G.isOdd v) ∧
  (∀ a b : G.Vertex, b ∈ G.E a ↔
      (Vertex3.old b ∈ G.E3 (.old a) ∨
        ∃ p, Vertex3.isPad G p = true ∧ p ∈ G.E3 (.old a) ∧ G.E3 p = {.old b})) ∧
  (∀ a : G.Vertex, ∀ w ∈ G.E3 (.old a),
      (∃ b, w = .old b) ∨ (Vertex3.isPad G w = true ∧ ∃ b, G.E3 w = {.old b}))

/-- **The vertex count** (R117: «n = N + 7M + 10»). -/
def Gamma3CardStatement : Prop :=
  Fintype.card G.Vertex3 = G.N + 7 * G.M + 10 ∧
  (G.WF → Function.Injective G.idx3 ∧ ∀ v, G.idx3 v < G.N + 7 * G.M + 10)

end Genome

end PG
