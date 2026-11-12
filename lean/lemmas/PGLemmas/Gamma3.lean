/-
DEFINITIONS ONLY: the S3-padded game Γ3(G) of RESULTS R117 and its free-priority form Γ3*(G*) of
L-SI box 104 §4 (used by box 105 §1), with their standard states.  No theorem is in this file.
ACCEPTED by the Lead (2026-11-12 22:22Z) «with deviations (a)-(e) as you named them», diffed against
RESULTS R117 l. 13362.  Lead 22:22Z, to be recorded here: «per-pad priorities fixed by
experiments/new/box189/gamma3.py (R117's text: ≤ 2), DATA-checked» (lean/lemmas/check/gamma3check.py:
25 genomes, 5,834 vertices, 7 counters 0, the control fires).  (P-N5-REACH §3, quoted below as [REACH],
states the same per-pad values.)  Γ3*: «the line-by-line check of the transcription against build_free
is accepted, and its source commit is 3417f6c1.»

Fleet texts transcribed (opened; quoted in the docstrings):
* [R117]  RESULTS R117 (docs/RESULTS.md l. 13362, trunk): «the game Γ3(G) obtained from Γ(G) by 4M + 4
          single-successor Even pads of priority ≤ 2 (pA on K0 → K3, s on K1's loop, q on K1 → K0, r on
          K2 → K1, pe_g and pβ_g on both faces of every gate g, pb_g on every β_g → u, and m_(x,k) on every
          mover edge x → (x, k) with priority 2 for the genome start and 0 otherwise, appended after
          Γ(G)'s vertices; n = N + 7M + 10)».
* [REACH] the landed packet docs/new/P-N5-REACH.md §3 (claude/l-new e7dff7d1), the definition R117
          names: «A PAD on an edge a → b is a new Even vertex p with the single edge p → b, the edge
          a → b being replaced by a → p.  Γ3(G) is Γ(G) ([DEF], with its vertex indices, priorities and
          owners unchanged) with these pads, appended after Γ's vertices in the order pA, s, q, r, pe
          (gate-index order), pβ (gate-index order), pb (option order), m (gate-index order): core: pA
          (Ω 0) on K0 → K3; s (Ω 0) on the self-loop of K1 (K1 → s → K1); q (Ω 1) on K1 → K0; r (Ω 0)
          on K2 → K1; gates: pe_g (Ω 1) on g → e_g, and pβ_g (Ω 0) on g → β_g; escapes: pb_g (Ω 1) on
          β_g → u (for every gate g, also when xt(g) = X); movers: m_(x,k) on x → g_(x,k), with Ω 2 if
          k = start(x) and Ω 0 otherwise.  top, the priority of c_W, is computed as in [DEF] and is
          unchanged (every pad has Ω ≤ 2).»  STANDARD STATE: «the transport of R104's start with the
          genome start replaced by s: σ(x) = m_(x,s(x)); σ(β_g) = xt(g) if xt(g) is a mover, pb_g
          otherwise; σ(K0) = pA, σ(K1) = s, σ(K3) = K2; τ(g) = pe_g at every gate, τ(K2) = K2; forced
          choices elsewhere.»
* [FREE]  L-SI box 104 §4 (docs/si/box104-map.md l. 209-216, claude/l-si 3417f6c1): «G* = (G, π): G has
          the data of an R104 genome without its β-ranks and parities …, and π is an injective map from
          the 2M CARRIERS β_q, e_q into the integers ≥ 6, of either parity.  Γ3*(G*) is R117's Γ3 (same
          vertices, indices, owners, edges and pads) with Ω(β_q) := π(β_q), Ω(e_q) := π(e_q), top := the
          least even number ≥ max π + 2, Ω(c_W) := top, Ω(K0) := top + 2, Ω(K3) := top + 3; movers 0,
          gates 1, c_X 2, K2 3, K1 5 and the pad priorities are R117's.»  Box 105 §1 takes the standard
          state from there: «σ_s(x) = m_(x, s(x)) at every mover, every β on its Ξ-target (on pb when the
          target is X), K0 → pA, K1 → s, K3 → K2; τ0 = pe at every gate and K2 → K2.»
* Builders (the machine comparison, lean/lemmas/check/gamma3check.py): experiments/new/box189/gamma3.py
  `build(G, {"K","pe","pb","m"})` for Γ3(G); L-SI's experiments/si/box104/free104.py `build_free` for
  Γ3*(G*).

DEVIATIONS from the texts (named):
(a) ONE definition for both games: the carrier priorities are a parameter `π : G.Carrier`; Γ3(G) is
    `π = G.r104` (Ω(β) = `bprio`, Ω(e) = `eprio` of Genome.lean) and Γ3*(G*) is a free `π`.  A free genome
    is a `Genome` whose fields `brank`, `bpar` are not read by Γ3*; the conditions on a free π (injective
    on the 2M carriers, ≥ 6) are the separate predicate `Carrier.WF`.
