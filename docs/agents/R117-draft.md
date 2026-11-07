# Draft RESULTS R117 (Lead; first fill 2026-11-07T06:35:20Z by date -u (subagent) on P-N5-REACH line L-3, docs/new/P-N5-REACH-line-L3.txt, l-new 727163f0, sha1 adfbb3b8219026b23a80b2081a3c227c35730451 (draft sha1 f652c0d3, CHECKER C130 126f9772: FAIL E-1..E-4); SECOND FILL 2026-11-07T09:00:05Z by date -u (subagent) on P-N5-REACH line L-4, docs/new/P-N5-REACH-line-L4.txt, l-new fdf01b8c, sha1 f85a024b8c8caa4c996fcd15bf1e78fbd436b534) — to CHECKER C130 Add. 1 — NOT LANDED; goes after the last landed R-entry, before «**Erratum E-1**»: R116, which landed at 97d17f63 (landing simulation after R116: Addendum 2 (8))
SECOND FILL (2026-11-07T09:00:05Z by date -u, subagent; for CHECKER C130 Add. 1). Read at the origin heads fetched at 2026-11-07T08:50Z
(git fetch of claude/l-new, claude/referee, claude/referee-2, claude/checker; a Lead push.sh was running; I merged, committed and pushed
nothing, and edited docs/agents/R117-draft.md only): l-new 50c80a92 (its ancestor fdf01b8c, 2026-11-07T07:57:34Z, «L-NEW P-N5-REACH
fixes entry 3 + line L-4 (CHECKER C130 E-1..E-4: R1-R4 by script; L-4 = C130's sha1 f85a024b); pins», holds fixes entry 3 and line L-4;
git diff 727163f0 fdf01b8c changes, for P-N5-REACH, only docs/new/P-N5-REACH-fixes.md (+16 lines, entry 3), the new
docs/new/P-N5-REACH-line-L4.txt, experiments/new/box189/reach.pins (fixes be31f774 for 54774088, L-4 added) and check.sh's «P-N5-REACH»
block (the reach.pins sha1 1a075f50 and its PASS line); git diff fdf01b8c 50c80a92 changes no P-N5-REACH file and nothing in box189
(P-N5-XICYC work); the packet, L-1, L-2, L-3 and every box189 tool and output are byte-equal at 727163f0, fdf01b8c and 50c80a92, by
script), referee 419cc268 (2026-11-07T08:23:51Z, REFEREE successor 26's §C add. 2 of R-P-N5-REACH.md, l. 211-247; the file 247 lines,
18,881 bytes, sha1 d986a8c33e71b6a9a26b8e3044bcb3d8dcc91918; its l. 1-209 = 85cc9ebb's file, by diff; the origin head), referee-2
d4838991 (REFEREE-2 successor 30's Addendum 3 of R2-P-N5-REACH.md, l. 175-197, written at d2b08049, 2026-11-07T08:23:41Z, its heading
stamp «08:3xZ» corrected to «08:2xZ» at d4838991, 08:23:54Z; the file 197 lines, 20,330 bytes, sha1
2068ac6b14ecadd08777f75ac4ffe77bac2b4b3f; its l. 1-173 = ddf42cb6's file, by diff; d4838991 IS on origin: it is the origin head of
claude/referee-2, git merge-base --is-ancestor d4838991 origin/claude/referee-2 true at 08:50Z), checker 6aabf98f (C129 Add. 2;
docs/checker/C130.md byte-equal at 126f9772 and 6aabf98f, git diff empty: 135 lines, sha1 42aa8b262bd16ccbf84248d4f80dc902bbb3b6df).
fdf01b8c, 419cc268, d4838991 and 126f9772 are NOT ancestors of the local trunk 172af6ad or of origin trunk 137b5e18 (git merge-base
--is-ancestor); the Lead merges and pushes before landing. Local trunk 172af6ad: R116 LANDED at 97d17f63 (2026-11-07T07:42:55Z, «Lead:
land R116 IDEAL-MOVES (P-IDEAL-MOVES, line L-5; CHECKER C129 Add. 1 9246878c PASS); resume point»), and DE37 landed at 172af6ad
(«appended after DE36, no GAPS change»), which leaves R117's place unchanged. RESULTS at 172af6ad: sha1
8353e283a98aaa921f20c557e382fd8f46a5d288, 14,004 lines; «### R116» l. 13072, «**Erratum E-1**» l. 13362, «**Erratum E-2**» l. 13375,
«**Note E-3**» l. 13403, «## Dead ends (kept;» l. 13434; RESULTS l. 1-13071 byte-equal to the first fill's 0ea36025 (prem117b.py), so
the premise checks stand. GAPS at 172af6ad: sha1 01edd3723a0f64f9065b1aa512395d89b2eaf3de, 23 lines, l. 11 76 "|", 51 «UPDATE 2026-»,
the last R116's «UPDATE 2026-11-07 07:42Z: RESULTS R116 (P-IDEAL-MOVES; CHECKER C129 9246878c)».
New sources: CHECKER C130 (126f9772, 2026-11-07T07:29:13Z): «Verdict: FAIL (E-1 to E-4, all DATA wording; one L-4 with four
replacements, §5)» (l. 16), E-1..E-4 = the first fill's G-9 (i)-(iii) and G-D, notes N-1 (scope) and N-2 (tool and corpus named via the
packet), everything else PASS (title, UPDATE shape, statements, Lead rulings, TARGET diff, quotes 0 not found, placement (B)), and §5's
L-4 (sha1 f85a024b…) and rebuilt UPDATE (b4d74e09…); fixes entry 3 (docs/new/P-N5-REACH-fixes.md l. 71-85 at fdf01b8c, L-NEW successor
59; file 85 lines, 9,935 bytes, sha1 be31f7741264c809ec306889ecb31046c1671598, its l. 1-69 = entry 2's file); line L-4
(docs/new/P-N5-REACH-line-L4.txt, fdf01b8c, the file's only commit); experiments/new/box189/reach.pins at fdf01b8c (24 lines, sha1
1a075f50314bd3fd8a5933b51d41a43b1f2f62a8); experiments/new/check.sh at fdf01b8c (979 lines, sha1
71b788d04a30a401abf786cc6179b2c06c9857f0, blocks l. 943-957 unchanged but for the pins sha1 and the PASS line); REFEREE §C add. 2 (byte
test by its own script, R1-R4 read against the counters, the XC-3 point on K3; l. 246-247 its verdict, quoted in the entry); REFEREE-2
Addendum 3 (own bt_l4.py, R1-R4 read against the counters; l. 196-197 its verdict, quoted in the entry).
Checks run at this fill (scratch /tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad/r117b;
nothing written into the repository but this file). (a) l4rel117.py: L-4 at fdf01b8c is sha1 f85a024b8c8caa4c996fcd15bf1e78fbd436b534,
3,942 bytes, one line with its newline, 3,893 characters, 749 tokens, 64 «(» / 64 «)», depth never negative, final depth 0, 0 "|";
byte-equal at the l-new head 50c80a92; R1-R4 parsed from fixes entry 3 (l. 81-84), from C130 §5 (l. 108-115, wrapped lines joined) and
from the first fill's G-9 / G-D proposals R-A..R-D: the three lists are equal (True, True); each old string once in L-3 and once in the
running line, each new string once in L-4; L-3 + R1-R4 = L-4 (True); 9 token hunks (8 tokens out, 47 in), all inside R1-R4; reach.pins
at fdf01b8c pins L-4 (f85a024b) and the fixes (be31f774) (True); check.sh at fdf01b8c pins reach.pins 1a075f50 (True). (b) check.sh
blocks «BOX 189 REACH» and «P-N5-REACH» from a git archive of fdf01b8c's experiments/ and docs/new/ (check.sh l. 1-7 and l. 943-957 at
fdf01b8c; runblk189b.sh), 2026-11-07T08:51:44Z-08:52:04Z, rc 0, both PASS, the second line «P-N5-REACH: reachcheck re-run = frozen
output (NO-REACH 0/908 states, S3-START 0/454, PAD 0/693030, REACH3 0/454 failures, SUBDIV-DEAD A and B); pins (reach.pins 1a075f50:
packet b7bd6937, line L-1 b12ec57a, fixes be31f774, line L-2 4de27b32, line L-3 adfbb3b8, line L-4 f85a024b, reachcheck c368b363, gamma3
8758456f, subdiv 63c7ae38, output af50ee34, 14 genomes): PASS». (c) xcheck.sh from the same archive with this container's Oink 8fbf0a7
build, 2026-11-07T08:55:43Z-08:55:53Z, rc 0: output byte-equal to xcheck.out (cmp), 28 lines, 28 «OK strategies verified». (d)
upd117b.py (upd117.py with Part C run on L-4 and a new Part B2, the R116 control): the controls R97-R116 rebuilt from their lines byte
for byte and compared with GAPS l. 11 at 172af6ad, True ×20; the R116 control is upd116b.py's R116 section, exec'd unchanged and filled
with R116's landed stamp (2026-11-07, 07:42, 9246878c): equal to GAPS l. 11 (True), to R116-draft.md's UPDATE line and to
r116/fill2/upd116L5.txt with the same fill (True, True), unfilled sha1 c924a0e2… = C129 §5's (True); the last UPDATE on l. 11 is R116's.
R117 rebuilt on L-4: sha1 b4d74e094a30cba61017eeda4a0c33cb7a1db6f3 (no newline, unfilled), 3,973 bytes, 63 «(» / 63 «)», 0 "|", one each
of «<DATE>», «<HH:MM>», «<checker>» = the first fill's prediction (G-D) and C130 §5's value (True); = the first fill's UPDATE ce44ee1f…
with R1-R4 (True); build = direct build (True); the filled UPDATE inserted after R116's, before the row's closing « |», keeps 76 "|" on
l. 11, R117's UPDATE last (True). (e) prem117b.py: L-4's premise parenthesis, and all of L-4 before «: (Theorem NO-REACH)», are
byte-equal to L-3's (True); packet §1's 38 quotes, 0 not found, the same RESULTS and SPEC hits as at the first fill; labels in L-4 R104
7 (R1 adds «R104's stated start»), R57 1, R24 2, R103 1, R36 1, R15 1. (f) chk117b.py (title, block, UPDATE, quote sweep, stale grep)
and (g) sim117b.py (landing simulation on 172af6ad), wd117b.py (word diff), rec117b.py (first-fill record unchanged): Addendum 2.
C130's E-items, resolved in L-4 (string checks by script on L-4, l4rel117.py and chk117b.py): E-1 (NO-REACH count: NR-STD named with a
predicate it does not test, NR-CORE uncited) by R1 = the first fill's R-A: the count now reads «σ(K0) = K1 and σ(K1) = K0 at all 908
states of the S3 runs on Γ(G) and 0 of them equal to R104's stated start off the movers», NR-CORE then NR-STD; «0 standard states» 0
times in L-4. E-2 (no-improving-edge clause without a counter, not in the line's no-DATA list) by R2 = R-B: «NO-REACH's
no-improving-edge clause and Corollary REAL-IDEAL-S3 no separate DATA». E-3 (the 28 games unnamed) by R3 = R-C: «the 28 games Γ(G) and
Γ3(G) of the 14 corpus genomes» and «with verify OK on the same 28»; «28/28» 0 times in L-4. E-4 (DEAD SUBDIV instances not reproducible
from the line) by R4 = R-D: «the n = 3 and n = 5 games with the start pairs of packet §9 (instances A, B)»; «given start pairs» 0 times
in L-4. Each new string once in L-4. C130's notes N-1 and N-2 need no change; the body records them (Honest limits (viii)).
XC-3 NOTE (K3 and SBAR3; changes nothing in the line): REFEREE §C add. 2 l. 236-245 records that K3 (b) uses SBAR3, which is IDEAL-ACYC,
so K3's «every genome» label was incomplete as printed and its own earlier SIGN of that label missed it; fixes entry 1's reply settles
K3 (a)-(d) for every genome; «For R117 nothing changes.» The body carries the note with the exact quotes (the bullet "XC-3 NOTE", after
Claims signed).
Changes at this fill, and nothing else: line 1 (the header); this paragraph; the title (L-4); in the entry: Object (identical at
fdf01b8c; three fixes entries; L-4 the line of record, its line history, the L-4 verdicts of both referees), Claims signed (the L-4
rounds), (e)'s pointer to the new XC-3 NOTE bullet, the XC-3 NOTE (new), The RESULTS line (L-4; the DEAD clause names packet §9's
instances A and B), L41 and L43 (C130's R1-R4; bt_l4.py), Fixes (header, the entry-3 bullet with the E-item resolution, the closing
sentence), Referee strengthening (iv) (new), Honest limits (vi) (packet §11 named without its old wording) and (viii) (C130's E-items
and notes), Data (fdf01b8c; reach.pins 1a075f50; the block and xcheck re-runs at this fill and C130's), Signatures (REFEREE §C add. 2,
REFEREE-2 Addendum 3, the lane commit fdf01b8c), INDEPENDENCE (the L-4 DATA wording and round), TARGET.md diff (L-4); the GAPS preamble
(R116's UPDATE now the last on l. 11; built from L-4) and the UPDATE (rebuilt from L-4); Addendum 2 (new). The FIRST FILL text below
(from "FIRST FILL (this text)" to (14)) and Addendum (1)-(7) are kept byte-unchanged as the record of draft f652c0d3 on L-3
(rec117b.py): where they call L-3 the title line or the current line, quote L-3's DATA phrases as the line's, flag G-9 (i)-(iii) and G-D
or propose R-A..R-D, describe R116 as a draft at C129 Add. 1 and the L-3 rounds as the last referee rounds, or give the first fill's
line numbers, counts, placement and UPDATE sha1 (ce44ee1f…), they describe draft f652c0d3 at 06:35Z; C130 ruled G-9 (i)-(iii) and G-D as
E-1..E-4, used the number C130 (G-0) and PASSED the UPDATE procedure (G-U) and placement (B) (G-P); the entry block now follows L-4.
FIRST FILL (this text). Read at the origin heads fetched from 2026-11-07T04:51Z (git fetch of claude/l-new, claude/referee,
claude/referee-2, claude/checker; a Lead push.sh was running at the start, so nothing was merged or committed until pgrep was empty):
l-new 727163f0 (fixes entry 2 and line L-3; git diff 73b3d1fd 727163f0 changes in experiments/new/box189/ only reach.pins (+3 lines:
the fixes, L-2, L-3) and in docs/new/ adds the fixes, L-2, L-3 and box 190 / P-IDEAL-MOVES files; the packet and L-1 are unchanged;
check.sh gains the box 190 block and the new reach.pins sha1), referee 85cc9ebb (§C add. 1 of R-P-N5-REACH.md; f66942c1, cc9f4afd its ancestors), referee-2 ddf42cb6 (Addendum 2 of R2-P-N5-REACH.md, 2026-11-07T04:50:08Z, fetched 05:42:46Z; b0860fcd, c420666d, 5025b198 its ancestors), checker 2603f321 (C128 Add. 1; an ancestor of the local trunk, merged by the Lead as c02f9065); local trunk 5ec57d84 (R115 landed, see below), f7fcfccd at commit time (Addendum (1)).
Merges and commit: see Addendum (1). Not pushed; the Lead pushes trunk before landing. The body makes NO statement about trunk (C113 E-2).
At the fetch, RESULTS (sha1 555d41bd85b8ea52a1e57459c0a4fe0fcb7f6cc1, 13,306 lines) and GAPS (sha1
3c4ff44d1b822110d9bfd0d1a2d8661ea6b5361e) were as last changed by b6d1484b (R114's landing). During this fill the Lead landed R115 on the
local trunk: 5ec57d84 (2026-11-07T05:07:40Z, «Lead: land R115 IDEAL-IM (P-IDEAL-IM, line L-3; CHECKER C128 Add. 1 2603f321 PASS)»; not
yet on origin when read, a Lead push.sh running). Every check below is on that local trunk: RESULTS sha1
0ea360253a0e102ecf5750e187233ab750d0af04, 13,681 lines; GAPS sha1 19da0f5180dff9e1f90b72222b6118091adb50d4, 23 lines, l. 11 76 "|", 50
«UPDATE 2026-», the last one R115's («UPDATE 2026-11-07 05:07Z: RESULTS R115 (P-IDEAL-IM; CHECKER C128 2603f321) [refereed-only] »).
R116 is NOT landed (see (0) and the landing simulations, Addendum (5)).
Sources read: the packet docs/new/P-N5-REACH.md (frozen 73b3d1fd, 2026-11-07T02:35:31Z, sha1 b7bd693744fdec2aa993f2133c22cbe724933ff0,
345 lines, 39,253 bytes; read in full); line L-1 (73b3d1fd, sha1 b12ec57aa18893701bd88bfdab75e3f7e9cf80e0, 3,105 bytes); fixes entry 1
(571c75c5, 2026-11-07T03:32:05Z; the file then 47 lines, 5,344 bytes, sha1 307651b2779f3df1fb8857de2974d3ffdd69ac6a) and line L-2
(571c75c5, sha1 4de27b32d5ed11accb092cf44cb27e14be6b9609, 3,628 bytes); fixes entry 2 (727163f0, 2026-11-07T04:26:17Z;
docs/new/P-N5-REACH-fixes.md at 727163f0: 69 lines, 7,851 bytes, sha1 547740887c7974798206b4075d67f6a379cbfe47, its l. 1-47 = entry 1's
file, by script) and line L-3 (727163f0, sha1 adfbb3b8219026b23a80b2081a3c227c35730451, 3,748 bytes); experiments/new/box189/
reachcheck.py (sha1 c368b363ff654c8e7aead970f866b7e4d482f793, 183 lines; read in full), reachcheck.out (sha1
af50ee340e11c35209c39496e7354925e832d3eb, 28 lines), gamma3.py (8758456ffb932bb75cdc327114c3023c454f0dc2, 89 lines), subdiv.py
(63c7ae383af5dc1c70bba8ba78cec385afad1382, 41 lines; read in full), reach.pins at 727163f0 (sha1 11ebdbeec367b467691fb10072617c7245fd8ab5,
23 lines: the packet, L-1, the fixes, L-2, L-3, reachcheck.py, gamma3.py, subdiv.py, reachcheck.out and the 14 corpus genomes),
xcheck.sh (eeddd8bb138b7348e497170127bf50f1164e51fd, 11 lines), xcheck.out (cfcf38bb2112d81352d5b7af8c74d60c0562cc3c, 28 lines),
check189.sh, experiments/new/check.sh at 727163f0 (965 lines, sha1 163b9c9e1aef3ef8b4481c864aefb315d01d82b7; blocks «BOX 189 REACH»
l. 943-949 and «P-N5-REACH» l. 950-957); the SPEC file docs/new/N5-ssi-global.md (sha1 66fde9ef1726602fc0a52ca8d6d6fe8cbbcf110e, the
packet's «66fde9ef…»; last commit 7039eb52, 2026-10-18); REFEREE successor 25's docs/referee/R-P-N5-REACH.md (report f66942c1, §C
cc9f4afd, §C add. 1 85cc9ebb) with scratch/reach_replay.py and scratch/subdiv_replay.py (listed, not re-run); REFEREE-2's
docs/referee-2/R2-P-N5-REACH.md (successor 29's report b0860fcd, successor 30's Addendum 1 c420666d, Addendum 2 ddf42cb6) with
R2-P-N5-REACH/ (r2reach.py sha1 8dd52cb4acfc38eafa79da87c956221298b04d69, reachcheck_r2.py, bt_l2.py and their outputs; listed, not
re-run); RESULTS R104 (title l. 9864, body l. 9865-10154), R57 (b) (l. 2915-2916), R36 (c) (l. 1723-1724, 1730-1731), R15 (d) (l.
640-642); R115 (l. 12697-13070), Erratum E-1 (l. 13072), E-2 (l. 13085), Note E-3 (l. 13113), Dead ends (l. 13144), on the local trunk
5ec57d84; GAPS l. 11; DECISIONS-INDEX (L41, L43, L45,
L46, L50) and docs/agents/LEAD-STATE.md l. 2438 (the Lead's REACH rulings); docs/checker/C120.md-C129.md and notes/CHECKER.md on
claude/checker; docs/agents/R104-draft.md, R114-draft.md and R115-draft.md (the models of this draft) and R116-draft.md (first fill).
Re-runs (scratch /tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad/r117, from a git archive
of 727163f0's experiments/ and docs/new/, nothing written into the repository): (a) check.sh blocks «BOX 189 REACH» and «P-N5-REACH»
(check.sh l. 1-7, the shebang, comments, «set» and «cd» lines, then l. 943-957; runblk189.sh, blk189.out), 2026-11-07T04:54:26Z-04:54:43Z,
rc 0, lines «BOX 189 REACH: Gamma3 from S3 = stated start, FL run [0, L(G)] on 3 pinned genomes (L 35, 59, 13); Gamma from S3: 1
iteration; 2 instances regenerated byte-identical: PASS» and «P-N5-REACH: reachcheck re-run = frozen output (NO-REACH 0/908 states,
S3-START 0/454, PAD 0/693030, REACH3 0/454 failures, SUBDIV-DEAD A and B); pins (reach.pins 11ebdbee: packet b7bd6937, line L-1 b12ec57a,
fixes 54774088, line L-2 4de27b32, line L-3 adfbb3b8, reachcheck c368b363, gamma3 8758456f, subdiv 63c7ae38, output af50ee34, 14
genomes): PASS»; (b) xcheck.sh from the same archive with this container's Oink (tools/oink/build/oink, source at 8fbf0a7 by git
rev-parse, built by scripts/setup_oink.sh), 2026-11-07T04:58:52Z-04:59:00Z, rc 0, output byte-equal to the committed xcheck.out
(cmp; xcheck117.out); (c) my split of reachcheck.py's counters (tools/g9split117.py: the frozen source exec'd unchanged, then my own
measurements on its own 454 genomes; my DATA, not lane DATA, not wired into check.sh; g9split117.out, 10.8 s); (d) xcmp117.py: n5b's
counts in xcheck.out against the lane engine's in reachcheck.out; (e) the L-1 → L-2 → L-3 byte and token tests (l3rel117.py); (f) the
premise quote test (prem117.py); (g) the UPDATE build with 19 controls (upd117.py); (h) the title check, quote sweep, stale-status grep
and landing simulations (chk117.py, sim117.py).
LESSONS APPLIED. C113 E-1: the title is L-3 verbatim with no insertion. C114 Add. 1 E-1: the UPDATE head carries «<DATE>». C115 E-1: the
premise route is checked against what RESULTS records (G-4; prem117.py, hits per quote). C116 G-1, C118-C129 §4: the UPDATE rule of the
precedent with the same line shape (here R104's build() call, with R111's DEAD-clause step), flagged (G-U). C116 G-2: name clashes
settled by one body sentence (G-6). C117 E-1 / E-2: no sentence wider than signed (G-2 (ii), (iii)). C118 E-1: no stale status sentence.
C118 §3 / Erratum E-2: EVERY DEFINITION of L-3 diffed against the packet and R104 (G-2). C120 §5 / C121 §5 / C122 E-2 / C124 E-1 / C125
E-1 / C127 E-1 / C128 E-1..E-5 / C129 E-1: EVERY clause of L-3 tested against reachcheck.py's counter code, for unit, set and the
statement's scope, and every signed clause matched to a count or a no-DATA entry (notes/CHECKER.md l. 8, successor 19: «Method kept: for each
signed clause of the line, find its counter or its no-DATA entry»): G-9, three clauses flagged with exact replacements. C129 E-2: a DEAD
instance must be reproducible from the line (G-D, flagged). C122 G-0: parentheses balanced (G-1). C122 E-3: the source note names every
proof-carrying file (G-1). C123 E-1: no lane label and no packet name in the title before the claims (G-1). C123 E-2 / C118 E-1: no
stale referee or landing state (G-13). C119 E-1: every «referee X did Y» is checked against that referee's file.
to check: FLAGS FIRST (G-0 to G-14; the ones for the Lead or CHECKER: G-9 (i)-(iii) (DATA, with exact replacements R-A, R-B, R-C), G-D (the
DEAD instances in the line, R-D), G-0 (number), G-U (UPDATE procedure), G-P (placement with R115 / R116 pending)), then the CLEAN items
and (0)-(14).
- G-9, DATA (FLAG; the C120 §5 / C124 E-1 / C125 E-1 / C127 E-1 / C128 / C129 E-1 check item: unit, set and the statement's scope of
  every count, against reachcheck.py's counter code, read by me in full at 727163f0, and every signed clause matched to a count or a
  no-DATA entry). Every figure in L-3's DATA equals reachcheck.out, xcheck.out and my re-runs: «on 14 corpus genomes (L(G) 9 to 59)» =
  the 14 «C14 …» rows (L sorted 9, 11, 13, 13, 15, 17, 24, 25, 31, 33, 35, 44, 48, 59); «440 random acyclic genomes» = gen(Random(seed)),
  seed 1-440 (l. 143-144; acyclic() asserted, l. 138, 144); 908, 454, 42,880, 693,030 = the «C14+R440 …» lines. Clause by clause
  (reachcheck.py line numbers):
  - (i) FLAG, NO-REACH (a), (b): «0 standard states in 908 states of the S3 runs on Γ(G),». The counter named is NR-STD (l. 89): a state
    counts when σ equals the stated start of Γ(G) at EVERY non-mover Even vertex (v ≥ N) and τ equals it at every Odd vertex. The packet's
    «standard state» is wider: «no state (σ_j, τ_j) is a standard state of R104 (one with σ(K0) = K3, σ(K1) = K1)» (§2 (b), l. 97). So
    NR-STD's 0 counts R104's REALIZE states (every REALIZE state agrees with the stated start off the movers: R104's «τ unchanged», «σ
    unchanged off the movers»), the line's «i.e.» half, but not the predicate σ(K0) = K3, σ(K1) = K1, and not clause (a), «σ_j(K0) = K1
    and σ_j(K1) = K0 at every state j». Clause (a) HAS a lane counter, NR-CORE (l. 90, «core-not-(K0->K1,K1->K0) 0» on the same 908
    states), which the line does not cite; (b)'s σ(K0) = K3 predicate then follows from (a) by arithmetic (K1 ≠ K3). My split: states
    with σ(K0) = K3 and σ(K1) = K1: 0 of 908; NR-CORE 0; NR-STD 0. So the count is numerically right under either reading, but the line
    names a predicate the counter does not test and leaves the signed clause (a) without a count. Unit / predicate mismatch plus a
    signed clause with no count in the line (the C127 E-1 / C129 E-1 classes). Neither referee raised it (REFEREE l. 123 «L-1's DATA
    parenthesis covers NO-REACH (a)-(b)»; REFEREE-2 l. 83 «NR-STD, NR-CORE, NR-LAM per state ✓»). Proposed R-A (the old string occurs
    once in L-3 and once in the UPDATE, by script; not mine to choose): "0 standard states in 908 states of the S3 runs on Γ(G)," →
    "σ(K0) = K1 and σ(K1) = K0 at all 908 states of the S3 runs on Γ(G) and 0 of them equal to R104's stated start off the movers,".
  - (ii) FLAG, NO-REACH (c): «(S3 picks them, and K0, K1 never have an improving edge while they hold)». «S3 picks them» is state 0 of
    NR-CORE. «K0, K1 never have an improving edge» has NO counter in reachcheck.py, and L-3's no-DATA entry is «Corollary REAL-IDEAL-S3
    no separate DATA» only; the packet's no-DATA list has it (§10 l. 313 «§2 (c) (it is a step of (a)'s proof; its effect is counted by
    «core-not-…»)»), the line does not. It does not follow by arithmetic from NR-CORE (a vertex with an improving edge can keep its
    choice under S4a; S4c fires only when σ and τ both stay). The C127 E-1 / C128 E-5 class (a signed clause with no counter, not in the
    line's no-DATA list). True on data: my split computes Iσ at all 908 states (si.py Engine.improving, as n5x.step does): 0 edges out of
    K0 or K1 (my DATA, not lane DATA); REFEREE-2's own replay checked (a) and (c) on the 14 corpus genomes (l. 73 «σ(K0) = K1, σ(K1) =
    K0 at every state; no improving edge out of K0, K1; 1 iteration ✓.»; referee data, not lane DATA). Proposed R-B (old string once in L-3 and in the UPDATE; not mine to choose): "Corollary
    REAL-IDEAL-S3 no separate DATA," → "NO-REACH's no-improving-edge clause and Corollary REAL-IDEAL-S3 no separate DATA,".
  - (iii) FLAG (set, the C128 E-3 class): «n5b (SPEC mode) iteration counts equal on 28/28 games and Oink 8fbf0a7 --zlk with verify OK on
    28/28». The 28 games are Γ3(G) («_g3») and Γ(G) («_g0») of the 14 corpus genomes (xcheck.sh l. 5-9; packet §10 l. 306-309), not
    games of the 440 random genomes; the line names neither the 28 nor what the counts equal. My check (xcmp117.py): n5b's (iterations,
    fallbacks) = the lane engine's on 28/28 (Γ3: the «C14» rows' S3-iterations, = L + 3, and 1 fallback; Γ: 1 and 0, NR-IT and my split);
    «zielonka(oink zlk) OK strategies verified» 28/28; my own run of xcheck.sh with Oink 8fbf0a7 is byte-equal to xcheck.out. xcheck.sh
    is not in check.sh (it needs Oink) and xcheck.out is not in reach.pins. Proposed R-C (old string once in L-3 and in the UPDATE; not
    mine to choose): "n5b (SPEC mode) iteration counts equal on 28/28 games and Oink 8fbf0a7 --zlk with verify OK on 28/28" → "n5b (SPEC
    mode) iteration counts equal on the 28 games Γ(G) and Γ3(G) of the 14 corpus genomes and Oink 8fbf0a7 --zlk with verify OK on the
    same 28". CHECKER: E-item or note.
  - «every such run 1 iteration»: NR-IT (l. 87), per run, the 454 runs on Γ(G): «iterations histogram {1: 454}». MATCH (DATA without a
    statement; packet l. 120 «Not claimed: anything about τ_j beyond what SPEC does; the iteration count (DATA §10: 1 iteration on every
    genome tried).»).
  - «0 failures of REACH3 in 454 genomes»: R3-FAIL (l. 113-124), per genome: len(states) ≥ L + 2 (so «at least L(G) + 1 iterations»),
    states 0..L equal to the standard state of Γ3 for s_j (standard(), l. 67-73: movers at s_j's pads), transitions 1..L FL (no fallback,
    τ kept, σ changed, the (σ, τ)-play valuation equal at every vertex, playval l. 64-66), transition L + 1 a fallback. MATCH (unit, set,
    scope). Set note: R440 has L ∈ {0, 1, 2} (94, 298, 48 genomes; my split), so «no FL run if L(G) = 0» is exercised 94 times and every
    longer run is in C14; the packet says it (l. 301 «R440 alone has L ≤ 3: a weak test of REACH3.»).
  - «the β-free P-sets of NO-REACH 0 on 42,880 (state, vertex) pairs»: NR-BETA over NR-PAIRS (l. 92-95): every (state, v ∉ {K2, K3,
    c_X}), the line's own scope «at a vertex outside K2, K3 and the unused even self-loop of priority 2»; the predicate (a β in P, or a
    cycle node ranked at or below some β) is §2 (d), stronger than the line's clause. MATCH (both referees; 42,880 = Σ (n − 3) over the
    908 states, my split).
  - «S3-START 0 on 454 genomes»: S3-START (l. 101), per genome, n5x.start_pair against gamma3.build's start with the pads. MATCH.
  - «PAD 0 on 693,030 (state, vertex, world) triples of the S3 runs on Γ3 (every vertex but the unused even self-loop of priority 2)»:
    PAD over PAD-PAIRS (l. 106-112), «if v == cX: continue», both worlds (Ξσ, Ξτ), every state of the run. MATCH after L-3's R1. Note:
    the line's clause «no pad is ever a cycle node or in a P-set (Lemma PAD)» has no c_X exception (§5 (b) has one, G-2 (ii)); at c_X my
    split finds 0 pads as cycle node or in P on the 5,174 excluded triples (698,204 with them), as REFEREE-2 Add. 1 l. 136-138.
  - «both DEAD SUBDIV instances re-run»: the two «SUBDIV-DEAD instance» lines (l. 159-169). MATCH (A: fallbacks 1 vs 0; B: iterations
    2 vs 3).
  - «Corollary REAL-IDEAL-S3 no separate DATA»: true (no counter; packet l. 315 «§8 (a), (b) (reduction, no data)»).
  - NOTE, Γ3's size «4M + 4 single-successor Even pads of priority ≤ 2», «n = N + 7M + 10»: a definition and a count, in the packet's
    no-DATA list («§3 size (count)», l. 314), not in the line's; the C124 G-9 (vii) ruling (a definition need not be named) applies. The
    14 «C14» rows print n = N + 7M + 10 (xcmp117.py, 14/14); my split 454/454.
  - NOTE, the «so it never visits a state with σ(K0) = K3, σ(K1) = K1» half follows from (a) (R-A covers it); «i.e. none of R104's
    REALIZE states» is NR-STD.
  - SCOPE (NOTE): NO-REACH (a)-(c) is stated «for EVERY genome G»; its DATA is on acyclic genomes only (C14 + R440, acyclic() asserted),
    as the DATA head says (the C122 W-ONLY / C127 / C128 N-3 / C129 N-2 precedent).
