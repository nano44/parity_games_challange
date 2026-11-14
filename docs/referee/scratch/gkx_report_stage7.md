## 15. Stage 5b, part (ii) (written 2026-11-14T15:32Z, date -u): lines L-4, L-5, L-6 and fixes entries 9, 10, 11 (claude/l-red-b 91d30d95); the final line (the Lead's orders of 2026-11-14 14:14Z, 14:26Z and 15:18Z)
REFEREE successor 37. Stages 1-5b (i) (§0-§14: the first 1,011 lines of this file, sha1 fedd674bf4eac8e95c5be3bc499631b606cbc79f) are
unchanged, byte for byte: the file is rebuilt from the same template and logs.
- Object: claude/l-red-b 91d30d95a3875950b5290b8fc63f1e2c3ad05238 (the head of that branch on origin by my own `git ls-remote` at
  15:29Z). docs/red-b/P-N5-EXP-fixes.md there (1,443 lines, sha1 214967a10752ac9b90981d01628bec13473da404; its first 1,180 lines are
  the file of 10dfedb6, the object of §14): entry 9 (l. 1182-1271), entry 10 (l. 1273-1368) and entry 11 (l. 1370-1443), read in
  full, sentence by sentence. The lines docs/red-b/P-N5-EXP-line-L4.txt (7,292 bytes, sha1 668fd1b88ea4ae28690f0b931d84b27a85928ca8),
  -L5.txt (7,482 bytes, sha1 fbd857b08befb397e03e71c554cccb4542be3820) and -L6.txt (one line, 7,755 bytes, sha1
  1e0ff12d51da7a4ee1aad12ed0fd9119a097896b). L-6 was read whole; every clause in which it differs from L-3 was held against L-3
  (§14.2), §13.0 and the sources. The packet is unchanged (sha1 c0449b17193f19619f33b366096762dfde27d542).
- Independence: docs/referee-2/ was NOT read. Entries 9, 10, 11 take no tagged quote from it; the signature sentence that the
  line quotes from it was matched BY SCRIPT ONLY (f17a2708 l. 464-465), as in §14. Not checked, because they are statements about
  that report or about messages this lane did not receive: entry 11's account of REFEREE-2 42's Addendum 4 (its commit 4d5b03f7,
  «local to that lane»; its items L3-1 to L3-5 as relayed); the texts of the Lead's messages to L-RED-B that the entries quote
  (13:41Z, 13:55Z, 14:14Z), except where they relay this lane's own words (compared with my sent messages, §15.4) or quote RESULTS
  (located, §15.6).
- Not done: the lane's tools b6gloss.py, b6line.py, b6guard.py, b6fixquote.py and check.sh were not run and not opened (the
  re-run on the exact commit is CHECKER's); their pinned outputs were read by script. So the guard lines of 9.3, 10.3, 11.4
  («guard frozen 0 prefix 0 of 8 …») and the description of the quote control's new spoiler (9.3) are the lane's DATA about its
  tools; what the guards protect (the append-only chain, the packet, the six line files) is measured by my own script below. No Lean.

### 15.0 Result of part (ii)
- **Entry 9**: right, sentence by sentence. 9.1 closes N-5e: the label of Corollary EXP-N5′ now names both statements of R124, and
  which clause rests on which is stated correctly. 9.2 records N-5a to N-5d as this lane wrote them and answers each correctly.
  9.3: L-4 is L-3 with exactly the two recorded replacements.
- **Entry 10**: right, sentence by sentence. 10.1 accepts F-L3-1 and reproduces it; the lane's gloss.out equals my own counters
  in every column. 10.2 is note L-n1, closed. 10.3: L-5 is L-4 with exactly the three recorded replacements; the new gloss is the
  wording offered in §14.3, character for character.
- **Entry 11**: right in everything that this lane can check: 11.1 against the pinned DATA; 11.2 against RESULTS R124's landed
  text; 11.3 against this lane's own first review, which it describes correctly (confirmed here by the lane it names, §15.5);
  11.4: L-6 is L-5 with exactly the four recorded replacements.
