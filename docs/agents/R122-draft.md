# Draft RESULTS R122 (Lead; first fill 2026-11-08T05:11:16Z by date -u (subagent) on P-ACYC line L-3, docs/si/P-ACYC-line-L3.txt, l-si ff9b1639, sha1 03453361fead881493e2d2786b869f1c63158c4c (draft sha1 0fa23b17); SECOND FILL 2026-11-08T06:50:03Z by date -u (subagent) on P-ACYC line L-4, docs/si/P-ACYC-line-L4.txt, l-si 0bc6f028, sha1 85bb221f19ca457655c954f570552bc0f4d8095d (draft sha1 2cd7cfd0, CHECKER C136 b2fe3440: FAIL E-1, E-2); THIRD FILL 2026-11-08T17:20:12Z by date -u (subagent) on P-ACYC line L-5, docs/si/P-ACYC-line-L5.txt, l-si 358ede16, sha1 7a84e0944b0f33ce4d569604bec41d6e9236d82f) — to CHECKER C136 Add. 1 — NOT LANDED; goes after R121 (LANDED at 59dacf22), before Erratum E-1 — LANDED in RESULTS 2026-11-08 20:27Z (CHECKER C136 3e7fe04e PASS), after R121, before Erratum E-1
THIRD FILL (2026-11-08T17:20:12Z by date -u, subagent; for CHECKER C136 Add. 1). Read at the origin heads of one fetch at
2026-11-08T17:14:25Z-17:14:26Z (date -u before and after the fetch; git fetch of claude/l-si, claude/referee, claude/referee-2 and
claude/checker, not of the trunk, whose push by the Lead was running; rc 0; I merged, committed and pushed nothing, wrote nothing into the
repository and built this file in the scratchpad by fill3.py): l-si 358ede16 (358ede16eba893e13d9b3229db4291ae7d24d2a4,
2026-11-08T15:55:24Z, «L-SI P-ACYC fixes entry 4 + line L-5 (CHECKER C136 E-1, E-2: R1-R3, line-only; L-5 sha1 7a84e094 = CHECKER's)»,
L-SI successor 46, the branch head and the commit of record; git diff --name-only 0bc6f028 358ede16 on the packet, the fixes file, the
line files and experiments/si/box81 names only docs/si/P-ACYC-fixes.md, docs/si/P-ACYC-line-L5.txt, experiments/si/box81/check81.sh and
experiments/si/box81/fix4/ (check_fix4.sh, mkL5.py, mkfix4.py); the packet and L-1 to L-4 are byte-equal at both). referee ae980555
(ae9805556a1feee09de9a95d2043607d591374bf, 2026-11-08T16:44:42Z, «REFEREE successor 30: R-P-ACYC §F: R1 proof-use sentence corrected to
step (4) at every gate; pacyc81.py line numbers», the branch head): docs/referee/R-P-ACYC.md there 411 lines, 33,314 bytes, sha1
5b8d737583b5267f6ac27c8882a105f91352c726; its l. 1-378 = 055758ba's file, by cmp; §F (l. 380-411) was first committed at 5b2aa604
(5b2aa6044357856caefdc8f5ed165b7629ddc00f, 2026-11-08T16:44:19Z, «REFEREE successor 30: R-P-ACYC §F (L-5 7a84e094 MATCHES; R1 = packet §1
l. 69 sense; R2/R3 = pacyc81.py set; entry 4 line-only)»; the file 410 lines, 33,146 bytes, sha1
da3e5d143c13811388bd267cc4f0ff804c39180a), and ae980555 changes only R1's proof-use sentence (two lines become three, l. 391-393 at
ae980555) and the loop's line numbers in the R2 / R3 reading (l. 399: «(l. 27-30)» becomes «(l. 24-29)»), git diff; the verdict line is
the same text at both. referee-2 c1e71a25 (c1e71a25596ff01554a1bd7390d7f8b0380a97d6, 2026-11-08T16:43:45Z, «REFEREE-2 successor 35: P-ACYC
L-5 MATCHES (Add. 5: R1-R3 byte test, R1 pointwise sense, R2/R3 set = states 0..T3)», the branch head): docs/referee-2/R2-P-ACYC.md there
427 lines, 39,268 bytes, sha1 f4475c670a865ff0f4b529ba0ff43f15aca684bf; its first 37,109 bytes = 79430e80's file, by cmp; Addendum 5 is l.
408-427, with R2-P-ACYC/bt_l5.py and bt_l5.out. checker dcdecd2a (dcdecd2a9b977d11db7a0dbc84f016961b09c279, 2026-11-08T15:43:57Z, «CHECKER
C135: CI line (run 7091 green on 59dacf22); close pending only the F-2 merge of claude/checker», the branch head): docs/checker/C136.md
there is b2fe3440's file (b2fe34407619498954471c019228282c35bc03a5, 2026-11-08T15:18:43Z; 103 lines, 10,011 bytes, sha1
01e3fe8454d8d0cd2faf964085a8f619085f6f57; git diff --quiet), with no Add. 1. 358ede16, b2fe3440, dcdecd2a, 0bc6f028, 055758ba and 79430e80
are ancestors of the local trunk a4a777de (git merge-base --is-ancestor); 5b2aa604, ae980555 and c1e71a25 are NOT ancestors of a4a777de or
of the trunk's remote-tracking ref d35ce1ec. claude/l-si 358ede16 and claude/checker dcdecd2a are merged at a4a777de (91a80111, 7cc51436).
The Lead merges claude/referee (ae980555 or later) and claude/referee-2 (c1e71a25 or later) before landing.
Trunk: local HEAD a4a777de (a4a777de95c128e0f3799cf6d9a1899554bc2e5d, 2026-11-08T17:00:41Z, «Lead: log 16:03Z-17:00Z (L-COMP 14 created;
BOX 198 routed + SURVIVES at L-RED; P-ACYC L-5 to referees); NOW + LANE-RESTART rows for L-COMP 14», being pushed by the Lead during this
fill); it carries the merges 91a80111 («Lead: merge claude/l-si into trunk (P-ACYC fixes entry 4 + L-5 358ede16, premise of R122 third
fill)», its parent) and 7cc51436 («Lead: merge claude/checker into trunk (C135 Add. 3 + CI line; F-2: a9bf46bb ancestry)», the parent of
91a80111). The trunk's remote-tracking ref, not re-fetched by me, is d35ce1ec. docs/agents/R122-draft.md at a4a777de is the second fill,
sha1 2cd7cfd03c58c01653d665c657a2ff71826e2df3 (committed at a1decf9a, 2026-11-08T07:30:27Z; fill3.py asserts it). R121 LANDED at 59dacf22
(2026-11-08T14:06:41Z): RESULTS R121 l. 14320-14742, GAPS l. 11 «UPDATE 2026-11-08 14:06Z: RESULTS R121 (P-N5-ASC; CHECKER C135
a9bf46bb)». RESULTS at a4a777de: sha1 04a444ee05569591d3b44c981e35af1b33cf37b5, 15,386 lines, = 59dacf22's (git diff --quiet), = RESULTS
66e7119615efa5a0bb25b898e32b5b371c55c122 (the file both referees checked their premise quotes against) with R121's block and its blank
line inserted at l. 14320-14743 and nothing else (by script); «**Erratum E-1**» l. 14744, «**Erratum E-2**» l. 14757, «**Note E-3**» l.
14785, «## Dead ends (kept;» l. 14816. GAPS at a4a777de: sha1 a47210669a534c5ba9c1dbf2be2919080cfcfe68, 23 lines, l. 11 76 "|", 56 «UPDATE
2026-», the last R121's. «R122», «C136», «P-ACYC», «BETA-ACYC», «LAMBDA-CONST», «ACYC-LIN» and «ACYC-XI» occur 0 times in RESULTS and in
GAPS (by script).
New sources (read in full): docs/checker/C136.md at b2fe3440; fixes entry 4 (docs/si/P-ACYC-fixes.md l. 138-163 at 358ede16; the file 163
lines, 15,987 bytes, sha1 165355113b7b12c40856ecc2c4a06ef296609fdd; its first 13,468 bytes = 0bc6f028's file, by cmp); L-5 (358ede16, the
file's only commit); experiments/si/box81/fix4/mkL5.py, mkfix4.py and check_fix4.sh, and check81.sh's new line l. 44 «bash
fix4/check_fix4.sh»; experiments/si/box81/pacyc81.py l. 1-40 at 358ede16 (the counted set, for R2 and R3); REFEREE §F (l. 380-411 at
ae980555) and its scratch/acyc_l5.py and acyc_logs/l5test.out at 5b2aa604 (read, not re-run); REFEREE-2 Addendum 5 (l. 408-427 at
c1e71a25) and its R2-P-ACYC/bt_l5.py and bt_l5.out (read, not re-run); docs/agents/LEAD-STATE.md at a4a777de l. 2896-2898 (15:43Z-15:55Z:
C136 FAIL; R1-R3 routed to L-SI 46 at 15:52Z) and l. 2903 (16:42Z: L-5 routed to REFEREE 30 and REFEREE-2 35).
WHAT CHANGED SINCE THE SECOND FILL. CHECKER C136 (b2fe3440) FAILED the second fill (draft 2cd7cfd0 at trunk 59dacf22): «Verdict: FAIL
(E-1, E-2; one L-5 with three replacements, §5)» (l. 16), «No statement, proof or DATA figure changes.» (l. 18). E-1 is the second fill's
G-4 (REFEREE-2's N-1), ruled REQUIRED: «By the rule that closed C135 (a term that carries a hypothesis of a signed clause must be stated
in the line), this is a FAIL.» (l. 27); the second fill's optional R-N does not fix it («R-N says that σ̄ is pointwise optimal, but the
lemma quantifies over EVERY optimal counterstrategy, not over σ̄.», l. 28-29), so R-N is not taken and R1 defines the word. E-2 is new, a
DATA set: «pacyc81.py counts on states 0..k1−1 only (its docstring l. 4; l. 28 breaks at the first fallback).» (l. 33), «The line drops
it.» (l. 35), «Read on the whole run, the zeros are FALSE.» (l. 36); R2 and R3 state the set. C136 ruled the second fill's other notes:
N-S «no action» (l. 47; «R-S not taken.», l. 48), G-2 «no action» (l. 50), G-U «R118's procedure applies, as in C135.» (l. 52), premises
landed (l. 56-58). L-5 = L-4 + R1 + R2 + R3 (fixes entry 4, L-SI successor 46; F-14 = R1, F-15 = R2 + R3), sha1 7a84e094… and 3,321 bytes,
as C136 §5 gave (l. 90-91). Both referees MATCH L-5: REFEREE successor 30, «Verdict: fixes entry 4 CORRECT. **Line L-5 MATCHES** (L-4 +
exactly R1-R3). Statements as signed (§0 and §C-§E).» (§F l. 410 at ae980555); REFEREE-2 successor 35, «(4) Verdict: **L-5 MATCHES** (byte
test, and in meaning). Statement verdicts unchanged.» (Add. 5 l. 427 at c1e71a25). Both read entry 4 as line-only (REFEREE §F l. 407-409;
REFEREE-2 Add. 5 l. 426). The UPDATE is the second fill's with R1-R3 applied, 79319350… as C136 §5 gave (l. 92). C136's instructions for
this fill («Third fill: the title from L-5; the UPDATE as above; both referees' L-5 verdicts.», l. 93) are met below; «Merge claude/l-si.»
(l. 94) is done at a4a777de (91a80111).
Checks run at this fill (scratch /tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad/r122c;
nothing written into the repository). (a) l5rel122c.py: R1, R2 and R3 parsed from C136 l. 84-89 (wrapped lines joined with one space) =
fixes entry 4's F-14 and F-15 strings (l. 151-158) = fix4/mkL5.py's tuples (True ×3); each old string once in L-4 and 0 times in L-5, each
new string 0 times in L-4 and once in L-5; L-4 + R1 + R2 + R3 = L-5 (True). L-5 = 7a84e0944b0f33ce4d569604bec41d6e9236d82f, 3,321 bytes,
one line with its newline, 3,261 characters, 554 tokens, 43 «(» / 43 «)», depth never negative, final depth 0, 0 "|", one « — »,
«gauntlet» 0, «not a step-4 pass» once, «referee-originated» once, «R57 (b)» once; token diff L-4 → L-5 three hunks (4 tokens out, 46 in),
the three replacements. fix4/mkL5.py re-run from the archive of 358ede16: rc 0, output = L-5. The packet (0e9edcfd…) and L-1 to L-4 at
358ede16 = at 0bc6f028 (True). (b) check81.sh from a git archive of 358ede16 (experiments, docs, scripts), 2026-11-08T17:17:38Z-17:19:44Z
by date -u, rc 0, output «P-ACYC fix1 checks: PASS», «P-ACYC fix2 checks: PASS», «P-ACYC fix3 checks: PASS», «P-ACYC fix4 checks: PASS»,
«box 81 checks: PASS» (it checks the pins, re-runs every frozen output of box 81, rebuilds L-2 to L-5 and the four fixes entries and
compares them byte for byte, and checks L-5's sha1 against C136's). (c) upd122c.py: the second fill's UPDATE d[728]
(425d10fe5ca0223568b5fb2f29bea4858307dc43, the sha1 of the line without newline) with R1, R2, R3 applied, each old string once in it: sha1
793193506cd6e4ca67ebb88235a75f70b72f7808 without newline (= C136 §5's, True), 3,349 bytes, 3,291 characters, 553 tokens, 43 «(» / 43 «)»,
0 "|", one each of the three fill tokens, «2026-11-07» 0 times, « — » 0 times; cross-checked by a standalone re-implementation of
run122()'s direct build (R118's procedure): on L-4 it gives d[728] (True, the control), on L-5 the same 79319350… (True). Token diff L-5 →
UPDATE: 11 hunks, 51 tokens out, 50 in, the 11 hunks of the second fill and of C136's G-U reading. On GAPS l. 11 at a4a777de, R121's
UPDATE is the last (True); R122's filled UPDATE appended after it keeps 76 "|", R122's last, the prefix byte-unchanged (True). (d)
chk122c.py (title, block, UPDATE, pipes, the fill token, parentheses, stale grep, quote sweep), lp122c.py (line-precise quotes new at this
fill), sim122c.py (landing simulation on a4a777de), rec122c.py (the kept sections byte-unchanged) and hex122c.py (every hex id new at this
fill is a git object or a sha1 measured at this fill): Addendum 3.
NOTES at this fill (for CHECKER; no line change proposed):
- N-C, R1'S CITATION (both referees' notes, no change asked). REFEREE §F: «Note (no change asked): this cites the sense, not the premise
  that gives IDEAL-CYC's σ̄ (successor 28's ruling: R118 (b) + R21 (a)); the clause defines a word, so the citation suffices.» (l.
  396-397). REFEREE-2 Add. 5: «Note (optional, no change asked): for IDEAL-CYC's σ̄, a defined object in R118, existence of a pointwise
  optimum is VJ00 §4 / Friedmann §3 (R118 [VJ]) rather than R57 (b). R1 defines the word, so this is not an error.» (l. 421-422). The
  entry's Honest limits (ix) records it. Premise route of R1's new label: «### R57» is l. 2893 of RESULTS at a4a777de (landed), «R57 (b)»
  occurs 36 times there, and [1E-N3]'s pointwise form is R104's title (l. 9864: «S1's σ̄, and τ̄ on the dual game, are pointwise optima»);
  the R-labels of L-5 are R104, R117, R118, R15 and R57, all landed (by script).
- N-E, THE EDGE OF R2 / R3'S SET (REFEREE's note, no change asked): «if a run had no fallback within cap = 10^4, pacyc81.py would count
  all states and report k1 None; every pinned genome has k1 set (C136: k1 equals pacyc81_towers.out), so the clause is exact on the pinned
  sets.» (§F l. 405-406). The line's «genomes with no fallback 0» says that no pinned genome is in that case.
- N-W, THE WHOLE-RUN COUNTS (new entry text, for CHECKER's ruling). Honest limits (v) of the entry now records C136's measured whole-run
  counts on the four towers (C136 §3 l. 36-45: σ̄ off the β-face 94, 121, 138, 150; non-standard states 3 each), the reason for R2 and R3.
  They are CHECKER's data from an instrumented copy of pacyc81.py outside the archive, not lane or referee data, and the entry makes no
  statement about the states after the first fallback. CHECKER may rule whether the entry keeps that sentence; if not, Honest limits (v)
  returns to the second fill's text and nothing else changes.
- N-S AT L-5. The source note still names «fixes entries 1-2» and «L-SI successors 43-44»; entries 3 and 4 (successors 45 and 46) are
  line-only. C136 ruled N-S «no action» for entry 3 and for «the line-only entry R1-R3» (l. 47-48); REFEREE §F: «So the source note need
  not name it (C134 N-S, as CHECKER ruled in C136); not L41's case.» (l. 408-409); REFEREE-2 Add. 5: «(3) Fixes entry 4 is line-only.» (l.
  426). Honest limits (viii) records it.
- D-10, STAMPS (history, no verdict affected). Fixes entry 4's heading «routed by the Lead 15:52Z» (l. 138) is LEAD-STATE l. 2897's stamp;
  358ede16 was committed at 15:55:24Z. LEAD-STATE l. 2903 logs 358ede16 and the routing of L-5 to both referees under «16:42Z».
  REFEREE-2's Add. 5 heading reads «16:43Z» (commit 16:43:45Z); REFEREE's §F heading reads «16:44Z» (commits 16:44:19Z and 16:44:42Z):
  each stamp at or before its commit.
- D-11, REFEREE §F's FIRST WORDING (history). At 5b2aa604 §F said that BETA-ACYC's comparison needs the inequality at the gate and at both
  faces' successors; ae980555 corrects it to the gate only («(Corrected at writing from a first wording that claimed the faces'
  successors; the proof's step (4) is at g only.)», l. 393). The verdict is the same at both commits (5b2aa604 l. 409, ae980555 l. 410).
  The entry cites ae980555's file.
