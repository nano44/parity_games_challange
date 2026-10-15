# T16: gauntlet step 3 for DTL (Oink's distance tangle learning, dtl.cpp @ 8fbf0a7) (L-LIT, 2026-10-15)

Asked by the Lead at 15:35Z. The object is van Dijk's research solver `dtl`. L-ALG transcribed it as C5-DTL (claude/l-alg, docs/alg/candidates/C5-DTL.md), and L-RED R8 (b72707e) gives Lemma M; both are unrefereed.

Sources were opened by L-LIT, with sha256 values in notes/L-LIT.md. The Oink repository was cloned from github.com/trolando/oink, all refs (master = 8fbf0a7, dftl, maintenance). "p." is the PDF page.

**Verdict (step 3): SIGNED, with four caveats (§4).**
- No published lower bound, and no barrier theorem in B1–B17, covers DTL.
- DTL lies outside the formal models of the universal-tree and separator barriers (B1–B3).
- Its framework (attractor decomposition with tangles) has **no** general lower-bound theorem (B4).
- The caveats are serious:
  - (i) the author's README asserts an uncommitted "counter_dtl";
  - (ii) a public DFTL counterexample on Oink's `dftl` branch is untested against DTL;
  - (iii) the author's 2019 slides call path-based variants vulnerable;
  - (iv) the author's 2024 talk proposes, unproven, a universal-tree style argument against tangle learning.

## 1. Provenance: what the author claims about DTL
- **No publication defines or analyses DTL.**
- **ISoLA 2024 paper** (van Dijk, "Avoiding Distractions in Parity Games", LNCS 15221 pp.330–352, DOI 10.1007/978-3-031-75380-0_19; author copy tvandijk.nl/pdf/2024isola_rtl.pdf):
  - It never mentions dtl, distance tangle learning or DFTL: a grep for dtl, distance, progressive, ptl and "good path" finds only "along good paths" (p.12, the progress-measure view).
  - It defines rtl and ortl and gives exponential lower bounds for both: Fig. 6 (p.17, "A exponentially hard parity game for player Even in ortl") and Fig. 7 (p.18, "Bit 2 of a 4-bit Two Counters game that delays rtl exponentially").
  - Conclusion, p.20: "whether these ideas can lead to a true polynomial-time algorithm remains an open question."
- **ISoLA 2024 talk** (tvandijk.nl/pdf/2024isola_rtl_talk.pdf, 91 pp.), last slide "PERSPECTIVES" (p.91):
  - "TL and RTL have worst-case exponential behavior"; "Ongoing work: heuristics for 'currently distractions' (DF*TL)".
  - "Ideas to prove that TL cannot solve in polynomial time • Learning tangles moves vertices along the universal tree • Every algorithm orders vertices with a universal tree • Maybe: the maximal 'knowledge' (tangles and path values) per iteration can be characterized, such that the number of steps in the worst case is quasi-polynomial? • Could be generalized to classes of algorithms?"
