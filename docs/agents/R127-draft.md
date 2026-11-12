# Draft RESULTS R127 (Lead; first fill 2026-11-12T06:54:50Z by date -u (subagent) on P-N5-SPLIT line L-1, docs/new/P-N5-SPLIT-line-L1.txt, l-new 8f4dab7e, sha1 634b2fdfda31eda9e82e9f558ffebf3c89f5701c (draft sha1 80a1f05c, the Lead's record commit 039b0558, not routed to CHECKER; Lead rulings R-D7a 07:12Z and R-U127 07:58Z); SECOND FILL 2026-11-12T09:52:22Z by date -u (subagent) on P-N5-SPLIT line L-3, docs/new/P-N5-SPLIT-line-L3.txt, l-new 621e6b77, sha1 a8661c4b7998aafc02299c43dfe4e2c6320f73ee; THIRD FILL 2026-11-12T10:29:09Z by date -u (subagent): REFEREE §E on origin, claude/referee 33cd0fca) — to CHECKER C141 — NOT LANDED; goes after R126 (LANDED at 07139249, RESULTS l. 15726-15901), directly before the line-start «**Erratum E-1** (not a result» (l. 15903 at 07139249); its GAPS UPDATE after R126's on GAPS l. 11 — LANDED in RESULTS 2026-11-12 13:58Z (CHECKER C141 850e9765 PASS), after R126, before Erratum E-1
THIRD FILL (2026-11-12T10:29:09Z by date -u, subagent; for CHECKER C141). Read at the origin heads of a git fetch of claude/referee,
claude/l-new, claude/referee-2, claude/checker and claude/vibrant-johnson-nxvvxo at 2026-11-12T10:28:19Z-2026-11-12T10:28:21Z by date -u
(before and after), rc 0 (r127c/fetch.txt, fetch.log). I merged, committed and pushed nothing, wrote nothing into the repository and did not
run scripts/push.sh or scripts/verify.sh; this file is built in the scratchpad r127c/ by fill3.py from r127b/R127-draft.md (the second fill,
sha1 419dedea37fa46bfcc64e9eb8450676f5fcf6251, asserted). HEADS: referee 33cd0fcaf6c8ce4c88b2f466aec8a20ec09626aa (2026-11-12T09:18:41Z,
«REFEREE s31: R-P-N5-SPLIT §E: fixes entries 3-4 CORRECT, line L-3 MATCHES (L-1 + R-D7a + R-U127), DATA ids resolved»), the branch head,
child of 49d34123; referee-2 98a64b91 (unchanged); checker 4fd8ef42 (unchanged); trunk 07139249 (unchanged); l-new d16cc6d7
(2026-11-12T09:16:47Z, «L-NEW successor 71: HANDOVER for park (boxes 206 E, 207 + A/B; R127 L-2/L-3; open items)»), a descendant of 621e6b77
whose diff from 621e6b77 leaves the packet, the fixes file, L-1, L-2, L-3, experiments/new/box198/ and box199/ byte-unchanged (git diff
--stat empty).
WHAT CHANGED: REFEREE 31's §E is on origin. docs/referee/R-P-N5-SPLIT.md at 33cd0fca: 169 lines, 17,961 bytes, sha1
e1bbd55b2321bff4b59591b6c144051934ad918e; its first 141 lines are 49d34123's file (prefix test); its §E, headed «§E. Fixes entries 3-4 and
line L-3 (REFEREE successor 31, Opus 5.5, D15; date -u at writing 2026-11-12T09:18Z; Lead 09:18Z byte test)» (l. 143), is l. 143-169 (git
blame: l. 142-169 are 33cd0fca's). Its verdict: «Verdict: fixes entries 3-4 CORRECT. **Line L-3 MATCHES** (= L-1 + R-D7a + R-U127 exactly).
Statements and labels unchanged (§0; §C).» (l. 169). Its byte test: «`cmp` with the lane's L-3: **EQUAL**» (l. 149), with «strings typed
from fixes entries 3-4;» (l. 148); on R-U127: «The units name the counters as split199.py computes them (entry 4 quotes its l. 31).» (l.
164). In the entry block, the three items that said pending on origin now cite §E (The RESULTS line is; Claims signed, twice; Signatures),
re-wrapped; no other entry line, the title, the GAPS preamble and the UPDATE (5bd83938…) are unchanged. The SECOND FILL section, the FIRST
FILL record, the first-fill Addendum and Addendum 2 are kept byte-unchanged as records: their words pending on origin, the G-S flag and the
ancestry list describe the second fill at 09:52Z and are superseded here.
FLAGS AND NOTES, UPDATED (my reading; CHECKER rules):
- G-S (pending on origin in the entry block): RESOLVED; the entry block's only remaining pending is the title's fill token, checker
  PENDING).
- §E OPTIONAL NOTE W86_n77: §E says «W86_n77 also has maxSPL 5 in split199.out.» (l. 166-167) and offers «(FW6_4, FW8_4, W86_n77)» if the
  line is touched again. Withdrawn by REFEREE 31 (message 10:27Z; withdrawal commit pending on origin); not carried; L-3 unaffected.
  split199.out at 621e6b77 gives W86_n77 maxSPL 2 (maxc 5); maxSPL 5 occurs on FW6_4 and FW8_4 only. Optional for CHECKER, not a line item.
- REFEREE-2 N-5 (optional, unchanged): «unit: states of the HOW3 run» is loose, not false (see the SECOND FILL section).
- G-1 (source note): unchanged and accurate as the SECOND FILL section states it: L-3 reads «with fixes entries 1-4» and «L-NEW successors
  65-67 and 69»; successor 71's entries 3-4 are line-only; note for CHECKER.
