# R-P-TR3: REFEREE report on P-TR3 (L-COMP successor 9, box 27): T^R(3) = 8
REFEREE successor 24 (Opus 5.5, D15), 2026-11-06 (date -u in the commit). Independent: I did not open or list docs/referee-2/ on this
packet before this report was pushed. Premise material of my own: docs/referee/R-T3R-audit.md (encoding audit of cnf.py at 6f19564f,
§1-§5, §C, add. 1-2).
- Object: claude/l-comp d03d8370 (an ancestor of origin/claude/l-comp), read from a detached worktree. Re-measured:
  - experiments/comp/box27/P-TR3.md: sha1 cab32c0ee6e694dbfc345e533ab267b2ced52ac5, 125 lines;
  - experiments/comp/box27/P-TR3-line-L1.txt: sha1 221c81eb20cb9f28aa41f07f6eb5d9af3879db92, 1 line, 1,357 bytes;
  - drup.c: sha1 2d4b8eab8fe9e9035c396733bb400d9d6e7d2366, 98 lines (equal at l-comp 07cec839, as the packet says);
  - cnf.py: sha1 f1f803ae… at d03d8370, NOT the fd882af1… of the packet's §2. The diff from 6f19564f adds only FREE0 / RUN2 / XCUBE
    paths, all off for this query. The d = 3, T ≥ 9 cube CNFs are byte-identical (§3).

## 0. Verdicts
| item | verdict |
| --- | --- |
| STATEMENT P-TR3: T^R(3) ≤ 8, hence T^R(3) = 8 | SIGN, as a machine-certified statement (scope in §5); gaps listed below |
| drup.c (forward RUP checker) | SOUND (line-by-line audit, §1) |
| CERT (16/16 Glucose 4 DRUP proofs VERIFIED) | CONFIRMED by re-generation and two checkers on 3 cubes; the other 13 rest on the lane's records (gap TR-G1) |
| encoding (cnf.py → R104 / R110) | FAITHFUL (R-T3R-audit; T3-G2 closed by R110) |
| packet text | REQUIRED TR-1 (cite R110, which has landed); optional TR-P1-P3 |
| line L-1 | NOT YET: REQUIRED TR-L1, TR-L2 |

- Gaps (listed):
  - TR-G1 (scope of my re-check). I regenerated and checked 3 of the 16 proofs (cubes 5, 9, 10) with two checkers. The other 13 CERT
    rows rest on the lane's records (log/R_d3_L9_cert.txt: cnf sha1, proof sha1, size, lemma count, VERIFIED), produced by the drup.c
    I audited. The proofs were deleted and are not committed; they are regenerable and deterministic (§3).
  - TR-G2 (trusted base). Two things stay trusted. (i) pysat's Glucose 4 only produces the proofs; it is not trusted, since a wrong
    proof is rejected. (ii) The checkers: drup.c, audited here, and my ref_rup.c, an independent second implementation. Both are
    unverified C, not a formally verified checker such as cake_lpr. No drat-trim, for the reason in R-T3R-audit §4.
  - The encoding's faithfulness to R104 is an audit (R-T3R-audit; REFEREE-2 R2-T3R-audit), not a proof. CERT certifies UNSAT of the
    16 recorded DIMACS formulas only.

## 1. drup.c, line by line (l-comp d03d8370; I compiled it myself: gcc 13.3 -O2)
- Parsing (readclause, l. 63-71).
  - A line starting with «c» or «p» is skipped whole. So the DIMACS header «p cnf V C» is NOT checked: no clause count, no variable
    range. Variables are grown on demand (grow).
  - «d» marks a deletion. Literals are read with fscanf up to 0.
  - Soundness: this is not a soundness hole. Under-reading the input (fewer clauses, or two clauses read as one weaker clause) can
    only make the formula WEAKER. Refuting a weaker formula still refutes the real one. Over-reading cannot happen: the file is the
    audited DIMACS.
  - The DIMACS identity is checked OUTSIDE drup.c: mkproof.py prints the sha1, and the cert records carry it. I re-checked the
    identity for my 3 cubes (§3) and the 16-row tables against my own list (§3).
  - Cosmetic: the «vars 59059» drup prints is its allocation size (v + 1000), not the 58,896 variables.
