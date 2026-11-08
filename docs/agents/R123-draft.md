# Draft RESULTS R123 (Lead; first fill 2026-11-08T12:15:15Z by date -u (subagent) on P-N5-QUIET line L-2, docs/new/P-N5-QUIET-line-L2.txt, l-new 559cdffc, sha1 fed893462811ea10d0b99622dcbb31f7b50b6d47 (draft sha1 8f361e55); SECOND FILL 2026-11-08T20:39:34Z by date -u (subagent) on P-N5-QUIET line L-4, docs/new/P-N5-QUIET-line-L4.txt, l-new 87603d07, sha1 0809da259cc54e3cec1fdf455070620314d4e622) — to CHECKER C137 — NOT LANDED; goes after R121 (LANDED at 59dacf22) and R122 (LANDED at aaf52291), before Erratum E-1
SECOND FILL (2026-11-08T20:39:34Z by date -u, subagent; for CHECKER C137). Read at the origin heads of one fetch at
2026-11-08T20:28:37Z-20:28:38Z (date -u before and after the fetch; git fetch of claude/l-new, claude/referee, claude/referee-2 and
claude/checker, not of the trunk, whose push by the Lead was running; rc 0; I merged, committed and pushed nothing, wrote nothing into the
repository and built this file in the scratchpad by fill2.py): l-new 91ed2f3f (91ed2f3f3dd1a26eff2e28ef0ecafc888601b012,
2026-11-08T19:48:45Z, «L-NEW 66: box 199 Addendum 2», the branch head; git diff 87603d07 91ed2f3f on docs/new/P-N5-QUIET.md,
docs/new/P-N5-QUIET-fixes.md, the four QUIET line files and experiments/new/box194/: empty), so the objects are those of 87603d07
(87603d07f946a880595dabeff2eef068e3493c72, 2026-11-08T13:19:30Z, «L-NEW 65: P-N5-QUIET fixes entry 4 + L-4 (R-B2); P-N5-CHAIN fixes entry
3 + L-4 (R-G3, R-W, R-B3)», L-NEW successor 65, the commit of record), with fixes entry 3 and L-3 at b61c2029
(b61c202986302b9d07c4bc02c56b0a9a566089bd, 2026-11-08T12:45:13Z, «L-NEW 65: P-N5-QUIET fixes entry 3 + L-3 (R-L, R-U, R-B, R-Q, R-T,
R-G)», successor 65); 559cdffc → b61c2029 → 87603d07 is an ancestor chain and 87603d07 an ancestor of origin/claude/l-new (git merge-base
--is-ancestor). By git, 87603d07 is the commit and 0809da259cc54e3cec1fdf455070620314d4e622 the sha1 of the file
docs/new/P-N5-QUIET-line-L4.txt (its blob is a81ad4aef6e8c5334c311a405ef7f6b7c6da780a); «0809da25» names no git object (D-7). referee
ae980555 (ae9805556a1feee09de9a95d2043607d591374bf, 2026-11-08T16:44:42Z, the branch head): docs/referee/R-P-N5-QUIET.md there is
byte-equal to 3e02e7c3's (3e02e7c33f2b79b06204a86b37421ce4eb593c43, 2026-11-08T13:55:51Z, «REFEREE successor 30: R-P-N5-QUIET §D (L-4
0809da25 MATCHES, after R121) and R-P-N5-CHAIN §E (L-4 a69c8aa9 MATCHES)»; git log names no later commit on it): 284 lines, 23,338 bytes,
sha1 f34e5430089c9935500f4983a752a7d51fd3c487; its first 21,114 bytes (l. 1-264) are 407f4a21's file, by cmp; §D is l. 266-284, with
docs/referee/scratch/quiet_l4.py and scratch/quiet_logs/l4test.out. referee-2 c1e71a25 (c1e71a25596ff01554a1bd7390d7f8b0380a97d6,
2026-11-08T16:43:45Z, the branch head): docs/referee-2/R2-P-N5-QUIET.md there is byte-equal to 96d8a3fd's
(96d8a3fd2e69e994fc9498ecfc255fc01be19dd5, 2026-11-08T13:55:42Z, «REFEREE-2 successor 35: P-N5-QUIET L-3/L-4 MATCH (Add. 4); P-N5-CHAIN
L-4 MATCHES with attribution caveat (Add. 4)»): 429 lines, 38,160 bytes, sha1 c4baf6d8c95b26db836196bd5e6759234bbc51aa; its first 36,563
bytes (l. 1-412) are the file of 09ce14fc (09ce14fc1183615c884a8a96c4468ee2b79280a0, 2026-11-08T12:32:12Z, «REFEREE-2 successor 35:
P-N5-CHAIN L-3 MATCHES (Add. 2); boundary step in (Q5) signed for P-N5-QUIET (Add. 3) and P-N5-CHAIN (Add. 3)»; sha1
e5e2b6a1e8d198b1c78da614fd85021fe59b5b69), and its first 33,659 bytes (l. 1-381) f699a724's, by cmp; Addendum 3 is l. 383-412, Addendum 4
l. 414-429, with R2-P-N5-QUIET/bt_l34.py and bt_l34.out. checker bdfb2d07 (bdfb2d07b5245b23870809b2c40d0d685c7f070a, 2026-11-08T19:21:38Z,
«CHECKER C136 Add. 1 heading date; resume point», the branch head): docs/checker/ ends at C136.md; C137 does not exist; notes/CHECKER.md
l. 7: «Then R123 (P-N5-QUIET), P-N5-END, P-N5-CHAIN.». 3e02e7c3, ae980555, 09ce14fc, 96d8a3fd, c1e71a25 and bdfb2d07 are ancestors of the
local trunk aaf52291; 87603d07, b61c2029 and 91ed2f3f are NOT (git merge-base --is-ancestor; claude/l-new is in the trunk up to 219e3933;
7a0e6175, the next l-new commit, is not). The Lead merges claude/l-new (87603d07 or later) before landing; claude/referee and
claude/referee-2 are already in the trunk.
Trunk: local HEAD aaf52291 (aaf52291295f489f59d6ed2033c07eb4f86e2cc5, 2026-11-08T20:27:48Z, «Lead: land RESULTS R122 (P-ACYC: BETA-ACYC,
ACYC-XI; line L-5) after R121, before Erratum E-1 (CHECKER C136 Add. 1 3e7fe04e PASS); GAPS G-N5-TIME update; NOW counters; owner line +
log 19:19Z-20:27Z», being pushed by the Lead during this fill; the working tree was clean); the trunk's remote-tracking ref, not
re-fetched by me, is dc1b29eb, an ancestor of aaf52291. docs/agents/R123-draft.md at aaf52291 is the first fill, sha1
8f361e5572926ffddda3e6d418b71c7d9685ac88 (committed at 5a2f8bda, 2026-11-08T12:40:07Z; fill2.py asserts it). R121 LANDED at 59dacf22
(2026-11-08T14:06:41Z) and R122 at aaf52291: RESULTS «### R121» l. 14320-14742 and «### R122» l. 14744-15074, each followed by a blank
line; GAPS l. 11 «UPDATE 2026-11-08 14:06Z: RESULTS R121 (P-N5-ASC; CHECKER C135 a9bf46bb)» and «UPDATE 2026-11-08 20:27Z: RESULTS R122
(P-ACYC; CHECKER C136 3e7fe04e)», R122's the last. RESULTS at aaf52291: sha1 2eca04ea9b6301e9120a554d09edf9fc494e0bdd, 15,718 lines, =
RESULTS 66e7119615efa5a0bb25b898e32b5b371c55c122 (the file of the first fill and of both referees' premise checks) with l. 14320-15075
inserted (R121's and R122's blocks with their blank lines) and nothing else (by script); «**Erratum E-1**» l. 15076, «**Erratum E-2**» l.
15089, «**Note E-3**» l. 15117, «## Dead ends (kept;» l. 15148. GAPS at aaf52291: sha1 298be51ec457b87fd93cd2ee3b6ac57570d0bde1, 23 lines,
l. 11 76 "|", 57 «UPDATE 2026-». «R123», «C137», «CN2», «LOC-GATE», «LOC-K2», «B-ONLY», «NO-TIE», «T-QUIET», «ASC-T» and «UP-T» occur 0
times in RESULTS and in GAPS; «P-N5-QUIET» occurs once in RESULTS (R121's «BOX 194 (P-N5-QUIET, separate packet)», l. 14604) and 0 times
in GAPS (by script).
New sources (read in full): fixes entries 3 and 4 (docs/new/P-N5-QUIET-fixes.md l. 112-152 at 87603d07; the file 152 lines, 17,582 bytes,
sha1 cd3581f722d5f803ca9f661042b7e2bbf4d5d6dc; its first 16,292 bytes = b61c2029's file, 140 lines, sha1
9a9ae29cda44dc1ee636dbc94767e06c27497a1e, and its first 11,791 bytes = 559cdffc's file, by cmp); L-3 (b61c2029, the file's only commit;
sha1 d9b5e610300927fd0e8c1ec8567ee1fb68758df7, 5,429 bytes) and L-4 (87603d07, the file's only commit);
experiments/new/box194/mkl3_194.py, mkl4_194.py and quiet.pins at 87603d07 (42 rows: 559cdffc's 38 with the fixes file re-pinned, and L-3,
mkl3_194.py, L-4 and mkl4_194.py added); experiments/new/check.sh l. 1004-1019 at 87603d07 (the blocks «BOX 194 LOC» and «P-N5-QUIET»,
byte-equal to 559cdffc's); REFEREE §D (l. 266-284 at ae980555); REFEREE-2 Addenda 3 and 4 (l. 383-429 at c1e71a25);
docs/agents/LEAD-STATE.md at aaf52291 l. 2858, 2860, 2865, 2871, 2882, 2887, 2888 and 2892 (the R123 rulings and routing, 12:22Z-14:54Z);
RESULTS R121 and R122 as landed (titles; R121's definitions of seq_t(v) and «an ascent of seq_t(v)»); GAPS l. 11 at aaf52291; DECISIONS l.
355-358 (L41); notes/CHECKER.md l. 1-9 at bdfb2d07; the fills of R122 (c9591e35, a1decf9a, 40e6ffb8; the house form of a re-point) and
their tools.
WHAT CHANGED SINCE THE FIRST FILL. The Lead ruled on the first fill (draft 8f361e55) before CHECKER: «Lead rulings: take R-L, R-U, R-B
(entry 2 has tool fixes, not line-only), R-Q, R-T -> L-NEW 65 fixes entry 3 + L-3 (pred a4802f27, 5,225 B); G-7 (REFEREE 28 (Q4) boundary
step) asked to REFEREE 30 (L41 or AC-6 class); (ii) label placement to CHECKER.» (LEAD-STATE l. 2858, 12:22Z); «R123 (Q4) boundary step
reading = (b) referee-originated step the proof needs. Lead ruling: L41 APPLIES -> R-G clause added to QUIET L-3 (L-NEW 65, six changes);
REFEREE-2 35 to sign the step» (l. 2860, 12:25Z); «Lead: entry 3 proof-bearing -> L-4 = L-3 + R-B2 (entries 1-3, successors 62, 64, 65)
before byte tests.» (l. 2865, 12:48Z). REFEREE-2 35 signed REFEREE 28's step in Addendum 3 (09ce14fc, 12:32:12Z): «**SIGN.** No statement
changes, and QUIET's proof is complete with it.» (l. 398-399). L-NEW successor 65 wrote fixes entry 3 + L-3 (b61c2029; L-3 never routed)
and fixes entry 4 + L-4 (87603d07): L-4 = L-2 + R-L, R-U, R-B2, R-Q, R-T, R-G. Both referees MATCH L-4: REFEREE successor 30, «Verdict:
fixes entries 3-4 CORRECT. **Line L-4 MATCHES** the packet read with fixes entries 1-4, provided it lands after R121.» (§D l. 284 at
ae980555); REFEREE-2 successor 35, «Verdict: **L-3 and L-4 MATCH.** Statement verdicts unchanged (all SIGN, with the boundary step
explicit).» (Add. 4 l. 429 at c1e71a25). R121 is landed (59dacf22), so REFEREE's proviso holds. CHECKER has not ruled on R123 (no C137).
Checks run at this fill (scratch /tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad/r123b;
nothing written into the repository). (a) l4rel123b.py: mkl3_194.py's six (key, old, new) tuples and mkl4_194.py's one, read by ast
without executing lane code, = the tables of fixes entries 3 and 4 (l. 117-122, l. 146; R-U's «…» matched as a wildcard between its fixed
ends) (True ×7); R-L, R-U, R-B, R-Q and R-T = the first fill's strings in r123/tools/upd123.py (True ×5); each old string once in L-2
(R-B2's once in L-3); L-2 + R-L, R-U, R-B, R-Q, R-T, R-G = L-3 d9b5e610… (True), L-3 + R-B2 = L-4 (True); L-2 + the first five =
a4802f276d1f9095479696edba78a271955b2f25 (the first fill's prediction). L-4 = 0809da259cc54e3cec1fdf455070620314d4e622, 5,433 bytes, one
line with its newline, 5,320 characters, 906 tokens, 103 «(» / 103 «)», depth never negative, final depth 0, 0 "|", one « — », «to land
first» 0, «referee-originated» once, «signed by both referees» once, «G-N5-TIME stays OPEN» once, «; not M3, not a step-4 pass, not a
TARGET.md claim» once, «so this is not M4» once, «(2026-11-08)» once, «R1xx» 0; R-labels R104, R118, R121, R21, R57 (and R221, L-RED's
report); token diff L-2 → L-4: 11 hunks, 16 tokens out, 68 in, all inside the six changes. mkl3_194.py and mkl4_194.py re-run from a copy
of the git archive of 87603d07 (L-3 and L-4 removed first): rc 0 each, outputs cmp-equal to L-3 and L-4. The packet is 066dfc7d… at
87603d07 and 91ed2f3f (True). (b) The two check.sh blocks (l. 1004-1019 at 87603d07) from a git archive of 87603d07 (experiments, docs,
scripts), 2026-11-08T20:33:31Z-20:36:39Z by date -u, rc 0, output «BOX 194 LOC: LOC-GATE / LOC-K2 / CN2 / OVT-DV / QUIET 0 failures, DEAD
constant IN-BOUND (RS2_L32M6 IN 33) = frozen: PASS» and «P-N5-QUIET: packet and 42 pinned files match quiet.pins: PASS». (c) upd123b.py:
the first fill's UPDATE d[554] (a6f09325fd6d7e2409ef30078f27bc38aee20028, the sha1 of the line without newline) with L-4's six changes in
their UPDATE forms, each old string once in it: sha1 739c5f7142fada0a55bb24b9d7627c9a348918d8 without newline
(1798910000d1d78bdf69684ec9f3871ef7a91329 with it), 5,465 bytes, 5,354 characters, 905 tokens, 103 «(» / 103 «)», 0 "|", one each of the
three fill tokens, «2026-11-08» 0 times, « — » 0 times; cross-checked by a standalone re-implementation of run123()'s direct build (R118's
procedure): on L-2 with the first fill's G-U reading it gives d[554] (True, the control), on L-2 without it an AssertionError (as in the
first fill), on L-4 without a reading the same 739c5f71… (True), on L-4 with the old reading an AssertionError (the status list it dropped
is gone). Token diff L-4 → UPDATE: 17 hunks, 58 tokens out, 57 in (the head; the nine labels behind their clauses, UP-T's after the
premises parenthesis in place of « (2026-11-08) —»; R-L's «;»; the drop words; «65)» → «65). G-N5-TIME stays open.»). On GAPS l. 11 at
aaf52291 the draft UPDATEs of R121 (e975c303…, at 5a2f8bda) and R122 (79319350…, at 40e6ffb8) occur once each, filled with «2026-11-08»,
«14:06» / «20:27» and «a9bf46bb» / «3e7fe04e», R122's last (True); R123's filled UPDATE appended after it keeps 76 "|", R123's last, the
prefix byte-unchanged (True). (d) chk123b.py (title, block, UPDATE, pipes, the fill token, parentheses, stale grep, quote sweep),
lp123b.py (line-precise quotes new at this fill), sim123b.py (landing simulation on aaf52291), rec123b.py (the kept sections
byte-unchanged) and hex123b.py (every hex id new at this fill is a git object or a sha1 measured at this fill): Addendum 2.
The first fill's flags, resolved in L-4 (string checks by script, l4rel123b.py): G-L by R-L («to land first» 0 in L-4). G-U (i) by R-U:
L-4 ends its scope words «… is not M4, so this is not M4; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim
(P-N5-QUIET, …», so R118's procedure applies with no reading (c). G-U (ii), the UP-T label after the premises parenthesis: unchanged, for
CHECKER («(ii) label placement to CHECKER», the Lead's 12:22Z ruling). G-1 by R-B, then R-B2: L-4's note «(P-N5-QUIET,
docs/new/P-N5-QUIET.md with its fixes entries 1-3, docs/new/P-N5-QUIET-fixes.md; L-NEW successors 62, 64 and 65)». G-2 (ii) by R-Q and
R-T. G-7 by R-G, under L41: «the step β_g ∉ Π(y) for boundary targets y in (Q5)'s F4′ (else E(y) ⊇ S, against y's class) is
referee-originated (REFEREE R-P-N5-QUIET §3 (Q4), l. 118-120, REFEREE 28), signed by both referees» once in L-4, before «DATA, clause by
clause»; the wording is the Lead's, not the first fill's sketch (fixes l. 128-131), and REFEREE-2 signed the step before L-3 was written
(Add. 3, 12:32:12Z; b61c2029, 12:45:13Z), as the first fill's G-7 asked. G-4 (ii) and the G-9 notes: not ruled; unchanged at L-4 (no
premise, signed clause or DATA figure changes; R-T changes T-QUIET's unit words only), restated below.
NOTES at this fill (for CHECKER; no line change proposed):
- N-T, T-QUIET's COUNTER (REFEREE-2's optional note; the first fill's G-9 (ii)). REFEREE-2 Add. 4: «Optional: add «the Σ_v form is not
  counted», as in P-N5-CHAIN's R-2, since the line states T-QUIET in the Σ-form.» (l. 426-427); the Lead: «Optional R-T note not taken.»
  (LEAD-STATE l. 2888). L-4's unit «runs with T_CYC > Q + (Q + 1)L, Q the number of loud steps» is what quiet194.py tests (the first
  fill's G-9); the entry's Honest limits (v) says that the Σ_v form is not counted. CHECKER may rule whether the line must say it.
- N-L41, THE ELEMENTS OF L41 AT L-4 (DECISIONS l. 355-358). The author referee signs the step in its report (REFEREE 28, §3 (Q4) l.
  118-120: «It holds.»); the other referee checks and signs it (REFEREE-2 35, Add. 3 l. 394-399, re-derived, «**SIGN.**»); both signatures
  and the joint gap map are quoted in the entry (Claims signed; L41 and L43); the scope tail says the step is referee-originated (R-G).
  REFEREE-2 was asked by the Lead with REFEREE 28's sentence quoted (Add. 3 l. 384-385); its first report's (Q5) did not state the step
  («**No, not explicitly.**», l. 400). The rule is met in my reading; CHECKER rules.
- N-G4, THE FIRST FILL'S G-4 (ii), RESTATED (unchanged at L-4). L-4 still says «QUIET, T-QUIET, B-ONLY and NO-TIE use neither [E-LEV] nor
  R121»; B-ONLY's proof uses E-DOM and QUIET's (F-cls) E-MON's argument, both consequences of R104's priorities re-derived by both
  referees (first fill, G-4 (ii)). R121 is now landed before R123, so no landing-order question remains; the wording is CHECKER's call.
- N-R, REFEREE §D's R-L NOTE: «CORRECT only as a landing-time sentence. At trunk bef76cf4 (fetched at writing) R121 is NOT yet in RESULTS»
  (l. 281). At aaf52291 R121 is RESULTS l. 14320, and R123 lands after it.
- D-6, STAMPS (history, no verdict affected). Fixes entry 3 names «Lead 12:21Z» and «12:25Z» in its heading (l. 112) and «12:24Z (R-G,
  Lead reading L41)» in its Source line (l. 113-114); LEAD-STATE logs the rulings under 12:22Z and 12:25Z (l. 2858, 2860); REFEREE §D says
  «as the Lead ruled (12:24Z, L41)» (l. 275-276). Fixes entry 4 names «Lead 12:47Z» (l. 142); LEAD-STATE logs it under 12:48Z (l. 2865).
  REFEREE-2 Add. 3's heading reads «2026-11-08 12:21Z by date -u» (l. 383) while its first bullet answers «Lead 12:25Z» (l. 384); its
  commit is 12:32:12Z. Both referees name the L-4 routing «Lead 13:54Z» (REFEREE §D l. 267; REFEREE-2 Add. 4 l. 415); LEAD-STATE logs it
  under 13:55Z (l. 2882).
- D-7, THE BRIEF'S SHAs. The brief for this fill gave 0809da25 as the l-new commit and 87603d07 as the start of the file's sha1; by git
  output it is the other way round: 87603d07 is the l-new commit and 0809da25… the sha1 of the line file (git cat-file -t 0809da25: «Not a
  valid object name»). The entry uses git's reading.
- D-8, REFEREE-2 Add. 3 cites REFEREE 28's step at «claude/referee 407f4a21 l. 118-120» (l. 384); the step was first committed at
  6ae1fc04, and l. 1-222 of REFEREE's file are the same at 6ae1fc04, 407f4a21 and ae980555 (by cmp), so L-4's «l. 118-120» holds at each.
Changes at this fill, and nothing else: line 1 (the header: the first fill's draft sha1, the SECOND FILL clause, R121 and R122 now
LANDED); this section (new); the title (L-4: the six changes); in the entry: Object (successors 62-65; the packet at 87603d07; four fixes
entries; L-4 the line of record; line history L-1 to L-4; the L-4 rounds, REFEREE §D and REFEREE-2 Addenda 3 and 4), Claims signed (the
new rounds; the joint gap map with the boundary step; the six changes read CORRECT), Setting (entries 1-4) and (f) and (h), The RESULTS
line (L-4; R-Q, R-G, R-T, R-U, R-B2), Premise (R121 LANDED; RESULTS at aaf52291), L41 and L43 (the Lead's ruling, REFEREE-2's signature,
L-4's sentence, both referees' readings of it), Fixes (header, two new sub-bullets for entries 3 and 4, closing bullet), Honest limits
(v), (viii) and a new (x), Data (87603d07; this fill's re-run; REFEREE 30's pins check), Signatures (§D, Addenda 3 and 4; successor 65's
commits), INDEPENDENCE (L-4's strings and byte tests), TARGET.md diff (L-4); the GAPS preamble and the UPDATE (rebuilt from L-4 with no
reading); Addendum 2 (new, at the end). The FIRST FILL record (from "FIRST FILL (this text)" to (14)) and the first fill's Addendum
(1)-(10) are kept byte-unchanged (rec123b.py): where they call L-2 the title or the line of record, raise G-L, G-U, G-1, G-2 (ii), G-7 as
flags, propose R-L, R-U, R-B, R-Q, R-T or an R-G sketch, or give their line numbers, counts, slices and UPDATE sha1 (a6f09325…), they
describe draft 8f361e55 at 12:17Z; the Lead ruled from 12:22Z, and the entry block now follows L-4.
FIRST FILL (this text). Read at the origin heads of one git fetch at 2026-11-08T11:52:48Z by date -u (date -u before and after it:
11:52:48Z both; claude/l-new, claude/referee, claude/referee-2, claude/checker, claude/vibrant-johnson-nxvvxo; rc 0; I merged, committed
and pushed nothing and edited docs/agents/R123-draft.md only): l-new 2f4167cd (2f4167cd6c87b3ca3c41144ff33765536f9ddb4a,
2026-11-08T10:52:09Z, «L-NEW 65: P-N5-ASC fixes entry 6 + L-6 (CHECKER C135 Add. 1 R6); box 197 (ASC-WIT, ASC-ROOT, RE-COUNT, RE-EQUIV;
DS-order DATA)», the branch head; git diff 559cdffc 2f4167cd on docs/new/P-N5-QUIET.md, docs/new/P-N5-QUIET-fixes.md, the two QUIET line
files and experiments/new/box194/: empty), so the objects are those of 559cdffc (559cdffcc46001c6a7e023522a8e5518448ddd7a,
2026-11-08T06:59:11Z, «L-NEW P-N5-QUIET fixes entry 2 (REFEREE 28 QT-L1..QT-L6 + REFEREE-2 33 Addendum 1; D-1, D-2 by tool fix, re-run all
0) + line L-2 (sha1 fed89346 = prediction, 5131 B); Form B DATA only; quiet.pins 38 rows», L-NEW successor 64, the commit of record); the
packet freeze 9329859d (9329859d59b53b36eadb70e1399cbc06cce2a633, 2026-11-08T00:14:29Z, L-NEW successor 62), fixes entry 1 d9c49489
(d9c49489cef17fd829ea33d7b1e60c126dcab93e, 2026-11-08T01:08:08Z, successor 62) and line L-1 df0d2a25
(df0d2a25d6950fba0ce9fc81ab180fd75c88bf42, 2026-11-08T02:23:15Z, «L-NEW P-N5-QUIET line L-1 by script (fixes entry 1 applied: B-ONLY +
NO-TIE, Gamma3 scope sentence verbatim, [OPT] as R57 (b)); quiet.pins 35 rows», successor 63). 9329859d → d9c49489 → df0d2a25 → 559cdffc
is an ancestor chain, and 559cdffc is an ancestor of origin/claude/l-new (git merge-base --is-ancestor). referee 4434597c
(4434597c947e8bca85792c10d49a1069b9a795ac, 2026-11-08T10:54:53Z, «REFEREE successor 30: R-P-N5-CHAIN §C (L-2 e481d260 MATCHES), R-P-N5-END
§D (L-3 d6afe92a MATCHES); asc_l6.py prepared», the branch head): docs/referee/R-P-N5-QUIET.md there is byte-equal to 407f4a21's
(407f4a2158f2570dc98a2c865ae30b9cef88575c, 2026-11-08T08:09:56Z, «REFEREE 29: R-P-N5-QUIET §C (L-2 fed89346 MATCHES; D-1/D-2 tool fixes
checked; Form B replay EQUAL); R-P-N5-END §C (L-2 e8a8ac51 MATCHES LN-1..LN-8); notebook»): 264 lines, 21,114 bytes, sha1
6ee1a57163421e79aad76ed2a535bc07ee3cbdac; by cmp its first 17,974 bytes (l. 1-222) are the report as first committed at 6ae1fc04
(6ae1fc0425916503194ae5e3270886d972929dee, 2026-11-08T03:11:05Z, «REFEREE 28: R-P-N5-QUIET first review (all SIGN; ASC-T/UP-T conditional
on R121; L-1 NOT YET: QT-L1..QT-L6)»; 222 lines, sha1 ae0aa9b069164a359e2f82f047302c7f9e16d62a), byte-equal at a233f356
(a233f35606c28b5e8168cb21a9b83b8b23342e9c, 03:11:09Z, «REFEREE 28: notebook time fix (03:11Z by date -u)», which changes notes/REFEREE.md
only). referee-2 0e5c7c37 (0e5c7c37b567320d97621914b462c17d94cbfb53, 2026-11-08T11:05:52Z, the branch head):
docs/referee-2/R2-P-N5-QUIET.md there is byte-equal to f699a724's (f699a7245ccb46f8b82d9e3b155b8727c115a7a7, 2026-11-08T08:12:19Z,
«REFEREE-2 R2-P-N5-QUIET Addendum 2: L-2 fed89346 MATCHES (byte test; D-1, D-2 tool fixes verified on archive); HANDOVER successor 33»):
381 lines, 33,659 bytes, sha1 2a868e3c7a3c5379d880860b805738aea73a4551; by cmp its first 30,584 bytes (l. 1-343) are 11a7a911's file
(11a7a911a5b988939d58b943148710383542c29d, 06:14:50Z, Add. 1; sha1 007f1abf1d481e6369c46f9892f49a502d516514) and its first 26,910 bytes
(l. 1-308) are 17a85958's (17a859580549209b508c8f84ccfb7bb85770db17, 05:49:41Z, the report; sha1
2cdf6d8c4a66c22d82503d5b3a5d93dd306d5915). checker 9ee82f6a (9ee82f6aafed5077ff47fb29b663a8caf362d0aa, 2026-11-08T10:05:25Z, «CHECKER
successor 22: resume point (C135 Add. 1 FAIL E-5, R6)», the branch head; docs/checker/ ends at C135.md; C136 and C137 do not exist; «C137»
0 and «P-N5-QUIET» 0 times in notes/CHECKER.md). 407f4a21 is an ancestor of origin/claude/referee and f699a724 of origin/claude/referee-2;
9329859d and d9c49489 are ancestors of origin trunk fdc0f1e9; df0d2a25, 559cdffc, 6ae1fc04, a233f356, 407f4a21, 17a85958, 11a7a911 and
f699a724 are NOT (git merge-base --is-ancestor). The Lead merges claude/l-new, claude/referee and claude/referee-2 before landing. Second
fetch at 2026-11-08T12:05:26Z by date -u (same five branches; rc 0): referee 6c8d6956 (6c8d6956d500be70211100a1557da6f42e091a35,
11:26:43Z, «REFEREE successor 30: R-P-N5-ASC §H (L-6 a23c61d3 MATCHES = L-5 + R6; HL-1 optional)»), referee-2 762e98fd
(762e98fde9a77166bef9b87bcb69572852c09e9b, 11:36:02Z, «REFEREE-2 successor 35: P-N5-ASC L-6 byte test (Add. 7: MATCHES, R6 read against
packet §2)»); l-new 2f4167cd, checker 9ee82f6a and origin trunk fdc0f1e9 unchanged. git diff --quiet 407f4a21 6c8d6956 on
docs/referee/R-P-N5-QUIET.md, f699a724 762e98fd on docs/referee-2/R2-P-N5-QUIET.md and docs/referee-2/R2-P-N5-QUIET/, 559cdffc 2f4167cd on
the QUIET files and box194: equal. So every object of this fill is unchanged at the second fetch.
Trunk: origin trunk fdc0f1e9 (fdc0f1e9cff20275b6e7c2c20b4e61a0ddfcd8a5, 2026-11-08T11:14:47Z, «Lead: L-RED 60 roster/restart; L-SI 46 +
L-RED 60 checks 5/5; log 10:33Z-11:16Z + resume point (R121 L-6 path; CHAIN L-2 / END L-3 at byte tests; BOX 197 RE-EQUIV; OSC-ROOM)»),
the local HEAD at the first fetch; the local HEAD is now 567a53f3 (567a53f3df9297e6b6a141e007378185308fc8b3, 2026-11-08T12:03:02Z, «Lead:
R121 fourth fill on P-N5-ASC L-6 (c9fb8f5b; <R2-A7> pending REFEREE-2 Add. 7); log 11:16Z-12:02Z (L-6 MATCHES both; CHAIN R-1/R-2/R-4; C10
W0-R UNSAT t 7 f5)», committed during this fill; it changes docs/agents/LEAD-STATE.md and docs/agents/R121-draft.md only; RESULTS, GAPS
and R122-draft.md equal at both, git diff --quiet). RESULTS: sha1 66e7119615efa5a0bb25b898e32b5b371c55c122, 14,962 lines; «### R104» l.
9864, «### R118» l. 13607, «### R119» l. 13879, «### R120» l. 14114-14318, «**Erratum E-1**» l. 14320, «**Erratum E-2**» l. 14333, «**Note
E-3**» l. 14361, «## Dead ends (kept;» l. 14392. GAPS: sha1 2a41c7654d4e9dedee7abc8591dfb792633bc2c9, 23 lines, l. 11 76 "|", 55 «UPDATE
2026-», the last R120's «UPDATE 2026-11-07 21:05Z: RESULTS R120 (P-TOWER-FUEL; CHECKER C134 0c816917)». R121 and R122 are NOT landed
(«R121», «R122» 0 times as RESULTS headings and in GAPS UPDATEs); R121-draft.md is the fourth fill
(c9fb8f5b1412587bb2850d80d17f6265b1c39aba at 567a53f3; origin trunk's copy is the third fill 1fa73568), R122-draft.md the second fill
(2cd7cfd03c58c01653d665c657a2ff71826e2df3, at both). «R123», «C137», «P-N5-QUIET», «CN2», «LOC-GATE», «LOC-K2», «B-ONLY», «NO-TIE»,
«QUIET», «T-QUIET», «ASC-T», «UP-T», «[E-LEV]», «[OPT]» occur 0 times in RESULTS and in GAPS.
Sources read: the packet docs/new/P-N5-QUIET.md (frozen 9329859d, unchanged at d9c49489, df0d2a25, 559cdffc and 2f4167cd; sha1
066dfc7d5a03b983a126ffc6866a13046b5e9724, 199 lines, 20,022 bytes; read in full); docs/new/P-N5-QUIET-fixes.md at 559cdffc (sha1
e86e6dd86a55b3adf9fc11185cc65409fcc5f5fa, 110 lines, 11,791 bytes; read in full; by cmp its first 6,775 bytes are entry 1's file at
d9c49489, sha1 cf4dcfd0d1b61dfbfd2261fe78f22c0a71218203, 66 lines, and its first 7,721 bytes the file at df0d2a25 with the «Line L-1»
note, sha1 5f903276380e8dd01d3f0267d8a2945ba3b90615, 75 lines); line L-1 docs/new/P-N5-QUIET-line-L1.txt (df0d2a25; sha1
62de90753d764c99f9b10e6f201d155f8b4ec79c, 4,600 bytes); L-2 docs/new/P-N5-QUIET-line-L2.txt (559cdffc, the file's only commit; sha1
fed893462811ea10d0b99622dcbb31f7b50b6d47, 5,131 bytes, one line with its newline); experiments/new/box194 at 559cdffc: check194.sh,
quiet.pins (38 rows), loc194.py, quiet194.py, bonly194.py, mkl2_194.py (read in full), check194.out, formB194.out; the check.sh blocks
«BOX 194 LOC» and «P-N5-QUIET» (experiments/new/check.sh l. 1004-1019 at 559cdffc); REFEREE's file at 6ae1fc04 and 407f4a21 (read in full;
its scratch tools listed, not re-run); REFEREE-2's file at 17a85958, 11a7a911 and f699a724 (read in full; its tools listed, not re-run);
RESULTS R104 (l. 9864; (vi) at l. 10083-10086), R118 (l. 13607; its (a)-(e) at l. 13677-13692), R21 (a) (l. 933), and the landed titles of
R118-R120; the frozen P-N5-XICYC.md l. 75 (trunk, sha1 149e2414be657ba12472faa4f46d5a251f2d3e98) and P-N5-REALIZE.md l. 88 (trunk, sha1
067f06b6c67969adf346621b4a92b253491ab2b9); R121's lines L-5 (e28e962d, fe4d3f90) and L-6 (2f4167cd, docs/new/P-N5-ASC-line-L6.txt, sha1
a23c61d384036ce3fa771e27e175a8dbf2331658, 5,449 bytes; read in full) and P-N5-ASC.md l. 66-72 (E-MON's proof); GAPS l. 11; DECISIONS l.
355-374 (L41, L42, L43) and DECISIONS-INDEX l. 34, 36; docs/checker/C132.md-C135.md at 9ee82f6a (read: verdicts, E-items, G-U and N-S
rulings) and notes/CHECKER.md l. 1-20; docs/agents/LEAD-STATE.md (grep: P-N5-QUIET, R123, C137); docs/agents/R122-draft.md and the first
fills of R121 and R122 (b83443b6, c9591e35; the house form) and their tools (r121/tools/upd121.py, r122/tools/upd122.py,
r122b/tools/upd122b.py, chk122b.py, sim122b.py).
Checks run at this fill (scratch /tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad/r123;
nothing written into the repository but this file). (a) The check.sh blocks «BOX 194 LOC» and «P-N5-QUIET» (experiments/new/check.sh l.
1004-1019 at 559cdffc, unchanged) run from a git archive of 559cdffc (experiments, docs, scripts), 2026-11-08T11:57:15Z-12:00:20Z, rc 0,
output «BOX 194 LOC: LOC-GATE / LOC-K2 / CN2 / OVT-DV / QUIET 0 failures, DEAD constant IN-BOUND (RS2_L32M6 IN 33) = frozen: PASS» and
«P-N5-QUIET: packet and 38 pinned files match quiet.pins: PASS» (the first re-runs check194.sh and diffs it against check194.out, and
greps the failure counters; the second checks the 38 pins). (b) mkl2_194.py from a copy of that archive: «QT-L1..QT-L6 old once each,
applied; sha1 fed893462811ea10d0b99622dcbb31f7b50b6d47 5131 bytes», output cmp-equal to L-2. (c) A shape script on L-2. (d) DATA, clause
by clause, against loc194.py, quiet194.py, bonly194.py and check194.out (G-9). (e) upd123.py: the UPDATE with the controls R97-R120
(landed), R121 (fourth fill, not landed) and R122 (second fill, not landed) (Addendum (8)). (f) chk123.py (title, block, UPDATE, quote
sweep, stale grep) and sim123.py (landing simulation): Addendum.
LESSONS APPLIED (R121's and R122's lists, plus C135 Add. 1). C113 E-1 / C123 E-1 / C133 E-1: the title is L-2 verbatim, nothing inserted
and nothing stripped; L-2 has no «R1xx» and no ledger tag before its claims (CLEAN). C133 E-3 / C134 E-3: the scope tail carries the
landed status words once (G-U: FLAG, L-2 has «not M3, not M4, not a step-4 pass, not a TARGET.md claim»). C120-C135 / C134 E-4: EVERY DATA
clause tested against the code of its counter for unit, set and scope (G-9). C122 G-0: parentheses balanced (96 / 96). C122 E-3 / C132 E-2
/ C133 E-2 / C134 E-1 / C135 E-1 with C134 N-S and C135 Add. 1 N-S: the source note names the authors of proof-bearing text (G-1: note,
CHECKER's call). C132 E-7 / C133 E-6 / C134 E-2 / C135 E-2: a referee-originated proof step is named in the scope tail (L41; G-7: FLAG for
the Lead). C117 E-1 / E-2 / C135 E-3: no READING inside a signed clause (G-2: CLEAN). C135 E-4 / C135 Add. 1 E-5: every term of a signed
clause defined in the line or landed (G-2 (ii): note on seq_t(v) and «ascent»). C118 E-1 / C132 E-1: no status word that goes stale at
landing (G-L: FLAG, «to land first»). C115 E-1: premises checked against RESULTS, landed entries only, and R121 against its line of record
(G-4). C116 G-2: name clashes (G-6). C116 G-3: pins (G-12). C119 E-1: every «referee X did Y» checked against that referee's file. C130
G-P / C133 G-P: the UPDATE builder carries a control for every UPDATE that lands before this one (R97-R120 landed; R121 and R122 not
landed, controlled against their drafts and C135 Add. 1). C132 Add. 1: block re-run times as a date -u interval.
FLAGS FIRST (G-L and G-U make CHECKER FAIL as L-2 stands by the C118 E-1 / C132 E-1 and C133 E-3 / C134 E-3 precedents; G-7 needs the
Lead's L41 ruling, and if it is L41's case CHECKER FAIL as it stands by C132 E-7 / C133 E-6 / C134 E-2 / C135 E-2, with a REFEREE-2 check
still to be made; G-1, G-2 (ii), G-4 (ii) and G-9 are CHECKER's rulings, with optional strings). Exact replacements R-L and R-U (and
optional R-B, R-Q, R-T), each old string once in L-2, by script (upd123.py Part O): L-2 + R-L + R-U: sha1
e13a80f645791f5a1500ba98819d9cfbf180137a with its newline, 5,127 bytes, 96 «(» / 96 «)», 0 "|", one « — »; its UPDATE by R118's procedure
with no reading cab24ad0969cfd3d7eab95411ce6daa451e31338 (5,159 bytes). With R-B as well: 13de74bea165da410a991189a50bab3429b8f4c6 (5,143
bytes), UPDATE c467443b3fa374e967d1bbbd9db7af2054d210d9 (5,175 bytes). With R-B, R-Q and R-T as well:
a4802f276d1f9095479696edba78a271955b2f25 (5,225 bytes, 97 / 97), UPDATE 499acfb6eef2c1e18b5b2dc569c239c49aad752d (5,257 bytes). No R-G
line is built (G-7).
- G-L, STALE STATUS (FLAG; the C118 E-1 / C132 E-1 class; CHECKER FAIL as it stands). ASC-T's clause ends «with F′_B of RESULTS R121
  (P-N5-ASC, to land first);». C132 E-1 ruled on «not landed» in R118's label: «R117 has landed (ac1bc37c), so «not landed» goes stale at
  R118's landing». R123 lands only after R121 (G-P), so «to land first» is stale at R123's landing. Proposed R-L: "with F′_B of RESULTS
  R121 (P-N5-ASC, to land first);" → "with F′_B of RESULTS R121 (P-N5-ASC);". Old string once in L-2; in the UPDATE its form without the
  «;» ("with F′_B of RESULTS R121 (P-N5-ASC, to land first)" → "with F′_B of RESULTS R121 (P-N5-ASC)") occurs once (the label move puts
  «(Corollary ASC-T);» after it). It changes no statement; the dependence on R121 stays in the premises («for ASC-T and UP-T only, RESULTS
  R121's HUB-ASC-G whole-run form and UP-B»).
- G-U, THE STATUS WORDS AND THE UPDATE PROCEDURE (FLAG; the C133 E-3 / C134 E-3 class; CHECKER FAIL as it stands in my reading). L-2's
  tail ends «; G-N5-TIME stays OPEN; TARGET.md §2 (M4) asks for an algorithm polynomial on every parity game and §4 says a bound on a
  restricted class is not M4: not M3, not M4, not a step-4 pass, not a TARGET.md claim (P-N5-QUIET, …». C134 E-3: «every landed line
  R90-R119 except R112 reads «not M3, not a step-4 pass, not a TARGET.md claim»», and the procedure «as written it applies only with a
  reading». L-2 has the landed words neither as one string nor after «G-N5-TIME stays OPEN» («not M3, not M4, not a step-4 pass, not a
  TARGET.md claim»: the inserted «not M4»). R118's procedure (run122()'s drops, R121's and R122's) asserts «; not M3, not a step-4 pass,
  not a TARGET.md claim» once and fails on L-2 (upd123.py: AssertionError). The draft's UPDATE is therefore built with ONE READING: «;
  G-N5-TIME stays OPEN» dropped as landed, and the status list «: not M3, not M4, not a step-4 pass, not a TARGET.md claim» dropped in its
  place, so that «… is not M4» ends the scope words (Addendum (8)). Proposed R-U (the meaning kept: the TARGET sentence stays as scope
  words, «not M4» once, the landed words once, after «G-N5-TIME stays OPEN»): "; G-N5-TIME stays OPEN; TARGET.md §2 (M4) asks for an
  algorithm polynomial on every parity game and §4 says a bound on a restricted class is not M4: not M3, not M4, not a step-4 pass, not a
  TARGET.md claim (P-N5-QUIET" → "; TARGET.md §2 (M4) asks for an algorithm polynomial on every parity game and §4 says a bound on a
  restricted class is not M4, so this is not M4; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim (P-N5-QUIET". Old
  string once in L-2. With R-U, R118's procedure applies with no reading (only R123's date, start, labels and source prefix in place), and
  the UPDATE is the draft's UPDATE with «is not M4 (P-N5-QUIET» → «is not M4, so this is not M4 (P-N5-QUIET» (True, by script). Both
  referees' TARGET diffs carry «not M4» (REFEREE §7 l. 216: «§4: a restricted class is not M4.»; REFEREE-2 l. 293: «§4 bullet 1
  («Polynomial only on a restricted class») applies, so it is not M4.»). (ii) THE LAST LABEL. L-2's premises parenthesis stands after the
  last clause and before the date (« B fixed (premises: …; QUIET, T-QUIET, B-ONLY and NO-TIE use neither [E-LEV] nor R121) (2026-11-08) —
  »), a position no landed line R97-R122 has (R118 and R121 have their premises before the claims). build() takes the last clause to the
  date, so the UP-T label goes after the premises parenthesis: «… nor R121) (Corollary UP-T, under HYPOTHESIS [E-LEV]: lev(x) < lev(x′)
  implies pr(e_(x,k)) < pr(e_(x′,k′))): this bounds T_CYC only, …». That is the procedure unchanged, and it is the draft's UPDATE. The
  other placement (label before « (premises: ») gives 5a9f3be6540a6ed85c161c2a9c73d68c00096f30 (5,155 bytes; upd123L2_alt.txt). CHECKER
  rules on (i) and (ii).
- G-7, L41: A REFEREE-WRITTEN STEP IN QUIET's LOWER BOUND (FLAG for the Lead's ruling; the C132 E-7 / C133 E-6 / C134 E-2 / C135 E-2
  class). The packet's Bellman-Ford step (Q5) applies F4′ at the face of a path and says «the face is in neither Π, by (Q4)'s argument and
  simplicity» (l. 155-156). REFEREE's §3 (Q4) adds a step for the boundary value: «A boundary W-target y in class (w, S ∖ {e}) never has a
  C-vertex β in Π(y). If y's play passed β_g ∈ C, then E(y) ⊇ E(β_g) = S, which is impossible. I add this, because the Bellman-Ford step's
  F4′ at a β-face needs it for the BOUNDARY value too, not only along the simple path. It holds.» (l. 118-120), and uses it in (Q5) («F4′
  at x, g (CN2) and at the face (not in Π of the next mover's value, since a cycle vertex is never in Π; not in the path value, by
  simplicity and the boundary remark above)», l. 126-128). REFEREE signs QUIET (l. 14, «SIGN. As frozen, the (Q5) tie case was a gap (G-1,
  «flips at most twice … to a tie»). NO-TIE closes it, and the stated L stays valid») and does not call the boundary point a gap.
  REFEREE-2's re-derivation of the same step reads «The face is in neither Π: not on the simple sub-path, and not in Π(z) by (Q4)'s
  argument.» (l. 130-131); it does not state the boundary case, and its Addendum 1 (l. 310-343) does not compare it. No fixes entry
  restates the step. In my reading the step is needed: the path value from the next mover contains Π of the boundary value, and neither
  simplicity nor (Q4)'s β_g ∉ Π(z) sentence (l. 141-142, about z, the β-face's own successor) excludes a C β-face there. If the Lead rules
  L41's case (a referee-originated step of record): L41 needs «the OTHER referee independently checks and signs it» (DECISIONS l. 357),
  which REFEREE-2's file does not show, so REFEREE-2 checks the step, and the line's scope tail names it, e.g. R-G (built only after that
  signature): "; no separate DATA for ASC-T and UP-T (R121's UP-B / HUB-ASC-G plus T-QUIET); G-N5-TIME stays OPEN" → "; no separate DATA
  for ASC-T and UP-T (R121's UP-B / HUB-ASC-G plus T-QUIET); the step of QUIET's lower bound that no β-face of a B-class C lies in Π of a
  boundary W-target's value (E(y) ⊇ E(β_g) = S otherwise) is referee-originated (REFEREE R-P-N5-QUIET §3 (Q4)), signed by both referees;
  G-N5-TIME stays OPEN" (old string once in L-2; with R-U the old string's tail is «… T-QUIET); TARGET.md §2 …», and R-G goes after «plus
  T-QUIET)» with «; TARGET.md §2» as its new tail). If the Lead reads the packet's «(Q4)'s argument» as covering it (the R122 G-7 (ii) /
  AC-6 class: «G-7 (ii) AC-6 NOT L41», LEAD-STATE l. 2754 at c9591e35), no line change. (ii) Not L41's case in my reading: QT-L1 ([OPT]'s
  source, REFEREE's string, REFEREE-2's W-2 found independently) and QT-L2 (F2 in the premise list, REFEREE's) are premise citations, not
  proof steps; B-ONLY is L-RED's lemma (adversary lane, «credit: L-RED R221 §3; proof re-derived here», fixes l. 8), re-derived by L-NEW
  and credited in the line, signed by both referees.
- G-1, SOURCE NOTE (note for CHECKER; the C122 E-3 / C132 E-2 / C133 E-2 / C134 E-1 / C135 E-1 class; CLEAN by the N-S rulings in my
  reading). L-2's last parenthesis is «(P-N5-QUIET, docs/new/P-N5-QUIET.md with fixes entry 1, docs/new/P-N5-QUIET-fixes.md; L-NEW
  successor 62)». Entry 1 is L-NEW successor 62's («## Fixes entry 1 (L-NEW successor 62; Lead 00:36Z: L-RED 56 R221 items 1-2 and the
  [OPT] reading)», fixes l. 3) and carries proof text (B-ONLY's and NO-TIE's proofs, l. 11-29; the (Q5) / (Q3) consequences, l. 30-35):
  named. The «Line L-1» note (successor 63, l. 68-75) is line-only. Entry 2 (successor 64, «## Fixes entry 2 (L-NEW successor 64; …», l.
  77) carries no proof: QT-L1..QT-L6 are line strings (it withdraws entry 1's [OPT] paragraph, l. 86-88, and G-2's «governs», l. 91-94),
  and D-1, D-2 are tool fixes («No line string.», l. 99, l. 101). C135 Add. 1 N-S: «Entries 3-5 (successors 63, 64) are line-only: they
  carry no proof … C134 N-S applies: the note names the authors of proof-bearing text.» So L-2's note meets N-S. But C134 E-1 and C135 E-1
  also counted DATA units («the measured I-ROOM unit», «the unit counts») as text the line rests on, and the line's «wfail 0 (unit: quiet
  windows)», «Tfail … T > Q + (Q + 1)L» and «k2fail 0 (unit: states …)» are true of the tools only after entry 2's D-1 and D-2 (fixes l.
  96-101). Optional R-B (CHECKER's call): "(P-N5-QUIET, docs/new/P-N5-QUIET.md with fixes entry 1, docs/new/P-N5-QUIET-fixes.md; L-NEW
  successor 62)" → "(P-N5-QUIET, docs/new/P-N5-QUIET.md with its fixes entries 1-2, docs/new/P-N5-QUIET-fixes.md; L-NEW successors 62 and
  64)". Old string once in L-2 and once in the UPDATE.
