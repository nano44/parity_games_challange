# Box 210 (D18): GEN-LEVEL — the level lemma of boxes 208 / 209 holds for Howard on EVERY parity game in split form (CANDIDATE); it bounds the moves of the top even scale and nothing below it; on the exponential families the potential moves 3 to 5 times and all the time sits in frozen-class windows where Odd keeps flipping (DATA) (L-NEW successor 72)
Written 2026-11-12 (date -u in the commit). D18 (owner, verbatim): «Focus on N5 and work toward proving it. Explore novel approaches,
especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable
assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures
and open problems.»
**SCOPE LINE: Howard strategy improvement for Even (switch-best, optimal reply of Odd, Vöge-Jurdziński values) on parity games in split
form. No bound on the length of such a run is claimed for general games. Not N5, not N5′-xi (boxes 208 / 209 are the only place where this
lemma reaches them), not M4; G-N5-TIME stays OPEN.**
**LABEL: the lemmas and the conditional theorem are CANDIDATES** (lane, unrefereed); §5 is DATA; §6 is a READING. D1 (owner, verbatim): «A
claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until
it passes the gauntlet below.» Nothing here claims a polynomial algorithm.
Why this box: box 208 Addendum A5 left open where its argument breaks on Friedmann's games («I have not analysed where the argument breaks
on them»). This box answers that: LEVEL does not break. PLATEAU's step (P4) does.
Tools: experiments/new/box210/ (gen210.py, climb210.py, n5lev210.py, scale210.py, run210.sh, summ210.py, check210.sh, quotes210.py);
outputs box210/out/ with SHA1SUMS; section «BOX 210 GEN-LEVEL» of experiments/new/check.sh.

## 0. Answer
- A parity game is in SPLIT FORM if its vertices are of two kinds: P-vertices, with exactly one successor, and C-vertices (the choices),
  less relevant than every P-vertex and with all successors in P. Every parity game has a split form (each vertex i becomes P_i → C_i).
  In split form a choice vertex is never a cycle node and never in a set Π. That is all that boxes 208 / 209 took from the genome
  premises CN2, LOC-GATE, NO-TIE and DOM.
- **Lemma G-CLASS (CANDIDATE; §2).** Let H be any set of P-vertices of even priority that contains every vertex more relevant than one
  of its members (for instance: the even P-vertices above every odd priority). With class(v) := (Λ(v), Π(v) ∩ H), the five class facts
  of box 208 hold on every Howard run of every split-form game: classes never fall; a class is at least the class of the successor on
  the play, with equality outside H; an Odd choice vertex has the lowest class among its successors; after a step, an Even choice
  vertex has at least the class each of its successors had before.
- **Lemma GEN-LEVEL (CANDIDATE; §3).** On every Howard run of every split-form game, for every such H and every reference state b: the
  potential Φ_t = (lowest lagging class, −size of its front) never falls, rises at every step that is not a stall, and takes at most
  2·|P|·n values. At a stall the front contains a cycle of the map «Even choice → its successor at b; any other vertex → its successor
  now».
- **Lemma GEN-PLATEAU (CANDIDATE; §4).** During a plateau the vertices of class ≤ m form a set Y closed under plays and under Even's
  choices, with constant classes; Odd's chosen successor in Y always has the class of its vertex. What is NOT implied: that Odd's
  choice is constant. Odd may move among successors of equal class.
- **Theorem OF (CANDIDATE, CONDITIONAL on hypothesis (OF); §4).** If on every plateau Odd's reply is constant on Y, and Odd's reply is
  constant after the last class change, then the run has at most 2·|P|·n·(n_E + 1) + n_E steps (n_E the number of Even vertices). Boxes
  208 and 209 are this theorem for Γ(G) and Γ3(G), where (OF) is their step (P4).
- DATA (§5). Friedmann's switch-all family (N = 2, …, 7; T from 30 to 1243), Friedmann's and Fearnley's sub-exponential families (T up
  to 3554), every random game tried: every counter of G-CLASS, GEN-LEVEL and GEN-PLATEAU is 0. On the three exponential families the
  number of non-stall steps does not grow with the size of the game (5, 3 and 3); the run is one plateau and one tail, each about
  half of T, and Odd's reply changes inside both. Hypothesis (OF) fails there.
- READING (§6). The scale profile (the number of steps that change a value truncated at priority θ) of the exponential families doubles
  from one block of priorities to the next: a binary counter with one scale per bit, even and odd scales alternating. Genome games have
  two scales: an even one on top (the e-vertices), which LEVEL bounds, and one below it that is one-player on every plateau, which
  BR-SEG-G bounds. That is the whole reason for boxes 208 / 209, and it is special to that family.
- Not claimed: any bound on Howard for general games, anything on N5 or on N5′-xi outside Γ3(G), any statement for an odd top scale.

## 1. Setting and premises (every «…» on a line marked [Q] is quoted by script from trunk docs/RESULTS.md: quotes210.py)
- Games, values. A parity game on n vertices; a fixed relevance order refining the priorities; reward(v) = the rank of v, negated if
  its priority is odd. For a positional pair (σ, τ), [VJ] as in box 208 §1: Λ(v) is the most relevant vertex of the cycle of v's play;
  Π(v) the vertices on the path from v to Λ(v), before Λ(v), that are more relevant than Λ(v); (VJ-1) if Λ ≠ Λ′, Ω ◁ Ω′ iff reward(Λ)
  < reward(Λ′); (VJ-2) if Λ = Λ′ and Π ≠ Π′, with z the most relevant vertex of Π Δ Π′: Ω ◁ Ω′ iff (z ∈ Π′ and z even) or (z ∈ Π and z
  odd); then the length k.
