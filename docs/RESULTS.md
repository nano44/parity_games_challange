# Results ledger: only checked results
Each entry: label (formalized | refereed-only), statement, commit SHA, referee reports, CHECKER report.
Nothing enters here without passing the gauntlet (TARGET.md section 5).

## Results
### R1 [refereed-only] L4: vertex-priority strong separators need quasi-polynomially many states (2026-10-15)
- Signed claim (both referees, exact wording), proof docs/struct/L4-proof.md at l-struct 50dc28b (copied to trunk). Definitions:
  docs/struct/S1-statement.md (E/S/V conventions, s^X, w^X), docs/struct/S2-lower-bound-statement.md §1 (algorithm class (i)-(iii)),
  docs/struct/S3-statement.md D6 (TARGET alphabet, S(n) = s^V(n,n)); all copied from l-struct 50dc28b. Convention: here d is the
  largest letter of the alphabet Σ_d = {1..d}, not TARGET's d = |pr(V)|.
  Lemma L4.1, for k ≥ 1 and d ≥ 2, on infinite words: s^E(k,d) ≤ s^V(kd,d) and w^E(k,d) ≤ w^V(kd,d) (Parys-Wiacek conversion);
  Lemma L4.2 (monotonicity in n, d); Theorem L4 for n ≥ 2: S(n) ≥ max over even d' with 2 ≤ d' ≤ n of
  C(⌊lg⌊n/d'⌋⌋ + d'/2 − 1, ⌊lg⌊n/d'⌋⌋); Corollary L4.3: S(n) ≥ C(a0+b0, a0) for n ≥ 64 (a0 = ⌊½ lg n⌋ − 2, b0 = ⌈√n/2⌉ − 2),
  so S(n) = n^{Ω(lg n)}; Corollary L4.4 (theorem part only): any algorithm of class (i)-(iii) using a deterministic strong separator
  of the TARGET alphabet takes ≥ n·S(n) steps. Excluded: the literature sentence in L4.4.
- Referees: REFEREE (first) OK at 50dc28b, docs/referee/2026-10-14-L4-proof-check.md (referee 9bf5301); REFEREE-2 OK,
  docs/referee-2/R2-L4.md §7 (referee-2 d76c9e1). CHECKER PASS: docs/checker/C1-report.md (checker 62cf1c4).
- Gaps (union, see R2-L4.md §7): CDFJLP Thm 5.1 (arXiv 1807.10546) used as a black box (G-L4-1); first referee G1-G6.
- Status: supporting lemma, not claimed as M3 (Lead reading L7). Credit: conversion remark Parys-Wiacek 2305.00308 p.2;
  Claim R by L-LIT; sharpening by REFEREE; write-up L-STRUCT.

### R2 [refereed-only] T-A1: exact characterisation of psolB's completely-solved games (2026-10-15) — M3 (L9), novelty T10 NEW, CHECKER PASS (docs/checker/C1-report.md, checker 62cf1c4)
- Signed claim (both referees, at l-attr 57a1515; docs/attr/TA1-proof.md copied to trunk): Theorem T-A1: for every finite parity
  game G (TARGET §1), Huth-Kuo-Piterman's partial solver psolB (arXiv 1405.0386v2) solves G completely iff PA**(G).
  T-A1': PA**(G) ⟹ psolQ solves G completely; the converse is false (HKP Fig. 4(a); n=2 game `0 0 1 0,1; 1 2 0 0`).
  Corollaries 1-2 as stated in the file (HKP's Büchi, SCC-constant and deterministic classes ⊆ PA**, via HKP's theorems);
  Remark 3 (holds for every stable colour order). Excluded: Remark 4 (inclusions among the predicates PA, PA*, PA**; data only, not signed).
- Referees: REFEREE OK, docs/referee/2026-10-14-TA1-proof-check.md signature (referee d1e065b); REFEREE-2 OK,
  docs/referee-2/R2-TA1.md §8 (referee-2 2eb1a2d). Machine evidence: all 3-vertex games (both referees, own code), 490,944 games
  (REFEREE-2), random n=4,5; lane: all 27.3M canonical 4-vertex games for the psolQ-failure side.
- Gaps: G1-G9 closed; G10 open (dependency on HKP's proofs of Thm 7, Thm 8, Lemma 5; re-derived informally by both referees);
  G11 (HKP Thm 4, used by T-A1') closed at referee level ONLY with REFEREE-2's witness-successor repair of HKP's strategy
  (both referees: REFEREE answer (b), referee 5ff8edb, re-derived with the witness successor); Corollary 2 uses HKP Thm 5(1) as a black box (first referee's list); all steps are prose,
  nothing machine-checked beyond the data searches. Source note: the first referee did not open DJT (arXiv 2003.08627) §2; the trap
  definition used is stated in full in TA1-proof §1 and matches HKP Def. 2. Side finding: HKP Thm 4's proof defines an unsound minimal-rank
  strategy (REFEREE-2 counterexample docs/referee-2/R2-TA1/hkp_thm4_strategy.py; repair: witness successor); theorem unaffected.
- Status: M3 "a tighter analysis of a known algorithm" (Lead reading L9). Novelty: L-LIT T10 (docs/lit/T10-PAstarstar.md, l-lit 1f9e9f8):
  exact class NEW (HKP give sufficient classes only; Ah-Fat-Huth 2016 leave it open); PA** NEW as a condition (ingredients known:
  HKP fatal attractors, DJT traps); HKP Thm 4 proof flaw NEW (v1 = v2, no erratum). Chapter check (L-LIT T11, docs/lit/T11-HKP-DTR15-4.md,
  l-lit 933dc12): HKP's LNCS 9560 chapter (DOI 10.1007/978-3-319-27810-0_8) read as its pre-publication text Imperial DTR15-4
  (identical 29-entry reference list; Springer pages not opened): T10 verdicts unchanged, no G10 closure, Thm 4 flaw absent there.
  CAVEAT: the Springer pages are needed only before any external 'first' claim (owner, D4/L12). Also explains DE1 (2511.03752): its errors lie where no PA** piece can go first.


### R3 [refereed-only] Original Random-Facet on parity games (2026-10-15) — M3-type (L21), novelty T13 NEW as statement, CHECKER PASS (docs/checker/C2-report.md, checker 068f9de)
- Algorithm: original Random-Facet strategy improvement (Matousek-Sharir-Welzl / Kalai; FHZ arXiv 1410.7530 section 2 and errata
  1410.7871; = Zwick 2607.06334 Fig. 1 Random-Action-Removal with Voge-Jurdzinski valuations and the STRICT improvement test,
  ties not switched).
- Claim: started from sigma_{B_0}, B_0 any tree of FHZ zero-edges, the algorithm performs e^{Omega(sqrt n)} expected improving
  switches on the one-sink parity games P_{n,r,s,t}, where n is FHZ's bit parameter and r = Theta(log n), s = Theta(sqrt n log n),
  t = Theta(log n). These games have N = Theta(n^{3/2} log^3 n) vertices and edges, so, equivalently (FHZ's own form, N = Theta(M)), the bound
  is e^{Omega(N^{1/3}/log N)} in the game size. Priorities O(nrs), compressible to {0..|V|} (TARGET section 1).
- Proof: FHZ 1410.7530 Thm 6.3 (shortest paths) plus L-RED's Transfer Lemma (docs/red/R2-RAR.md at l-red 49ae306): for every tree
  B and edge e not in B, e is strictly improving in G_{n,r,s,t} iff its image is strictly improving in P_{n,r,s,t}, ties included; hence
  the run distributions coincide.
- Signatures: REFEREE (docs/referee/R-TL2.md sections 8-9, referee 42f11c6/5ed56c5, condition met at l-red 49ae306) and
  REFEREE-2 (docs/referee-2/R2-TL.md section 6, referee-2 94dde7b, at l-red 49ae306).
- Gaps: G-TL-1 FHZ Thm 6.3 used as a black box (asymptotic parameters). G-TL-2 the lemma is proved in prose; exhaustive machine
  checks cover only small (n,r,s,t) (REFEREE-2 435,584 tests; REFEREE ~308M tests). G-TL-3 S1's strict test and zero-edge start
  conventions are read from si.py (l-si 95d37d3); a non-strict test or another start is outside Thm 6.3's hypothesis. G-TL-4 Zwick's
  RAR is defined on AUSOs; P has ties, so the strict convention is part of the algorithm's definition (Zwick's analysis not
  invoked). G-TL-5 the lemma is specific to G_{n,r,s,t}, not a general shortest-path-to-parity reduction. G-TL-6 priority
  compression stated, not formalised; nothing Lean-checked. G-TL-7 code (fhz.py, vj.py) is evidence, not part of the signed
  statement.
- Status: M3-type "tighter analysis of a known algorithm" (Lead reading L21, corrected 13:40Z). Novelty: NEW as a published
  statement, low technical novelty (L-LIT T13, l-lit c962d80); Hansen 2012 thesis unopened. Also kills L-SI candidate S1 (DE6).

### R4 [refereed-only] GAP-C Step 5 for A_DTL: KT survives every depth-0 P piece, with (ACYC) as the only open hypothesis (2026-10-17) — partial step-4 lemma (not M3, not a step-4 pass), CHECKER PASS (docs/checker/C4-R4-step5.md, checker 7d7c6fb + re-diff fd8e3eb)
- Object: A_DTL = `oink --dtl --no-single --no-wcwc --no-loops` @ 8fbf0a7, every order datum (frozen §0, L26). G' = the game at the
  start of a search(p); D = W_p(G'). A depth-0 P piece is, as in STEP5.md line 9, "the −1 branch with Q empty, dtl.cpp
  961-991" at depth 0 (best_vertices 643-776 returned −1); R is its context and Y_0 the set it removes. Packet: docs/alg/STEP5.md and docs/alg/GAP-C.md §18g-§18k at trunk 8f41be8.
- Claims signed (both referees, all labelled "(Opus 5.5, D12)"):
  (1) KT(R) definitions; KT(G') holds when D ≠ ∅; KT(R_end) fails.
  (2) Lemma NT-f: the final pruning round of a −1 call accepts no stored tangle in its region loop.
  (3) FM (Z_f ⊆ Z^r for every round r of a −1 call) and WM (Z^r ⊆ A^r_t, GAP-C §18k), as consequences of NT-f.
  (4) The (YZ) reading of dtl.cpp 961-976, and (YZ) ⇐ (ACYC).
  (5) Lemma P-KT, given (YZ): at every depth-0 P piece with D ∩ R ≠ ∅, KT(R \ Y_0) holds (witnessed at level c1).
  Hence: at every depth-0 P piece with D ∩ R ≠ ∅, KT(R \ Y_0) holds, with (ACYC) as the only open hypothesis.
- Signatures: REFEREE docs/referee/R-STEP5.md (referee 8c2d012): (1)-(3) SIGN, (4) SIGN + SIGN WITH GAPS, (5) SIGN WITH GAPS.
  REFEREE-2 docs/referee-2/R2-STEP5.md (referee-2 ce37984, comparison §9 at a18e9e5): (1),(2),(4),(5) SIGN WITH GAPS, (3) SIGN.
  Independent (REFEREE-2 read docs/referee/ only after pushing ce37984). No REJECT.
- Gaps (union of both reports). G-S5-1..5 are closed in the reports and are to be imported into the author's text; G-S5-6 is
  OPEN; G-S5-7 lists dependencies checked only for this use:
  G-S5-1 NT-f (D) needs DTL-proof Lemma 1.5a (top ∈ t, tpr(t) = max pr(t)), re-derived by both referees (F2.1 / G2).
  G-S5-2 (YZ) ⇐ (ACYC) (iii): both inclusions, regions and Dom part as least fixed points with tangle retrial at escape pops,
         DTL-proof Lemma 1.2 (G4.1).
  G-S5-3 trigger case: a new opponent vertex whose R-edges all lie in earlier parts would have been taken there (G4.2 / G3).
  G-S5-4 P-KT case c1 = 0 (p Even): A^r_{−1} := Z^r, candidacy at dtl.cpp 714 (G5.1 / G4).
  G-S5-5 "all its edges" in A_c means edges of G' (REFEREE-2 G1; REFEREE wording note); whole-game edges make P-KT (4) false.
  G-S5-6 OPEN hypothesis (ACYC): the new part of a Dom(prevV) straddle contains no tangle-graph cycle. DATA only.
  G-S5-7 Lemmas 1.5a and 1.2 of DTL-proof.md checked by the referees only for this use; sorted indices (oink.cpp:35);
         O1 (index order follows priority) is an Oink order-datum fact; positional determinacy and D = W_p(G')
         (DTL-proof.md Lemma 1.4c; REFEREE §6.6, REFEREE-2 'standard parity-game facts named in (1)'), standard.
         Nothing Lean-checked.
- Scope: depth-0 P pieces of one search only. The S step ((S-LOW), data) and T step (CORE-PASS + REC, data), hence (K-in)
  and GAP-C as a whole, are NOT established. GAP-A untouched. Gauntlet step 4 stays open.
- Data (evidence, not part of the signed statement): REFEREE step5_probe.py (Python ref; 243 of the 254 corpus files: n > 80 and one unreadable file skipped; both orders):
  NT-f 0/8,323 and 0/8,145, YZ 0/4,476 and 0/4,377. REFEREE-2 instrumented pinned C++ (docs/referee-2/R2-STEP5/), 254 corpus
  + 3,000 random/unions + 9,000 climb mutants (each in 2 in-orders), 32,026 runs: 0 NT-f / FM / YZ / ACYC / tpr violations. In the corpus the only straddling Dom
  firing is strfam_S5_n46 stable order (both referees; Lead and CHECKER re-ran pinned Oink: 6 iterations, verified); REFEREE-2's
  climbs from it (18,000 runs) produce many straddling firings, none with a cyclic new part or a YZ failure (no total count
  kept). CHECKER C4 (checker 7d7c6fb) reproduced REFEREE's probe and REFEREE-2's corpus and random parts exactly.

### R5 [refereed-only] Eleven structural lemmas on A_DTL (GAP-C support and GAP-A conditional bound) (2026-10-17) — partial step-4 lemmas (not M3, not a step-4 pass), CHECKER PASS (docs/checker/C5-R5-packet2.md, checker c14c09f + re-diff 1209739)
- Object: A_DTL = `oink --dtl --no-single --no-wcwc --no-loops` @ 8fbf0a7, every order datum (frozen §0, L26). Packet: the
  fleet's unrefereed PROVED readings, pinned at trunk 43d63b0 (REFEREE) and 20fe2ed (REFEREE-2); statements as in the cited
  sections at those pins, with the readings fixed by the referees (below).
- Claims signed (both referees, all labelled "(Opus 5.5, D12)"):
  (a) Lemma SCC1 (GAP-C §3): in a closed sptl region Z_τ every vertex reaches τ in extractTangles' graph, so extractTangles(τ)
      finds at most one nontrivial SCC, the set C_τ reachable from τ.
  (b) Lemma B-thr (GAP-C §3), in the stronger form "(a) always": if C_τ equals a stored tangle t, then τ ∈ t, every escape of t
      lies outside the context R, and the last escape of t to leave the current call's context chain was popped in an
      attractor with threshold < pr(τ). Branch (b) of the stated lemma is vacuous (F-b3), so GAP-β = (β-a).
  (c) Theorem A (GAP-C §13): if the root call of search(p) is stable, the lowest region of its first sptl pass lies in W_p(G')
      and, if closed (no (α)), is productive (learns a new tangle or finds a dominion).
  (d) Lemma O0 (GAP-C §6): at the start of search(p) there is no orphan. Lemma O1 (GAP-C §6) as stated there.
  (e) Lemma OPP-EXIT (GAP-C §11), with conclusion π(o) ∉ Z_τ: the SCC C_τ extracted at a closed top τ meets W_{1-p} only
      where the opponent's winning move is an edge the region forgives.
  (f) Lemma K0 (GAP-C §18b): K(G') holds when W_p(G') ≠ ∅ and K(R_end) fails, with edges of G'.
  (g) Phases ≤ D + 2, where D ≤ n is the number of searches that find a dominion (GAP-A-M §21c; run() loops C5-DTL.md
      lines 141-142; --dtl is non-interleaved).
  (h) First-Difference Lemma (GAP-A-M §21d), stated on the call log with repeated sptl passes (dtl.cpp 870-874) deleted.
      POST-LANDING NOTE (2026-10-17 12:15Z by date -u): REFEREE-2 R2-P4 (referee-2 352da6e) re-opened part of (h) as gap
      G-STR: (ii)-(iii) compare set outputs only, but extraction reads str (dtl.cpp 268), so an equal-set tattr with different
      str could change an extracted SCC before the first set difference. (h) holds GIVEN (STR-DET) "equal set outputs before a
      point imply equal extracted SCCs before it" (DATA: 0 of 4,290 same-phase pairs), or its weak form (STR-DET-w) "s+1 creates
      no tangle before its first set difference, and none at all if there is none" (R2-P4 §8, 69b38ab). REFEREE R-P4 §C
      (e0cb163) agrees G-STR is real (str written at 89 or 171 depending on which rule fires first; 268 reads it with no set
      test) and revises (h) to SIGN WITH GAPS: (h) holds given (STR-DET-w), and holds unconditionally for transitions whose
      first difference is in the ROOT best_vertices call (no extraction before it; best_vertices reads str only at 73), an
      exemption signed by both referees (REFEREE-2 R2-P4 §9, 5ae9747). No instance either way. GAPS G-STR.
      UPDATE (2026-10-17 12:42Z by date -u): G-STR CLOSED. L-ALG's Lemma STR-DET (GAP-A-M §22i) is signed by both referees:
      REFEREE R-P5 (referee ca03021; SIGN WITH GAPS, closed: W-a1, G-a2) and REFEREE-2 R2-P5 (referee-2 6d508da; SIGN). Both
      state that (h) now holds without the (STR-DET) condition, for every first-difference location. Landing as RESULTS R8.
  (i) Lemma DV*-MONO (GAP-A-M §21h), reading INF as "never dropped".
  (j) The per-context LRN budget: at most n(n + 1) LRN transitions per distinct context per phase (GAP-A-M §21j), with
      REFEREE-2's reading of LRN (R2-PROVED2 §10).
  (k) Conditional bound: if (SPP) "searches per phase ≤ |G'|" holds for every order datum, then A_DTL makes ≤ n(n + 2)
      searches and runs in O(n^10 (m + n²)) word operations, and unit cost equals bit cost under TARGET.md §3.
- Signatures: REFEREE docs/referee/R-PROVED2.md (referee 50f2546; comparison §C ef6cf37, §C5 88d8e4c): (a),(c),(d),(f),(g),(i),
  (j),(k) SIGN; (b),(e),(h) SIGN WITH GAPS, all closed. REFEREE-2 docs/referee-2/R2-PROVED2.md (referee-2 581902f; comparison
  §13 72d1cd2): (a),(d),(g),(i),(j) SIGN; (b),(c),(e),(f),(h),(k) SIGN WITH GAPS, all closed. Independent (each read the other's
  report only after pushing its own). No REJECT. After comparison no gap of the packet is open in either report.
- Gaps (union of both reports and comparisons). G-R5-1..7 are closed in the reports; imported into the author's text at
  l-alg d67c5c8, and the REFEREE-2 G-b1 closure in G-R5-1 at l-alg 0743478; G-R5-8 lists dependencies:
  G-R5-1 B-thr: escapes solved before the search via O0 (REFEREE G-b1 = REFEREE-2 G-b3); "last escape" = the pop at which it
         leaves the current call's context chain (REFEREE G-b2); tangles created in the current search cannot recur in a
         later context of that search (REFEREE-2 G-b1, closed R2 §13.2, signed by REFEREE §C5, dtl.cpp 879-880, 885, 914-955).
  G-R5-2 Theorem A: read on the first sptl pass with premise "Z_k closed" (REFEREE-2 G-c1, same reading in REFEREE §c).
  G-R5-3 OPP-EXIT: conclusion π(o) ∉ Z_τ; proof needs the tangle-rule and top cases (G-e1, G-e2).
  G-R5-4 K0: edges of G' (REFEREE-2, as R2-STEP5 G1).
  G-R5-5 FDL: log alignment with repeated sptl passes deleted (G-h1; closed by REFEREE-2 §13.1, accepted by REFEREE §C).
  G-R5-6 DV*-MONO: INF read as "never dropped" (R-i, adopted by both).
  G-R5-7 (k): Lemma W needs SCC1 (G-k1, closed by (a)); DTL-proof §3(c) off by a factor 2, harmless (G-k2).
  G-R5-8 Dependencies: DTL-proof §2.3 K4 and K5(ii) (Theorem A) and DTL-proof §3 (b)-(e), checked in outline only for
         this use; code facts C1-C6 of docs/referee/R-STEP5.md §0 (REFEREE hypothesis 5); (α) and Case B (GAP-K') remain
         open (REFEREE hypothesis 3), which is why (c) is conditional on no (α). Priorities renumbered to ≤ 2n + 2 under L26
         (REFEREE's (k) text says ≤ n; the O(log n)-bit conclusion is unchanged). Nothing Lean-checked.
- Finding outside the signed statements: DTL-proof.md K5 (i)/(iii) is FALSE as written (REFEREE-2, docs/referee-2/
  R2-PROVED2/k5.pg, 4 vertices; confirmed by REFEREE; pinned Oink solves k5.pg in 1 iteration, verified: the run is correct,
  the lemma statement is wrong). Corrected form in R2-PROVED2 §3. Theorem A uses only K4 and K5(ii) and is unaffected; the
  definition of (α) is to be restated against the corrected K5 (GAPS G-K5).
- Scope: (a)-(f) support GAP-C but do not establish completeness (GAP-K / K-in open). (g)-(k) do not establish GAP-A: (k) is
  conditional on (SPP), which is DATA only. Gauntlet step 4 stays open.

### R6 [refereed-only] Packet 3 on A_DTL: corrected K5 (K5''), (α) with Dep(Str), K6 closed case, Lemma O-P, and the first step of the GAP-A root-call angle (2026-10-17) — partial step-4 lemmas (not M3, not a step-4 pass), CHECKER PASS (docs/checker/C6-R6-packet3.md, checker 83bcc23)
- Object: A_DTL = `oink --dtl --no-single --no-wcwc --no-loops` @ 8fbf0a7, every order datum (frozen §0, L26). Packet pinned at
  trunk 6e0082f (docs/alg/GAP-C.md §18l, §18n, §18p; DTL-proof.md K5/K6); the Dep(Str) forms are stated in GAP-C §18q at
  l-alg 89f0f4e, as both referees signed them in their comparison sections.
- Claims signed (both referees, all labelled "(Opus 5.5, D12)"):
  (a) K5'' (GAP-C §18q): with A_< the rescue set below pr(τ_k) and Dep(Str) the derivation closure (rescue witnesses; for a
      fired tangle, its escapes and its old vertices outside Reg), A_< \ Reg ⊆ Dep(Str). Consequence: if the lowest region
      Z_k is open, then τ_k has a successor in A_< \ Reg ⊆ Dep(Str) ≠ ∅. Parts (i') and (ii) of K5' as written are signed too.
  (b) (α) with Dep(Str), direction ⇒ (GAP-C §18q): if Z_k is open, τ_k has a successor in A_< \ Reg ⊆ Dep(Str). This is the
      direction used by K6 and the S step.
  (c) K6, closed case (GAP-C §18n; DTL-proof K6 note): a closed lowest region yields a new tangle, a dominion, or a (β')
      duplicate with no escape in R. It uses neither K5 (i)/(iii) nor K5'.
  (d) Lemma O-P, given (YZ) (GAP-C §18l, line 843 at 6e0082f): a depth-0 P piece creates no orphan.
  (e) GAP-A angle, first step (GAP-C §18p at 6e0082f), round r only: if the first difference e of consecutive searches
      s -> s+1 (reduced log) is in the root call's threshold loop at round r and level t_e, then for every level t ≥ t_e of
      round r the rescue set of s+1 contains that of s, and V_{r+1}(s+1) ⊇ V_{r+1}(s).
      Note (CHECKER C7 N-2, C8 addendum ca9188f; REFEREE R-P4 §C2): 'root call' here means the first best_vertices call of the
      search; read that way, (e) holds without (STR-DET), which RESULTS R8 in any case discharges.
- Refuted proof step (both referees, no instance, no run shown): K5'(iii') and (α) in the ψ-play Up(Str) form. A vertex pushed
  by a non-straddling fired tangle need not lie in Up(Str): configuration t' = {x, y, u, o} with u ∈ t' ∩ Z_k old, whose ψ is
  its region strategy (attractTangle skips u, dtl.cpp 169; 73 does not overwrite), so ψ-plays from x go x -> y -> {x, u}
  (REFEREE-2 R2-P3 §1, §6; REFEREE R-P3 §C). Whether the Up(Str) statement itself is false is open (L-RED box 7 item (4)).
- Signatures: REFEREE docs/referee/R-P3.md (referee e3f3256; comparison §C at 87f1043): (a) K5'' SIGN, K5'(iii') Up(Str)
  REJECT (withdrawn SIGN); (b) Dep(Str) ⇒ SIGN, Up(Str) REJECT, ⇔ form SIGN WITH GAPS (G-α1); K6 closed case SIGN WITH GAPS,
  closed; (d) O-P SIGN; (e) SIGN, round r only. REFEREE-2 docs/referee-2/R2-P3.md (referee-2 d555ebf; comparison §6 at
  f25feaf): (a) K5'' SIGN, K5'(iii') Up(Str) proof step REJECT, (i') and (ii) SIGN; (b) Dep(Str) SIGN, Up(Str) REJECT; K6
  closed case SIGN; (d) O-P SIGN; (e) SIGN, round r only. Independent (each read the other's report only after pushing its
  own). After both comparisons (REFEREE §C 87f1043 is the later one) the reports agree on every item R6 signs. Item letters
  here differ from the reports: R6 (d) = reports' (c), R6 (e) = reports' (d).
- Gaps (union of both reports and comparisons). G-R6-1..5 are closed in the reports and imported into the author's text at
  l-alg 89f0f4e; G-R6-6 lists dependencies and open hypotheses:
  G-R6-1 K5'' proof: the non-straddling fired-tangle sub-cases (in-R escapes all in higher regions: fires into the last such
         region; escapes in Z_k ∪ higher regions with one in Z_k: fires into Z_k) (REFEREE G-a1, G-a2; agreed by REFEREE-2).
  G-R6-2 Reading R-a: "Z_k ∪" in K5' is redundant (Z_k ⊆ Reg); Str read inside A_<.
  G-R6-3 K6 wording: (β') means "no escape in R" (in X, or in G' \ R at depth > 0); solved escapes excluded by O0 (REFEREE
         G-b1; REFEREE-2 "G' \ R at depth > 0").
  G-R6-4 R-b: W[τ_k] (dtl.cpp 528) cannot block extraction at a piece's first pass.
  G-R6-5 (α) in the ⇔ form needs G-α1: for a p-owned τ_k, read "no successor in Z_k" (str[τ_k] set at 73, closed at 515).
         R6 signs only the ⇒ form.
  G-R6-6 Dependencies: (d) is conditional on (YZ), which follows from the OPEN hypothesis (ACYC) (RESULTS R4, G-S5-6); (e)
         uses DTL-proof Lemma 1.2b (monotonicity of the attractor at fixed R, Gx = R, consume = None). Also open: K6's open case
         (orphan analysis and route are SKETCH; REFEREE open point 2) and orphans created by T pieces (REFEREE-2 §5).
         Nothing Lean-checked.
- Scope: (a)-(d) support GAP-C but do not establish completeness; after DE13 the S and T steps must be restated. (e) covers
  round r of the root call only; the later-round step is open, and RMONO (all rounds) is FALSE (DE14). Gauntlet step 4 stays
  open.

### R7 [refereed-only] Packet 4 on A_DTL: root-call monotonicity (PREFIX-MONO, POS-FALL, ROOT-BOUND) and the conditional reduction of GAP-A (2026-10-17) — partial step-4 lemmas (not M3, not a step-4 pass), CHECKER PASS (docs/checker/C7-R7-packet4.md, checker 09ea986 + addenda 8ea6c06, ad8434c, 544c3a9)
- Object: A_DTL = `oink --dtl --no-single --no-wcwc --no-loops` @ 8fbf0a7, every order datum (frozen §0, L26). Packet pinned at
  trunk 44d1428, docs/alg/GAP-A-M.md §22 (§22c PREFIX-MONO / ROOT-BOUND around lines 1929-1990; §22e reduction). A phase fixes
  G' and the player p; s -> s+1 are consecutive searches of the phase; e* is their first difference on the reduced log (FDL,
  RESULTS R5 (h)). A transition is CLEAN if every round of s+1's root best_vertices call is step-ideal, DIRTY otherwise.
- Claims signed (both referees, all labelled "(Opus 5.5, D12)"):
  (a) (S0): for every processed top τ of a round, P(τ) ⊆ Cl_{pr τ}(P(τ⁺) ∪ {τ}), where Cl_q is the TRIGGERED closure of the
      code (dtl_ideal.lfp: new vertices of priority ≤ q, a tangle needing an escape in the set).
  (b) Lemma PREFIX-MONO: if V ⊆ V′, T ⊆ T′ and the later round is step-ideal, then P(τ) ⊆ P′(τ) for every τ; with its
      corollaries C1-C4 (monotone unions and rescue sets, RMONO on clean transitions, NO-LATER).
  (c) (POS-FALL), for clean transitions with e* in the root call: if RV and Ψ are equal in s and s+1, Φ_top falls strictly.
  (d) Theorem ROOT-BOUND: Π = (RV, Ψ, Φ_top) rises lexicographically at every clean transition whose e* is in the root call;
      per phase, #(root-e* transitions) ≤ (#DIRTY + 1)·H + #DIRTY with H = (n(n+1)+1)((n+1)(d+2)n+1)((n+1)n²+1).
  (e) Conditional reduction (§22e, with both referees' additions): the number S of searches in a phase satisfies
      S − 1 ≤ Σ_{R ∈ C_bv} (D_R + 1)(H + 1) + n·|C_T| + #(Dom-e* transitions) + 1, given (STR-DET-w). Hence
      GAP-A ⇐ (CTX) ∧ (DIRTY) ∧ (DOM-e*) ∧ (STR-DET-w), where (CTX): polynomially many distinct first-difference contexts
      per phase; (DIRTY): D_R, the step-deficit points per context, polynomial; (DOM-e*): polynomially many transitions whose
      e* lies in a Dom tattr (dtl.cpp 878-890, 962-991); (STR-DET-w): s+1 creates no tangle before its first set-level
      difference from s, and none at all if there is none.
  (f) Bit cost: with S polynomial, the time bound of DTL-proof §3(e) (RESULTS R5 (k)) holds at bit cost; H, Ψ, Φ_top, RV are
      analysis quantities only.
- Signatures: REFEREE docs/referee/R-P4.md (referee f74857c; comparison §C e0cb163): (a) SIGN; (b) SIGN WITH GAPS, closed
  (R-b1); (c) SIGN; (d) SIGN WITH GAPS, closed (G-d1); (e) SIGN WITH GAPS, G-e1 (= DOM-e*) and G-STR OPEN, G-e2 closed (+1);
  (f) SIGN, conditional. REFEREE-2 docs/referee-2/R2-P4.md (referee-2 352da6e; comparison §8 69b38ab): (a) SIGN; (b) SIGN WITH
  GAPS, closed (G-Ψ); (c) SIGN, set-level, given FDL (ii); (d) SIGN WITH GAPS (G-Ψ), closed; (e) SIGN WITH GAPS, G-DOM and
  G-STR OPEN; (f) SIGN, conditional. Independent (each read the other's report only after pushing its own). No REJECT.
- Gaps (union of both reports and comparisons). G-R7-1..3 are closed in the reports and to be imported into the author's text;
  G-R7-4..6 are OPEN and are hypotheses of (e); G-R7-7 lists dependencies:
  G-R7-1 Cl_q is the triggered closure (dtl_ideal.lfp); the §22c prose rule lacks the trigger (REFEREE R-b1, REFEREE-2 (a)).
  G-R7-2 A round that returns at dtl.cpp 716 has no threshold loop: define W_{r,t} := Cl_t(U_r) there (REFEREE G-d1 =
         REFEREE-2 G-Ψ).
  G-R7-3 One transition per phase may have no differing tattr (the last, barren search): +1 in (e) (REFEREE G-e2, agreed
         REFEREE-2 §8).
  G-R7-4 OPEN (DOM-e*) / G-DOM: "e* never in Dom" is DATA only (REFEREE-2 corpus: 0 of 1,091 first differences in Dom); it
         needs an X-straddling Dom acceptance (seen on strfam_S5_n46). GAPS G-DOM.
  G-R7-5 OPEN (STR-DET-w) / G-STR: extraction reads str (268), written at 89 or 171 depending on which rule fires first, so set-
         level alignment of s and s+1 does not determine extracted SCCs (REFEREE-2; confirmed REFEREE §C). DATA 0 of 4,290
         pairs. The (STR-DET-w) wording is REFEREE-2 §8's; REFEREE §C signs the stronger form (STR-DET) and covers the
         no-difference case through G-e2, so both cover (STR-DET-w) in substance. It also conditions RESULTS R5 (h) except for
         root-call first differences, and RESULTS R6 (e) holds without it only if "root call" means the first best_vertices
         call of the search (REFEREE §C2). GAPS G-STR.
  G-R7-6 OPEN (CTX) and (DIRTY): DATA only (first-difference contexts ≤ 8 per phase; dirty ≤ 12 per phase, = K+1 on h4_defK).
         Also DATA only: Π rising on dirty transitions that do not lower RV (GAP-A-M §22d; REFEREE open point 3, REFEREE-2 §8).
  G-R7-7 Dependencies: FDL (RESULTS R5 (h)) for (c)-(e). For root-call first differences G-STR cannot arise (no extraction
         before e*; inside best_vertices no set test reads str: 73 tests only "== -1"), signed by REFEREE §C (e0cb163) and
         REFEREE-2 §9 (5ae9747); so (c) and (d) are independent of (STR-DET-w), which affects only non-root first differences. O1 (index order follows priority); DTL-proof 1.2b; DTL-proof §3(e).
         Nothing Lean-checked.
- Post-gate note: G-R7-5 (STR-DET-w) was discharged after this packet by Lemma STR-DET, signed by both referees (RESULTS R8).
- Scope: (a)-(d) are root-call statements; (e) is a reduction with four OPEN hypotheses, not a bound. GAP-A stays open; L-ALG
  §22f (unrefereed) sharpens (DIRTY) to (FALL) and finds (CTX) and (FALL) have different causes (§22g). Gauntlet step 4 stays
  open.

### R8 [refereed-only] Lemma STR-DET on A_DTL: equal set-level logs force equal extraction (2026-10-17) — partial step-4 lemma (not M3, not a step-4 pass), CHECKER PASS (docs/checker/C8-R8-strdet.md, checker 544c3a9)
- Object: A_DTL = `oink --dtl --no-single --no-wcwc --no-loops` @ 8fbf0a7, every order datum (frozen §0, L26). Packet pinned at
  trunk f920dc2, docs/alg/GAP-A-M.md §22i (L-ALG). s -> s+1 are consecutive searches of one phase; their reduced logs (repeated
  sptl passes deleted, RESULTS R5 (h)) are aligned up to a point π with equal inputs and equal set outputs before π.
- Claims signed (both referees, all labelled "(Opus 5.5, D12)"):
  (a) No tangle that s lacked when it computed a given sptl region before π (i.e. in T_{s+1} \ T_s^ρ for the region at point
      ρ < π) fires in that region in s+1.
  (b) Hence every sptl region computation before π is step-identical in s and s+1, str included.
  (c) Hence the extracted SCCs, the W bits and the `more` flag agree before π (on the reduced log; s's repeated pass is a pure
      repetition); s+1 creates no tangle before π.
  (d) A transition with no differing tattr ends in a barren s+1 (search returns false, dtl.cpp 1068; run() breaks, 1113/1120),
      so it is the last search of the phase (at most one per phase).
  Consequences signed by both: gap G-STR is CLOSED for every first-difference location (best_vertices, −1 attractor, sptl,
  Dom); the str part of G-h1 is closed; RESULTS R5 (h) (First-Difference Lemma) holds without the (STR-DET) condition; the
  (STR-DET-w) hypothesis of RESULTS R7 (e) is discharged.
- Signatures: REFEREE docs/referee/R-P5.md (referee ca03021): (a) SIGN WITH GAPS, closed (W-a1, G-a2); (b), (c), (d) SIGN.
  REFEREE-2 docs/referee-2/R2-P5.md (referee-2 6d508da): (a), (b), (c), (d) SIGN. Independent (neither read the other's P5
  report before pushing its own). No REJECT.
- Gaps (union; all closed in the reports, to be imported into §22i):
  G-R8-1 Wording W-a1: state (a) for T_{s+1} \ T_s^ρ (the tangle set s held at the region's point ρ), not T_s^π (REFEREE).
         REFEREE-2 signed (a) in the pin's T_s^π wording; its Case A ("t created by s in a later piece, at any depth") covers
         the W-a1 form in substance.
  G-R8-2 Case A's step Z_τ ⊆ Dom_P(s): the cited PREFIX-MONO absorbed case needs a step-ideal later run, which Dom is not
         known to be; correct argument: Dom's target is X (877-890) and attractTangle skips X vertices (136), the union of Dom's
         parts for tops ≥ τ is closed under the threshold-pr(τ) triggered rules (74-90; tangle rule at the last escape pop),
         so it contains Cl_{pr τ}(P(τ⁺)∪{τ}) ⊇ Z_τ by
         (S0) (REFEREE G-a2; REFEREE-2 gives the same D_{≥σ} argument in its own (a)).
  G-R8-3 Dependencies: context chain R-PROVED2 §C5 (RESULTS R5 (b)), SCC1 (R5 (a)), (S0) (R7 (a)), O1, DTL-proof 1.2b. Nothing
         Lean-checked.
- Data (evidence only): weak STR-DET 1,065/1,065 (Oink) and 1,035/1,035 (stable) on the corpus plus 4 instances, 3,377/3,377 on
  600 cross unions (stable) (L-ALG, GAP-A-M §22j, l-alg 6d79ce8, after the pin); 0 of 4,290 same-phase pairs (REFEREE-2 R2-P4 probe).
- Scope: STR-DET removes one hypothesis from the GAP-A reduction; GAP-A still needs (CTX) and (DIRTY)/(FALL) and the Dom term
  (RESULTS R7 (e); GAPS G-DOM). Gauntlet step 4 stays open.

### R9 [refereed-only] Packet 6 on A_DTL: per-context budgets reduce GAP-A to (CTX⁺) and (FALL) (2026-10-17) — partial step-4 reduction (not M3, not a step-4 pass), CHECKER PASS (docs/checker/C9-R9-packet6.md, checker a9258e6)
- Object: A_DTL = `oink --dtl --no-single --no-wcwc --no-loops` @ 8fbf0a7, every order datum (frozen §0, L26). Packet pinned at
  trunk 8ff4085, docs/alg/GAP-A-M.md §22f (line 2049) and §22j (line 2213), building on RESULTS R5 (h) (FDL), R7 (PREFIX-MONO,
  ROOT-BOUND, reduction), R8 (STR-DET). A phase fixes G' and p; S is its number of searches; e* is the first difference of
  consecutive searches on the reduced log.
- Claims signed (both referees, all labelled "(Opus 5.5, D12)"):
  (a) For every best_vertices context R, the potential Π_R is a function of (R, p, T) (no X or W read; str read only at 73, deciding a str write only); T grows along a
      phase; clean later visits never lower Π_R. Hence the e*-at-R transitions number at most (F_R + 1)(H + 1) (given STR-DET; see
      POST-LANDING NOTE), where F_R counts
      EVERY transition at R where Π_R does not rise (descents, incomparable steps, and Π-blind e* transitions).
  (b) For a fixed tattr input I of a −1 attractor or a Dom step, the output is a triggered closure monotone in T (DTL-proof 1.2b;
      for Dom, the closure triggered by the new part, with only the top pushed), so the transitions whose e* has input I form a
      strictly increasing chain: at most n per input. A −1 attractor's input is a function of (R, X) alone (dtl.cpp 898-912). A
      Dom step's input is (X ∪ Dom_{<j}, R \ Dom_{<j}, τ_j, pr τ_j), which depends on T and is NOT fixed by (R, X).
  (c) Hence S − 1 ≤ Σ_{R ∈ C_bv} (F_R + 1)(H + 1) + n·(|C_T| + |C_Dom|) + 1, where C_bv are the distinct first-difference
      best_vertices contexts, C_T the distinct −1 attractor contexts (R, X) and C_Dom the distinct Dom INPUTS at first
      differences; and GAP-A ⇐ (CTX⁺) ∧ (FALL), with
      (CTX⁺): |C_bv| + |C_T| + |C_Dom| is polynomial per phase;
      (FALL): Σ_R F_R (F_R as in (a)) is polynomial per phase.
      The (DOM-e*) hypothesis of RESULTS R7 (e) is no longer needed (absorbed into |C_Dom|).
      POST-LANDING NOTE (2026-10-17 15:35Z by date -u): REFEREE R-P7 §C (referee 1abe1d7) withdraws its R-P6 A4 premise that an
      e*-pair at R is a pair of consecutive visits of R (false when R is visited more than once per search). Corrected budget:
      #(e*-transitions at R) ≤ 2(F_R + 1)(H + 1) (a consecutive pair lies in at most 2 e*-intervals). The reduction GAP-A ⇐ (CTX⁺)
      ∧ (FALL) is unchanged; the per-context constant doubles. CONFIRMED by REFEREE-2 R2-P7 §7 (referee-2 94bcc2a), which withdraws the
      same premise in R2-P6 and adds: the per-input term of (b) is ≤ 2n (an input can recur within a search), so (c) reads
      S − 1 ≤ Σ_R 2(F_R + 1)(H + 1) + 2n(|C_T| + |C_Dom|) + 1. REFEREE R-P7 §C2 (referee 876c06e) confirms the +2F′ correction
      and agrees this doubled display is TRUE; it argues via STR-DET (c) that the original constants also hold ((F_R+1)(H+1)
      and n per input). REFEREE-2 R2-P8 §7 (referee-2 c2ac652) SIGNS that argument and withdraws its "2n needed". So, given
      STR-DET (RESULTS R8), R9's ORIGINAL constants in (a)-(c) hold with both signatures; the doubled display holds without
      STR-DET (c). Constants do not affect the reduction GAP-A ⇐ (CTX⁺) ∧ (FALL).
  (d) The remark that the raw per-input bound S − 1 ≤ n·|I_fd| + 1 is vacuous on data (|I_fd| ≈ S − 1) is DATA, used only as
      motivation.
- Signatures: REFEREE docs/referee/R-P6.md (referee 9f77ff9 + 0c0e3ce): (a) SIGN WITH GAPS (G6-a1, G6-a2, closed); (b) SIGN WITH
  GAPS (G6-b1 closed; G6-b2: Dom input not fixed by (R, X), so |C_Dom| counts inputs, OPEN inside (CTX⁺)), revised in the
  comparison §C (ad4be01) to SIGN once (CTX⁺) says "inputs" for Dom, as (c) here does; (c) SIGN.
  REFEREE-2 docs/referee-2/R2-P6.md (referee-2 5ef09aa; comparison §5 c7634a7): (a) SIGN WITH GAPS (G-F1 = G6-a1); (b) SIGN with
  reading R-I (the Dom input includes the whole current X; "fixed" means equal in s and s+1 at a first difference, not
  determined by (R, X)); (c) SIGN. Independent (each read the other's P6 report only after pushing its own). No REJECT. Item letters: R9 (b)+(c) = reports' (b); R9 (d) = reports' (c).
- Gaps (union). G-R9-1..3 closed in the reports, to be imported into §22f/§22j; G-R9-4..5 OPEN (they are the hypotheses);
  G-R9-6 dependencies:
  G-R9-1 F_R must count every non-rise of Π_R at R, not only descents (REFEREE G6-a1 = REFEREE-2 G-F1); data: 0 such non-
         descent non-rises after L-ALG's G-Ψ tool fix (one apparent case on cross union 411 was a tool artifact; full re-run
         of corpus, mixed and cross unions in both orders: 0, GAP-A-M §22n, l-alg e4e52ac).
  G-R9-2 §22f's display alone omits the Dom term and the +1 of R7 G-R7-3 (REFEREE G6-a2; agreed REFEREE-2 §5).
  G-R9-3 Dom pushes only its top (Q = {top}, Z = X), so DTL-proof Lemma 1.2 applies as "the closure triggered by the new part",
         same proof (REFEREE G6-b1; REFEREE-2 R-I). §22j's (CTX⁺) wording "contexts" of Dom steps reads "inputs" (REFEREE
         G6-b2, a wording item closed in the reports).
  G-R9-4 OPEN (CTX⁺), including Dom INPUTS: DATA only (first-difference contexts ≤ 10 per phase on the SPP families; Dom e* 0 on
         all data; REFEREE probe: Dom input varies at fixed (R, X, top) in 105/2,110 (stable) and 111/2,166 (Oink)
         phase-contexts, up to 4 inputs). (CHAIN) is FALSE (DE16).
  G-R9-5 OPEN (FALL): DATA only. "Descends only where RV falls" (73/72) is data; the "≤ 2 per context" maximum is BROKEN on data
         by L-RED fall3_n76 (experiments/red/carry/instances/fall3_n76.pg, sha1 a85133ec, docs/red/R31-fall3.md: 3 descents at one
         context, both orders; Lead re-ran pinned Oink (10 iterations, verified) and dtl_rootmono.py (max 3 per context, both
         orders; also re-run by CHECKER C9, a9258e6)), DATA unrefereed, which does not refute (FALL); "≤ 2" was never signed.
  G-R9-6 Dependencies: R5 (h), R7 (a)-(d), R8; DTL-proof 1.2b; phases ≤ D + 2 (R5 (g)); bit cost via DTL-proof §3(e) (R5 (k)).
         H's (d + 2) factor counts distinct threshold levels while the code loops t = 0..max_prio (dtl.cpp 721-722); still
         polynomial (REFEREE nit).
         Nothing Lean-checked.
- Scope: a reduction, not a bound. GAP-A stays OPEN on (CTX⁺) and (FALL), which have different causes (GAP-A-M §22g), so this
  is not the L32 single-statement criterion. GAP-C (completeness) is separate and open (DE13, DE15). Gauntlet step 4 stays open.

### R10 [refereed-only] Packet 7 on A_DTL: Lemma EXACT, PREFIX-MONO-X, and (FALL) ⇐ (NSTEAL) (2026-10-17) — partial step-4 lemmas (not M3, not a step-4 pass), CHECKER PASS (docs/checker/C10-R10-packet7.md, checker 383533b + re-diff 8f0f4db)
- Object: A_DTL = `oink --dtl --no-single --no-wcwc --no-loops` @ 8fbf0a7, every order datum (frozen §0, L26). Packet pinned at
  trunk d461a76 (REFEREE) and 357224b (REFEREE-2), docs/alg/GAP-A-M.md §22r (L-ALG). For a top τ of a round, P(τ⁺) is the
  union of the regions of processed tops of higher index; E_τ is the set of stored tangles that meet P(τ⁺) but are not inside
  it. A NEW STEAL at a consecutive visit pair of context R is a tangle t of the earlier visit's T with t ∈ E′_τ \ E_τ for some
  top τ processed in the earlier round (E′_τ computed from the later prefix, whether or not τ is processed there).
- Claims signed (both referees, all labelled "(Opus 5.5, D12)"):
  (a) Lemma EXACT: every best_vertices region step (dtl.cpp 690-705; the Dom loops and sptl are not claimed) is exactly the triggered closure Cl_{pr τ}(P(τ⁺) ∪ {τ}; T \ E_τ) (Cl as in
      dtl_ideal lfp_ref: new vertices of priority ≤ pr τ, a tangle needing an escape in the set).
  (b) Lemma PREFIX-MONO-X: if V ⊆ V′, T ⊆ T′ and there is no new steal (E′_τ ∩ T ⊆ E_τ for every τ processed in the earlier
      run), then P(τ) ⊆ P′(τ) for every τ.
  (c) Corollary: Π_R fails to rise between visits only at a new steal (including Π-blind e* steps), and
      F_R ≤ N_R^desc + N_R^e* ≤ 3·N_R, where N_R is the number of consecutive visit pairs of R in the phase that contain a new
      steal. Hence (FALL) ⇐ (NSTEAL): N_R is polynomial per phase for every first-difference context R; and
      GAP-A ⇐ (CTX⁺) ∧ (NSTEAL), given STR-DET (RESULTS R8, R9). (NSTEAL) implies (FALL), not the converse.
  (d) Data check on fallv_viol_n28 (RESULTS DE18): each fall is at a new steal; both falls of vertex 14 at the root are new steals
      of the SAME old tangle at different rounds, so "each tangle is newly stolen at most once per context" is FALSE.
- Signatures: REFEREE docs/referee/R-P7.md (referee 299bc58; comparison §C 1abe1d7): (a) SIGN WITH GAPS, closed (G7-a1, G7-a2);
  (b) SIGN; (c) SIGN WITH GAPS, closed (G7-c1, G7-c2), and in §C accepts REFEREE-2's G-P7-c2 (F_R ≤ 3·N_R; §C: "my claim that it held 'as stated' was
  wrong"); (d) agrees. REFEREE-2 docs/referee-2/R2-P7.md (referee-2 a66ff93;
  comparison §6 19e63f7): (a) SIGN; (b) SIGN; (c) SIGN WITH GAPS, closed (G-P7-c1, G-P7-c2); (d) confirmed. REFEREE-2 §6:
  REFEREE's (NS-COUNT) and REFEREE-2's (NSTEAL) are the same statement. Independent (each read the other's P7 report only
  after pushing its own). No REJECT.
- Gaps (union). G-R10-1..4 closed in the reports, to be imported into §22r (L-ALG §22t imports REFEREE's); G-R10-5 OPEN;
  G-R10-6 dependencies:
  G-R10-1 The rejection of a tangle with a consumed vertex is at dtl.cpp 138-139, not 137 (REFEREE G7-a1 = REFEREE-2 N-a1).
  G-R10-2 ⊇ of EXACT: mixed-premise rule instances are tried at a pop in Z_τ; vertices of P(τ⁺) are never escapes since
          Gx = CurR (80, 156) (REFEREE G7-a2; REFEREE-2's single last-pop argument).
  G-R10-3 Strict rise at e* comes from POS-FALL together with PREFIX-MONO-X's C4; Π-blind e* steps also need a new steal
          (REFEREE G7-c1 = REFEREE-2 G-P7-c1).
  G-R10-4 e*-pairs need not be consecutive visits of R, so F_R ≤ 3·N_R over consecutive pairs (REFEREE-2 G-P7-c2, accepted by
          REFEREE §C). "PREFIX-MONO is the special case" is the same proof pattern, not a special case (REFEREE note = N-b1).
  G-R10-5 OPEN (NSTEAL): DATA only and lossy (new steals : non-rises ≈ 9.5:1 REFEREE-2, ≈ 13:1 REFEREE).
  G-R10-6 Also open, inherited: (ACYC) (G-S5-6, a GAP-C item, listed by REFEREE-2). Dependencies: (S0) and PREFIX-MONO pattern (RESULTS R7), STR-DET (R8), the R9 reduction; O1 (oink.cpp 35,
          game.cpp 478-495). Nothing Lean-checked.
- Data (evidence only): EXACT held at every best_vertices region step in both referees' independent probes: REFEREE 477k
  steps (Python reference, own closure; non-rises detected via RV falls), REFEREE-2 463,742 steps (instrumented pinned C++, own
  closure; plus 420 random games; E_τ nonempty at 196,340 steps and the closure without exclusion differs from the code at
  24,259, so the exclusion is used); 0 non-rises without a new steal in either probe.
- Scope: a sharper reduction, not a bound. GAP-A stays OPEN on (CTX⁺) and (NSTEAL). L-ALG's later unrefereed refinement
  (GAP-A-M §22s-§22u: PREFIX-MONO-X* on fired tangles; (STEAL-ONCE), (FIRED-R), DATA) is not part of R10. Gauntlet step 4
  stays open.

### R11 [refereed-only] Packet 8 on A_DTL: only fired tangles matter (EXACT*, PREFIX-MONO-X*), and GAP-A ⇐ (CTX⁺) ∧ (STEAL-ONCE*) ∧ (FIRED-R) (2026-10-17) — partial step-4 reduction (not M3, not a step-4 pass), CHECKER PASS (docs/checker/C11-R11-packet8.md, checker 7a7d23c + re-diff 2031e13)
- Object: A_DTL = `oink --dtl --no-single --no-wcwc --no-loops` @ 8fbf0a7, every order datum (frozen §0, L26). Packet pinned at
  trunk a907c46, docs/alg/GAP-A-M.md §22s (EXACT*, PREFIX-MONO-X*) and §22u (chain), building on RESULTS R10. F_τ is the set of
  tangles that FIRED at top τ's best_vertices region step in the earlier visit. A RELEVANT STEAL at a consecutive visit pair of
  context R is a tangle of F_τ, for some τ processed in the earlier round, that the later prefix P′(τ⁺) meets without
  containing.
- Claims signed (both referees, all labelled "(Opus 5.5, D12)"):
  (a) Lemma EXACT*: every best_vertices region step equals the triggered closure Cl_{pr τ}(P(τ⁺) ∪ {τ}; F_τ) over the fired
      tangles alone (a corollary of RESULTS R10 (a): the code's derivation uses only F_τ, and F_τ ⊆ T \ E_τ).
  (b) Lemma PREFIX-MONO-X*: if V ⊆ V′, T ⊆ T′ and no tangle of F_τ (τ processed in the earlier run) is newly met-but-not-
      contained by the later prefix ((NS*), weaker than R10's (NS)), then P(τ) ⊆ P′(τ) for every τ.
  (c) Corollary: Π_R fails to rise between visits only at a relevant steal, and F_R ≤ 3·N*_R, where N*_R counts consecutive visit
      pairs of R with a relevant steal.
  (d) Conditional chain (§22u, with both referees' corrections): given (STEAL-ONCE*) "each (context, round, top, fired tangle)
      is a relevant steal at most once per phase", F_R ≤ 3(|R| + 1)·|R|·#fired(R), where #fired(R) is the number of distinct
      tangles that fire at R in the phase (rounds ≤ |V| + 1, dtl.cpp 748-760; tops are p-vertices of R). Hence, with (CTX⁺) for
      the sum over contexts, GAP-A ⇐ (CTX⁺) ∧ (STEAL-ONCE*) ∧ (FIRED-R), given STR-DET, where (FIRED-R): #fired(R) is polynomial
      in |R|.
- Signatures: REFEREE docs/referee/R-P8.md (referee fe4be51; comparison §C c0edb9c): (a) SIGN; (b) SIGN; (c) SIGN WITH GAPS,
  closed (G8-1); (d) VALID as a conditional. REFEREE-2 docs/referee-2/R2-P8.md (referee-2 b8fdd76; comparison §6 018ab0d): (a)
  SIGN; (b) SIGN; (c) SIGN WITH GAPS, closed (G8-1 = G-P7-c2); (d) VALID as a conditional, with G8-2 ((CTX⁺) for the sum) and
  the relevant-triple form (STEAL-ONCE*). Independent (each read the other's P8 report only after pushing its own). No REJECT;
  full agreement after comparison.
- Gaps (union). G-R11-1..3 closed in the reports (REFEREE's items imported by L-ALG in GAP-A-M §22w, l-alg c915af1; G8-2 and
  N8-1 still to be imported); G-R11-4..6 OPEN;
  G-R11-7 dependencies:
  G-R11-1 Over consecutive visit pairs the corollary needs the factor 3 (G8-1); §22s "F_R ≈ #relevant steals" and §22u's first
          line omit it. REFEREE-2 R2-P8 §7 (c2ac652) adds that, given STR-DET, the factor tightens to 2
          (overlapping e*-intervals overlap only where T is constant); one signature, not used here.
  G-R11-2 The per-context form "(FALL) ⇐ (STEAL-ONCE) ∧ (FIRED-R)" holds per context; the sum over C_bv needs (CTX⁺) (REFEREE-2
          G8-2, accepted by REFEREE §C). Only the relevant-triple form (STEAL-ONCE*) is needed.
  G-R11-3 Wording: §22s's ⊆/⊇ labels are swapped (REFEREE-2 N8-1); F_τ depends on the pop order of the earlier run, which is
          harmless because only the earlier run's F_τ is used (REFEREE; REFEREE-2 §6).
  G-R11-4 OPEN (CTX⁺): DATA only (max 13 first-difference contexts per phase at n = 40, L-RED ctx13_n40, re-run CHECKER C11:
          dtl_rootmono both orders, pinned Oink 29 iterations verified).
  G-R11-5 FALSE AS STATED (STEAL-ONCE*), see the POST-LANDING NOTE and DE20; before that: DATA only (max 1 on every set: corpus, specials, mixed and cross unions, both orders; REFEREE-2
          523 groups; L-ALG 665/703 (GAP-A-M §22w, mixed unions) and 325/338 (§22u, cross unions) phases with new
          steals).
  G-R11-6 OPEN (FIRED-R): DATA only and without any argument (REFEREE R-P8: "the obstruction is (FIRED-R)"): max 17 fired
          tangles at one
          context; the ratio to |R| reaches 0.62 (REFEREE) and 0.67 (REFEREE-2) on small contexts, so L-ALG's "≤ 0.5·|R|" is
          not robust. CAVEAT (L-ALG GAP-A-M §22w, l-alg 8642d5c as corrected 16:13Z): (FIRED-R) bounds a count of stored
          tangles, and the tangle count is GAP-A's own core (Lemma W: #fired(R) ≤ #tangles ≤ n·S), so it is unlikely to be much
          easier than GAP-A; its content is that the tangles active at one context do not grow with the phase length, and only
          long phases (S ≫ |R|) test it. (STEAL-ONCE*) is of a different kind (repetition, not size). Short-phase climbs reach
          15 fired tangles at |R| = 17 (0.88; stable order, dtl_pyref; Oink order 12 at |R| = 16 (0.75), then 13 (0.87)).
  G-R11-7 Also open, inherited: (ACYC) (G-S5-6, a GAP-C item). Dependencies: RESULTS R10 (EXACT, PREFIX-MONO-X), R9 (reduction; constants per its post-landing note), R8 (STR-DET).
          Nothing Lean-checked.
- Data (evidence only): EXACT* 0 failures in REFEREE's 481k and REFEREE-2's 927k best_vertices region steps; every non-rise at a
  relevant steal (REFEREE-2: 103/103 consecutive non-rises; 5 relevant steals at rises, = L-ALG's 5; 872 plain-only steals,
  all at rises), so the relevant-steal charge is nearly tight.
- Scope: a reduction, not a bound, to three open statements (not the L32 single-statement criterion); (FIRED-R) in particular
  is a tangle count close to GAP-A's core (G-R11-6 caveat). GAP-A stays OPEN on (CTX⁺), (STEAL-ONCE*) and (FIRED-R). Completeness (GAP-C) is separate.
  Gauntlet step 4 stays open.
- POST-LANDING NOTE (2026-10-17 19:28Z by date -u): hypothesis (STEAL-ONCE*) of (d) is FALSE on A_DTL under the stable order datum
  (RESULTS DE20, stealonce_viol_n76: 2 relevant steals of one fired tangle at one (context, round, top)); so are (STOLEN-PERM),
  (STAYS-MET) and (NO-REFIRE), L-ALG's route to it (GAP-A-M §23b). (a)-(c) are unaffected, and (d) remains VALID as a
  conditional, but its hypothesis fails, so (d) gives no reduction of GAP-A as stated. Lead reading (unsigned, not part of
  R11): the §22u count multiplies the number of (context, round, top, fired tangle) quadruples by the maximum number of relevant
  steals per quadruple, so (STEAL-ONCE*) would be replaceable by "relevant steals per quadruple are polynomially bounded"; that
  replacement needs both referees before it is used.

### R12 [refereed-only] Packet 9 on A_DTL: R11 (d) with the factor k, Lemma CHARGE, and GAP-A ⇐ (CTX⁺) ∧ (STEAL-DEPTH_D, D constant) ∧ (FIRED-R) (2026-10-17) — partial step-4 reduction (not M3, not a step-4 pass), CHECKER PASS (docs/checker/C12-R12-packet9.md, checker ed3a58c + re-diff cdc9009)
- Object: A_DTL = `oink --dtl --no-single --no-wcwc --no-loops` @ 8fbf0a7, every order datum (frozen §0, L26). Packet pinned at
  trunk c5e2b4d, docs/alg/GAP-A-M.md §23f (line 2904) and §23g (line 2944) (L-ALG succ. 7), building on RESULTS R10, R11 and
  the R11 POST-LANDING NOTE ((STEAL-ONCE*) FALSE, DE20). A quadruple is q = (R, round, top τ, fired tangle t); k_q is the
  number of consecutive visit pairs of R at which q is a relevant steal (an EVENT of q); Q := (|R| + 1)·|R|·#fired(R) bounds
  the number of q with k_q > 0. A RE-STEAL is an event of q after an earlier event of q. P(τ⁺) is the round's prefix before τ.
- Claims signed (both referees, all labelled "(Opus 5.5, D12)"):
  (a) F_R ≤ 3·N*_R ≤ 3·Σ_q k_q ≤ 3·k_R·Q (k_R = max_q k_q). Hence, given STR-DET and (CTX⁺) for the sum over contexts:
      GAP-A ⇐ (CTX⁺) ∧ (STEAL-POLY_sum), where (STEAL-POLY_sum): Σ_q k_q is polynomial per phase for every first-difference
      context R; and GAP-A ⇐ (CTX⁺) ∧ (STEAL-POLY_k) ∧ (FIRED-R), where (STEAL-POLY_k): k_R is polynomial.
  (b) Lemma CHARGE: every re-steal of q at pair i, with the previous event of q at pair j < i, has a CAUSE: an event at a pair m
      with j < m < i, at a step strictly earlier than (round, τ) in the step order (rounds ascending, tops descending).
      Distinct re-steals of one q have distinct causes (their open pair intervals are disjoint).
  (c) Depth: depth(first event) = 0; depth(re-steal) = 1 + min over its causes. If E_d is the number of events of depth d,
      E_0 ≤ Q and E_d ≤ Q·E_{d−1}; so (STEAL-DEPTH_D) "every event has depth ≤ D" gives Σ_q k_q ≤ 2Q^{D+1}. With (FIRED-R)
      (Q polynomial) this gives (STEAL-POLY_sum) for CONSTANT D only (D = O(log n) gives quasi-polynomial). Depth ≤ #steps − 1
      ≤ (|R|+1)|R| − 1 is proved, which gives only exp(Θ(n² log n)). Hence GAP-A ⇐ (CTX⁺) ∧ (STEAL-DEPTH_D, D constant)
      ∧ (FIRED-R), given STR-DET.
  (d) Data check on stealonce_viol_n76 (RESULTS DE20): one re-steal (stable order; tangle 7 at (round 4, top 18), k = 2, depth
      1, single cause: the depth-0 relevant steal of tangle 9 at (round 4, top 66)); none in the Oink order.
- Signatures: REFEREE docs/referee/R-P9.md (referee 72313f3 + a3e9566; comparison §C 3785d3f): (a) SIGN (its note N9-a1 WITHDRAWN in §C; accepts REFEREE-2 N9-a1); (b) SIGN
  WITH GAPS, closed (G9-b1, G9-b2; G23g-1/2 checked; N9-b1); (c) SIGN WITH GAPS, closed (G9-c1); (d) CONFIRMED (dtl_stealdepth
  unmodified + own probe p9charge.py). REFEREE-2 docs/referee-2/R2-P9.md (referee-2 2612634; comparison §5 19a94b8): (a) SIGN
  (N9-a1: name the form of STEAL-POLY); (b) SIGN WITH GAPS, closed (G9-b1, G9-b2 = REFEREE N9-b1); (c) SIGN (N9-c1); (d) own
  pinned-C++ probe an9.py. Independent (each read the other's P9 report only after pushing its own). No REJECT; full
  agreement after comparison.
- Gaps (union). G-R12-1..4 closed in the reports and imported by L-ALG (GAP-A-M §23k, l-alg 67b9e05; §23f-§23g not rewritten); G-R12-5..7 OPEN; G-R12-8 dependencies:
  G-R12-1 Notation: §23g's P_{j+1}(τ), P_i(τ) must read P(τ⁺) (the prefix before τ); as written "t ∩ P_i(τ) = ∅" is false
          since t fired inside region τ (REFEREE G9-b1 = REFEREE-2 G9-b1).
  G-R12-2 An intermediate visit may have fewer than r rounds: a "no candidates" stop (dtl.cpp 716/765) repeats its last round
          (virtual round, C3); a V′ = ∅ stop (768-771) forces an earlier-round steal (REFEREE G9-b2; REFEREE-2's rounds
          convention, R2-P7 §3).
  G-R12-3 The forms of (STEAL-POLY): the sum form needs no (FIRED-R) in (a); the k_R form and (c) need (FIRED-R) (REFEREE-2
          N9-a1, REFEREE G9-c1). Cite dtl.cpp 136-139, not dtl_pyref (REFEREE N9-b1 = REFEREE-2 G9-b2).
  G-R12-4 §23f's remark "the factor tightens to 2 given STR-DET (REFEREE-2 R2-P8 §7; one signature)": REFEREE N9-a1 called it
          misattributed; REFEREE-2 §5 and the Lead checked c2ac652:docs/referee-2/R2-P8.md §7 (line 139ff, "The same device
          tightens G-P7-c2 / G8-1 from 3 to 2, given STR-DET (optional)"); the citation is correct; the device is REFEREE's
          R-P7 §C2; REFEREE §C (3785d3f) WITHDRAWS N9-a1 (it had read R2-P8 at b8fdd76, before §7). Unused here.
  G-R12-5 OPEN (STEAL-DEPTH_D, D constant): DATA only; see RESULTS DE21 (depth 2/3/4 on a growing sequence). Before that: Every re-steal found has depth 1: 1 in the corpus (stable), 64 in 320
          random tie-break runs (REFEREE-2, all on stealonce_viol_n76, k_q ≤ 2); L-ALG: k max 1 on big unions (n ≤ 120,
          both orders); no re-steal elsewhere. Attack in progress (L-RED; L-ALG dtl_depthclimb).
  G-R12-6 OPEN (FIRED-R): DATA only, no route (L-ALG box 8 self-kills FIRED-STEP, FIRED-LAMINAR, FIRED-TOP-INJ, NO-RETURN).
  G-R12-7 OPEN (CTX⁺): DATA only (max 13). (CTX-LAMINAR) self-killed (GAP-A-M §23i).
  G-R12-8 Dependencies: R10 (EXACT, PREFIX-MONO-X and its Corollary incl. V alignment), R11 (a)-(c) (EXACT*, PREFIX-MONO-X*,
          F_R ≤ 3·N*_R), R8 (STR-DET), R9 (budget); also open, inherited: (ACYC) (G-S5-6, a GAP-C item).
          Nothing Lean-checked.
- Scope: a reduction, not a bound. CHARGE turns the steal count into a depth question but does not bound the depth. GAP-A
  stays OPEN on (CTX⁺), (FIRED-R) and (STEAL-DEPTH_D) (or directly (STEAL-POLY_sum)); all are DATA only, and only
  (STEAL-DEPTH) has a proof route. Not the L32 single-statement criterion. GAP-C is separate. Gauntlet step 4 stays open.
- POST-LANDING NOTE (2026-10-18 03:22Z by date -u): the hypothesis (STEAL-DEPTH_D, D constant) of (c) is FALSE on A_DTL in both order
  data: a UNIFORM family has re-steal depth = D (RESULTS DE21 addendum, experiments/red/lag/lagfam.py, n = 7D + 22). (a), (b)
  and (c) as a conditional are unaffected, but (c) gives no reduction of GAP-A; the routes via (STEAL-POLY_sum) (a), RESULTS
  R13 and R14 remain. Max re-steals per quadruple grow too (k = ⌊(D+1)/2⌋ + 1), so no constant-k form holds; (STEAL-POLY_k)
  is not refuted (k ≤ n).

### R13 [refereed-only] Packet 10 on A_DTL: Lemma ENTRY-CHARGE, and GAP-A ⇐ (CTX⁺) ∧ (EXIT_c) (2026-10-18) — partial step-4 reformulation (not M3, not a step-4 pass), CHECKER PASS (docs/checker/C13-R13-packet10.md, checker 1bd345d + re-diff 8886315)
- Object: A_DTL = `oink --dtl --no-single --no-wcwc --no-loops` @ 8fbf0a7, every order datum (frozen §0, L26). Packet pinned at
  trunk 1100f3a, docs/alg/GAP-A-M.md §23q (line 3244) (L-ALG succ. 7), building on RESULTS R11 (c) and R12 (a)-(b). One
  context R and one phase; steps σ = (r, τ) over a FIXED set (every round r ≤ |R| + 1 with the round convention of G-R13-1,
  every p-vertex τ of R); P_i(σ⁺) is the prefix before τ in round r at visit i. An EVENT is (i, q) with q = (σ, t), t ∈ F_σ(i)
  and t a relevant steal at the pair (i, i+1). An ENTRY of w at σ is a visit pair (i, i+1) with w ∉ P_i(σ⁺), w ∈ P_{i+1}(σ⁺);
  an EXIT is the reverse. N_ent and X_R are the numbers of entries and exits over all (σ, w).
- Claims signed (both referees, all labelled "(Opus 5.5, D12)"):
  (a) Lemma ENTRY-CHARGE: Σ_q k_q ≤ |R|·N_ent ≤ |R|·(X_R + (|R|+1)|R|²). Step 1: each event (i, q) gives an entry (σ, w, i)
      with w ∈ t (t fired at σ in visit i, so t ∩ P_i(σ⁺) = ∅ by dtl.cpp 136-139, 690, 699; the steal makes t meet
      P_{i+1}(σ⁺)). Step 2: at most |F_σ(i)| < |R| events share one entry, because every firing adds a new vertex
      (can_attract_new, dtl.cpp 142-146, 153-157, 169-172; the top is in CurZ from 693; a tangle fires at most once per step).
      Step 3: per (σ, w), entries ≤ exits + 1.
  (b) Corollary C1: GAP-A ⇐ (CTX⁺) ∧ (EXITS-POLY), given STR-DET, where (EXITS-POLY): X_R is polynomial per phase for every
      first-difference context R; no (FIRED-R) and no (STEAL-DEPTH) are needed.
  (c) Corollary C2: (EXIT_c) "each (step, vertex) exits at most c times per phase" gives Σ_q k_q ≤ (c+1)(|R|+1)|R|³; hence
      GAP-A ⇐ (CTX⁺) ∧ (EXIT_c) for any constant c, given STR-DET.
  (d) Corollary C3 (honesty): X_R ≤ N*_R·|R|·#steps, so (EXITS-POLY) ⇔ (STEAL-POLY_sum) ⇔ (RELSTEAL) up to polynomial
      factors: a REFORMULATION of a premise already in R10/R11/R12, not a reduction. What is new is the LOCAL sufficient form
      (EXIT_c).
  (e) Data: at most 2 exits per (step, vertex) on all data, both orders; 2 only on stealonce_viol_n76, stealonce_both_n45,
      stealonce_core_n76 and resteal34_union_n90.
- Signatures: REFEREE docs/referee/R-P10.md (referee aabcefd; draft 8f2db93, report a09a89d; comparison §C 434a552): (a) SIGN WITH GAPS,
  closed (G10-a1); (b) SIGN (N10-b1); (c) SIGN (constants: X_R ≤ c(|R|+1)|R|², F_R ≤ 3(c+1)(|R|+1)|R|³); (d) SIGN; (e) CONFIRMED
  (dtl_prefexits unmodified + own probe p10entry.py, 140 files, both orders, 0 failures). REFEREE-2 docs/referee-2/R2-P10.md (referee-2 0cbe61e; comparison §6
  57468a8): (a) SIGN WITH GAPS, closed (G10-a1); (b) SIGN (N10-b1); (c) SIGN; (d) CONFIRMED; (e) own probe an10.py, 268 files,
  both orders, 0 failures. Independent (each read the other's P10 report only after pushing its own). No REJECT; full
  agreement after comparison (REFEREE §C accepts the fixed σ set and confirms the shorter route; its probe's per-pair σ
  set gives only a lower bound on the fixed-set X_R).
- Gaps (union). G-R13-1..3 closed in the reports and imported by L-ALG (GAP-A-M §23t, l-alg 44e2bd8; §23q not rewritten); G-R13-4..5 OPEN; G-R13-6 dependencies:
  G-R13-1 Counting convention (both G10-a1, complementary halves): entries, exits and events are counted on ONE membership
          sequence per (σ, w): a FIXED σ set (every p-vertex τ of R, not "τ ∈ V_r" read per visit; REFEREE-2) and one round
          convention (repeat the last round after a "no candidates" stop (dtl.cpp 716/765); P = ∅ for later rounds after a
          V = ∅ stop (768-771); REFEREE).
  G-R13-2 FIRED-freeness is not new: R12 (a)'s sum form and R11 (c) ((RELSTEAL) via F_R ≤ 3·N*_R) are already free of
          (FIRED-R) (REFEREE N10-b1, REFEREE-2 N10-b1). What ENTRY-CHARGE removes is the #fired factor between exits and
          Σ_q k_q (compare EXIT-CHARGE, §23p, unrefereed).
  G-R13-3 Shorter route (REFEREE-2 N10-b1; confirmed by REFEREE §C, so two signatures): step 1 alone gives N*_R ≤ N_ent, so F_R ≤ 3(X_R + (|R|+1)|R|²)
          without step 2 or R12 (a); with (EXIT_c), F_R ≤ 3(c+1)(|R|+1)|R|².
  G-R13-4 OPEN (EXIT_c): DATA only; see RESULTS DE21 ((EXIT_2) FALSE: 3 exits on depth4_n53). Before that: c = 2 on all data (both referees' probes and L-ALG dtl_prefexits.py); L-RED's exit climb
          stayed at 2 (R37 addendum, l-red 59b3522).
  G-R13-5 OPEN (CTX⁺): DATA only (max 13); no route (CTX-ROOT DE17, CTX-LAMINAR, PIECES-LAMINAR dead).
  G-R13-6 Dependencies: R12 (a)-(b) (G9-b1 prefix convention), R11 (c), R10, R8 (STR-DET), R9; also open, inherited: (ACYC)
          (G-S5-6, a GAP-C item). Nothing Lean-checked.
- Scope: a reformulation, not a bound. GAP-A stays OPEN on (CTX⁺) and (EXIT_c) (or the equivalent (EXITS-POLY) / (RELSTEAL)),
  both DATA only; (EXIT_c) is a single local statement but has no proof yet, and (CTX⁺) has no route. Not the L32
  single-statement criterion. GAP-C is separate. Gauntlet step 4 stays open.
- POST-LANDING NOTE (2026-10-18 03:27Z by date -u): the local premise (EXIT_c) of (c) is FALSE for EVERY constant c on A_DTL in both
  order data: on the uniform family experiments/red/lag/lagfam.py (RESULTS DE21 addendum) the max exits per (context, step,
  vertex) are ⌈D/2⌉ + 1 (2/3/4/5/7 at D = 2/4/6/8/12; 3/4/5 at D = 3/5/7, REFEREE-2 R2-FAITH-lagfam). (a), (b), (d) and (c) as a conditional are unaffected; the route
  GAP-A ⇐ (CTX⁺) ∧ (EXITS-POLY) (b) remains: total exits per context on the family are 25/75/166/310/805 at n = 36/50/64/78/106
  (polynomial on these data).

### R14 [refereed-only] Packet 11 on A_DTL: Lemma CHANGE-NEW, F_R ≤ 3·#fired⁺(R) unconditionally, and GAP-A ⇔ (CTX⁺) ∧ (FIRED⁺-R) (2026-10-18) — partial step-4 reformulation (not M3, not a step-4 pass), CHECKER PASS (docs/checker/C14-R14-packet11.md, checker f89502d + re-diff 1af4995)
- Object: A_DTL = `oink --dtl --no-single --no-wcwc --no-loops` @ 8fbf0a7, every order datum (frozen §0, L26). Packet pinned at
  trunk 5909724, docs/alg/GAP-A-M.md §23s (line 3313) (L-ALG succ. 7), building on RESULTS R10 (EXACT), R11 (EXACT*,
  F_R ≤ 3·N*_R), R9 (budget). For a context R in a phase, D_R is the number of consecutive visit pairs of R whose set-level
  traces differ; #fired⁺(R) is the number of distinct tangles that fire at R (in a region step or in the threshold loop) in
  the phase; ntv(x) is the number of stored tangles when visit x starts.
- Claims signed (both referees, all labelled "(Opus 5.5, D12)"):
  (a) Lemma CHANGE-NEW: if two consecutive visits x < y of R differ at set level, then a tangle born between them (index in
      [ntv(x), ntv(y))) fires at R in visit y. Proof: within a phase the set-level trace of a best_vertices call is a function
      of (R, p, alive T, order datum) only (both referees' state inventories: V rebuilt from R 648/662-667; Candidates written
      at 714 before read at 735; Q empty on entry; str read only at 73; this->G read only at 132 and changed only at 1035;
      X, W, depth not read); tangles are only appended (stored 440/458-461; tpr = −1 only at 134; G changes only at 1035, ending
      the phase), so T_x ⊆ T_y; at the first differing tattr call the inputs agree; a region step is handled by EXACT/EXACT*
      (E_y ∩ T_x = E_x), the threshold step by DTL-proof Lemma 1.2 (all of Z pushed at 724, Gx = R).
  (b) Corollary: birth intervals of consecutive pairs are disjoint (ntv non-decreasing), so D_R ≤ #fired⁺(R); N*_R ≤ D_R; with
      R11's F_R ≤ 3·N*_R: F_R ≤ 3·#fired⁺(R) with NO premise. Hence GAP-A ⇐ (CTX⁺) ∧ (FIRED⁺-R), given STR-DET, where
      (FIRED⁺-R): #fired⁺(R) is polynomial per phase for every first-difference context R.
  (c) Honest limit: the bound is tight (spp_chain_up_n43: root D_R = #fired⁺ = 41, both orders), and over all contexts the
      conditional is an EQUIVALENCE: GAP-A ⇔ (CTX⁺) ∧ (FIRED⁺-R) up to polynomial factors, given STR-DET (GAP-A gives
      (FIRED⁺-R) via Lemma W, ≤ n·S tangles per phase, and (CTX⁺) via R5 (k)); a reformulation, not a reduction to something
      easier. At G′ alone (FIRED⁺-R) is implied by GAP-A but does not imply it; on chain families where every first
      difference is at the root (spp_chain_up_n43) it equals S − 1 (both referees). (L-ALG's unrefereed note at the end of
      GAP-A-M §23s relates the root case to (SPP); not part of R14.)
  (d) Data: CHANGE-NEW held at every differing pair checked: REFEREE p11probe.py (corpus 138 files, both orders, AT the first
      differing tattr) 1,160/1,160 and 1,231/1,231, and on spp_chain_up_n43 + stealonce_viol_n76 with dtl_changenew.py 89/89
      (stable) and 49/49 (Oink); REFEREE-2 (268 files, both orders) 3,028/3,028 and
      3,066/3,066; L-ALG dtl_changenew.py 37,361/37,361; D_R > #fired⁺(R) in 0 contexts.
- Signatures: REFEREE docs/referee/R-P11.md (referee fc86762; draft f953548; comparison §C abc5185): (a) SIGN WITH GAPS, closed
  (N11-a1, G11-a1); (b) SIGN; (c) CONFIRMED (equivalence); (d) CONFIRMED. REFEREE-2 docs/referee-2/R2-P11.md (referee-2
  aeedd00; comparison §5 bb8a625): (a) SIGN (N11-a1); (b) SIGN (N11-b1); (c) CONFIRMED (equivalence); (d) own probe, 0
  failures. Independent (each read the other's P11 report only after pushing its own). No REJECT; full agreement after comparison.
- Gaps (union). G-R14-1..3 closed in the reports and imported by L-ALG (GAP-A-M §23v, l-alg 510cb18, which marks N11-b1
  as one signature, written before REFEREE §C confirmed it; §23s not rewritten); G-R14-4..5 OPEN; G-R14-6 dependencies:
  G-R14-1 STR-DET is not needed for the determinism step: best_vertices reads str only at 73, to guard a str write (REFEREE
          N11-a1 = REFEREE-2 N11-a1). STR-DET remains a hypothesis of the GAP-A conditional through R9.
  G-R14-2 The threshold step follows from DTL-proof Lemma 1.2 directly (all of Z pushed at 724, Gx = R), not from "the §22r
          Corollary" (REFEREE G11-a1; REFEREE-2 §1 makes the same fix in substance).
  G-R14-3 Sharper use (REFEREE-2 N11-b1; CONFIRMED by REFEREE §C abc5185, so two signatures): an e*-at-R transition contains a differing
          consecutive pair and, given STR-DET (c), overlaps occur only where T is constant, so #(e*-at-R) ≤ D_R ≤ #fired⁺(R)
          (2·D_R without STR-DET); hence S − 1 ≤ Σ_R #fired⁺(R) + n(|C_T| + |C_Dom|) + 1, with no H and no F_R.
  G-R14-4 OPEN (FIRED⁺-R): DATA only; ≤ |R| on all data (tight: fired18_stable_n20 stable, #fired⁺ = |R|); at G′ it is necessary, not sufficient, and equals S − 1 on chain families;
          route via (EXIT_c) (GAP-A-M §23u, SKETCH, gap G23u, unrefereed).
  G-R14-5 OPEN (CTX⁺): DATA only; |C_bv| ≤ S − 1 per phase, best contexts/transitions ≈ 0.5 at n = 20, 30, 40 (L-RED box 9,
          unpinned, in progress).
          POINTER (2026-10-18, CHECKER C16): see L-RED R40 (docs/red/R40-tcL-contexts.md, l-red 2a75c4a): first-difference contexts in Even phase 0 are S − 3 (tcL(N), N ≥ 6) and S − 1 (leanT(N), n = 8N), both orders, i.e. linear in S and within an additive constant of the phase length S (no slack at all on leanT); no refutation of (CTX⁺).
  G-R14-6 Dependencies: R10 (EXACT), R11 (EXACT*, F_R ≤ 3·N*_R), R9 (budget), R8 (STR-DET), R5 (k), Lemma W (GAP-A-M), DTL-proof
          Lemma 1.2; also open, inherited: (ACYC) (G-S5-6, a GAP-C item). Nothing Lean-checked.
- Scope: an unconditional per-context bound (F_R ≤ 3·#fired⁺(R)) and a reformulation of GAP-A, not a bound. GAP-A stays OPEN on
  (CTX⁺) and (FIRED⁺-R) (the alternative sufficient pair (CTX⁺) and (EXIT_c) is RESULTS R13), all DATA only. Not the L32 single-statement
  criterion. GAP-C is separate. Gauntlet step 4 stays open.

### R15 [refereed-only] Termination of N5 (SSI-GLOBAL), and of every VJ00 strategy-improvement step sequence, by the potential (Ω, φ) (2026-10-18) — correctness half of gauntlet step 4 for N5 (not M3, not a step-4 pass; no running-time bound), CHECKER PASS (docs/checker/C17.md, checker 9e8f841 + re-diff c5a8c52)
- Object: N5 "SSI-GLOBAL" as specified in docs/new/N5-ssi-global.md, sections "Exact pseudocode" and "SPEC (EXACT ...)" S1-S5
  (L-NEW, (c) lane under D14/L35); reading docs/new/G-N5-TERM-reading.md pinned at trunk 812ecba (L-NEW successor 2). Source:
  Vöge-Jurdziński, "A Discrete Strategy Improvement Algorithm for Solving Parity Games", BRICS RS-00-48 (Dec 2000), pdf sha256
  485a12de… (opened independently by L-NEW and by both referees). Notation as there: Ωσ = (Λσ, Πσ), ⊴ on play values (§4.2),
  R+ / R− the priorities of ⊕ / ⊖, k_σ(u) the length component of Πσ(u).
- Claims signed (both referees, all labelled "(Opus 5.5, D12)"):
  (a) Lemma A: for any non-empty unambiguous set I of improvements of σ (VJ00 §4.4), Ωσ ⊴ Ω_{Switch_I(σ)}. This is VJ00 Lemma
      5.7 as stated (VJ00's Improve already allows any non-empty I); both referees checked VJ00's unproved Prop. 5.4 clause 2.
  (b) Lemma B: if moreover Ω_{Switch_I(σ)} = Ωσ, then every (v, w) ∈ I is a length-only switch at a cycle node: Λσ(v) = v,
      Λσ(w) = Λσ(σ(v)) = v, Πσ(w) ∩ V>v = Πσ(σ(v)) ∩ V>v = ∅, and k(w) > k(σ(v)) if v ∈ R−, k(w) < k(σ(v)) if v ∈ R+.
      (The cancellation uses "=_ℓ on pairs includes equal lengths": REFEREE G-B1 = REFEREE-2's reading of =_ℓ; closed.)
  (c) Theorem: with φ(σ) = Σ_{v ∈ M⊕, Λσ(v) = v} ε(v)·k_σ(σ(v)) (ε = +1 on R−, −1 on R+) and σ ≺ σ⁺ iff Ωσ ◁ Ωσ⁺ or
      (Ωσ = Ωσ⁺ and φ(σ) < φ(σ⁺)), ≺ is a strict partial order on strategies and every non-empty switch of improvements goes
      strictly up in ≺. Consequence: no strategy repeats in any VJ00 strategy-improvement run with any non-empty selection
      rule; φ is an integer with |φ| ≤ n(n−1).
  (d) N5: every iteration applies Switch_I with ∅ ≠ I ⊆ Iσ to Even's σ (on G) and/or with ∅ ≠ I ⊆ Iτ to Odd's τ (on G^d), and
      changes at least one of them (S4a/S4b, or the S4c fallback, a switch-all); Iσ depends on σ alone (Ωσ is against ⊖'s
      optimal reply, not against τ). Hence no (σ, τ) state repeats and N5 terminates within h(≺_G) + h(≺_{G^d}) iterations; at most 4n(n−1)
      consecutive N5 iterations leave both Ωσ and Ωτ unchanged (two potentials φ, φ^d).
- Honest limits: (i) termination only. h(≺) can be exponential; NO polynomial or other useful iteration bound follows, and the
  running-time half of G-N5-TERM and gauntlet step 4 for N5 stay open. (ii) G-N1 = G-N5T-1 (DATA, code link): (d) applies to
  experiments/new/n5.py to the extent that si.py computes VJ00's Ωσ and improvements; REFEREE: 0 mismatches in 22,969 vertex
  valuations (G and G^d); REFEREE-2: 0 mismatches on Even's side (3,000 random games, 23,943 strategies); improving() on Odd's
  side: REFEREE-2 §C (fd5abd8, si_vs_bf.py dual mode, G^d built as n5.py's dual()): 3,000 games, 21,205 strategies, 0
  valuation and 0 improvement-set mismatches; so si.py agrees with a VJ00 brute force on both sides (still DATA, not proof). (iii) G-N5T-3 (outside the packet): N5's output correctness at S5 rests on VJ00 Lemma 5.8 "1 ⇒ 2", which uses VJ00's
  unproved Lemma 5.9 and Prop. 5.10; not re-derived by either referee (every N5 output in the fleet's runs is verified
  independently: regions against Oink zlk, or Oink tl where zlk hit its cap (labelled per row), or harness Zielonka on random
  games; strategies by experiments/harness/verify.py).
- Side finding (signed as CONFIRMED by both referees; literature check L-LIT T21): VJ00 BRICS RS-00-48 Lemma 5.8's direction
  "Improve(σ) ≠ σ ⇒ σ not maximum" and postulates I1 and I2 FAIL at cycle nodes (instances: G-N5-TERM-reading.md §0; one-player
  prio [0,2,4], succ 0→{1}, 1→{0,1}, 2→{0,1}, σ = (0→1, 1→0, 2→0): switching (1,1) leaves Ω unchanged though σ is not
  maximal). The CAV 2000 version's p.13 sentence "in every strategy improvement step the current valuation strictly improves
  in at least one vertex" fails on L-NEW's instance (even for its own switch-all step) and, under p.12's arbitrary-subset switching, on REFEREE-2's
  (L-LIT T21, docs/lit/T21-VJ00-check.md, l-lit 9281eb5; CAV text quoted from T21, not opened by CHECKER). Not found in the
  literature checked; the strict-improvement claim is restated without exception in Friedmann arXiv 1106.0778 Thm 3.2,
  Fearnley-Savani arXiv 1507.04500 Lemma 2.3, van Dijk-Loho-Maat arXiv 2309.02223 p.6. Unaffected: "no improvement ⇒
  optimal" and weak monotonicity. (c) restores termination of VJ00-based strategy improvement. Fleet-internal (D1/D11).
- Data: REFEREE docs/referee/scratch/n5t_probe.py (from VJ00 §4 only): 83,472 switches, 3,855 flat, 0 failures of A, B, T;
  negative control fails on every flat switch (113/113). REFEREE-2 docs/referee-2/R2-N5T/vjbf.py (all-plays oracle): all
  3-vertex games (up to relabelling) + 5,000 random 4-7-vertex games and their 5,000 duals, 936,826 switches, 33,103 flat, 0 failures; mutation tests fail as they should.
  L-NEW: no repeated (σ, τ) state found (n5_lock.py, all start pairs, 1,600 games with n ≤ 8; all climbs; every step-2 run,
  12,000 random games and the M1 families, terminated).
- Signatures: REFEREE docs/referee/R-N5T.md (referee 87839f2 + 1cdcdc1; §C 368a7a7): SIGNED WITH GAPS (G-B1, G-B2, G-N2 closed;
  G-N1 DATA). REFEREE-2 docs/referee-2/R2-N5T.md (referee-2 0fb5fd2; §C §8 fd5abd8): SIGNED WITH GAPS (G-N5T-1 DATA, G-N5T-2 scope,
  G-N5T-3 outside; notes N1-N4). Both §C: no disagreement; joint gap list G-B1, G-B2, G-N2 (closed), G-N1 = G-N5T-1 (DATA, both sides), G-N5T-2 (scope), G-N5T-3 (outside), notes N1-N4 (applied by L-NEW as wording, e7157417 + 110a2228; statement unchanged from 812ecba). I1 counts agree: one-player n = 3, 2,270 triples, both referees independently.
- Gauntlet: N5 has passed step 2 (data; second implementation in progress, L-COMP) and step 3 (L-LIT T20, signed with caveats).
  This entry is a partial step-4 lemma (termination). GAPS G-N5-TERM: termination half closed by this entry on landing;
  running-time half open.

### R16 [refereed-only] A_DTL on one-player games 𝒞^1P: the search count per phase is n^{O(NEST*)}, so GAP-A on 𝒞^1P ⇐ (NEST*-BOUNDED) (2026-10-19) — partial step-4 reduction on a subclass (not M3, not a step-4 pass, not M4), CHECKER PASS (docs/checker/C19.md, checker 86f43ad + Addenda e2250d0, e6ed679)
- Object: A_DTL = `oink --dtl --no-single --no-wcwc --no-loops` @ 8fbf0a7, every order datum (frozen §0, L26). Class (GAP-A-M
  §27b): 𝒞_C (C ∈ {0, 1}): every vertex of player q = 1 − C has exactly one successor; 𝒞_C^dist adds: q's priorities are pairwise
  distinct; 𝒞^1P := 𝒞_0^dist ∪ 𝒞_1^dist. Packet P-C1P pinned at trunk 01d63d7 (docs/alg/GAP-A-M.md §27b, §28e, §33b, §35b, L-ALG
  successors 9-10; docs/red/R46-nest-bound.md §1, §2b, §3, L-RED successor 9) and addendum A1 pinned at trunk da63c40
  (docs/red/R47-chainkeep.md §1-§5, L-RED successor 9, l-red b9d7580).
- Claims signed (both referees, all labelled "(Opus 5.5, D12)"):
  (a) Lemma CTRL: in 𝒞_C every tangle that search(C) extracts is a dominion; player C makes ≤ n + 1 searches in the run.
  (b) Lemma NOSTEAL-1P: in 𝒞_C^dist, in every phase of q, under every order datum, there is no relevant steal (RESULTS R11
      definition) in any best_vertices context.
  (c) Lemma OUTCOME-MONO-1P: in 𝒞_C^dist, at a fixed context R in a q-phase, consecutive visits have monotone round sets
      V_r, a stable visit is followed by a stable one with V* nested, and a −1 visit by a stable one or a −1 one with
      emptying round e not smaller, and prevV nested when e is equal (e = the FIRST round with V_e = ∅).
  (d) Lemma SAME-CTX: equal depth-0 context SET R at a position in two searches of a q-phase ⇒ the call is a function of
      (R, T), its outcome does not fall, and with equal outcome the piece is ⊆-monotone (ρ carries the emptying round e;
      T-monotonicity on the consumed Dom subgame cites RESULTS R9 (b)).
  (e) Lemma LEX, in the form signed: at every transition whose depth-0 chain changes, the chain rises strictly in the
      tree-lexicographic per-context order; hence c(s′) ≤ c(s″) for all searches s′ < s″ of a phase. (The strict form "for ALL
      pairs" needs (CHAIN-CHANGE), DATA only; nothing below uses it.)
  (f) K-constraint (R46 §1): between two consecutive transitions at positions < p, at most K transitions have position p,
      K ≤ (n+2)²(n+1) = O(n³) (R46 §1 count; R47 §7 uses this signed K).
  (g) L-NEST* (R46 §2b): a sequence over m positions satisfying the K-constraint with NEST* ≤ d has length ≤ (2(d+2)m²K)^d;
      NEST* (first-to-last-occurrence nesting) is monotone under subsequences.
  (h) Lemma EMPTY-REC (R47 §1): in 𝒞_C (out-degree-1 hypothesis only), every recursive search_rec call of a q-search gets an
      empty subgame (dtl.cpp 898-955).
  (i) Theorem CK (R47 §2-§4): on 𝒞_C^dist every q-phase has I ≤ (n+1)(|P|+1)(H+1+n²) + 1 chain-keeping transitions (H from
      RESULTS R7 (d)), using Lemma DOM-MONO (fixed-input Dom step outputs monotone in T) and Lemma SPTL-SANDWICH; the case of e*
      in search()'s dominion attractor is excluded by STR-DET (RESULTS R8); CHECK_UNIQUE = 1 (dtl.cpp 23).
  (j) THEOREM (NEST*-BOUND with CK; R46 §3 + R47 §5): on 𝒞^1P every q-phase has S − 1 = |P| + I with
      |P| ≤ (2(d+2)(n+1)²K)^d, d = NEST*(P), and I as in (i). So S ≤ n^{O(NEST*)}, and with CTRL (≤ n + 1 searches for C) and
      the phase count, GAP-A on 𝒞^1P ⇐ (NEST*-BOUNDED): "NEST* ≤ c on 𝒞^1P for a constant c" (R46 §3; NEST* of the first-difference
      sequences P of the q-phases). ONE named statement; (CHAIN-CHANGE) is not needed.
- Honest limits: (i) a REDUCTION, not a bound: (NEST*-BOUNDED) is DATA only (class best NEST* 3: nest3_n20, nest3_n24), with no
  proof route; NEST* = Θ(log n) would allow up to n^{O(log n)}, so even its failure in that form would not give a super-polynomial
  lower bound. (ii) Subclass only: LEX fails in two-player games (GAP-A-M §36b), so (e)-(j) do not apply there; GAP-A in general
  is unchanged. (iii) The L32 criterion asks for one named statement WITH a proof route; this gives the statement, not the
  route. (iv) DATA caveats: REFEREE-2's DOM-MONO pairs (163) all had identical step vectors (vacuous as data; the verdict rests
  on the proof); REFEREE-2's logs are Oink order only.
- Data (DATA, not proof): REFEREE (lanes' tools, both orders): samectx 646 pairs 0 failures; lexchk 169 pairs per order 0
  violations; neststar K=2, d=2, m ≤ 3 far below the bound; dagchk 188 depth-≥1 calls, max |R| = 0. REFEREE-2 (own logging patch
  on pinned 8fbf0a7 + own analyser, Oink order): 13 pinned class instances, 0 violations of CTRL, CHAIN-CHANGE, LEX, K, the
  bound and CK (I = 0, total |P| = 79); 7,500 random class games 0 violations (trivial phases); nestbf = R46's tables. L-RED:
  DOM-MONO 12,043 + 1,434 same-input pairs per order, 0 violations (R47 §6).
- Signatures: REFEREE docs/referee/R-C1P.md (referee 2ad62df; §C 2d69929; A1 83c2916; §C-A1 4701783). REFEREE-2
  docs/referee-2/R2-C1P.md (referee-2 1ecc8d5; §C ff4011f; A1 8e7a02c + 22e5d2d; §C-A1 420b14b). Both §C-A1: no conflict. Closed gaps: S-1 = G-SC-1, S-2, S-3,
  G-SC-2 (REFEREE-2 citation point) (SAME-CTX), O-1/O-2 (OUTCOME-MONO-1P), N-1 (NOSTEAL-1P wording), R-1 (L-NEST* wording), A1-1..A1-5 and
  A1-G1/A1-G2, A1-N1..A1-N3. Closed by A1 for the theorem: R-2 = G-R46-1. L-1 = G-LEX-1 stays open as a statement about LEX's strict all-pairs form,
  which nothing here uses.
- Constant K: at the pin both referees signed (trunk 01d63d7), R46 §1 and §3 state K ≤ (n+2)²(n+1); R46 §1 (the K line and the last sentence of its
  proof, now a different count) and §3 (the K line) were changed AFTER the pin to (n+3)(n+1)² (l-red 938cea5; a process slip,
  recorded); the signed text is the 01d63d7 one, and R47 §5 at da63c40 quotes (n+3)(n+1)². REFEREE signed R46
  §1's (n+2)²(n+1); its own count had an arithmetic slip, corrected 02:47Z (referee 89fee50, R-C1P "Correction note"); the bound
  holds by REFEREE-2's count (n²+n+1)·n ≤ (n+2)²(n+1), which also makes (n+3)(n+1)² valid. This entry states the signed
  K ≤ (n+2)²(n+1); R47 §7 (l-red 28c0a20) uses it.
- Gauntlet: partial step-4 reduction for A_DTL on a subclass. GAP-A (general) stays OPEN; GAPS gets a row for (NEST*-BOUNDED).

### R17 [refereed-only] N5 (switch-best) on one-player games: a λ-phase has at most n − 1 value-changing steps, so N5 makes fewer than (n² − n + 1)(n + m) iterations on one-player games (2026-10-22) — a bound on the candidate N5 itself on a subclass that is polynomial by other means (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C20.md, checker dccf08d + Addenda 128610e, 576bb67, 3001bb1)
- Object: docs/new/N5-phase-bound-box10.md §1-§4 (L-NEW successor 4, Fable 5.1), packet P-N5-1P pinned at trunk 26905f0, with addendum A1
  = the SCOPE line and §6 (VJ00 dependency list) at trunk 0f899f3 (29 inserted lines, 0 deleted; §1-§4 unchanged). N5 as specified in
  docs/new/N5-ssi-global.md (SPEC S1-S5; RESULTS R15). Source: Vöge-Jurdziński, BRICS RS-00-48 (pdf sha256 485a12de…). Setting: H a
  one-player game (one player has out-degree 1 everywhere), injective priorities, VJ00 valuation Ω = (cycle node, P, length) with VJ00's
  order; switch-best: ρ_{k+1} = an optimal strategy of the arena H_k in which every vertex x may use {ρ_k(x)} ∪ I_k(x) (VJ00 improving
  edges, §4.4 eq. (2)); λ-phase = a maximal run of steps in which no vertex changes its cycle node.
- Claims signed (both referees, both labelled "(Fable 5.1)"; first signatures after the D12 Opus period, Lead reading L36):
  (a) (V1)/(V2) (prefix equation and prefix monotonicity of values) and (F1)/(F2) (the optimum of a one-player game dominates every strategy
      of that game pointwise; hence Ω_{k+1} ⪰ Ω_k). (F1) has two independent derivations: REFEREE via the dual of VJ00 Lemma 5.5's proof,
      REFEREE-2 via VJ00 (11) in the dual game plus the "⊵" halves of (4)/(6), which VJ00 asserts and REFEREE-2 derived.
  (b) Lemma P (phase progress): in a λ-phase, after k steps every vertex x satisfies Ω_k(x) ⪰ value(r) for every simple path r of at most k
      edges from x to a cycle node of ρ_0 (all four cases, including the cycle-closing cases B1/B2).
  (c) Theorem PH: in a λ-phase, after n − 1 steps every further in-phase step is value-flat, and there are fewer than m such steps; so a
      phase has fewer than n + m steps.
  (d) Corollary 1: switch-best on one-player games makes fewer than (n² − n + 1)(n + m) steps, O(n²·m), at most n³ − n² + n of them
      value-changing. The arena optimum is not unique; the bound holds for every pointwise-optimal choice (step counts depend on the tie-break).
  (e) Corollary 2: on a game in which one player has out-degree 1 everywhere, N5's step for the other player is switch-best, N5's fallback
      (S4c) fires only in the value-flat situation and then leaves no improving edge; so N5 makes fewer than (n² − n + 1)(n + m) iterations on
      one-player games. This closes K8's constant case (τ constant; Even's steps = switch-best on G_c) for every G_c, cyclic or not.
  (f) Corollary 3 (signed as a reading): VJ00 Prop. 7.4's O(n³) holds for the arena-optimum rule; for arbitrary single switches the statement
      is false (CDAG_n, L-NEW). Not an attribution claim about VJ00's intended rule.
  (g) §6 (A1): the proof uses VJ00 §4.2/§4.5 (the order), §5.1 (6)-(10) (path values), (11) on the dual (F1) and §4.4 eq. (2) (improving
      edges); it does NOT use VJ00 Lemma 5.5, 5.7, 5.8, postulates P1/P2/I1/I2, §5.6. So it does not rest on Lemma 5.8 "2 ⇒ 1" or I1/I2, which
      fail at cycle nodes (RESULTS R15 side finding).
- Honest limits: (i) SUBCLASS that is already polynomial: one-player parity games are solvable in polynomial time by other means; the value
  is a bound on N5 itself. (ii) Two-player N5 is NOT covered: Lemma P's statement is FALSE for N5's Even moves inside a σ̄-segment
  (seg_r16, seg_n24: stalls against τ_k), and the count bound does not transfer (vc_g25, sha1 243f890d…: 26 value-changing Even moves in one segment-phase at
  n = 25, one-player bound 24) (docs/new/N5-phase-bound-box10.md §5, DATA). G-N5-TIME stays OPEN; so do the best-reply-change factor of K9
  (three candidate invariants false, docs/new/N5-brchanges-box11.md) and SB1' (O(n)). (iii) Code link (G-N1 = G-N5T-1 = G-1P-6): N5's code
  experiments/new/n5.py agrees with the referees' definitions on all tested runs (REFEREE-2: 34,601 iterations, 522 fallbacks all value-flat;
  REFEREE: 7,224 runs, every iteration the exhaustive arena optimum or S4c), DATA not proof. (iv) G-N5T-3 (R15) untouched: the output
  correctness at S5 still rests on VJ00 Lemma 5.8 "1 ⇒ 2"; the bounds here do not depend on it.
- Data (DATA, not proof): REFEREE (own probe from VJ00 §4, exhaustive arena optimum, three tie-breaks): F1 462,110 strategy comparisons,
  Lemma P 30,958 checks, Theorem PH/phase count/fallback on 21,224 runs (R-N5-1P §6, all nine rows), "no improving edge ⇒ maximum" exhaustively on 7,945 games n ≤ 6,
  0 violations; Lemma P on n5.py's own ph_n48 sequence (45-step phase) over all simple paths of ≤ 8/11/16 edges, 13,325/18,078/24,987
  checks, and (REFEREE follow-up, referee 708b996a: ≤ 24 edges 33,834 checks; every simple path 43,781 checks; 0 violations). REFEREE-2 (own code from the definitions): 8,500 random one-player games (17,000
  runs, 4 tie-breaks), Lemma P 58,534 checks at every in-phase step, arena optimum verified by brute force over 170,544 arena strategies,
  0 violations. Tightness: in-phase n − 1 value-changing steps attained at n = 12 (rel_g12, sbstep rule; n5.py takes 10 from the same start);
  at n = 16 and n = 48 the longest in-phase counts are 14 and 45 (phase_vc.py counts the closing λ-step as well: N-2).
- Signatures: REFEREE docs/referee/R-N5-1P.md (referee dfa87d0; §C 492ad6d + follow-up 708b996a): SIGNED WITH GAPS G1-G9. REFEREE-2 docs/referee-2/R2-N5-1P.md
  (referee-2 f954070; §7 addendum 857ce07; §C 498b8c9; stamp correction ec8d7a7): (V1)/(V2), Lemma P and Corollary 1 SIGN; (F1)/(F2), Theorem PH, Corollary 2 and §6 SIGN WITH GAPS; Corollary 3 SIGN as a remark. Both §C: identical
  verdicts, no disagreement; joint gap map G1 = G-1P-4, G2 = G-1P-1, G3 = G-1P-3, G4 = G-1P-5, G5 = N-1, G6 = N-3, G-N1 = G-1P-6, G-1P-2
  separate; all closed or DATA except G7-G9 (= N-4..N-6, citation slips in §6: Improve is §4.4 eq. (2) p. 11; the switch-all fixpoint rule
  relies on Lemma 5.8 "1 ⇒ 2"; Prop. 7.4 is on printed p. 27), corrected by L-NEW in the new §7 (l-new a300339, merged trunk ace3841; §1-§4 and §6 unchanged: 0 deleted lines against 0f899f3); G-1P-7 (Lemma P on ph_n48) closed by REFEREE's exhaustive check (referee 708b996a: every simple path, 43,781 checks, 0 violations); L-NEW §7 adds the C1/C2 checks (111 / 166,608, both rules).
- TARGET.md diff: not a claim of TARGET.md section 1 (one-player games; no statement about general parity games). Gauntlet: partial step-4
  lemma for N5 on a subclass. GAPS G-N5-TIME: K8's constant case closed by this entry on landing; G-N5-TIME open.

### R18 [refereed-only] N5 on o-acyclic one-Odd-choice games: fewer than (C_X + d)(B + 1) iterations from any start, conditional on (P) for one-player games; and Proposition X (2026-10-24) — a bound on the candidate N5 itself on a subclass that is polynomial by other means (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C27.md, checker b688c81 + Addenda 0638755, 46605bb, 7a140bc)
- Objects (packet P-N5-1OA, signed object = trunk d78e54f): (A) docs/red/R58-n5-width.md §9, Proposition X and Corollary X1 (L-RED
  successor 13, Opus 5.5; l-red f93e517); (B) docs/new/N5-1Oacyc-box24.md at l-new 8cc6aaf, the self-contained text (file sha1
  d35502679af112e9fa31eb3af99e64fb4afda1ba; L-NEW successor 8, Opus 5.5), with Lemma R and Lemma S of docs/new/N5-time-box21.md
  §2.1-§2.2. Both referees first reviewed the earlier sketch (trunk 07f298d, l-new 9d7890f), then re-checked d78e54f (REFEREE §0,
  REFEREE-2 §7) and signed it in §C2; verdicts are identical at both pins. N5 as specified in docs/new/N5-ssi-global.md (SPEC S1-S5; RESULTS R15).
  Source for (P): Vöge-Jurdziński, BRICS RS-00-48 (pdf sha256 485a12de…), Lemma 5.8 "1 ⇒ 2".
- Setting: 𝒞^1O = games in which exactly one Odd vertex o has out-degree d > 1. X := the vertices with no path to o (so G[X] has no Odd
  choice), Y := V \ X, m_X := the number of edges inside X. o-acyclic := o lies on no cycle of the game graph. A transition of N5 is
  PURE if σ|X and τ are unchanged; a block is a maximal run of pure transitions; G_τ is the one-player game with Odd fixed to τ.
- Claims signed (both referees, both labelled "(Fable 5.1)"; the packet went to the two Fable referees by a Lead routing error against
  L37 (1), which has Fable sessions succeeded on Opus after their box; the signatures stand as two independent signatures on the more
  capable model, labelled as given):
  (a) Proposition X (any start pair, any 𝒞^1O game, o-acyclic or not): the sequence of distinct σ|X along N5 on G is a prefix of N5's
      run on G[X], and the whole run because N5 terminates (R15 (d)); so σ|X changes fewer than C_X := (|X|² − |X| + 1)(|X| + m_X) times.
      The strategy-level identity holds under SPEC's tie-breaks with G[X] keeping X's index order; the COUNT does not depend on
      tie-breaks (each change of σ|X is a pointwise optimum of G[X]'s arena or its terminal flat fallback, so R17 Corollary 1 bounds it).
  (b) Corollary X1 (signed as a reading, superseded by (c)): on o-acyclic 𝒞^1O, θ = Ξ(o) and w = W(o) change fewer than C_X times
      between changes of τ.
  (c) Theorem (conditional on (P) for the one-player game G[X]): on o-acyclic 𝒞^1O, N5 from ANY start pair makes fewer than
      (C_X + d)·(B + 1) iterations, B := (n² − n + 1)(n + m) (R17). Proof: Lemma 1, at a pure transition σ|X has G[X]'s optimal
      valuation (both cases; the flat case is R17's single-switch case analysis at an arbitrary state, proved in place in the d78e54f text; the pointer to R-N5-1P §4 G4 is the referees'); Lemma 2, θ = w
      at a pure transition (o-acyclicity is used here and only here); Lemma 3, Ξ = W at a pure transition, so the gate is G_τ's
      improving set and every block is a prefix of N5's run on the one-player game G_τ, shorter than B (R17 Corollary 2, which both
      referees confirmed holds from any start); non-pure transitions number at most C_X + d − 1.
  (d) Lemma R (box 21 §2.1): the order of the dual game G^d is the exact reverse of G's. Lemma S (box 21 §2.2) (a)-(b): (a) L_σ is the
      pointwise minimum of V_{σ,τ'} over Odd's strategies τ' and U_τ the pointwise maximum of V_{σ',τ} over Even's σ' (VJ00 (11) on G
      and on G^d); (b) L_{σ_k} ⊴ V_{σ_k,τ_k} ⊴ U_{τ_k}, with L non-decreasing and U non-increasing along the run. Lemma S (c)-(d)
      (N5's arena step maximises V_{·,τ_k} over the arena, i.e. is a gated best response; comparison with SSI's step) hold for S4a
      steps only, not at S4c fallbacks (G-1OA-6); the theorem uses (a)-(b) only.
- Honest limits: (i) SUBCLASS that is already polynomial: 𝒞^1O games are solvable in polynomial time by other means; the value is a
  bound on N5 itself. (ii) CONDITIONAL on (P) for one-player games (G-1OA-4, open by design): VJ00 Lemma 5.8 "1 ⇒ 2", used only in
  Lemma 1 on G[X]. A derivation of the one-player form exists (R-N5-1P §3 route (a)), read as sound by REFEREE-2 but not refereed as a
  signature; DATA: 2,283 improvement-free strategies of G[X] all optimal (REFEREE-2). (iii) o-CYCLIC 𝒞^1O is NOT covered: Lemma 1 holds on (REFEREE-2 N-3, accepted by REFEREE; the signed text §6 says instead that Lemma 1 "has no analogue" there)
  all of 𝒞^1O, but Lemma 2 fails when an exit of o routes back through o (fts_best16: Lemma 2 fails at 24 of 28 pure states). fts_best16 is an
  o-cyclic 𝒞^1O game with 27 iterations in one λ-phase (box 21); box 21's longer one-phase runs fts_best39 (78) and fts_g43
  (121) have 4 and 8 Odd choice vertices and lie outside 𝒞^1O. (iv) Code link (G-N1 = G-N5T-1, inherited): n5.py agrees
  with the referees' definitions on all tested runs, DATA not proof. (v) L-NEW's DATA remark "every block ≤ |Y|" is FALSE (L-RED R58 §10:
  block_bk20 n 24, |Y| 21, one block of 27; block_bk32 n 36, |Y| 33, one block of 49); the theorem bounds blocks by B, not |Y|.
- Data (DATA, not proof): REFEREE (own probe, n5.py unmodified): 7,200 random o-acyclic runs, 2,707 pure transitions, Lemmas 1-3 0
  failures, 2,380 blocks all prefixes of n5.py on G_τ (max 7), Prop X 7,168 runs / 4,841 changes of σ|X 0 mismatches, engine Ξ = own Ξ at
  15,985 states. REFEREE-2 (own code): 1,147 random o-acyclic games (canonical and random starts), 20 composed games with long X runs,
  statY_12, i4_hand: Prop X exact in every case (also on 735 𝒞^1O games with X ≠ ∅, o-cyclic or not), 1,531 changes of σ|X all pointwise optima, 83 pure
  transitions 0 violations. Both: block_bk20 / block_bk32 (blocks of 27 and 49), Lemmas 1-3 and the block identity at all 76 pure states,
  0 violations. Lead: statcheck.py fresh seeds 41/42 and bk20/bk32, 0 failures. Negative control fts_best16 fails as expected (all three).
- Signatures: REFEREE docs/referee/R-N5-1OA.md (referee 9060b51; §0 re-pin bb96f45; §C 061052c; §C2 73b46eb): (A) SIGNED WITH GAPS
  A1-A2, Cor. X1 SIGNED as a reading, (B) SIGNED CONDITIONAL ON (P) WITH GAPS B7 (= N-4) and N-5 (B1-B6 closed or confirmed), Lemma R
  SIGNED, Lemma S SIGNED WITH GAPS S1, S2, G-1OA-6 (first half). REFEREE-2 docs/referee-2/R2-N5-1OA.md (referee-2 603cb3a; §7 re-pin
  3188622; logs d5d941a; §C 0ea3441; §C2 77f9cf7): (A) SIGN WITH GAPS (G-1OA-1, -2 closed; N-1), Cor. X1 SIGN, (B) SIGN WITH GAPS
  conditional on (P) for one-player games (N-2, N-4 = B7, N-5; G-1OA-3, -5 closed by the d78e54f text), Lemma R SIGN, Lemma S SIGN WITH
  GAPS (G-1OA-6; S1, S2). Both §C and §C2: identical verdicts at both pins, no disagreement; joint gap map A1 = G-1OA-2 + N-1,
  A2 = G-1OA-1, B2 = G-1OA-3, B3 = N-3, B4 = G-1OA-5, B7 = N-4, S2 = G-1OA-6 (second half), (P) = G-1OA-4; REFEREE accepted two items it
  had missed (G-1OA-6 first half and N-5). Joint open list: G-1OA-4 ((P), conditional by design) and inherited DATA gap G-N1;
  wording items G-1OA-1, G-1OA-2/N-1, G-1OA-6, N-2, N-4, N-5, S1.
- TARGET.md diff: not a claim of TARGET.md section 1 (a subclass with one Odd choice vertex; no statement about general parity games).
  Gauntlet: partial step-4 lemma for N5 on a subclass. GAPS G-N5-TIME: o-acyclic 𝒞^1O closed conditional on (P) on landing; o-cyclic
  𝒞^1O and the general case open.

### R19 [refereed-only] N5 on one-Odd-choice games: gate/selection structure (Lemma G), monotone w (Wo), monotone routes (RM), re-entry (RE) and two-run decomposition between crossings (PIECE) (2026-10-24) — partial step-4 lemmas for N5 on a subclass (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C28.md, checker b53136d + Addenda e5c4694, 8f2ee01)
- Object (packet P-N5-RE, pinned trunk 52c7261, unchanged during review): docs/new/P-N5-RE-box26.md, sha1
  8dba4576950d4888b90d4c0cc86217b9b8fec745 (L-NEW successor 9, Opus 5.5). The repairs both referees require are written in the
  referees' reports and applied by the lane in docs/new/N5-xing-box27.md §9 (not refereed as text; the signed statements are below).
  N5 as in docs/new/N5-ssi-global.md (SPEC S1-S5; RESULTS R15). Setting: 𝒞^1O (exactly one Odd vertex o of out-degree d > 1),
  o-acyclic or not; θ := Ξ(o) (Even's honest value at o, against Odd's best reply), w := W(o) (the value N5's selection trusts at o); R := the vertices whose
  current play reaches o; (h) the packet's regularity hypothesis (P-N5-RE §1), assumed only where a claim says so.
- Claims signed (both referees "(Opus 5.5, D15)", L37):
  (a) Lemma G (a)-(c): off R, Ξ = W (no (h) needed, N-RE-1); under (h), on R, Ξ = π ⊕ θ and W = π ⊕ w with π the route to o, and
      the route order is the same whether o is valued at θ or at w; hence an edge inside R is in Iσ iff it is route-improving iff it is
      W-improving.
  (b) Lemma Wo: under (h) at consecutive states k, k+1 with τ_{k+1} = τ_k, τ(o) ∉ R, w = o ⊕ Ξ(τ(o)), and w_{k+1} ⊵ w_k.
  (c) Lemma RM: in a stretch with τ and θ constant and (h), routes of vertices staying in R never decrease (route order (c, A_π, |π|)
      without the terminal, RM-1).
  (d) Lemma RE, WITHOUT the packet's hypothesis (NC): inside one joint λ-phase, with (h) at L and at E+1 and τ constant on [L, E+1]
      (the packet's hypothesis; not needed: REFEREE §C3, REFEREE-2 §A), if x
      leaves R at L and next re-enters at E, then route_{E+1}(x) ▷ route_L(x) or
      θ_{E+1} ▷ θ_L. Proof as repaired by both referees: key step (SG) — at any N5 transition a switched Even vertex y with λ_L(y) ≠ y
      gains strictly (on all games, not only 𝒞^1O) (Ξ_{L+1}(z) ⊵ Ξ_L(z) ▷ Ξ_L(σ_L y), then one strict (V2)); the packet's step-2 caveat and step-3 sentence are
      false as written (RE-1 = G-RE-1, RE-2 = G-RE-2) and are replaced. Gap G26-1 is CLOSED; the packet's §6 "flat leave" is excluded by the proof;
      nc_fail_n12.pg (REFEREE-2) exhibits the (NC) configuration with a strict gain.
  (e) Corollary RE: with (h) at every leave and re-entry state (REFEREE §4.4), re-entries per joint λ-phase ≤ n·#θ-changes +
      #(route-improving re-entries). REFEREE-2 raised N-RE-3 (τ constant per interval) and withdrew it in R2-N5-RE §A (Lemma RE's
      proof never uses τ constant; 25 re-entries with a τ-change inside the interval, all strict); REFEREE §C3 reads the same.
  (f) Lemma PIECE: in one joint λ-phase, in a stretch with τ, w, R constant, (h), no fallback (θ constant not needed, N-RE-4), N5 runs two independent R17
      arena runs, the route game on R with o's frozen continuation as terminal and the o-free game on F; with the contraction 𝓡* (o a
      self-loop with c's priority; REFEREE) or Lemma P re-run with base case at o (REFEREE-2) each piece has ≤ |R| − 1 resp. |F| − 1
      value-changing transitions (P-1 = G-RE-3). The packet's Consequence (a count over a whole stretch) is a READING, not signed
      (REFEREE §5.4); it needs "inside one joint λ-phase" (P-2).
- Honest limits: (i) SUBCLASS (𝒞^1O) that is polynomial by other means; a bound on N5 itself, not on parity games. (ii) These lemmas
  do NOT bound N5 on o-cyclic 𝒞^1O: the open items are (CYC') θ- and w-changes per joint λ-phase and (NH) non-(h) transitions
  (L-NEW box 27 reduction, READING; its Lemmas C, FBL, FBF, CR, XA are in a second packet, P-N5-XA, under review). (iii) Data caveat:
  the lane's random re-entry samples are vacuous (737 leaves, 0 re-entries; REFEREE); RE's support is the proof plus the referees' own
  checks. (iv) Code link G-N1 (inherited): n5.py agrees with the referees' definitions on all tested runs, DATA.
- Data (DATA, not proof): REFEREE (re_probe.py): 17,473 switches of non-cycle-node vertices, 0 non-strict (494 (NC) cases); 512 leaves
  (RE step 3), 0 violations; PIECE split bounds 480 transitions, 0 violations; negative control (cycle-node switches): 57/446 non-strict.
  REFEREE-2 (own checker from the definitions): 31,827 runs, 60,225 transitions, 0 violations; 1,321 re-entries (the 400 with θ unchanged
  are strict; 921 have a θ-change); (SG) 25,283 switches; all 3,356 non-strict leaves at non-(h) states. L-RED 13: RM/RE attacks on rt48/ph64 climbs, 0
  violations.
- Signatures: REFEREE docs/referee/R-N5-RE.md (referee 4457a9a; §C 87beaa6, a3d1f70): G, Wo, RM SIGNED; RE SIGNED WITH GAPS (closed),
  (NC) not needed; Corollary RE SIGNED WITH GAP N-RE-3 (τ-free reading §C3); PIECE SIGNED WITH GAPS (P-1 closed, P-2 wording). REFEREE-2
  docs/referee-2/R2-N5-RE.md (referee-2 3ee7b73, c66da44; §C dd5aaa2; §A 9d3f1fb): G, Wo, RM SIGN (RM-1 noted); RE SIGN without (NC); Corollary RE
  SIGN WITH GAPS (N-RE-3), revised to SIGN in §A; PIECE SIGN WITH GAPS (P-1 closed, P-2 open as wording). Both §C: no disagreement; gap map RE-1 = G-RE-1,
  RE-2 = G-RE-2, P-1 = G-RE-3, P-2 = N-RE-4 (second half); (SG) = REFEREE §4.2. REFEREE-2's wording notes N-RE-1, -2, -5
  accepted by REFEREE (§C).
- TARGET.md diff: not a claim of TARGET.md section 1. Gauntlet: partial step-4 lemmas for N5 on a subclass. GAPS G-N5-TIME: open.
- POST-LANDING NOTE (2026-10-24 19:10Z by date -u): (f)'s per-part bound holds with θ free only with the R-part counting route (W on R) changes; read with Ξ on R it fails (fbref_n48, 56 → 57). The total stands. Signed clarification: RESULTS R21 (i) (REFEREE R-N5-X X-1 / §C3, REFEREE-2 R2-N5-X Lemma TF / §C.4).

### R20 [refereed-only] N5 on one-Odd-choice games, throttled stretches with a top difference (u* ≠ none): coarse monotonicity (C), fallbacks only evict (FBL), no entry after a fallback (FBF), coarse R17 (CR), strict re-entry (XA), and O(n³) value changes per stretch (2026-10-24) — partial step-4 lemmas for N5 on a subclass (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C29.md, checker 5a39540 + Addendum aa909fd)
- Object (packet P-N5-XA, pinned trunk b70aa59, unchanged during review): docs/new/P-N5-XA-box27.md, sha1
  832d0da2b45bcc0850929b0f614bb1d9b19ed7b3 (L-NEW successor 9, Opus 5.5). The referees' repairs are collected by the lane in
  docs/new/P-N5-XA-fixes-box28.md (sha1 a7022bf5…, L-NEW successor 10; a record of the reports, not itself refereed text).
  Setting as in R19 (𝒞^1O, θ, w, R, (h)); a throttled stretch S: τ, joint λ-phase, θ, w constant, θ ◁ w, (h) at every state of S;
  u* := the most relevant vertex of P(θ) Δ P(w); COARSE(v) := (cycle node, path vertices more relevant than u*).
- Claims signed (both referees "(Opus 5.5, D15)", L37):
  (a) Lemma C: in S, COARSE(Ξ) = COARSE(W) at every vertex, and it is non-decreasing along S, fallbacks included.
  (b) Lemma FBL, FOR u* ≠ none only, in the strong form: at a throttled S4c fallback state there is no F→R and no R→R gate edge, so
      the fallback switches only leaves (R→F edges), apart from flat cycle-node switches. For u* = none FBL is UNPROVED (a switched
      F→R edge whose target's route leaves R in the same fallback is not excluded; no instance known; G-XA-1 (b), found by REFEREE-2,
      accepted by REFEREE).
  (c) Lemma FBF, for every u*: after a throttled fallback at L, for the rest of S no vertex enters R and no vertex in R changes its
      route (base: c ∉ R_t on S, REFEREE-2; inductive step: best-key choice of S4c, REFEREE).
  (d) Lemma CR: R17's Lemma P / Theorem PH transcribed to the coarse order (B1/B2 in full; the omitted case "P(π) = ∅, c′ even,
      shorter" (XA-3) and Odd vertices in Case A (XA-4) added); coarse values change only in the first n − 1 transitions of S. CR does
      not depend on FBL: the fallback case is vacuous (N-XA-1).
  (e) Theorem XA, for u* ≠ none: a re-entry into R after an arena (non-fallback) leave inside S is a strict coarse increase; ≤ n − 1 such re-entries
      per vertex (N-XA-2), ≤ n(n − 1) per stretch.
  (f) Corollary, for u* ≠ none with (h) at every state of S: pieces (PIECE, R19 (f)) pass through value-flat fallbacks (σ_{k+1} is
      another optimum of the arena; REFEREE §C5 = REFEREE-2 §C.5/§C2.2), hence S has O(n³) crossings, non-flat fallbacks and
      value-changing transitions, and O(n⁵) transitions in all (value-preserving = Ξ and W unchanged; such runs ≤ 4n(n−1), R15 (d), N-XA-3).
- Honest limits: (i) SUBCLASS 𝒞^1O, polynomial by other means; a bound on N5 itself. (ii) This bounds ONE throttled stretch with
  u* ≠ none. Open for G-N5-TIME on 𝒞^1O: the number of (θ, w)-stretches per joint λ-phase ((CYC'): θ- and w-changes; climbs reach 43
  θ-changes in one phase at n 32 (sc32, above n); whether growth is linear is OPEN), non-(h) transitions ((NH)), stretches with u* = none, and FBL for u* = none. (iii)
  "Value-changing" in (f): the lane's fixes file §6 defines it as "Ξ or W changes" (a crossing can change Ξ with W flat); that
  definition is the lane's, not checked by a referee; inside a piece the two readings coincide. (iv) No data for (e): 0 re-entries
  inside throttled stretches in every sample (lane, both referees); the claim rests on the proof.
- Data (DATA, not proof): REFEREE xa_probe.py: 25 named instances + 26,483 random runs, 44 throttled stretches (32 with u* ≠ none, 12 with u* = none), 41 throttled fallbacks
  (all u* ≠ none), 151 post-fallback states, 0 failures of C, coarse monotonicity, CR, FBL, FBF; random samples nearly vacuous (~1
  throttled stretch per 1,000 runs). REFEREE-2 xa_check.py (own code): 16,672 runs, 707 throttled stretches (longest 56), 576 fallbacks
  in S, 921 switched edges (all leaves), 0 violations; piece_flatfb.py: 1,052 pieces, 64 with a flat fallback, 0 violations (weak: 10
  value-changing steps in those 64).
- Signatures: REFEREE docs/referee/R-N5-XA.md (referee f39972d; §C 1123baf; §C7 a1de721): C SIGNED; FBL SIGNED for u* ≠ none, unproved for
  u* = none; FBF SIGNED WITH GAPS (closed); CR SIGNED; XA SIGNED; Corollary SIGNED in §C7 (the form of R2 §C2.3 / fixes §5-§6; value-preserving = Ξ and W unchanged). REFEREE-2
  docs/referee-2/R2-N5-XA.md (referee-2 9d3f1fb; §C 4df15e6, stamp fix a8c7351; §C2 38af0df): §1, C, FBF, CR, XA SIGN; FBL SIGN WITH GAPS (u* = none
  unproved); Corollary SIGNED in §C2 for u* ≠ none via §C5. Joint gap map: XA-1 = G-XA-1 (a), (b) REFEREE-2 only (accepted); XA-2 =
  G-XA-2 (closed); XA-3, XA-4 wording (accepted by REFEREE-2); XA-5 CLOSED (REFEREE §C5 + §C7, REFEREE-2 §C2.3: two signatures on the same form); N-XA-1..3 accepted.
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.

### R21 [refereed-only] N5 on one-Odd-choice games: inside one joint λ-phase, transitions are bounded by crossings and OTHER states (Theorem X), with Lemmas XW, EQ, FBL-N, NF, F1, F2, FB-W, and a clarification of R19 (f) (2026-10-24) — partial step-4 lemmas for N5 on a subclass (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C30.md, checker 7bf1999 + Addendum 679ea11)
- Object (packet P-N5-X, pinned trunk afc88b0, unchanged during review): docs/new/P-N5-X-box28.md, sha1
  b21d2d0638d08d750f26ae4dda2faaca7891fa23 (L-NEW successor 10, Opus 5.5). The referees' repairs are collected by the lane in
  docs/new/P-N5-X-fixes-box29.md (l-new 331ad0c, on trunk; sha1 dd467be05462b17ef5744d4e1019afeada95588c, L-NEW successor 10; a record of
  the reports, not itself refereed text).
  Setting as in R19 (𝒞^1O, θ, w, R, (h)). A PHASE is a joint λ-phase with τ constant. F := V \ R. A CROSSING transition changes R.
  State types: EQ (Ξ = W pointwise), THR ((h) and Ξ ≠ W), OTHER ((h) fails and Ξ ≠ W); an OTHER-touching transition has an OTHER
  endpoint. VALUE-CHANGING: Ξ or W changes at some vertex.
- Claims signed (both referees "(Opus 5.5, D15)", L37):
  (a) Lemma XW: Ξ_k ⊴ W_k pointwise at every state (Odd's best reply σ̄_k is pointwise optimal in G_{σ_k}).
  (b) Lemma EQ: a run of consecutive EQ states inside one phase has ≤ n − 1 value-changing transitions; (h) not assumed.
  (c) Lemma FBL-N: at an S4c fallback with τ unchanged, (i) it is Even's and σ_k is a pointwise arena optimum in G_τ; (ii) every gate
      edge from F is flat for W; (iii) if H2 fails, no gate edge goes from F to R.
  (d) Lemma NF: a value-changing S4c fallback inside a phase with neither endpoint OTHER is a crossing.
  (e) Lemma F1: on an F-interval (a maximal run of a phase with no crossing and no OTHER-touching transition; F constant), Ξ changes
      on F at ≤ max(0, |F| − 1) transitions (X-2); w, θ and (h) at EQ states never enter (step 2 needs only Lemma G (a), N-X-1).
  (f) Lemma F2: inside an F-interval, an EQ → THR transition changes Ξ(τ(o)), and at a THR → THR transition a w-change is a change of
      Ξ(τ(o)).
  (g) Theorem X: inside one phase, with X := #crossing transitions and O := #OTHER-touching transitions, the phase has at most
      (3n²(1 + X + O) + X + O + 1)(4n(n − 1) + 1) = O(n⁴(1 + X + O)) transitions. Step 4 uses PIECE (R19 (f)) with θ free in the form
      of item (i) below (X-1 = G-X-1), and re-derives "flat fallbacks pass PIECE" from NF outside u* ≠ none stretches instead of citing
      R20 (f) (X-4 = N-X-3). (FBRE-F) is not used.
  (h) Lemma FB-W, given the CR row of the (w, u*)-run table: in a (w, u*)-run, a vertex evicted by a fallback at L ≥ k_0 + n − 1 to a
      target with w's status at u* never re-enters R in that run. (DATA vacuous: 0 qualifying evictions in REFEREE-2's sample.)
  (i) Clarification of R19 (f) (landed text frozen; docs/agents/R19-note-X1.md): R19 (f) holds with θ free in this form: the R-part
      bound counts route (𝓡*, i.e. W on R) changes; a θ-change at a transition with H1 at its start and R constant changes W on F
      (REFEREE X-1, via Lemma S (a) and R15 (a); REFEREE-2 Lemma TF as a second proof) and is charged to the F-part; the total
      (|R| − 1) + (|F| − 1) counts transitions at which Ξ or W changes. Read with Ξ on R counted in the R-part, the per-part bound fails
      with θ varying (fbref_n48, transition 56 → 57, R = {o}). (Wording: REFEREE-2 §C.4; REFEREE §C3 confirms its content.) A
      POST-LANDING NOTE under R19 points here.
- Also checked, not a claim: the (w, u*)-run table (which R20 lemmas survive θ-changes: all except FBF), checked by both as a READING.
- Consequence (READING, not signed): with Lemma Φ (≤ 2n(n − 1) + 1 joint λ-phases; box 21, PROVED by the lane, UNREFEREED) and
  τ-changes ≤ d − 1 (R15 (c) on G^d, checked by REFEREE), N5 on o-cyclic 𝒞^1O is polynomial if (X) and (NH') hold: X and O are poly(n)
  per phase.
- Honest limits: (i) SUBCLASS 𝒞^1O, polynomial by other means; a bound on N5 itself. (ii) Theorem X moves the open part of G-N5-TIME on
  𝒞^1O to two counts, and both exceed n in data: X = 54 at n 32 and 70 at n 48 (L-NEW climbs, Lead re-run); O = 11 at n 10 (L-COMP
  experiments/n5-exhaustive/instances/b5_o11.pg, l-comp 67471f7b, on trunk; sha1 db4fe55a…; Lead re-run) and 19 at n 24 (L-NEW). (X) and (NH') are OPEN; no growth law beyond linear is established either way.
  (iii) The phase count (Lemma Φ) is unrefereed. (iv) (FBRE-F) is FALSE (L-RED fbref_cex_n32; L-NEW fbref_n48); not used here.
- Data (DATA, not proof): REFEREE x_probe.py: 42 named instances + 8,731 random runs, 1,947 phases (max length 110, X up to 70, O up to
  19), 0 failures of XW, NF (121), F1 (1,592 intervals), F2 (33), EQ (1,464 blocks), sub-block ≤ n − 2 (136), θ-change ⇒ F-change (176),
  or the Theorem X bound. REFEREE-2 x_check.py (own code): 15,378 runs, 37,235 phases, 3,558 F-intervals, 753 sub-blocks (211 with θ
  varying), 1,735 (w, u*)-runs, 0 violations of any packet statement; the per-part R19 (f) reading with Ξ on R fails in 111 sub-blocks
  (item (i)). Lane eqcheck.py: 0 failures (Lead re-run, seed 2832, 1,296 runs).
- Signatures: REFEREE docs/referee/R-N5-X.md (referee 53c0c68; §C 865eadd): F1 SIGNED WITH GAPS (X-2); NF SIGNED WITH GAPS (X-3);
  Theorem X SIGNED WITH GAPS, all closed (X-1 closed in §3.2, X-4 valid as re-derivation); XW, EQ, FBL-N, F2, FB-W SIGNED; table
  checked as a READING; §C: no disagreement of substance, N-X-2 accepted, X-1 and TF equivalent, its "R19 (f) as landed TRUE" withdrawn for the wording, item (i) wording confirmed (precision: R_{k+1} = R_k, (h) at k suffices). REFEREE-2 docs/referee-2/R2-N5-X.md (referee-2 059f492; §C 3a581a5): F1, NF SIGN; Theorem X SIGN WITH GAPS
  (G-X-1 closed by Lemma TF); XW, EQ, FBL-N, F2, FB-W SIGN; table agreed; §C: no disagreement, X-2 and X-3 accepted, X-1 accepted as a
  substitute for TF, item (i) wording proposed. Joint gap map: X-1 = G-X-1 (closed); X-2, X-3 wording; X-4 = N-X-3 (re-derivation);
  N-X-1 = REFEREE §1 remark; N-X-2 = REFEREE §3.3 R19 (b) row. Nothing open in the packet.
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.

### R22 [refereed-only] N5 on one-Odd-choice games: crossing-free intervals with OTHER states (F1°), the clauses of (h) on them (TC), and route frames with the honest cycle node higher (P3′) (2026-10-24) — partial step-4 lemmas for N5 on a subclass (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C31.md, checker c500832 + Addendum 4db6e4c)
- Object (packet P-N5-NH, pinned trunk c7981ee, unchanged during review): docs/new/P-N5-NH-box30.md, sha1
  382c514300fe056d5d95b836f359b78b1374eabe (L-NEW successor 10, Opus 5.5). The referees' repairs are collected by the lane in
  docs/new/P-N5-NH-fixes-box30.md (l-new b4fc3a4, on trunk; sha1 2d7e366a2e9782d98ff1598c6eb460af8f46ac57, L-NEW successor 11; a record
  of the reports, not itself refereed text).
  Setting as in R21 (𝒞^1O; a PHASE is a joint λ-phase with τ constant; R, F := V \ R; (h) = H1 ∧ H2 ∧ H3; EQ / THR / OTHER). A
  CROSSING-FREE INTERVAL I is a maximal run of states of a phase with R constant.
- Claims signed (both referees "(Opus 5.5, D15)", L37):
  (a) Lemma F1°: on a crossing-free interval I, OTHER states included, Ξ changes at some vertex of F at ≤ max(0, |F| − 1) transitions
      (R21 (e) extended; FBL-N (ii) and Lemma G (a) need no (h)).
  (b) Lemma TC: on a crossing-free interval I, (i) H1 ⟺ λ_Ξ(o) ∈ F and H2 ⟺ τ(o) ∈ F, both constant on I; (ii) under H2, λ_W(o) =
      λ_Ξ(τ(o)) is fixed in the phase, so H3 and (h) are constant on I, and I is all OTHER or has no OTHER state; (iii) under H1 ∧ ¬H2,
      every state of I is OTHER; (iv) under ¬H1 ∧ ¬H2, a state of I is EQ iff θ = w, and every EQ → OTHER transition inside I changes w.
  (c) Lemma P3′: let J ⊆ I be a (θ, w)-piece (both frames in route form: honest by H1 or λ_Ξ(o) = o, W by H2 or λ_W(o) = o; θ, w
      constant) with c_θ = λ_Ξ(o) strictly more relevant than c_w = λ_W(o). Then the transitions of J with a Ξ-change at some vertex of
      R number at most (n + 1)|R| (both referees: also ≤ |R| + (|R| − 2)(|R| − 1)). Step 1 (coarse freeze, R20 (d) CR run on the route game
      𝓡*_w) uses only the single-switch (F1) inequality at κ-strict B-cases, proved directly by both referees; the packet's sentence "S4a's
      optimum restricted to R is an optimum of 𝓡*_w's arena" is UNPROVED under ¬H2 with λ_W(o) = o, not refuted, and not needed
      (P3-1 = G-NH-1; for x on o's W-cycle a κ-strict edge would move x's W cycle node off o inside J, so that case is vacuous).
  (d) Corollary: under H2 on I, I has ≤ max(1, |F|) pieces (θ via R21 (i) / X-1, w via R19 (b) under H2, F1°).
- Reduction (READING, checked by both referees, not signed): inside one phase, the transitions number at most
  poly(n) · (1 + X + Σ_I (ROI(I) + WC(I))), with X = crossings, ROI(I) = R-only value-changing transitions in OTHER blocks of I, WC(I) =
  w-changes in I under ¬H1 ∧ ¬H2 (the ≤ 2(1 + WC(I)) OTHER-block boundary transitions are counted, NH-1 = N-NH-3; an R-only W-change
  raises Ξ on R by (SG), NH-2). With R21, N5 on o-cyclic 𝒞^1O is polynomial if X, ROI and WC are poly(n) per phase. P3′ bounds ROI on
  its pieces.
- Honest limits: (i) SUBCLASS 𝒞^1O; a bound on N5 itself. (ii) Open: (X); ROI outside P3′'s case, i.e. U1 (route form, c_w higher), U2
  (honest frame not in route form), U3 (W frame not in route form); W-CYC. CONJECTURES (OB), (OB_R) (counted in transitions), (NFB-O) (L-NEW, data only);
  WF0 FALSE (wf0_cex_n16); (U1-T) FALSE as stated (L-RED u1t_cex_n32, l-red 959184d9, sha1 63dfd785; one piece of 7 transitions,
  |R| = 28, a vertex with 7 Ξ-changes at one W-length by propagation along its fixed σ-path; Lead re-run n5 12/1, Oink OK verified,
  u1vertex max 7 per vertex, total 88; (OB_R) counted per vertex fails there (88 > 28), counted in transitions it holds (7 ≤ 28)). (iii) P3′'s data is thin: REFEREE 901 qualifying pieces, longest 6 transitions; REFEREE-2 1,017 nontrivial
  pieces from climbs, 1,871 S4a steps under ¬H2 with 0 mismatches. P3′ rests on the proof. (iv) DATA on O (not signed): L-COMP's chain
  of whole-OTHER phases reaches O = 77 at n 40 (≈ 2n; pattern 23, crossings + F-changes + R-only ≤ |R|; Lead re-run).
- Data (DATA, not proof): REFEREE nh_probe.py: 78 named instances (by REFEREE's §5 globs) + 8,784 random runs, 20,840 crossing-free intervals, 0 failures of
  F1°, TC, the Corollary (11,213 intervals) or (SG) (6,942). REFEREE-2 nh_check.py (own code): 12,064 runs, 34,842 crossing-free
  intervals (184 with OTHER states), 39,250 TC state checks, 151,926 (R1) checks, 0 violations.
- Signatures: REFEREE docs/referee/R-N5-NH.md (referee 78d61b1; §C 68e314c): P3′ step 1 SIGNED WITH GAP P3-1 (closed by vacuity), step 2
  and count SIGNED, Corollary SIGNED, TC SIGNED, F1° SIGNED, reduction checked (NH-1, NH-2); §C: no verdict differs, P3-1 = G-NH-1 (same
  argument, each a substitute), N-NH-2 accepted, R2's §1.3 W ⇔ Ξ remark should cite (SG). REFEREE-2 docs/referee-2/R2-N5-NH.md
  (referee-2 48da84a; §C 8621a84, stamp fix e7578fe): P3′ step 1 SIGN WITH GAPS (G-NH-1, closed by a direct single-switch proof), steps 2-3 SIGN, Corollary
  SIGN, TC SIGN, F1° SIGN, reduction correct as a READING (N-NH-1..3); §C: no verdict differs, sharper count accepted, NH-2 accepted and its own §1.3
  "W-change ⇔ Ξ-change on R" converse withdrawn (W ⇒ Ξ fails at a single vertex; the transition-level claim holds by (SG)), P3-1's
  closure and its single-switch proof are the same proof. Joint gap map: P3-1 = G-NH-1 (CLOSED); NH-1 = N-NH-3 (wording);
  NH-2 ((SG) step); N-NH-1 (cite X-1 / R21 (i)); N-NH-2 (THR remark needs (h)).
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.
- POST-LANDING NOTE (2026-10-24 21:38Z by date -u): limit (ii)'s description of u1t_cex_n32 needs two corrections (REFEREE R-N5-U1 D-1, D-2, referee 257fa4c). (1) |R| = 28 there is |R \ {o}|; with this entry's convention o ∈ R, |R| = 29 (and "(OB_R) … 88 > 28 … 7 ≤ 28" reads with |R \ {o}|). (2) σ(10) switches once (12 → 29 at transition 0), so its σ-path is fixed only from transition 1; L-RED R63 §1b also shows own-successor switches at one W-length on the same instance. (U1-T) FALSE as stated is unaffected.

### R23 [refereed-only] N5 on one-Odd-choice games: crossings have active crossers (ACT, LOOP), what fallbacks can switch (NOFE, NOFL-E, GAP), W never drops at arena steps (WM), and crossings are bounded by reversals of R (LV′, Corollary Z) (2026-10-24) — partial step-4 lemmas for N5 on a subclass (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C32.md, checker 2cd52a6 + Addendum 0077eed)
- Object (packet P-N5-Z, pinned trunk fba7177, unchanged during review; a post-pin edit on the lane branch was reverted to the pinned
  bytes before merge): docs/si/P-N5-Z-box5.md, sha1 a027638f06d18143ed0779290b24f8e5decb8249 (L-SI successor 2, Opus 5.5). The lane's
  data corrections and the referees' repairs are in docs/si/P-N5-Z-fixes-box5.md (l-si c3c62ef, on trunk; sha1
  c6d9c13f6b06c0df3b6ca1b9ada04e0c716112ee; a record, not itself refereed text).
  Setting as in R21 (𝒞^1O; a PHASE is a joint λ-phase with τ constant). Convention of this packet: R excludes o and R̄ := R ∪ {o};
  F := V \ R̄, and the crossing transitions (R changes) are the same as in R19-R22.
- Claims signed (both referees "(Opus 5.5, D15)", L37):
  (a) Step (K): at an S4c fallback inside a phase, no arena edge (y, z) raises W at y (from R21 (c) FBL-N (i)).
  (b) Lemma ACT: at a transition with τ unchanged, (i) if R̄ gains a vertex, some switched Even s ∈ F_k with σ_{k+1}(s) ∈ R̄_k enters;
      (ii) if R̄ loses a vertex, some switched s ∈ R_k with σ_{k+1}(s) ∈ F_k leaves, or a new cycle avoiding o lies inside R_k and
      contains a switched vertex.
  (c) Lemma LOOP and Corollary: inside a phase with H1 at k, ACT (ii)'s cycle alternative does not occur, so every leave has an active
      leaver. (H1 is needed: REFEREE's probe saw the cycle alternative 88 times, all without H1.)
  (d) Lemma NOFE, strong form: at an S4c fallback inside a phase, every switched edge y → z with y ∈ F_k and z ∈ R̄_k has y on o's
      W-play at k. (Also a one-line corollary of R21 (c) FBL-N (ii): y is a W-cycle node on o's W-play; Z-2.)
  (e) Lemma NOFL-E and Corollary: at a fallback inside a phase from a state with Ξ = W and H2, no switched edge goes R → F; with H1 ∧ H2 such a
      fallback has no leave.
  (f) Lemma GAP: at a fallback inside a phase with (h) at k, every switched edge y → z with y ∈ R_k, z ∈ F_k satisfies
      Ξ_k(σ_k y) ◁ Ξ_k(z) ⊴ W_k(σ_k y) (the evicted target lies in the trust gap).
  (g) Lemma WM and Corollary: inside a phase, W_{k+1} ⊵ W_k pointwise at every transition that is not an S4c fallback; so every
      W-decrease is at a fallback.
  (h) Lemma LV′: sign each crossing '+' (R̄ grows), '−' (R̄ shrinks) or '±'; with Z := #'±' + #(sign changes between consecutive pure
      signs), X ≤ (n − 1)(Z + 1) + Z and Z ≤ X. "Runs" of equal pure signs are runs adjacent among crossing transitions, so a '±'
      breaks a run (Z-1 = N-Z-1; read "ignoring ±", the monotonicity step fails).
  (i) Corollary Z: inside one phase, #transitions ≤ (3n²(1 + X + O) + X + O + 1)(4n(n − 1) + 1) with X ≤ (n − 1)(Z + 1) + Z, so
      O(n⁵(1 + Z + O)) (from R21 (g) within its signed hypotheses, and LV′).
- Honest limits: (i) SUBCLASS 𝒞^1O; a bound on N5 itself. (ii) LV′ moves (X) to (Z) up to a factor n; Z is OPEN. The lane locates its
  hard part in carries (C), i.e. '+−' reversals at evicting fallbacks (fixes file: a drain counts once); OPEN, CONJECTURE (CL) only.
  (iii) The phase count (Lemma Φ) is unrefereed, so a running-time bound is still a READING. (iv) DATA on Z: lane climbs Z 11 / 18 /
  22 at n 24 / 32 / 48 (zcl_fb2_n32: 13 carries in one phase); L-RED box 32: X ≈ 0.86n from random seeds, X 65 at n 32 from wave
  seeds; L-COMP b6_xw_n32: X 67 at n 32 (Lead re-runs). (v) Refuted lane forms (packet §10): NOFE's first form (nofe_cyc_n8),
  (U*-DROP), (W-LAY). s_rt32_final (si/orlens) is NOT in 𝒞^1O (two Odd choice vertices); it is excluded from all counts.
- Data (DATA, not proof; out-of-class files excluded): REFEREE z_probe.py (appendix 555cbeb): ACT (i) 1,126 / (ii) 855, NOFE 17, GAP
  511, WM 3,957, LV′ 595 phases (max X 78, max Z 22), 0 failures. REFEREE-2 z_check.py (own code): 13,756 runs, 38,186 transitions,
  35,072 phases, 0 violations (ACT 9,174 / 7,951, LOOP 2,689, GAP 1,950 edges, WM 15,717; 963 of 1,153 fallbacks lower W, no
  non-fallback does; 21 F→R̄ fallback edges, all tails W-cycle nodes on o's W-play).
- Signatures: REFEREE docs/referee/R-N5-Z.md (referee c818ef2; data appendix 555cbeb; §C dcee223): LV′ SIGNED WITH GAP Z-1 (wording);
  Corollary Z SIGNED; NOFE SIGNED (Z-2 remark, Z-3 wording); Step (K), ACT, LOOP, NOFL-E, GAP, WM SIGNED; §C: no disagreement.
  REFEREE-2 docs/referee-2/R2-N5-Z.md (referee-2 1a5854b; §C fde0448): every statement SIGN (N-Z-1 wording, N-Z-2 data); §C: no
  disagreement, Z-2 and Z-3 accepted. Joint gap map: Z-1 = N-Z-1 (CLOSED); N-Z-2 = appendix 555cbeb (data); Z-2 (remark); Z-3 (wording).
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.

### R24 [refereed-only] N5 on one-Odd-choice games: S4a keeps every fully optimal edge (R), its tie-break is a monotone potential (TB), W-flat runs are short (CASC), U1 pieces have polynomially many R-changing transitions given their fallbacks (Theorem U1), and w-changes under ¬H2 (WC) (2026-10-24) — partial step-4 lemmas for N5 on a subclass (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C33.md, checker 0102170 + Addendum 59a9799)
- Object (packet P-N5-U1, pinned trunk eee0d8a, unchanged during review): docs/new/P-N5-U1-box31.md, sha1
  eb90788d2949050f316ed983fa56c34d7a1dd9c7 (L-NEW successor 11, Opus 5.5). The referees' repairs are collected by the lane in
  docs/new/P-N5-U1-fixes-box31.md (l-new 61a36b9, on trunk; sha1 88675ab782df24a63426756674579e7336c1508c; a record, not itself
  refereed text).
  Setting as in R22 (𝒞^1O; a PHASE is a joint λ-phase with τ constant; R ∋ o, F := V \ R; crossing-free interval; route form; U1 = both
  frames in route form with c_w strictly more relevant than c_θ; a PIECE J is a maximal run with both frames in route form and θ, w
  constant). Level ℓ(v) := |π_v|.
- Claims signed (both referees "(Opus 5.5, D15)", L37):
  (a) Lemma R: in N5's S1 restriction step, every FULLY optimal successor of x (equal in cycle node, path set and length) survives, so
      the length step chooses among exactly the fully optimal edges (FIX 4 order). The packet's wording "optimal in the cycle-node and
      path-set components" is FALSE at x = u (R-1 = G-R-2; REFEREE's 3-vertex instance; 4,074 / 8,464 such deleted edges, all with
      u = x); the step-1 invariant holds for processed u ≠ x (G-R-1). VJ00 (BRICS RS-00-48) §6 Prop. 6.1 gives only existence of one
      surviving path; Lemma R is the packet's own strengthening (R-2).
  (b) Lemma TB: at an S4a transition without fallback, if an Even v switches with W'(v) = W_k(v) and is not its own cycle node c, then
      (TB-odd) c odd ⇒ σ_{k+1}(v) < σ_k(v) as indices; (TB-even) c even and W' = W_k on v's σ_k-play from v to (before) c ⇒ the
      root-first index key pk(v) strictly decreases lexicographically. Tie-breaks equal SPEC S1 (iv) / FIX 4 exactly (TB-1 = G-TB-1:
      the sandwich case where the optimal play passes x, closed by an (F1)-only case proof; TB-2 wording).
  (c) Lemma CASC: in a W-flat run (consecutive non-fallback transitions of a piece with W unchanged on R), an R-vertex of level ℓ
      switches only at run steps ≤ ℓ − 2; so no R-vertex switches at a run step ≥ |R| − 2. Step 1 uses only TB's choice rule (C-1,
      wording after §C; C-2, C-3 wording).
  (d) Theorem U1: a U1 piece with f fallback transitions has at most |R| + f + K + (K + f + 1)(|R| − 2) transitions that change Ξ, W
      or σ on R, with K ≤ (f + 1)(|R| − 1)(|R| − 2) counting non-fallback transitions (N-U1-1); O((f + 1)|R|³), and ≤ |R|³ for f = 0.
      Includes the κ_w-freeze, with R22 (c)'s P3-1 repair transferred.
  (e) Lemma WC: on a crossing-free interval with ¬H2, the w-changing transitions number WC(I) ≤ (f_I + 1)(|R|² − 1) + f_I, with f_I
      the fallback transitions of I. Sharpened in both §C (N-U1-3): at an EQ state Ξ = W, so an Even fallback switches improving
      edges of G_τ and W does not decrease (R15 (a) / VJ00 Lemma 5.7 in G_τ); hence only fallbacks at OTHER states count in f_I.
- Reduction (READING, checked by both referees, not signed): with RESULTS R22's reduction (itself a READING), (NH') reduces to (X),
  NFB-O (fallbacks at OTHER states) and the U2/U3 re-routings. Unsigned inputs named by REFEREE: the P-N5-NH §4 assembly and its fixes
  §4 one-liner (checked true by TC (iv)).
- Honest limits: (i) SUBCLASS 𝒞^1O; a bound on N5 itself. (ii) U1 is bounded GIVEN f; fallbacks at OTHER states (NFB-O) are open (0
  seen), as are the U2/U3 re-routings and (X). (iii) DATA is thin: K = 0 everywhere, no U1 piece with a fallback was found, and CASC
  climbs never came within 2 steps of the bound. (iv) (U1-T) is FALSE as stated, per vertex (L-RED u1t_cex_n32 sha1 63dfd785; L-NEW
  u1t_cex2_n32 6162a26f; own-switch version L-RED u1t_own6_n32 f6368500, 6 own switches at one W-length in a 6-transition piece);
  Theorem U1 counts transitions per piece. (v) |R| convention: lane scripts printed |R \ {o}|; with R ∋ o the three cex instances have
  |R| = 29 / 29 / 25 (D-1 = N-U1-5); every checked bound grows with |R|, so the lane's checks were stricter.
- Data (DATA, not proof): REFEREE: 3 pinned instances re-run; 78 named 𝒞^1O instances (92 U1 pieces, longest 12); 5,500 random runs
  (U1 pieces single-state, vacuous); 23,000 random arenas (TB-odd 113, TB-even 535); 381,241 choice-rule checks; 3 CASC climbs (7,599
  candidates, best margin −2); 322 EQ-state fallbacks, W non-decreasing; 0 failures. REFEREE-2 (own code): 11,910 runs + 20,000 arenas
  + 13 climbs (70,400 runs), 0 violations; 426,737 key-min checks against SPEC, 0 mismatches.
- Signatures: REFEREE docs/referee/R-N5-U1.md (referee 257fa4c; §C 4de5c2e, stamp fix 5054e81): Theorem U1 SIGNED; CASC SIGNED (C-1
  downgraded to wording in §C); TB SIGNED WITH GAPS (TB-1, TB-2, closed); Lemma R SIGNED WITH GAPS (R-1, R-2, G-R-1, closed by
  restating); WC SIGNED, sharpened (N-U1-3, proved in §C.3); §6 READING correct. REFEREE-2 docs/referee-2/R2-N5-U1.md (referee-2
  28ddf6f; §C 3d68a03, stamp fix cab4e7d): U1 SIGN; CASC SIGN WITH GAPS (C-1 accepted as a citation gap, closed; C-2, C-3 wording); TB SIGN WITH GAPS
  (G-TB-1, closed); R SIGN WITH GAPS (G-R-1, G-R-2, closed); WC SIGN, N-U1-3 closure proved in §C.4; §6 READING correct. Joint gap
  map: TB-1 = G-TB-1; R-1 = G-R-2; R-2 (VJ00 existence only); G-R-1, C-1..C-3, TB-2 wording; N-U1-1 (K counts non-fallback
  transitions); N-U1-3 closed by both; D-1 = N-U1-5, D-2 = N-U1-4 (data notes).
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.

### R25 [refereed-only] N5 inside a phase: coarse super-solutions (claim (T), COARSE-SI, TAME), the max gate level never rises at tame transitions (MONO, NOINF), fallbacks are bounded by non-tame transitions (Theorem FB), and on one-Odd-choice games every non-tame transition is an exit jump at o (J1, OFF, CAP) (2026-10-24) — partial step-4 lemmas for N5 (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C34.md, checker 298e4b6 + Addenda 4278b5a, e9f7b67)
- Object (packet P-N5-FB, pinned trunk 348393b, unchanged during review): docs/si/P-N5-FB-box7.md, sha1
  9ece9994a1251f904935048a605495cd325946e7 (L-SI successor 3, Opus 5.5). The referees' repairs are collected by the lane in
  docs/si/P-N5-FB-fixes-box7.md (part 1, REFEREE's items; l-si 1c8bb9c, on trunk; sha1 8548c3fc56eebc56e82d099d7c378bd481d79a5d)
  and docs/si/P-N5-FB-fixes2-box7.md (part 2, REFEREE-2's items and a concordance of both reports; l-si 8d0b180, on trunk; sha1
  4d5b3716731285eb629e8d92fca5b01b756a6d1f), both L-SI successor 3; records, not themselves refereed text; the lane's third,
  minimality-free CAP proof (part 1) is unrefereed.
  Setting: N5 (SPEC docs/new/N5-ssi-global.md) on any game unless marked 𝒞^1O; a PHASE is a joint λ-phase with τ constant, and "a
  transition of the phase" has both ends in the phase (FB-2); lev(a, b) := the level at which two valuations first differ; COARSE_L
  keeps a valuation's cycle node and its path-set part above level L; M_k := the max gate-edge level at k; a transition is TAME if
  COARSE_{M_k}(Ξ) is unchanged across it (TAME's hypothesis), NON-TAME otherwise; J := #non-tame transitions of the phase.
- Claims signed (both referees "(Opus 5.5, D15)", L37):
  (a) Claim (T) and COARSE-SI (a): if every switched edge has gate level ≤ L and the switched graph closes no new bad cycle ((NC)),
      COARSE_L(Ξ) is unchanged; converse: if (NC) fails, COARSE_L changes at the top of a bad cycle. Uses VJ00 (BRICS RS-00-48) σ̄ p.
      14, Prog p. 15 (V-1 = N-FB-1), Lemma 5.2 p. 15, (11) p. 16; applying Lemma 5.2 to SPEC's σ̄ uses Ξ_k = Θ_{H_k} (ENG-1, the
      inherited R15 code link; re-checked at 26,724 states).
  (b) COARSE-SI (b), Lemma TAME: with λ unchanged and every Odd switch of σ̄ at level ≤ M_k, COARSE_{M_k}(Ξ) is unchanged.
  (c) Lemma MONO: at a tame transition M_{k+1} ≤ M_k. Lemma NOINF: inside a phase every switch keeps its cycle node, so every switched
      edge has finite gate level (at an S4c fallback every gate edge does, by S4c's best target: FB-1).
  (d) Theorem FB: a phase has at most n_E(2n − 1)(J + 1) + J S4c fallback transitions (both ends in the phase; a phase-exit fallback
      adds at most 1, FB-2). Step (2)'s "M < ∞" uses S4c's best target to carry NOINF to all gate edges of y (FB-1 = G-FB-1); step (2)
      takes FBL-N (i) directly from S4c + FIX 3, so it holds on every game (G-FB-2). Corollary: W-lowering transitions are bounded the same way on
      every game, WM being transferred to every game by (F1) in G_τ (G-FB-3); on 𝒞^1O so are the carries (C) ('+−' reversals of R at
      fallbacks).
  (e) On 𝒞^1O: J1 (a non-tame transition switches σ̄(o) at a level above M_k), OFF (a vertex leaving R̄ keeps its COARSE_{M_k} value),
      and CAP (every exit within level M_k of σ̄_k(o) is captured into R̄_{k+1}). CAP's "σ̄ minimises Ξ over succ(o)" holds for VJ00's
      σ̄ but not for SPEC's FIX-2 DFS choice at a cycle node (925 / 1,228 observed cases); two valid closures (CAP-1 = G-FB-4):
      CAP uses only COARSE_M with M ≥ −1 and SPEC's DFS σ̄(o) is a COARSE_{−1}-minimiser (REFEREE-2; Prog clause 3, VJ00 (3), (10));
      or by cases, λ(o) ≠ o giving a full minimiser and λ(o) = o needing no minimality (REFEREE).
  (f) On 𝒞^1O: Lemma A, proved part: at tame carries, the carry level L ≤ M_k.
- Refuted: (JUMP-EQ) (an INR jump above the last carry level lands at θ = w) is FALSE, confirmed by both referees with their own code:
  x31_rx32 (experiments/red/xing/instances, sha1 4fe9ec0e), transition 53 → 54, θ_54 ≠ w_54 with (h) at 54.
- Honest limits: (i) Theorem FB, its W-lowering Corollary, (T), COARSE-SI, TAME, MONO and NOINF hold on every game; the (C) bound, J1, OFF, CAP
  and A are on 𝒞^1O. (ii) Theorem FB moves the
  fallback count, and with R23 the carries (C) and Z, to J; (J-poly), a polynomial bound on J per phase, is OPEN. DATA on J: J ≤ 3 on the
  53 named instances; L-RED climbs reach J = 7 at n 32 and n 48 (j7_n32 sha1 78ec52e8, j7_n48 c593e43c; Lead re-run with L-SI's
  tame.py); L-SI climbs report 12 at n 32 and 17 at n 48 (lane data). (iii) L = M_k at carries is DATA (201 / 201), not proved.
  (iv) The phase count (Lemma Φ) is unrefereed.
- Data (DATA, not proof): REFEREE fb_probe.py: named set (53 files, one o asserted) reproduces the packet's counts (207 fallbacks, max
  block 25, J ≤ 3, 23 J1, 159 CAP, 40,704 OFF), plus 3,300 random general games and 4,000 random 𝒞^1O; 0 failures. REFEREE-2 (own
  code): 8,265 runs + 9,600 climb runs, 0 violations; the lane's 12 logs regenerated byte-identically.
- Signatures: REFEREE docs/referee/R-N5-FB.md (referee eb1ec3c; §C 2b78c6d): Theorem FB SIGNED WITH GAPS (FB-1, FB-2, closed);
  Corollary, (T), TAME, MONO, NOINF, J1, OFF, A SIGNED; COARSE-SI (a) SIGNED WITH GAPS (ENG-1, V-1, V-2); CAP SIGNED WITH GAP CAP-1
  (closed); §C: no disagreement, G-FB-2 and G-FB-3 accepted (only these two citations were 𝒞^1O-scoped), both CAP closures valid
  (REFEREE-2's recommended), L ≥ M_k OPEN. REFEREE-2 docs/referee-2/R2-N5-FB.md (referee-2 7699593; §C eb10cf7): FB SIGN WITH GAPS (G-FB-1, G-FB-2; FB-2 accepted in §C); Corollary SIGN WITH
  GAPS (G-FB-3); (T), COARSE-SI, TAME, MONO, NOINF, J1, OFF SIGN; CAP SIGN WITH GAPS (G-FB-4); A signed; §C: no disagreement, FB-2
  accepted, both CAP closures valid (REFEREE's case split recommended for the fixes file). Joint gap map: FB-1 = G-FB-1; FB-2;
  G-FB-2, G-FB-3; ENG-1; V-1 = N-FB-1; V-2; CAP-1 = G-FB-4; all closed.
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.

### R26 [refereed-only] N5 on one-Odd-choice games: W-flat runs outside route form are short (CASC-U2 for U2 stretches; CASC-U3 for U3 and U23 stretches, between events), with counting corollaries given fallbacks, W-changes and events (2026-10-25) — partial step-4 lemmas for N5 on a subclass (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C35.md, checker 3653d4a)
- Object (packet P-N5-U23, pinned trunk 7666336, unchanged during review): docs/new/P-N5-U23-box31.md, sha1
  ee3e5d1ef95623d3f5e08a34af416fa6b2d09186 (L-NEW successor 11, Opus 5.5). The referees' repairs are collected by the lane in
  docs/new/P-N5-U23-fixes-box31.md (l-new 0274bd5, on trunk; sha1 870c63a35ceafbd6d8cf94ea9b43923002c68ca6, L-NEW successor 12; a
  record, not itself refereed text).
  Setting as in R22 and R24 (𝒞^1O; a PHASE is a joint λ-phase with τ constant; R ∋ o, F := V \ R; route form). A STRETCH is a
  maximal run of states of a phase with R, θ, w constant; a W-FLAT RUN is a maximal run of consecutive non-fallback transitions of a
  stretch with W unchanged at every vertex of R. U2: ¬H1 and c_θ := λ_Ξ(o) ≠ o, with the W frame in route form; U3: ¬H2 and
  c_w := λ_W(o) ≠ o, with the honest frame in route form; U23: ¬H1, ¬H2, c_θ ≠ o, c_w ≠ o. π_v is v's σ-route (its (σ, τ)-path before
  its first visit of o); level ℓ(v) := |π_v|.
- Claims signed (both referees "(Opus 5.5, D15)", L37):
  (a) Lemma CASC-U2: in a W-flat run of a U2 stretch, an R-vertex v switches only at run steps 0, …, ℓ(v) − 2. Proof: R24 CASC step 3
      with three new steps (levels constant via P-N5-NH (R1), W half; honest values on R are route functions with constant terminals
      θ and Ξ(c_θ); R24 TB's choice rule with keys depending only on σ along π_z).
  (b) Corollary: a U2 stretch with f fallback transitions and K_W non-fallback transitions with a W-change on R has at most
      f + K_W + (K_W + f + 1)(|R| − 2) transitions that change Ξ, W or σ on R.
  (c) Lemma CASC-U3 (U3 and U23 stretches; under ¬H2, o lies on its W-cycle o → A1 → c_w → A2 → o; v ∈ R \ {o} is of KIND A if
      c_w ∈ π_v, else KIND B; an EVENT is a switch of an Even R-vertex that changes its kind, or a switch of c_w, whose choice is SPEC
      S1 (v) / FIX 2): in an event-free sub-run, kinds are constant, and (i) a kind-B vertex v switches only at sub-run steps
      ≤ |π_v| − 2; (ii) a kind-A vertex v whose σ-path reaches c_w after λ(v) steps switches only at sub-run steps
      ≤ max(L_B − 1, 0) + λ(v) − 2, with L_B the largest |π| over kind B (0 if kind B is empty); (iii) no R-vertex switches at a sub-run
      step ≥ 2|R| − 4. The packet's (ii) "≤ L_B + λ(v) − 3" is unproved when kind B is empty (L_B = 0: the proof gives ≤ λ − 2);
      repaired as above (U3-1 = G-U23-1; REFEREE's form max(L_B, 1) + λ − 3 is the same bound); no counterexample. "Kinds constant"
      is proved by induction along the new routes when several vertices switch at once (U3-2); the case c_θ = c_w under U23 is
      covered (Ξ(c_w) = (c_w, ∅, 0); U3-3).
  (d) Corollary: a U3 or U23 stretch with f fallbacks, K_W non-fallback W-changes on R and E transitions containing an event has at
      most f + K_W + E + (K_W + f + E + 1)(2|R| − 4) R-changing transitions. (Sharper per-sub-run factor available: L_B + λ ≤ |R| − 2,
      REFEREE §2.4, accepted by REFEREE-2.)
- Reading (checked by both referees, not signed): with R24 §6, (NH') reduces to (X), NFB-O, (E) and (K_W). Stretch counts under ¬H1
  need the θ-changes, which TF (it needs H1) does not cover: under ¬H1, θ = (c_θ, ∅, d) with d monotone (R15 (a)), so θ changes at
  most |R| − 1 times per phase (REFEREE R-1 = REFEREE-2 N-U23-2; closed by R-1's argument, re-checked by REFEREE-2).
- Honest limits: (i) SUBCLASS 𝒞^1O; a bound on N5 itself. (ii) Both bounds are GIVEN f, K_W and E. (E) (events per W-flat run:
  kind crossings and c_w's switches) and (K_W) (non-fallback W-changes on R outside route form; R24's κ_w-freeze does not transfer)
  are OPEN, as are (X) and NFB-O; G-N5-TIME stays open. (iii) DATA is thin: CASC-U2 is exercised only by L-RED's u2flat_n32
  (experiments/red/xing/instances/u2flat_n32.pg, l-red bee6487, sha1 1a016c446d8c48b0e856d88b4527f61dfb1983e0; Lead re-run n5 13/3,
  Oink zlk OK strategies verified, one Odd choice vertex): 2 U2 W-flat switches at run step 0 (REFEREE), 7 over 20 starts with the
  bound attained (REFEREE-2); the kind-B half of CASC-U3 is vacuous in all data; the literal (ii) never failed, but its L_B = 0 corner
  had no switch in any sub-run. (iv) Lane DATA (not re-checked by the referees): every (E) and (K_W) transition seen is tame in
  RESULTS R25's sense (78 of 78), so neither is charged to J. (v) The lane's checker u23check.py tests less than the packet (U23
  stretches unchecked, (iii) at 2|R|, (ii) and corollaries untested; L-RED box 35); L-RED's u23x.py checks the packet as stated: 0
  violations on ~90 pinned 𝒞^1O instances.
- Data (DATA, not proof; every probe asserts one Odd choice vertex): REFEREE u23_probe.py (own code): 120 named 𝒞^1O instances
  (U2 / U3 / U23 stretches 39 / 54 / 90), 5,500 random runs (all W-flat runs switch-free, vacuous), 3 climbs (7,845 candidates);
  nr_u23_n32 32 kind-A switches within (ii); u3ev_n16 8 W-flat switches, all events (n5 6/0, Oink OK); 0 failures. REFEREE-2
  u23_check.py (own code): 6,650 batch runs + 28,800 climb runs, 34,230 kind-A switches within the repaired bound (closest bound − 1),
  1,364 ¬H1 states with θ of the form (c_θ, ∅, d), 0 violations.
- Signatures: REFEREE docs/referee/R-N5-U23.md (referee 7ffbd9f; Appendix A 2bdb045; §C cde420b): CASC-U2 and Corollary SIGNED;
  CASC-U3 (i), (iii) SIGNED WITH GAPS (U3-2 closed, downgraded to wording in §C; U3-3 wording); (ii) SIGNED WITH GAP U3-1 (closed by
  the repair); Corollary SIGNED; §3 READING correct with R-1. REFEREE-2 docs/referee-2/R2-N5-U23.md (referee-2 07b22b0; §C 5e24010):
  CASC-U2 and Corollary SIGN; kinds/events, (i), (iii) SIGN, after §C SIGN WITH GAPS (U3-2, U3-3 accepted as precisions; closed);
  (ii) SIGN WITH GAPS (G-U23-1, closed); Corollary SIGN; §3 READING correct with N-U23-2. §C: no disagreement. Joint gap map
  (REFEREE §C.3, REFEREE-2 §C.6): U3-1 = G-U23-1 (closed); U3-2 (closed); U3-3 (wording); §2.4 sharpening (accepted); R-1 =
  N-U23-2 (closed); N-U23-1 (CASC-U2 vacuous) superseded by u2flat_n32.
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.

### R27 [refereed-only] N5 inside a phase: the used-level freeze and a carry bound (Lemma U, HI, UL, GR, NU, Theorem LP), dormant edges and wakes on one-Odd-choice games (DF′, BAND, WAKE), and on those games σ̄(o)-changes, non-tame transitions and fallbacks per phase reduce to θ-changes and crossings (TH, SO, Corollaries LP′, XJ) (2026-10-25) — partial step-4 lemmas for N5 (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C36.md, checker 108c2e6 + Addendum c64ec13)
- Objects (pinned, unchanged during review): packet P-N5-LP docs/new/P-N5-LP-box32.md, sha1 d2c8121a0089add13c9417080cfb57620f592c88,
  pinned trunk bc42f2c; packet P-N5-SO docs/new/P-N5-SO-box32.md, sha1 deb5ee4422da3ab7389ce35e4542977927b53886, pinned trunk 1ef02bb (both
  L-NEW successor 12, Opus 5.5). The referees' repairs are collected by the lane in docs/new/P-N5-LP-fixes-box32.md (l-new 459660c, on
  trunk; sha1 af17cce0ec8686994a64dbaf512e89be67809eb0) and docs/new/P-N5-SO-fixes-box32.md (l-new 078c05d, on trunk; sha1
  cae3bb5b9aa67e5d54f38cca0d5be8a2b6b0cd0a), L-NEW successor 12; records, not themselves refereed text.
  Setting: N5 (SPEC docs/new/N5-ssi-global.md) on any game unless marked 𝒞^1O; valuations x = (c, P, ℓ), lev and COARSE_L as in RESULTS
  R25; Ξ_k = Θ_{H_k} (ENG-1, inherited); a PHASE is a run of transitions with λ_Ξ and τ constant. RELEVANT CHANGE at k → k+1: an Even y
  with σ_{k+1}(y) ≠ σ_k(y) and λ_k(y) ≠ y, or an Odd u with σ̄_{k+1}(u) ≠ σ̄_k(u) and λ_k(u) ≠ u. USED LEVEL L_k := the max of
  lev(Ξ_k(old successor), Ξ_k(new successor)) over the relevant changes (⊥ if none); a transition is NU if L_k = ⊥, RELEVANT otherwise.
  A RISE is a pair of consecutive relevant transitions k < k′ (only NU between) with L_{k′} > L_k; ρ := #rises; ε := #relevant transitions
  whose used level is attained only by Odd changes. On 𝒞^1O: R, F, crossing, c_θ, c_w as in R21-R26; S_o := #transitions with a relevant
  σ̄(o) change; Θ := #transitions changing θ = Ξ(o); X := #crossings; J := #non-tame transitions (R25); d_o := |succ(o)|. A WAKE at k′ is
  a relevant Even switch at k′ of level > L_k (k < k′ consecutive relevant, no fallback in [k, k′], R constant on [k, k′ + 1]); K := #wakes.
- Claims signed (both referees "(Opus 5.5, D15)", L37):
  (a) Lemma U (used-level freeze; any game, inside a phase): L_k < ∞ and COARSE_{L_k}(Ξ_{k+1}(v)) = COARSE_{L_k}(Ξ_k(v)) for every v; an
      NU transition leaves Ξ unchanged. (R25 TAME's proof with M_k replaced by L_k; checked line by line by REFEREE.)
  (b) Lemma HI: with L := L_k ≠ ⊥ and y an Even vertex that is not an own cycle node switched at k, for every ℓ > L, (y, z) is a gate edge
      of level ℓ at k iff at k+1. Its Consequence: "≤" (M_{k+1} ≤ M_k) by REFEREE's HI-1 argument (single signature; REFEREE-2 G-LP-2:
      unproved as written); unused downstream.
  (c) Lemma UL (L_k = ℓ ≥ 0 is never attained by a relevant switch of the rank-ℓ vertex u_ℓ), Lemma GR (ℓ-goodness: (a) if L_k = ⊥ or
      L_k ≤ ℓ then G_ℓ(k) ⊆ G_ℓ(k+1); (b) if L_k = ℓ is attained by a relevant Even switch of y then y ∉ G_ℓ(k), y ∈ G_ℓ(k+1)), Lemma NU (a
      run of consecutive NU transitions has ≤ Σ_{y Even}(deg(y) − 1) ≤ m − n transitions).
  (d) Theorem LP (any game): a phase with T transitions, T_rel relevant, has T ≤ (m − n + 1)(T_rel + 1) and
      T_rel ≤ (n + 1)(ρ + 1)·n(n − 1) + ε (n ≥ 2). Step 4's "y ⊕ keeps order and strictness" holds here because the values compared share
      one path set (N-LP-1, wording).
  (e) On 𝒞^1O: Lemma DF′: at an S4a transition k → k+1 of a phase, if (y, z) is an edge of the arena H_k that is a gate edge at k+1 and y
      is not its own (W-)cycle node at k+1, then σ_{k+1}(y) ∈ R_{k+1} (two proofs: REFEREE, Bellman via R24 G-TB-1, (F1) only; REFEREE-2,
      R15 (a) Lemma A + (F1) + R15 (b) Lemma B). Lemma BAND: at a state with both frames in route form and c_θ ≠ c_w, a gate edge (y, z) of
      level ℓ ≥ 0 with σ(y), z ∈ R and W(z) ⊴ W(σ y) has rank c_θ < ℓ < rank c_w and equal W path sets. Lemma WAKE: a wake y: a → z has
      a, z ∈ R; if both frames are in route form, the state is in a U1 piece (cites DF′: W-1 = G-LP-1, closed).
  (f) Corollary LP′ (𝒞^1O): with f fallback transitions, T ≤ (m − n + 1)·((n + 1)(2f + S_o + 2X + K + 1)·n(n − 1) + S_o + 1) with
      f ≤ n_E(2n − 1)(S_o + 1) + S_o; so T = O(m·n⁵·(1 + S_o + X + K)). (Via ε ≤ S_o, ρ ≤ 2f + S_o + 2X + K, J ≤ S_o by R25 J1 and Lemma
      U, and R25 Theorem FB; it uses neither DF nor WAKE.)
  (g) On 𝒞^1O, per phase with λ_Ξ(o) ≠ o: Lemma TH: Θ ≤ (n − 1) + n(X + 1) + X (¬H1: θ = (c_θ, ∅, d), RESULTS R26's R-1; H1: σ̄(o) is a
      full Ξ-minimiser (R25 CAP-1, REFEREE's case proof, re-checked and adopted by REFEREE-2 in R2-N5-FB §C.3: SO-1, closed with two
      signatures) and a θ-change changes Ξ at that exit in F, one of R22 F1°'s F-changes (F1° transfers to this coarser phase: N-SO-1)).
      Lemma SO: S_o ≤ Θ + (d_o − 1)(Θ + 1) ≤ d_o(Θ + 1); at a relevant σ̄(o) change with θ unchanged, the old choice is no longer a
      minimiser (the R24 Lemma R / TB key of an exit that stays a minimiser is frozen; the strict rises use (SG), R19 (d), and the prefix
      vertices lie in no path set: G-SO-1, closed; N-SO-3 wording).
  (h) Corollary XJ (𝒞^1O): S_o ≤ d_o(2n + (n + 1)X) and J ≤ S_o, so f = O(d_o·n³(1 + X)) ⊆ O(n⁴(1 + X)) (XJ-1 = N-SO-2: the packet's
      O(n³(1 + X)) is corrected); with (f), a phase has T = O(m·n⁷(1 + X) + m·n⁵·K) transitions.
- Refuted: Lemma DF as stated (without "y not its own cycle node") is FALSE, NOT SIGNED by both referees: the cited VJ00 (BRICS
  RS-00-48) Lemma 5.8 step 2 ⇒ 3 ⇒ 1 ("a maximum has no improvement") fails at own cycle nodes, where a length-only improvement is kept by
  FIX 2's DFS (as in RESULTS R15's side finding). Counterexamples: docs/referee/R-N5-LP/df_cex.pg (n 11, sha1 a128663e…, o = 1) and
  docs/referee-2/R2-N5-LP/instances/df_cex.pg (n 5, sha1 0a98e1b7…, o = 3); Lead re-ran both: n5 2/1, Oink zlk OK strategies verified,
  one Odd choice vertex (the DF failure itself is the referees' own code). Lane forms refuted before the packets (P-N5-LP §5, not
  signed): NO-WAKE "K = 0" FALSE (experiments/new/box32/instances/nowake_cex_n32.pg, sha1 3a56e3fb…; reproduced by both referees and the
  Lead); (KW-M) FALSE (instances/kwm_cex_n24.pg, sha1 c2723e08…; Lead re-run).
- Reading (not signed): with Corollary XJ, RESULTS R25's open core (J-poly), NFB-O and the fallback count follow from (X); per phase of
  o-cyclic 𝒞^1O the open quantities are X (≡ Z up to a factor n, R23 LV′) and K (wakes: in U1 pieces bounded by R24 Theorem U1; in U2 /
  U3 / U23 stretches by R26's corollaries in terms of the open (E) and (K_W)).
- Honest limits: (i) Lemma U, HI, UL, GR, NU and Theorem LP hold on every game; DF′, BAND, WAKE, LP′, TH, SO and XJ are on 𝒞^1O.
  (ii) Theorem LP bounds nothing by itself: it moves the count to rises (carries) and ε. (iii) X and K per phase are OPEN, so G-N5-TIME
  stays open; the phase count (Lemma Φ) is unrefereed. (iv) The bounds are loose in d_o and n; the data show neither a growth law nor
  tightness beyond J = S_o (REFEREE-2). (v) DATA on K: nowake_cex_n32 has one wake, a U3 W-tie switch in the length-only regime
  (P-N5-LP §5); L-NEW's climbs found at most 2 wakes per run (docs/new/N5-L-box32.md, lane DATA, not re-checked by the referees).
- Data (DATA, not proof; every probe asserts one Odd choice vertex where 𝒞^1O): REFEREE lp_probe.py (own code): 228 library 𝒞^1O files
  (5,482 in-phase transitions), 4,500 random 𝒞^1O runs, 1,500 random general games: 0 failures of §1-§2; DF 170 failures (all own W-cycle
  nodes), DF′ 0; so_probe.py: 234 library files (257 phases with λ(o) ≠ o) + 3,000 random runs: 0 failures of TH, SO, XJ (max Θ 51,
  S_o 49). REFEREE-2 (own code): 8,284 runs on LP, 0 violations of the signed statements (176 DF failures, all own-cycle-node length-only
  edges); SO batch 4,502 runs + 6 climbs (12,000 fully checked runs aimed at S_o − d_o(Θ + 1), J − S_o and θ-fixed σ̄(o) changes): 0
  violations, best margins −1 and 0; 3,915 relevant σ̄(o) changes with θ fixed, the old choice leaving the minimiser set every time.
  L-NEW's socheck.py, run unmodified by L-SI (docs/si/N5-C-box8.md §8), on L-SI's climb bests and the named set: 0 failures (max J 18 ≤ S_o 19, n 48); Lead socheck on jcl_zcl_cu_n48: J 17 ≤ S_o
  18 = d_o.
- Signatures: REFEREE docs/referee/R-N5-LP.md (referee 4957b2c; Part 2 = P-N5-SO dcb4119; §C bb6f60f; SO-1 addendum 2a0cb30): U, UL, GR,
  NU, Theorem LP, BAND, LP′ SIGNED; HI SIGNED, Consequence WITH GAP HI-1; DF NOT SIGNED (FALSE), DF′ SIGNED; WAKE SIGNED WITH GAP W-1
  (closed); SO SIGNED; TH SIGNED (SO-1 closed in the addendum); XJ SIGNED WITH GAP XJ-1. REFEREE-2 docs/referee-2/R2-N5-LP.md (referee-2
  4949d6c; §8 = P-N5-SO ba67f41; combined §C caee2ae): U, HI, UL, GR, NU SIGN (HI Consequence G-LP-2); Theorem LP SIGN (N-LP-1); DF NOT
  SIGNED, DF′ SIGN; BAND SIGN; WAKE SIGN WITH GAPS (G-LP-1, closed); LP′ SIGN; TH SIGN (N-SO-1); SO SIGN WITH GAPS (G-SO-1, closed;
  N-SO-3); XJ SIGN WITH GAPS (N-SO-2). §C (REFEREE: P-N5-LP; REFEREE-2: both): no disagreement. Joint gap map: P-N5-LP rows REFEREE §C and REFEREE-2 §C.2; P-N5-SO rows
  REFEREE-2 §C.1-§C.2 only (REFEREE compared Part 1 only; both referees signed P-N5-SO independently with gaps listed): DF FALSE, DF′ signed by both;
  HI-1 = G-LP-2; W-1 = G-LP-1 (closed); N-LP-1 (wording); SO-1 (closed, two signatures); XJ-1 = N-SO-2; G-SO-1 (closed), N-SO-1, N-SO-3.
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.

### R28 [refereed-only] N5 on one-Odd-choice games: off crossings σ̄(o) never outruns Even (Lemma OE, with a local used-level freeze U-loc), so non-tame transitions, fallbacks and carries per phase are polynomial in crossings and wakes (Corollary OX) (2026-10-25) — partial step-4 lemmas for N5 (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C37.md, checker f5c4672)
- Object (packet P-N5-OE, pinned trunk 361d18c, unchanged during review): docs/new/P-N5-OE-box32.md, sha1
  adeccd898ad1e4de6532fc3a77a9d600d8a0bc16 (L-NEW successor 12, Opus 5.5). The referees' repairs are collected by the lane in
  docs/new/P-N5-OE-fixes-box32.md (l-new 7ad82a9, on trunk; sha1 5f06276a32824c872493b92a82081c13e6d0ba01, L-NEW successor 13; a record,
  not itself refereed text).
  Setting as in RESULTS R27 (relevant changes, used level L_k, NU, phase with λ_Ξ and τ constant, R, F, crossing, wakes, K; Ξ_k = Θ_{H_k},
  ENG-1). E_k := the max level of the relevant Even changes at k → k+1 (⊥ if none); O_k := the level of the relevant σ̄(o) change (⊥ if
  none); on 𝒞^1O, L_k = max(E_k, O_k). The packet's phase key (λ_Ξ, τ) is coarser than R25's (λ_Ξ, λ_U, τ); the cited R22 TC (i) and R25
  FB, J1, CAP-1 use only λ_Ξ and τ or hold statewise, so they apply (N-OE-3, closed).
- Claims signed (both referees "(Opus 5.5, D15)", L37):
  (a) Lemma U-loc (any game, inside a phase): if every relevant change at a vertex of v's H_{k+1}-path before its first visit of
      c := λ(v) has level ≤ L, then COARSE_L(Ξ_{k+1}(v)) = COARSE_L(Ξ_k(v)) (R27 (a) Lemma U's proof, localised).
  (b) Lemma OE (𝒞^1O): at a transition of a phase with R_k = R_{k+1} (no crossing), O_k ≤ E_k; so σ̄(o) makes no relevant change of
      level ≠ ⊥ when Even makes no relevant change. The packet's "In particular" sentence (no relevant σ̄(o) change at all when Even makes
      none) is stronger than the proof by a level-⊥ tie move at o; it is unproved, not refuted (0 such cases in all data; tie changes
      off crossings occur only with E_k ≠ ⊥: REFEREE library 2 / random 50, REFEREE-2 library 2 / random 5) and is not used (OE-1 =
      N-OE-1, wording). Step 1 uses CAP-1 (σ̄(o) a full Ξ-minimiser when λ(o) ≠ o, including o on its honest cycle: RESULTS R25 CAP-1,
      REFEREE's case proof, adopted by REFEREE-2 in R2-N5-FB §C.3; OE-2, closed); step 3 compares by (C1) and (C3) (OE-3, wording) and uses
      that under H1 x0's honest play is the tail of o's, so it avoids o (N-OE-2, wording).
  (c) Corollary OX (𝒞^1O): in a phase with X crossings, K wakes and f fallback transitions, (i) ε ≤ X; (ii) J ≤ X; (iii) ρ ≤ 2f + 2X + K;
      (iv) f ≤ n_E(2n − 1)(X + 1) + X; (v) T ≤ (m − n + 1)·((n + 1)(2f + 2X + K + 1)·n(n − 1) + X + 1) = O(m·n⁵·(1 + X + K)); f and T
      count transitions with both ends in the phase (R25 FB-2; OX-1, wording). (From R27 Theorem LP and Corollary LP′ step 2, R25 (d)
      Theorem FB and (e) J1, R15 (d); sharper than R27 (h) Corollary XJ: no S_o or Θ term.)
- Reading (not signed): per phase of o-cyclic 𝒞^1O, everything is polynomial in X (crossings, ≡ Z up to a factor n by R23 LV′, the
  direction a bound on Z needs) and K (wakes: in U1 pieces bounded by R24 Theorem U1; in U2 / U3 / U23 stretches by R26's corollaries in
  terms of the open (E) and (K_W)). RESULTS R25's (J-poly) and the fallback count follow from (X) with J ≤ X.
- Honest limits: (i) U-loc holds on every game inside a phase; OE and OX are on 𝒞^1O. (ii) X and K per phase are OPEN, so G-N5-TIME stays
  open; the phase count (Lemma Φ) is unrefereed. (iii) The wake term is barely exercised: K ≤ 1 in both referees' data. (iv) Both
  referees' DATA show O_k > E_k only at crossings and every non-tame transition at a crossing; J = X is attained (jcl_zcl_cu_n48:
  J 17 = X 17; Lead re-run n5 23/1, Oink zlk OK strategies verified, one Odd choice vertex).
- Data (DATA, not proof; every probe asserts one Odd choice vertex): REFEREE oe_probe.py (own code, trace asserted = n5.run): 234 library
  𝒞^1O files, 5,603 in-phase transitions, 0 failures (crossing-free σ̄(o) changes 436 H1 + 11 ¬H1; O_k > E_k 279 times, all crossings;
  235 non-tame, all crossings; the lane's oddlev.py gives identical counts); 11,000 random games, 0 failures. REFEREE-2 oe_check.py (own
  code): the 234-file library × 3 starts + 7,600 random runs (3,800 general for U-loc), 0 violations (U-loc 373,394 checks; OE 5,015
  crossing-free transitions; O_k > E_k 602 times, all crossings; 509 non-tame, all crossings; CAP-1 held at all 19,573 states with
  λ(o) ≠ o, and fails at 420 states with λ(o) = o, which OE never uses); climbs 27,200 runs (72,414 off-crossing σ̄(o) changes, 4,598
  under ¬H1; 30,002 non-tame transitions, all crossings; J − X never > 0). Three implementations agree on the canonical-start library
  counts (436 + 11 / 279 / 235).
- Signatures: REFEREE docs/referee/R-N5-OE.md (referee 5e98e33, stamp fix 696b08c; §C 8474881): U-loc SIGNED; OE SIGNED WITH GAPS OE-1,
  OE-2 (closed), OE-3; OX SIGNED (OX-1 wording); §C: no verdict differs; N-OE-3 missed by REFEREE, accepted. REFEREE-2
  docs/referee-2/R2-N5-OE.md (referee-2 ca6e5bd; §C ea6ad67): U-loc, OE, OX (i)-(v) SIGN (notes N-OE-1..3); §C: no disagreement of
  substance; its own "0 tie moves" corrected to the general count (library 2, random 5). Joint gap map (REFEREE §C, REFEREE-2 §C): OE-1 =
  N-OE-1 (wording); OE-2 (closed); OE-3 + N-OE-2 (wording); N-OE-3 (closed); OX-1 (wording).
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.

### R29 [refereed-only] N5 on one-Odd-choice games: gates into F never exceed the gate level (OFFGATE), cycle-node switches are length-only (CN), values off R̄ freeze at S4a steps above a gap (NL), and fallback levels never rise along a scope run at THR fallbacks (Theorem CLS1) (2026-10-25) — partial step-4 lemmas for N5 (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C38.md, checker b250d88 + Addenda f0cf7c9, 7d31aba)
- Object (packet P-N5-CLS, pinned trunk 486107a, unchanged during review): docs/si/P-N5-CLS-box8.md, sha1
  5bbfd872383d9b2c2d3caaf902b174d0aa54e4ae (L-SI successor 3, Opus 5.5). The referees' repairs are collected by the lane in
  docs/si/P-N5-CLS-fixes-box8.md (l-si 2c5e57c, on trunk; sha1 92f79dc98628159a1ef328b76a1672851eb0dda1, L-SI successor 3; a record, not
  itself refereed text; it holds CLS-1..CLS-4 and N-CLS-1) and docs/si/P-N5-CLS-fixes2-box8.md (l-si b90f639, on trunk; sha1
  8f1b52b4dce13e758bcc4b0b05e98750e0a51ce4; part 2, the six-row joint map; N-CLS-2 is a row of REFEREE's §C only (REFEREE-2 §C: same argument, no row needed)).
  Setting: N5 as in RESULTS R25 (gates, gate levels, M_k, lev, COARSE_L, (C1)-(C4), Ξ_k = Θ_{H_k}, ENG-1). PHASE: a joint λ-phase with
  τ constant. On 𝒞^1O, R, R̄ := R ∪ {o}, F, (h), EQ / THR, u* as in R19-R23. SCOPE RUN: a maximal run of consecutive in-phase transitions
  k → k+1 with (h) at k, H2 at k+1 and w_{k+1} = w_k. r_k := lev(θ_k, w_k) (< ∞ under (h)).
- Claims signed (both referees "(Opus 5.5, D15)", L37):
  (a) Elementary facts (C5) (a ◁ b ⊴ c ⇒ lev(a, b) ≤ lev(a, c)), (C6) (lev(a, c) ≤ max(lev(a, b), lev(b, c))), (C7) (a prefix disjoint
      from both path sets and cycle nodes preserves lev and order); Fact R (r is non-increasing along a scope run); Lemma CLU (at an
      in-phase S4c fallback k with (h) and θ_k ◁ w_k, every switched y → z with y ∈ R_k, z ∈ F_k has level ≤ r_k; re-proved from R23 (f)).
  (b) Lemma TRANSFER (every game): for an in-phase k → k+1, L < ∞ and z with COARSE_L(Ξ_{k+1} z) = COARSE_L(Ξ_k z), a gate (y, z) at
      k+1 of level > L is a gate at k of level > L.
  (c) Lemma OFFGATE (𝒞^1O): at every in-phase transition, tame or not, every gate (y, z) at k+1 with z ∉ R̄_{k+1} has level ≤ M_k. (M_k ≥ −1
      at every in-phase transition, since no gate means σ unchanged and so τ changes: CLS-1, wording; R̄ is R25 OFF's honest
      reachability, equal to the (σ, τ) one on 𝒞^1O: N-CLS-1.)
  (d) Lemma CN (every game, inside a phase): if λ_{k+1} = λ_k and an Even y with λ_k(y) = y switches to z, the gate level of (y, z) at k
      is −1 (CLS-2, wording).
  (e) Lemma NL (𝒞^1O): at an S4a transition j → j+1 inside a phase with (h) at j, L < ∞, r_j > L and (A_j) (every gate at j into F_j has
      level ≤ L): (i) COARSE_L(Ξ) is unchanged on every v ∉ R̄_{j+1}; (ii) R_j ⊆ R̄_{j+1} (no leave); (iii) (A_{j+1}) holds.
  (f) Theorem CLS1 (𝒞^1O): in a scope run S, at an S4c fallback k1 at a THR state with r_{k1} ≥ 0 (u* ≠ none),
      M_{k1} ≤ min{M_k : k < k1 an S4c fallback of S}. Its case r_{k1} ≤ L uses FBL in its u* ≠ none strong gate form at the single state
      k1 (no F → R and no R → R gate edge; R-N5-XA §3, R2-N5-XA §2), not "a single fallback state is a stretch of length 1"
      (CLS-3 = G-CLS-1, citation, closed); every in-scope fallback is THR or EQ, since under (h) θ = w ⟺ EQ (N-CLS-2, wording).
      Corollary: along a scope run, the levels of its THR fallbacks with u* ≠ none are non-increasing; these are all its fallbacks
      before the first EQ / u* = none state (Fact R) ("evicting" dropped: CLS-4, wording).
- Refuted (both referees, own code): OG′ "gates into F at k+1 have level ≤ MF_k (the max level of the gates at k into F_k)" is FALSE:
  experiments/red/xing/instances/x31_re24.pg (sha1 49eaf50e…), transition 1 → 2, an S4a step: MF_1 = −1, gate (4, 8) at state 2 of level
  22 into F, |R| 21 → 1; OFFGATE holds there (M_1 = 23). REFEREE found 17 more violations in random games. The data counter MF_up in the
  lane's cls2.py is this OG′ counter, not a rise of a fallback level.
- Honest limits: (i) TRANSFER, CN and (C5)-(C7) hold on every game; Fact R, CLU, OFFGATE, NL, CLS1 are on 𝒞^1O. (ii) CLS1 bounds the
  levels, not the number, of fallbacks per scope run: the per-level count ("≤ n_E fallbacks per level") is OPEN, as are fallbacks at EQ
  states or with u* = none ((H-EQ)) and θ-changes per scope run without X; G-N5-TIME stays open. (iii) No fallback with u* = none occurs in
  any data, so CLS1's (β) case rests on Fact R alone; CN has few library cases (48; 711 random). (iv) Random games are nearly vacuous for
  CLS1 (≤ 1 fallback per scope run); the evidence is the named set, the library and REFEREE-2's climbs.
- Data (DATA, not proof; one Odd choice vertex asserted on every game): REFEREE cls_probe.py (own trace = n5.run, phase key
  (λ_Ξ, λ_U, τ)): named 65 / library 234 / random 5,500 games, 0 failures of every check; its named counts equal the packet's §8
  (OFFGATE 6,645; CN 7; 70 scope runs; in-scope fallbacks 252 THR u* ≠ none / 4 EQ / 0 u* = none); no rise of M at any in-scope
  fallback (named 256, library 534). REFEREE-2 (own code): 234 files × 3 starts + 12,000 random + 12,400 climb runs, 913 in-scope
  fallbacks (890 THR u* ≠ none, 23 EQ, 0 u* = none), 0 failures; TRANSFER 442,864, OFFGATE 26,464, CLU 1,948 checks; NL tested at every
  admissible L (40,516 library + 20,283 climb checks); CLS1's case r > L 678 library comparisons with (A_j) asserted at all 1,731
  intermediate states, + 20,544 in climbs. Lead re-ran experiments/si/coarse/run_cls.sh: the packet's logs regenerate byte-identically.
- Signatures: REFEREE docs/referee/R-N5-CLS.md (referee a0b92ec; §C 8af6347): (C5)-(C7), Fact R, CLU, TRANSFER, NL SIGNED; OFFGATE
  SIGNED WITH GAP CLS-1; CN SIGNED WITH GAP CLS-2; CLS1 SIGNED WITH GAP CLS-3 (closed); Corollary SIGNED WITH GAP CLS-4; OG′ FALSE
  confirmed. REFEREE-2 docs/referee-2/R2-N5-CLS.md (referee-2 ffe10e1; §C 848839e): (C5)-(C7), Fact R, CLU, TRANSFER, CN, NL SIGN; OFFGATE
  SIGN (N-CLS-1); CLS1 + Corollary SIGN WITH GAPS G-CLS-1 (closed), N-CLS-2; OG′ refutation reproduced. §C: no verdict differs. Joint
  gap map (REFEREE §C, REFEREE-2 §C): CLS-3 = G-CLS-1 (closed, REFEREE-2's form adopted); CLS-1, CLS-2, CLS-4, N-CLS-1, N-CLS-2 (wording).
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.

### R30 [refereed-only] N5 on one-Odd-choice games: anatomy of an ε-transition (OR, TC-SPLIT), R never shrinks at S4a steps outside the c_w = c_θ regime (R-STICK, SN-PREFIX, H3H2), who can leave R (LEAVE), counting absorptions (ABS-COUNT′, with H1-DROP and H1-KEEP), wakes in the odd mode (WK), and absorptions above a fallback level (ABS-L) (2026-10-25) — partial step-4 lemmas for N5 (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C39.md, checker 09c8dc7 + Addendum 262104b)
- Object (packet P-N5-SN, pinned trunk 2c70ef6, unchanged during review): docs/new/P-N5-SN-box33.md, sha1
  340d4f298d8ee137b53ff76d7dd81de49f8fa542 (L-NEW successor 13, Opus 5.5). The referees' repairs and the lane's repair of SN-1 are in
  docs/new/P-N5-SN-fixes-box33.md (l-new 9de7820, on trunk; sha1 f242b0118a30cf3362cda59e48787cc0bd1768b2, L-NEW successor 13); its §2b (H1-DROP, H1-KEEP, ABS-COUNT′) is new
  proof text, signed by both referees in addenda (REFEREE-2 R2-N5-SN §B, REFEREE R-N5-SN Addendum 2); the rest of the file is a record.
  Setting as in RESULTS R27-R29 (𝒞^1O; phase with λ_Ξ and τ constant; R, F, H1-H3, (h), c_θ := λ(o), c_w := the W-cycle node of o,
  crossings; relevant changes, E_k, O_k, L_k; ε-transition: O_k > E_k; x0 := σ̄_k(o); scope runs and r := lev(θ, w) as in R29). An
  ABSORPTION is an ε-transition with x0 ∈ F_k ∩ R_{k+1}; REL_run := the number of exits of o leaving R at transitions of a run; d_o :=
  |succ(o)|; f := fallback transitions of the phase.
- Claims signed (both referees "(Opus 5.5, D15)", L37):
  (a) Lemma OR: at an ε-transition, (a) x0's H_{k+1}-path to c visits o, so x0 ∈ R_{k+1}; (b) under H1 at k, x0 ∈ F_k (an absorption);
      (c) lev(θ_k, θ_{k+1}) = O_k and θ_{k+1} ▷ θ_k.
  (b) Lemma TC-SPLIT: at every phase transition with θ_{k+1} ≠ θ_k, lev(θ_k, θ_{k+1}) ≤ E_k, or k is an ε-transition and
      lev(θ_k, θ_{k+1}) = O_k.
  (c) Lemma R-STICK: at an S4a transition of a phase, every v ∈ R_s whose W-cycle node differs from λ(v) stays in R_{s+1}; so if
      c_w(s) ≠ c_θ, R_s ⊆ R_{s+1}. Corollary SN-PREFIX: in a run of consecutive non-fallback transitions of a phase, the states with
      c_w = c_θ form a prefix; after it R never loses a vertex, so at most n − 1 crossings follow; per phase, crossings ≤
      (f + 1)(n − 1) + f + X_SN, X_SN := S4a crossings at states with c_w = c_θ. (WM, R23 (g), applies on this phase: its proof uses only
      τ_{k+1} = τ_k at a non-fallback step and the S4a optimum; both referees.)
  (d) Lemma H3H2: H1 ∧ H3 ⇒ H2; so under H1 the regime c_w = c_θ is exactly (h).
  (e) Lemma LEAVE: at an S4a transition with H1, a vertex q ∈ R_s \ {o} leaving R has (h) at s, and q's H_{s+1}-path before its cycle node
      carries a relevant change of level ≥ r_s (L_s ≥ r_s); for r_s = ⊥ such a relevant change still exists (SN-3, wording).
  (f) Lemma H1-DROP (fixes §2b): inside a phase, H1 at k and ¬H1 at k+1 force P(θ_k) = ∅. Corollary H1-KEEP: at an ε-transition with H1
      at k and O_k ≥ 0, H1 holds at k+1. Corollary ABS-COUNT′: in a fallback-free run of a phase, the H1 ε-transitions number at most
      (d_o − 1) + REL_run if the run's last H1 ε-transition has O ≥ 0, and at most d_o + REL_run otherwise; per phase, ε_{H1} ≤
      (d_o − 1)(f + 1) + REL + f + ε⁽⁻¹⁾, with ε⁽⁻¹⁾ := runs whose last H1 ε-transition has O = −1 and + f for ε-transitions at fallbacks.
      The packet's ABS-COUNT ("(d_o − 1) + REL_run" for every run; per phase (d_o − 1)(f + 1) + REL) was unproved as written: "ends
      ≤ d_o − 1" needs H1 at the run's last state, and ε-transitions at fallbacks belong to no run (SN-1 = G-SN-1 (a), SN-2 = G-SN-1 (b));
      §2b closes SN-1 except ε⁽⁻¹⁾.
  (g) Lemma WK: a wake y: a → z (R27 (e)) with y not its own W-cycle node and W unchanged at a and z has an even W-cycle node at y (BFS
      mode); so in the odd mode every wake transition changes W on R. (y ⊕ is strictly monotone between W(z) and W(a) since y lies on
      neither W-path: N-SN-1, wording; REFEREE's Bellman route via R24 G-TB-1 also closes it.)
  (h) Lemma ABS-L (premises R29 (e) NL and (f) CLS1's proof): in a scope run, between consecutive fallbacks k0 < k with L := M_{k0} and
      r_j > L on [k0+1, k], every transition with lev(θ_j, θ_{j+1}) > L is an absorption whose exit stays in R up to k; so at most d_o − 1
      θ-changes above L in (k0, k).
- Refuted (not signed; L-RED, own checkers; Lead re-runs: n5 + Oink zlk + check_sol2, one Odd choice vertex, and L-NEW's orx.py EPS=1 /
  oddlev.py): CONJECTURE EXIT-R (an absorbed exit stays in R until the next fallback) is FALSE: experiments/red/so/instances/
  exitr_cex_n48.pg (sha1 7a663df2…, transition 4 absorbs exit 13, which leaves R at the S4a step 5→6, f = 0 in the phase), and
  exitr_cex_n16.pg (6971211e…). Its consequence "ε_{H1} ≤ (d_o − 1)(f + 1) per phase" is FALSE: epsseg_cex_n48.pg (b4c7dcb0…, phase f = 0,
  17 H1 ε-transitions against 16; exit 33 released at 8→9 and re-absorbed at 14) and epsseg_cex_n16.pg (8d83f7c2…, 6 against 5);
  ABS-COUNT′ holds on all of them (REL ≥ 1, tight on epsseg_cex_n48). Also lane forms (not signed): H-RE FALSE (b6_xl_n48); (KW-M) and
  NO-WAKE FALSE (R27).
- Honest limits: (i) SUBCLASS 𝒞^1O; inside a phase. (ii) REL (exit releases in the c_w = c_θ prefix), X_SN and K per phase are OPEN;
  ε⁽⁻¹⁾ and ε at fallbacks are OPEN but never observed; G-N5-TIME stays open. (iii) DATA is thin for WK (its hypothesis held at none of
  the observed wakes) and ABS-L (no θ-change above L in any window); no ¬H1 ε-transition was observed anywhere. (iv) K per phase can
  be Θ(n) (L-NEW K-chain family, DATA: kchain4/10/32 with 3/9/31 wakes; Lead re-ran kchain4; REFEREE reproduced 3/9/31 wakes, Oink OK).
- Data (DATA, not proof; one Odd choice vertex asserted on every game): REFEREE sn_probe.py + absc_climb.py (own code): 243 library files,
  the K-chain instances, 11,000 random games, 5 + 4 climbs, 0 failures (17 in-phase H1 → ¬H1 transitions, all with P(θ_k) = ∅; 349
  H1 ε-transitions on its 245-file Addendum-2 library, all O ≥ 0). REFEREE-2 (own code): library × 3 starts + 5,500 random, climbs 47,200 + 42,000 runs, 0 failures
  (R-STICK 867,072 checks; 39,461 crossings after a c_w = c_θ prefix; 23,798 H1 leaves, 14,438 tight; 15,716 in-phase H1 → ¬H1
  transitions, all P(θ_k) = ∅; 18,669 H1 ε-transitions, none with O = −1; 728 H1 ε-transitions on library × 3 + 5,500 random, all O ≥ 0). L-RED box 37 (Lead
  relay; own checker, library 241 files): 0 failures of OR, TC-SPLIT, R-STICK, SN-PREFIX, ABS-L; X_SN = X = 29 at n 32 (xsn29_n32); 31
  crossings after the prefix at n 48 (post31_n48; ≤ 47); CHECKER C39 re-ran both.
- Signatures: REFEREE docs/referee/R-N5-SN.md (referee 59a886d; addendum 58dd6e8; §C 3d49e0a; Addendum 2 on §2b 2f465ff): OR, TC-SPLIT,
  R-STICK, SN-PREFIX, H3H2, WK, ABS-L SIGNED; LEAVE SIGNED WITH GAP SN-3 (wording); ABS-COUNT SIGNED WITH GAPS SN-1, SN-2; H1-DROP,
  H1-KEEP, ABS-COUNT′ SIGNED. REFEREE-2 docs/referee-2/R2-N5-SN.md (referee-2 ddbecaf; §A 91d95e8; §C 80d2e45; §B on §2b 4c8dcfd): OR,
  TC-SPLIT, R-STICK, SN-PREFIX, H3H2, LEAVE SIGN; WK SIGN (N-SN-1); ABS-COUNT SIGN WITH GAPS G-SN-1; ABS-L SIGN (premises signed);
  H1-DROP, H1-KEEP, ABS-COUNT′ SIGN. WM transfer VALID in both. §C: no verdict differs. Joint gap map (REFEREE §C, REFEREE-2 §C): SN-1 =
  G-SN-1 (a) (closed by §2b except ε⁽⁻¹⁾); SN-2 = G-SN-1 (b) (+ f); SN-3, N-SN-1 (wording); ABS-L unconditional (R29).
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.

### R31 [refereed-only] N5 on one-Odd-choice games: a fallback gate never outruns the Ξ/W gap (Lemma FBW, every game), so fallback levels never rise along a whole scope run (Theorem CLS2, (H-EQ) closed), fallbacks of level ≥ 0 freeze coarse values (FLAT-ALL), a tail repeats at most once per frozen stretch (STRETCH), and an additive per-level fallback count (Theorem PL, Corollary PL-S) (2026-10-25) — partial step-4 lemmas for N5 (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C40.md, checker 737b193)
- Object (packet P-N5-FBW, pinned trunk e69772b, unchanged during review): docs/si/P-N5-FBW-box9.md, sha1
  88337bd621d3467dde4b35aa93b254bf847bb330 (L-SI successor 4, Opus 5.5). The referees' repairs are collected by the lane in
  docs/si/P-N5-FBW-fixes-box9.md (l-si 51491b7, on trunk; sha1 91ff42168f81a7b4ef2f5af10eea81c52225b42a, L-SI successor 4; repairs only,
  no strengthening of the reviewed text).
  Setting as in RESULTS R25 and R27-R30 (gates, gate levels, M_k, lev, COARSE_L, (C1)-(C7), Ξ_k = Θ_{H_k}; on 𝒞^1O: R, R̄, F, (h), EQ /
  THR, u*, scope runs, r_k := lev(θ_k, w_k), Fact R, OFF, Lemma G, Lemma S, TRANSFER, CN, NL, CLS1, U-loc, OR, TC-SPLIT, ABS-L). For an
  S4c fallback k and a gate (y, z) at k: u := σ_k(y), ℓ := lev(Ξ_k u, Ξ_k z), δ := max(lev(Ξ_k u, W_k u), lev(Ξ_k z, W_k z)). A BLOCK of
  a scope run S at level M ≥ 0 is the set f_1 < … < f_N of fallbacks of S at level M; an interval (f_i, f_{i+1}) is DIRTY if COARSE_M(Ξ)
  changes at some vertex inside it; D_M := #dirty intervals; REL_M := #exits of o leaving R at f_1, …, f_{N−1}; d_o := |succ(o)|.
- Claims signed (both referees "(Opus 5.5, D15)", L37):
  (a) Premise P-OPT: at an S4c fallback k, σ_k is the arena optimum against τ_k (S4a ran at k and returned σ_k); RESULTS R18 G-1OA-6
      concerns σ_{k+1}, not σ_k (both referees VALID, same reason).
  (b) Lemma FBW (every game): at an S4c fallback k at which Even switches, every gate (y, z) has (i) ℓ ≤ max(δ, −1); (ii) if
      ℓ = −1 > δ, y is its own W_k-cycle node and its own Ξ_k-cycle node.
  (c) Corollary FBW-S (𝒞^1O): at an in-phase S4c fallback k with (h) at k, every gate has level ≤ max(r_k, −1); so M_k ≤ −1 at EQ states
      and at THR states with u* = none. Theorem CLS2 (𝒞^1O): along a scope run the fallback levels are non-increasing and M_k ≤
      max(r_k, −1) at each; R29's OPEN item (H-EQ) is closed.
  (d) Lemma FLAT-ALL (𝒞^1O): at a fallback k of a scope run with M := M_k ≥ 0 and (h) at k and k+1: (i) F_k ⊆ F_{k+1}, and every v ∈
      R̄_{k+1} lies in R̄_k with the same route to o; (ii) COARSE_M(θ_{k+1}) = COARSE_M(θ_k); (iii) COARSE_M(Ξ_{k+1} v) = COARSE_M(Ξ_k v)
      for every v; (iv) M_{k+1} ≤ M. In (i), a switched cycle node's new cycle avoids o by H1 at k+1, not by "o's W-cycle / H2"
      (FBW-1, citation, closed).
  (e) Lemma STRETCH (𝒞^1O): if COARSE_M(Ξ_t v) is constant in t ∈ [s, e] for every v (M ≥ 0), each Even y is a level-M tail at most
      once among the fallbacks k of the scope run with s ≤ k ≤ e (packet: "k < e"; the proof covers k = e: FBW-2 = N-FBW-1, wording,
      closed).
  (f) Theorem PL (𝒞^1O): for a block of a scope run S at level M ≥ 0, (a) N ≤ n_E(1 + D_M); (b) the first COARSE_M(Ξ)-change j of a
      dirty interval is an S4a ε-transition with O_j > M ≥ E_j, lev(θ_j, θ_{j+1}) = O_j > M, and an absorption; (c) if r_t > M on
      [f_1, f_N], D_M ≤ (d_o − 1) + REL_M, so N ≤ n_E(d_o + REL_M). Corollary PL-S: if every block of S has r > M on it, the
      fallbacks of S at levels ≥ 0 number at most n_E·Σ_M (d_o + REL_M) ≤ n_E(n·d_o + REL(S)), REL(S) := #exit releases at fallbacks
      of S. Levels never reset along a scope run (compare R25 (d) Theorem FB, which resets at every non-tame transition).
- Not signed (packet §6, not to sign): CONJECTURE NJB (no COARSE_M change strictly inside a level-M block; gives ≤ n_E fallbacks per
  level) and NJ-INT; Lemma ABS-O (true, vacuous); OPEN: blocks on which r drops to M, fallbacks at level −1, REL(S).
- Honest limits: (i) FBW holds on every game; the rest is on 𝒞^1O. (ii) PL bounds fallbacks per block GIVEN D_M (and REL_M under
  r > M); NJB, REL and the r-drop blocks are OPEN here, so G-N5-TIME stays open. (iii) PL (b), (c) are vacuous in all data: D_M = 0 in
  every block for both referees, including REFEREE-2's climbs aimed at dirty intervals. (iv) Lane work after the pin (RDROP, PL (c′),
  MINSET, NO-RF-OLD, ENT-SHAPE; l-si bb8ed9e, dd5fa25, d7e0441, 8bb1134) is unrefereed and not part of this entry.
- Data (DATA, not proof; one Odd choice vertex asserted on every 𝒞^1O game): REFEREE fbw_probe.py (own trace = n5.run): named 65 /
  library 252 / climb bests 3 / random general 6,000 / random 𝒞^1O 4,000 games, 0 failures; Even fallbacks / gates 272 / 837 (named,
  equal to the packet), 798 / 2,618 (library); in-scope fallbacks library 596 THR u* ≠ none + 9 EQ, named 252 + 4; tails never repeat
  inside a constant-COARSE_M run (172 library + 75 named blocks, max block 37 = cl9_rep_b); climb bests re-run n5 29/27, 40/33, 45/37,
  Oink zlk OK strategies verified. REFEREE-2 fbw_check.py (own code): every arena single switch at every Even fallback fails to raise
  W(y) (44,611 library, 788 random, ~3.4 M in climbs); FBW (a) on 3,921 library + 409 random + 140,045 climb gates, tight (ℓ = δ ≥ 0) at
  69,184 climb gates, never exceeded; FLAT-ALL 956 library + 77,192 climb checks; STRETCH 1,328 library + 81,057 climb tail checks, 0
  repeats. Lead re-ran cl9_rep_b (8efbbc9e): n5 45/37, Oink OK, one Odd choice vertex.
- Signatures: REFEREE docs/referee/R-N5-FBW.md (referee 9a94dc7; §C a04615b): P-OPT VALID; FBW, FBW-S, CLS2, STRETCH, PL-S SIGNED;
  FLAT-ALL SIGNED WITH GAP FBW-1 (closed); PL SIGNED WITH GAP FBW-2 (closed). REFEREE-2 docs/referee-2/R2-N5-FBW.md (referee-2 2596285,
  successor 6; §C bc2e7b7, successor 7): P-OPT VALID; FBW, FBW-S, CLS2, STRETCH (N-FBW-1), PL, PL-S SIGN; FLAT-ALL SIGN, after §C SIGN WITH
  GAP FBW-1 (citation, closed; CONFIRMED: the cycle is y′'s honest H_{k+1}-cycle, which H2 does not exclude; H1 at k+1 does). §C: no
  verdict differs. Joint gap map (REFEREE §C, REFEREE-2 §C): FBW-2 = N-FBW-1 (wording, closed); FBW-1 (citation, closed; REFEREE's
  fixes line adopted by both).
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.

### R32 [refereed-only] N5 on one-Odd-choice games: a coarse freeze that survives θ-changes, w-changes and fallbacks (Theorem FREEZE, with Fact 0, ARENA, P^c_ℓ, RATCHET, BLOCK), polynomially many crossings per fallback-free run with an H1 SN prefix (Theorem X-RUN), and R20's subrun machinery with θ free (Theorem SUB) (2026-10-25) — partial step-4 lemmas for N5 (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C41.md, checker 1670d0d4)
- Object (packet P-N5-FRZ, added at l-new edbccb6, pinned trunk 25fda0f, unchanged during review): docs/new/P-N5-FRZ-box34.md, sha1
  39df373c17d91f942ad2cb15244cd779ca7abda1 (L-NEW successor 14, Opus 5.5). The referees' repairs are collected by the lanes in
  docs/new/P-N5-FRZ-fixes-box34.md (l-new 1dc42ba, sha1 168de464adab5c56945bc5587f4f0ad3262a1fcd, L-NEW successor 14: FRZ-1..FRZ-3) and
  docs/new/P-N5-FRZ-fixes2-box34.md (l-new 5f02ceb, sha1 ed2ca80df2fcd57bf35160d0e1ad926a29e5bb60, L-NEW successor 15: REFEREE-2's rows
  mapped to FRZ-1..3; N-FRZ-1's two-prefix fact C7′; N-FRZ-4 definitions; NL phase-key line); both on trunk; repairs only.
  Setting as in RESULTS R25 and R27-R31 (COARSE_L, (C1)-(C7), lev with ⊥ < −1 < 0 < …; Ξ, W, λ; on 𝒞^1O inside a PHASE (λ_Ξ and τ
  constant): R, R̄, F, θ, w, c_θ, c_w, H1-H3, (h), r_k := lev(θ_k, w_k), SN prefix (R30 (c))). A WINDOW at ℓ < ∞ is a run of consecutive
  states of a phase, all with (h) and r ≤ ℓ (fallbacks allowed). A (w, r)-SUBRUN is a maximal run of consecutive (h) states of a phase
  with w and r constant (θ may change; fallbacks allowed).
- Claims signed (both referees "(Opus 5.5, D15)", L37):
  (a) Corollary NL-MF: at an in-phase S4a step j with (h), if r_j > MF_j (the maximal level of a gate into F_j, ⊥ if none), then R_j ⊆
      R̄_{j+1} and MF_{j+1} ≤ MF_j (R29 NL; NL is signed on the key (λ_Ξ, λ_U, τ), and its proof uses no λ_U, so it applies on the
      (λ_Ξ, τ) phase: REFEREE §1, accepted by REFEREE-2 §C).
  (b) Fact 0: at an (h) state of a phase every vertex's W-cycle node is λ(v), and λ(v) = c_θ ∈ F for v ∈ R̄. Lemma ARENA: at an S4a step
      from an (h) state the arena contains every W-improving edge of G_τ except possibly F → R̄ non-gates (WITHHELD), each of level ≤ r_k.
      (The R → R̄ case uses the two-prefix, one-base twin of (C7), not (C7): N-FRZ-1, citation, closed; fixes2 Fact C7′.)
  (c) Lemma P^c_ℓ (R20's Lemma P^c with COARSE_ℓ, statewise Lemma C_ℓ and coarse monotonicity along a window, fallbacks included):
      Ω^c_{k0+j}(x) ⪰ COARSE_ℓ(value(ρ)) for every simple path ρ of G_τ of length ≤ j from x to an honest cycle node. Gaps FRZ-1 = N-FRZ-2
      (case (γ) of B1, the inherited XA-3; wording) and FRZ-2 = N-FRZ-3 (B-fallback B1 at an own cycle node x = λ(x); wording), both
      closed by fixes 168de464.
  (d) Theorem FREEZE: if a window at ℓ has n states ending at F, then for every state t ≥ F of the phase that has some H2 state t2 ≥ t
      in the phase, COARSE_ℓ(Ξ_t) = COARSE_ℓ(Ξ_F) everywhere, and at H2 states t also COARSE_ℓ(W_t) = COARSE_ℓ(Ξ_F); θ, w, R may change
      and fallbacks may occur after F. Corollary RATCHET: at every H2 state t ≥ F, COARSE_ℓ(θ_t) = COARSE_ℓ(w_t) (so H1 there gives (h));
      for ℓ ≥ 0, COARSE_{ℓ−1}(θ) takes ≤ 2d_o values over those states with H1, COARSE_{ℓ−1}(w) changes ≤ once, and they split into
      ≤ 2d_o + 1 runs with constant pair. Lemma BLOCK: on consecutive (h) states t ≥ F with a constant differing pair (r = ℓ), a vertex
      leaving R at an S4a step inside the run does not re-enter R in the run.
  (e) Theorem X-RUN: in a fallback-free run Q of a phase whose SN prefix P has H1 throughout, crossings with both ends in P number
      ≤ 13(d_o + 1)n³; REL_Q ≤ 13 d_o(d_o + 1)n³; ε_H1(Q) ≤ d_o + REL_Q (R30 ABS-COUNT′); Q has ≤ 13(d_o + 1)n³ + n crossings. The
      transition leaving P can release exits and is not covered by R-STICK; REL_Q ≤ d_o(C_P + 1) with C_P + 1 ≤ 13(d_o + 1)n³ (FRZ-3 =
      G-FRZ-1, accounting, closed by fixes 168de464; the stated bounds stand).
  (f) Theorem SUB: on a (w, r)-subrun with r = ρ ≥ 0, R20's Lemma C, Lemma CR and Theorem XA hold with COARSE_ρ (θ free).
- Not signed (packet §8, not to sign): FBF on (w, r)-subruns FALSE (b6_xl2_n32; 1,442 entries after fallbacks); CL1 ("one fallback
  cluster per level per scope run") FALSE (x48_rt48_final, 9 clusters); OPEN (L1), (L2), ¬H1 SN states, f per phase.
- Honest limits: (i) SUBCLASS 𝒞^1O, inside a phase. (ii) X-RUN bounds crossings per fallback-free run GIVEN H1 on the SN prefix; f per
  phase, (L1) and (L2) are OPEN here, so G-N5-TIME stays open. (iii) DATA is thin: random games never give an n-state (h) window, so
  FREEZE, RATCHET, BLOCK and SUB (iii) rest on library and climb instances; BLOCK is VACUOUS in both referees' data (0 S4a leaves at an
  (h) state after any freeze); no freeze at ℓ = −1 or ⊥ occurs anywhere, so X-RUN's segment −1 and post-F(⊥) parts are proof-only; the
  transition leaving P never carried a leave in any data (FRZ-3 is a proof gap only). (iv) Lane work after the pin (P-N5-L2, P-N5-TOG,
  CN-LAST, PF-THETA) is not part of this entry.
- Data (DATA, not proof; one Odd choice vertex asserted on every game): REFEREE frz_probe.py (own trace = n5.run, phase key (λ_Ξ, τ)):
  library 252 files, random 𝒞^1O 4,000 + 3,000 games, 0 failures (NL-MF 1,978; Fact 0 5,320 library + 8,476 random; ARENA withheld
  edges 41,479, every one F → R̄ and not a gate; Step 1 54,191 library + 48,714 random window states; FREEZE 142 windows / 2,958
  later-state checks; BLOCK 30 runs; X-RUN 472 library runs, max 55 crossings in P, max REL_Q 12; SUB 357 subruns); random games give 0
  freeze windows. REFEREE-2 frz_check.py (own N5 accepting any S4a arena optimum; agrees with Oink zlk on 468 / 468 library runs): 16,434
  batch runs + 12 climbs (1,485,828 runs), 0 violations (FREEZE 302 library freezes, 5,502 later states; P^c_ℓ 3,386 windows, 927,530
  sampled path comparisons; BLOCK 60 library blocks + 3,610 in the 12 climbs (three aimed at leaves), 0 S4a leaves); with windows of n/2 states FREEZE
  fails on x32_sc32_final (96 violations), and FREEZE's later-H2 hypothesis is used (x31_rx48). REFEREE re-ran b6_xl2_n32 and
  x48_rt48_final (n5, Oink OK).
- Signatures: REFEREE docs/referee/R-N5-FRZ.md (referee 3a520ce, successor 6; Addendum 3171efc on fixes 168de464; §C 1f13a6f + C.6 9ad6bfb, successor 7):
  NL-MF, Fact 0, ARENA, Steps 1-2, FREEZE, RATCHET, BLOCK, SUB SIGNED; P^c_ℓ SIGNED WITH GAPS FRZ-1, FRZ-2 (closed); X-RUN SIGNED WITH
  GAP FRZ-3 (closed); §C accepts N-FRZ-1 (missed by REFEREE) and N-FRZ-4; C.6: 0 S4a leaves at any (h) state after a freeze at ℓ ≥ 0 (library 261 files, 2,410 (window, ℓ) transition checks). REFEREE-2 docs/referee-2/R2-N5-FRZ.md (referee-2 20a73ca; §C
  f546b43; successor 7): NL-MF, Fact 0, ARENA (N-FRZ-1), P^c_ℓ (N-FRZ-2, N-FRZ-3; label aligned to REFEREE's in §C), FREEZE, RATCHET,
  BLOCK, SUB SIGN; X-RUN SIGN WITH GAPS G-FRZ-1 (closed). §C: no verdict differs. Joint gap map (REFEREE §C, REFEREE-2 §C), 6 rows: FRZ-1
  = N-FRZ-2 (wording, closed); FRZ-2 = N-FRZ-3 (wording, closed); FRZ-3 = G-FRZ-1 (accounting, closed); N-FRZ-1 (citation, closed;
  REFEREE-2 only); N-FRZ-4 (wording: d_o, crossing, leave defined in fixes2; REFEREE-2 only); NL phase key (REFEREE only; accepted).
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.

### R33 [refereed-only] N5 on one-Odd-choice games: how (h)-runs end and restart (H3-CONST, H2-STICK), the frames at H3 states without H1 (Lemma G′), the freeze through ¬H1 states (FREEZE′), R̄ constant at ¬H1 states (R-CONST), the single empty-path interval (H1-INT), and crossings per fallback-free run without an H1 hypothesis (Theorem X-RUN′) (2026-10-25) — partial step-4 lemmas for N5 (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C42.md, checker 639ff523)
- Object (packet P-N5-L2, added at l-new 1afccb5, pinned trunk 04b3f48, unchanged during review): docs/new/P-N5-L2-box34.md, sha1
  cbea07392521bcdfbce137ba361bb581f9df11d7 (L-NEW successor 14, Opus 5.5). The referees' repairs are collected by the lane in
  docs/new/P-N5-L2-fixes-box34.md (l-new 97c3b4e, sha1 7a110bca8d52b532d531c0836547b2d22b7437cd, L-NEW successor 15: L2-1, L2-2) and
  docs/new/P-N5-L2-fixes2-box34.md (l-new ea78e9b, sha1 e343d74e1502e7c75ca5c40fd79350a3b8662b26, L-NEW successor 15: N-L2-1 = L2-1;
  N-L2-2 as Lemma X-RUN°: any set of consecutive (h) states of one fallback-free run has ≤ 13(d_o+1)n³ crossing transitions with both
  ends in it); both on trunk; repairs only.
  Setting as in RESULTS R30-R32 (𝒞^1O; phase with λ_Ξ and τ constant; R, R̄, F, θ, w, c_θ, c_w, H1-H3, (h), r, SN prefix, windows,
  FREEZE, X-RUN). U := λ^{-1}(c_θ) (a phase constant). An H1-TOGGLE is a transition at which H1 changes.
- Claims signed (both referees "(Opus 5.5, D15)", L37):
  (a) Lemma H3-CONST: in a phase, at every H2 state c_w = λ(τ(o)); so H3 holds at all H2 states of the phase or at none, and if the
      phase has an (h) state, then (h) ⟺ H1 ∧ H2 at every state of the phase.
  (b) Lemma H2-STICK: at an S4a transition s → s+1 of a phase with H1 and ¬H2 at s, ¬H2 holds at s+1 (the case τ(o) = o, where
      "τ(o) ∈ R_s" is false since R excludes o, is trivial: L2-1 = N-L2-1, wording, closed).
  (c) Lemma G′: at a phase state with H3 and ¬H1 (c := c_θ = c_w): ¬H2 holds and c ∈ R̄; a vertex of R̄ whose (σ, τ)-play visits c
      before o has Ξ = W; any other has Ξ = π_v ⊕ θ and W = π_v ⊕ w, with π_v disjoint from P(θ), P(w) and c.
  (d) Theorem FREEZE′ (premise RESULTS R32 FREEZE, with FRZ-1, FRZ-2): FREEZE holds with "(h)" replaced by "H3" in the window and "H2"
      replaced by "H2 or H3" in the conclusion (b) and in the range of t.
  (e) Lemma R-CONST: at every ¬H1 state of a phase, R̄ = U; so no transition between two ¬H1 states of a phase is a crossing.
  (f) Lemma H1-INT: in a phase, the states with P(θ) = ∅ form one interval I_∅; every ¬H1 state lies in I_∅, and so does every state k
      such that k → k+1 is a transition of the phase with H1 at k and ¬H1 at k+1 (the packet's reading with k+1 outside the phase is
      FALSE: docs/referee/R-N5-L2/exitdrop_n3.pg, sha1 73c7a21b…, n 3; L2-2, wording, closed); on I_∅, θ changes only in length,
      monotonically, at most n − 1 times.
  (g) Theorem X-RUN′ (premise RESULTS R32 X-RUN, with FRZ-3): for a fallback-free run Q of a phase with SN prefix P and t_Q H1-toggles
      with both ends in P, P has ≤ 13(d_o + 1)n³(t_Q + 1) + t_Q crossing transitions with both ends in P, and REL_Q ≤ d_o(C + 1) with C
      that number; no hypothesis on H1. X-RUN's proof uses only "consecutive (h) states of one fallback-free run" (N-L2-2, accepted by
      REFEREE; Lemma X-RUN° in fixes2).
- Refuted (§8, not signed; lane and referee instances, each re-run by the Lead: n5, Oink zlk OK strategies verified, one Odd choice
  vertex): CONJECTURE ONE-H ("the (h) states of a phase are consecutive") FALSE, experiments/new/box34/instances/oneh_cex_n32.pg (sha1
  51dab086…); CONJECTURE ONE-DROP ("≤ 1 H1 → ¬H1 transition per phase") FALSE, experiments/new/box34/instances/onedrop_cex_n32.pg
  (5793d5a3…, n5 6/1); CONJECTURE DROP-LEN ("θ changes between two drops of a phase") FALSE, docs/referee/R-N5-L2/droplen_cex_n12.pg
  (REFEREE; a6af26db…, n 12, n5 4/0, one phase, θ constant, drops at 1→2 and 3→4); its weaker form "≤ 1 drop per fallback-free run"
  FALSE, experiments/new/box35/instances/onerun_cex_n32.pg (L-NEW successor 15; 70832fcb…, n5 8/0). The open item "(h) restarted by a
  fallback at an H1 ∧ ¬H2 state that moves τ(o) out of R" OCCURS: experiments/new/box35/instances/fbrestart_cex_n12.pg (35223b6c…, n5
  5/2) and fbrestart_cex_n24.pg (a0aacfba…, 23/3) (L-NEW successor 15, SPEC trace); REFEREE-2 also saw it with its own N5 (j5_n16).
- Honest limits: (i) SUBCLASS 𝒞^1O, inside a phase. (ii) FREEZE′ and X-RUN′ rest on R32. (iii) X-RUN′ is per fallback-free run and
  in terms of t_Q; the H1-toggle count, f per phase, (L1) and fallbacks outside scope runs are OPEN here, so G-N5-TIME stays open.
  (iv) DATA is thin for FREEZE′'s new content: no n-state H3 window containing a ¬H1 state with a later state of its phase was found by
  either referee (REFEREE-2's climbs reached 668,549 such windows at n ≤ 10, all ending at the phase end; REFEREE's FIT=frz climbs (random starts and three library seeds)
  reached none). (v) Lane work after the pin (P-N5-TOG, CN-LAST, box 36) is not part of the claims; its box-35 instances appear only as
  DATA under Refuted.
- Data (DATA, not proof; one Odd choice vertex asserted on every game): REFEREE l2_probe.py and companions (own code): library 258
  files (319 phases, 7,155 states) and random 30,000 + 15,000 games, 0 failures of §1-§7; P^c_ℓ on windows containing ¬H1 states:
  library 491 windows / 2,097 checks, random 267,221 windows / 641,105 checks, 0 failures. REFEREE-2 (own code): 27,444 batch runs and
  6 climbs (2,416,844 runs), 0 violations; G′ frames checked per vertex at H3 ∧ ¬H1 states; P^c_ℓ on H3 windows with ¬H1 states about
  17 M path comparisons (11.3 M exhaustive).
- Signatures: REFEREE docs/referee/R-N5-L2.md (referee 7626354, successor 7; addenda 524d93f (climbs), d3ccb9c (fixes 7a110bca
  checked); §C ce24106 + 0363a7b): H3-CONST, G′, FREEZE′, R-CONST, X-RUN′ SIGNED; H2-STICK SIGNED WITH GAP L2-1; H1-INT SIGNED WITH GAP
  L2-2; both closed. REFEREE-2 docs/referee-2/R2-N5-L2.md (referee-2 388caf6, successor 7; §C 21429c9): H3-CONST, H2-STICK
  (N-L2-1), G′, FREEZE′, R-CONST, H1-INT, X-RUN′ (N-L2-2) SIGN; notes N-L2-1..3; in §C adopts REFEREE's labels and accepts L2-2 (missed).
  §C: no verdict differs. Joint gap map (REFEREE §C, REFEREE-2 §C), 4 rows: L2-1 = N-L2-1 (wording, closed); L2-2 (wording, closed;
  REFEREE only); N-L2-2 (X-RUN°, accepted); N-L2-3 (DATA thin, FREEZE′).
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.

### R34 [refereed-only] N5 on one-Odd-choice games: H1-toggles per phase are polynomial (L-MONO, Z-COUNT, Theorem TOGGLE, TOGGLE-COUNT), so crossings in SN prefixes per phase are polynomial in f (X-SN-PHASE) and (h)-runs per phase are at most 1 + T + f (RESTARTS) (2026-10-25) — partial step-4 lemmas for N5 (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C43.md, checker 36905e57)
- Object (packet P-N5-TOG, added at l-new 3e45aed, pinned trunk d3daae1, unchanged during review): docs/new/P-N5-TOG-box35.md, sha1
  7dfda8c88a0e9b752156f4faec726d8dccc20ccb (L-NEW successor 15, Opus 5.5). The referees' repairs are collected by the lanes in
  docs/new/P-N5-TOG-fixes-box35.md (l-new b5b8e66, sha1 f15b58dddf232d810fab277010e29ae5187d382d, L-NEW successor 15: G-TOG-1, N-TOG-1)
  and docs/new/P-N5-TOG-fixes2-box35.md (l-new e570bc6, sha1 698539a9e525c467a46ebd59b1785dc0be98c113, L-NEW successor 16: TOG-1 =
  G-TOG-1 and TOG-2 = N-TOG-1 with REFEREE's tighter record line; the DATA attribution of G-TOG-1; §7's DROP-LEN line out of date);
  both on trunk; repairs only.
  Setting as in RESULTS R30-R33 (𝒞^1O; phase with λ_Ξ and τ constant; c := λ(o), U := λ^{-1}(c); H1; next_k(v) := σ_k(v) for Even v,
  σ̄_k(v) for Odd v; (M) := RESULTS R15 (a)). An H1-TOGGLE is a transition inside a phase at which H1 changes; a DROP is one from H1 to ¬H1.
  Z_k := {(v, length of Ξ_k(v)) : v ∈ U, P(Ξ_k v) = ∅}.
- Claims signed (both referees "(Opus 5.5, D15)", L37):
  (a) Fact (F): if x lies on the cycle of c's H_k-play and λ_k(c) = c, then Ξ_k(x) = (c, ∅, dist_k(x → c)); if x ≠ c and λ_k(x) = c,
      then Ξ_k(x) = x ⊕ Ξ_k(next_k x). (Separately signed by REFEREE-2; used by REFEREE in its setting.)
  (b) Lemma L-MONO: for c = λ(o) ≠ o in a phase, the length L_k of the cycle of c's H_k-play is non-increasing if Ω(c) is even and
      non-decreasing if Ω(c) is odd, strictly whenever σ(c) changes; so σ(c) changes at most n − 1 times per phase.
  (c) Lemma Z-COUNT: Z_k ≠ Z_{k+1} at no more than |U|(n + 1) transitions of a phase.
  (d) Theorem TOGGLE: at an H1-toggle k → k+1 inside a phase with c ≠ o, if Z_{k+1} = Z_k then next_{k+1}(c) ≠ next_k(c), so c ∈ V_E
      and σ(c) changes.
  (e) Corollary TOGGLE-COUNT: H1-toggles per phase ≤ T := |U|(n + 1) + n − 1 ≤ n² + 2n − 1, and drops ≤ ⌈T/2⌉; no toggles when c = o.
  (f) Corollary X-SN-PHASE (premise RESULTS R33 X-RUN′, hence R32): X_SN per phase ≤ 13(d_o + 1)n³(f + 1 + T) + T, with no hypothesis
      on H1. X_SN also counts the S4a crossing from each run's last SN-prefix state out of the prefix, which X-RUN′ (a) does not; X-RUN°
      gives ≤ 13(d_o + 1)n³ − 1 crossings per H1 run, and the slack covers it, so the stated bound stands (TOG-1 = G-TOG-1, accounting,
      closed). The packet cites X-RUN′ as "P-N5-L2 §11"; it is §7 (TOG-2 = N-TOG-1, citation, closed).
  (g) Corollary RESTARTS (premises RESULTS R33 H2-STICK, H3-CONST and RESULTS R30 H3H2): a phase has at most 1 + T + f maximal (h)-runs;
      a restart is an H1-toggle or an Even S4c fallback.
- Not signed (packet §7): CONJECTURE DROP-LEN is listed there as open; it is FALSE (RESULTS R33, droplen_cex_n12), and so is its
  per-run form (onerun_cex_n32, RESULTS R33). OPEN: (L1), the f ↔ X loop, K.
- Honest limits: (i) SUBCLASS 𝒞^1O, inside a phase. (ii) X-SN-PHASE and RESTARTS are polynomial GIVEN f; f per phase, (L1) and the
  out-of-SN fallbacks are OPEN, so G-N5-TIME stays open. (iii) DATA is thin against the bounds: at most 6 toggles per phase in the
  library and 5 in climbs against T ≈ n²; max X_SN 91 per phase (library). (iv) TOG-1's boundary crossing occurs on the SPEC trace
  (REFEREE: 26 library files, one per file, e.g. experiments/n5-exhaustive/instances/b4_cyc6_0.pg 0→1, and 88 random; REFEREE-2 19 of
  its 239 files (the report text says 238); L-RED 26 files, e.g. experiments/red/so/instances/so_sor5_n24.pg 21→22); REFEREE-2's counts 310 batch / 246,038 climb
  come from its own N5 (another S4a optimum) only. (v) Lane work after the pin (box 36, P-N5-SCOPE) is not part of this entry.
- Data (DATA, not proof; one Odd choice vertex asserted on every game): REFEREE tog_probe.py, tog_climb.py (own trace = n5.run):
  library 272 files, random 30,000 + 15,000 games, 2 climbs (714 improvements re-checked), 0 failures; library toggles 29, random 329 +
  132, each with Z changed or σ(c) switched; c = o phases have no toggle. REFEREE-2 (own code): 31,434 batch runs (239 files and
  random) and 4 climbs (1.75 M runs), 0 violations; every toggle with Z unchanged changed next(c) at an Even c. Re-runs of
  onerun_cex_n32 (8/0), fbrestart_cex_n12 (5/2), fbrestart_cex_n24 (23/3) agree (REFEREE, REFEREE-2, Lead); Lead re-ran b4_cyc6_0 (2/0)
  and so_sor5_n24 (23/0), Oink zlk OK strategies verified, one Odd choice vertex.
- Signatures: REFEREE docs/referee/R-N5-TOG.md (referee fff6e62, successor 7; §C 49dc13b): L-MONO, Z-COUNT, TOGGLE, TOGGLE-COUNT,
  RESTARTS SIGNED; X-SN-PHASE SIGNED WITH GAPS TOG-1, TOG-2 (closed). REFEREE-2 docs/referee-2/R2-N5-TOG.md (referee-2 faabe71, successor
  7; Addendum A 16d27d1; §C 8681e3f): (F), L-MONO, Z-COUNT, TOGGLE, TOGGLE-COUNT, RESTARTS SIGN; X-SN-PHASE SIGN WITH GAPS G-TOG-1;
  note N-TOG-1. §C: no verdict differs. Joint gap map (REFEREE §C, REFEREE-2 §C), 2 rows: TOG-1 = G-TOG-1 (accounting, closed); TOG-2 =
  N-TOG-1 (citation, closed).
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.

### R35 [refereed-only] N5 on one-Odd-choice games: the per-level fallback count holds for every block (RDROP, PL (c′), PL-S′), the minimum free-exit set governs θ above a block level (MINSET, survivor form), only entrant tails can be evicted after a rise (NO-RF-OLD), and the shape a violation of the per-level conjecture must take (ENT-SHAPE (1)-(4), (5′)) (2026-10-25) — partial step-4 lemmas for N5 (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C44.md, checker 1555d239)
- Object (packet P-N5-NJB, added at l-si 5c949ec, pinned trunk a7d85b3, unchanged during review): docs/si/P-N5-NJB-box9.md, sha1
  f43a8823b3b50399dacb387697bdb433373ea671 (L-SI successor 4, Opus 5.5). The referees' repairs are collected by the lane in
  docs/si/P-N5-NJB-fixes-box9.md (l-si 32c2393, sha1 6a3377482739a9dd5fdfcddc82314c9304ff94ec, L-SI successor 5: NJB-1, NJB-2, NJB-L1)
  and docs/si/P-N5-NJB-fixes2-box9.md (l-si 90b5fb3, sha1 647386fb8f77cf9a7909bb4d0beed517e4b50e83, L-SI successor 5: G-NJB-1, which
  supersedes part 1's (b), (c) texts; N-NJB-1 withdrawn; (5′) with both branches; concordance); both on trunk; repairs only.
  Setting as in RESULTS R29 and R31 (scope runs, r, M_k, COARSE_L, (C1)-(C7), gates, b_k(y), THR / EQ, FBL, OFFGATE, NL, CLS1, FBW-S,
  CLS2, FLAT-ALL, STRETCH, PL (a)-(b)) on 𝒞^1O. A BLOCK of a scope run at level M ≥ 0 is its set of fallbacks f_1 < … < f_N at level M;
  an INTERVAL is (f_i, f_{i+1}); it is DIRTY if COARSE_M(Ξ) changes inside it; D_M := #dirty intervals; REL_M, REL(S) as in R31. For t in
  an interval with r > M: Mn_t := {exits x ∈ F_t : COARSE_M(o ⊕ Ξ_t x) = COARSE_M(θ_t)}.
- Claims signed (both referees "(Opus 5.5, D15)", L37):
  (a) Lemma RDROP: the first COARSE_M(Ξ)-change j of a dirty interval of a level-M block has r_j > M. Theorem PL (c′): for every level-M
      block of a scope run (M ≥ 0), D_M ≤ (d_o − 1) + REL_M, so N ≤ n_E(d_o + REL_M), with no hypothesis on r. Corollary PL-S′: for
      every scope run S, the fallbacks of S at levels ≥ 0 number at most n_E(n·d_o + REL(S)) (R31's PL-S without its hypothesis).
  (b) Lemma MINSET (a), (b), (d) and survivor (c): (a) COARSE_M(θ_t) is the minimum of COARSE_M(o ⊕ Ξ_t x) over the exits x ∈ F_t,
      attained at σ̄_t(o); (b) a member of Mn_t that stays in F stays in Mn_{t+1} with the same COARSE_M value, and members leave Mn
      only by entering R; (c) COARSE_M(θ) changes at t → t+1 exactly when no member of Mn_t lies in F_{t+1}, and then every member of
      Mn_t entered R at t; (d) at a fallback of the block Mn can only gain members. The packet's literal (c) ("exactly when
      Mn_{t+1} = ∅") is NJB itself, since Mn_{t+1} ∋ σ̄_{t+1}(o) by (a); it is NOT signed (G-NJB-1, statement; joint with NJB-1,
      "absorbed" read as "entered R", wording; fixes2).
  (c) Lemma NO-RF-OLD: for a fallback k0 of a scope run S with L := M_{k0}, t* ≤ the next fallback of S, r > L on [k0+1, t*], and an S4a
      step j ∈ (k0, t*) with COARSE_L(θ_{j+1}) ≠ COARSE_L(θ_j), no gate (y, z) at t ∈ [j+1, t*] has y ∈ R_j ∩ R_t and z ∈ F_t.
      Corollary: if t* = k is the next fallback with M_k ≥ 0, every non-flat switched edge at k is R → F with an entrant tail
      y ∈ R_k ∖ R_j.
  (d) Lemma ENT-SHAPE (1)-(4), (5′): with M_k = L ≥ 0 and a level-L gate (y, z) at k, y ∈ R_k, z ∈ F_k: (1) y is an entrant and
      COARSE_L(b_t y) is constant on [k0, k]; (2) y's rank-L bit is bad on [k0, k]; (3) y was not a level-L tail at k0; (4) z has frozen
      COARSE_L and its rank-L bit goes from bad at k0 to good at k; (5′) z's honest value rises at level exactly L at some transition s ∈ [k0, k). Either s = k0 and z ∈ R_{k0} ∩ F_{k0+1} (z
      leaves R at the fallback), or s is an S4a step in (k0, k) with z ∈ F_s ∩ F_{s+1}. In the second case U-loc and (A_s) leave only Even
      switches of level ≤ L on z's F-play, so the rise needs a switch of level exactly L on that play. The packet's (5) (the flip at an S4a step in (k0, k) with z ∈ F) is NOT SIGNED: z ∈ R_{k0} may be evicted at the
      fallback k0 with the flip at k0 → k0+1 (NJB-2; hand-checked by REFEREE on experiments/si/orlens/instances/cycelim_cex_n32.pg,
      fallback 15, L = 31, z = 7; the local configuration occurs 569 named / 1,159 library times in REFEREE's data and 278 times in
      REFEREE-2's own N5, e.g. b6_xl2_n32 fallback 18, level 31, y = 3, z = 23). REFEREE-2's N-NJB-1 (the fallback is excluded) assumed
      z ∈ F_{k0} and is withdrawn; it proves that branch of (5′).
- Not signed (packet §5): CONJECTURE NJB (no COARSE_M change strictly inside a level-M block; gives ≤ n_E fallbacks per level) and
  CONJECTURE ENT (no entrant tail at the next fallback after a rise above L); the obstruction, with §5 (iii) split into (iii-a) an F → F
  level-L switch in (k0, k) and (iii-b) z ∈ R_{k0} evicted at k0 (fixes 6a337748).
- Honest limits: (i) SUBCLASS 𝒞^1O. (ii) PL (c′) and PL-S′ bound fallbacks of level ≥ 0 per scope run GIVEN REL; NJB / ENT, REL(S),
  level −1 fallbacks and the out-of-scope fallbacks are OPEN, so G-N5-TIME stays open. (iii) DATA is vacuous for the substance of
  RDROP and PL (c′) (D_M = 0 in every block for both referees, including dirty-aimed and Mn-aimed climbs) and for NO-RF-OLD's Corollary
  and ENT-SHAPE (0 fallbacks after a rise in both referees' data and climbs). (iv) Lane work after the pin (docs/si/N5-RL-box10.md:
  BL, FREE-FREEZE, EV, EV+, TEV-RED, conditional on (P); CONJECTURE TEV; L-RED's CONJECTURE RISE-LAST) is not part of this entry.
- Data (DATA, not proof; one Odd choice vertex asserted on every game): REFEREE njb_probe.py (own code): named 72 files, library 261
  files, 6,000 random games, 0 failures; D_M = 0 in every block; Mn never emptied; random games produce no level ≥ 0 block; Oink re-runs
  of experiments/si/coarse/instances/box9/cl9_mn_a, cl9_mn_b, cl9_norf_a, cl9_norf_b agree (n5 39/15, 41/35, 35/2, 32/2). REFEREE-2
  (own code): 15,446 batch runs (241 library + named files and random) and 8 climbs (1.77 M runs), 0 violations; 32,871 Mn members
  entered R in climbs, Mn never emptied; 6,687 rises in climbs, none followed by a fallback. Lead re-ran cl9_mn_a and cl9_mn_b (Oink
  zlk OK strategies verified, one Odd choice vertex).
- Signatures: REFEREE docs/referee/R-N5-NJB.md (referee 524d93f, successor 7; §C 5e85c70 + 0363a7b; C.7 49dc13b): RDROP, PL (c′),
  PL-S′, NO-RF-OLD + Corollary, ENT-SHAPE (1)-(4) SIGNED; MINSET SIGNED WITH GAP NJB-1; ENT-SHAPE (5) NOT SIGNED as stated, (5′)
  SIGNED (NJB-2); in §C accepts G-NJB-1 (missed): literal MINSET (c) NOT SIGNED, survivor (c) SIGNED. REFEREE-2
  docs/referee-2/R2-N5-NJB.md (referee-2 45eae59, successor 7; §C 21429c9 + e65cbcd; §C.3a 16d27d1): RDROP, PL (c′), PL-S′, MINSET (a),
  (b), (d), NO-RF-OLD + Corollary, ENT-SHAPE (1)-(4) SIGN; MINSET (c) SIGN WITH GAPS G-NJB-1 (survivor form); in §C withdraws N-NJB-1 and accepts NJB-1,
  NJB-2: ENT-SHAPE (5) NOT SIGNED, (5′) SIGN. §C: no verdict differs after both §Cs. Joint gap map (REFEREE-2 §C.3, fixes2
  concordance): row 1 NJB-1 + G-NJB-1 (wording + statement, closed by the survivor line); row 2 NJB-2 ((5) not signed, (5′) signed by
  both; N-NJB-1 withdrawn).
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.

### R36 [refereed-only] The one-player premise (P) holds: in a one-player game a positional Even strategy with no improving edge is optimal (Lemma P1, via a set/multiset bridge, Lemma B), which discharges R18's G-1OA-4 (2026-10-25) — a lemma used by N5's analysis (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C45.md, checker 3667fb1c)
- Object (packet P-N5-P1, added at l-si 6ba9a69, pinned trunk 48a8a4c, unchanged during review): docs/si/P-N5-P1-box10.md, sha1
  b98ca7941264affe4bfe79cb72b744d2ab158e07 (L-SI successor 5, Opus 5.5). The referees' notes are collected by the lane in
  docs/si/P-N5-P1-fixes-box10.md (l-si d2701d8, sha1 83ef83b0e3a9c2df7c76d8d6f8096564db0618bf, L-SI successor 6: N-P1-1; REFEREE's §5
  correction) and docs/si/P-N5-RL-P1-addendum-box10.md §3 (l-si f5b39de, sha1 5c29d93d54f133edd4a8fb9e43c331067b8c6b2e: P1's joint
  state); on trunk; repairs only.
  Setting: SPEC S1 (VJ00 play values (c, P, ℓ) and Even's order ⊴, with lengths at cycle nodes), S2 (improving edge). A ONE-PLAYER game
  is a game in which every non-Even vertex has one successor. V_σ is the play valuation of a positional Even strategy σ.
- Claims signed (both referees "(Opus 5.5, D15)", L37):
  (a) Lemma B: the extended order on path MULTISETS (lexicographic on signed multiplicity vectors, then length by the parity of the
      cycle node) is a total order; on sets it coincides with SPEC S1's order; real play values are sets (the play is simple before its
      first visit of the cycle node). Multisets occur only inside chains whose two ends are real values.
  (b) Lemma M: prefixing x ⊕ · is strictly monotone in the extended order.
  (c) Lemma P1 (Steps 1-6): if σ is a positional Even strategy of a one-player game H with no improving edge (no Even edge (x, y) with
      V_σ(y) ▷ V_σ(σ(x))), then V_σ(v) ⊵ V_{σ′}(v) for every positional Even strategy σ′ and every vertex v. Corollary P1′: V_σ is then
      the pointwise maximum over positional Even strategies (R17 F1's W*). The trivial cases m = 0 in Step 4 and b = 0 in Step 6 are
      named in the fixes file (N-P1-1, wording, closed).
  (d) Hypothesis match: R18's premise (P) ("CONDITIONAL on (P) for one-player games (G-1OA-4, open by design): VJ00 Lemma 5.8 '1 ⇒ 2',
      used only in Lemma 1 on G[X]") and P-N5-RL §0's (P) are exactly the statement of Lemma P1 on the one-player games G[X], G_τ and
      G_τ[F_k]. So R18's condition G-1OA-4 is discharged.
- Reading (both referees, not signed as such): P1 discharges (P) for one-player games only. It does NOT discharge the two-player VJ00
  Lemma 5.8 (R15's G-N5T-3). For P-N5-RL (in review) it removes the (P) condition from BL (b), (c), (e), FREE-FREEZE, EV, EV+ and
  TEV-RED′; the packet's original TEV-RED stays NOT SIGNED as stated (RL-1 is independent of (P)); EQ-END keeps
  its CN-LAST condition (REFEREE §5 correction).
- Honest limits: (i) one-player games only. (ii) This entry discharges a premise of R18; it adds no bound on N5's running time.
- Data (DATA, not proof): REFEREE p1_probe.py (own engine): 8,000 random one-player games (n ≤ 13), every positional strategy
  enumerated, 9,083 improvement-free strategies, 0 violations of P1; control: 266,806 strategies with an improving edge are non-optimal;
  ~2.35 M order / Lemma B / M pairs, 0 failures. REFEREE-2 (own code): 28,973 one-player games, 1,030,157 strategies, 0 violations;
  Lemma B against SPEC S1 on 46,356,800 real-value pairs, 0 mismatches; mutation tests (a flipped odd rule; a coarse "improving" without
  lengths) fail as expected. Lane: p1check.py, 136,286 strategies, 0 violations.
- Signatures: REFEREE docs/referee/R-N5-P1.md (referee 58a5b73, successor 8; §C 5f52510): Lemma B (a)-(c), Lemma M, Lemma P1 (Steps 1-6)
  and Corollary P1′, §4 hypothesis match SIGNED; no gaps. REFEREE-2 docs/referee-2/R2-N5-P1.md (referee-2 e036e4c, successor 8; §C
  88571b0): Lemma B, Lemma M, Lemma P1, §4 SIGN; note N-P1-1. §C: no verdict differs.
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.

### R37 [refereed-only] N5 on one-Odd-choice games: blocked edges at a fallback (BL-FORM, BL), the confined optimum and the free freeze (CONF-MONO, FREE-FREEZE), the end of a scope run at θ = w (EQ-END), and where a violation of the per-level conjecture must live (EV, EV+, TEV-RED′) (2026-10-25) — partial step-4 lemmas for N5 (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C46.md, checker 2314af84)
- Object (packet P-N5-RL, added at l-si 01d69ac, pinned trunk 2fb698d, unchanged during review): docs/si/P-N5-RL-box10.md, sha1
  0a3c70cbf873b2e011a5a00be54d38926f7861f1 (L-SI successor 5, Opus 5.5). The referees' repairs are in docs/si/P-N5-RL-fixes-box10.md
  (l-si 1f107bf, sha1 ac0274586a3b715d8725bc5226e3b32572edf017, L-SI successor 6: RL-1 with Lemma CYC-EV and the replacement TEV-RED,
  RL-2, RL-3, RL-4; this file contains new proof text, signed by both referees in addenda) and docs/si/P-N5-RL-fixes2-box10.md (l-si
  d2701d8, sha1 b3e3cd93f21cb61e019cb975afa428292a75d983, L-SI successor 6: REFEREE-2's items and the concordance) and
  docs/si/P-N5-RL-P1-addendum-box10.md (l-si f5b39de, sha1 5c29d93d54f133edd4a8fb9e43c331067b8c6b2e, L-SI successor 6: the joint
  verdicts; it governs where it differs from the fixes files); all on trunk. By Lead ruling (12:58Z), the CYC-EV text in fixes
  ac027458 is not landed under this entry: CYC-EV is a to-sign item of P-N5-ENT (signed there by REFEREE, R-N5-ENT 55a3f6f).
  Setting as in RESULTS R31 and R35 (𝒞^1O; phase; (h); THR; scope run S; gates and gate levels; M_k; COARSE_L; R̄ / R / F; b_k(y)). G_τ
  is the one-player game "Odd fixed to τ" and G_τ[F] its restriction to a closed F; an Even edge is BLOCKED if it is W-improving and not
  a gate. THE ENT SETTING: S a scope run, k0 < k consecutive fallbacks of S with M_{k0} = M_k = L ≥ 0, r > L on [k0+1, k], and an S4a
  step in (k0, k) that changes COARSE_L(θ) (a RISE); Ev := F_{k0+1} ∖ F_{k0}; A, B := the parts of P(θ_{k0}), P(θ_k) in
  H := V_{>max(L, rank c)}. (P) := for one-player games, a positional Even strategy with no improving edge is optimal (R18's premise
  G-1OA-4; discharged by RESULTS R36).
- Claims signed (both referees "(Opus 5.5, D15)", L37); every "CONDITIONAL on (P)" item is unconditional given RESULTS R36:
  (a) Lemma R-SAME and Lemma BL-FORM: at a state with (h), the order of π ⊕ a against π′ ⊕ a (routes in R) is the same for a ∈ {θ, w};
      every blocked edge (v, u) has σ_k(v) ∈ F_k, u ∈ R̄_k, π_u ⊕ θ_k ⊴ Ξ_k(σ_k v) ◁ π_u ⊕ w_k, and Ξ_k(σ_k v) has cycle node c.
  (b) Lemma BL at an in-phase THR S4c fallback k with (h) (x0 := σ̄_k(o)): (a) σ_k is not optimal in G_τ; (d) x0 is nominally deficient,
      and so is every free exit x with o ⊕ Ξ_k(x) ◁ w_k; and, CONDITIONAL on (P): (b) some Even edge is blocked at k; (c) on F_k,
      W_k = Opt(G_τ[F_k]); (e) every optimal G_τ-play from x0 leaves F_k along an Even edge into R̄_k.
  (c) Lemma CONF-MONO: for closed F′ ⊆ F, Opt(G_τ[F′]) ⊴ Opt(G_τ[F]) on F′. Lemma FREE-FREEZE (CONDITIONAL on (P)): if k0 is an
      in-phase THR S4c fallback with (h), t > k0 a state of the same phase, z ∈ F_t and z's (σ_t, τ)-play lies in F_{k0}, then
      Ξ_t(z) = Ξ_{k0}(z) (the packet's "(h) at t" is not needed).
  (d) Corollary EQ-END (CONDITIONAL on CN-LAST, P-N5-SCOPE §6): if θ_t = w at a state t of a scope run S, every later state of S is EQ,
      and S has at most one S4c fallback after t, the last transition of its phase.
  (e) Lemma MERGE′ (packet: MERGE): for a window gate (y, z) of level −1 ≤ ℓ < ∞ at a state with (h), y's route has no vertex of
      H := V_{>max(ℓ, rank c)}, COARSE_ℓ(Ξ z) = COARSE_ℓ(π ⊕ θ), o ∉ H, and before their first common vertex the σ-plays of z and x0
      contain no vertex of H. The packet's range "ℓ ≥ −1" includes ∞, where it is FALSE: level-∞ window gates with disjoint plays exist,
      e.g. experiments/si/orlens/instances/inr2_n32.pg, state 0, gate (6, 29) (RL-2, both referees).
  (f) In the ENT setting, CONDITIONAL on (P): Proposition EV (the σ_k-play of the level-L gate target z meets Ev; with q its first Ev
      vertex, ρ the play before q and π_q q's route at k0: A ⊆ B and B ∖ A = (ρ ∪ π_q) ∩ H; the window gate exists by RESULTS R35's
      NO-RF-OLD Corollary, RL-4); Proposition EV+ (the σ_k-play of the new threat x_k := σ̄_k(o) also meets Ev).
  (g) Proposition TEV-RED′ (CONDITIONAL on (P)): for t ∈ (k0, k] after the rise with x_t's σ_t-play meeting Ev and NO Ev VERTEX ON
      THAT PLAY'S CYCLE (the added hypothesis, RL-1), with e the last Ev vertex on the play's prefix before its first visit of c, f := σ_t(e), u_e := σ_{k0}(e), B_t := P(θ_t) ∩ H: (1) e is Even, f's play lies in
      F_{k0}, Ξ_t(f) = Ξ_{k0}(f); (2) u_e's route at k0 has no vertex in H and COARSE_L(Ξ_{k0} u_e) = COARSE_L(θ_{k0}); (3) B_t = A ⊔ (the
      H-vertices of x_t's play up to and including e) (RL-3); (4) if u_e ∈ R̄_t, (e, u_e) is a gate of level > L at t; (5) at t = k,
      u_e ∈ Ev ∩ F_k. Consequence (CONDITIONAL on (P), RL-3 wording, WITH the added hypothesis at t = k): if the per-level conjecture fails
      in the ENT setting and no Ev vertex lies on the cycle of the threat's σ_k-play, then at k the threat's play passes an Even e with e and u_e both evicted at k0 and both free at k, e re-routed to a frozen f ∈ F_{k0} of class
      (c, A), and B ∖ A on the threat's play up to and including e.
- Not signed: the packet's TEV-RED as stated (RL-1 = G-RL-1: an Ev vertex may lie on the cycle of x_t's play, and the packet does not
  exclude it; RL-3 = G-RL-2: "before e" is false when e ∈ H, which occurs on experiments/red/so/instances/tevlast_cex_n40.pg at
  k0 = 3, t = 7, e = 15) and its Consequence as stated (without the hypothesis); packet §7: CONJECTURE TEV FALSE in both forms (tev_cex_n40, sha1 17078f78;
  tevlast_cex_n40, sha1 ff1e9cb4; L-RED successor 16; Lead re-run: one Odd choice vertex, n5 27/16 and 11/1, Oink zlk OK strategies
  verified), CONJECTURES RISE-LAST and NJB / ENT, BL-X FALSE (lane data).
- Honest limits: (i) SUBCLASS 𝒞^1O. (ii) EV, EV+, TEV-RED′ (4)-(5) and the Consequence are about the ENT setting, which occurs in NO data
  of either referee or the lane: they are vacuous in data and rest on their proofs. (iii) These results narrow where a violation of the per-level conjecture NJB must live;
  NJB itself and G-N5-TIME stay OPEN. (iv) Lane work after the pin (P-N5-ENT with CYC-EV, N5-STR-box11) is not part of this entry.
- Data (DATA, not proof; one Odd choice vertex asserted on every game): REFEREE own engine from the SPEC text: 309 library + named
  games, agreeing with Oink zlk on all; FREE-FREEZE 93,125 + 177,919 checks, BL 376 + 526 THR fallbacks, BL-FORM 74,710 blocked edges,
  R-SAME 944k pairs, 0 failures; the lane's climb bests rl_a / rl_b / rl_c reproduced (35/2, 33/2, 30/3); REFEREE-2 own N5: batch 566 logs / 45,680 runs and
  climbs 1,583,748 runs, 0 violations; 168 level-∞ window gates, all with disjoint plays.
- Signatures: REFEREE docs/referee/R-N5-RL.md (referee b7419da, successor 8; climbs 257c3d8; Addendum A1 3886384; §C 5f52510; Addendum
  A2 d104aac on the fixes; 6d480e7 records the Lead ruling: A2's CYC-EV rows superseded for this landing): BL-FORM + R-SAME, BL (a), (d), CONF-MONO SIGNED; BL (b), (c), (e), FREE-FREEZE, EV (RL-4), EV+ SIGNED
  CONDITIONAL ON (P); EQ-END SIGNED CONDITIONAL ON CN-LAST; MERGE SIGNED WITH GAP RL-2; TEV-RED NOT SIGNED as stated, TEV-RED′
  SIGNED CONDITIONAL ON (P) with RL-3; A2's checks of the RL-2..4 texts stand. REFEREE-2 docs/referee-2/R2-N5-RL.md (referee-2 30dc5f5, successor 8; §C 88571b0; Addendum A db9d66a on the fixes): R-SAME,
  BL-FORM, BL (a), (d), CONF-MONO SIGN; BL (b), (c), (e), FREE-FREEZE, EV (N-RL-2, N-RL-3), EV+ SIGN CONDITIONAL ON (P); EQ-END SIGN
  CONDITIONAL ON CN-LAST; in §C MERGE SIGN WITH GAP RL-2 (missed) and TEV-RED NOT SIGNED as stated, TEV-RED′ SIGN CONDITIONAL ON (P);
  (its Addendum A db9d66a also signs CYC-EV, which lands with P-N5-ENT). §C: no verdict differs after both §Cs.
  Joint gap map (both §Cs; fixes2 concordance): RL-1 = G-RL-1 (proof gap; closed by TEV-RED′'s added hypothesis); RL-2
  (with N-RL-1; MERGE range, closed); RL-3 = G-RL-2 (wording, closed); RL-4 (citation, closed); N-RL-2, N-RL-3 and the FREE-FREEZE
  "(h) at t" remark (wording).
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.

### R38 [refereed-only] N5: (λ_Ξ, τ)-phases are the joint λ-phases (KEY), w-changes between H2 states and scope runs per phase are polynomial in (T, f, X) (WCH, SCOPE-COUNT), fallbacks per crossing-free stretch and at ¬H1 states are polynomial (FB-INT, NH1-FB), and a fallback whose gates are all own-cycle-node length switches ends its phase (CN-LAST) (2026-10-25) — partial step-4 lemmas for N5 (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C47.md, checker e666fb56)
- Object (packet P-N5-SCOPE, added at l-new 8483279, pinned trunk 8998ee6, unchanged during review): docs/new/P-N5-SCOPE-box36.md, sha1
  c3f5ed3788f0853939d247dbcfb970334c9dcf7d (L-NEW successor 16, Opus 5.5). The referees' notes are collected by the lane in
  docs/new/P-N5-SCOPE-fixes-box36.md (l-new eb5477a, sha1 e25507556562d8d84f2c0038ba3d3f85b2b851a1, L-NEW successor 17: N-SC-1..4, O-1
  as a §7.2 note, REFEREE's §C lines); on trunk; repairs only.
  Setting as in RESULTS R28-R34 (phase; R, F; H1-H3, (h); crossings X; fallbacks f; H1-toggles; T := TOGGLE-COUNT's count, at most
  T* = |U|(n+1) + n − 1 (R34 (e)); scope runs; n_E := number of Even vertices). U_k = Ξ^d_{τ_k} is Odd's valuation and λ_U its cycle-node
  map.
- Claims signed (both referees "(Opus 5.5, D15)", L37):
  (a) Remark KEY (every game): λ_U is a function of τ alone, so on every run of states with τ constant it is constant; a (λ_Ξ, τ)-phase is
      exactly a joint λ-phase (λ_Ξ, λ_U, τ), and every result signed on joint λ-phases with τ constant holds verbatim on (λ_Ξ, τ)-phases.
  (b) Lemma WCH (𝒞^1O): at a transition k → k+1 of a phase with H2 at k and k+1 and w_k ≠ w_{k+1}, either it is a crossing or
      Ξ_k(t0) ≠ Ξ_{k+1}(t0) for t0 := τ(o); off crossings t0 ∈ F_k = F_{k+1} (N-SC-2, wording). Hence such transitions number at most
      (n − 2)(X + 1) + X per phase.
  (c) Corollary SCOPE-COUNT (𝒞^1O; premise RESULTS R34 (g) RESTARTS): the scope runs of a phase number at most
      #(h)-runs + #WCH ≤ (1 + T + f) + (n − 2)(X + 1) + X.
  (d) Lemma FB-INT (𝒞^1O): a maximal run of consecutive transitions of a phase, none of them a crossing, contains at most n_E(2n − 1)
      S4c fallback transitions (every non-tame transition of a phase is a crossing: the proof of RESULTS R28 (c) (ii); N-SC-3).
  (e) Corollary NH1-FB (𝒞^1O; premises RESULTS R33 (e) R-CONST and R34 (e) TOGGLE-COUNT): the S4c fallback transitions k → k+1 of a phase
      with ¬H1 at k number at most n_E(2n − 1)(⌈T/2⌉ + 1) + T ≤ poly(n), with no X term and no f term.
  (f) Lemma CN-LAST (every game): if k → k+1 is an S4c fallback at which Even switches (Iσ_k ≠ ∅), and every gate (y, z) ∈ Iσ_k has λ_k(y) = y and
      lev(Ξ_k(σ_k y), Ξ_k(z)) = −1, then Ξ_{k+1} = Ξ_k, Iσ_{k+1} = ∅, and k + 1 is the last state of its phase (the next iteration changes
      τ, or N5 stops).
- Not signed (packet §7): the out-of-SN fallbacks (fallbacks at H1 ∧ ¬H2 states and at H1 ∧ H2 ∧ ¬H3 states; OPEN), CONJECTURE OUT-POLY,
  the level −1 residue (oc12_s1), and the dead end "PF-THETA, linear form" FALSE (experiments/red/so/instances/pftheta_cex_n32.pg, sha1
  9f526135; 33 θ-changes > n = 32 after one fallback in one scope run; L-RED successor 15; Lead re-run: one Odd choice vertex, n5 38/1,
  Oink zlk OK strategies verified). Note O-1 (both referees): §7.2's out-of-SN count needs f_out ≤ n_E(2n − 1)(X_out + 1) + X_out, since
  evicting fallbacks are crossings and lie in no FB-INT stretch (experiments/new/box25/instances/wd16_s2.pg: every in-phase fallback a
  crossing; Lead re-run n5 19/14, Oink OK).
- Honest limits: (i) KEY and CN-LAST hold on every game; the rest is on 𝒞^1O. (ii) The bounds are polynomial GIVEN T, f, X; f per phase
  outside these classes (the out-of-SN fallbacks) is OPEN, so G-N5-TIME stays open. (iii) The bounds are far from reached in all data
  (at most 4 fallbacks per crossing-free stretch, 4 ¬H1 fallbacks per phase in REFEREE-2's climbs on its own N5; REFEREE's climbs: at
  most 1 per crossing-free run, no ¬H1 fallback). (iv) The packet's dependency status "IN LANDING"
  for P-N5-L2 was stale: RESULTS R33 landed before the packet (N-SC-1). (v) Lane work after the pin (P-N5-OUT, P-N5-NEB) is not part of
  this entry.
- Data (DATA, not proof; one Odd choice vertex asserted on every 𝒞^1O game): REFEREE scope_probe.py, scope_climb.py (own trace = n5.run):
  library 276 files (KEY 7,455; WCH 135; scope runs 225; non-tame 339; ¬H1 fallbacks 9; CN-LAST 23), random 𝒞^1O 30,000 games, general
  games 20,000 (KEY, CN-LAST), 2 climbs (766,585 candidates), 0 failures; CN-LAST 1,422 cases, in 1,420 N5 stops at k+1 and in 2 the next
  transition changes τ. REFEREE-2 (own N5, which takes another S4a optimum; own general N5 for CN-LAST): 849 logs / 86,517 runs and 8
  climbs (5,443,544 runs), 0 violations; Oink zlk agrees on 552 / 552 + 574 / 574 + 16 / 16 games.
- Signatures: REFEREE docs/referee/R-N5-SCOPE.md (referee fb6089b + 560ff4c, successor 7; §C 257c3d8, successor 8): KEY, WCH,
  SCOPE-COUNT, FB-INT, NH1-FB, CN-LAST SIGNED; no gaps. REFEREE-2 docs/referee-2/R2-N5-SCOPE.md (referee-2 6d6e4bc, successor 8, draft 1f8a9109, stamp 8655f692; §C
  fb6fa69): KEY, WCH (N-SC-2), SCOPE-COUNT, FB-INT (N-SC-3), NH1-FB (N-SC-4), CN-LAST SIGN; notes N-SC-1..4, observation O-1. §C: no
  verdict differs; the joint gap map is empty; REFEREE accepts N-SC-1..4 and O-1.
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.

### R39 [refereed-only] N5 on one-Odd-choice games: fallbacks at H1 ∧ ¬H2 states are evictions and θ-flat (SPLIT, F-FLAT), crossings and fallbacks per HN stretch are bounded by breaks (EPOCH), Ξ freezes on R̄ once no gate enters it (FREEZE-STEP, TAIL), and for τ(o) = o in case A no vertex enters R after a fallback while θ is constant (NO-ENTRY-A), so out-of-SN fallbacks per phase are polynomial in θ-changes (NE-COUNT); in case B every R → R̄ gate at a fallback is length-only (CASE-B-LEN) (2026-10-25) — partial step-4 lemmas for N5 (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C48.md, checker d22ddb69)
- Object (packet P-N5-OUT, added at l-new b1a43578, pinned trunk 719ce66, unchanged during review): docs/new/P-N5-OUT-box37.md, sha1
  9f032e616b515d703da4939cc1b0de89eb658aba (L-NEW successors 16 (proofs) and 17 (packet, filled-in steps), Opus 5.5). The referees'
  notes are collected by the lane in docs/new/P-N5-OUT-fixes-box37.md (l-new dd3f780b, sha1 640a5db215e7d5e2bcdc3b335ae5e4972fed1fb2,
  L-NEW successor 17: OUT-R1 = N-OUT-2, OUT-N1 = N-OUT-3, N-OUT-1, N-OUT-4); on trunk; repairs only.
  Setting as in RESULTS R21 and R38 (𝒞^1O; phase = (λ_Ξ, τ)-phase = joint λ-phase (R38 (a)); R_k, R̄_k, F_k, routes π_z; H1, H2; θ, w,
  c_θ; crossings, entries, evictions; Iσ_k; n_E; K := n_E(2n − 1)). An HN STATE has H1 ∧ ¬H2; an HN STRETCH is a maximal run of
  consecutive HN states of one phase. A BREAK of S is an entry preceded in S by an eviction with no entry in between; B, X_S, f_S are
  the numbers of breaks, crossings and fallback transitions of S. For τ(o) = o with an H1 state, CASE A: rank(o) > rank(c_θ); CASE B:
  rank(c_θ) > rank(o).
- Claims signed (both referees "(Opus 5.5, D15)", L37); no item uses (P):
  (a) Lemma SPLIT: at an in-phase transition with H1 ∧ ¬H2 at k, a non-fallback has R_k ⊆ R_{k+1} and an Even S4c fallback has
      R̄_{k+1} ⊆ R̄_k; so inside an HN stretch every crossing is an entry at an S4a step or an eviction at a fallback, never both.
  (b) Corollary EPOCH (corrected form): X_S ≤ 2(n − 1)(B + 1) and f_S ≤ K(X_S + 1) + X_S (premise FB-INT, RESULTS R38 (d)). The
      "+ X_S" is needed: an evicting fallback is a crossing and lies in no crossing-free run (REFEREE-2's O-1 on P-N5-SCOPE; both
      referees). The superseded successor-16 forms without it are NOT signed.
  (c) Lemma F-FLAT: at an in-phase Even S4c fallback with H1 ∧ ¬H2 at k, Ξ_{k+1} = Ξ_k on F_k and θ_{k+1} = θ_k; inside an HN stretch θ
      changes only at S4a steps.
  (d) Lemma FREEZE-STEP: at an in-phase transition with H1 ∧ ¬H2 at t, H1 at t+1, θ_{t+1} = θ_t and no gate (y, z) ∈ Iσ_t with
      z ∈ R̄_t: (i) R̄_{t+1} ⊆ R̄_t with routes unchanged; (ii) Ξ_{t+1} = Ξ_t on R̄_{t+1}; (iii) no gate into R̄_{t+1}. Corollary TAIL: from
      such a state to the end of the stretch or the first θ-change, nothing enters R, R̄ only shrinks and Ξ is frozen on R̄.
  (e) Theorem NO-ENTRY-A (τ(o) = o, case A): if an Even fallback a → a+1 is taken at a ∈ S and θ is constant on [a, b] ⊆ S, then the
      invariant INV(t) (no F → R̄ gate; every R → R̄ gate has lev < rank(o)) holds on [a, b], no transition of [a, b] is an entry, R̄ only
      shrinks, and Ξ_t(z) ≡ Ξ_a(z) for t ∈ [a, b] and z ∈ R̄_t (the same cycle node, and P agrees on vertices of rank ≥ rank(o)). The base cites FBL-N (i) (RESULTS R21 (c)) + F1 (RESULTS R17 (a)) in
      place of Step (K) (R23 (a), "inside a phase"), so b = a with a phase-exiting fallback is covered (OUT-R1 = N-OUT-2, citation).
  (f) Corollary NE-COUNT (τ(o) = o, case A; θ a parameter): (a) every break has a θ-change at an S4a step after its eviction and no
      later than its entry, so B ≤ θ_S; (b) X_S ≤ 2(n − 1)(θ_S + 1), f_S ≤ K(X_S + 1) + X_S; (c) over the phase, N_HN ≤ ⌊T_ph/2⌋ + 1 ≤
      ⌊T*/2⌋ + 1 (TOGGLE-COUNT, RESULTS R34 (e)), f_HN ≤ (K + 1)(2(n − 1)·θ_ph + (2n − 1)·N_HN) and X_HN ≤ 2(n − 1)(θ_ph + N_HN).
  (g) Lemma CASE-B-LEN (τ(o) = o, case B): at an HN state a where an Even fallback is taken, every R → R̄ gate (v, z) has
      lev(Ξ_a(σ_a v), Ξ_a(z)) = −1 and z's route longer than σ_a(v)'s (same citation repair as (e), N-OUT-2). Remark W-SIDE (same
      setting): if z's route avoids v (Case 1), the W-difference of the gate is W-unfavourable to z, or empty with Ω(o) even; if
      π_z = q · v · π_{σ_a v} (Case 2), the top t of q ∪ {v} has reward(t) ≤ reward(o); its "Consequence" paragraph is a
      READING and is not signed.
- Not signed (packet §7): CONJECTURE NO-ENTRY in general; CONJECTURE NO-ENTRY-B (τ(o) = o, case B) is FALSE
  (experiments/new/box38/instances/nebc_cex_n14.pg, sha1 399119af; the HN fallback 1 → 2 makes a length-only R → R̄ switch and S4a
  2 → 3 enters 4 with θ = (12, ∅, 2) constant; Lead re-run n5 9/5, Oink zlk OK strategies verified, one Odd choice vertex);
  CONJECTURE NO-ENTRY for τ(o) ≠ o is FALSE when c_w ≠ o, in both cases (experiments/new/box38/instances/tauw_A_cex_n24.pg, sha1
  e29908d5, n5 16/3; tauw_B_cex_n24.pg, sha1 c0ad4f0c, n5 10/4; Lead re-runs, Oink OK, one Odd choice vertex) (L-NEW successor 17,
  after the pin; N-OUT-4: REFEREE-2 reproduces a break with no θ-change between eviction and entry on all three; REFEREE's probe finds
  every signed check holding on them); the dead end
  ROUTE-FROZEN FALSE (experiments/new/box37/instances/rfroz_cex_n16.pg, sha1 a9b40395; Lead re-run); the OPEN core: θ-changes per HN
  stretch (θ_S, θ_ph), HN stretches per phase for τ(o) ≠ o, OTHER states (H1 ∧ H2 ∧ ¬H3). §7's reduction "given NO-ENTRY" is valid only
  in case A with c_w = o.
- Honest limits: (i) SUBCLASS 𝒞^1O, inside a phase. (ii) NE-COUNT is polynomial GIVEN θ_ph (and T_ph ≤ T*); θ_ph is OPEN, so the
  out-of-SN fallbacks per phase and G-N5-TIME stay open; NO-ENTRY-A covers τ(o) = o in case A only. (iii) FB-INT's per-run term is never
  used in data: every fallback with both ends in an HN stretch is a crossing (library 107 / 107 in the lane's count, 103 / 103 in
  REFEREE's); CASE-B-LEN's hypothesis occurs in the batches only on the counterexample nebc_cex_n14 (4 gates). (iv) N-OUT-1: the
  filled-in "target o" step of SPLIT (b) / F-FLAT is correct and redundant (landed FBL-N has o ∈ R). (v) Lane work after the pin
  (P-N5-NEB: NO-ENTRY-A′ for c_w = o, any τ(o); RISE; Theorem BRK; OUT-1) is not part of this entry.
- Data (DATA, not proof; one Odd choice vertex asserted on every game): REFEREE out_probe.py (own code on its rl_engine; logs
  rl_logs/out_lib37.txt, out_named.txt): lib37 270 𝒞^1O games plus 3 named, SPLIT 521 + 6 S4a / 105 + 22 fallbacks, F-FLAT 127,
  FREEZE-STEP 391 transitions, 121 HN stretches, NO-ENTRY-A 88 runs / 889 states, CASE-B-LEN 4 gates, 0 failures. REFEREE-2 (own
  checker; own / random / SPEC traces): 66,655 batch runs and 4 climbs (741,432 runs), 0 violations; CASE-B-LEN's hypothesis 4 gates in
  the batch and 1,291,962 in climbs, both W-SIDE cases; NO-ENTRY-A 2.35 M (a, b) pairs; mutation controls (drop "θ constant", case B
  read as case A, drop FREEZE-STEP's gate hypothesis) fail as expected; the lane's fbsplit numbers reproduced (115 HN stretches,
  107 / 107 crossing fallbacks, breaks 8 + 3); NE-COUNT (c)'s per-phase bounds (N_HN, f_HN, X_HN, T_ph ≤ T*) 0 violations (max f_HN 12
  on wd16_s2, max θ_ph 11; REFEREE checked (c) as arithmetic only). Lane: fbsplit.py library 115 stretches, 20,000 random games, 0 failures. Lead re-ran
  wd16_s2 (n5 19/14, Oink OK).
- Signatures: REFEREE docs/referee/R-N5-OUT.md (referee fa08687, successor 8; §C a8b8ef3): SPLIT, EPOCH, F-FLAT, FREEZE-STEP, TAIL,
  NO-ENTRY-A, NE-COUNT (a)-(c), CASE-B-LEN, W-SIDE SIGNED; notes OUT-R1, OUT-N1; no gaps. REFEREE-2 docs/referee-2/R2-N5-OUT.md
  (referee-2 dfcaae67, successor 9; §C 2a9e8db0): SPLIT, EPOCH (corrected), F-FLAT, FREEZE-STEP, TAIL, NO-ENTRY-A, NE-COUNT (a)-(c),
  CASE-B-LEN, W-SIDE SIGN; notes N-OUT-1..4; no gap. §C (both): verdicts identical; joint gap map empty; N-OUT-1..4 ACCEPTED
  (N-OUT-2 = OUT-R1, extended to CASE-B-LEN; N-OUT-3 = OUT-N1); REFEREE-2's §C checks the fixes file 640a5db2 item by item (all
  correct) and the c_w ≠ o qualification of N-OUT-4 on its own traces.
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.

### R40 [refereed-only] N5 on one-Odd-choice games: between consecutive fallbacks of a scope run with r above the fallback level, coarse values freeze and routes walk back (FZ, BF, RB, WALK), no evicted vertex lies on the threat's cycle and the threat's play avoids the evicted set after a rise (CYC-EV, TEV-FB), so the ENT setting is empty (ENT-X) and every level-M block has at most one dirty interval, giving at most 2·n·n_E fallbacks of level ≥ 0 per scope run (NJB-A, D1, PL-S″) (2026-10-25) — partial step-4 lemmas for N5 (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C49.md, checker cc26fd23)
- Object (packet P-N5-ENT, added at l-si 3126857, pinned trunk 765e893, unchanged during review): docs/si/P-N5-ENT-box11.md, sha1
  4fd22be79f7050a7f466288c76eea8bfe2f669d0 (L-SI successor 6, Opus 5.5). The referees' notes are collected by the lane in
  docs/si/P-N5-ENT-fixes-box11.md (l-si b6b8f85b, sha1 72d052b5bc24ef57752924d61ec1b46fd8fc6452, L-SI successor 7: joint verdicts,
  N-ENT-1..3, the R36 status line); on trunk; repairs only.
  Setting as in RESULTS R31, R35 and R37 (𝒞^1O; scope run S; fallbacks, gates, gate levels, M_k; COARSE_L, (C1)-(C7); b_k(y); θ, w, r;
  R̄ / R / F; (h); THR; blocks, intervals, D_M). SETTING (Σ): k0 < k are consecutive fallbacks of S, L := M_{k0} ≥ 0, and r_s > L for
  every s ∈ [k0+1, k]; c is the common cycle node of θ and w on S; H := V_{>max(L, rank c)}; Ev := F_{k0+1} ∖ F_{k0}; A := P(θ_{k0}) ∩ H,
  B := P(θ_k) ∩ H; a RISE is an S4a step in (k0, k) that changes COARSE_L(θ); the ENT setting is (Σ), a rise and M_k = L (R37 (f)).
  (P) := for one-player games, a positional Even strategy with no improving edge is optimal (R18's premise; RESULTS R36).
- Claims signed (both referees "(Opus 5.5, D15)", L37):
  (a) Facts (Σ1)-(Σ6) (from landed results): no fallback and τ constant in (k0, k); (h) and (A_s) on [k0, k]; no leave (F_k ⊆ F_s for
      s ∈ [k0+1, k], Ev ∩ F_k = R_{k0} ∩ F_k); M_k ≤ L (CLS2); c ∈ F_{k0} ∩ F_k; after a rise B ≠ A.
  (b) Lemma FZ: if v ∈ F_k, then v ∈ F_s for s ∈ [k0+1, k] and COARSE_L(Ξ_k v) = COARSE_L(Ξ_{k0} v). Lemma BF: if v is Even,
      v ∈ R_{k0} ∩ F_k and a := σ_{k0}(v), then COARSE_L(b_k v) = COARSE_L(Ξ_{k0} a), both with cycle node c.
  (c) Lemma RB: if moreover a ∈ R̄_k, then COARSE_L(Ξ_k a) = COARSE_L(Ξ_{k0} a). Corollary WALK (a)-(c): along the k0-route of
      v0 ∈ R_{k0} ∩ F_k, the first vertex a_j back in R̄_k has COARSE_L(Ξ_k a_j) = COARSE_L(Ξ_{k0} a_j); if the k0-route after v0 is low,
      then (π_{a_j}^k ∩ H) ⊔ B = A.
  (d) Lemma CYC-EV ((Σ) and a rise; M_k = L not assumed): no vertex of Ev ∩ F_k lies on C_k, the σ_k-cycle of c. This form implies the
      CYC-EV of docs/si/P-N5-RL-fixes-box10.md (fixes ac027458, signed in REFEREE A2 and REFEREE-2 Addendum A, not landed under RESULTS
      R37 by the Lead ruling of 12:58Z): its proof uses only M_k ≤ L (N-ENT-1, both referees).
  (e) Proposition TEV-FB ((Σ) and a rise): the σ_k-play of the threat x_k := σ̄_k(o) avoids Ev. (This is the dead CONJECTURE TEV at the
      single state t = k; at S4a states TEV is FALSE, RESULTS R37.)
  (f) Theorem ENT-X, signed CONDITIONAL on (P) by both referees: the ENT setting is empty; equivalently, if k0 < k are consecutive
      fallbacks of a scope run with M_{k0} = M_k = L ≥ 0 and r > L on [k0+1, k], then COARSE_L(θ) does not change in (k0, k). Proof: R37
      (f) EV+ against (e). Corollaries, signed CONDITIONAL on (P) by both: NJB-A (an interval of a level-M block, M ≥ 0, with r > M on
      [f_i + 1, f_{i+1}] is clean), D1 (every level-M block has D_M ≤ 1: only the straddling interval can be dirty), PL-S″ (every scope run
      has at most Σ_{M≥0} n_E(1 + D_M) ≤ 2·n·n_E fallbacks of level ≥ 0, without REL(S); compare R35 PL-S′). (P) enters only through
      EV+ ⇐ FREE-FREEZE ⇐ BL (c), i.e. (P) on G_τ[F_k]; REFEREE's §C records that RESULTS R36 (d) states P1 for exactly G[X], G_τ and
      G_τ[F_k], so given R36 (landed) ENT-X, NJB-A, D1 and PL-S″ hold without condition (as R37 records for EV, EV+, TEV-RED′). REFEREE-2's
      §C (C.1) records the same conclusion: with P1 landed, §4-§5 become unconditional; the check that R36 (d) names G_τ[F_k] is
      REFEREE's.
- Not signed (packet §6): CONJECTURE NJB in full (open only for the straddling interval, where r reaches M and NL and FZ are
  unavailable; straddling intervals occur 0 times in the data); TEV at S4a states (FALSE, RESULTS R37: tev_cex_n40, tevlast_cex_n40);
  the level −1 fallbacks per scope run (OPEN here; lane work after the pin, P-N5-LV pinned 601df6e and N5-LV4 / N5-LV5, in the referee
  queue).
- Honest limits: (i) SUBCLASS 𝒞^1O. (ii) PL-S″ bounds fallbacks of level ≥ 0 per scope run only; level −1 fallbacks, scope runs per
  phase beyond R38 SCOPE-COUNT, out-of-scope fallbacks, S4a steps and phases are OPEN, so G-N5-TIME stays open. (iii) The hypotheses of
  CYC-EV, TEV-FB and ENT-X ((Σ) with a rise) occur in NO data of either referee or the lane; they rest on their proofs. The packet's
  "vacuous everywhere" is too strong for the corollaries: NJB-A's hypothesis (an interval with r > M throughout) occurs, always clean
  (REFEREE-2 698 / 601 / 701 library (Σ)-pairs with M_k = L; REFEREE 654, all of its (Σ)-pairs) (N-ENT-2, both referees). (iv) The packet's §0 status of the
  RL report and of P-N5-P1 is stale: R36 and R37 have landed (N-ENT-3). (v) Lane work after the pin (N5-STR, N5-STR2: NL=, CONJECTURE)
  is not part of this entry.
- Data (DATA, not proof; one Odd choice vertex asserted on every game): REFEREE cyc_probe.py (own engine; logs rl_logs/cyc_*.txt):
  NAMED 262 + LIB 377 + tev_cex_n40 15 (Σ)-pairs (the tev_cex_n40 row is report text, no committed log;
  CHECKER's re-run and REFEREE-2's engine agree); FZ 17,116, BF 1,614, RB 938, WALK 1,669 checks; 0 failures (FZ, BF, RB, WALK,
  M_k ≤ L, Ev on C_k); 0 pairs with a rise; pair / RB / WALK counts equal the lane's. REFEREE-2 (own code; own / random / SPEC traces):
  66,655 batch runs and 4 climbs (62,036 runs, seeded with L-RED's TEV instances), 0 violations; (Σ)-pairs 756 / 660 / 760 library and
  134,200 in climbs, none with a rise; control: without a rise the threat's play meets Ev in 64 / 60 / 65 library pairs; after a rise
  following a fallback with r > L the scope run has no further fallback (62 library rises: r drops to ≤ L 38, N5 stops 13, the λ-phase
  ends 6, H2 fails 5; 26,665 in climbs). On tev_cex_n40 the two engines agree (15 pairs; FZ 414, BF 19, RB 16, WALK 19). Lane rb.py,
  straddle.py: 0 violations.
- Signatures: REFEREE docs/referee/R-N5-ENT.md (referee 55a3f6f, successor 8; §C d6b8aef): FZ, BF, RB, WALK, CYC-EV, TEV-FB SIGNED;
  ENT-X, NJB-A, D1, PL-S″ SIGNED CONDITIONAL ON (P); no gaps; in §C: R36 lifts the condition. REFEREE-2 docs/referee-2/R2-N5-ENT.md
  (referee-2 b7df84b, successor 9; §C f33884e): FZ, BF, RB, WALK (a)-(c), CYC-EV, TEV-FB and (Σ1)-(Σ6) SIGN; ENT-X, NJB-A, D1, PL-S″ SIGN
  CONDITIONAL ON (P); notes N-ENT-1..3; no gap. §C: verdicts identical; joint gap map empty; N-ENT-1..3 ACCEPTED (N-ENT-2 missed by
  REFEREE); one wording difference ("vacuous"), not a verdict.
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.

### R41 [refereed-only] N5 on one-Odd-choice games: in-scope THR fallbacks of level −1 have three gate shapes (LV-SHAPE), a fallback without an R → F gate ends its phase (LV-CN, LV-COUNT), and those with r ≥ 0 number at most n·n_E·(d_o + REL(S)) per scope run (FLAT-ALL_{−1}, STRETCH_{−1}, PL_{−1}, LV-PL) (2026-10-25) — partial step-4 lemmas for N5 (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C50.md, checker 3031cc69)
- Object (packet P-N5-LV, added at l-si b7f18fe, pinned trunk 601df6e, unchanged during review): docs/si/P-N5-LV-box11.md, sha1
  d0d797f084904f9ce4df641e90298cac53c61356 (L-SI successor 6, Opus 5.5), with its not-to-sign addendum docs/si/P-N5-LV-addendum-box11.md
  (l-si 84974fe, sha1 a15a8871024d33d1734a41cbeb9c2dd75ecdadef). The referees' notes are collected by the lane in
  docs/si/P-N5-LV-fixes-box11.md (l-si 6480a0f, sha1 b75ab1fc4b150e7836757c8719ddcd5c928e1ba7, L-SI successor 8: LV-N1, N-LV-1,
  LV-N2 = N-LV-2, LV-N3, N-LV-3, NL= FALSE); on trunk; repairs only.
  Setting as in RESULTS R31, R35, R37 and R38 (𝒞^1O; scope run S; fallbacks, gates, gate levels, M_k; COARSE_L for −1 ≤ L < ∞, (C1)-(C7);
  b_k(y); θ, w, r; R̄ / R / F; routes π; (h); THR; u*; c, the common cycle node of θ and w; x0 := σ̄_k(o)). SETTING (LV): k is an
  in-scope S4c fallback, THR at k, and M_k = −1 (so every gate at k has level −1). The LEVEL −1 BLOCK of S is the set of its fallbacks
  f_1 < … < f_N with M = −1 and r ≥ 0; D_{−1}, REL_{−1} as in R31 PL and R35 at level −1.
- Claims signed (both referees "(Opus 5.5, D15)", L37); no item uses (P) (the packet labels §1 "(no (P))"; for §2-§4 this holds by its §0 dependency list):
  (a) Proposition LV-SHAPE: in setting (LV), for a gate (y, z) with s := σ_k(y), exactly one of: (α) s, z ∈ F_k and y is its own Ξ- and
      W-cycle node; (γ) s ∈ F_k, z ∈ R̄_k, r_k = −1, y = c and P(W_k z) = ∅; (β) y ∈ R_k, z ∈ F_k, rank o < rank c,
      π^k_s ∩ V_{>c} = ∅ and P(Ξ_k z) = P(θ_k), and if r_k ≥ 0 also W_k(s) ▷ W_k(z) at level r_k. The case s, z ∈ R̄_k does not occur.
  (b) Corollary LV-CN: in setting (LV), if no gate at k is of kind (β), then Ξ_{k+1} = Ξ_k, Iσ_{k+1} = ∅ and k + 1 is the last state of
      its phase. Corollary LV-COUNT: in each phase the in-scope THR fallbacks with M = −1 number at most 1 + (those with a (β) gate); if
      rank o > rank c there is at most one, the phase's last transition. The packet's condition "CONDITIONAL on CN-LAST" is discharged:
      CN-LAST is RESULTS R38 (f), with exactly LV-CN's hypotheses (LV-N1; REFEREE's verdict, REFEREE-2's §C).
  (c) Lemma FLAT-ALL_{−1}: at a fallback k of a scope run with M_k = −1, r_k ≥ 0 and (h) at k and k + 1, R31 FLAT-ALL (i)-(iv) hold with
      M := −1. Part (i) uses FBL, the phase and H1 at k + 1 (R31 FBW-1), not H2 (N-LV-1, citation, both referees).
  (d) Lemma STRETCH_{−1}: if [s, e] are consecutive states of a scope run S and COARSE_{−1}(Ξ_t v) is the same for all t ∈ [s, e] and
      every v, each Even y is a level −1 tail at most n
      times among the fallbacks k of S with s ≤ k ≤ e and M_k = −1 (LV-N2 = N-LV-2: "k ≤ e", which PL_{−1} (a)'s last run needs; the
      packet's "k < e" is repaired; the bound n stays).
  (e) Theorem PL_{−1}: (a) N ≤ n·n_E·(1 + D_{−1}); (b) the first COARSE_{−1}(Ξ) change j of a dirty interval is an S4a step with
      O_j > −1 ≥ E_j, lev(θ_j, θ_{j+1}) = O_j, and an absorption; (c) D_{−1} ≤ (d_o − 1) + REL_{−1}, hence N ≤ n·n_E·(d_o + REL_{−1}).
      In (a) the block's fallbacks lie in at most 1 + D_{−1} runs of constant COARSE_{−1}(Ξ) (LV-N3, wording). Corollary LV-PL: every
      scope run S has at most n·n_E·(d_o + REL(S)) THR fallbacks with M = −1 and r ≥ 0; with LV-COUNT, all but at most one per phase
      are (β)-fallbacks.
- Not signed (packet §5 and the addendum): CONJECTURE "in scope, THR ⇒ M ≥ 0"; OPEN: THR fallbacks with u* = none (r = −1; bounded
  separately by LV-NONE in packet P-N5-LV2, in review), REL(S) at level −1; the addendum's CONJECTURE NL= is FALSE
  (experiments/red/so/instances/nleq_cex_n48.pg, sha1 e72e4034, L-RED successor 16: an NL (ii) leave at r = L = 47, step 6, vertex
  40 → 9; Lead re-run: one Odd choice vertex, n5 10/1, Oink zlk OK strategies verified, L-SI's nleq.py nl2_fail 1), so the reading
  "NJB in full ⇐ (P) ∧ NL=" gives nothing and NJB's straddling interval stays OPEN; no signed item cites NL at r_j = L (both §Cs).
- Honest limits: (i) SUBCLASS 𝒞^1O. (ii) LV-PL bounds level −1 fallbacks with r ≥ 0 per scope run GIVEN REL(S); the u* = none
  fallbacks, REL(S) at level −1, scope runs per phase and the other open pieces of G-N5-TIME stay OPEN. (iii) The r ≥ 0 part (FLAT-ALL_{−1},
  STRETCH_{−1}, PL_{−1}, LV-PL) has vacuous hypotheses in all data of both referees and the lane: no in-scope THR fallback with M = −1
  and r ≥ 0 occurs. The setting with r = −1 (u* = none) IS reachable (N-LV-3): 173,371 such fallbacks in REFEREE-2's climbs (witness
  docs/referee-2/R2-N5-LV/climb/best_lv_9401.pg, sha1 4b74cd84; Lead re-run: one Odd choice vertex, n5 5/1, Oink zlk OK strategies
  verified) and 351,417 in REFEREE's, with LV-SHAPE holding at every gate (1,037,743 and 1,321,606 gates). (iv) The packet's §0
  statuses of R37 / R38 are stale (LV-N1).
- Data (DATA, not proof; one Odd choice vertex asserted on every game): REFEREE lv_probe.py (own engine; logs docs/referee/R-N5-LV/):
  288 𝒞^1O games, 788 in-scope THR fallbacks with r ≥ 0, all M ≥ 0, 0 with r = −1, 11 EQ fallbacks with M = −1; a 2,636,361-mutant
  climb that never reached an in-scope THR fallback (weak evidence); in §C, a climb seeded from best_lv_9401 (769,515 evaluations,
  351,417 u* = none fallbacks, LV-SHAPE 0 failures). REFEREE-2 (own code): 66,655 batch runs (the (LV) setting never occurs) and 4
  climbs (850,608 runs, 173,371 u* = none fallbacks), 0 violations. Lane lvm1.py: 1,032 in-scope THR fallbacks with r ≥ 0, all M ≥ 0.
- Signatures: REFEREE docs/referee/R-N5-LV.md (referee 8054da2, successor 9; §C 46a8030): LV-SHAPE, LV-CN, LV-COUNT (CN-LAST
  discharged by R38 (f)), FLAT-ALL_{−1}, STRETCH_{−1}, PL_{−1} (a)-(c), LV-PL SIGNED; notes LV-N1..N3; no gaps. REFEREE-2
  docs/referee-2/R2-N5-LV.md (referee-2 b1038be, successor 9; §C a769ff5): LV-SHAPE, FLAT-ALL_{−1}, STRETCH_{−1}, PL_{−1} (a)-(c), LV-PL
  SIGN; LV-CN, LV-COUNT and LV-PL's last sentence SIGN CONDITIONAL ON CN-LAST (in §C: unconditional now that CN-LAST is R38 (f));
  notes N-LV-1..3; no gap. §C (both): verdicts the same in substance; joint gap map empty; N-LV-1 accepted by REFEREE (missed),
  LV-N2 = N-LV-2, LV-N3 accepted by REFEREE-2, N-LV-3 accepted and re-run by REFEREE.
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.

### R42 [refereed-only] N5 on one-Odd-choice games: after an HN fallback with θ constant, a new F → R̄ gate needs an R̄-rise (RISE; high in case A, HIGH-RISE), no vertex enters R when o tops its W-cycle in case A (NO-ENTRY-A′), case-B gates are length-only and their failures need a low rise (CASE-B-LEN′, LOW-RISE′), so every break of an HN stretch is paid by a θ-change or an R̄-rise (Theorem BRK), and for τ(o) = o the out-of-SN fallbacks per phase are polynomial in θ-changes and H1-toggles (OUT-1) (2026-10-25) — partial step-4 lemmas for N5 (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C51.md, checker bd08936b)
- Object (packet P-N5-NEB, added at l-new 8ca3571, pinned trunk 314d220, unchanged during review): docs/new/P-N5-NEB-box38.md, sha1
  ba15e51fb02471207b11ecd64e9687a23fe8a744 (L-NEW successor 17, Opus 5.5). The referees' notes are collected by the lane in
  docs/new/P-N5-NEB-fixes-box38.md (l-new e535e61, sha1 15434c1ca9920b8254ce48834b07cd86f5946837, L-NEW successor 19: NEB-R1 =
  N-NEB-1, NEB-N1..N5, N-NEB-2, N-NEB-3, NEB-B1); on trunk; repairs only.
  Setting as in RESULTS R38 and R39 (𝒞^1O; phase = (λ_Ξ, τ)-phase; R_k, R̄_k, F_k, routes; H1, H2; θ, w, c_θ, c_w; HN states and HN
  stretches; crossings, entries, evictions; breaks; Iσ_k; case A: rank(o) > rank(c_θ), case B: rank(c_θ) > rank(o); K := n_E(2n − 1)).
  An R̄-RISE at t → t+1 is a strict rise of Ξ at some z ∈ R̄_t ∩ R̄_{t+1} with z ≠ o; it is HIGH if its level is ≥ rank(o) and LOW if
  Ξ_t(z) and Ξ_{t+1}(z) both lie in the low class C_θ := {(c_θ, P(θ), ℓ) : ℓ ≥ 0}. "o tops its W-cycle at a" means c_w(a) = o.
  x ≡_o y iff lev(x, y) < rank(o); x ≡_B y iff lev(x, y) ≤ −1. For a break of an HN stretch S, its EVICTION STATE is the state of the
  first eviction after the previous entry of S (or after S's start). LR_S counts the transitions of S with θ unchanged and a low rise;
  RW_S counts the transitions with θ unchanged and an R̄-rise that lie in [a, k) for a break whose eviction state a has c_w ≠ o.
- Claims signed (both referees "(Opus 5.5, D15)", L37); no item uses (P):
  (a) Lemma RISE (any τ(o), cases A and B): if an in-phase Even fallback is taken at a ∈ S (S an HN stretch), θ is constant on [a, t+1]
      with t+1 ∈ S,
      no state of [a, t] has an F → R̄ gate and t+1 has one, then there is an R̄-rise at t → t+1.
  (b) Lemma HIGH-RISE (case A, any τ(o), any c_w): in (a), the rise satisfies lev(Ξ_t z, Ξ_{t+1} z) ≥ rank(o).
  (c) Theorem NO-ENTRY-A′ (case A, c_w(a) = o, any τ(o)): if an Even fallback a → a+1 is taken at a ∈ S (S an HN stretch) and θ is
      constant on [a, b] ⊆ S, then the invariant INV(t) (no F → R̄ gate; every
      R → R̄ gate has lev < rank(o)) holds on [a, b], no transition of [a, b] is an entry, R̄ only shrinks, and Ξ_t(z) ≡_o Ξ_a(z) for
      z ∈ R̄_t; in particular no R̄-rise on [a, b] is high. For τ(o) = o this is RESULTS R39 (e) in the general form. The base cites
      FBL-N (i) (RESULTS R21 (c)) + F1 (RESULTS R17 (a)) in place of Step (K) (R23 (a), "inside a phase") (NEB-R1 = N-NEB-1, citation;
      as R39's OUT-R1; it applies to (d) as well).
  (d) Lemma CASE-B-LEN′ (case B, c_w(a) = o, any τ(o)): at an HN state a where an Even fallback is taken, every R → R̄ gate (v, z) has
      lev(Ξ_a(σ_a v), Ξ_a(z)) = −1 and z's route longer than σ_a(v)'s.
  (e) Lemma LOW-RISE′ (case B, c_w(a) = o, any τ(o)): with a as in (d) and S its HN stretch, INV_B(a) holds (no F → R̄ gate; every
      R → R̄ gate has level −1); if t+1 ∈ S, θ is constant on [a, t+1] and INV_B holds on [a, t], then (a) no transition of [a, t+1] is an entry and Ξ_{t+1}(z) ≡_B Ξ_t(z) for
      z ∈ R̄_{t+1}; (b) (ii_B) holds at t+1; (c) if (i) fails at t+1, there is a LOW rise at some z ∈ R̄_t ∩ R̄_{t+1} at t → t+1. (b)
      does not need (i) at t+1 (N-NEB-2, optional).
  (f) Theorem BRK (any τ(o)): for every break of an HN stretch S, with eviction state a and entry k → k+1: (a) in case A with
      c_w(a) = o there is a θ-change in (a, k]; (b) in case B with c_w(a) = o, a θ-change in (a, k] or a LOW rise in [a, k) with θ
      unchanged; (c) in general, a θ-change in (a, k] or an R̄-rise in [a, k) with θ unchanged, HIGH in case A; (d) B_S ≤ θ_S + LR_S + RW_S
      with LR_S ≤ (n − 2)²(θ_S + 1), and if o tops its W-cycle at every eviction state of S (always when τ(o) = o), B_S ≤ θ_S +
      (n − 2)²(θ_S + 1), and in case A B_S ≤ θ_S. The eviction a → a+1 is a fallback by SPLIT (a) (RESULTS R39 (a)) (NEB-N1; the packet's
      "SPLIT (b)"), and a itself has no F → R̄ gate by FBL-N (iii) + (iii+) (NEB-N2).
  (g) Corollary OUT-1 (τ(o) = o, cases A and B): with D := (n − 2)² + 1, X_HN ≤ 2(n − 1)·D·(θ_ph + N_HN) and
      f_HN ≤ (K + 1)(2(n − 1)·D·(θ_ph + N_HN) + N_HN), where N_HN ≤ ⌊T_ph/2⌋ + 1 and f_HN counts the in-phase fallbacks from HN states
      (premises RESULTS R39 (b) EPOCH, (f) NE-COUNT (c), R38 (a), (d), R34 (e)).
- Not signed (packet §8): NO-ENTRY-B FALSE and NO-ENTRY for c_w ≠ o FALSE (both recorded in RESULTS R39: nebc_cex_n14, tauw_A_cex_n24,
  tauw_B_cex_n24); the dead ends NO-RR-B, NO-RISE-B and "INV_B (i) propagates" (all killed on nebc_cex_n14: states 1, 1 → 2, 2; obstruction
  §5 (c), a low rise); CONJECTURE BAND is FALSE in three forms (NEB-B1): in the rises form on experiments/new/box38/instances/tauw_A_cex_n24.pg
  (sha1 e29908d5; the S4a step 12 → 13 raises Ξ(11) and Ξ(16) at level 23 > rank(c_w) = 21; L-NEW successor 17, Lead re-run of the
  lane's score (4, 5, 2)), (REFEREE successor 9, both gates forms) in the gates form at a later state (tauw_A state 13, gates 3 → 11 and 7 → 16 at level 23), and in the gates
  form at the base at the boundary (docs/referee/R-N5-NEB/band_base_cex.pg, sha1 468edac8, n 24: base a = 2, gate 5 → 14 at level
  19 = rank(c_w = 2); REFEREE successor 9; Lead re-run: one Odd choice vertex, n5 6/1, Oink zlk OK strategies verified); OPEN: RW_S
  (rises after c_w ≠ o evictions), θ_S / θ_ph, HN stretches per phase for τ(o) ≠ o, OTHER states.
- Honest limits: (i) SUBCLASS 𝒞^1O, inside a phase. (ii) BRK bounds breaks by θ-changes plus R̄-rises; RW_S and θ-changes per phase are
  not bounded here, so G-N5-TIME stays open; OUT-1 is polynomial GIVEN θ_ph for τ(o) = o only. (iii) On the library (lib37) the
  hypotheses of RISE, HIGH-RISE, CASE-B-LEN′ and LOW-RISE′ (c) never occur and every break is charged to a θ-change; they occur only on
  the box-38 instances and in climbs, where they occur many times (REFEREE's §9). (iv) The packet's §9 base totals (13 / 6 / 34 / 27,
  data/inv2_all.txt) came from an unnamed larger input; the stated command gives 75 / 9 / 4 / 20 / 8 (NEB-N5; the lane re-ran it and
  withdraws the old totals). (v) Status rows of the packet are stale: P-N5-OUT is RESULTS R39, KEY / FB-INT are RESULTS R38 (N-NEB-3,
  NEB-N4). (vi) Lane work after the pin (P-N5-PFZ, P-N5-RHO, N5-NHN) is not part of this entry.
- Data (DATA, not proof; one Odd choice vertex asserted on every game): REFEREE neb_probe.py (own engine; logs docs/referee/R-N5-NEB/):
  lib37 270 games, lane set 275, 6 named starts; 0 failures; NO-ENTRY-A′ 84 runs / 835 states on lib37; climbs from nebc_cex_n14,
  tauw_A_cex_n24, tauw_B_cex_n24, wd16_s2 (3,336,298 mutants): every hypothesis of §1, §2, §4, §5 (c) and the B= / B≠ charging of §6 occurs
  many times, 0 failures; in REFEREE's data case-A breaks with c_w = o occur only in the library (8, all θ-charged). REFEREE-2 (own checker; own / random
  / SPEC traces): 66,655 batch runs and climbs (501,892 runs), 0 violations; the new class (case A, c_w = o, τ(o) ≠ o) 26 / 20 / 28
  library bases and 18,324 in climbs; LOW-RISE′ (c) 31,951 first INV_B failures in climbs, each with a low rise; control: INV fails
  80k times outside the proved class, never inside.
- Signatures: REFEREE docs/referee/R-N5-NEB.md (referee 40adbf1, successor 9; §C 46a8030): RISE, HIGH-RISE, NO-ENTRY-A′, CASE-B-LEN′,
  LOW-RISE′, BRK (a)-(d), OUT-1 SIGNED; notes NEB-R1, NEB-N1..N5, NEB-B1; no gaps. REFEREE-2 docs/referee-2/R2-N5-NEB.md (referee-2
  a4516df, successor 9; §C a769ff5): RISE, HIGH-RISE, NO-ENTRY-A′ (with its Case 1′), CASE-B-LEN′, LOW-RISE′, BRK (a)-(d), OUT-1 SIGN;
  notes N-NEB-1..3; no gap. §C (both): verdicts identical; joint gap map empty; N-NEB-2 accepted by REFEREE (missed); NEB-N1..N3
  accepted by REFEREE-2.
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.

### R43 [refereed-only] N5 on one-Odd-choice games: a gate target always changes value after an Even fallback (STALE-GATE, every game), level −1 fallbacks need no REL (ENT-X_{−1}, LV-PL′), the u* = none fallbacks are counted (SAND, FLAT-ALL_{−1}^{none}, LV-NONE), and every scope run has at most 4·n·n_E + 3 fallbacks (SCOPE-FB) (2026-10-25) — partial step-4 lemmas for N5 (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C52.md, checker 707b402e)
- Object (packet P-N5-LV2, added at l-si ed936af1, pinned trunk 283bcb6, unchanged during review): docs/si/P-N5-LV2-box12.md, sha1
  3b23a41fee6b705e20092d8dd49e7ce0b1408b03 (L-SI successor 7, Opus 5.5). The referees' notes are collected by the lane in
  docs/si/P-N5-LV2-fixes-box12.md (l-si 680c0294, sha1 f76fd1d1d7bfa70e5eb2e2bd354597853f093f87, L-SI successor 8: statuses, the
  CYC-EV citation and P-set identity in ENT-X_{−1} (c), §9 data); on trunk; repairs only.
  Setting as in RESULTS R31, R35, R37, R40 and R41 (scope run S; fallbacks, gates, gate levels, M_k; COARSE_L, (C1)-(C7); b_k(y);
  θ, w, r; THR, EQ; u* (u* = none iff r = −1); R̄ / R / F; (h); c; window gates; the kinds (α), (β), (γ) of R41 (a); the level −1 block
  f_1 < … < f_N of R41 (e)). (a) holds on every game; the rest is on 𝒞^1O.
- Claims signed (both referees "(Opus 5.5, D15)", L37); no item uses (P) beyond what RESULTS R36 discharges:
  (a) Lemma STALE-GATE (every game): if k0 is an S4c fallback at which Even switches and k > k0 a later state of the same run, every gate
      (y, z) at k has Ξ_k(z) ≠ Ξ_{k0}(z).
  (b) Corollary EV-G: if k0 is an in-phase THR S4c fallback with (h), k > k0 a state of the same phase and (y, z) a gate at k with
      z ∈ F_k, then z's σ_k-play is not contained in F_{k0} (FREE-FREEZE, RESULTS R37 (c), with (P) discharged by RESULTS R36).
  (c) Theorem ENT-X_{−1}: if k0 < k are consecutive fallbacks of a scope run in its level −1 block and k has a window gate (equivalently a
      (β) gate), the interval (k0, k) is clean. Step (c) cites CYC-EV (RESULTS R40 (d)) to place q before c on z's play, and the identity
      "Ξ_k(z) = ρ ⊕ Ξ_k(q)" is read as a P-set identity (LV2-N1, N-LV2-2; fixes).
  (d) Corollary LV-PL′: every scope run has at most n·n_E + 1 THR fallbacks with M = −1 and r ≥ 0 (REL(S) removed; compare R41 (e)).
  (e) Lemma SAND: if t ≤ t′ are states of a scope run with r_t = −1, then COARSE_{−1}(θ_{t′}) = COARSE_{−1}(θ_t).
  (f) Lemma FLAT-ALL_{−1}^{none}: at a fallback k of a scope run with r_k = −1 and (h) at k and k + 1, R31 FLAT-ALL (i)-(iv) hold with
      M := −1.
  (g) Theorem LV-NONE: every scope run has at most n·n_E + 1 THR fallbacks with r = −1.
  (h) Corollary SCOPE-FB: every scope run has at most 4·n·n_E + 3 S4c fallbacks (level ≥ 0: ≤ 2·n·n_E by RESULTS R40 (f) PL-S″; level −1
      with r ≥ 0: ≤ n·n_E + 1 by (d); r = −1: ≤ n·n_E + 1 by (g); EQ: ≤ 1 by RESULTS R37 (d) with CN-LAST = R38 (f)). The packet's
      conditions (C-ENT) and (C-LV) are now RESULTS R40 and R41 (landed); (c), (d), (f), (g) rest on R41.
- Not signed (packet §10): docs/si/N5-LV3-box12.md (XG, ANTI, NEED-β; now packet P-N5-NEEDB, in review) and the CONJECTURE "in scope,
  THR ⇒ M ≥ 0"; the packet's Reading that SCOPE-FB closes R29's per-scope-run count CL-S (a reading). REFEREE-2's candidate CONJECTURE
  in N-LV2-3 ("an in-scope THR fallback with M = −1 is the last fallback of its scope run") is FALSE (R2 Addendum B withdraws it), and so is
  L-SI's CONJECTURE NONE-LAST (docs/si/DEAD.md): experiments/red/so/instances/beta2_n11.pg (sha1 bdea2a23, L-RED successor 16) has one scope run with two
  r = −1 THR fallbacks at states 0 and 1 (an eviction cascade: fallback 0 evicts 5, and the R-vertex 10 then has a (β) gate (10, 5));
  Lead re-run: one Odd choice vertex, n5 4/2, Oink zlk OK strategies verified, L-SI's scopefb.py gives fb_r=-1 2 in one scope run;
  confirmed on both referees' engines.
- Honest limits: (i) SUBCLASS 𝒞^1O except (a). (ii) SCOPE-FB bounds fallbacks per scope run; scope runs per phase, out-of-scope
  fallbacks, S4a steps, phases and wakes K stay open here, so G-N5-TIME stays open. (iii) Thin data: ENT-X_{−1} and LV-PL′'s block with
  N ≥ 2 are vacuous in all data; the first level −1 block fallback with r ≥ 0 is REFEREE-2's witness
  docs/referee-2/R2-N5-LV2/climb/block_9501.pg (sha1 1b5b76fd; from the start pair in climb/block_9501.txt, state 1; N = 1; reproduced
  on REFEREE's engine from that start pair, R-N5-NEEDB (referee 008ad8ab); Lead re-run from the canonical start, where the run has no
  block fallback: one Odd choice vertex, n5 3/1, Oink zlk OK strategies verified). LV-NONE's N = 2 step is exercised only on beta2_n11; climbs
  give at most 1 u* = none fallback per scope run.
- Data (DATA, not proof; one Odd choice vertex asserted on every game): REFEREE (own probe): STALE-GATE 70,267 checks on 402 games
  (114 non-𝒞^1O), EV-G 34,389, SAND 181, SCOPE-FB on 236 scope runs (max 37 fallbacks per run); in its addendum, a climb seeded from
  best_lv_9401: FLAT-ALL_{−1}^{none} 351,417 checks, SAND 1,000,826, max 1 u* = none fallback per scope run; 0 failures. REFEREE-2 (own code): batch (66,655 runs + 1,422 on newer files; max 37 fallbacks per scope run, all of level ≥ 0) and 5
  climbs (1.72 M runs): in the climbs 237,033 u* = none fallbacks, max 1 per scope run (worst LV-NONE ratio 22‰), max 5 fallbacks per
  scope run, FLAT-ALL^{none} at all 237,033, SAND 921,624, 645 level −1 block fallbacks with r ≥ 0 (max 1 per scope run); 0 violations;
  mutation controls bite in 2 of 4 (sand0, fa0; the other two cannot bite at N ≤ 1). Lane: STALE-GATE 72,589, EV-G 39,406, SAND 310, SCOPE-FB 293 scope runs.
- Signatures: REFEREE docs/referee/R-N5-LV2.md (referee b454ca3, successor 9; addendum 46a8030; §C ed8bc20, successor 10): STALE-GATE,
  EV-G, ENT-X_{−1}, LV-PL′, SAND, FLAT-ALL_{−1}^{none}, LV-NONE, SCOPE-FB SIGNED with the conditions as labelled; notes LV2-N1, LV2-N2; no gaps.
  REFEREE-2 docs/referee-2/R2-N5-LV2.md (referee-2 a551deb, successor 10; addendum f2209fa (block witness); Addendum B 11126df; §C ab7843a, successor 11): all 8 SIGN; notes
  N-LV2-1..3; no gap. §C (both): verdicts identical; joint gap map empty; LV2-N1 and LV2-N2 accepted by REFEREE-2; N-LV2-1 matches
  REFEREE's verdict note.
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.

### R44 [refereed-only] N5 on one-Odd-choice games: every in-phase Even fallback is a Bellman-Ford round on U = λ⁻¹(c_θ) (FB-ROUND), so on a θ-run (and on a P-epoch) P(Ξ) freezes on U after |U| − 1 fallbacks (P-FREEZE, P-FREEZE′), later U-rises are length rises and, in case A, not crossings (LEN-TAIL, NO-CROSS-A), θ changes at most |U| − 2 times inside a P-epoch (θ-LEN), and breaks per HN stretch are polynomial in θ-changes (BRK-POLY, via RISE′) and in P(θ)-changes (BRK-POLY′) (2026-10-25) — partial step-4 lemmas for N5 (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C53.md, checker 053a74f0)
- Objects (one review unit; both unchanged during review): packet P-N5-PFZ, docs/new/P-N5-PFZ-box39.md, sha1
  3c617e06f7b9c67d5d9cd865acd134f3a8aed071 (added at l-new c9f9caa1, pinned trunk 283bcb6), and its companion P-N5-PFZ-ext,
  docs/new/P-N5-PFZ-ext-box39.md, sha1 b3702b1ba1849c6aa19cebd2c8fa57e02a318d2a (added at l-new 1b6239fb, pinned trunk c61ecc4) (L-NEW
  successor 18, Opus 5.5). The referees' notes and the repair of gap PFZ-1 are collected by the lane in docs/new/P-N5-PFZ-fixes-box39.md
  (l-new cf20cdc2, sha1 3f55bc882b08d97508d98eda1c3a9f6aeaa0c99c, L-NEW successor 20); on trunk; repairs only.
  Setting as in RESULTS R39 and R42 (𝒞^1O; phase; HN states and stretches; θ, c_θ; R_k, R̄_k, F_k; crossings, entries, evictions;
  breaks B_S; θ_S the θ-changes of S). U := λ⁻¹(c_θ) (constant on a phase); wt(v) := sgn(v)·2^rank(v) if rank(v) > rank(c_θ), else 0
  (sgn = +1 for even, −1 for odd priority); M_t(z) := wt(P(Ξ_t z)) for z ∈ U. A θ-RUN is a maximal run of states of a phase with θ
  constant, and f_1 < f_2 < … are its in-run Even S4c fallback transitions. A P-EPOCH is a maximal run of states of a phase with P(θ)
  constant; ρ_S is the number of transitions of S at which P(θ) changes. A U-RISE is a strict rise of Ξ at some z ∈ U. The
  TERMINALS are o and c_θ. G_U is the graph on U in which every Even v ∈ U ∖ {c_θ} keeps all its edges into U, every Odd
  v ∈ U ∖ {o, c_θ} keeps its forced edge, and o and c_θ are sinks. For a θ-run Θ, M_Θ(o) := wt(P(θ)) and M_Θ(c_θ) := 0, and
  Mopt_Θ(z) := max{wt(p ∖ {end}) + M_Θ(end) : p a simple path in G_U from z to a terminal}; M_Π and Mopt_Π are the same on a P-epoch Π.
- Claims signed (both referees "(Opus 5.5, D15)", L37); no item uses (P):
  (a) Lemma FB-ROUND: at an in-phase Even S4c fallback k → k+1, M_{k+1}(v) ≥ wt(v) + M_k(x) for every Even v ∈ U ∖ {c_θ} and every
      successor x ∈ U of v (with the facts (A) additivity, (M1′), (M2′) of packet §1).
  (b) Theorem P-FREEZE: on a θ-run Θ, (a) after f_j, M_t(z) is at least the weight of every simple path in G_U from z to a terminal
      with ≤ j edges (plus the terminal's value); (b) M_t(z) ≤ Mopt_Θ(z); (c) for t > f_{|U|−1}, M_t = Mopt_Θ on U and P(Ξ_t z) is
      constant on U.
  (c) Corollary LEN-TAIL: in a θ-run, at most |U|(|U| − 1) transitions after f_{|U|−1} carry a U-rise, each a length rise. Corollary
      NO-CROSS-A (case A): a transition of a θ-run after f_{|U|−1} with H1 at both ends is not a crossing.
  (d) Lemma RISE′ (a re-proof of P-N5-NEB's RISE from landed results): if an in-phase Even fallback is taken at a ∈ S (S an HN stretch),
      k > a, k → k+1 is an entry in S and no transition of [a, k) is an entry, then θ changes at some t → t+1 with a + 1 ≤ t ≤ k, or some
      t → t+1 with a ≤ t < k, θ constant on [a, t+1] and t+1 ∈ S, carries an R̄-rise.
  (e) Theorem BRK-POLY: for every HN stretch S, any τ(o) and any c_w, B_S ≤ θ_S + (θ_S + 1)(|U| − 1 + |U|(|U| − 1)) ≤ θ_S +
      (θ_S + 1)(n² − 1); in case A, B_S ≤ θ_S + (θ_S + 1)(|U| − 1).
  (f) Theorem P-FREEZE′ (ext §1): P-FREEZE (a)-(c), LEN-TAIL and NO-CROSS-A hold verbatim on P-epochs, with Θ, M_Θ, Mopt_Θ replaced by
      Π, M_Π, Mopt_Π (only M(o) = wt(P(θ)) is used). Lemma θ-LEN (ext §2): a P-epoch has
      at most max(|U| − 2, 0) θ-changes.
  (g) Theorem BRK-POLY′ (ext §3), for every HN stretch S, any τ(o) and any c_w: (i) θ_S ≤ (ρ_S + 1)·max(|U| − 2, 0); (ii) B_S ≤ θ_S +
      (ρ_S + 1)(|U| − 1 + |U|(|U| − 1)) ≤ (ρ_S + 1)(|U|² + |U| − 3) ≤ (ρ_S + 1)(2n² − 1); (iii) in case A, B_S ≤ θ_S + (ρ_S + 1)(|U| − 1) ≤
      (ρ_S + 1)(2n − 3). The ext's proof of (i) ("apply θ-LEN to each of the ≤ ρ_S + 1 P-epochs") omits the ρ_S transitions at which
      P(θ) itself changes, which are θ-changes too (gap PFZ-1 = G-PFX-1, found independently by both referees); as written it gives
      only (i′) θ_S ≤ ρ_S + (ρ_S + 1)·max(|U| − 2, 0). (i)-(iii) are signed as stated with REFEREE's repair as the proof of (i)
      (fixes §1): a refined θ-LEN, ≤ |A_low| − [o ∈ A_low] = |U| − 2 − |A_high ∖ {o}| θ-changes per P-epoch, and ρ_S ≥ 1 forces some
      u ∈ A_high ∖ {o} (o's membership in P(θ) is fixed on the phase), so θ_S ≤ (ρ_S + 1)(|U| − 2) − 1 for ρ_S ≥ 1 (for ρ_S = 0, θ-LEN gives θ_S ≤ max(|U| − 2, 0)).
      REFEREE-2 diffed the fixes §1 text against its C.2 (§C addendum C.5, referee-2 ea5cc217): equal in substance in every step
      that carries the argument; two omissions, not mismatches (the case o = c_θ, where θ is constant; U constant on the phase).
- Not signed (packets' "Not to sign"): W-TIE steps (OPEN); the block lemmas of docs/new/N5-RW-box39.md (BF-RW, FREEZE-M, FREEZE-X,
  ROUTE-LEN, W-POT, CW-COUNT; lane, not routed); OPEN: θ_S / θ_ph, ρ per phase (lane packet P-N5-RHO, in review), HN stretches per phase
  for τ(o) ≠ o (lane packet P-N5-NHN, in review), OTHER states, S4a steps between fallbacks (P-FREEZE is not an iteration bound).
- Honest limits: (i) SUBCLASS 𝒞^1O, inside a phase. (ii) BRK-POLY and BRK-POLY′ bound breaks GIVEN θ_S, resp. ρ_S; the counts of θ- and
  P(θ)-changes per phase and the other open pieces of G-N5-TIME remain. (iii) Thin data: the post-freeze regime (t > f_{|U|−1}) occurs
  in data only for |U| ≤ 2, even under targeted climbs (REFEREE-2: 955,321 θ-runs at |U| = 2, none at |U| ≥ 3; REFEREE: one fallback short
  of the freeze at |U| ≥ 3, never past it); so P-FREEZE (c), LEN-TAIL, NO-CROSS-A and BRK-POLY's j ≥ |U| branch rest on their proofs. The
  repaired (i) never came within 6 of its bound in REFEREE-2's data.
- Data (DATA, not proof; one Odd choice vertex asserted on every game): REFEREE (own probe on 278 𝒞^1O games, θ-runs and P-epochs):
  FB-ROUND 80,955 checks, the upper bound and P-FREEZE (a) exact for |U| ≤ 13, BRK-POLY / BRK-POLY′ all checked, 0 failures; a 6.48 M
  mutant climb; the refined θ-LEN count 0 failures over 599 in-epoch θ-changes. REFEREE-2 (own checker): batch 66,655 runs, climbs
  4,653,840 runs, FB-ROUND 6.77 M checks, 0 violations; ext: 1,367 logs and 408k climb runs, 0 violations, (i) as written never exceeded;
  in its PFZ §C, the refined count was reached exactly 6,398 times in 849,280 climb runs and never exceeded. Lane: 714 θ-runs, 857
  P-epochs, 0 failures.
- Signatures: REFEREE docs/referee/R-N5-PFZ.md (referee 8595343, successor 9; main §C 4859e63; ext §C ed8bc20, successor 10):
  FB-ROUND, P-FREEZE (a)-(c), LEN-TAIL, NO-CROSS-A, RISE′, BRK-POLY (i), (ii), P-FREEZE′, θ-LEN SIGNED; BRK-POLY′ (ii), (iii) SIGNED given
  (i); (i) SIGNED WITH GAP PFZ-1, repaired in the ext §C; notes PFZ-N1..N3. REFEREE-2 docs/referee-2/R2-N5-PFZ.md (referee-2 37e55fd,
  successor 9, main packet; §X 78896bf, successor 10, ext; §C 212f88e, successor 11): FB-ROUND, P-FREEZE, LEN-TAIL, NO-CROSS-A, RISE′,
  BRK-POLY, P-FREEZE′, θ-LEN SIGN; BRK-POLY′ (i) NOT SIGNED as stated in §X (G-PFX-1), (i′) signed; in §C (C.2) BRK-POLY′ (i)-(iii)
  SIGNED as stated with REFEREE's repair as the proof of (i), subject to its diff of the fixes text; in C.5 (ea5cc217, successor 11)
  the diff is recorded and (i)-(iii) are SIGNED UNCONDITIONALLY as stated, with the fixes §1 repair as the proof of (i); notes N-PFZ-1..3. §C (both): verdicts identical after the repair; joint
  gap map: PFZ-1 = G-PFX-1, closed by the repair (fixes §1; REFEREE-2's condition discharged in C.5).
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.

### R45 [refereed-only] N5 on one-Odd-choice games: θ's signed path weight is a Bellman-Ford value (Y-FORM), it freezes on F ∩ U after |U| − 2 fallbacks of a phase (HAT-FREEZE) and then changes P(θ) at most deg(o) times (RHO-TAIL); S4a steps between HN states are Bellman-Ford rounds (BF-F, FREEZE-F), so P(θ)-changes over the HN states of a phase are polynomial in n and N_HN (RHO-HN), and so are HN breaks, crossings, fallbacks and θ-changes (HN-POLY) (2026-10-25) — partial step-4 lemmas for N5 (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C54.md, checker 21f7d9b9)
- Object (packet P-N5-RHO, added at l-new 3e9fe5c2, pinned trunk c814455, unchanged during review): docs/new/P-N5-RHO-box40.md, sha1
  cd5df65c2f3e6829f85739a57023fc3da6944baa (L-NEW successors 18 (source) and 19 (packet), Opus 5.5). The referees' notes are collected by
  the lane in docs/new/P-N5-RHO-fixes-box40.md (l-new cf02711c, sha1 cc4e8540ee8aeb4a85e68e1493b2bc71b9824997, L-NEW successor 20:
  RHO-N1, RHO-N2, RHO-N3, N-RHO-1, N-RHO-2); on trunk; repairs only.
  Setting as in RESULTS R39, R42 and R44 (𝒞^1O; phase; HN states and stretches; θ, c_θ; R_k, R̄_k, F_k; g_1 < g_2 < … the in-phase Even
  S4c fallback transitions of the phase). U := λ^{-1}(c_θ), Û := U ∖ {o}; wt(v) := sgn(v)·2^rank(v) if rank(v) > rank(c_θ), else 0;
  M_t(z) := wt(P(Ξ_t z)) for z ∈ U; G_Û is the graph on Û in which every Even v ∈ Û ∖ {c_θ} keeps its edges into Û, every Odd
  v ∈ Û ∖ {c_θ} keeps its forced edge if it lies in Û, and c_θ is a sink; MoptÛ(z) := max{wt(p ∖ {c_θ}) : p a simple path in G_Û from z
  to c_θ} (undefined if there is none); for A ⊆ U ∖ {o} with c_θ ∈ A, G[A] is defined in the same way on A; Y_t := succ(o) ∩ U ∩ F_t; deg(o) the out-degree of o; N_HN the number of HN stretches of the phase; ρ_HN (ρ_S)
  the number of transitions of the phase (of S) with both ends HN at which P(θ) changes.
- Claims signed (both referees "(Opus 5.5, D15)", L37); no item uses (P):
  (a) Lemma Y-FORM: at an H1 state t, σ̄_t(o) ∈ Y_t and M_t(o) = wt(o) + min_{y ∈ Y_t} M_t(y); at a ¬H1 state, P(θ_t) = ∅.
  (b) Lemma HAT-FREEZE: in a phase, (a) for j ≥ 0, every state t > g_j, z ∈ Û and simple path p in G_Û from z to c_θ with ≤ j edges,
      M_t(z) ≥ wt(p ∖ {c_θ}); (b) for z ∈ F_t ∩ U, MoptÛ(z) is defined and M_t(z) ≤ MoptÛ(z); (c) if |U| ≥ 2, M_t(y) = MoptÛ(y) for every
      state t > g_{|U|−2} and y ∈ F_t ∩ U. No assumption on θ, H1, H2, τ(o) or c_w. (The case o = c_θ occurs for every |U|, and the
      statements hold there as well; RHO-N1, wording.)
  (c) Theorem RHO-TAIL: in a phase with |U| ≥ 2, at most deg(o) transitions t → t+1 with t > g_{|U|−2} change P(θ).
  (d) Lemma BF-F: at an in-phase S4a transition k → k+1 with H1 ∧ ¬H2 at k and k+1, M_{k+1}(v) ≥ wt(v) + M_k(x) for every Even
      v ∈ U ∩ F_{k+1}, v ≠ c_θ, and every successor x ∈ U of v.
  (e) Theorem FREEZE-F: on a run [s, e] of consecutive HN states of one phase with no fallback transition, (a) for t ∈ [s, e], z ∈ F_t ∩ U and
      every simple path p in G[F_t ∩ U] from z to c_θ with ≤ t − s edges, M_t(z) ≥ wt(p ∖ {c_θ}); (b) for t ≤ t′ in [s + |U| − 2, e] and
      z ∈ F_{t′} ∩ U, M_{t′}(z) = M_t(z); (c) at most
      max(|U| − 2, 0) + deg(o) − 1 transitions of [s, e] change P(θ).
  (f) Theorem RHO-HN: for one phase with |U| ≥ 2, ρ_HN ≤ (N_HN + |U| − 2)(|U| + deg(o) − 3) + deg(o) (its proof gives the sharper
      (N_HN + |U| − 3)(|U| + deg(o) − 3) + deg(o); N-RHO-1).
  (g) Corollary HN-POLY, conditional on BRK-POLY′ in the weak form (i′) and on (ii)'s window bound B_S ≤ θ_S + (ρ_S + 1)(|U|² − 1)
      (P-N5-PFZ-ext §3, RESULTS R44): HN breaks, crossings, fallbacks at HN states and θ-changes per phase are ≤ poly(n, N_HN)
      (Σ_S B_S = O(n⁴·N_HN), Σ_S X_S = O(n⁵·N_HN), fallbacks at HN states O(n⁷·N_HN)). For τ(o) = o: N_HN ≤ ⌊T*/2⌋ + 1 by RESULTS R34
      (e), with HN = H1 when τ(o) = o, so these are polynomial in n. (The packet cites RESULTS R39 (f) (c), which is signed for case A
      only; RHO-N2, citation, both referees.)
- Not signed (packet §7): N_HN for τ(o) ≠ o (lane result then, now packet P-N5-NHN, in review); the non-HN states; S4a steps that change
  none of the counted quantities (no iteration bound); W-TIE steps and the block lemmas of docs/new/N5-RW-box39.md.
- Honest limits: (i) SUBCLASS 𝒞^1O, inside a phase. (ii) HN-POLY is polynomial in n and N_HN; for τ(o) ≠ o, N_HN is not bounded here;
  wakes (K) and the other open pieces of G-N5-TIME remain. (iii) Thin data: HAT-FREEZE (c) and RHO-TAIL after the freeze occur in the
  library only at |U| = 2 (trivial) and in climbs only at |U| = 3 (lane 5 phases; REFEREE 685k phases, 1.16 M HAT-FREEZE (c) checks;
  REFEREE-2 133,889 phases), never at |U| ≥ 4; FREEZE-F (b) is vacuous (no fallback-free HN run longer than |U| − 2 transitions; N-RHO-2).
- Data (DATA, not proof; one Odd choice vertex asserted on every game): REFEREE (own engine and probe): library 0 failures, the packet's
  §8 (L) counts reproduced exactly; climbs (877k + 5.95 M candidates) 0 failures, 685k post-freeze phases at |U| = 3, RHO-TAIL 0 changes
  past the freeze. REFEREE-2 (own exact-DFS checker): 1,385 batch logs OK, 1.55 M climb runs, 0 violations; mutation control hatall
  bites (701 violations), frzb0 does not (reported as such). Lane rhodata.py: 990 phases, Y-FORM 6,335, BF-F 28,394, FREEZE-F (c) max
  13 changes (epsseg_cex_n48, bound 62), RHO-HN max 13 (bound 2,931), 0 failures.
- Signatures: REFEREE docs/referee/R-N5-RHO.md (referee 5927831, successor 10; §C 06d6e6d): Y-FORM, HAT-FREEZE, RHO-TAIL, BF-F,
  FREEZE-F, RHO-HN SIGNED; HN-POLY SIGNED conditional as labelled; notes RHO-N1..N3; no gaps. REFEREE-2 docs/referee-2/R2-N5-RHO.md
  (referee-2 269ae45, successor 10; §C ab7843a, successor 11): all SIGN; notes N-RHO-1, N-RHO-2; no gap. §C (both): verdicts identical;
  joint gap map empty; RHO-N2 accepted by REFEREE-2 (missed by successor 10), RHO-N1 accepted.
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.

### R46 [refereed-only] N5 on one-Odd-choice games: for τ(o) ≠ o, every end of an HN stretch into H1 ∧ H2 is an Even fallback that evicts τ(o) and strictly raises Ξ(τ(o)) (T0U, EV2-FB, SG-EV), after |U| − 2 fallbacks such an end is pinned (T0-PIN), so a phase has at most ⌈T/2⌉ + 2n − 3 HN stretches (NHN-BOUND), and HN breaks, θ-changes, crossings and fallbacks at HN states per phase are polynomial in n for every τ(o) (HN-POLY-ALL) (2026-10-25) — partial step-4 lemmas for N5 (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C55.md, checker bdc05b60)
- Object (packet P-N5-NHN, added at l-new 5fb9dca0, pinned trunk 0bb175d, unchanged during review): docs/new/P-N5-NHN-box40.md, sha1
  da7d09ec6cb27ee8f7d94b857bc13fb2946aff1a (L-NEW successor 19, Opus 5.5). The referees' notes are collected by the lane in
  docs/new/P-N5-NHN-fixes-box40.md (l-new 5e1b5ea0, sha1 d1460ffede49a68d2a5f779b1a1b2b3cd8f62a02, L-NEW successor 21: NHN-N1 =
  N-NHN-1 = RHO-N2, NHN-N2, N-NHN-2, NHN-N3); on trunk; repairs only.
  Setting as in RESULTS R39, R44 and R45 (𝒞^1O; phase; HN states and HN stretches; θ, c_θ, c_w; R_k, R̄_k, F_k; U, Û, G_Û, MoptÛ,
  M_t, g_1 < g_2 < … the in-phase Even S4c fallbacks; N_HN, ρ_HN, θ_S, B_S, X_S, f_S). t0 := τ(o) (constant on a phase). H3: c_θ = c_w;
  (h) := H1 ∧ H2 ∧ H3. T := |U|(n + 1) + n − 1 (RESULTS R34 (e)). A DROP is an in-phase transition from H1 to ¬H1; an EV2 END is an
  in-phase transition k → k+1 with HN at k and H1 ∧ H2 at k+1. A Q state is an H1 ∧ H2 ∧ ¬H3 state.
- Claims signed (both referees "(Opus 5.5, D15)", L37); no item uses (P):
  (a) Lemma T0U: in a phase with t0 ≠ o, (a) at every state t, ¬H2 holds iff t0 ∈ R_t; (b) if the phase has an HN state, then
      t0 ∈ U ∖ {o, c_θ} at every state of the phase, so |U| ≥ 3.
  (b) Lemma EV2-FB: in a phase with t0 ≠ o, every EV2 end k → k+1 is an Even S4c fallback with t0 ∈ R_k ∖ R_{k+1} (SPLIT (a), RESULTS
      R39 (a)).
  (c) Lemma SG-EV: if k → k+1 is an in-phase transition with H1 at k, t0 ∈ R_k and t0 ∉ R_{k+1} (in particular any EV2 end), then
      Ξ_k(t0) ◁ Ξ_{k+1}(t0).
  (d) Lemma T0-PIN: in a phase with t0 ≠ o, if the EV2 end k → k+1 is the fallback g_j with j ≥ |U| − 1, then MoptÛ(t0) is defined
      and M_k(t0) = M_{k+1}(t0) = MoptÛ(t0) (HAT-FREEZE (b), (c), RESULTS R45 (b)).
  (e) Theorem NHN-BOUND: in a phase with t0 ≠ o, (a) there are at most 2·max(|U| − 2, 0) EV2 ends; (b) N_HN ≤ 1 + ⌈T/2⌉ +
      2·max(|U| − 2, 0) ≤ ⌈T/2⌉ + 2n − 3, with T ≤ n² + 2n − 1. For τ(o) = o the packet's remark cites RESULTS R39 (f) (c), which is
      landed for case A only; the bound for τ(o) = o follows from RESULTS R34 (e) with HN = H1 (NHN-N1 = N-NHN-1, citation, both
      referees; = RHO-N2 of RESULTS R45).
  (f) Remark H3-IN-HN: in a phase with t0 ≠ o and an HN state, every H2 state has H3, so every H1 ∧ H2 state of the phase satisfies
      (h) (H3-CONST, RESULTS R33 (a)). Its bookkeeping consequence holds with "there" read as "in a phase containing a Q state" (NHN-N2,
      wording; accepted by REFEREE-2).
  (g) Corollary HN-POLY-ALL: for every τ(o) and every phase, N_HN ≤ ⌈T/2⌉ + 2n − 3 = O(n²); ρ_HN ≤ (N_HN + |U| − 2)(|U| + deg(o) − 3) +
      deg(o) = O(n³); Σ_S θ_S ≤ ρ_HN + (ρ_HN + N_HN)·max(|U| − 2, 0) = O(n⁴); Σ_S B_S ≤ (ρ_HN + N_HN)(2n² − 1) = O(n⁵); Σ_S X_S ≤
      2(n − 1)(Σ_S B_S + N_HN) = O(n⁶); fallbacks from HN states ≤ K(Σ_S X_S + N_HN) + Σ_S X_S + N_HN = O(n⁸), K = n_E(2n − 1). Signed
      CONDITIONAL on P-N5-PFZ §1 ((A), (M1′), (M2′), FB-ROUND), P-N5-PFZ-ext BRK-POLY′ (i′) and (ii), and P-N5-RHO §2, §6. These conditions
      are now RESULTS R44 (a), (g) and R45 (b), (f), (g) (landed; R44 (g) includes the weak form (i′), which (g) uses); the τ(o) = o line
      as in (e).
- Not signed (packet §8, §9 and "What this closes", a GAPS reading): OPEN: fallbacks and crossings at Q states (only in phases without
  an HN state, by (f)); the global count f per phase as it enters SCOPE-COUNT (RESULTS R38 (c)) and X-SN-PHASE (RESULTS R34 (f));
  fallbacks at (h) states; S4a steps that change none of the counted quantities; the number of phases. This entry is not an iteration
  bound.
- Honest limits: (i) SUBCLASS 𝒞^1O, inside a phase. (ii) HN-POLY-ALL bounds what happens at HN states; OTHER states, (h)-state
  fallbacks, quiet S4a steps and wakes K are not bounded here, so G-N5-TIME stays open. (iii) Thin data: T0-PIN and NHN-BOUND (a)'s
  second branch (EV2 ends at g_j with j ≥ |U| − 1) are VACUOUS in all data of both referees and the lane (REFEREE's climbs reached
  j = |U| − 9 at best; REFEREE-2 found none even at j = |U| − 2), so they rest on their proofs; EV2-FB and SG-EV occur in the library
  and climbs only (random 𝒞^1O games reach no EV2 end); max N_HN 4 against bounds in the hundreds.
- Data (DATA, not proof; one Odd choice vertex asserted on every game): REFEREE (own nhn_probe.py on rl_engine): 253 𝒞^1O library games
  (990 phases; 76 with t0 ≠ o and an HN state; 30 τ(o) = o phases with HN states, 13 in case B) and the lane's 8 climb outputs: the
  packet's §9 totals reproduced exactly (84 phases, 8 EV2 ends, 395 H3 checks, N_HN 89 with max 4, 165 Q phases); climbs (1,882,532
  candidates): 1,022,295 EV2 ends checked, 35 DROPs ending an HN stretch, 0 failures. REFEREE-2 (own nhn_check.py): 4,428 library runs
  and 64,000 random 𝒞^1O runs, 159,084 phases (5,062 with t0 ≠ o and an HN state), 45 EV2 ends, 7,237 H3 checks, N_HN ≤ ⌊T_ph/2⌋ + 1 in
  1,252 case-A and 1,885 case-B τ(o) = o phases, 0 violations; mutation control nhn bites (10 violations), pin1 gives 0 (no EV2 end even at j = |U| − 2, so T0-PIN is not approached).
  Lane nhn.py: 0 failures of every check.
- Signatures: REFEREE docs/referee/R-N5-NHN.md (referee 9bb3f79, successor 10; §C 41b93026): T0U, EV2-FB, SG-EV, T0-PIN, NHN-BOUND,
  H3-IN-HN SIGNED (T0-PIN and NHN-BOUND conditional on P-N5-RHO's HAT-FREEZE, now RESULTS R45 (b)); HN-POLY-ALL SIGNED with
  exactly its conditions; notes NHN-N1..N3; no gaps. REFEREE-2 docs/referee-2/R2-N5-NHN.md (referee-2 04b5c1fd, successor 11; §C
  a41f2c13): all SIGN; HN-POLY-ALL SIGN CONDITIONAL as labelled; notes N-NHN-1, N-NHN-2; no gap. §C (both): verdicts identical; joint gap
  map empty; NHN-N1 = N-NHN-1; N-NHN-2 accepted by REFEREE; NHN-N2 accepted by REFEREE-2.
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.

### R47 [refereed-only] N5: cycle nodes only rise and Odd's dual cycle nodes only fall along a run, so every run has at most 2n(n − 1) + 1 joint λ-runs (Lemma Φ, every game), and on one-Odd-choice games τ changes at most deg(o) − 1 times and a run has at most n(n − 1) + deg(o) phases (Corollary Φ-1O) (2026-10-25) — partial step-4 lemmas for N5 (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C56.md, checker 5bb11d61)
- Object (packet P-N5-PHI, added at l-si af3a3b5a, pinned trunk 02ad3f88, unchanged during review): docs/si/P-N5-PHI-box14.md, sha1
  35e79ec1a91d0213b2b673779b69eb58a3e76b39 (L-SI successor 9, Opus 5.5). Its source is docs/new/N5-time-box21.md §2.3 (L-NEW box 21),
  which RESULTS R21, R23, R25, R27 and R28 call unrefereed; the packet re-proves it from landed results and governs where they differ.
  The referees' notes are collected by the lane in docs/si/P-N5-PHI-fixes-box14.md (l-si
  dfa14399, sha1 29936b3de0180322145b39fbfcd70ded780d2f76, L-SI successor 10: PHI-N1 = N-PHI-2, N-PHI-1, PHI-N2); on trunk; repairs only.
  Setting: N5 = SPEC S1-S5 of docs/new/N5-ssi-global.md; states (σ_k, τ_k); Ξ_k := Ξ_{σ_k} (Even's valuation, R15's Ω_σ), λ_k(v) its
  cycle node; U_k := Odd's valuation of τ_k in the dual game G^d (R38 (a)'s U_k), λ^U_k(v) its cycle node; reward(c) := p′(c) if Ω(c)
  is even, −p′(c) if odd, with p′(v) = 2·rank(v) + (Ω(v) mod 2) and rank injective (SPEC S1), so reward is injective on V. A JOINT
  λ-RUN is a maximal run of consecutive states with (λ_k, λ^U_k) constant. On 𝒞^1O, d := deg(o), and a PHASE is a maximal run with
  (λ_k, τ_k) constant (a joint λ-phase by RESULTS R38 (a) KEY).
- Claims signed (both referees "(Opus 5.5, D15)", L37); no item uses (P); landed premises only:
  (a) Lemma Φ (every game): (a) reward(λ_{k+1}(v)) ≥ reward(λ_k(v)) for every v and k, with equality iff λ_{k+1}(v) = λ_k(v) (RESULTS
      R15 (a), (d)); (b) reward(λ^U_{k+1}(v)) ≤ reward(λ^U_k(v)), with equality iff λ^U_{k+1}(v) = λ^U_k(v) (RESULTS R18 (d) Lemma S (b));
      (c) along a run at most n(n − 1) transitions change λ and at most n(n − 1) change λ^U, so a run has at most 2n(n − 1) + 1 joint
      λ-runs. S1 does not touch (b) (it concerns Lemma S (a)), and S2 is (b)'s own citation, a citation item and not open
      mathematics: R15 (a), (d) applied on G^d with R18 (d) Lemma R (PHI-N1 = N-PHI-2, citation, both referees); G-1OA-6 concerns
      Lemma S (c)-(d) and is not used.
  (b) Corollary Φ-1O (𝒞^1O): (a) along any N5 run τ changes at most d − 1 times (the τ's form a strict ≺_{G^d}-chain by R15 (c), (d)
      on G^d, so no τ repeats; N-PHI-1); (b) a run has at most n(n − 1) + d phases.
- Not signed (packet §2 "Use", §3): the READING that with Φ-1O a polynomial bound for N5 on 𝒞^1O needs only a polynomial bound on the
  length of one phase (docs/si/N5-LEDGER-box14.md, docs/si/N5-FBPHASE-box14.md); the packet's data.
- Honest limits: (i) Lemma Φ holds on every game but bounds only λ- and λ^U-changes, not iterations; Corollary Φ-1O is on 𝒞^1O. (ii)
  Nothing here bounds the length of a phase, so G-N5-TIME stays open. (iii) Φ-1O (a)'s bound d − 1 is reached in data (REFEREE-2:
  1000‰, library and random), so it is tight.
- Data (DATA, not proof): REFEREE (own probe phifx_probe.py on rl_engine): 367 library games (any game; 253 𝒞^1O) and 8,000 random
  games (half general n 3-10, half 𝒞^1O n 4-14; 4,995 𝒞^1O): Φ (a) and (b) 278,285 + 57,066 checks each, λ^U checked directly (PHI-N2),
  joint λ-runs at most 15.3% of the bound, max 29 phases, 0 failures. REFEREE-2 (own phi_check.py): 492 𝒞^1O files × 3 tracers (own / rand / spec) × 3 starts (4,428 runs)
  and 64,000 random 𝒞^1O runs, 1,484 logs OK: 3,219,607 checks each of (a) and (b), 0 drops / 0 rises; phases at most 375‰ of
  n(n − 1) + d (max 30); mutation control ub bites (2,385 violations). Lane phicheck.py: 590 traces, 427,644 reward checks, 0 drops
  (λ^U not checked).
- Signatures: REFEREE docs/referee/R-N5-PHI.md (referee 843ba1f8, successor 10; §C 37608e06 + count fix 92628d03): Lemma Φ (a)-(c),
  Corollary Φ-1O (a), (b) SIGNED; notes PHI-N1, PHI-N2; no gaps. REFEREE-2 docs/referee-2/R2-N5-PHI.md (referee-2 b621f9af, successor
  11; §C f8cb3ef3): all SIGN; notes N-PHI-1, N-PHI-2; no gap. §C (both): verdicts identical; joint gap map empty; N-PHI-2 = PHI-N1's
  recommendation and N-PHI-1 accepted by REFEREE; REFEREE's general-game data cover REFEREE-2's thin spot ("every game").
- TARGET.md diff: not a claim of TARGET.md section 1 (Lemma Φ bounds cycle-node changes of N5 on every game, not its running time).
  GAPS G-N5-TIME: open.

### R48 [refereed-only] N5 on one-Odd-choice games: in every phase the in-phase Even fallbacks number at most 1 + (|U| − 2)(|succ(o) ∩ Û| + |U|) ≤ 1 + (n − 2)(2n − 1) if o ≠ c_θ, and at most |U| if o = c_θ, with no hypothesis on H1, H2, H3, τ(o), c_w, θ or N_HN: each fallback is a Bellman-Ford round for κ on U (κ-FB-ROUND, κ-HAT-FREEZE, κ-PFZ, κ-Y-FORM), a switched vertex exits to a terminal (EXIT-SWITCH), late fallbacks switch nothing in U ∖ T (FREEZE-EXIT), the rest are one CN-LAST fallback (CN-ONLY), and θ changes few times after the freeze (THETA-AFTER) (Theorem FB-POLY) (2026-10-25) — partial step-4 lemmas for N5 (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C57.md, checker 6b15a543)
- Object (packet P-N5-FBPOLY, added at l-new 4a17f8e1, pinned trunk 42d8c3a9, unchanged during review): docs/new/P-N5-FBPOLY-box41.md,
  sha1 de244dcd3592b04eca2080a0efe10a7c0b2e5301 (L-NEW successor 20, Opus 5.5). It restates in κ form, with proofs, the facts of P-N5-PFZ
  §1 and P-N5-RHO §0-§2 it uses (now RESULTS R44, R45), so it does not depend on their landing. The referees' repairs and notes are
  collected by the lane in docs/new/P-N5-FBPOLY-fixes-box41.md (l-new 5e1b5ea0, sha1 c016c1906b197b41d1be35ab64ea0908f030b2ca, L-NEW
  successor 21: FBP-1 = N-FBP-2, FBP-N1, FBP-2 = N-FBP-1, FBP-N2, FBP-N3 = N-FBP-3 (scope part), FBP-N4, N-FBP-3 (data part), N-FBP-4);
  on trunk; repairs only.
  Setting as in RESULTS R39, R44 and R45 (𝒞^1O; phase; θ, c_θ; R_k, R̄_k, F_k; H1; U := λ^{-1}(c_θ), Û := U ∖ {o}; wt; G_Û; g_1 < g_2 < …
  the in-phase Even S4c fallbacks of the phase; a θ-run Θ and its in-run fallbacks f^Θ_1 < f^Θ_2 < …). T := {o, c_θ} (the TERMINALS);
  deg_U(o) := |succ(o) ∩ U|; s_θ := +1 if Ω(c_θ) is odd, −1 if even; for z ∈ U, κ_t(z) := (M_t(z), s_θ·ℓ(Ξ_t z)), ordered
  lexicographically, with M_t(z) the signed weight of P(Ξ_t z); κwt(v) := (wt(v), s_θ), κwt(A) := Σ_{v∈A} κwt(v); κoptÛ(z) :=
  max{κwt(p ∖ {c_θ}) : p a simple path of G_Û from z to c_θ}; G_U^o: the graph on U ∖ {c_θ} in which every Even v keeps its edges into
  U ∖ {c_θ}, every Odd v ≠ o keeps its forced edge if it lies in U ∖ {c_θ}, and o is a sink; G_U as in RESULTS R44. At a fallback
  k → k+1: S_k the switched Even vertices (the gate sources), x*_v := σ_{k+1}(v), S_U := S_k ∩ (U ∖ T); Y_t := succ(o) ∩ U ∩ F_t.
- Claims signed (both referees "(Opus 5.5, D15)", L37); no item uses (P); no hypothesis on H1, H2, H3, τ(o), c_w or N_HN:
  (a) Lemma κ-FB-ROUND: at an in-phase Even fallback k → k+1, κ_{k+1}(v) ≥ κwt(v) + κ_k(x) for every Even v ∈ U ∖ {c_θ} and every
      successor x ∈ U of v.
  (b) Lemma κ-HAT-FREEZE: in a phase, (a) for j ≥ 0, every state t > g_j, z ∈ Û and simple path p of G_Û from z to c_θ with ≤ j edges,
      κ_t(z) ≥ κwt(p ∖ {c_θ}); (b) for every state t and z ∈ F_t ∩ U, κoptÛ(z) is defined and κ_t(z) ≤ κoptÛ(z); (c) if |U| ≥ 2,
      κ_t(y) = κoptÛ(y) for every state t > g_{|U|−2} and every y ∈ F_t ∩ U.
  (c) Lemma κ-PFZ: if o ≠ c_θ and Θ is a θ-run of the phase, then for j ≥ 0, every t ∈ Θ with t > f^Θ_j (every t ∈ Θ if j = 0), every
      z ∈ U ∖ {c_θ} and every simple path p of G_U^o from z to o with ≤ j edges, κ_t(z) ≥ κwt(p ∖ {o}) + κ_t(o).
  (d) Lemma κ-Y-FORM: at an H1 state t, σ̄_t(o) ∈ Y_t and κ_t(o) = κwt(o) + min_{y∈Y_t} κ_t(y).
  (e) Lemma EXIT-SWITCH: at an in-phase Even fallback k → k+1 with S_U ≠ ∅, some u ∈ S_U has the property that the honest play at k
      from x*_u visits a vertex of T before it visits u; with e the first such vertex and p_u := u · (that play up to e), p_u is a
      simple path from u to e, a path of G_Û if e = c_θ and of G_U^o if e = o, and κ_k(x*_u) = κwt(p_u ∖ {u, e}) + κ_k(e). (The
      excluded "loop" branch DOES occur for some switched vertices, N-FBP-4: witness docs/referee-2/R2-N5-FBPOLY/climb/loop_4102.pg,
      sha1 016473b4, re-run by REFEREE; the lemma's "some u exits" is what holds.)
  (f) Lemma FREEZE-EXIT: if o ≠ c_θ and k = g_j is an in-phase Even fallback that is the i-th fallback of its θ-run (k = f^Θ_i), with
      j ≥ |U| − 1 and i ≥ |U| − 1, then S_U = ∅.
  (g) Lemma CN-ONLY: at an in-phase Even fallback with S_U = ∅, every gate (y, z) ∈ Iσ_k has λ_k(y) = y and lev(Ξ_k(σ_k y), Ξ_k(z)) = −1;
      hence (CN-LAST, RESULTS R38 (f)) k + 1 is the last state of its phase, and a phase has at most one such fallback.
  (h) Lemma THETA-AFTER: if o ≠ c_θ and the phase has at least |U| − 2 in-phase Even fallbacks, at most deg_U(o) + |U| − 2 of its
      transitions t → t+1 with t > g_{|U|−2} change θ, so at most deg_U(o) + |U| − 1 θ-runs of the phase contain a state t > g_{|U|−2}.
      Its proof ranges over y ∈ succ(o) ∩ Û, so it holds with |succ(o) ∩ Û| ≤ |U| − 1 in place of deg_U(o) (FBP-N1).
  (i) Theorem FB-POLY: with f the number of in-phase Even S4c fallbacks of a phase of N5 on 𝒞^1O, (a) if o ≠ c_θ, f ≤ 1 + (|U| − 2)·
      (deg_U(o) + |U|), and f ≤ 1 + (|U| − 2)(|succ(o) ∩ Û| + |U|) ≤ 1 + (n − 2)(2n − 1); (b) if |U| = 2, f ≤ 1; (c) if o = c_θ, f ≤ |U|;
      (d) at most one fallback has S_U = ∅, and it is followed by the last state of the phase. The packet's end bound used deg_U(o) ≤
      n − 1, false when o has a self-loop and succ(o) ⊇ U = V; the repair replaces deg_U(o) by |succ(o) ∩ Û| (FBP-1 = N-FBP-2, both
      referees, independently). The packet's proof of (b) covers only o ≠ c_θ; for o = c_θ and |U| = 2 the other vertex v has next(v) = o
      at every state and can never switch, so S_U = ∅ and (d) gives f ≤ 1 (FBP-2 = N-FBP-1, both referees, independently).
- Not signed (packet §7, §8, §6 Remarks): CONJECTURE FB-CAP (L-RED successor 17: f ≤ max(1, |U| − 2) in every phase), proved here only
  for |U| ≤ 2, OPEN for |U| ≥ 3, with its routes (FB-CAP-1), (FB-CAP-2) OPEN; §7's question whether EXIT-SWITCH's excluded branch can occur
  for SOME switched vertex is answered by data: it does (N-FBP-4; the packet's "never occurs in data" is out of date); the Remarks' consequences (f removed from
  SCOPE-COUNT, EPOCH, X-SN-PHASE) are READINGS (FBP-N3 = N-FBP-3).
- Honest limits: (i) SUBCLASS 𝒞^1O, inside a phase. (ii) FB-POLY bounds fallbacks per phase; S4a steps, crossings, OTHER-touching
  transitions and wakes K are not bounded here, so G-N5-TIME stays open. (iii) UNTESTED BY DATA: the hypotheses of FREEZE-EXIT and
  THETA-AFTER (a fallback g_j with j ≥ |U| − 1 at |U| ≥ 3) never occur in the data of either referee or the lane (REFEREE: 3.82 M climb
  candidates, best one fallback short; REFEREE-2: 1,484 batch logs and 1.92 M climb runs; L-RED R71), so FREEZE-EXIT, THETA-AFTER and
  FB-POLY (a) beyond FB-CAP rest on their proofs; max f per phase in data 37 (|U| 48).
- Data (DATA, not proof; one Odd choice vertex asserted on every game): REFEREE (own fbpoly_probe.py, fbpoly_climb.py on rl_engine):
  P-N5-RHO's 412-file list (253 𝒞^1O), 990 phases, 660 fallbacks (21 with S_U = ∅, 639 with S_U ≠ ∅), the packet's §8 (L) figures
  reproduced (except the κ-PFZ count, by convention); with 4 random start pairs 5,240 phases, 1,313 fallbacks; climbs 3,822,173 candidates (2,815,066 fully checked:
  κ-HAT-FREEZE (a) 4,646,931, (c) 3,140,099, κ-PFZ 1,197,169 exact checks); 0 failures. REFEREE-2 (own fbpoly_check.py): 4,428 library
  runs and 64,000 random 𝒞^1O runs, 159,383 phases (7,357 with o = c_θ and |U| = 2, max f 1), 8,643 fallbacks, (Aκ) 3,001,987,
  κ-Y-FORM 139,928, κ-PFZ 104,199 exact checks; climbs 1,922,112 runs (31 loop-kind switched vertices); 0 violations. Lane fbpoly.py:
  (L) and 13,364 random runs, 0 failures. L-RED successor 18 (docs/red/R72-fx-fbpoly-k.md, l-red 6e28e4f1; own fbx18.py from the
  frozen texts): library and 8,546,164 random runs, 0 FAIL; the loop kind at 10 of 1,709 switched vertices of U ∖ T (witness
  experiments/red/fbx/instances/exsw_loop_n15.pg, sha1 e38329f8, from the start pair in exsw_loop_n15.start.json; Lead re-run from the canonical start, where the run has no
  fallback: one Odd choice vertex, n5 1/0, Oink zlk OK strategies verified); FREEZE-EXIT's hypothesis never reached.
- Signatures: REFEREE docs/referee/R-N5-FBPOLY.md (referee 3de7cab, successor 10; §C d6248f7b): κ-FB-ROUND, κ-HAT-FREEZE (a)-(c),
  κ-PFZ, κ-Y-FORM, EXIT-SWITCH, FREEZE-EXIT, CN-ONLY, THETA-AFTER, FB-POLY (a) first bound, (c), (d) SIGNED; FB-POLY (a) end bound
  SIGNED WITH GAP FBP-1 and (b) SIGNED WITH GAP FBP-2, each repaired in one line; in §C, with both repairs in the fixes file, FB-POLY (a)
  and (b) SIGNED without a gap; notes FBP-N1..N4. REFEREE-2 docs/referee-2/R2-N5-FBPOLY.md (referee-2 2fef7c4a, successor 11; §C
  75372604, successor 12): all SIGN, no gap; notes N-FBP-1 ((b) at o = c_θ), N-FBP-2 ((a)'s end bound with a self-loop), N-FBP-3, N-FBP-4;
  in §C it accepts REFEREE's form: with the two one-line repairs in the fixes file, both referees sign FB-POLY (a)-(d) unconditionally.
  §C (both): verdicts identical in substance; FBP-1 = N-FBP-2 and FBP-2 = N-FBP-1, found independently with the same repairs; joint gap
  map one row, closed by the agreed repairs; FBP-N2 accepted by REFEREE-2; N-FBP-4 accepted and re-run by REFEREE.
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.

### R49 [refereed-only] N5 on one-Odd-choice games: a gate into F along an optimal F-play has level ≥ r (XG), one-player valuations do not rise under non-improving or exceptional edges (ANTI, every one-player game), at an in-scope THR fallback with M = −1 and r ≥ 0, Even's best reply to τ from the threat x0 uses a (β) gate (NEED-β), an old threat stays in R after a rise (OLD-THREAT), and CONJECTURE INTO would exclude a later fallback (reduction); the CONJECTURE "in scope, THR ⇒ M ≥ 0" is FALSE (2026-10-25) — partial step-4 lemmas for N5 (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C58.md, checker a58dcd3a)
- Object (packet P-N5-NEEDB, added at l-si 3ea0f5f9, pinned trunk e6ee6130, unchanged during review): docs/si/P-N5-NEEDB-box13.md, sha1
  7471aef37f9ad2a746dbc63451a5543b3917a443 (L-SI successors 7 (§1-§3 cases (B), (A1), (A2′), (A2″)) and 8 (the rest), Opus 5.5). The
  referees' notes are collected by the lane in docs/si/P-N5-NEEDB-fixes-box13.md (l-si 863ca636, sha1
  0e5f24af086c54609c1a2233e6b1c485a0bf442c, L-SI successor 10: NEEDB-N1..N4, N-NEEDB-1..5, R71 §4's INTO wording); on trunk; repairs only.
  Setting as in RESULTS R31, R35, R37, R40 and R41 (𝒞^1O; scope run S; S4a / S4c; Ξ, W; gates, gate levels, M_k; COARSE_L, (C1)-(C7);
  R̄ / R / F; (h); r; THR; phase; c; the gate kinds (α), (β), (γ) of R41 (a)). x0 := σ̄_k(o), t := τ(o). G_τ: the one-player game "Odd
  fixed to τ", U := Opt(G_τ) its pointwise optimum, σ* an optimal strategy of G_τ (V_{σ*,τ} = U). An Even edge (v, u) of a one-player
  game with σ-valuation V is V-EXCEPTIONAL if v is its own V-cycle node, u ≠ σ(v) and V(u) = (v, ∅, ·). SETTING (LV+): setting (LV) of RESULTS R41 with r_k ≥ 0, i.e. k is an in-scope S4c fallback, THR at
  k with u* ≠ none, and M_k = −1 (by LV-SHAPE every gate is (α) or (β)); 𝒫 is the σ*-play from x0 in G_τ. RISE SETTING (packet §4): k0 an in-scope
  fallback of S with L := M_{k0} ≥ 0, j > k0 the first S4a step after k0 that changes COARSE_L(θ); between k0 and j there is no fallback,
  every transition is in S, and r > L; a POST-RISE STATE is a state t > j such that every transition s → s+1 with k0 < s < t is an in-scope S4a step with r_s > L.
- Claims signed (both referees "(Opus 5.5, D15)", L37); no item uses (P) beyond what RESULTS R36 discharges:
  (a) Lemma XG: let k be an in-phase THR S4c fallback with (h), y ∈ R_k Even, s := σ_k(y) and z := σ*(y) ∈ F_k, where z's (σ*, τ)-play
      stays in F_k. Then (y, z) is a gate at k of level ≥ r_k. "In particular M_k ≥ r_k" holds when such a y exists (NEEDB-N1, wording).
  (b) Lemma ANTI (every one-player game): if H is a one-player game, σ an Even strategy with valuation V, and σ′ chooses at every Even
      vertex v either an edge (v, u) with V(u) ⊴ V(σ v) or a V-exceptional edge, then V_{σ′} ⊴ V pointwise; and its instances ANTI-Ξ,
      ANTI-W.
  (c) Corollary NEED-β: in setting (LV+), 𝒫 uses an edge (y, σ*(y)) that is a (β) gate. The cases (B) 𝒫 avoids o, (A1) 𝒫 visits o and
      its cycle avoids o, (A2′), (A2″) and (A2*) (𝒫's cycle contains o, by where its top lies) are exhaustive.
  (d) Lemma OLD-THREAT: if t is a post-rise state and x ≠ o is an exit of o with x ∈ F_{k0} and COARSE_L(o ⊕ Ξ_{k0} x) =
      COARSE_L(θ_{k0}), then x ∈ R_t; in particular the k0-threat σ̄_{k0}(o) lies in R_t.
  (e) Reduction: CONJECTURE INTO ("at every post-rise state t with r_t > L, some gate (y, z) has z ∈ R̄_t", read at states with
      Iσ_t ≠ ∅, R71 §4; fixes) implies that no case (i)
      fallback occurs, i.e. no later fallback k of S with r > L on [k0 + 1, k]; "case (i)" is read as the NEXT fallback of S after k0
      (N-NEEDB-2 = NEEDB-N2), and R20 (b) FBL's "no F → R and no R → R gate" is read in R19's notation, where R contains o (NEEDB-N3).
- Not signed (packet §5): CONJECTURE INTO (OPEN); case (ii) of the rise question, r ≤ L before the next fallback (OPEN); the dead
  conjectures RISE-DROP, GATE-ABOVE, FEED (FALSE, recorded in docs/si/DEAD.md, box 13; instances tevlast7_n32, rise_thin51_n40,
  tevlast11_n40). The CONJECTURE "in scope, THR ⇒ M ≥ 0"
  (docs/si/N5-LV3-box12.md §4-§5; RESULTS R41, R43, not signed) is FALSE (N-NEEDB-5): docs/referee-2/R2-N5-LV2/climb/block_9501.pg
  (sha1 1b5b76fd), from the start pair in block_9501.txt, state 1: (h), θ = (5, {9}, 3) ◁ w = (5, ∅, 1), r = 10, M = −1, gates (10, 1),
  (10, 3), (10, 8), all (β) (rank o 2 < rank c 9), k → k+1 in scope; reproduced on REFEREE-2's three traces, confirmed on REFEREE's engine (§C C.3, referee 7dbd5118) and on L-SI's
  (experiments/si/needb5/repro.py, l-si 34e5225a). From
  the canonical start the run has no such state (RESULTS R43 limit (iii)). At this counterexample NEED-β holds: 𝒫 uses the (β) gate
  (10, 8), case (B). Recorded FALSE in docs/si/DEAD.md box 15 (l-si adf80994); the S3-start form survives there as a weak CONJECTURE.
- Honest limits: (i) SUBCLASS 𝒞^1O except (b). (ii) These lemmas locate the (β) gate of any M = −1 fallback and reduce case (i) to INTO;
  they bound no count, so G-N5-TIME stays open. (iii) Thin data: XG's hypothesis is VACUOUS in both referees' batch data and occurs 7 times
  only in REFEREE-2's climbs (N-NEEDB-4: its first saved start pair was invalid, so REFEREE could not
  reproduce it, §C C.4; REFEREE-2's Addendum A, referee-2 1a9a0407, pins a valid start pair and an optimal σ*, and its rng-free
  xg_witness.py gives RESULT OK; the hypothesis holds for some optimal σ*, not for the deterministic one); NEED-β's cases (A1), (A2′), (A2″), (A2*) never occur in setting (LV+) (every (LV+) state in
  data is case (B)), so they rest on their proofs; random-seeded climbs (REFEREE-2 12002, 12005) reach neither (LV+) nor a rise.
- Data (DATA, not proof; one Odd choice vertex asserted on every game): REFEREE (own needb_probe.py on rl_engine): P-N5-RHO's 412-file list
  (253 𝒞^1O) from SPEC S3's start and with 4 random start pairs, REFEREE-2's 145 climb outputs, 1,400 random-start runs on the LV2
  witnesses and beta2_n11, and block_9501 from its own start pair: in-scope THR fallbacks with r ≥ 0 985 + 398 + 434 + 1, setting (LV+)
  exactly once (block_9501, (β) gate (10, 8)), NEED-β's stronger form (NEEDB-N4: 𝒫 uses a gate that is not Ξ-exceptional, at every THR
  fallback with (h) and r ≥ 0) at each of them, XG 0 cases, OLD-THREAT 510 exit checks, INTO 52 / 52, ANTI 100,000 random checks; 0 failures. REFEREE-2
  (own needb_check.py): 5,904 library runs and 3,000 random runs, 0 violations; six climbs: 297,752 (LV+) states, every one case (B) with a
  (β) gate on 𝒫, XG hypothesis 7 times, OLD-THREAT 57,988 exit checks at 38,664 post-rise states, INTO 1,492 / 1,492, case (i) 0, 0
  violations; mutation controls xg, otc, b0, anti fire, otf does not.
- Signatures: REFEREE docs/referee/R-N5-NEEDB.md (referee 008ad8ab, successor 10; §C 7dbd5118, successor 11): XG, ANTI (+
  ANTI-Ξ, ANTI-W), NEED-β (B), (A1), (A2′), (A2″), (A2*), OLD-THREAT, the reduction SIGNED; notes NEEDB-N1..N4; no gaps. REFEREE-2
  docs/referee-2/R2-N5-NEEDB.md (referee-2 ef433d32, successor 12; Addendum A 1a9a0407: witness start pairs corrected,
  four lines of §1 / §6 marked "corrected in Addendum A", no verdict change): all SIGN; notes N-NEEDB-1..5; no gap. REFEREE-2 discloses that, after
  its verdicts and notes were written, a repository grep printed two lines that report on REFEREE's R-N5-NEEDB (LEAD-STATE l. 1410, RESULTS R43
  limit (iii)); it changed no verdict or note after that and did not open docs/referee/. §C (REFEREE): verdicts identical; joint gap map empty;
  NEEDB-N2 = N-NEEDB-2; N-NEEDB-1 = REFEREE's IN-DATA line; N-NEEDB-3 accepted; N-NEEDB-5 confirmed; N-NEEDB-4 accepted as REFEREE-2's
  data but NOT reproduced by REFEREE (the saved start pair of witness_xg_12004 is not a strategy pair of that game); corrected in
  REFEREE-2's Addendum A (1a9a0407).
  §C (REFEREE-2, fafea30e, successor 12): verdicts identical; NEEDB-N1, NEEDB-N3 and NEEDB-N4 (checked) accepted; NEEDB-N2 = N-NEEDB-2;
  C.3 = N-NEEDB-5; C.4 correct, repaired in Addendum A. Joint gap map empty; no disagreement remains.
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.

### R50 [refereed-only] N5 on one-Odd-choice games: above the more relevant cycle node m*, routes freeze after |R| − 1 transitions of every fallback-free run of every stretch (FRZ-U), kinds change at most once and only B → A after the freeze (KIND-MONO, with PAR: c_w ≻ c_θ forces c_w even), so the Ξ-changes on R of a run are ≤ 3Δ·r⁴ (Theorem RUN), (K_W), (E) and wakes K are polynomial per stretch given its fallbacks (Corollary KW-S), and the transitions of a phase are ≤ an explicit polynomial in n, m and its fallbacks f (Corollary PHASE) (2026-10-25) — partial step-4 lemmas for N5 (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C59.md, checker a58dcd3a)
- Objects (one review unit; both unchanged during review): packet P-N5-KW, docs/si/P-N5-KW-box15.md, sha1
  c0b0111fcc2259e4ed9d43647bc4fa08cec452a5 (added at l-si bf1ed0f7), and its addendum docs/si/P-N5-KW-addendum-box15.md, sha1
  8d6bfb3c32d80ed7040df4ae2dee56bb9bb9b5bd (added at l-si 47c4e7a2: every count is a TRANSITION count; switches ≤ n · transitions),
  both pinned trunk d9291be0 (L-SI successor 10, Opus 5.5; Lemma PAR and four additions from L-NEW successor 21's cross-read). The
  referees' notes are collected by the lane in docs/si/P-N5-KW-fixes-box15.md (l-si 1d33a337, sha1
  c65f4c1e31b437f66e19cef2ff29cec66b212bdc, L-SI successor 10: KW-1 = N-KW-3, KW-N1..N5, N-KW-1..6, REFEREE's Addendum 1); on trunk;
  repairs only.
  Setting as in RESULTS R24, R26, R27 and R38 (𝒞^1O; phase = joint λ-phase; S4a / S4c; Ξ, W; θ, w, c_θ, c_w; H1, H2; R = R_k (o ∈ R),
  r := |R|, F := V ∖ R, routes π_v; crossings; route form; R26's classes U1, U2, U3, U23 and kinds A / B (under ¬H2 with c_w ≠ o, v is of
  kind A iff c_w ∈ π_v); W-flat runs). A STRETCH is a maximal run of states of a phase with R, θ, w constant; a RUN of a stretch is a
  maximal run of its consecutive non-fallback transitions. m* := the more relevant of c_θ and c_w (c_θ if equal); κ(ρ) := ρ ∩ V_{>m*},
  κ_k(v) := κ(π_v^k). Δ := the maximum out-degree, d_o := |succ(o)|, m := #edges.
- Claims signed (both referees "(Opus 5.5, D15)", L37); no item uses (P); every premise is LANDED (R15, R17, R18 (d), R19, R21 (a) XW, R22, R23
  (g), R24, R26, R27, R30 (c), R34 (e), (f), R38 (a)):
  (a) Lemma W-ONCE (every game): if k → k+1 → k+2 are two consecutive S4a transitions of one phase with Ξ_{k+1} = Ξ_k, then
      W_{k+2} = W_{k+1}; and Corollary W-ONCE′.
  (b) Facts A0, A, B (on a stretch): values on R are route values with constant terminals (A0); P(Ξ(v)) ∩ V_{>m*} = κ(π_v) ⊔ C_Ξ and
      P(W(v)) ∩ V_{>m*} = κ(π_v) ⊔ C_W with C_Ξ, C_W constant and disjoint from π_v (A); for y, z ∈ R with κ(π_y) ≠ κ(π_z),
      Ξ(y) ◁ Ξ(z) ⟺ W(y) ◁ W(z) ⟺ κ(π_y) ≺ κ(π_z) (B).
  (c) Lemma FRZ-U: on a run S of a stretch (states k0, …), κ_t(v) = κ_{k0+r−1}(v) for every state t ≥ k0 + r − 1 of S and every v ∈ R.
      Its proof is self-contained (Claim P^c, cases A, B1, B2, B3); it does not rest on a transfer of R20 CR (REFEREE §3).
  (d) Corollary LEN: after k0 + r − 1, the frame whose cycle node is m* changes on R only by lengths, monotonically.
  (e) Lemma PAR (L-NEW successor 21): at every state of a phase on 𝒞^1O, if c_w ≻ c_θ then Ω(c_w) is even (R21 (a) XW).
      Lemma H-PATH: on a stretch with ¬H2, c_w ≠ o and c_w ≻ c_θ, for v ∈ R ∖ {o}, c_w ∈ P(Ξ(v)) iff v is of kind A.
      Lemma KIND-MONO: in a run of such a stretch, after k0 + r − 1 every v ∈ R ∖ {o} changes kind at most once, and only from B to A.
      Lemma CASC-B: in a W-flat segment of a U3 / U23 stretch with no kind change (c_w and kind-A vertices may switch), a kind-B vertex v
      switches only at steps ≤ |π_v| − 2.
      Lemma CW-INT: in a run of a stretch with ¬H2 and c_w ≠ o, between two states with no kind change and no kind-B switch in
      between, c_w switches at ≤ deg(c_w) − 1 transitions.
      Proposition E-SEG (ii)-(v) on a post-freeze W-flat segment Q of a U3 / U23 stretch with c_w ≻ c_θ, with N_cut(Q) := the transitions
      of Q with a kind change or a kind-B switch ≤ (e(Q) + 1)(r − 1). E-SEG (i) as written (N_B(Q) ≤ (e(Q) + 1)(r − 2) over all
      kind-B-switch transitions) is not proved: a kind-change transition can also carry a kind-B switch; the proof gives
      N_B(Q) ≤ e(Q) + (e(Q) + 1)(r − 2); with N_B(Q) redefined as the kind-B-switch transitions WITHOUT a kind change, (i) holds,
      N_cut (counted once) ≤ (e(Q) + 1)(r − 1) − 1, and (ii)-(iv) and Theorem RUN use only N_cut (KW-1 = N-KW-3, both referees,
      independently; fixes).
  (f) Theorem RUN: on a run of a stretch, the transitions with a Ξ-change at some vertex of R number ≤ 3Δ·r⁴: ≤ (r − 1)² if
      c_θ ⪰ c_w; ≤ r³ if c_w ≻ c_θ and the W frame is in route form; ≤ (r − 1)² + (Δr + 1)(2r − 3)·r² ≤ 3Δ·r⁴ on U3 / U23 with
      c_w ≻ c_θ (for r ≥ 2; KW-N3 = N-KW-4).
  (g) Corollary KW-S: a stretch with f_st fallback transitions has ≤ (f_st + 1)·n² non-fallback transitions with a W-change on R ((K_W)),
      polynomially many event transitions per W-flat run ((E); explicit per run: ≤ (r − 1) + (Δr + 1)(r − 1)², KW-N4 = N-KW-6), and
      K ≤ T_rel (wakes counted as transitions).
  (h) Corollary PHASE (CONDITIONAL on f only): a phase on 𝒞^1O with f fallback transitions has T ≤ (m − n + 1)(T_rel + 1) transitions,
      with T_rel ≤ S_o + N_Ξ, N_Ξ ≤ f + (N_st − 1) + (X + 1)(n − 1) + (N_st + f)·3Δn⁴, N_st ≤ 1 + X + Θ + W_ch and the landed bounds on X
      (R30 (c), R34 (e), (f)), Θ and S_o (R27 (g)) and W_ch (R24 (e), F1°); so T = O(m·Δ·d_o·n⁹·(f + n²)).
- Not signed (packet §8 READINGs, §9-§11): with FB-POLY (RESULTS R48), T = O(m·Δ·d_o·n¹¹) per phase; with Corollary Φ-1O (RESULTS R47)
  and a polynomial bit cost per iteration, N5 on 𝒞^1O would make polynomially many iterations (a READING here, to be packeted and
  refereed as an assembly); the lane notes docs/si/N5-KW-box15.md (5ebbb3b6) and docs/new/N5-KW-box42.md v3.2 (349d553c), two independent
  lane proofs. No polynomial bound for N5 on 𝒞^1O is proved by this entry; the assembly (P-N5-1O) is not yet refereed.
- Honest limits: (i) SUBCLASS 𝒞^1O, inside a phase; Corollary PHASE is conditional on f. (ii) Thin data: no post-freeze kind change and no post-freeze c_w switch occurs in
  any data (REFEREE: 0 in 2.46 M post-freeze U3 / U23 transitions with c_w ≻ c_θ; REFEREE-2; L-RED R73; both lanes), so KIND-MONO,
  CW-INT after the freeze and E-SEG's post-freeze counts rest on their proofs; W-ONCE's hypothesis: 2 checks on REFEREE's engine, 571 in
  REFEREE-2's climbs; CASC-B's hypothesis is exercised on REFEREE's engine (Addendum 1, cascb_witness.pg, one step below its bound), in
  REFEREE-2's climbs (10 cases, the latest at step |π_v| − 2, the bound) and twice in L-RED's runs (R73 §7 random, at step |π_v| − 4, two
  below the bound, not pinned; §8 on REFEREE's witness); the c_w-odd branches are empty by PAR. (iii) FRZ-U's index |R| − 1 and CW-INT's deg(c_w) − 1 are attained in
  data (L-RED R73: frzu_tight_n14, cw11_n24).
- Data (DATA, not proof; one Odd choice vertex asserted on every game): REFEREE (own kw_probe.py, kw_climb.py on rl_engine): library 253
  games × 4 starts and climbs (2.24 M evaluations): Corollary PHASE inequalities 2.77 M phases, H-PATH 21.9 M vertex-states, PAR 5.1 M
  states, CW-INT 413k c_w switches, CASC-B 687k kind-B switches; 0 failures. REFEREE-2 (own kw_check.py, kw_climb.py): batch 503 files × 3 starts × 3
  traces (4,527 runs) and 3,000 random runs, climbs 160,163 evaluations (640,652 runs); 0 violations; 1.15 M kind changes and 157,577
  c_w switches with c_w ≻ c_θ, ¬H2, all BEFORE the freeze index; CASC-B exercised 10 times, the latest at step exactly |π_v| − 2
  (not saved; two later climbs saved witnesses witness_cascb_13011.pg, witness_cascb_13012.pg, one step below the bound); FRZ-U's κ changes as late as run step 39 on kw_n48.pg
  (N-KW-5; index r − 1 = 47 never exceeded); mutations frz0 and par fire, casc does not on saved data. L-RED successor 18
  (docs/red/R73-*.md, l-red 896aea76; own kw18 tools): lib41 and 4,267,132 random runs, 0 FAIL; PAR 0 odd cases in 1.24 M qualifying
  states. Lane (kwcheck.py, kwclimb.py): ~13 M states, 0 failures.
- Signatures: REFEREE docs/referee/R-N5-KW.md (referee 56ac6538, successor 11; Addendum 1 1d6cbf32; §C a6e50742 + stamp fix 776281ac): W-ONCE, Facts A0 / A /
  B, FRZ-U, LEN, PAR, H-PATH, KIND-MONO, CASC-B, CW-INT, RUN, KW-S, PHASE SIGNED; E-SEG SIGNED WITH GAP KW-1 (one-line repair); notes
  KW-N1..N5. REFEREE-2 docs/referee-2/R2-N5-KW.md (referee-2 8a47fd92, successor 12; §C 20fea7d7): all SIGN, no gap; notes N-KW-1..6.
  §C (both): verdicts identical; joint gap map one row, KW-1 = N-KW-3, found independently and closed by the definitional repair;
  KW-N3 = N-KW-4, KW-N4 = N-KW-6, KW-N5 = N-KW-5; N-KW-1, N-KW-2 (CW-INT step 1 reads "kind B or o") accepted by REFEREE; KW-N1, KW-N2
  accepted by REFEREE-2; REFEREE's CASC-B witness reproduced on REFEREE-2's SPEC trace. No disagreement remains.
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open.

### R51 [refereed-only] N5 solves one-Odd-choice parity games in polynomial time: from any start pair it stops after at most (n(n − 1) + d_o)(T* + 1) = O(m·Δ·d_o·n¹³) iterations (Theorem 1O-POLY), each iteration and the output step cost polynomially many bit operations (Lemma BIT), and the output is the pair of winning regions with positional winning strategies (Lemma OUT; Corollary 1O-TIME) (2026-10-26) — a SUBCLASS result (𝒞^1O, polynomial by other means; TARGET.md §4 first bullet): not a TARGET.md §2 claim, not M4, and not M3 as a class result (the method's novelty is not checked by L-LIT); G-N5-TIME stays open for general games, CHECKER PASS (docs/checker/C60.md, checker 231c8fe6)
- Object (packet P-N5-1O, added at l-si 058e5aee, pinned trunk 291c110d, unchanged during review): docs/si/P-N5-1O-box15.md, sha1
  2cf5e67262d31712976fb882175f5080cc3dc4ec (L-SI successor 10, Opus 5.5). The referees' notes are collected by the lane in
  docs/si/P-N5-1O-fixes-box15.md (l-si 90f93566, sha1 647deab5f9aeff2c113230bd18df88a6c58b6d68, L-SI successor 10: OUT-1 = N-1O-1, 1O-N1,
  1O-N2, BIT-N1, N-1O-2..6, R-N5-START Addendum 1); on trunk; repairs only.
  Setting: N5 = SPEC S1-S5 of docs/new/N5-ssi-global.md (with Q1-Q4 and FIX 1-4); 𝒞^1O := the games in which exactly one Odd vertex o
  has out-degree > 1; n := |V|, m := #edges, d_o := deg(o), Δ := the maximum out-degree. Cost model: TARGET.md §3 (word RAM with words
  of O(log(n + m)) bits; longer numbers cost their bit length).
- Claims signed (both referees "(Opus 5.5, D15)", L37); no item uses (P); every cited premise is LANDED (RESULTS R15 (c), (d), R18 (d)
  Lemma S (a), R21 (a), R36 (c), R47 (b), R48 (i), R50 (h)):
  (a) Theorem 1O-POLY: for G ∈ 𝒞^1O and any start pair (the S3 start included), N5 stops after at most ITER ≤ (n(n − 1) + d_o)·(T* + 1)
      iterations, where T* is R50 (h)'s bound with f := F := 2n² (R48 (i) gives f ≤ 2n² in every phase; every term of R50 (h)'s chain is
      non-decreasing in f) and R50 (h)'s landed chain, and n(n − 1) + d_o is R47 (b)'s phase count. So ITER = O(m·Δ·d_o·n¹³) ⊆ O(n¹⁸)
      (REFEREE-2 N-1O-2: in fact O(n¹⁷)). R48's f (in-phase Even fallbacks) equals R50 (h)'s f (in-phase fallback transitions), since an
      Odd fallback ends a phase (1O-N1).
  (b) Start-freeness: every result the chain cites is start-free in statement and proof (statewise facts, per-transition facts, and
      inductions whose base is the first state of the window they bound): docs/referee/R-N5-START.md (referee 4e440bd5), with the R32 /
      R33 chain under X-SN-PHASE read line by line in its Addendum 1 (REFEREE, with this review) and by REFEREE-2 (N-1O-5), and
      R34 (b)-(f) line by line in REFEREE-2's report (R2-N5-1O §3; its §C.4 notes that R-N5-START Addendum 1 covers R32 / R33 and R34
      (f), not R34 (b)-(e)).
  (c) Lemma BIT: with valuations stored as (a vertex, an n-bit path-set vector indexed by rank, a length ≤ n), compared by cycle-node
      reward, then the top differing bit, then length (SPEC S1, Q1), one N5 iteration and the final output step cost O(n³(n + m)) word
      operations on O(log(n + m))-bit words and O(n)-bit vectors; no big integers. The longest-path recursion of S1 (iv) is memoised, with the
      same outputs as SPEC's recursion (BIT-N1).
  (d) Lemma OUT: if N5 stops at (σ, τ) on G ∈ 𝒞^1O (Iσ = Iτ = ∅), λ(v) is the cycle node of Ξσ(v), W := {v : Ω(λ(v)) even} and σ̄ is
      S1's best reply, then W = W_E(G), V ∖ W = W_O(G), σ wins for Even from every v ∈ W against every (history-dependent) Odd strategy, and
      σ̄ wins for Odd from every v ∉ W against every Even strategy. The proof's "reward(λ(v)) > 0" fails at the rank-0 even cycle node and
      is repaired to "≥ 0", with every odd vertex of reward ≤ −1; the conclusion is unchanged (OUT-1 = N-1O-1, both referees,
      independently; fixes). It uses R21 (a)'s parenthetical (σ̄ pointwise optimal in G_σ), which holds on every game (N-1O-4; R18 (d)
      Lemma S (a)).
  (e) Corollary 1O-TIME: on 𝒞^1O, N5 from any start pair outputs W_E(G), W_O(G) and positional winning strategies for both players in
      O(ITER·n³(n + m)) word operations, with the O(n log n) priority ranking, i.e. in time polynomial in n + m at bit cost (TARGET.md §3); the class test costs O(n + m).
- Not signed (packet §6, §7): the gauntlet table (a READING: steps 1-3 done for N5 per RESULTS R15 (step 3 with caveats, L-LIT T20; a second
  implementation by L-COMP in progress), step 4 for the subclass by this entry
  and R47-R50; Lean not done and not needed, since this is not an M4 claim); MIRROR / 𝒞^1E (P-N5-DUAL, in review); the frontier
  𝒞^(≥2E,≥2O), where every known exponential strategy-improvement family lies (L-NEW 22, DATA) and nothing here transfers as proved.
- Honest limits: (i) SUBCLASS 𝒞^1O, which is polynomial by other means (Odd has at most d_o positional strategies); the value is the
  method. (ii) The bound is loose and unoptimised; it is not a growth law (R47's data: at most 30 phases in any run). (iii) It rests on
  RESULTS R15, R18 (d), R21, R36, R47, R48 and R50 and on everything those cite. (iv) The objects are SPEC's N5 (pseudocode); BIT is checked
  against SPEC's text, and the code's match to SPEC is DATA (R15 G-N5T-1). (v) Thin data: random 𝒞^1O runs are short (max 8 phases, phase
  length 4, f 1); the long runs are the library's (f 37, length 112, 29 phases); REFEREE-2's Even-strategy enumeration is capped at 4,096
  per stop (skipped at 3,645 random and 1,080 library stops).
- Data (DATA, not proof; one Odd choice vertex asserted on every game): REFEREE (own onecheck.py on rl_engine; checks at the stop: W =
  own Zielonka's W_E, σ wins W, σ̄ wins V ∖ W, ITER ≤ the bound, f ≤ 2n² per phase): P-N5-RHO's library (253 𝒞^1O games) from S3 and 2
  random start pairs, 759 runs, 3,116 phases (max f 33, max ITER 115), and 500 random 𝒞^1O games; 0 failures; its Zielonka agrees with
  Oink 8fbf0a7 --zlk on 109 library files; mutation controls bite (the output read at the start state is wrong in 133 of 239 games).
  REFEREE-2 (own onecheck.py): 26,000 random 𝒞^1O stops (n 4-30) and 503 library files × 3 starts, every check from definitions (play =
  Ξσ, W = W_E, both strategies win against every enumerated positional counter-strategy), 0 violations; ITER, f, phases and phase
  lengths within the bounds on 1,509 library runs (max f 37, max phase length 112, max 29 phases); all mutation controls bite. The
  bound is far above every observed count.
- Signatures: REFEREE docs/referee/R-N5-1O.md (referee 4298dae9, successor 11; §C e785b8e1): 1O-POLY, BIT, 1O-TIME SIGNED; OUT SIGNED
  WITH GAP OUT-1 (one-word repair); notes 1O-N1, 1O-N2, BIT-N1; R-N5-START Addendum 1 (R32 / R33 line by line). REFEREE-2
  docs/referee-2/R2-N5-1O.md (referee-2 04c2d708, successor 13; §C 3312144c): all SIGN, no gap; notes N-1O-1..6. §C (both): verdicts identical in substance; joint gap map one row, OUT-1 =
  N-1O-1, closed by the repair; 1O-N1, 1O-N2, BIT-N1 and N-1O-2, N-1O-3, N-1O-4, N-1O-6 accepted across; REFEREE-2's §3 reads R34 (b)-(f) line by
  line (§C.4), so the R32 / R33 / R34 chain is read in full jointly. No disagreement remains.
- TARGET.md diff: not a claim of TARGET.md §2 (restricted class; TARGET.md §4, first bullet). Its objects match TARGET.md §1 (winning
  regions against history-dependent strategies; positional strategies output) and §3 (word RAM, bit cost). GAPS G-N5-TIME: open for general
  games; its 𝒞^1O part is closed by this entry.

### R52 [refereed-only] N5 on one-Odd-choice games: crossings per phase are at most n·(f + X_SN) + n − 1 in every phase type (Corollary FX (a)), hence O(d_o·n⁶) with R48's fallback bound (FX (b)) (2026-10-26) — partial step-4 lemmas for N5 (not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open for general games), CHECKER PASS (docs/checker/C61.md, checker 22e8a23b)
- Object (packet P-N5-FX, added at l-si fe58fbab, pinned trunk 02ad3f88, unchanged during review): docs/si/P-N5-FX-box14.md, sha1
  aa227b0b310b60c630a89afa248cd60ea04b66c3 (L-SI successor 9, Opus 5.5). The referees' notes are collected by the lane in
  docs/si/P-N5-FX-fixes-box14.md (l-si cfadaee9, sha1 4253d51eb453e6b336cfb9498134a98d003baff9, L-SI successor 11: FX-N1 = N-FX-1,
  FX-N2 = N-FX-2, FX-N3); on trunk; repairs only.
  Setting as in RESULTS R30 and R34 (𝒞^1O; phase; R := the vertices ≠ o whose (σ, τ)-play reaches o; c_θ := λ_Ξ(o), c_w := the cycle node
  of W(o)). A CROSSING is an in-phase transition with R_{k+1} ≠ R_k; X counts the crossings of a phase; f its in-phase Even S4c
  fallback transitions; X_SN its S4a crossings at states with c_w = c_θ (R30 (c)); T := n² + 2n − 1 (R34 (e)).
- Claims signed (both referees "(Opus 5.5, D15)", L37); no item uses (P); premises LANDED: RESULTS R30 (c) R-STICK, R34 (e) (T),
  R34 (f) X-SN-PHASE, R48 (i) FB-POLY:
  (a) Corollary FX (a) (no hypothesis on f, H1, H2, H3, τ(o) or case A / B): in every phase, X ≤ n·(f + X_SN) + n − 1. This is implied by,
      and weaker than, the landed R30 (c) bound (f + 1)(n − 1) + f + X_SN; the packet's proof is a second derivation from R-STICK alone
      (FX-N1 = N-FX-1, both referees).
  (b) Corollary FX (b): hence X ≤ n·(F* + 13(d_o + 1)n³(F* + 1 + T) + T) + n − 1 = O(d_o·n⁶), with F* := 1 + (n − 2)(2n − 1). Signed
      by REFEREE conditional on FB-POLY, by REFEREE-2 unconditionally after FB-POLY landed as RESULTS R48; both §Cs: unconditional now. The
      packet's chain through deg_U(o) is FBP-1's false end inequality: read f ≤ F* by R48 (i) (a) (repaired) if o ≠ c_θ, and by R48 (i) (b)
      / (c) if o = c_θ (f ≤ |U| ≤ n ≤ F* for n ≥ 3, f ≤ 1 = F* for n = 2) (FX-N2 ≈ N-FX-2, both referees; the o = c_θ branch from REFEREE-2).
- Not signed (packet §2, §3): the READINGs that FX covers every phase type ("TYPE H, TYPE Q and TYPE N phases alike" is right for (a);
  FX-N3) and its use in the 𝒞^1O assembly (now RESULTS R51, which uses R30 (c)'s sharper form); FB-PHASE (a lane cross-check).
- Honest limits: (i) SUBCLASS 𝒞^1O, inside a phase. (ii) FX (a) is subsumed by R30 (c); its value is the independent derivation. (iii) The
  bound's tightness is untested: no phase comes above 0.66 of the FX (a) bound in REFEREE-2's data, and its tighter-count mutations do not
  bite.
- Data (DATA, not proof; one Odd choice vertex asserted on every game): REFEREE (own phifx_probe.py on rl_engine): 253 𝒞^1O library games,
  990 phases, X 3,661 in total (X_SN 2,867), max 100 in one phase; 4,995 random 𝒞^1O runs, 8,255 phases, max X 2; 0 failures. REFEREE-2 (own
  fx_check.py): 1,509 library runs (503 files, S3 + 2 random starts), 6,282 phases, crossings by kind (i) / (ii) / (iii) 2,513 / 8,444 /
  456, max X 100 (xsn91_n48); 6,000 random 𝒞^1O runs; 0 violations; mutations stick and noiii bite.
- Signatures: REFEREE docs/referee/R-N5-FX.md (referee 843ba1f8, successor 10; §C 9f736349, successor 11): FX (a) SIGNED, FX (b) SIGNED
  conditional on FB-POLY (unconditional in §C); notes FX-N1..N3; no gaps. REFEREE-2 docs/referee-2/R2-N5-FX.md (referee-2 83a3e8c7,
  successor 13; §C 253fe5c5): (a), (b) SIGN, (b) unconditional; notes N-FX-1, N-FX-2; no gap. §C (both): verdicts identical; joint gap map
  empty; FX-N1 = N-FX-1, FX-N2 ≈ N-FX-2 with the o = c_θ branch accepted by REFEREE; FX-N3 REFEREE only.
- TARGET.md diff: not a claim of TARGET.md section 1. GAPS G-N5-TIME: open for general games (its 𝒞^1O part closed by RESULTS R51).

### R53 [refereed-only] N5 on one-Odd-choice games: inside one phase, the OTHER-touching transitions and all transitions are bounded by explicit polynomials in four per-phase counts X, f^O, K_W and E (Theorem NH: O ≤ 11n⁷(1 + X + f^O) + 8n³(K_W + E), T ≤ 156n¹¹(1 + X + f^O) + 104n⁷(K_W + E)), with Lemmas SW, ST, CL, STR-COUNT and NR (2026-10-26) — a REDUCTION signed as an implication (partial step-4 lemmas for N5; not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open for general games), CHECKER PASS (docs/checker/C62.md, checker 04ad4a15)
- Object (packet P-N5-NH-box42, added at l-new 44088266, pinned trunk 54ac72e6, unchanged during review): docs/new/P-N5-NH-box42.md, sha1
  93d19be8018e07a2727bbe1db5920198a0beb1eb (L-NEW successor 21, Opus 5.5). It is a different object from the box-30 packet P-N5-NH (RESULTS
  R22). The referees' notes are collected by the lane in docs/new/P-N5-NH-fixes-box43.md (l-new 478dd6e1, sha1
  7c499640460eb360bb0407ff051bdfb4907d4f1b, L-NEW successor 23: NH42-N1 + N-NH42-1, N-NH42-2, NH42-N2 + N-NH42-3, NH42-N3); on trunk;
  repairs only, no signed statement changes.
  Setting as in RESULTS R21, R22, R24 and R26 (𝒞^1O; phase; Ξ, W; θ := Ξ(o), w := W(o), c_θ := λ_Ξ(o), c_w := λ_W(o); H1, H2, H3, (h);
  EQ / THR / OTHER). R_k := the vertices whose (σ_k, τ)-play reaches o, with o ∈ R_k (the R22 convention; NH's counts are the same without
  o, NH42-N3), F_k := V ∖ R_k; a CROSSING is a transition with R_{k+1} ≠ R_k, X their number in the phase; a CROSSING-FREE INTERVAL I is a
  maximal run of the phase with R constant; a STRETCH is a maximal run of the phase with R, θ and w constant (R26); π_v is v's σ-route
  (the vertices of v's (σ, τ)-path before its first visit of o); route form and the classes P3′, U1, U2, U3, U23 as in R22 (c) and R26.
  O := the OTHER-touching transitions of the phase (an end is OTHER); f^O := its fallback transitions with an OTHER start state; K_W := the
  sum over the OTHER stretches of class U2, U3 or U23 of their non-fallback transitions with a W-change at some vertex of R; E := the sum
  over the OTHER stretches of class U3 or U23 of their transitions containing an event (R26 (c)); f_S, K_S, E_S the same inside a stretch
  S; Θ_I, WC_I the transitions of I at which θ, respectively w, changes; D := 4n(n − 1) + 1; n ≥ 2.
- Claims signed (both referees "(Opus 5.5, D15)", L37); no item uses (P); every cited premise is LANDED (RESULTS R15 (a), (d), R19 (a),
  R21 (g), (i), R22 (a)-(c), R24 (d), (e), R26 (b), (d), R38 (a)):
  (a) Lemma SW: on a stretch S and for v ∈ R, (a) Ξ_k(v) is determined by π_v and θ, and W_k(v) by π_v and w; (b) hence a transition of S
      that changes Ξ or W at some vertex of R has some Even vertex of R switching.
  (b) Lemma ST: on a crossing-free interval I, (a) under H1 ∧ H2, H1 ∧ ¬H2 or ¬H1 ∧ H2 either every state of I is OTHER or none is; (b)
      under ¬H1 ∧ ¬H2 a state of I is OTHER iff θ ≠ w; (c) so OTHER status is constant on every stretch.
  (c) Lemma CL: for an OTHER stretch S, (a) H1, H2, c_θ, c_w and the route form of each frame are constant on S; (b) if both frames are in
      route form, c_θ ≠ c_w, so S is a P3′ or U1 piece, and a route-form stretch is a piece in the sense of R22 (c) and conversely; (c)
      otherwise S is a U2, U3 or U23 stretch in the sense of R26.
  (d) Lemma STR-COUNT: for a crossing-free interval I, (a) Θ_I ≤ n − 1 (under H1 every θ-change is a transition with a Ξ-change at some
      vertex of F); (b) under H2 every w-change is a transition with a Ξ-change at some vertex of F, so WC_I ≤ n − 1, and under ¬H2
      WC_I ≤ (f^O_I + 1)(|R|² − 1) + f^O_I; (c) I has at most 1 + Θ_I + WC_I ≤ n − 1 + (f^O_I + 1)n² stretches; (d) summed over the
      phase, N := Σ_I (1 + Θ_I + WC_I) ≤ n²(2X + 2 + f^O). (a) under ¬H1 proves RESULTS R26's READING R-1.
  (e) Lemma NR: for an OTHER stretch S with r := |R| and N_R(S) := its transitions with a Ξ-change at some vertex of R: P3′ N_R(S) ≤ (n + 1)r
      ≤ n³; U1 N_R(S) ≤ r + f_S + K + (K + f_S + 1)(r − 2) with K ≤ (f_S + 1)(r − 1)(r − 2), ≤ (f_S + 1)n³; U2 N_R(S) ≤ f_S + K_S +
      (K_S + f_S + 1)(r − 2) ≤ n(K_S + f_S + 1); U3, U23 N_R(S) ≤ f_S + K_S + E_S + (K_S + f_S + E_S + 1)(2r − 4) ≤ 2n(K_S + f_S + E_S
      + 1); in every class N_R(S) ≤ n³(1 + f_S) + 2n(K_S + E_S). K_S and E_S are the counts R26 defines; R26 (d)'s "R-changing" is read
      as "a transition with a switch on R", and by SW (b) a Ξ-change on R comes with a switch on R, so NR's use of U3C is exact in either
      reading (NH42-N1 + N-NH42-1, complementary, both referees).
  (f) Theorem NH: in one phase of N5 on 𝒞^1O, (a) O ≤ X + N + D·(n(X + 1) + (n³ + 1)N + n³f^O + 2n(K_W + E)), with N ≤ n²(2X + 2 + f^O);
      (b) O ≤ 11n⁷(1 + X + f^O) + 8n³(K_W + E); (c) the phase has T ≤ 156n¹¹(1 + X + f^O) + 104n⁷(K_W + E) transitions. Signed as an
      implication: (NH′) (O polynomial per phase, RESULTS R21 limit (ii)) follows from (X), NFB-O, (E) and (K_W), each read as polynomial
      per phase; not a claim that any input is polynomial (NH42-N2 + N-NH42-3, both referees). "Event" (R26 (c)) may be read narrowly or
      broadly; the transition counts are equal by R26 (c)'s kinds-constant, and the theorem holds in both readings (N-NH42-2).
- Not signed (packet §4 Remarks, §5, §6, §7): the remarks; the input statuses of §5 (a READING, dated trunk 6d78b8f4 and superseded:
  FB-POLY LANDED as RESULTS R48, P-N5-FX signed by both referees (RESULTS R52), (E) and (K_W) bounded per stretch given its
  fallbacks by RESULTS R50, a READING for this assembly; fixes file); the map to the R22, R24 and R26 readings (checked, consistent, a
  READING); the data.
- Honest limits: (i) SUBCLASS 𝒞^1O, inside one phase. (ii) A REDUCTION: in its own terms (E) and (K_W) are OPEN; that R50 bounds them is a
  READING outside this entry. The 𝒞^1O running-time result is RESULTS R51, by another route (R50 (h)); NH is a second route to a
  per-phase transition bound. (iii) The exponents are loose; the bounds are far from the data (max O / Theorem NH (a) bound 1.47·10⁻⁴ in
  REFEREE-2's data). (iv) Thin data: random runs barely reach OTHER states (46 of 16,880 phases in REFEREE-2's data); the library carries
  the data; the R15d run step of Theorem NH is not exercised (no OTHER stretch in the data has two consecutive Ξ-flat transitions, so
  REFEREE-2's mutation "run" does not bite) and rests on RESULTS R15 (d); the U3 / U23 bounds near tightness are not exercised.
- Data (DATA, not proof; one Odd choice vertex asserted on every game): REFEREE (own nh42_probe.py on rl_engine): 253 𝒞^1O library games
  from SPEC S3's start, 990 phases, 101 with O > 0, ΣO = 833, OTHER stretches P3′ 131 / U1 353 / U2 66 / U3 104 / U23 51, per-phase maxima
  O 77, X 100, T 112, f^O 12, K_W 25, E 15, equal to the packet's §7 counts on an independent engine; with 3 random start pairs per game
  (759 more runs) 4,202 phases, 388 with O > 0; 0 failures. REFEREE-2 (own nh42_check.py, own definitions): 1,509 library runs (503 files,
  S3 + 2 random starts) 6,205 phases, 529 with O > 0; 1,006 runs on its own trace 4,123 phases; 7,000 random 𝒞^1O runs (n 6-16); 0
  violations; mutation controls sw, stc, nr bite, run does not (limit (iv)).
- Signatures: REFEREE docs/referee/R-N5-NH42.md (referee a47f8540, successor 10; §C 5fc234ba, successor 11): SW, ST, CL, STR-COUNT, NR,
  Theorem NH (a)-(c) SIGNED; notes NH42-N1..N3; no gaps. REFEREE-2 docs/referee-2/R2-N5-NH42.md (referee-2 d2142087, successor 13; §C
  253fe5c5): all SIGN; notes N-NH42-1..3; no gap. §C (both): verdicts identical; joint gap map empty; NH42-N1 and N-NH42-1 complementary,
  N-NH42-2 accepted, NH42-N2 = N-NH42-3, NH42-N3 REFEREE only; nothing open.
- TARGET.md diff: not a claim of TARGET.md section 1 (a subclass, inside a phase, a reduction). GAPS G-N5-TIME: open for general games
  (its 𝒞^1O part closed by RESULTS R51).

### R54 [refereed-only] N5 is mirror-symmetric: on every game, the N5 run on G is the mirror of the "Odd first" run N5^OF on the dual game G^d (Lemma DUAL); on one-Even-choice games σ changes at most d_e − 1 times and a run has at most n(n − 1) + d_e dual phases, and a per-first-phase bound L(n) for N5^OF on one-Odd-choice games ((H-OF), implied by the same bound for N5 by MIRROR (c)) gives at most (n(n − 1) + d_e)(L(n) + 1) iterations on one-Even-choice games (Theorem MIRROR, (b) as an implication); phases ≤ n(n − 1) + ∏ deg(o_i) on every game (Corollary Φ-kO); an empty improving set stays empty (Lemma ENDGAME) (2026-10-26) — structural lemmas for N5 and a conditional transfer (not M3, not a step-4 pass, not a TARGET.md claim; no running-time bound on any class is signed here; G-N5-TIME stays open for general games), CHECKER PASS (docs/checker/C63.md, checker 04ad4a15)
- Object (packet P-N5-DUAL, added at l-new b15856e8, pinned trunk df073cb5, unchanged during review): docs/new/P-N5-DUAL-box43.md, sha1
  a51f7c30c267a4c02088cf2c849388e28c4121fa (L-NEW successor 22, Opus 5.5). The referees' repair and notes are collected by the lane in
  docs/new/P-N5-DUAL-fixes-box43.md (l-new 478dd6e1, sha1 5d08d0fd421fa85d36408b1caeabf03b75653760, L-NEW successor 23: DUAL-1 = N-DUAL-1 (the one repair), N-DUAL-2,
  N-DUAL-3, a status line); on trunk; repairs only.
  Setting: N5 = SPEC S1-S5 of docs/new/N5-ssi-global.md (with FIX 1-4); n := |V|. G^d := the dual game (owners swapped, Ω + 1, same ids
  and successor lists; n5.py's dual). N5^OF ("Odd first"): N5 with S4c replaced by "if σ_new = σ and τ_new = τ: if I_τ ≠ ∅ Odd falls
  back (switch-all on I_τ, each Odd v with an improving edge takes the w maximising (Ξ_τ(w), w) on G^d, σ unchanged), else Even falls
  back as in S4c". A TWO-SIDED FALLBACK is an iteration where S4c applies with I_σ ≠ ∅ and I_τ ≠ ∅. The MIRROR of a state (σ, τ) of G is
  the state (τ, σ) of G^d. A choice vertex has out-degree ≥ 2; 𝒞^1O: exactly one Odd choice vertex; 𝒞^1E: exactly one Even choice
  vertex e, d_e := deg(e), any number of Odd choice vertices. Phase: a maximal run with (λ, τ) constant (RESULTS R38 (a) KEY); dual
  phase: a maximal run with (λ^U, σ) constant (λ, λ^U as in RESULTS R47).
- Claims signed (both referees "(Opus 5.5, D15)", L37); no item uses (P); premises LANDED: RESULTS R15 (a)-(d), R38 (a), R47 (a):
  (a) Lemma DUAL (every game, every start pair (σ_0, τ_0)): the N5 run on G from (σ_0, τ_0) is the mirror of the N5^OF run on G^d from
      (τ_0, σ_0) (same length, state k ↦ the mirror of state k). Consequently the N5 run on G^d from (τ_0, σ_0) agrees with that mirror on
      states 0, …, j; the first possible difference is at state j + 1, where j → j + 1 is the first two-sided fallback of the run on G;
      with no two-sided fallback the two runs are mirrors. (The second sentence is read with the fixes file's repair: the packet's
      sentence named two different agreement points, its "i.e." clause is the right one and the proof is unchanged; DUAL-1 = N-DUAL-1,
      found independently by both referees.) The proof rests on Ω + 2 invariance of SPEC S1 (rank by (Ω(v), v) and Ω(v) mod 2 only).
  (b) Theorem MIRROR (a): on 𝒞^1E, along any N5 run σ changes at most d_e − 1 times, and the run has at most n(n − 1) + d_e dual phases.
  (c) Theorem MIRROR (b), signed as an IMPLICATION: under hypothesis (H-OF) "there is L(n) such that for every 𝒞^1O game with n vertices
      and every start pair, the first phase of the N5^OF run from that start pair has at most L(n) transitions", N5 on every 𝒞^1E game
      with n vertices, from every start pair, makes at most (n(n − 1) + d_e)(L(n) + 1) iterations. (H-OF) is not proved in the packet.
  (d) Theorem MIRROR (c): (H-OF) follows from (H-N5) "for every 𝒞^1O game with n vertices and every start pair, the first phase of the
      N5 run has at most L(n) transitions" (the first N5^OF phase from a state is a prefix of, or equal to, the first N5 phase from it).
  (e) Corollary Φ-kO (every game): along any N5 run the number of distinct τ's is at most ∏ over the Odd choice vertices o_i of deg(o_i),
      and the run has at most n(n − 1) + ∏_i deg(o_i) phases; mirror: at most n(n − 1) + ∏ over the Even choice vertices of deg dual
      phases. On 𝒞^kO with k fixed, phases ≤ n(n − 1) + n^k. (A bound on phases, not on iterations.)
  (f) Lemma ENDGAME (every game): if I_σ = ∅ at state k of an N5 run, then σ_j = σ_k for every j ≥ k; mirror: if I_τ = ∅ at state k,
      then τ_j = τ_k for every j ≥ k.
- Not signed (packet §1 Scope, §2, §3): the scope READING (𝒞^1E has unboundedly many Odd choice vertices); the §2 start / N5^OF table
  ("to check, not to sign"; its general argument checked by REFEREE, rows spot-checked; the rows used by the 𝒞^1O chain are covered by
  docs/referee/R-N5-START.md with its Addendum 1 and REFEREE-2's R2-N5-1O §3, the other rows unaudited by both, N-DUAL-2); the Φ-kO
  Remark (DATA); docs/new/N5-MULTI-box43.md §2-§4 (CONJECTURES Δ1, Δ2); the cross-field reading of DUAL. READING (N-DUAL-3, both
  referees; not signed here): with RESULTS R51, (H-N5) holds with L(n) = T*(n, n², n, n) (T* is non-decreasing in m, d_o, Δ), so MIRROR
  (b), (c) would give O(n¹⁷) iterations on 𝒞^1E from every start pair; output correctness on 𝒞^1E would also need Lemma OUT stated and
  signed on every game, and Lemma BIT; both are for a separate packet. The 𝒞^1E bound is not a result of this entry.
- Honest limits: (i) No running-time bound is signed here: MIRROR (b) is an implication, and its 𝒞^1E instance is a READING (above).
  (ii) DUAL needs N5^OF on the dual side; the plain N5 run on G^d can part from the mirror at a two-sided fallback (the packet's example
  experiments/red/so/instances/exitr_cex_n48.pg, sha1 7a663df2: first two-sided fallback 2 → 3, first difference at state 3, 22
  iterations on G against 23 on G^d). (iii) Thin data: random games never produce a two-sided fallback (0 in every random set of both
  referees); DUAL's second sentence is exercised by library runs and REFEREE's climbs only.
- Data (DATA, not proof): REFEREE (own dual_probe.py on rl_engine, S4c side rule as a parameter; checks DUAL, PLAIN first difference,
  Ω + 2, ENDGAME, Φ-kO and its mirror, MIRROR (a) on 𝒞^1E, the MIRROR (c) prefix property on 𝒞^1O): lib41 n ≤ 64 (367 files) from S3 and
  2 random start pairs, 1,101 runs, 50 with two-sided fallbacks (128); 3,000 random games with k = 0..4 Odd choice vertices (378 𝒞^1E);
  climbs (dual_climb.py, 3 × 1,200 s) 390,158 runs, 135,671 with two-sided fallbacks (297,779); every plain-mirror first difference exactly
  at j + 1; prefix property on 24,056 sampled states; 0 failures. REFEREE-2 (own dual_check.py on L-SI's si.py engine with an Odd-first
  flag): lib41 824 runs (33 with two-sided fallbacks, 88), 1,006 𝒞^1O library runs (33, 170), 6,000 random runs (2,000 𝒞^kO, 2,000 𝒞^1E,
  2,000 𝒞^1O); every first difference at j + 1; MIRROR (a)'s bound d_e − 1 attained; 0 violations; on lib41 from S3 it reproduces the
  packet's 15 runs / 54 two-sided fallbacks exactly; mutation controls plain (15), phi (36), endg (163) bite.
- Signatures: REFEREE docs/referee/R-N5-DUAL.md (referee cdb187c7, successor 11; §C 78db369b): DUAL first sentence, MIRROR (a), (c),
  Φ-kO, ENDGAME SIGNED; MIRROR (b) SIGNED as an implication; DUAL second sentence SIGNED WITH GAP DUAL-1 (wording), closed by the fixes
  file's repair. REFEREE-2 docs/referee-2/R2-N5-DUAL.md (referee-2 73c2b4a1, successor 13; §C 253fe5c5): all SIGN ((b) as an
  implication), no gap; notes N-DUAL-1..3. §C (both): verdicts identical in substance; joint gap map DUAL-1 = N-DUAL-1, closed by the
  one-line repair; N-DUAL-2 accepted (REFEREE's §6 updated by its R-N5-START audit); N-DUAL-3 agreed as a READING. Nothing open.
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (no running-time bound is proved; MIRROR (b) is conditional; DUAL, Φ-kO and
  ENDGAME are structural). GAPS G-N5-TIME: open for general games (its 𝒞^1O part closed by RESULTS R51; 𝒞^1E a READING).

### R55 [refereed-only] N5 on EVERY game: with the disagreement set D_k := {Odd u : σ̄_k(u) ≠ τ_k(u)} in place of o, the honest and the W-valuation agree off the D-region (G_D (a)), factor through the first D-vertex under (h_D) (G_D (b)) and agree in coarse form above M_D under (h_D) ∧ (h3_D) (G_D (c1), (c2)); Ξ changes on F_D at most max(0, |F_D| − 1) times per D-crossing-free interval (F1°_D); W(u) does not drop at u ∈ D_k ∩ D_{k+1} under (h_D) (Wo_D) (2026-10-26) — structural lemmas for N5 beyond one Odd choice vertex (not M3, not a step-4 pass, not a TARGET.md claim; nothing here bounds N5's running time on any class; G-N5-TIME stays open for general games), CHECKER PASS (docs/checker/C64.md, checker 0c1969e7)
- Object (packet P-N5-GD, added at l-new 205c9ed7, pinned trunk 3c6f6c16, unchanged during review): docs/new/P-N5-GD-box43.md, sha1
  b898ff8256bf444ef90d69eb3154f5fe16dddf10 (L-NEW successor 23 from successor 22's working doc, Opus 5.5). The referees' notes are
  collected by the lane in docs/new/P-N5-GD-fixes-box44.md (l-new b93f6c7d, sha1 dfa6dd2b4cc51f95285dcdd4f9df14ff55a01d09, L-NEW
  successor 23: GD-N1 = N-GD-1, GD-N2, GD-N3, the premise-class note); on trunk; repairs only, no signed statement changes.
  Setting (every game; no class hypothesis): N5 = SPEC S1-S5 of docs/new/N5-ssi-global.md (with FIX 1-4); n := |V|; state k = (σ_k, τ_k);
  σ̄_k := SPEC S1's optimal Odd counterstrategy to σ_k; Ξ_k(v) := the value of the (σ_k, σ̄_k)-play from v; G_τ := G with every Odd
  vertex fixed to τ_k; W_k(v) := the value of the (σ_k, τ_k)-play from v; λ_Ξ, λ_W the cycle-node maps; values and ⊴ as in VJ00 (RESULTS
  R15). Phase as in RESULTS R38 (a) KEY. D_k := {Odd u : σ̄_k(u) ≠ τ_k(u)}; u(v) := the first vertex of D_k on v's (σ_k, τ_k)-play (v
  included), if any; R_D := {v : u(v) exists}, F_D := V ∖ R_D; π_v := the (σ_k, τ_k)-path from v to u(v), u(v) excluded. (h_D) at k: for
  every u ∈ D_k, neither the honest play nor the W-play from u visits D_k after leaving u. (h3_D) at k: λ_Ξ(u) = λ_W(u) for every u ∈ D_k.
  lev, COARSE_L, (C2), (C4) as in RESULTS R25; M_D := max over u ∈ D_k of lev(Ξ_k(u), W_k(u)), ⊥ if D_k = ∅. On 𝒞^1O with D_k = {o}:
  R_D = R, F_D = F, (h_D) = H1 ∧ H2, (h3_D) = H3.
- Claims signed (both referees "(Opus 5.5, D15)", L37); no item uses (P); premises LANDED: RESULTS R15 (a) and R38 (a) (both landed
  for every game); R17 (a)-(c), R18 (c) flat case, R18 (d) Lemma S (c) in its landed "⇒" form, R21 (a) XW, R21 (c) FBL-N (i), each
  signed under a 𝒞^1O setting line, whose proofs both referees read and CONFIRM use no one-Odd step (R17 and R18's flat case are
  one-player statements, applied to G_τ, its arenas and 𝓕, which are one-player on every game; XW is VJ00 (11) on G_σ); and R25 (C2),
  (C4), facts about lev and COARSE_L on values. R21 (c) FBL-N (ii) and
  R22 (a) step 1 DO have a one-Odd step; the packet does not cite them and re-proves both in set form (F1°_D steps 1 and 4) (premise-class
  note; N-GD-2 + REFEREE §1; fixes):
  (a) Lemma G_D (a) (no hypothesis): for every state k and every v ∈ F_D, Ξ_k(v) = W_k(v).
  (b) Lemma G_D (b) (under (h_D) at k): for v ∈ R_D with u := u(v), Ξ_k(v) = π_v ⊕ Ξ_k(u) and W_k(v) = π_v ⊕ W_k(u), and the honest and
      the W-play from u avoid π_v.
  (c) Lemma G_D (c) (under (h_D) and (h3_D) at k): (c1) if y, z ∈ R_D and u(y) = u(z) = u, then π_y ⊕ Ξ_k(u) ⊴ π_z ⊕ Ξ_k(u) iff
      π_y ⊕ W_k(u) ⊴ π_z ⊕ W_k(u); (c2) for every L with M_D ≤ L < ∞ (L = ⊥ allowed when M_D = ⊥) and every v ∈ V,
      COARSE_L(Ξ_k(v)) = COARSE_L(W_k(v)), hence the COARSE_L-orders of Ξ_k and W_k coincide on V. Nothing is claimed for routes to
      different terminals below M_D (Δ-RT, OPEN).
  (d) Lemma F1°_D (no (h_D), no (h3_D)): on a D-crossing-free interval I (a maximal run of states of one phase on which (D_k, R_D) is
      constant), the transitions at which Ξ changes at some vertex of F_D number at most max(0, |F_D| − 1). In step 4, R18 (d) Lemma S
      (c) is read in its landed "⇒" form (S4a returning σ_k makes σ_k a pointwise arena optimum; only "⇒" is used) (GD-N1 = N-GD-1, both
      referees, independently), and the sentence "Since k+1 ∈ I, z ∈ F_D" is read for x's switched successor x* := σ_{k+1}(x), which lies
      in F_D because F_D is closed under σ_{k+1}; the conclusion stands (GD-N2, REFEREE; accepted by REFEREE-2).
  (e) Lemma Wo_D (under (h_D) at k and at k+1): if k → k+1 is an N5 transition with τ_{k+1} = τ_k and u ∈ D_k ∩ D_{k+1}, then
      W_{k+1}(u) ⊵ W_k(u). (No (h3_D) and no phase hypothesis; the honest-side statement is not claimed.)
- Not signed (packet §2, §3, §4): the port table (a READING); CONJECTURE Δ1 (D-changes per phase poly(n)); Δ-RT (OPEN); the R20
  coarse port (CONJECTURE); docs/new/N5-MULTI-box43.md §2-§4; the data. DATA, not a gap (GD-N3, REFEREE): in REFEREE's random games
  Wo_D's conclusion also held at all 66 transitions where (h_D) failed; the proof uses (h_D).
- Honest limits: (i) Structural lemmas only: they bound no count of transitions, crossings or phases on any class beyond what F1°_D
  states per interval; the frontier 𝒞^(≥2E,≥2O) stays open, and Δ1 and Δ-RT are what an R_D-side count would need. (ii) The premises'
  game-generality is a reading of their proofs by both referees (above), not a re-signature of the landed entries. (iii) F1°_D's bound is
  not approached in the data (REFEREE-2's mutation f1 with |F_D| − 2 does not bite), so its tightness is untested; Wo_D is thin on
  random multi-Odd games (36 checks in REFEREE's, 225 in REFEREE-2's).
- Data (DATA, not proof): REFEREE (own gd_probe.py; logs scratch/gd_logs/): lib41 (n ≤ 64: 367 games, any class) from S3 and 2 random
  start pairs, 1,101 runs, and 500 random games with 2-4 Odd choice vertices × 3 starts, 1,500 runs; G_D (a), (b), (c1), (c2) (at every L
  from max(M_D, −1) to n − 1), F1°_D and Wo_D checked; 0 failures; mutation: (c2) at L = M_D − 1 fails at all 85 states with M_D ≥ 0 (the
  threshold is sharp). REFEREE-2 (own gd_check.py, own play values): lib41 × 3 starts (1,236 runs), 503 𝒞^1O files × 2 (1,006), the
  box-43 instances × 5 (25), 20,000 random 𝒞^kO runs; 92,210 states, G_D (a) at every state, (c2) at every level L ≥ M_D, 7,039 + 8,420
  + 28 + 225 Wo_D checks; 0 violations; max Ξ-changes on F_D per interval 55 (x32_rand64.pg); mutations gda, c2, wo bite, f1 does not.
- Signatures: REFEREE docs/referee/R-N5-GD.md (referee a50f6623, successor 11; §C a639e39e): G_D (a), (b), (c1), (c2), F1°_D, Wo_D
  SIGNED; premise class CONFIRMED; notes GD-N1..N3; no gaps. REFEREE-2 docs/referee-2/R2-N5-GD.md (referee-2 ab4a5af0, successor 13;
  §C 6e12b2bc): all SIGN; premise class CONFIRMED (N-GD-2); notes N-GD-1, N-GD-2; no gap. §C (both): verdicts identical; joint gap map
  empty; GD-N1 = N-GD-1 (found independently); GD-N2 accepted by REFEREE-2; GD-N3 REFEREE only (data); nothing open.
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (structural lemmas; no running time). GAPS G-N5-TIME: open for general games.

### R56 [refereed-only] N5 on EVERY game: in-phase fallbacks per phase are at most 1 + (n − 1)(2 + ρ), ρ := the Ξ-changes at Odd choice vertices in the phase, and at most 1 + (n − 1) + (n − 1)·N_late counting only Q-runs that hold a late fallback (Theorem FB-RED, both forms, signed as a REDUCTION in ρ), with the set-form κ lemmas of RESULTS R48 and the terminal-value freeze (Lemma TV) (2026-10-26) — partial step-4 lemmas for N5 beyond one Odd choice vertex (not M3, not a step-4 pass, not a TARGET.md claim; ρ is not bounded, CONJECTURE ρ-POLY OPEN; G-N5-TIME stays open for general games), CHECKER PASS (docs/checker/C65.md, checker b911ecce)
- Object (packet P-N5-FBRED, added at l-new 3732ab55, pinned trunk c3f6f2bf, unchanged during review): docs/new/P-N5-FBRED-box44.md, sha1
  11b15455f70d439c93a48d7e82fcdc14ef73854d (L-NEW successor 23, Opus 5.5); a port of RESULTS R48 (P-N5-FBPOLY, "FBP") to every game. The
  referees' notes are collected by the lane in docs/new/P-N5-FBRED-fixes-box44.md (l-new 2742f3e9, sha1 05c249433431f7e147272ad689c0a7815b7a5b71, L-NEW successor 23:
  N-FBRED-1, N-FBRED-2, FBRED-N1, N-FBRED-3, N-FBRED-4 = FBRED-N2, the signed scope); on trunk; repairs only, no signed statement changes.
  Setting (every game; no hypothesis on the class, (h_D), (h3_D), H1, τ or c_w): N5 = SPEC S1-S5 of docs/new/N5-ssi-global.md; phases as
  in RESULTS R38 (a) KEY; g_1 < g_2 < … the in-phase (Even S4c) fallbacks of a phase. Q := the Odd vertices of out-degree ≥ 2; C := the
  honest cycle nodes of the phase; T := C ∪ Q (terminals); for c ∈ C the honest class U_c := λ^{-1}(c). κ_t(z) := (signed weight of
  P(Ξ_t z), s_c·ℓ(Ξ_t z)) for z ∈ U_c, s_c := +1 if Ω(c) is odd, −1 if even; κwt_c(v) := (wt_c(v), s_c), wt_c(v) := sgn(v)·2^rank(v) if
  rank(v) > rank(c), else 0. At a fallback k → k+1, S_k := the switched Even vertices, S := S_k ∖ T, S_c := S ∩ U_c, x*_v := σ_{k+1}(v).
  G_c := U_c ∖ (Q ∖ {c}) with c a sink; for q ∈ Q ∩ U_c, q ≠ c, G_c^q := U_c ∖ (T ∖ {q}) with q a sink (Even vertices keep their edges
  inside, Odd vertices, all forced there, their edge if inside); κopt_c(z), κopt^q(z) := the best κwt_c-weight of a simple path of G_c
  to c, respectively of G_c^q to q. A Q_c-run (Q-run): a maximal run of the phase with Ξ(q) constant for every q ∈ Q ∩ U_c (every q ∈ Q).
  ρ := the number of pairs (transition t → t+1 of the phase, q ∈ Q) with Ξ_{t+1}(q) ≠ Ξ_t(q). "The i-th fallback of its run" counts the
  fallback k → k+1 in the run that contains its source state k (FBRED-N1, both referees).
- Claims signed (both referees "(Opus 5.5, D15)", L37), on every game; no item uses (P); premises LANDED: RESULTS R15 (a), R17 (a) (V1),
  R18 (d) Lemma S (a), R38 (a) KEY and R38 (f) CN-LAST, and the FBP steps of RESULTS R48 that the packet ports. R18 (d) Lemma S (a) is
  signed under a 𝒞^1O setting line; both referees read its proof (VJ00 (11) and R17 (F1) on the one-player game G_σ) and CONFIRM it holds
  on every game (N-FBRED-3 = REFEREE §1):
  (a) Facts (Aκ), (A0κ), (M1κ), (M2κ), (INJ), (SP′) per honest class, and κ-FB-ROUND_D (FBP §0.3, §1 with c for c_θ).
  (b) κ-HAT-FREEZE_D (a)-(c) on G_c: (a) for t > g_j, z ∈ U_c ∖ (Q ∖ {c}) and every simple path p of G_c from z to c with ≤ j edges,
      κ_t(z) ≥ κwt_c(p ∖ {c}); (b) if z's honest play at t avoids Q ∖ {c}, κ_t(z) ≤ κopt_c(z); (c) for t > g_{|U_c|−1}, κ_t(y) =
      κopt_c(y) for every y ∈ U_c whose honest play at t avoids Q ∖ {c}.
  (c) κ-PFZ_D (per q ∈ Q ∩ U_c, q ≠ c, Θ a Q_c-run): for t ∈ Θ after the j-th fallback of Θ and every simple path p of G_c^q from z to q
      with ≤ j edges, κ_t(z) ≥ κwt_c(p ∖ {q}) + κ_t(q); stated for z ∈ (U_c ∖ T) ∪ {q}, since the induction passes through z = q, where the
      claim is trivial (N-FBRED-1, both referees).
  (d) κ-Y-FORM_D (per q ∈ Q ∩ U_c, q ≠ c, at a state t where q lies on no honest cycle): κ_t(q) = κwt_c(q) + min over y ∈ Y^q_t of κ_t(y),
      with Y^q_t := {y ∈ succ(q) ∩ U_c : y's honest play at t avoids q}, a definition the packet gives only in its not-to-sign §4 table and
      which is read into the signed text (N-FBRED-2, REFEREE-2; accepted by REFEREE). The "≤" half uses R18 (d) Lemma S (a) on every game.
  (e) EXIT-SWITCH_D (at an in-phase fallback k → k+1 with S_c ≠ ∅, some u ∈ S_c has: the honest play at k from x*_u visits T ∩ U_c
      before it visits u; for the first such vertex e, p_u := u · (that play up to e) is a simple path of G_c (e = c) or G_c^e (e ∈ Q),
      and κ_k(x*_u) = κwt_c(p_u ∖ {u, e}) + κ_k(e)), FREEZE-EXIT_D (conservative indices: if k = g_j with j ≥ |U_c| and k is the i-th
      fallback of its Q_c-run with i ≥ |U_c|, then S_c = ∅) and CN-ONLY_D (a fallback with S = ∅ is the last transition of its phase; at most one per phase).
  (f) Theorem FB-RED: for every phase of N5 on any game, f ≤ 1 + (n − 1) + (n − 1)(1 + ρ) = 1 + (n − 1)(2 + ρ). Late form: f ≤ 1 + (n − 1)
      + (n − 1)·N_late, with N_late := the Q-runs of the phase holding a fallback g_j, j ≥ n, and N_late ≤ 1 + ρ_late (ρ_late := the
      Ξ-changes at Odd choice vertices at transitions after g_{n−1}). Both SIGNED AS A REDUCTION in ρ: polynomial in n only given ρ.
  (g) Lemma TV: for a Q-run Θ, c ∈ C, and t ∈ Θ after |U_c| − 1 fallbacks of the phase and of Θ, every z ∈ U_c ∖ T has κ_t(z) =
      max(κopt_c(z), max over q ∈ Q ∩ U_c, q ≠ c, of κopt^q(z) + κ_Θ(q)).
- Not signed (packet §4-§6): the step table against FBP (a READING; both referees' own diffs agree with it); THETA-AFTER (fails as proved
  with several terminals; its per-terminal bound held in every check, unproved); CONJECTURE ρ-POLY and the nested-freeze route (OPEN;
  §5.1: short late Q-runs and terminal path-sum values); the data. On 𝒞^1O, RESULTS R48 (FB-POLY) stays the unconditional form.
- Honest limits: (i) A REDUCTION: ρ per phase is not bounded (max ρ 218 in one phase, tcL_N10, n 350, REFEREE). (ii) Vacuity
  (FBRED-N2 = N-FBRED-4, both referees): no phase in any sample or climb of either referee or the lane reaches n in-phase fallbacks (max
  37 at n 48 on 𝒞^1O, dirty_a_best in REFEREE-2's 503 files, 33 in lib41; 17 at n 32 on the frontier, fb17_n32; REFEREE-2's climbs on f − n reach −4), so FREEZE-EXIT_D's hypothesis, the
  third bullet of FB-RED, the late form's N_late and Lemma TV's hypothesis are never met in data: they rest on their proofs. (iii)
  REFEREE successor 12 re-derived every port against FBP §0.3-§4 except κ-HAT-FREEZE (b), (c) in detail, where it accepts successor 11's
  reading (R-N5-FBRED §C C.1). (iv) The constant n − 1 (not FBP's |U| − 2) comes from FREEZE-EXIT_D's conservative indices.
- Data (DATA, not proof): REFEREE (successor 11, own fbred_probe.py on rl_engine; logs scratch/fbred_logs/): lib41 n ≤ 64 (367 games)
  from S3 and 2 random start pairs, 1,101 runs, 5,393 phases, max f 33, max ρ 51; the box-43/44 instances × 5 starts, 50 runs, max f 17
  (fb17_n32); 1,200 random runs with 1-4 Odd choice vertices; 0 failures; successor 12 added the 45 games with n > 64 (135 runs, 1,834
  phases, max ρ 218), 0 failures, and reproduced REFEREE-2's ρ 194 on tcL_N8 at its start pair. REFEREE-2 (own fbred_check.py): 22,292
  runs, 61,151 phases (lib41 × 3, 503 𝒞^1O files × 2, the 10 instances × 5, 20,000 random 𝒞^kO), κ-Y-FORM_D 309k and κ-PFZ_D 290k checks
  (exhaustive simple-path enumeration for n ≤ 11), HAT (c) and TV 97 qualifying states each; 0 violations; mutations yf, cno bite, fex,
  red do not (the data never come within 4 of FREEZE-EXIT_D's indices).
- Signatures: REFEREE docs/referee/R-N5-FBRED.md (referee 1feff548, successor 11; §C 1ea0d317, successor 12): every to-sign statement
  SIGNED, FB-RED and its late form AS A REDUCTION; notes FBRED-N1, FBRED-N2; no gap. REFEREE-2 docs/referee-2/R2-N5-FBRED.md (referee-2
  814ac456, successor 13; §C a4a642b6): all SIGN, FB-RED as a reduction in ρ; notes N-FBRED-1..4; no gap. §C (both): verdicts
  identical; joint gap map empty; N-FBRED-1, N-FBRED-2 accepted (N-FBRED-2 missed by REFEREE successor 11); N-FBRED-3 = REFEREE §1;
  N-FBRED-4 = FBRED-N2; FBRED-N1 REFEREE's, the convention REFEREE-2 uses; nothing open.
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (a reduction; no running-time bound). GAPS G-N5-TIME: open for general games.

### R57 [refereed-only] N5's output at its stop is correct on EVERY parity game (Lemma OUT-G), each iteration costs polynomially many bit operations on every game (Lemma BIT-G), and N5 solves one-Even-choice games in polynomial time from any start pair: at most (n(n − 1) + d_e)(T*(n, m, Δ, d_e) + 1) = O(m·Δ·d_e·n¹³) ⊆ O(n¹⁷) iterations (Theorem 1E-POLY; Corollary 1E-TIME) (2026-10-26) — output correctness (OUT-G) and per-iteration bit cost (BIT-G) of N5 on every game, under the standing SPEC premise 1E-N3 (not a step-4 pass: no iteration bound on general games), and a SUBCLASS time result (𝒞^1E, polynomial by other means; TARGET.md §4 first bullet): not a TARGET.md §2 claim, not M4; G-N5-TIME stays open for general games, CHECKER PASS (docs/checker/C66.md, checker 33aa8b3a)
- Object (packet P-N5-1E, added at l-si adb721b5, pinned trunk 7fef9699, unchanged during review): docs/si/P-N5-1E-box16.md, sha1
  e613db131d3871c038f53fcb4e009c33f47ca20e (L-SI successor 11, Opus 5.5). The referees' notes are collected by the lane in
  docs/si/P-N5-1E-fixes-box16.md (l-si f5d62bba, sha1 8f3615bcfcb7e8810a2847207ad3986febec83dd, L-SI successor 11: 1E-N1,
  1E-N2 = N-1E-2, 1E-N3 = N-1E-1, N-1E-4, N-1E-3 closed, 1E-N4 data, N-1E-5 / §6 reading); on trunk; repairs only.
  Setting: N5 = SPEC S1-S5 of docs/new/N5-ssi-global.md (with Q1-Q4 and FIX 1-4); any parity game G (TARGET.md §1: V finite, every vertex
  has a successor); n := |V|, m := #edges, Δ := the maximum out-degree. 𝒞^1E := the games in which exactly one Even vertex e has
  out-degree > 1 (any number of Odd choice vertices); d_e := deg(e). Ξσ: Even's honest valuation of σ against S1's optimal Odd
  counterstrategy σ̄; Iσ: SPEC S2's Even improving set. T* is RESULTS R50 (h)'s per-phase bound as used in RESULTS R51 (a). Cost model:
  TARGET.md §3 (word RAM with O(log(n + m))-bit words; longer numbers cost their bit length).
- Claims signed (both referees "(Opus 5.5, D15)", L37); no item uses (P); every cited premise is LANDED (RESULTS R15 (c), (d), R18 (d)
  Lemma S (a), R21 (a), R36 (c), R51 (a), (b), (c), (d), R54 (a)-(d)); R18 (d) Lemma S (a), R21 (a)'s parenthetical and R36 (c)
  have game-general proofs (one-player G_σ̄ / G_σ on every game; RESULTS R51 (d) N-1O-4, R55, R56), a reading of their proofs
  confirmed again by both referees here, not a re-signature of those entries:
  (a) Premise (VJ), on every game: for every positional σ and every positional Odd strategy τ′, Ξσ(v) ⊴ V_{σ,τ′}(v) at every v; read from
      VJ00 (BRICS RS-00-48) §4.3 (Ωσ as the minimum over all plays consistent with σ) and §5.2 (Prop. 5.1, Lemma 5.2, (11)), every finite
      game graph (§2), checked by both referees against the PDF (sha256 485a12de…) (1E-N2 = N-1E-2).
  (b) Lemma OUT-G (every game): if σ is a positional Even strategy with Iσ = ∅, λ(v) is the cycle node of Ξσ(v), W := {v : Ω(λ(v))
      even} and σ̄ is S1's Odd counterstrategy at σ, then W = W_E(G), V ∖ W = W_O(G), σ wins for Even from every v ∈ W against every
      (history-dependent) Odd strategy, σ̄ wins for Odd from every v ∉ W against every (history-dependent) Even strategy, and σ on W and
      σ̄ on V ∖ W are well defined on their regions. Iτ = ∅ is not used; determinacy is derived, not assumed (W_E ∩ W_O = ∅ is proved).
      The "≥ 0" repair of RESULTS R51 (d) (OUT-1) is built in. In particular, on every game N5 stops (R15 (d)) and SPEC S5's output there
      is correct. Standing premise, as in R51 (d): OUT-G concerns SPEC's Ξσ and σ̄; that S1's procedure realises an optimal σ̄ is VJ00 §6
      plus SPEC conformance, and the code's match to SPEC is DATA (R15 G-N5T-1) (1E-N3 = N-1E-1).
  (c) Lemma BIT-G (every game): RESULTS R51 (c) with "on 𝒞^1O" dropped. With valuations stored as (a vertex, an n-bit path-set vector
      indexed by rank, a length ≤ n), compared by cycle-node reward, then the top differing bit, then length (SPEC S1, Q1), one N5
      iteration and the final output step cost O(n³(n + m)) word operations on O(log(n + m))-bit words and O(n)-bit vectors on every
      parity game; no big integers. The longest-path recursion of S1 (iv) is memoised, with the same outputs as SPEC's recursion: R51 (c)'s
      sentence (BIT-N1), which the proof uses and the packet's statement dropped, is read into the statement (1E-N1, REFEREE; accepted by
      REFEREE-2).
  (d) Theorem 1E-POLY: for G ∈ 𝒞^1E and any start pair (the S3 start included), N5 stops after at most ITER ≤ (n(n − 1) +
      d_e)·(T*(n, m, Δ, d_e) + 1) = O(m·Δ·d_e·n¹³) iterations; with m ≤ n² and Δ, d_e ≤ n, ITER ≤ (n(n − 1) + d_e)(L(n) + 1) = O(n¹⁷),
      L(n) := T*(n, n², n, n) = O(n¹⁵). Uniform form: RESULTS R54 (c) MIRROR (b) with (H-OF) from (H-N5) by R54 (d) MIRROR (c), and (H-N5)
      from R51 (a) with T*'s monotonicity in m, Δ and d. Parameter form: R54 (c)'s and (d)'s proofs applied to the one game G^d (same n, m,
      Δ; d_o(G^d) = d_e with o = e; F = 2n²), not their uniform statements (N-1E-4); MIRROR (a) (R54 (b)) gives the n(n − 1) + d_e dual
      phases.
  (e) Corollary 1E-TIME: on 𝒞^1E, N5 from any start pair outputs W_E(G), W_O(G) and positional winning strategies for both players (σ on
      W_E, σ̄ on W_O) in O(ITER · n³(n + m)) word operations, with the O(n log n) priority ranking, i.e. in time polynomial in n + m at bit
      cost (TARGET.md §3); the class test costs O(n + m).
- Not signed (packet §6, §7): the READING on G-N5T-3 (RESULTS R15 (iii): output correctness rested on VJ00 Lemma 5.8 '1 ⇒ 2', which uses
  VJ00's unproved Lemma 5.9 and Prop. 5.10): with OUT-G signed, its premises are VJ00 (11) and R36 (c), not Lemma 5.8, 5.9 or Prop. 5.10;
  both referees concur that the output half of G-N5T-3 is thereby removed on every game, under the standing premise 1E-N3 (S1's
  procedure realises an optimal σ̄; code DATA, G-N5T-1) (N-1E-5, REFEREE §C C.4). This is recorded as a Lead
  reading in GAPS, not as a signed statement. Also not signed: the gauntlet table for 𝒞^1E, the scope reading, the frontier remark, the
  data.
- Honest limits: (i) The time bound is for a SUBCLASS that is polynomial by other means (Even has ≤ d_e positional strategies, each leaving
  a one-player game); its value is the method. (ii) It rests on RESULTS R51 and everything R51 cites (R15, R18 (d), R21, R36, R47, R48,
  R50) and on R54. (iii) OUT-G and BIT-G are about SPEC's N5 and S1 (pseudocode); the code's match is DATA (G-N5T-1). (iv) OUT-G gives
  correctness at the stop on every game; it gives no running-time bound: G-N5-TIME stays OPEN for general games. (v) Thin data for long
  runs: random 𝒞^1E runs are short (max ITER 6 in REFEREE-2's data, 8 in REFEREE's).
- Data (DATA, not proof): REFEREE (successor 12, own engine; seeds fixed or by relative path): 21,101 runs (lib41 n ≤ 64, random 𝒞^1E n
  4-30, random any-class); OUT-G checked at all 34,808 states with Iσ = ∅ (13,707 of them with Iτ ≠ ∅); ITER and σ-changes within the
  bounds on 11,846 𝒞^1E runs; 0 failures; mutation controls bite; its Zielonka agrees with Oink --zlk on the 8 lib41 𝒞^1E games.
  REFEREE-2 (successor 13, own onee_check.py: own SPEC loop, outputs checked from definitions with own Zielonka, enumerated strategies
  and a strategy verifier): 12,324 stops (7,500 random 𝒞^1E n 4-30, 4,000 any-class, 824 lib41), 0 violations; with R2-N5-1O's 7,000
  general-game stops, 19,324; mutations flip, sbar, early bite.
- Signatures: REFEREE docs/referee/R-N5-1E.md (referee c82c4ecf, successor 12; §C 6170561a): (VJ), OUT-G, BIT-G, 1E-POLY (both forms),
  1E-TIME SIGNED; notes 1E-N1..N4; no gap. REFEREE-2 docs/referee-2/R2-N5-1E.md (referee-2 ceed1f63, successor 13; §C bd68d39d, successor
  14): all SIGN; notes N-1E-1..5; no gap. §C (both): verdicts identical; joint gap map empty; 1E-N1 REFEREE's, accepted by REFEREE-2 (its
  predecessor's tick on that quote withdrawn); 1E-N2 = N-1E-2; 1E-N3 = N-1E-1; N-1E-4 = REFEREE's §4 per-game assembly; N-1E-3 closed
  (the quoted R-N5-DUAL C.2 lines exist, l. 138); nothing open.
- TARGET.md diff: OUT-G and BIT-G are statements about N5 on every game (correctness at the stop; cost per iteration); they are not a
  TARGET.md §2 claim, which needs a polynomial bound on iterations for every game. 1E-POLY / 1E-TIME are for a restricted class (TARGET.md
  §4, first bullet). Objects match TARGET.md §1 (winning regions against history-dependent strategies; positional strategies output) and §3
  (bit cost). GAPS G-N5-TIME: the row stays open (general games); subclass bounds for 𝒞^1O (R51) and 𝒞^1E (this entry) are proved.

### R58 [refereed-only] N5 on EVERY game, CONDITIONAL on RESULTS R56: with at most two Odd choice vertices per honest class, the Q-runs holding a late fallback number O(n²) per phase (Theorem FB-2T), so on two-Odd-choice games every phase of every run has at most 1 + (n − 1)(1 + 12n²) = O(n³) in-phase fallbacks (Corollary FB-2O), with Lemmas (YB_q), PFZ-q, ROUTE-2, DIR and SAT-2 (2026-10-26) — partial step-4 lemmas for N5 beyond one Odd choice vertex (a fallback count only; not an iteration bound on any class, not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C67.md, checker 36d6f3e8)
- Object (packet P-N5-2T, added at l-si f6839fd3, pinned trunk cbb3b738, unchanged during review): docs/si/P-N5-2T-box16.md, sha1
  fcb91130b1f93d041233c9def50614b4d0dc9a05 (L-SI successor 11, Opus 5.5). The referees' notes are collected by the lane in
  docs/si/P-N5-2T-fixes-box16.md (l-si 35c8eee9, sha1 8aad9f77d27a6231dd012a270882f35b437ab227, L-SI successor 11: 2T-N1 = N-2T-4,
  N-2T-1, 2T-N3 = N-2T-5, N-2T-2, N-2T-3, 2T-N2, 2T-N4 = N-2T-6 data); on trunk; repairs only.
  Setting (every game): as in RESULTS R56 (phase; g_1 < g_2 < … the in-phase fallbacks, g_j also its source state; a fallback belongs to
  the run containing its source, FBRED-N1; f^Θ_j the source of the j-th fallback whose source lies in the run Θ; Q, C, T := C ∪ Q, honest
  classes U_c, κ, κwt_c, G_c, G_c^q, κopt_c, κopt^q, Q-runs; sums of κ values are arithmetic). Q_c := (Q ∩ U_c) ∖ {c}, the terminals of
  class c; a q-run is a maximal run of the phase with Ξ(q) (equivalently κ(q)) constant; q ∈ Q_c is DIRECT at t if q lies on its own
  honest cycle at t or its honest play at t visits c before any other vertex of Q_c; d_q := |succ(q) ∩ U_c|; w_c := |U_c| − 1; Cyc_c :=
  {(0, s_c·ℓ) : 1 ≤ ℓ ≤ |U_c| − 1}. A_q := {κwt_c(q) + κopt_c(y) : y ∈ succ(q) ∩ U_c ∖ Q, κopt_c(y) defined} ∪ {κwt_c(q) : c ∈ succ(q)}
  ∪ Cyc_c; for Q_c = {q, q′}, V_{q′}(α) := {κwt_c(q′) + β_y(α) : y ∈ succ(q′) ∩ U_c, y ≠ q′, β_y(α) defined} ∪ Cyc_c with β_q(α) := α,
  β_c(α) := (0, 0) and, for y ∉ T, β_y(α) := the larger of κopt_c(y) and κopt^q(y) + α over those defined. Hypothesis (2T) for a phase:
  |Q_c| ≤ 2 for every class. 𝒞^2O := the games with exactly two Odd choice vertices.
- Claims signed (both referees "(Opus 5.5, D15)", L37), on every game and CONDITIONAL on RESULTS R56 (landed); no item uses (P); premises
  LANDED: RESULTS R56 (a), (b), (c), (f), R38 (a); the packet quotes R56 from its landed text (the κ-FB-ROUND parenthetical it quotes is
  FBRED §1.1 l. 52, not R56's own wording: N-2T-1, REFEREE-2; accepted by REFEREE):
  (a) (YB_q): if q ∈ Q_c lies on its own honest cycle at t, then P(Ξ_t q) = ∅ and 1 ≤ ℓ(Ξ_t q) ≤ |U_c| − 1, so κ_t(q) ∈ Cyc_c (proved in
      the packet, not cited: N-2T-2).
  (b) Lemma PFZ-q: R56 (c) κ-PFZ_D with "Q_c-run" weakened to "q-run" and with N-FBRED-1's range: for a q-run Θ with value κ_Θ(q), j ≥ 0,
      t ∈ Θ with t > f^Θ_j (any t ∈ Θ if j = 0), z ∈ (U_c ∖ T) ∪ {q} and every simple path p of G_c^q from z to q with ≤ j edges,
      κ_t(z) ≥ κwt_c(p ∖ {q}) + κ_Θ(q) (the weakening is safe: N-2T-3).
  (c) Lemma ROUTE-2: if Q_c = {q, q′}, at every state of the phase q or q′ is direct.
  (d) Lemma DIR: if t > g_{|U_c|−1} and q ∈ Q_c is direct at t, then κ_t(q) ∈ A_q, |A_q| ≤ d_q + w_c. Its proof never uses |Q_c| ≤ 2, so
      it holds in any class (2T-N2, REFEREE; also REFEREE-2's R2-N5-FBK §0).
  (e) Lemma SAT-2: if Q_c = {q, q′}, Θ is a q-run and t ∈ Θ with t > g_{|U_c|−1} and t > f^Θ_{|U_c|−1}, then κ_t(q′) ∈ V_{q′}(κ_Θ(q)),
      |V_{q′}(α)| ≤ d_{q′} + w_c.
  (f) Theorem FB-2T: in a phase with (2T), R56 (f)'s N_late (the Q-runs holding a fallback g_j, j ≥ n) satisfies N_late ≤ 1 + Σ_c (N_c −
      1) over the classes with Q_c ≠ ∅, where N_c := |A_q| ≤ d_q + w_c if Q_c = {q}, and N_c := |A_q|·(w_c + max_α |V_{q′}(α)|) +
      |A_{q′}|·(w_c + max_α |V_q(α)|) ≤ 2(d + w_c)(d + 2w_c), d := max(d_q, d_{q′}), if Q_c = {q, q′}. Step 3 counts distinct pair
      VALUES (b on I_α) (2T-N3 = N-2T-5, both referees).
  (g) Corollary FB-2O: on 𝒞^2O every phase of every N5 run, from every start pair, has f ≤ 1 + (n − 1)(1 + N_late) ≤ 1 + (n − 1)(1 +
      12n²) = O(n³). Its case list is read with the omitted case "both Odd choice vertices are cycle nodes", where N_late ≤ 1 (2T-N1 =
      N-2T-4, both referees, independently).
- Not signed (packet §6, §7): what else a 𝒞^2O running-time bound needs (crossings, T per phase given f) and the case of more than two
  terminals (READING; that case is RESULTS-pending P-N5-FBK's Theorem FB-kT, in review); the data. The remark after FB-2O's proof (a
  whole-run count via RESULTS R54 (e)) is not part of the signed statements.
- Honest limits: (i) A fallback count per phase, CONDITIONAL on R56; it bounds no iterations, crossings or S4a steps on any class:
  G-N5-TIME stays open, and a 𝒞^2O polynomial bound would still need crossings and transitions per phase. (ii) Vacuity (2T-N4 = N-2T-6):
  natural data never meet SAT-2's or FB-2T's hypothesis in either referee's batches (best closeness −2 on the library, −1 on random
  games); REFEREE-2 met SAT-2's hypothesis on CONSTRUCTED disjoint unions of the box-43/44 instances with small two-terminal gadgets (648 SAT
  checks over all unions, every branch of its proof exercised); the four fb17_g{3,4,5,5c}_P66.pg witnesses (docs/referee-2/R2-N5-2T/
  instances/) carry 108 of them, and REFEREE re-ran those four on its own engine (DIR 93 and SAT 108 checks, equal counts, 0 failures); FB-2T's late regime (an index ≥ n) is never reached (max f 37), so FB-2T rests on
  its proof. (iii) DIR's hypothesis is met 65 times in REFEREE's natural data. (iv) The title's O(n²) for N_late uses d_q ≤ |U_c| (by the
  definition d_q := |succ(q) ∩ U_c|), so N_c = O(w_c²), and Σ_c w_c < n; this arithmetic is in neither report (C67 N-1).
- Data (DATA, not proof): REFEREE (successor 12, own probe; path checks for n ≤ 14 by default, some batches at PATHN 16 / 40): 11,999 natural runs (lib41 × 7, lib2o × 7 and × 3,
  3,000 random 𝒞^2O × 3); PFZ-q 169,165 checks, (YB_q) and ROUTE-2 exercised often, DIR 65, 0 failures; mutation (PFZ with j +
  1 edges; DIR / SAT without Cyc_c) bites (125 PFZ failures). REFEREE-2 (successor 14, own tt_check.py, reusing successor 13's SPEC loop; lane code not run): 22,003 natural
  runs (lib41 × 2, 503 𝒞^1O files × 2, lib2o × 3, box-43/44 instances × 5, 20,000 random 𝒞^kO); (YB_q), ROUTE-2, PFZ-q and DIR checked on
  every run, 0 violations; the constructed unions above; mutations sat0 and satalpha bite. L-RED (adversary, docs/red/R76 §8, l-red 7cc9f5ac; not a
  referee check): SAT-2 exercised on climbed natural instances (sat68_n20, 68 checks), DIR 82 checks, 0 violations.
- Signatures: REFEREE docs/referee/R-N5-2T.md (referee 7055b4a5, successor 12; §C 09b5dbf5 + 906247c6): all seven statements SIGNED,
  conditional on R56; notes 2T-N1..N4; no gap. REFEREE-2 docs/referee-2/R2-N5-2T.md (referee-2 8f43432b + 416334cc and §C
  3d8de145, successor 14): all SIGN, conditional on R56; notes N-2T-1..6; no gap. §C (both): verdicts identical; joint gap map empty; 2T-N1
  = N-2T-4; 2T-N3 = N-2T-5; N-2T-1 accepted by REFEREE (missed by it); 2T-N2 REFEREE's, accepted; SAT-2 exercised on two engines; nothing
  open.
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (a per-phase fallback count, conditional on R56; no running-time bound). GAPS
  G-N5-TIME: open.

### R59 [refereed-only] N5 on EVERY game: after j in-phase fallbacks, the honest κ-values of every honest class are at least the j-step value of that class's min-max reachability game (Lemma VI-LB), i.e. every in-phase fallback is at least one round of value iteration on it (2026-10-26) — a LOWER bound on progress (no count of fallbacks, S4a steps, crossings or phases; not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C68.md, checker cf48d915)
- Object (packet P-N5-VILB, added at l-new 999e73f4, pinned trunk e7febdc2, unchanged during review): docs/new/P-N5-VILB-box44.md, sha1
  872d4400194ed9d0f6ad9f6a2cc82f2f0821cd9f (L-NEW successor 23, Opus 5.5). The referees' notes are collected by the lane in
  docs/new/P-N5-VILB-fixes-box44.md (l-new 1c344659, sha1 56da789eb295591dada219db9eab41358583211b, L-NEW successor 24: VILB-N1 = N-VILB-1,
  N-VILB-2, VILB-N2 data); on trunk; repairs only, no signed statement changes.
  Setting (every game): N5 = SPEC S1-S5; phases as in RESULTS R38 (a); an in-phase transition is an S4a step or an Even S4c fallback; g_1
  < g_2 < … the in-phase fallbacks ("t > g_0" means every state); next_t(v) := σ_t(v) for Even v, σ̄_t(v) for Odd v; for a cycle node c
  of the phase, U_c := λ^{-1}(c); wt_c, s_c, κwt_c and κ_t on U_c as in RESULTS R56. The game Γ_c: vertices U_c; at an Even vertex the
  maximiser and at EVERY Odd vertex the minimiser choose a successor inside U_c; target c with value (0, 0); a play pays the sum of κwt_c
  over its vertices before c, and −∞ if it never reaches c. Val^{≤0}_c(c) := (0, 0), Val^{≤0}_c(z) := −∞ for z ≠ c; for j ≥ 1,
  Val^{≤j}_c(c) := (0, 0) and Val^{≤j}_c(z) := κwt_c(z) + max (Even z ≠ c), respectively min (Odd z ≠ c), over x ∈ succ(z) ∩ U_c of
  Val^{≤j−1}_c(x). For z ∈ U_c ∖ {c} the empty-set conventions of the packet never fire, since by (Aκ) succ(z) ∩ U_c ≠ ∅ (VILB-N1 =
  N-VILB-1, both referees).
- Claims signed (both referees "(Opus 5.5, D15)", L37), on every game; no item uses (P); premises LANDED: RESULTS R17 (a) (V1), R15 (a),
  R38 (a), SPEC S1, S2, S4c (FIX 3):
  (a) Facts (Aκ), (M1κ), (M2κ) and Lemma κ-FB-ROUND (at an in-phase fallback k → k+1, for every Even v ∈ U_c ∖ {c} and every successor
      x ∈ U_c of v, κ_{k+1}(v) ≥ κwt_c(v) + κ_k(x)), restated with proofs as in RESULTS R48 / R56 (a) with c for c_θ.
  (b) Lemma VI-LB: for every phase, every cycle node c of it, every j ≥ 0, every state t of the phase with t > g_j and every z ∈ U_c,
      κ_t(z) ≥ Val^{≤j}_c(z). The Odd step uses only (Aκ) at t and the induction hypothesis at t, for choice and forced Odd vertices
      alike (N-VILB-2, REFEREE-2; the same step in REFEREE's report).
- Not signed (packet §2 remark, §3, §4): the relation to R48's κ-HAT-FREEZE (a) (an agreed READING: VI-LB is its two-player form); what
  VI-LB does not give (no upper bound κ_t ≤ Val_c, hence no freeze; no count; no claim that N5 does one VI round per fallback; values over
  walks vs N5's simple-path values); the cross-field reading via [BGHM] (T. Brihaye, G. Geeraerts, A. Haddad, B. Monmege, arXiv:1407.5030v4,
  §3 Algorithm 1, Theorem 1 item 4: value iteration on min-cost reachability games is pseudo-polynomial, exponential with 2^rank
  weights; source opened by the lane, sha256 in notes/L-NEW.md) and the obstruction shape (Figure 2(a) mirrored into U_c). The
  obstruction did not materialise: built as N5 games, the gadget collapses to ≤ 1 iteration and 0 fallbacks from every start pair (L-RED
  docs/red/R76, l-red 2207620f, instances bghm_k1_gap6_A, bghm_k3_gap4_A; DATA), a READING consistent with the lane's Lemma ACCEL (RESULTS R60;
  positional simple-path values; R76 §2).
- Honest limits: (i) A LOWER bound only: it bounds no count of anything, and it does not make f polynomial. (ii) The regime where it
  could force a count (many fallbacks in one phase) is not reached in any data (max 33 in-phase fallbacks in lib41, 37 in REFEREE-2's
  𝒞^1O files; never ≥ n).
- Data (DATA, not proof; VILB-N2): REFEREE (successor 12, own vilb_probe.py): 7,151 runs, 20,531 phases, 777,048 VI-LB checks, tight at
  61,861 of 105,188 finite lib41 checks (59 %), 0 failures; mutation oddmax (Odd maximises) fails 46,067 times. REFEREE-2 (successor 13,
  own va_check.py): 70,288 runs (incl. 47,996 climb runs), 161,847 phases, 2,677,247 VI-LB checks, 0 violations; the control "one round
  too many" (Val^{≤j+1}) fails 774 times on lib41, so the bound is attained at round j in data.
- Signatures: REFEREE docs/referee/R-N5-VILB.md (referee dcb1451c, successor 12; §C 09b5dbf5): §1 and VI-LB SIGNED; notes VILB-N1, VILB-N2;
  no gap. REFEREE-2 docs/referee-2/R2-N5-VILB.md (referee-2 f0e82d8a, successor 13; §C 5ad79417, successor 14): all SIGN; notes N-VILB-1,
  N-VILB-2; no gap. §C (both): verdicts identical; joint gap map empty; VILB-N1 = N-VILB-1; the Odd step = N-VILB-2; nothing open.
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (a lower bound on progress; no running time). GAPS G-N5-TIME: open.

### R60 [refereed-only] N5 on EVERY game: inside a phase, every switching transition of a non-cycle-node Even vertex raises its κ-value through the finite set of its simple-path levels, so in-phase fallbacks are at most 1 + N_K (Lemma ACCEL); and inside each epoch of Odd's best response the honest values freeze at the one-player optimum after n − 1 fallbacks, so f ≤ 1 + n·N_ep (Lemma EPOCH) (2026-10-26) — partial step-4 lemmas for N5 beyond one Odd choice vertex (neither gives a polynomial bound: N_K can be exponential, N_ep is not bounded here; not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C69.md, checker 81f75721)
- Object (packet P-N5-ACCEL, added at l-new e9eaaaaf, pinned trunk e7febdc2, unchanged during review): docs/new/P-N5-ACCEL-box44.md, sha1
  301f0be0fa2b2240bba59b347dfbee8426b8dba3 (L-NEW successor 23, Opus 5.5). The referees' notes are collected by the lane in
  docs/new/P-N5-ACCEL-fixes-box44.md (l-new 1c344659, sha1 46ef947403eaea1606837b261c4827aeabd352d3, L-NEW successor 24: N-ACC-2,
  ACCEL-N1 = N-ACC-1, ACCEL-N2, ACCEL-N3 = N-ACC-3, data); on trunk; repairs only, no signed statement changes.
  Setting (every game): N5 = SPEC S1-S5; honest frame next_t(v) := σ_t(v) (Even), σ̄_t(v) (Odd); phases as in RESULTS R38 (a); an in-phase
  transition is an S4a step or an Even S4c fallback; f := the in-phase fallbacks of a phase; C, Q, T := C ∪ Q, U_c, wt_c, s_c, κwt_c and κ
  as in RESULTS R56; at a fallback k → k+1, S_k := the switched Even vertices (= the gate sources, S4c) and S := S_k ∖ T. K_c(z) := {κwt_c(p ∖ {c}) : p a simple path of G[U_c] from z to c}. An EPOCH: a
  maximal run E of consecutive states of a phase on which σ̄_t|Q is constant; G_E := G with every Odd vertex fixed to σ̄_E; opt_E(z) := the
  best κwt_c-weight of a simple path of G_E[U_c] from z to c; e_1 < e_2 < … the in-phase fallbacks k → k+1 with k ∈ E; N_ep := the epochs
  of the phase.
- Claims signed (both referees "(Opus 5.5, D15)", L37), on every game; no item uses (P); premises LANDED: RESULTS R17 (a) (V1), R15 (a),
  R15 (d), R19 (d)'s step (SG) ("on all games, not only 𝒞^1O"; its proof uses only R15 (a), the gate, (V1) and strict (V2): ACCEL-N1 =
  N-ACC-1, both referees), R38 (a), R38 (f) CN-LAST (every game), SPEC S1, S2, S4a, S4c; and (VJ) (RESULTS R57 (a), with P-N5-1E §2's
  argument that SPEC's Ξσ is VJ00's Ω_σ, checked by both referees; under R57's standing premise 1E-N3), so R15 (d) applies to Ξ (ACCEL-N2, REFEREE; accepted by REFEREE-2):
  (a) Facts (Aκ), (A0κ), (M1κ), (M2κ), (INJ), (SP′), κ-FB-ROUND and CN-ONLY_D, restated with proofs (as in RESULTS R56).
  (b) Lemma ACCEL: in every phase, (a) κ_t(z) ∈ K_c(z) for every state t and z ∈ U_c; (b) the in-phase transitions at which some Even z
      with λ(z) ≠ z switches number at most N_K := Σ_{c ∈ C} Σ_{Even z ∈ U_c ∖ {c}} (|K_c(z)| − 1); (c) f ≤ 1 + N_K.
  (c) Lemma EPOCH: for every phase and epoch E, (a) for t ∈ E with t > e_j and z ∈ U_c, κ_t(z) ≥ the best κwt_c-weight of a simple path of
      G_E[U_c] from z to c with ≤ j edges, and κ_t(z) ≤ opt_E(z) for every t ∈ E; hence κ_t = opt_E on every class for t ∈ E with t >
      e_{n−1}; (b) no transition with both ends in E after e_{n−1} switches an Even z with λ(z) ≠ z, and the part of E after e_{n−1} has at
      most 4n(n − 1) + 1 transitions; (c) f ≤ 1 + n·N_ep.
  Consequence noted by REFEREE-2 and checked by REFEREE (N-ACC-2; it follows from the signed EPOCH (a) and is not a separate statement): for
  every class c and t ∈ E with t > e_{|U_c|−1}, κ_t = opt_E on U_c.
- Not signed (packet §4): what the lemmas do not give (|K_c(z)| can be exponential; no bound on N_ep or on an epoch's S4a steps before its
  freeze); the READING that value-iteration gadgets do not force many N5 switches (consistent with L-RED's built gadget, which collapses:
  docs/red/R76, l-red 2207620f; DATA); the σ̄|Q-repeat instance; the data.
- Honest limits: (i) Neither lemma is a polynomial bound: N_K can be exponential, and N_ep is not bounded here. σ̄|Q REPEATS inside a phase,
  so N_ep is not bounded by the number of σ̄|Q configurations: experiments/new/box25/laps/lap_n6_s1_110421.pg (n 6, Q = {2}, sha1
  4f4fe69c51e1c6f170c9c732feca025da70e7edb), σ̄_t(2) = 0, 4, 0 in one phase, reproduced by REFEREE; repeats in 203 lib41 phases (3 starts)
  and 187 phases of REFEREE-2's 𝒞^1O files; up to 50 epochs in one phase (lev_l_x.pg) and 53 (rise_thin51_n40). (ii) Vacuity (ACCEL-N3 =
  N-ACC-3): EPOCH's global frozen regime (an epoch with ≥ n − 1 in-phase fallbacks) is never reached (REFEREE 0 times; REFEREE-2's best epoch
  1 short in the library, 2 short after four climbs aimed at it, 47,996 runs); EPOCH (a)'s global freeze and (b) rest on their proofs. The
  per-class freeze (N-ACC-2) is reached in data.
- Data (DATA, not proof): REFEREE (successor 12, own engine): lib41 n ≤ 64, the box-43/44 instances, 2,000 random games, 0 failures;
  reproduces the packet's 112 switching transitions and 50 epochs in one phase; 410 switches of Even cycle nodes, none raises κ, so (SG)'s
  hypothesis λ(y) ≠ y cannot be dropped (accepted by REFEREE-2). REFEREE-2 (successor 13, own checker): 51,331 switches, all gaining strictly;
  the per-class freeze checked 18,251 times plus 38,213 in climbs, 0 violations; mutations sg and kk bite (vi, in the same batch, is
  VILB's), ep does not (f stays far below n·N_ep).
- Signatures: REFEREE docs/referee/R-N5-ACCEL.md (referee a19cdff7, successor 12; §C 09b5dbf5): §1, ACCEL (a)-(c), EPOCH (a)-(c) SIGNED; notes
  ACCEL-N1..N3; no gap. REFEREE-2 docs/referee-2/R2-N5-ACCEL.md (referee-2 f0e82d8a, successor 13; §C 5ad79417, successor 14): all SIGN; notes
  N-ACC-1..3; no gap. §C (both): verdicts identical; joint gap map empty; ACCEL-N1 = N-ACC-1; ACCEL-N3 = N-ACC-3; N-ACC-2 accepted by REFEREE
  (missed by it); ACCEL-N2 REFEREE's, accepted; nothing open.
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (no polynomial bound). GAPS G-N5-TIME: open.

### R61 [refereed-only] N5 on EVERY game, CONDITIONAL on RESULTS R56 and R58: the "routes-through" relation among the Odd choice vertices of an honest class is acyclic (ROUTE-k), a routed terminal's value is a shift of its parent's (SAT-k), so the Q-runs holding a late fallback are polynomially many whenever classes have boundedly many Odd choice vertices (Theorem FB-kT): on 𝒞^kO with k fixed, f = O(n^{k+1}) in-phase fallbacks per phase (Corollary FB-kO); and a clean change of Odd's best response at q strictly raises κ(q) unless tied (Lemma ALT), so epochs are bounded by ρ plus ties, non-clean and cycle-node changes (Corollary N_ep) (2026-10-26) — partial step-4 lemmas for N5 (a fallback count; not an iteration bound on any class; not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C70.md, checker 761bcc73)
- Object (packet P-N5-FBK, added at l-new 9dd499d3, pinned trunk 5d723af6, unchanged during review): docs/new/P-N5-FBK-box44.md, sha1
  afd7c65a265053531171b66294811bbd9a801dd2 (L-NEW successor 23, Opus 5.5). Two correction layers, both on trunk, repairs only, no signed
  statement changes: docs/new/P-N5-FBK-fixes-box44.md (l-new 399e8ec6, sha1 79ad8597b2eb54f56b65718baa89d69b90543a68, written before
  review: verbatim quotes of P-N5-2T's PFZ-q, DIR, A_q and DIRECT, checked verbatim by both referees) and docs/new/P-N5-FBK-fixes2-box44.md
  (l-new 2cf61061, sha1 c6c4569120455a9b578570891a251bff90a30dd6, L-NEW successor 24: FBK-1 = G-FBK-1, N-FBK-1, N-FBK-2, FBK-N1 = N-FBK-4,
  FBK-N2 ⊇ N-FBK-3, data).
  Setting (every game): as in RESULTS R56 and R58 (phases, g_j source states, Q, C, T, U_c, κ, κwt_c, G_c, G_c^q, κopt_c, κopt^q, Q-runs;
  Q_c := (Q ∩ U_c) ∖ {c}, m_c := |Q_c|, w_c := |U_c| − 1, d_q, DIRECT, A_q, q-runs, f^Θ_j; N_late := the Q-runs holding a fallback g_j,
  j ≥ n). For q ∈ Q_c not direct at t, par_t(q) := the first vertex of Q_c ∖ {q} on q's honest play at t. D_c := max_{q ∈ Q_c} d_q + w_c
  (≤ 2n). 𝒞^kO := the games with exactly k Odd choice vertices. An EPOCH: a maximal run of a phase with σ̄|Q constant; N_ep := their number.
- Claims signed (both referees "(Opus 5.5, D15)", L37), on every game, CONDITIONAL on RESULTS R56 and on P-N5-2T's PFZ-q and DIR (now
  landed as RESULTS R58 (b), (d)); no item uses (P); premises LANDED: R15 (a), R54 (e), R56 (a), (b), (d), (f), R58 (a), (b), (d). FB-kT
  step 1 also uses (INJ) (R56 (a)), which the packet's §0 omits (N-FBK-2, accepted by REFEREE), and the "(YB as used there)" of §0 is
  P-N5-2T's (YB_q), i.e. R58 (a), not an R56 fact (N-FBK-1, accepted by REFEREE):
  (a) Lemma ROUTE-k: the relation q → par_t(q) has no cycle; every chain ends at a direct terminal, and the depth of q is ≤ m_c − 1.
  (b) Lemma SAT-k: if t > g_{w_c}, q ∈ Q_c is not direct at t, p := par_t(q), Θ_p is the p-run containing t and t > f^{Θ_p}_{w_c}, then
      κ_t(q) ∈ S_{q,p} + κ_t(p), with S_{q,p} := {κwt_c(q) + κopt^p(y) : y ∈ succ(q) ∩ U_c ∖ T, κopt^p(y) defined} ∪ {κwt_c(q) : p ∈ succ(q)},
      |S_{q,p}| ≤ d_q. The hypothesis t > g_{w_c} is unused (FBK-N1 = N-FBK-4).
  (c) Theorem FB-kT: in every phase, N_late ≤ 1 + Σ_c Σ_{q ∈ Q_c} (V_q − 1), with V_q the number of distinct values of κ(q) at the late
      fallbacks and V_q ≤ Σ_{h=0}^{m_c−1} D_c·((m_c − 1)·D_c)^h ≤ m_c·D_c·((m_c − 1)·D_c)^{m_c−1}; with R56 (f), f ≤ 1 + (n − 1)(1 + N_late).
  (d) Corollary FB-kO, per phase: on 𝒞^kO every phase of every N5 run from every start pair has N_late ≤ 1 + k·(2n)·k·(2(k − 1)n)^{k−1} and
      f ≤ 1 + (n − 1)(1 + N_late) = O(k^{k+1}·2^k·n^{k+1}); for fixed k, f = O(n^{k+1}). The packet's last sentence (whole runs) reads, after
      the joint repair FBK-1 = G-FBK-1 (found independently by both referees): "the in-phase fallbacks of a whole run are O(n^{k+1}(n² +
      n^k)): O(n^{2k+1}) for fixed k ≥ 2, O(n⁴) for k = 1". The per-phase bounds are unaffected.
  (e) Lemma ALT: for an in-phase transition t → t+1 and q ∈ Q_c, q ≠ c, with y1 := σ̄_t(q) ≠ y2 := σ̄_{t+1}(q), call the change CLEAN if q
      lies on no honest cycle at t and at t + 1 and y2's honest play at t avoids q; then a clean change has κ_{t+1}(q) ≥ κ_t(q), with
      equality only if κ_t(y2) = κ_t(y1) and κ_{t+1}(y2) = κ_t(y2) (a TIE at t). Its "≥" is (M2κ); its content is "strict unless a tie";
      the step at t + 1 is (Aκ), which needs only q ≠ c, so "q on no honest cycle at t + 1" is unused (FBK-N2 ⊇ N-FBK-3, both referees).
  (f) Corollary (N_ep): N_ep ≤ 1 + Σ_{q ∈ Q} (ρ_q + tie_q + nc_q + cyc_q), where ρ_q counts the transitions of the phase changing Ξ(q), tie_q
      the clean ties at q, nc_q the non-clean changes at q, and cyc_q the changes at q while λ(q) = q.
- Not signed (packet §5): the model obstruction (the lemmas used admit abstract tuple sequences with D^{depth} values per terminal, so no
  SUM bound over terminals follows from them alone; a statement about the lemmas, not about N5); the data; what N5 on 𝒞^kO still needs
  (crossings per phase, transitions per phase given f; READING); the ALT reading that epochs and ρ count the same quantity up to residuals.
- Honest limits: (i) A fallback count per phase, conditional on R56 and R58; no iterations, crossings or S4a steps are bounded, and for k
  not fixed the bound is exponential in k. (ii) Vacuity: FB-kT's late regime (an index ≥ n) is never reached in data; SAT-k's hypothesis is
  met only on constructed unions (REFEREE-2's fb17_k3_P66.pg, a 3-terminal chain class, at depths 1 and 2), re-run on both engines.
  (iii) ALT's residuals are not always small: 33 % non-clean changes on one climbed instance (L-RED rho3_253_n32, R76 §8; DATA).
- Data (DATA, not proof): REFEREE (successor 12, own engine): 14,874 runs (lib41 with 6 random starts, the lib2o list, random 𝒞^3O,
  𝒞^4O, and the four 2T witnesses), 0 failures; ROUTE-k holds with depth up to 15 in its batches (118 in its §C run); ALT 7,354 σ̄(q) changes, no violation; SAT-k 37 checks on REFEREE-2's 2T witnesses
  and 26 on fb17_k3_P66 (equal to REFEREE-2's count), 0 failures, the mutation fails all 37. REFEREE-2 (successor 14, own fbk_check.py; lane
  code not run): ROUTE-k 246,592 checks, depth up to 118 (tcL_N12, 233 terminals in one class), no cycle; ALT reproduces the lane's lib41
  counts exactly (1,910 clean strict, 75 ties, 65 non-clean, 1 at a cycle node), every clean equality a tie; SAT-k 76 checks on the k3
  gadget at depths 1 and 2, 0 violations; mutations satk0 (4) and shift (76 / 76) bite.
- Signatures: REFEREE docs/referee/R-N5-FBK.md (referee c7fa8d5e, successor 12; §C 0e4ba6ee): ROUTE-k, SAT-k, FB-kT, FB-kO per phase, ALT and
  its corollary SIGNED, conditional; GAP FBK-1 (FB-kO's whole-run sentence); notes FBK-N1..N3. REFEREE-2 docs/referee-2/R2-N5-FBK.md
  (referee-2 d4cc40d9, Addendum A 5ad79417 on the pre-review fixes file and §C 9a482c93, all successor 14): all SIGN, conditional;
  minor gap G-FBK-1 (the same sentence); no inherited gap from P-N5-2T; notes N-FBK-1..4. §C (both): verdicts identical; the one gap is
  joint, FBK-1 = G-FBK-1, the two repairs giving the same bound, closed by fixes2 §1; N-FBK-1, N-FBK-2 accepted by REFEREE (missed by it);
  FBK-N1 = N-FBK-4; FBK-N2 ⊇ N-FBK-3; nothing open.
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (a per-phase fallback count, conditional; no running-time bound). GAPS G-N5-TIME:
  open.

### R63 [refereed-only] N5 on EVERY game: at an in-phase S4a step a split vertex never leaves the disagreement region (R-STICK_D), unsplit states form a prefix of each S4a run (SN-PREFIX_D), the disagreement set changes only at epoch boundaries (D-EPOCH), and crossings per phase are at most (N_ep − 1) + N_ep·O(n²) + Σ_E X_SN^pre(E) (Lemma X-EP), so every crossing outside a residual inside fixed-frame S4a runs is charged to epochs, hence (with ALT) to ρ and its residuals (2026-10-26) — partial step-4 lemmas for N5 beyond one Odd choice vertex (a reduction; the residual X_SN^pre is OPEN; not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C72.md, checker a42e44f8)
- Object (packet P-N5-XEP, added at l-new a4fa94b0, pinned trunk 8460897d, unchanged during review): docs/new/P-N5-XEP-box44.md, sha1
  237dd5eb31f60f19ef70099dc9351532e88b56f8 (L-NEW successor 23, Opus 5.5). The referees' notes are collected by the lane in
  docs/new/P-N5-XEP-fixes-box44.md (l-new 2c02b015, sha1 639a70981b5fa0161e92b5b6111a6ce5dc57f3cf, L-NEW successor 24: XEP-N1 = N-XEP-1,
  N-XEP-2, XEP-N2, XEP-N3 data); on trunk; repairs only, no signed statement changes.
  Setting (every game): N5 = SPEC S1-S5; state k = (σ_k, τ_k); σ̄_k, Ξ_k, λ, W_k (σ_k's valuation in G_τ), λ_W as in RESULTS R55; phases as
  in RESULTS R38 (a); f := the in-phase fallbacks of a phase. D_k := {Odd u : σ̄_k(u) ≠ τ_k(u)}; R_D(k) := the vertices whose (σ_k,
  τ_k)-play meets D_k; F_D(k) := V ∖ R_D(k). A vertex v is SPLIT at k if λ_{W,k}(v) ≠ λ(v), UNSPLIT otherwise. A CROSSING is an in-phase
  transition s → s+1 with R_D(s) ≠ R_D(s+1); X_D := the crossings of the phase. Q := the Odd vertices of out-degree ≥ 2; an EPOCH is a
  maximal run of the phase with σ̄|Q constant, N_ep := their number, and e_1 < e_2 < … the in-phase fallbacks of an epoch E (by source).
  X_SN^pre(E) := the crossings with both ends in E and source state ≤ e_{n−1} (all of E's crossings if E has fewer than n − 1 fallbacks)
  at which some vertex unsplit at the source changes R_D-membership.
- Claims signed (both referees "(Opus 5.5, D15)", L37), on every game; no item uses (P); premises LANDED: RESULTS R55 (a) G_D (a), R21 (a)
  XW, R23 (g) WM (signed under a 𝒞^1O line; its proof, P-N5-Z §8, is game-general, and so is the route via (F1) in G_τ with (VJ) of R57:
  XEP-N2 = REFEREE-2 §1, both referees), R38 (a), and RESULTS R60 (c) Lemma EPOCH (b); §4's last line uses RESULTS R61 (e)-(f) (ALT and its
  N_ep corollary):
  (a) Lemma R-STICK_D: at an in-phase S4a transition s → s+1, every split v ∈ R_D(s) lies in R_D(s+1), whatever D_{s+1} is.
  (b) Corollary SN-PREFIX_D: (a) along a run of consecutive in-phase S4a transitions, for each vertex v the states at which v is unsplit
      form a prefix of the run; (b) after its unsplit prefix a vertex changes its R_D-membership at most once (it may enter R_D, and never
      leaves); (c) per phase, X_D ≤ (f + 1)·n + f + X_SN^D, where X_SN^D := the crossings at which some vertex unsplit at the source changes
      R_D-membership.
  (c) Fact D-EPOCH: on a phase, D_s changes only at epoch boundaries; on an epoch E, D and σ̄ are constant, the honest frame is the
      one-player game G_E (Odd fixed to σ̄_E) and the W-frame is the one-player game G_τ, and they differ exactly at the vertices of D; in
      particular σ̄(c) is constant on each epoch for an Odd choice vertex c that is an honest cycle node of the phase.
  (d) Lemma X-EP: for every phase, X_D ≤ (N_ep − 1) + N_ep·(n² + n + 4n(n − 1)) + Σ_E X_SN^pre(E). With RESULTS R61 (f), N_ep ≤ 1 +
      Σ_{q ∈ Q} (ρ_q + tie_q + nc_q + cyc_q), hence X_D = O(n²)·(1 + ρ + ties + non-clean + cycle-node changes) + Σ_E X_SN^pre(E): signed as
      an inequality; the packet's clause "every crossing outside the residual is charged to the quantity that also bounds fallbacks (R56 (f))"
      is a READING, since R56 (f) bounds f by ρ only and ties, non-clean and cycle-node changes are extra (N-XEP-2, REFEREE-2; accepted by
      REFEREE).
  Sharpening (XEP-N1 = N-XEP-1, found independently by both referees; the packet's weaker forms are true as written): by R55 (a) every split
  vertex already lies in R_D, so R-STICK_D's hypothesis v ∈ R_D(s) is automatic, split vertices never change membership at S4a transitions,
  SN-PREFIX_D (b)'s "at most once" is "never", and so X_D ≤ f + X_SN^D, and X-EP holds without the n² term: X_D ≤ (N_ep − 1) + N_ep·(n + 4n(n
  − 1)) + Σ_E X_SN^pre(E).
- Not signed (packet §5): the qc_toggle configuration instance (experiments/new/box44/instances/qc_toggle.pg, n 5, sha1
  27850ecc3d9e660aefa6a3401d6af0cfc2b3317c: every honest cycle node is the Odd choice vertex 4, and an unsplit vertex enters R_D at an S4a
  step; a configuration, not a counterexample); the residual X_SN^pre (OPEN; for epochs with |D| ≤ 1 L-NEW's P-N5-EPR, in review, reduces it
  to one-Odd-choice phases, for |D| = 1 under its premise (Στ); |D| ≥ 2 needs Δ-RT); the data.
- Honest limits: (i) A REDUCTION: N_ep (equivalently ρ and its residuals) and X_SN^pre are not bounded here. (ii) Most crossings are in the
  residual: of lib41's 3,222 crossings (S3 start), 1,269 are at epoch boundaries, 1,833 are X_SN^pre and 120 have only split changers (all
  at fallback transitions), none after an epoch freeze. (iii) EPOCH (b)'s term is vacuous in data (XEP-N3).
- Data (DATA, not proof): REFEREE (successor 12, own engine, random start pairs): 11,302 runs, 0 failures; G_D (a) 1.58M and WM 0.85M
  checks; reproduces the packet's lib41 S3 figures exactly (R-STICK_D 14,253 checks; 3,222 = 1,269 + 1,833 + 120) and qc_toggle. REFEREE-2
  (successor 14, own xep_check.py, S3 and random start pairs; lane code not run): 23,381 runs (22,969 plus its lib41 S3-only row), 66,022 phases, 0 violations; reproduces the
  same lib41 counts exactly (178 split-only crossings over its starts, all at fallbacks); mutations rstick_all (6,444) and xsn0 (607) bite.
- Signatures: REFEREE docs/referee/R-N5-XEP.md (referee 62f4bd2c, successor 12; §C ead5fdb3): R-STICK_D, SN-PREFIX_D (a)-(c), D-EPOCH, X-EP
  SIGNED; notes XEP-N1..N3; no gap. REFEREE-2 docs/referee-2/R2-N5-XEP.md (referee-2 fd43a69f, §C b7b04fad, successor 14): all SIGN; notes
  N-XEP-1, N-XEP-2; no gap. §C (both): verdicts identical; joint gap map empty; XEP-N1 = N-XEP-1 with REFEREE's extension (drop the n² term)
  accepted by REFEREE-2; N-XEP-2 accepted by REFEREE; XEP-N2 = REFEREE-2 §1; nothing open.
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (a reduction; no running time). GAPS G-N5-TIME: open.

### R64 [refereed-only] N5 on EVERY game: inside an epoch (σ̄|Q constant within a phase) N5 runs, state by state, as the variant N5^τ on the restricted game G′_E in which only the epoch's disagreement vertices keep a choice (RESTRICT_E, REPRO); an epoch with no disagreement has at most n + m in-phase transitions (EP-0); per phase, in-phase transitions are the sum over epochs of at most one N5^τ phase plus one (EP-k); and, under premise (Στ), an epoch with one disagreement vertex has at most T*(G′_E) + 1 = O(m·Δ·n¹¹) (EP-1, an implication) (2026-10-26) — partial step-4 lemmas for N5 beyond one Odd choice vertex (a reduction: the number of epochs is not bounded here; not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C73.md, checker 7b326f11)
- Object (packet P-N5-EPR, added at l-new 08abd9cb, pinned trunk a3b1cff3, unchanged during review): docs/new/P-N5-EPR-box45.md, sha1
  8fecca797478d1a77564ac1c5b82d11e952559e0 (L-NEW successor 24, Opus 5.5). The referees' notes are collected by the lane in
  docs/new/P-N5-EPR-fixes-box45.md (l-new 5d14c991, sha1 5af1fde6f0c1a926bb556ecbe47cc2c0f3d562d3, L-NEW successor 24: EPR-1 = G-EPR-1,
  EPR-N1, N-EPR-1, the (Στ) list, data); on trunk; repairs only.
  Setting (every game): N5 = SPEC S1-S5 (with FIX 1-4, Q1-Q4); n := |V|, m := |E|, Δ := the maximum out-degree; state k = (σ_k, τ_k);
  σ̄_k := S1's Odd counterstrategy to σ_k; Ξ_k := V_{σ_k,σ̄_k}; W_k := V_{σ_k,τ_k}; λ := Ξ's cycle-node map; phases as in RESULTS R38 (a);
  Q := the Odd vertices of out-degree ≥ 2. An EPOCH is a maximal run E = (x, …, y) of a phase on which σ̄|Q is constant; σ̄_E, D_E := {u ∈ Q
  : σ̄_E(u) ≠ τ(u)}; len(E) := the in-phase transitions whose source lies in E. G′_E: G with every Odd v ∉ D_E cut to τ(v) and every u ∈ D_E
  cut to {τ(u), σ̄_E(u)}; so G′_E ∈ 𝒞^{|D_E|}O with every Odd choice vertex of out-degree 2. N5^τ: SPEC N5 with S4b replaced by S4b^τ (if
  Iτ ≠ ∅ and τ is value-optimal against σ in S4b's arena, keep τ; otherwise SPEC's S4b).
- Claims signed (both referees "(Opus 5.5, D15)", L37), on every game; no item uses (P); premises LANDED: SPEC; RESULTS R18 (d) Lemma S (a)
  (= (VJ), signed on every game in RESULTS R57 (a)); R17 (c), (e); R38 (a); and, for EP-1 only, R48 (i), R50 (h), R51 (a), (b) read through
  premise (Στ). RESTRICT_E (i) rests on the standing SPEC premise that S1's counterstrategy is optimal (1E-N3, RESULTS R57; N-EPR-1, a
  landing note):
  (a) Lemma RESTRICT_E: for an epoch E and k ∈ E, at the pair (σ_k, τ): (i) Ξ′_k = Ξ_k and W′_k = W_k; (ii) Iσ′_k = Iσ_k, SPEC S4a's output on
      G′_E equals its output on G, and S4c's Even switch-all on Iσ is the same on both; (iii) Odd's dual valuation of τ is the same on both,
      so Iτ′_k = Iτ_k ∩ E(G′_E); (iv) if k → k+1 is an in-phase transition of N5 on G and Iτ′_k ≠ ∅, then τ is value-optimal against σ_k in
      S4b's arena of G′_E.
  (b) Corollary REPRO, read with the joint repair EPR-1 = G-EPR-1 (found independently by both referees): N5^τ on G′_E from the start pair
      (σ_x, τ) passes through the pairs (σ_x, τ), …, (σ_{y′}, τ), y′ := x + len(E), with the same fallback / non-fallback type at each of its
      len(E) transitions as N5 on G; the states x, …, y lie in ONE phase of that N5^τ run, and the last transition y → y′ has its source there
      and may leave it. The packet's clause that y′ also lies in that phase is FALSE in general: RESTRICT_E (i) needs σ̄_k = σ̄_E, and y + 1
      ∉ E (witnesses below).
  (c) Corollary EP-0: if D_E = ∅, then len(E) ≤ n + m. The statement stands; its proof covers the exit or fallback-last case (EPR-N1).
  (d) Corollary EP-k (a REDUCTION), with the repair: for every phase P of N5 on any game, the in-phase transitions of P number Σ_E len(E)
      over its epochs, and for each epoch len(E) ≤ 1 + the in-phase transitions of one phase of an N5^τ run on G′_E ∈ 𝒞^{|D_E|}O started at
      (σ_x, τ).
  (e) Corollary EP-1, an IMPLICATION, with the repair: premise (Στ) — RESULTS R48 (i) (f ≤ 1 + (n − 2)(2n − 1) ≤ 2n², as used by R51 (a)) and
      R50 (h), with the per-phase statements they cite and their own landed chains, hold for every phase of every N5^τ run on every 𝒞^1O
      game from every start pair — implies that every epoch E with D_E = {u} has len(E) ≤ T*(G′_E) + 1, with T* R51 (a)'s per-phase bound at
      G′_E's parameters (n, m′ ≤ m, Δ′ ≤ Δ, d_o = 2); so len(E) = O(m·Δ·n¹¹). (Στ) is NOT claimed here. The packet's (Στ) list names R49
      under R48; R48 does not cite R49, so that entry is spurious and only strengthens the premise (fixes §2, lane remark). REFEREE-2 checked
      the list item by item against R51 (a)'s per-phase citations (R36 (c), R47 (b) rightly absent); REFEREE accepts that as the stronger
      form of its catch-all reading.
  (f) Consequence: every count inside one epoch (its S4a steps, fallbacks, crossings, in particular RESULTS R63's residual X_SN^pre(E)) is
      ≤ len(E); so X_SN^pre(E) ≤ n + m if D_E = ∅, and, under (Στ), O(m·Δ·n¹¹) if |D_E| = 1.
- Not signed (packet §4-§6): the (Στ) audit as written in the packet (a text search; READING), Lemma TIE-W (offered, not needed), the data,
  and the combination with ALT (READING). L-NEW's later line-by-line audit of (Στ) (docs/new/N5-EPR-box45.md §9, l-new bcca6c83, a198c9b9;
  Lemma Στ-STEP lane-PROVED plus a per-entry table) is a premise check for a separate packet (P-N5-STAU), not part of this entry.
- Honest limits: (i) A REDUCTION: the number of epochs per phase (N_ep, tied to ρ and its residuals by RESULTS R61 (f)) is not bounded, and
  epochs with |D_E| ≥ 2 are not bounded here. (ii) EP-1 is conditional on (Στ). (Στ) IS exercised: on L-NEW's DIV instance
  experiments/new/box45/instances/div_n8.pg (n 8, sha1 4ed57ef2c1c92ee526ccd2683ae7c28b1caf5bfa, with div_n8.start) SPEC's S4b on G′_E moves
  τ inside an epoch while N5^τ keeps it, reproduced on both referees' engines; so the packet's §5 line "(Στ) is never exercised" holds
  only for its listed samples. Both referees' own samples give DIV = 0. L-COMP's independent N5^τ engine (l-comp 16c960b5; not a referee
  check) finds N5^τ ≠ SPEC on 497 of 26,573 runs and 0 violations of R48 (i), R50 (h) and R51 (a)'s f-form on 66,709 N5^τ phases (DATA).
  (iii) The exit mismatch of EPR-1 is common: 491 of 3,791 epoch exits (REFEREE) and 1,063 of 8,436 (REFEREE-2).
- Data (DATA, not proof): REFEREE (successor 12, own engine and own N5^τ): 52,631 epochs, 64,331 RESTRICT_E checks, 0 failures; REPRO
  reproduced; witness fb17_n32 from S3 (epoch (26), D_E = {11}: λ′ at 27 ≠ λ); div_n8 DIV = 1, 0 failures. REFEREE-2 (successor 14, own
  epr_check.py; lane code not run): 38,834 sample runs, 4 climbs and 72,000 tie-seeded runs, DIV = 0 there; witnesses
  docs/referee-2/R2-N5-EPR/instances/lamend_D0.pg (n 5, sha1 7f78faf7, D = ∅) and lamend_D1.pg (n 7, sha1 80063b9f), re-run by REFEREE;
  div_n8 reproduced (Addendum A); its step function equals the Runner at every step; the d1 mutation bites; longest epochs 92 / 56 on both
  engines.
- Signatures: REFEREE docs/referee/R-N5-EPR.md (referee 3def3e11, Addendum A e18b4370, §C a0858144, successor 12): RESTRICT_E, REPRO (state
  sequence, fallback types), EP-0, the consequence SIGNED; REPRO's one-phase clause SIGNED WITH GAP EPR-1; EP-k / EP-1 with the +1. REFEREE-2
  docs/referee-2/R2-N5-EPR.md (referee-2 796b4d36, Addendum A 9a5692ad, §C 61022fe3, successor 14): RESTRICT_E, REPRO's pairs and types,
  EP-0, EP-k's sum, the consequence SIGN; the one-phase clause "not signed as stated" (G-EPR-1); EP-1 signed as an implication with the +1.
  §C (both): verdicts identical in substance; one joint gap EPR-1 = G-EPR-1, same repair; EPR-N1 = REFEREE-2's EP-0 bullet; N-EPR-1 =
  REFEREE's standing-premise line; nothing open.
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (a reduction; EP-1 conditional; no running-time bound). GAPS G-N5-TIME: open.

### R62 [refereed-only] N5 on EVERY game: R55's factorisation holds under (NC) "no disagreement vertex on its own cycle" (G_D-NC), every vertex has the cycle nodes of its first disagreement vertex so terminal changes stay inside one honest class (TC-CLASS), the honest and W-valuations agree in coarse form above M_D under (h3_D) alone (C2-H3), W never drops at an in-phase S4a step (WM-G), and on every fallback-free in-phase run with (h3_D) throughout the coarse values freeze from state k_0 + n − 1 on (P^c_L, CR-D, FRZ-U_H3) (2026-10-26) — structural lemmas for N5 beyond one Odd choice vertex (no count; not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C71.md, checker 2a5da1ac)
- Object (packet P-N5-H3, added at l-si 10b11167, pinned trunk d096e404, unchanged during review): docs/si/P-N5-H3-box16.md, sha1
  680e45287aed82ea3d9ac05ed9decdf9c260e849 (L-SI successor 11, Opus 5.5). It supersedes P-N5-NC (sha1 2036e7c8, l-si eeb08be7), WITHDRAWN
  unreviewed by the Lead (REFEREE-2's report on it, 4d54b6a5, is VOID by its author, 9a482c93). The referees' notes are collected by the lane
  in docs/si/P-N5-H3-fixes-box16.md (l-si beb1e803, sha1 5666b4a5f71fabbf10cdd3b5bba796acdcdf6240, L-SI successor 12: H3-N4 = N-H3-6,
  H3-N2 = N-H3-4, N-H3-1, H3-N1, N-H3-2 / N-H3-3, data); on trunk; repairs only, no signed statement changes.
  Setting (every game): as in RESULTS R55 (state k = (σ_k, τ_k); σ̄_k; Ξ_k; G_τ; W_k; λ_Ξ, λ_W; D_k; u(v); R_D, F_D; π_v; (h_D); (h3_D);
  lev, COARSE_L, (C2), (C4) of RESULTS R25; M_D, ⊥ if D_k = ∅). (NC) at k: no vertex of D_k lies on its own honest cycle, and none lies on
  its own W-cycle; (h_D) implies (NC). A run S: consecutive states k_0, …, k_1 inside one phase, all of whose transitions are S4a steps (no
  fallback); Ω_k := W_k, the valuation of σ_k in the fixed one-player game G_τ; COARSE := COARSE_L for a level −1 ≤ L < ∞.
- Claims signed (both referees "(Opus 5.5, D15)", L37), on every game; no item uses (P); premises LANDED: RESULTS R55 (a), (b) (its proof,
  whose one use of (h_D) is replaced), R17 (a) (F1), R25 (C1)-(C4), R38 (a), SPEC S1, S4a; WM-G rests on the standing SPEC premise that S1
  returns the arena optimum, as 1E-N3 in RESULTS R57 (H3-N1, REFEREE; a landing note):
  (a) Lemma G_D-NC (b′): under (NC) at k, for v ∈ R_D with u := u(v), Ξ_k(v) = π_v ⊕ Ξ_k(u) and W_k(v) = π_v ⊕ W_k(u), and the honest and the
      W-play from u avoid π_v. R55 (b)'s proof uses (h_D) exactly once, and (NC) closes that step (N-H3-2 = REFEREE §1).
  (b) Lemma TC-CLASS (no hypothesis): at every state k and for every v ∈ R_D, λ_Ξ(v) = λ_Ξ(u(v)) and λ_W(v) = λ_W(u(v)); hence inside a phase,
      if v ∈ R_D at k and at k + 1 and u_k(v) ≠ u_{k+1}(v), then λ_Ξ(u_k(v)) = λ_Ξ(v) = λ_Ξ(u_{k+1}(v)).
  (c) Lemma C2-H3: if (h3_D) holds at k and M_D ≤ L < ∞, L ≥ −1 (L = −1 when M_D = ⊥), then COARSE_L(Ξ_k(v)) = COARSE_L(W_k(v)) for every v;
      no (h_D) and no (NC). The path set above the common cycle node factors through u(v) by the lasso fact (N-H3-3 = REFEREE §3).
  (d) Lemma WM-G: for every transition k → k+1 of a run S, Ω_{k+1} ⊵ Ω_k pointwise.
  (e) Lemma P^c_L and Lemma CR-D: if at every state of S (i) COARSE(Ξ_k(v)) = COARSE(W_k(v)) for every v and (ii) the map v ↦ λ_W(v) is the
      same, then COARSE(Ω_t) = COARSE(Ω_{k_0+n−1}) for every t ∈ S with t ≥ k_0 + n − 1 (Lemma P^c_L: for every j with k_0 + j ∈ S and every
      simple path r of G_τ from x to a W-cycle node u with at most j edges, Ω^c_{k_0+j}(x) ⪰ COARSE(value(r))). CR-D's statement is L-SI
      successor 10's (docs/si/N5-FRONTIER-box15.md §2, l-si 0bd6fb23); the proof is written out in the packet. In P^c_L's case B1 with x on
      c′'s W-cycle, the new cycle is simple because π meets the old arc only at c′ (π's part on the cycle and the arc c′ → x are disjoint,
      since x ∉ π): a sentence the packet omits (H3-N2 = N-H3-4, found independently by both referees).
  (f) Corollary FRZ-U_H3: on a run S inside one phase with (h3_D) at every state, for max_S M_D ≤ L < ∞, L ≥ −1, COARSE_L(W) = COARSE_L(Ξ)
      on V at every state of S, and it is constant on S FROM STATE k_0 + n − 1 ON. This is the 0-based reading, which the proof gives (P^c_L
      at k_0 + j covers paths with ≤ j edges, and simple paths have ≤ n − 1 edges); the packet's §0 phrase "(n − 1)-th state" is read so, a
      non-vacuous check needs a run of ≥ n + 1 states, and the stronger 1-based reading is NOT signed (H3-N4 = N-H3-6, both referees and the
      author). Scope: any number and any cycle configuration of the disagreement vertices (¬(h_D) by routing or by a gate on its own cycle).
- Not signed (packet §7, §8): ¬(h3_D) (M_D = ∞; on 𝒞^1O this is R50's ¬H3 case, which needs kinds); the fine route order below L inside
  one honest class with two or more disagreement vertices (Δ-RT; on 𝒞^1O R50's LEN), which by TC-CLASS is the only place where terminals
  can change; R55's Wo_D, not ported; the data. The packet's quotes of R55's proof and of (C1)-(C4) are content-verbatim, with joined
  bullets and some parentheticals dropped without "…" (N-H3-1, accepted by REFEREE).
- Honest limits: (i) Structural lemmas: they bound no count. (ii) The freeze is exercised only on runs of ≥ n + 1 states: lib41 3 runs,
  L-COMP's frz1_n24 and frz3_n24 (frz3_n24 also run by REFEREE-2, Addendum A 9a5692ad); pftheta34_n32 (L-RED) (all in the (h_D) regime or (NC) ∧ ¬(h_D)), and REFEREE-2's constructed witness
  pft34_h3u_P32 (¬(NC) at every state, (h3_D) holding; a disjoint union, so the cycling disagreement vertex is decoupled from the
  freezing part), re-run by REFEREE on its engine; natural freezes with ¬(NC) are not reached. Both referees' first freeze counts included
  vacuous n-state runs; both corrected them in addenda (REFEREE ead5fdb3, REFEREE-2 d449d72b).
  (iii) Content (DATA, L-SI successor 12, experiments/si/rund/rel.py, l-si d61b3cf0): on frz1_n24, frz3_n24,
  pftheta34_n32 and pft34_h3u_P32 the level max_S M_D is the top rank, and no W path set at any state of the run has a vertex above it;
  so on every long run known the frozen COARSE_L(W) is only the cycle node, and the freeze there is non-vacuous by length but
  content-free by level (it says nothing beyond hypothesis (ii)). Confirmed by REFEREE Addendum B (e18b4370; all its non-vacuous
  freezes, the 3 lib41 runs included) and REFEREE-2 Addendum A (9a5692ad). The signed statements are unaffected.
- Data (DATA, not proof): REFEREE (successor 12, own engine, random starts and given start pairs): 29,174 runs, 0 failures; C2-H3 1.22M
  checks, 5,773 states with (h3_D) ∧ ¬(NC); (b′) 153k checks; TC-CLASS 528 terminal changes (the sum of its logs, as its §C C.3 states), all inside one class; WM-G 679k checks;
  mutation (L = M_D − 1) fails 76,353 times. REFEREE-2 (successor 14, own h3_check.py reusing its NC checker; lane code not run): 0
  violations; C2-H3 201,701 checks at (h3_D) ∧ ¬(NC) states; TC-CLASS 1,664 in-phase terminal changes, none across classes; mutations c2l,
  b0, pc1, crd1 bite. L-COMP (independent checker; not a referee check): C2-H3 151,611 checks, 10,487 at ¬(NC) states, on the library frontier (l-comp
  56d42105), and 1,131,485 checks, 115,640 at ¬(NC) states, on 50,000 random runs (l-comp 785c38d3), 0 violations.
- Signatures: REFEREE docs/referee/R-N5-H3.md (referee 7c2d9b49, successor 12; Addendum A ead5fdb3; §C 6b17eb58; Addendum B e18b4370): all SIGNED; notes
  H3-N1..N4; no gap. REFEREE-2 docs/referee-2/R2-N5-H3.md (referee-2 5b251bed, N-H3-6 d449d72b, §C b7b04fad + 723909be, Addendum A 9a5692ad, successor 14): all
  SIGN; notes N-H3-1..6; no gap. §C (both): verdicts identical, FRZ-U_H3 signed in the 0-based reading; joint gap map empty; H3-N2 = N-H3-4;
  N-H3-1 accepted by REFEREE (partly missed by it); H3-N1, H3-N4 REFEREE's; nothing open.
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (structural; no running time). GAPS G-N5-TIME: open.

### R65 [refereed-only] N5 and its keep-τ-on-ties variant N5^τ compute the same state functions, every τ-keeping transition of either is the Σ-transition from a τ-stable state (N5's are those among N5^τ's at which SPEC's S4b returns τ), so a per-phase proof for N5 transfers to N5^τ unless it uses more than the Σ-transition, τ fixed, τ-stability, the shared state functions, the phase-end facts and R15 (c), (d) (Lemma Στ-STEP, transfer clause); both referees audited the per-phase chain behind RESULTS R48 (i) and R50 (h) (CHECKED, not signed) and found the packet's file list complete with completions and no implicit use of S4b's output, so, at the strength of that audit, premise (Στ) of RESULTS R64 (e) holds and EP-1 holds without it: an epoch with one disagreement vertex has len(E) ≤ T*(G′_E) + 1 = O(m·Δ·n¹¹) (2026-10-26) — a transfer lemma plus an audit for N5 (not M3, not a step-4 pass, not a TARGET.md claim; the number of epochs and epochs with |D_E| ≥ 2 are not bounded; G-N5-TIME stays open), CHECKER PASS (docs/checker/C74.md, checker 24916090)
- Object (packet P-N5-STAU, added at l-new 010bfdae, pinned trunk ca0a4e97, unchanged during review): docs/new/P-N5-STAU-box45.md, sha1
  7446d9a9e198ffa5073e0d43823d753b6aa46b3b (L-NEW successor 24, Opus 5.5). The referees' notes are collected by the lane in
  docs/new/P-N5-STAU-fixes-box45.md (l-new ee95661f, sha1 42d7b04c7e00bee1a95241b52edf2e7a67004f33, L-NEW successor 25: STAU-1 with
  REFEREE's two repair lines verbatim, N-STAU-2..4, STAU-N1..N3, audit-list completions, box24); on trunk; repairs only, no signed statement
  changes.
  Setting (every game): as in RESULTS R64 (N5 = SPEC S1-S5 with FIX 1-4, Q1-Q4; N5^τ := N5 with S4b replaced by S4b^τ: if Iτ ≠ ∅ and τ is
  value-optimal against σ in S4b's arena H′, keep τ, otherwise SPEC's S4b). σ_a := S4a's output; Σ(σ, τ) := σ_a if σ_a ≠ σ, else S4c's Even
  switch-all on Iσ. A state is τ-STABLE if Iσ ≠ ∅ and (Iτ = ∅ or τ is value-optimal against σ in H′); a Σ-TRANSITION is (σ, τ) → (Σ(σ, τ), τ).
- Claims signed (both referees "(Opus 5.5, D15)", L37), on every game; no item uses (P); premises LANDED: SPEC; RESULTS R18 (d) Lemma S (a)
  (= (VJ), RESULTS R57 (a)); R15 (a), (c), (d); the standing SPEC premise that S1's procedure returns an optimal counterstrategy (1E-N3,
  RESULTS R57), which the packet's (b) uses in citing "S4b's output τ is value-optimal" (N-STAU-2, REFEREE-2; accepted by REFEREE); R15 (a)
  also transfers and belongs in (d) (STAU-N1 = N-STAU-3, both referees):
  (a) Lemma Στ-STEP (a): at every state N5 and N5^τ compute the same Ξ, W, Iσ, Iτ, the same S4a output σ_a and the same S4c switch-alls.
  (b) Lemma Στ-STEP (b): if N5's transition from (σ, τ) keeps τ, N5^τ's transition from (σ, τ) is the same transition.
  (c) Lemma Στ-STEP (c): if N5^τ's (or N5's) transition from (σ, τ) keeps τ, then (σ, τ) is τ-stable and the transition is the Σ-transition;
      conversely N5^τ's transition from a τ-stable state is the Σ-transition.
  (d) Lemma Στ-STEP (d): every N5^τ iteration applies a non-empty improving switch to σ or to τ, so the proofs of RESULTS R15 (c), (d) apply
      to N5^τ runs.
  (e) Corollary, transfer clause: a per-phase proof for N5 transfers to N5^τ unless it uses, at an in-phase transition, more than the
      Σ-transition, τ fixed, τ-stability, the shared state functions ((a)), the phase-end facts "Iσ = ∅ ⇒ τ changes or the run stops" ((c))
      and R15 (c), (d) ((d)). SIGNED by both.
      The Corollary's sentences 1-2 are SIGNED WITH GAP STAU-1 (minor, wording):
      sentence 2 by both, sentence 1 by REFEREE-2 (REFEREE: a note, §C.2); both read with REFEREE's repair, checked by REFEREE-2:
      "The τ-keeping transitions of N5^τ are exactly the Σ-transitions from τ-stable states; N5's are those among them at which SPEC's S4b
      returns τ; the in-phase ones are the τ-keeping ones with λ unchanged." and "N5 and N5^τ make different transitions only (i) at a
      τ-stable state where SPEC's S4b returns a value-equal τ′ ≠ τ (N5 leaves the phase, N5^τ need not), and (ii) at a state with Iσ = ∅
      where SPEC's S4b returns a value-equal τ′ ≠ τ (both leave the phase, N5^τ by Odd's fallback)." As written, sentence 1's "exactly" is
      only an inclusion (a τ-keeping Σ-transition can change λ_Ξ; witness REFEREE-2's nonex_min.pg, n 4), and sentence 2 misses case (ii)
      (witness REFEREE's is0_c1o264.pg, n 12, sha1 b0006099716e5c57932c0ce7f334ae3750ff9188). The referees differ only on whether sentence 1
      alone was a gap (REFEREE-2) or a note (REFEREE); both close with the repair. No downstream effect: (Στ) and EP-1 use τ-keeping in-phase
      transitions only, and case (ii) ends the phase in both runs.
- Audited (both referees CHECKED the packet's §2 table; an audit, not a signed theorem):
  (f) Audit (1), "is §2.1 the whole per-phase chain behind R48 (i) and R50 (h)?": YES (both). Each referee computed the RESULTS citation
      closure with its own script: R15, R17, R18, R19-R34, R38, R39, R42, R44, R45, R48, R50 (R47 only in R50's not-signed reading), equal to
      the packet's list. Completions, none on a proof path that uses S4b: four entry-named files outside the packet's 66 (the SPEC,
      docs/lit/T21-VJ00-check, N5-brchanges-box11, docs/red/R58-n5-width §9 = R18 (a); STAU-N2 = REFEREE-2 §2.1 (i)); referee-written proof
      steps on the chain (X-1 / TF for R21 (i), CAP-1 for R25, TB-1 and N-U1-3 for R24; REFEREE-2, missed by REFEREE's scan of docs/referee*,
      then checked by it by search (§C l. 150)); table rows "R17 Lemma P / Theorem PH on τ-fixed segments as runs on G_τ" and "Lemma S (b)", both "yes" (REFEREE-2).
      Detail: REFEREE called N5-1Oacyc-box24 "not on the chain"; REFEREE-2 shows it is (cited as a proof step by P-N5-X, P-N5-XA, P-N5-NH),
      and the packet lists it; no effect on either answer.
  (g) Audit (2), "does any proof in that chain use S4b's OUTPUT implicitly?": NO (both). Own searches wider than the packet's (REFEREE
      108 + 172 hits, including SPEC's ASCII H' (14 hits, none S4b's arena); REFEREE-2 323 hits plus two further passes), all hits read in context; every tie-break used
      is S4a's (Lemma TB) or σ̄'s.
  (h) Consequence (by RESULTS R64 (e) with (e), (f), (g); AUDIT strength, not signed: REFEREE states it
      on REFEREE-2's confirmation, l. 28 and §C.3; REFEREE-2 states (Στ) as a READING, §4, and leaves EP-1 to the Lead and CHECKER; CHECKER C74
      checked the deduction): premise (Στ) of RESULTS R64 (e) holds, so RESULTS R64 (e) EP-1 holds without
      premise: every epoch E with D_E = {u} has len(E) ≤ T*(G′_E) + 1 = O(m·Δ·n¹¹), and, by R64 (f), X_SN^pre(E) ≤ len(E) there.
- Not signed (packet §3, §4): the data; the conclusion line (READING), replaced by (h). The Corollary's sentences as written (STAU-1).
- Honest limits: (i) (h) rests on an audit: both referees read the closure's proofs by search plus targeted reading, not every line of
  the 66 files (10,307 lines, REFEREE's scope note); a missed implicit use of S4b's output would void (h) for the entry containing it. REFEREE-2 answers (1) YES "as far as I can
  determine" (l. 73); neither referee audited the ~40 lane working texts that packets name as sources, on the ground that each packet is
  self-contained and governs (REFEREE-2 l. 74-77); REFEREE checked the referee-written steps (ii-a)-(ii-d) by search only (§C l. 150).
  (ii) It bounds |D_E| = 1 epochs only. The number of epochs per phase (N_ep), and epochs with |D_E| ≥ 2, are not bounded here; with R63 and
  R64 these are the open parts of the per-phase count. (iii) (h) is per epoch; no per-phase, per-run or running-time bound on any class
  follows from this entry alone.
- Data (DATA, not proof): REFEREE (successor 13, own stau_probe.py; lane code not run): 0 failures of (b), (c), (c) for N5, (c) converse,
  (d), DIFF_OTHER, "in-phase = Σ", and R48 (i) on N5^τ phases, on 20,000 random games, 5,000 random 𝒞^1O and lib41 (45 files with n > 64
  skipped); lib41 max f 33; DIFF_IS0 44 (all at Iσ = ∅), DIFF_TS 4,761. REFEREE-2 (successor 15, own stau_check.py; lane code not run):
  122,512 states over its 503 𝒞^1O files, lib41 (410 files, 45 with n > 64 skipped), 3,000 random 𝒞^1O, 2,000 random general games and div_n8, 0 violations of (a)-(d), the converse and
  the corollary inclusion; LINK 45,490 checks, 0; R48 (i) on N5^τ phases max f 37, phase length 112; mutants keep / sig caught (1,574 / 48);
  L-COMP's 6 pinned instances (l-comp 16c960b5): 0 violations, keep counts equal to its own at step level (report l. 131-133; logs/lcomp_pinned.txt holds the transition-level counts); is0_c1o264 reproduced (is0_count.py:
  86 random 𝒞^1O + 76 random general states of that case, of which 3 + 1 lead to different successors).
- Signatures: REFEREE docs/referee/R-N5-STAU.md (referee 48674360, §C 3a999280, successor 13): Στ-STEP (a)-(d) SIGNED; transfer clause
  SIGNED; sentences 1-2 SIGNED WITH GAP STAU-1 (§C.2: narrowed to sentence 2; sentence 1 a note, = N-STAU-1); §2 CHECKED, (1) YES, (2) NO; notes STAU-N1..N3. REFEREE-2 docs/referee-2/R2-N5-STAU.md
  (referee-2 8e42c473, §C fbbe66a4, successor 15): (a)-(d) SIGN; Corollary SIGN, in its §C SIGN WITH GAP STAU-1 (it missed sentence 2,
  reproduced is0_c1o264); §2 CHECKED, (1) YES, (2) NO; notes N-STAU-1..4. §C (both): no verdict disagreement; joint gap STAU-1 (wording),
  closed by REFEREE's repair text in the fixes file (REFEREE C.3: open until that line exists; written at l-new ee95661f); STAU-N1 = N-STAU-3; STAU-N2 = REFEREE-2 §2.1 (i); N-STAU-2, N-STAU-4 and the
  referee-written steps accepted by REFEREE; box24 detail as in (f); STAU-N3 accepted by REFEREE-2 (C.4); nothing open of substance (REFEREE-2 C.6).
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (a transfer lemma, an audit, and a per-epoch consequence; no running-time
  bound). GAPS G-N5-TIME: open.

### R66 [refereed-only] N5 on EVERY game: in every phase, the epochs in which Odd's best reply agrees with τ (D = ∅) number at most (f + 1)(n + 1) + 4n(n − 1) + 1, with f the phase's in-phase fallbacks (Lemma REC-0), so the in-phase transitions whose source lies in such an epoch number at most that times n + m (Corollary, via RESULTS R64 (c) EP-0) (2026-10-26) — a REDUCTION of the D = ∅ part of the epoch count to f (not free of f; not M3, not a step-4 pass, not a TARGET.md claim; epochs with D ≠ ∅ are not bounded here; G-N5-TIME stays open), CHECKER PASS (docs/checker/C75.md, checker ae40434a)
- Object (packet P-N5-REC0, added at l-new 18dd8c90, pinned trunk 64506ecf, unchanged during review): docs/new/P-N5-REC0-box45.md, sha1
  343239b54a35d2701d076805674ef77aa7a21f7d (L-NEW successor 24, Opus 5.5). The referees' notes are collected by the lane in
  docs/new/P-N5-REC0-fixes-box45.md (l-new ec0105e2, sha1 f35b26f369d4ea92e794d24791142f8f864f68a7, L-NEW successor 25: REC0-N1..N3,
  N-REC0-1, N-REC0-2, the full Q-R17 input list); on trunk; repairs only, no signed statement changes.
  Setting (every game): N5 = SPEC S1-S5 (FIX 1-4, Q1-Q4); state k = (σ_k, τ_k); σ̄_k; Ξ_k; W_k := V_{σ_k,τ_k} (σ_k's valuation in G_τ); λ, λ_W;
  phases as in RESULTS R38 (a); f := the in-phase S4c fallbacks of a phase; Q := the Odd vertices of out-degree ≥ 2; an EPOCH is a maximal run of
  a phase with σ̄|Q constant, D_E := {q ∈ Q : σ̄_E(q) ≠ τ(q)}. A state is D = ∅ if σ̄_k|Q = τ|Q (then σ̄_k = τ and Ξ_k = W_k), ALL-UNSPLIT if
  λ_W = λ there. LEVEL j at k: W_k(x) ⪰ value(r) for every x and every simple path r of G_τ with ≤ j edges from x to a cycle node of λ (value
  as in RESULTS R17 Lemma P).
- Claims signed (both referees "(Opus 5.5, D15)", L37), on every game; no item uses (P); premises LANDED: SPEC S4a; RESULTS R17 (b) Lemma P
  (its induction step only), R17 (F1)/(F2), (d); R18 (d) Lemma S (c); R23 (g) Lemma WM (game-general, RESULTS R63 XEP-N2); R21 (a) Lemma XW
  (= (VJ), RESULTS R57); R15 (a), (d), with R15 (d)'s Ωσ read as S1's Ξ (standing code link G-N5T-1; N-REC0-2, REFEREE-2); RESULTS R63 (b)
  SN-PREFIX_D (a) (the packet cites P-N5-XEP; REC0-N1, REFEREE); and, for the corollary only, RESULTS R64 (c) EP-0:
  (a) Lemma REC-0: in every phase P of N5, N_0 := the number of epochs of P with D_E = ∅ satisfies N_0 ≤ (f + 1)(n + 1) + 4n(n − 1) + 1. Proof
      steps (both referees re-derived each): level step at a D = ∅ state (step 1, an in-phase S4a step, N-REC0-1), persistence and base,
      fallback-free runs and their all-unsplit prefixes, saturation (W = B, then Ξ constant and R15 (d)), the epochs before saturation by
      kind of last transition, sum. In step 3 "rises by one" reads "level ≥ min(j + 1, n − 1)" (REC0-N2, REFEREE).
  (b) Corollary: the in-phase transitions of P whose source lies in a D = ∅ epoch number at most ((f + 1)(n + 1) + 4n(n − 1) + 1)·(n + m); R64's
      len(E) is the count used, and EP-0 is unaffected by R64's repair EPR-1 (REFEREE).
  (c) Q-R17 (the packet's question to the referees), answered YES by both, with the same input list: the induction step k → k + 1 of R17 (b)
      Lemma P uses only the hypothesis at k; that I_k is read from the same valuation Ω_k (here D = ∅ at k gives Ξ_k = W_k, so S4a's arena is
      G_τ's switch-best arena (every improving edge available, ρ_k in it)); that the step's result is a pointwise optimum of that arena ((F1) via R18 (d) S (c), and (F2)); (V1), (V2);
      that u is a cycle node at k and no vertex changes its W-cycle node from k to k + 1; and the one-player structure of G_τ. Nothing about
      earlier steps or the phase start is used; the start enters only the base case, which REC-0 replaces by its step 2. The packet's list
      omits (V1), (V2), the cycle node and the one-player structure (REC0-N3 = N-REC0-2, first half). Consistent with R17's honest limit
      (ii), whose counterexamples have Ξ ≠ W (REFEREE; agreed by REFEREE-2).
- Not signed (packet §2, §3): what REC-0 does not give and its consequences with RESULTS R56 and R61 (READING: N_0 = O(n²(1 + ρ)), and
  N_0 = O(n^{k+2}) on 𝒞^kO, conditional as RESULTS R61 is); the data and the climbs.
- Honest limits: (i) A REDUCTION: N_0 is bounded in terms of f, and f is not bounded here (R56 bounds it by ρ; R61 by O(n^{k+1}) on 𝒞^kO with k
  fixed, conditional). (ii) Only epochs with D_E = ∅; epochs with D_E ≠ ∅ (for |D_E| = 1 see RESULTS R64 (e) and R65; |D_E| ≥ 2 OPEN) and the
  number of epochs per phase in general (N_ep) are not bounded here. (iii) Thin data: step 5's n − 1 cap on kind-(iii) steps is not exercised
  (at most 1 per run in both referees' samples, at most 4 in the packet's lib41 row); only 291 non-saturating level steps in REFEREE-2's
  runs; max N_0 = 5 over all samples (lib41 and REFEREE-2's 503 files; 1-2 on every random sample), far below the bound; REFEREE-2's mutant
  without the 4n(n − 1) term does not fail on its logged run.
- Data (DATA, not proof): REFEREE (successor 13, own rec0_probe.py with exact levels by simple-path enumeration; lane code not run): 0
  failures; REC0 182,522, EP0 113,532, STEP1 9,929, STEP2 10,929, base and saturation 147,070 checks; 20,000 random games (n 4-9, up to 3 Odd
  choice vertices) and lib41 (45 files with n > 64 skipped; level checks for n ≤ 14); lib41 max N_0 = 5. REFEREE-2 (successor 15, own
  rec0_check.py; N5 runs from successor 13's Runner; levels exact for n ≤ 11; lane code not run): 42,604 runs, 96,490 phases (random general
  and random 𝒞^1O, its 503 files, lib41 without its docs/referee games), 0 violations of BOUND, EP0, the prefix property, BASE/UB, STEP2,
  STEP1, SAT and the step-5 kind counts; max N_0 = 5; the saturation-at-once mutant is caught, the +2 mutant does not bite on the logged seed-53 run (its 3 bites are from an unlogged smoke run).
- Signatures: REFEREE docs/referee/R-N5-REC0.md (referee 6006b963, §C 981307c9, successor 13): REC-0 SIGNED as a reduction in f, corollary
  SIGNED, no gap; Q-R17 YES; notes REC0-N1..N3. REFEREE-2 docs/referee-2/R2-N5-REC0.md (referee-2 a0457eb0, independence-line correction
  82fdc8d4, §C 1ff6c484, successor 15): REC-0 and corollary SIGN, no gap; Q-R17 YES; notes N-REC0-1, N-REC0-2. §C (both): verdicts identical;
  REC0-N3 = N-REC0-2 (first half); REC0-N1, REC0-N2 accepted by REFEREE-2; N-REC0-1 and N-REC0-2 (second half) accepted by REFEREE; joint gap
  map empty; nothing open.
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (a per-phase reduction in f; no running-time bound). GAPS G-N5-TIME: open.

### R67 [refereed-only] N5 on EVERY game, inside one fallback-free run S of one phase: CR-D's hypothesis (i) can be replaced by a per-edge order transfer (CR-REL); under (h3_D) on S the W/Ξ offset of a vertex is 0 or its gate's offset, a sum of ±2^r over the run's band, so its changes are at most (n − 1) + 2^{B+1} (OFFSET, MERGE-B, TWIN-GAP), and a block of aligned states is a switch-best block of G_τ, so S has at most N_split + (N_split + 1)(n + m − 1) transitions (PIECE_D, SPLIT-RED); and if only λ_W is constant on S (hypothesis (ii)), Lemma P's coarse lower bound holds whenever each Even edge of the path is unforbidden at its one scheduled state (P^c_sch, FRZ-SCH), so every coarse W-change after the first n − 1 states is charged to a forbidden edge (CHARGE), which points into the disagreement region (FZ) and is charged only if later switched into (UNF), giving at most (n − 1)(1 + |U(S)|) coarse W-changes per vertex per run (CHARGE-U) (2026-10-26) — structural lemmas and reductions for N5 beyond one Odd choice vertex (no count: the band B, N_split and the unforbid-switches U(S) are not bounded here; not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C76.md, checker 9ebda4df)
- Object (packet P-N5-RUND, added at l-si 762b7243, pinned trunk 94910ed3, unchanged during review): docs/si/P-N5-RUND-box17.md, sha1
  71e198f359cbb321fc0c15e6c28676d4dd046d52 (L-SI successors 12 (§2-§4) and 13 (§5, §6, assembly), Opus 5.5). The referees' notes are
  collected by the lane in docs/si/P-N5-RUND-fixes-box17.md (l-si 74e0375d, sha1 aa4a39201313ba9b34364fb82f76a95589edb828, L-SI successor
  14: the union of RUND-N1..N4 and N-RUND-1..7, a §7 status line; 36 quotes checked by script); on trunk; repairs only, no signed statement
  changes.
  Setting (every game): as in RESULTS R62 (state k; σ̄_k; Ξ_k; G_τ; W_k; λ_Ξ, λ_W; D_k; u(v); R_D, F_D; π_v; (h_D); (h3_D); lev, COARSE_L,
  (C1)-(C4) of RESULTS R25; M_D). A run S: consecutive states k_0, …, k_1 inside one phase, all of whose transitions are S4a steps (no
  fallback); Ω_k := W_k; COARSE := COARSE_L, −1 ≤ L < ∞; (ii) := λ_W constant on S. An Even edge (x, z), a := σ_k(x), is FORBIDDEN at k (level
  L) if COARSE_L(W_k(z)) ≻_L COARSE_L(W_k(a)) but not Ξ_k(z) ▷ Ξ_k(a); SPLIT at k if [Ξ_k(z) ▷ Ξ_k(a)] ≠ [W_k(z) ▷ W_k(a)]; a state is ALIGNED if
  it has no split edge, N_split(S) := the transitions of S with a non-aligned source. Offsets: s^Ξ_k(v), s^W_k(v) := the signed weights
  w(P(·)) of the path sets (R25 (C3)), Δ_k(v) := s^W_k(v) − s^Ξ_k(v), δ_k(u) for u ∈ D_k; L* := max(max_S M_D, −1); U_S, ℓ_S as in the packet
  §3; B := L* − ℓ_S + 1. The SCHEDULE of a simple path r = (r_0, …, r_m) of G_τ to a W-cycle node at state k is CLEAN if k − m ≥ k_0 and no
  Even edge (r_q, r_{q+1}) is forbidden at state k − 1 − q. U(S) := the S4a switch events (k′, (y, z)) of S into an edge forbidden at some
  state of [k′ − n + 1, k′ − 1] ∩ S (UNFORBID-SWITCHES).
- Claims signed (both referees "(Opus 5.5, D15)", L37), on every game; no item uses (P); premises LANDED: RESULTS R62 (a)-(f) (setting,
  TC-CLASS, C2-H3, WM-G, P^c_L / CR-D, FRZ-U_H3), R55 (a), R25 (C1)-(C4) and (Cstrict), R17 (a) (F1), (c) Theorem PH, (d), R18 (d) Lemma S
  (c), R15 (a), (d) with (VJ) (RESULTS R57), R21 (a) XW; and the standing SPEC premise 1E-N3 (RESULTS R57) in two forms (N-RUND-1,
  REFEREE-2; accepted by REFEREE): P1, S1's σ̄_k is Odd's pointwise optimum in G_{σ_k} (used by FZ, and by OFFSET (a) and so TWIN-GAP); P2, S4a's σ_{k+1}
  is Even's pointwise optimum in its arena H_k (used by §2-§5 and by CHARGE-U, through WM-G and (F1) on H_k; REFEREE-2 §0: OFFSET (b), (c),
  MERGE-B and UNF need neither). The packet's "R19 (d) (SG)" quote is not
  verbatim; the fact OFFSET (a) uses is R15 (a) carried to SPEC's Ξ by (VJ) under P1 (RUND-N1 = N-RUND-2, both referees):
  (a) Lemma CR-REL: CR-D (RESULTS R62 (e)) holds with its hypothesis (i) replaced by EDGE ORDER TRANSFER at L at every state of S (no Even
      edge forbidden at L): under it and (ii), COARSE_L(W) is constant on S from state k_0 + n − 1 on.
  (b) Lemma OFFSET, under (h3_D) on S: (a) λ_Ξ = λ_W, constant on S, and s^Ξ, s^W are non-decreasing along S; (b) Δ_k(v) = 0 if v ∈ F_D or
      λ(v) ∈ π_v, otherwise Δ_k(v) = δ_k(u(v)); (c) every δ_k(u) is a sum of terms ±2^r with ranks r ∈ [ℓ_S, L*], so every offset on S is a
      multiple of 2^{ℓ_S}. Lemma MERGE-B: if λ(y) = λ(z) and Δ(y) = Δ(z), the two frames order the path sets of y and z the same way.
  (c) Theorem TWIN-GAP, under (h3_D) on S, with N_v := the transitions of S at which Δ(v) changes: (i) at such a transition with d :=
      Δ_{k+1}(v) − Δ_k(v), s^W(v) rises by ≥ d if d > 0 and s^Ξ(v) by ≥ −d if d < 0; (ii) at most (2^{L*+2} − 2)/2^{ℓ_S} < 2^{B+1} of them have
      source state ≥ k_0 + n − 1 (N-RUND-4); (iii) N_v ≤ (n − 1) + 2^{B+1}. Corollary: the terminal changes of v at which its offset changes
      are ≤ N_v. In (ii)'s proof each score's rise bound 2^{L*+1} − 1 is the width of the low-part range (RUND-N4, REFEREE).
  (d) Lemma PIECE_D: (a) at an aligned state, Iσ_k is G_τ's improving set and the S4a step is a switch-best step of G_τ (R17's rule, for
      SPEC's pointwise-optimal choice); (b) a block of consecutive transitions of S with aligned sources and λ_W constant has fewer than
      n + m transitions (m = m_τ ≤ m, N-RUND-3; R17 (c) applied to switch-best started mid-run, RUND-N3). Corollary SPLIT-RED, under (h3_D)
      on S: |S| ≤ N_split(S) + (N_split(S) + 1)(n + m − 1), |S| counting transitions (N-RUND-3).
  (e) Lemma P^c_sch, under (ii) only (not (i), not (h3_D)): if the schedule of r at k is clean, Ω^c_k(r_0) ⪰ COARSE(value(r)). Corollary
      FRZ-SCH: if the schedule at s of x's W-play prefix at t is clean, COARSE(W(x)) is constant on [s, t]; it contains CR-D and CR-REL.
      Corollary CHARGE (hypothesis (ii) only): every change of COARSE(W(x)) at s − 1 → s is a WINDOW change (s − 1 − m < k_0, so s ≤ k_0 + n − 1, at most n − 1 per
      x per run) or is CHARGED to an Even edge (r_q, r_{q+1}) of x's W-play prefix at s that is forbidden at state s − 2 − q.
  (f) Fact FZ (premise P1 only, with totality of ⊴, (Cstrict) and the definition of D_k; RUND-N2, REFEREE; no run, phase, S4a or (ii)
      hypothesis): a forbidden (x, z) has Ξ_k(z) ◁ W_k(z), so z's W-play meets D_k. Lemma UNF: a charged change is preceded by an S4a switch
      INTO the charged edge at some k′ with f < k′ ≤ s − 1 ≤ f + n − 1, at which the edge is not forbidden. Corollary CHARGE-U (hypothesis (ii)
      only): for every x the changes of COARSE_L(W(x)) on S number ≤ (n − 1)(1 + |U(S)|); U(S) depends on L, and U_L ⊆ U_{−1} (N-RUND-5).
- Not signed (packet §7-§9): the CONJECTURES FS and LC2 (OPEN) and the OPEN items (R1)-(R4); the
  dead CONJECTURES UF-ONCE (packet §7; REFEREE-2's side finding: so_th_n32, sha1 ae9126ad, reproduced by REFEREE; phase2_pk48, sha1 83dead9b;
  both reproduced by the lane) and PAIR-OC (packet §7; L-RED R81, pairoc_n58, sha1 4824c73c), and, outside the packet, U-SPLIT (lane note
  §17; L-RED R80, usplit_rd_s3_n27, sha1 1e9ca56d), all three recorded as DEAD in the fixes file's §7 status line, none of them a signed
  item; the §3 READING (polynomial only for a narrow band); the data.
- Honest limits: (i) Structural lemmas and reductions; no count. TWIN-GAP is exponential in the band B (B reaches 39 at n ≤ 48 in the
  lane's data (44 on lib41 in REFEREE's data, 155 at n = 192 in REFEREE-2's)); SPLIT-RED leaves N_split unbounded; CHARGE-U leaves |U(S)| unbounded, and |U(S)| = Θ(n) for one vertex in one run is
  realized (L-RED R82, mkgrow, DATA), so CHARGE-U's route gives at best order n² coarse W-changes per vertex per run. (ii) The lane's
  reduction of stretch boundaries to ρ, epochs and gate W-changes (docs/si/N5-RUND-box17.md §20) and the relay-cycle obstruction (§22) are
  lane work after the packet, not part of this entry. (iii) Thin data (N-RUND-6 and REFEREE's thin-data bullets): CR-REL's own hypothesis
  held only 3-5 times in REFEREE's samples and 12 CR-REL freezes are non-vacuous in REFEREE-2's; the TWIN-GAP (ii) and PIECE_D (b) bounds
  are slack in all data (max tail rise 38 % of its cap; longest aligned block 55 against n + m_τ = 300) and the mutations tg4, tgr and piece
  do not bite; the exhaustive P^c_sch check ran only on small games, where nothing is charged; REFEREE's probe skips runs where λ_W changes,
  so CHARGE-U on so_th_n32's sub-run is REFEREE-2's check only, and there it holds through the window term alone (the run has 21 < n − 1
  transitions); the U-term is exercised elsewhere (REFEREE-2: 15,314 charged changes).
- Data (DATA, not proof): REFEREE (successor 13, own rund_probe.py, every L in {−1, …, n − 1}, suffix runs on the long instances; lane code
  not run): 0 failures; long runs (frz1-3_n24 with their starts, pftheta34_n32): 9.9M FRZ-SCH pairs, 47,413 charged changes, 57,867 UNF
  checks, max |U| 7; lib41: 67M FRZ-SCH pairs, 65,201 charged changes, 70,546 UNF checks; 6,000 random games with exhaustive P^c_sch for
  n ≤ 7; controls MUT=1 and MUT=2 fail (78,800 / 405,240). REFEREE-2 (successor 16, own rund_check.py with Ξ and W as play values; lane
  code not run): 20,254 N5 runs (90,290 states), 0 violations, including about 5.4M P^c_sch clean checks (random paths seeded by a salted hash; not exactly reproducible), 15.4M FRZ-SCH checks, 17,088 UNF and
  566,623 FZ checks; brute force on small arenas: P1 at 31,001 states, P2 at 24,910 transitions; mutations shift, noforb, fz, unf, chu0 and
  crrel1 bite; CHARGE-U on so_th_n32 states 1-22: 29,696 checks, 0 violations.
- Signatures: REFEREE docs/referee/R-N5-RUND.md (referee 29846bca, §C 62a1a01d, successor 13): §2-§6 SIGNED, no gap; notes RUND-N1..N4.
  REFEREE-2 docs/referee-2/R2-N5-RUND.md (referee-2 7a02a1f2, §C 2c8c17c6, addendum ac7e80e9 (merged at e8d31c47) correcting its §C header to REFEREE's §C
  62a1a01d and adding the so_th_n32 CHARGE-U check, successor 16): all 14 items SIGN, no gap; notes N-RUND-1..7. §C (both): verdicts
  identical, all 14 items signed by both; joint gap map empty; RUND-N1 = N-RUND-2; RUND-N2, N3, N4 accepted by REFEREE-2; N-RUND-1, 3, 4, 5
  accepted by REFEREE; N-RUND-6, 7 agree with REFEREE's thin-data bullets and §4 checks; nothing open on the signed items (REFEREE §C: outside them, §7's route to |U(S)| ≤ n_E via UF-ONCE is closed and needs another argument).
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (structural lemmas and reductions; no running-time bound). GAPS G-N5-TIME: open.

### R68 [refereed-only] N5 on EVERY game: in every phase the W-honest states (Ξ = W) number at most f + 4n² − 3n (Lemma HON), a fallback at a W-honest state is flat and ends the phase at a saturated W-honest state (SAT0, HON-FB), so f may be replaced by the in-gap fallbacks f_in (HON′), and the D = ∅ states, the D = ∅ epochs and their transitions number at most f_in + 4n² − 3n (HON-0, which implies RESULTS R66's bound); a run with D ⊆ {u} is an N5^τ run on the one-Odd-choice game G^u (RESTRICT_u, REPRO_u), and the {u}-intervals of a phase number at most 1 + f_in + 4n² − 3n + X_dir + X_big (REC-1 (a)); as IMPLICATIONS from premise (Στ), u-runs have length ≤ T*(G^u) + 1 (EP-1u) and the |D| = 1 states of a phase are bounded by REC-1 (b)-(d) (2026-10-26) — partial step-4 lemmas for N5 beyond one Odd choice vertex (reductions to f_in, X_dir and X_big; not free of f; not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C77.md, checker f8698135)
- Object (packet P-N5-HON, added at l-new 67a7b54d, pinned trunk 31835c4b, unchanged during review): docs/new/P-N5-HON-box46.md, sha1
  07f8e767cfca12d29c8f6f2e3f03358326abbef1 (L-NEW successor 25, Opus 5.5). The referees' notes are collected by the lane in
  docs/new/P-N5-HON-fixes-box46.md (l-new 0238b1cb, sha1 54985acfbfb0feb0e8bb3b04d882df78eaf72f1b, L-NEW successor 26: N-HON-1..5,
  HON-N1..N4, 46 quotes checked by script); on trunk; repairs only, no signed statement changes.
  Setting (every game): N5 = SPEC S1-S5 (FIX 1-4, Q1-Q4); state k = (σ_k, τ_k); σ̄_k; Ξ_k; W_k := V_{σ_k,τ_k} in G_τ; λ, λ_W; phases as in
  RESULTS R38 (a); f := the in-phase S4c fallbacks of a phase; Q, D_k, epochs as in RESULTS R64. A state is W-HONEST if Ξ_k = W_k pointwise
  (every D = ∅ state is); LEV(k) := the largest j ≤ n − 1 with Ξ_k(x) ⪰ value(r) for every x and every simple path r of G_τ with ≤ j edges to a
  cycle node of λ (value as in RESULTS R17 Lemma P); SATURATED if LEV = n − 1. f_in := the in-phase fallbacks of a phase at non-W-honest
  states strictly between two W-honest states (f_in ≤ f). G^u: G with every Odd v ∈ Q ∖ {u} cut to τ(v) (u keeps its edges); a u-run is a
  maximal run of a phase with D_k ⊆ {u}; a {u}-interval is a maximal run with D_k = {u}. X_dir := the in-phase transitions with
  |D_k| = |D_{k+1}| = 1 and D_k ≠ D_{k+1}; X_big := those with |D_k| ≥ 2 and |D_{k+1}| = 1. T*(G^u) := RESULTS R51 (a)'s per-phase bound at
  G^u's parameters, T*_Q := max_u T*(G^u).
- Claims signed (both referees "(Opus 5.5, D15)", L37), on every game; no item uses (P); premises LANDED: SPEC (S2, S4a, S4c with FIX 3);
  RESULTS R15 (a), (d); R17 (a) (V1)/(V2), (F1)/(F2), R17 (b) Lemma P (its induction step), (c) Theorem PH's case split, (d); R18 (d) Lemma S
  (a), (c); R21 (a) Lemma XW (= (VJ), RESULTS R57); R23 (g) Lemma WM (game-general, RESULTS R63 XEP-N2); R64 (a), (b) with the repair EPR-1
  (proofs read with G^u in place of G′_E); for the implications, premise (Στ) of RESULTS R64 (e) and R51 (a); the standing SPEC premise 1E-N3
  (RESULTS R57), under which both referees sign (N-HON-3, REFEREE-2; accepted by REFEREE):
  (a) Lemma HON: in every phase, the W-honest states number at most f + 4n² − 3n.
  (b) Lemma SAT0: if σ_k has no W-improving edge in G_τ, then W_k(x) ⪰ value(r) for every x and every such simple path r. In its Odd case the
      packet's parenthesis "(r′ and z's play avoid x)" reads "z's path to its cycle node avoids x" (N-HON-1, REFEREE-2; a note, settled in
      both §Cs).
  (c) Lemma HON-FB: a fallback h → h + 1 at a W-honest state h is flat (values unchanged), leaves no W-improving edge, and lands on a
      W-honest, saturated state that is the phase's last ((i)-(iv)).
  (d) Corollary HON′: the W-honest states of a phase number at most f_in + 4n² − 3n.
  (e) Corollary HON-0: (a) the D = ∅ states, (b) N_0, the epochs with D_E = ∅, and (c) the in-phase transitions whose source lies in a D = ∅ epoch each
      number at most f_in + 4n² − 3n. Relation to RESULTS R66 (REC-0), both confirmed by both referees: HON-0 (b) implies R66 (a) strictly,
      since (f + 1)(n + 1) + 4n(n − 1) + 1 − (f + 4n² − 3n) = f·n + 2 > 0 and f_in ≤ f, and HON-0 (c) implies R66 (b) without the factor n + m;
      HON's proof uses neither REC-0, SN-PREFIX_D nor EP-0, and REC-0's proof does not use HON (REFEREE §2, by script; REFEREE-2 §2), but the premise sets overlap: XW is in both chains (HON-N1, REFEREE), so the
      packet's "HON-FB adds XW" is inexact.
  (f) Lemma RESTRICT_u: for every state k with D_k ⊆ {u}, RESULTS R64 (a) (i)-(iv) hold with G′_E replaced by G^u. Corollary REPRO_u: N5^τ on
      G^u from (σ_x, τ) reproduces a u-run J = (x, …, y) of N5 on G state by state, with the same fallback types, through y′ := x + len(J), in
      one N5^τ phase as read with EPR-1.
  (g) Theorem REC-1 (a): in every phase the {u}-intervals, over all u ∈ Q, number at most 1 + (f_in + 4n² − 3n) + X_dir + X_big.
  (h) IMPLICATIONS from (Στ) (signed as implications, as the packet states them): Corollary EP-1u: every u-run J has len(J) ≤ T*(G^u) + 1.
      Theorem REC-1: (b) every {u}-interval has at most T*(G^u) + 2 states; (c) the states with |D_k| = 1, and the epochs with |D_E| = 1, number
      at most (1 + f_in + 4n² − 3n + X_dir + X_big)·(T*_Q + 2); (d) if every state of the phase has |D_k| ≤ 1, then X_big = 0 and the phase has
      at most (f_in + 4n² − 3n) + (1 + f_in + 4n² − 3n + X_dir)·(T*_Q + 2) states. Both referees note that (h) holds at RESULTS R65's audit strength, not signed in that form (REFEREE's verdict line; REFEREE-2 §0 and N-HON-4: (Στ) as used here is RESULTS R64 (e)'s premise word for word).
  Q-R17 (as in RESULTS R66 (c)), answered YES by both in HON's own use, with REFEREE's three-use list, accepted by REFEREE-2: Lemma HON's
  step 1 uses the full step at a W-honest state h, the absence of a cycle-node change coming from the sandwich W_h ⊴ W_{h+1} ⊴ W_{h′} (WM
  along a fallback-free gap); SAT0 uses Case A at one state, without (F2); HON-FB (i) uses the B1/B2 outcome list (re-derived by both: REFEREE §2, REFEREE-2 §2).
- Not signed (packet §5, §6): CONJECTURE HON-FF (the level rises across every gap between W-honest states, fallbacks included; it would give
  W-honest states ≤ 4n² − 3n per phase, free of f), OPEN; its three DEAD routes, recorded in the packet with instances: IMM (immfail_n14, sha1
  db3fc2ca), IMM′ (immp_cex_n11, sha1 1dd7f585, and exitr_cex_n16), FB-WLEV (b5_o11, sha1 db4fe55a); also DEAD there as context: the
  permanent Ξ-level in H_C for |D_C| = 1 (thclimb_n12_s11) and "no in-phase fallback at a W-honest state" (b4_n5_other_0, replaced by
  HON-FB); the data. L-COMP successor 5's later add-on (l-comp 15bcfa06; DATA, not a referee check) finds 0 HON-FF failures with exact LEV
  and pins three more inside-fallback gaps (up to 12 fallbacks in one gap, ffin12_n32). L-NEW successor 26's later packet P-N5-HONFF (docs/new/P-N5-HONFF-box47.md, sha1 98101d1f, pinned at 4a0a8aba) claims a proof of HON-FF; it is unrefereed and not part of this entry.
- Honest limits: (i) Reductions: f_in, X_dir and X_big are not bounded here, and (h) needs T*(G^u), which is polynomial but very large (R51 (a)).
  (ii) HON-FF would remove f_in; an HON-FF proof must replace both uses of the fallback-free hypothesis, the rise and the sandwich (HON-N3,
  REFEREE). (iii) Thin data where the proofs are subtle (N-HON-5): in-gap fallbacks occur in 9 phases (16 fallbacks) of REFEREE-2's library
  runs and in none of its random runs, and REFEREE's climbs produced none (one inside-gap case at LEV exact in its LEVMAX-20 lib41 pass); exact
  LEV meets 128 library step-1 checks in REFEREE-2's runs; the HON bound is never approached (max 57 W-honest states in a phase, both
  engines); REFEREE-2's mutation hon does not bite; T* is so large that (h) is tested only in its structural parts.
- Data (DATA, not proof): REFEREE (successor 14, own engine; lane code not run): 0 failures; lib41 1,101 runs, 5,365 phases, 20,473
  RESTRICT_u checks, max 57 W-honest states; lib41 n ≤ 20 at exact LEV (422 step-1 gaps); random games n 4-11 (9,000 runs) and n 12-22
  (4,500 runs); climbs: 48,751 candidates with LEV (235,399 step-1 gaps) and 19,754 without; controls: MUT=1 (G^u cut at u) RU1 55, RU2 46,
  REPU 15 failures, MUT=3 (a rise of 2) 5 of 70; IMM′'s failure reproduced on immp_cex_n11. REFEREE-2 (successor 16, own hon_check.py with
  exact LEV for n ≤ 11 and its own N5^τ for REPRO_u; lane code not run): 23,344 runs over its §4.2 rows (packet and lane instances, lib41
  minus referee games, its 503 𝒞^1O files, random games with 2-4 Odd choice vertices, random 𝒞^kO n 12-20), 0 violations; longest u-run
  reproduced by N5^τ on G^u 112 transitions (xsn91_n48); mutations fb4, ru, r1 and s1 bite.
- Signatures: REFEREE docs/referee/R-N5-HON.md (referee e7f9bc31, independence-line correction 59121877, §C a00a15c0, successor 14): all
  §1-§4 items SIGNED, (h) as implications, no gap; §2 claims TRUE; notes HON-N1..N4. REFEREE-2 docs/referee-2/R2-N5-HON.md (referee-2
  1566b439, §C 7f8bafdc, successor 16): all SIGN, (h) as implications, no gap; notes N-HON-1..5. §C (both): verdicts identical item by item;
  N-HON-1 settled as a note (both read the parenthesis as "z's path to its cycle node avoids x"; it is false only of z's infinite play, REFEREE C.2; REFEREE-2 withdrew "false"); HON-N1, HON-N2, HON-N3 accepted by
  REFEREE-2; N-HON-1, N-HON-3 accepted by REFEREE; N-HON-2, N-HON-4, N-HON-5 match REFEREE's report in substance; joint gap map empty; nothing open on the signed items (HON-FF stays OPEN). Both signatures are under the standing SPEC premise 1E-N3 (P1, P2) (N-HON-3).
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (per-phase reductions; no running-time bound). GAPS G-N5-TIME: open.

### R69 [refereed-only] N5 on EVERY game, inside one phase: a change of Ξ at an Odd choice vertex (a ρ event) needs an Even switch on an exit path from Q (ROOT); at a terminal on no honest cycle, a ρ event that is not caused on its own route is relayed from another terminal of its class (ROUTE-RELAY), never with one Odd choice vertex per class (SELF-FREE); per class, with the exits included, unchanged exit paths and exits keep κ (ROOT-C, corrected form); on an interval with no fallback and σ̄|Q, Ξ|Q fixed, N5 runs on two fixed one-player games (STATIC); and a relay flip between two terminals q1, q2 needs a switch on q1's old exit path, overlapping exit paths, or a strict rise of κ(q2) by at least the weight of an Odd-unattractive cycle C (FLIP, N1 ∨ N2 ∨ N3); when C's top lies above c (and, if it lies on q2's exit path, that path is intact at t1), q2's path set changes at a rank ≥ that top (N3-LEVEL) (2026-10-26) — structural lemmas for N5 beyond one Odd choice vertex (no count: the number of flips and of ρ events per phase is not bounded here; not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C78.md, checker 978791e1)
- Object (packet P-N5-FLIP, added at l-si 7ea3d8cf, pinned trunk d67fdb87, unchanged during review): docs/si/P-N5-FLIP-box18.md, sha1
  96a7e088c2175f71ab1aef2577d6139f80a4efff (L-SI successor 14, Opus 5.5). The referees' notes and repairs are collected by the lane in
  docs/si/P-N5-FLIP-fixes-box18.md (l-si b5d3d321, sha1 93a65e1b7e1df4a1d19a16c1f5ebb794e1d4331b, L-SI successor 15: G-FLIP-1..3 with the
  referees' repair texts, FLIP-N1..N4, N-FLIP-1..4; 23 quotes checked by script); on trunk; repairs only.
  Setting (every game): phases as in RESULTS R38 (a); Q := the Odd vertices of out-degree ≥ 2; classes, U_c, κ, κwt_c and ρ events as in
  RESULTS R56 and R61; for q ∈ Q and y ∈ succ(q), the Q-EXIT PATH of y at s is the play from y in G_{σ_s} up to and including the first vertex
  in Q or repeated; for q ∈ Q_c, the EXIT of y ∈ succ(q) ∩ U_c is the first vertex of Q_c ∪ {c} on y's honest play, and its CLASS EXIT PATH
  the part strictly before it; a ρ event at q is ROUTE if some such y has a different class exit path or exit at t and t + 1, RELAY
  otherwise. A FLIP is (q1, q2, t1 < t2) in one phase with par_{t1}(q1) = q2 and par_{t2}(q2) = q1, exit paths p1 := p_{t1}(q1), p2 :=
  p_{t2}(q2), closed walk C = q1·p1·q2·p2.
- Claims signed (both referees "(Opus 5.5, D15)", L37), on every game; no item uses (P); premises LANDED: RESULTS R38 (a), R56 (setting,
  (d) κ-Y-FORM_D, named also in ROUTE-RELAY's premise line, FLIP-N1), R57 (a) and the standing SPEC premise 1E-N3 in its two forms (P1:
  S1's σ̄ is Odd's pointwise optimum in G_σ; P2: S4a's step is Even's optimum in its arena), R62 (d) WM-G's premise line, R15 (a), (d) via
  (VJ) ((SG)), R61 (a), (e). P1 only: ROOT, ROUTE-RELAY, SELF-FREE, ROOT-C, FLIP (b); P1 and (SG): FLIP (a), (c), N3-LEVEL, and the necessary condition (from (a)-(c)); STATIC uses P2
  only (N-FLIP-1, REFEREE-2; accepted by REFEREE):
  (a) Lemma ROOT: if at an in-phase transition t → t + 1 every Q-exit path is the same at t and t + 1, then Ξ_t = Ξ_{t+1} on Reach_t(Q);
      so every transition carrying a ρ event switches some Even vertex on a Q-exit path.
  (b) Lemma ROUTE-RELAY: for q ∈ Q_c on no honest cycle at t and t + 1, a RELAY event at q has a SOURCE: an exit e ∉ {q, c} with κ_t(e) ≠
      κ_{t+1}(e), or with e's honest play avoiding q at exactly one of t, t + 1. Corollary SELF-FREE: if Q_c = {q}, every such ρ event at q is
      ROUTE.
  (c) Lemma ROOT-C, corrected form, SIGNED WITH GAPS G-FLIP-1 (= ROOTC-2) and G-FLIP-2 (= ROOTC-1), both closed (both referees; the packet's literal form NOT SIGNED: FALSE): if at an in-phase transition every class exit path AND EXIT
      of every q′ ∈ Q_c (from every y ∈ succ(q′) ∩ U_c) is the same at t and t + 1, then κ_t(q) = κ_{t+1}(q) for every q ∈ Q_c; so every
      transition with a ρ event at a terminal of class c changes a class exit path or exit of class c. As written in the packet (exit paths
      only), ROOT-C is FALSE: an Even last vertex can switch exits without changing its path (witnesses n4_thch_0, sha1 77018c63, found by
      both referees, and REFEREE's rootc_lit_n5, sha1 602e6db6). Its proof's step "each walk is the play of a positional Odd strategy with
      cycle node c" is false when a walk leaves c's honest cycle at an Odd vertex on it (G-FLIP-2 = ROOTC-1, both referees; witnesses
      leanT_N6 and best_tog_83); the conclusion stands by REFEREE-2's repair, the Bellman inequality B(e, y): κ_s(e) ⪯ κwt(e) + κwt(p_y) +
      κ_s(e′) along the walk's steps, with REFEREE's equivalent LOCAL form κ_s(e) ⪯ κwt(e) + κ_s(y) as a remark (P1 only; the two are the same inequality by additivity, both referees; both referees accept either).
  (d) Lemma STATIC: on a ρ-FREE INTERVAL I (a maximal run of in-phase transitions with no fallback and Ξ|Q, σ̄|Q constant), σ̄_k = σ̄_I on all
      Odd vertices and τ_k = τ_I, so I is a run of "improve in G_{σ̄_I}, choose by G_{τ_I}" on two fixed one-player games ("Ξ|Q constant" is part of the cut and not used in the proof, REFEREE).
  (e) Lemma FLIP: (a) FLIP-COST: κ_{t2}(q2) ⪰ κ_{t1}(q2) + wt(C); (b) FLIP-1: if p1 is intact at t2, the cycle that q1's play reaches in
      G_{σ_{t2}} when q1 re-chooses σ̄_{t1}(q1) has a node w with rew(w) > rew(c); (c) Corollary: if moreover p1 ∩ p2 = ∅, that cycle is C,
      wt(C) ≻ 0, and κ(q2) rises strictly between t1 and t2 by at least wt(C). NECESSARY CONDITION at every flip: (N1) an Even vertex of p1
      switches between t1 and t2, or (N2) p1 ∩ p2 ≠ ∅, or (N3) κ(q2) rises strictly between t1 and t2 by at least wt(C), C an
      Odd-unattractive cycle through q1 and q2.
  (f) Lemma N3-LEVEL, SIGNED WITH GAP G-FLIP-3 (minor; REFEREE-2, accepted by REFEREE): for a flip with p1 ∩ p2 = ∅, with h the
      highest-ranked vertex of C, rank(h) > rank(c) and h even (and, if h ∈ p2, p2 intact at t1), q2's path set changes between t1 and t2 at
      a rank ≥ rank(h). The packet's parenthesis "(both hold when p1 is intact at t2, by (c))" does not follow: (c) gives only the
      disjunction "rank(h) > rank(c) with h even, or rank(h) < rank(c) with c odd"; it is unproved, not shown false (the second alternative
      occurs in neither referee's data), and is replaced by that disjunction; the lemma under its explicit hypotheses is unaffected.
- Not signed (packet §7, §8): CONJECTURE FRZ-RHO; ROOT-C's strong form (all relays chain to a route event; DATA); the READINGs (in
  particular that N3 flips of a pair are at most 2^{#ranks ≥ top(C)}); the data. The flip type "C below an odd c" left open by G-FLIP-3 is
  OPEN.
- Honest limits: (i) Structural lemmas: no count of flips, ρ events or phases is given; N1 flips (switches on the old exit path) are not
  charged here, and in the OPEN case "C below an odd c" (G-FLIP-3) N3's rise is a pure length rise, by at least |C| (fixes R3). (ii) N3-LEVEL's sharpness pin leanT_N6 is reproduced by REFEREE (its
  three equalities) but not by REFEREE-2 (no multi-state phase from its starts; it sees equality 80 times elsewhere). (iii) Lane work after
  the packet (L-SI 15's CHOSEN and RELAY-CHAIN, L-RED 21's N3-CHAIN in R87) is not part of this entry.
- Data (DATA, not proof): REFEREE (successor 14, own engine; lane code not run): 0 failures of every signed item with ROOT-C in its
  corrected form; lib41 1,101 runs, 5,365 phases, 1,002 flips, 12 N3-LEVEL checks; random games n 5-24 (12,000 runs); pp_K12 with its start,
  60 flips, all N3, 60 N3-LEVEL checks; ROOT-C's min formula in 105k+ checks and the LOCAL inequality in 462k+; controls: FLIP-COST with
  wt(C) doubled fails 55 times, strict N3-LEVEL fails 3 times on leanT_N6. REFEREE-2 (successor 16, own flip_check.py with its own play
  values and walks; lane code not run): 17,245 N5 runs, 13,876 ρ events, 0 violations of every signed check; ROOT-C's exits form 0
  failures, the walk-form conclusion 10,993 checks; on its 𝒞^1O set every event is ROUTE (SELF-FREE); mutations root, cost and lev bite.
- Signatures: REFEREE docs/referee/R-N5-FLIP.md (referee 8317a435, §C 72db1b18, successor 14): ROOT, ROUTE-RELAY, SELF-FREE, STATIC, FLIP
  (a)-(c), the necessary condition SIGNED; ROOT-C as written NOT SIGNED (ROOTC-2), corrected form SIGNED WITH GAP ROOTC-1, closed by the
  repair; N3-LEVEL SIGNED WITH GAP G-FLIP-3 (in its §C, accepting REFEREE-2's finding); notes FLIP-N1..N4. REFEREE-2
  docs/referee-2/R2-N5-FLIP.md (referee-2 e9044674, §C 75b8b52a, successor 16): the same items SIGN; ROOT-C SIGN WITH GAPS G-FLIP-1, G-FLIP-2; in its §C, adopting REFEREE's wording: as written NOT SIGNED (false), corrected form SIGNED WITH GAP ROOTC-1 = G-FLIP-2 closed (REFEREE's §C in turn accepts REFEREE-2's single line as the joint verdict);
  N3-LEVEL SIGN WITH GAP G-FLIP-3; notes N-FLIP-1..4. §C (both): no disagreement on any signed lemma; joint gaps G-FLIP-1 = ROOTC-2
  (statement; found by both), G-FLIP-2 = ROOTC-1 (proof step; found by both; equivalent repairs), G-FLIP-3 (parenthesis; REFEREE-2 only),
  all minor and closed by the fixes file; notes, the union of FLIP-N1..N4 and N-FLIP-1..4; both under the standing premise 1E-N3 (P1, P2).
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (structural lemmas; no running-time bound). GAPS G-N5-TIME: open.

### R70 [refereed-only] N5 on EVERY game: an in-phase fallback is a Bellman-Ford step of the honest valuation, so across it the level LEV reaches min(LEV + 1, LEV_odd, n − 1), a rise unless an Odd vertex's own level binds or LEV is saturated (Lemma FB-RISE (a)), and after a W-honest state h it reaches min(LEV(h) + 1, n − 1) (FB-RISE (b)); hence in every phase the W-honest states number at most 4n² − 3n (Theorem HON-FF), with no fallback term, and so do the D = ∅ states, the D = ∅ epochs and the in-phase transitions whose source lies in a D = ∅ epoch (HON-0-FF), and the {u}-intervals of a phase number at most 1 + (4n² − 3n) + X_dir + X_big (REC-1-FF (a)); as IMPLICATIONS from premise (Στ), the |D| = 1 part of a phase is bounded by REC-1-FF (c), (d) (2026-10-26) — partial step-4 lemmas for N5 beyond one Odd choice vertex (the D = ∅ part of every phase is free of f; f itself, X_dir, X_big and |D| ≥ 2 epochs are not bounded here; not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C79.md, checker 1199b9a9)
- Object (packet P-N5-HONFF, added at l-new 2fca63b8, pinned trunk 4a0a8aba, unchanged during review): docs/new/P-N5-HONFF-box47.md, sha1
  98101d1fe723a570f3c79085b929a456ebb7dff5 (L-NEW successor 26, Opus 5.5). The referees' notes are collected by the lane in
  docs/new/P-N5-HONFF-fixes-box47.md (l-new b2dcf365, sha1 ccc520dd83c9086b57a2417c1cdcede44e7b7865, L-NEW successor 27: HONFF-N1..N3,
  N-HONFF-1..4, the independence addendum; 45 quotes checked by script); on trunk; repairs only, no signed statement changes.
  Setting (every game): as in RESULTS R68 (N5 = SPEC S1-S5; Ξ_k the value of the honest play (σ_k, σ̄_k); W_k := V_{σ_k,τ_k}; phases; W-HONEST
  states; LEV(k) the largest j ≤ n − 1 with Ξ_k(x) ⪰ value(r) for every x and every simple path r of G_τ with ≤ j edges to a cycle node of λ;
  f_in, X_dir, X_big, T*_Q). LEV_odd(k): the same with x ranging over the Odd vertices only, so LEV(k) ≤ LEV_odd(k).
- Claims signed (both referees "(Opus 5.5, D15)", L37), on every game; no item uses (P); premises LANDED: SPEC S2, S4c with FIX 3; RESULTS R15
  (a), (d) ((MON)); R17 (a) (V1)/(V2), R17 (b) Lemma P's Case A; RESULTS R68 (HON, its step 1 for fallback-free gaps, and the Odd-case argument
  of SAT0's proof (b), with the wording of R68 (b)); the standing SPEC premise 1E-N3, FB-RISE using P1 only (through (MON)) and HON-FF P1 and
  P2 (P2 only through HON's step 1) (N-HONFF-2, REFEREE-2; accepted by REFEREE). The packet's premise list names XW, which HON-FF does not use
  (N-HONFF-1, REFEREE-2; checked by REFEREE); and it cites "SAT0's Odd case" where the Odd-case argument of SAT0's proof is meant, SAT0's
  hypothesis need not hold at h (HONFF-N1, REFEREE = REFEREE-2 §1 (b)):
  (a) Lemma FB-RISE: let t → t + 1 be an in-phase S4c fallback and j := min(LEV(t) + 1, LEV_odd(t), n − 1). (a) (general form) LEV(t + 1) ≥ j.
      (b) (honest form) If h ≤ t is a W-honest state of the phase, then LEV(t + 1) ≥ min(LEV(h) + 1, n − 1).
  (b) Theorem HON-FF: in every phase P of N5, the W-honest states number at most 4n² − 3n.
  (c) Corollary HON-0-FF: in every phase, (a) the D = ∅ states, (b) N_0, the epochs with D_E = ∅, and (c) the in-phase transitions whose
      source lies in a D = ∅ epoch each number at most 4n² − 3n. Against RESULTS R66 (REC-0): (f + 1)(n + 1) + 4n(n − 1) + 1 − (4n² − 3n) =
      f(n + 1) + 2 > 0 for every f ≥ 0, n ≥ 1 (checked by both referees).
  (d) Corollary REC-1-FF (a): the {u}-intervals of a phase, over all u ∈ Q, number at most 1 + (4n² − 3n) + X_dir + X_big.
  (e) IMPLICATIONS from (Στ) (signed as implications; both referees note that they hold at RESULTS R65's audit strength): REC-1-FF (c) the
      |D_k| = 1 states, and the epochs with |D_E| = 1, number at most (1 + 4n² − 3n + X_dir + X_big)·(T*_Q + 2); (d) if every state of the
      phase has |D_k| ≤ 1, the phase has at most (4n² − 3n) + (1 + 4n² − 3n + X_dir)·(T*_Q + 2) states.
  Q-A (the packet's question to the referees), answered YES by both, with the same list: Lemma P's Case A (A1, A2) with Ω := Ξ_t reads only
  facts about the value of a single play of a positional strategy pair (the Case-A non-improvement inequality from S2, the bound at the
  suffix from LEV(t), (V1) with the path to the cycle node avoiding x, (V2), and the own-cycle-node facts), so it holds for the honest
  valuation and needs no optimality premise; A1's last link via (F2) is replaced by (MON).
- Not signed (packet §3, §4): the data; §4's READING (f on general games is not bounded here: a fallback with LEV_odd(t) ≤ LEV(t) need not
  raise LEV; fallbacks with no W-honest state before them are not touched by (b)).
- Honest limits: (i) The D = ∅ part of each phase is free of f; f itself, X_dir, X_big and the |D| ≥ 2 epochs are not bounded here (lane work
  after the packet, P-N5-FBC, under review, bounds f by distinct configurations; not part of this entry). (ii) (e) needs T*(G^u), polynomial
  but very large (RESULTS R51 (a)). (iii) Thin decisive data (N-HONFF-3, both referees): exact LEV was reached on 5 of the 6 known gaps
  with a fallback inside (j7_n32 stays over budget on both engines, REFEREE-2 even at 1.5·10⁸ paths per phase); REFEREE verified 10 inside
  fallbacks exactly, with 7 phases over budget. The "no Odd term" control fails, always where LEV_odd binds (both referees; "always where LEV_odd binds" is REFEREE's observation), so the Odd term
  in (a) is needed.
- Data (DATA, not proof): REFEREE (successor 14, own ff_probe; lane code not run): 0 failures in 23,129 phases (the packet's six
  inside-gap instances with their starts, lib41 n ≤ 20, random games n 5-12, 9,000 runs); max 18 W-honest states in a phase; the "+2"
  mutation bites (5). REFEREE-2 (successor 16, own honff_check.py; lane code not run): 0 violations; FB-RISE (a) exercised at 1,642
  in-phase fallbacks (1,084 at non-honest states) in its sets (overlapping sets; its report §4); Case A checked pointwise 661M+ times, 0 failures; mutations
  ctrl and b2 bite (b2 once).
- Signatures: REFEREE docs/referee/R-N5-HONFF.md (referee cce5ea5e, §C e7db1ab4, successor 14): all SIGNED, (e) as implications, no gap;
  Q-A YES; notes HONFF-N1..N3. REFEREE-2 docs/referee-2/R2-N5-HONFF.md (referee-2 05e7663c, independence addendum 1306c31e, §C 11e3cfb1,
  successor 16): all SIGN, (e) as implications, no gap; Q-A YES; notes N-HONFF-1..4. §C (both): verdicts identical; joint gap map empty;
  N-HONFF-1, N-HONFF-2 accepted by REFEREE; HONFF-N1 = REFEREE-2 §1 (b); N-HONFF-3, N-HONFF-4 match REFEREE's data; REFEREE-2's independence
  addendum (it saw REFEREE's file name and commit subject, never the file, after its report was final) accepted by REFEREE, no effect;
  nothing open on the signed items. Both under the standing premise 1E-N3.
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (per-phase bounds and reductions; no running-time bound). GAPS G-N5-TIME: open.

### R71 [refereed-only] N5 on EVERY game: in the honest frame H_C of a configuration C = σ̄|Q (every Odd vertex cut to its σ̄_C edge), an in-phase fallback from a C-state raises the level LEV_C to at least min(LEV_C + 1, n − 1) (Lemma FB-RISE_C); LEV_C = n − 1 at a C-state gives Ξ = B_C, and later C-states of the phase follow within 4n(n − 1) transitions with Ξ constant (Lemma SAT_C); hence in every phase the in-phase fallbacks number at most |𝒞_f(P)|·(4n² − 3n), 𝒞_f(P) the configurations at fallback sources (Theorem FB-C), so f ≤ (4n² − 3n)·min(N_ep, Π_q deg(q)), f ≤ Δ^k(4n² − 3n) on 𝒞^kO, and f ≤ (1 + m)(4n² − 3n) when |D| ≤ 1 throughout (Corollaries (a)-(d)) (2026-10-26) — a REDUCTION of f to the number of distinct configurations per phase (that number is not bounded here on general games; (a)'s N_ep form and (d) are weaker than RESULTS R60 (c) EPOCH for n ≥ 2; not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C80.md, checker 4069b310)
- Object (packet P-N5-FBC, added at l-new 1f8d6d7d, pinned trunk de02d37e, unchanged during review): docs/new/P-N5-FBC-box47.md, sha1
  32d3776cf4090fb15c1d0cb4c8b4f59276f64e21 (L-NEW successor 26, Opus 5.5). The referees' notes are collected by the lane in
  docs/new/P-N5-FBC-fixes-box47.md (l-new c2691e46, sha1 1347222ccc39ea380035da050b8af2f7cc8473d6, L-NEW successor 28: R1-R6 for FBC-N1, -N2,
  -N4, N-FBC-1..5 and REFEREE's n = 1 line; §4: FBC-N3 is not a repair but P-N5-EPC §3; 45 quotes checked by script); on trunk; repairs only,
  no signed statement changes.
  Setting (every game): as in RESULTS R70 (N5 = SPEC S1-S5; Ξ_k the value of the honest play; phases; λ; value(r); f). Q := the Odd vertices of
  out-degree ≥ 2; a CONFIGURATION is C = σ̄|Q, k is a C-STATE if σ̄_k|Q = C; H_C := G with every Odd v cut to its one edge σ̄_C(v) (H_{τ|Q} = G_τ);
  LEV_C(k) := the largest j ≤ n − 1 with Ξ_k(x) ⪰ value(r) for every x and every simple path r of H_C with ≤ j edges from x to a cycle node of
  λ, defined at every state of the phase, LEV_C ≥ 0 there (N-FBC-1, REFEREE-2; checked by REFEREE) and non-decreasing along it; B_C(x) := the
  maximum of value(r) over the simple H_C-paths r from x to a cycle node of λ; 𝒞_f(P) := the configurations of the sources of P's in-phase S4c
  fallbacks; D_k := {q ∈ Q : σ̄_k(q) ≠ τ(q)} as in RESULTS R68 (P-N5-HON §0), and epochs / N_ep as in RESULTS R60, R61 (the packet imports them
  from P-N5-HONFF §0, which does not define them: FBC-N1 = N-FBC-3).
- Claims signed (both referees "(Opus 5.5, D15)", L37), on every game; no item uses (P); premises LANDED: SPEC S2, S4c with FIX 3; RESULTS R15
  (a), (d) ((MON), and R15 (d)'s window applied to Ξ through RESULTS R57 (a) (VJ) under the standing premise 1E-N3, P1 (FBC-N2, REFEREE; the
  packet's "read as S1's Ξ" names no source)); R17 (a) (V1)/(V2), R17 (b) Lemma P's Case A with Ω := Ξ_t (RESULTS R70's Q-A, YES by both);
  R38 (a); RESULTS R70 (a) FB-RISE's proof, items 2-3 (Even vertices), used verbatim; for (a), (d) only RESULTS R61 (f):
  (a) Lemma FB-RISE_C: if t → t + 1 is an in-phase S4c fallback whose source t is a C-state, then LEV_C(t + 1) ≥ min(LEV_C(t) + 1, n − 1). Its
      Odd case uses no fallback and holds at every C-state (REFEREE); its Even case holds at any source state, the C-state hypothesis being
      needed only for the Odd case (N-FBC-2, REFEREE-2; accepted by REFEREE).
  (b) Lemma SAT_C: if t is a C-state with LEV_C(t) = n − 1, then Ξ_t = B_C; and if t < t′ are C-states of the phase with LEV_C(t) = n − 1, then
      Ξ is constant on t, …, t′ and t′ − t ≤ 4n(n − 1).
  (c) Theorem FB-C: in every phase P, f ≤ |𝒞_f(P)|·(4n² − 3n) (per C: at most n − 1 unsaturated and 4n(n − 1) + 1 saturated fallback sources).
  (d) Corollaries: (a) f ≤ (4n² − 3n)·min(N_ep(P), Π_{q ∈ Q} deg(q)); (b) on 𝒞^kO with maximum out-degree Δ, f ≤ Δ^k(4n² − 3n) per phase;
      (c) if every state of P has |D_k| ≤ 1, f ≤ (1 + m)(4n² − 3n), and the configurations with |D| ≤ d number at most
      Σ_{j ≤ d} C(|Q|, j)(Δ − 1)^j; (d) with RESULTS R61 (f), f ≤ (4n² − 3n)(1 + Σ_q (ρ_q + tie_q + nc_q + cyc_q)) (the inequality; the
      comparison sentences after it are READINGS, FBC-N4).
  Header claim CONFIRMED by both for n ≥ 2: (a)'s N_ep form and (d) are implied by RESULTS R60 (c) EPOCH (f ≤ 1 + n·N_ep; with R61 (f) for
  (d)), since 1 + n·N_ep ≤ (4n² − 3n)·N_ep ⇔ 1 ≤ 4n(n − 1)·N_ep; at n = 1, f = 0 (the only vertex has a self-loop only) (REFEREE; N-FBC-4,
  REFEREE-2). What FB-C adds over EPOCH is the per-configuration form: a configuration that recurs in the phase is paid once.
- Not signed (packet §3-§5): the τ-frame split and its DEAD charge (s4c8_n13, j5_n16); the data; the OPEN items (the number of distinct
  configurations per phase on general games; a better saturated term); the READINGs, including "incomparable with RESULTS R56", which is
  witnessed in one direction only (FBC-N4 = N-FBC-5: FB-C's number never beat EPOCH's or R56's in any phase REFEREE-2 ran, nor R56's in the two batches where REFEREE checked it; max
  N_ep/|𝒞_f| = 45 at n = 32 against 4n − 3 = 125, REFEREE-2).
- Referee strengthening (NOT part of this entry): FBC-N3 (REFEREE's proof, checked line by line and accepted by REFEREE-2 in its §C): at most
  one saturated fallback per configuration and phase, via SAT_C (b), RESULTS R15 (b) through R57 (a), and RESULTS R38 (f) CN-LAST, so
  f ≤ n·|𝒞_f(P)|. The same statement is a lane statement in packet P-N5-EPC §3 (Lemma SAT-FB, Corollary SAT-FB1, Theorem FB-C′; l-new
  81ab0b72, sha1 9f48ded7, pinned), proved by the lane on its own route and in review; it lands, if at all, with that packet.
- Honest limits: (i) A REDUCTION: f is bounded by distinct configurations at fallback sources, which is not bounded here on general games
  (Π_q deg(q) in the worst case); for fixed k and bounded degree (b) is O(n²) per phase. (ii) The saturated term 4n(n − 1) + 1 is untested:
  at most 1 saturated source per (phase, configuration) in every set of both referees, longest saturated window 2 transitions (tog6b_n32, REFEREE-2);
  REFEREE-2's "≤ 1 saturated per C" control cannot bite (N-FBC-6; FBC-N3 proves why). (iii) Over-budget pairs: REFEREE-2 left 173 (phase,
  configuration) pairs undecided at budget 3·10⁶ (1,519 fallback sources skipped for the LEV_C checks); at 3·10⁷ its six worst named
  instances are decided except one configuration in each of ffin12_n32, rise_thin51_n40, zcl_rx_n32; REFEREE's n ≤ 34 row has 115 UNK
  phases. (iv) No running-time bound.
- Data (DATA, not proof): REFEREE (successor 15, own fbc_probe.py on its own engine; exact LEV_C by simple-path enumeration in H_C; lane code
  not run): 35,720 runs in its §4 table over the library at n ≤ 20 and n ≤ 34 (1,140 files), two random 𝒞^kO batches (k ≤ 4, k ≤ 8) and
  fr39_q4_n48, with 2,794 in-phase fallbacks checked exactly by FB-RISE_C out of 3,384 (the other 590 in the n ≤ 34 row's 115 over-budget
  phases); its §C's "36,720 runs, 3,394 FB-RISE_C checks" is an arithmetic slip, corrected by its erratum below the §C (referee ae36ce48;
  LEAD-N1); 0 failures of REAL, MONO, FBC, ODDC, SATB, SATW, THM, CORA, CORC; FLATLAST (FBC-N3) 951 Ξ-flat fallbacks, all end their
  phase; reproduces fr39_q4_n48 (39 fallbacks, 7 configurations, 24 unsaturated) and farrise25_n32 (25); mutations MUT=1 (G_τ frame) 79,
  MUT=2 (+2) 144, MUT=3 (S4c minimum) 15 and FLATLAST 8 failures. REFEREE-2 (successor 17, own fbc_check.py; lane code not run): 21,753
  runs (named instances, lib41, its 503 𝒞^1O files, random games with 2, 4 and all Odd choice vertices); 2,294 fallback sources checked
  exactly (1,637 unsaturated); 0 violations of every signed check, Case A in H_C 32,431,842 times; max f 37 in one phase (rise_fb38_n48,
  |𝒞_f| 1); controls plus2 298 and tau 14,399 failures (the honest frame is what makes the Odd case free).
- Signatures: REFEREE docs/referee/R-N5-FBC.md (referee 0addfc5f, §C d08011be, successor 15): FB-RISE_C, SAT_C, Theorem FB-C, Corollaries
  (a)-(d) SIGNED, no gap; header claim CONFIRMED for n ≥ 2; notes FBC-N1..N4. REFEREE-2 docs/referee-2/R2-N5-FBC.md (referee-2 aab45be6,
  §C bde1ea77, successor 17): the same items SIGN, no gap; header claim CONFIRMED for n ≥ 2; notes N-FBC-1..6. §C (both): verdicts identical;
  joint gap map empty; FBC-N1 = N-FBC-3, FBC-N4 = N-FBC-5, REFEREE's n = 1 remark = N-FBC-4; N-FBC-1, N-FBC-2 accepted by REFEREE; FBC-N3
  accepted by REFEREE-2 and explains N-FBC-6; nothing open. Both under the standing premise 1E-N3 (P1) and RESULTS R70's Q-A.
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (a per-phase reduction of f; no running-time bound). GAPS G-N5-TIME: open.

### R72 [refereed-only] N5 on EVERY game, inside one phase: a RELAY ρ event at a terminal q is traced to the exit e of q's CHOSEN option (e ≠ c, e ≠ q): e has a ρ event at the same transition, or e's honest play at t + 1 passes through q (TOG) (Lemma CHOSEN); following chosen exits, every RELAY event chains in at most |Q_c| − 1 steps to a ROUTE or CYC event of its class at the same transition, or to a TOG step (Corollary RELAY-CHAIN), so Σ_{q ∈ Q_c} ρ_q ≤ |Q_c|·(ROUTE_c + CYC_c + TOG_c) per phase (consequence (b)); and once every non-terminal of a class sits at its target value TV_Θ (hypothesis (H)), the class has no Even switch outside its terminals and no ρ event to the end of the phase (Lemma TV-END) (2026-10-26) — structural lemmas for N5 beyond one Odd choice vertex (no count: ROUTE_c, CYC_c, TOG_c and the time to (H) are not bounded here; not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C81.md, checker 3c5ae7ee)
- Object (packet P-N5-CHOSEN, added at l-si b7189738, pinned trunk 9196c318, unchanged during review): docs/si/P-N5-CHOSEN-box19.md, sha1
  764cfbb331a1aaefa819a01d64ee6b7cfbbd7316 (L-SI successor 15, Opus 5.5). The referees' notes are collected by the lane in
  docs/si/P-N5-CHOSEN-fixes-box19.md (l-si d0b94c1f, sha1 2ae6f681c5abecc915f66296cd0c5a3d5fe1c73e, L-SI successor 16: F1-F7 for CHOSEN-N1..N5,
  N-CHOSEN-1..7; 22 quotes checked by script); on trunk; repairs only, no signed statement changes.
  Setting (every game): as in RESULTS R69 (phases as in R38 (a); Q; classes U_c, κ, κwt_c and ρ events as in RESULTS R56 and R61; EXIT and
  CLASS EXIT PATH per y; ROUTE / RELAY as there); Q_c := (Q ∩ U_c) ∖ {c}, T := Q ∪ {c}; a ρ event at q is CYC if q = c or q lies on its honest
  cycle at t or t + 1. The CHOSEN EXIT of q at t is the exit e of y* := σ̄_t(q), p its class exit path. A Q_c-RUN Θ is a maximal run of the phase
  with Ξ(q) constant for every q ∈ Q_c; TV_Θ(z) := max(κopt_c(z), max_{q ∈ Q_c} κopt^q(z) + κ_Θ(q)) for z ∈ U_c ∖ T with RESULTS R56's κopt_c,
  κopt^q (κ_Θ(c) means κ(c) = (0, 0): CHOSEN-N4, REFEREE); (H) at t ∈ Θ: κ_t(z) = TV_Θ(z) for every z ∈ U_c ∖ T.
- Claims signed (both referees "(Opus 5.5, D15)", L37), on every game, inside one phase, fallbacks included; no item uses (P); premises LANDED:
  RESULTS R15 (a), (d) ((SG) via (VJ), RESULTS R57 (a), under the standing premise 1E-N3, P1; (SW): every Even switch of N5 is to an edge
  of Iσ); R38 (a) KEY; R56 setting line, (d) κ-Y-FORM_D (its "≤" half resting on R18 (d) Lemma S (a), every game), (g) Lemma TV (only for
  when (H) holds); RESULTS R69's setting and additivity (P-N5-FLIP §1, signed as a proof step) and R69 (c) ROOT-C in its corrected form
  ("class exit path AND exit"). CHOSEN's identity κ_t(q) = κwt_c(q) + κ_t(y*) at t is the play decomposition (one-step additivity); R56 (d)
  with P1 is needed only for the "⪯" step at t + 1 (CHOSEN-N1 = N-CHOSEN-4, both referees):
  (a) Lemma CHOSEN: for q ∈ Q_c on no honest cycle at t and t + 1 with a RELAY ρ event at t → t + 1, the chosen exit e satisfies e ≠ c and
      e ≠ q, and either κ_t(e) ≠ κ_{t+1}(e) or e's honest play at t + 1 passes through q (TOG). The packet's statement says only "e ≠ c";
      e ≠ q follows from the same hypothesis and RELAY-CHAIN uses it (N-CHOSEN-2, REFEREE-2; accepted by REFEREE, who had checked it).
  (b) Corollary RELAY-CHAIN: with e_0 := q and e_{i+1} := the chosen exit of e_i while e_i has a RELAY event at t → t + 1, the e_i are distinct
      and the sequence stops after at most |Q_c| − 1 steps at an e_i whose event is ROUTE or CYC, or at a TOG step. Consequences: (a) every
      transition with a ρ event at a terminal of the class carries a ROUTE or CYC event of the class, or a TOG step; (b) per phase,
      Σ_{q ∈ Q_c} ρ_q ≤ |Q_c|·(ROUTE_c + CYC_c + TOG_c), ROUTE and CYC events mapped to themselves (N-CHOSEN-3, REFEREE-2; accepted by REFEREE),
      and REFEREE's §3 derives the sharper Σ_q ρ_q ≤ |Q_c|(ROUTE_c + CYC_c) + TOG_c (CHOSEN-N3; REFEREE-2's §C calls it a compatible reading of the same argument and does not sign it separately).
  (c) Lemma TV-END: if (H) holds at t ∈ Θ and t → t + 1 is in the phase, no Even vertex of U_c ∖ T switches at t → t + 1, t + 1 ∈ Θ and (H) holds
      at t + 1; hence from t to the phase's end class c has no switch in U_c ∖ T and no ρ event, and Θ lasts to the phase's end. By R56 (g), (H)
      holds at every t after |U_c| − 1 fallbacks of the phase and of a Q-run. REFEREE-2 signed TV-END conditional on ROOT-C's corrected form
      landing (N-CHOSEN-5); R69 (c) landed at trunk a7c141b8 with that wording, and its §C lifts the condition.
- Not signed: consequence (a)'s parenthetical "(This is the stronger, per-event form of ROOT-C's consequence …)", which is not an implication
  (CYC and TOG ends name no changed class exit path) (CHOSEN-N2, REFEREE; REFEREE-2's verdict is on the statement). READING (REFEREE's
  CHOSEN-N2, both §Cs): (a) proves RESULTS R69's not-signed CONJECTURE ROOT-C strong form up to the TOG alternative. Also not signed (packet
  §5): the obstruction map (READING) and the data.
- Honest limits: (i) Structural lemmas: no count; ROUTE_c, CYC_c, TOG_c and the number of transitions before (H) first holds are not bounded
  here; ρ events of the class all occur before (H) (TV-END bounds nothing by itself). (ii) TOG: CHOSEN's second alternative occurs, but in
  both referees' data never alone (the first alternative held at every RELAY event) and no chain ends in a TOG step (CHOSEN-N5 = N-CHOSEN-6,
  first half); the packet's §5 "TOG never occurs" is too strong. (iii) Over-budget classes: REFEREE-2 skipped 2,272 (phase, class) pairs for
  TV-END (κopt over 3·10⁵ paths; tcL_*, pp_K48_n449); REFEREE 122 UNK classes in its §5 rows and 668 in the n ≤ 40 batch.
- Data (DATA, not proof): REFEREE (successor 15, own chosen_probe.py; lane code not run): library n ≤ 24 (2,960 runs; ROUTE / RELAY / CYC
  2,482 / 678 / 92; chains up to 11), random 3,000 games with ≤ 8 and ≤ 12 Odd choice vertices (15,000 runs each), the lane's five
  instances at their starts and with S3, and the n ≤ 40 library batch (e49bf11a: 2,610 runs, 6,364 / 2,027 / 99, 1,485 TV-END checks, chains
  up to 11, ends 2,015 ROUTE / 12 CYC / 0 TOG); 0 failures; TV-END tested at every non-final (H) state, 4,356 checks in the library and random
  rows (2,145 with |Q_c| ≥ 1), so not thin (its §5; N-CHOSEN-6 second half); mutations MUT=1 (σ̄_{t+1}) CHO 5 / CHAIN 3, MUT=2 (TV without
  the q-terms) 24. REFEREE-2 (successor 17, own chosen_check.py; lane code not run): 21,949 runs (the lane's instances, lib2o, lib41, its 503
  𝒞^1O files, random games with 2, 4 and all Odd choice vertices); 6,322 RELAY events, 241 with TOG, first alternative at all of them; chains
  up to 86 (tcL_N12, |Q_c| = 233); 66,816 (class, state) pairs reach (H), 2,955 transitions checked after (H); KADD 2,161,705 and KORD
  2,410,459 self-checks; 0 violations; on its 503 𝒞^1O files 3,781 ROUTE, 68 CYC and 0 RELAY events (N-CHOSEN-7, cross-check of R69 (b)
  SELF-FREE); controls next 740 and noH 12,651 failures. Both reproduce the lane's nep90_n40 (153 / 139) and nep76_n40 (129 / 48) at its
  starts.
- Signatures: REFEREE docs/referee/R-N5-CHOSEN.md (referee b3473114, data e49bf11a, §C d08011be, successor 15): CHOSEN, RELAY-CHAIN, (a)
  (without its parenthetical), (b), TV-END SIGNED, no gap; notes CHOSEN-N1..N5. REFEREE-2 docs/referee-2/R2-N5-CHOSEN.md (referee-2 aab45be6,
  §C bde1ea77, successor 17): the same items SIGN, TV-END conditional on ROOT-C's corrected form, lifted in its §C (R69 (c) at a7c141b8); no
  gap; notes N-CHOSEN-1..7. §C (both): verdicts identical; joint gap map empty; CHOSEN-N1 = N-CHOSEN-4, CHOSEN-N5 = N-CHOSEN-6; CHOSEN-N3 and
  N-CHOSEN-3 compatible wordings of (b)'s count; N-CHOSEN-1, -2, -3, -7 accepted by REFEREE; CHOSEN-N2 accepted by REFEREE-2; N-CHOSEN-5
  closed by R69's landing; nothing open. Both under the standing premise 1E-N3 (P1).
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (structural lemmas; no running-time bound). GAPS G-N5-TIME: open.

### R73 [refereed-only] N5 on EVERY game: after an in-phase fallback, every configuration C finds its honest level LEV_C at least min(LEV_C(t) + 1, n − 1) at each of its later C-states (Lemma RET-FB), so a configuration has at most 2n² − n epochs per phase besides its fallback-free returns R⁰_C (Corollary VIS) and N_ep ≤ NCONF·(2n² − n) + R⁰ (Theorem EP-C); a fallback from a saturated C-state ends the phase or is followed by no further C-state of the phase (Lemma SAT-FB), so at most one saturated fallback per configuration and f ≤ n·|𝒞_f(P)| per phase (Corollary SAT-FB1, Theorem FB-C′); and N_ep ≤ (4n² − 3n) + N_1 + NCONF_{≥2}·(2n² − n) + R⁰_{≥2}, with N_1 bounded only as an implication from (Στ) (Corollary EP-ASM) (2026-10-26) — a REDUCTION of the epoch count N_ep to four open quantities X_dir, X_big, NCONF_{≥2}, R⁰_{≥2} (none bounded here; not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C82.md, checker c785690c)
- Object (packet P-N5-EPC, added at l-new 81ab0b72, pinned trunk e57ba8cb, quote base f4562054, unchanged during review):
  docs/new/P-N5-EPC-box48.md, sha1 9f48ded742d7f44bbf82ae8ec9e0e88c46457700 (L-NEW successor 27, Opus 5.5). The referees' notes are collected
  by the lane in docs/new/P-N5-EPC-fixes-box48.md (l-new c6a5d467, sha1 174aedd5de766a3f69a90c70cf2bfc1601956763, L-NEW successor 29: R1-R6 for
  EPC-N1..N3 and N-EPC-1..3; remarks for N-EPC-4, EPC-N4 = N-EPC-5; §5 DATA on non-flat saturated fallbacks; 41 quotes checked by script); on
  trunk; repairs only, no signed statement changes.
  Setting (every game): as in RESULTS R71 (N5 = SPEC S1-S5; Ξ_k the value of the honest play; phases (RESULTS R38 (a)); λ; value(r); f; Q;
  configurations C = σ̄|Q, C-states, H_C, LEV_C, B_C, 𝒞_f(P)); LEV_C ≥ 0 at every state of the phase (fixes R1 = EPC-N1, as in R71's setting).
  An EPOCH is a maximal run of the phase with σ̄|Q constant (RESULTS R64), N_ep its number, D_E := {q ∈ Q : σ̄_E(q) ≠ τ(q)}, and D_C := {q ∈ Q :
  C(q) ≠ τ(q)} for a configuration (fixes R5 = N-EPC-2); NCONF(P) := the distinct configurations of P's states, NCONF_{≥2}(P) := those with
  |D_C| ≥ 2. For a configuration C with epochs E_1 < … < E_V (V = V_C), a RETURN is a pair (i, i + 1); R⁰_C := its returns (i, i + 1) with no in-phase fallback source in [s_i, s_{i+1}) and LEV_C(s_i) ≤ n − 2 (s_i the first state of E_i);
  R⁰ := Σ_C R⁰_C, R⁰_{≥2} := Σ_{|D_C| ≥ 2} R⁰_C; REV(S) := (epoch starts in S) − (distinct configurations among them), per maximal
  fallback-free run S.
- Claims signed (both referees "(Opus 5.5, D15)", L37), on every game; no item uses (P); premises LANDED: SPEC S2, S4a ("Else σ_new = σ."),
  S4b, S4c, S5, FIX 3; the standing premise 1E-N3 (P1) with RESULTS R57 (a) (VJ); RESULTS R15 (a), (d) ((MON)); R17 (a) (V1), (V2), R17 (b)
  Lemma P's Case A with Ω := Ξ_t (RESULTS R70's Q-A, YES by both); R38 (a); R64 (the epoch); RESULTS R70 (FB-RISE (a)'s items 2-3,
  HON-0-FF (b), REC-1-FF (c)); RESULTS R68 (X_dir, X_big, T*_Q, (Στ)); RESULTS R71 (a), (b) (FB-RISE_C, SAT_C). The packet's §1 restates
  FB-RISE_C and SAT_C with their proofs; both referees signed the restatement: FB-RISE_C as identical to RESULTS R71 (a), and SAT_C as R71 (b) without its 4n(n − 1) window (which VIS (a) takes from R15 (d) through R57 (a)); R71 (a), (b) already hold it, so it is not re-landed here. SAT-FB's last step reads S4a / S4b / S4c / S5 and FIX 3 directly; the packet's citation of R68's HON-FB (iv) is a cross-reference only
  (fixes R6 = N-EPC-3, both referees):
  (a) Lemma RET-FB: if t → t + 1 is an in-phase S4c fallback of P, then for EVERY configuration C and every C-state s ≥ t + 1 of P,
      LEV_C(s) ≥ min(LEV_C(t) + 1, n − 1). The induction is on |r| at the fixed C-state s, and only its Odd branch calls the hypothesis
      (fixes R2 = EPC-N2); its Even step holds in every frame H_C at once (N-EPC-4, REFEREE-2; accepted by REFEREE).
  (b) Corollary VIS: per phase and configuration, V_C ≤ 2n² − n + R⁰_C (returns of kind (a), after saturation, ≤ 2n(n − 1); of kind (b) ≤ n − 1).
  (c) Theorem EP-C: N_ep(P) ≤ NCONF(P)·(2n² − n) + R⁰(P), and R⁰ ≤ Σ_S REV(S) over the ≤ f + 1 fallback-free runs S of P.
  (d) Lemma SAT-FB: if an in-phase fallback has a saturated C-state source t, then t + 1 is the last state of P or P has no C-state after t,
      by SAT_C (b), S2 and S4c's (Ξ_t(w), w)-maximum (a Ξ-flat fallback leaves Iσ_{t+1} = ∅) and S4a / S4b / S4c / S5. Corollary SAT-FB1: per
      phase and configuration, at most one in-phase fallback has a saturated C-state source. Theorem FB-C′: f ≤ n·|𝒞_f(P)| per phase; hence
      f ≤ n·N_ep (implying RESULTS R60 (c)), f ≤ n·Δ^k on 𝒞^kO with maximum out-degree Δ, and f ≤ n(1 + m) when every |D_k| ≤ 1 (with RESULTS
      R71 (d)'s counts). FB-C′'s proof stands without REFEREE's FBC-N3 route (no R15 (b), no R38 (f) CN-LAST): both referees, in answer to
      the Lead's question; FBC-N3 (REFEREE's note on R71) reaches the same conclusion by another route.
  (e) Corollary EP-ASM: N_ep(P) ≤ (4n² − 3n) + (1 + 4n² − 3n + X_dir + X_big)(T*_Q + 2) + NCONF_{≥2}(P)·(2n² − n) + R⁰_{≥2}(P), signed as an
      assembly, its second term (the |D_E| = 1 epochs N_1, by RESULTS R70 REC-1-FF (c)) signed AS AN IMPLICATION from (Στ). Term by term
      (REFEREE §4, both): 4n² − 3n bounds N_0 unconditionally (R70 HON-0-FF (b)); the N_1 term is an implication, with T*_Q (RESULTS R51 (a))
      polynomial but very large and X_dir, X_big OPEN; the factor 2n² − n is proved (VIS) and NCONF_{≥2} is OPEN; R⁰_{≥2} is OPEN. The packet's
      statement line should name these four open terms (fixes R3 = EPC-N3).
  (f) Remark: (D changes) + 1 ≤ N_ep (τ fixed on the phase).
- Not signed (packet §6): the data, the OPEN items and the READINGs, including CONJECTURE SAT-1 (no C-epoch after a saturated C-state, which
  would make VIS's kind (a) zero; SAT-FB1 bounds saturated fallbacks, not epochs: EPC-N4). The packet's §5 DEAD item ("a fallback from a saturated
  C-state is flat and ends the phase") is CONFIRMED DEAD by both referees on their own runs (rho3_253_n32; cond_stuck_symsi3_YE).
- Honest limits: (i) A REDUCTION: EP-C and EP-ASM bound N_ep only in terms of NCONF_{≥2}, R⁰_{≥2}, X_dir, X_big (and premise (Στ) for N_1); none
  is bounded here, on any class. (ii) VIS's kind-(a) term 2n(n − 1) is never exercised: no return after saturation occurs in either referee's
  data (EPC-N4 = N-EPC-5); REFEREE-2's "VIS without R⁰" control does not bite. (iii) Fallback-free returns are most returns (REFEREE-2: R⁰ 729 of
  its 1,340 returns, N-EPC-6; REFEREE: 124 of 155 at n ≤ 20, 272 of 370 at n ≤ 34): R⁰ is exactly the term left open. (iv) Over-budget
  configurations: REFEREE-2 1,102 (phases containing one skipped for EP-C / EP-ASM); REFEREE 144 UNK phases in its n ≤ 34 row; the n = 40
  lane instances were checked at depth cap 16, decided checks only. (v) Non-flat saturated fallbacks: REFEREE sees 5 of 236 (n ≤ 20) and 11 of
  178 (n ≤ 34) in its library, REFEREE-2 none in its library (0 of 43) but 25 of 25 on its named instances; the instance lists differ (DATA,
  fixes §5; both §Cs).
- Data (DATA, not proof): REFEREE (successor 15, own epc_probe.py, exact LEV_C for every configuration visited, with a path budget; lane code
  not run): 20,753 runs (the sum of its §6 rows, 20,752, and the nep76_n40 run of its addendum: the library at n ≤ 20 and n ≤ 34, 3,000 random games with ≤ 8 Odd choice vertices, rho3_253_n32 at 32 starts, and
  long121_n40, nep90_n40, nep76_n40 at depth cap 16); RET-FB checked at every later C-state for every configuration; 0 failures of every
  check; reproduces long121 (N_ep 37, NCONF 14), nep90 (90, 48), nep76 (76, 40); mutations MUT=1 (RET-FB + 2) 247 + 82 on long121, MUT=2 (RET-FB
  at non-C states) 251, MUT=3 (the DEAD guess) 1 + 7 failures. REFEREE-2 (successor 17, own epc_check.py with a deep mode; lane code not run):
  21,753 runs (named instances, lib41, its 503 𝒞^1O files, random games with 2, 4 and all Odd choice vertices); RET-FB 25,065 checks (10,200
  across configurations), its Even step 7,126, VIS on 1,340 returns, EP-C on 59,553 phases, SAT-FB / SAT-FB1 on 713 saturated fallbacks,
  Iσ_{t+1} = ∅ and "last state" at all 734 Ξ-flat fallbacks; 0 violations; same three reproductions; controls plus2 609, nonC 11,424, last
  21 failures, noR0 0 (does not bite).
- Signatures: REFEREE docs/referee/R-N5-EPC.md (referee a52feb43, data addendum 58fd9535, §C cd4795f8, successor 15): every item SIGNED, EP-ASM
  as an assembly with its second term as an implication, §5 DEAD CONFIRMED, no gap; FB-C′ stands without FBC-N3; notes EPC-N1..N4. REFEREE-2
  docs/referee-2/R2-N5-EPC.md (referee-2 62b72f6e, §C c4975512, successor 17): every item SIGN, EP-ASM likewise, DEAD CONFIRMED, no gap; the
  same answer on FB-C′; notes N-EPC-1..6. §C (both): verdicts identical; joint gap map empty; EPC-N4 = N-EPC-5; EPC-N3 compatible with N-EPC-6;
  N-EPC-1..4 accepted by REFEREE; EPC-N1..N4 accepted by REFEREE-2; the non-flat saturated fallback counts differ by instance list only;
  nothing open. Both under the standing premise 1E-N3 (P1) and RESULTS R70's Q-A.
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (per-phase reductions; no running-time bound). GAPS G-N5-TIME: open.

## Dead ends (kept; each with the exact obstruction or counterexample and the instance that killed it)
- DE1 (2026-10-14): arXiv 2511.03752 v1 (van der Heijden), claimed O(n²(n+m)) algorithm. BROKEN: wrong regions on 4-vertex games
  CE1 (l-comp 19b5ce2, experiments/m2/counterexamples/ce1_4v.pg) and cex1 (referee 936d47c, docs/referee/scratch/cex1-*.pg).
  Obstruction: Theorem 1/2 (A(G,d) is a dominion) is false; U^k refinement removes only vertices where the opponent can force A'.
  Details: docs/decisions/M2-arxiv-2511.03752.md.
- DE2 (2026-10-14): L-STRUCT target T1, w^X(n,d) ≥ s^X(n,d−2) for deterministic weak separators (docs/struct/S2-lower-bound-statement.md).
  REFUTED at n=2, d=10 in E, S, V: a 4-state weak (2,10)-separator (l-comp 3e44d2c, experiments/sat-hard/results/weak_E_n2_d10_k4.json)
  while s(2,8) = 5 (strong k=4 UNSAT, LRAT-verified, two solvers). Checked by REFEREE with independent tools (referee 92846bf).
  Obstruction: strong separators grow as s(2,2h) = h+1, weak ones stay at 4 for d = 8, 10. (Not algorithmic: 2-vertex games have d ≤ 3.)
- DE3 (2026-10-15): psolC (Huth-Kuo-Piterman, Imperial DTR15-4 Fig. 5 = LNCS 9560 chapter text) as a route to a complete solver.
  NOT COMPLETE: decides no vertex on the 4-vertex game psolc_min_n4_m6.pg (l-attr 02174e2, experiments/attr/instances/; colours 3,2,3,1,
  all vertices Even's, Odd wins all) and on tc from N=2 (22 vertices). REFEREE R-psolC (referee 1600917): implementation FAITHFUL; hand
  run from Defs 1-2 decides nothing under BOTH readings of ambiguity A1 (literal reading is the chapter's; Ex. 3 step (ii) is a slip).
  Obstruction: the weak-parity prefix minimum of Wr_p: a sub-trap the escaper loses, entered after a better colour of his parity, spoils
  the minimum for good (DTR p.11). Data (unrefereed): complete on all n ≤ 3 games and on 9 of 13 M1 families; 0% on tc, tc+,
  counter_symsi, counter_rr; three repairs dead (docs/attr/A3-psolC-results.md).
- DE4 (2026-10-15): L-SI candidate S2a MSF (most-significant-first single-switch strategy improvement, docs/si/candidates/S2.md
  at l-si 95d37d3) toward M4. KILLED by L-RED (l-red e1e9402; Gate Lemma stated in docs/red/R1-MSF.md at 7a7ed5e): on gated_bland N (experiments/red/gens_red.py;
  n = 5N+2, m = 9N+2; instances experiments/red/instances/gated_bland_N6.pg, _N8.pg), MSF from the best-reward start takes exactly
  2^N - 1 iterations (N = 2..13 on L-SI's si.py and L-RED's independent vj.py, both validated against brute force and Zielonka;
  vj.py to N = 15). Obstruction: a Friedmann simple-cycle gate (1106.0778 Lemma 6.1) sets each switch's level freely while Odd's
  current choice sets its sign and the exit its effect, so MSF on G'_N replays Bland's rule on the DLMM counter G_N (2512.16684
  Lemma 4.4). Class consequence (correspondence proof unrefereed): every single-switch rule ranking improving edges by the
  first-difference position inherits the index-based lower bounds (DLMM Thm 4.3 class). Also killed: S2b LSF, S3 steepest
  (DLMM M_L port), S4 (switchallexp); docs/si/DEAD.md.
- DE5 (2026-10-15): L-ALG candidates C1-C3 toward M4 (docs/alg/DEAD.md, l-alg e73ffad; single implementation each, data).
  C1/C2 nested fatal attractors NE(k), NE'(k): sound, polynomial for fixed k, incomplete for every fixed k; killer family S_s
  (experiments/alg/strfam.py, |S_s| = 3*2^(s-1)-2, S_2 = psolc_min_n4_m6): NE'(k) solves S_s iff k >= s-1 (measured s <= 4).
  Obstruction: required nesting depth = Strahler number - 1 = Lehtinen register number (DJT 2003.08627v2 Thm 8), up to log n.
  C3 ZP (Zielonka recursion with psolC pruning at every call): complete, but recursive calls 247 / 7,273 / 234,133 on tiled family
  T_R, R = 1/2/3 (n = 32/64/96; instances experiments/alg/instances/zp_tile8_R*.pg), ~30x per tile. Obstruction: psolC is blind on
  compositions of the Strahler-2 gadget at every recursion node, so the recursion is plain Zielonka.
- DE6 (2026-10-15): L-SI candidate S1 Random-Action-Removal = ORIGINAL Random-Facet (Zwick 2607.06334 Fig. 1), the fleet's M4-R
  candidate. NOT polynomial expected time: e^Omega(sqrt n) expected switches on sink parity games P_{n,r,s,t} of size
  Theta(n^{3/2} log^3 n), by FHZ arXiv 1410.7530 Thm 6.3 (black box, gap G-TL-1) plus L-RED's transfer lemma (l-red 0d50d4a,
  docs/red/R2-RAR.md; experiments/red/fhz.py, instances/fhz_*.pg). First referee REFEREE-2 R2-TL (referee-2 995cfd3): OK with fixes
  (F1: a missing two-line sub-case of case (2), verdicts agree; F2 remarks); independent exhaustive check 435,584 tests, 0
  disagreements. Not yet a result (second referee and L-LIT novelty check pending; FHZ errata 1410.7871: "It is not difficult to
  obtain similar examples for parity games", said of its cube examples).
- DE7 (2026-10-15): L-SI candidate S7 "most-improved" single-switch strategy improvement (docs/si/candidates/S7.md) toward M4.
  KILLED by L-RED (l-red bf0922f, docs/red/R5-S7-kill.md): family fhz_padded(n) = sink-parity encoding P_{n,1,1,1} of FHZ's
  one-player Random-Facet counter (arXiv 1410.7530 Fig. 3, R2 encoding) plus linear pads (W_x (n+1-i) dangling priority-0 Even
  vertices per level-i vertex, W = (3,4,3,1)); |V| = Theta(n^2) (64..632 for n = 2..9); S7 iterations 16, 44, 104, 228, 480, 988,
  2008, 4052, 8144 (n = 10; observed i(n) = 2 i(n-1) + 4n on every row; not proved), on L-SI's vjfast and L-RED's vj.py (n = 2..4), regions = Zielonka,
  strategies verified; instances experiments/red/instances/fhz_padded_n4.pg, _n6.pg. Obstruction: FHZ's level-i bit vertices take
  no traffic from other levels, so pads make S7's count order equal the counter's "lower level first" order, and resets pass
  through a quiet higher level (exact longest downstream-first runs on G_{n,1,1,1}: 5, 20, 53, 124, 269). Unrefereed measurement;
  a proof would need an FHZ-style phase analysis.
- DE8 (2026-10-15): L-SI candidates S2b LSF, S3 steepest and S4 (subgame-optimal start, then switch-all) toward M4
  (docs/si/DEAD.md, l-si 0d48da2; single implementation each, si.py/vjfast.cpp; unrefereed measurements).
  S2b KILLED by zadehexp (PGSolver port, n = 17N-6): 33, 89, 205, 441, 917, 1873, 3789 iterations at N = 2..8, 15301 at N = 10;
  instance experiments/si/instances/zadehexp_N5.pg (441, pinned); also DLMM 2512.16684 G_n (2^n-1) and the M_L port.
  S3 KILLED by the sink-parity port of DLMM 2512.16684 Lemma 5.4's MDP M_L (n = 3L+4): 4, 11, 26, ..., 2036 = 2^(L+1)-(L+2)
  at L = 2..10, the same run as LSF. Obstruction: the largest re-evaluated gain is the least significant switch (f = 1 case).
  S4 KILLED by switchallexp (Friedmann): 10, 30, 70, ..., 2486 at N = 1..8, identical to plain switch-all. Obstruction: an
  optimum of the subgame V minus Attr_Odd(top) restarts the counter at zero; it is not a surrogate for sigma*.
- DE9 (2026-10-16): proof-route potentials Φ and Φ_idx for the DTL polynomial bound (GAP-A, condition (H2b)); NOT a dead
  end for DTL itself (docs/alg/DEAD.md, l-alg 38f10e4; GAP-A-M.md §11b-§11e; unrefereed).
  Φ (global -1-record per vertex) KILLED by experiments/alg/instances/cross_h_k1_n11_m17_37.pg (n = 11, search 1, piece 0:
  the rescued vertex reaches death round 3, equal to its record from another -1 piece of the same search).
  Φ_idx (record per vertex and depth-0 piece index) KILLED by experiments/alg/instances/phi_idx_flat_n20.pg (n = 20; Oink
  5 iterations, verified; Dom(prevV) piece index 2, original ids: single driver t9 (top 5, pr 16, dead at round 2), a
  dead-top cap carry, rescues vertex 14 only back to its record from an earlier context, death rounds 6, 5, 5, 6; confirmed independently by L-RED, l-red 17db195) and by climbs_1016/nest_nest_s84.pg
  (redundant drivers t26-t28; vertex 30 death 6 -> 5 -> 6 across contexts). Obstruction: records from different contexts at
  one index are not comparable; Lemma F (the same-context raise) is proved and kept. Proved reduction kept: (H2b) carries at
  index i <= n(n+2)·c_i, c_i = distinct Dom(prevV) contexts at i.
- DE10 (2026-10-16): candidate per-context bounds for (H4) (deficit-triggered changes at one context, A_DTL) and three A_DTL
  extensions of C6 facts; NOT dead ends for DTL itself (docs/alg/GAP-A-M.md §13-§13h, §17 ledger, l-alg c18eaad; docs/red/R15-H4.md,
  R16; unrefereed). Each killed by an Oink-verified instance (Lead re-ran Oink on each):
  "-1 return set of A_DTL inside the ideal's" FALSE: experiments/red/carry/instances/h4_notweaker_n20.pg (actual {8,9} vs ideal
  {8}; only the per-round inclusion holds); Lemma S on A_DTL FALSE under deficits: lemmaS_viol_n20.pg (return set shrinks at
  equal M) and lemmaS_Mdrop_n20.pg (M 10->9); "<= 1 DEF change per context" FALSE: h4_def2ctx_n20.pg, then up to 11 at one
  ideal-stable context (experiments/alg/instances/h4_def11_oink_n28.pg); nested-chain-of-straddlers bound FALSE:
  h4_def8_oink_n44.pg (pairwise disjoint drivers, 20 crossing pairs); (C-rM) distinct (r0,M) FALSE at ideal -1 contexts
  (a_best_s32) and (C-rM-stable) FALSE at ideal-stable contexts: h4_def9_oink_n28.pg ((3,8) and (9,12) repeat).
  Obstruction: deficit changes run through the threshold phase over a growing, non-laminar tangle set; no per-context
  potential survives. Kept: Lemma R (regions lexicographic in T, A_DTL), per-round inclusion, Lemma S for C6 and for A_DTL
  under M-cond.

- DE11 (2026-10-16): further per-context (H4) candidates on A_DTL; NOT dead ends for DTL itself (docs/alg/GAP-A-M.md §18c-§18k,
  §17 ledger; docs/alg/DEAD.md; docs/red/R17-R20; unrefereed). Each killed by an Oink-verified instance, in both order data
  (Lead re-ran Oink on each): (LEX) per-context death vector lexicographically increasing FALSE:
  experiments/alg/instances/lex_viol_oink_n20.pg and experiments/red/carry/instances/lex_viol_inj_n28.pg; (NR) a fallen
  vertex never again the top changed vertex FALSE: lex_viol_inj_n28.pg; (CM) child M never drops across a parent DEF step
  into an ideal-stable child context FALSE: experiments/alg/instances/cm_viol_oink_n28.pg and
  experiments/red/carry/instances/cm_mdrop_both_n28.pg; (F1) at most one fall step per context FALSE:
  experiments/red/carry/instances/f1_twofall_n48.pg (one DEF and one LRN fall); (F1-DEF) at most one DEF fall step per
  context FALSE: experiments/red/carry/instances/f1_twodef_n48.pg (two DEF falls, disjoint components).
  Obstruction: a rising vertex or new tangle can steal a vertex of a straddling tangle into a higher region; the loss
  propagates over later rounds, and independent steal gadgets add fall steps at one context. Kept as DATA only:
  (U-MONO_DTL), (LEX-R), "no DEF-down step at an ideal-stable context"; PROVED on C6: Lemma P (GAP-A-M §20).
- DE12 (2026-10-17): proof-route candidates for GAP-A (per-phase search bound) and GAP-C (completeness) of A_DTL; NOT dead ends
  for DTL itself (docs/alg/GAP-A-M.md §21, §17; docs/alg/GAP-C.md §1-§17; docs/alg/DEAD.md box 5; docs/red/R22-R24; unrefereed).
  Each killed by an Oink-verified instance (Lead re-ran pinned Oink on each): 13+ per-phase potentials (tangle-vertex union, tops,
  incidences, PSI1-3, settled labels, PHI0 and others; GAP-A-M §21d); (ABS-mono) and (ABS-mono-pw): experiments/red/carry/instances/
  absmono_viol_n44.pg; NODUP / (NO-ORPHAN): gapb_dup_n20.pg (duplicate-check hit, also printed by release Oink -t; search with
  W_p empty); (NO-ORPHAN-W): gapbW_dup_n20.pg (duplicate inside W_p); (S2) "dominion context never pruned to -1": spp_final_n20.pg;
  (K-first), (K4-B): experiments/alg/instances/kfirst_viol_union.pg; (FIRST-W): firstw_viol_cross.pg; (PEEL), (Cb1):
  c1_k1_min_n7_m10. In every instance the run is COMPLETE and CORRECT. Obstruction: no rule that names the productive piece of a
  search, and no per-phase potential, survives; the remaining statements are DATA only: (SPP) searches per phase <= |G'| (tight,
  chain family spp_chain_up_n43) and, for GAP-C, the existential (K-low) plus (TW), with the open step the Dom(prevV) removal
  (dtl.cpp 962-991). Kept as PROVED readings (unrefereed): phases <= D+2, First-Difference Lemma, DV*-MONO, per-context LRN budget,
  SCC1, B-thr, O0/O1, OPP-EXIT, Theorem A (root case, up to alpha).
- DE13 (2026-10-17): GAP-C data statements (K-in), (K-low)/(LOW-W), (TW), (S-LOW) in the TIGHT form, and (KT-STEP-first) at an S
  piece are FALSE on A_DTL in both order data; NOT a dead end for DTL itself (the run is complete and correct). Instance:
  experiments/red/carry/instances/kin_viol_n29.pg (n = 29, sha1 50987098; L-RED R29, docs/red/R29-kin.md, l-red 2455159; found by
  the interacting-union sampler). Lead re-ran pinned Oink: 2 dominions, 15 tangles, 8 iterations, solution verified (13
  strategies); L-ALG's unmodified dtl_kin.py and dtl_loww.py print one VIOLATION each in both orders; carry/slow.py: loose 0,
  tight 1 in both orders. Obstruction: search 0 (Even, |W_0(G')| = 9, no dominion) has one depth-0 stable MIX piece whose tops
  include W_0 vertices; it removes all of W_0 and learns only tangles outside W_0 and one tangle STRADDLING W_0 (3 W_0 vertices,
  6 opponent-won); nothing is learned inside W_0. Search 1 learns inside W_0 at depth 1 and search 2 finds the dominion.
  Consequence: Lemma K in its plain form (search(p) learns or finds a dominion when W_p(G') is nonempty) is not refuted, but every
  route that requires the learning to be INSIDE W_p in the same search is dead. RESULTS R4 (depth-0 P pieces) and R5 are unaffected.
- DE14 (2026-10-17): GAP-A root-call pruning monotonicity (RMONO: the root call's pruning rounds never fall across consecutive
  searches s -> s+1 of a phase) is FALSE on A_DTL in both order data; it is the box-4 claim (M) at the root context. NOT a dead
  end for DTL itself. Instance: experiments/alg/instances/dtl_mviol_n20.pg (L-ALG, GAP-A-M §22, l-alg 9372231). Lead re-ran
  pinned Oink (6 iterations, verified), dtl_mviol_check.py ("M-VIOLATION REPRODUCED"; Oink -t -t first-call distances of orig16,
  orig1 fall 8 -> 7 and orig19 9 -> 8) and dtl_rootmono.py (RMONO FAILS in the root threshold loop, both orders). Corpus: 18
  failures per order out of 863 / 842 root-call transitions, every one with a root deficit round (U != Û). Obstruction: Lemma E
  (a straddling stored tangle's unconsumed rest is re-absorbed by a lower surviving top). Surviving DATA candidates (GAP-A-M §22):
  (RV-ND), (PSI-MONO), (POS-FALL) on deficit-free root calls.
- DE15 (2026-10-17): GAP-C statement (MEET) "search(p) learns a tangle meeting D = W_p(G') or finds a dominion" (GAP-C §18r, the
  last local single-search progress statement after DE13) is FALSE on A_DTL in both order data; NOT a dead end for DTL itself
  (the run is complete and correct). Instance: experiments/red/carry/instances/meet_viol_n17.pg (n = 17, sha1 ab329297; L-RED
  R30, docs/red/R30-meet.md, l-red 06cd9f8; shrunk from a climb seeded at kin_viol_n29). Lead re-ran pinned Oink (--dtl: 2
  dominions, 4 tangles, 6 iterations, verified; --zlk verified) and L-ALG's unmodified dtl_meetd.py in both orders: "(MEET)
  FAILS search 0 p=0 |G'|=17 |D|=7 new=[[7, 10, 11, 14]]", (K) holds 5/5, (PHASE-IN) holds 5/5. Obstruction: in search 0 a T
  piece removes a D vertex (cutting an Odd escape), then one S piece Even-attracts the rest of D into the closed region of a top
  whose core cycle lies in W_1, and only that core is learned; searches 1-3 then learn inside D and find the dominion.
  Consequence: no statement of the form "each search makes progress toward D" survives; with (PHASE-IN) equivalent to phase
  completeness (run() dtl.cpp 1106-1121, search() 1068), a completeness proof needs a cross-search progress measure.
- DE16 (2026-10-17): GAP-A route (CHAIN) "the first-difference contexts of a phase form a ⊆-chain" (which would give at most n+1
  first-difference contexts per depth, i.e. (CTX)) is FALSE on A_DTL in both order data; NOT a dead end for DTL itself. L-ALG
  GAP-A-M §22k (l-alg 5b48b91): fails in 13 of 49 phases (Oink) and 12 of 50 (stable); smallest instance
  experiments/alg/instances/dtl_searches15_n24.pg (Oink order; first-difference context sizes 14, 16, 24), both orders on
  nest_nest_s43. Lead re-ran pinned Oink on dtl_searches15_n24 (16 iterations, verified) and dtl_rootmono.py ("CHAIN FAILS").
  (CTX) itself is not refuted: at most 10 first-difference contexts per phase on the SPP families (spp25_oink_n40, |G'| = 38).
- DE17 (2026-10-17): GAP-A route (CTX-ROOT) "distinct first-difference contexts per phase ≤ 1 + number of root-call
  transitions" (which would reduce (CTX⁺)'s best_vertices part to the root call, bounded by RESULTS R7) is FALSE on A_DTL; NOT
  a dead end for DTL itself. L-ALG GAP-A-M §22o (l-alg e225fc4): fails in 5 of 261 corpus phases; smallest instance
  experiments/alg/instances/dtl_cnew14_n20.pg (Oink order; 3 contexts with 1 root transition, context sequence 3 1 5). Lead
  re-ran pinned Oink (9 iterations, verified) and dtl_rootmono.py ("CTX-ROOT FAILS ... contexts 3 root transitions 1").
  Obstruction: deeper contexts change inside blocks where the root call is frozen.
- DE18 (2026-10-17): GAP-A route (FALL-V) "each vertex's RV at a fixed context falls at most once per phase" (which would give
  F_R ≤ n and GAP-A ⇐ (CTX⁺) alone) is FALSE on A_DTL in both order data; NOT a dead end for DTL itself. Instance
  experiments/red/carry/instances/fallv_viol_n28.pg (n = 28, sha1 21b235f4; L-RED, climbed from lex_viol_inj_n28). Lead re-ran
  pinned Oink (7 iterations, verified) and dtl_rootmono.py: vertex 14 (priority 27) at the root context has RV 4, 6, 5, 4, 4
  over the phase's 5 searches (rise, then two falls; "RMONO FAILS ... round 3 vertex 14 pr 27 round 5 -> 4"); 8 (context,
  vertex) pairs fall twice; L-ALG re-ran too (GAP-A-M §22q, DEAD.md ce7cca6). Obstruction: a new tangle raises the RV, then two
  later steals lower it. Surviving charge (unrefereed, GAP-A-M §22r): every descent coincides with a new steal (17/17 here).
- DE19 (2026-10-17): GAP-A route (STEALER-MONO) "the region holding a relevant steal's stealing vertices never loses a vertex
  later in the phase" (an ORDER on relevant steals, proposed as a route to (STEAL-ONCE*), GAP-A-M §23a; DATA 216/216 Oink order)
  is FALSE on A_DTL under the stable order datum (L22/L26: the statement covers every order datum); NOT a dead end for DTL
  itself, nor for (STEAL-ONCE*). Instance experiments/red/carry/instances/stealer_viol_n76.pg (n = 76, sha1 714ecc0f; L-RED R34,
  l-red 549f8de, climbed from fall3_n76 with ROOTFIT=stealer). Lead re-ran pinned Oink (7 iterations, solution verified, 33 strategies)
  and the unmodified dtl_rootmono.py (unchanged since l-alg e2f7e198; RM_EXCL=1 RM_PREF=1 RM_DV=0): stable order
  "STEALER-MONO ...: FAILS" 3, holds 14; Oink order holds 1/1; run complete. Obstruction: a stealing region later loses
  vertices (shape being traced by L-ALG). Surviving on the same instance, both orders: STOLEN-PERM 17/17, (STAYS-MET)
  "NO-REFIRE after a relevant steal: never refires | stays met" 17/17, (STEAL-ONCE*) "RELEVANT STEALS per (context, round,
  top, tangle): max 1"; (MET-MONO) fails 8 times (already false).
- DE20 (2026-10-17): GAP-A hypothesis (STEAL-ONCE*) of RESULTS R11 (d) "each (context, round, top, fired tangle) is a relevant
  steal at most once per phase", and L-ALG's route to it (STOLEN-PERM) ⇒ (STAYS-MET) ⇒ (NO-REFIRE) ⇒ (STEAL-ONCE*) (GAP-A-M
  §23b), are FALSE on A_DTL under the stable order datum (L22/L26); NOT a dead end for DTL itself. Instance
  experiments/red/carry/instances/stealonce_viol_n76.pg (n = 76, sha1 32c2da0b; L-RED R35, l-red 6af3a14; stealer_viol_n76 with
  edge 3→31 replaced by 3→64 and edge 20→31 added). Lead re-ran pinned Oink (1 dominion, 50 tangles, 7 iterations, solution
  verified, 33 strategies) and L-ALG's unmodified tools: dtl_rootmono.py (unchanged since l-alg e2f7e198; RM_EXCL=1 RM_PREF=1
  RM_DV=0), stable order: "STOLEN-PERM ...: FAILS" 7 / holds 12, "NO-REFIRE ...: REFIRES later | prefix later unmeets t" 7,
  "RELEVANT STEALS per (context, round, top, tangle): max 2", no INCOMPLETE; dtl_stealtrace.py (l-alg 7b909b6; RM_EXCL=1
  RM_PREF=1 RM_LIGHT=1 RM_DV=0), stable: "STEAL-ONCE* VIOLATION ... phase 1 ctx |R| 76 step (round 4, top 18) tangle 7: 2
  relevant steals", STAYS-MET FAILS 7; Oink order: everything holds. Obstruction (L-RED R35): vertex 3 of fired tangle 7 joins
  higher region 66 via 3→64 (first relevant steal); a new top 68 relevantly steals region 66's tangle, region 66 shrinks, 64
  leaves every region above 18, so 3 leaves the prefix and tangle 7 refires; later region 66 fires a new tangle, holds 3 again,
  and steals tangle 7 a second time (L-ALG's dependency case A, one level up). No growth shown (k = 2).
  ADDENDUM (2026-10-17 21:53Z by date -u): the same four statements also FAIL under the Oink order datum (the shipped solver's order),
  so this dead end does not depend on L22/L26: experiments/red/carry/instances/stealonce_both_n45.pg (n = 45, 70 edges, sha1
  ee52c4a3; L-RED R36 §5, l-red 3256056; obtained from stealonce_core_n76 by vertex deletion). Lead re-ran pinned Oink (2
  dominions, 17 tangles, 6 iterations, verified, 13 strategies) and the unmodified dtl_rootmono.py (at l-alg 2ff12ff; RM_EXCL=1 RM_PREF=1
  RM_DV=0) and dtl_stealtrace.py (+RM_LIGHT=1), identical in BOTH orders: STOLEN-PERM FAILS 2 / holds 4, NO-REFIRE "REFIRES
  later" 2, relevant steals per quadruple max 2, no INCOMPLETE; "STEAL-ONCE* VIOLATION ... phase 2 ctx |R| 43 step (round 5,
  top 12) tangle 0: 2 relevant steals" (and at round 6). Depth still 1.
- DE21 (2026-10-18): the DATA hypotheses (STEAL-DEPTH_D) for D ≤ 3 (RESULTS R12 (c)) and (EXIT_2) (RESULTS R13 (c)) are
  FALSE on A_DTL in BOTH order data; re-steal depth GROWS along a constructed sequence; NOT a dead end for DTL itself (iterations
  stay linear), and [superseded by ADDENDUM and ADDENDUM 2 below] NOT yet a refutation of (STEAL-DEPTH_D) or (EXIT_c) for every constant (that needs a uniform family; the
  control wiring is hill-climbed per D). Instances experiments/red/lag/instances/depth2_n39.pg (sha1 6200e586),
  depth3_n46.pg (54cc8526), depth4_n53.pg (40dacf0e) (L-RED R39, l-red 9cd2702; an inversion relay driven by a region
  clock, n = 7D + 25). Lead re-ran (03:07Z by date -u) pinned Oink (10/11/12 iterations, verified, 28/33/38 strategies)
  and L-ALG's unmodified dtl_stealdepth.py (unchanged since l-alg e0fc1bb; RM_EXCL=1 RM_PREF=1 RM_LIGHT=1 RM_DV=0): max
  depth 2/3/4 and max k 2/2/3, identical in both orders; and dtl_prefexits.py (same flags): max exits per (context, step,
  vertex) 2/2/3 in both orders (3 on depth4_n53, |R| 53, 11 visits), total exits per context / |R| 0.64 / 1.13 / 1.79.
  Obstruction (L-RED R39): a staggered freeze clock (top level first, one level per search) plus holds whose release reaches
  the levels below drives a relay F_j(x) = not(F_(j-1)(x) or x ≥ j+3); each level's re-steal is caused by the level above.
  Consequence: the R12 (c) route with D ≤ 3 and the R13 (c) route with c = 2 are dead on data; depth grows along the R39
  sequence (no uniform family yet [superseded: see ADDENDUM]); R12 (a) (STEAL-POLY_sum),
  R13 (b) (EXITS-POLY) and R14 are untouched (k ≤ 3, totals small).
  ADDENDUM (2026-10-18 03:22Z by date -u): UNIFORM FAMILY. experiments/red/lag/lagfam.py D (L-RED R39 §5, l-red a0eb07a; one fixed
  wiring rule T_j → {x_1, τ_j}, no climbed helpers) builds a game on n = 7D + 22 vertices. Lead regenerated D = 4, 8, 12
  byte-identical to the pinned fam_D4_n50 (c8fd8616), fam_D8_n78 (46ad828c), fam_D12_n106 (0dd2899e), and ran D = 2, 3, 4,
  5, 6, 8, 10, 12: pinned Oink D + 8 iterations, verified, every D; unmodified dtl_stealdepth.py (RM_EXCL=1 RM_PREF=1
  RM_LIGHT=1 RM_DV=0), identical in both orders: max depth = D and max k = ⌊(D+1)/2⌋ + 1 (2,3,3,4,4,5,6,7). Hence
  (STEAL-DEPTH_D) is FALSE for EVERY constant D (on this family, at D > the constant), and re-steals per quadruple are
  unbounded (they grow linearly in n); RESULTS R12 (c) carries a POST-LANDING NOTE. Still NOT refuted: (STEAL-POLY_sum), (EXITS-POLY) / (EXIT_c) for
  c ≥ 3 (exits on the family not yet measured [superseded: ADDENDUM 2 refutes (EXIT_c) for every constant c]), (CTX⁺), (FIRED⁺-R), GAP-A (iterations D + 8, linear).
  ADDENDUM 2 (2026-10-18 03:27Z by date -u): (EXIT_c) FALSE for EVERY constant c on the same family (L-RED R39 §7, l-red 702e2e9). Lead
  ran the unmodified dtl_prefexits.py (same flags) on lagfam D = 2, 4, 6, 8, 12, identical in both orders: max exits per
  (context, step, vertex) 2/3/4/5/7 (= ⌈D/2⌉ + 1, odd D per REFEREE-2 below); total exits per context 25/75/166/310/805 (|R| 36/50/64/78/106), polynomial on
  these data. First break at c = 3: fam_D4_n50. RESULTS R13 (c) carries a POST-LANDING NOTE. dtl_rootmono (L-RED): one
  first-difference context per phase on the family, so it says nothing about (CTX⁺).
  FAITHFULNESS (2026-10-18 03:47Z by date -u): REFEREE-2 docs/referee-2/R2-FAITH-lagfam.md (referee-2 636697c, "(Opus 5.5, D12)") re-measured
  lagfam D = 2..8 with its own logging-only pinned-C++ build and own checkers (an9, an10; no L-ALG tools, no pyref), pinned and
  stable order: D + 8 iterations verified; max depth = D, max k = ⌊(D+1)/2⌋ + 1, every re-steal with a CHARGE cause; max exits per
  (σ, w) on the fixed grid = ⌈D/2⌉ + 1; 0 failures of CHARGE, ENTRY-CHARGE steps 1-3, N* ≤ N_ent, C3 and fan-out. Its exit TOTALS
  (64/177/376/685 at D = 2/4/6/8) count virtual rounds on the fixed grid and are ≈ 2.2-2.6× dtl_prefexits'; both polynomial.
  DE21 and its addenda therefore stand on a faithful implementation.
  ADDENDUM 3 (2026-10-18, fixed d): the DE21 kills hold at d = 3. Source: L-ALG succ. 9, docs/alg/GAP-A-M.md §26a-§26d, l-alg
  9b86244. lagflat7(D) := lagfam(D) with ids renumbered by (original priority, id), then priority classes merged to {0, 1, 2}
  (experiments/alg/fixd_lagcollapse.py D flat7). Instances experiments/alg/instances/lagflat7_d3_D{4,8,16}.pg (sha1 45de9d933756,
  60f2df733ffa, 67b2d56b32c6).
  - Lead re-run (2026-10-18 ~10:10Z, detached checkout of l-alg 9b86244, pinned Oink @ 8fbf0a7, unmodified dtl_stealdepth.py with
    RM_EXCL=1 RM_PREF=1 RM_LIGHT=1 RM_DV=0): regeneration of D = 8 byte-identical; Oink `--dtl --no-single --no-wcwc --no-loops`
    12 / 15 / 23 searches (even 11/14/22, odd 1) at D = 4 / 8 / 16, solution verified (37/57/97 strategies), winners equal to
    `--zlk`; re-steal depth STABLE order 4 / 8 / 16 (max k 3 / 5 / 9); OINK order 4 / 0 / 0 (max k 3 / 0 / 0).
  - Consequence: under L26 (a failure under either order datum refutes a statement about A_DTL) the stable order alone makes
    (STEAL-DEPTH_{f(d)}) false for every function f, already at d = 3; by L-ALG's measurement the same holds for (EXIT_{f(d)})
    (max exits D/2 + 1; CHECKER C16 re-ran D = 4, 8: 3, 5). Fixing d bounds the call depth of A_DTL (DTL-proof §3(c)) but none of the
    per-context constants. In the Oink order the depth collapses (to 0 at D = 8 and 16 in the re-runs; L-ALG saw the drop from D = 6 on) because std::sort is unstable on large
    equal-priority classes (the §21b effect); an Oink-order-robust variant is open (routed to L-RED).
  - Not a running-time kill: searches grow linearly in D; every total stays polynomial, as for lagfam.
  - (rev. 10:32Z) All-distinct priorities as well (L-ALG succ. 9, GAP-A-M §27a, l-alg 6266da9): lagdist(D) := lagfam(D) with
    priorities refined to pairwise distinct (order and parity kept, ties broken by id); instances
    experiments/alg/instances/lagdist_D4.pg (af9b429696a0), _D8 (215e9ce202dd), _D12 (66855da1a880). With no ties the stable and
    Oink orders coincide. Lead re-run (detached l-alg 6266da9): Oink 12 / 16 searches at D = 4 / 8, verified (37/57
    strategies), winners equal to `--zlk`; unmodified dtl_stealdepth.py re-steal depth 4 / 8 (max k 3 / 5) in BOTH orders. So
    (STEAL-DEPTH_c) is false in both order data on games with all-distinct priorities; the relay needs only a total order of
    the region tops. D = 12 not re-run by the Lead.
- DE22 (2026-10-18): L-NEW candidate N1 = Loff-Skomra IncreasingDiscountPI (arXiv 2402.03975 Fig. 12; 2610.22149 §7.4,
  Fig. 7.2) on parity-induced rewards ±n^pr, Howard switch-all for the switching player, warm starts, γ_j = 1 − 2^−j (L-NEW
  docs/new/N1-disc-anneal.md; implementation experiments/new/anneal.cpp / anneal.py, cross-checked on 1,000 games). Passed
  gauntlet step 2 on data (13 M1 families + 12,000 random games; owner told 17:58Z), then KILLED on data (owner told 18:12Z).
  Obstruction: deep traps. At every Even vertex with ≥ 2 successors add v → t_v (Odd, even priority P = B + 2 + 2k) → c_v (Odd
  self-loop, odd priority q = B + 1), k = ⌊B/2⌋ + 2, so P − q > B + 2 (experiments/new/gen_deeptrap.sh N = pgsolver_port
  switchallexp(N) + alltrap.py; regions unchanged, Odd wins all). The all-traps strategy stays discounted-optimal until a
  release phase beyond Friedmann's β_G = 1 − 1/(4|V|³ max|r|) (1106.0778 p.35); that one phase is switch-all from the
  best-reward start and replays Friedmann's counter (1106.0778 §9).
  Instances: experiments/new/instances/killer/deeptrap_sae_N1..N7.pg (claude/l-new 8ac5e5c; N7 sha1 835ce1326ca3…, n = 239).
  Even switch-all rounds in ONE phase: 11, 31, 71, 151, 311, 631, 1244 at N = 1..7 (n = 32N + 15); 5·2^(N+1) − 9 fits N = 1..6
  only (N = 7: 1244). Lead re-run (detached l-new 8ac5e5c, anneal.cpp unmodified): N = 1..6 exact, sha1 = pins, regions = Oink
  zlk. Robust (L-NEW f301bfb): start γ (--j0 1/100/400/700) and Odd's rule (--odd-howard) give the same 311 at N = 5;
  the priority-compression variant N1m dies once priorities are padded (pad_prio.py).
  Faithfulness: REFEREE-2 docs/referee-2/R2-N1-FAITH.md (referee-2 520d701), FAITHFUL WITH CAVEATS (Opus 5.5, D12):
  (C1) anneal.cpp swaps the players' roles relative to 2402.03975's DiscPI figure (Odd best-responds, Even switches) — LS on
  the negated game, allowed by 2610.22149 §7.4, where DiscPI(σ,τ,γ) is any procedure that outputs a pair of optimal policies (REFEREE-2's reading of the opened text); in LS's literal orientation G_N is easy, and the kill
  transfers by duality: LS-literal on dual(G_N) gives 11, 31, 71, 151, 311 outer switch-alls in one phase (N = 1..5, regions
  verified). So IncreasingDiscountPI with Howard is exponential in both orientations (G_N resp. dual(G_N)).
  (C2) The general claim "the parity-certificate stop fires no later than LS's mean-payoff-optimality test" (N1-KILL.md) is not proved and can fail; it is not needed: on G_N
  the all-traps strategy is never mean-payoff optimal, so LS cannot stop before the release phase.
  (C3) the closed form is a fit for N ≤ 6 only (above).
  Literature (L-LIT T19, l-lit 8d8da04): not found in any opened source; a theorem form needs two lemmas (GAPS G-N1-LB,
  optional). DATA kill, not a theorem.
- DE23 (2026-10-18): L-NEW candidate N2 = priority annealing with warm-started Vöge-Jurdziński switch-all (coarse games G_t,
  priorities below q_t set to 0; docs/new/N2-prio-anneal.md; experiments/new/n2.py + n2_si.cpp). Obstruction: block priority
  merging with one isolated self-loop dummy per priority (experiments/new/gen_padsae.sh N = switchallexp + pad_prio.py); the
  stage that reveals the low priorities replays Friedmann's counter from the coarse optimum. Instances:
  experiments/new/instances/killer/padsae_N1..N7.pg (claude/l-new f301bfb; N7 sha1 9ee0385509ac…, n = 230). Largest single
  stage 6, 15, 34, 72, 148, 300, 604 switch-all iterations at N = 1..7. Lead re-run (detached l-new f301bfb, unmodified):
  N = 3..6 give 34, 72, 148, 300 (stage counts 61/77/93/109), sha1 = pins, regions = Oink zlk. Single implementation, DATA.
- DE24 (2026-10-18): five DATA hypotheses toward GAP-A (A_DTL = `oink --dtl --no-single --no-wcwc --no-loops` @ 8fbf0a7) are
  FALSE, each in BOTH order data (L22/L26), each found by L-RED successor 9 (box 14) with graded climbs and checked with L-ALG's
  UNMODIFIED tools; each re-run by the Lead (tools at the cited l-alg commit, detached worktree; pinned Oink verified, regions =
  Oink zlk); L-ALG (author) confirmed that the tools for (a), (b) and the (VR-NEW_all) part of (c) compute the statements as written (GAP-A-M §37, docs/alg/DEAD.md, l-alg ad6cd54 +
  e35b0f2). None is a refereed result; R4-R14 are unaffected. 𝒞^1P = 𝒞_0^dist ∪ 𝒞_1^dist: every vertex of the opponent
  q = 1 − C has exactly one successor, and q's priorities are pairwise distinct (GAP-A-M §27b; the instances here have all
  priorities distinct).
  (a) (XCTX@p0) (GAP-A-M §35a, the hypothesis of §33's 𝒞^1P reduction "GAP-A ⇐ (XCTX@p0) ∧ (CHAIN-CHANGE)"): FALSE on
      𝒞^1P. Instance experiments/red/xctx/instances/xctx_viol_n20.pg (sha1 742ba103cdb77cbb20e8d94e99120331568e84cd; n = 20;
      pinned Oink 6 iterations). Even phase, s2 → s3, p0 = 2: N = {12} is covered by piece_{p0}(s0) at the different context
      G′ \ {13,19,18} (same size 17, same signature (3, 17, 4)). b12_core.py @ l-alg 9ab9a3e, CLASS=1 DIST=1: MODE=xcover max
      covered fraction 1.0 at ((0,0),2,2); MODE=core "CORE-ALL violations 1". docs/red/R42-xctx.md §1 (l-red 8f09538).
  (b) (TREE-PIECE⁺) (GAP-A-M §36a: at every consecutive pair of searches whose call sequences differ, some vertex holds a key
      (v, depth, position, ρ, |R|, |V|) it held at no earlier search of the phase): FALSE in two-player games. Instances
      experiments/red/tpp/instances/tpp_viol_n22.pg (sha1 a5088b091cbddad1b62233335649b8088b7d1089; pinned Oink 5 iterations)
      and tpp_viol_n63.pg (sha1 64d0832859a415f8bda8959f35e55bc9520425d9; 8 iterations). b12_ident.py @ l-alg 5eb1b4b: TREE=1
      "without a new key 1"; tp_score with PLUS=1: n22 (1, 0, 3, 5), n63 (1, 0, 6, 8). Obstruction: at depth 1 the key does not
      determine the call's input (R, X); a different parent subgame X repeats the key. Adding X to the key reintroduces (CTX⁺).
      Cannot occur on 𝒞^1P (L-RED Lemma EMPTY-REC, a reading). docs/red/R43-treepiece.md (l-red 313aaae).
  (c) (VR-NEW_all) (GAP-A-M §32-§33a: every chain-changing transition gives some vertex a new full key (v, ρ_j, j, |R_j|, |V_j|))
      and (FD-WITNESS_all) (a new-key vertex in the piece at j* or j* − 1): FALSE on 𝒞^1P and in general. Instance
      experiments/red/xctx/instances/vrall_viol_n20.pg (sha1 ed50585765541988d42aa4fa2b3d97c0b3bb8401; 𝒞^1P; pinned Oink 5
      iterations). b12_pot.py @ l-alg 5eb1b4b (with and without CLASS=1 DIST=1): "K-v-all violations 1"; b12_fdwit.py: no
      new-key vertex at j* nor at j* − 1 for K-v-rV, K-v-rs, K-v-all; b12_core xcover fraction 1.0. Obstruction: a depth-0
      cross-context cover with nothing new below p0. docs/red/R42-xctx.md §5 (l-red 8a81ce9).
  (d) (NO-PRE-a) (GAP-A-M §28c: "a vertex of a tangle that fired at top τ in round r is never a round-r top above τ at the next
      visit"): FALSE (two-player, tied priorities). Instance experiments/red/nopre/instances/nopre_viol_n20.pg (sha1
      9a93a8e24832a2440206658fc0f4fdca63cb1574; pinned Oink 4 iterations). b12_nopre.py @ l-alg 5eb1b4b scan: "PRECONDITION",
      (pre, near, surv, gap, above) stable (1, 2, 6, 4, 6), oink (1, 1, 5, 4, 5). Found by L-ALG's own climb (b12_nopre.py climb,
      seed 51) from L-ALG's near miss nopre_near_n20. NOSTEAL-1P (distinct q-priorities) untouched. docs/red/R44-nopre-and-growth.md.
  Consequence: every known key-based (local no-repetition) route to GAP-A on 𝒞^1P is closed (R44 §3; GAP-A-M §37;
  docs/alg/DEAD.md); in general games the key statements tried so far ((TREE-PIECE⁺), (VR-NEW_V), (VR-NEW_s), (VR-NEW_all))
  and (NO-PRE-a) are false too. Surviving DATA among the statements attacked in box 14 (R44 §1): (CHAIN-CHANGE) on 𝒞^1P,
  which cannot give super-polynomial growth even if false (R44 §3, a reading); also still open: (TOP-CHAIN@R) on 𝒞^1P
  (GAP-A-STATUS §4) and the R14 hypotheses (CTX⁺), (FIRED⁺-R). These are "proof route dead" results, not lower-bound steps (R44 §3): each counterexample repeats a label
  once in a phase of 3-6 searches; NEST ≤ 2 on these instances; the open question is the global (CTX⁺) count. Pinned in
  experiments/red/check.sh: sha1 of all five instances; checker outputs in both orders except b12_fdwit (unpinned) and
  tpp_viol_n63 (sha1 only).
- DE25 (2026-10-22): N6 = path-following interior-point method on the Jurdziński-Savani P-matrix LCP of the discounted game obtained
  from a parity game (L-NEW successor 5, (c) lane under D14/D15; docs/new/N6-ipm.md §1-§8, l-new c0e8b57 + addendum 8ace011) is a DEAD
  END. (a) Proof route dead at the screen (sources opened by L-NEW; HIJ re-opened by L-LIT T24, docs/lit/T24-HIJ-barrier.md, BARRIERS
  B21): Hansen & Ibsen-Jensen arXiv 1304.1888 Thm 19 / Thm 21, κ = Θ(n/(1−γ)²) for these LCPs (lower bound on the arena G_n, M
  independent of the costs); Friedmann arXiv 1106.0778 §9: at β_G, 1/(1−γ) = 4n^{d+3}, so every κ-based IPM bound at that discount is
  n^Θ(d) (L-LIT / L-NEW reading, T24 §2, BARRIERS B21; no opened source gives a polynomial 1/(1−γ) that works for all parity games);
  and, by HMZ arXiv 1008.0530 Thm 6.5 (reading, T24), whenever such a bound is polynomial, strategy iteration is already polynomial. ABGJ arXiv 1708.01544 Thm B
  (Cor. 31) does not transfer as stated (LPs, doubly exponential data). (b) Gauntlet step 2 fails on data for the implementation
  experiments/new/ipm/n6.py in its default central mode (target-following, adaptive long step, fraction-to-boundary Newton, precision 8×bits): no answer on 7 of
  13 hard families at small N (tc N=4, tc+ N=2, counter_ortl N=3, counter_symsi N=1, counter_rob N=2, counter_core N=4, counter_dp N=8)
  and on 6 of the 8 random games with n ≥ 23 (n = 25-30; n = 23, 24 answered correctly after a centring failure; 10 of 40
  random games without a solution; gen.py, seeds 20261023-62); the weighted mode fails on tc, tc+, counter_ortl, counter_symsi and
  counter_rob from N ≤ 3 (N6 §7); every produced answer correct (check_sol2.py against Oink zlk).
  Obstruction instance experiments/new/instances/n6/counter_ortl-3.pg (sha1 c8bc349942b32305edee56ba8fb7d6504ed86622, n = 16): M
  certified P (all 262,143 principal minors positive, arb); the path is lost at μ = 3.19e-26 under every setting tried (HIJ's κ scale n/(1−γ)² ≈ 1e43: a
  neighbourhood on the products w_i z_i no longer pins the coordinates). Lead re-run (2026-10-22 08:20Z, trunk, python-flint):
  "stalled/c141/mu36, 3.1911607757279757e-26", no solution, identical to results/counter_ortl.central.csv. The step-2 failure is
  non-convergence of this implementation, not an incorrect answer; the generic method is killed by (a). Open and not claimed: the
  iteration count of a convergent IPM on these LCPs (HIJ §1.1).
- DE26 (2026-10-22): N7 = entropic temperature homotopy (soft log-sum-exp Bellman operator on the parity-induced discounted game at
  γ = β_G, temperature τ → 0, Newton / soft policy iteration; docs/new/N7-entropic.md, l-new 9d8846f) is a DEAD END. (a) Screen:
  known entropy-regularised rates are poly(1/(1−γ), 1/τ) (Cen et al. arXiv 2007.06558 Thm 1; Cen-Wei arXiv 2105.15186 Thm 3); both
  factors are exponential for parity (1/(1−γ) = n^Θ(d); τ below action gaps 2^−O(n d log n)); HMZ Thm 6.5 as in DE25. (b) Data
  (experiments/new/ipm/n7.py, results/*.n7.csv): stalls mid-path on counter_ortl N=3 (same instance as DE25; τ ≈ 2.83e-7) and tc+
  N=2; start-phase failures on tc N=4, counter_symsi N=1-2, counter_rob N=2; every produced answer correct. Lead re-run on
  counter_ortl-3 (08:22Z): no solution, τ = 2.8349e-07 at the 3,000-iteration cap (lane: 3,213 iterations, "stalled/tau38", same τ;
  CHECKER C21 with --maxit 20000 reproduced the lane row to every digit).
  Screen rule recorded by the lane (N7 §4): every method that works on the parity → discounted reduction and whose analysis is
  polynomial in 1/(1−γ) is no better than strategy iteration (HMZ Thm 6.5); such a candidate needs a γ-free argument before any bench.
- DE27 (2026-10-22): the k-pools attack on (NEST*-BOUNDED) (GAPS G-NEST; RESULTS R16) is CLOSED without a family (L-RED boxes 16-19,
  docs/red/R49-nest4-attempt.md, R50-kpools.md, R51-piecemap.md; l-red e1c3f2b, b575ae7, 4f73e7a, c6ac001). DATA: class best NEST* on
  𝒞^1P went 3 → 6 (nest4u_n46 ae7ed559 and nest4uu_n51 302c03a8 NEST* 4, nest5_n49 fe50a2c9 NEST* 5, nest6_n75 dc8b04cc NEST* 6; each
  re-run by the Lead in both orders with pinned Oink: even iterations = S, solutions verified); k = 4 parts: NEST* 6, no 7, in climbs
  (≥ 650 / ≥ 300 steps) and in 448 hand-built gate/return configurations (k4u_n101 sha1 37a45ff8a932bcc6e4a79d4848a0a57dbb82367a,
  NEST* 6, S 25; k4L72r_n101 e84a57b6f13e546811c203bf35b86a0ee8b69462, S 31, NEST* 5); S ≤ 31 at n = 101 throughout (about n/3).
  Obstruction (reading, one seed, R51 §4-§5): a seventh level needs a longer post-block stretch with no shallow first change inside it;
  no edge class tried gives both. False single-pool laws found on the way (R49 §6, §8): (G-NEXT) and (G-ADJ) (nest4u_n46 transition
  #3, nest4uu_n51 #16, nest5_n49 #2), (O-SEG) (oseg_n26, sha1 381b7b9d…), (W) (near4_n26, 6d7c5e38…). Closed by the Lead (decision 07:35Z under
  L37 (3); Lead reading): even a family refuting (NEST*-BOUNDED) would not give a super-polynomial family while S stays linear (S ≤ 31
  at n = 101, DATA). (NEST*-BOUNDED) stays OPEN.
- DE28 (2026-10-23): N8a = Koh-Loho strategy iteration over the perfect (n, d/2)-universal tree (Koh & Loho arXiv 2108.13338, Algorithm 1;
  pdf sha256 21ee0e43…), with either frozen rule "global" or "switch-all" (L-NEW, (c) lane under D14/D15; docs/new/N8a-kohloho.md §2
  frozen, §7 dead-end record, l-new 30b8a6c), is a DEAD END at gauntlet step 2 (runtime growth, DATA): under both rules, pivot families
  whose verified members follow laws that are super-polynomial in n (laws DATA: H_k k ≤ 3, F_k k ≤ 1, G_k k ≤ 2, L_k k ≤ 3; R53 §6b G2) (L-RED box 21, docs/red/R53-n8a-counter.md §1-§6; l-red 9fa1067, 4035ab5, 1c19da3, 866615f). Every row below: kl.py
  --sol, then experiments/new/check_sol2.py = Oink zlk OK, strategies verified.
  Canonical family H_k = klmin_n13 (13 vertices, 18 edges, sha1 b8a5b1bdb2f130adee4a20e70b5b5382932f1b4e) + 2k isolated self-loops
  with new top priorities (experiments/red/kl/gen_gk.py or famgen.py H k), n = 13 + 2k: dual pivots 52, 900, 19,652, 521,284 for
  k = 0..3 = 4·n^{k+1} under BOTH rules (runs identical for k ≤ 2 as below, traces logged for k = 0; equal counts for k = 3) (H_1 889e8e1d…, H_2 c8a9fdffd5c74781f803a47da950829985457820,
  H_3 7b7b2ecc…); law DATA for k ≤ 3, i.e. n^{(n−11)/2}. Further families: F_k (klcount_n16 b5269084…, switch-all 4·n^{3+k}+3, k = 0, 1),
  G_k (klglobal_n16 179b2cd0…, global 8·n^{1+k}+6 and switch-all 5·n^{1+k}+1, k = 0..2); independently L-NEW's L_k (15-node core
  40dde127…, primal, global 3·n^{k+1}+1, switch-all 4·n^{k+1}; levels_2 3c0092c4…, levels_3 9ce17076…). Lead re-runs (trunk kl.py, both
  rules where listed): klcount_n16 and klcount_n18_lvl (switch-all), klglobal_n18_lvl and klglobal_n20_lvl2 (global), H_2 from famgen.py
  (both, 19,652 each); all verified. gen_gk.py reproduces every pinned F/G/H sha1 (L-RED R53 §6a; CHECKER C22 re-run).
  Mechanism (R53 §2-§5, reading from traces): Tighten on the perfect tree carries in base n; a lapping cycle that the rule keeps open
  climbs one leaf per period through all leaves of the top L levels, and each extra priority value (even on an isolated vertex) adds a
  level. R53 §6b: PROVED Tighten = leftmost leaf below the successor (any ordered tree); PROVED the top L levels of an (ℓ, h)-universal
  tree are (ℓ, L)-universal; COMPUTED (kadmiss.py: at most one admissible arc per Odd node at every iteration on H_0..H_2), hence
  PROVED by induction: every rule in SA (switch every Odd node that has an admissible arc, to an admissible arc; R53 §6b
  item 3) gives the identical run on H_0..H_2; transfer to every
  universal tree for SA rules is a READING with gaps G1 (succinct trees: local offsets), G2 (law DATA for k ≤ 3), G3 (rules outside SA not
  covered). REFUTED (computed, ksubset.py) for 'every pivot rule': four single-switch rules (lowest index, highest index, random seeds
  1, 2) solve H_0..H_2 in 9, 5, 5, 17 iterations (this led to N8d). Not touched: the paper's theorems
  (iterations ≤ n·|L(T)|; the family shows the perfect-tree bound is nearly attained). Random corpus (10,000 games, both rules) all
  verified: the kill is on running time, not correctness.
- DE29 (2026-10-23): N8d-R1 = Koh-Loho tree SI over the perfect tree with the single-switch rule R1 (lowest-index Odd node with an
  admissible arc takes its largest-Tighten arc; rules frozen in docs/new/N8d-single.md §0 at l-new d7fadfb before any run; code
  experiments/new/kl/kl_single.py --rule r1) is a DEAD END at gauntlet step 2 (runtime growth): on Friedmann's switch-all family
  (experiments/hard-families/pgsolver_port.py switchallexp N, n = 14N + 7) dual pivots 14, 39, 84, 165, 318, 615, 1,200, 2,361, 4,674,
  9,291 for N = 1..10 (ratio 1.93-1.99 per N from N = 5; DATA fit ≈ 9·2^N = 2^{Θ(n)}); switchbestexp N = 1..8: 28 … 2,297 (×1.8 per N at the top);
  every output verified and = Oink zlk (results/switchallexp.r1.csv, switchbestexp.r1.csv; l-new c79dd24). Lead re-run (03:50Z, trunk
  kl_single.py): N = 6 (sha1 5dc850b156c6…) 615 and N = 7 (ff46e32f1d93…) 1,200 dual pivots, check_sol2 verified, = lane CSV.
  Reading (lane, N8d §3): the lowest-index single switch falls to Friedmann's families as single-switch rules do on VJ valuations
  (BARRIERS B8); the tree labels do not help there. Not a kill of N8d-R2 (random node), which is under attack (L-RED box 22).
- DE30 (2026-10-23): N8d-R2 = Koh-Loho strategy iteration over the perfect (n, d/2)-universal tree (arXiv 2108.13338v5, Algorithm 1) with
  the single-switch rule R2 (a uniformly random Odd node with an admissible arc, drawn by random.Random(seed), takes its largest-Tighten
  admissible arc; docs/new/N8d-single.md §0 frozen at l-new d7fadfb, pins §0b/§0c: compressed priorities canonical) is a DEAD END at
  gauntlet step 2 (runtime growth, DATA): a family whose verified members run the full lap counter, about (4L+2)·n^{k+1} pivots, on all but one of 17 runs
  (L-RED successor 12, box 24, docs/red/R56-r2-vj-switchsets.md §2-§4; l-red 29f74b1, 3bc170d, c5e3abb, b088440).
  Family HLg_k = experiments/red/kl24/hlgen.sh k L L: R53's H_k (DE28) plus two z-separated delay lanes (lanegen.py) on the two moves
  by which R2 escaped H_k, with L = 5, 6, 8, 10 for k = 0..3, n = 9 + 2k + 4L = 29, 35, 45, 55 (sha1 d2b96b45…, 2366cbad…, 1c3c7889…,
  9918e9b8463507401cf73a73a2945aa9bf5f23ac). R2 dual pivots (primal 0 on every row), every output with regions = Oink zlk @ 8fbf0a7 and
  both strategies passing experiments/harness/verify.py, code experiments/n8d-second/kl2fast.py (= L-NEW's kl_single.py seed for seed,
  checked on HL88_0 seeds 1-3 and HL88_1 seed 1): k = 0: 633, 623, 639, 643, 611 (mean 630); k = 1: 32,170, 32,232, 32,156, 32,214,
  32,232 (mean 32,201); k = 2: 3,139,182, 3,139,646, 1,230,538, 3,138,968, 3,139,556 (mean 2,757,578; one early stop, seed 3); k = 3: 388,766,970 and
  388,771,694 (seeds 1-2 only, runtime; mean 388,769,332). Steps ×51, ×86, ×141 per +1 of k. Lead re-runs: k = 0 and k = 1 seeds 1-5
  (kl2fast, all = lane, all verified; hlgen sha1s reproduced), k = 2 seeds 1 and 3 (= lane, verified, as HL88_2: same sha1), k = 3:
  lane rows only (results/hlg_k3.csv, solvecheck.py); not re-run by the Lead or CHECKER (a Lead re-run of seed 1 was lost to a container restart).
  Per-lap failure probability ε(L) of the lap counter (DATA: exact absorbing-chain computation, experiments/red/kl24/exactlap.py, from
  kl2fast's own candidate sets and least fixed point): steady per-lap ε = 6.2e-3, 5.75e-4, 3.92e-5, 2.1e-6, 1.0e-7 at L = 4..8, ratios
  ×10.8, ×14.7, ×18.3, ×21 per +1 of L (ratios growing; reading, R56 §3c: not a power law on this range). Lead re-run of the one-lap chain: L = 5 3.90822e-4,
  L = 6 2.75358e-5 (= lane). Coverage caveats: one snapshot lap per L for the multi-lap chain; every lap start scanned only at L = 4, 5
  (R56 §3b'); L ≥ 9 one-lap or extrapolated.
  Mechanism (READING, R56 §1, §4d): on Friedmann's Random-Edge game G_ζ (faithful: VJ Random-Edge counts on it, R55) R2's admissible
  sets differ from VJ's improving sets from state 0 (M1: label truncation hides odd costs; M2: truncation is idempotent, so delay lanes
  do not unwind), which is why G_ζ does not kill R2; the z-separated lanes repair M2, and a lap fails only if a run of L frontier picks
  beats every rescuer, so ε(L) ≲ 2^{−L}; with L(k) = Θ(k log k) the size stays polynomial in k and the expected pivot count is
  exp(Θ(n)) (READING beyond k = 3).
  Status: PROVED nothing new about R2's running time; DATA the table and the exact chains; READING the mechanism, the at-least-
  exponential decay of ε beyond L = 8 and the asymptotic schedule. Gaps for a proof: (G1) an ε bound for every lap type reachable in
  HLg_k; (G2) lap failures are the only exit from the counter. Not touched: correctness (N8d-proofs.md §2, PROVED by L-NEW, unrefereed:
  any single admissible switch rule is correct and terminates within n·n^h pivots); gauntlet steps 2 (two independent implementations,
  ~83,000 runs, 0 incorrect; L-COMP experiments/n8d-second/; passed by Lead reading 08:35Z) and 3 (L-LIT T26, SIGN WITH CAVEATS) had been passed; on Friedmann's
  switch-all/switch-best families and 10,000 random games R2's means stay about n^2 (DATA), which this family overturns.
- DE31 (2026-10-23): N9a = the fixed-level Sherali-Adams lift SA+_k of the 0-1 program ACYC for the query "Even wins every vertex"
  (L-NEW successor 7, box 18, (c) lane under D14/D15; docs/new/N9-screen.md §1; l-new 67884f3, eb4d33c; Lemma A (§1, PROVED by the lane,
  unrefereed): integral ACYC is feasible iff Even wins every vertex) is a DEAD END at gauntlet step 2 (incorrect answers, DATA): for
  each k ≤ 3 the level-k lift is feasible (answer "Even wins every vertex") on one-player games that Odd wins everywhere. Family
  circ(n,1,2) (every vertex Even's, every priority 1, edges v → v+1, v+2 mod n); least exact level k* = ceil(n/3) for n = 3..11
  (formula written before the n = 10, 11 runs, experiments/new/sa/results/circ12_sym_prediction.txt); wrong instances
  instances/circ12_n7.pg (k = 2, sha1 4a1973a88a1311966ef5d2f5382221aef3d09c3e) and circ12_n10.pg (k = 3, sha1
  5683b4e48a53988a71ca5eae386a4a03f8a08e27), Oink zlk: Odd wins every vertex; gaps survive tightening the strict constraints to +1.05
  (robust.py). Solver: scipy/HiGHS (infeasible verdicts by IPM; dual simplex agrees for n ≤ 8; every feasible verdict, i.e. every wrong
  answer, is checked by the residual of the returned point, ≤ 1e-6, N9-screen §1(f)). Lead re-run (twoout.py circ 3 9 4 1 2
  --sym, scipy 1.18.1): k* = 1, 2, 2, 2, 3, 3, 3 for n = 3..9 (= ceil(n/3), = lane). READING (not proved): k* is unbounded on this
  family, so no fixed level is exact. Scope: this kills SA+_k of this encoding (ACYC) for k ≤ 3 (DATA), and every fixed k only under the READING
  above; its level 1 is already inexact on one-player games; it says nothing about lifts of other encodings, Lasserre/SOS levels, or
  levels growing with n (N9-screen §1(f)).
- DE32 (2026-10-23): N9b = certified LP-guided peeling (round the level-1 lift of the region program REGION, certify the rounded
  strategy by a one-player solve, remove its attractor, repeat; sound by construction, at most n rounds; docs/new/N9-screen.md §2) is a
  DEAD END at gauntlet step 2 (incomplete: STUCK, no answer): stuck on 6 of 300 and 57 of 2,000 random games and on counter_symsi
  N = 2, 3; every game it solves agrees with Zielonka. Smallest: instances/peel_r1147.pg (n = 5, sha1
  68a8c41b926e2fd324b196c99c4c61ea6d2a91ed; Odd wins every vertex): STUCK after 1 round with 5 vertices left. Obstruction (lane, §2(f)):
  on peel_r26 (n = 6, sha1 86542531214dd56ef1e21adb6e816448ffbe8f13) the LP value equals |W_Odd| = 6 yet the rounded strategy wins nowhere, because the LP optimum is a mixture of
  strategies, so no rounding threshold helps (READING); on peel_r90 the outcome depends on which optimal vertex HiGHS returns.
  Not tested (lane, §2(f)): higher levels; rounding by conditioning. Lead re-run (peel.py instances/peel_r1147.pg): "STUCK after 1 rounds, 5
  vertices left"; Oink zlk: Odd wins all 5 vertices.
- DE33 (2026-10-23): N10a, N10b, N10c = LP relaxations of the 0-1 program ACYC (N9-screen §1(e), level 0) strengthened by ESCAPE cuts,
  separated exactly by minimum cuts (L-NEW successor 7, box 19, (c) lane under D14/D15; docs/new/N10-screen.md §0-§3,
  experiments/new/esc/; l-new b8a4282, 25b7ac2). Lemma B (§0, PROVED by the lane, unrefereed): ESCAPE cuts are valid, and ACYC + ESC1 is
  exact on one-player games of either owner (data: 924 one-player queries and circ(n,1,2), n = 3..10, 0 gaps). All three are DEAD ENDS
  at gauntlet step 2 on two-player games (DATA):
  (a) N10a (ACYC + ESC1): gaps (feasible although Odd wins a vertex) in 15 of 800 two-player queries (random seeds 0..299, n = 3..12;
      results/rand300.txt); in 12 of the 15 no ESC1 cut was ever violated.
  (b) N10b (+ ESC-tau, Odd's strategy tau from the REGION LP of N9b): 0 gaps in 800 and 3 in 5,432 random queries, 0 in 17,528
      exhaustive n = 3 queries (every 10th game), 2 on hard families (counter_symsi N = 2, 3, Odd query). Smallest gap:
      instances/esc_gap_r1794_Q1.pg (n = 8, sha1 ab859e3f4acf4ca223bc7af905010d59db758d66; Oink zlk: Even wins only vertex 5); no
      violated cut was found.
  (c) N10c (conditioning on the N10b oracle; Lemma D, PROVED by the lane, unrefereed: YES answers are correct, NO-instances get NO,
      never wrong on one-player games; errors one-sided): STUCK on yes-instances r1569 (n = 14, instances/cond_stuck_r1569_YE.pg, sha1
      c7715537ff454341b3309ea058796c1f759c1ba6; 1 of 8,000 random games) and counter_symsi N = 3 restricted to W_E (n = 32,
      instances/cond_stuck_symsi3_YE.pg, sha1 4483eb7c813989cb79edf76c6e604367d39db75a); the r1569 failure is an N10b gap at n = 14
      (instances/esc_gap_from_r1569.pg, sha1 194a1ff6c5d83307f221180b39cdba11eb891c06; the LP point passes a residual check ≤ 1e-6).
      The hard-family run was stopped after counter_symsi N = 3; tc, tc+ N = 1, 2 and switchallexp N = 3 are NOT FINISHED for N10c.
  Lead re-run (pip scipy 1.18.1, highspy, networkx; experiments/new/esc, python3 -I): all five pinned sha1s reproduced;
  esctest.py files esc_gap_r1794_Q1.pg --tau: "GAP … Q1 n=8 cuts=0" (N10b); without --tau: gaps on Q1 and Q2 (N10a); condtest.py
  files cond_stuck_symsi3_YE.pg cond_stuck_r1569_YE.pg: STUCK on both (21 oracle calls, 654 s); Oink zlk: Even wins exactly 1 of the
  8 vertices of esc_gap_r1794_Q1 and all 14 of cond_stuck_r1569_YE.
  READING (lane, §5): one-player exactness is cheap (a min-cut family); the remaining difficulty is Odd's strategy tau, which the cuts
  do not supply; every N10 failure is a game where no LP-guided tau exposes a violated cut. N10d (exact (U, tau) separation) not run:
  finding a separating tau is finding an Odd dominion, the problem itself.
- DE34 (2026-10-24): N11 = N5-HT, N5 (SSI-GLOBAL, docs/new/N5-ssi-global.md) with an honest override at trust conflicts (at
  each Even vertex x where N5's step is honestly worse than the best edge of Iσ, i.e. key(Ξσ(σ_W(x))) < max over (x, z) ∈ Iσ of
  key(Ξσ(z)), take that best edge, ties to the larger index; Odd symmetric on G^d; L-NEW successor 8, box 23, (c) lane under
  D14/D15; docs/new/N11-proposal.md, rule frozen in its FREEZE section at l-new e003f7e before any run, code
  experiments/new/n11/n5ht.py sha1 598cc9000e293e2a6e59e0cc9b030dd0b4912604; l-new 138ea49, 5f27c48) is a DEAD END at gauntlet
  step 2 (runtime growth, DATA). Termination and correctness are not in question: σ', τ' switch subsets of Iσ, Iτ, so RESULTS R15
  applies. Faithfulness (faith.py 1500 12 31): with the override off, traces equal n5.py on 1,500 of 1,500 random games; every run
  with no conflict (1,137 of 1,500) equals N5's trace.
  Families (experiments/hard-families/pgsolver_port.py, deterministic), canonical start, every output with regions = Oink zlk and
  both strategies verified (check_sol2.py), results experiments/new/n11/results/:
  (a) Friedmann's switch-best family switchbestexp N = 2..8 (n = 25N + 10): N5-HT iterations 61, 141, 301, 621, 1,261, 2,541,
      5,101 = 20·2^N − 19 exactly (DATA, N ≤ 8); N5 on the same games 32, 41, 47, 55, 62, 68, 77. N = 4 sha1
      57b27b7476bcb72bae29fc5e8b2221be0609e8ec, N = 8 sha1 7082e7242d8250993d175771c1e2ac17372fb31c.
  (b) Friedmann's switch-all family switchallexp N = 2..8 (n = 14N + 7): 30, 70, 150, 310, 630, 1,243, 2,486 (= 10·2^N − 10 for
      N ≤ 6, then ×2.0 per step); N5 8 … 16. N = 6 sha1 5dc850b156c6d1e2adace088b58c0f65cc9e0bf2, N = 8 sha1
      18c2462457856437590d82018d0e9140916a67a6.
  DLM families 1-2 from their start pairs: linear (≤ 17 iterations at n = 72); not a kill.
  Lead re-run (trunk experiments/new/n11/bench.sh with OUT/TMPD in the Lead scratchpad; n5ht.py sha1 = frozen): switchbestexp
  N = 2..8 and switchallexp N = 2..8, every row = lane CSV (iterations, conflicts, N5 iterations), every row "zielonka(oink zlk)
  OK strategies verified"; generated sha1s = lane.
  Obstruction (lane, N11-proposal.md RESULT): on these games the conflict set is large at almost every iteration (17,882
  conflicts in 5,101 iterations at switchbestexp N = 8) and the override is switch-all's own choice, so N5-HT replays Even
  switch-all SI (READING; the counts equal Even switch-all from σ_0 on switchbestexp N = 2..5, box 21 table) and meets BARRIERS
  B8 (Friedmann LMCS 7(3:19) 2011, Thm 6.14, Thm 8.4). Not run (dead at the first test): R56/R57 families, frozen climbs, the
  I3/I4 invariant test. READING (lane): a repair of N5's trust-mode deadlock that falls back to honest-greedy choices on
  conflicts collapses to switch-all on Friedmann's games.
