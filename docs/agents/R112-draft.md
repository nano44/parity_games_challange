# Draft RESULTS R112 (Lead; first fill 2026-11-06T06:07:58Z on line L-2 (draft sha1 35856ab5, CHECKER C123 96b7f8a1: FAIL E-1, E-2; G-0: C123 is right); SECOND FILL 2026-11-06T08:45:53Z by date -u (subagent) on P-TR3 line L-3, experiments/comp/box27/P-TR3-line-L3.txt, l-comp 9c70c980, sha1 d87bb3f062115ccf13164465395ef0187ccda7cf) — to CHECKER C123 Add. 1
SECOND FILL (2026-11-06T08:45:53Z by date -u, subagent; for CHECKER C123 Add. 1). Read at the origin heads fetched at its start (git
fetch, 2026-11-06T08:2xZ): l-comp 9c70c980 (its parent dd4a55c6 holds L-3 and fixes entry 2; 9c70c980 changes only entry 2's word-diff
bullet of P-TR3-fixes.md, and L-3 is byte-equal at dd4a55c6 and 9c70c980), referee 1140096d (it holds §C add. 1 of R-P-TR3.md, the L-3
byte test; its parent 365f22e1 holds Addendum 1, TR-G1 CLOSED), referee-2 ee1d6e18 (it holds Addendum 2 of R2-P-TR3.md, the L-3 byte
test), checker 8f1ae7b4 (its ancestor 96b7f8a1 holds docs/checker/C123.md, byte-equal at 8f1ae7b4); trunk 07112377 («Lead: P-TR3 L-3 to
byte tests; L-RED 51 check; L-NEW 55 park order; log»), pushed. Local trunk 4eb26876 = four merges (--no-ff, none an ancestor of
07112377 before) into 07112377: 7ec75c1b (l-comp 9c70c980), 66b46083 (referee 1140096d), e1e3a8e9 (referee-2 ee1d6e18), 4eb26876
(checker 8f1ae7b4); then the commit holding this file. Not pushed; dd4a55c6, 9c70c980, 365f22e1, 1140096d, ee1d6e18 and 8f1ae7b4 are NOT
ancestors of origin trunk 07112377 (git merge-base --is-ancestor); the Lead pushes trunk before landing. R111 IS LANDED: RESULTS R111
since e751969c (2026-11-06 07:16Z, CHECKER C124 18aa6728), and GAPS l. 11 ends with its UPDATE. RESULTS (sha1 e3bf07f3…, 12,487 lines),
GAPS (sha1 126d32f8…, 23 lines) and TARGET.md are byte-equal at e751969c, 07112377 and the local trunk (git diff, empty). So R112 goes
directly after R111's landed block (R111 l. 11,598-11,907, blank l. 11,908) and before «**Erratum E-1**» (l. 11,909); the first fill's
(0), (9) and Addendum (9), which simulated R111's landing, are superseded by Addendum 2 (8), run on RESULTS and GAPS as they are.
RESULTS R104's and R110's premise quotes still occur once each, at l. 9864 and l. 11323 (prem112.py re-run, fill2/prem112b.out). New
sources: docs/checker/C123.md (96b7f8a1, 2026-11-06T06:51:33Z, 142 lines, sha1 5fe8c8cff524ee9908b7e4cd5d71525e893f8abd): FAIL E-1 (the
packet name and the lane label in the title; L-3 = L-2 with one deletion, §5) and E-2 (the body's TR-G1 sentences after REFEREE's
Addendum 1; exact texts (a)-(c), §5), G-0 «C123 is right», G-T and G-U PASS, G-12 a note, everything else PASS; expected L-3 sha1
d87bb3f0… (§5) and rebuilt UPDATE sha1 21ab6559… (§4); line L-3, experiments/comp/box27/P-TR3-line-L3.txt (l-comp dd4a55c6,
2026-11-06T07:36:20Z, the file's only commit; unchanged at 9c70c980; sha1 d87bb3f062115ccf13164465395ef0187ccda7cf with newline, 1,682
bytes, = C123 §5's expected values); fixes entry 2 (experiments/comp/box27/P-TR3-fixes.md l. 75-86 at 9c70c980, F7; file 86 lines, sha1
38b97e59869572c85d6f680c935c4253df4e23c9, l. 1-73 = entry 1's file, by script); REFEREE's Addendum 1 (docs/referee/R-P-TR3.md l.
207-221, 365f22e1, 2026-11-06T06:15:35Z, file sha1 c31d4281068e6dce8ac2327f9ff9fa77db475d0b, 221 lines, l. 1-205 = fadbb9a0's, by cmp;
log scratch/t3r_logs/tr3_rest13.txt): l. 218 «TR-G1 is CLOSED.», l. 219 «TR-G2 stands», l. 220 «It is true and conservative, so no L-3
is needed»; REFEREE's byte test of L-3 (R-P-TR3.md §C add. 1, l. 223-234, 1140096d, 2026-11-06T08:04:04Z, file sha1
15f3a22ed607b277ebc5f7a92af5acf3ccfe2c59, 234 lines, l. 1-221 = 365f22e1's, by cmp: l. 230 «L-3 is byte-EQUAL to it (cmp).», l. 234
«Verdict: L-3 MATCHES. P-TR3 stays SIGNED as machine-certified; TR-G1 is CLOSED (Addendum 1).»); REFEREE-2's byte test of L-3
(docs/referee-2/R2-P-TR3.md Addendum 2, l. 164-174, ee1d6e18, 2026-11-06T08:04:07Z, file sha1 cd3b3453fd5119f6658a6ce1f8a645925d38c592,
174 lines, l. 1-162 = 7ff32432's, by cmp: l. 168 «**Fixes entry 2: CORRECT.**», l. 170 «**Line L-3: MATCHES.**», l. 174 «My verdicts
stand.»). My byte test of L-3 (fill2/l3rel112.py, rc 0): the prefix parsed by script from C123 §5 l. 91, «P-TR3 [lane: EXACT-SAT + CERT]
» (31 characters); L-2 starts with it and holds it once; L-2 minus it = L-3 (True); 13 «(» / 13 «)», depth never negative; 0 "|"; 0 «[»;
one « — »; «2026» once. My check of Addendum 1's log against the lane's record (fill2/rest13ck.py, rc 0): 13 cubes (0-4, 6-8, 11-15),
each with cnf sha1, proof sha1 and proof bytes equal to log/R_d3_L9_cert.txt and «s VERIFIED» by ref_rup; with §3's cubes 5, 9, 10 all
16; lemma counts differ from the record only on cubes 1, 3, 8, as Addendum 1 l. 212-214 states. The E-2 texts were parsed by script from
C123 §5 (fill2/c123txt.py: wrapped lines joined by single spaces, outermost guillemets) and applied verbatim; each old string occurred
once in the entry block. Re-runs: the UPDATE rebuilt from L-3 (fill2/upd112b.py: upd112.py's procedure with the one G-U adaptation,
unchanged, run on L-3; its R111 control now compares with R111 as LANDED on GAPS l. 11, so the 15 controls are the landed UPDATEs of
R97-R111, byte for byte, True; it equals the first fill's UPDATE with «P-TR3 [lane: EXACT-SAT + CERT] » deleted after «LANDED: », True;
sha1 = C123 §4's 21ab6559…, True); the quote sweep, the stale-status grep, the word diff and the landing simulation (Addendum 2).
Changed at this fill, and nothing else: this header line and this paragraph; the title (L-3); in the entry, Object (the packet identical
at 9c70c980, fixes entry 2, the line of record L-3 without the lane label, line history, the L-3 byte tests), Claims (L-3), What rests
on the machine (iv) (C123 E-2 (a), verbatim), Premise (L-3), Fixes (entry 2: the header, F7, the closing sentence), Honest limits (ii)
(C123 E-2 (b), verbatim), Data (L-3's DATA parenthesis), Signatures (C123 E-2 (c), verbatim; REFEREE §C add. 1, REFEREE-2 Addendum 2,
the lane commits), INDEPENDENCE (L-3), TARGET.md diff (L-3); the GAPS preamble and the UPDATE (rebuilt from L-3); the digest of Addendum
(10); Addendum 2 (new). The line's counts «REFEREE 3 cubes, REFEREE-2 1 cube» are unchanged (C123's optional change not taken, fixes l.
85-86); the body gives the final TR-G1 state in (iv). The FIRST FILL text below (from FIRST FILL (this text) to (14)) and Addendum
(1)-(9) are kept byte-unchanged as the record of the fill on L-2: where they call L-2 the title line or the current line, flag the lane
label in the title (G-L, D-1), say that no L-3 exists, give TR-G1 as open on 13 cubes or the announced REFEREE addendum as not on origin
(G-R), simulate R111's landing, or give the first fill's line numbers, counts and UPDATE sha1, they describe draft 35856ab5 at 06:07Z;
C123 ruled its flags G-0 (C123 right), G-L (E-1), G-R (E-2), G-T and G-U (PASS) and G-12 (note) as above, and the entry block follows
L-3.
FIRST FILL (this text). Read at the origin heads fetched at its start (git fetch, 2026-11-06T05:3xZ): l-comp 159df067 (its ancestor
d3e3cde8 holds L-2 and fixes entry 1; 159df067 changes no P-TR3 file: P-TR3.md, P-TR3-fixes.md, L-1, L-2, ENCODING.md, drup.c, cnf.py,
mkproof.py, sim.py, out/R_d3_L8.json and log/R_d3_L9_cert.txt are byte-equal at d3e3cde8 and 159df067, by sha1), referee 6f0daf60 (its
parent fadbb9a0 holds §C of R-P-TR3.md; 6f0daf60 leaves R-P-TR3.md byte-equal), referee-2 ea08029d (its parent 7ff32432 holds Addendum 1
of R2-P-TR3.md; ea08029d leaves it byte-equal), l-new 432edf82, checker 9c9b03b7; origin trunk 65231422 («Lead: P-TR3 L-2 MATCHES at
REFEREE; P-IDEAL-ALIGN signed by REFEREE (AL-L1); SUM_2 DEAD (L-SI); log»). Local trunk = five merges (--no-ff) into 65231422: c54f19b8
(l-new), 6b95c066 (l-comp), 02d0f872 (referee), 1d689e9a (referee-2), 7ad0389c (checker); then 285e5061 (the R111 second fill,
docs/agents/R111-draft.md only) and the commit holding this file. Not pushed. RESULTS (sha1 90dd5827fa59f504fa0f94a7b61aad46f834d5a1,
12,176 lines), GAPS (sha1 d608ac714c702ee07218e3d73955d71eecb1d28b, 23 lines) and TARGET.md are byte-equal at d056db87 (R110's landing,
the last commit on RESULTS and GAPS), 65231422 and the local trunk. R111 (docs/agents/R111-draft.md, second fill 285e5061) is NOT
landed; this draft assumes it lands first (placement (0), UPDATE (9), landing simulation Addendum (9)).
Sources read: the packet experiments/comp/box27/P-TR3.md (frozen d03d8370, sha1 cab32c0ee6e694dbfc345e533ab267b2ced52ac5, 125 lines;
unchanged at d3e3cde8 and 159df067), line L-1 (d03d8370), fixes entry 1 and line L-2 (d3e3cde8), ENCODING.md (d3e3cde8 = 138ae99d's; and
6f19564f's), README.md, experiments/comp/check.sh, out/R_d3_L8.json, log/R_d3_L9_cert.txt and log/R_d3_L9_cubes.txt (d3e3cde8); drup.c,
cnf.py and mkproof.py were built or run, not re-audited; drup2.c, sim.py, pinck.py and bf2.c were not opened; REFEREE successor 24's
docs/referee/R-P-TR3.md (report 5a5b94cf, §C fadbb9a0; l. 1-171 at fadbb9a0 = the report, by cmp) with
scratch/t3r_logs/tr3_regen_check.txt and dimacs_sha1.txt (ref_rup.c, t3r_dimacs.py and neg_tests.txt not opened); REFEREE successor 24's
encoding audit docs/referee/R-T3R-audit.md (776d0fdf; §C bfeca123; Addendum 1 5c02d44d; Addendum 2 ece8c4ee); REFEREE-2 successor 28's
docs/referee-2/R2-P-TR3.md (report 60e24158, Addendum 1 7ff32432; l. 1-134 at 7ff32432 = the report, by cmp; its tools
R2-P-TR3/fuzz_drup.py and r2rup.c not opened); REFEREE-2 successor 27's encoding audit docs/referee-2/R2-T3R-audit.md (d1c4a530; its
tools not opened); RESULTS R104 (title l. 9864), R110 (l. 11323-11596), Erratum E-1, E-2 and the Dead-ends section; GAPS l. 11;
DECISIONS D1 and docs/decisions/D001-launch-brief.md, L25, L41-L43; docs/agents/LEAD-STATE.md (2026-11-06 entries to 05:11Z);
docs/checker/C116.md, C122.md, C124.md and notes/CHECKER.md (9c9b03b7); docs/agents/R110-draft.md and R111-draft.md (the models of this
draft).
Re-runs (scratch /tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad/r112, from a git
archive of d3e3cde8's experiments/comp, nothing written into the repository): (a) all 16 d 3 cube DIMACS rebuilt in memory with cnf.py
f1f803ae (d3e3cde8) and with cnf.py fd882af1 (git show 557b045b), env SYM=1, W=R, CUBE as mkproof.py sets it, ISO / FREE0 / P / KF /
RUN2 / XCUBE unset (dimacs112.py): 16/16 sha1 equal to the packet's §3 and §4 tables and to REFEREE's t3r_logs/dimacs_sha1.txt, both
versions byte-identical; each 58,896 variables, 204,036 clauses, 0 empty clauses, 69 units; (b) the certificate records (certck112.py):
the §4 table equals log/R_d3_L9_cert.txt field by field (16/16), the sums are 11,353,990 lemmas and 19,694,959,174 proof bytes, the
CaDiCaL times sum to 4,946.2 s, log/R_d3_L9_cubes.txt has 16 UNSAT lines; (c) experiments/comp/check.sh (05:53:45Z, rc 0: «box27
witnesses replayed: 5, failures: 0»); (d) my own simulator mysim112.py, written from the R104 model text that packet §1 quotes (no lane
or referee code imported), on out/R_d3_L8.json: in 𝓛^R_3, T = 8 from its stored start with all 9 states equal to the stored ones, stop
«opt», maximum 8 over all 64 starts; (e) drup.c (sha1 2d4b8eab…, built here with gcc -O2) on fresh d 2 files from mkproof.py: the d 2 L
5 cube 0 UNSAT proof «s VERIFIED (5730 lemmas RUP-checked)» with deletions applied and with IGNDEL=1, the SAT d 2 L 4 formula with its
solver «proof» and the L 5 proof cut to its first 3,000 lines «s NOT VERIFIED: no refutation reached», and the L 5 proof without
deletion lines and with every 7th remaining line removed «s NOT VERIFIED: lemma 7 is not RUP» (the packet's own holed proof gives lemma
10; my holes differ); (f) cube 10 regenerated with mkproof.py (python3 -I mkproof.py 3 9 10 DIR glucose4, d3e3cde8;
2026-11-06T05:54:50Z-2026-11-06T05:57:52Z): DIMACS sha1 924ae011…, Glucose 4 UNSAT in 169.8 s, proof sha1
cae6998bd94b78005931ee2faff7eaffc3c122fc and 851,461,087 bytes, both equal to the packet's row 10 (Glucose is deterministic here, as
REFEREE and REFEREE-2 found); drup.c (deletions applied) «s VERIFIED (485366 lemmas RUP-checked)»
(2026-11-06T05:57:52Z-2026-11-06T06:07:34Z; = the row's 485,366); proof deleted after the check (cube10.sh, cube10.out); (g) the L-1 →
L-2 byte test and token diff (wdiff112.py); the premise quote test (prem112.py); the UPDATE build with 15 controls (upd112.py); the
quote sweep, the line-precise check and the landing simulation (chk112.py, lp112.py, sim112.py).
TRUNK STATUS (git merge-base --is-ancestor at 05:4xZ): d03d8370, d3e3cde8, 159df067, 5a5b94cf, fadbb9a0, 6f0daf60, 60e24158, 7ff32432
and ea08029d are ancestors of the local trunk and NOT of origin trunk 65231422; 776d0fdf, bfeca123, 5c02d44d, ece8c4ee, d1c4a530,
6f19564f, 557b045b and d056db87 are on both. The Lead pushes trunk before landing. The body makes NO statement about trunk (C113 E-2).
LESSONS APPLIED. C113 E-1: the title is L-2 verbatim with no insertion (G-L). C114 Add. 1 E-1: the UPDATE head carries «<DATE>». C115
E-1: the premise route is checked against what RESULTS records (G-4; prem112.py, 1 hit each). C116 G-1, C118-C122 §4, C124 §4: the
UPDATE rule of R105 / R111, with one adaptation, flagged (G-U). C117 E-1 / E-2: no sentence wider than signed; DATA scoped as measured;
the witness inlined. C118 E-1: no stale status sentence; the entry calls nothing «pending» (the only «PENDING» is the title fill). C118
§3: every DEFINITION in the title line diffed against RESULTS R104 / R110, the packet and the fixes (G-2). C120 §5 / C121 §5 / C122 E-2
/ C124 E-1 (DATA unit and set): every DATA count is tested against the tool or record that produced it (G-9). C122 G-0: parentheses
balanced (G-1). C122 E-3: the source note names every proof-carrying file (G-1). C119 E-1: every «referee X did Y» is checked against
that referee's file (line-precise check, Addendum (5)). REFEREE fadbb9a0 R-P-IDEAL-KEYS l. 241-242 «Lesson: test each DATA clause
against the tool's counter code (unit and set), not only against the packet's §8 wording.»: applied to every count (G-9).
to check: FLAGS FIRST (G-0 to G-14; five of them are for the Lead or CHECKER: G-0 (number), G-T (the tag: first machine-certified
entry), G-L (a lane label inside the verbatim title), G-U (one adaptation of the UPDATE rule), G-R (TR-G1 state, and nothing about an
announced addendum)), then the CLEAN items and (0)-(14). A NOTE FOR THE LEAD that is NOT part of this entry: G-C (R110's CONDITIONAL).
- G-0, THE CHECKER NUMBER. C123 is reserved for P-TR3: C124 l. 2 «C123 stays reserved for P-TR3 (draft G-0).», l. 99 «G-0 (the number):
  C124 is right. C123 is reserved for P-TR3 (Lead 02:26Z).»; notes/CHECKER.md (9c9b03b7) l. 12 «NEXT: C123 = P-TR3 («T^R(3) = 8»,
  L-COMP), when the Lead routes it.». docs/checker/C123.md does not exist at 9c9b03b7, and «C123» occurs 0 times in RESULTS and GAPS.
  This draft uses C123 (title fill, UPDATE head, GAPS preamble).
- G-T, THE TAG (FLAG; precedent found, tag kept). R112 is the first RESULTS entry whose main statement rests on a machine computation.
  Precedent read: (i) RESULTS l. 2 «Each entry: label (formalized | refereed-only), statement, commit SHA, referee reports, CHECKER
  report.»; (ii) the owner's launch brief, docs/decisions/D001-launch-brief.md l. 92 «Only then does it enter docs/RESULTS.md, labelled
  formalized or refereed-only.»; (iii) CLAUDE.md «A claim is a result only when Lean checks it (no sorry, allowed axioms only) or two
  referees signed it with its gaps listed.»; (iv) all 110 landed titles carry «[refereed-only]» (by script; no other tag, no «[lane», no
  «machine» tag); (v) machine items so far entered RESULTS only as a listed premise or gap: R110's DEAD (g) is «CONDITIONAL DEAD
  (premise T^R(3) ≤ 8, machine)» with the machine premise named in the line («CaDiCaL UNSAT on L-RED's encoding, not Lean, not
  refereed»); the Dead-ends row DE2 cites «strong k=4 UNSAT, LRAT-verified, two solvers»; (vi) Lead reading L25 «Standard for SAT data
  points: UNSAT by >= 2 independent solvers; no LRAT for now.» (met: CaDiCaL 1.9.5 and Glucose 4 at the lane, CaDiCaL 1.9.5, Kissat
  4.0.4 and Glucose 4 at REFEREE, CaDiCaL 1.9.5 at REFEREE-2 27). So the only labels the ledger has are formalized and refereed-only;
  P-TR3 is not formalized and is signed by two referees with gaps listed (REFEREE TR-G1, TR-G2; REFEREE-2 TR3-G1, TR3-G2), so the tag is
  «[refereed-only]», and the machine character is carried by the line itself («a machine statement: …; not Lean») and by the body
  (Claims, "What rests on the machine", Honest limits (i)-(iii)). REFEREE-2 l. 25 asks: «Any citation must say «machine, CERT by an own
  RUP checker».»; the line says «a machine statement» and «accepted by the own forward RUP checker drup.c», and the body says it in
  those words (Claims (a)). No tag differs from the brief's; nothing to change unless the Lead or CHECKER wants a third label, which
  would be an owner-level change of RESULTS l. 2 and D1 l. 92, not a CHECKER item.
- G-L, A LANE LABEL INSIDE THE VERBATIM TITLE (FLAG for CHECKER). L-2 begins «P-TR3 [lane: EXACT-SAT + CERT] In the IDEAL model», so the
  title reads "### R112 [refereed-only] P-TR3 [lane: EXACT-SAT + CERT] In the IDEAL model …": a packet name and a second bracketed label
  inside a RESULTS title. No landed title carries a packet name or a lane label (by script on RESULTS: «[lane» 0 times; the 110 titles
  start after «[refereed-only] » with a statement). The lane and REFEREE both call it a lane label: fixes l. 70-71 «The tag «[lane:
  EXACT-SAT + CERT]» is a lane label; the Lead sets the RESULTS tag (REFEREE TR-L1).»; REFEREE l. 148 ««[lane: EXACT-SAT + CERT]» is a
  lane label, not a RESULTS tag; the Lead sets the tag.». Neither referee required removing it, and both MATCHED L-2 with it. Per the
  brief (and C113 E-1) the title is L-2 verbatim. CHECKER to rule: (a) PASS as verbatim (the RESULTS tag is «[refereed-only]», and
  «[lane: …]» reads as the lane's own label for its evidence class); or (b) an E-item, fixed by one L-3 = L-2 with «P-TR3 [lane:
  EXACT-SAT + CERT] » removed at the start (one deletion; both referees byte-test; the UPDATE and the title are rebuilt by the same
  scripts). Nothing else in this draft depends on the choice.
- G-U, THE UPDATE RULE, ONE ADAPTATION (FLAG). The R105 / R111 procedure drops the two scope sentences «G-N5-TIME stays OPEN» and «not
  M3, not a step-4 pass, not a TARGET.md claim» from the tail and appends «. G-N5-TIME stays open.». L-2's tail has «; not Lean; not a
  TARGET.md claim; G-N5-TIME stays OPEN»: its scope sentence is the shorter «not a TARGET.md claim». upd112.py drops «; G-N5-TIME stays
  OPEN» and «; not a TARGET.md claim» and KEEPS «; not Lean» (a statement about the evidence, not a scope sentence). Cross-checks: a
  direct build (head + «LANDED: » + body + «: » + the tail with the DATA parenthesis opened and the two sentences dropped) is equal
  (True); the variant that keeps «; not a TARGET.md claim» differs only by that phrase (True). R111's adaptation for the «(DATA, »
  opening is reused unchanged. L-2 has no item labels and no DEAD clause, so build() moves nothing. Note: the rule « (2026-11-05) — » →
  «: » gives «T^R(3) = 8: a machine statement: CaDiCaL …» (two colons), as the rule makes it.
- G-R, TR-G1: THE STATE ON FILE (FLAG for the Lead). The line's counts are «REFEREE 3 cubes, REFEREE-2 1 cube» (fixes F4 l. 34-37, F6
  item 3; «Counts as on file in the two reports»). On file: REFEREE regenerated and re-checked cubes 10, 9, 5 (R-P-TR3 §3 l. 100-110;
  t3r_logs/tr3_regen_check.txt); REFEREE-2 cube 10 (R2-P-TR3 (2) l. 61-79); so 3 distinct cubes have independent re-checks, cube 10 by
  both (REFEREE-2 Add. 1 l. 161 «now: 3 + 1 cube proofs re-checked independently, cube 10 by both referees; the other 13 on the lane's
  record»). The body states exactly this. REFEREE's §C l. 205 announces more: no further R-P-TR3.md text is on origin claude/referee at
  this fill (head 6f0daf60; the file was last changed by fadbb9a0), so the body says nothing about it. If a TR-G1 addendum lands before
  R112 does, the Lead may cite it in the body as the final TR-G1 state; the line keeps the counts on file at fix time (LEAD-STATE
  05:11Z: «the line keeps on-file counts»). My own regeneration of cube 10 ((f) above) is draft DATA, not a referee check.
- G-C, R110's CONDITIONAL (NOTE for the Lead and CHECKER; NOT part of R112; nothing about it is in the entry). R110's DEAD (g) is
  «CONDITIONAL DEAD (premise T^R(3) ≤ 8, machine)»; R110's body names that premise as «a CaDiCaL UNSAT on L-RED's encoding, not Lean and
  not landed» and says «the label changes only through a separately landed item» (RESULTS R110, Honest limits (iii)). With R112 landed,
  the statement T^R(3) ≤ 8 is a landed RESULTS item (refereed-only, machine-certified, on L-COMP's encoding cnf.py, not L-RED's
  xcnf.py). Whether R110's «CONDITIONAL» can then be lifted is a separate erratum-style item for the Lead (L42 / L43 reading; both
  referees of R110 to confirm), not part of R112; this draft neither proposes nor implies it.
- G-9, DATA (the C120 §5 / C121 §5 / C124 E-1 check item: unit and set of every count, against the tool or record): MET. «16 cube
  UNSATs»: log/R_d3_L9_cubes.txt, 16 UNSAT lines (CaDiCaL); «16/16 VERIFIED proofs (11,353,990 lemmas)»: log/R_d3_L9_cert.txt, 16
  VERIFIED lines, lemma sum 11,353,990 (certck112.py) — both «cover «T ≤ 8» only»: they are the upper-bound evidence, not DATA of a
  further statement. «pinck.py's 0 disagreements on 450 random genomes»: packet §3 l. 53-54 «0 disagreements on 300 random d 2 and 150
  random d 3 genomes of 𝓛^R» (450 = 300 + 150; random 𝓛^R genomes, REFEREE l. 155, REFEREE-2 l. 114); «on the 128 start runs of the 2
  distinct length-8 genomes»: «all 64 starts of each of the 2 distinct length-8 genomes» (l. 54-56; 2 × 64); unit: one pinned (genome,
  start) per test, «SAT at L = T and UNSAT at L = T + 1» (l. 53-54); «cover only the agreement of the CNF with the simulator»: exactly
  what pinck.py tests (REFEREE-2 27 l. 47-48: «Its random genomes give mostly T 0-2; its long runs are all 64 starts of two T = 8
  genomes.»; the line claims nothing wider). «bf2.c's exhaustive maximum T = 4 on 𝓛^R_2 covers only the d 2 cross-check»: packet l.
  56-57. No count is stated for a wider set than its record. Both referees: REFEREE l. 154-156 «MEETS C120.»; REFEREE-2 l. 113-116
  «Every count names what it covers. ✓».
- G-1, TITLE SHAPE AND SOURCE NOTE: CLEAN (my script). L-2 is one line, 1,713 bytes, 13 «(» / 13 «)», depth never negative, 0 "|", one «
  — », «2026» once, two opening and two closing guillemets; the title adds the fill (14 / 14). Source note «(P-TR3,
  experiments/comp/box27/P-TR3.md with its fixes entry 1, experiments/comp/box27/P-TR3-fixes.md, and experiments/comp/box27/ENCODING.md;
  L-COMP successor 9)»: the lane's proofs (SYM, E1-E3, the cover, «Q(9) UNSAT ⇔ P-TR3» given the encoding) are in P-TR3.md §2 and
  ENCODING.md §1, §3 (packet §5 l. 113-114); the fixes file carries no proof (F1-F6 are citations, wording, a new tool outside the
  record, and L-2). Every proof-carrying file is named (C122 E-3; REFEREE §C l. 199 «TR-L2 MET», REFEREE-2 Add. 1 l. 160).
- G-2, DEFINITIONS DIFFED (my own diff; the C118 §3 lesson). (i) «the IDEAL model of RESULTS R104 (definition only, no theorem of R104
  used)»: R104's model text, which packet §1 l. 7-14 quotes verbatim (prem112.py: 1 hit in RESULTS, inside R104's block). (ii) 𝓛^R_3:
  L-2 «the 2-wide degree-2 ladders with levels 0, 1, 2 in L-RED's R197 W-convention, all acyclic Ξ-data, β's, gates and starts, ISO not
  assumed» against R110 «on acyclic Ξ-graphs, with 𝓦_d the genomes with levels 0, …, d − 1 whose level-0 movers are exactly two movers
  named 0 and 1, 𝓛^R_d ⊆ 𝓦_d the 2-wide degree-2 ladders in L-RED's R197 convention (movers 2l and 2l + 1 on level l, all of degree 2,
  no other movers, option k of a mover of level l ≥ 1 W-pointing to mover 2(l − 1) + k)» at d = 3: the same class (levels 0, 1, 2;
  «acyclic Ξ-data» = R110's «on acyclic Ξ-graphs»; Ξ-data, β's, gates and starts free in both; ISO is R110's property, not assumed). L-2
  does not restate R110's mover numbering; it cites R110's definitions («RESULTS R110's definitions of 𝓛^R_d and T^R(d) only»). «R197
  W-convention» is L-2's wording, not a quotation (R110: «R197 convention»); no meaning changes. (iii) T^R(d): «T^R(d) the largest
  number of steps over 𝓛^R_d and all starts», verbatim R110 (1 hit). (iv) T = R104's L(G), the number of steps of the run from the given
  start (packet §1 l. 18-19). (v) The encoding's class (ENCODING.md §1 l. 8-11) is the same, «ISO is NOT imposed». Both referees diffed
  the class against R110: REFEREE §4 l. 120-124 «The classes are the same; I checked both texts.», §C l. 181; REFEREE-2 (3) l. 82-89
  «are the SAME sets and the same maximum», Add. 1 l. 143.
- G-3, STRICT SYMBOL TEST (notes). Every symbol of L-2 is R104's (IDEAL model, genome, mover, option, Ξ-data, β, gate, start, step,
  run), R110's (𝓛^R_d, T^R(d), ISO, «L-RED's R197» convention), a file or tool named with its path (cnf.py, ENCODING.md, drup.c with its
  sha1, pinck.py, bf2.c), or a solver with its version (CaDiCaL 1.9.5, Glucose 4, «drat-trim» named as not used). «T» in «T ≥ 9», «T ≤
  8», «T = 4» is R104's number of steps (packet §1 l. 18). «cube» is defined by the line («16 cubes that cover every start up to one
  sound relabelling (both level-0 movers start on option 0)»); the cube is a fixing of s_0 on movers 2-5 (packet §2 l. 41-42). «REFEREE»
  and «REFEREE-2» are the fleet's referee lanes (both files named in the body).