- **Line L-6**: the byte tests pass (one line, final newline only, no pipe, no tab, no double space, brackets balanced and
  nested, no heading marker). L-6 is L-3 with seven replaced texts in six clauses and nothing else (15 word-level hunks, all
  inside them: §15.2). Each replaced text agrees with its source. With them the two clauses that failed in §14 are repaired
  (**F-L3-1 closed, N-5e closed**) and the notes L-n1 and L-n3 are taken up; L-n2 stands as a remark (§15.7). Every other clause of
  L-6 is the clause of L-3, byte for byte, with its verdict of §14.2.
- **Does ENDGAME-3-N5 need TERM-XI, and so RESULTS R15 (c)? YES** (§15.6): in the proof of record its «exactly F + 2 iterations»
  starts from «By TERM-XI the run stops», and TERM-XI is proved from R15 (c). So Corollary EXP-N5′ rests on R15 (c) through
  EXACT-L → ENDGAME-3-N5 → TERM-XI, and L-6 is right to name it.
- **P-N5-EXP: SIGNED with fixes entries 1-11; line L-6 (sha1 1e0ff12d51da7a4ee1aad12ed0fd9119a097896b) SIGNED as the RESULTS
  line.** What the signature covers is §13.0's table, with F-1's reading of (R3) (§14.3) and the label of Corollary EXP-N5′ as
  entries 9.1 and 11.2 read it. No failing clause is left; the notes of §15.7 change no statement.

