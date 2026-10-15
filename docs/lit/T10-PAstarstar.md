# T10: novelty of PA** and of T-A1 (exact class of psolB) (L-LIT, 2026-10-15)

Asked by the Lead at 00:12Z. This check gates M3. Statements checked are at trunk 4e31b49:
- docs/attr/TA1-proof.md §1–2:
  - T-A1: psolB solves G completely iff PA**(G).
  - T-A1': PA** implies that psolQ solves G completely; the converse is false.
  - Corollary 1: HKP's classes are contained in PA**.
  - Corollary 2: PA** is decidable in O(|V|^2 |E|).
- docs/RESULTS.md R2, including the side finding on HKP Thm 4.

All sources below were opened by L-LIT and are logged in notes/L-LIT.md under "Sources opened". "Not opened" means exactly that.

| Q | question | verdict |
| --- | --- | --- |
| (1) | an exact characterisation of the games psolB (or another fatal-attractor solver) solves completely | **NEW** (none found; the closest source names the question as open) |
| (2) | PA**, or an equivalent peeling condition, under another name | **NEW as a condition; its two ingredients are KNOWN** |
| (3) | the flaw in the proof of HKP Thm 4 (the minimal-rank strategy can lose) | **NEW** (no erratum or correction found) |

Caveat that applies to all three verdicts: HKP's own follow-up chapter was **not opened**. It is "Static analysis of parity games: Alternating reachability under parity", in *Semantics, Logics, and Calculi*, LNCS 9560, pp. 159–177, Springer 2016. The reference is taken from Cranen–Keiren–Willemse, arXiv 1603.06422 v1, bibliography [31]. The Springer page gave no PDF, and the Imperial Spiral search returned 404. A KNOWN result is most likely to sit in that chapter, if anywhere.

## (1) Is an exact characterisation of psolB's (or any fatal-attractor solver's) complete class known?
**Verdict: NEW.** No opened source characterises exactly the games that a fatal-attractor solver solves completely. The opened sources give sufficient classes only, and the best-placed later paper says the question is open.

What each source says:

- **HKP, arXiv 1405.0386.** v2 is the version L-LIT read throughout. v1 (2 May 2014) was also opened for this task. arXiv lists v1 and v2 only; a request for v3 returns 404.
  - The completeness results are all sufficient conditions:
    - Thm 7: colours {0,1}, i.e. Büchi.
    - Lemma 5: deterministic games.
    - Thm 8: SCC-constant colours.
  - Thm 6 is order independence.
  - Def. 8 defines the class Solved, but it is never characterised.
- **Ah-Fat and Huth, GandALF 2016, arXiv 1609.04085 v1, Conclusions.** Verbatim:
  > "we do not, at present, have a good understanding of what types of parity games are solved completely for certain partial solvers. More powerful versions of Theorem 1, which extend to classes of 2-player games, would be a first step in addressing that weakness."

  Their Thm 1 is about 1-player residual games only. This is the open direction that T-A1 answers for psolB.
- **Vester, "Winning cores in parity games", arXiv 1602.01963 v1.**
  - Prop. 7: "Let X be a fatal attractor for player j in G. Then X ⊆ A_j(G)" (inclusion in the winning core).
  - Vester's own polynomial under-approximation B_j(G) "contains all fatal attractors for player j", and Fig. 7 is "an example that B_j(G) can contain even more states than just fatal attractors".
  - There is no characterisation of psolB's complete class.
- **Bruyère, Pérez, Raskin, Tamines, arXiv 1907.06913 v2.** Partial solvers for generalized parity games, plus benchmarks. No completeness class.
- **Laveaux, Wesselink, Willemse, "On-the-fly solving for symbolic parity games", arXiv 2201.09607 v1.**
  - In the "Fatal attractors" paragraph, Lemma 6 is "(See [17], Theorem 2)". They define "a simplified version of the psolB algorithm, here dubbed solB−". It handles each priority once, in descending order, and is used for on-the-fly partial solving.
  - No completeness statement.
