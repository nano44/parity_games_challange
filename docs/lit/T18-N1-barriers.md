# T18: gauntlet step 3 for N1 (Loff-Skomra IncreasingDiscountPI on parity-induced rewards) (L-LIT, 2026-10-18)

Asked by the Lead, 2026-10-18. The object is L-NEW's N1:
- the pseudocode is in docs/new/N1-disc-anneal.md (trunk);
- the step-2 data are in docs/new/N1-step2.md (claude/l-new 5366078; not yet on trunk);
- the killer sketch is in docs/new/N1-killer-sketch.md.

N1 has four parts:
- rewards r(v) = (−n)^pr(v);
- discounts γ_j = 1 − 2^−j for j = 1, 2, ...;
- in each phase, Howard (switch-all) strategy iteration for Even on the discounted game, warm-started at the previous phase's optimum, with Odd answering by an exact best response (Dantzig simplex);
- a stop on a verified region certificate.

Sources were opened by L-LIT in this session. PDFs are in the scratchpad, with sha256 prefixes recorded in notes/L-LIT.md. "p." means the printed or PDF page as stated. Quotes are verbatim from pdftotext, with superscripts restored where pdftotext flattened them. "L-LIT reading" marks interpretation.

**SUPERSEDED 2026-10-18 18:15Z:** N1 was killed on data (L-NEW 8ac5e5c, docs/new/N1-KILL.md) by the route of caveat 1. See docs/lit/T19-N1-kill-lit.md. Step 3 is moot; the text below is kept as the record.

**Verdict (step 3): SIGNED, with six caveats (§6).**
- No published lower-bound theorem covers N1.
- **The one framework that comes close is B8.** Friedmann's switch-all bound transfers to discounted Howard at one discount exponentially close to 1 (1106.0778 §9). N1 lies outside it only because of its warm-started schedule: B8's theorems fix the start strategy and a single discount. **This is the weakest point.**
- No source analyses the warm start. Both Loff-Skomra bounds hold "for any initial policies". Asadi-Chatterjee-Luo say explicitly that warm-starting "is not used in our analysis".
- Every quasi-polynomial and separator barrier (B1–B3, B16) is outside N1 by model. Those barriers say nothing about strategy-iteration algorithms.

## 1. Provenance: N1 is a known algorithm; what its authors prove and do not prove
- **Loff-Skomra, ICALP 2024 version, arXiv 2402.03975 v1** ("Smoothed analysis of deterministic discounted and mean-payoff games"):
  - Fig. 11 (p.36) is DiscountedPI: an inner loop of SwitchMax until Max's policy is a best response, and an outer loop of SwitchMin.
  - Fig. 12 (p.36) is "IncreasingDiscountPI(σ, τ) ⊲ (σ, τ) are any initial policies; γ ← 0; repeat γ ← (1 + γ)/2; (σ, τ) ← DiscountedPI(σ, τ, γ) … until (λ, u) solves the ergodic equation".
  - Thm 1.10 (p.11): "The greedy-all switches policy iteration rule combined with increasing discount factor solves random instances of deterministic discounted or mean-payoff games in polynomial smoothed complexity."
  - Thm 6.6 (p.36) gives halting, correctness and smoothed polynomiality. The proof of halting uses the Blackwell threshold. **No worst-case bound is given.**
- **Loff-Skomra, arXiv 2610.22149 v1** (15 Oct 2026, general graphs):
  - §7.4, Fig. 7.2 (p.45) is the same procedure. Its stop test is "until (σ, τ) are optimal in the mean payoff game", and DiscountedPI is "any procedure that … outputs a pair of optimal policies" (p.44).
  - Thm 7.9 (p.42): if r ∈ P^{σ,τ} and 1 > γ > 1 − 1/(4n²Δ(r)), then (σ, τ) is the unique optimal pair.
  - Thm 7.14 (p.45): if r ∈ U (generic weights), Howard's rule makes O(m² + m²n⁴Δ(r)² log³(nΔ⁺(r))) switches and Dantzig's rule makes O(m³n³log²n + m³n⁵Δ(r)·log²n·log²(nΔ⁺(r))) switches.
  - The proof of Thm 7.14 bounds each phase by Thm 7.12 ([AG13], Howard) and Thm 7.13 (Dantzig). Both are **start-independent**.
  - Definition 5.7 (p.30): Δ(r) = ‖r‖_H / sl(r), where sl(r) is the slack of the optimal cone.
