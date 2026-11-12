/-
DEFINITIONS ONLY: the IDEAL genome, the game Γ(G), and IDEAL-CYC(G).  No theorem about them is
in this file.  ACCEPTED by the Lead (2026-11-12 15:36Z, 15:50Z) with the deviations (a)-(g) listed
in lean/lemmas/README.md and the required change (h): `WF.one_le_N`.

Fleet texts transcribed (opened; quoted in the docstrings):
* [DEF]  RESULTS R104 (docs/RESULTS.md l. 9864), definitions only, in the wording of the landed
         packet docs/red/P-N5-REALIZE.md §2 (the genome) and §3.1 (the game Γ(G), its indices,
         priorities, edges and start), which is experiments/red/r187/stab.py
         `build(G, 0, kgad=True, esc=True)`.
* [CYC]  RESULTS R118 (a) (docs/RESULTS.md l. 13607) in the wording of the landed packet
         docs/new/P-N5-XICYC.md §2 (IDEAL-CYC(G), the Howard step).
* [SI]   experiments/si/si.py l. 7, l. 38-43: «Priorities are made injective by rank:
         p'(v) = 2*rank(v) + (pr(v) mod 2) with rank by (pr(v), v)».

The structural part (`Genome`, `Vertex`, `idx`, `prio`, `pr`, `E`, `isOdd`, `start0`) is
computable, so that it can be evaluated on a pinned genome and compared with stab.py's output
(lean/lemmas/check/genomecheck.py).
-/
import PGLemmas.Statements6
import Mathlib.Data.Fintype.Sigma
import Mathlib.Data.Fintype.BigOperators
import Mathlib.Data.Finset.Lattice.Fold
import Mathlib.Tactic.DeriveFintype

namespace PG

/-- A GENOME.  P-N5-REALIZE §2: «movers x = 0, …, N − 1, each with a level lev(x) ∈ {0, …, d − 1}
and options k = 0, …, deg(x) − 1; M := Σ_x deg(x); per option (x, k): a W-target wt(x, k), which
is a mover of level lev(x) − 1 if lev(x) ≥ 1 and «none» if lev(x) = 0 (GRADED); a Ξ-target
xt(x, k) ∈ {movers} ∪ {X}; a β-id b(x, k) (a bijection onto 0..M − 1); a gate index gate(x, k), a
bijection of the options onto 0..M − 1; per β-id b: a rank br(b) (a bijection onto 0..M − 1) and a
parity bp(b) ∈ {0, 1}; a start s_0 (an option per mover).»

An option is a pair `⟨x, k⟩ : Σ x : Fin N, Fin (deg x)`.  `none` stands for «none» (W-target) and
for the exit `X` (Ξ-target).  The β-id is not a field: Γ(G) uses it only through the rank and the
parity of an option's β, `brank ⟨x, k⟩ = br(b(x, k))` and `bpar ⟨x, k⟩ = bp(b(x, k))`.  The
conditions «GRADED», «bijection», «∈ {0, 1}» are the predicate `Genome.WF`. -/
structure Genome where
  /-- the number of movers -/
  N : ℕ
  /-- the level of a mover -/
  lev : Fin N → ℕ
  /-- the number of options of a mover -/
  deg : Fin N → ℕ
  /-- the W-target of an option (`none`: «none») -/
  wt : (Σ x : Fin N, Fin (deg x)) → Option (Fin N)
  /-- the Ξ-target of an option (`none`: the exit X) -/
  xt : (Σ x : Fin N, Fin (deg x)) → Option (Fin N)
  /-- the gate index of an option -/
  gate : (Σ x : Fin N, Fin (deg x)) → ℕ
  /-- the rank of the option's β: `br(b(x, k))` -/
  brank : (Σ x : Fin N, Fin (deg x)) → ℕ
  /-- the parity of the option's β: `bp(b(x, k))` -/
  bpar : (Σ x : Fin N, Fin (deg x)) → ℕ
  /-- the start: an option per mover -/
  start : (x : Fin N) → Fin (deg x)

namespace Genome

