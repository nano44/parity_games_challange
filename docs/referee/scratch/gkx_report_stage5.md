## 13. Stage 5a (written 2026-11-13T19:15Z, date -u): fixes entries 2, 3, 5 word by word, the proof of EXP-N5′, entry 6 (the Lead's order of 19:03Z)
REFEREE successor 37 (this lane; successor 36 wrote stages 1-4). Stages 1-4 (§0-§12: the first 542 lines of this file, sha1
0ec7d605ffd23b31114cdc328d792261a108ced9) are unchanged, byte for byte: the file is rebuilt from the same template and logs.
- Object: docs/red-b/P-N5-EXP-fixes.md at claude/l-red-b 0c8fdf9e (881 lines, sha1 43a941eb6249f0278e342438f92293b7f7a4449e). Its
  first 829 lines are the file of 24f4d436 (sha1 9dc9179f…, the object of §12): entries 2 (l. 150-244), 3 (l. 245-287), 5 (l.
  648-829) and the conventions (l. 126-148) were read in full, sentence by sentence, with the frozen packet's §2 and §5-§7 beside
  them; entry 6 (l. 831-881) and its driver experiments/red-b/b6n5ck.py (111 lines) were read in full.
- Sources opened: trunk aeb90ac1 docs/RESULTS.md (sha1 eecbd798…, the file of trunk 5d7aab0f that the lane cites): R117's title
  line (l. 13362) and its item (f) (l. 13445; «REACH3 = (f)» l. 13475), R124's title line (l. 15371) in full, R57 (b) (l. 2893,
  2914-2916); claude/l-new 44775605 docs/new/P-N5-KEY1P.md §1-§3, §9 (for entry 2 (a′)); for entry 5.8, the two summary files it
  cites (claude/l-comp dc6d831f experiments/comp/box48/README.md; claude/l-red c7ed9b8b docs/red/R245-kill-Gk.md), only for the
  numbers the entry repeats.
- Independence: docs/referee-2/ was NOT read. The 18 quotes that entries 2-5 take from it (label REF2) were matched BY SCRIPT ONLY
  against the file the fixes file names (found / not found and line numbers; as in §12).
- How this stage came about. The Lead's change of order (17:15Z: stage 4 is successor 36's) reached this session at 19:04Z,
  after its turn had been stopped by a usage limit. By then I had read entries 2-5 in full and had written and run direct tests of
  entry 4. Entry 4 is NOT re-reviewed here: §12 stands as successor 36 wrote it. My entry-4 logs are named in §13.6 as
  supplementary DATA; they agree with §12 in every point.
- Not done: N5 at k = 13 was not re-run on this lane's engine (successor 35's run at k = 12 took 1,555 s on it; the lane's k = 13
  line is DATA of ONE engine and is cited as such); the lane's tools were not run (the re-run on the exact commit is CHECKER's);
  the unquoted references of entry 5 to the second referee's report (5.1 «its l. 79-81», 5.3 «its §3.6, l. 219-220» and «its l.
  221-222», 5.5 «its l. 169», 5.8's line on REFEREE-2 41) were not checked: that report is not opened by this session; no Lean.

### 13.0 Result
- **Entry 2**: every sentence is right. P-1 and E-7 are closed. One citation locator is off by one line (note N-5a); no statement,
  label or quote is wrong.
- **Entry 3**: the statement of Corollary EXP-N5′ and its PROOF are right. I SIGN the corollary as PROVED-CONDITIONAL on RESULTS
  R124 (Corollary EXACT-L, Theorem ENDGAME-3-N5) and RESULTS R117 (f) as landed, as successor 36 signed the statement (§12
  addendum). O-1 is closed.
- **Entry 5**: every sentence is right, the five unquoted references to the second referee's report excepted, which I did not
  check (listed above under «Not done»; they are records, no statement rests on them). E-3 and E-6 are closed; the pre-check items P-2, M-1, M-2, M-3 are answered with the right numbers. One parenthesis is incomplete
  (note N-5b); what it supports is right.
