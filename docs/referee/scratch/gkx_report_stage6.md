## 14. Stage 5b, part (i) (written 2026-11-14T13:55Z, date -u): line L-3 and fixes entries 7, 8 (claude/l-red-b 10dfedb6); the final line is held for line L-4 and entry 9 (the Lead's order of 2026-11-14 13:41Z)
REFEREE successor 37. Stages 1-5a (§0-§13: the first 784 lines of this file, sha1 d5017ab5f382685cb9941273b893c31b2174c8a2) are
unchanged, byte for byte: the file is rebuilt from the same template and logs.
- Object: claude/l-red-b 10dfedb6574c9291011a5a7fbbdff261fe312d91. docs/red-b/P-N5-EXP-fixes.md there (1,180 lines, sha1
  013290889e9e08f58ae162baa0c2eb5082f4b135; its first 881 lines are the file of 0c8fdf9e, the object of §13): entry 7 (l. 883-1147)
  and entry 8 (l. 1149-1180), read in full, sentence by sentence. docs/red-b/P-N5-EXP-line-L3.txt (one line, 7,267 bytes, sha1
  fd9074a3b9961f59a1b64d5acdaa28529306ede9), read word by word against §13.0's table, with L-2 (sha1 6e047c67…) and L-1 beside it.
  Also read: the repaired runner experiments/red-b/run_b6fix.sh (57 lines), the lines that entry 7 adds to check.sh, and the
  lane's record data/b6b/out/line_L2_build.out.
- Independence: docs/referee-2/ was NOT read. The 13 quotes that entry 7 takes from it (label REF2B, claude/referee-2 f17a2708)
  and the signature sentence that the line quotes from it were matched BY SCRIPT ONLY (found / not found, line numbers, headings).
  Not checked, because they are statements about that report: entry 7's «REFEREE-2's Addendum 3 … has no item for this lane beyond
  F-1 to F-5», 7.1's «r3_u1, 0 of 4,082 windows» (REF2B l. 483), 7.5's «its second review is deferred by REFEREE-2's own account»,
  7.6's «REF2B l. 342».
- Not done: the lane's tools b6e7.py, b6fixtest.sh, b6guard.py, b6line.py, b6fixquote.py were not run (the re-run on the exact
  commit is CHECKER's) and, except for the lines of b6line.py that print «kept unchanged», not opened; so 7.4's test lines N1-N7
  and C1-C3 are the lane's DATA about its runner, read but not reproduced. No Lean.

### 14.0 Result of part (i)
- **Entry 7**: right, sentence by sentence. **F-1 is ACCEPTED by this lane, as the lane that wrote LEMMA′** (§14.3): clause (R3) is
  to be read with the range t − 1 ≤ τ < last, as entry 7.1 restates it. 7.2's table of the frozen lines is right. 7.3 is this
  lane's N-5b, closed. 7.4: the runner does what the entry says. 7.5 is §13.0's reading of entry 2 (a′). 7.6 is right.
- **Entry 8**: right. L-3 is L-2 with exactly the two named replacements.
- **Line L-3**: the byte tests pass (one line, final newline only, no pipe, brackets balanced and nested, no heading marker). Clause
  by clause (§14.2) it agrees with §13.0's table and with the pinned DATA, EXCEPT two clauses:
  - **F-L3-1 (FAILING CLAUSE, new): «β-ranks by Ξ-depth with ties broken by β-id».** Rule R's rank is the rank of the triple
    (−depth, local δ, β-id); the gloss drops the local δ. Read as written it describes a different genome, which is in IDEAL-ACYC
    and whose IDEAL run has 3 steps, or 1, for every k = 3..12 (§14.3). The theorem is not affected; the line's gloss is wrong.
  - **N-5e (known since stage 5a; ruled by the Lead: line L-4):** «PROVED-CONDITIONAL on RESULTS R124's Corollary EXACT-L as
    landed» stands before a clause that includes «with one fallback», which is R124's Theorem ENDGAME-3-N5, not EXACT-L.