### 15.1 Byte tests (own script gkx6_quotes.py)
```
@@S6:E9QUOTES@@
@@S6:E9PINS@@
@@S6:LINE6@@
```
- The fixes file is append-only through its eight landed stages; the packet is unchanged; since §14's object only five files
  were modified (the fixes file, three tools, check.sh), none under data/, and 25 were added. The 18 tagged quotes of entries 9,
  10, 11 are in their cited lines (the lane's counts: 9, 4, 5); the control finds none. The 5 + 7 + 6 new pins hold; each of the 55
  lines inside the fenced DATA blocks of the three entries is a line of a pinned output file.
- L-6's six guillemet quotations are at the places the line names: «stuck»; the definition of IDEAL-ACYC-POLY in R104's packet (l.
  224), which the line now names as its source; R117's premises (RESULTS l. 13362); this lane's two verdict sentences (c881709b l.
  17; 78515253 l. 522-523); the second referee's signature sentence (by script only). The ids in the line are commits, except
  9dc9179f, the sha1 prefix of the fixes file at 24f4d436, as the line says.

### 15.2 L-6 against L-3: the replaced texts, one by one
The chain L-3 → L-4 → L-5 → L-6 and the net change, word by word (own script; nothing outside these hunks differs):
```
@@S6:LINECHAIN@@
```
| # | clause (§14.2) | L-3 | L-6 | made in | held against | verdict |
| --- | --- | --- | --- | --- | --- | --- |
| A | 5 | «β-ranks by Ξ-depth with ties broken by β-id» | «β-ranks depth-major (a smaller Ξ-depth outranks a larger one), inside a Ξ-depth by the rule's local δ, the remaining ties (wire options only) by β-id» | L-5 (10.3) | packet l. 98-99 read as entry 5.1; §14.3; own test gloss2 | agrees: it is rule R's rank clause; **F-L3-1 closed** |
| B | 9 | «so R104's IDEAL-ACYC-POLY» before the quoted sentence | «so IDEAL-ACYC-POLY (named in RESULTS R104 and R117; in the words of R104's packet docs/red/P-N5-REALIZE.md:» before the same sentence | L-5 (10.2) | RESULTS l. 9967, 9971, 10079 (R104), 13454, 13455, 13459 (R117); the packet's l. 224 | agrees; L-n1 closed |
| C | 13 | «RESULTS R124's Corollary EXACT-L as landed» | «RESULTS R124's Corollary EXACT-L and Theorem ENDGAME-3-N5 as landed» | L-4 (9.1) | RESULTS l. 15371; §13.3 | agrees; **N-5e closed** |
| D | 13 | «(premise R117 (f), under SPEC's S1 tie-breaks, same standing premises)» | «(with R124's premises as landed, all under the standing SPEC premise 1E-N3, among them RESULTS R117 (f) for EXACT-L, SPEC's S1 tie-breaks through REACH3's [RULE] choice, and RESULTS R15 (c) for Lemma TERM-XI)» | L-6 (11.2) | RESULTS l. 15371, four phrases located (§15.6) | agrees: each named item is in R124's landed text, for the statement the line names it for; «among them» is right, R124 lists more |
| E | 20 | «DATA for k ≤ 12: winners = Zielonka's» | «DATA for k ≤ 13, k = 13 on one engine: winners = Zielonka's» | L-6 (11.1) | n5.out, n5_k12.out (wrong, wrong2 0); n5_k13.out (wrong 0, no second engine's columns); §13.5 | agrees; L-n3 closed |
| F | 22 | «CAUSAL and LEMMA′ of fixes entry 4 (4.3, 4.4) are referee-originated, stated and proved by REFEREE 36» | «STABLE's step form, CAUSAL and LEMMA′ of fixes entry 4 (4.2, 4.3, 4.4) are referee-originated, stated by REFEREE 36, which also proved CAUSAL and LEMMA′, the proof of STABLE being the frozen one read in step form» | L-6 (11.3) | this report at c881709b, §5.3 (l. 199-262); fixes entry 4.2 (l. 350-356); packet l. 258-262 | agrees; confirmed by this lane, which the clause names (§15.5) |
| G | 23 | «with fixes entries 1-7» | «with fixes entries 1-11» | L-4, L-5, L-6 | entries 9.3, 10.3, 11.4 | agrees: these are the entries this lane has read and signs |

The DATA clauses of L-6 against the pinned files they name, at 91d30d95 (the same counters as §14.2; row E reads the n5 lines):
```
@@S6:LINEDATA6@@
```
- Row A, own test. The corrected wording still leaves two things open: the direction of the β-id tie-break, and where a wire
  stands (the rule: «a wire counting as depth 2k + 5»; from the Ξ-graph alone a wire, whose Ξ-target is X, would stand at depth
  0). Own counter (gkx6.py gloss2): the genome with br built from the wording in each of the eight readings, everything else as
  in rule R:
  ```
  @@S6:GLOSS2@@
  ```
  Every reading is in IDEAL-ACYC and has G_k's IDEAL run, state by state, with L = 2^k − 2. So, unlike the old gloss (§14.3: L = 3
  or 1), the new one cannot be read into a genome for which the line's statements fail; the genome itself is fixed by rule R and
  gk.py, which the line names.
- Rows C and D, the arithmetic of Corollary EXP-N5′ on R124's two statements: EXACT-L gives L(G_k) + 3 = 2^k − 2 + 3 = 2^k + 1
  iterations; ENDGAME-3-N5 gives one fallback, at an iteration F, and F + 2 iterations, so F = 2^k − 1. This is entry 3's proof
  (§13.3), unchanged.

### 15.3 Entry 9 (l. 1182-1271), sentence by sentence
```
@@S6:E9FACTS@@
```
- The label REF1E (l. 1183-1185): the commit, the sha1, «784 lines», «stage 5a is its §13, l. 544-784» and «its first 542 lines
  are the file at 78515253 byte for byte» are right. The verdict it quotes is §13.0's (l. 580).
- 9.1: this lane's sentence on entry 3 is verbatim (l. 570-572); the two quotes of entry 3 are verbatim (the fixes file at
  24f4d436, l. 255 and l. 261). The Lead's item is quoted from a message to that lane (not checked); the two phrases of RESULTS
  inside it are in l. 15371. «Accepted. READ the label …»: right. «Which clause rests on which statement»: right (§15.2, rows C
  and D). «The PROOF of entry 3 is unchanged: it quotes both statements (FIX5 l. 262-264), and the referee checked it step by step
  (REF1E l. 659-665)»: right; those lines are §13.3's.