- **Entry 6**: DATA only, as it says; no statement changes. It names its ONE engine (engine 1: L-NEW's n5v.step in mode spec from S3
  = n5x.start_pair; engine 2 «is NOT run by it») and its counters with units (ckdiff, must 0, unit (genome, field), 0 of 72, with a
  firing control and a kill-and-resume line; at k = 13 the must-0 counters mism, wrong, nonmover, gdiff). Every number in it is
  the number of its pinned file; its k = 13 game is the game this lane's builder makes (§13.5).
- **P-N5-EXP: SIGNED with fixes entries 1-6.** What the signature covers, by kind (this is §0 with every item of §9 closed, §12's
  verdict line, and the rows that entries 2 and 3 add):
| statement | where it now stands | verdict | kind |
| --- | --- | --- | --- |
| Theorem EXP-IDEAL (a), (b), (c), with MEMBER, MOVE-2, V0-V4, K1-K4, WIRE | packet §2-§7; rule R read as entry 5.1; standing assumption entry 4.1 (S1); §7 read as entry 4.6 | **SIGNED** (§0, §12) | unconditional: R104's definitions only |
| RESPONSE LEMMA = LEMMA′, with CAUSAL; STABLE in step form | entry 4 (4.2-4.5) = this report §5.3 | **SIGNED** (§12; referee-originated, L41: it also needs REFEREE-2's independent signature) | unconditional |
| «IDEAL-ACYC-POLY is false» | entry 2 (a′), its sentences on R104's model | **SIGNED** | unconditional ((a)-(c) put into R104's definition of L) |
| Corollary EXP-N5 (at least 2^k − 1 iterations) | packet §2, §7 with entry 2 (b) | **SIGNED as PROVED-CONDITIONAL** on RESULTS R117's Theorem REACH3 as landed | conditional: R117's standing premises, in R117's words |
| Corollary EXP-N5′ (exactly 2^k + 1 iterations, exactly one fallback, at iteration 2^k − 1) | entry 3 | **SIGNED as PROVED-CONDITIONAL** on RESULTS R124 (EXACT-L, ENDGAME-3-N5) and R117 (f) as landed | conditional: R117's premises and R124's own |
| Dead-end paragraph | packet l. 61-71 read as entry 2 (c), (e) | **SIGNED AS CONDITIONAL** on R117's premises, «for N5 from S3»; its arithmetic is unconditional; «CORRECT» is RESULTS R57 (b) for every k (under 1E-N3) and DATA for k ≤ 13 | conditional |
| DATA (packet §9; entries 1, 4.7, 5, 6) | | MEASURED | premise-free; N5 itself: k ≤ 12 on two engines of the lane, k = 13 on one |
  The sentence of entry 2 (a′) on L-NEW's packet (QUIET-KEY-1P and SW-POLY are false) is right as worded: it holds THROUGH
  L-NEW's Lemma IDEAL-1P (T_key(G) = L(G); packet P-N5-KEY1P, a frozen lane packet, signed by this lane in R-P-N5-KEY1P.md §2;
  not a landed result) and is not a statement of this packet. L43 as in §0: the growth is PROVED for every k ≥ 3; no measured run
  lies beyond an explicit polynomial bound of degree 2 or more (entry 2 (d) and entry 6 say so).

### 13.1 Byte tests (own script gkx5_quotes.py; the lane's b6fixquote.py was not opened)
```
@@S5:OBJ5@@
@@S5:QUOTES5@@
@@S5:PINS5@@
```
- The frozen packet is unchanged; nothing of the frozen data was modified or deleted; each version of the fixes file is a byte
  prefix of the next, so entries 1-5 are, at 0c8fdf9e, the texts that §10 and §12 checked.
