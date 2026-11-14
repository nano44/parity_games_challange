# Packet P-N5-LEVEL (box 208 + Addenda A, B): Howard ALL-SWITCH strategy improvement (Even = MAXIMISER improves; switch-best with keep-if-best tie rule) with VJ values on IDEAL-CYC(G), for every R104 genome G: the lowest-lagging-class potential rises at every step that is not a stall (LEVEL), a stall freezes a closed one-player part of the game (PLATEAU), and T_CYC ≤ P·(N + 2M + 6) + N with P = 2M(N + 2M) (ALL-TCYC)
L-NEW successor 73, D1 / D14 / D18 / D21. Lead brief 2026-11-12 (session start): «FREEZE PACKET P-N5-LEVEL (box 208 + Addenda A, B as
one packet, with box 209 NOT included; PR-6 resolved: one packet)»; «Premises by landed R-id only, each quoted by script at a pinned
trunk commit»; «No lane lemma as a premise». Lead 17:52Z («go»): «CHANGE: KEEP K1-TCYC and FVS-TCYC»; «a proposed RESULTS line L-1 by
script, frozen with the packet». FROZEN at push. Later text goes to docs/new/P-N5-LEVEL-fixes.md, append-only.
Source, history only: docs/new/N5-LEVEL-box208.md (box 208 body + Addenda A, B; L-NEW successor 72; l-new 8db300fe and 3f896099). Every
proof is carried here in full; nothing is cited from that file. NOT in this packet: box 208 §8 and §10 (relations to older boxes; the
abstract reading ABS), box 209 (the Γ3 form), box 210 (split-form games).
Labels: PROVED (lane) = proved in this lane and unrefereed; by CLAUDE.md a claim is a result only when Lean checks it or two referees
have signed it with its gaps listed, so until then every PROVED (lane) row is a CANDIDATE. DATA (unit, set, scope, counter) / READING (not to sign).
D1 (owner, verbatim): «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the
fleet's own, as wrong until it passes the gauntlet below.» This packet claims no algorithm. It bounds the number of steps of one
improvement rule in one model on one restricted family of games, and D1 applies to it in full.
This packet is NOT a TARGET.md claim, NOT M3 and NOT M4. It does not decide G-N5-TIME (§13).

## Scope (explicit)
- Rule: Howard ALL-SWITCH strategy improvement in which Even, the MAXIMISER of the value order, improves and Odd answers optimally:
  at every step EVERY mover goes to a ⊴-best successor and keeps its current successor if that is one (switch-best, keep-if-best;
  among several ⊴-best non-current successors any choice). Values: Vöge–Jurdziński (VJ) triples (Λ, Π, k). This is the step of RESULTS
  R118 (a), quoted in §1.
- Games and run: IDEAL-CYC(G) of R118 (a) for EVERY genome G of R104 (Ξ-cycles and Ξ self-loops allowed): Γ(G) with every Even vertex
  that is not a mover frozen at R104's start; states 0, …, T_CYC of the run that R118 (a) defines.
- NOT covered, rule: single-switch rules, and any rule other than the one above. Every theorem of §6-§8 uses (K5), through (L4) or
  (P3), and (K5) needs every mover to go to a ⊴-best successor at every step. (Fleet literature record, not opened by this lane and not a premise: L-LIT T69
  Addendum A1, claude/l-lit 4a0db9d1, reports from Björklund–Vorobyov, DAM 155 (2007) 210-229, §10, acyclic shortest-path instances on
  which a single-switch rule is exponential. This lane cites T69, not the paper.)
- NOT covered, games: the argument uses the genome's shape at the steps named in §9, first of all through E-DOM (R121) and B-ONLY
  (R123). It is not an argument about Howard's rule on parity games in general. DATA (L-COMP 19 BOX 43, cited in §9, not re-run
  here): lifted to Friedmann's game G_N, the counter of (K5) is 0 on G_1 and first fires on G_2 at the step 5 → 6.
- NOT covered, algorithms: not N5 (SPEC S1-S5; its S4a step is not a Howard step); not N5′-xi, neither on Γ3(G) (box 209 is a separate
  CANDIDATE of this lane and is not in this packet) nor off Γ3 (L-SI 52's box 104, Lemma WRAP, lane and unrefereed, claude/l-si 26704e01,
  has N5′-xi replay Howard's rule on a wrapper of every parity game); not M4. G-N5-TIME stays OPEN.
- What it would give if signed: on IDEAL-CYC(G), for every genome, a bound polynomial in N + M on T_CYC, hence on the number of steps
  at which σ̄ changes (R118's count R, of which R118's line says «no bound on R is claimed (OPEN)») and on the number of steps at
  which some class changes. Nothing else.

## To sign
| § | statement | label | premises |
| --- | --- | --- | --- |
| §3 | Class facts (K1)-(K5) | PROVED (lane) | [DEF] with (D3); [VJ]; R118 (a), (c) DOM, (e)'s reason; R121 E-MON, E-DOM; R123 CN2, B-ONLY, NO-TIE, LOC-GATE, LOC-K2 |
| §4 | Lemma LEVEL (L1)-(L5) | PROVED (lane) | §3; [DEF] with (D4); R123 CN2 |
| §5 | Counting (C1)-(C4) | PROVED (lane) | §4; R126 QUIET-N (in (C4) only) |
| §6 | Theorem WIN | PROVED (lane) | §4, §5 |
| §6 | Corollary R-INT | PROVED (lane) | Theorem WIN; R126's Ξ-feedback number |
| §6 | Theorem R-HEIGHT | PROVED (lane) | §4, §5; R126's Ξ-feedback number |
| §6 | Theorem K1-TCYC | PROVED (lane) | §4, §5, Theorem WIN; R126's Ξ-feedback number |
| §6 | Theorem FVS-TCYC | PROVED (lane) | §4, §5, Theorem WIN; R126's Ξ-feedback number |
| §7 | Lemma PLATEAU (P1)-(P7) | PROVED (lane) | §3, §4; [DEF] with (D1); R118 (a), (b) F1, (i) BR-SEG-G (a) with H0; R123 CN2, LOC-K2, [OPT] (spelled out in R122) |
| §8 | Theorem ALL-TCYC, with its bullet «Consequences» | PROVED (lane) | §4, §5, §7 |
| §8-§14 | the arithmetic «Against K1-TCYC and FVS-TCYC», remark SHARP, genome-only steps, referee items, DATA, check record, TARGET diff, machine checks | READING / DATA (not to sign) | |
- The rows of §3-§6 do not use §7. If a referee refuses PLATEAU, LEVEL, WIN, R-INT, R-HEIGHT, K1-TCYC and FVS-TCYC still stand or fall
  on their own (Lead ruling 17:52Z).
- When ALL-TCYC is signed it supersedes K1-TCYC and FVS-TCYC as bounds on T_CYC for every genome with M ≥ 2 and k ≥ 1 (§8 gives the
  arithmetic); at k = 0, where K1-TCYC does not apply, landed R122's T_CYC ≤ N is sharper than FVS-TCYC and ALL-TCYC.
- No other premise: no lane packet, no lane lemma of this or another lane (Lemma PAID, R-LOCAL, LOUD-SPLIT, LAM-GAP / SHARP are not
  used), no Γ3 fact, no P-N5-CHAIN fact, no [E-LEV], no bound on ascents or on depth, no Lean theorem (Lean is named where a step
  coincides with a lane-level Lean theorem, never as the proof of record).

## 1. Premises (landed R-ids; every «…» on a bullet marked [Q …], here and in §13, is checked by script, experiments/new/box211/quotes211.py, inside the named entry of docs/RESULTS.md at trunk claude/vibrant-johnson-nxvvxo 68c8d29339d5945efe6878a7e4cfc9d6a1611d48, in the named landed packet file at its pinned sha1, or in TARGET.md; output box211/quotes211.out)
- [Q R104] [DEF], definitions of the genome and of Γ(G) only: «Even movers of priority 0; Odd gates of priority 1 with a W-face e and a
  Ξ-face β»; «β of priority 6 + 2·rank + parity with edges to the Ξ-target and to u, or to u alone»; «e of even priority above every β
  with one edge to the W-target or to the top even self-loop c_W»; «an unused even self-loop of priority 2; c_W's priority top is the
  least even number at least 2 above every other priority so far»; «a closed core u = K0 (Even, top + 2) → {K1, K3}, K1 (Even, 5) →
  {K0, K1}, K2 (Odd, 3) → {K1, K2}, K3 (Even, top + 3) → {K1, K2}»; «with start σ = the genome start at movers, β → its Ξ-target (u
  when the target is X), K0 → K3, K1 → K1, K3 → K2»; the β-vertices have pairwise different priorities: «a distinct β-rank with a
  parity».
- [Q P-N5-QN] Readings of [DEF], as in the packet landed as R126 (docs/new/P-N5-QN.md §1, sha1 97254bd2a97f28bb0c14ab5f4d236ee723821dd9):
  «(D1) each gate g has its own e-vertex e_g, whose only in-edge is from g»; «(D3) the core is entered from outside only at u = K0
  (the β's escape edge)»; «(D4) the unused self-loop c_X has no in-edge from another vertex». (That packet's (D2) is E-DOM, quoted
  below from R121; its (D5) is the Ξ-graph, quoted below from R126.)
- [Q R118] [VJ], R118's own premise: «VJ00 §4.2 / Friedmann arXiv 1106.0778 §3 for the order ⊴ on values (Λ, Π, k)».
- [Q R118] (a) IDEAL-CYC and the step: «The game is Γ(G) with every Even vertex that is not a mover frozen at its start successor. Odd
  is unrestricted (gates and K2).»; «every mover x goes to a successor of ⊴-largest Ω_t value, and keeps σ_t(x) if σ_t(x) is such a
  successor»; «T_CYC := the number of steps to the first state where no mover has a strictly better successor».
- [Q R118] (b) F1: «Facts F1-F6 (§3 l. 68-83) with F4 REPLACED by F4′»; R118's premise line: «for F1 (Ω_t ⊴ Ω_(t+1) under a Howard
  step, an unambiguous non-empty switch set)».