- G-4 (premise scope) and G-7 (L41 credit placement): STILL FLAGS FOR CHECKER, unchanged.
COMMITS TO MERGE BEFORE LANDING (none an ancestor of 07139249): claude/l-new 621e6b77 (or its descendant d16cc6d7); claude/referee-2
98a64b91; claude/referee 33cd0fca (2 commits not in 07139249: 49d34123, 33cd0fca); CHECKER C141's commit (not written). claude/l-si 4ded1e8d
and 2d0344d3 stay records, not needed.
SECOND FILL (2026-11-12T09:52:22Z by date -u, subagent; for CHECKER C141). Read at the origin heads of a git fetch of claude/l-new,
claude/referee, claude/referee-2, claude/checker, claude/vibrant-johnson-nxvvxo and claude/l-si at 2026-11-12T09:43:58Z-2026-11-12T09:43:58Z
by date -u (before and after), rc 0 (r127b/fetch.txt, fetch.log), after an earlier fetch of all branches at 09:42Z that moved claude/checker
7b2fa753..4fd8ef42, claude/l-comp and claude/l-lower (between 09:42:32Z and 09:43:58Z; its exact time and rc not captured), and later
fetches of claude/referee only (2026-11-12T09:49:54Z, 2026-11-12T09:57:49Z, 2026-11-12T10:00:13Z: rc 0, head unchanged). I merged, committed
and pushed nothing, wrote nothing into the repository and did not run scripts/push.sh or scripts/verify.sh; this file is built in the
scratchpad r127b/ by fill2.py from r127a/R127-draft.md (sha1 80a1f05c37f0f0b6e59d8b57e57fcd424061e93a, asserted; byte-equal to
docs/agents/R127-draft.md at 039b0558 (039b05586b20579d2c6c5dbd77b20e020940b9f8), 2026-11-12T09:42:39Z, «Lead: R127 first fill (P-N5-SPLIT
over L-1 634b2fdf @ l-new 8f4dab7e; both referees MATCH …», the Lead's record commit, a child of 07139249 that adds only that file; the
local HEAD, NOT on origin at my fetches).
HEADS. l-new 0ea262a0 (0ea262a0ecacb55f7952a5384c6dfcc1e2ef0482, 2026-11-12T08:38:04Z, «L-NEW successor 71 BOX 207 Addendum B: Lemma PAID
labelled CANDIDATE (Lead …»), the branch head, child of 621e6b77 (621e6b77397cf437f353c2195753a8beb8bed684, 2026-11-12T08:37:02Z, «L-NEW
successor 71 DUTY R-U127 (P-N5-SPLIT, R127): fixes entry 4 + line L-3 = L-2 + units (a)-(c) + …»), the commit of record; 0ea262a0 changes
docs/new/N5-RLOCAL-box207.md, box207/out/quotes207.out and notes/L-NEW.md only, and the packet, the fixes file, L-1, L-2, L-3 and
experiments/new/box198/, box199/ are byte-equal at 621e6b77 and 0ea262a0 (git diff --stat empty). L-2's commit d0a7d351
(d0a7d351865bb7b4ffdfe7a9d21befe6cc32e688, 2026-11-12T07:14:44Z, «L-NEW successor 71 DUTY R-D7a (P-N5-SPLIT, R127): fixes entry 3 + line L-2
(D7 reduced to fan-in 1 of RA with …»). referee-2 98a64b91 (98a64b91cdb76a71d3f6a7749edc78511c7d5aca, 2026-11-12T09:18:33Z, «REFEREE-2 37:
R2-P-N5-SPLIT Addendum 3 — L-3 (l-new 621e6b77, sha1 a8661c4b) MATCHES: independent rebuild …»), the branch head. referee 49d34123
(49d34123e1dd71a06d3f2b3652e839e3a808bb33, 2026-11-12T05:09:52Z), the branch head, unchanged since the first fill: no commit on
origin/claude/referee names R-P-N5-SPLIT §E or L-3, and 33cd0fca is not a git object here (git cat-file); REFEREE 31's §E is cited as
33cd0fca (pending on origin) below. checker 4fd8ef42 (4fd8ef42f30e2775504af95714816b16172ed1c5, «CHECKER C140 CLOSED: CI #7426 (43178734647)
success on the R126 landing 07139249»); docs/checker/ there and at 07139249 has no C141.md. trunk 07139249
(071392490dcea36bfa952288aa6170d45fadf874, «Lead: land R126 (P-N5-QN) after CHECKER C140 Add. 1 PASS (7b2fa753); GAPS …»). l-si 3b6ae726
(not P-N5-SPLIT; the two L-SI commits L-3 cites, 4ded1e8d and 2d0344d3, are on origin/claude/l-si).
LINE OF RECORD: docs/new/P-N5-SPLIT-line-L3.txt, COMMIT 621e6b77 (the file's only commit), FILE sha1
a8661c4b7998aafc02299c43dfe4e2c6320f73ee (git show | sha1sum; blob c8a9d17777a5545ffa34db110f9975d544ab1b11), 9,796 bytes, 9,481 characters
with its newline, one line, 273 «(» = 273 «)», 0 «|», one « — », «(2026-11-11)» once; «RA-LOG», «MW32_2, 445031d1» and «with fixes entries
1-2» 0 each. Built by experiments/new/box199/mkl3_199.py from L-2 (d8888d0b090339b80b4ce9b636a23461b476bf3f, 9,521 bytes, d0a7d351, by
mkl2_199.py from L-1). L-1 → L-3 = R-D7a (two replacements) + R-U127 (four), byte for byte (upd127b.py (4c), the strings read by ast from
mkl2_199.py and mkl3_199.py, each old string once). FIXES at 621e6b77: 134 lines, 13,865 bytes, sha1
242ade7b046515a8895c3f787eaefba1cf64c542; entry 3 (l. 77-117) appended at d0a7d351 and entry 4 (l. 119-134) at 621e6b77 (prefix tests:
8f4dab7e ⊂ d0a7d351 ⊂ 621e6b77). split.pins 61 / 63 / 65 rows at 8f4dab7e / d0a7d351 / 621e6b77; check.sh l. 1071-1085 at 621e6b77 =
0ea262a0 (sha1 f51f824e…) with the «P-N5-SPLIT» block asserting L-3's row (a8661c4b…, DOCS/P-N5-SPLIT-line-L3.txt) in split.pins (at
d0a7d351 it asserted L-2's row, sha1 f802050e…). The packet docs/new/P-N5-SPLIT.md is sha1 5bc1b1f3… at 399cda07, 63515442, 8f4dab7e,
d0a7d351, 621e6b77, 0ea262a0 and 07139249 (untouched).
WHAT CHANGED SINCE THE FIRST FILL. The first fill (80a1f05c) was not routed to CHECKER: its FLAGS proposed R-D7a / R-D7b for G-L43 (D7) and
noted D7's missing unit and the maxima clauses' missing units (G-9). The Lead RULED before CHECKER, and the lane applied both rulings as
line-only fixes entries. R-D7a: «Fixes entry 3 (L-NEW successor 71; Lead ruling R-D7a 07:12Z 2026-11-12, L43; written 2026-11-12T07:14Z by
date -u)» (l. 77), «ACCEPTED as ruled.» (l. 82), «Ruling R-D7a (Lead, line-only), applied verbatim» (l. 83); its strings are the first
fill's R-D7a proposal (fill2.py asserts the old string, the new D7 and the DATA insertion of mkl2_199.py in the first fill's FLAGS text).
R-U127: «Fixes entry 4 (L-NEW successor 71; Lead ruling R-U127 07:58Z 2026-11-12, DATA rule; written 2026-11-12T08:36Z by date -u)» (l.
119), «Ruling R-U127 (Lead): «every DATA clause names its counter … units (a), (b), (c) exactly as you proposed in entry 3, and the source
note «with fixes entries 1-2» → «with fixes entries 1-4»», with (a) in the FIRST «max c_y».» (l. 120-121), «ACCEPTED; applied verbatim, line
only:» (l. 121) (the units are entry 3's proposals, «Lead's second ask (the three maxima clauses and the DATA rule), PROPOSED, NOT APPLIED
(L-2 carries R-D7a only)» (l. 108)). L-2 = L-1 + R-D7a; L-3 = L-2 + R-U127 («L-1 → L-3 = R-D7a + R-U127.» (l. 132-133)). The entry block,
GAPS preamble and UPDATE now follow L-3; history mentions of L-1 (its byte tests, the referees' MATCH on L-1, the first fill's re-runs) are
kept and marked as L-1's.
REFEREES ON L-3. REFEREE-2 successor 37, docs/referee-2/R2-P-N5-SPLIT.md at 98a64b91: 511 lines, 45,717 bytes, sha1
6070dff1168e1a3f0f30368c84a2102e6a9f7def; its first 469 lines are c5bc1365's file (prefix test); its Addendum 3 is l. 471-511 (git blame: l.
470-511 are 98a64b91's), headed «Addendum 3 (REFEREE-2 successor 37, Opus 5.5 under D1; 2026-11-12 by date -u): byte test of fixes entries
3-4 + line L-3 (claude/l-new 621e6b77)» (l. 471). Its verdict: «Verdict: L-3 (621e6b77, sha1 a8661c4b) MATCHES. L-1 → L-3 is exactly rulings
R-D7a and R-U127, as stated in fixes entries 3-4, and every new DATA number and unit is correct. P-N5-SPLIT's signed statements are
unchanged.» (l. 509-510). Its rebuild: «R2-P-N5-SPLIT/bt_l3.py (my code; mkl2_199.py and mkl3_199.py not imported)» (l. 478); «Result: sha1
a8661c4b…, 9,796 B, BYTE-EQUAL to the lane's L-3 (cmp equal).» (l. 483); «Diff L-1 → L-3, word level: 10 regions, all inside the six
replacements.» (l. 484). REFEREE successor 31: §E, commit 33cd0fca (pending on origin): the Lead's brief says it MATCHES L-3, but it was not
on origin/claude/referee at 2026-11-12T09:43:58Z or at my later fetches of claude/referee (2026-11-12T09:49:54Z, 2026-11-12T09:57:49Z,
2026-11-12T10:00:13Z: rc 0, head unchanged; head 49d34123, the first fill's), so I cannot quote its verdict or its line numbers; CHECKER
reads it once it is on origin.
ANCESTRY (git merge-base --is-ancestor against origin trunk 07139249). Ancestors (True): every commit the first fill named as one (399cda07,
63515442, 8f4dab7e; ca091557, 8c395bff; 15a05bf0, 026de5fb, b0b7c3f3, 4948ce5d, 991296c9, c708c968, c5bc1365; 93531b03), among them
4948ce5d, which L-3's DATA clause names. NOT ancestors, and needed before landing: claude/l-new 621e6b77 (fixes entries 3-4, L-2, L-3,
mkl2_199.py, mkl3_199.py, split.pins 65 rows, check.sh's L-3 assert; 6 commits not in 07139249: 8d6c363b, 9b6f6f44, 2d599a09, d0a7d351,
b72411cf, 621e6b77; the head 0ea262a0 adds box 207 Addendum B), claude/referee-2 98a64b91 (Addendum 3; 3 commits: 93413fc6, 3282fc6c,
98a64b91), claude/referee's §E commit 33cd0fca once it is on origin (the head 49d34123 is 1 commit not in 07139249), and CHECKER C141's
commit (not written; claude/checker 4fd8ef42 is 2 commits not in 07139249: ad06352c, 4fd8ef42). Not ancestors and not needed: claude/l-si
4ded1e8d and 2d0344d3, which L-3's DATA clause cites as sources of DATA, not premises (the C138 §5 ruling on cited lane commits, applied in
the first fill to L-RED 60-62's), and the Lead's record commit 039b0558 (a docs/agents draft).
CHECKS RUN AT THIS FILL (scratch r127b/; nothing written into the repository). (a) mk.out: the lane chain from a git archive of 621e6b77
(packet, fixes file, experiments/new/box199; no line file copied): mkl1_199.py with RESULTS at 07139249, then mkl2_199.py, then mkl3_199.py,
2026-11-12T09:45:12Z-2026-11-12T09:45:12Z, rc 0 each, «L-3 written: sha1 a8661c4b7998aafc02299c43dfe4e2c6320f73ee 9796 B»; L-1, L-2 and L-3
cmp SAME with the committed files. (b) The check.sh blocks «BOX 199 SPLIT» and «P-N5-SPLIT» (l. 1071-1085 at 0ea262a0 = 621e6b77,
tools/blocks199.sh, run by tools/runblocks.sh) from a FULL git archive of 0ea262a0 (r127b/arch/, 47,724 files = git ls-tree -r):
2026-11-12T09:45:49Z-2026-11-12T09:45:55Z, rc 0, «BOX 199 SPLIT: SPLIT / REWIN / REWIN-HI / PAIR-SPLIT / SPLIT-COUNT / RW-1 counters 0, DEAD
witnesses present, controls fire = frozen: PASS» and «P-N5-SPLIT: packet and 65 pinned files match split.pins, line L-3 a8661c4b pinned:
PASS». NEGATIVE CONTROL 1: one byte appended to the archive's L-3, the «P-N5-SPLIT» block alone (tools/blocksplit.sh),
2026-11-12T09:46:03Z-2026-11-12T09:46:03Z, rc 1, «P-N5-SPLIT check: FAILED» / «../../../docs/new/P-N5-SPLIT-line-L3.txt: FAILED»; L-3
restored (sha1 a8661c4b again) and the block re-run: PASS, rc 0. NEGATIVE CONTROL 2: one byte prepended to the archive's box199/check199.out
(pinned in split.pins, row 9), the «BOX 199 SPLIT» block alone (tools/blockbox.sh), 2026-11-12T09:46:03Z-2026-11-12T09:46:15Z, rc 1, «BOX
199 SPLIT check: FAILED (check199.sh exit 0)»; file restored (cmp-equal to its backup) and both blocks re-run: rc 0, both PASS. (c)
tools/upd127b.py (upd127b.out): the UPDATE by R118's procedure from L-3 with NO reading, sha1 5bd83938b1dfb6603581fc98669593ae2e09c83e (no
newline), 9828 bytes; the three controls (R124, R125, R126 landed UPDATEs on 07139249) True; two negative controls raise; UPDATE(L-1) = the
first fill's b7601151… with the six replacements = UPDATE(L-3), True. (d) tools/prem127b.py (prem127b.out): L-3's premise parenthesis is
byte-equal to L-1's (906 characters) and so is its text before « — »; the 17 names cited «as RESULTS R125» are each in landed R125's title
(0 missing; made-up names F7, LOC-GATE4: 0); RESULTS R-ids L-3 cites: R21, R104, R117, R118, R125, all landed, none above R125 (other
R-tokens: R2 in the file name R2-P-N5-SPLIT; R226-R228, L-RED reports). (e) tools/data127b.py (data127b.out): 40 checks OK, «DATA EQUAL», on
the archive of 0ea262a0; D1-D7 each name counter and «unit:»; the DATA clauses split at top-level «;»: see FLAGS (G-9). tools/src127b.py
(src127b.out): R-D7a's DATA against its cited sources, with negative controls. (f) tools/chk127b.py, lp127b.py, hex127b.py and sim127b.py:
Addendum 2.
FLAGS OF THE FIRST FILL, UPDATED (my reading; CHECKER rules):
- G-L43 (D7): RESOLVED by ruling R-D7a (L-3). L-3's D7 is «D7 fan-in 1 of RA as a game property (NK6_cl21, 408b9988, fan-in 3; DSALT9_n416,
  da3308b5, fan-in 4; unit: max over (v, I, y) of the number of letters of RA(y), box198/pair198.out maxRA)», an explicit bound exceeded by
  named instances (data127b.py: pair198.out maxRA 3 and 4); RA depth and multiplicity are DATA with sources (src127b.py). R-D7b not taken.
- G-9 (D-unit note: D7 and the three maxima without «unit:»): RESOLVED by R-U127 and R-D7a; each maximum names its split199.out field (maxc,
  maxSPL, T3) and D7 its pair198.out field. Clauses still without a counter field or «unit:» (data127b.py, DATA clauses [1]-[9]): [5] the
  R-D7a DATA clause («RA depth (longest RA chain) 4 / 8 / 12 / 16 on FW4/8/12/16_2 …», «the per-pair multiplicity n on MW(n) …»: quantities
  in words, numbers and source commits, no field, no «unit:»; the ruling's own string); [8] the cited replays («every fail counter 0, cited,
  not re-run»); [9] the attack record; [1], [2] and [7] are a remark on controls, the control values (fields named) and a caveat. Note for
  CHECKER; no line change proposed.
- G-4 (premise scope, six items from P-N5-CHAIN's frozen text): STILL FOR CHECKER, as in the first fill; L-3's premise parenthesis is
  byte-equal to L-1's.
- G-7 (L41: the referee-originated credit sits in the premise parenthesis, not after « — »): STILL FOR CHECKER; unchanged in L-3 (its text
  before « — » is L-1's).
- G-1 (source note): L-3 reads «with fixes entries 1-4» (R-U127 (d)) and still «L-NEW successors 65-67 and 69»; successor 71 wrote the
  line-only entries 3-4. As R126's N-S (landed with a source note naming the proof-bearing entries' successors); note for CHECKER.
- G-S AT THIS FILL (FLAG for the Lead): the entry block says pending on origin four times (REFEREE §E, 33cd0fca: The RESULTS line is, Claims
  signed twice, Signatures), stale at landing by construction; once §E is on origin, a third pass (fill2.py stops when it finds §E there)
  replaces them with §E's full SHA, its line numbers and its verdict sentence. L-3 itself has no stale status word (chk127b.py [G-S]).
- G-R125 MET, G-U, G-T CLEAN, G-6 and G-2 notes, G-DE, G-P and G-0 (C141 unused: no docs/checker/C141.md at 4fd8ef42 or 07139249) as in the
  first fill, re-checked on L-3 (Addendum 2).
OPTIONAL NOTES FOR CHECKER (no line change):
- REFEREE-2 N-5 (Add. 3): «Optional N-5: T3 is the last state's index (= the number of steps); the run has T3 + 1 states. «unit: states of
  the HOW3 run» is loose, not false.» (l. 499-500); also ««199 on MW32_2» is right: split199.out's largest T3 is 199.» (l. 501)
- REFEREE (§E, 33cd0fca, pending on origin; relayed by the Lead, not read): W86_n77 also maxSPL 5. NOT CONFIRMED on the lane's output: at
  621e6b77 box199/split199.out row 28, W86_n77 has maxSPL 2 (maxc 5, T3 19), and maxSPL 5 occurs on FW6_4 and FW8_4 only (data127b.py, «max
  split pairs 5 on FW6_4, FW8_4 only (maxSPL)» OK). If §E counts on its own engine, CHECKER compares its unit with split199.py's maxSPL.
Changes at this fill, and nothing else: line 1; this section (new); the title (L-3); in the entry block (166 lines in the first fill):
Object, Fixes, The RESULTS line is, Claims signed, Setting (fixes entries 1-4) and (h), Premise, L41 and L43, Referee strengthening (iii),
Honest limits (vii), (x), (xi), Data, Signatures, INDEPENDENCE, TARGET.md diff; the GAPS preamble (built from L-3 by upd127b.py) and the
UPDATE; Addendum 2 (new, at the end). The FIRST FILL record (from the line that begins FIRST FILL (this text) to the L-1 SHAPE line, with
its blank line) and the first fill's Addendum are kept byte-unchanged: where they call L-1 the title or the line of record, raise G-L43 or
the D7 unit as flags, or give counts, slices, the UPDATE sha1 (b7601151…) and the block run (61 pinned files), they describe draft 80a1f05c
at 06:54Z-07:05Z; the Lead ruled at 07:12Z and 07:58Z, and the entry block now follows L-3.
FIRST FILL (this text). Built by script (r127a/fill1.py) in the scratchpad r127a/ for the Lead to copy to docs/agents/R127-draft.md; nothing
  in the repository was edited, committed, merged or pushed by me, and scripts/push.sh and scripts/verify.sh were not run (a push was
  running in the repository; I used read-only git and git archive only). Read at the origin heads of one git fetch of claude/l-new,
  claude/referee, claude/referee-2, claude/checker, claude/l-red and claude/l-si at 2026-11-12T06:45:35Z-2026-11-12T06:45:37Z by date -u
  (before and after), rc 0 (r127a/fetch.txt, fetch.log; it moved only l-si 10e0554e..9a490206). After it, another process moved
  origin/claude/l-red to 52606148 (d27b8f5d, 52606148: L-RED notebook and R231 (b2), not P-N5-SPLIT objects); every head below is the one my
  fetch gave and an ancestor of the current ref.
HEAD l-new 9b6f6f44 (9b6f6f44d804b324aa7e1d0da30a30ab2b9cd0fd, 2026-11-12T05:49:11Z, «L-NEW successor 71 BOX 206 Addendum E: (E1) R118 (a)
  added to LOUD-SPLIT and DEPTH-COUNT premise lists (quoted by script from trunk b3d7294c); (E2) DE…»).
HEAD referee 49d34123 (49d34123e1dd71a06d3f2b3652e839e3a808bb33, 2026-11-12T05:09:52Z, «REFEREE s31: R-P-N5-GATE §K: fixes entry 4 CORRECT,
  line L-4 MATCHES (L-3 + LT-1 landing-order form + GL-1..GL-3)»).
HEAD referee-2 3282fc6c (3282fc6c2450efe4b01ed4ad2441ff8c67a1cd9d, 2026-11-12T05:40:10Z, «REFEREE-2 37: R2-P-N5-GATE Addendum 4 — spot
  replay on IDEAL-CYC: MW32_2 C 65 = 2n+1, flips 130; FW16_2 C 3; all must-0 counters 0»).
HEAD checker 7b2fa753 (7b2fa753a68a971eb64827fa25f59bdba4424104, 2026-11-12T06:15:21Z, «CHECKER C140 Add. 1: R126 (P-N5-QN) second fill on
  L-2 166e4695 PASS (trunk 7f7ee70e, draft 946f929a; UPDATE 89c5f357; blocks rc 0 from archive 70501a…»).
HEAD l-red c80e4fb2 (c80e4fb2d6433696d02d68122d2af45434a4711e, 2026-11-12T06:14:50Z, «L-RED R231 item (b): two gated re-arm designs vs
  DEEP-k1 (CWG1-4, n 4/8/16, frozen): static exit one-shot, dynamic exit (hv) = race trap; none beats C…»).
HEAD l-si 9a490206 (9a4902065cc91da2c223b9f1e91b7382e638f97a, 2026-11-12T05:12:38Z, «L-SI successor 50: handover (P-N5-GATE L-4 with both
  referees; BONLY3 withdrawn; box 99 in flight) + box 99 tools (scc99 SCC census)»).
No P-N5-SPLIT object changed after its last commit: the packet, the fixes file, L-1, experiments/new/box199/ and box198/ are byte-equal at
  8f4dab7e, at the l-new head 9b6f6f44 and at trunk 07139249 (git diff --stat empty both ways); docs/referee/R-P-N5-SPLIT.md (141 lines,
  sha1 d8d1df41ab01b2d819dfa5591dab0503650c6d7a) is byte-equal at 8c395bff, at the referee head 49d34123 and at 07139249;
  docs/referee-2/R2-P-N5-SPLIT.md (469 lines, sha1 186330d67b56f502782005e93c47896758a9faf9) at c5bc1365, at the referee-2 head 3282fc6c and
  at 07139249. The brief's facts were checked by script (this file's asserts and the tools): every one MATCHES except where BRIEF FACTS
  below say otherwise.
LINE OF RECORD: docs/new/P-N5-SPLIT-line-L1.txt, COMMIT 8f4dab7e (8f4dab7eedf632002351ff1071df46300d82a0b9, 2026-11-11T22:57:03Z, «L-NEW 69:
  P-N5-SPLIT fixes entry 2 + line L-1 — SP-1 = W-1 ((LEX-Λ) only on non-core vertices), SP-2 = R-6 citation form…»), the file's only commit;
  FILE sha1 634b2fdfda31eda9e82e9f558ffebf3c89f5701c (git show | sha1sum; blob 726d0c5d9bb740b2f3f146f425cc3f2fc18c7e5b), 9,249 bytes, one
  line with its newline, 260 «(» = 260 «)», 0 «|», one « — », «(2026-11-11)» once.
PACKET: docs/new/P-N5-SPLIT.md FROZEN at 399cda07 (399cda074b2c93200b531bdbfec5ec15078ab9bd, 2026-11-08T23:38:56Z, «L-NEW PACKET P-N5-SPLIT
  FROZEN (boxes 197-199: SPLIT + TRANSFER, REWIN, REWIN-HI, PAIR-SPLIT, SPLIT-COUNT (SPL…»), the file's only commit; sha1
  5bc1b1f390ed81683fe5c93008c7ea0b338fe735, 275 lines, 30,949 bytes. FIXES: docs/new/P-N5-SPLIT-fixes.md, two commits only: entry 1 at
  63515442 (63515442c4d3a6f70a81de7fe9b828d429db9c9f, 2026-11-09T00:44:26Z; 14 lines then), entry 2 + the «Line L-1» note at 8f4dab7e (75
  lines, 7,523 bytes, sha1 f7940ddf3361d45407855ce51baddc9e59515426); entry 2 is append-only (the 63515442 text is a byte prefix of the
  8f4dab7e text; git diff removes no line). GENERATOR experiments/new/box199/mkl1_199.py (8f4dab7e). PINS experiments/new/box199/split.pins:
  61 rows at 8f4dab7e (58 at 399cda07, 59 at 63515442; the two added at 8f4dab7e are L-1 and mkl1_199.py, and the fixes row is re-pinned).
REFEREES (git blame at the heads). REFEREE docs/referee/R-P-N5-SPLIT.md: l. 1-108 the first review ca091557
  (ca091557e43f2a9c6cce3baaa573260dd5e39e3e, 2026-11-09T09:28:06Z, «REFEREE successor 30: R-P-N5-SPLIT first review (all SIGN, cond. R125;
  SP-1 LEX-Λ = W-1 class, L41 clause; SP-2 citation; own replay 0)»); l. 109-141 §C 8c395bff (8c395bffe0f1b0f31f7533715909341914c833b7,
  2026-11-11T23:29:45Z, «REFEREE s31: R-P-N5-SPLIT §C: fixes entry 2 CORRECT, line L-1 MATCHES; R125 citation ruled acceptable as a
  landing-order condition»). REFEREE-2 docs/referee-2/R2-P-N5-SPLIT.md: l. 1-82 box 1 15a05bf0, l. 83-152 box 2 026de5fb, l. 153-217 box 3
  b0b7c3f3, l. 218-240 and l. 252-351 boxes 4-5 4948ce5d (4948ce5d650b8ef81a15fb6489b39ef5e21854af, 2026-11-09T10:44:20Z; the verdict table
  l. 329-347), l. 241-251 the final sweep 991296c9 (991296c97739d8547403288158fabbb181ae9e7c, 2026-11-11T22:34:15Z), l. 352-384 Addendum 1
  c708c968 (c708c96804dc3b73757bc891e2b1cb079d958fb9, 2026-11-11T22:34:50Z), l. 385-469 Addendum 2 c5bc1365
  (c5bc13653b1cfad96213249f9781d6277620fadb, 2026-11-11T23:42:02Z, «REFEREE-2 37: R2-P-N5-SPLIT Addendum 2 — L-1 (l-new 8f4dab7e, sha1
  634b2fdf) MATCHES R-1..R-6 (rebuild byte-equal; bt_l1.py 36 PASS; DATA ru…»).
BOTH REFEREES SAY L-1 MATCHES (VERIFIED). REFEREE 31 §C (8c395bff) l. 140-141 «Verdict: fixes entry 2 CORRECT. **Line L-1 MATCHES** the
  packet read with fixes entries 1-2 and my LS-1..LS-8, SP-1, SP-2. Statements and labels as in §0 (all SIGN, conditional on R125).».
  REFEREE-2 37 Addendum 2 (c5bc1365) l. 465 «Verdict: L-1 (8f4dab7e, sha1 634b2fdf) MATCHES. R-1 to R-6 are met in bytes and in meaning, and
  fixes entry 2 changes no signed statement.». SIGN verdicts: REFEREE 30 (ca091557) l. 19 «No GAP; nothing refused. SP-2 is a citation
  requirement for the line, not a gap. TARGET.md diff CLEAN (§6).»; REFEREE-2 36 (4948ce5d) l. 346 «No statement is REFUSED, and no gap is
  left open in any signed proof.»; and Addendum 1 (c708c968) l. 383 «Result: P-N5-SPLIT has two referee signatures on every statement,
  CONDITIONAL on R125.».
BRIEF FACTS THAT DID NOT MATCH, OR NEED A QUALIFIER: (1) the brief's "R126 = P-N5-QN just landed there; not yet on origin": my local ref
  origin/claude/vibrant-johnson-nxvvxo is 7f7ee70e (I did not fetch the trunk), and 07139249 is not its ancestor: consistent with the brief,
  not re-checked on the remote. (2) the brief names REFEREE 31's file part «§C»: it is l. 110-141 (blame 109-141, l. 109 blank), with the
  first review l. 1-108 by REFEREE 30 (ca091557); REFEREE-2 37's Addendum 2 is l. 386-469 (blame 385-469), Addendum 1 (c708c968) and the
  verdict table (4948ce5d) are REFEREE-2 36's. (3) the brief's "premises only from landed RESULTS (R1-R126)": L-1 cites six items, (R), (P),
  (E-DOM), (Core), F2 and CYC, from «P-N5-CHAIN's frozen text (l-new 93531b03, sha1 6e613ba7, §2 and §4)», a lane packet (the object of
  landed R125), not a RESULTS text (G-4 below). Everything else in the brief matched: trunk 07139249, R126 at RESULTS l. 15726-15901,
  Erratum E-1 at l. 15903, 16,545 lines, 1,477 «|»; GAPS l. 11 76 «|» ending with R126's UPDATE; packet frozen at 399cda07 (its only
  commit); fixes entries 63515442 and 8f4dab7e; L-1 at 8f4dab7e, sha1 634b2fdf…; the generator box199/mkl1_199.py; both referees MATCH L-1;
  C141 unused (G-0).
ANCESTRY (git merge-base --is-ancestor against trunk 07139249): the packet, fixes and line commits 399cda07, 63515442, 8f4dab7e; REFEREE's
  ca091557, 8c395bff; REFEREE-2's 15a05bf0, 026de5fb, b0b7c3f3, 4948ce5d, 991296c9, c708c968, c5bc1365; P-N5-CHAIN's frozen text 93531b03
  (the six P-N5-CHAIN items of L-1); the trunk commits the generator and REFEREE-2 assert the TARGET tail against (8ba1b23b, 86f62c26): ALL
  ancestors (True). NOT ancestors (True): L-RED 60-62's report commits named in the packet §9.2 and fixes entry 1 (677b4edb, 1c802d82,
  1ea37d91, c482e0d8, 0eb43a7a, 68639e7a, 6540fbb6, 4b309716, f3903cb8, 6080533a, 4b06129e, 0657d38f) and L-SI 47's box 90 commits (4ded1e8d
  FW, 2d0344d3 MW, named in box 199 Add. 3 and in L-SI's log, not in L-1). L-1 names none of these commits: it cites «attack record L-RED
  60-62 (R226, R227, R228; all PROVED statements SURVIVE)» and «L-SI DATA cited» as records, not premises. So for P-N5-SPLIT NOTHING needs a
  merge before landing; what must exist first is CHECKER C141's commit (merge claude/checker at it before landing, as for C137-C140).
BASE: trunk 07139249 (071392490dcea36bfa952288aa6170d45fadf874, 2026-11-12T06:44:27Z, «Lead: land R126 (P-N5-QN) after CHECKER C140 Add. 1
  PASS (7b2fa753); GAPS line-11 UPDATE; log 05:08Z…»), R126 landed: RESULTS sha1 0ef236b9b7146cd19fcc380c4fcd2a7314aec402, 16,545 lines,
  1,477 «|»; «### R126» l. 15726-15901 (blank l. 15902), the line-start «**Erratum E-1** (not a result» l. 15903 (the only one); GAPS sha1
  2965fc2ec61b5ddebc529d9ee21c285100914940, 23 lines, l. 11 76 «|», its last UPDATE R126's («UPDATE 2026-11-12 06:44Z: RESULTS R126
  (P-N5-QN; CHECKER C140 7b2fa753)»). No simulated base is needed (no unlanded predecessor; L-1 cites no RESULTS id above R125).
SOURCES READ: the packet (399cda07) in full; the fixes file (8f4dab7e) in full; L-1 in full; mkl1_199.py; check.sh l. 1071-1085 (8f4dab7e);
  box199/split199.out, check199.out, inst/SHA1SUMS, box198/pair198.out (by data127a.py); box 199's Addendum 3 (N5-SPLIT-box199.md l.
  336-362) and box 198 (N5-PAIR-box198.md l. 17-65) for RA-LOG; REFEREE's R-P-N5-SPLIT.md in full; REFEREE-2's R2-P-N5-SPLIT.md l. 1-80 and
  l. 217-469; P-N5-CHAIN.md (93531b03) §2 and §4; RESULTS (07139249) R21 (a) l. 933, R104 l. 9864, R117 l. 13362, R118 (b) l. 13682, R125 l.
  15595-15724, R126 l. 15726; GAPS l. 11; DECISIONS L41 (l. 355-360), L43 (l. 369-374); docs/checker/C140.md (07139249); the R126 first fill
  (4c2f407d) and its tools r126a/ and r126b/ (adapted).