- Quotes. A tag owns the guillemet groups that follow it, separated by white space only; each is searched in the lines its tag
  cites, white-space runs collapsed. All 55 quotes with a label other than REF2 are in their cited lines (19 in entry 2, 10 in
  entry 3, 14 in entry 4, 12 in entry 5); the control finds none. Of the 18 REF2-tagged quotes 17 are in their cited lines; the
  one that is not ([Q REF2 l. 248-249], entry 2 (d), fixes l. 224) is verbatim in that file at its l. 247-249: N-5a. The lane's
  count «75 in entries 2-5» is this script's 73 plus the two untagged quotes of 4.0's E-1 bullet (both verbatim in the packet).
- The 20 sha1 values written in entries 2-6 equal the git objects; the 13 + 6 pins of SHA1SUMS_b6b_fixes2 and _fixes3 hold; each
  of the 120 lines inside the fenced DATA blocks of entries 4, 5, 6 is a line of a pinned output file (pasted, not typed).

### 13.2 Entry 2 (l. 150-244), paragraph by paragraph
- Heading and the five quoted items (l. 150-170): the labels and line numbers of this lane's items are right (§2 at l. 55-63, the
  verdict rows at l. 20-21, E-7 at l. 281-285, the pre-check's P-1 at its l. 322-326); the quotes are verbatim.
- (a) UNCONDITIONAL (l. 174-178): right. It is §2's N-1: the packet uses R104's definitions only, MEMBER c8 first.
- (a′) (l. 180-188): the quoted definition is R104's packet l. 224, verbatim. L(G_k) = 2^k − 2 with N + M = 27k − 48 and all
  degrees 2 refutes it for G_k ∈ IDEAL-ACYC; «the movers of unit k − 1 change their option 2^(k−2) times» is (c). The two KEY1P
  quotes are verbatim (its l. 138, 211); that packet's l. 138-139 itself says of QUIET-KEY-1P: «By Lemma IDEAL-1P this is word for
  word R117's IDEAL-ACYC-POLY», and its l. 212: «QUIET-KEY-1P ⟺ SW-POLY». Right, with the dependence on L-NEW's lemma stated in
  the sentence.
- (b) PROVED-CONDITIONAL (l. 190-204): the line references of Corollary EXP-N5 (packet l. 54-60, 276-282) are right. The premises
  are quoted from R117's title line, verbatim, l. 13362: «with R104's premises as landed (1E-N3 = RESULTS R57 (b) in its two
  forms; RESULTS R24 (a) Lemma R and R24 (b)'s choice rule with RESULTS R103's bridge B and (R1) ruling; RESULTS R36 (c) Lemma P1
  on the dual game) and RESULTS R15 (d) for termination only». The names [1E-N3], [RULE], [VJ-LOC], [TERM] and what they leave
  open are quoted from R117's entry (l. 13482-13488, 13543-13544), verbatim. REACH3's hypothesis («for every G with an ACYCLIC
  Ξ-graph») is met by MEMBER c8, and L(G_k) ≥ 1; nothing else of R117 is used: right (the packet's mention of Corollary
  REAL-IDEAL-S3 is a remark). **P-1 closed.**
- (c) (l. 206-215): the two frozen sentences are quoted verbatim; the reading «under R117's Theorem REACH3 as landed, N5 (SPEC
  S1-S5) from its default start S3 makes at least 2^k − 1 iterations on Γ3(G_k)», with the sizes n = 135k − 230 and n + m = 311k −
  530 and the conclusion «G-N5-TIME is answered NO for N5 from S3», is the Corollary with its condition; «The arithmetic of that
  paragraph (the sizes; the first k beyond n^c) is unconditional» is right (§6: exact integers).
- (d) MEASURED (l. 217-229): every number recomputed (line `arith` above). «no measured run lies beyond an explicit polynomial
  bound of degree 2 or more» is right, and stays right with entry 6's k = 13 (8,193 < n² = 2,325,625).
