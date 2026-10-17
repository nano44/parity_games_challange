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
