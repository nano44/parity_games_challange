# P-TR3 fixes (append-only). The frozen packet experiments/comp/box27/P-TR3.md (l-comp d03d8370, sha1
# cab32c0ee6e694dbfc345e533ab267b2ced52ac5, 125 lines) is NOT edited; every correction is here.

## Entry 1 (2026-11-06, L-COMP successor 9; Lead 03:23Z fix round 1)
Sources: REFEREE 24, claude/referee 5a5b94cf, docs/referee/R-P-TR3.md (SIGN as machine-certified; REQUIRED TR-1, TR-L1, TR-L2;
optional TR-P1-P3, TR-L3); REFEREE-2 28, claude/referee-2 60e24158, docs/referee-2/R2-P-TR3.md (SIGN WITH GAPS TR3-G1/G2; line
changes L-a, L-b required, L-c optional, L-d; robustness note D-1; stale-text notes).

### F1 (REQUIRED TR-1, REFEREE-2 stale note): the definitions now come from RESULTS R110 (landed)
- Replaces §1's second bullet («Class and quantity (not landed terms; quoted from L-NEW's packet P-IDEAL-FLIP §1 …)» through
  «… (= RESULTS R110 once landed; P-IDEAL-FLIP is CHECKER C122's item.)»). New text: «Class and quantity: RESULTS R110's definitions
  only, no theorem of R110 used (docs/RESULTS.md, trunk claude/vibrant-johnson-nxvvxo 4b35e2b0, l. 11323), verbatim: «on acyclic
  Ξ-graphs, with 𝓦_d the genomes with levels 0, …, d − 1 whose level-0 movers are exactly two movers named 0 and 1, 𝓛^R_d ⊆ 𝓦_d the
  2-wide degree-2 ladders in L-RED's R197 convention (movers 2l and 2l + 1 on level l, all of degree 2, no other movers, option k of a
  mover of level l ≥ 1 W-pointing to mover 2(l − 1) + k), T^R(d) the largest number of steps over 𝓛^R_d and all starts (kept apart
  from R109's T*(d) over 𝓛_d; T^R(d) ≤ T*(d))».» The rest of the bullet («Here T = R104's L(G) from the given start, and «Ξ-data
  arbitrary» includes Ξ-targets at level-0 movers (ISO is NOT assumed).») stays, with «Ξ-data arbitrary» read as «acyclic Ξ-data
  arbitrary» (R110: «on acyclic Ξ-graphs»).
- The class is the same as the one P-TR3 quoted (P-IDEAL-FLIP §1): REFEREE 24 checked both texts (R-P-TR3 §4). Nothing in §2-§5 changes.

### F2 (optional TR-P3): §1 cross-reference
- §1 «With the witness of §5, T^R(3) = 8.» → «With the witness of §3, T^R(3) = 8.» (the witness is in §3).

### F3 (optional TR-P2): which cnf.py made which file
- §2 names cnf.py sha1 fd882af1… (l-comp 557b045b), the version that built the 16 CaDiCaL cube formulas. The Glucose 4 proofs of §4
  were made by mkproof.py importing the later cnf.py f1f803ae… (l-comp d03d8370; it adds only the env options XCUBE and RUN2, both
  unused here). The 16 d 3 cube DIMACS files built by the two versions are byte-identical (§3 sha1 table; checked by building all 16
  with both versions, 0 differences), and the §4 DIMACS sha1 column equals that table.

### F4 (optional TR-P3, REFEREE-2 stale note): status of drup.c and of the certificate
- §4 «Limits»: «drup.c is my own, unaudited tool» → «drup.c is my own tool, audited sound by REFEREE 24 (R-P-TR3 §1: line-by-line;
  13 negative / positive tests) and by REFEREE-2 28 (R2-P-TR3: audit and 12,902 fuzz runs, UNSOUND 0)»; «its correctness is a premise
  of CERT» stays.
