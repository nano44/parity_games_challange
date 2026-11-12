/-
Box 208 §3 (L1) and §4 (C1)-(C2) (claude/l-new 8db300fe docs/new/N5-LEVEL-box208.md), without the
genome: the counting that turns «Φ takes at most P values» and «a plateau has at most L steps» into
«the first state with LAG = ∅ comes after at most P·(L + 1) steps».  PROPOSED to the Lead.

Lane text.  §3: «LAG_t := {v : class_t(v) ≠ class_b(v)}.  […] m_t := min{class_t(v) : v ∈ LAG_t};
FRONT_t := {v ∈ LAG_t : class_t(v) = m_t}; Φ_t := (m_t, −|FRONT_t|) […].  A step t → t + 1 with
t < b and LAG_t ≠ ∅ is a STALL if class_(t+1)(v) = class_t(v) for every v ∈ FRONT_t.»
§4: «(C1) q ≤ 2M(N + 2M) =: P (L5) […] (C2) The steps inside an interval [u_i, v_i] are stalls and
the steps u_(i+1) − 1 → u_(i+1) and v_q → b′ are not (L1).  So the number of non-stall steps on
[a, b′] is exactly q ≤ P, and b′ − a = q + Σ_i (v_i − u_i).»

Here `c t v` is the class of the vertex `v` at state `t`, in any linear order `α`; `b` is the
reference state.  The hypotheses are (K1) «no class falls», a set `M` that contains every lowest
lagging class ((L3), (L5): at most 2M values), a bound `F` on the size of the front ((L2), (L5):
N + 2M), and a bound `L` on the number of consecutive stalls (Lemma PLATEAU).  The conclusion:
every state `t` with LAG_t ≠ ∅ has `t − a < |M|·F·(L + 1)`; so b′ − a ≤ |M|·F·(L + 1).
(With |M| ≤ 2M, F = N + 2M: P·(L + 1), the first term of Theorem ALL-TCYC for L = N + 2M + 5.)
NOT stated here: (C4) (the quiet steps after b′), and every genome fact.
-/
import Mathlib.Data.Fintype.Card
import Mathlib.Data.Finset.Prod
import Mathlib.Order.Basic

namespace PG

open Classical

noncomputable section

variable {V : Type*} {α : Type*} [LinearOrder α]

/-- `v ∈ FRONT_t` (reference state `b`): `v` lags, and its class is the lowest lagging class. -/
def FrontAt (c : ℕ → V → α) (b t : ℕ) (v : V) : Prop :=
  c t v ≠ c b v ∧ ∀ u, c t u ≠ c b u → c t v ≤ c t u

/-- The step `t → t + 1` is a STALL: something lags at `t`, and every vertex of the front keeps
its class. -/
def StallAt (c : ℕ → V → α) (b t : ℕ) : Prop :=
  (∃ v, c t v ≠ c b v) ∧ ∀ v, FrontAt c b t v → c (t + 1) v = c t v

/-- **LEVEL, the counting** (box 208 §3 (L1) + §4 (C1), (C2), abstract). -/
def LevelCountStatement (V : Type*) [Fintype V] (α : Type*) [LinearOrder α] : Prop :=
  ∀ (c : ℕ → V → α) (a b : ℕ) (M : Finset α) (F L : ℕ),
    -- (K1) no class falls
    (∀ t, a ≤ t → t < b → ∀ v, c t v ≤ c (t + 1) v) →
    -- (L3), (L5): the lowest lagging class lies in `M`
    (∀ t, a ≤ t → t ≤ b → ∀ v, FrontAt c b t v → c t v ∈ M) →
    -- (L2), (L5): the front has at most `F` vertices
    (∀ t, a ≤ t → t ≤ b → (Finset.univ.filter (FrontAt c b t)).card ≤ F) →
    -- PLATEAU: at most `L` consecutive stalls
    (∀ u v, a ≤ u → u ≤ v → v ≤ b → (∀ t, u ≤ t → t < v → StallAt c b t) → v - u ≤ L) →
    -- every state at which something lags is among the first `|M|·F·(L + 1)` states
    ∀ t, a ≤ t → t ≤ b → (∃ v, c t v ≠ c b v) → t - a < M.card * F * (L + 1)

end

end PG
