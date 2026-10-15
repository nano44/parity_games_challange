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
  docs/referee-2/R2-L4.md §7 (referee-2 d76c9e1). CHECKER: docs/checker/C1-report.md.
- Gaps (union, see R2-L4.md §7): CDFJLP Thm 5.1 (arXiv 1807.10546) used as a black box (G-L4-1); first referee G1-G6.
- Status: supporting lemma, not claimed as M3 (Lead reading L7). Credit: conversion remark Parys-Wiacek 2305.00308 p.2;
  Claim R by L-LIT; sharpening by REFEREE; write-up L-STRUCT.

### R2 [refereed-only] T-A1: exact characterisation of psolB's completely-solved games (2026-10-15) — M3 (L9), CHECKER re-check pending
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
  nothing machine-checked beyond the data searches. Side finding: HKP Thm 4's proof defines an unsound minimal-rank
  strategy (REFEREE-2 counterexample docs/referee-2/R2-TA1/hkp_thm4_strategy.py; repair: witness successor); theorem unaffected.
- Status: M3 "a tighter analysis of a known algorithm" (Lead reading L9). Novelty: L-LIT T8 (docs/lit/T8-TA1.md): Ah-Fat-Huth 2016
  name 2-player completeness classes as open. Also explains DE1 (2511.03752): its errors lie where no PA** piece can go first.


## Dead ends (kept; each with the exact obstruction or counterexample and the instance that killed it)
- DE1 (2026-10-14): arXiv 2511.03752 v1 (van der Heijden), claimed O(n²(n+m)) algorithm. BROKEN: wrong regions on 4-vertex games
  CE1 (l-comp 19b5ce2, experiments/m2/counterexamples/ce1_4v.pg) and cex1 (referee 936d47c, docs/referee/scratch/cex1-*.pg).
  Obstruction: Theorem 1/2 (A(G,d) is a dominion) is false; U^k refinement removes only vertices where the opponent can force A'.
  Details: docs/decisions/M2-arxiv-2511.03752.md.
- DE2 (2026-10-14): L-STRUCT target T1, w^X(n,d) ≥ s^X(n,d−2) for deterministic weak separators (docs/struct/S2-lower-bound-statement.md).
  REFUTED at n=2, d=10 in E, S, V: a 4-state weak (2,10)-separator (l-comp 3e44d2c, experiments/sat-hard/results/weak_E_n2_d10_k4.json)
  while s(2,8) = 5 (strong k=4 UNSAT, LRAT-verified, two solvers). Checked by REFEREE with independent tools (referee 92846bf).
  Obstruction: strong separators grow as s(2,2h) = h+1, weak ones stay at 4 for d = 8, 10. (Not algorithmic: 2-vertex games have d ≤ 3.)