- G-4, PREMISE ROUTE (the C115 E-1 class): CLEAN (prem112.py). Premises: RESULTS R104's definition of the IDEAL model (packet §1 l.
  7-14, 861 characters, 1 hit in RESULTS, inside R104's block, title l. 9864) and RESULTS R110's definitions of 𝓛^R_d and T^R(d) (fixes
  F1 l. 11-16, 446 characters, 1 hit, inside R110's title l. 11323). No theorem of R104 or R110 is used (L-2: «definition only, no
  theorem of R104 used», «only, no theorem of R110 used»). No lit note, no lane file as a premise (P-IDEAL-FLIP §1 is no longer cited:
  fixes F1, L-a). The machine part is not a premise from RESULTS: it is the entry's own evidence (G-T, Claims (a)).
- G-5, ERRATA (note). Erratum E-1 and E-2 (RESULTS) concern R105 items; R112 uses no R105 item. Not bearing.
- G-6, NAMES (note; by script on RESULTS 90dd5827 / GAPS d608ac71). «R112» 0 times in RESULTS and GAPS; L-RED has a box R112
  (notes/L-RED.md, «R112 (coupled relay chain, cpl tools, check.sh gate», a different object, not cited in RESULTS); «P-TR3» 0 times in
  RESULTS; «CERT» and «EXACT-SAT» are lane labels (packet l. 2-3); «TR-G1», «TR-G2», «TR3-G1», «TR3-G2» are the two referees' gap labels
  (and «T3-G1», «T3-G2» the encoding audit's), not GAPS rows. One body sentence (Honest limits (vii)) settles them.
- G-7, L41 (the C109 E-1 class): not triggered (my reading). The proofs (SYM, E1-E3, the cover) are the lane's (packet §2, ENCODING.md);
  the referees wrote their own checkers (ref_rup.c, r2rup.c) and simulators as verification tools, not as proof steps of the statement.
  Neither referee mentions L41.
- G-8, NO DEAD (note). L-2 kills nothing; no Dead-ends row ((14)).
- G-10, LEAD READINGS AND RULINGS (the C111 E-1 class): L-2 cites none. The body cites none as a premise; G-T and G-R quote L25 and the
  05:11Z LEAD-STATE entry as the Lead's words, labelled.
- G-11, STALE LANE TEXT (notes; nothing here lands). Packet §1 l. 15-18 («not landed terms; … (= RESULTS R110 once landed; P-IDEAL-FLIP
  is CHECKER C122s item.)»), §1 l. 22 «With the witness of §5», §4 l. 108 «drup.c is my own, unaudited tool» and ENCODING.md l. 5 «no
  DRAT/LRAT certificate was produced or checked» are stale; fixes F1, F2, F4 correct them (append-only). The entry quotes the packet
  only where the fixes leave it unchanged, and uses the fixes' texts elsewhere. ENCODING.md as audited by REFEREE-2 27 is 6f19564f's
  (sha1 2ba6b1a0…, 64 lines); at d3e3cde8 it is 138ae99d's (sha1 9e135abb…, 66 lines): the only change is l. 2-4 (the cnf.py note:
  «Later version 06f25e35 adds ONLY the env option XCUBE»), §1-§4 unchanged (git diff). README.md l. 2-3 still says «no proof
  certificate is checked» (box 27's general label); not cited.
- G-12, SHA1 PINS (the C110 F-1 / C116 G-3 class): experiments/comp/check.sh (d3e3cde8) replays the five stored box-27 witnesses only;
  it has no sha1 pins of the packet, the lines, the fixes, ENCODING.md or drup.c. Pins are in the text instead: the line pins drup.c
  («sha1 2d4b8eab…»), the packet pins cnf.py, the 16 DIMACS and the 16 proofs, the fixes pin drup2.c. C116 G-3 ruled the same absence
  for L-NEW «NOT required before landing». Note.
- G-13, THE REFEREES' ROUNDS (note). L-1 (221c81eb): REFEREE (5a5b94cf) SIGN as machine-certified, L-1 «NOT YET: REQUIRED TR-L1, TR-L2»
  (l. 20); REFEREE-2 (60e24158) SIGN WITH GAPS, L-1 «**does NOT match** as written» (l. 18). Fixes entry 1 (d3e3cde8): F1-F6, L-2 = L-1
  with four replacements (L-a / TR-L1, L-b / TR-L1, L-c / TR-L3, L-d / TR-L2). Second round: REFEREE §C (fadbb9a0) «Fixes entry 1 is
  CORRECT.», «L-2 MATCHES.»; REFEREE-2 Add. 1 (7ff32432) «**Fixes entry 1: CORRECT.**», «**Line L-2: MATCHES.**».
- G-14, WHAT IS NOT PROVED (note; for the reader of the entry). The upper bound is not a human-readable proof and not Lean: REFEREE l.
  138 «Not signed as a mathematical proof: no Lean, no human-readable proof.»; REFEREE-2 l. 20 «(each is a statement of what rests on
  the machine, not a hole in an argument)». The entry says this in Claims (a), in "What rests on the machine" and in Honest limits
  (i)-(iii).
- CLEAN AT L-2 (the pre-check against CHECKER's recurring items, by script on 11cd9acc):
  C106 E-1 (old line as current): L-2 is the current line; no L-3 exists (experiments/comp/box27/P-TR3-line-L3.txt absent at 159df067).
  C113 E-1 (title «verbatim» after an insertion): no insertion; the title is byte-equal to prefix + L-2 + fill (G-L).
  C113 E-2 (trunk status that goes stale): the body has no trunk statement (header).
  C114 Add. 1 E-1 (UPDATE date): <DATE> placeholder.
  C115 E-1 (premise route): G-4.
  C116 G-2 (name clash): G-6, one body sentence.
  C117 E-1 / E-2 (scope; instance under-specified): the witness genome is inlined in Claims (b) (every option field, the start, the 9
  states).
  C118 E-1 (stale status sentence): no «pending» in the entry; the TR-G1 addendum is not mentioned (G-R).
  C120 §5 / C121 E-1 / C122 E-2 / C124 E-1 (DATA unit and set): G-9.
  C122 G-0 (parentheses): 13 / 13 in L-2, depth never negative (G-1).
  C122 E-3 (source note): G-1.
  «|»: 0 in L-2, 0 in the entry block, 0 in the UPDATE (by script, Addendum (3)).
(0) PLACEMENT. R112 goes DIRECTLY AFTER R111's block, which lands first (from docs/agents/R111-draft.md, second fill), and before
«**Erratum E-1**». docs/RESULTS.md at the local trunk (= d056db87's): «### R110» l. 11323, its block to l. 11596, blank l. 11597,
«**Erratum E-1**» l. 11598. After R111's landing (simulated, Addendum (9)) R111 is l. 11598-11907, blank l. 11908, and R112 goes at l.
11909. If R112 lands before R111, it goes directly after R110's block instead; the entry text is the same.
(1) TITLE. The title is the line file experiments/comp/box27/P-TR3-line-L2.txt (l-comp d3e3cde81411a5487c588f3bd132451efc63abae,
2026-11-06T03:23:21Z, the file's only commit; sha1 11cd9acc14147fb7a3820e9a16c9cee15875e611 with newline, 1,713 bytes) verbatim, after
"### R112 [refereed-only] " and before ", CHECKER PASS (docs/checker/C123.md, checker PENDING)", nothing inserted. Title line:
1,761 characters, 1,791 bytes, sha1 33d321373feb191dc3135994aaffdbcf92ad479d (line without newline).
(2) LINE HISTORY: two lines. L-1 221c81eb20cb9f28aa41f07f6eb5d9af3879db92 (d03d8370, frozen with the packet, 2026-11-06T01:18:33Z, 1,357
bytes); L-2 11cd9acc (d3e3cde8, fixes entry 1 F6: L-1 with the four replacements L-a, L-b, L-c, L-d). My byte test (wdiff112.py): the
four «old» → «new» pairs parsed from fixes l. 51-59, each old string once in L-1 and each new string once in L-2, L-1 with them = L-2
(True); my token diff has 9 hunks, each equal to one line of F6's word diff (l. 61-69). Both referees byte-tested it: REFEREE §C l.
194-196 «Result: EQUAL to L-2 (sha1 11cd9acc…, 1,713 bytes).»; REFEREE-2 Add. 1 l. 155-157.
(3) THE LINE AT BOTH REFEREES. REFEREE successor 24, docs/referee/R-P-TR3.md: report 5a5b94cf (2026-11-06T02:39:17Z, 171 lines, sha1
a2ced7e8003bb31b09ca064a288e517434542047), §C fadbb9a0 (04:09:18Z, 205 lines, sha1 9976bac7b794c395cf5f2c9d5b6b18596dc842ad): «L-2
MATCHES.» (l. 203). REFEREE-2 successor 28, docs/referee-2/R2-P-TR3.md: report 60e24158 (02:39:25Z, 134 lines, sha1
79989749b1133cef9934ba5c08a4c4cdab2190be), Addendum 1 7ff32432 (04:13:09Z, 162 lines, sha1 8313172f1234447e91b0575e6b76883cf77e47a5):
«**Line L-2: MATCHES.**» (l. 155).
(4) CLAIMS SIGNED = the items below, each signed in BOTH referees' verdicts (REFEREE "## 0. Verdicts" l. 12-20, §5 l. 132-140, §C l.
202-205; REFEREE-2 "## Verdicts" l. 11-18, Add. 1 l. 161-162):
| item (source) | REFEREE (successor 24) | REFEREE-2 (successor 28) |
| --- | --- | --- |
| (a) T^R(3) ≤ 8 (packet §1 l. 21; §2-§5) | l. 15 «SIGN, as a machine-certified statement (scope in §5); gaps listed below» (TR-G1, TR-G2) | l. 14 «**SIGN WITH GAPS** (Opus 5.5, D12): gaps TR3-G1, TR3-G2 below» |
| (b) T^R(3) ≥ 8, witness out/R_d3_L8.json (packet §3 l. 51-52) | l. 118 «So T^R(3) = 8.»; §5 l. 134 «lower bound by an explicit instance» | l. 15 «**SIGN** (Opus 5.5, D12)» |
| (c) SYM, the cube cover, E1-E3 (packet §2; ENCODING.md §1, §3) | R-T3R-audit l. 19 «SOUND; the cubes cover every start»; R-P-TR3 §4 l. 116-117 | l. 16 «**SIGN** (Opus 5.5, D12)» |
| (d) drup.c sound as a refutation checker | l. 16 «SOUND (line-by-line audit, §1)» | l. 17 «audited: **SOUND** for the inputs used; robustness note D-1» |
| (e) the encoding cnf.py → R104 / R110 | l. 18 «FAITHFUL (R-T3R-audit; T3-G2 closed by R110)» | gap TR3-G2: rests on REFEREE-2 27's audit R2-T3R-audit.md, «which I cite and did not redo» |
Both, final: REFEREE §C l. 205 «P-TR3 stays SIGNED as machine-certified.»; REFEREE-2 Add. 1 l. 161-162 «My verdicts stand. Upper bound:
SIGN WITH GAPS TR3-G1 (now: 3 + 1 cube proofs re-checked independently, cube 10 by both referees; the other 13 on the lane's record) and
TR3-G2. Lower bound: SIGN.».
(5) OTHER TEXTS THE ENTRY DEPENDS ON: RESULTS R104's definition of the IDEAL model (title l. 9864; no R104 theorem); RESULTS R110's
definitions of 𝓛^R_d and T^R(d) (title l. 11323; no R110 theorem). Nothing else of RESULTS; no docs/lit; no machine premise from
elsewhere.
(6) PREMISE LABELS (stale-label test; RESULTS and GAPS at d056db87's version). RESULTS labels in L-2 (by script): «R104» 3, «R110» 2,
«R197» 1 (L-RED's convention as R110 names it). Each is a landed RESULTS entry or the name R110 itself uses. No GAPS label in L-2 except
«G-N5-TIME» (GAPS l. 11, open).
(7) SYMBOL TEST: G-3.
(8) FIXES AND STATUS NOTES (experiments/comp/box27/P-TR3-fixes.md, L-COMP successor 9, append-only, one entry, one commit d3e3cde8):
sha1 d7b33861ea3a6aecc0a069e43f6df8b53c3f28e3, 73 lines. F1 (TR-1) R110's definitions quoted verbatim (l. 9-19); F2 (TR-P3) §5 → §3 (l.
21-22); F3 (TR-P2) which cnf.py made which file (l. 24-28); F4 (TR-P3, stale notes) drup.c audited, the re-check counts, ENCODING.md l.
5 (l. 30-39); F5 (TR-P1, D-1) drup2.c, a NEW file outside the record (l. 41-47); F6 line L-2 (l. 49-73). Verdicts: REFEREE §C l.
180-193; REFEREE-2 Add. 1 l. 142-154.
(9) GAPS: G-N5-TIME (GAPS l. 11) stays open; L-2 bounds nothing polynomially and is not about a parity game. The proposed UPDATE (below
the entry) is built by upd112.py from L-2 by the R111 procedure with one adaptation (G-U); 15 controls: R97-R110's landed UPDATEs (GAPS
l. 11) byte for byte, and R111's UPDATE as drafted (docs/agents/R111-draft.md, second fill, unfilled) byte for byte.
(10) DATA of record = packet §3 (pinck, bf2, the replays) and §4 (the certificate records), NOT signed as DATA; the CERT records are the
evidence of (a). Re-runs at this fill: Re-runs (a)-(f) above. REFEREE re-ran: CaDiCaL 1.9.5 and Kissat 4.0.4 on all 16 cubes
(R-T3R-audit §4), Glucose 4 on all 16 (Addendum 1), 3 cube proofs regenerated and checked by drup.c and ref_rup.c (R-P-TR3 §3), 13
negative / positive tests (§2). REFEREE-2: drup.c fuzzed 12,902 runs, «**UNSOUND 0**» (l. 58); cube 10 regenerated and checked by drup.c
(both modes) and r2rup.c ((2)); REFEREE-2 27: CaDiCaL 1.9.5 on all 16 cubes, 414 pinned pairs against its own simulator (R2-T3R-audit
§4-§5).
(11) Discrepancies, recorded for CHECKER, no verdict affected: D-1 the lane label in the title (G-L). D-2 two colons in the UPDATE
(G-U). D-3 packet §2 names cnf.py fd882af1 while the proofs were made with f1f803ae: fixes F3; both build byte-identical DIMACS (my
rebuild (a): True). D-4 the packet's holed-proof negative test gives «lemma 10» (l. 79); my own holes give «lemma 7»; REFEREE's «every
7th lemma dropped» gives «lemma 7» (l. 89); different hole patterns, all NOT VERIFIED. D-5 ENCODING.md changed after REFEREE-2 27's
audit (l. 2-4 only; G-11). D-6 drup.c prints «vars 59059», its allocation size (REFEREE l. 42), not the 58,896 variables.
(12) Excluded: packet §3's DATA (pinck, bf2, the replays) as statements; §6 EXCLUDED; drup2.c (F5; «not the checker of record»); box
27's other results (T^R(2) = 4 as a statement, the T_k(m) table, T*(d), the d 4 cubes, L-SI's frame UNSATs); L-RED's xcnf.py encoding
(not audited by REFEREE, R-T3R-audit §C l. 173).
(13) Commits: lane (claude/l-comp): 557b045b (cnf.py fd882af1, the CaDiCaL cubes); 6f19564f (ENCODING.md, the audited version); 07cec839
(drup.c 2d4b8eab); d03d8370 (2026-11-06T01:18:33Z; freeze: packet cab32c0e, L-1 221c81eb); d3e3cde8 (2026-11-06T03:23:21Z; fixes entry
1, L-2 11cd9acc, drup2.c); 864f607a, 159df067 (notebook, L-SI certification tools; no P-TR3 file). Referees: claude/referee 2005aee7
(ref_rup.c, neg_tests), 5a5b94cf (report), fadbb9a0 (§C); 776d0fdf, bfeca123, 5c02d44d, ece8c4ee (R-T3R-audit and its §C and addenda);
claude/referee-2 d1c4a530 (R2-T3R-audit, successor 27), b1fbc8d4 (fuzz_drup.py, r2rup.c), 60e24158 (report), 7ff32432 (Addendum 1).
Checker: 9c9b03b7 (C124, which reserves C123).
(14) Placement: see (0). DEAD-ENDS ROWS: NONE (not drafted). R112 kills nothing.

### R112 [refereed-only] In the IDEAL model of RESULTS R104 (definition only, no theorem of R104 used), on 𝓛^R_3 (RESULTS R110's definitions of 𝓛^R_d and T^R(d) only, no theorem of R110 used: the 2-wide degree-2 ladders with levels 0, 1, 2 in L-RED's R197 W-convention, all acyclic Ξ-data, β's, gates and starts, ISO not assumed; T^R(d) the largest number of steps over 𝓛^R_d and all starts): T^R(3) ≤ 8, hence T^R(3) = 8 (2026-11-05) — a machine statement: CaDiCaL 1.9.5 UNSAT of the CNF query «some genome and start have T ≥ 9» (experiments/comp/box27/cnf.py, mapped clause by clause to R104 in ENCODING.md) on 16 cubes that cover every start up to one sound relabelling (both level-0 movers start on option 0), each cube also refuted by a Glucose 4 DRUP proof accepted by the own forward RUP checker drup.c (sha1 2d4b8eab…; no drat-trim; drup.c audited sound by REFEREE and REFEREE-2, its correctness still a premise; cube proofs regenerated byte-identically and re-checked independently: REFEREE 3 cubes, REFEREE-2 1 cube), and T ≥ 8 SAT with a witness replayed under two simulators; not Lean; not a TARGET.md claim; G-N5-TIME stays OPEN (DATA, each count naming the statement it covers: 16 cube UNSATs and 16/16 VERIFIED proofs (11,353,990 lemmas) cover «T ≤ 8» only; pinck.py's 0 disagreements on 450 random genomes and on the 128 start runs of the 2 distinct length-8 genomes cover only the agreement of the CNF with the simulator; bf2.c's exhaustive maximum T = 4 on 𝓛^R_2 covers only the d 2 cross-check) (P-TR3, experiments/comp/box27/P-TR3.md with its fixes entry 1, experiments/comp/box27/P-TR3-fixes.md, and experiments/comp/box27/ENCODING.md; L-COMP successor 9), CHECKER PASS (docs/checker/C123.md, checker PENDING)
- Object (L-COMP successor 9, box 27; frozen, unchanged during review): packet P-TR3, experiments/comp/box27/P-TR3.md, sha1
  cab32c0ee6e694dbfc345e533ab267b2ced52ac5, 125 lines (l-comp freeze d03d8370, 2026-11-06T01:18:33Z; identical at d3e3cde8 and
  9c70c980). Both referees measured the sha1 (REFEREE l. 6 «experiments/comp/box27/P-TR3.md: sha1
  cab32c0ee6e694dbfc345e533ab267b2ced52ac5, 125 lines;»; REFEREE-2 l. 6 «experiments/comp/box27/P-TR3.md sha1
  cab32c0ee6e694dbfc345e533ab267b2ced52ac5, 125 lines;»). Labels (l. 2-4): «Labels: EXACT-SAT (solver UNSAT, machine-checked, not Lean,
  not refereed),» «CERT (a solver proof checked by my own RUP checker), PROVED (lane: a short argument written out here), DATA. Not a
  TARGET.md claim.» Sections: §1 statement (l. 6-22), §2 method (l. 24-42), §3 evidence (l. 44-57), §4 certificate (l. 59-110), §5 «What
  is proven, and what rests on the solver» (l. 112-119), §6 EXCLUDED (l. 121-122), §7 TARGET.md diff (l. 124-125). The clause-by-clause
  map of the encoding to R104 is experiments/comp/box27/ENCODING.md (d3e3cde8, sha1 9e135abbd1a2…, 66 lines; §1-§4 as audited at
  6f19564f).
  Fixes: experiments/comp/box27/P-TR3-fixes.md, append-only, entry 1 (d3e3cde8; 73 lines, sha1 d7b33861ea3a6aecc0a069e43f6df8b53c3f28e3)
  and entry 2 (dd4a55c6, its word-diff bullet 9c70c980; 86 lines, sha1 38b97e59869572c85d6f680c935c4253df4e23c9, l. 1-73 unchanged).
  Entry 1: F1 replaces the packet's lane-file citation by RESULTS R110's definitions, quoted verbatim; F2-F4 correct stale packet text
  and name which cnf.py made which file; F5 adds drup2.c, a strict-parsing copy of drup.c, as a NEW file outside the certified record;
  F6 makes line L-2; entry 2 (F7) makes line L-3 (one deletion, CHECKER C123 E-1). The packet «is NOT edited; every correction is here.»
  (l. 2).
  The RESULTS line is L-3, d87bb3f062115ccf13164465395ef0187ccda7cf (experiments/comp/box27/P-TR3-line-L3.txt, l-comp dd4a55c6,
  2026-11-06T07:36:20Z, the file's only commit; unchanged at 9c70c980; 1,682 bytes). The title is L-3 verbatim, with nothing inserted
  (its date parenthesis «(2026-11-05)» and its source note are the line's own). The title carries no lane label and no packet name:
  L-2's opening «P-TR3 [lane: EXACT-SAT + CERT]», a lane label, not a RESULTS tag (fixes l. 70-71, REFEREE l. 148), is deleted in L-3
  (CHECKER C123 E-1); the RESULTS tag is «[refereed-only]», and the line states the machine character in words («a machine statement»,
  «not Lean»). L-3's parentheses balance (13 «(» / 13 «)»). Line history: L-1 (221c81eb, d03d8370, frozen with the packet); L-2
  (11cd9acc, d3e3cde8, fixes entry 1 F6: L-1 with exactly four replacements: L-a and L-b (REFEREE TR-L1, REFEREE-2 L-a, L-b) cite
  RESULTS R110's definitions of 𝓛^R_d and T^R(d), add «acyclic» and R110's definition of T^R(d); L-c (TR-L3) pins drup.c and states its
  audit and the re-check counts; L-d (TR-L2) names the fixes file and ENCODING.md in the source note; L-1 with the four replacements
  equals L-2 byte for byte, by my script); L-3 (d87bb3f0, dd4a55c6, fixes entry 2 F7: L-2 with exactly one deletion, the leading «P-TR3
  [lane: EXACT-SAT + CERT] » (31 characters, once, at the start; CHECKER C123 E-1), nothing else changed, the re-check counts included
  (fixes l. 85-86); L-2 minus that prefix equals L-3 byte for byte, by my script). L-2 MATCHES at both referees, each after its own byte
  test: REFEREE (fadbb9a0) §C l. 196 «Result: EQUAL to L-2 (sha1 11cd9acc…, 1,713 bytes).», l. 203 «L-2 MATCHES.»; REFEREE-2 (7ff32432)
  Addendum 1 l. 155 «**Line L-2: MATCHES.**», l. 156 «applying them in order gives a string byte-identical to L-2 (1,713 B)». L-3
  MATCHES at both referees, each after its own byte test against C123 §5: REFEREE (1140096d) §C add. 1 l. 230 «L-3 is byte-EQUAL to it
  (cmp).», l. 234 «Verdict: L-3 MATCHES. P-TR3 stays SIGNED as machine-certified; TR-G1 is CLOSED (Addendum 1).»; REFEREE-2 (ee1d6e18)
  Addendum 2 l. 170 «**Line L-3: MATCHES.**», l. 171 «L-3 equals L-2 with that prefix removed, byte for byte (1,682 B)». Both diffed the
  line's class and quantity against R110 (REFEREE §C l. 198 «TR-L1 MET: R110's definitions are cited, «acyclic» is added, and T^R(d) is
  defined verbatim from R110.»; REFEREE-2 Add. 1 l. 143); L-3 changes no definition (REFEREE §C add. 1 l. 233 «No statement or
  definition changes.»; REFEREE-2 Add. 2 l. 168-169).
- Claims signed (REFEREE successor 24 «(Opus 5.5, D15)», report 5a5b94cf, §C fadbb9a0; REFEREE-2 successor 28 «(Opus 5.5, D12/D20)»,
  report 60e24158, Addendum 1 7ff32432; encoding audits: REFEREE successor 24, R-T3R-audit.md 776d0fdf with §C bfeca123, Addendum 1
  5c02d44d, Addendum 2 ece8c4ee; REFEREE-2 successor 27, R2-T3R-audit.md d1c4a530). Every item is about R104's IDEAL model on acyclic
  Ξ-graphs, on the class 𝓛^R_3 of RESULTS R110 (levels 0, 1, 2; movers 2l and 2l + 1 on level l, all of degree 2; option k of a mover of
  level l ≥ 1 W-pointing to mover 2(l − 1) + k; Ξ-targets, β-ranks and parities, gates and the start free; ISO not assumed), T the
  number of steps of the IDEAL run from the given start (R104's L(G)), T^R(3) the largest T over 𝓛^R_3 and all starts (R110).
  (a) T^R(3) ≤ 8, A MACHINE-CERTIFIED STATEMENT (packet §1 l. 21: «STATEMENT P-TR3: for every genome G ∈ 𝓛^R_3 and every start s_0, the
      IDEAL run of G from s_0 has at most 8 steps: T^R(3) ≤ 8.»). Route (packet §2): the query Q(L) «there are a genome of 𝓛^R_3 and a
      start whose run has at least L steps» (l. 25) is a CNF built by experiments/comp/box27/cnf.py, mapped clause by clause to R104's
      wording in ENCODING.md §2-§3; one symmetry break SYM (s_0(0) = s_0(1) = 0, sound by relabelling the two options of a level-0
      mover, l. 35-40); 16 cubes fixing s_0 on movers 2-5, «Q(9) is UNSAT iff all 16 cube formulas are UNSAT.» (l. 42). Evidence:
      CaDiCaL 1.9.5 answers UNSAT on all 16 cube formulas (§3 l. 45-48, 4,946 s; each formula 58,896 variables, 204,036 clauses, DIMACS
      sha1 per cube l. 49-50); for each cube, Glucose 4 (pysat 1.9.dev15) writes a DRUP proof and the lane's own forward RUP checker
      experiments/comp/box27/drup.c (sha1 2d4b8eab8fe9e9035c396733bb400d9d6e7d2366, l-comp 07cec839, 98 lines of C) accepts it: «Totals:
      16/16 VERIFIED; 11,353,990 lemmas; 19,694,959,174 proof bytes.» (l. 100; per-cube DIMACS sha1, proof sha1, proof size and lemma
      count in the table l. 82-99 and in log/R_d3_L9_cert.txt). It is CERT by an own RUP checker, not drat-trim, LRAT or Lean (l. 60-63,
      108-110; REFEREE-2 l. 25 «Any citation must say «machine, CERT by an own RUP checker».»). Cells: REFEREE l. 15 «SIGN, as a
      machine-certified statement (scope in §5); gaps listed below», §5 l. 133 «SIGNED: STATEMENT P-TR3 (T^R(3) ≤ 8, hence T^R(3) = 8)
      as a MACHINE-CERTIFIED result:», §C l. 205 «P-TR3 stays SIGNED as machine-certified.»; REFEREE-2 l. 14 «**SIGN WITH GAPS** (Opus
      5.5, D12): gaps TR3-G1, TR3-G2 below», Add. 1 l. 161-162 «My verdicts stand.».
  (b) T^R(3) ≥ 8, BY AN EXPLICIT INSTANCE (packet §3 l. 51-52; fixes F2): experiments/comp/box27/out/R_d3_L8.json (sha1
      dbe8b9bcdb05d03b23ac350f9da429485ebd6d57, l-comp 557b045b), a genome of 𝓛^R_3. Option fields (W-target, Ξ-target, gate, β rank, β
      parity; X the exit, − no W-target): mover 0 (lev 0): (−, 1, 0, 9, even), (−, X, 2, 5, even); 1 (lev 0): (−, X, 3, 10, odd), (−, 4,
      1, 1, odd); 2 (lev 1): (0, 5, 102, 7, even), (1, 4, 100, 8, even); 3 (lev 1): (0, 0, 103, 6, odd), (1, 4, 101, 0, even); 4 (lev
      2): (2, X, 203, 2, even), (3, X, 202, 11, odd); 5 (lev 2): (2, 4, 201, 3, odd), (3, 3, 200, 4, odd). Start 101110 (movers 0..5);
      run 101110, 101010, 101011, 100001, 111100, 011100, 011000, 011001, 010001: T = 8, stop because no mover has a strictly better
      option. Replayed by the lane's sim.py and L-RED's r187/ideal.py (l. 51-52), by REFEREE's t3r_sim.py (R-T3R-audit l. 68-69 «So
      T^R(3) ≥ 8 is PROVED by this instance»), by REFEREE-2's r2sim.py («T = 8 from its start with all 9 states equal to the stored
      «states»; the maximum over all 64 starts of this genome is 8.», R2-P-TR3 l. 93-94) and by my own simulator for this draft (the
      same 9 states; maximum 8 over the 64 starts). Cells: REFEREE l. 118 «Lower bound: the witness out/R_d3_L8.json gives T = 8 under
      my simulator t3r_sim.py (R-T3R-audit §3). So T^R(3) = 8.»; REFEREE-2 l. 15 «**SIGN** (Opus 5.5, D12)».
  (c) The lane's proved steps (packet §2 l. 31-42, ENCODING.md §1, §3; «PROVED (lane, written out above / in ENCODING.md): E1-E3, the
      soundness of SYM, the cube cover, «Q(9) UNSAT ⇔ P-TR3» given that the CNF encodes R104 for 𝓛^R_3» (§5 l. 113-114)): (E1) the
      symmetric difference of the two chains of a mover is never empty; (E2) only the order of gates inside a level matters; (E3) two
      movers of one level compare their W-targets' keys if the targets differ and their own gates if not; SYM is sound (the relabelled
      genome is in 𝓛^R_3 and its run is the old run with bit x flipped); the 16 cubes are all 2^4 assignments of movers 2-5. Cells:
      REFEREE-2 l. 16 «**SIGN** (Opus 5.5, D12) (encoding audited by my predecessor, R2-T3R-audit.md; reconfirmed below)»; REFEREE:
      R-T3R-audit l. 19 «SOUND; the cubes cover every start», R-P-TR3 §4 l. 116-117 «Q(9) is UNSAT ⇔ the statement, given the encoding
      and the SYM / cube cover (R-T3R-audit §1-§2).».
  (d) drup.c, the checker of record (packet §4 l. 64-75): forward RUP for each added lemma, deletions applied by default (IGNDEL=1
      ignores them), no RAT step, «s VERIFIED» iff a top-level conflict is reached. Cells: REFEREE l. 16 «SOUND (line-by-line audit,
      §1)», l. 67-69 «drup.c is SOUND as a refutation checker of the file it reads.»; REFEREE-2 l. 17 «audited: **SOUND** for the inputs
      used; robustness note D-1» (D-1: a malformed token makes drup.c loop, never give a false VERIFIED; it does not bear on the result:
      the 16 DIMACS files are written by mkproof.py from integer lists, and cube 10's was checked strictly, l. 50-55; fixes F5 adds the
      strict parser drup2.c as a separate file, «drup.c (sha1 2d4b8eab…) stays the checker of the certified record» (fixes l. 44)).
  (e) The encoding: «cnf.py as an encoding of «some genome of 𝓛^R_3 and some start give T ≥ L»» is «FAITHFUL WITH GAPS (T3-G1, T3-G2;
      neither is an error)» (R-T3R-audit l. 17), T3-G2 closed by R110 (R-T3R-audit Addendum 2, l. 186-187 «So the class and the quantity
      now have a landed definition, and T3-G2 is CLOSED.»); REFEREE-2 27: «The encoding is faithful to R104's definition on every
      clause» (R2-T3R-audit l. 59). REFEREE l. 18 «FAITHFUL (R-T3R-audit; T3-G2 closed by R110)»; REFEREE-2 28 cites its predecessor's
      audit (TR3-G2, l. 26-28) and re-checked that the certified DIMACS files are those of the audited cnf.py (l. 65-67).
  The RESULTS line (L-3) states (a) and (b) with their exact hypotheses, the evidence of (a) as «a machine statement», and nothing
  wider.
- What rests on the machine (packet §5 l. 112-119 with fixes F4; both referees' gap lists): (i) PROVED (lane, signed): (c), and «Q(9)
  UNSAT ⇔ P-TR3» given the encoding. (ii) AUDITED, NOT PROVED: that cnf.py's DIMACS output is the encoding of R104 for 𝓛^R_3 (packet l.
  116-117 «(ii) cnf.py's DIMACS output being the encoding of §2 (checked by two referee audits of ENCODING.md and by pinck.py, not by a
  proof)»; REFEREE l. 29-30 «The encoding's faithfulness to R104 is an audit (R-T3R-audit; REFEREE-2 R2-T3R-audit), not a proof. CERT
  certifies UNSAT of the 16 recorded DIMACS formulas only.»; REFEREE-2 TR3-G2 l. 26 «CERT certifies UNSAT of the DIMACS formulas, not
  that they encode R104 on 𝓛^R_3.»). (iii) MACHINE: the UNSAT of the 16 cube formulas. It is certified by 16 Glucose 4 DRUP proofs
  accepted by drup.c; Glucose itself is not trusted (REFEREE TR-G2 (i) l. 26-27 «pysat's Glucose 4 only produces the proofs; it is not
  trusted, since a wrong proof is rejected.»); trusted: drup.c, an own tool, audited sound by both referees, «its correctness is a
  premise of CERT» (fixes F4 l. 31-33), and the referees' own checkers on the re-checked cubes (REFEREE TR-G2 l. 27-28, of drup.c and
  its ref_rup.c: «unverified C, not a formally verified checker such as cake_lpr»); the identity of the DIMACS files is checked by sha1
  outside drup.c (REFEREE l. 40-41). (iv) RE-CHECK SCOPE: all 16 proofs were regenerated byte-identically by REFEREE and accepted by its
  own ref_rup.c, deletions ignored: cubes 10, 9, 5 also with drup.c (R-P-TR3 §3), the other 13 in R-P-TR3 Addendum 1 (claude/referee
  365f22e1, file sha1 c31d4281…, l. 207-221, log scratch/t3r_logs/tr3_rest13.txt: «TR-G1 is CLOSED.»); cube 10 also by REFEREE-2 with
  drup.c in both modes and its own r2rup.c (REFEREE-2 Add. 1 l. 161). The line keeps the counts on file at its fix («REFEREE 3 cubes,
  REFEREE-2 1 cube»), which Addendum 1 calls «true and conservative». The proofs (19.7 GB) are not committed; they are regenerable and
  deterministic (packet l. 101-107; REFEREE l. 108-109 «So the proofs are deterministic across machines»). (v) Independent of the
  certificate, the 16 UNSAT answers are reproduced by CaDiCaL 1.9.5 (lane; REFEREE; REFEREE-2 27), Kissat 4.0.4 and Glucose 4 (REFEREE,
  R-T3R-audit §4 and Addendum 1) on byte-identical formulas: corroboration, not a certificate. (vi) NOT MACHINE: the lower bound (b) is
  one explicit run of 8 steps, recomputed by five simulators.
