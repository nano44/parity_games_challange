# Box 208 (D18): the lowest-lagging-class potential on IDEAL-CYC — CANDIDATE: a window of constant class(R) has at most M(N + 2M) + N steps, class(R) changes at most 2M(N + 2M) times, so T_CYC would be polynomial at Ξ-feedback number 1 and at most (P + N)(P + 1)^k in general (L-NEW successor 72)
Written 2026-11-12 (date -u in the commit). Lead 11:27Z («go»): «BOX 208 = F1-F2 first … Your claim is large, and D1 applies in full … 1. Write
Lemma LEVEL and Theorem WIN with complete proofs … Quote every premise by script from LANDED RESULTS … Label everything CANDIDATE. 2. Make
the step «unless FRONT_t contains a whole cycle of Ξ_(σ_b)» airtight … 3. Make the counting explicit … 4. Push the counter tool with its
controls and frozen outputs … 5. Keep the scope line exactly as you wrote it … Also say how F2 relates to box 206's DEEP-k1 / LOUD-SPLIT and
to R121-R126, and whether any landed statement already contradicts it.»
**SCOPE LINE: IDEAL-CYC on Γ(G) only; not Γ3, not N5′-xi, not M4; G-N5-TIME stays OPEN.**
**LABEL: every statement of this box is a CANDIDATE** (lane, unrefereed, not yet attacked by another lane, not yet run on a second engine).
The body (§0-§10) is what the Lead ruled on (F1-F2). **Addendum A** (at the end) is a further CANDIDATE found while the body's data ran:
a bound on plateaus that would make T_CYC polynomial for EVERY genome. It is kept apart so that the body can be attacked on its own.
D1 (owner, verbatim): «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the
fleet's own, as wrong until it passes the gauntlet below.» What is claimed here is not an algorithm claim and not a TARGET.md claim: it is
a bound on the number of Howard steps of one restricted model (IDEAL-CYC, RESULTS R118 (a)) on one restricted family of games (the genome
games Γ(G) of R104), and it is to be treated as wrong until L-RED and a second engine have been through it. N5′-xi stays a CANDIDATE (D1).
Other labels used: DATA (unit, set, scope, counter) / READING / OPEN. Tools: experiments/new/box208/ (level208.py, run208.sh, quotes208.py,
check208.sh; outputs box208/out/); «BOX 208 LEVEL» in experiments/new/check.sh.

## 0. Answer
- The brief's item ((Q2) through PAID's chains) is answered by a different route, which does not use Lemma PAID. Fix a reference state b
  of the run. A vertex LAGS at a state t ≤ b if its class at t is not yet its class at b. Let m_t be the lowest class of a lagging vertex,
  FRONT_t the lagging vertices of that class, Φ_t := (m_t, −|FRONT_t|).
- **Lemma LEVEL (CANDIDATE; §3).** For every genome (any Ξ-feedback number): Φ never falls. At a step it stays equal exactly when no vertex
  of FRONT_t changes class (a STALL), and a stall forces FRONT_t to contain a whole cycle of the functional graph Ξ_(σ_b): movers
  x_1 → … → x_r → x_1 with x_(i+1) = xt(x_i, σ_b(x_i)), their gates (x_i, σ_b(x_i)) and those gates' β-faces. m_t takes at most 2M values
  (the class at b of a gate, or (c, ∅) for a β-vertex c), so Φ takes at most P := 2M(N + 2M) values.
- **Theorem WIN (CANDIDATE; §5).** Let S be a set of movers meeting every cycle of the Ξ-graph. On an interval of states on which every
  vertex of S keeps its class there is no stall: at most M(N + 2M) steps, all loud, until every class has its value at the interval's
  end, then at most N quiet steps. So the interval has at most A := M(N + 2M) + N steps.
- **Corollary R-INT (CANDIDATE) = box 207's (Q2).** At Ξ-feedback number 1, with R a feedback vertex: every window of constant class(R) has
  at most A steps, and λ_max ≤ M(N + 2M) + 1.
- **Theorem R-HEIGHT (CANDIDATE; §6) = box 207's (Q1).** At Ξ-feedback number 1: a step that changes class(R) is never a stall (reference
  b = the last state), so D^tot(R) ≤ P + 1.
- **Theorem K1-TCYC (CANDIDATE; §6).** At Ξ-feedback number 1: T_CYC ≤ P·(A + 1) + N (about 2M²(N + 2M)²). This would be CONJECTURE
  DEEP-k1 of box 206.
- **Theorem FVS-TCYC (CANDIDATE; §6).** Ξ-feedback number k: T_CYC ≤ (P + N)·(P + 1)^k. Polynomial for every FIXED k, degree growing with
  k. It is NOT a polynomial bound for genomes in general: for unbounded k nothing is gained, and general genomes stay OPEN.
- READING (what makes it work). On IDEAL-CYC the class of a vertex equals the class of its successor on the play, except at an e-vertex,
  where it is strictly higher (§2 (K3)). At class level the game is therefore a shortest-path game with non-negative weights: Odd
  minimises, Even maximises, only e-vertices cost. LEVEL is Dijkstra's argument turned against Howard: the lowest lagging class cannot
  wait, except on a cycle of weight 0, and the cycles of weight 0 are exactly the Ξ-cycles. A feedback vertex set that keeps its classes
  cuts them all.
