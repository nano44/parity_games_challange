# T15: Zadeh's rule with a fixed, strategy-independent tie-break (L-LIT, 2026-10-15)

Asked by the Lead at 15:07Z. The context is L-RED R7 (claude/l-red b560aa8, docs/red/R7-S5-zadeh-ties.md, not re-read here). It reports that the published Zadeh runs (Friedmann IPCO'11 / PGSolver; Disser–Friedmann–Hopp 1911.01074 Thm 6.18 with Def. 6.4) have cyclic tie constraints, so no fixed order reproduces them.

The open statement checked: is there a polynomial family of sink parity games (injective priorities) with a vertex numbering under which Zadeh's least-entered rule, with the smallest-(source, target)-index tie-break, makes 2^{Ω(n^c)} switches?

All sources below were opened by L-LIT and are logged in notes/L-LIT.md. "p." is the PDF page unless marked "printed".

**Verdict: OPEN.**
- No opened source gives a super-polynomial lower bound for Zadeh's rule with a fixed, strategy-independent tie-break on parity games, MDPs or LPs.
- The only fixed-order result is Thomas 2017. It is on **abstract** cubes (AUSOs), and Thomas lists realising it as an LP as open.
- A separate fact bears on how solid the published Zadeh bounds are: the 2011 subexponential bound was found flawed (Disser–Hopp 2019, as quoted by DFH and Zadeh 2025), and the 2020/2023 exponential bound is publicly disputed for its LP/MDP part (Zadeh, arXiv 2510.16055).

## The published Zadeh bounds and their tie-breaks
| source (opened) | setting | tie-break | fixed? |
| --- | --- | --- | --- |
| Friedmann, IPCO 2011 (author's preprint, zadeh_lower_bound.pdf), Thm 2 (p.14) | MDPs, built from parity games, then LPs; Ω(2^n) steps on O(n^2) size | p.6: "we as 'lower bound designers' are the ones that choose a particular tie breaking rule … We will not specify the tie-breaking rule used for our lower bound explicitly, due to the fact that the rule itself is not a natural one" | **No** (unspecified, designer-chosen) |
| Disser–Friedmann–Hopp, arXiv 1911.01074 v2, Thm 6.18 (p.31) | parity games (VJ strategy improvement), MDPs, LPs; size O(n) | Def. 6.4 (p.15): a pre-order ≺_σ on E_0 that depends on σ, via open/half-open cycles and bit values β^σ, extended to "an arbitrary but fixed total ordering". Then "Apply the first improving switch contained in I^σ_min with respect to the ordering ≺_σ with the following exception: If φ^σ(b_1,b_2) = φ^σ(s_{1,1},h_{1,1}) = 0, then apply (s_{1,1},h_{1,1})". p.2: "an artificial, but systematic and polynomial time computable, tie-breaking rule"; p.3: "it cannot be avoided to fix a tie-breaking rule when analyzing Zadeh's pivot rule" | **No.** The order depends on the current strategy σ, and the exception depends on the occurrence record |
| Friedmann PhD thesis, Cor. 4.79 (PDF p.207) | MDPs | "there is always a way to break ties that results in a linear number of pivoting steps … The question whether Zadeh's pivoting rule solves MDPs (and LPs) in polynomial time should therefore be phrased independently of the heuristic of breaking ties" | — (why some tie-break must be fixed) |
| Thomas, arXiv 1706.09380 v1 (ESA 2017), Thm 8 (p.15) | **abstract AUSOs** of the n-cube | "Zadeh's rule, with a suitable starting vertex and tie-breaking rule, takes a path of length at least 2^{n/6}". p.15: "our lower bound construction will have the simplest possible tie-breaking rule, an ordered list which will be given explicitly. This is in contrast to the lower bounds by Friedmann". p.3: "it is based on a tie-breaking rule that is essentially as simple as possible: a fixed ordered list" | **Yes, but abstract.** p.22: "First and foremost is settling if Zadeh's and Johnson's rules admit exponential lower bounds even on linear programs". DFH p.2: "it is unclear whether the corresponding construction can be realized as a Linear Program" |
| Avis–Friedmann, arXiv 1305.3944 (Cunningham), Thm 4 (p.15) | parity games, then MDPs, LPs, AUSOs | the rule *is* a fixed cyclic order. p.11: "In order to derive a lower bound we are entitled to give both the input graph and the ordering to be used" | yes, for **Cunningham** (a different rule). It is precedent that a designer-chosen fixed order can be engineered on parity games |

## Status of the published Zadeh bounds (bears on how much the open statement matters)
- **Disser–Hopp, IPCO 2019** (LNCS 11480, pp.168–180) is **NOT opened**; author search found no arXiv version. It is quoted by Zadeh 2025 (p.1): "We investigate Friedmann's lower bound construction and exhibit three flaws in his analysis: … (c) the sequence of improving switches described by Friedmann does not consistently follow Zadeh's pivot rule". DFH p.2 cite it as [DH19] next to Friedmann's result.
- **N. Zadeh, arXiv 2510.16055 v1** (Oct 2025, 8 pp., not peer-reviewed as far as shown). Abstract: "We show that their arguments contain multiple flaws. In other words, the worst-case behavior of the least-entered rule has not been established".
  - Its objections concern DFH's LP form "(P)" and the LPs and MDP the authors supplied in Aug 2025: infeasibility as probabilities, and LP vs MDP mismatch.
  - It does **not** discuss the parity-game construction or tie-breaking (a grep for parity, tie, strategy improvement and game finds only reference titles).
  - L-LIT has not checked its claims. They are the author's.
- **Consequence (L-LIT reading).** The DFH parity-game statement (Thm 6.18, item 1) is not directly attacked. It holds only with Def. 6.4's strategy-dependent tie-break. Whether Zadeh's rule is super-polynomial on parity games under any *fixed* tie-break is not settled by any opened source.

## Answer to the open statement
- **Known:** no.
- **Closest:**
  - Thomas Thm 8: a fixed ordered list, but on abstract AUSOs. Binary parity games give AUSOs (Thomas p.3: "binary parity games correspond directly to AUSO"), but not every AUSO comes from a game, and Thomas's are not shown realisable.
  - Avis–Friedmann: a fixed order, but for Cunningham.
- **Narrower than "fixed order":** the Lead's statement asks for the tie-break *induced by a vertex numbering* (smallest (source, target) index). That is a lexicographic edge order, a special case of Thomas's arbitrary ordered list. A Thomas-style construction would need its list to be lexicographic under some numbering.
- **Verdict: OPEN.** A positive answer would be new: the first fixed-tie-break Zadeh lower bound in any non-abstract setting. A negative answer is not suggested by any source.

## (b) Citation fix
docs/lit/T13-RF-parity.md line 3 now reads:
- REFEREE-2: "first read 995cfd3, signature 94dde7b, R2-TL §6";
- REFEREE: "signed at 42f11c6/5ed56c5";
- with a note that this was corrected per the Lead at 15:07Z.

## DONE / FINDINGS / NEEDS
- FINDINGS:
  - (a) OPEN. All published Zadeh bounds on games, MDPs or LPs use a designer-chosen, strategy-dependent tie-break (Friedmann p.6 "not a natural one"; DFH Def. 6.4 ≺_σ).
  - The only fixed-list result is Thomas 2017 Thm 8, on abstract AUSOs, with LP realisability open (Thomas p.22; DFH p.2).
  - Zadeh 2025 disputes the LP/MDP part of DFH, not the parity part. Disser–Hopp 2019 is not opened.
  - (b) T13 citation fixed.
- NEEDS:
  - owner: Disser–Hopp IPCO 2019, only if the status of Friedmann's 2011 bound matters to a claim.
  - L-RED: Thomas's AUSO construction (1706.09380 §5) is the natural template for the open statement.