- (e) (l. 231-243): the frozen sentence is quoted verbatim; R57's two quotes are verbatim (l. 2893, 2914-2916); «For EVERY k it is
  not DATA but landed RESULTS R57 (b), Lemma OUT-G, under the same standing premise as (b)» is what E-7 asked. **E-7 closed.**

### 13.3 Entry 3 (l. 245-287): Corollary EXP-N5′, statement and proof
- The statement (l. 255-258) names its condition (R124's Corollary EXACT-L as landed), its premise (R117 (f) = Theorem REACH3, which
  is right: RESULTS l. 13445, 13475) and the algorithm in R124's words («N5 (SPEC S1-S5 with its FIX 1-4 tie-breaks) from S3»).
- The proof (l. 260-266), step by step. (1) «G_k ∈ IDEAL-ACYC (Lemma MEMBER, c8: the Ξ-graph is acyclic and has no self-loop)»:
  right; the self-loop clause matters, R124 records that EXACT-L fails without it. (2) «L(G_k) = 2^k − 2 (Theorem EXP-IDEAL (b))».
  (3) The three R124 quotes are verbatim, from l. 15371: EXACT-L, «PROVED for G ∈ IDEAL-ACYC», gives exactly L(G) + 3 iterations;
  ENDGAME-3-N5 (every genome) gives exactly one fallback, at an iteration F ≥ 1, and exactly F + 2 iterations. (4) «So the count is
  L(G_k) + 3 = 2^k + 1 and the fallback is iteration F = L(G_k) + 1 = 2^k − 1»: the count by EXACT-L; F from F + 2 = L(G_k) + 3,
  the one step the text leaves to the reader. It is also REACH3's «transition L(G) + 1 is a fallback». The proof is right and
  complete; it is the derivation of §12's addendum.
- «R124's premises, in its words» (l. 268-271): the three quotes are verbatim. «What EXP-N5′ adds» (l. 273-280): the two quotes
  are verbatim; R124's «iff» is used in the direction «count polynomial in n ⟹ L(G) polynomial in N + M» (count = L + 3 and n = N +
  7M + 10), and L(G_k) = 2^k − 2 with N + M = 27k − 48 refutes the right-hand side: right.
- The DATA sentence (l. 282-286): its = its2 = 2^k + 1, fb = fb2 = 1, F = 2^k − 2 on every line of the frozen n5.out (k = 3..11) and
  of entry 1's n5_k12.out (line `facts entry 3` below). **O-1 closed.**

### 13.4 Entry 5 (l. 648-829)
```
@@S5:FACTS5@@
```
- 5.1 (E-3): rule R's br is to be read as the rank of the triple (−depth, local δ, β-id), c6 with it; gk.py has exactly the quoted
  line. The ties are as listed (wv_j: 1 ≤ j ≤ k − 2; wu_j: 2 ≤ j ≤ k − 2; both options each), 4k − 14 for k ≥ 4 and none at k = 3,
  my wtie of §3. «Harmless for every tie-break»: right: a wire's β lies in the one-element chain of its own option only, and is
  compared only with the other option of the same wire, whose δ differs (N-5b on the parenthesis). **E-3 closed.**
- 5.2: «step τ» is defined once, in 4.1 (S2), (S3): right. 5.3 (E-6): the summary of quote.out (33 lines: 5 sources, 27 FOUND, the
  last line) with the five sha1s, all equal to the git objects and to my count of §8. **E-6 closed.**
- 5.4 (P-2): both frozen numbers are quoted verbatim; 9 is the width for k ≥ 6 and 8 the width at k = 5 (my `member`, §3). 5.5
  (M-1): the eight sha1s are right (pins); the packet's l. 96-97 and l. 119-121 say what the entry says; SHA1SUMS_b6b has 50
  lines; the pre-check's RENUM is at its l. 86. 5.6 (M-2): the mover order is the order of the table's rows as my rule writes
  them (§3: gendiff 0 compares the option lists with their indices), β-id 2x + o. 5.7 (M-3): the eight keys, deg the number 2.
