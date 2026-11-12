# T70: (1) robustness of T69's «NEW»: a published linear step bound exists for the MIRROR orientation (Jurdziński–Trivedi Lemma 19), none was found for box 208's orientation; (2) box 208's potential against PPI's Dijkstra potential: same game, different object
L-LIT successor (D18, D1; Lead brief 2026-11-12 13:46Z, its clock). Written 2026-11-12 (date -u in the commit). Working note, unrefereed.
Not a TARGET.md claim; not M3 or M4; G-N5-TIME stays OPEN; every statement of box 208 stays a CANDIDATE (D1).
Labels: KNOWN (source) / IMPLIED (source + argument) / NEW (searched where) / CONTRADICTS (source); READING (L-LIT, not to sign);
PROVED-in-source; DATA (unit, set, scope, counter). «NEW» is a search result, not a theorem.
Objects: claude/l-new 8db300fe docs/new/N5-LEVEL-box208.md (sha1 55e65381); docs/lit/T69-dijkstra-potentials-policy-iteration.md.
Tool: docs/lit/T69-mirror-check.py (own engine, no code of another lane).
Words: «ABS orientation» = the MAXIMISER improves by Howard's all-switch step and the minimiser answers with shortest paths (box 208
§10; on Γ(G): Even improves, Odd answers). «MIRROR orientation» = the MINIMISER improves and the maximiser answers exactly.

## 0. Answers
1. T69's verdict needs one correction. A polynomial (linear) bound on all-switch strategy improvement steps for a class of two-player
   games with non-negative weights IS published, in the MIRROR orientation: Jurdziński–Trivedi, arXiv 0907.3414 v1, Lemma 19
   («terminate in O(\|R\|) iterations»), with a three-sentence proof («a routine induction»). For finite shortest-path games with
   weights ≥ 0 and no zero-weight cycle the MIRROR bound ≤ n − 1 steps is IMPLIED by a Dijkstra-order induction (§2; READING).
