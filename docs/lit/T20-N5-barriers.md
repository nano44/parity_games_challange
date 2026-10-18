# T20: gauntlet step 3 for N5 "SSI-GLOBAL" (L-LIT, 2026-10-18)

Asked by the Lead at 20:51Z (Lead clock). The object is L-NEW's N5:
- spec and step-2 report: docs/new/N5-ssi-global.md (claude/l-new 8925171);
- proposal: docs/new/N4N5-proposals.md;
- code: experiments/new/n5.py.

All sources were opened by L-LIT in this session. sha256 prefixes are in notes/L-LIT.md. "p." is the PDF page; for 2309.02223 this equals the running head. "L-LIT reading" marks interpretation.

Name check: "DLM" is **van Dijk, Loho, Maat**, "The worst-case complexity of symmetric strategy improvement", arXiv 2309.02223 v1 = LIPIcs CSL 2024.24. The author copy tvandijk.nl/pdf/2024ssi.pdf has the same text. The Lead's message expanded DLM as "Deng-Li-Mo"; that expansion is wrong.

**Verdict (step 3): SIGNED WITH CAVEATS (§5).**
- No published lower-bound theorem covers N5.
- **DLM (B11) is the nearest.** N5 lies outside DLM's Algorithms 2 and 3 as defined: it can switch along edges outside both candidate sets. The data agree: N5 is polynomial on DLM's own families, which Lemma 12 forbids for every rule inside Algorithms 2 and 3.
- **The rule appears unpublished** (best effort, §3). Its nearest relatives are:
  - Schewe-Trivedi-Varghese's naïve symmetric algorithm (best response to the opponent's current strategy; it can cycle, per Condon);
  - SSI;
  - Schewe's globally optimal "switch-best" rule (Friedmann Thm 8.4).
- **Not a dead end.** No existing exponential lower bound applies.

## 0. What N5 is (from N5-ssi-global.md, read against the code description)
- **Even's step.** σ' is Even's optimal strategy in the arena where:
  - Odd is FIXED to its current τ;
  - each Even vertex v may use only A_σ(v) = {σ(v)} ∪ {w : (v,w) ∈ Iσ}, where Iσ is Vöge-Jurdziński's improving set for σ.
- **Odd's step** is symmetric.
- **Fallback.** One classical switch-all step, used when σ' = σ, τ' = τ and Iσ ∪ Iτ ≠ ∅.
- **L-LIT description.** N5 is STV's naïve symmetric update (σ ← best response to τ), restricted to the improvement arena, so that every step is a classical improvement. Equivalently, it is Schewe's switch-best ("best strategy in the improvement arena"), but evaluated against the opponent's CURRENT strategy instead of its optimal counterstrategy.

## 1. L-NEW's non-coverage argument against DLM, checked against the opened PDF (sha256 10e6794d82aba465…)
| L-NEW's citation | opened text | check |
| --- | --- | --- |
| improvement rule, p.5 | "an improvement rule, which is a function f : P(E) → P(E) that takes as input a set of improving edges, and outputs a set of improving edges subject to … If \|S\| > 0, then \|f(S)\| > 0. f(S) ⊆ S for all S ∈ P(E). Every node has at most one outgoing edge in f(S)." (p.5) | **correct** |
| SSI = Algorithm 2, p.7 | "3: I ← f((Iσ ∩ {(v, τ̄(v)) \| v ∈ V0}) ∪ (Iτ ∩ {(v, σ̄(v)) \| v ∈ V1}))", where τ̄ and σ̄ are optimal counterstrategies (p.7) | **correct** |
| generalized SSI = Algorithm 3, p.8 | "3: I ← f((Iσ ∩ Jσ(τ)) ∪ (Iτ ∩ Jτ(σ)))"; "Jσ(τ) = {(v, w) : v ∈ V0 ∧ Ξτ(w) ⊵ Ξτ(σ(v))}" (p.8). Lemma 6 (p.8): every (v, τ̄(v)) is in Jσ(τ), so Algorithm 3's candidates contain Algorithm 2's | **correct** |
| Theorem 1, p.2 | "exponential in the number of nodes and edges in the graph independently of the improvement rule. This holds for any of the currently used valuations in the literature." (p.2). It covers parity, mean-payoff and discounted payoff games | **correct** |
| Theorem 13, "p.14" | "Theorem 13. The results from Theorem 1 also hold for generalized SSI." is on **p.15**. Lemma 12 ("The results of Propositions 7 and 11 hold for any improvement rule f") is on p.14 | page slip (p.15, not p.14); content correct |
| p.3 quote | "one needs a different approach involving more than only local information to benefit from insights in the interplay of strategies for both players" (p.3) | **correct** |
| p.15 quote | "they can make too few crucial switches, as they are distracted by their opponent's (bad) strategy" (p.15, §7) | **correct** |