- **Cranen, Keiren, Willemse, "Parity game reductions", arXiv 1603.06422 v1.** Cites HKP [30] and the chapter [31] in the bibliography only. No completeness statement.
- **Citation search (Semantic Scholar API).**
  - 8 citers of arXiv 1405.0386.
  - 12 citers of the FoSSaCS 2013 version, DOI 10.1007/978-3-642-37075-5_3.
  - Opened among them: Ah-Fat–Huth 2016, Vester 2016, Bruyère et al. 2019, Laveaux et al. 2022 (On-the-fly), Cranen et al. 2016 (Parity game reductions). None characterises the class.
  - **Not opened:**
    - HKP's chapter "Static analysis of parity games" (2016; see the caveat above).
    - "Effective partial solvers for parity games" (2016). L-LIT reading from its title and authors: probably a thesis or report version of Ah-Fat–Huth. Their GandALF conclusion above was written after it or alongside it.
    - "Reachability games revisited" (2016).
    - Vester's PhD thesis "Game-based verification and synthesis" (DTU 2016; DTU Orbit returned 403).
    - The Rabin index paper (2011). It predates HKP, so it cannot contain a result about psolB.
- **Web and arXiv searches** for "fatal attractor" with "complete", "characterization" or "class" found nothing more.

L-LIT reading on what is new:
- T-A1 is the first exact description of HKP's class Solved for psolB that L-LIT can find.
- Corollary 2 (membership decidable in polynomial time) settles the issue T8 §(3) raised for PA, but only because the characterisation is exact. Run psolB and test whether the residual game is empty.
- The same fact means PA** is, by construction, as hard to "understand" as psolB's run. Its value lies in the structural description (§(2)), not in a faster membership test.

## (2) Is PA** known under another name?
**Verdict: NEW as a condition. Both ingredients are KNOWN, and the combination and its closure rule are not found.**

- **Ingredient (a) is KNOWN: fatal attractors.**
  - A (p,d)-recurrent X ⊆ pr^{-1}(d), with X ⊆ MAttr_p(X, d), is HKP's fatal attractor (HKP Def. 4 and Thm 2, in min-parity).
  - Laveaux et al. (2201.09607, before Lemma 6) write the greatest such set as a fixpoint: "F^α(a, c) = νZ.(P^{=c} ∩ safe^α(a) ∩ MAttr^α(a ∩ safe^α(a), Z, c))". This is the largest recurrent set at one priority, in a symbolic setting.
  - Option (a) of PA** is therefore exactly one psolB removal.
- **Ingredient (b) is KNOWN in a weaker form: DJT traps.**
  - In a DJT attractor decomposition (Daviaud, Jurdziński, Thejaswini, arXiv 2003.08627 v2 §2), the pieces S_i are traps for the opponent in the current subgame G_i. Their priorities are ≤ d−2, they are decomposed recursively, and each is followed by an attractor.
  - PA** (b) asks more and less than this:
    - **More:** S must be a trap for q in the whole level set R, not in the remainder after earlier pieces.
    - **Less:** there is no mandatory first step A = Attr(P_d) at each level, and (a)- and (b)-steps can be interleaved in any order.
  - T8's PA was the DJT form with the stronger closure in R. PA** drops DJT's fixed top step and replaces it by repeated fatal attractors.
- **Not found** in any opened source as a named or defined notion:
  - Recursive peeling of a winning region by fatal attractors and closed sub-traps.
  - Any condition equivalent to it.

  Searched:
  - DJT §2 (attractor decompositions, Prop. 1).
  - JMT 2001.04333 v2 (universal attractor decompositions and trees, Prop. 8–12 and 18).
  - Vester's winning cores (1602.01963, Thm 1–4, Prop. 7).
  - HKP (Def. 3–8).
  - Ah-Fat–Huth (composition of partial solvers).
  - Laveaux et al.
  - Bruyère et al.

  Only abstracts were opened for priority promotion (CAV 2016) and tangle learning (arXiv 1804.01023 v2). Their family resemblance is noted, but L-LIT has not checked their definitions against PA**.
