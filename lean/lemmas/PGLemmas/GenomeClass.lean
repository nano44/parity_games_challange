/-
Box 208 §1-§2 (claude/l-new 8db300fe docs/new/N5-LEVEL-box208.md) on the game Γ(G) of
`PGLemmas/Genome.lean`: classes, their order, and the five class facts (K1)-(K5) as Lean
propositions.  DEFINITIONS AND STATEMENTS ONLY; PROPOSED to the Lead for the diff.

Lane text, §1: «E_t(v) := the e-vertices of Π_t(v); class_t(v) := (Λ_t(v), E_t(v))».
«ORDER ON CLASSES: (Λ, E) < (Λ′, E′) iff reward(Λ) < reward(Λ′), or Λ = Λ′ and E <lex E′ (the most
relevant element of E Δ E′ lies in E′).»

§2: «(K1) MONOTONE.  class_t(v) ≤ class_(t+1)(v) for every vertex v and step t.»
«(K2) COARSE.  Let Ω = (Λ, Π, ·), Ω′ = (Λ′, Π′, ·) be values of two vertices outside the core, at
the same state or at two states, with classes c, c′.  If Ω ⊴ Ω′ then c ≤ c′.»
«(K3) ALONG THE PLAY.  At every state t: (a) Λ_t(v) = Λ_t(s_t(v)) for every vertex; (b) no
e-vertex lies on the cycle of a play; (c) class_t(v) = class_t(s_t(v)) for every vertex v that is
not an e-vertex; (d) for an e-vertex e whose successor w is a mover: class_t(e) = (Λ_t(w), {e} ∪
E_t(w)), e ∉ E_t(w), so class_t(e) > class_t(w); (e) the classes of K0, K1, K2, K3, c_W, c_X and
of the e-vertices with successor c_W are the same at every state.»
«(K4) GATES.  class_t(g) = min(class_t(e_g), class_t(β_g)) for every gate g and state t.»
«(K5) HOWARD DOMINATES.  For every mover x, step t and gate y of x: class_(t+1)(x) ≥ class_t(y).»

Encoding.  A «state» is a pair (σ, τ) with `τ` an optimal counterstrategy against `σ`
(`OptCounter`) whose successor map `pair G.V0 σ τ` is a state of IDEAL-CYC(G) (`IsState`); (K1)
and (K5) are about two consecutive states of a run (`IdealCycRun`).  (K2) is stated for any two
`IsState` maps with `K2 → K1` (which holds at every state: `loc_k2`).  (K3) (e) is stated with the
values of the constant classes.
-/
import PGLemmas.GenomeBOnly

namespace PG

open Classical
open scoped symmDiff

noncomputable section

namespace Genome

variable (G : Genome)

/-- The core `K0, K1, K2, K3`. -/
def isCore : G.Vertex → Bool
  | .K0 => true
  | .K1 => true
  | .K2 => true
  | .K3 => true
  | _ => false

/-- «E_t(v) := the e-vertices of Π_t(v)». -/
def eset (s : G.Vertex → G.Vertex) (v : G.Vertex) : Finset G.Vertex :=
  (pset G.pr s v).filter (fun u => G.isE u = true)

/-- «class_t(v) := (Λ_t(v), E_t(v))». -/
def cls (s : G.Vertex → G.Vertex) (v : G.Vertex) : G.Vertex × Finset G.Vertex :=
  (lam G.pr s v, G.eset s v)