- [Q P-N5-XICYC] F1 and ext as stated in the packet landed as R118 (docs/new/P-N5-XICYC.md §3, sha1
  149e2414be657ba12472faa4f46d5a251f2d3e98): «F1 (from [R15a]): Ω_t ⊴ Ω_(t+1) pointwise, for every step t.»; «ext(v, (Λ, Π, k)) :=
  (Λ, Π ∪ {v if v is more relevant than Λ}, k + 1)».
- [Q R15] (a), the source of F1: «Lemma A: for any non-empty unambiguous set I of improvements of σ (VJ00 §4.4), Ωσ ⊴
  Ω_{Switch_I(σ)}.»
- [Q R118] (c) DOM: «For every mover x, step t and successor y of x: Ω_(t+1)(x) ⊵ ext(x, Ω_t(y)).»
- [Q R118] (e), its reason: «each vertex's Λ moves only to a vertex of strictly larger reward among at most 2M + 3 possible cycle
  nodes».
- [Q R118] (i) BR-SEG-G, scope «any parity game, Howard from any σ_0, under H0»: «H0: every step t → t+1 switches some Even x with
  Λ_t(x) ≠ x and Λ_(t+1)(x) ≠ x.»; «(a) every maximal run of p-steps has at most n_E steps;»; the labels: «labelled C if some
  vertex's cycle node Λ changes, else R if Odd's optimal counterstrategy σ̄ (any fixed deterministic choice) changes somewhere, else p».
- [Q P-N5-XICYC] BR-SEG-G's setting in that packet (§5): «G is any parity game on n vertices, with n_E Even vertices. Run Howard from
  any σ_0: every Even v goes to a ⊴-best successor under Ω_t and keeps σ_t(v) when it is one.»
- [Q R121] E-MON: «If Λ_t(v) = Λ_(t+1)(v), then E_t(v) ≤ E_(t+1)(v).»; E-DOM: «Every vertex more relevant than some e-vertex is an
  e-vertex, c_W, K0 or K3, by [DEF]»; the order on e-sets: «sets of e-vertices compared lexicographically by their most relevant
  differing element».
- [Q R123] CN2: «For every genome G, every positional pair of IDEAL-CYC(G) and every vertex v, the cycle node of v's play has priority
  ≥ 2. So no gate (priority 1) and no mover (priority 0) is ever a cycle node, and no gate or mover is ever in a set Π.»
- [Q R123] B-ONLY: «In IDEAL-CYC(G), for every genome G, every state t and every vertex v other than c_W and the e-vertices whose
  successor is c_W, Λ_t(v) is less relevant than every e-vertex (it is a β-vertex, K1, K2 or the unused loop).»
- [Q R123] NO-TIE: «At every state and every gate g, Ω_t(e_g) ≠ Ω_t(β_g). So LOC-GATE applies at every gate and state.»
- [Q R123] LOC-GATE: «Let G be any genome, t a state of a run of IDEAL-CYC(G), g a gate, a := σ̄_t(g), b := its other face, Ω := Ω_t.
  If Ω(a) ≠ Ω(b), then Ω(a) ◁ Ω(b).»
- [Q R123] LOC-K2: «At every state σ̄_t(K2) = K1 and Ω_t(K1) ◁ Ω_t(K2).»
- [Q R123] [OPT], R123's title: «σ̄_t is optimal at every vertex at once against σ_t»; classes and loud / quiet steps: «with
  class_t(v) := (Λ_t(v), E_t(v)), E_t(v) the e-vertices of Π_t(v), a step loud if some vertex changes class and quiet otherwise».
- [Q R122] [OPT] spelled out, R122's premise clause, which names it as the fleet's standing premise 1E-N3 of R57 (b): «an optimal
  counterstrategy being pointwise optimal (at every vertex its play value is ⊴ the value under every Odd strategy; RESULTS R57 (b),
  [1E-N3], as landed in R104)».
- [Q R126] QUIET-N: «every maximal window of quiet steps has at most N steps»; the Ξ-feedback number: «the minimum size of a set of
  movers meeting every cycle (self-loops count) of the Ξ-graph on the movers (an edge x → xt(x, j) for each option whose Ξ-target is
  a mover; options whose Ξ-target is X omitted)».
- Comparison only, not premises:
  - [Q R118] «no bound on R is claimed (OPEN)».
  - [Q R122] at k = 0: «the Howard run of IDEAL-CYC(G) from any mover state has C = 0, R = 0 and T_CYC ≤ N».
  - [Q R126] «it makes no new class of genomes on which T_CYC is polynomial, and at k = 1 it bounds the cycle nodes only (whether
    max_g min(D^tot(e_g), D^tot(β_g)) is polynomial in N + M at k = 1 is OPEN)».
- [VJ] as used (the reading of the landed packets P-N5-QN §1 and P-N5-XICYC §1; no script check): vertices are strictly ordered by
  relevance (priority, then index); reward(v) is v's rank in that order, taken negative if v's priority is odd. For a positional pair,
  Λ(v) is the most relevant vertex of the cycle of v's play; Π(v) is the set of vertices on the path from v to Λ(v), before Λ(v),
  that are more relevant than Λ(v); k(v) is the length of that path. (VJ-1) If Λ ≠ Λ′: (Λ, Π, k) ◁ (Λ′, Π′, k′) iff reward(Λ) <
  reward(Λ′). (VJ-2) If Λ = Λ′ and Π ≠ Π′, with z the most relevant vertex of Π Δ Π′: (Λ, Π, k) ◁ (Λ′, Π′, k′) iff (z ∈ Π′ and z has
  even priority) or (z ∈ Π and z has odd priority). The third component decides only when Λ = Λ′ and Π = Π′. ⊴ means ◁ or equal.
- Not used anywhere below: R126 GATE-CLASS (QUIET-N is used as landed); F2-F6; R118 (d) BR-SEG, (f) T-CYC; any bound on k(v).

## 2. Setting and notation
- G is any genome, with N movers and M options. Γ(G) has the N movers (Even, priority 0); for each option a gate g (Odd, priority 1)
  with its two faces e_g and β_g (Even); c_X, c_W, K0, K1, K3 (Even) and K2 (Odd). In IDEAL-CYC(G) every Even vertex other than a mover
  has one successor at every state: e_g → its W-target mover, or c_W; β_g → its Ξ-target mover xt(g), or u = K0; K0 → K3; K1 → K1;
  K3 → K2; c_X → c_X; c_W → c_W. The vertices with a choice are the movers (among their gates), the gates (between their two faces)
  and K2. The CORE is {K0, K1, K2, K3}. The number of Even vertices is N + 2M + 5.
- The run: states 0, …, T := T_CYC of IDEAL-CYC(G) as R118 (a) defines it. Ω_t(v) = (Λ_t(v), Π_t(v), k_t(v)) is the value of v under
  (σ_t, σ̄_t), σ̄_t Odd's optimal counterstrategy ([OPT]). s_t(v) := the successor of v on its play at state t. No proof below uses
  the movers' start choices, but the premises are quoted for the run of R118 (a), and nothing is claimed for other runs.
