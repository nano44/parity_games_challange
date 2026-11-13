/-
DEFINITIONS AND A STATEMENT: the transport of strategies Γ → Γ3 and RESULTS R117's Lemma PAD (c) (the value
transport), asked for by the Lead 2026-11-12 23:53Z («(a) PAD (c), the value transport Γ ↔ Γ3, definitions
first: lift a Γ-state to a standard Γ3-state, then «val3 (old v) = Γ's value with padded length»»).
ACCEPTED by the Lead (2026-11-13 00:00Z) «with deviations (i)-(iv)», diffed against P-N5-REACH §5 (c) and §3
«Transport».  On (c3), the Lead, verbatim (to be kept in this header): «(c3) is correct and correctly limited. It
claims order preservation only when (Λ, Π) differ. When they agree, the padded lengths decide, and no claim is
made, so the Γ3 order may differ there, exactly as the text says.»  Proofs: `pad_value`, `lift_start`
(PGLemmas/Gamma3Lift.lean).

Text (P-N5-REACH §5 (c), claude/l-new e7dff7d1): «(c) Hence the value in Γ3 of a vertex v of Γ under transported
strategies is (c, P, ℓ + π), where (c, P, ℓ) is the value in Γ and π is the number of pads on the play before c;
for a pad p, value(p) = p ⊕ value(its successor), with the same c and P. Two values compare as in Γ when their
pairs (c, P) differ; only when (c, P) agree do the padded lengths decide.»  [REACH] §3: «Transport. Every pad has
one successor, so the positional strategies of the two players in Γ and in Γ3 correspond one to one (a choice
a → b of Γ is a → p(a, b) in Γ3 when that edge is padded, a → b otherwise), and plays correspond with pads
inserted.»

Definitions:
* `padAt a b`   the pad p(a, b) on the edge a → b of Γ, if that edge is padded (P-N5-REACH §3's list:
                K0 → K3: pA; K1 → K1: s; K1 → K0: q; K2 → K1: r; g → e_g: pe_g; g → β_g: pβ_g; β_g → u = K0:
                pb_g; x → g_(x,k): m_(x,k)); `none` otherwise.
* `lift3 s`     the transport of a successor map s of Γ (one map for both players, as `pair`): at `old a`,
                the pad on a → s a if the edge is padded, else `old (s a)`; at a pad, its only successor.
* `npad s v n`  the number of padded edges among the first n steps s^j v → s^(j+1) v, j < n, of v's play.

`PadValueStatement` (under `G.WF`, for π = G.r104, for every legal successor map s of Γ):
(c1) for every vertex v of Γ: the cycle node of `old v` under `lift3 s` is `old` of v's cycle node in Γ; the
     P-set is the image under `old` of v's P-set; the length is ℓ + npad (the pads on the play before c);
(c2) for every pad p: cycle node and P-set equal those of its successor, the length is one more («value(p) =
     p ⊕ value(its successor), with the same c and P»);
(c3) for vertices u, w of Γ whose pairs (c, P) differ: the Γ3 values of `old u`, `old w` compare (strictly,
     ◁) as the Γ values of u, w do.
`LiftStartStatement`: `lift3 start0 = start3` (the standard state of the genome start is the lift of R104's
stated start; for another mover state s, `std3 s` is the lift of the start with the movers moved, by the same
case check).
DEVIATIONS: (i) Γ3 here is Γ3(G) only (π = G.r104): Γ3*(G*) has no Γ to transport from (box 104 defines Γ3*
directly); (ii) «the number of pads on the play before c» is `npad s v ℓ` (one pad per padded edge, counted on
the ℓ steps before the first visit of c); (iii) `G.WF` is assumed (the injective priority p' of Γ and of Γ3
needs injective indices); (iv) (c3) is stated as an equivalence of the strict orders; «only when (c, P) agree
do the padded lengths decide» is not a separate clause (it is (c1) with Defs.lean's order).
-/
import PGLemmas.Gamma3Statement

namespace PG

namespace Genome

variable (G : Genome)

open Classical in
/-- The pad on the edge a → b of Γ, if that edge is padded ([REACH] §3). -/
noncomputable def padAt : G.Vertex → G.Vertex → Option G.Vertex3
  | .K0, .K3 => some .pA
  | .K1, .K1 => some .pS
  | .K1, .K0 => some .pQ
  | .K2, .K1 => some .pR
  | .gate o, .eface o' => if o = o' then some (.pe o) else none
  | .gate o, .beta o' => if o = o' then some (.pbeta o) else none
  | .beta o, .K0 => some (.pb o)
  | .mover x, .gate o => if x = o.1 then some (.m o) else none
  | _, _ => none

/-- The only successor of a pad (and `old v` itself on Γ's vertices, unused). -/
def padSucc : G.Vertex3 → G.Vertex3
  | .pA => .old .K3
  | .pS => .old .K1
  | .pQ => .old .K0
  | .pR => .old .K1
  | .pe o => .old (.eface o)
  | .pbeta o => .old (.beta o)
  | .pb _ => .old .K0
  | .m o => .old (.gate o)
  | .old v => .old v

/-- The transport of a successor map of Γ to Γ3 ([REACH] §3: «a choice a → b of Γ is a → p(a, b) in Γ3
when that edge is padded, a → b otherwise»; a pad steps to its only successor). -/
noncomputable def lift3 (s : G.Vertex → G.Vertex) : G.Vertex3 → G.Vertex3
  | .old a => (G.padAt a (s a)).getD (.old (s a))
  | p => G.padSucc p

open Classical in
/-- The number of padded edges among the first n steps of the play from v under s. -/
noncomputable def npad (s : G.Vertex → G.Vertex) (v : G.Vertex) (n : ℕ) : ℕ :=
  ((Finset.range n).filter (fun j => (G.padAt (s^[j] v) (s (s^[j] v))).isSome)).card

/-- **Lemma PAD (c)**, the value transport (RESULTS R117; P-N5-REACH §5 (c)). -/
def PadValueStatement : Prop :=
  G.WF → ∀ s : G.Vertex → G.Vertex, (∀ a, s a ∈ G.E a) →
    (∀ v : G.Vertex,
      lam (G.pr3 G.r104) (G.lift3 s) (.old v) = .old (lam G.pr s v) ∧
      pset (G.pr3 G.r104) (G.lift3 s) (.old v) = (pset G.pr s v).image Vertex3.old ∧
      plen (G.pr3 G.r104) (G.lift3 s) (.old v) = plen G.pr s v + G.npad s v (plen G.pr s v)) ∧
    (∀ p : G.Vertex3, Vertex3.isPad G p = true →
      lam (G.pr3 G.r104) (G.lift3 s) p = lam (G.pr3 G.r104) (G.lift3 s) (G.padSucc p) ∧
      pset (G.pr3 G.r104) (G.lift3 s) p = pset (G.pr3 G.r104) (G.lift3 s) (G.padSucc p) ∧
      plen (G.pr3 G.r104) (G.lift3 s) p = plen (G.pr3 G.r104) (G.lift3 s) (G.padSucc p) + 1) ∧
    (∀ u w : G.Vertex, (lam G.pr s u, pset G.pr s u) ≠ (lam G.pr s w, pset G.pr s w) →
      (Val.lt (G.pr3 G.r104) (val (G.pr3 G.r104) (G.lift3 s) (.old u))
          (val (G.pr3 G.r104) (G.lift3 s) (.old w)) ↔
        Val.lt G.pr (val G.pr s u) (val G.pr s w)))

/-- **The lift of Γ's start is Γ3's standard start** (R117: «R104's stated start transported through the
pads»): `lift3 start0 = start3` at every vertex. -/
def LiftStartStatement : Prop :=
  ∀ v : G.Vertex3, G.lift3 G.start0 v = G.start3 v

end Genome

end PG
