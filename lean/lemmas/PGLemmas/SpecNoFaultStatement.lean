/-
NO FAULT in the Lean transcription of SPEC S1-S5 (PGLemmas/Spec.lean): si.py's exception cases never occur on a
well-formed game.  STATEMENTS; the Lead's diff 09:58Z: ACCEPTED as drafted, with (a) `StratWF` for Iter (below), (b) the
`fault` analogue of `specStep_flag` (Lead R2) is REQUIRED when the proof is written, (c) the VJ00 source and the si.py lines
below.  PROOF DEFERRED (Lead 09:58Z, owner «put everything into trying solving it today»): NO THEOREM here; the proof
(~1,500-3,000 lines) lands later.  The ~1,400-line graph toolkit it needs (DFS completeness, even/odd phase invariants,
`longest` acyclicity, BFS completeness, `restrict` / `assign` semantics) is built and compiles in L-FORMAL's scratch.

What `fault` records (Spec.lean, deviation (D2)): (F1) `longest` meets a vertex that is busy (si.py l. 159
`RuntimeError("cycle in restricted graph")`): a cycle of the restricted graph that avoids the cycle node v; (F2) a vertex of
R without a length (si.py: KeyError; only the BFS of S1 (iv), odd Ω(v), can miss one: a vertex of R that no longer reaches v
after the restriction step (iii)); (F3) an Odd vertex of R without a choice (si.py carries a None on): in longest-path mode
a vertex of R \ {v} with no successor left in the restricted graph; (F4) an Odd cycle node whose choice DFS finds no cycle
(impossible: the choice DFS is the cycle test's DFS run again); (F5) a vertex left without a valuation at the end of the
outer loop (si.py's `improving` would fail on it); (F6) in S4a / S4b, a chooser's vertex without a choice.
Paper source of the claim: VJ00 §6, Prop. 6.1 (BRICS RS-00-48 / CAV 2000; opened by the fleet, see SPEC Q3,
docs/new/N5-ssi-global.md l. 111-120, «there is no cycle in G(r) containing s») for (F1): si.py raises at l. 159
`RuntimeError("cycle in restricted graph")`, KeyErrors at l. 196-200, a None choice at l. 180/195, the same restriction argument for (F2), (F3); (F5) is the standard
«every alive subgraph has a cycle whose most relevant vertex was a cycle node when processed» argument (to be written out
in the proof file).

What it does NOT say: that the valuations or the choices are the right ones (optimal counterstrategy, SPEC S1's
correctness); nothing about N5's running time.  G-N5-TIME stays OPEN.

Hypotheses: `SGame.WF` (here `succ_ne` IS needed: an Odd vertex without successors has no play) and choices that are
vertices; which other parts are used will be named in the header when the proof is done.
-/
import PGLemmas.Spec

namespace PG.Spec

/-- One evaluation (SPEC S1 on G for Even's strategy `s`) never sets `fault`. -/
def NoFaultEvalStatement : Prop :=
  ∀ g : SGame, g.WF → ∀ s : Array ℕ, g.StratWF 0 s → ((Eng.ofGame g).evaluate s).fault = false

/-- Every iteration record of `specIter` from a pair (σ, τ) of strategies has `fault = false`. -/
def NoFaultIterStatement : Prop :=
  ∀ g : SGame, g.WF → ∀ sigma tau : Array ℕ, g.StratWF 0 sigma → g.StratWF 1 tau →
    ∀ cap : ℕ, ∀ r ∈ (specIter g (Eng.ofGame g) (Eng.ofGame g.dual) cap sigma tau).1, r.fault = false

/-- Every iteration record of `specRun g start cap` has `fault = false`. -/
def NoFaultRunStatement : Prop :=
  ∀ g : SGame, g.WF → ∀ start : Option (List (ℕ × ℕ) × List (ℕ × ℕ)),
    (∀ ss ts, start = some (ss, ts) →
      (∀ p ∈ ss, p.1 < g.n ∧ g.owner[p.1]! = 0 ∧ p.2 ∈ g.succ[p.1]!) ∧
      (∀ p ∈ ts, p.1 < g.n ∧ g.owner[p.1]! = 1 ∧ p.2 ∈ g.succ[p.1]!)) →
    ∀ cap : ℕ, ∀ r ∈ (specRun g start cap).steps, r.fault = false

/-- Both S1 evaluations at every state of such a run never set `fault` (covers S5's stopping call). -/
def NoFaultStatesStatement : Prop :=
  ∀ g : SGame, g.WF → ∀ start : Option (List (ℕ × ℕ) × List (ℕ × ℕ)),
    (∀ ss ts, start = some (ss, ts) →
      (∀ p ∈ ss, p.1 < g.n ∧ g.owner[p.1]! = 0 ∧ p.2 ∈ g.succ[p.1]!) ∧
      (∀ p ∈ ts, p.1 < g.n ∧ g.owner[p.1]! = 1 ∧ p.2 ∈ g.succ[p.1]!)) →
    ∀ cap : ℕ, ∀ p ∈ (specRun g start cap).states,
      ((Eng.ofGame g).evaluate p.1).fault = false ∧ ((Eng.ofGame g.dual).evaluate p.2).fault = false

end PG.Spec