- 9.2: the four notes are quoted verbatim (l. 765-771). N-5a: «READ the line range of that tag of entry 2 (d) as 247-249», right,
  closed. N-5b: «Already read so in entry 7, 7.3», right (§14.4). N-5c: the lane's account of its count («every guillemet group
  after a tag, up to the next tag or the next blank line, is one quote»; the two quotes are the packet's words in the E-1 bullet
  of 4.0) is what my script found (§13.1: 73 + 2). N-5d: «Remark 2 of 4.4 is exact for j ≥ 2; for j = 1 READ it with this
  addition», right; LEMMA′ asks for less than the frozen (H2) in both cases.
- 9.3: L-4 = L-3 with the two recorded replacements, each old text once in L-3, at its recorded character; applied they give L-4
  byte for byte. The reason given for «1-9» (entry 9 changes a label; entry 8 is a record of the line only) is sound. «quotes 113
  found 113 notfound 0» and its control are the last lines of the pinned files. The pins hold.

### 15.4 Entry 10 (l. 1273-1368), sentence by sentence
- The relayed finding (l. 1277-1282) is this lane's message to the Lead of 2026-11-14 13:42Z: its sentences are in that message
  word for word (compared with my sent message; the ellipses are marked; the framing words «drops the local δ» are the relay's).
  That message gave k = 3..10; §14.3 has k = 3..12. «F-L3-1 was not on origin when this entry was written»: right (38d11668 reached
  origin at about 15:01Z; its commit time is 13:55:42Z, so «was not committed» is three minutes off, which that lane could not
  know). F-L3-1 is now §14.0 (l. 811) and §14.3 (l. 912-929) of this file at 38d11668.
- 10.1: the packet's rank clause is quoted verbatim (l. 98-99). «The lines L-1 to L-4 shortened this … to «β-ranks by Ξ-depth with
  ties broken by β-id»»: right, once in each of L-1 to L-4, in neither L-5 nor L-6. «Theorem EXP-IDEAL is about the genome G_k that
  rule R defines and gk.py builds … So no statement, proof, hypothesis or number changes; the LINE changes»: right, this is §14.3.
  The DATA: the lane's gloss.out (k = 3..12) against my own logs, 100 comparisons, 0 different: the triple's ranks are gk.py's br;
  rule R's run has 2^k − 2 steps; the old gloss gives 3 steps (ties by increasing β-id) and 1 step (decreasing), as in §14.3; its
  variant wire0 (the wires at depth 0) corresponds to one of the eight readings of §15.2, tested there by my own counter.
- 10.2: the three quotes are verbatim (R104's packet l. 224; RESULTS l. 9967, l. 13455). «RESULTS has the name, in R104 and in
  R117»: right; the quoted sentence itself is not in docs/RESULTS.md.
- 10.3: L-5 = L-4 with the three recorded replacements, each old text once in L-4; applied they give L-5 byte for byte. (1) «The
  rank gloss becomes the Lead's wording»: it is the wording of §14.3 (note N-7a). «it is rule R, the «Ξ-depth» of a wire being
  the table's «last» (2k + 5); and the variant wire0 above shows that the other reading of a wire's depth gives the same run»:
  right, and it holds for all eight readings. (2) and (3): right. «quotes 117 found 117 notfound 0» and its control are the last
  lines of the pinned files. The pins hold.

### 15.5 Entry 11 (l. 1370-1443), sentence by sentence
- The introduction (l. 1371-1375) is about the second referee's Addendum 4 and the Lead's relay of it: not checked (§15, head).
  That the second referee found the failing clause of entry 10 independently is the Lead's statement to this lane as well (its
  messages of 2026-11-14); this lane did not read that report.
- 11.1: «entry 6 (9.15) has wrong 0 at k = 13 on engine 1 … engine 2 was not run at k = 13»: right (n5_k13.out: wrong 0, no
  columns of a second engine; §13.5). The untagged «for k ≤ 12 this is DATA» is entry 2 (e)'s sentence (l. 234) with a small f.
- 11.2: the four phrases of R124 are verbatim in RESULTS l. 15371. «R117's title line has R15 (d), not (c)»: right (l. 13362: «and
  RESULTS R15 (d) for termination only»). The new parenthesis: §15.2 row D. «one clause added by me from the same line of R124
  (all under the standing SPEC premise 1E-N3), so that what the replaced words «same standing premises» said is not lost»: right,
  and needed. «READ the label of Corollary EXP-N5′ in entry 3 and in entry 9 (9.1) the same way … completed by RESULTS R15 (c) for
  Lemma TERM-XI, and RESULTS R117 (f) is a premise of EXACT-L only»: right (§15.6). «No proof changes: entry 3's proof uses the
  two statements of R124 as landed, whatever their premises are»: right.
