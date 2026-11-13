/-
PROPOSED DEFINITIONS, not yet diffed by the Lead.
N5's step (PGLemmas/Spec.lean) specialised to Γ3(G) / Γ3*(G*) (PGLemmas/Gamma3.lean): DEFINITIONS ONLY
(L-FORMAL successor 4, 2026-11-13; Lead 23:53Z item (b) «on a general game first, then specialised to Γ3»).  No theorem in this file; nothing here proves N5.

`sgame3 π` is Γ3 written as SPEC's input (V = {0..n-1} through `idx3`, owner 0 = Even, Ω = `prio3 π`, successor lists =
`E3` through `idx3`), and `n5Gamma3 π cap` is SPEC S1-S5 on it from Γ3's standard start `start3` (R117: «R104's stated
start transported through the pads») given as SPEC's start pair.  Deviations (beyond Spec.lean's (D1)-(D9)):
(G1) the vertex enumeration `vert3List` is the order of check/gamma3check.py (movers, gates, β, e, c_X, c_W, K0-K3, then the
     pads); the arrays are filled through `idx3`, so the enumeration order does not matter when `idx3` is a bijection onto
     0..n − 1 (`gamma3_card`, under WF); without WF a later vertex overwrites an earlier one at a shared index.
(G2) Γ3's start is given at EVERY vertex (σ at Even's, τ at Odd's), so SPEC S3's best-reward start is not used.
-/
import PGLemmas.Gamma3
import PGLemmas.Spec

namespace PG

namespace Genome

variable (G : Genome)

/-- The options in (x, k) order. -/
def optList : List G.Opt :=
  (List.finRange G.N).flatMap (fun x => (List.finRange (G.deg x)).map (fun k => (⟨x, k⟩ : G.Opt)))

/-- Γ's vertices: movers, gates, β-faces, e-faces, c_X, c_W, K0, K1, K2, K3. -/
def vertList : List G.Vertex :=
  (List.finRange G.N).map Vertex.mover ++ G.optList.map Vertex.gate ++ G.optList.map Vertex.beta ++
    G.optList.map Vertex.eface ++ [Vertex.cX, Vertex.cW, Vertex.K0, Vertex.K1, Vertex.K2, Vertex.K3]

/-- Γ3's vertices: Γ's, then the pads pA, s, q, r, pe, pβ, pb, m. -/
def vert3List : List G.Vertex3 :=
  G.vertList.map Vertex3.old ++ [Vertex3.pA, Vertex3.pS, Vertex3.pQ, Vertex3.pR] ++ G.optList.map Vertex3.pe ++
    G.optList.map Vertex3.pbeta ++ G.optList.map Vertex3.pb ++ G.optList.map Vertex3.m

/-- n = N + 7M + 10 = n0 + 4 + 4M (`gamma3_card`). -/
def nV3 : ℕ := G.n0 + 4 + 4 * G.M

/-- Γ3 as SPEC's input game. -/
def sgame3 (π : G.Carrier) : Spec.SGame :=
  let vs := G.vert3List
  ⟨G.nV3,
   vs.foldl (fun a v => a.set! (G.idx3 v) (G.prio3 π v)) (Array.replicate G.nV3 0),
   vs.foldl (fun a v => a.set! (G.idx3 v) (if G.isOdd3 v then 1 else 0)) (Array.replicate G.nV3 0),
   vs.foldl (fun a v => a.set! (G.idx3 v) ((vs.filter (fun u => decide (u ∈ G.E3 v))).map G.idx3))
     (Array.replicate G.nV3 [])⟩

/-- Γ3's standard start `start3` as SPEC's start pair: (σ0 on Even's vertices, τ0 on Odd's). -/
def start3Pair : List (ℕ × ℕ) × List (ℕ × ℕ) :=
  ((G.vert3List.filter (fun v => !G.isOdd3 v)).map (fun v => (G.idx3 v, G.idx3 (G.start3 v))),
   (G.vert3List.filter (fun v => G.isOdd3 v)).map (fun v => (G.idx3 v, G.idx3 (G.start3 v))))

/-- N5 (SPEC S1-S5) on Γ3(G) with carriers π, from Γ3's standard start, at most `cap` iterations. -/
def n5Gamma3 (π : G.Carrier) (cap : ℕ) : Spec.RunOut :=
  Spec.specRun (G.sgame3 π) (some G.start3Pair) cap

end Genome

end PG