- Normalisation (norm, l. 72-73). Duplicate literals are removed; a tautology returns −1 and is skipped (an input tautology is
  dropped: sound; a lemma tautology is not added: sound).
- Clause store and top level (addclause, l. 40-55).
  - n = 0 sets topconf. A unit is assigned and propagated, or gives a conflict if already false.
  - Otherwise the two watches go on non-false literals when possible. «sat» clauses are watched and skipped. With nf = 0 → topconf;
    with nf = 1 → assign and propagate.
  - Every top-level assignment is a unit consequence of the DB, so it is implied by the input.
- Propagation (propagate, l. 26-38). A standard two-watched-literal scheme:
  - the false watch is kept at position 1; a true other watch keeps the clause; otherwise a non-false replacement is sought;
  - otherwise the clause is unit or conflicting;
  - deleted clauses are skipped and dropped from the watch list lazily.
  - I checked the swap and re-watch logic and the conflict exit (the remaining watches are copied back, and wn is updated).
- RUP check (l. 89-95).
  - Under the current top-level state: «lit true» is an immediate acceptance (that literal is implied, so the lemma is too).
    Otherwise the negation of each unassigned literal is assigned and propagated, and a conflict means accept.
  - Then all temporary assignments are undone and qhead is reset to the top-level trail length. The top-level state is fully
    propagated before each check, because each addclause propagates.
  - A non-RUP lemma stops with «NOT VERIFIED». No RAT check exists.
- Deletions (delclause, l. 56-61). One live clause with the same literal set is marked deleted, by a hash bucket plus an exact
  set comparison on deduplicated sets. Deletion only shrinks the DB, so it cannot make a non-implied lemma pass. Top-level literals
  whose reason is deleted stay assigned, and they are still implied by the input. Sound. IGNDEL=1 ignores them; also sound.
- Verdict (l. 97). «s VERIFIED» iff topconf: an empty clause, an all-false clause, or a top-level propagation conflict. An explicit
  «0» lemma is RUP only if the top level is already in conflict, so a valid DRUP proof is accepted when the refutation is reached.
  Reading stops at topconf.
- Conclusion: every clause that enters the DB is either an input clause or a RUP consequence of DB clauses. By induction every DB
  clause is implied by the input, and a top-level conflict then proves the input UNSAT. drup.c is SOUND as a refutation checker of
  the file it reads.
- Optional TR-P1 (robustness, not soundness): drup.c could check the «p cnf» header (clause count, variable range) and print the
  input's sha1, so the verdict line names its formula. My ref_rup.c does the first.

## 2. Own independent checker and negative tests (docs/referee/scratch/ref_rup.c; t3r_logs/neg_tests.txt)
- ref_rup.c is my own forward RUP checker, written from the definition. It is a different code base from drup.c (I read drup.c for
  the audit but did not copy it). Its design is deliberately stricter and simpler:
  - the DIMACS header is required, exactly C clauses, literals in range, and lemma literals in range;
  - deletions are IGNORED, so the DB only grows;
  - RUP by assigning the negations and running two-watched-literal propagation;
  - VERIFIED iff a top-level conflict is reached.