- So **L-3 is NOT signed as the RESULTS line**: the failing clause is F-L3-1 (and N-5e's premise is to be named). Nothing in
  entries 7 and 8 fails. The last line of this lane's report is held until line L-4 and entry 9 are on origin (part (ii)).

### 14.1 Byte tests (own script gkx6_quotes.py; the lane's b6fixquote.py, b6guard.py were not opened)
```
@@S6:E7QUOTES@@
@@S6:E7PINS@@
@@S6:LINE3@@
```
- The fixes file is append-only through its five landed stages; the packet is unchanged; no data file of entries 1-6 and no
  earlier pin file was touched. Entry 7's 24 tagged quotes are in their cited lines (the lane's count: 24), the 13 from the
  second referee's report by script only; entry 8 has none. The 10 + 3 new pins hold; each of the 69 lines inside the fenced
  DATA blocks of entries 7 and 8 is a line of a pinned output file.
- L-3's six guillemet quotations: «stuck»; the definition of IDEAL-ACYC-POLY (verbatim in R104's PACKET, docs/red/P-N5-REALIZE.md
  l. 224; not in docs/RESULTS.md: note L-n1); R117's premises (RESULTS l. 13362, verbatim); this lane's two verdict sentences, at
  the commits the line names (c881709b l. 17; 78515253 l. 522-523, §12); the second referee's signature sentence (f17a2708 l.
  464-465, under its heading A2.3; by script only). The ids in the line are commits, except 9dc9179f, the sha1 prefix of the
  fixes file at 24f4d436, as the line says.