CHECKS RUN AT THIS FILL (scratch r127a/; outputs there). (a) The check.sh blocks «BOX 199 SPLIT» and «P-N5-SPLIT» (check.sh l. 1071-1085 at
  8f4dab7e, the same 15 lines at 399cda07, 63515442, 07139249 and the l-new head; = tools/blocks199.sh, run by tools/runblocks.sh) from a
  FULL git archive of 8f4dab7e (r127a/arch/, every path of the tree): 2026-11-12T06:47:46Z-2026-11-12T06:47:52Z by date -u, rc 0, output
  «BOX 199 SPLIT: SPLIT / REWIN / REWIN-HI / PAIR-SPLIT / SPLIT-COUNT / RW-1 counters 0, DEAD witnesses present, controls fire = frozen:
  PASS» and «P-N5-SPLIT: packet and 61 pinned files match split.pins: PASS». Negative control 1: one byte appended to the archive's L-1, the
  «P-N5-SPLIT» block alone (tools/blocksplit.sh): 2026-11-12T06:48:00Z-2026-11-12T06:48:00Z, rc 1, «P-N5-SPLIT check: FAILED» /
  «../../../docs/new/P-N5-SPLIT-line-L1.txt: FAILED»; byte restored (sha1 634b2fdf again) and the block re-run PASS (rc 0). Negative control
  2: one byte prepended to the archive's box199/check199.out (a pinned output), the «BOX 199 SPLIT» block alone (tools/blockbox.sh):
  2026-11-12T06:48:00Z-2026-11-12T06:48:07Z, rc 1, «BOX 199 SPLIT check: FAILED (check199.sh exit 0)»; file restored (cmp equal to its
  backup) and both blocks re-run PASS (rc 0). (b) mk.out: the lane generator mkl1_199.py from a git archive of 8f4dab7e (docs/new,
  experiments/new/box199), run with RESULTS at 07139249 (R126 landed) as its argument: rc 0, «ok sha1
  634b2fdfda31eda9e82e9f558ffebf3c89f5701c 9249 bytes; parens 260 260», L-1 rewritten byte-equal (cmp SAME). (c) tools/upd127a.py: the
  UPDATE by R118's procedure, with three controls (R124, R125, R126 on 07139249) and two negative controls (upd127a.out). (d)
  tools/prem127a.py: L-1's named premises at 07139249 with negative controls (prem127a.out). (e) tools/data127a.py: L-1's DATA and DEAD
  figures against the pinned outputs (data127a.out). (f) tools/chk127a.py (title, block, UPDATE, tokens, pipes, anchors, stale grep, quote
  sweep with a negative control), tools/lp127a.py (every quote of this file at its cited file, commit and lines, two negative controls),
  tools/hex127a.py (every hex id, negative control) and tools/sim127a.py (landing simulation on 07139249): Addendum.
LESSONS APPLIED (R126's fills, C140 and earlier). C113 E-1 / C133 E-1: the title is L-1 verbatim (CLEAN). C133 E-3 / C138 E-1 / C139 E-1:
  R118's procedure runs with no reading (G-U: CLEAN). C118 E-1 / C139 E-2: no status word stale at landing (G-S: CLEAN). L43 / C140 E-1
  (G-L43: FLAG, D7). L41 / C140 G-7 (G-7: note). C134 N-S (G-1: CLEAN). C115 E-1 / C140 G-4: premises landed only (G-4: FLAG, six P-N5-CHAIN
  items). REFEREE §C's landing condition on R125 (G-R125: MET). C120-C140: every DATA clause against its counter (G-9: EQUAL; one note).
  C122 G-0: parentheses. C130 G-P: the UPDATE builder with controls on the last landed UPDATEs. C132 Add. 1: block re-run times as a date -u
  interval.
FLAGS FIRST (my reading; CHECKER rules; strings below are PROPOSALS only).
- G-L43, D7 CARRIES TWO ASYMPTOTIC STATEMENTS REFUTED ONLY ON FINITELY MANY INSTANCES (FLAG; the class of C140 E-1, which ruled R-D2a on
  R126). L-1: «D7 fan-in 1 of RA and RA-LOG / bounded multiplicity as game properties (NK6_cl21, 408b9988, fan-in 3; DSALT9_n416, fan-in 4;
  FW16_2, 94df42b7, linear RA depth; MW32_2, 445031d1, multiplicity n, L-SI DATA cited)». DECISIONS L43 (07139249 l. 370-371): «it enters as
  DATA with its numbers and source commit, or not at all»; «in a landing line needs a refereed proof, or one instance exceeding an EXPLICIT
  bound (as R90's REP-LIN, 570 > 538)». D7 bundles three claims: (i) «fan-in 1 of RA» (RA(y) has at most one letter, an EXPLICIT bound;
  NK6_cl21 3 and DSALT9_n416 4 exceed it; lane DATA pair198.out maxRA 3 / 4, data127a.py; REFEREE-2 re-ran it, ««fan-in 1» is DEAD.» (l.
  283)): CLEAN. (ii) «RA-LOG»: box 198's «CONJECTURE RA-LOG: for every genome G with [E-LEV], every (v, I) and letter y, the longest
  RA-chain from y has O(log(N + M)) letters.» (N5-PAIR-box198.md l. 63, 8f4dab7e), an unspecified constant; L-1's kill is «FW16_2, 94df42b7,
  linear RA depth», one instance, no number and no source commit; the depth data are L-SI 47's (box 199 Add. 3 «Lead 19:58Z relays L-SI 47
  BOX 90, claude/l-si 4ded1e8d: FW staircase family, RA-LOG and (S2) DEAD» (l. 336), claude/l-si 4ded1e8d, not an ancestor of 07139249), the
  lane measured no RA depth on FW (box199 / box198 outputs have no FW RA row, data127a.py), and REFEREE-2 re-ran four instances, «The
  longest RA chain (counting y) on FW4/8/12/16_2 is 4 / 8 / 12 / 16: linear in the family parameter.» (l. 282). (iii) «bounded
  multiplicity»: L-SI's CONJECTURE RA-MULT(K) (K an absolute constant, box 199 Add. 3 «Consistent with L-SI's per-pair multiplicity m(y, z)
  ≤ 2 (relayed; CONJECTURE RA-MULT(K))» (l. 360)); L-1's kill is «MW32_2, 445031d1, multiplicity n, L-SI DATA cited», one instance, no
  number, no commit, re-run by neither referee (REFEREE-2 «The multiplicity m(y, z) = n on MW is L-SI's census. I did not compute it; it is
  cited DATA of another lane and not a premise.» (l. 283-284); REFEREE «D1, D2, D4, D5, D6 reproduced by the lane's check199.sh (lane code,
  re-run, byte-equal); D3, D7 cited, not re-run» (l. 18)). So (ii) and (iii) are the L43 case: «DEAD» with neither a refereed proof nor an
  instance beyond an explicit bound. D1-D6 are not (each is a structural claim with no constant, killed by a named instance and counter:
  CLEAN). PROPOSED (one of; CHECKER chooses or rules no action): R-D7a (keep the explicit part, carry the rest into DATA, as C140's R-D2a +
  R-S) "D7 fan-in 1 of RA and RA-LOG / bounded multiplicity as game properties (NK6_cl21, 408b9988, fan-in 3; DSALT9_n416, fan-in 4; FW16_2,
  94df42b7, linear RA depth; MW32_2, 445031d1, multiplicity n, L-SI DATA cited)" → "D7 fan-in 1 of RA as a game property (NK6_cl21,
  408b9988, fan-in 3; DSALT9_n416, da3308b5, fan-in 4; unit: max over (v, I, y) of the number of letters of RA(y), box198/pair198.out
  maxRA)" and, in the DATA clause after «max split pairs 5 (FW6_4, FW8_4);», add "RA depth (longest RA chain) 4 / 8 / 12 / 16 on
  FW4/8/12/16_2 (REFEREE-2 36 R2-P-N5-SPLIT, claude/referee-2 4948ce5d, own engine; L-SI 47 box 90, claude/l-si 4ded1e8d) and the per-pair
  multiplicity n on MW(n) (L-SI 47 box 90, claude/l-si 2d0344d3, not re-run by the lane or a referee), DATA only;"; R-D7b (drop) "D7 fan-in
  1 of RA and RA-LOG / bounded multiplicity as game properties (NK6_cl21, 408b9988, fan-in 3; DSALT9_n416, fan-in 4; FW16_2, 94df42b7,
  linear RA depth; MW32_2, 445031d1, multiplicity n, L-SI DATA cited)" → "D7 fan-in 1 of RA as a game property (NK6_cl21, 408b9988, fan-in
  3; DSALT9_n416, da3308b5, fan-in 4)". Either is a line change both referees re-sign. Old string once in L-1 (fill1.py asserts). The L-SI
  commits in R-D7a are not ancestors of 07139249 (records, as C138 §5 ruled for L-RED commits); R-D7b needs none.
- G-4, PREMISE SCOPE (FLAG for CHECKER; the C115 E-1 class; precedent C140 G-4 for a non-premise lane quote). L-1's premise parenthesis
  cites: 17 facts «as RESULTS R125 (P-N5-CHAIN)» (each named in landed R125's title, RESULTS l. 15595 at 07139249, prem127a.py: 17 of 17, 0
  missing); [DEF] = RESULTS R104 (l. 9864), [G3] = RESULTS R117 (l. 13362), [OPT] = RESULTS R118 (b) (l. 13682) and RESULTS R21 (a) (l.
  933); and «(R), (P), (E-DOM), (Core) in its W-1-repaired reading (…), F2 and CYC: P-N5-CHAIN's frozen text (l-new 93531b03, sha1 6e613ba7,
  §2 and §4)», which are P-N5-CHAIN.md l. 91, 93, 96, 97 (§2) and l. 165, 166 (§4) at 93531b03 (an ancestor of 07139249; the file is
  byte-equal at 07139249), a LANE PACKET, the object of landed R125, not a RESULTS text: landed R125's title names none of F2, (Core),
  (E-DOM), (R), (P) (its block names F2 once), as fixes entry 2 says («R125's line (L-4 a69c8aa9, L-5 473344b1) does not contain F2, (Core),
  (E-DOM), [G3], [DEF], (R) or (P)», l. 37) and both referees required (REFEREE SP-2 «cite these as P-N5-CHAIN's frozen text (sha1 6e613ba7)
  or their landed sources ([DEF] R104, [G3] R117, [OPT] R118 (b) + R21 (a)), with (Core) in the W-1 repaired reading» (l. 29-30); REFEREE-2
  R-6 adopted, Add. 1 l. 372). Both referees re-derived the six (REFEREE §1 «Re-derived here: F2 ([VJ] compares the reward of Λ first;
  priorities are injective by rank, so distinct cycle nodes have distinct rewards)» (l. 27-28); REFEREE-2 box 1 l. 24-28, «All 30 are
  defined, each in the section SPLIT gives»). So the six are premises from outside landed RESULTS, cited exactly and signed as used by both
  referees, unlike R126's one quote, which was not a premise. L-1's own words «not used: any other packet» must be read as other than
  P-N5-CHAIN. CHECKER's call: accept as P-N5-CHAIN's frozen text signed under R125 (the referees' SP-2 / R-6 form), or ask for a line naming
  them CONDITIONAL on that text. No string proposed.
- G-R125, REFEREE'S LANDING CONDITION (MET at 07139249). REFEREE §C l. 136-138 «Condition (for the CHECKER of P-N5-SPLIT): P-N5-SPLIT lands
  only after R125 is in trunk docs/RESULTS.md under that id, and the landed R125 still names each fact cited «as RESULTS R125» (re-run
  split_l1.py's R125 block on the landed text).». R125 is in trunk RESULTS under that id (l. 15595-15724) with L-5's text (its title = «###
  R125 [refereed-only] » + L-5 (dd83371b, sha1 473344b1) + «, CHECKER PASS (docs/checker/C139.md, checker 1622c7d9)», byte-equal, asserted
  by fill1.py), and each of the 17 names L-1 cites «as RESULTS R125» occurs in that title as a whole token (prem127a.py (1); negative
  control: made-up names F7 and LOC-GATE4 occur 0 times). So L-1 needs no regeneration; «CONDITIONAL on RESULTS R125 (P-N5-CHAIN)» now
  refers to a landed entry.
- G-7, L41 (note; CHECKER's call). L-1 names one referee-originated proof repair, in its premise parenthesis: «(LEX-Λ) is applied only to
  non-core vertices (pads), where P-N5-CHAIN's W-1 repair holds (pads of movers and gates; P-N5-CHAIN fixes entry 3, R-W;
  referee-originated: REFEREE-2 R2-P-N5-SPLIT W-1; also REFEREE R-P-N5-SPLIT SP-1)». It restricts a sentence of §1's proof text (false as
  written for plays from pA or K3) to the pads, where every use sits; both referees found it independently and each signed the proofs on the
  repaired reading (REFEREE «By the Lead's L41 standard (12:24Z ruling on P-N5-QUIET; 13:12Z on P-N5-CHAIN): a frozen sentence false as
  written whose needed restriction is not in the text.» (l. 40-41); REFEREE-2 «It closes as P-N5-CHAIN's W-1 closed: by restricting the
  sentence to non-core vertices.» (l. 57-58); Add. 1 «SP-1 (REFEREE) = my W-1, found independently.» (l. 359)). DECISIONS L41 (l. 355-360)
  «both signatures and the joint gap map are quoted in the RESULTS entry, whose scope tail says the proof is referee-originated». L-1
  carries the credit, but in the premise parenthesis, not in the scope tail (after « — »), which has no «referee-originated». Fixes entry 2
  «ACCEPTED (L41 standard, as P-N5-CHAIN's W-1 and P-N5-QUIET's R-G).» (l. 25). Precedent: landed R125 carries «referee-originated» twice,
  both AFTER its « — » (in its scope tail, RESULTS l. 15595 at 07139249, by script); L-1 carries it once, BEFORE its « — » (character 5,269
  of L-1; « — » at 5,470). CHECKER's call whether the premise-parenthesis placement meets L41's «scope tail» words; if not, PROPOSED: append
  to L-1's scope tail, before « (P-N5-SPLIT, docs/new», the clause "; the restriction of (LEX-Λ) to non-core vertices is referee-originated
  (REFEREE-2 R2-P-N5-SPLIT W-1; REFEREE R-P-N5-SPLIT SP-1)" (a line change both referees re-sign).
- G-9, DATA, CLAUSE BY CLAUSE (data127a.py on the archive of 8f4dab7e: 41 checks OK, «DATA EQUAL»): split199.out 28 rows, the 11
  PROVED-lemma counters 0 on every row; check199.out controls on CX4_n21 hwfail 444, dnfail 219, rhfail 219, rh2fail 313, spfail 161,
  rw1fail 127, gtfail 284, and playfail, kindfail, trfail, wlamfail fire in no control; max c_y 6 outside MW (C6G8_n54), MW4/8/16/32_2 9 /
  17 / 33 / 65; max split pairs 5 on FW6_4 and FW8_4 only; max T3 199; D1-D6 dn_nobelow_all 192, wcfail 18, wbfail 18, ytopB_ne 65,
  premono_no 18, rwfail 31 on their instances; D7 fan-in 3 / 4 (pair198.out maxRA); the 8 sha1 prefixes. COUNTERS NAMED: every DATA counter
  clause names counter, unit and set (the 28 frozen instances); D1-D6 each name counter and «unit:»; the three maxima («max c_y», «max split
  pairs», «T3 ≤ 199») name the quantity and the set but no counter field or «unit:» (split199.out fields maxc, maxSPL, T3; unit per (v, I,
  y) resp. per instance, packet §9.1 l. 241); D7 names NO counter and NO unit (its four items are «fan-in 3», «fan-in 4», «linear RA depth»,
  «multiplicity n»). REFEREE-2 N-3 («So the measured 0 is over (state, vertex) pairs, a superset. The line's sentence is true as written, a
  fortiori.», l. 459-461) is a unit note, not a defect. Fixes entry 1 (n1)'s L-RED climb (C 12, C 26) is not in L-1 (CHECKER may ask for it:
  it is a record of another lane, «(relayed by the Lead; not re-run by me; instances not frozen by me)»).
- G-U, STATUS WORDS AND THE UPDATE PROCEDURE (CLEAN). L-1's tail is the landed R123 / R124 form (the generator asserts it in RESULTS;
  REFEREE-2 Add. 2 l. 451-452): «… so this is not M4; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim (P-N5-SPLIT».
  R118's procedure with the landed drops («; G-N5-TIME stays OPEN», «; not M3, not a step-4 pass, not a TARGET.md claim») runs with NO
  reading: UPDATE sha1 b7601151eaa454196e90a91da340b7c16606df68 (upd127a.py (4)). START is the span from «for every genome G (Ξ-cycles and Ξ
  self-loops allowed), » through «σ̄_s(u) at a gate: » (the definitions before the first label, as R126's); fifteen labels, «(Lemma SPLIT,
  incl. TRANSFER)» … «(Lemmas ASC-WIT, ASC-ROOT, under HYPOTHESIS [E-LEV]: …)»; the premise parenthesis stays inside the last claim, as in
  R125 and R126. L-1 keeps «N5′-xi stays a CANDIDATE (D1)» (as R124, R125; packet §10 «G-N5-TIME stays OPEN; N5′-xi stays a CANDIDATE (D1).»
  (l. 265)); not a status word that goes stale.
- G-S, STALE STATUS WORDS (CLEAN by grep: in L-1 «unlanded» 0, «not landed» 0, «when landed» 0, «pending» 0, «to land» 0, «landing» 0,
  «landed» 0, «will » 0, «not yet» 0; «CANDIDATE» once, in «N5′-xi stays a CANDIDATE (D1)»; «stays» twice: «G-N5-TIME stays OPEN» and that
  CANDIDATE clause). The packet's own «landing as R125, pending» (l. 36-38) is not in L-1, which says «CONDITIONAL on RESULTS R125
  (P-N5-CHAIN)», true at landing (G-R125).
- G-1, SOURCE NOTE (CLEAN by C134 N-S). L-1: «(P-N5-SPLIT, docs/new/P-N5-SPLIT.md, frozen at l-new 399cda07, sha1 5bc1b1f3, with fixes
  entries 1-2, docs/new/P-N5-SPLIT-fixes.md; sources boxes 197-199; L-NEW successors 65-67 and 69)» = REFEREE LS-8 (§C «LS-8: «sha1
  5bc1b1f3, with fixes entries 1-2», «L-NEW successors 65-67 and 69», «L-RED 60-62». All CORRECT.» (l. 131-132)) = REFEREE-2 Add. 2 (MET).
- G-6, NAMES. In RESULTS (07139249): «SPLIT-COUNT» 0, «REWIN-HI» 0, «REWIN-COUNT» 0, «PAIR-SPLIT» 0, «RW-SHAPE» 0, «RW-1» 0, «PAIR-HIGH» 0,
  «RA-PATHS» 0, «RE-COUNT» 0, «RE-EQUIV» 0, «PAIR-COUNT» 0, «ALT-EQUIV» 0, «C-EQUIV» 0, «ASC-WIT» 0, «ASC-ROOT» 0, «TRANSFER» 17, «LEX-Λ» 0,
  «Dhi_y» 0, «Rtop» 0, «RA-LOG» 0, «HOW3(G)» 10, «P-N5-SPLIT» 0, «R127» 0, «C141» 0 (by script). «HOW3(G)» is R125's. NAME CLASHES (note):
  «Lemma SPLIT» and «TRANSFER» are already landed names of OTHER statements: R39's «(a) Lemma SPLIT: at an in-phase transition» (RESULTS l.
  1873; cited as «SPLIT (a)» by R42 l. 2074 and R46 l. 2282), R29's «(b) Lemma TRANSFER (every game)» (l. 1351; also R31 l. 1456) and R104's
  «(b) TRANSFER.» (l. 9968). L-1 names its §2 «(Lemma SPLIT, incl. TRANSFER)»; inside an entry the names are scoped by its setting, but a
  later «RESULTS R… Lemma SPLIT» needs the R-id. CHECKER's call whether to ask for qualified names (e.g. SPLIT3, TRANSFER3, the R125
  convention). The other names are new to RESULTS.