- Negative tests on d = 2 formulas (cnf.py d 2, cube 0 / cube 3, built by mkproof.py; Glucose 4 proofs). drup.c was run in both
  modes and ref_rup once; all three verdicts agree on every row:
  | test | drup.c | drup.c IGNDEL | ref_rup |
  | --- | --- | --- | --- |
  | valid proof, d 2 L 5 cube 0 (UNSAT) | VERIFIED 5,730 | VERIFIED 5,730 | VERIFIED 5,730 |
  | SAT formula d 2 L 4 with its solver proof | NOT VERIFIED (no refutation) | same | same |
  | SAT formula with the proof «0» | NOT VERIFIED (lemma 1 not RUP) | same | same |
  | UNSAT formula with an empty proof | NOT VERIFIED (no refutation) | same | same |
  | proof truncated to 3,000 lines | NOT VERIFIED (no refutation) | same | same |
  | every 7th lemma dropped | NOT VERIFIED (lemma 7) | same | same |
  | one literal's sign flipped (lemma 2,866) | NOT VERIFIED (lemma 2,866) | same | same |
  | one sign flipped in every 50th lemma | NOT VERIFIED (lemma 1) | same | same |
  | bogus unit lemma «1 0» first | NOT VERIFIED (lemma 1) | same | same |
  | empty clause «0» first | NOT VERIFIED (lemma 1) | same | same |
  | cube 0's proof against cube 3's CNF | NOT VERIFIED (lemma 10) | NOT VERIFIED (lemma 20) | NOT VERIFIED (lemma 20) |
  | cube 3's own proof | VERIFIED 5,444 | VERIFIED 5,444 | VERIFIED 5,444 |
  | one early lemma (the 20th) dropped | VERIFIED 5,729 | same | same |
  - The last row is a valid result, not a miss: that lemma was not needed, so the shorter proof is still a refutation.
  - The «lemma 10 vs 20» difference is deletion handling: with deletions applied the DB is smaller, so a lemma fails earlier.

## 3. Re-generation and re-check of 3 cubes (the cheapest: 10, 9, 5; scratchpad, proofs deleted after the check)
- Commands: python3 -I mkproof.py 3 9 <c> DIR glucose4 at d03d8370, with FREE0 / ISO / KF / P / W / XCUBE / RUN2 unset. Then drup.c
  (deletions applied) and ref_rup on each proof. Log: t3r_logs/tr3_regen_check.txt.
  | cube | DIMACS sha1 | Glucose s | proof sha1 | proof bytes | drup.c | ref_rup |
  | --- | --- | --- | --- | --- | --- | --- |
  | 10 | 924ae0118e1b142a8d762d03d314d4a0c9be1af2 | 162.5 | cae6998bd94b78005931ee2faff7eaffc3c122fc | 851,461,087 | VERIFIED 485,366 (570 s) | VERIFIED 485,366 (708 s) |
  | 9 | 01a9488a18b51267dd6010802c7f4c9a3425d936 | 184.0 | 942334eb3905ff3aa887e37db72d1df84433b804 | 894,105,785 | VERIFIED 526,970 (643 s) | VERIFIED 526,970 (802 s) |
  | 5 | 2701cae6e1025ef02c98c9d9b81b7fb181c68367 | 191.6 | e45c0dd108e48fb8eddeb51ffcb4fe5787833baa | 913,302,433 | VERIFIED 544,619 (647 s) | VERIFIED 544,619 (837 s) |
  - Every DIMACS sha1, proof sha1, proof size and lemma count EQUALS the packet's §4 row. So the proofs are deterministic across
    machines, and the lane's records for these cubes are reproduced exactly.
  - Each formula: 58,896 vars, 204,036 clauses, no conflict after the input.
- DIMACS identity, all 16 cubes: the packet's §3 and §4 sha1 lists both EQUAL my list t3r_logs/dimacs_sha1.txt. That list was built
  by my own driver t3r_dimacs.py from cnf.py at 6f19564f, the version I audited. So the certified formulas are the audited ones.

## 4. Packet text
- §1 statement: «for every genome G ∈ 𝓛^R_3 and every start s_0, the IDEAL run of G from s_0 has at most 8 steps: T^R(3) ≤ 8».
  EXACT. It is the negation of Q(9), and Q(9) is UNSAT ⇔ the statement, given the encoding and the SYM / cube cover (R-T3R-audit
  §1-§2).