- G-D, THE DEAD INSTANCES (FLAG; the C129 E-2 class). L-3 names the killed statement exactly (W-1, RC-2 in «(a, b) order»; subdiv.pad
  l. 15-22 builds G^pad exactly so: priorities + 4, pads n + i over E = sorted((a, b)), Ω 2 / 1 / 0 as stated) but gives its instances
  only as «n = 3 and n = 5 games with given start pairs»; the games and start pairs are in packet §9 (l. 275-279) and in reachcheck.py
  (l. 161-163), not in the line. C129 l. 47-48: «A dead end must give the instance that killed it (CLAUDE.md), so a reader must be able
  to reproduce it from the line.» Proposed R-D (old string once in L-3 and in the UPDATE; not mine to choose): "n = 3 and n = 5 games with
  given start pairs" → "the n = 3 and n = 5 games with the start pairs of packet §9 (instances A, B)" (the packet is frozen and named in
  the source note); an alternative is the instances' data verbatim from §9 l. 275, 278-279. No Dead-ends row is drafted: SUBDIV is a lane
  statement killed inside a landed line (the C118 §5 / C129 precedent); the obstruction is a READING (§9 l. 280 «Obstruction (READING,
  from the traces; not to sign)») and is not landed. L43 does not bear (not an asymptotic statement; killed by instances, replayed by
  both referees with their own builders).
  L-3 with R-A, R-B, R-C and R-D (my script, upd117.py): sha1 f85a024b8c8caa4c996fcd15bf1e78fbd436b534 with its newline, 3,942 bytes, 64
  «(» / 64 «)», depth never negative, 0 "|"; its UPDATE (same procedure) sha1 b4d74e094a30cba61017eeda4a0c33cb7a1db6f3 = this draft's
  UPDATE with the same four replacements (True).
