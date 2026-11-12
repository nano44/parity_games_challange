/-
RF-A (the Lead, 2026-11-12 19:00Z, for L-NEW's box 212): the rule-free part of box 208 on the
genome.  DEFINITION AND STATEMENTS ONLY (accepted by the Lead 19:05Z; `ImpK5NewStatement`, added at his request,
accepted 19:13Z; it is stated for every mover, moved or not).
Proofs: `PGLemmas/GenomeImp.lean`.

The Lead's wording: «Define IdealImpRun: IdealCycRun with `howard` replaced by «each step moves a
non-empty set of movers, each to a gate strictly ⊴-better under the current values; every other
mover keeps its gate».»  «state the rule-free versions for IdealImpRun of those that do not need
it, plus «at most P = 2M(N + 2M) non-stall steps for every reference state b».»

`IdealImpRun σ τ T` is `IdealCycRun σ τ T` (`PGLemmas/Genome.lean`) with the fields `howard` and
`moves` replaced by `improve` (every mover keeps its gate or moves to a gate of strictly larger
value under Ω_t) and `moves` (some mover moves).  Every Howard run is such a run (to be proved:
`IdealCycRun.toImp`), so each rule-free statement contains its Howard form.

WHERE `howard` IS USED in the proofs of commit e14f5508 (read off the proof terms):
* NOT used: (K2), (K3), (K4) (statements about one state); (K1) beyond F1, and F1 needs only
  «kept or strictly improved», which is `IdealImpRun.improve`; (L2), (L3), (L5); `level_count`'s
  hypotheses (K1), the set of front classes and the bound on fronts; (P4) `IdealCycRun.gate_const`
  (Odd does not move on a set whose classes are constant).
* USED: (K5) (`howard`'s clause «the new successor is ⊴-best»); `plateau_g`: (P3) through (K5),
  (P6) through the clauses «⊴-best» and «keeps the current gate if it is ⊴-best», (P5) + (P7)
  through `plateau`, which is LAM-GAP SHARP, a statement about Howard's step; `quiet` through the
  same window lemma; `all_tcyc`, `all_tcyc_sharp` through `plateau_g` and `quiet`; `run_exists`
  (it constructs Howard's run).
So the stalls are where the rule enters: the number of NON-stall steps is rule-free.

Statements (LAG, FRONT, STALL as in `PGLemmas/GenomeLevelStatement.lean`, on the keys `G.ck`):
* `NonStallCountStatement`  abstract (no genome): classes in a linear order that never fall, the
  front's class in a set M, fronts of at most F vertices ⇒ at most |M|·F steps t with a ≤ t < b
  at which something lags and the step is not a stall.  (Box 208 §4 (C1), (C2): «the number of
  non-stall steps on [a, b′] is exactly q ≤ P».)
* `ImpK1Statement`, `ImpL2Statement`, `ImpL3Statement`, `ImpL5Statement`  (K1), (L2), (L3), (L5)
  for `IdealImpRun`, word for word as for `IdealCycRun`.
* `ImpNonStallStatement`  for every `IdealImpRun` and every reference state b: at most
  P = 2M(N + 2M) steps t < b at which something lags and the step is not a stall.
* `ImpK5NewStatement`  the rule-free remnant of (K5): the class at t of the NEW gate of a mover is
  at most the class of the mover at t + 1.
-/
import PGLemmas.GenomeLevelStatement

namespace PG

open Classical

noncomputable section

/-- **The count of non-stall steps**, abstract (box 208 §4 (C1), (C2)). -/
def NonStallCountStatement (V : Type*) [Fintype V] (α : Type*) [LinearOrder α] : Prop :=
  ∀ (c : ℕ → V → α) (a b : ℕ) (M : Finset α) (F : ℕ),
    -- (K1) no class falls
    (∀ t, a ≤ t → t < b → ∀ v, c t v ≤ c (t + 1) v) →
    -- the front's class lies in `M`
    (∀ t, a ≤ t → t ≤ b → ∀ v, FrontAt c b t v → c t v ∈ M) →
    -- the front has at most `F` vertices
    (∀ t, a ≤ t → t ≤ b → (Finset.univ.filter (FrontAt c b t)).card ≤ F) →
    ((Finset.Ico a b).filter (fun t => (∃ v, c t v ≠ c b v) ∧ ¬ StallAt c b t)).card ≤ M.card * F

namespace Genome

variable (G : Genome)

/-- A run `σ 0, …, σ T` of IDEAL-CYC(G) under an ARBITRARY improvement rule: `IdealCycRun` with
Howard's step replaced by «each step moves a non-empty set of movers, each to a gate strictly
⊴-better under the current values; every other mover keeps its gate». -/
structure IdealImpRun (σ τ : ℕ → G.Vertex → G.Vertex) (T : ℕ) : Prop where
  /-- every Even vertex that is not a mover is frozen at its start successor -/
  frozen : ∀ t, t ≤ T → ∀ v ∈ G.V0, (∀ x, v ≠ Vertex.mover x) → σ t v = G.start0 v
  /-- a state carries a choice at every mover: one of its gates -/
  legal : ∀ t, t ≤ T → ∀ x, σ t (Vertex.mover x) ∈ G.E (Vertex.mover x)
  /-- `τ t` is an optimal counterstrategy against `σ t` -/
  opt : ∀ t, t ≤ T → OptCounter G.pr G.E G.V0 (σ t) (τ t)
  /-- every mover keeps its gate or moves to a gate of strictly larger value under `Ω_t` -/
  improve : ∀ t, t < T → ∀ x, σ (t + 1) (Vertex.mover x) = σ t (Vertex.mover x) ∨
    Val.lt G.pr (val G.pr (nxt G.V0 σ τ t) (σ t (Vertex.mover x)))
      (val G.pr (nxt G.V0 σ τ t) (σ (t + 1) (Vertex.mover x)))
  /-- every step moves some mover -/
  moves : ∀ t, t < T → ∃ x, σ (t + 1) (Vertex.mover x) ≠ σ t (Vertex.mover x)

/-- **(K1) MONOTONE**, rule-free. -/
def ImpK1Statement : Prop :=
  G.WF → ∀ (σ τ : ℕ → G.Vertex → G.Vertex) (T : ℕ), G.IdealImpRun σ τ T →
    ∀ t, t < T → ∀ v,
      G.clsLe (G.cls (nxt G.V0 σ τ t) v) (G.cls (nxt G.V0 σ τ (t + 1)) v)

/-- **(L2)**, rule-free. -/
def ImpL2Statement : Prop :=
  G.WF → ∀ (σ τ : ℕ → G.Vertex → G.Vertex) (T : ℕ), G.IdealImpRun σ τ T →
    ∀ b t, t ≤ b → b ≤ T → ∀ v, FrontAt (G.ck σ τ) b t v →
      (∃ x, v = Vertex.mover x) ∨ (∃ o, v = Vertex.gate o) ∨
        (∃ o y, v = Vertex.beta o ∧ G.xt o = some y)

/-- **(L3)**, rule-free. -/
def ImpL3Statement : Prop :=
  G.WF → ∀ (σ τ : ℕ → G.Vertex → G.Vertex) (T : ℕ), G.IdealImpRun σ τ T →
    ∀ b t, t ≤ b → b ≤ T → (∃ v, G.ck σ τ t v ≠ G.ck σ τ b v) →
      (∃ x, FrontAt (G.ck σ τ) b t (Vertex.mover x) ∧
        G.ck σ τ t (σ t (Vertex.mover x)) = G.ck σ τ b (σ t (Vertex.mover x)) ∧
        G.cls (nxt G.V0 σ τ t) (Vertex.mover x) =
          G.cls (nxt G.V0 σ τ b) (σ t (Vertex.mover x))) ∨
      (∃ v o, lam G.pr (nxt G.V0 σ τ t) v = Vertex.beta o ∧
        (∀ u, OnCycle (nxt G.V0 σ τ t) v u → FrontAt (G.ck σ τ) b t u ∧
          ((∃ x, u = Vertex.mover x) ∨ (∃ o', u = Vertex.gate o') ∨
            (∃ o', u = Vertex.beta o'))) ∧
        G.cls (nxt G.V0 σ τ t) (Vertex.beta o) = (Vertex.beta o, ∅))

/-- **(L5)**, as its two factors, rule-free. -/
def ImpL5Statement : Prop :=
  G.WF → ∀ (σ τ : ℕ → G.Vertex → G.Vertex) (T : ℕ), G.IdealImpRun σ τ T →
    ∀ b t, t ≤ b → b ≤ T →
      (∀ v, FrontAt (G.ck σ τ) b t v →
        (∃ o, G.cls (nxt G.V0 σ τ t) v = G.cls (nxt G.V0 σ τ b) (Vertex.gate o)) ∨
        (∃ o, G.cls (nxt G.V0 σ τ t) v = (Vertex.beta o, ∅))) ∧
      (Finset.univ.filter (FrontAt (G.ck σ τ) b t)).card ≤ G.N + 2 * G.M

/-- **At most P = 2M(N + 2M) non-stall steps**, for every improvement rule and every reference
state `b`: the steps `t < b` at which something lags and that are not stalls. -/
def ImpNonStallStatement : Prop :=
  G.WF → ∀ (σ τ : ℕ → G.Vertex → G.Vertex) (T : ℕ), G.IdealImpRun σ τ T →
    ∀ b, b ≤ T →
      ((Finset.range b).filter (fun t =>
        (∃ v, G.ck σ τ t v ≠ G.ck σ τ b v) ∧ ¬ StallAt (G.ck σ τ) b t)).card ≤
        2 * G.M * (G.N + 2 * G.M)

/-- **The rule-free remnant of (K5)** (asked for by the Lead, 2026-11-12 19:05Z: «for the NEW gate
y′ = σ_(t+1)(x), class_t(y′) ≤ class_(t+1)(x)»). -/
def ImpK5NewStatement : Prop :=
  G.WF → ∀ (σ τ : ℕ → G.Vertex → G.Vertex) (T : ℕ), G.IdealImpRun σ τ T →
    ∀ t, t < T → ∀ x,
      G.clsLe (G.cls (nxt G.V0 σ τ t) (σ (t + 1) (Vertex.mover x)))
        (G.cls (nxt G.V0 σ τ (t + 1)) (Vertex.mover x))

end Genome

end

end PG