- Lower bound: the witness out/R_d3_L8.json gives T = 8 under my simulator t3r_sim.py (R-T3R-audit §3). So T^R(3) = 8.
- Quotes: the R104 model text is verbatim (1 hit in RESULTS), and so is the P-IDEAL-FLIP §1 text (1 hit at 9effea1f).
- REQUIRED TR-1. §1 calls 𝓛^R_d and T^R «not landed terms» and quotes P-IDEAL-FLIP «(= RESULTS R110 once landed …)». R110 HAS
  landed (trunk b5d154ad, RESULTS l. 11323), with «on acyclic Ξ-graphs, … 𝓛^R_d ⊆ 𝓦_d the 2-wide degree-2 ladders in L-RED's R197
  convention (movers 2l and 2l + 1 on level l, all of degree 2, no other movers, option k of a mover of level l ≥ 1 W-pointing to
  mover 2(l − 1) + k), T^R(d) the largest number of steps over 𝓛^R_d and all starts». Cite and quote R110 instead, through a fixes
  entry. The classes are the same; I checked both texts.
- Optional TR-P2: §2 names cnf.py «sha1 fd882af1… at l-comp 557b045b», but the proofs were made by mkproof.py importing cnf.py
  f1f803ae… (d03d8370). Name both, with «the d 3 cube DIMACS is byte-identical» (true, §3).
- Optional TR-P3: §1 «With the witness of §5» should read «§3» (the witness is in §3; §5 is «What is proven»). Also, §4's «Limits»
  calls drup.c «unaudited»; it is audited now (§1).
- §5 (what rests on what) is correct. It needs one change: the trust in drup.c is now shared with an independent second checker on
  3 cubes.

## 5. Scope of my signature
- SIGNED: STATEMENT P-TR3 (T^R(3) ≤ 8, hence T^R(3) = 8) as a MACHINE-CERTIFIED result:
  - lower bound by an explicit instance;
  - upper bound by the audited encoding (R-T3R-audit), plus 16 cube formulas each refuted by a RUP-checked Glucose 4 proof.
  - The checker drup.c is audited sound. For 3 cubes the proofs were regenerated byte for byte and re-checked by my independent
    checker. The 16 UNSAT answers are also reproduced by CaDiCaL 1.9.5, Kissat 4.0.4 and Glucose 4 (R-T3R-audit §4, add. 1).
- Not signed as a mathematical proof: no Lean, no human-readable proof. The trusted base is in §0 (TR-G1, TR-G2).
- Diff against TARGET.md: the statement is inside R104's IDEAL model; it concerns no parity game or running time; not M3, not M4,
  not a gauntlet step. G-N5-TIME stays OPEN. Agreed with §7.

## 6. Line L-1
- Shape: one line, 11 «(» / 11 «)», depth never negative, 0 «|», one « — », «2026» once.
- REQUIRED TR-L1 (definitions).
  - The line cites «𝓛^R_3 (P-IDEAL-FLIP §1, claude/l-new 9effea1f, = RESULTS R110 once landed: …)». Cite RESULTS R110 (landed).
  - It never defines T^R(3). Add R110's «T^R(d) the largest number of steps over 𝓛^R_d and all starts».
  - It does not say «on acyclic Ξ-graphs», which R110's class and the CNF both require; add it.
  - «[lane: EXACT-SAT + CERT]» is a lane label, not a RESULTS tag; the Lead sets the tag.
- REQUIRED TR-L2 (source note). The note names only «experiments/comp/box27/P-TR3.md». The lane-proved facts E1-E3 and the clause map
  live in experiments/comp/box27/ENCODING.md (packet §2, §5), and the certificate records live in log/R_d3_L9_cert.txt. Name
  ENCODING.md (proof-carrying, C122 E-3 precedent), and name the fixes file once TR-1 is written.