- [Q] The source of [VJ], as landed R118 names it: «VJ00 §4.2 / Friedmann arXiv 1106.0778 §3 for the order ⊴ on values (Λ, Π, k)».
- SPLIT FORM. V = C ⊔ P; every vertex of P has exactly one successor; every vertex of C is less relevant than every vertex of P; every
  successor of a vertex of C is in P. Consequences used: (S1) every cycle contains a P-vertex, so no C-vertex is a cycle node; (S2) no
  C-vertex is in a set Π (it is less relevant than the cycle node). THE SPLIT of a game: vertex i becomes P_i (priority of i plus 2, one
  successor C_i) and C_i (owner of i, priority 0, successors P_j for the successors j of i). Plays correspond one to one. Nothing is
  claimed about the Howard run of a game and of its split being the same run (in §5's data their lengths agree where both are known).
- THE RUN. Howard for Even from any σ_0, in the sense of landed BR-SEG-G's setting: every Even vertex goes to a ⊴-best successor under
  Ω_t and keeps σ_t(v) when it is one; σ̄_t is Odd's optimal counterstrategy; Ω_t the values under (σ_t, σ̄_t); states 0, …, T, T the
  first state at which no Even vertex has a strictly better successor. s_t(v) := the successor of v on its play at t.
- [Q] (F1), landed R15 (a), for any game: «Lemma A: for any non-empty unambiguous set I of improvements of σ (VJ00 §4.4), Ωσ ⊴
  Ω_{Switch_I(σ)}.» As used: Ω_t(v) ⊴ Ω_(t+1)(v) for every vertex and step.
- [Q] [OPT], as landed R118 uses it: «an optimal counterstrategy being pointwise optimal (at every vertex its play value is ⊴ the value
  under every Odd strategy». This is a PREMISE from [VJ] here, for every game, as it is in R118 (i).
- [Q] R118 (i) BR-SEG-G [any parity game, Howard from any σ_0, under H0]: «H0: every step t → t+1 switches some Even x with Λ_t(x) ≠ x
  and Λ_(t+1)(x) ≠ x.»; «(a) every maximal run of p-steps has at most n_E steps;»; the labels: «labelled C if some vertex's cycle node Λ
  changes, else R if Odd's optimal counterstrategy σ̄ (any fixed deterministic choice) changes somewhere, else p».
- H, CLASSES. H ⊆ P is an EVEN UP-SET: every vertex of H has even priority, and every vertex more relevant than a vertex of H is in H.
  class(v) := (Λ(v), Π(v) ∩ H); (Λ, E) < (Λ′, E′) iff reward(Λ) < reward(Λ′), or Λ = Λ′ and the most relevant element of E Δ E′ lies
  in E′. A strict total order (different vertices have different rewards).
- NOT used: any genome premise, any statement of boxes 208 / 209 (their proofs are the template; every step is redone here).

## 2. Lemma G-CLASS (CANDIDATE)
For every split-form game, every Howard run, every even up-set H:
- **(G-K2) COARSE.** For any two triples Ω = (Λ, Π, k), Ω′ = (Λ′, Π′, k′) of plays: Ω ⊴ Ω′ implies class ≤ class′.
  Proof: Λ ≠ Λ′: (VJ-1). Λ = Λ′ and Π ∩ H = Π′ ∩ H: equal classes. Otherwise let z_H be the most relevant element of (Π ∩ H) Δ (Π′ ∩ H)
  and z the most relevant element of Π Δ Π′. z is at least as relevant as z_H ∈ H, so z ∈ H (up-set), so z = z_H, and z is even. By
  (VJ-2), Ω ◁ Ω′ iff z ∈ Π′ iff class < class′. ∎
- **(G-K1) MONOTONE.** class_t(v) ≤ class_(t+1)(v). Proof: (F1) and (G-K2). ∎
- **(G-K3) ALONG THE PLAY.** At every state, for every vertex v with s := s_t(v): Λ_t(v) = Λ_t(s); if v ∉ H, or v is not more relevant
  than Λ_t(v), then class_t(v) = class_t(s); otherwise class_t(v) = (Λ_t(s), {v} ∪ (Π_t(s) ∩ H)) > class_t(s). In every case class_t(v)
  ≥ class_t(s), and class_t(v) is determined by v and class_t(s).
  Proof: v and s have the same cycle. If v is its cycle node, Π_t(v) = ∅ = Π_t(s) (the path of s to v runs inside the cycle, whose most
  relevant vertex is v). Otherwise Π_t(v) is Π_t(s), plus v if v is more relevant than Λ. If v ∈ H is more relevant than Λ, then
  v ∉ Π_t(s): else v would be on the play of s before the cycle node, so v → s → … → v would put v on its own cycle, and a vertex of a
  cycle is not more relevant than its cycle node. The two classes then differ exactly in v, which is in the larger. ∎
- **(G-K4) ODD CHOICES.** For every Odd C-vertex g, every successor y of g and every state t: class_t(g) ≤ class_t(y). So class_t(g) =
  class_t(σ̄_t(g)) = the lowest class among the successors of g.
  Proof: Case 1, the play of y under (σ_t, σ̄_t) does not pass g. Let τ′ be σ̄_t with g ↦ y. The play of g under (σ_t, τ′) is g followed
  by that play of y; its triple has the Λ and the Π of Ω_t(y) (S2). By [OPT], Ω_t(g) is ⊴ that triple; (G-K2). Case 2, the play of y
  under (σ_t, σ̄_t) passes g. Then it continues as the play of g, so Λ_t(y) = Λ_t(g). If g is on the cycle, Π_t(g) = ∅ ⊆ Π_t(y). If not,
  Π_t(y) = Π_t(g) ∪ (the vertices between y and g that are more relevant than Λ). Either way Π_t(g) ∩ H ⊆ Π_t(y) ∩ H, so every element
  of the difference lies in class_t(y)'s set: class_t(g) ≤ class_t(y). The equality class_t(g) = class_t(σ̄_t(g)) is (G-K3) (g ∉ H). ∎
- **(G-K5) DOM AT CLASS LEVEL.** For every Even C-vertex x, every successor y of x and every step t: class_(t+1)(x) ≥ class_t(y).
  Proof: y′ := σ_(t+1)(x) is ⊴-best under Ω_t, so Ω_t(y′) ⊵ Ω_t(y); Ω_(t+1)(y′) ⊵ Ω_t(y′) (F1). By (G-K2), class_(t+1)(y′) ≥ class_t(y).
  And class_(t+1)(x) = class_(t+1)(y′) by (G-K3) at t + 1 (x ∉ H). ∎
Remark. Without split form (G-K4) and (G-K5) can fail (control GEN_CTRL=3, §5), in line with the landed remark that DOM is false on
general games (P-N5-XICYC fixes entry 2, XC-2).

## 3. Lemma GEN-LEVEL (CANDIDATE)
Fix a reference state b ≤ T. LAG_t := {v : class_t(v) ≠ class_b(v)}; if LAG_t ≠ ∅: m_t := the lowest class_t(v), v ∈ LAG_t; FRONT_t :=
{v ∈ LAG_t : class_t(v) = m_t}; Φ_t := (m_t, −|FRONT_t|). A step t → t + 1 (t < b, LAG_t ≠ ∅) is a STALL if no vertex of FRONT_t
changes class at it.
**Statement.** For every split-form game, Howard run, even up-set H, reference state b and t < b with LAG_t ≠ ∅:
- (GL1) LAG_(t+1) ⊆ LAG_t; if LAG_(t+1) ≠ ∅ then Φ_(t+1) ≥ Φ_t, with equality iff the step is a stall; at a stall FRONT_(t+1) = FRONT_t.
- (GL3) Either (α) some Even C-vertex z ∈ FRONT_t has σ_t(z) ∉ LAG_t, and then m_t = class_b(σ_t(z)); or (β) the cycle of some play at
  t lies inside FRONT_t, and then m_t = (c, ∅) for its cycle node c.
- (GL4) If the step is a stall, the map s on FRONT_t (s(x) := σ_b(x) for an Even C-vertex x; s(v) := s_t(v) for every other vertex)
  maps FRONT_t into itself, so it has a cycle inside FRONT_t.
- (GL5) Over 0 ≤ t ≤ b, Φ takes at most 2·|P|·n values, each on one interval of states. So at most 2·|P|·n steps before LAG is empty
  are not stalls.
**Proof.**
(GL1) Box 208 (L1), from (G-K1) alone: a vertex outside LAG_t has class_t = class_b and stays between them; a vertex of LAG_(t+1) has
class_(t+1) ≥ class_t ≥ m_t; if m_(t+1) = m_t, FRONT_(t+1) is the set of vertices of FRONT_t that keep their class.
(GL3) Take v ∈ FRONT_t and follow its play v_0 = v, v_1, …. If v_i ∈ FRONT_t and v_(i+1) ∈ LAG_t then class_t(v_(i+1)) ≤ class_t(v_i) =
m_t (G-K3) and ≥ m_t (it lags), so v_(i+1) ∈ FRONT_t. So either the whole play stays in FRONT_t, and its cycle lies in FRONT_t; every
vertex u of the cycle has Π_t(u) = ∅, so its class is (c, ∅), and it is m_t: case (β). Or there is a first z := v_i ∈ FRONT_t with
w := s_t(z) ∉ LAG_t. z is not a P-vertex: its successor is w at t and at b, and its class is determined by z and the class of w (G-K3),
which is the same at t and b; so z would not lag. z is not an Odd C-vertex: class_t(z) = class_t(w) (G-K3) = class_b(w) ≥ class_b(z)
(G-K4 at b) ≥ class_t(z) (G-K1); so z would not lag. So z is an Even C-vertex and m_t = class_t(z) = class_t(w) = class_b(w): case (α).
(GL4) An Even C-vertex x ∈ FRONT_t, y := σ_b(x): class_b(y) = class_b(x) (G-K3 at b) > m_t (x lags; (G-K1)); class_t(y) ≤ class_(t+1)(x)
(G-K5) = m_t (stall). So y lags, hence class_t(y) ≥ m_t: y ∈ FRONT_t. A P-vertex v ∈ FRONT_t with successor w: if w did not lag, v
would not (as in (GL3)); and class_t(w) ≤ class_t(v) = m_t (G-K3): w ∈ FRONT_t. An Odd C-vertex g ∈ FRONT_t, a := σ̄_t(g): class_t(a) =
class_t(g) = m_t; class_b(a) ≥ class_b(g) (G-K4 at b) > m_t: a ∈ FRONT_t.
(GL5) (GL1) gives the intervals. m_t is the class at b of a successor of an Even C-vertex, a P-vertex (α), or (c, ∅) for a cycle node
c, a P-vertex (β): at most 2·|P| values. |FRONT_t| ≤ n. ∎

## 4. Plateaus: Lemma GEN-PLATEAU and Theorem OF (CANDIDATES)
A PLATEAU (reference b) is a maximal interval [u, v] of states, u < v, with LAG ≠ ∅ and constant Φ = (m, −|J|). Y := {x : class_u(x) ≤
m}.
**Lemma GEN-PLATEAU.** For every plateau [u, v] and every s ∈ [u, v]:
- (GP1) {x : class_s(x) ≤ m} = Y and class_s = class_u on Y. [Box 208 (P1), from (GL1) and (G-K1).]
- (GP2) Y is closed under plays: s_s(x) ∈ Y for x ∈ Y. [(G-K3): the successor's class is not larger.]
- (GP3) Every successor of an Even C-vertex of Y is in Y, with class ≤ the vertex's class. [(G-K5) for s < v and (GP1), as box 208 (P3).]
- (GP4) For an Odd C-vertex g ∈ Y: σ̄_s(g) ∈ Y and class_s(σ̄_s(g)) = class_s(g); a successor of g with a class above class_s(g) is not
  chosen at any state of the plateau. [(G-K4), (GP1).]
Not implied: σ̄_s(g) = σ̄_u(g). Among the successors of g that have the class of g, Odd's choice is decided by what lies below H.
**Hypothesis (OF) for a run** (reference b = T, b′ the first state with LAG = ∅): (OF1) on every plateau [u, v], σ̄_s(g) = σ̄_u(g) for
every Odd C-vertex g ∈ Y and s ∈ [u, v]; (OF2) σ̄_s = σ̄_(b′) on [b′, T].
**Theorem OF (CONDITIONAL on (OF)).** A Howard run of a split-form game that satisfies (OF) for some even up-set H has
T ≤ 2·|P|·n·(n_E + 1) + n_E, n_E the number of Even vertices.
Proof. Box 208 Addendum A2 (P5)-(P7) with Addendum B1, on a plateau [u, v]:
- The game H_Y: vertices Y; an Even C-vertex keeps its successors (GP3); every other vertex x keeps the single successor s_u(x), which
  by (OF1) and (GP2) is s_s(x) for every s ∈ [u, v]. Only Even C-vertices have a choice. For s ∈ [u, v], Ω_s on Y is the value in H_Y
  under σ_s, and the step of the run at an Even C-vertex of Y is a Howard step of H_Y (same successors, same values, same rule).
- Every step s → s + 1, u ≤ s ≤ v, switches an Even C-vertex of Y. If not: by induction on s′ ≥ s, σ_(s′) = σ_s on the Even C-vertices
  of Y (their successors are in Y with the values of state s, and Howard keeps a best current successor) and Ω_(s′) = Ω_s on Y (Odd may
  answer σ_(s′+1) by σ̄_s, whose plays from Y stay in Y and are the plays of state s: [OPT] gives ⊴, (F1) gives ⊵). Then the front
  would have its class of state s at b, and would not lag.
- So u → u + 1, …, v − 1 → v are consecutive steps of a Howard run of H_Y that change no cycle node (GP1) and no choice of Odd (none in
  H_Y): p-steps. H0 holds (the switching vertices are C-vertices, never cycle nodes: (S1)). BR-SEG-G (a): v − u ≤ n_E(H_Y) ≤ n_E.
- The tail [b′, T]: no class changes; with (OF2), the same three steps with Y := all vertices give T − b′ ≤ n_E.
- Count as in box 209 §5: at most 2·|P|·n intervals of constant Φ, each with at most n_E stalls and one non-stall step after it. ∎
Boxes 208 and 209 as instances. Γ(G) and Γ3(G) are not in split form (gates have priority 1, β-vertices have two edges in Γ and are
frozen), so G-CLASS is proved there from the genome premises instead of (S1), (S2). (OF1) and (OF2) are their step (P4): at a gate, a
face of higher class is never chosen, and two faces of equal class force the e-face.

## 5. DATA
Engine: box210/gen210.py, with the valuation, the order and Odd's reply of box208/rv208.py (the third implementation of box 208
Addendum B); Howard's step is gen210's own. Cross-check: gen210.py --xcheck compares the value of every vertex at every state with
experiments/si si.Engine on the split game. Family games are split from the .pg files named below (sha1 of each in
out/gen210_instances.sha1), start = si.Engine's best-reward start, as in landed R118's DATA. Reference state b = T unless stated; H = the
even P-vertices above every odd priority («H top») unless stated.
Counters (definitions and units in gen210.py's header): F1; K1, K3, K4, K5 (G-CLASS); L1, L3, L3m, L4, L4c, L5 (GEN-LEVEL); P1, P2,
P3, P4w (GEN-PLATEAU). Unit of the L-counters: states t < b with a lagging vertex (L4: (vertex of the front, stall)); scope: every
vertex of the split game.
**(a) The exponential families** (out/gen210_families.out; sae_N = Friedmann's switch-all family, experiments/new/box191/inst;
friedmannsubexp_N, fearnleysubexp_N: experiments/n5-box21/instances; the last three: experiments/si/instances).
| game (out/gen210_families.out) | n (split) | H | sum of the 15 must-0 counters | T | non-stall steps | stalls | plateaus (longest) | tail | Odd flips inside Y on plateaus | Odd flips at steps with no class change |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sae_2.pg | 70 | 2 | 0 | 30 | 5 | 13 | 1 (13) | 12 | 1 | 2 |
| sae_3.pg | 98 | 2 | 0 | 70 | 5 | 33 | 1 (33) | 32 | 4 | 8 |
| sae_4.pg | 126 | 2 | 0 | 150 | 5 | 73 | 1 (73) | 72 | 11 | 23 |
| sae_5.pg | 154 | 2 | 0 | 310 | 5 | 153 | 1 (153) | 152 | 26 | 54 |
| sae_6.pg | 182 | 2 | 0 | 630 | 5 | 313 | 1 (313) | 312 | 57 | 117 |
| sae_7.pg | 210 | 2 | 0 | 1243 | 5 | 633 | 1 (633) | 605 | 120 | 244 |
| friedmannsubexp_1.pg | 40 | 2 | 0 | 12 | 3 | 5 | 1 (5) | 4 | 0 | 0 |
| friedmannsubexp_2.pg | 88 | 2 | 0 | 38 | 3 | 19 | 1 (19) | 16 | 4 | 5 |
| friedmannsubexp_3.pg | 154 | 2 | 0 | 92 | 3 | 47 | 1 (47) | 42 | 26 | 35 |
| friedmannsubexp_4.pg | 238 | 2 | 0 | 202 | 3 | 103 | 1 (103) | 96 | 99 | 143 |
| friedmannsubexp_5.pg | 340 | 2 | 0 | 424 | 3 | 215 | 1 (215) | 206 | 309 | 469 |
| friedmannsubexp_6.pg | 460 | 2 | 0 | 870 | 3 | 439 | 1 (439) | 428 | 868 | 1365 |
| friedmannsubexp_7.pg | 598 | 2 | 0 | 1764 | 3 | 887 | 1 (887) | 874 | 2288 | 3695 |
| friedmannsubexp_8.pg | 754 | 2 | 0 | 3554 | 3 | 1783 | 1 (1783) | 1768 | 5785 | 9539 |
| fearnleysubexp_1.pg | 40 | 2 | 0 | 12 | 3 | 5 | 1 (5) | 4 | 0 | 0 |
| fearnleysubexp_2.pg | 76 | 2 | 0 | 36 | 3 | 17 | 1 (17) | 16 | 1 | 2 |
| fearnleysubexp_3.pg | 118 | 2 | 0 | 84 | 3 | 41 | 1 (41) | 40 | 8 | 14 |
| fearnleysubexp_4.pg | 166 | 2 | 0 | 180 | 3 | 89 | 1 (89) | 88 | 31 | 54 |
| fearnleysubexp_5.pg | 220 | 2 | 0 | 372 | 3 | 185 | 1 (185) | 184 | 92 | 162 |
| fearnleysubexp_6.pg | 280 | 2 | 0 | 756 | 3 | 377 | 1 (377) | 376 | 239 | 426 |
| switchallexp_N3.pg | 98 | 2 | 0 | 70 | 5 | 33 | 1 (33) | 32 | 4 | 8 |
| zadehexp_N5.pg | 158 | 2 | 0 | 6 | 2 | 0 | 0 (0) | 4 | 0 | 10 |
| randomfacetsubexp_N5.pg | 414 | 56 | 0 | 10 | 10 | 0 | 0 (0) | 0 | 0 | 0 |
- What the table shows: every counter is 0; the number of non-stall steps is 5 on every sae_N and 3 on every friedmannsubexp_N and
  fearnleysubexp_N, while T doubles; the run is one plateau and one tail of about T/2 steps each; inside them Odd's reply changes
  (last two columns), so hypothesis (OF) fails on these games. T for sae_2..7 equals landed R118's «T = 30, 70, 150, 310, 630, 1243».
- xcheck: 23 of 23 files OK (values of every vertex at every state equal to si.Engine's on the split game).
**(b) Random games and the controls** (out/gen210_rand.out, out/gen210_ctrl.out; random start strategy).
| set | games | sum of the 15 must-0 counters | descriptive |
| --- | --- | --- | --- |
| seed 2111: 8 vertices, priorities 1..6, out-degree 1..3, top priority even, H top | 3000 | 0 | max T 5, sum T 3554, vertices of H 6692, non-stall steps 2958, stalls 12, plateaus 12 (longest 1), longest tail 2, Odd flips inside Y 2, at class-quiet steps 70, capped 0 |
| seed 2112: 8 vertices, priorities 1..6, out-degree 1..3, top priority odd, H top | 3000 | 0 | max T 5, sum T 3644, vertices of H 0, non-stall steps 2593, stalls 136, plateaus 132 (longest 2), longest tail 3, Odd flips inside Y 32, at class-quiet steps 136, capped 0 |
| seed 2113: 16 vertices, priorities 1..10, out-degree 1..3, top priority even, H top | 1500 | 0 | max T 8, sum T 2802, vertices of H 3564, non-stall steps 2381, stalls 25, plateaus 25 (longest 1), longest tail 3, Odd flips inside Y 12, at class-quiet steps 65, capped 0 |
| seed 2114: 40 vertices, priorities 1..12, out-degree 1..4, top priority even, H top | 400 | 0 | max T 10, sum T 1453, vertices of H 1437, non-stall steps 1258, stalls 11, plateaus 9 (longest 2), longest tail 3, Odd flips inside Y 25, at class-quiet steps 66, capped 0 |
| seed 2115: 12 vertices, priorities 1..8, out-degree 1..3, top priority even, H none | 1500 | 0 | max T 7, sum T 2349, vertices of H 0, non-stall steps 1652, stalls 106, plateaus 98 (longest 2), longest tail 3, Odd flips inside Y 46, at class-quiet steps 182, capped 0 |
| CONTROL GEN_CTRL=1, seed 2116: 16 vertices, priorities 1..10, out-degree 1..3, top priority even, H top | 300 | fires: L1 79, L3 240, L4 103, L4c 91, P1 432, P2 6, P3 10 | max T 6, sum T 556, vertices of H 703, non-stall steps 380, stalls 94, plateaus 26 (longest 3), longest tail 3, Odd flips inside Y 28, at class-quiet steps 15, capped 0 |
| CONTROL GEN_CTRL=2, seed 2117: 8 vertices, priorities 1..6, out-degree 1..3, top priority odd, H top | 300 | fires: K1 64, K4 122, K5 163, L1 3, L4 2, L4c 2, P3 9 | max T 4, sum T 351, vertices of H 711, non-stall steps 266, stalls 10, plateaus 8 (longest 2), longest tail 2, Odd flips inside Y 1, at class-quiet steps 9, capped 0 |
| CONTROL GEN_CTRL=3, seed 2118: 6 vertices, priorities 1..6, out-degree 1..3, top priority even, H top | 3000 | fires: K1 7, K4 15, K5 11, L1 1, L3 1, L4 1, L4c 1, L5 191, P3 2 | max T 4, sum T 2876, vertices of H 1993, non-stall steps 2175, stalls 86, plateaus 80 (longest 2), longest tail 3, Odd flips inside Y 30, at class-quiet steps 83, capped 0 |
- Controls: GEN_CTRL=1 (FRONT := the highest lagging class) fires L1, L3, L4, L4c; GEN_CTRL=2 (H := the odd P-vertices above every even
  priority, on games with an odd top priority) fires K1, K4, K5 and L4; GEN_CTRL=3 (the game is not split) fires K1, K4, K5, L4. L5's
  count under GEN_CTRL=3 is an artefact (|P| is then the number of single-successor vertices). F1, K3, L3m, P4w have no control that
  fires; on the family games GEN_CTRL=1 does not fire (the highest and the lowest lagging class coincide there).
- With an odd top priority H is empty and the class is Λ alone (seed 2112, and GEN_H=none, seed 2115): the lemma then speaks about the
  steps that change a cycle node.
**(c) Every reference state, and hill-climbs** (out/gen210_allb.out, out/climb210.out; GEN_ALLB=1 runs LEVEL and the plateaus for
every b = 1, …, T, and the counts add up over b; climb210.py mutates small games towards long runs and checks every game visited).
| run (every reference state b; counts add up over b) | games | sum of the 15 must-0 counters | descriptive |
| --- | --- | --- | --- |
| sae_2.pg | 1 | 0 | max T 30, non-stall (b, t) pairs 75, stalls 221, plateaus 17 (longest 13), longest tail 13, Odd flips inside Y 17 |
| sae_3.pg | 1 | 0 | max T 70, non-stall (b, t) pairs 175, stalls 1221, plateaus 37 (longest 33), longest tail 33, Odd flips inside Y 148 |
| sae_4.pg | 1 | 0 | max T 150, non-stall (b, t) pairs 375, stalls 5621, plateaus 77 (longest 73), longest tail 73, Odd flips inside Y 847 |
| friedmannsubexp_1.pg | 1 | 0 | max T 12, non-stall (b, t) pairs 18, stalls 35, plateaus 7 (longest 5), longest tail 5, Odd flips inside Y 0 |
| friedmannsubexp_2.pg | 1 | 0 | max T 38, non-stall (b, t) pairs 54, stalls 361, plateaus 19 (longest 19), longest tail 19, Odd flips inside Y 76 |
| friedmannsubexp_3.pg | 1 | 0 | max T 92, non-stall (b, t) pairs 132, stalls 2115, plateaus 45 (longest 47), longest tail 47, Odd flips inside Y 1170 |
| random, seed 2120: 8 vertices, priorities 1..6, out-degree 1..3, top priority even | 1500 | 0 | max T 5, non-stall (b, t) pairs 2138, stalls 11, plateaus 10 (longest 2), longest tail 2, Odd flips inside Y 0 |
| hill-climb, seed 2121, 6000 games visited, 7 vertices, priorities 1..8 (longest run found: T 8) | 6000 | 0 | max T 8, non-stall (b, t) pairs 75714, stalls 2100, plateaus 1291 (longest 3), longest tail 3, Odd flips inside Y 241 |
| hill-climb, seed 2122, 6000 games visited, 10 vertices, priorities 1..10 (longest run found: T 11); b = T only | 6000 | 0 | max T 11, non-stall (b, t) pairs 27873, stalls 1936, plateaus 970 (longest 4), longest tail 4, Odd flips inside Y 1088 |
| hill-climb, seed 2123, 3000 games visited, 14 vertices, priorities 1..12 (longest run found: T 18); b = T only | 3000 | 0 | max T 18, non-stall (b, t) pairs 19590, stalls 384, plateaus 382 (longest 2), longest tail 3, Odd flips inside Y 261 |
- The hill-climbs do not find long runs (T ≤ 18): they test the lemma on many shapes, not on hard ones. The hard ones are table (a).
**(d) N5's own σ-sequence** (out/n5lev210.out; n5lev210.py copies the loop of experiments/new/n5.py mode n5 and runs gen210's counters
on the sequence of Even's strategies; states = iterations; start: best-reward pair on the family games, a random pair otherwise).
| N5 run (out/n5lev210.out) | games | iterations (max, sum) | fallbacks | K1 + K3 + K4 + L1 + L3 + L3m | K5 | L4 | L4c | P3 | stalls |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sae_2.pg | 1 | 8, 8 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |
| sae_3.pg | 1 | 7, 7 | 0 | 0 | 11 | 0 | 0 | 0 | 0 |
| sae_4.pg | 1 | 8, 8 | 0 | 0 | 15 | 0 | 0 | 0 | 0 |
| sae_5.pg | 1 | 10, 10 | 0 | 0 | 19 | 0 | 0 | 0 | 0 |
| sae_6.pg | 1 | 12, 12 | 0 | 0 | 23 | 0 | 0 | 0 | 0 |
| friedmannsubexp_2.pg | 1 | 10, 10 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| friedmannsubexp_3.pg | 1 | 15, 15 | 0 | 0 | 0 | 0 | 0 | 0 | 6 |
| friedmannsubexp_4.pg | 1 | 19, 19 | 0 | 0 | 0 | 0 | 0 | 0 | 8 |
| random, seed 2124: 8 vertices, priorities 1..6 | 1500 | 5, 2401 | 1 | 0 | 144 | 83 | 76 | 195 | 141 |
| random, seed 2125: 16 vertices, priorities 1..10 | 500 | 8, 1168 | 2 | 0 | 128 | 57 | 50 | 128 | 85 |
- The counters that do not depend on the switching rule are 0. K5 (DOM at class level) fires on the random games and on sae_N, and with
  it L4 / L4c on the random games: SPEC S4a is not switch-best. This is DATA about which step of GEN-LEVEL N5's rule lacks; N5 is fast
  on these families (7 to 19 iterations), and nothing is claimed about N5.
**(e) Scale profiles** (out/scale210.out, scale210.py --blocks; «a..b:c» = for every priority threshold θ from a down to b, c steps
change some value truncated at θ; the first entry is the top priority, where nothing changes; long lines are wrapped).
- sae_2.pg (T 30, Λ-loud 0): 44..44:0 42..39:5 38..38:13 37..35:14 34..34:16 32..32:27 30..1:30
- sae_3.pg (T 70, Λ-loud 0): 60..60:0 58..55:5 54..54:14 53..53:15 51..51:16 50..50:32 49..47:34 46..46:38 44..44:67 42..1:70
- sae_4.pg (T 150, Λ-loud 0): 76..76:0 74..71:5 70..70:14 69..69:15 67..67:16 66..66:33 65..65:35 63..63:36 62..62:68 61..59:74 58..58:82
  56..56:147 54..1:150
- sae_5.pg (T 310, Λ-loud 0): 92..92:0 90..87:5 86..86:14 85..85:15 83..83:16 82..82:33 81..81:35 79..79:36 78..78:69 77..77:75 75..75:76
  74..74:140 73..71:154 70..70:170 68..68:307 66..1:310
- sae_6.pg (T 630, Λ-loud 0): 108..108:0 106..103:5 102..102:14 101..101:15 99..99:16 98..98:33 97..97:35 95..95:36 94..94:69 93..93:75
  91..91:76 90..90:141 89..89:155 87..87:156 86..86:283 85..83:312 82..82:344 80..80:627 78..1:630
- sae_7.pg (T 1243, Λ-loud 0): 124..124:0 122..119:5 118..118:14 117..117:15 115..115:16 114..114:33 113..113:35 111..111:36 110..110:69
  109..109:75 107..107:76 106..106:141 105..105:155 103..103:156 102..102:284 101..101:314 99..99:315 98..98:562 97..95:620 94..94:682
  92..92:1240 90..1:1243
- friedmannsubexp_2.pg (T 38, Λ-loud 0): 48..48:0 46..46:3 45..41:4 40..40:10 39..39:11 37..31:12 30..28:13 26..26:35 24..12:36 10..1:38
- friedmannsubexp_3.pg (T 92, Λ-loud 0): 66..66:0 64..64:3 63..59:4 58..58:10 57..57:12 55..53:13 52..52:25 51..51:28 49..41:31 40..38:32
  36..36:86 34..16:88 14..11:91 10..1:92
- friedmannsubexp_4.pg (T 202, Λ-loud 0): 84..84:0 82..82:3 81..77:4 76..76:10 75..75:12 73..71:13 70..70:25 69..69:29 67..65:32 64..64:56
  63..63:63 61..51:71 50..48:72 46..46:194 44..20:196 18..15:200 14..1:202
- friedmannsubexp_5.pg (T 424, Λ-loud 0): 102..102:0 100..100:3 99..95:4 94..94:10 93..93:12 91..89:13 88..88:25 87..87:29 85..83:32
  82..82:56 81..81:64 79..77:72 76..76:120 75..75:135 73..61:153 60..58:154 56..56:414 54..24:416 22..19:421 18..1:424
- friedmannsubexp_6.pg (T 870, Λ-loud 0): 120..120:0 118..118:3 117..113:4 112..112:10 111..111:12 109..107:13 106..106:25 105..105:29
  103..101:32 100..100:56 99..99:64 97..95:72 94..94:120 93..93:136 91..89:154 88..88:250 87..87:281 85..71:319 70..68:320 66..66:856
  64..28:858 26..23:865 22..19:869 18..1:870
- fearnleysubexp_2.pg (T 36, Λ-loud 0): 46..46:0 44..44:3 43..39:4 38..29:10 28..26:12 24..24:34 22..10:35 8..1:36
- fearnleysubexp_3.pg (T 84, Λ-loud 0): 64..64:0 62..62:3 61..57:4 56..56:10 55..51:12 50..39:24 38..36:28 34..34:82 32..14:83 12..1:84
- fearnleysubexp_4.pg (T 180, Λ-loud 0): 82..82:0 80..80:3 79..75:4 74..74:10 73..69:12 68..68:24 67..63:28 62..49:52 48..46:60 44..44:178
  42..18:179 16..1:180
- fearnleysubexp_5.pg (T 372, Λ-loud 0): 100..100:0 98..98:3 97..93:4 92..92:10 91..87:12 86..86:24 85..81:28 80..80:52 79..75:60
  74..59:108 58..56:124 54..54:370 52..22:371 20..1:372
- check210.sh (re-run by experiments/new/check.sh, section «BOX 210 GEN-LEVEL», diffed against check210.out): sae_2, sae_3,
  friedmannsubexp_2, 200 random games, the three controls, one cross-check, one scale profile.

## 6. READING (not a statement): scales
- For a priority θ, truncate every value at θ: keep Λ and the part of Π of priority ≥ θ, ordered by (VJ-1), (VJ-2). By the argument of
  (G-K2) (the most relevant difference of two truncated sets is the most relevant difference of the full sets), truncated values never
  fall along a Howard run, for every θ and both parities. loud(θ) := the number of steps at which some truncated value changes. It
  does not fall as θ falls; it starts at the number of Λ-changing steps and is at most T.
- On the exponential families loud(θ) roughly doubles from one block of priorities to the next (§5, scale210.py --blocks): 5, 14-16,
  33-36, 69-76, 140-156, … on Friedmann's switch-all family; the number of blocks grows with N. The run is a binary counter that
  spends one scale per bit, and the scales alternate in parity. GEN-LEVEL bounds the top one (5 steps) and says nothing below.
- A statement for more scales would need two things that are not here. (1) A version for an ODD scale: there Even's classes fall along
  the play (negative weights), the lowest lagging class can wait for a higher one, and (GL3) / (GL4) fail (control GEN_CTRL=2). The
  mirror argument, ordering the lagging vertices by their FINAL class from the top, settles one vertex at a time but does not freeze
  the rest, so it gives no plateau. (2) A recursion: on a plateau the run on Y is a Howard run with every class of the upper scale
  constant, so the next scale could be treated the same way, at the price of one factor 2·|P|·n per scale. Even if (1) were solved,
  that is a bound of the form n^(O(number of scales)): polynomial only for a bounded number of scales.
- Genome games are the two-scale case in which the second scale needs no recursion, because it is one-player on every plateau. Read
  this way, an instance on which the argument of boxes 208 / 209 fails must break (OF): Odd must have, at some vertex, two successors
  of the same top-scale class between which its choice is not forced. R104's gates do not allow that (two faces of equal class force
  the e-face). This is a statement about the proof, not a lower-bound recipe.

## 7. Relation to landed results; contradiction check
- [Q] R118 (i) BR-SEG-G («T ≤ C + R + (C + R + 1)·n_E» for any game under H0): GEN-LEVEL is a different decomposition of the same runs,
  by the classes of one even scale and not by the labels C / R / p. It does not bound R. On Friedmann's family landed R118 records
  «C = 0; R = 4, 10, 24, 54, 116, 241; T = 30, 70, 150, 310, 630, 1243»; §5 has the same T and adds: 5 non-stall steps for every N.
- No contradiction with the exponential lower bounds: on those families GEN-LEVEL's count is constant and (OF) fails.
- Boxes 208 / 209: unchanged. This box neither strengthens nor weakens their statements. It isolates what they use: the five class
  facts (here from split form), and (OF) (there from the shape of the gates).

## 8. Not claimed; where to attack
- Not claimed: a bound on T for Howard on general games; anything on N5, or on N5′-xi outside Γ3(G) from S3; that the split of a game
  has the same Howard run as the game; novelty against the literature (no source was opened for this box; the argument is Dijkstra's
  settling order applied to the top even priorities, and I have not searched for it).
- N5 itself. SPEC S4a does not move an Even vertex to its ⊴-best successor: it takes Even's optimum against the current τ among «keep
  or take an improving edge». (F1) holds for every such step (R15 (a) is for any set of improvements), so (G-K1)-(G-K4), (GL1) and
  (GL3) hold along N5's σ-sequence on a split-form game by the proofs above. (G-K5), and with it (GL4), is the step that uses
  switch-best. §5's last table (n5lev210.py, N5's own runs on split-form games) shows exactly this split: the first group of counters
  is 0, K5 / L4 / L4c fire. No statement about N5 is made.
- Where I would attack: (G-K4) case 2 (the play of y returns to g); (G-K3) when v is its own cycle node; (GL3)'s use of «determined by
  z and the class of w» for a vertex of H; the premise [OPT] for arbitrary games (it is a [VJ] premise, as in R118 (i)); the engine's
  reply of Odd (an Odd-side iteration to local optimality; cross-checked against si.Engine on every file of §5, not proved here).

## Addendum A (L-NEW successor 72; written 2026-11-12 after the push of 7e793af1: two sentences of the body CORRECTED, one citation corrected, one remark relabelled, a brute-force check of every even up-set; no lemma changes)
The body is unchanged above this line. **SCOPE LINE and LABEL as above.** A second reviewer agent (started by this session, fresh
context, read-only on the repository; not a fleet referee; it changes no label) read §1-§4 and attacked them by computation. Its verdict:
no mathematical error found in G-CLASS, GEN-LEVEL, GEN-PLATEAU or Theorem OF; four defects of wording or citation, corrected here.
### A1. Corrections
- (1) WRONG AS WORDED, §0 «Boxes 208 and 209 are this theorem for Γ(G) and Γ3(G), where (OF) is their step (P4)» and §4 «Boxes 208
  and 209 as instances». Γ(G) and Γ3(G) are not in split form, and their class uses the e-vertices, which are NOT an even up-set: K3
  (odd), K0 and c_W lie above them. Boxes 208 / 209 are ANALOGUES of Theorem OF, with their own proofs of the class facts (the core is
  handled there by a separate clause) and with (P4) in the place of (OF). Corrected reading: Theorem OF is the split-form analogue of
  boxes 208 / 209; neither implies the other. §7's last bullet («It isolates what they use») is to be read the same way.
- [Q] (2) CITATION CORRECTED, §1. The spelled-out form of [OPT] is not from landed R118 (the body's words): the string is in landed R122's premise
  clause, and it continues: «an optimal counterstrategy being pointwise optimal (at every vertex its play value is ⊴ the value under
  every Odd strategy; RESULTS R57 (b), [1E-N3], as landed in R104)». So [OPT] is here what it is everywhere in the fleet: the standing
  SPEC premise 1E-N3 (R57 (b)). It is a premise of every statement of this box.
- (3) RELABELLED, §8's bullet «N5 itself». It stands under «Not claimed» but asserts that (G-K1)-(G-K4), (GL1), (GL3) hold along N5's
  σ-sequence. Label: READING + DATA, not a statement. The reading: by SPEC S4a (docs/new/N5-ssi-global.md) σ_new(v) is σ(v) or the
  head of an improving edge of Iσ, and S4c's fallback switches improving edges, one per vertex; so every change of σ is a set of
  improvements to which R15 (a) applies. That reading of the SPEC is mine and unrefereed. The DATA is §5 (d).
- (4) GAP IN THE DATA, §5: the lemma is stated for every even up-set H, and §5 tests only H = the whole top even block and H = ∅.
  Closed by A2.
### A2. Brute force, every even up-set, every reference state (brute210.py; run210b.sh; outputs out/brute210_*.out)
brute210.py is the reviewer agent's checker, taken into the lane: its own valuation; Odd's reply found by enumerating ALL positional Odd
strategies (so it does not assume, as gen210.py's engine does, that a locally optimal reply is optimal; it reports NO_POINTWISE_MIN if
no pointwise minimum exists); its own Howard run; F1, [OPT], (G-K1)-(G-K5), (GL1), (GL3), (GL4), (GL5), (GP1)-(GP4) and the «switch in
Y» step of Theorem OF, for every even up-set H and every reference state b. Unit: (H, run) pairs; scope: every vertex.
| set (file in out/) | runs | (H, run) pairs | must-0 counters | descriptive |
| --- | --- | --- | --- | --- |
| every split of every 3-vertex game, every start strategy (exhaustive) (brute210_exh3.out) | 54872 | 102885 | 0 | Odd strategies enumerated 173137, replies 92569, max T 3, stalls 777, plateaus 777 (longest 1) |
| every general split-form game with 2 choice and 3 priority vertices, every start strategy (exhaustive) (brute210_exhgen23.out) | 361000 | 676875 | 0 | Odd strategies enumerated 797023, replies 531693, max T 3, stalls 851, plateaus 851 (longest 1) |
| random: rsplit seed 2131 cnt 20000 n0 5 d 6 deg 3 (brute210_rand.out) | 20000 | 47304 | 0 | Odd strategies enumerated 217482, replies 35908, max T 5, stalls 626, plateaus 614 (longest 2) |
| random: rsplit seed 2132 cnt 10000 n0 6 d 8 deg 3 (brute210_rand.out) | 10000 | 23594 | 0 | Odd strategies enumerated 174364, replies 19337, max T 4, stalls 439, plateaus 425 (longest 2) |
| random: rgen seed 2133 cnt 20000 nC 4 nP 5 d 6 (brute210_rand.out) | 20000 | 47362 | 0 | Odd strategies enumerated 144070, replies 32548, max T 4, stalls 124, plateaus 122 (longest 2) |
| random: rgen seed 2134 cnt 10000 nC 5 nP 7 d 8 (brute210_rand.out) | 10000 | 24439 | 0 | Odd strategies enumerated 116994, replies 17420, max T 4, stalls 84, plateaus 83 (longest 2) |
| CONTROL CTRL=H (H not an up-set): rsplit seed 2135 cnt 3000 n0 5 d 6 deg 3 (brute210_ctrl.out) | 3000 | 2071 | fires: K1 28 K2 507 K4 22 K5 35 L1fall 1 L1stall 1 L3 1 L4odd 1 L4even 19 L5set 1 P3 36 | Odd strategies enumerated 31867, replies 5372, max T 4, stalls 29, plateaus 28 (longest 1) |
| CONTROL CTRL=Hodd (H of both parities): rsplit seed 2136 cnt 3000 n0 5 d 6 deg 3 (brute210_ctrl.out) | 3000 | 5341 | fires: K1 434 K2 3397 K4 771 K5 959 L1fall 36 L1stall 18 L1rise 12 L4even 37 P1 2 P3 54 OFswitchY 13 | Odd strategies enumerated 32432, replies 5422, max T 5, stalls 80, plateaus 62 (longest 1) |
| CONTROL CTRL=nosplit (game not split): rsplit seed 2137 cnt 3000 n0 5 d 6 deg 3 (brute210_ctrl.out) | 3000 | 3909 | fires: L5 233 L5set 1399 | Odd strategies enumerated 32173, replies 5377, max T 5, stalls 78, plateaus 78 (longest 1) |
- No NO_POINTWISE_MIN in any set: a pointwise minimum of Odd existed in every state enumerated. The controls CTRL=H and CTRL=Hodd fire
  on the class facts; CTRL=nosplit fires only the counting clauses (L5, L5set) on this set, so it is a weak control here (gen210.py's
  GEN_CTRL=3 fires K4 and K5 on unsplit games, §5 (b)).
- Not in the lane, so not DATA: the reviewer's larger exhaustive set (every general split-form game with 3 choice and 3 priority
  vertices, 11,852,352 runs, reported 0), its comparison of gen210.py's reply of Odd with brute force (73,000 games, reported equal),
  and its re-run of §5 (a) / (c) on seven family files with its own engine (reported equal to the tables).
### A3. What the reviewer did not check (its own list)
VJ00 itself; BR-SEG-G by computation; §5's tables (b), (d), (e) and §6; the N5 reading of (3); the numeric bound of Theorem OF (no run
comes near it). Its exhaustive and random games are tiny (T ≤ 6, plateaus ≤ 2): long plateaus are tested only by §5 (a) and (c).
