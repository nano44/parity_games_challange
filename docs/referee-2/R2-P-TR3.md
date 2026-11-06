# R2-P-TR3: second-referee report on premise packet P-TR3 (L-COMP successor 9, box 27): T^R(3) ≤ 8, so T^R(3) = 8
REFEREE-2 successor 28 (Opus 5.5, D12/D20). Written 2026-11-06 02:38Z (date -u). Independent: docs/referee/
(including R-P-TR3.md) not read before this push. Asked by the Lead 01:55Z (its stamp).

## Object
- claude/l-comp d03d8370. experiments/comp/box27/P-TR3.md sha1 cab32c0ee6e694dbfc345e533ab267b2ced52ac5, 125 lines;
  P-TR3-line-L1.txt sha1 221c81eb20cb9f28aa41f07f6eb5d9af3879db92, 1 line. drup.c sha1 2d4b8eab8fe9e9035c396733bb400d9d6e7d2366
  (98 lines; = the packet's pin). cnf.py at d03d8370 sha1 f1f803ae…; the audited cnf.py fd882af1 (l-comp 557b045b / 6f19564f).
  All re-hashed: match.

## Verdicts
| item | verdict |
| --- | --- |
| STATEMENT P-TR3: T^R(3) ≤ 8 on 𝓛^R_3, every start (EXACT-SAT + CERT, machine) | **SIGN WITH GAPS** (Opus 5.5, D12): gaps TR3-G1, TR3-G2 below |
| T^R(3) ≥ 8 (witness out/R_d3_L8.json) | **SIGN** (Opus 5.5, D12) |
| SYM soundness, cube cover, E1-E3 (lane PROVED) | **SIGN** (Opus 5.5, D12) (encoding audited by my predecessor, R2-T3R-audit.md; reconfirmed below) |
| drup.c (forward RUP soundness, deletions, verdict, parsing) | audited: **SOUND** for the inputs used; robustness note D-1 |
| line L-1 | **does NOT match** as written; MATCHES after the exact word changes L-a to L-d (L-a, L-b required) |

### Gaps (each is a statement of what rests on the machine, not a hole in an argument)
- TR3-G1 (machine premise, as the packet's §4 «Limits» and §5 say): the 16 UNSATs are certified by RUP proofs checked with an own tool,
  not by drat-trim / LRAT or Lean. I audited drup.c by reading every line, fuzzed it (0 unsound verdicts) and re-checked one cube's
  proof (cube 10) with drup.c in both modes AND with my own independent checker r2rup.c: all VERIFIED. The other 15 proofs I did not
  regenerate (19.7 GB, ~4 h); for them the certificate is the lane's record (log/R_d3_L9_cert.txt) plus Glucose's determinism, which I
  reproduced on cube 10 (proof sha1 and size equal to the table row). Any citation must say «machine, CERT by an own RUP checker».
- TR3-G2 (encoding = R104; carried over): CERT certifies UNSAT of the DIMACS formulas, not that they encode R104 on 𝓛^R_3. That rests
  on the clause-by-clause audit of cnf.py fd882af1 (REFEREE-2 27, R2-T3R-audit.md §1-§3, 6 sections; pin test 0/414 vs an independent
  simulator), which I cite and did not redo; I re-checked here only that the certified DIMACS files are those of the audited cnf.py.

## (1) Audit of drup.c (every line read)
- Soundness argument (mine, independent of the header's): every clause ever in the DB is the input or a lemma that passed the check,
  hence implied by the input. In propagate() a literal is assigned only when its clause has C[1] = fl false (fl = −p, p on the trail),
  C[0] unassigned and every C[m], m ≥ 2, false — checked on the full clause at that moment (l. 31-36); a conflict is declared only when
  C[0] is also false (l. 35). So every implication and every conflict is a genuine unit / falsified clause of the DB, whatever the
  watch-list state; a watch bug could only LOSE propagations (reject, never accept). The watch invariant (c ∈ wl[l] ⇔ l ∈ {C[0], C[1]})
  is maintained by addclause (l. 51-52) and the move at l. 32, so C[1] = fl after the swap at l. 29 holds. ✓
- RUP step (l. 90-94): negate the lemma's literals on top of the top-level trail; a literal already true at top level counts as
  conflict (the lemma is implied by top-level units, which are implied by the DB); then propagate; undo to the base. Accept iff
  conflict. RAT is never accepted. Tautological lemmas are skipped (always implied). ✓
- Deletions (l. 56-61, 86): remove one live clause with the same literal SET (hash + exact set comparison, length equal). Top-level
  assignments stay: sound, each was implied when made. Deleted clauses are skipped and dropped from watch lists (l. 28) before any
  dereference of the freed pointer. Deleting can only shrink the DB. IGNDEL ignores them (also sound). ✓
- Verdict (l. 97): «s VERIFIED» iff topconf, which is set only by an input empty clause, a unit falsified at top level, an all-false
  clause at insertion, or a top-level propagation conflict — each a genuine refutation of DB ⊨-consequences. A proof that ends before
  a conflict gives «no refutation reached». The final «0» line of a proof cannot pass by itself (an empty lemma has no literal to
  negate and, with qhead = tn, propagate finds nothing). ✓
- Parsing (l. 63-71, 83): sound in the direction that matters: dropping input clauses (e.g. a truncated file; the «p cnf» counts are
  not checked) or merging two clauses into one longer clause only WEAKENS the input, so a refutation of the parsed input still refutes
  the true input. The only unsound parse would be one that SPLITS a clause or creates an empty clause.
  - D-1 (robustness, not soundness for these inputs): a malformed token (e.g. «1e5») makes readclause return 0 literals forever:
    drup.c then loops without reaching EOF (I observed a hang on a 1-line test file, not a false VERIFIED; the code path would add an
    empty input clause and set topconf if it ever returned). The 16 DIMACS files are produced by mkproof.py from integer lists; I
    checked cube 10's file strictly (regex `(-?[1-9]\d*( -?[1-9]\d*)* )?0` on every line: 0 bad lines; header 58,896 / 204,036 =
    the counts; max |literal| 58,896; 0 empty clauses; 69 units; max length 13). So D-1 does not bear on the result. Suggest the lane
    add a strict-format check (as r2rup.c does) before citing drup.c again.
- Fuzz (docs/referee-2/R2-P-TR3/fuzz_drup.py, seed 28, 3,000 random CNFs with n ≤ 9, both deletion modes; brute-force UNSAT as the
  oracle): Glucose proofs 3,840 runs, 3,840 VERIFIED (all on UNSAT formulas); random lemma sequences with random deletions 6,000 runs,
  3,837 VERIFIED; mutated Glucose proofs 902 runs, 4 VERIFIED; SAT formulas with any proof 2,160 runs, 0 VERIFIED. **UNSOUND 0**
  (every VERIFIED is on a brute-force UNSAT formula).

## (2) Regenerated proof, re-checked (cube 10: CUBE 2:0,3:1,4:0,5:1, the smallest proof in the table)
- mkproof.py 3 9 10 (lane tool, l-comp d03d8370, pysat 1.9.dev15 glucose4; env ISO, FREE0, P, W, KF, RUN2, XCUBE unset): UNSAT in
  162.1 s; DIMACS sha1 924ae0118e1b142a8d762d03d314d4a0c9be1af2 (= table); proof sha1 cae6998bd94b78005931ee2faff7eaffc3c122fc,
  851,461,087 bytes (= table: Glucose is deterministic here); 946,149 lines, 460,782 deletion lines.
- The audited cnf.py fd882af1 (extracted from 6f19564f) with my own DIMACS writer gives the same sha1 for cubes 0, 1, 10, 15
  (7e70b9e1…, 40412c7b…, 924ae011…, 44fb2796…; each 58,896 vars, 204,036 clauses). So the certified formulas are the audited
  encoding's, not only the later cnf.py's.
- Checks of that proof (my build of drup.c, gcc -O2, sha1 2d4b8eab):
  | run | result | lemmas | wall |
  | --- | --- | --- | --- |
  | drup.c, deletions applied | s VERIFIED (all 460,782 deletions matched) | 485,366 (= table) | 9 m 12 s |
  | drup.c, IGNDEL=1 | s VERIFIED | 485,366 | 14 m 47 s |
  | **r2rup.c (mine, independent; deletions ignored, strict parser, every unit/conflict re-verified on the whole clause)** | R2RUP VERIFIED | 485,366 | 15 m 49 s |
  | negative: proof truncated to its first 90 % of lines (851,534 lines) | s NOT VERIFIED: no refutation reached | 448,862 | 9 m 32 s |
  | mutation: lemma at line 400,001 with its first literal's sign flipped | s VERIFIED (the flipped lemma is still RUP; its later deletion finds no clause: 460,781 removed) | 485,366 | 10 m 32 s |
  | same mutated proof, r2rup.c | R2RUP VERIFIED: the two checkers agree that the flipped lemma is RUP, so this mutation is benign, not a checker miss | 485,366 | 14 m 0 s |
  | negative: unit lemma «59500 0» (a variable in no input clause) inserted before line 400,001 | **s NOT VERIFIED: lemma 219672 is not RUP** (the inserted lemma's index: 400,000 lines before it, 180,329 of them deletions) | 219,672 | 3 m 8 s |
- r2rup.c was itself fuzzed with the same harness (seed 29, 1,500 CNFs): Glucose proofs 1,874 / 1,874 VERIFIED, SAT formulas 0 / 1,126,
  UNSOUND 0; on a 1-line malformed file it stops with «R2RUP PARSE ERROR» (drup.c hangs, D-1).

## (3) Statement and definitions against RESULTS R110; witness; TARGET diff
- R110 (landed; RESULTS l. 11323): «𝓛^R_d ⊆ 𝓦_d the 2-wide degree-2 ladders in L-RED's R197 convention (movers 2l and 2l + 1 on level
  l, all of degree 2, no other movers, option k of a mover of level l ≥ 1 W-pointing to mover 2(l − 1) + k)», 𝓦_d «the genomes with
  levels 0, …, d − 1 whose level-0 movers are exactly two movers named 0 and 1», «T^R(d) the largest number of steps over 𝓛^R_d and all
  starts», all «In the IDEAL model of RESULTS R104 … on acyclic Ξ-graphs». The packet's class (quoted from P-IDEAL-FLIP §1 at 9effea1f,
  verbatim there: «N = 2d movers 0, …, 2d − 1, lev(x) = ⌊x/2⌋, every mover of degree 2, and wt(x, k) = 2(lev(x) − 1) + k …; Ξ-data,
  β's, gates and start arbitrary») and quantity («the largest T over 𝓛^R_d and all starts») are the SAME sets and the same maximum;
  the packet's §1 «Model» bullet restricts to acyclic Ξ-graphs; ISO not assumed. Statement exact. ✓ But the packet cites the lane file
  as the source and says «= RESULTS R110 once landed»; R110 has landed, so the premise route must now be R110 (L-a).
- The packet's R104 quote (§1) is a verbatim substring of RESULTS R104 (Python test). ✓
- Witness (lower bound): out/R_d3_L8.json, replayed by MY simulator (docs/referee-2/R2-P-IDEAL-KEYS/r2sim.py, written from R104's
  text, β-set comparison): well-formed (W-targets one level down, gates and ranks distinct, Ξ acyclic), in 𝓛^R_3 (lev 0,0,1,1,2,2,
  degree 2, wt(x, k) = 2(lev(x) − 1) + k), T = 8 from its start with all 9 states equal to the stored «states»; the maximum over all 64
  starts of this genome is 8. ✓
- Cover: SYM fixes s_0(0) = s_0(1) = 0; mkproof's CUBE fixes movers 2..5 to the bits of c (cube 10 = 2:0,3:1,4:0,5:1 ✓); 16 × 1 = all
  starts up to the level-0 relabelling, whose soundness (level-0 options carry no W-role in R110's wiring, which refers to MOVERS) I
  re-read and accept. Q(9) UNSAT ⇔ no run with ≥ 9 steps (the «each of the first L steps changes the state» encoding excludes both stop
  reasons; audited in R2-T3R-audit §1). ✓
- Sums: the per-cube table gives 11,353,990 lemmas and 19,694,959,174 bytes (= §4 totals); the CaDiCaL times sum to 4,946.2 s (= §3). ✓
- TARGET.md diff: a statement inside the IDEAL model; no game, no algorithm, no complexity class; not M3 / M4 / step 4. ✓

## Line L-1 (clause by clause)
- Parentheses balanced (0 at end, never negative); 2 «, 2 »; 0 «|»; one line. ✓
- «In the IDEAL model of RESULTS R104 (definition only, no theorem of R104 used)» ✓.
- «on 𝓛^R_3 (P-IDEAL-FLIP §1, claude/l-new 9effea1f, = RESULTS R110 once landed: the 2-wide degree-2 ladders with levels 0, 1, 2 in
  L-RED's R197 W-convention, all Ξ-data, β's, gates and starts, ISO not assumed)»: (i) the premise must be the landed R110; (ii) «all
  Ξ-data» without «acyclic» widens the claim to Ξ-cyclic genomes, which the encoding excludes (pi order) and the packet excludes (§1,
  §6). Required changes L-a, L-b.
- «T^R(3) ≤ 8, hence T^R(3) = 8 (2026-11-05)» ✓ (lower bound by the witness, named later in the line).
- Machine clause: CaDiCaL 1.9.5 UNSAT on 16 cubes, the cover «up to one sound relabelling (both level-0 movers start on option 0)», «each
  cube also refuted by a Glucose 4 DRUP proof accepted by the own forward RUP checker drup.c (no drat-trim; drup.c's correctness is a
  premise)», witness «replayed under two simulators»: ✓ (matches §3-§4). Optional L-c: pin drup.c (sha1 2d4b8eab…).
- DATA clause: «16 cube UNSATs and 16/16 VERIFIED proofs (11,353,990 lemmas) cover «T ≤ 8» only» ✓ (sum checked); «pinck.py's 0
  disagreements on 450 random genomes» (= 300 d 2 + 150 d 3, §3 ✓) «and on the 128 start runs of the 2 distinct length-8 genomes» (2 ×
  64 ✓) «cover only the agreement of the CNF with the simulator» ✓; «bf2.c's exhaustive maximum T = 4 on 𝓛^R_2 covers only the d 2
  cross-check» ✓. Every count names what it covers. ✓
- Source note «(P-TR3, experiments/comp/box27/P-TR3.md; L-COMP successor 9)»: the lane PROVED items E1-E3 and SYM are proved in P-TR3.md
  §2 AND ENCODING.md §1, §3 (P-TR3 §5: «PROVED (lane, written out above / in ENCODING.md)»); the source note must name ENCODING.md (L-d).
- Exact word changes:
  - L-a (required; premise route): «on 𝓛^R_3 (P-IDEAL-FLIP §1, claude/l-new 9effea1f, = RESULTS R110 once landed: the 2-wide degree-2
    ladders» → «on 𝓛^R_3 (RESULTS R110's definitions of 𝓛^R_d and T^R(d) only, no theorem of R110 used: the 2-wide degree-2 ladders».
  - L-b (required; scope): «all Ξ-data, β's, gates and starts, ISO not assumed)» → «all acyclic Ξ-data, β's, gates and starts, ISO not
    assumed)» (or insert «on acyclic Ξ-graphs,» after «(definition only, no theorem of R104 used)»).
  - L-c (optional): «the own forward RUP checker drup.c» → «the own forward RUP checker drup.c (sha1 2d4b8eab…)».
  - L-d (required by the source-note rule): «(P-TR3, experiments/comp/box27/P-TR3.md; L-COMP successor 9)» → «(P-TR3,
    experiments/comp/box27/P-TR3.md with experiments/comp/box27/ENCODING.md; L-COMP successor 9)».
- Packet text (not the line; a fixes note): §1 «(= RESULTS R110 once landed; P-IDEAL-FLIP is CHECKER C122s item.)» is stale;
  ENCODING.md l. 5 «no DRAT/LRAT certificate was produced or checked» is stale since §4 (it is not a DRAT/LRAT certificate, but a DRUP
  proof was produced and checked).

## Files
- docs/referee-2/R2-P-TR3/fuzz_drup.py (fuzz harness, used for drup.c and r2rup.c), r2rup.c (my RUP checker). Proof and CNF files
  (scratch, not committed: 851 MB). Re-run: python3 -I mkproof.py 3 9 10 DIR glucose4 (l-comp d03d8370 box27), then
  `drup DIR/d3_L9_c10.cnf DIR/d3_L9_c10.glucose4.proof` and `r2rup …` (gcc -O2).