### 14.2 Line L-3, clause by clause
The DATA clauses against the pinned files they name (own script; ctrl-0 lines; every named counter summed over the named k):
```
@@S6:LINEDATA@@
```
| # | clause of L-3 (abridged) | held against | verdict |
| --- | --- | --- | --- |
| 1 | «DEAD-END packet for the candidate N5 (SPEC S1-S5 with FIX 1-4, from its default start S3), CONDITIONAL until two referees sign, in three parts» | §13.0: three kinds of statement | agrees (the status phrase is the Lead's to change at landing) |
| 2 | «(1) UNCONDITIONAL (premise: RESULTS R104's definitions of the genome, IDEAL-ACYC, the X-chain order, the IDEAL step and L(G) only; no theorem of R104 used)» | §13.0 row 1; §2 (N-1) | agrees |
| 3 | «(Theorem EXP-IDEAL, PROVED lane; its RESPONSE LEMMA in the prefix form LEMMA′ of fixes entry 4, with CAUSAL and STABLE in step form)» | §12; §13.0 row 2 | agrees |
| 4 | the gloss of rule R, its mover part: levels 0..k; unit j = u_j, v_j, Y_j and, for 2 ≤ j ≤ k − 2 only, e_j and Y′_j; units 1 and k − 1 four movers, the others seven; outside the units u_0, v_0, wv_j (1 ≤ j ≤ k − 2), wu_j (2 ≤ j ≤ k − 2) | packet §3 (table), §6 l. 186 | agrees: 2 + 4 + 4 + 7(k − 3) + (k − 2) + (k − 3) = 9k − 16 |
| 5 | «all parities even, β-ranks by Ξ-depth with ties broken by β-id» | packet l. 98-99 read as entry 5.1 | «all parities even» agrees; the rank clause **FAILS: F-L3-1** |
| 6 | «is in IDEAL-ACYC with N = 9k − 16 movers, M = 18k − 32 options (every mover has two) and k + 1 levels» | Theorem EXP-IDEAL (a) | agrees |
| 7 | «its IDEAL run has exactly L(G_k) = 2^k − 2 steps and stops «stuck»» | (b) | agrees |
| 8 | «every mover of unit j (1 ≤ j ≤ k − 1) changes its option exactly 2^(j−1) times, v_0 once, u_0 and the wires never (11·2^(k−2) − 9 option changes in all)» | (c) | agrees |
| 9 | «so R104's IDEAL-ACYC-POLY («there is a polynomial q …») is FALSE, already for genomes of degree 2 (N + M = 27k − 48)» | §13.0 row 3 | agrees; note L-n1 on the quotation's source |
| 10 | «(2) PROVED-CONDITIONAL on RESULTS R117's Theorem REACH3 as landed (refereed-only; R117's standing premises, in the words of its title line: «…»)» | RESULTS l. 13362 | agrees: the premises are the title line's words, verbatim |
| 11 | «(Corollary EXP-N5) … (n = 135k − 230 vertices, m = 176k − 300 edges) has one FL run of length exactly 2^k − 2 and makes at least 2^k − 1 iterations, so no polynomial in n or in n + m = 311k − 530 bounds the number of iterations of N5 from S3» | §13.0 row 4; §6 | agrees |
| 12 | «hence, through R117, N5 (SPEC S1-S5, default start S3) does not run in polynomial time, cannot pass gauntlet step 4 (TARGET.md §5), is a DEAD END as an M4 candidate, and G-N5-TIME is answered NO for N5 from S3» | §13.0 row 6 | agrees: conditional, «through R117», for N5 from S3 |
| 13 | «and, PROVED-CONDITIONAL on RESULTS R124's Corollary EXACT-L as landed (premise R117 (f), under SPEC's S1 tie-breaks, same standing premises): (Corollary EXP-N5′) … exactly 2^k + 1 iterations, with one fallback, at iteration 2^k − 1» | §13.0 row 5; RESULTS l. 15371 | the statement agrees; its premise is **under-named: N-5e** (the fallback clause is R124's Theorem ENDGAME-3-N5) |
| 14 | «obstruction RIPPLE (S4a's root-first key rule refuses an improving switch until the key order allows it, and on Γ3(G_k) this makes unit j + 1 respond twice in every response of unit j)» | packet l. 67-68; §5.1 | agrees (a description) |
| 15 | «(3) DATA (measured; every measured run is below n²: the largest, k = 13 (fixes entry 6, one engine), makes 8,193 iterations on n = 1,525 vertices, and 2^k − 1 > n² first at k = 23, n = 2,875, > n³ at k = 37, > n⁴ at k = 51, by arithmetic, not run; so the dead end rests on the proof of (1) and (2) and not on the DATA)» | entry 2 (d), entry 6 (§13.5), §6 | agrees |
| 16 | the six DATA clauses with their files and counters: member.out; sim.out; lemma.out; prefix_*.out with «16,368 response windows», «every triple (j, a, t) for k = 3 … 12», «every state of G_3 and G_4», the frozen wording failing «at exactly k − 1 triples per k»; n5.out and n5_k12.out «two engines and two Γ3 builders, for k = 3 … 12»; n5_k13.out «one engine» | the pinned files (lines `linedata` above) | agree: every named counter is 0 in the file named, the ranges of k are the files' (the frozen-wording control is pinned for k = 3..8; mine, §13.6, for k = 3..13) |
| 17 | «frozen instances Γ3(G_k) = …/pg/G_k_g3.pg, k = 3, …, 11 (175 to 1,255 vertices, 9 to 2,049 iterations), genomes of record …/G/G_k.json, k = 3, …, 14, at claude/l-red-b 350d84eb» | git objects | agrees |
| 18 | «independent replays … cited, not re-run»: L-COMP 22, L-RED 70, REFEREE 35, REFEREE 36, REFEREE-2 41 | entry 5.8 (§13.4) | agree; the clause on REFEREE-2 41 is not checked by me |
| 19 | «NOT claimed: … other start pairs, … other S4a tie rules (DATA: N5′-xi makes 7 iterations on Γ3(G_4) and Γ3(G_6)) or about Howard's rule (DATA: at most 4 steps on the model), about any other candidate, or about parity games in general» | packet l. 72-76; sim.out howard ≤ 4 | agrees |
| 20 | «N5's output on these games is correct (RESULTS R57 (b), Lemma OUT-G, under 1E-N3; DATA for k ≤ 12: winners = Zielonka's)» | entry 2 (e) | agrees (L-n3: k = 13 on one engine is named in part (3)) |
| 21 | «TARGET.md §2 (M4) stays OPEN; not M3 or M4, not a TARGET.md claim» | TARGET.md §2, §4 | agrees |
| 22 | «scope tail (Lead reading L41): CAUSAL and LEMMA′ of fixes entry 4 (4.3, 4.4) are referee-originated, stated and proved by REFEREE 36 (… §5.3; … «NOT SIGNED AS WRITTEN; SIGNED in the form LEMMA′ of §5.3 below»; … §12: «RESPONSE LEMMA SIGNED as restated in fixes entry 4 …»), and are signed independently by REFEREE-2 42, in the form its signature sentence gives (… Addendum 2 §A2.3: «… (R3)'s range read as t − 1 ≤ τ < last (F-1).»)» | this report l. 17, l. 522-523; f17a2708 by script | agrees: both sentences of this lane are verbatim at the commits named, the second referee's is verbatim at its commit (script). Note L-n2: this lane's acceptance of the same reading of (R3) is §14.3 |
| 23 | «(P-N5-EXP, docs/red-b/P-N5-EXP.md, with fixes entries 1-7, docs/red-b/P-N5-EXP-fixes.md; L-RED-B successors 5-7)» | entry 8 | agrees with entry 8 |

### 14.3 F-L3-1: the gloss of the rank clause; and this lane's acceptance of F-1
- F-L3-1. The packet's rule (l. 98-99: «the rank, among all options, of the pair (−depth(x), local δ of (x, o)), a wire counting as
  depth 2k + 5», read with entry 5.1's β-id for the tied wire options) orders the βs depth-major, and INSIDE a depth by the local
  δ of the table; the β-id decides only between the 4k − 14 wire options whose pair is tied. The local δ is what V1-V3 and §8's
  rank orders read (δ(v_j, ·) > δ(u_j, ·); (y, forward) > (ȳ, back); …). L-3 (as L-1 and L-2) says «β-ranks by Ξ-depth with ties
  broken by β-id»: no local δ. Own test (gkx6.py gloss): the genome whose br is the rank of (Ξ-depth, β-id), in the four ways the
  words can be read, everything else as in rule R:
  ```
  @@S6:GLOSS6@@
  ```
  Each of them is a member of IDEAL-ACYC, and none has the run of G_k: for the genome that the gloss describes, «L(G_k) = 2^k −
  2» is false for every k tested. The line names rule R and gk.py, so G_k itself is well defined and Theorem EXP-IDEAL stands;
  what fails is the line's description of the rule. The second referee's note L-a had the unit part of the same gloss corrected
  for the same reason; the rank part was left. A wording that I would sign: «all parities even, β-ranks depth-major (a smaller
  Ξ-depth outranks a larger one), inside a Ξ-depth by the rule's local δ, the remaining ties (wire options only) by β-id». (Sent to
  the Lead on 2026-11-13 at about 19:19Z as a remark on L-1, in a message whose typed header says 19:20Z, and again on 2026-11-14
  at 13:42Z as F-L3-1.)
- F-1, accepted. LEMMA′ is this lane's statement (§5.3, l. 219-225). Its last sentence says «s_τ(E(j)) = a for τ < last» with no
  lower end for τ. The range that the proof proves is t − 1 ≤ τ < last: the proof (l. 226-239) speaks of the states s_(t−1), …,
  s_last of the window only, and this lane's counters test exactly that range (`resp`, column econ, §5.3: τ from t − 1 to last − 1;
  `all`, clause (R3), §13.6). Without the lower end the clause is false at every window of a unit j ≥ 2 that is not that unit's
  first. **This lane signs LEMMA′ with clause (R3) read as fixes entry 7.1 restates it**: «(R3) For T = last: if j ≥ 2, then s_τ(E(j))
  = a for every τ with t − 1 ≤ τ < last, and E(j) moves to c at step last; and (for every j) REST_j(c) and REST_i(0) for every i >
  j hold under s_last.» With this, the author's signature and the second referee's (in the words the line quotes) are on one
  statement in one reading, which is what L41 asks. Own counter (gkx6.py r3; literal = windows with j ≥ 2 where the clause without
  a lower end is false, expected 2^(k−1) − k per k):
  ```
  @@S6:R36@@
  ```