- G-2, SIGNED CLAUSES (the C117 E-1 / E-2 / C135 E-3 class): CLEAN. Each labelled clause is its statement (packet §2-§5, fixes entry 1) in
  the same or a narrower form: CN2 (l. 80-81), B-ONLY (fixes l. 11-12, without its gloss «(it is a β-vertex, K1, K2 or the unused loop)»),
  NO-TIE (fixes l. 26), LOC-GATE in its strict form (l. 89-90 with NO-TIE), LOC-K2 (l. 113), QUIET (l. 119-122 definitions, l. 130),
  T-QUIET (l. 131, the second inequality only), ASC-T (l. 170-171), UP-T (l. 165-166). No READING is inside a clause; the Γ3 sentence and
  the OPEN sentence follow « (2026-11-08) — ». (ii) SYMBOLS (the C135 E-4 / C135 Add. 1 E-5 class; note). Landed or defined in L-2:
  IDEAL-CYC(G), Howard steps, T_CYC (R118 (a), restated in L-2's head); genome, Γ(G), movers, gates, c_W, K1, K2, the e- and β-faces
  (R104; «e_g», «β_g» read as gate g's W-face e and Ξ-face β of R104's «Odd gates of priority 1 with a W-face e and a Ξ-face β»); Λ_t,
  Π_t, Ω_t, σ̄_t, ⊴, ◁ (R118, [VJ]); class_t(v), E_t(v), loud, quiet, L, n, D^tot_E(v) (L-2); U(G) (L-2, «the number of options whose
  Ξ-target has a higher level»); [E-LEV] (stated inline); F′_B («of RESULTS R121»). NOT defined in L-2: «seq_t(v)» and «ascent» in ASC-T's
  hypothesis «if every seq_t(v) has at most B ascents for every vertex v». C135 E-4 failed R121's L-2 on exactly these words («L-2 defines
  neither seq_t(v) nor «ascent»»); R121's L-6 now defines them («with seq_t(v) the e-vertices in Π_t(v) in play order, E_t(v) their set,
  an ascent of seq_t(v) a step to a more relevant element,»), so they are landed notation when R123 lands (the C124 G-9 (vii) route), but
  L-2 does not say whose they are. Optional R-Q: "(Corollary ASC-T) if every seq_t(v) has at most B ascents for every vertex v," →
  "(Corollary ASC-T) with seq_t(v) and its ascents as in RESULTS R121, if every seq_t(v) has at most B ascents for every vertex v,". In
  DATA and scope words (not signed clauses): «Q» in «Tfail 0 (unit: runs with T > Q + (Q + 1)L; same set as QUIET)» and «T» in «T bounds
  IDEAL-CYC iterations only» are not defined in L-2 (packet l. 9, l. 120); optional R-T: "T-QUIET: Tfail 0 (unit: runs with T > Q + (Q +
  1)L; same set as QUIET)" → "T-QUIET: Tfail 0 (unit: runs with T_CYC > Q + (Q + 1)L, Q the number of loud steps; same set as QUIET)". R-Q
  and R-T: old string once in L-2 each; R-T's old string once in the UPDATE, R-Q's clause part («if every seq_t(v) has at most B ascents
  for every vertex v,») once.