2. For the ABS orientation (box 208's) no step bound was found, in T69's sources or in Schewe CSL 2008 and Rutkowski (opened
   today). The MIRROR induction does NOT transfer: on a designed instance the vertex with the second-smallest optimal value is the
   last to reach it (§2.3, DATA). So Statement ABS keeps the label NEW (searched), and the reason is now sharper: the easy half is
   published; the half box 208 needs is the one where Howard's run does not follow Dijkstra's order.
3. Schewe CSL 2008 has no hidden step bound: «finding a non-trivial bound on the number of updates remains an intriguing future
   challenge» (p.14). Rutkowski's algorithm is not a strategy improvement.
4. LEVEL is NOT a statement about PPI's potential applied to Howard's rule (§3). The exact relation:
   - the game solved inside ONE PPI round (the En+ game of a simple game) satisfies Statement ABS's hypotheses; PPI solves it in one
     label-setting pass, Howard (ABS) in up to (edges of Max)·(vertices) steps;
   - LEVEL's potential (m_t, −\|FRONT_t\|) is an ANALYSIS quantity defined from a reference state; PPI's potential En+ is a COMPUTED
     vertex labelling; the first is not the second evaluated along a Howard run;
   - Question 19 is about the number of PPI ROUNDS on games with weights of both signs. Nothing in LEVEL bounds rounds, and no answer
     to Question 19 would confirm or refute LEVEL.

## 1. Sources opened for T70 (2026-11-12; sha256 prefixes in notes/L-LIT.md)
| source | location | quote / content |
| --- | --- | --- |
| Jurdziński, Trivedi, «Reachability-time games on timed automata», arXiv 0907.3414 v1 (20 Jul 2009; conference version ICALP 2007) | abstract; §4 PDF p.7-10: Improve_Max, Algorithm 1, Theorem 13, Improve_Min, Algorithm 2, Theorem 18; §5 Lemma 19 PDF p.10; its proof, appendix PDF p.15 | abstract: «players Min and Max choose moves so that the time to reach a final state in a timed automaton is minimised or maximised»; «a strategy improvement algorithm for the problem». Improve_Min (p.9): «µ(s) if µ(s) ∈ M_*(s, (T, D))», else «Choose(M_*(s, (T, D)))» (every state not at an optimal move switches). Algorithm 2 step 2: «Compute the solution (T_i, D_i) of Opt_Max(Γ↾µ_i)». «Lemma 19 … The strategy improvement algorithms for Opt_Max(Γ_1) and Opt_MinMax(Γ_2) terminate in O(\|R\|) iterations and hence run in O(\|R\|²) and O(\|R\|³) time, respectively.» Proof: «We claim that for every i ≥ 0, if D(R) ≡ i then for all j ≥ i, we have (T_j(R), D_j(R)) = (T(R), D(R)). This can be established by a routine induction on the values of the regionally constant function D.» … «Algorithm 1 must therefore terminate no later than after \|R\| + 1 iterations» … «An analogous routine proof by induction on the value of D can be used to prove that Algorithm 2 terminates in O(\|R\|) iterations.» |
| Schewe, «An optimal strategy improvement algorithm for solving parity and payoff games», CSL 2008 (DOI 10.1007/978-3-540-87531-4_27), author copy from the CISPA publication page | §4 «Complexity» and Theorem 4, PDF p.10; §6 PDF p.14 | «The optimal improvement algorithm generalizes Dijkstra's single source shortest path algorithm to two player games.» «Theorem 4. For an escape game with n positions and m edges, the optimal improvement can be computed using O(m + δ log δ) arithmetic operations». p.14: «finding a non-trivial bound on the number of updates remains an intriguing future challenge. The algorithm inherits the Ω(n) bound on the required number of updates from Büchi games, while the size of the codomain implies an O((1 + n/c)^c) upper bound» (the fraction and exponent are restored from the layout; the text layer reads «O((1 + nc )c )») |
| Rutkowski, «Two-player reachability-price games on single-clock timed automata», arXiv 1107.1199 (EPTCS 57, QAPL 2011) | abstract; Theorem 19 PDF p.13 | «we develop a theory of cost functions» … «an EXPTIME algorithm for computing the optimum reachability price». Theorem 19 (termination): «the number of iterations in each case is bounded by the number of all the possible intersections of the cost functions». Not a strategy improvement; no step bound of the kind asked |
| Cadilhac, Casares, Ohlmann, arXiv 2110.07346 v3 (re-opened, read §2-§4.1, App. A.3 heading, App. B.2, App. C) | §2 PDF p.4-6 (En+ p.4, simple games p.5); §3.1-§3.2 PDF p.6-7, Algorithm 1 and Theorem 4 p.7; §4.1 PDF p.10-11, Algorithms 2, 3, Theorem 11 p.11; App. B.2 PDF p.27; App. C PDF p.29; §6 PDF p.17 | En+: «En+(w) = Σ_(i < k_neg) w_i», «k_neg = min{k \| w_k < 0} … the first index of a negative weight». «A game is simple if all simple cycles have nonzero sum.» Potential reduction: «w_φ(vv′) = w(vv′) + φ(v′) − φ(v)». Theorem 4: «Let Ψ be a sound and complete potential assigner. Then Algorithm 1 terminates in at most n²W iterations, and returns Φ = En_G.» §4.1: «the potential assigner Ψ_En+(G) = En+_G. We call it the Positive path iteration algorithm (PPI)»; «computing En+-values in G corresponds to solving a variant of the energy game which stops whenever N is reached»; Theorem 11: «Algorithms 2 and 3 both compute En+_G, and both can be implemented to run in O(m + n log n) operations.» App. B.2: OSI's update game has «a sink state ⊥ to which Max can retreat at any point»; «we see PPI as a polished and streamlined version of Schewe's algorithm». App. C: «QDPM and PPI perform a linear number of iterations» on «the family of examples proposed by Friedmann [17]» («# states = 21N»); PPI-alt 2 iterations: «the dual algorithm immediately attracts the whole game to the single negative cycle» |

## 2. Robustness of «NEW»: the two orientations
### 2.1 What is published (KNOWN)
- Jurdziński–Trivedi's games: Min minimises and Max maximises the time to reach a final state; weights are elapsed times, so ≥ 0;
  values are pairs (T, D) (time, number of steps) compared lexicographically, which removes zero-time cycles (my reading of
  their §4). Algorithm 2 is
  all-switch strategy improvement for MIN with MAX's exact answer (computed by Algorithm 1). Lemma 19 states O(|R|) iterations for it.
- So «strategy improvement makes linearly many steps on a class of two-player non-negative-weight reachability games» is a
  published STATEMENT, in the MIRROR orientation, on timed region graphs. Their one-player Algorithm 1 (Max alone) has the bound
  |R| + 1, which is the Bellman–Ford-type bound of Cochet-Terrasson–Gaubert Theorem 2.3 again.
- About the proof sketch (READING; I checked no timed-automata detail). It is an induction on D, the step count of the optimal
  play. For a region owned by MAX in the two-player Algorithm 2 that hypothesis covers the lexicographically best successor only;
  another successor may have a larger D. The induction that does go through for finite games is on the lexicographic VALUE (§2.2).
  The paper says «analogous routine proof» and gives no more. I report the statement as published and the gap as a READING.
### 2.2 The MIRROR bound for finite games (IMPLIED: Lemma 19's idea + this argument; READING, unrefereed)
Setting: Statement ABS's games (target t, weights ≥ 0, no cycle of weight 0). µ_0, µ_1, … Howard for Min; V_j the exact value under
µ_j (Max answers; ∞ if Max can avoid t); opt the optimal value. Standard facts: V_j ≥ opt and V_(j+1) ≤ V_j pointwise.
- Order the vertices of finite opt as v_1 = t, v_2, …, v_r with opt non-decreasing, and u before v whenever opt(u) = opt(v) and
  there is an edge v → u of weight 0 (possible: no zero-weight cycle).
- Claim: V_j(v_i) = opt(v_i) for all i ≤ j + 1. Induction on j. Let v = v_(j+2).
  - v is a Max vertex. opt(v) = max over edges (v, y) of w + opt(y), so every successor y has opt(y) ≤ opt(v) − w and comes before v
    in the order: V_j(y) = opt(y). Max's exact answer gives V_j(v) = max(w + V_j(y)) = opt(v). Settled already at state j.
  - v is a Min vertex. Its optimal successor y* comes before v: V_j(y*) = opt(y*). Howard picks y′ with w(v, y′) + V_j(y′) = min ≤
    w(v, y*) + opt(y*) = opt(v), and ≥ opt(v) because V_j ≥ opt. Then V_(j+1)(v) = w(v, y′) + V_(j+1)(y′) ≤ w(v, y′) + V_j(y′) = opt(v).
- So after at most r − 1 ≤ n − 1 steps every value is optimal; then no Min vertex has a strictly better edge and Howard stops:
  at most n − 1 steps. This IS Dijkstra's order: a Max vertex settles when all its successors have, a Min vertex one step after its best successor.
  It is the invariant of Cadilhac–Casares–Ohlmann's Algorithm 2 («let v ∈ F_Max^(<∞)», then «let v ∈ F_Min^(<∞) minimizing …»).
- DATA (docs/lit/T69-mirror-check.py, sha1 in the commit; unit: Howard run from a random start; own engine): `rand 1 1500 7 7`,
  `rand 2 20000 12 0`, `rand 3 5000 40 0`, `rand 4 2000 120 0` (random games with 3 … NMAX vertices, weights 0, 1, 2, 4, 8, 16, 32,
  zero-weight edges only to a higher index): mono_m, bound_m (more than n − 1 steps), order_m (a vertex below the (j + 1)-th
  smallest optimal value not settled at state j), opt_m, and for the ABS run mono_a, opt_a: all 0. Runs are short (MIRROR at most
  10 steps, ABS at most 6): the sets test the logic state by state, not growth. Control: `ctrl 8` (below) fires order's test.
### 2.3 Why the argument fails in the ABS orientation (DATA + READING)
- In the ABS orientation values rise from below. A Min vertex takes the minimum over ALL its edges under current values, so one
  successor whose value is still too low holds it down, however early its optimal successor settled. Dijkstra's order is lost.
- Designed instance (`T69-mirror-check.py ctrl M`): a Min vertex v with edges v → t (10) and v → a_1 (0); Max vertices a_1, …, a_M
  with a_i → t (M − i + 1) and a_i → a_(i+1) (0) for i < M, a_M → t (100); start: every a_i → t.
  `ctrl 8`: «ABS steps 7, MIRROR steps 0»; optimal values v 10, a_1 100; «ABS: value of v per state [8, 8, 8, 8, 8, 8, 8, 10]»:
  v, the vertex with the second-smallest optimal value, reaches it at state 7 of 7. «Dijkstra-order violations: ABS run 5 …
  MIRROR run 0». `ctrl 30`: ABS steps 29. (One-player-like chain, so the step count is still below n.)
- This is the content of box 208's potential: it does not follow final values; it follows the lowest CURRENT value among the
  vertices not yet final, and pays (edges of Max)·(vertices) instead of n − 1.
- I found no example with more than n ABS steps (none searched beyond the random sets: gt_n_a = 0), and no proof that n suffices.
### 2.4 Verdict table (supersedes the ABS rows of T69 §3 and T69-summary §1)
| statement | label | by what |
| --- | --- | --- |
| all-switch strategy improvement, MIRROR orientation, two-player reachability-time games: O(\|R\|) steps | KNOWN (a published statement with a proof sketch) | Jurdziński–Trivedi Lemma 19 |
| the same for finite shortest-path games with weights ≥ 0 and no zero-weight cycle: ≤ n − 1 steps | IMPLIED (source + §2.2) | Lemma 19's idea; Dijkstra-order induction; DATA §2.2 |
| ABS orientation (box 208 §10): ≤ (edges of Max)·(vertices) steps by the lowest-lagging-value potential | NEW (searched: T69 §6 plus today's three papers), weakly | no source; the MIRROR induction fails there (§2.3) |
| «Dijkstra's order of settling holds for Howard» | true in MIRROR (§2.2), FALSE in ABS orientation | `ctrl 8` |
| a step bound for Schewe's OSI or for PPI | not published; open in both papers | Schewe p.14; Cadilhac–Casares–Ohlmann Question 19 |

## 3. Box 208's LEVEL potential against PPI's Dijkstra potential (READING; quotes in §1)
### 3.1 The two objects
| | PPI (Cadilhac–Casares–Ohlmann §3-§4.1) | box 208 (LEVEL / ABS) |
| --- | --- | --- |
| input | an energy / mean-payoff game, integer weights of both signs, simple | Γ(G) with the VJ valuation; at class level a shortest-path game with weights ≥ 0 |
| what iterates | the GAME: G ← G_φ with φ = En+_G, until φ = 0 | the STRATEGY of Even: Howard's all-switch step, Odd answers |
| «potential» | φ = En+_G : V → N∞, a vertex labelling COMPUTED each round by a two-player Dijkstra pass (Algorithms 2 / 3) | Φ_t = (m_t, −\|FRONT_t\|), ONE pair per state, defined from a reference state b; an ANALYSIS quantity, never computed by the run |
| what is counted | rounds; bound n²W (Theorem 4); lower bound open (Question 19) | Howard steps; bound P = 2M(N + 2M) non-stall steps (LEVEL), plateaus by PLATEAU |
| role of weights ≥ 0 | inside a round only (the play stops at the first negative edge) | throughout, at class level (E-DOM) |
### 3.2 Is LEVEL a statement about PPI's potential under Howard's rule? No. What is true instead
- (S1) Same game, one round. The En+ game of a simple game G is a shortest-path game in ABS's sense: target = the set N («vertices
  from which Min can ensure to immediately see a negative» edge), only non-negative edges are played before N, Max maximises and Min
  minimises the sum, and there is no zero-weight cycle because G is simple. Its value is PPI's potential φ.
- (S2) Two ways to compute φ. PPI: one label-setting pass, O(m + n log n) (Theorem 11). Howard for Max on the same game: Statement
  ABS (if it survives its referees) bounds the steps by (edges of Max)·(vertices). Same fixed point, different routes.
- (S3) The routes differ in order. The pass settles vertices in Dijkstra's order (§2.2 is that order). Howard in the ABS orientation
  does not (§2.3). So LEVEL's potential is not «the pass's potential read along Howard's run»: the pass has n settling events, one
  per vertex, in the order of final values; LEVEL has up to (edges of Max)·(vertices) values of (m_t, −|FRONT_t|), ordered by
  CURRENT values of lagging vertices.
- (S4) What LEVEL and the pass share is one inequality: with weights ≥ 0, the lowest value among the unfinished vertices cannot be
  undercut from the unfinished part. In the pass it is the greedy invariant; in LEVEL it is (L3) (the play of a front vertex stays
  at class ≤ m_t and meets a non-lagging vertex or a cycle inside the front).
### 3.3 What transfers, and what does not
| direction | transfers | does not transfer |
| --- | --- | --- |
| LEVEL / ABS → PPI | (S1)-(S2): a step bound for computing ONE round's potential by Howard. Of no use to PPI, which has the pass | anything about the number of ROUNDS: ABS concerns one game with weights ≥ 0; rounds range over G, G_φ1, G_(φ1+φ2), … with weights of both signs |
| PPI → LEVEL | the greedy invariant as a proof idea (S4); the remark that a second component (path length) is the standard way to break zero-weight ties (OSI's ⊥ and potential adjustments; VJ's (Π, k) on Γ(G)) | Theorem 11's proof cannot be cited for LEVEL: other orientation of progress (labels from above, one pass) and no strategy sequence; Theorem 4's n²W is pseudopolynomial and about rounds |
| Question 19 → LEVEL | nothing formal. A superpolynomial family for PPI would be an energy game with signed weights needing many rounds: not a genome game under Howard | it would not refute LEVEL; a polynomial bound for PPI would be far stronger than box 208 (it would solve mean-payoff games) and LEVEL is no step towards it |
| LEVEL → Question 19 | nothing formal. (A2) of T69 §1 (class-level weights ≥ 0, Odd decided at class level) is exactly the case in which a label-setting pass finishes the class level in ONE round | no family, no bound |
- One factual contact (PROVED-in-source for the quotes; READING for the comparison): on «the family of examples proposed by
  Friedmann [17]» PPI makes linearly many rounds (App. C, experiments), while Howard is exponential on Friedmann's G_n ([F11]
  Theorem 6.14). So iterating the Dijkstra potential and iterating Howard's step differ exactly on the games that violate E-DOM
  (T66); on E-DOM games box 208 claims Howard is polynomial as well. I did not check which of Friedmann's families the 21N-state
  instances encode, so this is a pointer, not a comparison on one fixed game.
- PPI-alt (the alternating variant) needs 2 rounds there because «the dual algorithm immediately attracts the whole game to the
  single negative cycle» (App. C). That is the 1-sink structure seen from the other player, the same asymmetry as §2 (the
  orientation in which the minimiser moves is the easy one).
### 3.4 Leads for the designers (D18; READING, no claim)
- LEVEL's P-factor is the price of running Howard at class level instead of a label-setting pass. A step that evaluated classes by
  one two-player Dijkstra pass (Schewe's «optimal improvement», PPI's round) would settle the class level of an E-DOM game at
  once. This is not a route to M4 by itself: Schewe leaves the number of updates open and Cadilhac–Casares–Ohlmann cite an
  exponential family for OSI (Friedmann's thesis §4.6.2, not opened by me).
- In the MIRROR orientation the class level would settle in Dijkstra's order (fewer steps than vertices, §2.2) IF facts
  like (K1)-(K5) hold for a run in which Odd improves and Even answers on Γ(G). Not checked; a question for L-NEW, since N5 is a
  symmetric rule and R54 (P-N5-DUAL) relates the two sides.

## 4. Limits
- §2.2's argument and §3 are READINGS by a literature lane; nobody refereed them. §2.2's DATA is one engine, short runs.
- Jurdziński–Trivedi's timed setting (values are functions on regions) was not checked; Lemma 19 is quoted, not verified.
- NOT OPENED: the ICALP 2007 conference version of Jurdziński–Trivedi; Friedmann's thesis §4.6.2 (today); Benerecetti et al.
  (QDPM); Khachiyan–Gurvich–Zhao CSR 2006; Hansen–Kaplan–Zwick SODA 2014.

## DONE / FINDINGS / NEEDS
- DONE: this note; docs/lit/T69-mirror-check.py; T69 Addendum A (the all-switch scope line and the pointer to §2); summary update.
- FINDINGS:
  1. Hidden step bound FOUND, in the MIRROR orientation only: Jurdziński–Trivedi Lemma 19 (O(|R|) iterations; proof sketch).
     For finite games ≤ n − 1 steps by a Dijkstra-order induction (IMPLIED; READING).
  2. ABS orientation: still NEW (searched). The MIRROR induction fails there (`ctrl 8`: the second-smallest value settles last).
  3. Schewe CSL 2008: number of updates left open (p.14). Rutkowski: not a strategy improvement.
  4. LEVEL ≠ PPI's potential under Howard. Same one-round game (S1); PPI solves it in one pass, ABS bounds Howard's steps on it;
     nothing transfers between LEVEL and the number of PPI rounds (Question 19) in either direction.
- NEEDS: Lead: relay finding 1-2 to the box-208 checkers and to L-NEW (a citation for «strategy improvement is polynomial on
  non-negative shortest-path games» must name the orientation; Lemma 19 is the mirror); decide whether §3.4's second lead (the
  Odd-improves run on Γ(G)) is worth a designer's box. Owner: nothing.

## Addendum A (2026-11-12, date -u in the commit; append-only): lead 7 (b) from the literature side — is Dijkstra-order settling for the Odd-improving half of a dual or symmetric strategy improvement published? (Lead 14:25Z, its clock)
Sources opened for this addendum: Schewe, Trivedi, Varghese, «Symmetric strategy improvement», arXiv 1501.06484 v1 (ICALP 2015
version: DOI 10.1007/978-3-662-47666-6_31, not opened); van Dijk, Loho, Maat, arXiv 2309.02223 (re-opened); §1's sources.
«Baier et al.» (your message): I found no paper of Baier on symmetric or dual strategy improvement, neither in my searches nor in
the reference lists of these two papers; nothing opened under that name.
| question | label | by what |
| --- | --- | --- |
| the minimiser improves against the maximiser's exact answer, non-negative-weight reachability games: settling in the order of optimal values, linearly many steps | KNOWN (statement, proof sketch) on reachability-time games; IMPLIED for finite games | Jurdziński–Trivedi Lemma 19; §2.2 above |
| symmetric strategy improvement, once ONE player's strategy is optimal: at most linearly many further iterations | KNOWN as a statement, no proof in the opened version | Schewe–Trivedi–Varghese Theorem 3.7 (PDF p.7): «The difference in the number of iterations of Algorithm 5 and Algorithm 6 is at most linear in the number of states of G.» (Algorithm 6 stops as soon as Prof(σ) or Prof(τ) is empty) |
| symmetric strategy improvement on Friedmann's 1-sink games: polynomially many steps | KNOWN as an informal argument + experiments | the same paper §4 (PDF p.9-10): «Player Min will move to the right in the j most significant positions after 2j improvement steps»; «We have not formalised these arguments on other instances»; abstract: «symmetric strategy improvement defies Friedmann's traps» |
| symmetric strategy improvement on sink parity games in general: a polynomial bound, or any settling order | CONTRADICTS (for the symmetric rule) | van Dijk–Loho–Maat Theorem 1 (PDF p.2): «the number of iterations of symmetric strategy improvement in parity games, mean payoff games and discounted payoff games is exponential … independently of the improvement rule»; p.3: «The key insight here is that the optimal counterstrategy to a bad strategy can also be a bad strategy itself.» Their games are sink parity games (Definition 2, PDF p.4) and violate E-DOM (T66 Addendum C) |
| the Odd-improving half settles in Dijkstra's order on VJ-type games with non-negative class-level weights (E-DOM games, Γ(G)) | NEW if proved; NOT FOUND (searched: these two papers and their reference lists by title, T69 §6, T70 §1) | – |
| alternating / dual potential iteration (PPI-alt): termination | OPEN in its source | Cadilhac–Casares–Ohlmann Question 18 («Do alternating fast value iterations terminate over simple games?»); 2 rounds on Friedmann's family (App. C) |
READING (what the three published mechanisms are, and which could serve N5):
- Jurdziński–Trivedi: value order. The improving minimiser settles vertices in the order of their optimal values because the
  maximiser's answer is exact and weights are ≥ 0 (§2.2). This is the only Dijkstra-order statement found, and it is one-sided
  (the other player does not improve; it answers optimally to every strategy).
- Schewe–Trivedi–Varghese: guidance by the opponent's best response. A player switches only to edges that are profitable AND used
  by its optimal counterstrategy to the opponent's current strategy (Algorithm 6 line 5, PDF p.7: «σ_(i+1) := σ_i^P for P ⊆
  Prof(σ) ∩ σ^c_(τ_i)»; superscripts restored from the layout). Theorem 3.7 is the
  statement closest to «Odd improves against an optimal Even»: once Even is optimal, Odd's guidance is a fixed optimal strategy and
  Odd needs linearly many steps. The paper gives no proof and no order of settling; it is not a Dijkstra argument.
- van Dijk–Loho–Maat: the guidance itself can be bad while NEITHER player is optimal, on sink games, for every rule. So Theorem 3.7
  cannot be extended to «polynomially many steps before one player is optimal» on sink parity games.
- For N5 (a symmetric rule; R54 P-N5-DUAL): no published result gives Dijkstra-order settling for the Odd half on VJ games. The two
  usable facts are one-sided: (i) against an EXACT opponent and with weights ≥ 0 the improving minimiser is linear (Lemma 19, §2.2);
  (ii) against an OPTIMAL opponent strategy the symmetric rule is linear (Theorem 3.7, unproved in the source). Whether N5's Odd
  half on Γ(G) is in situation (i) at class level depends on fleet facts (analogues of (K1)-(K5) with the roles exchanged), not on
  literature. The exponential symmetric family does not live in the genome class (E-DOM fails, T66 Addendum C), so it does not
  decide the question either way.
Limits: Schewe–Trivedi–Varghese read in the arXiv v1 text (abstract, §3.1-§3.2, §4); the ICALP version may contain a proof of
Theorem 3.7 (not opened). I did not open the papers they cite for one-sided analyses beyond those already in T69 / T70.