- Premise: RESULTS R104's definition of the IDEAL model (no R104 theorem), quoted verbatim by the packet (§1 l. 7-14), 1 hit in RESULTS
  (inside R104's block, title l. 9864); RESULTS R110's definitions of 𝓛^R_d and T^R(d) (no R110 theorem), quoted verbatim by the fixes
  (F1 l. 11-16: «on acyclic Ξ-graphs, with 𝓦_d the genomes with levels 0, …, d − 1 whose level-0 movers are exactly two movers named 0
  and 1, 𝓛^R_d ⊆ 𝓦_d the 2-wide degree-2 ladders in L-RED's R197 convention (movers 2l and 2l + 1 on level l, all of degree 2, no other
  movers, option k of a mover of level l ≥ 1 W-pointing to mover 2(l − 1) + k), T^R(d) the largest number of steps over 𝓛^R_d and all
  starts (kept apart from R109's T*(d) over 𝓛_d; T^R(d) ≤ T*(d))»), 1 hit in RESULTS (R110's title, l. 11323). L-3: «In the IDEAL model
  of RESULTS R104 (definition only, no theorem of R104 used), on 𝓛^R_3 (RESULTS R110's definitions of 𝓛^R_d and T^R(d) only, no theorem
  of R110 used:». REFEREE §C l. 181 «The R110 quote («on acyclic Ξ-graphs, with 𝓦_d … T^R(d) ≤ T*(d))») is verbatim: 1 hit in RESULTS at
  trunk 4b35e2b0, l. 11323.»; REFEREE-2 Add. 1 l. 143 «F1: the R110 quote (446 characters) is a verbatim substring of docs/RESULTS.md.».
  No lit note, no lane file, no other RESULTS entry, no machine premise from outside the entry. No Lean.
- L41. The proved steps (c) are the lane's (packet §2, ENCODING.md); the referees' ref_rup.c, r2rup.c and simulators are checking tools,
  not proof steps. Nothing referee-written is a proof step of the entry (my reading; neither referee mentions L41). No DEAD item; L43
  does not bear.
- Fixes (experiments/comp/box27/P-TR3-fixes.md, L-COMP successor 9, append-only; entry 1 at d3e3cde8, 73 lines, sha1
  d7b33861ea3a6aecc0a069e43f6df8b53c3f28e3; entry 2 at dd4a55c6 and 9c70c980, 86 lines, sha1 38b97e59869572c85d6f680c935c4253df4e23c9,
  l. 1-73 unchanged); entry 1 after REFEREE 5a5b94cf and REFEREE-2 60e24158, entry 2 after CHECKER C123 (96b7f8a1):
  - F1 (l. 9-19, REQUIRED TR-1, REFEREE-2 stale note): §1's class and quantity now come from RESULTS R110, quoted verbatim; «Ξ-data
    arbitrary» is read as «acyclic Ξ-data arbitrary»; «Nothing in §2-§5 changes.» (l. 19). REFEREE §C l. 180 «F1 (TR-1): CORRECT; TR-1
    CLOSED.»; REFEREE-2 Add. 1 l. 143-144.
  - F2 (l. 21-22, optional TR-P3): «With the witness of §5» → «With the witness of §3». REFEREE §C l. 183; REFEREE-2 Add. 1 l. 145.
  - F3 (l. 24-28, optional TR-P2): cnf.py fd882af1 built the CaDiCaL cube formulas, cnf.py f1f803ae the Glucose proofs; the 16 DIMACS
    files are byte-identical (l. 27-28). REFEREE §C l. 184-187; REFEREE-2 Add. 1 l. 146-147 («16/16 byte-identical»).
  - F4 (l. 30-39, optional TR-P3, REFEREE-2 stale note): drup.c is «audited sound by REFEREE 24 (R-P-TR3 §1: line-by-line; 13 negative /
    positive tests) and by REFEREE-2 28 (R2-P-TR3: audit and 12,902 fuzz runs, UNSOUND 0)»; «its correctness is a premise of CERT»
    stays; the re-check counts «(Counts as on file in the two reports; the 13 other cubes rest on log/R_d3_L9_cert.txt plus Glucose's
    determinism.)» (l. 36-37); ENCODING.md l. 5 read with the DRUP addition. REFEREE §C l. 188-192; REFEREE-2 Add. 1 l. 148-150.
  - F5 (l. 41-47, optional TR-P1 / REFEREE-2 D-1): drup2.c (sha1 34ff0d8079b0143b5757e653c6d50364b333c49a), strict parsing, a NEW file;
    «drup.c (sha1 2d4b8eab…) stays the checker of the certified record; nothing in §4 changes.» (l. 44). REFEREE §C l. 193 «I did not
    audit drup2.c; nothing in the claim uses it.»; REFEREE-2 Add. 1 l. 151-154 («drup.c stays the checker of record.»).
  - F6 (l. 49-73): line L-2 = L-1 with the four replacements L-a to L-d; «Not taken: none of the required or optional items was
    declined.» (l. 72).
  - F7 (entry 2, l. 75-86, after CHECKER C123 E-1): line L-3 = L-2 «with exactly one deletion: the leading «P-TR3 [lane: EXACT-SAT +
    CERT] »» (l. 77), «copied by script from C123 §5's text» (l. 78-79), «Nothing else changes.» (l. 80); the word diff, «one deletion;
    no insertion» (l. 81-82); «Not taken (Lead 07:38Z): C123's optional «REFEREE all 16 cubes» change; L-3 keeps the on-file counts
    «REFEREE 3 cubes, REFEREE-2 1 cube».» (l. 85-86). REFEREE §C add. 1 (1140096d) l. 232-233 «Fixes entry 2 (F7) describes exactly this
    one deletion.», «No statement or definition changes.»; REFEREE-2 Add. 2 (ee1d6e18) l. 168 «**Fixes entry 2: CORRECT.**», l. 169
    «nothing in the statement, its scope or its DATA changes».
  No fix changes the statement, a proof or a certificate record; F1 changes the premise route to the landed R110; F2-F4 correct packet
  text; F5 adds a tool outside the record; F7 deletes the lane label at the start of the line only.
- Not signed: packet §3's DATA (pinck.py, bf2.c, sim.py = ideal.py on 198,085 runs) and §5 l. 119 «DATA only (not part of the claim):
  pinck, bf2, the replays.»; drup2.c (F5); every other box-27 number (T^R(2) = 4 as a statement, T_k(m), T*(d), d ≥ 4). OPEN, not
  claimed: any bound on T^R(d) for d ≥ 4; T*(3); any statement on Ξ-cyclic genomes or on R109's 𝓛_d; G-N5-TIME.
- Referee strengthening (NOT part of this entry; referee checks):
  (i) REFEREE: 16/16 UNSAT under CaDiCaL 1.9.5 and Kissat 4.0.4 on its own rebuild (R-T3R-audit §4), and under Glucose 4 (Addendum 1 l.
      181 «So three solvers of two lineages (CaDiCaL 1.9.5 and Kissat 4.0.4; Glucose 4, MiniSat lineage) agree: 16/16 UNSAT each.»);
      12,384 pinned runs and 345 genome-only tests against its own simulator, 0 disagreements, with four encoding mutations each caught
      (R-T3R-audit §3 l. 87-95); its own forward RUP checker ref_rup.c and 13 negative / positive tests on d 2 proofs, three verdict
      columns agreeing on every row (R-P-TR3 §2 l. 73-98).
  (ii) REFEREE-2 28: drup.c fuzzed on 3,000 random CNFs (12,902 runs: 3,840 + 6,000 + 902 + 2,160), every VERIFIED on a brute-force
       UNSAT formula (l. 56-59); r2rup.c fuzzed (l. 78-79); all 16 cube DIMACS rebuilt with the audited cnf.py fd882af1 and with
       f1f803ae, 16/16 byte-identical (Add. 1 l. 146-147). REFEREE-2 27: CaDiCaL 1.9.5 re-run of the 16 cubes, and 414 pinned (genome,
       start) pairs against its own simulator, 0 disagreements, including d = 4 runs of length up to 12 (R2-T3R-audit §4-§5).
- Honest limits: (i) A MACHINE STATEMENT: the upper bound T^R(3) ≤ 8 rests on the UNSAT of 16 recorded DIMACS formulas, certified by
  DRUP proofs checked with the lane's own RUP checker drup.c (unverified C, audited sound by both referees), and on an audited, not
  proved, encoding of R104 for 𝓛^R_3; no drat-trim, LRAT, formally verified checker or Lean; no human-readable proof. (ii) Gaps, as
  listed by the referees: TR3-G1 (REFEREE-2: the certificate is a RUP proof checked by an own tool, not drat-trim, LRAT or Lean;
  REFEREE-2 re-checked cube 10) and REFEREE's TR-G1, CLOSED by R-P-TR3 Addendum 1 (all 16 proofs regenerated and accepted by REFEREE's
  ref_rup.c) and TR-G2 / TR3-G2 (the trusted base: the checkers, and the encoding as an audit). (iii) Only d = 3: no bound is claimed
  for d ≥ 4; Ξ-cyclic genomes, R109's 𝓛_d and T*(d) are not covered (packet §6). (iv) Bounds nothing polynomially; a statement inside
  R104's IDEAL model only; G-N5-TIME stays open; not M3, not a step-4 pass, not a TARGET.md claim. (v) The DATA is per statement, as the
  line's DATA parenthesis says: pinck.py's 450 random genomes are 300 of 𝓛^R_2 and 150 of 𝓛^R_3 (packet l. 53-54), mostly short runs
  (REFEREE-2 27 l. 47-48), and the 128 runs are the 64 starts of each of the two length-8 genomes (l. 54-56); bf2.c's maximum is over
  all of 𝓛^R_2 and all starts (l. 56-57). (vi) Premises: RESULTS R104's definition and R110's definitions of 𝓛^R_d and T^R(d); no other
  RESULTS entry, no lit note, no lane file, no outside source. (vii) Names: «R112» here is this RESULTS entry, not L-RED's box R112
  (notes/L-RED.md); «CERT» and «EXACT-SAT» are the lane's labels for its evidence, not RESULTS tags; «TR-G1», «TR-G2» (REFEREE),
  «TR3-G1», «TR3-G2» (REFEREE-2) and «T3-G1», «T3-G2» (the encoding audit) are referee gap labels, not GAPS rows; «cube» is a fixing of
  the start bits of movers 2-5; «drup.c» is L-COMP's experiments/comp/box27/drup.c at sha1 2d4b8eab…, not drat-trim. (viii) The
  proof-carrying files are the packet (§2) and ENCODING.md (§1, §3), which the line's source note names with the fixes file.