- G-4, PREMISES (the C115 E-1 class). R-labels in L-2: «R118» ×6, «R104» ×5, «R121» ×4, «R21», «R57» (and «R221» ×2, L-RED's report, «R22»
  inside the instance name cR_d2_w8_R22). Landed: ### R104 l. 9864, ### R118 l. 13607 (its (a) l. 13677, (b) l. 13682 «Facts F1-F6 (§3 l.
  68-83) with F4 REPLACED by F4′», (c) l. 13686 DOM and STRICT, (e) l. 13691 «C ≤ n·(2M + 2).»), R21 (a) l. 933 («(Odd's best reply σ̄_k
  is pointwise optimal in G_{σ_k})», verbatim), R57 (b) (cited as «not used»); R118's DATA for «a run that can differ from the IDEAL-CYC
  run at exact VJ ties» (R118's line: «each of the other 29 diverges first at an exact VJ tie»). The frozen P-N5-XICYC l. 75 («σ̄_t is
  optimal at every vertex at once ([VJ])», verbatim, inside R118 (b)'s incorporated «(§3 l. 68-83)») and P-N5-REALIZE l. 88 (the
  e-priorities by «(lev(owner), gate index)», l. 88-89). NOT landed: R121 (P-N5-ASC), premise of ASC-T and UP-T only («for ASC-T and UP-T
  only, RESULTS R121's HUB-ASC-G whole-run form and UP-B»). Checked against R121's line of record L-6 (a23c61d3; the fourth fill's title):
  «over the whole run the number D_E(v) of distinct (Λ_t(v), E_t(v)) is at most (2M + 3)·F′_B(M)» and «under [E-LEV] every seq_t(v) has at
  most U(G) ascents» occur once each, as REFEREE quoted them from L-2 (§2 l. 67-69), and F′_B is defined there («F′_B(M) = (M² + 3M + 1)(1
  + M·F′_(B−1)(M)²)»); D_E(v) = D^tot_E(v) by both definitions (REFEREE l. 70, REFEREE-2 l. 143). R123 lands only after R121 (G-P). Both
  referees checked every premise quote by script (REFEREE §2 l. 39-48, quiet_quotes.py; REFEREE-2 l. 38-43, r2qq.py, «Missing: 0.»)
  against RESULTS sha1 66e71196…, the RESULTS of this fill. [E-LEV]: a HYPOTHESIS at both referees and in L-2 (QT-L3). (ii) NOTE
  (CHECKER's call; no change in my reading): L-2 says «QUIET, T-QUIET, B-ONLY and NO-TIE use neither [E-LEV] nor R121», while B-ONLY's
  proof uses E-DOM («E-DOM: only e-vertices, c_W, K0, K3 are more relevant than an e-vertex», fixes l. 20) and QUIET's (F-cls) uses
  «E-MON's proof, P-N5-ASC §3» (packet l. 124), both arguments in R121's packet. Neither is an R121 statement: E-DOM is a consequence of
  R104's priorities (packet l. 46-47; P-N5-ASC l. 70: «by [DEF]»), and both referees re-derived (F-cls) from [DEF], [VJ] and LOC-K2
  (REFEREE l. 105-113, «The packet's «below the common K0, K3» is this argument in short form. Correct.»; REFEREE-2 l. 115-117). And R123
  lands after R121 in any case.
- G-9, DATA, CLAUSE BY CLAUSE (the C120-C135 rule: unit, set and the statement's scope of every count, against the counter code it names;
  every signed clause matched to a count or a no-DATA entry). Every figure is in check194.out and reproduced by my re-run of the block
  ((a) above: it diffs the run against check194.out). Counter code at 559cdffc: loc194.py l. 13-44 (analyse) and l. 46-55; quiet194.py l.
  13-36 and l. 40-48; bonly194.py l. 9-23 and l. 26-34.
  - Set S and scope. «scope IDEAL-CYC, box191 idealcyc via box192 rpot192»: each tool calls rpot192.states(G). «1,000 random genomes
    rand191.rgen seed 2, d 1-6, w 1-3, degree 2-3»: rgen(rng, rng.randint(1, 6), rng.randint(1, 3), rng.randint(2, 3)) in each tool's rand
    mode (rgen's third argument D is the largest degree, deg = rng.randint(2, D)). «the 13 P-N5-ASC instances»: box193/inst/*.json (8) and
    box192/inst/ cR_d2_w8_R22, rd2_d9, rd2_d10, rd3_d7, rf_d5 (check194.sh). MATCH. NOTE (i): «L-RED's rd3_d4 and RS2_L32M6 and LEAP_k64»:
    RS2_L32M6 was generated by L-RED's rs2.py, not frozen by L-RED (check194.sh l. 3-5; REFEREE-2 l. 209: «loose but harmless»).
  - CN2 «cnlow 0 (unit: (state, vertex) pairs under (σ_t, σ̄_t); other positional pairs: no separate DATA; same runs)»: loc194.py l. 20,
    h.prio of the value's cycle node < 2, per state and vertex. MATCH. The «so no gate or mover is … in a set Π» half follows from the
    definition of Π (no counter; not a separate statement).
  - LOC-GATE «locfail 0 in 149,859 (gate, state) pairs»: l. 26-31: per gate and state, a tie is counted apart, else E.key of the chosen
    face ≠ the smaller key; 66,950 (LEAP_k64) + 380 (rd3_d4) + 13,980 (the 13 instances: 2,871 + 1,380 + 2,261 + 1,206 + 330 + 936 + 938 +
    184 + 800 + 792 + 1,080 + 962 + 240) + 68,549 (random) = 149,859, ties 0 on every line. MATCH.
  - LOC-K2 «k2fail 0 (unit: states; same runs)»: l. 21, «sb[k2] != k1 or not E.key(vs[k1]) < E.key(vs[k2])», both conjuncts (D-2). MATCH.
  - B-ONLY «bonlyfail 0 in 297,192 (state, vertex) pairs»: bonly194.py l. 11-19, v not in {c_W} ∪ {e : s0[e] = c_W}, fail E.rank[Λ] ≥ emin
    (Λ at least as relevant as the least relevant e-vertex); 1,273 + 17,430 + 42,355 + 236,134 = 297,192. NO-TIE «ties 0 in 89,125 (state,
    gate) pairs»: l. 20-22, E.key equality of the two faces; 380 + 6,216 + 13,980 + 68,549 = 89,125. MATCH (sets as stated: rd3_d4,
    RS2_L32M6, the 13, random; LEAP_k64 not in B-ONLY's set, RS2_L32M6 not in LOC-GATE's).
  - QUIET «wfail 0 (unit: quiet windows) and crossflip 0 (unit: σ̄ flips on quiet steps at gates whose faces are in different classes),
    longest window W ≤ N on every run»: quiet194.py l. 19 L = (M+1)(2M+1)(N+1) + N(n−1) (D-1), l. 24-28 (a window's step counter cur;
    wfail once when cur == L + 1, i.e. once per window longer than L), l. 29-32 (crossflip: a σ̄ change at g on a quiet step with the
    faces in different classes at both states; on a quiet step the classes do not change, so this is the line's unit); W per run (l. 27).
    Set: rd3_d4, RS2_L32M6, box193's 8, rd2_d9, rd2_d10 (check194.sh), and random: «10 of the 13 instances (all but cR_d2_w8_R22, rd3_d7,
    rf_d5)». MATCH; W ≤ N on all 12 lines (rd3_d4 2 / 8 … RS2_L32M6 32 / 77, RS2_L8M6 8 / 29), random «maxWoverN 1.0». n = h.n = N + 3M +
    6 on every line (rd3_d4 8 + 60 + 6 = 74).
  - T-QUIET «Tfail 0 (unit: runs with T > Q + (Q + 1)L; same set as QUIET)»: l. 35. MATCH as worded. NOTE (ii): the counter tests T ≤ Q +
    (Q + 1)L, the packet's first inequality; the clause's bound follows with Q ≤ Σ_v (D^tot_E(v) − 1), which no lane counter tests on the
    random set (sumDE is printed for the 12 named runs only, and sumDE ≥ Q on each: rd3_d4 488 ≥ 15, … rd2_d10 1,433 ≥ 21); REFEREE-2's
    own counter «Q > Σ(D − 1)» is 0 (l. 192), referee data. The counter is stronger than the clause given that fact, not weaker.
  - ASC-T, UP-T: «no separate DATA … (R121's UP-B / HUB-ASC-G plus T-QUIET)». No-DATA entries. CLEAN.
  - Form B (formB194.out, the three instances outside QUIET's set: wfail 0, Tfail 0, crossflip 0) is DATA only and not in the line (fixes
    l. 103-107); REFEREE §C l. 250-253 and REFEREE-2 Add. 2 l. 369-373 replayed it EQUAL.
- G-6, NAMES (by script on RESULTS 66e71196 / GAPS 2a41c765). 0 times in RESULTS and GAPS: «R123», «C137», «P-N5-QUIET», «CN2»,
  «LOC-GATE», «LOC-K2», «B-ONLY», «NO-TIE», «QUIET», «T-QUIET», «ASC-T», «UP-T», «D^tot_E», «class_t», «box194». R121's line names
  HUB-ASC(B), HUB-ASC-G, UP-JUMP, UP-B, NOUP, E-MON, CHAIN-DECOMP, SKELETON; no R123 label equals one of them.
- G-P, PLACEMENT (Lead). R121 (C135 Add. 2) and R122 (C136) are routed before R123 («R123 (P-N5-QUIET) first fill subagent launched (C137
  after R121, R122).», LEAD-STATE l. 2848 at 567a53f3). R123's block goes after R122's block, before «**Erratum E-1**», and its UPDATE
  after R122's on GAPS l. 11. Simulated with R121's and R122's draft entries in place, and without (sim123.py): Addendum (7).
- G-0, THE CHECKER NUMBER. docs/checker/ on claude/checker (9ee82f6a) ends at C135.md; C136 is R122's (R122-draft.md line 1); «C137»
  occurs 0 times in RESULTS, GAPS, DECISIONS-INDEX, NOW and notes/CHECKER.md, and once in LEAD-STATE at 567a53f3, the Lead's routing of
  this fill (G-P). This draft uses C137 (title fill, UPDATE head, GAPS preamble), as the brief says.
- G-5, ERRATA (note). E-1 (R97-R100 counts), E-2 (R105's CHAIN-BACK, RANK_t, KEYFLIP) and Note E-3 (R110's SC-ISO) do not bear on R104's
  definitions, R118 (a)-(e), R21 (a) or R57 (b).
- G-8, SCOPE AND TARGET (note). L-2's «this bounds T_CYC only, in one restricted model; for Σ_v D^tot_E(v) with U(G) unbounded and
  unboundedly many ascents nothing is claimed (OPEN)» and the Γ3 sentence (QT-L4) equal packet Scope l. 14-23 and §9 in meaning, as
  restated by both referees (REFEREE §4, §7; REFEREE-2 Γ3 section and TARGET.md diff). No statement mentions a parity game's winning
  region or an algorithm's running time; T_CYC is the length of one restricted run (TARGET.md §4: «Polynomial only on a restricted class
  …»).
- G-10, LEAD RULINGS AND READINGS. L-2 cites no Lead reading («Lead reading» 0, «L4» 0 in L-2). Two Lead readings of the packet's history
  were not accepted by the referees and are gone from L-2: 23:54Z ([E-LEV] as R104's order; REFEREE l. 19 «The Lead's incorporation path
  is not accepted»; REFEREE-2 l. 70) and 00:36Z ([OPT] as R57 (b); REFEREE l. 18, REFEREE-2 l. 59: «I do not accept the Lead reading
  00:36Z as the source»). The Lead's 06:39Z routing («L-2 = L-1 + QT-L1..QT-L6 exactly … D-1 and D-2 BY TOOL FIX», fixes l. 77) is what
  entry 2 did.
- G-11, STALE WORDS. L-2: «to land first» once (G-L); «pending», «not landed», «NOT YET», «will » 0 each. «G-N5-TIME stays OPEN» and
  «(OPEN)» are dated by the line's «(2026-11-08)», the packet's freeze date (9329859d, 00:14:29Z).
- G-12, PINS (the C116 G-3 class): CLEAN. quiet.pins (38 rows) pins the packet, the fixes file, L-1, L-2, mkl1_194.py, mkl2_194.py, every
  tool and instance the line cites, check194.sh, check194.out and formB194.out; the «P-N5-QUIET» block re-ran it (PASS, (a)).
- G-13, THE REFEREES' ROUNDS: (3), (4). D-items: (11).
- G-14, THE FIXES FILE (note). Entry 1 (successor 62): G-1 (R221 §3) closed by B-ONLY and NO-TIE, G-2 (R221 §7) the Γ3 sentence, the [OPT]
  reading, DATA added (bonly194.py); the «Line L-1» note (successor 63; the 10-of-13 correction); entry 2 (successor 64): QT-L1..QT-L6,
  D-1, D-2, line L-2, Form B. L-1 + QT-L1..QT-L6 = L-2 (mkl2_194.py, (b)).
- G-N, NOVELTY (note). No outside source beyond R118's landed premise (VJ00 §4.2 / Friedmann arXiv 1106.0778 §3, which REFEREE-2 opened,
  l. 49-53); the entry makes no literature claim.
- CLEAN AT L-2 (by script on fed89346): C113 E-1 / C123 E-1 / C133 E-1 (L-2 starts «In IDEAL-CYC(G) (RESULTS R118 (a):», «R1xx» 0); C122
  G-0 (96 / 96, depth never negative, final 0); C114 Add. 1 E-1 (<DATE>); C116 G-2 (G-6); C116 G-3 (G-12); C117 E-1 / C135 E-3 (G-2); the
  DATA clauses (G-9, notes only); «|»: 0 in L-2, 0 in the entry block, 0 in the UPDATE (Addendum). NOT CLEAN: C118 E-1 / C132 E-1 (G-L);
  C133 E-3 / C134 E-3 (G-U); for the Lead: L41 (G-7); for CHECKER: G-1, G-2 (ii), G-4 (ii), G-U (ii).
- (L-2 SHAPE, by script) L-2 is one line: 5,131 bytes and 5,027 characters with its newline, 96 «(» / 96 «)», depth never negative, final
  depth 0, 0 "|", one « — », «R1xx» 0, «(DATA: » 0, «(DATA, » 0, «DATA, clause by clause» once, two guillemet quotes (QT-L1's),
  «(2026-11-08)» once, «referee» 0, «REFEREE» 0.
(0) PLACEMENT. RESULTS at origin trunk fdc0f1e9 (= local HEAD 567a53f3's): sha1 66e7119615efa5a0bb25b898e32b5b371c55c122, 14,962 lines;
  "### R123" 0 times in RESULTS and GAPS. PROPOSED (R102's to R122's layout): insert R123's entry, with one blank line after it, directly
  before «**Erratum E-1**», after the blank line that follows R122's block (G-P). Simulation: Addendum (7).
(1) TITLE. The title is the line file docs/new/P-N5-QUIET-line-L2.txt (l-new 559cdffc, 2026-11-08T06:59:11Z, the file's only commit, sha1
  fed893462811ea10d0b99622dcbb31f7b50b6d47, 5,131 bytes with the newline; byte-equal at the l-new head 2f4167cd), verbatim: NOTHING is
  stripped and NOTHING is inserted: "### R123 [refereed-only] ", then the file without its newline, then ", CHECKER PASS
  (docs/checker/C137.md, checker PENDING)" (as R90-R122). Built by script and re-checked after writing (chk123.py): equal.
(2) LINE HISTORY: two lines. L-1 62de9075 (df0d2a25; 4,600 bytes, 85 «(» / 85 «)»; written by mkl1_194.py with fixes entry 1 applied;
  REFEREE «NOT YET: QT-L1 to QT-L6 required» (l. 22); REFEREE-2 «NOT YET» (l. 32: W-1, W-2, W-3, D-1, D-2), then Add. 1 withdrew W-1..W-3
  for QT-L4, QT-L1, QT-L3 (l. 342) and kept D-1, D-2 «either fix is enough» (l. 336)). L-2 fed89346 (559cdffc, fixes entry 2; 5,131 bytes,
  96 / 96): L-1 with QT-L1..QT-L6, each old string once in L-1, no overlap (mkl2_194.py; REFEREE §C l. 230-234, quiet_linefix.py;
  REFEREE-2 Add. 2 l. 351-353, bt_l2.py), with D-1 and D-2 made in the tools; both referees MATCH.
(3) THE LINE AT BOTH REFEREES. REFEREE: report 6ae1fc04 (= a233f356; successor 28; L-1 NOT YET, l. 22), §C 407f4a21 (successor 29; L-2
  MATCHES, l. 262). REFEREE-2: report 17a85958 (successor 33; L-1 NOT YET, l. 32), Add. 1 11a7a911 (comparison; the merged string set),
  Add. 2 f699a724 (L-2 MATCHES, l. 378).
(4) CLAIMS SIGNED = the statement rows of both verdict tables (REFEREE l. 9-17; REFEREE-2 l. 23-31): CN2, LOC-GATE, LOC-K2, B-ONLY,
  NO-TIE, QUIET, T-QUIET SIGN at both from the first round (QUIET's frozen (Q5) tie case a gap closed by entry 1's NO-TIE at REFEREE,
  «closes the tie case of (Q5)» at REFEREE-2); ASC-T SIGN with R121 as premise; UP-T SIGN under HYPOTHESIS [E-LEV] with R121 as premise.
  Not signed: §6 (READING), §7-§9 (DATA, machine checks, TARGET diff), Form B.
(5) OTHER TEXTS THE ENTRY DEPENDS ON: RESULTS R104 (definitions), R118 (a), (b) F1-F4′, (c) DOM and STRICT, (e), [VJ]; R21 (a); R121's
  HUB-ASC-G whole-run form and UP-B (ASC-T and UP-T only); the frozen P-N5-XICYC l. 75 and P-N5-REALIZE l. 88 as cited; the box 194 tools
  and instances (L-NEW 62-64, L-RED's instances).
(6) PREMISE LABELS: G-4.
(7) SYMBOL TEST: G-2 (ii).
(8) FIXES AND STATUS NOTES: G-14; body Fixes.
(9) GAPS: G-N5-TIME (GAPS l. 11) stays open; L-2 states no CONJECTURE and kills no statement («P-N5-QUIET», «T-QUIET» 0 times in GAPS). A
  line-11 UPDATE is proposed at the end, BUILT FROM L-2 AS IT STANDS with the G-U reading (upd123.py: r122b/tools/upd122b.py exec'd
  unchanged but for its one file write; its controls R97-R120 as landed True ×24 and its R121 / R122 controls; then the R121 fourth-fill
  and R122 second-fill controls; then R123 (G-U)).
(10) DATA of record = packet §7 with fixes entries 1-2 (DATA added; D-1, D-2; Form B), NOT signed; L-2's DATA states its counts (G-9).
  Re-run (a): PASS.
(11) Discrepancies, recorded for CHECKER, no verdict affected: D-1 fixes entry 2 (l. 78) and mkl2_194.py (l. 4) cite REFEREE 28's report
  at «claude/referee a233f356»; the report was committed at 6ae1fc04 (03:11:05Z) and a233f356 (03:11:09Z) changes notes/REFEREE.md only
  (the file is byte-equal at both). D-2 REFEREE-2's verdict row for ASC-T says «premise P-N5-ASC = R121 (L-4 MATCHES, my R2-P-N5-ASC Add.
  5)» (l. 30), and REFEREE's checks the forms against «P-N5-ASC's L-2» (§2 l. 65-66); R121's line of record is now L-6 (fourth fill), and
  the two quoted forms are in L-6 verbatim (G-4). D-3 the packet's §1 [ASC] reads «P-N5-ASC (docs/new/P-N5-ASC.md, frozen, with fixes
  entry 1 and line L-1), to land as RESULTS R121 BEFORE this packet» (l. 68) and its Scope cites P-ACYC's ACYC-XI as «not landed» (l. 23):
  packet history, not in L-2. D-4 REFEREE §C's heading «date -u at writing 2026-11-08T07:51Z» and REFEREE-2 Add. 2's «2026-11-08 07:50Z by
  date -u» precede their commits (08:09:56Z, 08:12:19Z), as writing times do. D-5 L-2's set list calls RS2_L32M6 «L-RED's» (G-9 (i)).
(12) Excluded: box 194's OVT-DV and IN-BOUND material (loc194.py's intervals / flips / ovtfail / efail / bfail counters, in194.py, «DEAD
  constant IN-BOUND»: check194.sh runs them, the line cites none but «not used: … OVT-DV, IN-BOUND»), the packet's §6 READING, the
  draft_entry2/ folder (fixes l. 108: «history only»), box 196 (P-N5-CHAIN, a separate packet), REFEREE-2's Γ3 data (r2quiet_gamma3.out,
  r2quiet_T3cmp.out, r2bestset.out) and own random set (referee data). Not part of this entry.
(13) Commits: lane (claude/l-new): 9329859d (2026-11-08T00:14:29Z; packet FROZEN, quiet.pins, the «P-N5-QUIET» block; L-NEW successor 62),
  d9c49489 (01:08:08Z; fixes entry 1, bonly194.py; successor 62), df0d2a25 (02:23:15Z; L-1, mkl1_194.py; successor 63), 559cdffc
  (06:59:11Z; fixes entry 2, L-2, mkl2_194.py, formB194.out, the D-1 / D-2 tool fixes; successor 64); box 194 itself e9993378
  (2026-11-07T22:57:48Z). REFEREE: 6ae1fc04 (= a233f356) → 407f4a21. REFEREE-2: 17a85958 → 11a7a911 → f699a724. CHECKER: docs/checker/
  ends at C135.
(14) DEAD-ENDS ROWS: NONE (no statement killed; the packet's (Q5) tie gap was closed by NO-TIE, a proof fix, not a dead end).

### R123 [refereed-only] In IDEAL-CYC(G) (RESULTS R118 (a): Γ(G) with every non-mover Even vertex frozen at R104's start, Odd unrestricted, Howard steps at the movers), for every genome G: (Lemma CN2) the cycle node of every play under every positional pair has priority ≥ 2, so no gate or mover is a cycle node or in a set Π; (Lemma B-ONLY, credit L-RED R221 §3, re-derived in fixes entry 1) at every state t and every vertex v other than c_W and the e-vertices whose successor is c_W, Λ_t(v) is less relevant than every e-vertex; (Corollary NO-TIE) at every state and gate g, Ω_t(e_g) ≠ Ω_t(β_g); (Lemma LOC-GATE) at every state t and gate g, Odd's optimal counterstrategy σ̄_t chooses the face of strictly ⊴-smaller value; (Lemma LOC-K2) σ̄_t(K2) = K1 and Ω_t(K1) ◁ Ω_t(K2) at every state; (Theorem QUIET) with class_t(v) := (Λ_t(v), E_t(v)), E_t(v) the e-vertices of Π_t(v), a step loud if some vertex changes class and quiet otherwise, every maximal window of quiet steps has at most L := (M + 1)(2M + 1)(N + 1) + N(n − 1) steps, n = N + 3M + 6; (Corollary T-QUIET) T_CYC ≤ (1 + Σ_v (D^tot_E(v) − 1))·(L + 1), D^tot_E(v) the number of distinct classes of v over the run; (Corollary ASC-T) with seq_t(v) and its ascents as in RESULTS R121, if every seq_t(v) has at most B ascents for every vertex v, T_CYC ≤ (1 + n·((2M + 3)·F′_B(M) − 1))·(L + 1) with F′_B of RESULTS R121 (P-N5-ASC); (Corollary UP-T, under HYPOTHESIS [E-LEV]: lev(x) < lev(x′) implies pr(e_(x,k)) < pr(e_(x′,k′))) the same bound with B = U(G), the number of options whose Ξ-target has a higher level, so T_CYC is polynomial in N + M for genomes with U(G) ≤ B, B fixed (premises: RESULTS R104's definitions of the genome and of Γ(G) only; RESULTS R118 (a), (b) F1, F2, F3 and F4′'s stated clause, (c) DOM and STRICT, (e); VJ00 §4.2 / Friedmann arXiv 1106.0778 §3 for the value (Λ, Π, k) and its order ⊴; [OPT] (σ̄_t is optimal at every vertex at once against σ_t) = RESULTS R118's σ̄, Odd's optimal counterstrategy for the order ⊴, as used in R118 (b) (F3's proof in the frozen P-N5-XICYC §3, l. 75: «σ̄_t is optimal at every vertex at once ([VJ])»), and RESULTS R21 (a) («(Odd's best reply σ̄_k is pointwise optimal in G_{σ_k})»); RESULTS R57 (b) concerns the output of SPEC's S1 procedure and is not used; for ASC-T and UP-T only, RESULTS R121's HUB-ASC-G whole-run form and UP-B; [E-LEV] is a hypothesis (the e-priorities of R104's packet §3.1, docs/red/P-N5-REALIZE.md l. 88, satisfy it, but R104 (vi) leaves them to that packet as immaterial to its own results, so R104's line does not fix them); not used: [LOC], OVT-DV, IN-BOUND, F4 as printed, F5, F6, any L-RED lane lemma; QUIET, T-QUIET, B-ONLY and NO-TIE use neither [E-LEV] nor R121) (2026-11-08) — this bounds T_CYC only, in one restricted model; for Σ_v D^tot_E(v) with U(G) unbounded and unboundedly many ascents nothing is claimed (OPEN); T bounds IDEAL-CYC iterations only; nothing is proved on Γ3: by RESULTS R118 (k) and (l), under REACH3-CYC's premises, N5′-xi from S3 on Γ3(G) makes Howard steps on Γ3 up to its first fallback, a run that can differ from the IDEAL-CYC run at exact VJ ties (R118's DATA), and a Γ3 form of this proof (not given here) would bound N5′-xi only up to its first fallback; nothing is claimed about post-fallback iterations, N5′-xi's total count, N5 or general games (witnesses that the restriction is needed: L-RED R221 §7 DIV_2_493, DIV_2_583, DIV_3_717, claude/l-red d49b9f0c, experiments/red/r221q/inst/SHA1SUMS, where N5′-xi on Γ3 changes movers after its first fallback); the step β_g ∉ Π(y) for boundary targets y in (Q5)'s F4′ (else E(y) ⊇ S, against y's class) is referee-originated (REFEREE R-P-N5-QUIET §3 (Q4), l. 118-120, REFEREE 28), signed by both referees; DATA, clause by clause (scope IDEAL-CYC, box191 idealcyc via box192 rpot192; tools in experiments/new/box194/, run by check194.sh; set S: L-RED's rd3_d4 and RS2_L32M6 and LEAP_k64 (box194/inst/), the 13 P-N5-ASC instances, 1,000 random genomes rand191.rgen seed 2, d 1-6, w 1-3, degree 2-3): LOC-GATE: locfail 0 in 149,859 (gate, state) pairs (LEAP_k64, rd3_d4, the 13 instances, the 1,000 random genomes; loc194.py); LOC-K2: k2fail 0 (unit: states; same runs); CN2: cnlow 0 (unit: (state, vertex) pairs under (σ_t, σ̄_t); other positional pairs: no separate DATA; same runs); B-ONLY: bonlyfail 0 in 297,192 (state, vertex) pairs, NO-TIE: ties 0 in 89,125 (state, gate) pairs (rd3_d4, RS2_L32M6, the 13 instances, the 1,000 random genomes; bonly194.py); QUIET: wfail 0 (unit: quiet windows) and crossflip 0 (unit: σ̄ flips on quiet steps at gates whose faces are in different classes), longest window W ≤ N on every run (max W/N 1.0 on the 1,000 random genomes; quiet194.py; rd3_d4, RS2_L32M6, 10 of the 13 instances (all but cR_d2_w8_R22, rd3_d7, rf_d5), the 1,000 random genomes); T-QUIET: Tfail 0 (unit: runs with T_CYC > Q + (Q + 1)L, Q the number of loud steps; same set as QUIET); no separate DATA for ASC-T and UP-T (R121's UP-B / HUB-ASC-G plus T-QUIET); TARGET.md §2 (M4) asks for an algorithm polynomial on every parity game and §4 says a bound on a restricted class is not M4, so this is not M4; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim (P-N5-QUIET, docs/new/P-N5-QUIET.md with its fixes entries 1-3, docs/new/P-N5-QUIET-fixes.md; L-NEW successors 62, 64 and 65), CHECKER PASS (docs/checker/C137.md, checker PENDING)
- Object (L-NEW successors 62-65, D1 / D14 / D18, box 194; frozen, unchanged during review): packet P-N5-QUIET, docs/new/P-N5-QUIET.md,
  sha1 066dfc7d5a03b983a126ffc6866a13046b5e9724, 199 lines, 20,022 bytes (l-new 9329859d, 2026-11-08T00:14:29Z, the file's only commit;
  identical at d9c49489, df0d2a25, 559cdffc, 2f4167cd, b61c2029, 87603d07 and 91ed2f3f, the l-new head; pinned in
  experiments/new/box194/quiet.pins). Both referees measured it (REFEREE l. 27 «docs/new/P-N5-QUIET.md: sha1
  066dfc7d5a03b983a126ffc6866a13046b5e9724, 20,022 B (EQUAL to the brief, and equal at 9329859d).»; REFEREE-2 l. 9 «Packet
  docs/new/P-N5-QUIET.md at 9329859d: sha1 066dfc7d5a03b983a126ffc6866a13046b5e9724, 20,022 B (= the brief).»). Labels (l. 5): «PROVED
  (L-NEW 62, unrefereed) / HYPOTHESIS (stated in the statement) / DATA / READING (not to sign).». To sign (l. 26-35): §2 Lemma CN2; §3
  Lemmas LOC-GATE and LOC-K2; §4 Theorem QUIET and Corollary T-QUIET; §5 Corollary UP-T («under HYPOTHESIS [E-LEV]; premise P-N5-ASC (R121
  when landed)») and Corollary ASC-T; §6 READING; §7-§9 DATA / READING. The packet's own scope (l. 6): «This packet is NOT a TARGET.md
  claim, NOT M3 and NOT M4. It does not decide G-N5-TIME. N5′-xi stays a CANDIDATE.».
  Fixes: docs/new/P-N5-QUIET-fixes.md, append-only, four entries (87603d07: 152 lines, 17,582 bytes, sha1
  cd3581f722d5f803ca9f661042b7e2bbf4d5d6dc, unchanged at 91ed2f3f; its first 16,292 bytes are the file at b61c2029, 140 lines, sha1
  9a9ae29cda44dc1ee636dbc94767e06c27497a1e, and its first 11,791 bytes the file at 559cdffc, 110 lines, sha1
  e86e6dd86a55b3adf9fc11185cc65409fcc5f5fa; its first 7,721 bytes are the file at df0d2a25 and its first 6,775 bytes entry 1's file at
  d9c49489, by cmp). Entry 1 (d9c49489, L-NEW successor 62, l. 3-66): G-1 (L-RED R221 §3, the (Q5) tie case) closed by Lemma B-ONLY
  («credit: L-RED R221 §3; proof re-derived here», l. 8) and Corollary NO-TIE, with their proofs (l. 11-29) and the consequences for (Q5)
  and (Q3) («no statement changes», l. 30-35); G-2 (R221 §7) the Γ3 sentence (l. 39-48); the [OPT] source (l. 50-55); DATA added,
  bonly194.py (l. 57-61). The «Line L-1» note (L-NEW successor 63, l. 68-75): L-1 by mkl1_194.py; «QUIET / T-QUIET ran on 10 of the 13
  P-N5-ASC instances (all but cR_d2_w8_R22, rd3_d7, rf_d5), not on all 13; the line says so. No statement changes.» (l. 73-74). Entry 2
  (559cdffc, L-NEW successor 64, l. 77-110): QT-L1..QT-L6 (line strings; QT-L1 withdraws entry 1's [OPT] paragraph, l. 86-88; QT-L4
  withdraws G-2's «governs», l. 91-94), D-1 and D-2 by tool fix («No line string.», l. 99, l. 101), line L-2, Form B (DATA only, l.
  105-107). «The packet is unchanged; where entry 1 and this entry differ, this entry governs.» (l. 82-83). Entry 3 (b61c2029, L-NEW
  successor 65, l. 112-140): «line strings + one referee-originated proof step (R-G)» (l. 112), R-L, R-U, R-B, R-Q and R-T («No statement
  or DATA number changes», l. 114) and R-G with its «R-G repair (proof step; credit REFEREE 28, found again by REFEREE 30)» (l. 123-127),
  line L-3 (l. 135-140). Entry 4 (87603d07, successor 65, l. 142-152): R-B2 (l. 146) and line L-4 (l. 148-151); «Entry 4 is line-only (no
  tool or proof change), so it is not named (C134 N-S).» (l. 147). Entry 1 carries the proofs of B-ONLY and NO-TIE and the repaired (Q5)
  count; entry 2 carries no proof (it carries the D-1 / D-2 tool fixes); entry 3 carries the boundary step of (Q5), REFEREE 28's (L41);
  entry 4 carries no proof.
  The RESULTS line is L-4, 0809da259cc54e3cec1fdf455070620314d4e622 (docs/new/P-N5-QUIET-line-L4.txt, l-new 87603d07,
  2026-11-08T13:19:30Z, the file's only commit; 5,433 bytes). The title is L-4 verbatim, with nothing inserted and nothing stripped (its
  date parenthesis «(2026-11-08)», its scope tail and its source note are the line's own). L-4's parentheses balance (103 «(» / 103 «)»).
  Line history: L-1 (62de90753d764c99f9b10e6f201d155f8b4ec79c, 4,600 bytes, df0d2a25, fixes entry 1 applied by mkl1_194.py); L-2
  (fed89346, 559cdffc, fixes entry 2: L-1 with QT-L1..QT-L6, each old string once in L-1, no overlap, by mkl2_194.py, which asserts L-1's
  sha1 and the predicted sha1; strings «copied verbatim from REFEREE 28's quiet_linefix.py», fixes l. 84). L-1: REFEREE «NOT YET: QT-L1 to
  QT-L6 required» (l. 22); REFEREE-2 «NOT YET» with «W-1 (Γ3 over-claim), W-2 ([OPT] source), W-3 ([E-LEV] reading), D-1, D-2 (DATA rule);
  strings below» (l. 32), then «My W-1..W-3 strings are withdrawn in favour of QT-L4, QT-L1 and QT-L3, so as not to give L-NEW two strings
  for one span.» (Add. 1 l. 342) and «If the tool fixes D-1 (a) and D-2 (second conjunct) are made and re-run, fed89346… matches for me as
  it stands.» (l. 341). L-2 MATCHES at both referees, each after its own byte test: REFEREE successor 29 (407f4a21, 2026-11-08T08:09:56Z)
  §C l. 230-234 («Byte test: scratch/quiet_linefix.py (successor 28's strings) run on L-1 at 559cdffc gives a result byte-equal to L-2»;
  «So L-2 = L-1 + exactly QT-L1..QT-L6. Form B is NOT in the line, as the entry says.»), l. 236-249 (D-1 and D-2 read in the diff and
  re-run: «check194.sh in a detached worktree: output byte-identical to the committed check194.out»), l. 261-264 «Fixes entry 2 CORRECT.
  L-2 MATCHES the packet (= L-1 + QT-L1..QT-L6).» … «All statements stay as in §0: SIGN; ASC-T and UP-T conditional on R121 landing first;
  UP-T under HYPOTHESIS [E-LEV].»; REFEREE-2 successor 33 (f699a724, 2026-11-08T08:12:19Z) Addendum 2 l. 351-353 («L-1 + QT-L1..QT-L6 =
  L-2 byte for byte, which is the merged-set target of my Add. 1.»), l. 354-368 (D-1, D-2 read in git diff df0d2a25..559cdffc and re-run
  on the archive: «check194.sh on the git archive of 559cdffc exits 0, and its output is byte-equal to the pinned check194.out»), l.
  378-381 «**Verdict: L-2 MATCHES** (Opus 5.5, D1).» … «ASC-T and UP-T land after R121.». L-3 (d9b5e610300927fd0e8c1ec8567ee1fb68758df7,
  5,429 bytes, b61c2029, fixes entry 3: L-2 with R-L, R-U, R-B, R-Q, R-T and R-G, each old string once in L-2, by mkl3_194.py; «L-3 is not
  routed; L-4 replaces it.», fixes l. 143) and L-4 (0809da25, 87603d07, fixes entry 4: L-3 with R-B2, by mkl4_194.py, which asserts the
  packet's and L-3's sha1). R-L, R-U, R-B, R-Q and R-T are the drafter's proposals, taken by the Lead (fixes l. 112-113, «Lead rulings
  12:21Z»); R-G is the Lead's clause for REFEREE 28's step (L41; «Wording of the clause: the Lead's, unchanged.», fixes l. 130), placed
  before «DATA, clause by clause» (l. 128-129); R-B2 is the Lead's 12:47Z ruling (l. 142). L-4 MATCHES at both referees, each after its
  own byte test: REFEREE successor 30 (3e02e7c3, 2026-11-08T13:55:51Z) §D l. 270-272 («`cmp` with the lane's L-4: **EQUAL**»), l. 274-283
  (each change read in meaning), l. 284 «Verdict: fixes entries 3-4 CORRECT. **Line L-4 MATCHES** the packet read with fixes entries 1-4,
  provided it lands after R121.»; REFEREE-2 successor 35 (96d8a3fd, 2026-11-08T13:55:42Z) Addendum 4 l. 417-421 («**L-3 == L-2 + R-L, R-U,
  R-B, R-Q, R-T, R-G: True. L-4 == L-3 + R-B2: True.**»), l. 422-428 (meaning), l. 429 «Verdict: **L-3 and L-4 MATCH.** Statement verdicts
  unchanged (all SIGN, with the boundary step explicit).». R121 is landed (59dacf22), so REFEREE's proviso holds.
- Claims signed (REFEREE successor 28: report 6ae1fc04 (= a233f356); successor 29: §C 407f4a21; successor 30: §D 3e02e7c3; REFEREE-2
  successor 33: report 17a85958, Addendum 1 11a7a911, Addendum 2 f699a724; successor 35: Addendum 3 09ce14fc, Addendum 4 96d8a3fd).
  REFEREE's table («## 0. Verdicts», l. 6-23 of R-P-N5-QUIET.md) reads Lemma CN2 «SIGN», Lemma LOC-GATE «SIGN (with [OPT] taken from
  R118's σ̄, §2 below)», Lemma LOC-K2 «SIGN», Lemma B-ONLY «SIGN», Corollary NO-TIE «SIGN», Theorem QUIET «SIGN. As frozen, the (Q5) tie
  case was a gap (G-1, «flips at most twice … to a tie»). NO-TIE closes it, and the stated L stays valid», Corollary T-QUIET «SIGN»,
  Corollary ASC-T «SIGN, conditional on P-N5-ASC landing first as R121 with the quoted HUB-ASC-G whole-run form (its L-2 states it for
  every vertex)», Corollary UP-T «SIGN under HYPOTHESIS [E-LEV], conditional as ASC-T, plus UP-B», premises [OPT] «ACCEPTED, but from
  R118's σ̄ (R118 (b) l. 75) and R21 (a), NOT from R57 (b) → QT-L1» and [E-LEV] «a HYPOTHESIS. The Lead's incorporation path is not
  accepted: R104 (vi) calls the e-priorities «immaterial» → QT-L3», the Γ3 sentence «OVERCLAIM as worded → QT-L4», §7 DATA «every replayed
  number EQUAL (own engine), plus the 3 instances the lane did not run for QUIET», §9 «CLEAN». REFEREE-2's table («## Verdicts (Opus 5.5,
  D1)», l. 20-32 of R2-P-N5-QUIET.md) reads CN2, LOC-GATE, LOC-K2, B-ONLY, NO-TIE, QUIET, T-QUIET, ASC-T «SIGN» and UP-T «SIGN, under
  HYPOTHESIS [E-LEV]», with «No statement is REFUSED. No statement has a mathematical gap. Every required change is to the line's scope or
  premise wording or to its DATA clauses.» (l. 34-35); QUIET's note «layered Bellman-Ford window bound re-derived; with NO-TIE the true
  bound is smaller, and L as stated stays valid» (l. 28), T-QUIET's «holds for every Howard run (any tie rule among new ⊴-best
  successors)» (l. 29). The joint gap map: two items, both in the FROZEN text of QUIET's proof. (1) The (Q5) tie case (L-RED R221 §3 as
  quoted in fixes entry 1 G-1; REFEREE «That was a real gap in the frozen text. NO-TIE removes ties at every gate and state, so it is
  CLOSED.», l. 131-132; REFEREE-2 «The tie case of (Q5) is closed by NO-TIE, and the Bellman-Ford window bound holds.», l. 301), closed by
  fixes entry 1 before either referee read the packet. (2) The boundary step of (Q5)'s Bellman-Ford induction (F4′ at a β-face needs the
  face outside Π of the boundary value; the frozen «by (Q4)'s argument and simplicity», packet l. 155-156, does not give it): written by
  REFEREE 28 in its first report (§3 (Q4) l. 118-120, «It holds.»), read for the Lead by REFEREE 30 as a step the proof needs and ruled
  L41's case by the Lead (12:25Z), checked and signed by REFEREE-2 35 (Add. 3: «Did this report's (Q5) cover it? **No, not explicitly.**»,
  l. 400; «So REFEREE 30 is right that the cited «(Q4)'s argument» does not give it.», l. 401-402; «**SIGN.** No statement changes, and
  QUIET's proof is complete with it.», l. 398-399), restated in fixes entry 3 (R-G repair, l. 123-127) and named in L-4's scope tail (L41
  and L43, below). No other gap at either referee («No statement has a mathematical gap.», REFEREE-2 l. 34, its first report; REFEREE's
  other findings are premise, scope and DATA wording); open gaps: none. Every required item (QT-L1..QT-L6; W-1, W-2, W-3, D-1, D-2) was
  premise, scope or DATA wording, and each is closed: REFEREE §C l. 261-264, REFEREE-2 Add. 1 l. 342 (W-1..W-3 withdrawn for QT-L4, QT-L1,
  QT-L3) and Add. 2 l. 354-375 (D-1, D-2 by tool fix). L-4's six changes (fixes entries 3-4) are line wording and the named step; both
  referees read each of them CORRECT (REFEREE §D l. 274-284; REFEREE-2 Add. 4 l. 422-429). Nothing is REFUSED.
  Setting: IDEAL-CYC(G) of R118 (a) on Γ(G) of R104, for every genome G (Γ(G) with every non-mover Even vertex frozen at R104's start, Odd
  unrestricted at the gates and K2, Howard steps at the movers); values (Λ, Π, k), ⊴ and σ̄_t as in R118's premises; [OPT]: σ̄_t optimal
  at every vertex at once against σ_t (R118's σ̄, as used in R118 (b), with R21 (a); REFEREE §2 l. 49-56, REFEREE-2 l. 46-54). Statements
  as signed (packet with fixes entries 1-4; entries 2-4 change no statement):
  (a) Lemma CN2 (§2 l. 80-81) [every genome, every positional pair]: «For every genome G, every positional pair of IDEAL-CYC(G) and every
    vertex v, the cycle node of v's play has priority ≥ 2. So no gate (priority 1) and no mover (priority 0) is ever a cycle node, and no
    gate or mover is ever in a set Π.». REFEREE SIGN (l. 9), REFEREE-2 SIGN (l. 23).
  (b) Lemma B-ONLY (fixes entry 1 l. 11-12; L-RED R221 §3, re-derived) [every genome, every state of IDEAL-CYC]: «In IDEAL-CYC(G), for
    every genome G, every state t and every vertex v other than c_W and the e-vertices whose successor is c_W, Λ_t(v) is less relevant
    than every e-vertex (it is a β-vertex, K1, K2 or the unused loop).». REFEREE SIGN (l. 12), REFEREE-2 SIGN (l. 26).
  (c) Corollary NO-TIE (fixes entry 1 l. 26): «At every state and every gate g, Ω_t(e_g) ≠ Ω_t(β_g). So LOC-GATE applies at every gate and
    state.». REFEREE SIGN (l. 13), REFEREE-2 SIGN (l. 27).
  (d) Lemma LOC-GATE (§3 l. 89-90) [every genome, every state]: «Let G be any genome, t a state of a run of IDEAL-CYC(G), g a gate, a :=
    σ̄_t(g), b := its other face, Ω := Ω_t. If Ω(a) ≠ Ω(b), then Ω(a) ◁ Ω(b).»; with NO-TIE the chosen face is the strictly ⊴-smaller one
    at every gate and state (the line's form). REFEREE SIGN (l. 10), REFEREE-2 SIGN (l. 24).
  (e) Lemma LOC-K2 (§3 l. 113): «At every state σ̄_t(K2) = K1 and Ω_t(K1) ◁ Ω_t(K2).». REFEREE SIGN (l. 11), REFEREE-2 SIGN (l. 25).
  (f) Theorem QUIET (§4 l. 119-122, 130, with fixes entry 1's (Q5) / (Q3) consequences) [every genome]: with class_t(v) := (Λ_t(v),
    E_t(v)), loud and quiet steps and quiet windows as defined (l. 119-120), «Every quiet window has at most L := (M + 1)(2M + 1)(N + 1) +
    N(n − 1) steps (n = N + 3M + 6).»; with NO-TIE, «(Q5): «flips at most twice … (to a tie, then to e)» becomes «at most once (β to e)»;
    G_C changes at most M times; at most M + 1 sub-windows; the stated L stays a valid (larger) bound.» (fixes l. 31-32). With the
    boundary step of fixes entry 3 (R-G repair: «Read (Q5)'s «by (Q4)'s argument and simplicity» as including this step. No statement
    changes.», fixes l. 127). REFEREE SIGN (l. 14; the step §3 l. 118-120), REFEREE-2 SIGN (l. 28; the step Add. 3 l. 398-399).
  (g) Corollary T-QUIET (§4 l. 131): «T ≤ Q + (Q + 1)·L ≤ (1 + Σ_v (D^tot_E(v) − 1))·(L + 1).», D^tot_E(v) «the number of distinct classes
    of v over the run» (l. 121). The line states the second bound. REFEREE SIGN (l. 15), REFEREE-2 SIGN (l. 29).
  (h) Corollary ASC-T (§5 l. 170-171) [premise RESULTS R121]: «If for every vertex v every seq_t(v) has at most B ascents, T ≤ (1 + n·((2M
    + 3)·F′_B(M) − 1))·(L + 1).». REFEREE SIGN, conditional on R121 (l. 16, §3 l. 136; §D l. 284: «provided it lands after R121»);
    REFEREE-2 SIGN (l. 30, l. 142-146).
  (i) Corollary UP-T (§5 l. 165-166) [under HYPOTHESIS [E-LEV]; premise RESULTS R121]: «For every genome G, T ≤ (1 + n·((2M +
    3)·F′_(U(G))(M) − 1))·(L + 1), with F′ as in P-N5-ASC §5. For genomes with U(G) ≤ B, B fixed, this is a polynomial in N + M.». REFEREE
    SIGN under HYPOTHESIS [E-LEV], conditional as ASC-T, plus UP-B (l. 17, §3 l. 137); REFEREE-2 SIGN, under HYPOTHESIS [E-LEV] (l. 31).
- The RESULTS line (L-4, the title): «In IDEAL-CYC(G) (RESULTS R118 (a): Γ(G) with every non-mover Even vertex frozen at R104's start, Odd
  unrestricted, Howard steps at the movers), for every genome G:» … «(premises: RESULTS R104's definitions of the genome and of Γ(G)
  only;» … «(2026-11-08) — this bounds T_CYC only, in one restricted model;» … «DATA, clause by clause (scope IDEAL-CYC, box191 idealcyc
  via box192 rpot192;» … «(P-N5-QUIET, docs/new/P-N5-QUIET.md with its fixes entries 1-3, docs/new/P-N5-QUIET-fixes.md; L-NEW successors
  62, 64 and 65)». Its clauses: the setting (R118 (a)); CN2 = (a); B-ONLY = (b) without its gloss; NO-TIE = (c); LOC-GATE = (d) in its
  strict form; LOC-K2 = (e); QUIET = (f) with its definitions inline; T-QUIET = (g), its second bound; ASC-T = (h), with «seq_t(v) and its
  ascents as in RESULTS R121» (R-Q); UP-T = (i) with [E-LEV] stated in the label; the premises parenthesis (R104, R118 (a), (b) F1, F2, F3
  and F4′'s stated clause, (c) DOM and STRICT, (e); VJ00 / Friedmann for the value order; [OPT] as R118's σ̄ with R21 (a); R121 for ASC-T
  and UP-T only; [E-LEV] a hypothesis; what is not used); the scope tail (T_CYC only, in one restricted model; the OPEN case; nothing
  proved on Γ3, with L-RED's DIV witnesses; the referee-originated boundary step, R-G); DATA clause by clause, inline (each count against
  its counter: loc194.py, bonly194.py, quiet194.py and check194.out; T-QUIET's unit with T_CYC and Q defined, R-T); the TARGET sentence
  with «so this is not M4», then «G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim» (R-U); the source note (fixes
  entries 1-3, successors 62, 64 and 65; R-B2).
- Premise: RESULTS R104's definitions of the genome and of Γ(G) only (packet §1 [DEF], l. 38-47; six quotes verbatim in R104, l. 9864), no
  R104 theorem; RESULTS R118 (a) IDEAL-CYC(G), the Howard step and T_CYC (l. 13677-13681), (b) F1, F2, F3 and F4′'s stated clause («if v ∉
  Π(A) ∪ Π(B), then A ⊴ B ⇒ ext(v, A) ⊴ ext(v, B), and A ◁ B ⇒ ext(v, A) ◁ ext(v, B).», l. 13682-13683), (c) DOM and STRICT (l.
  13686-13687), (e) CYC-COUNT («C ≤ n·(2M + 2).», l. 13691); R118's value order ⊴ (VJ00 §4.2 / Friedmann arXiv 1106.0778 §3, R118's
  premises); [OPT] (σ̄_t is optimal at every vertex at once against σ_t) as R118's σ̄, through R118 (b)'s incorporation of the frozen
  P-N5-XICYC «(§3 l. 68-83)» (l. 75: «σ̄_t is optimal at every vertex at once ([VJ])»), and RESULTS R21 (a) (l. 933); RESULTS R57 (b) is
  named as not used. For ASC-T and UP-T only, RESULTS R121 (P-N5-ASC): its Corollary HUB-ASC-G's whole-run form («over the whole run the
  number D_E(v) of distinct (Λ_t(v), E_t(v)) is at most (2M + 3)·F′_B(M)») and Corollary UP-B («under [E-LEV] every seq_t(v) has at most
  U(G) ascents»), as stated in RESULTS R121 (LANDED at 59dacf22, 2026-11-08T14:06:41Z; «### R121» l. 14320 at aaf52291, its title L-6,
  docs/new/P-N5-ASC-line-L6.txt, l-new 2f4167cd, sha1 a23c61d384036ce3fa771e27e175a8dbf2331658, verbatim, then «, CHECKER PASS
  (docs/checker/C135.md, checker a9bf46bb)»), with F′_B, seq_t(v) and «an ascent of seq_t(v)» as defined there (L-4: «with seq_t(v) and
  its ascents as in RESULTS R121», R-Q). ASC-T and UP-T rest on R121, and this entry lands only after R121 (REFEREE «Landing order: R121
  (P-N5-ASC) must land before this line, as the packet says.», l. 221; REFEREE-2 «ASC-T and UP-T are signed with R121 as a premise. They
  land only after it.», l. 45; REFEREE §D: «provided it lands after R121», l. 284); R121 is landed, and L-4 no longer says «to land first»
  (R-L). HYPOTHESIS [E-LEV] (UP-T only): «lev(x) < lev(x′) implies pr(e_(x,k)) < pr(e_(x′,k′))», stated in the line, as R121 states UP-B
  under it. «Not used: [LOC] (LOC-GATE proves it), OVT-DV, IN-BOUND, F4 as printed, F4′'s extra clause of the XICYC fixes file, F5, F6,
  BR-SEG, PATH, any L-RED lane lemma. QUIET and T-QUIET do not use [E-LEV] or [ASC].» (packet l. 76-77). Both referees checked every
  premise quote by script against RESULTS sha1 66e71196… (REFEREE §2 l. 39-48; REFEREE-2 l. 38-43: «Each one is verbatim
  (whitespace-normalised) in trunk docs/RESULTS.md, the frozen P-N5-XICYC.md (fd1266a5, sha1 149e2414, the object of R118), the frozen
  docs/red/P-N5-REALIZE.md (e609c5d2, sha1 067f06b6, the object of R104) or the packet itself. Missing: 0.»), which equals RESULTS at
  origin trunk fdc0f1e9 and local HEAD 567a53f3; RESULTS at aaf52291 (sha1 2eca04ea9b6301e9120a554d09edf9fc494e0bdd, 15,718 lines) is that
  file with l. 14320-15075 inserted (R121's and R122's blocks with their blank lines) and nothing else (by script), so every premise line
  cited here (l. 933, 9864, 10083-10086, 13607-13692) is unchanged.
- L41 and L43. The packet's proofs are L-NEW successor 62's («This packet carries every proof in full.», l. 4); B-ONLY is L-RED's lemma
  (L-RED 56, R221 §3), re-derived by L-NEW in fixes entry 1 («credit: L-RED R221 §3; proof re-derived here», l. 8) and credited in the
  line («(Lemma B-ONLY, credit L-RED R221 §3, re-derived in fixes entry 1)»); L-RED is an adversary lane, not a referee, and both referees
  signed B-ONLY on its re-derived proof (REFEREE §3 l. 92-99; REFEREE-2 l. 102-109). REFEREE's §3 adds one step in QUIET's (Q4) / (Q5),
  for the boundary value of a Bellman-Ford path («A boundary W-target y in class (w, S ∖ {e}) never has a C-vertex β in Π(y). If y's play
  passed β_g ∈ C, then E(y) ⊇ E(β_g) = S, which is impossible.», l. 118-119), and signs QUIET with it («It holds.», l. 120); REFEREE-2's
  first re-derivation does not state that case (l. 129-131). The Lead ruled L41 (DECISIONS l. 355-358) for that step: «Lead ruling: L41
  APPLIES -> R-G clause added to QUIET L-3 (L-NEW 65, six changes); REFEREE-2 35 to sign the step» (LEAD-STATE l. 2860, 12:25Z, after
  REFEREE 30's reading «(b) referee-originated step the proof needs»). The other referee checked and signed it: REFEREE-2 35, Addendum 3
  (09ce14fc), re-derives the step (l. 394-397) and «**SIGN.** No statement changes, and QUIET's proof is complete with it.» (l. 398-399).
  L-4's scope tail says so: «the step β_g ∉ Π(y) for boundary targets y in (Q5)'s F4′ (else E(y) ⊇ S, against y's class) is
  referee-originated (REFEREE R-P-N5-QUIET §3 (Q4), l. 118-120, REFEREE 28), signed by both referees» (R-G, once in L-4); both referees
  read that sentence as correct at L-4 (REFEREE §D: «R-G: CORRECT. It is the step of my §3 (Q4) l. 118-120 (REFEREE 28)», l. 275;
  REFEREE-2 Add. 4: «Its attribution to REFEREE 28 (R-P-N5-QUIET §3 (Q4), l. 118-120) is right. «signed by both referees» holds», l.
  424-425). The joint gap map (Claims signed): the tie case, closed by entry 1, and this step, closed by REFEREE 28's text with both
  signatures; open gaps: none. Fixes entry 3 restates the step as the lane's record of it («credit REFEREE 28, found again by REFEREE 30»,
  l. 123), so the source note names entry 3 (R-B2, the Lead's 12:47Z ruling: «fixes entry 3 carries a proof step, so by CHECKER's C134 N-S
  / C135 E-1 rule the source note must name it», fixes l. 142). L-4's «l. 118-120» is REFEREE's file at 6ae1fc04, 407f4a21 and ae980555
  alike (its l. 1-222 unchanged, by cmp). L43: every statement is exact or an explicit bound (L, T_CYC ≤ (1 + Σ_v (D^tot_E(v) − 1))·(L +
  1), the ASC-T and UP-T bounds), on a restricted model; no statement is killed.
- Fixes (docs/new/P-N5-QUIET-fixes.md, append-only; entry 1 by L-NEW successor 62 at d9c49489, l. 3-66, under «Lead 00:36Z: L-RED 56 R221
  items 1-2 and the [OPT] reading» (l. 3); the «Line L-1» note by successor 63 at df0d2a25, l. 68-75; entry 2 by successor 64 at 559cdffc,
  l. 77-110, under «Lead 06:39Z» (l. 77); entry 3 by successor 65 at b61c2029, l. 112-140, under «Lead 12:21Z» and «12:25Z» (l. 112);
  entry 4 by successor 65 at 87603d07, l. 142-152, under «Lead 12:47Z» (l. 142)):
  - Entry 1 G-1 (R221 §3, the (Q5) tie case): Lemma B-ONLY and Corollary NO-TIE with proofs (l. 11-29); (Q5) «at most once (β to e)», at
    most M + 1 sub-windows, (Q3) vacuous, «L stays a valid bound as stated» (l. 31-34); L-RED's DATA quoted (l. 36-37).
  - Entry 1 G-2 (R221 §7): the Γ3 sentence and L-RED's DIV witnesses DIV_2_493, DIV_2_583, DIV_3_717 (l. 39-48); the sentence's «governs»
    withdrawn by entry 2 (QT-L4), the witnesses kept.
  - Entry 1 [OPT] source (Lead reading 00:36Z, R57 (b)): withdrawn by entry 2 (QT-L1, l. 86-88).
  - Entry 1 DATA added: bonly194.py, «B-ONLY: bonlyfail 0 in 297,192 (state, vertex) pairs» and «NO-TIE: ties 0 in 89,125 (state, gate)
    pairs» (l. 58-59).
  - «Line L-1» note: L-1 by mkl1_194.py; QUIET's DATA set 10 of the 13 instances (l. 73-74).
  - Entry 2: QT-L1 ([OPT] = R118's σ̄ as used in R118 (b), with R21 (a); «R57 (b) concerns SPEC's S1 output and is not used», l. 86-88),
    QT-L2 (F2 in the premise list, l. 89), QT-L3 ([E-LEV] a HYPOTHESIS, l. 90), QT-L4 (the Γ3 sentence, l. 91-94), QT-L5 (the random set's
    parameters), QT-L6 (CN2's DATA scope) (l. 95); D-1 (quiet194.py: the exact L, wfail per window; «the only diff is each printed L one
    smaller (12 lines). No line string.», l. 96-99); D-2 (loc194.py: k2fail counts both conjuncts of LOC-K2, l. 100-101); line L-2 (l.
    102-104); Form B (l. 105-107); quiet.pins re-pinned (l. 109-110).
  - Entry 3 (Lead 12:21Z and 12:25Z, «pre-CHECKER, to save a C137 round», l. 112): R-L («to land first» dropped), R-U (the landed status
    words after «so this is not M4»), R-B (the note names entries 1-2), R-Q (seq_t(v) and its ascents as in R121), R-T (T_CYC and Q in
    T-QUIET's unit), each with the precedent the Lead cited (l. 117-121); R-G, the L41 clause, «Wording of the clause: the Lead's,
    unchanged.» (l. 130), placed before «DATA, clause by clause» (l. 128-129); the R-G repair (l. 123-127); line L-3 by mkl3_194.py (l.
    135-140), never routed.
  - Entry 4 (Lead 12:47Z; line-only): R-B2, the note names entries 1-3 and successors 62, 64 and 65 (l. 146); line L-4 by mkl4_194.py,
    «sha1 0809da259cc54e3cec1fdf455070620314d4e622, 5,433 B, 103 «(» = 103 «)»» (l. 151); quiet.pins re-pinned (l. 152).
  - Entry 1 adds two lemmas (B-ONLY, NO-TIE) and changes QUIET's proof counts, not its statement; entry 2 changes premise, scope and DATA
    wording in the line and two counters in the tools, and no statement or proof; entry 3 changes six line strings and records the
    referee-originated boundary step of QUIET's proof (R-G), and no statement; entry 4 changes one line string (R-B2).
- Not signed: packet §6 (READING: OVT-DV without [LOC]), §7 (DATA), §8 (machine checks), §9 (TARGET diff), the packet's Scope READINGs;
  Form B (formB194.out); box 194's OVT-DV / IN-BOUND counters and in194.py; REFEREE-2's Γ3 data and own random set (referee data).
- Referee strengthening (NOT part of this entry; referee checks):
  (i) REFEREE: own quiet_replay.py on successor 26's own VJ engine xicyc_vj.py and Γ builder (l. 31-34): every §7 count EQUAL (§6 l.
    204-211), B-ONLY 297,192 pairs and NO-TIE 89,125 gate-states EQUAL, «37 Howard ties in 2,522 steps, totals still equal» (l. 211);
    QUIET with the exact L (§5 l. 157); Form B on its own engine, EQUAL (§C l. 250-256).
  (ii) REFEREE-2: own r2quiet.py (builder, VJ order, Odd policy iteration from two starts and brute force from its R2-P-ACYC/r2acyc.py;
    Howard and every counter written from the packet's text; l. 184-192): violations 0 for CN2, LOC-GATE, ties, LOC-K2 (both conjuncts),
    B-ONLY, σ̄ start-dependence, brute (724 + 692 states), crossflip, q2a, q2b, backflip, multiflip, wfail with the exact L, Tfail, TQfail
    and «Q > Σ(D − 1)» (l. 190-192), on the 15 named instances, LEAP_k64, the lane's rand191 set and its own 1,000 genomes; the same with
    the e-order by gate index (l. 198-199); cn2rand «0 in 2,256,980 (random positional (σ, τ) pair, vertex) units» (l. 83); its Γ3 data
    (l. 162-173).
- Honest limits: (i) Every statement is about T_CYC, the number of Howard steps of IDEAL-CYC(G) from R104's start (Γ(G) with the
  non-movers frozen); nothing is proved on Γ3(G), about N5′-xi, about N5, or about general parity games, and nothing bounds a running time
  or a bit cost. (ii) T-QUIET moves the question to Σ_v D^tot_E(v); for genomes with U(G) unbounded and unboundedly many ascents nothing
  is claimed (OPEN). (iii) ASC-T and UP-T rest on RESULTS R121 (HUB-ASC-G's whole-run form and UP-B), and UP-T also on HYPOTHESIS [E-LEV],
  which is not part of R104's landed definition (REFEREE §2 l. 57-63; REFEREE-2 l. 64-72) and is necessary for UP-B (R121's line: «[E-LEV]
  is NECESSARY for UP-JUMP, UP-B and NOUP»). (iv) L is far from tight (W ≤ 32 against L ≥ 8,333 on the named instances; REFEREE-2 N-3, l.
  286-287), and F′_B has degree 5·2^B − 3 in M, super-polynomial when B grows like log M (packet §9 l. 199). (v) The DATA units are
  narrower than some statements: CN2's counter covers (σ_t, σ̄_t) pairs only (the line says so), LOC-GATE's and B-ONLY's the computed
  σ̄_t, and T-QUIET's counter tests T_CYC ≤ Q + (Q + 1)L (the packet's first bound; the line says so, R-T), not the Σ_v form (REFEREE-2's
  optional «the Σ_v form is not counted», Add. 4 l. 426-427, not taken: LEAD-STATE l. 2888); QUIET ran on 10 of the 13 P-N5-ASC instances
  (Form B, DATA only, covers the other three). (vi) All DATA are runs of implementations (box191 idealcyc via box192 rpot192; the
  referees' own engines) on the named sets. (vii) Names: «CN2», «LOC-GATE», «LOC-K2», «B-ONLY», «NO-TIE», «QUIET», «T-QUIET», «ASC-T»,
  «UP-T» are new to RESULTS. (viii) The source note names the packet, its fixes entries 1-3 and L-NEW successors 62, 64 and 65: entry 1
  carries B-ONLY's and NO-TIE's proofs, entry 2 the D-1 / D-2 tool fixes (the Lead's R-B: «entry 2 has tool fixes, not line-only»,
  LEAD-STATE l. 2858), entry 3 the R-G step (R-B2); the «Line L-1» note (successor 63) and entry 4 (successor 65, line-only, fixes l. 147)
  are not named (C134 N-S). (ix) Literature: VJ00 §4.2 and Friedmann arXiv 1106.0778 §3, as cited by R118 (landed; REFEREE-2 opened
  Friedmann §3, l. 49-53); no novelty is claimed. (x) QUIET's frozen proof cites «(Q4)'s argument» where the boundary step is needed; with
  REFEREE 28's step, signed by both referees, it is complete (REFEREE-2 Add. 3 l. 398-399), and the line says that the step is
  referee-originated (L41).
- Data (DATA, not proof): experiments/new/box194/ at l-new 87603d07 (= 559cdffc's but for mkl3_194.py, mkl4_194.py and quiet.pins, 42
  rows; unchanged to 91ed2f3f, git diff), run by check194.sh (loc194.py on LEAP_k64, rd3_d4, the 13 instances and 1,000 random genomes;
  quiet194.py on rd3_d4, RS2_L32M6, box193's 8 instances, rd2_d9, rd2_d10 and the random set; bonly194.py on rd3_d4, RS2_L32M6, the 13 and
  the random set; in194.py, not cited), its frozen output check194.out; called from the check.sh blocks «BOX 194 LOC» and «P-N5-QUIET»
  (experiments/new/check.sh l. 1004-1019), run by scripts/verify.sh. Re-run by the drafter from a git archive of 559cdffc (experiments,
  docs, scripts): the two blocks 2026-11-08T11:57:15Z-12:00:20Z, rc 0, «BOX 194 LOC: LOC-GATE / LOC-K2 / CN2 / OVT-DV / QUIET 0 failures,
  DEAD constant IN-BOUND (RS2_L32M6 IN 33) = frozen: PASS» and «P-N5-QUIET: packet and 38 pinned files match quiet.pins: PASS»; and from a
  git archive of 87603d07 (the two blocks byte-equal there): 2026-11-08T20:33:31Z-20:36:39Z, rc 0, the same first line and «P-N5-QUIET:
  packet and 42 pinned files match quiet.pins: PASS». Frozen totals: LOC-GATE gate-states 66,950 (LEAP_k64, T 129) + 380 (rd3_d4) + 13,980
  (13 instances) + 68,549 (random, «rand count 1000 seed 2») = 149,859, locfail 0, ties 0, cnlow 0, k2fail 0 on all 16 loc194 lines;
  B-ONLY pairs 1,273 + 17,430 + 42,355 + 236,134 = 297,192, bonlyfail 0, NO-TIE gate-states 380 + 6,216 + 13,980 + 68,549 = 89,125, ties
  0; QUIET / T-QUIET on 12 named runs (T 7-41, Q 6-28, W 0-32, L 8,333 to 3,492,236) and the random set («wfail 0 Tfail 0 crossflip 0 maxW
  4 maxT 8 maxWoverN 1.0»), wfail 0, Tfail 0, crossflip 0 everywhere; Form B (formB194.out): cR_d2_w8_R22 W 0 (N 16), rd3_d7 W 4 (N 14),
  rf_d5 W 0 (N 10), wfail 0, Tfail 0, crossflip 0. Both referees re-ran check194.sh (REFEREE at 559cdffc, §C l. 246; REFEREE-2 at
  df0d2a25, l. 203-204, and at 559cdffc, Add. 2 l. 365-366) and their own engines (above); REFEREE 30 checked the 42 pins and mkl4_194.py
  from a git archive of 87603d07 («quiet.pins 42 rows, `sha1sum -c` all OK; box194/mkl4_194.py reproduces L-4.», §D l. 273). Instances:
  experiments/new/box194/inst/ (LEAP_k64, rd3_d4 from claude/l-red d1a11af6; RS2_L{2,4,16,32}M6 by L-RED's rs2.py; SHA1SUMS), box193/inst/
  (8) and box192/inst/ (5), all pinned in quiet.pins; the random set is generated (rand191.rgen, seed 2).
- Signatures: REFEREE docs/referee/R-P-N5-QUIET.md: successor 28's report 6ae1fc0425916503194ae5e3270886d972929dee (2026-11-08T03:11:05Z;
  byte-equal at a233f35606c28b5e8168cb21a9b83b8b23342e9c, 03:11:09Z; «Written from 2026-11-08T03:10Z (date -u). The header time of record
  is the commit time.»), «I did NOT read docs/referee-2/ for this report.» (l. 3), verdict table l. 6-23; successor 29's §C
  407f4a2158f2570dc98a2c865ae30b9cef88575c (2026-11-08T08:09:56Z; heading «REFEREE successor 29, Opus 5.5, D15; date -u at writing
  2026-11-08T07:51Z»), «Only REFEREE-2's items as quoted in fixes entry 2 were read; docs/referee-2/ was not opened.» (l. 225), l.
  224-264, «Fixes entry 2 CORRECT. L-2 MATCHES the packet (= L-1 + QT-L1..QT-L6).» (l. 262). REFEREE-2 docs/referee-2/R2-P-N5-QUIET.md:
  successor 33's report 17a859580549209b508c8f84ccfb7bb85770db17 (2026-11-08T05:49:41Z; «Written 2026-11-08 by date -u (times in the
  commit).»), «Independent: docs/referee/R-P-N5-QUIET.md (REFEREE 28) NOT read before this report is on origin.» (l. 2-3), verdict table
  l. 20-32; Addendum 1 11a7a911a5b988939d58b943148710383542c29d (2026-11-08T06:14:50Z; heading «REFEREE-2 successor 33, 2026-11-08 06:14Z
  by date -u»), l. 310-343, «Read only after my report was on origin (17a85958).» (l. 311), «Verdicts unchanged (Opus 5.5, D1).» (l. 343);
  Addendum 2 f699a7245ccb46f8b82d9e3b155b8727c115a7a7 (2026-11-08T08:12:19Z; heading «REFEREE-2 successor 33, 2026-11-08 07:50Z by date
  -u»), l. 345-381, «**Verdict: L-2 MATCHES** (Opus 5.5, D1).» (l. 378). REFEREE successor 30's §D
  3e02e7c33f2b79b06204a86b37421ce4eb593c43 (2026-11-08T13:55:51Z; heading «REFEREE successor 30, Opus 5.5, D15; date -u at writing
  2026-11-08T13:55Z»), l. 266-284, «Verdict: fixes entries 3-4 CORRECT. **Line L-4 MATCHES** the packet read with fixes entries 1-4,
  provided it lands after R121.» (l. 284); the file at the referee head ae980555 is 3e02e7c3's (284 lines, sha1
  f34e5430089c9935500f4983a752a7d51fd3c487). REFEREE-2 successor 35's Addendum 3 09ce14fc1183615c884a8a96c4468ee2b79280a0
  (2026-11-08T12:32:12Z; heading «REFEREE-2 successor 35, Opus 5.5, D1; 2026-11-08 12:21Z by date -u»), l. 383-412, «**SIGN.** No
  statement changes, and QUIET's proof is complete with it.» (l. 398-399); Addendum 4 96d8a3fd2e69e994fc9498ecfc255fc01be19dd5
  (2026-11-08T13:55:42Z; heading «REFEREE-2 successor 35, Opus 5.5, D1; 2026-11-08 13:55Z by date -u»), l. 414-429, «Verdict: **L-3 and
  L-4 MATCH.** Statement verdicts unchanged (all SIGN, with the boundary step explicit).» (l. 429); the file at the referee-2 head
  c1e71a25 is 96d8a3fd's (429 lines, sha1 c4baf6d8c95b26db836196bd5e6759234bbc51aa). Lane (claude/l-new): L-NEW successor 62, 9329859d
  (packet FROZEN) and d9c49489 (fixes entry 1); successor 63, df0d2a25 (L-1); successor 64, 559cdffc (fixes entry 2, L-2); successor 65,
  b61c2029 (fixes entry 3, L-3) and 87603d07 (fixes entry 4, L-4).
- INDEPENDENCE: the packet's proofs are L-NEW's, B-ONLY's is L-NEW's re-derivation of L-RED's lemma (L41 and L43, above); each referee
  re-derived every proof step (REFEREE «## 3. Proofs (task 1; each step re-derived)»; REFEREE-2 «## Proofs (own re-derivation)») and
  replayed the DATA on its own code (REFEREE: quiet_replay.py on its own VJ engine and builder, rand191.rgen «imported only as the set's
  definition», l. 34; REFEREE-2: r2quiet.py, «no si.py, pg.py, gamma3, idealcyc or box19x code», l. 184-185). Each referee wrote its first
  report without reading the other's (REFEREE l. 3; REFEREE-2 l. 2-3); REFEREE-2 compared afterwards (Add. 1); REFEREE 29 read REFEREE-2's
  items only as quoted in fixes entry 2 (§C l. 225). L-RED R221 was context only at both («L-RED R221 (claude/l-red d49b9f0c) is context
  only; I used it only as quoted in fixes entry 1.», REFEREE l. 4; REFEREE-2 l. 3-4). One disclosure at REFEREE-2: before its Γ3 verdict
  it saw a trunk subject line («I did not read that commit's text.», l. 5). The L-2 wording is REFEREE's QT-L strings (REFEREE-2's
  W-1..W-3 withdrawn in their favour), applied by the lane by script under the Lead's 06:39Z routing; each referee byte-tested L-2 with
  its own script (REFEREE §C quiet_linefix.py; REFEREE-2 Add. 2 bt_l2.py) and read entry 2 in meaning. At L-4: R-L, R-U, R-B, R-Q and R-T
  are the drafter's proposals, R-G the Lead's clause for REFEREE 28's step, R-B2 the Lead's; REFEREE 30 byte-tested L-4 «with strings
  typed from the tables of fixes entries 3-4 … not from the lane's scripts» (§D l. 270-271); REFEREE-2 35's bt_l34.py «reads the (key,
  old, new) lists from the lane's mkl3_194.py and mkl4_194.py by ast literal parsing, without executing lane code» (Add. 4 l. 417-418), so
  it tests the lane's application of the lane's strings; both read each change in meaning. REFEREE-2's Add. 3 answers the Lead's question
  on REFEREE 28's step, which it quotes (l. 384-385), and REFEREE 30's §D names REFEREE-2's Add. 3 as the second signature (l. 276-277);
  both first reports stay independent (above).
- TARGET.md diff: TARGET.md §2 (M4) asks for one algorithm, polynomial on EVERY parity game, that outputs (W_E, W_O); every statement here
  bounds one count, T_CYC, the Howard steps of IDEAL-CYC(G) on R104 genomes, a restricted model, and UP-T / ASC-T are polynomial only
  under a hypothesis on the genome ([E-LEV] with U(G) bounded) or on its runs (bounded ascents) (TARGET.md §4: «Polynomial only on a
  restricted class …»; packet §9 l. 195-199; REFEREE §7 l. 213-217: «Not M3, not a step-4 pass. G-N5-TIME stays OPEN. N5′-xi stays a
  CANDIDATE (D1).»; REFEREE-2 l. 289-297: «§3: the values (Λ, Π, k) are n-bit objects, and no unit-cost big integer is used.»). It is not
  an algorithm claim on every game, so TARGET.md §5's gauntlet does not apply, and it is not a step-4 pass. L-4 carries «so this is not
  M4», «G-N5-TIME stays OPEN» and «not M3, not a step-4 pass, not a TARGET.md claim», in that order (R-U; by script). GAPS G-N5-TIME:
  open.

Proposed GAPS line-11 UPDATE (append-only), to go AFTER the last UPDATE on GAPS l. 11 at landing, R122's («UPDATE 2026-11-08 20:27Z:
RESULTS R122 (P-ACYC; CHECKER C136 3e7fe04e)», the last at aaf52291, after R121's «UPDATE 2026-11-08 14:06Z: RESULTS R121 (P-N5-ASC;
CHECKER C135 a9bf46bb)»), as a pure insertion with one separating space before the row's closing « |». BUILT FROM L-4 by R118's procedure
with NO reading (upd123b.py: run123()'s direct build, re-implemented, with run122()'s two drop strings «; G-N5-TIME stays OPEN» and «; not
M3, not a step-4 pass, not a TARGET.md claim» unchanged, each once in L-4; R123's date «(2026-11-08)», start «for every genome G: », its
nine labels and its source prefix «(P-N5-QUIET, docs/new/P-N5-QUIET.md»; control: on L-2 with the first fill's G-U reading the same build
gives the first fill's UPDATE a6f09325…, True). It is the first fill's UPDATE with L-4's six changes in their UPDATE forms (R-L without
its «;»; R-U as «is not M4 (P-N5-QUIET» → «is not M4, so this is not M4 (P-N5-QUIET», the first fill's Part O; R-B with R-B2; R-Q's clause
part; R-T; R-G), each old string once (True). The UP-T label stands after the premises parenthesis, as in the first fill (G-U (ii), for
CHECKER). sha1 739c5f7142fada0a55bb24b9d7627c9a348918d8 of the line without newline and unfilled (5,465 bytes). <DATE>, <HH:MM> and
<checker> are the landing date, time and the C137 commit, all filled at landing, as R121's and R122's were (their draft UPDATEs occur on
GAPS l. 11 at aaf52291 filled, True):
UPDATE <DATE> <HH:MM>Z: RESULTS R123 (P-N5-QUIET; CHECKER C137 <checker>) [refereed-only] LANDED: In IDEAL-CYC(G) (RESULTS R118 (a): Γ(G) with every non-mover Even vertex frozen at R104's start, Odd unrestricted, Howard steps at the movers), for every genome G: the cycle node of every play under every positional pair has priority ≥ 2, so no gate or mover is a cycle node or in a set Π (Lemma CN2); at every state t and every vertex v other than c_W and the e-vertices whose successor is c_W, Λ_t(v) is less relevant than every e-vertex (Lemma B-ONLY, credit L-RED R221 §3, re-derived in fixes entry 1); at every state and gate g, Ω_t(e_g) ≠ Ω_t(β_g) (Corollary NO-TIE); at every state t and gate g, Odd's optimal counterstrategy σ̄_t chooses the face of strictly ⊴-smaller value (Lemma LOC-GATE); σ̄_t(K2) = K1 and Ω_t(K1) ◁ Ω_t(K2) at every state (Lemma LOC-K2); with class_t(v) := (Λ_t(v), E_t(v)), E_t(v) the e-vertices of Π_t(v), a step loud if some vertex changes class and quiet otherwise, every maximal window of quiet steps has at most L := (M + 1)(2M + 1)(N + 1) + N(n − 1) steps, n = N + 3M + 6 (Theorem QUIET); T_CYC ≤ (1 + Σ_v (D^tot_E(v) − 1))·(L + 1), D^tot_E(v) the number of distinct classes of v over the run (Corollary T-QUIET); with seq_t(v) and its ascents as in RESULTS R121, if every seq_t(v) has at most B ascents for every vertex v, T_CYC ≤ (1 + n·((2M + 3)·F′_B(M) − 1))·(L + 1) with F′_B of RESULTS R121 (P-N5-ASC) (Corollary ASC-T); the same bound with B = U(G), the number of options whose Ξ-target has a higher level, so T_CYC is polynomial in N + M for genomes with U(G) ≤ B, B fixed (premises: RESULTS R104's definitions of the genome and of Γ(G) only; RESULTS R118 (a), (b) F1, F2, F3 and F4′'s stated clause, (c) DOM and STRICT, (e); VJ00 §4.2 / Friedmann arXiv 1106.0778 §3 for the value (Λ, Π, k) and its order ⊴; [OPT] (σ̄_t is optimal at every vertex at once against σ_t) = RESULTS R118's σ̄, Odd's optimal counterstrategy for the order ⊴, as used in R118 (b) (F3's proof in the frozen P-N5-XICYC §3, l. 75: «σ̄_t is optimal at every vertex at once ([VJ])»), and RESULTS R21 (a) («(Odd's best reply σ̄_k is pointwise optimal in G_{σ_k})»); RESULTS R57 (b) concerns the output of SPEC's S1 procedure and is not used; for ASC-T and UP-T only, RESULTS R121's HUB-ASC-G whole-run form and UP-B; [E-LEV] is a hypothesis (the e-priorities of R104's packet §3.1, docs/red/P-N5-REALIZE.md l. 88, satisfy it, but R104 (vi) leaves them to that packet as immaterial to its own results, so R104's line does not fix them); not used: [LOC], OVT-DV, IN-BOUND, F4 as printed, F5, F6, any L-RED lane lemma; QUIET, T-QUIET, B-ONLY and NO-TIE use neither [E-LEV] nor R121) (Corollary UP-T, under HYPOTHESIS [E-LEV]: lev(x) < lev(x′) implies pr(e_(x,k)) < pr(e_(x′,k′))): this bounds T_CYC only, in one restricted model; for Σ_v D^tot_E(v) with U(G) unbounded and unboundedly many ascents nothing is claimed (OPEN); T bounds IDEAL-CYC iterations only; nothing is proved on Γ3: by RESULTS R118 (k) and (l), under REACH3-CYC's premises, N5′-xi from S3 on Γ3(G) makes Howard steps on Γ3 up to its first fallback, a run that can differ from the IDEAL-CYC run at exact VJ ties (R118's DATA), and a Γ3 form of this proof (not given here) would bound N5′-xi only up to its first fallback; nothing is claimed about post-fallback iterations, N5′-xi's total count, N5 or general games (witnesses that the restriction is needed: L-RED R221 §7 DIV_2_493, DIV_2_583, DIV_3_717, claude/l-red d49b9f0c, experiments/red/r221q/inst/SHA1SUMS, where N5′-xi on Γ3 changes movers after its first fallback); the step β_g ∉ Π(y) for boundary targets y in (Q5)'s F4′ (else E(y) ⊇ S, against y's class) is referee-originated (REFEREE R-P-N5-QUIET §3 (Q4), l. 118-120, REFEREE 28), signed by both referees; DATA, clause by clause (scope IDEAL-CYC, box191 idealcyc via box192 rpot192; tools in experiments/new/box194/, run by check194.sh; set S: L-RED's rd3_d4 and RS2_L32M6 and LEAP_k64 (box194/inst/), the 13 P-N5-ASC instances, 1,000 random genomes rand191.rgen seed 2, d 1-6, w 1-3, degree 2-3): LOC-GATE: locfail 0 in 149,859 (gate, state) pairs (LEAP_k64, rd3_d4, the 13 instances, the 1,000 random genomes; loc194.py); LOC-K2: k2fail 0 (unit: states; same runs); CN2: cnlow 0 (unit: (state, vertex) pairs under (σ_t, σ̄_t); other positional pairs: no separate DATA; same runs); B-ONLY: bonlyfail 0 in 297,192 (state, vertex) pairs, NO-TIE: ties 0 in 89,125 (state, gate) pairs (rd3_d4, RS2_L32M6, the 13 instances, the 1,000 random genomes; bonly194.py); QUIET: wfail 0 (unit: quiet windows) and crossflip 0 (unit: σ̄ flips on quiet steps at gates whose faces are in different classes), longest window W ≤ N on every run (max W/N 1.0 on the 1,000 random genomes; quiet194.py; rd3_d4, RS2_L32M6, 10 of the 13 instances (all but cR_d2_w8_R22, rd3_d7, rf_d5), the 1,000 random genomes); T-QUIET: Tfail 0 (unit: runs with T_CYC > Q + (Q + 1)L, Q the number of loud steps; same set as QUIET); no separate DATA for ASC-T and UP-T (R121's UP-B / HUB-ASC-G plus T-QUIET); TARGET.md §2 (M4) asks for an algorithm polynomial on every parity game and §4 says a bound on a restricted class is not M4, so this is not M4 (P-N5-QUIET, docs/new/P-N5-QUIET.md with its fixes entries 1-3, docs/new/P-N5-QUIET-fixes.md; L-NEW successors 62, 64 and 65). G-N5-TIME stays open.

Addendum (subagent, for the Lead; does not land; written 2026-11-08T12:17:00Z by date -u). (1) FIRST FILL on line L-2 (l-new 559cdffc,
sha1 fed89346…), to CHECKER C137. I edited docs/agents/R123-draft.md only; no merge, no commit and no push by me; the Lead commits this
file. Fetches: 11:52:48Z and 12:05:26Z (record, l. 2); every object is unchanged at the second (git diff --quiet). (2) TITLE d[327] (l.
328) = "### R123 [refereed-only] " + L-2 without its newline + ", CHECKER PASS (docs/checker/C137.md, checker PENDING)", checked by script
(chk123.py): equal, byte for byte (True); and the title minus that prefix and that tail is L-2 (True); the only «### R» heading of this
file; 5,105 characters, 5,209 bytes, sha1 of the heading line without its newline 2da352ac9b1b431d1d1ec4fcc62558d8342063f8; 97 «(» / 97
«)» (L-2's 96 and the fill's), 0 "|", «R1xx» 0, «[refereed-only]» once. (3) SHAPE. The entry block is l. 328-542 (python slice d[327:542],
215 lines), followed by a blank line (d[542]); 0 "|" in it; «checker PENDING)» once in it (five times in the whole file: the title, item
(1) of the record and items (2), (3) and (7) of this Addendum). The GAPS preamble is l. 544-554 (d[543:554]); the UPDATE is l. 555
(d[554]), one line, sha1 a6f09325fd6d7e2409ef30078f27bc38aee20028 without newline and unfilled (= upd123L2.txt, True), 5,155 bytes, 5,053
characters, 851 tokens, 96 «(» / 96 «)», 0 "|", one each of «<DATE>», «<HH:MM>», «<checker>», «2026-11-08» 0 times, « — » 0 times. A
landing script slices d[327:542] for the entry and reads d[554] for the UPDATE, with «R123», «C137», PREV = R122's block and UPDATE (when
R121 and R122 land first, as routed; else the last landed entry, G-P). The FIRST FILL record is l. 2-326 (d[1:326]), then a blank line.
(4) WHAT IS LEFT: the Lead's ruling on G-7 (L41) and its routing of G-L (R-L) and G-U (R-U); CHECKER C137 on this file (G-L, G-U (i) and
(ii), G-1 with optional R-B, G-2 (ii) with optional R-Q and R-T, G-4 (ii), the G-9 notes); if any replacement is taken, an L-3 by L-NEW
(fixes entry 3, line only), both referees' byte tests (R-U, R-Q, R-T and an R-G are new text: read in meaning), and a second fill (title,
line history, Object, L41 and L43, Honest limits (viii), Signatures, the UPDATE rebuilt from L-3 by the same procedure with no reading).
If the Lead rules L41's case for G-7, REFEREE-2 checks and signs REFEREE's (Q4) boundary step before R-G is written. R121 (C135 Add. 2)
and R122 (C136) land first, then R123. The Lead merges claude/l-new (559cdffc or later), claude/referee (407f4a21 or later) and
claude/referee-2 (f699a724 or later) before landing, then lands R123 with <DATE>, <HH:MM> and <checker> filled. (5) QUOTE SWEEP
(chk123.py: outermost guillemet quotes, nested ones inside them, split at «…», parts of 6+ characters, whitespace-normalised, NO
docs/agents draft as a source; sources: the packet, fixes (at 559cdffc, d9c49489, df0d2a25), L-1, L-2 at 559cdffc; REFEREE's file at
6ae1fc04 and 407f4a21 (= the head); REFEREE-2's at 17a85958, 11a7a911 and f699a724 (= the head); at fdc0f1e9 and 567a53f3 RESULTS, GAPS,
DECISIONS, DECISIONS-INDEX, LEAD-STATE, NOW, TARGET.md, CLAUDE.md, P-N5-XICYC.md, P-N5-REALIZE.md, and LEAD-STATE at c9591e35;
C132.md-C135.md and notes/CHECKER.md on claude/checker; P-N5-ASC.md and its L-5 at e28e962d, L-6 at 2f4167cd; check.sh and box 194's
check194.sh, quiet.pins, loc194.py, quiet194.py, bonly194.py, mkl1_194.py, mkl2_194.py, in194.py, check194.out, formB194.out at 559cdffc;
the subjects of the 22 commits cited; my outputs blocks.out, mkl2.out, upd123.out, upd123L2.txt, upd123L2_alt.txt, prop_*.txt,
upd_prop_*.txt): on the draft before this Addendum, line 1 and the first-fill record 238 quotes, 202 parts, 0 not found; title and body
144 quotes, 134 parts, 0 not found; GAPS preamble and UPDATE 11 quotes, 10 parts, 0 not found; whole file 393 quotes, 346 parts, 0 not
found; negative control (a made-up quote) reported missing (True); the run on the final file is in chk_final.out. lp123.py: 169 quotes and
line references at their cited lines (packet l. 4-199, fixes l. 3-110, REFEREE l. 3-264, REFEREE-2 l. 2-381, RESULTS l. 933, 9864,
10083-10086, 13607-13691, 13879, 14114, 14320-14392, DECISIONS l. 355-358, DECISIONS-INDEX l. 34, 36, LEAD-STATE l. 2848 (567a53f3) and l.
2754 (c9591e35), P-N5-XICYC l. 75, P-N5-REALIZE l. 88-89, P-N5-ASC l. 70, check.sh l. 1004-1019, loc194.py, quiet194.py, bonly194.py and
check194.sh at the cited lines), 0 failed. (6) STALE STATUS (chk123.py, case-insensitive): in the entry block with the title excepted
«pending», «will », «awaiting», «to come», «not landed», «first fill», «second fill», «this fill», «to land» 0 each; «NOT YET» 2
(REFEREE's and REFEREE-2's L-1 verdicts, quoted as history); the title has «PENDING» once (the fill) and «to land first» once (L-2's own
words, G-L); GAPS preamble and UPDATE: «to land» 1 (the UPDATE carries L-2's «to land first», G-L); line 1 «NOT LANDED» 1 (R123 is not
landed). (7) LANDING SIMULATION (sim123.py on in-memory copies of RESULTS 66e71196… and GAPS 2a41c765… at origin trunk fdc0f1e9, = local
HEAD 567a53f3's). CASE 1, as routed: R121's fourth-fill entry (R121-draft.md c9fb8f5b, d[659:1072]; its «checker PENDING)» left as is) + a
blank line inserted directly before «**Erratum E-1**», then R122's entry (R122-draft.md 2cd7cfd0, d[446:718]) + a blank line, then R123's
d[327:542] + a blank line, each directly before «**Erratum E-1**» (each a pure insertion: prefix and suffix byte-unchanged, True); RESULTS
14,962 → 15,376 → 15,649 → 15,865 lines (+216 for R123); R118 l. 13,607, R119 l. 13,879, R120 l. 14,114, R121 l. 14,320, R122 l. 14,734,
R123 at l. 15,007-15,221, blank l. 15,222, «**Erratum E-1**» to l. 15,223, E-2 15,236, Note E-3 15,264, Dead ends 15,295; order R110-R123,
E-1, E-2, E-3, Dead ends: True. GAPS: only l. 11 changes (True), the closing " |" replaced by " " + R121's, R122's and R123's filled draft
UPDATEs + " |"; "|" on l. 11 76 → 76; «UPDATE 2026-» 55 → 55 plus three heads with the simulation year 2099 after R120's; R123's UPDATE
last, R121 < R122 < R123 (True); 23 → 23 lines. CASE 1b, with R121's third-fill entry as on origin trunk (1fa73568, d[530:886]): R121 l.
14,320, R122 l. 14,677, R123 at l. 14,950-15,164, E-1 15,166; the same order and GAPS results (True). CASE 2, R123 directly after R120 (if
neither R121 nor R122 is landed first): R123 at l. 14,320-14,534, blank l. 14,535, E-1 l. 14,536, E-2 14,549, Note E-3 14,577, Dead ends
14,608; order True; GAPS as above with one 2099 head, R123's last (True). Fill values used only for the simulation: 2099-01-08 /
2099-01-09 / 2099-01-10, 00:00, 0000000 / 1111111 / 2222222. (8) UPDATE (upd123.py): r122b/tools/upd122b.py exec'd unchanged but for its
one file write (into r122b/, not executed); it execs r122/tools/upd122.py, which execs r121/tools/upd121.py l. 1-70, which execs
r120b/tools/upd120b.py l. 1-311: controls R97-R120 as landed, True ×24, the last UPDATE on l. 11 R120's (True); the R121 controls, NOT
landed: run121 on P-N5-ASC L-2 = 6635b14e… (True), with C135 §5's R1-R4 = f545cba7… (True), on L-4 = d3a42330… (True), and (new) on L-5
(e28e962d) = C135 Add. 1's 3571ef76… (5,222 bytes, True) and on L-6 (2f4167cd) = C135 Add. 1's e975c303… (5,479 bytes, True) =
R121-draft.md's UPDATE line at c9fb8f5b (True); the R122 controls: run122 on P-ACYC L-3 = a9274893… (True) and on L-4 = 425d10fe… (3,108
bytes, True) = R122-draft.md's UPDATE line at 2cd7cfd0 (True). Part N, R123 by run123() (run122()'s steps: R123's date «(2026-11-08)»,
START «for every genome G: », nine labels, source prefix «(P-N5-QUIET, docs/new/P-N5-QUIET.md»), = the direct build (True); connectors «;
» ×8 kept in front of their clauses. Without the reading the build stops at its drop assertion («; not M3, not a step-4 pass, not a
TARGET.md claim» not in L-2: AssertionError, G-U). With the reading: token diff L-2 → UPDATE, 18 hunks, 60 tokens out, 57 in: the head
inserted («UPDATE <DATE> <HH:MM>Z: RESULTS R123 (P-N5-QUIET; CHECKER C137 <checker>) [refereed-only] LANDED:»); the nine labels moved
behind their clauses (UP-T's, with its inner «: », in place of « (2026-11-08) —», followed by «:», after the premises parenthesis, G-U
(ii)); «G-N5-TIME stays OPEN;» dropped; «M4: not M3, not M4, not a step-4 pass, not a TARGET.md claim» → «M4»; «62)» → «62). G-N5-TIME
stays open.». Nothing else. Part O: each of R-L, R-U, R-B, R-Q, R-T occurs once in L-2 (True ×5); L-2 + R-L + R-U e13a80f6… (5,127 bytes)
and its UPDATE by run123() with NO reading (run122()'s drops unchanged) cab24ad0… (5,159 bytes) = the draft's UPDATE with R-L's and R-U's
UPDATE forms applied (True); with R-B 13de74be… / c467443b… (True); with R-B, R-Q, R-T a4802f27… / 499acfb6… (True). Pipe rule: the filled
R123 UPDATE appended after R122's after R121's (simulated) after R120's (landed), and directly after R120's: 76 "|" on l. 11, R123's last,
prefix byte-unchanged (True). (9) NOT VERIFIED / NOT DONE: scripts/verify.sh not run (the two box 194 blocks of experiments/new/check.sh
only, from a git archive of 559cdffc; not the whole check.sh); the referees' tools not re-run (their files read); no simulator of my own
(the DATA are the lane's tools, re-run through the blocks; rpot192, idealcyc and si.py not read beyond what the three counters call); the
proofs not re-derived by me beyond reading the packet, entry 1 and both referees' re-derivations (G-7 is a text check of where REFEREE's
(Q4) step stands in each file; I did not test whether REFEREE-2's «(Q4)'s argument» is meant to cover it); VJ00 / Friedmann not opened by
me (R118's landed premise; REFEREE-2 opened Friedmann); L-RED R221 (claude/l-red d49b9f0c) not read beyond the SHA1SUMS of its r221q/inst/
(the four rows, as quoted in fixes entry 1); R121's line L-6 is the fourth fill's (CHECKER C135 Add. 2 not run yet), so the R121 premise
check is against L-6 and L-5, not against a landed R121; no Oink run (L-2 cites no Oink check). (10) Scratch:
/tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad/r123/ (src/ (the packet, fixes at 559cdffc
and d9c49489, L-1, L-2, the referee files at each commit, C132.md-C135.md, R121's L-6, the first fills of R121 and R122, GAPS l. 11);
arch/ = git archive of 559cdffc (experiments, docs, scripts), arch_mk/ its copy for mkl2_194.py; blocks.out, blocks.rc, blocks.start,
blocks.end, mkl2.out; tools/upd123.py, upd123.out, upd123L2.txt, upd123L2_alt.txt, prop_*.txt, upd_prop_*.txt; tools/chk123.py,
chk_p1.out, chk_final.out; tools/lp123.py, lp_p1.out, lp_final.out; tools/sim123.py, sim_p1.out, sim_final.out; tools/assemble123.py,
template.txt, addendum.txt, filltime.txt).

Addendum 2 (subagent, for the Lead; does not land; written 2026-11-08T20:39:34Z by date -u). (1) SECOND FILL on line L-4 (l-new 87603d07,
sha1 0809da25…), to CHECKER C137. Built in the scratchpad by fill2.py from git show aaf52291:docs/agents/R123-draft.md (sha1 8f361e55…,
asserted); I merged, committed and pushed nothing and wrote nothing into the repository; the Lead commits this file. Fetch:
20:28:37Z-20:28:38Z (SECOND FILL section). (2) TITLE d[467] (l. 468) = "### R123 [refereed-only] " + L-4 without its newline + the fill
tail ", CHECKER PASS (docs/checker/C137.md, checker " + "PENDING)", checked by script (chk123b.py): equal, byte for byte (True); the title
minus that prefix and that tail is L-4's bytes without the newline (True); the only «### R» heading of this file; 5,398 characters, 5,511
bytes, sha1 of the heading line without its newline 4ec05053179fe41219fc729631b2caa30da2f6ab; 104 «(» / 104 «)» (L-4's 103 and the
fill's), depth never negative, 0 "|", «R1xx» 0, «[refereed-only]» once, the fill token once. (3) SHAPE. The entry block is l. 468-761
(python slice d[467:761], 294 lines), followed by a blank line (d[761]); 0 "|" in it; the fill token once in it (five times in the whole
file: the title, item (1) of the first-fill record and items (2), (3) and (7) of the first-fill Addendum; this Addendum spells it in two
pieces); the landing anchor «\n**Erratum E-1** (not a result» 0 times in it («**Erratum E-1**» 0 times). The GAPS preamble is l. 763-774
(d[762:774]); the UPDATE is l. 775 (d[774]), one line, sha1 739c5f7142fada0a55bb24b9d7627c9a348918d8 without newline and unfilled
(1798910000d1d78bdf69684ec9f3871ef7a91329 with its newline; = upd123L4.txt, True), 5,465 bytes, 5,354 characters, 905 tokens, 103 «(» /
103 «)», 0 "|", one each of «<DATE>», «<HH:MM>», «<checker>», «2026-11-08» 0 times, « — » 0 times. A landing script slices d[467:761] for
the entry and reads d[774] for the UPDATE, with «R123», «C137», PREV = R122's block and UPDATE (both landed). The SECOND FILL section is
l. 2-141 (d[1:141]); the FIRST FILL record l. 142-466 (d[141:466]), then a blank line; the first fill's Addendum l. 777-856 (d[776:856]);
this Addendum follows a blank line. (4) WHAT IS LEFT: CHECKER C137 on this file (G-U (ii); the notes N-T, N-L41, N-G4; the first fill's
G-9 notes); the Lead merges claude/l-new (87603d07 or later) before landing (claude/referee ae980555, claude/referee-2 c1e71a25 and
claude/checker bdfb2d07 are already in the trunk at aaf52291), then lands R123 after R122 with <DATE>, <HH:MM> and <checker> filled. (5)
QUOTE SWEEP (chk123b.py: outermost guillemet quotes, nested ones inside them, split at «…», parts of 6+ characters, whitespace-normalised,
NO docs/agents draft as a source; sources: the first fill's (r123/src, its archive of 559cdffc, its outputs) and the new ones: the packet,
fixes and L-1 to L-4 at their commits, REFEREE's file at 6ae1fc04, 407f4a21 and ae980555, REFEREE-2's at 17a85958, 11a7a911, f699a724,
09ce14fc and c1e71a25, REFEREE's quiet_logs/l4test.out and REFEREE-2's bt_l34.out, RESULTS, GAPS, DECISIONS, DECISIONS-INDEX, LEAD-STATE,
NOW, TARGET.md, CLAUDE.md, P-N5-XICYC.md and P-N5-REALIZE.md at fdc0f1e9, 567a53f3 and aaf52291, C132.md-C136.md and notes/CHECKER.md at
bdfb2d07, check.sh at 559cdffc and 87603d07, box 194's files at 559cdffc and 87603d07, the subjects of the 38 commits cited, git's «Not a
valid object name» (D-7), and my outputs blocks.out, mk.out, l4rel123b.out, upd123b.out, upd123L4.txt): on the draft before this Addendum,
line 1 0 quotes; the SECOND FILL section 92 quotes, 75 parts, 0 not found; the first-fill record 238 quotes, 202 parts, 0 not found; title
and body 202 quotes, 193 parts, 0 not found; GAPS preamble and UPDATE 13 quotes, 11 parts, 0 not found; the first-fill Addendum 51 quotes,
35 parts, 0 not found; whole file 596 quotes, 516 parts, 0 not found; negative control (a made-up quote) reported missing (True); the run
on the final file is in chk_final.out. lp123b.py: 102 quotes and line references new at this fill at their cited lines (REFEREE l.
118-120, 266-284 at ae980555 and 6ae1fc04; REFEREE-2 l. 34, 129-131, 383-429 at c1e71a25; fixes l. 111-152 at 87603d07; LEAD-STATE l.
2858, 2860, 2865, 2871, 2882, 2887, 2888, 2892 at aaf52291; RESULTS l. 933, 9864, 13607, 14320, 14604, 14743, 14744, 15075, 15076, 15089,
15117, 15148 and GAPS l. 11 at aaf52291; DECISIONS l. 355-358; notes/CHECKER.md l. 7 at bdfb2d07; packet l. 155-156; check.sh l. 1004-1019
at 87603d07; R121's L-6), 0 failed. (6) STALE STATUS (chk123b.py, case-insensitive): in the entry block with the title excepted «pending»,
«will », «awaiting», «to come», «not landed», «first fill», «second fill», «this fill» 0 each; «NOT YET» 2 (REFEREE's and REFEREE-2's L-1
verdicts, quoted as history); «to land» 2, both the dropped words «to land first» quoted as dropped (Premise; the Fixes bullet of entry
3); the title has «PENDING» once (the fill) and «to land first» 0 times. Line 1 «NOT LANDED» once (R123 is not landed). (7) LANDING
SIMULATION (sim123b.py on in-memory copies of RESULTS 2eca04ea… and GAPS 298be51e… at aaf52291): R123's d[467:761] (the fill token filled
with a simulation value) + a blank line inserted directly before «\n**Erratum E-1** (not a result», after R122's block and its blank line:
a pure insertion (prefix and suffix byte-unchanged, True); RESULTS 15,718 → 16,013 lines (+295); R120 l. 14,114, R121 l. 14,320, R122 l.
14,744-15,074 (blank l. 15,075), R123 l. 15,076-15,369, blank l. 15,370, «**Erratum E-1**» to l. 15,371, E-2 15,384, Note E-3 15,412, Dead
ends 15,443; order R120 < R121 < R122 < R123 < E-1 < E-2 < E-3 < Dead ends (True); R123 the last of 24 «### R1xx» headings; "|" in RESULTS
1,477 → 1,477 (unchanged). GAPS: only l. 11 changes (True), its closing " |" replaced by " " + R123's filled UPDATE + " |"; "|" on l. 11
76 → 76 (whole file 198 → 198); «UPDATE 2026-» 57 → 57 plus one head with the simulation year 2099 after R122's; R123's last (True); 23 →
23 lines. Fill values used only for the simulation: 2099-01-10, 00:00, 2222222. (8) UPDATE (upd123b.py; SECOND FILL section (c)): the
first fill's d[554] with L-4's six changes in UPDATE form = the standalone direct build on L-4 with no reading = 739c5f71… (True); control
on L-2 with the first fill's reading = a6f09325… (True); on GAPS l. 11 at aaf52291 R121's and R122's draft UPDATEs occur filled, R122's
last (True); R123's appended after it keeps 76 "|" (True). (9) KEPT SECTIONS (rec123b.py): the first-fill record d[141:467] = the first
fill's d[1:327] (True, 326 lines with its blank line) and the first fill's Addendum d[775:856] = its d[555:636] (True, the blank line and
80 lines); the first fill's title and UPDATE lines occur nowhere in this file. (10) HEX IDS (hex123b.py): in line 1, the SECOND FILL
section, the entry block, the GAPS preamble and the UPDATE (before this Addendum) 88 distinct hex ids: 55 git objects, 33 sha1s measured
at this fill (files at their commits, the lines, the drafts, the UPDATE lines, the title), 0 neither; the run on the final file is in
hex_final.out. (11) NOT VERIFIED / NOT DONE: scripts/verify.sh and scripts/push.sh not run (not asked; the two box 194 blocks of
experiments/new/check.sh only, from a git archive of 87603d07; not the whole check.sh); the referees' scripts quiet_l4.py and bt_l34.py
not read or re-run (their outputs l4test.out and bt_l34.out read); the proofs not re-derived by me beyond reading REFEREE 28's step (§3
(Q4) l. 118-120) and REFEREE-2's Add. 3 re-derivation; L-RED's files not read; the Lead's rulings taken from LEAD-STATE and the fixes
headings as logged there (stamps: D-6); CHECKER C137 does not exist yet; no Oink run (L-4 cites no Oink check). (12) Scratch:
/tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad/r123b/ (src/ (the first-fill draft's
sources new at this fill: L-2 to L-4, fixes at 559cdffc, b61c2029 and 87603d07, the referee files at each commit, RESULTS, GAPS, DECISIONS
and LEAD-STATE at aaf52291, mkl3_194.py, mkl4_194.py, the packet); arch/ = git archive of 87603d07 (experiments, docs, scripts), arch_mk/
its copy for mkl3_194.py and mkl4_194.py; blocks.out, blocks.rc, blocks.start, blocks.end, mk.out; tools/l4rel123b.py, l4rel123b.out;
tools/upd123b.py, upd123b.out, upd123L4.txt; tools/chk123b.py, chk_p1.out, chk_final.out; tools/lp123b.py, lp_p1.out, lp_final.out;
tools/sim123b.py, sim_p1.out, sim_final.out; tools/rec123b.py, rec_p1.out, rec_final.out; tools/hex123b.py, hex_p1.out, hex_final.out;
tools/blocks194.sh, runblocks.sh; parts/secondfill.src, preamble.src, addendum2.src; fill2.py; filltime.txt; report.txt).