(b) top: [FREE] «the least even number ≥ max π + 2»; [REACH] «computed as in [DEF]» (Genome.lean `top`:
    the least even number ≥ max(2, Ω so far) + 2).  Here `top3 π` := the least even number ≥ max(2, max π)
    + 2, which is [DEF]'s formula; it equals [FREE]'s when some carrier exists (π ≥ 6 > 2), and for
    `π = G.r104` it is Genome.lean's `top` (the same expression).
(c) Names: the pads s, q, r of the core are `pS`, `pQ`, `pR` (`pr` is the injective priority); pβ_g is
    `pbeta`, m_(x,k) is `m`.  Γ's vertices enter as `old v`.
(d) The standard state is ONE map `std3 s` on all vertices (σ_s on Even's, τ0 on Odd's), as `start0` in
    Genome.lean; «forced choices elsewhere» are written out (pads, e_g, c_X, c_W).  `start3` := `std3
    G.start` is «R104's stated start transported through the pads» (R117, Lemma S3-START's right side).
(e) Not defined here: SPEC's S3 (the start N5 computes), N5, N5′-xi, HOW3 / T3 (R125), and the transport
    of strategies Γ ↔ Γ3 beyond the standard states.
-/
import PGLemmas.Genome

namespace PG

namespace Genome

variable (G : Genome)

/-- The priorities of the 2M CARRIERS β_q, e_q ([FREE]: «π … from the 2M CARRIERS β_q, e_q»). -/
structure Carrier (G : Genome) where
  /-- Ω(β_q) -/
  pb : G.Opt → ℕ
  /-- Ω(e_q) -/
  pe : G.Opt → ℕ

/-- R104's carriers ([DEF]): Ω(β_g) = 6 + 2·br + bp, Ω(e_g) = eb + 2·i (Genome.lean). -/
def r104 : G.Carrier := ⟨G.bprio, G.eprio⟩

/-- [FREE]: «π is an injective map from the 2M CARRIERS β_q, e_q into the integers ≥ 6, of either
parity». -/
structure Carrier.WF (π : G.Carrier) : Prop where
  pb_ge : ∀ o, 6 ≤ π.pb o
  pe_ge : ∀ o, 6 ≤ π.pe o
  pb_inj : Function.Injective π.pb
  pe_inj : Function.Injective π.pe
  pb_ne_pe : ∀ o o', π.pb o ≠ π.pe o'

/-- The vertices of Γ3(G) ([REACH] §3): Γ's vertices and the 4M + 4 pads. -/
inductive Vertex3 (G : Genome) : Type
  | old (v : G.Vertex)
  | pA
  | pS
  | pQ
  | pR
  | pe (o : G.Opt)
  | pbeta (o : G.Opt)
  | pb (o : G.Opt)
  | m (o : G.Opt)
  deriving DecidableEq, Fintype

/-- n(Γ) = N + 3M + 6, the first index after Γ's vertices. -/
def n0 : ℕ := G.N + 3 * G.M + 6

/-- The vertex index.  [REACH] §3: Γ's indices unchanged; the pads «appended after Γ's vertices in the
order pA, s, q, r, pe (gate-index order), pβ (gate-index order), pb (option order), m (gate-index
order)». -/
def idx3 : G.Vertex3 → ℕ
  | .old v => G.idx v
  | .pA => G.n0
  | .pS => G.n0 + 1
  | .pQ => G.n0 + 2
  | .pR => G.n0 + 3
  | .pe o => G.n0 + 4 + G.gate o
  | .pbeta o => G.n0 + 4 + G.M + G.gate o
  | .pb o => G.n0 + 4 + 2 * G.M + G.pos o
  | .m o => G.n0 + 4 + 3 * G.M + G.gate o

/-- «max Ω so far» when c_W gets its priority: max(2, max π) (deviation (b)). -/
def pmax3 (π : G.Carrier) : ℕ := max 2 (max (Finset.univ.sup π.pb) (Finset.univ.sup π.pe))

/-- top: the least even number ≥ pmax3 + 2 (deviation (b)). -/
def top3 (π : G.Carrier) : ℕ := G.pmax3 π + 2 + (G.pmax3 π + 2) % 2

/-- The priority Ω.  [REACH] §3 / [DEF] §3.1 and [FREE]: movers 0, gates 1, Ω(β_q) = π(β_q),
Ω(e_q) = π(e_q), c_X 2, c_W top, K0 top + 2, K1 5, K2 3, K3 top + 3; pads: «pA (Ω 0) … s (Ω 0) … q
(Ω 1) … r (Ω 0) … pe_g (Ω 1) … pβ_g (Ω 0) … pb_g (Ω 1) … m_(x,k) … with Ω 2 if k = start(x) and Ω 0
otherwise». -/
def prio3 (π : G.Carrier) : G.Vertex3 → ℕ
  | .old (.mover _) => 0
  | .old (.gate _) => 1
  | .old (.beta o) => π.pb o
  | .old (.eface o) => π.pe o
  | .old .cX => 2
  | .old .cW => G.top3 π
  | .old .K0 => G.top3 π + 2
  | .old .K1 => 5
  | .old .K2 => 3
  | .old .K3 => G.top3 π + 3
  | .pA => 0
  | .pS => 0
  | .pQ => 1
  | .pR => 0
  | .pe _ => 1
  | .pbeta _ => 0
  | .pb _ => 1
  | .m o => if o.2 = G.start o.1 then 2 else 0