- G-2, DEFINITIONS DIFFED (my own diff; the C118 §3 / Erratum E-2 lesson). Premise parenthesis = packet §1 (G-4). NO-REACH = §2 (a)-(d)
  l. 95-101 (the line's (d) omits «the cycle node of Ξσ_j(v) ranks above every β-vertex», a narrower statement); Γ3 = §3 l. 123-131;
  S3-START = §4 l. 139; PAD = §5 l. 146-150; REACH3 = §7 l. 243-246; REAL-IDEAL-S3 = §8 l. 261-266; the killed statement = §9 l. 271-273
  with the pad order of l. 272; «the unused even self-loop of priority 2» = R104's own words (title l. 9864 «an unused even self-loop of
  priority 2»), the c_X of packet §2-§5 (fixes l. 29-30, W-2).
  (i) NOTE. L-3's Γ3 says «appended after Γ(G)'s vertices» but not the order of the pads among themselves (§3 l. 124-125 «appended after
    Γ's vertices in the order pA, s, q, r, pe (gate-index order), pβ (gate-index order), pb (option order), m (gate-index order)»). The
    proofs do not use it (my reading): S3-START compares distinct priorities at every vertex with two or more successors (§4); KEY3 (b)
    l. 239-240 «(In Γ the block is e, g, x; the pad indices never decide because pe_i, m_i are determined by g_i.)». Both referees
    re-derived the INDEX spot; REFEREE-2's builder equals the pinned Γ3 games byte for byte. Note.
  (ii) NOTE (C117 E-1 class, harmless). L-3's PAD clause «no pad is ever a cycle node or in a P-set» has no exception; §5 (b) is stated for
    «every vertex v ≠ c_X». At c_X (a self-loop of priority 2, no other edge) every play is the loop: cycle node c_X, P = ∅, so the clause
    holds there too. REFEREE-2 Add. 1 l. 136-138 says so («The line's PAD clause («no pad is ever a cycle node or in a P-set») has no
    exception and is true at c_X too»). Note.
  (iii) NOTE. Corollary (b) in L-3, «would give games on which N5 from its default start makes super-polynomially many iterations», omits
    §8 (b)'s «(n_i = N_i + 7M_i + 10 vertices, polynomial input size, §3)»; n_i is linear in N_i + M_i, so super-polynomial in N + M and
    in n coincide. The line states (a) with «L(G) ≤ p(N + 7M + 10)», weaker than §8 (a)'s «L(G) + 1 ≤ p(N + 7M + 10)» for the iteration
    bound. Note.
- G-0, THE CHECKER NUMBER. docs/checker/ on claude/checker ends at C129.md (C128 = R115, Add. 1 PASS 2603f321, landed; C129 = R116,
  Add. 1 pending);
  docs/checker/C130.md does not exist; «C130» occurs 0 times in RESULTS, GAPS, NOW, LEAD-STATE and on the claude/checker branch (git grep).
  This draft uses C130 (title fill, UPDATE head, GAPS preamble).
- G-U, THE UPDATE PROCEDURE (FLAG). L-3 has R104's shape: the labels (Theorem NO-REACH), (Theorem REACH3), (Corollary REAL-IDEAL-S3)
  stand BEFORE their clauses, (Lemma S3-START) and (Lemma PAD) already follow their sub-clauses inside REACH3's clause, and the DATA sits
  inside the scope parenthesis («; DATA: …»), not in a separate «(DATA, …)» parenthesis. So upd117.py runs build() of upd100L3.py
  unchanged with R104's call form (the three leading labels, start «and RESULTS R15 (d) for termination only: », the date «2026-11-07»),
  plus R111's DEAD-clause step (as R111 and R116): the unlabelled clause «; the statement that, for every game and start pair, … (DEAD
  SUBDIV: …)» is cut before the build and put back behind «(Corollary REAL-IDEAL-S3)». Without the step build() runs but files the DEAD
  clause under the Corollary (default build ≠ result, True). Cross-check: a direct build by string operations is equal (True). Head
  «UPDATE <DATE> <HH:MM>Z: RESULTS R117 (P-N5-REACH; CHECKER C130 <checker>) [refereed-only] ».
- G-P, PLACEMENT (FLAG; landing order). R115 is landed on the local trunk (5ec57d84); R116 (C129 Add. 1 pending, second fill) is not.
  R117 goes after the last landed R-entry, before «**Erratum E-1**», and its UPDATE after the last UPDATE on GAPS l. 11. Two simulations
  (Addendum (5)): (A) after R115, R116 not landed (the local trunk as it is); (B) after R116 (R116-draft.md as it stands, a stand-in for
  its final fill). At landing the UPDATE builder is re-run: upd117.py already carries the R115 control (True); if R116 lands first, an
  R116 control must be added the same way (the R116 call of its second-fill builder, filled with the landed stamp).
- G-4, PREMISE ROUTE (the C115 E-1 class): CLEAN (prem117.py on RESULTS 0ea36025 and the SPEC file 66fde9ef; the same hits on 555d41bd). Packet §1 (l. 23-79) has
  38 outermost «…» quotes; every one, and every piece of the four with an elision, is found (0 not found). RESULTS hits, whitespace
  normalised: [DEF]'s three R104 quotes 1 hit each (R104's title l. 9864); «one FL run (…)» 1 (l. 9864); [1E-N3] 2 (R104's title l. 9864
  and body l. 9975-9978, both R104); R57 (b)'s two pieces 11 and 4 (R57 l. 2915-2916, the source, and R85-R88, R102-R104 quoting it);
  [RULE] 2 (R104 title and body l. 9990-9992); «σ_j(x) is the κ_j-least element of» 1 (R104 body l. 10004); [VJ-LOC] 2 (R104 title,
  body l. 10011-10012); R36 (c)'s three quotes 2 each (R36 l. 1723-1724, 1730-1731, the source, and R104's body quoting it); [TERM] 2 / 1 /
  1 (R15 l. 640-642, the source; R80 l. 4428 quotes the first). SPEC: S2, S3, FIX 1, S4a, S4b, S4c and S1 quotes 1 hit each in
  N5-ssi-global.md at the cited lines (47, 48-49, 81-83, 51-57, 45-46); two short ones («to τ(v).», «Else σ_new = σ.») also occur in R89 /
  R73. Both referees: REFEREE l. 28-33, REFEREE-2 l. 25-31 (38 quotes, 34 verbatim, 4 with an elision, each piece verbatim). L-3's
  premise parenthesis («premise: R104's definitions of the IDEAL model, L(G), the Ξ-graph, the game Γ(G) with its vertex indices and
  start, and the FL run; no theorem of R104 used», then R104's premises as landed and R15 (d)) = packet [DEF], [1E-N3], [RULE], [VJ-LOC],
  [TERM]; the SPEC is the line's «N5 (SPEC S1-S5) from its DEFAULT start S3 (SPEC S3 with FIX 1)». No R104 THEOREM is used: packet l. 43
  «No THEOREM of R104 is used.»; the §6 lemmas transfer P-N5-REALIZE §3 and are proved in the packet (l. 78-79 «every step of §6 is
  proved here.»); REFEREE l. 32-33 «All cited results are landed: R104, R57 (b), R24, R103, R36 (c), R15 (d). No theorem of R104 is
  used: I checked every proof step against [DEF] only.»
- G-10, LEAD READINGS AND RULINGS. L-3 cites no Lead reading by label (by script: «Lead reading» 0, «L4» 0); through «R104's premises as
  landed» it carries R104's L45 (S4b covered) and L46 (R24 class-free) readings, both active (DECISIONS-INDEX l. 38-39). L50 (l. 45,
  active): «T^R growth / tower question open» agrees with L-3's «nothing is claimed about whether long IDEAL-ACYC runs exist». The two
  Lead rulings of this round are recorded, not as readings (they are not in DECISIONS): fixes entry 2 l. 54-61 and LEAD-STATE l. 2438
  «Lead ruling: W-3 wording for PAD (resolves RC-1), RC-2 in «(a, b) order» per §9 l. 272 (Option B) -> L-3 at L-NEW.». Body: Fixes.
- G-C, OVERLAP WITH LANDED R104 (NOTE). REACH3 is R104's REALIZE run reached from S3 on a padded game; R104's line already says «nothing
  about N5's default start S3»; R117 is the S3 statement, on Γ3(G) not Γ(G), with its own transfer of R104's packet lemmas (proved in the
  packet, not cited). REAL-IDEAL-S3 strengthens R104's REAL-IDEAL from «from every start pair» to S3 with n = N + 7M + 10 instead of 3(N
  + M) + 6. Nothing landed is claimed again.
- G-3, SYMBOL TEST (notes). s, j, L, n, p, M, N, G, g, x, k bound in their clauses; K0-K3, u, β_g, «the unused even self-loop of priority
  2» are R104's Γ(G) objects (R104 title); pA, s, q, r, pe_g, pβ_g, pb_g, m_(x,k) are defined in the line; «Ξσ_j», «P-set», «cycle node»,
  «fallback», «FL» are SPEC / R104 words; «s» names both a pad and (in §3) a mover state in the packet, in the line only the pad. «IDEAL-ACYC»
  is used in the line («long IDEAL-ACYC runs») without definition: R104's IDEAL model on ACYCLIC Ξ-graphs (69 RESULTS occurrences).
- G-5, ERRATA (note). E-1 concerns R97-R100 counts, E-2 R105's binders, Note E-3 R110's CONDITIONAL DEAD; none bears on R104's
  definitions or premises used here.
- G-6, NAMES (by script on RESULTS 0ea36025 / GAPS 19da0f51; the same on 555d41bd / 3c4ff44d). 0 times in RESULTS and GAPS: «R117», «C130», «P-N5-REACH», «NO-REACH»,
  «REACH3», «S3-START», «Lemma PAD», «REAL-IDEAL-S3», «SUBDIV», «Γ3», «reachcheck», «box189», «FL-S3-POLY». «REAL-IDEAL» is R104's
  Corollary (a different statement; the new one carries «-S3»). One body sentence (Honest limits (vii)).