- **GandALF 2019 talk** (tvandijk.nl/pdf/2019gandalf_talk.pdf), slide 42 (p.62): "'Recursive tangle learning' and 'progressive tangle learning' (unpublished) use this method [play to the best path, not just the best endpoint] to identify distractions … BUT VULNERABLE! (to a different version of the TC game)!" The talk names rtl and ptl, not dtl.
- **Oink repository** (git, all refs; commit claims are the author's):
  - dtl.cpp history: e67cb4c 2019-09-14 "New experimental solver distraction-free tangle learning"; 7798285, 2d12471 (2019); 0c2fab6 2020-03-27. It was renamed to "Distance Tangle Learning (research variant based on 'good path length')" on 2021-07-02 (1ba8b0a).
  - README at 8fbf0a7: line 47 is the DTL row; line 196 is "counter\_dtl | Counterexample to the DTL solver", added in 39254fe (2021-06-25, before the rename). **No file named counter_dtl exists on any ref** (`git log --all -S`, `ls-tree` of all 4 remotes).
  - README lines 213–216 list "DTL, IDTL" among algorithms that "can solve the two binary counters games in polynomial time".
  - **Branch `origin/dftl` (missed by L-ALG):**
    - a028e62 (2021-07-04) "Added solver DFTL and counterexample": src/solvers/dftl.cpp (744 lines) and src/tools/counter_dftl.cpp (8+4N vertices: a fixed "dominion / distracted tangle / barrier" gadget plus N copies of "distracted vertex / distraction / dominant").
    - 5502912, d1a923d, d54dfad (Jun 2024): "Improved DFTL version with better two-player interaction"; counter_odftl.cpp (8+6N vertices, adding "a tiny tangle of the opponent after the distraction").
    - ea51834 (2024-06-24): "Slight refactor to test a hypothesis".
    - DFTL is a **different** solver from dtl (added after the rename). By its code shape the generator looks like a distraction or correctness counterexample, not an exponential counter. It is **untested against dtl** here: this container has no Boost, Oink does not build, and L-LIT did not install system packages.
- **Not opened:** van Dijk, "Solving Parity Games, Very Slowly" (2024 chapter, DOI 10.1007/978-3-031-75778-5_21; L-ALG notes a paywall; not on the author's publication list as a PDF).

**Summary of the author's position (L-LIT reading):** DTL is unpublished. The author asserts a counterexample exists (README, 2021) but never committed it. He states that path-based tangle-learning variants are vulnerable (2019), and in 2024 suggests a universal-tree route to proving that tangle learning is not polynomial. He makes no bound or conjecture specifically about DTL's running time.

## 2. Published lower bounds for tangle learning and its variants
| source (opened) | algorithms covered | DTL? |
| --- | --- | --- |
| van Dijk, CAV 2018, arXiv 1804.01023 v1 | upper bound only: Lemma 13 (p.9) "Tangle learning runs in time O(dnm\|T\| + dn^2\|T\|^2) … \|T\| learned tangles"; no lower bound | — (a polynomial bound in \|T\|; DTL's analogue is R8's tangle-count argument) |
| van Dijk, "A Parity Game Tale of Two Counters", GandALF 2019, EPTCS 305.8 (tvandijk.nl/pdf/2019tc.pdf) | Ω(2^√n) for tl, pp, dp, zlk and others. p.1: "the first to provide such a lower bound to tangle learning"; p.9: "the exponential behavior is clear from the empirical data … we sketch out an inductive proof" | **escapes.** ISoLA p.12: the tc mechanism "works for all parity game algorithms that neutralize distractions by attracting them to a region or dominion of the opponent". DTL prunes distractions by good paths (best_vertices), which is not opponent attraction. The README (l.213–216) lists DTL among algorithms solving tc in polynomial time. L-ALG measured 2N+1 tangles on tc (fleet data, not a source) |
| ISoLA 2024 Fig. 7 (tc+) | rtl, exponential | not claimed for dtl. L-ALG's tc+ port gives ~1.4 N^2 DTL tangles (fleet data) |
| ISoLA 2024 Fig. 6 (counter_ortl) | ortl, exponential | not claimed for dtl. Untested by L-LIT |
| Oink counter_dftl / counter_odftl (branch dftl) | DFTL, per commit message | **untested** on dtl |
| GandALF 2019 slide 42 | rtl, ptl "VULNERABLE" (no family given) | names only rtl/ptl |
| anything on ptl/spptl/dtl/idtl in a publication | none found (ISoLA grep; author's publication list scanned: 2018tangles, 2019tc, 2019gandalf_talk, 2020gandalf, 2024isola_rtl(+talk), 2024rrrr_oink, 2024ssi) | — |

**Headline check:** no published family is claimed exponential for DTL.

## 3. Barrier statement: DTL against B1–B17
- **B1, B2 (separating automata, universal graphs; Czerwiński et al. Thm 5.1; CFGO Thm 4.1, Cor. 6.13 "informal").**
  - The lower bounds bind algorithms that *are* a separating automaton or a value iteration over an (n,d)-universal graph: a fixed structure, read along priority sequences.
  - DTL keeps no such structure. It recomputes regions from the graph, extracts tangles as bottom SCCs of strategy-restricted subgraphs (Tarjan/Pearce, extractTangles), and its state is the learned tangle set, which depends on the input.
  - **Outside, by model.** Caveat (iv): the author's own 2024 idea is to *embed* tangle learning into a universal-tree ordering ("Every algorithm orders vertices with a universal tree"). That is unproven. If proved for DTL, it would give a quasi-polynomial lower bound.
- **B3 (Arnold–Niwiński–Parys Thm 5.1; Remark 5.5 games).**
  - The model is an evaluation of a nested fixpoint expression ‖F‖_{U,V} driven by fixed trees U, V, accessing the game only through the one-step operator f. Its lower bound covers non-adaptive universal attractor decompositions (JM, and LPSW with fixed trees).
  - DTL's decompositions are adaptive (top-down α-maximal with tangle attractors, pruned by best_vertices). It also uses graph structure beyond f queries: SCCs, tangle escapes, edge lists.
  - **Outside**, exactly in the B3 escape column ("adaptive trees; algorithms using graph structure beyond fixpoint queries").
- **B4 (attractor decomposition as a class).**
  - DTL *is* an attractor-decomposition algorithm (ISoLA abstract places tangle learning among them).
  - There is **no** general lower-bound theorem for this class: JMOT 2010.08288 p.2, "not formally subject to the lower bound from universal trees".
  - So DTL is outside by the **absence** of a theorem, not by a structural escape. This is the weakest point of the barrier statement.
- **B5 (Zielonka exponential families).** Per-algorithm. DTL's only Zielonka-like branch is search_rec on Z (C5-DTL §2, L-ALG's untried attack). No published family targets it.
- **B6 (Two Counters).** Covers algorithms that neutralise distractions only by opponent attraction (ISoLA p.12). **DTL escapes the mechanism** (§2). The bound is empirical and sketched anyway.
- **B7 (partial solvers).** DTL is complete (fleet: dtl_check on 67,000+ games, verified strategies; not a source).
- **B8–B13 (strategy improvement, LCP).** DTL is not strategy improvement or LCP.
- **B14 (AUSO), B15 (IPM), B16 (time-bounded weak separators), B17 (complexity classes).** Not applicable.

## 4. Verdict for step 3
**SIGNED, with caveats.** No published lower bound or barrier theorem covers DTL. It is outside B1–B3 by model and outside B6 by mechanism, and B4 has no theorem.

Caveats (each could flip the verdict):
1. **Uncommitted author counterexample.** README "counter_dtl | Counterexample to the DTL solver" (39254fe, 2021-06-25). It is unpublished, has no source, and it is unknown whether it is a correctness or a running-time counterexample.
2. **Public DFTL counterexamples untested on DTL.** `origin/dftl`: src/tools/counter_dftl.cpp (a028e62) and counter_odftl.cpp (d54dfad). Action for L-ALG or L-RED: build them against master and run `--dtl` and `--idtl` with verification at N = 1..20.
3. **Author's 2019 statement** that path-based variants (rtl, ptl) are vulnerable to a modified Two Counters game. rtl was later defeated (ISoLA Fig. 7).
4. **Author's 2024 conjectured route to a barrier for tangle learning** (universal-tree ordering, "could be generalized to classes of algorithms?"). Unproven. If realised, it would put DTL inside a B1/B3-type quasi-polynomial bound.

Also: no published definition exists, so every statement here refers to dtl.cpp @ 8fbf0a7 as transcribed by L-ALG.

## 5. Addenda (Lead 15:38Z and 15:45Z)
**(a) The GandALF 2019 "VULNERABLE" slide.** Found: tvandijk.nl/pdf/2019gandalf_talk.pdf, slide 42 (p.62), quoted in §1.
- **Which variants it means.** The slide names "'Recursive tangle learning' and 'progressive tangle learning' (unpublished)", i.e. RTL and PTL. The talk PDF was created 2019-09-02 (pdfinfo). Oink commit afb589c (2019-09-05) is "New experimental solvers recursive tangle learning and progressive tangle learning". DTL's first commit, e67cb4c, is 2019-09-14, after the talk. **So DTL is not one of the variants the slide means.**
- **The "different version of the TC game"** is **tc+**:
  - afb589c (2019-09-05) adds src/tools/tc+.cpp together with rtl and ptl.
  - README: "tc+ | TC modified to defeat the RTL solver".
  - 3327c54 (2021-07-10): "New TC+ implementation to defeat the improved RTL implementation".
  - It was **published** as ISoLA 2024 Fig. 7 (p.18), "Bit 2 of a 4-bit Two Counters game that delays rtl exponentially". The paper also says (p.18): "The rtl algorithm solves both exponential lower bounds of Figure 4 and Figure 6 in polynomial time. To delay rtl exponentially often, we need to …".
  - Nothing in the slide, the repo or the paper claims tc+ against PTL or DTL. The README lists DTL among algorithms solving tc (not tc+) in polynomial time. L-ALG measured ~1.4 N^2 DTL tangles on tc+ (fleet data).

**(b) Which solver each counterexample commit targets.**
| commit | date | message / README text | solver targeted |
| --- | --- | --- | --- |
| 39254fe | 2021-06-25 | "Updated README.md"; adds "counter\_dtl \| Counterexample to the DTL solver" while the row reads "DTL \| Distraction-free Tangle Learning (research variant)" | **the pre-rename distraction-free TL = today's dtl.cpp**. dtl.cpp changed by only 6 lines between 39254fe and 8fbf0a7 (2024 refactors: fc79aee, 0c7ee84, 1f7ecb8, 38d654e, 77c6992). No source was ever committed |
| 1ba8b0a | 2021-07-02 | "Rename the DTL solver": README row becomes "Distance Tangle Learning (research variant based on 'good path length')"; touches only README.md and solvers.cpp | rename only, same algorithm |
| a028e62 (branch dftl) | 2021-07-04 | "Added solver DFTL and counterexample"; README adds "counter\_dftl \| Counterexample to the DFTL solver" | **DFTL**, a new 744-line solver distinct from dtl.cpp |
| 5502912, d1a923d (dftl) | 2024-06-18/19 | "Prepare for making DFTL two-player and keeping the original one-player version"; "Improved DFTL version with better two-player interaction" | DFTL |
| d54dfad (dftl) | 2024-06-19 | "Fix counter_odftl to have a tiny tangle of the opponent after the distraction" | (O)DFTL |

Consequence: caveat (i) is stronger than first stated. The README's counter_dtl targets **the same algorithm as current DTL**, and it is the only author claim against DTL. Its content is unknown: correctness or running time, and no file exists.

**(c) What ISoLA 2024 presents.** Neither DTL nor DFTL. It presents rtl and ortl (with tl, pp, zlk, fpi, fpj in the evaluation). DFTL appears only in the talk's "Ongoing work … (DF*TL)" (p.91).

## DONE / FINDINGS / NEEDS
- FINDINGS:
  - No published family is claimed exponential for DTL. The ISoLA 2024 paper does not mention DTL; its conclusion calls polynomiality open.
  - The Oink branch `dftl` holds public counterexamples for DFTL (counter_dftl, counter_odftl), which L-ALG missed and which are untested on DTL. The README's counter_dtl was never committed.
  - The author's 2024 talk proposes a universal-tree argument against tangle learning as unproven future work.
  - DTL is outside B1–B3 (model) and B6 (mechanism). B4 has no theorem.
  - Step 3: SIGNED with caveats.
- NEEDS:
  - L-ALG or L-RED (via the Lead): run dtl and idtl on counter_dftl and counter_odftl from origin/dftl. L-LIT cannot build Oink (no Boost in this container).
  - owner: the 2024 chapter "Solving Parity Games, Very Slowly", only if wanted.