### 14.4 Entry 7 (l. 883-1147), sentence by sentence
```
@@S6:E7FACTS@@
@@S6:XT6@@
```
- Conventions (l. 884-896): the three new labels with their commits, sha1s and line counts are right (REF2B's by script; REF1D is
  this report at 78515253: 542 lines, §12 at l. 498-542, commits 577e8df9 and 4cf6e1ff, its first 496 lines the file at 7ca9c2b4;
  FIX5 is the file both referees read). «quotes 104 found 104 notfound 0» and its control are the last lines of the pinned files.
- The verdicts it answers (l. 898-921): this lane's two sentences are verbatim (l. 522-524, l. 537-538). Its summary of stage 4
  («raises no new item … leaves entry 3's proof text unread») is accurate; stage 5a has since read entries 2, 3, 5 and the proof.
- 7.1 (F-1): the two quoted wordings are verbatim (entry 4.4, l. 384-385; packet l. 203-204). The restated (R3) is right. «Proved»:
  (H1) puts E(j) at a under s_(t−1), and the list moves E(j) once, at the window's last step (u_(k−1) at step t + 2 in case (i),
  e_j at step t_2 + 1 in case (ii)): right. «Used»: only by unit j − 1, inside the window (D, Z under (s_(T−1))⁺; the two frozen
  phrases are verbatim): right. «Without a lower end the clause is false at every window of a unit j ≥ 2 except that unit's first»:
  right, 2^(k−1) − k windows per k. The lane's e7_r3.out equals my own counters in every column (98 comparisons).