- E_t(v) := the e-vertices of Π_t(v); class_t(v) := (Λ_t(v), E_t(v)) (R123). D^tot(v) := the number of distinct classes of v over the run.
- ORDER ON CLASSES: (Λ, E) < (Λ′, E′) iff reward(Λ) < reward(Λ′), or Λ = Λ′ and E <lex E′ (the most relevant element of E Δ E′ lies in
  E′; R121's order). On the classes that occur it is a strict total order: by B-ONLY and its two exceptions the cycle nodes are
  β-vertices, K1, K2, c_X or c_W, of pairwise different priorities ([DEF]: 5, 3, 2, top, and «a distinct β-rank with a parity»), so
  different cycle nodes have different rewards; the lex order on finite sets of e-vertices is total.
- A step t → t + 1 is LOUD if some vertex changes class and QUIET otherwise (R123).
- The Ξ-graph: the movers, with an edge x → xt(x, j) for each option whose Ξ-target is a mover. k := the Ξ-feedback number (R126).
- Constants: P := 2M(N + 2M); A := M(N + 2M) + N.
- Symbols with two uses, told apart by context: k (the third component of a value; the Ξ-feedback number); R (a feedback vertex;
  R118's count of the steps at which σ̄ changes); u (K0, in [DEF]; the first state of an interval); s (a state, in §7; the map of
  (L4); s_t(v), the successor on the play); a, b (states; in (K4)'s proof the two faces of a gate); σ_b(x) is the gate of x at state
  b, and «(x, σ_b(x))», «xt(x, σ_b(x))» name that gate's option and its Ξ-target.

## 3. Five class facts (K1)-(K5) (PROVED, lane)
- **(K1) MONOTONE.** class_t(v) ≤ class_(t+1)(v) for every vertex v and every step t → t + 1.
  Proof. Λ moves only to a vertex of strictly larger reward (R118 (e)'s reason); while Λ is unchanged, E does not fall (E-MON). ∎
- **(K2) COARSE.** Let Θ = (Λ, Π, ·) and Θ′ = (Λ′, Π′, ·) be triples such that (Λ, Π) and (Λ′, Π′) are each the cycle node and the Π-set
  of the play of a vertex outside the core, at one state or at two states of the run. Put c := (Λ, E), c′ := (Λ′, E′), with E, E′ the
  e-vertices of Π, Π′. If Θ ⊴ Θ′ then c ≤ c′.
  Proof. If Λ ≠ Λ′: Θ ◁ Θ′, so reward(Λ) < reward(Λ′) by (VJ-1), and c < c′. Let Λ = Λ′. If E = E′ then c = c′. Otherwise let z_E be
  the most relevant element of E Δ E′ and z the most relevant vertex of Π Δ Π′. E Δ E′ ⊆ Π Δ Π′, so z is at least as relevant as z_E.
  Suppose z ≠ z_E. Then z is more relevant than the e-vertex z_E, so by E-DOM z is an e-vertex, c_W, K0 or K3. z is not an e-vertex
  (it would lie in E Δ E′ above z_E). z is not c_W: c_W's only out-edge is its self-loop, so on a play c_W is the cycle node, and a
  cycle node is in no set Π. z is not K0 or K3: a play from a vertex outside the core has cycle node K1 iff it enters the core; it
  then enters at K0 (D3) and runs K0 → K3 → K2 → K1 (frozen successors; σ̄(K2) = K1 by LOC-K2, at every state), so K0, K3 ∈ Π (both
  are more relevant than K1); and if its cycle node is not K1 it does not enter the core, so K0, K3 ∉ Π. As Λ = Λ′, K0 and K3 are in
  both of Π, Π′ or in neither. Hence z = z_E, an e-vertex, of even priority. Θ ≠ Θ′ and Θ ⊴ Θ′ give Θ ◁ Θ′; by (VJ-2) z ∈ Π′, i.e.
  z_E ∈ E′, i.e. E <lex E′: c < c′. ∎
  (PR-5, note N-a of REFEREE 32, applied: (K2) is stated for triples, not only for values of vertices; (K5) needs that form.)
- **(K3) ALONG THE PLAY.** At every state t: (a) Λ_t(v) = Λ_t(s_t(v)) for every vertex v; (b) no e-vertex lies on the cycle of a
  play; (c) class_t(v) = class_t(s_t(v)) for every vertex v that is not an e-vertex; (d) for an e-vertex e whose successor w is a
  mover: class_t(e) = (Λ_t(w), {e} ∪ E_t(w)) and e ∉ E_t(w), so class_t(e) > class_t(w); (e) the classes of K0, K1, K2, K3, c_W, c_X
  and of the e-vertices with successor c_W are the same at every state; an e-vertex with successor c_W has the class (c_W, ∅) of c_W,
  and (c_W, ∅) is the largest class that occurs.
  Proof. (a) v's play is v followed by s_t(v)'s play: the same cycle. (b) Let an e-vertex f lie on the cycle of a play at t. Its
  successor is not c_W (f's play would be f, c_W, c_W, …, and f would not be on its cycle). f is on the cycle of its own play, so
  Λ_t(f) is at least as relevant as f, against B-ONLY (f is not one of its excepted vertices). (c) If v ≠ Λ_t(v): the path from
  s_t(v) to the cycle node is the path from v without v, so Π_t(v) = Π_t(s_t(v)) ∪ ({v} if v is more relevant than Λ_t(v)), and
  E_t(v) = E_t(s_t(v)) because v is not an e-vertex. If v = Λ_t(v): Π_t(v) = ∅, and Π_t(s_t(v)) holds vertices of the cycle only, none
  of them an e-vertex (b): E_t(s_t(v)) = ∅ = E_t(v). (d) By B-ONLY Λ_t(e) is less relevant than e, so e ≠ Λ_t(e); e is not on the
  cycle (b), so e is on the path before Λ_t(e) and e ∈ Π_t(e); as in (c) Π_t(e) = Π_t(w) ∪ {e}; e ∉ Π_t(w), since by (b) the play
  from e passes e once. Same Λ and E_t(e) = E_t(w) ∪ {e} ⊋ E_t(w) give class_t(e) > class_t(w). (e) c_W and c_X are self-loops:
  classes (c_W, ∅), (c_X, ∅). An e-vertex with successor c_W: cycle node c_W, which is more relevant than every e-vertex ([DEF]), so
  Π = ∅. The core: K0 → K3 → K2 (frozen, R118 (a) with R104's start), K2 → K1 (LOC-K2), K1 → K1: cycle node K1 and no e-vertex on
  the way, class (K1, ∅) for all four. Largest: c_W has the largest reward among the cycle nodes that occur (β-vertices, K1, K2,
  c_X, c_W; [DEF]: top lies above every other priority outside K0, K3), and a play with cycle node c_W has Π = ∅ (only K0 and K3 are
  more relevant than c_W, and a play through them has cycle node K1). ∎
- **(K4) GATES.** class_t(g) = min(class_t(e_g), class_t(β_g)) for every gate g and state t, and the face σ̄_t(g) has that class.
  Proof. Let a := σ̄_t(g) and b the other face. Ω_t(a) ◁ Ω_t(b) (NO-TIE, then LOC-GATE). The faces are outside the core, so
  class_t(a) ≤ class_t(b) (K2). class_t(g) = class_t(a) (K3 (c)). ∎
- **(K5) HOWARD DOMINATES.** For every mover x, every step t → t + 1 and every gate y of x: class_(t+1)(x) ≥ class_t(y).
  Proof. DOM: Ω_(t+1)(x) ⊵ ext(x, Ω_t(y)). x has priority 0 and no cycle node has priority below 2 (CN2), so x is not more relevant
  than Λ_t(y) and ext(x, Ω_t(y)) = (Λ_t(y), Π_t(y), k_t(y) + 1): its cycle node and Π-set are those of the play of the gate y at
  state t. (K2), for that triple and the value of the mover x at state t + 1. ∎
- Remark (not needed). Outside the core (K1) also follows from F1 and (K2) (REFEREE 32, pre-read §2; L-RED-B, B1 §2.1).
- Lean (lane-level, on L-FORMAL's transcription Genome.lean / GenomeClass.lean, whose definitions the Lead accepted; never the proof
  of record): (K1), (K2), (K3), (K5) are also Lean-checked (lane) in box 208 §2's form ((K2) for the values of two vertices outside the
  core, not for triples; (K3 (e)) without the «largest class» clause): Genome.k1, Genome.k2, Genome.k3, Genome.k5, claude/l-formal
  f74d38a4 (its k5 goes through F1 and (K2), not DOM and CN2). (K4) is stated there (K4Statement) and NOT proved in Lean.

## 4. Lemma LEVEL (PROVED, lane)
Setting. States a ≤ b of the run; b is the REFERENCE state. For a ≤ t ≤ b:
- LAG_t := {v : class_t(v) ≠ class_b(v)}. By (K1), v ∈ LAG_t iff class_t(v) < class_b(v).
- If LAG_t ≠ ∅: m_t := min{class_t(v) : v ∈ LAG_t}; FRONT_t := {v ∈ LAG_t : class_t(v) = m_t}; Φ_t := (m_t, −|FRONT_t|), ordered
  lexicographically.
- A step t → t + 1 with t < b and LAG_t ≠ ∅ is a STALL if class_(t+1)(v) = class_t(v) for every v ∈ FRONT_t.
**Statement.** For every t < b with LAG_t ≠ ∅:
- (L1) LAG_(t+1) ⊆ LAG_t. If the step t → t + 1 is a stall: LAG_(t+1) ≠ ∅, FRONT_(t+1) = FRONT_t and Φ_(t+1) = Φ_t. If it is not a
  stall: LAG_(t+1) = ∅ or Φ_(t+1) > Φ_t.
- (L2) Every vertex of FRONT_t is a mover, a gate, or a β-vertex whose frozen successor is a mover.
- (L3) (α) Some mover z ∈ FRONT_t has σ_t(z) ∉ LAG_t, and then m_t = class_b(σ_t(z)); or (β) there is a play at t whose cycle
  consists of movers, their chosen gates and those gates' β-faces, all in FRONT_t, and then m_t = (c, ∅) for its cycle node c, a
  β-vertex.
- (L4) If the step t → t + 1 is a stall, there are r ≥ 1 and movers x_1, …, x_r with x_(i+1) = xt(x_i, σ_b(x_i)) for all i (indices
  mod r) such that for every i the mover x_i, its gate g_i := (x_i, σ_b(x_i)) and the β-face β_(g_i) lie in FRONT_t, and σ̄_t(g_i) =
  β_(g_i). In particular x_1 → x_2 → … → x_r → x_1 is a cycle of the Ξ-graph all of whose vertices lag at t.
- (L5) On [a, b] the potential Φ takes at most 2M·(N + 2M) = P values; at most M·(N + 2M) if case (α) of (L3) holds at every state.
**Proof.**
(L1) Let v ∈ LAG_(t+1). By (K1), class_t(v) ≤ class_(t+1)(v) < class_b(v): v ∈ LAG_t, and class_(t+1)(v) ≥ class_t(v) ≥ m_t. Hence
LAG_(t+1) ⊆ LAG_t; and if LAG_(t+1) ≠ ∅: (i) m_(t+1) ≥ m_t; (ii) if m_(t+1) = m_t then FRONT_(t+1) ⊆ FRONT_t (for v ∈ FRONT_(t+1):
v ∈ LAG_t and m_t ≤ class_t(v) ≤ class_(t+1)(v) = m_(t+1) = m_t, so class_t(v) = m_t).
- Stall: every v ∈ FRONT_t has class_(t+1)(v) = m_t < class_b(v), so v ∈ LAG_(t+1) with class m_t. Hence LAG_(t+1) ≠ ∅, m_(t+1) ≤ m_t,
  so m_(t+1) = m_t by (i), FRONT_(t+1) ⊇ FRONT_t, and equality by (ii): Φ_(t+1) = Φ_t.
- Not a stall: some v ∈ FRONT_t has class_(t+1)(v) > m_t (by (K1) a changed class is larger). If LAG_(t+1) = ∅ there is nothing to
  show. Otherwise, if m_(t+1) > m_t, Φ rises in its first coordinate; if m_(t+1) = m_t, then FRONT_(t+1) ⊆ FRONT_t by (ii) and v ∉
  FRONT_(t+1), because class_(t+1)(v) ≠ m_(t+1): |FRONT_(t+1)| < |FRONT_t| and Φ rises in its second coordinate. By (i) there is no
  third case.
(L2) K0, K1, K2, K3, c_W, c_X and the e-vertices with successor c_W never lag (K3 (e)). Let e be an e-vertex with a mover successor
w. If w ∉ LAG_t: class_t(e) = (Λ_t(w), {e} ∪ E_t(w)) = (Λ_b(w), {e} ∪ E_b(w)) = class_b(e) (K3 (d) at t and at b), so e ∉ LAG_t. If
w ∈ LAG_t: m_t ≤ class_t(w) < class_t(e) (K3 (d)), so e ∉ FRONT_t. A β-vertex whose frozen successor is u = K0 has the class of K0 at
every state (K3 (c), (e)) and never lags. What is left: movers, gates, β-vertices with a mover successor.
(L3) Take v ∈ FRONT_t and its play p_0 = v, p_1, p_2, … at t. class_t(p_(i+1)) ≤ class_t(p_i) for every i ((K3 (c)); (K3 (d)) for
an e-vertex with a mover successor; (K3 (e)) for an e-vertex with successor c_W, where the two classes are equal; note N-1 of L-RED-B).
So every p_i has class ≤ m_t; hence every p_i is non-lagging or lies in FRONT_t (a lagging vertex has class ≥ m_t). The cycle of the
play is K1's self-loop, c_W's self-loop, or a cycle without e-vertex (K3 (b)), without core vertex (a play that enters the core ends
in K1's loop) and without c_X (D4; v ≠ c_X by (L2)): a cycle of movers, gates and β-vertices, on which the kinds alternate as mover
→ chosen gate → β-face → mover.
- If every vertex of the cycle lags: it is not K1's or c_W's loop (K3 (e)); its vertices are all in FRONT_t; none is an e-vertex, so
  by (K3 (c)) they all have the class of the cycle node c, which is (c, ∅) (Π_t(c) = ∅). c is not a mover or a gate (CN2), so c is a
  β-vertex. This is (β).
- Otherwise some lagging vertex z of the play has a non-lagging successor y := s_t(z): if no vertex of the cycle lags, take the last
  lagging p_i (p_0 lags); if some but not all vertices of the cycle lag, go round the cycle. z ∈ FRONT_t. z is not a gate: then y is
  a face of z, and class_b(z) ≤ class_b(y) (K4 at b) = class_t(y) (y does not lag) = class_t(z) (K3 (c) at t); with (K1), class_b(z)
  = class_t(z), so z would not lag. z is not a β-vertex: y is its frozen successor at both states, so class_b(z) = class_b(y) =
  class_t(y) = class_t(z) (K3 (c)). z is not an e-vertex, a core vertex, c_W or c_X (L2). So z is a mover, y = σ_t(z) is a gate, and
  m_t = class_t(z) = class_t(y) = class_b(y). This is (α).
(L4) Let the step t → t + 1 be a stall. Define a map s on FRONT_t (its vertices are movers, gates and β-vertices with a mover
successor, (L2)):
- z a mover: s(z) := σ_b(z) =: w, a gate of z. class_b(w) = class_b(z) (K3 (c) at b) > m_t (z lags and class_t(z) = m_t). class_t(w)
  ≤ class_(t+1)(z) (K5) = class_t(z) = m_t (the stall; z ∈ FRONT_t). So class_t(w) < class_b(w): w lags at t, hence class_t(w) ≥ m_t,
  hence class_t(w) = m_t: w ∈ FRONT_t. (This is the only case that uses the stall.)
- g a gate: s(g) := σ̄_t(g) =: r, a face of g; class_t(r) = class_t(g) = m_t (K3 (c)). If r did not lag: class_b(g) ≤ class_b(r) (K4
  at b) = class_t(r) = m_t = class_t(g), so g would not lag (K1). So r lags, r ∈ FRONT_t, and by (L2) r is not e_g: r = β_g, i.e.
  σ̄_t(g) = β_g.
- β_g, with frozen successor a mover y = xt(g): s(β_g) := y. class_t(y) = class_t(β_g) = m_t and class_b(y) = class_b(β_g) ≠ m_t
  (K3 (c) at t and at b): y ∈ FRONT_t.
s maps the finite non-empty set FRONT_t into itself, so iterating s from any vertex reaches a cycle of s. On it the kinds alternate
mover x → gate (x, σ_b(x)) → its β-face → mover xt(x, σ_b(x)): the statement, with the movers of the cycle as x_1, …, x_r. Each
x_i → x_(i+1) is the Ξ-edge of the option σ_b(x_i) of x_i (for r = 1 a Ξ self-loop).
(L5) By (L3), m_t is the class at b of one of the M gates (case α) or (c, ∅) for one of the M β-vertices c (case β): at most 2M
values, at most M if (α) holds at every state. By (L2), 1 ≤ |FRONT_t| ≤ N + 2M. ∎
- Remark. b is any state of the run; with b = T the lagging vertices are those not yet at their final class.
- Lean (lane-level, never the proof of record): the bookkeeping of (L1) with (C1), (C2) of §5, for classes in any linear order that
  never fall, is also Lean-checked (lane): level_count, claude/l-formal f74d38a4. (L2)-(L5) on the genome are not formalized.

## 5. The counting (C1)-(C4) (PROVED, lane)
Fix a ≤ b, and let a = u_1 ≤ v_1 < u_2 ≤ v_2 < … < u_q ≤ v_q be the states of [a, b] with LAG ≠ ∅, grouped into the maximal intervals
[u_i, v_i] of constant Φ (u_(i+1) = v_i + 1; Φ takes each value on one interval, since it never falls). Let b′ := v_q + 1 if q ≥ 1 and
b′ := a otherwise: the first state with LAG = ∅ (LAG_b = ∅, and LAG only shrinks, (L1)).
- (C1) q ≤ P (L5); q ≤ M(N + 2M) if case (α) of (L3) holds at every state of [a, b′).
- (C2) The steps inside an interval [u_i, v_i] are stalls, and the steps v_i → u_(i+1) and v_q → b′ are not (L1). So the number of
  non-stall steps on [a, b′] is exactly q, and b′ − a = q + Σ_i (v_i − u_i).
- (C3) On an interval [u_i, v_i] with u_i < v_i (a PLATEAU) the front is one set J at all its states, every vertex of J keeps the
  class m there (L1), and J contains the movers x_1, …, x_r of a cycle of the Ξ-graph (L4 at u_i).
- (C4) For b′ ≤ t ≤ b every class equals its value at b ((K1): class_(b′) ≤ class_t ≤ class_b = class_(b′) pointwise). So the steps
  b′ → b′ + 1, …, b − 1 → b are quiet, they lie in one maximal window of quiet steps, and b − b′ ≤ N by QUIET-N.

## 6. Theorem WIN, Corollary R-INT, Theorems R-HEIGHT, K1-TCYC, FVS-TCYC (PROVED, lane; none uses §7)
**Theorem WIN.** Let G be any genome and S a set of movers that meets every cycle of the Ξ-graph (self-loops count; S = ∅ if the
Ξ-graph is acyclic). Let a ≤ b be states such that class_t(x) = class_b(x) for every x ∈ S and every a ≤ t ≤ b. With reference b and
b′ as in §5:
(i) no step t → t + 1 with a ≤ t < b′ is a stall: each changes the class of a vertex of FRONT_t, so it is loud;
(ii) case (α) of (L3) holds at every state of [a, b′), and b′ − a ≤ M(N + 2M);
(iii) the steps after b′ are quiet and b − b′ ≤ N.
Hence b − a ≤ M(N + 2M) + N = A.
Proof. No vertex of S lags at any t ∈ [a, b]. (i) At a stall, (L4) gives a cycle of the Ξ-graph all of whose vertices lag; S meets
it: contradiction. (ii) In case (β) the movers of the play cycle form a cycle of the Ξ-graph (mover → chosen gate → β-face → its
Ξ-target), all lagging: the same contradiction; so (α) holds, and by (C1) q ≤ M(N + 2M). By (i) and (C2) every interval [u_i, v_i]
is a single state: b′ − a = q. (iii) is (C4). ∎
**Corollary R-INT.** Let G have Ξ-feedback number 1 and let R be a feedback vertex (a mover on every cycle of the Ξ-graph). For every
maximal interval [a, b] of states of constant class(R): b − a ≤ A; at most M(N + 2M) of its steps are loud, and they come first.
Proof. Theorem WIN with S = {R}. ∎
**Theorem R-HEIGHT.** Let G have Ξ-feedback number 1 and R a feedback vertex. Then class(R) changes at at most P steps: D^tot(R) ≤ P + 1.
Proof. Reference b := T, a := 0. Let class(R) change at the step t → t + 1. Then R ∈ LAG_t (K1). If the step were a stall, (L4)
would give a cycle of the Ξ-graph inside FRONT_t; R is on it, so R ∈ FRONT_t, and at a stall no vertex of FRONT_t changes class:
contradiction. So the step is one of the q ≤ P non-stall steps (C1), (C2). By (K1) the classes of R at different times of change are
different, so D^tot(R) = 1 + (the number of such steps). ∎
**Theorem K1-TCYC.** For every genome with Ξ-feedback number 1: T_CYC ≤ P·(A + 1) + N.
Proof. Reference b := T, a := 0, R a feedback vertex. By (C2), b′ = q + Σ_i (v_i − u_i). For a plateau [u_i, v_i], (C3) gives a cycle
of the Ξ-graph inside J; R is on it; so class(R) is the same at all states of [u_i, v_i], and Theorem WIN with S = {R} on that
interval (as its own [a, b]) gives v_i − u_i ≤ A. So b′ ≤ q(A + 1) ≤ P(A + 1) (C1), and T − b′ ≤ N (C4). ∎
**Theorem FVS-TCYC.** For every genome with Ξ-feedback number k: T_CYC ≤ (P + N)·(P + 1)^k.
Proof. Fix a set F_0 of k movers meeting every cycle of the Ξ-graph. For S ⊆ F_0 let W(S) be the largest b − a over the intervals
[a, b] on which every vertex of S keeps its class, and w_j := max{W(S) : |S| = j}. By Theorem WIN, w_k = W(F_0) ≤ A ≤ P + N. Let
S ≠ F_0 and [a, b] such an interval; reference b. For a plateau [u_i, v_i], (C3) gives a cycle of the Ξ-graph inside J; F_0 meets it
in some x; x lags, so x ∉ S (the vertices of S do not lag); every vertex of S ∪ {x} keeps its class on [u_i, v_i]: v_i − u_i ≤
W(S ∪ {x}) ≤ w_(|S|+1). By (C1), (C2) and (C4): b − a ≤ q(w_(|S|+1) + 1) + N ≤ P(w_(|S|+1) + 1) + N. So w_j ≤ P(w_(j+1) + 1) + N for
j < k. By downward induction w_j ≤ (P + N)(P + 1)^(k−j): for j = k it is w_k ≤ P + N; and with X := (P + N)(P + 1)^(k−j−1) ≥ P + N,
P(X + 1) + N = PX + (P + N) ≤ PX + X = X(P + 1). T_CYC = W(∅) = w_0. ∎
- What FVS-TCYC is not: a bound polynomial in N + M for all genomes. Its exponent grows with k, and k can be of order N.
- Check against k = 0: Theorem WIN with S = ∅ gives T_CYC ≤ M(N + 2M) + N for Ξ-acyclic genomes, weaker than landed R122's T_CYC ≤ N
  (§1). Consistent; not new.

## 7. Lemma PLATEAU (PROVED, lane)
**Statement.** For every genome, every reference state b and every maximal interval [u, v] of states of constant Φ (reference b):
v − u ≤ N + 2M + 5.
**Proof.** Let [u, v] be such an interval with u < v, Φ = (m, −|J|) on it, J := FRONT_u. By (L1) every step inside is a stall,
FRONT_s = J and class_s(x) = m for x ∈ J, at every state s ∈ [u, v]; and v < b, since LAG_v ≠ ∅. Put Y := {x : class_u(x) ≤ m}.
(P1) For every s ∈ [u, v]: {x : class_s(x) ≤ m} = Y, and class_s(x) = class_u(x) for x ∈ Y.
  A vertex of Y lags at u or not. If it lags, its class is ≥ m (it lags) and ≤ m (it is in Y), so it is in J and has class m at
  every s. If it does not lag, its class at u is its class at b, and by (K1) at every state from u to b. A vertex outside Y has class
  > m at u, and by (K1) at s.
(P2) Y is closed under plays: for x ∈ Y and s ∈ [u, v], s_s(x) ∈ Y.
  class_s(s_s(x)) ≤ class_s(x) ≤ m ((K3 (c), (d), (e)), as in (L3)); (P1).
(P3) For every mover x ∈ Y, every gate y of x and every s ∈ [u, v]: class_s(y) ≤ class_s(x); so every gate of a mover of Y is in Y.
  For s < v: class_s(y) ≤ class_(s+1)(x) (K5) = class_s(x) (P1). So y ∈ Y (P1; such an s exists since u < v), its class is constant
  on [u, v] (P1), and the inequality holds at s = v too.
(P4) For every gate g ∈ Y: σ̄_s(g) is the same face for all s ∈ [u, v], and it lies in Y. If K2 ∈ Y: σ̄_s(K2) = K1 at every s (LOC-K2).
  The chosen face has the class of g (K4), so it is in Y (P1). Three cases.
  (1) One face is outside Y. By (P1) it is outside Y at every s, with class > m ≥ class_s(g), so it is never the chosen face (K4);
  the chosen face is the other one at every s.
  (2) Both faces are in Y, with different classes. The classes are constant on [u, v] (P1), and at every s the chosen face is the one
  of lower class (K4).
  (3) Both faces are in Y, with equal classes (at one state, hence by (P1) at every state of [u, v]). The successor of e_g is not
  c_W: then class_s(e_g) = (c_W, ∅), the largest class (K3 (e)), which is above the lagging class m, and e_g would not be in Y. So it
  is a mover w, and e_g ∈ E_s(e_g) = E_s(β_g) (K3 (d)). So the play of β_g at s passes e_g; it enters e_g by its only in-edge, from g
  (D1): it passes g and leaves g by e_g. So σ̄_s(g) = e_g at every s.
(P5) The game H. Vertices: Y. A mover of Y keeps all its gates (in Y by (P3)). Every other vertex x of Y keeps the single successor
  s_u(x) (in Y by (P2)): for a gate its face σ̄_u(g); for K2, K1; for a β- or e-vertex, K0, K1, K3 or c_X, its frozen successor. By
  (P4), LOC-K2 and the freeze, s_s(x) = s_u(x) for every such x and every s ∈ [u, v]. H is a parity game (owners and priorities
  inherited; every vertex has a successor in Y) in which only the movers of Y have a choice. The order of relevance and the
  parities of H's vertices are those of Γ(G), so the VJ order on the values of plays inside Y is the same in H and in Γ(G).
  For s ∈ [u, v] and x ∈ Y the play of x under (σ_s, σ̄_s) stays in Y (P2) and uses H's edges, so Ω_s(x) is the value of x in H
  under σ_s restricted to Y; Odd has one strategy in H, which is therefore its optimal counterstrategy. For u ≤ s < v the step s →
  s + 1 of IDEAL-CYC at a mover of Y compares the values Ω_s of its gates, which are its successors in H with their values in H, by
  the rule «⊴-best successor, the current one kept if it is one»; that setting leaves the choice among several ⊴-best non-current
  successors free, so the run's own choice is allowed. H's Howard step is the step at EVERY Even vertex of H (BR-SEG-G's setting, §1): the movers of Y do exactly this, and every other Even vertex of H has one successor, so its step is trivial. Hence
  σ_u, σ_(u+1), …, σ_v, restricted to Y, are consecutive states of a Howard run of H in the sense of BR-SEG-G's setting, as long as
  each step changes the strategy (a Howard run ends at the first state at which no Even vertex has a strictly better successor).
(P6) Every step s → s + 1 with u ≤ s ≤ v changes σ at some mover of Y. (Only u ≤ s < v is used in (P7).)
  Suppose not, for some s. Claim: for every s′ with s ≤ s′ ≤ b: (A) σ_(s′) = σ_s on the movers of Y, and (B) Ω_(s′) = Ω_s on Y.
  Induction on s′; s′ = s is trivial. Let the claim hold for some s′ < b.
  (A) at s′ + 1. Let x be a mover of Y. Its gates are in Y (P3) and have at s′ the values of state s (B); its current gate is
  σ_(s′)(x) = σ_s(x) (A). At the step s → s + 1, x kept σ_s(x), so by the rule of R118 (a) σ_s(x) was a ⊴-largest gate of x under
  Ω_s; it is one under Ω_(s′), and by the same rule x keeps it at the step s′ → s′ + 1.
  (B) at s′ + 1. Let Odd answer σ_(s′+1) by σ̄_s, the counterstrategy of the state s of the plateau. For x ∈ Y the play from x
  under (σ_s, σ̄_s) stays in Y ((P2) at s ∈ [u, v]); σ_(s′+1) = σ_s on the movers of Y ((A) at s′ + 1) and the other Even vertices
  are frozen; so the play from x under (σ_(s′+1), σ̄_s) is that same play, of value Ω_s(x). By [OPT] at state s′ + 1 (the value under
  σ̄_(s′+1) is ⊴ the value under every Odd strategy): Ω_(s′+1)(x) ⊴ Ω_s(x). By F1 and (B) at s′: Ω_(s′+1)(x) ⊵ Ω_(s′)(x) = Ω_s(x).
  So Ω_(s′+1)(x) = Ω_s(x).
  At s′ = b the claim gives class_b(x) = class_s(x) = m for x ∈ J ⊆ Y: the vertices of J do not lag at s. Contradiction with J =
  FRONT_s ⊆ LAG_s.
  (PR-1 applied: the induction answers by σ̄_s and uses [OPT], then F1. The step «Odd answers by σ̄_s, the plateau state's
  counterstrategy» is referee-originated: REFEREE 32's repair of gap G-P6, claude/referee 7524342b, R-box208-preread.md §5.2. The
  same gap was found independently by L-RED-B as G-1, claude/l-red-b 0510c800, B1-box208.md §2.5, with a second repair, and in this
  lane's own re-reading, box 208 Addendum B1 (1). Details in §10.)
(P7) By (P5) and (P6) the steps u → u + 1, …, v − 1 → v are v − u consecutive steps of a Howard run of H. Each changes no cycle
  node of a vertex of H ((P1): the class contains Λ) and no choice of Odd (Odd has none in H): in R118's labels they are p-steps, so
  they lie in one maximal run of p-steps of that run. H0 holds for every step of every Howard run of H: a step switches some Even
  vertex with a choice, that is, a mover of Y; and a mover is not the cycle node of its play under any positional pair of H (such a
  pair extends to a positional pair of IDEAL-CYC(G) with the same plays from Y, because Y is closed in H; CN2). By landed R118 (i)
  BR-SEG-G (a), applied to the parity game H: v − u ≤ n_E(H) ≤ the number of Even vertices of Γ(G) = N + 2M + 5. ∎
  (PR-2 applied: (P7) cites exactly one proof of record, landed R118 (i) BR-SEG-G (a), with H0 checked above. The same step is also
  Lean-checked (lane): brsegG, and in the abstract one-player form of (P5) + (P7) with (P1)-(P4), (P6) as hypotheses: plateau,
  claude/l-formal f74d38a4. Neither Lean theorem is used as a premise.)

## 8. Theorem ALL-TCYC (PROVED, lane); what it supersedes; remark SHARP (not to sign)
**Theorem ALL-TCYC.** For every genome G: T_CYC ≤ P·(N + 2M + 6) + N, P = 2M(N + 2M).
Proof. Reference b := T, a := 0. By (C2), b′ = q + Σ_i (v_i − u_i), with q ≤ P (C1) and v_i − u_i ≤ N + 2M + 5 (PLATEAU). By (C4),
T − b′ ≤ N. So T_CYC ≤ P + P(N + 2M + 5) + N. ∎
- Consequences (to sign with the theorem), each a count of steps of the run: the number R of steps at which σ̄ changes, the number Q of loud steps and
  D^tot(v) − 1 for every vertex v are at most P(N + 2M + 6) + N.
- Against K1-TCYC and FVS-TCYC (arithmetic remark, not to sign; N ≤ M, every mover having an option). A + 1 ≤ N + 2M + 6 iff M(N + 2M) ≤ 2M + 5, which fails for
  M ≥ 2: for M = 2, M(N + 2M) ≥ 2·5 = 10 > 9; for M ≥ 3, M(N + 2M) > 2M² ≥ 6M > 2M + 5. So for M ≥ 2 ALL-TCYC's value is below
  K1-TCYC's. (P + N)(P + 1) ≥ P(N + 2M + 6) + N iff P ≥ 2M + 5, which holds for M ≥ 2 (P ≥ 4·5 = 20 for M = 2; P > 4M² > 2M + 5 for
  M ≥ 3). So for M ≥ 2 and k ≥ 1 ALL-TCYC's value is at most FVS-TCYC's. For M = 1 (then N = 1, P = 6, A = 4) the values are 55
  (ALL-TCYC), 31 (K1-TCYC) and 49 (FVS-TCYC at k = 1).
- Remark SHARP (NOT a statement of this packet; not to sign; credit L-RED 66). L-RED 66 (claude/l-red 2d2969c2, R235-box208.md §5,
  «second route») derives v − u ≤ the number of movers of Y ≤ N on every plateau from the lane lemma LAM-GAP (L-SI 51's proof, checked
  by L-RED 66) in L-RED 66's sharp form SHARP, which would give T_CYC ≤ P(N + 1) + N. REFEREE 32 (pre-read §5.3, note N-b) and L-RED-B (B1 §2.5, note N-2) point to the same bound through
  BR-SEG's own count of movers on a path. Landed BR-SEG (R118 (d)) is stated for IDEAL-CYC(G), not for the sub-game H, and LAM-GAP /
  SHARP and the Lean theorems brseg and lam_gap_sharp are lane-level, so the sharper constant is not proved from landed premises
  here and is not claimed. (PR-5, note N-b: applied as this remark only.) DATA agrees with it and does not prove it: no plateau of
  §11's plat208 and rv208 sets is longer than the number of movers of its Y (the level208 sets do not count the movers of Y).

## 9. The genome-only steps, and Friedmann's G_N (READING and DATA; not to sign)
Howard's rule with VJ values is not polynomial on parity games in general, so an argument of this kind must use a property of the
genome games at some step. The steps that use one, each with the landed fact it rests on:
- (K2) COARSE and (K3 (b), (d)): from B-ONLY (R123) and E-DOM (R121, a [DEF] fact). Above the β-level, the part of Π that can decide
  the value order consists of e-vertices only; they are even, never on a cycle, and each adds itself to the class of its successor.
  This makes the class a monotone image of the value that is constant along a play except at an e-vertex, where it rises. (K4) and
  (K5) rest on (K2); Lemma LEVEL and everything after it rest on (K3), (K4) and (K5).
- (K1): from E-MON (R121) and R118 (e)'s reason, both statements about IDEAL-CYC(G). (K4): from NO-TIE and LOC-GATE (R123), then (K2).
- (K5): from DOM (R118 (c)), which needs that the movers have priority 0 and are never cycle nodes (CN2), and then (K2).
- QUIET-N (R126), in (C4), hence in WIN (iii), R-INT, K1-TCYC, FVS-TCYC and ALL-TCYC: Odd does not move while every class stands
  still. It is a genome statement (R126 proves it from GATE-CLASS).
- (P4): Odd's choice at a gate of Y is constant on a plateau. Cases (1), (2) are (K4); case (3) is decided by (D1), «e_g's only
  in-edge is from g», with (K3 (d), (e)).
- (L2), (L4): the only Odd vertices with a choice are the gates, each with one e-face and one β-face, and K2, whose choice is
  constant (LOC-K2).
DATA, Friedmann's game (L-COMP 19 BOX 43, claude/l-comp a6cce717, experiments/comp/box43/README.md item 1 (b), sha1 db74c1555ed9…;
cited, not re-run in this lane; L-COMP's own lift of the statements to a plain parity game: «movers» := Even vertices with ≥ 2
successors, «gates» := Odd vertices with ≥ 2 successors, «e-vertices» := for each gate its successor of largest even priority,
class := (reward(Λ), Π ∩ those)). Counter k5 (unit: (mover, successor, step) with class_(t+1)(mover) < class_t(successor); set: G_N
for N = 1, …, 8, Howard from the start ι, in L-COMP's own transcription of the game as quoted in L-LIT T66 §3 (checked there equal
to L-LIT's), two engines agreeing; scope: every Even vertex with a choice):
- G_1: all of L-COMP's 23 counters are 0. G_2: k5 = 38; the first failure is at the step 5 → 6, at the mover g2 and its successor
  f2. There the most relevant vertex of the difference of the two Π-sets is f2, of ODD priority, above the escape vertex h1: an odd
  vertex above an e-vertex, which E-DOM excludes on Γ(G). DOM itself holds in values at every failure (L-COMP's counter domfail 0).
  So on G_2 the step that fails is (K2) inside (K5), and the missing genome property is E-DOM.
- On G_1, …, G_8 (DATA on eight instances, not a statement about all N; L43): the run length is 8, 26, 62, 134, 278, 566, 1,142,
  2,294; the number of values of Φ is 3, 8, 15, 24, 35, 48, 63, 80; the longest plateau is 2, 7, 16, 34, 70, 142, 286, 574; counters
  of (K1), (K3), (K4), (L1), (L2), (L3), (C2), (C4), (P1), (P2), (P4) are 0, and those of (K5), (L4), (P3), (P6), (P7) fire from G_2
  on. READING (L-COMP's, not a checked statement): under that lift the potential moves few times and the run length sits in the
  plateaus, where (P3) fails through (K5). (REFEREE 32's pre-read §7 gives a different reading, with class := Λ: the run length sits
  in plateaus in which Odd moves, the place of QUIET-N and (P4).)
- The same DATA is the reason for the scope line: nothing here is about Howard's rule on games that are not genome games.

## 10. Referee and adversary items, and where each is applied (L41: every referee- or adversary-originated step is named)
- PR-1 (REFEREE 32, required): (P6)'s induction via σ̄_s and [OPT], then F1. APPLIED in §7 (P6), step (B). Origin of the step, under
  L41: the gap in box 208's wording of (P6) (ii) («the play of state s′ stays in Y» was used for states s′ after the plateau, where
  (P2) is not available) was found by REFEREE 32 as G-P6 (claude/referee 7524342b, docs/referee/R-box208-preread.md §5.2, sha1
  7c350c4d8d56…), with the repair used here; independently by L-RED-B as G-1 (claude/l-red-b 0510c800, docs/red-b/B1-box208.md §2.5,
  sha1 57fc936fadd8…), whose repair is different (σ̄_(s′) = σ̄_s on the gates of Y, from F3, CN2 and NO-TIE) and is not used here;
  and in this lane (box 208 Addendum B1 (1), l-new 3f896099), whose repair (a) is the sentence REFEREE 32 gives. L-RED 66 read the
  same sentence as correct and wrote it out through (K1) (claude/l-red 2d2969c2, docs/red/R235-box208.md §5, sha1 d268748689e8…),
  which is Addendum B1 (1)'s repair (b); not used here. The step in the packet is credited to REFEREE 32.
- PR-2 (REFEREE 32, required): APPLIED in §7 (P7): one proof of record (landed R118 (i) BR-SEG-G (a), H0 checked); the sentence
  «H's Howard step is the step at EVERY Even vertex of H» is in (P5).
- PR-3 (REFEREE 32, required): APPLIED in «To sign» and §1: premises by landed R-id; (D1), (D3), (D4) quoted from R126's packet; no
  lane lemma.
- PR-4 (REFEREE 32, required): APPLIED in §11: each DATA clause names unit, set, scope and counter as the tools compute them, and
  says that no run tests the constants.
- PR-5 (REFEREE 32, optional): N-a («triples») APPLIED in §3 (K2), (K5); N-b (plateau ≤ movers of Y) recorded as remark SHARP in §8,
  not claimed.
- PR-6 (the Lead's call): one packet; K1-TCYC and FVS-TCYC kept in «To sign» (Lead 17:52Z).
- L-RED-B's note N-1 ((L3)'s first sentence and the e-vertices with successor c_W): APPLIED in §4 (L3) and §7 (P2) through (K3 (e)).
- L-RED-B's remark that PLATEAU needs (P6) only for u ≤ s < v: APPLIED in §7 (P6), (P7).
- L-RED-B's remark on H's value order (the restriction of Γ(G)'s) and REFEREE 32's bridge B-1: APPLIED in §7 (P5).
- Box 208 Addendum B1 (2)-(4) (the keep-if-best rule spelled out in (P6); «a» Howard run of H for any choice among several best
  gates; (K2) for triples): APPLIED in §7 (P6) (A), §7 (P5), §3.
- Statements that say more than box 208's text, each proved in place: (K3 (e)) adds «(c_W, ∅) is the largest class that occurs» (box
  208 has it inside A2 (P4)); (K4) adds that the face σ̄_t(g) has the class of g; (P4)'s statement carries the clause on K2. Statements
  that say less: R-INT is given without box 207's count λ(W).
- L43: this packet has no DEAD row. Every sentence about growth on finitely many instances is DATA with its counter (§9, §11).

## 11. DATA (not to sign; tools and frozen outputs in experiments/new/box208/, pinned in experiments/new/box211/level.pins)
What the DATA tests and what it does not: it tests the class facts and the steps of the proofs state by state. NO RUN TESTS THE
CONSTANTS: the largest number of values of Φ in any run of these sets is 199 (MW32_2, where P = 2,120,796), the longest plateau has
26 steps, and T_CYC ≤ 199 on every frozen genome of these sets. Large zero counts are DATA, not evidence of the theorems.
Scope of every row except the three level208_g3_* rows: IDEAL-CYC from the genome's start, every vertex of Γ(G). Tables generated by box208/summ208.py and summ208c.py
from the frozen outputs (no number typed by hand); «0» in a must-0 column means that every counter of that tool is 0 on every row.
- level208.py (engine: box203 gfc203.hist_ideal over box191 idealcyc and experiments/si/si.py's VJ engine; reference b = T, and for
  the window counters the last state of each interval). Counters, each must-0, units as in the tool's header: monofail (K1; unit (vertex,
  step)), k3fail (K3; unit (vertex, state)), k4fail (K4; unit (Odd vertex with two successors, state)), k5fail (K5; unit (mover,
  successor, step)); einF (L2), l3fail (L3), phifail (L1), stallnocyc (L4) (unit: states t < b with a lagging vertex); nofvs (unit:
  stalls whose cycle misses the feedback set found; k ≤ 3 only); rstall (unit: steps, k = 1; R-HEIGHT); boundfail (unit: genomes;
  more than P values of Φ, or at k = 1 T_CYC above P(A + 1) + N); for every maximal interval of constant classes of S (k = 1: every
  single feedback vertex in turn; 2 ≤ k ≤ 3: one minimum feedback set; k = 0: the empty set; k ≥ 4: not run): winstall (unit: steps),
  wbeta, wl3fail (unit: states), wmid, wbound (unit: intervals).
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
  Sets: level208_records.out, the 25 frozen k = 1 genomes of boxes 202-207; level208_corpus.out, the 53 genomes of box202/inst (the
  window counters for the 28 genomes with k ≤ 3 only); level208_rand_*.out, random genomes (2,000 of shape k1, seed 2081; 500 of each
  of six eg195 shapes, seed 2082); mut208_*.out, 250 mutants of each of eight frozen k = 1 genomes (seed 2086). The rows
  level208_g3_*.out are the same counters on the N5′-xi run on Γ3(G): DATA only, no statement of this packet is about Γ3. Controls:
  LV_CTRL=1 (S := one mover that is not a feedback vertex) fires on two of the four genomes tried and on a random set; LV_CTRL=2
  (FRONT := the HIGHEST lagging class) fires on all three genomes tried.
- The same counters on a second engine (ownhist208.py: the run of L-RED 54's own IDEAL-CYC implementation, claude/l-red 72e2c5dc,
  experiments/red/r221q/own.py, read by git show, fed to level208.py --hist). A second ENGINE under the same counter code:
| set (file in out/) | rows | sum of the 16 must-0 counters | descriptive |
| --- | --- | --- | --- |
| own208_records.out | 25 genomes | 0 | max T 114, stalls 31 (loud 0), plateaus 14 (longest 9), intervals 556 (longest loud prefix 91); T differs from this lane's engine on 0 genomes |
| own208_corpus.out | 53 genomes | 0 | max T 199, stalls 48 (loud 23), plateaus 15 (longest 13), intervals 615 (longest loud prefix 53); T differs from this lane's engine on 0 genomes |
- plat208.py, PLATEAU (reference b = T; over every plateau [u, v], u < v). Counters, each must-0: p1 (P1; unit (vertex, state)),
  pclos (P2; unit (vertex of Y, state)), p2 (P3; unit (mover of Y, gate, state)), p3 (P4; unit (Odd vertex of Y, step)), p4 (P6; unit
  steps s → s + 1, u ≤ s ≤ v, at which no mover of Y switches), p5 (P7; unit plateaus with v − u above the number of Even vertices
  of Y). Control PL_CTRL=1 (Y := the front alone) fires.
| set (file in out/) | genomes | sum of p1, pclos, p2, p3, p4, p5 | descriptive |
| --- | --- | --- | --- |
| plat208_corpus.out | 53 | 0 | plateaus 15, longest 13 steps, largest 100·(v − u)/(movers of Y + 1) = 14 |
| plat208_ctrl1.out | 3 | CONTROL fires: pclos 210, p5 1 | plateaus 5, longest 13 steps, largest 100·(v − u)/(movers of Y + 1) = 433 |
| plat208_mut2_s2093.out | 600 | 0 | plateaus 302, longest 25 steps, largest 100·(v − u)/(movers of Y + 1) = 51 |
| plat208_mut_s2092.out | 600 | 0 | plateaus 846, longest 15 steps, largest 100·(v − u)/(movers of Y + 1) = 20 |
| plat208_rand_s2091.out | 3600 | 0 | plateaus 546, longest 4 steps, largest 100·(v − u)/(movers of Y + 1) = 57 |
| plat208_records.out | 25 | 0 | plateaus 14, longest 9 steps, largest 100·(v − u)/(movers of Y + 1) = 18 |
- rv208.py, a third implementation with its own builder of Γ(G), valuation, Odd reply, Howard run and 49 must-0 counters (premises
  re-tested: CN2, B-ONLY, NO-TIE, LOC-GATE, LOC-K2, F1, DOM; (K1)-(K5); (L1)-(L5); (C4); (P1)-(P7) with H built and valued on its
  own), for EVERY reference state b = 1, …, T. Units: pairs (b, t) with a lagging vertex for the LEVEL counters, (b, plateau) for the
  PLATEAU counters. Control RV_CTRL=1 fires. rv208_xcheck.out compares its builder, run and values with box191 idealcyc / si.Engine.
| set (file in out/) | lines | genomes | sum of the 49 must-0 counters | VIOLATION lines | descriptive |
| --- | --- | --- | --- | --- | --- |
| rv208_ctrl1.out | 2 | 2 | CONTROL fires: L1rise 1, L1stall 29, L2 50, L3 50, L4beta 44, L4gate_face 21, L4mover 4, L4nocycle 47, P1 1267, P3 20, P4 24, P5howard 57, P5val 316 | 0 | max T 30, sum T 54, (b, t) pairs with a lagging vertex 54, stalls 47, non-stalls 7, case (β) only 0, plateaus 2 (longest 15; longer than the movers of Y: 0), equal-class gates met 16, (K2) pairs 8000 |
| rv208_frozen.out | 81 | 81 | 0 | 0 | max T 199, sum T 2707, (b, t) pairs with a lagging vertex 93856, stalls 1247, non-stalls 92609, case (β) only 623, plateaus 538 (longest 13; longer than the movers of Y: 0), equal-class gates met 187, (K2) pairs 321444 |
| rv208_mut_s2094.out | 8 | 480 | 0 | 0 | max T 33, sum T 10148, (b, t) pairs with a lagging vertex 115116, stalls 16734, non-stalls 98382, case (β) only 1740, plateaus 6787 (longest 26; longer than the movers of Y: 0), equal-class gates met 1664, (K2) pairs 1920000 |
| rv208_rand_s2095.out | 3 | 3300 | 0 | 0 | max T 11, sum T 5405, (b, t) pairs with a lagging vertex 9041, stalls 368, non-stalls 8673, case (β) only 5337, plateaus 311 (longest 4; longer than the movers of Y: 0), equal-class gates met 6, (K2) pairs 9314030 |
| rv208_xcheck.out | 81 | 81 | builder, run length, states and values equal to box191 idealcyc / si.Engine on 81 of 81 files | | max T 199 |
  rv208_frozen.out: the 25 + 53 genomes above and the three genomes of landed R118 (m) (DEAD_SEG2P_d4_N8, _d7_N14, _d9_N18).
- Independent replays by other lanes and a referee are in §12; their numbers are theirs, in their own pinned outputs.

## 12. Attack and check record (cited by commit and file sha1; not re-run here)
Object of the first four: claude/l-new 8db300fe, docs/new/N5-LEVEL-box208.md, sha1 55e6538110d3… (box 208 body + Addendum A, before
Addendum B). None of the entries below is a signature.
- L-RED 66, R235 (claude/l-red 2d2969c2, docs/red/R235-box208.md): every statement SURVIVES; own engine (r221q/own.py) and a fresh
  counter (lv235.py), 0 failures on box 208's 53-genome corpus with the same descriptive numbers; mutant climbs (N ≤ 56) with 0
  failures; the second route of §8's remark.
- L-RED-B, B1 (claude/l-red-b 0510c800, docs/red-b/B1-box208.md; INTERIM by its own heading): every statement SURVIVES with gap G-1
  in the write-up of (P6); own engine and 27 must-0 counters, 0 violations on about 8.1 million runs (every reference state on its
  exhaustive, random and tie-branch sets, reference T on its mutants), among them every genome of the eight tiers (N, M) = (1, 1),
  (1, 2), (2, 2), (1, 3), (2, 3), (3, 3), (1, 4), (2, 4) and every tie-breaking branch on 4,500 small genomes; its runs are short (T ≤ 199).
- REFEREE 32, pre-read (claude/referee 7524342b, docs/referee/R-box208-preread.md; «NOT A SIGNATURE»): no gap found except G-P6;
  own replay with 36 must-be-0 counters, all 0; its §9 lists PR-1..PR-6.
- L-COMP 19, BOX 43 (claude/l-comp a6cce717, experiments/comp/box43/README.md): this lane's counters on its own engine give the same
  lines as this lane's two engines on the 78 frozen genomes; its own 23 counters are 0 on 137 runs, 3,300 random genomes and 1,350
  mutants; item 1 (b) is §9's DATA on G_N.
- L-FORMAL (claude/l-formal f74d38a4, lean/lemmas/INDEX.md and README.md; lane-level, «Lean-checked (lane)», a result only through
  CHECKER; its object is box 208 §1-§4 and Addendum A2 as its INDEX names them): on its transcription of the genome, CN2, B-ONLY,
  E-DOM, and (K1), (K2), (K3), (K5) in box 208 §2's form; abstractly, the counting of §4-§5 (level_count) and (P5) + (P7) (plateau);
  BR-SEG-G (brsegG). (K4) is stated and not proved. NO-TIE, LOC-GATE, (L2)-(L5), (P1)-(P4), (P6), QUIET-N and ALL-TCYC are NOT
  formalized.
- This lane (history): one fresh-context reviewer agent started by successor 72 (box 208 Addendum B1, B2, B4) and one proofreading
  agent started by successor 73 on this packet's draft before the freeze. Neither is a referee; no signature, no label changed.

## 13. TARGET.md diff and scope
- [Q TARGET] TARGET.md §2 (M4), verbatim: «There is a deterministic algorithm A and a polynomial p such that for every parity game G, A on input
  G halts within p(n + m) steps and outputs the pair (W_E(G), W_O(G)).» This packet has no algorithm A for parity games: it counts
  the steps of an improvement rule in the model IDEAL-CYC, on the games Γ(G) only. Not M4.
- [Q TARGET] TARGET.md §4, verbatim, first bullet of what does not count as M4: «Polynomial only on a restricted class (bounded d, treewidth,
  Strahler/register number, ...).» The genome games are a restricted class. §4 adds that such a result may count as M3 if new
  against the literature map, and §7e asks that an M3 result be stated in TARGET.md's vocabulary and checked for novelty by L-LIT
  before proof work starts. Neither has been done for this packet: it is not presented as M3, and no novelty is claimed.
- Not a gauntlet step-4 pass (TARGET.md §5): step 4 is about the candidate algorithm N5, on every parity game. G-N5-TIME stays OPEN.
  N5′-xi stays a CANDIDATE (D1), and by L-SI 52's lane Lemma WRAP (unrefereed) it would replay Howard's rule on every parity game.
- What a signed ALL-TCYC would change in the landed record: R118's «no bound on R is claimed (OPEN)» would get a bound, for
  IDEAL-CYC only; R126's sentence that the k = 1 face class height is OPEN (§1) would be answered, since D^tot(v) − 1 ≤ T_CYC.
- Limits: nothing on Γ3(G) (R118's DATA records Γ3 runs that differ from the IDEAL-CYC run at exact VJ ties); nothing for N5,
  N5′-xi, other games, other rules, other runs; no tightness of any constant.

## 14. Machine checks
- experiments/new/check.sh, blocks «BOX 208 LEVEL» and «BOX 208 ADD-B» (existing): re-run box208/check208.sh and check208c.sh
  (level208.py, plat208.py and rv208.py on their check sets, the controls, the frozen outputs), diff against check208.out and
  check208c.out, require every must-0 counter 0 and every control to fire.
- experiments/new/check.sh, block «P-N5-LEVEL» (new): sha1 of this packet, of its source note, of line L-1, of the two landed packet
  files quoted in §1, and of every tool, output and engine module named in §11, against experiments/new/box211/level.pins; and the
  last line of box211/quotes211.out must begin «quotes 44 missing 0» and name the pinned trunk commit.
- Record tools (they need git objects, so they are not run by check.sh): box211/quotes211.py TRUNK (the quote check of §1);
  box211/mkl1_211.py RES.md (generates docs/new/P-N5-LEVEL-line-L1.txt, the proposed RESULTS line, and asserts this packet's sha1).
