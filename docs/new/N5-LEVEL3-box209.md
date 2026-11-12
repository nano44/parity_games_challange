# Box 209 (D18): the Γ3 form of box 208 — CANDIDATE: on HOW3(G), for every genome, T3 ≤ P3·(n_E3 + 1) + n_E3 with P3 = 2M(N + 4M), n_E3 = N + 6M + 9; with landed R124 / R125, N5′-xi from S3 on Γ3(G) would make at most that many + 3 iterations (L-NEW successor 72)
Written 2026-11-12 (date -u in the commit). Brief, research item 2: «relate (Q2) to DEEP3 / LAM-GAP on Γ3»; announced to the Lead with box
208's SHA (message 12:50Z).
**SCOPE LINE: HOW3(G) on Γ3(G) (RESULTS R117, R125), which by landed R125 is N5′-xi's run from S3 up to its first fallback, for the genomes
of R104. Not N5, not another start, not another game, not M4; G-N5-TIME stays OPEN.**
**LABEL: every statement of this box is a CANDIDATE** (lane, unrefereed). It is box 208 (docs/new/N5-LEVEL-box208.md, l-new 8db300fe, itself
a CANDIDATE under attack) carried to Γ3: if LEVEL or PLATEAU falls there, it falls here. D1 (owner, verbatim): «A claimed polynomial
algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet
below.» This box claims no algorithm for TARGET.md's problem: it bounds the iterations of the fleet's candidate N5′-xi on one restricted
family of games.
Tools: experiments/new/box209/ (plat209.py, own3hist209.py, quotes209.py, summ209.py, run209.sh, check209.sh; the LEVEL counters are box
208's level208.py with --g3 or --hist); outputs box209/out/ with SHA1SUMS; section «BOX 209 LEVEL3» of experiments/new/check.sh.

## 0. Answer
- Box 208's two lemmas use only: five class facts, the frozen structure of the game, [OPT], F1 and BR-SEG-G. Each has a LANDED Γ3 form in
  R125 (F1, DOM, CN2-3, LOC-GATE3, NO-TIE3, B-ONLY3, LOC-K2-3) or is game-independent (R118 (i) BR-SEG-G). The pads of Γ3 are
  single-successor vertices that are never cycle nodes and never in a set Π, so in the argument they behave like the gates and β-vertices
  of box 208. Both lemmas go through with the pads added to the front.
- **Lemma LEVEL3 (CANDIDATE; §3).** On HOW3(G), for any genome and any reference state b: the potential Φ_t = (m_t, −|FRONT_t|) (lowest
  lagging class, size of its front) never falls and rises at every step that is not a stall; a stall forces a whole cycle of Ξ-edges of
  σ_b inside the front; Φ takes at most P3 := 2M·(N + 4M) values.
- **Lemma PLATEAU3 (CANDIDATE; §4).** A maximal interval of states of constant Φ has at most n_E3 := N + 6M + 9 steps (the number of
  Even vertices of Γ3(G)); so has the interval between the last class change and T3.
- **Theorem T3-ALL (CANDIDATE; §5).** For every genome G: T3 ≤ P3·(n_E3 + 1) + n_E3. Degree 3 in N + M.
- **Corollary N5XI-G3 (CANDIDATE; §5; with landed R125 REACH3-ALL and R124 END-T3).** For every genome G, N5′-xi from S3 on Γ3(G) makes
  exactly T3 + 3 ≤ P3·(n_E3 + 1) + n_E3 + 3 iterations. Landed R125 (CHAIN3) has a polynomial bound only under HYPOTHESIS [E-LEV] and for
  U(G) ≤ B fixed; L-SI's chain (box 99-102) has one under CONJECTURE DEEP3.
- **Corollary FLIPS3 (CANDIDATE; §5).** On HOW3(G), for every genome: the number of steps at which σ̄ changes, the number of steps at which
  some class changes, and D^tot_E(v) − 1 for every vertex v are at most T3, hence polynomial. This would give the conclusions of
  CONJECTURES DEEP3, DEEP3-G and DEEP3-all of L-SI box 100-102 (polynomially many deep flips), not their exact forms.
- DATA (§6): every must-0 counter is 0 on the 25 frozen k = 1 genomes, the 53 corpus genomes of box 202 and the three genomes of landed
  R118 (m), on random genomes and on mutants, on N5′-xi's own run (engine n5v) and, for the frozen genomes, on L-RED 65's independent
  HOW3 engine with its own tie rule. Controls fire. Exact rows in §6.
- What it is not: M4, M3, a step-4 pass, a statement about N5 (landed R125's scope: N5's pre-fallback run on Ξ-cyclic genomes is not a
  Howard run), about another start, or about any game that is not a Γ3(G). The cost of one iteration at bit cost is a separate item.

## 1. Setting and premises (every «…» on a line marked [Q] is quoted by script from trunk docs/RESULTS.md: quotes209.py, out/quotes209.out)
Setting: HOW3(G) for any genome G; states 0, …, T := T3; Ω_t(v) = (Λ_t(v), Π_t(v), k_t(v)) the value of v under (σ_t, σ̄_t); E_t(v) := the
e-vertices of Π_t(v); class_t(v) := (Λ_t(v), E_t(v)); s_t(v) := the successor of v on its play at t. The order on values [VJ], the order
on classes, LAG, m_t, FRONT_t, Φ_t, stall and plateau are those of box 208 §1, §3, §4, read on Γ3(G); they are restated where used.
- [Q] R117 (the game): «4M + 4 single-successor Even pads of priority ≤ 2 (pA on K0 → K3, s on K1's loop, q on K1 → K0, r on K2 → K1,
  pe_g and pβ_g on both faces of every gate g, pb_g on every β_g → u, and m_(x,k) on every mover edge x → (x, k) with priority 2 for the
  genome start and 0 otherwise, appended after Γ(G)'s vertices; n = N + 7M + 10)».
- [Q] R104 ([DEF], the game Γ(G) that is padded): «Even movers of priority 0; Odd gates of priority 1 with a W-face e and a Ξ-face β»;
  «β of priority 6 + 2·rank + parity with edges to the Ξ-target and to u, or to u alone»; «e of even priority above every β with one edge
  to the W-target or to the top even self-loop c_W»; «a closed core u = K0 (Even, top + 2) → {K1, K3}, K1 (Even, 5) → {K0, K1}, K2 (Odd,
  3) → {K1, K2}, K3 (Even, top + 3) → {K1, K2}».
- [Q] R125 (the run): «HOW3(G), the Howard run on Γ3(G) (every non-mover Even vertex frozen at the standard state's choice of P-N5-REACH
  §3, Odd unrestricted at the gates and K2, every mover moving to a ⊴-best successor and keeping a best current one; T3 := the first
  state at which no mover has a strictly better successor)».
- The standard state, as landed R124 names it: [Q] «the core K-config κ0 = (σ(K0), σ(K1), σ(K3)) = (pA, s, K2)»; with R104's start off
  the movers ([Q] «β → its Ξ-target (u when the target is X), K0 → K3, K1 → K1, K3 → K2») carried through the pads: a β-vertex whose
  Ξ-target is a mover goes to that mover, one whose target is X goes to pb_g → K0; an e-vertex goes to its W-target mover or to c_W.
- READINGS of the construction used below (the Γ3 forms of box 208's (D1), (D3), as in the landed packets P-N5-QN §1 and P-N5-CHAIN §5):
  (D1′) the only in-edge of e_g is from pe_g, and the only in-edge of pe_g is from g; (D3′) the core vertices are K0, K1, K2, K3 and the
  pads pA, s, q, r; the only edges into the core from outside are pb_g → K0; inside it the frozen choices are K0 → pA → K3 → K2 and
  K1 → s → K1, and Odd's choice at K2 is r → K1 (LOC-K2-3 below); (D4′) c_W's and c_X's only out-edge is the own self-loop.
- [Q] R125 REACH3-ALL: «N5′-xi from S3 on Γ3(G) visits only standard states and its mover parts form a run of HOW3(G) until its first
  fallback, at iteration T3 + 1».
- [Q] R125 facts: «(Facts F1, F3, F4′, F5, F6, DOM, STRICT on HOW3(G)) F1 from RESULTS R15 (a)»; R15 (a): «Lemma A: for any non-empty
  unambiguous set I of improvements of σ (VJ00 §4.4), Ωσ ⊴ Ω_{Switch_I(σ)}.» As used: (F1) Ω_t(v) ⊴ Ω_(t+1)(v) for every vertex and step.
- [Q] R118 (c) DOM (its HOW3 form is the fact named in the line above): «For every mover x, step t and successor y of x: Ω_(t+1)(x) ⊵
  ext(x, Ω_t(y)).»
- [Q] R125 CN2-3: «for every positional pair and every vertex v other than c_X the cycle node of v's play has priority ≥ 3, so no mover,
  gate or pad is ever a cycle node or in a set Π».
- [Q] R125 LOC-GATE3: «at every state and gate g, if the faces pe_g, pβ_g have different values then Odd's optimal counterstrategy σ̄_t
  picks the strictly ⊴-smaller one».
- [Q] R125 NO-TIE3: «Ω_t(pe_g) ≠ Ω_t(pβ_g) at every state and gate».
- [Q] R125 LOC-K2-3: «σ̄_t(K2) = r and Ω_t(r) ◁ Ω_t(K2) at every state».
- [Q] R125 B-ONLY3: «at every state and every vertex v other than c_W, the e-vertices whose successor is c_W and their pads pe_g, Λ_t(v)
  is less relevant than every e-vertex».
- [Q] R125's premise [VJ]: «VJ00 §4.2 / Friedmann arXiv 1106.0778 §3 for the value (Λ, Π, k) and its order ⊴»; [OPT]: «[OPT] for HOW3's
  σ̄_t = RESULTS R118's σ̄ as used in R118 (b)», which landed R123 spells out as «[OPT] (σ̄_t is optimal at every vertex at once against
  σ_t)» and landed R118 as «an optimal counterstrategy being pointwise optimal (at every vertex its play value is ⊴ the value under every
  Odd strategy».
- [VJ] as used (box 208 §1): Λ(v) is the most relevant vertex of the cycle of v's play; Π(v) is the set of vertices on the path from v
  to Λ(v), before Λ(v), that are more relevant than Λ(v); (VJ-1) if Λ ≠ Λ′, Ω ◁ Ω′ iff reward(Λ) < reward(Λ′); (VJ-2) if Λ = Λ′ and
  Π ≠ Π′, with z the most relevant vertex of Π Δ Π′: Ω ◁ Ω′ iff (z ∈ Π′ and z even) or (z ∈ Π and z odd). ext(x, (Λ, Π, k)) = (Λ, Π ∪
  ({x} if x is more relevant than Λ), k + 1).
- [Q] R121 E-DOM (on Γ(G)): «Every vertex more relevant than some e-vertex is an e-vertex, c_W, K0 or K3, by [DEF]». On Γ3(G) the same
  holds: the added vertices are pads of priority ≤ 2 (R117's line above), below every e-vertex. Call this (E-DOM3).
- [Q] R118 (i) BR-SEG-G [any parity game, Howard from any σ_0, under H0]: «H0: every step t → t+1 switches some Even x with Λ_t(x) ≠ x
  and Λ_(t+1)(x) ≠ x.»; «(a) every maximal run of p-steps has at most n_E steps;»; the labels: «labelled C if some vertex's cycle node Λ
  changes, else R if Odd's optimal counterstrategy σ̄ (any fixed deterministic choice) changes somewhere, else p». Its Howard, in the
  landed packet P-N5-XICYC §5: every Even vertex goes to a ⊴-best successor and keeps its current one when that is one.
- [Q] R124 END-T3: «if REACH3-CYC holds for G, N5′-xi from S3 on Γ3(G) makes exactly T3 + 3 iterations»; its condition is discharged by
  [Q] R125: «RESULTS R118 (k)'s Theorem REACH3-CYC».
- ORDER ON CLASSES: (Λ, E) < (Λ′, E′) iff reward(Λ) < reward(Λ′), or Λ = Λ′ and the most relevant element of E Δ E′ lies in E′. A strict
  total order on the classes that occur (box 208 §1; the cycle nodes have pairwise different priorities).
- NOT used: E-MON3, QUIET3, T-QUIET3, CHAIN-DECOMP3, [E-LEV], UP-B3, ascents, depth, the Ξ-feedback number, any lemma of box 99-102 or of
  R232-R234, any statement of box 208 as a premise (its proofs are the template; every step is redone below on Γ3).

## 2. Five class facts on Γ3
«Outside the core» means: not one of K0, K1, K2, K3, pA, s, q, r.
- **(K0′) CORE.** The class of each of the eight core vertices is the same at every state. A vertex outside the core has Λ_t = K1 iff
  its play enters the core; then the play enters at K0 and K0, K3 ∈ Π_t; otherwise neither is in Π_t. c_W is in no set Π.
  Proof: inside the core the plays are fixed: K0 → pA → K3 → K2 → r → K1 → s → K1 ((D3′), LOC-K2-3), with cycle K1 → s → K1 and cycle
  node K1 (priority 5; s has priority ≤ 2); q → K0 likewise. So the eight values are constant. A play has cycle node K1 only if it reaches
  K1, and from outside the core is entered only at K0 (D3′); K0 (top + 2) and K3 (top + 3) are more relevant than K1. c_W is the cycle
  node of every play that reaches it (D4′), so it is on no path before a cycle node. ∎
- **(K2′) COARSE.** Let Ω, Ω′ be values of two vertices outside the core, at the same state or at two states, with classes c, c′. If
  Ω ⊴ Ω′ then c ≤ c′.
  Proof: If Λ ≠ Λ′, (VJ-1). Let Λ = Λ′. If E = E′ then c = c′. Otherwise let z_E be the most relevant element of E Δ E′ and z the most
  relevant vertex of Π Δ Π′. E Δ E′ ⊆ Π Δ Π′, so z is at least as relevant as z_E; by (E-DOM3) z is an e-vertex, c_W, K0 or K3. Not c_W
  (K0′). Not K0 or K3: both are in Π and in Π′ (if Λ = K1) or in neither (K0′). So z is an e-vertex, z = z_E, of even priority, and by
  (VJ-2) Ω ◁ Ω′ iff z ∈ Π′ iff z_E ∈ E′ iff c < c′. ∎
- **(K1′) MONOTONE.** class_t(v) ≤ class_(t+1)(v) for every vertex v and step t.
  Proof: core vertices: (K0′). Otherwise (F1) and (K2′), for the values of v at t and t + 1. ∎
- **(K3′) ALONG THE PLAY.** At every state t: (a) Λ_t(v) = Λ_t(s_t(v)); (b) no e-vertex lies on the cycle of a play; (c) class_t(v) =
  class_t(s_t(v)) for every vertex v that is not an e-vertex; (d) for an e-vertex e with successor a mover w: class_t(e) = (Λ_t(w),
  {e} ∪ E_t(w)) > class_t(w), and e ∉ E_t(w); (e) the classes of c_W, c_X, of every e-vertex with successor c_W and its pad pe_g, and of
  every pad pb_g are the same at every state.
  Proof: (a) v and s_t(v) have the same cycle. (b) An e-vertex on a cycle would make the cycle node at least as relevant as an
  e-vertex. By B-ONLY3 this is possible only for the vertices it excepts, whose plays end in c_W's self-loop, which contains no e-vertex.
  (c) The path of v is v followed by the path of s_t(v). If v is the cycle node, both Π are empty (the cycle node is the most relevant
  vertex of the cycle, and the path of s_t(v) to it runs inside the cycle). Otherwise Π_t(v) is Π_t(s_t(v)), plus v if v is more
  relevant than Λ; v is not an e-vertex, so E is the same. (d) w is a mover, so Λ_t(w) is less relevant than e (B-ONLY3) and e ∈ Π_t(e):
  E_t(e) = {e} ∪ E_t(w). e ∉ E_t(w): else e would lie twice on the play of e before its cycle node, hence on its cycle, against (b). The
  two classes differ exactly in e, which is in the larger. (e) c_W and c_X are self-loops (D4′); an e-vertex with successor c_W, and its
  pad, play into c_W's loop; pb_g → K0 is (K0′). ∎
- **(K4′) GATES.** class_t(g) = class_t(σ̄_t(g)) = min(class_t(pe_g), class_t(pβ_g)) for every gate g and state t.
  Proof: the first equality is (K3′ c). The two faces have different values (NO-TIE3), and σ̄_t(g) is the ⊴-smaller (LOC-GATE3); by
  (K2′) its class is ≤ the other's. ∎
- **(K5′) DOM AT CLASS LEVEL.** For every mover x, every successor y of x (an m-pad) and every step t: class_(t+1)(x) ≥ class_t(y).
  Proof: DOM: Ω_(t+1)(x) ⊵ ext(x, Ω_t(y)). x is in no set Π (CN2-3), so ext(x, Ω_t(y)) has the Λ and the Π of Ω_t(y), the value of a
  vertex outside the core; (K2′)'s proof uses only Λ and Π, so it applies to this triple. ∎

## 3. Lemma LEVEL3 (CANDIDATE)
Fix a reference state b ≤ T3. For t ≤ b: LAG_t := {v : class_t(v) ≠ class_b(v)}; if LAG_t ≠ ∅: m_t := the lowest class_t(v), v ∈ LAG_t;
FRONT_t := {v ∈ LAG_t : class_t(v) = m_t}; Φ_t := (m_t, −|FRONT_t|), ordered lexicographically. A step t → t + 1 (t < b, LAG_t ≠ ∅) is a
STALL if no vertex of FRONT_t changes class at it.
**Statement.** For every genome G, every reference state b and every t < b with LAG_t ≠ ∅:
- (L1′) LAG_(t+1) ⊆ LAG_t; if LAG_(t+1) ≠ ∅ then Φ_(t+1) ≥ Φ_t, with equality iff the step is a stall; at a stall FRONT_(t+1) = FRONT_t.
- (L2′) FRONT_t consists of movers, m-pads, gates, pads pβ_g and β-vertices whose frozen successor is a mover.
- (L3′) Either (α) some mover z ∈ FRONT_t has σ_t(z) ∉ LAG_t, and then m_t = class_b(σ_t(z)), the class at b of an m-pad; or (β) the
  cycle of some play at t lies inside FRONT_t, and then m_t = (c, ∅) for a β-vertex c.
- (L4′) If the step is a stall, there are movers x_1, …, x_r (r ≥ 1) with x_(i+1) = the Ξ-target of the option σ_b(x_i) (indices mod r)
  such that x_i, the m-pad σ_b(x_i), its gate g_i, pβ_(g_i) and β_(g_i) all lie in FRONT_t, and σ̄_t(g_i) = pβ_(g_i).
- (L5′) Over 0 ≤ t ≤ b, Φ takes at most P3 = 2M·(N + 4M) values, each on one interval of states.
**Proof.**
(L1′) A vertex outside LAG_t has class_t = class_b, and by (K1′) class_(t+1) is between them: it is outside LAG_(t+1). A vertex of
LAG_(t+1) has class_(t+1) ≥ class_t ≥ m_t (K1′), so m_(t+1) ≥ m_t. If m_(t+1) = m_t, a vertex v ∈ FRONT_(t+1) has m_t ≤ class_t(v) ≤
class_(t+1)(v) = m_t: v ∈ FRONT_t with unchanged class. So FRONT_(t+1) ⊆ FRONT_t, and it is the set of vertices of FRONT_t that keep their
class (such a vertex still lags: class_b ≠ m_t). Hence Φ_(t+1) ≥ Φ_t, with equality iff FRONT_(t+1) = FRONT_t iff no vertex of FRONT_t
changes class. If LAG_(t+1) ≠ ∅ but every vertex of FRONT_t changes class, then m_(t+1) > m_t or the front shrank: Φ rose.
(L2′) Core vertices, c_W, c_X, pads pb_g, e-vertices with successor c_W and their pads never lag (K0′, K3′ e). An e-vertex e with mover
successor w: class_t(e) is determined by class_t(w) (K3′ d), so if e lags, w lags, and class_t(w) < class_t(e): e ∉ FRONT_t. Its pad
pe_g has the class of e at every state (K3′ c): the same. A β-vertex whose frozen successor is pb_g has pb_g's class (K3′ c): constant.
What is left: movers, m-pads, gates, pads pβ_g, and β-vertices with a mover successor.
(L3′) Take v ∈ FRONT_t and follow its play v = v_0, v_1 = s_t(v_0), …. Claim: if v_i ∈ FRONT_t and v_(i+1) ∈ LAG_t, then v_(i+1) ∈
FRONT_t. Indeed v_i is no e-vertex (L2′), so class_t(v_(i+1)) = class_t(v_i) = m_t (K3′ c). So either the whole play stays in FRONT_t,
and then its cycle lies in FRONT_t: case (β); or there is a first i with z := v_i ∈ FRONT_t and w := v_(i+1) ∉ LAG_t. Then z is a mover:
- z an m-pad, a pad pβ_g or a β-vertex: w is its only (frozen) successor, at t and at b, so class_b(z) = class_b(w) = class_t(w) =
  class_t(z) (K3′ c at b and at t): z does not lag. Contradiction.
- z a gate: class_t(z) = class_t(w) (K4′) = class_b(w) ≥ class_b(z) (K4′ at b: the minimum over both faces) ≥ class_t(z) (K1′): z does
  not lag. Contradiction.
So z is a mover, w = σ_t(z) an m-pad outside LAG_t, and m_t = class_t(z) = class_t(w) = class_b(w): case (α). In case (β) the cycle
consists of vertices of FRONT_t; its cycle node c has priority ≥ 3 (CN2-3), so it is none of the movers, pads and gates: it is a
β-vertex. No e-vertex is on the play from c to c (the cycle), and no other vertex of Π can be an e-vertex either, as Π_t(c) = ∅; every
vertex u of the cycle has the class of c (K3′ c along the cycle), and class_t(c) = (c, ∅). So m_t = (c, ∅).
(L4′) Let the step be a stall. Define a map s on FRONT_t: s(x) := σ_b(x) for a mover x; s(v) := s_t(v) for every other vertex of
FRONT_t (for an m-pad, a pad pβ_g or a β-vertex its only successor; for a gate its face σ̄_t(g)). Claim: s maps FRONT_t into FRONT_t.
- A mover x ∈ FRONT_t, y := σ_b(x). class_b(y) = class_b(x) (K3′ c at b) > m_t (x lags and (K1′)). class_t(y) ≤ class_(t+1)(x) (K5′) =
  class_t(x) = m_t (stall). So class_t(y) ≠ class_b(y): y lags, and class_t(y) ≥ m_t by the choice of m_t. Hence class_t(y) = m_t:
  y ∈ FRONT_t.
- An m-pad, a pad pβ_g or a β-vertex v ∈ FRONT_t with successor w (a gate, β_g, or a mover by (L2′)): class_t(w) = class_t(v) = m_t and
  class_b(w) = class_b(v) ≠ m_t (K3′ c at t and b): w ∈ FRONT_t.
- A gate g ∈ FRONT_t, a := σ̄_t(g). class_t(a) = class_t(g) = m_t (K4′). class_b(a) ≥ class_b(g) (K4′ at b) > m_t. So a ∈ FRONT_t. By
  (L2′) a is not pe_g: a = pβ_g.
FRONT_t is finite, so s has a cycle inside it. On the cycle the kinds follow each other as mover → m-pad → gate → pβ-pad → β-vertex →
mover (the Ξ-target of that option): it contains a mover x_1, and from x_1 it runs through σ_b(x_1), its gate g_1, pβ_(g_1), β_(g_1), then
x_2 = the Ξ-target of the option σ_b(x_1), and so on, back to x_1.
(L5′) By (L1′) Φ is non-decreasing in t, so each value is taken on one interval. m_t is the class at b of one of the M m-pads (α) or
(c, ∅) for one of the M β-vertices (β): at most 2M values. |FRONT_t| ≤ N + 4M (L2′: N movers, M m-pads, M gates, M pads pβ_g, at most
M β-vertices). ∎

## 4. Lemma PLATEAU3 (CANDIDATE)
A PLATEAU (reference b) is a maximal interval [u, v] of states, u < v, with LAG ≠ ∅ and constant Φ. By (L1′) its steps are stalls.
**Statement.** For every genome G and every reference state b: (i) every plateau [u, v] has v − u ≤ n_E3 = N + 6M + 9; (ii) if b = T3
and b′ is the first state with LAG_(b′) = ∅, then T3 − b′ ≤ n_E3.
**Proof of (i).** Let Φ = (m, −|J|) on [u, v], J := FRONT_u. By (L1′), FRONT_s = J and class_s(x) = m for x ∈ J, at every state s ∈
[u, v]. Put Y := {x : class_u(x) ≤ m}.
(P1) For every s ∈ [u, v]: {x : class_s(x) ≤ m} = Y, and class_s(x) = class_u(x) for x ∈ Y.
  A vertex of Y either lags at u, and then it is in J (its class is ≥ m as it lags, ≤ m as it is in Y) with class m throughout; or it
  does not lag at u, and then its class is class_b at u and, by (K1′), at every state from u to b. A vertex outside Y has class > m at
  u, hence at s (K1′).
(P2) Y is closed under plays: for x ∈ Y and s ∈ [u, v], s_s(x) ∈ Y. (class_s(s_s(x)) ≤ class_s(x) ≤ m by (K3′ c, d); (P1).)
(P3) For every mover x ∈ Y, every successor y of x and every s ∈ [u, v]: class_s(y) ≤ class_s(x); so every m-pad of a mover of Y, and
  its gate, are in Y.
  For s < v: class_s(y) ≤ class_(s+1)(x) (K5′) = class_s(x) (P1). So y ∈ Y at state u (u < v), its class is constant on [u, v] (P1),
  and the inequality holds at s = v too. The gate is s_s(y) (P2).
(P4) For every gate g ∈ Y, σ̄_s(g) is the same face for all s ∈ [u, v], and it lies in Y.
  The chosen face has the class of g (K4′), so it is in Y (P1). Three cases. (1) The other face is outside Y: at every s its class is
  > m ≥ class_s(g), so it is never the chosen face (K4′). (2) Both faces are in Y with different classes: the classes are constant on
  [u, v] (P1), and the lower one is chosen at every s (K4′). (3) Both faces are in Y with the same class at every s. e_g's
  successor is not c_W: else Λ_s(pe_g) = c_W, while Λ_s(pβ_g) ≠ c_W, because pβ_g is none of the vertices B-ONLY3 excepts. So it is a
  mover w, and E_s(pe_g) = E_s(e_g) = {e_g} ∪ E_s(w) (K3′ c, d). So e_g ∈ E_s(pβ_g): the play of pβ_g passes e_g. e_g ≠ pβ_g, so the play
  enters e_g by its only in-edge, from pe_g, and pe_g by its only in-edge, from g (D1′): the play passes g and leaves it to pe_g. So
  σ̄_s(g) = pe_g at every s.
  The other Odd vertex with a choice, K2, goes to r at every state (LOC-K2-3).
(P5) The game H. Vertices: Y. A mover of Y keeps all its successors (in Y by (P3)). Every other vertex x of Y keeps the single
  successor s_u(x) (in Y by (P2)); by (P4), the frozen choices of HOW3 and LOC-K2-3, s_s(x) = s_u(x) for every s ∈ [u, v]. H is a parity
  game (priorities and owners inherited; every vertex has a successor) in which only the movers of Y have a choice. For s ∈ [u, v] and
  x ∈ Y, the play of x under (σ_s, σ̄_s) stays in Y (P2) and uses H's edges, so Ω_s(x) is the value of x in H under σ_s restricted to
  Y; Odd has no choice in H, so this is H's value against Odd's optimal (only) counterstrategy. The step of HOW3 at a mover of Y
  compares the values Ω_s of its successors, which are its successors in H with H's values, by the same rule (a ⊴-best successor,
  keeping a best current one). So σ_u, σ_(u+1), …, σ_v, restricted to Y, are consecutive states of a Howard run of H in the sense of
  BR-SEG-G (every Even vertex of H goes to a ⊴-best successor and keeps a best current one; the Even vertices that are not movers have one
  successor).
(P6) Every step s → s + 1 with u ≤ s ≤ v changes σ at some mover of Y.
  Suppose not, for some s. Claim: for every s′ with s ≤ s′ ≤ b: σ_(s′) = σ_s on the movers of Y, and Ω_(s′) = Ω_s on Y. Induction on s′;
  s′ = s is trivial. Let the claim hold for s′ < b. (a) No mover x of Y switches at s′ → s′ + 1: its successors are in Y (P3) and have
  the values of state s (induction), its current successor is σ_s(x), and at step s → s + 1 it kept σ_s(x), i.e. no successor had a
  strictly larger value; HOW3 keeps a best current one, so x keeps it again. (b) Ω_(s′+1) = Ω_s on Y: let Odd answer σ_(s′+1) by σ̄_s,
  the counterstrategy of state s. From x ∈ Y the play under (σ_s, σ̄_s) stays in Y (P2, s ∈ [u, v]), where σ_(s′+1) = σ_s by (a); so the
  play under (σ_(s′+1), σ̄_s) is the same play, of value Ω_s(x). By [OPT] at s′ + 1, Ω_(s′+1)(x) ⊴ Ω_s(x). By (F1), Ω_(s′+1)(x) ⊵
  Ω_(s′)(x) = Ω_s(x). This proves the claim. At s′ = b it gives class_b(x) = class_s(x) = m for x ∈ J ⊆ Y: J does not lag at s.
  Contradiction with J = FRONT_s.
(P7) The steps u → u + 1, …, v − 1 → v of H's Howard run each switch a mover of Y (P6), change no cycle node on Y (P1: the class
  contains Λ) and no choice of Odd (Odd has none in H): they are v − u consecutive p-steps of H's run. H0 holds: the vertices that switch
  are movers, and a mover is never a cycle node (CN2-3, «for every positional pair»: a positional pair of H is one of Γ3(G)). By
  BR-SEG-G (a), v − u ≤ n_E(H) ≤ the number of Even vertices of Γ3(G) = N movers + M β + M e + (4M + 4) pads + c_X, c_W, K0, K1, K3 =
  N + 6M + 9. ∎
**Proof of (ii).** On [b′, T3] no vertex changes class ((L1′): LAG stays empty). Put Y := all vertices. (P4) holds on [b′, T3] by its
cases (2) and (3) (no face is outside Y; both cases use only that the classes of the two faces are constant on the interval, and case
(3) B-ONLY3 and (D1′)); so does (P5), with H := Γ3(G) with every non-mover vertex restricted to its successor at b′. Every step b′ ≤ s < T3 switches a mover, by the definition of T3 (a state before T3 has a mover
with a strictly better successor). As in (P7), the steps b′ → b′ + 1, …, T3 − 1 → T3 are consecutive p-steps of a Howard run of H under
H0: T3 − b′ ≤ n_E3. ∎

## 5. Theorem T3-ALL and its corollaries (CANDIDATES)
**Theorem T3-ALL.** For every genome G: T3 ≤ P3·(n_E3 + 1) + n_E3, with P3 = 2M(N + 4M) and n_E3 = N + 6M + 9.
Proof. Reference b := T3; b′ := the first state with LAG = ∅. The states 0, …, b′ − 1 have LAG ≠ ∅ and carry the values of Φ, at most P3
of them (L5′), each on one interval (L1′). Such an interval with j + 1 states has j stall steps, j ≤ n_E3 (PLATEAU3 (i); j = 0 is not a
plateau). Between two consecutive intervals, and from the last one to b′, there is one non-stall step. So b′ ≤ (number of intervals) ·
(n_E3 + 1) ≤ P3·(n_E3 + 1) (if b′ = 0 there is no interval). T3 − b′ ≤ n_E3 (PLATEAU3 (ii)). ∎
**Corollary N5XI-G3.** For every genome G, N5′-xi from S3 on Γ3(G) makes exactly T3 + 3 ≤ P3·(n_E3 + 1) + n_E3 + 3 iterations.
Proof. REACH3-ALL: the mover parts of the run are a run of HOW3(G) until the first fallback at iteration T3 + 1; §2-§4 use no property
of the tie rule beyond «a ⊴-best successor, keeping a best current one», which is HOW3's definition, so T3-ALL bounds this run's T3.
END-T3 with REACH3-ALL: exactly T3 + 3 iterations. ∎
**Corollary FLIPS3.** On HOW3(G), for every genome: R (the steps at which σ̄ changes) ≤ T3; the number of steps at which some vertex
changes class ≤ T3; D^tot_E(v) ≤ T3 + 1 for every vertex v; the number of pairs (step, gate) at which σ̄ changes at the gate is ≤ M·T3.
Proof. Each is a count of steps of the run, or of at most M events per step. ∎
- In numbers: if N ≤ M, then P3 ≤ 10M² and n_E3 + 1 ≤ 7M + 10, so T3 ≤ about 70M³ + 100M².
- The bound is far from the DATA (§6: the longest run has 199 steps, where the bound is above 10^10). Nothing here says the true order; L-SI's U-FREE conjecture (T3 ≤ N + M + 4 on its class) and SCC-LIN are exact statements that T3-ALL does not give.

## 6. DATA
Engines. «n5v»: N5′-xi itself, from S3 on Γ3(G), stepped by box190/n5v.py up to its first fallback (level208.prep(G, True)); states
0, …, T3. «L-RED how3»: L-RED 65's own HOW3 engine (claude/l-red 707c0e82, experiments/red/r232/how3_232.py with r221q/own.py: its own
values, its own reply of Odd, its own tie rule «keep the current successor if best, else the larger vertex index»; read by git archive
into a temporary directory, not copied; sha1 in out/own3_engine.sha1) through own3hist209.py. Both use the builder box189/gamma3.py (the
builder of R117-R125) for the graph: the second engine is independent for values and runs, not for the graph. The counter code is this
lane's in both rows. An engine that shares nothing is L-COMP's to write (level208.py --hist and plat209.py --hist take any history).
Counters (definitions in the tools' headers).
- level208.py, unit: states t < b with a lagging vertex unless stated, reference b = T3, scope: every vertex of Γ3(G): monofail (K1′),
  k3fail (K3′), k4fail (K4′), k5fail (K5′), einF (L2′), l3fail (L3′), phifail (L1′), stallnocyc (L4′), boundfail (unit genomes: more than
  P3 values of Φ). Its other seven counters (nofvs, rstall, winstall, wbeta, wl3fail, wmid, wbound) are box 208's feedback-set statements
  (WIN, R-HEIGHT) read on Γ3: reported in the same sum, DATA only, not claimed in this box.
- plat209.py: p1 (P1), pclos (P2), p2 (P3), p3 (P4: unit (Odd vertex of Y, step inside a plateau)), p4 (P6: unit steps), p5 (P7: unit
  plateaus), t1, t2 (PLATEAU3 (ii): unit (Odd vertex, step of the tail) and genomes), t3 (T3-ALL: unit genomes).
- struct209.py (no run; unit (genome, clause)): the readings (D1′), (D3′), (D4′), (E-DOM3), the pads and the two vertex counts of §1.
| set (file in out/) | engine | rows | sum of the 16 must-0 counters | descriptive |
| --- | --- | --- | --- | --- |
| level3_records.out | n5v | 25 genomes, k in {1} | 0 | max T3 114, max levels 15, max Phi values 114, stalls 31 (loud 0), plateaus 14 (longest 9), intervals 556 (longest loud prefix 91) |
| level3_corpus.out | n5v | 53 genomes, k in {1, 2, 3, 4, 7, 8, 10, 11, 12, 99} | 0 | max T3 199, max levels 16, max Phi values 199, stalls 48 (loud 23), plateaus 15 (longest 13), intervals 615 (longest loud prefix 53) |
| level3_dead.out | n5v | 3 genomes, k in {2, 3, 4} | 0 | max T3 21, max levels 9, max Phi values 16, stalls 16 (loud 0), plateaus 5 (longest 8), intervals 17 (longest loud prefix 2) |
| own3_level_records.out | L-RED how3 | 25 genomes, k in {1} | 0 | max T3 114, max levels 15, max Phi values 114, stalls 31 (loud 0), plateaus 14 (longest 9), intervals 556 (longest loud prefix 91); T3 differs from the n5v run on 0 of 25 genomes |
| own3_level_corpus.out | L-RED how3 | 53 genomes, k in {1, 2, 3, 4, 7, 8, 10, 11, 12, 99} | 0 | max T3 199, max levels 16, max Phi values 199, stalls 48 (loud 23), plateaus 15 (longest 13), intervals 615 (longest loud prefix 53); T3 differs from the n5v run on 0 of 53 genomes |
| own3_level_dead.out | L-RED how3 | 3 genomes, k in {2, 3, 4} | 0 | max T3 21, max levels 9, max Phi values 16, stalls 16 (loud 0), plateaus 5 (longest 8), intervals 17 (longest loud prefix 2); T3 differs from the n5v run on 0 of 3 genomes |
| level3_rand_deep_s2102.out | n5v | 300 | 0 | max T 11, max levels 8, max phivals 10, max platmax 3, max wmax 1; stalls 80, stallloud 0, plat 64, windows 427 |
| level3_rand_dense_s2102.out | n5v | 300 | 0 | max T 9, max levels 6, max phivals 8, max platmax 2, max wmax 2; stalls 70, stallloud 0, plat 61, windows 538 |
| level3_rand_esc_s2102.out | n5v | 300 | 0 | max T 5, max levels 2, max phivals 4, max platmax 2, max wmax 2; stalls 25, stallloud 0, plat 21, windows 504 |
| level3_rand_k1_s2101.out | n5v | 1000 | 0 | max T 7, max levels 3, max phivals 5, max platmax 3, max wmax 4; stalls 96, stallloud 0, plat 78, windows 2104 |
| level3_rand_lvl0_s2102.out | n5v | 300 | 0 | max T 9, max levels 7, max phivals 7, max platmax 3, max wmax 2; stalls 64, stallloud 0, plat 55, windows 324 |
| level3_rand_noesc_s2102.out | n5v | 300 | 0 | max T 8, max levels 6, max phivals 7, max platmax 3, max wmax 1; stalls 36, stallloud 0, plat 30, windows 492 |
| level3_rand_rand_s2102.out | n5v | 300 | 0 | max T 8, max levels 7, max phivals 7, max platmax 2, max wmax 2; stalls 41, stallloud 0, plat 35, windows 614 |
| CONTROL level3_ctrl1.out: CFI3_n48.json | n5v | 1 | fires: winstall 7 | |
| CONTROL level3_ctrl1.out: RINT_n48.json | n5v | 1 | fires: winstall 1 | |
| CONTROL level3_ctrl1.out: K1L10_n48.json | n5v | 1 | fires: NOTHING | |
| CONTROL level3_ctrl1.out: MWR4_2.json | n5v | 1 | fires: NOTHING | |
| CONTROL level3_ctrl2.out: CFI3_n48.json | n5v | 1 | fires: einF 20, l3fail 20, stallnocyc 22, rstall 2, winstall 12, wl3fail 14 | |
| CONTROL level3_ctrl2.out: MWR4_2.json | n5v | 1 | fires: einF 30, l3fail 30, stallnocyc 25, rstall 4, winstall 4, wl3fail 8 | |
| CONTROL level3_ctrl2.out: WC8_2.json | n5v | 1 | fires: einF 1, l3fail 1, stallnocyc 2, winstall 1, wl3fail 2 | |

| set (file in out/) | engine | genomes | sum of p1, pclos, p2, p3, p4, p5, t1, t2, t3 | descriptive |
| --- | --- | --- | --- | --- |
| plat3_corpus.out | n5v | 53 | 0 | plateaus 15, longest 13 steps, largest 100·(v − u)/(movers of Y + 1) = 14, longest tail 0, max T3 199 |
| plat3_ctrl1.out | n5v | 3 | CONTROL fires: pclos 210 | plateaus 5, longest 13 steps, largest 100·(v − u)/(movers of Y + 1) = 433, longest tail 2, max T3 24 |
| plat3_dead.out | n5v | 3 | 0 | plateaus 5, longest 8 steps, largest 100·(v − u)/(movers of Y + 1) = 88, longest tail 4, max T3 21 |
| plat3_mut_s2104.out | n5v | 1200 | 0 | plateaus 1059, longest 26 steps, largest 100·(v − u)/(movers of Y + 1) = 50, longest tail 25, max T3 33 |
| plat3_rand_s2103.out | n5v | 2800 | 0 | plateaus 396, longest 4 steps, largest 100·(v − u)/(movers of Y + 1) = 66, longest tail 4, max T3 13 |
| plat3_records.out | n5v | 25 | 0 | plateaus 14, longest 9 steps, largest 100·(v − u)/(movers of Y + 1) = 18, longest tail 2, max T3 114 |
| own3_plat_corpus.out | L-RED how3 | 53 | 0 | plateaus 15, longest 13 steps, largest 100·(v − u)/(movers of Y + 1) = 14, longest tail 0, max T3 199 |
| own3_plat_dead.out | L-RED how3 | 3 | 0 | plateaus 5, longest 8 steps, largest 100·(v − u)/(movers of Y + 1) = 88, longest tail 4, max T3 21 |
| own3_plat_records.out | L-RED how3 | 25 | 0 | plateaus 14, longest 9 steps, largest 100·(v − u)/(movers of Y + 1) = 18, longest tail 2, max T3 114 |

(Tables generated by box209/summ209.py.) Sets: level3_records / plat3_records: the 25 frozen k = 1 genomes of box 208 §7; level3_corpus /
plat3_corpus: the 53 corpus genomes of box 202 (every k); level3_dead / plat3_dead: the three genomes of RESULTS R118 (m)
(experiments/new/box191/inst/DEAD_SEG2P_d4_N8.json, _d7_N14.json, _d9_N18.json); level3_rand_*: 1,000 random k = 1 genomes (seed 2101) and
300 of each of six shapes (seed 2102); plat3_rand_s2103: 400 random genomes of each of k1, rand, dense, deep, noesc, esc, lvl0;
plat3_mut_s2104: 150 mutants (1 to 6 mutations, box203 aclimb203.mutate) of each of K1L10_n48, CFI3_n48, K1D4_n48, K1F21_n48, BLKX26_n48,
MWR4_2, CW4_n, RINT_n48; own3_*: the second engine on the same 81 frozen genomes.
- Controls. LV_CTRL=2 (FRONT := the highest lagging class): einF, l3fail, stallnocyc fire on every genome tried. LV_CTRL=1 (a non-feedback
  mover as S) is the control of the feedback-set counters only: it fires on CFI3 and RINT and not on K1L10 and MWR4, as in box 208.
  PL_CTRL=1 (Y := FRONT_u only): pclos fires. The tail counters t1, t2 and the bound counters boundfail, t3 have NO control: every tail
  is short (the longest has 25 steps) and no run is near a bound.
- struct209.py: structfail 0 on the 81 frozen genomes and on 2,100 random genomes (out/struct3.out).
- What the data do not test: the constants. The longest run (MW32_2, N 300, M 657) has T3 = 199 where the bound is 16,359,115,035; the
  smallest frozen genome (DEAD_SEG2P_d4_N8, N 8, M 16) has T3 = 10 where the bound is 262,769. Nor anything on genomes outside R104's
  shape.
- check209.sh (re-run by experiments/new/check.sh, section «BOX 209 LEVEL3», diffed against check209.out): six frozen genomes under
  level208.py --g3, both LV controls, four genomes and the PL control under plat209.py, 40 random k = 1 genomes, and the --dump /
  --hist round trip.

## 7. Relation to landed results and to the other lanes; contradiction check
- [Q] R125 QUIET3 / T-QUIET3 («T3 ≤ (1 + Σ_v (D^tot_E(v) − 1))·(L3 + 1)», Σ_v D^tot_E(v) recorded as OPEN): T3-ALL would close that sum from
  the other side (FLIPS3) and does not use QUIET3. PLATEAU3 would also sharpen QUIET3's window bound L3 = (M + 1)(2M + 1)(N + 1) +
  N(n3 − 1) to n_E3 for the windows before LAG is empty, since a step that changes no class is a stall; it is the mechanism of landed
  R126 QUIET-N (a step with no class change is a p-step; BR-SEG), applied to the lower part Y while classes above m still move.
- R125 CHAIN3 (polynomial for U(G) ≤ B under [E-LEV], degree growing like 5·2^B): N5XI-G3 would hold for every genome, with no [E-LEV],
  no U(G), degree 3. [E-LEV] is not used here: the argument never looks at the order of the e-priorities, only at «e-vertices are even
  and above every β».
- [Q] R118 (l) Corollary T3 («T3 ≤ C + R + (C + R + 1)·N», «N5′-xi's FL run on Γ3(G) is polynomial in N + M for every genome» ⇔ «R is
  polynomial along these Howard runs»): FLIPS3 gives R ≤ T3 polynomial, by bounding T3 directly rather than R.
- R118 (m) DEAD SEG-2P / ODD-FIXED (Odd's reply moves inside Λ-keeping runs, on three pinned genomes): not contradicted. PLATEAU3 (P4)
  says Odd's reply is fixed on Y during a plateau, where the CLASSES of Y are fixed, not only the cycle nodes. The three genomes are in
  §6's set: all counters 0, plateaus of 8, 2 and 3 steps.
- R125 DEAD RUN-TRANSFER (T3 is not T_CYC, by exact ties): the reason this box redoes box 208's proof on Γ3 instead of transferring its
  conclusion.
- L-SI box 99-102 and L-RED R232-R234 (claude/l-si d8945c4a, claude/l-red ef026a61; lane statements, unrefereed): their chain is
  «polynomial T3 ⇐ CONJECTURE DEEP3» (box 101 Add. A), shortened to CONJECTURE DEEP3-G (box 101 Add. C), with LAM-GAP (a one-player
  Howard window with every Λ constant lasts at most |Ch| + 1 iterations; SURVIVES L-RED 66) in the role BR-SEG-G has here. T3-ALL would
  give a polynomial T3 with no conjecture, by a different route: no SCC decomposition, no depth, no charging of flips. It would make the
  polynomial forms of DEEP3, DEEP3-G, DEEP3-all and MOVER-DEEP3 true as consequences (FLIPS3), which is weaker than proving them from
  their own side. Their exact statements (U-FREE: T3 ≤ N + M + 4; SCC-LIN: H(C) ≤ M_C) are not touched.
- [Q] Contradiction check. No landed statement gives a lower bound on T3 above linear: R125's DATA has max T3 129 (LEAP_k64); R124 records
  «it bounds none of F, T3, L(G) (OPEN)»; R117's REAL-IDEAL-S3 is a necessity statement for acyclic genomes, where landed R122 / R118
  bound the run. L-RED's kill-side climbs on Γ3 (R234 item 3) report small counts (Deep_3 19 at N 40), no super-polynomial family. None found.

## 8. Scope in TARGET.md's terms; not claimed; where to attack
- What is counted: iterations of N5′-xi (R118's [N5XI]) from SPEC's default start S3 on Γ3(G), under the standing SPEC premise 1E-N3 of
  R57 (b), as in R104 / R117 / R124 / R125. Inputs: the games Γ3(G) for the genomes G of R104 (Ξ-cycles and self-loops allowed).
- [Q] Not claimed: anything about N5 (R125: «says nothing about N5 (whose pre-fallback run on Ξ-cyclic genomes is not a Howard run)»), other
  starts, other games, general parity games; M3, M4; tightness. TARGET.md §2 asks for an algorithm polynomial on every parity game and
  §4 says a bound on a restricted class is not M4. G-N5-TIME stays OPEN.
- Where I would attack (beyond box 208 A5's list): (1) (K2′) / (K0′): are K0 and K3 really «in both Π or in neither» for the pads pb_g
  and for values compared across states; (2) (L2′): the pads pe_g of e-vertices with a mover successor; (3) (P4) case (3) on Γ3: (D1′)
  is a reading of the construction, not a quoted line; (4) (P5) / (P7): H contains pads and frozen vertices; BR-SEG-G is used on H with
  «Howard» in the packet's sense; (5) PLATEAU3 (ii) is new relative to box 208, which used landed QUIET-N for the tail; (6) N5XI-G3's
  step «any tie rule»: REACH3-ALL's run is a HOW3 run by R125's definition, but its tie rule is not this lane's engine's.

## 9. Next
- If boxes 208 / 209 survive L-RED and L-COMP: freeze as one packet (LEVEL, PLATEAU on Γ(G); LEVEL3, PLATEAU3, T3-ALL, N5XI-G3 on Γ3),
  premises by landed R-id as in §1.
- The question behind G-N5-TIME is untouched: which parity games, beyond padded genomes, have a top scale with non-negative weights
  (only even vertices above a threshold enter Π) and a one-player game below it on every plateau. That is where a general statement
  would have to start; nothing is claimed about it here.