- Data (DATA, not proof): packet §3 (l. 44-57): pinck.py «pins a whole genome and start by unit clauses; the CNF is SAT at L = T and
  UNSAT at L = T + 1 with T from sim.py: 0 disagreements on 300 random d 2 and 150 random d 3 genomes of 𝓛^R and on all 64 starts of
  each of the 2 distinct length-8 genomes ext/dbl_d3_F6.json (L-RED R197) and ext/own_R_d3_L8.json (= the genome of out/R_d3_L8.json)»
  (l. 53-55); «At d 2 the same encoder gives Q(5) UNSAT and the exhaustive C enumeration bf2.c (no SAT) gives max T = 4 over all of
  𝓛^R_2 and all starts. sim.py = ideal.py on 198,085 runs.» (l. 56-57). L-3's DATA parenthesis: «(DATA, each count naming the statement
  it covers: 16 cube UNSATs and 16/16 VERIFIED proofs (11,353,990 lemmas) cover «T ≤ 8» only; pinck.py's 0 disagreements on 450 random
  genomes and on the 128 start runs of the 2 distinct length-8 genomes cover only the agreement of the CNF with the simulator; bf2.c's
  exhaustive maximum T = 4 on 𝓛^R_2 covers only the d 2 cross-check)». The certificate records (packet §4 l. 80-104,
  log/R_d3_L9_cert.txt): 16 rows (cube, DIMACS sha1, Glucose s, proof sha1, proof bytes, lemmas, drup s, verdict), all «s VERIFIED»,
  deletions applied; cube 1 proved twice with the same proof sha1 (l. 101-104). Negative tests of drup.c (l. 76-79): a valid d 2 proof
  VERIFIED, a SAT formula, a truncated proof and a holed proof NOT VERIFIED. Re-run for this draft (scratch, from a git archive of
  d3e3cde8's experiments/comp): the 16 cube DIMACS rebuilt with both cnf.py versions, sha1 equal to the packet's tables (16/16); the §4
  table equal to log/R_d3_L9_cert.txt (16/16) with the stated totals; experiments/comp/check.sh «box27 witnesses replayed: 5, failures:
  0»; the witness replayed by my own simulator (T = 8, the stored states, maximum 8 over 64 starts); drup.c on fresh d 2 files (VERIFIED
  5,730 lemmas in both modes; NOT VERIFIED on the SAT formula, the truncated proof and a holed proof); cube 10 regenerated with the same
  proof sha1 and size as the packet's row and «s VERIFIED (485366 lemmas RUP-checked)» by drup.c (a fourth check of the cube both
  referees re-checked; not a referee check). No signed statement uses any DATA count; (a) rests on the certificate records, which are
  the evidence, not DATA.