/-- The rank of a vertex in the order by (priority, index) (as `Genome.rk`). -/
def rk3 (π : G.Carrier) (v : G.Vertex3) : ℕ :=
  (Finset.univ.filter (fun u : G.Vertex3 =>
    G.prio3 π u < G.prio3 π v ∨ (G.prio3 π u = G.prio3 π v ∧ G.idx3 u < G.idx3 v))).card

/-- The injective priority (as `Genome.pr`: «p'(v) = 2*rank(v) + (pr(v) mod 2)»). -/
def pr3 (π : G.Carrier) (v : G.Vertex3) : ℕ := 2 * G.rk3 π v + G.prio3 π v % 2

/-- Odd's vertices: the gates and K2 ([REACH] §3: owners unchanged; every pad is Even). -/
def isOdd3 : G.Vertex3 → Bool
  | .old v => G.isOdd v
  | _ => false

/-- Even's vertices. -/
def V0_3 : Finset G.Vertex3 := Finset.univ.filter (fun v => G.isOdd3 v = false)

/-- The edges of Γ3(G): Γ's edges with the padded ones replaced, a → b by a → p, and p → b
([REACH] §3).  Padded: K0 → K3 (pA), K1 → K1 (s), K1 → K0 (q), K2 → K1 (r), g → e_g (pe_g), g → β_g
(pβ_g), β_g → u (pb_g, for every gate), x → (x, k) (m_(x,k)).  Unpadded: K0 → K1, K2 → K2, K3 → K1,
K3 → K2, β_g → xt(g), e_g → wt(g) or c_W, c_X → c_X, c_W → c_W. -/
def E3 : G.Vertex3 → Finset G.Vertex3
  | .old (.mover x) => Finset.univ.image (fun k : Fin (G.deg x) => Vertex3.m ⟨x, k⟩)
  | .old (.gate o) => {.pe o, .pbeta o}
  | .old (.beta o) =>
    match G.xt o with
    | some y => {.old (.mover y), .pb o}
    | none => {.pb o}
  | .old (.eface o) =>
    match G.wt o with
    | some y => {.old (.mover y)}
    | none => {.old .cW}
  | .old .cX => {.old .cX}
  | .old .cW => {.old .cW}
  | .old .K0 => {.old .K1, .pA}
  | .old .K1 => {.pQ, .pS}
  | .old .K2 => {.pR, .old .K2}
  | .old .K3 => {.old .K1, .old .K2}
  | .pA => {.old .K3}
  | .pS => {.old .K1}
  | .pQ => {.old .K0}
  | .pR => {.old .K1}
  | .pe o => {.old (.eface o)}
  | .pbeta o => {.old (.beta o)}
  | .pb _ => {.old .K0}
  | .m o => {.old (.gate o)}

/-- The STANDARD STATE of a mover state `s` ([REACH] §3, box 105 §1), as one map: σ_s on Even's
vertices, τ0 on Odd's.  «σ(x) = m_(x,s(x)); σ(β_g) = xt(g) if xt(g) is a mover, pb_g otherwise;
σ(K0) = pA, σ(K1) = s, σ(K3) = K2; τ(g) = pe_g at every gate, τ(K2) = K2; forced choices
elsewhere.» -/
def std3 (s : (x : Fin G.N) → Fin (G.deg x)) : G.Vertex3 → G.Vertex3
  | .old (.mover x) => .m ⟨x, s x⟩
  | .old (.gate o) => .pe o
  | .old (.beta o) =>
    match G.xt o with
    | some y => .old (.mover y)
    | none => .pb o
  | .old (.eface o) =>
    match G.wt o with
    | some y => .old (.mover y)
    | none => .old .cW
  | .old .cX => .old .cX
  | .old .cW => .old .cW
  | .old .K0 => .pA
  | .old .K1 => .pS
  | .old .K2 => .old .K2
  | .old .K3 => .old .K2
  | .pA => .old .K3
  | .pS => .old .K1
  | .pQ => .old .K0
  | .pR => .old .K1
  | .pe o => .old (.eface o)
  | .pbeta o => .old (.beta o)
  | .pb _ => .old .K0
  | .m o => .old (.gate o)

/-- R104's stated start transported through the pads: the standard state of the genome start. -/
def start3 : G.Vertex3 → G.Vertex3 := G.std3 G.start

end Genome

end PG
