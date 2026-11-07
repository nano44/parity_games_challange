# Draft RESULTS R119 (Lead; first fill 2026-11-07T10:45:39Z by date -u (subagent) on P-IDEAL-DBL line L-2, docs/si/P-IDEAL-DBL-line-L2.txt, l-si 0ea6959f, sha1 1b3dc82544adfaf2cdea0deffbcbd052db9cd371 (draft sha1 3fb40db1, CHECKER C133 8f6d03bc: FAIL E-1..E-6); SECOND FILL 2026-11-07T14:55:19Z by date -u (subagent) on P-IDEAL-DBL line L-3, docs/si/P-IDEAL-DBL-line-L3.txt, l-si 610897dd, sha1 845ffdc9f0306d5db4bdb41d613588b219545838) — to CHECKER C133 Add. 1 — NOT LANDED; goes after R118 (LANDED at the local trunk 478d0bd9), before Erratum E-1
SECOND FILL (2026-11-07T14:55:19Z by date -u, subagent; for CHECKER C133 Add. 1). Read at the origin heads fetched at 2026-11-07T14:49Z
and again at 14:57Z (git fetch of claude/l-si, claude/referee, claude/referee-2, claude/checker, claude/vibrant-johnson-nxvvxo; the same
heads both times; a Lead push was running: I merged, committed and pushed nothing, and edited docs/agents/R119-draft.md only): l-si
610897dd (610897dde6955bf6b7b3eda0fa1bebf6630c88d0, 2026-11-07T12:38:17Z, «L-SI 42: P-IDEAL-DBL fix round 2 (CHECKER C133 E-1..E-6):
fixes entry 2 + line L-3 (sha1 845ffdc9) by script; check79 regenerates L-3; notebook trap», the branch head; git diff 0ea6959f 610897dd
names only docs/si/P-IDEAL-DBL-fixes.md (entry 2 appended), the new docs/si/P-IDEAL-DBL-line-L3.txt, the new
experiments/si/box79/c133_8f6d03bc.md (= docs/checker/C133.md at 8f6d03bc, by script), mkL3.py and mkfix2.py, check79.sh (the mkL3.py
step), pins.sha1 (the fixes re-pinned at edda8237; mkL3.py, mkfix2.py, the C133 copy and L-3 added) and notes/L-SI.md; the packet, L-1
and L-2 are byte-equal at 0ea6959f and 610897dd, by script), referee cb95edbf (REFEREE 27's handover check, the branch head;
docs/referee/R-P-IDEAL-DBL.md is the same blob at 07a950ae and cb95edbf: REFEREE successor 26's §C add. 1, l. 226-249, committed at
07a950ae, 2026-11-07T13:01:15Z; the file 249 lines, 20,264 bytes, sha1 17eb7af12acb56102fb231dec6e3d5e6d2093435; its l. 1-224 =
34589c09's file, by script), referee-2 7d7affb1 (REFEREE-2 successor 31's handover check, the branch head;
docs/referee-2/R2-P-IDEAL-DBL.md is the same blob at 37c733e2 and 7d7affb1: REFEREE-2 successor 30's Addendum 2, l. 168-185, with
R2-P-IDEAL-DBL/bt_l3.py and bt_l3.out, committed at 37c733e2, 2026-11-07T13:01:16Z; the file 185 lines, 19,383 bytes, sha1
a00e22b04230e82b00b1d5c54958acb7900c1084; its l. 1-166 = 1b9e3ea5's file, by script), checker 3dd22cbd (the last commit of CHECKER C132
Add. 1; docs/checker/C133.md is the same blob at 8f6d03bc and 3dd22cbd: 93 lines, 8,831 bytes, sha1
1a82f10900527db85de081426bea17ffbe653384). 610897dd, 07a950ae and 8f6d03bc are ancestors of the local trunk 478d0bd9 and of origin trunk
ebf59a34; 37c733e2 is NOT an ancestor of either (git merge-base --is-ancestor): the Lead merges claude/referee-2 before landing. Trunk:
R118 LANDED at the local trunk 478d0bd9 (2026-11-07T14:48:42Z, «Lead: land R118 XICYC (P-N5-XICYC, line L-4; CHECKER C132 Add. 1
af92b846 PASS); log»; being pushed; origin trunk ebf59a34 is its ancestor, four commits behind, without R118). RESULTS at 478d0bd9: sha1
576a89b7d6c98b7ba6b359897c8a94672d3cb9f0, 14,521 lines; «### R117» l. 13362, «### R118» l. 13607, «**Erratum E-1**» l. 13879, «**Erratum
E-2**» l. 13892, «**Note E-3**» l. 13920, «## Dead ends (kept;» l. 13951. GAPS at 478d0bd9: sha1
ac63d1a7fc1bfd3ffc753c765cc2ff9da952c7f9, 23 lines, l. 11 76 "|", 53 «UPDATE 2026-», the last R118's «UPDATE 2026-11-07 14:48Z: RESULTS
R118 (P-N5-XICYC; CHECKER C132 af92b846)».
New sources: CHECKER C133 (8f6d03bc, 2026-11-07T12:05:45Z): «Verdict: FAIL (E-1 to E-6; one L-3 with six replacements, §5)» (l. 15);
«All six are the drafter's flags (G-L, G-1, G-U, G-7, G-9 (i), (ii)).» (l. 16); E-1..E-6 are the first fill's G-L, G-1, G-U, G-9 (i),
G-9 (ii) and G-7, fixed by R1, R2, R3, R5, R6 and R4 (l. 20-37); on G-U: «I rule G-U accordingly: no new procedure is needed.» (l. 29);
«Not taken (note N-1): R-F» (l. 38); G-P: «R119 lands only after R118, after R118's block and before «**Erratum E-1**»; its UPDATE goes
after R118's.» (l. 40); everything else PASS (§4: check79.sh re-run from git archive 0ea6959f, the DATA clause by clause, the referees,
the quotes, the TARGET.md diff); §5: L-3 (sha1 845ffdc9…) and the UPDATE rule «R116's procedure, unchanged (sentinel_build111 with
R111's DEAD-clause step), on L-3. I check it in Add. 1 by token diff against L-3.» (l. 76-77), with no UPDATE sha1. Fixes entry 2
(docs/si/P-IDEAL-DBL-fixes.md l. 69-95 at 610897dd, L-SI successor 42; the file 95 lines, 11,286 bytes, sha1
edda8237f4c30cea060f44b20392b29a57b126a5, its l. 1-67 = entry 1's file); line L-3 (docs/si/P-IDEAL-DBL-line-L3.txt, 610897dd, the file's
only commit); experiments/si/box79/mkL3.py (30 lines), mkfix2.py, c133_8f6d03bc.md, check79.sh (30 lines, sha1
cfb906f75ba811bde8b317c297a4e6bd94e3c592) and pins.sha1 (27 lines, sha1 d22cc278c55400d66b58c14f5321c89a9ed1bd4b) at 610897dd; REFEREE
§C add. 1 (own byte test; R4's attribution, R5's range and R6's class checked; l. 249 its verdict, quoted in the entry) and REFEREE-2's
Add. 2, with its own bt_l3.py (R5, R6, R4, R3 read in meaning; l. 185 its verdict, quoted in the entry).
Checks run at this fill (scratch /tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad/r119b;
nothing written into the repository but this file). (a) l3rel119.py: L-3 at 610897dd is sha1 845ffdc9f0306d5db4bdb41d613588b219545838,
6,167 bytes, one line with its newline, 6,017 characters, 1,093 tokens, 101 «(» / 101 «)», depth never negative, final depth 0, 0 "|",
one « — », 0 «[»; byte-equal at the l-si head; R1-R6 parsed from C133 §5 at 8f6d03bc (l. 60-71, wrapped lines joined with one space) and
from fixes entry 2 (its OLD / NEW lines, l. 76-93): the two lists are equal (True); they are the first fill's R-A, R-B, R-C, R-G, R-D,
R-E in that order (True ×6); R1's, R2's, R3's, R5's and R6's old strings once in L-2, R4's 0 times in L-2 and once in the running line
after R1-R3, inside R3's new text; L-2 + R1-R6 in C133's order = L-3 (True); R3's new text with R4 applied occurs once in L-3; 5 token
hunks (11 tokens out, 69 in), R3 and R4 in one; pins.sha1 at 610897dd pins L-3, L-2, the fixes edda8237 and the C133 copy (= C133 at
8f6d03bc) (True ×4). (b) check79.sh from a git archive of 610897dd (docs/si, experiments/si, scripts, notes/L-SI.md),
2026-11-07T14:51:53Z-14:52:24Z, rc 0, «box 79 P-IDEAL-DBL (frozen) checks: PASS»: the pins (sha1sum -c --strict), dblcheck.py (CORPUS
and LOWER), NEG=2, EXTRA, wiring79.py, dead79.py, reentry_levels.py and mkL2.py, each against its committed output, and, new at
610897dd, mkL3.py (cmp against L-3). (c) upd119b.py (r119/upd119.py with its Part C2 replaced by the R118 control as landed and its
Parts D-E by the R119 build on L-3): the controls R97-R116 rebuilt from their lines and compared with GAPS l. 11 at 478d0bd9, True ×20;
the R117 control (run117() on R117's L-4, filled with its GAPS l. 11 stamp 2026-11-07 10:30 d7091311) equal to its GAPS segment, to
R117-draft.md's UPDATE line and r117b/upd117L4.txt with the same fill, unfilled sha1 = C130 §5's b4d74e09… (True ×4); the R118 control
(run118() on R118's L-4, filled with its GAPS l. 11 stamp 2026-11-07 14:48 af92b846) equal to its GAPS segment, to R118-draft.md's
UPDATE line and r118b/upd118L4.txt with the same fill, unfilled sha1 = C132 §5's d4acaeef… (True ×4); all controls True ×22; the last
UPDATE on l. 11 is R118's (True). R119 rebuilt on L-3 by R116's procedure, unchanged (C133 E-3): sha1
074e3c05060c7adcd7b20e5560674bdf12d8b2fa (no newline, unfilled), 6,199 bytes, 100 «(» / 100 «)», 0 "|", one each of «<DATE>», «<HH:MM>»,
«<checker>»; = the direct build (True); = the first fill's upd119prop.txt (f65f4329…, L-2 with R-A..R-E by the same procedure) with R4's
sentence inserted after «(MP-LIN about max-plus recursions)» (True); the filled UPDATE inserted after R118's, before the row's closing «
|», keeps 76 "|" on l. 11, R119's UPDATE last (True). (d) prem119b.py: RESULTS at 478d0bd9; L-3's premise labels (RESULTS R104, R105,
R110, R113, R116) each name a landed «### R» entry; the 18 premise quote parts of packet §0 and fixes F-1 found, 0 not found. (e)
chk119b.py (title, block, UPDATE, quote sweep, stale grep), lp119b.py (line-precise quotes), sim119b.py (landing simulation), rec119b.py
(first-fill record unchanged), wd119b.py (word diff): Addendum 2.
C133's E-items, resolved in L-3 (string checks by script on L-3, l3rel119.py and chk119b.py): E-1 (G-L, the heading label; the C123 E-1
class) by R1 = R-A: «R1xx» 0 times and «[» 0 times in L-3, which starts «In the IDEAL model of RESULTS R104». E-2 (G-1, source note; the
C122 E-3 class) by R2 = R-B: « (P-IDEAL-DBL, docs/si/P-IDEAL-DBL.md with its fixes entry 1, docs/si/P-IDEAL-DBL-fixes.md; L-SI
successors 41-42)»; «which carries every proof» 0 times in L-3. E-3 (G-U, scope tail; C133's ruling) by R3 = R-C: «(2026-11-07) — each
statement is about the step sequence of R104's IDEAL model (MP-LIN about max-plus recursions);» … «G-N5-TIME stays OPEN; not M3, not a
step-4 pass, not a TARGET.md claim (DATA,»; L-3 has R116's shape, and R116's UPDATE procedure runs on it unchanged. E-4 (G-9 (i),
PASS-FREEZE's range) by R5 = R-D: «for 1 ≤ l ≤ d − 2, if the pair l + 1 never moves and starts split, then F(l + 1) = F(l)». E-5 (G-9
(ii), FUEL-EXACT's class) by R6 = R-E: «on 𝓛^R_d, E_l is the set of steps at which some mover of the old chain». E-6 (G-7, L41; Lead
ruling) by R4 = R-G: «DBL-EQ (b)'s window count uses one referee-originated step (REFEREE's DB-3, fixes entry 1 F-3, found independently
by REFEREE-2)», inside R3's tail. Each new string once in L-3 (R3's as edited by R4). The first fill's optional R-F is not taken (C133
N-1), and R-B′ is not needed.
Changes at this fill, and nothing else: line 1 (the header); this section; the title (L-3); in the entry: Object (610897dd; two fixes
entries; L-3 the line of record, its line history, the L-3 verdicts of both referees), Claims signed (the L-3 round), The RESULTS line
(L-3; what R1-R6 change), L41 and L43 (the Lead's L41 ruling, R4), Fixes (header, the entry-2 bullet with the E-item resolution, the
closing bullet), Referee strengthening (iii) (new), Honest limits (viii) (new), Data (610897dd; mkL3.py in check79.sh; the re-run at
this fill and C133's), Signatures (REFEREE §C add. 1, REFEREE-2 Addendum 2, the lane commit 610897dd), INDEPENDENCE (the L-3 wording and
round), TARGET.md diff (L-3's scope tail); the GAPS preamble (R118's UPDATE now the last on l. 11; built from L-3) and the UPDATE
(rebuilt from L-3); Addendum 2 (new). The FIRST FILL text below (from "FIRST FILL (this text)" to (14)) and the Addendum (1)-(10) are
kept byte-unchanged as the record of draft 3fb40db1 on L-2 (rec119b.py): where they call L-2 the title line or the current line, raise
G-L, G-1, G-U, G-9 (i)-(ii), G-7, G-0 or G-P, propose R-A..R-G or R-B′, describe R117 as the last landed entry or R118 as unlanded, or
give the first fill's line numbers, counts, placement and UPDATE sha1 (cec3db26…), they describe draft 3fb40db1 at 10:56Z; C133 ruled
G-L, G-1, G-U, G-9 (i), G-9 (ii) and G-7 as E-1..E-6 (fixed by R1, R2, R3, R5, R6, R4), did not take R-F, ruled the UPDATE procedure
(G-U: R116's, unchanged) and set the placement after R118 (G-P); the entry block now follows L-3.
FIRST FILL (this text). Read at the origin heads fetched at 2026-11-07T10:35Z (git fetch of claude/l-si, claude/referee, claude/referee-2,
claude/checker, claude/vibrant-johnson-nxvvxo; I merged, committed and pushed nothing and edited docs/agents/R119-draft.md only):
l-si 0ea6959f (0ea6959fd2096c8cac7497a3cbfb10c9268673fb, 2026-11-07T09:21:52Z, «L-SI 42: P-IDEAL-DBL fix round 1: fixes entry 1 …»; the
branch head; the packet, L-1, L-2, the fixes, experiments/si/box79/, box76/ and check.sh are those of 0ea6959f), referee 34589c09
(2026-11-07T10:08:01Z, REFEREE successor 26's §C of docs/referee/R-P-IDEAL-DBL.md; the file 224 lines, 18,252 bytes, sha1
db32cb4d75708a6e74bd00cf3755f56a13c07364; its l. 1-178 = d7885be4's file, by script), referee-2 58595823 (the branch head; its
docs/referee-2/R2-P-IDEAL-DBL.md is 2b425bb6's report, 136 lines, 13,907 bytes, sha1 72a1986e66c039086cb9b362810996c396f5de18, unchanged
at 7891ba32 and 58595823), checker d7091311 (docs/checker/ ends at C131.md; C132 = R118, not yet written). REFEREE-2's Addendum 1 was
not on origin at that fetch (three fetches 10:35Z-10:36Z: git cat-file «Not a valid object name» for 30615935 and 1b9e3ea5); a re-fetch
at 2026-11-07T10:52Z found referee-2 1b9e3ea5 (1b9e3ea50a48dc45fd258e6ffcd6ffbc4ab3f768, 10:07:40Z, «REFEREE-2 successor 30: DBL Add. 1
stamp 10:0xZ (date -u)»; Addendum 1 itself 30615935, 10:07:30Z; git diff 30615935 1b9e3ea5: the heading stamp «10:1xZ» → «10:0xZ» and
one notebook line); docs/referee-2/R2-P-IDEAL-DBL.md at 1b9e3ea5: 166 lines, 17,333 bytes, sha1 f9f5952e303baaf52702c14716b522e1985a6449,
its l. 1-136 = 2b425bb6's file (by script). This fill quotes REFEREE-2 at 1b9e3ea5 (G-R2). l-si, referee and checker unchanged at the
re-fetch. 0ea6959f, 34589c09, 30615935 and 1b9e3ea5 are NOT ancestors of the local trunk (git merge-base --is-ancestor); d7885be4 and
2b425bb6 are. The Lead merges and pushes before landing.
Local trunk: HEAD ac1bc37c (2026-11-07T10:30:26Z, «Lead: land R117 REACH3 (P-N5-REACH, line L-4; CHECKER C130 Add. 1 d7091311 PASS)»;
being pushed); RESULTS sha1 68d3d046276ba4168ce99ec8b00118775261b12a, 14,249 lines; «### R116» l. 13072, «### R117» l. 13362, «**Erratum
E-1**» l. 13607; GAPS sha1 36179c4799317e26953886e53a8fcdec2c306e58, 23 lines, l. 11 76 "|", 52 «UPDATE 2026-», the last one R117's
«UPDATE 2026-11-07 10:30Z: RESULTS R117 (P-N5-REACH; CHECKER C130 d7091311)». R118 (P-N5-XICYC) is NOT landed (first fill 217ac0cc at
CHECKER C132, an L-4 round to come). R119 goes after the last landed R-entry (G-P).
Sources read: the packet docs/si/P-IDEAL-DBL.md (frozen f5263d5a, 2026-11-07T08:17:54Z, sha1 3573e93bdbd18e824fb6a9d973eb9277d6d6d488,
199 lines, 21,583 bytes; read in full; draft 2c396f6f differs, its sha1 68a9df6e…); line L-1 (93177184…, 3,425 bytes; committed at
2c396f6f, unchanged at the freeze and at 0ea6959f); fixes entry 1 and line L-2 (0ea6959f, both files' only commit: docs/si/P-IDEAL-DBL-fixes.md
67 lines, 8,797 bytes, sha1 172bfa2faf343b41075fdea2802539fbb782c9c3, read in full; L-2 sha1 1b3dc82544adfaf2cdea0deffbcbd052db9cd371,
5,810 bytes); experiments/si/box79/ at 0ea6959f: dblcheck.py (143 lines), dblcheck.out, dblcheck_neg2.out, extra79.out, dead79.py (49),
dead79.out, reentry_levels.py (45), reentry_levels.out (38), wiring79.py, mkfix1.py, mkL2.py, check79.sh (28), pins.sha1 (23 pins),
ref_d7885be4.md, ref2_7891ba32.md, every one read (wiring79.out and tower_H5.out listed); experiments/si/box76/tw.py (load_corpus, is_lr,
the NEG switch), box76/pins.sha1 and experiments/si/check.sh l. 1236-1251; REFEREE successor 26's docs/referee/R-P-IDEAL-DBL.md (report
d7885be4, §C 34589c09; its scratch tools listed, not re-run); REFEREE-2 successor 30's docs/referee-2/R2-P-IDEAL-DBL.md (report 2b425bb6;
its tools listed, not re-run); RESULTS R104 (title l. 9864), R105 (l. 10155), R110 (l. 11323), R113 (l. 12152 and its body (g) l.
12245-12247), R116 (l. 13072), the Errata and Note E-3; GAPS l. 11; DECISIONS-INDEX (L41, L43, L44, L50) and DECISIONS L41 (l. 355-358);
docs/agents/LEAD-STATE.md l. 2455-2486; notes/L-SI.md at 0ea6959f (BOX 79 l. 36-47, «Sources opened» l. 164); docs/checker/C122, C123,
C125-C131 and notes/CHECKER.md on claude/checker; docs/agents/R118-draft.md (the model, fresh first fill) and R116-draft.md (P-IDEAL-MOVES,
the nearest IDEAL-model entry).
Checks run at this fill (scratch /tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad/r119;
nothing written into the repository but this file). (a) rel119.py: the L-1 → L-2 byte and token tests, shapes, objects at every commit,
the referees' texts against L-2. (b) check79.sh from a git archive of 0ea6959f (docs/si, experiments/si, scripts, notes/L-SI.md),
2026-11-07T10:36:24Z-10:36:54Z, rc 0, «box 79 P-IDEAL-DBL (frozen) checks: PASS»: it re-ran dblcheck.py (CORPUS and LOWER), NEG=2
dblcheck.py, dblcheck.py on the four EXTRA genomes, wiring79.py, dead79.py, reentry_levels.py and mkL2.py, each output byte-equal to its
committed file (diff -q / cmp under set -e), and sha1sum -c --strict of pins.sha1. (c) static119.py, my own code (no lane code): 𝓛^R
shape, Ξ-acyclicity, stored starts, byte copies against l-red 36d340c7 and l-lower 4d747490, the Ξ-target and descendant facts of the
four DEAD instances, DEAD-REENTRY's level sets for every l in 0, …, d − 1 under readings A and B, and the CORPUS (208 entries, blob re-hash
and l-new 9995f5a2 blobs, run count). (d) prem119.py, the premise quotes and labels. (e) upd119.py, the UPDATE build with the controls
R97-R117 (R117 landed) and an R118 control (not landed). (f) chk119.py (title, block, UPDATE, quote sweep, stale grep), lp119.py
(line-precise quotes) and sim119.py (landing simulation): Addendum.
LESSONS APPLIED (R118's list, plus C130 and C131). C113 E-1: the title is L-2 verbatim, no insertion and no stripping (G-L shows what
that does here). C114 Add. 1 E-1: the UPDATE head carries «<DATE>». C115 E-1: the premise route is checked against what RESULTS records
(G-4). C116 G-1, C118-C130 §4: the UPDATE rule of the precedent with the nearest line shape, flagged where no precedent has this shape
(G-U). C116 G-2: name clashes (G-6). C117 E-1 / E-2: no sentence wider than signed (G-9 (i), (ii)). C118 E-1 / C113 E-2: no status
sentence that goes stale at landing (G-R2: REFEREE-2's L-2 verdict quoted from origin only). C118 §3 / Erratum E-2: every definition of
L-2 diffed against the packet and its fixes (G-2). C120 §5 / C121 §5 / C122 E-2 / C124 E-1 / C125 E-1 / C127 E-1 / C128 E-1..E-5 / C129
E-1 / C130 E-1..E-3: EVERY clause of L-2 tested against the code of the counter it names, for unit, set and the statement's scope, and
every signed clause matched to a count or a no-DATA entry, including «so …» consequences (G-9). C129 E-2 / C130 E-4: every DEAD instance
reproducible from the line (G-D). C122 G-0: parentheses balanced (G-1). C122 E-3: the source note names every proof-carrying file (G-1:
FLAG). C123 E-1: no lane label, packet name or second ledger label in the title before the claims (G-L: FLAG). C119 E-1: every «referee X
did Y» checked against that referee's file. C130 G-P: the UPDATE builder carries a control for every UPDATE that lands before this one
(R97-R117 landed; R118 by an unfilled control).
FLAGS FIRST (G-L, G-1, G-U, G-9 (i)-(ii) are for CHECKER or the Lead; G-7 and G-P are the Lead's; exact replacements R-A, R-B (or
R-B′), R-C, R-D, R-E and optional R-F, R-G, each old string once in L-2, by script; L-2 with R-A, R-D, R-E, R-C, R-B: sha1
ba7ffc523427d98020b1715a835d78b60cc5ce31 with its newline, 6,037 bytes, 99 «(» / 99 «)», depth never negative, 0 "|", one « — »; its UPDATE
by R116's procedure unchanged (sentinel_build111 with R111's DEAD-clause step) f65f43290e820d263234e98abddf014a1953df04, 6,069 bytes;
R-B′, R-F, R-G not built), then the notes and CLEAN items, then (0)-(14).
- G-L, THE HEADING LABEL (FLAG; the C123 E-1 class; CHECKER FAIL as it stands). L-2 begins «R1xx [refereed-only] In the IDEAL model of
  RESULTS R104», so the title built by the C113 rule reads "### R119 [refereed-only] R1xx [refereed-only] In the IDEAL model …": a
  placeholder label and a second ledger tag inside the heading, and the same pair after «LANDED: » in the UPDATE (upd119.out: «R1xx» 1,
  «[refereed-only]» 2 in the UPDATE). C123 l. 83-86: «L-2 starts «P-TR3 [lane: EXACT-SAT + CERT] In the IDEAL model», so the RESULTS
  heading would read» …; «every landed title starts with the statement»; «A second bracket right after the RESULTS label reads as a second
  ledger label». L-1 has the same prefix (rel119.py: «[» once in L-1 and in L-2); no referee mentions it (REFEREE «R1xx» 0 times, REFEREE-2
  0 times). Every landed L-SI line starts with its statement (R115 «In the IDEAL model of RESULTS R104 (premise: …»). Proposed R-A (the
  C123 E-1 remedy, one deletion): "R1xx [refereed-only] In the IDEAL model of RESULTS R104" → "In the IDEAL model of RESULTS R104" (old
  string once in L-2 and once in the UPDATE; the deleted prefix «R1xx [refereed-only] » is 21 characters, at the start of the line).
- G-1, SOURCE NOTE (FLAG; the C122 E-3 class). L-2's last parenthesis is «(2026-11-07; source: packet P-IDEAL-DBL, docs/si/P-IDEAL-DBL.md,
  which carries every proof)». Fixes entry 1 carries text the line rests on: F-2 fixes the READING of DEAD-REENTRY (the line's killed
  statement is F-2's «the strict Ξ-descendants of the fuel targets U_l lie at levels > l», not the packet's «The movers on the chains of the
  fuel targets U_l lie at levels > l»; REFEREE l. 18 «read literally the statement is false almost trivially») and gives its measured level
  sets; F-3 adds a proof step to DBL-EQ (iv) («Add to (iv): at a doubling level, Φ(s_0) = 2 while Φ(s_(t−1)) = 0 at every l-b-step t (DBL-EQ
  (a)); so step 1 is not an l-b-step»); F-1 replaces a premise quote. So «which carries every proof» is no longer exact, and against the
  packet alone the DEAD-REENTRY clause is not the packet's statement. C122 l. 85-88 («Two clauses of the line are proved only in the fixes
  file» … «R109's precedent names its fixes entry in the source note»); R113-R116 name theirs («with its fixes entry 1,
  docs/si/P-IDEAL-IM-fixes.md», R115). The note also names no lane (R105-R117 do: «L-SI successors 39-40», R115). Proposed R-B (with R-C,
  G-U): " (2026-11-07; source: packet P-IDEAL-DBL, docs/si/P-IDEAL-DBL.md, which carries every proof)" → " (P-IDEAL-DBL,
  docs/si/P-IDEAL-DBL.md with its fixes entry 1, docs/si/P-IDEAL-DBL-fixes.md; L-SI successors 41-42)"; R-B′ (if R-C is not taken): the
  same old string → " (2026-11-07; source: packet P-IDEAL-DBL, docs/si/P-IDEAL-DBL.md with its fixes entry 1, docs/si/P-IDEAL-DBL-fixes.md;
  L-SI successors 41-42)". Both old strings once in L-2 and once in the UPDATE (script).
  Shape otherwise CLEAN: L-2 is one line, 5,671 characters, 5,810 bytes with its newline, 1,035 whitespace tokens, 97 «(» / 97 «)», depth
  never negative, final depth 0, 0 "|", five guillemet pairs (the five killed statements: LEV-ADD, DAG-ADD, DBLGAP, DECAY, RE-ENTRY), «2026»
  once (in the source parenthesis), 0 « — », one «[» (the G-L prefix).
- G-U, THE LINE SHAPE AND THE UPDATE PROCEDURE (FLAG; no precedent has this shape; CHECKER rules). Every landed line R90-R117 has " (date)
  — " followed by its scope words; every one carries «not a TARGET.md claim», and R96-R101 and R103-R117 also «G-N5-TIME stays OPEN» (my
  script on the titles at ac1bc37c: " — " at least once, one "(2026-MM-DD)" date parenthesis, «not a TARGET.md claim» once in each). L-2 has NO « — », NO scope sentence
  (its only scope words «FUEL-NEED and FUEL (i), which use L-LOWER's unrefereed FEEDBACK (b), are not stated; no statement bounds T
  polynomially» sit at the end of its DATA parenthesis), «G-N5-TIME» 0 times, «TARGET» 0 times, and its date inside the source parenthesis.
  The packet says what the scope tail would say (l. 6-7 «Not a TARGET.md claim. Every statement is about the IDEAL model of RESULTS R104's
  definition only. No statement bounds T polynomially; G-N5-TIME stays OPEN.»; §7 «Each is about the step sequence of R104's IDEAL model
  (MP-LIN about max-plus recursions).»); both referees say it (REFEREE l. 167-168, REFEREE-2 l. 24 «No statement bounds T; G-N5-TIME stays
  OPEN.»). UPDATE: sentinel_build111 fails on L-2 (no " (date) — "), build() on the full line fails (upd119.out); upd119.py therefore runs
  build() of upd100L3.py unchanged for the label move on the claim body with sentinel_build111's sentinel tail (the R105-R118 route), start
  «changes its value: », with R111's / R116's DEAD-clause step (the unlabelled «; and four statements are false (DEAD, instances
  machine-replayed): …» cut before the build and put back behind (TOWER-NEED)), then «: » + the DATA parenthesis opened («DATA, …») + the
  source parenthesis kept verbatim with its date + «. G-N5-TIME stays open.». Cross-check: a direct build by string operations is equal
  (True). The «R1xx [refereed-only] » prefix is carried (G-L). Proposed R-C (the precedent shape; CHECKER's or the Lead's call): " (DATA,
  experiments/si/box79/dblcheck.py, CORPUS = " → " (2026-11-07) — each statement is about the step sequence of R104's IDEAL model (MP-LIN
  about max-plus recursions); G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim (DATA, experiments/si/box79/dblcheck.py,
  CORPUS = " (old string once in L-2); with R-C and R-B the line has R116's shape exactly, and R116's procedure builds its UPDATE unchanged
  (f65f4329…, «R1xx» 0, «2026-11-07» 0; upd119prop.txt). The scope words of R-C are the packet's (§7) and the precedent's.
- G-9, DATA, CLAUSE BY CLAUSE (the C120-C130 rule: unit, set and the statement's scope of every count, against the code of the counter
  the line names; every signed clause matched to a count or a no-DATA entry). Every figure of L-2's DATA equals dblcheck.out /
  dblcheck_neg2.out, reproduced byte for byte by check79.sh at this fill ((b) above; dblcheck.py RE-RUN, about 30 s for the whole block).
  The counter code is dblcheck.py l. 28-122 (run_checks) on box76/tw.py's Sim and analyse. Clause by clause:
  - (i) FLAG (the C117 E-1 «wider than signed» class, with the C124 E-1 set class). PASS-FREEZE in the line, «if the pair l + 1 never moves
    and starts split, then F(l + 1) = F(l)», carries NO range; read with the line's definitions it covers every l with a pair l + 1, i.e.
    0 ≤ l ≤ d − 2. The signed packet statement has «Hypotheses: G ∈ 𝓛^R_d, 1 ≤ l ≤ d − 2, any run.» (packet l. 95). REFEREE notes it both
    times without a fix: «The proof also works at l = 0. The line states no range.» (l. 76) and «PASS-FREEZE states no range; it holds for 0
    ≤ l ≤ d − 2.» (l. 133); REFEREE-2 signs the packet's statement (l. 16) and finds the L-1 clause equal to it (l. 117-118). The counter PF
    (dblcheck.py l. 65 «for l in range(1, d)», l. 110 «if l <= d - 2:») counts l = 1, …, d − 2 only, while the DATA unit «(run, level)»
    names no range (DBL-EQ's does: «(run, level ≥ 1)»). Proposed R-D (the statement narrowed to the signed range, which also fixes the
    DATA scope): "if the pair l + 1 never moves and starts split, then F(l + 1) = F(l)" → "for 1 ≤ l ≤ d − 2, if the pair l + 1 never moves
    and starts split, then F(l + 1) = F(l)". (Alternative, not built: keep the statement, have REFEREE-2 sign l = 0, and write «(run, level
    ≥ 1)» in the DATA.)
  - (ii) FLAG (the same class). FUEL-EXACT in the line, «E_l is the set of steps at which some mover of the old chain of some y ∈ U_l
    moves», carries no class; the line's global setting is «on acyclic Ξ-graphs», and its U_l / E_l definitions are not tied to 𝓛^R_d, so
    the clause reads for every acyclic genome. The signed statement is «Corollary FUEL-EXACT (= FUEL (ii) of the source note). Hypotheses: G
    ∈ 𝓛^R_d, Ξ-acyclic, 0 ≤ l ≤ d − 1, any run.» (packet l. 115). Its proof (MONO + HIT + union) uses no 𝓛^R_d fact, and REFEREE-2 says so
    (l. 123 «FUEL-EXACT holds for any set U, so this does not affect a verdict.»), but neither referee signs it outside 𝓛^R_d, and the DATA
    head names only «HIT and ALT-MIN» as «stated at any degree». Proposed R-E: "E_l is the set of steps at which some mover of the old
    chain" → "on 𝓛^R_d, E_l is the set of steps at which some mover of the old chain". (Alternative, not built: both referees sign the
    any-degree form, and the DATA head adds FUEL-EXACT to «so HIT and ALT-MIN, stated at any degree, are tested only there».)
  - WINDOW-ONCE «each member of the pair l moves at most once in every l-window»: «0 violations on 577,908 / 1,736 (run, level, window,
    member)». Counter WO (l. 65-78): for l = 1, …, d − 1, the l-windows W (l. 68-72: maximal runs of steps with no flip of the pair l − 1
    after the first), per member, «nm > 1». Unit and set MATCH; l ≥ 1 is implied by «l-window» (l-b-steps are flips of the pair l − 1).
  - DBL-EQ (a) «level l is doubling iff Φ_l(s_0) = 2, Φ_l(s_T) = 0, Φ_l = 0 before every l-b-step, no step moves both members and the flips
    of the pair l are exactly its moving steps»: «0 on 225,647 / 72 (run, level ≥ 1), both directions, with 4,534 / 12 doubling (run,
    level)». Counter DBLa (l. 79-87): cond = the five conditions in that order, dbl = [F(l) = 2F(l − 1) + 2], a violation iff dbl ≠ cond
    (both directions). MATCH.
  - DBL-EQ (b) «each member moves exactly once in every l-window (so F(l − 1) + 1 times)»: «0 on 11,052 / 176 (run, doubling level, window,
    member)». Counter DBLb (l. 90-93), «!= 1». MATCH. NOTE: «(so F(l − 1) + 1 times)» is not counted directly; the windows of l. 68-72 start
    at step 1, so their number is F(l − 1) + 1 exactly when step 1 is not an l-b-step, which DBLa = 0 forces at a doubling level (cond
    needs Φ(0) = 2 and Φ = 0 before every l-b-step); F-3's proof step says the same. Covered by DBLa and DBLb together.
  - DBL-EQ (c) «γ_l(0) = γ_l(1) and the first mover of every window is 2l iff γ_l is false»: «0 on every doubling (run, level)». Counter DBLc
    (l. 94-100), per doubling (run, level), γ from the gate indices («gam = [G["gate"][p][k] < G["gate"][q][k] for k in range(2)]»). MATCH
    (the count is DBL-EQ (a)'s 4,534 / 12).
  - PASS-FREEZE: (i).
  - HIT «at any degree, cv(y) rises at step t iff some mover of y's old chain moves at t, so R(y) ≥ moves(y)»: «0 on 1,298,948 / 5,216 (run,
    mover, step)». Counter HIT (l. 40-46): every mover x and step t, rise ≠ hit with chain(S[t − 1], x) (l. 36-39; the chain starts at x
    itself). MATCH. NOTE: «so R(y) ≥ moves(y)» has no counter of its own; it follows from the counted equivalence because y is on its own
    old chain (l. 37 «out = [y]»), so every step moving y is a counted rise. Covered (no separate DATA needed; REFEREE-2 counts it in its
    own r2dbl.py, l. 65-66, referee data). The «at any degree» scope: the DATA head says so («so HIT and ALT-MIN, stated at any degree, are
    tested only there»).
  - FUEL-EXACT: (ii) for the scope; the count «0 on 288,870 / 81 (run, level)»: counter FU2 (l. 115-122), l = 0, …, d − 1, U = the
    Ξ-targets y ≥ 0 of options (x, k) with lev(x) ≤ l and lev(y) > lev(x) (the line's U_l, N-2's wording), E = the steps where cv of
    some y ∈ U changes, compared with the old-chain move set. Unit and set MATCH.
  - ALT-MIN «the changes of π(x) to k number at most R_k(x), PF_x ≤ 2 min(R_0(x), R_1(x)) + 1, moves(x) ≤ 2 + 2 min(R_0(x), R_1(x)), and
    R_k(x) is R of the Ξ-target of (x, k) (0 if X)»: «0 on 577,740 / 162 (run, mover), (a) and (d) counted per (run, mover, k)». Counters
    ALTa, ALTd (per k, l. 54-56), ALTb, ALTc (l. 57), the unit «ALT units (run, mover)» (l. 53). MATCH (every mover of 𝓛^R_d has degree 2).
  - TOWER-NEED «each member x moves f + 1 times, P(x) ≥ f + 2, and for f ≥ 2 both Ξ-targets of x are movers with R ≥ (f − 1)/2»:
    «TOWER-NEED's bounds on P and R 0 on 9,068 / 24 (run, doubling level, member), its moves clause through DBL-EQ (b)». Counter TN (l.
    101-109): P(x) by the path recursion (l. 60-64, P(X) = 1), «2 * R[y] < f - 1» and «y < 0» for f ≥ 2. MATCH; the moves clause is DBLb's
    (above), as the line says.
  - Controls: «ALT-MIN's bounds (b) and (c) minus 1 fail on 112,372 / 43 and 7,085 / 13 (run, mover)»: ALTb_T «PF > 2 * m», ALTc_T «mv[x]
    > 1 + 2 * m» (l. 58). MATCH. «with the key-least option taken regardless of availability HIT fails on 238,546 CORPUS (run, mover,
    step)»: tw.py l. 9 «2 = key-least option ignoring availability», dblcheck_neg2.out «CORPUS violations: WO 0 HIT 238546». NOTE (as
    REFEREE l. 158-159 «The NEG=2 HIT count 238,546 is over the NEG=2 run's own 574,938 units.»): the NEG=2 runs are different runs of the
    same genomes and starts (62,846 steps), so 238,546 is out of 574,938, not out of 1,298,948; the line gives no denominator. Unit MATCH.
  - No-DATA list «MP-LIN, the sufficient condition of PASS-FREEZE and DEAD-REENTRY (static Ξ-graph; its level sets measured by
    experiments/si/box79/reentry_levels.py): no separate DATA; the other three DEAD instances re-run by experiments/si/box79/dead79.py».
    MP-LIN: algebra, true. DEAD-REENTRY: static, its sets are the clause's own (G-D). NOTE: PASS-FREEZE's sufficient condition is not
    stated in the line (L-2's PASS-FREEZE clause has no «Sufficient for …» part), so this no-DATA item names a statement the line does not
    make; harmless, and REFEREE accepted the widening («No counter tests PASS-FREEZE's sufficient condition.», l. 196).
  - CORPUS and LOWER: «CORPUS = the 63,223 runs (140,395 steps) of the 208 𝓛^R_d genomes of the frozen P-IDEAL-MOVES corpus (l-new
    9995f5a2; every start for N ≤ 10, the stored start otherwise)»: dblcheck.py l. 130-131 («if G["N"] <= 10 else [tuple(G["start"])]»);
    my static119.py: 208 entries, 208 blobs re-hash, 208 equal to «git rev-parse 9995f5a2:<path>», 208 𝓛^R, 208 Ξ-acyclic, 193 with N ≤ 10,
    Σ 2^N + 15 = 63,223 runs (True). «LOWER = the 9 runs of L-LOWER 3's kill genomes from their stored starts»: l. 133, the 9 files of
    box76/inst/lower/, each a byte copy of l-lower 4d747490 experiments/lower/l3/kill/ (static119.py, True), all 𝓛^R and Ξ-acyclic. «every
    genome of degree 2 and width 2»: true of 𝓛^R_d by definition (R110). MATCH.
  - SCOPE (NOTE): HIT and ALT-MIN are stated at any degree, tested on degree-2, width-2 ladders only (the line says so); every other
    statement is on 𝓛^R_d (with R-D, R-E). FUEL-NEED and FUEL (i) are «not stated» (true: neither occurs in L-2 as a claim; §5 is
    CONDITIONAL, REFEREE l. 16 «not reviewed for signature», REFEREE-2 l. 23 «Not signed»).
- G-D, THE DEAD INSTANCES: CLEAN (the C129 E-2 / C130 E-4 check). Each killed statement is quoted in the line, and each instance is
  named by path with its start: (1) LEV-ADD / DAG-ADD: experiments/si/box76/inst/dense_d5_l3_H10.json (sha1 a449d771…, byte copy of
  l-red 36d340c7 experiments/red/r214/out/dense_d5_l3_H10.json, True), 𝓛^R_5, start 1100110110 (= its stored start; the line says «start»):
  mover 6 (level 3) is the Ξ-target of option (1, 1), its strict Ξ-descendants are {0, 2, 3, 4, 5, 7, 8, 9} (my static119.py; = REFEREE l.
  106 and REFEREE-2 l. 76); dead79.py D1 asserts T 10, moves(6) 10, max moves over movers 0-5 and over those descendants 4 (re-run (b)).
  10 > c + 4 iff c ≤ 5 for integer c. (2) DBLGAP: experiments/si/box76/inst/lower/REC_d10_tower_mu30.json (cc94dc9c…, byte copy of
  l-lower 4d747490, True), 𝓛^R_10, stored start 00111111010010111010 (static119.py: equal to the line's): dead79.py D2 asserts T 35, F(0..3)
  = 2, 6, 14, 30. (3) DECAY: experiments/si/box76/inst/passfreeze77_d5.json (56436bc0…, pinned in box76/pins.sha1, built by
  box76/append77.py; packet l. 156-160), 𝓛^R_5, stored start 1101111101 (= the line's): dead79.py D3 asserts T 10, F = [2, 2, 2, 6, 6],
  movers 8, 9 move 0 times, no upward option at level 4 (both options of 8 and 9 have Ξ-target X, static119.py), N 10. (4) RE-ENTRY
  (static): my own code reproduces the line's sets: REC_d10_tower_mu30 reading A fails at l = 1, …, 9, reading B at l = 1, …, 8;
  KILL_M2D_d6_mu13 (5301c716…, byte copy of l-lower 4d747490, True) reading A at l = 1, …, 5, reading B at 1, 2, 3; both hold at l = 0. On
  the line's range l ∈ 0, …, d − 2 reading A gives exactly «false for l = 1, …, 8» and «for l = 1, …, 4», «true for l = 0 on both» (=
  reentry_levels.out, = REFEREE §C l. 200-205, = REFEREE-2 Add. 1 l. 149-150 and r2reentry.out at 1b9e3ea5). Witnesses, by my code: (1, 0) →
  11 (level 0 → 5) and 11's option 0 → 3 (level 1); 5 is the Ξ-target of (1, 0) and (2, 1) (levels 0, 1) and 5's option 0 → 3 (level 1); so
  «mover 11 of level 5 is the Ξ-target of mover 1's option 0» and «mover 5 of level 2 is the Ξ-target of an option of mover 2 of level 1»
  are exact, and each witness works for every l ≥ 1 (REFEREE l. 207-208). NOTE: reading A also fails at l = d − 1 (9 and 5; REFEREE l.
  206 «Note, no fix»); the line's «measured for every l in 0, …, d − 2» is exact for its stated range. No Dead-ends row is drafted: the five
  killed statements are lane statements killed inside the line (the C118 §5 / C129 / C130 precedent). L43 does not bear (not asymptotic;
  killed by instances, replayed by both referees with their own simulators).
- G-2, DEFINITIONS AND STATEMENTS DIFFED (my own diff of L-2 against packet §0-§6 with fixes entry 1). Premises = §0 with F-1 and F-5
  (N-1: F0 dropped). Notation = §0 l. 44-52 (T, Mv_t, moves, cv, R, R_k, old chain, P, F(l), l-b-step, Φ_l, l-window, doubling, U_l with
  N-2's wording, E_l). MP-LIN = §1 without «C depends on A, b and x_0 but not on j» and without a's role. WINDOW-ONCE = §2 l. 65-66 without
  «c_l(s_t) is the same for every t ∈ ω» and «to that option» (narrower). DBL-EQ = §2 (a)-(c). PASS-FREEZE = §2 l. 95-97 without its
  range (G-9 (i)) and without its sufficient condition. HIT = §3 l. 107-108. FUEL-EXACT = §3 l. 115-116 set form, without 𝓛^R_d (G-9
  (ii)) and without «|E_l| ≤ Σ_(y ∈ U_l) R(y)». ALT-MIN = §4 (a)-(d) without (d)'s «so if an option of x has Ξ-target X, moves(x) ≤ 2».
  TOWER-NEED = §4 l. 130-131. DEAD = §6 with F-2's reading of RE-ENTRY; LEV-ADD in the line drops «a Ξ-target» (a stronger statement,
  killed by the same instance: REFEREE l. 132-133).
  (i) NOTE. π(x), PF_x (R116's notation, through the AND-GATE premise), c_l(s), γ_l(j) and «flip» (R113's, through ALIGN) and the
    constant C of MP-LIN are not defined in the line. The C124 G-9 (vii) ruling covers definitions not named; the premise parenthesis names
    R113 and R116.
  (ii) NOTE. «RESULTS R116's AND-GATE (a)-(c)»: (a)-(c) is the packet's partition of the landed clause (packet l. 39-41), not a RESULTS
    label («AND-GATE (a)» 0 times in RESULTS); both referees found the partition faithful (REFEREE l. 35-42; REFEREE-2 l. 41-43 «The three
    parts partition the landed clause; nothing is added or strengthened.»). As (a)-(c) is the whole clause, optional R-F: "RESULTS R116's
    AND-GATE (a)-(c))" → "RESULTS R116's AND-GATE)" (old string once in L-2).
  No other sentence of L-2 is wider than the signed statements (C117 E-1 / E-2).
- G-R2, REFEREE-2'S L-2 VERDICT ON ORIGIN (note; resolved during this fill). REFEREE-2's verdict on L-1 is «**MATCHES after W-2 (a)-(d),
  W-3**» (l. 22). Its verdict on L-2, Addendum 1 (30615935 + stamp fix 1b9e3ea5; LEAD-STATE 10:07Z «DBL Addendum 1 30615935 + 1b9e3ea5
  (pushing)»), was not on origin at my first fetch (10:35Z-10:36Z) and is on origin at the re-fetch (10:52Z, head 1b9e3ea5). The body
  quotes it from 1b9e3ea5: l. 142-144 (own byte test bt_l2.py: «L-1 with all seven == L-2 byte for byte»), l. 145-146 «**W-1 closed**»,
  l. 147-155 (DEAD-REENTRY sets by its own code, r2reentry.out, equal to the lane's; «I withdraw «only».»), l. 156-162 (DATA «met in
  substance»), l. 165-166 «Verdict: fixes entry 1 **CORRECT**; W-1, W-2 (a)-(d), W-3 **met**; **L-2 MATCHES** the packet with fixes entry
  1, in bytes and in meaning». No body sentence depends on the earlier absence.
- G-0, THE CHECKER NUMBER. docs/checker/ on claude/checker (d7091311) ends at C131.md; C132 is R118's (first fill 217ac0cc, routed
  10:30Z, not yet written); «C133» occurs 0 times in RESULTS, GAPS, NOW, LEAD-STATE and on claude/checker (by script). This draft uses
  C133 (title fill, UPDATE head, GAPS preamble).
- G-P, PLACEMENT AND NUMBERING (Lead). R117 is landed at the local trunk ac1bc37c (being pushed); R118 is not (C132, an L-4 round to come).
  R119 goes after the last landed R-entry, before «**Erratum E-1**», and its UPDATE after the last UPDATE on GAPS l. 11. Simulated both
  ways (Addendum): directly after R117, and after a stand-in R118 (R118-draft.md's block and UPDATE). NUMBERING NOTE: if R119 lands before
  R118, the RESULTS order would read R117, R119, R118 unless the Lead renumbers; the Lead decides (renumber this entry to R118 and P-N5-XICYC
  to R119, or keep the numbers and accept the order). A renumbering changes the title prefix, the UPDATE head and every «R119» of this
  draft (by script), and the UPDATE builder's controls (the R118 control becomes a landed one or drops out).
- G-4, PREMISE ROUTE (the C115 E-1 class): CLEAN (prem119.py on RESULTS 68d3d046 at ac1bc37c; 18 quote parts of packet §0 and fixes F-1,
  0 not found). Labels in L-2 (by script): «R104» 2, «R105» 2, «R110» 1, «R113» 1, «R116» 1; each exists (### R104 l. 9864, ### R105 l.
  10155, ### R110 l. 11323, ### R113 l. 12152, ### R116 l. 13072); «(ENC)», «(MONO)», «(LOCAL)» in R105's title, «(ALIGN)»,
  «(PATH-RISE)» in R113's, «(AND-GATE)» in R116's, once each; R110's title defines 𝓛^R_d («option k of a mover of level l ≥ 1 W-pointing
  to mover 2(l − 1) + k»). F-1's new quote «(PATH-RISE) at any degree, the current value cv(z) of every mover z rises at most P(z) − 1
  times in a run» is in R113's title (l. 12152), the line of record. NOTE (no verdict changes): the packet's OLD quote «Then the number of
  steps at which cv(z) rises is at most P(z) − 1.» DOES occur in RESULTS once the line break is normalised: R113's body, statement (g), l.
  12246-12247, quoting P-IDEAL-ALIGN l. 142-143, with the scope «[IDEAL-ACYC, any degree, any width; z any mover; any run]» (prem119.py;
  RESULTS at 97d17f63 has the same lines). REFEREE («does not occur in RESULTS.md», l. 44-45) and REFEREE-2 («Those words are not in
  R113.», l. 34) read it as absent; it is a quote of R113's entry body, not of its line. F-1 (quote the line) is the better premise
  either way; DB-Q1 / W-1 stand as fixes, not as findings of a misquote.
- G-7, L41 (Lead ruling) AND L43. The packet's proofs are L-SI successor 41's (packet l. 2-5). Fixes entry 1 adds one proof step, F-3 (DBL-EQ
  (iv): step 1 is not an l-b-step at a doubling level, so the windows are [1, t_1 − 1], …, [t_f, T]), REFEREE's optional DB-3 («DB-3,
  optional: say this in the proof.», l. 68); REFEREE-2 derived the same step independently in its report («under (a), 1 ∉ B (Φ(0) = 2 ≠
  0), so there are exactly F(l − 1) + 1 windows ✓», l. 54-55). The packet's (iv) already states the count («There are F(l − 1) + 1
  windows.», l. 90); F-3 supplies the reason. Whether L41 («referee-originated proofs»; DECISIONS l. 355-358) applies to a one-step
  justification suggested by one referee and found independently by the other is the Lead's ruling (for R118 the Lead ruled that L41
  applies when the lane restates a referee's proof). If it does, optional R-G (with R-C): "; G-N5-TIME stays OPEN; not M3" → "; DBL-EQ
  (b)'s window count uses one referee-originated step (REFEREE's DB-3, fixes entry 1 F-3, found independently by REFEREE-2); G-N5-TIME
  stays OPEN; not M3" (old string in R-C's new text, once). L43: the DEAD items are not asymptotic; they are DEAD by explicit instances.
