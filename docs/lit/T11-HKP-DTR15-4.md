# T11: HKP DTR15-4 against T10 (L-LIT, 2026-10-15)

Asked by the Lead at 07:55Z. The source is: M. Huth, J. H.-P. Kuo, N. Piterman, "Static analysis of parity games: alternating reachability under parity", Imperial College London, Department of Computing, Technical Report 2015/4, dated 9 August 2015 (footnote 1, p.1), 18 pp.

L-LIT opened it as follows:
- Downloaded at 07:49Z from https://www.doc.ic.ac.uk/research/technicalreports/2015/DTR15-4.pdf.
- sha256 a7b61fe3a72926a94a3019e34620339f38aa653fe8aeed9ab4210187763e9cd6, the same as the hash the Lead gave.
- pdfinfo reports 18 pages, created 26 Sep 2015.
- The whole text was read via pdftotext.

The OWNER-DESK reading (owner-desk 48cf448) was compared with this one and agrees on all four of its points. It is not cited as a source.

Conventions: DTR uses min-parity (p.3: "Player 0 wins play π iff min Inf(π) is even"), the same as HKP and unlike TARGET. "[13]" in DTR is the FoSSaCS 2013 paper, and "[14]" is arXiv 1405.0386.

| item | verdict |
| --- | --- |
| a. DTR15-4 = LNCS 9560 pp. 159–177? | **UNCLEAR, very likely the same text up to copy-editing**: the reference lists are identical; the published abstract and section list were not obtained |
| b. T10 Q1 (exact class of psolB) | **NEW**, unchanged |
| b. T10 Q2 (PA** under another name) | **NEW as a condition**, unchanged. DTR adds a known neighbour (gfp of F^p_G), which is not a peeling condition |
| b. T10 Q3 (flaw in the proof of HKP Thm 4) | **NEW**, unchanged |
| c. bearing on gap G10 | **NO** |
| d. the Thm 4 flaw in DTR | **ABSENT** (psolQ's strategy does not appear) |
| e. psolC | stated below; T-A1 + DTR Thm 4 give PA** ⊊ (games psolC solves completely), conditional on DTR Thm 4 |

## a. Is DTR15-4 the text of LNCS 9560 pp. 159–177?
**Verdict: UNCLEAR, very likely the same text up to copy-editing.**

The DOI 10.1007/978-3-319-27810-0_8 is correct. Crossref (api.crossref.org/works/10.1007/978-3-319-27810-0_8, opened) gives:
- title "Static Analysis of Parity Games: Alternating Reachability Under Parity";
- container "Semantics, Logics, and Calculi", Lecture Notes in Computer Science, pages "159-177";
- authors Huth, Kuo, Piterman;
- published 2015-12-25.

Semantic Scholar gives the DBLP key conf/birthday/HuthKP16.

Evidence for "same text":
- **Title and authors** are identical.
- **Reference list.** Crossref deposits 29 references for the chapter. They match DTR's 29 references (pp.16–18) entry for entry, in the same order. Both run from [1] Chatterjee, "Linear time algorithm for weak parity games", to [29] Zielonka 1998, and both include [13] FoSSaCS 2013 and [14] arXiv 1405.0386. The only differences are Springer formatting: Crossref adds editor names, e.g. "In: Pfenning..." for [13].
- **Self-description.** DTR calls itself a chapter throughout: "Outline of chapter" (p.3), "In this chapter, we assume that such graphs are finite" (p.2).

What could not be compared:
- **Abstract and section list of the published chapter.**
  - link.springer.com and dblp.org served bot challenges to this container.
  - Crossref has no abstract, and Semantic Scholar says the publisher elided the abstract.
  - Semantic Scholar's open-access link for the chapter DOI (hdl.handle.net/10044/1/94990) resolves to the Imperial Spiral record of this same report. That record lists "Departmental Technical Report: 15/4, 2015, pp.1-18", file DTR15-4.pdf, with an abstract identical to DTR's p.1.
  - So no open copy of the Springer pages exists that L-LIT can reach.
- **Page count.** 18 report pages against 19 LNCS pages (159–177) is not diagnostic, because the layouts differ.

Changes between 9 August 2015 and publication (25 December 2015) cannot be excluded. The section list, the theorem numbering, and any added "related work" (e.g. on completeness classes) are unverified for the Springer version.

## b. T10 Q1–Q3 against DTR15-4
- **Q1 (an exact characterisation of the games psolB, or any fatal-attractor solver, solves completely): still NEW.**
  - DTR has no characterisation of the games any partial solver solves completely.
  - Its only statements about psolB are:
    - Thm 4 (p.12): "The call psolC(G) decides the winner of all nodes for which call psolB(G) decides a winner".
    - Its consequence, §6 (p.13): "psolC will solve completely all games that psolB solves completely".
  - Its examples are single games:
    - Ex. 2 / Fig. 4 (p.10): psolC solves the game completely.
    - Ex. 3 / Fig. 6 (pp.10–11): psolC solves no node.
    - Fig. 8 (p.12): psolC solves the game completely; psolQ solves no node.
  - Its conclusion (p.15) measures a partial solver's quality "by how often it computes winning regions completely", i.e. empirically, and names no class.
- **Q2 (PA** under another name): still NEW as a condition.**
  - DTR's new object is the greatest fixed point of F^p_G(X) = X ∩ Wr_p(G, X) on sets of p-parity nodes (eq. (2), p.7).
  - Lemma 2 (p.7) shows that every X ⊆ Wr_p(G, X) is won by p.
  - §5 (p.12) shows that every fatal attractor (X of one colour c, X ⊆ MA(X)) is a fixed point of F^p_G.
  - This is a single gfp that over-approximates the union of fatal attractors, i.e. of PA** (a)-steps. It has no recursive (b)-step (a closed sub-trap peeled at a lower level), and no peeling sequence.
  - It is a known neighbour of ingredient (a), not an equivalent of PA**.
- **Q3 (flaw in the proof of HKP Thm 4): still NEW.** See d.

The T10 caveat ("HKP's 2016 chapter not opened") now narrows to the gap between the 9 August 2015 report and the Springer pages.

## c. Does DTR15-4 bear on RESULTS R2 gap G10?
**No.** G10 is T-A1 Corollary 1's dependence on HKP's proofs of Thm 7 (colours 0/1), Thm 8 (SCC-constant) and Lemma 5 (deterministic), arXiv 1405.0386 v2. DTR does not state, restate or re-prove any of these three.
- Its only use of HKP results is the following:
  - Def. of MA(X) and psolB reproduced from [13] (eq. (3) p.11; Fig. 7 p.12, "a reproduction of Fig. 3 in [13]").
  - "Theorem 2 in [13]" (fatal attractors are won), p.11.
  - "Theorem 5 in [13]" (order of fatal-attractor detection does not matter), used in the proof of Thm 4, p.12.
  - lift(ρ) and Locality from [14], §7 p.15, and §8 p.16 "Definition 7.2 in [14]".
- Two side notes:
  - (i) The order-independence result DTR cites as [13] Thm 5 is Thm 6 in arXiv v1 and v2. L-LIT did not open FoSSaCS 2013 to confirm its numbering.
  - (ii) "Definition 7.2 in [14]" matches neither arXiv version: Locality is Def. 10 item 3 in both v1 and v2.
- R2's G10 note also mentions that HKP's Thm 7 proof invokes Thm 6. DTR re-proves nothing there either.

## d. The Thm 4 flaw (the minimal-rank strategy of arXiv 1405.0386 v2 Thm 4, psolQ)
**ABSENT.**
- psolQ appears in DTR only by name:
  - p.12: "In [13], we also studied a more precise but more complex partial solver psolQ ... psolQ does not solve even a single node for the parity game in Figure 8".
  - Fig. 8 caption.
- layeredAttr, rank (d, i) and the minimal-rank strategy do not occur. DTR's own "Theorem 4" (p.12) is a different statement (psolC vs psolB).
- DTR's strategy content concerns psolC only:
  - Thm 1's proof (p.6) builds a strategy with memory from an attractor strategy on G^p_X.
  - Thm 3 (p.9) shows that finite memory is needed for reachability under parity in general.
  - Question 1 (p.10) asks whether the greatest fixed points need memory.
  - None of this touches psolQ.

## e. psolC (stated only; no work started)
- **Definition.**
  - §3 defines "reachability of (X, p) under parity" (Def. 1, p.4). Player p wins a play iff some v_j, j > 0, is in X and the minimum colour on v_0..v_j has parity p. The opponent wins plays that never revisit X.
  - It is solved by an ordinary attractor on the product graph G^p_X = V × (C(G) ∪ {⊥}) (Def. 2 p.5, Thm 1 p.6).
  - F^p_G(X) = X ∩ Wr_p(G, X) on subsets of p-parity nodes is monotone (eq. (2), Lemma 3 p.7). Its non-empty fixed points are won by p (Lemma 2 p.7).
  - psolC (Fig. 5, p.9) works as follows:
    1. For p = 0 and then p = 1, compute the gfp X of F^p_G from {v | c(v)%2 = p}.
    2. If X ≠ ∅, remove Attr_p[G, X] and recurse.
    3. Stop when both gfps are empty.
- **Complexity.** Thm 2 (p.8): time O(|E|·|C(G)|·|V|^2), space O(|E|·(1+|C(G)|)), and sound. Cor. 1 (p.6): one Wr_p computation costs O(|E|·|C(G)|).
- **Relation to psolB.** Thm 4 (p.12): psolC decides every node psolB decides. On random games psolC never solved fewer nodes than psolB.
  - The text (§6, p.13) says psolC "solves more than psolB for around 10% of games" at edge density 1-5.
  - Its own Fig. 9 (p.14), column #9, gives 1184 / 100000 (500-5-1-5) and 1104 / 100000 (500-50-1-5), i.e. about 1.2%. That is about 6% of the roughly 19,000 games psolB leaves unsolved (#6).
  - So the "10%" is not supported by the table as printed.
- **Relation to psolQ.** Fig. 8 (p.12) is a 1-player game that psolC solves completely and psolQ does not touch. No converse example is given.
- **Partiality.** Ex. 3 / Fig. 6 (pp.10–11) is a game owned by player 1 and won by player 0 on which psolC solves no node. By Thm 4, psolB solves no node there either.
- **What T-A1 / PA** say about psolC** (L-LIT derivation from stated results; not refereed):
  - T-A1 ("if") + DTR Thm 4 give: PA**(G) ⟹ psolC solves G completely.
  - The inclusion is strict. By T-A1', PA**(G) ⟹ psolQ solves G completely. psolQ solves no node of DTR's Fig. 8 game, so that game is not PA** although psolC solves it completely.
  - So PA** ⊊ (games psolC solves completely). Note that T-A1' is itself conditional on gap G11.
  - T-A1 gives no characterisation of psolC's class.
  - The derivation is only as strong as DTR Thm 4. Its proof (p.12) handles the first removal and then appeals to order independence ([13] Thm 5). L-LIT reading: it does not argue the step after psolC has removed a larger set than psolB would. That step needs psolB's decided set to shrink only by removed nodes when a p-attractor of a p-won set is deleted, a removal-monotonicity property of the same kind as the fleet's G8. L-LIT has not checked whether this property holds. A referee check is needed before the fleet uses DTR Thm 4.

## DONE / FINDINGS / NEEDS
- FINDINGS:
  - a: UNCLEAR, very likely the same text. The 29-entry reference lists are identical (Crossref vs pp.16–18), and the text calls itself a chapter. The Springer abstract and sections were not reachable, and the only open copy of the chapter DOI is this report.
  - b: T10 Q1, Q2 and Q3 all stay NEW. DTR's gfp of F^p_G is a known neighbour of PA** (a), not of PA**.
  - c: G10 NO; DTR re-proves none of HKP Thm 7, Thm 8, Lemma 5.
  - d: the Thm 4 flaw is ABSENT, because DTR never touches psolQ's strategy.
  - e: psolC is O(|E|·|C|·|V|^2) and decides at least what psolB decides (DTR Thm 4). With T-A1 this gives PA** ⊊ Solved(psolC), conditional on DTR Thm 4, whose multi-round step is a sketch.
- NEEDS:
  - owner: only if a "first" claim is to leave the fleet, the Springer pages 159–177, to close a.
  - REFEREE (via the Lead): DTR Thm 4's multi-round step, before PA** ⊊ Solved(psolC) is used.