- G-2, SYMBOLS (note). L-1 uses «C» for C := max over v, I, y of c_y(v, I) and «C(M, 2)» for a binomial coefficient in ALT-EQUIV; in RESULTS
  «C» is also R118's count of steps labelled C (C140 N-C). Each is defined in place in L-1; no undefined symbol found (E_t, Π_t, Λ_t, Ω_t,
  σ̄, ⊴ / ▷, HOW3, T3, n3, L3, wt(y), pe_g, pβ_g, lev, seq_t are R125's or R104's, or defined in L-1).
- G-DE, DEAD ENDS (note). D1-D7 are stated inside the line with instance, sha1 prefix and counter, as R125's DEAD RUN-TRANSFER was, with no
  Dead-ends row; none proposed (and G-L43 for D7).
- G-P, PLACEMENT (Lead). R127 goes after R126 (07139249 l. 15726-15901, blank l. 15902), directly before the line-start «**Erratum E-1**
  (not a result» (l. 15903), its UPDATE after R126's on GAPS l. 11 (the last there). Simulated (sim127a.py): Addendum.
- G-0, THE CHECKER NUMBER. docs/checker/ ends at C140.md (at 07139249 and on claude/checker 7b2fa753, which trunk contains); «C141» 0 times
  in trunk docs/ and notes/ except the Lead state log's plan (docs/agents/LEAD-STATE.md l. 3156 «R127 first fill … for C141»), 0 on
  claude/checker (git grep). This draft uses C141 (title, UPDATE head), as the brief says.
- G-T, TARGET (CLEAN). L-1's scope words equal packet §10 in meaning («this proves no running-time bound … neither side is proved
  polynomial; the open core is max over y, b, J of Dhi_y(b, J)»), and its TARGET clause is R123 / R124's (REFEREE §6 «## 6. TARGET.md diff:
  CLEAN»; REFEREE-2 box 5 «SPLIT proves no running-time bound, and it claims none.»).
- (L-1 SHAPE, by script) one line: 9,249 bytes, 260 «(» / 260 «)», 0 «|», one « — », «(2026-11-11)» once, «DATA, clause by clause» 1,
  «HYPOTHESIS» 1, «CONDITIONAL» 1, «referee-originated» 1, «R126» 0, «PROVED» 3, «DEAD» 1.

