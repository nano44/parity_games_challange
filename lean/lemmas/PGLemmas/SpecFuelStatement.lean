/-
FUEL SUFFICIENCY of the Lean transcription of SPEC S1-S5 (PGLemmas/Spec.lean, definitions accepted by the Lead 03:58Z
with fixes U1-U4 + U-3, fixed in 9176725a).  STATEMENTS; the Lead's diff: ACCEPTED 08:42Z (draft dee24dfe,
with required changes R1, R2) and 08:44Z (draft 6b6a86af: FuelStatesStatement satisfies R1; «The four Fuel Statements are
accepted as written»; R2 = the paragraph on a record's `fuelOut` below).  Proofs: SpecFuel.lean.

What it says.  Spec.lean writes every loop of si.py's `Engine.evaluate` (DFS, BFS, longest path, the FIX 2 parent walk) as
a step function run by `loopFuel` with a fuel bound; reaching a bound sets the flag `fuelOut` (deviation of the
transcription, not of SPEC: si.py's loops are unbounded `while` loops).  The three Statements say that on a well-formed
game the bound is never reached:
  * `FuelEvalStatement`: one evaluation (S1, Even's strategy s on G) never sets `fuelOut`;
  * `FuelIterStatement`: no iteration record of `specIter` (S4a, S4b, S4c, from any pair (σ, τ) whose choices are
    vertices) has `fuelOut` set, for every iteration cap;
  * `FuelRunStatement`: the same for `specRun` from the S3 start (`start = none`) or from a given start file
    (`start = some (ss, ts)`, every listed pair an edge of the right owner), through `startPair`;
  * `FuelStatesStatement`: both S1 evaluations at every STATE of such a run (including S5's stopping call, which leaves
    no step record) never set `fuelOut`.
What a step record's `fuelOut` covers (Lead 08:42Z (R2)).  `specStep` (Spec.lean) sets
  `let fo := ov.fuelOut || od.fuelOut || A.2.1 || B.2.1`
and puts `fo` into every record it returns (fallback branches included): `ov` = S1 on G for σ (gives Iσ and σ's S4c
fallback values), `od` = S1 on G^d for τ (Iτ, τ's fallback values), `A` = S4a's call on dual(H) (made only if Iσ ≠ ∅; else
`false`), `B` = S4b's call on H′ (only if Iτ ≠ ∅).  `improving`, `arenaH`, `arenaH'`, `fallbackAt` have no fuel loop.  Proved
as `specStep_flag`, `stepA_flag`, `stepB_flag` (SpecFuel.lean).  Inside one S1 call (`Eng.evaluate` / `procNode`) every
fuel loop feeds its `fuelOut` except the cycle-node choice DFS and the FIX 2 walk at an EVEN cycle node, whose results are
discarded there (si.py l. 182 runs them only for Odd v); FuelEvalStatement covers the flag as defined.  With
FuelStatesStatement (the run's states, including S5's stopping call), no S1 call the run makes runs out of fuel.
Consequence: on well-formed games the transcription's outputs are never artefacts of the fuel bounds, so the speccheck
DATA comparisons (101 + 25 frozen instances, A, B) compare SPEC with SPEC, not with a truncated loop.

What it does NOT say.  Nothing about `fault` (si.py's exception cases: «cycle in restricted graph», a vertex left without
a value or choice): that is the separate NoFault Statement (Lead 03:43Z).  Nothing about the number of iterations, i.e.
nothing about N5's running time: `cap` is arbitrary and the Statements hold for every cap.  G-N5-TIME stays OPEN.

Hypotheses used (Lead 04:07Z (e): «Name in the Statement header that only «successors < n, owners ≤ 1» is used»).  Of
`SGame.WF` the proofs use only `succ_lt` (every successor is a vertex), `owner_le` (owners in {0, 1}) and `owner_size`
(owner array of length n; needed for the dual game's owners, `1 - owner`).  `prio_size`, `succ_size`, `succ_ne` are not
used.  Of `SGame.StratWF 0 s` only the second part (s[v]! ∈ g.succ[v]! at Even's v) is used, and only through `succ_lt`
(to get s[v]! < n); the size part s.size = n is not used.
-/
import PGLemmas.Spec

namespace PG.Spec

/-- One evaluation (SPEC S1, si.py `Engine.evaluate` on G for Even's strategy `s`) never runs out of fuel. -/
def FuelEvalStatement : Prop :=
  ∀ g : SGame, g.WF → ∀ s : Array ℕ, g.StratWF 0 s → ((Eng.ofGame g).evaluate s).fuelOut = false

/-- Every iteration record of `specIter` from a pair (σ, τ) whose choices are vertices has `fuelOut = false`. -/
def FuelIterStatement : Prop :=
  ∀ g : SGame, g.WF → ∀ sigma tau : Array ℕ,
    (∀ v, v < g.n → g.owner[v]! = 0 → sigma[v]! < g.n) → (∀ v, v < g.n → g.owner[v]! = 1 → tau[v]! < g.n) →
    ∀ cap : ℕ, ∀ r ∈ (specIter g (Eng.ofGame g) (Eng.ofGame g.dual) cap sigma tau).1, r.fuelOut = false

/-- Every iteration record of a run `specRun g start cap` (S3 start, or a start file of edges of the right owner, through
`startPair`) has `fuelOut = false`. -/
def FuelRunStatement : Prop :=
  ∀ g : SGame, g.WF → ∀ start : Option (List (ℕ × ℕ) × List (ℕ × ℕ)),
    (∀ ss ts, start = some (ss, ts) →
      (∀ p ∈ ss, p.1 < g.n ∧ g.owner[p.1]! = 0 ∧ p.2 ∈ g.succ[p.1]!) ∧
      (∀ p ∈ ts, p.1 < g.n ∧ g.owner[p.1]! = 1 ∧ p.2 ∈ g.succ[p.1]!)) →
    ∀ cap : ℕ, ∀ r ∈ (specRun g start cap).steps, r.fuelOut = false

/-- The evaluations of every STATE of a run (both players' S1 calls: Even's strategy on G, Odd's on G^d) never run out
of fuel.  This covers the evaluations of S5's stopping call (`specStep` returns `none`, so no step record carries its
flags) and of the state reached at the cap. -/
def FuelStatesStatement : Prop :=
  ∀ g : SGame, g.WF → ∀ start : Option (List (ℕ × ℕ) × List (ℕ × ℕ)),
    (∀ ss ts, start = some (ss, ts) →
      (∀ p ∈ ss, p.1 < g.n ∧ g.owner[p.1]! = 0 ∧ p.2 ∈ g.succ[p.1]!) ∧
      (∀ p ∈ ts, p.1 < g.n ∧ g.owner[p.1]! = 1 ∧ p.2 ∈ g.succ[p.1]!)) →
    ∀ cap : ℕ, ∀ p ∈ (specRun g start cap).states,
      ((Eng.ofGame g).evaluate p.1).fuelOut = false ∧ ((Eng.ofGame g.dual).evaluate p.2).fuelOut = false

end PG.Spec
