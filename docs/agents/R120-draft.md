# Draft RESULTS R120 (Lead; first fill 2026-11-07T16:28:58Z by date -u (subagent) on P-TOWER-FUEL line L-2, docs/lower/P-TOWER-FUEL-line-L2.txt, l-lower 740f6c79, sha1 d866ca50b0a0372efd9e93a2db0410801b3ddc15 (draft sha1 752f9531, CHECKER C134 23871f48: FAIL E-1..E-4); SECOND FILL 2026-11-07T19:43:08Z by date -u (subagent) on P-TOWER-FUEL line L-3, docs/lower/P-TOWER-FUEL-line-L3.txt, l-lower 4f25ae6f, sha1 7328e67345e1bb6a8605ccfa4f406d1020eabfdb) — to CHECKER C134 Add. 1 — NOT LANDED; goes after R119 (LANDED at the local trunk 2f98d985), before Erratum E-1 — LANDED in RESULTS 2026-11-07 21:05Z (CHECKER C134 0c816917 PASS), after R119, before Erratum E-1
SECOND FILL (2026-11-07T19:43:08Z by date -u, subagent; for CHECKER C134 Add. 1). Read at the origin heads of a first fetch (not
stamped; before 2026-11-07T19:29:33Z, the first date -u of this fill) and of a second fetch at 2026-11-07T19:36:40Z-19:36:41Z (git fetch
of claude/l-lower, claude/referee, claude/referee-2, claude/checker, claude/vibrant-johnson-nxvvxo; I merged, committed and pushed
nothing and edited docs/agents/R120-draft.md only): l-lower 4f25ae6f (4f25ae6f1706f8e994ec92c8495b6b0faa4caadc, 2026-11-07T18:44:07Z,
«L-LOWER 7: P-TOWER-FUEL fix round 2 (CHECKER C134 R1-R4): fixes entry 2, line L-3 (7328e673, 4,908 B), check pins L-3 and SL41's 119
j-windows», the commit of record and the branch head at the first fetch; git diff 740f6c79 4f25ae6f names, for P-TOWER-FUEL,
docs/lower/P-TOWER-FUEL-fixes.md (entry 2 appended), the new docs/lower/P-TOWER-FUEL-line-L3.txt, the new
experiments/lower/l5/mkL3_tf.py and mkfix2_tf.py, and experiments/lower/l5/p_tower_check.py (5 lines added: the L-3 pin and the
assertion of SL41_d28's 119 j-windows), and otherwise BOX L6 files (docs/lower/L6-supplier.md, experiments/lower/l6/), notes/L-LOWER.md
and docs/agents/handover-checks/L-LOWER.md; the packet, L-1, L-2, experiments/lower/check.sh and the two instance files are byte-equal
at 740f6c79 and 4f25ae6f, by script). At the second fetch the l-lower head is 8cc6ebc6 (8cc6ebc6cbc31f3a569e8763d5ea6f77adf02bff,
2026-11-07T19:11:16Z, «L-LOWER 7: BOX L7 round 1 (RC-PLATEAU read: survives; WINDOW-CAP, PULSE-TRIGGER, GREEDY-COMPLETE; exact rank
solver; COUPLING-UP and one-read XOR data)»): git diff 4f25ae6f 8cc6ebc6 names docs/lower/L7-design.md, experiments/lower/l7/,
notes/L-LOWER.md and experiments/lower/check.sh (two lines appended, the BOX L7 block); no P-TOWER-FUEL file and nothing under
experiments/lower/l3, l4 or l5 changes (git diff --quiet). referee af752251 (af752251cf6a8afaf25073a960189b2281d9cbe1,
2026-11-07T19:08:39Z, «REFEREE 27: R-P-TOWER-FUEL §C add. 1 (L-3 MATCHES; C134 R1-R4)», the branch head; docs/referee/R-P-TOWER-FUEL.md
§C add. 1 l. 254-273, with scratch/tf_l3.py, tf_logs/l3.out and tf_logs/lane_check_4f25ae6f.out; the file 273 lines, 25,739 bytes, sha1
477afd8662659c859e93d6ade0bcc64176ebcaff; its l. 1-252 = d39fc93a's file, by script), referee-2 e72661d0
(e72661d01602ab9c629cd1fe01676c98a7ae15ec, 2026-11-07T19:08:25Z, «REFEREE-2 succ. 31: P-TOWER-FUEL Add. 2 (L-3 MATCHES, C134 R1-R4)»,
the branch head; docs/referee-2/R2-P-TOWER-FUEL.md Addendum 2 l. 225-245, with R2-P-TOWER-FUEL/bt_l3.py, bt_l3.out and
lanecheck_4f25ae6f.out; the file 245 lines, 23,277 bytes, sha1 525926693843390613700afed28f69d34a1022bf; its l. 1-223 = fa010874's file,
by script), checker 23871f48 (23871f4806e2670ccfb04d32fc8664e8ede9bc04, 2026-11-07T18:05:38Z, «CHECKER C134: REFEREE §3 line range of
the repair (l. 107-112)», the branch head; docs/checker/C134.md was first committed at 85e4cdea, 18:05:28Z, and 23871f48 changes one
line of it, E-2's REFEREE line range; at 23871f48 it has 105 lines, 11,360 bytes, sha1 f6a841439fc122a9d8d38a8abf47227139043a09).
referee, referee-2 and checker are unchanged at the second fetch. 4f25ae6f, 8cc6ebc6, af752251, e72661d0 and 23871f48 are NOT ancestors
of the local trunk c8bdafe2 or of origin trunk 762c2184 (git merge-base --is-ancestor); 740f6c79, d39fc93a and fa010874 are. The Lead
merges claude/l-lower, claude/referee and claude/referee-2 before landing.
Trunk: local HEAD c8bdafe2 (2026-11-07T19:05:32Z, «Lead: roster L-NEW 61; restart scores; log; resume point»; origin trunk 762c2184 its
parent). docs/agents/R120-draft.md at HEAD is the first fill, sha1 752f9531453c24a4dc7089ea2c286e7e1641efbc (committed at 2067739b,
2026-11-07T17:13:56Z; C134's object). RESULTS at HEAD: sha1 b6038515848b9c0d3217657f8dce7d099d805c6a (= RESULTS at 2f98d985, R119's
landing), 14,756 lines; «### R118» l. 13607, «### R119» l. 13879, «**Erratum E-1**» l. 14114, «**Erratum E-2**» l. 14127, «**Note E-3**»
l. 14155, «## Dead ends (kept;» l. 14186. GAPS at HEAD: sha1 3825c35d868bb5ee5bc34c9b6f046c49634b31e5 (= GAPS at 2f98d985), 23 lines, l.
11 76 "|", 54 «UPDATE 2026-», the last R119's «UPDATE 2026-11-07 16:38Z: RESULTS R119 (P-IDEAL-DBL; CHECKER C133 b86962ae)». «R120»,
«C134» and «P-TOWER-FUEL» occur 0 times in RESULTS and in GAPS.
New sources: CHECKER C134 (85e4cdea, 2026-11-07T18:05:28Z; read at 23871f48): «Verdict: FAIL (E-1 to E-4; one L-3 with four
replacements, §5)» (l. 15); «All four are the drafter's flags with its exact strings: G-1 (R-B), G-7 (R-G), G-U (R-U) and G-9 (i)
(R-S).» (l. 16); «R-C is not taken (N-1).» (l. 17); E-1..E-4 are the first fill's G-1, G-7, G-U and G-9 (i), fixed by R1 (R-B), R2
(R-G), R3 (R-U) and R4 (R-S) (l. 21-37); N-1 (l. 38-40); on G-U: «With R3, L-3 has the landed words and R105's procedure applies
unchanged.» (l. 31); G-P: R120 after R119, its UPDATE after R119's (l. 46); everything else PASS (§4: p_tower_check.py re-run from git
archive 2a89b7f2, the DATA clause by clause against the counter code, the instrumented counts, the statements, the premises, the quotes,
the TARGET.md diff); §5: L-3 (sha1 7328e673…, 4,908 bytes) and its UPDATE (sha1 17cba597…, 4,941 bytes), and the second-fill list (l.
95-96). Fixes entry 2 (docs/lower/P-TOWER-FUEL-fixes.md l. 95-144 at 4f25ae6f, L-LOWER successor 7, written by
experiments/lower/l5/mkfix2_tf.py; the file 144 lines, 15,426 bytes, sha1 c99bfd3acb8e062fd7b05fec98a5898a7ac883d2, its l. 1-93 = entry
1's file 0902efb9…, by script); line L-3 (docs/lower/P-TOWER-FUEL-line-L3.txt, 4f25ae6f, the file's only commit);
experiments/lower/l5/mkL3_tf.py (32 lines), mkfix2_tf.py (52 lines) and p_tower_check.py (177 lines; new l. 12-13, 38, 85-86) at
4f25ae6f; REFEREE's §C add. 1 (its own byte test; R1-R4 read in meaning; R4 by its own replay; l. 273 its verdict, quoted in the entry)
and REFEREE-2's Addendum 2 (its own bt_l3.py; R2, R4, R3 and R1 read in meaning; l. 245 its verdict, quoted in the entry).
Checks run at this fill (scratch /tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad/r120b;
nothing written into the repository but this file). (a) l3rel120b.py: L-3 at 4f25ae6f is sha1 7328e67345e1bb6a8605ccfa4f406d1020eabfdb,
4,908 bytes, one line with its newline, 4,758 characters, 860 tokens, 82 «(» / 82 «)», depth never negative, final depth 0, 0 "|", one «
— », «gauntlet» 0 times, «step-4 pass» once, «[» 3 times; byte-equal at 8cc6ebc6; R1-R4 parsed from C134 §5 at 23871f48 (l. 80-88,
wrapped lines joined with one space) and from fixes entry 2 §2 (its old / new strings, l. 126-135): the two lists are equal (True); they
are the first fill's R-B, R-G, R-U and R-S in that order (True ×4, parsed from draft 752f9531 at 2067739b); each old string once in L-2
and once in the running line (R3's, after R2, once, inside R2's new text); L-2 + R1-R4 in C134's order = L-3 (True); each new string
once in L-3 (R2's with R3 applied); token diff L-2 → L-3 5 hunks (5 tokens out, 51 in), each inside one of R1-R4. mkL3_tf.py (from the
archive of 4f25ae6f) re-run on C134 at 23871f48 and on L-2: rc 0, its output cmp-equal to L-3; mkfix2_tf.py re-run on C134, that L-3 and
a copy of the fixes file at 740f6c79 (0902efb9…): rc 0, the result cmp-equal to the fixes file at 4f25ae6f (c99bfd3a…). (b)
experiments/lower/check.sh from a git archive of 4f25ae6f (docs/lower, experiments, scripts), 2026-11-07T19:29:33Z-19:29:46Z, rc 0, 54
output lines, «pins OK: 5 files», «SL41_d28: 119 j-windows at j = 1..5 (3, 7, 15, 31, 63)», «P-TOWER-FUEL CHECK PASS»; against the first
fill's output (f62faf37) exactly two lines differ, «pins OK: 4 files» → «pins OK: 5 files» and the new SL41 line; the counters line is
the same. Again from a git archive of 8cc6ebc6, 2026-11-07T19:36:55Z-19:37:07Z, rc 0, 58 output lines: the same 54 lines, then the BOX
L7 block («L7 CHECK PASS»). (c) upd120b.py (r120/tools/upd120.py l. 1-243, Parts A-D, unchanged; its Parts E-G replaced by the R120
build on L-3): the controls R97-R116 rebuilt from their lines and compared with GAPS l. 11 at c8bdafe2, True ×20; R117, R118 and R119 as
landed (filled with their GAPS l. 11 stamps 2026-11-07 10:30 d7091311, 14:48 af92b846 and 16:38 b86962ae), each = its GAPS segment (True
×3), = its draft's UPDATE line filled the same way, with the unfilled sha1s b4d74e09… (C130 §5), d4acaeef… (C132 §5) and 074e3c05…
(R119-draft.md d[666]) (True); all controls True ×23; the last UPDATE on l. 11 is R119's (True). R120 rebuilt on L-3 by R105's
procedure, unchanged (C134 E-3): sha1 17cba597ebbf57e12dce1f328cc2ccc6a0865ea3 (no newline, unfilled), 4,941 bytes, 81 «(» / 81 «)», 0
"|", one each of «<DATE>», «<HH:MM>», «<checker>», «step-4 pass» 0 times (dropped, as in R105-R119); = C134 §5's sha1 and bytes (True);
= the direct build (True); = the first fill's UPDATE fba98779… with R1, R4 and R2's sentence after «are not covered», before «; DATA: »
(True; C134 §5's description); = the first fill's upd120prop.txt (9896971b…) with R4 (True); token diff L-3 → UPDATE 12 hunks, 31 tokens
out, 30 in (the 12 hunks of C134's G-U ruling, with «not a step-4 pass» in place of «not a gauntlet step»); R111's sentinel_build111
fails on L-3, as on L-2 (the «(DATA: » form); the filled UPDATE inserted after R119's, before the row's closing « |», keeps 76 "|" on l.
11, R120's UPDATE last (True). (d) prem120b.py: RESULTS at c8bdafe2; L-3's premise labels (RESULTS R104, R105, R110, R113) each name a
landed «### R» entry; the 3 RESULTS quote parts of packet §1 (ENC in two parts, ALIGN) found in the landed titles of R105 and R113, 0
not found («signed, not landed» is not a quote of RESULTS, as at the first fill); L-3 itself quotes nothing. (e) chk120b.py (title,
block, UPDATE, quote sweep, stale grep), lp120b.py (line-precise quotes), sim120c.py (landing simulation), rec120b.py (first-fill record
unchanged): Addendum 2.
C134's E-items, resolved in L-3 (string checks by script on L-3, l3rel120b.py and chk120b.py): E-1 (G-1, source note; the C122 E-3 /
C132 E-2 / C133 E-2 class) by R1 = R-B: L-3 ends «(P-TOWER-FUEL, docs/lower/P-TOWER-FUEL.md with its fixes entry 1,
docs/lower/P-TOWER-FUEL-fixes.md; L-LOWER successors 5-6)». E-2 (G-7, L41; Lead ruling) by R2 = R-G: «the proof of record of
CROSS-ECONOMY's sign-change clause is referee-originated (REFEREE R-P-TOWER-FUEL §3, restated in P-TOWER-FUEL's fixes entry 1 §1;
REFEREE-2's own repair is a second route), signed by both referees» once in L-3, in the scope tail before «; G-N5-TIME stays OPEN». E-3
(G-U, scope words; C134's ruling on the UPDATE procedure) by R3 = R-U: «not M3, not a step-4 pass, not a TARGET.md claim» once in L-3,
«gauntlet» 0 times; R105's procedure runs on L-3 unchanged ((c)). E-4 (G-9 (i), I-FUEL's unit and set) by R4 = R-S: «meets PULSE, GAP ≥
7 − j at levels 1-5 (unit = j-window; set = all 119 of them) while» once in L-3; «(unit = j-window; set = all 119 of them)» now twice in
L-3 (I-ROOM's clause and I-FUEL's); the 119 are asserted by p_tower_check.py since 4f25ae6f ((b)). Each new string once in L-3. The
first fill's optional R-C is not taken (C134 N-1); its note G-9 (ii) is history.
NOTES at this fill (for CHECKER; no line change proposed):
- N-S, THE SOURCE NOTE'S SUCCESSORS (CLEAN by precedent, in my reading). L-3's note names «L-LOWER successors 5-6»; fixes entry 2 and
  L-3 are L-LOWER successor 7's («L-LOWER successor 7», fixes l. 95). Entry 2 carries no proof and changes no statement («no statement,
  proof, definition, instance or counter changes», fixes l. 101), and R1 is C134 §5's exact string. Precedents on trunk: R118's note
  «with its fixes entries 1-2, docs/new/P-N5-XICYC-fixes.md; L-NEW successor 59» names neither its line-only entry 3 nor successor 60,
  who wrote it (R118-draft.md, Object); R119's note names fixes entry 1 only, not its line-only entry 2.
- D-6, STAMPS (history, no verdict affected). REFEREE-2's Addendum 2 heading reads «2026-11-07 19:1xZ by date -u» and its object line
  «equal to the Lead's relay 19:09Z» (l. 225-226); the commit e72661d0 is dated 2026-11-07T19:08:25Z (author and committer date),
  earlier than both times; a partial stamp, the class of the first fill's D-2 (REFEREE-2's «15:5xZ by date -u»). REFEREE's heading «date
  -u at writing 2026-11-07T19:08Z» agrees with af752251 (19:08:39Z).
- D-7, INPUTS AND PINS (the C116 G-3 class; note). mkL3_tf.py and mkfix2_tf.py read a byte copy of docs/checker/C134.md that is not
  committed at 4f25ae6f (git ls-tree: no C134 file; notes/L-LOWER.md l. 5-7 names the git show command that makes it); L-3 itself is
  pinned by p_tower_check.py (l. 38), and my re-runs of mkL3_tf.py and mkfix2_tf.py on C134 from claude/checker 23871f48 give L-3 and
  the fixes file at 4f25ae6f ((a)). The packet and the fixes file are still not pinned by the block (first fill G-12); C116 l. 67: «NOT
  required before landing.».
Changes at this fill, and nothing else: line 1 (the header); this section; the title (L-3); in the entry: Object (4f25ae6f; two fixes
entries; L-3 the line of record, its line history, the L-3 verdicts of both referees), Claims signed (the L-3 round), The RESULTS line
(L-3; what R1-R4 change), L41 and L43 (L-3's scope tail, R2), Fixes (header, the entry-2 bullet with the E-item resolution, the closing
bullet), Referee strengthening (iii) (new), Honest limits (viii) (new), Data (4f25ae6f; the L-3 pin and SL41's 119; the re-run at this
fill and C134's), Signatures (REFEREE §C add. 1, REFEREE-2 Addendum 2, the lane commit 4f25ae6f), INDEPENDENCE (the L-3 wording and
round), TARGET.md diff (L-3's scope words); the GAPS preamble (built from L-3) and the UPDATE (rebuilt from L-3); Addendum 2 (new). The
FIRST FILL text below (from "FIRST FILL (this text)" to (14)) and the Addendum (1)-(10) are kept byte-unchanged as the record of draft
752f9531 on L-2 (rec120b.py): where they call L-2 the title line or the current line, raise G-1, G-7, G-U, G-9 (i)-(iii), G-0 or G-P,
propose R-B, R-G, R-S, R-C or R-U, give R119's landing as an event during that fill, or give the first fill's line numbers, counts,
placement and UPDATE sha1 (fba98779…), they describe draft 752f9531 at 16:42Z; C134 ruled G-1, G-7, G-U and G-9 (i) as E-1..E-4 (fixed
by R1-R4 = R-B, R-G, R-U, R-S), did not take R-C (N-1), ruled the UPDATE procedure (G-U: R105's, unchanged, once R3 is applied) and kept
the placement after R119 (G-P); the entry block now follows L-3.
FIRST FILL (this text). Read at the origin heads fetched at 2026-11-07T16:19Z and again at 16:28Z (git fetch of claude/l-lower,
claude/referee, claude/referee-2, claude/checker, claude/vibrant-johnson-nxvvxo; the same heads both times; I merged, committed and pushed
nothing and edited docs/agents/R120-draft.md only): l-lower f62faf37 (f62faf370179ade80f1953ae40121ad51441e824, 2026-11-07T15:50:53Z,
«L-LOWER 6: notebook resume point (duty round 1 done, milestone reported)», the branch head; git diff 740f6c79 f62faf37 names only
notes/L-LOWER.md, so the packet, L-1, L-2, the fixes, experiments/lower/ and check.sh are those of 740f6c79
(740f6c798860c24db35f12c5e19cac196b9b1f9b, 2026-11-07T15:26:05Z, L-LOWER successor 6's fix round 1, the commit of record; byte-equal at
both, by script), referee d39fc93a (d39fc93ae559a9ea03af71b060011c8ed0fdcd24, 2026-11-07T15:53:22Z, REFEREE successor 27's §C of
docs/referee/R-P-TOWER-FUEL.md; the file 252 lines, 23,831 bytes, sha1 acbfe4f433cda5869c4c6a0fc03303cb6bac89f1; its l. 1-211 = 807984e3's
file, by script), referee-2 fa010874 (fa0108743e17465322a30fb1e92a05a1c7c0f311, 2026-11-07T15:53:15Z, REFEREE-2 successor 31's Addendum 1
of docs/referee-2/R2-P-TOWER-FUEL.md; the file 223 lines, 21,184 bytes, sha1 8edefeca0b4c8046da03b88dd01b827da5731f4d; its l. 1-177 =
4bede4dd's file, by script), checker ca749d6e (the last commit of CHECKER C132 Add. 2; docs/checker/ ends at C133.md, whose Add. 1 for R119
is not on origin at either fetch; C134 does not exist). 7f7ff6f5, 740f6c79, f62faf37, d39fc93a and fa010874 are NOT ancestors of the local
trunk 2f98d985 or of origin trunk 0c317432 (git merge-base --is-ancestor; also 559be040, below); 807984e3 and 4bede4dd are. The Lead merges claude/l-lower,
claude/referee and claude/referee-2 before landing.
Local trunk at the start of this fill: HEAD 0c317432 (2026-11-07T16:03:02Z, «Lead: restart scores (REFEREE 27, REFEREE-2 31, L-RED 54);
log»; origin trunk 498a44e4 its parent). RESULTS at HEAD: sha1 576a89b7d6c98b7ba6b359897c8a94672d3cb9f0, 14,521 lines (= RESULTS at 478d0bd9, where R118 landed);
«### R117» l. 13362, «### R118» l. 13607, «**Erratum E-1**» l. 13879, «**Erratum E-2**» l. 13892, «**Note E-3**» l. 13920, «## Dead ends
(kept;» l. 13951. GAPS at HEAD: sha1 ac63d1a7fc1bfd3ffc753c765cc2ff9da952c7f9, 23 lines, l. 11 76 "|", 53 «UPDATE 2026-», the last R118's
«UPDATE 2026-11-07 14:48Z: RESULTS R118 (P-N5-XICYC; CHECKER C132 af92b846)». R119 (P-IDEAL-DBL) was then not landed (its second fill
docs/agents/R119-draft.md, 205f6002, sha1 94a2be76c13e518994929438205acd8c0a106b0e, at CHECKER C133 Add. 1).
TRUNK CHANGE DURING THIS FILL: CHECKER C133 Add. 1 b86962ae (2026-11-07T16:17:29Z) reached origin/claude/checker, and the Lead landed R119 at
the local trunk 2f98d985 (2026-11-07T16:38:28Z, «Lead: land R119 IDEAL-DBL (P-IDEAL-DBL, line L-3; CHECKER C133 Add. 1 b86962ae PASS);
log»; origin trunk 0c317432 at the 16:39Z fetch). RESULTS at 2f98d985: sha1 b6038515848b9c0d3217657f8dce7d099d805c6a, 14,756 lines; «### R119»
l. 13879-14112, «**Erratum E-1**» l. 14114, «**Erratum E-2**» l. 14127, «**Note E-3**» l. 14155, «## Dead ends (kept;» l. 14186; R104-R118's line
numbers unchanged. GAPS at 2f98d985: sha1 3825c35d868bb5ee5bc34c9b6f046c49634b31e5, 23 lines, l. 11 76 "|", 54 «UPDATE 2026-», the last R119's
«UPDATE 2026-11-07 16:38Z: RESULTS R119 (P-IDEAL-DBL; CHECKER C133 b86962ae)». The 16:39Z fetch also found l-lower 559be040 (16:14:01Z,
«L-LOWER 6: L6 §5c (READ-NEST DEAD on SL41; climb predicate guard_l6.py; GAD95 xcheck vs box150)»): git diff f62faf37 559be040 names
only docs/lower/L6-supplier.md, four experiments/lower/l6/ files and notes/L-LOWER.md, so the packet, L-1, L-2, the fixes,
experiments/lower/l3-l5 and check.sh are unchanged. The trunk-dependent checks were re-run on 2f98d985 (prem120.py, upd120.py,
sim120b.py; names by grep); R120 goes after R119 (G-P).
Sources read: the packet docs/lower/P-TOWER-FUEL.md (frozen 7f7ff6f5, 2026-11-07T13:01:29Z, the file's only commit; sha1
a093e0e7f668555395fb0aae476e7677c2a89ffd, 130 lines, 14,998 bytes; read in full); line L-1 (408470adbb1d80f0ed4f29b363867da3d6d430d4, 3,834
bytes, 7f7ff6f5, the file's only commit); fixes entry 1 and line L-2 (740f6c79, both files' only commit): docs/lower/P-TOWER-FUEL-fixes.md
93 lines, 9,973 bytes, sha1 0902efb9eaea48501e4289a8ce3980b235347ac8, read in full; L-2 sha1 d866ca50b0a0372efd9e93a2db0410801b3ddc15,
4,586 bytes; experiments/lower/l5/p_tower_check.py (172 lines, read in full), mkL2_tf.py (read in full), experiments/lower/check.sh (50
lines; the P-TOWER-FUEL block is l. 49-50); REFEREE successor 27's docs/referee/R-P-TOWER-FUEL.md (report 807984e3, §C d39fc93a; read in
full; its scratch tools listed, not re-run); REFEREE-2 successor 31's docs/referee-2/R2-P-TOWER-FUEL.md (report 4bede4dd, Addendum 1
fa010874; read in full; its tools listed, not re-run); RESULTS R104 (title l. 9864), R105 (l. 10155), R110 (l. 11323), R113 (l. 12152),
the Errata and Note E-3; GAPS l. 11; DECISIONS l. 355-358 (L41) and DECISIONS-INDEX (its L41 row); docs/agents/LEAD-STATE.md l. 2512-2552 (the
P-TOWER-FUEL routing, the 15:18Z rulings at l. 2545); docs/NOW.md (grep); notes/L-LOWER.md at f62faf37 (its diff to 740f6c79); CHECKER C116 (G-3), C122,
C125-C133 (verdicts and E-items; C132 and C133 in full) on claude/checker; docs/agents/R119-draft.md (the model; its first-fill record l. 87-425 and its UPDATE d[666]) and
docs/agents/R118-draft.md (the model's model).
Checks run at this fill (scratch /tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad/r120;
nothing written into the repository but this file). (a) rel120.py: the L-1 → L-2 byte and token tests (M1-M7), L-2's shape. (b)
experiments/lower/check.sh (the whole file, P-TOWER-FUEL block included) from a git archive of f62faf37 (experiments, docs/lower,
scripts), 2026-11-07T16:23:15Z-16:23:27Z by date -u, rc 0, 53 output lines ending «P-TOWER-FUEL CHECK PASS». (c) static120.py, my own
instrumented copy of p_tower_check.py's counters (the lane simulator l3/sim.py run, not edited): every DATA clause of L-2 against its
counter, unit, set and scope. (d) prem120.py, the premise labels and quotes. (e) upd120.py, the UPDATE with controls R97-R119 (R119's unfilled
and, after the landing, as landed). (f) chk120.py (title, block, UPDATE, quote sweep, stale grep), lp120.py (line-precise quotes),
sim120.py (landing simulation with a stand-in R119, on 0c317432) and sim120b.py (on 2f98d985): Addendum.
LESSONS APPLIED (R119's list, plus C132 and C133, the E-items of C125-C133 at origin/claude/checker ca749d6e). C113 E-1 / C123 E-1 /
C133 E-1: the title is L-2 verbatim, nothing inserted and nothing stripped, and L-2 has no «R1xx» and no ledger tag before its claims
(CLEAN). C133 E-3: the scope tail « (date) — … not a TARGET.md claim» and «G-N5-TIME stays OPEN» are in the line (CLEAN; G-U for the
UPDATE). C120-C130 §3-§4 / C128 E-1..E-5 / C130 E-1..E-4 / C132 E-3..E-5 / C133 E-4, E-5: EVERY DATA clause tested against the code of
its counter for unit, set and scope, and every signed clause matched to a count or a no-DATA entry, «so …» consequences included (G-9).
C129 E-2 / C130 E-4: each instance reproducible from the line (G-D). C122 G-0: parentheses balanced (the L-2 SHAPE item). C122 E-3 / C132 E-2 / C133
E-2: the source note names every proof-carrying file and the lane successors (G-1: FLAG). C132 E-7 / C133 E-6: a referee-originated
proof of record is named in the scope tail (L41; G-7: FLAG). C118 E-1 / C132 E-1: no status word that goes stale at landing (G-11).
C115 E-1: premises checked against what RESULTS records, landed entries only (G-4). C116 G-2: name clashes (G-6). C116 G-3: pins (G-12).
C119 E-1: every «referee X did Y» checked against that referee's file. C130 G-P / C133 G-P: the UPDATE builder carries a control for every
UPDATE that lands before this one (R97-R119 landed; R119's control checked unfilled against
R119-draft.md and filled against GAPS l. 11). C132 Add. 1: block re-run times as a
date -u interval.
FLAGS FIRST (G-1 and G-7 make CHECKER FAIL as L-2 stands, by the C133 E-2 / E-6 precedents; G-U is CHECKER's ruling on the UPDATE
procedure, no line change needed; G-9 (i), (ii) are notes with optional replacements; G-P is the Lead's). Exact replacements R-B, R-G
(and optional R-S, R-C, R-U), each old string once in L-2, by script; L-2 with R-G then R-B: sha1
87161a3e18354d346e3297d43c77289ccf3b7fd1 with its newline, 4,869 bytes, 81 «(» / 81 «)», depth never negative, 0 "|", one « — »; its
UPDATE by the procedure of G-U 9896971b28892728d9e1be41b6c0cc0d2ad79dc7 (4,900 bytes); R-S, R-C, R-U not built into a line. Then the notes
and CLEAN items, then (0)-(14).
- G-1, SOURCE NOTE (FLAG; the C122 E-3 / C132 E-2 / C133 E-2 class; CHECKER FAIL as it stands). L-2's last parenthesis is «(P-TOWER-FUEL,
  docs/lower/P-TOWER-FUEL.md; L-LOWER successor 5)». Fixes entry 1 carries text the line rests on: §1 replaces the packet's proof of
  Lemma 5 (iii) (CROSS-ECONOMY's sign clause), whose inequality both referees found false, by the «Proof of record (REFEREE's repair; it uses
  only the packet's Lemma 4 (a), ENC and acyclicity)» (fixes l. 18-24); §3 (TF-4 = W-3) replaces the packet's I-FUEL sentence, which
  REFEREE-2 found «false literally» (l. 21), by the measured scopes that L-2's I-FUEL clause states (48 at some pre-state, 16 at every
  pre-state, 0 of the other 79); §2 (TF-3) gives the 30 I-ROOM units their unit. So the packet alone does not carry the proof of a signed
  clause of the line, and L-2's instance clauses are the fixes entry's, not the packet's §4. L-2 was made by L-LOWER successor 6 (fixes l.
  3), the note names successor 5 only. C133 l. 24 on R119: «The note names neither the fixes file nor the lane.»; every landed line
  R113-R118 with a fixes file names it (R118: «with its fixes entries 1-2, docs/new/P-N5-XICYC-fixes.md»). Proposed R-B (the R113-R119
  form): " (P-TOWER-FUEL, docs/lower/P-TOWER-FUEL.md; L-LOWER successor 5)" → " (P-TOWER-FUEL, docs/lower/P-TOWER-FUEL.md with its fixes
  entry 1, docs/lower/P-TOWER-FUEL-fixes.md; L-LOWER successors 5-6)". Old string once in L-2 and once in the UPDATE (script).
- G-7, L41: THE REFEREE-ORIGINATED PROOF OF RECORD (FLAG; the C132 E-7 / C133 E-6 class; CHECKER FAIL as it stands; the Lead's ruling of
  15:18Z already names the proof of record). LEAD-STATE l. 2545: «TF-1 = W-1 with REFEREE's Lemma-4(a) repair as proof of record,
  REFEREE-2's ENC route second». The proof of record of CROSS-ECONOMY's sign clause is REFEREE's text (R-P-TOWER-FUEL §3, l. 107-112),
  copied into fixes entry 1 §1; the lane's own proof is the false inequality. L41 (DECISIONS l. 355-358) counts a referee-written proof
  as two-referee signed when «the author referee signs it in its report and the OTHER referee independently checks and signs it; both
  signatures and the joint gap map are quoted in the RESULTS entry, whose scope tail says the proof is referee-originated.» Met in
  substance: REFEREE signs it (§C l. 251-252 «CROSS-ECONOMY (iii) is now SIGN (TF-1 closed by the proof of record)»); REFEREE-2 checked it
  after its own independent repair (Add. 1 l. 210 «The proof of record (REFEREE's) is correct.», l. 213 «The Lead's choice of record is
  fine with me.», l. 223 «(iii) on the repaired proof now of record»); the gap map is TF-1 = W-1, closed at both. Missing: the scope tail.
  L-2 says nothing of it («referee» 0 times, «fixes» 0 times in L-2, by script). C132 l. 47: «L41 requires the scope tail to say a proof
  is referee-originated.» Proposed R-G (the R118 / R119 form, inside the scope tail): "; G-N5-TIME stays OPEN; not M3, not a gauntlet
  step" → "; the proof of record of CROSS-ECONOMY's sign-change clause is referee-originated (REFEREE R-P-TOWER-FUEL §3, restated in
  P-TOWER-FUEL's fixes entry 1 §1; REFEREE-2's own repair is a second route), signed by both referees; G-N5-TIME stays OPEN; not M3, not a
  gauntlet step". Old string once in L-2; it is not in the UPDATE (the UPDATE drops «; G-N5-TIME stays OPEN»), where the new sentence
  lands after the scope words, before «; DATA: » (script: the proposed UPDATE = the L-2 UPDATE with R-B and that one insertion, True).
- G-U, THE UPDATE PROCEDURE (FLAG for CHECKER's ruling; no line change needed). L-2 has R105-R116's line shape: labels BEFORE their
  clauses, one unlabelled clause «; instances (DATA, stored start): …» last before the one « (2026-11-07) — », scope words, a DATA
  parenthesis, the source parenthesis. Two departures from the landed precedents (by script on the titles at HEAD): (1) its DATA
  parenthesis opens «(DATA: », R105-R110's form (sentinel_build of R105's procedure requires it), not R111-R116's «(DATA, » (sentinel_build111
  requires that); (2) its drop words read «; not M3, not a gauntlet step, not a TARGET.md claim», where every landed line R90-R118 but R112
  (whose tail reads «not Lean; not a TARGET.md claim») has «not M3, not a step-4 pass, not a TARGET.md claim» («gauntlet» 0 times in the
  titles R90-R118). So R116's procedure as
  C133 E-3 ruled it for R119 (sentinel_build111) fails on L-2, and R105's sentinel_build unchanged fails on the drop assertion
  (upd120.py: «AssertionError('not M3, not a step-4 pass, not a TARGET.md claim')»). Built here: R105's sentinel_build UNCHANGED, run on L-2
  with its one «not a gauntlet step» read as «not a step-4 pass» (the phrase occurs once and is dropped, so it does not reach the UPDATE),
  with R111's / R116's DEAD-clause step for the instances clause (cut before the build, put back behind the last label (CROSS-ECONOMY));
  cross-checked by a direct build that drops the line's own words (True). Result: labels behind their clauses, the instances clause behind
  (CROSS-ECONOMY), « (2026-11-07) — » → «: », «; G-N5-TIME stays OPEN» and «; not M3, not a gauntlet step, not a TARGET.md claim» dropped,
  «(DATA: » opened as «; DATA: » and its «)» dropped, the source parenthesis kept, «. G-N5-TIME stays open.» appended; token diff L-2 →
  UPDATE 12 hunks, 31 tokens out, 30 in, nothing else (Addendum (8)). The «(DATA, » inside «instances (DATA, stored start)» stays as text.
  CHECKER rules whether this is the procedure. Optional R-U (only if CHECKER wants the landed drop words): "not a gauntlet step" → "not a
  step-4 pass" (old once in L-2; REFEREE §7 l. 203-204 and REFEREE-2 l. 163 read the scope with «not a gauntlet step»; R-U changes no
  meaning-bearing claim and the UPDATE is the same).
- G-9, DATA, CLAUSE BY CLAUSE (the C120-C133 rule: unit, set and the statement's scope of every count, against the counter code it names;
  every signed clause matched to a count or a no-DATA entry). Every figure of L-2's DATA is asserted by p_tower_check.py (l. 75-109, 168-171)
  and reproduced by the re-run ((b) above); my static120.py re-derives the units below. Counter code: p_tower_check.py §(3) l. 111-171 on
  l3/sim.py's run(). The DATA head: «on 24 runs from the stored start (the 15 genomes experiments/lower/l3/kill/*.json, the 7 genomes
  experiments/lower/l4/rec/*.json and the two instances), 62 doubling (run, level) pairs, 757 j-windows»: l. 112-113 (glob of the two *.json
  sets plus G7_best_d28, SL41_d28); static120.py: 15 + 7 json files (G7_best_d28.txt is not among l4/rec/*.json), 24 runs, 1,999 steps;
  «levels» counts doubling (run, level) pairs (l. 124), 62. MATCH.
  - DOUBLE-EQ «no step moves both members of pair j, the pair flips exactly at the steps moving a member, each member moves exactly once in
    every j-window, and if F(j − 1) ≥ 1 the first mover is the same member in every j-window»: «its first two clauses on 7,069 (step,
    doubling level) units, its third on the 757 j-windows, its fourth on the 62 doubling (run, level) pairs, 61 of them with F(j − 1) ≥ 1».
    Counters E3 (l. 126-128, per step t of the run and doubling level: both members move, or whether a member moves differs from whether pair j flips), E3_units += T per doubling
    (run, level) (l. 124; static120.py: Σ T over the 62 = 7,069), E4 (l. 130-131, per window: the movers are not exactly p, q, or two moves at one
    step), E5 (l. 133, per doubling (run, level), counted only when F(j − 1) ≥ 1), E5_hyp 61 (l. 124). MATCH. NOTE: the unit «(step,
    doubling level)» is (run, step, doubling level) with the run implicit (both referees use it: REFEREE l. 164-165, REFEREE-2 l. 102).
  - PULSE-NEST «0 on 757 windows, attained on 215»: PN (l. 135-139), per window of a doubling level with k = the number of consecutive
    doubling levels above j (the largest k the hypothesis allows on that run). MATCH.
  - GAP-NEST «0 on 260 window pairs, attained on 12»: GN (l. 140-141), per (window, next window) with k ≥ 1. MATCH. (ii) below for its «so …»
    form.
  - DOMINANCE-FREEZE «0 on 65,885 (consecutive-state pair, mover) units with equal deciders and on 1,390 (member of a doubling pair, pair of
    consecutive moves) units»: DFa (l. 118-121), every run, every step t and every mover x with dec(s_(t−1), x) = dec(s_t, x), π equal;
    DF (l. 143-146) per member of a doubling pair and consecutive moves, the decider not constant on s_(t−1), …, s_(t′−1). MATCH. NOTE (no
    change): (a)'s statement is for every state; the counter compares consecutive states only (65,885 of the 76,972 (consecutive-state
    pair, mover) units of the 24 runs have equal deciders, static120.py; = REFEREE l. 136); the line names that unit. Both referees tested
    (a) at every state as referee data (REFEREE l. 93-94, 77,674 (state, mover) units; REFEREE-2 l. 108).
  - CROSS-ECONOMY «0 on the 65 windows of 4 crossed doubling pairs, its sign clause on 43»: CE (l. 149-164): crossed iff xt(p, 0) = xt(q, 1),
    xt(p, 1) = xt(q, 0), distinct, both movers, outside pair j (the line's definition); (ii) per window, equal truth values of D(s_(u₁−1)) > θ_f and
    D(s_(u₂−1)) > θ_(x₂) are a violation; (iii) on the windows with the RANK hypothesis at both pre-states (largest rank in the symmetric
    difference of the chains of the CURRENT options of A_0, A_1 above the four pair-j option ranks, M7's wording), 43. The 4 are four
    doubling (run, level) pairs of four different runs (REC_d10_tower_mu30 level 3, REC_d12_mu42 level 6, REC_d9_mu29 level 6,
    RECF4_d20_F60 level 3; static120.py = packet §5 = REFEREE-2 l. 103-104). MATCH.
  - MOVE «no separate DATA»: listed (both referees counted it as referee data, 72,974 units: REFEREE l. 59, REFEREE-2 l. 106).
  - Instances «the two instances re-derived exactly»: I-ROOM «levels 0-5 capped, F(6) = 222» (l. 75, 77: F[:8] asserted); «violates
    PULSE, GAP ≥ 7 − j at levels j = 1, …, 5 (unit = j-window; set = all 119 of them) only at level 5, 30 times (unit = (5-window, PULSE or
    GAP); in 16 of its 63 5-windows) (15 pulses and 14 gaps of length 1 in the 5-windows opened by mover 9 moving to option 1, and 1 pulse
    of the first 5-window)»: slack() l. 67-73 with need 7 − j, c7 = levels 1-4 (0, 0), level 5 (16, 14) (l. 79), per[((9, 1),)] = [15, 14],
    per[()] = [1, 0] (l. 80), nwin 119, 63 windows at level 5, 16 distinct (l. 82-85). static120.py: windows 3, 7, 15, 31, 63 = 119; every
    violation of length 1; the 14 gap windows are among the 16 pulse windows; a GAP(W) is attributed to W, as the line's GAP(W) :=
    u₁(W⁺) − u₂(W) says. MATCH (REFEREE-2 Add. 1 l. 199-200 on the two «unit =» parentheses: they «bind to different counts»).
    I-FUEL «meets PULSE, GAP ≥ 7 − j at levels 1-5 while 48 of its 127 6-windows do not have exactly one move of each member of pair 6 (the
    movers 12 and 13, crossed onto movers 22, 11)»: cs all (0, 0) (l. 81), fail6 «len(w[3]) != 2» on 127 windows, 48 (l. 89-92). The counter
    tests the move count 2, the line says «exactly one move of each member»: equal here, because no 6-window of either instance has two
    moves of one member (static120.py; profile 79 with both, 16 with 12 only, 16 with 13 only, 16 with none = REFEREE-2 l. 85-86), and by
    MOVE a member that moved sits on c_6 for the rest of the window. «in each of these 48 windows [a, e] the option (9, 1) of rank 87 is
    dec_s(12) or dec_s(13) at some state s among s_(a−1), …, s_(e−1) (at every such state in 16 of them; at no such state in any of the
    other 79)»: l. 94-100, 108 (states t = a − 1, …, e − 1 of the window [a, e]; dec_fail 48, dec_every 16, dec_good 0; also dec_first 32,
    not in the line); option 19 is (mover 9, option 1) (static120.py: opts[9][1] carries β 19; l. 107 asserts its rank 87 and parity, and
    the crossing (22, 11) / (11, 22)). MATCH.
  - (i) NOTE, optional R-S (the C130 set-per-clause class; not a FAIL in my reading, because a 0-violation clause has no count). The
    I-FUEL clause «meets PULSE, GAP ≥ 7 − j at levels 1-5» names no unit and no set, where the I-ROOM clause names «(unit = j-window; set =
    all 119 of them)». The set is SL41's 119 j-windows of levels 1-5 (static120.py: 3, 7, 15, 31, 63), which p_tower_check.py tests (l. 78,
    81) but does not count (nwin is counted for G7_best_d28 only, l. 82). Optional R-S: "meets PULSE, GAP ≥ 7 − j at levels 1-5 while" →
    "meets PULSE, GAP ≥ 7 − j at levels 1-5 (unit = j-window; set = all 119 of them) while" (old once in L-2; p_tower_check.py would then
    count and assert SL41's 119).
  - (ii) NOTE, optional R-C («so …» consequence). GAP-NEST's capped form «so with levels 0, …, h − 1 capped (F(l) = 2^(l+2) − 2) PULSE and GAP
    are ≥ h − j for 1 ≤ j ≤ h − 2» has no counter of its own and no no-DATA entry. It is covered: on a run with levels 0, …, h − 1 capped,
    levels 1, …, h − 1 are doubling, so at every j ≤ h − 2 the counters' k is ≥ h − 1 − j and PN, GN test PULSE, GAP ≥ k + 1 ≥ h − j. The
    R119 precedent (L-3's so R(y) ≥ moves(y), a covered consequence) was not an E-item at C133. Optional R-C: "MOVE: no separate DATA;" → "MOVE:
    no separate DATA; GAP-NEST's capped form: no separate DATA (PULSE-NEST and GAP-NEST with k = h − 1 − j);" (old once in L-2).
  - (iii) NOTE. «the option (9, 1) of rank 87 is dec_s(12)»: by the line's definition dec_s(x) is the option «together with its side»; the
    counter compares the option only (l. 96, «[0] == 19»). REFEREE §C l. 231: «means the option component of dec; acceptable.»
  - SCOPE (NOTE): every statement is on acyclic Ξ-graphs on 𝓛^R_d and every DATA genome is in 𝓛^R_d (REFEREE l. 134 «all in 𝓛^R_d»;
    REFEREE-2 l. 78, its own ok_lr); DATA is from the stored start only (the line says so twice).
- G-D, THE INSTANCES: CLEAN (the C129 E-2 / C130 E-4 check). Each is named by path with its sha1 prefix and «stored start» (the start line
  of the genome file): experiments/lower/l4/rec/G7_best_d28.txt (b995fff21c1f8558eb3e1868ec5ce59a3d4ccfb3, pinned at p_tower_check.py l.
  31) and experiments/lower/l5/rec/SL41_d28.txt (c1b46c319fd614e5bcb0909b616a9f2833e0dfee, pinned); their starts are packet §4's (static120.py
  prints them; both referees compared, REFEREE l. 118, 122, REFEREE-2 l. 78). Every number of the two instance clauses is asserted (G-9).
  The instances are DATA, not DEAD: L-2 kills no statement; «with two obstruction instances for a seventh capped level» is the scope
  tail's description, and «does not claim that F(6) = 222 is a cap» (packet §4 «Not claimed: that the plateau F(6) = 222 is a cap»). No
  Dead-ends row is drafted.
- G-2, DEFINITIONS AND STATEMENTS DIFFED (my own diff of L-2 against packet §1-§5 with fixes entry 1). Premises = §1 (R116, R119 and lane
  items not used). Notation: j-window = §1 l. 20-22 without «of [1, T]» and «(the j-windows partition [1, T]; …)»; doubling = §1 l. 22;
  PULSE, GAP = §1 l. 23-25; dec = Lemma 4's dec_s(x) (§2 l. 41-42) in words. MOVE = Lemma 0. DOUBLE-EQ = Lemma 1 (E3), (E4), (E5) without
  (E1), (E2) and without «(and γ_j(0) = γ_j(1))» (narrower). PULSE-NEST = Lemma 2 (its «k ≥ 0, j + k ≤ d − 1» and j ≥ 1 implicit in
  «levels j, …, j + k are doubling», doubling being defined through F(j − 1)). GAP-NEST = Lemma 3 with its capped corollary. DOMINANCE-FREEZE
  = Lemma 4 (a) («the option of larger value of x under s» = π_s(x), §1 l. 27) and (b) («a member x of a doubling pair» = «x is a member
  of pair j, level j doubling»). CROSS-ECONOMY = Lemma 5 (ii) and (iii) without (i) and without the packet's «and nothing else is required
  of it there», which REFEREE labels a READING (l. 113-114: «is a READING, not part of the signed statement»); the RANK hypothesis
  with M7's «Ξ-chains of the current options of A_0 and A_1» = §2 «chain(A_0) △ chain(A_1)» as the proof of record reads it («(chains of
  the current options)», fixes l. 19). Instances = packet §4 with fixes §2 (TF-3) and §3 (TF-4, the measured part; the READING is not in
  L-2). DATA = §5 with fixes §4 (E5's hypothesis 61 of 62). No sentence of L-2 is wider than the signed statements (C117 E-1 / E-2).
  (i) NOTE. xt(x, k) (R104's notation), ε(x, k) and rank (R105 ENC), T^R(d) (R110's) and «capped» (defined in the line) are used; xt, ε and
    T^R(d) are not defined in the line. The C124 G-9 (vii) ruling covers landed notation not named; the premise parenthesis names R104,
    R105 ENC and R110.
- G-4, PREMISE ROUTE (the C115 E-1 class): CLEAN (prem120.py on RESULTS 576a89b7 at 0c317432 and b6038515 at 2f98d985). Labels in L-2 (by script): «R104» 3, «R105» 1,
  «R110» 1, «R113» 1, no other R-label; each a landed entry (### R104 l. 9864, ### R105 l. 10155, ### R110 l. 11323, ### R113 l. 12152).
  «R116», «R119», «DBL-EQ», «WINDOW-ONCE», «P-IDEAL-DBL», «PATH-RISE», «AND-GATE», «PAIR-DOUBLE», «T-BOUND» 0 times in L-2 and in the
  fixes; the packet names R116, R119 / P-IDEAL-DBL and L-LOWER's DOUBLE-EQ′ / FROZEN-WINDOW only in its «Not used» bullet (l. 25-26), and
  PULSE-NEST as «re-proved; first proved in L-SI 42's lane» (l. 37): re-proved from ALIGN, not cited (REFEREE l. 52 «No R116, R119 or
  lane item is used in a proof (checked line by line in §3).»; REFEREE-2 l. 37). Quotes: packet §1's ENC quote, two parts split at «…»,
  both in R105's title (and in R113's body, l. 12254-12255); the ALIGN quote (273 characters) in R113's title; «signed, not landed» is not a
  quote of RESULTS (REFEREE l. 44). 3 of 3 RESULTS quote parts found, 0 not found. L-2 itself quotes nothing (no opening guillemet in L-2). Uses: R104's
  definition only («no theorem of R104 used»); R105 ENC only; R110's definition of 𝓛^R_d only; R113 ALIGN with its notation c_l, γ_l, flip,
  F(l) and cv, all in R113's title (cv_s(z) «the integer value of z's current option (R105 ENC)»; REFEREE §C l. 225 «cv is R113's notation»).
  R113 is stated on acyclic Ξ-graphs, as L-2 is.
- G-6, NAMES (by script on RESULTS 576a89b7 / GAPS ac63d1a7 and again on b6038515 / 3825c35d at 2f98d985). 0 times in RESULTS and GAPS: «R120», «C134», «P-TOWER-FUEL», «(MOVE)»,
  «DOUBLE-EQ», «PULSE-NEST», «GAP-NEST», «DOMINANCE-FREEZE», «CROSS-ECONOMY». Near-clashes, none a label collision: «(MOVE)» against R113's
  «(MOVES)» and «(KP-MOVE)» (different statements); DOUBLE-EQ (E3)-(E5) overlaps R119's DBL-EQ (a)-(c) and WINDOW-ONCE in content
  (R119 landed at 2f98d985; R120 re-proves from ALIGN and does not cite it); «PULSE-NEST» is also L-SI's lane name for the same lemma (packet l.
  37); «R120» is also an old L-RED round label (docs/red/R120-reset-lin.md, LEAD-STATE l. 1994-1995), not a RESULTS label. «capped»
  occurs 3 times in RESULTS, never as a term about F(l). Body sentence: Honest limits (vi).
- G-P, PLACEMENT (Lead). R119 LANDED at the local trunk 2f98d985 during this fill (16:38:28Z). R120's block goes after R119's (l.
  13879-14112), before «**Erratum E-1**» (l. 14114), and its UPDATE after R119's on GAPS l. 11. Simulated on 2f98d985 (sim120b.py) and,
  before the landing, on 0c317432 with a stand-in R119 (R119-draft.md d[425:659] and d[666], sim120.py); the stand-in with the landed fill
  equals RESULTS and GAPS at 2f98d985 (True ×2): Addendum (7).
- G-0, THE CHECKER NUMBER. docs/checker/ on claude/checker (ca749d6e, and b86962ae at 16:39Z) ends at C133.md; «C134» occurs 0 times in
  RESULTS, GAPS, NOW, LEAD-STATE, DECISIONS-INDEX and on claude/checker (git grep, both heads). This draft uses C134 (title fill, UPDATE head, GAPS preamble).
- G-5, ERRATA (note). E-1 (R97-R100 counts) does not bear; E-2 corrects R105's CHAIN-BACK, RANK_t and KEYFLIP, not ENC (REFEREE-2 l.
  31-32); Note E-3 concerns R110's SC-ISO, not its 𝓛^R_d definition (REFEREE-2 l. 34).
- G-8, SCOPE AND TARGET (note). L-2's scope words «bounds nothing polynomially and does not claim that F(6) = 222 is a cap or any bound on
  T^R(d); Ξ-cyclic genomes and genomes outside 𝓛^R_d are not covered; G-N5-TIME stays OPEN; not M3, not a gauntlet step, not a TARGET.md
  claim» equal packet §4 «Not claimed» and §7 (REFEREE-2 l. 121-122). No statement mentions a parity game, a winning region, a running
  time or a complexity class.
- G-10, LEAD RULINGS. L-2 cites no Lead reading by label («Lead reading» 0, «L4» 0 in L-2). The rulings of 15:18Z (LEAD-STATE l. 2545)
  are applied as ruled: TF-1 = W-1 with REFEREE's repair of record and REFEREE-2's route second (fixes §1: «Proof of record (REFEREE's
  repair; …)», «Independent second route (REFEREE-2's repair, recorded, not needed for the record)»); TF-4 = W-3 as measured statements plus
  a READING (fixes §3: «READING: the room conditions are met and the missing piece is fuel», not in L-2); the overlapping L-1 targets merged
  into one string each (M1-M7, fixes §5; rel120.py). NOTE: the fixes header calls the rulings «(Lead reading)» (l. 7); they are routing
  rulings, not a numbered reading in DECISIONS. L41: G-7.
- G-11, STALE WORDS (notes). L-2 has none («pending», «not landed», «NOT YET», «candidate», «will » 0 times). The packet header «Status:
  FROZEN 2026-11-07 …» and the fixes' «L-1 NOT YET» (quoting REFEREE's first verdict) are history. L-1's and L-2's source note says
  «L-LOWER successor 5» although L-2 is successor 6's (G-1). notes/L-LOWER.md at f62faf37 («Waiting for both referees' byte tests») is
  stale since d39fc93a / fa010874; notebooks are history.
- G-12, PINS (the C116 G-3 class; note). p_tower_check.py pins the two instances, L-1 and L-2 (l. 29-36, «pins OK: 4 files»); the packet,
  the fixes file and the 22 corpus json files are not pinned by this block. C116 l. 67: «NOT required before landing.». I re-hashed the
  packet, L-1, L-2 and the fixes at 740f6c79 and f62faf37 (equal). The block is wired: experiments/lower/check.sh l. 49-50 («timeout 100
  python3 -I l5/p_tower_check.py»), run by scripts/verify.sh.
- G-13, THE REFEREES' ROUNDS: (3), (4). D-items: (11).
- G-14, THE FIXES FILE (note). One entry (§1 TF-1 = W-1, §2 TF-3, §3 TF-4 = W-3, §4 E5's hypothesis with TF-2 = N-1 noted, statement NOT
  changed, §5 line L-2 with the merge map M1-M7, §6 the description slip); entry 1 carries the proof of record of a signed clause (G-1,
  G-7). Each M-old once in L-1, each M-new once in L-2, L-1 + M1..M7 = L-2 (rel120.py, True; REFEREE §C l. 221-222 and REFEREE-2 Add. 1
  l. 193-194 by their own scripts).
- G-N, NOVELTY (note). No source outside the fleet is cited by L-2 or the packet; the entry makes no literature claim.
- CLEAN AT L-2 (pre-check against CHECKER's recurring items, by script on d866ca50): C113 E-1 / C123 E-1 / C133 E-1 (L-2 starts «In the
  IDEAL model of RESULTS R104», «R1xx» 0); C133 E-3 (« (2026-11-07) — » once, «not a TARGET.md claim» once, «G-N5-TIME stays OPEN» once);
  C114 Add. 1 E-1 (<DATE>); C115 E-1 (G-4); C116 G-2 (G-6); C122 G-0 (80 / 80, depth never negative); C129 E-2 / C130 E-4 (G-D); the DATA
  clauses (G-9, notes only); «|»: 0 in L-2, 0 in the entry block, 0 in the UPDATE (Addendum). NOT CLEAN: C122 E-3 (G-1), L41 (G-7); for
  CHECKER: the UPDATE procedure (G-U).
- (L-2 SHAPE, by rel120.py) L-2 is one line: 4,586 bytes and 4,438 characters with its newline, 814 whitespace tokens, 80 «(» / 80 «)», depth
  never negative, final depth 0, 0 "|", one « — », «[» 3 times (two Iverson brackets [D(s_(u₁−1)) > θ_f], [D(s_(u₂−1)) > θ_(x₂)] and the window
  [a, e]; none a label), «R1xx» 0, «(DATA: » once, «(DATA, » once (the instances clause), «not a gauntlet step» once.
(0) PLACEMENT. RESULTS at the local trunk 2f98d985: sha1 b6038515848b9c0d3217657f8dce7d099d805c6a, 14,756 lines; "### R120" 0 times in
  RESULTS and GAPS. PROPOSED (R102's to R119's layout): insert R120's entry, with one blank line after it, directly before «**Erratum
  E-1**» (l. 14114), after the blank line that follows R119's block (G-P). Simulation: Addendum (7).
(1) TITLE. The title is the line file docs/lower/P-TOWER-FUEL-line-L2.txt (l-lower 740f6c79, 2026-11-07T15:26:05Z, the file's only commit,
  sha1 d866ca50b0a0372efd9e93a2db0410801b3ddc15, 4,586 bytes with the newline; byte-equal at the l-lower head f62faf37), verbatim: NOTHING
  is stripped and NOTHING is inserted: "### R120 [refereed-only] ", then the file without its newline, then ", CHECKER PASS
  (docs/checker/C134.md, checker PENDING)" (as R90-R118). Built by script and re-checked after writing (chk120.py): equal.
(2) LINE HISTORY: two lines. L-1 408470ad (7f7ff6f5 with the frozen packet; 3,834 bytes, 3,699 characters with the newline, 677 tokens, 64
  «(» / 64 «)»). L-2 d866ca50 (740f6c79; 4,586 bytes, 814 tokens, 80 / 80): fixes entry 1 §5, L-1 with exactly seven replacements M1-M7 (M1
  = W-2 (a); M2 = TF-L5 + W-2 (b) + TF-3; M3 = TF-L3 + W-2 (c); M4 = W-4 (a); M5 = TF-L1 + W-4 (b); M6 = TF-L2 with W-4 (c) inside; M7 =
  TF-L4); my byte test (olds parsed from 807984e3 and 4bede4dd by my own code, the referee-written news likewise, the three merged news
  M2, M3, M5 read from mkL2_tf.py's literals): each old string once in L-1 and once in the running line, each new string once in L-2, L-1 +
  M1..M7 = L-2, True; REFEREE's TF-L1 / TF-L3 / TF-L5 olds equal REFEREE-2's W-4 (b) / W-2 (c) / W-2 (b) olds, and W-4 (c)'s old lies
  inside TF-L2's (True ×4, the merge map's premise); token diff 12 hunks (21 tokens out, 158 in), every inserted token inside one of the
  seven new strings (True). Neither referee's predicted line is L-2 (REFEREE d115d8df…, REFEREE-2 1a4e8dcc…; fixes l. 72-73: «the Lead's
  rulings merge the two sets»).
(3) THE LINE AT BOTH REFEREES. REFEREE successor 27, docs/referee/R-P-TOWER-FUEL.md: report 807984e3 (2026-11-07T14:42:53Z, new file,
  211 lines): L-1 «NOT YET: TF-L1, TF-L2, TF-L3 (DATA rule, required); TF-L4, TF-L5 optional; exact texts in §5» (l. 18); §C d39fc93a
  (2026-11-07T15:53:22Z; heading «date -u at writing 2026-11-07T15:52Z»; l. 213-252): «Verdict: fixes entry 1 CORRECT. L-2 MATCHES (byte
  test and meaning).» (l. 251). REFEREE-2 successor 31, docs/referee-2/R2-P-TOWER-FUEL.md: report 4bede4dd (2026-11-07T14:40:11Z, new
  file, 177 lines): L-1 «**MATCHES after W-2 (a)-(c) and W-4 (a)-(c)**» (l. 25); Addendum 1 fa010874 (2026-11-07T15:53:15Z; heading
  «15:5xZ by date -u»; l. 179-223): «**L-2 MATCHES** the packet with fixes entry 1, in bytes and in meaning» (l. 222-223).
(4) CLAIMS SIGNED = every row of both verdict tables (REFEREE «## 0. Verdicts» l. 5-19; REFEREE-2 «## Verdicts» l. 11-26) as closed in the
  second round: CROSS-ECONOMY (iii)'s gap TF-1 closed at REFEREE (§C l. 251-252) on the proof of record; REFEREE-2 signed (iii) from the
  first round on its own repair (l. 20) and on the proof of record in Add. 1 (l. 223); every other row SIGN at both from the first round.
  Not signed: §4, §5 (DATA, both), the §4 READING (fixes §3), TF-2 = N-1 (a remark, statement unchanged).
(5) OTHER TEXTS THE ENTRY DEPENDS ON: RESULTS R104 (definition), R105 ENC, R110 (𝓛^R_d), R113 ALIGN and its notation; the two instance
  files and the 22 corpus genomes of experiments/lower/l3/kill/ and l4/rec/ (L-LOWER 3 and 4).
(6) PREMISE LABELS: G-4.
(7) SYMBOL TEST: G-2 (i).
(8) FIXES AND STATUS NOTES: G-14; body Fixes.
(9) GAPS: G-N5-TIME (GAPS l. 11) stays open; L-2 states no CONJECTURE as claimed and kills no statement («P-TOWER-FUEL», «PULSE-NEST» 0
  times in GAPS). A line-11 UPDATE is proposed at the end, BUILT FROM L-2 AS IT STANDS (upd120.py: r119b/tools/upd119b.py's Parts A-D
  unchanged: R97's to R116's LANDED UPDATEs rebuilt from their lines and compared with GAPS l. 11 byte for byte, True ×20; the R117 control,
  LANDED, run117() on L-4 filled with GAPS l. 11's stamp 2026-11-07 10:30 d7091311, = that segment, = R117-draft.md's UPDATE line and =
  r117b/upd117L4.txt filled, unfilled sha1 = C130 §5's b4d74e09…: True ×4; the R118 control, LANDED, run118() on L-4 filled with
  2026-11-07 14:48 af92b846, = its GAPS segment, = R118-draft.md's UPDATE line and = r118b/upd118L4.txt filled, unfilled sha1 = C132 §5's
  d4acaeef…: True ×4; then the R119 control: R116's procedure on R119's L-3 (l-si 610897dd) = R119-draft.md's UPDATE line d[666] =
  r119b/upd119L3.txt, unfilled sha1 074e3c05060c7adcd7b20e5560674bdf12d8b2fa: True ×3, and, LANDED at 2f98d985, filled with GAPS l. 11's
  stamp 2026-11-07 16:38 b86962ae, = that segment: True; all controls True ×23, the last UPDATE on l. 11 R119's; then R120 (G-U)).
(10) DATA of record = packet §4-§5 with fixes §2-§4, NOT signed; L-2's DATA states its counts (G-9). Re-run (b): PASS.
(11) Discrepancies, recorded for CHECKER, no verdict affected: D-1 the packet header «Status: FROZEN 2026-11-07 (date -u, at the commit
  that adds this file)»: commit 7f7ff6f5, 13:01:29Z. D-2 REFEREE l. 2 «Written from 2026-11-07T14:41Z (date -u); the header time of record
  is the commit time.» (807984e3 14:42:53Z); REFEREE-2 l. 2 «2026-11-07 from 14:35Z (date -u)» (4bede4dd 14:40:11Z); REFEREE-2's Add. 1
  heading «15:5xZ by date -u» is a partial stamp (commit 15:53:15Z), the class C132 Add. 1 corrected in a CHECKER stamp; history, not a
  verdict. D-3 the description slip (L-1 «3,699 bytes» = 3,699 characters, 3,834 bytes; fixes §6; both referees). D-4 REFEREE-2 l. 7
  gives p_tower_check.py at 7f7ff6f5 as «155 lines»; at 740f6c79 it has 172 (extended by fix round 1). D-5 REFEREE l. 3 and REFEREE-2 l. 4 name
  the frozen packet at 7f7ff6f5; the lane head at review was later (e362f15b, 14:37:48Z: box L6 work), the packet unchanged (git log:
  the packet's only commit is 7f7ff6f5).
(12) Excluded: packet §4's «Not claimed» (the plateau and T^R(d)), the READING of fixes §3, TF-2 / N-1 (the stronger (E5) without F(j − 1)
  ≥ 1, a referee remark), BOX L6 (docs/lower/ L6 work, experiments/lower/l6/: TOP-CLOCK, TAP, TRANSPARENT-LEVEL, RANK-LOCKED, CONJECTURE
  READ-NEST; lane, unrefereed), docs/lower/L5-rule.md (history). Not part of this entry.
(13) Commits: lane (claude/l-lower): 7f7ff6f5 (2026-11-07T13:01:29Z; packet FROZEN, L-1, check block; L-LOWER successor 5), 4d1c4e4b
  (handover), 2ce74ff9 (successor 6 handover check), fa9104fa, e362f15b, 3329b094 (BOX L6, other work), 740f6c79 (15:26:05Z; fixes entry 1,
  L-2, mkfix_tf.py, mkL2_tf.py, p_tower_check.py extended; successor 6), f62faf37 (notebook). REFEREE: 807984e3 → d39fc93a. REFEREE-2:
  4bede4dd → fa010874. CHECKER: docs/checker/ ends at C133.
(14) DEAD-ENDS ROWS: NONE (G-D).

### R120 [refereed-only] In the IDEAL model of RESULTS R104 (premise: R104's definition of the model only, no theorem of R104 used; RESULTS R105's ENC only; RESULTS R110's definition of 𝓛^R_d only; and RESULTS R113's ALIGN only, with its notation c_l, γ_l, flip, F(l) and cv), on acyclic Ξ-graphs on 𝓛^R_d, with a j-window a maximal set of consecutive steps containing no change of c_j except possibly at its first step, level j doubling if F(j) = 2F(j − 1) + 2, and for a doubling level j and consecutive j-windows W, W⁺ with move steps u₁(W) < u₂(W) of the pair j PULSE(W) := u₂(W) − u₁(W) and GAP(W) := u₁(W⁺) − u₂(W), and dec_s(x) the option of largest rank in the symmetric difference of the Ξ-chains of x's two options under s together with its side: (MOVE) a mover x of level l ≥ 1 moves at step t iff its other option is strictly better under s_(t−1) and c_l(s_t) ≠ s_(t−1)(x), and then moves to c_l(s_t); (DOUBLE-EQ) if level j is doubling then no step moves both members of pair j, the pair flips exactly at the steps moving a member, each member moves exactly once in every j-window, and if F(j − 1) ≥ 1 the first mover is the same member in every j-window; (PULSE-NEST) if levels j, …, j + k are doubling then PULSE ≥ k + 1 on every j-window; (GAP-NEST) if moreover k ≥ 1 then GAP ≥ k + 1, so with levels 0, …, h − 1 capped (F(l) = 2^(l+2) − 2) PULSE and GAP are ≥ h − j for 1 ≤ j ≤ h − 2; (DOMINANCE-FREEZE) the option of larger value of x under s is fixed by dec_s(x), and for a member x of a doubling pair and consecutive moves t < t′ of x, dec(x) is not constant on s_(t−1), …, s_(t′−1); (CROSS-ECONOMY) if level j is doubling and pair j is crossed onto two movers A_0 ≠ A_1 outside it (xt(2j, k) = A_k = xt(2j + 1, 1 − k)), then with D := cv(A_0) − cv(A_1) and the member thresholds θ_(2j) := ε(2j, 1) − ε(2j, 0), θ_(2j+1) := ε(2j + 1, 0) − ε(2j + 1, 1), in every j-window [D(s_(u₁−1)) > θ_f] ≠ [D(s_(u₂−1)) > θ_(x₂)] for the first and second movers f, x₂, and D changes sign between s_(u₁−1) and s_(u₂−1) whenever at both states the largest rank in the symmetric difference of the Ξ-chains of the current options of A_0 and A_1 exceeds the ranks of the four options of pair j; instances (DATA, stored start): experiments/lower/l4/rec/G7_best_d28.txt (sha1 b995fff2…; levels 0-5 capped, F(6) = 222) violates PULSE, GAP ≥ 7 − j at levels j = 1, …, 5 (unit = j-window; set = all 119 of them) only at level 5, 30 times (unit = (5-window, PULSE or GAP); in 16 of its 63 5-windows) (15 pulses and 14 gaps of length 1 in the 5-windows opened by mover 9 moving to option 1, and 1 pulse of the first 5-window), and experiments/lower/l5/rec/SL41_d28.txt (sha1 c1b46c31…; levels 0-5 capped, F(6) = 222) meets PULSE, GAP ≥ 7 − j at levels 1-5 (unit = j-window; set = all 119 of them) while 48 of its 127 6-windows do not have exactly one move of each member of pair 6 (the movers 12 and 13, crossed onto movers 22, 11), and in each of these 48 windows [a, e] the option (9, 1) of rank 87 is dec_s(12) or dec_s(13) at some state s among s_(a−1), …, s_(e−1) (at every such state in 16 of them; at no such state in any of the other 79) (2026-11-07) — a STRUCTURE statement inside the IDEAL model on doubling levels of 2-wide ladders (room: PULSE-NEST, GAP-NEST; fuel: DOMINANCE-FREEZE, CROSS-ECONOMY), with two obstruction instances for a seventh capped level; bounds nothing polynomially and does not claim that F(6) = 222 is a cap or any bound on T^R(d); Ξ-cyclic genomes and genomes outside 𝓛^R_d are not covered; the proof of record of CROSS-ECONOMY's sign-change clause is referee-originated (REFEREE R-P-TOWER-FUEL §3, restated in P-TOWER-FUEL's fixes entry 1 §1; REFEREE-2's own repair is a second route), signed by both referees; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim (DATA: experiments/lower/l5/p_tower_check.py on 24 runs from the stored start (the 15 genomes experiments/lower/l3/kill/*.json, the 7 genomes experiments/lower/l4/rec/*.json and the two instances), 62 doubling (run, level) pairs, 757 j-windows: DOUBLE-EQ 0 violations (its first two clauses on 7,069 (step, doubling level) units, its third on the 757 j-windows, its fourth on the 62 doubling (run, level) pairs, 61 of them with F(j − 1) ≥ 1); PULSE-NEST 0 on 757 windows, attained on 215; GAP-NEST 0 on 260 window pairs, attained on 12; DOMINANCE-FREEZE 0 on 65,885 (consecutive-state pair, mover) units with equal deciders and on 1,390 (member of a doubling pair, pair of consecutive moves) units; CROSS-ECONOMY 0 on the 65 windows of 4 crossed doubling pairs, its sign clause on 43; MOVE: no separate DATA; the two instances re-derived exactly) (P-TOWER-FUEL, docs/lower/P-TOWER-FUEL.md with its fixes entry 1, docs/lower/P-TOWER-FUEL-fixes.md; L-LOWER successors 5-6), CHECKER PASS (docs/checker/C134.md, checker PENDING)
- Object (L-LOWER successors 5-7, D14 / D18 / D20, BOX L5; frozen, unchanged during review): packet P-TOWER-FUEL,
  docs/lower/P-TOWER-FUEL.md, sha1 a093e0e7f668555395fb0aae476e7677c2a89ffd, 130 lines, 14,998 bytes (l-lower 7f7ff6f5,
  2026-11-07T13:01:29Z, the file's only commit; identical at 740f6c79, f62faf37 and 4f25ae6f). Both referees measured it (REFEREE l. 26
  «docs/lower/P-TOWER-FUEL.md a093e0e7…, 130 lines»; REFEREE-2 l. 5 «docs/lower/P-TOWER-FUEL.md a093e0e7… (14,998 B, 130 lines)»).
  Labels (l. 4-5): «PROVED (the statements of §2, proofs below, premises §1 only) / DATA (§4, §5, each with its counter) / READING». To
  sign (§2): Lemma 0 MOVE, Lemma 1 DOUBLE-EQ (E1)-(E5), Lemma 2 PULSE-NEST, Lemma 3 GAP-NEST with its capped corollary, Lemma 4
  DOMINANCE-FREEZE (a), (b), Lemma 5 CROSS-ECONOMY (i)-(iii); DATA: §4 (the instances I-ROOM, I-FUEL) and §5 (the counters). The
  packet's own scope (l. 5-6): «Nothing here bounds T polynomially; G-N5-TIME stays OPEN; not a TARGET.md claim (§7).».
  Fixes: docs/lower/P-TOWER-FUEL-fixes.md, append-only, two entries, entry 1 by L-LOWER successor 6 and entry 2 by L-LOWER successor 7
  (4f25ae6f: 144 lines, 15,426 bytes, sha1 c99bfd3acb8e062fd7b05fec98a5898a7ac883d2; its l. 1-93 are entry 1's file, by script). Entry 1
  (740f6c79; the file then 93 lines, 9,973 bytes, sha1 0902efb9eaea48501e4289a8ce3980b235347ac8): §1 TF-1 = W-1 (the proof of Lemma 5
  (iii) replaced by REFEREE's repair, the proof of record, with REFEREE-2's repair as a second route; statement unchanged), §2 TF-3 (the
  unit of the 30 I-ROOM units), §3 TF-4 = W-3 (the I-FUEL sentence replaced by measured scopes and a READING), §4 (E5's hypothesis holds
  on 61 of 62; TF-2 = N-1 noted, statement NOT changed), §5 line L-2 = L-1 with M1-M7, §6 the description slip. Entry 2 (4f25ae6f, l.
  95-144, written by experiments/lower/l5/mkfix2_tf.py): CHECKER C134's E-1..E-4 with its §5 replacements R1-R4, line L-3, and
  p_tower_check.py extended to pin L-3 and to assert SL41_d28's 119 j-windows; «The packet (frozen at 7f7ff6f5), L-1, L-2 and fixes
  entry 1 are unchanged; no statement, proof, definition, instance or counter changes.» (l. 100-101). Entry 1 carries the proof of
  record of CROSS-ECONOMY's sign clause; entry 2 carries none.
  The RESULTS line is L-3, 7328e67345e1bb6a8605ccfa4f406d1020eabfdb (docs/lower/P-TOWER-FUEL-line-L3.txt, l-lower 4f25ae6f,
  2026-11-07T18:44:07Z, the file's only commit; 4,908 bytes). The title is L-3 verbatim, with nothing inserted and nothing stripped (its
  date parenthesis «(2026-11-07)», its scope tail with the L41 sentence and its source note are the line's own; the source note names
  the packet with its fixes entry 1, which carries the proof of record; entry 2 carries no proof). L-3's parentheses balance (82 «(» /
  82 «)»). Line history: L-1 (408470ad, committed with the frozen packet at 7f7ff6f5); L-2 (d866ca50, 740f6c79, fixes entry 1 §5: L-1
  with exactly seven replacements M1-M7: REFEREE-2's W-2 (a) (cv in the notation), REFEREE's TF-L5 with REFEREE-2's W-2 (b) and
  REFEREE's TF-3 (I-ROOM's level range, 119 j-windows, the 30 units' unit, 16 of 63), REFEREE's TF-L3 with REFEREE-2's W-2 (c) (I-FUEL's
  failing windows defined, the crossing, the decider scope 48 / 16 / 0), REFEREE-2's W-4 (a) (the 24 runs and the (run, level) unit),
  REFEREE's TF-L1 with REFEREE-2's W-4 (b) (DOUBLE-EQ's units 7,069 / 757 / 62, 61), REFEREE's TF-L2 containing REFEREE-2's W-4 (c)
  (DOMINANCE-FREEZE's units), REFEREE's TF-L4 (the chains of the current options)); L-3 (7328e673, 4f25ae6f, fixes entry 2 §2-§3: L-2
  with exactly CHECKER C134 §5's R1-R4, applied in that order, R3's old string inside R2's new text; they are the first fill's R-B, R-G,
  R-U, R-S; see Fixes). Each old string occurs once in L-1 and each new string once in L-2, and L-1 with the seven replacements is L-2
  (my script, True; REFEREE by its own script, §C l. 221-222; REFEREE-2 by its own bt_l2b.py, Add. 1 l. 193-194); L-2 with R1-R4 is L-3
  (my script, True; mkL3_tf.py re-run, True; both referees by their own scripts). L-1: REFEREE «NOT YET: TF-L1, TF-L2, TF-L3 (DATA rule,
  required); TF-L4, TF-L5 optional; exact texts in §5» (807984e3 l. 18); REFEREE-2 «**MATCHES after W-2 (a)-(c) and W-4 (a)-(c)**»
  (4bede4dd l. 25). L-2 MATCHES at REFEREE (d39fc93a §C): «each OLD occurs once in L-1; each NEW once in L-2; L-1 with the seven
  replacements is byte-equal to L-2.» (l. 221-222), M1-M7 judged for meaning (l. 224-237), «Verdict: fixes entry 1 CORRECT. L-2 MATCHES
  (byte test and meaning).» (l. 251). L-2 MATCHES at REFEREE-2 (fa010874 Add. 1): «each OLD occurs once in L-1 and each NEW once in L-2,
  and L-1 + M1..M7 == L-2 byte for byte (sha1 d866ca50…) ✓.» (l. 193-194), M1-M7 against its W items (l. 196-208), «**L-2 MATCHES** the
  packet with fixes entry 1, in bytes and in meaning» (l. 222-223). L-3 MATCHES at both referees, each after its own byte test: REFEREE
  successor 27 (af752251, 2026-11-07T19:08:39Z) §C add. 1 l. 260-262 (own script scratch/tf_l3.py: «each old string occurs once in the
  text it is applied to (R3's only inside R2's new text); the result is byte-equal to L-3.»), l. 263-272 (meaning: «R1: CORRECT.»; «R2:
  CORRECT and correctly attributed.»; «R3: CORRECT, same meaning.»; «R4: CORRECT.»), l. 273 «Verdict: L-3 MATCHES, by the byte test and
  in meaning. All statements stay SIGN as in §C.»; REFEREE-2 successor 31 (e72661d0, 2026-11-07T19:08:25Z) Addendum 2 l. 233-235 (own
  bt_l3.py: «L-2 + R1..R4 == L-3 byte for byte, sha1 7328e67345e1bb6a8605ccfa4f406d1020eabfdb, 4,908 B (= C134's prediction)»), l.
  236-244 (meaning: R2, R4, R3 and R1, each marked ✓), l. 245 «**Verdict:** **L-3 MATCHES** the packet with fixes entries 1-2, in bytes
  and in meaning (Opus 5.5, D1). Statements all SIGN.».
- Claims signed (REFEREE successor 27, report 807984e3 and §C d39fc93a and §C add. 1 af752251; REFEREE-2 successor 31, report 4bede4dd,
  Addendum 1 fa010874 and Addendum 2 e72661d0). REFEREE's table (l. 5-19 of R-P-TOWER-FUEL.md) reads Lemma 0 MOVE, Lemma 2 PULSE-NEST,
  Lemma 4 DOMINANCE-FREEZE (a), (b), Lemma 5 CROSS-ECONOMY (i), (ii) «SIGN», Lemma 1 DOUBLE-EQ (E1)-(E5) «SIGN (remark TF-2, optional:
  (E5) holds without F(j − 1) ≥ 1)», Lemma 3 GAP-NEST «(with the capped corollary)» SIGN, Lemma 5 CROSS-ECONOMY (iii) «SIGN WITH GAP
  TF-1: statement true» with the proof's inequality false and a repaired proof in its §3, the premises «all LANDED on trunk 9315f36c»,
  §7 «CLEAN»; «Gaps of record: TF-1 (proof of (iii); closed by the repair in §3 once the lane takes it into a fixes entry).» (l. 21).
  REFEREE-2's table (l. 11-26 of R2-P-TOWER-FUEL.md) reads every §2 row «**SIGN**», Lemma 5 (iii) «on my repaired proof: the packet's
  proof has a FALSE step (W-1, required)» (l. 20), §4 and §5 «re-derived exactly» / «every counter reproduced exactly by my own code»
  (DATA, not signed), and «Nothing is REFUSED. No statement bounds T; G-N5-TIME stays OPEN.» (l. 26). Second round: REFEREE §C «TF-1 (=
  W-1): CORRECT.» (l. 239) and «All statements SIGNED as in §0; CROSS-ECONOMY (iii) is now SIGN (TF-1 closed by the proof of record).
  TF-L1..TF-L5, TF-3, TF-4 CLOSED.» (l. 251-252); REFEREE-2 Add. 1 «The proof of record (REFEREE's) is correct.» (l. 210) and «Statement
  verdicts are unchanged: all SIGN, (iii) on the repaired proof now of record.» (l. 223). Third round (L-3, wording only): REFEREE §C
  add. 1 «All statements stay SIGN as in §C.» (l. 273); REFEREE-2 Addendum 2 «Statements all SIGN.» (l. 245). No gap remains; nothing is
  REFUSED. Setting: R104's IDEAL model on acyclic Ξ-graphs on 𝓛^R_d (R110); R113's c_l, γ_l, flip, F(l), cv; R105's ε and ranks.
  Statements as signed (packet §2 with fixes entry 1):
  (a) Notation (§1 l. 18-29): o_l(s), c_(l+1)(s) = o_l(s); j-b-steps and j-windows; doubling; for a doubling level and a window with one
    move of each member u₁(W) < u₂(W), f(W), x₂(W), PULSE(W), GAP(W); cv_s, v_s(x, k), π_s(x), chain_s(x, k).
  (b) Lemma 0 MOVE (§2 l. 31-32) [𝓛^R_d, level l ≥ 1]: «a mover x of level l ≥ 1 moves at step t iff its other option is strictly better
    under s_(t−1) and c_l(s_t) ≠ s_(t−1)(x); it then moves to c_l(s_t).»
  (c) Lemma 1 DOUBLE-EQ (E1)-(E5) (§2 l. 33-36) [1 ≤ j ≤ d − 1, level j doubling]: (E1) Φ(0) = 2, Φ(T) = 0; (E2) Φ(t − 1) = 0 at every
    j-b-step; (E3) «no step moves both members, and pair j flips exactly at the steps that move a member»; (E4) «in every j-window each
    member moves exactly once»; (E5) «if F(j − 1) ≥ 1, the first mover f is the same member in every j-window (and γ_j(0) = γ_j(1))». Its
    proof re-proves R113's PAIR-DOUBLE bound F(j) ≤ 2 + 2F(j − 1) (REFEREE l. 49-50).
  (d) Lemma 2 PULSE-NEST (§2 l. 37-38) [levels j, …, j + k doubling, k ≥ 0, j + k ≤ d − 1]: «every j-window has PULSE ≥ k + 1».
  (e) Lemma 3 GAP-NEST (§2 l. 39-40) [the same, k ≥ 1]: «GAP(W) ≥ k + 1 for consecutive j-windows W, W⁺», with the capped corollary «PULSE
    and GAP of every j-window are ≥ h − j for 1 ≤ j ≤ h − 2».
  (f) Lemma 4 DOMINANCE-FREEZE (§2 l. 41-44) [a mover x, a state s; (b): x a member of pair j, level j doubling]: (a) «π_s(x) is determined
    by dec_s(x)»; (b) «dec(x) is not constant on s_(t−1), …, s_(t′−1)» for consecutive moves t < t′ of x.
  (g) Lemma 5 CROSS-ECONOMY (§2 l. 45-51) [level j doubling, pair j crossed onto A_0 ≠ A_1 outside it]: (i) the threshold form of π for
    each member; (ii) «In every j-window: [D(s_(u₁−1)) > θ_f] ≠ [D(s_(u₂−1)) > θ_(x₂)].»; (iii) under the RANK hypothesis at both pre-states, D
    changes sign between s_(u₁−1) and s_(u₂−1), proved by the proof of record (fixes entry 1 §1, REFEREE's repair); its closing «and nothing
    else is required of it there» is a READING, not signed (REFEREE l. 113-114).
- The RESULTS line (L-3, the title): «In the IDEAL model of RESULTS R104 (premise: R104's definition of the model only, no theorem of
  R104 used; RESULTS R105's ENC only;» … «on acyclic Ξ-graphs on 𝓛^R_d,» … «(2026-11-07) — a STRUCTURE statement inside the IDEAL model
  on doubling levels of 2-wide ladders» … «are not covered; the proof of record of CROSS-ECONOMY's sign-change clause is
  referee-originated (REFEREE R-P-TOWER-FUEL §3, restated in P-TOWER-FUEL's fixes entry 1 §1; REFEREE-2's own repair is a second route),
  signed by both referees; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim (DATA:» … «(P-TOWER-FUEL,
  docs/lower/P-TOWER-FUEL.md with its fixes entry 1, docs/lower/P-TOWER-FUEL-fixes.md; L-LOWER successors 5-6)». Its clauses: notation =
  (a) in words; MOVE = (b); DOUBLE-EQ = (c) (E3)-(E5) without the γ clause; PULSE-NEST = (d); GAP-NEST = (e); DOMINANCE-FREEZE = (f);
  CROSS-ECONOMY = (g) (ii), (iii); instances = packet §4 as fixed by entry 1 §2-§3 (DATA). Its DATA: the parenthesis «(DATA:
  experiments/lower/l5/p_tower_check.py on 24 runs from the stored start …)», clause by clause. What R1-R4 change (C134 §5): R1 the
  source note (it names fixes entry 1, which carries the proof of record and the measured instance units and scopes, and the successors
  5-6); R2 the scope tail's L41 sentence (see L41 and L43); R3 the drop words, «not a gauntlet step» → «not a step-4 pass», the landed
  wording; R4 the unit and set of I-FUEL's PULSE, GAP clause, «(unit = j-window; set = all 119 of them)», as in I-ROOM's. «No statement,
  proof, definition or instance changes.» (C134 l. 17-18).
- Premise: RESULTS R104's definition of the IDEAL model only, no theorem of R104; RESULTS R105's ENC only («the Ξ-order of β-sets is the
  order of the integers Σ ±2^rank (+ for even parity), so … the value of option (x, k) is ε(x, k) plus the current value of its Ξ-target»,
  R105 l. 10155), for Lemmas 4 and 5; RESULTS R110's definition of 𝓛^R_d only («movers 2l and 2l + 1 on level l, all of degree 2, no other
  movers, option k of a mover of level l ≥ 1 W-pointing to mover 2(l − 1) + k», l. 11323); RESULTS R113's ALIGN only («on 𝓛^R_d, for 1 ≤ l
  ≤ d − 1 and every state s of a run, both movers 2l and 2l + 1 have KP_s = c_l(s), each of them that moves at step t moves to option
  c_l(s_t), and the order of their keys under s is [s(2l) = c_l(s)] if s(2l) ≠ s(2l + 1) and γ_l(j) if both are on option j», l. 12152),
  with its notation c_l, γ_l, flip, F(l) and cv, for Lemmas 0 and 1 and through them 2-5. R113 is stated on acyclic Ξ-graphs, as this line
  is. Both referees checked every premise quote against RESULTS (REFEREE l. 38-52; REFEREE-2 l. 28-37); no R116, R119 or lane item is used.
- L41 and L43. The packet's proofs are L-LOWER successor 5's, except one: the proof of record of CROSS-ECONOMY (iii) is REFEREE
  successor 27's repair (R-P-TOWER-FUEL §3, l. 107-112), restated in fixes entry 1 §1 under the Lead's ruling of 15:18Z; the packet's
  own step (its first inequality) is false (REFEREE: 57 of 86 RANK states; REFEREE-2: 651 of 1,010). REFEREE signs it (§C l. 251-252);
  REFEREE-2, which wrote its own repair before reading REFEREE (report l. 70-74, «Independent: docs/referee/ not read on this item.», l.
  2), checked the proof of record and signs (Add. 1 l. 209-214, l. 223). This is L41's case (DECISIONS l. 355-358), as the Lead ruled
  («E-2 (G-7, L41; Lead ruling).», C134 l. 25; there «L41 requires the scope tail to say so», l. 26-27); L-3's scope tail says so (R2,
  the first fill's R-G): «the proof of record of CROSS-ECONOMY's sign-change clause is referee-originated (REFEREE R-P-TOWER-FUEL §3,
  restated in P-TOWER-FUEL's fixes entry 1 §1; REFEREE-2's own repair is a second route), signed by both referees». Both referees read
  R2 in meaning (REFEREE §C add. 1 «R2: CORRECT and correctly attributed.», l. 265; REFEREE-2 Addendum 2 «R2 is true and is what my
  Addendum 1 says.», l. 237). L43: no statement is asymptotic; the two instances are DATA, not DEAD.
- Fixes (docs/lower/P-TOWER-FUEL-fixes.md, append-only; entry 1 by L-LOWER successor 6 at 740f6c79, written by
  experiments/lower/l5/mkfix_tf.py, the file then 93 lines, 9,973 bytes, sha1 0902efb9eaea48501e4289a8ce3980b235347ac8, «Merged under
  the Lead rulings of 15:18Z (Lead reading).», l. 7; entry 2 by L-LOWER successor 7 at 4f25ae6f, written by
  experiments/lower/l5/mkfix2_tf.py, l. 95-144, the file now 144 lines, 15,426 bytes, sha1 c99bfd3acb8e062fd7b05fec98a5898a7ac883d2):
  - §1 TF-1 = W-1: the packet's proof sentence replaced by the «Proof of record (REFEREE's repair; it uses only the packet's Lemma 4 (a),
    ENC and acyclicity)» (l. 18-24); the «Independent second route (REFEREE-2's repair, recorded, not needed for the record)» (l. 25-31).
  - §2 TF-3: the 30 I-ROOM units are (5-window, PULSE or GAP) units on 16 distinct 5-windows.
  - §3 TF-4 = W-3: the I-FUEL sentence replaced by measured scopes (48 / 48 at some pre-state, 32 / 48 at s_(a−1), 16 / 48 at every
    pre-state, 0 / 79 good; 188 of 188 consecutive-move pairs with a non-constant decider) and a READING («READING: the room conditions are
    met and the missing piece is fuel»); Lemma 4 (b) is no longer said to be violated.
  - §4: E5's hypothesis F(j − 1) ≥ 1 holds on 61 of the 62 doubling (run, level) pairs; TF-2 = N-1 recorded, statement NOT changed.
  - §5: line L-2 = L-1 with M1-M7 (above); p_tower_check.py extended to pin L-2 and to assert 7,069, 61, 119, 16, 32, 16 and 188.
  - §6: the description slip (L-1 is 3,834 bytes, 3,699 characters).
  - Entry 2 (CHECKER C134's fix round; l. 95-144): §1 C134's four findings E-1..E-4 and N-1, each quoted from C134 by the script; §2
    R1-R4 with C134 §5's joining rule; §3 line L-3 (made by experiments/lower/l5/mkL3_tf.py, which asserts C134's target sha1 and byte
    count) and p_tower_check.py extended to pin L-3 and to assert SL41_d28's 119 j-windows (3, 7, 15, 31, 63). E-1 (the source note) by
    R1 (the first fill's R-B); E-2 (L41: the proof of record is referee-originated) by R2 (R-G); E-3 (the scope words; C134's ruling on
    the UPDATE procedure) by R3 (R-U); E-4 (the unit and set of I-FUEL's PULSE, GAP clause) by R4 (R-S). The first fill's optional R-C
    is not taken («R-C is not taken (N-1).», C134 l. 17).
  - No statement of the packet changes; entry 1 replaces one proof, re-measures §4 and rewrites the line; entry 2 rewrites the line
    only.
- Not signed: packet §4, §5 (DATA), the READING of fixes §3, TF-2 / N-1, the packet's «Not claimed» items, BOX L6 (lane).
- Referee strengthening (NOT part of this entry; referee checks):
  (i) REFEREE: own replay tools on its own IDEAL simulator t3r_sim.py (docs/referee/scratch/tf_replay.py, tf_units.py; no L-LOWER code
    imported): both instances and every §5 counter reproduced exactly (l. 116-137); extra counters with 0 violations: MOVE both directions
    on 72,974 (step, mover of level ≥ 1) units, E1 and E2 on 62 levels, γ_j(0) = γ_j(1) on 62, PAIR-DOUBLE on every (run, level ≥ 1), Lemma
    4 (a) at every state on 77,674 (state, mover) units, Lemma 5 (i) at every state on 185 (l. 138-139); mutants (l. 140-142); the decider
    scope table (l. 125-133).
  (ii) REFEREE-2: own r2tower.py and r2fuel.py on its own R104 simulator r2moves.py, «Lane code was only run, never imported into mine.»
    (l. 8-9): both instances, every §5 counter reproduced (l. 77-104); extra checks with 0 violations (l. 105-109); its repair checked
    pointwise at 1,010 RANK states of the 14 crossed pairs, 0 violations (l. 74); the 188 consecutive-move pairs (r2fuel.out, l. 97-98).
  (iii) The L-3 round: REFEREE §C add. 1 replayed R4's set on its own simulator («My own replay (tf_logs/inst.log, I-FUEL): 3, 7, 15,
    31, 63 = 119 j-windows at j = 1, …, 5, 0 PULSE and 0 GAP violations of ≥ 7 − j.», l. 271-272) and checked R2's attribution against
    its own §3 (l. 265-266); REFEREE-2 Addendum 2 counted the same set with its own code («SL41_d28 has 3 + 7 + 15 + 31 + 63 = 119
    j-windows at j = 1..5», l. 240) and read R3 against its own TARGET diff (l. 242-243).
- Honest limits: (i) Nothing is bounded polynomially; the lemmas are necessary conditions for doubling levels (room: PULSE-NEST,
  GAP-NEST; fuel: DOMINANCE-FREEZE, CROSS-ECONOMY), not a bound on their number, and nothing is claimed about T^R(d). (ii) The two
  instances are DATA from one start each; they say what a seventh capped level would need on those runs, not that it is impossible; the
  plateau F(6) = 222 is not claimed a cap. (iii) DOMINANCE-FREEZE (a) is counted on consecutive states only (65,885 equal-decider
  units); the every-state check is referee data. (iv) MOVE has no DATA of its own in the line (referee data only). (v) All DATA runs are
  runs of implementations (l3/sim.py; the referees' own simulators), from stored starts only. (vi) Names: «MOVE», «DOUBLE-EQ»,
  «PULSE-NEST», «GAP-NEST», «DOMINANCE-FREEZE», «CROSS-ECONOMY» are new to RESULTS; DOUBLE-EQ overlaps R119's DBL-EQ in content and is
  re-proved here from ALIGN; «PULSE-NEST» is also L-SI's lane name; «R120» is also an old L-RED round label
  (docs/red/R120-reset-lin.md), not a RESULTS label. (vii) No literature source is cited and no novelty is claimed. (viii) CHECKER C134
  (85e4cdea, 23871f48) FAILED the first fill (draft 752f9531, on L-2) with E-1..E-4, all line wording («No statement, proof, definition
  or instance changes.», C134 l. 17-18); L-3 resolves them by R1-R4 (Fixes).
- Data (DATA, not proof): experiments/lower/l5/p_tower_check.py at l-lower 4f25ae6f (177 lines; 172 at 740f6c79; simulator
  experiments/lower/l3/sim.py, R104's IDEAL model): pins (the two instances, L-1, L-2, L-3); §(2) the instance counts of I-ROOM and
  I-FUEL, with SL41_d28's 119 j-windows at j = 1..5 (3, 7, 15, 31, 63) asserted since 4f25ae6f (fixes entry 2 §3; the set of R4's
  clause); §(3) the counters E3, E4, E5, PN, GN, DF, DFa, CE (ii), CE (iii) on the 24 runs, every count asserted against an expected
  table (l. 172-176; l. 167-171 at 740f6c79). Wired into experiments/lower/check.sh (l. 49-50), run by scripts/verify.sh. Re-run from a
  git archive of 4f25ae6f at the second fill: the whole experiments/lower/check.sh, 2026-11-07T19:29:33Z-19:29:46Z, rc 0, 54 output
  lines, «pins OK: 5 files», «SL41_d28: 119 j-windows at j = 1..5 (3, 7, 15, 31, 63)», «P-TOWER-FUEL CHECK PASS», the counters line
  equal to the first fill's; and from a git archive of the l-lower head 8cc6ebc6 (BOX L7 added), 2026-11-07T19:36:55Z-19:37:07Z, rc 0,
  the same 54 lines and «L7 CHECK PASS» (first fill: from f62faf37, 2026-11-07T16:23:15Z-16:23:27Z, rc 0, «pins OK: 4 files»; CHECKER
  C134 §4: p_tower_check.py from git archive 2a89b7f2, rc 0; both referees re-ran it at 4f25ae6f, REFEREE §C add. 1 l. 258-259,
  REFEREE-2 Addendum 2 l. 231-232, and at 740f6c79, REFEREE §C l. 219, exit 0, REFEREE-2 Add. 1 l. 184-185). Sets: the 15 genomes
  experiments/lower/l3/kill/*.json, the 7 genomes experiments/lower/l4/rec/*.json and the two instances
  experiments/lower/l4/rec/G7_best_d28.txt (b995fff2…) and experiments/lower/l5/rec/SL41_d28.txt (c1b46c31…), each from its stored
  start: 24 runs, 1,999 steps, 62 doubling (run, level) pairs, 757 j-windows. Independent simulators named by the packet (§5): fev.c,
  utmpl.c and L-NEW's box150 Gen via l3/xcheck.py (identical T and F on both instances; lane DATA).
- Signatures: REFEREE docs/referee/R-P-TOWER-FUEL.md: successor 27's report 807984e3 (2026-11-07T14:42:53Z; «Written from
  2026-11-07T14:41Z (date -u); the header time of record is the commit time.»), «I did NOT read docs/referee-2/ for this report.» (l.
  3), verdict table l. 5-19; §C d39fc93a (2026-11-07T15:53:22Z), l. 213-252, «Independence: I read docs/referee-2/R2-P-TOWER-FUEL.md
  (4bede4dd) only after 807984e3 was on origin.» (l. 223), verdict l. 251-252: «Verdict: fixes entry 1 CORRECT. L-2 MATCHES (byte test
  and meaning). All statements SIGNED as in §0; CROSS-ECONOMY (iii) is now SIGN (TF-1 closed by the proof of record). TF-L1..TF-L5,
  TF-3, TF-4 CLOSED.»; §C add. 1 af752251cf6a8afaf25073a960189b2281d9cbe1 (2026-11-07T19:08:39Z; heading «date -u at writing
  2026-11-07T19:08Z»), l. 254-273, «Verdict: L-3 MATCHES, by the byte test and in meaning. All statements stay SIGN as in §C.» (l. 273).
  REFEREE-2 docs/referee-2/R2-P-TOWER-FUEL.md: successor 31's report 4bede4dd (2026-11-07T14:40:11Z), «Independent: docs/referee/ not
  read on this item.» (l. 2), verdict table l. 11-26; Addendum 1 fa010874 (2026-11-07T15:53:15Z), l. 179-223, REFEREE's report «was read
  only now, after my report (4bede4dd) was on origin.» (l. 186), verdict l. 222-223: «**L-2 MATCHES** the packet with fixes entry 1, in
  bytes and in meaning» … «Statement verdicts are unchanged: all SIGN, (iii) on the repaired proof now of record.»; Addendum 2
  e72661d01602ab9c629cd1fe01676c98a7ae15ec (2026-11-07T19:08:25Z; heading «2026-11-07 19:1xZ by date -u»), l. 225-245, with
  R2-P-TOWER-FUEL/bt_l3.py, bt_l3.out and lanecheck_4f25ae6f.out, «**Verdict:** **L-3 MATCHES** the packet with fixes entries 1-2, in
  bytes and in meaning (Opus 5.5, D1). Statements all SIGN.» (l. 245). Lane (claude/l-lower): L-LOWER successor 5, 7f7ff6f5 (packet
  FROZEN, L-1); successor 6, 740f6c79 (fixes entry 1, L-2); successor 7, 4f25ae6f (fixes entry 2, L-3).
- INDEPENDENCE: the packet's proofs are L-LOWER's except (iii)'s proof of record (L41, above); each referee re-derived every step
  (REFEREE §3; REFEREE-2 «## Proofs (own re-derivation)») and replayed the statements on a simulator that is not the lane's (REFEREE:
  t3r_sim.py; REFEREE-2: r2moves.py). Each referee wrote its first report without reading the other's (REFEREE l. 3; REFEREE-2 l. 2),
  and each found the false proof step and repaired it on its own (REFEREE l. 100-112; REFEREE-2 l. 65-74); the repairs are the same
  argument (REFEREE §C l. 240-241: «REFEREE-2's route is the same argument written through ENC directly; both are sound.»). The L-2
  wording merges both referees' line items under the Lead's rulings (M1-M7); each referee judged the merged strings for meaning against
  its own items (REFEREE §C l. 224-237; REFEREE-2 Add. 1 l. 196-208). L-3's further wording (R1-R4) is CHECKER C134's (the first fill's
  R-B, R-G, R-U, R-S, taken by C134; R-B and R-G by the Lead's rulings); in the L-3 round each referee byte-tested L-3 with its own
  script and read R1-R4 in meaning (REFEREE §C add. 1 l. 260-272, scratch/tf_l3.py; REFEREE-2 Addendum 2 l. 233-244, bt_l3.py).
- TARGET.md diff: TARGET.md §1 defines a parity game; the IDEAL model of R104 is a step rule on genomes (R104's definition), not a
  parity-game solver, and no statement of this entry mentions a parity game, a winning region, an algorithm's running time or a
  complexity class (packet §7: «No statement mentions a parity game, a winning region, an algorithm's running time or a complexity
  class»; REFEREE §7 l. 203-204 «Nothing bounds T polynomially; the line says G-N5-TIME stays OPEN, not M3, not a gauntlet step, not a
  TARGET.md claim. CLEAN.»; REFEREE-2 l. 163 «Not M3/M4, not a gauntlet step (§5 does not apply); G-N5-TIME OPEN ✓.»). «d» is the ladder
  depth, not TARGET.md's number of priorities (REFEREE l. 205). No statement bounds T polynomially (L-3: «bounds nothing polynomially»).
  It is not an algorithm claim, so TARGET.md §5's gauntlet does not apply, and it is not a step-4 pass. L-3 carries the scope tail
  «G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim» (R3, by script). The referees' first-round TARGET diffs
  quoted above read L-1's «not a gauntlet step»; both read R3 as the same meaning (REFEREE §C add. 1 «R3: CORRECT, same meaning.», l.
  269; REFEREE-2 Addendum 2 «the packet is not an algorithm claim, so no gauntlet step applies (TARGET.md §5, my TARGET diff).», l.
  242). GAPS G-N5-TIME: open.

Proposed GAPS line-11 UPDATE (append-only), to go AFTER the last UPDATE on GAPS l. 11 at landing (R119's, «UPDATE 2026-11-07 16:38Z:
RESULTS R119 (P-IDEAL-DBL; CHECKER C133 b86962ae)», the last at this second fill, at the local trunk c8bdafe2), as a pure insertion with
one separating space before the row's closing « |». BUILT FROM L-3 by upd120b.py (R105's procedure, unchanged, as CHECKER C134 E-3
rules: sentinel_build with its default drops and R111's / R116's DEAD-clause step for the instances clause; controls R97-R116 rebuilt
byte for byte and the R117, R118 and R119 controls as landed, each compared with GAPS l. 11, True ×23; sha1
17cba597ebbf57e12dce1f328cc2ccc6a0865ea3 of the line without newline and unfilled, = C134 §5's). <DATE>, <HH:MM> and <checker> are the
landing date, time and the C134 commit, all filled at landing:
UPDATE <DATE> <HH:MM>Z: RESULTS R120 (P-TOWER-FUEL; CHECKER C134 <checker>) [refereed-only] LANDED: In the IDEAL model of RESULTS R104 (premise: R104's definition of the model only, no theorem of R104 used; RESULTS R105's ENC only; RESULTS R110's definition of 𝓛^R_d only; and RESULTS R113's ALIGN only, with its notation c_l, γ_l, flip, F(l) and cv), on acyclic Ξ-graphs on 𝓛^R_d, with a j-window a maximal set of consecutive steps containing no change of c_j except possibly at its first step, level j doubling if F(j) = 2F(j − 1) + 2, and for a doubling level j and consecutive j-windows W, W⁺ with move steps u₁(W) < u₂(W) of the pair j PULSE(W) := u₂(W) − u₁(W) and GAP(W) := u₁(W⁺) − u₂(W), and dec_s(x) the option of largest rank in the symmetric difference of the Ξ-chains of x's two options under s together with its side: a mover x of level l ≥ 1 moves at step t iff its other option is strictly better under s_(t−1) and c_l(s_t) ≠ s_(t−1)(x), and then moves to c_l(s_t) (MOVE); if level j is doubling then no step moves both members of pair j, the pair flips exactly at the steps moving a member, each member moves exactly once in every j-window, and if F(j − 1) ≥ 1 the first mover is the same member in every j-window (DOUBLE-EQ); if levels j, …, j + k are doubling then PULSE ≥ k + 1 on every j-window (PULSE-NEST); if moreover k ≥ 1 then GAP ≥ k + 1, so with levels 0, …, h − 1 capped (F(l) = 2^(l+2) − 2) PULSE and GAP are ≥ h − j for 1 ≤ j ≤ h − 2 (GAP-NEST); the option of larger value of x under s is fixed by dec_s(x), and for a member x of a doubling pair and consecutive moves t < t′ of x, dec(x) is not constant on s_(t−1), …, s_(t′−1) (DOMINANCE-FREEZE); if level j is doubling and pair j is crossed onto two movers A_0 ≠ A_1 outside it (xt(2j, k) = A_k = xt(2j + 1, 1 − k)), then with D := cv(A_0) − cv(A_1) and the member thresholds θ_(2j) := ε(2j, 1) − ε(2j, 0), θ_(2j+1) := ε(2j + 1, 0) − ε(2j + 1, 1), in every j-window [D(s_(u₁−1)) > θ_f] ≠ [D(s_(u₂−1)) > θ_(x₂)] for the first and second movers f, x₂, and D changes sign between s_(u₁−1) and s_(u₂−1) whenever at both states the largest rank in the symmetric difference of the Ξ-chains of the current options of A_0 and A_1 exceeds the ranks of the four options of pair j (CROSS-ECONOMY); instances (DATA, stored start): experiments/lower/l4/rec/G7_best_d28.txt (sha1 b995fff2…; levels 0-5 capped, F(6) = 222) violates PULSE, GAP ≥ 7 − j at levels j = 1, …, 5 (unit = j-window; set = all 119 of them) only at level 5, 30 times (unit = (5-window, PULSE or GAP); in 16 of its 63 5-windows) (15 pulses and 14 gaps of length 1 in the 5-windows opened by mover 9 moving to option 1, and 1 pulse of the first 5-window), and experiments/lower/l5/rec/SL41_d28.txt (sha1 c1b46c31…; levels 0-5 capped, F(6) = 222) meets PULSE, GAP ≥ 7 − j at levels 1-5 (unit = j-window; set = all 119 of them) while 48 of its 127 6-windows do not have exactly one move of each member of pair 6 (the movers 12 and 13, crossed onto movers 22, 11), and in each of these 48 windows [a, e] the option (9, 1) of rank 87 is dec_s(12) or dec_s(13) at some state s among s_(a−1), …, s_(e−1) (at every such state in 16 of them; at no such state in any of the other 79): a STRUCTURE statement inside the IDEAL model on doubling levels of 2-wide ladders (room: PULSE-NEST, GAP-NEST; fuel: DOMINANCE-FREEZE, CROSS-ECONOMY), with two obstruction instances for a seventh capped level; bounds nothing polynomially and does not claim that F(6) = 222 is a cap or any bound on T^R(d); Ξ-cyclic genomes and genomes outside 𝓛^R_d are not covered; the proof of record of CROSS-ECONOMY's sign-change clause is referee-originated (REFEREE R-P-TOWER-FUEL §3, restated in P-TOWER-FUEL's fixes entry 1 §1; REFEREE-2's own repair is a second route), signed by both referees; DATA: experiments/lower/l5/p_tower_check.py on 24 runs from the stored start (the 15 genomes experiments/lower/l3/kill/*.json, the 7 genomes experiments/lower/l4/rec/*.json and the two instances), 62 doubling (run, level) pairs, 757 j-windows: DOUBLE-EQ 0 violations (its first two clauses on 7,069 (step, doubling level) units, its third on the 757 j-windows, its fourth on the 62 doubling (run, level) pairs, 61 of them with F(j − 1) ≥ 1); PULSE-NEST 0 on 757 windows, attained on 215; GAP-NEST 0 on 260 window pairs, attained on 12; DOMINANCE-FREEZE 0 on 65,885 (consecutive-state pair, mover) units with equal deciders and on 1,390 (member of a doubling pair, pair of consecutive moves) units; CROSS-ECONOMY 0 on the 65 windows of 4 crossed doubling pairs, its sign clause on 43; MOVE: no separate DATA; the two instances re-derived exactly (P-TOWER-FUEL, docs/lower/P-TOWER-FUEL.md with its fixes entry 1, docs/lower/P-TOWER-FUEL-fixes.md; L-LOWER successors 5-6). G-N5-TIME stays open.

Addendum (subagent, for the Lead; does not land; written 2026-11-07T16:42:43Z by date -u). (1) FIRST FILL on line L-2 (l-lower 740f6c79, sha1
d866ca50…), to CHECKER C134. I edited docs/agents/R120-draft.md only; no merge, no commit and no push by me; the Lead commits this file.
Re-fetch at 2026-11-07T16:35:56Z: l-lower f62faf37, referee d39fc93a, referee-2 fa010874, checker ca749d6e, origin trunk 498a44e4 (unchanged
since 16:19Z); local trunk HEAD 0c317432. Re-fetch at 16:39Z: l-lower 559be040 (BOX L6 only, see the preface), referee d39fc93a,
referee-2 fa010874, checker b86962ae (C133 Add. 1), origin trunk 0c317432; local trunk HEAD 2f98d985 (R119 landed by the Lead at 16:38:28Z;
git status then showed only this file as untracked). (2) TITLE l. 313 = "### R120 [refereed-only] " + L-2 without its newline + ",
CHECKER PASS (docs/checker/C134.md, checker PENDING)", checked by script (chk120.py): equal, byte for byte (True); the only «### R»
heading of this file; 4,516 characters, 4,664 bytes, sha1 of the heading line without its newline 115d16fa0c50f371b0be612e29e14860f5347006;
81 «(» / 81 «)» (L-2's 80 and the fill's), depth never negative, 0 "|", «R1xx» 0, «[refereed-only]» once. (3) SHAPE. The entry block is
l. 313-458 (python slice d[312:458]), followed by a blank line; 0 "|" in it; one «PENDING», the title's fill «checker PENDING)». The GAPS
preamble is l. 460-467; the UPDATE is l. 468 (d[467]), one line, sha1 fba98779231a4fb5b871d93aa7106f313baec4f2 without newline and
unfilled (= upd120L2.txt, True), 4,617 bytes, 4,471 characters, 813 tokens, 79 «(» / 79 «)», 0 "|", one each of «<DATE>», «<HH:MM>»,
«<checker>», «2026-11-07» 0 times. A landing script slices d[312:458] for the entry and reads d[467] for the UPDATE, with «R120», «C134»,
PREV = R119's block and UPDATE (landed, G-P). (4) WHAT IS LEFT: CHECKER's rulings on G-1 (R-B), G-7 (R-G; L41, the Lead's 15:18Z ruling
already names the proof of record), G-U (the UPDATE procedure; optional R-U) and the optional R-S, R-C; then an L-3 by L-LOWER (fixes
entry 2), both referees' byte tests, and a second fill (title, line history, Data, Signatures, the L41 sentence in the body, UPDATE
rebuilt from L-3 with the controls R97-R119 as landed). (5) QUOTE SWEEP (chk120.py: chk119b.py's rule, outermost guillemet quotes split at
«…», parts of 6+ characters, whitespace-normalised, NO docs/agents draft as a source; sources: the trunk docs at HEAD (RESULTS, GAPS,
DECISIONS, DECISIONS-INDEX, TARGET.md, CLAUDE.md, LEAD-STATE, NOW, scripts/verify.sh); at 7f7ff6f5, 740f6c79 and f62faf37 the packet,
fixes, L-1, L-2, experiments/lower/check.sh, p_tower_check.py, mkL2_tf.py, mkfix_tf.py and notes/L-LOWER.md; REFEREE's file at 807984e3
and d39fc93a, REFEREE-2's at 4bede4dd and fa010874; C116, C122, C125-C133 and notes/CHECKER.md on claude/checker; the commit subjects
cited, 2f98d985's, 559be040's and b86962ae's included; my outputs, upd119b.py and upd120.py): title and body 79 quotes, 76 parts, 0 not found; GAPS preamble and UPDATE 5 quotes, 4 parts, 0 not found; preface 206 quotes, 179 parts, 0 not found; this Addendum 50 quotes, 37 parts, 0 not found; the whole file 340 quotes, 296 parts, 0 not found (same script on the final file). Line-precise (lp120.py): 63 of 63 (source, cited lines, quote) triples of this draft found inside the cited
lines (REFEREE l. 2, 3, 10, 12, 15, 18, 21, 26, 52, 113-114, 134, 203-204, 221-223, 225, 231, 239-241, 251-252; REFEREE-2 l. 2, 5, 7, 8-9,
20-22, 25-26, 163, 179, 186, 193-194, 199-200, 210, 213, 222-223; fixes l. 7, 18-19, 25, 46-47, 72-73; packet l. 3-6, 37, 110, 129-130;
p_tower_check.py l. 90, 96; check.sh l. 50; DECISIONS l. 356-358; LEAD-STATE l. 2545; C116 l. 67; C132 l. 47; C133 l. 24; RESULTS l.
10155, 11323, 12152). (6) STALE STATUS (chk120.py): title «PENDING» 1 (the fill); body «NOT YET» 1 (REFEREE's L-1 verdict, quoted as
history) and one first-fill sentence in L41 and L43 (that the scope tail does not yet say so, draft G-7, R-G), to be re-worded at the
second fill; «pending», «candidate», «will », «awaiting», «to come», «not landed», «not on origin», «pushing», «second fill» 0 in the body;
GAPS preamble and UPDATE 0; line 1 «NOT LANDED» 1 (R120 is not landed). Model names: 0 in this file (the referees' role notes are not
quoted). (7) LANDING SIMULATION. (a) sim120b.py on the local trunk 2f98d985 (R119 LANDED; sim117.py's parts() and land(), unchanged, on
in-memory copies of RESULTS b6038515… and GAPS 3825c35d…): R120 a pure insertion (True) directly before «**Erratum E-1**»; RESULTS l. 1
to the end of R119's block byte-unchanged (True); every line after the insertion byte-unchanged (Errata, Note E-3, Dead ends with DE37):
True; RESULTS 14,756 → 14,903 lines (+147); R118 l. 13,607, R119 l. 13,879, R120 at l. 14,114-14,259, blank l. 14,260, «**Erratum E-1**»
to l. 14,261, E-2 14,274, Note E-3 14,302, Dead ends 14,333, DE37 l. 14,871; order R110-R120, E-1, E-2, E-3, Dead ends: True. GAPS: only
l. 11 changes, the closing " |" replaced by " " + the filled UPDATE + " |": True; "|" on l. 11 76 → 76; «UPDATE 2026-» 54 → 54 plus one
head with the simulation year 2099 after R119's: True; R120's UPDATE last: True; 23 → 23 lines. (b) Before the landing, sim120.py on
0c317432 (RESULTS 576a89b7…, GAPS ac63d1a7…) with a stand-in R119 (docs/agents/R119-draft.md, sha1 94a2be76…, block d[425:659], UPDATE
d[666] 074e3c05…) then R120: both pure insertions; RESULTS 14,521 → 14,756 → 14,903, R120 at the same lines as in (a); "|" 76 → 76 → 76;
R118's, R119's, R120's UPDATE in that order (True ×7). (c) Cross-check (sim120b.py): the stand-in R119 from the checked draft
(205f6002) on 0c317432, with the landed fill (2026-11-07 16:38 b86962ae) in place of the simulation's, equals RESULTS and GAPS at
2f98d985 (True, True). Fill values used only for the simulation: R119 2099-01-06, R120 2099-01-07, <HH:MM> 00:00, <checker> 0000000.
(8) UPDATE (upd120.py: a copy of r119b/tools/upd119b.py l. 1-228, Parts A-D, without its file write into r119b/ and its pipe-count tail,
and with one assertion relaxed: upd119b.py's Part C2 asserts that R118's UPDATE is the last on l. 11, which R119's landing ended, so
«and last==l.find(h118L)» is dropped (the pre-landing copy upd120a.py keeps it and ran True on 0c317432); new Parts D2-G): controls
R97-R116 rebuilt from their lines and compared with GAPS l. 11, True ×20; R117 (LANDED) True ×4 and R118 (LANDED) True ×4 as in (9)
above; the R119 control: u119 by R116's procedure on L-3 = R119-draft.md d[666] = r119b/upd119L3.txt, unfilled sha1 074e3c05… (True ×3),
and filled with its GAPS l. 11 stamp 2026-11-07 16:38 b86962ae = that segment (True); all controls True ×23, the last UPDATE on l. 11
R119's, R118's before it (True, True). R120 built (G-U): R105's sentinel_build and R111's sentinel_build111 each fail on L-2 as it stands
(the drop words; the «(DATA: » form), the build with the one phrase read as «not a step-4 pass» runs, = the direct build (True). Token
diff L-2 → UPDATE, 12 hunks, 31 tokens out, 30 in: the head inserted («UPDATE <DATE> <HH:MM>Z: RESULTS R120 (P-TOWER-FUEL; CHECKER C134
<checker>) [refereed-only] LANDED:»); the six labels moved behind their clauses («c_l(s_t) (MOVE);», «j-window (DOUBLE-EQ);», «j-window
(PULSE-NEST);», «2 (GAP-NEST);», «s_(t′−1) (DOMINANCE-FREEZE);», «j (CROSS-ECONOMY);»), so the instances clause follows (CROSS-ECONOMY);
«79) (2026-11-07) —» → «79):»; «G-N5-TIME stays OPEN; not M3, not a gauntlet step, not a TARGET.md claim (DATA:» → «DATA:»; «exactly)» →
«exactly»; «5)» → «5). G-N5-TIME stays open.». Nothing else. The UPDATE built before and after R119's landing is the same (sha1
fba98779… both runs). With R-G then R-B (each old string once in L-2 and once in the running line; R-B's old string once in the UPDATE,
R-G's 0 times): L-2 + proposals sha1 87161a3e18354d346e3297d43c77289ccf3b7fd1 (4,869 bytes, 81 / 81, one " — "), its UPDATE by the same
procedure 9896971b28892728d9e1be41b6c0cc0d2ad79dc7 (4,900 bytes; = the L-2 UPDATE with R-B applied and R-G's sentence inserted before «;
DATA: », True; token diff the same 12 hunks). The optional R-S, R-C, R-U each apply once after R-G and R-B (script; all five: sha1
89ac08650c56e2b44ad840a7a711e05f9ac4ee92, 4,999 bytes, 83 / 83; not proposed as a whole). Pipe rule: the filled R120 UPDATE appended after
R119's (landed) keeps 76 "|" on l. 11, R120's last, prefix byte-unchanged (True). (9) NOT VERIFIED / NOT DONE: the referees' tools not
re-run (their files and logs read); scripts/verify.sh not run (experiments/lower/check.sh only, in full, at f62faf37; not re-run at
559be040, whose diff does not touch l3-l5 or check.sh); 𝓛^R_d membership and Ξ-acyclicity of the 24 genomes not re-checked by my own
code (both referees did: REFEREE l. 117, 134; REFEREE-2 l. 78); l3/sim.py run as the lane's simulator, not read beyond its interface, and
no simulator of my own (the IDEAL step is taken from R104 and from both referees' replays on their own simulators); fev.c, utmpl.c and
l3/xcheck.py not run by me (the L3 block of check.sh compares sim.py with L-NEW's box150 Gen on the kill genomes and passed in (b));
mkL2_tf.py not re-run (the report byte copies it reads are not committed; rel120.py makes the same byte test from the reports at
807984e3 and 4bede4dd); R-S, R-C and R-U not built into an UPDATE; no Oink run (L-2 cites no Oink check). (10) Scratch:
/tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad/r120/ (tools/rel120.py, rel120.out;
archf62/ = git archive of f62faf37, checksh.out, blk.start, blk.end, blk.rc; tools/static120.py, static120.out; tools/prem120.py,
prem120.out; tools/upd120a.py (pre-landing), tools/upd120.py, upd120.out, upd120L2.txt, L2prop.txt, upd120prop.txt; tools/chk120.py,
chk_final.out; tools/lp120.py, lp_final.out; tools/sim120.py, sim_final.out; tools/sim120b.py, simb_final.out, R119-205f6002.md;
tools/assemble120.py, R120-src.md, addendum.txt, addtime.txt, sweep.txt, lp.txt, parts/; fetch.out; L1.txt, L2.txt, packet.md, fixes.md,
ref_807984e3.md, ref_d39fc93a.md, ref2_4bede4dd.md, ref2_fa010874.md, mkL2_tf.py, R119L3.txt; R120-draft.md).

Addendum 2 (subagent, for the Lead; does not land; written 2026-11-07T19:45:31Z by date -u). (1) SECOND FILL on line L-3 (l-lower
4f25ae6f, sha1 7328e673…), to CHECKER C134 Add. 1. I edited docs/agents/R120-draft.md only; no merge, no commit and no push by me; the
Lead commits this file. Heads at the second fetch (2026-11-07T19:36:40Z): l-lower 8cc6ebc6 (BOX L7 only, see the SECOND FILL section),
referee af752251, referee-2 e72661d0, checker 23871f48, origin trunk 762c2184; local trunk HEAD c8bdafe2. (2) TITLE l. 427 = "### R120
[refereed-only] " + L-3 without its newline + ", CHECKER PASS (docs/checker/C134.md, checker PENDING)", checked by script (chk120b.py):
equal, byte for byte (True); the only «### R» heading of this file; 4,836 characters, 4,986 bytes, sha1 of the heading line without its
newline 2c17e7476b661ff51eddcc7db7341470d89ab4ba; 83 «(» / 83 «)» (L-3's 82 and the fill's), depth never negative, 0 "|", «R1xx» 0,
«[refereed-only]» once. (3) SHAPE. The entry block is l. 427-631 (python slice d[426:631], 205 lines), followed by a blank line; 0 "|"
in it; one «PENDING», the title's fill «checker PENDING)». The GAPS preamble is l. 633-639; the UPDATE is l. 640 (d[639]), one line,
sha1 17cba597ebbf57e12dce1f328cc2ccc6a0865ea3 without newline and unfilled (= upd120L3.txt and = C134 §5's, True), 4,941 bytes, 4,793
characters, 859 tokens, 81 «(» / 81 «)», 0 "|", one each of «<DATE>», «<HH:MM>», «<checker>», «2026-11-07» 0 times. A landing script
slices d[426:631] for the entry and reads d[639] for the UPDATE, with «R120», «C134», PREV = R119's block and UPDATE (landed, G-P). The
SECOND FILL section is l. 2-115, the first fill's record l. 116-426 (rec120b.py: 752f9531's l. 2-312, byte-unchanged, directly before
the title, True) and the first fill's Addendum l. 642-714 (752f9531's l. 470-542, byte-unchanged, directly after the UPDATE and a blank
line, True). (4) WHAT IS LEFT: CHECKER C134 Add. 1 on this file; the Lead merges claude/l-lower (4f25ae6f or later), claude/referee
(af752251) and claude/referee-2 (e72661d0) before landing, then lands R120 after R119, with <DATE>, <HH:MM> and <checker> filled. (5)
QUOTE SWEEP (chk120b.py: chk120.py's rule, outermost guillemet quotes split at «…», parts of 6+ characters, whitespace-normalised, NO
docs/agents draft as a source; sources as at the first fill plus, at 4f25ae6f and 8cc6ebc6, the packet, fixes, L-1, L-2, L-3, check.sh,
p_tower_check.py, mkL3_tf.py, mkfix2_tf.py, notes/L-LOWER.md and docs/agents/handover-checks/L-LOWER.md; REFEREE's file at af752251 with
tf_l3.py and its two logs, REFEREE-2's at e72661d0 with bt_l3.py, bt_l3.out and lanecheck_4f25ae6f.out; C116, C122, C125-C134 and
notes/CHECKER.md on claude/checker; the subjects of the commits cited; my outputs, upd120b.py included): on the draft before this
Addendum, title and body 116 quotes, 114 parts, 0 not found; GAPS preamble and UPDATE 2 quotes, 1 part, 0 not found; SECOND FILL section
63 quotes, 53 parts, 0 not found; first-fill record 206 quotes, 179 parts, 0 not found; first-fill Addendum 50 quotes, 37 parts, 0 not
found; whole file 437 quotes, 384 parts, 0 not found; negative control (a made-up quote) reported missing (True); the run on the final
file is in chk_final.out. lp120b.py: the 50 quotes and line references new at this fill (REFEREE l. 254-273, REFEREE-2 l. 225-245, fixes
l. 95-135, C134 l. 15-96, p_tower_check.py l. 12-13, 38, 85-86, 172-176 and 740f6c79's l. 167-171, notes/L-LOWER.md l. 5-7, C116 l. 67,
check.sh l. 49-50) each at its cited lines, 0 failed. (6) STALE STATUS (chk120b.py): title «PENDING» 1 (the fill); body «NOT YET» 1
(REFEREE's L-1 verdict, quoted as history) and «second fill» 1 (the Data re-run, as R119's landed entry); GAPS preamble «second fill» 1
(as R119's); first-fill flag words in the body only as history of the replacements (R-B, R-G, R-U, R-S, R-C as the first fill's names)
and in quotes; the strings "does not yet", "L-2 AS IT STANDS", "upd120prop" and "fba98779" 0 times in the entry block, preamble and
UPDATE; line 1 «NOT LANDED» 1 (R120 is not landed). Model names: 2 occurrences, both inside REFEREE-2's quoted L-3 verdict (Object and
Signatures). (7) LANDING SIMULATION (sim120c.py: r120/tools/sim120b.py without its stand-in part; sim117.py's parts() and land(),
unchanged, on in-memory copies of RESULTS b6038515… and GAPS 3825c35d… at the local trunk c8bdafe2): R120 a pure insertion (True)
directly before «**Erratum E-1**»; RESULTS l. 1 to the end of R119's block byte-unchanged (True); every line after the insertion
byte-unchanged (True); RESULTS 14,756 → 14,962 lines (+206); R118 l. 13,607, R119 l. 13,879, R120 at l. 14,114-14,318, blank l. 14,319,
«**Erratum E-1**» to l. 14,320, E-2 14,333, Note E-3 14,361, Dead ends 14,392, DE37 l. 14,930; order R110-R120, E-1, E-2, E-3, Dead
ends: True. GAPS: only l. 11 changes, the closing " |" replaced by " " + the filled UPDATE + " |": True; "|" on l. 11 76 → 76; «UPDATE
2026-» 54 → 54 plus one head with the simulation year 2099 after R119's: True; R120's UPDATE last: True; 23 → 23 lines. Fill values used
only for the simulation: 2099-01-07, 00:00, 0000000. (8) UPDATE: (c) of the SECOND FILL section; upd120b.out has the controls and the 12
token hunks. (9) NOT VERIFIED / NOT DONE: scripts/verify.sh not run (experiments/lower/check.sh only, in full, at 4f25ae6f and at
8cc6ebc6); the referees' tools not re-run (their files and logs read); my static120.py not re-run (no counter changed at 4f25ae6f; the
check.sh counters line is the first fill's); no simulator of my own; no Oink run (L-3 cites no Oink check); notes/L-LOWER.md at 8cc6ebc6
read only through its diff. (10) Scratch:
/tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad/r120b/ (tools/l3rel120.py, l3rel120.out,
tools/l3rel120b.py, l3rel120b.out; arch4f2/ and arch8cc/ = git archives of 4f25ae6f and 8cc6ebc6, checksh.out, checksh8.out, blk.start,
blk.end, blk.rc, blk8.start, blk8.end, blk8.rc; mkl3/ (C134.md, L2.txt, L3.txt, mkL3.out, fixes_e1.md, mkfix2.out); tools/refs120b.py,
refs120b.out; tools/facts120b.py, facts120b.out; tools/upd120b.py, upd120b.out, upd120L3.txt; tools/prem120b.py, premin/, prem120b.out;
tools/chk120b.py, chk_p1.out, chk_p2.out, chk_final.out; tools/lp120b.py, lp_final.out; tools/sim120c.py, sim_final.out;
tools/rec120b.py, rec_final.out; tools/edit120b.py, parts/secondfill.txt, parts/addendum2.txt, filltime.txt, addtime.txt; fetch2.out;
R120-p1.md, R120-p2.md, R120-draft.md).