- DATA (§7): every must-0 counter of level208.py is 0 on the 25 frozen k = 1 genomes (T_CYC up to 114), on the 53 corpus genomes of box
  202 (k from 1 to above 12, T_CYC up to 199; the window counters for k ≤ 3), on 2,000 random k = 1 genomes and 3,000 random genomes of
  six other shapes (short runs, T_CYC ≤ 12), on 2,000 mutants of eight frozen k = 1 genomes (T_CYC up to 37), and, on a second engine
  (L-RED 54's own.py), on the same 78 frozen genomes, with the same run lengths. Both controls fire.
- Contradiction check (§8): no landed statement contradicts these candidates, and none implies them; R126's line records the k = 1
  question as OPEN.

## 1. Setting and premises (every «…» on a line marked [Q] is quoted by script from trunk docs/RESULTS.md: quotes208.py, out/quotes208.out)
Setting: IDEAL-CYC(G) for any genome G; states 0, …, T := T_CYC; Ω_t(v) = (Λ_t(v), Π_t(v), k_t(v)) the value of v under (σ_t, σ̄_t);
E_t(v) := the e-vertices of Π_t(v); class_t(v) := (Λ_t(v), E_t(v)); s_t(v) := the successor of v on its play at t.
- [Q] R104 ([DEF]): «Even movers of priority 0; Odd gates of priority 1 with a W-face e and a Ξ-face β»; «β of priority 6 + 2·rank +
  parity with edges to the Ξ-target and to u, or to u alone»; «e of even priority above every β with one edge to the W-target or to the
  top even self-loop c_W»; «a closed core u = K0 (Even, top + 2) → {K1, K3}, K1 (Even, 5) → {K0, K1}, K2 (Odd, 3) → {K1, K2}, K3 (Even,
  top + 3) → {K1, K2}»; «β → its Ξ-target (u when the target is X), K0 → K3, K1 → K1, K3 → K2».
- Readings of [DEF] used, as in the landed packet P-N5-QN §1 (R126): (D1) e_g's only in-edge is from g; (D3) the core is entered from
  outside only at u = K0; (D4) c_X has no in-edge from another vertex; (D5) the Ξ-graph on the movers.
- [Q] R126, the Ξ-feedback number: «the minimum size of a set of movers meeting every cycle (self-loops count) of the Ξ-graph on the
  movers (an edge x → xt(x, j) for each option whose Ξ-target is a mover; options whose Ξ-target is X omitted)».
- [Q] R118 (a): «The game is Γ(G) with every Even vertex that is not a mover frozen at its start successor. Odd is unrestricted (gates
  and K2).»; the step: «every mover x goes to a successor of ⊴-largest Ω_t value, and keeps σ_t(x) if σ_t(x) is such a successor».
- [Q] R118 (c) DOM: «For every mover x, step t and successor y of x: Ω_(t+1)(x) ⊵ ext(x, Ω_t(y)).»
- [Q] R118 (e), its reason: «each vertex's Λ moves only to a vertex of strictly larger reward among at most 2M + 3 possible cycle nodes».
- [Q] R118's premise [VJ]: «VJ00 §4.2 / Friedmann arXiv 1106.0778 §3 for the order ⊴ on values (Λ, Π, k)».
- [VJ] as used (the reading of box 207 Addendum B, P-N5-QN §1): Λ(v) is the most relevant vertex of the cycle of v's play; Π(v) is the
  set of vertices on the path from v to Λ(v), before Λ(v), that are more relevant than Λ(v); (VJ-1) if Λ ≠ Λ′, Ω ◁ Ω′ iff reward(Λ) <
  reward(Λ′); (VJ-2) if Λ = Λ′ and Π ≠ Π′, with z the most relevant vertex of Π Δ Π′: Ω ◁ Ω′ iff (z ∈ Π′ and z even) or (z ∈ Π and z
  odd). The third clause (length) decides only when Λ = Λ′ and Π = Π′. ext(x, (Λ, Π, k)) = (Λ, Π ∪ ({x} if x is more relevant than Λ),
  k + 1).
- [Q] R121 E-MON: «If Λ_t(v) = Λ_(t+1)(v), then E_t(v) ≤ E_(t+1)(v).»; E-DOM: «Every vertex more relevant than some e-vertex is an
  e-vertex, c_W, K0 or K3, by [DEF]»; the order on e-sets: «sets of e-vertices compared lexicographically by their most relevant
  differing element».
- [Q] R123 CN2: «For every genome G, every positional pair of IDEAL-CYC(G) and every vertex v, the cycle node of v's play has priority
  ≥ 2. So no gate (priority 1) and no mover (priority 0) is ever a cycle node, and no gate or mover is ever in a set Π.»
- [Q] R123 B-ONLY: «In IDEAL-CYC(G), for every genome G, every state t and every vertex v other than c_W and the e-vertices whose
  successor is c_W, Λ_t(v) is less relevant than every e-vertex (it is a β-vertex, K1, K2 or the unused loop).»
- [Q] R123 NO-TIE: «At every state and every gate g, Ω_t(e_g) ≠ Ω_t(β_g). So LOC-GATE applies at every gate and state.»
- [Q] R123 LOC-GATE: «Let G be any genome, t a state of a run of IDEAL-CYC(G), g a gate, a := σ̄_t(g), b := its other face, Ω := Ω_t.
  If Ω(a) ≠ Ω(b), then Ω(a) ◁ Ω(b).»
- [Q] R123 LOC-K2: «At every state σ̄_t(K2) = K1 and Ω_t(K1) ◁ Ω_t(K2).»
- [Q] R126 QUIET-N: «every maximal window of quiet steps has at most N steps».
- ORDER ON CLASSES: (Λ, E) < (Λ′, E′) iff reward(Λ) < reward(Λ′), or Λ = Λ′ and E <lex E′ (the most relevant element of E Δ E′ lies in
  E′). It is a strict total order on the classes that occur: the cycle nodes are β-vertices, K1, K2, c_X or c_W (B-ONLY and its two
  exceptions), with pairwise different priorities (R104: «a distinct β-rank»), hence different rewards; the lex order is total (box 207
  Addendum B).
- Not used anywhere below: a bound on k (except where stated), [E-LEV], ascents, depth, Lemma PAID, R-LOCAL, LOUD-SPLIT, any lane lemma of
  another lane, any Γ3 fact.

## 2. Five class facts (K1)-(K5)
- **(K1) MONOTONE.** class_t(v) ≤ class_(t+1)(v) for every vertex v and step t.
  Proof: Λ moves only to larger reward (R118 (e)'s reason); while Λ is fixed, E does not fall (E-MON). ∎
- **(K2) COARSE.** Let Ω = (Λ, Π, ·), Ω′ = (Λ′, Π′, ·) be values of two vertices outside the core, at the same state or at two states, with
  classes c, c′. If Ω ⊴ Ω′ then c ≤ c′.
  Proof: If Λ ≠ Λ′, (VJ-1). Let Λ = Λ′. If E = E′ then c = c′. Otherwise let z_E be the most relevant element of E Δ E′ and z the most
  relevant vertex of Π Δ Π′; E Δ E′ ⊆ Π Δ Π′, so z is at least as relevant as z_E, and by E-DOM z is an e-vertex, c_W, K0 or K3. c_W is in
  no set Π (its only out-edge is its self-loop, so on a play it is the cycle node). K0 and K3: a vertex outside the core has cycle node
  K1 iff its play enters the core, and then it enters at K0 (D3) and runs K0 → K3 → K2 → K1 (frozen start; LOC-K2), so K0, K3 ∈ Π (both
  are more relevant than K1); if Λ ≠ K1 the play does not enter the core. So K0 and K3 are in both of Π, Π′ or in neither, and z is an
  e-vertex: z = z_E, of even priority. By (VJ-2), Ω ◁ Ω′ iff z ∈ Π′, i.e. iff z_E ∈ E′, i.e. iff E <lex E′. ∎
- **(K3) ALONG THE PLAY.** At every state t: (a) Λ_t(v) = Λ_t(s_t(v)) for every vertex; (b) no e-vertex lies on the cycle of a play;
  (c) class_t(v) = class_t(s_t(v)) for every vertex v that is not an e-vertex; (d) for an e-vertex e whose successor w is a mover:
  class_t(e) = (Λ_t(w), {e} ∪ E_t(w)), e ∉ E_t(w), so class_t(e) > class_t(w); (e) the classes of K0, K1, K2, K3, c_W, c_X and of the
  e-vertices with successor c_W are the same at every state.
  Proof: (a) v's play is v followed by s_t(v)'s play: the same cycle. (b) Let an e-vertex f lie on the cycle of a play. Its successor is
  not c_W (then f's play would be f, c_W, c_W, …, and f would not be on its cycle). Λ_t(f) is the most relevant vertex of that cycle, so
  at least as relevant as f, against B-ONLY. (c) If v ≠ Λ_t(v), the path from s_t(v) to the cycle node is the path from v without v, so
  Π_t(v) = Π_t(s_t(v)) ∪ ({v} if v is more relevant than Λ_t(v)), and E_t(v) = E_t(s_t(v)) because v is not an e-vertex. If v = Λ_t(v),
  Π_t(v) = ∅, and Π_t(s_t(v)) holds vertices of the cycle only, none of them an e-vertex (b): E_t(s_t(v)) = ∅ = E_t(v). (d) By B-ONLY
  Λ_t(e) is less relevant than e, so e ≠ Λ_t(e), e ∈ Π_t(e), and as in (c) Π_t(e) = Π_t(w) ∪ {e}; e ∉ Π_t(w) since the path from e to
  its cycle node visits e once. (e) c_W and c_X: self-loops. An e-vertex with successor c_W: cycle node c_W, the most relevant vertex
  of its play, so Π = ∅. Core: K0 → K3 → K2 (frozen, R118 (a) with R104's start), K2 → K1 (LOC-K2), K1 → K1: cycle node K1, no e-vertex. ∎
- **(K4) GATES.** class_t(g) = min(class_t(e_g), class_t(β_g)) for every gate g and state t.
  Proof: a := σ̄_t(g) has Ω_t(a) ◁ Ω_t(b) for the other face b (LOC-GATE with NO-TIE); the faces are outside the core, so class_t(a) ≤
  class_t(b) (K2); class_t(g) = class_t(a) (K3 (c)). ∎
- **(K5) HOWARD DOMINATES.** For every mover x, step t and gate y of x: class_(t+1)(x) ≥ class_t(y).
  Proof: DOM: Ω_(t+1)(x) ⊵ ext(x, Ω_t(y)). x has priority 0 and no cycle node has priority below 2 (CN2), so ext(x, ·) adds nothing to
  Π: ext(x, Ω_t(y)) has Λ_t(y) and Π_t(y). (K2), for the mover x and the gate y. ∎
- DATA: level208.py counts (K1), (K3), (K4), (K5) directly (monofail, k3fail, k4fail, k5fail); all 0 on every set of §7.

## 3. Lemma LEVEL (CANDIDATE)
Setting: any genome; states a ≤ b of the IDEAL-CYC run (b the REFERENCE state). For a ≤ t ≤ b:
- LAG_t := {v : class_t(v) ≠ class_b(v)}. By (K1), v ∈ LAG_t iff class_t(v) < class_b(v).
- If LAG_t ≠ ∅: m_t := min{class_t(v) : v ∈ LAG_t}; FRONT_t := {v ∈ LAG_t : class_t(v) = m_t}; Φ_t := (m_t, −|FRONT_t|), ordered
  lexicographically.
- A step t → t + 1 with t < b and LAG_t ≠ ∅ is a STALL if class_(t+1)(v) = class_t(v) for every v ∈ FRONT_t.
**Statement.** For every t < b with LAG_t ≠ ∅:
- (L1) LAG_(t+1) ⊆ LAG_t. If the step t → t + 1 is a stall: LAG_(t+1) ≠ ∅, FRONT_(t+1) = FRONT_t and Φ_(t+1) = Φ_t. If it is not a
  stall: LAG_(t+1) = ∅ or Φ_(t+1) > Φ_t.
- (L2) Every vertex of FRONT_t is a mover, a gate or a β-vertex whose frozen successor is a mover.
- (L3) (α) some mover z ∈ FRONT_t has σ_t(z) ∉ LAG_t, and then m_t = class_b(σ_t(z)); or (β) there is a play at t whose cycle consists
  of movers, their chosen gates and those gates' β-faces, all in FRONT_t, and then m_t = (c, ∅) for its cycle node c, a β-vertex.
- (L4) If the step t → t + 1 is a stall, there are r ≥ 1 and movers x_1, …, x_r with x_(i+1) = xt(x_i, σ_b(x_i)) for all i (indices
  mod r), such that for every i the mover x_i, its gate g_i := (x_i, σ_b(x_i)) and the β-face β_(g_i) lie in FRONT_t, and σ̄_t(g_i) =
  β_(g_i). In particular x_1 → x_2 → … → x_r → x_1 is a cycle of the Ξ-graph, all of whose vertices lag at t.
- (L5) On [a, b] the potential Φ takes at most 2M·(N + 2M) values; at most M·(N + 2M) if case (β) of (L3) never occurs on [a, b].
**Proof.**
(L1) Let v ∈ LAG_(t+1). By (K1), class_t(v) ≤ class_(t+1)(v) < class_b(v): v ∈ LAG_t, and class_(t+1)(v) ≥ class_t(v) ≥ m_t. Hence
LAG_(t+1) ⊆ LAG_t; and if LAG_(t+1) ≠ ∅: (i) m_(t+1) ≥ m_t; (ii) if m_(t+1) = m_t then FRONT_(t+1) ⊆ FRONT_t (for v ∈ FRONT_(t+1):
v ∈ LAG_t, and m_t ≤ class_t(v) ≤ class_(t+1)(v) = m_(t+1) = m_t, so class_t(v) = m_t).
- Stall: every v ∈ FRONT_t has class_(t+1)(v) = m_t < class_b(v), so v ∈ LAG_(t+1) with class m_t. Hence LAG_(t+1) ≠ ∅, m_(t+1) ≤ m_t,
  so m_(t+1) = m_t by (i), FRONT_(t+1) ⊇ FRONT_t, and equality by (ii). Φ_(t+1) = Φ_t.
- Not a stall: some v ∈ FRONT_t has class_(t+1)(v) > m_t (by (K1) a changed class is larger). If LAG_(t+1) = ∅ there is nothing to
  show. Otherwise, case m_(t+1) > m_t: Φ rises in its first coordinate. Case m_(t+1) = m_t: FRONT_(t+1) ⊆ FRONT_t by (ii), and v ∉
  FRONT_(t+1) because class_(t+1)(v) ≠ m_(t+1); so |FRONT_(t+1)| < |FRONT_t|: Φ rises in its second coordinate. By (i) there is no
  third case.
(L2) K0, K1, K2, K3, c_W, c_X and the e-vertices with successor c_W never lag (K3 (e)). Let e be an e-vertex with a mover successor
w. If w ∉ LAG_t, then class_t(e) = (Λ_t(w), {e} ∪ E_t(w)) = (Λ_b(w), {e} ∪ E_b(w)) = class_b(e) (K3 (d) at t and at b): e ∉ LAG_t. If
w ∈ LAG_t, then class_t(w) < class_t(e) (K3 (d)), so class_t(e) is not the lowest lagging class: e ∉ FRONT_t. A β-vertex whose frozen
successor is u has the class of K0 at every state (K3 (c), (e)) and never lags. What is left: movers, gates, β-vertices with a mover
successor.
(L3) Take v ∈ FRONT_t and its play p_0 = v, p_1, p_2, … at t. By (K3 (c), (d)) class_t(p_(i+1)) ≤ class_t(p_i), so every p_i has class
≤ m_t; hence every p_i is non-lagging or lies in FRONT_t (a lagging vertex has class ≥ m_t). The cycle of the play is K1's self-loop,
c_W's self-loop, or a cycle without e-vertex (K3 (b)), without core vertex (a play that enters the core ends in K1's loop) and without
c_X (D4): a cycle of movers, gates and β-vertices, which alternate as mover → chosen gate → β-face → mover.
- If every vertex of the cycle lags: they are all in FRONT_t and have the class of the cycle node c, which is (c, ∅) (K3 (c): Π(c) = ∅);
  c is not a mover or gate (CN2), so it is a β-vertex. This is (β).
- Otherwise some lagging vertex z on the play has a non-lagging successor y := s_t(z): if no vertex of the cycle lags, take the last
  lagging p_i (it exists: p_0 lags; it is before the cycle); if some but not all vertices of the cycle lag, go round the cycle. z ∈
  FRONT_t. z is not a gate: class_b(z) ≤ class_b(y) by (K4) at b (y is a face of z), = class_t(y) (y does not lag), = class_t(z) by
  (K3 (c)) at t; with (K1) class_b(z) = class_t(z), so z would not lag. z is not a β-vertex: y is its frozen successor at both states,
  so class_b(z) = class_b(y) = class_t(y) = class_t(z) (K3 (c)). z is not an e-vertex, a core vertex, c_W or c_X (L2). So z is a mover,
  y = σ_t(z) is a gate, and m_t = class_t(z) = class_t(y) = class_b(y). This is (α).
(L4) Assume the step is a stall. Define a map s on FRONT_t (its vertices are movers, gates and β-vertices with a mover successor, (L2)):
- z a mover: s(z) := σ_b(z) =: w, a gate of z. class_b(w) = class_b(z) (K3 (c) at b) > m_t (z lags, class_t(z) = m_t). class_t(w) ≤
  class_(t+1)(z) (K5) = class_t(z) = m_t (stall, z ∈ FRONT_t). So class_t(w) < class_b(w): w lags at t, hence class_t(w) ≥ m_t, hence
  class_t(w) = m_t: w ∈ FRONT_t.
- g a gate: s(g) := σ̄_t(g) =: r, a face of g; class_t(r) = class_t(g) = m_t (K3 (c)). If r did not lag: class_b(g) ≤ class_b(r) (K4 at
  b) = class_t(r) = m_t = class_t(g), so g would not lag (K1). So r lags, r ∈ FRONT_t, and by (L2) r is not e_g: r = β_g, i.e.
  σ̄_t(g) = β_g. (This case does not use the stall.)
- β_g with frozen successor a mover y = xt(g): s(β_g) := y. class_t(y) = class_t(β_g) = m_t and class_b(y) = class_b(β_g) ≠ m_t
  (K3 (c) at t and at b): y ∈ FRONT_t. (This case does not use the stall.)
s maps the finite non-empty set FRONT_t to itself, so iterating s from any vertex reaches a cycle of s. On it the kinds alternate
mover x → gate (x, σ_b(x)) → its β-face → mover xt(x, σ_b(x)): the statement, with the movers of the cycle as x_1, …, x_r. Each
x_i → x_(i+1) is the Ξ-edge of the option σ_b(x_i) of x_i (for r = 1 a Ξ self-loop).
(L5) By (L3), m_t is the class at b of one of the M gates (case α) or (c, ∅) for one of the M β-vertices c (case β): at most 2M values,
at most M without case (β). By (L2), 1 ≤ |FRONT_t| ≤ N + 2M. ∎
- Remark (reference state). b is any state of the run. With b = T the lagging vertices are those not yet at their final class.
- Remark (the airtight step, in one sentence). At a stall, every mover of the front finds its b-gate in the front (because Howard would
  otherwise have lifted it, (K5)), every gate of the front finds its current face in the front and that face is its β-face (because an
  e-face in the front would have a lower lagging successor, and a non-lagging face would pin the gate, (K4)), and every β-vertex of the
  front finds its Ξ-target in the front (K3); a map of a finite set into itself has a cycle.

## 4. The counting, made explicit
Fix a ≤ b, and let a = u_1 ≤ v_1 < u_2 ≤ v_2 < … < u_q ≤ v_q be the states of [a, b] with LAG ≠ ∅, grouped into the maximal intervals
[u_i, v_i] of constant Φ (u_(i+1) = v_i + 1; Φ takes each value on one interval, since it never falls). Let b′ := v_q + 1 if q ≥ 1 and
b′ := a otherwise: the first state with LAG = ∅ (LAG_b = ∅, and LAG only shrinks).
- (C1) q ≤ 2M(N + 2M) =: P (L5); q ≤ M(N + 2M) without case (β).
- (C2) The steps inside an interval [u_i, v_i] are stalls and the steps u_(i+1) − 1 → u_(i+1) and v_q → b′ are not (L1). So the number
  of non-stall steps on [a, b′] is exactly q ≤ P, and b′ − a = q + Σ_i (v_i − u_i).
- (C3) On an interval [u_i, v_i] with u_i < v_i (a PLATEAU) the front is one set J at all its states, every vertex of J keeps the
  class m there (L1), and J contains the vertices x_1, …, x_r of a cycle of the Ξ-graph (L4 at u_i). So LEVEL by itself does not bound
  the length of a plateau: it says that a plateau is an interval on which a whole Ξ-cycle keeps its class. The length is bounded by
  applying §5 to that interval with a larger frozen set (§6).
- (C4) For b′ ≤ t ≤ b every class equals its value at b ((K1): class_(b′) ≤ class_t ≤ class_b = class_(b′) pointwise), so the steps
  after b′ are quiet, and b − b′ ≤ N by QUIET-N.
Constants used below: P := 2M(N + 2M); A := M(N + 2M) + N.

## 5. Theorem WIN and Corollary R-INT (CANDIDATES)
**Theorem WIN.** Let G be any genome and S a set of movers that meets every cycle of the Ξ-graph (self-loops count; S = ∅ if the Ξ-graph
is acyclic). Let a ≤ b be states such that class_t(x) = class_b(x) for every x ∈ S and every a ≤ t ≤ b. With reference b and b′ as in §4:
(i) no step t → t + 1 with a ≤ t < b′ is a stall: each changes the class of a vertex of FRONT_t, so it is loud;
(ii) case (β) of (L3) does not occur on [a, b′), and b′ − a ≤ M(N + 2M);
(iii) the steps after b′ are quiet and b − b′ ≤ N.
Hence b − a ≤ M(N + 2M) + N = A.
Proof. No vertex of S lags at any t ∈ [a, b]. (i) At a stall, (L4) gives a cycle of the Ξ-graph all of whose vertices lag; S meets it:
contradiction. (ii) In case (β) the movers of the play cycle form a cycle of the Ξ-graph (mover → chosen gate → β-face → its Ξ-target),
all lagging: the same contradiction. So by (C1) q ≤ M(N + 2M), and by (i) and (C2) every interval [u_i, v_i] is a single state: b′ − a
= q. (iii) is (C4). ∎
**Corollary R-INT.** Let G have Ξ-feedback number 1 and let R be a feedback vertex (a mover on every cycle of the Ξ-graph). For every
window W = [a, b] (a maximal interval of states of constant class(R)): b − a ≤ A; at most M(N + 2M) of the steps between states of W
are loud, and they come first; λ(W) ≤ M(N + 2M) + 1 in box 207's count (which adds the step that enters W). So CONJECTURE R-INT of box
207 would hold, with λ_max ≤ M(N + 2M) + 1. ∎
- Check against k = 0: S = ∅ gives T_CYC ≤ M(N + 2M) + N for Ξ-acyclic genomes, weaker than landed R122's T_CYC ≤ N. Consistent; not new.
- DATA: counters winstall, wbeta, wmid, wbound (§7) are 0; the longest loud prefix of a window is 91 steps (CWRR16_n, N 171, M 487),
  against M(N + 2M) = 557,615.

## 6. Theorems R-HEIGHT, K1-TCYC, FVS-TCYC (CANDIDATES)
**Theorem R-HEIGHT.** Let G have Ξ-feedback number 1 and R a feedback vertex. Then class(R) changes at at most P steps: D^tot(R) ≤ P + 1.
Proof. Reference b := T, a := 0. Let class(R) change at the step t → t + 1. Then R ∈ LAG_t. If the step were a stall, (L4) would give a
cycle of the Ξ-graph inside FRONT_t; R is on it, so R ∈ FRONT_t, and at a stall no vertex of FRONT_t changes class: contradiction. So
the step is one of the q ≤ P non-stall steps (C2). ∎
**Theorem K1-TCYC.** For every genome with Ξ-feedback number 1: T_CYC ≤ P·(A + 1) + N.
Proof. Reference b := T, a := 0, R a feedback vertex. By (C2), b′ = q + Σ_i (v_i − u_i). For a plateau [u_i, v_i], (C3) gives a cycle of
the Ξ-graph inside J; R is on it; so class(R) is the same at all states of [u_i, v_i], and Theorem WIN with S = {R} on that interval
gives v_i − u_i ≤ A. So b′ ≤ q(A + 1) ≤ P(A + 1), and T − b′ ≤ N (C4). ∎
- Equivalently, by windows: at most P + 1 windows (R-HEIGHT), each of at most A steps (R-INT), and at most P steps between them.
- Size: P·(A + 1) + N = 2M²(N + 2M)² + 2M(N + 2M)(N + 1) + N. The measured runs are far below it (§7: the longest k = 1 run is CW16_n,
  T_CYC = 114, N 171, M 472, where the bound is 554,122,317,291); the bound is crude, and nothing is claimed about its tightness.
**Theorem FVS-TCYC.** For every genome with Ξ-feedback number k: T_CYC ≤ (P + N)·(P + 1)^k.
Proof. Fix a set F_0 of k movers meeting every cycle of the Ξ-graph. For S ⊆ F_0 let W(S) be the largest b − a over the intervals [a, b]
on which every vertex of S keeps its class, and w_j := max{W(S) : |S| = j}. By Theorem WIN, w_k = W(F_0) ≤ A ≤ P + N. Let S ≠ F_0 and
[a, b] such an interval; reference b. For a plateau [u_i, v_i], (C3) gives a cycle of the Ξ-graph inside J; F_0 meets it in some x; x
lags, so x ∉ S (the vertices of S do not lag); every vertex of S ∪ {x} keeps its class on [u_i, v_i]: v_i − u_i ≤ W(S ∪ {x}) ≤
w_(|S|+1). By (C2) and (C4): b − a ≤ q(w_(|S|+1) + 1) + N ≤ P(w_(|S|+1) + 1) + N. So w_j ≤ P(w_(j+1) + 1) + N for j < k. By downward
induction w_j ≤ (P + N)(P + 1)^(k−j): for j = k it is w_k ≤ P + N; and P((P + N)(P + 1)^(k−j−1) + 1) + N ≤ (P + N)(P + 1)^(k−j−1)·P +
(P + N) ≤ (P + N)(P + 1)^(k−j). T_CYC = W(∅) = w_0. ∎
- For k = 1 this is (P + N)(P + 1), weaker than K1-TCYC's P(A + 1) + N (A + 1 ≤ P + N).
- What FVS-TCYC is NOT: a polynomial bound for genomes in general. The exponent grows with k, and k can be of order N. Whether nested
  plateaus (a plateau on which a second Ξ-cycle stalls above the first, and so on) really multiply is OPEN. DATA (§7): the longest
  plateau on the frozen sets has 13 steps (DSALT6_n108, k = 8, T_CYC 21); stalls at which some other vertex changes class («stallloud»)
  occur 23 times on the 53 corpus genomes, all at k ≥ 3, and 0 times on the 25 k = 1 records. (Addendum A is a CANDIDATE answer:
  a plateau has at most N + 2M + 5 steps, whatever k is.)

## 7. DATA (level208.py; engine box203 gfc203.hist_ideal / box191 idealcyc; outputs box208/out/, run by run208.sh and run208b.sh)
Counters (definitions in the tool's header; unit: states t < b with a lagging vertex unless stated; scope: every vertex of Γ(G)):
- class facts: monofail (K1), k3fail (K3), k4fail (K4), k5fail (K5);
- LEVEL with reference b = T: einF (L2), l3fail (L3), phifail (L1: Φ falls, or stays equal at a non-stall step, or changes at a stall),
  stallnocyc (L4), nofvs (unit stalls; the cycle of (L4) misses the feedback set found; k ≤ 3 only), rstall (unit steps, k = 1: a stall
  at which the class of a feedback vertex changes; R-HEIGHT), boundfail (unit genomes: more than P values of Φ, or at k = 1 T_CYC above
  P(A + 1) + N);
- Theorem WIN, for every maximal interval of constant classes of S (k = 1: every single feedback vertex in turn; 2 ≤ k ≤ 3: one minimum
  feedback set; k = 0: S = ∅; k ≥ 4: not run), reference its last state: winstall (unit steps: stalls before LAG is empty), wbeta (case
  (β) without (α)), wl3fail, wmid (unit intervals: a class changes after LAG was empty), wbound (unit intervals: more than M(N + 2M)
  steps before LAG is empty, or more than N after).
DATA table to be read with its outputs; «all 0» means every must-0 counter above is 0 on every row.
| set (file in out/) | rows | sum of the 16 must-0 counters | descriptive |
| --- | --- | --- | --- |
| level208_records.out | 25 genomes, k in {1} | 0 | max T 114, max levels 15, max Phi values 114, stalls 31 (loud 0), plateaus 14 (longest 9), intervals 556 (longest loud prefix 91) |
| level208_corpus.out | 53 genomes, k in {1, 2, 3, 4, 7, 8, 10, 11, 12, 99} | 0 | max T 199, max levels 16, max Phi values 199, stalls 48 (loud 23), plateaus 15 (longest 13), intervals 615 (longest loud prefix 53) |
| level208_g3_records.out | 8 genomes, k in {1, 2} | 0 | max T 59, max levels 8, max Phi values 59, stalls 11 (loud 0), plateaus 5 (longest 4), intervals 110 (longest loud prefix 22) |
| level208_rand_deep_s2082.out | 500 | 0 | max T 12, max levels 8, max phivals 10, max platmax 3, max wmax 2; stalls 108, stallloud 1, plat 94, windows 735 |
| level208_rand_dense_s2082.out | 500 | 0 | max T 12, max levels 8, max phivals 9, max platmax 3, max wmax 1; stalls 112, stallloud 0, plat 91, windows 910 |
| level208_rand_esc_s2082.out | 500 | 0 | max T 4, max levels 2, max phivals 4, max platmax 2, max wmax 2; stalls 50, stallloud 1, plat 44, windows 847 |
| level208_rand_k1_s2081.out | 2000 | 0 | max T 7, max levels 4, max phivals 5, max platmax 3, max wmax 3; stalls 192, stallloud 1, plat 168, windows 4378 |
| level208_rand_lvl0_s2082.out | 500 | 0 | max T 10, max levels 7, max phivals 7, max platmax 4, max wmax 1; stalls 112, stallloud 1, plat 95, windows 550 |
| level208_rand_noesc_s2082.out | 500 | 0 | max T 10, max levels 7, max phivals 7, max platmax 3, max wmax 1; stalls 59, stallloud 0, plat 49, windows 863 |
| level208_rand_rand_s2082.out | 500 | 0 | max T 10, max levels 7, max phivals 9, max platmax 5, max wmax 2; stalls 70, stallloud 0, plat 61, windows 1003 |
| level208_g3_rand_k1_s2084.out | 500 | 0 | max T 6, max levels 3, max phivals 4, max platmax 2, max wmax 4; stalls 52, stallloud 0, plat 47, windows 1087 |
| level208_g3_rand_rand_s2085.out | 300 | 0 | max T 10, max levels 7, max phivals 8, max platmax 2, max wmax 3; stalls 37, stallloud 0, plat 33, windows 579 |
| mut208_BLKX26_n48_s2086.out | 250 | 0 | max T 33, max levels 7, max phivals 31, max platmax 21, max wmax 22; stalls 535, stallloud 2, plat 246, windows 3361, k0 0, k1 156, k2-3 93, k4+ 1 |
| mut208_CFI3_n48_s2086.out | 250 | 0 | max T 25, max levels 3, max phivals 21, max platmax 9, max wmax 12; stalls 1153, stallloud 0, plat 379, windows 945, k0 0, k1 155, k2-3 95, k4+ 0 |
| mut208_CW4_n_s2086.out | 250 | 0 | max T 32, max levels 6, max phivals 32, max platmax 23, max wmax 28; stalls 127, stallloud 1, plat 13, windows 2548, k0 0, k1 181, k2-3 69, k4+ 0 |
| mut208_K1F21_n48_s2086.out | 250 | 0 | max T 32, max levels 6, max phivals 32, max platmax 17, max wmax 24; stalls 284, stallloud 2, plat 223, windows 9064, k0 0, k1 171, k2-3 79, k4+ 0 |
| mut208_K1L10_n48_s2086.out | 250 | 0 | max T 31, max levels 8, max phivals 28, max platmax 4, max wmax 17; stalls 499, stallloud 4, plat 359, windows 4921, k0 0, k1 170, k2-3 79, k4+ 1 |
| mut208_K1L7_n48_s2086.out | 250 | 0 | max T 37, max levels 8, max phivals 34, max platmax 7, max wmax 25; stalls 559, stallloud 0, plat 329, windows 3412, k0 0, k1 160, k2-3 89, k4+ 1 |
| mut208_MWR4_2_s2086.out | 250 | 0 | max T 31, max levels 5, max phivals 31, max platmax 26, max wmax 28; stalls 129, stallloud 1, plat 12, windows 2020, k0 0, k1 176, k2-3 74, k4+ 0 |
| mut208_RINT_n48_s2086.out | 250 | 0 | max T 24, max levels 4, max phivals 23, max platmax 4, max wmax 22; stalls 237, stallloud 0, plat 220, windows 741, k0 0, k1 149, k2-3 100, k4+ 1 |
| CONTROL level208_ctrl1.out: CFI3_n48.json | 1 | fires: winstall 7 | |
| CONTROL level208_ctrl1.out: RINT_n48.json | 1 | fires: winstall 1 | |
| CONTROL level208_ctrl1.out: K1L10_n48.json | 1 | fires: NOTHING | |
| CONTROL level208_ctrl1.out: MWR4_2.json | 1 | fires: NOTHING | |
| CONTROL level208_ctrl1_rand_k1_s2083.out: rand k1 seed 2083 (300 genomes) | 1 | fires: winstall 11, wbeta 39 | |
| CONTROL level208_ctrl2.out: CFI3_n48.json | 1 | fires: einF 20, l3fail 20, stallnocyc 22, rstall 2, winstall 12, wl3fail 14 | |
| CONTROL level208_ctrl2.out: MWR4_2.json | 1 | fires: einF 30, l3fail 30, stallnocyc 25, rstall 4, winstall 4, wl3fail 8 | |
| CONTROL level208_ctrl2.out: WC8_2.json | 1 | fires: einF 1, l3fail 1, stallnocyc 2, winstall 1, wl3fail 2 | |
(Table generated by box208/summ208.py from the files named; «rows» = genomes or samples; the 16 must-0 counters are those listed above.)
- level208_records.out: the 25 frozen k = 1 genomes of boxes 202-207 (MWR4/8/16_2, CW4/8/16_n, CWRR4/8/16_n, CWRQ8_n, K1F21_n48, K1F34_n84,
  K1C16_n400, K1L7_n48, K1L10_n48, K1D4_n48, BLKX23_n48, BLKX26_n48, B400_r32, CFI3_n48, RINT_n48, k1fail_202, naive_k1_s71, ST4_k1, ST8_k1;
  their sha1 in those boxes' SHA1SUMS). Every single feedback vertex of each genome was used as S in turn.
- level208_corpus.out: the 53 genomes of experiments/new/box202/inst/ (k = 1: 8 genomes, k = 2: 19, k = 3: 1, k = 4: 5, k = 7, 8, 10, 11,
  12: 10, k above fvs202's cap 12 (printed 99): 10; no genome with k = 0). The window counters (winstall … wbound) and nofvs are run for
  k ≤ 3 only (28 genomes); for the 25 genomes with k ≥ 4 only the class facts and (L1)-(L5) are counted.
- level208_rand_*.out: random genomes, IDEAL-CYC from the genome's start: 2,000 with k = 1 (box202 k1srch202.mk, seed 2081) and 500 for
  each of the eg195.gen shapes rand, dense, deep, noesc, esc, lvl0 (seed 2082; k up to 10). Short runs (T ≤ 12).
- mut208_*.out: mut208.py, seed 2086: 250 mutants (1 to 6 random mutations of box203 aclimb203.mutate, Ξ-edges free) of each of eight
  frozen k = 1 genomes; the mutants have k = 1, 2-3 or more (columns k1, k2-3, k4+); long runs (T up to the «max T» column).
- level208_g3_*.out: the same counters on the N5′-xi run from S3 on Γ3(G) up to its first fallback (--g3). DATA only: no statement of
  this box is about Γ3 (§8).
- Controls: LV_CTRL=1 (S := one mover that is not a feedback vertex) fires on CFI3_n48 (winstall 7) and RINT_n48 (winstall 1) and on a
  random k = 1 set (seed 2083: winstall 11, wbeta 39); it does not fire on K1L10_n48 and MWR4_2 (there the replaced vertex happens to
  keep the windows stall-free), so the control is genome-dependent. LV_CTRL=2 (FRONT := the HIGHEST lagging class) fires on all three
  genomes tried (einF, l3fail, stallnocyc).
- What this DATA does and does not test. It tests the five class facts and (L1)-(L4) / WIN (i)-(iii) state by state, on this lane's
  engine (box203 gfc203 over box191 idealcyc and experiments/si/si.py's VJ engine) and, for the 78 frozen genomes, on a second engine
  (last rows). It does not test the constants: no run comes near P or M(N + 2M) (the largest count of Φ values is 199, on MW32_2,
  where P = 2,120,796). Any other engine can be wired through level208.py --hist (format in the tool's header).
- Descriptive, for §6's open question: stalls at which some other vertex changes class (stallloud) are 0 on the 25 k = 1 records, 23
  on the corpus (9 genomes, all with k ≥ 3), and occur a few times in the random and mutant sets (columns above), also at k = 1.
- SECOND ENGINE (run208b.sh H; ownhist208.py): the same counters, computed by level208.py --hist on the run of L-RED 54's independent
  IDEAL-CYC implementation (claude/l-red 72e2c5dc, experiments/red/r221q/own.py: its own builder of Γ(G), its own VJ valuation, Odd's
  answer by its own one-player strategy iteration; read by `git show`, not copied into this lane; sha1 in out/own208_engine.sha1):
| set (file in out/) | rows | sum of the 16 must-0 counters | descriptive |
| --- | --- | --- | --- |
| own208_records.out | 25 genomes | 0 | max T 114, stalls 31 (loud 0), plateaus 14 (longest 9), intervals 556 (longest loud prefix 91); T differs from this lane's engine on 0 genomes |
| own208_corpus.out | 53 genomes | 0 | max T 199, stalls 48 (loud 23), plateaus 15 (longest 13), intervals 615 (longest loud prefix 53); T differs from this lane's engine on 0 genomes |
  This is a second ENGINE under the same counter code; it is not an independent check of the counters themselves, and not L-COMP's.

## 8. How this sits with boxes 204-207, with R121-R126 and with the Γ3 lane work; contradiction check
- Box 207 (this lane; R-LOCAL): DEEP-k1 ⟺ (Q1) «D^tot(R) polynomial» ∧ (Q2) R-INT. Corollary R-INT is (Q2) and Theorem R-HEIGHT is (Q1),
  each proved directly, without R-LOCAL. Lemma PAID (box 207 A-C, SURVIVED L-RED 65) is not used; the brief's «chained flips» item is
  not needed if WIN survives: a window has at most M(N + 2M) loud steps of any kind, hence at most that many flip steps.
- Box 206 (DEPTH-COUNT, LOUD-SPLIT, CONJECTURE DEEP-k1 «for some fixed c, Q_(>c) is polynomial at k = 1»): Q_(>c) ≤ Q ≤ T_CYC, so
  K1-TCYC would give DEEP-k1 for every c, with no depth analysis. LOUD-SPLIT («T_CYC polynomial iff Q_(>c) polynomial») is consistent and
  becomes unnecessary at k = 1. The dead items of box 206 (depth bounded, loud depth bounded, LD-ASC, BLOCK-DESC) are not contradicted:
  LEVEL bounds steps, not depths or class heights per block.
- Box 204 (Theorem EQ: T_CYC polynomial iff D_mov polynomial): with K1-TCYC, D_mov − 1 ≤ T_CYC would be polynomial at k = 1.
- [Q] R126's line states the k = 1 question as open: «it makes no new class of genomes on which T_CYC is polynomial, and at k = 1 it
  bounds the cycle nodes only (whether max_g min(D^tot(e_g), D^tot(β_g)) is polynomial in N + M at k = 1 is OPEN)». K1-TCYC would answer
  it: D^tot(v) − 1 ≤ T_CYC for every vertex. It would make the genomes of Ξ-feedback number ≤ k, for each fixed k, a new class on which
  T_CYC is polynomial.
- [Q] R122 (k = 0): «the Howard run of IDEAL-CYC(G) from any mover state has C = 0, R = 0 and T_CYC ≤ N». WIN with S = ∅ gives the
  weaker M(N + 2M) + N. No conflict.
- [Q] R118 (f): «T_CYC ≤ C + R + (C + R + 1)·N ≤ (C + R + 1)(N + 1).» K1-TCYC bounds T_CYC itself; R (the flip steps) is then ≤ T_CYC.
- R121 / R123 (HUB-ASC-G, ASC-T, UP-T: T_CYC polynomial when plays have boundedly many ascents, degree growing with the bound): a
  different restricted class (ascents, not feedback number); CW(n) has k = 1 and b − 1 ascents (box 206 C2), so it lies outside ASC-T's
  fixed-B regime and inside K1-TCYC's. No conflict.
- R124 / R125 (Γ3, N5′-xi, HOW3): not touched; see the Γ3 paragraph below.
- Dead statements recorded in R126's line (D1 «at k = 1 each gate flips at most 2·lamch(g) + 1 times», D3 «every e-sequence has at most
  k + 1 ascents») and the MWR(n) counts (flips 2n + 1, T 6n + 6) are not contradicted: all are linear or small.
- Contradiction check, method: `grep` of trunk docs/RESULTS.md (07139249) for T_CYC or IDEAL-CYC together with «super-polynomial»,
  «exponential», «2^» or «≥»: the only hit is R122's DATA sentence that T_CYC ≤ N is not tight on its set A. The lower-bound results R113
  (T^R(d)), R109 (T*(d)), R112 (T^R(3) = 8) are about the IDEAL model of R104 (N5's key-driven steps on Ξ-ACYCLIC genomes), not about
  IDEAL-CYC's Howard steps: at k = 0, landed R122 already gives T_CYC ≤ N on the same genomes. So no landed statement contradicts the
  candidates, and no lane record does either (the k = 1 records of boxes 203-207 and of L-RED R229-R233 are all linear in N).
- The brief's second question (scope: IDEAL-CYC on Γ here; box 100-102 and R232-R234 are on Γ3 / HOW3):
  - Is an R-window a WINDOW of L-SI's box 100? No. Box 100's window holds σ̄ on C and every Λ fixed, so it is a one-player Howard run;
    inside an R-window gates flip (CFI3_n48 window [4, 18]: 10 flips; RINT_n48 [2, 24]: 8) and Λ may change (in RINT's window Λ(R) is an
    even β and other vertices join that cycle node). An R-window is a union of box-100-type windows plus the flip steps between them.
  - Does LAM-GAP's one-player bound transfer to IDEAL-CYC at k = 1? LAM-GAP (box 101; SURVIVED L-RED 66, sharp form b − a ≤ |Ch|) is
    stated for every one-player game under the VJ valuation, so it applies as it stands to a stretch of an IDEAL-CYC run on which σ̄ and
    every Λ are fixed, with Ch = the movers. It bounds such a stretch, not a window. WIN is the two-player statement of the same kind:
    LAM-GAP is a Bellman–Ford induction on full values with Odd fixed; LEVEL is a Dijkstra induction on classes with Odd free, and Odd's
    freedom costs nothing because a gate's class is the minimum of its faces' classes (K4).
  - DEEP3 (box 100 §5.2 / box 102, on Γ3) is the Γ3 form of DEEP-k1 for the internal gates of one SCC. This box does NOT prove it: every
    statement here is on Γ(G). What a Γ3 form of LEVEL would need: R125's F1, DOM, CN2-3, LOC-GATE3, NO-TIE3, B-ONLY3, LOC-K2-3, E-MON3
    in place of §1's premises, a Γ3 form of E-DOM (L-SI's CORE-ABOVE, lane), and the pads treated like β-vertices in (K3) and (L4). It is
    NOT written. DATA only (level208.py --g3, the N5′-xi run from S3 to its first fallback; out/level208_g3_*.out): the same counters,
    see §7's last rows. If a Γ3 form held, it would give T3 polynomial for bounded k WITHOUT DEEP3, and would say nothing for unbounded k,
    where L-SI's chain (T3 polynomial ⇐ DEEP3) is still the only route on the table.

## 9. What is not claimed; open; next
- Not claimed: anything on Γ3, N5′-xi, N5 or general parity games; any algorithm claim; M3 or M4; a bound polynomial in N + M for all
  genomes; tightness of any constant; novelty of the abstract argument (READING: «Howard for the maximiser in a shortest-path game with
  non-negative weights and no zero-weight cycle makes at most (number of the maximiser's edges)·(number of vertices) iterations» is the
  same proof; I have not searched the literature for it, so it is not cited and not claimed as new).
- OPEN: (1) general k: do plateaus nest multiplicatively, or is there a bound polynomial in N + M (L-SI's CONJECTURE SCC-LIN / U-FREE
  would say linear)? (2) the Γ3 form. (3) the true order at k = 1: all records are linear, the bound is of degree 4.
- Side structure seen while looking for this (DATA, scratch count on 9 records, not committed as a counter): in every state with Λ(R) =
  K1 or an even β, class(R) is the largest class of any vertex on a play; so at k = 1 a stall with R in the front is a quiet step there.
  Not used; a possible sharpening (plateaus of length ≤ N in those states).
- Next: L-RED attack (the Lead routes it); an independent engine through level208.py --hist; then, if it survives, the Γ3 form.

## 10. Appendix: the argument without parity games (CANDIDATE; a READING aid, with its own engine)
This section is about a different object. It is here because it isolates the logic of §3 from the genome premises, so that an error in
the logic can be looked for separately from an error in the class facts (K1)-(K5).
- Object: a SHORTEST-PATH GAME: a finite graph, every vertex owned by Max or Min, a target, an integer weight ≥ 0 on every edge, and no
  cycle of total weight 0. For a positional Max strategy s, d_s(v) := the least weight of a path from v to the target in the graph where
  every Max vertex keeps only its edge s(v) (∞ if there is none). HOWARD: every Max vertex moves to an edge (z, y) of largest w(z, y) +
  d_s(y), keeping its edge if that is one of them.
- **Statement ABS (CANDIDATE).** From every positional start, Howard makes at most (number of edges of Max vertices)·(number of
  vertices) steps, and every step before the last one raises d at a vertex of the lowest lagging value.
- Proof (the same five facts, then §3 word for word). (K1′) d never falls: d_s is a feasible potential in the next graph (d_s(o) ≤ w +
  d_s(r) for every edge of a Min vertex; d_s(z) ≤ w + d_s(y) for the new edge of a Max vertex), so along any path of the next graph to
  the target d_s(v) ≤ its weight. (K3′) d_s(v) = w + d_s(y) along the chosen edge of a Max vertex and along a best edge of a Min vertex.
  (K4′) d_s(o) ≤ w + d_s(r) for every edge of a Min vertex. (K5′) after the step, with y′ the new successor of a Max vertex z and d′
  the new values: d′(z) = w(z, y′) + d′(y′) ≥ w(z, y′) + d_s(y′) ≥ w(z, y) + d_s(y) for every edge (z, y) of z. With reference b = the last state: a lagging vertex of the lowest lagging
  value m whose current edge leads to a lagging vertex has that edge of weight 0 (the successor's value would otherwise be below m); so
  as in (L3) m = w(z, y) + d_b(y) for an edge of a Max vertex z, at most one value per such edge; and as in (L4) a stall gives a map of
  the front into itself along weight-0 edges (Max vertex → its edge at b, Min vertex → a current best edge), hence a cycle of weight 0,
  which does not exist. So Φ rises at every step. ∎
- In this reading IDEAL-CYC at class level is such a game with the E-set as weight (an e-vertex adds itself, every other vertex adds
  nothing), Λ as a terminal value, and the Ξ-cycles as its cycles of weight 0; freezing the classes of a feedback vertex set turns those
  vertices into terminals.
- DATA (abs208.py, its own engine: Dijkstra for Min, no code of another box; out/abs208.out): counters monofail, phifail, levfail
  (m_t is not w(z, y) + d_b(y)), stall0 (a stall), boundfail, optfail (unit games with at most 9 vertices: the last d is not the pointwise
  maximum of d_s over ALL Max strategies, by enumeration): all 0 on 30,000 games with at most 9 vertices, 20,000 with at most 30 and
  3,000 with at most 120 (weights 0, 1, 2, 4, 8, 16, 32; weight-0 edges only to a higher index, so no weight-0 cycle); with weight-0
  edges anywhere (20,000 games) monofail, phifail, levfail, stallnocyc are 0. Control ABS_CTRL=1 (move to a SMALLEST edge) fires. The
  runs are short (at most 6 steps): this checks the logic, not any growth.
- Not claimed: that Statement ABS is new. I opened no source for it (notebook, «Sources opened», box 208).

## Addendum A (L-NEW successor 72; CANDIDATE: Lemma PLATEAU — a plateau has at most N + 2M + 5 steps, for every genome; so T_CYC ≤ P·(N + 2M + 6) + N for EVERY genome; written 2026-11-12 by date -u)
Found after the Lead's «go» of 11:27Z, while the body's data ran; NOT part of F1-F2 as ruled, so it is kept apart from the body, which
it does not change. The Lead has not seen it before this commit. **SCOPE LINE: IDEAL-CYC on Γ(G) only; not Γ3, not N5′-xi, not M4; G-N5-TIME
stays OPEN. LABEL: CANDIDATE.** D1 applies with more force than to the body: this is a bound for ALL genomes, the statement that boxes
100-207 did not reach, found within one session. Treat it as wrong until it has been attacked.
### A0. Answer
- §4 (C3) left the length of a plateau open, and §6 bounded it by freezing one more feedback vertex per level, which costs a factor P
  per level (Theorem FVS-TCYC). A plateau can be bounded directly. During a plateau the vertices of class ≤ m form a closed part Y of
  the game on which no class changes; there Odd does not move ((P4) below), so the run on Y is a run of Howard on a ONE-player game
  with every cycle node fixed, and landed R118 (i) BR-SEG-G bounds such a run by the number of Even vertices.
- **Lemma PLATEAU (CANDIDATE).** For every genome, every reference state b and every maximal interval [u, v] of states of constant Φ
  (reference b): v − u ≤ N + 2M + 5.
- **Theorem ALL-TCYC (CANDIDATE).** For every genome G: T_CYC ≤ P·(N + 2M + 6) + N, P = 2M(N + 2M). So the number R of flip steps and
  the number Q of loud steps would be polynomial for every genome, with no hypothesis on the Ξ-graph.
- If this stands, Theorems K1-TCYC and FVS-TCYC of §6 are special cases with worse constants; LEVEL, (C1)-(C4) and PLATEAU are the
  whole proof. Theorem WIN, R-INT and R-HEIGHT keep their own content (they are statements about windows of a feedback set).
### A1. Premises added (quoted by script, quotes208.py)
- [Q] R126 GATE-CLASS, NOT used (the step it could serve, (P4), is proved directly), quoted because (P4) agrees with it: «for every
  gate g and every step t, if σ̄_(t−1)(g) ≠ σ̄_t(g), then class_(t−1)(e_g) ≠ class_t(e_g) or class_(t−1)(β_g) ≠ class_t(β_g)».
- [Q] R118 (i) BR-SEG-G [any parity game, Howard from any σ_0, under H0]: «H0: every step t → t+1 switches some Even x with Λ_t(x) ≠ x
  and Λ_(t+1)(x) ≠ x.»; «(a) every maximal run of p-steps has at most n_E steps;»; the labels: «labelled C if some vertex's cycle node Λ
  changes, else R if Odd's optimal counterstrategy σ̄ (any fixed deterministic choice) changes somewhere, else p».
- [Q] R118 (b): «(b) Facts F1-F6 (§3 l. 68-83) with F4 REPLACED by F4′»; R123's setting [OPT]: «optimal at every vertex at once
  against σ_t».
- F1 as stated in the landed packet P-N5-XICYC §3 (R118 (b)): Ω_t ⊴ Ω_(t+1) pointwise, for every step t.
### A2. Lemma PLATEAU, proof
Let [u, v] be a maximal interval of constant Φ = (m, −|J|) with u < v (reference b; J := FRONT). By (L1) every step inside is a stall,
FRONT_s = J and class_s(x) = m for x ∈ J at every state s ∈ [u, v]. Y := {x : class_u(x) ≤ m}.
(P1) For every s ∈ [u, v]: {x : class_s(x) ≤ m} = Y, and class_s(x) = class_u(x) for x ∈ Y.
  A vertex of Y lags at u (then it is in J, class m throughout) or not (then its class is class_b at u, and by (K1) at every later
  state up to b). A vertex outside Y has class > m at u, and by (K1) at s.
(P2) Y is closed under plays: for x ∈ Y and s ∈ [u, v], s_s(x) ∈ Y. (K3 (c), (d): class_s(s_s(x)) ≤ class_s(x) ≤ m; (P1).)
(P3) For every mover x ∈ Y, every gate y of x and every s ∈ [u, v]: class_s(y) ≤ class_s(x); so every gate of a mover of Y is in Y.
  For s < v: class_s(y) ≤ class_(s+1)(x) (K5) = class_s(x) (P1). So y ∈ Y (P1), its class is constant on [u, v] (P1), and the
  inequality holds at s = v too.
(P4) For every gate g ∈ Y: σ̄_s(g) is the same face for all s ∈ [u, v], and it lies in Y.
  The chosen face has the class of g (K3 (c)), so it is in Y. If the other face is outside Y at u, it is outside Y at every s (P1): its
  class is > m ≥ class_s(g), so it is never the chosen one (K4). If both faces are in Y, neither changes class on [u, v] (P1). If
  their classes differ, the face of lower class is the chosen one at every s: the chosen face a has Ω_s(a) ◁ Ω_s(b) (LOC-GATE, NO-TIE),
  so class_s(a) ≤ class_s(b) (K2). If their classes are equal, then e_g ∈ E_s(e_g) = E_s(β_g) (K3 (d)), so the play of β_g at s passes
  e_g, hence g ((D1): the only in-edge of e_g is from g), and leaves g by e_g: σ̄_s(g) = e_g at every s. (K3 (d) applies: an e-vertex
  with successor c_W has the class (c_W, ∅), the largest class there is, which is above every lagging class m; so if e_g ∈ Y, its
  successor is a mover.) K2 (if in Y) goes to K1 at every state (LOC-K2).
(P5) The game H: vertices Y; a mover of Y keeps all its gates; every other vertex x of Y keeps the single successor s_u(x) (for a gate:
  its face σ̄_u(g); for a β- or e-vertex, K0, K1, K3, c_X: its frozen successor; K2 → K1). By (P2)-(P4) every successor is in Y: H is a
  parity game in which only the movers of Y have a choice. For s ∈ [u, v] and x ∈ Y the play of x under (σ_s, σ̄_s) stays in Y and uses
  H's edges, so Ω_s(x) is the value of x in H under σ_s restricted to Y (Odd has no choice in H). By (P3) the Howard step of IDEAL-CYC
  at a mover of Y compares exactly its successors in H, by these values, with the same tie rule. So σ_u, σ_(u+1), …, σ_(v+1),
  restricted to Y, are consecutive states of the Howard run of H from σ_u restricted to Y, as long as that run has not stopped.
(P6) It has not stopped before v: every step s → s + 1 with u ≤ s ≤ v changes σ at some mover of Y.
  Suppose not, for some s. Claim: for every s′ with s ≤ s′ ≤ b, σ_(s′) = σ_s on the movers of Y and Ω_(s′) = Ω_s on Y. Induction on
  s′; s′ = s is trivial. Step s′ → s′ + 1 (s′ < b): (i) no mover of Y switches: if s′ = s by assumption; if s′ > s, its gates are in Y
  (P3) and have the values of state s′ − 1, at which its current gate was kept as ⊴-largest (the step s′ − 1 → s′ kept σ on Y); so it
  is kept again. (ii) Ω_(s′+1) = Ω_(s′) on Y: Odd may answer σ_(s′+1) by σ̄_(s′) on the gates of Y; then the play from x ∈ Y is the play
  of state s′ (it stays in Y, where σ is unchanged), so by [OPT] Ω_(s′+1)(x) ⊴ Ω_(s′)(x); and Ω_(s′+1)(x) ⊵ Ω_(s′)(x) by F1. So the
  vertices of J ⊆ Y have class m at state b: they do not lag. Contradiction.
(P7) The steps u → u + 1, …, v − 1 → v of H's Howard run change σ (P6), change no cycle node (P1) and no Odd choice (there is none in
  H): they are v − u consecutive p-steps. H0 holds for H's run: the vertices that switch are movers, and a mover is never a cycle node
  (CN2; a positional pair of H is a positional pair of IDEAL-CYC(G)). By BR-SEG-G (a), v − u ≤ n_E(H) ≤ the number of Even vertices of
  Γ(G) = N + 2M + 5 (movers, β- and e-vertices, c_X, c_W, K0, K1, K3). ∎
### A3. Theorem ALL-TCYC, proof
Reference b := T, a := 0. By (C2) b′ = q + Σ_i (v_i − u_i) with q ≤ P (C1), and v_i − u_i ≤ N + 2M + 5 (PLATEAU). By (C4) T − b′ ≤ N.
So T_CYC ≤ P(N + 2M + 6) + N. ∎
### A4. DATA (plat208.py; engine level208.prep; outputs out/plat208_*.out)
Counters, each must-0, reference b = T, over every plateau [u, v] (u < v): p1 (P1: a vertex of Y changes class, or a vertex outside Y has
class ≤ m; unit (vertex, state)), pclos (P2; unit (vertex of Y, state)), p2 (P3; unit (mover of Y, gate, state)), p3 (P4; unit (Odd
vertex of Y, step)), p4 (P6: a step s → s + 1, u ≤ s ≤ v, at which no mover of Y switches), p5 (P7: v − u above the number of Even
vertices in Y; unit plateaus). Descriptive: plateaus, maxlen, maxpct := the largest 100·(v − u) / (number of movers in Y + 1).
| set (file in out/) | genomes | sum of p1, pclos, p2, p3, p4, p5 | descriptive |
| --- | --- | --- | --- |
| plat208_corpus.out | 53 | 0 | plateaus 15, longest 13 steps, largest 100·(v − u)/(movers of Y + 1) = 14 |
| plat208_ctrl1.out | 3 | CONTROL fires: pclos 210, p5 1 | plateaus 5, longest 13 steps, largest 100·(v − u)/(movers of Y + 1) = 433 |
| plat208_mut2_s2093.out | 600 | 0 | plateaus 302, longest 25 steps, largest 100·(v − u)/(movers of Y + 1) = 51 |
| plat208_mut_s2092.out | 600 | 0 | plateaus 846, longest 15 steps, largest 100·(v − u)/(movers of Y + 1) = 20 |
| plat208_rand_s2091.out | 3600 | 0 | plateaus 546, longest 4 steps, largest 100·(v − u)/(movers of Y + 1) = 57 |
| plat208_records.out | 25 | 0 | plateaus 14, longest 9 steps, largest 100·(v − u)/(movers of Y + 1) = 18 |
(Table generated by box208/summ208.py.) plat208_records.out: the 25 k = 1 genomes of §7; plat208_corpus.out: the 53 corpus genomes (every
k); plat208_rand_s2091.out: 600 random genomes for each of k1, rand, dense, deep, noesc, lvl0 (seed 2091); plat208_mut_s2092.out: 150
mutants of each of K1L10_n48, CFI3_n48, K1D4_n48 and DSALT6_n108 (k = 8); plat208_mut2_s2093.out: 150 mutants of each of MWR4_2, CW4_n,
BLKX26_n48 and K1F21_n48 (the bases whose mutants had the longest plateaus in §7). Control PL_CTRL=1 (Y := the front alone) fires.
Plateaus are short everywhere (the longest has 25 steps, on a mutant of K1F21_n48, N 48, M 97), so p5 is never near its bound: the
data test (P1)-(P6) state by state, not the bound N + 2M + 5.
### A5. What Addendum A would mean, and what it does not
- With LEVEL it would give, on IDEAL-CYC(G) for every genome: T_CYC, the number R of flip steps (R118's label), the number Q of loud
  steps and every D^tot(v) are at most P(N + 2M + 6) + N. R118's line says of R «no bound on R is claimed (OPEN)»; this would be one.
- It would NOT give anything on Γ3, N5′-xi or N5: the same scope line as the body. A Γ3 form needs, beyond §8's list, a Γ3 form of
  (D1) for the pads (the only way into e_g is g → pe_g → e_g) and BR-SEG-G on the one-player sub-game (it is stated for any parity
  game). Not written.
- It is not M4 and not a step-4 pass: the genome games are a restricted family (TARGET.md §4), IDEAL-CYC is a model, the claim is
  unrefereed, and G-N5-TIME stays OPEN.
- Contradiction check for ALL-TCYC (same method as §8): no landed statement gives a lower bound on T_CYC, on R or on Q of IDEAL-CYC
  beyond linear data. R118's line records Howard on Friedmann's switchallexp for N = 2, …, 7 with R = 4, 10, 24, 54, 116, 241 flip
  steps: those games are not genome games Γ(G), and ALL-TCYC says nothing about them (I have not analysed where the argument breaks on
  them). That record is the reason not to read this addendum as a statement about Howard
  in general: what is used is special to Γ(G) — Odd's choices are decided at class level (K2, K4, (P4)), where only e-vertices
  count and they count for Even, so the two-player part is a shortest-path game with non-negative weights, and everything with a sign
  (the β-vertices) lives below it, in a part where Odd does not move.
- Where it could be wrong (for the attacker): (P4) at a gate whose two faces are both in Y; (P5)'s claim that the
  actual Howard step at a mover of Y is the Howard step of H (it needs every gate of the mover in Y: (P3)); (P6), which uses [OPT] and
  F1 beyond the plateau; (P7), which applies BR-SEG-G to H, a sub-game that is not a genome game (BR-SEG-G is stated for any parity
  game under H0). LEVEL itself: (L3) and (L4) of §3.

## Addendum B (L-NEW successor 72; written 2026-11-12 after the push of 8db300fe: clarifications of proof wording in §2 and Addendum A, a third implementation that checks every reference state, three more genomes; no statement, bound or label changes)
The body and Addendum A are unchanged. **SCOPE LINE and LABEL as above: IDEAL-CYC on Γ(G) only; not Γ3, not N5′-xi, not M4; G-N5-TIME
stays OPEN; every statement a CANDIDATE.** The Γ3 form is a separate box (docs/new/N5-LEVEL3-box209.md).
### B1. Clarifications (each closes a step that was terse; found by my own re-reading (1) and by a fresh-context reviewer agent (1)-(4))
The reviewer agent was started by this session while the push ran, with the note, the landed premises and the engines to read, and the
order to find the gap. It is not a fleet referee, its report is not a signature, and it changes no label. Its verdict: no error found in
§2-§6 and Addendum A; four presentational gaps, listed here with their repairs.
- (1) (P6) (ii), the sentence «the play from x ∈ Y is the play of state s′ (it stays in Y, where σ is unchanged)». For s′ > v, (P2) is
  not available as stated. Repair, either of two: (a) let Odd answer σ_(s′+1) by σ̄_s, the counterstrategy of the state s inside the
  plateau, instead of σ̄_(s′): the play from x ∈ Y under (σ_s, σ̄_s) stays in Y by (P2), σ_(s′+1) = σ_s on the movers of Y by (i), so
  the play under (σ_(s′+1), σ̄_s) is that play, of value Ω_s(x); [OPT] gives Ω_(s′+1)(x) ⊴ Ω_s(x), and F1 with the induction hypothesis
  gives Ω_(s′+1)(x) ⊵ Ω_(s′)(x) = Ω_s(x). (b) Keep σ̄_(s′): by the induction hypothesis class_(s′) = class_s on Y, and vertices outside
  Y have class > m at s′ (K1), so {x : class_(s′)(x) ≤ m} = Y, and (K3 (c), (d)) at s′ keeps the play in Y. The conclusion of (P6) is
  unchanged.
- (2) (P6) (i) uses the rule of R118 (a), quoted in §1: «keeps σ_t(x) if σ_t(x) is such a successor». Spelled out: at the step
  s → s + 1 the mover x kept σ_s(x), so no gate of x had a strictly larger value at s; at s′ its gates have the same values and its
  current gate is the same, so it keeps it again.
- (3) (P5), «with the same tie rule». What is used: the restriction of the run to Y is A Howard run of H in the sense of BR-SEG-G's
  setting (P-N5-XICYC §5: «every Even v goes to a ⊴-best successor under Ω_t and keeps σ_t(v) when it is one»), namely the one whose
  choice among several ⊴-best gates is the run's own. BR-SEG-G holds for every such choice. (Exact ties among ⊴-best non-current gates
  do occur. In rv208.py the run and H use the same rule and the counter P5howard is 0; the reviewer agent reports that in its scratch
  runs, with a different rule in H than in the run, that counter fired 468 times. That observation is not reproduced by a lane tool.)
- (4) §2 (K5) applies (K2) to ext(x, Ω_t(y)), which is not the value of a vertex. (K2)'s proof uses only the pair (Λ, Π) of a play that
  starts outside the core, and ext(x, ·) changes neither (x is in no set Π, CN2): read (K2) for such triples.
- (5) My own note. (P4)'s three cases need only that the classes of the two faces are constant on the interval; so (P4)-(P7) also bound
  the interval after LAG is empty by N + 2M + 5 (Y := all vertices), without QUIET-N. Not needed in this box ((C4) uses landed QUIET-N,
  which is sharper); it is the form box 209 uses on Γ3.
### B2. A third implementation, every reference state (rv208.py; run208c.sh; summ208c.py; outputs out/rv208_*.out)
- rv208.py is the reviewer agent's checker, taken into the lane with a control and a mutation mode added: its own builder of Γ(G), its
  own valuation and order (by the definition), Odd's reply by its own Odd-side iteration, its own Howard run, its own 49 must-0
  counters, one per step of the note (premises re-tested: CN2, B-ONLY, NO-TIE, LOC-GATE, LOC-K2, F1, DOM; (K1)-(K5); (L1)-(L5) with the
  2M-set of m_t; (P1)-(P7) with H built and valued independently). It imports nothing of box203 / box208 / si.py; --xcheck compares its
  builder, run and values with box191 idealcyc / si.Engine state by state.
- Unlike level208.py (reference b = T, and the ends of feedback-set intervals) it runs LEVEL and PLATEAU for EVERY reference state
  b = 1, …, T. Unit of the LEVEL counters: pairs (b, t) with a lagging vertex; of the PLATEAU counters: (b, plateau) with the unit named
  in the tool; scope: every vertex of Γ(G).
| set (file in out/) | lines | genomes | sum of the 49 must-0 counters | VIOLATION lines | descriptive |
| --- | --- | --- | --- | --- | --- |
| rv208_ctrl1.out | 2 | 2 | CONTROL fires: L1rise 1, L1stall 29, L2 50, L3 50, L4beta 44, L4gate_face 21, L4mover 4, L4nocycle 47, P1 1267, P3 20, P4 24, P5howard 57, P5val 316 | 0 | max T 30, sum T 54, (b, t) pairs with a lagging vertex 54, stalls 47, non-stalls 7, case (β) only 0, plateaus 2 (longest 15; longer than the movers of Y: 0), equal-class gates met 16, (K2) pairs 8000 |
| rv208_frozen.out | 81 | 81 | 0 | 0 | max T 199, sum T 2707, (b, t) pairs with a lagging vertex 93856, stalls 1247, non-stalls 92609, case (β) only 623, plateaus 538 (longest 13; longer than the movers of Y: 0), equal-class gates met 187, (K2) pairs 321444 |
| rv208_mut_s2094.out | 8 | 480 | 0 | 0 | max T 33, sum T 10148, (b, t) pairs with a lagging vertex 115116, stalls 16734, non-stalls 98382, case (β) only 1740, plateaus 6787 (longest 26; longer than the movers of Y: 0), equal-class gates met 1664, (K2) pairs 1920000 |
| rv208_rand_s2095.out | 3 | 3300 | 0 | 0 | max T 11, sum T 5405, (b, t) pairs with a lagging vertex 9041, stalls 368, non-stalls 8673, case (β) only 5337, plateaus 311 (longest 4; longer than the movers of Y: 0), equal-class gates met 6, (K2) pairs 9314030 |
| rv208_xcheck.out | 81 | 81 | builder, run length, states and values equal to box191 idealcyc / si.Engine on 81 of 81 files | | max T 199 |
(Table generated by box208/summ208c.py.) rv208_frozen.out: the 25 k = 1 genomes of §7, the 53 corpus genomes and the three genomes of B3,
every reference state; rv208_xcheck.out: the same 81 files against box191 idealcyc / si.Engine; rv208_mut_s2094.out: 60 mutants (1 to 8
of the tool's own mutations) of each of K1L10_n48, CFI3_n48, RINT_n48, MWR4_2, CW4_n, BLKX26_n48, K1D4_n48, DSALT6_n108;
rv208_rand_s2095.out: 2,000 genomes of the tool's own generator (seed 2095), 1,000 more with the other tie rule TIE=min (seed 2096) and
300 of its mode «big» (seed 2097); rv208_ctrl1.out: the control RV_CTRL=1 on MWR4_2 and CFI3_n48 with b = T (it fires).
- In every set, no plateau is longer than the number of movers of Y (the bound proved is the number of Even vertices of Y).
- Not in the lane, so not DATA: the reviewer's hill-climbs over small genomes (objectives T, stalls, plateau length; about 35,500
  genomes visited, T up to 17, no violation) and its test of QUIET-N / GATE-CLASS with its own engine. Its scripts stayed in this
  session's scratch directory.
### B3. Three more genomes: the DEAD instances of landed R118 (m)
RESULTS R118 (m) records, on three pinned genomes, that Odd's reply moves inside runs of steps that keep every Λ (DEAD ODD-FIXED: «σ̄ is
constant on every run of Λ-keeping steps»). (P4) says less: σ̄ is constant on Y during a plateau, where the classes of Y are constant, not
only the cycle nodes. The three genomes (experiments/new/box191/inst/DEAD_SEG2P_d4_N8.json, _d7_N14.json, _d9_N18.json) are in
rv208_frozen.out and rv208_xcheck.out: every counter 0; they have plateaus of 8, 2 and 3 steps (b = T).
### B4. What the reviewer agent did not check (its own list)
- The proofs of the landed premises (it re-tested them numerically only; its test of BR-SEG-G on random one-player games had p-runs of
  at most 3 steps, so it says nothing: BR-SEG-G is used as landed).
- VJ theory: F1, [OPT], and «locally optimal ⇒ optimal» for Odd, which its engine assumes (cross-checked against the lane engine only).
- The size of the bounds: no run comes near P or N + 2M + 5, so the data test the mechanism, not the constants.
- §7's tables, §8's contradiction search, §10, anything on Γ3, and genomes outside R104's shape.