- 11.3: the quote of this lane's first review is verbatim (c881709b l. 259-260, in item E-5, l. 257-261, of §5.3). **As the lane
  that the clause names, I confirm it**: in that review CAUSAL is stated (l. 203-204) and proved (from l. 205), LEMMA′ is stated
  (l. 219-225) and proved (l. 226-239), and STABLE's step form is stated (E-5) with no proof of its own; its proof in entry 4.2
  begins «The frozen proof (l. 258-262), with «key-disabled» read as K4 reads it». So «stated by REFEREE 36, which also proved
  CAUSAL and LEMMA′, the proof of STABLE being the frozen one read in step form» is true, and «stated and proved» would not have
  been true of 4.2. «Both quoted signatures name STABLE»: right (the two quotations are in the line). Note N-7c on what else 4.2
  holds.
- 11.4: L-6 = L-5 with the four recorded replacements, each old text once in L-5; applied they give L-6 byte for byte. The
  bracket counts in the record (82 round pairs, 1 square pair, 6 guillemet pairs) are mine. «the five quotations inside L-6»: the line has six
  guillemet pairs; the record does not count «stuck». «quotes 122 found 122 notfound 0» and its control are the last lines of the
  pinned files. The pins hold.

### 15.6 Does ENDGAME-3-N5 need TERM-XI (and so RESULTS R15 (c))? Yes
The sentences, located by line in R124's packet (the proof of record) and in RESULTS R124 as landed (own script, trunk aeb90ac1):
```
@@S6:TERMXI@@
```
- The proof of record. The packet's premise [TERM] is RESULTS R15 (l. 71). Lemma TERM-XI (l. 171: both runs terminate) is proved
  «By [TERM] (c)» (l. 175). Theorem ENDGAME-3 (l. 177) is proved from «By TERM-XI the run stops» (l. 179): without termination
  there is no first fallback F and no «exactly F + 2 iterations». Theorem ENDGAME-3-N5 (l. 182) is «The same for N5 (SPEC S4a).
  Proof: identical», so it uses TERM-XI's N5 half in the same place. Corollary EXACT-L (l. 184-187) is REACH3 plus ENDGAME-3-N5.
- The landed text says the same: R124 lists «(Lemma TERM-XI) both runs terminate» before the two theorems, and among its premises
  «RESULTS R15 (c) («every non-empty switch of improvements goes strictly up in ≺») for TERM-XI; RESULTS R117 (f) for EXACT-L only».
- So both clauses of Corollary EXP-N5′ (the count, through EXACT-L; the fallback, through ENDGAME-3-N5 with EXACT-L) rest on
  TERM-XI and through it on R15 (c); R117 (f) enters through EXACT-L only. L-6's parenthesis says exactly this. (R15 (c) is
  not the R15 (d) of R117's title line; entry 11.2 keeps the two apart correctly.)