- 7.2 (F-2): the table was held against the packet's l. 191-204, row by row: right. As the author of LEMMA′ I confirm it: «the
  packet's list (i) / (ii)», «the lemma's F, B, F′, B′, t_1, t_2» and «last» (through P_j) in LEMMA′ refer to the frozen l. 197,
  l. 198-202, the first sentence of l. 195 and l. 191; l. 193 is (H1); what LEMMA′ replaces is l. 192, l. 194, the conclusion's
  first sentence (l. 195-196) and its last (l. 203-204). The remark on the two parentheses of l. 198 and l. 200 is right.
- 7.3 (F-3): this is N-5b of §13.7; the parenthesis is now to be read with y′, ȳ′; the quoted table row is verbatim (packet l. 87).
  The lane's e7_xt.out equals my own counters (116 comparisons): no Ξ-target is a wire or an e_j; 2(k − 3) options point at a y′_j
  or ȳ′_j.
- 7.4 (F-4): read against the runner. Each stage command writes to a temporary file that is appended only on exit 0; the ctrl
  stage replaces prefix_ctrl.out only if all ten commands exit 0; failures are counted and printed, exit 1 if any, exit 2 for an
  unknown stage; the ERR trap is there as a backstop; check.sh runs one stage with a failing interpreter and one normally. The
  eleven E lines carry the sha1s of SHA1SUMS_b6b_fixes2, and those pinned files and that pin file are unchanged since 24f4d436:
  «No DATA changes» is right. N1-N7 and C1-C3 were not run by me.