- 5.8: the frozen §9 header has «three N5 engines (n5v, n5b, n5s237) and three Γ3 builders»; the commits exist on their branches (dc6d831f
  on claude/l-comp; c7ed9b8b on claude/l-red with 706d1ecc its ancestor); the numbers repeated from the two summary files are in
  them (model k = 3..20 and N5 k = 3..12 with Oink --tl and --zlk in box 48; SURVIVES, the model to k = 12 and N5 for k = 3..8 in
  R245, whose own list says «N5 beyond k = 8» is not established); the lines on REFEREE 35 and REFEREE 36 are right (§1, §3, §7);
  the line on REFEREE-2 41 is not checked by me (as said above). 5.9: O-2 and N-1 are recorded as this report states them; «about 40%» is entry
  1's 9.10.

### 13.5 Entry 6 (l. 831-881): N5 at k = 13 on one engine
- The driver (read): the game is built by L-NEW's gamma3.build / eg195.topg and compared with the lane's own builder (gdiff); N5
  is n5v.step in mode spec from n5x.start_pair; the model's key run is compared state by state up to the first fallback (mism);
  nonmover counts a change of a non-mover Even vertex or of τ before the fallback; wrong compares the winners with harness
  Zielonka's; a checkpoint (σ, τ, the counters) every 100 iterations. This is what the entry says. The k = 13 line has resumes
  0, so it is one uninterrupted run; the kill-and-resume line (G_9, resumes 2) equals the frozen line in all twelve fields.
- The entry's numbers against its pinned files: lines `facts entry 6` above (72 fields of n5ck_check.out against the frozen n5.out,
  0 different; the control fires wrong; the k = 13 line: 15 fields, 0 different, pg_sha1 the sha1 of the committed game).
- The game. The lane's G_13_g3.pg is IDENTICAL, vertex by vertex (priority, owner, successor set), to the game this lane's builder
  (gk_gamma3.py) makes from my genome, which equals successor 35's rebuild (as §7 for k ≤ 11 and §10.1 for k = 12):
  ```
  @@S5:PG13@@
  ```
- So entry 6 is right as DATA: at k = 13, on one engine, 8,193 = 2^13 + 1 iterations with one fallback at iteration 8,191 = 2^13 −
  1, on n = 1,525 vertices; it is the value EXP-N5 (at least 8,191, through R117) and EXP-N5′ (exactly 8,193, through R124) give.
  Its «What this does NOT add» is right: above n + m = 3,513, below n² = 2,325,625. Not reproduced by me: the N5 run itself.