- G-6, NAMES (by script on RESULTS 68d3d046 / GAPS 36179c47). 0 times in RESULTS and GAPS: «R119», «C133», «P-IDEAL-DBL», «MP-LIN»,
  «WINDOW-ONCE», «DBL-EQ», «PASS-FREEZE», «FUEL-EXACT», «ALT-MIN», «TOWER-NEED», «DEAD-MAXPLUS», «DEAD-DBLGAP», «DEAD-DECAY», «DEAD-REENTRY»,
  «LEV-ADD», «DAG-ADD», «FUEL-NEED», «FEEDBACK», «R1xx»; «HIT» 0 times as a word. Clashes: «R119» is also L-RED's old round label
  (docs/red/R119-mixed-gate.md, «R119 Lemma MG» in notes/L-RED.md), not a RESULTS label; «FUEL (i)» / «FUEL-NEED» occur only in the line's
  «are not stated» phrase, and RESULTS has R98's «FUEL-LEX» and «FUEL-COUNT» (different labels). One body sentence (Honest limits (vi)).
- G-5, ERRATA (note). E-1 (R97-R100 counts), E-2 (R105's binders), Note E-3 (R110): E-2 bears on R105's binders, not on ENC, MONO, LOCAL
  as quoted; none bears on R110's 𝓛^R_d definition, R113's ALIGN / PATH-RISE or R116's AND-GATE.
- G-8, SCOPE AND TARGET (note): see G-U. The line's own scope words «FUEL-NEED and FUEL (i), which use L-LOWER's unrefereed FEEDBACK (b),
  are not stated; no statement bounds T polynomially» are true (packet l. 7, §5, §7); no tower or CANDIDATE claim in the line.
- G-10, LEAD READINGS AND RULINGS. L-2 cites no Lead reading by label («Lead reading» 0, «L4» 0 times, by script). The Lead's rulings of
  this round (LEAD-STATE 09:20Z «DBL fix round routed to L-SI 42 (rulings: W-1 = DB-Q1; DB-L1 New text is base for DATA, W-3 additions
  as no-DATA/pointers; DB-L2 wording, level set MEASURED by script (REFEREE l = 1..4 vs REFEREE-2 N-3 l = 1 only); DB-3 taken).»; fixes l.
  3-4 «Lead 09:20Z», «Lead rulings 1-5»): applied as ruled (rel119.py: fixes NEW for DB-L1 + W-3 = REFEREE's DB-L1 New with exactly the
  W-3 no-DATA widening; DB-L2's wording with the measured sets; F-1 = W-1 = DB-Q1; F-3 = DB-3). Not readings (not in DECISIONS). L41: G-7.
  L44, L50 do not bear.
- G-3, SYMBOL TEST (notes): G-2 (i). t, x, y, k, l, j, f, c bound in their clauses; s_0, s_T, s_(t−1) are run states; λ, A, b, ⊗, ⊕ are
  MP-LIN's own; X is the exit (R104).
- G-11, STALE LANE TEXT (notes). The packet's header «FROZEN 2026-11-07 by L-SI successor 42 after RESULTS R116 … landed (trunk
  97d17f63)» is history. The fixes header «REFEREE-2 30 7891ba32» names REFEREE-2's report by the commit that carried it to origin
  (2b425bb6's file is unchanged at 7891ba32, rel119.py). LEAD-STATE 10:05Z dates the lane's report; the lane commit 0ea6959f is
  09:21:52Z (the lane's «committed during push» slip, same line). notes/L-SI.md l. 8 and l. 62 still call the packet a draft
  («DUTY P-IDEAL-DBL freeze (draft 2c396f6f …)»), as of 0ea6959f.
- G-12, PINS (the C110 F-1 / C116 G-3 class): pins.sha1 (pinned and checked by check79.sh l. 7, «sha1sum -c --quiet --strict») covers the
  packet, L-1, L-2, the fixes, the tools, every frozen output, the four EXTRA genomes and both byte-copied referee reports; the DEAD and
  LOWER instance files and the corpus are pinned in box76/pins.sha1 (l. 14, 18-19, 90-98; run by check76.sh); check79.sh is wired into
  experiments/si/check.sh (l. 1247, «bash box79/check79.sh»), which scripts/verify.sh runs (l. 20, 27). Every command of L-2's DATA is
  re-run by check79.sh (no seeded command outside it). CLEAN.
- G-13, THE REFEREES' ROUNDS: (3), (4).
- G-14, THE FIXES FILE (note). One entry, F-1..F-5, and the seven OLD / NEW pairs of «Line L-2 = L-1 with these replacements» (l. 44-65),
  each old string once in L-1 and each new once in L-2 (rel119.py: L-1 + 7 = L-2, True; REFEREE's own byte test the same, §C l. 187-190).
  Entry 1 carries proof text (F-3) and a statement reading (F-2) (G-1).
- G-N, NOVELTY (note). MP-LIN is the standard growth bound of max-plus recursions by the maximum cycle mean; the packet proves it in full
  and cites no source, and the line makes no literature claim; this entry is not a novelty claim. No source is cited by L-2.
- CLEAN AT L-2 (pre-check against CHECKER's recurring items, by script on 1b3dc825): C106 E-1 (no L-3 exists; L-1 only in the line
  history); C113 E-2 (no trunk statement in the body); C114 Add. 1 E-1 (<DATE>); C115 E-1 (G-4); C116 G-2 (G-6); C122 G-0 (97 / 97, G-1);
  C129 E-2 / C130 E-4 (G-D); «|»: 0 in L-2, 0 in the entry block, 0 in the UPDATE (Addendum). NOT CLEAN: C123 E-1 (G-L), C122 E-3 (G-1),
  C117 E-1 / C124 E-1 (G-9 (i), (ii)), the line shape (G-U).
(0) PLACEMENT. RESULTS at the local trunk: sha1 68d3d046276ba4168ce99ec8b00118775261b12a, 14,249 lines; "### R119" 0 times in RESULTS and
  GAPS. PROPOSED (R102's to R117's layout): insert R119's entry, with one blank line after it, directly before «**Erratum E-1**», after the
  blank line that follows the last landed entry's block (R117's at this fill; R118's if it lands first). Simulation: Addendum.
(1) TITLE. The title is the line file docs/si/P-IDEAL-DBL-line-L2.txt (l-si 0ea6959f, 2026-11-07T09:21:52Z, the file's only commit,
  sha1 1b3dc82544adfaf2cdea0deffbcbd052db9cd371, 5,810 bytes with the newline; byte-equal at the l-si head), verbatim: NOTHING is
  stripped and NOTHING is inserted: "### R119 [refereed-only] ", then the file without its newline, then ", CHECKER PASS
  (docs/checker/C133.md, checker PENDING)" (as R90-R118). Built by script and re-checked after writing (chk119.py): equal. As it stands
  the title carries L-2's «R1xx [refereed-only] » prefix (G-L).
(2) LINE HISTORY: two lines. L-1 93177184 (committed at 2c396f6f with the draft packet, unchanged at the freeze f5263d5a; 3,425 bytes, 643
  tokens, 69 «(» / 69 «)»). L-2 1b3dc825 (0ea6959f; 5,810 bytes, 1,035 tokens, 97 / 97): fixes entry 1, L-1 with exactly seven
  replacements (W-2 (a), (b), (c); DB-L2 + W-2 (d) + N-3; DB-L1 + W-3; N-1; N-2; my byte test: each old string once in L-1 and once in the
  running line, each new string once in L-2, L-1 + 7 = L-2, True); token diff 20 hunks (30 tokens out, 422 in), all inside the seven.
(3) THE LINE AT BOTH REFEREES. REFEREE successor 26, docs/referee/R-P-IDEAL-DBL.md: report d7885be4 (2026-11-07T08:49:35Z, new file,
  178 lines, sha1 4aacbd64889bd5c87df3438c668671c592648faa, byte-copied by the lane as box79/ref_d7885be4.md): L-1 «NOT YET: DB-L1 (DATA
  rule), DB-L2 (REENTRY wording); exact texts in §5» (l. 19); §C 34589c09 (2026-11-07T10:08:01Z, 224 lines): «Verdict: fixes entry 1
  CORRECT. L-2 MATCHES, by the byte test and in meaning.» (l. 223). REFEREE-2 successor 30, docs/referee-2/R2-P-IDEAL-DBL.md: report
  2b425bb6 (2026-11-07T08:49:56Z, new file, 136 lines, sha1 72a1986e66c039086cb9b362810996c396f5de18, byte-copied as
  box79/ref2_7891ba32.md): L-1 «**MATCHES after W-2 (a)-(d), W-3**» (l. 22); Addendum 1 30615935 (2026-11-07T10:07:30Z; heading stamp
  «10:1xZ» corrected to «10:0xZ» by 1b9e3ea5, 10:07:40Z; the file 166 lines, l. 137-166): «**L-2 MATCHES** the packet with fixes entry 1,
  in bytes and in meaning» (l. 165-166).
(4) CLAIMS SIGNED = every row of both verdict tables (REFEREE «## 0. Verdicts» l. 5-19; REFEREE-2 «## Verdicts» l. 10-24) as closed in the
  second round: DEAD-REENTRY's gap DB-2 closed at REFEREE (§C l. 217, 224); every other row SIGN at both from the first round. Not signed:
  §5 (both), §7 (both).
(5) OTHER TEXTS THE ENTRY DEPENDS ON: RESULTS R104 (definition), R105 ENC, MONO, LOCAL, R110 (𝓛^R_d), R113 ALIGN, PATH-RISE (and its
  notation c_l, γ_l, flips), R116 AND-GATE (and its notation π, PF_x, KF_x); L-RED's dense_d5_l3_H10 and L-LOWER 3's kill genomes (byte
  copies, G-D); the P-IDEAL-MOVES corpus (l-new 9995f5a2).
(6) PREMISE LABELS: G-4.
(7) SYMBOL TEST: G-2 (i), G-3.
(8) FIXES AND STATUS NOTES: G-14; body Fixes.
(9) GAPS: G-N5-TIME (GAPS l. 11) stays open; L-2 states no CONJECTURE as claimed and kills five lane statements, which are not in GAPS
  («P-IDEAL-DBL», «LEV-ADD», «DAG-ADD» 0 times in GAPS). A line-11 UPDATE is proposed at the end, BUILT FROM L-2 (upd119.py: upd118.py's
  Parts A, B, B2 unchanged: R97's to R116's LANDED UPDATEs rebuilt from their lines byte for byte and compared with GAPS l. 11, True ×20;
  then the R117 control, LANDED: run117() on L-4 filled with GAPS l. 11's stamp 2026-11-07 10:30 d7091311, equal to that segment, to
  R117-draft.md's UPDATE line and to r117b/upd117L4.txt with the same stamp, unfilled sha1 b4d74e09… = C130 §5's: True ×4; then the R118
  control, NOT landed: run118() on L-3 = R118-draft.md's UPDATE line = r118/upd118L3.txt, sha1 fb37efeb…: True ×3; then R119 (G-U)).
(10) DATA of record = packet §7 (l. 169-195) and fixes F-4, NOT signed; L-2's DATA states its counts, with the flags of G-9. Re-run (b):
  PASS, byte-equal.
(11) Discrepancies, recorded for CHECKER, no verdict affected: D-1 the packet header «Written 2026-11-07 from 04:05Z (date -u: see the
  commits)» against the draft commit 2c396f6f at 04:00:12Z. D-2 REFEREE l. 2 «Written from 2026-11-07T08:48Z (date -u); the header time of
  record is the commit time.» (d7885be4 08:49:35Z); REFEREE-2 l. 2 «2026-11-07 from 08:4xZ» (2b425bb6 08:49:56Z): consistent. D-3 REFEREE's
  DB-L2 «fails for l = 1, …, 4» and REFEREE-2's N-3 «killed at l = 1» understated the sets; REFEREE §C l. 209-210 records «MY MISS»; the
  line carries the measured sets. D-4 check79.sh l. 2 «(~30 s)»: 30 s here. D-5 REFEREE-2 W-3 wrote «every start for d ≤ 5» where the
  line (after DB-L1) writes «every start for N ≤ 10»: the same set on 𝓛^R_d (N = 2d). D-6 the packet's PATH-RISE quote is in RESULTS
  after all (G-4).
(12) Excluded: packet §5 (CONDITIONAL: FUEL-NEED, FUEL (i), L-LOWER's FEEDBACK (b)), §7 (DATA, lane DATA, READING), every READING of the
  source note docs/si/N5-TROPICAL-box76.md, EXTRA (RECF4, DBL4, H5, H6; extra79.out, not cited in the line), wiring79.out, tower_H5.out.
  Not part of this entry.
(13) Commits: lane (claude/l-si): 2c396f6f (2026-11-07T04:00:12Z; draft packet, L-1, tools; L-SI successor 41), f5263d5a (08:17:54Z;
  freeze, AND-GATE re-quoted from landed R116, re-pinned; successor 42) → 0ea6959f (09:21:52Z; fixes entry 1, L-2, reentry_levels,
  mkfix1, mkL2, pins); 9b51f2cb, 1d99635c (box 80, other work). REFEREE: d7885be4 → 34589c09. REFEREE-2: 2b425bb6 (carried to origin by
  7891ba32) → 30615935 → 1b9e3ea5 (stamp). CHECKER: docs/checker/ ends at C131.
(14) DEAD-ENDS ROWS: NONE (G-D).

### R119 [refereed-only] In the IDEAL model of RESULTS R104 (premise: R104's definition of the model only; RESULTS R105's ENC, MONO and LOCAL; RESULTS R110's definition of 𝓛^R_d only; RESULTS R113's ALIGN and PATH-RISE; and, for ALT-MIN and TOWER-NEED only, RESULTS R116's AND-GATE (a)-(c)), on acyclic Ξ-graphs, with T the number of steps of a run, Mv_t the movers of step t, moves(x) the number of steps t with x ∈ Mv_t, cv_s(y) the integer value of y's current option (R105 ENC), R(y) the number of steps at which cv(y) rises, R_k(x) the number of steps at which the value of option (x, k) rises, the old chain of y at t its chain under s_(t−1), P(x) the number of maximal Ξ-paths from x, on 𝓛^R_d F(l) the number of flips of the pair (2l, 2l + 1), an l-b-step a flip step of the pair l − 1, Φ_l(s) the number of members of the pair l off c_l(s), an l-window a maximal set of consecutive steps with no l-b-step after its first, a level l ≥ 1 doubling if F(l) = 2F(l − 1) + 2, U_l the Ξ-targets of options of movers of level ≤ l whose Ξ-target has a higher level than that mover and E_l the steps at which some y ∈ U_l changes its value: (MP-LIN) any recursion x_(j+1) ≤ (A ⊗ x_j) ⊕ b over a finite max-plus matrix A grows at most like max(λ, 0)·j + C with λ the maximum cycle mean; (WINDOW-ONCE) on 𝓛^R_d each member of the pair l moves at most once in every l-window; (DBL-EQ) level l is doubling iff Φ_l(s_0) = 2, Φ_l(s_T) = 0, Φ_l = 0 before every l-b-step, no step moves both members and the flips of the pair l are exactly its moving steps, and then each member moves exactly once in every l-window (so F(l − 1) + 1 times), γ_l(0) = γ_l(1) and the first mover of every window is 2l iff γ_l is false; (PASS-FREEZE) for 1 ≤ l ≤ d − 2, if the pair l + 1 never moves and starts split, then F(l + 1) = F(l); (HIT) at any degree, cv(y) rises at step t iff some mover of y's old chain moves at t, so R(y) ≥ moves(y); (FUEL-EXACT) on 𝓛^R_d, E_l is the set of steps at which some mover of the old chain of some y ∈ U_l moves; (ALT-MIN) for a mover x of degree 2, the changes of π(x) to k number at most R_k(x), PF_x ≤ 2 min(R_0(x), R_1(x)) + 1, moves(x) ≤ 2 + 2 min(R_0(x), R_1(x)), and R_k(x) is R of the Ξ-target of (x, k) (0 if X); (TOWER-NEED) at a doubling level l with f = F(l − 1), each member x moves f + 1 times, P(x) ≥ f + 2, and for f ≥ 2 both Ξ-targets of x are movers with R ≥ (f − 1)/2; and four statements are false (DEAD, instances machine-replayed): the max-plus transfers «moves at level j ≤ c + max moves below» and «moves(x) ≤ c + max moves of strict Ξ-descendants» for every c ≤ 5 (experiments/si/box76/inst/dense_d5_l3_H10.json, a byte copy of L-RED's, 𝓛^R_5, start 1100110110: mover 6 of level 3, a Ξ-target, moves 10 times, every mover of levels 0-2 and every strict Ξ-descendant of 6 at most 4 times), «two consecutive doubling levels only if F(l − 1) = 0» (experiments/si/box76/inst/lower/REC_d10_tower_mu30.json, a byte copy of L-LOWER's, 𝓛^R_10, its stored start 00111111010010111010: F(0..3) = 2, 6, 14, 30), «F(l + 1) ≤ F(l) − c above a doubling level without upward options» for every c ≥ 1 (experiments/si/box76/inst/passfreeze77_d5.json, 𝓛^R_5, its stored start 1101111101: F = 2, 2, 2, 6, 6, the top pair never moving), and «the strict Ξ-descendants of the fuel targets U_l lie at levels > l» (static Ξ-graph; measured for every l in 0, …, d − 2 by experiments/si/box79/reentry_levels.py: false for l = 1, …, 8 on experiments/si/box76/inst/lower/REC_d10_tower_mu30.json, a byte copy of L-LOWER's, 𝓛^R_10, witness 1 → 11 → 3 (mover 11 of level 5 is the Ξ-target of mover 1's option 0, and 3 of level 1 is a Ξ-target of an option of 11), and for l = 1, …, 4 on experiments/si/box76/inst/lower/KILL_M2D_d6_mu13.json, a byte copy of L-LOWER's, 𝓛^R_6, witness 2 → 5 → 3 (mover 5 of level 2 is the Ξ-target of an option of mover 2 of level 1, and 3 of level 1 is a Ξ-target of an option of 5); true for l = 0 on both) (2026-11-07) — each statement is about the step sequence of R104's IDEAL model (MP-LIN about max-plus recursions); DBL-EQ (b)'s window count uses one referee-originated step (REFEREE's DB-3, fixes entry 1 F-3, found independently by REFEREE-2); G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim (DATA, experiments/si/box79/dblcheck.py, CORPUS = the 63,223 runs (140,395 steps) of the 208 𝓛^R_d genomes of the frozen P-IDEAL-MOVES corpus (l-new 9995f5a2; every start for N ≤ 10, the stored start otherwise), LOWER = the 9 runs of L-LOWER 3's kill genomes from their stored starts, counts given as CORPUS / LOWER, every genome of degree 2 and width 2 (so HIT and ALT-MIN, stated at any degree, are tested only there): WINDOW-ONCE 0 violations on 577,908 / 1,736 (run, level, window, member); DBL-EQ (a) 0 on 225,647 / 72 (run, level ≥ 1), both directions, with 4,534 / 12 doubling (run, level); (b) 0 on 11,052 / 176 (run, doubling level, window, member); (c) 0 on every doubling (run, level); PASS-FREEZE 0 on the 23,317 (run, level) of CORPUS whose pair above never moves and starts split (none in LOWER); HIT 0 on 1,298,948 / 5,216 (run, mover, step); FUEL-EXACT 0 on 288,870 / 81 (run, level); ALT-MIN 0 on 577,740 / 162 (run, mover), (a) and (d) counted per (run, mover, k); TOWER-NEED's bounds on P and R 0 on 9,068 / 24 (run, doubling level, member), its moves clause through DBL-EQ (b); controls: ALT-MIN's bounds (b) and (c) minus 1 fail on 112,372 / 43 and 7,085 / 13 (run, mover), and with the key-least option taken regardless of availability HIT fails on 238,546 CORPUS (run, mover, step); MP-LIN, the sufficient condition of PASS-FREEZE and DEAD-REENTRY (static Ξ-graph; its level sets measured by experiments/si/box79/reentry_levels.py): no separate DATA; the other three DEAD instances re-run by experiments/si/box79/dead79.py; FUEL-NEED and FUEL (i), which use L-LOWER's unrefereed FEEDBACK (b), are not stated; no statement bounds T polynomially) (P-IDEAL-DBL, docs/si/P-IDEAL-DBL.md with its fixes entry 1, docs/si/P-IDEAL-DBL-fixes.md; L-SI successors 41-42), CHECKER PASS (docs/checker/C133.md, checker PENDING)
- Object (L-SI successors 41-42, D14 / D18 / D20, box 79; frozen, unchanged during review): packet P-IDEAL-DBL, docs/si/P-IDEAL-DBL.md,
  sha1 3573e93bdbd18e824fb6a9d973eb9277d6d6d488, 199 lines, 21,583 bytes (l-si freeze f5263d5a, 2026-11-07T08:17:54Z, after RESULTS R116
  landed at trunk 97d17f63; identical at 0ea6959f and 610897dd). Both referees measured it (REFEREE l. 23 «docs/si/P-IDEAL-DBL.md
  3573e93b…;»; REFEREE-2 l. 5 «docs/si/P-IDEAL-DBL.md 3573e93b… (21,583 B)»). Labels (l. 5-6): «PROVED (L-SI 41, unrefereed) / DEAD
  (instance, machine-checked) / CONDITIONAL (not to sign) / DATA / READING (not to sign)». To sign (table l. 11-21): §1 Fact MP-LIN, §2
  Lemmas WINDOW-ONCE, DBL-EQ (a)-(c), PASS-FREEZE, §3 Lemma HIT and Corollary FUEL-EXACT, §4 Lemmas ALT-MIN (a)-(d) and TOWER-NEED, §6
  DEAD-MAXPLUS, DEAD-DBLGAP, DEAD-DECAY, DEAD-REENTRY; not to sign: §5 FUEL-NEED and FUEL (i) («CONDITIONAL (not to sign)», on L-LOWER's
  FEEDBACK (b), «not landed, not refereed»), §7 DATA / READING. Source (l. 4): docs/si/N5-TROPICAL-box76.md §1-§12 (this lane), history
  only; the packet «carries every proof in full and is checked against this text only» (l. 4-5). The packet's own scope (l. 6-7): «Not a
  TARGET.md claim. Every statement is about the IDEAL model of RESULTS R104's definition only. No statement bounds T polynomially;
  G-N5-TIME stays OPEN.».
  Fixes: docs/si/P-IDEAL-DBL-fixes.md, append-only, two entries by L-SI successor 42 (610897dd: 95 lines, 11,286 bytes, sha1
  edda8237f4c30cea060f44b20392b29a57b126a5). Entry 1 (0ea6959f; the file then 67 lines, 8,797 bytes, sha1
  172bfa2faf343b41075fdea2802539fbb782c9c3): F-1 (W-1 = DB-Q1: the PATH-RISE premise quoted from R113's line), F-2 (DB-2 + W-2 (d) +
  N-3: DEAD-REENTRY's reading and its measured level sets), F-3 (DB-3: a proof step in DBL-EQ (iv)), F-4 (DB-L1 + W-3: the DATA clause),
  F-5 (N-1: F0 dropped from the line's premises; N-2: U_l's wording), and line L-2 = L-1 with seven replacements (l. 44-65). «Not
  changed: every statement of the packet (all SIGN at both referees); L-1 and the packet stay as frozen.» (l. 67). Entry 2 (610897dd, l.
  69-95): CHECKER C133's E-1..E-6 with its §5 replacements R1-R6, line L-3; «Line only: no packet statement, proof or DATA changes.» (l.
  70); «L-1, L-2 and the packet are unchanged.» (l. 94-95). Entry 1 carries one proof step (F-3) and the reading of one DEAD statement
  (F-2); entry 2 carries none.
  The RESULTS line is L-3, 845ffdc9f0306d5db4bdb41d613588b219545838 (docs/si/P-IDEAL-DBL-line-L3.txt, l-si 610897dd,
  2026-11-07T12:38:17Z, the file's only commit; 6,167 bytes). The title is L-3 verbatim, with nothing inserted and nothing stripped (its
  date parenthesis «(2026-11-07)», its scope tail and its source note are the line's own; the source note names the packet with its
  fixes entry 1, which carries F-2 and F-3; entry 2 carries no proof). L-3's parentheses balance (101 «(» / 101 «)»). Line history: L-1
  (93177184, committed with the draft packet at 2c396f6f, unchanged at the freeze f5263d5a); L-2 (1b3dc825, 0ea6959f, fixes entry 1: L-1
  with exactly seven replacements: REFEREE-2's W-2 (a), (b), (c) (the DEAD instances by path and start), REFEREE's DB-L2 with
  REFEREE-2's W-2 (d) and N-3 (DEAD-REENTRY's reading, with the level sets measured by experiments/si/box79/reentry_levels.py),
  REFEREE's DB-L1 with REFEREE-2's W-3 no-DATA items (the DATA clause by clause), REFEREE-2's N-1 (F0 dropped) and N-2 (U_l «whose
  Ξ-target has a higher level than that mover»)); L-3 (845ffdc9, 610897dd, fixes entry 2: L-2 with exactly CHECKER C133 §5's R1-R6,
  applied in that order, R4's old string inside R3's new text; they are the first fill's R-A, R-B, R-C, R-G, R-D, R-E; see Fixes). Each
  old string occurs once in L-1 and each new string once in L-2, and L-1 with the seven replacements is L-2 (my script, True; REFEREE by
  its own script, §C l. 187-190); L-2 with R1-R6 is L-3 (my script, True; both referees by their own scripts). L-1: REFEREE «NOT YET:
  DB-L1 (DATA rule), DB-L2 (REENTRY wording); exact texts in §5» (d7885be4 l. 19); REFEREE-2 «**MATCHES after W-2 (a)-(d), W-3** (DEAD
  instances not reproducible from the line; DATA not clause by clause)» (2b425bb6 l. 22). L-2 MATCHES at REFEREE after its own byte
  test: REFEREE successor 26 (34589c09) §C l. 187-190 («the seven OLD / NEW pairs are parsed from fixes entry 1;», «each old string
  occurs once in L-1 and each new string once in L-2;», «L-1 with the seven replacements is byte-equal to L-2 (sha1 1b3dc825…).»), l.
  191-210 (meaning: DB-L1 «MET», with «exactly one change» (the W-3 widening), «The widening is correct.»; DB-L2 «MET, with the MEASURED
  level sets»), l. 223 «Verdict: fixes entry 1 CORRECT. L-2 MATCHES, by the byte test and in meaning.». REFEREE-2 successor 30
  (30615935, heading stamp corrected at 1b9e3ea5) Addendum 1 l. 142-144 (own bt_l2.py: «each old string once in L-1, each new once in
  L-2; L-1 with all seven == L-2 byte for byte (sha1 1b3dc825…, 5,810 B, 1 line, 97 «(» = 97 «)», depth never negative»; «W-2 (a), (b),
  (c): NEW is my text verbatim ✓»), l. 147-155 (DEAD-REENTRY's sets by its own code: «Equal to the lane's reentry_levels.out as quoted
  in F-2 ✓»), l. 156-162 (DATA: «My W-3 is met in substance.»), l. 165-166 «Verdict: fixes entry 1 **CORRECT**; W-1, W-2 (a)-(d), W-3
  **met**; **L-2 MATCHES** the packet with fixes entry 1, in bytes and in meaning (Opus 5.5, D1).». L-3 MATCHES at both referees, each
  after its own byte test: REFEREE successor 26 (07a950ae, 2026-11-07T13:01:15Z) §C add. 1 l. 232-236 (own script: «R1-R6 are parsed
  from C133 §5 (wrapped lines joined by one space) and applied in C133's order.»; «The result is byte-equal to L-3 (sha1 845ffdc9…,
  6,167 bytes).»), l. 237-248 (meaning: «R4: CORRECT, and correctly attributed.»; «R5: CORRECT.»; «R6: CORRECT.»; «R1-R3: CORRECT.»), l.
  249 «Verdict: L-3 MATCHES, by the byte test and in meaning. All statements stay as signed in §C.»; REFEREE-2 successor 30 (37c733e2,
  2026-11-07T13:01:16Z) Addendum 2 l. 171-174 (own bt_l3.py: «L-2 + R1..R6 == L-3 byte for byte, sha1
  845ffdc9f0306d5db4bdb41d613588b219545838, 6,167 B (= C133's prediction)»), l. 175-184 (meaning: R5 and R6 against the packet's
  hypotheses and the ranges it signed, R4 against its own report's DBL-EQ (iv), «written and pushed (2b425bb6) before I read any REFEREE
  text», R3 against the packet's §7 TARGET diff, R1, R2), l. 185 «Verdict: entry 2 **CORRECT**; **L-3 MATCHES** the packet with fixes
  entries 1-2, in bytes and in meaning (Opus 5.5, D1). Statements all SIGN.».
- Claims signed (REFEREE successor 26 (D15), report d7885be4, §C 34589c09 and §C add. 1 07a950ae; REFEREE-2 successor 30 (D1), report
  2b425bb6, Addendum 1 30615935 / 1b9e3ea5 and Addendum 2 37c733e2). REFEREE's table (l. 5-19 of R-P-IDEAL-DBL.md) reads MP-LIN,
  WINDOW-ONCE, PASS-FREEZE «(and its sufficient condition)», HIT, FUEL-EXACT, ALT-MIN «SIGN», DBL-EQ «SIGN (optional DB-3: say why step
  1 is no l-b-step at a doubling level)», TOWER-NEED «SIGN (its PATH-RISE premise with DB-Q1)», DEAD-MAXPLUS, DEAD-DBLGAP, DEAD-DECAY
  «SIGN (own simulator; the IDEAL step is deterministic: distinct gate indices, no ties)», DEAD-REENTRY «SIGN WITH GAP DB-2 (the level l
  is not named; read literally the statement is false almost trivially)», §5 «not reviewed for signature (CONDITIONAL on L-LOWER's
  unrefereed FEEDBACK (b), as the packet says)»; REFEREE-2's table (l. 10-24 of R2-P-IDEAL-DBL.md) reads every §1-§4 row and the four
  DEAD items «**SIGN** (Opus 5.5, D1)», with «the §0 mapping of R116 AND-GATE onto (a)-(c) is faithful» (l. 18) and «every instance
  replayed with my own simulator (N-3 on REENTRY's l)» (l. 20), «Not signed (as the packet says): §5 FUEL-NEED and FUEL (i) (CONDITIONAL
  on L-LOWER's unlanded FEEDBACK (b)); §7 DATA / READING.» (l. 23), «Nothing is REFUSED.» (l. 24). Fixes entry 1 closes DB-2 and DB-Q1 /
  W-1 at REFEREE: §C l. 215-218 («F-1 (DB-Q1): CLOSED.», «F-2 (DB-2): CLOSED. It fixes the reading (strict Ξ-descendants, static
  Ξ-graph) and gives the measured sets.», «F-3 (DB-3): CLOSED.») and l. 223-224 «All statements stay SIGNED; DEAD-REENTRY is now SIGN
  (DB-2 closed).». REFEREE-2 Addendum 1 l. 145-146 «**W-1 closed** (F-1)» and l. 166 «Statement verdicts unchanged (all SIGN).». No gap
  remains; nothing is REFUSED. The L-3 round changes no verdict: REFEREE §C add. 1 l. 249 «All statements stay as signed in §C.»;
  REFEREE-2 Addendum 2 l. 185 «Statements all SIGN.». Setting: R104's IDEAL model on acyclic Ξ-graphs; 𝓛^R_d as R110 defines it; R113's
  c_l(s), γ_l(j) and flips; R116's π_s(x), PF_x, KF_x. Statements as signed (packet with fixes entry 1):
  (a) Notation (§0 l. 44-52): T, s_t, Mv_t, moves(x); on 𝓛^R_d the pair l = (2l, 2l + 1), F(l) its flips, an l-b-step a flip step of the
    pair l − 1, Φ_l(s), the l-windows, a level l ≥ 1 doubling if F(l) = 2F(l − 1) + 2; cv_s(y), R(y), R_k(x), the old chain, P(x); the
    upward options, U_l and E_l.
  (b) Fact MP-LIN (§1 l. 54-58) [max-plus algebra, no premise]: «max_τ x_j(τ) ≤ max(λ, 0)·j + C for every j, where C depends on A, b and
    x_0 but not on j».
  (c) Lemma WINDOW-ONCE (§2 l. 65-69) [𝓛^R_d, 1 ≤ l ≤ d − 1, any run]: «Then c_l(s_t) is the same for every t ∈ ω, and each of 2l, 2l + 1
    moves at most once in ω, to that option.»
  (d) Lemma DBL-EQ (a)-(c) (§2 l. 70-94, with F-3 in (iv)) [𝓛^R_d, 1 ≤ l ≤ d − 1, any run]: «(a) Level l is doubling iff all of: Φ(s_0) =
    2; Φ(s_T) = 0; Φ(s_(t−1)) = 0 at every l-b-step t; no step moves both p and q; the flip steps of the pair l are exactly the steps that
    move p or q.»; «(b) If level l is doubling, each of p, q moves exactly once in every l-window; so moves(p) = moves(q) = F(l − 1) + 1.»;
    «(c) If level l is doubling, γ_l(0) = γ_l(1) =: γ, and in every l-window the first of p, q to move is p iff γ is false.» Its proof
    re-proves R113's PAIR-DOUBLE bound F(l) ≤ 2 + 2F(l − 1) (step (iii)).
  (e) Lemma PASS-FREEZE (§2 l. 95-104) [𝓛^R_d, 1 ≤ l ≤ d − 2, any run]: «If neither member of the pair l + 1 moves in the run and they start
    on different options, then F(l + 1) = F(l).», with a sufficient condition for «never moves» (not in the line).
  (f) Lemma HIT (§3 l. 107-114) [IDEAL-ACYC, any degree, any width]: «cv_(s_t)(y) > cv_(s_(t−1))(y) iff some mover of the old chain of y at
    t moves at t. Hence R(y) = #{t : Mv_t meets the old chain of y} ≥ moves(y).»
  (g) Corollary FUEL-EXACT (§3 l. 115-118) [𝓛^R_d, Ξ-acyclic, 0 ≤ l ≤ d − 1]: «Then E_l = {t : some mover of the old chain at t of some y ∈
    U_l moves at t}» with a size bound by Σ_(y ∈ U_l) R(y) (the line states the set form only).
  (h) Lemma ALT-MIN (a)-(d) (§4 l. 121-129) [IDEAL-ACYC, any degree elsewhere, x of degree 2]: «(a) #{t : π(x) changes at t to k} ≤ R_k(x)
    for k = 0, 1.», «(b) PF_x ≤ 2·min(R_0(x), R_1(x)) + 1.», «(c) moves(x) ≤ 2 + 2·min(R_0(x), R_1(x)).», «(d) R_k(x) = R(y_k) if y_k is a
    mover, and R_k(x) = 0 if y_k = X; so if an option of x has Ξ-target X, moves(x) ≤ 2.» Premise: R116's AND-GATE, parts (b) and (c) of
    the packet's partition (REFEREE l. 40 «Only (b) and (c) are used»; REFEREE-2 l. 43).
  (i) Lemma TOWER-NEED (§4 l. 130-134) [𝓛^R_d, Ξ-acyclic, 1 ≤ l ≤ d − 1, a run in which level l is doubling, f := F(l − 1)]: «Then moves(x)
    = f + 1, P(x) ≥ f + 2, and if f ≥ 2 both Ξ-targets of x are movers y with R(y) ≥ (f − 1)/2.» Premises: DBL-EQ (b), HIT, R113's PATH-RISE,
    ALT-MIN (c), (d).
  (j) DEAD (§6 l. 145-167, DEAD-REENTRY read by F-2) [instances, machine-replayed]: LEV-ADD c and DAG-ADD c for every c ≤ 5 on
    dense_d5_l3_H10 from 1100110110 (mover 6 of level 3 moves 10 times; levels 0-2 and 6's strict Ξ-descendants at most 4); «If levels l
    and l + 1 are both doubling in a run, then F(l − 1) = 0» on REC_d10_tower_mu30 from its stored start (F(0..3) = 2, 6, 14, 30); «If level
    l is doubling and the level l + 1 has no upward option, then F(l + 1) ≤ F(l) − c», every c ≥ 1, on passfreeze77_d5 from its stored start
    (F = 2, 2, 2, 6, 6); and F-2's «the strict Ξ-descendants of the fuel targets U_l lie at levels > l» (static Ξ-graph) on
    REC_d10_tower_mu30 and KILL_M2D_d6_mu13, with the level sets of reentry_levels.out.
- The RESULTS line (L-3, the title): «In the IDEAL model of RESULTS R104 (premise: R104's definition of the model only;» … «and, for
  ALT-MIN and TOWER-NEED only, RESULTS R116's AND-GATE (a)-(c)), on acyclic Ξ-graphs,» … «(2026-11-07) — each statement is about the
  step sequence of R104's IDEAL model (MP-LIN about max-plus recursions); DBL-EQ (b)'s window count uses one referee-originated step
  (REFEREE's DB-3, fixes entry 1 F-3, found independently by REFEREE-2); G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a
  TARGET.md claim (DATA,» … «(P-IDEAL-DBL, docs/si/P-IDEAL-DBL.md with its fixes entry 1, docs/si/P-IDEAL-DBL-fixes.md; L-SI successors
  41-42)». Its clauses: notation = (a); MP-LIN = (b); WINDOW-ONCE = (c) without the constancy of c_l; DBL-EQ = (d); PASS-FREEZE = (e)
  with its range 1 ≤ l ≤ d − 2 (R5), without its sufficient condition; HIT = (f); FUEL-EXACT = (g) set form, on 𝓛^R_d (R6), without the
  size bound; ALT-MIN = (h) without (d)'s last clause; TOWER-NEED = (i); DEAD = (j). Its DATA: the parenthesis «(DATA,
  experiments/si/box79/dblcheck.py, …)», clause by clause. L-3 changes, from L-2, the head (R1 drops «R1xx [refereed-only] »), the
  source note (R2: the packet with its fixes entry 1, docs/si/P-IDEAL-DBL-fixes.md; L-SI successors 41-42), the scope tail (R3: the date
  parenthesis, the packet's §7 scope words, «G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim»; R4: L41's sentence
  inside it), PASS-FREEZE's range (R5) and FUEL-EXACT's class (R6).
- Premise: RESULTS R104's definition of the IDEAL model only, no theorem of R104; RESULTS R105's «(ENC) the Ξ-order of β-sets is the order
  of the integers Σ ±2^rank (+ for even parity), so, with ε(x, k) := ±2^rank(x, k) (+ for even parity), the value of option (x, k) is ε(x,
  k) plus the current value of its Ξ-target (ε(x, k) alone if the Ξ-target is the exit X)», «(MONO) the current Ξ-value of every mover never
  decreases along a run» and «(LOCAL) an option's value depends only on the states on its chain, a key only on the states below its level»
  (R105 l. 10155), for HIT, FUEL-EXACT, ALT-MIN (d); RESULTS R110's definition of 𝓛^R_d only («movers 2l and 2l + 1 on level l, all of
  degree 2, no other movers, option k of a mover of level l ≥ 1 W-pointing to mover 2(l − 1) + k», l. 11323); RESULTS R113's «(ALIGN) on
  𝓛^R_d, for 1 ≤ l ≤ d − 1 and every state s of a run, both movers 2l and 2l + 1 have KP_s = c_l(s), each of them that moves at step t moves
  to option c_l(s_t), and the order of their keys under s is [s(2l) = c_l(s)] if s(2l) ≠ s(2l + 1) and γ_l(j) if both are on option j»,
  for WINDOW-ONCE, DBL-EQ, PASS-FREEZE, and «(PATH-RISE) at any degree, the current value cv(z) of every mover z rises at most P(z) − 1
  times in a run» (l. 12152), for TOWER-NEED; RESULTS R116's «(AND-GATE) at any degree elsewhere, a mover x of degree 2 moves at step t
  iff s_(t−1)(x) ≠ π_(s_(t−1))(x) = KP_(s_t)(x), so moves(x) ≤ 1 + min(KF_x, PF_x), and when π(x) changes at step t to b the value v(x, b)
  rises strictly at t» (l. 13072), for ALT-MIN and through it TOWER-NEED. R113 and R116 are stated on acyclic Ξ-graphs, as this line is.
  Both referees checked every premise quote against RESULTS (REFEREE l. 35-48; REFEREE-2 l. 26-43).
- L41 and L43. The proofs are L-SI successor 41's (packet l. 2-5). One proof step, F-3 in DBL-EQ (iv) (step 1 is not an l-b-step at a
  doubling level, so there are exactly F(l − 1) + 1 windows), was suggested by REFEREE as optional DB-3 (l. 67-68) and derived by
  REFEREE-2 independently in its first report (l. 54-55); the packet's (iv) already stated the count. The Lead ruled that L41 applies
  (CHECKER C133 E-6: «The Lead ruled that L41 applies.»); L-3's scope tail says so (R4, the first fill's R-G): «DBL-EQ (b)'s window
  count uses one referee-originated step (REFEREE's DB-3, fixes entry 1 F-3, found independently by REFEREE-2)» (REFEREE §C add. 1 l.
  237 «R4: CORRECT, and correctly attributed.»; REFEREE-2 Addendum 2 l. 179-181, «written and pushed (2b425bb6) before I read any
  REFEREE text»). L43: the four DEAD items are not asymptotic statements; they are DEAD by explicit instances, replayed by both referees
  with their own simulators.
- Fixes (docs/si/P-IDEAL-DBL-fixes.md, append-only, entries 1-2 by L-SI successor 42; entry 1 at 0ea6959f, l. 1-67, the file then 67
  lines, 8,797 bytes, sha1 172bfa2faf343b41075fdea2802539fbb782c9c3; entry 2 at 610897dd, l. 69-95, the file now 95 lines, 11,286 bytes,
  sha1 edda8237f4c30cea060f44b20392b29a57b126a5, its l. 1-67 = entry 1's file, by script; entry 1: «Lead 09:20Z: REFEREE 26 d7885be4
  DB-Q1, DB-2, DB-3, DB-L1, DB-L2; REFEREE-2 30 7891ba32 W-1, W-2 (a)-(d), W-3, N-1..N-3; Lead rulings 1-5», l. 3-4; «Strings copied by
  script», l. 4; the referee reports byte-copied as experiments/si/box79/ref_d7885be4.md and ref2_7891ba32.md, equal to d7885be4's and
  2b425bb6's files, by script):
  - F-1 (W-1 = DB-Q1; Lead ruling 1): PATH-RISE quoted from R113's line («Same content; TOWER-NEED (§4) and FUEL-NEED (§5) use exactly this.
    No proof changes.»).
  - F-2 (DB-2 + W-2 (d) + N-3; Lead ruling 3): DEAD-REENTRY read as «the strict Ξ-descendants of the fuel targets U_l lie at levels > l»
    (static Ξ-graph); the level sets MEASURED for every l in 0, …, d − 2 under readings A and B (reentry_levels.out); «The DEAD verdicts
    stand.».
  - F-3 (DB-3, taken; Lead ruling 4): DBL-EQ (iv), step 1 is not an l-b-step at a doubling level.
  - F-4 (DB-L1 + W-3; Lead ruling 2): the DATA clause is DB-L1's New text with W-3's no-DATA items; PASS-FREEZE keeps its PF count.
  - F-5 (N-1, N-2): F0 dropped from the line's premises; U_l's wording.
  - Entry 2 (after CHECKER C133 8f6d03bc, «Verdict: FAIL (E-1 to E-6; one L-3 with six replacements, §5)» (C133 l. 15); L-SI successor
    42, 610897dd, 2026-11-07T12:38:17Z): «Line only: no packet statement, proof or DATA changes.» (l. 70); «Strings copied by script
    (experiments/si/box79/mkL3.py) from experiments/si/box79/c133_8f6d03bc.md, a byte copy of docs/checker/C133.md at 8f6d03bc, §5
    (wrapped lines joined with one space).» (l. 70-71). Line L-3 = L-2 with R1-R6 applied in that order (l. 75-93), each old string once
    in the text it is applied to (R4's inside R3's new text). My script (l3rel119.py): the six pairs of entry 2 (l. 76-93) and of C133
    §5 (l. 60-71) are the same (True); they are the first fill's R-A, R-B, R-C, R-G, R-D, R-E (True ×6); L-2 + R1-R6 = L-3 (True). How
    each E-item is resolved (by script on L-3; each new string once in L-3, R3's as edited by R4): E-1 (the heading label) by R1, and
    «R1xx» occurs 0 times in L-3; E-2 (source note) by R2, «(P-IDEAL-DBL, docs/si/P-IDEAL-DBL.md with its fixes entry 1,
    docs/si/P-IDEAL-DBL-fixes.md; L-SI successors 41-42)»; E-3 (scope tail) by R3, the date parenthesis and the scope words (see The
    RESULTS line); E-4 (PASS-FREEZE's range) by R5, «for 1 ≤ l ≤ d − 2, if the pair l + 1 never moves and starts split, then F(l + 1) =
    F(l)»; E-5 (FUEL-EXACT's class) by R6, «on 𝓛^R_d, E_l is the set of steps at which some mover of the old chain»; E-6 (L41) by R4
    (see L41 and L43). The first fill's optional R-F is not taken («Not taken (note N-1): R-F», C133 l. 38).
  - No statement of the packet changes; entry 1 corrects a premise quote, fixes one DEAD reading, adds one proof step and rewrites the
    line; entry 2 changes the line only.
- Not signed: packet §5 (FUEL-NEED, FUEL (i): CONDITIONAL on L-LOWER's Lemma FEEDBACK (b) of docs/lower/L3-families.md §4, «not landed, not
  refereed», packet l. 137), §7 (DATA, lane DATA, READING), the READINGs of docs/si/N5-TROPICAL-box76.md, EXTRA (extra79.out).
- Referee strengthening (NOT part of this entry; referee checks):
  (i) REFEREE: own replay tools on its own IDEAL simulator t3r_sim.py (docs/referee/scratch/dbl_replay.py, dbl_dead_static.py,
    dbl_corpus.py); 0 violations on 16 runs (the three run-based DEAD instances, EXTRA's four genomes, the nine LOWER genomes); DBL-EQ on
    H6_d24_F126 (levels 1-5 doubling, F(0..5) = 2, 6, 14, 30, 62, 126); the corpus with N ≤ 10 (193 genomes, every start: 63,208 runs) with
    0 violations of DBL-EQ, WINDOW-ONCE, TOWER-NEED, HIT, MONO and ALT-MIN (l. 93-121); every DEAD value equal to the packet; the
    DEAD-REENTRY level sets measured with its own code (dbl_reentry_levels.py; §C l. 200-206).
  (ii) REFEREE-2: own r2dbl.py on its own R104 simulator r2moves.py, no lane code: CORPUS 208 files, 63,223 runs, 140,395 steps, 4,534
    doubling (run, level), «**0 violations of every check**» (l. 67-69); LOWER and EXTRA 0 (l. 70-73), DBL-EQ on H6_d24_F126 and on H5,
    DBL4, RECF4; the four DEAD instances replayed (l. 74-82); check79.sh re-run on git archive f5263d5a (l. 7-8).
  (iii) The L-3 round: REFEREE §C add. 1 checked R4's attribution against its own DB-3 and against REFEREE-2's report («REFEREE-2
    derived the same step on its own: docs/referee-2/R2-P-IDEAL-DBL.md l. 53-54»; «Read after my reports on this packet were pushed.»),
    R5's range against the hypothesis it signed (§3 of its report) and R6's class (l. 237-244); REFEREE-2 Addendum 2 checked R5 and R6
    against the packet's hypotheses and the ranges it signed, R4 against its own report's DBL-EQ (iv) («written and pushed (2b425bb6)
    before I read any REFEREE text») and R3 against the packet's §7 TARGET diff (l. 175-184).
- Honest limits: (i) No statement bounds T, R or F polynomially; TOWER-NEED gives necessary conditions for doubling levels, not a bound
  on their number (packet l. 134). (ii) MP-LIN bounds max-plus recursions; no such recursion is claimed for a quantity of the IDEAL
  model, and DEAD-MAXPLUS kills the two natural scalar ones (packet l. 60). (iii) HIT and ALT-MIN are stated at any degree and tested on
  degree-2, width-2 ladders only. (iv) FUEL-NEED and FUEL (i) are not stated: they rest on L-LOWER's unlanded, unrefereed FEEDBACK (b).
  (v) All DATA runs are runs of implementations (box76/tw.py's Sim; the referees' own simulators). (vi) Names: «MP-LIN», «WINDOW-ONCE»,
  «DBL-EQ», «PASS-FREEZE», «HIT», «FUEL-EXACT», «ALT-MIN», «TOWER-NEED» and the DEAD labels are new to RESULTS; «R119» is also an old
  L-RED round label (docs/red/R119-mixed-gate.md), not a RESULTS label. (vii) MP-LIN is the standard max-plus growth bound, proved in
  full in the packet; no literature source is cited and no novelty is claimed. (viii) CHECKER C133 (8f6d03bc) FAILED the first fill
  (draft 3fb40db1, on L-2) with E-1..E-6, all line wording («No statement is strengthened; E-4 and E-5 narrow two clauses to their
  signed scope.», C133 l. 16-17); L-3 resolves them by R1-R6 (Fixes).
- Data (DATA, not proof): experiments/si/box79/ at l-si 0ea6959f (unchanged at 610897dd but for check79.sh, which adds the mkL3.py step,
  and pins.sha1, which re-pins the fixes and adds L-3, mkL3.py, mkfix2.py and c133_8f6d03bc.md, a byte copy of C133 at 8f6d03bc):
  dblcheck.py (the counters WO, DBLa, DBLb, DBLc, PF, HIT, FU2, ALTa-ALTd, TN and the controls; Sim of experiments/si/box76/tw.py,
  R104's IDEAL model), dblcheck.out (CORPUS and LOWER), dblcheck_neg2.out (NEG=2: the key-least option regardless of availability),
  dead79.py and dead79.out (the DEAD instances, every number asserted), reentry_levels.py and reentry_levels.out (DEAD-REENTRY, readings
  A and B, every l in 0, …, d − 2). Wired into experiments/si/check.sh (l. 1247, «bash box79/check79.sh»; run by scripts/verify.sh):
  check79.sh, pins.sha1 (sha1sum -c --strict: packet, L-1, L-2, L-3, fixes, tools, outputs, EXTRA genomes, the two byte-copied referee
  reports, the C133 copy), then dblcheck.py (CORPUS, LOWER), NEG=2, EXTRA, wiring79.py, dead79.py, reentry_levels.py, mkL2.py and
  mkL3.py, each diffed against its committed output (mkL2.py's against L-2, mkL3.py's against L-3), and four violation lines asserted.
  Re-run from a git archive of 610897dd at the second fill: 2026-11-07T14:51:53Z-14:52:24Z, rc 0, «box 79 P-IDEAL-DBL (frozen) checks:
  PASS» (first fill: 0ea6959f, 10:36:24Z-10:36:54Z, rc 0, PASS; CHECKER C133 §4: from 0ea6959f, rc 0, PASS; both referees re-ran it:
  REFEREE §C l. 186 «check79.sh at 0ea6959f: PASS, exit 0»; REFEREE-2 l. 7-8 at f5263d5a). Sets: CORPUS = the 208 𝓛^R_d genomes of the
  frozen P-IDEAL-MOVES corpus (experiments/si/box76/corpus_lr.json.gz, each text re-hashed against its git blob at l-new 9995f5a2),
  every start for N ≤ 10 (193 genomes) and the stored start otherwise (15), 63,223 runs, 140,395 steps; LOWER = L-LOWER 3's nine kill
  genomes (experiments/si/box76/inst/lower/, byte copies of l-lower 4d747490 experiments/lower/l3/kill/), stored starts, 9 runs, 270
  steps. Instance and corpus files are pinned in experiments/si/box76/pins.sha1 (run by check76.sh).
- Signatures: REFEREE docs/referee/R-P-IDEAL-DBL.md: successor 26's report d7885be4 (2026-11-07T08:49:35Z; «Written from
  2026-11-07T08:48Z (date -u); the header time of record is the commit time.»), «I did NOT read docs/referee-2/ for this report.» (l.
  3), verdict table l. 5-19; §C 34589c09 (2026-11-07T10:07Z by its heading, commit 10:08:01Z), l. 180-224, verdict l. 223-224: «Verdict:
  fixes entry 1 CORRECT. L-2 MATCHES, by the byte test and in meaning. All statements stay SIGNED; DEAD-REENTRY is now SIGN (DB-2
  closed).»; §C add. 1 07a950ae8f4690f851ee2b5d33a0e0252ce873b2 (2026-11-07T13:01:15Z; heading «date -u at writing 2026-11-07T13:01Z»),
  l. 226-249, «Verdict: L-3 MATCHES, by the byte test and in meaning. All statements stay as signed in §C.» (l. 249). REFEREE-2
  docs/referee-2/R2-P-IDEAL-DBL.md: successor 30's report 2b425bb6 (2026-11-07T08:49:56Z; carried to origin by 7891ba32), «Independent:
  docs/referee/ not read on this item.» (l. 2), verdict table l. 10-24, «F-4: L-1 MATCHES after W-2 (a)-(d) and W-3.» (l. 131); Addendum
  1 30615935 (2026-11-07T10:07:30Z; heading «10:0xZ by date -u» after the stamp fix 1b9e3ea5, 10:07:40Z), l. 137-166, «I read REFEREE's
  items only as the fixes file quotes them, after my report (2b425bb6) was on origin.» (l. 140-141), verdict l. 165-166 (above);
  Addendum 2 37c733e2362991d0e309879ff264ce1e2971d724 (2026-11-07T13:01:16Z; heading «2026-11-07 13:0xZ by date -u»), l. 168-185, with
  R2-P-IDEAL-DBL/bt_l3.py and bt_l3.out, «Verdict: entry 2 **CORRECT**; **L-3 MATCHES** the packet with fixes entries 1-2, in bytes and
  in meaning (Opus 5.5, D1). Statements all SIGN.» (l. 185). Lane (claude/l-si): L-SI successor 41, 2c396f6f (draft); successor 42,
  f5263d5a (freeze), 0ea6959f (fixes entry 1, L-2), 610897dd (fixes entry 2, L-3).
- INDEPENDENCE: the packet's proofs are L-SI's; each referee re-derived every step (REFEREE §3; REFEREE-2 «## Proofs (own
  re-derivation)») and replayed the statements on a simulator that is not the lane's (REFEREE: t3r_sim.py, written by its successor 24
  from R104's text; REFEREE-2: r2moves.py, «no lane code», l. 64). Each referee wrote its first report without reading the other's
  (REFEREE l. 3; REFEREE-2 l. 2); REFEREE's §C read REFEREE-2's items through fixes entry 1. The DATA wording of L-2 is REFEREE's DB-L1
  with REFEREE-2's W-3 items; the DEAD wording is REFEREE-2's W-2 (a)-(c) and REFEREE's DB-L2 with the lane's measured sets (F-2);
  REFEREE §C l. 209-210 records that its own DB-L2 set was unmeasured («MY MISS») and that «The lane's measured sets replace mine.», and
  REFEREE-2 Add. 1 l. 153-154 that its N-3 was incomplete («I withdraw «only».»); both re-measured the sets with their own code (REFEREE
  dbl_reentry_levels.py; REFEREE-2 r2reentry.out), equal to the lane's. L-3's further wording (R1-R6) is CHECKER C133's (the first
  fill's R-A, R-B, R-C, R-G, R-D, R-E, adopted by C133; R4 by the Lead's L41 ruling); in the L-3 round each referee byte-tested L-3 with
  its own script and read R1-R6 in meaning (REFEREE §C add. 1 l. 232-248; REFEREE-2 Addendum 2 l. 171-184).
- TARGET.md diff: TARGET.md §1 defines a parity game; the IDEAL model of R104 is a step rule on genomes (R104's definition), not a
  parity-game solver, and no statement of this entry mentions a parity game, a winning region, an algorithm's running time or a
  complexity class (packet §7 l. 193-195; REFEREE l. 167-168 «no statement mentions a parity game, a winning region or a running time»;
  REFEREE-2 l. 24 «No statement bounds T; G-N5-TIME stays OPEN.»). No statement bounds T polynomially (L-3: «no statement bounds T
  polynomially»). It is not an algorithm claim, so TARGET.md §5's gauntlet does not apply, and it is not a step-4 pass. L-3 carries the
  scope tail «each statement is about the step sequence of R104's IDEAL model (MP-LIN about max-plus recursions);» … «G-N5-TIME stays
  OPEN; not M3, not a step-4 pass, not a TARGET.md claim» (R3, by script). GAPS G-N5-TIME: open.

Proposed GAPS line-11 UPDATE (append-only), to go AFTER the last UPDATE on GAPS l. 11 at landing (R118's, «UPDATE 2026-11-07 14:48Z:
RESULTS R118 (P-N5-XICYC; CHECKER C132 af92b846)», the last at this second fill), as a pure insertion with one separating space before the
row's closing « |». BUILT FROM L-3 by upd119b.py (R116's procedure, unchanged, as CHECKER C133 E-3 rules: sentinel_build111 with its
default drops and R111's / R116's DEAD-clause step; controls R97-R116 rebuilt byte for byte and the R117 and R118 controls as landed, each
compared with GAPS l. 11, True ×22; sha1 074e3c05060c7adcd7b20e5560674bdf12d8b2fa of the line without newline and unfilled). <DATE>,
<HH:MM> and <checker> are the landing date, time and the C133 commit, all filled at landing:
UPDATE <DATE> <HH:MM>Z: RESULTS R119 (P-IDEAL-DBL; CHECKER C133 <checker>) [refereed-only] LANDED: In the IDEAL model of RESULTS R104 (premise: R104's definition of the model only; RESULTS R105's ENC, MONO and LOCAL; RESULTS R110's definition of 𝓛^R_d only; RESULTS R113's ALIGN and PATH-RISE; and, for ALT-MIN and TOWER-NEED only, RESULTS R116's AND-GATE (a)-(c)), on acyclic Ξ-graphs, with T the number of steps of a run, Mv_t the movers of step t, moves(x) the number of steps t with x ∈ Mv_t, cv_s(y) the integer value of y's current option (R105 ENC), R(y) the number of steps at which cv(y) rises, R_k(x) the number of steps at which the value of option (x, k) rises, the old chain of y at t its chain under s_(t−1), P(x) the number of maximal Ξ-paths from x, on 𝓛^R_d F(l) the number of flips of the pair (2l, 2l + 1), an l-b-step a flip step of the pair l − 1, Φ_l(s) the number of members of the pair l off c_l(s), an l-window a maximal set of consecutive steps with no l-b-step after its first, a level l ≥ 1 doubling if F(l) = 2F(l − 1) + 2, U_l the Ξ-targets of options of movers of level ≤ l whose Ξ-target has a higher level than that mover and E_l the steps at which some y ∈ U_l changes its value: any recursion x_(j+1) ≤ (A ⊗ x_j) ⊕ b over a finite max-plus matrix A grows at most like max(λ, 0)·j + C with λ the maximum cycle mean (MP-LIN); on 𝓛^R_d each member of the pair l moves at most once in every l-window (WINDOW-ONCE); level l is doubling iff Φ_l(s_0) = 2, Φ_l(s_T) = 0, Φ_l = 0 before every l-b-step, no step moves both members and the flips of the pair l are exactly its moving steps, and then each member moves exactly once in every l-window (so F(l − 1) + 1 times), γ_l(0) = γ_l(1) and the first mover of every window is 2l iff γ_l is false (DBL-EQ); for 1 ≤ l ≤ d − 2, if the pair l + 1 never moves and starts split, then F(l + 1) = F(l) (PASS-FREEZE); at any degree, cv(y) rises at step t iff some mover of y's old chain moves at t, so R(y) ≥ moves(y) (HIT); on 𝓛^R_d, E_l is the set of steps at which some mover of the old chain of some y ∈ U_l moves (FUEL-EXACT); for a mover x of degree 2, the changes of π(x) to k number at most R_k(x), PF_x ≤ 2 min(R_0(x), R_1(x)) + 1, moves(x) ≤ 2 + 2 min(R_0(x), R_1(x)), and R_k(x) is R of the Ξ-target of (x, k) (0 if X) (ALT-MIN); at a doubling level l with f = F(l − 1), each member x moves f + 1 times, P(x) ≥ f + 2, and for f ≥ 2 both Ξ-targets of x are movers with R ≥ (f − 1)/2 (TOWER-NEED); and four statements are false (DEAD, instances machine-replayed): the max-plus transfers «moves at level j ≤ c + max moves below» and «moves(x) ≤ c + max moves of strict Ξ-descendants» for every c ≤ 5 (experiments/si/box76/inst/dense_d5_l3_H10.json, a byte copy of L-RED's, 𝓛^R_5, start 1100110110: mover 6 of level 3, a Ξ-target, moves 10 times, every mover of levels 0-2 and every strict Ξ-descendant of 6 at most 4 times), «two consecutive doubling levels only if F(l − 1) = 0» (experiments/si/box76/inst/lower/REC_d10_tower_mu30.json, a byte copy of L-LOWER's, 𝓛^R_10, its stored start 00111111010010111010: F(0..3) = 2, 6, 14, 30), «F(l + 1) ≤ F(l) − c above a doubling level without upward options» for every c ≥ 1 (experiments/si/box76/inst/passfreeze77_d5.json, 𝓛^R_5, its stored start 1101111101: F = 2, 2, 2, 6, 6, the top pair never moving), and «the strict Ξ-descendants of the fuel targets U_l lie at levels > l» (static Ξ-graph; measured for every l in 0, …, d − 2 by experiments/si/box79/reentry_levels.py: false for l = 1, …, 8 on experiments/si/box76/inst/lower/REC_d10_tower_mu30.json, a byte copy of L-LOWER's, 𝓛^R_10, witness 1 → 11 → 3 (mover 11 of level 5 is the Ξ-target of mover 1's option 0, and 3 of level 1 is a Ξ-target of an option of 11), and for l = 1, …, 4 on experiments/si/box76/inst/lower/KILL_M2D_d6_mu13.json, a byte copy of L-LOWER's, 𝓛^R_6, witness 2 → 5 → 3 (mover 5 of level 2 is the Ξ-target of an option of mover 2 of level 1, and 3 of level 1 is a Ξ-target of an option of 5); true for l = 0 on both): each statement is about the step sequence of R104's IDEAL model (MP-LIN about max-plus recursions); DBL-EQ (b)'s window count uses one referee-originated step (REFEREE's DB-3, fixes entry 1 F-3, found independently by REFEREE-2); DATA, experiments/si/box79/dblcheck.py, CORPUS = the 63,223 runs (140,395 steps) of the 208 𝓛^R_d genomes of the frozen P-IDEAL-MOVES corpus (l-new 9995f5a2; every start for N ≤ 10, the stored start otherwise), LOWER = the 9 runs of L-LOWER 3's kill genomes from their stored starts, counts given as CORPUS / LOWER, every genome of degree 2 and width 2 (so HIT and ALT-MIN, stated at any degree, are tested only there): WINDOW-ONCE 0 violations on 577,908 / 1,736 (run, level, window, member); DBL-EQ (a) 0 on 225,647 / 72 (run, level ≥ 1), both directions, with 4,534 / 12 doubling (run, level); (b) 0 on 11,052 / 176 (run, doubling level, window, member); (c) 0 on every doubling (run, level); PASS-FREEZE 0 on the 23,317 (run, level) of CORPUS whose pair above never moves and starts split (none in LOWER); HIT 0 on 1,298,948 / 5,216 (run, mover, step); FUEL-EXACT 0 on 288,870 / 81 (run, level); ALT-MIN 0 on 577,740 / 162 (run, mover), (a) and (d) counted per (run, mover, k); TOWER-NEED's bounds on P and R 0 on 9,068 / 24 (run, doubling level, member), its moves clause through DBL-EQ (b); controls: ALT-MIN's bounds (b) and (c) minus 1 fail on 112,372 / 43 and 7,085 / 13 (run, mover), and with the key-least option taken regardless of availability HIT fails on 238,546 CORPUS (run, mover, step); MP-LIN, the sufficient condition of PASS-FREEZE and DEAD-REENTRY (static Ξ-graph; its level sets measured by experiments/si/box79/reentry_levels.py): no separate DATA; the other three DEAD instances re-run by experiments/si/box79/dead79.py; FUEL-NEED and FUEL (i), which use L-LOWER's unrefereed FEEDBACK (b), are not stated; no statement bounds T polynomially (P-IDEAL-DBL, docs/si/P-IDEAL-DBL.md with its fixes entry 1, docs/si/P-IDEAL-DBL-fixes.md; L-SI successors 41-42). G-N5-TIME stays open.

Addendum (subagent, for the Lead; does not land; written 2026-11-07T10:56:09Z by date -u). (1) FIRST FILL on line L-2 (l-si 0ea6959f, sha1
1b3dc825…), to CHECKER C133. I edited docs/agents/R119-draft.md only; no merge, no commit and no push by me; the Lead commits this file.
Re-fetch at 2026-11-07T10:56Z: l-si 0ea6959f, referee 34589c09, referee-2 1b9e3ea5, checker d7091311 (unchanged since the 10:52Z
re-fetch); local trunk HEAD ac1bc37c. (2) TITLE l. 341 = "### R119 [refereed-only] " + L-2 without its newline + ", CHECKER PASS
(docs/checker/C133.md, checker PENDING)", checked by script (chk119.py): equal, byte for byte (True); the only «### R» heading of this file;
5,750 characters, 5,888 bytes, sha1 of the heading line without its newline 3fc0ffd6bb872beae56e9388a0ce469799d4cd05; 98 «(» / 98 «)»
(L-2's 97 and the fill's), depth never negative, 0 "|". It carries L-2's «R1xx [refereed-only] » prefix (G-L, R-A). (3) SHAPE. The entry
block is l. 341-514 (python slice d[340:514]), followed by a blank line; 0 "|" in it; one «PENDING», the title's fill «checker PENDING)».
The GAPS preamble is l. 516-522; the UPDATE is l. 523 (d[522]), one line, sha1 cec3db26ff86ebe1395359bad729db2cddc0543c without newline
and unfilled (= upd119L2.txt, True), 5,930 bytes, 5,792 characters, 1,049 tokens, 97 «(» / 97 «)», 0 "|", one each of «<DATE>»,
«<HH:MM>», «<checker>», «2026-11-07» once (inside L-2's source parenthesis, G-U). A landing script slices d[340:514] for the entry and
reads d[522] for the UPDATE, with «R119», «C133», PREV = the last landed entry (R117 now, R118 if it lands first; G-P). (4) WHAT IS LEFT:
CHECKER's rulings on G-L (R-A), G-1 (R-B or R-B′), G-U (R-C and the UPDATE procedure), G-9 (i), (ii) (R-D, R-E) and the optional R-F; the
Lead's on G-7 (L41, optional R-G) and G-P (numbering if R119 lands before R118); then an L-3 by L-SI (fixes entry 2), both referees' byte
tests, and a second fill (title, line history, Data, Signatures, UPDATE rebuilt from L-3 with the controls of every UPDATE then landed).
(5) QUOTE SWEEP (chk119.py: chk118.py's rule, outermost guillemet quotes split at «…», parts of 6+ characters, whitespace-normalised, NO
docs/agents draft as a source; sources: the trunk docs at HEAD, RESULTS at 97d17f63, TARGET.md, CLAUDE.md, NOW, LEAD-STATE,
scripts/verify.sh; at 2c396f6f, f5263d5a and 0ea6959f the packet, fixes, L-1, L-2, experiments/si/check.sh and notes/L-SI.md; every box79
file of the archive, box76/tw.py and box76/pins.sha1; REFEREE's file at d7885be4 and 34589c09, REFEREE-2's at 2b425bb6, 30615935 and
1b9e3ea5 and its r2reentry.out; C122, C123, C125-C131, notes/CHECKER.md and notes/L-RED.md on claude/checker; the commit subjects cited;
my outputs): title and body 114 quotes, 110 parts, 0 not found; GAPS preamble and UPDATE 9 quotes, 7 parts, 0 not found; preface 239
quotes, 204 parts, 0 not found; this Addendum and the whole file: 0 not found (same script on the final file). Line-precise (lp119.py):
87 of 87 (source, cited lines, quote) triples of this draft found inside the cited lines (REFEREE l. 3, 11, 15-19, 23, 40, 44-45, 68, 76,
133, 158-159, 167-168, 186-191, 196, 199, 206, 209-210, 215, 218, 223-224; REFEREE-2 l. 2, 5, 18, 20, 22-24, 34, 42-43, 54-55, 64, 68-69,
123, 131, 140-145, 151, 154, 161-162, 165-166; packet l. 4-7, 19, 39-41, 56, 65-66, 90, 95, 107-108, 115, 125, 130-131, 194; fixes l. 3-4,
10-11, 26, 29, 67; C122 l. 85-88; C123 l. 83-86; DECISIONS l. 355-358; RESULTS l. 12246-12247; LEAD-STATE l. 2466, 2481; dblcheck.py
l. 37, 65, 94, 110, 131; tw.py l. 9; experiments/si/check.sh l. 1247; check79.sh l. 7; scripts/verify.sh l. 20). (6) STALE STATUS
(chk119.py): title «PENDING» 1 (the fill); body «NOT YET» 1 (REFEREE's L-1 verdict, quoted as history), «not landed» 2 (the packet's «not
landed, not refereed» for FEEDBACK (b), quoted twice), «pending», «not yet», «CANDIDATE» / «candidate», «will », «awaiting», «to come»,
«not on origin», «pushing», «second fill» 0; GAPS preamble and UPDATE 0; line 1 «NOT LANDED» 1 (R119 is not landed). Model names
outside exact quotes: 0 (two occurrences, both inside exact quotes of REFEREE-2). (7) LANDING SIMULATION (sim119.py: sim117.py's parts() and land(),
unchanged, on in-memory copies of the local trunk ac1bc37c's RESULTS 68d3d046… and GAPS 36179c47…; R117 landed, R118 not). Case A, R119
directly: a pure insertion (True) directly before «**Erratum E-1**», the prefix and every line after the insertion byte-unchanged (Errata,
Note E-3, Dead ends with DE37): True; RESULTS 14,249 → 14,424 lines (+175); R117 l. 13,362; R119 at l. 13,607-13,780, blank l. 13,781,
«**Erratum E-1**» to l. 13,782, E-2 13,795, Note E-3 13,823, Dead ends 13,854, DE37 from l. 14,392 (the last row); order R110-R117, R119,
E-1, E-2, E-3, Dead ends: True. GAPS: only l. 11 changes, the closing " |" replaced by " " + the filled UPDATE + " |": True; "|" on l. 11
76 → 76; «UPDATE 2026-» 52 → 52 plus one head with the simulation year 2099 after R117's: True; R119's UPDATE last: True; 23 → 23 lines.
Case B, a stand-in R118 first (docs/agents/R118-draft.md, sha1 217ac0cc…, block d[363:577], UPDATE fb37efeb…), then R119: both pure
insertions (True, True); R118's block byte-unchanged by R119's insertion (True); RESULTS 14,249 → 14,464 → 14,639 lines; R118 l. 13,607,
R119 l. 13,822-13,995, blank 13,996, E-1 13,997, E-2 14,010, Note E-3 14,038, Dead ends 14,069, DE37 from 14,607; GAPS "|" 76 → 76, R117,
R118, R119 in that order, R119 last: True. Fill values used only for the simulation: R118 2099-01-05, R119 2099-01-06, <HH:MM> 00:00,
<checker> 0000000. (8) UPDATE (upd119.py, a copy of upd118.py l. 1-80 and l. 104-152 with new Parts C1, C2, D, E): controls R97-R116
rebuilt from their lines and compared with GAPS l. 11, True ×20; the R117 control (LANDED) run117() on L-4 filled with the landed stamp
2026-11-07 10:30 d7091311, = its GAPS l. 11 segment, = R117-draft.md's UPDATE line and = r117b/upd117L4.txt with the same fill, unfilled
sha1 = C130 §5's b4d74e09… (True ×4; the last UPDATE on l. 11 is R117's: True); the R118 control (NOT landed) run118() on L-3 =
R118-draft.md's UPDATE line = r118/upd118L3.txt, sha1 fb37efeb… (True ×3); R119 built (G-U), = the direct build (True); the filled R119
UPDATE appended after R117's, and after a filled stand-in R118, keeps 76 "|" on l. 11 (True, True). With R-A, R-D, R-E, R-C, R-B (each old
string once in L-2 and once in the running line, script; R-C's old string is not in the UPDATE, since the UPDATE opens the DATA
parenthesis): L-2 + proposals sha1 ba7ffc523427d98020b1715a835d78b60cc5ce31 (6,037 bytes, 99 / 99, one " — "), its UPDATE by R116's
procedure unchanged f65f43290e820d263234e98abddf014a1953df04 (6,069 bytes, «R1xx» 0). (9) NOT VERIFIED / NOT DONE: the referees' tools
not re-run (their files and logs read; my rel119.py and static119.py make the same byte test and level-set measurement); scripts/verify.sh
and the full experiments/si/check.sh not run (check79.sh only); box76/tw.py's Sim not read beyond load_corpus, is_lr and the NEG switch
(the IDEAL step is taken from R104 and both referees' replays on their own simulators); dead79.py's XCHK cross-check with L-NEW's Gen not
run; wiring79.py's output not compared with any line clause (not cited in L-2); R-B′, R-F and R-G not built into a line or UPDATE; no
Oink run (L-2 cites no Oink check). (10) Scratch:
/tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad/r119/ (tools/rel119.py, rel119.out;
arch0ea/ = git archive of 0ea6959f, blk79.out, blk.start, blk.end, blk.rc; tools/static119.py, static119.out; tools/prem119.py,
prem119.out; tools/upd119.py, upd119.out, upd119L2.txt, props119.tsv, L2prop.txt, upd119prop.txt; tools/chk119.py, chk_final.out;
tools/lp119.py, lp_final.out; tools/sim119.py, sim_final.out; tools/assemble119.py, parts/; fetch.out; R119-p1.md, R119-p2.md,
R119-draft.md).

Addendum 2 (subagent, for the Lead; does not land; written 2026-11-07T15:02:42Z by date -u). (1) SECOND FILL on line L-3 (l-si 610897dd,
sha1 845ffdc9…), to CHECKER C133 Add. 1. I edited docs/agents/R119-draft.md only; no merge, no commit and no push by me (a Lead push was
running); the Lead commits this file. (2) TITLE l. 426 = "### R119 [refereed-only] " + L-3 without its newline + ", CHECKER PASS
(docs/checker/C133.md, checker PENDING)", checked by script (chk119b.py): equal, byte for byte (True); the only «### R» heading of this
file; 6,096 characters, 6,245 bytes, sha1 of the heading line without its newline dadb704e298f6349d8b1dbad95f1ccbf18eca06b; 102 «(» / 102
«)» (L-3's 101 and the fill's), depth never negative, 0 "|"; «R1xx» 0 times, «[» once (the ledger tag «[refereed-only]»). (3) SHAPE. The
entry block is l. 426-659 (python slice d[425:659]), followed by a blank line; 0 "|" in it; one «PENDING», the title's fill «checker
PENDING)». The GAPS preamble is l. 661-666; the UPDATE is l. 667 (d[666]), one line, sha1 074e3c05060c7adcd7b20e5560674bdf12d8b2fa without
newline and unfilled (= upd119L3.txt, True), 6,199 bytes, 6,052 characters, 1,092 tokens, 100 «(» / 100 «)», 0 "|", one each of «<DATE>»,
«<HH:MM>», «<checker>», «2026-11-07» 0 times, «R1xx» 0 times. A landing script slices d[425:659] for the entry and reads d[666] for the
UPDATE, with «R119», «C133», PREV = «R118» (landed at the local trunk 478d0bd9) and the assertion that the last UPDATE on GAPS l. 11 is
R118's «UPDATE 2026-11-07 14:48Z: RESULTS R118 (P-N5-XICYC; CHECKER C132 af92b846)». (4) WHAT IS LEFT TO FILL: only the title's «checker
PENDING)» and the UPDATE's three placeholders, at landing. No referee item is open on this packet. Before landing the Lead merges
claude/referee-2 (37c733e2, REFEREE-2's Addendum 2, is NOT an ancestor of the local trunk 478d0bd9 or of origin trunk ebf59a34); 610897dd
(l-si), 07a950ae (referee) and 8f6d03bc (checker) are ancestors of both. (5) THE UPDATE, TOKEN DIFF L-3 → UPDATE (upd119b.py: difflib on
the whitespace tokens of L-3 without its newline, 1,093 tokens, and of the unfilled UPDATE, 1,092 tokens): 14 hunks, 35 tokens out, 34 in,
every other token equal and in order. (i) Head inserted: «UPDATE <DATE> <HH:MM>Z: RESULTS R119 (P-IDEAL-DBL; CHECKER C133 <checker>)
[refereed-only] LANDED:» (11 tokens). (ii) The eight labels move from before their clauses to behind them, «; » kept between clauses (9
hunks): «(MP-LIN)» deleted before its clause; «mean; (WINDOW-ONCE)» → «mean (MP-LIN);», «l-window; (DBL-EQ)» → «l-window (WINDOW-ONCE);»,
«false; (PASS-FREEZE)» → «false (DBL-EQ);», «F(l); (HIT)» → «F(l) (PASS-FREEZE);», «moves(y); (FUEL-EXACT)» → «moves(y) (HIT);», «moves;
(ALT-MIN)» → «moves (FUEL-EXACT);», «X); (TOWER-NEED)» → «X) (ALT-MIN);», «1)/2;» → «1)/2 (TOWER-NEED);»; the unlabelled DEAD clause «;
and four statements are false (DEAD, instances machine-replayed): …» stays last, behind (TOWER-NEED) (R111's / R116's DEAD-clause step).
(iii) «both) (2026-11-07) —» → «both):» (the date parenthesis and the dash become «: »). (iv) «G-N5-TIME stays OPEN; not M3, not a step-4
pass, not a TARGET.md claim (DATA,» → «DATA,» (the two scope sentences dropped, the DATA parenthesis opened). (v) «polynomially)» →
«polynomially» (the DATA parenthesis's «)» dropped). (vi) «41-42)» → «41-42). G-N5-TIME stays open.» (the source parenthesis kept, the
final sentence appended). KEPT: the 33 tokens of scope words «each statement is about the step sequence of R104's IDEAL model (MP-LIN
about max-plus recursions); DBL-EQ (b)'s window count uses one referee-originated step (REFEREE's DB-3, fixes entry 1 F-3, found
independently by REFEREE-2)», between «: » and «; DATA, », because R116's procedure (sentinel_build111 with its default drops) removes
only «; G-N5-TIME stays OPEN» and «; not M3, not a step-4 pass, not a TARGET.md claim»; R116's landed UPDATE keeps its own scope words the
same way («a STRUCTURE / EQUIVALENCE statement inside the IDEAL model; bounds nothing polynomially;», GAPS l. 11), and R118's keeps its
L41 sentence («are referee-originated», GAPS l. 11). NOTE N-U for CHECKER: C133 §5 lists the expected transformation with «the scope tail
up to «(DATA, » dropped, with «(DATA, » opened and its «)» dropped;» (l. 81). Read literally, that drops these 33 tokens too, which R116's
procedure, «unchanged» (l. 76), does not do. I built the UPDATE by the procedure as named; if CHECKER means the scope words to go, the
right UPDATE would be this one with «each statement … REFEREE-2); » removed after «both): » (not built). Cross-checks: = the direct build
(True); = the first fill's upd119prop.txt (f65f4329…, L-2 with R-A, R-D, R-E, R-C, R-B by the same procedure) with R4's sentence «; DBL-EQ
(b)'s window count uses one referee-originated step (REFEREE's DB-3, fixes entry 1 F-3, found independently by REFEREE-2)» inserted after
«(MP-LIN about max-plus recursions)» (True). (6) CONTROLS (upd119b.py on GAPS at 478d0bd9, sha1 ac63d1a7…): R97-R116 rebuilt from their
lines, each equal to its GAPS l. 11 segment, True ×20; R117 (landed 2026-11-07 10:30Z, d7091311) and R118 (landed 2026-11-07 14:48Z,
af92b846) rebuilt from their L-4 lines and filled with their GAPS l. 11 stamps, each equal to its segment, to its draft's UPDATE line and
to its scratch UPDATE file with the same fill, unfilled sha1 = C130 §5's b4d74e09… and C132 §5's d4acaeef… (True ×4 each); all controls
True ×22; the last UPDATE on l. 11 is R118's (True). (7) QUOTE SWEEP (chk119b.py: chk119.py's rule, outermost guillemet quotes split at
«…», parts of 6+ characters, whitespace-normalised; its sources plus, at this fill, the P-IDEAL-DBL files, experiments/si/check.sh and
notes/L-SI.md at 610897dd, box79 from the archive of 610897dd, REFEREE's file at 07a950ae, REFEREE-2's at 37c733e2 with bt_l3.py and
bt_l3.out, C133 at 8f6d03bc, C132 at the checker head, RESULTS and GAPS at 478d0bd9, the commit subjects cited, the first fill's outputs
and mine; no docs/agents draft as a source): title and body 152 quotes, 148 parts, 0 not found; GAPS preamble and UPDATE 7 quotes, 6
parts, 0 not found; SECOND FILL section 39 quotes, 29 parts, 0 not found; the preface (SECOND FILL section and FIRST FILL text) 278
quotes, 233 parts, 0 not found; the first fill's Addendum 34 quotes, 24 parts, 0 not found; this Addendum and the whole file: 0 not found
(same script on the final file). Line-precise (lp119b.py): 27 of 27 (source, lines, quote) triples of this fill found inside the cited
lines (REFEREE l. 226, 233, 236, 237, 239-240, 240, 241, 243, 245, 249; REFEREE-2 l. 54-55, 168, 172-173, 181, 185; fixes l. 70, 70-71,
94-95; C133 l. 15, 16, 16-17, 29, 36-37, 38, 40, 76-77, 81). (8) STALE STATUS (chk119b.py) in the title and body: «PENDING» 1 (the title's
fill «checker PENDING)»), «pending» 0, «not yet» 0, «Not yet» 0, «NOT YET» 1 (REFEREE's L-1 verdict, quoted in Object, history),
«CANDIDATE» / «candidate» 0, «will » 0, «awaiting» 0, «to come» 0, «not landed» 2 (the packet's «not landed, not refereed» for FEEDBACK
(b), quoted in Object and Not signed), «second fill» 1 (Data: the re-run «at the second fill»); first-fill flags in the title, body, GAPS
preamble and UPDATE: «G-L», «G-U», «G-7», «G-9», «G-P», «draft G-», «which carries every proof», «L-2 itself» 0 each; «R1xx» 0 in the
title and the UPDATE, 2 in the body (The RESULTS line and Fixes, each saying that R1 removes it); GAPS preamble and UPDATE: «second fill»
1 (R118's UPDATE is the last on l. 11 at this second fill), all else 0; SECOND FILL section: all 0; line 1: «NOT LANDED» 1 (R119 is not
landed; as R118's draft). In L-3, the title and the UPDATE R1's and R2's old strings occur 0 times; R5's and R6's once each, inside their
own new strings; R3's new text occurs 0 times verbatim (R4 edits inside it) and R4's old string once, inside R4's new string. (9) WORD
DIFF 3fb40db1 → this file (wd119b.py, difflib on lines, then on whitespace tokens, Addendum 2 left out): 11 line regions, 87 token hunks
(180 tokens out, 3,121 in), every region in the list of changes of the SECOND FILL section. (10) LANDING SIMULATION (sim119b.py:
sim117.py's parts() and land(), unchanged, on in-memory copies of the local trunk 478d0bd9's RESULTS 576a89b7… and GAPS ac63d1a7…; the
working tree's two files are equal to them; R118 landed, so one case): pure insertion of 235 lines (the entry block with "checker
PENDING)" filled, plus one blank line) directly before «**Erratum E-1**», after R118's landed block: True; RESULTS l. 1 to the end of
R118's block byte-unchanged and every line after the insertion byte-unchanged (Errata, Note E-3, Dead ends with DE37): True; RESULTS
14,521 → 14,756 lines; R118 at l. 13,607, R119 at l. 13,879-14,112, blank l. 14,113, «**Erratum E-1**» to l. 14,114, Erratum E-2 14,127,
Note E-3 14,155, Dead ends 14,186, DE37 l. 14,724; order R110-R119, E-1, E-2, E-3, Dead ends: True. GAPS: only l. 11 changes, its closing
" |" replaced by " " + the filled UPDATE + " |": True; "|" on l. 11 76 → 76; «UPDATE 2026-» 53 → 53 plus one head with the simulation year
2099, after R118's and the last: True; 23 → 23 lines. Fill values used only for the simulation: <DATE> 2099-01-06, <HH:MM> 00:00,
<checker> 0000000. (11) FIRST-FILL RECORD (rec119b.py): 3fb40db1's l. 2-340 (FIRST FILL to (14) and the blank line) = this file's l.
87-425, directly before the title (True); 3fb40db1's Addendum (1)-(10), l. 525-584 = this file's l. 669-728, directly after the UPDATE and
a blank line (True). (12) NOT VERIFIED / NOT DONE: the referees' tools not re-run (bt_l3.py, bt_l3.out and both addenda read; my
l3rel119.py makes the same byte test); scripts/verify.sh and the full experiments/si/check.sh not run (check79.sh only); static119.py and
dblcheck.py's counters not re-run or re-read at this fill (fixes entry 2 changes the line only, git diff 0ea6959f 610897dd names no tool,
output, instance or corpus file but check79.sh, mkL3.py, mkfix2.py, the C133 copy and pins.sha1, and check79.sh reproduced every output
byte for byte); mkfix2.py not read (the fixes file it wrote is read in full); C133's own scripts not re-run; the R-F variant and the N-U
variant of the UPDATE not built; no Oink run (L-3 cites no Oink check). (13) NOTES for the CHECKER, no verdict affected: D-7 REFEREE §C
add. 1 l. 239-240 places REFEREE-2's own DB-3 step at «docs/referee-2/R2-P-IDEAL-DBL.md l. 53-54»; at 2b425bb6 and at 37c733e2 the quoted
words «under (a), 1 ∉ B (Φ(0) = 2 ≠ 0), so there are exactly F(l − 1) + 1 windows» are at l. 54-55 (lp119b.py), as this draft's L41 bullet
cites; a one-line offset, the attribution is right. D-8 REFEREE-2 Addendum 2 (committed 13:01:16Z, heading «2026-11-07 13:0xZ by date -u»)
says at l. 169 its objects are «equal to the Lead's relay 13:02Z», a stamp one minute after its commit time (the R117 D-6 / R118 D-8
pattern). D-9 fixes entry 2's heading «Lead 12:08Z»: C133's commit 8f6d03bc is 12:05:45Z, 610897dd 12:38:17Z; consistent. D-10 R3's new
text does not occur verbatim in L-3 because R4 edits inside it (REFEREE §C add. 1 l. 234-235; REFEREE-2's bt_l3.out «R3 old in current
text 1, new in L-3 0»); R5's and R6's new strings contain their old strings, so those old strings occur once in L-3, inside their new
strings. D-11 C133 §4 re-ran check79.sh from 0ea6959f; git diff 0ea6959f 610897dd changes check79.sh only by the two mkL3.py lines, and
this fill re-ran it from 610897dd. D-12 N-U (item (5)). Scratch:
/tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad/r119b/ (tools/l3rel119.py, l3rel119.out;
arch610/ = git archive of 610897dd (docs/si, experiments/si, scripts, notes/L-SI.md), blk79.out, blk.start, blk.end, blk.rc;
tools/upd119b.py, upd119b.out, upd119L3.txt; tools/prem119b.py, prem119b.out; tools/edit119b.py, parts/secondfill.txt,
parts/addendum2.raw, filltime.txt, addtime.txt, fetch2.out; tools/chk119b.py, chk_p1.out, chk_final.out; tools/lp119b.py;
tools/sim119b.py, sim_p1.out, sim_final.out; tools/rec119b.py; tools/wd119b.py; R119-draft-3fb40db1.md, R119-p1.md, R119-draft.md).
