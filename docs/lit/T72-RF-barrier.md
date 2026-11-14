# T72: DRAFT barrier statement for candidate RF («ROOT-FIRST»): gauntlet step 3, NOT SIGNED
L-LIT successor (design day, D27 / D28 / L61; Lead brief 2026-11-14 14:36Z, item 3; the brief's file name was «T-next-RF-barrier»).
Written 2026-11-14 (date -u in the commit). Working note, unrefereed. RF is a CANDIDATE under attack (D1). This is a draft: the
Lead's brief says «You do not sign off today; you say what is missing for a sign-off.»

**Status added 2026-11-14 19:06Z (date -u), after this draft was written.** RF is reported DEAD by the Lead (15:39Z, 19:05Z):
L-RED-B 8's family K^s_n, «RF makes exactly 7·2^(n−1) − 2n − 3 iterations for n = 2..15», «confirmed by L-SI's rebuild».
Fleet-internal, not checked by me. So this draft will not be signed; it is kept as the record. Its §2 item 1 («the adversaries need
one new ingredient, not a new framework») is what happened: the kill is a Friedmann-type counter with lowest-first re-closing.

Gauntlet step 3 (TARGET.md §5, the owner's text, verbatim): «A barrier statement: which known lower-bound frameworks it lies outside,
and why. L-LIT signs off.»
> A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below. (D1)

Sources and data: docs/lit/T71-RF-prior-art.md (quotes, sha256 prefixes, runs) and docs/lit/BARRIERS.md (rows B1-B21). Labels:
PROVED-in-source; DATA (docs/lit/T71-rf-trace.py, my reading of RF, one engine, unrefereed); READING (mine).

**Status: NOT SIGNED. Verdict of the draft, in four lines.**
- No published lower-bound THEOREM covers RF. Every theorem for one-sided strategy improvement fixes a rule, and RF is none of them.
- RF is NOT outside the FRAMEWORK those theorems come from (Friedmann's binary counters on sink games). One of its three
  ingredients, the reset, already works against RF as published (H_n). RF is polynomial on the published families only because a
  second ingredient, the index-ordered delay, fails under RF. That is a weaker position than «outside».
- RF has no claimed bound and no proof, in the two-player case or in the one-player case.
- «Outside all known frameworks» is true of every classical rule before its counterexample was built; for RF it is evidence of
  nothing yet.

## 0. The object and its class
RF as in the Lead's brief (T71 §1): memoryless, deterministic, one-sided VJ strategy improvement; switch-best exactly at the
improvable vertices in the sink strongly connected components of the dependency digraph of the play graph of (σ, σ̄).
- Class: an improvement policy in Friedmann's sense ([F] = arXiv 1106.0778 v2, §3 p.5-6). Correct and terminating for the same
  reason as every such policy ([F] Theorem 3.2; a sink component always exists, so every step switches at least one vertex).
- What the class can and cannot be told by a barrier: a policy with at most |V| iterations exists ([F] Lemma 4.3, non-constructive),
  so no theorem can cover all improvement policies. A barrier for RF can only be rule-specific or mechanism-specific.
- Two elementary facts (T71 §2.12; READING, unrefereed): ACYC, RF stops within #(Even choice vertices) iterations on a game that
  is acyclic apart from the sink (DATA: 5,500 random games); SCC-DECOMP, RF's run restricted to a successor-closed set is RF's
  run on that subgame, so RF's worst case lives on strongly connected games with a sink. Neither bounds RF on a hard instance;
  both say where a counterexample must sit (inside cycles of the game graph).
- Per-iteration cost (TARGET §3): valuations as in every VJ engine (n-bit path sets, comparisons at bit cost O(n)); the dependency
  digraph needs one play per improving edge, O(nm) vertex visits, and one component computation. Polynomial per iteration; the
  whole question is the number of iterations.

## 1. RF against each framework
| framework (BARRIERS row; source) | RF inside / outside | why; what the DATA says |
| --- | --- | --- |
| B1-B3 separating automata, universal graphs, black-box nested fixpoints (arXiv 1807.10546 Thm 5.1; 2104.05262 Thm 4.1; ANP Thm 5.1) | **outside, by model** | RF keeps positional strategies and VJ valuations; no automaton product, no universal tree, no fixpoint recursion. Worth nothing as evidence: every strategy-improvement rule is outside these, and the two classical ones are exponential |
| B4-B7 attractor / Zielonka / Two Counters / partial solvers | **outside** | not attractor-based. RF on tc / tc+ / recursive ladder is a battery question (L-COMP) |
| **B8 locally optimizing policy** ([F] Thm 6.14, G_n) | **outside the theorem; the family is defeated** | RF ≠ switch-all. DATA: G_n from ι in 3n + 3 iterations (n = 2..7); the reset of [F] Lemma 6.11 is cancelled (T71 §3 row 1) |
| **B8 globally optimizing policy** ([F] Thm 8.4, H_n; Schewe CSL 2008; Luttenberger) | **outside the theorem; NOT outside the mechanism** | RF ≠ Schewe's rule. DATA: on H_n the reset is NOT cancelled (bit i reopened n − i times, n = 2..7); RF = 7n² + 11n − 13 (n = 2..8), polynomial only because reopened bits re-close highest first (T71 §3 row 2, readings 1-3) |
| Snare memorization (Fearnley arXiv 1003.2976; Friedmann DAM 2013 preprint Thm 26) | **outside the theorem** | RF has no memory. Fearnley's strategy tree is RF's play graph; his back edges are RF's cyclic dependencies. DATA: resets survive on both PGSolver snare families, counts polynomial-looking for N ≤ 5-6 |
| B8 Zadeh (arXiv 1911.01074 Thm 6.18), Cunningham (arXiv 1305.3944 Thm 4) | **outside** | single-switch rules with memory / a fixed order. DATA: ports need ≤ 13 RF iterations at N ≤ 6; switch-all itself is fast there, so the families say nothing about multi-switch rules |
| B9 index- / ranking-based rules (arXiv 2512.16684 Thm 1.1, 1.2) | **outside, by definition** | the class is single-switch and decides «solely on the ordering of improving edges/variables by global index» (plus reduced cost and objective improvement in Thm 1.2); RF is multi-switch and reads the play graph. DATA: dlmm_bland in 1 iteration |
| B10 randomized rules | **not applicable** | RF is deterministic |
| B11 symmetric strategy improvement (arXiv 2309.02223 Thm 1) | **outside** | RF is one-sided; Thm 1 itself notes that the one-sided setting always has a linear rule |
| B12 PSPACE-completeness of all-switches path prediction (arXiv 1507.04500 Thm 1.2) | **not an iteration bound; not about RF** | proved for all-switches. Whether RF's run is as hard to predict is unknown; a polynomial bound for RF would make its EdgeSwitch problem polynomial |
| B13 LCP pivoting; B15 / B21 interior point | **not applicable** | no pivoting on an LCP, no path following |
| B14 unique sink orientations | **outside** | RF moves by a jump inside the cube of improving switches but chooses the jump from the play graph, which an abstract orientation does not have; abstract-cube bounds are not known to be game-realizable (B14) |
| B18 Howard on MDPs / discounted transfer (Fearnley arXiv 1003.3418; [F] §9) | **outside** | Howard = all switches. READING: Fearnley's MDP counter has G_n's simultaneous reset |
| B19 linear decision trees (arXiv 2503.17294) | **inside the model, no time bound follows** | a fixed-rule strategy improvement is a linear-decision-tree algorithm there (Prop. 5.5); the theorem is about weight compression, not running time |
| B17 complexity classes | **no obstacle** | a polynomial RF would put parity games in P; nothing known forbids that (UP ∩ coUP, UniqueEOPL) |
| Melekopoglou–Condon topological improvement (1994, Cor. 2.9) | **outside the theorem; the lesson applies** | other model (random vertices, single switch, whole-graph components). The lesson: ordering by component is void inside one component. For RF: whenever the improvable vertices are mutually dependent, RF IS switch-best-everywhere on them |
| Howard on deterministic MDPs (Hansen–Zwick Ω(n²); open upper bound; Zhong–Ye CLAIM) | **outside; no collision** | RF's one-player case is weaker than that open problem (T71 §2.10): VJ cycle nodes take ≤ n values per vertex |
| Fleet kills (P-N5-EXP / R131 pending, R130 wrapper family, L-RED R246 SCHEME-TIE) | **not literature; to be checked by their lanes** | the Lead's rows: Γ3(G_k) in 6 … 10 iterations. L-LOWER's barrier theorem («rules that cannot work») does not exist yet |

## 2. What RF is NOT outside (bluntly)
1. **Friedmann's counter framework.** A Friedmann counter has three ingredients (T37 §2): a hidden-profit gate per bit, a delay
   supply ordered by bit index, a one-step reset. Under RF:
   - gates: intact (the closing switch d_i → e_i is still chosen only when nothing better is left; Odd's reply still hides the
     exit; DATA: on G_n and H_n the bits close one at a time);
   - reset: G_n's is cancelled; H_n's is intact, by a mechanism published in 2011 for another purpose ([F] §8.1, §8.3: make the
     resetting event last two iterations with a delay node);
   - delay order: broken in H_n (T71 §3 reading 3), by RF's own dependency channels.
   Two of three ingredients work against RF today. The adversaries need one new ingredient, not a new framework.
2. **Bounded lookahead.** Schewe's rule looks one step ahead in VALUE and was beaten by making a profitable event last two steps.
   RF looks zero steps ahead in IMPROVABILITY: it sees vertices improvable now, not vertices that become improvable when another
   sink switches. The same delay node defeats that (DATA, H_n). READING: any rule that tests a fixed number k of such rounds is
   exposed to k + 1 delay nodes; a rule with unbounded foresight of improvability is a game solver.
3. **Component collapse.** RF equals the locally optimizing policy on any state whose improvable vertices form one component. The
   lane fact «decoy edges cannot merge components» is what separates RF from G_n-type bounds; it is unrefereed and I have not seen
   its statement. READING: in a sink game the plays are root paths of a tree, so the dependencies through σ(v) alone
   are acyclic (strict tree ancestors), and every cyclic dependency uses at least one improving edge whose target's root path
   contains another improvable vertex. With two vertices that is a profitable back edge in Fearnley's sense (v's improving
   target lies in v's own subtree, with u on the play between them) or a pair of crossing improving edges: the snare structure that Friedmann's counters are made of. DATA: on H_n the
   dependency digraph has a component of size > 1 at 3, 13, 29, 51 iterations (n = 2..5) and a SINK component of size > 1 at 1,
   2, 3, 4 of them; on G_n never.
4. **Intransitivity.** [F] p.7: «The reason why this proposition is incorrect lies in the intransitivity of optimality of strategy
   updates.» «RF never makes a switch that is stale now» does not compose over iterations; H_n is the witness.

## 3. What a proof of a polynomial bound would have to beat
1. **Its own lower bound on the published families.** DATA: RF needs 7n² + 11n − 13 iterations on H_n (21n vertices, n = 2..8),
   and bit i's cycle is reopened n − i times (n = 2..7). Any argument giving O(|V|) iterations, or O(1) reply changes per Odd
   vertex, or «no set bit is ever reset», is false. A potential must allow one reset per (gate, higher bit) pair and forbid
   cascades.
2. **The cascade.** The proof must show that lowest-first re-closing cannot be arranged against RF (T71 §4 (b)), in every game, not
   on the lane's and the literature's families. No published technique does this for any rule; the fleet's nearest tools (R118
   PATH / BR-SEG, λ-windows) rely on Howard's domination step, which a delayed vertex does not satisfy.
3. **The one-player case first.** Even with Odd trivial there is no proof: the O(n²) cap on substantial steps is free (VJ00
   p.213), the window between them is not. «About 3 iterations per vertex» is a climb result. A superpolynomial one-player run
   kills RF without any gate; a one-player proof is the smallest honest milestone and would itself be new (T71 §2.10).
4. **Parity-specific structure.** If the argument never uses a VJ-specific fact (cycle nodes take ≤ n values; path sets compare
   lexicographically), it applies verbatim to mean-payoff and discounted games and claims a strongly polynomial algorithm for them:
   a much larger claim than TARGET.md's and a warning sign in itself. The referees should ask where the proof stops working for
   mean-payoff weights.
5. **Tie rules and starts.** N5 died on its tie rule «for every tie rule» (Lead, L-RED R246). RF's «switch-best» needs a frozen
   tie rule for non-injective priorities and a statement for every start strategy; my runs use the engine's PGSolver tie-break and
   two starts only.
6. **The base rate.** Both earlier structural fixes of G_n (Schewe 2008; Fearnley 2010) were refuted by a modified counter
   (Friedmann 2011; 2013). RF is the third fix of the same family. Fearnley (arXiv 1003.2976 §9): «we are not claiming that
   simply terminating in polynomial time on Friedmann's examples is a major step forward».

## 4. What is missing for a sign-off
1. A frozen statement of RF on origin (file, SHA): tie rule, start, the exact meaning of «lies on the play» (path and final cycle,
   as I implemented), and whether Odd's reply ties are broken as in si.py. My script agrees with every number of the Lead's brief
   that I could compare (G_n n = 1..7; switchallexp 10 and 65 at N = 1 and 8; switchbestexp 17 and 106 at N = 1 and 8). Needed
   still: L-SI's engine on H_n ([F] Table 7), where my load-bearing DATA sits, and the intermediate rows.
2. The adversaries' reports on T71 §4 (a) + (b), from both lanes, with the instance that kills or the exact obstruction.
3. A refereed statement of «decoy edges cannot merge components» (§2 item 3), or its withdrawal.
4. A claimed bound for RF (none exists: gauntlet step 4 has no object yet) and at least the one-player proof (§3 item 3).
5. L-LOWER's barrier theorem, once stated, checked against RF's definition.
6. A second literature pass over what stayed unopened (Hansen's thesis §5-6 on rule lists and Conjecture 6.1.1; Hoffmann–
   Luttenberger ATVA 2013; Vöge's thesis; the Gauss–Seidel policy-iteration primaries; Madani's proofs), before any wording like
   «new rule» is used outside the fleet's notes. Owner-optional library items; nothing is asked of the owner now.
7. RF on the full battery with verified strategies (gauntlet step 2: L-COMP), since several rows above rest on one engine.

## DONE / FINDINGS / NEEDS
- DONE: this draft (not a sign-off).
- FINDINGS:
  1. No published theorem covers RF; RF is outside B1-B7, B9-B15, B18, B21 by model or by definition.
  2. RF is not outside Friedmann's counter framework: gates and (H_n's) reset work against it; only the delay order fails.
  3. A proof must be consistent with the quadratic count on H_n (DATA), must handle the one-player case without Howard's domination step, and must use
     parity-specific structure.
  4. Seven items are missing for a sign-off (§4); the first is a frozen statement of RF on origin.
- NEEDS: Lead: the frozen RF statement and full data rows (§4 item 1); route §2-§3 to the design and adversary lanes. Owner: nothing.