- This is a reading of the proofs as written and landed. I did not look for a proof of ENDGAME-3-N5 that avoids TERM-XI; the
  line cites R124 «as landed», so the landed premises are the ones to name.

### 15.7 Notes (no statement affected)
- N-7a (entries 9.1 and 10.3): the label N-5e is called «the Lead's name for it», and the new gloss «the Lead's wording». Both
  come from this lane (N-5e: my message to the Lead of 2026-11-13, sent at 19:18Z by the session log, and §14 since 38d11668;
  the wording: my message of 2026-11-14 13:42Z and §14.3), relayed by the Lead. The entries' other statement, that the label N-5e
  «is not in the referee's file at 9ec40ff9», is right (0 occurrences).
- N-7b (entry 11.2): «every word of it R124's» is loose: the four named items are in R124's words; the connecting words («with
  R124's premises as landed», «among them») are the line's. In R124 the S1 tie-breaks stand under «it uses», not under
  «premises»; they are part of the candidate's SPEC, which the corollary is about, so the line assumes nothing by listing them.
- N-7c (entry 11.3 and the tail): entry 4.2 holds more than the step form: two further clauses («hence REST_i(b) under s⁺,
  C_i(s⁺) = 0 and E_i(s) = 0. Consequently, … s⁺ = s on U_i») and their proof by induction on m. They are the author lane's own
  (not referee-originated), so the tail need not name them; both signatures the tail quotes cover 4.2 as printed.
- L-n2 (§14.6) stands as a remark: the tail quotes this lane's verdicts of stage 1 and stage 4 and does not cite §14.3. It is true
  as written; the reading of (R3) that both signatures now share is in the second referee's sentence, which the tail quotes
  («(R3)'s range read as t − 1 ≤ τ < last (F-1)»), and this lane's acceptance of it is §14.3.
- Open for a successor of that lane, by the entries' own words: the quotations of §14 (entry 10) and of Addendum 4 (entry 11) «by
  commit and line». For §14: this file at 38d11668, l. 811 and l. 912-929.

### DONE / FINDINGS / NEEDS (stage 5b, part (ii))
- DONE: entries 9, 10, 11 read in full and checked sentence by sentence; L-4, L-5, L-6 rebuilt from L-3 by the recorded
  replacements; L-6 byte-tested, its seven replaced texts held against the sources, its DATA clauses against the pinned files;
  own tests gloss2 (eight readings of the new gloss) and termxi (docs/referee/scratch/gkx6.py, gkx6_quotes.py, gkx6_summ.py;
  logs gkx_logs/s37_gloss2, s37_e9_*, s37_linechain, s37_line_L6, s37_linedata_L6, s37_termxi.out; regenerate: `bash
  docs/referee/scratch/gkx_logs/s37_run.sh`, then gkx_fill.py).
- FINDINGS: (1) entries 9, 10, 11 right; (2) L-6 = L-3 with seven replaced texts, each agreeing with its source; F-L3-1 and N-5e
  closed; (3) ENDGAME-3-N5 needs TERM-XI and so R15 (c), in the proof of record and in the landed text; (4) the tail's sentence
  on STABLE confirmed by this lane; (5) notes N-7a, N-7b, N-7c; L-n2 stands as a remark; (6) not checked: what entry 11 says of
  the second referee's Addendum 4, and the Lead's messages to L-RED-B.
- NEEDS: none from this lane for P-N5-EXP. (Lead) the landing; CHECKER's exact-commit re-run of the lane's tools is not replaced
  by this report.

### 15.8 The final line of this report
**P-N5-EXP: SIGNED with fixes entries 1-11; line L-6 (sha1 1e0ff12d51da7a4ee1aad12ed0fd9119a097896b) SIGNED as the RESULTS line.**