**Assessment of the two escape claims.**
- **(i) N5 can switch along an edge outside both candidate sets: AGREED.**
  - N5's choice at an Even vertex v is the best successor in the RESTRICTED arena against τ. That ranking is not the ranking by Ξτ, which is the valuation of τ against Even's unrestricted counterstrategy τ̄.
  - So the chosen w need not be τ̄(v), which escapes Algorithm 2. It also need not satisfy Ξτ(w) ⊵ Ξτ(σ(v)), which escapes Algorithm 3.
  - **Evidence that (i) actually happens.** Lemma 12 (p.14) argues that on DLM's families every rule f inside the candidate set takes at least as many iterations as SWITCH-ALL: "either there is only one switch possible, or every switch but one switch is irrelevant". Yet N5 needs 1, 2, 4, 4, 6, 7 iterations on family 1 and 2..13 on family 2, against SSI's 2^(n+1) − 3 and 7·2^(n−1) − 5. It used no fallback. So on those runs N5 must leave the candidate sets (data, single implementation).
  - The family transcription is validated by exact reproduction of Prop. 7 (2^(n+1) − 3) and of Prop. 11's count.
- **(ii) N5's choice is not a function of the candidate set alone: NOT an escape by itself (L-LIT reading).**
  - Lemma 12's proof argues only that at most one switch in the candidate set is relevant per iteration. That bounds ANY selection inside the candidate set, adaptive or not.
  - So the escape rests on (i) alone. The dependence on more than local information matters only through (i).
- **Mechanism risk (DLM §7, p.15) is NOT excluded.**
  - DLM: "the restriction imposed by using local information of the opponent's strategy might always be exploited to lure the iterations into an exponential trap"; "Our work leaves open if there is actually any way to use the interplay of strategies of the two players which does not end up with exponential worst-case running time" (p.15).
  - N5 is exactly a non-local use of that interplay. Its steps are steered by the opponent's CURRENT strategy τ, which can be bad: DLM's "distraction" mechanism.
  - DLM's construction does not cover N5, but its principle is the obvious attack line.

## 2. Barrier statement: N5 against each framework (BARRIERS.md B1–B20 and the Lead's list)
**Framework of N5.** Even's sequence σ0, σ1, … is a classical strategy-improvement run: every step applies a subset of Iσ (or a switch-all fallback), and DLM p.6 confirms "By [22], for any choice of improving edges, we have Ξσ′(v) ⊵ Ξσ(v)". The rule that picks the subset is adaptive: it depends on τ, which is extra state. The same holds for Odd. Hence:
- every classical-SI lower bound that fixes a rule says nothing unless N5's choices coincide with that rule;
- no barrier can cover ALL SI rules. Friedmann 1106.0778 Lemma 4.3 (p.7, [Vög00]) and thesis Cor. 4.79 (PDF p.207) show a ≤ |V|-step rule exists, and 2512.16684 Obs. 4.1 (p.12) shows a linear-time index-based rule exists.