- **N1 against Fig. 7.2 (L-LIT reading).** N1 is IncreasingDiscountPI up to three differences:
  - (a) the players' roles in DiscountedPI are mirrored: in N1 Odd (Min) best-responds and Even (Max) switches all, where in Fig. 11 Max best-responds;
  - (b) the inner best response uses Dantzig's rule (the Thm 7.13 option, only for the best-responder);
  - (c) the stop test is a region certificate, not mean-payoff optimality. It can stop earlier, never later than the parity-correct optimum. On parity rewards the stop test does not change the phase work bound.
  - With these differences, a worst-case result for Fig. 7.2 with Howard would transfer to N1 only up to the mirror and the stop rule. None exists (§4).
- **Theorem 7.14 is uninformative on parity-induced rewards (L-LIT reading).** Two reasons:
  - (i) It needs r ∈ U. Parity rewards sit on vertices, so every out-edge of a vertex carries the same weight. Ties between optimal successors are common in parity games. Such r lies on a cone boundary (Def. 5.7 gives Δ = ∞) or outside U, and then the bound says nothing. Halting and correctness still hold: the proof of Thm 7.14 uses only Prop. 7.11.
  - (ii) Even for generic r, ‖r‖_H ≈ 2n^d while sl(r) can be O(n^0), so the bound is n^Θ(d). This is an upper bound being large, not a lower bound.
- **N1's own ceiling: N1 is in the n^O(d) class.** HMZ Thm 6.5 (any start) together with LS Thm 7.9 gives O(m·n^(d+2)·d log n) Even switches (L-NEW's argument, docs/new/N1-step2.md "Ceiling"). L-LIT checked both theorem statements against the opened PDFs: they match. So any counterexample needs d → ∞ and a long late phase.