### R127 [refereed-only] On HOW3(G), i.e. N5′-xi from S3 on Γ3(G) until its first fallback (the Howard run on Γ3(G) of RESULTS R125 (P-N5-CHAIN), states 0, …, T3, n3 = N + 7M + 10; by R125's REACH3-ALL the mover part of N5′-xi from S3 until its first fallback), for every genome G (Ξ-cycles and Ξ self-loops allowed), each statement PROVED and CONDITIONAL on RESULTS R125 (P-N5-CHAIN), with E_t(v) the e-vertices of Π_t(v), sets of e-vertices ordered lexicographically by the most relevant differing element, a Λ-interval I of v a maximal interval of states with Λ_t(v) constant, a change a step t − 1 → t in I with E_(t−1)(v) ≠ E_t(v), its top the most relevant element of E_(t−1)(v) Δ E_t(v), U_y the e-vertices more relevant than y, c_y(v, I) the number of changes in I with top y, Dhi_y(v, I) the number of distinct values of E_t(v) ∩ U_y on I, C := max over v, I, y of c_y(v, I), and nx_s(u) := σ_s(u) at a mover, σ̄_s(u) at a gate: (Lemma SPLIT, incl. TRANSFER) at every change of (v, I), the first vertex u at which the plays P_(t−1)(v), P_t(v) leave by different edges is a mover with σ_(t−1)(u) ≠ σ_t(u) and Ω_(t−1)(new) ▷ Ω_(t−1)(old), or a gate with σ̄_(t−1)(u) ≠ σ̄_t(u) whose abandoned face rose strictly, Ω_t(old) ▷ Ω_t(new) ⊵ Ω_(t−1)(new) ▷ Ω_(t−1)(old); and Λ_(t−1)(u) = Λ_t(u) and E_(t−1)(v) Δ E_t(v) = E_(t−1)(u) Δ E_t(u); (Lemma REWIN, Lemma REWIN-HI) for two consecutive y-tops t1 < t2 of (v, I) with the same split u and the same new successor b := nx_t1(u) = nx_t2(u), and a := nx_(t2−1)(u): (a) Ω_(t2−1)(a) ▷ Ω_t1(b), (b) Ω_(t2−1)(b) ▷ Ω_(t2−1)(a) ▷ Ω_t1(b), (c) E_t2(b) ∩ U_y >lex E_t1(b) ∩ U_y; (Corollary REWIN-COUNT, superseded by SPLIT-COUNT) c_y(v, I) ≤ 1 + W_y(v, I) + Σ_(u,b) (Dhi_y(b, J_b) − 1), W_y the number of consecutive y-top couples with different split pairs; (Lemma PAIR-SPLIT) (a′), (b′), (c′) hold for ANY two y-tops t < t′ of (v, I) through the same split pair (u, b), with a := nx_(t′−1)(u): Ω_(t′−1)(a) ▷ Ω_t(b), Ω_(t′−1)(b) ▷ Ω_t(b), E_t′(b) ∩ U_y >lex E_t(b) ∩ U_y; (Corollary SPLIT-COUNT) c_y(v, I) ≤ Σ_((u,b) ∈ SPL_y(v,I)) Dhi_y(b, J_b) ≤ 3M · max_((u,b)) Dhi_y(b, J_b), SPL_y(v, I) the split pairs of the y-tops of (v, I) and J_b the Λ-interval of b containing the y-tops through (u, b), so C polynomial ⇐ max over y, b, J of Dhi_y(b, J) polynomial (a reduction, not an equivalence); (Lemma RW-SHAPE, RW-SHAPE*) for same-pair y-tops t < t′ through (u, b) (consecutive, resp. any), m := wt(y), E_s(b) ∩ U_y = B_s ⊔ S_s with B_s the U_y-letters of b's play at s before y and S_s := E_s(m) ∩ U_y: if S_t = S_t′, then B_t′ ≠ ∅ and for every f ∈ B_t′ some vertex of P_t′(b) strictly between f and y has nx_(t′−1) ≠ nx_t′; (Corollary RW-1) at every such couple whose t′-step is single-split, S_t ≠ S_t′; (Lemma PAIR-HIGH, abstract: any lex-increasing set sequence, E-MON3 only) on (v, I), c_y ≤ Dhi_y, A_xy ≤ 2·Dhi_y + 1 (A_xy the longest x/y-alternating subsequence of the tops, y more relevant than x) and Dhi_y = 1 + Σ_(z ∈ U_y) c_z; (Lemma RA-PATHS) c_y ≤ P(y), the number of directed paths from y in the graph RA of most relevant tops strictly between consecutive y-tops; (Lemma RE-COUNT) D_I(v) ≤ 1 + Mact_I(v) + Rtop_I(v) (D_I(v) the number of distinct sets E_t(v), t ∈ I; Mact_I(v) the number of e-vertices in ⋃_(t∈I) E_t(v); Rtop_I(v) the number of changes in I whose top lies in E_s(v) for some s ∈ I, s < t − 1); (Theorem RE-EQUIV) T3 ≤ (1 + n3·((2M + 3)(M + 1) − 1) + Rtop)·(L3 + 1) and Rtop ≤ n3·T3, so T3 is polynomial in N + M iff Rtop is; (Lemma PAIR-COUNT, corrected form) a sequence over m letters with no two equal consecutive letters has length ≤ 1 + Σ_(x<y) max(0, A_xy − 1); (Theorem ALT-EQUIV, corrected form) with A := max(1, the longest two-letter alternation in tops(v, I) over v, I), T3 ≤ (1 + n3·((2M + 3)·(2 + C(M, 2)·(A − 1)) − 1))·(L3 + 1) and A ≤ max(1, T3), so T3 is polynomial iff A is; (Corollary C-EQUIV) T3 ≤ (1 + n3·((2M + 3)(1 + M·C) − 1))·(L3 + 1) and C ≤ max(1, T3), so T3 is polynomial iff C is; (Lemmas ASC-WIT, ASC-ROOT, under HYPOTHESIS [E-LEV]: lev(x) < lev(x′) implies pr(e_(x,k)) < pr(e_(x′,k′))) at an ascent (c_i, c_(i+1)) of seq_t(v), y the successor of c_i and g1 the gate of σ_t(y): σ̄_t(g1) = pβ_(g1), Ω_t(pe_(g1)) ▷ Ω_t(pβ_(g1)), and either Λ_t(pe_(g1)) = Λ_t(v) and E_t(pe_(g1)) contains an e-vertex at least as relevant as c_(i+1), or Λ_t(pe_(g1)) has strictly larger reward than Λ_t(v); and at the first ascent there is a gate g* with lev(g*) < lev(c_i), σ̄_t(g*) = pβ_(g*) and Ω_t(pe_(g*)) ▷ Ω_t(pβ_(g*)), whose W-face's cycle node has strictly larger reward than Λ_t(v) (premises: RESULTS R125 (P-N5-CHAIN): HOW3, REACH3-ALL, F1, F3, F4′, F5, F6, DOM, STRICT, CN2-3, LOC-GATE3, LOC-K2-3, B-ONLY3, NO-TIE3, T-QUIET3 with L3, E-MON3, CHAIN-DECOMP3; [DEF] = RESULTS R104's definitions of the genome and of Γ(G); [G3] = RESULTS R117's definition of Γ3(G); [OPT] = RESULTS R118 (b) and RESULTS R21 (a) (σ̄_t optimal at every vertex at once); (R), (P), (E-DOM), (Core) in its W-1-repaired reading (the only edge into the eight-vertex core from outside is pb_g → K0), F2 and CYC: P-N5-CHAIN's frozen text (l-new 93531b03, sha1 6e613ba7, §2 and §4); (LEX-Λ) is applied only to non-core vertices (pads), where P-N5-CHAIN's W-1 repair holds (pads of movers and gates; P-N5-CHAIN fixes entry 3, R-W; referee-originated: REFEREE-2 R2-P-N5-SPLIT W-1; also REFEREE R-P-N5-SPLIT SP-1); [E-LEV] only in ASC-WIT and ASC-ROOT; not used: any other packet, any other R-id, any L-RED or L-SI lemma) (2026-11-11) — this proves no running-time bound: RE-EQUIV, ALT-EQUIV and C-EQUIV are equivalences and SPLIT-COUNT is a reduction, and neither side is proved polynomial; the open core is max over y, b, J of Dhi_y(b, J); nothing is claimed for N5 (SPEC S4a), outside Γ3(G), or on iteration counts beyond T3; DEAD (each with the instance that kills it, experiments/new/box199/inst, sha1 prefix; none is a premise): D1 «each re-win of y at u is paid by a class change of a vertex on the y-route below y» (CX4_n21, ef29debb; dn_nobelow_all 192, unit: re-wins); D2 «E(wt(y)) ∩ U_y changes between any two consecutive y-tops» (GROW7_n34, 42bbd562; wcfail 18, unit: re-entries); D3 «c_y(v) ≤ the number of values of E(wt(y)) ∩ U_y on the span» (HOLD2K_n84, 423a4a88; wbfail 18, unit: (v, I, y)); D4 ROUTE-LOW «no U_y-letter on v's new play between u and y at a y-top» (ROUTELOW_n21, 80f9b977; ytopB_ne 65, unit: y-tops); D5 the product-chain idea «the U_y-letters before y on v's play are lex-monotone at y-tops» (GROW7_n34; premono_no 18, unit: (v, I, y)); D6 CONJECTURES RW-WT, RW-WT*, RW-B0, RW-B0* (RWX_n95, da8b3a30, L-RED 62; rwfail 31, unit: re-wins); D7 fan-in 1 of RA as a game property (NK6_cl21, 408b9988, fan-in 3; DSALT9_n416, da3308b5, fan-in 4; unit: max over (v, I, y) of the number of letters of RA(y), box198/pair198.out maxRA); DATA, clause by clause (tool experiments/new/box199/split199.py on R125's engine: box 189 gamma3.build, box 190 n5v.step mode xi from S3 to the first fallback; set: the 28 frozen instances of experiments/new/box199/inst; record box199/split199.out; check199.sh re-run by check.sh): every PROVED-lemma counter 0 on all 28: playfail, kindfail, hwfail, gtfail, trfail (unit: changes at (v, I); SPLIT), dnfail (REWIN), rhfail (REWIN-HI), rw1fail (RW-1) (unit: re-wins), rh2fail (unit: same-pair couples, all pairs t < t′; PAIR-SPLIT), spfail (unit: (v, I, y); SPLIT-COUNT's first inequality with Dhi_y(b, J_b) replaced by the number of distinct values of E(b) ∩ U_y at the pair's own y-tops, a lower bound for Dhi_y(b, J_b), so spfail 0 is the stronger statement), wlamfail (unit: re-entries; Λ(wt(y)) = w at both y-tops); playfail, kindfail, trfail and wlamfail are definition checks without a firing control; every other counter has one (check199.out on CX4_n21: hwfail 444, dnfail 219, rhfail 219, rh2fail 313, spfail 161, rw1fail 127, gtfail 284); on the 28 frozen instances max c_y (unit: y-tops of one (v, I, y), max over (v, I, y); split199.out maxc) ≤ 6 outside the MW family (C6G8_n54: 6) and MW(n) has max c_y = 2n + 1 (65 on MW32_2); max split pairs (unit: distinct split pairs (u, b) of the y-tops of one (v, I, y), max over (v, I, y); split199.out maxSPL) 5 (FW6_4, FW8_4); RA depth (longest RA chain) 4 / 8 / 12 / 16 on FW4/8/12/16_2 (REFEREE-2 36 R2-P-N5-SPLIT, claude/referee-2 4948ce5d, own engine; L-SI 47 box 90, claude/l-si 4ded1e8d) and the per-pair multiplicity n on MW(n) (L-SI 47 box 90, claude/l-si 2d0344d3, not re-run by the lane or a referee), DATA only; every run is short (T3 ≤ 199; unit: states of the HOW3 run, max over the 28 frozen instances, split199.out T3; 199 on MW32_2) and nothing here tests a polynomial bound; large zero counts are DATA, not evidence of a lemma; independent replays, every fail counter 0, cited, not re-run: REFEREE 30 R-P-N5-SPLIT §4 (claude/referee ca091557; 28 pinned instances and 800 random genomes), REFEREE-2 36 R2-P-N5-SPLIT (claude/referee-2 991296c9; 28 pinned, 7,000 random and 2,200 mutants, D1-D7 re-run); attack record L-RED 60-62 (R226, R227, R228; all PROVED statements SURVIVE); N5′-xi stays a CANDIDATE (D1); TARGET.md §2 (M4) asks for an algorithm polynomial on every parity game and §4 says a bound on a restricted class is not M4, so this is not M4; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim (P-N5-SPLIT, docs/new/P-N5-SPLIT.md, frozen at l-new 399cda07, sha1 5bc1b1f3, with fixes entries 1-4, docs/new/P-N5-SPLIT-fixes.md; sources boxes 197-199; L-NEW successors 65-67 and 69), CHECKER PASS (docs/checker/C141.md, checker PENDING)
- Object (L-NEW successors 65-67, 69 and 71, D1 / D14 / D18, boxes 197-199; frozen, unchanged during review): packet P-N5-SPLIT,
  docs/new/P-N5-SPLIT.md, sha1 5bc1b1f390ed81683fe5c93008c7ea0b338fe735, 275 lines, 30,949 bytes (l-new 399cda07, 2026-11-08T23:38:56Z, the
  file's only commit; identical at 63515442, 8f4dab7e, d0a7d351, 621e6b77, at the l-new head 0ea262a0 and at trunk 07139249; pinned in
  experiments/new/box199/split.pins). Both referees measured it (REFEREE l. 3-4 «docs/new/P-N5-SPLIT.md sha1
  5bc1b1f390ed81683fe5c93008c7ea0b338fe735, 30,949 B, 275 lines»; REFEREE-2 l. 11 «docs/new/P-N5-SPLIT.md at 399cda07: sha1
  5bc1b1f390ed81683fe5c93008c7ea0b338fe735, 30,949 B (= the brief)»). Labels (l. 8): «Labels: PROVED (L-NEW 65 / 66, unrefereed; each
  survived the L-RED attacks listed in §9) / DEAD / DATA / READING (not to sign).». Scope (l. 9): «This packet is NOT a TARGET.md claim, NOT
  M3 and NOT M4. It does not decide G-N5-TIME. It is a REDUCTION / EQUIVALENCE (§10).». To sign (l. 24-35): §2 Lemma SPLIT (i)-(iv) incl.
  TRANSFER; §3 Lemma REWIN, Lemma REWIN-HI, Corollary REWIN-COUNT; §4 Lemma PAIR-SPLIT, Corollary SPLIT-COUNT, Lemma RW-SHAPE(*), Corollary
  RW-1; §5 Lemma PAIR-HIGH, Lemma RA-PATHS; §6 Lemma RE-COUNT, Theorem RE-EQUIV, Lemma PAIR-COUNT, Theorem ALT-EQUIV, Corollary C-EQUIV; §7
  Lemmas ASC-WIT, ASC-ROOT; §8 DEAD D1-D7; §9-§11 DATA / READING. Premises (l. 36-38): «Every row is conditional on P-N5-CHAIN (lane packet,
  frozen at l-new 93531b03, sha1 6e613ba762b6ecf67247ef6d8674b4c960013039»; «Nothing else is a premise: no other packet, no landed R-id, no
  L-RED or L-SI lemma.». Dropped (l. 39-40): «DROPPED from the sources (no standing here): Corollary C-WT and Corollary REWIN-ASC (both
  implications from the DEAD CONJECTURES of §8),». Source (l. 5-7): «Every proof is carried here in full; nothing is cited from those
  files.». The packet's own scope (l. 20): «What it does NOT imply: any polynomial bound. The open core after this packet is max over y, b,
  J of Dhi_y(b, J) (§10).».
- Fixes: docs/new/P-N5-SPLIT-fixes.md, append-only, four entries (621e6b77, 2026-11-12T08:37:02Z: 134 lines, 13,865 bytes, sha1
  242ade7b046515a8895c3f787eaefba1cf64c542, byte-equal at the l-new head 0ea262a0; its first 12,071 bytes are the file at d0a7d351 (117
  lines, sha1 c51caa12…), whose first 7,523 bytes are the file at 8f4dab7e (75 lines, sha1 f7940ddf3361d45407855ce51baddc9e59515426,
  byte-equal at 07139249); by prefix test, entries 3-4 appended). Entry 1 (L-NEW successor 67, 63515442, 2026-11-09T00:44:26Z; l. 3-14;
  answering L-RED 62's packet-level read): «Scope: DATA only (§9.1). No statement, proof, premise or DEAD row of the packet changes.» (l.
  4); (n1) restates §9.1's max c_y clause with its set, «On the 28 frozen instances of experiments/new/box199/inst (split199.out)» (l. 6),
  and relays L-RED 62's MW-mutant climb (C 12 at N + M ≤ 200, C 26 at N + M ≤ 400, «relayed by the Lead; not re-run by me», l. 9); (n2) no
  change. Entry 2 (L-NEW successor 69, 8f4dab7e, 2026-11-11T22:57:03Z; l. 16-70; answering REFEREE 30 and REFEREE-2 36): «No statement,
  proof, label, premise of a signed row, or DATA number changes. Where this entry and the packet differ, this entry governs. Every item is
  ACCEPTED.» (l. 22-23). SP-1 = W-1 (l. 25-34): §1 (LEX-Λ)'s reason is false over all vertices; every use is at pads; governing reading
  «(LEX-Λ) is applied only to non-core vertices (pads), where P-N5-CHAIN's W-1 repair holds.» (l. 31), «Credit: referee-originated:
  REFEREE-2 R2-P-N5-SPLIT W-1; also REFEREE R-P-N5-SPLIT SP-1 (found independently).» (l. 33). SP-2 = R-6 (l. 36-44): the citation form of
  L-1's premise list. SP-3 = N-1 (l. 46-48): (PL)'s wording. N-2 (l. 50-51): «These were used in the proofs as written; no new premise.».
  split.pins 61 rows (l. 53-55). LS-1..LS-8 (l. 57-70). «Line L-1» (l. 72-75): generator experiments/new/box199/mkl1_199.py, pinned in
  split.pins. No item changes a statement, a label, a proof's content or a DATA number: SP-1 restricts one sentence of §1's proof text to
  where it is used. Entry 3 (L-NEW successor 71, d0a7d351, 2026-11-12T07:14:44Z; l. 77-117): «Fixes entry 3 (L-NEW successor 71; Lead ruling
  R-D7a 07:12Z 2026-11-12, L43; written 2026-11-12T07:14Z by date -u)» (l. 77); «Ruling R-D7a (Lead, line-only), applied verbatim» (l. 83);
  D7 reduced to «fan-in 1 of RA» with its unit, and the RA depth on FW and the MW(n) multiplicity carried into DATA with their numbers and
  source commits; «Ids and numbers verified by git before the build (Lead: «If any id or number is wrong, STOP»; none was)» (l. 93); Line
  L-2 = L-1 + R-D7a (l. 104-106); the units the Lead asked for next, «Lead's second ask (the three maxima clauses and the DATA rule),
  PROPOSED, NOT APPLIED (L-2 carries R-D7a only)» (l. 108). Entry 4 (L-NEW successor 71, 621e6b77, 2026-11-12T08:37:02Z; l. 119-134): «Fixes
  entry 4 (L-NEW successor 71; Lead ruling R-U127 07:58Z 2026-11-12, DATA rule; written 2026-11-12T08:36Z by date -u)» (l. 119); «ACCEPTED;
  applied verbatim, line only:» (l. 121): units (a)-(c) on the three maxima clauses and (d) the source note; «Counters checked against the
  tool: split199.py header l. 31 «maxc, maxW (non-rewin re-entries), maxSPL (distinct (u, b)): per (v, I, y), maxima over the genome»» (l.
  128-129); Line L-3 = L-2 + R-U127, «L-1 → L-3 = R-D7a + R-U127.» (l. 132-133). Both entries are line-only; REFEREE-2 37 on L-3:
  «P-N5-SPLIT's signed statements are unchanged.» (l. 510).
- The RESULTS line is L-3, a8661c4b7998aafc02299c43dfe4e2c6320f73ee (docs/new/P-N5-SPLIT-line-L3.txt, l-new 621e6b77, 2026-11-12T08:37:02Z,
  the file's only commit, on origin through its child 0ea262a0; 9,796 bytes, 9,481 characters with its newline, one line, blob
  c8a9d17777a5545ffa34db110f9975d544ab1b11). The title is L-3 verbatim, with nothing inserted and nothing stripped (its date parenthesis
  «(2026-11-11)», its scope tail and its source note are the line's own). L-3's parentheses balance (273 «(» / 273 «)»); it has no pipe
  character. It is written by experiments/new/box199/mkl3_199.py (L-2 + R-U127; it asserts the frozen packet's sha1, L-2's sha1, each old
  string once, one line, no pipe character, balanced parentheses, each new unit string once and «with fixes entries 1-2» absent) from L-2
  (d8888d0b090339b80b4ce9b636a23461b476bf3f, docs/new/P-N5-SPLIT-line-L2.txt, l-new d0a7d351, 2026-11-12T07:14:44Z, the file's only commit,
  9,521 bytes; written by mkl2_199.py, L-1 + R-D7a, which asserts L-1's sha1, each old string once, «RA-LOG» and «MW32_2, 445031d1» absent
  and each new source id once) from L-1 (634b2fdfda31eda9e82e9f558ffebf3c89f5701c, docs/new/P-N5-SPLIT-line-L1.txt, l-new 8f4dab7e,
  2026-11-11T22:57:03Z, the file's only commit, 9,249 bytes, blob 726d0c5d9bb740b2f3f146f425cc3f2fc18c7e5b), written by
  experiments/new/box199/mkl1_199.py, which asserts the frozen packet's sha1, fixes entry 2's governing (LEX-Λ) sentence verbatim in the
  fixes file, the absence of the withdrawn sentence, R124's landed TARGET tail in RESULTS, one line, no pipe character, balanced
  parentheses. L-1 → L-3 is the six replacements of rulings R-D7a and R-U127 and nothing else (L-1 with the six strings of mkl2_199.py and
  mkl3_199.py applied = L-3, byte for byte: tools/upd127b.py (4c)). L-1 rebuilt byte-equal by REFEREE-2 (Add. 2, l. 394-395: «The output is
  byte-equal to the committed L-1 (cmp).») and by the drafter with RESULTS at 07139249 (rc 0); REFEREE tested it against its own strings
  (§C, l. 113-115: «strings typed from this report (scratch/split_l1.py; log split_logs/l1test.out), not from the lane's generator»). L-3
  rebuilt by REFEREE-2 37 with its own code (Add. 3, «R2-P-N5-SPLIT/bt_l3.py (my code; mkl2_199.py and mkl3_199.py not imported)» (l. 478);
  «Result: sha1 a8661c4b…, 9,796 B, BYTE-EQUAL to the lane's L-3 (cmp equal).» (l. 483)) and by the drafter with the lane's chain
  mkl1_199.py (RESULTS at 07139249), mkl2_199.py and mkl3_199.py from a git archive of 621e6b77 (rc 0 each; L-1, L-2 and L-3 cmp-equal to
  the committed files). REFEREE: L-1 MATCHES (§C, 8c395bff, l. 140-141, quoted below); its §E on L-3 (REFEREE successor 31, 33cd0fca, l.
  143-169) tested L-3 with strings of its own («strings typed from fixes entries 3-4;» (l. 148)), «`cmp` with the lane's L-3: **EQUAL**» (l.
  149), and found «Verdict: fixes entries 3-4 CORRECT. **Line L-3 MATCHES** (= L-1 + R-D7a + R-U127 exactly). Statements and labels
  unchanged (§0; §C).» (l. 169). REFEREE-2: L-1 MATCHES (Add. 2, c5bc1365, l. 465, quoted below); L-3 MATCHES (Add. 3, REFEREE-2 successor
  37, 98a64b91, l. 509-510, quoted below).
- Claims signed (REFEREE successor 30: report ca091557; successor 31: §C 8c395bff, §E 33cd0fca; REFEREE-2 successor 36: report 15a05bf0 …
  4948ce5d, final sweep 991296c9, Add. 1 c708c968; successor 37: Add. 2 c5bc1365, Add. 3 98a64b91); every row CONDITIONAL on R125, as the
  packet states. REFEREE's table («## 0. Verdicts», «every row CONDITIONAL on R125 = P-N5-CHAIN landing, as the packet states», l. 8-19 of
  R-P-N5-SPLIT.md) reads: SPLIT «**SIGN**» (l. 11); REWIN / REWIN-HI / REWIN-COUNT «**SIGN WITH SP-1** ((LEX-Λ) read for non-core vertices;
  every use is on pads)» (l. 12); PAIR-SPLIT / SPLIT-COUNT «**SIGN WITH SP-1**» (l. 13); RW-SHAPE(*) / RW-1 «**SIGN WITH SP-1**» (l. 14);
  PAIR-HIGH / RA-PATHS «**SIGN** (abstract; E-MON3 only)» (l. 15); RE-COUNT, RE-EQUIV, PAIR-COUNT, ALT-EQUIV, C-EQUIV «**SIGN**» (l. 16);
  ASC-WIT, ASC-ROOT «**SIGN** under HYPOTHESIS [E-LEV] (ASC-WIT (c) WITH SP-1)» (l. 17); DEAD D1-D7 «D1, D2, D4, D5, D6 reproduced by the
  lane's check199.sh (lane code, re-run, byte-equal); D3, D7 cited, not re-run» (l. 18); then «No GAP; nothing refused.» (l. 19).
  REFEREE-2's table («## Verdicts (Opus 5.5, D1)», l. 329-344 of R2-P-N5-SPLIT.md, 4948ce5d) reads «SIGN» on each of its eleven statement
  rows (l. 332-342; ASC-WIT, ASC-ROOT «under HYPOTHESIS [E-LEV]», l. 342), «SIGN (dead)» on DEAD D1-D7 (l. 343), and W-1 «a proof-text
  defect: false over all pairs, true for non-core pairs, and every use is at pads; the conclusion holds for all pairs» (l. 344); then «No
  statement is REFUSED, and no gap is left open in any signed proof. W-1 is a sentence of §1's proof text, closed above.» (l. 346). Addendum
  1 (c708c968): «Verdicts: equal on every row.» (l. 354); «These are the same finding and the same repair, under different labels.» (l.
  357-358). Both re-signed on L-1: REFEREE §C (quoted above, l. 140-141); REFEREE-2 Add. 2 «With REFEREE's signatures, P-N5-SPLIT's
  statements stand as two-referee signed, CONDITIONAL on R125. ASC-WIT and ASC-ROOT stand under HYPOTHESIS [E-LEV].» (l. 466-467). On L-3:
  REFEREE-2 Add. 3 «P-N5-SPLIT's signed statements are unchanged.» (l. 510), with D7's scope «D7 now claims only «fan-in 1 of RA as a game
  property». That is an explicit bound, so finite instances kill it (NK6_cl21 3, DSALT9_n416 4).» (l. 487-488); REFEREE §E «Statements and
  labels unchanged (§0; §C).» (l. 169). The HYPOTHESIS statements, with their condition as the line states it: ASC-WIT and ASC-ROOT «under
  HYPOTHESIS [E-LEV]: lev(x) < lev(x′) implies pr(e_(x,k)) < pr(e_(x′,k′))», and no other row (REFEREE-2 R-3 MET, Add. 2 l. 412-414). The
  joint gap map: EMPTY (REFEREE l. 19; REFEREE-2 l. 346). The one defect found in review, §1 (LEX-Λ)'s reason (SP-1 = W-1), is a sentence of
  the proof text, not a statement; it is closed by restricting it to the pads, where every use sits (fixes entry 2, governing; REFEREE §C
  «The withdrawn sentence is ABSENT» (l. 118); REFEREE-2 Add. 2 R-1 MET). Nothing is REFUSED.
- Setting: HOW3(G) of RESULTS R125, the Howard run on Γ3(G) (RESULTS R117) from SPEC's default start S3, states 0, …, T3, for every genome G
  of R104 (Ξ-cycles and Ξ self-loops allowed); by R125's REACH3-ALL it is the mover part of N5′-xi from S3 until its first fallback. Every
  statement is PROVED and CONDITIONAL on RESULTS R125 (P-N5-CHAIN), which is landed (G-R125). Statements as signed (packet with fixes
  entries 1-4; entry 2's (LEX-Λ) reading and (PL) wording govern; entries 3-4 are line-only; PAIR-COUNT and ALT-EQUIV in the packet's
  corrected forms):
  (a) Lemma SPLIT (i)-(iv), incl. TRANSFER (§2 l. 67-84): at every change of (v, I) the first departure u of the two plays is a mover making
    a strict Howard switch or a gate whose abandoned face rose strictly, and «The change at v is a change of u's e-set inside a Λ-interval
    of u, with the same symmetric difference and the same top.» Both SIGN (REFEREE l. 11; REFEREE-2 l. 332).
  (b) Lemma REWIN (a)(b), Lemma REWIN-HI (c), Corollary REWIN-COUNT (§3 l. 86-113): «(c) REWIN-HI: E_t2(b) ∩ U_y >lex E_t1(b) ∩ U_y.»
    REWIN-COUNT «(Superseded by SPLIT-COUNT, §4, which has no W term.)» Both SIGN (REFEREE l. 12 WITH SP-1; REFEREE-2 l. 333-334).
  (c) Lemma PAIR-SPLIT, Corollary SPLIT-COUNT (§4 l. 116-130): (a′)(b′)(c′) for ANY two y-tops t < t′ through one split pair (u, b); «c_y(v,
    I) ≤ Σ_((u,b) ∈ SPL_y(v,I)) Dhi_y(b, J_b) ≤ 3M · max_((u,b)) Dhi_y(b, J_b),», «J_b the Λ-interval of b containing the y-tops through (u,
    b).» Both SIGN (REFEREE l. 13 WITH SP-1; REFEREE-2 l. 335-336).
  (d) Lemma RW-SHAPE, RW-SHAPE*, Corollary RW-1 (§4 l. 131-148): if S_t = S_t′ then B_t′ ≠ ∅ and every f ∈ B_t′ has a second split after it;
    «At every y-top couple through (u, b) whose t′-step is single-split (u is the only vertex of v's play before y at t′ whose successor
    changes at t′), S_t ≠ S_t′» Both SIGN (REFEREE l. 14 WITH SP-1; REFEREE-2 l. 337).
  (e) Lemma PAIR-HIGH (a)(b)(c), Lemma RA-PATHS (§5 l. 150-166; abstract, E-MON3 only): «Both lemmas hold for any lex-increasing set
    sequence; the abstract counter (every subset in binary order) makes them tight with c_y and P(y) exponential.» Both SIGN (REFEREE l. 15;
    REFEREE-2 l. 338).
  (f) Lemma RE-COUNT, Theorem RE-EQUIV, Lemma PAIR-COUNT (corrected), Theorem ALT-EQUIV (corrected), Corollary C-EQUIV (§6 l. 168-189): «So
    T3 is polynomial in N + M iff Rtop is.» «T3 is polynomial iff A is.» «C ≤ max(1, T3). T3 is polynomial iff C is.» Both SIGN (REFEREE l.
    16; REFEREE-2 l. 339-341).
  (g) Lemmas ASC-WIT, ASC-ROOT (§7 l. 191-211) [under HYPOTHESIS [E-LEV]]: static witnesses at an ascent of seq_t(v); «Static (any σ against
    an optimal σ̄); not a bound.» REFEREE SIGN under HYPOTHESIS [E-LEV] (l. 17), REFEREE-2 SIGN (l. 342).
  (h) DEAD D1-D7 (§8 l. 213-224, instances frozen in experiments/new/box199/inst): D1 downward charge, D2 W-target charge for all
    re-entries, D3 W-target bound, D4 ROUTE-LOW, D5 product chain, D6 CONJECTURES RW-WT, RW-WT*, RW-B0, RW-B0*, D7 as L-3 states it, «D7
    fan-in 1 of RA as a game property» (the packet's D7 also names RA-LOG and bounded multiplicity; by ruling R-D7a their numbers are DATA
    in L-3, not DEAD: L43 below). REFEREE: D1, D2, D4, D5, D6 reproduced by the lane's check199.sh, D3, D7 cited (l. 18); REFEREE-2 SIGN
    (dead) (l. 343), D1-D6 and D7's fan-in and FW depth re-run on its own engine, «I did not compute it; it is cited DATA of another lane
    and not a premise.» (l. 283-284). On L-3: REFEREE-2 Add. 3 «D7 now claims only «fan-in 1 of RA as a game property». That is an explicit
    bound, so finite instances kill it (NK6_cl21 3, DSALT9_n416 4).» (l. 487-488); «DSALT9_n416 now carries its sha1 da3308b5, which closes
    my optional N-4.» (l. 488-489).
- Premise (named, not quoted; L-1 and L-3 have no premise quote, and L-3's premise parenthesis is byte-equal to L-1's; checked by script at
  trunk 07139249, prem127a.py on L-1, prem127b.py on L-3): the 17 facts L-3 cites «as RESULTS R125 (P-N5-CHAIN)», HOW3, REACH3-ALL, F1, F3,
  F4′, F5, F6, DOM, STRICT, CN2-3, LOC-GATE3, LOC-K2-3, B-ONLY3, NO-TIE3, T-QUIET3 with L3, E-MON3, CHAIN-DECOMP3, each named in landed
  R125's title (RESULTS l. 15595); [DEF] = RESULTS R104 (l. 9864), definitions of the genome and of Γ(G); [G3] = RESULTS R117 (l. 13362),
  the definition of Γ3(G); [OPT] = RESULTS R118 (b) (l. 13682) and RESULTS R21 (a) (l. 933), σ̄_t optimal at every vertex at once; (R), (P),
  (E-DOM), (Core) in its W-1-repaired reading, F2 and CYC: P-N5-CHAIN's frozen text (l-new 93531b03, sha1
  6e613ba762b6ecf67247ef6d8674b4c960013039; P-N5-CHAIN.md l. 91, 93, 96, 97 (§2), l. 165, 166 (§4)), the frozen packet of landed R125, not a
  RESULTS text (G-4). HYPOTHESIS [E-LEV] only in ASC-WIT and ASC-ROOT. Not used (L-3): any other packet, any other R-id, any L-RED or L-SI
  lemma. Both referees checked the premises against P-N5-CHAIN's frozen text and R125's line (REFEREE §1 l. 21-32 and §C «are EACH named in
  R125's line L-5 (counted by script). CORRECT.» (l. 124); REFEREE-2 box 1 l. 24-38 and Add. 2 «The list after «RESULTS R125 (P-N5-CHAIN):»
  has 17 names. Every one occurs in CHAIN's L-5» (l. 435)).
- L41 and L43. The packet's proofs are L-NEW successors 65-66's (packet l. 8; «Every proof is carried here in full»). One proof repair is
  referee-originated: (LEX-Λ) used only at pads (REFEREE-2 W-1, REFEREE SP-1, found independently; REFEREE-2 Add. 1 l. 359-360), named in
  L-1's and L-3's premise parenthesis with the words «referee-originated: REFEREE-2 R2-P-N5-SPLIT W-1; also REFEREE R-P-N5-SPLIT SP-1»; each
  referee signed the proofs on it. L43: D1-D6 are structural claims, each killed by a named instance and counter; D7's «fan-in 1» is an
  explicit bound (RA(y) has at most one letter) exceeded on NK6_cl21 (3) and DSALT9_n416 (4); D7's «RA-LOG» (an O(log(N + M)) bound) and
  «bounded multiplicity» (L-SI's RA-MULT(K), K a constant) are asymptotic and rest on finitely many instances, FW4/8/12/16_2 RA depth 4 / 8
  / 12 / 16 (REFEREE-2 l. 282) and MW32_2 (L-SI's census, re-run by no referee). In L-1 these two were in the DEAD list; by ruling R-D7a
  (Lead, 07:12Z, before CHECKER; fixes entry 3, «ACCEPTED as ruled.» (l. 82)) L-3's D7 keeps the explicit bound only, with its unit, and the
  FW RA depth 4 / 8 / 12 / 16 (REFEREE-2 36, 4948ce5d; L-SI 47, 4ded1e8d) and the MW(n) multiplicity n (L-SI 47, 2d0344d3, re-run by neither
  the lane nor a referee) enter the DATA clause with their source commits, as L43 asks (DECISIONS, 07139249: «it enters as DATA with its
  numbers and source commit, or not at all» (l. 371)); REFEREE-2 Add. 3: «RA-LOG and the bounded multiplicity leave DEAD (L43). Their
  numbers enter as DATA, with sources:» (l. 491).
- Not signed: packet §9 (DATA and the attack record of L-RED 60-62), §10 (TARGET diff), §11 (machine checks), the dropped corollaries and
  conjectures of l. 39-40 (C-WT, REWIN-ASC, RW-WT, RW-WT*, RW-B0, RW-B0*, DS-TOPS, RA-LOG, ALT-POLY, DS-POLY), the READING remarks;
  REFEREE-2's strengthening of (LEX-Λ)'s conclusion to all pairs (Add. 1 l. 361-362, recorded in fixes entry 2, not used); the referees'
  replays.
- Referee strengthening (NOT part of this entry; referee checks): (i) REFEREE 30: own engine (xicyc_replay.howard, own Γ3 builder, own VJ;
  «No lane code.», l. 73), the 28 pinned instances and families rand, deep, wide, selfl × 200, seed 1992: «**every counter 0**» (l. 77);
  controls ctrlU, ctrlG fire; the lane's split.pins and check199.sh from git archive 63515442 (l. 80-83). (ii) REFEREE-2 36: own engine
  (R2-P-N5-END/r2end.py with r2chain.py's stepping; «No lane, L-RED, REFEREE or L-SI code.», l. 224): 28 pinned runs, «Script output:
  «compared 28 diffs 0».» (l. 236); «Random genomes (gen.out): 7,000 runs, 65,045 changes, every must-0 counter 0.» (l. 239); 2,200 mutants,
  «Every must-0 counter is 0.» (l. 245); the FW6_4 mutant chunk not completed (l. 247-251); controls fire (l. 252-257). (iii) L-RED 60-62
  (not referees): the attack record cited in L-1 and L-3, all PROVED statements SURVIVE (packet §9.2).
- Honest limits: (i) No running-time bound: RE-EQUIV, ALT-EQUIV and C-EQUIV are equivalences (T3 polynomial if and only if Rtop, A, resp. C
  is) and SPLIT-COUNT is a one-way reduction (C polynomial ⇐ max over y, b, J of Dhi_y(b, J) polynomial); neither side is proved polynomial,
  and the open core is max over y, b, J of Dhi_y(b, J). (ii) One run, HOW3(G) on Γ3(G), up to N5′-xi's first fallback; nothing for N5 (SPEC
  S4a), outside Γ3(G), on general parity games or on iteration counts beyond T3. (iii) Everything is CONDITIONAL on RESULTS R125, and six
  premise items are P-N5-CHAIN's frozen text, not RESULTS text (G-4). (iv) ASC-WIT and ASC-ROOT rest on HYPOTHESIS [E-LEV]; they are static
  witnesses, not a bound. (v) PAIR-HIGH and RA-PATHS are abstract (E-MON3 only) and tight with c_y exponential for an abstract counter; the
  game input is §3-§4. (vi) DATA are runs of the lane's engine (box 189 gamma3.build, box 190 n5v.step) and the referees' engines on short
  runs (T3 ≤ 199); they test that no lemma counter fires, not a polynomial bound; large zero counts are DATA, not evidence. (vii) The RA
  depth on FW4/8/12/16_2 and the per-pair multiplicity n on MW(n) are measured on finitely many instances; L-3 carries them as DATA with
  their sources, not as DEAD (ruling R-D7a, L43 above), and the MW multiplicity is L-SI 47's census, re-run by neither the lane nor a
  referee. (viii) Names: REWIN, REWIN-HI, PAIR-SPLIT, SPLIT-COUNT, RW-SHAPE, RW-1, PAIR-HIGH, RA-PATHS, RE-COUNT, RE-EQUIV, PAIR-COUNT,
  ALT-EQUIV, C-EQUIV, ASC-WIT, ASC-ROOT and the instance names are new to RESULTS; «Lemma SPLIT» and «TRANSFER» are also landed names of
  other statements (R39 (a); R29 (b), R104 (b)), so this entry's are «RESULTS R127 Lemma SPLIT» and «RESULTS R127 TRANSFER». (ix)
  Literature: VJ00 §4.2 / Friedmann arXiv 1106.0778 §3 for [VJ] as in R118 / R125; no novelty is claimed. (x) L-3's source note reads «with
  fixes entries 1-4» (R-U127 (d)) and «L-NEW successors 65-67 and 69»: entries 3-4 are successor 71's and line-only (entry 3 «Ruling R-D7a
  (Lead, line-only)», l. 83; entry 4 «applied verbatim, line only», l. 121). (xi) The DATA clause R-D7a added names its quantities in words
  («RA depth (longest RA chain)», «the per-pair multiplicity n on MW(n)») and its source commits, with no output field and no «unit:»;
  R-U127 gave a «unit:» to the three maxima clauses, and R-D7a to D7.
- Data (DATA, not proof): experiments/new/box199/ at l-new 621e6b77 (tools, outputs and instances unchanged since 399cda07, and to 0ea262a0;
  8f4dab7e adds mkl1_199.py and re-pins split.pins, 59 → 61 rows; d0a7d351 adds mkl2_199.py and L-2, 61 → 63; 621e6b77 adds mkl3_199.py and
  L-3, 63 → 65; each re-pins the fixes file): split199.py on R125's engine (box 189 gamma3.build, box 190 n5v.step mode xi from S3 to the
  first fallback), its record split199.out (28 rows, one per frozen instance of box199/inst), check199.sh with its frozen output
  check199.out (5 instances + 6 controls on CX4_n21); box198/pair198.py, pair198.out for D7's fan-in; called from the check.sh blocks «BOX
  199 SPLIT» and «P-N5-SPLIT» (experiments/new/check.sh: the same 15 lines, sha1 e1d2a63c4972afbeef7a8214e5853173c71a2713, at l. 1068-1082
  at 399cda07 and 63515442 and at l. 1071-1085 at 8f4dab7e and 07139249; l. 1071-1085 at 621e6b77 and 0ea262a0 sha1
  f51f824e52056d3e32ad1f248f4eca8fb57b4a07, whose «P-N5-SPLIT» block also asserts L-3's pin row), run by scripts/verify.sh. Re-run by the
  drafter from a full git archive of 0ea262a0: 2026-11-12T09:45:49Z-2026-11-12T09:45:55Z, rc 0, «BOX 199 SPLIT: SPLIT / REWIN / REWIN-HI /
  PAIR-SPLIT / SPLIT-COUNT / RW-1 counters 0, DEAD witnesses present, controls fire = frozen: PASS» and «P-N5-SPLIT: packet and 65 pinned
  files match split.pins, line L-3 a8661c4b pinned: PASS»; with one byte appended to L-3 the «P-N5-SPLIT» block printed «P-N5-SPLIT check:
  FAILED», rc 1, and with one byte prepended to check199.out (a pinned output) the «BOX 199 SPLIT» block printed «BOX 199 SPLIT check:
  FAILED (check199.sh exit 0)», rc 1 (negative controls). The same blocks from a full archive of 8f4dab7e (61 pinned files): rc 0 at
  2026-11-12T06:47:46Z-2026-11-12T06:47:52Z (drafter, first fill). Frozen totals (by script, data127b.py on the archive of 0ea262a0, 40
  checks; data127a.py on 8f4dab7e, 41): the 11 PROVED-lemma counters 0 on all 28; controls hwfail 444, dnfail 219, rhfail 219, rh2fail 313,
  spfail 161, rw1fail 127, gtfail 284; max c_y 6 outside MW (C6G8_n54), MW4/8/16/32_2 9 / 17 / 33 / 65; max split pairs 5 (FW6_4, FW8_4);
  max T3 199; DEAD counters as L-3 (= L-1's; D7 with pair198.out maxRA as its unit). L-3 changes no DATA number: R-D7a moves the FW RA depth
  and the MW(n) multiplicity from D7 into DATA with sources (tools/src127b.py: 4948ce5d R2-P-N5-SPLIT.md l. 272; 4ded1e8d
  docs/si/box90-ra.md, RA depth 4 / 8 / 12 / 16 on FW4/8/12/16_2; 2d0344d3, MW4/8/16/32_2 maxm 4 / 8 / 16 / 32), and R-U127 names the unit
  of each maximum by its split199.out field (maxc, maxSPL, T3; REFEREE-2 Add. 3 «All three are right.» (l. 498); maxSPL 5 on FW6_4 and FW8_4
  only, T3 199 on MW32_2 only, data127b.py). REFEREE-2 read every DATA clause against split199.py (Add. 2, «R-5: MET. I read split199.py
  line by line, all 178 lines (unchanged since 399cda07), against the DATA clause», l. 421).
- Signatures: REFEREE docs/referee/R-P-N5-SPLIT.md: successor 30's report ca091557 (ca091557e43f2a9c6cce3baaa573260dd5e39e3e,
  2026-11-09T09:28:06Z), «docs/referee-2/ and L-RED 62's R228-box91 / R229 reads NOT read before this verdict.» (l. 5-6), verdict table l.
  8-19; successor 31's §C 8c395bff (8c395bffe0f1b0f31f7533715909341914c833b7, 2026-11-11T23:29:45Z) l. 110-141, «**Line L-1 MATCHES** the
  packet read with fixes entries 1-2» (l. 140); successor 31's §E 33cd0fca (33cd0fcaf6c8ce4c88b2f466aec8a20ec09626aa, 2026-11-12T09:18:41Z)
  l. 143-169, «**Line L-3 MATCHES** (= L-1 + R-D7a + R-U127 exactly).» (l. 169). REFEREE-2 docs/referee-2/R2-P-N5-SPLIT.md: successor 36's
  report in boxes 15a05bf0, 026de5fb, b0b7c3f3, 4948ce5d (4948ce5d650b8ef81a15fb6489b39ef5e21854af, 2026-11-09T10:44:20Z) and 991296c9
  (2026-11-11T22:34:15Z), «Independent: docs/referee/ (REFEREE 30's R-P-N5-SPLIT.md, ca091557) NOT read before this report's verdict is
  committed.» (l. 2-3), verdict table l. 329-347; Add. 1 c708c968 (c708c96804dc3b73757bc891e2b1cb079d958fb9, 2026-11-11T22:34:50Z) l.
  353-384; successor 37's Add. 2 c5bc1365 (c5bc13653b1cfad96213249f9781d6277620fadb, 2026-11-11T23:42:02Z) l. 386-469, «L-1 (8f4dab7e, sha1
  634b2fdf) MATCHES.» (l. 465); successor 37's Add. 3 98a64b91 (98a64b91cdb76a71d3f6a7749edc78511c7d5aca, 2026-11-12T09:18:33Z) l. 471-511,
  «Verdict: L-3 (621e6b77, sha1 a8661c4b) MATCHES.» (l. 509). Lane (claude/l-new): L-NEW successor 67, 399cda07 (packet FROZEN) and 63515442
  (fixes entry 1); successor 69, 8f4dab7e (fixes entry 2, L-1); successor 71, d0a7d351 (fixes entry 3, L-2) and 621e6b77 (fixes entry 4,
  L-3). Adversary (not a signature): L-RED 60-62 (R226, R227, R228), cited in L-1 and L-3 as the attack record.
- INDEPENDENCE: each referee wrote its first verdict without reading the other's (REFEREE l. 5-6; REFEREE-2 l. 2-3 and l. 349-351, «I did
  not read docs/referee/ for this packet, nor L-RED's R227 / R228 / R229 reports.»). REFEREE-2 36 read REFEREE's report only after its
  verdict (Add. 1, l. 353 «written after my verdict, committed in 991296c9 and boxes 1-5 on origin»); REFEREE §C tested L-1 with strings
  from its own report, not from the lane generator (l. 113-115), and read R2-P-N5-SPLIT only to check the replay sizes L-1 cites (l.
  133-134); REFEREE-2 37's Add. 2 «I have not read docs/referee/ for this byte test.» (l. 469). Each referee re-derived every proof step and
  replayed the DATA on its own engine; only REFEREE-2 rebuilt L-1 from the lane generator. REFEREE-2 37 byte-tested L-3 with its own code
  («R2-P-N5-SPLIT/bt_l3.py (my code; mkl2_199.py and mkl3_199.py not imported)» (l. 478)) and wrote «I did not read docs/referee/ for this
  test.» (l. 511).
- TARGET.md diff: TARGET.md §2 (M4) asks for one algorithm, polynomial on EVERY parity game, that outputs (W_E, W_O); this entry is a set of
  structural lemmas, exact equivalences and one reduction on one run, HOW3(G) on Γ3(G), for no algorithm on general games (TARGET.md §4:
  «Polynomial only on a restricted class»; packet §10 l. 260-267; REFEREE §6 «No running-time bound; equivalences (T3 polynomial ⇔ Rtop ⇔ A
  ⇔ C polynomial) and one reduction (C ⇐ max Dhi_y(b, J)). Not M3, not M4»; REFEREE-2 box 5 «Not M3, not M4, not a gauntlet step-4 pass, not
  a TARGET.md claim.»). It is not an algorithm claim on every game, so TARGET.md §5's gauntlet does not apply, and it is not a step-4 pass.
  L-3 ends its scope words «so this is not M4; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim», the form of landed
  R123 and R124. GAPS G-N5-TIME: open.

Proposed GAPS line-11 UPDATE (append-only), to go AFTER the last UPDATE on GAPS l. 11 at landing (R126's, «UPDATE 2026-11-12 06:44Z: RESULTS
R126 (P-N5-QN; CHECKER C140 7b2fa753)», the last at 07139249), as a pure insertion with one separating space before the row's closing « |».
BUILT FROM L-3 by tools/upd127b.py (R118's procedure: the direct build of r127a/tools/upd127a.py, itself r126b/tools/upd126b.py's,
unchanged, with R127's constants unchanged: date «(2026-11-11)», start «for every genome G (Ξ-cycles and Ξ self-loops allowed), each
statement PROVED and CONDITIONAL on RESULTS R125 (P-N5-CHAIN), with E_t(v) … σ̄_s(u) at a gate: » (the span up to the first label), its
fifteen labels «(Lemma SPLIT, incl. TRANSFER)», «(Lemma REWIN, Lemma REWIN-HI)», «(Corollary REWIN-COUNT, superseded by SPLIT-COUNT)»,
«(Lemma PAIR-SPLIT)», «(Corollary SPLIT-COUNT)», «(Lemma RW-SHAPE, RW-SHAPE*)», «(Corollary RW-1)», «(Lemma PAIR-HIGH, abstract: any
lex-increasing set sequence, E-MON3 only)», «(Lemma RA-PATHS)», «(Lemma RE-COUNT)», «(Theorem RE-EQUIV)», «(Lemma PAIR-COUNT, corrected
form)», «(Theorem ALT-EQUIV, corrected form)», «(Corollary C-EQUIV)», «(Lemmas ASC-WIT, ASC-ROOT, under HYPOTHESIS [E-LEV]: lev(x) < lev(x′)
implies pr(e_(x,k)) < pr(e_(x′,k′)))», source prefix «(P-N5-SPLIT, docs/new/P-N5-SPLIT.md»), with NO reading; controls on 07139249: the same
function rebuilds R124's landed UPDATE (8cd83060…; filled with 2026-11-09, 09:04, 5b9f4af8 it occurs once on l. 11: True), R125's
(f22faed5…; 2026-11-11, 23:47, 1622c7d9, once: True) and R126's (89c5f357…; 2026-11-12, 06:44, 7b2fa753: it ends l. 11, True); negative
controls (an altered drop string; an altered label) raise errors. sha1 5bd83938b1dfb6603581fc98669593ae2e09c83e of the line without newline
and unfilled (13cbf43e8cb150eb4e27022af7472401a2e9fb37 with its newline), 9828 bytes, 273 «(» / 273 «)», 0 pipe characters; = the first
fill's UPDATE (b7601151…, which the same function rebuilds from L-1: True) with the six replacements of R-D7a and R-U127 applied (True).
<DATE>, <HH:MM> and <checker> are the landing date, time and the CHECKER commit of the PASS (C141), all filled at landing:
UPDATE <DATE> <HH:MM>Z: RESULTS R127 (P-N5-SPLIT; CHECKER C141 <checker>) [refereed-only] LANDED: On HOW3(G), i.e. N5′-xi from S3 on Γ3(G) until its first fallback (the Howard run on Γ3(G) of RESULTS R125 (P-N5-CHAIN), states 0, …, T3, n3 = N + 7M + 10; by R125's REACH3-ALL the mover part of N5′-xi from S3 until its first fallback), for every genome G (Ξ-cycles and Ξ self-loops allowed), each statement PROVED and CONDITIONAL on RESULTS R125 (P-N5-CHAIN), with E_t(v) the e-vertices of Π_t(v), sets of e-vertices ordered lexicographically by the most relevant differing element, a Λ-interval I of v a maximal interval of states with Λ_t(v) constant, a change a step t − 1 → t in I with E_(t−1)(v) ≠ E_t(v), its top the most relevant element of E_(t−1)(v) Δ E_t(v), U_y the e-vertices more relevant than y, c_y(v, I) the number of changes in I with top y, Dhi_y(v, I) the number of distinct values of E_t(v) ∩ U_y on I, C := max over v, I, y of c_y(v, I), and nx_s(u) := σ_s(u) at a mover, σ̄_s(u) at a gate: at every change of (v, I), the first vertex u at which the plays P_(t−1)(v), P_t(v) leave by different edges is a mover with σ_(t−1)(u) ≠ σ_t(u) and Ω_(t−1)(new) ▷ Ω_(t−1)(old), or a gate with σ̄_(t−1)(u) ≠ σ̄_t(u) whose abandoned face rose strictly, Ω_t(old) ▷ Ω_t(new) ⊵ Ω_(t−1)(new) ▷ Ω_(t−1)(old); and Λ_(t−1)(u) = Λ_t(u) and E_(t−1)(v) Δ E_t(v) = E_(t−1)(u) Δ E_t(u) (Lemma SPLIT, incl. TRANSFER); for two consecutive y-tops t1 < t2 of (v, I) with the same split u and the same new successor b := nx_t1(u) = nx_t2(u), and a := nx_(t2−1)(u): (a) Ω_(t2−1)(a) ▷ Ω_t1(b), (b) Ω_(t2−1)(b) ▷ Ω_(t2−1)(a) ▷ Ω_t1(b), (c) E_t2(b) ∩ U_y >lex E_t1(b) ∩ U_y (Lemma REWIN, Lemma REWIN-HI); c_y(v, I) ≤ 1 + W_y(v, I) + Σ_(u,b) (Dhi_y(b, J_b) − 1), W_y the number of consecutive y-top couples with different split pairs (Corollary REWIN-COUNT, superseded by SPLIT-COUNT); (a′), (b′), (c′) hold for ANY two y-tops t < t′ of (v, I) through the same split pair (u, b), with a := nx_(t′−1)(u): Ω_(t′−1)(a) ▷ Ω_t(b), Ω_(t′−1)(b) ▷ Ω_t(b), E_t′(b) ∩ U_y >lex E_t(b) ∩ U_y (Lemma PAIR-SPLIT); c_y(v, I) ≤ Σ_((u,b) ∈ SPL_y(v,I)) Dhi_y(b, J_b) ≤ 3M · max_((u,b)) Dhi_y(b, J_b), SPL_y(v, I) the split pairs of the y-tops of (v, I) and J_b the Λ-interval of b containing the y-tops through (u, b), so C polynomial ⇐ max over y, b, J of Dhi_y(b, J) polynomial (a reduction, not an equivalence) (Corollary SPLIT-COUNT); for same-pair y-tops t < t′ through (u, b) (consecutive, resp. any), m := wt(y), E_s(b) ∩ U_y = B_s ⊔ S_s with B_s the U_y-letters of b's play at s before y and S_s := E_s(m) ∩ U_y: if S_t = S_t′, then B_t′ ≠ ∅ and for every f ∈ B_t′ some vertex of P_t′(b) strictly between f and y has nx_(t′−1) ≠ nx_t′ (Lemma RW-SHAPE, RW-SHAPE*); at every such couple whose t′-step is single-split, S_t ≠ S_t′ (Corollary RW-1); on (v, I), c_y ≤ Dhi_y, A_xy ≤ 2·Dhi_y + 1 (A_xy the longest x/y-alternating subsequence of the tops, y more relevant than x) and Dhi_y = 1 + Σ_(z ∈ U_y) c_z (Lemma PAIR-HIGH, abstract: any lex-increasing set sequence, E-MON3 only); c_y ≤ P(y), the number of directed paths from y in the graph RA of most relevant tops strictly between consecutive y-tops (Lemma RA-PATHS); D_I(v) ≤ 1 + Mact_I(v) + Rtop_I(v) (D_I(v) the number of distinct sets E_t(v), t ∈ I; Mact_I(v) the number of e-vertices in ⋃_(t∈I) E_t(v); Rtop_I(v) the number of changes in I whose top lies in E_s(v) for some s ∈ I, s < t − 1) (Lemma RE-COUNT); T3 ≤ (1 + n3·((2M + 3)(M + 1) − 1) + Rtop)·(L3 + 1) and Rtop ≤ n3·T3, so T3 is polynomial in N + M iff Rtop is (Theorem RE-EQUIV); a sequence over m letters with no two equal consecutive letters has length ≤ 1 + Σ_(x<y) max(0, A_xy − 1) (Lemma PAIR-COUNT, corrected form); with A := max(1, the longest two-letter alternation in tops(v, I) over v, I), T3 ≤ (1 + n3·((2M + 3)·(2 + C(M, 2)·(A − 1)) − 1))·(L3 + 1) and A ≤ max(1, T3), so T3 is polynomial iff A is (Theorem ALT-EQUIV, corrected form); T3 ≤ (1 + n3·((2M + 3)(1 + M·C) − 1))·(L3 + 1) and C ≤ max(1, T3), so T3 is polynomial iff C is (Corollary C-EQUIV); at an ascent (c_i, c_(i+1)) of seq_t(v), y the successor of c_i and g1 the gate of σ_t(y): σ̄_t(g1) = pβ_(g1), Ω_t(pe_(g1)) ▷ Ω_t(pβ_(g1)), and either Λ_t(pe_(g1)) = Λ_t(v) and E_t(pe_(g1)) contains an e-vertex at least as relevant as c_(i+1), or Λ_t(pe_(g1)) has strictly larger reward than Λ_t(v); and at the first ascent there is a gate g* with lev(g*) < lev(c_i), σ̄_t(g*) = pβ_(g*) and Ω_t(pe_(g*)) ▷ Ω_t(pβ_(g*)), whose W-face's cycle node has strictly larger reward than Λ_t(v) (premises: RESULTS R125 (P-N5-CHAIN): HOW3, REACH3-ALL, F1, F3, F4′, F5, F6, DOM, STRICT, CN2-3, LOC-GATE3, LOC-K2-3, B-ONLY3, NO-TIE3, T-QUIET3 with L3, E-MON3, CHAIN-DECOMP3; [DEF] = RESULTS R104's definitions of the genome and of Γ(G); [G3] = RESULTS R117's definition of Γ3(G); [OPT] = RESULTS R118 (b) and RESULTS R21 (a) (σ̄_t optimal at every vertex at once); (R), (P), (E-DOM), (Core) in its W-1-repaired reading (the only edge into the eight-vertex core from outside is pb_g → K0), F2 and CYC: P-N5-CHAIN's frozen text (l-new 93531b03, sha1 6e613ba7, §2 and §4); (LEX-Λ) is applied only to non-core vertices (pads), where P-N5-CHAIN's W-1 repair holds (pads of movers and gates; P-N5-CHAIN fixes entry 3, R-W; referee-originated: REFEREE-2 R2-P-N5-SPLIT W-1; also REFEREE R-P-N5-SPLIT SP-1); [E-LEV] only in ASC-WIT and ASC-ROOT; not used: any other packet, any other R-id, any L-RED or L-SI lemma) (Lemmas ASC-WIT, ASC-ROOT, under HYPOTHESIS [E-LEV]: lev(x) < lev(x′) implies pr(e_(x,k)) < pr(e_(x′,k′))): this proves no running-time bound: RE-EQUIV, ALT-EQUIV and C-EQUIV are equivalences and SPLIT-COUNT is a reduction, and neither side is proved polynomial; the open core is max over y, b, J of Dhi_y(b, J); nothing is claimed for N5 (SPEC S4a), outside Γ3(G), or on iteration counts beyond T3; DEAD (each with the instance that kills it, experiments/new/box199/inst, sha1 prefix; none is a premise): D1 «each re-win of y at u is paid by a class change of a vertex on the y-route below y» (CX4_n21, ef29debb; dn_nobelow_all 192, unit: re-wins); D2 «E(wt(y)) ∩ U_y changes between any two consecutive y-tops» (GROW7_n34, 42bbd562; wcfail 18, unit: re-entries); D3 «c_y(v) ≤ the number of values of E(wt(y)) ∩ U_y on the span» (HOLD2K_n84, 423a4a88; wbfail 18, unit: (v, I, y)); D4 ROUTE-LOW «no U_y-letter on v's new play between u and y at a y-top» (ROUTELOW_n21, 80f9b977; ytopB_ne 65, unit: y-tops); D5 the product-chain idea «the U_y-letters before y on v's play are lex-monotone at y-tops» (GROW7_n34; premono_no 18, unit: (v, I, y)); D6 CONJECTURES RW-WT, RW-WT*, RW-B0, RW-B0* (RWX_n95, da8b3a30, L-RED 62; rwfail 31, unit: re-wins); D7 fan-in 1 of RA as a game property (NK6_cl21, 408b9988, fan-in 3; DSALT9_n416, da3308b5, fan-in 4; unit: max over (v, I, y) of the number of letters of RA(y), box198/pair198.out maxRA); DATA, clause by clause (tool experiments/new/box199/split199.py on R125's engine: box 189 gamma3.build, box 190 n5v.step mode xi from S3 to the first fallback; set: the 28 frozen instances of experiments/new/box199/inst; record box199/split199.out; check199.sh re-run by check.sh): every PROVED-lemma counter 0 on all 28: playfail, kindfail, hwfail, gtfail, trfail (unit: changes at (v, I); SPLIT), dnfail (REWIN), rhfail (REWIN-HI), rw1fail (RW-1) (unit: re-wins), rh2fail (unit: same-pair couples, all pairs t < t′; PAIR-SPLIT), spfail (unit: (v, I, y); SPLIT-COUNT's first inequality with Dhi_y(b, J_b) replaced by the number of distinct values of E(b) ∩ U_y at the pair's own y-tops, a lower bound for Dhi_y(b, J_b), so spfail 0 is the stronger statement), wlamfail (unit: re-entries; Λ(wt(y)) = w at both y-tops); playfail, kindfail, trfail and wlamfail are definition checks without a firing control; every other counter has one (check199.out on CX4_n21: hwfail 444, dnfail 219, rhfail 219, rh2fail 313, spfail 161, rw1fail 127, gtfail 284); on the 28 frozen instances max c_y (unit: y-tops of one (v, I, y), max over (v, I, y); split199.out maxc) ≤ 6 outside the MW family (C6G8_n54: 6) and MW(n) has max c_y = 2n + 1 (65 on MW32_2); max split pairs (unit: distinct split pairs (u, b) of the y-tops of one (v, I, y), max over (v, I, y); split199.out maxSPL) 5 (FW6_4, FW8_4); RA depth (longest RA chain) 4 / 8 / 12 / 16 on FW4/8/12/16_2 (REFEREE-2 36 R2-P-N5-SPLIT, claude/referee-2 4948ce5d, own engine; L-SI 47 box 90, claude/l-si 4ded1e8d) and the per-pair multiplicity n on MW(n) (L-SI 47 box 90, claude/l-si 2d0344d3, not re-run by the lane or a referee), DATA only; every run is short (T3 ≤ 199; unit: states of the HOW3 run, max over the 28 frozen instances, split199.out T3; 199 on MW32_2) and nothing here tests a polynomial bound; large zero counts are DATA, not evidence of a lemma; independent replays, every fail counter 0, cited, not re-run: REFEREE 30 R-P-N5-SPLIT §4 (claude/referee ca091557; 28 pinned instances and 800 random genomes), REFEREE-2 36 R2-P-N5-SPLIT (claude/referee-2 991296c9; 28 pinned, 7,000 random and 2,200 mutants, D1-D7 re-run); attack record L-RED 60-62 (R226, R227, R228; all PROVED statements SURVIVE); N5′-xi stays a CANDIDATE (D1); TARGET.md §2 (M4) asks for an algorithm polynomial on every parity game and §4 says a bound on a restricted class is not M4, so this is not M4 (P-N5-SPLIT, docs/new/P-N5-SPLIT.md, frozen at l-new 399cda07, sha1 5bc1b1f3, with fixes entries 1-4, docs/new/P-N5-SPLIT-fixes.md; sources boxes 197-199; L-NEW successors 65-67 and 69). G-N5-TIME stays open.

Addendum (subagent, first fill; checks run on the pass-1 draft, whose title, entry block, GAPS preamble and UPDATE are byte-equal to this
file's; outputs r127a/*_p1.out; the final run on this file is r127a/*_final.out). Verbatim key lines, with «|» printed as «¦»:
  [chk] model: landed R126 title (07139249) == «### R126 [refereed-only] » + R126 L-2 + «, CHECKER PASS (docs/checker/C140.md, checker 7b2fa753)»: True
  [chk] file: sha1 d19902c10319f8b50bcfc8079bb3db6c90c7a1d1 bytes 71175 lines 406 ends with newline True
  [chk] ### R headings at d[...]: [222]
  [chk] (a) title == prefix + L-1 (no newline) + tail: True ; middle bytes == L-1 bytes without newline: True
  [chk]     title: 9012 chars, 9327 bytes, sha1 fc1f319c4a9953c9cd0cc695c51542ecd39d662d, ( 261 ) 261, min depth 0, final 0, ¦ 0, fill token 1
  [chk] (e) entry block d[222:388] (lines 223-388, 166 lines, sha1 of the joined block 8c03c53c08f7acb98d8e9b4923b9714a977642f1); next line blank: True; line after: 'Proposed GAPS line-11 UPDATE (append-onl'
  [chk] (b) fill token in the entry block: 1 ; in the whole file: 1 at lines [223]
  [chk]     «\n**Erratum E-1** (not a result» in the block: False ; line-start «**Erratum» in the file: 0 ; empty lines inside the block: 0
  [chk] (e) UPDATE line(s) at d[...]: [404] (line [405])
  [chk]     GAPS preamble at d[389:404]
  [chk] (c) "¦" in entry block: 0 ; in UPDATE: 0 ; in GAPS preamble: 1 (the quoted « ¦» of the row end); in the file: 8
  [chk] (d) UPDATE <DATE> 1 <HH:MM> 1 <checker> 1; head at its start: True
  [chk]     UPDATE = upd127L1.txt: True ; sha1 (no newline) b7601151eaa454196e90a91da340b7c16606df68 ; with newline a5273a490cee70e4ff98eb4e78e6aa9f1f691a26 ; 9281 bytes ( 260 ) 260
  [chk]     stale grep, entry block minus title (case-insensitive): {}
  [chk]     stale grep, title: {'pending': 1, 'candidate': 1} ; UPDATE: {'candidate': 1}
  [chk]     line 1 «NOT LANDED» 1 ; «<DATE>» in file 2 ; «<checker>» 2 ; «<HH:MM>» 2
  [chk] (e) slices: line 1 d[0]; FIRST FILL record d[1:221] (+ blank d[221]: ''); title d[222]; entry d[222:388]; blank d[388]; preamble d[389:404]; UPDATE d[404]; blank d[405]: ''; Addendum none
  [chk] (f) QUOTE SWEEP (corpus: 55 texts)
  [chk]     sweep line 1: 1 quotes, 1 parts, 0 not found []
  [chk]     sweep FIRST FILL record: 184 quotes, 161 parts, 0 not found []
  [chk]     sweep entry block: 101 quotes, 101 parts, 2 not found ['RESULTS R127 Lemma SPLIT', 'RESULTS R127 TRANSFER']
  [chk]     sweep GAPS preamble + UPDATE: 25 quotes, 25 parts, 0 not found []
  [chk]     sweep whole file: 311 quotes, 288 parts, 2 not found ['RESULTS R127 Lemma SPLIT', 'RESULTS R127 TRANSFER']
  [chk]     sweep NEGATIVE CONTROL: 1 quotes, 1 parts, 1 not found ['SPLIT-COUNT bounds T3 by M squared on every genome']
  [chk]     negative control reported missing: True
  [lp] cites 98 (96 shown in the draft as «quote», 2 used for a line number only) in 10 (commit, file) pairs; failed at the cited lines: 0 []
  [lp] shown quotes not in the draft as «quote»: 0 []
  [lp] NEGATIVE CONTROL 1 (window shifted by 40 lines): 0 of 98 still pass []
  [lp] NEGATIVE CONTROL 2 (longest word mutated): 0 of 98 still pass
  [lp]     07139249 TARGET.md 1
  [lp]     07139249 docs/DECISIONS.md 4
  [lp]     399cda07 docs/new/P-N5-SPLIT.md 20
  [lp]     63515442 docs/new/P-N5-SPLIT-fixes.md 3
  [lp]     8c395bff docs/referee/R-P-N5-SPLIT.md 7
  [lp]     8f4dab7e docs/new/N5-PAIR-box198.md 2
  [lp]     8f4dab7e docs/new/N5-SPLIT-box199.md 2
  [lp]     8f4dab7e docs/new/P-N5-SPLIT-fixes.md 5
  [lp]     c5bc1365 docs/referee-2/R2-P-N5-SPLIT.md 33
  [lp]     ca091557 docs/referee/R-P-N5-SPLIT.md 21
  [hex] hex ids in the draft: 89; git objects 59; measured sha1s (not objects) 30; neither: 0 []
  [hex] NEGATIVE CONTROL (0badc0de1, 1234abcd9f): neither: 2 ['0badc0de1', '1234abcd9f']
  [sim] trunk 07139249 RESULTS sha1 0ef236b9b7146cd19fcc380c4fcd2a7314aec402 lines 16545 "¦" 1477 ; GAPS sha1 2965fc2ec61b5ddebc529d9ee21c285100914940 lines 23
  [sim] pure insertion: prefix byte-unchanged True ; suffix byte-unchanged True ; inserted lines 167
  [sim] headings after insertion: {'R125': [15595], 'R126': [15726], 'R127': [15903], 'E-1': [16070], 'E-2': [16083], 'E-3': [16111], 'Dead': [16142]}
  [sim] R126 at l. 15726 (unchanged: True); R127 at l. 15903-16068, blank l. 16069 (''), «**Erratum E-1**» l. 16070; the line before R127: l. 15902 '' (R126's block ends l. 15901)
  [sim] order R125 < R126 < R127 < E-1 < E-2 < E-3 < Dead ends: True
  [sim] RESULTS lines 16545 -> 16712 (+167) ; "¦" 1477 -> 1477 (unchanged True) ; «checker 3333333)» once True ; fill token 0
  [sim] ### R1xx headings: 28, R127 the last: True
  [sim] GAPS: only l. 11 changes True ; lines 23 -> 23 ; l. 11 "¦" 76 -> 76 ; «UPDATE 2026-» 61 -> 61 ; R127 last: True ; after R126's (2026-11-12 06:44Z, 7b2fa753): True ; prefix byte-unchanged: True
  [sim] GAPS whole file "¦" 198 -> 198
  [sim] fill values used only here: 2099-01-11 00:00 3333333

Addendum 2 (subagent, for the Lead; does not land; second fill, 2026-11-12T09:52:22Z by date -u). (1) SECOND FILL on line L-3 (l-new
621e6b77, sha1 a8661c4b…), to CHECKER C141. Built in the scratchpad by fill2.py from r127a/R127-draft.md (sha1 80a1f05c…, asserted; =
docs/agents/R127-draft.md at the Lead's record commit 039b0558); I merged, committed and pushed nothing and wrote nothing into the
repository; the Lead commits this file. (2) WHAT IS LEFT: REFEREE §E (33cd0fca) on origin, read and quoted; CHECKER C141 on this file; the
Lead's merges of claude/l-new (621e6b77 or later), claude/referee-2 (98a64b91), claude/referee (§E's commit) and claude/checker (C141's
commit), none of them an ancestor of 07139249; then the Lead lands R127 after R126 with <DATE>, <HH:MM> and <checker> filled. (3) Scratch:
/tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad/r127b/ (arch/ = full git archive of
0ea262a0; mk/ = archive of 621e6b77 for the generator chain; blocks.*, neg.*, neg2.*, mk.out; tools/blocks199.sh, blocksplit.sh,
blockbox.sh, runblocks.sh, upd127b.py, prem127b.py, data127b.py, src127b.py, chk127b.py, lp127b.py, hex127b.py, sim127b.py with their *.out,
*_p1.out and *_final.out; fill2.py, cites2.json, fetch.txt, fetch.log, heads.txt, filltime.txt, upd127L3.txt, R127-draft.pre.md (pass 1);
report.txt). (4) NOT DONE: scripts/verify.sh and scripts/push.sh not run (the two box 199 blocks of experiments/new/check.sh only, and each
block once more for its negative control); the referees' scripts (bt_l3.py, r2split.py) not re-run; the proofs not re-derived; REFEREE §E
not read (not on origin); no Oink run (L-3 cites no Oink check). (5) Checks on the pass-1 draft, whose line 1, SECOND FILL section, title,
entry block, GAPS preamble and UPDATE are byte-equal to this file's (outputs r127b/*_p1.out; the final run on this file is
r127b/*_final.out). Verbatim output lines, with «|» printed as «¦» and the guillemets as ‹ ›, so that they are not read as quotes of this
file:
  [chk] model: landed R126 title (07139249) == ‹### R126 [refereed-only] › + R126 L-2 + ‹, CHECKER PASS (docs/checker/C140.md, checker 7b2fa753)›: True
  [chk] file: sha1 9bad502c699f1b7505dad49c7cf5224c20e73166 bytes 102921 lines 655 ends with newline True
  [chk] ### R headings at d[...]: [344]
  [chk] (a) title == prefix + L-3 (no newline) + tail: True ; middle bytes == L-3 bytes without newline: True
  [chk]     title: 9559 chars, 9874 bytes, sha1 a82ef899ec8ffd1cc539b39a8ba8de3b92649311, ( 274 ) 274, min depth 0, final 0, ¦ 0, fill token 1
  [chk] (e) entry block d[344:565] (lines 345-565, 221 lines, sha1 of the joined block d9d378c687ace606e0e795f5f3c293238fb7733f); next line blank: True; line after: 'Proposed GAPS line-11 UPDATE (append-onl'
  [chk] (b) fill token in the entry block: 1 ; in the whole file: 1 at lines [345]
  [chk]     ‹\n**Erratum E-1** (not a result› in the block: False ; line-start ‹**Erratum› in the file: 0 ; empty lines inside the block: 0
  [chk] (e) UPDATE line(s) at d[...]: [582] (line [583])
  [chk]     GAPS preamble at d[566:582]
  [chk] (c) "¦" in entry block: 0 ; in UPDATE: 0 ; in GAPS preamble: 1 (the quoted ‹ ¦› of the row end); in the file: 12
  [chk] (d) UPDATE <DATE> 1 <HH:MM> 1 <checker> 1; head at its start: True
  [chk]     UPDATE = upd127L3.txt: True ; sha1 (no newline) 5bd83938b1dfb6603581fc98669593ae2e09c83e ; with newline 13cbf43e8cb150eb4e27022af7472401a2e9fb37 ; 9828 bytes ( 273 ) 273
  [chk]     stale grep, entry block minus title (case-insensitive): {'pending': 4, 'first fill': 1}
  [chk]       'pending' at block lines: [(407, ' quoted below); its §E on L-3 is commit 33cd0fca (pending on origin'), (410, 'ca091557; successor 31: §C 8c395bff, §E 33cd0fca (pending on origin'), (427, '  pending on origin'), (541, " 140); successor 31's §E on L-3, commit 33cd0fca (pending on origin")]
  [chk]     stale grep, title: {'pending': 1, 'candidate': 1} ; UPDATE: {'candidate': 1}
  [chk]     line 1 ‹NOT LANDED› 1 ; ‹<DATE>› in file 5 ; ‹<checker>› 5 ; ‹<HH:MM>› 5
  [chk]     SECOND FILL section d[1:123]; Addendum 2 d[638:655]
  [chk] (e) slices: line 1 d[0]; FIRST FILL record d[123:343] (+ blank d[343]: ''); title d[344]; entry d[344:565]; blank d[565]; preamble d[566:582]; UPDATE d[582]; blank d[583]: ''; Addendum d[584:637]
  [chk] (f) QUOTE SWEEP (corpus: 86 texts)
  [chk]     sweep line 1: 1 quotes, 1 parts, 0 not found []
  [chk]     sweep FIRST FILL record: 184 quotes, 161 parts, 0 not found []
  [chk]     sweep entry block: 141 quotes, 147 parts, 0 not found []
  [chk]     sweep GAPS preamble + UPDATE: 27 quotes, 25 parts, 0 not found []
  [chk]     sweep first fill Addendum: 16 quotes, 11 parts, 0 not found []
  [chk]     sweep Addendum 2: 2 quotes, 0 parts, 0 not found []
  [chk]     sweep SECOND FILL section: 64 quotes, 65 parts, 0 not found []
  [chk]     sweep whole file: 435 quotes, 410 parts, 0 not found []
  [chk]     sweep NEGATIVE CONTROL: 1 quotes, 1 parts, 1 not found ['SPLIT-COUNT bounds T3 by M squared on every genome']
  [chk]     negative control reported missing: True
  [chk] [rec] FIRST FILL record + blank: this d[123:344] == first fill d[1:222]: True (221 lines)
  [chk] [rec] first fill Addendum: this d[584:637] == first fill d[406:459]: True (53 lines); blank before: '', after: ''
  [chk] [rec] first fill title in this file: 0; first fill UPDATE (b7601151) in this file: 0; first fill line 1: 0
  [chk] [rec] token diff L-1 -> L-3: 10 hunks, 20 tokens out, 122 in
  [chk] [rec]     delete 'and RA-LOG / bounded multiplicity' -> ''
  [chk] [rec]     insert '' -> 'a'
  [chk] [rec]     replace 'properties' -> 'property'
  [chk] [rec]     insert '' -> 'da3308b5,'
  [chk] [rec]     replace 'FW16_2, 94df42b7, linear RA depth; MW32_2, 445031d1, multiplicity n, L-SI DATA cited);' -> 'unit: max over (v, I, y) of the number of letters of RA(y), box198/pair198.out maxRA);'
  [chk] [rec]     insert '' -> '(unit: y-tops of one (v, I, y), max over (v, I, y); split199.out maxc)'
  [chk] [rec]     insert '' -> '(unit: distinct split pairs (u, b) of the y-tops of one (v, I, y), max over (v, I, y); split199.out
  [chk] [rec]     insert '' -> 'RA depth (longest RA chain) 4 / 8 / 12 / 16 on FW4/8/12/16_2 (REFEREE-2 36 R2-P-N5-SPLIT, claude/re
  [chk] [rec]     replace '199)' -> '199; unit: states of the HOW3 run, max over the 28 frozen instances, split199.out T3; 199 on MW32_2
  [chk] [rec]     replace '1-2,' -> '1-4,'
  [chk] [rec] token diff title (first fill -> this): 10 hunks, 20 tokens out, 122 in
  [chk] [rec] token diff entry block without title (first fill -> this): 67 hunks, 76 tokens out, 1224 in
  [chk] [G-S] L-3 stale grep: {'unlanded': 0, 'not landed': 0, 'when landed': 0, 'pending': 0, 'to land': 0, 'landing': 0, 'landed': 0, 'will ': 0, 'not yet': 0}; ‹CANDIDATE› 1; ‹stays› 2
  [lp] cites 25 (25 shown in the draft as ‹quote›, 0 used for a line number only) in 3 (commit, file) pairs; failed at the cited lines: 0 []
  [lp] shown quotes not in the draft as ‹quote›: 0 []
  [lp] NEGATIVE CONTROL 1 (window shifted by 40 lines): 0 of 25 still pass []
  [lp] NEGATIVE CONTROL 2 (longest word mutated): 0 of 25 still pass
  [lp]     07139249 docs/DECISIONS.md 1
  [lp]     621e6b77 docs/new/P-N5-SPLIT-fixes.md 10
  [lp]     98a64b91 docs/referee-2/R2-P-N5-SPLIT.md 14
  [hex] hex ids in the draft: 126; git objects 78; measured sha1s (not objects) 47; named as pending on origin (REFEREE §E, Lead brief): ['33cd0fca']; neither: 0 []
  [hex]     da3308b5 in the draft: True; git object: False; measured: True
  [hex]     4948ce5d in the draft: True; git object: True; measured: False
  [hex]     4ded1e8d in the draft: True; git object: True; measured: False
  [hex]     2d0344d3 in the draft: True; git object: True; measured: False
  [hex] NEGATIVE CONTROL (0badc0de1, 1234abcd9f): neither: 2 ['0badc0de1', '1234abcd9f']
  [sim] trunk 07139249 RESULTS sha1 0ef236b9b7146cd19fcc380c4fcd2a7314aec402 lines 16545 "¦" 1477 ; GAPS sha1 2965fc2ec61b5ddebc529d9ee21c285100914940 lines 23
  [sim] pure insertion: prefix byte-unchanged True ; suffix byte-unchanged True ; inserted lines 222
  [sim] headings after insertion: {'R125': [15595], 'R126': [15726], 'R127': [15903], 'E-1': [16125], 'E-2': [16138], 'E-3': [16166], 'Dead': [16197]}
  [sim] R126 at l. 15726 (unchanged: True); R127 at l. 15903-16123, blank l. 16124 (''), ‹**Erratum E-1**› l. 16125; the line before R127: l. 15902 '' (R126's block ends l. 15901)
  [sim] order R125 < R126 < R127 < E-1 < E-2 < E-3 < Dead ends: True
  [sim] RESULTS lines 16545 -> 16767 (+222) ; "¦" 1477 -> 1477 (unchanged True) ; ‹checker 3333333)› once True ; fill token 0
  [sim] ### R1xx headings: 28, R127 the last: True
  [sim] GAPS: only l. 11 changes True ; lines 23 -> 23 ; l. 11 "¦" 76 -> 76 ; ‹UPDATE 2026-› 61 -> 61 ; R127 last: True ; after R126's (2026-11-12 06:44Z, 7b2fa753): True ; prefix byte-unchanged: True
  [sim] GAPS whole file "¦" 198 -> 198
  [sim] fill values used only here: 2099-01-11 00:00 3333333

Addendum 3 (subagent, for the Lead; does not land; third fill, 2026-11-12T10:29:09Z by date -u). Checks re-run by r127c/tools/chk127c.py,
hex127c.py and sim127c.py on the pass-1 draft, whose line 1, THIRD FILL note, entry block, GAPS preamble and UPDATE are byte-equal to this
file's (outputs r127c/*_p1.out; the final run on this file is r127c/*_final.out). Verbatim output lines, with «|» printed as «¦» and the
guillemets as ‹ ›:
  [chk] model: landed R126 title (07139249) == ‹### R126 [refereed-only] › + R126 L-2 + ‹, CHECKER PASS (docs/checker/C140.md, checker 7b2fa753)›: True
  [chk] file: sha1 508c589b2863965fd9c15537114f2783062e7374 bytes 114730 lines 765 ends with newline True
  [chk] ### R headings at d[...]: [377]
  [chk] (a) title == prefix + L-3 (no newline) + tail: True ; middle bytes == L-3 bytes without newline: True
  [chk]     title: 9559 chars, 9874 bytes, sha1 a82ef899ec8ffd1cc539b39a8ba8de3b92649311, ( 274 ) 274, min depth 0, final 0, ¦ 0, fill token 1
  [chk] (e) entry block d[377:600] (lines 378-600, 223 lines, sha1 of the joined block 81b9888424e937fe9d661ffa9b586700e33379f1); next line blank: True; line after: 'Proposed GAPS line-11 UPDATE (append-onl'
  [chk] (b) fill token in the entry block: 1 ; in the whole file: 1 at lines [378]
  [chk]     ‹\n**Erratum E-1** (not a result› in the block: False ; line-start ‹**Erratum› in the file: 0 ; empty lines inside the block: 0
  [chk] (e) UPDATE line(s) at d[...]: [617] (line [618])
  [chk]     GAPS preamble at d[601:617]
  [chk] (c) "¦" in entry block: 0 ; in UPDATE: 0 ; in GAPS preamble: 1 (the quoted ‹ ¦› of the row end); in the file: 13
  [chk] (d) UPDATE <DATE> 1 <HH:MM> 1 <checker> 1; head at its start: True
  [chk]     UPDATE = upd127L3.txt: True ; sha1 (no newline) 5bd83938b1dfb6603581fc98669593ae2e09c83e ; with newline 13cbf43e8cb150eb4e27022af7472401a2e9fb37 ; 9828 bytes ( 273 ) 273
  [chk]     stale grep, entry block minus title (case-insensitive): {'first fill': 1}
  [chk]     stale grep, title: {'pending': 1, 'candidate': 1} ; UPDATE: {'candidate': 1}
  [chk]     line 1 ‹NOT LANDED› 1 ; ‹<DATE>› in file 7 ; ‹<checker>› 7 ; ‹<HH:MM>› 7
  [chk]     THIRD FILL note d[1:34]; Addendum 3 d[760:765]
  [chk]     SECOND FILL section d[34:156]; Addendum 2 d[673:765]
  [chk] (e) slices: line 1 d[0]; FIRST FILL record d[156:376] (+ blank d[376]: ''); title d[377]; entry d[377:600]; blank d[600]; preamble d[601:617]; UPDATE d[617]; blank d[618]: ''; Addendum d[619:672]
  [chk] (f) QUOTE SWEEP (corpus: 95 texts)
  [chk]     sweep line 1: 1 quotes, 1 parts, 0 not found []
  [chk]     sweep FIRST FILL record: 184 quotes, 161 parts, 0 not found []
  [chk]     sweep entry block: 146 quotes, 152 parts, 0 not found []
  [chk]     sweep GAPS preamble + UPDATE: 27 quotes, 25 parts, 0 not found []
  [chk]     sweep first fill Addendum: 16 quotes, 11 parts, 0 not found []
  [chk]     sweep Addendum 2: 2 quotes, 0 parts, 0 not found []
  [chk]     sweep Addendum 3: 2 quotes, 0 parts, 0 not found []
  [chk]     sweep THIRD FILL note: 12 quotes, 12 parts, 0 not found []
  [chk]     sweep SECOND FILL section: 64 quotes, 65 parts, 0 not found []
  [chk]     sweep whole file: 454 quotes, 427 parts, 0 not found []
  [chk]     sweep NEGATIVE CONTROL: 1 quotes, 1 parts, 1 not found ['SPLIT-COUNT bounds T3 by M squared on every genome']
  [chk]     negative control reported missing: True
  [chk] [rec] FIRST FILL record + blank: this d[156:377] == first fill d[1:222]: True (221 lines)
  [chk] [rec] first fill Addendum: this d[619:672] == first fill d[406:459]: True (53 lines); blank before: '', after: ''
  [chk] [rec] first fill title in this file: 0; first fill UPDATE (b7601151) in this file: 0; first fill line 1: 0
  [chk] [rec] token diff L-1 -> L-3: 10 hunks, 20 tokens out, 122 in
  [chk] [rec]     delete 'and RA-LOG / bounded multiplicity' -> ''
  [chk] [rec]     insert '' -> 'a'
  [chk] [rec]     replace 'properties' -> 'property'
  [chk] [rec]     insert '' -> 'da3308b5,'
  [chk] [rec]     replace 'FW16_2, 94df42b7, linear RA depth; MW32_2, 445031d1, multiplicity n, L-SI DATA cited);' -> 'unit: max over (v, I, y) of the number of letters of RA(y), box198/pair198.out maxRA);'
  [chk] [rec]     insert '' -> '(unit: y-tops of one (v, I, y), max over (v, I, y); split199.out maxc)'
  [chk] [rec]     insert '' -> '(unit: distinct split pairs (u, b) of the y-tops of one (v, I, y), max over (v, I, y); split199.out
  [chk] [rec]     insert '' -> 'RA depth (longest RA chain) 4 / 8 / 12 / 16 on FW4/8/12/16_2 (REFEREE-2 36 R2-P-N5-SPLIT, claude/re
  [chk] [rec]     replace '199)' -> '199; unit: states of the HOW3 run, max over the 28 frozen instances, split199.out T3; 199 on MW32_2
  [chk] [rec]     replace '1-2,' -> '1-4,'
  [chk] [rec] token diff title (first fill -> this): 10 hunks, 20 tokens out, 122 in
  [chk] [rec3] vs second fill: SECOND FILL..record d[34:377] == f2[1:344]: True; title == f2 title: True; preamble+UPDATE+blank+first-fill Addendum+blank+Addendum 2 d[600:759] == f2[565:724]: True; UPDATE == f2[582]: True
  [chk] [rec] token diff entry block without title (second fill -> this): 5 hunks, 46 tokens out, 79 in
  [chk] [rec]     replace 'is commit 33cd0fca (pending on origin): not on origin/claude/referee at my fetches (head 49d34123), -> "(REFEREE successor 31, 33cd0fca, l. 143-169) tested L-3 with strings of its own (‹strings typed fro
  [chk] [rec]     replace '33cd0fca (pending on origin);' -> '33cd0fca;'
  [chk] [rec]     replace '(33cd0fca, pending on origin) not read.' -> '‹Statements and labels unchanged (§0; §C).› (l. 169).'
  [chk] [rec]     delete 'on L-3, commit' -> ''
  [chk] [rec]     replace '(pending on origin; not on origin/claude/referee at my fetches, head 49d34123), not read.' -> '(33cd0fcaf6c8ce4c88b2f466aec8a20ec09626aa, 2026-11-12T09:18:41Z) l. 143-169, ‹**Line L-3 MATCHES** 
  [chk] [rec] token diff entry block without title (first fill -> this): 67 hunks, 76 tokens out, 1257 in
  [chk] [G-S] L-3 stale grep: {'unlanded': 0, 'not landed': 0, 'when landed': 0, 'pending': 0, 'to land': 0, 'landing': 0, 'landed': 0, 'will ': 0, 'not yet': 0}; ‹CANDIDATE› 1; ‹stays› 2
  [hex] hex ids in the draft: 134; git objects 81; measured sha1s (not objects) 53; named as pending on origin (REFEREE §E, Lead brief): []; neither: 0 []
  [hex]     da3308b5 in the draft: True; git object: False; measured: True
  [hex]     4948ce5d in the draft: True; git object: True; measured: False
  [hex]     4ded1e8d in the draft: True; git object: True; measured: False
  [hex]     2d0344d3 in the draft: True; git object: True; measured: False
  [hex]     33cd0fca in the draft: True; git object: True; measured: True
  [hex] NEGATIVE CONTROL (0badc0de1, 1234abcd9f): neither: 2 ['0badc0de1', '1234abcd9f']
  [sim] trunk 07139249 RESULTS sha1 0ef236b9b7146cd19fcc380c4fcd2a7314aec402 lines 16545 "¦" 1477 ; GAPS sha1 2965fc2ec61b5ddebc529d9ee21c285100914940 lines 23
  [sim] pure insertion: prefix byte-unchanged True ; suffix byte-unchanged True ; inserted lines 224
  [sim] headings after insertion: {'R125': [15595], 'R126': [15726], 'R127': [15903], 'E-1': [16127], 'E-2': [16140], 'E-3': [16168], 'Dead': [16199]}
  [sim] R126 at l. 15726 (unchanged: True); R127 at l. 15903-16125, blank l. 16126 (''), ‹**Erratum E-1**› l. 16127; the line before R127: l. 15902 '' (R126's block ends l. 15901)
  [sim] order R125 < R126 < R127 < E-1 < E-2 < E-3 < Dead ends: True
  [sim] RESULTS lines 16545 -> 16769 (+224) ; "¦" 1477 -> 1477 (unchanged True) ; ‹checker 3333333)› once True ; fill token 0
  [sim] ### R1xx headings: 28, R127 the last: True
  [sim] GAPS: only l. 11 changes True ; lines 23 -> 23 ; l. 11 "¦" 76 -> 76 ; ‹UPDATE 2026-› 61 -> 61 ; R127 last: True ; after R126's (2026-11-12 06:44Z, 7b2fa753): True ; prefix byte-unchanged: True
  [sim] GAPS whole file "¦" 198 -> 198
  [sim] fill values used only here: 2099-01-11 00:00 3333333