variable (G : Genome)

/-- The options `(x, k)` of a genome. -/
abbrev Opt : Type := Σ x : Fin G.N, Fin (G.deg x)

/-- `M := Σ_x deg(x)`, the number of options. -/
def M : ℕ := Fintype.card G.Opt

/-- The conditions of P-N5-REALIZE §2 on a genome: GRADED; the gate index and the β-rank are
bijections of the options onto `0..M − 1`; the parities are 0 or 1; and (h) there is a mover.
Every mover has an option by the type of `start` (`Fin (deg x)` is inhabited), so `one_le_N`
gives `M ≥ 1`: the text's implicit assumption, under which §3.1's «Rank facts» hold (with no
option, `top = 4 < Ω(K1) = 5`). -/
structure WF : Prop where
  one_le_N : 1 ≤ G.N
  graded0 : ∀ o : G.Opt, G.lev o.1 = 0 → G.wt o = none
  graded : ∀ o : G.Opt, 0 < G.lev o.1 → ∃ y, G.wt o = some y ∧ G.lev y + 1 = G.lev o.1
  gate_inj : Function.Injective G.gate
  gate_lt : ∀ o, G.gate o < G.M
  brank_inj : Function.Injective G.brank
  brank_lt : ∀ o, G.brank o < G.M
  bpar_le : ∀ o, G.bpar o ≤ 1

/-- The vertices of Γ(G).  P-N5-REALIZE §3.1: «Vertices and indices (n = N + 3M + 6)»: the
movers, per option `g = (x, k)` a gate `g`, a Ξ-face `β_g` and a W-face `e_g`, the two self-loops
`c_X`, `c_W`, and the core `K0 = u, K1, K2, K3`. -/
inductive Vertex (G : Genome) : Type
  | mover (x : Fin G.N)
  | gate (o : G.Opt)
  | beta (o : G.Opt)
  | eface (o : G.Opt)
  | cX
  | cW
  | K0
  | K1
  | K2
  | K3
  deriving DecidableEq, Fintype

/-- The position of an option in the `(x, k)` order: `Σ_{x' < x} deg(x') + k`. -/
def pos (o : G.Opt) : ℕ :=
  (∑ x' ∈ Finset.univ.filter (fun x' : Fin G.N => x' < o.1), G.deg x') + (o.2 : ℕ)

/-- The vertex index.  §3.1: «movers x: index x»; «gates g = (x, k): index N + gate(x, k)»;
«β_g: indices N + M, … (options in (x, k) order)»; «e_g: indices N + 2M, … allocated in
GATE-INDEX order»; «c_X: index N + 3M»; «c_W: index N + 3M + 1»; «the core K = (K0, K1, K2, K3)
…, indices N + 3M + 2, …, N + 3M + 5». -/
def idx : G.Vertex → ℕ
  | .mover x => x
  | .gate o => G.N + G.gate o
  | .beta o => G.N + G.M + G.pos o
  | .eface o => G.N + 2 * G.M + G.gate o
  | .cX => G.N + 3 * G.M
  | .cW => G.N + 3 * G.M + 1
  | .K0 => G.N + 3 * G.M + 2
  | .K1 => G.N + 3 * G.M + 3
  | .K2 => G.N + 3 * G.M + 4
  | .K3 => G.N + 3 * G.M + 5

/-- §3.1: «Ω(β_g) := 6 + 2·br(b(g)) + bp(b(g))». -/
def bprio (o : G.Opt) : ℕ := 6 + 2 * G.brank o + G.bpar o

/-- §3.1: «bmax := the largest Ω(β)». -/
def bmax : ℕ := Finset.univ.sup G.bprio

/-- §3.1: «eb := the least even number > bmax» (stab.py: `eb = bmax + 1 + (bmax + 1) % 2`). -/
def eb : ℕ := G.bmax + 1 + (G.bmax + 1) % 2