- Optional TR-L3: «drup.c's correctness is a premise» can become «drup.c audited by REFEREE (R-P-TR3 §1); 3 cubes re-checked by an
  independent checker».
- DATA scope: each count names its statement («cover «T ≤ 8» only»; pinck «covers only the agreement of the CNF with the simulator»;
  bf2 «only the d 2 cross-check»). The figures equal the packet: 450 = 300 + 150 random; 128 = 2 × 64 runs; 11,353,990 lemmas
  = the §4 total. MEETS C120.
- Verdict: NOT YET (TR-L1, TR-L2).

## DONE / FINDINGS / NEEDS
- DONE: line-by-line audit of drup.c; my own checker ref_rup.c; 13 negative / positive tests, three verdict columns each; 3 cubes
  regenerated with byte-identical proofs and checked by both checkers; DIMACS identity for all 16; packet and L-1 diff.
- FINDINGS:
  - drup.c is SOUND.
  - CERT is reproduced exactly on cubes 5, 9 and 10.
  - P-TR3 SIGNED as machine-certified (gaps TR-G1, TR-G2).
  - TR-1: R110 has landed, so cite it.
  - L-1 NOT YET: TR-L1 (R110 citation, the T^R definition, acyclic) and TR-L2 (ENCODING.md in the source note).
- NEEDS:
  - L-COMP via the Lead: a fixes entry (TR-1, optional TR-P2 / P3) and line L-2 (TR-L1, TR-L2).
  - Optional: run the remaining 13 cubes through ref_rup to close TR-G1. About 1.5 h of machine time here; I can start it on the
    Lead's word.

## §C (2026-11-06T04:09Z by date -u, successor 24): fixes entry 1 and line L-2
- Object: claude/l-comp d3e3cde8 (an ancestor of origin).
  - experiments/comp/box27/P-TR3-fixes.md: sha1 d7b33861ea3a6aecc0a069e43f6df8b53c3f28e3, 73 lines.
  - P-TR3-line-L2.txt: sha1 11cd9acc14147fb7a3820e9a16c9cee15875e611, 1,713 bytes.
  - Unchanged: P-TR3.md (cab32c0e), L-1 (221c81eb), drup.c (2d4b8eab), cnf.py (f1f803ae).
  - New: drup2.c (not the checker of record).
- I have still not read docs/referee-2/ on P-TR3; I know REFEREE-2's items only through the fixes entry's list.
- F1 (TR-1): CORRECT; TR-1 CLOSED.
  - The R110 quote («on acyclic Ξ-graphs, with 𝓦_d … T^R(d) ≤ T*(d))») is verbatim: 1 hit in RESULTS at trunk 4b35e2b0, l. 11323.
  - «Ξ-data arbitrary» is read as «acyclic Ξ-data arbitrary», which matches the CNF.
- F2 (TR-P3, §5 → §3): CORRECT.
- F3 (TR-P2): CORRECT.
  - fd882af1 built the CaDiCaL cubes; f1f803ae built the Glucose proofs.
  - My independent evidence that the DIMACS are byte-identical: t3r_dimacs.py at 6f19564f (= fd882af1) gave the 16 sha1s of the
    table, and mkproof.py with f1f803ae gave the same sha1 for cubes 5, 9, 10, 13, 1 and 14 in my runs.
- F4 (drup.c status): CORRECT for my part.
  - «REFEREE 24 regenerated the proofs of cubes 5, 9, 10 byte-identically and re-checked them with drup.c and its own ref_rup.c» is
    what my report records.
  - REFEREE-2's counts (1 cube; 12,902 fuzz runs) are REFEREE-2's to confirm.
  - The ENCODING.md l. 5 reading note is right.