/-- «(Λ, E) < (Λ′, E′) iff reward(Λ) < reward(Λ′), or Λ = Λ′ and E <lex E′ (the most relevant
element of E Δ E′ lies in E′).» -/
def clsLt (c c' : G.Vertex × Finset G.Vertex) : Prop :=
  rew G.pr c.1 < rew G.pr c'.1 ∨
  (c.1 = c'.1 ∧ ∃ d ∈ c.2 ∆ c'.2, (∀ x ∈ c.2 ∆ c'.2, G.pr x ≤ G.pr d) ∧ d ∈ c'.2)

/-- `≤` on classes. -/
def clsLe (c c' : G.Vertex × Finset G.Vertex) : Prop := G.clsLt c c' ∨ c = c'

/-- **(K2) COARSE.** -/
def K2Statement : Prop :=
  G.WF → ∀ s s' : G.Vertex → G.Vertex, G.IsState s → G.IsState s' →
    s Vertex.K2 = Vertex.K1 → s' Vertex.K2 = Vertex.K1 →
    ∀ u v : G.Vertex, G.isCore u = false → G.isCore v = false →
      Val.le G.pr (val G.pr s u) (val G.pr s' v) → G.clsLe (G.cls s u) (G.cls s' v)

/-- **(K3) ALONG THE PLAY**, at a state `s = pair G.V0 σ τ` with `τ` optimal against `σ`. -/
def K3Statement : Prop :=
  G.WF → ∀ σ τ : G.Vertex → G.Vertex, OptCounter G.pr G.E G.V0 σ τ →
    G.IsState (pair G.V0 σ τ) →
    -- (a)
    (∀ v, lam G.pr (pair G.V0 σ τ) v = lam G.pr (pair G.V0 σ τ) (pair G.V0 σ τ v)) ∧
    -- (b)
    (∀ v o, ¬ OnCycle (pair G.V0 σ τ) v (Vertex.eface o)) ∧
    -- (c)
    (∀ v, G.isE v = false →
      G.cls (pair G.V0 σ τ) v = G.cls (pair G.V0 σ τ) (pair G.V0 σ τ v)) ∧
    -- (d)
    (∀ o y, G.wt o = some y →
      G.cls (pair G.V0 σ τ) (Vertex.eface o) =
        (lam G.pr (pair G.V0 σ τ) (Vertex.mover y),
          insert (Vertex.eface o) (G.eset (pair G.V0 σ τ) (Vertex.mover y))) ∧
      Vertex.eface o ∉ G.eset (pair G.V0 σ τ) (Vertex.mover y) ∧
      G.clsLt (G.cls (pair G.V0 σ τ) (Vertex.mover y))
        (G.cls (pair G.V0 σ τ) (Vertex.eface o))) ∧
    -- (e)
    (G.cls (pair G.V0 σ τ) Vertex.K0 = (Vertex.K1, ∅) ∧
      G.cls (pair G.V0 σ τ) Vertex.K1 = (Vertex.K1, ∅) ∧
      G.cls (pair G.V0 σ τ) Vertex.K2 = (Vertex.K1, ∅) ∧
      G.cls (pair G.V0 σ τ) Vertex.K3 = (Vertex.K1, ∅) ∧
      G.cls (pair G.V0 σ τ) Vertex.cW = (Vertex.cW, ∅) ∧
      G.cls (pair G.V0 σ τ) Vertex.cX = (Vertex.cX, ∅) ∧
      ∀ o, G.wt o = none → G.cls (pair G.V0 σ τ) (Vertex.eface o) = (Vertex.cW, ∅))

/-- **(K4) GATES**, at a state `s = pair G.V0 σ τ` with `τ` optimal against `σ`: the class of a
gate is the smaller of the classes of its two faces. -/
def K4Statement : Prop :=
  G.WF → ∀ σ τ : G.Vertex → G.Vertex, OptCounter G.pr G.E G.V0 σ τ →
    G.IsState (pair G.V0 σ τ) → ∀ o : G.Opt,
      (G.cls (pair G.V0 σ τ) (Vertex.gate o) = G.cls (pair G.V0 σ τ) (Vertex.eface o) ∨
        G.cls (pair G.V0 σ τ) (Vertex.gate o) = G.cls (pair G.V0 σ τ) (Vertex.beta o)) ∧
      G.clsLe (G.cls (pair G.V0 σ τ) (Vertex.gate o)) (G.cls (pair G.V0 σ τ) (Vertex.eface o)) ∧
      G.clsLe (G.cls (pair G.V0 σ τ) (Vertex.gate o)) (G.cls (pair G.V0 σ τ) (Vertex.beta o))

/-- **(K1) MONOTONE**, along a run of IDEAL-CYC(G). -/
def K1Statement : Prop :=
  G.WF → ∀ (σ τ : ℕ → G.Vertex → G.Vertex) (T : ℕ), G.IdealCycRun σ τ T →
    ∀ t, t < T → ∀ v,
      G.clsLe (G.cls (nxt G.V0 σ τ t) v) (G.cls (nxt G.V0 σ τ (t + 1)) v)

/-- **(K5) HOWARD DOMINATES**, along a run of IDEAL-CYC(G). -/
def K5Statement : Prop :=
  G.WF → ∀ (σ τ : ℕ → G.Vertex → G.Vertex) (T : ℕ), G.IdealCycRun σ τ T →
    ∀ t, t < T → ∀ x, ∀ y ∈ G.E (Vertex.mover x),
      G.clsLe (G.cls (nxt G.V0 σ τ t) y) (G.cls (nxt G.V0 σ τ (t + 1)) (Vertex.mover x))

end Genome

end

end PG