/-- §3.1: «i := the position of g in the order by (lev(owner), gate index)». -/
def epos (o : G.Opt) : ℕ :=
  (Finset.univ.filter (fun o' : G.Opt =>
    G.lev o'.1 < G.lev o.1 ∨ (G.lev o'.1 = G.lev o.1 ∧ G.gate o' < G.gate o))).card

/-- §3.1: «Ω(e_g) := eb + 2·i». -/
def eprio (o : G.Opt) : ℕ := G.eb + 2 * G.epos o

/-- The largest priority of a mover (0), a gate (1), a β, an e-vertex or `c_X` (2): «max Ω so
far» when `c_W` gets its priority (stab.py: `max(prio)` before `prio[cW]` and the core are set). -/
def pmax : ℕ := max 2 (max G.bmax (Finset.univ.sup G.eprio))

/-- §3.1: «Ω top := the least even number ≥ 2 + max Ω so far» (stab.py:
`top = max(prio) + 2; top += top % 2`). -/
def top : ℕ := G.pmax + 2 + (G.pmax + 2) % 2

/-- The priority Ω.  §3.1: movers «Ω 0»; gates «Ω 1»; `β_g`, `e_g` as above; `c_X` «Ω 2»; `c_W`
«Ω top»; «K0 Even Ω top + 2 …; K1 Even Ω 5 …; K2 Odd Ω 3 …; K3 Even Ω top + 3». -/
def prio : G.Vertex → ℕ
  | .mover _ => 0
  | .gate _ => 1
  | .beta o => G.bprio o
  | .eface o => G.eprio o
  | .cX => 2
  | .cW => G.top
  | .K0 => G.top + 2
  | .K1 => 5
  | .K2 => 3
  | .K3 => G.top + 3

/-- The rank of a vertex in the order by (priority, index) ([SI]: «rank by (pr(v), v)»). -/
def rk (v : G.Vertex) : ℕ :=
  (Finset.univ.filter (fun u : G.Vertex =>
    G.prio u < G.prio v ∨ (G.prio u = G.prio v ∧ G.idx u < G.idx v))).card

/-- The injective priority ([SI]: «p'(v) = 2*rank(v) + (pr(v) mod 2)»): the relevance order is the
order by (priority, index), the parity is the parity of the priority.  This is the `pr` of
`PGLemmas/Defs.lean` for the game Γ(G). -/
def pr (v : G.Vertex) : ℕ := 2 * G.rk v + G.prio v % 2

/-- The edges of Γ(G).  §3.1: movers «edges to its gates»; gates «edges {e_g, β_g}»; `β_g`
«edges {xt(g), u} if xt(g) is a mover (ESC), {u} if xt(g) = X»; `e_g` «single edge to wt(g), or
to c_W if lev = 0»; `c_X`, `c_W` «self-loop»; «K0 … edges {K1, K3}; K1 … edges {K0, K1}; K2 …
edges {K1, K2}; K3 … edges {K1, K2}»; «u := K0». -/
def E : G.Vertex → Finset G.Vertex
  | .mover x => Finset.univ.image (fun k : Fin (G.deg x) => Vertex.gate ⟨x, k⟩)
  | .gate o => {.eface o, .beta o}
  | .beta o =>
    match G.xt o with
    | some y => {.mover y, .K0}
    | none => {.K0}
  | .eface o =>
    match G.wt o with
    | some y => {.mover y}
    | none => {.cW}
  | .cX => {.cX}
  | .cW => {.cW}
  | .K0 => {.K1, .K3}
  | .K1 => {.K0, .K1}
  | .K2 => {.K1, .K2}
  | .K3 => {.K1, .K2}

/-- Odd's vertices.  §3.1: «Odd vertices: the gates and K2 only.» -/
def isOdd : G.Vertex → Bool
  | .gate _ => true
  | .K2 => true
  | _ => false

/-- Even's vertices (the `V0` of `PGLemmas/Statements.lean`). -/
def V0 : Finset G.Vertex := Finset.univ.filter (fun v => G.isOdd v = false)

/-- The start.  §3.1: «σ_0(x) := (x, s_0(x)); σ_0(β_g) := xt(g) if a mover, u otherwise;
σ_0(K0) := K3, σ_0(K1) := K1, σ_0(K3) := K2; single edges elsewhere.  τ_0(g) := e_g at every gate;
τ_0(K2) := K2.»  One map: `σ_0` on Even's vertices, `τ_0` on Odd's.  (IDEAL-CYC uses it on Even's
vertices only.) -/
def start0 : G.Vertex → G.Vertex
  | .mover x => .gate ⟨x, G.start x⟩
  | .gate o => .eface o
  | .beta o =>
    match G.xt o with
    | some y => .mover y
    | none => .K0
  | .eface o =>
    match G.wt o with
    | some y => .mover y
    | none => .cW
  | .cX => .cX
  | .cW => .cW
  | .K0 => .K3
  | .K1 => .K1
  | .K2 => .K2
  | .K3 => .K2

open Classical in
/-- A run `σ 0, …, σ T` of IDEAL-CYC(G), with `τ t` Odd's counterstrategy `σ̄_t`.
P-N5-XICYC §2 = RESULTS R118 (a): «The game is Γ(G) with every Even vertex that is not a mover
frozen at its start successor.  Odd is unrestricted (gates and K2).  A state σ_t is the start off
the movers plus a choice at every mover; Ω_t := Ω_(σ_t), the [VJ] value against Odd's optimal
counterstrategy.  σ̄_t is the optimal counterstrategy chosen by a fixed deterministic rule (any
rule …).  A HOWARD step σ_t → σ_(t+1): every mover x goes to a successor of ⊴-largest Ω_t value,
and keeps σ_t(x) if σ_t(x) is such a successor.  The run stops at the first σ_T where no mover has
a strictly better successor.»

`Ω_t` is `val G.pr (nxt G.V0 σ τ t)`.  `τ t` is ANY optimal counterstrategy against `σ t`
(`OptCounter`); a fixed deterministic rule is one way to choose it.  The first state is any mover
state; `FromStart` says that it is the genome's start. -/
structure IdealCycRun (σ τ : ℕ → G.Vertex → G.Vertex) (T : ℕ) : Prop where
  /-- every Even vertex that is not a mover is frozen at its start successor -/
  frozen : ∀ t, t ≤ T → ∀ v ∈ G.V0, (∀ x, v ≠ Vertex.mover x) → σ t v = G.start0 v
  /-- a state carries a choice at every mover: one of its gates -/
  legal : ∀ t, t ≤ T → ∀ x, σ t (Vertex.mover x) ∈ G.E (Vertex.mover x)
  /-- `τ t` is an optimal counterstrategy against `σ t` -/
  opt : ∀ t, t ≤ T → OptCounter G.pr G.E G.V0 (σ t) (τ t)
  /-- Howard's step at every mover -/
  howard : ∀ t, t < T → ∀ x,
    HowardAt G.pr G.E (nxt G.V0 σ τ t) (nxt G.V0 σ τ (t + 1)) (Vertex.mover x)
  /-- the run has not stopped before `T`: some mover has a strictly better successor -/
  moves : ∀ t, t < T → ∃ x, ∃ y ∈ G.E (Vertex.mover x),
    Val.lt G.pr (val G.pr (nxt G.V0 σ τ t) (σ t (Vertex.mover x))) (val G.pr (nxt G.V0 σ τ t) y)

/-- The run starts at the genome's start (§3.1: «σ_0(x) := (x, s_0(x))»). -/
def FromStart (σ : ℕ → G.Vertex → G.Vertex) : Prop :=
  ∀ x, σ 0 (Vertex.mover x) = G.start0 (Vertex.mover x)

open Classical in
/-- `σ T` is the last state of the run: «no mover has a strictly better successor». -/
def Stopped (σ τ : ℕ → G.Vertex → G.Vertex) (T : ℕ) : Prop :=
  ∀ x, ∀ y ∈ G.E (Vertex.mover x),
    ¬ Val.lt G.pr (val G.pr (nxt G.V0 σ τ T) (σ T (Vertex.mover x))) (val G.pr (nxt G.V0 σ τ T) y)

end Genome

end PG