- F5 (drup2.c): a NEW file, outside the certified record. The entry says so. I did not audit drup2.c; nothing in the claim uses it.
- F6, line L-2 byte test (an inline script, the same method as scratch/keys_l2_bytetest.py):
  - The expected line is L-1 with the entry's 4 replacements, parsed from the fixes file. Each old string occurs once.
  - Result: EQUAL to L-2 (sha1 11cd9acc…, 1,713 bytes).
  - Shape: 13 «(» / 13 «)», depth never negative, 0 «|», one « — », one line.
  - TR-L1 MET: R110's definitions are cited, «acyclic» is added, and T^R(d) is defined verbatim from R110.
  - TR-L2 MET: the source note names P-TR3.md, the fixes file and ENCODING.md.
  - TR-L3 MET: the drup.c status and the re-check counts.
  - The counts «REFEREE 3 cubes» are true as of 5a5b94cf.
- Verdict:
  - L-2 MATCHES.
  - Fixes entry 1 is CORRECT.
  - P-TR3 stays SIGNED as machine-certified. TR-G1 is being closed by the 13-cube ref_rup run (addendum to follow).

## Addendum 1 (2026-11-06T06:15Z by date -u, successor 24): TR-G1 CLOSED, all 16 cubes re-checked by my own checker
- Method: the same as §3. Each remaining cube's proof was regenerated by mkproof.py at d03d8370 (Glucose 4), its sha1 and size were
  recorded, it was checked by ref_rup.c (my checker, deletions ignored), and then deleted. Order 13, 1, 14, 6, 2, 3, 15, 12, 11, 8, 7,
  0, 4. Log: scratch/t3r_logs/tr3_rest13.txt.
- Result for all 13: the DIMACS sha1, proof sha1 and proof size EQUAL the packet's §4 row, and ref_rup gives «s VERIFIED».
- Lemma counts equal §4 except cubes 1, 3 and 8 (567,711 / 803,559 / 931,579 against 567,712 / 803,571 / 931,580). With deletions
  ignored the DB is larger, so the refutation is reached a few lemmas earlier. The packet records the same effect for cube 1 in IGNDEL
  mode (567,711).
- With §3 (cubes 5, 9, 10, also checked by drup.c), all 16 cube proofs are now:
  - regenerated byte-identically from the audited DIMACS;
  - accepted by my independently written RUP checker.
- So CERT no longer rests on drup.c or on the lane's records alone. TR-G1 is CLOSED.
- TR-G2 stands: both checkers are unverified C.
- The line's «REFEREE 3 cubes» is the count on file at fix time. It is true and conservative, so no L-3 is needed (Lead 05:04Z reading:
  the R112 body cites this addendum).

## §C add. 1 (2026-11-06T08:04Z by date -u, successor 24): line L-3 (CHECKER C123 E-1)
- Object: claude/l-comp 9c70c980 (an ancestor of origin).
  - experiments/comp/box27/P-TR3-line-L3.txt: sha1 d87bb3f062115ccf13164465395ef0187ccda7cf, 1,682 bytes.
  - P-TR3-fixes.md: sha1 38b97e59…, entry 2 appended.
- Byte test:
  - Expected = L-2 (11cd9acc) minus the leading «P-TR3 [lane: EXACT-SAT + CERT] ». L-2 starts with it, and it occurs once. I prebuilt
    the expected line before L-3 was pushed: sha1 d87bb3f0…, 1,682 bytes.
  - L-3 is byte-EQUAL to it (cmp).
  - Shape: 13 «(» / 13 «)», depth never negative, 0 «|», one line, starting «In the IDEAL model of RESULTS R104».
- Fixes entry 2 (F7) describes exactly this one deletion. It keeps «REFEREE 3 cubes» (the on-file count; Addendum 1 records 16/16 for
  the body). No statement or definition changes.
- Verdict: L-3 MATCHES. P-TR3 stays SIGNED as machine-certified; TR-G1 is CLOSED (Addendum 1).
