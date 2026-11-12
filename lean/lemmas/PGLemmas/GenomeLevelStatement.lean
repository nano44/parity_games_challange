/-
Box 208 §3 (Lemma LEVEL: (L2), (L3), (L5)), Addendum A (Lemma PLATEAU, Theorem ALL-TCYC) and the
quiet window of §4 (C4), on the game Γ(G) of `PGLemmas/Genome.lean`, as Lean propositions.
STATEMENTS ONLY; PROPOSED to the Lead for the diff (claude/l-new 311bbf81
docs/new/N5-LEVEL-box208.md; every statement of box 208 is a CANDIDATE in its lane).

Lane text, §3: «LAG_t := {v : class_t(v) ≠ class_b(v)}.»  «If LAG_t ≠ ∅: m_t := min{class_t(v) :
v ∈ LAG_t}; FRONT_t := {v ∈ LAG_t : class_t(v) = m_t}; Φ_t := (m_t, −|FRONT_t|)».  «A step
t → t + 1 with t < b and LAG_t ≠ ∅ is a STALL if class_(t+1)(v) = class_t(v) for every
v ∈ FRONT_t.»
«(L2) Every vertex of FRONT_t is a mover, a gate or a β-vertex whose frozen successor is a mover.»
«(L3) (α) some mover z ∈ FRONT_t has σ_t(z) ∉ LAG_t, and then m_t = class_b(σ_t(z)); or (β) there
is a play at t whose cycle consists of movers, their chosen gates and those gates' β-faces, all in
FRONT_t, and then m_t = (c, ∅) for its cycle node c, a β-vertex.»
«(L5) On [a, b] the potential Φ takes at most 2M·(N + 2M) values; at most M·(N + 2M) if case (β)
of (L3) never occurs on [a, b].»  Its proof: «By (L3), m_t is the class at b of one of the M gates
(case α) or (c, ∅) for one of the M β-vertices c (case β): at most 2M values, at most M without
case (β).  By (L2), 1 ≤ |FRONT_t| ≤ N + 2M.»
Addendum A0: «Lemma PLATEAU (CANDIDATE).  For every genome, every reference state b and every
maximal interval [u, v] of states of constant Φ (reference b): v − u ≤ N + 2M + 5.»
«Theorem ALL-TCYC (CANDIDATE).  For every genome G: T_CYC ≤ P·(N + 2M + 6) + N, P = 2M(N + 2M).»
§1, quoted there from RESULTS R126 QUIET-N: «every maximal window of quiet steps has at most N
steps»; §4 (C4): «the steps after b′ are quiet, and b − b′ ≤ N by QUIET-N».

Encoding.  A run is `G.IdealCycRun σ τ T`.  The class of `v` at state `t` is
`G.cls (nxt G.V0 σ τ t) v`; `G.ck σ τ t v` is its key in `ℤ ×ₗ ℤ` (`clsKey`,
`PGLemmas/GenomeOrderStatement.lean`).  LAG, FRONT and STALL are `FrontAt` and `StallAt` of
`PGLemmas/LevelCountStatement.lean` on these keys: by `ClassOrderStatement` the key is injective
and order-preserving, so «the key of v at t ≠ its key at b» is «class_t(v) ≠ class_b(v)» and the
lowest key is the lowest class.

DEVIATIONS, named:
* (L3) (β): the kinds of the cycle's vertices are stated (mover, gate or β-vertex, all in the
  front); that they alternate as mover → chosen gate → β-face → mover is not stated: it is what the
  successor map does on a cycle of such vertices.
* (L5) is stated as its two factors, the form `level_count` consumes: the front's class is the
  class at b of a gate or `(β, ∅)` for a β-vertex (so at most 2M classes), and a front has at most
  N + 2M vertices.  The clause «at most M·(N + 2M) if case (β) never occurs» is not stated.
* PLATEAU: the bound is N, the number of movers (`plateau`, LAM-GAP SHARP), where A0 has
  N + 2M + 5; and the interval is any interval of consecutive stalls (by §3 (L1) the steps inside
  an interval of constant Φ are stalls; maximality is not used).
* QUIET: stated for every window of a run on which no class changes, with no premise; RESULTS
  R126 QUIET-N is not used.