- G-7, L41 and L43 (my reading): REFEREE's RE-L1 and RC-2 and REFEREE-2's W-1, W-2, W-3 are wording of the line, applied verbatim (RC-2
  in the Lead's «(a, b) order» form); no referee-written text is a proof step. L43: SUBDIV is not asymptotic; DEAD by instances, replayed.
- G-8, THE SCOPE TAIL (note). «a REDUCTION / NECESSITY statement only (no count is bounded; nothing is claimed about whether long
  IDEAL-ACYC runs exist; Ξ-cyclic genomes are not covered; the converse is not claimed; …; G-N5-TIME stays OPEN; not M3, not a step-4
  pass, not a TARGET.md claim)»: true. No CONDITIONAL; no tower or CANDIDATE claim (packet §11's context is not in the line).
- G-11, STALE LANE TEXT (notes). Fixes entry 2 l. 50-51 «(SHAs as relayed by the Lead; not yet on origin when this entry was written)»:
  cc9f4afd and c420666d are on origin now. Packet §12 l. 327-329 describes the «P-N5-REACH» block's pins as of the freeze; at 727163f0
  the block pins reach.pins 11ebdbee (with L-2, L-3, the fixes).
- G-12, PINS (the C110 F-1 / C116 G-3 class): reach.pins (pinned by the check.sh block) covers the packet, L-1, L-2, L-3, the fixes, the
  tools, reachcheck.out and the corpus; xcheck.sh and xcheck.out are not pinned (xcheck needs Oink). Note.
- G-13, THE REFEREES' ROUNDS (state on file at this fill): see (3), (4).
- G-14, THE FIXES FILE (note). Two entries, each «This entry carries no proof.» (l. 8, l. 53); each lists exact old / new strings, each old
  string once (my script: L-1 + entry 1 = L-2, L-2 + entry 2 = L-3, True, True). Entry 1's notes N-1..N-4, D-1 change nothing in the line.
- CLEAN AT L-3 (the pre-check against CHECKER's recurring items, by script on adfbb3b8):
  C106 E-1 (old line as current): L-3 is the current line; no L-4 exists on l-new 727163f0; L-1 and L-2 appear only in the line history.
  C113 E-1: no insertion; the title is byte-equal to prefix + L-3 + fill (Addendum (2)).
  C113 E-2: no trunk statement in the body.
  C114 Add. 1 E-1: <DATE> placeholder.
  C115 E-1: G-4.
  C116 G-2: G-6.
  C118 E-1: no stale status sentence (Addendum (4)).
  C122 G-0: 59 «(» / 59 «)», depth never negative (G-1).
  C122 E-3: source note CLEAN (G-1).
  C123 E-1: no lane label and no packet name before the claims (G-1).
  C120-C129 DATA: G-9 (three flags), G-D.
  «|»: 0 in L-3, 0 in the entry block, 0 in the UPDATE (Addendum (3)).
- G-1, TITLE SHAPE AND SOURCE NOTE: CLEAN (my script). L-3 is one line, 3,704 characters, 3,748 bytes with the newline, 710 whitespace
  tokens, 59 «(» / 59 «)», depth never negative, final depth 0; 0 "|"; 0 guillemets; one « — » with its own date «(2026-11-07)»,
  «2026» once; no «c_X». It begins «N5 (SPEC S1-S5) from its DEFAULT start S3»: no packet name and no lane label before the claims (C123
  E-1: met; R104's line begins the same way); «L-COMP», «L-NEW» do not occur in the claims; «L-NEW successor 58» and the packet name
  occur only in the source note. Source note «(P-N5-REACH, docs/new/P-N5-REACH.md; L-NEW successor 58)»: the packet carries every proof
  (l. 5-6 «This packet carries every proof in full and is checked against this text only.»); fixes entries 1 and 2 carry none (l. 8, l.
  53 «This entry carries no proof.»). So every proof-carrying file is named (C122 E-3: met).
(0) PLACEMENT. docs/RESULTS.md at the local trunk: sha1 0ea360253a0e102ecf5750e187233ab750d0af04, 13,681 lines (wc -l), last changed by
  5ec57d84 (R115's landing); «### R115» l. 12697 (entry l. 12697-13070, l. 13071 blank); «**Erratum E-1**» l. 13072; «**Erratum E-2**»
  l. 13085; «**Note E-3**» l. 13113; «## Dead ends (kept;» l. 13144. "### R117" occurs 0 times in RESULTS and GAPS. PROPOSED (R102's to
  R115's layout): insert R117's entry, with one blank line after it, directly before «**Erratum E-1**», i.e. after the blank line that
  follows the last landed R-entry: after R115's block if R116 is not yet landed (A), after R116's block if it is (B). Simulations: Addendum
  (5). GAPS has sha1 19da0f5180dff9e1f90b72222b6118091adb50d4, 23 lines.
(1) TITLE. The title is the line file docs/new/P-N5-REACH-line-L3.txt (l-new 727163f0, 2026-11-07T04:26:17Z, the file's only commit,
  sha1 adfbb3b8219026b23a80b2081a3c227c35730451, 3,748 bytes with the newline; byte-equal at the l-new head), verbatim: NOTHING is
  stripped and NOTHING is inserted: "### R117 [refereed-only] ", then the file without its newline, then ", CHECKER PASS
  (docs/checker/C130.md, checker PENDING)" (as R90-R116). Built by script (fill117.py) and re-checked after writing (chk117.py): equal.
(2) LINE HISTORY: three lines. L-1 b12ec57a (73b3d1fd, frozen with the packet; 3,105 bytes, 593 tokens, 52 «(» / 52 «)»; one «c_X», one
  guillemet pair): REFEREE NOT YET (RE-L1); REFEREE-2 «MATCHES after W-1, W-2». L-2 4de27b32 (571c75c5; 3,628 bytes, 689 tokens, 57 / 57):
  fixes entry 1, L-1 with exactly RE-L1, W-1, W-2 (my byte test: each old string once, L-1 + the three = L-2, True); token diff 5 hunks
  (11 tokens out, 107 in), all inside the three. L-3 adfbb3b8 (727163f0; 3,748 bytes, 710 tokens, 59 / 59): fixes entry 2, L-2 with
  exactly R1 (W-3, resolves RC-1) and R2 (RC-2 in «(a, b) order», Lead ruling) (my byte test: True); token diff 2 hunks (2 out, 23 in).
  REFEREE's predicted L-3 (RC-1 and RC-2 in its own words, «edge order») has sha1 13d0ce80…, as §C l. 181 says, and is NOT L-3; L-2 with
  REFEREE-2's W-3 alone has sha1 46c2e507…, as Addendum 1 l. 142 says; L-3 = that line with RC-2 in the «(a, b) order» form (True).
(3) THE LINE AT BOTH REFEREES. REFEREE successor 25, docs/referee/R-P-N5-REACH.md: report f66942c1 (2026-11-07T03:04:24Z, new file, 146
  lines, sha1 a010881ca2cf8eb2f6c381a1dc2d362f6d800b58): L-1 NOT YET (RE-L1); §C cc9f4afd (2026-11-07T03:58:16Z, 187 lines, sha1
  2399683e9f4659d91c9f1c80585340b55ddbdbb6): L-2 MATCHES the byte test, in meaning NOT YET (RC-1, RC-2); §C add. 1 85cc9ebb: (2026-11-07T04:50:03Z, 209 lines, sha1 f5e46e3fbcf925431a7c2e3da0642571b193165b; l. 1-187 = cc9f4afd's, by diff): «Verdict: fixes entry 2 is CORRECT. L-3 MATCHES, by the byte test and in meaning. All statements stay SIGNED.» (l. 209).
  REFEREE-2, docs/referee-2/R2-P-N5-REACH.md: successor 29's report b0860fcd (2026-11-07T03:06:42Z, new file, 114 lines, sha1
  037916d542bed7e2a9831d548952ed6756f7f2d8): L-1 «MATCHES after W-1, W-2»; successor 30's Addendum 1 c420666d (2026-11-07T03:59:26Z, 147
  lines, sha1 6e406426763a2ca7ff9c69544d1af1f44d7c4e74): «L-2 MATCHES after W-3»; Addendum 2 ddf42cb6: (2026-11-07T04:50:08Z, 173 lines, sha1 d74b19a77e22e4dbf266ac00b9432649f034ea63; l. 1-147 = c420666d's, by diff; tools bt_l3.py, bt_l3.out): «Verdict: entry 2 **CORRECT**; **L-3 MATCHES** the packet with fixes entries 1-2, in bytes and in meaning (Opus 5.5, D1).» (l. 172).
(4) CLAIMS SIGNED = every row of both verdict tables (REFEREE "## 0. Verdicts" l. 5-17; REFEREE-2 "## Verdicts" l. 10-22), each SIGN,
  no gap, unchanged in every later round. Not signed: §10-§13 (table l. 21 «DATA / CONJECTURE / READING (not to sign)»).
(5) OTHER TEXTS THE ENTRY DEPENDS ON: RESULTS R104's definitions (title l. 9864) and its three landed premises (body l. 9975-10012), R57
  (b), R24 (a), (b), R103's bridge B and (R1) ruling, R36 (c), R15 (d) (through R104's premise text and [TERM]); the SPEC file (66fde9ef).
  Nothing else for a signed statement. docs/new/N5-REACH-box189.md (f55dac37) is history (packet l. 5); P-N5-REALIZE is the source of the
  §6 proof pattern, not a premise (l. 78-79).
(6) PREMISE LABELS (by script on L-3): «R104» 6, «R57» 1, «R24» 2, «R103» 1, «R36» 1, «R15» 1; each exists (titles l. 9864, 2893,
  1064, 9641, 1717, 624). No other RESULTS label. G-N5-TIME open (GAPS l. 11).
(7) SYMBOL TEST: G-3.
(8) FIXES AND STATUS NOTES: G-14; body Fixes.
(9) GAPS: G-N5-TIME (GAPS l. 11) stays open; L-3 states no CONJECTURE as claimed and kills one lane statement (SUBDIV), which is not in
  GAPS («SUBDIV», «P-N5-REACH» 0 times in GAPS). A line-11 UPDATE is proposed at the end, BUILT FROM L-3 (upd117.py: upd115b.py l. 3-337
  = upd115.py l. 1-335 unchanged, exec'd: R97's to R114's LANDED UPDATEs rebuilt from their lines byte for byte, True ×18; then the
  R115 control, upd115b.py's R115 section unchanged, exec'd, filled with the landed stamp 2026-11-07, 05:07, 2603f321: equal to GAPS l. 11,
  True (19 controls, all landed); then R117 (G-U)). Checked by script: one line, 0 "|", one each of
  «<DATE>», «<HH:MM>», «<checker>», 3,779 bytes, 3,738 characters, 709 tokens, 58 «(» / 58 «)», balanced, «2026-11-07» 0 times; token
  multiset diff against L-3 = the head, the three moved labels, « — », the opened scope parenthesis, the two dropped scope sentences and
  the final sentence (upd117.out).
(10) DATA of record = packet §10 (l. 286-315), NOT signed; L-3's DATA states its counts, with the flags of G-9. Re-runs (a)-(d) in the
  header: PASS; reachcheck.py re-run byte-equal (inside block (a)); xcheck.sh byte-equal; my split g9split117.out.
(11) Discrepancies, recorded for CHECKER, no verdict affected: D-1 REFEREE-2's report header «Written 2026-11-07 03:0xZ to 03:3xZ» (l.
  2) against its commit b0860fcd (03:06:42Z); REFEREE's f66942c1 is 03:04:24Z; each states it did not read the other's file before its
  push. D-2 fixes entry 2 «(2026-11-07 from 04:2xZ …)» with its sources «not yet on origin» (l. 50-51); both were on origin at 03:58Z /
  03:59Z. D-3 packet §12 l. 327-328 «(~15 s)», REFEREE l. 106 «(11.5 s)», REFEREE-2 l. 79 «17.6 s» for both blocks, mine 17 s for both:
  consistent. D-4 xcheck.sh l. 2 «~10 min»; my run took 8 s. D-5 packet §10 l. 301 «L ≤ 3» for R440: measured max 2.
(12) Excluded: packet §10 (DATA counts as statements), §11 (CONJECTURES BLIND and SUBDIV-APPROX; the tower context), §12, §13's
  READINGs, the SUBDIV obstruction (§9 l. 280-284, READING), W3's DATA, entry 1's notes N-1..N-4 (K3 «every genome» is not used by the
  line). Not part of this entry.
(13) Commits: lane (claude/l-new): f55dac37 (box 189, history), 73b3d1fd (2026-11-07T02:35:31Z; freeze: packet, L-1, reachcheck.py,
  reachcheck.out, gamma3.py, subdiv.py, reach.pins, xcheck.sh / xcheck.out, check.sh block «P-N5-REACH») → 571c75c5 (03:32:05Z; fixes
  entry 1, L-2, pins) → 727163f0 (04:26:17Z; fixes entry 2, L-3, pins). REFEREE: f66942c1 → cc9f4afd → 85cc9ebb. REFEREE-2: b0860fcd →
  c420666d → ddf42cb6. CHECKER: docs/checker/ ends at C129.
(14) Placement: see (0) and G-P. DEAD-ENDS ROWS: NONE (G-D). R117 kills one lane statement (SUBDIV), inside the line.

### R117 [refereed-only] N5 (SPEC S1-S5) from its DEFAULT start S3 (SPEC S3 with FIX 1), on the games of RESULTS R104 (premise: R104's definitions of the IDEAL model, L(G), the Ξ-graph, the game Γ(G) with its vertex indices and start, and the FL run; no theorem of R104 used), with R104's premises as landed (1E-N3 = RESULTS R57 (b) in its two forms; RESULTS R24 (a) Lemma R and R24 (b)'s choice rule with RESULTS R103's bridge B and (R1) ruling; RESULTS R36 (c) Lemma P1 on the dual game) and RESULTS R15 (d) for termination only: (Theorem NO-REACH) for EVERY genome G the N5 run of Γ(G) from S3 has σ_j(K0) = K1 and σ_j(K1) = K0 at every state j (S3 picks them, and K0, K1 never have an improving edge while they hold), so it never visits a state with σ(K0) = K3, σ(K1) = K1, i.e. none of R104's REALIZE states, and, for acyclic G, no β-vertex is ever in the P-set of Ξσ_j at a vertex outside K2, K3 and the unused even self-loop of priority 2; (Theorem REACH3) for every G with an ACYCLIC Ξ-graph, the game Γ3(G) obtained from Γ(G) by 4M + 4 single-successor Even pads of priority ≤ 2 (pA on K0 → K3, s on K1's loop, q on K1 → K0, r on K2 → K1, pe_g and pβ_g on both faces of every gate g, pb_g on every β_g → u, and m_(x,k) on every mover edge x → (x, k) with priority 2 for the genome start and 0 otherwise, appended after Γ(G)'s vertices; n = N + 7M + 10) has S3's start pair equal to R104's stated start transported through the pads (Lemma S3-START), no pad is ever a cycle node or in a P-set (Lemma PAD), and the N5 run of Γ3(G) FROM S3 has states 0, …, L(G) equal to the transported REALIZE states of the IDEAL run, transitions 1, …, L(G) are FL transitions and transition L(G) + 1 is a fallback, so if L(G) ≥ 1, [0, L(G)] is one FL run of length exactly L(G) and the run makes at least L(G) + 1 iterations (no FL run if L(G) = 0); hence (Corollary REAL-IDEAL-S3) if every FL run of N5 from S3 on every n-vertex game has length at most p(n) for a nondecreasing polynomial p (in particular if N5 from S3 makes at most p(n) iterations), then L(G) ≤ p(N + 7M + 10) for every acyclic G, and a family of acyclic genomes with L super-polynomial in N + M would give games on which N5 from its default start makes super-polynomially many iterations; the statement that, for every game and start pair, the game with every priority + 4 and every edge subdivided by an Even pad of priority 2 (Even, start edge), 1 (Odd, start edge) or 0, the pads indexed after the game's vertices in (a, b) order, has an N5 run from S3 equal state for state and transition for transition (fallbacks included) to the run of the game from that start pair is DEAD as stated (DEAD SUBDIV: the n = 3 and n = 5 games with the start pairs of packet §9 (instances A, B) whose padded N5 runs from S3 differ in a fallback flag, resp. in the iteration count, 2 vs 3) (2026-11-07) — a REDUCTION / NECESSITY statement only (no count is bounded; nothing is claimed about whether long IDEAL-ACYC runs exist; Ξ-cyclic genomes are not covered; the converse is not claimed; DATA: on 14 corpus genomes (L(G) 9 to 59) and 440 random acyclic genomes, σ(K0) = K1 and σ(K1) = K0 at all 908 states of the S3 runs on Γ(G) and 0 of them equal to R104's stated start off the movers, every such run 1 iteration, 0 failures of REACH3 in 454 genomes, the β-free P-sets of NO-REACH 0 on 42,880 (state, vertex) pairs, S3-START 0 on 454 genomes, PAD 0 on 693,030 (state, vertex, world) triples of the S3 runs on Γ3 (every vertex but the unused even self-loop of priority 2), both DEAD SUBDIV instances re-run, NO-REACH's no-improving-edge clause and Corollary REAL-IDEAL-S3 no separate DATA, n5b (SPEC mode) iteration counts equal on the 28 games Γ(G) and Γ3(G) of the 14 corpus genomes and Oink 8fbf0a7 --zlk with verify OK on the same 28; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim) (P-N5-REACH, docs/new/P-N5-REACH.md; L-NEW successor 58), CHECKER PASS (docs/checker/C130.md, checker PENDING)
- Object (L-NEW successor 58, Opus 5.5, D1 / D14 / D18, box 189; frozen, unchanged during review): packet P-N5-REACH,
  docs/new/P-N5-REACH.md, sha1 b7bd693744fdec2aa993f2133c22cbe724933ff0, 345 lines (l-new freeze 73b3d1fd, 2026-11-07T02:35:31Z;
  identical at 571c75c5, 727163f0 and fdf01b8c). Both referees measured it (REFEREE l. 21 «P-N5-REACH.md b7bd6937…;»; REFEREE-2 l. 6
  «docs/new/P-N5-REACH.md b7bd693744fd… (345 lines)»). Labels (l. 6-7): «PROVED (L-NEW 58, unrefereed) / DEAD (instance, machine-checked)
  / DATA / CONJECTURE / READING (not to sign).» To sign (table l. 10-21): §2 Theorem NO-REACH (a)-(d), §3 the game Γ3(G) and its size, §4
  Lemma S3-START, §5 Lemma PAD (a)-(c), §6 the transfer lemmas K3, PLAY3, SBAR3, TAU3, ESC3, W3, KEY3, §7 Theorem REACH3, §8 Corollary
  REAL-IDEAL-S3 (a), (b) («PROVED (reduction / necessity only)»), §9 DEAD SUBDIV (instances A, B); §10-§13 not to sign. Sections:
  premises (l. 23-79), §0 notation, Fact DUAL, Fact X (l. 81-92), §2 (l. 94-120), §3 (l. 122-136), §4 (l. 138-143), §5 (l. 145-155), §6
  (l. 157-240), §7 (l. 242-258), §8 (l. 260-268), §9 (l. 270-284), §10 DATA (l. 286-315), §11 (l. 317-324), §12 (l. 326-336), §13 (l.
  338-345). Source (l. 5): docs/new/N5-REACH-box189.md (f55dac37), history only; «This packet carries every proof in full and is checked
  against this text only.» (l. 5-6). The packet's own scope (l. 7-8): «NOT a TARGET.md claim; does NOT decide G-N5-TIME; NOT M3; not a
  step-4 pass. It bounds nothing and asserts nothing about whether long IDEAL-ACYC runs exist.»
  Fixes: docs/new/P-N5-REACH-fixes.md, append-only, three entries, entries 1-2 by L-NEW successor 58 and entry 3 by L-NEW successor 59
  (fdf01b8c: 85 lines, 9,935 bytes, sha1 be31f7741264c809ec306889ecb31046c1671598). Entry 1 (571c75c5): REFEREE's RE-L1, REFEREE-2's W-1, W-2, notes N-1..N-4, D-1; line L-2.
  Entry 2 (727163f0): REFEREE-2's W-3 and REFEREE's RC-1 (resolved by W-3), REFEREE's RC-2 in the Lead's «(a, b) order» form; line L-3.
  Entry 3 (fdf01b8c): CHECKER C130's E-1..E-4 with its §5 replacements R1-R4; line L-4. Each: «No statement, proof, tool, output or
  instance of the packet changes» (l. 8; l. 52-53 the same with «packet and entry 1 unchanged»; l. 73-74 «The packet and entries 1-2 are
  unchanged.») and «This entry carries no proof.».
  The RESULTS line is L-4, f85a024b8c8caa4c996fcd15bf1e78fbd436b534 (docs/new/P-N5-REACH-line-L4.txt, l-new fdf01b8c,
  2026-11-07T07:57:34Z, the file's only commit; 3,942 bytes). The title is L-4 verbatim, with nothing inserted (its date parenthesis
  «(2026-11-07)» and its source note are the line's own; the source note names the packet, which carries every proof; the fixes file
  carries none). L-4's parentheses balance (64 «(» / 64 «)»). Line history: L-1 (b12ec57a, 73b3d1fd, frozen with the packet); L-2
  (4de27b32, 571c75c5, fixes entry 1: L-1 with exactly three replacements, each old string once in L-1: RE-L1, REFEREE's text verbatim,
  adds the DATA counts of NO-REACH (d), S3-START, PAD, the SUBDIV instances and «Corollary REAL-IDEAL-S3 no separate DATA»; W-1,
  REFEREE-2's text verbatim, replaces L-1's quoted gloss «S3 can be simulated on every game by subdividing every edge» with the exact
  killed statement; W-2, REFEREE-2's text verbatim, replaces «{K2, K3, c_X}» with «K2, K3 and the unused even self-loop of priority 2»);
  L-3 (adfbb3b8, 727163f0, fixes entry 2: L-2 with exactly R1, REFEREE-2's W-3, «(every vertex but the unused even self-loop of priority
  2)» after the PAD count, and R2, REFEREE's RC-2 with «in (a, b) order» for its «in edge order» by Lead ruling); L-4 (f85a024b, fdf01b8c,
  fixes entry 3: L-3 with exactly CHECKER C130 §5's R1-R4, which are the first fill's R-A..R-D; see Fixes). Each step is the previous
  line with exactly the named replacements (my script, True ×3; both referees by their own scripts). L-2 MATCHES the byte test at REFEREE
  (cc9f4afd §C l. 185 «L-2 MATCHES the byte test.») and at REFEREE-2 (c420666d Addendum 1 l. 146 «**L-2 MATCHES after W-3**»). L-3:
  L-3 MATCHES at both referees, each after its own byte test: REFEREE successor 25 (85cc9ebb) §C add. 1 l. 195-199 (R1 and R2 once each in L-2; «L-2 + R1 = 3,687 B, sha1 46c2e507…, which is REFEREE-2's own computation for W-3.»; «L-2 + R1 + R2 is byte-equal to L-3.»), l. 200-208 (meaning: «RC-1 is SATISFIED; W-3 replaces it, as the Lead ruled.»; «The (a, b) form is better. RC-2 is SATISFIED.»), l. 209 «Verdict: fixes entry 2 is CORRECT. L-3 MATCHES, by the byte test and in meaning. All statements stay SIGNED.»; REFEREE-2 successor 30 (ddf42cb6) Addendum 2 l. 152-156 (own bt_l3.py: each old string once in L-2, each new once in L-3, «L-2 with R1, R2 == L-3 byte for byte, sha1 adfbb3b8219026b23a80b2081a3c227c35730451, 3,748 B»), l. 157-170 (meaning: R1 «names the same set as REFEREE's RC-1»; R2 «is the packet's own phrase»), l. 172-173 «Verdict: entry 2 **CORRECT**; **L-3 MATCHES** the packet with fixes entries 1-2, in bytes and in meaning (Opus 5.5, D1). Statement verdicts unchanged (all SIGN); W-1, W-2, W-3 all met.». Neither third round re-tested L-3's other DATA clauses against the counters; CHECKER C130 did (§3: E-1..E-4, the first fill's G-9 (i)-(iii) and G-D). L-4: L-4 MATCHES at both referees, each after its own byte test and a check of R1-R4 against reachcheck.py's counters at fdf01b8c: REFEREE successor 26 (419cc268) §C add. 2 l. 217-221 (R1-R4 parsed from fixes entry 3 and from C130 §5: «The two sets of strings are identical.»; «L-3 with R1-R4 applied is byte-equal to L-4 (sha1 f85a024b…, 3,942 bytes).»), l. 222-235 (R1-R4 against the counters), l. 246-247 «Verdict: fixes entry 3 is CORRECT. L-4 MATCHES, by the byte test and in meaning (R1-R4). All statements stay SIGNED; K3 is signed for every genome with fixes entry 1's reply as its proof of σ̄(K2) = r.»; REFEREE-2 successor 30 (d2b08049, its heading stamp corrected at d4838991) Addendum 3 l. 179-181 (own bt_l4.py: «L-3 with R1-R4 == L-4 byte for byte, sha1 f85a024b8c8caa4c996fcd15bf1e78fbd436b534, 3,942 B»), l. 182-194 (R1-R4 against the counters), l. 196-197 «Verdict: entry 3 **CORRECT**; **L-4 MATCHES** the packet with fixes entries 1-3, in bytes and in meaning» … «Statement verdicts unchanged (all SIGN); W-1, W-2, W-3 stay met.».
  Both diffed every clause of L-1 against the packet (REFEREE l. 118-122; REFEREE-2 l. 98-100 «Premises, NO-REACH, REACH3 (pads,
  priorities, n, S3-START, PAD, states, FL, fallback, L + 1 iterations), REAL-IDEAL-S3, the DATA counts (908 states, 1 iteration, 454
  genomes, L 9-59, 28/28) and the NOT-claims match the packet and my replays ✓.»); W-2 and RC-2 change wording of a definition (the
  unused loop; the pad order of the killed statement) to the packet's and R104's; no claim changes.
- Claims signed (REFEREE successor 25 (Opus 5.5, D15), report f66942c1, §C cc9f4afd, §C add. 1 85cc9ebb, and successor 26, §C add. 2
  419cc268; REFEREE-2 successor 29 «(Opus 5.5, D1/D18/D20)», report b0860fcd, and successor 30, Addenda 1-3 c420666d, ddf42cb6,
  d2b08049 / d4838991). Every row is SIGN in both verdict tables
  (REFEREE "## 0. Verdicts" l. 5-17 of R-P-N5-REACH.md; REFEREE-2 "## Verdicts" l. 10-22 of R2-P-N5-REACH.md), with no gap (REFEREE-2 l.
  22 «No statement is REFUSED; no gap. N-1..N-4 are notes that do not affect a verdict.»); they stand in every later round (REFEREE §C l.
  187 «All statements stay SIGNED.»; REFEREE-2 Addendum 1 l. 146-147 «Statement verdicts unchanged (all SIGN); W-3 is wording only and
  changes no count.»; REFEREE §C add. 1 l. 209 «All statements stay SIGNED.»; REFEREE-2 Addendum 2 l. 172-173 «Statement verdicts unchanged (all SIGN); W-1, W-2, W-3 all met.»; REFEREE §C add. 2 l. 246-247 «All statements stay SIGNED; K3 is signed for every genome with fixes entry 1's reply as its proof of σ̄(K2) = r.»; REFEREE-2 Addendum 3 l. 196-197 «Statement verdicts unchanged (all SIGN); W-1, W-2, W-3 stay met.»). Setting: N5 is SPEC S1-S5 (docs/new/N5-ssi-global.md, the N5 of RESULTS R57 and R104); S3 is
  SPEC's default start with FIX 1 (Even: «highest even priority, else lowest odd priority; equal priorities: largest index if even,
  smallest if odd.»; Odd the same rule on G^d); Γ(G) and its stated start, the IDEAL run and L(G), and the FL run are R104's (title l.
  9864); a genome is in IDEAL-ACYC when its Ξ-graph is acyclic. Notation (packet §0 l. 82-92): values (c, P, ℓ) and ⊳ as in SPEC S1;
  Ξσ: σ with Odd's optimal σ̄; Fact DUAL (G^d's order is Γ's reversed, so τ̄ maximises Γ's order); Fact X (IDEAL-ACYC: two options of one
  mover have different β-sets on their X-chains). Cells: REFEREE «SIGN» (l. 9-16; §6 «SIGN (every LENGTH and INDEX spot re-derived, §2
  below)», §7 «SIGN; replayed on two corpus games with L-COMP's n5b against my own simulator (§3)», §8 «SIGN as a reduction / necessity
  statement», §9 «SIGN; replayed with my own G^pad builder and n5b (§3)»); REFEREE-2 «**SIGN** (Opus 5.5, D1)» (l. 13-20; with N-2 at §3,
  N-1 at §6, «(replayed on my engine)» at §9).
  (a) Theorem NO-REACH (§2 l. 94-120) [EVERY genome G for (a)-(c); IDEAL-ACYC for (d)]: «(a) σ_j(K0) = K1 and σ_j(K1) = K0;» «(b)
    Ξσ_j(K0) = (K0, ∅, 0); no state (σ_j, τ_j) is a standard state of R104 (one with σ(K0) = K3, σ(K1) = K1); in particular no state of
    the run is a state of R104's REALIZE run for any mover state s;» «(c) K0 and K1 have no improving edge at any state: Iσ_j contains no
    edge out of K0 or K1.» and (d): for every j and every vertex v ∉ {K2, K3, c_X} the cycle node of Ξσ_j(v) ranks above every β-vertex,
    so no β-vertex lies in its P-set. Proof (l. 102-119): at j = 0, S3 / FIX 1 picks K0 → K1 (both of K0's successors odd, K1 the lowest)
    and K1 → K0 (the even one); while (a) holds, the play from K0 is K0 → K1 → K0 …, Ξσ_j(K0) = (K0, ∅, 0), K1's loop is shorter-worse
    (c even), K0 → K3 is worse through K1 ({K3} odd) or through K2 (Odd's loop bounds the reward below 0); S4a keeps σ off Iσ and S4c
    touches only improving vertices, so (a) and (c) hold by induction. (d): the only edge into K from outside is β → K0, and a cycle
    outside K without an e-vertex would be a Ξ-graph cycle; the cycle node is K0, c_W or an e-vertex, ranked above every β. Here c_X is
    R104's «an unused even self-loop of priority 2» (fixes l. 29-30); the line says so. The packet does not claim τ_j or the iteration
    count (l. 120).
  (b) The game Γ3(G) and its size (§3 l. 122-136) [every genome]: Γ(G) with its indices, priorities and owners unchanged, plus the pads
    (single-successor Even vertices) pA (Ω 0) on K0 → K3, s (Ω 0) on K1's loop, q (Ω 1) on K1 → K0, r (Ω 0) on K2 → K1, pe_g (Ω 1) on g
    → e_g and pβ_g (Ω 0) on g → β_g, pb_g (Ω 1) on β_g → u, m_(x,k) on x → g_(x,k) with Ω 2 if k = start(x) and Ω 0 otherwise, appended
    in the order of l. 124-125; top unchanged; 4M + 4 pads, n3 = N + 7M + 10; input size polynomial in N + M at bit cost. Transport:
    positional strategies of Γ and Γ3 correspond one to one; the STANDARD STATE of Γ3 for a mover state s is R104's start with the genome
    start replaced by s, transported (l. 135-136).
  (c) Lemma S3-START (§4 l. 138-143) [every genome]: «S3's start pair on Γ3(G) is the standard state of Γ3 for the genome start s_0.»
    Proof: FIX 1 at every vertex with two or more successors (mover: the unique Ω-2 pad; β_g: xt(g) over pb_g; K0: pA; K1: s; K3: K2; Odd
    gate: pe_g; Odd K2: its loop).
  (d) Lemma PAD (§5 l. 145-155) [every genome]: (a) every cycle of Γ3 other than the self-loop of c_X contains a vertex of Ω ≥ 3; (b)
    «for every pair of positional strategies and every vertex v ≠ c_X, the cycle node c of v's play has Ω(c) ≥ 3 > Ω(p) for every pad p:
    no pad is a cycle node and no pad is in a P-set.»; (c) values in Γ3 under transported strategies are those of Γ with the padded
    length; comparisons decided by reward or P-set are those of Γ.
  (e) The transfer lemmas (§6 l. 157-240) [IDEAL-ACYC; K3 and TAU3 every genome]: K3 (the core values, Iσ ∩ core = {(K0, K1)}, Iτ at K2
    empty, S4a's arena keeps pA at K0), PLAY3 (play shapes), SBAR3 (Odd's best reply is the β-face; Ξσ = φ), TAU3 (Iτ = ∅), ESC3 (S4a
    keeps σ off the movers), W3 (W graded 5ℓ + 5 and the same in every standard state; TIE(x) = R(x)), KEY3 (availability and the
    root-first keys are the IDEAL ones). Each is P-N5-REALIZE §3's lemma re-proved on Γ3; the LENGTH spots (K3 (b) at K3, SBAR3 at K2, W3)
    and the INDEX spot (KEY3 (b)) are re-proved with the padded lengths and indices, and both referees re-derived each (REFEREE §2 l.
    56-81; REFEREE-2 l. 45-58). K3 is labelled «every genome» while its (b) cites SBAR3: REFEREE-2 N-1, accepted (fixes l. 26-28); REACH3
    uses K3 only under IDEAL-ACYC. See the XC-3 NOTE below.
  (f) Theorem REACH3 (§7 l. 242-258) [IDEAL-ACYC]: «Let G ∈ IDEAL-ACYC with IDEAL run s_0 → s_1 → … → s_L, L = L(G). Then the N5 run of
    Γ3(G) FROM S3 has states 0, …, L equal to the standard states of Γ3 for s_0, …, s_L; transitions 1, …, L are FL transitions;
    transition L + 1 is a fallback.» Hence one FL run of length exactly L(G) if L ≥ 1, at least L(G) + 1 iterations, and no FL run if L
    = 0. Proof: induction on j (j = 0 is S3-START): τ is kept (TAU3); Iσ ≠ ∅ (ESC3), S4a's σ_new is a pointwise optimum of H ([1E-N3] P2)
    and equals σ off the movers (ESC3); at the movers, level by level, [RULE] gives the κ-least element of TIE(x) = R(x) (W3 (iii)), which
    KEY3 (a), (b) identify with the IDEAL choice s_(j+1)(x); so state j + 1 is the standard state for s_(j+1), S4c does not fire and W is
    kept (W3 (i)): an FL transition. At j = L the IDEAL run stops, σ_new = σ and τ_new = τ while Iσ ∋ (K0, K1): a fallback. Finiteness of
    L(G) is not assumed ([TERM]).
  (g) Corollary REAL-IDEAL-S3 (§8 l. 260-268) [a REDUCTION / NECESSITY statement only]: with FL-S3-POLY «there is a nondecreasing
    polynomial p such that, on every parity game on n vertices, every FL run of the N5 run FROM S3 has length ≤ p(n)» and IDEAL-ACYC-POLY
    «there is a polynomial q with L(G) ≤ q(N + M) for every G ∈ IDEAL-ACYC»: «(a) FL-S3-POLY ⇒ IDEAL-ACYC-POLY, with L(G) ≤ p(N + 7M +
    10).», and a polynomial bound on the number of iterations of N5 from S3 gives L(G) + 1 ≤ p(N + 7M + 10); (b) the contrapositive: a
    family in IDEAL-ACYC with L super-polynomial in N + M gives games Γ3(G_i), n_i = N_i + 7M_i + 10, of polynomial input size, on which
    N5 from S3 makes at least L(G_i) + 1 iterations. Proof: REACH3 on Γ3(G). «Not claimed: that such a family exists or does not exist;
    IDEAL-ACYC-POLY ⇒ FL-S3-POLY; anything for Ξ-cyclic genomes. This packet says nothing about how long IDEAL-ACYC runs are.» (l.
    267-268).
  (h) DEAD SUBDIV (§9 l. 270-284) [DEAD, by two instances]: the statement killed is that, for every game G and start pair (σ0, τ0), G^pad
    (every priority + 4, every edge (a, b) subdivided by an Even pad p(a, b) with «indices n, n + 1, … in (a, b) order», Ω(p) = 2 if a
    is Even and b = σ0(a), 1 if a is Odd and b = τ0(a), 0 otherwise) has an N5 run from S3 equal, state for state and transition for
    transition (fallbacks included), to the transported run of G from (σ0, τ0). Instance A: n = 3, Ω (3, 3, 1), owners (Odd, Even, Odd),
    0 → {1}, 1 → {0, 1, 2}, 2 → {0}, σ0(1) = 1, τ0(0) = 1, τ0(2) = 0: G 1 iteration with 1 fallback, G^pad (n = 8) 1 iteration with 0
    fallbacks (the projected states are equal; the fallback flag differs). Instance B: n = 5, Ω (3, 2, 4, 0, 0), owners (Odd, Odd, Even,
    Odd, Even), 0 → {1, 3, 4}, 1 → {2, 3}, 2 → {3, 4}, 3 → {0, 2, 3}, 4 → {1, 4}, σ0(2) = 4, σ0(4) = 1, τ0(0) = 4, τ0(1) = 2, τ0(3) =
    2: G 2 iterations, G^pad (n = 17) 3. S3's start on G^pad IS the transported (σ0, τ0) in both (FIX 1); the run is not. Both referees
    replayed both instances with their own G^pad builders (REFEREE l. 102-105 on n5b; REFEREE-2 l. 77-78 on its own engine).
- XC-3 NOTE (K3 and SBAR3; a note: it changes nothing in the line). REFEREE successor 26, §C add. 2 (419cc268) l. 236-245, on REFEREE-2's N-1 and its own item XC-3 on the later packet P-N5-XICYC: «K3 (b) ends «These values hold once SBAR3 gives σ̄(K2) = r», and SBAR3 is IDEAL-ACYC, so the label «every genome» of K3 is incomplete as printed. My miss in this report (§0 signed K3 with that label).» Fixes entry 1's reply (l. 26-28: «K is closed, so K's values depend only on the strategies on K, and Odd's unique best at K2 is r») gives σ̄(K2) = r in every standard state for every genome (REFEREE l. 238-240), and «Together they settle it: K3 (a)-(d) hold for every genome.» (l. 241). «For R117 nothing changes. REACH3 and Corollary REAL-IDEAL-S3 are IDEAL-ACYC, where SBAR3 itself holds. TAU3 and NO-REACH use K3 (c) or no K3. The line does not mention K3.» (l. 242-243). So REFEREE's earlier SIGN of K3 with the «every genome» label missed K3 (b)'s use of SBAR3; that SIGN now rests on fixes entry 1's reply (l. 246-247); no clause, count or scope of L-4 depends on it (L-4 does not name the lemma K3: its three «K3» are the vertex K3 of Γ(G), in «K0 → K3», «σ(K0) = K3» and «outside K2, K3», by script).
- The RESULTS line (L-4, the title): «N5 (SPEC S1-S5) from its DEFAULT start S3 (SPEC S3 with FIX 1), on the games of RESULTS R104» …
  «(2026-11-07) — a REDUCTION / NECESSITY statement only (no count is bounded; nothing is claimed about whether long IDEAL-ACYC runs
  exist; Ξ-cyclic genomes are not covered; the converse is not claimed;» … «G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a
  TARGET.md claim) (P-N5-REACH, docs/new/P-N5-REACH.md; L-NEW successor 58)». Its clauses: NO-REACH = (a); Γ3 = (b); S3-START = (c);
  PAD = (d) (the line drops §5 (b)'s «v ≠ c_X», harmless: c_X's only edge is its loop); REACH3 = (f); REAL-IDEAL-S3 = (g); the DEAD
  clause = (h), its instances named as packet §9's instances A and B (R4). The transfer lemmas (e) are proof steps of REACH3, not clauses of the line.
- Premise: RESULTS R104's definitions only, no R104 theorem (packet [DEF], l. 24-43): the IDEAL model, L(G), the Ξ-graph, Γ(G) with its
  vertex indices and stated start, and the FL run, quoted from R104's title l. 9864 (prem117.py: each quote 1 hit, there); where R104's
  line leaves a detail to «packet §3.1», the packet uses R104's packet of record (the β-vertex order; Ω(e)), and «The proofs below use of
  Ω(e) only that it is even and lies strictly between every Ω(β) and top.» (l. 42-43). SPEC S1-S4 with FIX 1 (packet [SPEC], l. 44-55;
  docs/new/N5-ssi-global.md, sha1 66fde9ef…, each quote 1 hit at its cited line): S2 (Iσ, Iτ), S3 / FIX 1 (the default start), S4a-S4c
  (the arena H, «Else σ_new = σ.», «Else τ_new = τ.», FALLBACK), S1 (values; Odd on G^d). R104's three premises as landed, in R104's
  forms: [1E-N3] (R104 l. 9975-9978, with R57 (b) l. 2915-2916 «that S1's procedure realises an optimal σ̄ is VJ00 §6» «plus SPEC
  conformance, and the code's match to SPEC is DATA (R15 G-N5T-1) (1E-N3 = N-1E-1).»), forms P1 (σ̄, τ̄ pointwise optima) and P2 (S4a's
  σ_new a pointwise optimum of H); [RULE] (R104 l. 9989-9992: R24 (a) Lemma R and R24 (b)'s choice rule with R103's bridge B, Lead reading
  L46, at every Even vertex that is not its own W′-cycle node, R103's (R1) ruling), in R104's form «σ_j(x) is the κ_j-least element of»
  «TIE_j(x)» (l. 10004-10005); [VJ-LOC] (R104 l. 10011-10012, R36 (c) Lemma P1 on the dual game, l. 1730-1731, setting l. 1723-1724).
  [TERM] RESULTS R15 (d) (l. 640-642) «N5: every iteration applies Switch_I with ∅ ≠ I ⊆ Iσ to Even's σ (on G) and/or with ∅ ≠ I ⊆ Iτ
  to Odd's τ (on G^d), and» … «Hence no (σ, τ) state repeats and N5 terminates», for the finiteness of L(G) only. Packet l. 78-79:
  «Nothing else is used. P-N5-REALIZE (claude/l-red docs/red/P-N5-REALIZE.md, sha1 067f06b6…, fixes entries 1-3) is the SOURCE of the
  proof pattern of §6; every step of §6 is proved here.» Both referees checked the 38 premise quotes (REFEREE l. 28-31; REFEREE-2 l.
  25-29) and that no R104 theorem is used (REFEREE l. 32-33; REFEREE-2 l. 30-31 «No R104 THEOREM used ✓.»).
- L41 and L43. The proofs are L-NEW successor 58's (packet l. 2-6); the fixes entries carry none. REFEREE's RE-L1 and RC-2, REFEREE-2's
  W-1, W-2, W-3 and CHECKER C130's R1-R4 are wording of the line, applied verbatim (RC-2 in the Lead's form); the referees'
  reach_replay.py, subdiv_replay.py, t3r_sim.py, r2reach.py, reachcheck_r2.py, bt_l2.py and bt_l4.py are checking tools. Nothing referee-written is a proof step of the entry (my
  reading; neither referee mentions L41). L43: SUBDIV is not an asymptotic statement; it is DEAD by two explicit instances, replayed by
  both referees.
- Fixes (docs/new/P-N5-REACH-fixes.md, append-only, entries 1-2 by L-NEW successor 58, entry 3 by L-NEW successor 59; entry 1 at
  571c75c5, the file then 47 lines, sha1 307651b2779f3df1fb8857de2974d3ffdd69ac6a; entry 2 at 727163f0, l. 49-69, the file then 69
  lines, sha1 547740887c7974798206b4075d67f6a379cbfe47; entry 3 at fdf01b8c, l. 71-85, the file now 85 lines, 9,935 bytes, sha1
  be31f7741264c809ec306889ecb31046c1671598, its l. 1-69 = entry 2's file, by script):
  - Entry 1 (after REFEREE f66942c1 and REFEREE-2 b0860fcd): RE-L1 (REFEREE, «required, DATA coverage; ACCEPTED»), each count checked
    against reachcheck.py's counter (l. 9-19); W-1 (the killed statement in REFEREE-2's words; the old span chosen as «the shortest one
    that the new text replaces», l. 20-23, confirmed by REFEREE §C l. 159-161 and REFEREE-2 Addendum 1 l. 122-124); W-2 (c_X in R104's
    words); notes N-1 (K3 for every genome), N-2 (c_X), N-3 (the priority bound assumes β-ranks 0..M − 1; not signed), N-4 ([RULE] at
    transition L + 1 as in R104), D-1 (NR-LAM checks only the cycle node of Ξσ(K0)); line L-2.
  - Entry 2 (after REFEREE §C cc9f4afd and REFEREE-2 Addendum 1 c420666d): W-3 and RC-1, the PAD count's set (the counter skips c_X);
    «RC-1 is RESOLVED BY W-3 (Lead ruling 04:02Z: W-3's wording reuses W-2's term).» (l. 55-56). RC-2, the pad order of the killed
    statement: «RC-2 (REFEREE), ACCEPTED with a change by Lead ruling (04:15Z, «Option B»).» (l. 58); «Reason: the packet's wording (§9
    l. 272 «indices n, n + 1, … in (a, b) order»; subdiv.pad: E = sorted((a, b))); «edge order» is ambiguous (it could be read as the
    input order). REFEREE's predicted sha1 for L-3 therefore does NOT apply; both referees byte-test the result below.» (l. 59-61). The
    Lead's rulings, as recorded in LEAD-STATE l. 2438: «Lead ruling: W-3 wording for PAD (resolves RC-1), RC-2 in «(a, b) order» per §9
    l. 272 (Option B) -> L-3 at L-NEW.». Line L-3 = L-2 with R1 (W-3) and R2 (RC-2, Lead ruling), each old string once (l. 62-68).
  - Entry 3 (after CHECKER C130 126f9772, «Verdict: FAIL (E-1 to E-4, all DATA wording; one L-4 with four replacements, §5)» (C130 l. 16)): «E-1 (NO-REACH count: unit; NR-CORE uncited), E-2 (the no-improving-edge clause had no counter and was not in the line's no-DATA list), E-3 (the 28 games were unnamed), E-4 (the DEAD SUBDIV instances were not reproducible from the line): all ACCEPTED.» (l. 75-76); «The strings are C130 §5's verbatim (wrapped lines joined with single spaces).» (l. 76-77).
    Line L-4 = L-3 with exactly R1-R4 (l. 78-84), each old string once in L-3. My script (l4rel117.py): the four pairs of entry 3, of
    C130 §5 (l. 108-115) and of the first fill's R-A..R-D are the same, and L-3 + R1-R4 = L-4 (True). How each E-item is resolved (by
    script on L-4; each new string once in L-4): E-1 by R1, the NO-REACH count now names NR-CORE («σ(K0) = K1 and σ(K1) = K0 at all 908
    states of the S3 runs on Γ(G)») and NR-STD («0 of them equal to R104's stated start off the movers»), and «0 standard states in 908
    states» occurs 0 times in L-4; E-2 by R2, the line's no-DATA list now reads «NO-REACH's no-improving-edge clause and Corollary
    REAL-IDEAL-S3 no separate DATA»; E-3 by R3, the set is named, «the 28 games Γ(G) and Γ3(G) of the 14 corpus genomes» and «with
    verify OK on the same 28», and «28/28» occurs 0 times in L-4; E-4 by R4, «the n = 3 and n = 5 games with the start pairs of packet
    §9 (instances A, B)», and «with given start pairs» occurs 0 times in L-4. The packet is frozen, named in the source note and pinned
    (b7bd6937 in reach.pins).
  - No entry changes a statement, a proof, a tool, an output or an instance (l. 7-8, 52-53, 73).
- Not signed: packet §10 (DATA, «not to sign»), §11 (CONJECTURE BLIND, CONJECTURE SUBDIV-APPROX, the context READING on L-LOWER's
  REC_d10_tower), §12 (pins, commands), §13 (TARGET diff and limits, READING); the SUBDIV obstruction (§9 l. 280-284, «Obstruction
  (READING, from the traces; not to sign)»); fixes entry 1's note N-3. NOT landed.
- Referee strengthening (NOT part of this entry; referee checks):
  (i) REFEREE: REACH3 replayed with L-COMP's n5b (spec mode, default start S3) against its own IDEAL simulator t3r_sim.py on the two pinned
    Γ3 games (RECT_d11_T59_g3, n 340, L 59, 62 iterations, 1 fallback; REC_d10_tower_mu30_g3, n 310, L 35, 38 iterations, 1 fallback),
    each with the maximal FL run from state 0 equal to L(G), transition L + 1 a fallback and the mover choices equal to the IDEAL states
    (l. 92-101); SUBDIV replayed with its own G^pad builder on n5b (l. 102-105); the check block re-run (l. 106).
  (ii) REFEREE-2: its own Γ(G) builder (from its R104 review) plus its own pads, its own S3 and its own SPEC state loop on the fleet's si.py
    Engine, «No box21/n5x, no box189 code.» (l. 63-66); its Γ3 and S3 start equal the two pinned games BYTE FOR BYTE (l. 67-68); REACH3 on
    all 14 corpus genomes, FL runs = [L(G)] exactly, L 9-59 (l. 69-72); NO-REACH on the same 14 (l. 73); L-COMP's n5b on the two pinned Γ3
    games, 38 and 62 iterations (l. 74-75); a control with all mover pads Ω 0 breaks S3-START and REACH3 (l. 76); SUBDIV on its own builder
    (l. 77-78); both check blocks re-run (l. 79); in Addendum 1, reachcheck.py with counters added (reachcheck_r2.py) for the DATA rule:
    698,204 triples with c_X, 0 at c_X on its 5,174 (l. 126-139).
  (iii) REFEREE §C add. 1: the pad order of the killed statement checked against its own builder, l. 204-206 «It reads as the lexicographic order of the edges (a, b), which is subdiv.pad's sorted((a, b)) and the order my own builder used (scratch/subdiv_replay.py: edges = sorted((a, b))).», so its SUBDIV replay stands for the statement as landed; a note without a fix, l. 208 «Note (no fix): «(a, b)» is not bound earlier in the line, but «every edge … (a, b) order» reads unambiguously as edges (a, b).». REFEREE-2 Addendum 2: subdiv.pad's order read against the line (l. 164-166) and its predecessor's builder r2reach.py subdiv() checked to append pads in the same (a, b) order on instances A and B (every successor list sorted), so «r2reach_subdiv.out (A: fallbacks 1 vs 0; B: iterations 2 vs 3, projected states differ) is a replay of the corrected statement too ✓.» (l. 167-170).
  (iv) The L-4 rounds tested R1-R4 against reachcheck.py's counters at fdf01b8c. REFEREE §C add. 2 l. 222-235: R1's first half is NR-CORE; for its second half, «The σ-only phrase «0 of them equal to R104's stated start off the movers» follows from NR-CORE = 0, since every state has σ(K0) = K1 while the start has σ(K0) = K3.» (NR-STD tests the stated start off the movers and τ together); R2: NO-REACH (c) «has no counter in reachcheck.py (it never reads Iσ)»; R3 from xcheck.sh's loop and xcheck.out's 28 rows; R4 against its own G^pad replay of §C add. 1. REFEREE-2 Addendum 3 l. 182-194: R1's second half is NR-STD, whose predicate it read against gamma3.build's stated start (gamma3.py l. 67-70); R2 checked independently by its predecessor's r2reach.py on the 14 corpus genomes («NOREACH_noKimpr true»); R3 and R4 against xcheck.out and packet §9. The two read R1's second half through different counters (NR-CORE by arithmetic, NR-STD directly); reachcheck.out has both at 0 («standard 0, core-not-(K0->K1,K1->K0) 0»).
- Honest limits: (i) A REDUCTION / NECESSITY statement only: no count is bounded, no run is shown long or short; it claims nothing about
  whether super-polynomial IDEAL-ACYC families exist (packet l. 7-8, §8 l. 267-268). It does not decide G-N5-TIME; it is not M3, not a
  step-4 pass and not a TARGET.md claim. (ii) Premises [1E-N3], [RULE], [VJ-LOC] as landed in R104: the correctness of S1's procedure stays
  SPEC's requirement, and the code's match to SPEC is DATA (R57 (b)); every N5 run in the DATA is a run of an implementation (n5x; n5b; the
  referees' engines). (iii) Ξ-cyclic genomes are not covered. (iv) Γ3 is one padding; other paddings and other start rules are not studied;
  SUBDIV shows that subdividing every edge uniformly does NOT reproduce the run of a game from a given start pair (DEAD), so REACH3 is a
  statement about Γ3's pads only. (v) NO-REACH speaks of Γ(G) only; it does not say that N5 from S3 is
  fast or slow on any class (its 1-iteration runs are DATA). (vi) The DATA's long runs come from the 14 corpus genomes (L 9-59, n ≤ 370);
  R440 has L ≤ 2 (94 genomes with L = 0), so the random part tests REACH3 weakly (packet l. 301). Packet §11 (the tower context and its two
  lane conjectures) is context only and plays no part in this entry. (vii) Names: «REAL-IDEAL» is R104's Corollary (every start pair, Γ(G)); «REAL-IDEAL-S3» is
  this entry's (S3, Γ3(G)); «NO-REACH», «REACH3», «S3-START», «PAD», «SUBDIV» and «Γ3» are new to RESULTS. (viii) The first fill's DATA flags
  (G-9 (i)-(iii), G-D) were CHECKER C130's E-1..E-4 and are fixed in L-4 by R1-R4 (fixes entry 3). C130's two notes stand: NO-REACH
  (a)-(c) is stated for every genome, its DATA is on acyclic genomes only (N-1); the line's DATA names neither its tool nor its corpus
  directory, which packet §10, named by the source note, gives (N-2).
- Data (DATA, not proof): experiments/new/box189/reachcheck.py (l-new 73b3d1fd, unchanged at 571c75c5, 727163f0 and fdf01b8c, sha1
  c368b363ff654c8e7aead970f866b7e4d482f793, 183 lines; engine experiments/new/box21/n5x.py, SPEC S1-S5 on si.py's Engine; builder
  gamma3.py; SUBDIV builder subdiv.py) prints reachcheck.out (sha1 af50ee340e11c35209c39496e7354925e832d3eb): «C14+R440 NO-REACH runs 454
  states 908: standard 0, core-not-(K0->K1,K1->K0) 0, cycle-node(K0)!=K0 0; (state, vertex) pairs 42880: beta-in-P-or-low-cycle-node 0;
  iterations histogram {1: 454}», «C14+R440 S3-START genomes 454: S3 != stated start 0», «C14+R440 PAD (state, vertex, world) triples
  693030: pad-in-P-or-cycle-node-Om<3 0», «C14+R440 REACH3 genomes 454 (states 0..L checked 1225): failures 0», «C14+R440 W3 (state,
  mover) pairs 11642: W(x) != (c_W, empty, 5 lev + 5) 0», the 14 «C14 …» rows (e.g. «C14 RECT_d11_T59_norm.json N 22 M 44 L 59 Gamma3 n
  340 S3-iterations 62 fallbacks 1 REACH3 ok»), the two SUBDIV-DEAD lines and two CONJECTURE lines (BLIND, SUBDIV-APPROX). Sets: C14 = the
  14 genomes of box189/corpus (4 L-RED r187 A_* genomes, 10 L-LOWER l3/kill genomes order-preservingly normalised by norm.py); R440 =
  gen(Random(seed)), seed 1-440. Wired into experiments/new/check.sh (run by scripts/verify.sh): block «P-N5-REACH» (l. 950-957 at
  fdf01b8c: the re-run diffed against reachcheck.out, the sha1 pins of reach.pins 1a075f50, which adds L-4 and the fixes be31f774 to
  11ebdbee's list, five DATA lines asserted) and block «BOX 189
  REACH» (l. 943-949: three pinned genomes, two .pg instances regenerated byte-identically). Re-run from a git archive of fdf01b8c at
  this second fill: 2026-11-07T08:51:44Z-08:52:04Z, rc 0, both PASS, the P-N5-REACH line with «pins (reach.pins 1a075f50: packet
  b7bd6937, line L-1 b12ec57a, fixes be31f774, line L-2 4de27b32, line L-3 adfbb3b8, line L-4 f85a024b,» (first fill: 727163f0,
  04:54:26Z-04:54:43Z, rc 0, both PASS; CHECKER C130 l. 21: rc 0, PASS). Oink and a second engine: xcheck.sh (not in check.sh; it needs Oink) runs L-COMP's
  experiments/n5-second/n5b.py --mode spec from its default start on the 28 games Γ3(G) and Γ(G) of the 14 corpus genomes and checks
  n5b's solutions with experiments/new/check_sol2.py (Oink 8fbf0a7 --zlk, harness/verify.py): xcheck.out, 28 lines, each «zielonka(oink
  zlk) OK strategies verified»; n5b's iterations and fallbacks equal the lane engine's on 28/28 (Γ3: L + 3 and 1; Γ: 1 and 0). Neither
  referee ran Oink (REFEREE l. 107 «Oink: NOT RUN by me (Oink not built in this container). The lane's xcheck.out is lane DATA.»;
  REFEREE-2 l. 80 «Oink cross-check (xcheck.sh): NOT RUN by me (Oink not built here); xcheck.out has 28/28 «OK strategies verified» lines
  (lane DATA).»); the drafter re-ran xcheck.sh with Oink 8fbf0a7 built in the Lead's container, at 727163f0 (8 s) and at fdf01b8c
  (2026-11-07T08:55:43Z-08:55:53Z, rc 0; xcheck.sh and xcheck.out unchanged at fdf01b8c), and CHECKER C130 re-ran it from fd1266a5 (l.
  46-48): output byte-equal to xcheck.out each time. Oink checks n5b's final solutions, not the runs. L(G) cross-check: the 10 L-LOWER genomes' L equal the T column of
  claude/l-lower experiments/lower/l3/kill/README.md (12216a37) (packet l. 304-305; not re-checked by me).
- Signatures: REFEREE docs/referee/R-P-N5-REACH.md: successor 25's report f66942c1ab2cdd45987c033fa6015e6daaaea789 (2026-11-07T03:04:24Z),
  «I did not read docs/referee-2/ for this report.» (l. 2-3), verdict table l. 5-17, «FINDINGS: §2-§9 all SIGN; L-1 NOT YET (RE-L1, DATA
  coverage only).» (l. 145); §C cc9f4afd (2026-11-07T03:58:16Z), l. 148-187, «Fixes entry 1 is CORRECT as an application of RE-L1, W-1
  and W-2.», «L-2 MATCHES the byte test.», «In meaning, L-2 is NOT YET: RC-1 (my own RE-L1 wording) and RC-2. With both, the line
  MATCHES.», «All statements stay SIGNED.» (l. 184-187); §C add. 1 85cc9ebb: 85cc9ebb8976bb68b62345162d0d4b69c660cca9 (2026-11-07T04:50:03Z), l. 189-209, «Verdict: fixes entry 2 is CORRECT. L-3 MATCHES, by the byte test and in meaning. All statements stay SIGNED.» (l. 209); successor 26's §C add. 2 419cc2689733b0c3cf657386314d0c8ca5a410c3 (2026-11-07T08:23:51Z; heading «date -u at writing 2026-11-07T08:23Z»), l. 211-247, «Verdict: fixes entry 3 is CORRECT. L-4 MATCHES, by the byte test and in meaning (R1-R4). All statements stay SIGNED; K3 is signed for every genome with fixes entry 1's reply as its proof of σ̄(K2) = r.» (l. 246-247). REFEREE-2 docs/referee-2/R2-P-N5-REACH.md:
  successor 29's report b0860fcd (2026-11-07T03:06:42Z), «Independent: docs/referee/ not read for this packet before this push.» (l. 2-3),
  verdict table l. 10-22, «F-3: L-1 MATCHES after W-1, W-2.» (l. 114); successor 30's Addendum 1 c420666d (2026-11-07T03:59:26Z), l.
  116-147, «Verdict: entry 1 **CORRECT** for W-1, W-2, RE-L1 as applied; **L-2 MATCHES after W-3** (Opus 5.5, D1).» (l. 146);
  Addendum 2 ddf42cb6: ddf42cb6c15e49c38692239b65a33e69f346c726 (2026-11-07T04:50:08Z), l. 149-173, «Verdict: entry 2 **CORRECT**; **L-3 MATCHES** the packet with fixes entries 1-2, in bytes and in meaning (Opus 5.5, D1).» (l. 172); Addendum 3 d2b08049ba14c38cdae4a9ae9e38c80736d0317f (2026-11-07T08:23:41Z), its heading stamp «08:3xZ» corrected to «08:2xZ» by d4838991f4ce8cc9e0115d701f6d377054ca17e1 (2026-11-07T08:23:54Z, the only change), l. 175-197, «Verdict: entry 3 **CORRECT**; **L-4 MATCHES** the packet with fixes entries 1-3, in bytes and in meaning» … «Statement verdicts unchanged (all SIGN); W-1, W-2, W-3 stay met.» (l. 196-197). Lane: L-NEW successor 58, 73b3d1fd (freeze), 571c75c5 (fixes entry 1, L-2), 727163f0 (fixes
  entry 2, L-3); L-NEW successor 59, fdf01b8c (fixes entry 3, L-4).
- INDEPENDENCE: the proofs are L-NEW's; each referee re-derived every step, the LENGTH and INDEX spots in full (REFEREE §2; REFEREE-2
  «Proof checks»), and replayed REACH3 and SUBDIV on engines that are not L-NEW's: REFEREE with L-COMP's n5b (experiments/n5-second, its
  own SI in hard-families/pgsolver_si, not si.py) and its own IDEAL simulator, on the two pinned games; REFEREE-2 with its own builder
  and SPEC state loop (r2reach.py) on the fleet's si.py Engine, on all 14 corpus genomes, and with n5b on the two pinned games. The
  valuation Engine si.py is shared by n5x (L-NEW's engine) and REFEREE-2's loop; n5b shares no code with either. Each referee wrote its
  report without reading the other's (REFEREE l. 2-3; REFEREE-2 l. 2-3); the line rounds read the other's W- / RC-items by design (fixes
  entries 1-2). The DATA wording of L-4 is REFEREE's (RE-L1), REFEREE-2's (W-3) and CHECKER C130's (R1-R4: the first fill's
  R-A..R-D, which C130 tested against the counters and adopted, l. 118-119); in the L-4 round each referee byte-tested L-4 with its own
  script and read R1-R4 against reachcheck.py itself.
- TARGET.md diff: TARGET.md §1 defines a parity game («A parity game is G = (V, V_E, V_O, E, pr) with V finite»; «every vertex has at
  least one successor (self-loops allowed)»); Γ(G), Γ3(G) and the SUBDIV games are such games (every vertex of Γ3 has a successor; every
  pad has one), and «on every n-vertex game» in the Corollary ranges over them; «polynomial» is in n at bit cost (TARGET.md §3), and Γ3(G)
  has polynomial input size (packet §3 l. 131-132). No statement of this entry is M4 (TARGET.md §2), names an algorithm's running time or
  claims a winning region; it is not an algorithm claim, so TARGET.md §5's gauntlet does not apply, and it is not a step-4 pass. The line
  (L-4) makes no TARGET claim; its tail reads «a REDUCTION / NECESSITY statement only (no count is bounded;» and «G-N5-TIME stays OPEN;
  not M3, not a step-4 pass, not a TARGET.md claim» (L-4, by script). GAPS G-N5-TIME: open.

Proposed GAPS line-11 UPDATE (append-only), to go AFTER the last UPDATE on GAPS l. 11 at landing (R116's, «UPDATE 2026-11-07 07:42Z:
RESULTS R116 (P-IDEAL-MOVES; CHECKER C129 9246878c)», at this second fill), as a pure insertion with one separating space before the
row's closing « |». BUILT FROM L-4 by upd117b.py (R104's build() call with R111's DEAD-clause step, G-U; controls R97-R116 rebuilt byte
for byte, True ×20; sha1 b4d74e094a30cba61017eeda4a0c33cb7a1db6f3 of the line without newline and unfilled, = C130 §5's «Rebuilt UPDATE
(no newline, unfilled)»). <DATE>, <HH:MM> and <checker> are the landing date, time and the C130 commit, all filled at landing:
UPDATE <DATE> <HH:MM>Z: RESULTS R117 (P-N5-REACH; CHECKER C130 <checker>) [refereed-only] LANDED: N5 (SPEC S1-S5) from its DEFAULT start S3 (SPEC S3 with FIX 1), on the games of RESULTS R104 (premise: R104's definitions of the IDEAL model, L(G), the Ξ-graph, the game Γ(G) with its vertex indices and start, and the FL run; no theorem of R104 used), with R104's premises as landed (1E-N3 = RESULTS R57 (b) in its two forms; RESULTS R24 (a) Lemma R and R24 (b)'s choice rule with RESULTS R103's bridge B and (R1) ruling; RESULTS R36 (c) Lemma P1 on the dual game) and RESULTS R15 (d) for termination only: for EVERY genome G the N5 run of Γ(G) from S3 has σ_j(K0) = K1 and σ_j(K1) = K0 at every state j (S3 picks them, and K0, K1 never have an improving edge while they hold), so it never visits a state with σ(K0) = K3, σ(K1) = K1, i.e. none of R104's REALIZE states, and, for acyclic G, no β-vertex is ever in the P-set of Ξσ_j at a vertex outside K2, K3 and the unused even self-loop of priority 2 (Theorem NO-REACH); for every G with an ACYCLIC Ξ-graph, the game Γ3(G) obtained from Γ(G) by 4M + 4 single-successor Even pads of priority ≤ 2 (pA on K0 → K3, s on K1's loop, q on K1 → K0, r on K2 → K1, pe_g and pβ_g on both faces of every gate g, pb_g on every β_g → u, and m_(x,k) on every mover edge x → (x, k) with priority 2 for the genome start and 0 otherwise, appended after Γ(G)'s vertices; n = N + 7M + 10) has S3's start pair equal to R104's stated start transported through the pads (Lemma S3-START), no pad is ever a cycle node or in a P-set (Lemma PAD), and the N5 run of Γ3(G) FROM S3 has states 0, …, L(G) equal to the transported REALIZE states of the IDEAL run, transitions 1, …, L(G) are FL transitions and transition L(G) + 1 is a fallback, so if L(G) ≥ 1, [0, L(G)] is one FL run of length exactly L(G) and the run makes at least L(G) + 1 iterations (no FL run if L(G) = 0) (Theorem REACH3); hence if every FL run of N5 from S3 on every n-vertex game has length at most p(n) for a nondecreasing polynomial p (in particular if N5 from S3 makes at most p(n) iterations), then L(G) ≤ p(N + 7M + 10) for every acyclic G, and a family of acyclic genomes with L super-polynomial in N + M would give games on which N5 from its default start makes super-polynomially many iterations (Corollary REAL-IDEAL-S3); the statement that, for every game and start pair, the game with every priority + 4 and every edge subdivided by an Even pad of priority 2 (Even, start edge), 1 (Odd, start edge) or 0, the pads indexed after the game's vertices in (a, b) order, has an N5 run from S3 equal state for state and transition for transition (fallbacks included) to the run of the game from that start pair is DEAD as stated (DEAD SUBDIV: the n = 3 and n = 5 games with the start pairs of packet §9 (instances A, B) whose padded N5 runs from S3 differ in a fallback flag, resp. in the iteration count, 2 vs 3): a REDUCTION / NECESSITY statement only; no count is bounded; nothing is claimed about whether long IDEAL-ACYC runs exist; Ξ-cyclic genomes are not covered; the converse is not claimed; DATA: on 14 corpus genomes (L(G) 9 to 59) and 440 random acyclic genomes, σ(K0) = K1 and σ(K1) = K0 at all 908 states of the S3 runs on Γ(G) and 0 of them equal to R104's stated start off the movers, every such run 1 iteration, 0 failures of REACH3 in 454 genomes, the β-free P-sets of NO-REACH 0 on 42,880 (state, vertex) pairs, S3-START 0 on 454 genomes, PAD 0 on 693,030 (state, vertex, world) triples of the S3 runs on Γ3 (every vertex but the unused even self-loop of priority 2), both DEAD SUBDIV instances re-run, NO-REACH's no-improving-edge clause and Corollary REAL-IDEAL-S3 no separate DATA, n5b (SPEC mode) iteration counts equal on the 28 games Γ(G) and Γ3(G) of the 14 corpus genomes and Oink 8fbf0a7 --zlk with verify OK on the same 28 (P-N5-REACH, docs/new/P-N5-REACH.md; L-NEW successor 58). G-N5-TIME stays open.

Addendum (subagent, for the Lead; does not land; written 2026-11-07T06:35:21Z by date -u).
(1) MERGES AND COMMIT. No merge by me. When the Lead's push.sh ended (pgrep empty at 2026-11-07T06:02Z), the Lead had already merged all four branches into the local trunk (--no-ff): 3c89b1b8 (l-new f09f67ec: box 191 only after 727163f0; the P-N5-REACH files, experiments/new/box189/ and check.sh's REACH blocks unchanged, git diff), 8c545266 (referee e74638b6, holding 85cc9ebb; R-P-N5-REACH.md unchanged after it), a3033a91 (referee-2 ddf42cb6), b7f37ce8 (checker 4195a8c3, the CHECKER handover; no docs/checker/C130.md). After them the Lead committed f7fcfccd (06:02:38Z, the R116 second fill, docs/agents/R116-draft.md). RESULTS, GAPS, TARGET.md and DECISIONS are unchanged from 5ec57d84 to f7fcfccd (git diff, empty). Then the commit holding this file (subject: Lead: R117 draft (P-N5-REACH, line L-3) for CHECKER C130), docs/agents/R117-draft.md only. Not pushed by me; the Lead pushed f7fcfccd (origin trunk at 06:35Z), so 727163f0, 85cc9ebb and ddf42cb6 are ancestors of origin trunk (git merge-base --is-ancestor); this commit is not pushed.
(2) TITLE l. 300 = "### R117 [refereed-only] " + L-3 without its newline + ", CHECKER PASS (docs/checker/C130.md, checker PENDING)",
checked by script (chk117.py): equal, byte for byte (True); the only «### R» heading of this file; 3,783 characters, 3,826 bytes;
sha1 of the heading line without its newline 79b92aae489538586fec1090024c3f6835877712; 60 «(» / 60 «)» (L-3's 59 and the fill's), depth never negative, 0 "|".
(3) SHAPE. The entry block is l. 300-519 (python slice d[299:519]), followed by a blank line; 0 "|" in it; the GAPS preamble is l.
521-524; the UPDATE is l. 525 (d[524]), sha1 ce44ee1f3c297ff3e99ff63d21d76b4c361e0539 without newline (= upd117L3.txt, True), 3,779 bytes, 58 «(» / 58 «)», 0 "|",
one each of «<DATE>», «<HH:MM>», «<checker>». A landing script slices d[299:519] and reads d[524].
(4) QUOTE SWEEP (chk117.py: outermost guillemet quotes, split at «…», parts of 6+ characters, whitespace-normalised, searched in the
sources: trunk RESULTS, GAPS, DECISIONS, DECISIONS-INDEX, TARGET.md, CLAUDE.md, LEAD-STATE, the SPEC file, R104 / R115 / R116 drafts;
at 727163f0 the packet, fixes, L-1, L-2, L-3, reachcheck.py / .out, xcheck.sh / .out, subdiv.py, check.sh, reach.pins; both referee
files at every commit of this round; C120-C129 and notes/CHECKER.md; the commit subjects cited; my outputs blk189.out, g9split117.out,
xcmp117.out, xcheck117.out, prem117.out, l3rel117.out, upd117L3.txt): title and body: 125 quotes, 129 parts, 0 not found; GAPS preamble and UPDATE: 1 quotes, 0 parts, 0 not found; preface: 198 quotes, 157 parts, 0 not found.
Stale grep in the title and body: «PENDING» 1 (the title fill «checker PENDING)»), «pending» 0, «not yet» 0, «NOT YET»
2 (both inside quotations of REFEREE's L-1 / L-2 verdicts, history), «will » 0, «awaiting» 0.
(5) LANDING SIMULATIONS (sim117.py, on in-memory copies of the local trunk's RESULTS 0ea36025 and GAPS 19da0f51; the entry block with
"checker PENDING)" filled plus one blank line inserted directly before «**Erratum E-1**»; GAPS l. 11's closing « |» replaced by « » +
the filled UPDATE + « |»). R116 stand-in: docs/agents/R116-draft.md ae0efb69b51c5a777c09b82d4f5cc167dfe9a0cc UPDATE sha1 c924a0e2fb94e32489a2263a9ddbf9cbf82e5993
(A) after R115: pure insertion True ; order True ; previous block byte-unchanged True ; RESULTS 13,681 -> 13,902 lines (+221) ; R117 at l. 13,072 - 13,291 blank 13,292 ; E-1 13,293 E-2 13,306 E-3 13,334 Dead ends 13,365 ; GAPS only l. 11: True ; "|" on l. 11 76 -> 76 ; «UPDATE 2026-» 50 -> 50 + «UPDATE 2099-» 1 ; R117 UPDATE last True
(B) after R116: pure insertion True ; order True ; previous block byte-unchanged True ; RESULTS 13,971 -> 14,192 lines (+221) ; R117 at l. 13,362 - 13,581 blank 13,582 ; E-1 13,583 E-2 13,596 E-3 13,624 Dead ends 13,655 ; GAPS only l. 11: True ; "|" on l. 11 76 -> 76 ; «UPDATE 2026-» 50 -> 50 + «UPDATE 2099-» 2 ; R117 UPDATE last True
(B) uses R116's second fill as committed in f7fcfccd; a later R116 fill moves its line numbers, not the shape.
(6) UPDATE: upd117.py, 19 controls (R97-R115, all landed) rebuilt byte for byte (True ×19), then R117 (G-U), cross-checked by a direct
build (True). With R-A..R-D the line would be f85a024b… and its UPDATE b4d74e09… (G-D).
(7) NOT RE-RUN: the referees' scripts (reach_replay.py, subdiv_replay.py, t3r_sim.py, r2reach.py, reachcheck_r2.py, bt_l2.py: their
reports read); gamma3.py's builder self-test (needs an L-RED tree); norm.py; the L-LOWER README cross-check of L(G); check.sh's other
blocks and scripts/verify.sh.

Addendum 2 (subagent, for the Lead; does not land; written 2026-11-07T09:05:04Z by date -u). (1) SECOND FILL on line L-4 (l-new
fdf01b8c, sha1 f85a024b…), to CHECKER C130 Add. 1. I edited docs/agents/R117-draft.md only; no merge, no commit and no push by me (a
Lead push.sh was running); the Lead commits this file. (2) TITLE l. 382 = "### R117 [refereed-only] " + L-4 without its newline + ",
CHECKER PASS (docs/checker/C130.md, checker PENDING)", checked by script (chk117b.py): equal, byte for byte (True); the only «### R»
heading of this file; 3,972 characters, 4,020 bytes, sha1 of the heading line without its newline
84d79ef5b7336b821def9587b15844dfdff22bcf; 65 «(» / 65 «)» (L-4's 64 and the fill's), depth never negative, 0 "|". (3) SHAPE. The entry
block is l. 382-625 (python slice d[381:625]), followed by a blank line; 0 "|" in it; one «PENDING», the title's fill «checker
PENDING)». The GAPS preamble is l. 627-631; the UPDATE is l. 632 (d[631]), one line, sha1 b4d74e094a30cba61017eeda4a0c33cb7a1db6f3
without newline and unfilled (= upd117L4.txt, = C130 §5's, True), 3,973 bytes, 63 «(» / 63 «)», 0 "|", one each of «<DATE>», «<HH:MM>»,
«<checker>». A landing script slices d[381:625] for the entry and reads d[631] for the UPDATE, with «R117», «C130», PREV = «R116»
(landed at 97d17f63) and the assertion that the last UPDATE on GAPS l. 11 is R116's «UPDATE 2026-11-07 07:42Z: RESULTS R116
(P-IDEAL-MOVES; CHECKER C129 9246878c)». (4) WHAT IS LEFT TO FILL: only the title's «checker PENDING)» and the UPDATE's three
placeholders, at landing. No referee item is open on this packet. (5) QUOTE SWEEP (chk117b.py: chk117.py's rule, outermost guillemet
quotes split at «…», parts of 6+ characters, whitespace-normalised; its sources plus the trunk files at 172af6ad, NOW, the packet files,
fixes, L-1 to L-4, reachcheck.py / .out, gamma3.py, xcheck.sh / .out, subdiv.py, check.sh and reach.pins at 727163f0 and fdf01b8c, both
referee files at every commit of this packet including 419cc268, d2b08049 and d4838991, C120-C129 and C130 (126f9772), notes/CHECKER.md,
the commit subjects cited, the first fill's outputs and mine): title and body 166 quotes, 169 parts, 0 not found, also with no
docs/agents draft as a source; GAPS preamble and UPDATE 3 quotes, 2 parts, 0 not found; SECOND FILL paragraph 38 quotes, 32 parts, 0 not
found (no draft as a source); the preface 237 quotes, 190 parts, 0 not found; this Addendum and the whole file: 0 not found (same script
on the final file). Line-precise: 20 of 20 (source, cited lines, quote) triples of this fill found inside the cited lines (REFEREE l.
211, 218-219, 221, 227-228, 229, 236-237, 241, 242-243, 246-247; REFEREE-2 l. 180, 189, 196-197 twice; fixes l. 26-28, 73, 73-74, 75-76,
76-77; C130 l. 16, 117). (6) STALE STATUS (chk117b.py) in the title and body: «PENDING» 1 (the title's fill «checker PENDING)»),
«pending» 0, «not yet» 0, «Not yet» 0, «NOT YET» 2 (both inside quotations of REFEREE's L-1 and L-2 verdicts in Signatures, history),
«CANDIDATE» / «candidate» 0, «will » 0, «awaiting» 0, «to come» 0, «not landed» 0; GAPS preamble and UPDATE: all 0; SECOND FILL
paragraph: all 0; line 1: «NOT LANDED» 1 (R117 is not landed; as R116's draft). «L-3» in the title, the body, the GAPS preamble and the
UPDATE: 23 times, every one history (fixes entry 2 and its line L-3 in Object and Fixes, the line history, L-3's verdicts at both
referees in Object and Signatures, the L-3 → L-4 step in Object and Fixes, the pins list «line L-3 adfbb3b8» in Data, the lane commit
727163f0 in Signatures); «RESULTS line is L-3», «title is L-3», «line (L-3», «(L-3, by script)», «L-3's parentheses» 0 times; C130's old
strings of R1-R4 in the title, the body and the UPDATE: 0 times each (R2's old string occurs inside R2's new string only). (7) WORD DIFF
f652c0d3 → this file (wd117b.py, difflib on lines, then on whitespace tokens, Addendum 2 left out): 25 line regions, 95 token hunks (113
tokens out, 3,141 in), every region in the list of changes of the SECOND FILL paragraph. (8) LANDING SIMULATION (sim117b.py: sim117.py's
land(), unchanged, on in-memory copies of the local trunk 172af6ad's RESULTS 8353e283… and GAPS 01edd372…; R115 and R116 landed, so one
case, after R116): pure insertion of 245 lines (the entry block with "checker PENDING)" filled, plus one blank line) directly before
«**Erratum E-1**», after R116's landed block: True; R116's block byte-unchanged (from l. 13,072) and every line after the insertion
byte-unchanged (Errata, Note E-3, Dead ends with DE37): True; RESULTS 14,004 → 14,249 lines; R117 at l. 13,362-13,605, blank l. 13,606,
«**Erratum E-1**» to l. 13,607, Erratum E-2 13,620, Note E-3 13,648, Dead ends 13,679; order R110-R116, R117, E-1, E-2, E-3, Dead ends:
True. GAPS: only l. 11 changes, its closing " |" replaced by " " + the filled UPDATE + " |": True; "|" on l. 11 76 → 76; «UPDATE 2026-»
51 → 51 plus one head with the simulation year 2099, after R116's and the last: True; 23 → 23 lines. Fill values used only for the
simulation: <DATE> 2099-01-03, <HH:MM> 00:00, <checker> 0000000. (9) FIRST-FILL RECORD (rec117b.py): f652c0d3's l. 2-299 (FIRST FILL to
(14) and the blank line) = this file's l. 84-381, directly before the title (True); f652c0d3's Addendum (1)-(7), l. 527-552 = this
file's l. 634-659 (True). (10) NOT VERIFIED: the referees' tools (bt_l4.py, REFEREE's byte-test script) not re-run (their files read; my
l4rel117.py makes the same test); scripts/verify.sh and the full check.sh not run (blocks «BOX 189 REACH» and «P-N5-REACH» only);
g9split117.py and xcmp117.py not re-run (box189's tools and outputs are byte-equal at 727163f0 and fdf01b8c, and L-4's figures are
L-3's: R1-R4 change wording and the names of counters, not counts); C130's own scripts not re-run. (11) NOTES for the CHECKER, no
verdict affected: D-6 REFEREE-2 Addendum 3 l. 176 says its objects are «equal to the Lead's relay 08:26Z», a stamp later than its commit
d2b08049 (08:23:41Z); its heading stamp «08:3xZ» was corrected to «08:2xZ» at d4838991 (08:23:54Z). D-7 fixes entry 3's heading
«(2026-11-07 from 07:3xZ by date -u; L-NEW successor 59; Lead relay 07:31Z of CHECKER C130, R117)»: C130's commit 126f9772 is 07:29:13Z;
fdf01b8c is 07:57:34Z; consistent. D-8 The referees back R1's second half («0 of them equal to R104's stated start off the movers»)
through different counters: REFEREE by NR-CORE and arithmetic (§C add. 2 l. 226-228), REFEREE-2 by NR-STD directly (Addendum 3 l.
183-187); reachcheck.out has both at 0, so either reading holds. D-9 R2's new string contains its old string, so «Corollary
REAL-IDEAL-S3 no separate DATA,» still occurs once in L-4, inside the new list. D-10 DE37 landed at 172af6ad after R116, appended after
DE36 at the end of RESULTS, with no GAPS change; R117's place (after R116, before «**Erratum E-1**») and its UPDATE are unaffected
(sim117b.py). D-11 L-4 names the vertex K3 three times and the lemma K3 never; the XC-3 NOTE says so. Scratch:
/tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad/r117b/ (tools/l4rel117.py, l4rel117.out;
check_fdf01b8c.sh, archfdf/ with runblk189b.sh, blk189b.out, blk.start, blk.end, blk.rc; xcheckb.out, xc.start, xc.end, xc.rc;
tools/upd117b.py, upd117b.out, upd117L4.txt; tools/prem117b.py, prem117b.out; tools/edit117b.py, secondfill.txt, addendum2.raw,
filltime.txt; tools/chk117b.py, chk_p1.out, chk_final.out; tools/sim117b.py, sim_p1.out, sim_final.out; tools/rec117b.py, rec117b.out;
tools/wd117b.py, wd117b.out; R117-draft-f652c0d3.md, R117-p1.md, R117-draft.md).