| framework (opened source) | inside / outside / unclear for N5 | why |
| --- | --- | --- |
| **B8 switch-all**: Friedmann 1106.0778 v2 Thm 6.14; thesis Thm 4.41 (Gn, ≥ 2^n), Thm 4.44 | **outside** (unclear only through the fallback) | N5's step is not switch-all; data on switchallexp: 5..80 iterations (N = 1..40), 0 fallbacks. Caveat 3: if an adversary forces a fallback at every step, Even's run becomes switch-all from N5's state |
| **B8 switch-best** (Schewe's globally optimal rule = "best improvement over the whole game"): 1106.0778 §4 p.7 ("computes a globally optimal successor strategy in the sense that the associated valuation is the best under all allowed successor strategies", arena A_G,σ, p.5), Thm 8.4 (≥ 2^n on H_n from ι_Hn); thesis Thm 4.50 (PDF p.165) | **outside** | switch-best picks the best strategy in A_G,σ against Odd's OPTIMAL reply; N5 picks the best against Odd's CURRENT τ (and with strictly improving edges only, where A_G,σ also keeps equal-valued ones). These differ whenever τ is not a best response to σ', and in N5 it generally is not. Data on switchbestexp: 20..242 iterations (N = 1..32), about +6 per N, 0 fallbacks; switch-best doubles there |
| Fearnley 1003.3418 Thm 17–18 (Howard on MDPs); Hollanders thesis Thm 2.18 (discounted MDPs) | **outside** | Howard (switch-all) on one-player stochastic models from a fixed start; N5 is not switch-all and is two-player deterministic |
| **B10 Random-Edge / Random-Facet**: thesis Thm 4.76 (Random-Edge, ≥ 2^n expected), Thm 4.58 (Random-Facet 2^Ω(√n/log n)), Thm 4.78 (oblivious randomized rules); errata 1410.7871 v1 p.1 ("The main result of [1] is thus flawed", the Random-Facet parity bound) | **outside** | N5 is deterministic. Note: thesis Thm 4.58 predates the errata (2014); the Random-Facet bound on parity games is withdrawn (BARRIERS B10) |
| **Zadeh**: Disser-Friedmann-Hopp 1911.01074 v2 Thm 6.18 (specific tie-break); Disser-Hopp IPCO 2019 flaws (predecessor's record, 2026-10-14) | **outside** | single-switch, least-entered memory rule; N5 is multi-switch and valuation-driven |
| **Cunningham**: Avis-Friedmann 1305.3944 v1 Thm 4 (≥ 2^n "using the ordering (1)") | **outside** | single-switch round-robin; not N5 |
| "Melczer/Hansen-style best improvement over the whole game" | **outside**; no such separate result found | the only opened lower bound for a best-over-the-whole-improvement-arena rule is switch-best (row above). Melekopoglou-Condon 1994 (simple single-switch PI variants for SSGs) and Hansen-Kaplan-Zwick SODA 2014 (Dantzig on DMDPs) were NOT opened (publisher 403, T12). HKZ/Post-Ye concern single-switch Dantzig; 2610.22149 Thm 7.13 records Dantzig as polynomial on deterministic one-player discounted games |
| **B11 DLM** 2309.02223 Thm 1, Thm 13 | **outside as defined; mechanism unclear** | §1: N5 switches outside both candidate sets (i). DLM's distraction principle (p.15) is the natural attack and is not excluded |
| any lower bound for symmetric or best-response iteration | **none found** | STV 1501.06484 p.2: the naïve concurrent best-response update "has earlier been suggested by Condon [5] where it was shown that a repeated application of this update can lead to cycles"; p.12: "it was folklore that symmetric strategy improvement does not work". That is non-termination of the UNRESTRICTED naïve rule, not a lower bound; N5's restriction to improving edges restores monotonicity. Condon 1993 itself NOT opened. Dell'Erba-Dumas-Schewe 2404.04124 (LMCS 22(1), objective improvement, p.2 same Condon remark): a different symmetric method; its conclusion gives only "a trivial bound … the number of strategies (exponential)" |
| **B9 index-based** (2512.16684 v2 Thm 4.3) | **outside** | single-switch rules ranking edges by global index with o(m/log m) memory; N5 is multi-switch and uses valuations |
| **B12 PSPACE path prediction** (1507.04500 v4 Thm 1.2) | **not an iteration bound** | concerns switch-all |
| **B13 LCP** (0909.5653 Thm 18–19) | **outside** | no LCP pivoting |
| **B14 AUSO** | **outside** | N5 is not a path in one player's AUSO: its run moves both strategies and depends on the pair; abstract-cube bounds do not transfer (Matoušek-Szabó p.12, predecessor's record) |
| **B1–B3 separators, universal graphs, nested fixpoints** (1807.10546 v2 Thm 5.1; 2104.05262 v8 Thm 4.1, Cor. 6.13; LIPIcs.CSL.2021.9 Thm 5.1) | **outside, by model** | N5 keeps positional strategies and VJ valuations; there is no automaton product and no tree-driven fixpoint evaluation. These barriers say nothing about SI |
| **B4–B7** attractor / Zielonka / Two Counters / partial solvers | **outside** | not attractor-based; B5/B6 families were run in step 2 (polynomial-looking, data); N5 is complete (terminates optimal, Lemma 5 for sink games; regions verified) |
| **B15–B17** IPM, time-bounded weak separators, complexity classes | **not applicable** | — |
| **B18** Howard lower bounds outside parity games | **outside** | Howard/switch-all on MDPs |
| **B19** LDT representability (2503.17294 Thm 5.10) | **not a running-time bound** | N5 compares VJ valuations (priority sets), so the weight-size issue does not arise |
| **B20** increasing-discount PI (N1 kill) | **outside** | no discount; VJ valuations depend only on the priority order (N5 spec "Deep traps"; deeptrap data: 4..145 iterations, N = 1..40) |

**Cost check (TARGET §3).** Per iteration N5 does:
- two VJ valuations;
- at most two one-player optima, each one optimal-counterstrategy computation (polynomial: 1106.0778 Lemma 4.1 [VJ00] and Thm 4.2 [Sch08] for the related policies, p.6–7; VJ00 itself not opened);
- no big-number arithmetic.

So the cost is polynomial per iteration. Only the iteration count is open.

## 3. Is N5 (or an equivalent) already in the literature? Places checked
| place (opened) | finding |
| --- | --- |
| STV 1501.06484 v1 (ICALP 2015) | Alg. 2 "Naïve symmetric" (σ' = best response to τ, unrestricted; cycles per Condon), Alg. 3 SSI (Prof(σ) ∩ σ^c_τ). No restricted-best-response variant |
| DLM 2309.02223 v1 and tvandijk.nl/pdf/2024ssi.pdf (CSL 2024) | Alg. 2, Alg. 3 (above); §7 open question. No N5 |
| Friedmann 1106.0778 v2 §4, §8 and thesis (LMU 2011) §4.2–4.6, Thm 4.41–4.90 | locally and globally optimizing policies, Random-Edge/Facet, Zadeh, Switch-Half; no symmetric or two-player-steered rule |
| Oink README @ 8fbf0a7 (l.118–127) | "SSI … applies the principle of only updating strategies that are also the best response"; no global variant |
| Citers of 2309.02223 (Semantic Scholar: 2509.16075 Maat, 2503.17294 Loho-Maat-Skomra) and of 1501.06484 (14 records, incl. 2404.04124 Dell'Erba-Dumas-Schewe, 1607.01474 Hahn-Schewe-Turrini-Zhang) | grep for symmetric/SSI/best response: none defines N5's rule |
| Luttenberger 0806.2923 v4 (non-deterministic strategies; "locally optimal" successor), Friedmann-Lange 1006.1409 (local SI, alternating both players), Fearnley 1705.02313 (best-response computation), Mei-Sun-Ye 2606.29568, Křetínský et al. 2008.09465 (SSG algorithm comparison; Condon refs) | abstracts and greps: no N5 |
| arXiv API ("symmetric strategy improvement"; "strategy improvement" ∧ "best response"; "strategy iteration" ∧ "both players"; "strategy improvement" ∧ "parity games", 40 hits scanned); web search (extended) | only STV and DLM for symmetric SI; nothing on a restricted-best-response variant |
| NOT opened | Condon 1993 (DIMACS volume); Schewe CSL 2008 "optimal strategy improvement" (definition read via Friedmann 1106.0778 §4); Friedmann's snare-memorization lower bound (Fearnley's non-oblivious SI); Melekopoglou-Condon 1994; Hansen-Kaplan-Zwick 2014 |

**Conclusion of the search (best effort).** N5's rule is not in the opened literature, with or without a lower bound. It is a hybrid of STV's naïve symmetric update and Schewe's switch-best, and it sits in the direction DLM leave open (p.15).

## 4. (no existing exponential lower bound applies: nothing to report at once)

## 5. Verdict and caveats
**SIGNED WITH CAVEATS.** N5 is:
- outside DLM's Algorithms 2/3 by (i), with data consistent with it;
- outside every rule-specific SI theorem (switch-all, switch-best, Zadeh, Cunningham, Random-Edge/Facet, index-based);
- outside B1–B7 and B12–B20 by model or kind.

No opened source analyses or bounds N5's rule.

Caveats (each could flip the verdict):
1. **DLM's mechanism.** N5 is steered by the opponent's current, possibly bad, strategy, which is the "distraction" principle (2309.02223 §7, p.15). The authors conjecture traps exist for local uses of the interplay. N5 is non-local, but a DLM-style module that makes τ's restricted best response mislead Even is the obvious attack (L-RED / L-NEW killer item).
2. **The escape (i) is shown by data only.** That N5 leaves the candidate sets on DLM's families is inferred from Lemma 12 plus a single implementation (n5.py on L-SI's engine). A referee should confirm on one small instance (e.g. DLM family 1, n = 3) the iteration where N5's switch is outside Iσ ∩ {(v, τ̄(v))} and outside Jσ(τ).
3. **The fallback is switch-all.** A family that empties N5's selection at every step turns N5 into classical switch-all (inside B8, Friedmann Thm 6.14). Step 2 saw at most 4 fallbacks per N (counter_symsi, constant from N = 4), but no adversary has tried to force them.
4. **Even's projection is classical SI with an adaptive rule.** No theorem covers all rules, and good rules exist (≤ |V| steps), so "outside B8–B11" is structural, not evidence of polynomiality.
5. **Weak bench.** As for N1: the families were built against other algorithms; the deep-trap and padding families do not affect VJ-based methods.

## DONE / FINDINGS / NEEDS
- FINDINGS:
  - L-NEW's DLM quotes are correct (one page slip: Thm 13 is p.15).
  - Escape (i), switches outside both candidate sets, is real by argument, and the data on DLM's families plus Lemma 12 imply it occurs. Escape (ii), "not a function of the set", is not an escape by itself.
  - The nearest lower bounds are switch-best (Friedmann Thm 8.4; best over the improvement arena against Odd's OPTIMAL reply) and DLM; neither covers N5.
  - N5's rule is not in the literature (STV, DLM, Friedmann, Oink, citers, arXiv and web search). Its closest relatives are STV's naïve symmetric update (Condon: cycles) and Schewe's switch-best.
  - No existing exponential lower bound applies: not a dead end.
  - Step 3: SIGNED WITH CAVEATS.
- NEEDS:
  - Lead: route caveat 1 (a DLM-style distraction module against N5) and caveat 3 (forced fallbacks) to the adversary.
  - REFEREE: caveat 2 check (one instance).