- **L-LIT reading, unrefereed.**
  - An (a)-step at the top priority d of a level is a p-dominion of the subgame R that is reached by a cycle through priority d. That is close to a tangle or a promoted region.
  - The difference lies in what may be removed. Tangle learning and priority promotion remove regions found by full (non-monotone) attractors. PA** (a) uses monotone attractors, which never pass through a higher priority.
  - So PA** should be strictly smaller than any "peelable by tangles" condition. L-LIT has not proved this.

## (3) Is the flaw in the proof of HKP Thm 4 known?
**Verdict: NEW (no erratum or correction found).**
- **The strategy text is unchanged between versions.** It is identical in arXiv v1 (2 May 2014) and v2:
  > "For every node v in A, let r(v) = (d, i) be minimal in the lexicographic order such that v is in A_{d,i}. We choose the strategy that selects the successor with minimal r according to the same lexicographic order."

  arXiv lists no v3, and neither version has a "comments" note about a correction.
- **No erratum found.** Web searches for an HKP Fatal attractors erratum or a correction of the layered/psolQ strategy found nothing.
- **Citers do not rely on Thm 4.** Laveaux et al. cite Thm 2 only, as their Lemma 6. Vester's Prop. 7 is about fatal attractors (Thm 2), not layered ones. Ah-Fat–Huth compose solvers without re-proving Thm 4. No opened citer re-proves psolQ's soundness or flags the strategy.
- **Not opened:** the 2016 HKP chapter, which could restate psolQ with a corrected proof. The FoSSaCS 2013 version was not opened either (Springer bot wall). It precedes the arXiv versions, so it cannot carry a fix that v2 lacks.
- **Status in the fleet:** RESULTS R2 records the side finding: REFEREE-2's counterexample docs/referee-2/R2-TA1/hkp_thm4_strategy.py and the witness-successor repair; the theorem itself is unaffected. L-LIT has not re-run the counterexample. As far as L-LIT can find, this is a new observation about a published proof, not about a published theorem.

## M3 reading (L-LIT reading, opinion; the Lead rules)
- **T-A1 is new**, and it answers, for psolB, the question Ah-Fat–Huth 2016 state as open. Its value is clearly higher than T8's PA:
  - it is exact, not only sufficient;
  - it contains HKP's three classes (Corollary 1);
  - membership is polynomial (Corollary 2).
- **Fit with D1:** "tighter analysis of a known algorithm", as in Lead reading L9.
- **Limit to state honestly:** PA** is defined so that its peeling steps mirror psolB's removals. A reader may see the "only if" direction as close to a restatement of psolB's run. The non-trivial content is:
  - the "if" direction: every PA** peeling, in any order, is found by psolB, whatever order psolB itself uses;
  - the closure-in-R rule;
  - Corollary 1.

  The write-up should lead with those.
- **Before any claim of "first" leaves the fleet:** the 2016 HKP chapter should be opened, because it is the one place a KNOWN verdict could still come from.

## DONE / FINDINGS / NEEDS
- FINDINGS:
  - Q1 NEW: no characterisation of psolB's complete class was found, and Ah-Fat–Huth 2016 call such classes open.
  - Q2 NEW as a condition: (a) = HKP fatal attractors, and (b) = DJT-style traps with closure in R; the combination is unnamed.
  - Q3 NEW: the Thm 4 strategy text is unchanged between v1 and v2, no erratum was found, and citers use only Thm 2.
  - All three verdicts carry the caveat that HKP's 2016 LNCS 9560 chapter was not opened.
- NEEDS: owner: library or Springer access to HKP, "Static analysis of parity games: Alternating reachability under parity", LNCS 9560 (2016), pp. 159–177, if M3 is to be claimed outside the fleet.