Changes at this fill, and nothing else: line 1 (the header: the second fill's draft sha1 and C136 verdict, the THIRD FILL clause, and R121
now LANDED); this section (new); the title (L-5: R1, R2, R3); in the entry: Object (successors 43-46; the packet at 358ede16; four fixes
entries; L-5 the line of record; line history L-1 to L-5; the L-5 rounds, REFEREE §F and REFEREE-2 Addendum 5), Claims signed (the L-5
rounds; entry 4 changes three line strings only), Setting and (b) (the pointwise sense, now in the line), The RESULTS line (L-5; R1's
premise clause; the Γ3 set), Premise (R57 (b) and [1E-N3] for R1; RESULTS at a4a777de), L41 and L43 (L-5's scope tail), Fixes (header,
entry-4 bullet, closing bullet), Honest limits (v), (viii) and (ix), Data (358ede16; the re-run of this fill; REFEREE's check_fix4.sh run
and C136's re-run), Signatures (§F, Addendum 5, successor 46's commit), INDEPENDENCE (L-5's strings and byte tests), TARGET.md diff (L-5);
the GAPS preamble and the UPDATE (= the second fill's with R1-R3); Addendum 3 (new, at the end). The SECOND FILL section (from "SECOND
FILL (2026-11-08T06:50:03Z" to its last line), the FIRST FILL record, the first fill's Addendum and Addendum 2 are kept byte-unchanged
(rec122c.py): where they call L-4 or L-3 the title or the line of record, raise G-4 (N-1), N-S, G-2 or G-U for CHECKER, propose R-N or
R-S, or give their line numbers, counts, slices and UPDATE sha1s (a9274893…, 425d10fe…), they describe drafts 0fa23b17 and 2cd7cfd0; C136
ruled at 15:18Z, and the entry block now follows L-5.
SECOND FILL (2026-11-08T06:50:03Z by date -u, subagent; for CHECKER C136). Read at the origin heads of one fetch at
2026-11-08T06:39:15Z-06:39:16Z by date -u (git fetch of claude/l-si, claude/referee, claude/referee-2, claude/checker,
claude/vibrant-johnson-nxvvxo; rc 0; I merged, committed and pushed nothing and edited docs/agents/R122-draft.md only): l-si 0bc6f028
(0bc6f0285c6fc042ebd446883b817fb38960cb08, 2026-11-08T05:54:32Z, «L-SI P-ACYC fixes entry 3 + line L-4 (Lead rulings 05:13Z: G-7 = L41
referee-originated w* = K1 step; G-1 source names fixes entries 1-2 and authors); fix3/ by script, wired in check81.sh», L-SI successor
45, the branch head and the commit of record). Between ff9b1639 and 0bc6f028 the lane committed 27ef5506 (handover check), the trunk merge
70eeefd8 and box 85 work (2860cd16, ee0dc99c, ede6acfb); git diff ff9b1639 ede6acfb names no P-ACYC file and nothing under
experiments/si/box81, and git diff ede6acfb 0bc6f028 names only docs/si/P-ACYC-fixes.md, docs/si/P-ACYC-line-L4.txt,
experiments/si/box81/check81.sh and experiments/si/box81/fix3/ (check_fix3.sh, mkL4.py, mkfix3.py). referee e4cb208a
(e4cb208abe3c2bc5519fe87266cc71dec4458dab, 2026-11-08T06:09:15Z, «REFEREE 29: R-P-N5-END first review (all SIGN, END-T3 conditional;
EXACT-L tie-break note; line requirements LN-1..LN-8); notebook», the branch head): docs/referee/R-P-ACYC.md there is the file of d4423d6d
(348 lines, 26,849 bytes, sha1 b09be901fb54f1e0f27075817a53ece4864e5b5b; git log names no later commit on it), with no §E at this fetch
and at the second (06:52:17Z). referee-2 11a7a911 (11a7a911a5b988939d58b943148710383542c29d, 2026-11-08T06:14:50Z, «REFEREE-2
R2-P-N5-QUIET Addendum 1: comparison with REFEREE 28», the branch head): docs/referee-2/R2-P-ACYC.md there is the file of e1878470 (374
lines, 34,017 bytes, sha1 6cdb50101bbe8526502f973d3ab55faa7e71055b; git log names no later commit on it); Addendum 4 reached origin only
at the fourth fetch (below). At the third fetch (2026-11-08T06:54:04Z by date -u, the same five branches) the referee head is 055758ba
(055758ba570fa9c9a08f92cd73aea00a1c4ff6c3, 2026-11-08T06:31:48Z, «REFEREE 29: R-P-N5-ASC §F add. 1 (N-I: R-I optional; N-A: R-A required,
predicted L-5 shas); R-P-ACYC §E (L-4 85bb221f MATCHES)»), which adds §E to docs/referee/R-P-ACYC.md (l. 349-378; the file 378 lines,
29,613 bytes, sha1 1b6f11605c6505517632022aeb39003196675ef6; its l. 1-348 = d4423d6d's file, by cmp): REFEREE successor 29's byte test of
L-4, own scratch/acyc_l4.py, «L-3 + R-G + R-B in order is byte-equal to L-4.» (l. 357), R-G and R-B read in meaning (l. 360-376),
«Verdict: L-4 MATCHES (L-3 + exactly R-G and R-B; both CORRECT in meaning). All statements of P-ACYC stay SIGN (ACYC-XI
PROVED-CONDITIONAL, as before).» (l. 377-378); the entry cites it in Object, Claims signed, L41 and L43, Honest limits (viii) and
Signatures. l-si, referee-2 and checker are unchanged at the third fetch; origin trunk is 616941eb. At the fourth fetch
(2026-11-08T07:02:54Z-07:02:55Z by date -u, the same five branches; rc 0) the referee-2 head is 79430e80
(79430e80429c5aaa6b645f2bf0db13da65162275, 2026-11-08T06:38:24Z, «REFEREE-2 R2-P-ACYC Addendum 4: L-4 = L-3 + R-G + R-B (MATCHES); G-1 /
W-1 citation and unique-optimum wording checked»), which adds Addendum 4 to docs/referee-2/R2-P-ACYC.md (l. 376-406; the file 406 lines,
37,109 bytes, sha1 51b5354f04206dfbb8b3c1bd41ab5605e69a5b48; its l. 1-374 = e1878470's file, by cmp): REFEREE-2 successor 33's byte test
of L-4, own bt_l4.py, «The rebuild L-3 + R-G + R-B is 85bb221f…, 3,080 B, which is L-4 byte for byte, so nothing else changed.» (l. 382),
F-12 and F-13 read in meaning (l. 384-402), «**Verdict: L-4 MATCHES** (Opus 5.5, D1). Statement verdicts unchanged: all SIGN (ACYC-XI
PROVED-CONDITIONAL on R118 (k), (l), as before).» (l. 405-406); the entry cites it where it cites REFEREE's §E. l-si 0bc6f028, referee
055758ba, checker fa8add12 and origin trunk 616941eb are unchanged at the fourth fetch. checker fa8add12 (unchanged since the first fill;
docs/checker/ ends at C135.md; C136 does not exist). 0bc6f028, ff9b1639, d4423d6d, e1878470, e4cb208a, 055758ba, 11a7a911, 79430e80 and
fa8add12 are NOT ancestors of the local trunk 616941eb or of origin trunk c9591e35 (git merge-base --is-ancestor). The Lead merges
claude/l-si (0bc6f028 or later), claude/referee (055758ba or later) and claude/referee-2 (79430e80 or later) before landing.
Trunk: origin trunk c9591e35 (c9591e35ac3aca556e718468e701ab91c84eba4c, 2026-11-08T05:40:39Z, «Lead: R122 first fill (P-ACYC over L-3; G-7
L41 + G-1 ruled, L-4 routed)», which commits the first fill, sha1 0fa23b17…); local HEAD 616941eb
(616941ebdb0ebd7398d66c2b5fe2112db73945a6, 2026-11-08T06:17:27Z, «Lead: R121 second fill on L-4 (823d15c3;», one commit ahead of origin
trunk at this fetch and origin trunk at the third; it changes docs/NOW.md, docs/agents/LANE-RESTART.md, docs/agents/LEAD-STATE.md and
docs/agents/R121-draft.md, the second fill, sha1 823d15c3ac27a04dd5f7e8e50bdbe889b1332cc2; the working tree was clean at the fetch; the
Lead has since committed 36c183f8 locally (36c183f87cc8ca27ce09514fbda56da2a1daaacf, «Lead: L-LOWER 10 roster/restart row;», changing
docs/NOW.md, docs/agents/LANE-RESTART.md and docs/agents/LEAD-STATE.md only). RESULTS at c9591e35, 616941eb and 36c183f8 (git diff
--quiet): sha1 66e7119615efa5a0bb25b898e32b5b371c55c122 (= RESULTS at 37a4855e, the trunk both referees checked their premise quotes
against), 14,962 lines; GAPS at all three: sha1 2a41c7654d4e9dedee7abc8591dfb792633bc2c9, 23 lines, l. 11 76 "|", 55 «UPDATE 2026-», the
last R120's. «R121», «R122», «C135», «C136», «P-ACYC», «BETA-ACYC», «LAMBDA-CONST», «ACYC-LIN» and «ACYC-XI» occur 0 times in RESULTS and
in GAPS (by script). Nothing landed on trunk since the first fill.
New sources: fixes entry 3 (docs/si/P-ACYC-fixes.md l. 116-136 at 0bc6f028, read in full; the file 136 lines, 13,468 bytes, sha1
ae03871f8eb064a5a4c8d99063dbef8e88264a73); L-4 (0bc6f028, the file's only commit); experiments/si/box81/fix3/mkL4.py, mkfix3.py and
check_fix3.sh (read in full) and check81.sh's new line «bash fix3/check_fix3.sh»; docs/agents/LEAD-STATE.md l. 2754 (the Lead's rulings of
05:13Z: «Lead rulings: G-7 L41 APPLIES (w* = K1 required referee repair, both SIGN WITH GAP; R119 precedent) -> R-G; G-7 (ii) AC-6 NOT
L41; G-1 source note -> R-B; G-4/G-U/G-2/G-9 to CHECKER; R-N not taken.»); DECISIONS l. 355-358 (L41: «both signatures and the joint gap
map are quoted in the RESULTS entry, whose scope tail says the proof is referee-originated»); CHECKER C135 l. 15-44 (E-1, E-2, the N-S
rule, G-U); REFEREE l. 1-14, 118-137, 295-301, 326-331 and REFEREE-2 l. 1-21, 84-102, 260, 312-316, 349-352, 372-374 (re-read for L41 and
L43).
Checks run at this fill (scratch /tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad/r122b;
nothing written into the repository but this file). (a) l4rel122b.py: F-12 and F-13 parsed from fixes entry 3 (l. 126-133, wrapped lines
joined with one space) = mkL4.py's RG and RB = the first fill's R-G and R-B (True ×4); each old string once in the running line and 0
times in L-4, each new string 0 times before and once in L-4; L-3 + F-12 then F-13 = L-4 (True; the other order too); L-4 =
85bb221f19ca457655c954f570552bc0f4d8095d, 3,080 bytes, one line with its newline, 3,026 characters, 512 tokens, 41 «(» / 41 «)», depth
never negative, final depth 0, 0 "|", one « — », no guillemet, «gauntlet» 0, «not a step-4 pass» once, «referee-originated» once; token
diff L-3 → L-4 three hunks (3 tokens out, 49 in), all inside F-12 and F-13. fix3/mkL4.py re-run from the archive of 0bc6f028: rc 0, output
cmp-equal to L-4. The packet, L-1, L-2 and L-3 at 0bc6f028 are the first fill's (sha1 0e9edcfd…, bb12deec…, 3a3096a4…, 03453361…); the
fixes file's first 11,487 bytes at 0bc6f028 = the file at ff9b1639 (cmp). (b) check81.sh from a git archive of 0bc6f028 (experiments,
docs, scripts), 2026-11-08T06:41:07Z-06:43:18Z by date -u, rc 0, output «P-ACYC fix1 checks: PASS», «P-ACYC fix2 checks: PASS», «P-ACYC
fix3 checks: PASS», «box 81 checks: PASS» (it checks the pins, re-runs every frozen output of box 81, rebuilds L-2, L-3, L-4 and the three
fixes entries and compares them byte for byte). (c) upd122b.py: the first fill's builder r122/tools/upd122.py exec'd with three changes
(its R121-draft read pointed at the first-fill R121 draft committed at c9591e35, sha1 04323afb…; its two file writes not executed):
controls R97-R116 rebuilt from their lines and compared with GAPS l. 11 byte for byte, True ×20; R117, R118, R119 and R120 as landed, True
×4; all controls True ×24, the last UPDATE on l. 11 R120's; R121 controls: run121 on P-N5-ASC L-2 = the first-fill R121 draft's d[491]
(6635b14e…, True), with C135 §5's R1-R4 = f545cba7… (True), and on L-4 = R121-draft.md d[715] in the working tree (the second fill,
823d15c3…; d3a42330…, True); the first fill's L-3 UPDATE reproduced (a92748935ead9054b1029880e863e4c97268e9bd, = d[528] of the first-fill
draft at c9591e35, True). run122() unchanged on L-4: sha1 425d10fe5ca0223568b5fb2f29bea4858307dc43 (no newline, unfilled), 3,108 bytes,
3,056 characters, 511 tokens, 41 «(» / 41 «)», 0 "|", one each of «<DATE>», «<HH:MM>», «<checker>», «2026-11-07» 0 times, « — » 0 times; =
the direct build (True); = the first fill's prediction (its Addendum (8), True); = a9274893… with F-13 applied and F-12's sentence
inserted after «(no bound on R for Ξ-cyclic genomes)», each old string once (True). Token diff L-4 → UPDATE: 11 hunks, 51 tokens out, 50
in, the 11 hunks of the L-3 UPDATE (the head; the four labels behind their clauses, the fourth whole; « (2026-11-07) —» → «:»; the drop
words; «43-44)» → «43-44). G-N5-TIME stays open.»). Appended after R121's L-4 UPDATE (simulated) after R120's, or directly after R120's,
on GAPS l. 11 it keeps 76 "|", R122's last, the prefix byte-unchanged (True). (d) opt122b.py (the optional R-N and R-S below, counts and
sha1s only); chk122b.py (title, block, UPDATE, placeholders, pipes, stale grep, quote sweep), lp122b.py (line-precise quotes new at this
fill), sim122b.py (landing simulation on origin trunk 616941eb, both cases) and rec122b.py (the first fill's record byte-unchanged):
Addendum 2.
The first fill's flags, resolved in L-4 (string checks by script, l4rel122b.py): G-1 (the source note) by F-13, the Lead's «G-1 source
note -> R-B»: L-4 ends «(P-ACYC, docs/si/P-ACYC.md with its fixes entries 1-2, docs/si/P-ACYC-fixes.md; L-SI successors 43-44)». G-7 (L41)
by F-12, the Lead's «G-7 L41 APPLIES (w* = K1 required referee repair, both SIGN WITH GAP; R119 precedent) -> R-G»: «the step w* = K1 of
LAMBDA-CONST's proof (σ̄(K2) toward K1 is Odd's unique optimum) is referee-originated (REFEREE R-P-ACYC §4.2 LC-1 and REFEREE-2 R2-P-ACYC
G-1 / W-1, found independently, restated in P-ACYC's fixes entry 1 F-1), signed by both referees» once in L-4, in the scope tail after
«not a TARGET.md claim);», before «DATA (experiments/si/box81, check81.sh):»; the entry's L41 and L43 quote the ruling, the sentence, both
signatures and the joint gap map (one gap, LC-1 = G-1, closed by F-1 at both; open gaps: none). G-7 (ii) (AC-6): «G-7 (ii) AC-6 NOT L41»,
no line change. G-4 (N-1), G-U, G-2 and the G-9 notes: «G-4/G-U/G-2/G-9 to CHECKER; R-N not taken.»; unchanged at L-4 (F-12 and F-13 touch
no signed clause, no label, no DATA clause), restated below.
NOTES at this fill (for CHECKER; no line change proposed; each optional string exact, its old string once in L-4 and once in the UPDATE,
opt122b.py):
- G-4 (N-1), RESTATED FOR CHECKER'S RULING (the C115 E-1 class; the Lead left it to CHECKER; no change needed in my reading). BETA-ACYC's
  proof needs POINTWISE optimality (REFEREE-2 N-1, l. 41-48). L-4 names «the order ⊴ and σ̄ of R118 [VJ]», and R118's quoted σ̄ («σ̄ is
  Odd's optimal counterstrategy, chosen by a fixed deterministic rule», packet l. 38-39) does not say «pointwise»; the landed source
  (RESULTS R57 (b), [1E-N3], as landed in R104: «S1's σ̄, and τ̄ on the dual game, are pointwise optima», RESULTS l. 9864) is in L-4 only
  for the corollary («with Lemma K2-r and [1E-N3] as listed in R118 (k)»). F-7 put N-1 into the packet text only («N-1 is applied to the
  packet text only, so that AC-L1's string stays byte-exact in the line», fixes l. 79). REFEREE-2 marks it «(N-1, recommended only)» (l.
  185-186) and matched L-3 without it; REFEREE's §4.1 uses «against pointwise optimality» (l. 108) and did not ask for it; the packet's §1
  (l. 69-70) defines σ̄ pointwise, and R118's own premise text and BR-SEG use the same σ̄. Optional R-N: "the order ⊴ and σ̄ of R118
  [VJ];" → "the order ⊴ and σ̄ of R118 [VJ], σ̄ pointwise optimal (RESULTS R57 (b), [1E-N3], as landed in R104);": L-4 + R-N sha1
  d4b8d8f27c15ad8cbd86efcc26450529daa42b0b (3,150 bytes, 43 «(» / 43 «)»), its UPDATE = the L-4 UPDATE with R-N, sha1
  e89525fdb33a4bafa7f0a09d7fe778dc5deab23b (3,178 bytes). If taken, it changes AC-L1's new string, so both referees' byte tests are
  re-run, with a fixes entry 4 and an L-5.
- N-S, THE SOURCE NOTE'S ENTRIES AND SUCCESSORS (CLEAN by C135 E-1's statement of the rule, in my reading; CHECKER's choice). L-4's note
  names «fixes entries 1-2» and «L-SI successors 43-44»; fixes entry 3 and L-4 are successor 45's (fixes l. 116). Entry 3 carries no proof
  and changes two line strings only (F-12, F-13); C135 l. 22-23: «the note names the authors of proof-bearing text; a line-only entry need
  not be named»; REFEREE §E agrees: «Note, not an item: entry 3 (successor 45) changes only the line, as in P-N5-ASC §F's note. «entries
  1-2 … successors 43-44» is accurate for the packet's content.» (l. 375-376), and REFEREE-2 Add. 4: «Entry 3 changes only the line, so
  omitting it is consistent with the Lead's G-1 ruling ✓.» (l. 402). R121's L-4 has the same shape (entries 3-4 by L-NEW successor 63, not
  named; C135 Add. 1 on it is not on origin at the third fetch). Entry 3's own words «G-1 = the source note must name the fixes entries
  and their author» (l. 119-120) can be read as all entries. If CHECKER wants entry 3 named: R-S "(P-ACYC, docs/si/P-ACYC.md with its
  fixes entries 1-2, docs/si/P-ACYC-fixes.md; L-SI successors 43-44)" → "(P-ACYC, docs/si/P-ACYC.md with its fixes entries 1-3,
  docs/si/P-ACYC-fixes.md; L-SI successors 43-45)": L-4 + R-S sha1 5c5a33798ae2503b4b2d78fc81e4e2f5b24e2974 (3,080 bytes), its UPDATE
  36b9bef4205458928a715363cde1a5e6b19c3a6b (3,108 bytes); with R-N and R-S both: L-4 935d10dcbbf659ee6302e6159955740e4bb6a068 (3,150
  bytes), UPDATE d1dbe8e75a41b2ff8db541630bf4d44040dd6dc9 (3,178 bytes).
- G-2, G-U, G-9 (unchanged at L-4). F-12 and F-13 change no signed clause, no label and no DATA clause; the scope tail's READING (G-2) is
  byte-unchanged; the UPDATE procedure (G-U) is the first fill's, and on L-4 it gives the same 11 hunks; every DATA figure is
  byte-unchanged and re-run ((b) above). G-2 (ii) on the new sentence: w*, σ̄, K1 and K2 are the packet's (§1-§2) and R118's (Lemma K2-r);
  «LC-1», «G-1», «W-1» and «F-1» name report and fixes items, not terms of a signed clause; «found independently» is REFEREE-2 Add. 1 l.
  260.
- D-7, A COUNT IN THE FIRST FILL'S G-10 (history, no verdict affected). G-10 says «L4» 0 in L-3; that is a token count: the string «L41»
  occurs once in L-3 and once in L-4, inside the tower genome name «SL41_d28», not as a citation of L41.
- D-9, A LINE CITATION IN REFEREE-2 ADD. 4 (history, no verdict affected). Add. 4 l. 391 says «Add. 3 (l. 315) recorded «F-1 (W-1 = LC-1):
  my text verbatim … This closes G-1, so LAMBDA-CONST is now SIGN»»; l. 315 is in Addendum 2 (l. 298-353; Addendum 3 is l. 355-374), and
  the quote drops the bold marks of l. 315. The entry cites l. 315 as Add. 2.
- D-8, STAMPS (history). Fixes entry 3's heading «ruled in by the Lead 05:13Z» (l. 116) is LEAD-STATE l. 2754's stamp; 0bc6f028 was
  committed after it (05:54:32Z). The first-fill draft 0fa23b17 was committed at c9591e35 (05:40:39Z).
Changes at this fill, and nothing else: line 1 (the header); this section; the title (L-4); in the entry: Object (successors 43-45; the
packet at 0bc6f028; three fixes entries; L-4 the line of record; line history L-1 to L-4; the L-4 rounds: REFEREE §E, REFEREE-2 Addendum
4), Claims signed (the L-4 rounds; entry 3 changes the line only), The RESULTS line (L-4; the L41 sentence; the source note; one
parenthesis re-worded), Premise (the trunk), L41 and L43 (the Lead's ruling, L-4's sentence, both referees' readings of it at L-4, both
signatures, the joint gap map, the AC-6 ruling), Fixes (header, entry-3 bullet, closing bullet), Honest limits (viii) and (ix)
(re-worded), Data (0bc6f028; the re-run of 06:41Z), Signatures (§E and Addendum 4; successor 45's commit), INDEPENDENCE (L-4's strings),
TARGET.md diff (L-4); the GAPS preamble and the UPDATE (rebuilt from L-4); Addendum 2 (new). The FIRST FILL text below (from "FIRST FILL
(this text)" to (14)) and the Addendum (1)-(10) are kept byte-unchanged as the record of draft 0fa23b17 on L-3 (rec122b.py): where they
call L-3 the title line or the current line, raise G-1 or G-7 as flags, propose R-B, R-G or R-N, or give the first fill's line numbers,
counts, slices and UPDATE sha1 (a9274893…), they describe draft 0fa23b17 at 05:11Z; the Lead ruled at 05:13Z (R-G and R-B taken, as F-12
and F-13; R-N not taken; G-4, G-U, G-2 and G-9 to CHECKER), and the entry block now follows L-4.
FIRST FILL (this text). Read at the origin heads fetched between 2026-11-08T04:54:20Z and 04:55:00Z by date -u (one git fetch of
claude/l-si, claude/referee, claude/referee-2, claude/checker, claude/vibrant-johnson-nxvvxo; date -u before and after it; I merged,
committed and pushed nothing and edited docs/agents/R122-draft.md only): l-si 9177e274 (9177e27451b291470fae17608a57b67151038dbc,
2026-11-08T04:03:48Z, «L-SI box 84 milestone 3 (i): LOWER-BLIND (keep form) PROVED, adoption form false; LO2 smallest test
(SELF-MIRROR DICHOTOMY); successor 44 handover», the branch head; git diff ff9b1639 9177e274 names only docs/si/box84-hubpair.md,
experiments/si/box84/ and notes/L-SI.md, so no P-ACYC file and nothing under experiments/si/box81 changes), so the objects are those of
ff9b1639 (ff9b16396129de30cca6d10a67285c3ed558d14a, 2026-11-08T03:35:20Z, «L-SI: P-ACYC fixes entry 2 + line L-3 (D-5; N-2 = AC-7), by
script», L-SI successor 44, the commit of record); the packet freeze e3ac4b06 (e3ac4b06f13cd0c7c7ac4589b0c5824bf41ca5a7,
2026-11-07T22:38:10Z, L-SI successor 43) and fixes entry 1 / L-2 01a68edc (01a68edc54e64030d3e623694c58ce0c99f4f363,
2026-11-08T02:10:34Z, successor 44). referee 013f821b (013f821bd31de10ee93abf4f5c279962e1570de9, 2026-11-08T04:24:28Z, «REFEREE 28:
R-P-N5-ASC §E (L-3 = L-2 + R1-R4, byte test PASS; R5 required: CHAIN-DECOMP hypothesis in the line)», the branch head; it does not touch
docs/referee/R-P-ACYC.md, whose last commit is d4423d6d (d4423d6dec00a24c1df71c230411f13684922cec, 2026-11-08T04:03:53Z, «REFEREE 28:
R-P-ACYC §D time fix (04:03Z by date -u)»): the file there and at 013f821b 348 lines, 26,849 bytes, sha1
b09be901fb54f1e0f27075817a53ece4864e5b5b; by cmp its l. 1-331 = c865da81's file (c865da817aeb579cfce6ca0fba6da68249742548,
2026-11-08T02:38:59Z, §C: 331 lines, 25,488 bytes, sha1 e01080f9448789b6049afde96f5102cc2754bd73) and its l. 1-273 = the report
(first committed a9d4e44e, 2026-11-08T00:48:22Z, «REFEREE 28: R-P-ACYC first review (BETA-ACYC SIGN; LC-1 gap with repair; L-1 NOT
YET: AC-L1..AC-L5)»; byte-equal at d3d0a600 (d3d0a600372b897a03cba23a96e9028cb5e99875, 00:48:27Z, «REFEREE 28: notebook time fix (00:48Z
by date -u)», which changes notes/REFEREE.md only), the commit the fixes file and the brief cite: 273 lines, 20,848 bytes, sha1
f3099aeb7d35430892d92aef820463787aa893c7 = fix1/fix1.sha1's pin of ref_d3d0a600.md); §D was first committed at 17c81b70
(17c81b707d1c08ce69bb9ae70f794ef342d0a85e, 04:03:49Z; sha1 86f1a1bb…), whose l. 333 heading read «04:05Z», and d4423d6d changes that
one line to «04:03Z» (diff: one line). referee-2 e1878470 (e187847085de9c572e016edab37dd0a7e18faf78, 2026-11-08T04:06:09Z, «REFEREE-2
32: R2-P-ACYC Addendum 3 (fixes entry 2 CORRECT, L-3 MATCHES, all SIGN); handover for successor 33 (next: P-N5-QUIET)», the branch
head; docs/referee-2/R2-P-ACYC.md there 374 lines, 34,017 bytes, sha1 6cdb50101bbe8526502f973d3ab55faa7e71055b; its prefixes, by cmp:
l. 1-353 = d7ca68f4's file (d7ca68f42d1afc1db557be734f4fe96e17f05a29, 02:38:33Z, Add. 2: 353 lines, 32,354 bytes, sha1
6f4fa7869a42593137b400e80990989bf456eecf), l. 1-296 = 6c937bc6's (6c937bc6e3af08a68530b01d7b5639c5ec7de25c, 01:44:31Z, Add. 1: 296
lines, 27,351 bytes, sha1 81ddbab7ce0bc5ca26429774f1350a81ab6a0f8c = fix1.sha1's pin of ref2_6c937bc6.md), l. 1-254 = bf02e618's
(bf02e61888453d86f93d4fcce5207d446ce9a378, 00:55:23Z, the report: 254 lines, 23,547 bytes, sha1
aac39a791b414248175b864460c64fbb7ca8219d)). checker fa8add12 (fa8add12b8f81e827af46da77b051e1be13a970e, 2026-11-08T03:51:39Z,
«CHECKER successor 21: HANDOVER to successor 22 (C135 open: Add. 1 next)», the branch head; docs/checker/ ends at C135.md; C136 does not
exist; notes/CHECKER.md l. 10: «Coming: P-ACYC (L-SI 43).»). e3ac4b06, 01a68edc, ff9b1639, c865da81, 17c81b70, d4423d6d, d7ca68f4 and
e1878470 are NOT ancestors of the local trunk c8f42538 or of origin trunk 8f490d7a (git merge-base --is-ancestor, after the second
fetch); a9d4e44e, d3d0a600, bf02e618 and 6c937bc6 are ancestors of both; ff9b1639 is an ancestor of origin/claude/l-si, d4423d6d of
origin/claude/referee, e1878470 of origin/claude/referee-2. The Lead merges claude/l-si, claude/referee and claude/referee-2 before
landing. Second fetch at 2026-11-08T05:10:38Z-05:10:39Z by date -u (same five branches; rc 0): l-si 27ef5506
(27ef5506bfa82d5f8739a09db3a193051a562783, 04:31:16Z, «L-SI successor 45: handover check (five questions)», after a merge of trunk
4aaba7d5, 70eeefd8), referee-2 98b9622b (98b9622b99e0dfd16353c68572a74c9ee8eb7c8f, 04:30:58Z, «REFEREE-2 32: R2-P-N5-ASC Addendum 4: L-3
(C135 R1-R4) MATCHES»), origin trunk 8f490d7a; referee 013f821b and checker fa8add12 unchanged. git diff --quiet ff9b1639 27ef5506 on the
packet, the fixes file, L-1, L-2, L-3 and experiments/si/box81: equal; git diff --quiet e1878470 98b9622b on docs/referee-2/R2-P-ACYC.md
and docs/referee-2/R2-P-ACYC/: equal. So every object of this fill is unchanged at the second fetch.
Trunk: local HEAD c8f42538 (c8f42538f25b97cc85dfa3df2b33cd7948eb41ca, 2026-11-08T05:05:24Z, «Lead: REFEREE-2 33 roster + restart row;
L-RED 58 check scored 5/5 + GO R223; L-COMP L7cr ROOM lane; log 04:3xZ-05:05Z», committed during this fill; its parent 8f490d7a, «Lead:
L-SI 45 roster + restart row», the local HEAD at the first fetch and origin trunk at the second; c8f42538 changes docs/NOW.md,
docs/agents/LANE-RESTART.md and docs/agents/LEAD-STATE.md only; the working tree has the Lead's uncommitted docs/agents/LANE-RESTART.md,
and RESULTS and GAPS equal HEAD and 8f490d7a, git diff --quiet). RESULTS at HEAD: sha1 66e7119615efa5a0bb25b898e32b5b371c55c122, 14,962 lines (byte-equal
to RESULTS at 37a4855e, the trunk both referees checked their premise quotes against: git diff --quiet); «### R104» l. 9864, «### R117»
l. 13362, «### R118» l. 13607, «### R119» l. 13879, «### R120» l. 14114-14318, «**Erratum E-1**» l. 14320, «**Erratum E-2**» l. 14333,
«**Note E-3**» l. 14361, «## Dead ends (kept;» l. 14392. GAPS at HEAD: sha1 2a41c7654d4e9dedee7abc8591dfb792633bc2c9, 23 lines, l. 11
76 "|", 55 «UPDATE 2026-», the last R120's «UPDATE 2026-11-07 21:05Z: RESULTS R120 (P-TOWER-FUEL; CHECKER C134 0c816917)». R121 is NOT
landed («R121» 0 times in RESULTS and in GAPS; its draft docs/agents/R121-draft.md is the L-2 first fill, CHECKER C135 FAIL E-1..E-4 at
0942e8be, L-3 pending). «R122», «C136», «P-ACYC», «BETA-ACYC», «LAMBDA-CONST», «ACYC-LIN» and «ACYC-XI» occur 0 times in RESULTS and in
GAPS.
Sources read: the packet docs/si/P-ACYC.md (frozen e3ac4b06, unchanged at 01a68edc, ff9b1639 and 9177e274; sha1
0e9edcfda3e3a68dee63ff01427d526b14c67bc4, 193 lines, 16,852 bytes; read in full); docs/si/P-ACYC-fixes.md at ff9b1639 (sha1
c782b15ba07ef921a54963ab198c8ae73129a67f, 114 lines, 11,487 bytes; entries 1-2; read in full; its first 10,104 bytes = the file at
01a68edc, sha1 dd3d4546f12f11b9fd4848c5ab13739ac814fb5d, 97 lines, by cmp); line L-1 docs/si/P-ACYC-line-L1.txt (e3ac4b06; sha1
bb12deec6fb0129b4ea9f5af7dd96d6302c5ca50, 2,085 bytes); L-2 docs/si/P-ACYC-line-L2.txt (01a68edc; sha1
3a3096a45df6ca22e8099ca4e1a9ac1779c1321e, 2,741 bytes); L-3 docs/si/P-ACYC-line-L3.txt (ff9b1639, the file's only commit; sha1
03453361fead881493e2d2786b869f1c63158c4c, 2,765 bytes, one line with its newline; equal at 9177e274); experiments/si/box81 at ff9b1639:
check81.sh (read in full), pacyc.sha1 (pins the packet and L-1), fix1/fix1.sha1 (pins the two referee-report copies and L-2),
fix1/check_fix1.sh and fix2/check_fix2.sh (read in full; L-3 is rebuilt by fix2/mkL3.py, which asserts L-2's sha1, and compared by cmp),
lemma81.py and pacyc81.py (read in full), fix1/pacyc81t.py (its diff against pacyc81.py read), the frozen outputs out/lemma81_*.out,
out/pacyc81_*.out, fix1/pacyc81t_*.out, fix1/tn81.out, out/quotes81.out; REFEREE's file at a9d4e44e / d3d0a600, c865da81, 17c81b70 and
d4423d6d (read in full; its scratch tools listed, not re-run); REFEREE-2's file at bf02e618, 6c937bc6, d7ca68f4 and e1878470 (read in
full; its tools listed, not re-run); RESULTS R104 (l. 9864), R117 (l. 13362), R118 (l. 13607-13878; (a), (d), (k), (l) and its K2-r
paragraphs read), R119 and R120 (the landed form); GAPS l. 11; DECISIONS l. 355-358 (L41) and DECISIONS-INDEX l. 34; docs/checker/C135.md
at fa8add12 (read in full; sha1 87dfa1eb7dd600a33cb0ad7aad2fca516bdabbc4, 93 lines) and notes/CHECKER.md l. 1-12; docs/NOW.md and
docs/agents/LEAD-STATE.md (grep: P-ACYC, R122, C136); docs/agents/R121-draft.md and R120-draft.md (the house form; R121's entry d[271:482]
and UPDATE d[491]) and R121's tools (r121/tools/upd121.py, chk121.py, sim121.py).
Checks run at this fill (scratch /tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad/r122;
nothing written into the repository but this file). (a) check81.sh from a git archive of ff9b1639 (experiments, docs, scripts),
2026-11-08T04:57:59Z-04:59:56Z, rc 0, output «P-ACYC fix1 checks: PASS», «P-ACYC fix2 checks: PASS», «box 81 checks: PASS» (it re-runs
every frozen output of box 81, pacyc81t and tn81, rebuilds L-2, L-3 and both fixes entries and compares them byte for byte, and checks
the pins). (b) A shape script on L-3 and the L-2 → L-3 byte test. (c) DATA, clause by clause, against lemma81.py, pacyc81.py and
fix1/pacyc81t.py and their frozen outputs (G-9). (d) upd122.py: the UPDATE with the controls R97-R120 (landed) and R121 (not landed)
(Addendum (8)). (e) chk122.py (title, block, UPDATE, quote sweep, stale grep) and sim122.py (landing simulation): Addendum.
LESSONS APPLIED (R121's list, plus C135). C113 E-1 / C123 E-1 / C133 E-1: the title is L-3 verbatim, nothing inserted and nothing
stripped; L-3 has no «R1xx» and no ledger tag before its claims (CLEAN). C133 E-3 / C134 E-3: the scope tail « (2026-11-07) — … » carries
«G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim» once; «gauntlet» 0 times in L-3 (CLEAN). C120-C135 / C134 E-4:
EVERY DATA clause tested against the code of its counter for unit, set and scope (G-9). C122 G-0: parentheses balanced (38 / 38). C122 E-3
/ C132 E-2 / C133 E-2 / C134 E-1 / C135 E-1: the source note names every proof-carrying file and the lane successors (G-1: FLAG). C132
E-7 / C133 E-6 / C134 E-2 / C135 E-2: a referee-originated proof step is named in the scope tail (L41; G-7: FLAG). C117 E-1 / E-2 / C135
E-3: no sentence of the line wider than the signed statements, no READING inside a signed clause (G-2: note). C135 E-4: every term of a
signed clause defined in the line or landed (G-2 (ii): CLEAN). C118 E-1 / C132 E-1: no status word that goes stale at landing (G-11).
C115 E-1: premises checked against RESULTS, landed entries only (G-4: one FLAG, N-1). C116 G-2: name clashes (G-6). C116 G-3: pins
(G-12). C119 E-1: every «referee X did Y» checked against that referee's file. C130 G-P / C133 G-P: the UPDATE builder carries a control
for every UPDATE that lands before this one (R97-R120 landed; R121 not landed, controlled against its draft and C135 §5). C132 Add. 1:
block re-run times as a date -u interval.
FLAGS FIRST (G-1 makes CHECKER FAIL as L-3 stands by the C122 E-3 / C132 E-2 / C133 E-2 / C134 E-1 / C135 E-1 precedents; G-7 needs
the Lead's L41 ruling, and if it is L41's case CHECKER FAIL as it stands by C132 E-7 / C133 E-6 / C134 E-2 / C135 E-2; G-4 (N-1), G-2
and G-U are CHECKER's rulings; G-9 (i)-(iv) are notes). Exact replacements R-B, R-G (and optional R-N), each old string once in L-3, by
script; L-3 with R-G then R-B: sha1 85bb221f19ca457655c954f570552bc0f4d8095d with its newline, 3,080 bytes, 41 «(» / 41 «)», 0 "|", one
« — »; its UPDATE by the procedure of G-U 425d10fe5ca0223568b5fb2f29bea4858307dc43 (3,108 bytes); R-N not built into a line.
- G-1, SOURCE NOTE (FLAG; the C122 E-3 / C132 E-2 / C133 E-2 / C134 E-1 / C135 E-1 class; CHECKER FAIL as it stands). L-3's last
  parenthesis is «(P-ACYC, docs/si/P-ACYC.md; L-SI successor 43)». It names neither the fixes file nor its author: both fixes entries
  are L-SI successor 44's (fixes l. 3 «## Entry 1 (fix round 1; L-SI successor 44; Lead 01:22Z and 01:39Z)», l. 99 «## Entry 2 (fix round
  2; L-SI successor 44; Lead 03:06Z)»), and entry 1 carries text the line rests on: F-1 repairs LAMBDA-CONST's statement («Old (§2): «w*
  does not depend on σ. Proof.» New: «w* = K1 for every σ in the frozen frame. Proof.»», fixes l. 11) and its proof (l. 12-17), and
  ACYC-LIN's R = 0 step (l. 20-21); F-9 adds AC-6 to ACYC-LIN's proof (l. 90-91). By C135's ruling («My C134 N-S ruling (the note names
  the authors of proof-bearing text; a line-only entry need not be named) gives the same answer: entry 1 is proof-bearing.») entry 1 must
  be named. Entry 2 is line text (F-10) and packet READING text (F-11, the header); R-B names both entries, as R121's R1 did; the R120
  form («with its fixes entry 1») would also meet the N-S ruling (CHECKER's choice). Proposed R-B: "(P-ACYC, docs/si/P-ACYC.md; L-SI
  successor 43)" → "(P-ACYC, docs/si/P-ACYC.md with its fixes entries 1-2, docs/si/P-ACYC-fixes.md; L-SI successors 43-44)". Old string
  once in L-3 and once in the UPDATE (script).
