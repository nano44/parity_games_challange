# T14: published barriers vs L-SI's S7 "most-improved" rule (gauntlet step 3) (L-LIT, 2026-10-15)

Asked by the Lead at 13:27Z. The rule checked is from claude/l-si, docs/si/candidates/S7.md, "The rule, exactly":
- single-switch strategy improvement on the Vöge–Jurdziński valuation (Friedmann 1106.0778 §3);
- among improving edges e = (v, w), take one maximising count(e) = |{x : Ξ_{σ[e]}(x) ≻ Ξ_σ(x)}|;
- ties go to the ≻-largest Ξ_{σ[e]}(v), and then to the index (counted last resort);
- it is deterministic and memoryless, and costs O(n^2 m^2) word operations per iteration.

L-RED R3 (claude/l-red 7edf1c8, not re-read here, quoted from the Lead's brief): count = traffic through v (Lemma T), and upstream outranks downstream (Lemma D).

All sources were opened by L-LIT in T12/T14, and quotes were re-grepped. "p." is the PDF page unless marked "printed".

**Verdict: NOT COVERED.** No opened lower bound applies to S7, and no published rule of the "maximise the number of improved vertices / states" type was found, for games, MDPs or LPs. The closest published analogue is LargestIncrease (sum of value gains), which DLMM / Disser–Mosis defeat only on stochastic MDPs.

## (a) Published rule classes, one by one

| source (opened) | rule class | covers S7? |
| --- | --- | --- |
| Friedmann PhD thesis (LMU 2011), §4.2 Tables 4.1–4.2 (printed pp.94–95), §4.6.2 (printed pp.139–140) | SWITCH-BEST = Schewe's globally optimal rule: "Apply the best possible combination of switches … for every non-empty applicable subset of improving switches I … Ξ_{σ[I]} ⊴ Ξ_{σ*}"; properties "multi-switching, structurally involved, deterministic, oblivious" | **No.** Switch-best picks a *set* of switches whose resulting valuation dominates pointwise. S7 picks *one* switch by a *cardinality* (how many vertices improve), not by how much or by dominance. Friedmann's Thm 8.4 (1106.0778 p.33) relies on multi-switch timing |
| same thesis, printed p.93 | deterministic oblivious single-switch rules: "there is no particularly clever way to define [one], which is why they are not considered to be a good candidate" | no theorem; S7 is in this unanalysed class |
| Friedmann 1106.0778 Thm 6.14 / 8.4 | switch-all, switch-best | **No** (multi-switch) |
| Canavoi–Grädel–Rabinovich 1210.2459 v1, abstract (p.1) | catalogue of rules with Friedmann-type super-polynomial bounds: "switch-all (also with Fearnley's snare memorisation), switch-best, random-facet, random-edge, switch-half, least-recently-considered, and Zadeh's Pivoting rule" | **No.** No count-type rule. (Random-Facet is listed there before the 2014 errata) |
| Zadeh (1911.01074 Thm 6.18), Cunningham (1305.3944 Thm 4), Random-Facet*/Random-Edge (FHZ; errata 1410.7871) | history-based or randomized | **No** |
| Fearnley 1003.3418 Thm 17–18 | "greedy policy iteration, which selects the most appealing switchable action at every state" (p.4), multi-switch, MDPs | **No** |
| Melekopoglou–Condon 1994 | single-switch simple rules on MDPs (second-hand only) | **Unclear: NOT opened** (INFORMS 403) |
| DLMM 2512.16684 v2, Def. 3.4–3.7 (pp.10–11) | **Is S7 rankable?** Yes, trivially. count(·) and then Ξ_{σ[e]}(v) define a total preorder on the improving switches, so they form a neighbor ranking (Def. 3.4), and S7 is the greedy rule for it (Def. 3.5) with a Bland last resort. DLMM p.11: "Every deterministic memoryless pivot rule can be formulated as a ranking-based rule". So rankability alone carries no barrier; what matters is *which* rankings a theorem covers | — |
| DLMM Thm 4.3 (p.13) | {Bland}-ranking-based (index-only) rules, sink parity games | **No**, as long as count separates the switches. If the index last resort fired on a constant fraction of steps, S7 would approach an index rule on those steps. L-SI reports 0 firings on its families |
| DLMM Thm 5.3 (p.33); Disser–Mosis 2309.14034 Thm 1 (p.2) | {Bland, Dantzig, LargestIncrease} rankings; weak unichain **MDPs** with randomized actions | **No.** count is none of these rankings: LargestIncrease orders by the objective gain Σ_s ΔVal(s) (DLMM Obs. 3.6, p.10), S7 by #{s : ΔVal(s) > 0}. The setting is also stochastic |
| arXiv sweep (abstracts: "pivot rule" + "number of states"; "policy iteration" + "number of improved"; "strategy improvement" + "improvement rule"; pivot rule + lower bound + policy iteration) | — | no count-type rule found: hits were 1008.0530, 2309.14034, 2309.02223, 1210.2459, 2512.16684, 1911.01074, all checked above or in T12 |

## (b) Barrier statement (gauntlet step 3): S7 lies outside B1–B17 (docs/lit/BARRIERS.md)
- **B1, B2, B16 (separating automata, universal graphs, time-bounded weak separators).** S7 is not a safety or separating automaton reading priority sequences, nor value iteration over a universal graph.
  - Its state per iteration is a whole strategy plus valuations, and it uses the graph (paths, counterstrategies), not a priority stream.
- **B3 (black-box nested fixpoints, tree-driven).** S7 is not a tree-parameterised evaluation of a fixpoint expression by queries to f. Valuations are computed from the arena's paths, adaptively.
- **B4–B7 (attractor decompositions, Zielonka, priority promotion / tangles / "Two Counters", fatal-attractor partial solvers).** These are different algorithm families. S7 is a total algorithm, sound by standard strategy-improvement theory.
- **B8 (named deterministic SI rules).** S7 is not switch-all, switch-best, Zadeh or Cunningham: it is single-switch, uses no history, and has no round robin.
- **B9 (index-based rules, DLMM Thm 4.3).** S7 ranks by a valuation-derived count. It is outside **unless** the index last resort fires often; L-SI's counter of last-resort firings is the evidence that must stay near 0.
- **B10 (randomized: Random-Edge, Random-Facet*).** S7 is deterministic.
- **B11 (symmetric SI, van Dijk–Loho–Maat).** S7 is ordinary one-player-improves SI, not the Schewe–Trivedi–Varghese symmetric scheme.
- **B12 (PSPACE-completeness of predicting all-switches runs).** This concerns all-switches SI and is not an iteration bound.
- **B13 (Lemke / Cottle–Dantzig LCP).** S7 is not an LCP method.
- **B14 (AUSO lower bounds).** These are abstract cubes. S7 needs per-vertex valuations, which an AUSO does not provide, so those bounds are not even stated for it. They also do not transfer to games (B14 row).
- **B15 (IPMs).** Not applicable.
- **B17 (UP ∩ coUP, CLS).** Membership results, not barriers.
- **Beyond BARRIERS.md (from T12):**
  - DLMM Thm 5.3 and Disser–Mosis cover LargestIncrease only on stochastic MDPs, via probability-scaled gadgets. LargestIncrease is the nearest relative of S7, as S7.md itself says.
  - The deterministic-Dantzig positive results (Post–Ye, Zhong–Ye, Mei–Sun–Ye) are about a different ranking and constrain nothing here.

**What an S7 killer would have to do (L-LIT reading, from the DLMM index-based proof technique):**
- DLMM keep the number of improving moves constant with "controller" and "filler" gadgets (Fig. 4.2, p.16), so that an index-only rule's choice is forced.
- The S7 analogue would be gadgets that **equalise traffic** (Lemma T), so that the counter's intended switch always has the maximal count. That is L-SI's "padding" attack (S7.md (iii)).
- Lemma D (upstream counts more) is the obstruction: polynomial padding must beat the depth-induced count gap at every level.
- No published construction does this.

## (c) Verdict
**Not covered.** No published lower bound covers S7 or a class containing it. S7 falls in the class Friedmann's thesis calls deterministic oblivious single-switch rules, for which no theorem exists (printed p.93).

Caveats:
- Melekopoglou–Condon (1994) is unopened.
- S7's index last resort, if it fired often, would pull it toward B9.

## DONE / FINDINGS / NEEDS
- FINDINGS:
  - S7 is not covered.
  - Switch-best is multi-switch and dominance-based (thesis §4.6.2), not count-based.
  - No count-type rule appears in Friedmann's thesis, the 1210.2459 catalogue, DLMM, Disser–Mosis, or an arXiv sweep.
  - S7 is trivially rankable (DLMM p.11), but count is not Bland, Dantzig or LargestIncrease.
  - S7 lies outside B1–B17. The B9 boundary depends on the index last resort firing rarely.
- NEEDS:
  - L-SI (via the Lead): keep reporting last-resort firings.
  - L-RED: the traffic-equalising (padding) construction is the one attack the literature suggests.
  - owner: Melekopoglou–Condon only if S7 is to be claimed outside the fleet.