- §5 «What remains trusted: (i) drup.c (own forward RUP checker, §4 limits)» gains: «shared with independent checkers on part of the
  cubes: REFEREE 24 regenerated the proofs of cubes 5, 9, 10 byte-identically and re-checked them with drup.c and its own ref_rup.c;
  REFEREE-2 28 regenerated cube 10 byte-identically and re-checked it». (Counts as on file in the two reports; the 13 other cubes rest
  on log/R_d3_L9_cert.txt plus Glucose's determinism.)
- ENCODING.md l. 5 «no DRAT/LRAT certificate was produced or checked» is stale: no DRAT/LRAT certificate exists, but since P-TR3 §4 a
  DRUP proof was produced for each of the 16 d 3 cubes and checked by drup.c. Read ENCODING.md l. 5 with that addition.

### F5 (optional TR-P1 / REFEREE-2 D-1): strict parsing, as a NEW file
- experiments/comp/box27/drup2.c (sha1 34ff0d8079b0143b5757e653c6d50364b333c49a): drup.c's checking logic unchanged, plus strict
  parsing (every token an integer or, in a proof, a leading «d»; otherwise «s PARSE ERROR», exit 2) and the «p cnf V C» header check
  (exactly C clauses; every |literal| ≤ V). drup.c (sha1 2d4b8eab…) stays the checker of the certified record; nothing in §4 changes.
- Tests: on the four d 2 files of §4 drup2.c gives the same verdicts as drup.c (L 5 proof VERIFIED, 5,730 lemmas; SAT formula,
  truncated proof, holed proof NOT VERIFIED); a formula with the token «1e5» stops with «s PARSE ERROR: token '1e5'» (exit 2; drup.c
  hangs there, D-1); a header with too many clauses and a literal above V each stop with «s PARSE ERROR».

### F6: line L-2 (experiments/comp/box27/P-TR3-line-L2.txt)
- L-2 = L-1 with exactly these changes (L-1: sha1 221c81eb20cb9f28aa41f07f6eb5d9af3879db92):
  1. (L-a, TR-L1) «on 𝓛^R_3 (P-IDEAL-FLIP §1, claude/l-new 9effea1f, = RESULTS R110 once landed: the 2-wide degree-2 ladders» → «on
     𝓛^R_3 (RESULTS R110's definitions of 𝓛^R_d and T^R(d) only, no theorem of R110 used: the 2-wide degree-2 ladders».
  2. (L-b, TR-L1) «all Ξ-data, β's, gates and starts, ISO not assumed)» → «all acyclic Ξ-data, β's, gates and starts, ISO not
     assumed; T^R(d) the largest number of steps over 𝓛^R_d and all starts)» (adds «acyclic» and R110's definition of T^R(d)).
  3. (L-c, TR-L3) «the own forward RUP checker drup.c (no drat-trim; drup.c's correctness is a premise)» → «the own forward RUP
     checker drup.c (sha1 2d4b8eab…; no drat-trim; drup.c audited sound by REFEREE and REFEREE-2, its correctness still a premise;
     cube proofs regenerated byte-identically and re-checked independently: REFEREE 3 cubes, REFEREE-2 1 cube)».
  4. (L-d, TR-L2) «(P-TR3, experiments/comp/box27/P-TR3.md; L-COMP successor 9)» → «(P-TR3, experiments/comp/box27/P-TR3.md with its
     fixes entry 1, experiments/comp/box27/P-TR3-fixes.md, and experiments/comp/box27/ENCODING.md; L-COMP successor 9)».
- Word diff (git diff --no-index --word-diff=plain L-1 L-2; [-old-]{+new+}):
  - [-(P-IDEAL-FLIP §1, claude/l-new 9effea1f, = RESULTS-]{+(RESULTS R110's definitions of 𝓛^R_d and T^R(d) only, no theorem of+}
  - [-once landed:-]{+used:+}
  - {+acyclic+}
  - [-assumed):-]{+assumed; T^R(d) the largest number of steps over 𝓛^R_d and all starts):+}
  - [-(no-]{+(sha1 2d4b8eab…; no+}
  - [-drup.c's-]{+drup.c audited sound by REFEREE and REFEREE-2, its+}
  - [-is-]{+still+}
  - [-premise),-]{+premise; cube proofs regenerated byte-identically and re-checked independently: REFEREE 3 cubes, REFEREE-2 1 cube),+}
  - [-experiments/comp/box27/P-TR3.md;-]{+experiments/comp/box27/P-TR3.md with its fixes entry 1, experiments/comp/box27/P-TR3-fixes.md, and experiments/comp/box27/ENCODING.md;+}
- Shape: one line; 13 «(» / 13 «)»; 0 «|»; one « — »; «2026» once. The tag «[lane: EXACT-SAT + CERT]» is a lane label; the Lead sets
  the RESULTS tag (REFEREE TR-L1). L-2 sha1 11cd9acc14147fb7a3820e9a16c9cee15875e611.
- Not taken: none of the required or optional items was declined. REFEREE's count «3 cubes re-checked» and REFEREE-2's «1» are the
  counts on file at 5a5b94cf / 60e24158; no other re-check count is used.

## Entry 2 (2026-11-06, L-COMP successor 9; Lead 07:38Z; CHECKER C123 E-1, claude/checker 96b7f8a1, docs/checker/C123.md §5)
### F7: line L-3 (experiments/comp/box27/P-TR3-line-L3.txt)
- L-3 = L-2 (sha1 11cd9acc14147fb7a3820e9a16c9cee15875e611) with exactly one deletion: the leading «P-TR3 [lane: EXACT-SAT + CERT] »
  (31 characters, occurring once, at the start; C123 §5: the RESULTS title must not carry the lane label). The prefix was copied by
  script from C123 §5's text (the «…» after «the leading» in the L-3 bullet) and the result checked: L-2 starts with it, it occurs
  once, and L-3 == L-2 minus that prefix (Python string test: True). Nothing else changes.
- Word diff (git diff --no-index --word-diff=plain L-2 L-3), verbatim start of its only line: «[-P-TR3 [lane: EXACT-SAT + CERT]-]In the
  IDEAL model of RESULTS R104 …» (one deletion; no insertion).
- L-3: sha1 d87bb3f062115ccf13164465395ef0187ccda7cf (with its final newline), 1,682 bytes, 13 «(» / 13 «)», 0 «|», one « — »,
  «2026» once. = the expected sha1 given by the Lead (07:38Z) / C123 §5.
- Not taken (Lead 07:38Z): C123's optional «REFEREE all 16 cubes» change; L-3 keeps the on-file counts «REFEREE 3 cubes, REFEREE-2
  1 cube».