- Signatures: REFEREE docs/referee/R-P-TR3.md: successor 24's report 5a5b94cf1bbd23c97fcf75c7de5c06b22abe652a (2026-11-06T02:39:17Z, new
  file, 171 lines, sha1 a2ced7e8003bb31b09ca064a288e517434542047, with scratch/ref_rup.c (2005aee7), t3r_logs/neg_tests.txt,
  tr3_regen_check.txt): P-TR3 SIGN as machine-certified with gaps TR-G1, TR-G2, drup.c SOUND, CERT confirmed on 3 cubes, the encoding
  FAITHFUL, L-1 NOT YET (TR-L1, TR-L2) (l. 12-30); §C fadbb9a06ea3d829366d01023cead7040d389e88 (2026-11-06T04:09:18Z, 205 lines, sha1
  9976bac7b794c395cf5f2c9d5b6b18596dc842ad; l. 1-171 = 5a5b94cf's, by cmp): F1-F3 CORRECT, F4 «CORRECT for my part», F5 a new file it
  did not audit («nothing in the claim uses it»), the byte test of L-2 (l. 194-197), «L-2 MATCHES.» (l. 203), «Fixes entry 1 is
  CORRECT.» (l. 204), «P-TR3 stays SIGNED as machine-certified.» (l. 205). Addendum 1 365f22e1daadedf023a57a2012141963875d4be6
  (2026-11-06T06:15Z by its own stamp; file sha1 c31d4281…): the 13 remaining cubes regenerated and accepted by ref_rup.c, «TR-G1 is
  CLOSED.» (l. 218), «TR-G2 stands» (l. 219). §C add. 1 1140096d222d18ddc36fd279ed747cf322c8cc86 (2026-11-06T08:04:04Z, 234 lines, sha1
  15f3a22ed607b277ebc5f7a92af5acf3ccfe2c59; l. 1-221 = 365f22e1's, by cmp): the byte test of L-3 against C123 §5 (l. 227-231), «Verdict:
  L-3 MATCHES. P-TR3 stays SIGNED as machine-certified; TR-G1 is CLOSED (Addendum 1).» (l. 234). Encoding audit
  docs/referee/R-T3R-audit.md (successor 24): 776d0fdf (2026-11-05T16:00:24Z, 141 lines), §C bfeca123 (16:54:44Z), Addendum 1 5c02d44d
  (17:26:52Z), Addendum 2 ece8c4ee (23:49:08Z; 187 lines, sha1 d0a5d7e188742d8164fd58a5adeaa7364143bd7f). REFEREE-2
  docs/referee-2/R2-P-TR3.md: successor 28's report 60e24158ef66fc15bfef2e8d28cdb64403bb3ed7 (2026-11-06T02:39:25Z, new file, 134 lines,
  sha1 79989749b1133cef9934ba5c08a4c4cdab2190be, with R2-P-TR3/fuzz_drup.py and r2rup.c (b1fbc8d4)): the upper bound SIGN WITH GAPS
  TR3-G1, TR3-G2, the witness SIGN, SYM / cover / E1-E3 SIGN, drup.c SOUND, L-1 not matching as written (l. 11-28); Addendum 1
  7ff32432964d8adbf30d75932f37552de810434d (2026-11-06T04:13:09Z, 162 lines, sha1 8313172f1234447e91b0575e6b76883cf77e47a5; l. 1-134 =
  60e24158's, by cmp): «**Fixes entry 1: CORRECT.**» (l. 142), «**Line L-2: MATCHES.**» after its byte test (l. 155-157), «My verdicts
  stand.» (l. 161); Addendum 2 ee1d6e183bf156565727f3bf38a17c1d6aeab73b (2026-11-06T08:04:07Z, 174 lines, sha1
  cd3b3453fd5119f6658a6ce1f8a645925d38c592; l. 1-162 = 7ff32432's, by cmp): «**Fixes entry 2: CORRECT.**» (l. 168), «**Line L-3:
  MATCHES.**» after its byte test (l. 170-172), «My verdicts stand.» (l. 174). Encoding audit docs/referee-2/R2-T3R-audit.md (REFEREE-2
  successor 27): d1c4a530788881ec5029848033e4933e431728e0 (2026-11-05T12:49:17Z, 66 lines, sha1
  751979956af86ebb7c65348726720beb4ee1fc71). Lane: freeze and L-1 d03d8370120ffba19f7bf1fa73f8814ca00bf2d3, fixes entry 1 and L-2
  d3e3cde81411a5487c588f3bd132451efc63abae, fixes entry 2 and L-3 dd4a55c6126afa21feb77b7c9bc6f00fa9c469a2, entry 2's word-diff bullet
  9c70c98018eb07a2ee6dab1bde6144a7692d3eff.
  INDEPENDENCE: REFEREE l. 2-3 «Independent: I did not open or list docs/referee-2/ on this packet before this report was pushed.»;
  REFEREE-2 l. 2-3 «Independent: docs/referee/ (including R-P-TR3.md) not read before this push.». The two reports were pushed 8 s apart
  (02:39:17Z, 02:39:25Z); each audited drup.c by reading every line, wrote its own RUP checker (ref_rup.c, r2rup.c) and regenerated
  proofs on its own (cubes 10, 9, 5; cube 10). In the second round REFEREE read REFEREE-2's items only through the fixes entry (§C l.
  179 «I have still not read docs/referee-2/ on P-TR3; I know REFEREE-2's items only through the fixes entry's list.»); REFEREE-2 read
  R-P-TR3.md at 5a5b94cf «only to check the counts F4 quotes from it» (Add. 1 l. 140-141). The two encoding audits were independent too
  (R-T3R-audit l. 2-3; compared afterwards in its §C, «No disagreement on any fact.», l. 174). Differences, resolved: REFEREE signs «as
  a machine-certified statement», REFEREE-2 «SIGN WITH GAPS»; both list the same two gaps (re-check scope; trusted base and encoding
  audit) and both sign the lower bound. In the encoding audits REFEREE-2 27 called the missing certificate a «Residual caveat (stated,
  not a gap in the sense of G-FLIP-1)» (R2-T3R-audit l. 61), REFEREE listed it as gap T3-G1 (R-T3R-audit l. 24, §C l. 167-172); the
  certificate now exists (packet §4), and both successors list its limits as gaps. Both MATCH L-2 and L-3 (each byte-tested L-3 against
  C123 §5 and had computed the expected sha1 before L-3 was pushed: REFEREE §C add. 1 l. 228-229, REFEREE-2 Add. 2 l. 171-172). No
  disagreement in substance.
- TARGET.md diff: TARGET.md §1-§3 define parity games («A parity game is G = (V, V_E, V_O, E, pr) with V finite»), the regions W_E, W_O,
  M4 (§2 «There is a deterministic algorithm A and a polynomial p such that for every parity game G, A on input G halts within») and the
  word-RAM cost model; the statement of this entry mentions no parity game, no winning region, no algorithm's running time and no cost
  model: it is a statement about the run lengths of one finite class of genomes of R104's IDEAL model (packet §7 l. 125 «Not a TARGET.md
  claim: a statement inside the IDEAL model; G-N5-TIME stays OPEN; not M3, not a step-4 pass.»; REFEREE §5 l. 139-140 «Diff against
  TARGET.md: the statement is inside R104's IDEAL model; it concerns no parity game or running time; not M3, not M4, not a gauntlet
  step. G-N5-TIME stays OPEN. Agreed with §7.»; REFEREE-2 (3) l. 100 «TARGET.md diff: a statement inside the IDEAL model; no game, no
  algorithm, no complexity class; not M3 / M4 / step 4. ✓»). The solver times in the packet are machine data, not a running-time claim.
  The line (L-3) makes no M4 claim and no TARGET claim; its tail reads «not Lean; not a TARGET.md claim; G-N5-TIME stays OPEN» (L-3, by
  script). Not a step-4 pass. GAPS G-N5-TIME: open.

Proposed GAPS line-11 UPDATE (append-only), to go AFTER R111's UPDATE of G-N5-TIME (R111 is LANDED, e751969c: the last UPDATE on GAPS l.
11 is R111's, «UPDATE 2026-11-06 07:16Z: RESULTS R111 (P-IDEAL-KEYS; CHECKER C124 18aa6728) …», before the row's closing « |»), built by
script (upd112b.py: upd112.py's procedure, unchanged, run on L-3, with its R111 control now against R111 as LANDED on GAPS l. 11 (15
controls, R97-R111, all landed, byte for byte, True); upd112.py: upd111b.py's procedure and R97-R110 controls unchanged;
sentinel_build111 of upd111.py unchanged, with ONE ADAPTATION (G-U): the drop list is «G-N5-TIME stays OPEN» and «not a TARGET.md
claim», L-2's and L-3's form of the scope sentence; «not Lean» is kept; cross-checked against a direct build: True) only from the
clauses of the title line L-3: « (2026-11-05) — » → «: »; L-3 has no item labels and no DEAD clause; the DATA parenthesis before the
source parenthesis opened as «; DATA, …»; «G-N5-TIME stays OPEN» and «not a TARGET.md claim» dropped; the source parenthesis kept; «.
G-N5-TIME stays open.» at the end. L-3 holds no "|"; the UPDATE holds none (1,735 bytes, 12 «(» / 12 «)»; sha1 of the line without
newline, placeholders unfilled: 21ab655986310c668c0ac4f8995e57ef1759716d, = C123 §4; it equals the first fill's UPDATE with «P-TR3
[lane: EXACT-SAT + CERT] » deleted after «LANDED: », True). <DATE> is the landing date (YYYY-MM-DD, by date -u at the landing commit;
C114 Add. 1 E-1), <HH:MM> the landing time and <checker> the CHECKER C123 commit, all filled at landing:
UPDATE <DATE> <HH:MM>Z: RESULTS R112 (P-TR3; CHECKER C123 <checker>) [refereed-only] LANDED: In the IDEAL model of RESULTS R104 (definition only, no theorem of R104 used), on 𝓛^R_3 (RESULTS R110's definitions of 𝓛^R_d and T^R(d) only, no theorem of R110 used: the 2-wide degree-2 ladders with levels 0, 1, 2 in L-RED's R197 W-convention, all acyclic Ξ-data, β's, gates and starts, ISO not assumed; T^R(d) the largest number of steps over 𝓛^R_d and all starts): T^R(3) ≤ 8, hence T^R(3) = 8: a machine statement: CaDiCaL 1.9.5 UNSAT of the CNF query «some genome and start have T ≥ 9» (experiments/comp/box27/cnf.py, mapped clause by clause to R104 in ENCODING.md) on 16 cubes that cover every start up to one sound relabelling (both level-0 movers start on option 0), each cube also refuted by a Glucose 4 DRUP proof accepted by the own forward RUP checker drup.c (sha1 2d4b8eab…; no drat-trim; drup.c audited sound by REFEREE and REFEREE-2, its correctness still a premise; cube proofs regenerated byte-identically and re-checked independently: REFEREE 3 cubes, REFEREE-2 1 cube), and T ≥ 8 SAT with a witness replayed under two simulators; not Lean; DATA, each count naming the statement it covers: 16 cube UNSATs and 16/16 VERIFIED proofs (11,353,990 lemmas) cover «T ≤ 8» only; pinck.py's 0 disagreements on 450 random genomes and on the 128 start runs of the 2 distinct length-8 genomes cover only the agreement of the CNF with the simulator; bf2.c's exhaustive maximum T = 4 on 𝓛^R_2 covers only the d 2 cross-check (P-TR3, experiments/comp/box27/P-TR3.md with its fixes entry 1, experiments/comp/box27/P-TR3-fixes.md, and experiments/comp/box27/ENCODING.md; L-COMP successor 9). G-N5-TIME stays open.

Addendum (subagent, for the Lead; does not land; written 2026-11-06T06:07:58Z by date -u). (1) FIRST FILL on line L-2 (l-comp d3e3cde8,
sha1 11cd9acc…), to CHECKER C123. NOT pushed; my commits: the five merges (--no-ff) c54f19b8, 6b95c066, 02d0f872, 1d689e9a, 7ad0389c,
then 285e5061 (R111 second fill) and one commit holding this file. Push trunk before landing. (2) TITLE l. 265 = "### R112
[refereed-only] " + L-2 without its newline + ", CHECKER PASS (docs/checker/C123.md, checker PENDING)", checked by script (chk112.py):
equal, byte for byte (True); the only «### R» heading of this file; 13 + 1 «(» and 13 + 1 «)», balanced. (3) BODY l. 265-476
(python slice d[264:476]; 0 "|" in the range, by script); GAPS preamble l. 478-488 (its only "|" are the two inside the
quoted closing « |», as in R107's to R111's preambles); UPDATE l. 489 (d[488]; one line, 0 "|", one each of <DATE>, <HH:MM>,
<checker>; 1,766 bytes; sha1 1ff15db00661eda0d916b1cb1930081303b01e88 of the unfilled line without newline; controls True ×15:
R97's-R110's landed UPDATEs and R111's drafted one). No Dead-ends row is drafted ((14)). A landing script in the shape of R110's /
R111's slices d[264:476] for the entry and reads d[488] for the UPDATE (with «R112», «R111» as PREV, «C123», and the GAPS l.
11 assertion on «RESULTS R111 (P-IDEAL-KEYS» as the last UPDATE). (4) RE-RUNS: listed in the header paragraph "Re-runs", (a)-(g). NOT
RUN: the 16 Glucose proofs except cube 10's ((f)); ref_rup.c, r2rup.c and the fuzz harness; CaDiCaL / Kissat; scripts/verify.sh;
L-COMP's pinck.py and bf2.c (their records read). (5) QUOTE SWEEP (chk112.py: chk111b.py's rule: outermost guillemet quotes, whitespace
joined, split at the ellipsis, parts of 6+ characters; sources: the packet, L-1, L-2, fixes, ENCODING.md (both versions), README.md,
drup.c, drup2.c, check.sh, cert and cube logs, both referee reports and both encoding audits at their head commits with the referee
logs, RESULTS, GAPS, DECISIONS, D001, LEAD-STATE, NOW, TARGET.md, CLAUDE.md, C116, C122, C124, notes/CHECKER.md, notes/L-RED.md,
R110-draft, R111-draft, my re-run outputs): 315 outermost quotes, 272 parts of 6+ characters, every part found (0 not found); in the
title and body alone 117 quotes, 112 parts, 0 not found; GAPS preamble and UPDATE 15 quotes, 10 parts, 0 not found. Line-precise: 124 of
124 (source, cited line range, quote) triples found verbatim, whitespace-normalised, inside the cited lines. Every sha1, line count and
commit time cited was re-measured in this session (sha1sum, wc -l, cmp, git log -1). (6) DISCREPANCIES: (11) D-1 to D-6. I found no
error in a signed statement. (7) FLAGS FOR THE LEAD AND CHECKER: G-0 (C123), G-T (tag «[refereed-only]», precedent and reasons), G-L
(the lane label «P-TR3 [lane: EXACT-SAT + CERT]» inside the verbatim title), G-U (the UPDATE's one adaptation), G-R (TR-G1 counts on
file; the announced REFEREE addendum is not on origin and is not mentioned); NOTE G-C (R110's CONDITIONAL: a separate item for the Lead,
not in R112). (8) NOT VERIFIED: the 13 proofs no referee regenerated (lane record only; my cube 10 run is a fourth check of the same
cube); the referees' tools were not re-run (their files and logs read); scripts/verify.sh not run. (9) LANDING SIMULATION (sim112.py, on
in-memory copies of RESULTS and GAPS at the local trunk, R111 landed first from docs/agents/R111-draft.md (285e5061) with the same
procedure): R111 first (sim111.py's procedure on R111-draft d[470:780], UPDATE d[794]): RESULTS 12,176 -> 12,487 lines, a pure insertion
of 311 lines after R110's block: True; then R112: RESULTS 12,487 -> 12,700 lines (wc -l), a pure insertion of 213 lines (the entry block
with "checker PENDING)" filled, plus one blank line) directly after R111's block (R111 l. 11,598-11,907, blank l. 11,908,
byte-unchanged: True; R110's block byte-unchanged: True): True; R112 at l. 11,909-12,120, blank l. 12,121, the next line (**Erratum
E-1**) moves to l. 12,122, «**Erratum E-2**» to l. 12,135, «## Dead ends» to l. 12,163; order R110, R111, R112, E-1, E-2, Dead ends:
True; every other line byte-unchanged (common prefix and suffix: True); 0 "|" inserted. GAPS: only l. 11 changes at each step: True; new
l. 11 = old l. 11 with its closing " |" replaced by " " + the filled UPDATE + " |": True; "|" on l. 11 76 -> 76 -> 76 (pipe count
unchanged); «UPDATE 2026-» 45 -> 45 plus 2 UPDATE heads with the simulation year 2099, R112's the last on the line; 23 -> 23 lines (wc
-l). Fill values used only for the simulation: <DATE> 2099-01-01 (R111) and 2099-01-02 (R112), <HH:MM> 00:00, <checker> 0000000. (10)
THIS DRAFT'S SHA1: a file cannot state its own sha1. The sha1 of this file with the forty hex digits after the next colon replaced by
forty «0» characters is: 9983313dd4c70db90da02d1a7e6a3ef5cf75af88. The file's actual sha1 and line count are in the hand-back to the
Lead (and re-measurable with sha1sum).

