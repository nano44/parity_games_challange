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
