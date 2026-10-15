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
  at l-si 95d37d3) toward M4. KILLED by L-RED (l-red e1e9402, docs/red/R1-MSF.md): on gated_bland N (experiments/red/gens_red.py;
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
