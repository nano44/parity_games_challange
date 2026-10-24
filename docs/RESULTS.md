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
