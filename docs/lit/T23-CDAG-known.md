# T23: is L-NEW's CDAG_n (exponential single-switch VJ chain on a one-player game) known? (L-LIT, 2026-10-19)

Asked by the Lead (00:52Z). The object is CDAG_n (docs/new/N5-K9-Pstrict-counter.md, l-new de4b588):
- n+1 vertices, all owned by ⊕;
- priorities 2(n+1−v);
- edges v → every u < v; sink 0;
- from σ0 = "all → 0", there is a chain of 2^n − n − 1 single-switch VJ00 improvements, each Ω-strict.

The Lead re-ran it for n = 4..10. Fleet-internal only.

**L-LIT reading of the instance.**
- Every play ends in the sink 0, whose priority (2) is even and lowest, so every VJ value has cycle node 0.
- Values are then compared by the path set alone. All priorities are even (R+), so a set containing the higher-priority vertex is better (MaxDiff).
- So VJ improvement on CDAG_n is longest-path policy improvement on the complete acyclic graph with weights 2^(rank). It is a deterministic, acyclic, one-player instance, of the kind called "acyclic shortest paths" in the simplex literature.

## (1) Places checked
| source (opened; sha256 in notes/L-LIT.md) | what it shows | relation to CDAG_n |
| --- | --- | --- |
| Friedmann, Hansen, Zwick, "Random-Facet and Random-Bland require subexponential time even for shortest paths", arXiv 1410.7530 v1, abstract and §1 p.1–2 | "we obtain subexponential lower bounds for the running times of Random-Facet, Random-Facet1P and Random-Bland on LPs that correspond to standard acyclic shortest paths problems, the simplest form of deterministic 1-player games" (p.2); bounds 2^Ω̃(m^{1/3}) and 2^Ω̃(√m) expected improving switches; §9 p.33 open problems | **closest known form.** It is deterministic, one-player and acyclic, with single-switch rules and super-polynomially many improving switches, so long single-switch improving sequences exist on acyclic one-player games. Differences: shortest-path valuations with their own weights (not VJ on priorities); randomized rules and expected counts; subexponential, not 2^n − n − 1; no parity-game statement |
| Melekopoglou-Condon 1994 (ORSA J. Comput. 6(2); NOT opened, publisher 403 in T12), via Christ-Yannakakis arXiv 2212.00083 v1 §5 p.30 and Fearnley arXiv 1003.3418 v1 p.1 | simple, topological and difference single-switch policy iteration take 2^n − 1 steps (Fearnley p.1: "They give a family of examples upon which these policy iteration algorithms take 2^n − 1 steps"). The MDPs have **random vertices**: "The vertex 0′ has a random edge going to n with probability 1/2 …" (2212.00083 p.30) | close form: single-switch and exponential, but **stochastic** (one-player SSGs / MDPs with chance nodes), not deterministic, and under specific rules |
| VJ00 BRICS RS-00-48 §7 (printed p.27), CAV 2000 p.12 | VJ00 cite Melekopoglou-Condon as SSG examples and pose Problem 7.3: "Are there families of examples of parity games for which there exist strategy improvement policies of super-polynomial length?" | the authors treat the one-player parity case as polynomial (Prop. 7.4) and the existence of long policies as open; no example given |
| Friedmann PhD thesis (LMU 2011) §4.1, PDF p.100, Thm 4.9; Cor. 4.79 (PDF p.207) | one-player parity games: SWITCH-ALL polynomial ([Vög00]); every MDP has a short improving sequence (≤ n) | no remark on long single-switch sequences in one-player games |
| Friedmann 1106.0778, Fearnley-Savani 1507.04500, DLM 2309.02223, Post-Ye 1208.5083 (intro p.2: "Policy iteration … is conjectured to run in O(m) iterations on deterministic MDPs … a lower bound of O(m) is known [HZ10]"), Mei-Sun-Ye 2606.29568 p.4, Scherrer 1306.0386 p.4 ("a similar result does not seem to exist for Simplex-PI in the literature" except Melekopoglou-Condon) | — | no deterministic one-player exponential single-switch construction stated |
| NOT opened | Melekopoglou-Condon 1994 itself; Zadeh 1973 ("A bad network problem for the simplex method", min-cost flow); Hansen-Zwick ISAAC 2010; Fearnley PhD thesis | Zadeh 1973 is the classical network-simplex bad example and could be relevant; not checked |

## (2) Verdict
**KNOWN IN A CLOSE FORM.** Super-polynomially long single-switch improving sequences on deterministic, acyclic, one-player instances are known: FHZ 1410.7530, acyclic shortest paths, Random-Facet and Random-Bland, 2^Ω̃(m^{1/3}) / 2^Ω̃(√m) expected. Exponential single-switch policies are known on stochastic MDPs (Melekopoglou-Condon, 2^n − 1).

**The exact statement was NOT FOUND:** an explicit one-player PARITY game with VJ valuations and a 2^n − n − 1 chain of Ω-strict single switches, contradicting VJ00 Prop. 7.4 on the any-policy reading. CDAG_n differs from the known forms in three ways:
- (i) VJ valuations on priorities (longest path with 2^rank weights), not general shortest-path weights;
- (ii) an exhibited deterministic chain (existence of a policy), not a randomized rule's expectation;
- (iii) full 2^n − n − 1 length on n+1 vertices.

Consistent with T22: the switch-all reading of Prop. 7.4 (Friedmann thesis Thm 4.9) is untouched.

## DONE / FINDINGS / NEEDS
- FINDINGS:
  - CDAG_n is longest-path policy improvement on a complete DAG with 2^rank weights.
  - Known in close form: FHZ 1410.7530 (acyclic shortest paths, deterministic one-player, randomized single-switch rules, subexponential) and Melekopoglou-Condon 1994 (stochastic MDPs, single-switch, 2^n − 1).
  - The exact VJ/parity instance and its bearing on Prop. 7.4 were not found.
  - Zadeh 1973 was not opened.
- NEEDS: none (owner: nothing; fleet-internal).
