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

### R74 [refereed-only] N5 on EVERY game, inside one phase: an S4a step is a Bellman-Ford round at the Even vertices of A_t := F_D(t) ∩ U_c that stay disagreement-free (v ∈ F_D(t) ∩ F_D(t+1)) (Lemma BF-F_D); while A does not grow and no fallback occurs, path weights on A freeze after |A_s| − 1 transitions and an Odd vertex q whose choice lies in A then changes its path weight at most deg(q) − 1 times (Theorem FREEZE-A, (R-LEN)); hence a per-phase bound on those changes in terms of f + G_c (Corollary ROOT-PIECE, a REDUCTION: G_c, the A-gains, is not bounded); every A-gain is a D-leave or an Even switch of an unsplit vertex, and a clean D-leave carries a ROUTE / CYC / TOG event, a route change or a tie (Lemma DL-SPLIT); behind a D-direct gate u the honest path weight M lags the W-path weight MW by exactly the gate's offset Δ_t(u) ≥ 0 and the W-frame step is exact (Lemma GATE-SHIFT), so on a G-interval (S4a steps only, u a D-direct gate, A and R_u not growing, Δ constant) W-path weights on A ∪ R_u freeze after |E_s| − 1 transitions (Theorem FREEZE-G), and a relay of the gate then changes its path weight at most deg(u)(|U_c| − 1 + deg(q)) times after A's freeze (Corollary RELAY-PIECE) (2026-10-26) — structural lemmas and two REDUCTIONS for N5 (G_c, f and the number of G-intervals are not bounded here; FREEZE-G (b)'s freeze sentence, FREEZE-G (c) and RELAY-PIECE's multi-value content rest on proof alone; not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C83.md, checker 4f494319)
- Objects (L-SI successor 16, Opus 5.5; frozen, unchanged during review): packet P-N5-ROOT, docs/si/P-N5-ROOT-box20.md, sha1
  d3788bc0ce0e3da2d54298c58e227e437242419a (l-si freeze ced5cf27), and its addendum P-N5-ROOT-add, docs/si/P-N5-ROOT-add-box20.md, sha1
  af1c7ad4581cce4a9830b4ed01e2370d26ef850b (l-si freeze 829003b2), reviewed together; both on trunk 539b4192 at REFEREE's review. The
  referees' notes are collected by the lane in docs/si/P-N5-ROOT-fixes-box20.md (l-si 15795d31, sha1
  c8d01a25c61d6ae2eefd3f42a470fa2a467e0c3a, L-SI successor 19: F1-F10 for ROOT-N1..N5, ADD-N1..N2, N-ROOT-1..7; 36 quotes checked by
  script); on trunk; repairs only, no signed statement changes. The statements below are in their repaired wording (F1, F4, F5, F6, F9).
  Setting (every game): N5 = SPEC S1-S5 with FIX 1-4; phases as in RESULTS R38 (a) KEY (λ_Ξ and τ constant); every in-phase transition is an
  S4a step or an Even S4c fallback; D_k, u(v), R_D, F_D as in RESULTS R55's setting; W_t(v) the value of the (σ_t, τ)-play; classes U_c, κ,
  κwt_c, wt_c as in RESULTS R56's setting. Fix a phase, a cycle node c, U := U_c, wt := wt_c, M_t(z) := wt(P(Ξ_t z)), MW_t(z) := wt(P(W_t z))
  when W_t(z) has cycle node c. A_t := F_D(t) ∩ U. G[A]: the graph on A in which every Even v ∈ A ∖ {c} keeps its edges into A, every Odd
  v ∈ A ∖ {c} keeps its τ-edge if τ(v) ∈ A, and c is a sink; MoptA(z) := the best wt-weight of a simple G[A]-path from z to c. An A-GAIN: an
  in-phase S4a transition with A_{t+1} ⊄ A_t; G_c := their number in the phase; f := the in-phase fallbacks. An Odd u ∈ U is a D-DIRECT
  GATE at t (u ∈ DD_t) if u ∈ D_t, σ̄_t(u) ∈ A_t and τ(u) ∈ A_t; its OFFSET Δ_t(u) := M_t(τ u) − M_t(σ̄_t u); R_u(t) := {z ∈ U : the first
  D_t-vertex of z's (σ_t, τ)-play is u}; E_t := A_t ∪ R_u(t); off_t := 0 on A_t and Δ_t(u) on R_u(t); N_t := MW_t on E_t. G′[E] and
  MoptG′[E] as G[A] and MoptA, with R_u-vertices keeping their edges into E (Even) or their τ-edge if it lies in E (Odd, u included). A
  G-INTERVAL for u: states [s, e] of the phase, all transitions S4a, u ∈ DD_t throughout, A_{t+1} ⊆ A_t, R_u(t+1) ⊆ R_u(t), Δ_t(u) constant.
- Claims signed (both referees "(Opus 5.5, D15)", L37), on every game, inside one phase; no item uses (P); premises LANDED: SPEC S1
  (injective rewards), S4c with FIX 3; RESULTS R38 (a); R55 setting and (a) G_D (a); R17 (a) (F1) and (V1), R21 (a) XW (game-general by
  RESULTS R54 / R55); R56 (a) (Aκ), (A0κ), (M1κ), (M2κ), (INJ) and (d) κ-Y-FORM_D; R61 (e) ALT (CLEAN); R62 (d) WM-G; R63 (a) R-STICK_D;
  P-N5-FLIP §1 additivity (signed as a proof step); RESULTS R72 (b) RELAY-CHAIN for DL-SPLIT (i) (the packet's condition, MET by R72's
  landing: REFEREE-2, and REFEREE's §C). Standing premise 1E-N3 in its two forms (N-ROOT-5, accepted by REFEREE in place of ROOT-N2; F2):
  P2 (S4a's σ_{t+1} is Even's pointwise optimum in the arena H_t) for (F1) on S4a's arena and WM-G (BF-F_D, FREEZE-A, GATE-SHIFT (b),
  FREEZE-G, and through them ROOT-PIECE, RELAY-PIECE); P1 (σ̄ is Odd's pointwise optimum in G_σ) for κ-Y-FORM_D (FREEZE-A (c), DL-SPLIT,
  GATE-SHIFT (a); through them also (R-LEN) and ROOT-PIECE (fixes F2's table), and FREEZE-G and RELAY-PIECE, whose Even step uses GATE-SHIFT
  (a)'s Δ ≥ 0):
  (a) Lemma BF-F_D: at an in-phase S4a transition t → t + 1, for Even v ∈ U ∖ {c} with v ∈ F_D(t) ∩ F_D(t+1) and every successor x ∈ U of v,
      M_{t+1}(v) ≥ wt(v) + M_t(x).
  (b) Theorem FREEZE-A: let every transition of [s, e] be an S4a step with A_{t+1} ⊆ A_t, and L := max(|A_s| − 1, 0). (a) For t ∈ [s, e],
      z ∈ A_t and every simple G[A_t]-path p from z to c with ≤ t − s edges, M_t(z) ≥ wt(p ∖ {c}). (b) M_t(z) ≤ MoptA_t(z) on A_t; hence for
      s + L ≤ t ≤ t′ ≤ e and z ∈ A_{t′}, M_{t′}(z) = M_t(z) = MoptA_t(z). (c) For Odd q ∈ U and V_q := {wt(q) + M_{s+L}(y) : y ∈ succ(q) ∩
      A_{s+L}}: at every t ∈ [s + L, e] with σ̄_t(q) ∈ A_t, M_t(q) ∈ V_q; so at most deg(q) − 1 transitions in [s + L, e) with σ̄(q) ∈ A at both
      ends change M(q). For q = c, (Aκ) is not used: M(c) = 0 and τ(c) is c's successor on its cycle, with M = 0 (ROOT-N1 = N-ROOT-1, F1).
      (R-LEN): at the states counted in (c), Ξ(q) runs through ≤ deg(q)·(|U| − 1) distinct values, so it changes at most
      deg(q)·(|U| − 1) − 1 times at the counted transitions (ROOT-N4 = N-ROOT-2, F6: the count follows from the chain of distinct
      (M, length) pairs; the packet's sentence about Ξ on A_t is true but is not the step, as q may lie in D_t).
  (c) Corollary ROOT-PIECE (a REDUCTION in G_c): for Odd q ∈ U, the transitions of the phase with σ̄(q) ∈ A at both ends that change M(q)
      number ≤ (f + G_c + 1)·(|U| + deg(q) − 2) + f + G_c, and the Ξ-changes of q at them ≤ (f + G_c + 1)·(|U| − 1)(deg(q) + 1) + f + G_c.
  (d) Lemma DL-SPLIT: at an in-phase S4a A-gain of class c, every entering z ∈ A_{t+1} ∖ A_t satisfies (A) its first D_t-vertex u is not in
      D_{t+1} (a D-LEAVE at u: σ̄_{t+1}(u) = τ(u) ≠ σ̄_t(u)), or (B) z is unsplit at t (λ_{W,t}(z) = λ_t(z) = c) and leaves R_D by an Even switch
      (N-ROOT-4, F4: the packet's statement lacks the binder; the proof shows this form). In case (A) with a CLEAN change (RESULTS R61 (e)),
      y1 := σ̄_t(u), y2 := σ̄_{t+1}(u) and e1 := y1's exit: (i) e1 ≠ c and Ξ(e1) changes, so the transition carries a ROUTE, CYC or TOG event of
      class c (RESULTS R72 (b) RELAY-CHAIN (a)); or (ii) u has a ROUTE CHANGE (some class exit path or exit of u's options differs at t and
      t + 1) (N-ROOT-3, F5); or (iii) a TOG step at e1 or a TIE κ_t(y2) = κ_t(y1). Consequence (a decomposition, not a bound): G_c ≤
      #(B-gains) + #(S4a transitions carrying a ROUTE / CYC / TOG event of class c, or a route change, a tie or a non-clean change at a
      D-leaving vertex). REFEREE's §C: in the clean case (A) without a tie, u also has a ρ event, so a route change there is a ROUTE event in
      P-N5-FLIP's sense; the list is unchanged in content.
  (e) Lemma GATE-SHIFT: (a) at a state t, for z ∈ U with u(z) ∈ DD_t: W_t(z) has cycle node c, Δ_t(u) ≥ 0 and M_t(z) = MW_t(z) − Δ_t(u);
      (b) at an in-phase S4a transition, for Even z ∈ U ∖ {c} whose first D_{t+1}-vertex u lies in DD_{t+1} and every successor x ∈ U of z whose
      (σ_t, τ)-play avoids z: MW_{t+1}(z) ≥ wt(z) + M_t(x), hence M_{t+1}(z) ≥ wt(z) + M_t(x) − Δ_{t+1}(u).
  (f) Theorem FREEZE-G: on a G-interval [s, e] for u, L := |E_s| − 1: (a) for t ∈ [s, e], z ∈ E_t and every simple G′[E_t]-path p from z to c
      with ≤ t − s edges, N_t(z) ≥ wt(p ∖ {c}) (the base N_t(c) = 0 uses c ∉ R_u(t): ADD-N1, F8); (b) N_t(z) ≤ MoptG′[E_t](z); hence for
      s + L ≤ t ≤ t′ ≤ e and z ∈ E_{t′}, N_{t′}(z) = N_t(z) and M_{t′}(z) = M_t(z); (c) for Odd q ∈ U ∖ {u, c}, over t ∈ [s + L, e] with
      σ̄_t(q) ∈ E_t, M_t(q) lies in {wt(q) + M_{s+L}(y) : y ∈ succ(q) ∩ E_{s+L}}, non-decreasingly, so ≤ deg(q) − 1 such transitions with
      σ̄(q) ∈ E at both ends change M(q).
  (g) Corollary RELAY-PIECE (a REDUCTION in the number of G-intervals): let [s, e] satisfy FREEZE-A's hypothesis, L_A := |A_s| − 1, u ∈ DD_t
      for every t ∈ [s, e] and R_u(t+1) ⊆ R_u(t). (i) Over [s + L_A, e], Δ_t(u) takes ≤ deg(u) values (non-increasing), so [s + L_A, e] is the
      union of ≤ deg(u) disjoint G-intervals for u (blocks of consecutive states; each transition at which Δ changes lies between two
      consecutive blocks, in neither) (ADD-N2, F9). (ii) For Odd q ∈ U ∖ {u, c}, the transitions in [s + L_A, e) with σ̄(q) ∈ E at both ends
      that change M(q) number ≤ deg(u)·(|U| − 1 + deg(q)).
- Not signed: ROOT §6 and the addendum's §5-§6 (the map of FRZ-U's single-gate steps, GATE-LAG and the other READINGs; the DATA; the OPEN
  items: G_c, which is self-referential with ROOT-PIECE (ρ ≤ (f + G_c + 1)·B and G_c ≤ B-gains + ROUTE / CYC / TOG transitions); the relays'
  own ROUTE events; f on general games; the number of G-intervals). The packet's DATA sentence "case (iii) never occurred" holds only as
  "never ALONE": (iii) occurs (REFEREE 237 ties and 221 TOG steps in its library; REFEREE-2 579 clean D-leaves), always with (i) or (ii)
  (ROOT-N5 = N-ROOT-6, F7).
- Honest limits: (i) Structural lemmas and REDUCTIONS: ROOT-PIECE bounds an Odd vertex's path-weight changes by (f + G_c + 1)·poly(n) and
  RELAY-PIECE bounds a relay's per G-interval; G_c, f and the number of G-intervals (resets of a gate's offset or region) are not bounded
  here; DL-SPLIT decomposes G_c but does not bound it. Nothing here bounds ρ, N_ep, f or N5's running time. (ii) PROOF ALONE (N-ROOT-7,
  REFEREE §4, both §Cs, F10): FREEZE-G (b)'s freeze sentence, FREEZE-G (c), and RELAY-PIECE's multi-value / multi-interval content are never
  reached on natural games (no G-interval outlives its freeze window in the lane's, REFEREE's or REFEREE-2's data, nor in REFEREE's hill
  climbs (best excess −1); Δ(u) never changes after FREEZE-A's freeze index in any run). They are reached only in REFEREE-2's constructed
  disjoint unions (docs/referee-2/R2-N5-ROOT/union/: 25,497 G-intervals past the freeze index, 5 with N moving inside the interval, all pass;
  REFEREE successor 16 re-ran u7101_1900, u7201_1948, u7202_374 with its own engine: 3 G-intervals past the freeze window, max excess 45, 0
  failures); the control that tightens (b)'s freeze index never bites. Both referees checked these proofs line by line. (iii) Over-budget
  pieces: path enumeration skipped REFEREE 165 FREEZE-A pieces / 111 G-intervals in its library row (UNK) and REFEREE-2 the large classes of
  the n = 40-64 library games (e.g. lib41: 7,350 pieces, 5,024 G-intervals UNK).
- Data (DATA, not proof): REFEREE (successor 15, own root_probe.py on its own engine; lane code not run): library n ≤ 24 (2,960 runs; BF-F_D
  316,395 checks; FREEZE-A 142,861 checks, 378 pieces past s + L; FREEZE-G (a) = (b) 47,498 checks on 1,899 G-intervals), 3,000 random games
  (21,000 runs), nep90_n40 and nep76_n40 at the lane's starts, FREEZE-G hill climbs (n 5-10, 2 × 100,000 candidates); 0 failures;
  mutations bite (MUT=1 one more edge: FREEZE-A (a) 136, FREEZE-G (a) 1; MUT=2 GATE-SHIFT (b) with Δ := 0: 181; MUT=3 BF-F_D without
  v ∈ F_D(t+1): 48). REFEREE-2 (successor 17, own root_check.py; lane code not run): the lane's starts, lib2o, lib41, its 503 𝒞^1O files,
  random games with 2, 4 and all Odd choice vertices (19,500 runs), and 12,000 constructed unions; BF-F_D 922,585 checks on lib41 alone;
  0 violations of every check in every set; controls gs0 (Δ := 0) 9,469, fa1 81, fg1 20 (and 8 on unions), early 0 (N-ROOT-7). Both
  reproduce the lane's BF-F_D 7,827 / 8,701 and GATE-SHIFT (a) 684 / 404, (b) 943 / 661 on nep90 / nep76.
- Signatures: REFEREE docs/referee/R-N5-ROOT.md (referee 619fccf2, successor 15; §C da0c1902, stamp corrected 65f55427, successor 16):
  BF-F_D, FREEZE-A (a)-(c), (R-LEN), ROOT-PIECE (as a REDUCTION), DL-SPLIT (split, clean case (A), Consequence as a decomposition), GATE-SHIFT
  (a), (b), FREEZE-G (a)-(c) (FREEZE-G (b)'s freeze sentence and (c) on PROOF ALONE), RELAY-PIECE (i), (ii) SIGNED, no gap; notes ROOT-N1..N5,
  ADD-N1..N2. REFEREE-2 docs/referee-2/R2-N5-ROOT.md (referee-2 3febbfaf, §C f5381a5c, successor 17): the same items SIGN, no gap; DL-SPLIT's
  condition MET (RESULTS R72); notes N-ROOT-1..7. §C (both): verdicts identical; joint gap map EMPTY; ROOT-N1 = N-ROOT-1, ROOT-N4 = N-ROOT-2,
  ROOT-N5 = N-ROOT-6; N-ROOT-5 replaces ROOT-N2 (accepted by REFEREE); N-ROOT-3 and N-ROOT-4 accepted by REFEREE; ROOT-N3, ADD-N1, ADD-N2
  accepted by REFEREE-2; nothing open. Both under the standing premise 1E-N3 (P1 and P2).
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (structural lemmas and per-phase reductions; no running-time bound). GAPS
  G-N5-TIME: open.

### R75 [refereed-only] N5 on EVERY game, inside one phase: the κ-offset off(q; p) of an Odd choice vertex q ≠ c to its routing vertex p := par_{t+1}(q) never falls (Lemma OFFSET-MONO for q on no honest cycle at t; Lemma OFFSET-MONO⁺ for every q), so a change of κ(q) is a sum of non-negative level rises along q's chain (Corollary CHAIN-SUM with OFFSET-MONO⁺), and per run J of a phase and class the transitions that change κ(q) number at most Σ_x (|EXIT_x| + Σ_π (v_x(π) − 1)) ≤ Σ_x D·(|EXIT_x| + 1), pieces cut at the exit changes only (Corollary CHAIN-COUNT‴; the cut versions CHAIN-COUNT, CHAIN-COUNT′, CHAIN-COUNT″ hold on their own proofs); an unchanged cycle of c keeps every κ-value, routing vertex and offset on it (Remark Z-CONST); the cycle changes of a class number at most (n − 1)|U_c| + TIE_c + ODDC_c per phase (Lemma ZCH-COUNT); the transitions with an F-touching κ-change number at most 2(n − 1)(|U_c| − 1) per phase (Lemma FT-COUNT), and outside them κ is constant on the path-free vertices and on c's cycle every offset is constant (Remark FT-CONST); and, code-level against si.py e688b963 (= SPEC S1), S1's choice at a path-free Odd vertex is the (κ, tie-break)-minimiser of its options that are path-free or c (Lemma PF-CHOICE), so STRICT_c + TIE_c ≤ 2(n − 1)(|U_c| − 1) (Corollary TIE-CHARGE) (2026-10-26) — structural lemmas and a REDUCTION for N5 (the per-phase, per-class count of κ-changes is reduced to EXIT_x and D, both OPEN; ODDC_c is not bounded; not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C84.md, checker d756549c)
- Objects (four packets reviewed as ONE unit, "the OFFMONO unit"; all frozen, unchanged during review; all four on trunk 77f2664e at
  REFEREE-2's review): P-N5-OFFMONO, docs/new/P-N5-OFFMONO-box49.md, sha1 d9705ac6cede9849d68bf9b8d0fc5c54ab6fc3c4 (l-new freeze 1f816370,
  L-NEW successor 28, Opus 5.5); add1 P-N5-OFFMONO-add, docs/new/P-N5-OFFMONO-add-box49.md, sha1 5911aba8fc4e968187523c27b4f48cdc55433b3f
  (freeze b2a78eb1, successor 29); add2 P-N5-OFFMONO-add2, docs/new/P-N5-OFFMONO-add2-box49.md, sha1 f2d123ef6ebbb71408dc25b503b78edc085cbf9a
  (freeze 6ef3dd25, successor 29); add3 P-N5-OFFMONO-add3, docs/new/P-N5-OFFMONO-add3-box49.md, sha1 b7cd0ff103ead10054c8f42f787369710f7feb40
  (freeze 8b7e2e6e, successor 29). The referees' notes are collected by the lane in docs/new/P-N5-OFFMONO-fixes-box49.md (l-new 34d176ab, sha1
  490fc7f3ff31605062ac4239c3387873c06276e9, L-NEW successor 30 as the authors' successor: F1-F14 for OFFMONO-N1..N4, OFFADD-N1..N2,
  ADD2-N1..N4, ADD3-N1..N3, N-OFF-1..9; 76 quotes checked by script, experiments/new/box49/quotecheck3.py "quotes=76 bad=0", pinned in
  experiments/new/check.sh); on trunk; repairs only, no signed statement changes. The statements below are in their repaired wording (F1,
  F2, F4, F5, F6, F7, F8, F9).
  Setting (every game): N5 = SPEC S1-S5 (docs/new/N5-ssi-global.md, sha1 66fde9ef1726602fc0a52ca8d6d6fe8cbbcf110e) with FIX 1-4. A phase P is a
  (λ_Ξ, τ)-phase: λ_Ξ and τ are constant on it by definition; RESULTS R38 (a) Remark KEY (λ_U is a function of τ alone) is what makes these the
  joint λ-phases (N-OFF-1, F1; the packets' "λ constant, R38 (a)" is read so). Fix c, U := U_c := λ^{-1}(c), Q := the Odd vertices of out-degree
  ≥ 2; κ_t(z), s_c, κwt_c as in RESULTS R56's setting line; next_t(z) := σ_t(z) (Even), σ̄_t(z) (Odd); par_t(q) := the first vertex of Q ∖ {q} on
  q's honest play at t strictly before c, else c (q ∈ Q ∩ U ∖ {c}); off_s(q; p) := κ_s(q) − κ_s(p). The (t+1)-CHAIN of q: x_0 := q, x_{i+1} :=
  par_{t+1}(x_i), up to c. For a run J of consecutive in-phase transitions: EXIT_x := those with par_t(x) ≠ par_{t+1}(x); CYC_c := those at which
  some x ∈ Q ∩ U ∖ {c} is on an honest cycle at t; Z_t(c) := c's honest cycle at t as a sequence from c; ZCH_c := those with Z_t(c) ≠ Z_{t+1}(c);
  ZC_c := ZCH_c ∩ CYC_c. F := {(0, s_c·ℓ) : 1 ≤ ℓ ≤ n − 1}; A_t := {z ∈ U_c ∖ {c} : P(Ξ_t z) = ∅} (the PATH-FREE vertices); FT_c := the in-phase
  transitions at which some z ∈ U_c ∖ {c} has κ_t(z) ≠ κ_{t+1}(z) with κ_t(z) ∈ F or κ_{t+1}(z) ∈ F; ZC″_c := CYC_c ∩ ZCH_c ∩ FT_c. An x-PIECE
  (resp. ′, ″, ‴) is a maximal run of consecutive transitions of J none in EXIT_x ∪ CYC_c (resp. EXIT_x ∪ ZC_c, EXIT_x ∪ ZC″_c, EXIT_x);
  par(x) = p is constant on it; v_x(π) := the number of distinct values of off(x; p) on the states of π. Facts used as proof steps, not in the
  packets' to-sign tables: (CYC-ID) x ∈ U is on an honest cycle at t ⇔ x ∈ Z_t(c); (CYC-SHAPE) for v ∈ Z_t(c) ∖ {c}, κ_t(v) = (0, s_c·ℓ),
  1 ≤ ℓ ≤ n − 1; (A-F) z ∈ A_t ⇔ κ_t(z) ∈ F (REFEREE SIGNED them, REFEREE-2 checked them CORRECT; carried here as checked proof steps).
- Claims signed (both referees "(Opus 5.5, D15)", L37), on every game, inside one phase, fallbacks included; no item uses (P); premises LANDED:
  SPEC S1's order (l. 30-31) and S4c; standing premise 1E-N3 in its form P1 (P-N5-FLIP §1: S1's σ̄ is Odd's pointwise optimum in G_σ; RESULTS
  R57), used through Lemma S (a) by Case L of (a) and Cases L1, L2 of (i) (OFFMONO-N3, F2); RESULTS R18 (d) Lemma S (a), every game by RESULTS
  R57 (a) (VJ); R38 (a) KEY (as read in F1); R56 setting line, (a) (Aκ), (A0κ), (M1κ), (M2κ) (resting on RESULTS R15 (a) Lemma A), (INJ), and
  (d) κ-Y-FORM_D, the minimum attained at σ̄_t(q) by R56 (d) with (Aκ) (N-OFF-4, F10); (SW) "every Even switch of N5 is to an edge of Iσ", as
  listed among RESULTS R72's landed premises. (h) only: SPEC S1 l. 33 names si.py Engine.evaluate (l. 78-205) as exact; si.py sha1
  e688b96327b7fd2770126e20bb00e459c1f18869:
  (a) Lemma OFFSET-MONO (OFFMONO §1): at an in-phase transition t → t + 1, for q ∈ Q ∩ U with q ≠ c and q on no honest cycle at t, and
      p := par_{t+1}(q): off_{t+1}(q; p) ⪰ off_t(q; p). (Step 1: backwards along q's (t+1)-play from y2 := σ̄_{t+1}(q) to p, by (Aκ), (SW), (M1κ);
      Step 2: Case N by κ-Y-FORM_D, Case L by Lemma S (a) and S1's reward order.)
  (b) Corollaries CHAIN-SUM and CHAIN-COUNT (OFFMONO §2): κ_{t+1}(q) − κ_t(q) = Σ_{i=0}^{h} [off_{t+1}(x_i; x_{i+1}) − off_t(x_i; x_{i+1})] over q's
      (t+1)-chain, every term with x_i on no honest cycle at t ⪰ (0, 0). If off(x; p) takes at most D values on every x-piece, the transitions of
      J that change κ(q) number at most |CYC_c| + Σ_{x ∈ Q ∩ U ∖ {c}} D·(|EXIT_x| + |CYC_c| + 1) (a REDUCTION to EXIT_x, CYC_c and D).
  (c) Remark Z-CONST (add1 §1): if Z_t(c) = Z_{t+1}(c), then κ_t(x) = κ_{t+1}(x) for every x on it, and for x ∈ Q on it, x ≠ c, par_t(x) = par_{t+1}(x)
      and off_t(x; par(x)) = off_{t+1}(x; par(x)).
  (d) Corollary CHAIN-COUNT′ (add1 §2): Step A (off_{t+1}(x; p) ⪰ off_t(x; p) at every level of every transition of J not in ZC_c); sum form
      |ZC_c(J)| + Σ_x (|EXIT_x| + Σ_{π′} (v_x(π′) − 1)); stated form, if v_x(π′) ≤ D on every x-piece′: |ZC_c(J)| + Σ_x D·(|EXIT_x| + |ZC_c(J)| + 1).
      Remark (i), repaired (OFFADD-N1, F5): through the SUM form CHAIN-COUNT′ implies CHAIN-COUNT (an x-piece′ is a union of x-pieces glued at
      CYC ∖ ZC transitions, so Σ_{π′}(v_x(π′) − 1) ≤ (D − 1)(#x-pieces) + |CYC_c ∖ ZC_c|); the stated form alone does not.
  (e) Lemma ZCH-COUNT and its Corollary (add1 §3; a REDUCTION in TIE_c, ODDC_c): with N := {v ∈ Z_{t+1}(c) ∖ {c} : next_{t+1}(v) ≠ next_t(v)}, a
      transition of ZCH_c is STRICT (some v ∈ N with κ_{t+1}(v) ≻ κ_t(v)), TIE (not STRICT, N ≠ ∅), CEVEN (N = ∅, c owned by Even) or ODDC (N = ∅,
      c owned by Odd; the owner, not the parity Ω(c): N-OFF-5, F7). Per phase and class |ZCH_c| ≤ (n − 1)|U_c| + TIE_c + ODDC_c; STRICT ≤
      (n − 1)(|U_c| − 1), CEVEN ≤ n − 1; at a TIE every vertex of N is Odd with κ unchanged; at an ODDC c ∈ Q and σ̄(c) changes. Corollary: with
      J = the phase, |ZC_c| ≤ |ZCH_c| ≤ (n − 1)|U_c| + TIE_c + ODDC_c.
  (f) Lemma FT-COUNT and Remark FT-CONST (add2 §1-§2): |FT_c| ≤ 2(n − 1)(|U_c| − 1) per phase and class (sharper, REFEREE's ADD2-N1, checked
      CORRECT by REFEREE-2: at most n F-touching changes per vertex, |FT_c| ≤ n(|U_c| − 1); not needed, the signed bound stands; F9). At an
      in-phase transition not in FT_c: A_t = A_{t+1}; κ_t(z) = κ_{t+1}(z) for every z ∈ A_t ∪ {c}; and for every x ∈ Z_t(c) ∩ Q, x ≠ c, with
      p := par_{t+1}(x), off_{t+1}(x; p) = off_t(x; p) (N-OFF-3, F6). No tie-break of S1 is used.
  (g) Corollary CHAIN-COUNT″ (add2 §3; a REDUCTION to EXIT_x and D): Step A″ (as Step A, outside ZC″_c); sum form |ZC″_c(J)| + Σ_x (|EXIT_x| +
      Σ_{π″} (v_x(π″) − 1)); D form |ZC″_c(J)| + Σ_x D·(|EXIT_x| + |ZC″_c(J)| + 1); |ZC″_c(J)| ≤ min(|CYC_c ∩ ZCH_c|, |FT_c|) ≤ 2(n − 1)(|U_c| − 1);
      so per phase and class κ(q)-changes ≤ 2(n − 1)(|U_c| − 1) + Σ_x D·(|EXIT_x| + 2(n − 1)(|U_c| − 1) + 1).
  (h) CODE-LEVEL, against si.py e688b963 (= SPEC S1): Lemma PF-CHOICE (add2 §4): at a state t, for Odd x ∈ A_t, σ̄_t(x) is the minimiser over y ∈
      succ(x) ∩ (A_t ∪ {c}) of (κ_t(y), tb_t(y)) lexicographically, tb_t(y) := y's index if Ω(c) is even, the index sequence of y's honest play at
      t from c's side if Ω(c) is odd. Corollary TIE-CHARGE: at an in-phase transition not in FT_c, next_{t+1}(z) = next_t(z) for every z ∈ A_t
      (the Even step with x′ := σ_{t+1}(z) ∈ U_c taken from (Aκ) at t + 1: ADD2-N2, F8); every STRICT and TIE transition lies in FT_c, so
      STRICT_c + TIE_c ≤ 2(n − 1)(|U_c| − 1). ODDC_c is not covered (add2 §4's remark, not signed).
  (i) Lemma OFFSET-MONO⁺ (add3 §1), item (a) without the honest-cycle hypothesis: for every q ∈ Q ∩ U_c with q ≠ c and p := par_{t+1}(q),
      off_{t+1}(q; p) ⪰ off_t(q; p). For q on an honest cycle at t (q ∈ Z_t(c), path-free): y2 ≠ q (a self-loop at q would make q its own
      cycle node at t + 1, against λ_Ξ constant on the phase: ADD3-N1, F4); y2's t-play meets q before c (Case L1, OFFSET-MONO's Case L) or after
      c (Case L2: strict when P(Ξ_t y2) ≠ ∅, "L2a", by Lemma S (a) and S1's reward order; by Lemma S (a), (M1κ) and (Aκ) when P(Ξ_t y2) = ∅, "L2b").
  (j) Corollary CHAIN-COUNT‴ (add3 §2; a REDUCTION to EXIT_x and D, both OPEN): for every q ∈ Q ∩ U_c ∖ {c}, the transitions of J that change
      κ(q) number at most Σ_{x ∈ Q ∩ U_c ∖ {c}} (|EXIT_x| + Σ_{x-pieces‴ π} (v_x(π) − 1)); if v_x(π) ≤ D for every x and π, at most Σ_x D·(|EXIT_x| + 1)
      (D ≥ 1 is implicit, a piece has a state; the sum forms are the sharper statements: N-OFF-6, F5).
- Not signed: OFFMONO §3-§5, add1 §4-§7, add2 §5-§7, add3 §3-§4 (READING / DATA / OPEN), as the packets asked; OFFMONO's Remarks (i), (ii)
  (READINGs; (iii) CHECKED by REFEREE); add2 §4's ODDC remark. Joint reading of add3 §3 (N-OFF-2 refined by OFFADD-N1, F5): the cycle cuts are
  no longer needed for the route; as NUMBERS, the stated / D forms of CHAIN-COUNT, CHAIN-COUNT′ and CHAIN-COUNT″ follow from CHAIN-COUNT‴'s sum
  form, the cut SUM forms of CHAIN-COUNT′ and CHAIN-COUNT″ do not (a cut sum bound is below ‴'s in 10 / 12 of 27,395 (q, J) pairs in REFEREE-2's
  data, e.g. tcS8_N9, J = 19..21: 39 against 55); those stand on their own proofs (signed). OFFMONO-N4, OFFADD-N2 and ADD2-N4 (the on-cycle
  CONJECTURE and the necessity of the cuts) are PROVED by add3's OFFSET-MONO⁺ (ADD3-N3 for the first two; REFEREE-2's §C for ADD2-N4; F3); OFFMONO's statement keeps its hypothesis as
  signed.
- Honest limits: (i) A REDUCTION, not a bound: the unit reduces the per-phase, per-class count of κ-changes to EXIT_x (exit changes) and D
  (offset values on a piece); both are OPEN and neither is addressed by the unit. ODDC_c is not bounded; ZCH-COUNT, FT-COUNT and TIE-CHARGE
  are true but no longer on the route (REFEREE-2 §4). Nothing here bounds ρ, N_ep, f, the phases or N5's running time. D is large where it
  matters: max D 69 on nep90_n40's phase against at most 72 κ-changes of one vertex (OFFMONO-N2, F13). (ii) READING (Lead), from L-SI's
  docs/si/N5-ALT-box23.md §8 (l-si 6ec0aa2b): a passive Odd READER (an appended Odd vertex o with no predecessors and edges into one class) can leave N5's run on the old vertices
  unchanged but raise L-SI's per-vertex and cut counts. REFEREE's R-N5-READER (e83fd19d; one referee): the unconditional invariance is FALSE
  (G-READ-1: S4b can move τ(o), splitting phases or cancelling a fallback; counterexample cex_reader.pg); Theorem READER-INV PROVED under (R),
  'τ(o) never moves at a transition at which τ is unchanged on the old vertices', which a dual-optimal start gives on any τ-constant stretch;
  l121reader_n41 reproduced with (R). For l121reader6_n46, (R) was not checked by a referee (READ-N2); L-SI's orcheck.py finds the run SAME
  and the phases equal there (DATA). On
  experiments/si/root/instances/l121reader6_n46.pg (sha1 29d2c84203f97bc247986d0af90778c5194d65a7, start
  7c6897065a63ce81e43c2355ac20980c81a3b515; long121_n40 plus six two-option readers, run on the old 40 vertices SAME) L-SI's exit-change count
  at cuts (its "EXIT_x") goes 23 → 41 (one reader) → 57 (six readers), its C-cuts K 53 → 57 → 73. L-SI's §8 concludes that bounding K(S) or ALT
  polynomially is at least as hard as bounding the phase length; the Lead reads the same for EXIT_x (READING, not proved: that L-SI's count is
  the unit's EXIT_x is not checked here), so the unit's reduction need not make the problem smaller (a phase is τ-constant, so REFEREE's Corollary, a dual-optimal start per
  τ-constant stretch, covers a whole phase: the reading is per phase, the unit's own scope). Related: CONJECTURE XR-LIN ("in every
  phase, every vertex's Ξ changes ≤ 2n times") is DEAD (L-SI, same §8): experiments/si/root/instances/l121reader_n41.pg (sha1
  084da8cd47707b8937ebe30fdfae88d3d988bdaf, start 7ca283c43b7092acc454c5ffc6b1995e3a29bf68), Ξ(o) changes 86 times in the phase [1, 122], > 2n =
  82; reproduced by a second engine (L-COMP experiments/xr-lin/, l-comp eabb3018: n5b SPEC only, run on 0..39 = long121_n40, phases equal,
  86, Oink zlk OK). (iii) Thin spots: Case L2a of (i) is exercised twice, both in REFEREE-2's saved instances docs/referee-2/R2-N5-OFFMONO/l2a/
  (r1814_6302_0.pg sha1 9c575fc9, r1813_619_1.pg sha1 fd6d95a4), strictly, and never in the lane's or REFEREE's data (0 of 9,390); Case L1 once in
  each referee's data (REFEREE: harm_n12_seed412, sha1 5282c3f1; REFEREE-2: once in its lib41 runs), never in the lane's (ADD3-N2 corrected by
  N-OFF-7, F12). The cycle cuts ZC_c, ZC″_c never bite in data (now explained by OFFSET-MONO⁺); FT-COUNT's factor 2 is never needed. (iv) (h) is
  CODE-LEVEL: it holds for si.py at e688b963, which SPEC S1 names as exact; si.py was executed only as the object, never as a checker (ADD2-N3).
- Data (DATA, not proof): REFEREE (successor 15 for OFFMONO and add1, successor 16 for add2 and add3; own engine rl_engine; lane code not run):
  OFFMONO (offmono_probe.py): library n ≤ 40 (870 files, 2,610 runs) 30,635 OFFSET-MONO checks (Case L 117), STEP1 112,498, CHAIN-SUM 34,641;
  3,000 random games (15,000 runs) 7,619; the lane's start files 455 / 390 / 363 (exact), parent changes 53 / 60 / 48 (OFFMONO-N1, F11);
  MUT=1 (p := par_t) 490 of 1,769, MUT=2 (opposite length sign) 1,308, MUT=3 (admit on-cycle q) 0 of 4,006. add1 (zch_probe.py): Z-CONST
  29,793 + 11,601; ZCH STRICT / TIE / CEVEN / ODDC 183 / 8 / 291 / 5 and 331 / 8 / 952 / 13; 806 + 565 ZC checks, 0 offset falls; MUT=1 (no ZC cut)
  0, MUT=2 Step A 1,271, MUT=3 (no EXIT cut) PM 422. add2 (add2_probe.py, 112,872 runs): si.py and rl_engine give the same (Ξ, σ̄) at 75,525
  states; PF-CHOICE at 29,141 pairs on both engines (1,506 κ-tied) plus 39,787 on rl_engine only (2,740 tied); TIE-CHARGE 62,181 checks, all
  1,184 STRICT and 36 TIE transitions in FT_c; ZC″ 1,054 cut checks, 0 falls; at most 7 F-touching changes per vertex per phase; MUT=1
  (reversed tie-break) 568, MUT=2 (FT-CONST asked at FT_c) 1,157 / 1,485 / 330. add3 (add3_probe.py, 103,872 runs): 9,390 on-cycle checks (L1 1,
  L2a 0, L2b 9,389); MUT=1 361 / 1,780, MUT=2 59 / 472. REFEREE-2 (successor 18, own offmono_check.py on its SPEC loop over si.py; lane code
  not run): 23,959 runs, 142,287 (phase, class) pairs; OFFSET-MONO 69,881 checks (Case L 138) and 44,966 more in the thin-spot search;
  OFFSET-MONO⁺ 4,049 (L1 1, L2 4,048 all with P(Ξ_t y2) = ∅) + 13,890 thin-spot (L2a 2, L1 0); CHAIN-SUM 73,930; Z-CONST 38,639; ZCH 1,562
  transitions (STRICT 459, TIE 14, CEVEN 1,060, ODDC 29); FT-COUNT 142,287 / FT-CONST 34,281; PF-CHOICE 315,088 (128,674 with ≥ 2 options);
  CHAIN-COUNT / ′ / ″ / ‴ 27,395 (q, J) pairs per form (cuts CYC 3,181, ZC 729, ZC″ 331), ‴'s sum form tight in 2,857; 0 violations of every
  check; controls bite (opposite sign 2,756; p := par_t 1,358; no EXIT cut 904; tie-break mutations 2,585 / 13,369 / 645), CTL_ft1 0. Both
  reproduce the lane's 455 / 390 / 363 checks and Case L 2 on long121_n40.
- Signatures: REFEREE docs/referee/R-N5-OFFMONO.md (report 04a563d3, successor 15): OFFSET-MONO, CHAIN-SUM, CHAIN-COUNT (as a REDUCTION)
  SIGNED, no gap; notes OFFMONO-N1..N4. R-N5-OFFMONO-add.md (c2a97189, successor 15): (CYC-ID), (CYC-SHAPE), Z-CONST, CHAIN-COUNT′ (Step A,
  both forms), ZCH-COUNT and its Corollary (as a REDUCTION) SIGNED, no gap; notes OFFADD-N1..N2. R-N5-OFFMONO-add2.md (d6e07396, stamp
  ff99f1f5, successor 16): (A-F), FT-COUNT, FT-CONST, CHAIN-COUNT″, PF-CHOICE and TIE-CHARGE (code-level) SIGNED, no gap; notes ADD2-N1..N4.
  R-N5-OFFMONO-add3.md (907e21b9, stamp d1a22e18, successor 16): OFFSET-MONO⁺, CHAIN-COUNT‴ SIGNED, no gap; notes ADD3-N1..N3. Unit §C at the
  end of R-N5-OFFMONO.md (96b2cd9a, successor 16; pointers in the three addendum reports). REFEREE-2 docs/referee-2/R2-N5-OFFMONO.md (report
  4e9a6372, §C c040084a, successor 18): every to-sign item of the four files SIGN, no gap; (CYC-ID), (CYC-SHAPE), (A-F) CORRECT; notes
  N-OFF-1..9. §C (both): verdicts identical; joint gap map EMPTY. N-OFF-1 (KEY's clause is about λ_U) ACCEPTED by REFEREE (F1); OFFMONO-N3
  matches REFEREE-2's premise column (F2); OFFMONO-N4, OFFADD-N2, ADD2-N4 PROVED by add3 (F3); ADD3-N1 agreed (F4); N-OFF-2 refined by
  OFFADD-N1, REFEREE withdrawing its add3 "follow" wording, N-OFF-6 compatible (F5); N-OFF-3, N-OFF-4, N-OFF-5 ACCEPTED by REFEREE (F6, F10,
  F7); ADD2-N2 consistent with REFEREE-2's step (F8); ADD2-N1 accepted by REFEREE-2, CORRECT (F9); OFFMONO-N1 confirmed by REFEREE-2, 53 / 60 / 48
  (F11); ADD3-N2 CORRECTED by N-OFF-7: L2a exercised twice (F12); OFFMONO-N2, N-OFF-8, ADD2-N3 data / method (F13); N-OFF-9 independence
  record (F14); nothing open. Quotes: all verbatim (REFEREE 12 / 15 / 23 / 9; REFEREE-2 55 / 55 after its §C, counting add1 12, add2 22). Both under the standing premise 1E-N3 (P1).
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (structural lemmas and a per-phase reduction; no iteration bound, no algorithm
  claim). GAPS G-N5-TIME: open.

### R76 [refereed-only] N5 on EVERY game, inside one phase: at an in-phase S4a step, a vertex z that migrates into the region R_u of a D-direct gate u (u ∈ DD_t ∩ DD_{t+1}, z ∉ R_u(t) ∪ A_t) has its first D_t-vertex u′ leave D (u′ ∉ D_{t+1}), or some Even vertex on z's play before u′ (z included) switches, and then z's play changes (Lemma MIG-SPLIT); so on a run S the transitions carrying such a migration into u number at most the transitions at which a vertex of D ∩ U_c leaves D plus those at which some z ∈ U_c changes its W-play (its Consequence); on every run S of in-phase S4a steps with λ_W constant, IF every unforbid-switch (k′, e) of S inside a global C-interval [a, b] has k′ − a < n − 1 (CONJECTURE UL_G, OPEN), THEN |U(S)| ≤ n_E((n − 1)(K(S) + 1) + K(S)) and every vertex's COARSE_{−1}(W) changes at most (n − 1)(1 + n_E((n − 1)(K(S) + 1) + K(S))) times on S, K(S) the number of C-cuts, global C-intervals read transition-locally (Corollary UL-RED, an implication); and in the abstract model ABS (steps to a pointwise greatest valid arena strategy), an acyclic run is fixed after at most its height ≤ n steps under the basic tie rule (Lemma ABS-HEIGHT) and after at most max over paths of Σ deg ≤ m steps under any deterministic tie rule (Lemma ABS-TIE), and in the cyclic model a vertex v with s_{t+2}(v) ≠ s_{t+1}(v) has a successor y with M_t(y) ≠ M_{t+1}(y), N_{t+1}(y) ≠ N_{t+2}(y) or a change of viability for v, or has s_{t+1}(v) ≠ s_t(v) (Lemma LOC′, any deterministic tie rule; without the last alternative, LOC, for tie rules that keep a maximal current choice) (2026-10-26) — structural lemmas and a conditional REDUCTION for N5, and settling lemmas in an abstract model (UL_G is a CONJECTURE and K(S) is not bounded; the model's link to N5 is a READING; LOC as stated, "any deterministic rule", is FALSE (G-GCX-1); not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C85.md, checker 85255772)
- Object (L-SI successor 17, Opus 5.5; frozen, unchanged during review): packet P-N5-GCX, docs/si/P-N5-GCX-box21.md, sha1
  5a91bebbc34f14be147da38adc1a6202407c70c2 (l-si freeze 02240121; quote base 7d87f9be). The referees' notes are collected by the lane in
  docs/si/P-N5-GCX-fixes-box21.md (l-si 652a574f, sha1 6a416c0ac0797922f8d45b2a70fe9e7d2d33c595, L-SI successor 19: F1-F8 for G-GCX-1,
  GCX-N1..N5, N-GCX-1..5; 29 quotes checked by script, experiments/si/rund/quotecheck.py "quotes=29 bad=0", pinned in experiments/si/check.sh);
  on trunk; repairs only, no signed statement changes except G-GCX-1's repair of LOC (F1). The statements below are in their repaired
  wording (F1-F6).
  Setting (every game): N5 = SPEC S1-S5 with FIX 1-4; a phase as in RESULTS R38 (a) KEY (λ_Ξ and τ constant); D_k as in RESULTS R55; W_k the
  (σ_k, τ)-play value (RESULTS R62 setting). A RUN S: consecutive states of one phase, all transitions S4a steps (no fallback); (ii) := λ_W
  constant on S; U(S) at level L = −1 as in RESULTS R67's setting (UNFORBID-SWITCHES). For a cycle node c, U_c := λ^{-1}(c); A_t := {z ∈ U_c : z's
  (σ_t, τ)-play meets no vertex of D_t}; R_u(t) := {z ∈ U_c : u is the first D_t-vertex of z's play}; DD_t := {u ∈ D_t ∩ U_c : σ̄_t(u), τ(u) ∈ A_t}
  (D-DIRECT gates); Δ_t(u) := M_t(τ u) − M_t(σ̄ u). An X-MIGRATION into u at t → t+1: z ∈ R_u(t+1) ∖ (R_u(t) ∪ A_t) with u ∈ DD_t ∩ DD_{t+1};
  X_u(S) := the transitions of S carrying one. A transition of S is GOOD if, for every c, A_{t+1} ⊆ A_t, D_{t+1} = D_t, DD_{t+1} = DD_t and
  Δ_{t+1}(u) = Δ_t(u) on DD_t; a GLOBAL C-INTERVAL is a maximal run of good transitions, a C-CUT a transition that is not good, K(S) their
  number (F2, GCX-N1 = N-GCX-2: under the packet's interval-level reading maximal intervals can overlap and UL-RED (a)'s count step fails,
  long121_n40 (experiments/red/n3/instances, sha1 c667c085), S = [31, 37]: two maximal intervals, K = 0). Model ABS (§4): non-terminals V
  (|V| = n), terminals t with h(t) ≤ T(t), weights w, values in a totally ordered abelian group; a valid strategy s reaches a terminal from
  every v; M_s, N_s add h, resp. T; ARENA Al_s(v) := {s(v)} ∪ {y ∈ succ(v) : M_s(y) > M_s(s(v))}; s′ := a valid arena strategy whose N is
  pointwise GREATEST among those (F6, GCX-N4), assumed to exist; ties broken by a deterministic rule R(arena, values, current choice); the
  BASIC rule keeps the current choice when it is a maximiser (a KEEP rule). Acyclic model: the digraph on V is acyclic.
- Claims signed (both referees "(Opus 5.5, D15)", L37); no item uses (P); premises LANDED: SPEC (definitions); RESULTS R38 (a) KEY; R55
  setting (D_k); R62 setting and (b) TC-CLASS (for the Consequence's u′ ∈ U_c, F3); R67 setting (run S, (ii), U(S)) and (f) CHARGE-U (for UL-RED (b), at L = −1); CHARGE-U rests on the standing premise 1E-N3 in its form
  P2 (RESULTS R67's premise line). (c)-(e) are self-contained in the model:
  (a) Lemma MIG-SPLIT (§2): let t → t+1 be an in-phase S4a transition and z an X-migration into u, with first D_t-vertex u′ (u′ ≠ u). Then (L)
      u′ ∉ D_{t+1}, or (S) some Even vertex w on the part π of z's play at t before u′ (z included) has σ_{t+1}(w) ≠ σ_t(w); in case (S) z's play
      changes (proof with the FIRST switching w, F4; on the play every Odd vertex follows τ, constant on the phase, F3). "(z included)" is
      needed (L-RED R93's cxmig_k: the only switcher is z; REFEREE's MUT=2 fails 28 of 28). Consequence: X_u(S) ≤ #{transitions of S at which
      some vertex of D ∩ U_c leaves D} + #{transitions of S at which some z ∈ U_c changes its W-play}; u′ ∈ U_c by RESULTS R62 (b) TC-CLASS, or
      because z's honest play and W-play agree up to the first D-vertex (GCX-N2 = N-GCX-1, F3).
  (b) Corollary UL-RED (§3; an IMPLICATION from CONJECTURE UL_G, under the transition-local reading, F2): premise UL_G: for every run S with
      (ii), every U event (k′, e) ∈ U(S) whose transition k′ → k′+1 lies in a global C-interval [a, b] has k′ − a < n − 1. Under UL_G, for every
      run S with (ii), n_E the number of Even vertices: (a) |U(S)| ≤ n_E·((n − 1)(K(S) + 1) + K(S)); (b) for every vertex x, COARSE_{−1}(W(x))
      changes ≤ (n − 1)(1 + n_E·((n − 1)(K(S) + 1) + K(S))) times on S (CHARGE-U with (a)).
  (c) Lemma ABS-HEIGHT (§4; acyclic model, basic tie rule): the run is fixed (s′ = s) after at most height ≤ n steps (height: longest path to
      a terminal, in vertices). The tie-rule hypothesis is needed (REFEREE: the one-vertex game below is acyclic and, under the rules "anti"
      or "sizedep", is fixed only after 2 steps at height 1).
  (d) Lemma ABS-TIE (§4; acyclic model, any deterministic tie rule): the run is fixed after at most max over paths of Σ deg(v) ≤ m steps. Its
      proof gives "v constant from t + deg(v) − 1" (N-GCX-3, accepted by REFEREE's §C; F5); the stated bound is unchanged.
  (e) Lemma LOC′ (§4 as repaired, G-GCX-1, F1; REFEREE-2's statement, signed by REFEREE in its §C; cyclic model, any deterministic rule): if
      s_{t+2}(v) ≠ s_{t+1}(v), then some successor y of v has M_t(y) ≠ M_{t+1}(y), or N_{t+1}(y) ≠ N_{t+2}(y), or changes VIABILITY for v (its
      play avoids v under s_{t+1} but not under s_{t+2}, or the reverse), OR s_{t+1}(v) ≠ s_t(v). LOC, the same without the last alternative,
      is signed by both for KEEP rules (R returns the current choice whenever it is a maximiser), the basic rule among them.
  Remarks MONO, MONO-SUCC, NO-RETURN (§4; not to-sign items): REFEREE CHECKED, REFEREE-2 SIGN (MONO's N-half with "greatest", F6).
- Not signed: LOC as stated, "(cyclic model; basic or any deterministic rule)": FALSE for "any deterministic rule" (G-GCX-1, found by both
  independently). Witness (REFEREE, scratch/loc_cex.py; REFEREE-2's is the same model under its rule "flip"): one non-terminal v, w(v) = 0,
  terminal successors a (h 0, T 0), b (h 1, T 5), c (h 2, T 5), s_0(v) = a; under the rules "anti" or "sizedep", s_1(v) = b and s_2(v) = c while
  every successor is a terminal (M, N constant, always viable). REFEREE's second repair class (rules current-independent and consistent
  under contraction) is REFEREE's alone; REFEREE-2 calls the repairs compatible. §5 (READING, CONJECTURES, OPEN, DEAD, DATA), as the packet
  asked: the READING that S4a on a pure global C-interval after A's freeze is the model's step (GCX-N3, F7: h_u's constancy follows from
  RESULTS R74 (b) FREEZE-A (b) and the constant Δ(u); the identification stays a READING); the OPEN lift (cycles in G_c, N5's own tie rule,
  impure intervals); CONJECTURES UL_G (OPEN), FINAL-EACH / ABS-CYC; CONJECTURE UL_C is DEAD (L-RED R91, reader_L; it is not UL-RED's premise:
  UL_G holds there with slack, both referees); DEAD box 21 (C-ONCE, UE-ONCE_C) and DEAD box 21b (the naive cyclic settling order, abscyc.py
  DEEP), docs/si/DEAD.md.
- Honest limits: (i) A conditional REDUCTION: UL-RED is an implication from UL_G, whose support where it could bite is thin (index / threshold
  at most 0.45: x32_waves48 21/47, reader_L40 40/95; N-GCX-4); only its arithmetic is new. K(S) (transitions at which some class's A grows,
  D or DD changes, or a D-direct offset changes) is not bounded; L-SI's passive readers raise L-SI's C-cut count without changing the run
  (DATA, fixes F8; RESULTS R75 honest limit (ii)). MIG-SPLIT bounds X_u by D-leaves and play changes, neither bounded here. (ii) (c)-(e) are
  about the model ABS; its link to N5 is the unsigned READING above. Which kind N5's S4a tie rule is stays OPEN, so a use of LOC for N5 must
  check that N5's rule keeps, or use LOC′; LOC is used by no signed item. (iii) Thin: MIG-SPLIT is exercised at 298 migrations in REFEREE-2's
  data, most on constructed families (N-GCX-4). Nothing here bounds N5's running time.
- Data (DATA, not proof): REFEREE (successor 16; own gcx_probe.py on its engine rl_engine, abs_model.py; lane code not run): library 1,140
  files (2,739 runs; MIG-SPLIT 223 checks: (L) only 134, (S) only 84, both 5), lib41 (1,130 runs; 30), L-RED's ul instances (48 runs; 40, all
  (S)), 9,000 + 4,500 random 𝒞^kO runs; UL_G held in every run; 0 failures of every signed check; model: 60,000 acyclic runs (6 rules),
  ABS-HEIGHT's bound attained, 15 runs (non-keep rules) fixed after their height (GCX-N5); LOC fails only under non-keep rules, LOC′ 0
  failures in 25,503 change events (§C); controls MUT=1 and MUT=2 fail 28/28, MUT=4 on all 3 reader runs (MUT=3 does not bite). REFEREE-2
  (successor 18; own gcx_check.py on its SPEC loop over si.py, abs_check.py; lane tools not run): 22,592 N5 runs, 5,193 runs S; MIG-SPLIT 298
  migrations ((L) 83, (S) only 215), Consequence 69 (u, S) pairs, C-intervals disjoint in 5,193 runs (5,687 intervals, 4,327 cuts), UL_G 1,187
  U events inside intervals, UL-RED (a) 5,193, (b) 128,361 vertex-runs: 0 violations; model 150,000 acyclic and 97,065 cyclic runs: LOC
  (non-basic) 166 failures, LOC′ and the other model checks 0. Both: nep90 / nep76 migrations all case (L), cxmig_k all case (S).
- Signatures: REFEREE docs/referee/R-N5-GCX.md (report e01bdec6, §C 4aa7cc2f, stamp corrected 159c8f04; successor 16): MIG-SPLIT and its
  Consequence (with TC-CLASS), UL-RED (a), (b) (conditional, transition-local reading), ABS-HEIGHT, ABS-TIE SIGNED; LOC SIGNED for keep rules,
  NOT as stated (G-GCX-1); LOC′ SIGNED in §C; notes GCX-N1..N5. REFEREE-2 docs/referee-2/R2-N5-GCX.md (report fe04ca32, §C fc63f1f1; successor
  18): the same items SIGN, LOC for the basic rule only (G-GCX-1), LOC′ SIGN; notes N-GCX-1..5. §C (both): verdicts identical; joint gap map
  {G-GCX-1}, with two compatible repairs; GCX-N1 = N-GCX-2, GCX-N2 = N-GCX-1, N-GCX-3 ACCEPTED by REFEREE; nothing open.
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (structural lemmas, a conditional reduction and abstract-model lemmas; no
  running-time bound, no algorithm claim). GAPS G-N5-TIME: open.

### R77 [refereed-only] N5 on EVERY game, inside one phase: on states [a, b] of one phase on which every transition is an S4a step and τ, λ, λ_W are constant (H1), σ̄ is constant (H2), the honest and the W-cycles are the same cycles and constant (H3), the end-state graph H_b is acyclic off the cycle vertices (H4), and distinct W-plays from a vertex have distinct W-valuations (GEN_W), every non-cycle vertex v has its end-state W-play and honest play from state a + d*(v) on, so σ_t = σ_b on [a + max d*, b] and b − a ≤ max d* ≤ n − 1 (Theorem STATIC-DEPTH); if every gate is D-direct at b, then (H4) holds and every cycle at b is common to both frames (Corollary PURE-END); hence b − a ≤ n − 1 on a global C-interval of a λ_W-constant fallback-free in-phase run on which σ̄ is constant and (H3), (H4), GEN_W hold (Corollary GCI-LEN-ρF; its proof does not use the C-interval structure); and in the cyclic abstract model ABS of RESULTS R76, N never falls along the run (Fact N-MONO) and, if distinct plays from a vertex have distinct N-values (GEN), every vertex v holds its final play from step d*(v) on, so the run is fixed within max d* ≤ n steps under any deterministic tie rule (Theorem ABS-DEPTH) (2026-10-26) — structural lemmas for N5 and a settling theorem in an abstract model (only intervals with σ̄ constant, (H3), (H4) and GEN_W are bounded, and their number is not; the length bound is global, not per class; CONJECTURE ABS-DEPTH-TIE is DEAD for general tie rules; not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C86.md, checker 0f71e023)
- Object (L-SI successor 18, Opus 5.5; frozen, unchanged during review): packet P-N5-DEPTH, docs/si/P-N5-DEPTH-box22.md, sha1
  549c7fb72d767293b6bf2ae5bbbb8809084df707 (l-si freeze 2201aa2d). The referees' notes are collected by the lane in
  docs/si/P-N5-DEPTH-fixes-box22.md (l-si 96bde5f3, sha1 67724abe21b87eea46b7e38b1cef7de1290c542d, L-SI successor 19: F1-F5 for DEPTH-N1..N4,
  N-DEPTH-1..5; 14 quotes checked by script, experiments/si/rund/quotecheck.py "quotes=14 bad=0", pinned in experiments/si/check.sh); on
  trunk; repairs only, no signed statement changes; joint gap map EMPTY. The statements below are in their repaired wording (F1, F3, F4).
  Setting (every game): N5 = SPEC S1-S5 with FIX 1-4. Ξ_t(v): the S1 valuation (c, P, ℓ) of v's honest play (σ_t, σ̄_t); W_t(v): that of v's
  (σ_t, τ)-play. D_t := {Odd u : σ̄_t(u) ≠ τ(u)}; A_t := the vertices whose (σ_t, τ)-play meets no vertex of D_t; a gate u ∈ D_t is D-direct if
  σ̄_t(u), τ(u) ∈ A_t. H_b: edges v → σ_b(v) (Even v), v → τ(v) (Odd v ∉ D), u → τ(u) and u → σ̄(u) (u ∈ D); cycle vertices are sinks. d*(v) := 0
  on cycle vertices, 1 + d*(σ_b v) (Even), d*(τ v) (Odd v ∉ D), max(d*(τ u), d*(σ̄ u)) (u ∈ D): the non-cycle Even vertices on a longest
  H_b-path from v, so d*(v) ≤ n − 1. Model (§1): ABS as in RESULTS R76's setting on any digraph, "pointwise maximal" read as pointwise GREATEST
  (F1, DEPTH-N1 = N-DEPTH-1); play_t(v) := v's play under s_t; s* the fixed point; d*(v) := the non-terminals on v's play under s*; GEN: for
  every v, distinct plays from v have distinct N-values.
- Claims signed (both referees "(Opus 5.5, D15)", L37); no item uses (P); premises LANDED: SPEC S1 (valuation and order), S4a (arena
  {σ(v)} ∪ Iσ(v); Even's one-player optimum), S4c (FALLBACK); RESULTS R18 (d) Lemma S (a), every game by R57 (a), on S4a's arena: the standing
  premise 1E-N3 in its form P2 (as listed in RESULTS R69); (SW) as listed among RESULTS R72's landed premises; R56 (a) (M1κ), (M2κ); R69 (d)
  Lemma STATIC (only for (H2)'s parenthetical); and RESULTS R76's model ABS and global C-interval (definitions only; R76 is not yet in
  docs/RESULTS.md at trunk e3bd64e3 and lands before R77):
  (a) Fact N-MONO (§1): N_{t+1} ⪰ N_t for every t ≥ 0, hence N_t ⪯ N* := N_{s*} (s_t is a candidate; s_{t+1}'s N is pointwise greatest, F1).
      (MONO), (MONO-SUCC), (TERM): REFEREE CHECKED, REFEREE-2 CORRECT.
  (b) Theorem ABS-DEPTH (§1; cyclic model, under GEN): for every v and every t ≥ d*(v), play_t(v) = play*(v); hence the run is fixed after at
      most max_v d*(v) ≤ n steps. The induction runs on the final forest; neither step looks at the tie rule (REFEREE: any deterministic rule).
  (c) Theorem STATIC-DEPTH (§2; N5, every game): on states [a, b] of one phase with (H1) every transition an S4a step (no fallback), τ, λ and
      λ_W constant; (H2) σ̄_t = σ̄_a on [a, b]; (H3) at every t the W-cycles and the honest cycles are the same cycles, constant on [a, b]; (H4)
      H_b acyclic outside the cycle vertices; and GEN_W (for every v, different W-plays from v to the same cycle have different W-valuations):
      every non-cycle v has, at every t ∈ [a + d*(v), b], the same W-play and the same honest play as at b; hence σ_t = σ_b on [a + max d*, b]
      and b − a ≤ max_v d*(v) ≤ n − 1. Facts used as proof steps (REFEREE ✓, REFEREE-2 CORRECT): (W-MONO) W_{t+1} ⊵ W_t (P2), (Ξ-SUCC)
      Ξ_t(σ_t v) non-decreasing ((M2κ), (SW)), (CV) cycle vertices constant ((H1), (H3)). Remark (N-DEPTH-2, ACCEPTED by REFEREE; F4): the
      per-vertex settling restricts to any set of vertices closed under H_b-successors; the length conclusion is global (it uses that σ is
      unchanged on the whole game, then S4c's fallback), and a per-class length bound does not follow.
  (d) Corollary PURE-END (§2): if every gate is D-direct at b, then (H4) holds, and every cycle at b is common to both frames. ((H3)'s
      constancy on [a, b] remains a hypothesis.)
  (e) Corollary GCI-LEN-ρF (§3): let [a, b] be a global C-interval of a λ_W-constant fallback-free run in one phase on which σ̄ is constant,
      (H3) and (H4) hold (by (d), (H4) holds if every gate is D-direct at b), and GEN_W holds; then b − a ≤ n − 1. The proof does not use the
      global C-interval structure: the bound holds for every interval of a λ_W-constant fallback-free in-phase run on which σ̄ is constant and
      (H3), (H4), GEN_W hold (DEPTH-N3, accepted by REFEREE-2; F3).
- Not signed: §4 (the instance showing GEN is needed for ABS-DEPTH's per-vertex form: at state 1 vertex 2 has N = N*(2) = 2 on the play
  2 → 0 → 1 → t5, not its final play 2 → t4; the run still ends within max d* = 3; confirmed by both), §5 (data), §6 ((G1)-(G4), CONJECTURE
  STATIC-DEPTH-TIE (OPEN, untouched), the READING), as the packet asked. CONJECTURE ABS-DEPTH-TIE ("in the model, the run is fixed within max d*
  steps without GEN") is DEAD for general deterministic rules (DEPTH-N2 = N-DEPTH-3, F2; not yet in docs/si/DEAD.md at trunk e3bd64e3).
  Obstruction: after the arena shrinks a non-keep rule may leave a current maximiser (the mechanism of G-GCX-1, RESULTS R76). Witnesses:
  REFEREE, R76's one-vertex LOC game (non-GEN, max d* = 1, fixed only after 2 steps under "anti" or "sizedep"); REFEREE-2, non-terminals 0, 1,
  terminals T2 (h 0, T 2), T3 (h 2, T 2), succ(0) = {T2}, succ(1) = {0, T2, T3}, w = (−2, −1), start s(1) = 0, rule "flip": s(1) = 0 → T2 → T3,
  fixed after 2 steps against max d* = 1. Restated (OPEN): CONJECTURE ABS-DEPTH-TIE_keep, for tie rules that keep a maximal current choice (no
  overrun under keep rules in either referee's data).
- Honest limits: (i) STATIC-DEPTH bounds only intervals with σ̄ constant, (H3), (H4) and GEN_W, and the number of such intervals is not
  bounded: GCI-LEN-ρF covers 3,499 of 4,747 global C-intervals in REFEREE-2's corpus (479 with a σ̄ change, (G1); 766 without (H3)) (N-DEPTH-5).
  (G1)-(G4) stay OPEN. (ii) The length conclusion is global ((c)'s Remark): it does not give a per-class length (this is what breaks the
  companion packet's PURE-LEN, G-DADD-1). (iii) GEN_W: SPEC breaks S4a ties by the S1 procedure on the current arena, so GEN_W has no
  automatic substitute ((G4)); REFEREE-2's used-form check failed in 13 intervals, all with the conclusion intact (N-DEPTH-4); REFEREE saw
  none. (iv) (a), (b) are about the model ABS; its link to N5 is a READING (RESULTS R76). (v) The bound is attained: length = max d* in 920
  intervals (REFEREE, DEPTH-N4) and 651 (REFEREE-2). Nothing here bounds N5's running time.
- Data (DATA, not proof): REFEREE (successor 16; own abs_depth.py on abs_model.py, depth_probe.py on its engine rl_engine; lane code not run):
  model, 3,246 + 1,794 GEN runs, 12,798 + 6,876 per-vertex checks, 0 failures; N-MONO 0 failures; non-GEN runs later than max d* 8 + 10, all
  under non-keep rules; MUT=1 612. N5: library 1,140 files (2,739 runs; 8,918 STATIC-DEPTH intervals, 4,263 with gates; 512,278 per-vertex
  checks), lib41 (1,130 runs; 6,667 intervals), 9,000 random 𝒞^kO runs (1,059), named instances (184); PURE-END 19,361 / 13,427 / 16,583 / 213
  states; GCI-LEN-ρF 2,046 / 1,313 / 960 / 35 intervals; 0 failures; MUT=1 3,010. REFEREE-2 (successor 18; own absdepth_check.py,
  depth_check.py on its SPEC loop over si.py; lane tools not run): model 36,711 + 37,449 + 60,000 runs, N-MONO and ABS-DEPTH 0 violations
  where GEN holds, non-GEN overruns 9 / 18 / 7 only under non-keep rules; N5 21,775 runs: STATIC-DEPTH 53,113 intervals (17,348 with gates;
  longest 55 on x32_rand64, n 64, max d* 56), PURE-END 18,339 states, GCI-LEN-ρF 3,499 intervals, 0 violations. Both reproduce the §4 run,
  b6_xs 21 / 29 / 36 at n = 24, 32, 40, and x32_waves48 26 (the longest with gates).
- Signatures: REFEREE docs/referee/R-N5-DEPTH.md (report 1d74c963, §C f5081a6a, stamp corrected dc4e47b8; successor 16): N-MONO (greatest
  reading), ABS-DEPTH, STATIC-DEPTH, PURE-END, GCI-LEN-ρF SIGNED, no gap; §4 instance CONFIRMED; notes DEPTH-N1..N4. REFEREE-2
  docs/referee-2/R2-N5-DEPTH.md (report dad93591, §C d8402f3d; successor 18): the same items SIGN, no gap; notes N-DEPTH-1..5. §C (both):
  verdicts identical; joint gap map EMPTY; DEPTH-N1 = N-DEPTH-1, DEPTH-N2 = N-DEPTH-3, DEPTH-N3 accepted by REFEREE-2, N-DEPTH-2 and N-DEPTH-5
  ACCEPTED by REFEREE, N-DEPTH-4 a corpus difference; nothing open.
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (structural lemmas bounding the intervals they cover, and an abstract-model
  theorem; no running-time bound, no algorithm claim). GAPS G-N5-TIME: open.

### R78 [refereed-only] N5 on EVERY game, inside one phase (the packet's conditional premises, now landed in RESULTS R74, R75 and R77; R78 depends on R77 and lands after it): on a pure per-class C-interval [a, b] of class c (every gate of U_c D-direct at every state), a change of a gate's choice from y1 to y2 at t → t + 1 with a + L ≤ t < b, L := max(|A_a| − 1, 0), and y1 ∈ A_{t+1} leaves M(y1) unchanged and strictly raises κ(y1), in its length component alone, unless κ_{t+1}(y1) = κ_{t+1}(y2) (Lemma GATE-PUSH), so the transitions of [a + L, b] with a σ̄ change in U_c number N_σ̄ ≤ Σ_{u ∈ D ∩ U_c} deg(u)(|U_c| − 2) + |A_a| + TIES_c (its Count; both rest on proof alone); under GEN_W on U_c, the transitions of [a, b] at which some Even vertex of U_c switches number at most L + (1 + N_σ̄ + N_cyc)(|U_c| − 1) + N_σ̄ + N_cyc, N_cyc the transitions changing c's cycle (Proposition PURE-LEN′, replacing the false length bound PURE-LEN); for z ∈ U_c ∖ {c} and m ∈ T, m ≠ z, at or before the first visit of c on z's honest (t+1)-play, with the Q-vertices from z (included) to m (excluded) on no honest cycle at t, the offset off(z; m) does not fall at an in-phase transition t → t + 1 (Lemma MONO-REF); and an Even w ∈ U_c ∖ {c} that switches a → b at t → t + 1 does not switch back to a at t′ → t′ + 1 if a's class exit path and exit e1 are unchanged on [t, t′] and e1 lies at or before the first c on w's honest play at every state of [t + 1, t′], with MONO-REF's no-cycle hypothesis (Lemma E-ONEWAY) (2026-10-26) — structural lemmas and a REDUCTION for N5 (TIES_c, ODDC_c and the length of a per-class pure C-interval are not bounded; GATE-PUSH is never exercised; E-ONEWAY's e1-after-c case is OPEN; not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C87.md, checker d0b32277)
- Object (L-SI successor 18, Opus 5.5; frozen, unchanged during review): packet P-N5-DEPTH-add, docs/si/P-N5-DEPTH-add-box22.md, sha1
  4d51aa5ea4e1a1d145da4cb825deab75198abae7 (l-si freeze aa6061d1; quote base 78bc0e6a8), the CONDITIONAL companion of P-N5-DEPTH (RESULTS R77).
  The referees' notes are collected by the lane in docs/si/P-N5-DEPTH-add-fixes-box22.md (l-si 96bde5f3, sha1
  a1ab7bfb3ac9308178374993ccb0ed9d8f562be8, L-SI successor 19: F1-F5 for G-DADD-1, G-DADD-2 (G-DADD-3 folded in), DADD-N1..N3, N-DADD-1..3; 20
  quotes checked by script, experiments/si/rund/quotecheck.py "quotes=20 bad=0", pinned in experiments/si/check.sh); on trunk; repairs only:
  PURE-LEN is replaced by PURE-LEN′ (F1), MONO-REF and E-ONEWAY gain their "before c" hypotheses (F2, F3). The statements below are in that
  repaired wording.
  Setting (every game): N5 = SPEC S1-S5 with FIX 1-4; a run S and D_t, DD, Δ as in RESULTS R76's setting. Fix a cycle node c, U := U_c.
  A_t := F_D(t) ∩ U_c (RESULTS R74's setting); M := the path-weight component of κ; κ, κwt_c, Y^q_t as in RESULTS R56 (κ-Y-FORM_D); Q, T := (Q ∩
  U) ∪ {c}, par and off_s(z; m) := κ_s(z) − κ_s(m) as in RESULTS R75's setting. A PER-CLASS C-INTERVAL of S: a maximal run of transitions with,
  for class c alone, A_{t+1} ⊆ A_t, D ∩ U_c constant and Δ constant on its D-direct gates (R76's transition-local reading, REFEREE §1); PURE if
  every gate of U_c is D-direct at every state. L := max(|A_a| − 1, 0). TIES_c: the gate switches with κ_{t+1}(y1) = κ_{t+1}(y2); N_cyc: the
  transitions changing c's cycle (≤ (n − 1)|U_c| + TIE_c + ODDC_c per phase, RESULTS R75 (e) ZCH-COUNT). For Even w switching a → b: e1 := the
  exit of a (the first T-vertex on a's play), π_a := a's class exit path.
- Claims signed (both referees "(Opus 5.5, D15)", L37); no item uses (P); premises LANDED (the packet's CONDITIONAL premises included), except
  R76 (definitions) and R77, which are not yet in docs/RESULTS.md at trunk e3bd64e3 and land before R78: RESULTS
  R56 (a) (Aκ), (M1κ), (M2κ) and (d) κ-Y-FORM_D; (SW) as listed among RESULTS R72's landed premises; R74 (b) FREEZE-A (b), and for the Count
  the lengths of Ξ on A in [1, |U_c| − 1] (the packet cites (R-LEN) in the ROOT packet's sentence about Ξ on A_t, which RESULTS R74 (b) records as
  true; both referees check the Count from FREEZE-A (b), (M2κ) and those lengths; Lead reading for the landing: the sentence follows from
  R74 (b) (M constant on A_t from a + L) with R56 (a) (INJ) and the common cycle node c, so the path set is fixed and only the length can change;
  R74's (R-LEN) count itself is not the step used); R75 (a) OFFSET-MONO and its Step 1, (e) ZCH-COUNT; R77 (c)
  STATIC-DEPTH with its Remark (per-vertex settling restricted to a set closed under H_b-successors, F4 of P-N5-DEPTH's fixes) and (d)
  PURE-END. Through them, the standing premise 1E-N3 (P1 via R56 (d) and R75 (a), P2 via R77 (c)):
  (a) Lemma GATE-PUSH and its Count (§1): let [a, b] be a pure per-class C-interval of class c, a + L ≤ t < b, and let σ̄ change at a gate u ∈
      D ∩ U_c from y1 to y2 at t → t+1, with y1 ∈ A_{t+1}. Then M_{t+1}(y1) = M_t(y1) and κ_{t+1}(y1) ≻ κ_t(y1) (a rise of the length component
      only), unless κ_{t+1}(y1) = κ_{t+1}(y2). Count: N_σ̄ := the transitions of [a + L, b] with a σ̄ change in U_c satisfy N_σ̄ ≤ Σ_{u ∈ D ∩ U_c}
      deg(u)·(|U_c| − 2) + |A_a| + TIES_c.
  (b) Proposition PURE-LEN′ (§2 as repaired, G-DADD-1, F1; signed by both): for a pure per-class C-interval [a, b] of class c, under GEN_W on
      U_c, the transitions of [a, b] at which some Even vertex of U_c switches number ≤ L + (1 + N_σ̄ + N_cyc)·(|U_c| − 1) + N_σ̄ + N_cyc. (At most
      L before a + L; cut [a + L, b] at every σ̄ change in U_c and every change of c's cycle; on each piece STATIC-DEPTH's per-vertex settling
      restricted to U_c puts every Even switch of U_c in the piece's first max_{U_c} d* ≤ |U_c| − 1 transitions. No step uses that the pieces
      are adjacent or that a frozen class stays frozen.)
  (c) Lemma MONO-REF (§3 as repaired, G-DADD-2, F2): let t → t+1 be in-phase, z ∈ U ∖ {c}, and m ∈ T on z's honest (t+1)-play, m ≠ z, with m AT
      OR BEFORE the first visit of c on that play; suppose the Q-vertices of that play from z (included) to m (excluded) are on no honest
      cycle at t. Then off_{t+1}(z; m) ⪰ off_t(z; m).
  (d) Lemma E-ONEWAY (§3 as repaired, G-DADD-2 with G-DADD-3 folded in, F3): let Even w ∈ U ∖ {c} switch a → b at t → t+1, with a's class
      exit path π_a and exit e1 ∈ T unchanged on [t, t′], and let e1 lie AT OR BEFORE the first c on w's honest play at every state of
      [t + 1, t′], with MONO-REF's no-cycle hypothesis. Then w does not switch back to a at t′ → t′ + 1.
- Not signed: PURE-LEN as stated, "b − a ≤ L + (1 + N_σ̄ + N_cyc)·(|U_c| − 1) + N_σ̄ + N_cyc": FALSE (G-DADD-1; it uses STATIC-DEPTH's global
  length step per class, RESULTS R77 (c)'s Remark). Witness (both): pure_22 (experiments/new/box22/instances/pure_22.pg, sha1 f7ba3897, n = 22)
  at its S3 start, class 10, U_c = {4, 9, 10}, interval [23, 33]: bound 4, b − a = 10, while Even vertices of other classes switch at every
  transition; REFEREE-2 also reader40_plus2 (docs/referee-2/R2-N5-DEPTH/union/, sha1 8b233aa5; [0, 41] against bound 2), kw25_n32 ([0, 25],
  bound 4) and ccl_w48_n48 ([1, 27]). REFEREE's POSITION form ("every Even switch of U_c lies before a + bound") is WITHDRAWN as a repair (data
  only); its missing step, that a frozen class stays frozen (REFEREE-2 §C C2), is not proved. MONO-REF as stated (any m ∈ T on z's play):
  FALSE for m after c (G-DADD-2). Witnesses: frzh3n_701_best (experiments/n5-exhaustive/results/box9b/, sha1 6de40c62, n = 8) at its S3 start,
  t = 1, c = 2, z = 0, m = 4: off(0; 4) falls from (0, 1) to (0, 0) (REFEREE); b4_theta_n7 (experiments/n5-exhaustive/instances/, sha1
  5627745306a45f1a98387c53bba40065375acd5e) from docs/referee-2/R2-N5-DEPTH/mr/b4_theta_n7_mrafter.start, c = 1, z = 3, m = 6: off(3; 6) falls
  from (0, −2) to (0, −3) (REFEREE-2). E-ONEWAY as stated ("e1 on w's honest play"): the case e1 after c is not reached by the proof and is
  OPEN (DADD-N3; REFEREE-2's G-DADD-3); it held in 704 (REFEREE) and 711 (REFEREE-2) windows, 0 returns. DADD-N2 = N-DADD-1: with RESULTS R75
  (i) OFFSET-MONO⁺ the no-cycle hypothesis can be dropped, the before-c restriction stays (a premise alternative, not adopted, F2). §4 (data).
- Honest limits: (i) A REDUCTION: PURE-LEN′ counts the Even-switch transitions of U_c, not the interval's length, which is not bounded by
  class quantities (pure_22, reader40_plus2). Its bound is in N_σ̄ and N_cyc, bounded by (a)'s Count and ZCH-COUNT only up to TIES_c, TIE_c and
  ODDC_c: TIES_c and ODDC_c are not bounded (ZCH-COUNT's TIE_c is bounded per phase only code-level, RESULTS R75 (h)). (ii) PROOF ALONE: (a)
  and its Count are never exercised (0 qualifying σ̄ changes; REFEREE 7,295 pure per-class intervals, 2,492 with gates; REFEREE-2 1,398 pure
  intervals with gates; DADD-N1 = N-DADD-2, F4). The packet's §4 PURELATE line is about Even switches: it supports PURE-LEN′, not PURE-LEN
  (F4). (iii) MONO-REF fails after c (REFEREE 1,527 of 29,786 checks with m after c; REFEREE-2 610 of 43,388); L-SI's working-note statements
  in docs/si/N5-EXIT-box22.md §1-§2 that used it unrestricted carry G-DADD-2's hypothesis from now on (F2). (iv) Order: R78 rests on R77 (c),
  (d) and lands after it. Nothing here bounds N5's running time.
- Data (DATA, not proof): REFEREE (successor 16; own dadd_probe.py on its engine rl_engine; lane code not run): library 1,140 files (2,739
  runs), lib41 (1,130), 9,000 random 𝒞^kO runs, named instances (18 runs); MONO-REF with m at or before c 1,411,999 checks, 0 failures;
  E-ONEWAY 184,217 window checks, 0 switch-backs; 7,295 pure per-class intervals: PURE-LEN as stated fails in 1,140, all with class c frozen,
  the class-local form 0 failures. REFEREE-2 (successor 18; own depth_check.py and mkunion.py; lane tools not run; 21,775 N5 runs): GATE-PUSH's
  Count 6,742 intervals, 0; PURE-LEN as stated 1,326 FAIL of 6,742; PURE-LEN′ 0 of 6,742; MONO-REF with m at or before c 1,087,965 checks, 0;
  E-ONEWAY with e1 at or before c 63,065 checks, 0 returns. Both: MONO-REF failures only after c, PURE-LEN failures all frozen.
- Signatures: REFEREE docs/referee/R-N5-DEPTH-add.md (report f4b54c43, stamp c9bdfa68; §C f5081a6a, stamp corrected dc4e47b8; successor 16):
  GATE-PUSH and its Count SIGNED (never exercised); PURE-LEN NOT SIGNED (G-DADD-1), PURE-LEN′ SIGNED in §C (with REFEREE-2); MONO-REF NOT SIGNED
  as stated (G-DADD-2), SIGNED with "m at or before the first visit of c"; E-ONEWAY SIGNED with the matching hypothesis; position form
  withdrawn; notes DADD-N1..N3. REFEREE-2 docs/referee-2/R2-N5-DEPTH-add.md (report dad93591, §C d8402f3d; successor 18): GATE-PUSH SIGN;
  PURE-LEN FALSE AS STATED (G-DADD-1), PURE-LEN′ SIGN; MONO-REF SIGN with the before-c scope (G-DADD-2); E-ONEWAY SIGN with e1 at or before c
  (G-DADD-3); notes N-DADD-1..3. §C (both): no disagreement on any verdict; joint gap map {G-DADD-1, G-DADD-2}, G-DADD-3 folded into G-DADD-2;
  the PURE-LEN repair is the COUNT form; DADD-N1 = N-DADD-2, DADD-N2 = N-DADD-1, N-DADD-3 ACCEPTED; nothing else open.
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (structural lemmas and a per-interval reduction; no running-time bound, no
  algorithm claim). GAPS G-N5-TIME: open.

### R79 [refereed-only] N5 on EVERY game, inside one phase: a run J = (x, …, y) of a phase depends only on the Odd edges it uses — on every Odd cut H of G (G's Even successor lists, each Odd list a non-empty subset of G's) that contains τ and every Odd best reply σ̄_k, k ∈ J, RESULTS R64 (a) (i)-(iv) hold at each state of J (Lemma RESTRICT_H), and N5^τ on H from (σ_x, τ) passes through (σ_x, τ), …, (σ_{y′}, τ), y′ := x + len(J), with N5's fallback / non-fallback type at each transition, the states of J in one N5^τ phase and the last transition may leave it unless σ̄_{y′} is an Odd strategy of H (Corollary REPRO_H, with EPR-1); instances: the epoch game G′_E (RESULTS R64), G^u (RESULTS R68 (f)), the frozen-side game G^{u|J}, which proves N5-NCONF §9's CONJECTURE RESTRICT_{u|J}, and the used-edge game G^P of a whole phase P, of which P is the initial segment, of len(P) transitions, of the first N5^τ phase on G^P started at (σ_x, τ) (G-RESTRICT-1 repaired) (2026-10-26) — structural lemmas for N5 (they bound nothing: no phase length is bounded, QP(P) and XDEG(P) are OPEN; not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C88.md, checker 7f59a4f9)
- Object (L-NEW successor 28, Opus 5.5; frozen, unchanged during review): packet P-N5-RESTRICT, docs/new/P-N5-RESTRICT-box48.md, sha1
  48c63a8e45c0288678805195a91f9c00ee703da9 (l-new freeze 7e56744a; quote base 08abd9cb), the proof of RESULTS R64 (a), (b) (packet P-N5-EPR
  §1-§2, sha1 8fecca79) carried from G′_E to any admissible Odd cut; source docs/new/N5-NCONF-box48.md §9-§10 at 7b5876d8. The referees' notes
  are collected by the lane in docs/new/P-N5-RESTRICT-fixes-box48.md (l-new a99dee17, sha1 f33f00b36ab5626e7ccd24e3b2fdd75ca56b2764, L-NEW
  successor 30: F1-F6 for G-RESTRICT-1 = G-R2-RESTRICT-1, RESTRICT-N1..N3, N-RESTRICT-1..3 and a data correction; 31 quotes checked by script,
  experiments/new/box49/quotecheck3.py "quotes=31 bad=0", pinned in experiments/new/check.sh with a shifted-line control and the file's sha1);
  on trunk; repairs only: §2's G^P sentence is replaced by the joint repair (F1); F2, F5 correct unsigned READINGs; F3, F4, F6 change no
  statement. The statements below are in that repaired wording.
  Setting (every game): N5 = SPEC S1-S5 (FIX 1-4, Q1-Q4); state k = (σ_k, τ_k); σ̄_k := S1's Odd counterstrategy to σ_k; Ξ_k := V_{σ_k,σ̄_k};
  W_k := V_{σ_k,τ_k}; λ := Ξ's cycle-node map; phases as in RESULTS R38 (a) (τ constant inside one); Q := the Odd vertices of out-degree ≥ 2;
  N5^τ as in RESULTS R64's setting (S4b^τ keeps τ when Iτ ≠ ∅ and τ is value-optimal against σ in S4b's arena). An ODD CUT of G: a game H
  with G's vertices, priorities, owners and Even successor lists, every Odd v keeping a non-empty succ_H(v) ⊆ succ_G(v); SPEC's objects on H
  are primed. A run J = (x, …, y) of consecutive states of one phase is H-ADMISSIBLE if τ(v) ∈ succ_H(v) and σ̄_k(v) ∈ succ_H(v) for every Odd
  v and k ∈ J; len(J) := (y − x) + [1 if y → y + 1 is in-phase]. Instances: G′_E with an epoch E (RESULTS R64's setting); G^u with a u-run
  (RESULTS R68's setting); for a FROZEN-SIDE u-STRETCH J (a maximal run of a phase with σ̄ constant on Q ∖ {u}), D⁻ := {v ∈ Q ∖ {u} :
  σ̄_J(v) ≠ τ(v)} and G^{u|J}: v ∈ D⁻ cut to {τ(v), σ̄_J(v)}, every other Odd v ≠ u to τ(v), u keeping all its edges; for a phase P, the
  USED-EDGE game G^P: every Odd v cut to {τ(v)} ∪ {σ̄_k(v) : k ∈ P}; QP(P) := #{Odd v : |succ_{G^P}(v)| ≥ 2}, XDEG(P) := Σ_v (|succ_{G^P}(v)| − 1).
- Claims signed (both referees "(Opus 5.5, D15)", L37), on every game; no item uses (P); premises LANDED: SPEC S1-S5 (S1's injective rewards
  included); RESULTS R18 (d) Lemma S (a) (= (VJ), signed on every game in RESULTS R57 (a)), on G, on H and on S4b's arenas; R38 (a); R64 (a),
  (b) with the repair EPR-1, and their proof (P-N5-EPR §1-§2, pinned in R64), read with H in place of G′_E; R68 (f) for G^u. RESTRICT_H (i) rests, as R64 (a) (i) does, on the standing SPEC premise 1E-N3 (RESULTS R57; N-EPR-1):
  (a) Lemma RESTRICT_H (§1): let J be an H-admissible run of a phase of N5 on G and k ∈ J. At the pair (σ_k, τ): (i) Ξ′_k = Ξ_k and W′_k =
      W_k; (ii) Iσ′_k = Iσ_k, SPEC S4a's output on H equals its output on G, and S4c's Even switch-all on Iσ is the same on both; (iii) Odd's
      dual valuation of τ is the same on both, so Iτ′_k = Iτ_k ∩ E(H); (iv) if k → k + 1 is an in-phase transition of N5 on G and Iτ′_k ≠ ∅,
      then τ is value-optimal against σ_k in S4b's arena of H. (Each item is a statement at one state, so σ̄ may change along J.)
  (b) Corollary REPRO_H (§1), with R64 (b)'s repair EPR-1: for H-admissible J = (x, …, y) and y′ := x + len(J), N5^τ on H from (σ_x, τ)
      passes through (σ_x, τ), …, (σ_{y′}, τ) with the same fallback / non-fallback type at each of its len(J) transitions as N5 on G; the
      states x, …, y lie in one phase of that N5^τ run; the last transition y → y′ has its source there and may leave it, unless σ̄_{y′} is
      also an Odd strategy of H (then J ∪ {y′} is H-admissible and y′ lies in that phase too).
  (c) Instances (§2; admissibility by definition, checked by both): an epoch E is G′_E-admissible (= RESULTS R64 (a), (b)); a u-run is
      G^u-admissible (= RESULTS R68 (f)); a frozen-side u-stretch J is G^{u|J}-admissible; a phase P is G^P-admissible with len(P) = y − x (no
      EPR-1 exit; N-RESTRICT-1, F4), and G^P ∈ 𝒞^{QP(P)}O. Consequence (RESTRICT-N3, F3; agreed by both): by (a), (b) on G^{u|J}, CONJECTURE
      RESTRICT_{u|J} (docs/new/N5-NCONF-box48.md §9, L-NEW successor 27, 4b79f056; l. 223 at the packet's pin 7b5876d8: "For k ∈ J, RESULTS
      R64 (a) (i)-(iv) hold with G′_E replaced by G^{u|J}; hence N5^τ on G^{u|J} from (σ_x, τ) reproduces J state by state with the same
      fallback types (as R64 (b) with EPR-1)") is PROVED, as an instance of RESTRICT_H.
  (d) The G^P sentence as repaired (G-RESTRICT-1 = G-R2-RESTRICT-1, F1; the joint repair in REFEREE's §C wording): every phase P = (x, …, y)
      of N5 on G is the INITIAL SEGMENT, of len(P) transitions, of the first N5^τ phase on G^P started at (σ_x, τ), state by state, with the
      same fallback types. Its clause "and equal to it when P ends by a λ change" is NOT part of this entry (one referee's proof; see the
      bullet "Referee strengthening" below).
- Not signed: the packet's G^P sentence as written, "EVERY PHASE OF N5 ON G IS ONE N5^τ PHASE ON G^P, from (σ_x, τ), state by state, with
  the same fallback types": FALSE in the equality reading (G-RESTRICT-1 = G-R2-RESTRICT-1; true as containment, which is (d)): REPRO_H says
  nothing about N5^τ's step from y, as y → y + 1 is not in-phase on G. Two mechanisms: nep_n12 (experiments/n5-epoch/results/climb/nep_n12.pg,
  sha1 682f6bf3, at its .start; REFEREE): P = [0, 1], τ(1): 10 → 8 at 1 → 2, the edge (1, 8) is not in G^P, so N5^τ keeps τ and its phase
  holds states 0, 1, 2; nh_r2802 (experiments/new/box28/out/nh_r2802.pg.pg, sha1 8652ac82, n = 7, S3 start; REFEREE-2, reproduced by REFEREE
  successor 17): G^P = G, P = [0, 0], SPEC's S4b moves τ(4) from 6 to 4 at 0 → 1 on a tie while S4b^τ keeps it, so the first N5^τ phase is
  [0, 1]. Also not signed (packet §3-§4, as the packet asks): the DATA; the READINGs, corrected for accuracy (F2: nep90_n40, nep76_n40 and
  long121_n40 have |Q| = 5 / 5 / 3 themselves, so G^P removes no Odd choice vertex there and drops 2 / 2 / 1 Odd edges, XDEG 24 / 26 / 9 on
  G against 22 / 24 / 8 on G^P; QP < |Q| in 2,307 of REFEREE's 4,073 phases; F5: a 𝒞^kO count transfers only if proved for N5^τ phases, read
  as the possibly longer phase of (d)); the OPEN items QP(P), XDEG(P).
- Referee strengthening (NOT part of this entry; one referee): the clause of (d) "and equal to it when P ends by a λ change" is PROVED by REFEREE alone (successor 17, in its §C, "(Opus
      5.5, D15)": with τ_{y+1} = τ, σ_{y+1} ≠ σ_y; (ii) and (iv) at y give N5^τ's step to (σ_{y+1}, τ); R15 (a), (d), injective rewards, (P1)
      and Lemma S (a) give reward(λ′_{y+1}(v)) > reward(λ′_y(v)) at a v whose λ changes); REFEREE-2 stated it from data only ("Equality holds
      when P ends by a λ change.", report l. 80), and nothing further was asked of it (fixes F1).
- Honest limits: (i) It bounds nothing: a phase of N5 depends only on the Odd edges it uses; no phase length, QP(P) or XDEG(P) is bounded
  (REFEREE-2's max QP 129, tcS8_N11, n = 418, a one-state phase). (ii) By (d), any bound on N5^τ phase lengths on G^P bounds len(P) (both
  referees); the equality at λ-ends rests on one referee's proof (REFEREE successor 17), with data agreeing on both engines (0 of 4,215 and
  0 of 11,777 λ-ends extend). (iii) Whether RESULTS R61's 𝒞^kO counts hold for N5^τ is not checked by the packet or either referee. (iv) The
  extension in (d) is rare but real: 186 of 11,527 phase ends (REFEREE) and 176 of 39,385 (REFEREE-2), all τ-ends; REFEREE successor 16's
  earlier "44 of 4,073" counted multi-state phases only (F6).
- Data (DATA, not proof): REFEREE (successor 16; own docs/referee/scratch/restrict_probe.py (sha1 0429b61b at the report; f451e00a, with ONE=1, at successor 17's §C), on its engine rl_engine with
  REFEREE successor 12's own N5^τ step; lane code not run): library 1,140 files (2,739 runs), lib41 (763), 4,500 random 𝒞^kO runs, nep90 /
  nep76 / long121 at their starts: 8,005 N5 runs, 4,073 phases, 28,938 in-phase transitions reproduced on G^P (and on G′_E), 202,408
  RESTRICT_H checks over five families (G^P, a random admissible cut, G′_E, G^u, G^{u|J}), 3,954 "unless" checks, 2,976 EPR-1 exits that
  leave (allowed), 0 failures; control MUT=1 (one edge (v, σ̄_x(v)) dropped from G^P) bites. Successor 17 (ONE=1: one-state phases included;
  lib1140, G^P only): 12,625 runs, 18,036 transitions, 0 failures; 186 of 11,527 phase ends extend, all τ-ends (7,312 τ-ends, 4,215 λ-ends).
  REFEREE-2 (successor 18; own docs/referee-2/R2-N5-RESTRICT/restrict_check.py on its lane's Runner (si.py) and its R2-N5-EPR step; lane
  tools not run): 21,971 runs, 61,356 phases; (H, J) instances G^P 61,356, G^u 104,910, G^{u|J} 372,118, G′_E 69,253, 0 violations (ADM,
  (i)-(iv), REPRO_H, λ′ = λ); of 39,385 phase ends with a next state on G, G's phase ends by τ in 27,020 and by λ in 11,777, N5^τ on G^P stops at y in 588 (the three counts partition the 39,385; G's end type is recorded only where N5^τ steps on), and its phase extends past y in 176, all τ-ends; control (one (v, σ̄_x(v)) dropped) fails in 30,335 of 35,196 runs.
- Signatures: REFEREE docs/referee/R-N5-RESTRICT.md (report c9bdfa68, successor 16; §C 3b2631be, successor 17): RESTRICT_H (i)-(iv), REPRO_H
  with EPR-1 and the "unless" clause, the four instances' admissibility SIGNED; the G^P sentence SIGNED in the containment reading, FALSE as
  equality (G-RESTRICT-1, wording; witness nep_n12); notes RESTRICT-N1..N3; in §C the λ-end equality PROVED. REFEREE-2
  docs/referee-2/R2-N5-RESTRICT.md (report 9549e59a, §C 864302d0; successor 18): RESTRICT_H, REPRO_H with EPR-1 (the "unless" clause in its
  §C), the instances SIGN; the G^P sentence TRUE ONLY AS CONTAINMENT (G-R2-RESTRICT-1; witness nh_r2802); notes N-RESTRICT-1..3. EXPOSURE:
  REFEREE-2 declared that before its review it saw the subject line of REFEREE's commit c9bdfa68 (REFEREE's verdicts, the gap's subject and
  the witness name nep_n12) and added experiments/n5-epoch/results/climb/*.pg to its corpus because of it. Per REFEREE's §C ruling, recorded in
  fixes F1: G-RESTRICT-1 was found by REFEREE (successor 16) and CONFIRMED by REFEREE-2 (anchored, not blind), with REFEREE-2's own witness
  nh_r2802 (a second mechanism); both signatures stand, REFEREE-2's recorded as anchored, not blind. §C (both): no disagreement on any
  verdict; joint gap map {G-RESTRICT-1 = G-R2-RESTRICT-1}; RESTRICT-N1 superseded by the joint repair (REFEREE-2's §C names "LIES IN ONE";
  REFEREE's later §C adopts REFEREE-2's initial-segment wording with the λ-end addition); RESTRICT-N2 = N-RESTRICT-2; RESTRICT-N3 agreed by
  REFEREE-2; N-RESTRICT-1, N-RESTRICT-3 accepted by REFEREE; nothing else open.
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (structural lemmas on N5's runs; no running-time bound, no algorithm claim). GAPS
  G-N5-TIME: open.

### R80 [refereed-only] N5 on EVERY game, inside one phase: every transition of a phase changes Even's σ (Lemma EVERY-SWITCH), so a phase P has |P| ≤ Σ_w SW_P(w), |P| the number of TRANSITIONS of P and SW_P(w) the number of those at which σ(w) changes (PHASE-SW; FALSE if |P| counts states); an Even vertex w that switches at a transition t → t + 1 of a phase and lies on no honest cycle at t and at t + 1 strictly raises Ξ(w) (Lemma RISE-SW), so |P| ≤ Σ_w XR_P(w) + #{(w, t) : w switches at t and lies on an honest cycle at t or t + 1}, XR_P(w) the transitions of P at which Ξ(w) changes (its Consequence); a CLEAN change y1 → y2 of σ̄ at an Odd choice vertex u ∈ U_c ∖ {c} of class c, u on no honest cycle at t and at t + 1, gives κ_{t+1}(y1) ⪰ κ_t(y1), strictly unless κ_{t+1}(y1) = κ_{t+1}(y2) (Lemma RISE-GATE-CLEAN; the tie exception is needed, nep22f_n64); a set I of consecutive transitions of one phase has |I| ≤ m_E + NOFRESH(I) (FRESH-RED); and on a global C-interval (RESULTS R76's definition, taken inside one phase) the transitions with a fresh Even edge, with a fresh Odd option and with a strict shrink of some A number at most m_E, Σ_{Odd u} (deg(u) − 1) and Σ_c |A_a(U_c)| ≤ n (FRESH3-COUNT) (2026-10-28) — elementary structural lemmas for N5 (they bound nothing: no count of switches or Ξ-changes per vertex, no NOFRESH and no phase length is bounded; the per-vertex forms SW-LIN and XR-LIN are DEAD; not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C89.md, checker 3f849b3a)
- Object (L-SI successor 19, Opus 5.5; frozen, unchanged during review): packet P-N5-CORE, docs/si/P-N5-CORE-box23.md, sha1
  7b66f1bae1a1b675c0fda0af1e5eaabf13f128a0 (l-si freeze 081ae740; quote base 33f43c20; 10 quotes), the §11 PROVED core (C1)-(C6) of
  docs/si/N5-ALT-box23.md. The referees' notes are collected by the lane in docs/si/P-N5-CORE-fixes-box23.md (l-si 5533c58c, sha1
  5f22c9ecd534bcf041f9f0672d842b643faf90e2, L-SI successor 20: F1-F7 for CORE-N1, CORE-N2 (a)-(c), N-CORE-1, CORE-N3 = N-CORE-4, CORE-N4 =
  N-CORE-2, N-CORE-3, and the records N-CORE-5, N-CORE-6, CORE-N5, CORE-N6; 35 quotes checked by script, experiments/si/rund/quotecheck.py
  "quotes=35 bad=0", pinned in experiments/si/check.sh with a shifted-line control that must fail); on trunk; repairs only: F1 adds the
  definition of |P| (CORE-N1), F2 corrects three citations, F4 replaces (C6)'s premise by RESULTS R76's landed definition and states the
  scope, F5 adds a remark (the tie exception is needed), F6 and F7 change no statement. F3 widens (C3) to every N5 transition (N-CORE-1);
  that widening is NOT part of this entry (bullet "Referee strengthening"). The statements below are in the repaired wording otherwise.
  Setting (every game): N5 = SPEC S1-S5 (docs/new/N5-ssi-global.md) with FIX 1-4 and the standing premise 1E-N3; state t = (σ_t, τ_t); Ξ_t
  := Ξσ_t, the valuation of σ_t against S1's Odd counterstrategy σ̄_t, Ξ_t(v) the value of v's honest (σ_t, σ̄_t)-play; ▷, ⊵ the S1 order;
  λ := Ξ's cycle-node map. A PHASE: a maximal run of states with λ_Ξ and τ constant (RESULTS R38 (a) KEY: the (λ_Ξ, τ)-phase is the joint
  λ-phase); a transition t → t+1 of a phase P joins two states of P; |P| := the number of transitions of P (pairs t → t+1 of consecutive
  states of P), so a phase with s states has |P| = s − 1 (F1). SW_P(w) := the transitions of P at which σ(w) changes; XR_P(w) := those at
  which Ξ(w) changes. Per honest class c, U_c := λ^{-1}(c); Q := the Odd vertices of out-degree ≥ 2; κ, κwt_c, Y^q_t as in RESULTS R56's
  setting and (d). A σ̄ change y1 := σ̄_t(u) ≠ y2 := σ̄_{t+1}(u) is CLEAN if y2 ∈ Y^u_t and y1 ∈ Y^u_{t+1}. For a set I of consecutive
  transitions of one phase, t → t+1 ∈ I is FRESH if some Even w switches at it to an edge (w, y) that w held at no earlier state of I (the
  first state of I included); NOFRESH(I) := the other transitions of I; m_E := the number of Even edges. GLOBAL C-INTERVAL: RESULTS R76's
  definition (a maximal run of GOOD transitions: for every c, A_{t+1} ⊆ A_t, D_{t+1} = D_t, DD_{t+1} = DD_t and Δ_{t+1}(u) = Δ_t(u) on DD_t;
  transition-local reading), taken inside one phase (R76 takes it inside a fallback-free run S; (C6) holds in both scopes, both referees
  checked both; F4); A_a(U_c) is A of U_c at the interval's first state a.
- Claims signed (both referees "(Opus 5.5, D15)", L37), on every game; no item uses (P); premises LANDED: SPEC S1, S2, S4 (a)-(d) with
  FIX 1-4; RESULTS R15 (a) Lemma A and (d) (cited in full, F2 (a): «(d) N5: every iteration applies Switch_I with ∅ ≠ I ⊆ Iσ to Even's σ
  (on G) and/or with ∅ ≠ I ⊆ Iτ to Odd's τ (on G^d), and» …; used with τ fixed); RESULTS R17 (a) (V1) for Ξ(v) = v ⊕ Ξ(next v) off v's
  play's cycle (F2 (b)); (SW) "every Even switch of N5 is to an edge of Iσ", as listed among RESULTS R72's landed premises; RESULTS R38 (a)
  KEY (only for the remark that a (λ_Ξ, τ)-phase is a joint λ-phase; τ constant is the phase definition, F2 (c)); RESULTS R56 (a) (Aκ),
  (M1κ), (M2κ) and (d) κ-Y-FORM_D; RESULTS R76 (the global C-interval definition only; CORE-N3 = N-CORE-4, F4):
  (a) (C1) EVERY-SWITCH (§2): at every transition t → t+1 of a phase, σ_{t+1} ≠ σ_t. (τ_{t+1} = τ_t by the definition of a phase; a
      non-fallback iteration changes (σ, τ); an Even fallback moves every Even vertex with an improving edge, to w ≠ σ(v) by S2; an Odd
      fallback changes τ and so cannot occur inside a phase.)
  (b) (C2) PHASE-SW (§2, with F1): for a phase P, |P| ≤ Σ_w SW_P(w), |P| the number of TRANSITIONS of P.
  (c) (C3) RISE-SW (§3, with F2): let t → t+1 be a transition of a phase and w an Even vertex with y := σ_{t+1}(w) ≠ σ_t(w), w on no honest
      cycle at t and at t + 1. Then Ξ_{t+1}(w) ▷ Ξ_t(w). Remark: the order of the steps matters (Ξ_t(y) may be the value of a play through
      w; the proof compares Ξ_{t+1}(y) ▷ Ξ_t(σ_t w), two w-free values with cycle node λ(w), and only then applies w ⊕). Consequence (with
      (b)): |P| ≤ Σ_w XR_P(w) + #{(w, t) : w switches at t and lies on an honest cycle at t or t + 1}.
  (d) (C4) RISE-GATE-CLEAN (§4): let t → t+1 be a transition of a phase, c a class, u ∈ Q ∩ U_c, u ≠ c, on no honest cycle at t and at
      t + 1, with a CLEAN change y1 := σ̄_t(u) ≠ y2 := σ̄_{t+1}(u). Then κ_{t+1}(y1) ⪰ κ_t(y1), strictly unless κ_{t+1}(y1) = κ_{t+1}(y2).
      (Chain κ_t(y1) ⪯ κ_t(y2) ⪯ κ_{t+1}(y2) ⪯ κ_{t+1}(y1) by (Aκ) and κ-Y-FORM_D at t and t + 1 and (M2κ) at y2.) Its two closing
      sentences: ties at t + 1 aside, a clean σ̄ change at u is a strict Ξ-rise of the abandoned option y1 at the same transition ((M1κ));
      each such rise of y1 at t is charged by at most the number of Odd u with σ̄_t(u) = y1. Remark (F5; CORE-N4 = N-CORE-2): the tie
      exception cannot be dropped: nep22f_n64 (sha1 d98de59f…, its .start in experiments/n5-epoch/instances/, sha1 a7ecb00e…), transition
      8 → 9 (a fallback), class 18, gates 9 (57 → 30) and 56 (6 → 1), both clean, all four κ = (0, 4) at t and t + 1 (found independently
      by both referees, two engines).
  (e) (C5) FRESH-RED (§5): for a set I of consecutive transitions of one phase, |I| ≤ m_E + NOFRESH(I) (fresh transitions map injectively
      to fresh Even edges); with (a), the non-fresh transitions of I are exactly those at which every switching Even vertex returns to an
      edge it held before in I.
  (f) (C6) FRESH3-COUNT (§5, with F4): on a global C-interval I = [a, b]: the transitions with a fresh Even edge (in I's scope) number
      ≤ m_E; those at which some Odd vertex moves σ̄ to an option it did not hold at an earlier state of I number ≤ Σ_{Odd u} (deg(u) − 1);
      those with A_{t+1} ⊊ A_t for some class number ≤ Σ_c |A_a(U_c)| ≤ n. (Of goodness only "A non-increasing" is used, REFEREE §4,
      accepted by REFEREE-2.)
- Not signed: (C2) and (C3)'s Consequence with |P| read as the number of STATES of P (the packet's §1 calls a phase a run of states and
  did not define |P|): FALSE, every one-state phase has |P| = 1 > 0 = Σ_w SW_P(w) (CORE-N1; REFEREE: 13,932 of 16,595 phases of lib1140;
  REFEREE-2: 2,098 one-state phases in alt_all); repaired by F1. (C4) without its tie exception ("strictly"): FALSE (nep22f_n64, above).
  The packet's §6 (not to sign, as the packet says): the DATA; the UNCLEAN gate change (N5-ALT §1 RISE-GATE, through Fact CL of P-N5-OFFMONO
  §1); the conjecture FRESH3 (every σ̄-changing in-interval transition has one of (f)'s three events), DEAD (ret14_n48, N5-ALT §3; REFEREE
  reproduces 4 failures of 1,379 in alt_all, CORE-N6); the DEAD per-vertex forms XR-LIN and SW-LIN; the READING on passive readers.
- Referee strengthening (NOT part of this entry; N-CORE-1: in REFEREE-2's (C3) verdict line as an addition, not in REFEREE's verdict table): (C3) RISE-SW at EVERY N5 transition, in a
  phase or not (fixes F3 writes it into (C3)'s statement). REFEREE-2 states and proves it in its report (verdict line of (C3), "Also true at
  every N5 transition, not only in-phase ones (N-CORE-1)"; §3: if the cycle nodes at t and t + 1 differ, the two values compare by the
  cycle node's reward, which w ⊕ does not change; data XC3, 0 failures off-cycle) and calls it in its §C "mine alone; it is an extension and
  changes no verdict"; REFEREE in its §C: "ACCEPTED, re-derived" (steps 1-2 of its §2 hold at every iteration, w-freeness needs only "off
  honest cycles at t and t + 1", same cycle node → step 5, different → reward), not entered as a SIGNED verdict ("Verdicts identical:
  (C1)-(C6) all SIGNED by both"). Also not signed as a bound: m_E − n_E in (e) and (f)'s first count (N-CORE-3; REFEREE "could be m_E − n_E
  ... Not needed"; F6 keeps m_E; REFEREE-2's control X5nE shows it cannot be lowered to n_E, 344 in alt_all).
- Honest limits: (i) It bounds nothing. (b), (c)'s Consequence, (e) and (f) move |P| or |I| onto SW_P, XR_P, the on-cycle switch pairs and
  NOFRESH, none of which is bounded here; (f) counts three events but FRESH3 is DEAD, so some σ̄-changing transitions of a global C-interval
  carry none of them. (ii) READING (Lead): the PROVED (C2)-type bound |P| ≤ Σ_w SW_P(w) is reader-inflatable per vertex: some passive Even
  readers (those that keep the run SAME; not every Even reader does, N5-ALT §12's CORRECTION) raise one vertex's SW, and Σ_w SW_P(w), without
  changing the run (docs/si/N5-ALT-box23.md §12, l-si 3cb6035b, corrected 992e3bb0: on long121_n40's phase [1, 122] the most switches
  of one Even vertex is 12, and an appended Even reader switches 16 times with the run SAME, instance l121ereader_n41); the transition count |P| is intrinsic. CONJECTURE SW-LIN ("in every phase, every Even vertex switches
  ≤ n times") is DEAD (l-si 85709361, swlin_kill_n26: one Even vertex switches 27 > n = 26 in one phase; L-COMP's n5b agrees), and
  CONJECTURE RUN-LIN (every fallback-free run of a phase has ≤ 2n transitions) is DEAD (runfam_K10, n = 49: a fallback-free run of 99 > 2n =
  98 transitions; L-SI 51281c00, docs/si/N5-RUNLIN-box24.md §7 at l-si 90bcc50c; reproduced by REFEREE, docs/referee/R-N5-RUNLIN-kill.md
  c609f779). So (b) and (c)'s Consequence are not completed by a linear per-vertex bound. (iii) Every hypothesis is needed in data:
  (a) fails at phase-leaving transitions (τ-only moves; REFEREE MUT3 4 of 52, e.g. swlin_kill_n26 at its given start, transition 48;
  REFEREE-2 X1 435 / 939 / 2,789 on alt_all / lib41 / random k2); (c)'s off-cycle hypothesis (on-cycle switches without a Ξ(w) rise:
  REFEREE alt_all 73 of 128, lib1140 328 of 615; REFEREE-2 X3cyc 38 / 89 / 328); (d)'s tie exception (nep22f_n64); (e)'s NOFRESH term
  (REFEREE MUT6: 40 failures of |I| ≤ m_E on l121reader_n41, a 121-transition phase, m_E = 103); (f)'s goodness (REFEREE-2 X6A 26 / 34 and
  X6Ax 201 / 472 on alt_all / lib41; REFEREE's MUT4 did not bite on its corpus). (iv) (d) is for CLEAN changes only; the unclean case is not
  claimed (REFEREE-2 saw (d)'s conclusion hold at every unclean change it checked, DATA). (v) NOFRESH is not small over a phase: the packet's
  §6 "≤ 22 per run" holds per fallback-free run (fresh.py's unit; F7, N-CORE-6); over whole phases it reaches 90 (long121_n40 and
  l121ereader_n41 [1, 122], both referees), and 115 in one fallback-free run on the RUN-LIN family (runfam_K40, L-SI's experiments/si/runlin/anatomy.py; fixes F7). Nothing here bounds N5's running time.
- Data (DATA, not proof): REFEREE (successor 17; own scratch/core_probe.py (sha1 be6bb900…) on its engine rl_engine, written from SPEC S1-S5
  + FIX 1-4; lane code not run; 0 failures in every MUT=0 run): alt_all (413 games of root/logs/alt_all.lst, n ≤ 600; 918 runs: given start
  when valid, best-reward, 1 random) 12,937 in-phase transitions, (C3) 27,194 checks, (C4) 4,953 clean / 1,764 unclean / 29 ties at t + 1 /
  2 without a rise, (C5) 98,053 intervals, (C6) 1,891 / 1,874 intervals (phase / fallback-free scope); lib41 (349 games, 698 runs) 9,059
  transitions; lib1140 (1,024 games, 3,072 runs) 22,018 transitions, (C3) 40,019, (C4) 3,195 clean; rand3000 (6,000 runs) and MUT=2 random
  sets (48,000 games, 96,000 runs). Premise checks at every state: (V1), (SW), R15 pointwise monotonicity, (C3)'s steps separately, (Aκ)
  and κ-Y-FORM_D at both ends, (M2κ) at y2, 0 failures. Controls: MUT1 ((C3) demanded of the abandoned option) bites 579 on its 4-instance
  set; MUT2 ((C4) strict) bites 2 (nep22f_n64); MUT3, MUT6 above; MUT4, MUT5 do not bite. REFEREE-2 (successor 19; own
  docs/referee-2/R2-N5-CORE/core_check.py and qcheck.py on its lane's Runner (si.py); lane tools not run; every run 0 violations): alt_all
  (413 runs, given start else S3) 458 phases (its phase count; 2,098 one-state phases besides), 8,048 in-phase transitions (729 fallbacks),
  (C3) 16,825, (C4) 3,071 clean / 1,075 unclean, (C5) 86,519 intervals, (C6) 1,187 (1,172 in GCX's scope S); lib41_noref × 3 starts
  (1,230 runs) 12,135 transitions; named (8 runs) 537; random k2 / kO / k5 (9,000 / 4,500 / 800 runs); RULE=rand (any non-empty subset of
  Iσ, lib41 × 3, 1,230 runs, 14,822 transitions): (C3)-(C5) hold, 0 violations. Engine Ξ equals the play value at every state (ENGXI, 0
  differences). Counts differ from the packet's §6 (alt_all 8,048 against 8,084 in-phase transitions; cause unknown on both sides, no
  violation on either; N-CORE-5) and from REFEREE's (extra starts). CORE-N5: three start files in alt_all.lst (L-RED's comp54_n80,
  n3cov_lean, n3cov_phi under experiments/red/n3/instances/) do not fit their games or are partial; REFEREE skipped or corrected them,
  REFEREE-2 re-ran alt_all with start validation (every count IDENTICAL, 0 violations); L-RED repaired them in R99 (l-red 5e8f0174,
  docs/red/R99-start-erratum.md: every reported count reproduces). No signed statement uses the counts on those games.
- Signatures: REFEREE docs/referee/R-N5-CORE.md (report 9d831869, sha1 0e1480a3709671f395a8813fcafa6e464fd2ffd4 there; §C 8641ae40;
  successor 17): (C1) SIGNED; (C2) SIGNED with |P| the number of TRANSITIONS (CORE-N1; the state reading false); (C3) with its Remark and
  Consequence SIGNED; (C4) with its two closing sentences SIGNED, tie clause needed (CORE-N4); (C5) with its parenthesis SIGNED; (C6) SIGNED
  in either scope (CORE-N3); quotes 10/10; notes CORE-N1..N6; no gap. REFEREE-2 docs/referee-2/R2-N5-CORE.md (report 2ed8d3fb, sha1
  a402d9e71efee5830ad2a853cf7808a1a1ab4402 there; §C b28d1ba9; successor 19): (C1)-(C6) SIGN, quotes 10/10 (shifted control 0/10); notes
  N-CORE-1..6; no gap. INDEPENDENCE: both clean, no exposure on either side (REFEREE re-listed REFEREE-2's paths at 23:00Z, 0 / 0 / 0 CORE
  files before its push; REFEREE-2 ran only a names-only count on docs/referee/ and opened REFEREE's report only after pushing 2ed8d3fb).
  §C (both): verdicts identical, (C1)-(C6) SIGNED by both; joint gap map EMPTY; CORE-N4 = N-CORE-2 found independently on two engines
  (same instance, transition, class, gates and κ); CORE-N3 = N-CORE-4; CORE-N1, CORE-N2 (a) and CORE-N5 ACCEPTED by REFEREE-2 as missed,
  CORE-N2 (b), (c) agreed; N-CORE-1 (re-derived), N-CORE-3, N-CORE-6 and REFEREE-2's controls ACCEPTED by REFEREE; N-CORE-5 no conflict;
  nothing open.
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (elementary structural lemmas on N5's phases; no running-time bound, no
  algorithm claim). GAPS G-N5-TIME: open.

### R81 [refereed-only] N5 on EVERY game, inside one phase: with K the vertices reachable from an Even vertex of out-degree ≥ 2 (K is closed under successors, so the honest play from a vertex of K stays in K; every Even vertex outside K has out-degree 1; K = ∅ leaves no in-phase fallback: Facts K1-K3), n_K := |K| and a K-configuration C = σ̄|Q ∩ K (Q the Odd vertices of out-degree ≥ 2), an in-phase S4c fallback from a K-C-state raises the level LEV^K_C, taken over the simple paths of the frame H^K_C (G[K] with every Odd vertex of K cut to its σ̄_C edge), to at least min(LEV^K_C + 1, n_K − 1) (Lemma FB-RISE^K); LEV^K_C = n_K − 1 at a K-C-state t gives Ξ_t = B^K_C on K, and Ξ constant on K from t to any later K-C-state of the phase (Lemma SAT^K); a fallback from such a saturated K-C-state is followed by the end of the phase or by no further K-C-state of it (Lemma SAT-FB^K), so per phase and K-configuration at most one in-phase fallback has a saturated source (Corollary SAT-FB1^K); hence in every phase P, f ≤ n_K·|𝒞^K_f(P)|, f the number of in-phase S4c fallbacks of P and 𝒞^K_f(P) the K-configurations of their sources (Theorem FB-C^K), which implies RESULTS R73's Theorem FB-C′, f ≤ n·|𝒞_f(P)| (Corollary (i)); and, signed only AS AN IMPLICATION (Corollary (ii)): if G′ is G plus new vertices H with no edge from an old vertex into H, no Even vertex of out-degree ≥ 2 in H, and the run on the old vertices, the fallbacks and the phases unchanged (an assumption for a general H; for ONE added Odd vertex with no predecessors satisfying (R) it is supplied by REFEREE's Theorem READER-INV, which has one referee and is NOT landed), then n_K, 𝒞^K_f(P) and f are the same for G′ as for G, the step σ̄′|V = σ̄ following from the first hypothesis alone (2026-10-28) — a REDUCTION of f to the number of K-configurations at the fallback sources of a phase (that number is not bounded here; FB-LIN, f ≤ n per phase, is OPEN; not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C90.md, checker 9777e9e6)
- Object (L-NEW successor 30, Opus 5.5; frozen, unchanged during review): packet P-N5-FBCK, docs/new/P-N5-FBCK-box49.md, sha1
  7747ecf23f65ac82fc2d75e0f6ecc28c7621ce1f (l-new freeze 0e63596d, 2026-10-28T23:25:01Z; quote base 6d863a4d; 9 quotes, quotecheck3.py
  "quotes=9 bad=0"; both referees measured the pin), RESULTS R71 (a), (b) and R73's SAT-FB / SAT-FB1 / FB-C′ re-run on the successor-closed
  set K; source docs/new/N5-READER-box49.md §7-§8 (working note). The referees' notes are collected by the lane in
  docs/new/P-N5-FBCK-fixes-box49.md (l-new e0fda64f, sha1 19237624d32db379db858ea961861bd094441db1, L-NEW successor 30: F1-F8 for
  FBCK-N1 = N-FBCK-1, FBCK-N2, FBCK-N3, FBCK-N4, N-FBCK-2..5, in REFEREE-2's §C C.4 order; 25 quotes checked by script,
  experiments/new/box49/quotecheck3.py "quotes=25 bad=0", pinned in experiments/new/check.sh with a shifted-line control and the file's sha1);
  on trunk; repairs only, "No signed statement changes. Corollary (ii) stays an IMPLICATION." (fixes l. 6): F1 replaces Corollary (ii)'s
  third bullet and adds one sentence after the bullets (FBCK-N1); F3 adds a sentence after Lemma SAT^K (FBCK-N3); F2, F4-F8 are records and
  change no statement. The statements below are in that repaired wording.
  Setting (every game): as in RESULTS R71 (N5 = SPEC S1-S5 with FIX 3, an in-phase fallback being Even's; Ξ_k the value of the honest
  (σ_k, σ̄_k)-play; λ its cycle-node map; phases as in RESULTS R38 (a), λ and τ constant on one; value(r) := (u, P(r), |r|) for a simple path
  r ending at a cycle node u of λ; f := the in-phase S4c fallbacks of a phase; Q := the Odd vertices of out-degree ≥ 2; R71's configurations
  C = σ̄|Q, H_C, LEV_C, B_C, 𝒞_f(P)). K := the vertices reachable in G, by a path with ≥ 0 edges, from an Even vertex of out-degree ≥ 2;
  n_K := |K|; Q_K := Q ∩ K. A K-CONFIGURATION is C = σ̄|Q_K, and k is a K-C-STATE if σ̄_k|Q_K = C. H^K_C := G[K] with every Odd v ∈ K cut to
  its one edge σ̄_C(v) (C(v) for v ∈ Q_K, the unique successor otherwise). LEV^K_C(k) := the largest j ≤ n_K − 1 such that Ξ_k(x) ⪰ value(r)
  for every x ∈ K and every simple path r of H^K_C with ≤ j edges from x to a cycle node of λ; B^K_C(x) := the maximum of value(r) over the
  simple H^K_C-paths r from x ∈ K to a cycle node of λ. 𝒞^K_f(P) := the K-configurations of the sources of P's in-phase S4c fallbacks. For
  Corollary (ii): G′ is G plus new vertices H, V the old vertices, primes for G′'s objects.
- Claims signed (both referees "(Opus 5.5, D15)", L37), on every game; no item uses (P); premises LANDED: SPEC S1-S5 with FIX 3 (S2's Iσ,
  S4c's rule); the standing premise 1E-N3, form P1 (RESULTS R57); RESULTS R71's setting, (a) Lemma FB-RISE_C and its proof (P-N5-FBC-box47
  §1, sha1 32d3776c…, the pin), (b) Lemma SAT_C and its proof (first part and the (MON) sandwich only; its 4n(n − 1) window is not used,
  N-FBCK-4 = F7, FBCK-N3 = F3); R71's premises (MON) (RESULTS R15 (a) with R15 (d)), RESULTS R17 (a) (V1), (V2), R17 (b) Lemma P's Case A
  with Ω := Ξ_t (RESULTS R70's Q-A, YES by both of its referees), R38 (a); RESULTS R73 (d) Lemma SAT-FB and its proof (P-N5-EPC-box48 §3,
  sha1 9f48ded7…, the pin; its last step in the post-fix R6 form, without HON-FB), Corollary SAT-FB1, Theorem FB-C′. NOT landed, for Corollary (ii) = item (i) only: REFEREE's Theorem READER-INV under (R) (docs/referee/R-N5-READER.md at e83fd19d, §1; one referee), which item (i) does
  not use as a premise, only as the source that supplies Corollary (ii)'s third hypothesis in one case:
  (a) Facts K1-K3 (§0). K1: K is closed under successors; hence the honest play from x ∈ K stays in K at every state, λ(x) ∈ K, and at a
      K-C-state the honest play from every x ∈ K is a play of H^K_C. K2: every Even vertex outside K has out-degree 1, so Iσ_k(x) = ∅ at
      every state for Even x ∉ K (S2). K3: if K = ∅ there is no in-phase fallback (an in-phase fallback is Even's, FIX 3, and needs Iσ ≠ ∅).
  (b) The setting facts (§0; REFEREE's K1-K3 row, REFEREE-2's own row "LEV^K_C ≥ 0 and non-decreasing on P (setting sentences)", the §C
      joint row "K1-K3 (with LEV^K_C ≥ 0, non-decreasing; 𝒞^K_f the image of 𝒞_f)"): LEV^K_C is defined at every state of P and is
      non-decreasing along P (H^K_C and λ fixed on P; (MON)); LEV^K_C ≥ 0 (a 0-edge path has x = u a cycle node, and Ξ_k(u) = (u, ∅, 0)
      throughout the phase); 𝒞^K_f(P) is the image of R71's 𝒞_f(P) under restriction to Q_K, so |𝒞^K_f(P)| ≤ |𝒞_f(P)|.
  (c) Lemma FB-RISE^K (§1): let t → t + 1 be an in-phase S4c fallback of P whose source t is a K-C-state. Then
      LEV^K_C(t + 1) ≥ min(LEV^K_C(t) + 1, n_K − 1). (R71 (a)'s proof with x ∈ K, H^K_C for H_C and n_K for n; the configuration is used only
      at an Odd x ∈ Q_K, and every vertex the proof names lies in K by K1.)
  (d) Lemma SAT^K (§1, with F3): if t is a K-C-state with LEV^K_C(t) = n_K − 1, then Ξ_t = B^K_C on K; if t < t′ are K-C-states of P with
      LEV^K_C(t) = n_K − 1, then Ξ is constant on K on the states t, …, t′. F3: "R71 (b)'s window bound t′ − t ≤ 4n(n − 1) is not used:
      saturated sources are counted by SAT-FB1^K, which needs only that the second source is a K-C-state after the first (not that it is
      saturated)."
  (e) Lemma SAT-FB^K (§1): let t be a K-C-state of P with LEV^K_C(t) = n_K − 1 whose transition t → t + 1 is an in-phase S4c fallback. Then
      t + 1 is the last state of P, or P has no K-C-state after t. (Iσ_{t+1} = ∅ at Even x ∉ K by K2 and at Even x ∈ K since succ(x) ⊆ K
      (K1); the rest is R73's text. This is the one step that needs more than restriction to K, N-FBCK-2 = F5.)
  (f) Corollary SAT-FB1^K (§1): for every phase P and K-configuration C, at most one in-phase fallback of P has a saturated K-C-state as its
      source.
  (g) Theorem FB-C^K (§2): in every phase P of N5 on every game, f ≤ n_K·|𝒞^K_f(P)|. (K = ∅: f = 0 by K3. Otherwise, per C ∈ 𝒞^K_f(P), at
      most n_K − 1 unsaturated sources, LEV^K_C strictly rising between consecutive ones in {0, …, n_K − 2}, and at most 1 saturated one
      (SAT-FB1^K); sum over C.)
  (h) Corollary (i) (§2): n_K ≤ n and |𝒞^K_f(P)| ≤ |𝒞_f(P)|, so FB-C^K implies RESULTS R73's Theorem FB-C′ (f ≤ n·|𝒞_f(P)|).
  (i) Corollary (ii) (§2, repaired by F1), signed AS AN IMPLICATION by both (REFEREE: "SIGNED as an implication"; REFEREE-2: "SIGN AS AN
      IMPLICATION from its three bullets"). Let G′ be G plus new vertices H such that: no old vertex has an edge into H; no Even vertex of H has
      out-degree ≥ 2; the run on the old vertices, the fallbacks and the phases are unchanged. "This is an ASSUMPTION for a general H, with (R)
      read for every Odd vertex of H. READER-INV supplies it for ONE added Odd vertex with no predecessors that satisfies (R)." Then
      K(G′) = K(G) (no new Even choice vertex is added, and no new vertex is reachable from an old one), and "Moreover σ̄′|V = σ̄ and Ξ′|V = Ξ
      at every state, by the first bullet alone. No old vertex reaches H, so S1's choices at old vertices are unchanged (REFEREE's proof,
      R-N5-FBCK §3; checked by REFEREE-2 against SPEC S1 and on 100,000 cases). Hence 𝒞^K_f(P), which reads σ̄ on Q_K ⊆ V, is unchanged." So
      n_K, 𝒞^K_f(P) and f are the same for G′ as for G. The step σ̄′|V = σ̄ (Ξ′|V = Ξ as triples, ranks relabelled order-preservingly; the
      argument of READER-INV's one-state Lemma (a) extended to H) is part of this item: REFEREE's report signs (ii) "with one implicit step made
      explicit (FBCK-N1)" and proves it (§3), and REFEREE-2's §C joint verdict for (ii) reads "SIGN as an implication; the σ̄ step is proved
      (C.3)" after checking the argument step by step against SPEC S1 (i)-(vi) ("ACCEPTED"; its own N-FBCK-1 reading SUPERSEDED). It uses
      the first hypothesis only, not READER-INV. The corollary's conclusion stays an IMPLICATION from its three hypotheses, and stays one until
      READER-INV is refereed twice (FBCK-N4 = F4, agreed by REFEREE-2).
- Not signed: Corollary (ii) as the packet wrote it, as an application of READER-INV to a general H: its parenthesis "(READER-INV gives this
  for a reader satisfying (R))" is right for ONE new Odd vertex with no predecessors, which is what READER-INV states, not for a set H with
  several readers, Even vertices or edges inside H (FBCK-N1 = N-FBCK-1, both referees); and its implicit step (σ̄ on the old vertices) was
  not stated by "the run on the old vertices is unchanged". Not false; repaired by F1 into (i). Repeated single-reader additions would need H
  acyclic, each new vertex without predecessors when added, and (R) at each step; not proved (REFEREE-2 N-FBCK-1). Also not signed (packet
  §3-§4, as the packet says): the DATA, including Corollary (ii)'s closing instance sentence (RESULTS R71 / R73's |𝒞_f(P)| inflated by a
  reader on l121_cf35_39, 5 → 8 = f; DATA, reproduced by both, below); the READING and OPEN items of §3: CONJECTURE FB-C° in the read frame
  of N5-READER §8 (OPEN; an Even choice vertex puts everything it reaches into K, even along an edge it never uses: on l121_cf_emb12
  |𝒞^K_f| = 8 = f), and FB-LIN, which FB-C^K does not imply.
- Referee strengthening (NOT part of this entry; REFEREE's remark outside its verdict table; REFEREE-2 AGREED in its §C only): K ≠ ∅ forces n_K ≥ 2, since an Even choice vertex has two distinct successors
  in K (REFEREE's remark under K3, report §1); REFEREE-2 in its §C: "AGREED (an Even choice vertex has two distinct successors in K). It is
  not in my report."
- Honest limits: (i) A REDUCTION, not a bound: f is bounded by n_K times the number of K-configurations at fallback sources; |𝒞^K_f(P)| is not
  bounded here, FB-LIN (f ≤ n per phase) is OPEN, and the CONJECTURE FB-C° in the read frame is OPEN (packet §3; fixes "What this file does
  not do"). Nothing here bounds N5's running time. (ii) READING (Lead): FB-C^K does not shrink FB-LIN. Two of L-NEW's dead ends
  (docs/new/N5-READER-box49.md §9, l-new 95714e3e; L-NEW's records, not refereed): MONO-CONF ("there is an order on K-configurations in which
  the configurations at successive fallback sources of a phase never go back") DEAD on the plain long121_n40 (sha1 c667c085…; phase [1, 122],
  8 fallback sources with K-configurations C0 C1 C2 C3 C4 C1 C2 C3) and on njb_reabs65_n48 (sha1 3388d0be…; phase [2, 68], f 29, 2
  alternating K-configurations); SMALL-CK ("|𝒞^K_f(P)| ≤ g(n) with g smaller than the trivial f") DEAD by
  experiments/new/box49/inst/l121_cf_emb12.pg (sha1 5440021b27bb0ab23cd4db682ae73bfbf5aaf39a): an embedded reader (the old Even vertex 12 →
  o) lifts |𝒞^K_f| from 5 to 8 = f with the run SAME (L-NEW's DATA; READER-INV does not cover it, o has a predecessor), so a bound
  |𝒞^K_f| ≤ g(n) gives f ≤ g(n + 1) on the base game. Both referees reproduce |𝒞^K_f| = 8 = f, n_K = n = 41 there. Plain readers cannot
  inflate the K-count (Corollary (ii), an implication); edges from an Even choice vertex can. (iii) The K frame rarely improves on R73 in
  natural data (FBCK-N2 = F2): FB-C^K is strictly stronger than FB-C′ only when n_K < n or |𝒞^K_f| < |𝒞_f|; REFEREE: n_K < n in 90 of 575
  fallback phases of lib1140, |𝒞^K_f| < |𝒞_f| only on the dressing l121_cf35_39 and 2 phases of lib41; REFEREE-2: the gain appears when
  vertices outside K are added (lib41 + 5, no old → new edges: Σ |𝒞_f| / Σ |𝒞^K_f| 414 → 257, |𝒞^K_f| < |𝒞_f| in 76 of 205 phases). Its use
  is reader-proofness, not a better count on undressed games. (iv) The closure of K is needed (N-FBCK-2 = F5): REFEREE-2's control open1
  (K′ := the Even choice vertices and their successors, not closed) bites 2,528 + 1,281 on its dressed k4 and random kO sets, among them
  795 + 418 SAT, 1 + 1 SATFB and 1 SATFB1 failures; REFEREE's §C: "ACCEPTED, stronger evidence". (v) The per-configuration bound n_K is not
  approached (N-FBCK-3 = F6): max fallbacks from one K-configuration / n_K = 0.781 (farrise25_n32, sha1 8941d1c9…: 25 of 32; REFEREE, as the
  packet's 0.78) and 0.75 (wd16_s2: 12 of 16; ccl_fbx_n32 + 5: 24 of 32; REFEREE-2); REFEREE-2's nk1 ((n_K − 1) per configuration) does not
  bite, REFEREE's MUT3 (n_K // 2) bites 3. SAT-FB^K's alternative "P has no K-C-state after t" never occurs on its own in REFEREE-2's data
  (every saturated case, 36 + 20 + 6,188, has a later K-C-state and t + 1 the last state of P), so it rests on the proof alone.
- Data (DATA, not proof): REFEREE (successor 17; own docs/referee/scratch/fbck_probe.py (sha1 deeb2391…) on its engine rl_engine, exact levels
  by simple-path enumeration in H^K_C; lane code not run; 0 failures in every MUT=0 run): named (box49/inst/l121_* (9), farrise25_n32,
  wd16_s2, zcl_rx_n32, long121_n40, swlin_kill_n26, l121reader_n41; given + S3) 27 runs, 16 fallback phases, f 145, Σ |𝒞_f| / Σ |𝒞^K_f|
  71 / 68; lib1140_part00-03 (n ≤ 40; given + S3 + 2 random) 2,725 runs, 575 fallback phases, f 1,956, 710 / 710, "RISE checks (unsat.)"
  870 (662), 208 saturated fallbacks; lib41 (n ≤ 48; given + S3 + 1 random) 726 runs, 206 fallback phases, f 901, 261 / 259; rand3000
  (n 6-18, k ≤ 6) 9,000 runs, 315 fallback phases, f 315, 312 saturated. THM and COR1 on EVERY fallback phase (also the 12 + 203 + 104
  phases whose exact levels were skipped at the budget); K1, K2 (and Iσ ⊆ K at every state), K3 (1,277 phases with K = ∅: no fallback) and
  REAL on every run. Reproduced: l121_cf35_39 f = 8, |𝒞_f| = 8, |𝒞^K_f| = 5 (vertex 40 ∉ K, n_K = 40); l121_cf_emb12 |𝒞^K_f| = 8 = f
  (n_K = n = 41); l121_a 5. Controls: MUT1 (FB-RISE^K with + 2) bites 51 of 53; MUT2 (configuration read at t + 1) does not bite on the named
  set; MUT3 above; MUT4 (S4c's (Ξ, w)-MINIMUM) bites RISE 3 (named) and SATFB 20, SATFB1 12, RISE 1 on rand3000. REFEREE-2 (successor 19;
  own docs/referee-2/R2-N5-FBCK/fbck_check.py, percase.py, sbar_ext.py on its lane's Runner (si.py); lane tools not run; every non-mutation
  run 0 violations; LEV^K_C exact by enumeration, or min(LEV^K_C, D) exactly in deep mode): named (18 runs) 15 fallback phases, f 117,
  78 / 75; lib41_noref × 3 starts (1,230 runs) 240, f 1,103, 299 / 297; lib41 dressed + 5 (820 runs) 205, f 887, 414 / 257; random dressed
  k4 and kO (60,000 runs each) 1,743 and 1,944; random k2 (60,000) 1,712; random kO (30,000) 847 fallback phases; K3 on 409 + 267 + 6,434
  phases with K = ∅; RISE exact at 276 + 213 + 6 + 6,249 sources, 401 + 352 + 98 more in deep mode, 426 + 322 + 13 undecided at the cap;
  THM and CNT (≤ n_K sources per K-configuration) decided in every fallback phase. Same instance figures as REFEREE on l121_cf35_39,
  l121_cf_emb12, l121_a; swlin_kill_n26: 6 fallbacks, |𝒞^K_f| 3. σ̄ extension (sbar_ext.py; random G plus random H, Even H vertices of
  out-degree ≥ 2 included, random σ): S1's σ̄ and Ξ agree on V in 100,000 / 100,000 cases (h = 4 and h = 10); control MUT=backedge (one old →
  H edge) 8,203 differences in 20,000. Controls: plus2 bites 4 + 6, tau (Q_K cut to τ instead of C) 263 + 264, open1 above, nk1 does not
  bite. The packet's §4 (lane, experiments/new/box49/fbconf.py): KVIOL 0 on named (17 runs), lib41 (1,047) and L-RED (311). Counts differ by
  start choice (N-FBCK-5 = F8): lib41 Σ |𝒞_f| / Σ |𝒞^K_f| 303 / 301 (packet, 1,047 runs), 299 / 297 (REFEREE-2, 1,230), 261 / 259 (REFEREE,
  726); no conflict, no violation on any side.
- Signatures: REFEREE docs/referee/R-N5-FBCK.md (report f2d22ad7, sha1 913f31be56428f515652a482750cbd8c8cd3e67c there; §C 6b752e89; successor
  17): K1-K3 (with LEV^K_C ≥ 0, non-decreasing; 𝒞^K_f the image of 𝒞_f), FB-RISE^K, SAT^K (both parts), SAT-FB^K, SAT-FB1^K, Theorem FB-C^K,
  Corollary (i) SIGNED; Corollary (ii) SIGNED as an implication, its implicit step σ̄′|V = σ̄ made explicit and proved (FBCK-N1); quotes 9/9;
  notes FBCK-N1..N4; no gap. REFEREE-2 docs/referee-2/R2-N5-FBCK.md (report 30237ebb, sha1 e2d7eb8db4064b7ce3a9292ae506d132e0716e40 there; §C
  991f9e27; successor 19): K1-K3, LEV^K_C ≥ 0 and non-decreasing, FB-RISE^K, SAT^K, SAT-FB^K, SAT-FB1^K, Theorem FB-C^K, Corollary (i) SIGN;
  Corollary (ii) SIGN AS AN IMPLICATION (in its §C: "SIGN as an implication; the σ̄ step is proved (C.3)"); quotes 9/9 (SHIFT=1 control 0/9);
  notes N-FBCK-1..5; no gap. INDEPENDENCE: REFEREE opened no REFEREE-2 FBCK file before its push (names re-listed at 23:54Z: 0 / 0 / 0) and
  ran no lane code; REFEREE-2 did not open REFEREE's report before pushing 30237ebb (names-only count of FBCK files on origin/claude/referee,
  14 at 00:13:33Z and at 00:42:38Z) and declared one read of docs/referee/R-N5-READER.md @ e83fd19d l. 1-30 (another packet, READER: the
  premise of Corollary (ii)), to check that implication; REFEREE's §C: "No effect on any verdict". §C (both): verdicts identical; joint gap
  map EMPTY; FBCK-N1 = N-FBCK-1 (REFEREE's wording with its proof; supersedes the σ̄ half of N-FBCK-1; the scope half stands for both),
  FBCK-N2, FBCK-N3 and FBCK-N4 AGREED by REFEREE-2, N-FBCK-2..4 ACCEPTED by REFEREE, N-FBCK-5 no conflict; nothing open.
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (a per-phase reduction of N5's in-phase fallback count to a configuration count; no
  running-time bound, no algorithm claim). GAPS G-N5-TIME: open.

### R82 [refereed-only] N5 on EVERY game, inside one phase: on states [a, b] of one phase with (H1′) every transition an S4a step (no fallback) and τ, λ constant (λ_W need not be constant), (H2) σ̄_t = σ̄_a on [a, b], (H3′) every W-cycle of state b a W-cycle at every state of [a, b] and every honest cycle of b an honest cycle at every state of [a, b] (T_W, T_H the vertices of those end-state cycles, T := T_W ∪ T_H; the two frames' cycles may differ and other cycles may come and go), (H4′) the depth recursion (dW := 0 on T_W, dH := 0 on T_H, through τ (W) or σ̄ (honest) at Odd vertices and σ_b at Even vertices of T, d(v) := dW(v) := dH(v) := 1 + max(dW(σ_b v), dH(σ_b v)) at Even v ∉ T) well founded, equivalently the graph J_b on the Even vertices outside T (v → the first Even vertex outside T after v on v's W-play or honest play at b) acyclic, d(v) then being the number of vertices of a longest J_b-path from v, and GEN_W (RESULTS R77 (c)'s: for every v, different W-plays from v to the same cycle have different W-valuations), every vertex v has its W-play at b at every state of [a + dW(v), b] and its honest play at b at every state of [a + dH(v), b], so σ_t = σ_b on [a + max d, b] and b − a ≤ max d ≤ |Even ∖ T| ≤ n − 1 (Theorem STATIC-DEPTH′; its proof uses W-MONO and Ξ-SUCC at in-phase S4a transitions at which λ_W may change, a proof step signed by both referees for this entry: λ_W is not used); under RESULTS R77's (H1)-(H4), (H1′), (H3′) (with T_W = T_H) and (H4′) hold and d ≤ d*, so STATIC-DEPTH′ contains RESULTS R77 (c) (Remark); and a piece [a, b] (a maximal stretch of a fallback-free run of one phase with σ̄ constant), cut backwards into epochs that satisfy (H1′), (H2), (H3′) by construction, has b − a ≤ (CF + 1)·n − 1 transitions, CF the transitions of the piece at which a W-cycle or an honest cycle appears, if (H4′) holds at every epoch end, and GEN_W holds (Corollary EPOCH) (2026-10-29) — structural lemmas for N5 and a REDUCTION of a piece's length to its cycle-appearance count CF (CF is not bounded here; CONJECTURE PIECE, every piece ≤ n − 1 transitions, and CONJECTURE STATIC-DEPTH′-TIE, STATIC-DEPTH′ without GEN_W, are OPEN; not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C91.md, checker 81502454)
- Object (L-SI successor 21, Opus 5.5; frozen, unchanged during review): packet P-N5-SDPRIME, docs/si/P-N5-SDPRIME-box25.md, sha1
  54678c38a04842bd936a9bf4b241d47ad8ab90a3 (l-si freeze edc14c51, 2026-10-29T03:58:27Z; quote base 55e0bcbda; 12 quotes,
  experiments/si/rund/quotecheck.py "quotes=12 bad=0", pinned with the sha1 in experiments/si/check.sh; both referees measured the pin),
  Theorem STATIC-DEPTH′ extending RESULTS R77 (c); working note with data docs/si/N5-PIECE-box25.md (l-si 6bb0ec34). The referees' notes are
  collected by the lane in docs/si/P-N5-SDPRIME-fixes-box25.md (l-si fc0312e2, sha1 f0bc5f4594e67fa483738f51b9e99065c4b2a2c1, L-SI
  successor 21: F1-F6 for SDP-N2 = N-SD-5, SDP-N3 = N-SD-1, SDP-N4 = N-SD-2, SDP-N1 = N-SD-7, SDP-N5 ⊇ N-SD-3 with N-SD-4, N-SD-6; 12 quotes
  checked by script, experiments/si/rund/quotecheck.py "quotes=12 bad=0", pinned in experiments/si/check.sh with a shifted-line control); on
  trunk; repairs only, "This file changes NO signed statement" (fixes l. 3-4): F1 replaces the packet §1's citation of W-MONO and Ξ-SUCC
  (as R77 (c)'s landed steps "on in-phase S4a transitions (R77's (H1))") by a proof step signed by both referees, item (a) below; F2 makes
  the (SW) quote strictly verbatim; F3 rewords EPOCH's hypothesis ("if (H4′) holds at every epoch end, and GEN_W holds": GEN_W is a property
  of (G, τ)); F4-F6 are records and change no statement. The statements below are in that repaired wording.
  Setting (every game): N5 = SPEC S1-S5 (docs/new/N5-ssi-global.md) with FIX 1-4; state t = (σ_t, τ); phases as in RESULTS R80's setting
  (λ and τ constant). Ξ_t(v): the S1 valuation (c, P, ℓ) of v's honest play (σ_t at Even vertices, σ̄_t at Odd ones); W_t(v): that of v's
  (σ_t, τ)-play; ▷, ⊵ the S1 order, TOTAL on valuations (p′ injective, distinct sets have distinct signed weights); a valuation is a function
  of the play. A W-cycle (honest cycle) at t: a cycle of the successor map v ↦ σ_t(v) / τ(v) (v ↦ σ_t(v) / σ̄_t(v)), as a vertex sequence up
  to rotation; a vertex on such a cycle has that cycle as its play. Depths: dW(v) := 0 on T_W, dH(v) := 0 on T_H; Odd v: dW(v) := dW(τ v)
  (v ∉ T_W), dH(v) := dH(σ̄ v) (v ∉ T_H); Even v ∈ T_H ∖ T_W: dW(v) := dW(σ_b v); Even v ∈ T_W ∖ T_H: dH(v) := dH(σ_b v); Even v ∉ T:
  dW(v) := dH(v) := d(v) := 1 + max(dW(y), dH(y)), y := σ_b(v); max d is taken over Even v ∉ T (0 if there is none). n: the number of
  vertices.
- Claims signed (both referees "(Opus 5.5, D15)", L37), on every game; no item uses (P); premises LANDED: SPEC S1 (valuation, order), S2
  (Iσ), S4a (arena {σ(v)} ∪ Iσ(v); Even's one-player optimum), S4c (FALLBACK); RESULTS R15 (a) Lemma A and (d); RESULTS R18 (d) Lemma S (a)
  on S4a's arena, the standing premise P2 as listed in RESULTS R69; (SW) "every Even switch of N5 is to an edge of Iσ", as listed among
  RESULTS R72's landed premises; RESULTS R77 (c) (GEN_W's definition; its proof steps W-MONO and Ξ-SUCC, landed under R77's (H1), which
  includes λ_W constancy; for the Remark its (H1)-(H4), H_b and d*); RESULTS R80 (a) EVERY-SWITCH and R80's phase setting:
  (a) Facts used as proof steps, signed by both referees for this entry (SDP-N2 = N-SD-5, F1): W-MONO (P2 / R18 (d) Lemma S (a) at one S4a
      step) and Ξ-SUCC (R15 (a), (d) + (SW)) hold at every in-phase S4a transition; λ_W is not used. (W-MONO: W_{t+1} ⊵ W_t, since σ_t uses
      only arena edges and σ_{t+1} is pointwise W-optimal over the strategies using arena edges. Ξ-SUCC: Ξ_t(σ_t v) is non-decreasing along
      in-phase S4a transitions: if v keeps, Ξ_{t+1}(σ_t v) ⊵ Ξ_t(σ_t v) by R15 (a), (d); if v switches, (SW) gives Ξ_t(σ_{t+1} v) ▷ Ξ_t(σ_t v)
      and R15 (a), (d) give Ξ_{t+1}(σ_{t+1} v) ⊵ Ξ_t(σ_{t+1} v).) This extends RESULTS R77's landed facts, which are stated under λ_W
      constancy, to the transitions at which λ_W changes; STATIC-DEPTH′ needs it. REFEREE §C (d693a6fe): "SDP-N2 SETTLED (Lead's question):
      the extension of W-MONO and Ξ-SUCC to in-phase S4a transitions at which λ_W changes is a SIGNED PROOF STEP of this entry, not a note."
      REFEREE-2 §C C.3 (9784229a): "YES, it is signed as a proof step, with a citation repair." The (M2κ) citation R77 gives for Ξ-SUCC is
      replaced by R15 (a), (d) (N-SD-5: "fine but stronger than needed").
  (b) Theorem STATIC-DEPTH′ (§2): on states [a, b] of one phase with (H1′) every transition t → t + 1, a ≤ t < b, an S4a step (no fallback),
      τ and λ constant on [a, b] (λ_W need not be constant); (H2) σ̄_t = σ̄_a for t ∈ [a, b]; (H3′) every W-cycle at b is a W-cycle at every
      t ∈ [a, b], and every honest cycle at b is an honest cycle at every t ∈ [a, b] (T_W / T_H := the vertices of the W-cycles / honest
      cycles at b; T := T_W ∪ T_H; the two frames' cycles may differ, and other cycles may come and go); (H4′) the depth recursion of the
      setting is well founded; and GEN_W: every v has its W-play at b at every t ∈ [a + dW(v), b] and its honest play at b at every
      t ∈ [a + dH(v), b]. Hence σ_t = σ_b on [a + max d, b], and b − a ≤ max d ≤ |Even ∖ T| ≤ n − 1 (T ≠ ∅: every play ends in a cycle).
      (Induction along the recursion: item 1, an end-state cycle keeps its vertices settled from a and fixes σ_t = σ_b on Even vertices of T;
      items 2-3, settling passes back one step through Odd vertices and through Even vertices of the other frame's T; item 4 at Even v ∉ T:
      (A) y = σ_b(v) is kept or improving at v from a + max(dW(y), dH(y)) on, by (SW) and Ξ-SUCC; (B) W_{t+1}(v) = W_b(v) by P2's pointwise
      optimality and W-MONO; (C) the W-play of v at t + 1 ends in the same end-state cycle, and GEN_W makes it the play at b; item 5, a
      transition with σ unchanged would contradict R80 (a).) The proof does not use R77's (CV) (cycle vertices constant); item 1, from (H3′),
      replaces it, which is what lets other cycles come and go (N-SD-6 = F6, ACCEPTED by REFEREE).
  (c) (H4′)'s equivalence (§2; REFEREE: "SIGNED (checked by proof)"; REFEREE-2: "SIGN (proof steps; checked)"): the recursion is well
      founded ⇔ the graph J_b on the Even vertices outside T, with an edge v → v′ when v′ is the first Even vertex outside T after v on v's
      W-play at b or on v's honest play at b, is acyclic; and then d(v) is the number of vertices of a longest J_b-path from v, so
      max d ≤ |Even ∖ T|. Parenthesis: a cycle of the recursion that meets no Even vertex outside T would be a cycle of one frame's successor
      map at b outside that frame's end-state cycles, which does not exist.
  (d) Remark (§2): STATIC-DEPTH′ contains RESULTS R77 (c). Under R77's (H1)-(H4): (H1) gives (H1′); (H3) gives (H3′) with T_W = T_H = the
      common cycle vertices; a J_b-edge follows σ_b at Even vertices and τ or σ̄ at Odd ones through vertices outside T, i.e. it is a path of
      R77's H_b, so (H4) gives (H4′); and d(v) ≤ R77's d*(v) (both count the Even non-cycle vertices of a path, J_b's paths being H_b's). So
      R77 (c)'s bound follows from STATIC-DEPTH′. New: the W- and honest cycles may differ, cycles other than the end state's may come and go,
      and λ_W may change.
  (e) Corollary EPOCH (§3, with F3), a REDUCTION. A PIECE: a maximal stretch [a, b] of states of a fallback-free run of one phase on which σ̄
      is constant (so (H1′), (H2) hold on it). Epochs: b_k := b; a_k := the least state of [a, b_k] such that every W-cycle (honest cycle) of
      state b_k is a W-cycle (honest cycle) at every state of [a_k, b_k]; then b_{k−1} := a_k − 1, and so on down to a; each epoch
      [a_i, b_i] satisfies (H1′), (H2), (H3′) with end state b_i, by construction. CF := the transitions t → t + 1 of [a, b] at which some
      W-cycle (honest cycle) of state t + 1 is not a W-cycle (honest cycle) of state t. Claim: if (H4′) holds at every epoch end b_i, and
      GEN_W holds, then |[a, b]| = b − a = Σ_i (b_i − a_i) + (k − 1) ≤ k(n − 1) + k − 1, and k − 1 ≤ CF; so b − a ≤ (CF + 1)·n − 1. (STATIC-DEPTH′
      per epoch; for i ≥ 2 the minimality of a_i gives a cycle of b_i that appears at a_i − 1 → a_i, and these k − 1 transitions are distinct.)
- Not signed: the packet's §4 (as the packet says): the DATA, CONJECTURE PIECE (every piece has ≤ n − 1 transitions, OPEN) and CONJECTURE
  STATIC-DEPTH′-TIE (STATIC-DEPTH′ without GEN_W, OPEN). The packet §1's premise line as written (W-MONO and Ξ-SUCC cited as R77 (c)'s landed
  steps, whose scope (H1) includes λ_W constancy, which (H1′) drops): it does not cover the transitions at which λ_W changes; not false;
  repaired by F1 into (a). The packet's (SW) quote with "…" where the source has only a line break (SDP-N3 = N-SD-1; content identical;
  repaired by F2). EPOCH's "GEN_W at every epoch end" as written (SDP-N4 = N-SD-2: redundant, GEN_W being a property of (G, τ) with τ fixed on
  the phase; reworded by F3).
- Honest limits: (i) EPOCH is a REDUCTION, not a bound: CF is not bounded, nor is the number of pieces of a phase. CONJECTURE PIECE stays
  OPEN; the packet's §3: "CONJECTURE PIECE ... reduces to the pieces with CF ≥ 1". READING (Lead), from EPOCH's construction: a piece in which
  every cycle of its end state b is a cycle at every state of the piece is one epoch (k = 1), and then (H4′) at b and GEN_W give b − a ≤ n − 1
  by STATIC-DEPTH′; so the pieces this entry leaves open are those in which an end-state cycle forms inside the piece (a cycle of b appears
  at a transition of the piece), besides those where (H4′) fails at an epoch end or GEN_W fails. (ii) GEN_W is a hypothesis; CONJECTURE
  STATIC-DEPTH′-TIE is OPEN (the conclusion held wherever the used form of GEN_W failed: packet §4, 22 pieces; REFEREE 161 intervals;
  REFEREE-2 132 + 173). (iii) Thin spots (SDP-N5 ⊇ N-SD-3, F5): "other cycles come and go" is exercised in only 3 + 0 + 3 intervals
  (REFEREE-2; REFEREE did not count it); EPOCH with CF ≥ 1 on few pieces (REFEREE 25 / 41 / 137 / 438; REFEREE-2 24 + 50 with every
  hypothesis), and (CF + 1)n − 1 is far from reached (no piece longer than n − 1 in any referee's data); MUT=1 (settling from d − 1) bites
  only where the bound is sharp. The other new freedoms are well exercised: T_W ≠ T_H in 3,409 intervals (REFEREE, all corpora) and 6,158 +
  4,811 + 159 (REFEREE-2), λ_W changing in 585 and 562 + 681 + 159. (iv) Every hypothesis carries weight in data: (H4′) is not vacuous
  (N-SD-4 = F5: fails at 4 + 28 (H3′)-intervals, REFEREE-2; 4 + 2 + 1 (H4′) failures in the lane's data (alt_all, lib41, random; F5 counts the first two), N5-PIECE-box25 §2); both halves of (H3′) (REFEREE MUT2,
  W-cycles only: SDV 77, SD 1, SB 1 on lib41; REFEREE-2 onlyH 3,009 + 38 with the length bound failing 23 + 1 times, onlyW 368 + 30, LEN 7);
  the dH half of d (REFEREE MUT3, W-frame depth only: SD 17, SDV 3,924 on lib41); honest-cycle appearances in CF (REFEREE MUT4: 5 + 2 on k − 1 ≤ CF); the depth is exact
  (REFEREE MUT1 14,126 on lib41; REFEREE-2 dm1 19,355 + 923), and b − a = max d is attained (REFEREE 369 / 383 / 359 / 152 intervals,
  REFEREE-2 369 + 429). (v) Nothing here bounds N5's running time.
- Data (DATA, not proof): the packet's §4 (lane, experiments/si/piece/sdprime.py and epochs.py; one engine, n5x; DEFAULT S3 starts, F4):
  STATIC-DEPTH′'s hypotheses hold on 844 of 872 alt_all pieces (R77's: 708), 914 / 943 lib41, 940 / 1,080 random 𝒞^kO; 0 violations of the
  per-vertex settling, of b − a ≤ max d and of b − a ≤ n − 1; MUT=1 (d − 1) fails 912 / 74 times; EPOCH ≤ 6 epochs and CF ≤ 5 per piece, 0
  violations; pieces outside STATIC-DEPTH′ ≤ 0.43(n − 1) in alt_all, a climb found none above 0.71(n − 1). Recount with the pinned starts
  (F4, piece/sdprime_alt_start.txt): 1,140 alt_all pieces (1,131 without the 9 games with no Odd choice vertex), (H3′) fails 25, (H4′) 2, the
  hypotheses hold on 1,113 (97.6 %; the 9 GEN_W-failure pieces counted, not excluded), 0 violations. REFEREE (successor 17; own
  docs/referee/scratch/sdprime_probe.py (sha1 11d9b745…) on its engine rl_engine; lane code not run; 0 failures in every MUT=0 run):
  alt_all (413 games, n ≤ 600, given start else S3; 413 runs) 4,791 STATIC-DEPTH′ intervals (905 with T_W ≠ T_H, 153 with λ_W changing),
  pieces 5,765 (1,132 with ≥ 1 transition), the hypotheses on 1,098 of 1,132 (97.0 %) and R77's on 918 (81.1 %); lib41 (727 runs) 5,440
  intervals; lib1140 (1,857 runs) 7,929; random rand_ck (n 6-20, k ≤ 6; 12,000 runs) 2,175; Remark: (H3′) and max(dW, dH) ≤ d* at 3,878 +
  4,538 + 6,380 + 2,080 R77 instances, 0 failures; at most 6 epochs and CF ≤ 5 per piece; λ_W-changing in-phase S4a transitions: W-MONO and
  Ξ-SUCC 0 failures at 285 (alt_all) + 214 (lib41) (scratch/lw_facts.py). REFEREE-2 (successor 19; own
  docs/referee-2/R2-N5-SDPRIME/sdprime_check.py on its lane's Runner (si.py); lane tools not run; every non-mutation run 0 violations):
  alt_all (413 runs) 1,133 pieces, 32,404 (H3′)-intervals (every sub-interval of a piece up to length 60); lib41_noref × 3 (1,230 runs)
  1,812 pieces, 52,303 intervals; named (8 runs) 91 pieces, 634 intervals; random kO / k2 / k4 (24,000 runs); item 4 (A) checked at
  10,540,227 + 8,589,064 + 38,414 instances, (B) at 9,531,639 + 7,602,983 + 29,715; H4EQ and DEQ ((c)) 0 failures; Remark on 26,103 + 47,270
  + 475 R77 intervals, 0 failures; EPOCH's cut, sum, appearance and length checks 0 failures; W-MONO and Ξ-SUCC 0 failures at 283 + 657 + 24
  + 56 λ_W-changing transitions; longest STATIC-DEPTH′ interval 55 transitions (x32_rand64, n 64, max d 56). Piece counts (SDP-N1 = N-SD-7,
  F4): the referees agree with each other (alt_all pieces with ≥ 1 transition: 1,132 and 1,133); the lane found the cause of §4's 872: its
  corpus run used the default S3 start for every file (the list's second column, a pinned .start file on 94 of its 413 lines, was not
  read); the remaining 1-9 difference to 1,140 / 1,131 is not determined (fixes F4). No signed statement uses any count.
- Signatures: REFEREE docs/referee/R-N5-SDPRIME.md (report 573d2695, sha1 47d5287569a739ec4e491e26fb1a263ee785733f there; §C d693a6fe;
  successor 17): STATIC-DEPTH′ SIGNED; (H4′)'s "Equivalently" and its parenthesis SIGNED (checked by proof); the Remark (contains R77 (c))
  SIGNED; Corollary EPOCH SIGNED (a REDUCTION: CF unbounded); quotes 12/12 (own scratch/flip_quotes.py, which treats "…" as a separator);
  notes SDP-N1..N5; no gap. REFEREE-2 docs/referee-2/R2-N5-SDPRIME.md (report bf48b8f4, sha1 e12e36413fe3e7e25ca9eea63fbe6c67c67ab94c there;
  §C 9784229a; successor 19): STATIC-DEPTH′ SIGN; (H4′)'s equivalence and d(v) = vertices of a longest J_b-path SIGN (proof steps; checked);
  the Remark SIGN; Corollary EPOCH SIGN (a REDUCTION; GEN_W wording, N-SD-2); quotes 11/12 strictly verbatim, the twelfth with a spurious
  "…" (N-SD-1, content identical), SHIFT=1 control 0/12; notes N-SD-1..7; no gap. INDEPENDENCE: REFEREE opened no docs/referee-2/ file on
  SDPRIME (names only at 04:33Z: 0 on its tree, 25 on origin/claude/referee-2, 18 on trunk docs/referee-2/; none read) and ran no lane code;
  REFEREE-2 opened no docs/referee/ file on SDPRIME before pushing bf48b8f4 (names-only count 0 at 04:04:20Z and at 04:12:45Z) and ran no
  lane tool. §C (both): verdicts identical (STATIC-DEPTH′, (H4′)'s equivalence with d = longest J_b-path count, the Remark, EPOCH); joint
  gap map EMPTY; SDP-N2 = N-SD-5 SETTLED as a signed proof step (item (a)); SDP-N3 = N-SD-1, SDP-N4 = N-SD-2, SDP-N1 = N-SD-7 matched;
  SDP-N5 ⊇ N-SD-3, N-SD-4 and N-SD-6 ACCEPTED by REFEREE; quotes 12/12 in content, one cosmetic "…"; nothing open.
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (structural lemmas on N5 inside one phase and a reduction of a piece's length to
  its cycle-appearance count; no running-time bound, no algorithm claim). GAPS G-N5-TIME: open.

### R83 [refereed-only] N5 on EVERY game, inside one phase: at an in-phase S4a transition t → t + 1, a change y1 := σ̄_t(u) ≠ y2 := σ̄_{t+1}(u) of Odd's best reply at an Odd vertex u with (i) u on no honest cycle at t and at t + 1, (ii) y2's honest t-play not through u, and (iii) Ξ_t(y1) ≠ Ξ_t(y2) strictly raises Ξ at u itself, Ξ_{t+1}(u) ▷ Ξ_t(u) (Lemma GATE-RISE: the strict form, in Ξ and for every Odd u, of RESULTS R61 (e) Lemma ALT, proved without R61's conditionality on R56 and R58), so on a run S (a maximal stretch of states of one phase with no fallback between them) G(S) ≤ Σ_u (XR_S(u) + TIE_S(u) + CYC_S(u) + THRU_S(u)) over the Odd vertices u of out-degree ≥ 2, G(S) the σ̄-changing transitions of S, XR_S(u) the transitions of S changing Ξ(u), and TIE_S(u), CYC_S(u), THRU_S(u) the σ̄(u)-changes of S at which (iii) fails, (i) fails, and (i) holds but (ii) fails (its Count); with E_2 the Even vertices of out-degree ≥ 2 and, at a state b of S, X_b the least set of Even vertices containing E_2 and every Even vertex on the W-play or honest play at b of one of its members, V^W_b (V^H_b) the vertices on the W-plays (honest plays) at b of the members of X_b (every Even vertex of V^W_b ∪ V^H_b is in X_b, and V^W_b (V^H_b) is closed under the W-successor (honest successor) at b), RO_b the Odd vertices on those honest plays, CW_b (CH_b) the W-cycles (honest cycles) at b on which those W-plays (honest plays) end, T_W, T_H their vertices and T := T_W ∪ T_H: if states [a, b] of S are REL-ADMISSIBLE (σ̄_t(u) = σ̄_b(u) for every u ∈ RO_b and t ∈ [a, b], and every cycle of CW_b (CH_b) a W-cycle (honest cycle) at every t ∈ [a, b]; σ̄ may move at Odd vertices outside RO_b, and other cycles may come and go), (H4′_rel) the depth recursion on V^W_b and V^H_b (dW := 0 on T_W, dH := 0 on T_H, through τ (W) or σ̄_b (honest) at Odd vertices and σ_b at Even vertices of T, d(v) := dW(v) := dH(v) := 1 + max(dW(σ_b v), dH(σ_b v)) at Even v ∉ T; it stays in its domains) is well founded, and GEN_W (RESULTS R77 (c)'s: for every v, different W-plays from v to the same cycle have different W-valuations) holds, then every v ∈ V^W_b has its W-play at b at every state of [a + dW(v), b] and every v ∈ V^H_b its honest play at b at every state of [a + dH(v), b], so σ_t = σ_b on [a + max_{v ∈ E_2 ∖ T} d(v), b] and b − a ≤ max_{v ∈ E_2 ∖ T} d(v) ≤ |Even ∖ T| ≤ n − 1 (Theorem STATIC-DEPTH-REL; its proof uses W-MONO and Ξ-SUCC at in-phase S4a transitions at which λ_W may change, a proof step signed by both referees for this entry: λ_W is not used); and a run S cut from its end into SEG(S) maximal REL-admissible segments [a_i, b_i] has |S| = Σ_i (b_i − a_i) + SEG(S) − 1 ≤ SEG(S)·n − 1 transitions if (H4′_rel) and GEN_W hold at every segment end b_i, each cut a_i − 1 → a_i (i ≥ 2) being a transition at which σ̄ changes at a vertex of RO_{b_i} or a cycle of CW_{b_i} ∪ CH_{b_i} appears, so SEG(S) − 1 ≤ G(S) + CF(S), CF(S) the transitions of S at which a W-cycle or an honest cycle appears (Corollary REL-SPLIT) (2026-10-29) — structural lemmas for N5 and a REDUCTION of a run's length to its segment count SEG (SEG is not bounded here; CONJECTURE SEG-RUN, SEG = O(n), is OPEN, and with REL-SPLIT it would give O(n²) transitions per run on runs where (H4′_rel) and GEN_W hold at every segment end, not O(n); not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C92.md, checker 76272f51)
- Object (L-SI successor 21, Opus 5.5; frozen, unchanged during review): packet P-N5-REL, docs/si/P-N5-REL-box25.md, sha1
  f79300a2d01cfb0aa27ad7214bcefbd84eafd7bb (l-si freeze 07f19760, 2026-10-29T04:13:22Z; quote base b28123a58; 17 quotes,
  experiments/si/rund/quotecheck.py "quotes=17 bad=0", pinned with the sha1 in experiments/si/check.sh; both referees measured the pin),
  Lemma GATE-RISE with its Count, Theorem STATIC-DEPTH-REL and Corollary REL-SPLIT. SELF-CONTAINED: the packet's §2 proves STATIC-DEPTH-REL
  in full and does not use P-N5-SDPRIME's Theorem STATIC-DEPTH′ (packet l. 8-9). Working note with data docs/si/N5-GRUN-box25.md (l-si
  3433460b). The referees' notes are collected by the lane in docs/si/P-N5-REL-fixes-box25.md (l-si 843cf5b5, sha1
  16a74626d77dddc088a573005481360d6ab2b699, L-SI successor 21: F1-F9 for REL-N1, REL-N2 = N-REL-6, REL-N3 = N-REL-4, REL-N5 = N-REL-1,
  REL-N4 ~ N-REL-7, N-REL-2, N-REL-3, N-REL-5, N-REL-8; 12 quotes checked by script, experiments/si/rund/quotecheck.py "quotes=12 bad=0",
  pinned in experiments/si/check.sh with a shifted-line control); on trunk; repairs only, "This file changes NO signed statement" (fixes
  l. 3-4): F1 cites RESULTS R61 (e) Lemma ALT for GATE-RISE (REL-N1); F2 replaces the packet's citation of W-MONO and Ξ-SUCC (as RESULTS R77
  (c)'s landed steps "on in-phase S4a transitions") by a proof step signed by both referees, item (a) below (REL-N2 = N-REL-6); F3 renames
  the packet §2's Q (the Even vertices of out-degree ≥ 2) to E_2, the fleet's Q being the Odd vertices of out-degree ≥ 2 (REL-N3 =
  N-REL-4); F4 makes the (SW) quote strictly verbatim (REL-N5 = N-REL-1); F6 rewords GATE-RISE's step 3 (N-REL-2); F8 corrects the scope of
  the not-signed Remark (N-REL-5); F5, F7, F9 are records and change no statement. The statements below are in that repaired wording.
  Setting (every game): N5 = SPEC S1-S5 (docs/new/N5-ssi-global.md) with FIX 1-4; state t = (σ_t, τ); phases as in RESULTS R80's setting
  (λ and τ constant). A RUN S: a maximal stretch of states of one phase with no fallback between them; its transitions are in-phase S4a
  steps (λ_W, the W-frame's cycle-node map, need not be constant on S). Ξ_t(v): the S1 valuation (c, P, ℓ) of v's honest play (σ_t at Even
  vertices, σ̄_t at Odd ones); W_t(v): that of v's (σ_t, τ)-play; ▷, ⊵ the S1 order, TOTAL on valuations (p′ injective, distinct sets have
  distinct signed weights); a valuation is a function of the play; u ⊕ x: the valuation of the play u followed by a play of valuation x
  (RESULTS R17 (a) (V1)). A W-cycle (honest cycle) at t: a cycle of the successor map v ↦ σ_t(v) / τ(v) (v ↦ σ_t(v) / σ̄_t(v)), as a vertex
  sequence up to rotation; a vertex on such a cycle has that cycle as its play. For a run S: G(S) := the transitions of S with σ̄_t ≠
  σ̄_{t+1}; CH_S(u) := the σ̄(u)-changes of S; XR_S(u) := the transitions of S at which Ξ(u) changes; CF(S) := the transitions of S at which
  a W-cycle or an honest cycle appears. E_2 := the Even vertices of out-degree ≥ 2 (F3). X_b, V^W_b, V^H_b, RO_b, CW_b, CH_b, T_W, T_H, T at a
  state b of S as in the title. Depths: dW on V^W_b, dH on V^H_b: dW(v) := 0 for v ∈ T_W; dH(v) := 0 for v ∈ T_H; Odd v: dW(v) := dW(τ v)
  (v ∉ T_W), dH(v) := dH(σ̄_b v) (v ∉ T_H); Even v ∈ T_H ∖ T_W: dW(v) := dW(σ_b v); Even v ∈ T_W ∖ T_H: dH(v) := dH(σ_b v); Even v ∉ T:
  dW(v) := dH(v) := d(v) := 1 + max(dW(y), dH(y)), y := σ_b(v); max ∅ := 0. (H4′_rel): this recursion is well founded. n: the number of
  vertices.
- Claims signed (both referees "(Opus 5.5, D15)", L37), on every game; no item uses (P); premises LANDED: SPEC S1 (valuation, order, Ξσ
  against σ̄), S2 (Iσ), S4a (arena {σ(v)} ∪ Iσ(v); Even's one-player optimum), S4c (FALLBACK); RESULTS R15 (a) Lemma A and (d); RESULTS R17
  (a) (V1), (V2); RESULTS R57 (a) premise (VJ); RESULTS R18 (d) Lemma S (a) on S4a's arena, the standing premise P2 as listed in RESULTS R69;
  (SW) "every Even switch of N5 is to an edge of Iσ", as listed among RESULTS R72's landed premises; RESULTS R77 (c) (GEN_W's definition;
  its proof steps W-MONO and Ξ-SUCC, landed under R77's (H1), which includes λ_W constancy, are replaced here by item (a)); RESULTS R80 (a)
  EVERY-SWITCH and R80's phase setting. RESULTS R61 (e) Lemma ALT (landed, CONDITIONAL on RESULTS R56 and R58) is cited for comparison only
  (item (b)); no item uses it as a premise. No item uses P-N5-SDPRIME or STATIC-DEPTH′.
  (a) Facts used as proof steps, signed by both referees for this entry (REL-N2 = N-REL-6, F2): (W-MONO) W_{t+1} ⊵ W_t at every in-phase S4a
      transition (P2; RESULTS R18 (d) Lemma S (a), at one S4a step); (Ξ-SUCC) Ξ_t(σ_t v) non-decreasing along in-phase S4a transitions
      (RESULTS R15 (a), (d) and (SW)); λ_W is not used. (W-MONO: σ_t uses only arena edges, and σ_{t+1} is pointwise W-optimal over the
      strategies using arena edges. Ξ-SUCC: if v keeps, Ξ_{t+1}(σ_t v) ⊵ Ξ_t(σ_t v) by R15 (a), (d); if v switches, (SW) gives
      Ξ_t(σ_{t+1} v) ▷ Ξ_t(σ_t v) and R15 (a), (d) give Ξ_{t+1}(σ_{t+1} v) ⊵ Ξ_t(σ_{t+1} v).) This extends RESULTS R77's landed facts, which are
      stated under λ_W constancy, to the transitions at which λ_W changes; STATIC-DEPTH-REL needs it on runs, which do not fix λ_W.
      REFEREE §C (a343d6b4): "REL-N2 = N-REL-6 (W-MONO / Ξ-SUCC at λ_W changes; the same signed proof step as SDPRIME's §C)." REFEREE-2 §C
      (b6811cf1): "REL-N2 (W-MONO / Ξ-SUCC beyond R77 (H1)) = N-REL-6. The same signed proof step as SDPRIME §C.3. Identical." REFEREE-2's
      N-REL-6: "Both facts hold at every in-phase S4a transition: P2 at one step, and R15 (a), (d) with (SW)." The (M2κ) citation R77 gives
      for Ξ-SUCC is replaced by R15 (a), (d) (F2).
  (b) Lemma GATE-RISE (§1, with F1 and F6): let t → t + 1 be an in-phase S4a transition and u an Odd vertex with σ̄_t(u) = y1 ≠ y2 =
      σ̄_{t+1}(u), such that (i) u is on no honest cycle at t and at t + 1, (ii) y2's honest t-play does not pass through u, (iii) Ξ_t(y1) ≠
      Ξ_t(y2). Then Ξ_{t+1}(u) ▷ Ξ_t(u). (Step 1, (i) and (V1): Ξ_t(u) = u ⊕ Ξ_t(y1), Ξ_{t+1}(u) = u ⊕ Ξ_{t+1}(y2). Step 2: τ′ := σ̄_t with u's
      choice changed to y2; by (ii) y2's (σ_t, σ̄_t)-play is also its (σ_t, τ′)-play and u's (σ_t, τ′)-play is u followed by it, so
      V_{σ_t,τ′}(u) = u ⊕ Ξ_t(y2), and (VJ) gives u ⊕ Ξ_t(y1) ⊴ u ⊕ Ξ_t(y2). Step 3 (F6): "x ↦ u ⊕ x is strictly monotone on the values of
      plays avoiding u: monotone by (V2); for two such x with the same cycle node c it adds u to both path sets or to neither and 1 to both
      lengths, so the comparison is unchanged and x is recovered; for different cycle nodes u ⊕ keeps each cycle node, so the order (decided
      by the cycle nodes) is kept"; Ξ_t(y1) and Ξ_t(y2) are values of plays avoiding u, by (i) and (ii); with (iii) and totality, Ξ_t(y1) ◁
      Ξ_t(y2). Step 4: R15 (a), (d) give Ξ_{t+1}(y2) ⊵ Ξ_t(y2), so Ξ_{t+1}(u) = u ⊕ Ξ_{t+1}(y2) ⊵ u ⊕ Ξ_t(y2) ▷ u ⊕ Ξ_t(y1) = Ξ_t(u).) F1
      (REL-N1): "GATE-RISE is the strict form, in Ξ and for every Odd u (not only u ∈ Q_c), of RESULTS R61 (e) Lemma ALT; its proof here uses
      only R57 (a), R17 (a) and R15 (a), (d), so it does not inherit R61's conditionality on R56 and R58." (R61 (e), landed: a clean change at
      q ∈ Q_c, q ≠ c, "has κ_{t+1}(q) ≥ κ_t(q), with equality only if κ_t(y2) = κ_t(y1) and κ_{t+1}(y2) = κ_t(y2) (a TIE at t)".) REFEREE
      (report §1): "GATE-RISE is the strict form of RESULTS R61 (e) Lemma ALT"; REFEREE-2 §C C.3: "ACCEPTED, MISSED by me", after reading
      R61 (e)'s landed text.
  (c) Its Count (§1): for a run S and an Odd u, every σ̄(u)-change of S is clean ((i)-(iii) hold), TIE ((iii) fails), CYC ((i) fails) or
      THRU ((i) holds, (ii) fails) (the kinds may overlap; the sum still bounds), and each clean change is a transition at which Ξ(u) changes;
      so CH_S(u) ≤ XR_S(u) + TIE_S(u) + CYC_S(u) + THRU_S(u), and, summing over the Odd vertices of out-degree ≥ 2 (every σ̄-changing
      transition changes σ̄ at one of them), G(S) ≤ Σ_u (XR_S(u) + TIE_S(u) + CYC_S(u) + THRU_S(u)).
  (d) Theorem STATIC-DEPTH-REL (§2, with F3), the domain-closure sentences of its definitions included (REFEREE: "SIGNED, including the
      domain-closure sentences of the definitions"; REFEREE-2: "SIGN (RCLOSE / RDOM checked)"). Definitions at a state b of a run S as in the
      Setting; every Even vertex of V^W_b ∪ V^H_b is in X_b, and V^W_b (V^H_b) is closed under the W-successor (honest successor) at b; the
      recursion stays in its domains: τ(v) (Odd v) and σ_b(v) (Even v) of v ∈ V^W_b are on the same W-play, so in V^W_b; σ̄_b(v), σ_b(v) of
      v ∈ V^H_b likewise in V^H_b; for Even v ∉ T, v ∈ X_b and y = σ_b(v) lies on both of v's b-plays, so y ∈ V^W_b ∩ V^H_b. [a, b] ⊆ S is
      REL-ADMISSIBLE if σ̄_t(u) = σ̄_b(u) for every u ∈ RO_b and t ∈ [a, b], and every cycle of CW_b (CH_b) is a W-cycle (honest cycle) at every
      t ∈ [a, b]. Statement: let [a, b] ⊆ S be REL-admissible, with (H4′_rel) and GEN_W. Then every v ∈ V^W_b has its W-play at b at every
      t ∈ [a + dW(v), b], and every v ∈ V^H_b its honest play at b at every t ∈ [a + dH(v), b]; σ_t = σ_b for t ∈ [a + max_{v ∈ E_2 ∖ T} d(v),
      b]; and b − a ≤ max_{v ∈ E_2 ∖ T} d(v) ≤ |Even ∖ T| ≤ n − 1 (T ≠ ∅ when E_2 ≠ ∅; if E_2 = ∅ there is no in-phase S4a step and b = a).
      (Induction along the well-founded recursion: item 1, a cycle of CW_b (CH_b) is a W-cycle (honest cycle) at every t, so its vertices are
      settled from a, and an Even v ∈ T has σ_t(v) = σ_b(v); item 2, Odd v ∈ V^W_b ∖ T_W settles through τ(v), and Odd v ∈ V^H_b ∖ T_H lies in
      RO_b, where REL-admissibility fixes σ̄(v) on [a, b], and settles through σ̄_b(v), the only use of σ̄; item 3, Even vertices of the other
      frame's T settle through σ_b(v); item 4 at Even v ∉ T (so v ∈ X_b): (A) y = σ_b(v) is kept or improving at v from a + max(dW(y), dH(y))
      on, by (SW), Ξ-SUCC and y's H-settledness; (B) W_{t+1}(v) = W_b(v) by P2's pointwise optimality and W-MONO; (C) v's W-cycle at b is in
      CW_b, so v's W-play at t + 1 ends in it, and GEN_W makes it the play at b, whence σ_{t+1}(v) = y and v's honest play at t + 1 is its
      honest play at b; item 5, from a + max_{E_2 ∖ T} d on σ_t = σ_b on E_2 (items 1, 4), the other Even vertices have out-degree 1, and a
      further transition would contradict R80 (a); a longest recursion path from v ∈ E_2 ∖ T visits distinct Even vertices outside T.)
  (e) Corollary REL-SPLIT (§3, with F3), a REDUCTION. Cut a run S = [s, e] from its end: b_k := e; a_k := the least state of [s, b_k] with
      [a_k, b_k] REL-admissible (with respect to b_k's sets); then b_{k−1} := a_k − 1, and so on down to s; SEG(S) := k. Claim: if (H4′_rel)
      and GEN_W hold at every b_i, then |S| = e − s = Σ_i (b_i − a_i) + SEG − 1 ≤ SEG·n − 1; every cut a_i − 1 → a_i (i ≥ 2) is a transition at
      which σ̄ changes at a vertex of RO_{b_i} or a cycle of CW_{b_i} ∪ CH_{b_i} appears; hence SEG − 1 ≤ G(S) + CF(S). (REL-admissibility of
      [x, b_i] for b_i's sets is monotone in x, so a_i is well defined; STATIC-DEPTH-REL on each segment gives b_i − a_i ≤ n − 1; for i ≥ 2,
      [a_i − 1, b_i] is not REL-admissible though [a_i, b_i] is, so σ̄_{a_i − 1}(u) ≠ σ̄_{b_i}(u) = σ̄_{a_i}(u) for some u ∈ RO_{b_i}, or a cycle of
      CW_{b_i} ∪ CH_{b_i}, a cycle at a_i, is not one at a_i − 1; the cuts are distinct transitions.) REFEREE: "SIGNED (a REDUCTION: SEG
      unbounded)"; REFEREE-2: "SIGN (a REDUCTION)".
- Not signed: the packet's §4 (as the packet says): the DATA, the reader-proofness READING ("a reader is on no play of another vertex, an
  anchor's plays are its own loop") and CONJECTURE SEG-RUN (SEG(S) = O(n), OPEN). The packet's §2 Remark (not in its to-sign table), as
  written "STATIC-DEPTH-REL contains STATIC-DEPTH′ (P-N5-SDPRIME) and, through it, RESULTS R77 (c)": its corrected scope (N-REL-5 = F8;
  REFEREE ACCEPTED it in its §C, correcting its own "true as stated") is "STATIC-DEPTH-REL contains STATIC-DEPTH′'s length bound and its
  per-vertex settling on V^W_b ∪ V^H_b; it does not give STATIC-DEPTH′'s settling at other vertices" (e.g. a reader). STATIC-DEPTH′ is
  P-N5-SDPRIME's theorem (RESULTS R82 (landed)); no signed item of this entry uses it. GATE-RISE's remark that (i) at t + 1 can
  be weakened to u ≠ λ(u) (REL-N1; F1: "remark, not signed"; REFEREE §1: "Not needed for any signed statement", 4 data cases, all rising;
  REFEREE-2 §C C.3: "The weakening holds", 1 + 4 own cases); (i) at t stays (REFEREE-2's cyc control: 8 of 23 CYC changes without a rise);
  REFEREE-2's further data on a weakening at t ("a data point, not a checked statement. Not proposed for signature"). The packet's wording
  as frozen, repaired by the fixes and not false: GATE-RISE without the R61 (e) citation (F1); W-MONO and Ξ-SUCC cited as R77 (c)'s landed
  steps, whose scope (H1) includes λ_W constancy (F2); Q for the Even vertices of out-degree ≥ 2 (F3; "The statement is unambiguous as
  written, since §2 defines it", REFEREE-2 N-REL-4); the (SW) quote with "…" where the source has only a line break (F4; content
  identical); step 3's injectivity sentence without "u-free" (F6; both values it is applied to are u-free).
- Honest limits: (i) REL-SPLIT is a REDUCTION, not a bound: SEG is not bounded here, nor are the runs of a phase or the phases. CONJECTURE
  SEG-RUN (SEG = O(n)) is OPEN; its DATA bound is SEG ≤ 1.00n over all starts (F5: max SEG / n 0.79 on alt_all with default S3 and with
  pinned starts, REFEREE 0.83 on lib41 and lib1140 (run_m_n24, SEG 20 at n 24), REFEREE-2 0.95 (lib41 lev_l_n20, random start), the lane's
  climb 1.00 (grun/out/sg_2, SEG 29 at n 29)). READING (Lead): with SEG-RUN, REL-SPLIT gives |S| ≤ SEG·n − 1 = O(n²) transitions per run, not
  O(n), and only on runs where (H4′_rel) and GEN_W hold at every segment end. (ii) G is not intrinsic (the lane's DATA and READING,
  N5-GRUN-box25 §3, not refereed as a claim): Odd readers (no predecessors) lift G on runfam_K10 from 9 to 91 at n 74 (grun/out/rdr_K10,
  .pg sha1 a7ac4830…) with the run fixed (99 transitions), and Even anchors put the readers into RESULTS R81's K with G^K 91 at n 99
  (grun/out/anc_K10, .pg sha1 13833299…); SEG stays 9 on all three. Reproduced: REFEREE on runfam_K10, rdr_K10, anc_K10 (G 9 / 91 / 91 inside
  the run, SEG 9; "So the readers inflate G tenfold and leave SEG unchanged"); REFEREE-2 on rdr_K10, anc_K10 (|S| = 99, G = 91, SEG = 9).
  READING (Lead): GATE-RISE's Count reduces G(S) to the gates' XR_S plus exception counts, and XR per vertex is not bounded (RESULTS R80:
  XR-LIN DEAD); REL-SPLIT's clause SEG − 1 ≤ G(S) + CF(S) bounds SEG by a count that readers inflate, so it is not a route to SEG-RUN; SEG
  itself was reader-proof in these instances (DATA). (iii) GEN_W and (H4′_rel) are hypotheses. Where GEN_W's used form fails the
  conclusions still held (REFEREE 34 / 52 / 76 intervals; REFEREE-2 132 + 164 + 1). (H4′_rel) is not vacuous: it fails at 45 of 1,908
  segment ends (lane, alt_all, default starts; 49 with pinned starts) and at 8 + 27 REL-admissible intervals (REFEREE-2); REFEREE: REL-SPLIT's
  hypotheses hold on 3,029 of 3,286, 4,279 of 4,353 and 11,229 of 11,445 runs; the other runs are not bounded by REL-SPLIT. (iv) The
  hypotheses carry weight in data: σ̄ constant on RO_b carries the length bound (REFEREE MUT4: SDV 26,383, SIG 1,274, LEN 283, SPLIT 3;
  REFEREE-2 nosbar: 212,050, including RLEN 1,450 and RSIG 1,450); GATE-RISE's (iii) (REFEREE MUT3 128 of 129 ties without a rise; REFEREE-2
  tie 167 of 168) and (i) (REFEREE-2 cyc 8 of 23) are needed; the depth is exact (REFEREE MUT1 SDV 15,442; REFEREE-2 dm1 18,837); X_b's
  closure is structurally needed (REFEREE-2 qonly: RDOM 246, RCLOSE 14,331; REFEREE's MUT5 did not bite because its depth routine is not
  restricted to the domains, REFEREE §C: "ACCEPTED"). Thin spot (N-REL-3 = F7): (ii) is not shown necessary in data (REFEREE MUT2: 13 THRU
  changes, all rising; REFEREE-2: 239; lane 73 + 176 + 56); it is used in step 2 and stays a hypothesis. (v) What the freedom buys (N-REL-8 =
  F9): REL-admissible intervals on which σ̄ moves at an Odd vertex off RO_b: REFEREE 789 + 495 + 1,122 + 175 (readers: 175 of 273);
  REFEREE-2 4,094 + 3,281 + 539 + 2,947 + 192 (lane instances: 2,947 of 3,012; REFEREE-2's logs carry the strict counter REL_sbar_moves_off_RO with these values; its wider REL_beyond_SDPRIME is equal in every log, and rel_check.py's _nonrel_cycle_breaks never fires). (vi) Nothing here bounds N5's running time.
- Data (DATA, not proof): the packet's §4 (lane, experiments/si/grun/gaterise.py and relseg.py; one engine, n5x): GATE-RISE 2,114 clean
  changes on alt_all (default S3 starts; TIE / CYC / THRU 75 / 8 / 73), 3,752 with pinned starts (82 / 10 / 176), 1,889 on lib41 (76 / 10 /
  56), 0 failures (grun/gaterise_alt.txt, _alt_start.txt, _lib41.txt); MUT (a strict rise of Ξ(y2) demanded instead) fails 1,892 times (packet
  §4; N5-GRUN-box25 §2); REL 1,908 segments on alt_all (2,890 with pinned starts), 0 violations, (H4′_rel) fails at 45 (49) ends, max SEG 26
  (62, gate_K64_n581), longest segment 67 (55) (grun/relseg_alt.txt, _alt_start.txt); MUT (d − 1) 994 (packet §4; N5-GRUN-box25 §4); max SEG /
  n 0.79 in both start sets (F5), ≤ 1.00n after climbs. REFEREE (successor 17; own docs/referee/scratch/rel_probe.py (sha1 4b35aabd…) on its
  engine rl_engine; lane code not run; 0 failures in every MUT=0 run; logs scratch/rel_logs/): alt_all (413 games, n ≤ 600, given start else
  S3) 413 runs (3,286 fallback-free runs S), GATE-RISE clean / TIE / CYC / THRU 3,700 / 82 / 10 / 118, 5,385 REL intervals (789 with σ̄ moving
  off RO_b), REL-SPLIT hypotheses on 3,029 / 3,286 runs, 1,951 cuts checked, max SEG / n 0.79; lib41 (n ≤ 48; given + S3 + 1 random) 727
  (4,353), 2,438 / 129 / 15 / 13, 5,814 (495), 4,279 / 4,353, 2,210, 0.83; lib1140 (n ≤ 40; given + S3 + 1 random; two halves) 1,857 (11,445),
  4,063 / 169 / 68 / 91, 8,741 (1,122), 11,229 / 11,445, 3,077, 0.83 (n ≥ 2; the only SEG = n case is the one-vertex strfam_S1_n1); readers
  (rdr_K10, anc_K10, runfam_K10; given starts) 3 (6), 445 / 22 / 0 / 0, 273 (175), 6 / 6, 24, 0.18; per-vertex settling, σ_t = σ_b, the length
  and the cap, the Count, REL-SPLIT's sum, cuts and SEG − 1 ≤ G + CF: 0 failures. REFEREE-2 (successor 19; own
  docs/referee-2/R2-N5-REL/rel_check.py (reusing its R2-N5-SDPRIME/sdprime_check.py) and seg_case.py; lane tools not run, lane instance files
  copied as inputs; every non-mutation run 0 violations; REL-admissible intervals up to length 60, RELCAP 60): alt_all (413 runs; given start
  else S3) GATE-RISE 3,713 / 82 / 10 / 125, 36,502 REL-admissible intervals (GEN_W used 36,362), Remark checks 32,400, runs S 920 (874 with
  the hypotheses), 2,874 segments; lib41_noref × 3 (1,230 runs) 3,751 / 168 / 23 / 109, 53,652 (53,461), 50,344, 1,612 (1,536) / 4,671; named
  (8 runs) 390 / 0 / 1 / 3, 1,173, 634, 48 (45) / 198; lane instances grun/out (28 runs) 870 / 71 / 9 / 0, 3,012, 65, 29 (29) / 407; random kO
  n 8-20 and k2 n 6-16 (18,000 runs) 325 / 55 / 70 / 2, 2,325 (2,324), 2,132, 2,518 (2,517) / 3,047; max SEG / n 0.792 on alt_all
  (so_sor5_n24), 0.95 on lib41 with a random start (lev_l_n20), 1.00 on sg_2; |S| / (SEG·n) ≤ 0.917 ("The bound is never reached"); longest
  REL interval 55 transitions (x32_rand64), sharp in 395 + 442 intervals; Remark (RREM, RREM_d): 0 on 85,575 checks. Run counts differ by
  definition: REFEREE's 3,286 counts every run, those of 0 transitions included (rel_probe.py l. 44-53), REFEREE-2's 920 only runs with ≥ 1
  transition (rel_check.py l. 46), the lane's 921 (pinned starts) likewise (grun/relseg.py l. 48); READING (Lead) of the three tools' code, no
  report states the cause; the remaining difference 920 / 921 is not determined. No signed statement uses any count.
- Signatures: REFEREE docs/referee/R-N5-REL.md (report 69b12910, sha1 8ae211bd760e7a7347cdc979e22a674c4ddd5d01 there; §C a343d6b4;
  successor 17): Lemma GATE-RISE SIGNED; its Count SIGNED; Theorem STATIC-DEPTH-REL SIGNED, including the domain-closure sentences of the
  definitions; Corollary REL-SPLIT SIGNED (a REDUCTION: SEG unbounded); the Remark not to sign; quotes 17 in their ranges (own
  scratch/flip_quotes.py, QUOTES 17 FAILED 0, "…" read as a separator), 16/17 strictly verbatim (the (SW) "…"); notes REL-N1..N5; no gap.
  REFEREE-2 docs/referee-2/R2-N5-REL.md (report eb5aa2b5, sha1 b75ae5caa74662f491f2fe80164e77ec16e32e4a there; §C b6811cf1; successor 19):
  Lemma GATE-RISE SIGN (step 3's injectivity used on u-free values only, N-REL-2); its Count SIGN; Theorem STATIC-DEPTH-REL SIGN; Corollary
  REL-SPLIT SIGN (a REDUCTION); the Remark not signed (correct for the length bound and for settling on V^W_b ∪ V^H_b, N-REL-5); quotes
  16/17 verbatim, the (SW) "…" (N-REL-1), SHIFT=1 control 0/17; notes N-REL-1..8; no gap. INDEPENDENCE: REFEREE opened no docs/referee-2/
  file on REL (names matching "N5-REL" at 04:53Z: 0 on its tree, 2 on origin/claude/referee-2, 0 on trunk; names only) and ran no lane code
  (only the data files grun/out/rdr_K10, anc_K10 copied by git show at 07f19760); REFEREE-2 opened no REL file under docs/referee/ before
  pushing eb5aa2b5 (names-only count 0 at 04:40:50Z and at 04:54:13Z) and ran no lane tool; its one declared overlap is REFEREE's SDPRIME
  report, read for its SDPRIME §C, on the W-MONO / Ξ-SUCC point it had found itself first (R2-N5-SDPRIME §1); REFEREE's §C: "No effect on any
  verdict". §C (both): verdicts identical (GATE-RISE, its Count, STATIC-DEPTH-REL, REL-SPLIT); joint gap map EMPTY; REL-N1 ACCEPTED by
  REFEREE-2 ("MISSED by me") and checked against R61 (e)'s landed text; REL-N2 = N-REL-6, REL-N3 = N-REL-4, REL-N5 = N-REL-1 identical;
  REL-N4 ~ N-REL-7 (start sets; no conflict); N-REL-2 ACCEPTED as wording, N-REL-3 = REFEREE's MUT2, N-REL-5 ACCEPTED by REFEREE (the Remark),
  REFEREE-2's cyc and qonly controls ACCEPTED as stronger evidence; nothing open.
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (structural lemmas on N5 inside one phase and a reduction of a run's length to its
  segment count SEG; no running-time bound, no algorithm claim). GAPS G-N5-TIME: open.

### R84 [refereed-only] N5 on EVERY game, inside one phase: for a fixed vertex v, a phase P (λ and τ constant on P, c := λ(v)) and top_t := the highest rank in P_t := P(Ξ_t v), v's path set at state t (⊥, below every rank, if P_t = ∅), a rank being EVEN or ODD as the priority Ω of the vertex of that rank (not the parity of the rank number), at every transition t → t + 1 of P with P_t ≠ P_{t+1} the top rises only to an even rank (if top_{t+1} > top_t then top_{t+1} is even; Lemma TOP-SHAPE (a)) and an even top never falls (if top_t is even then top_{t+1} ≥ top_t; TOP-SHAPE (b)); hence along P, once the top is even it stays even and never falls, and before that it is odd or ⊥, an odd top only falling or staying until it is replaced (by a lower odd rank, by ⊥, or by a lower or higher even rank) (TOP-SHAPE (c)); so the sequence of distinct values of top_t on P is a strictly decreasing run of odd ranks, then at most one ⊥, then a strictly increasing run of even ranks, and top_t changes at most n − 1 times on P, for every vertex v and every phase P (Corollary); the proof reads the strict rise of the signed path-set weight (Ξ non-decreasing by RESULTS R15 (a), (d), the cycle node λ(v) fixed on P, distinct sets of ranks having distinct signed weights) through Fact DELTA (for sets A ≠ B of ranks, weight(B) > weight(A) iff the largest rank d in A Δ B is even and d ∈ B ∖ A, or d is odd and d ∈ A ∖ B) (2026-10-29) — structural lemmas for N5 (they bound the changes of the top only, NOT the P-changes under a fixed top, which are not bounded here; the Δ form of TOP-MONO is DEAD; not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C93.md, checker f6728213)
- Object (L-NEW successor 30, Opus 5.5; frozen, unchanged during review): packet P-N5-TOPSHAPE, docs/new/P-N5-TOPSHAPE-box49.md, sha1
  c5b0e8d86745d6db5e0c9f6e1551b10c5b511b8f (l-new freeze 4c2ea43e, 2026-10-29T04:59:50Z; quote base e2da18b0; 2 quotes,
  experiments/new/box49/quotecheck3.py "quotes=2 bad=0", pinned with the sha1 and a shifted-line control in experiments/new/check.sh; both
  referees measured the pin), Fact DELTA, Lemma TOP-SHAPE (a)-(c) and its Corollary. Tool experiments/new/box49/topmono.py (sha1
  c8f470dfee2aa8cb104078b16d2bd09df553ff99, by git: committed only at 4c2ea43e; the packet's "sha1 in the push message" is not in that
  message); working note docs/new/N5-READER-box49.md §12 (a pointer to the packet). The referees' notes are collected by the lane in
  docs/new/P-N5-TOPSHAPE-fixes-box49.md (l-new 8e8f7238, sha1 be683e9fd1dcd64f48c9d02f2fac66fc214cff0d, L-NEW successor 30: F1-F5 for
  TOP-N1 = N-TS-3, N-TS-1, TOP-N2 with N-TS-2, TOP-N3 = N-TS-5, N-TS-4; 17 quotes checked by script, experiments/new/box49/quotecheck3.py
  "quotes=17 bad=0", pinned in experiments/new/check.sh with a shifted-line control and the sha1); on trunk; "Repairs only; no signed
  statement changes." (fixes l. 6): F1 corrects §3's rise count (DATA in a DEAD item); F2 adds the wider form of (a), (b) and of the
  Corollary as a REMARK outside the signed Lemma (bullet "Referee strengthening"); F3 adds the sharper count as a remark (same bullet); F4
  drops "of one class" from Fact DELTA, states (INJ) as the general fact and keeps RESULTS R38 (a) as the phase definition only; F5 adds to
  §2 that an even or odd rank is the parity of Ω of the vertex of that rank. The statements below are in that repaired wording.
  Setting (every game): N5 = SPEC S1-S5 (docs/new/N5-ssi-global.md) with FIX 1-4; phases as in RESULTS R80's setting (λ := Ξ's cycle-node
  map; a phase is a maximal run of states with λ and τ constant, RESULTS R38 (a) KEY); a transition t → t + 1 of a phase P joins two states
  of P (in-phase S4c fallbacks included). Ξ_t(v): the S1 valuation (c, P, ℓ) of v's honest play; rank(u): the position of u in V sorted by
  (Ω(u), u) (S1); a rank r is EVEN or ODD as Ω of the vertex of rank r (F5: not the parity of the rank number); weight(A) := Σ_{r ∈ A}
  s(r)2^r for a set A of ranks, s(r) = +1 for even r and −1 for odd r (S1's signed weight); S1's order: the reward of c, then the weight of
  P, then ℓ. v: a fixed vertex; c := λ(v), constant on P; P_t := P(Ξ_t v) ⊆ {u : rank(u) > rank(c)}, read as a set of ranks; top_t := the
  largest rank in P_t, or ⊥ (below every rank) if P_t = ∅; for sets A ≠ B, d(A, B) := the largest rank in A Δ B. n: the number of vertices.
- Claims signed (both referees "(Opus 5.5, D15)", L37), on every game; no item uses (P); premises LANDED: SPEC S1 (valuation (c, P, ℓ),
  rank, signed weight, order); RESULTS R15 (a) Lemma A and (d), as (MON): Ξ_{t+1}(v) ⊵ Ξ_t(v) at every N5 iteration, S4c fallbacks included
  (the packet quotes P-N5-HONFF's line "(MON): RESULTS R15 (a) with R15 (d)"); RESULTS R38 (a) KEY and R80's setting, as the phase
  definition only (F4). (INJ) is not a premise: it is the general fact that distinct sets of ranks have distinct signed weights, immediate
  from Fact DELTA (F4); RESULTS R56 (a) states it per honest class and is cited for comparison only.
  (a) Fact DELTA (§1, with F4): for sets A ≠ B of ranks, weight(B) > weight(A) iff d := d(A, B) is even and d ∈ B ∖ A, or d is odd and
      d ∈ A ∖ B. (weight(B) − weight(A) = Σ_{r ∈ B∖A} s(r)2^r − Σ_{r ∈ A∖B} s(r)2^r; the term at d dominates the sum of the others, Σ_{r<d} 2^r <
      2^d; its sign is s(d) if d ∈ B ∖ A and −s(d) if d ∈ A ∖ B.) Hence (INJ): distinct sets of ranks have distinct signed weights. F4:
      "Fact DELTA reads "For sets A ≠ B of ranks, weight(B) > weight(A) iff …"" (the packet's "path sets A ≠ B of one class": REFEREE TOP-N3, "of one class"
      "is not needed. Cosmetic."; REFEREE-2 N-TS-5: "(INJ) is just "distinct sets have distinct weights", which Fact
      DELTA itself proves").
  (b) Lemma TOP-SHAPE (§1): let t → t + 1 be a transition of the phase P with P_t ≠ P_{t+1}. Then (a) if top_{t+1} > top_t, then top_{t+1}
      is even; (b) if top_t is even, then top_{t+1} ≥ top_t; (c) hence, along P: once top is even it stays even and never falls; before
      that, top is odd or ⊥, and an odd top only falls or stays until it is replaced (by a lower odd rank, by ⊥, or by a lower or higher
      even rank). ((MON) gives Ξ_{t+1}(v) ⊵ Ξ_t(v); the cycle node c is the same at both states (λ constant on P), so the order compares the
      weights next: weight(P_{t+1}) ≥ weight(P_t), strictly since P_{t+1} ≠ P_t (INJ). (a): u′ := top_{t+1} > top_t is not in P_t and no
      rank above u′ is in either set, so d(P_t, P_{t+1}) = u′ ∈ P_{t+1} ∖ P_t, and DELTA with the strict rise forces u′ even; from ⊥ too.
      (b): an even u := top_t with top_{t+1} < u (⊥ included) gives d = u ∈ P_t ∖ P_{t+1}, and DELTA says the weight falls, a contradiction.
      (c): from an even top the next top is ≥ it and any rise is even, so tops stay even, non-decreasing, and P never empties again; from ⊥
      a change makes the top > ⊥, hence even; from an odd top a rise is even, otherwise the top stays or falls.)
  (c) Corollary (top changes, §1): for every vertex v and phase P, top_t changes at most n − 1 times on P. (By TOP-SHAPE (c) the sequence of
      distinct top values is a strictly decreasing run of odd ranks, then possibly ⊥, then a strictly increasing run of even ranks; the odd
      run has no ⊥ inside it, since from ⊥ the next top is even; so each rank above rank(c) occurs at most once and ⊥ at most once; there
      are at most n − 1 ranks above rank(c), so at most n values and at most n − 1 changes. A top changes only at a P-change, which the
      Lemma covers: REFEREE §1.)
- Not signed: the packet's §2 (DATA) and §3 (TOP-MONO in its Δ form, DEAD; bullet "Honest limits" (iii)), as the packet says. The
  packet's reader-proofness sentence (READING: "readers ... cannot raise a vertex's top changes above n − 1. What they raise is the
  P-changes under a fixed top"): REFEREE "not signed; true as a consequence of the Corollary"; REFEREE-2 "not signed. Follows from the
  Corollary being per vertex and on every game". The packet's wording as frozen, repaired by the fixes and not false where a statement:
  Fact DELTA "For path sets A ≠ B of one class" (F4; the proof never uses the class); the premise line "(INJ) (RESULTS R56 (a))", where R56
  (a) states it per honest class (F4); "Phases (RESULTS R38 (a))" as a premise beyond the phase definition (F4, REFEREE-2 N-TS-5: "R38 (a)
  is not needed beyond the phase definition"); §3's "with 20 rises in the phase" (F1: 17 for vertex 0; 20 is vertex 6's, the run's
  maximum: "vertex 0 has 35 P-changes and 17 rises; vertex 6 has 44 P-changes and 20 rises"); §2's "tops 31, 30, 29, 27, 26, 21, 20 (all
  odd ranks)" without the reminder that the parity is Ω's (F5, N-TS-4: it "reads as a contradiction without that definition at hand").
- Referee strengthening (NOT part of this entry; fixes F2 and F3 record both as remarks outside the signed Lemma and Corollary):
  (i) N-TS-1, the wider form: TOP-SHAPE (a) and (b) hold at every N5 transition at which λ(v) is unchanged, phase-leaving transitions
  included, and the Corollary holds per maximal run of states with λ(v) constant (which can be longer than a phase). REFEREE-2 states it
  in its verdict line ("It also holds at every N5 transition at which v's own cycle node is unchanged, phase or not (N-TS-1)") and checks
  it as XSAMEC, 0 failures in 115,702 checks; REFEREE's §C: "N-TS-1 SETTLED (Lead's question): a STRENGTHENING, not part of the signed
  statement. The packet's Lemma and Corollary are stated for transitions and runs inside one phase, and that is what both referees sign";
  it re-derives the wider form ("the proof uses only (MON), valid at every iteration since Ξ depends on σ alone, R15 (a), (d); the
  unchanged cycle node; and (INJ)") and checks it, 0 failures at 9,202 off-phase P-changes with λ(v) unchanged (scratch/ts_wide.py;
  top_logs/wide_lib41.txt 2,091, wide_lib1140.txt 7,111). REFEREE-2's CTL_cross shows the unchanged cycle node is needed: TSa / TSb fail
  17,907 + 50,151 + 666 + 40,331 + 28,705 times across phase-leaving transitions. The lane did not state it as a signed item (F2: "as a
  REMARK (not part of the signed Lemma)"). (ii) N-TS-2, the sharper count (F3, remark): top changes ≤ n − 1 − rank(λ(v)), ranks counted
  from 0 (F3), since the values are the ranks above rank(λ(v)) and ⊥. In REFEREE-2's Corollary verdict line as an addition ("SIGN. The same
  proof gives ≤ n − 1 − rank(λ(v)) (N-TS-2)"; CORc, 0 failures), not in REFEREE's verdict table; REFEREE's §C: "ACCEPTED, consistent".
- Honest limits: (i) TOP-SHAPE bounds only the changes of the top. The P-changes under a fixed top (the counting changes) are not bounded:
  P-changes of one vertex in one phase reach 71 (l121reader_n41, n 41; packet §2, reproduced by REFEREE) and 72 (l121_d29) and 67
  (nep92_n40) in REFEREE-2's data, which has P-changes per (v, phase) above n − 1 in 23 + 3 + 32 cases (CTL_counting). READING (Lead): a
  path set under a fixed top behaves like a binary counter below it (packet §3's obstruction), and L-RED's R104 (docs/red/R104-counting-gate.md,
  l-red 92754453; L-RED DATA, not refereed) counts low-digit resets under a fixed top (changes of an Odd choice vertex's path set that
  remove an element while its top is unchanged) as abundant: RESET 133 of PCH 157 (PCH: path-set changes summed over all Odd choice vertices, gate by gate, gatep.py l. 30-36) in one
  phase of pl130_n40 (own start). So the Corollary does not bound the P-changes of a vertex, nor Ξ-changes, nor a phase's length. (ii) Whether
  n − 1 is attained is OPEN (REFEREE TOP-N2: "Whether n − 1 is attained by some game is open (an odd run down all odd ranks, then the even
  ranks upward)"; REFEREE-2 §C: "stays OPEN"). In data the count stays far below it: max 0.37 n (REFEREE; 48 at n = 156) and 0.43·(n − 1)
  (REFEREE-2, lend9_n8; 62 at n = 581, gate_K64_n581, vertex 573); REFEREE's MUT2 (the Corollary with n − 2) does not bite. (iii) DEAD:
  TOP-MONO in its Δ form (Lead, 04:57Z: "the top rank of the symmetric difference between successive path sets P(Ξ_t(v)) at its P-changes
  is monotone") is false: experiments/new/box48/instances/long121_n40 at its .start, phase [1, 122], vertex 0, Δ-tops at its P-changes
  35, 37, 32, 33, 26, 39, 21, 29, 33, 36, … (35 P-changes, 17 rises of the Δ-top, F1; 20 rises for vertex 6, the run's maximum; 47 Δ-top
  rises for one vertex in one phase on ladderd0_k48_n156, packet §3 and REFEREE). Obstruction (packet §3): "the Δ-top is the carry position
  of a counter ... a counter's carry positions go up and down. Only the top of P itself is monotone in the sense of (c)." Confirmed by both
  referees on the same instance with the same first ten Δ-tops; REFEREE MUT3 (Δ-tops non-increasing demanded) bites at 7,305 (vertex,
  phase) pairs (lib41), REFEREE-2 CTL_deltatop fails in 4,360 of 6,124 sequences with ≥ 2 P-changes (alt_all). (iv) Nothing here bounds
  N5's running time.
- Data (DATA, not proof): the packet's §2 (lane, experiments/new/box49/topmono.py; outputs experiments/new/box49/out/topmono_*.txt; VIOL
  counters rise-to-odd / even-top-fell / odd-after-even 0 / 0 / 0 everywhere): lib41 (n ≤ 48, own start or S3 + 2 random, seed 7) 1,047
  runs, 59,663 P-changes, max top rises per (v, P) 3 (b5_os_n28, vertex 10: tops 10, 11, 22, 27); L-RED instances (n ≤ 200, own start or
  S3) 311 runs, 27,587, max 48 (ladderd0_k48_n156, vertex 50: ⊥, 107, 108, …); long121, qpcclimb scale, pl130_n40, si/root/instances 13
  runs, 11,177, max 2 (cone_n69: ⊥, 67, 68); 1,371 runs in all; gate example sc32 (box25), vertex 0, phase [4, 48]: tops 31, 30, 29, 27,
  26, 21, 20 (odd in Ω's sense, F5), ⊥, 25, 28. REFEREE (successor 17; own docs/referee/scratch/topshape_probe.py (sha1 b9c0d284…) on its
  engine rl_engine; lane code not run; logs scratch/top_logs/; 0 failures in every MUT=0 run): lib1140 (n ≤ 40; given + S3 + 1 random)
  1,857 runs, 56,473 P-changes, 17,882 (v, P) pairs, (a) / (b) checks 5,572 / 6,858, max top changes 9 (0.37 n), max P-changes per (v, P)
  60; lib41 (n ≤ 48; given + S3 + 2 random) 1,076, 58,143, 15,873, 3,612 / 4,694, 10 (0.28), 37; L-RED instances (316 games, n ≤ 200)
  316, 29,196, 8,083, 2,756 / 5,248, 48 (0.30), 62; random rand_ck (n 6-24, k ≤ 6) 12,000, 3,286, 3,224, 1,209 / 625, 2 (0.22), 2;
  long121_n40 1, 769, 39, 9 / 54, 7, 44; DELTA's iff, the strict rise, the unchanged cycle node, (a), (b), (c) and per (v, P) the shape and
  the bound: 0 failures on 147,867 P-changes and 45,101 (v, P) pairs; MUT1 ((a) with odd) bites at 3,612 of 3,612 rises, MUT2 (n − 2) does
  not bite, MUT3 (Δ form) 7,305 pairs; reproduced: ladderd0_k48_n156 48 top changes, l121reader_n41 71 P-changes, §3's ten Δ-tops (distinct
  tops of long121 vertex 0: 39, 38, 37, 36, 35, 26, 14). REFEREE-2 (successor 19; own docs/referee-2/R2-N5-TOPSHAPE/topshape_check.py and
  repro.py on its lane's SPEC loop (si.py, read-only); lane tools not run; every run 0 violations): alt_all (413 runs, given start else S3)
  458 phases, 53,549 P-changes, TSa / TSb 6,082 / 10,282, 8,516 (v, phase) with a top change, 3,643 odd-then-even sequences; lib41_noref × 3
  (1,230 runs) 1,116, 72,783, 6,986 / 13,914, 14,277, 5,429; named (20 runs) 24, 12,716, 426 / 1,103, 779, 505; random kO n 8-20 / k2 n 6-16
  (30,000 runs) 4,880, 4,021, 1,465 / 1,212, 2,386, 599; Fact DELTA also on 8,236 + 24,488 + 400 + 299,807 + 299,144 random mask pairs; TSc
  and COR / CORc on every (v, phase); reproduced: sc32's tops exactly as §2, ladderd0_k48_n156's 48 top changes, the l121reader-type
  P-change counts (72 / 67); controls CTL_flip (bites at every rise), CTL_deltatop, CTL_cross, CTL_counting as above. Run counts differ by
  start set and corpus (lane lib41 1,047 runs, REFEREE 1,076, REFEREE-2 1,230; L-RED instances 311 runs (lane) and 316 games (REFEREE));
  not reconciled in any report. No signed statement uses any count.
- Signatures: REFEREE docs/referee/R-N5-TOPSHAPE.md (report 1a6d6a24, sha1 8e4afe5a87b5e8e96bf7fb19b3d63f27ed3fe830 there; §C e0499401;
  successor 17): Fact DELTA SIGNED; Lemma TOP-SHAPE (a)-(c) SIGNED; Corollary SIGNED; the reader-proofness sentence not signed (true as a
  consequence); §2, §3 not signed, §3's instance reproduced (DEAD); quotes 2 of 2 verbatim (own scratch/flip_quotes.py); notes TOP-N1..N3;
  no gap. REFEREE-2 docs/referee-2/R2-N5-TOPSHAPE.md (report 97db54fc, sha1 e409e4439a18c368f452ed9a1c5de0ac1eefbb50 there; §C 0e2063bf;
  successor 19): Fact DELTA SIGN; Lemma TOP-SHAPE (a), (b), (c) SIGN; Corollary SIGN; reader-proofness not signed; §3 DEAD CONFIRMED; quotes
  2/2 verbatim (own qcheck.py; SHIFT=1 control 0/2); notes N-TS-1..5; no gap. INDEPENDENCE: REFEREE opened no docs/referee-2/ file on
  TOPSHAPE (names at 05:13Z: 0 on its tree, 0 on origin/claude/referee-2, 0 on trunk) and ran no lane code; REFEREE-2 opened no TOPSHAPE
  file under docs/referee/ before pushing 97db54fc (names-only count 0 at 05:06:23Z and at 05:18:26Z; it opened REFEREE's REL report, not a
  TOPSHAPE file, on the Lead's word) and ran no lane tool. §C (both): verdicts identical (Fact DELTA, TOP-SHAPE (a)-(c), the Corollary;
  Δ-form TOP-MONO DEAD on the same instance); joint gap map EMPTY; TOP-N1 = N-TS-3 (same numbers, found independently), TOP-N3 = N-TS-5,
  TOP-N2 with N-TS-2 ACCEPTED, N-TS-4 ACCEPTED as wording, N-TS-1 SETTLED as a strengthening (bullet "Referee strengthening"); REFEREE-2:
  "No verdict changes"; REFEREE: "Nothing open on TOPSHAPE."
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (structural lemmas on N5 inside one phase bounding the changes of the top of a
  vertex's path set; no running-time bound, no algorithm claim). GAPS G-N5-TIME: open.

### R85 [refereed-only] N5 on EVERY game: (A) for a vertex v, a phase 𝒫 (λ and τ constant on 𝒫, c := λ(v)), v's path sets P_t := P(Ξ_t v) ⊆ R_c := the K ranks above rank(c) (K ≤ n − 1, r_1 < … < r_K), pos(r_k) := k, w(r) := +pos(r) if r is even and −pos(r) if r is odd (a rank's parity is Ω's of its vertex), Φ(A) := Σ_{r ∈ A} w(r), and a P-change A → B (a transition of 𝒫 with P_t ≠ P_{t+1}) MATCHED if some matching M ⊆ (A ∖ B) × (B ∖ A) has w(i) > w(o) on every pair (o, i) and leaves only even incoming and odd outgoing ranks uncovered, a CARRY otherwise: for distinct ranks o, i, w(i) > w(o) iff weight({i}) > weight({o}), and adding an even rank or removing an odd rank raises the weight (Fact A1); Φ(B) − Φ(A) ≥ 1 at every MATCHED P-change (Lemma MATCH-Φ); hence PCH_𝒫(v) ≤ (K(K+1)/2)(NM_𝒫(v) + 1) + NM_𝒫(v) per vertex per phase, every game, PCH and NM counting v's P-changes and carries in 𝒫 (Corollary, added statement (A)); (B) at a state with τ(e) = h at an Odd vertex e, for a successor d ≠ h of e, a route π = (π_1 = d, …, π_m) of distinct Even vertices of G into e, Q := {π_1, …, π_m, e}, ρ the (τ̄, τ)-play from h and c_h the cycle node of Ξτ(h): (H1) every vertex of Q ranks above c_h, (H2) ρ (prefix and cycle) contains no vertex of Q and (H3) Q's vertex of largest rank has even Ω imply (e, d) ∉ Iτ (Lemma GATE-SHUT; via Fact B1: on valuations with the same cycle node and P ≠ P′, G^d's order reverses G's, and Fact B2: (VJ) of RESULTS R57 (a) on G^d), so on a stretch of states of one run with τ(e) = h and (H1)-(H3) at every state, (e, d) ∉ Iτ at each of them and τ never moves from h to d at a transition from one of them (added statement (B); the claim at t → t + 1 uses (H1)-(H3) at t only, π may differ from state to state, the Lemma uses no phase) (2026-10-29) — a REDUCTION of one vertex's path-set changes in one phase to its carries NM, and a structural lemma on Odd's improving edges that bounds no count (NM is OPEN, not bounded here; persistence of (H1)-(H3) not claimed; (H2)'s necessity not exhibited; not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C94.md, checker 7e309075)
- Object (L-LIT successor, Opus 5.5, D18, Lead reading L40; frozen, unchanged during review): packet P-N5-MPGS, docs/lit/P-N5-MPGS.md,
  sha1 24913a7f9efea437aa202b398113b7ce12890961, 246 lines (l-lit freeze a23179b01be61d7f85e37aa93c0ae55a2dde7de8,
  2026-10-29T11:03:06Z; quote base 1f15c91b; 9 quotes, docs/lit/P-N5-MPGS-quotecheck.py, sha1 74dbe8b4e6c4f37d4fdf7ca587eb479b5434579f,
  "quotes=9 bad=0"; all three referee reports measured the packet sha1 and the pins), Part (A) (A0 definitions, Fact A1, Lemma MATCH-Φ,
  added statement (A)) and Part (B) (B0 definitions, Fact B1, Fact B2, Lemma GATE-SHUT, added statement (B)). Superseded copies, not
  routed: P-N5-MATCHPHI (l-lit 12b7d12a, sha1 544705b74312e49ee31fd93ede1952396ebd12f1; Part (A)'s statements, reviewed before the
  supersession: REFEREE R-N5-MATCHPHI.md, REFEREE-2 R2-N5-MATCHPHI.md) and P-N5-GATESHUT (l-lit 1298d8b2, sha1
  affcae678b12bd8fc4ebc7a9b5759ee7b2442f39; no review). The fixes file's F1 ("WITHDRAWN") is withdrawn by F2 ("Lead ruling 11:27Z: F1
  withdrawn; P-N5-MPGS is the review object."). The referees' notes are collected by the lane in docs/lit/P-N5-MPGS-fixes.md (l-lit 510c47eb, sha1 57015bb6bb1c9597f506613083b2389a948c05c6, L-LIT successor 2: F3-F11 answer MPGS-N1..N5, MATCH-N1..N4, N-MPGS-1..6,
  N-GS-1..5, N-MP-1..5, C.4 items 1-6 and J1-J15; 50 quotes checked by docs/lit/P-N5-MPGS-fixes-quotecheck.py, sha1
  dc3f8c0b1b447324183061385e4e3eb643e4f98c, "quotes=50 bad=0"); on trunk; "No statement of P-N5-MPGS changes; no item is FALSE" (fixes,
  Coverage). F3 appends the rise/fall summation to the proof of (A) and writes W as an equality; F4 appends to step 3 of GATE-SHUT's
  proof that h ∉ Q and that d = π_1 is Even; F5 adds two DATA notes to B3 (T34's (H1) test, T34's imports); F6 corrects B3's "The
  hypotheses are needed"; F7 corrects B4's "(H1) automatic"; F8 adds three optional one-liners (full order reversal; per-state reading
  of (B); (A) on λ-runs); F9 carries MATCHPHI's notes (sharpness at NM = 0 and the additivity line, both PROVED by L-LIT, unrefereed);
  F10 records notes needing no packet change; F11 records the Lead's ruling of 12:29Z (REFEREE-2's E-class items required, done as F3-F7; J6-J8 carried into the entry); no statement change. The statements below are in the frozen wording with those repairs.
  Setting (every game): N5 = SPEC S1-S5 (docs/new/N5-ssi-global.md) with FIX 1-4; a phase is a maximal run of states with λ (Ξ's
  cycle-node map) and τ constant (RESULTS R38 (a), as in R84). Part (A): v a vertex, c := λ(v), constant on 𝒫; P_t := P(Ξ_t v), read
  as a set of ranks; R_c := {rank(u) : rank(u) > rank(c)} ⊇ P_t (by S1-rank, p'(u) > p'(c) iff rank(u) > rank(c)); K := |R_c| ≤ n − 1;
  a rank is even or odd as Ω of its vertex (R84 F5); weight(A) := Σ_{r ∈ A} s(r)2^r (R84 (a)); a P-change of v in 𝒫 is a transition
  t → t + 1 of 𝒫 (in-phase S4c fallbacks included) with P_t ≠ P_{t+1}, PCH_𝒫(v) their number; MATCHED: a matching M ⊆ (A ∖ B) × (B ∖ A)
  with (M1) "w(i) > w(o) for every (o, i) ∈ M", (M2) "every i ∈ B ∖ A not covered by M is even", (M3) "every o ∈ A ∖ B not covered by M
  is odd"; CARRY: a P-change that is not MATCHED; NM_𝒫(v) the number of carries of v in 𝒫. Part (B), at a state t of an N5 run (σ :=
  σ_t, τ := τ_t): G^d the dual game (owner swapped, Ω + 1); Ξτ S1's valuation of τ on G^d; τ̄ S1's optimal counterstrategy on G^d to
  τ, an Even strategy of G; ⊴ S1's order on G, ⊴_d S1's order on G^d (better for Odd of G); (e, w) ∈ Iτ iff e is Odd, w ≠ τ(e) and
  Ξτ(w) ▷_d Ξτ(τ(e)) (S2); π(x; σ′, τ) the play from x under (σ′, τ), a lasso, and V^d_{τ,σ′}(x) S1's valuation of it on G^d; the
  gate e, h := τ(e), d ≠ h, π, Q, ρ := π(h; τ̄, τ), c_h as in the title; (H1) "rank(u) > rank(c_h) for every u ∈ Q", (H2) "ρ, prefix and
  cycle, contains no vertex of Q", (H3) "the vertex of largest rank in Q has even Ω (in G)".
- Claims signed (both referees "(Opus 5.5, D15)", L37: REFEREE successor 17; REFEREE-2 successor 19, report of record); on every game;
  no item uses (P); premises LANDED: SPEC S1 (rank, valuation (c, P, ℓ), order, Odd's side on G^d), the SPEC ambiguity row A3 (G^d has
  G's ranks), S2, S4b, S4c (quote base 1f15c91b); RESULTS R57 (a) (VJ); RESULTS R84 (a) Fact DELTA; RESULTS R38 (a), as the phase
  definition only. Part (A) uses neither (MON) nor R84's TOP-SHAPE (packet A2: "Fact A1 also uses [DELTA]. It does not use (MON) or
  R84's TOP-SHAPE"; this repairs MATCH-N1 = N-MP-1, J11 "closed"). Standing premise, as in RESULTS R57 (b) (J6, REFEREE §C: "the RESULTS
  entry should carry the clause as R57 (b) does"): Ξτ(x) = V^d_{τ,τ̄}(x) is S1-val's definition (B0: "by definition"); that S1's
  procedure outputs it is SPEC conformance, the premise R57 (b) records ("that S1's procedure realises an optimal σ̄ is VJ00 §6 plus SPEC
  conformance"); the code's match to SPEC is DATA (REFEREE-2 19 DENG, REFEREE-2 20 ENGXI, 0 differences).
  (a) Fact A1 (A2): "For distinct ranks o, i: w(i) > w(o) iff weight({i}) > weight({o}). Adding an even rank or removing an odd rank
      raises the weight." ([DELTA] with d = max(o, i): for i > o the exchange raises the weight iff i is even, and then w(i) = pos(i) >
      pos(o) ≥ w(o), else w(i) = −pos(i) < −pos(o) ≤ w(o); for o > i iff o is odd, and then w(o) = −pos(o) < −pos(i) ≤ w(i), else w(o) =
      pos(o) > pos(i) ≥ w(i); additions and removals: [DELTA] with d the added or removed rank.)
  (b) Lemma MATCH-Φ (A2): "At every MATCHED P-change A → B, Φ(B) − Φ(A) ≥ 1." (Φ(B) − Φ(A) = Σ_{(o,i) ∈ M}(w(i) − w(o)) +
      Σ_{uncovered i ∈ B∖A} pos(i) + Σ_{uncovered o ∈ A∖B} pos(o); every term is an integer ≥ 1 by (M1), (M2), (M3), and some term exists
      since A ≠ B.)
  (c) Added statement (A), Corollary (A2): "PCH_𝒫(v) ≤ (K(K+1)/2)(NM_𝒫(v) + 1) + NM_𝒫(v) per vertex per phase, every game"; in the
      packet's words "For every game, vertex v and phase 𝒫: PCH_𝒫(v) ≤ (K(K+1)/2)·(NM_𝒫(v) + 1) + NM_𝒫(v)." (Proof with F3: W := max Φ −
      min Φ over subsets of R_c = Σ_{k=1}^{K} k = K(K+1)/2, an equality; Φ_t := Φ(P_t) changes only at P-changes; with R the sum of the
      positive and F of the absolute negative increments, R − F = Φ_end − Φ_start ≤ W; every MATCHED change adds ≥ 1 to R (Lemma
      MATCH-Φ), so #MATCHED ≤ R; negative increments occur only at carries, each ≤ W, so F ≤ W·NM_𝒫(v); so #MATCHED ≤ W + W·NM_𝒫(v) and
      PCH_𝒫(v) = #MATCHED + NM_𝒫(v). REFEREE MPGS-N1 = J4: "the inference is valid as a sketch"; REFEREE-2 §C D1: "Restore MATCHPHI's three
      lines". K ≤ n − 1 gives K(K+1)/2 ≤ n²/2 (A0; REFEREE-2 19 §1).)
  (d) Fact B1 (B1): "For valuations X = (c, P, ℓ) and X′ = (c, P′, ℓ′) with the same cycle node c and P ≠ P′: X ◁_d X′ iff X′ ◁ X."
      (By [A3] G^d has G's ranks, so P and the cycle node (the vertex of maximal rank on the cycle) are the same in both readings; G^d's
      signed weight of P is −weight(P); with equal cycle nodes and P ≠ P′ both orders decide on the weights; ℓ is never reached.)
  (e) Fact B2 (B1): "For every positional Even strategy σ′ of G and every x: Ξτ(x) ⊴_d V^d_{τ,σ′}(x)." ([VJ] holds "on every game",
      hence on G^d, whose "Even" strategy is τ and whose "Odd" strategies are G's Even strategies; instantiate with σ := τ, τ′ := σ′.)
  (f) Lemma GATE-SHUT (B2): "At a state t with τ(e) = h, (H1), (H2) and (H3) imply (e, d) ∉ Iτ." (1: σ′ := τ̄ except σ′(π_k) := π_{k+1}
      (k < m), σ′(π_m) := e, a positional Even strategy of G differing from τ̄ only on π. 2 ((H2)): π(h; σ′, τ) = ρ. 3: π(d; σ′, τ) is π_1,
      …, π_m, e, then ρ, with F4: "Here h ∉ Q, because ρ starts at h and (H2) says ρ contains no vertex of Q; so the play, after π·e,
      enters ρ at its first vertex h and then follows step 2. And d = π_1 is an Even vertex of G (π consists of Even vertices, B0), so
      σ′(d) = π_2 (or e if m = 1) is set by step 1."; its cycle node is c_h and by (H1) its set is P(ρ) ∪ Q, Q ∩ P(ρ) = ∅ by (H2): V :=
      V^d_{τ,σ′}(d) = (c_h, P(ρ) ∪ Q, ℓ(ρ) + |Q|). 4 ((H3)): the top rank of Q is even and in the larger set, so [DELTA] gives
      weight(P(ρ) ∪ Q) > weight(P(ρ)), Ξτ(h) ◁ V, and V ◁_d Ξτ(h) by Fact B1. 5 ((VJ)): Fact B2 at x = d: Ξτ(d) ⊴_d V. 6: Ξτ(d) ⊴_d V
      ◁_d Ξτ(h) = Ξτ(τ(e)), so (e, d) ∉ Iτ by [S2].)
  (g) Added statement (B), Corollary (B2): "(H1)-(H3) at every state of a stretch on which τ(e) = h ⇒ (e, d) ∉ Iτ at every state of it,
      and τ never moves from h to d at a transition from it"; in the packet's words "Let [t_0, t_1] be a stretch of states of one run with
      τ_t(e) = h and (H1)-(H3) at every t ∈ [t_0, t_1]. Then (e, d) ∉ Iτ_t for every such t, and τ_{t+1}(e) ≠ d for every t ∈ [t_0, t_1]."
      (The first claim is the Lemma at each t; S4b: τ_{t+1}(e) ∈ A(e) = {τ_t(e)} ∪ {w : (e, w) ∈ Iτ_t}; S4c's Odd fallback moves e only to
      an Iτ_t-target; S4a and an Even fallback (FIX 3) leave τ.) Scope, as both referees read it (J8; fixes F8 (b)): the claim at t → t + 1
      uses (H1)-(H3) at t only and π may differ per state (REFEREE §C J8: "the Corollary (B) uses only the hypotheses at the transition's
      source state; π may differ per state"; REFEREE §2: "the first claim is the Lemma per state"); REFEREE-2 19 N-MPGS-6: "The Lemma holds
      at any state of any N5 run, in-phase or not (it uses no phase). The added statement (B) is per transition. Both are stated that way;
      nothing to repair." (Also REFEREE-2 20 N-GS-4, concurring.) B0, A0: REFEREE "CHECKED", REFEREE-2 19 "SIGNED (well formed)"; REFEREE's
      §C: "same content".
- Not signed: A3, B3 (DATA) and A4, B4 (READING), as the packet says, with their corrections: B3's last bullet "The hypotheses are needed:
  the unhypothesised form is false on these instances." is true of the three together, of (H1) alone and of (H3) alone, and NOT exhibited
  for (H2) alone (F6; REFEREE MPGS-N3, REFEREE-2 19 N-MPGS-1, REFEREE-2 20 N-GS-3; bullet "Honest limits" (iii)); B4's first bullet "(H1)
  is automatic" holds only at states where c_h is the sink (F7; REFEREE-2 19 N-MPGS-4: "consistent with my H_n data only where c_h is the
  sink"; REFEREE J9; "These are the reopenings §B3 describes"); B3's T34 tests (H1) only as rank(c_h) < rank(d1_i), exact on H_n (hn.py
  l. 46-49: d1_i < d2_i < d3_i < e_i) and not a test of (H1) on other games (F5; MPGS-N4 = J2, N-MPGS-2, N-GS-5). The to-sign table's
  line for Fact A1, "MATCHED = decomposes into individually weight-raising one-rank moves", is not the signed Fact A1 (REFEREE §1: Fact A1
  "drops MATCHPHI's last sentence", "which the to-sign table still carries"; REFEREE-2 20: "N-MP-3 (additivity, one line) still applies to
  the table's wording"); it needs the additivity line (bullet "Referee strengthening" (iii)). The packet's A4 CONJECTURE NM = O(n) per
  vertex per phase (READING, OPEN) and B4's CONJECTURE NO-HIDE (not part of the packet). CONJECTURE H2-FREE (F6: at a state with τ(e) = h,
  (H1) and (H3) imply (e, d) ∉ Iτ): OPEN, "not claimed, not signed" (F6); REFEREE J1 "whether (H1) + (H3) suffice is OPEN", REFEREE-2 20
  N-GS-3 "NOT claimed by the packet and NOT signed here" (its partial argument is incomplete: "which I have not completed"). F9 (a) and
  F9 (b) are PROVED by L-LIT, unrefereed, and are not signed (bullet "Referee strengthening" (ii), (iii)).
- Referee strengthening (NOT part of this entry; REFEREE-2 20 is cited as "REFEREE-2 concurring" (Lead ruling 11:54Z, s20 status line),
  never as a third signature):
  (0) The λ-run form of (A) (fixes F8 (c), a remark): (A) and its proof hold
      verbatim with 𝒫 replaced by any stretch of consecutive states of one run on which λ(v) is constant (a λ-run with τ free, fallbacks
      included), PCH and NM counted over that stretch (fixes F8 (c)). REFEREE §1b: "YES (Opus 5.5, D15), verbatim, on ANY sequence of
      consecutive states (phase, λ-run with τ free, or any stretch, fallbacks included) on which v's own cycle node c = λ(v) is
      constant", "No step reads τ, the phase, (MON) or the direction of the weight change. (Even only λ(v) for the single vertex v is
      needed, not all of λ_Ξ.)". REFEREE-2 §C (e1ec568a): "REFEREE-2 20 reached the same conclusion independently in R2-N5-COMPOSE §2.5
      (pushed 4b8afa95 before §1b was read), and added that the Odd side reads parities on G^d (N-C3)", "Joint: AGREED. This is the premise
      P-N5-COMPOSE §6 needs." (R2-N5-COMPOSE §2.5: "So "phase → λ-run" is not merely a reading: it is the same proof verbatim. ✓")
      REFEREE §C (8da7b717): "REFEREE-2 did not address this question (it was asked of the first referee); nothing in either REFEREE-2
      report contradicts it (N-MPGS-6: the Lemma uses no phase)."; it does not cite REFEREE-2's §C, pushed 21 s before it.
      Status (CHECKER C94 E-1): REFEREE §1b is a labelled verdict outside its verdict table; REFEREE-2: not in the report of record;
      its §C (successor 20) "Joint: AGREED", classed "opt" (C.4 item 6), with its proof in R2-N5-COMPOSE §2.5. To be signed with
      P-N5-COMPOSE, which uses it.
  (i) J7, the full order reversal (fixes F8 (a), a remark after Fact B1): "For ALL valuations X ≠ X′, X ◁_d X′ iff X′ ◁ X. GATE-SHUT uses
  only the case of Fact B1." REFEREE-2 concurring N-GS-2: "G^d's order is the exact reverse of G's on ALL valuations, not only on equal
  cycle nodes with P ≠ P′", "the Lemma needs only the packet's B1" (b1_general.txt, 200,000 random valuation pairs, 0 violations);
  REFEREE §C J7: "I re-derived it: Ω(c) even, p′ = 2r → p′_d = 2r + 1, reward −(2r + 1); Ω(c) odd, −(2r + 1) → 2r; both = −reward − 1.
  Correct"; not raised by REFEREE-2 19 (REFEREE-2 §C D7: "Not raised by the others"). (ii) J12, sharpness at NM = 0: as a statement about
  subset sequences of R_c the bound is attained with NM = 0 (PCH = W = K(K+1)/2). In REFEREE-2 19's verdict line for (A) as an addition
  ("SIGNED. The first term is SHARP at NM = 0 (N-MP-2)"; R2-N5-MATCHPHI N-MP-2: "all-odd parities, K ≤ 7, exhaustive"); REFEREE
  R-N5-MATCHPHI MATCH-N4: "attained by abstract all-matched chains (§3); the bound is sharp as a statement about subset sequences. Its N5
  tightness is open." (its §3: "for all-even ranks and K = 1..8"); REFEREE §C: "may carry J7, J8, J12 as referees' remarks". F9 (a) gives
  an explicit all-odd construction, PROVED (L-LIT, unrefereed). Whether N5 attains it is OPEN. (iii) J13, additivity (F9 (b), PROVED by
  L-LIT, unrefereed): weight(S ∖ {o} ∪ {i}) − weight(S) = weight({i}) − weight({o}), so a MATCHED change raises the weight of the current
  set (weight(B) > weight(A)); in the superseded reviews REFEREE-2 19 (F1add, F1b: "Hence a MATCHED change always raises the weight (F1b:
  0 failures on all 2,374,900 ordered pairs, K ≤ 7)") and REFEREE ("immediate from additivity of the weight": MATCH-N2). READING (F9 (b),
  not signed): in a phase, where every P-change raises the weight (R84), the carries are exactly the weight-raising P-changes that do
  not decompose so. (iv) J1, (H1) alone gives e ∉ ρ (F6, PROVED by L-LIT, unrefereed as an item): REFEREE J1: "I checked the e ∉ ρ step:
  correct"; REFEREE-2 concurring §2.4: "(H1) already excludes e ∈ ρ"; so (H2) adds only "ρ avoids π_1, …, π_m". (v) REFEREE-2
  concurring N-C3 (R2-N5-COMPOSE, quoted in REFEREE-2 §C): on the Odd side (G^d), MATCHED, w and NM^U are read with G^d's parities.
- Honest limits: (i) MATCH-Φ and (A) are a REDUCTION of the path-set changes of one vertex in one phase to its carries NM. NM is OPEN and
  not bounded here (packet: "It does not bound the carries; NM is OPEN"; REFEREE-2 19: "(A) is a REDUCTION to NM (OPEN)"). DATA only, not
  refereed: carries of one vertex in one phase reach NM = 2n² + 5n − 5 on L-RED's R109 topfix family (claude/l-red e5c9b628,
  docs/red/R109-hn-topgate.md §5, phases keyed by (λ_Ξ, τ); n is Friedmann's index, N = 21n vertices: max NM 343 = 1.361 N at n 12, N 252;
  "Carries of ONE vertex in ONE phase are Θ(N²) on this family"). Lead reading: these DATA are against the packet's A4 CONJECTURE "NM = O(n)
  per vertex per phase" (READING, OPEN, not signed) on that family. T33 Part B (DATA): under abstract monotone set sequences with a fixed
  top NM can be exponential (k = 8: 255 P-changes, NM 63); these are not N5 runs. (ii) (B) bounds no count and does not claim that (H1)-(H3)
  persist (packet "What is not claimed": "a cycle node above the gate can appear"; REFEREE-2 19: "8,829 h → d moves of τ at gates where some
  hypothesis fails (CTL_flip_nohyp)"). On L-RED's R109 family (H1) fails at the τ-gates (DATA, R109 FINDINGS 2: "τ-gates never shut, because
  (H1) fails"). (iii) (H2)'s necessity is not exhibited, in all three data sets: REFEREE MUT 2 (8,975 relaxed hits, all still shut);
  REFEREE-2 19 noH2 0 of 15,528; REFEREE-2 20 X2 0 of 1,648 (426 under every τ of their game). (H1) and (H3) each bite alone (REFEREE MUT 3:
  Lemma 576, Corollary 66; MUT 1: Lemma 240, Corollary 89; REFEREE-2 19 noH1 5,673, noH3 4,422; REFEREE-2 20 X1, X3 > 0). Whether (H1) +
  (H3) suffice is OPEN (CONJECTURE H2-FREE). (iv) The referees' gate enumerations are capped (REFEREE DFS budget 4,000 nodes; REFEREE-2 19 π
  ≤ 6 vertices, ≤ 40 per (e, d); REFEREE-2 20 ≤ 64 per (state, e, d)); the proof has no length condition (J10). (v) Nothing here bounds N5's
  running time; not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open.
- Data (DATA, not proof): pinned (packet A3, B3), run as `python3 -I`: docs/lit/T33-match-phi-check.py (sha1
  6853179bf10bdf1c3d9cae61c939b1054aa4b70c) "A: improving pairs 80640 | matched with phi rise < 1: 0 | carries: 32534" (80640 / 0 /
  32534; Part A brute-forces the Lemma for K = 6), Part B k = 1..8 strict-rise=True, fixed-top=True, P-changes 1, 3, 7, …, 255, NM 0, 0,
  1, 3, 7, 15, 31, 63; docs/lit/T34-gateshut-check.py (sha1 7c33508b2ef6639da2ce736028bcf013f152ed75, N5 by L-COMP's n5b on Friedmann's
  H_n by L-COMP's hn.py, mode fig) four lines, gate-states with τ(e) = h / with (H1), (H2) / violations / h → d1 flips, of which with
  (H1), (H2): "3 0 0" 135 / 135 / 0 / 0, 0; "3 200 3" 14385 / 14217 / 0 / 102, 0; "4 100 4" 12045 / 11911 / 0 / 97, 0; "5 30 5" 5783 /
  5705 / 0 / 48, 0; S3 and F only, n = 4, 5, 6, 8: 228, 350, 510, 872 gate-states, all with (H1), (H2), 0 violations, 0 flips; the 247
  flips all fail (H1) or (H2) (B3's example rand4 fails (H1), F6). T34 imports hn, census, n5b from a hard-coded ROOT, the checkout at
  run time, not the freeze commit (F5, J3: tree ids of the six directories equal at a23179b0 and trunk 923b5b12, measured by L-LIT).
  Quote checks: P-N5-MPGS-quotecheck.py "quotes=9 bad=0"; P-N5-MPGS-fixes-quotecheck.py "quotes=50 bad=0". All three referees
  reproduced T33, T34 (four lines and S3 + F) and the quote check exactly; both quote checks re-run for this draft on trunk (docs/lit
  equal to l-lit 510c47eb): 9/0, 50/0. L-COMP
  box 18 (claude/l-comp fc0758fc, via the Lead; packet A3): the MATCHED test agrees with L-COMP's on 258,048 pairs; NM per (vertex,
  phase) at most 62 (n 581), max NM/n 1.18 (pl130_n40). REFEREE (successor 17; own scratch/matchphi_probe.py, mp_chain.py (Part (A),
  R-N5-MATCHPHI.md, carried over) and scratch/gateshut_probe.py (sha1 84a77eb7…) on its engine rl_engine; no L-COMP / L-LIT import; H_n
  exported once to .pg): Part (A) exhaustive K = 6, 7: 258,048 + 2,080,768 ordered pairs (78,268 + 571,298 MATCHED), 0 failures; 3,000 +
  2,000 arbitrary and as many weight-increasing sequences, 0 failures; N5: pl130_n40 1 run, 962 P-changes, 688 carries, max PCH / NM per
  (v, phase) 62 / 47 (1.175 n); alt_all n ≤ 100 379 runs, 45,234, 25,585, 67 / 41 (0.90); L-RED instances 319 runs, 29,501, 15,978,
  62 / 47; lib41 349 runs, 30,700, 15,751, 37 / 18; λ-runs (§1b, LAMRUN=1) lib41 38,243 (vertex, λ-run) checks, 31,662 P-changes, 16,291
  carries, 0 failures (the L-RED λ-run batch stopped unfinished, recorded); MUT1 ((M2) dropped) bites 43,975, MUT3 (W := K) bites on
  all-matched chains. Part (B): H_3, H_4 8 runs, 915 (e, d) pairs, 761 states with an (H1)-(H3) route, 733 Corollary checks; H_5, H_6 8,
  1,983, 1,722, 1,678; lib1140 1,857, 334,123, 10,198, 9,052; lib41 1,076, 198,065, 7,857, 6,825; rand_ck 12,000, 176,427, 1,949,
  1,196; 0 failures; step 4 and Fact B2 at every hit, 22,487 checks, 0 failures; Fact B1 on 3,712,665 dual-valuation pairs, 0 failures;
  MUT 1 / 2 / 3 as in "Honest limits" (iii). REFEREE-2 19 (own R2-N5-MATCHPHI/mphi_check.py and R2-N5-MPGS/gateshut_check.py on its
  lane's SPEC loop; no lane module imported): Part (A) every ordered pair, K ≤ 7, every parity pattern, 2,374,900 pairs (661,892
  MATCHED), 0 failures; 25,000 arbitrary subset sequences; N5 alt_all 413 runs, 53,549 P-changes, 23,330 / 30,219 MATCHED / carries,
  max NM 62 (gate_K64_n581, n 581), max NM/n 0.90 (ret22_n40), max PCH 67; lib41_noref × 3 1,230, 70,808, 31,014 / 39,794, 18, 0.469,
  37; named 19, 13,282, 3,763 / 9,519, 47 (pl130_n40), 1.175, 72 (l121_d29); random kO 9,000, 1,221, 872 / 349, 1, 0.125, 2; controls
  CTL_noM2 375,337, CTL_noM1 547,514, CTL_carry_rise 525,558. Part (B): gates with (H1)-(H3) / CORB transitions: H_n 71 runs 22,798 /
  22,412; lib41_noref × 3 1,230 runs 33,572 / 8,934; alt_all 413 runs 12,713 / 4,820; random 30,000 runs 3,902 / 2,123; 72,985 gates,
  0 violations of DENG, B1, GS, S3, S4, S5, CORB; Fact B1 on 10,036,398 same-cycle-node pairs; controls noH1 28/28 (H_n), 2,938/214,496,
  871/104,971, 1,836/20,780; noH2 0/10,837, 0/4,450, 0/241; noH3 2,777/210,912, 1,064/239,267, 581/2,539. REFEREE-2 concurring (successor
  20; own gs_check.py on R2-N5-DUAL/dual_check.Runner and si.py; L-COMP's n5b and hn.py not imported): (state, e, d) with (H1)-(H3) on
  run states (random n 5-14, n 15-24, lib41_noref, H3-H6) 1,523 / 419 / 6,017 / 2,348 and at arbitrary or every τ (tau n 5-10, n 8-14;
  alltau n 4-8, n 8-11) 6,174 / 2,219 / 7,778 / 5,193; 0 violations of GS, GS2-GS5, GSC, B1, ENGXI; X1 / X2 / X3 as in its §3.2 (H3-H6:
  X1 32 of 32); B1 on 76.3M random pairs; λ-run data (REFEREE-2 §C): 56,999 Even and 21,286 Odd (vertex, λ-run) pairs, 0 failures. Run
  counts differ by start set and corpus (REFEREE lib41 1,076 runs in Part (B) and 349 in Part (A); REFEREE-2 lib41_noref × 3 1,230); not
  reconciled in any report. No signed statement uses any count.
- Signatures: REFEREE docs/referee/R-N5-MPGS.md (report c3a0b5d7, sha1 b1a0310d1020ad7d9182d954666f4da4071bdc6b there, successor 17; §1b
  7cd20b05, sha1 988945c360be9b48a41f2db799536c365dfd54a2 there; §C 8da7b717, sha1 7c293a20af130a968df5e91cfee29f072db397dd there,
  successor 18): A0 CHECKED; Fact A1 SIGNED; Lemma MATCH-Φ SIGNED; added statement (A) SIGNED ("proof condensed; MPGS-N1"); B0-B1
  definitions CHECKED; Fact B1 SIGNED; Fact B2 SIGNED; Lemma GATE-SHUT (steps 1-6) SIGNED; added statement (B) SIGNED; A3, B3 reproduced
  exactly, not signed; A4, B4 not signed; §1b λ-runs "YES (Opus 5.5, D15), verbatim"; quotes 9 of 9 (own scratch/flip_quotes.py:
  "QUOTES 9 FAILED 0"); notes MPGS-N1..N5 (MATCH-N2..N4 carried over); "No gap." REFEREE-2 of record docs/referee-2/R2-N5-MPGS.md (report
  0c4524f0, sha1 5ed019b764708f5c61d09e46db4b591672a5a1bf there; successor 19): A0 SIGNED; Fact A1, Lemma MATCH-Φ SIGNED; added
  statement (A) SIGNED ("The first term is SHARP at NM = 0 (N-MP-2)"); B0 "SIGNED (well formed)"; Fact B1, Fact B2, Lemma GATE-SHUT (6
  steps), added statement (B) SIGNED; pinned re-runs "REPRODUCED exactly"; quotes "9/9 VERBATIM" (own qcheck 9/9, SHIFT=1 control 0/9);
  A3, A4, B3, B4 not signed; notes N-MPGS-1..6 (N-MP-2..5 carried over); "No gap." REFEREE-2 concurring docs/referee-2/R2-N5-MPGS-s20.md
  (report c1c4676a, sha1 b34e67d55479895fa3cafa6dad84734a8edb8dc1 there; marked c5f9e76e, sha1 ee4ca241ed54be2f19b3d0dd1076775c92364cd9
  there, and 152503ca, sha1 15f14eb487418908a4e063e407676f85827c0af5 there; successor 20; written without reading 19's report): every
  item SIGNED, no gap, no item FALSE; notes N-GS-1..5; not a third signature. REFEREE-2 §C docs/referee-2/R2-N5-MPGS-C.md (cfc77e84,
  sha1 8d8245369966b60611f9a8ea59dd7cca1e9bfe8a there; final e1ec568a, sha1 6a023656a417841297077b9db5aba6383196442f there; successor 20).
  Superseded-copy reviews (P-N5-MATCHPHI, not routed for landing): REFEREE docs/referee/R-N5-MATCHPHI.md (2f2c40dc, sha1
  b17f092b18e49eccd17c52ac3fb14fca840922b8 there; definitions CHECKED, Fact 1, Lemma MATCH-Φ, Corollary SIGNED, no gap, MATCH-N1..N4)
  and REFEREE-2 docs/referee-2/R2-N5-MATCHPHI.md (5ba3e21d, sha1 097e9858569e2623175b4ab2e314c39cd25c42d3 there; all SIGNED, no gap,
  N-MP-1..5); both carried over to Part (A) by content after a diff (REFEREE §1; REFEREE-2 19 §1; REFEREE-2 20 §1). INDEPENDENCE: REFEREE
  had no docs/referee-2/ MPGS file on its tree and saw 16 names matching "mpgs" on origin/claude/referee-2 at 11:42Z ("names only, none
  opened"); it did not open R2-N5-MATCHPHI.md; it read both REFEREE-2 reports after c3a0b5d7 and 7cd20b05 were pushed (§C). REFEREE-2 19
  opened no file under docs/referee/ on MPGS or MATCHPHI (name counts 0 at 11:17:40Z and 11:25:43Z); REFEREE-2 20 opened no file under
  docs/referee/ before its report (0 at 11:33:19Z and 11:36:04Z), first opened c3a0b5d7 at 12:05Z and §1b at 12:17Z, after both
  REFEREE-2 reports were pushed (§C Inputs). No review imported lane code; the lane's pinned scripts were read, then run, in worktrees
  at a23179b0. §C (both): verdicts identical (REFEREE §C: "VERDICTS IDENTICAL. Every item (A0-A2, B0-B2, Added statements (A), (B)) is
  SIGNED by all three reports; none FALSE; no gap on any side"; REFEREE-2 §C C.1: "SIGNED by both"); joint gap map EMPTY (REFEREE "JOINT
  GAP MAP: EMPTY."; REFEREE-2 "Joint gap map: EMPTY."); REFEREE "E-ITEMS (must change before landing): NONE. Every signed statement and
  proof is correct as frozen at a23179b0."; REFEREE-2 classes C.4 items 1-5 (D1-D4 and C.2's (H2) point) as E, text fixes for the fixes
  file, done as F3-F7 (fixes: "Both agree no statement or proof changes"); J1-J15 / D1-D10 answered in F3-F10; REFEREE: "Nothing open on
  MPGS. NM is OPEN; G-N5-TIME stays OPEN."
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (a reduction of one vertex's path-set changes in one phase of N5 to its
  carries NM, which are not bounded, and a structural lemma on Odd's improving edges in N5; no running-time bound, no algorithm claim).
  GAPS G-N5-TIME: open.

### R86 [refereed-only] N5 on EVERY game: with λ (λ^U) the cycle-node map of Even's valuation Ξ (Odd's valuation U of τ on G^d), a λ-run (λ^U-run) a maximal run of states with λ (λ^U) constant, and, for a stretch R of consecutive states of one run, ENT_R(v, c) the transitions of R at which v's strategy enters c, SW_R(v) := Σ_c ENT_R(v, c) the switches of v, RISE_R(c) the transitions of R at which Ξ(c) changes and PCH_R(c) those at which c's path set P(Ξ c) changes: ENT_R(v, c) ≤ 1 + RISE_R(c) on every stretch, for every Even v and vertex c (Lemma SW-RETURN; dually for Odd v with U on G^d); RISE_R(c) ≤ PCH_R(c) + (PCH_R(c) + 1)(n − 1) on every λ-run R and on every phase R = 𝒫 (Lemma LEN-MONO; dually on λ^U-runs with λ^U); so on every λ-run R Σ_v SW_R(v) ≤ Σ_{(v, c) ∈ E, v Even, SW_R(v) > 0} (1 + RISE_R(c)) ≤ Σ_{(v, c)} n·(PCH_R(c) + 1) ≤ m_E·n·(P*_R + 1), P*_R := max_c PCH_R(c), and a phase 𝒫 has |𝒫| ≤ Σ_v SW_𝒫(v) ≤ the same sums over 𝒫, |𝒫| := the number of transitions t → t + 1 with t, t + 1 ∈ 𝒫 (Theorem COMPOSE; dually for Odd's switches in every λ^U-run); hence every N5 run on every game has T ≤ 2n(n − 1) + (n(n − 1) + 1)·n·(m_E(P* + 1) + m_O(P*^U + 1)) transitions (iterations), P* (P*^U) the most path-set changes of one vertex's Ξ (U) inside one λ-run (λ^U-run) and m_E (m_O) the number of edges leaving Even (Odd) vertices (Corollary COMPOSE-RUN, via RESULTS R47 (a)'s every-game count: at most n(n − 1) transitions change λ and at most n(n − 1) change λ^U); and if MATCH-Φ's bound holds with "phase" replaced by "λ-run" ("λ^U-run" on G^d, read with G^d's parities), then P*_R ≤ (n²/2)(NM*_R + 1) + NM*_R, NM*_R the most carries of one vertex in R, and T is bounded by a polynomial in n, m and the largest carry count NM* = max(NM*_Even, NM*^U) (Corollary COMPOSE-NM, an implication), whose premise both referees sign as holding, with RESULTS R85's MATCH-Φ (landed at trunk 17f51175; CHECKER C94 Add. 2 PASS, b7461dd7), because MATCH-Φ's proof reads verbatim on every λ-run (λ^U-run on G^d), where c = λ(v) is fixed (2026-10-29) — a REDUCTION of N5's iteration count to per-vertex path-set changes P*, P*^U and, with MATCH-Φ, to carries NM*, NM*^U (none of which is bounded here; carries of one vertex reach Θ(N²) per phase, and through the dual mirror per λ^U-run, on L-RED's families, DATA only; not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C95.md, checker 79f2ba92)
- Object (L-SI successor 24, Opus 5.5, D18, Lead reading L40; frozen, unchanged during review): packet P-N5-COMPOSE,
  docs/si/P-N5-COMPOSE-box28.md, sha1 e1b977aa9cf1583d5e0c442a8f87d024230b6524, 141 lines (l-si freeze
  3ca0932d44c407fed38e5fb930744d7107ee79c8, 2026-10-29T11:34:00Z; quote bases b025560c9 (SPEC, RESULTS) and a23179b01 (P-N5-MPGS);
  16 quotes, experiments/si/rund/quotecheck.py, sha1 29bb4a971680c9278f5f8c6f40eac17c0134db72, "quotes=16 bad=0", pinned in
  experiments/si/check.sh with a shifted-line control (--mut: "quotes=16 bad=16", "QUOTES FAIL"); the packet sha1 is pinned in check.sh;
  both referees measured the packet sha1 and the pins): §1 setting with (F-SW) and (F-MON), §2 Lemma SW-RETURN, §3 Lemma LEN-MONO, §4
  Theorem COMPOSE, §5 Corollary COMPOSE-RUN, §6 Corollary COMPOSE-NM (the implication), §7 DATA. The referees' notes are collected by the
  lane in docs/si/P-N5-COMPOSE-fixes-box28.md (F1-F10: L-SI successor 25, l-si 45778960, sha1 3d63f0ab there; F11-F14 appended by L-SI
  successor 26 at l-si 4e928f11aeed2bb38954efa785ef6b93989b3cdf, 2026-10-29T13:36:48Z, append-only (git diff 45778960 4e928f11: 55 lines
  added, 0 removed; then e7c7dd78, 2026-10-29T14:17:47Z, +3 lines in F11 recording the Lead's 13:43Z ruling "D2 … and D3 … are REQUIRED
  appended items, the conservative reading", no statement change); at e7c7dd78 and on trunk sha1 b4c69e110d3c57eae73697d36729134f60ab5ea1,
  164 lines; 19 quotes checked by
  docs/si/P-N5-COMPOSE-fixes-quotecheck.py, sha1 45ff072708e4bd78591174fc556ea19040496470, "quotes=19 bad=0", a mutated quote caught in
  check.sh). The fixes file: "This file changes NO signed statement and NO proof step; every F-item below is APPENDED text that is read
  together with the packet". F1 and F11 define |𝒫| as the number of transitions (COMP-E1, E-item of both referees); F2 reads LEN-MONO and
  Theorem COMPOSE's first statement on any stretch with λ (λ^U) constant (N-C2 = REFEREE-2 §C D2); F3 reads Odd's side of §6 with G^d's
  parities (N-C3 = D3); the Lead ruled D2, D3 required ("Ruling: D2, D3 REQUIRED (already appended as fixes F2, F3)", 13:48Z). F4
  defines P*^U for the title, F5 says RISE counts changes, F6 spells out (F-MON)'s set I (optional: COMP-N1..N3 = D4-D6); F7 and F12
  record [MΦ]'s status, F8 the [MΦ] quote form (N-C1), F9 and F14 data figures, F10 (F-MON) on Odd's side, F13 REFEREE §C C11 = REFEREE-2
  §C D11 as OPEN: each a "No change, because" clause. The statements below are in the frozen wording with F1/F11, F2 and F3.
  Setting (every game): N5 = SPEC S1-S5 (docs/new/N5-ssi-global.md) with FIX 1-4; G any parity game, n = |V|; a run is the sequence of
  states (σ_t, τ_t), t = 0, …, T, a TRANSITION is t → t + 1; m_E (m_O) the number of edges leaving Even (Odd) vertices. Ξ_t := Ξ_{σ_t},
  S1's valuation (c, P, ℓ) against Odd's optimal counterstrategy, a function of σ_t only (R15 (d)); λ_t(v) its cycle node; U_t := Odd's
  valuation of τ_t on the dual game G^d (R47's setting), λ^U_t its cycle node. A λ-RUN: a maximal run of consecutive states with λ_t
  constant (τ free); a λ^U-RUN likewise; a PHASE: a maximal run with (λ_t, τ_t) constant (RESULTS R38 (a)), which lies inside one λ-run.
  For a stretch R (consecutive states of one run) and vertices v, c: ENT_R(v, c) := #{t : t, t + 1 ∈ R, σ_t(v) ≠ c = σ_{t+1}(v)} (Even
  v; τ for Odd v), SW_R(v) := Σ_c ENT_R(v, c); RISE_R(c) := #{t : t, t + 1 ∈ R, Ξ_{t+1}(c) ≠ Ξ_t(c)}; PCH_R(c) := #{t : t, t + 1 ∈ R,
  P(Ξ_{t+1} c) ≠ P(Ξ_t c)}; RISE^U, PCH^U the same with U_t on G^d; P*_R := max_c PCH_R(c), P* := max over λ-runs R of P*_R, P*^U likewise
  over λ^U-runs. F11: "|𝒫| := number of transitions t → t + 1 with t, t + 1 ∈ 𝒫." F1: for any stretch R, "|R| := #{t : t, t + 1 ∈ R},
  the number of TRANSITIONS inside R (one less than its number of states)", and "«transitions (iterations)» in Corollary COMPOSE-RUN count
  transitions". (F-SW): every Even switch goes along an edge of Iσ_t (S4a, S4c), every Odd switch along Iτ_t (S4b, S4c). (F-MON): Ξ_{t+1}
  ⊵ Ξ_t at every vertex and every transition (R15 (a) with (d)); dually U_{t+1} ⊵ U_t in G^d's order. §1 cells: REFEREE "CHECKED (F-SW
  and F-MON are correct consequences of S4a-c, [STEP], [MON]; |𝒫| is not defined: COMP-E1)"; REFEREE-2 "SIGNED (well formed; F-SW and
  F-MON proved correctly from [S4a-c], [STEP], [MON])".
- Claims signed (both referees "(Opus 5.5, D15)": REFEREE successor 18, REFEREE-2 successor 20). Each item below is SIGNED in both verdict
  tables (REFEREE "## Verdicts", l. 13-22 of R-N5-COMPOSE.md; REFEREE-2 "## 0. Verdicts", l. 27-36 of R2-N5-COMPOSE.md; REFEREE-2 §C
  C.1: "SIGNED by both" for §2-§6), in the frozen wording with the required appended text F1/F11, F2, F3. On every game; no item uses
  (P). Premises LANDED: SPEC S1 (valuation, order, Ξσ), S2, S4a-c (quote base b025560c9); RESULTS R15 (a) Lemma A ([MON]) and (d)
  ([STEP]); RESULTS R47 (a) Lemma Φ (every game), item (c) only ([Φ]); RESULTS R84 (a) Fact DELTA; RESULTS R38 (a), as the phase
  definition only. Premise for (e) only: RESULTS R85 (A) (P-N5-MPGS; landed at trunk 17f51175,
  2026-10-29T14:02:36Z, CHECKER C94 Add. 1 7e309075; landed check C94 Add. 2 PASS, b7461dd7).
  (a) Lemma SW-RETURN (§2): "For every run of states R of an N5 run, every Even v and every vertex c: ENT_R(v, c) ≤ 1 + RISE_R(c).
      Dually for Odd v with U." (Ξ-SUCC: Ξ_t(σ_t v) is non-decreasing in t, by (F-MON), (F-SW) and [S2]. For consecutive entries e < e′
      of v into c and the step s ∈ [e + 1, e′ − 1] at which v leaves c: Ξ_{e′}(c) ▷ Ξ_{e′}(σ_{e′} v) ⊵ Ξ_{s+1}(σ_{s+1} v) ⊵ Ξ_s(σ_{s+1}
      v) ▷ Ξ_s(c) ⊵ Ξ_{e+1}(c), so Ξ(c) changes at a transition in [e + 1, e′ − 1] ⊆ R; these windows are disjoint.) Cells: REFEREE
      "SIGNED", REFEREE-2 "SIGNED"; REFEREE §2: "No phase, no λ, no τ used: it holds on ANY stretch of consecutive states, fallbacks
      included."
  (b) Lemma LEN-MONO (§3) on every λ-run and, with F2, on every phase 𝒫 (a stretch inside one λ-run, RISE_𝒫 and PCH_𝒫 counted inside 𝒫): "For every λ-run R and every vertex c: RISE_R(c) ≤ PCH_R(c) + (PCH_R(c) + 1)(n − 1). Dually for
      λ^U-runs with U.", F2 appended: "In Lemma LEN-MONO and in Theorem COMPOSE's first statement, "every λ-run R" is to be read as
      "every stretch R of consecutive states on which λ is constant" (dually λ^U); a λ-run and a phase are such stretches." Signed here for λ-runs and phases only; F2's reading for every stretch with λ constant: Referee strengthening (0). (On R the
      cycle node c₀ of Ξ_t(c) is fixed; by (F-MON) and [S1-ord] the weight of P never falls and rises strictly at a P-change ([DELTA]),
      so the P-values form PCH_R(c) + 1 contiguous blocks; inside a block only ℓ changes, strictly in the direction [S1-ord] prefers for
      Ω(c₀), and ℓ ∈ {0, …, n − 1}; so RISE_R(c) ≤ n·PCH_R(c) + n − 1.) Cells: REFEREE "SIGNED" (row "Lemma LEN-MONO (any λ-run /
      λ^U-run)"); REFEREE-2 "SIGNED (it holds on any stretch with λ constant: N-C2)". The stretch reading, for the phase: REFEREE
      §4, inside its signed phase part: "a phase lies inside one λ-run, so LEN-MONO applies to it (cycle nodes fixed)"; REFEREE §C
      C3: "I agree: the proof never uses maximality" (classed "optional (wording; one word)"); REFEREE-2 §C D2: "Applying the λ-run
      bound to the enclosing λ-run would give PCH_R, not PCH_𝒫, so the phase statement needs the stretch form".
  (c) Theorem COMPOSE (§4), with F1/F11, and F2 for the phase statement: "For every λ-run R of an N5 run on any game, the Even switches inside R satisfy Σ_v
      SW_R(v) ≤ Σ_{(v, c) ∈ E, owner(v) = Even, SW_R(v) > 0} (1 + RISE_R(c)) ≤ Σ_{(v, c)} n·(PCH_R(c) + 1) ≤ m_E·n·(P*_R + 1). For every
      phase 𝒫 (inside a λ-run R): |𝒫| ≤ Σ_v SW_𝒫(v) ≤ the same sums with R replaced by 𝒫. Dually for Odd's switches in a λ^U-run.";
      F2: "Theorem COMPOSE's phase statement is the first statement applied to the stretch 𝒫, with RISE_𝒫, PCH_𝒫 counted inside 𝒫."
      (SW_R(v) = Σ_{c ∈ succ(v)} ENT_R(v, c), then SW-RETURN, then LEN-MONO, summed over the Even v that switch; in a phase τ is constant,
      so by [STEP] every transition of 𝒫 changes σ, i.e. contains an Even switch.) Cells: REFEREE "SIGNED, with |𝒫| read as the number of
      transitions inside 𝒫 (COMP-E1: under the "number of states" reading the phase part is FALSE)"; REFEREE-2 "SIGNED"; REFEREE-2 §C
      C.1: "SIGNED by both, with COMP-E1". (REFEREE §1: read as states, "a one-state phase gives 1 ≤ 0".)
  (d) Corollary COMPOSE-RUN (§5): "Every N5 run on every game has T ≤ 2n(n − 1) + Σ_{λ-runs R} Σ_v SW_R(v) + Σ_{λ^U-runs R′} Σ_{Odd
      v} SW_{R′}(v) ≤ 2n(n − 1) + (n(n − 1) + 1)·n·(m_E·(P* + 1) + m_O·(P*^U + 1)) transitions (iterations)." (Classify each transition,
      S4c fallbacks included, by the first of (i) λ changes, (ii) σ changes, (iii) λ^U changes, (iv) otherwise, when τ changes by [STEP];
      a kind-(ii) transition holds an Even switch of one λ-run, a kind-(iv) one an Odd switch of one λ^U-run; [Φ] (c), RESULTS R47 (a)
      Lemma Φ (every game): "along a run at most n(n − 1) transitions change λ and at most n(n − 1) change λ^U", read separately for each
      map, so at most n(n − 1) + 1 λ-runs and as many λ^U-runs; Theorem COMPOSE on each. Not used: R47's joint count, Corollary Φ-1O,
      R48. Fallbacks: an Even fallback is kind (i) or (ii), an Odd fallback kind (iii) or (iv); "No transition is uncharged".) Cells:
      REFEREE "SIGNED" (row "Corollary COMPOSE-RUN (every run, every game), including the classification and the fallback paragraph");
      REFEREE-2 "SIGNED (Lead's points (1) and (2) checked: §2.4)" (row "Corollary COMPOSE-RUN: T ≤ 2n(n−1) +
      (n(n−1)+1)·n·(m_E(P*+1) + m_O(P*^U+1)), every run, every game").
  (e) Corollary COMPOSE-NM (§6), the implication, with F3: "If [MΦ] holds with "phase" replaced by "λ-run" (resp. "λ^U-run" on G^d),
      then P*_R ≤ (n²/2)(NM*_R + 1) + NM*_R with NM*_R the most carries of one vertex in R, and Corollary COMPOSE-RUN bounds T by a
      polynomial in n, m and the largest carry count NM* (over both players)."; F3 appended: "On Odd's side (λ^U-runs of U on G^d),
      P-changes, MATCHED, CARRY and the carry count NM^U are read on G^d, i.e. with G^d's parities (Ω + 1; the ranks are those of G). NM*
      in the Corollary is max(NM*_Even, NM*^U)." (K ≤ n − 1 gives K(K + 1)/2 ≤ n²/2.) [MΦ] is P-N5-MPGS (A)'s Corollary, the subject of
      RESULTS R85 (A): "PCH_𝒫(v) ≤ (K(K+1)/2)·(NM_𝒫(v) + 1) + NM_𝒫(v)", K the number of ranks above rank(λ(v)), NM_𝒫(v) v's carries.
      Its λ-run form, the implication's premise, sits in both verdict cells for §6: REFEREE "SIGNED as an implication; its premise
      "[MΦ] on λ-runs" HOLDS (§6 below: MΦ's proof reads verbatim with c fixed; my predecessor's R-N5-MPGS §1b agrees), so the
      conclusion holds with [MΦ] as signed by both referees"; REFEREE-2 "SIGNED as an implication. The "phase → λ-run" replacement is
      VALID (Lead's point (3), §2.5). Read NM^U with G^d's parities (N-C3)". The λ^U-run side: REFEREE's cell names λ-runs; its §6,
      which the cell cites: "on λ^U-runs it holds for U on G^d (G^d is a game with the same ranks; MATCHED is then read with G^d's
      parities)"; REFEREE-2 §2.5: "MATCH-Φ's proof holds for every parity pattern, so the bound holds (N-C3)". Hence, with RESULTS R85's
      MATCH-Φ (landed at 17f51175, landed check PASS b7461dd7): P*_R ≤ (n²/2)(NM*_R + 1) + NM*_R on every λ-run R (and on every λ^U-run,
      NM^U read on G^d), and T is bounded by a polynomial in n, m and NM*. This is the λ-run form that RESULTS R85 carries as Referee
      strengthening (0), "To be signed with P-N5-COMPOSE, which uses it" (CHECKER C94 §3).
- Not signed: §7 (DATA; REFEREE "DATA, not signed; reproduced EXACTLY (below)", REFEREE-2 "DATA, not signed. Reproduced EXACTLY
  (§3.1)") and its "Slack (READING)". The packet's own label of §6, "PROVED from an ASSUMED premise (sign only the implication)", and its
  "Note for the referees", which calls the λ-run replacement "a reading of [MΦ]'s proof, to be confirmed by its referees": confirmed in
  both §6 cells (item (e)); the premise itself is R85's, not this entry's. LEN-MONO across a λ-change: not claimed; whether the
  restriction is needed is OPEN (F13; "Honest limits" (iii)). The fixes file's records F7, F12 ("[MΦ] is signed by both referees";
  "When P-N5-MPGS lands, §6's premise is that entry plus this referees' remark") and F9, F13, F14: lane records ("This file is a lane
  record, not refereed text"). F4-F6 (optional wording): bullet "Referee strengthening" (i), (ii).
- Referee strengthening (NOT part of this entry; remarks of one or both referees outside the verdict cells, or optional wording):
  (0) F2's general reading (N-C2 = REFEREE-2 §C D2; the Lead ruled D2 required as appended text, 13:43Z): LEN-MONO and Theorem
  COMPOSE's first statement on every stretch of consecutive states with λ (λ^U) constant. REFEREE-2 §3 cell: "SIGNED (it holds on any
  stretch with λ constant: N-C2)"; REFEREE: its §3 row signs "any λ-run / λ^U-run", its §4 applies the Lemma to a phase ("a phase lies
  inside one λ-run, so LEN-MONO applies to it (cycle nodes fixed)"), and its §C C3 "I agree: the proof never uses maximality", classed
  "optional (wording; one word)". Not used by any signed item beyond λ-runs and phases.
  (i) COMP-N2 = D5 (F5): RISE_R(c) counts changes of Ξ(c), and by (F-MON) every such change is a strict rise. REFEREE §8: "COMP-N2:
  SW-RETURN's RISE_R(c) counts CHANGES of Ξ(c); by F-MON they are rises."; REFEREE-2 §C D5: "Agreed" (class "opt"). The signed items
  count changes (≠), as defined. (ii) COMP-N3 = D6 (F6): (F-MON)'s set is I := {(v, σ_{t+1}(v)) : σ_{t+1}(v) ≠ σ_t(v)} ⊆ Iσ_t by (F-SW);
  REFEREE-2 §C D6: "Agreed; my §2.0 used exactly this I" (opt); COMP-N6 = D9 (F10): "F-MON on the Odd side is [MON] applied to G^d, as in
  R47's Lemma Φ (b) citation chain (PHI-N1 = N-PHI-2); no new premise." (both: REFEREE-2 §C D9 "Same"). (iii) The classification by what
  changes (REFEREE §5, a remark on the fallback paragraph): "A transition where S4a runs but leaves σ unchanged and S4b changes τ is (i),
  (iii) or (iv): the classification is by what changes, not by which step ran, so it is covered." The packet's sentence "A transition
  applying S4a and S4b together is charged to its Even switch (kind (ii)) unless λ changes" presumes σ changes; REFEREE-2 §2.4: "S4a + S4b
  together is kind (i) or (ii)". No gap: the proof classifies by what changes. (iv) REFEREE §5 on [Φ] (c): "Its content is elementary
  from (a), (b): reward is injective, so each vertex's λ changes ≤ n − 1 times, and each λ-changing transition changes some vertex."
  (v) COMP-N4 = D7, C5 (F7, F12): REFEREE §8: "the λ-run reading of [MΦ] is now confirmed by the first referee twice (R-N5-MPGS §1b, here
  §6); it can be stated as a remark of the landed MPGS entry rather than an assumption."; REFEREE §C C5 (1680010b): "§6 can land as
  "COMPOSE-RUN with [MΦ] (citing the landed MPGS entry) gives …", the λ-run transfer as a referees' remark."; REFEREE-2 §C D7: "Agreed.
  It is now confirmed by both referees (R2-N5-MPGS-C, "§1b AGREED"), so the packet's ASSUMED label on [MΦ] is resolved once MPGS lands"
  (opt). Status: this entry states the λ-run form inside item (e) because both §6 verdict cells carry it; R85 as landed carries it as Referee strengthening (0), "To be signed with P-N5-COMPOSE, which uses it"; this entry signs it (item (e)).
- Honest limits: (i) COMPOSE is a REDUCTION of N5's total iterations to P*, P*^U and, with R85's MATCH-Φ, to the carries NM*, NM*^U.
  None of them is bounded here (packet SCOPE: "P* and the carry counts are NOT bounded here"; REFEREE: "Nothing here bounds P* or NM*").
  The bound is polynomial in n, m and P* (or NM*), and P* is not bounded. NM* and NM*^U are OPEN. DATA only, not refereed: L-RED's R109
  (claude/l-red e5c9b628, docs/red/R109-hn-topgate.md §5; L-COMP's nm.py unmodified, phases keyed by r38 = (λ_Ξ, τ)): carries of one
  vertex in one phase reach max NM 343 (max PCH 354) on topfix n 12 (N 252 vertices), NM / N 1.361, "max NM = 2n² + 5n − 5", "Carries of
  ONE vertex in ONE phase are Θ(N²) on this family"; there "NM*^U = 0 exactly" (τ never changes). L-RED's R111 (claude/l-red 463bec6e,
  1811cae2, docs/red/R111-dual-tau-runs.md): on G^d N5's run is the mirror of the run on G (DATA, two pins: "σ_G = τ_{G^d} and τ_G =
  σ_{G^d} at EVERY state"); 264 τ-changes inside one joint λ-run (dual runquad_K8_m30); NM^U = 163 = 2n² + 5n − 5 per vertex per λ-run
  on dual hntop_n8 is a READING through the mirror ("Not measured directly: nm.py is Even-side only"); "Both are polynomial". (ii) T
  counts iterations (transitions), not bit operations; nothing here bounds N5's running time. (iii) OPEN (F13): whether LEN-MONO's
  restriction to stretches with λ constant is needed. REFEREE §C C11: "OPEN in data, not a finding (the proof uses it; LEN-MONO across a
  λ-change compares different cycle nodes)"; REFEREE-2 §3.2: "X_LENfull (LEN-MONO across λ-changes) never bit"; REFEREE-2 §C D11:
  "neither shows the λ restriction of LEN-MONO is needed". The restriction of the phase bound to phases is needed (REFEREE MUT 4: 423
  violations on whole λ-runs), and so are SW-RETURN's "+1" and LEN-MONO's length term (MUT 1, MUT 3; REFEREE-2 X_SWR0, X_LEN0). (iv)
  Slack (READING, packet §7 and COMP-N5): "the factor n of LEN-MONO and MΦ's n²/2 are the loose links". (v) Not M3, not a step-4 pass,
  not a TARGET.md claim; G-N5-TIME stays open. Item (e)'s conclusion rests on R85 (A) (landed at 17f51175, landed check PASS b7461dd7).
- Data (DATA, not proof): pinned (packet §7; experiments/si/chg/compose.py, sha1 9fc3b081bff815a72597a394af918786e3d6f2ec, check.sh box
  28 §9), run as `python3 -I` from experiments/si: runquad_K8_m30_n192 "TOP (263, 'chg/instances/red/runquad_K8_m30_n192.pg', 0, 263,
  481, 1016, 195072, 265890048, 8, 15, 15, 15, 192)" (L = 263 ≤ S1 = 481 ≤ S2 = 1,016 ≤ S3 = 195,072 ≤ S4; max NM 8, max PCH = max
  RISE = max SW = 15; n = 192; instance sha1 ebaa6ac57ec60948fb986210c27479cb3a7961d9, L-RED's R106 pin), I0 I1 LDIR LBLK I2 I3 PASS;
  dlsep_kill_n70 "TOP (12, 'chg/instances/dlsep_kill_n70.pg', 0, 12, 39, 387, 26810, 14059640, 5, 6, 7, 4, 70)" (sha1
  e500ea47e1dc0163b32a97042ff9752daf6db83a), the same six PASS; MODE=run seglast_kill_n110 "TOP (16, 'lay/instances/seglast_kill_n110.pg',
  0, 16, 27, 152, 16066, 0, 20, 1, 4, 2, 110)" (T = 16 ≤ 20 Even + 1 Odd in-run switches + 4 λ- and 2 λ^U-changes = 27), RUNI0 R47 EI1 OI1
  ELDIR OLDIR ELBLK OLBLK PASS, also on segcount_kill_n20. Re-run for this draft on trunk 764101b1 (compose.py sha1 as above; rund/,
  lay/ and root/ tree ids equal to 3ca0932d's, chg/ only 16 added files): the three TOP lines identical, every PASS line as listed;
  quote checks: packet "quotes=16 bad=0" (--mut "quotes=16 bad=16", "QUOTES FAIL"), fixes "quotes=19 bad=0" (mutated: "quotes=19
  bad=1"). Packet corpora (chg/compose_*.txt, chg/composerun_*.txt): every inequality on all phases of alt_all pinned starts (457), lib41
  (418), all experiments/si instances (345) and all runs (413, 412, 276); per vertex per phase NM 42 and PCH 71 at most, at n 41
  (l121reader_n41); at most 31 λ-runs and 28 λ^U-runs in one run; L-RED's R106 mkr.py families NM = K, PCH = 2K − 1; ladderd0_k48_n156
  NM 0, PCH 48. REFEREE (successor 18; own scratch/compose_probe.py, sha1 239d122e…, on its engine rl_engine; no lane code; pinned
  re-runs in a worktree at 3ca0932d, exact): library (n ≤ 64) 763 runs, 12,426 transitions, SW-RETURN checks 87,161 (strong form 7,057),
  LEN-MONO 129,260, kinds (i)/(ii)/(iii)/(iv) 2,101 / 9,964 / 238 / 123; lane pins 15, 512, 2,468 (610), 8,818, 43 / 463 / 5 / 1; random
  rand_ck n 5-16 6,000, 10,171, 82,509 (20), 232,299, 5,878 / 2,262 / 1,471 / 560; random n 6-16 with MPHI 4,000 runs; 0 violations; at
  most 29 λ-runs and 14 λ^U-runs in one run (library); [MΦ] on every λ-run of both players: library 294 games, 29,931 (Even) + 12,222
  (Odd, on G^d) (vertex, λ-run) checks, random 4,000 runs, 94,226 + 71,142, 0 failures, max NM 15; MUT 1 14,867, MUT 2 3, MUT 3 3,144,
  MUT 4 423 violations (all bite); a batch rand n 16-30 stopped unfinished (recorded). REFEREE-2 (successor 20; own
  R2-N5-COMPOSE/compose_check.py on its lane's dual_check.Runner and si.py, MATCHED test mphi_check.matched; lane code only run as the
  pinned re-runs, exact): 14,428 runs, 40,406 transitions, SWR checks 523,231 / 319,059 (Even / Odd), LEN 551,515 / 440,798, CMP 31,125
  / 26,918, 2,840 phases, 0 violations of FSW, FMON, SWR, LEN, LENB, LEND, CMP, RUN, NM; kinds 13,857 / 19,061 / 5,104 / 2,384; at most 29
  λ-runs and 32 λ^U-runs in one run (lib41); [MΦ] on 56,999 Even and 21,286 Odd (vertex, λ-run) pairs, max NM 62 / PCH 67 (alt_all) and
  42 / 71 (l121reader_n41); controls X_SWR0 "233,008 (stretch, v, c) checks", X_LEN0 "42,128 (λ-run, c) checks", X_RUN0 "bites at 8,597
  runs", X_LENfull never bit; strict quote check 15/16 (the miss is [MΦ]'s joined quote, N-C1; F8), SHIFT=1 control 0/16; max S1/S2 0.8.
  Run counts: REFEREE's §C says "mine 6,778 runs", REFEREE-2's §C D12 "REFEREE: 10,778 runs (763 library + 15 pins + 6,000 + 4,000
  random)"; F14 (lane reading) puts the difference at REFEREE's 4,000 MPHI runs; not reconciled by REFEREE. No signed statement uses any
  count.
- Signatures: REFEREE docs/referee/R-N5-COMPOSE.md (report 4896bc2e, 2026-10-29T12:51:21Z, sha1 3c29700d886cf1604fd49e19f2ab071ecca0d404
  there; §C c6011b70, 13:09:45Z, sha1 25b431846675f10883d3831acd5abd38de5ddbee there; §C wording 1680010b, 13:17:12Z, sha1
  5f7fa31269f160a3bf76f1ba6eed5af7aab12d03 there, = claude/referee head and trunk; successor 18; append-only after 4896bc2e): §1 CHECKED;
  §2 SW-RETURN SIGNED; §3 LEN-MONO SIGNED; §4 Theorem COMPOSE SIGNED with |𝒫| as transitions; §5 COMPOSE-RUN SIGNED; §6 COMPOSE-NM
  SIGNED as an implication, premise on λ-runs HOLDS; §7 DATA, reproduced exactly; quotes "quotes=16 bad=0"; E-item COMP-E1; notes
  COMP-N1..N6; "No gap in the mathematics." REFEREE-2 docs/referee-2/R2-N5-COMPOSE.md (report 4b8afa95, 2026-10-29T11:59:33Z, sha1
  3bc4f67cf8536f82c2c48e114c1e091cbd6a85db there; §C appended ee549524, 13:10:01Z, sha1 8a04defa57089c9eb271e77a22fa1df15b69a726 there, =
  claude/referee-2 head and trunk; successor 20): §1 SIGNED; §2-§5 SIGNED; §6 SIGNED as an implication, λ-run replacement VALID; §7 DATA,
  reproduced exactly; "No gap. No item FALSE."; notes N-C1..N-C5. INDEPENDENCE: REFEREE: "14 names matching "compose" under
  docs/referee-2/, 12:40Z; names only", "None opened.", and it read REFEREE-2's report "only after this report was pushed (4896bc2e)";
  REFEREE-2's name count of COMPOSE files on origin/claude/referee was 0 at 11:54:22Z and 11:59:23Z, and it first opened REFEREE's
  report at 13:09Z, after 4b8afa95 was pushed ("Neither referee had read the other's report before writing its own."). No review
  imported lane code.
  §C (both): verdicts identical (REFEREE: "VERDICTS IDENTICAL: §2 SW-RETURN, §3 LEN-MONO, §4 Theorem COMPOSE, §5 COMPOSE-RUN SIGNED by both;
  §6 COMPOSE-NM SIGNED as an implication by both"; REFEREE-2 C.1: "SIGNED by both" for §2-§6); joint gap map empty (REFEREE "JOINT GAP
  MAP: EMPTY. ONE E-ITEM: COMP-E1"; REFEREE-2 "Joint gap map: no mathematical gap."); COMP-E1 agreed as the E-item by both (REFEREE-2 §C
  C.2: "AGREED, it is an E-item"), done as F1 and F11; REFEREE §C C1-C11 classes C3 = N-C2 and C4 = N-C3 "optional", REFEREE-2 §C C.3
  classes D2 = N-C2 and D3 = N-C3 as E; the Lead ruled them required (13:48Z), done as F2, F3; C.4 joint list items 1-4 answered in F1-F8;
  REFEREE: "Nothing open on COMPOSE beyond COMP-E1. P*, P*^U and NM* are not bounded; G-N5-TIME stays OPEN."
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (a reduction of N5's iteration count on every game to per-vertex path-set
  changes P*, P*^U and, with MATCH-Φ, to carries NM*, NM*^U, which are not bounded; no running-time bound, no algorithm claim).
  GAPS G-N5-TIME: open.

### R87 [refereed-only] N5-SF (SPEC S1-S5 with S4a's opponent τ replaced by Odd's best reply σ̄(σ), S4b mirrored) terminates (Lemma SF-TERM; R15 (c), (d)); its sequence of distinct σ depends on σ_0 alone and that of τ on τ_0 alone (Lemma DECOUPLE); and its iteration count I satisfies SBC/2 ≤ I < (n + m + 1)(2(n² − n + 1) + SBC), SBC = the σ-changes at which σ̄(σ) changes plus the mirror (Theorem SF-RED; R15 (a), (c), (d), R17 (c), (e)): a reduction, polynomial iff SBC is (2026-10-29) — a REDUCTION for a VARIANT (N5-SF) of N5 (SBC is not bounded here; CONJECTURE SF-POLY (SBC polynomial) OPEN; output correctness not claimed (N5-SF stops, like N5, at a σ with Iσ = ∅, the hypothesis of RESULTS R57 (b) Lemma OUT-G; that application is not signed here); it says nothing about N5 itself; not M3, not a gauntlet pass, not a TARGET.md claim; G-N5-TIME untouched), CHECKER PASS (docs/checker/C96.md, checker 738a7762)
- Object (L-NEW successor 33, Opus 5.5, D14/D18, Lead reading L40; frozen, unchanged during review): packet P-N5-SF,
  docs/new/P-N5-SF-box55.md, sha1 dbc2345f62454d442e951de025b1b2aef8a35317, 172 lines (l-new freeze
  95a7a581353157ebc13bd57ae1ffe318e3ba581d, 2026-10-29T15:46:10Z; `git diff 95a7a581 3d8b357d` on the file is empty; quote base trunk
  305cc8be (2026-10-29T15:12:21Z); 18 quotes, experiments/new/box49/quotecheck3.py, sha1 eaf184117e025caa94e06bcecf456b595dffc9d5,
  "quotes=18 bad=0", --mut "quotes=18 bad=18", "QUOTES FAIL"; the packet sha1 is pinned in experiments/new/check.sh block "Box 55"
  (l. 190-210 at trunk 3d8b357d); both referees measured the packet sha1 at 95a7a581): §0 definitions, §2 Lemma SF-TERM and Lemma
  DECOUPLE, §3 Lemma ONE-PLAYER and Theorem SF-RED (a)-(c), Remarks 1-2 (READING), §4 DATA and the pinned check, §5 not to sign. The
  RESULTS line is the packet's "Proposed RESULTS line (as sent to the Lead 15:27:39Z, verbatim)" (packet l. 14-18), approved by the
  Lead as the packet records it (l. 5: «Lead 15:39Z: «push. Your RESULTS line is approved as worded at 15:27:39Z.»»); the title above
  is that line, unchanged, with the date and the scope parenthesis. The referees' notes are answered by the lane in
  docs/new/P-N5-SF-fixes-box55.md (F1-F6: L-NEW successor 33, l-new 122c2f6866c21f46b10a9aad47b32c0a4d4bb7eb, 2026-10-29T16:22:01Z,
  sha1 b4534e02cb143add059e567b9a015d3ea020c7df there, 35 lines; F7-F13 appended at l-new e9daffde325fcf0fda0ef76f986e7a667a940ef6,
  2026-10-29T16:52:01Z, append-only (`git diff 122c2f68 e9daffde`: 52 lines added, 0 removed); at e9daffde and on trunk 3d8b357d sha1
  d937c8a9110297e961cc2fb9398631e7c41472ac, 87 lines; 6 quotes at trunk e251d147 (2026-10-29T16:39:24Z), checked by quotecheck3.py,
  "quotes=6 bad=0", --mut "quotes=6 bad=6", "QUOTES FAIL", pinned in check.sh block "P-N5-SF fixes file" (l. 232-238)). The fixes
  file: «Each item is a CLARIFICATION: no statement of the packet is widened or changed.» F1 and F7 name ONE-PLAYER (a)'s standing
  premises; F2 gives the τ-side mirror of ONE-PLAYER (b) (S1 on the dual of a G^d-arena is H′ with Ω + 2); F3 reads SF-RED (a)'s proof
  with "a prefix of a λ-phase"; F8 cites R17's source proof for "the S4c step changes no valuation"; F9 gives the full S4a quote
  (with «Else σ_new = σ»); F10 says "the same arena H" is the same graph with the same increasing-index lists; F6 reads "iff" in SF-RED
  (c); F4, F5, F11, F12 are DATA; F13 says the LAM argument is proved in place. The statements below are in the frozen wording, read
  with F3, F7, F8, F9 (and F2, F10 in the proofs).
  Setting (every game): G = (V, E, Ω, owner) as in SPEC (docs/new/N5-ssi-global.md), n := |V|, m := |E|; priorities made injective by
  p′ (S1). σ̄(σ) := Odd's optimal counterstrategy to σ computed by S1's procedure (a deterministic function of (G, σ)); Ξσ := the
  valuation of every vertex under (σ, σ̄(σ)) (S1); Iσ := Even's improving edges (S2); λ_Ξ(σ) := v ↦ the cycle node of Ξσ(v); mirror
  τ̄(τ), Ξτ, Iτ, λ_Ξ(τ) on G^d. N5-SF := SPEC S1-S5 with exactly two changes: S4a′ (in S4a's arena H every Odd v keeps only the edge to
  σ̄(σ)(v), not τ(v), and σ_new is S1's Odd optimum in the dual of H to σ̄(σ)), S4b′ (mirrored: every Even v of H′ keeps only τ̄(τ)(v));
  S4c (with FIX 3), S4d, S5 and the iteration count unchanged. A(σ) := S4a′'s σ_new (Iσ ≠ ∅); F(σ) := A(σ) if A(σ) ≠ σ, else σ with
  every Even v that has an improving edge switched to S4c's choice (argmax of (Ξσ(w), w) over (v, w) ∈ Iσ); F undefined when Iσ = ∅;
  F^d the mirror. The run: states (σ_k, τ_k), k = 0..I, I the number of iterations; the distinct-σ sequence σ^(0), …, σ^(p) (consecutive
  repetitions removed), #σ := p + 1; τ^(0), …, τ^(q), #τ := q + 1. G_σ̄ := G with every Odd v cut to the single edge (v, σ̄(v)), a
  one-player game in R17's sense. SBC_σ := #{j < p : σ̄(σ^(j+1)) ≠ σ̄(σ^(j))}; LAM_σ := #{j < p : λ_Ξ(σ^(j+1)) ≠ λ_Ξ(σ^(j))}; SBC_τ,
  LAM_τ the mirror (τ̄, G^d); SBC := SBC_σ + SBC_τ. A STRETCH: a maximal interval [a, b] of indices of the distinct-σ sequence on which
  σ̄(σ^(j)) and λ_Ξ(σ^(j)) are constant. §0 cells: REFEREE «CHECKED (well formed; S4a′/S4b′ are S4a/S4b with the opponent argument
  replaced, nothing else)» (l. 16); REFEREE-2 «SIGNED (well formed; F is a function of σ alone)» (l. 36); both §Cs: "same content"
  (REFEREE §C l. 13), "agreed" (REFEREE-2 §C l. 14).
- Claims signed (both referees "(Opus 5.5, D15)": REFEREE successor 18, REFEREE-2 successor 20). Each item below is SIGNED in both verdict
  tables (REFEREE "## Verdicts", l. 13-25 of R-N5-SF.md; REFEREE-2 "## 0. Verdicts", l. 33-46 of R2-N5-SF.md; REFEREE §C table l. 10-21
  "SIGNED" in the joint column; REFEREE-2 §C C.1 l. 11-24 "SIGNED by both"), in the frozen wording read with F3, F7, F8, F9. On every
  parity game; every start pair; no item is about N5's own run. Premises LANDED: SPEC S1 (injective priorities, order, Ξσ, Odd's side),
  S2, S4, S4a (packet quote l. 51-53 and its full form with «Else σ_new = σ», F9, at e251d147), S4c, FIX 3, S5 (quote base 305cc8be);
  RESULTS R15 (a), (c), (d); RESULTS R17 (c), (e), with R17's source proof for the flatness of the S4c step (F8:
  docs/new/N5-phase-bound-box10.md §3, Theorem PH proof, l. 69-72 at e251d147, «no valuation changes (every play that met x still meets
  x with the same path set)»). Standing premise of ONE-PLAYER (a), named by F1/F7 (disclosure, not a widening; both referees'
  optional clause "(and SPEC S1 conformance, as R57 (b))", REFEREE l. 23 and §5 l. 78, REFEREE-2 §C l. 21 and C.6 l. 112): (i) the
  code's match to SPEC, RESULTS R15 limit (ii) = G-N5T-1 (DATA); (ii) «that S1's procedure realises an optimal σ̄ is VJ00 §6 plus SPEC
  conformance, and the code's match to SPEC is DATA (R15 G-N5T-1)» (RESULTS R57 (b), l. 2915-2916 at e251d147 and at 3d8b357d). F7:
  «It is NOT the VJ00 Lemma 5.8 / G-N5T-3 premise; SF-RED does not use output correctness.»
  (a) Lemma SF-TERM (§2, l. 77): "Every run of N5-SF stops, after I ≤ (#σ − 1) + (#τ − 1) iterations, at a state with Iσ = Iτ = ∅, and
      outputs S5's output." (Each σ-change is Switch_J(σ), ∅ ≠ J ⊆ Iσ, one edge per vertex (S4a′'s arena; S4a «Else σ_new = σ», F9;
      S4c's Even branch needs Iσ ≠ ∅); R15 (c): every such change goes strictly up in the strict partial order ≺, on G for σ and on G^d
      for τ, so no σ and no τ recurs; S4c makes every iteration change σ or τ; the loop exits only at S5.) «The CORRECTNESS of that
      output is not claimed here» (l. 88). Cells: REFEREE "SIGNED" (l. 17), REFEREE-2 "SIGNED" (l. 37).
  (b) Lemma DECOUPLE (§2, l. 89-90): "σ^(j+1) = F(σ^(j)) for every j < p, and Iσ^(p) = ∅. So the distinct-σ sequence is σ_0, F(σ_0),
      F(F(σ_0)), …, up to the first strategy with no improving edge, and it does not depend on τ_0. The mirror holds for τ with F^d and
      τ_0." (Iσ, Ξσ, σ̄(σ) are functions of σ (R15 (d), S1 deterministic); if A(σ) ≠ σ, S4c does not fire and σ := F(σ); if A(σ) = σ,
      σ changes only by S4c's Even branch, which by FIX 3 sets F(σ); τ decides WHEN σ stalls, not to what it moves.) Cells: REFEREE
      "SIGNED" (l. 18), REFEREE-2 "SIGNED" (l. 38).
  (c) Lemma ONE-PLAYER (§3, l. 102-104), with F7 (premise) and F10: "Let σ be an Even strategy with Iσ ≠ ∅, σ̄ := σ̄(σ), and G_σ̄ as in
      §0. Then: (a) the valuation of σ in G_σ̄ (SPEC S1 on G_σ̄) equals Ξσ, and the improving set of σ in G_σ̄ equals Iσ; (b) F(σ) equals
      N5's iteration (SPEC S4a + S4c) on G_σ̄ from (σ, τ := σ̄), restricted to σ." F10: «"The same arena H" means the same graph: the same
      vertex ids, owners and priorities, and the same successor lists in increasing index order, which S1's procedure uses». The τ side
      (used by SF-RED (b)'s mirror), F2: «Ω + 2 keeps every rank, every parity and every successor list, so S1's output is the same. …
      So the mirror of ONE-PLAYER (b) holds verbatim.» Cells: REFEREE "SIGNED (with the standing S1-conformance premise named, SF-N1)"
      (l. 19); REFEREE-2 "SIGNED (the τ-side mirror needs one line: N-SF-2)" (l. 39). F2 checked by both: REFEREE-2 §C C.3 (l. 69)
      "Correct; matches my OPb check"; REFEREE §C P2 (l. 33) "Correct" ("dual of dual adds 2 to every priority and swaps owners back").
  (d) Theorem SF-RED (a) (§3, l. 111), with F3 and F8: "Every stretch [a, b] has b − a ≤ n + m, and at most n − 1 of its transitions
      change Ξ." F3: «"these b − a transitions lie in one λ-phase of that run" is to be read as: they are a PREFIX of a λ-phase of N5's
      run on G_σ̄ started at (σ^(a), σ̄). … R17 (c) bounds the whole λ-phase, hence the prefix. The bound b − a ≤ n + m is unchanged.»
      F8: the S4c step «switches each such own-cycle-node x to an Ω-best improving successor (the Remark after Theorem PH), so it is a
      step of that kind and changes no valuation». (DECOUPLE and ONE-PLAYER (b): σ^(a..b) are consecutive N5 states on G_σ̄; R17 (e):
      S4a steps are switch-best, an S4c step leaves no improving edge, so it is the last transition of [a, b]; R17 (c): < n + m′ ≤ n + m
      switch-best steps in a λ-phase, ≤ n − 1 value-changing.) Cells: REFEREE "SIGNED (the S4c-step-is-flat link reads R17 (e) through
      R17's Theorem PH proof, SF-N2)" (l. 20); REFEREE-2 "SIGNED" (l. 40); REFEREE-2 §C C.1 (l. 18): "SIGNED by both, with the citation
      of C.2" (C.2 l. 27-35: the second clause "needs the S4c step on G_σ̄ to change no valuation"; "The first clause (b − a ≤ n + m)
      and (b), (c) do not depend on it"); discharged by F8 (REFEREE-2 C.5 l. 95; REFEREE §3 addendum l. 66).
  (e) Theorem SF-RED (b) (§3, l. 112-113): "#σ − 1 < (n + m + 1)(1 + LAM_σ + SBC_σ), LAM_σ ≤ n(n − 1); the mirror for τ. Hence
      I < (n + m + 1)(2(n² − n + 1) + SBC)." (At most LAM_σ + SBC_σ stretch boundaries, so S ≤ 1 + LAM_σ + SBC_σ stretches and
      #σ − 1 = Σ (b − a) + (S − 1) < S(n + m + 1); LAM_σ from R15 (a) on each Switch_J, the cycle node's reward compared first, p′
      injective (F13: proved in place, R47 deliberately not cited); G^d has the same n and m; then SF-TERM.) Cells: REFEREE "SIGNED"
      (l. 21), REFEREE-2 "SIGNED" (l. 41).
  (f) Theorem SF-RED (c) (§3, l. 114-115): "Conversely SBC_σ ≤ #σ − 1 and SBC_τ ≤ #τ − 1, so SBC ≤ 2I. N5-SF makes polynomially many
      iterations on a class of games iff SBC is polynomially bounded there." F6 (first sentence): the «iff» «quantifies over all runs
      on the class, i.e. every game of the class and every start pair». Cells: REFEREE "SIGNED" (l. 22), REFEREE-2 "SIGNED" (l. 42);
      REFEREE-2 §2.5 (l. 120): "The equivalence follows, read over all runs of the class."
  The proposed RESULTS line: REFEREE "MATCHES the signed content and claims no more (§5); one optional clause (SF-N1)" (l. 23);
  REFEREE-2 "MATCHES the signed content (§2.6)" (l. 43); REFEREE-2 §C C.1 (l. 21): "MATCHES, per both. I support the optional clause:
  it names the premise F1 now states". The optional clause is carried above as a premise disclosure, not in the title.
- Not signed: §3 Remarks 1-2 (READING, "not to sign", packet table l. 27); Remark 2's phrase «nothing about σ̄ beyond its being a
  function of σ» is replaced by F1 and F7 («F1 and F7 together replace that phrase of Remark 2»; REFEREE §3 addendum l. 65 "Remark 2
  was not signed, so its replacement touches no signed item"). Remark 1's sharper b − a < n + m: READING (F5: «Remark 1 stays a
  remark»). §4: DATA and the pinned check (DATA, not to sign). §5: CONJECTURE SF-POLY (SBC polynomially bounded on every game) OPEN;
  with SF-RED (c) it is EQUIVALENT to N5-SF being polynomial («it is not an easier statement; it only names where the cost sits»).
  Output correctness: S5 on the final σ, as in N5. The packet (l. 88, l. 170) rests it on VJ00 Lemma 5.8 (RESULTS R15 limit (iii),
  G-N5T-3). Since RESULTS R57 (b) Lemma OUT-G (every game, every σ with Iσ = ∅; standing premise 1E-N3), N5's output correctness rests on
  OUT-G, and the output half of G-N5T-3 is removed (R57 Not signed; GAPS G-N5-TIME). Neither the packet nor either referee applies OUT-G to
  N5-SF's stop, so output correctness is not claimed here. Gauntlet status (TARGET.md §5): «N5-SF has passed no gauntlet step in full» (packet l. 172;
  docs/new/N5-SF-gauntlet-box55.md, not reviewed). The packet's "Consequence (timing only)" (l. 98-99) is not a row of either verdict
  table: its "#σ only on σ_0 and #τ only on τ_0" is DECOUPLE's content, and "I depends on both starts" is not claimed. F12's sharper
  "n − 1" stretch bound: «a sharper statement (n − 1) would be a new claim for both referees» (not made).
- Referee strengthening (NOT part of this entry; remarks of one or both referees outside the verdict cells, or optional wording):
  (0) F6's per-start-rule form of SF-RED (c): «(b) and (c) are inequalities per run, so the same equivalence also holds for any fixed
  start rule (e.g. SPEC S3)». REFEREE-2 N-SF-6 (§4 l. 182-183) and §C C.3 (l. 73): "a direct reading of the signed per-run inequalities,
  not a new claim"; REFEREE §C P7 (l. 38): "Correct: (b), (c) are per-run inequalities, so the equivalence holds over ANY set of runs
  (all starts, or S3 starts only). It adds an immediate consequence, it widens no signed statement". Not in either verdict cell.
  (i) REFEREE §3 (l. 49), ONE-PLAYER (a): "It does NOT need σ̄(σ) to be a one-step minimiser (the FIX 2 / Lemma DF trap is not
  touched)." (one referee). (ii) REFEREE §4 (c) (l. 68): the equivalence uses "m ≤ n², self-loops included". (iii) REFEREE-2 §2.4
  (l. 102-103), a second derivation that an in-stretch S4c step is last: "Iσ^(j+1) in G equals its set in G_σ̄, which is ∅ (ONE-PLAYER
  (a)). Hence j + 1 = p = b". (iv) REFEREE-2 §2.5 (l. 116-117): "The inequality stays strict even when #σ = 1." (v) REFEREE-2 §1
  (l. 53-54): R15 (c)'s "every non-empty switch of improvements goes strictly up in ≺" "is for VJ00's unambiguous switches, which is what
  SF-TERM (i) supplies". (vi) REFEREE §4 (b) (l. 65) and SF-N7: the LAM argument "is R47 Lemma Φ (a)'s argument, re-proved here from
  R15 (a)"; REFEREE-2 §C (l. 49) "record only". (vii) REFEREE §C P4 (l. 35) and REFEREE §4 (l. 57-58): "the phase starts at a, since the
  G_σ̄ run starts there" — the same point as F3, "made from the other end" (REFEREE-2 §C l. 54-55).
- Honest limits: (i) SF-RED is a REDUCTION for a VARIANT (N5-SF) of N5: it bounds N5-SF's iterations by a polynomial times SBC and SBC by
  2I; SBC is NOT bounded here (CONJECTURE SF-POLY OPEN). DATA only (packet §5, not refereed): «SBC ≤ 1.17n on the library, ≤ 16 on the
  M1 families; on PGSolver's switchbestexp N = 1..16 SBC = 1, 4, 11, 26, 49, 56, 60, 75, 92, 97, …, 138, 179, 232 (0.57n at N = 16)».
  (ii) It says nothing about N5 itself: N5-SF is a different algorithm (REFEREE-2 X_ORBN5, DATA: on 2,787 of 14,220 runs N5's
  distinct-σ sequence differs from N5-SF's; REFEREE MUT 1, N5's own S4a in place of S4a′, bites: ORB 113, TAU_E 119, ONEPb 120 on
  1,000 runs). No statement here transfers to N5's run; G-N5-TIME untouched. (iii) I counts iterations, not bit operations; no
  running-time bound. (iv) Output correctness: not claimed (Not signed;
  RESULTS R57 (b) OUT-G covers S5 at every σ with Iσ = ∅, its application to N5-SF unsigned) (DATA: REFEREE-2 WIN, N5-SF's final regions equal N5's on all
  14,220 runs; packet: WIN PASS and OPT PASS on box 54's runs). (v) Sharpness (DATA): no stretch exceeds n − 1 transitions in either
  referee's data (REFEREE max 47 families / 44 library, MUT 2 does not bite; REFEREE-2 X_SEGn1: 0 on lib41, alt_all, fam, hard, max
  69 / 59 / 56 / 52); the lane's max is 101 at switchbestexp_16, n = 410 (F5, F12; not re-run by REFEREE-2, C.3 l. 72). The signed
  bound n + m stays. (vi) Not M3, not a gauntlet pass, not a TARGET.md claim.
- Data (DATA, not proof): pinned (packet §4; experiments/new/box55/pcheck.py, sha1 f4d741c2271b09fed3783d808af081bfd618860a, imports
  box54/n5sf.py, sha1 1ea3bdc79d1ee0f4110c9a1b61e37f854210ad4f, and box21/n5x.py, sha1 bbc7d4c9277011e8ddff7684a6f0e8b90192191a;
  box55/ntcheck.py sha1 7d60b5dde930c72fec7125e2fb170cf9880ad709; all four equal at 95a7a581 and 3d8b357d; check.sh block "Box 55";
  instances switchbestexp_2.pg b3d5bc293d1b76ce5c7ae8dadc4e9b0b51294484 and n3cov_lean.pg bcf8dbf64cba48123dc7da849b179793257e13e1,
  pinned there). Re-run for this draft on trunk 3d8b357d (experiments/new, `python3 -I`, outputs to a scratch file, exit codes read):
  n3all_maxph_0 «ROW E_ n 3 m 6 values 3 orbit 3 SBC 1 LAM 1 SEG 2 SEGMAX 1», CHECK PASS; switchbestexp_2 «ROW E_ n 60 m 130 values
  59 orbit 59 SBC 4 LAM 0 SEG 5 SEGMAX 18», CHECK PASS; n3cov_lean «ROW E_ n 48 m 128 values 29 orbit 29 SBC 11 LAM 4 SEG 12 SEGMAX 6»
  and «ROW O_ n 48 m 128 values 6 orbit 6 SBC 3 LAM 5 SEG 6 SEGMAX 0», CHECK PASS; MUT=1 on switchbestexp_2 «E_ORB_V», CHECK FAIL (exit
  1); ntcheck NT PASS; quote checks as in Object. All exactly as packet §4 and check.sh. Start convention (F4): unlisted vertices take
  their S3 start successor; n3cov_lean.start's SIGMA0 47:18 sits on an Odd vertex and has no effect (F11). Packet corpora (§4, lane
  DATA): alt_all 413 / 413 CHECK PASS, sicorpus 276 of 277 entries (1 not run: no TAU0 line), box 54 families 20 / 20, hard families
  (switchbestexp N = 1..8, switchallexp N = 1..6, Oink M1 generators) 73 / 73; 0 violations, 0 timeouts. REFEREE (successor 18; own
  scratch/sf_probe.py, sha1 24a38b5b…, its own N5-SF on rl_engine, no lane code; pinned re-runs from a clean worktree at 95a7a581,
  exact): 4,482 runs (random rand_ck n 5-14 4,000; library n ≤ 48 378; box 54 families + hard families + pins n ≤ 200 104), 12,826
  iterations, CONF 695,462 vertex checks (Ξσ = play value of (σ, σ̄(σ))), ONEP 15,614, 18,434 stretches, 353 in-stretch S4c steps
  (all Ξ-flat and last), max SBC 60, max stretch 47, 0 violations; skipped 63 library games with n > 48 and 6 hard-family games with
  n > 200; two given starts rejected by its parser (S3 only there). REFEREE-2 (successor 20; own R2-N5-SF/sf_check.py on si.py and its
  lane's dual_check.Runner; lane tools only run as check.sh's commands from a worktree at 95a7a581, never imported): 14,220 runs,
  34,162 iterations (random n 4-14 12,000, n 15-30 1,200, lib41 820, alt_all 93, box 54 families 34, hard 73), OP checks 28,052 /
  17,111 (Even / Odd), fallbacks 610 / 642, 0 violations of TERM, ORB, ORB2, OPa, OPb, SEG, FBLAST, BND, WIN; its own N5-SF reproduces
  the lane's SBC / LAM / stretch count / max stretch on all three pins, both sides, under the S3 fill (first-successor fill gives E SBC
  12 and 13 stretches on n3cov_lean, N-SF-4); max SBC 75 / 16 (E / O, hard), max LAM 28, max I 489; strict quote check 18/18, SHIFT=1
  control 0/18; at C.5 the fixes file's 6 quotes 6/6. No signed statement uses any count.
- Signatures: REFEREE docs/referee/R-N5-SF.md (report 500b51d7a78853710c88d4d49dd2603f923d815c, 2026-10-29T16:20:04Z, sha1
  d2311efa0e7fc1218f452c9018ccc08d1cd48fdf, 127 lines, = trunk 3d8b357d; successor 18); §C docs/referee/R-N5-SF-C.md (6bbf0aed,
  2026-10-29T16:37:34Z, sha1 827f81e3c56fdd7f1b6779e238f53fdd94fa137d there, 57 lines; §3 addendum 530e09c9, 2026-10-29T17:12:39Z,
  append-only (`git diff 6bbf0aed 530e09c9`: 16 added, 0 removed), sha1 247f82c56d68180a73d1dd188fa70bc381d7f28f, 73 lines, = trunk):
  §0 CHECKED; SF-TERM, DECOUPLE, ONE-PLAYER (a), (b), SF-RED (a), (b), (c) SIGNED; RESULTS line MATCHES (optional clause SF-N1); notes
  SF-N1..N7; "No gap. Nothing FALSE." REFEREE-2 docs/referee-2/R2-N5-SF.md (report 3ae22a6d8c0498326e09cd811b8ce6e12f4c8734,
  2026-10-29T16:03:33Z, sha1 031834ba91cb794e174d2b91786da5f94aacf63a, 193 lines, = trunk; successor 20); §C
  docs/referee-2/R2-N5-SF-C.md (42022bca, 2026-10-29T16:34:33Z, sha1 60a850b760e75e61a9c8640250b06d90158727ef there, 97 lines; C.5
  894a1971, 2026-10-29T17:16:25Z, sha1 1e20eb1d0308e76bab627893f2dbd2f28a4b737f, 112 lines, = trunk; `git diff 42022bca 894a1971`: 18
  added, 3 removed: the placeholder "## C.5 F7-F13" / "Pending (the Lead will send the SHA)." and the NEEDS line were replaced, no
  verdict line changed): §0 SIGNED; SF-TERM, DECOUPLE, ONE-PLAYER (a), (b), SF-RED (a), (b), (c) SIGNED; RESULTS line MATCHES; notes
  N-SF-1..6; "No gap. No item FALSE." INDEPENDENCE: REFEREE l. 7: "no REFEREE-2 SF file opened (none on my tree)"; REFEREE §C l. 3-4:
  REFEREE-2's report "read only after the Lead's word (my report pushed first)". REFEREE-2 l. 17-18: name count of SF files on
  origin/claude/referee 0 at 15:55:17Z and 16:03:20Z, "No docs/referee/ file opened"; REFEREE-2 §C l. 5-6: REFEREE's report "First
  opened 16:31Z, after my report was pushed (3ae22a6d, 16:09Z)" (commit time of 3ae22a6d: 16:03:33Z). No review imported lane code.
  §C (both): verdicts identical (REFEREE §C l. 22: "VERDICTS IDENTICAL. Nothing FALSE on either side. JOINT GAP MAP: EMPTY. E-ITEMS:
  NONE"; REFEREE-2 §C l. 24: "Joint gap map: EMPTY. No gap, nothing FALSE. Every to-sign item is SIGNED by both referees."). E-item
  classes differ: REFEREE-2 classes SF-N2 (citation) and SF-N3 (quote) as E (C.2), discharged by F8 and F9 (C.5 l. 95-96, l. 103-104:
  "With F1-F13, the P-N5-SF joint gap map stays EMPTY and has no open E-item"); REFEREE classes them as notes (§3 addendum l. 66: "I
  classed SF-N2 as a note: the step was already right, now cited"). Fixes accepted by both: F1-F6 (REFEREE §C l. 48 "CONFIRMED for
  F1-F6"; REFEREE-2 C.3 l. 75 "F1-F6 are ACCEPTED"), F7-F13 (REFEREE §3 addendum l. 72: "none widens or changes a signed statement";
  REFEREE-2 C.5 l. 102 "F7-F13 ACCEPTED"). REFEREE §3 addendum l. 73: "Nothing open on P-N5-SF; SF-POLY OPEN, G-N5-TIME untouched."
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (a reduction, for the variant N5-SF of N5, of N5-SF's iteration count to the
  best-reply change count SBC, which is not bounded; no running-time bound, no algorithm claim; N5-SF has passed no gauntlet step in
  full). GAPS G-N5-TIME: open, untouched.

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