### 13.6 Supplementary DATA on entry 4 (not a re-review; §12 is the lane's review of entry 4)
Tool docs/referee/scratch/gkx5.py, on this lane's own model (gkx.py). Every order bit is read from the DEFINITIONS (C_i(s) =
[key_s(v_i) < key_s(u_i)], E_i(s) = [B_s(v_i, ·) is better than B_s(u_i, ·)]); s⁺ is the step's s′, or s at a stop.
- `all`: LEMMA′ as stated (l. 219-225) at EVERY triple (j, a, t), 1 ≤ t ≤ L + 3, and every T of its window, hypotheses evaluated
  literally, with the guards. windows = triples where (H1) and (H2′_t) hold; notrec = windows that are not windows of the
  recursion, or the converse; must 0: viol = (window, T) with (H2′_T) where (R1), (R2) or (R3) fails. Then the lemma AS FROZEN
  (packet l. 192-204) at every triple: it fails exactly at the k − 1 triples with t = 2^k − 1 (E-1's instance among them):
  ```
  @@S5:ALL5@@
  ```
- `exh`: EVERY state with the wires and u_0 at option 0 (2^9 states of G_3, 2^16 of G_4): clos ((S1): s⁺ leaves the set), c0e0,
  v0plus (s⁺(v_0) ≠ 1), loc (CAUSAL as a function: a triple (s on U_j, E_(j−1)(s), C_(j−1)(s⁺)) seen with two different s⁺ on U_j),
  stviol / sthence / stcons (STABLE in step form with entry 4.2's two added clauses), onestate_* (the frozen one-state reading,
  which fails: E-5), pviol (LEMMA′ with s in the role of s_(t−1), along s, s⁺, …, up to the largest T with (H2′_T); proper = the
  hypothesis fails inside the window). Controls: 1 the list demanded one step beyond the hypothesis; 2 F and B exchanged; 3
  CAUSAL without the key bit; 4 without the value bit; 5 the key bit read under s. `arb`: the STABLE and pviol counters on 3,000
  states per (k, seed), half with a planted rest, half a run state with 1-3 movers below the unit flipped:
  ```
  @@S5:EXH5@@
  @@S5:ARB5@@
  ```
- Re-runs of stage 1's and stage 2's counters `unit`, `abs`, `resp`, `causal` (byte-equal to their committed logs), and the
  lane's pinned outputs of entry 4.7 (1), (2), (8) against my logs, column by column: two implementations, every shared count
  equal (the lane's h1only also counts t − 1 = L + 1, L + 2, hence 2(k − 1) more per k):
  ```
  @@S5:RERUN5@@
  @@S5:LANECMP5@@
  ```

### 13.7 Notes (no statement affected; the lane may take them into a later entry)
- N-5a (entry 2 (d), fixes l. 224): the tag [Q REF2 l. 248-249] should read l. 247-249: the quote begins one line earlier in the
  file the fixes file names (found by script; the lane's own quote_fixes.out prints «l. 247-249» for it). The quote is verbatim.
- N-5b (entry 5.1, fixes l. 670): «(table: every Ξ-target is a u, v, y, ȳ or X)» omits y′_j and ȳ′_j, the Ξ-targets of e_j (table,
  row e_j). What the sentence uses, «no Ξ-edge ends at a wire», is right by the table.
- N-5c (conventions, l. 134): «75 in entries 2-5» includes two quotes without a tag of their own (§13.1). Nothing is misquoted.
- N-5d (entry 4.4, Remark 2; seen while reading, entry 4 is not re-reviewed): for j = 1 the frozen (H2) ranged over τ ≤ t + P_1 −
  1 = last + 1, so it also asked for both bits under s_(last+1); a remark about what LEMMA′ drops, LEMMA′ being the stronger form.

### DONE / FINDINGS / NEEDS (stage 5a)
- DONE: entries 2, 3, 5, 6 read in full and checked sentence by sentence; byte tests, pins, pasted blocks, arithmetic and single
  facts by script (logs docs/referee/scratch/gkx_logs/s37_*.out; regenerate: `bash docs/referee/scratch/gkx_logs/s37_run.sh`,
  about 4 minutes, then gkx_fill.py); the k = 13 game compared with this lane's builder's.
- FINDINGS: (1) entry 2 right: P-1, E-7 closed; (2) entry 3: statement and proof of Corollary EXP-N5′ right, SIGNED as
  PROVED-CONDITIONAL on R124 and R117 as landed: O-1 closed; (3) entry 5 right: E-3, E-6 closed; (4) entry 6 right as DATA: one
  engine, counters named, the game identical to this lane's; (5) notes N-5a (a line range off by one), N-5b, N-5c, N-5d: no
  statement affected; (6) supplementary: LEMMA′ holds at every triple and every T for k = 3..13 and from every state of G_3, G_4,
  the frozen lemma fails exactly at the k − 1 triples with t = 2^k − 1, 163 shared counts equal the lane's.
- NEEDS: (Lead) nothing. Stage 5b (line L-2, entry 7) waits for the commit.

**P-N5-EXP: SIGNED with fixes entries 1-6.**
