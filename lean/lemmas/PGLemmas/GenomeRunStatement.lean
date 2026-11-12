/-
Runs of IDEAL-CYC(G) exist: the hypotheses of the statements about `Genome.IdealCycRun` are
satisfiable for every genome, and the Howard run from the genome's start reaches a state at which
no mover has a strictly better successor.  STATEMENT ONLY; PROPOSED to the Lead for the diff.

Fleet text, RESULTS R118 (a) = P-N5-XICYC §2: «A HOWARD step σ_t → σ_(t+1): every mover x goes to
a successor of ⊴-largest Ω_t value, and keeps σ_t(x) if σ_t(x) is such a successor.  The run stops
at the first σ_T where no mover has a strictly better successor.  T_CYC(G) := T.»

The statement says that such a run exists: a run `σ 0, …, σ T` of IDEAL-CYC(G)
(`IdealCycRun`: frozen, legal, σ̄ optimal, Howard's step, not stopped before T) from the genome's
start (`FromStart`) whose last state has stopped (`Stopped`).  The fleet texts take this for
granted (the run is what the engines compute); it is stated here because the Lean theorems about
runs would be empty without it.  It does not say that the run is unique: ties among ⊴-best gates
and the choice of the optimal counterstrategy are free in `IdealCycRun`.
-/
import PGLemmas.Genome

namespace PG

noncomputable section

namespace Genome

variable (G : Genome)

/-- **Runs exist and stop.**  There is a run of IDEAL-CYC(G) from the genome's start whose last
state has stopped. -/
def RunExistsStatement : Prop :=
  G.WF → ∃ (σ τ : ℕ → G.Vertex → G.Vertex) (T : ℕ),
    G.IdealCycRun σ τ T ∧ G.FromStart σ ∧ G.Stopped σ τ T

end Genome

end

end PG
