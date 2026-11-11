# Draft RESULTS R124 (Lead; first fill 2026-11-09T02:14:04Z by date -u (subagent) on P-N5-END line L-3, docs/new/P-N5-END-line-L3.txt, l-new 8b67d40e, sha1 d6afe92ae0d2c0021743c99d2bd10f16cad27c73 (draft sha1 f7aa004e, CHECKER C138 46905772: FAIL E-1, E-2); SECOND FILL 2026-11-09T06:17:06Z by date -u (subagent) on P-N5-END line L-4, docs/new/P-N5-END-line-L4.txt, l-new b7faeebe, sha1 5f88c2971718522027ae267754814c6ba401b829) — to CHECKER C138 Add. 1 — NOT LANDED; goes after R123 (LANDED at 9acebb5c, RESULTS l. 15076-15369), before Erratum E-1 — LANDED in RESULTS 2026-11-09 09:04Z (CHECKER C138 5b9f4af8 PASS), after R123, before Erratum E-1
SECOND FILL (2026-11-09T06:17:06Z by date -u, subagent; for CHECKER C138 Add. 1). Read at the origin heads of one fetch at
2026-11-09T06:04:22Z-06:04:24Z (date -u before and after the fetch; git fetch of claude/l-new, claude/referee, claude/referee-2,
claude/checker and claude/vibrant-johnson-nxvvxo; its exit code was not captured, the output having been piped to tail; a second fetch of
the same five branches at 2026-11-09T06:11:24Z-06:11:25Z: rc 0, every head unchanged; I merged, committed and pushed nothing, wrote nothing
into the repository and built this file in the scratchpad r124b/ by fill2.py): l-new 25e040ee (25e040ee694f13ed6175336962db714f1ac1e52b,
2026-11-09T04:48:58Z, «L-NEW 68: BOX 203 — Theorem GATE-CLASS (every gate flip changes a face class), Corollaries GATE-FLIP and QUIET-N
(PROVED, lane; IDEAL-CYC, landed premises); box 202 Addendum A (K1-POLY's REACH3-CYC condition; K1-FLIP(c) dead at k = 1)»), the branch head
(box 203 and the check.sh sentence below; not part of this entry); its parent b7faeebe (b7faeebe30a827f29628f978df5f2db174c7c432,
2026-11-09T04:48:50Z, «L-NEW 68: P-N5-END fixes entry 4 (C138 E-1, E-2; line-only) + line L-4 by script (sha1 5f88c297, 7,230 B)»), L-NEW
successor 68, the commit of record (fixes entry 4, L-4, mkl4_195.py, end.pins: the only P-N5-END objects git diff 8b67d40e b7faeebe names;
the packet and L-1 to L-3 are byte-equal at 8b67d40e, b7faeebe and 25e040ee, and git diff b7faeebe 25e040ee on the packet, the fixes file,
the four line files and experiments/new/box195/ is empty). 25e040ee adds to the check.sh block «P-N5-END» the assertion of L-4's sha1 and
size (experiments/new/check.sh l. 1031-1033 at 25e040ee: «# fixes entry 4 (C138 E-1, E-2): line L-4 = L-3 + R-U + R-T0 must be CHECKER's
5f88c297… (7,230 B)»). 8b67d40e → 14babccb → fbb62710 → b7faeebe → 25e040ee is an ancestor chain (git merge-base --is-ancestor; b7faeebe is
25e040ee's parent). By git, b7faeebe is the commit and 5f88c2971718522027ae267754814c6ba401b829 the sha1 of the file
docs/new/P-N5-END-line-L4.txt (the file's only commit; its blob is e6f009bffa65c97d8ae771d9da4fab2af88ba57a). referee 37195499
(3719549937af51513003a071861220929e23f196, 2026-11-09T05:27:35Z, «REFEREE successor 30: R-P-N5-END §E (L-4 5f88c297 MATCHES; S3's τ = packet
τ0; entry 4 line-only)»), the branch head: docs/referee/R-P-N5-END.md there 268 lines, 27,040 bytes, sha1
0c31b3d834ee285ed6631321f4857ac2038333b6; its first 24,567 bytes (l. 1-246) are ae980555's file, = 4434597c's (the file of the first fill),
by prefix test; §E is l. 248-268, with docs/referee/scratch/end_l4.py and scratch/end_logs/l4test.out (git diff ae980555 37195499 names
these three files only). referee-2 63a3cf87 (63a3cf87c0ea0faa106fddef23d421bbe5c8ec90, 2026-11-09T05:27:17Z, «REFEREE-2 successor 35:
P-N5-END L-4 MATCHES (Add. 3: R-U + R-T0; S3's τ = packet τ0)»), the branch head: docs/referee-2/R2-P-N5-END.md there 278 lines, 24,201
bytes, sha1 3dfdf3240b4f70a9d35a178c70723a6561558145; its first 22,597 bytes (l. 1-263) are c1e71a25's file, = 0e5c7c37's (the file of the
first fill), by prefix test; Addendum 3 is l. 265-278, with R2-P-N5-END/bt_l4.py and bt_l4.out (the only other files git diff c1e71a25
63a3cf87 names). checker 46905772 (46905772ddea51544309e7ba62aa3a1ed229349f, 2026-11-09T04:15:52Z, «CHECKER C138: R124 (P-N5-END) first fill
f7aa004e @ b3c7b461 on L-3 FAIL E-1 (scope words, UPDATE reading), E-2 (τ0 undefined); L-4 5f88c297, UPDATE 8cd83060; box 195 rc 0, DATA
equal, quotes 0 NF, landing sim R124 l. 15371-15562»), the branch head, after e7fb3028 (C137 CLOSED) and a0d7cb24 (C137 Add. 1):
docs/checker/C138.md 97 lines, 11,442 bytes, sha1 10645f1b6e38cb0dde5e19d15fdfdd3581a3c907, sections §1-§6, no Addendum.
ANCESTRY (git merge-base --is-ancestor against origin trunk 090f89d4 and the local HEAD b8408b39): every commit the first fill named as an
ancestor still is (131b4c1c, a60733b8, 2fcee038, 8b67d40e; REFEREE's e4cb208a, 407f4a21, 4434597c, ae980555; REFEREE-2's 9b3cc9b6, 0f82f03b,
0e5c7c37, c1e71a25; and checker 2101cd36). NOT ancestors, and needed for landing: claude/l-new b7faeebe (fixes entry 4, L-4, mkl4_195.py,
the re-pinned end.pins) with its head 25e040ee (the check.sh L-4 assertion that fixes entry 4 l. 114 names, D-6), claude/referee 37195499
(§E), claude/referee-2 63a3cf87 (Addendum 3) and claude/checker 46905772 (C138; e7fb3028 and a0d7cb24 before it are not ancestors either),
and C138 Add. 1's commit when it exists. The L-RED commits the line cites as records (6f56004c, 143f0b4c, 86a7a7a8) are still not ancestors;
C138 §5 ruled them records, not premises. So the Lead merges claude/l-new (b7faeebe or later; 25e040ee for the check.sh assertion),
claude/referee (37195499 or later), claude/referee-2 (63a3cf87 or later) and claude/checker (46905772 and C138 Add. 1) before landing.
Trunk: origin trunk 090f89d4 (090f89d4ea1151401cc1967eb28cdb3cab959e66, 2026-11-09T04:12:23Z, «Lead: log 03:08Z-04:12Z + resume point; NOW +
LANE-RESTART rows (L-SI 49, L-RED 63, L-NEW 68, L-COMP 15)»), = b3c7b461 (the first fill's commit) plus docs/NOW.md,
docs/agents/LANE-RESTART.md and docs/agents/LEAD-STATE.md (git diff --name-only); docs/agents/R124-draft.md there is the first fill, sha1
f7aa004ef679480d31aa4d177de3abcad8462786 (fill2.py asserts it). The local HEAD is b8408b39 (b8408b39d5b3ae70980256e7b4e5165fc74d066c,
2026-11-09T05:17:31Z, «Lead: log 04:12Z-05:17Z + resume point (R124 C138 FAIL line-only -> L-4; K1-FLIP(c) DEAD; per-gate flip bound);
LANE-RESTART rows L-NEW 68, L-COMP 15»), not on origin at my fetches; it changes docs/agents/LANE-RESTART.md and LEAD-STATE.md only. RESULTS
and GAPS at 090f89d4 and at b8408b39 are byte-equal to 9acebb5c's: RESULTS sha1 428bc92f5ddd4167bb8b2bac88eb04cc9de97c19, 16,013 lines,
1,477 «|»; «### R123» l. 15076, its block to l. 15369, blank l. 15370, the line-start «**Erratum E-1** (not a result» l. 15371, «**Erratum
E-2**» l. 15384, «**Note E-3**» l. 15412, «## Dead ends (kept;» l. 15443; GAPS sha1 82e9d475ef5e288f42152fbde61dd1498c4505f0, 23 lines, l.
11 76 «|», 58 «UPDATE 2026-», the last R123's «UPDATE 2026-11-09 00:52Z: RESULTS R123 (P-N5-QUIET; CHECKER C137 3479ecb0)». «R124», «C138»,
«P-N5-END» and «S3's τ» occur 0 times in RESULTS and in GAPS.
New sources (read in full): docs/checker/C138.md at 46905772; fixes entry 4 (docs/new/P-N5-END-fixes.md l. 94-114 at b7faeebe; the file 114
lines, 12,917 bytes, sha1 0a0cf11505a1b811ee3383fab3d1228328b6e097; its first 10,024 bytes = 8b67d40e's file, by prefix test); L-4
(b7faeebe); experiments/new/box195/mkl4_195.py and end.pins at b7faeebe (45 rows: 8b67d40e's 43 with the fixes file re-pinned, and L-4 and
mkl4_195.py added); experiments/new/check.sh l. 1020-1038 at 25e040ee (the blocks «BOX 195 END» and «P-N5-END»); REFEREE §E (l. 248-268 at
37195499) and its scratch/end_logs/l4test.out (read; end_l4.py listed, not re-run); REFEREE-2 Addendum 3 (l. 265-278 at 63a3cf87) and its
bt_l4.out (read; bt_l4.py listed, not re-run); notes/CHECKER.md l. 5-7 at 46905772; docs/agents/LEAD-STATE.md at b8408b39 l. 2995 and 3000
(the C138 routing, 04:45Z-04:46Z); the R123 second fill (72278533, sha1 a1ab70ef) and the R122 third fill (40e6ffb8), the house form of a
re-point after a line-only CHECKER FAIL.
WHAT CHANGED SINCE THE FIRST FILL. CHECKER C138 (46905772) FAILED the first fill (draft f7aa004e at trunk b3c7b461): «Verdict: **FAIL** on
two line-only items (E-1, E-2); the mathematics, DATA, tools and placement PASS» (l. 16). E-1 is the first fill's G-U (i): «By C134 E-3 an
UPDATE that needs a reading is an E-item: the line must carry the landed words so the procedure runs unchanged. Fix: R-U (§4).» (l. 21-22);
E-2 is the first fill's G-2 (ii): «but a signed clause must state it. Fix: R-T0 (§4).» (l. 27). «Both fixes are line-only: no statement,
label, hypothesis, premise or DATA number changes. With them, R124 may land (Add. 1 on the second fill).» (l. 28-29). C138 ruled the first
fill's other flags: «**G-U (iii), (iv) (labels moved by the procedure): no action.**» (l. 32), «**G-1 (ii) (S1 narrows E1's clause vs the
frozen Corollary): no action.**» (l. 36), «**G-4 (ii) (S3-START for every genome): no action (the C137 N-G4 rule).**» (l. 40), «**G-6
(«Lemma E0» vs «Lemma E0-BOUND»): no action.**» (l. 43), «**G-11 («P-N5-QUIET» named, now RESULTS R123): optional, no action.**» (l. 45) and
«**G-7 / L41: not triggered.**» (l. 47). L-4 = L-3 + R-U, then R-T0 (fixes entry 4, L-NEW successor 68, b7faeebe; «Fixes entry 4 (L-NEW
successor 68; LINE-ONLY; written 04:46Z by date -u)», l. 94), as C138 §4 gave it: «**L-4** = L-3 + R-U + R-T0 sha1
**5f88c2971718522027ae267754814c6ba401b829**, 7,230 B» (l. 58-59); R-U and R-T0 are the first fill's proposed strings (C138: «These equal
the drafter's proposals (draft l. 94-97); I derived them independently.», l. 59-60). Both referees MATCH L-4: REFEREE successor 30,
«Verdict: fixes entry 4 CORRECT. **Line L-4 MATCHES** (L-3 + exactly R-U and R-T0). Statements as signed (§0; END-T3 PROVED-CONDITIONAL on
REACH3-CYC).» (§E l. 267-268 at 37195499); REFEREE-2 successor 35, «(4) Verdict: **L-4 MATCHES** (byte test, and in meaning). Statement
verdicts unchanged.» (Add. 3 l. 278 at 63a3cf87). Both read entry 4 as line-only (REFEREE §E l. 265-266; REFEREE-2 Add. 3 «(3) Fixes entry 4
is line-only.», l. 277) and R-T0 in meaning (§E l. 256-260: «so «S3's τ» names τ0 in the line's own terms, for both N5′-xi and N5 (same S3).
CORRECT; no change of meaning.»; Add. 3 l. 272-274: «So τ0 is S3's τ by definition»). The UPDATE is the first fill's with C138's two
replacements, «**8cd83060b9cb5d22f3b3e4dfeb0ec6588e0dded0** (unfilled, no newline), 7,260 B» as C138 §4 gave it (l. 62-63), now built by
R118's procedure from L-4 with NO reading. C138's instruction for this fill, «The second fill must also refresh the entry block's own L-3
references (sha1, bytes, the «their form is G-U» sentence, l. 470-476 etc.) to L-4; Add. 1 checks that by word diff.» (l. 65-66), is met
below (Changes at this fill).
Checks run at this fill (scratch /tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad/r124b;
nothing written into the repository). (a) tools/l4rel124b.py: R-U and R-T0 parsed from C138 §4 (l. 52-57, wrapped lines joined with one
space) = fixes entry 4's table strings (l. 107-108) = mkl4_195.py's tuples (read by ast, not executed) = the first fill's strings in
r124a/tools/upd124a.py (True ×6); each old string once in L-3 and 0 times in L-4, each new string 0 times in L-3 and once in L-4; L-3 + R-U
= 2f8a11f90c02c94d8b4e95dd260eb5db49ac6a95 (7,226 bytes, = C138's); L-3 + R-U + R-T0 = L-4 (True). L-4 =
5f88c2971718522027ae267754814c6ba401b829, 7,230 bytes, one line with its newline, 7,105 characters, 1,223 tokens, 105 «(» / 105 «)», depth
never negative, final depth 0, 0 "|", one « — », «τ0» 0, «S3's τ» once, «so this is not M4» once, «; not M3, not a step-4 pass, not a
TARGET.md claim» once, «G-N5-TIME stays OPEN» once, «N5′-xi stays a CANDIDATE (D1)» once, «(2026-11-08)» once, «R1xx» 0,
«referee-originated» 0, «PROVED-CONDITIONAL» twice; R-labels R104, R117, R118, R15, R57 (and R221, R222, R223, L-RED's reports), as in L-3;
token diff L-3 → L-4: 4 hunks, 7 tokens out, 11 in, all inside R-U and R-T0. mkl4_195.py re-run from a copy of the packet and L-3 of the
archive of 25e040ee (scratch arch_mk/; L-4 not copied): rc 0, «R-U, R-T0 old once each, applied; sha1
5f88c2971718522027ae267754814c6ba401b829 7230 bytes; parens 105 105 ; tau0 0», output cmp-equal to L-4. (b) The two check.sh blocks (l.
1020-1038 at 25e040ee = tools/blocks195b.sh) from a FULL git archive of 25e040ee (r124b/arch/, every path of the tree, 47,575 files),
started after 2026-11-09T06:07:47Z and ended 2026-11-09T06:11:12Z by date -u, rc 0, output «BOX 195 END: E0-E4 / ENDGAME-3 (xi and spec) 0
failures, controls fire = frozen: PASS» and «P-N5-END: packet and 45 pinned files match end.pins: PASS»; NEGATIVE CONTROL: the «P-N5-END»
block (l. 1029-1038) on the same archive with one byte appended to L-4 printed «P-N5-END check: FAILED» and «L-4: sha1
641087018905ac00069babe15760a6a10acbf326, 7231 B (expected 5f88c297…, 7230 B)», rc 1; L-4 restored (sha1 5f88c297…) and the block re-run:
PASS, rc 0. (c) tools/upd124b.py: the UPDATE by R118's procedure (the first fill's direct() of upd124a.py, unchanged) from L-4 with NO
reading: sha1 8cd83060b9cb5d22f3b3e4dfeb0ec6588e0dded0 without newline (58a216f401f49db359fc3eee398894446c64323d with it; = C138 §4's
UPDATE-4, True), 7,260 bytes, 7,138 characters, 1,222 tokens, 105 «(» / 105 «)», 0 "|", one each of the three fill tokens, «2026-11-08» 0, «
— » 0, «τ0» 0, «S3's τ» once; = the first fill's d[487] (262a881c…) with «is not M4 (P-N5-END» → «is not M4, so this is not M4 (P-N5-END»
and «κ0 and τ0 (Theorem ENDGAME-3» → «κ0 and S3's τ (Theorem ENDGAME-3» (True); on L-4 with the first fill's reading: AssertionError (the
dropped words are gone). CONTROL: the same function with R123's constants on R123's L-4 (87603d07) and no reading gives 739c5f71…, which
filled with 2026-11-09, 00:52, 3479ecb0 occurs once on GAPS l. 11 at 090f89d4 and ends it (True). Token diff L-4 → UPDATE: 18 hunks, 147
tokens out, 146 in (the head; the nine labels behind their clauses, END-T3's after the premises parenthesis in place of « (2026-11-08) —»;
«M4; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim» → «M4»; «§10-§11)» → «§10-§11). G-N5-TIME stays open.»), the
hunk kinds of C138 §3. (d) tools/chk124b.py (title, block, UPDATE, pipes, the fill token, parentheses, stale grep, quote sweep with a
negative control), tools/lp124b.py (quotes new at this fill at their cited lines), tools/sim124b.py (landing simulation on 090f89d4),
tools/rec124b.py (the kept sections byte-unchanged; word diff of the entry against the first fill) and tools/hex124b.py (hex ids): Addendum
2.
The first fill's flags, as C138 ruled them, in L-4 (string checks by script, l4rel124b.py): G-U (i) = E-1 by R-U: L-4 ends its scope words
«is not M4, so this is not M4; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim (P-N5-END», so R118's procedure
applies with no reading ((c)). G-2 (ii) = E-2 by R-T0: ENDGAME-3's clause now reads «iterations 1, …, F − 1 being S4a steps with K-config κ0
and S3's τ;», «τ0» 0 times in L-4; the packet's «τ0 := pe_g at every gate g and K2 → K2» (§2 (S), l. 90-91) is S3's τ, as both referees read
it ((a) above; REFEREE-2 Add. 3: ««S3's τ» is exactly the proof's object, and E0 says it never changes before the end.», l. 274). G-U (iii),
(iv), G-1 (ii), G-4 (ii), G-6, G-11 and G-7: «no action» / «not triggered» (C138 §3); L-4 changes none of them (the labels, E1's clause, the
premises parenthesis and the source note are byte-equal in L-3 and L-4: the token diff has 4 hunks, all inside R-U and R-T0).
NOTES at this fill (for CHECKER; no line change proposed):
- D-6, FIXES ENTRY 4's CHECK.SH SENTENCE. Fixes entry 4 at b7faeebe says «check.sh block «P-N5-END» also asserts L-4's sha1 by name.» (l.
  114); at b7faeebe the check.sh blocks «BOX 195 END» and «P-N5-END» are l. 1020-1035, byte-equal to 8b67d40e's (check.sh itself changed
  between them only by other boxes' blocks): the assertion is added by the next commit, 25e040ee (l. 1031-1033). The sentence holds once
  claude/l-new is merged at 25e040ee or later; end.pins at b7faeebe pins L-4 by sha1 in any case, and the block at b7faeebe would print «45
  pinned files».
- D-7, STAMPS (history, no verdict affected). C138: «Report 2026-11-09 04:15Z by date -u.» (l. 2), commit 46905772 at 04:15:52Z; LEAD-STATE
  at b8408b39 logs it under «04:45Z» and the routing to L-NEW 68 under «04:46Z» (l. 2995). Fixes entry 4's heading «written 04:46Z by date
  -u» (l. 94) and the routing it quotes, «DUTY NOW … E-1 … → R-U … E-2 … → R-T0» (l. 96-97); b7faeebe at 04:48:50Z. REFEREE §E's heading
  «date -u at writing 2026-11-09T05:27Z» (l. 248), commit 05:27:35Z; REFEREE-2 Add. 3's heading «2026-11-09 05:27Z by date -u» (l. 265),
  commit 05:27:17Z; both name the routing «Lead 05:27Z» (l. 249; l. 266).
- D-8, C138 §3 G-6's COUNT. C138 says ««E0-BOUND» occurs once in RESULTS (l. 7476, an earlier entry's lemma)» (l. 43); at 9acebb5c =
  090f89d4 «E0-BOUND» is on two lines of RESULTS, l. 7476 (R95's title) and l. 7535 (R95 (d) «Lemma E0-BOUND», the first fill's G-6
  citation). The ruling (no landed label «Lemma E0»; C138 «grep: 0», l. 44) is unaffected.
- D-9, THE BRIEF'S VERDICT WORDS. The brief for this fill gave the referees' L-4 verdicts as "P-N5-END L-4: MATCHES" (REFEREE §E) and
  "**P-N5-END L-4 MATCHES.**" (REFEREE-2 Add. 3); neither string occurs in either file at 37195499 / 63a3cf87 (grep). The entry quotes the
  files' verdict sentences: REFEREE §E l. 267-268, REFEREE-2 Add. 3 l. 278 (above).
- N-S AT L-4. The source note still names «fixes entries 1-2» and «L-NEW successors 63-64»; entries 3 (successor 65) and 4 (successor 68)
  are line-only. REFEREE §E: «Fixes entry 4 is line-only: R-U reorders status words; R-T0 replaces a symbol by its packet definition. No
  proof step, tool or pinned output changes, so the source note need not name it (C134 N-S); not L41's case.» (l. 265-266); REFEREE-2 Add.
  3: «(3) Fixes entry 4 is line-only.» (l. 277); fixes entry 4: «No statement, label, hypothesis, premise, proof or DATA number changes; the
  packet stays frozen» (l. 97-98); C138 ruled the first fill's G-1 «no action» on the same rule (C134 N-S) for entry 3. Honest limits (vii)
  records it.
- N-L41 AT L-4. C138: «**G-7 / L41: not triggered.** No proof step is referee-originated» (l. 47); REFEREE §E: «not L41's case» (l. 266).
  R-T0 replaces a symbol by its packet definition and R-U reorders status words; neither is a proof step. «referee-originated» 0 times in
  L-4.
Changes at this fill, and nothing else: line 1 (the header: the first fill's draft sha1 and C138 verdict, the SECOND FILL clause, to CHECKER
C138 Add. 1, R123 LANDED); this section (new); the title (L-4: R-U, R-T0); in the entry: Object (successors 63-65 and 68; the packet also at
b7faeebe and 25e040ee), Fixes (entry 4; the fixes file at b7faeebe), The RESULTS line is (L-4 the line of record; line history L-1 to L-4;
the L-4 rounds, REFEREE §E and REFEREE-2 Addendum 3), Claims signed (§E, Addendum 3; the L-4 re-signatures; C138's E-items taken), Setting
(fixes entries 1-4) and (g) (one sentence: the line's «S3's τ» is the packet's τ0), The RESULTS line (L-4; R-T0 and R-U in its clause list),
L41 and L43 (L-4; C138's G-7 ruling and REFEREE §E in place of the first fill's open question to the Lead), Fixes (header; a new sub-bullet
for entry 4; the closing bullet), Honest limits (vii), Data (box195 at b7faeebe / 25e040ee; this fill's re-run, its negative control,
REFEREE §E's pins check and C138's re-run), Signatures (§E, Addendum 3; successor 68's commit), INDEPENDENCE (L-4's strings and byte tests),
TARGET.md diff (L-4, R123's landed form); the GAPS preamble and the UPDATE (rebuilt from L-4 with no reading); Addendum 2 (new, at the end).
The FIRST FILL record (from "FIRST FILL (this text)" to (14)) and the first fill's Addendum (1)-(10) are kept byte-unchanged (rec124b.py):
where they call L-3 the title or the line of record, raise G-U, G-2 (ii), G-7, G-1 (ii), G-4 (ii), G-6 or G-11 as flags, propose R-U or
R-T0, or give their line numbers, counts, slices, UPDATE sha1 (262a881c…) and block run (43 pinned files), they describe draft f7aa004e at
02:19Z; C138 ruled at 04:15Z, and the entry block now follows L-4.
FIRST FILL (this text). Built by script (r124a/fill1.py) in the scratchpad r124a/ for the Lead to copy to docs/agents/R124-draft.md; nothing
in the repository was edited, committed, merged or pushed by me, and scripts/push.sh and scripts/verify.sh were not run. Read at the origin
heads of one git fetch at 2026-11-09T01:59:33Z by date -u (date -u before it 01:59:33Z, after it 01:59:34Z; claude/l-new, claude/referee,
claude/referee-2, claude/checker, claude/vibrant-johnson-nxvvxo; rc 0; a second fetch 2026-11-09T02:14:03Z-02:14:04Z by date -u of the same
five branches and claude/l-red: rc 0, every head unchanged, l-red d345717a, read for the ancestry of the L-RED commits the line cites):
l-new 14babccb (14babccb0d3f939109a991b556d2e707c10893ca, 2026-11-09T01:20:35Z, «L-NEW N5-CORE-forms: the seven equivalent forms of
G-N5-TIME on Γ3 (T3, Rtop, A, C, Dmax, A*, R) with exact definitions, the implication chain with constants and premises, proof of C ≤ A* ≤ 1
+ M·C, and the tight instance per form (MW, FW, DHIB26, RWX_n95, C6G8)»), the branch head; git diff 8b67d40e 14babccb on
docs/new/P-N5-END.md, docs/new/P-N5-END-fixes.md, the three P-N5-END line files and experiments/new/box195/: empty, so the objects are those
of 8b67d40e (8b67d40e6020d03d4eea18bf4c697a5193a709f7, 2026-11-08T10:18:46Z, «L-NEW 65: P-N5-CHAIN fixes entry 1 + L-2 (CL-1, CN-1);
P-N5-END fixes entry 3 + L-3 (L-R1, N-1, N-2, EL-1, EL-2); repins»), L-NEW successor 65, the commit of record. The chain 131b4c1c
(131b4c1c0b98cca2c0b40f6e9cf96c840a4deb25, 2026-11-08T04:10:38Z) (packet FROZEN; L-NEW successor 63) → a60733b8
(a60733b88b0b643f4235e60fe3f6029dddb46a0b, 2026-11-08T06:27:26Z) (fixes entry 1 + L-1; successor 64) → 2fcee038
(2fcee038fd1ef30c48c851641d48c71bf48bcd5b, 2026-11-08T06:58:09Z) (fixes entry 2 + L-2; successor 64) → 8b67d40e (fixes entry 3 + L-3;
successor 65) is an ancestor chain, and 8b67d40e is an ancestor of origin/claude/l-new. referee ae980555
(ae9805556a1feee09de9a95d2043607d591374bf, 2026-11-08T16:44:42Z), the branch head: docs/referee/R-P-N5-END.md there is byte-equal to
4434597c (4434597c947e8bca85792c10d49a1069b9a795ac, 2026-11-08T10:54:53Z, «REFEREE successor 30: R-P-N5-CHAIN §C (L-2 e481d260 MATCHES),
R-P-N5-END §D (L-3 d6afe92a MATCHES); asc_l6.py prepared»): 246 lines, 24,567 bytes, sha1 91eda5b02802b38f8171c9ca1d7a1019fa2255f3; its
first 21,795 bytes (l. 1-220) are the file at 407f4a21 (407f4a2158f2570dc98a2c865ae30b9cef88575c, 2026-11-08T08:09:56Z) (sha1
077039c7099c5cbd6fd80462c9b2c1a74ba7e154) and its first 17,064 bytes (l. 1-167) the report as first committed at e4cb208a
(e4cb208abe3c2bc5519fe87266cc71dec4458dab, 2026-11-08T06:09:15Z, «REFEREE 29: R-P-N5-END first review (all SIGN, END-T3 conditional; EXACT-L
tie-break note; line requirements LN-1..LN-8); notebook») (sha1 ae70407681b5393e22043f30b77e352c8a9db039) (by prefix test; git blame: l.
1-167 e4cb208a, l. 168-220 407f4a21, l. 221-246 4434597c). referee-2 c1e71a25 (c1e71a25596ff01554a1bd7390d7f8b0380a97d6,
2026-11-08T16:43:45Z), the branch head: docs/referee-2/R2-P-N5-END.md and docs/referee-2/R2-P-N5-END/ there are byte-equal to 0e5c7c37
(0e5c7c37b567320d97621914b462c17d94cbfb53, 2026-11-08T11:05:52Z, «REFEREE-2 successor 35: P-N5-END L-3 byte test (Add. 2: MATCHES);
P-N5-CHAIN second review (all SIGN, W-1 closed; L-1/L-2 NOT YET: R-1, R-2, R-4)»): 263 lines, 22,597 bytes, sha1
25a40f245ddc332170637c130391435b3104741c; its first 20,905 bytes (l. 1-241) are the file at 0f82f03b
(0f82f03b0e66a4e175a710d19aad37e813fff430, 2026-11-08T09:30:50Z) (Add. 1; sha1 7b9f6f2631451082111647bd8665bb8adf836aff) and its first
18,201 bytes (l. 1-212) the report at 9b3cc9b6 (9b3cc9b6fd2aae5946cec5e232fd9cb241987a47, 2026-11-08T09:10:47Z, «REFEREE-2 34: R2-P-N5-END
second review: all statements SIGN (END-T3 PROVED-CONDITIONAL); line L-2 NOT YET (L-R1)») (sha1 0d7c8a152197ee7ccf18b3c17f249ab488aa6607)
(git blame: l. 1-212 9b3cc9b6, l. 213-241 0f82f03b, l. 242-263 0e5c7c37). checker 2101cd36 (2101cd36e33378d6818e2e0e79965822f29489cb,
2026-11-09T00:52:56Z, «CHECKER C136 CLOSED: CI of record #7176 green on ac9ab013 (descendant of aaf52291, RESULTS/GAPS byte-equal); resume
point»), the branch head: docs/checker/ ends at C137.md; C138.md does not exist; «C138» 0 times in notes/CHECKER.md, «P-N5-END» twice (its
queue: «Coming: P-N5-END, P-N5-CHAIN (L-NEW).» and «Then R123 (P-N5-QUIET), P-N5-END, P-N5-CHAIN.»).
ANCESTRY (git merge-base --is-ancestor against origin trunk 9acebb5c): the packet, fixes and line commits 131b4c1c, a60733b8, 2fcee038,
8b67d40e, REFEREE's e4cb208a, 407f4a21, 4434597c (and its head ae980555), REFEREE-2's 9b3cc9b6, 0f82f03b, 0e5c7c37 (and its head c1e71a25)
are ALL ancestors (they reached trunk through earlier merges of claude/l-new, claude/referee and claude/referee-2), and every one of their
P-N5-END files is byte-equal at 9acebb5c (git diff --quiet). NOT ancestors: l-new's head 14babccb (not needed: no P-N5-END file changed
after 8b67d40e), checker 2101cd36 (C138 is still to be written; merge claude/checker at its C138 commit before landing, as for C137), and
the L-RED commits the line cites as L-RED's counters, «cited, not re-run»: 6f56004c (L-RED 57 R222), 143f0b4c (L-RED 58 R223) and 86a7a7a8
(ideal.traj); each is an ancestor of origin/claude/l-red d345717a, and R123 landed citing claude/l-red d49b9f0c the same way. So nothing but
claude/checker (C138) needs a merge before landing.
Trunk: origin trunk 9acebb5c (9acebb5cd18dd24f2dbe850c137a225928db2656, 2026-11-09T00:52:57Z, «Lead: land RESULTS R123 (P-N5-QUIET:
LOC-GATE, CN2, LOC-K2, QUIET, T-QUIET, UP-T, ASC-T; line L-4) after R122, before Erratum E-1 (CHECKER C137 3479ecb0 PASS); GAPS G-N5-TIME
update; NOW counters + rows; log 23:50Z-00:53Z»), the local HEAD's ancestor; the local HEAD is a773c562
(a773c562be4b7ca32787789bc9c40156d4692a8e, 2026-11-09T01:59:41Z, «Lead: log 00:53Z-02:00Z (C136 CLOSED; R123 on origin; BOX 200 / BOX 91
verdicts; cap-scaling linear)») (it changes docs/agents/LEAD-STATE.md only; RESULTS and GAPS equal at both). RESULTS: sha1
428bc92f5ddd4167bb8b2bac88eb04cc9de97c19, 16,013 lines, 1,477 «|»; «### R123» l. 15076, its block to l. 15369, blank l. 15370, the
LINE-START «**Erratum E-1** (not a result» l. 15371 (the only line-start occurrence), «**Erratum E-2**» l. 15384, «**Note E-3**» l. 15412,
«## Dead ends (kept;» l. 15443. GAPS: sha1 82e9d475ef5e288f42152fbde61dd1498c4505f0, 23 lines, l. 11 76 «|», 58 «UPDATE 2026-», the last
R123's «UPDATE 2026-11-09 00:52Z: RESULTS R123 (P-N5-QUIET; CHECKER C137 3479ecb0)». «R124», «C138», «P-N5-END», «TERM-XI», «ENDGAME-3»,
«EXACT-L», «END-T3», «SELFL_n3», «box195» and «κ1» occur 0 times in RESULTS and in GAPS.
Sources read: the packet docs/new/P-N5-END.md (frozen 131b4c1c, unchanged at a60733b8, 2fcee038, 8b67d40e and 14babccb; sha1
5cae845b1da1a1c40b52e73da6edae3d6aadbf29, 228 lines, 22,967 bytes; read in full); docs/new/P-N5-END-fixes.md at 8b67d40e (sha1
1cd757a38a294669f40c8c7c6496b62143dec8a6, 92 lines, 10,024 bytes; read in full; by prefix test its first 7,670 bytes (l. 1-73) are the file
at 2fcee038, sha1 45a689ead96b30aa5fd67ad12aca2d2d7d0b1da5, and its first 3,570 bytes (l. 1-34) the file at a60733b8, sha1
a508aec15785bbd403cad0c75b3c068b1c22fe39; git blame: l. 1-34 a60733b8, l. 35-73 2fcee038, l. 74-92 8b67d40e); line L-1
docs/new/P-N5-END-line-L1.txt (a60733b8, sha1 68a691764c57ef16bb8a8c294925954a3c71fb1b, 5,903 bytes); L-2 docs/new/P-N5-END-line-L2.txt
(2fcee038, sha1 e8a8ac51cc79c9de4000749899e7f0b860eeebe5, 6,988 bytes); L-3 docs/new/P-N5-END-line-L3.txt (8b67d40e, the file's only commit;
sha1 d6afe92ae0d2c0021743c99d2bd10f16cad27c73, 7,215 bytes, one line with its newline; read in full); experiments/new/box195 at 8b67d40e:
check195.sh, eg195.py (counters l. 56-104, docstring l. 1-24), end.pins (43 rows), check195.out (138 lines), data/sweep195.out (46 lines),
data/selfl195.out; the check.sh blocks «BOX 195 END» and «P-N5-END» (experiments/new/check.sh l. 1020-1035 at 8b67d40e, byte-equal at
9acebb5c); REFEREE's file at e4cb208a, 407f4a21 and 4434597c and its end_logs/tiedep.out at e4cb208a (read; scratch tools listed, not
re-run); REFEREE-2's file at 9b3cc9b6, 0f82f03b and 0e5c7c37 (read; tools listed, not re-run); RESULTS R15 (l. 624; (c) l. 636-638), R57's
heading (l. 2893), R104 (l. 9864; l. 9910, 9976-9977), R117 (l. 13362; (b), (c), (e), (f) at l. 13425-13452), R118 (l. 13607; (k) l.
13704-13712; l. 13743-13744; (ii) l. 13805-13809), R123 (l. 15076-15369, the house form); SPEC docs/new/N5-ssi-global.md at 9acebb5c (S1-S5
l. 26-59, FIX 1 l. 81, FIX 3 l. 88); P-N5-REACH.md l. 202 and P-N5-XICYC.md l. 171 at 9acebb5c; GAPS l. 11; DECISIONS l. 355-360 (L41);
TARGET.md §2, §4; docs/checker/C133.md-C137.md and notes/CHECKER.md at 2101cd36 (verdicts, E-items, N-S, N-L41 and G-U rulings);
docs/agents/LEAD-STATE.md at a773c562 (grep: P-N5-END, R124, S6); the R123 draft's first fill (5a2f8bda, sha1
8f361e5572926ffddda3e6d418b71c7d9685ac88; the house form) and R123 as landed; the tools of r123b/ and r122c/ (upd123b.py's direct build,
sim123b.py, chk123b.py, hex123b.py, read and adapted).
Checks run at this fill (scratch r124a/; outputs there). (a) The check.sh blocks «BOX 195 END» and «P-N5-END» (experiments/new/check.sh l.
1020-1035 at 8b67d40e = tools/blocks195.sh) run from a FULL git archive of 8b67d40e (r124a/arch/, every path of the tree),
2026-11-09T02:03:20Z-2026-11-09T02:06:53Z by date -u, rc 0, output «BOX 195 END: E0-E4 / ENDGAME-3 (xi and spec) 0 failures, controls fire =
frozen: PASS» and «P-N5-END: packet and 43 pinned files match end.pins: PASS» (the first re-runs check195.sh, diffs it against the pinned
check195.out, requires 0 in every fail counter outside the «ctrl» lines and both controls to fire; the second checks the 43 pins). (b)
tools/upd124a.py: the UPDATE by R118's procedure, with the control that the same function rebuilds R123's landed UPDATE on GAPS l. 11 from
R123's L-4 (True). (c) DATA, clause by clause, against eg195.py, check195.sh, check195.out and sweep195.out (G-9). (d) tools/chk124a.py
(title, block, UPDATE, quote sweep with a negative control, stale grep), tools/lp124a.py (every quote at its cited file, commit and lines,
with negative controls), tools/hex124a.py (every hex id) and tools/sim124a.py (landing simulation on 9acebb5c): Addendum.
LESSONS APPLIED (R123's first fill list, plus C137). C113 E-1 / C123 E-1 / C133 E-1: the title is L-3 verbatim, nothing inserted and nothing
stripped (CLEAN). C133 E-3 / C134 E-3: the scope tail carries the landed status words (G-U: FLAG). C135 E-4 / C135 Add. 1 E-5: every term of
a signed clause defined in the line or landed (G-2 (ii): FLAG, «τ0»). C132 E-7 / C133 E-6 / C134 E-2 / C135 E-2 / C137 N-L41: a
referee-originated proof step is named in the scope tail (G-7: none found in my reading; the Lead rules). C122 E-3 / C132 E-2 / C133 E-2 /
C134 E-1 / C135 E-1 with C134 N-S: the source note names the authors of proof-bearing text (G-1: CLEAN in my reading, CHECKER's call). C117
E-1 / E-2 / C135 E-3: no READING inside a signed clause (G-2: CLEAN). C118 E-1 / C132 E-1: no status word that goes stale at landing (G-11:
CLEAN). C115 E-1: premises against RESULTS, landed entries only (G-4: all landed; notes). C120-C137: every DATA clause tested against its
counter's code for unit, set and scope (G-9). C122 G-0: parentheses balanced (105 / 105). C116 G-2 / G-3: names (G-6) and pins (G-12). C119
E-1: every «referee X did Y» checked against that referee's file. C130 G-P / C133 G-P: the UPDATE builder carries a control for the last
landed UPDATE (R123, True). C132 Add. 1: block re-run times as a date -u interval.
FLAGS FIRST (G-U and G-2 (ii) make CHECKER FAIL as L-3 stands by the C133 E-3 / C134 E-3 and C135 E-4 precedents in my reading; G-7 is for
the Lead (no L41 case found); G-1 (ii), G-4 (ii) and the G-9 notes are CHECKER's rulings, with no string needed). Exact replacements R-U and
R-T0, each old string once in L-3, by script (tools/upd124a.py): L-3 + R-U: sha1 2f8a11f90c02c94d8b4e95dd260eb5db49ac6a95, 7,226 bytes; its
UPDATE by R118's procedure with NO reading 0d9faf25ad5f20bef06e38e22f6efc4c584d97f9 (7,256 bytes) = the draft's UPDATE with «is not M4
(P-N5-END» → «is not M4, so this is not M4 (P-N5-END» (True). L-3 + R-U + R-T0: sha1 5f88c2971718522027ae267754814c6ba401b829, 7,230 bytes;
UPDATE 8cd83060b9cb5d22f3b3e4dfeb0ec6588e0dded0 (7,260 bytes).
- G-U, THE STATUS WORDS AND THE UPDATE PROCEDURE (FLAG; the C133 E-3 / C134 E-3 class; CHECKER FAIL as it stands in my reading). L-3's tail
  ends «; no separate DATA for TERM-XI and END-T3; G-N5-TIME stays OPEN, N5′-xi stays a CANDIDATE (D1); TARGET.md §2 (M4) asks for an
  algorithm polynomial on every parity game and §4 says a bound on a restricted class is not M4: not M3, not M4, not a step-4 pass, not a
  TARGET.md claim (P-N5-END, …». C134 E-3: «every landed line R90-R119 except R112 reads «not M3, not a step-4 pass, not a TARGET.md
  claim»»; 33 of the 34 landed titles R90-R123 carry «not M3, not a step-4 pass, not a TARGET.md claim» (by script), and R123, the last,
  reads «… is not M4, so this is not M4; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim (P-N5-QUIET» (R123's R-U,
  C137 PASS). L-3 has neither form: the inserted «not M4» and the colon. R118's procedure (the direct build of r123b/tools/upd123b.py,
  unchanged but for R124's constants) asserts «; not M3, not a step-4 pass, not a TARGET.md claim» once and fails on L-3 (upd124a.py (2):
  AssertionError). The draft's UPDATE is therefore built with ONE READING: «G-N5-TIME stays OPEN, » dropped as landed (the UPDATE ends «.
  G-N5-TIME stays open.»), and «: not M3, not M4, not a step-4 pass, not a TARGET.md claim» dropped in place of the landed «; not M3, not a
  step-4 pass, not a TARGET.md claim», so that «… is not M4» ends the scope words. Proposed R-U (R123's landed form; the CANDIDATE clause
  kept, now first): "; G-N5-TIME stays OPEN, N5′-xi stays a CANDIDATE (D1); TARGET.md §2 (M4) asks for an algorithm polynomial on every
  parity game and §4 says a bound on a restricted class is not M4: not M3, not M4, not a step-4 pass, not a TARGET.md claim (P-N5-END" → ";
  N5′-xi stays a CANDIDATE (D1); TARGET.md §2 (M4) asks for an algorithm polynomial on every parity game and §4 says a bound on a restricted
  class is not M4, so this is not M4; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim (P-N5-END". Old string once in
  L-3. With R-U, R118's procedure applies with no reading and gives the UPDATE above (True). (ii) «N5′-xi stays a CANDIDATE (D1)» is LN-7's
  requirement («N5′-xi stays a CANDIDATE (D1).») and occurs in 0 landed titles R90-R123; in the UPDATE it stays as scope words (once). (iii)
  THE LAST LABEL. As in R123 (C137 «G-U (ii) … no action»), END-T3's clause ends in the premises parenthesis, so R118's procedure puts
  END-T3's label after it: «… any L-RED lane lemma) (Corollary END-T3, PROVED-CONDITIONAL on REACH3-CYC, …): this gives the exact END …».
  The premises parenthesis states its own scope («RESULTS R117 (f) for EXACT-L only; RESULTS R118 (k) for END-T3 only»). (iv) EXACT-L's
  label carries the tie-break sentence and REFEREE 29's counter; the procedure moves it whole behind «… makes exactly L(G) + 3 iterations, …
  is a separate gauntlet step-4 item)». CHECKER rules on (i), (iii) and (iv).
- G-2 (ii), A SYMBOL IN A SIGNED CLAUSE (FLAG; the C135 E-4 / C135 Add. 1 E-5 class). ENDGAME-3's clause ends «iterations 1, …, F − 1 being
  S4a steps with K-config κ0 and τ0»; «τ0» occurs once in L-3 and is not defined there. The packet defines it in §2 (S): «τ0 := pe_g at
  every gate g and K2 → K2». In RESULTS «τ0» occurs 9 times, all on l. 13461, 13463, 13464, 13465, 13467, 13468 (R117's SUBDIV statement and
  its instances: «for every game G and start pair (σ0, τ0)», the start pair of a general game), a different object, so it is not landed
  notation for this clause. E0's clause («τ never changes») fixes τ to S3's τ, so the meaning is recoverable but not stated. Proposed R-T0:
  "iterations 1, …, F − 1 being S4a steps with K-config κ0 and τ0;" → "iterations 1, …, F − 1 being S4a steps with K-config κ0 and S3's τ;"
  (old string once in L-3; in the UPDATE once, with its «;» moved: the procedure takes the clause to «τ0 (Theorem ENDGAME-3, Theorem
  ENDGAME-3-N5);»). Every other symbol of the signed clauses is defined in L-3 or landed: Γ3(G), its pads pA, s, q, r, pe_g, pβ_g, pb_g,
  m_(x,k) and n (R117's line); genome, gates g, β_g, K0-K3, IDEAL-ACYC, L(G) (R104; L-3 glosses «L(G) the length of G's IDEAL run»); N5′-xi
  (R118, l. 13743-13744); Iσ, Iτ, S4a, S4c, fallback, S3 (SPEC); κ0-κ3, the K-config, F, σ* (L-3); [REACH-L] and T3 (R118 (k), and T3 quoted
  in L-3); [RULE] (R117 (f)'s proof, l. 13449).
- G-7, L41 (for the Lead's ruling; in my reading NO referee-originated proof step, so no line change). L-3 has «referee-originated» 0 times.
  Candidates checked: (i) S1 = REFEREE-2's L-R1, ««so the K-config changes only at a fallback …» → «so the K-config leaves κ0 only at a
  fallback …»», a line wording; both referees: no proof changes (REFEREE-2 «No proof changes: ENDGAME-3 uses exactly this reading.»; REFEREE
  §D «ENDGAME-3's proof (my §3) uses exactly the new reading; no proof changes.»); the κ0 reading is the packet's own (E1's Corollary, «in
  every state before the first fallback it is κ0 and Iσ ∋ (K0, K1) ≠ ∅»). (ii) EN-4, (H) restated on the value (REFEREE §6, taken in fixes
  entry 2: ««not its own H-cycle node» → «the cycle node of W*(v) is not v». Same meaning, stated on the value.»), the same fact; entry 2 is
  named in the source note. (iii) EN-1, the tie-break sentence in EXACT-L's label: a scope statement resting on REFEREE 29's counter, which
  L-3 labels «REFEREE 29's counter, … cited, not re-run»; REFEREE-2 found the same independently («EXACT-L fails on exactly the IDEAL-ACYC
  genomes with L ≥ 1: lfail 2,658 = the 2,658 such genomes»). Not a proof step. (iv) TERM-XI: both referees spell out that SPEC's Iσ is
  VJ00's improvement set on G, so R15 (c) applies (REFEREE «Iσ is VJ00's improvement set on the full game G (SPEC S1: σ̄ is Odd's optimum in
  G, not in H).»; REFEREE-2 «Ξσ does not depend on τ. So R15 (c) applies to the σ sequence and no σ repeats.»); the packet's proof already
  writes σ_new = Switch_I(σ) with I ⊆ Iσ and «By [TERM] (c), σ goes strictly up in ≺ at every iteration» (l. 172-175). (v) E0: REFEREE-2's
  «pointwise-optimal values are unique» glosses the packet's «Iτ is computed on G^d from τ alone». (vi) EXACT-L: «FL transitions, which are
  not fallbacks» is R117 (f)'s own reading (REFEREE «So «FL transitions, which are not fallbacks» in EXACT-L's proof is R117's own
  reading.»; REFEREE-2 «its FL transitions are non-fallback by R104's definition of an FL run»). If the Lead rules any of (i)-(vi) L41's
  case, the line's scope tail must name it and the other referee must sign it (DECISIONS l. 356-358).
- G-1, SOURCE NOTE (note for CHECKER; CLEAN by C134 N-S and the Lead's 10:18Z ruling in my reading). L-3's last parenthesis: «(P-N5-END,
  docs/new/P-N5-END.md, frozen at l-new 131b4c1c, sha1 5cae845b, with fixes entries 1-2, docs/new/P-N5-END-fixes.md; L-NEW successors 63-64;
  credit: ENDGAME-3 conjecture, E0-E4 skeleton and family generator L-RED 56, R221 §10-§11)». The packet's proofs are successor 63's («This
  packet carries every proof in full.»). Fixes entries, by what they carry: entry 1 (successor 64, a60733b8): W-1, the hypothesis wording of
  the «To sign» rows («Hypotheses of every row: under the standing SPEC premise 1E-N3 (RESULTS R57 (b)), as in RESULTS R104 / R117.»), and
  T-1, a tool fix — no proof text; the «Line L-1» note (successor 64): line-only; entry 2 (successor 64, 2fcee038): EN-1 (a sentence after
  EXACT-L on its tie-break dependence, with REFEREE's counter), EN-2 («No statement change; a reading of the proof the referee checked.»),
  EN-3 (wording), EN-4 ((H) restated on the value: the only change to the text of a proof fact, same meaning), and the «Line L-2» note —
  proof-bearing in the EN-4 sense and named; entry 3 (successor 65, 8b67d40e): S1-S5, line strings only («No statement and no proof changes;
  the packet stays frozen.»), not named, by the Lead's ruling quoted there («P-N5-END L-3: take S1-S5, DROP S6»; LEAD-STATE «S6 dropped
  (line-only entry need not be named)») and by C134 N-S («The note names who wrote proof-bearing text»). (ii) CHECKER's call: S1 narrows the
  line's E1 clause relative to the frozen Corollary's first sentence («The K-config changes only at a fallback»); both referees read it as
  no statement change (G-7 (i)), and the frozen Corollary's second sentence carries the κ0 reading. No R-B string is proposed.
- G-4, PREMISES (the C115 E-1 class): ALL LANDED (R-ids ≤ R123) or SPEC text; quotes by script with their RESULTS lines at 9acebb5c.
  R-labels in L-3: «R117» ×10, «R118» ×8, «R104» ×7, «R57» ×3, «R15» ×1 (and «R221» ×2, «R222», «R223», L-RED's reports). Each premise: (1)
  [DEF] R104's definitions (### R104 l. 9864), IDEAL-ACYC «Ξ-graph is ACYCLIC (self-loops count as cycles).» (l. 9910); (2) [1E-N3] «used in
  two forms: S1's σ̄, and τ̄ on the dual game, are pointwise optima; and S4a's σ_new» (R104, l. 9864; also l. 9976-9977 and R118 l.
  13741-13742), = «1E-N3 = RESULTS R57 (b) in its two forms» (R117 l. 13362), with R57's «under the standing SPEC premise 1E-N3» (l. 2893);
  (3) [TERM] R15 (c) «≺ is a strict partial order on strategies and every non-empty switch of improvements goes strictly up in ≺» (l.
  636-638); (4) [G3] R117 (b) «(b) The game Γ3(G) and its size (§3 l. 122-136) [every genome]» (l. 13425), (c) Lemma S3-START ««S3's start
  pair on Γ3(G) is the standard state of Γ3 for the genome start s_0.»» (l. 13431), (e) «(e) The transfer lemmas (§6 l. 157-240)
  [IDEAL-ACYC; K3 and TAU3 every genome]» (l. 13438); (5) [REACH3] R117 (f) «Let G ∈ IDEAL-ACYC with IDEAL run s_0 → s_1 → … → s_L, L =
  L(G). Then the N5 run of Γ3(G) FROM S3 has states 0, …, L equal to the standard states of Γ3 for s_0, …, s_L; transitions 1, …, L are FL
  transitions; transition L + 1 is a fallback.» (l. 13445-13447), EXACT-L only; (6) [R3C] R118 (k) «(k) Theorem REACH3-CYC (§7 l. 166-192,
  corrected by fixes l. 61-75) [every genome; PROVED-CONDITIONAL on [REACH-L]]» (l. 13704) with «T3 is the first state at which no mover has
  a strictly better successor in Γ3;» (l. 13705-13706), and R118's title «CONDITIONAL on P-N5-REACH's S3-START, PAD, K3, TAU3, ESC3, W3 for
  every genome» and «RESULTS R117's entry signs S3-START, PAD, K3 and TAU3 for every genome» (l. 13607), END-T3 only; (7) [N5XI] R118:
  ««with ONE change in S4a» (box 190's tie rule)» (l. 13744); (8) SPEC docs/new/N5-ssi-global.md (trunk sha1 66fde9ef) S1-S5 (l. 26-59), FIX
  1 (l. 81), FIX 3 (l. 88). L-3 also quotes two frozen packets that landed entries cite: P-N5-REACH §6.4 «In the standard state, Iτ = ∅, so
  S4b leaves τ unchanged.» (l. 202; its content is R117 (e)'s TAU3 [every genome]) and P-N5-XICYC §7 «T3 is the first state at which no
  mover has a strictly better successor in Γ3» (l. 171; the same words are R118 (k) at l. 13705-13706); and fixes entry 1's W-1 sentence
  (lane text, the hypothesis of every row). NOT landed: none; R123 (P-N5-QUIET) is named only as not used and in the scope tail. (ii) NOTE
  (CHECKER's call): L-3 lists «Lemma S3-START» for every genome; R118 records that R117's LINE states S3-START and PAD for acyclic Ξ-graphs
  only («states in its line only for acyclic Ξ-graphs (S3-START, PAD)», l. 13708-13709), while R117's entry signs (c) «[every genome]» (l.
  13431) and the packet re-derives the start from FIX 1 («S3's pair ([G3] S3-START, or FIX 1 directly)»); REFEREE-2 checked it by hand («The
  packet does not need S3-START from R117: its (S) re-derives the start from FIX 1, and I checked that by hand»). L-3's own END-T3
  parenthesis says R117 signs S3-START «for every genome», which is the entry's (c). No change proposed.
- G-9, DATA, CLAUSE BY CLAUSE (the C120-C137 rule: unit, set and scope of every count against the counter code it names; every signed clause
  matched to a count or a no-DATA entry). Every figure is in sweep195.out or check195.out (pinned) or in REFEREE's tiedep.out (cited by
  commit); the block re-run (a) diffs check195.sh's output against check195.out: PASS. By my script on sweep195.out: 24,000 xi runs and
  24,000 spec runs (16 rows × 1,500 per mode), every fail counter 0 and every tally [((1, 3), runs)] (bad rows 0); the spec rows' acyc
  column sums to 4,283; the acyc family's spec runs 3,000; 14 corpus rows in spec; RECT_d11_T59_norm maxxi 62. check195.out: 138 lines,
  every fail counter 0 outside the two «ctrl» lines; «ctrl1 rand seed 195 mode xi runs 100 e0fail 0 e1fail 0 e2fail 100 e3fail 100 e4fail
  100 stopfail 100 finsbar 100 fintie 100» and «ctrl2 rand seed 195 mode xi runs 100 e0fail 200 e1fail 200». Counter code (eg195.py at
  8b67d40e): e0fail «if list(tau) != tau0 or It: c["e0fail"] += 1» (l. 68), e1fail (l. 76), e2fail (l. 79), e3fail (l. 81), e4fail (l. 86),
  late (l. 87, «an iteration after F + 2»), capped (l. 89), nofb (l. 72), stopfail (l. 94), lfail «if F is None or F != L + 1 or it != L +
  3: c["lfail"] += 1» (l. 103-104). MATCH on every clause as worded in L-3, with three NOTES already handled by the referees: (i) eg195.py's
  docstring calls e1fail's unit «states before the first fallback» (l. 6); L-3 says «iterations before the first fallback» (REFEREE §5: «the
  count is the same (one input state per iteration)»; N-2 = S3); (ii) the clause «every run "one fallback, 3 iterations from it"» rests on
  the tally, not a fail counter (REFEREE-2 «So the clause is supported as written. Its support is the tally, not a fail counter; nothing to
  change.»); (iii) lfail is «record only»: check.sh leaves LRED unset (eg195.py l. 15), so check195.out's acyc and lfail columns are 0 and
  the EXACT-L DATA is sweep195.out's, as L-3 says. The xi rows also print lfail 0 (eg195.py l. 104 pops it only from the per-run row); L-3
  counts spec runs only. SELFL_n3: «SELFL_n3: IDEAL-ACYC False L(G) 1 N5 total 3 F 1» (data/selfl195.out). No separate DATA for TERM-XI and
  END-T3 (L-3 says so).
- G-6, NAMES (by script on RESULTS 428bc92f / GAPS 82e9d475): «TERM-XI», «ENDGAME-3», «EXACT-L», «END-T3», «κ1», «SELFL_n3» 0 times in both;
  «Lemma E1»-«Lemma E4» 0 times; «Lemma E0» once in RESULTS, as the prefix of «Lemma E0-BOUND» (l. 7535), a different lemma; «E0» 12 times
  in RESULTS and 7 in GAPS («E0-BOUND» and others), never as a label of its own; «K-config» 12 times in RESULTS (l. 4520,
  «K-configuration», another object). No clash in my reading; CHECKER's call on «E0»-«E4» as labels (they are qualified by «Lemma» in the
  line, and by the entry number at landing).
- G-P, PLACEMENT (Lead). R124 goes after R123 (### R123 l. 15076-15369, blank l. 15370), directly before the line-start «**Erratum E-1**
  (not a result» (l. 15371), and its UPDATE after R123's on GAPS l. 11 (the last UPDATE there). Simulated (sim124a.py): Addendum (7).
- G-0, THE CHECKER NUMBER. docs/checker/ on claude/checker (2101cd36) ends at C137.md (R123's); «C138» occurs 0 times in RESULTS, GAPS,
  DECISIONS-INDEX and notes/CHECKER.md and once in NOW (CHECKER 23's row: «then C138 / C139»). This draft uses C138 (title, UPDATE head,
  GAPS preamble), as the brief says.
- G-5, ERRATA (note). E-1 (R97-R100 counts), E-2 (R105's CHAIN-BACK, RANK_t, KEYFLIP) and Note E-3 (R110's SC-ISO) do not bear on R15 (c),
  R57, R104's definitions, R117 (b), (c), (e), (f) or R118 (k).
- G-8, SCOPE AND TARGET (note). L-3's scope tail («this gives the exact END of two runs on one family of games and, for IDEAL-ACYC genomes,
  an identity between N5's count and L(G); it bounds none of F, T3, L(G) (OPEN), and nothing outside Γ3(G)») equals packet Scope l. 13-18
  and §9 l. 225-228 in meaning; EXACT-L's Consequence is stated as an iteration-count statement (EN-3; «it is a statement about iteration
  counts (EN-3)»). TARGET.md §4 «Polynomial only on a restricted class». No statement bounds a running time.
- G-10, LEAD RULINGS AND READINGS. L-3 cites no Lead reading («Lead reading» 0, «L4» 0 in L-3). The Lead's rulings in the packet's history:
  04:00Z freeze words (packet l. 2-3), 05:56Z (W-1, T-1 routed), 06:33Z (REFEREE 29's LN-1..LN-8 «follow them exactly», EN-1 «take it with
  W-1»), 09:52Z (round routed) and 10:18Z («take S1-S5, DROP S6»), each quoted in the fixes file; none is a premise.
- G-11, STALE WORDS (C118 E-1 / C132 E-1): CLEAN. L-3: «pending», «not landed», «to land», «will », «NOT YET», «first fill» 0 each.
  «G-N5-TIME stays OPEN», «(OPEN)» and «stays a CANDIDATE» are dated by the line's «(2026-11-08)», the packet's freeze date (131b4c1c,
  04:10:38Z). «P-N5-QUIET's QUIET / T-QUIET» (scope tail) and «any P-N5-QUIET or box 194 lemma» (not used) name a packet landed since as
  RESULTS R123; the sentence stays true (R123 bounds T_CYC on Γ(G) and proves nothing on Γ3); optional, CHECKER's call, no string proposed.
- G-12, PINS (the C116 G-3 class): CLEAN. end.pins (43 rows) pins the packet, the fixes file, L-1, L-2, L-3, mkl1_195.py, mkl2_195.py,
  mkl3_195.py, eg195.py, check195.sh, check195.out, the data outputs and the instances; block «P-N5-END» re-ran it (PASS, (a)).
- G-14, THE FIXES FILE (note). Entry 1 (successor 64, a60733b8; l. 3-26): W-1, T-1; «Line L-1» note (l. 28-34); entry 2 (successor 64,
  2fcee038; l. 36-73): EN-1..EN-4 and «Line L-2» = L-1 + R1-R16 (mkl2_195.py); entry 3 (successor 65, 8b67d40e; l. 75-92): S1-S5 and «Line
  L-3» = L-2 + S1-S5 (mkl3_195.py). Each entry says the packet is unchanged and later entries govern.
- G-N, NOVELTY (note). No outside source is cited beyond R15's VJ00 §4.4 (landed); the entry makes no literature claim. Credit to L-RED 56
  (ENDGAME-3 conjecture, E0-E4 skeleton, family generator) is in L-3's source note.
- CLEAN AT L-3 (by script on d6afe92a): C113 E-1 / C123 E-1 / C133 E-1 (L-3 starts «On Γ3(G) of RESULTS R117 (», «R1xx» 0); C122 G-0 (105 /
  105, depth never negative, final 0); C114 Add. 1 E-1 (<DATE>); C116 G-2 (G-6); C116 G-3 (G-12); C117 E-1 / C135 E-3 (G-2: no READING in a
  signed clause; the one «READING» of the packet, §6 l. 196, is not in L-3); C118 E-1 (G-11); the DATA clauses (G-9, notes only); «|»: 0 in
  L-3, in the entry block and in the UPDATE (Addendum). NOT CLEAN: C133 E-3 / C134 E-3 (G-U); C135 E-4 (G-2 (ii)); for the Lead: L41 (G-7);
  for CHECKER: G-1 (ii), G-4 (ii), G-6, G-11's optional note.
- (L-3 SHAPE, by script) one line: 7,215 bytes and 7,091 characters with its newline, 105 «(» / 105 «)», 0 "|", one « — », «(2026-11-08)»
  once, «R1xx» 0, «DATA, clause by clause» once, 9 guillemet quotes, «REFEREE» 3, «referee-originated» 0, «PROVED-CONDITIONAL» 2.
(0) PLACEMENT. RESULTS at origin trunk 9acebb5c (= local HEAD a773c562's): sha1 428bc92f5ddd4167bb8b2bac88eb04cc9de97c19, 16,013 lines; "###
  R124" 0 times in RESULTS and GAPS. PROPOSED (R102's to R123's layout): insert R124's entry, with one blank line after it, directly before
  the line-start «**Erratum E-1** (not a result», after the blank line that follows R123's block (G-P). Simulation: Addendum (7).
(1) TITLE. The title is the line file docs/new/P-N5-END-line-L3.txt (l-new 8b67d40e, 2026-11-08T10:18:46Z, the file's only commit, sha1
  d6afe92ae0d2c0021743c99d2bd10f16cad27c73, 7,215 bytes with the newline; byte-equal at the l-new head 14babccb and at origin trunk
  9acebb5c), verbatim: NOTHING is stripped and NOTHING is inserted: "### R124 [refereed-only] ", then the file without its newline, then ",
  CHECKER PASS (docs/checker/C138.md, checker PENDING)" (as R90-R123; R123's title is "### R123 [refereed-only] " + its L-4 + ", CHECKER
  PASS (docs/checker/C137.md, checker 3479ecb0)" after landing). Built by script and re-checked after writing (chk124a.py): equal.
(2) LINE HISTORY: three lines. L-1 68a69176 (a60733b8; 5,903 bytes; by mkl1_195.py, W-1 applied; written before REFEREE 29's report reached
  the lane, «line L-1 (sha1 68a69176…, 5,903 B) was written and pushed (l-new a60733b8) before REFEREE 29's report reached this lane»;
  SUPERSEDED, reviewed by neither referee as a line). L-2 e8a8ac51 (2fcee038; 6,988 bytes, 101 «(» / 101 «)»): L-1 + R1-R16 (LN-1..LN-8,
  EN-3) by mkl2_195.py; REFEREE §C «L-2 MATCHES the packet with its fixes entries, and meets LN-1..LN-8.»; REFEREE-2 «NOT YET». L-3 d6afe92a
  (8b67d40e; 7,215 bytes, 105 / 105): L-2 + S1-S5 (L-R1, N-1, N-2, EL-1, EL-2) by mkl3_195.py; both referees MATCH after their own byte
  tests ((3)).
(3) THE LINE AT BOTH REFEREES. REFEREE: report e4cb208a (successor 29; no line existed; LN-1..LN-8), §C 407f4a21 (successor 29; L-2 MATCHES,
  l. 219), §D 4434597c (successor 30; «Verdict: fixes entry 3 CORRECT. **Line L-3 MATCHES** the packet read with fixes entries 1-3 and still
  meets LN-1..LN-8», l. 244, introduced by 4434597c, git blame). REFEREE-2: report 9b3cc9b6 (successor 34; L-2 NOT YET, L-R1), Add. 1
  0f82f03b (comparison; L-R1 kept REQUIRED), Add. 2 0e5c7c37 (successor 35; «Verdict: **L-3 MATCHES.**», l. 262, introduced by 0e5c7c37, git
  blame).
(4) CLAIMS SIGNED = the statement rows of both verdict tables (REFEREE l. 8-14; REFEREE-2 l. 23-32): E0, E1, E2, E3, E4 (a), (b), TERM-XI,
  ENDGAME-3, ENDGAME-3-N5, EXACT-L SIGN at both from the first round; END-T3 SIGN as PROVED-CONDITIONAL on REACH3-CYC (R118 (k), itself
  PROVED-CONDITIONAL on [REACH-L]) at both. Not signed: §7-§9 (DATA, machine checks, TARGET diff), END-T3's READING (packet l. 196).
(5) OTHER TEXTS THE ENTRY DEPENDS ON: RESULTS R15 (c); R57 (1E-N3, as landed in R104 and R117); R104 (definitions); R117 (b), (c), (e), (f);
  R118 (k) and its title's condition sentence; SPEC S1-S5, FIX 1, FIX 3; the frozen P-N5-REACH §6.4 and P-N5-XICYC §7 as quoted; the box 195
  tools and outputs (L-NEW 63-65); REFEREE's tiedep.out (e4cb208a), cited.
(6) PREMISE LABELS: G-4. (7) SYMBOL TEST: G-2 (ii). (8) FIXES AND STATUS NOTES: G-14; body Fixes.
(9) GAPS: G-N5-TIME (GAPS l. 11) stays open; L-3 states no CONJECTURE and kills no statement («P-N5-END», «ENDGAME-3» 0 times in GAPS). A
  line-11 UPDATE is proposed at the end, BUILT FROM L-3 AS IT STANDS with the G-U reading (upd124a.py).
(10) DATA of record = packet §7 with fixes entries 2-3 (the unit and set wording of R10-R14, N-2), NOT signed; L-3's DATA states its counts
  (G-9). Re-run (a): PASS.
(11) Discrepancies, recorded for CHECKER, no verdict affected: D-1 the Lead's notes give «L-3 d6afe92a (8b67d40e)»: d6afe92a is the file
  sha1 and 8b67d40e the commit (git), as in LEAD-STATE «L-3 d6afe92a MATCHES both». D-2 REFEREE §2.1 cites R117 (f) at «RESULTS l.
  13445-13447» and R118 (k) at «l. 13704-13712»: the same numbers at 9acebb5c (R119-R123 landed after them). D-3 REFEREE §D cites RESULTS
  R118's DATA at «trunk l. 13830»: at 9acebb5c that line is inside R118 (l. 13607-13878). D-4 the packet's §1 cites trunk 51eb65348 and
  fixes entry 1 re-ran the quotes at c8f42538f; both are ancestors of 9acebb5c, and my premise quotes (G-4) are at 9acebb5c. D-5 L-3's set
  wording «every pinned genome of box189 and box191-box194» is check195.sh's box194/inst, box193/inst, box192/inst, box191/inst,
  box189/inst, box189/corpus (l. 9-10).
(12) Excluded: the packet's READING after END-T3 (l. 196), quotes_end.py / quotes195.py (record tools: §1's quotes; my G-4 quotes are my
  own), REFEREE-2's n5w and gate-order DATA (referee data), L-RED R222 / R223 (cited by the line, not read beyond the fixes file). Not part
  of this entry.
(13) Commits: lane (claude/l-new): 131b4c1c (2026-11-08T04:10:38Z; packet FROZEN, end.pins, the «P-N5-END» block; L-NEW successor 63),
  a60733b8 (06:27:26Z; fixes entry 1, L-1, mkl1_195.py; successor 64), 2fcee038 (06:58:09Z; fixes entry 2, L-2, mkl2_195.py; successor 64),
  8b67d40e (10:18:46Z; fixes entry 3, L-3, mkl3_195.py; successor 65). REFEREE: e4cb208a → 407f4a21 → 4434597c. REFEREE-2: 9b3cc9b6 →
  0f82f03b → 0e5c7c37. CHECKER: docs/checker/ ends at C137.
(14) DEAD-ENDS ROWS: NONE (no statement killed; EXACT-L's tie-break dependence (EN-1) and SELFL_n3 are scope facts stated in the line, not
  dead ends of a claim).

### R124 [refereed-only] On Γ3(G) of RESULTS R117 (Γ(G) of R104 with 4M + 4 single-successor Even pads of priority ≤ 2, n = N + 7M + 10), for N5 (SPEC S1-S5 with FIX 1-4) and N5′-xi (RESULTS R118's [N5XI], SPEC with box 190's S4a tie rule) from SPEC's default start S3, iterations counted as in SPEC S4, for every genome G, each PROVED (every genome): (Lemma E0) τ never changes and Iτ = ∅ at every state; (Lemma E1) at every state with the core K-config κ0 = (σ(K0), σ(K1), σ(K3)) = (pA, s, K2) the only improving core edge is (K0, K1) and every S4a step keeps κ0, so the K-config leaves κ0 only at a fallback and the run cannot stop before one; (Lemma E2) the first fallback, at iteration F ≥ 1, is an Even fallback with result K-config κ1 = (K1, s, K2); (Lemma E3) from κ1 the next iteration is an S4a step to κ2 = (K1, q, K2); (Lemma E4) from κ2 the next iteration is an S4a step to σ* with K-config κ3 = (K1, q, K1) and σ*(β_g) = pb_g at every gate g, and Iσ* = ∅ whatever σ* is at the movers; (Lemma TERM-XI) both runs terminate; (Theorem ENDGAME-3, Theorem ENDGAME-3-N5) N5′-xi, and N5, from S3 on Γ3(G) have exactly one fallback, at an iteration F ≥ 1, and exactly F + 2 iterations, iterations 1, …, F − 1 being S4a steps with K-config κ0 and S3's τ; (Corollary EXACT-L, PROVED for G ∈ IDEAL-ACYC (R104: the Ξ-graph is acyclic; self-loops count as cycles; «Ξ-graph is ACYCLIC (self-loops count as cycles)»), premise RESULTS R117 (f); it uses SPEC's S1 tie-breaks, through REACH3's [RULE] choice: with another pointwise-optimal S4a choice the identity can fail, F = 1 on 382 of 382 IDEAL-ACYC genomes with L ≥ 1, REFEREE 29's counter, R-P-N5-END §4 (C), claude/referee e4cb208a, docs/referee/scratch/end_logs/tiedep.out, cited, not re-run) N5 (SPEC S1-S5 with its FIX 1-4 tie-breaks) from S3 on Γ3(G) makes exactly L(G) + 3 iterations, L(G) the length of G's IDEAL run, so on {Γ3(G) : G ∈ IDEAL-ACYC} N5's iteration count is polynomial in n iff L(G) is polynomial in N + M (a statement about iteration counts; the cost per iteration at bit cost is a separate gauntlet step-4 item); (Corollary END-T3, PROVED-CONDITIONAL on REACH3-CYC, RESULTS R118 (k), itself PROVED-CONDITIONAL on [REACH-L]: «CONDITIONAL on P-N5-REACH's S3-START, PAD, K3, TAU3, ESC3, W3 for every genome», and of these RESULTS R117 signs S3-START, PAD, K3 and TAU3 for every genome but ESC3 and W3 for acyclic Ξ-graphs only) if REACH3-CYC holds for G, N5′-xi from S3 on Γ3(G) makes exactly T3 + 3 iterations, with T3 as in R118 (k) (P-N5-XICYC §7: «T3 is the first state at which no mover has a strictly better successor in Γ3»), T3 + 1 being the first fallback (premises, all under the standing SPEC premise 1E-N3 of RESULTS R57 / R104 / R117 (fixes entry 1, W-1: «Hypotheses of every row: under the standing SPEC premise 1E-N3 (RESULTS R57 (b)), as in RESULTS R104 / R117.»): RESULTS R104's definitions of the genome, of Γ(G), of IDEAL-ACYC and of the start pair only; RESULTS R117's definition of Γ3 and pad priorities (P-N5-REACH §3), Lemma S3-START and, for E0, [TAU3] (RESULTS R117 / P-N5-REACH §6.4: «In the standard state, Iτ = ∅, so S4b leaves τ unchanged.», signed for every genome per R118: «RESULTS R117's entry signs S3-START, PAD, K3 and TAU3 for every genome»); [1E-N3] = RESULTS R57 (b) as landed in R104 («used in two forms: S1's σ̄, and τ̄ on the dual game, are pointwise optima; and S4a's σ_new»…, a pointwise optimum of the S4a arena before S4c), used for σ̄ and for S4a's σ_new inside SPEC runs (REFEREE 29 rules [OPT] = [1E-N3] for SPEC runs; R118 (b)'s [OPT] is not used); RESULTS R15 (c) («every non-empty switch of improvements goes strictly up in ≺») for TERM-XI; RESULTS R117 (f) for EXACT-L only; RESULTS R118 (k) for END-T3 only; the SPEC text docs/new/N5-ssi-global.md S1-S5 with FIX 1 and FIX 3; not used: ESC3, W3, KEY3, SBAR3, PLAY3, PAD (b)-(c), R118 (b)'s [OPT], any P-N5-QUIET or box 194 lemma, any L-RED lane lemma) (2026-11-08) — this gives the exact END of two runs on one family of games and, for IDEAL-ACYC genomes, an identity between N5's count and L(G); it bounds none of F, T3, L(G) (OPEN), and nothing outside Γ3(G); EXACT-L is false without IDEAL-ACYC's self-loop clause: L-RED 57's SELFL_n3 (N 3, two Ξ self-loops; experiments/new/box195/inst/SELFL_n3.json, sha1 27bc7f72…) has L(G) = 1 (IDEAL run read with B_s the set of β-ids on its eventually periodic X-chain; R104's IDEAL run is defined on IDEAL-ACYC) and N5 makes 3 iterations (F = 1); END-T3 gives no bound on T3: P-N5-QUIET's QUIET / T-QUIET bound IDEAL-CYC's T_CYC on Γ(G), and their transfer to the Γ3 run is NOT proved (the Γ3 run can differ from the IDEAL-CYC run at exact VJ ties, R118's DATA); DATA, clause by clause (unit: runs of N5′-xi (EG195_MODE xi) or N5 (spec) from S3 on Γ3(G) built by box189/gamma3.py, stepped by box190/n5v.py; tool experiments/new/box195/eg195.py, run by check195.sh; set: 8 families (rand d 1-5; L-RED R221 §11's esc, noesc, deep, dense, lvl0, transcribed; late, a stand-in with start = each mover's last option; acyc) × 1,500 × seeds 1951, 1952, 24,000 runs per mode, 48,000 in all (data/sweep195.out), plus the 14 R117 corpus genomes in spec mode (sweep195.out); and check195.out (re-run by check.sh): 8 families × 300, seed 1953, per mode, plus every pinned genome of box189 and box191-box194; all pinned in box195/end.pins): E0: e0fail 0 (unit: states); E1: e1fail 0 (unit: iterations before the first fallback); E2, E3, E4 (a): e2fail, e3fail, e4fail 0 (unit: the iterations F, F + 1, F + 2); E4 (b): stopfail 0, finsbar 0, fintie 0 (unit: final states); ENDGAME-3, ENDGAME-3-N5: nofb 0 and capped 0 (unit: runs), late 0 (unit: iterations after F + 2), every run «one fallback, 3 iterations from it»; EXACT-L: lfail 0 (unit: IDEAL-ACYC genomes with F ≠ L(G) + 1 or total ≠ L(G) + 3) on 4,297 genomes, spec runs only (4,283 random IDEAL-ACYC ones in the spec rows of sweep195.out, 3,000 of them from acyc, and the 14 corpus genomes; L(G) up to 59, RECT_d11_T59_norm, 62 iterations; L(G) by L-RED's ideal.traj at claude/l-red 86a7a7a8, record only (not re-run by check.sh, which leaves LRED unset)); controls fire (check195.out: ctrl1 e2fail, e3fail, e4fail, stopfail, finsbar, fintie 100 each in 100 runs; ctrl2 e0fail 200 (unit: states) and e1fail 200 (unit: iterations before the first fallback), nofb 100 (unit: runs)); independent replays, every fail counter 0, their counters in their own pinned outputs, cited, not re-run: L-RED 57 R222 item 3 (claude/l-red 6f56004c), L-RED 58 R223 item 1 (claude/l-red 143f0b4c), REFEREE 29 R-P-N5-END §4 (A), (B) (claude/referee e4cb208a); no separate DATA for TERM-XI and END-T3; N5′-xi stays a CANDIDATE (D1); TARGET.md §2 (M4) asks for an algorithm polynomial on every parity game and §4 says a bound on a restricted class is not M4, so this is not M4; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim (P-N5-END, docs/new/P-N5-END.md, frozen at l-new 131b4c1c, sha1 5cae845b, with fixes entries 1-2, docs/new/P-N5-END-fixes.md; L-NEW successors 63-64; credit: ENDGAME-3 conjecture, E0-E4 skeleton and family generator L-RED 56, R221 §10-§11), CHECKER PASS (docs/checker/C138.md, checker PENDING)
- Object (L-NEW successors 63-65 and 68, D1 / D14 / D18, box 195; frozen, unchanged during review): packet P-N5-END, docs/new/P-N5-END.md,
  sha1 5cae845b1da1a1c40b52e73da6edae3d6aadbf29, 228 lines, 22,967 bytes (l-new 131b4c1c, 2026-11-08T04:10:38Z, the file's only commit;
  identical at a60733b8, 2fcee038, 8b67d40e, b7faeebe and the l-new head 25e040ee; pinned in experiments/new/box195/end.pins). Both referees
  measured it (REFEREE «docs/new/P-N5-END.md sha1 5cae845b1da1a1c40b52e73da6edae3d6aadbf29, 22,967 B»; REFEREE-2 «Packet
  docs/new/P-N5-END.md at 131b4c1c: sha1 5cae845b1da1a1c40b52e73da6edae3d6aadbf29, 22,967 B, 228 lines (= the brief)»). Freeze: «FREEZE
  packet P-N5-END: E0-E4, TERM-XI, ENDGAME-3, ENDGAME-3-N5, EXACT-L (IDEAL-ACYC), and END-T3 marked conditional on REACH3-CYC» (l. 2-3).
  Labels (l. 7): «PROVED (L-NEW 63, unrefereed) / PROVED-CONDITIONAL / READING (not to sign) / DATA». To sign (l. 20-29): §3 Lemma E0; §4
  Lemma E1; §5 Lemmas E2, E3, E4; §6 Lemma TERM-XI, Theorems ENDGAME-3 and ENDGAME-3-N5 (every genome), Corollary EXACT-L (G ∈ IDEAL-ACYC,
  self-loops count as cycles; premise R117 (f)) and Corollary END-T3 (PROVED-CONDITIONAL on REACH3-CYC, RESULTS R118 (k), CONDITIONAL
  there); §7-§9 DATA / READING. The packet's own scope (l. 8): «This packet is NOT a TARGET.md claim, NOT M3 and NOT M4. It does not decide
  G-N5-TIME.». Credit (l. 5-6): L-RED 57 R222 item 3 attacked it («all SURVIVE»); «Credit: the conjecture ENDGAME-3, the skeleton E0-E4 and
  the family generator are L-RED 56's (R221 §10-§11).».
- Fixes: docs/new/P-N5-END-fixes.md, append-only (b7faeebe: 114 lines, 12,917 bytes, sha1 0a0cf11505a1b811ee3383fab3d1228328b6e097; its
  first 10,024 bytes are the file at 8b67d40e, its first 7,670 bytes the file at 2fcee038 and its first 3,570 bytes the file at a60733b8, by
  prefix test). Entry 1 (a60733b8, L-NEW successor 64, l. 3-26): W-1 (the standing SPEC premise 1E-N3 on every «To sign» row: «Hypotheses of
  every row: under the standing SPEC premise 1E-N3 (RESULTS R57 (b)), as in RESULTS R104 / R117.») and T-1 (quotes_end.py reads every source
  from trunk; «quotes 33 missing 0 (every source from trunk c8f42538f)»); «The packet is unchanged; where this entry and the packet differ,
  this entry governs.». The «Line L-1» note (l. 28-34). Entry 2 (2fcee038, successor 64, l. 36-73; Lead 06:33Z): EN-1 (EXACT-L's tie-break
  dependence, l. 43-46), EN-2 (ENDGAME-3-N5 for every pointwise-optimal S4a rule, l. 47-48), EN-3 («… would bound N5's iteration count on
  them», l. 49-50), EN-4 ((H) on the value, l. 51); «Line L-2» = L-1 + R1-R16 (l. 53-73). Entry 3 (8b67d40e, successor 65, l. 75-92;
  line-only): S1 L-R1 (REQUIRED, REFEREE-2 34), S2 N-1, S3 N-2 (REFEREE-2 34), S4 EL-1, S5 EL-2 (REFEREE 29); «P-N5-END L-3: take S1-S5,
  DROP S6»; «Line L-3» = L-2 + S1-S5 by mkl3_195.py («sha1 d6afe92ae0d2c0021743c99d2bd10f16cad27c73, 7,215 B, 105 «(» = 105 «)»»). Entry 4
  (b7faeebe, successor 68, l. 94-114; «LINE-ONLY»): R-U (C138 E-1) and R-T0 (C138 E-2), C138 §4's strings (l. 107-108); «No statement,
  label, hypothesis, premise, proof or DATA number changes; the packet stays frozen»; «Line L-4» = L-3 + R-U, then R-T0, by mkl4_195.py
  («Result: sha1 5f88c2971718522027ae267754814c6ba401b829, 7,230 B, 105 «(» = 105 «)»», l. 111-112).
- The RESULTS line is L-4, 5f88c2971718522027ae267754814c6ba401b829 (docs/new/P-N5-END-line-L4.txt, l-new b7faeebe, 2026-11-09T04:48:50Z,
  the file's only commit; 7,230 bytes). The title is L-4 verbatim, with nothing inserted and nothing stripped (its date parenthesis
  «(2026-11-08)», its scope tail and its source note are the line's own). L-4's parentheses balance (105 «(» / 105 «)»). Line history: L-1
  (68a69176, a60733b8, W-1 applied, superseded before review), L-2 (e8a8ac51, 2fcee038, L-1 + R1-R16 for REFEREE 29's LN-1..LN-8 and EN-3),
  L-3 (d6afe92a, 8b67d40e, L-2 + S1-S5, each old string once in L-2, by mkl3_195.py, which asserts the packet's, L-2's and the result's
  sha1), L-4 (5f88c297, b7faeebe, L-3 + R-U, then R-T0, CHECKER C138's strings for its E-1 and E-2, each old string once in L-3, by
  mkl4_195.py, which asserts the packet's and L-3's sha1, no «τ0», and CHECKER's expected sha1 and size). REFEREE: L-2 MATCHES (§C,
  407f4a21: «Fixes entries 1-2 CORRECT. L-2 MATCHES the packet with its fixes entries, and meets LN-1..LN-8.», l. 218-220); L-3 MATCHES (§D,
  4434597c, l. 225-228: «`cmp` with the lane's L-3: **EQUAL** (scratch/end_logs/l3test.out)»; l. 244-245: «**Line L-3 MATCHES** the packet
  read with fixes entries 1-3 and still meets LN-1..LN-8 (S1-S5 touch no label, scope, premise or TARGET clause). All statements stay as in
  §0: SIGN; END-T3 PROVED-CONDITIONAL on REACH3-CYC.»); L-4 MATCHES (§E, 37195499, l. 252-253: «`cmp` with the lane's L-4: **EQUAL**
  (scratch/end_logs/l4test.out)»; l. 267-268: «Verdict: fixes entry 4 CORRECT. **Line L-4 MATCHES** (L-3 + exactly R-U and R-T0). Statements
  as signed (§0; END-T3 PROVED-CONDITIONAL on REACH3-CYC).»). REFEREE-2: L-2 NOT YET (9b3cc9b6, l. 33, «one REQUIRED change (L-R1: E1's
  «changes only at a fallback» is false as written once E3 / E4 run)») for L-R1; L-3 MATCHES (Add. 2, 0e5c7c37, l. 247-252: «**L-3 == L-2 +
  S1-S5: True.** Nothing else changed.»; l. 262-263: «Verdict: **L-3 MATCHES.** All P-N5-END statement verdicts are unchanged: every row
  SIGN, END-T3 PROVED-CONDITIONAL on REACH3-CYC (R118 (k), itself PROVED-CONDITIONAL on [REACH-L]). From my side P-N5-END may land with
  L-3.»); L-4 MATCHES (Add. 3, 63a3cf87, l. 270: «**L-4 == L-3 + R-U + R-T0: True.** Nothing else changed.»; l. 278: «(4) Verdict: **L-4
  MATCHES** (byte test, and in meaning). Statement verdicts unchanged.»).
- Claims signed (REFEREE successor 29: report e4cb208a, §C 407f4a21; successor 30: §D 4434597c, §E 37195499; REFEREE-2 successor 34: report
  9b3cc9b6, Addendum 1 0f82f03b; successor 35: Addendum 2 0e5c7c37, Addendum 3 63a3cf87). REFEREE's table («## 0. Verdicts», l. 5-15 of
  R-P-N5-END.md) reads E0, E1 with its Corollary, E2, E3, E4 (a), (b), TERM-XI, ENDGAME-3 / ENDGAME-3-N5 «SIGN», EXACT-L «SIGN (scope note
  EN-1: SPEC's tie-breaks)» and END-T3 «SIGN as PROVED-CONDITIONAL on REACH3-CYC (R118 (k), itself PROVED-CONDITIONAL on [REACH-L])», with
  «No GAP. No required change to the frozen packet's mathematics.» (l. 16). REFEREE-2's table («## Verdicts (Opus 5.5, D1)», l. 20-33 of
  R2-P-N5-END.md) reads «SIGN» on E0 (note «under 1E-N3 (W-1, fixes entry 1), as every row»), E1 (note «its Corollary holds before the first
  fallback only (L-R1)»), E2, E3, E4 (a), (b), TERM-XI, ENDGAME-3, ENDGAME-3-N5 (note «holds for every pointwise-optimal S4a rule (EN-2): my
  n5w data») and EXACT-L (note «G ∈ IDEAL-ACYC; premise R117 (f); holds under SPEC's S1 tie-breaks (EN-1), FALSE for another
  pointwise-optimal S4a rule (my n5w data)»), and END-T3 «SIGN as PROVED-CONDITIONAL», with «No statement is REFUSED. No statement has a
  mathematical gap. The one required change is to the line's wording of E1's consequence.» (l. 35). Both re-signed after the line rounds:
  REFEREE «All statements stay as in §0: SIGN; END-T3 as PROVED-CONDITIONAL on REACH3-CYC.» (l. 220) and l. 244-245 (above); REFEREE-2 Add.
  1 «Net for routing: both referees SIGN every statement.» (l. 240) and Add. 2 l. 262-263 (above); at L-4, REFEREE §E l. 267-268 and
  REFEREE-2 Add. 3 l. 278 (above). The CONDITIONAL statement is END-T3: PROVED-CONDITIONAL on REACH3-CYC, RESULTS R118 (k), itself
  PROVED-CONDITIONAL on [REACH-L]; the line states the condition as both referees signed it (below, (i)). The joint gap map: EMPTY. REFEREE
  «No GAP.» (l. 16); REFEREE-2 «No statement has a mathematical gap.» (l. 35). The one REQUIRED item at either referee, L-R1, is line
  wording (closed by S1, both MATCH); the optional items EN-1..EN-4 (fixes entry 2), N-1, N-2, EL-1, EL-2 (entry 3) were taken; CHECKER
  C138's E-1 and E-2 (line-only) are taken in L-4 (R-U, R-T0, entry 4), and both referees MATCH it. Nothing is REFUSED.
- Setting: Γ3(G) of RESULTS R117 (b) for every genome G of R104; N5 = SPEC S1-S5 with FIX 1-4, N5′-xi = R118's [N5XI] (SPEC with box 190's
  S4a tie rule), both from SPEC's default start S3; iterations as in SPEC S4; σ̄ and S4a's σ_new pointwise optima by [1E-N3] (R57 (b) as
  landed in R104), which both referees rule is the premise here, not R118 (b)'s [OPT] (REFEREE §2.2 «[1E-N3] is the right premise here
  (§2.2).»; REFEREE-2 «[OPT] = [1E-N3] for SPEC runs: right.»). Statements as signed (packet with fixes entries 1-4; entries 3 and 4 are
  line-only):
  (a) Lemma E0 (§3 l. 99-103) [every genome, under 1E-N3]: «Every state of the run has τ = τ0, and Iτ = ∅ there.». REFEREE SIGN (l. 8),
    REFEREE-2 SIGN (l. 23).
  (b) Lemma E1 (§4 l. 105-118) [every genome, under 1E-N3]: «In every state with K-config κ0 and τ0: (a) Iσ ∩ (edges out of K0, K1, K3) =
    {(K0, K1)}; (b) every S4a σ_new (N5 or N5′-xi) has K-config κ0.»; with its Corollary read as REFEREE-2's L-R1 (the line: «the K-config
    leaves κ0 only at a fallback and the run cannot stop before one»). REFEREE SIGN (l. 9), REFEREE-2 SIGN (l. 24).
  (c) Lemma E2 (§5 l. 121-124): «If iteration F is the first fallback, its input state has κ0 and τ0, it is an Even fallback, and its result
    has K-config κ1 and τ0.». REFEREE SIGN (l. 10), REFEREE-2 SIGN (l. 25).
  (d) Lemma E3 (§5 l. 126-137): «From every state with K-config κ1 and τ0 (any σ at movers and β's), the next iteration is an S4a iteration
    (not a fallback) whose result has K-config κ2.». REFEREE SIGN (l. 10), REFEREE-2 SIGN (l. 26).
  (e) Lemma E4 (§5 l. 139-168): from every state with K-config κ2 and τ0, «(a) the next iteration is an S4a iteration whose result σ* has
    K-config κ3 and σ*(β_g) = pb_g at every β_g;» and «(b) at σ*, Iσ* = ∅ (whatever σ* is at the movers), so with E0 the run stops (S5).».
    REFEREE SIGN (l. 10), REFEREE-2 SIGN (l. 27).
  (f) Lemma TERM-XI (§6 l. 171-175): «The N5′-xi run and the N5 run from S3 on Γ3(G) terminate.». REFEREE SIGN (l. 11), REFEREE-2 SIGN (l.
    28).
  (g) Theorem ENDGAME-3 (§6 l. 177-181) [every genome]: «For every genome G, N5′-xi from S3 on Γ3(G) has exactly one fallback, at an
    iteration F ≥ 1, and makes exactly F + 2 iterations; iterations 1, …, F − 1 are S4a iterations with K-config κ0 and τ0.»; Theorem
    ENDGAME-3-N5 (l. 182): «The same for N5 (SPEC S4a).». REFEREE SIGN (l. 12), REFEREE-2 SIGN (l. 29-30). The line says «S3's τ» for the
    packet's τ0 (R-T0, C138 E-2; packet §2 (S): «τ0 := pe_g at every gate g and K2 → K2», l. 90-91), as both referees read it (REFEREE §E l.
    256-260; REFEREE-2 Add. 3 l. 272-274).
  (h) Corollary EXACT-L (§6 l. 184-192, with EN-1 of fixes entry 2) [G ∈ IDEAL-ACYC; premise R117 (f)]: «For every genome G ∈ IDEAL-ACYC
    (R104: its Ξ-graph is acyclic, self-loops count as cycles), N5 from S3 on Γ3(G) makes exactly L(G) + 3 iterations.»; «EXACT-L uses
    SPEC's S1 tie-breaks (through REACH3's [RULE] choice); with another pointwise-optimal S4a choice the identity can fail». REFEREE SIGN
    (l. 13), REFEREE-2 SIGN (l. 31).
  (i) Corollary END-T3 (§6 l. 194-195) [PROVED-CONDITIONAL on REACH3-CYC, R118 (k), itself PROVED-CONDITIONAL on [REACH-L]]: «For every
    genome, if [R3C] holds then N5′-xi from S3 on Γ3(G) makes exactly T3 + 3 iterations.». REFEREE SIGN as PROVED-CONDITIONAL (l. 14,
    «CORRECT as a conditional.», l. 84), REFEREE-2 SIGN as PROVED-CONDITIONAL (l. 32). The line states the condition in END-T3's label,
    «(Corollary END-T3, PROVED-CONDITIONAL on REACH3-CYC, RESULTS R118 (k), itself PROVED-CONDITIONAL on [REACH-L]:» … «if REACH3-CYC holds
    for G, N5′-xi from S3 on Γ3(G) makes exactly T3 + 3 iterations», as REFEREE's LN-1 asked («END-T3 PROVED-CONDITIONAL on REACH3-CYC
    (RESULTS R118 (k), itself PROVED-CONDITIONAL on [REACH-L])», l. 140-141) and as REFEREE §C found it («The sentence on which R117 rows
    are signed for every genome and which for acyclic Ξ-graphs only is R118 (k)'s own text», l. 193-194).
- The RESULTS line (L-4, the title): «On Γ3(G) of RESULTS R117 (Γ(G) of R104 with 4M + 4 single-successor Even pads of priority ≤ 2, n = N +
  7M + 10),» … «for every genome G, each PROVED (every genome):» … «(premises, all under the standing SPEC premise 1E-N3 of RESULTS R57 /
  R104 / R117» … «(2026-11-08) — this gives the exact END of two runs on one family of games» … «DATA, clause by clause» … «(P-N5-END,
  docs/new/P-N5-END.md, frozen at l-new 131b4c1c, sha1 5cae845b, with fixes entries 1-2». Its clauses: the setting (Γ3, N5, N5′-xi, S3, SPEC
  S4); E0 = (a); E1 = (b) in L-R1's form; E2 = (c); E3 = (d); E4 = (e); TERM-XI = (f); ENDGAME-3 and ENDGAME-3-N5 = (g), its S4a iterations
  «with K-config κ0 and S3's τ» (R-T0); EXACT-L = (h) with EN-1 and REFEREE 29's counter in its label, and the Consequence as an
  iteration-count statement (EN-3); END-T3 = (i) with its condition in its label and T3 quoted; the premises parenthesis (1E-N3 on every
  row, W-1; R104, R117, [TAU3], [1E-N3], R15 (c), R117 (f), R118 (k), SPEC; what is not used); the scope tail (the exact END; no bound on F,
  T3, L(G); SELFL_n3 for the self-loop clause; no transfer of P-N5-QUIET to Γ3); DATA clause by clause, inline (each count against eg195.py,
  sweep195.out and check195.out); the TARGET sentence and the status words in R123's landed form (R-U: «… is not M4, so this is not M4;
  G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim»); the source note.
- Premise: as G-4 of the fill record, all landed or SPEC text: RESULTS R104's definitions of the genome, of Γ(G), of IDEAL-ACYC (l. 9910)
  and of the start pair, no R104 theorem; RESULTS R117 (b) Γ3(G) and its pads [every genome] (l. 13425-13430), (c) Lemma S3-START [every
  genome] (l. 13431-13433), (e) TAU3 [every genome] (l. 13438), (f) Theorem REACH3 [IDEAL-ACYC] (l. 13445-13452; EXACT-L only); RESULTS R118
  (k) Theorem REACH3-CYC [every genome; PROVED-CONDITIONAL on [REACH-L]] (l. 13704-13712; END-T3 only), with its title's condition sentence
  (l. 13607); [1E-N3] = RESULTS R57 (b) as landed in R104 (l. 9864) and R117 (l. 13362); RESULTS R15 (c) (l. 636-638; TERM-XI); SPEC S1-S5
  with FIX 1 and FIX 3 (docs/new/N5-ssi-global.md). Not used (packet l. 80-81): «ESC3, W3, KEY3, SBAR3, PLAY3, PAD (b)-(c) (pads are handled
  directly in §2), R118 (b)'s [OPT], any box 194 / P-N5-QUIET lemma, any L-RED lemma». Both referees checked every premise quote by script
  against trunk (REFEREE §2.1: «all 33 quotes found, same status on both»; REFEREE-2 «53 quotes, 44 in trunk sources, 9 self-quotes, 0
  missing»).
- L41 and L43. The packet's proofs are L-NEW successor 63's («This packet carries every proof in full.», l. 4); E0-E4's skeleton and the
  ENDGAME-3 conjecture are L-RED 56's, credited in the line («credit: ENDGAME-3 conjecture, E0-E4 skeleton and family generator L-RED 56,
  R221 §10-§11»); L-RED is an adversary lane, not a referee. No fixes entry carries referee-written proof text: entry 2's EN-1..EN-4 are
  REFEREE's scope, reading and wording items (EN-4 restates (H) on the value, «Same meaning, stated on the value.»), entry 3's S1-S5 and
  entry 4's R-U and R-T0 are line strings. Each referee re-derived every step (REFEREE «## 3. Proofs, each step re-derived»; REFEREE-2 «##
  Re-derivation (every step redone by hand; values (c, P, ℓ) in the SPEC order)»). L-4's scope tail names no referee-originated step
  («referee» 0 times in L-4 outside «REFEREE 29»); L41 (DECISIONS l. 355-360) does not apply: CHECKER C138 «**G-7 / L41: not triggered.** No
  proof step is referee-originated» (l. 47), and REFEREE §E on entry 4: «not L41's case» (l. 266). L43: every statement is exact (E0-E4,
  ENDGAME-3: one fallback, F + 2 iterations; EXACT-L: L(G) + 3) or a conditional identity (END-T3: T3 + 3); no statement is killed.
- Fixes (docs/new/P-N5-END-fixes.md, append-only; entry 1 by L-NEW successor 64 at a60733b8, l. 3-26, under «Lead 05:56Z: L-RED 58 R223
  items W-1 and T-1» (l. 3); the «Line L-1» note, l. 28-34; entry 2 by successor 64 at 2fcee038, l. 36-73, under «Lead 06:33Z» (l. 36);
  entry 3 by successor 65 at 8b67d40e, l. 75-92, line-only; entry 4 by successor 68 at b7faeebe, l. 94-114, line-only):
  - Entry 1 W-1 (R223 §1): the standing SPEC premise 1E-N3 on every row of «To sign» (l. 10-16); «No statement and no proof changes.» (l.
    16).
  - Entry 1 T-1: quotes_end.py reads every source by `git show TRUNK:path`, asserts the packet's sha1; re-run «quotes 33 missing 0» (l.
    18-26).
  - Entry 2 EN-1: the tie-break sentence after EXACT-L, with REFEREE 29's «F = 1 on 382 of 382» (l. 43-46); «ENDGAME-3-N5 does not depend on
    the tie-break (EN-2)» (l. 46).
  - Entry 2 EN-2: ENDGAME-3-N5 for every rule whose S4a output is a pointwise optimum of H (l. 47-48). EN-3: «bound N5» → «bound N5's
    iteration count» (l. 49-50). EN-4: (H) on the value (l. 51).
  - Entry 2 «Line L-2»: L-1 + R1-R16 by mkl2_195.py, the map LN-1..LN-8 → R1-R16 (l. 53-73).
  - Entry 3 S1-S5 (l. 81-87): S1 L-R1 (REQUIRED, REFEREE-2 34), S2 N-1, S3 N-2, S4 EL-1, S5 EL-2; «Line L-3» (l. 88-92). S6 (naming entry 3
    in the source note) dropped by the Lead (10:18Z).
  - Entry 4 (C138 E-1, E-2; l. 94-114, «L-NEW successor 68; LINE-ONLY»): R-U, the status words in R123's landed form (C138 E-1); R-T0, «τ0»
    → «S3's τ» in ENDGAME-3's clause (C138 E-2); «No statement, label, hypothesis, premise, proof or DATA number changes; the packet stays
    frozen» (l. 97-98); «Line L-4» (l. 109-114), with end.pins re-pinned (45 rows).
  - No entry changes a statement or a proof of the packet; entry 2's EN-4 restates a proof fact in the same meaning, and entry 3's S1
    narrows the line's wording of E1's consequence to the reading the proofs use, and entry 4's R-T0 names the packet's τ0 in the line's own
    terms (S3's τ).
- Not signed: packet §7 (DATA), §8 (machine checks), §9 (TARGET diff and limits), the READING after END-T3 (l. 196); the L-RED replays
  (cited); REFEREE-2's gate-order and n5w DATA (referee data).
- Referee strengthening (NOT part of this entry; referee checks):
  (i) REFEREE: own engine (scratch/end_replay.py on its xicyc_vj.VJ; its own Γ3 builder and FIX-1 start), modes xi and n5w, 3,060 runs per
    mode, every counter 0, controls fire (§4 (A), l. 89-94); EXACT-L and ENDGAME-3-N5 under SPEC's tie-breaks with L-COMP's n5b.py on its Γ3
    and t3r_sim for L(G): the 14 corpus genomes, 1,500 own runs (341 IDEAL-ACYC, lfail 0), SELFL_n3 (§4 (B), l. 95-100); EN-1's «382 with L
    ≥ 1: EXACT-L fails on all 382» (§4 (C), l. 101-103); check195.sh re-run byte-identical (§4 (D), l. 107).
  (ii) REFEREE-2: own r2end.py (own Γ3 builder, SPEC S1 from SPEC's text, N5, N5′-xi, n5w, IDEAL by P-N5-REALIZE §2; l. 112-115) on 7,614
    genomes per mode, 3,751 IDEAL-ACYC: «e0fail, e1fail, e2fail, e3fail, e4fail, finsbar, fintie, nofb, multifb, late, totfail, capped,
    oddfb and Hfail are 0 in every mode» (l. 122); EXACT-L lfail 0 (l. 127); n5w F = 1 on all 7,614 runs and EXACT-L failing on exactly the
    2,658 IDEAL-ACYC genomes with L ≥ 1 (l. 133-135); 1E-N3 spot check sbar_opt_fail 0 (l. 138-139); controls fire (l. 140-143); r2q.py
    quotes (l. 206).
- Honest limits: (i) Every statement is about two runs, N5 and N5′-xi from S3, on the games Γ3(G); nothing is claimed on other games, other
  starts or general parity games, and nothing bounds a running time or a bit cost (EXACT-L's Consequence is about iteration counts; the cost
  per iteration is a separate gauntlet step-4 item). (ii) Nothing bounds F, T3 or L(G): ENDGAME-3 says only that the run ends two iterations
  after its single fallback; L(G) stays OPEN. (iii) EXACT-L uses SPEC's S1 tie-breaks (through REACH3's [RULE] choice) and fails for another
  pointwise-optimal S4a rule (REFEREE 29: 382 of 382; REFEREE-2: 2,658 of 2,658); it is false without IDEAL-ACYC's self-loop clause
  (SELFL_n3: L(G) 1 under the set reading of N-1, N5 3 iterations). (iv) END-T3 is PROVED-CONDITIONAL on REACH3-CYC (R118 (k)), whose
  [REACH-L] premises R117 signs for every genome only in part (S3-START, PAD, K3, TAU3; ESC3 and W3 for acyclic Ξ-graphs only); it gives no
  bound on T3, and P-N5-QUIET's T_CYC bounds (RESULTS R123) are on Γ(G), not on the Γ3 run. (v) DATA are runs of the lane's implementation
  (box189 gamma3, box190 n5v, box195 eg195) and the referees' own engines on the named sets; lfail is record only (LRED unset in check.sh),
  and the clause «one fallback, 3 iterations from it» rests on the tally. (vi) Names: «TERM-XI», «ENDGAME-3», «ENDGAME-3-N5», «EXACT-L»,
  «END-T3» and the lemma labels E0-E4 are new to RESULTS (G-6). (vii) The source note names the packet, fixes entries 1-2 and L-NEW
  successors 63-64; entries 3 (successor 65) and 4 (successor 68) are line-only. (viii) Literature: none beyond R15's VJ00 §4.4; no novelty
  is claimed.
- Data (DATA, not proof): experiments/new/box195/ at l-new 8b67d40e (its tools, outputs and data unchanged to 25e040ee; b7faeebe adds
  mkl4_195.py and re-pins end.pins, 45 rows), eg195.py run by check195.sh (8 families × 300, seed 1953, per mode, plus every pinned genome
  of box189 and box191-box194; two controls), its frozen output check195.out (138 lines); the record sweep data/sweep195.out (8 families ×
  1,500 × seeds 1951, 1952 per mode, 24,000 runs per mode, plus the 14 corpus genomes in spec mode) and data/selfl195.out; called from the
  check.sh blocks «BOX 195 END» and «P-N5-END» (experiments/new/check.sh l. 1020-1035 at 8b67d40e, l. 1020-1038 at 25e040ee, where
  «P-N5-END» also asserts L-4's sha1 and size), run by scripts/verify.sh. Re-run by the drafter from a full git archive of 25e040ee: the two
  blocks 2026-11-09T06:07:47Z-2026-11-09T06:11:12Z, rc 0, «BOX 195 END: E0-E4 / ENDGAME-3 (xi and spec) 0 failures, controls fire = frozen:
  PASS» and «P-N5-END: packet and 45 pinned files match end.pins: PASS»; with one byte appended to L-4 the «P-N5-END» block prints «P-N5-END
  check: FAILED», rc 1 (negative control). The same blocks at 8b67d40e: rc 0 at 2026-11-09T02:03:20Z-2026-11-09T02:06:53Z (drafter, 43
  pinned files) and by CHECKER C138 (§5 l. 75-77: «03:35:51Z-03:38:55Z, rc 0»). REFEREE §E checked the 45 pins and re-ran mkl4_195.py from
  git archive b7faeebe: «end.pins 45 rows, `sha1sum -c` all OK» (l. 254-255). Frozen totals (by script): sweep 24,000 xi + 24,000 spec runs,
  every fail counter 0, every tally «one fallback, 3 iterations from it»; EXACT-L lfail 0 on 4,297 genomes (4,283 random IDEAL-ACYC in the
  spec rows, 3,000 of them from acyc, + 14 corpus), RECT_d11_T59_norm 62 iterations; ctrl1 e2fail, e3fail, e4fail, stopfail, finsbar, fintie
  100 of 100; ctrl2 e0fail 200, e1fail 200, nofb 100. Both referees re-ran check195.sh (REFEREE at 131b4c1c, «output byte-identical to
  check195.out (138 lines, 2 min 13 s)»; REFEREE-2 at 2fcee038, «check195.sh exit 0, output byte-equal to check195.out») and their own
  engines (above).
- Signatures: REFEREE docs/referee/R-P-N5-END.md: successor 29's report e4cb208a (e4cb208abe3c2bc5519fe87266cc71dec4458dab,
  2026-11-08T06:09:15Z) (heading «REFEREE successor 29 (Opus 5.5, D15). date -u at writing 2026-11-08T05:58Z.»), «Independent:
  docs/referee-2/ not read for this packet before this verdict was written.» (l. 2-3), verdict table l. 5-19; successor 29's §C 407f4a21
  (407f4a2158f2570dc98a2c865ae30b9cef88575c, 2026-11-08T08:09:56Z) (l. 169-220; heading «REFEREE successor 29, Opus 5.5, D15; date -u at
  writing 2026-11-08T07:53Z»), L-2 verdict l. 218-220; successor 30's §D 4434597c (4434597c947e8bca85792c10d49a1069b9a795ac,
  2026-11-08T10:54:53Z) (l. 222-246; heading «REFEREE successor 30, Opus 5.5, D15; date -u at writing 2026-11-08T10:54Z»), «**Line L-3
  MATCHES**» (l. 244); successor 30's §E 37195499 (3719549937af51513003a071861220929e23f196, 2026-11-09T05:27:35Z) (l. 248-268; heading
  «REFEREE successor 30, Opus 5.5, D15; date -u at writing 2026-11-09T05:27Z»), «**Line L-4 MATCHES**» (l. 267). REFEREE-2
  docs/referee-2/R2-P-N5-END.md: successor 34's report 9b3cc9b6 (9b3cc9b6fd2aae5946cec5e232fd9cb241987a47, 2026-11-08T09:10:47Z)
  («Independent: docs/referee/R-P-N5-END.md (REFEREE 29) NOT read before this report is committed.», l. 2-3), verdict table l. 20-35;
  Addendum 1 0f82f03b (0f82f03b0e66a4e175a710d19aad37e813fff430, 2026-11-08T09:30:50Z) (l. 214-241), «read after 9b3cc9b6 was on origin» (l.
  214); successor 35's Addendum 2 0e5c7c37 (0e5c7c37b567320d97621914b462c17d94cbfb53, 2026-11-08T11:05:52Z) (l. 243-263; heading «REFEREE-2
  successor 35, Opus 5.5, D1; 2026-11-08 10:54Z by date -u»), «**L-3 MATCHES.**» (l. 262); successor 35's Addendum 3 63a3cf87
  (63a3cf87c0ea0faa106fddef23d421bbe5c8ec90, 2026-11-09T05:27:17Z) (l. 265-278; heading «REFEREE-2 successor 35, Opus 5.5, D1; 2026-11-09
  05:27Z by date -u; independent of REFEREE»), «**L-4 MATCHES**» (l. 278). Lane (claude/l-new): L-NEW successor 63, 131b4c1c (packet
  FROZEN); successor 64, a60733b8 (fixes entry 1, L-1) and 2fcee038 (fixes entry 2, L-2); successor 65, 8b67d40e (fixes entry 3, L-3);
  successor 68, b7faeebe (fixes entry 4, L-4).
- INDEPENDENCE: the packet's proofs are L-NEW's (L41 and L43, above); each referee re-derived every step and replayed the DATA on its own
  code (REFEREE: end_replay.py on its own VJ engine and builder, «no lane code», l. 89; REFEREE-2: «Own code throughout (no lane, L-RED or
  REFEREE module)», l. 113). Each referee wrote its first report without reading the other's (REFEREE l. 2-3; REFEREE-2 l. 2-3); REFEREE-2
  compared afterwards (Add. 1); REFEREE 29's §C and 30's §D read REFEREE-2's strings only as quoted or for S1-S3
  («docs/referee-2/R2-P-N5-END.md was read (after successor 29's verdict, as its §C allowed) only for the S1-S3 strings.», l. 246).
  Disclosure at REFEREE-2: «the fixes file (entry 2) and line L-2 quote REFEREE 29's verdicts in outline» (l. 4-5). L-RED R222 / R223 were
  context only at both (REFEREE l. 3; REFEREE-2 l. 3-4). The L-3 wording is the referees' strings (L-R1, N-1, N-2 from REFEREE-2; EL-1, EL-2
  from REFEREE), applied by the lane by script under the Lead's 10:18Z routing; each referee byte-tested L-3 with its own script (REFEREE §D
  end_l3.py; REFEREE-2 Add. 2 bt_l3.py) and read S1-S5 in meaning. L-4's two new strings are CHECKER C138's (§4), applied by the lane by
  script (mkl4_195.py); each referee byte-tested L-4 from C138's text, not from the lane's script (REFEREE §E end_l4.py, «with the strings
  typed from C138 §4 (claude/checker 46905772; wrapped lines joined with one space), not from the lane's script», l. 251-252; REFEREE-2 Add.
  3 bt_l4.py, «uses CHECKER 23's strings, verbatim from C138 §4 at claude/checker 46905772», l. 268-269), and read R-U and R-T0 in meaning;
  REFEREE §E: «docs/referee-2/ not read for this section.» (l. 268); REFEREE-2 Add. 3 is headed «independent of REFEREE» (l. 265).
- TARGET.md diff: TARGET.md §2 (M4) asks for one algorithm, polynomial on EVERY parity game, that outputs (W_E, W_O); every statement here
  is an exact count of iterations of two runs on the family {Γ3(G)}, or an identity between N5's count and L(G) on IDEAL-ACYC genomes, or a
  conditional identity; none bounds a count on general games (TARGET.md §4: «Polynomial only on a restricted class»; packet §9 l. 225-228;
  REFEREE §8 «it is a statement about iteration counts (EN-3)»; REFEREE-2 «Not M3, not M4, not a step-4 pass; G-N5-TIME stays OPEN.
  Right.»). It is not an algorithm claim on every game, so TARGET.md §5's gauntlet does not apply, and it is not a step-4 pass. L-4 carries
  «N5′-xi stays a CANDIDATE (D1)» and «is not M4, so this is not M4; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md
  claim», each once (by script; R123's landed form, R-U, C138 E-1). GAPS G-N5-TIME: open.

Proposed GAPS line-11 UPDATE (append-only), to go AFTER the last UPDATE on GAPS l. 11 at landing (R123's, «UPDATE 2026-11-09 00:52Z: RESULTS
R123 (P-N5-QUIET; CHECKER C137 3479ecb0)», the last at origin trunk 090f89d4, whose GAPS is 9acebb5c's), as a pure insertion with one
separating space before the row's closing « |». BUILT FROM L-4 by tools/upd124b.py (R118's procedure: the direct build of
r123b/tools/upd123b.py with R124's constants: date «(2026-11-08)», start «for every genome G, each PROVED (every genome): », its nine
labels, source prefix «(P-N5-END, docs/new/P-N5-END.md»), with NO reading; control: the same function rebuilds R123's landed UPDATE from
R123's L-4 with no reading (sha1 739c5f71… unfilled; filled with 2026-11-09, 00:52, 3479ecb0 it is the last UPDATE on l. 11: True); sha1
8cd83060b9cb5d22f3b3e4dfeb0ec6588e0dded0 of the line without newline and unfilled, = C138 §4's UPDATE-4 (True). <DATE>, <HH:MM> and
<checker> are the landing date, time and the C138 commit, all filled at landing:
UPDATE <DATE> <HH:MM>Z: RESULTS R124 (P-N5-END; CHECKER C138 <checker>) [refereed-only] LANDED: On Γ3(G) of RESULTS R117 (Γ(G) of R104 with 4M + 4 single-successor Even pads of priority ≤ 2, n = N + 7M + 10), for N5 (SPEC S1-S5 with FIX 1-4) and N5′-xi (RESULTS R118's [N5XI], SPEC with box 190's S4a tie rule) from SPEC's default start S3, iterations counted as in SPEC S4, for every genome G, each PROVED (every genome): τ never changes and Iτ = ∅ at every state (Lemma E0); at every state with the core K-config κ0 = (σ(K0), σ(K1), σ(K3)) = (pA, s, K2) the only improving core edge is (K0, K1) and every S4a step keeps κ0, so the K-config leaves κ0 only at a fallback and the run cannot stop before one (Lemma E1); the first fallback, at iteration F ≥ 1, is an Even fallback with result K-config κ1 = (K1, s, K2) (Lemma E2); from κ1 the next iteration is an S4a step to κ2 = (K1, q, K2) (Lemma E3); from κ2 the next iteration is an S4a step to σ* with K-config κ3 = (K1, q, K1) and σ*(β_g) = pb_g at every gate g, and Iσ* = ∅ whatever σ* is at the movers (Lemma E4); both runs terminate (Lemma TERM-XI); N5′-xi, and N5, from S3 on Γ3(G) have exactly one fallback, at an iteration F ≥ 1, and exactly F + 2 iterations, iterations 1, …, F − 1 being S4a steps with K-config κ0 and S3's τ (Theorem ENDGAME-3, Theorem ENDGAME-3-N5); N5 (SPEC S1-S5 with its FIX 1-4 tie-breaks) from S3 on Γ3(G) makes exactly L(G) + 3 iterations, L(G) the length of G's IDEAL run, so on {Γ3(G) : G ∈ IDEAL-ACYC} N5's iteration count is polynomial in n iff L(G) is polynomial in N + M (a statement about iteration counts; the cost per iteration at bit cost is a separate gauntlet step-4 item) (Corollary EXACT-L, PROVED for G ∈ IDEAL-ACYC (R104: the Ξ-graph is acyclic; self-loops count as cycles; «Ξ-graph is ACYCLIC (self-loops count as cycles)»), premise RESULTS R117 (f); it uses SPEC's S1 tie-breaks, through REACH3's [RULE] choice: with another pointwise-optimal S4a choice the identity can fail, F = 1 on 382 of 382 IDEAL-ACYC genomes with L ≥ 1, REFEREE 29's counter, R-P-N5-END §4 (C), claude/referee e4cb208a, docs/referee/scratch/end_logs/tiedep.out, cited, not re-run); if REACH3-CYC holds for G, N5′-xi from S3 on Γ3(G) makes exactly T3 + 3 iterations, with T3 as in R118 (k) (P-N5-XICYC §7: «T3 is the first state at which no mover has a strictly better successor in Γ3»), T3 + 1 being the first fallback (premises, all under the standing SPEC premise 1E-N3 of RESULTS R57 / R104 / R117 (fixes entry 1, W-1: «Hypotheses of every row: under the standing SPEC premise 1E-N3 (RESULTS R57 (b)), as in RESULTS R104 / R117.»): RESULTS R104's definitions of the genome, of Γ(G), of IDEAL-ACYC and of the start pair only; RESULTS R117's definition of Γ3 and pad priorities (P-N5-REACH §3), Lemma S3-START and, for E0, [TAU3] (RESULTS R117 / P-N5-REACH §6.4: «In the standard state, Iτ = ∅, so S4b leaves τ unchanged.», signed for every genome per R118: «RESULTS R117's entry signs S3-START, PAD, K3 and TAU3 for every genome»); [1E-N3] = RESULTS R57 (b) as landed in R104 («used in two forms: S1's σ̄, and τ̄ on the dual game, are pointwise optima; and S4a's σ_new»…, a pointwise optimum of the S4a arena before S4c), used for σ̄ and for S4a's σ_new inside SPEC runs (REFEREE 29 rules [OPT] = [1E-N3] for SPEC runs; R118 (b)'s [OPT] is not used); RESULTS R15 (c) («every non-empty switch of improvements goes strictly up in ≺») for TERM-XI; RESULTS R117 (f) for EXACT-L only; RESULTS R118 (k) for END-T3 only; the SPEC text docs/new/N5-ssi-global.md S1-S5 with FIX 1 and FIX 3; not used: ESC3, W3, KEY3, SBAR3, PLAY3, PAD (b)-(c), R118 (b)'s [OPT], any P-N5-QUIET or box 194 lemma, any L-RED lane lemma) (Corollary END-T3, PROVED-CONDITIONAL on REACH3-CYC, RESULTS R118 (k), itself PROVED-CONDITIONAL on [REACH-L]: «CONDITIONAL on P-N5-REACH's S3-START, PAD, K3, TAU3, ESC3, W3 for every genome», and of these RESULTS R117 signs S3-START, PAD, K3 and TAU3 for every genome but ESC3 and W3 for acyclic Ξ-graphs only): this gives the exact END of two runs on one family of games and, for IDEAL-ACYC genomes, an identity between N5's count and L(G); it bounds none of F, T3, L(G) (OPEN), and nothing outside Γ3(G); EXACT-L is false without IDEAL-ACYC's self-loop clause: L-RED 57's SELFL_n3 (N 3, two Ξ self-loops; experiments/new/box195/inst/SELFL_n3.json, sha1 27bc7f72…) has L(G) = 1 (IDEAL run read with B_s the set of β-ids on its eventually periodic X-chain; R104's IDEAL run is defined on IDEAL-ACYC) and N5 makes 3 iterations (F = 1); END-T3 gives no bound on T3: P-N5-QUIET's QUIET / T-QUIET bound IDEAL-CYC's T_CYC on Γ(G), and their transfer to the Γ3 run is NOT proved (the Γ3 run can differ from the IDEAL-CYC run at exact VJ ties, R118's DATA); DATA, clause by clause (unit: runs of N5′-xi (EG195_MODE xi) or N5 (spec) from S3 on Γ3(G) built by box189/gamma3.py, stepped by box190/n5v.py; tool experiments/new/box195/eg195.py, run by check195.sh; set: 8 families (rand d 1-5; L-RED R221 §11's esc, noesc, deep, dense, lvl0, transcribed; late, a stand-in with start = each mover's last option; acyc) × 1,500 × seeds 1951, 1952, 24,000 runs per mode, 48,000 in all (data/sweep195.out), plus the 14 R117 corpus genomes in spec mode (sweep195.out); and check195.out (re-run by check.sh): 8 families × 300, seed 1953, per mode, plus every pinned genome of box189 and box191-box194; all pinned in box195/end.pins): E0: e0fail 0 (unit: states); E1: e1fail 0 (unit: iterations before the first fallback); E2, E3, E4 (a): e2fail, e3fail, e4fail 0 (unit: the iterations F, F + 1, F + 2); E4 (b): stopfail 0, finsbar 0, fintie 0 (unit: final states); ENDGAME-3, ENDGAME-3-N5: nofb 0 and capped 0 (unit: runs), late 0 (unit: iterations after F + 2), every run «one fallback, 3 iterations from it»; EXACT-L: lfail 0 (unit: IDEAL-ACYC genomes with F ≠ L(G) + 1 or total ≠ L(G) + 3) on 4,297 genomes, spec runs only (4,283 random IDEAL-ACYC ones in the spec rows of sweep195.out, 3,000 of them from acyc, and the 14 corpus genomes; L(G) up to 59, RECT_d11_T59_norm, 62 iterations; L(G) by L-RED's ideal.traj at claude/l-red 86a7a7a8, record only (not re-run by check.sh, which leaves LRED unset)); controls fire (check195.out: ctrl1 e2fail, e3fail, e4fail, stopfail, finsbar, fintie 100 each in 100 runs; ctrl2 e0fail 200 (unit: states) and e1fail 200 (unit: iterations before the first fallback), nofb 100 (unit: runs)); independent replays, every fail counter 0, their counters in their own pinned outputs, cited, not re-run: L-RED 57 R222 item 3 (claude/l-red 6f56004c), L-RED 58 R223 item 1 (claude/l-red 143f0b4c), REFEREE 29 R-P-N5-END §4 (A), (B) (claude/referee e4cb208a); no separate DATA for TERM-XI and END-T3; N5′-xi stays a CANDIDATE (D1); TARGET.md §2 (M4) asks for an algorithm polynomial on every parity game and §4 says a bound on a restricted class is not M4, so this is not M4 (P-N5-END, docs/new/P-N5-END.md, frozen at l-new 131b4c1c, sha1 5cae845b, with fixes entries 1-2, docs/new/P-N5-END-fixes.md; L-NEW successors 63-64; credit: ENDGAME-3 conjecture, E0-E4 skeleton and family generator L-RED 56, R221 §10-§11). G-N5-TIME stays open.

Addendum (subagent, for the Lead; does not land; written 2026-11-09T02:19:19Z by date -u). (1) FIRST FILL on line L-3 (l-new 8b67d40e, sha1
d6afe92a…), to CHECKER C138. Nothing in the repository was edited, committed, merged or pushed by me; the file was written into the
scratchpad r124a/ by r124a/fill1.py, for the Lead to copy to docs/agents/R124-draft.md and commit. Fetches: 01:59:33Z and
02:14:03Z-02:14:04Z (record); every head unchanged at the second. (2) TITLE d[284] (l. 285) = "### R124 [refereed-only] " + L-3 without its
newline + ", CHECKER PASS (docs/checker/C138.md, checker PENDING)", checked by script (chk124a.py): equal, byte for byte (True); the title
minus that prefix and that tail is L-3 (True); the only «### R» heading of this file; 7,169 characters, 7,293 bytes, sha1 of the heading
line without its newline 18cb68e152ee1ee527aeb92464a5953a7fa8019d; 106 «(» / 106 «)» (L-3's 105 and the tail's), 0 "|", «[refereed-only]»
once. (3) SHAPE. The entry block is l. 285-476 (python slice d[284:476], 192 lines), followed by a blank line (d[476]); 0 "|" in it;
«checker PENDING)» once in it (four times in the whole file: the title, item (1) of the record and items (2) and (3) of this Addendum); the
landing anchor, a line starting «**Erratum E-1** (not a result», 0 times in it. The GAPS preamble is l. 478-487 (d[477:487]); the UPDATE is
l. 488 (d[487]), one line, sha1 262a881c3f26912728e2976d53d84258c279b49f without newline and unfilled
(f6a268a38e8b693c50e69210e8de05ab929ed9d5 with it; = upd124L3.txt, True), 7,237 bytes, 7,115 characters, 1,216 tokens, 105 «(» / 105 «)», 0
"|", one each of «<DATE>», «<HH:MM>», «<checker>», «2026-11-08» 0 times, « — » 0 times. A landing script slices d[284:476] for the entry and
reads d[487] for the UPDATE, with «R124», «C138», PREV = R123's block and UPDATE. The FIRST FILL record is l. 2-283 (d[1:283]), then a blank
line (d[283]). (4) WHAT IS LEFT: the Lead's ruling on G-7 (L41; none found in my reading) and its routing of G-U (R-U) and G-2 (ii) (R-T0);
CHECKER C138 on this file (G-U (i), (iii), (iv); G-2 (ii); G-1 (ii); G-4 (ii); G-6; G-11's optional note; the G-9 notes); if either
replacement is taken, an L-4 by L-NEW (fixes entry 4, line only), both referees' byte tests, and a second fill (title, line history, Object,
Honest limits (vii), Signatures, the UPDATE rebuilt from L-4 by the same procedure with no reading). The Lead merges claude/checker (C138's
commit) before landing; every lane and referee commit the entry needs is already an ancestor of 9acebb5c; then lands R124 with <DATE>,
<HH:MM> and <checker> filled. (5) QUOTE SWEEP (chk124a.py: outermost guillemet quotes, nested ones inside them, split at «…», parts of 6+
characters, whitespace-normalised, NO docs/agents draft as a source; sources: the packet, the fixes file at 8b67d40e, 2fcee038, a60733b8,
L-1, L-2, L-3, REFEREE's file at 4434597c and tiedep.out at e4cb208a, REFEREE-2's file at 0e5c7c37, RESULTS, GAPS, DECISIONS,
DECISIONS-INDEX, NOW, TARGET.md, CLAUDE.md, SPEC, P-N5-REACH, P-N5-XICYC at 9acebb5c, LEAD-STATE at a773c562, C133-C135, C137 and
notes/CHECKER.md at 2101cd36, check.sh, eg195.py, check195.sh, check195.out, sweep195.out, selfl195.out at 8b67d40e, R123's L-4, the
subjects of the 14 commits cited with subjects, and my outputs upd124L3.txt, upd124L3_RU.txt, L3_RU.txt, blocks.out, upd124a.out): on the
draft before this Addendum, line 1 and the record 223 quotes, 203 parts, 0 not found; entry block 137 quotes, 134 parts, 0 not found; GAPS
preamble and UPDATE 19 quotes, 18 parts, 0 not found; whole file 379 quotes, 355 parts, 0 not found; NEGATIVE CONTROL (a made-up quote)
reported missing (True); the run on the final file is in chk_final.out. lp124a.py (fresh git show, independent of fill1.py's check): 140
cited quotes in 16 (commit, file) pairs, each inside its cited lines, 0 failed, 0 missing from the draft; NEGATIVE CONTROLS: the same quotes
against windows shifted by 40 lines, 0 of 140 pass; with their longest word mutated, 0 of 140 pass. hex124a.py: 74 hex ids, 43 git objects,
31 measured sha1s, 0 neither; NEGATIVE CONTROL (two made-up ids) both reported. (6) STALE STATUS (chk124a.py, case-insensitive): in the
entry block with the title excepted «pending», «will », «awaiting», «to come», «not landed», «first fill», «second fill», «this fill», «to
land» 0 each; «not yet» 1 (REFEREE-2's L-2 verdict, quoted as history); the title has «PENDING» once (the fill); GAPS preamble and UPDATE: 0
each; line 1 «NOT LANDED» 1 (R124 is not landed). (7) LANDING SIMULATION (sim124a.py on in-memory copies of RESULTS 428bc92f… and GAPS
82e9d475… at origin trunk 9acebb5c): R124's d[284:476] (its «checker PENDING» filled with 3333333) + a blank line inserted directly before
the line-start «**Erratum E-1** (not a result», after R123's block (l. 15076-15369) and its blank line (l. 15370): a pure insertion (prefix
and suffix byte-unchanged, True); RESULTS 16,013 → 16,206 lines (+193); R124 at l. 15371-15562, blank l. 15563, «**Erratum E-1**» to l.
15564, E-2 15577, Note E-3 15605, Dead ends 15636; order R122 < R123 < R124 < E-1 < E-2 < E-3 < Dead ends: True; «|» 1,477 → 1,477
(unchanged); R124 the last "### R1xx" heading. GAPS: only l. 11 changes (True), the closing " |" replaced by " " + R124's filled UPDATE + "
|"; "|" on l. 11 76 → 76 (whole file 198 → 198); «UPDATE 2026-» 58 → 58 plus one head with the simulation year 2099 after R123's; R124's
UPDATE last and after R123's (True); 23 → 23 lines. Fill values used only for the simulation: 2099-01-11, 00:00, 3333333. (8) UPDATE
(upd124a.py): R118's procedure as the direct build of r123b/tools/upd123b.py (l. 32-60), generalised only in its constants; CONTROL: with
R123's constants on R123's L-4 (87603d07, 0809da25…) and no reading it gives 739c5f71… (= R123's draft UPDATE), which filled with
2026-11-09, 00:52, 3479ecb0 occurs once on GAPS l. 11 at 9acebb5c and ends it (True). R124 on L-3 without a reading: AssertionError («; not
M3, not a step-4 pass, not a TARGET.md claim» not in L-3, G-U). With the reading: 262a881c…; connectors «; » ×8 kept in front of their
clauses; token diff L-3 → UPDATE 19 hunks, 149 tokens out, 146 in: the head inserted («UPDATE <DATE> <HH:MM>Z: RESULTS R124 (P-N5-END;
CHECKER C138 <checker>) [refereed-only] LANDED:»); the nine labels moved behind their clauses (END-T3's, with its inner quote, in place of «
(2026-11-08) —», followed by «:», after the premises parenthesis, G-U (iii)); «G-N5-TIME stays OPEN,» dropped; «M4: not M3, not M4, not a
step-4 pass, not a TARGET.md claim» → «M4»; «§10-§11)» → «§10-§11). G-N5-TIME stays open.». Nothing else. L-3 + R-U (2f8a11f9…, 7,226 bytes)
by the procedure with NO reading: 0d9faf25… (7,256 bytes) = the draft's UPDATE with «is not M4 (P-N5-END» → «is not M4, so this is not M4
(P-N5-END» (True); with the reading on L-3 + R-U: AssertionError (as expected). L-3 + R-U + R-T0: 5f88c297… / 8cd83060… (True). Pipe rule:
the filled R124 UPDATE appended after R123's: 76 "|" on l. 11, R124's last, prefix byte-unchanged (True). (9) NOT VERIFIED / NOT DONE:
scripts/verify.sh and scripts/push.sh not run (the two box 195 blocks of experiments/new/check.sh only, from a full git archive of 8b67d40e;
not the whole check.sh); the referees' tools and the lane's mkl*_195.py and quotes_end.py not re-run (their outputs and both referees' byte
tests read); no simulator of my own (the DATA are the lane's tools, re-run through the blocks; gamma3, n5v and n5x not read beyond what
eg195.py calls); the proofs not re-derived by me beyond reading the packet and both referees' re-derivations (G-7 is a text check of where
each candidate step stands); L-RED R222 / R223 not read (cited by the line as L-RED's counters; their commits' ancestry checked only); no
Oink run (L-3 cites no Oink check). (10) Scratch:
/tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad/r124a/ (src/ (the packet, fixes, L-3, the
referee files at each commit, RESULTS, GAPS, C133-C137, sources); arch/ = full git archive of 8b67d40e; blocks.out, blocks.rc, blocks.start,
blocks.end; tools/blocks195.sh, runblocks.sh, upd124a.py (upd124a.out, upd124L3.txt, upd124L3_RU.txt, L3_RU.txt), chk124a.py (chk_p1.out,
chk_final.out), lp124a.py (lp_p1.out, lp_final.out), hex124a.py (hex_p1.out, hex_final.out), sim124a.py (sim_p1.out, sim_final.out),
loc124.py; fill1.py, cites.json, fetch.txt, filltime.txt, addtime.txt, report.txt).

Addendum 2 (subagent, for the Lead; does not land; written 2026-11-09T06:20:21Z by date -u). (1) SECOND FILL on line L-4 (l-new b7faeebe,
sha1 5f88c297…), to CHECKER C138 Add. 1. Built in the scratchpad by fill2.py from git show b3c7b461:docs/agents/R124-draft.md (sha1
f7aa004e…, asserted; the same file at origin trunk 090f89d4); I merged, committed and pushed nothing and wrote nothing into the repository;
the Lead commits this file. Fetches: 06:04:22Z-06:04:24Z and 06:11:24Z-06:11:25Z (SECOND FILL section); a third fetch of the same five
branches at 2026-11-09T06:21:27Z-06:21:28Z by date -u, rc 0, after the build: referee, referee-2, checker and trunk unchanged; l-new now
764a8f86 (764a8f86a3ce1e0232a9884cbb97c5e386005cf4, 2026-11-09T05:36:43Z, BOX 203 part 2), a descendant of 25e040ee; git diff 25e040ee
764a8f86 on the packet, the fixes file, the four line files and experiments/new/box195/ is empty, and check.sh l. 1020-1038 are the same
lines at both, so nothing in this file changes. (2) TITLE d[436] (l. 437) = "### R124 [refereed-only] " + L-4 without its newline + the fill
tail ", CHECKER PASS (docs/checker/C138.md, checker " + "PENDING)", checked by script (chk124b.py): equal, byte for byte (True); the title
minus that prefix and that tail is L-4's bytes without the newline (True); the only «### R» heading of this file; 7,184 characters, 7,308
bytes, sha1 of the heading line without its newline b11ae45fe170780410b68a7772f6dcd4563bdc1b; 106 «(» / 106 «)» (L-4's 105 and the fill's),
depth never negative, 0 "|", «R1xx» 0, «[refereed-only]» once, the fill token once. (3) SHAPE. The entry block is l. 437-659 (python slice
d[436:659], 223 lines), followed by a blank line (d[659]); 0 "|" in it; the fill token once in it (four times in the whole file: the title,
item (1) of the FIRST FILL record and items (2) and (3) of the first fill's Addendum; this Addendum spells it in two pieces); the landing
anchor «\n**Erratum E-1** (not a result» 0 times in it («**Erratum E-1**» 0 times). The GAPS preamble is l. 661-668 (d[660:668]); the UPDATE
is l. 669 (d[668]), one line, sha1 8cd83060b9cb5d22f3b3e4dfeb0ec6588e0dded0 without newline and unfilled
(58a216f401f49db359fc3eee398894446c64323d with its newline; = upd124L4.txt, True; = C138 §4's UPDATE-4), 7,260 bytes, 7,138 characters,
1,222 tokens, 105 «(» / 105 «)», 0 "|", one each of the three fill tokens, «2026-11-08» 0 times, « — » 0 times. A landing script slices
d[436:659] for the entry and reads d[668] for the UPDATE, with «R124», «C138», PREV = R123's block and UPDATE (both landed). The SECOND FILL
section is l. 2-153 (d[1:153]); the FIRST FILL record l. 154-435 (d[153:435]), then a blank line (d[435]); the first fill's Addendum l.
671-733 (d[670:733]); this Addendum follows a blank line. (4) WHAT IS LEFT: CHECKER C138 Add. 1 on this file (C138 §6: cmp L-4 with §4,
UPDATE = 8cd83060, word diff of the entry against the first fill, ancestry, quotes, landing simulation on the then trunk; and the notes D-6
to D-9, N-S and N-L41 of the SECOND FILL section); the Lead merges claude/l-new (b7faeebe or later; 25e040ee for the check.sh L-4
assertion), claude/referee (37195499 or later), claude/referee-2 (63a3cf87 or later) and claude/checker (46905772 and C138 Add. 1's commit)
before landing, none of which is an ancestor of origin trunk 090f89d4 or of the local HEAD b8408b39; then lands R124 after R123 with <DATE>,
<HH:MM> and <checker> filled. (5) QUOTE SWEEP (chk124b.py: outermost guillemet quotes, nested ones inside them, split at «…», parts of 6+
characters, whitespace-normalised, NO docs/agents draft as a source; sources: the first fill's (its 33 files and 14 commit subjects, and
r124a's outputs) and the new ones: C138.md and notes/CHECKER.md at 46905772, the fixes file and L-4 at b7faeebe, REFEREE's file and
l4test.out at 37195499, REFEREE-2's file and bt_l4.out at 63a3cf87, check.sh at 25e040ee, mkl4_195.py at b7faeebe, LEAD-STATE at b8408b39,
RESULTS, GAPS, DECISIONS and NOW at 090f89d4, the subjects of 25e040ee, b7faeebe, 37195499, 63a3cf87, 46905772, 090f89d4 and b8408b39, and
my outputs blocks.out, neg_pin.out, mk.out, l4rel124b.out, upd124b.out, upd124L4.txt): on the draft before this Addendum, line 1 0 quotes;
the SECOND FILL section 120 quotes, 121 parts, 0 not found; the FIRST FILL record 223 quotes, 203 parts, 0 not found; the entry block 171
quotes, 164 parts, 0 not found; GAPS preamble and UPDATE 14 quotes, 13 parts, 0 not found; the first fill's Addendum 45 quotes, 31 parts, 0
not found; whole file 573 quotes, 532 parts, 0 not found; NEGATIVE CONTROL (a made-up quote) reported missing (True); the run on the final
file is in chk_final.out. lp124b.py (fresh git show, independent of fill2.py's own check): the 61 quotes new at this fill in 8 (commit,
file) pairs (C138.md 20, REFEREE 12, REFEREE-2 11, fixes 9, L-4 5, the packet 2, check.sh 1, GAPS 1), each inside its cited lines, 0 failed,
0 missing from the draft; NEGATIVE CONTROLS: the same quotes against windows shifted by 40 lines, 0 of 61 pass; with their longest word
mutated, 0 of 61 pass. (6) STALE STATUS (chk124b.py, case-insensitive): in the entry block with the title excepted «pending», «will »,
«awaiting», «to come», «not landed», «first fill», «second fill», «this fill», «to land» 0 each; «not yet» 1 (REFEREE-2's L-2 verdict,
quoted as history); «L-3 » 13 times, each history (line history, L-3's rounds, entry 3, the lane commit, L-4 = L-3 + R-U + R-T0); the title
has «PENDING» once (the fill); GAPS preamble and UPDATE: 0 each. Line 1 «NOT LANDED» once (R124 is not landed). (7) LANDING SIMULATION
(sim124b.py on in-memory copies of RESULTS 428bc92f… and GAPS 82e9d475… at origin trunk 090f89d4; the same result at the local HEAD
b8408b39): R124's d[436:659] (the fill token filled with a simulation value) + a blank line inserted directly before the line-start
«\n**Erratum E-1** (not a result», after R123's block (l. 15076-15369) and its blank line (l. 15370): a pure insertion (prefix and suffix
byte-unchanged, True); RESULTS 16,013 → 16,237 lines (+224); R124 at l. 15371-15593, blank l. 15594, «**Erratum E-1**» to l. 15595, E-2
15608, Note E-3 15636, Dead ends 15667; order R122 < R123 < R124 < E-1 < E-2 < E-3 < Dead ends (True); R124 the last of 25 "### R1xx"
headings; "|" in RESULTS 1,477 → 1,477 (unchanged). GAPS: only l. 11 changes (True), its closing " |" replaced by " " + R124's filled UPDATE
+ " |"; "|" on l. 11 76 → 76 (whole file 198 → 198); «UPDATE 2026-» 58 → 58 plus one head with the simulation year 2099 after R123's; R124's
last and after R123's (True); 23 → 23 lines. Fill values used only for the simulation: 2099-01-11, 00:00, 3333333. (8) UPDATE (upd124b.py;
SECOND FILL section (c)): from L-4 with no reading = 8cd83060… = C138 §4's UPDATE-4 (True) = the first fill's d[487] with C138's two
replacements (True); control on R123's L-4 = R123's landed UPDATE, the last on GAPS l. 11 at 090f89d4 (True); R124's filled UPDATE appended
after it keeps 76 "|" (True). (9) KEPT SECTIONS AND WORD DIFF (rec124b.py): the FIRST FILL record d[153:436] = the first fill's d[1:284]
(True, 283 lines with its blank line) and the first fill's Addendum with its blank line d[669:733] = its d[488:552] (True); the first fill's
title and UPDATE lines occur nowhere in this file. Token diff first fill → this fill: title 4 hunks (7 tokens out, 11 in: R-U and R-T0
only); entry block without title 55 hunks (73 tokens out, 725 in), each inside a change named in the Changes paragraph of the SECOND FILL
section (rec_final.out prints every hunk); UPDATE 2 hunks (1 token out, 7 in: C138 §4's two replacements). (10) HEX IDS (hex124b.py): in the
whole file before this Addendum 110 distinct hex ids: 62 git objects, 48 sha1s measured at this fill or the first (files at their commits,
the lines, the drafts, the UPDATE lines, the titles), 0 neither; NEGATIVE CONTROL (two made-up ids) both reported; b8408b39 (the local HEAD)
resolves here but was not on origin at my fetches; the run on the final file is in hex_final.out. (11) NOT VERIFIED / NOT DONE:
scripts/verify.sh and scripts/push.sh not run (the two box 195 blocks of experiments/new/check.sh only, from a full git archive of 25e040ee,
and the «P-N5-END» block once more for the negative control; not the whole check.sh); the referees' end_l4.py and bt_l4.py not re-run (their
outputs l4test.out and bt_l4.out read); the lane's mkl4_195.py re-run on a copy (rc 0, cmp-equal); the proofs not re-derived (R-T0's meaning
read against packet §2 (S) and both referees); L-RED's files not read; the first fetch's exit code not captured (the second fetch rc 0,
heads unchanged); LEAD-STATE read at the local HEAD b8408b39 only; C138 Add. 1 does not exist yet; no Oink run (L-4 cites no Oink check).
(12) Scratch: /tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad/r124b/ (src/ (the first fill,
the R122 and R123 fills read for the house form, the referee files at both commits); arch/ = full git archive of 25e040ee, arch_mk/ the copy
for mkl4_195.py; blocks.out, blocks.rc, blocks.start, blocks.end, neg_pin.out, mk.out, L4.bak; tools/blocks195b.sh, pinblock.sh,
runblocks.sh, units.py; tools/l4rel124b.py, l4rel124b.out; tools/upd124b.py, upd124b.out, upd124L4.txt; tools/chk124b.py, chk_p1.out,
chk_final.out; tools/lp124b.py, lp_p1.out, lp_final.out; tools/sim124b.py, sim_p1.out, sim_final.out; tools/rec124b.py, rec_p1.out,
rec_final.out; tools/hex124b.py, hex_p1.out, hex_final.out; parts/addendum2.src; fill2.py, cites2.json, fetch.txt, filltime.txt, fetch2.log;
report.txt).
