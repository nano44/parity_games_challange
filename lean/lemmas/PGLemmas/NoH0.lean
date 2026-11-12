/-
`brsegG_noH0' : BrSegGNoH0Statement V`.  The proof step where H0 is not needed: in
`brsegG_noH0` (`PGLemmas/Corollaries.lean`) the hypothesis is used once, to give the field
`Window.moves` (the step changes the state); `lam_gap_sharp` asks nothing else of the step.
-/
import PGLemmas.Corollaries
import PGLemmas.Statements7

namespace PG

noncomputable section

variable {V : Type*} [Fintype V]

/-- BR-SEG-G clause (a) without H0, as a statement object. -/
theorem brsegG_noH0' : BrSegGNoH0Statement V :=
  fun pr hpr E V0 σ τ a r hhow hF1 hlam hbar hchg =>
    brsegG_noH0 pr hpr E V0 σ τ a r hhow hF1 hlam hbar hchg

end

end PG