* ALL-TCYC: for EVERY run of IDEAL-CYC(G) of length T (any first mover state, not only the
  genome's start; not only the run to its stop), so in particular for T = T_CYC.  `AllTCycStatement`
  has the lane's bound; `AllTCycSharpStatement` has the bound the Lean route gives,
  2M(N + 2M)(N + 1) + N, which is at most the lane's.
* None of these is a TARGET.md statement: they bound the number of Howard steps of a model
  (IDEAL-CYC, RESULTS R118 (a)) on a restricted family of games (the genome games of R104).
-/
import PGLemmas.GenomeOrderStatement
import PGLemmas.LevelCountStatement

namespace PG

open Classical

noncomputable section

namespace Genome

variable (G : Genome)

/-- The class of `v` at state `t` of a run, as a key in `ℤ ×ₗ ℤ`. -/
def ck (σ τ : ℕ → G.Vertex → G.Vertex) (t : ℕ) (v : G.Vertex) : ℤ ×ₗ ℤ :=
  G.clsKey (G.cls (nxt G.V0 σ τ t) v)

/-- **(L2)**: a vertex of the front is a mover, a gate or a β-vertex whose frozen successor is a
mover. -/
def L2Statement : Prop :=
  G.WF → ∀ (σ τ : ℕ → G.Vertex → G.Vertex) (T : ℕ), G.IdealCycRun σ τ T →
    ∀ b t, t ≤ b → b ≤ T → ∀ v, FrontAt (G.ck σ τ) b t v →
      (∃ x, v = Vertex.mover x) ∨ (∃ o, v = Vertex.gate o) ∨
        (∃ o y, v = Vertex.beta o ∧ G.xt o = some y)

/-- **(L3)**: at a state `t` at which something lags, (α) a mover of the front has a successor
that does not lag, and then the front's class is the class at `b` of that successor; or (β) a
play at `t` has a cycle of movers, gates and β-vertices, all in the front, its cycle node is a
β-vertex `c`, and the front's class is `(c, ∅)`. -/
def L3Statement : Prop :=
  G.WF → ∀ (σ τ : ℕ → G.Vertex → G.Vertex) (T : ℕ), G.IdealCycRun σ τ T →
    ∀ b t, t ≤ b → b ≤ T → (∃ v, G.ck σ τ t v ≠ G.ck σ τ b v) →
      -- (α)
      (∃ x, FrontAt (G.ck σ τ) b t (Vertex.mover x) ∧
        G.ck σ τ t (σ t (Vertex.mover x)) = G.ck σ τ b (σ t (Vertex.mover x)) ∧
        G.cls (nxt G.V0 σ τ t) (Vertex.mover x) =
          G.cls (nxt G.V0 σ τ b) (σ t (Vertex.mover x))) ∨
      -- (β)
      (∃ v o, lam G.pr (nxt G.V0 σ τ t) v = Vertex.beta o ∧
        (∀ u, OnCycle (nxt G.V0 σ τ t) v u → FrontAt (G.ck σ τ) b t u ∧
          ((∃ x, u = Vertex.mover x) ∨ (∃ o', u = Vertex.gate o') ∨
            (∃ o', u = Vertex.beta o'))) ∧
        G.cls (nxt G.V0 σ τ t) (Vertex.beta o) = (Vertex.beta o, ∅))

/-- **(L5)**, as its two factors: the class of a front vertex is the class at `b` of a gate or
`(β, ∅)` for a β-vertex, and a front has at most `N + 2M` vertices. -/
def L5Statement : Prop :=
  G.WF → ∀ (σ τ : ℕ → G.Vertex → G.Vertex) (T : ℕ), G.IdealCycRun σ τ T →
    ∀ b t, t ≤ b → b ≤ T →
      (∀ v, FrontAt (G.ck σ τ) b t v →
        (∃ o, G.cls (nxt G.V0 σ τ t) v = G.cls (nxt G.V0 σ τ b) (Vertex.gate o)) ∨
        (∃ o, G.cls (nxt G.V0 σ τ t) v = (Vertex.beta o, ∅))) ∧
      (Finset.univ.filter (FrontAt (G.ck σ τ) b t)).card ≤ G.N + 2 * G.M

/-- **Lemma PLATEAU** (Addendum A), with the bound `N`: an interval of consecutive stalls
(reference state `b`) has at most `N` steps. -/
def PlateauGStatement : Prop :=
  G.WF → ∀ (σ τ : ℕ → G.Vertex → G.Vertex) (T : ℕ), G.IdealCycRun σ τ T →
    ∀ b u v, u ≤ v → v ≤ b → b ≤ T →
      (∀ t, u ≤ t → t < v → StallAt (G.ck σ τ) b t) → v - u ≤ G.N

/-- **QUIET** (the content of RESULTS R126 QUIET-N, used in §4 (C4)): a window of a run on which
no vertex changes its class has at most `N` steps. -/
def QuietStatement : Prop :=
  G.WF → ∀ (σ τ : ℕ → G.Vertex → G.Vertex) (T : ℕ), G.IdealCycRun σ τ T →
    ∀ u v, u ≤ v → v ≤ T →
      (∀ t, u ≤ t → t ≤ v → ∀ x, G.cls (nxt G.V0 σ τ t) x = G.cls (nxt G.V0 σ τ u) x) →
      v - u ≤ G.N

/-- **Theorem ALL-TCYC** (Addendum A0), with the lane's bound `P·(N + 2M + 6) + N`,
`P = 2M(N + 2M)`: every run of IDEAL-CYC(G) has at most that many steps. -/
def AllTCycStatement : Prop :=
  G.WF → ∀ (σ τ : ℕ → G.Vertex → G.Vertex) (T : ℕ), G.IdealCycRun σ τ T →
    T ≤ 2 * G.M * (G.N + 2 * G.M) * (G.N + 2 * G.M + 6) + G.N

/-- ALL-TCYC with the bound of the Lean route, `P·(N + 1) + N`. -/
def AllTCycSharpStatement : Prop :=
  G.WF → ∀ (σ τ : ℕ → G.Vertex → G.Vertex) (T : ℕ), G.IdealCycRun σ τ T →
    T ≤ 2 * G.M * (G.N + 2 * G.M) * (G.N + 1) + G.N

end Genome

end

end PG