Addendum 2 (subagent, for the Lead; does not land; written 2026-11-06T08:45:53Z by date -u). (1) SECOND FILL on line L-3 (l-comp
9c70c980, sha1 d87bb3f0…), to CHECKER C123 Add. 1. NOT pushed; my commits: the four merges (--no-ff) 7ec75c1b, 66b46083, e1e3a8e9,
4eb26876 and one commit holding this file. (2) TITLE l. 315 = "### R112 [refereed-only] " + L-3 without its newline + ", CHECKER PASS
(docs/checker/C123.md, checker PENDING)", checked by script (chk112b.py): equal, byte for byte (True); the only «### R» heading of this
file; 13 + 1 «(» and 13 + 1 «)», balanced; no «[lane», no «P-TR3 [» in the title. (3) BODY l. 315-556 (python slice d[314:556]; 0 "|");
GAPS preamble l. 558-569 (two "|", both inside quotation marks: the row's closing « |» and «holds no "|"»); UPDATE l. 570 (d[569]; one
line, 0 "|", one each of <DATE>, <HH:MM>, <checker>; 1,735 bytes; sha1 21ab655986310c668c0ac4f8995e57ef1759716d of the line without
newline, computed on the UNFILLED form, as C123 §4 states it, «sha1 21ab655986310c668c0ac4f8995e57ef1759716d of the line without
newline»: equal). A landing script slices d[314:556] for the entry and reads d[569] for the UPDATE (with «R112», «R111» as PREV, «C123»,
and the GAPS l. 11 assertion on «RESULTS R111 (P-IDEAL-KEYS» as the last UPDATE). (4) NO PLACEHOLDER: both referees' byte tests of L-3
and REFEREE's Addendum 1 are on file, so everything in the entry is final for C123 Add. 1 (the only fill left is the title's «checker
PENDING)» and the UPDATE's three placeholders, at landing). (5) QUOTE SWEEP (chk112b.py: chk112.py's rule and sources, plus L-3, fixes
and the cert log at 9c70c980, R-P-TR3.md at 365f22e1 and 1140096d with tr3_rest13.txt, R2-P-TR3.md at ee1d6e18, C123, the trunk files
(RESULTS, GAPS, LEAD-STATE, NOW, R111-draft) at the local trunk, the commit subjects of the new commits, my second-fill outputs): 389
outermost quotes, 331 parts of 6+ characters, every part found (0 not found); in the title and body alone 143 quotes, 138 parts, 0 not
found; GAPS preamble and UPDATE 17 quotes, 12 parts, 0 not found. Line-precise: 167 of 167 (source, cited line range, quote) triples
found verbatim, whitespace-normalised, inside the cited lines. (6) WORD DIFF 35856ab5 → this file (wd112b.py, difflib on whitespace
tokens, Addendum 2 left out): 17 line regions, 70 token hunks (158 tokens deleted, 1730 inserted), every hunk in a region listed in the
SECOND FILL paragraph. (7) STALE STATUS in title and body (by script): «pending» 0 apart from the title fill «checker PENDING)»; «not
yet» once, REFEREE's L-1 verdict quoted as history (as at the first fill); «to follow» 0; «13 of the 16» 0; «on the lane's record» 0;
«[lane» 0 in the title and 3 times in the body, each naming the label L-3 deletes (Object, line history, F7); the 13 other cubes resting
on the lane's record occurs only inside the quote of fixes F4 (entry 1's text, l. 36-37, history; C123 named two stale sentences, (iv)
and Honest limits (ii), both replaced); «L-2» only as history (the line history, the L-2 verdicts and byte tests, fixes entry 1 and F7,
the DATA note of F6), never as the line of record; L-2 named as the current line («RESULTS line is L-2», «title is L-2», «The RESULTS
line (L-2)», «The line (L-2)», «L-2: «In the IDEAL», «L-2's DATA parenthesis», «(L-2, by script)»), by script: 0 times. (8) LANDING
SIMULATION (sim112b.py: sim112.py's R112 step, unchanged, on in-memory copies of RESULTS and GAPS at the local trunk, R111 as landed, no
R111 step): RESULTS 12,487 -> 12,730 lines (wc -l), a pure insertion of 243 lines (the entry block with "checker PENDING)" filled, plus
one blank line) directly after R111's landed block (R111 l. 11,598-11,907, blank l. 11,908, byte-unchanged: True; R110's block
byte-unchanged: True): True; R112 at l. 11,909-12,150, blank l. 12,151, the next line (**Erratum E-1**) moves to l. 12,152, «**Erratum
E-2**» to l. 12,165, «## Dead ends» to l. 12,193; order R110, R111, R112, E-1, E-2, Dead ends: True; every other line byte-unchanged
(common prefix and suffix: True); 0 "|" inserted. GAPS: only l. 11 changes: True; new l. 11 = old l. 11 with its closing " |" replaced
by " " + the filled UPDATE + " |": True; "|" on l. 11 76 -> 76 (pipe count unchanged); «UPDATE 2026-» 46 -> 46 plus 1 UPDATE head with
the simulation year 2099, directly after R111's and now the last on the line; 23 -> 23 lines (wc -l). Fill values used only for the
simulation: <DATE> 2099-01-02, <HH:MM> 00:00, <checker> 0000000. (9) NOT VERIFIED: the referees' tools not re-run (their files and logs
read; Addendum 1's log checked against the lane's record, rest13ck.py); the 13 proofs of Addendum 1 not regenerated by me;
scripts/verify.sh not run. (10) NOTE: fixes entry 2 cites the Lead at «07:38Z» (l. 75, 84, 85); dd4a55c6's commit time is
2026-11-06T07:36:20Z; no verdict depends on it. Scratch:
/tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad/r112/fill2/ (edit112b.py, c123txt.py,
chk112b.py, lp112b.py, wd112b.py, sim112b.py, l3rel112.py / l3rel112.out, rest13ck.py / rest13ck.out, upd112b.py / upd112b.out /
upd112L3.txt, prem112b.out, R112-draft-35856ab5.md).