- G-7, L41: THE w* = K1 STEP OF LAMBDA-CONST (FLAG for the Lead's ruling; the C132 E-7 / C133 E-6 / C134 E-2 / C135 E-2 class). The
  packet's proof of LAMBDA-CONST leaves w* open (BETA-ACYC (1), l. 96: «Its cycle node is w* := K1 if σ̄(K2) leads to K1, else K2.») and
  argues constancy by «Under a fixed deterministic rule it is the same in every state.» (l. 124). Both referees found the same gap in
  their independent first reports (REFEREE LC-1, l. 12: «SIGN WITH GAP LC-1 (the proof never fixes w* = K1; with w* = K2 the statement
  would be false at K1; repair below)»; REFEREE-2 G-1, l. 19: «**SIGN WITH GAP** (Opus 5.5, D1): G-1, the proof never shows w* = K1, and
  the map is false at K1 (and s on Γ3) unless w* = K1; my one-line repair closes the gap (W-1, required)»), each wrote the same one-line
  repair (REFEREE l. 129-134; REFEREE-2 l. 89-91, W-1 l. 93-102), and fixes entry 1 F-1 restates REFEREE-2's text, «which also carries
  REFEREE's uniqueness point» (fixes l. 13). ACYC-LIN's R = 0 at K2 and ACYC-XI rest on it (REFEREE l. 13-14; fixes l. 20-21). Each
  referee signs the repaired proof after reading the fixes entry (REFEREE §C l. 297-301, «LC-1 is CLOSED for LAMBDA-CONST, ACYC-LIN and
  ACYC-XI.»; REFEREE-2 Add. 2 l. 315, «This closes G-1, so LAMBDA-CONST is now **SIGN**.»). This is R119's case (DBL-EQ (b)'s DB-3:
  «uses one referee-originated step (REFEREE's DB-3, fixes entry 1 F-3, found independently by REFEREE-2)», RESULTS R119's line) more
  than R121's (an optional step): the step was REQUIRED (SIGN WITH GAP at both) and closes a gap in a signed statement. L-3's scope tail
  does not say so («referee» and «REFEREE» 0 times in L-3, by script). The repaired step is also R118's landed Lemma K2-r in substance
  (REFEREE l. 134: «This is R118 (g)'s O-1 sentence and Lemma K2-r. The repair re-proves it, so no new premise is needed.»); that makes it
  checked, not lane-originated. Proposed R-G (the R119 form, inside the scope words, before the DATA): "not a TARGET.md claim); DATA
  (experiments/si/box81, check81.sh):" → "not a TARGET.md claim); the step w* = K1 of LAMBDA-CONST's proof (σ̄(K2) toward K1 is Odd's
  unique optimum) is referee-originated (REFEREE R-P-ACYC §4.2 LC-1 and REFEREE-2 R2-P-ACYC G-1 / W-1, found independently, restated in
  P-ACYC's fixes entry 1 F-1), signed by both referees; DATA (experiments/si/box81, check81.sh):". Old string once in L-3; in the UPDATE
  the drop words are gone, so the same sentence goes after «(no bound on R for Ξ-cyclic genomes)» (old string "(no bound on R for Ξ-cyclic
  genomes); DATA (experiments/si/box81, check81.sh):" once in the UPDATE; script: the UPDATE built from L-3 + R-G + R-B = the L-3 UPDATE
  with R-B and that insertion, True). (ii) AC-6 (F-9, REFEREE's optional text «Any start mover state is covered: …», fixes l. 90-91) is a
  second referee-written sentence in ACYC-LIN's proof. In my reading it is NOT L41's case: both referees read the unrepaired proof as
  complete for every start (REFEREE l. 145-146, «(a) and (d) fix no start»; REFEREE-2 l. 110, «BR-SEG as landed holds for every Howard run
  of IDEAL-CYC(G) from any mover state («every maximal run of p-steps») ✓»), so AC-6 makes explicit what R118 (d) already gives. The
  Lead rules.
- G-4 (N-1), PREMISE OF BETA-ACYC's «every optimal counterstrategy» (FLAG for CHECKER's ruling; the C115 E-1 class; no change needed in
  my reading). BETA-ACYC's proof needs POINTWISE optimality (REFEREE-2 N-1, l. 41-48). L-3 names «the order ⊴ and σ̄ of R118 [VJ]», and
  R118's quoted σ̄ («σ̄ is Odd's optimal counterstrategy, chosen by a fixed deterministic rule», packet l. 38-39) does not say «pointwise»;
  the landed source (RESULTS R57 (b), [1E-N3], as landed in R104: «S1's σ̄, and τ̄ on the dual game, are pointwise optima», RESULTS l.
  9864) is in L-3 only for the corollary («with Lemma K2-r and [1E-N3] as listed in R118 (k)»). F-7 put N-1 into the packet text only
  («N-1 is applied to the packet text only, so that AC-L1's string stays byte-exact in the line», fixes l. 79). REFEREE-2 marks it
  «(N-1, recommended only)» (l. 185-186) and MATCHES L-3 without it; REFEREE's §4.1 uses «against pointwise optimality» (l. 108) and did
  not ask for it. The packet's §1 notation (l. 69-70) defines σ̄ pointwise, and R118's own premise text and BR-SEG use the same σ̄.
  Optional R-N (if CHECKER wants the source in the line): "the order ⊴ and σ̄ of R118 [VJ];" → "the order ⊴ and σ̄ of R118 [VJ], σ̄
  pointwise optimal (RESULTS R57 (b), [1E-N3], as landed in R104);" (old string once in L-3 and once in the UPDATE; it changes AC-L1's new
  string, so both referees' byte tests would be re-run). Not built into a line.
- G-2, THE SCOPE TAIL'S READING (note for CHECKER; the C117 E-1 / E-2 / C135 E-3 class; no change in my reading). L-3's tail begins «so
  on the whole domain of the tower route N5′-xi's mover phase is linear in N, while N5 with SPEC's S4a tie rule realises L(G) there
  (R117)». That is the packet's §5 («## 5. What this says about N5 (S4a) and N5′-xi (READING, not to sign)», l. 148) in its narrow form.
  It is not inside a signed clause (C135 E-3's case): it follows « (2026-11-07) — », where scope words stand (R118: «no bound on R is
  claimed (OPEN), so nothing about N5′-xi's or N5's running time follows»). Its two halves are ACYC-XI (signed) and R117's landed result,
  cited as R117; «the whole domain of the tower route» is R104's and R117's scope (REFEREE-2 l. 139: «The «whole domain of the tower
  route» is right: R104's Corollary REAL-IDEAL and R117's REACH3 are stated for acyclic G ✓.»). Both referees checked this sentence on
  L-1 (REFEREE l. 238: «L-1 is already correct here («N5′-xi's mover phase is linear in N»; «nothing is claimed about iterations after the
  first fallback, about Ξ-cyclic genomes»).»; REFEREE-2 l. 136-138), and W-2 / AC-3's over-reaches are packet text, not in the line.
  «realises L(G)» is weaker than §5's «length exactly L(G)», so F-4's «if L(G) ≥ 1» qualification is not needed in it.
  (ii) SYMBOLS (C135 E-4 class): CLEAN. Every term of a signed clause is landed or defined in L-3: genome, Ξ-graph, Γ(G), its start,
  β-face, e-vertex (R104); Γ3(G), pads, S3 (R117); IDEAL-CYC(G), Howard run, C, R, T_CYC, cycle node (R118 (a), [VJ]); T3, standard
  (R118 (k)); «first fallback» defined in the line («i.e. the least iteration k at which SPEC S4c applies»); the frozen frame defined in
  the line («every Even strategy that agrees with the stated start off the movers (transported through the pads on Γ3)»).
- G-U, THE UPDATE PROCEDURE (FLAG for CHECKER's ruling; no line change needed). L-3 has R118's line shape (the shape C135's G-U ruling
  covers: «G-U ruling: R118's procedure applies»): labels BEFORE their clauses after «RESULTS R15's object): », one « (2026-11-07) — »,
  scope words with the DATA inline («; DATA (experiments/si/box81, check81.sh): …», no «(DATA: » or «(DATA, » parenthesis), the drop
  words, the source parenthesis. So R105's sentinel_build («(DATA: ») and R111's sentinel_build111 («(DATA, ») do not apply; R118's
  run118() does, with R122's start, labels and source prefix in place of R118's and nothing else changed (upd122.py run122() = R121's
  run121(): build() with the sentinel, the source parenthesis kept, «; G-N5-TIME stays OPEN» and «; not M3, not a step-4 pass, not a
  TARGET.md claim» dropped, «. G-N5-TIME stays open.» appended), cross-checked by a direct build (True). Two differences from R121's line,
  both handled by build() unchanged: (1) the connectors «; hence » (before ACYC-LIN, as R118's «; hence (Theorem T-CYC)») and «; and »
  (before ACYC-XI) stay in front of their clauses (the direct build's assertion admits them; run118's admitted «; hence »); (2) the drop
  words stand INSIDE a parenthesis («(no bound on R for Ξ-cyclic genomes; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md
  claim)»), so dropping them leaves «(no bound on R for Ξ-cyclic genomes)» (R118's and R121's drop words were top-level). The fourth
  label «(Corollary ACYC-XI, PROVED-CONDITIONAL on …, with Lemma K2-r and [1E-N3] as listed in R118 (k))» carries an inner «(k)»; it is
  found by its matched parenthesis (paren_at, R118's way for REACH3-CYC's label) and moves whole. Result: the four labels behind their
  clauses, « (2026-11-07) — » → «: » (the last label then stands before «: »), the drop words dropped, the source parenthesis kept; token
  diff L-3 → UPDATE 11 hunks, 51 tokens out, 50 in, nothing else (Addendum (8)). CHECKER rules whether this is the procedure.
- G-9, DATA, CLAUSE BY CLAUSE (the C120-C135 rule: unit, set and the statement's scope of every count, against the counter code it names;
  every signed clause matched to a count or a no-DATA entry). Every figure is in the frozen outputs and reproduced by my re-run of
  check81.sh ((a) above; it diffs each output). Counter code: lemma81.py l. 30-51 (check()) and l. 54-70; pacyc81.py l. 18-40 (one()) and
  l. 43-58; fix1/pacyc81t.py (pacyc81.py with REFEREE-2's two diffs: taubad and the post-fallback histogram).
  - Sets. «300 random Ξ-acyclic genomes (lemma81.agen, d 1-6, w 1-3, degree 2-3, seed 7; 768 states)»: lemma81.py agen 300 7 draws
    agen(rng, randint(1, 6), randint(1, 3), randint(2, 3)) and keeps Ξ-acyclic ones («genomes 300 tried 300 states 768»); pacyc81.py 300 7
    draws the same stream (agen is acyclic by construction, so nothing is skipped), «genomes 300 states 768». «the four tower genomes …
    (44 states)»: lemma81 «states 44», pacyc81 «states 44». MATCH. «each run from the genome's stored start (IDEAL-CYC) or from S3 (Γ3)»:
    idealcyc.run(G) and n5x.start_pair (pacyc81.py l. 20). MATCH.
  - BETA-ACYC «σ̄ off the β-face in 0 (state, gate) pairs»: notbeta, lemma81.py l. 44 (sb[g] != b, per (state, gate) along the run) and
    pacyc81.py l. 33 (sb[gt] != pβ_g on states 0, …, k1 − 1); 0 on A and B in both. MATCH. NOTE (i): it tests the computed σ̄ only; the
    lemma's «every optimal counterstrategy» is covered by lemma81's nonstrict 0 (l. 45; in §6, not in the line) and by the referees' brute
    force (REFEREE l. 116; REFEREE-2 l. 147-148); REFEREE-2 l. 193-194: «Optional: add «, β-face not strictly better 0».» (not taken). The
    no-e-vertex clause: «no separate DATA» (REFEREE's eplay 0 is referee data, l. 113-114).
  - LAMBDA-CONST and ACYC-LIN «C 0, R 0, runs with T_CYC > N 0 (lemma81.py, IDEAL-CYC; ACYC-LIN from other mover states: no separate
    DATA)»: C and R from consecutive states' Λ-vector and σ̄-vector (l. 46-49), R118 (a)'s labels; T_gt_N «T > N» with T the run's step
    count (l. 51, 69). MATCH. NOTE (ii): C 0 along runs is weaker than LAMBDA-CONST (independence of σ and the explicit map); REFEREE-2 l.
    191-192: «The C counter (consecutive-state Λ changes) is weaker than LAMBDA-CONST (σ-independence and the explicit map). L-1 cites it
    as «C 0», not as LAMBDA-CONST's DATA, so it is OK as stated.»; the referees' lamfail 0 (REFEREE l. 136-137; REFEREE-2 17,204 states, l.
    192) is referee data. The line names no counter as LAMBDA-CONST's own; CHECKER may rule whether a no-DATA word is needed (packet §6 maps
    C to LAMBDA-CONST).
  - ACYC-XI «along N5′-xi on Γ3 from S3 (pacyc81.py; τ by fix1/pacyc81t.py), σ̄ off the β-face 0, states that are not standard (σ off the
    movers and τ) 0, genomes with no fallback 0, genomes with first fallback after iteration N + 1 0»: pacyc81.py nonstd (l. 34: an Even
    non-mover vertex whose σ differs from state 0 = S3) + pacyc81t taubad (τ(g) ≠ pe_g at some gate or τ(K2) ≠ K2), both 0; nofallback 0
    (l. 54); bigT (l. 57, T3 > N, i.e. k1 > N + 1) 0. MATCH (A: «nofallback 0 notbeta 0 nonstd 0 C 0 R 0 bigT 0», taubad 0; B the same).
    The parenthesis «(k = T3 + 1 is R118 (k)'s own clause, and N5's L(G) is R117's: no separate DATA)»: no-DATA entries. CLEAN.
  - Control «five Ξ-cyclic genomes rd2_d3, rd2_d4, rd3_d3, rf_d4, RS2 (59 states; the same counts on IDEAL-CYC and along N5′-xi on Γ3;
    e-priorities ordered by (lev, gate index), as in ref gamma3.build): σ̄ off the β-face in 121 (state, gate) pairs, C 15, R 25»:
    out/lemma81_cyclic_control.out «states 59 notbeta 121 nonstrict 121 C 15 R 25» and out/pacyc81_cyclic_control.out «states 59
    nofallback 0 notbeta 121 nonstd 0 C 15 R 25» (check81.sh's two command lines name the five files). MATCH. NOTE (iii): DATA of a
    control, not of a statement; the counts depend on the e-order (REFEREE-2's gate-index order gives 111, 15, 20 on 51 states, l. 170;
    D-3), which the line states.
  - No-DATA list: BETA-ACYC's no-e-vertex clause, ACYC-LIN from other mover states, «k = T3 + 1» and N5's L(G). The first-fallback
    definition and the scope tail are not counts. NOTE (iv): the unrepaired «The bound is attained» sentence is gone (F-2, AC-2); the line
    never claimed attainment. CLEAN.
- G-4, PREMISE ROUTE (the C115 E-1 class): CLEAN but for N-1 above (my script on RESULTS 66e71196 at c8f42538). R-labels in L-3: «R104»,
  «R117», «R118», «R15» (no other R-number); all landed (### R15 l. 624, ### R104 l. 9864, ### R117 l. 13362, ### R118 l. 13607). The
  sub-items R118 (a), (d), (k), (l) are R118's entry body (l. 13677, 13689, 13704, 13716); «[REACH-L]» 15 times in RESULTS, «Lemma K2-r»
  11, «[1E-N3]» 23, R15's object «N5 "SSI-GLOBAL" as specified in docs/new/N5-ssi-global.md» once. The corollary's condition is R118's
  REACH3-CYC, itself CONDITIONAL on [REACH-L], which R117's ENTRY signs for acyclic Ξ-graphs while R117's LINE states only S3-START and PAD
  (R118 l. 13707-13709: «which RESULTS R117 (P-N5-REACH) signs in its entry (S3-START, PAD, K3, TAU3 for every genome; ESC3, W3 for
  IDEAL-ACYC) and states in its line only for acyclic Ξ-graphs (S3-START, PAD)»); L-3 says «whose [REACH-L] premises RESULTS R117's entry
  signs for acyclic Ξ-graphs» and keeps the label PROVED-CONDITIONAL, the R118 form; both referees: the label is correct (REFEREE-2 l. 38:
  «The packet's label «PROVED-CONDITIONAL on (k) + (l)» is correct and conservative ✓.»). The packet's §0 quotes: «quotes: 28 of 28
  verbatim» (quotes81.py, re-run in (a)); REFEREE 27 + TARGET (l. 47-58), REFEREE-2 27 of 27 (l. 30-32). The LC-1 repair cites «R118's
  Lemma K2-r» in the proof (fixes l. 16), a landed lemma; REFEREE: «no new premise is needed» (l. 134). L-3 has no guillemet quote.
- G-6, NAMES (by script on RESULTS 66e71196 / GAPS 2a41c765). 0 times in RESULTS and GAPS: «R122», «C136», «P-ACYC», «BETA-ACYC»,
  «LAMBDA-CONST», «ACYC-LIN», «ACYC-XI», «w*», «frozen frame», «pacyc81», «box81». «IDEAL-ACYC» (R117 / R118) is another name that
  shares the string «ACYC»; no label equals it. Honest limits (vii).
- G-P, PLACEMENT (Lead). R120 LANDED (RESULTS l. 14114-14318, GAPS l. 11 last). R121 is NOT landed (C135 FAIL; second fill on L-3
  pending) and is routed before R122 (LEAD-STATE l. 2725: «(2) R122 = P-ACYC (L-SI): …»). R122's block goes after R121's block, before
  «**Erratum E-1**», and its UPDATE after R121's on GAPS l. 11. Simulated with R121's draft entry d[271:482] in place (sim122.py):
  Addendum (7). If R121 is not landed first, R122 goes after R120 by the same rule (also simulated).
- G-0, THE CHECKER NUMBER. docs/checker/ on claude/checker (fa8add12) ends at C135.md; «C136» occurs 0 times in RESULTS, GAPS,
  DECISIONS-INDEX, NOW and notes/CHECKER.md (whose l. 10 lists P-ACYC as «Coming»), and twice in LEAD-STATE at c8f42538, both the Lead's
  routing of this fill (l. 2743, l. 2746: «first fill subagent running -> C136 after R121 lands (ids in order).»). This draft uses C136
  (title fill, UPDATE head, GAPS preamble), as the brief says.
- G-5, ERRATA (note). E-1 (R97-R100 counts), E-2 (R105's CHAIN-BACK, RANK_t, KEYFLIP) and Note E-3 (R110's SC-ISO) do not bear on R104's
  definitions, R117's Γ3, R118 (a), (d), (k), (l) or R15.
- G-8, SCOPE AND TARGET (note). L-3's «nothing is claimed about iterations after the first fallback, about Ξ-cyclic genomes, or about the
  running time of N5 or N5′-xi» equals packet §4's «Not claimed» and §7 (l. 192) in meaning; REFEREE «## 8. TARGET.md diff (§7): CLEAN»
  (l. 258), REFEREE-2 l. 229-230 («Nothing bounds N5′-xi's total iterations, its bit cost (§3) or its output ✓.»). No statement mentions
  a parity game's winning region or an algorithm's total running time; T_CYC ≤ N and k ≤ N + 1 count steps of a restricted run on a
  restricted class (TARGET.md §4: «Polynomial only on a restricted class …»).
- G-10, LEAD RULINGS AND READINGS. L-3 cites no Lead reading by label («Lead reading» 0, «L4» 0 in L-3). REFEREE-2 l. 47 records a Lead
  reading at 00:44Z (R21 (a) on 𝒞^1O as a second source of pointwise optimality); F-7 did not add R21 (a) («R21 (a) is not added
  (optional).», fixes l. 82). No line change asked.
- G-11, STALE WORDS (notes). L-3 has no «pending», «not landed», «NOT YET», «candidate», «will » (0 each). «G-N5-TIME stays OPEN» is
  dated by the line's «(2026-11-07)». The packet date: frozen 2026-11-07 (e3ac4b06, 22:38:10Z), the line's date; L-3 itself is dated
  2026-11-08 (ff9b1639), as R121's L-2.
- G-12, PINS (the C116 G-3 class; CLEAN in substance). pacyc.sha1 pins the packet and L-1; fix1/fix1.sha1 pins L-2 and the two referee
  copies; L-3 and the fixes file are not in a sha1 pin file but are rebuilt by fix2/mkL3.py (which asserts L-2's sha1) and
  fix1/mkfix1.py + fix2/mkfix2.py and compared by cmp in check_fix2.sh, run by check81.sh (my re-run (a): PASS). A changed L-3 fails
  that cmp. ref.sha1 and inst.sha1 pin the runners and instances (check81.sh l. 7-8).
- G-13, THE REFEREES' ROUNDS: (3), (4). D-items: (11).
- G-14, THE FIXES FILE (note). Two entries (entry 1: F-1 LC-1 = W-1, F-2 AC-2, F-3 AC-3 = W-2 (a)-(c), F-4 AC-4 = W-2 (d), F-5 W-3 (a) +
  D-1 + AC-L4, F-6 AC-L5 = D-2 + D-3, F-7 AC-L1..AC-L3 + N-1 (packet only), F-8 D-4, F-9 AC-5, AC-6, line L-2; entry 2: F-10 D-5, F-11
  N-2 = AC-7, line L-3); entry 1 carries the LC-1 / W-1 step (G-7). L-2 + F-10's one string = L-3 (True, my script).
- G-N, NOVELTY (note). No outside source; VJ00 §4.2 / Friedmann arXiv 1106.0778 §3 enter through R118's landed premises; the entry makes
  no literature claim.
- CLEAN AT L-3 (by script on 03453361): C113 E-1 / C123 E-1 / C133 E-1 (L-3 starts «Odd never leaves the β-face on Ξ-acyclic genomes»,
  «R1xx» 0); C133 E-3 / C134 E-3 (« (2026-11-07) — » once, «not a TARGET.md claim» once, «G-N5-TIME stays OPEN» once, «not a step-4 pass»
  once, «gauntlet» 0); C114 Add. 1 E-1 (<DATE>); C115 E-1 (G-4 but N-1); C116 G-2 (G-6); C122 G-0 (38 / 38); C116 G-3 (G-12); C135 E-3
  (no READING inside a label's clause; G-2); C135 E-4 (G-2 (ii)); the DATA clauses (G-9, notes only); «|»: 0 in L-3, 0 in the entry
  block, 0 in the UPDATE (Addendum). NOT CLEAN: C122 E-3 / C135 E-1 (G-1); for the Lead: L41 (G-7); for CHECKER: G-4 (N-1), G-2 and the
  UPDATE procedure (G-U).
- (L-3 SHAPE, by script) L-3 is one line: 2,765 bytes and 2,714 characters with its newline, 38 «(» / 38 «)», depth never negative,
  final depth 0, 0 "|", one « — », «R1xx» 0, «(DATA: » 0, «(DATA, » 0, «DATA (» once, «; hence » once, «; and (» once, no guillemet.
(0) PLACEMENT. RESULTS at the local trunk c8f42538: sha1 66e7119615efa5a0bb25b898e32b5b371c55c122, 14,962 lines; "### R122" 0 times in
  RESULTS and GAPS. PROPOSED (R102's to R121's layout): insert R122's entry, with one blank line after it, directly before «**Erratum
  E-1**», after the blank line that follows R121's block (G-P). Simulation: Addendum (7).
(1) TITLE. The title is the line file docs/si/P-ACYC-line-L3.txt (l-si ff9b1639, 2026-11-08T03:35:20Z, the file's only commit, sha1
  03453361fead881493e2d2786b869f1c63158c4c, 2,765 bytes with the newline; byte-equal at the l-si head 9177e274), verbatim: NOTHING is
  stripped and NOTHING is inserted: "### R122 [refereed-only] ", then the file without its newline, then ", CHECKER PASS
  (docs/checker/C136.md, checker PENDING)" (as R90-R121). Built by script and re-checked after writing (chk122.py): equal.
(2) LINE HISTORY: three lines. L-1 bb12deec (e3ac4b06, the freeze; 2,085 bytes, 27 «(» / 27 «)»; REFEREE NOT YET: AC-L1..AC-L5;
  REFEREE-2 «**MATCHES after W-3 and D-1, D-2**», l. 26). L-2 3a3096a4 (01a68edc, fixes entry 1; 2,741 bytes, 38 / 38): L-1 with five
  replacements (AC-L1; AC-L2; AC-L3; W-3 (a) + D-1 ⊃ AC-L4 as one; AC-L5 = D-2 + D-3), REFEREE MATCHES (§C), REFEREE-2 NOT YET on D-5
  (Add. 2). L-3 03453361 (ff9b1639, fixes entry 2; 2,765 bytes, 38 / 38): L-2 with D-5 only, «along N5′-xi on Γ3 from S3 (pacyc81.py),»
  → «along N5′-xi on Γ3 from S3 (pacyc81.py; τ by fix1/pacyc81t.py),», old string once in L-2, new string once in L-3, L-2 + D-5 = L-3
  (True, my script; REFEREE by scratch/acyc_l3.py, REFEREE-2 by bt_l3.py).
(3) THE LINE AT BOTH REFEREES. REFEREE: report a9d4e44e (= d3d0a600; successor 28; L-1 NOT YET, l. 17), §C c865da81 (L-2 MATCHES, l.
  328), §D 17c81b70 + d4423d6d (L-3 MATCHES, l. 348). REFEREE-2: report bf02e618 (successor 32; L-1 «MATCHES after W-3 and D-1, D-2»,
  l. 26), Add. 1 6c937bc6 (comparison), Add. 2 d7ca68f4 (L-2 NOT YET: D-5, l. 352), Add. 3 e1878470 (L-3 MATCHES, l. 373).
(4) CLAIMS SIGNED = the four statement rows of both verdict tables (REFEREE l. 11-14; REFEREE-2 l. 18-21): BETA-ACYC SIGN at both from
  the first round; LAMBDA-CONST SIGN WITH GAP at both in the first round (LC-1 = G-1), SIGN after fixes entry 1 at both; ACYC-LIN and
  ACYC-XI SIGN WITH GAP LC-1 (inherited) at REFEREE and SIGN at REFEREE-2 in the first round, SIGN at both after entry 1; ACYC-XI
  PROVED-CONDITIONAL on R118 (k), (l) throughout. Not signed: §5 (READING), §6 (DATA), §7 (TARGET diff), the first-fallback definition
  (checked CORRECT against SPEC, not a statement).
(5) OTHER TEXTS THE ENTRY DEPENDS ON: RESULTS R104 (definitions), R117 (Γ3's definition; [REACH-L] for the corollary through R118 (k)),
  R118 (a), (d), (k), (l), [VJ], R15's object (SPEC S4, S4c); the 300 + 4 + 5 genomes and the box 81 tools (L-SI 43-44); the runners in
  box81/ref/ (byte copies of L-NEW's, pinned by ref.sha1).
(6) PREMISE LABELS: G-4.
(7) SYMBOL TEST: G-2 (ii).
(8) FIXES AND STATUS NOTES: G-14; body Fixes.
(9) GAPS: G-N5-TIME (GAPS l. 11) stays open; L-3 states no CONJECTURE and kills no statement («P-ACYC», «ACYC-LIN» 0 times in GAPS). A
  line-11 UPDATE is proposed at the end, BUILT FROM L-3 AS IT STANDS (upd122.py: r121/tools/upd121.py exec'd unchanged but for its file
  write: R97's to R116's LANDED UPDATEs rebuilt from their lines and compared with GAPS l. 11 byte for byte, True ×20; R117, R118, R119 and
  R120 as landed, True ×4; all controls True ×24, the last UPDATE on l. 11 R120's; then the R121 control, NOT landed: run121 on P-N5-ASC
  L-2 = R121-draft.md d[491] (6635b14e, True) and, with C135 §5's R1-R4, = C135's L-3 UPDATE f545cba7 (True); then R122 (G-U)).
(10) DATA of record = packet §6 with fixes entries 1-2 (F-5, F-6, F-8), NOT signed; L-3's DATA states its counts (G-9). Re-run (a): PASS.
(11) Discrepancies, recorded for CHECKER, no verdict affected: D-1 the brief and fixes l. 4 cite REFEREE's report as d3d0a600; the
  report was committed at a9d4e44e (00:48:22Z) and d3d0a600 (00:48:27Z) changes notes/REFEREE.md only (the file is byte-equal at both).
  D-2 REFEREE §D's heading first read «04:05Z» at 17c81b70 (04:03:49Z), after the commit time; d4423d6d corrects it to «04:03Z» (the C132
  Add. 1 class, fixed by its author). D-3 the packet's header «Written 2026-11-07 from 22:33Z (date -u: see the commits)»: commit
  e3ac4b06 22:38:10Z. D-4 REFEREE-2 l. 6-7: «The lane's message said 6b699f93; that is not the file's hash (the Lead's brief already
  corrected it).» (history; the pin and both referees agree on 0e9edcfd). D-5 L-3's source note (G-1). D-6 the packet's AC-6 sentence
  («Γ(G′) = Γ(G), since the start enters no priority of Γ») is about Γ only; REFEREE-2 Add. 2 l. 332-333: «on Γ3 the m-pads' priorities
  do depend on the start, but AC-6 is said of IDEAL-CYC on Γ.» (ACYC-LIN is stated on IDEAL-CYC(G) only; no gap).
(12) Excluded: box 81's bridge material other than the packet (docs/si/box81-bridge.md, census81.py, real81.py, xchk81.py, the census
  and real-runner outputs: check81.sh runs them, the line cites none), boxes 82-84 (LADDER-R, LOCK-UP, HUB PAIR MIRROR, LIVE-BREAK,
  LOWER-BLIND: lane items, unrefereed), the packet's §5 READING beyond the line's tail, REFEREE-2's set R2 and random-σ data and REFEREE's
  random-start and T_CYC ≤ d + 1 data (referee data, «This is DATA only, no claim.», REFEREE l. 158). Not part of this entry.
(13) Commits: lane (claude/l-si): e3ac4b06 (2026-11-07T22:38:10Z; packet FROZEN, L-1, box81 check; L-SI successor 43), 01a68edc
  (2026-11-08T02:10:34Z; fixes entry 1, L-2, fix1/; successor 44), ff9b1639 (03:35:20Z; fixes entry 2, L-3, fix2/; successor 44), other
  work between and after (2a44b7d6, 4cfc7510, 83d49640, 9177e274: boxes 83-84). REFEREE: a9d4e44e (= d3d0a600) → c865da81 → 17c81b70 →
  d4423d6d. REFEREE-2: bf02e618 → 6c937bc6 → d7ca68f4 → e1878470. CHECKER: docs/checker/ ends at C135.
(14) DEAD-ENDS ROWS: NONE (no statement killed; AC-2's «attained» correction is packet text, not a statement).

### R122 [refereed-only] Odd never leaves the β-face on Ξ-acyclic genomes (premises: R104's definitions of the genome, the Ξ-graph, Γ(G) and its start only; R117's definition of Γ3(G) only; R118 (a) definitions, (d) BR-SEG, and for the corollary (k) REACH3-CYC with (l) Corollary T3; the order ⊴ and σ̄ of R118 [VJ], an optimal counterstrategy being pointwise optimal (at every vertex its play value is ⊴ the value under every Odd strategy; RESULTS R57 (b), [1E-N3], as landed in R104); for the corollary's iterations and fallback, SPEC S4 and S4c, RESULTS R15's object): (Lemma BETA-ACYC) for every genome G whose Ξ-graph is acyclic, on Γ(G) or Γ3(G), and every Even strategy that agrees with the stated start off the movers (transported through the pads on Γ3), every optimal counterstrategy of Odd takes the β-face at every gate, and no play from a non-e vertex contains an e-vertex; (Lemma LAMBDA-CONST) every vertex's cycle node is then independent of the movers' choices; hence (Theorem ACYC-LIN) the Howard run of IDEAL-CYC(G) from any mover state has C = 0, R = 0 and T_CYC ≤ N; and (Corollary ACYC-XI, PROVED-CONDITIONAL on R118's REACH3-CYC, whose [REACH-L] premises RESULTS R117's entry signs for acyclic Ξ-graphs, with Lemma K2-r and [1E-N3] as listed in R118 (k)) the first fallback of N5′-xi on Γ3(G) from S3, i.e. the least iteration k at which SPEC S4c applies, comes at k = T3 + 1 ≤ N + 1 (2026-11-07) — so on the whole domain of the tower route N5′-xi's mover phase is linear in N, while N5 with SPEC's S4a tie rule realises L(G) there (R117); nothing is claimed about iterations after the first fallback, about Ξ-cyclic genomes, or about the running time of N5 or N5′-xi (no bound on R for Ξ-cyclic genomes; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim); the step w* = K1 of LAMBDA-CONST's proof (σ̄(K2) toward K1 is Odd's unique optimum) is referee-originated (REFEREE R-P-ACYC §4.2 LC-1 and REFEREE-2 R2-P-ACYC G-1 / W-1, found independently, restated in P-ACYC's fixes entry 1 F-1), signed by both referees; DATA (experiments/si/box81, check81.sh): on 300 random Ξ-acyclic genomes (lemma81.agen, d 1-6, w 1-3, degree 2-3, seed 7; 768 states) and the four tower genomes H5_d20_F62, H6_d24_F126, SL41_d28, L6Z_KILL238_d28 (44 states), each run from the genome's stored start (IDEAL-CYC) or from S3 (Γ3), σ̄ off the β-face in 0 (state, gate) pairs (BETA-ACYC's no-e-vertex clause: no separate DATA), C 0, R 0, runs with T_CYC > N 0 (lemma81.py, IDEAL-CYC; ACYC-LIN from other mover states: no separate DATA) and, along N5′-xi on Γ3 from S3, on its states 0, …, T3 before the first fallback (pacyc81.py; τ by fix1/pacyc81t.py), σ̄ off the β-face 0, states that are not standard (σ off the movers and τ) 0, genomes with no fallback 0, genomes with first fallback after iteration N + 1 0 (k = T3 + 1 is R118 (k)'s own clause, and N5's L(G) is R117's: no separate DATA); control, five Ξ-cyclic genomes rd2_d3, rd2_d4, rd3_d3, rf_d4, RS2 (59 states; the same counts on IDEAL-CYC and on N5′-xi's states 0, …, T3 on Γ3; e-priorities ordered by (lev, gate index), as in ref gamma3.build): σ̄ off the β-face in 121 (state, gate) pairs, C 15, R 25 (P-ACYC, docs/si/P-ACYC.md with its fixes entries 1-2, docs/si/P-ACYC-fixes.md; L-SI successors 43-44), CHECKER PASS (docs/checker/C136.md, checker PENDING)
- Object (L-SI successors 43-46, D18 / D14 / D1, box 81; frozen, unchanged during review): packet P-ACYC, docs/si/P-ACYC.md, sha1
  0e9edcfda3e3a68dee63ff01427d526b14c67bc4, 193 lines, 16,852 bytes (l-si e3ac4b06, 2026-11-07T22:38:10Z, the file's only commit;
  identical at 01a68edc, ff9b1639, 0bc6f028 and 358ede16, the l-si head; pinned in experiments/si/box81/pacyc.sha1). Both referees
  measured it (REFEREE l. 26-27 «docs/si/P-ACYC.md: sha1 0e9edcfda3e3a68dee63ff01427d526b14c67bc4, 16,852 B» … «This EQUALS the brief.»;
  REFEREE-2 l. 6 «docs/si/P-ACYC.md 0e9edcfda3e3a68dee63ff01427d526b14c67bc4 (16,852 B), as pinned in experiments/si/box81/pacyc.sha1.»).
  Labels (l. 4-5): «PROVED (L-SI 43, unrefereed) / PROVED-CONDITIONAL (on named landed premises) / DATA / READING (not to sign).». To sign
  (l. 13-20): §2 Lemma BETA-ACYC (on Γ(G) and on Γ3(G)), Lemma LAMBDA-CONST; §3 Theorem ACYC-LIN; §4 Corollary ACYC-XI,
  «PROVED-CONDITIONAL on R118 (k) REACH3-CYC with (l) Corollary T3»; §5-§6 «definitions / DATA / READING (not to sign)». The packet's own
  scope (l. 5): «Not a TARGET.md claim; not M3; not a gauntlet step; G-N5-TIME stays OPEN.».
  Fixes: docs/si/P-ACYC-fixes.md, append-only, four entries, entries 1-2 by L-SI successor 44, entry 3 by L-SI successor 45 and entry 4 by
  L-SI successor 46 (358ede16: 163 lines, 15,987 bytes, sha1 165355113b7b12c40856ecc2c4a06ef296609fdd; its first 13,468 bytes are the file
  at 0bc6f028, entries 1-3, 136 lines, sha1 ae03871f8eb064a5a4c8d99063dbef8e88264a73; its first 11,487 bytes are the file at ff9b1639,
  entries 1-2, sha1 c782b15ba07ef921a54963ab198c8ae73129a67f, and its first 10,104 bytes are entry 1's file, by cmp). Entry 1 (01a68edc,
  2026-11-08T02:10:34Z; the file then 97 lines, 10,104 bytes, sha1 dd3d4546f12f11b9fd4848c5ab13739ac814fb5d): F-1 = LC-1 = W-1
  (LAMBDA-CONST: w* = K1, σ̄(K2) unique; ACYC-LIN's K2 step), F-2 = AC-2 («attained» corrected), F-3 = AC-3 = W-2 (a)-(c) (scope
  sentences), F-4 = AC-4 = W-2 (d), F-5 = W-3 (a) + D-1 + AC-L4 (the τ counter, «no fallback»), F-6 = AC-L5 = D-2 + D-3 (the control
  clause), F-7 = AC-L1..AC-L3 (line) + N-1 (packet only), F-8 = D-4, F-9 = AC-5, AC-6, line L-2. Entry 2 (ff9b1639, 2026-11-08T03:35:20Z,
  l. 99-114): F-10 = D-5 (the Γ3 clause names fix1/pacyc81t.py), F-11 = N-2 = AC-7 (packet header only), line L-3. Entry 3 (0bc6f028,
  2026-11-08T05:54:32Z, l. 116-136): F-12, the Lead's G-7 ruling under L41 (the line names the referee-originated w* = K1 step), and F-13,
  the Lead's G-1 ruling (the source note names fixes entries 1-2 and L-SI successors 43-44), line L-4; «G-4 is left to CHECKER.» (l. 120).
  Entry 4 (358ede16, 2026-11-08T15:55:24Z, l. 138-163): F-14 = R1 (CHECKER C136 E-1: the pointwise sense of «optimal» stated in the line)
  and F-15 = R2 + R3 (C136 E-2: the set of the Γ3 counts stated in the line), C136's exact strings (§5 l. 84-89), line L-5; «The packet
  P-ACYC.md and lines L-1 to L-4 are not edited.» (l. 141). «LC-1 / W-1, AC-2, AC-3 / W-2, AC-4, D-4, AC-5, AC-6 change packet text only.»
  (l. 97). Entry 1 carries the w* = K1 step of LAMBDA-CONST's proof (see L41 and L43) and AC-6; entries 2, 3 and 4 carry no proof.
  The RESULTS line is L-5, 7a84e0944b0f33ce4d569604bec41d6e9236d82f (docs/si/P-ACYC-line-L5.txt, l-si 358ede16, 2026-11-08T15:55:24Z, the
  file's only commit; 3,321 bytes; the l-si head). The title is L-5 verbatim, with nothing inserted and nothing stripped (its date
  parenthesis «(2026-11-07)», its scope tail with the referee-originated step, and its source note are the line's own). L-5's parentheses
  balance (43 «(» / 43 «)»). Line history: L-1 (bb12deec6fb0129b4ea9f5af7dd96d6302c5ca50, 2,085 bytes, e3ac4b06, the freeze); L-2
  (3a3096a4, 01a68edc, fixes entry 1: L-1 with five replacements, AC-L1, AC-L2, AC-L3 verbatim, REFEREE-2's W-3 (a) + D-1 string
  containing AC-L4 as one, AC-L5 with D-3's insertion); L-3 (03453361, ff9b1639, fixes entry 2: L-2 with D-5 only, «along N5′-xi on Γ3
  from S3 (pacyc81.py),» → «along N5′-xi on Γ3 from S3 (pacyc81.py; τ by fix1/pacyc81t.py),»); L-4 (85bb221f, 0bc6f028, fixes entry 3: L-3
  with F-12 then F-13, each old string once in the running line; F-12 puts «the step w* = K1 of LAMBDA-CONST's proof (σ̄(K2) toward K1 is
  Odd's unique optimum) is referee-originated (REFEREE R-P-ACYC §4.2 LC-1 and REFEREE-2 R2-P-ACYC G-1 / W-1, found independently, restated
  in P-ACYC's fixes entry 1 F-1), signed by both referees;» into the scope tail before «DATA (experiments/si/box81, check81.sh):», and
  F-13 replaces «(P-ACYC, docs/si/P-ACYC.md; L-SI successor 43)» by «(P-ACYC, docs/si/P-ACYC.md with its fixes entries 1-2,
  docs/si/P-ACYC-fixes.md; L-SI successors 43-44)»); L-5 (7a84e094, 358ede16, fixes entry 4: L-4 with CHECKER C136's R1, R2 and R3 in that
  order, each old string once in the running line; R1 (F-14) replaces «the order ⊴ and σ̄ of R118 [VJ];» by «the order ⊴ and σ̄ of R118
  [VJ], an optimal counterstrategy being pointwise optimal (at every vertex its play value is ⊴ the value under every Odd strategy;
  RESULTS R57 (b), [1E-N3], as landed in R104);», R2 (F-15) puts «, on its states 0, …, T3 before the first fallback» after «along N5′-xi
  on Γ3 from S3» in the Γ3 DATA clause, and R3 (F-15) replaces «the same counts on IDEAL-CYC and along N5′-xi on Γ3;» by «the same counts
  on IDEAL-CYC and on N5′-xi's states 0, …, T3 on Γ3;» in the control). L-2 + D-5 is L-3 (my script, True; REFEREE by its own
  scratch/acyc_l3.py, §D l. 338-342; REFEREE-2 by its own bt_l3.py, Add. 3 l. 360-363). L-3 + F-12 + F-13 is L-4 (by script, True; the
  lane's fix3/mkL4.py, which asserts L-3's sha1, re-run from a git archive of 0bc6f028: output cmp-equal to L-4; fix3/check_fix3.sh makes
  the same cmp inside check81.sh). L-4 + R1 + R2 + R3 is L-5 (by script, True; the lane's fix4/mkL5.py, which asserts L-4's sha1 and each
  old string once, re-run from a git archive of 358ede16: output cmp-equal to L-5; fix4/check_fix4.sh makes the same cmp inside check81.sh
  and checks L-5's sha1 against C136's). L-1: REFEREE «NOT YET: AC-L1 to AC-L5 required (premises; DATA scope, units and sets)» (l. 17,
  the L-1 row); REFEREE-2 «**MATCHES after W-3 and D-1, D-2**; W-1 and W-2 are packet text, not line text» (l. 26). L-2: REFEREE «Verdict:
  fixes entry 1 CORRECT. L-2 MATCHES, by the byte test and in meaning.» (§C l. 328); REFEREE-2 «**L-2 does NOT yet match: D-5** (the τ
  clause's tool citation; one string) (Opus 5.5, D1).» (Add. 2 l. 352). L-3 MATCHES at both referees, each after its own byte test:
  REFEREE successor 28 (17c81b70, 2026-11-08T04:03:49Z; heading time fixed at d4423d6d) §D l. 338-342 («The old string occurs once in L-2
  and 0 times in L-3; the new string occurs once in L-3.»; «L-2 + D-5 is byte-equal to L-3 (sha1 03453361…).»), l. 345-346 («D-5 (F-10):
  CORRECT. pacyc81.py counts σ only. The τ half of «states that are not standard (σ off the movers and τ) 0» is fix1/pacyc81t.py's
  taubad.»), l. 348 «Verdict: fixes entry 2 CORRECT; L-3 MATCHES. All statements stay as in §C (all SIGN; ACYC-XI PROVED-CONDITIONAL on
  R118 (k), (l)).»; REFEREE-2 successor 32 (e1878470, 2026-11-08T04:06:09Z) Addendum 3 l. 360-363 («Rebuild L-2 + D-5 = L-3 byte for byte
  (03453361…). Nothing else changed.»), l. 364-365 (its re-run of check81.sh on a git archive of ff9b1639, «box 81 checks: PASS», exit 0),
  l. 369-370 (the DATA rule on L-3), l. 371-374 «fixes entry 2 **CORRECT**;» … «**L-3 MATCHES** (Opus 5.5, D1);» … «statements: BETA-ACYC,
  LAMBDA-CONST, ACYC-LIN **SIGN**; ACYC-XI **SIGN**, PROVED-CONDITIONAL on R118 (k) + (l); nothing REFUSED.». L-4: REFEREE successor 29
  (055758ba, 2026-11-08T06:31:48Z) §E l. 349-378, own scratch/acyc_l4.py: «R-G and R-B old strings: once each in L-3, 0 in L-4. New
  strings: 0 in L-3, once each in L-4.», «L-3 + R-G + R-B in order is byte-equal to L-4.» (l. 356-357), F-12 and F-13 read in meaning (l.
  360-376), «Verdict: L-4 MATCHES (L-3 + exactly R-G and R-B; both CORRECT in meaning). All statements of P-ACYC stay SIGN (ACYC-XI
  PROVED-CONDITIONAL, as before).» (l. 377-378). REFEREE-2 successor 33 (79430e80, 2026-11-08T06:38:24Z) Addendum 4 l. 376-406, own
  bt_l4.py: «R-G and R-B: each old string occurs once in L-3 and 0 times in L-4; each new string 0 times in L-3 and once in L-4.», «The
  rebuild L-3 + R-G + R-B is 85bb221f…, 3,080 B, which is L-4 byte for byte, so nothing else changed.» (l. 381-382), F-12 and F-13 read in
  meaning (l. 384-402), «**Verdict: L-4 MATCHES** (Opus 5.5, D1). Statement verdicts unchanged: all SIGN (ACYC-XI PROVED-CONDITIONAL on
  R118 (k), (l), as before).» (l. 405-406). L-5: REFEREE successor 30 (5b2aa604, 2026-11-08T16:44:19Z; R1's proof-use sentence and
  pacyc81.py's line numbers corrected at ae980555, 16:44:42Z) §F l. 380-411, own scratch/acyc_l5.py with the strings «typed from C136 §5
  (claude/checker b2fe3440 l. 84-89; wrapped lines joined with one space), not from the lane's script» (l. 384-385): «Each old string once
  in L-4.», «`cmp` with the lane's L-5: **EQUAL**» (l. 385-386), R1 read against packet §1 l. 69 and R2 / R3 against pacyc81.py (l.
  388-406), «Verdict: fixes entry 4 CORRECT. **Line L-5 MATCHES** (L-4 + exactly R1-R3). Statements as signed (§0 and §C-§E).» (l. 410).
  REFEREE-2 successor 35 (c1e71a25, 2026-11-08T16:43:45Z) Addendum 5 l. 408-427, own bt_l5.py with «CHECKER 22's strings, verbatim from
  C136.md l. 84-89 at claude/checker b2fe3440» (l. 412-413): «**L-5 == L-4 + R1 + R2 + R3: True.** Nothing else changed.» (l. 414), R1 and
  R2 / R3 read in meaning (l. 415-425), «(4) Verdict: **L-5 MATCHES** (byte test, and in meaning). Statement verdicts unchanged.» (l.
  427).
- Claims signed (REFEREE successor 28: report a9d4e44e (= d3d0a600), §C c865da81, §D 17c81b70 / d4423d6d; successor 29: §E 055758ba;
  successor 30: §F 5b2aa604 / ae980555; REFEREE-2 successor 32: report bf02e618, Addendum 1 6c937bc6, Addendum 2 d7ca68f4, Addendum 3
  e1878470; successor 33: Addendum 4 79430e80; successor 35: Addendum 5 c1e71a25). REFEREE's table («## 0. Verdicts», l. 5-18 of
  R-P-ACYC.md) reads §0 premises «all LANDED on trunk 37a4855e; every quote verbatim and in the entry it names (script)», §1 facts and
  FROZEN FRAME «CORRECT (re-derived from R104's and R117's quoted text)», FIRST FALLBACK «CORRECT against SPEC S4 / S4c (optional AC-5)»,
  Lemma BETA-ACYC on Γ(G) and on Γ3(G) «SIGN», Lemma LAMBDA-CONST «SIGN WITH GAP LC-1 (the proof never fixes w* = K1; with w* = K2 the
  statement would be false at K1; repair below)», Theorem ACYC-LIN «SIGN WITH GAP LC-1 (R = 0 at K2 rests on «a fixed deterministic rule»,
  which needs a unique optimum; repair below). Required data wording AC-2», Corollary ACYC-XI «SIGN as PROVED-CONDITIONAL on R118 (k) and
  (l), WITH GAP LC-1 (inherited; on Γ3 it can also be closed by (k)'s own Lemma K2-r)», §5 READING «header Scope sentence and §5's last
  bullet OVERREACH (AC-3, required text); AC-4 (required, minor)», §6 DATA «every replayed count EQUAL (own engine); check81.sh re-run
  PASS», §7 «CLEAN»; and «LC-1 is a proof gap with a one-line repair. No conclusion changes.» (l. 20). REFEREE-2's table («## Verdicts»,
  l. 13-26 of R2-P-ACYC.md) reads Lemma BETA-ACYC «**SIGN** (Opus 5.5, D1)», Lemma LAMBDA-CONST «**SIGN WITH GAP** (Opus 5.5, D1): G-1,
  the proof never shows w* = K1, and the map is false at K1 (and s on Γ3) unless w* = K1; my one-line repair closes the gap (W-1,
  required)», Theorem ACYC-LIN «**SIGN** (Opus 5.5, D1)», Corollary ACYC-XI «**SIGN** (Opus 5.5, D1), conditional as labelled», the scope
  sentence and READING over-reach (W-2), §6 «every count reproduced exactly (own simulator, plus lane runners on a git archive); W-3 (the
  «non-standard» counter tests σ only), D-1 to D-4», §0 «✓ all LANDED on trunk; 27 of 27 premise quotes verbatim by script», §7 «✓», and
  «Nothing is REFUSED. No statement bounds N5′-xi's total iterations or N5's; G-N5-TIME stays OPEN.» (l. 27). The one SIGN WITH GAP (LC-1
  = G-1, with ACYC-LIN and ACYC-XI inheriting it at REFEREE) is closed by fixes entry 1 F-1 at both referees: REFEREE §C l. 297-301 («F-1
  (LC-1): CORRECT.»; «LC-1 is CLOSED for LAMBDA-CONST, ACYC-LIN and ACYC-XI.»), REFEREE-2 Add. 2 l. 315 («F-1 (W-1 = LC-1): my text
  verbatim, plus the ACYC-LIN K2 line ✓. This closes G-1, so LAMBDA-CONST is now **SIGN**.»). Every other required item (AC-2, AC-3, AC-4,
  AC-L1..AC-L5; W-2, W-3, D-1, D-2; then D-5) was packet text, line text or DATA wording, and each is closed: REFEREE §C l. 328-331
  («Statements: BETA-ACYC SIGN; LAMBDA-CONST SIGN; ACYC-LIN SIGN; Corollary ACYC-XI SIGN as PROVED-CONDITIONAL on R118 (k) REACH3-CYC and
  (l) Corollary T3.»; «No gap remains open. AC-7 is optional (packet wording only; not in L-2).»), REFEREE-2 Add. 2 l. 350-351 («W-1, W-2,
  W-3, D-1, D-2, D-3, D-4 and N-1 **met**;»), REFEREE §D l. 348, REFEREE-2 Add. 3 l. 372-374. No SIGN WITH GAP remains open. Nothing is
  REFUSED. The line round L-4 (fixes entry 3) changes two line strings and no statement, proof or DATA (fixes l. 116-136; REFEREE §E l.
  377-378: «All statements of P-ACYC stay SIGN (ACYC-XI PROVED-CONDITIONAL, as before).»; REFEREE-2 Add. 4 l. 405-406: «Statement verdicts
  unchanged: all SIGN (ACYC-XI PROVED-CONDITIONAL on R118 (k), (l), as before).»). The line round L-5 (fixes entry 4, CHECKER C136's
  R1-R3) changes three line strings and no statement, proof or DATA figure (C136: «No statement, proof or DATA figure changes.», l. 18;
  REFEREE §F l. 410: «Statements as signed (§0 and §C-§E).»; REFEREE-2 Add. 5 l. 427: «Statement verdicts unchanged.»): R1 states in the
  line the sense of «optimal» that packet §1 l. 69 defines and BETA-ACYC's proof uses (C136 E-1, REFEREE-2 N-1), and R2 and R3 state the
  set on which pacyc81.py counts (C136 E-2).
  Setting: IDEAL-CYC(G) of R118 (a) on Γ(G) of R104, and N5′-xi on Γ3(G) of R117 from S3 (R118 (j), (k)), for every genome G whose Ξ-graph
  is acyclic; values (Λ, Π, k), ⊴ and σ̄ as in R118's premises; σ̄ pointwise optimal (packet §1 l. 69-70, with F-7's source RESULTS R57
  (b) [1E-N3] as landed in R104; L-5 states this sense of «optimal» in its premises, R1). Statements as signed (packet with fixes entries
  1-2; entries 3 and 4 change the line only):
  (a) Definitions (§1 l. 61-82): Ξ-ACYCLIC «the Ξ-graph has no directed cycle»; the FROZEN FRAME (σ agrees with the stated start at every
    Even vertex other than the movers, transported through the pads on Γ3; Odd = the gates and K2 is free); the facts [RANK], [CORE], [cX]
    (checked CORRECT by REFEREE l. 69-80 and REFEREE-2 l. 16); FIRST FALLBACK (the least k at which S4c applies; F-9 AC-5: «is the k-th
    iteration of SPEC S4 (one pass with Iσ ∪ Iτ ≠ ∅),»).
  (b) Lemma BETA-ACYC (§2 l. 85-87) [Ξ-acyclic G, H ∈ {Γ(G), Γ3(G)}, σ in the frozen frame]: «Then σ̄ chooses the β-face at every gate g:
    β_g on Γ(G), pβ_g on Γ3(G). Under (σ, σ̄), no play from a vertex other than an e-vertex (or a pad pe_g) contains an e-vertex.», for
    «σ̄ any optimal counterstrategy to σ», optimal in the pointwise sense of packet §1 l. 69 (L-5's R1); the β-face is strictly better for
    Odd (REFEREE l. 111; REFEREE-2 l. 81), so EVERY optimal σ̄ takes it. REFEREE SIGN (l. 11), REFEREE-2 SIGN (l. 18).
  (c) Lemma LAMBDA-CONST (§2 l. 114-119, repaired by F-1) [the hypotheses of BETA-ACYC]: «Under the hypotheses of BETA-ACYC, Λ(v) does not
    depend on σ.»: c_W for c_W and for the e-vertices of level-0 options (and their pe pads), the unused loop for itself, w* for every
    other vertex, and (F-1) «w* = K1 for every σ in the frozen frame.»; the proof's new step (F-1, fixes l. 13-17): «The odd cycle node
    of higher priority is worse for Even, so every optimal σ̄ has σ̄(K2) toward K1, and w* = K1 for every σ (R118's Lemma K2-r).». REFEREE
    SIGN WITH GAP LC-1 (l. 12), then SIGN (§C l. 329); REFEREE-2 SIGN WITH GAP G-1 (l. 19), then SIGN (Add. 2 l. 315, 351).
  (d) Theorem ACYC-LIN (§3 l. 126-133, with F-1's K2 line and F-9's AC-6) [Ξ-acyclic G, every start mover state]: «For every Ξ-acyclic
    genome G and every start mover state, the Howard run of IDEAL-CYC(G) has C = 0 and R = 0, and T_CYC ≤ N.»; R = 0 at K2 by «the unique
    optimal choice, toward K1» (fixes l. 20); T_CYC ≤ N by R118 (d) BR-SEG; F-2 replaces «The bound is attained» by «T_CYC = N occurs in
    set A only at N = 1 (10 runs); over N ≥ 2 the largest T_CYC / N is 0.8 (N 5, T 4).». REFEREE SIGN WITH GAP LC-1 (l. 13), then SIGN (§C
    l. 329); REFEREE-2 SIGN (l. 20, Add. 2 l. 351).
  (e) Corollary ACYC-XI (§4 l. 135-146) [Ξ-acyclic G; PROVED-CONDITIONAL on R118 (k) REACH3-CYC and (l) Corollary T3]: «For every
    Ξ-acyclic genome G, the first fallback of N5′-xi on Γ3(G) from S3 comes at iteration T3 + 1 ≤ N + 1. The mover phase (states 0, …, T3)
    has at most N iterations.»; «Not claimed:» the iterations after the first fallback and the correctness of the output. REFEREE SIGN
    as PROVED-CONDITIONAL WITH GAP LC-1 (inherited) (l. 14), then SIGN (§C l. 329-330); REFEREE-2 SIGN, conditional as labelled (l. 21,
    Add. 2 l. 351).
- The RESULTS line (L-5, the title): «Odd never leaves the β-face on Ξ-acyclic genomes (premises: R104's definitions of the genome, the
  Ξ-graph, Γ(G) and its start only;» … «the order ⊴ and σ̄ of R118 [VJ], an optimal counterstrategy being pointwise optimal (at every
  vertex its play value is ⊴ the value under every Odd strategy; RESULTS R57 (b), [1E-N3], as landed in R104);» … «(2026-11-07) — so on
  the whole domain of the tower route N5′-xi's mover phase is linear in N,» … «(no bound on R for Ξ-cyclic genomes; G-N5-TIME stays OPEN;
  not M3, not a step-4 pass, not a TARGET.md claim); the step w* = K1 of LAMBDA-CONST's proof (σ̄(K2) toward K1 is Odd's unique optimum)
  is referee-originated» … «signed by both referees; DATA (experiments/si/box81, check81.sh):» … «along N5′-xi on Γ3 from S3, on its
  states 0, …, T3 before the first fallback» … «(P-ACYC, docs/si/P-ACYC.md with its fixes entries 1-2, docs/si/P-ACYC-fixes.md; L-SI
  successors 43-44)». Its clauses: the premises (R104, R117, R118 (a), (d), (k), (l), [VJ] with the pointwise sense of «optimal» from R57
  (b) and [1E-N3] as landed in R104, SPEC S4 and S4c as R15's object); BETA-ACYC = (b) with the frozen frame of (a) stated inline;
  LAMBDA-CONST = (c) in the form «every vertex's cycle node is then independent of the movers' choices» (the map and w* = K1 are in the
  entry, not in the line); ACYC-LIN = (d); ACYC-XI = (e) with the first-fallback definition inline and its condition named in the label;
  the scope tail (ACYC-XI read on the tower route's domain with R117's L(G), what is not claimed, and the referee-originated step of L41
  and L43); DATA clause by clause, inline (each count against its counter: lemma81.py, pacyc81.py, fix1/pacyc81t.py and their frozen
  outputs; the Γ3 counts, and the control's, on N5′-xi's states 0, …, T3, the set pacyc81.py counts, docstring l. 4, loop l. 24-29); the
  source note.
- Premise: RESULTS R104's definitions of the genome, the Ξ-graph, Γ(G) and its start only (packet §0 l. 23-33, four quotes verbatim in
  R104's title, l. 9864), no R104 theorem; RESULTS R117's definition of Γ3(G) only (l. 34-36; R117 l. 13362), no R117 theorem except
  through R118 (k); RESULTS R118 (a) IDEAL-CYC(G), the Howard step, T_CYC and the labels C, R, p (l. 13677-13681), (d) BR-SEG (l. 13689:
  «If Λ and σ̄ are constant on the states a, a+1, …, a+j+1 and the step a+j → a+j+1 changes σ, then j ≤ N − 1.»), and for the corollary
  (k) REACH3-CYC (l. 13704-13715) and (l) Corollary T3 (l. 13716-13719: «the first fallback of N5′-xi on Γ3(G) comes at iteration T3 +
  1.»); R118's value order ⊴ and σ̄ (VJ00 §4.2 / Friedmann arXiv 1106.0778 §3, R118's premises), with «optimal» in the pointwise sense
  cited from RESULTS R57 (b) and [1E-N3] as landed in R104 (R57 l. 2893; R104's title, l. 9864: «S1's σ̄, and τ̄ on the dual game, are
  pointwise optima»), for the word's sense and the existence of a pointwise optimum only (both referees read R1's citation: REFEREE §F l.
  394-397, REFEREE-2 Add. 5 l. 419-422); SPEC S4 and S4c (docs/new/N5-ssi-global.md l. 50, 56-57; RESULTS R15's object, R15 l. 624). «Not
  used: every theorem of R104 and R117; R118 (b), (c), (e)-(j) except the definitions quoted; every lane note.» (packet l. 59). Both
  referees checked every premise quote against RESULTS at 37a4855e (REFEREE l. 46-61, acyc_quotes.py; REFEREE-2 l. 29-40, r2q.py), which
  equals RESULTS at the trunk commits c9591e35, 616941eb and 36c183f8 (sha1 66e7119615efa5a0bb25b898e32b5b371c55c122, git diff --quiet;
  R104 l. 9864, R117 l. 13362, R118 l. 13607 at each); RESULTS at the local trunk a4a777de (sha1 04a444ee05569591d3b44c981e35af1b33cf37b5,
  15,386 lines, = 59dacf22's, where R121 landed) is that file with R121's block and its blank line (l. 14320-14743) inserted and nothing
  else (by script), so every premise stands at the same line (R15 l. 624, R57 l. 2893, R104 l. 9864, R117 l. 13362, R118 l. 13607). The
  corollary's condition: R118 (k) is PROVED-CONDITIONAL on [REACH-L], which R117's entry signs for IDEAL-ACYC, the Ξ-acyclic case (R118 l.
  13707-13709), with Lemma K2-r (R118's entry, referee-originated there and signed by both referees) and [1E-N3] (RESULTS R57 (b) as
  landed in R104); REFEREE-2 l. 37-38: «So on the packet's domain, the only conditions left on (k) are R117's lemmas as signed in its
  entry, and the standing SPEC premise.».
- L41 and L43. The packet's proofs are L-SI successor 43's (packet l. 3-4, «This packet carries every proof in full and is checked against
  this text only.»), with one referee-written step: w* = K1 in LAMBDA-CONST. The packet left w* open («Its cycle node is w* := K1 if
  σ̄(K2) leads to K1, else K2.», l. 96) and argued by a fixed deterministic rule (l. 123-124); with w* = K2 the map would be false at K1
  (REFEREE l. 122-125; REFEREE-2 l. 86-88). Both referees wrote the same repair independently in their first reports (REFEREE l. 129-134,
  «Repair (one line, from §0 only):», «Hence σ̄(K2) is unique: K1 on Γ, r on Γ3 (the cycle K1 → s → K1 has node K1).»; REFEREE-2 l. 89-91
  and W-1 l. 93-102, «So every optimal σ̄ has σ̄(K2) toward K1 (K1 on Γ, r on Γ3), and w* = K1.»; REFEREE-2 Add. 1 l. 260: «LAMBDA-CONST:
  both find the same gap: REFEREE's LC-1 is my G-1. The repair is the same line (K1 beats K2 for Odd, so w* = K1; K2-r).»); fixes entry 1
  F-1 restates REFEREE-2's text («New (REFEREE-2's text, which also carries REFEREE's uniqueness point)», l. 13). The step is R118's
  landed Lemma K2-r in substance (REFEREE l. 134: «This is R118 (g)'s O-1 sentence and Lemma K2-r. The repair re-proves it, so no new
  premise is needed.»). The Lead ruled that L41 (DECISIONS l. 355-358) applies («Lead rulings: G-7 L41 APPLIES (w* = K1 required referee
  repair, both SIGN WITH GAP; R119 precedent)», LEAD-STATE l. 2754; fixes entry 3: «G-7 = L41 applies (the w* = K1 step of LAMBDA-CONST's
  proof is a REQUIRED referee-originated repair», l. 118), and the scope tail of L-4 and of L-5 carries the sentence (F-12): «the step w*
  = K1 of LAMBDA-CONST's proof (σ̄(K2) toward K1 is Odd's unique optimum) is referee-originated (REFEREE R-P-ACYC §4.2 LC-1 and REFEREE-2
  R2-P-ACYC G-1 / W-1, found independently, restated in P-ACYC's fixes entry 1 F-1), signed by both referees». REFEREE §E read that
  sentence part by part against §4.2 LC-1 and found each part «CORRECT» (l. 360-370); on «signed by both referees» it writes «this report
  §C signs LAMBDA-CONST with F-1. REFEREE-2's signature is as the Lead records it for R122. I did not re-read docs/referee-2/ for this.»
  (l. 371-372), so REFEREE-2's signature is quoted here from REFEREE-2's own file. REFEREE-2 Add. 4 checked the same sentence: «**R-G's
  citation of my predecessor's G-1 / W-1: correct.**» (l. 384), «**«σ̄(K2) toward K1 is Odd's unique optimum»: correct**, read as Odd's
  choice at K2.» (l. 393). The two signatures: REFEREE, who wrote LC-1 and its repair without reading REFEREE-2 («I did NOT read
  docs/referee-2/ for this report.», l. 3), signs the step as restated («F-1 (LC-1): CORRECT.», §C l. 297; «LC-1 is CLOSED for
  LAMBDA-CONST, ACYC-LIN and ACYC-XI.», l. 301; «Statements: BETA-ACYC SIGN; LAMBDA-CONST SIGN; ACYC-LIN SIGN; Corollary ACYC-XI SIGN as
  PROVED-CONDITIONAL on R118 (k) REACH3-CYC and (l) Corollary T3.», l. 329-330); REFEREE-2, who wrote G-1 and W-1, the text of record,
  without reading REFEREE («Independent: docs/referee/ not read on this item before this report is on origin.», l. 2-3), signs it («F-1
  (W-1 = LC-1): my text verbatim, plus the ACYC-LIN K2 line ✓. This closes G-1, so LAMBDA-CONST is now **SIGN**.», Add. 2 l. 315). The
  joint gap map: one gap, the same at both referees (REFEREE LC-1 = REFEREE-2 G-1, in LAMBDA-CONST's proof; at REFEREE also in ACYC-LIN's
  R = 0 at K2 and, inherited, in ACYC-XI: «SIGN WITH GAP LC-1», l. 12-14; at REFEREE-2 in LAMBDA-CONST only: «**SIGN WITH GAP** (Opus 5.5,
  D1): G-1», l. 19), closed by F-1 at both (above); no other gap at either referee in any round («No gap remains open.», REFEREE §C l.
  331; «nothing REFUSED.», REFEREE-2 Add. 3 l. 374); open gaps: none. AC-6 (F-9), REFEREE's optional sentence in ACYC-LIN's proof, is not
  L41's case («G-7 (ii) AC-6 NOT L41», LEAD-STATE l. 2754; «AC-6 (F-9) is not L41's case», fixes l. 119): both referees read the
  unrepaired proof as complete for every start mover state, by R118 (d). L43: every statement is exact (C = R = 0, T_CYC ≤ N, k = T3 + 1 ≤
  N + 1), on a restricted class; no statement is killed.
- Fixes (docs/si/P-ACYC-fixes.md, append-only; entries 1-2 by L-SI successor 44, entry 3 by L-SI successor 45, entry 4 by L-SI successor
  46; entry 1 at 01a68edc, l. 3-97, under «Lead 01:22Z and 01:39Z» (l. 3); entry 2 at ff9b1639, l. 99-114, under «Lead 03:06Z» (l. 99);
  entry 3 at 0bc6f028, l. 116-136, under «ruled in by the Lead 05:13Z» (l. 116); entry 4 at 358ede16, l. 138-163, under «routed by the
  Lead 15:52Z» (l. 138)):
  - F-1 = LC-1 = W-1 (required): LAMBDA-CONST's «w* does not depend on σ.» → «w* = K1 for every σ in the frozen frame.»; the K2 step of
    its proof (REFEREE-2's text); ACYC-LIN's «at K2 the same choice (LAMBDA-CONST's proof).» → «at K2 the unique optimal choice, toward K1
    (K1 on Γ, r on Γ3; LAMBDA-CONST's proof as repaired in F-1).»; «The last proof sentence («Under a fixed deterministic rule it is the
    same in every state.») stays and is now redundant» (l. 18).
  - F-2 = AC-2 (required): «attained» corrected (tn81.py, tn81.out: «set A: runs with T = N 10 (all at N = 1: True); max T/N over N >= 2:
    0.800»).
  - F-3 = AC-3 = W-2 (a)-(c), F-4 = AC-4 = W-2 (d) (required): the header and §5 scope sentences, the two referees' texts reconciled
    («C + R» taken); packet READING text, not in the line.
  - F-5 = W-3 (a) + D-1 + AC-L4, F-6 = AC-L5 = D-2 + D-3 (required, D-3 recommended): fix1/pacyc81t.py (taubad), the L-2 strings.
  - F-7 = AC-L1..AC-L3 (required, line) + N-1 (recommended, packet only); F-8 = D-4 (2 iterations after the first fallback on 300 of 300,
    4 of 4 and 5 of 5); F-9 = AC-5, AC-6 (optional, taken).
  - Entry 2: F-10 = D-5 (required: the Γ3 clause names fix1/pacyc81t.py for τ), F-11 = N-2 = AC-7 (recommended; the header's parenthesis
    «(at most N iterations; its first fallback comes by iteration N + 1)»); line L-3.
  - Entry 3: F-12 (G-7 = L41, required), the L41 sentence in the scope tail (L41 and L43, above; l. 125-129); F-13 (G-1, required),
    «(P-ACYC, docs/si/P-ACYC.md; L-SI successor 43)» → «(P-ACYC, docs/si/P-ACYC.md with its fixes entries 1-2, docs/si/P-ACYC-fixes.md;
    L-SI successors 43-44)» (l. 131-133); line L-4 by fix3/mkL4.py («asserts L-3's sha1 and each Old string once, R-G first, then R-B», l.
    121), compared byte for byte with docs/si/P-ACYC-line-L4.txt by fix3/check_fix3.sh, which check81.sh runs; G-4 left to CHECKER (l.
    120).
  - Entry 4 (CHECKER C136 E-1 and E-2, both required; «line-only», l. 138): F-14 = R1, «the order ⊴ and σ̄ of R118 [VJ];» → «the order ⊴
    and σ̄ of R118 [VJ], an optimal counterstrategy being pointwise optimal (at every vertex its play value is ⊴ the value under every Odd
    strategy; RESULTS R57 (b), [1E-N3], as landed in R104);» (l. 150-152); F-15 = R2 and R3, the Γ3 DATA clause and the control's Γ3
    counts on «states 0, …, T3» (l. 154-158); line L-5 by fix4/mkL5.py («asserts L-4's sha1 and each Old string once; R1, R2, R3 in that
    order», l. 140), compared byte for byte with docs/si/P-ACYC-line-L5.txt and with C136's sha1 by fix4/check_fix4.sh, which check81.sh
    runs (l. 44).
  - Entry 1 changes LAMBDA-CONST's statement wording (w* = K1) and the proofs of LAMBDA-CONST and ACYC-LIN; every other item is packet
    text (READING, a remark after ∎, §6 units), line text or DATA output; entry 2 changes one line string and one READING sentence; entry
    3 changes two line strings and nothing else; entry 4 changes three line strings (R1-R3) and nothing else.
- Not signed: packet §5 (READING), §6 (DATA), §7 (TARGET diff), the scope sentence of the header; box 81's bridge material
  (docs/si/box81-bridge.md, census81.py, real81.py, xchk81.py); REFEREE-2's set R2 and random-σ data and REFEREE's random-start data
  (referee data).
- Referee strengthening (NOT part of this entry; referee checks):
  (i) REFEREE: own acyc_replay.py on successor 26's own VJ engine and Γ / Γ3 builder (l. 34-37), acyc_xi.py along N5′-xi (the lane's
    n5v.py; «I have no second N5′-xi.», l. 39): every §6 count EQUAL (l. 244-256); eplay 0, nonstrict 0, brute force over all Odd
    strategies with 0 value differences on 305 states with M ≤ 12 (l. 112-116); lamfail 0 on 768 + 44 states and 3,842 states from
    random starts (l. 136-137); 1,500 runs from random mover starts, T_gt_N 0, C 0, R 0 (l. 157); taubad 0 on 309 genomes (§C l.
    311-313); 2 iterations after the first fallback on 300 / 300, 4 / 4, 5 / 5 (§C l. 318-319).
  (ii) REFEREE-2: own simulator r2acyc.py (own Γ and Γ3 builder, own VJ valuation, Odd's optimum by policy iteration from two starts,
    brute force for M ≤ 8 or 9, own Howard; l. 141-151): sets A, B, its own R2 (600 genomes) and random σ on Γ and Γ3, notbeta,
    nonstrict, lamfail, w* ≠ K1, C, R, T > N all 0 (l. 156-163); «brute_noopt 0, brute_valdiff 0, pi_startdep 0 and howard_ties 0
    everywhere» (l. 165); the control under both e-orders (l. 169-176); the lane's pacyc81 with its own τ counter (l. 177-182).
- Honest limits: (i) Nothing here bounds N5′-xi's total iterations, N5's, a running time or a bit cost; the iterations after the first
  fallback are not bounded (DATA only: 2 on every genome of §6), and games not of the form Γ(G) or Γ3(G) are not covered. (ii) Every
  statement is for Ξ-acyclic genomes only; on Ξ-cyclic genomes σ̄ leaves the β-face and C, R > 0 (the control: 121, 15, 25). (iii) ACYC-XI
  is PROVED-CONDITIONAL on R118 (k) REACH3-CYC, whose [REACH-L] premises R117 signs in its entry (its line states S3-START and PAD only),
  with Lemma K2-r and [1E-N3]. (iv) T_CYC ≤ N is not tight for N ≥ 2 on set A (max T_CYC / N 0.8 at N 5; T = N only at N = 1); REFEREE's
  data suggest T_CYC ≤ d + 1 (DATA, no claim). (v) The DATA units are narrower than the statements: σ̄ off the β-face tests the computed
  σ̄ (not every optimal one), C 0 tests Λ along runs (not every σ), runs start from the stored start or S3 (ACYC-LIN from other starts: no
  separate DATA); the wider counts are referee data. The Γ3 counts are taken on N5′-xi's states 0, …, T3 before the first fallback only
  (pacyc81.py breaks at the first fallback); read on the whole run they are not 0: CHECKER C136 measured, with an instrumented copy of
  pacyc81.py whose break was removed, on the four towers to N5′-xi's end, σ̄ off the β-face 94, 121, 138 and 150 and non-standard states 3
  each (C136 §3 l. 36-45); no statement is made about the states after the first fallback. (vi) All DATA are runs of implementations (the
  lane's byte copies of L-NEW's idealcyc.py, gamma3.py, si.py, n5v.py; the referees' own engines, one N5′-xi implementation only) on 300 +
  4 + 5 genomes. (vii) Names: «BETA-ACYC», «LAMBDA-CONST», «ACYC-LIN», «ACYC-XI» are new to RESULTS («ACYC» occurs there inside
  «IDEAL-ACYC»). (viii) The source note names the packet, its fixes entries 1-2 and L-SI successors 43-44; fixes entries 3 and 4 (L-SI
  successors 45 and 46) change line strings only and are not named, by the rule «a line-only entry need not be named» (CHECKER C135 l.
  22-23); REFEREE §E: «Note, not an item: entry 3 (successor 45) changes only the line» (l. 375); REFEREE-2 Add. 4: «Entry 3 changes only
  the line, so omitting it is consistent with the Lead's G-1 ruling ✓.» (l. 402). For entry 4: CHECKER C136 «N-S, ruled: no action», «and
  so will the line-only entry R1-R3 need. R-S not taken.» (l. 47-48); REFEREE §F: «So the source note need not name it (C134 N-S, as
  CHECKER ruled in C136); not L41's case.» (l. 408-409); REFEREE-2 Add. 5: «(3) Fixes entry 4 is line-only.» (l. 426). (ix) BETA-ACYC's
  proof needs pointwise optimality (CHECKER C136 E-1; REFEREE-2 N-1); L-5 states that sense in its premises (R1), citing RESULTS R57 (b)
  and [1E-N3] as landed in R104 for the word and for the existence of a pointwise optimum; both referees note, with no change asked, that
  this cites the sense, not the premise that gives IDEAL-CYC's σ̄ (REFEREE §F l. 396-397: «the clause defines a word, so the citation
  suffices.»; REFEREE-2 Add. 5 l. 421-422: «R1 defines the word, so this is not an error.»). (x) Literature: VJ00 §4.2 and Friedmann arXiv
  1106.0778 §3, as cited by R118 (landed); no novelty is claimed.
- Data (DATA, not proof): experiments/si/box81/ at l-si 358ede16 (from ff9b1639 to 0bc6f028 the only box81 changes are fix3/, with
  mkL4.py, mkfix3.py and check_fix3.sh, and one check81.sh line that runs check_fix3.sh, and from 0bc6f028 to 358ede16 fix4/, with
  mkL5.py, mkfix4.py and check_fix4.sh, and one check81.sh line that runs check_fix4.sh, git diff; no tool, instance or frozen output
  changes), run by check81.sh (lemma81.py on IDEAL-CYC, pacyc81.py and fix1/pacyc81t.py on Γ3 with N5′-xi, quotes81.py, tn81.py; the
  runners in box81/ref/ are byte copies of claude/l-new 9cdb7209's, pinned in ref.sha1), its frozen outputs in out/ and fix1/; called from
  experiments/si/check.sh, run by scripts/verify.sh. Re-run by the drafter from a git archive of ff9b1639 (experiments, docs, scripts):
  check81.sh 2026-11-08T04:57:59Z-04:59:56Z, rc 0, «P-ACYC fix1 checks: PASS», «P-ACYC fix2 checks: PASS», «box 81 checks: PASS»; and from
  a git archive of 0bc6f028: 2026-11-08T06:41:07Z-06:43:18Z, rc 0, the same three lines and «P-ACYC fix3 checks: PASS» (L-4 and fixes
  entry 3 rebuilt and compared byte for byte); and from a git archive of 358ede16: 2026-11-08T17:17:38Z-17:19:44Z, rc 0, the same four
  lines and «P-ACYC fix4 checks: PASS» (L-5 and fixes entry 4 rebuilt and compared byte for byte, L-5's sha1 checked against C136's).
  Frozen totals: lemma81 agen 300 7 «genomes 300 tried 300 states 768 notbeta 0 nonstrict 0 C 0 R 0 T_gt_N 0 maxT_over_N 1.0»; towers
  «genomes 4 tried 0 states 44 notbeta 0 nonstrict 0 C 0 R 0 T_gt_N 0 maxT_over_N 0.25»; pacyc81 300 7 «genomes 300 states 768 nofallback
  0 notbeta 0 nonstd 0 C 0 R 0 bigT 0 maxT3_over_N 1.0»; towers «genomes 4 states 44 nofallback 0 notbeta 0 nonstd 0 C 0 R 0 bigT 0
  maxT3_over_N 0.25» (k1 10, 13, 11, 10 for N 40, 48, 56, 56; pacyc81.py counts on states 0, …, k1 − 1, i.e. 0, …, T3, docstring l. 4,
  loop l. 24-29); pacyc81t taubad 0 on all three sets; control (lemma81 rgen and pacyc81) 59 states, notbeta 121, C 15, R 25. Both
  referees re-ran check81.sh (REFEREE at e3ac4b06, l. 30-31, and at 01a68edc, §C l. 327; REFEREE-2 at e3ac4b06, l. 9-10, at 01a68edc, Add.
  2 l. 303-304, and at ff9b1639, Add. 3 l. 364-365) and their own engines (above). REFEREE ran fix4/check_fix4.sh from a git archive of
  358ede16 (§F l. 387, rc 0), and CHECKER C136 re-ran check81.sh from a full git archive of 0bc6f028 (§4 l. 61-62, rc 0). Instances:
  experiments/si/box81/inst/{H5_d20_F62, H6_d24_F126, SL41_d28, L6Z_KILL238_d28}.json (set B) and {rd2_d3, rd2_d4, rd3_d3, rf_d4,
  RS2}.json (control), pinned in inst.sha1; set A is generated (lemma81.agen, seed 7).
- Signatures: REFEREE docs/referee/R-P-ACYC.md: successor 28's report a9d4e44e1b421fb2215a4489e95ea4a6bf02c1f5 (2026-11-08T00:48:22Z;
  byte-equal at d3d0a600372b897a03cba23a96e9028cb5e99875, 00:48:27Z; «Written from 2026-11-08T00:47Z (date -u). The header time of record
  is the commit time.»), «I did NOT read docs/referee-2/ for this report.» (l. 3), verdict table l. 5-18; §C
  c865da817aeb579cfce6ca0fba6da68249742548 (2026-11-08T02:38:59Z; heading «date -u at writing 2026-11-08T02:37Z»), l. 275-331, «Verdict:
  fixes entry 1 CORRECT. L-2 MATCHES, by the byte test and in meaning.» (l. 328), «No gap remains open.» (l. 331); §D
  17c81b707d1c08ce69bb9ae70f794ef342d0a85e (2026-11-08T04:03:49Z) with the heading time fixed at d4423d6dec00a24c1df71c230411f13684922cec
  (04:03:53Z; «date -u at writing 2026-11-08T04:03Z»), l. 333-348, «Verdict: fixes entry 2 CORRECT; L-3 MATCHES. All statements stay as in
  §C (all SIGN; ACYC-XI PROVED-CONDITIONAL on R118 (k), (l)).» (l. 348); successor 29's §E 055758ba570fa9c9a08f92cd73aea00a1c4ff6c3
  (2026-11-08T06:31:48Z; heading «date -u at writing 2026-11-08T06:31Z»), l. 349-378, «Verdict: L-4 MATCHES (L-3 + exactly R-G and R-B;
  both CORRECT in meaning).» (l. 377); successor 30's §F 5b2aa6044357856caefdc8f5ed165b7629ddc00f (2026-11-08T16:44:19Z; heading «date -u
  at writing 2026-11-08T16:44Z»), with R1's proof-use sentence and pacyc81.py's line numbers corrected at
  ae9805556a1feee09de9a95d2043607d591374bf (16:44:42Z), l. 380-411, «Verdict: fixes entry 4 CORRECT. **Line L-5 MATCHES** (L-4 + exactly
  R1-R3).» (l. 410). REFEREE-2 docs/referee-2/R2-P-ACYC.md: successor 32's report bf02e61888453d86f93d4fcce5207d446ce9a378
  (2026-11-08T00:55:23Z; «2026-11-08 from 00:45Z (date -u)»), «Independent: docs/referee/ not read on this item before this report is on
  origin.» (l. 2-3), verdict table l. 13-27; Addendum 1 6c937bc6e3af08a68530b01d7b5639c5ec7de25c (2026-11-08T01:44:31Z), l. 256-296, «Read
  only after this report was on origin (bf02e618). No verdict of mine changes.» (l. 257); Addendum 2
  d7ca68f42d1afc1db557be734f4fe96e17f05a29 (2026-11-08T02:38:33Z), l. 298-353, «fixes entry 1 **CORRECT** (N-2 recommended);» (l. 349);
  Addendum 3 e187847085de9c572e016edab37dd0a7e18faf78 (2026-11-08T04:06:09Z; heading «2026-11-08 04:06Z by date -u»), l. 355-374, «**L-3
  MATCHES** (Opus 5.5, D1);» (l. 373), «statements: BETA-ACYC, LAMBDA-CONST, ACYC-LIN **SIGN**; ACYC-XI **SIGN**, PROVED-CONDITIONAL on
  R118 (k) + (l); nothing REFUSED.» (l. 374); successor 33's Addendum 4 79430e80429c5aaa6b645f2bf0db13da65162275 (2026-11-08T06:38:24Z;
  heading «REFEREE-2 successor 33, 2026-11-08 06:30Z by date -u»), l. 376-406, «**Verdict: L-4 MATCHES** (Opus 5.5, D1).» (l. 405);
  successor 35's Addendum 5 c1e71a25596ff01554a1bd7390d7f8b0380a97d6 (2026-11-08T16:43:45Z; heading «2026-11-08 16:43Z by date -u;
  independent of REFEREE»), l. 408-427, «(4) Verdict: **L-5 MATCHES** (byte test, and in meaning). Statement verdicts unchanged.» (l.
  427). Lane (claude/l-si): L-SI successor 43, e3ac4b06 (packet FROZEN, L-1); successor 44, 01a68edc (fixes entry 1, L-2) and ff9b1639
  (fixes entry 2, L-3); successor 45, 0bc6f028 (fixes entry 3, L-4); successor 46, 358ede16 (fixes entry 4, L-5).
- INDEPENDENCE: the packet's proofs are L-SI's except the w* = K1 step (L41 and L43, above), which both referees wrote independently; each
  referee re-derived every proof step (REFEREE «## 4. Proofs (task 1; each step re-derived)»; REFEREE-2 «## Proofs (own re-derivation)»)
  and replayed the DATA on its own code (REFEREE: acyc_replay.py on its own VJ engine and builder, the lane's n5v.py for N5′-xi only;
  REFEREE-2: r2acyc.py, «shares no code with L-SI, L-NEW or REFEREE», l. 141). Each referee wrote its first report without reading the
  other's (REFEREE l. 3; REFEREE-2 l. 2-3); REFEREE-2 compared afterwards (Add. 1, l. 256-296); REFEREE «read REFEREE-2's items only as
  they are quoted in the fixes entry and byte-copied in fix1/» (§C l. 276). The L-2 and L-3 wording is the lane's under the Lead's routing
  (fixes l. 3, l. 99), from the referees' exact strings; each referee byte-tested it with its own script (REFEREE §C scratch/acyc_l2.py,
  §D scratch/acyc_l3.py; REFEREE-2 Add. 2 bt_l2.py, Add. 3 bt_l3.py) and read it in meaning. L-4's two strings are the Lead's rulings of
  05:13Z on the drafter's proposals (fixes l. 116-121), applied by the lane by script; L-5's three strings are CHECKER C136's R1-R3 (§5 l.
  84-89), applied by the lane by script (fix4/mkL5.py; fixes l. 138-163), and each referee byte-tested L-5 with the strings typed from
  C136, not from the lane's script (REFEREE §F l. 384-386; REFEREE-2 Add. 5 l. 412-414), REFEREE-2 «independent of REFEREE» (l. 408) and
  REFEREE «docs/referee-2/ not read for this section.» (§F l. 411); both referees' byte tests of L-4 and L-5 are under Signatures.
- TARGET.md diff: TARGET.md §2 asks for an algorithm polynomial on EVERY parity game that outputs (W_E, W_O); every statement here is
  about Howard steps on IDEAL-CYC(G), or N5′-xi's mover phase on Γ3(G), for Ξ-acyclic genome games, a restricted class (TARGET.md §4:
  «Polynomial only on a restricted class …»; packet §7 l. 189-193; REFEREE §8 l. 258-264: «No iteration total, no bit cost (§3) and no
  output correctness is claimed. Not M3, not a gauntlet step (§5). G-N5-TIME stays OPEN.»; REFEREE-2 l. 226-233). It is not an algorithm
  claim on every game, so TARGET.md §5's gauntlet does not apply, and it is not a step-4 pass. L-5 carries «G-N5-TIME stays OPEN; not M3,
  not a step-4 pass, not a TARGET.md claim» (by script); of F-12 and F-13 only F-12 touches the scope tail, adding the L41 sentence, and
  R1-R3 (F-14, F-15) touch the premises and two DATA clauses only (CHECKER C136 §4 l. 79-80: TARGET.md diff PASS on L-4). GAPS G-N5-TIME:
  open. N5′-xi stays a CANDIDATE (REFEREE-2 l. 233: «Under D1, N5′-xi stays a CANDIDATE: this packet rules out slow mover phases on
  Ξ-acyclic genomes only.»).

Proposed GAPS line-11 UPDATE (append-only), to go AFTER the last UPDATE on GAPS l. 11 at landing (R121's, «UPDATE 2026-11-08 14:06Z:
RESULTS R121 (P-N5-ASC; CHECKER C135 a9bf46bb)», is the last at 59dacf22, where R121 landed, and at the local trunk a4a777de), as a pure
insertion with one separating space before the row's closing « |». BUILT FROM L-5: the UPDATE of draft 2cd7cfd0 (d[728]; sha1
425d10fe5ca0223568b5fb2f29bea4858307dc43 of the line without newline and unfilled, built from L-4 by upd122b.py: R118's procedure,
run118()'s steps as run122(), with R122's start «RESULTS R15's object): », its four labels and its source prefix; controls R97-R120 True
×24 and the R121 draft controls True in that draft) with CHECKER C136's R1, R2 and R3 applied, each old string once in it (C136 §3:
«R1-R3's old strings occur once each in L-4 and in the UPDATE.»); sha1 793193506cd6e4ca67ebb88235a75f70b72f7808 of the line without
newline and unfilled, = C136 §5's and = run122()'s direct build from L-5 (upd122c.py). <DATE>, <HH:MM> and <checker> are the landing date,
time and the C136 commit, all filled at landing:
UPDATE <DATE> <HH:MM>Z: RESULTS R122 (P-ACYC; CHECKER C136 <checker>) [refereed-only] LANDED: Odd never leaves the β-face on Ξ-acyclic genomes (premises: R104's definitions of the genome, the Ξ-graph, Γ(G) and its start only; R117's definition of Γ3(G) only; R118 (a) definitions, (d) BR-SEG, and for the corollary (k) REACH3-CYC with (l) Corollary T3; the order ⊴ and σ̄ of R118 [VJ], an optimal counterstrategy being pointwise optimal (at every vertex its play value is ⊴ the value under every Odd strategy; RESULTS R57 (b), [1E-N3], as landed in R104); for the corollary's iterations and fallback, SPEC S4 and S4c, RESULTS R15's object): for every genome G whose Ξ-graph is acyclic, on Γ(G) or Γ3(G), and every Even strategy that agrees with the stated start off the movers (transported through the pads on Γ3), every optimal counterstrategy of Odd takes the β-face at every gate, and no play from a non-e vertex contains an e-vertex (Lemma BETA-ACYC); every vertex's cycle node is then independent of the movers' choices (Lemma LAMBDA-CONST); hence the Howard run of IDEAL-CYC(G) from any mover state has C = 0, R = 0 and T_CYC ≤ N (Theorem ACYC-LIN); and the first fallback of N5′-xi on Γ3(G) from S3, i.e. the least iteration k at which SPEC S4c applies, comes at k = T3 + 1 ≤ N + 1 (Corollary ACYC-XI, PROVED-CONDITIONAL on R118's REACH3-CYC, whose [REACH-L] premises RESULTS R117's entry signs for acyclic Ξ-graphs, with Lemma K2-r and [1E-N3] as listed in R118 (k)): so on the whole domain of the tower route N5′-xi's mover phase is linear in N, while N5 with SPEC's S4a tie rule realises L(G) there (R117); nothing is claimed about iterations after the first fallback, about Ξ-cyclic genomes, or about the running time of N5 or N5′-xi (no bound on R for Ξ-cyclic genomes); the step w* = K1 of LAMBDA-CONST's proof (σ̄(K2) toward K1 is Odd's unique optimum) is referee-originated (REFEREE R-P-ACYC §4.2 LC-1 and REFEREE-2 R2-P-ACYC G-1 / W-1, found independently, restated in P-ACYC's fixes entry 1 F-1), signed by both referees; DATA (experiments/si/box81, check81.sh): on 300 random Ξ-acyclic genomes (lemma81.agen, d 1-6, w 1-3, degree 2-3, seed 7; 768 states) and the four tower genomes H5_d20_F62, H6_d24_F126, SL41_d28, L6Z_KILL238_d28 (44 states), each run from the genome's stored start (IDEAL-CYC) or from S3 (Γ3), σ̄ off the β-face in 0 (state, gate) pairs (BETA-ACYC's no-e-vertex clause: no separate DATA), C 0, R 0, runs with T_CYC > N 0 (lemma81.py, IDEAL-CYC; ACYC-LIN from other mover states: no separate DATA) and, along N5′-xi on Γ3 from S3, on its states 0, …, T3 before the first fallback (pacyc81.py; τ by fix1/pacyc81t.py), σ̄ off the β-face 0, states that are not standard (σ off the movers and τ) 0, genomes with no fallback 0, genomes with first fallback after iteration N + 1 0 (k = T3 + 1 is R118 (k)'s own clause, and N5's L(G) is R117's: no separate DATA); control, five Ξ-cyclic genomes rd2_d3, rd2_d4, rd3_d3, rf_d4, RS2 (59 states; the same counts on IDEAL-CYC and on N5′-xi's states 0, …, T3 on Γ3; e-priorities ordered by (lev, gate index), as in ref gamma3.build): σ̄ off the β-face in 121 (state, gate) pairs, C 15, R 25 (P-ACYC, docs/si/P-ACYC.md with its fixes entries 1-2, docs/si/P-ACYC-fixes.md; L-SI successors 43-44). G-N5-TIME stays open.

Addendum (subagent, for the Lead; does not land; written 2026-11-08T05:11:22Z by date -u). (1) FIRST FILL on line L-3 (l-si ff9b1639,
sha1 03453361…), to CHECKER C136. I edited docs/agents/R122-draft.md only; no merge, no commit and no push by me; the Lead commits this
file. Fetches: the first between 04:54:20Z and 04:55:00Z, the second at 05:10:38Z-05:10:39Z (record, l. 2-40); every object is unchanged
at the second (git diff --quiet). (2) TITLE d[308] (l. 309) = "### R122 [refereed-only] " + L-3 without its newline + ", CHECKER PASS
(docs/checker/C136.md, checker PENDING)", checked by script (chk122.py): equal, byte for byte (True); and the title minus that prefix and
that tail is L-3 (True); the only «### R» heading of this file; 2,792 characters, 2,843 bytes, sha1 of the heading line without its
newline 65d5127d2da1a3e5f8936d6830f5aa35c76202f2; 39 «(» / 39 «)» (L-3's 38 and the fill's), 0 "|", «R1xx» 0, «[refereed-only]» once.
(3) SHAPE. The entry block is l. 309-518 (python slice d[308:518], 210 lines), followed by a blank line (d[518]); 0 "|" in it; the
title's fill string once in it (four times in the whole file: the title, item (1) of the record and items (2) and (7) of this
Addendum). The GAPS preamble is
l. 520-528 (d[519:528]); the UPDATE is l. 529 (d[528]), one line, sha1 a92748935ead9054b1029880e863e4c97268e9bd without newline and
unfilled (= upd122L3.txt, True), 2,793 bytes, 2,744 characters, 465 tokens, 38 «(» / 38 «)», 0 "|", one each of «<DATE>», «<HH:MM>»,
«<checker>», «2026-11-07» 0 times, « — » 0 times. A landing script slices d[308:518] for the entry and reads d[528] for the UPDATE, with
«R122», «C136», PREV = R121's block and UPDATE (when R121 lands first, as routed; else R120's, G-P). The FIRST FILL record is l. 2-307
(d[1:307]), then a blank line. (4) WHAT IS LEFT: the Lead's ruling on G-7 (L41; and G-7 (ii), AC-6) and on G-1's R-B; CHECKER C136 on
this file (G-1, G-7, G-4 with optional R-N, G-2, G-U, the G-9 notes); if any replacement is taken, an L-4 by L-SI (fixes entry 3, line
only), both referees' byte tests, and a second fill (title, line history, Object, L41 and L43 (the scope-tail sentence), Honest limits
(viii) and (ix), Signatures, the UPDATE rebuilt from L-4). R121 lands first (C135 Add. 1 pending), then R122 after it. The Lead merges
claude/l-si (ff9b1639 or later), claude/referee (d4423d6d or later) and claude/referee-2 (e1878470 or later) before landing, then lands
R122 with <DATE>, <HH:MM> and <checker> filled. (5) QUOTE SWEEP (chk122.py: outermost guillemet quotes, nested ones inside them, split at
«…», parts of 6+ characters, whitespace-normalised, NO docs/agents draft as a source; sources: the packet, fixes, L-1, L-2, L-3 at
ff9b1639; REFEREE's file at d3d0a600, c865da81, 17c81b70, d4423d6d and 013f821b; REFEREE-2's at bf02e618, 6c937bc6, d7ca68f4 and
e1878470; at HEAD RESULTS, GAPS, DECISIONS, DECISIONS-INDEX, LEAD-STATE, NOW, TARGET.md, CLAUDE.md; C135.md and notes/CHECKER.md on
claude/checker; box 81's lemma81.py, pacyc81.py, fix1/pacyc81t.py, check81.sh, check_fix1.sh, check_fix2.sh, mkL3.py and the frozen
outputs at ff9b1639; SPEC docs/new/N5-ssi-global.md; the subjects of the commits cited; my outputs check81.out, upd122.out, upd122L3.txt,
upd122prop.txt, L3prop.txt): on the draft before this Addendum, the first-fill record 213 quotes, 183 parts, 0 not found; title and body
132 quotes, 128 parts, 0 not found; GAPS preamble and UPDATE 3 quotes, 2 parts, 0 not found; whole file 348 quotes, 313 parts, 0 not
found; negative control (a made-up quote) reported missing (True); the run on the final file is in chk_final.out. lp122.py: 152 quotes
and line references at their cited lines (packet l. 3-193, fixes l. 3-114, REFEREE l. 3-348 and 17c81b70's l. 333, REFEREE-2 l. 2-374,
RESULTS l. 624, 9864, 13362, 13607, 13677-13719, DECISIONS l. 355-358, DECISIONS-INDEX l. 34, LEAD-STATE l. 2725, notes/CHECKER.md l.
10, lemma81.py l. 30-69, pacyc81.py l. 18-57, check81.sh l. 7-8), 0 failed (one reference corrected from l. 13707-13708 to l.
13707-13709 before the final run). (6) STALE STATUS (chk122.py): in the entry block «PENDING» 1 (the title's fill), «NOT YET» 1
(REFEREE's L-1 verdict, quoted as history), «first fill» 4 (L41 and L43 ×2 and Honest limits (viii), (ix): the open flags G-7, G-1 and
G-4, to be re-worded at the second fill or at landing), «R-B», «R-G», «R-N» 1 each (the same sentences); «pending», «will », «not
landed» 0; GAPS preamble: «first fill» 1 (R120's UPDATE is the last at this first fill); line 1 «NOT LANDED» 1 (R122 is not landed).
(7) LANDING SIMULATION (sim122.py on in-memory copies of RESULTS 66e71196… and GAPS 2a41c765… at the local trunk c8f42538). CASE 1, as
routed: R121's draft entry d[271:482] (its «checker PENDING)» left as is) + a blank line inserted directly before «**Erratum E-1**», then
R122's d[308:518] + a blank line directly before «**Erratum E-1**» (each a pure insertion: prefix and suffix byte-unchanged, True);
RESULTS 14,962 → 15,174 → 15,385 lines (+211 for R122); R118 l. 13,607, R119 l. 13,879, R120 l. 14,114, R121 l. 14,320, R122 at l.
14,532-14,741, blank l. 14,742, «**Erratum E-1**» to l. 14,743, E-2 14,756, Note E-3 14,784, Dead ends 14,815; order R110-R122, E-1,
E-2, E-3, Dead ends: True. GAPS: only l. 11 changes (True), the closing " |" replaced by " " + R121's filled draft UPDATE + " " + R122's
filled UPDATE + " |"; "|" on l. 11 76 → 76; «UPDATE 2026-» 55 → 55 plus two heads with the simulation year 2099 after R120's; R122's
UPDATE last, R121's before it (True); 23 → 23 lines. CASE 2, R122 directly after R120 (if R121 is not landed first): R122 at l.
14,320-14,529, blank l. 14,530, E-1 l. 14,531, E-2 14,544, Note E-3 14,572, Dead ends 14,603; order True; GAPS as above with one 2099
head, R122's last (True). Fill values used only for the simulation: 2099-01-08 / 2099-01-09, 00:00, 0000000 / 1111111. (8) UPDATE
(upd122.py): r121/tools/upd121.py l. 1-70 exec'd unchanged (its l. 71, the write into r121/, and its Part H not executed): controls
R97-R120 as landed, True ×24, the last UPDATE on l. 11 R120's (True); the R121 control, NOT landed: run121 on P-N5-ASC L-2 =
R121-draft.md d[491] (6635b14e…, True), and with C135 §5's R1-R4 = C135's L-3 UPDATE f545cba7… (5,184 bytes, True). Part I, R122 by
run122() (= run121(): run118()'s steps; G-U), = the direct build (True); connectors kept in front of their clauses: «; », «; hence »,
«; and ». Token diff L-3 → UPDATE, 11 hunks, 51 tokens out, 50 in: the head inserted («UPDATE <DATE> <HH:MM>Z: RESULTS R122 (P-ACYC;
CHECKER C136 <checker>) [refereed-only] LANDED:»); the four labels moved behind their clauses («e-vertex (Lemma BETA-ACYC);», «choices
(Lemma LAMBDA-CONST);», «N (Theorem ACYC-LIN);», and the corollary's label, with its inner «(k)», in place of « (2026-11-07) —», followed
by «:»); «genomes; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim);» → «genomes);»; «43)» → «43). G-N5-TIME stays
open.». Nothing else. With R-G then R-B (each old string once in L-3; R-G's UPDATE form, old string «(no bound on R for Ξ-cyclic
genomes); DATA (experiments/si/box81, check81.sh):», once in the UPDATE): L-3 + proposals sha1 85bb221f19ca457655c954f570552bc0f4d8095d
(3,080 bytes with its newline, 41 / 41, one " — "), its UPDATE by the same procedure 425d10fe5ca0223568b5fb2f29bea4858307dc43 (3,108
bytes; = the L-3 UPDATE with R-B applied and R-G's sentence inserted after «(no bound on R for Ξ-cyclic genomes)», True). R-N not built
into a line or an UPDATE (its old string once in L-3 and once in the UPDATE, by script). Pipe rule: the filled R122 UPDATE appended after
R121's (simulated) after R120's (landed) keeps 76 "|" on l. 11, R122's last, prefix byte-unchanged (True). (9) NOT VERIFIED / NOT DONE:
scripts/verify.sh not run (box81/check81.sh only, from a git archive of ff9b1639; not the whole experiments/si/check.sh); the referees'
tools not re-run (their files read); no simulator of my own (the DATA are the lane's tools, re-run; the runners in box81/ref/ not read
beyond what lemma81.py and pacyc81.py call); the proofs not re-derived by me beyond reading both referees' re-derivations against the
packet and the fixes (G-7 and G-4 are text checks); VJ00 / Friedmann not opened by me (R118's landed premise); RESULTS R117's entry body
not read beyond R118's account of [REACH-L] (l. 13704-13715); no Oink run (L-3 cites no Oink check). (10) Scratch:
/tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad/r122/ (fetch.time, fetch2.time,
fetch2.out; src/ (the packet, fixes, L-1, L-2, L-3, the referee files at each commit); arch/ = git archive of ff9b1639 (experiments,
docs, scripts), check81.out, check81.rc, run.start, run.end; tools/upd122.py, upd122.out, upd122L3.txt, L3prop.txt, upd122prop.txt;
tools/chk122.py, chk_p2.out, chk_final.out; tools/lp122.py; tools/sim122.py, sim_p2.out, sim_final.out; tools/assemble122.py,
template.md, addendum.md, filltime.txt).

Addendum 2 (subagent, for the Lead; does not land; written 2026-11-08T07:04:43Z by date -u). (1) SECOND FILL on line L-4 (l-si 0bc6f028,
sha1 85bb221f…), to CHECKER C136 (its first round). I edited docs/agents/R122-draft.md only; no merge, no commit and no push by me; the
Lead commits this file. Heads at the fetch of 2026-11-08T06:39:15Z: l-si 0bc6f028, referee e4cb208a, referee-2 11a7a911, checker fa8add12,
origin trunk c9591e35; local trunk HEAD 616941eb. Second fetch 2026-11-08T06:52:17Z-06:52:18Z (rc 0): all heads unchanged. Third fetch
2026-11-08T06:54:04Z: referee 055758ba (REFEREE 29's §E on P-ACYC, L-4 MATCHES, now cited in the draft), origin trunk 616941eb (the Lead's
push); l-si, referee-2 and checker unchanged. Fourth fetch 2026-11-08T07:02:54Z-07:02:55Z (rc 0): referee-2 79430e80 (REFEREE-2 33's
Addendum 4 on P-ACYC, L-4 MATCHES, now cited in the draft); the other four heads unchanged. The Lead has since committed 36c183f8 locally
(NOW, LANE-RESTART, LEAD-STATE only). (2) TITLE l. 447 (d[446]) = "### R122 [refereed-only] " + L-4 without its newline + ", CHECKER PASS
(docs/checker/C136.md, checker PENDING)", checked by script (chk122b.py): equal, byte for byte (True); the title minus that prefix and
that tail is L-4's bytes without the newline (True); the only «### R» heading of this file; 3,104 characters, 3,158 bytes, sha1 of the
heading line without its newline 8cd565ca7180a0d4befc1a81a7dc9d163466dc25; 42 «(» / 42 «)» (L-4's 41 and the fill's), depth never
negative, 0 "|", «R1xx» 0, «[refereed-only]» once. (3) SHAPE. The entry block is l. 447-718 (python slice d[446:718], 272 lines), followed
by a blank line (d[718]); 0 "|" in it; the title's fill string once in it (four times in the file before this Addendum: l. 402 in the
first fill's record, the title, and l. 735 and 767 in the first fill's Addendum). The GAPS preamble is l. 720-728 (d[719:728]); the UPDATE
is l. 729 (d[728]), one line, sha1 425d10fe5ca0223568b5fb2f29bea4858307dc43 without newline and unfilled (= upd122L4.txt, True), 3,108
bytes, 3,056 characters, 511 tokens, 41 «(» / 41 «)», 0 "|", one each of «<DATE>», «<HH:MM>», «<checker>», «2026-11-07» 0 times, « — » 0
times. A landing script slices d[446:718] for the entry and reads d[728] for the UPDATE, with «R122», «C136», PREV = R121's block and
UPDATE (when R121 lands first, as routed; else R120's). The SECOND FILL section is l. 2-139, the first fill's record l. 140-446
(rec122b.py: 0fa23b17's l. 2-308, byte-unchanged, directly before the title, True) and the first fill's Addendum l. 731-799 (0fa23b17's l.
531-599, byte-unchanged, directly after the UPDATE and a blank line, True). (4) PLACEHOLDERS: none left. REFEREE's §E (055758ba, third
fetch) and REFEREE-2's Addendum 4 (79430e80, fourth fetch) are on origin and cited verbatim, each with its commit (8 hex digits in Object
and Claims signed, 40 in Signatures), its time, its line range, its byte-test lines and its verdict line with line numbers; the four
former REFEREE-2 token places are now l. 17 (SECOND FILL, the referee-2 head, which now says that Addendum 4 reached origin only at the
fourth fetch, recorded at l. 25-32), l. 498-501 (Object, the line rounds), l. 504-505 (Claims signed, the list of REFEREE-2 rounds; its
verdict also at l. 528) and l. 698-699 (Signatures, after REFEREE-2's Addendum 3); L41 and L43 (l. 597-598) and Honest limits (viii) (l.
661-662) also quote Add. 4. (5) WHAT IS LEFT: R121 lands first (its L-5 and C135 Add. 1); then CHECKER C136 on this file (G-4 with
optional R-N, N-S with optional R-S, G-2, G-U, the G-9 notes, D-7, D-8, D-9); the Lead merges claude/l-si (0bc6f028 or later),
claude/referee (055758ba or later), claude/referee-2 (79430e80 or later) and claude/checker before landing, then lands R122 after R121
with <DATE>, <HH:MM> and <checker> filled. (6) QUOTE SWEEP (chk122b.py: chk122.py's rule, outermost guillemet quotes, nested ones inside
them, split at «…», parts of 6+ characters, whitespace-normalised, NO docs/agents draft as a source; sources: the first fill's (r122/src:
the packet, fixes, L-1, L-2, L-3, the referee files at each commit; r122/arch at ff9b1639) plus, at 0bc6f028, the packet, fixes, L-1 to
L-4 and box 81 (lemma81.py, pacyc81.py, fix1/pacyc81t.py, check81.sh, the fix1-fix3 tools, the frozen outputs); REFEREE's P-ACYC file at
055758ba and REFEREE-2's at 79430e80; at c9591e35 RESULTS, GAPS, DECISIONS, DECISIONS-INDEX, LEAD-STATE, NOW, TARGET.md, CLAUDE.md;
C135.md and notes/CHECKER.md on claude/checker; SPEC docs/new/N5-ssi-global.md; the subjects of the commits cited; the first fill's
outputs and mine (check81.out, upd122b.out, upd122L4.txt, l4rel122b.out, opt122b.out)): on the draft before this Addendum, line 1 and the
SECOND FILL section 81 quotes, 65 parts, 0 not found; first-fill record 213 quotes, 183 parts, 0 not found; title and body 179 quotes, 176
parts, 0 not found; GAPS preamble and UPDATE 4 quotes, 3 parts, 0 not found; first-fill Addendum 47 quotes, 28 parts, 0 not found;
together 524 quotes, 455 parts, 0 not found; negative control (a made-up quote) reported missing (True); the run on the final file is in
chk_final.out. lp122b.py: 70 quotes and line references new at this fill (REFEREE l. 3-378, REFEREE-2 l. 2-406, fixes l. 3-136, packet l.
3-96, LEAD-STATE l. 2754, DECISIONS l. 355-358, C135 l. 22-23, RESULTS l. 9864, check81.sh l. 43) each at its cited lines, 0 failed (one
check-list entry corrected from l. 131 to l. 132 before the final run; the draft cites that quote as l. 129-134). (7) STALE STATUS
(chk122b.py, case-insensitive): in the entry block, the title's fill excepted, «pending», «will », «awaiting», «to come», «not landed»,
«second fill», «first fill» and «this fill» 0 times each; «not yet» twice, both inside quotes of the referees' L-1 and L-2 verdicts
(history); «candidate» twice, in the TARGET.md diff (N5′-xi's status and REFEREE-2's quote, unchanged from the first fill); «R-G» 8 and
«R-B» 7 times, all inside quotes (fixes l. 121; REFEREE §E l. 356-357, and l. 377 quoted twice; REFEREE-2 Add. 4 l. 381, 382, 384); «R-N»,
«R-S», «a9274893» and «425d10fe» 0 times. GAPS preamble and UPDATE: the same words 0 times each. Line 1 «NOT LANDED» once (R122 is not
landed). Model names: «Opus» 10 times in the entry block, all inside quoted referee verdicts. (8) LANDING SIMULATION (sim122b.py, on
in-memory copies of RESULTS 66e71196… and GAPS 2a41c765… at origin trunk 616941eb, equal at c9591e35 and at the local HEAD 36c183f8). CASE
1, as routed: R121's second-fill entry (R121-draft.md at 616941eb, = the working tree, sha1 823d15c3…, d[404:706], its «checker PENDING)»
left as is) + a blank line inserted directly before «**Erratum E-1**», then R122's d[436:699] + a blank line directly before «**Erratum
E-1**» (each a pure insertion: prefix and suffix byte-unchanged, the inserted block = the draft's, True); RESULTS 14,962 → 15,265 → 15,538
lines (+273 for R122); R118 l. 13,607, R119 l. 13,879, R120 l. 14,114, R121 l. 14,320, R122 at l. 14,623-14,894, blank l. 14,895,
«**Erratum E-1**» to l. 14,896, E-2 14,909, Note E-3 14,937, Dead ends 14,968; order R110-R122, E-1, E-2, E-3, Dead ends: True; "|" in
RESULTS 1,477 → 1,477. GAPS: only l. 11 changes (True), the closing " |" replaced by " " + R121's filled L-4 UPDATE (its d[715]) + " " +
R122's filled UPDATE + " |"; "|" on l. 11 76 → 76; «UPDATE 2026-» 55 → 55 plus two heads with the simulation year 2099 after R120's;
R122's UPDATE last, R121's before it (True); 23 → 23 lines. CASE 2, R122 directly after R120 (if R121 is not landed first): R122 at l.
14,320-14,591, blank l. 14,592, E-1 l. 14,593, E-2 14,606, Note E-3 14,634, Dead ends 14,665; order True; GAPS as above with one 2099
head, R122's last (True). Fill values used only for the simulation: 2099-01-08 / 2099-01-09, 00:00, 0000000 / 1111111. R121's entry in
CASE 1 is its second fill on L-4; LEAD-STATE now routes an L-5 for R121, so its block will differ in length when it lands, which shifts
R122's line numbers only. (9) UPDATE: (c) of the SECOND FILL section; upd122b.out has the controls and the 11 token hunks. (10) NOT
VERIFIED / NOT DONE: scripts/verify.sh not run (box81/check81.sh only, from a git archive of 0bc6f028; not the whole
experiments/si/check.sh); the referees' tools not re-run (REFEREE's acyc_l4.py and REFEREE-2's bt_l4.py read only through §E and Add. 4);
the proofs not re-derived by me; mkfix3.py's output checked only through check_fix3.sh in the check81.sh re-run; R121's second fill not
re-checked by me beyond its entry slice, its UPDATE (= run121 on P-N5-ASC L-4, True) and its sha1; no Oink run (L-4 cites no Oink check).
(11) Scratch: /tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad/r122b/ (fetch.time,
fetch2.time, fetch2.out; src/ (the packet, fixes, L-1 to L-4 at 0bc6f028; fixes_ff9b1639.md; R122-draft-0fa23b17.md, the first fill, not a
quote source); ref.md, ref2.md (the P-ACYC files at e4cb208a and 11a7a911), ref_055758ba.md, ref2_79430e80.md; fetch4.time, fetch4.out;
arch/ = git archive of 0bc6f028 (experiments, docs, scripts), run.start, run.end, check81.rc, check81.out, mkL4.out; tools/l4rel122b.py,
l4rel122b.out; tools/upd122b.py, upd122b.out, upd122L4.txt; tools/opt122b.py, opt122b.out; tools/entry122b.py, sf122b.py, add122b.py,
assemble122b.py, parts/ (header.txt, secondfill.txt, entry.txt, preamble.txt, addendum2.txt); tools/chk122b.py, chk_p1.out, chk_p2.out,
chk_p3.out, chk_final.out; tools/lp122b.py, lp_p1.out, lp_final.out; tools/sim122b.py, sim_p1.out, sim_p2.out, sim_p3.out, sim_final.out;
tools/rec122b.py, rec_final.out; filltime.txt, addtime.txt; draft_p1.md, draft_p2.md, draft_p3.md, R122-draft-2133f5ac.md (the draft
before the Add. 4 fill), R122-draft.md).

Addendum 3 (subagent, for the Lead; does not land; written 2026-11-08T17:33:13Z by date -u). (1) THIRD FILL on line L-5 (l-si 358ede16,
sha1 7a84e094…), to CHECKER C136 Add. 1. I built this file in the scratchpad only
(/tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad/r122c/R122-draft.md, by fill3.py from the
draft at the local trunk a4a777de); I edited nothing in the repository, merged, committed and pushed nothing, and ran neither
scripts/verify.sh nor scripts/push.sh; the Lead commits this file as docs/agents/R122-draft.md. Heads at the fetch of
2026-11-08T17:14:25Z: l-si 358ede16, referee ae980555, referee-2 c1e71a25, checker dcdecd2a; local trunk HEAD a4a777de (being pushed); the
trunk's remote-tracking ref d35ce1ec (not fetched by me). Re-fetch at 2026-11-08T17:32:07Z-17:32:08Z (the same four branches; rc 0): all
four heads unchanged; local HEAD a4a777de unchanged, the working tree clean (git status --short empty). (2) TITLE l. 567 (d[566]) = "###
R122 [refereed-only] " + L-5 without its newline + ", CHECKER PASS (docs/checker/C136.md, checker PENDING)", checked by script
(chk122c.py): equal, byte for byte (True); the title minus that prefix and that tail is L-5's bytes without the newline (True); the only
«### R» heading of this file; 3,339 characters, 3,399 bytes, sha1 of the heading line without its newline
52c7e4287223cc4d2a44cb8458df91ae5143591d; 44 «(» / 44 «)» (L-5's 43 and the fill's), depth never negative, 0 "|", «R1xx» 0,
«[refereed-only]» once. (3) SHAPE. The entry block is l. 567-897 (python slice d[566:897], 331 lines; the second fill's was d[446:718],
272 lines), followed by a blank line (d[897]); 0 "|" in it; «PENDING» once in it (the title's fill); parentheses in the block 587 «(» /
585 «)», the same surplus of two as the second fill's block (507 / 505), from quoted fragments outside the title (the title balances); no
continuation line starts like a list marker; longest line but the title 138 characters. The GAPS preamble is l. 899-907 (d[898:907]); the
UPDATE is l. 908 (d[907]), one line, sha1 793193506cd6e4ca67ebb88235a75f70b72f7808 without newline and unfilled
(02b28fac7c0d5510b0384869508c0dcafd575c0d with a newline), = upd122L5.txt (True), 3,349 bytes, 43 «(» / 43 «)», one each of «<DATE>»,
«<HH:MM>», «<checker>», 0 "|". A landing script slices d[566:897] for the entry and reads d[907] for the UPDATE, with «R122», «C136», PREV
= R121's block and UPDATE (landed). The THIRD FILL section is l. 2-121; l. 122-566 (the SECOND FILL section, the FIRST FILL record and its
blank line) are 2cd7cfd0's l. 2-446, byte-unchanged, directly before the title (rec122c.py, True); l. 909-1052 (blank, the first fill's
Addendum, blank, Addendum 2) are 2cd7cfd0's l. 730-873, byte-unchanged, directly after the UPDATE (True); line 1 is 2cd7cfd0's line 1 with
only its tail after «sha1 85bb221f19ca457655c954f570552bc0f4d8095d» replaced (True). (4) TOKENS. In the new text (line 1, the THIRD FILL
section, the entry block, the preamble and the UPDATE) the only angle-bracket tokens are the three fill tokens, twice each (the preamble's
mention and the UPDATE); this Addendum names them only in (2), (3) and (5). (5) WHAT IS LEFT: CHECKER C136 Add. 1 on this file (the THIRD
FILL section's notes N-C, N-E, N-W, N-S and D-10, D-11; N-W is new entry text in Honest limits (v), for CHECKER's ruling); the Lead merges
claude/referee (ae980555 or later) and claude/referee-2 (c1e71a25 or later) before landing (claude/l-si 358ede16 and claude/checker
dcdecd2a are merged at a4a777de), then lands R122 after R121 with <DATE>, <HH:MM> and <checker> filled. (6) QUOTE SWEEP (chk122c.py:
chk122b.py's rule, outermost guillemet quotes, nested ones inside them, split at «…», parts of 6+ characters, whitespace-normalised, NO
docs/agents draft as a source; sources: the first and second fills' (r122/src, r122b/src, the box 81 archives of ff9b1639 and 0bc6f028,
REFEREE's file at 055758ba, REFEREE-2's at 79430e80, trunk files at c9591e35, C135 and notes/CHECKER.md at fa8add12, SPEC, their outputs)
plus C136 at b2fe3440; the packet, fixes, L-4 and L-5 at 358ede16 and box 81 from its archive (pacyc81.py, check81.sh, fix1-fix4 tools);
REFEREE's file at 5b2aa604 and ae980555 with acyc_l5.py and l5test.out; REFEREE-2's at c1e71a25 with bt_l5.py and bt_l5.out; RESULTS,
GAPS, LEAD-STATE, NOW, DECISIONS and TARGET.md at a4a777de; the subjects of the commits cited; my outputs check81.out, l5rel122c.out,
upd122c.out, upd122L5.txt): on the draft before this Addendum, line 1 and the THIRD FILL section 73 quotes, 65 parts, 0 not found; SECOND
FILL section 81 quotes, 65 parts, 0 not found; first-fill record 213 quotes, 183 parts, 0 not found; title and body 223 quotes, 223 parts,
0 not found; GAPS preamble and UPDATE 4 quotes, 3 parts, 0 not found; first-fill Addendum 47 quotes, 28 parts, 0 not found; Addendum 2 38
quotes, 22 parts, 0 not found; whole file 679 quotes, 589 parts, 0 not found; negative control (a made-up quote) reported missing (True);
the run on the final file is in chk_final.out. lp122c.py: 92 quotes and line references new at this fill (C136 l. 2-94, fixes l. 138-163,
REFEREE l. 380-411 at ae980555 and l. 391-409 at 5b2aa604, REFEREE-2 l. 408-427, packet l. 69-70, RESULTS l. 624-14816 and GAPS l. 11 at
a4a777de, LEAD-STATE l. 2896-2903, pacyc81.py l. 4-40, check81.sh l. 44) each at its cited lines, 0 failed. hex122c.py: 80 hex ids in the
new text before this Addendum (line 1, the THIRD FILL section, the entry, the preamble and the UPDATE): 51 git objects, 20 sha1s measured
at this fill (files, lines and drafts; hex_final.out lists them), 9 already in draft 2cd7cfd0, 0 unresolved. (7) STALE STATUS (chk122c.py,
case-insensitive): in the entry block, the title's fill excepted, «pending», «awaiting», «to come», «not landed», «first fill», «second
fill», «third fill» and «this fill» 0 times each; «will » once, inside the quote of C136 l. 48 («and so will the line-only entry R1-R3
need.»); «not yet» twice, inside the referees' L-1 and L-2 verdicts (history); «candidate» twice, in the TARGET.md diff (unchanged); «R-B»
7 and «R-G» 8 times, all inside quotes (as in the second fill); «R-N» 0; «R-S» 4 times, three inside «BR-SEG» and one inside the quote of
C136 l. 48; «425d10fe» and «79319350» 0 times. GAPS preamble and UPDATE: the same words 0 times each. Line 1 «NOT LANDED» once (R122 is
not landed). Model names: «Opus» 10 times in the entry block, all inside quoted referee verdicts. (8) LANDING SIMULATION (sim122c.py, on
in-memory copies of RESULTS 04a444ee… and GAPS a4721066… at the local trunk a4a777de, = 59dacf22's): R122's d[566:897] + a blank line
inserted directly before «**Erratum E-1**», after R121's block (l. 14320-14742) and its blank line, a pure insertion (prefix and suffix
byte-unchanged, the inserted block = the draft's, True); RESULTS 15,386 → 15,718 lines (+332); R118 l. 13,607, R119 l. 13,879, R120 l.
14,114, R121 l. 14,320, R122 at l. 14,744-15,074, blank l. 15,075, «**Erratum E-1**» to l. 15,076, E-2 15,089, Note E-3 15,117, Dead ends
15,148; order R110-R122, E-1, E-2, E-3, Dead ends: True; "|" in RESULTS 1,477 → 1,477. GAPS: only l. 11 changes (True), the closing " |"
replaced by " " + R122's filled UPDATE + " |"; "|" on l. 11 76 → 76; «UPDATE 2026-» 56 → 56 plus one head with the simulation year 2099
after R121's (True); R122's UPDATE last (True); 23 → 23 lines. Fill values used only for the simulation: 2099-01-09, 00:00, 1111111. (9)
UPDATE: (c) of the THIRD FILL section; upd122c.out has the control, the three replacements and the 11 token hunks. (10) NOT VERIFIED / NOT
DONE: scripts/verify.sh and scripts/push.sh not run (not asked; box81/check81.sh only, from a git archive of 358ede16; not the whole
experiments/si/check.sh); the referees' scripts acyc_l5.py and bt_l5.py read, not re-run (their logs read); upd122b.py's chain of GAPS
controls (R97-R120 rebuilt, R121 draft controls) not re-run, and no control for R121's landed UPDATE built: the UPDATE is the second
fill's d[728] with R1-R3, cross-checked by a standalone direct build, as above; C136's whole-run counts (Honest limits (v)) not reproduced
by me, cited as C136's; R1 read in meaning only through both referees' readings and against packet §1 l. 69-70 (a text check), R2 / R3
against pacyc81.py l. 4 and l. 24-29; the proofs not re-derived by me; no Oink run (L-5 cites no Oink check). (11) Scratch:
/tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad/r122c/ (filltime.txt, fetch.time; src/
(C136.md, the packet, fixes, L-4, L-5 at 358ede16; ref_5b2aa604.md, ref_ae980555.md, ref2_c1e71a25.md); draft2.md, the second fill, not a
quote source; arch/ = git archive of 358ede16 (experiments, docs, scripts), run.start, run.end, check81.rc, check81.out;
tools/l5rel122c.py, l5rel122c.out; tools/upd122c.py, upd122c.out, upd122L5.txt; parts/ (thirdfill.src, preamble.src, addendum3.src);
fill3.py, addtime.txt; tools/chk122c.py, chk_p1.out, chk_final.out; tools/lp122c.py, lp_final.out; tools/sim122c.py, sim_final.out;
tools/rec122c.py, rec_final.out; tools/hex122c.py, hex_final.out; report.txt; R122-draft.md).