- 7.5 (F-5): (i) unconditional, (ii) conditional on L-NEW's Lemma IDEAL-1P: this is §13.0's reading. No line names QUIET-KEY-1P,
  SW-POLY or P-N5-KEY1P.
- 7.6: the guards are in check.sh as described; «REF1D l. 504-505» are §12's two `fixes4` lines. L-2 is L-1 with the five recorded
  replacements (applied at their recorded characters they give L-2 byte for byte); outside them L-2 is L-1. Note N-6a on one
  phrase. The four quotations inside L-2 are verbatim at their commits. The pins hold.

### 14.5 Entry 8 (l. 1149-1180)
- L-3 = L-2 with the two named replacements, each old text once in L-2, nothing else (2 characters differ; undoing gives L-2).
  The builder's record lines are pasted from pinned files. «Why the parenthesis reads «1-7»» is a record of the Lead's ruling,
  which the entry quotes. The entry has no tagged quotation; the guard line it names is the one check.sh tests. Right.
- «L-3 IS THE LINE OF RECORD» was true when written; by the Lead's order of 13:41Z a line L-4 follows.

### 14.6 Notes
- L-n1 (line, clause 9): the guillemet definition of IDEAL-ACYC-POLY is verbatim in R104's packet (docs/red/P-N5-REALIZE.md l. 224
  at trunk 5d7aab0f, the same file at trunk today), not in docs/RESULTS.md, where only the NAME occurs (R104's scope tail l. 9967,
  9971; R117's l. 13454-13455). «R104's IDEAL-ACYC-POLY» is right as a name; a check of the line's quotations against RESULTS
  alone will not find this one.
- L-n2 (line, clause 22): the tail quotes this lane's verdicts of stage 1 and stage 4, which precede F-1. The author's acceptance
  of the reading of (R3) is §14.3; the tail may cite it, the Lead's call.
- L-n3 (line, clause 20): «DATA for k ≤ 12» is true; k = 13 (one engine, winners equal to Zielonka's) is named in part (3).
- N-6a (entry 7.6, l. 1135-1136): «the status phrase, part (1) with IDEAL-ACYC-POLY, … are byte for byte those of L-1»: part (1)
  holds the gloss that L-a rewrote; outside L-a's replacement part (1) is byte for byte L-1's. A loose phrase, nothing wrong.
- N-6b (entry 8, the pasted record): «characters of L-2 kept unchanged 7078 of 7084» is the builder's own measure (by its code, the
  length of L-2 minus the trimmed old texts, 3 characters each); character by character L-3 differs from L-2 at 2 positions.

### DONE / FINDINGS / NEEDS (stage 5b, part (i))
- DONE: entries 7 and 8 read in full and checked sentence by sentence; L-3 byte-tested and held clause by clause against §13.0
  and the pinned DATA; own counters for F-1's range, the Ξ-targets and the line's rank gloss (docs/referee/scratch/gkx6.py,
  gkx6_quotes.py, gkx6_summ.py; logs gkx_logs/s37_gloss, s37_r3, s37_xt, s37_e7_*, s37_linedata, s37_line_L3.out; regenerate:
  `bash docs/referee/scratch/gkx_logs/s37_run.sh`, then gkx_fill.py).
- FINDINGS: (1) entries 7 and 8 right; (2) F-1 accepted by this lane as the author of LEMMA′: (R3) with t − 1 ≤ τ < last; (3)
  F-L3-1: L-3's «β-ranks by Ξ-depth with ties broken by β-id» fails (the genome it describes has L = 3 or 1, k = 3..12); (4) N-5e
  stands for L-3 (the Lead ruled L-4); (5) every other clause of L-3 agrees with §13.0 and the pinned files; (6) notes L-n1, L-n2,
  L-n3, N-6a, N-6b.
- NEEDS: (Lead) line L-4 with BOTH replacements (N-5e and F-L3-1), or a ruling on the gloss; then part (ii) and the final line.