## 2. (i) Strategy-improvement lower bounds: what transfers to discounted Howard, and to warm-started schedules
| source (opened) | statement | discounted? | what is fixed | covers N1? |
| --- | --- | --- | --- | --- |
| Friedmann, LMCS 7(3:19), arXiv 1106.0778 v2, Thm 6.14 (switch-all), Thm 8.4 (switch-best) | exponential on 1-sink parity games G_n | §9: yes, at ONE discount β_G = 1 − 1/(4·\|V\|³·max\|r(v)\|) with r = (−\|V\|)^Ω (p.35; pdftotext -raw gives "4 · \|V \|3"). Thm 9.5 [Vög00]: improving switches of G are improving in H = IndDPG(IndMPG(G)). Lemma 9.6 and Lemma 9.7 (1-sink) give Thm 9.8 (ϱ_σ = τ_σ). Cor. 9.9: valuation orders coincide. Cor. 9.10 (p.39): "Puri's algorithm … requires exponentially many iterations in the worst case when parameterized with the locally or the globally optimal policy" | start ι_G; all of §9 assumes "σ … s.t. Ξ_ιG ⊴ Ξ_σ", i.e. strategies reachable from Friedmann's start; one discount | **No.** It covers N1's last phase only from a cold start (L-NEW's ablation reproduces it exactly). N1's last phase starts from the γ_{J−1} optimum, which is not reachable-from-ι_G by construction. Earlier phases have γ_j < β_G, where nothing transfers |
| Fearnley, ICALP 2010, arXiv 1003.3418 v1, Thm 17 (total reward), Thm 18 (average reward) | ≥ 2^n Howard iterations on an MDP | no; undiscounted only (abstract: "total reward and average-reward optimality criteria") | start π_∅; stochastic MDP | no: stochastic one-player, fixed start, no discount |
| Hollanders-Delvenne-Jungers, CDC 2012 (not opened; publisher). Result opened in Hollanders PhD thesis, UCLouvain 2015 (author copy), Thm 2.18, printed p.48 | "an infinite family of discounted-reward MDPs with a particular starting policy and a discount factor γ = 1 − 2^(−Ω(n²)) on which the number of iterations that Policy Iteration takes is lower bounded by Ω((2^(1/7))^n)". Restated in Hollanders-Gerencsér-Delvenne-Jungers arXiv 1410.7583 v1 p.1: "Ω(2^(n/7)) … for the discounted-reward criterion [HDJ12]" | **yes**, at one discount exponentially close to 1 | particular start; stochastic MDP (Fearnley's example) | no: one-player stochastic, fixed start, one discount. It is the MDP analogue of Friedmann §9 |
| Zadeh: Disser-Friedmann-Hopp arXiv 1911.01074 v2, Thm 6.18 | exponential for Zadeh with the tie-break of Def. 6.4 | VJ parity SI / MDPs (Thm 6.18 items) | fixed tie-break and start | no: single-switch rule, not Howard |
| Cunningham: Avis-Friedmann arXiv 1305.3944 v1, Thm 4 | ≥ 2^n "from the initial strategy … using the ordering (1)" | no | ordering and start | no: single-switch rule |
| Random-Facet / Random-Edge: FHZ errata arXiv 1410.7871 v1 p.1 ("The main result of [1] is thus flawed"); Random-Edge per Friedmann thesis Thm 4.76 (predecessor's record, 2026-10-14) | randomized rules | no | — | no: N1 is deterministic Howard |
| Howard on deterministic MDPs (Hansen-Zwick ISAAC 2010, not opened; via Asadi-Chatterjee-de Raaij arXiv 2506.12254 v1, Thm 3.2) | "(n² + 7n − 6)/2 iterations" on a DMDP with 2n vertices; best known lower bound for Howard on DMDPs is polynomial (ICAPS 2025 PDF p.5: "only Ω(n) (Hansen and Zwick 2010)" for constant k) | mean payoff | — | irrelevant: polynomial; it bounds N1's inner one-player subproblem class from below only quadratically |
| Christ-Yannakakis arXiv 2212.00083 v1, abstract | "subexponential lower bounds (i.e., 2^Ω(n^c)) on the smoothed complexity of … Howard's Policy Iteration … for Markov Decision Processes … total reward and average reward" | no | stochastic MDPs | no: N1's games are deterministic. 2610.22149 §9 item 2 makes the same distinction |

**Answer to (i).**
- Friedmann (§9) and Hollanders et al. (Thm 2.18) do transfer to **discounted Howard at a discount exponentially close to 1**, but each fixes **one** discount and **one** start strategy.
- No opened source studies Howard along a schedule of discounts or from a warm start.
- A transfer to N1 would need a game in which the optimum at γ_{j−1} is (or behaves like) a bad start at γ_j. L-NEW's route (B) asks for exactly this, and no source builds one.
- Fact check against N1's numbers:
  - Friedmann's theorem needs 1 − γ ≤ 1/(4n³·n^d). At switchallexp N = 6 (n = 91, max priority 108) that means j ≥ log2(4·91^111) ≈ 724.
  - N1 stops at J = 697 < 724. So **L-NEW's ablation "at N1's final discount" lies below β_G**: its exact match with Friedmann's counts is data beyond the theorem's stated range, not an instance of Thm 9.5–9.8.
  - docs/new/N1-disc-anneal.md writes β_G = 1 − 1/(4|V|·max|r(v)|). The opened text has |V|³. This changes constants only (for L-NEW).

## 3. (ii) Hansen-Miltersen-Zwick and matching lower bounds for discounted strategy iteration
- **HMZ, arXiv 1008.0530 v1, Thm 6.5:** "The Strategy-Iteration algorithm, starting from any initial strategy, terminates with an optimal strategy after at most (m + 1)(1 + log_{1/γ}(n²/(1−γ))) = O(m/(1−γ) · log(n/(1−γ))) iterations."
  - Their Strategy-Iteration (Fig. 1, PDF p.9) is player 1 switching all, against player 2's optimal counter-strategy. That is exactly N1's phase.
  - §1 and §7 (PDF p.3, p.11): "strongly polynomial for a fixed discount factor, but exponential for non-discounted problems, or when the discount factor is part of the input" (citing Friedmann, Fearnley).
- **Matching lower bounds as a function of 1/(1−γ): none found.**
  - Friedmann §9 gives 2^Ω(N) at 1/(1−γ) = 4n³·n^d with d = Θ(N). So the count is only (1/(1−γ))^Θ(1/log n), far below HMZ's 1/(1−γ).
  - Hollanders Thm 2.18 likewise gives 2^(n/7) at 1/(1−γ) = 2^Ω(n²).
  - Hollanders et al.:
    - arXiv 1407.4293 (Order-Regular matrices) gives combinatorial bounds on PI for 2-action MDPs: p.2, and Thm 1 is a computer search.
    - arXiv 1410.7583 Thm 1 gives an upper bound O(k^n/n) with k actions per state. Its Thm 2 is tight only for the "pseudo-PI-sequence" relaxation (p.8: "only holds for pseudo-PI-sequences which are much less constrained").
    - Neither paper has a 1/(1−γ)-type lower bound.
  - Scherrer arXiv 1306.0386 and Post-Ye arXiv 1208.5083 v2 Thm 3.7 are upper bounds. Post-Ye: "O(n³m²log²n) iterations on deterministic MDPs with uniform discount using the highest gain pivoting rule", independent of γ. It is the basis of N1's inner loop.
  - Mukherjee-Kalyanakrishnan, ICAPS 2025 (ojs.aaai.org ICAPS article 36104, PDF p.2, Thm 1.2) gives a subexponential upper bound for Howard on deterministic MDPs with fixed reward bit-size and any discount. It also shows (PDF p.2) that beyond a threshold γ_Q Howard's trajectory no longer depends on γ. This is one-player only.
  - Feinberg-Huang arXiv 1312.6832 concerns value iteration, not PI (not N1's class).
- **Answer to (ii).**
  - HMZ's per-phase bound O(m 2^j j) is the best known for N1's phase j.
  - The best published lower bounds for discounted Howard (Friedmann §9; Hollanders Thm 2.18) are exponential in n at one discount exponentially close to 1, from fixed starts. They are far from matching HMZ in 1/(1−γ), and none bounds a warm-started phase.

## 4. (iv) Worst-case statements on increasing-discount or homotopy policy iteration
- **Anchor sentence: CONFIRMED verbatim in both papers.**
  - 2402.03975 v1 p.4 (§1.2) and 2610.22149 v1 p.5 (§1.2): "Otherwise, for mean-payoff games, or for discount factors γ exponentially close to 1, no upper-bound is known on the number of iterations, significantly better than the number of policies, which is exponential in the number n of states. More precisely, the best upper-bound on the number of iterations is 2^Õ(√n) [Hal07, HZ15]."
  - L-LIT note: the 2^Õ(√n) bound is for randomized (Random-Facet type) rules, not Howard.
- **2610.22149 §9 item 1** (p.52): "As in [LS24], our policy-iteration rule is not one of the standard rules … do these standard rules also have polynomial smoothed complexity". Nothing about worst-case behaviour on parity-induced inputs.
- **Later work: every citer of 2402.03975 checked** (Semantic Scholar API, 8 records, 2026-10-18; citations of 2610.22149: API 429, but that paper is 3 days old).
  - Asadi-Chatterjee-Luo, arXiv 2610.14150 v1, PDF p.24 "Comparison with [LS24]": "IncreasingDiscountPI2 warm-starts policy iteration from the policies computed at the previous discount factor, whereas Algorithm 2 restarts policy iteration from scratch at each threshold; this difference, however, is not used in our analysis." Their Lemma 11 is a worst-case bound for THEIR restart algorithm: N_iter(r) ≤ (⌈n ln n⌉ + 2)·n^n, which is exponential.
  - Allamigeon-Gaubert-… arXiv 2610.10295 v1 and Gaubert-… arXiv 2506.18545 v1: bounds on the Blackwell threshold, i.e. on N1's phase COUNT J, not on phase length. 2506.18545 p.4 cites [LS24] only for this use.
  - Ohlmann arXiv 2603.07555 v1 p.1: "no deterministic subexponential time algorithm is known for solving mean-payoff games". A new recursive algorithm, not PI.
  - Asadi-Chatterjee-de Raaij 2506.12254 (above): polynomial lower bound for Howard on DMDPs.
  - Loho-Maat-Skomra 2503.17294: see B19 below.
  - The other citers are the ICALP 2024 proceedings and an ICMS 2024 tropical paper (irrelevant).
- **Other searches.**
  - Web search on increasing-discount / homotopy PI worst-case bounds found nothing beyond the above.
  - The arXiv API for "policy iteration" ∧ "discount" ∧ "increasing" returned no hits (the export endpoint answered 301 over http; the https query worked for author queries).
- **Answer to (iv).** No worst-case lower or upper bound for increasing-discount or discount-homotopy policy iteration on mean-payoff or parity games exists in the opened literature. The only worst-case statement is the anchor sentence: no upper bound much better than the number of policies.

## 5. Barrier statement: N1 against B1–B17 (+ two rows missing from BARRIERS.md)
- **B1, B2 (separating automata, universal graphs; Czerwiński et al. arXiv 1807.10546 v2 Thm 5.1; CFGO arXiv 2104.05262 v8 Thm 4.1, Cor. 6.13).**
  - B1 is a size bound on "non-deterministic safety strong (n, d)-separator[s]". CFGO Cor. 6.13: "All algorithms based on separating automata, GFSG automata, or universal graphs, have at least quasipolynomial complexity", stated as "informal".
  - N1 keeps a positional strategy pair and exact rational values. It reads no priority sequence through an automaton and iterates over no universal graph.
  - **Outside, by model.** (iii) These barriers say nothing about strategy iteration: they constrain the state space of one fixed structure.
- **B3 (Arnold-Niwiński-Parys, LIPIcs.CSL.2021.9, Thm 5.1).**
  - The model is the value ‖F‖_{U,V} of a fixed-point expression computed with trees U, V fixed in advance. Its access to the game is the monotone one-step operator.
  - N1 evaluates no nested fixpoint. It solves linear systems (lasso sums) and compares valuations along edges.
  - **Outside, by model.**
- **B4–B7 (attractor families, Zielonka, Two Counters, partial solvers).** N1 is not attractor-based. B5–B6 are per-algorithm families: N1 ran on them in step 2 (polynomial-looking, data). B7: N1 is complete (step 2; LS Thm 7.14 halting).
- **B8 (named SI rules). N1's strategy-iteration framework.**
  - **Inside the framework, outside every theorem.** Every theorem fixes a rule, a start and (if discounted) one discount: §2.
  - The classical-SI escape also holds: a |V|-iteration rule exists (Friedmann LMCS Lemma 4.3), so no theorem covers all SI. Obs. 4.1 (p.12) of arXiv 2512.16684 v2: "any parity game with n player 0 states can be solved in linear time by some n-index-based improvement rule".
  - **Weakest point:** N1 is outside B8 only through its schedule. At its last discount and from a cold start it is inside (ablation).
- **B9 (Disser-Loho-Maat-Mosis arXiv 2512.16684 v2, Thm 4.3).** Covers single-switch "ℓ-index-based" rules with ℓ(m) = o(m/log m), and the paper's MDP model is expected total reward (p.6). Howard is multi-switch and valuation-based, so **outside**.
- **B10 (randomized SI).** N1 is deterministic: **outside**.
- **B11 (symmetric SI, van Dijk-Loho-Maat arXiv 2309.02223, Thm 1).** It covers parity, mean-payoff and discounted payoff games, "independently of the improvement rule", but for Schewe-Trivedi-Varghese symmetric SI. In N1 Odd plays exact best responses, not the symmetric scheme. **Outside.**
- **B12 (Fearnley-Savani arXiv 1507.04500 v4, Thm 1.2).** "EdgeSwitch for Vöge and Jurdziński's algorithm is PSPACE-complete". p.1: "for discounted … games our results apply to the standard strategy improvement algorithms". This applies to ONE N1 phase (discounted Howard), with the discount part of the input. It is hardness of predicting the run, **not an iteration bound**.
- **B13 (Lemke, Cottle-Dantzig; Fearnley-Jurdziński-Savani arXiv 0909.5653, Thm 18–19).** Pivoting on the LCP at a fixed discount. N1 does no LCP pivoting: **outside**.
- **B14 (AUSO).** N1's phase on a binary-choice game is Howard on a game-induced AUSO, and that AUSO changes with γ. The abstract-cube lower bounds do not transfer: ICAPS 2025 PDF p.5, "not all AUSOs are induced by MDPs; it remains unknown if exponentially-long chains are possible for HPI on 2-action MDPs". **Outside.**
- **B15 (IPMs), B16 (time-bounded weak separators), B17 (UP ∩ coUP, CLS).** Not applicable. B17 rules out nothing for a polynomial claim.
- **B18 (missing from BARRIERS.md; Howard-specific lower bounds outside parity games).**
  - Covers Fearnley's MDPs, Hollanders Thm 2.18, Christ-Yannakakis smoothed bounds, and polynomial DMDP bounds (2506.12254 Thm 3.2).
  - All are one-player and/or stochastic, at a fixed discount or undiscounted, from fixed starts. **Outside**: N1 runs on deterministic two-player games with warm starts.
  - Added to BARRIERS.md as B18.
- **B19 (missing from BARRIERS.md; linear-decision-tree representability, Loho-Maat-Skomra arXiv 2503.17294 v1, Thm 5.10).**
  - Statement: for some arenas, every LDT algorithm for mean-payoff games has representability measure RM(T_G) > 2^(c·m). §5 p.24 calls it "a first step towards proving a lower bound on the running time".
  - Prop. 5.5: strategy improvement with a fixed rule is an LDT algorithm. Each N1 phase compares linear forms in r with γ-dependent coefficients, so plausibly N1 is LDT too (L-LIT reading).
  - The theorem bounds only how far weights can be shrunk while preserving the tree's cone structure. It is **not a running-time bound**, and N1 already pays for n^d-size weights at bit cost. **Does not apply** as a barrier.

## 6. Verdict and caveats
**SIGNED, with caveats.** No published lower bound or barrier theorem covers N1:
- outside B1–B3 and B16 by model;
- outside B9–B14 and B18 by rule, determinism, symmetry or model;
- B12 and B19 are not iteration bounds;
- inside the SI framework (B8), but outside each of its theorems through the warm-started schedule.

Caveats (each could flip the verdict):
1. **B8 by schedule only.** At N1's final discount from a cold start, Friedmann's counter runs (data). Friedmann §9 and Hollanders Thm 2.18 show discounted Howard is exponential at one discount exponentially close to 1, from a fixed start. A family where the warm start IS a bad start (L-NEW route (B)) would put N1 inside B8's mechanism. No source rules this out.
2. **No upper bound beyond n^O(d)** (HMZ Thm 6.5 + LS Thm 7.9). LS Thm 7.14 is vacuous or n^Θ(d) on parity rewards (§1). Polynomiality rests on the DATA hypothesis (PHASE-POLY), which nothing in the literature supports or refutes.
3. **The anchor sentence is the literature's whole worst-case position** (§4). No paper studies warm starts. Asadi-Chatterjee-Luo state that their analysis does not use warm-starting.
4. **The ablation is beyond Friedmann's stated range.** N1's final γ_J is below β_G (J = 697 < 724 at switchallexp N = 6). The match with Friedmann's counts is empirical. Also: N1-disc-anneal.md's β_G formula should have |V|³.
5. **N1 differs from LS's Fig. 7.2** by mirrored roles, a Dantzig best response and a certificate stop (§1). A future lower bound for Fig. 7.2 must be checked against these before it is applied to N1.
6. **Bench caveat (L-NEW's own):** Friedmann's families are trivial from Odd's side. The step-2 bench was not built to produce a long late phase, which the ceiling says a counterexample needs.

## DONE / FINDINGS / NEEDS
- FINDINGS:
  - No published lower bound covers N1. The nearest are Friedmann 1106.0778 §9 (Cor. 9.10) and Hollanders thesis Thm 2.18: discounted Howard is exponential at ONE discount exponentially close to 1 from a FIXED start. N1 is outside them only by its warm-started schedule.
  - HMZ Thm 6.5 has no matching lower bound in 1/(1−γ). The known lower bounds are about (1/(1−γ))^(1/log n) (Friedmann) or 2^(n/7) at 1/(1−γ) = 2^Ω(n²) (Hollanders).
  - The anchor sentence is confirmed verbatim in both LS papers. No later work bounds IncreasingDiscountPI in the worst case. 2610.14150 says the warm start "is not used in our analysis".
  - LS Thm 7.14 needs generic weights (r ∈ U). Vertex-based parity rewards tie easily, so the bound can be vacuous on them.
  - Friedmann's β_G has |V|³ (L-NEW wrote |V|). N1's final γ_J is below β_G, so the ablation match is empirical, not Thm 9.5–9.8.
  - Two rows are missing from BARRIERS.md: B18 (Howard lower bounds on MDPs and DMDPs, smoothed) and B19 (LDT representability, LMS 2503.17294 Thm 5.10). Neither covers N1.
  - Step 3: SIGNED with caveats.
- NEEDS:
  - none from the owner. B18 and B19 were added to docs/lit/BARRIERS.md in the same commit (L-LIT file).
  - L-NEW (via the Lead): fix the β_G formula in N1-disc-anneal.md.
  - L-RED (via the Lead): attack route (B), a warm start that is a bad start, since caveat 1 is where a kill would sit.
