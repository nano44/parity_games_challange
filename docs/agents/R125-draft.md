# Draft RESULTS R125 (Lead; first fill 2026-11-09T08:48:38Z by date -u (subagent) on P-N5-CHAIN line L-4, docs/new/P-N5-CHAIN-line-L4.txt, l-new 87603d07, sha1 a69c8aa96fb0b67c6c0a3f6d11670a0b57ba9331 (draft sha1 81cbdc63, CHECKER C139 389d19f8: FAIL E-1, E-2); SECOND FILL 2026-11-11T22:09:46Z by date -u (subagent) on P-N5-CHAIN line L-5, docs/new/P-N5-CHAIN-line-L5.txt, l-new dd83371b, sha1 473344b1149d4b44d87bdb917607b618d05d57ce) — to CHECKER C139 Add. 1 — NOT LANDED; goes after R124 (LANDED at 8ba1b23b, RESULTS l. 15371-15593), before Erratum E-1 — LANDED in RESULTS 2026-11-11 23:47Z (CHECKER C139 1622c7d9 PASS), after R124, before Erratum E-1
SECOND FILL (2026-11-11T22:09:46Z by date -u, subagent; for CHECKER C139 Add. 1). Read at the origin heads of a git fetch of claude/l-new,
claude/referee, claude/referee-2, claude/checker and claude/vibrant-johnson-nxvvxo at 2026-11-11T22:02:55Z-2026-11-11T22:02:56Z (date -u
before and after; its exit code was not captured, the output having been piped to tail), a second fetch of the same five branches at
2026-11-11T22:07:45Z-2026-11-11T22:07:46Z: rc 0, every head unchanged, and a third at 2026-11-11T22:13:13Z-2026-11-11T22:13:14Z before the
build: rc 0, the lane, referee and checker heads unchanged, the trunk moved to 86f62c26 (TRUNK below). I merged, committed and pushed
nothing, wrote nothing into the repository and did not run scripts/push.sh or scripts/verify.sh; this file is built in the scratchpad r125b/
by fill2.py from git show a179ef4a:docs/agents/R125-draft.md (sha1 81cbdc63175959f986ff90af8ffb7f1ddffa8fda, asserted; the same file at
origin trunk 8ba1b23b). Heads: l-new 1478886e (1478886ea4c21b78466e088fe66daa08b6a08f74, 2026-11-11T21:33:16Z, «L-NEW 69: BOX 205 — Lemma
BETA-LOC (per-state form of R122 BETA-ACYC: β-face whenever xt's Ξ_σ-path ends at X and Λ(e_g) is not an odd vertex ≠ K1), …»), the branch
head (box 205; not part of this entry); its parent dd83371b (dd83371b2d91163adacdb5b606c8f92a0cd697f6, 2026-11-11T21:07:21Z, «L-NEW 69:
P-N5-CHAIN fixes entry 4 (line-only, CHECKER C139 E-1 R-U, E-2 R-L1 / R-L2) + line L-5 by script (sha1 473344b1, 9,047 B = C139 §4);
chain.pins re-pinned»), L-NEW successor 69, the commit of record: git diff 87603d07 dd83371b on the packet, the fixes file, the line files
and experiments/new/box196/ names exactly docs/new/P-N5-CHAIN-fixes.md, docs/new/P-N5-CHAIN-line-L5.txt (new), box196/chain.pins and
box196/mkl5_196.py (new), and git diff dd83371b 1478886e on the same paths is empty. The packet docs/new/P-N5-CHAIN.md is sha1
6e613ba762b6ecf67247ef6d8674b4c960013039 at 93531b03, 87603d07, dd83371b, 1478886e and 8ba1b23b; L-4 is a69c8aa9 at 87603d07, dd83371b and
1478886e. By git, dd83371b is the commit and 473344b1149d4b44d87bdb917607b618d05d57ce the sha1 of docs/new/P-N5-CHAIN-line-L5.txt (the
file's only commit; its blob is c3d0fa631f6cefaa45ff92945d2ec2bd06a7a4cc; 9,047 bytes, one line with its newline). The fixes file at
dd83371b: 119 lines, 14,596 bytes, sha1 7b620ce2d0965f286ad9a3cec0c359e7406bbd3d; its first 11,431 bytes are the file at 87603d07 (sha1
e823ca09db0b61368841f831d2ae5dd13161acc9), by prefix test; fixes entry 4 is l. 96-119. chain.pins at dd83371b: 59 rows (87603d07's 57 with
the fixes file re-pinned, and L-5 and mkl5_196.py added). referee d2678292 (d2678292247a2778ded5b0e0c7a9f93ce9973de4, 2026-11-11T21:35:16Z,
«REFEREE successor 30: R-P-N5-CHAIN §F (L-5 473344b1 MATCHES; R-L1/R-L2 cite landed R124/R121); handover update; parking»), the branch head:
docs/referee/R-P-N5-CHAIN.md there 289 lines, 29,212 bytes, sha1 9b25eb46357d60cd552c36916d5dfa435483799d; its first 26,881 bytes (l. 1-268)
are 3e02e7c3's file (the first fill's), by prefix test; §F is l. 270-289, with scratch/chain_logs/l5test.out (git show --stat d2678292 names
these two files and notes/REFEREE.md); its byte-test script scratch/chain_l5.py is at 2d25e4db (2d25e4db28528f1a7cb09a8a86127be24559f01c,
2026-11-11T21:07:13Z, «REFEREE successor 30: chain_l5.py (P-N5-CHAIN L-5 prediction 473344b1 = C139)»), 8 seconds before dd83371b. referee-2
fb1ff08c (fb1ff08c980024dded83b91777b016fb888b6b61, 2026-11-11T21:34:25Z, «REFEREE-2 36: R2-P-N5-CHAIN Addendum 6 (L-5 at l-new dd83371b
MATCHES: L-4 + R-U + R-L1 + R-L2 byte-equal 473344b1; R121 / R124 landed, CHAIN3 stays CONDITIONAL)»), the branch head:
docs/referee-2/R2-P-N5-CHAIN.md there 358 lines, 33,465 bytes, sha1 4576fef744ddfd80ce2085fb45c578a17e907b81; its first 30,517 bytes (l.
1-329) are 3c5264e0's file (the first fill's), by prefix test; Addendum 6 is l. 331-358, with R2-P-N5-CHAIN/bt_l5.py and bt_l5.out. checker
4e8654c4 (4e8654c4350bd73267c9d392fb09b1dd5a46ebf8, 2026-11-11T21:06:45Z, «CHECKER C138 CLOSED: CI #7283 green on the R124 landing 8ba1b23b;
resume point after the stall (C139 Add. 1 next)»), the branch head; its parent 389d19f8 (389d19f8b6d55a00b4d6ef9b7d65e42b5e580988,
2026-11-09T10:39:43Z, «CHECKER C139: R125 (P-N5-CHAIN) first fill 81cbdc63 @ a179ef4a on L-4 FAIL E-1 (scope words, UPDATE reading), E-2 …»)
writes docs/checker/C139.md, 103 lines, 12,450 bytes, sha1 d4a0c1f173eb818b4b6873b4b0245ff6677e8ba9, byte-equal at 4e8654c4, sections §1-§6,
no Addendum; 8538284d (C138 Add. 2) is 389d19f8's parent.
TRUNK: THE REAL R124 LANDING (replacing the first fill's simulated base). 8ba1b23b (8ba1b23bbf2f4f760d59f96a335aa167ce2ac99e,
2026-11-09T09:04:36Z, «Lead: LAND R124 (P-N5-END; CHECKER C138 Add. 1 5b9f4af8 PASS) after R123, before Erratum E-1; GAPS line-11 UPDATE;
log») is R124's landing, after f6453111 (the claude/checker merge, C138 Add. 1 5b9f4af8) and a179ef4a (the first fill); git diff a179ef4a
8ba1b23b does not touch docs/agents/R125-draft.md. Origin trunk was 8ba1b23b at my first two fetches and 86f62c26
(86f62c265ea2dbddc9102a99f96c10aa53bf43f8, 2026-11-11T21:06:53Z) at the third; 86f62c26 is 8ba1b23b's child and changes
docs/agents/LEAD-STATE.md only. The local HEAD is 78f49435 (78f4943538d94016b8a985d4aa394d654a4267fe, 2026-11-11T22:11:32Z), not on origin
at my fetches: four Lead merges on 86f62c26, 1bf8d8a0 (claude/l-new 1478886e), 767d62d0 (claude/referee d2678292), aa310460
(claude/referee-2 fb1ff08c) and 78f49435 (claude/checker 4e8654c4), each «premises of the R125 second fill / C139 Add. 1». RESULTS, GAPS and
docs/agents/R125-draft.md are byte-equal at 8ba1b23b, 86f62c26 and 78f49435 (by script). RESULTS at 8ba1b23b: sha1
52e70927c5d851f1586a1e72db285bdae443fc7a, 16,237 lines, 1,477 «|»; «### R121» l. 14320, «### R123» l. 15076, «### R124» l. 15371, its block
to l. 15593, blank l. 15594, the LINE-START «**Erratum E-1** (not a result» l. 15595 (the only one), «**Erratum E-2**» l. 15608, «**Note
E-3**» l. 15636, «## Dead ends (kept;» l. 15667. GAPS: sha1 18ed7db646594ef6628aa8d93bbc055f16bd9232, 23 lines, l. 11 76 «|», 59 «UPDATE
2026-», the last R124's «UPDATE 2026-11-09 09:04Z: RESULTS R124 (P-N5-END; CHECKER C138 5b9f4af8)». «R125», «C139», «P-N5-CHAIN» and
«CHAIN3» occur 0 times in RESULTS and in GAPS. The first fill's simulated base (git archive 98e1c8be + land124.py 09:00 0000000; FIRST FILL
record, BASE) equals the real landing except for the placeholders: its RESULTS with «checker 0000000)» → «checker 5b9f4af8)» is byte-equal
to 8ba1b23b's, and its GAPS with R124's UPDATE head «09:00Z» / «0000000» → «09:04Z» / «5b9f4af8» is byte-equal to 8ba1b23b's (by script). So
every RESULTS line number the first fill cited, R124's l. 15371-15593 included, holds at 8ba1b23b, and the PLACEHOLDER DEPENDENCY the record
names is gone.
ANCESTRY (git merge-base --is-ancestor against 8ba1b23b, origin trunk 86f62c26 and the local HEAD 78f49435): every commit the first fill
named as an ancestor still is (93531b03, 71b75424, 8b67d40e, 219e3933, 87603d07; REFEREE's d49281a7, 36d2932d, 4434597c, b3912f09, b5ac2304,
91334ccd, 3e02e7c3; REFEREE-2's 52d51575, 0e5c7c37, 25f7752b, 09ce14fc, 96d8a3fd, 3c5264e0; CHECKER's 46905772; R121's landing 59dacf22),
and so are a179ef4a and 5b9f4af8. NOT ancestors of origin trunk 86f62c26 (nor of 8ba1b23b), and needed for landing: claude/l-new dd83371b
(fixes entry 4, L-5, mkl5_196.py, the re-pinned chain.pins; the head 1478886e adds box 205 only), claude/referee d2678292 (§F, with
2d25e4db), claude/referee-2 fb1ff08c (Addendum 6) and claude/checker 389d19f8 (C139) with its descendant 4e8654c4 (C138 CLOSED; 8538284d,
C138 Add. 2, before it), and C139 Add. 1's commit when it exists. The L-RED commits the line cites as records (71133de5, e7937985; the
packet's 77b8946b) are still not ancestors; C139 §5 ruled them records, as C138 §5 did. Every one of dd83371b, 1478886e, d2678292, 2d25e4db,
fb1ff08c, 389d19f8, 8538284d and 4e8654c4 IS an ancestor of the local HEAD 78f49435 (the Lead's four merges above). So the merges of
claude/l-new (dd83371b or later), claude/referee (d2678292 or later), claude/referee-2 (fb1ff08c or later) and claude/checker (4e8654c4) are
made locally and are to be pushed; claude/checker is merged again at C139 Add. 1's commit before landing.
WHAT CHANGED SINCE THE FIRST FILL. CHECKER C139 (389d19f8) FAILED the first fill (draft 81cbdc63 at trunk a179ef4a): «Verdict: **FAIL** on
two line-only items (E-1, E-2); the mathematics, DATA, tools and placement PASS» (l. 16). E-1 is the first fill's G-U: «Fix: R-U (§4),
C138's R-U with «P-N5-END» → «P-N5-CHAIN».» (l. 20); E-2 is the first fill's G-S: «so «unlanded», «not landed» and «when landed» are false.
Fix: R-L1, R-L2 (§4), the drafter's strings.» (l. 25). «Both fixes are line-only: no statement, label, hypothesis or DATA number changes
(R-L1 keeps «CONDITIONAL», §3 (i)). With them R125 may land after R124 (Add. 1 on the second fill).» (l. 26-27). C139 ruled the first fill's
other questions: «(i) CHAIN3 keeps «CONDITIONAL» with its premises named as landed RESULTS: yes, no label change.» (l. 30), «(ii)
HUB-ASC-G3's «the last CONDITIONAL on P-N5-ASC §4»: no action.» (l. 35), «(iii) The R124 premise: matches.» (l. 38), «G-2 (Ω_t, Λ_t, Π_t,
TIE(·) unglossed): no action; unlike C138 E-2.» (l. 42), «G-7 / L41: met.» (l. 47) and «Dead-ends row for RUN-TRANSFER: not required (Lead's
file).» (l. 51). L-5 = L-4 + R-U, then R-L1, then R-L2 (fixes entry 4, L-NEW successor 69, dd83371b; «Fixes entry 4 (L-NEW successor 69;
line-only; CHECKER C139, claude/checker 389d19f8, docs/checker/C139.md §2 and §4;», l. 96), as C139 §4 gave it: «**L-5** sha1
**473344b1149d4b44d87bdb917607b618d05d57ce**, 9,047 B,» (l. 68); R-U, R-L1 and R-L2 are the first fill's proposed strings («Equal to the
drafter's.», l. 69). Both referees MATCH L-5: REFEREE successor 30, «Verdict: fixes entry 4 CORRECT. **Line L-5 MATCHES** (L-4 + exactly
R-U, R-L1, R-L2). Statements as signed (§0, §D follow-ups 1-2).» (§F l. 289 at d2678292); REFEREE-2 successor 36, «Verdict: L-5 MATCHES
(fixes entry 4 CORRECT). Nothing REQUIRED is open on my side.» (Add. 6 l. 358 at fb1ff08c). Both read entry 4 as line-only (REFEREE §F
«Fixes entry 4 is line-only: R-U reorders status words; R-L1 and R-L2 replace stale status words by landed R-ids. No statement, label,
hypothesis, proof step or DATA number changes; not L41's case.», l. 287-288; REFEREE-2 Add. 6 «Fixes entry 4, line-only», l. 334) and R-L1 /
R-L2 in meaning against the landed R121 and R124 (REFEREE §F l. 279-286; REFEREE-2 Add. 6 l. 343-355: «Only the status words change. The
theorem, its hypothesis, its bound and its label are as I signed them.»). The UPDATE is the first fill's with C139's three replacements,
«sha1 **f22faed54eeafdff59de062b1ed0294e3acb7ec6** (unfilled, no newline), 9,079 B» as C139 §4 gave it (l. 71), now built by R118's
procedure from L-5 with NO reading. C139's instruction for this fill, «the second fill refreshes the entry block's L-4 references.» (l.
75-76), is met below (Changes at this fill).
Checks run at this fill (scratch r125b/; nothing written into the repository). (a) tools/l5rel125b.py: R-U, R-L1, R-L2 parsed from C139 §4
(l. 58-67, wrapped lines joined with one space) = fixes entry 4's «Line changes» strings (l. 104-113) = mkl5_196.py's tuples (read by ast,
not executed) = the first fill's proposals in r125a/tools/upd125a.py (True ×9); each old string once in the text it is applied to and 0
times after, each new string 0 times before and once after; L-4 + R-U = 62c9c3f4 (9,093 bytes), + R-L1 = fa545618 (9,078 bytes), + R-L2 =
L-5 (True, byte for byte). L-5 = 473344b1149d4b44d87bdb917607b618d05d57ce, 9,047 bytes, one line with its newline, 8,863 characters, 1,472
tokens, 175 «(» / 175 «)», depth never negative, final depth 0, 0 "|", one « — », «unlanded», «not landed», «when landed», «to land» 0 each,
«so this is not M4» once, «; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim» once, «N5′-xi stays a CANDIDATE (D1)»
once, «(2026-11-08)» once, «referee-originated» 2, «signed by both referees» 2, «CONDITIONAL» 3, «HYPOTHESIS» 3, «R124» 2, «R121» 2 (as in
L-4 but «R124» 0 there); token diff L-4 → L-5: 10 hunks, 33 tokens out, 26 in, all inside R-U, R-L1 and R-L2. mkl5_196.py re-run from a copy
of the packet and L-4 of dd83371b (scratch arch_mk/; L-5 not copied): rc 0, «L-5 sha1 473344b1149d4b44d87bdb917607b618d05d57ce 9047 bytes;
parens 175 175», output cmp-equal to L-5. (b) The two check.sh blocks (l. 1039-1054 at dd83371b = tools/blocks196b.sh; the same 16 lines,
sha1 da4acdc2873b1631e8e783b513608dca2016509d, are l. 1036-1051 at 87603d07 and l. 1039-1054 at 1478886e and 8ba1b23b) from a FULL git
archive of dd83371b (r125b/arch/, every path of the tree, 47,620 files), 2026-11-11T22:05:49Z-2026-11-11T22:08:28Z by date -u, rc 0, output
«BOX 196 CHAIN: Γ3-native QUIET3 / REACH3-ALL / UP-B3 counters 0, controls and spec-mode nohoward fire = frozen: PASS» and «P-N5-CHAIN:
packet and 59 pinned files match chain.pins: PASS»; NEGATIVE CONTROL: the «P-N5-CHAIN» block (l. 1048-1054) on the same archive with one
byte appended to L-5 printed «P-N5-CHAIN check: FAILED» and «../../../docs/new/P-N5-CHAIN-line-L5.txt: FAILED», rc 1; L-5 restored (sha1
473344b1…) and the block re-run: PASS, rc 0. (c) tools/upd125b.py: the UPDATE by R118's procedure (the first fill's direct() of upd125a.py,
unchanged) from L-5 with NO reading: sha1 f22faed54eeafdff59de062b1ed0294e3acb7ec6 without newline (849f381106a63593ad9c169bcdd96d437443718e
with it; = C139 §4's UPDATE-5, True), 9,079 bytes, 8,897 characters, 1,471 tokens, 175 «(» / 175 «)», 0 "|", one each of the three fill
tokens, «2026-11-08» 0, « — » 0, «unlanded» / «when landed» / «not landed» 0; = the first fill's d[301] (d7502428…) with «is not M4
(P-N5-CHAIN» → «is not M4, so this is not M4 (P-N5-CHAIN», R-L1 and R-L2 (True; 8 hunks); on L-4 with the landed drops: AssertionError (C139
E-1). CONTROLS on the real trunk 8ba1b23b: R123's constants on R123's L-4 (87603d07) give 739c5f71…, which filled with 2026-11-09, 00:52,
3479ecb0 occurs once on GAPS l. 11 (True); R124's on R124's L-4 (b7faeebe) give 8cd83060… (= C138 §4), which filled with 2026-11-09, 09:04,
5b9f4af8 ends l. 11, the last UPDATE there (True). Token diff L-5 → UPDATE: 26 hunks, 105 tokens out, 104 in (the head; the fifteen labels
behind their clauses, DEAD RUN-TRANSFER's in place of « (2026-11-08) —»; «M4; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a
TARGET.md claim» → «M4»; «§5)» → «§5). G-N5-TIME stays open.»), the hunk kinds of C139 §4 (l. 71-74). (d) tools/chk125b.py (title, block,
UPDATE, pipes, fill tokens, stale grep, quote sweep with a negative control), tools/lp125b.py (quotes new at this fill at their cited
lines), tools/sim125b.py (landing simulation on 8ba1b23b), tools/rec125b.py (the kept sections byte-unchanged; word diff of the entry
against the first fill) and tools/hex125b.py (hex ids): Addendum 2.
NOTES at this fill (for CHECKER; no line change proposed):
- D-1, CHECK.SH AND L-5. At dd83371b experiments/new/check.sh is unchanged (git show --stat dd83371b names four files, not check.sh); the
  «P-N5-CHAIN» block asserts L-5 through chain.pins only (L-5 and mkl5_196.py are pinned rows; the block prints «59 pinned files»), not by
  name as R124's 25e040ee did for its L-4. Fixes entry 4 claims no more: «chain.pins: this file re-pinned; L-5 and mkl5_196.py added.» (l.
  119).
- D-2, STAMPS (history, no verdict affected). C139: «Report 2026-11-09 10:17Z by date -u.» (l. 2), commit 389d19f8 at 10:39:43Z. Fixes entry
  4's heading quotes «Lead 21:09Z 2026-11-11» and «written 2026-11-11 by date -u» (l. 96); dd83371b is stamped 21:07:21Z and REFEREE's
  prediction 2d25e4db 21:07:13Z, both before the 21:09Z of that quote (the Lead's LEAD-STATE at 86f62c26 logs the resume messages
  «21:09-21:10Z RESUME messages to CHECKER 23», l. 3064). REFEREE §F «date -u at writing 2026-11-11T21:35Z» (l. 270), commit 21:35:16Z;
  REFEREE-2 Add. 6 «2026-11-11 by date -u» (l. 331), commit 21:34:25Z; both name «Lead 21:34Z» (l. 271; l. 332 of REFEREE-2's file).
- N-S AT L-5. The source note still names «fixes entries 1-3» and «L-NEW successors 64-65»; entry 4 (successor 69) is line-only (REFEREE §F
  l. 287-288, above; fixes entry 4: «No statement, label, hypothesis, proof or DATA number changes; the packet stays frozen», l. 98). R124
  landed (C138 Add. 1 PASS) with the same shape: its source note names fixes entries 1-2 while entries 3 and 4 were line-only. Honest limits
  (viii) records it.
- N-L41 AT L-5. C139 §3: «G-7 / L41: met.» (l. 47) on L-4; R-U, R-L1 and R-L2 touch neither referee-originated clause (the token diff L-4 →
  L-5 has its 10 hunks inside the three replacements); REFEREE-2 Add. 6: «The W-1 clause (R-W) and the (Q5) step (R-G3) are unchanged in
  L-5, and the three changes touch only the scope tail and the two status sentences.» (l. 356-357); REFEREE §F: «not L41's case» (l. 288).
- D-3, PLACEMENT AS C139 SIMULATED IT. C139 §5 simulated the first fill's block with L-5's title on 8ba1b23b: «R125 15595-15724, Erratum E-1
  15726» (l. 97-98). This fill keeps the block at 130 lines (every change is inside an existing line), so the same places hold (Addendum 2
  (7)).
Changes at this fill, and nothing else: line 1 (the header: the first fill's draft sha1 and C139 verdict, the SECOND FILL clause, to CHECKER
C139 Add. 1, R124 LANDED); this section (new); the title (L-5: R-U, R-L1, R-L2); in the entry (130 lines, as in the first fill): Object
(successors 64-65 and 69; the packet also at dd83371b and 1478886e), Fixes (the file at dd83371b; entry 4 appended to the bullet), The
RESULTS line is (L-5 the line of record; line history L-1 to L-5; the L-5 rounds, REFEREE §F and REFEREE-2 Addendum 6), Claims signed (§F,
Addendum 6; the L-5 re-signatures; CHAIN3's condition as L-5 states it, with C139 §3 (i); C139's E-items taken), Setting (fixes entries 1-4)
and (n) (CHAIN3's premises landed, named by L-5, label kept), L41 and L43 (both clauses unchanged in L-5; C139's G-7 ruling), Honest limits
(viii) (new: N-S at L-5), Data (box196 at dd83371b / 1478886e; this fill's re-run, its negative control; the first fill's and C139's
re-runs), Signatures (§F with 2d25e4db, Addendum 6; successor 69's commit), INDEPENDENCE (the L-5 byte tests), TARGET.md diff (L-5, R123's
and R124's landed form); the GAPS preamble (the real R124 landing; no reading) and the UPDATE (rebuilt from L-5 with no reading); Addendum 2
(new, at the end). The FIRST FILL record (from "FIRST FILL (this text)" to G-T and the L-4 SHAPE line) and the first fill's Addendum are
kept byte-unchanged (rec125b.py): where they call L-4 the title or the line of record, raise G-U or G-S as flags, propose R-U, R-L1 or R-L2,
describe the simulated base (BASE, PLACEHOLDER DEPENDENCY) or give their line numbers, counts, slices, UPDATE sha1 (d7502428…) and block run
(57 pinned files), they describe draft 81cbdc63 at 08:48Z on 2026-11-09; C139 ruled at 10:17Z, and the entry block now follows L-5 and the
real R124 landing (TRUNK above).
FIRST FILL (this text). Built by script (r125a/fill1.py) in the scratchpad r125a/ for the Lead to copy to docs/agents/R125-draft.md; nothing
in the repository was edited, committed, merged or pushed by me, and scripts/push.sh and scripts/verify.sh were not run. Read at the origin
heads of a git fetch of claude/l-new, claude/referee, claude/referee-2, claude/checker and claude/vibrant-johnson-nxvvxo at 2026-11-09T08:35:59Z
by date -u (before and after; its exit code was not captured, the output having been piped to tail), and a second fetch of the same five
branches at 2026-11-09T08:43:28Z-2026-11-09T08:43:29Z: rc 0 (date -u before and after), every head unchanged: l-new 3a492186 (3a4921864083e3de6c2a95bb2f73c1f8afb43301,
2026-11-09T07:50:10Z, «L-NEW 68: BOX 204 — Lemma FACE-TARGET and Theorem EQ (PROVED, lane): a gate's faces carry its W-/Ξ-target movers' classes, so T_CYC is polynomial iff max mover class height is; the k = 1 face question equals T_CYC polynomial at k = 1»), the branch head;
git diff 98e1c8be...3a492186 (the branch's changes since the merge base) names no P-N5-CHAIN file and nothing under experiments/new/box196/
(P-N5-QN, box 203-204 and notes only); on experiments/new/check.sh git diff 98e1c8be 3a492186 shows 16 added lines (a new block), the blocks «BOX 196 CHAIN» and «P-N5-CHAIN» byte-equal (by
script: l. 1036-1051 at 87603d07 and l. 1039-1054 at 98e1c8be and at 3a492186 have the same sha1 da4acdc2873b1631e8e783b513608dca2016509d,
16 lines from «# BOX 196 CHAIN» to the «P-N5-CHAIN» block's «fi»). referee 452800c5 (452800c55384828e52244fcef44144ab3cc923c0, 2026-11-09T07:38:09Z, «REFEREE successor 30: R-P-N5-QN first review (all SIGN; QN-1 wording; LN-1..LN-8; own replay 0 failures; DEAD confirmed)»), the branch head; git diff 98e1c8be...452800c5 names
only docs/referee/R-P-N5-QN.md and seven qn scratch files (qn_*.py, qn_logs/), so docs/referee/R-P-N5-CHAIN.md (268 lines, 26,881 bytes, sha1 f4ba7a1b8113383e0499042f0d5e372ac55f8246) is byte-equal at
98e1c8be, at 3e02e7c3 (its last commit) and at the head. referee-2 5d4f06c2 (5d4f06c2dcf25c2a6723bb398ac7632284f31cb5, 2026-11-09T07:37:31Z, «REFEREE-2 successor 35: R2-P-N5-QN second review (GATE-CLASS, GATE-FLIP, QUIET-N SIGN; (k+1)-Λ SIGN with W-1 wording; DEAD D1-D3 confirmed)»), the branch head (git diff 98e1c8be...5d4f06c2: R2-P-N5-QN.md and R2-P-N5-QN/ only); docs/referee-2/R2-P-N5-CHAIN.md
(329 lines, 30,517 bytes, sha1 7ca5401ace057dc518718cab468656a2932a6629) and R2-P-N5-CHAIN/ are byte-equal at 98e1c8be, 3c5264e0 (the file's last commit) and the head (git diff
empty). checker 46905772 (46905772ddea51544309e7ba62aa3a1ed229349f, 2026-11-09T04:15:52Z), the branch head: «CHECKER C138: R124 (P-N5-END) first fill f7aa004e @ b3c7b461 on L-3 FAIL E-1 (scope words, UPDATE reading), E-2 (τ0 undefined); L-4 5f88c297, UPDATE 8…»; docs/checker/ ends at C138.md; C139.md does not
exist; C138 Add. 1 is not written yet; notes/CHECKER.md l. 16 at 46905772: «Then C138 (R124 P-N5-END), C139 (R125 P-N5-CHAIN)».
LINE OF RECORD (settled from git): docs/new/P-N5-CHAIN-line-L4.txt, COMMIT 87603d07 (87603d07f946a880595dabeff2eef068e3493c72, 2026-11-08T13:19:30Z, «L-NEW 65: P-N5-QUIET fixes entry 4 + L-4 (R-B2); P-N5-CHAIN fixes entry 3 + L-4 (R-G3, R-W, R-B3)»), the file's only
commit; FILE sha1 a69c8aa96fb0b67c6c0a3f6d11670a0b57ba9331 (git show | sha1sum; its blob id is 76920f5c0f3219d5676b65bd3ade8c6fd3e13ebd), 9,082 bytes, one line with its newline.
«a69c8aa9» is not a git object (git rev-parse fails); it is the L-4 FILE sha1, as the Lead's notes say («L-4 a69c8aa9»), and the commit is
87603d07 (the same commit as P-N5-QUIET's fixes entry 4 and L-4 0809da25). LEAD-STATE at 98e1c8be l. 2882 reads it the same way: «CHAIN fixes 3 + L-4 a69c8aa9 (9,082 B) Lead-verified».
PACKET: docs/new/P-N5-CHAIN.md FROZEN at 93531b03 (93531b0368ef938b7ffcd44eb0743796810ea35d, 2026-11-08T08:38:53Z, «L-NEW PACKET P-N5-CHAIN FROZEN (box 196: REACH3-ALL with ESC3-ALL, W3-ALL; Γ3 forms of QUIET / ASC lemmas; CHAIN3 under HYPOTHESIS [E-LEV], conditional on P-N5-…»), the file's only commit (git log on
origin/claude/l-new); sha1 6e613ba762b6ecf67247ef6d8674b4c960013039, 348 lines, 38,551 bytes; byte-equal at 87603d07, 98e1c8be and 3a492186 (VERIFIED: the
Lead's note, frozen at 93531b03, holds). FIXES: docs/new/P-N5-CHAIN-fixes.md at 87603d07 (its last commit): 94 lines, 11,431 bytes, sha1
e823ca09db0b61368841f831d2ae5dd13161acc9; by prefix test its first 6852 bytes are the file at 219e3933 (sha1 cd36b9053c21435df8adcc526690c3aab0707efa), its first 3437 bytes the file at
8b67d40e (sha1 f5d20faf3cdb16bfeab72c4a9b748381c738017a) and its first 1176 bytes the file at 71b75424 (sha1 9e1375d99a976c92b5d62cbb8b764e67708a79e8); git blame: l. 1-11 71b75424 (the «Line L-1» note),
l. 12-31 8b67d40e (entry 1 + L-2), l. 32-62 219e3933 (entry 2 + L-3), l. 63-94 87603d07 (entry 3 + L-4). The Lead's pairing (8b67d40e entry 1 + L-2,
219e3933 entry 2 + L-3, 87603d07 entry 3 + L-4) is VERIFIED. LINES: L-1 bd152dd9 (71b75424, 8,124 B), L-2 e481d260 (8b67d40e, 8,248 B), L-3 c484795c
(219e3933, 8,450 B), L-4 a69c8aa9 (87603d07, 9,082 B); each file has exactly one commit.
REFEREES (git blame of the files at 98e1c8be). REFEREE docs/referee/R-P-N5-CHAIN.md: l. 1-154 the first review 36d2932d (36d2932d07dca6fa5b6d3eb28bc4a32b7a9e1e56, 2026-11-08T09:16:22Z, «REFEREE 29: R-P-N5-CHAIN first review (frozen 93531b03): all SIGN with labels; L-1 NOT YET (CL-1: control sets, ties has no control); notebook»;
blame gives l. 5, 22, 30, 94, 151 to the draft notes d49281a7, identical lines carried over), l. 155-173 §C 4434597c (2026-11-08T10:54:53Z), l. 174-201 §D b3912f09
(b3912f09cfbb8477bc1cbebd8118a9d300963af1, 2026-11-08T12:14:50Z), l. 202-235 §D follow-up b5ac2304 (b5ac230473dd9e382301f76d50612cccdfed83b2, 2026-11-08T12:43:22Z), l. 236-251 §D follow-up 2 91334ccd (91334ccd1a2d084efb393a65779b91b324b596f5, 2026-11-08T13:10:43Z), l. 252-268
§E 3e02e7c3 (3e02e7c33f2b79b06204a86b37421ce4eb593c43, 2026-11-08T13:55:51Z, «REFEREE successor 30: R-P-N5-QUIET §D (L-4 0809da25 MATCHES, after R121) and R-P-N5-CHAIN §E (L-4 a69c8aa9 MATCHES)»). REFEREE-2 docs/referee-2/R2-P-N5-CHAIN.md:
l. 1-263 0e5c7c37 (0e5c7c37b567320d97621914b462c17d94cbfb53, 2026-11-08T11:05:52Z, «REFEREE-2 successor 35: P-N5-END L-3 byte test (Add. 2: MATCHES); P-N5-CHAIN second review (all SIGN, W-1 closed; L-1/L-2 NOT YET: R-1, R-2, R-4)»; the report as first committed), l. 264-283 Add. 1 25f7752b (25f7752bdf67c5190fdb25d6cfc99492cf4df839, 2026-11-08T12:04:27Z), l. 284-305 Add. 2-3
09ce14fc (09ce14fc1183615c884a8a96c4468ee2b79280a0, 2026-11-08T12:32:12Z), l. 306-323 Add. 4 96d8a3fd (96d8a3fd2e69e994fc9498ecfc255fc01be19dd5, 2026-11-08T13:55:42Z, «REFEREE-2 successor 35: P-N5-QUIET L-3/L-4 MATCH (Add. 4); P-N5-CHAIN L-4 MATCHES with attribution caveat (Add. 4)»), l. 324-329 Add. 5 3c5264e0
(3c5264e047c5f4fcee41aa5a61c172ecdda06a2c, 2026-11-08T14:25:57Z, «REFEREE-2 successor 35: R2-P-N5-CHAIN Add. 5 (REFEREE 30 signatures confirmed; L-4 caveat closed)»). REFEREE-2's resume point 52d51575 (2026-11-08T10:36:13Z) committed its findings before reading fixes entry 1 (l. 7-10).
BOTH REFEREES SAY L-4 MATCHES (VERIFIED; the first fact the brief asks for). REFEREE §E (3e02e7c3) l. 268: «Verdict: fixes entry 3 CORRECT. **Line L-4 MATCHES** the packet read with fixes entries 1-3. Statements and labels as in §0.»;
its byte test l. 257-258: «`cmp` with the lane's L-4: **EQUAL** (scratch/chain_logs/l4test.out).». REFEREE-2 Add. 4 (96d8a3fd) l. 311-312: «**L-4 == L-3 + R-G3, R-W, R-B3: True.**»; l. 322:
«Verdict: **L-4 MATCHES** (byte test, and in meaning).», with an attribution caveat (l. 319-323: L-4's two «signed by both referees» clauses true only once REFEREE 30's
signatures are on origin), closed in Add. 5 (3c5264e0) l. 328-329: «**Caveat closed: L-4 MATCHES without condition.**». Both SIGN every statement with its label (Claims signed, below).
ANCESTRY (git merge-base --is-ancestor against origin trunk 98e1c8be): the packet, line and fixes commits 93531b03, 71b75424, 8b67d40e, 219e3933,
87603d07; REFEREE's d49281a7, 36d2932d, 4434597c, b3912f09, b5ac2304, 91334ccd, 3e02e7c3; REFEREE-2's 52d51575, 0e5c7c37, 25f7752b, 09ce14fc, 96d8a3fd,
3c5264e0; CHECKER's C138 46905772; and the R121 landing 59dacf22 are ALL ancestors (True), and every P-N5-CHAIN file is byte-equal at 98e1c8be.
NOT ancestors: the heads l-new 3a492186, referee 452800c5, referee-2 5d4f06c2 (not needed: no P-N5-CHAIN object changed after 87603d07 / 3e02e7c3 /
3c5264e0); the L-RED commits the line cites as records, «cited, not re-run» (71133de5 R223-reach, e7937985 R224-chain; the packet's 77b8946b
R223-q2) — the same status as the L-RED commits of R123 and R124 (C138 §5: records, not premises). So for P-N5-CHAIN NOTHING needs a merge
before landing; what must exist first is R124's landing (C138 Add. 1 on claude/checker, then the Lead's land124.py) and CHECKER C139's commit
(merge claude/checker at it before landing R125, as for C137 and C138).
BASE (simulated, as the brief says): `git archive 98e1c8be` into r125a/base/, then, inside it, `python3 land124.py 09:00 0000000` (rc 0, output «landed
R124 2026-11-09 09:00», kept as land124.out; 09:00 and 0000000 are placeholders for the landing time and the C138 Add. 1 commit; the date is date -u's). Trunk 98e1c8be
(98e1c8bee2e6567f3584d94a9016e4b5a18c879c, 2026-11-09T07:27:06Z, «Lead: R124 second fill (P-N5-END over L-4 5f88c297 @ l-new b7faeebe; both referees MATCH; UPDATE 8cd83060 = C1…»): RESULTS sha1 428bc92f5ddd4167bb8b2bac88eb04cc9de97c19, 16,013 lines, 1,477 «|»; «### R123» l. 15076, the
line-start «**Erratum E-1** (not a result» l. 15371; «### R124» 0 times; GAPS sha1 82e9d475ef5e288f42152fbde61dd1498c4505f0, 23 lines, l. 11 76 «|». Simulated base: RESULTS sha1
d847a9ece28e2eadf8f23128fcc98d0a7941e75c, 16,237 lines (+224), 1,477 «|» (unchanged); «### R124» l. 15371-15593 (blank l. 15594), «**Erratum E-1** (not a result» l. 15595 (the only line-start
occurrence); GAPS sha1 7e08dbf373280c4c4dcc05c92f8911d69205ba56, 23 lines, l. 11 76 «|», its last UPDATE R124's. PLACEHOLDER DEPENDENCY: the base's R124 title ends
«checker 0000000)» and its GAPS UPDATE begins «UPDATE 2026-11-09 09:00Z: RESULTS R124 (P-N5-END; CHECKER C138 0000000)»; these are the only
placeholder bytes. Every RESULTS line number this draft cites below l. 15371 is the same at 98e1c8be and in the base (R124 is inserted after
it); the R124 lines (l. 15371-15593) are R124-draft.md's entry block at 98e1c8be (second fill) and shift only if that block changes. R125's
content quotes R124's ENDGAME-3 clause only (title, l. 15371), never its tail or its UPDATE, so it does not depend on the placeholders; the
simulation's line numbers of R125 and the UPDATE control on GAPS l. 11 do (R124's filled bytes), and the Lead re-measures them at landing.
SOURCES READ: the packet (93531b03): l. 1-95 (head, Scope, To sign, §1 premises, §2), every statement of §3-§8 with §8 in full, §9-§11;
the proofs of §3-§7 were not re-derived by me (both referees did). The fixes file at 87603d07 in full (entries 1-3 and the line notes). L-1 to L-4
(L-4 in full). experiments/new/box196 at 87603d07: check196.sh, check196.out (17 rows), data/sweep196.out (81 lines), ctrl196.out, chain.pins
(57 rows); the check.sh blocks «BOX 196 CHAIN» and «P-N5-CHAIN» (l. 1036-1051 at 87603d07). REFEREE's R-P-N5-CHAIN.md in full (l. 1-268)
and R-P-N5-QUIET.md l. 116-121; REFEREE-2's R2-P-N5-CHAIN.md l. 1-60, 200-329. RESULTS (base) R15 (a) l. 631, R21 (a) l. 933, R104 l. 9864,
R117 l. 13362 and (b)-(f) l. 13425-13445, R118 l. 13607, (b)-(k) l. 13682-13712, l. 13738-13745, R121 l. 14320, R123 (title), R124 (title,
in the base); GAPS l. 11 (base); DECISIONS l. 355-360 (L41); docs/checker/C138.md and C118.md (stale-word rule) at 98e1c8be; P-N5-QUIET
fixes l. 117 (R-L, the stale-word precedent) and its L-1 at 87603d07; SPEC docs/new/N5-ssi-global.md l. 51-54 (A(v)); LEAD-STATE l. 2873,
2882, 2965, 3001; the R124 draft at 98e1c8be (second fill, the model; sha1 c03653ca22b24b6d0cabf1f2a53f5be63c279a69) and at b3c7b461 (first fill, the house form
of a first fill); the tools of r124a/ and r124b/ (adapted).
CHECKS RUN AT THIS FILL (scratch r125a/; outputs there). (a) The check.sh blocks «BOX 196 CHAIN» and «P-N5-CHAIN» (check.sh l. 1036-1051 at
87603d07 = tools/blocks196.sh, run by tools/runblocks.sh) from a FULL git archive of 87603d07 (r125a/arch/, every path of the tree), 2026-11-09T08:41:52Z-2026-11-09T08:44:25Z
by date -u, rc 0, output «BOX 196 CHAIN: Γ3-native QUIET3 / REACH3-ALL / UP-B3 counters 0, controls and spec-mode nohoward fire = frozen: PASS» and «P-N5-CHAIN: packet and 57 pinned files match chain.pins: PASS» (a first attempt that cut the block
one line short, without its closing «fi», printed the first PASS and then a bash syntax error, rc 2: my extraction error, kept as blocks.try1.out).
(b) tools/upd125a.py: the UPDATE by R118's procedure, with two controls (R123's landed UPDATE; R124's 8cd83060 and its filled form on the base's
l. 11), the no-reading attempt (AssertionError), the one-reading build, and the proposal L-5 (FLAGS). (c) tools/data125a.py: L-4's DATA figures
against sweep196.out, check196.out and ctrl196.out (G-9). (d) tools/chk125a.py (title, block, UPDATE, quote sweep with a negative control,
stale grep), tools/lp125a.py (every quote at its cited file, commit and lines, with negative controls), tools/hex125a.py (every hex id) and
tools/sim125a.py (landing simulation on the base): Addendum.
LESSONS APPLIED (R124's fills and C138). C113 E-1 / C123 E-1 / C133 E-1: the title is L-4 verbatim (CLEAN). C133 E-3 / C134 E-3 / C138 E-1:
the scope tail carries the landed status words so R118's procedure runs with no reading (G-U: FLAG). C118 E-1 / C132 E-1 / C138 G-11: no status
word that is stale at landing (G-S: FLAG). C135 E-4 / C138 E-2: every term of a signed clause defined (G-2: notes). L41 / C137 N-L41: a
referee-originated proof step named in the scope tail and signed by both referees (G-7: MET). C134 N-S: the source note names the authors of
proof-bearing text (G-1: CLEAN). C115 E-1: premises landed only (G-4: all landed in the base; R124 needed). C120-C138: every DATA clause against
its counter (G-9). C122 G-0: parentheses (174 / 174). C130 G-P: the UPDATE builder with a control on the last landed UPDATE (R123, and R124 on
the base). C132 Add. 1: block re-run times as a date -u interval.
FLAGS FIRST (G-U and G-S make CHECKER FAIL as L-4 stands, in my reading of the C134 E-3 / C138 E-1 and C118 E-1 / C132 E-1 precedents; both are
line-only in kind; the strings below are PROPOSALS, CHECKER writes the binding ones as C138 §4 did for R124).
- G-U, STATUS WORDS AND THE UPDATE PROCEDURE (FLAG; the C138 E-1 class, word for word). L-4's tail ends «no separate DATA for HUB-ASC-G3 and CHAIN3; G-N5-TIME stays OPEN, N5′-xi stays a CANDIDATE (D1); TARGET.md §2 (M4) asks for an algorithm polynomial on every parity game and §4 says a bound on a restricted class is not M4: not M3, not M4, not a step-4 pass, not a TARGET.md claim (P-N5-CHAIN».
  This is the form C138 E-1 failed in R124's L-3 (C138 l. 19-22: «By C134 E-3 an UPDATE that needs a reading is an E-item: the line must carry the landed words so the procedure runs unchanged.»). R118's procedure with the landed drops
  («; G-N5-TIME stays OPEN», «; not M3, not a step-4 pass, not a TARGET.md claim») stops with an AssertionError on L-4 (upd125a.py (3)). The
  draft's UPDATE is therefore built with ONE READING, the R124 first fill's two drops («G-N5-TIME stays OPEN, » and «: not M3, not M4, not a
  step-4 pass, not a TARGET.md claim»), sha1 d7502428d34fcb6a7cc24434848f0ee9d2ee09ae (upd125a.py (4)). Proposed R-U (C138 §4's R-U with «P-N5-END» → «P-N5-CHAIN»;
  old once in L-4): "; G-N5-TIME stays OPEN, N5′-xi stays a CANDIDATE (D1); TARGET.md §2 (M4) asks for an algorithm polynomial on every parity game
  and §4 says a bound on a restricted class is not M4: not M3, not M4, not a step-4 pass, not a TARGET.md claim (P-N5-CHAIN" → "; N5′-xi stays a
  CANDIDATE (D1); TARGET.md §2 (M4) asks for an algorithm polynomial on every parity game and §4 says a bound on a restricted class is not M4, so
  this is not M4; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim (P-N5-CHAIN". L-4 + R-U alone: sha1 62c9c3f4f914d5183e34bb2ed2bae3d974e7ddc5,
  9,093 bytes; its UPDATE with no reading = the draft's with «is not M4 (P-N5-CHAIN» → «is not M4, so this is not M4 (P-N5-CHAIN» (True).
- G-S, STALE STATUS WORDS (FLAG; the C118 E-1 / C132 E-1 class; C138 G-11 drew the line: «a packet name does not go stale at landing (not a status word, C118 E-1 does not apply)»).
  L-4 was written at 87603d07 (2026-11-08T13:19:30Z), before R121 landed (59dacf22, 2026-11-08T14:06:41Z) and before R124 lands. It has «unlanded» once,
  «not landed» once and «when landed» twice, all about the two premises of CHAIN3 and HUB-ASC-G3: CHAIN3's label «CONDITIONAL on the unlanded lane packets P-N5-END (ENDGAME-3) and P-N5-ASC §4 (its abstract core and F′; RESULTS R121 when landed)» and the premises
  «lane packets, not landed: P-N5-END's Theorem ENDGAME-3 (frozen at l-new 131b4c1c, REFEREE 29 SIGN) for CHAIN3, P-N5-ASC §4's game-free abstract core CS(M) and its constants F′_B (RESULTS R121 when landed) for HUB-ASC-G3 and CHAIN3;». At R125's landing R121 (P-N5-ASC, «Lemma SKELETON and Theorem HUB-ASC(B)», F′_B) is landed (since
  59dacf22) and so is R124 (P-N5-END, ENDGAME-3; base l. 15371), so the three status words are false at landing, as «pending» was in C118 E-1
  («R105 Erratum E-2 «pending», and that goes stale the moment E-2 lands»). Precedent at this very commit: P-N5-QUIET's R-L (87603d07, P-N5-QUIET-fixes l. 117, «C118 E-1 / C132 E-1 (stale status)»):
  «with F′_B of RESULTS R121 (P-N5-ASC, to land first);» → «with F′_B of RESULTS R121 (P-N5-ASC);», landed in R123. PROPOSED (minimal, label kept; each old string once in L-4, by script):
  R-L1 "CONDITIONAL on the unlanded lane packets P-N5-END (ENDGAME-3) and P-N5-ASC §4 (its abstract core and F′; RESULTS R121 when landed))" →
  "CONDITIONAL on P-N5-END's Theorem ENDGAME-3 (RESULTS R124) and P-N5-ASC §4 (its abstract core and F′; RESULTS R121))"; R-L2 "lane packets, not
  landed: P-N5-END's Theorem ENDGAME-3 (frozen at l-new 131b4c1c, REFEREE 29 SIGN) for CHAIN3, P-N5-ASC §4's game-free abstract core CS(M) and its
  constants F′_B (RESULTS R121 when landed) for HUB-ASC-G3 and CHAIN3;" → "RESULTS R124's Theorem ENDGAME-3 (P-N5-END) for CHAIN3, RESULTS R121's
  game-free abstract core CS(M) (Lemma SKELETON, Theorem HUB-ASC(B); P-N5-ASC §4) and its constants F′_B for HUB-ASC-G3 and CHAIN3;". L-5 :=
  L-4 + R-U + R-L1 + R-L2: sha1 473344b1149d4b44d87bdb917607b618d05d57ce, 9,047 bytes, 175 «(» = 175 «)», 0 «|», «unlanded» / «not landed» / «when landed» 0; its UPDATE by
  R118's procedure with the landed drops and NO reading (CHAIN3's label constant updated): sha1 f22faed54eeafdff59de062b1ed0294e3acb7ec6, 9,079 bytes (upd125a.py (5)).
  CHECKER rules: (i) whether «CONDITIONAL» stays in CHAIN3's label once both premises are landed results (R123's ASC-T, on landed R121, reads
  «PROVED» with the premise named), which would be a label change for both referees to re-sign (REFEREE §0 l. 16 signed CHAIN3 «SIGN with that label (it lands only after P-N5-END and R121 land)»;
  REFEREE-2 l. 45 «on P-N5-END (ENDGAME-3) and P-N5-ASC §4, both unlanded»); (ii) whether HUB-ASC-G3's «the last CONDITIONAL on P-N5-ASC §4» (a packet name, no status word) stays;
  (iii) the precise premise R124 supplies: R124's ENDGAME-3 clause (base l. 15371: «N5′-xi, and N5, from S3 on Γ3(G) have exactly one fallback, at an iteration F ≥ 1, and exactly F + 2 iterations») is the packet's [END] (packet l. 72-74: «For every genome G, N5′-xi from S3 on Γ3(G) has exactly one fallback, at an iteration F ≥ 1, and makes exactly F + 2 iterations»).
- G-7, L41 (MET in my reading). L-4 names two referee-originated proof steps in its scope tail, each «signed by both referees»: (1) the (Q5) boundary step,
  «the step β_g ∉ Π(y) for the boundary points y in QUIET3's (Q5) F4′ (an e-face target y of class (w, S ∖ {e}): else S = E(β_g) ⊆ E(y); the pb exit: Π = {K0, K3}; w: Π = ∅) is referee-originated»; signed by REFEREE §D follow-up 2 (91334ccd) l. 250 «Verdict: the Γ3 form of the step is CORRECT; I SIGN it. With REFEREE-2 35's signature it is signed by both referees.» and REFEREE-2 Add. 3 (09ce14fc) l. 305 «SIGN. Verdicts and L-3 MATCHES unchanged.»;
  its first form is REFEREE 28's (R-P-N5-QUIET l. 118-120, 98e1c8be: «A boundary W-target y in class (w, S ∖ {e}) never has a C-vertex β in Π(y).»). (2) The W-1 repair, «(F-cls3)'s convexity and E-MON3's reason hold for non-core vertices, the eight core vertices being constant (referee-originated: REFEREE-2 R2-P-N5-CHAIN W-1, signed by both referees)»;
  REFEREE-2 35 wrote it (report l. 38-40, 0e5c7c37) and REFEREE 30 re-derived and signed it (§D follow-up 1, b5ac2304, l. 230: «Verdict: REFEREE-2's W-1 repair is CORRECT and SUFFICIENT; I sign it.»).
  Both REFEREE (l. 230-235) and the fixes file (l. 64, 75) call each L41's case; fixes entry 3 restates both (l. 65-80). No other referee-written
  proof text in the fixes file: entry 1 (CL-1, CN-1) and entry 2 (R-1, R-2, R-4, N-1) are DATA wording; entry 2's W-1 note is the same repair,
  named through (2). Every referee-originated step the proofs need is named in the line, as L41 asks: yes, both.
- G-1, SOURCE NOTE (CLEAN by C134 N-S in my reading). L-4: «(P-N5-CHAIN, docs/new/P-N5-CHAIN.md, frozen at l-new 93531b03, sha1 6e613ba7, with its fixes entries 1-3, docs/new/P-N5-CHAIN-fixes.md; source box 196, docs/new/N5-CHAIN-box196.md; L-NEW successors 64-65; credit: chain map L-RED 58 R223-q2 §4, F1 / STRICT re-citation R223-reach §3, controls R224-chain §5)». The packet's proofs are
  successor 64's («This packet carries every proof in full, except the game-free abstract core CS(M) of P-N5-ASC §4, cited as a packet.»). Fixes entries by what they carry: entry 1 (successor 65, 8b67d40e): CL-1 (DATA clause), CN-1
  (a reading of §9 DATA), CO-1 not taken — line-only; entry 2 (successor 65, 219e3933): W-1 (a note: REFEREE-2's repair as the reading of the frozen
  text, «Read (F-cls3)'s convexity sentence and E-MON3's reason as restricted to non-core vertices, core vertices being constant.») and R-1, R-2, R-4, N-1 (DATA strings) — carries a proof reading; entry 3 (successor 65, 87603d07):
  the (Q5) boundary step and the W-1 repair restated (proof steps, referee-originated, G-7) and R-G3, R-W, R-B3 (line strings). Entries 2-3 carry
  proof text and are named («fixes entries 1-3», «L-NEW successors 64-65»; R-B3 put them in). Referee authorship is in the scope tail (G-7).
- G-4, PREMISES (the C115 E-1 class): ALL LANDED IN THE SIMULATED BASE, or SPEC text, or literature already cited by landed R118; R124 among them,
  so R125 STRICTLY DEPENDS ON R124's LANDING (and REFEREE l. 141-142: «CHAIN3 and HUB-ASC-G3 can land only after R121 (P-N5-ASC) and, for CHAIN3, after P-N5-END lands.»). Quotes by script, RESULTS lines of the
  base (l. ≤ 15370 equal at 98e1c8be): (1) [DEF] R104 (l. 9864): «Even movers of priority 0; Odd gates of priority 1 with a W-face e and a Ξ-face β»; (2) [1E-N3] R104 l. 9864: «used in two forms: S1's σ̄, and τ̄ on the dual game, are pointwise optima; and S4a's σ_new»;
  (3) [G3] R117 (l. 13362): «obtained from Γ(G) by 4M + 4 single-successor Even pads of priority ≤ 2»; standard state (l. 13429-13430): «the STANDARD STATE of Γ3 for a mover state s is R104's start with the genome start replaced by s, transported»; S3-START (l. 13431): «S3's start pair on Γ3(G) is the standard state of Γ3 for the genome start s_0.»; PAD (a) (l. 13434): «(a) every cycle of Γ3 other than the self-loop of c_X contains a vertex of Ω ≥ 3»; K3 and TAU3 (l. 13438): «(e) The transfer lemmas (§6 l. 157-240) [IDEAL-ACYC; K3 and TAU3 every genome]»; (4) [R117-SIGN], [K2r], [R3C] R118 (l. 13607): «RESULTS R117's entry signs S3-START, PAD, K3 and TAU3 for every genome and ESC3, W3 for acyclic Ξ-graphs», «with σ̄(K2) = r proved for every genome in P-N5-XICYC's fixes», «Theorem REACH3-CYC, CONDITIONAL on P-N5-REACH's S3-START, PAD, K3, TAU3, ESC3, W3 for every genome»; (k) (l. 13705-13706): «T3 is the first state at which no mover has a strictly better successor in Γ3;»; (5) [N5XI] R118 (l. 13744): «with ONE change in S4a»; (6) [TERM] R15 (a) (l. 631): «Lemma A: for any non-empty unambiguous set I of improvements of σ (VJ00 §4.4), Ωσ ⊴ Ω_{Switch_I(σ)}.»; (7) [OPT] R21 (a) (l. 933): «(Odd's best reply σ̄_k is pointwise optimal in G_{σ_k})»; (8) [VJ] R118's premise (l. 13607): «VJ00 §4.2 / Friedmann arXiv 1106.0778 §3»; (9) [ASC] R121 (l. 14320): «(Lemma SKELETON and Theorem HUB-ASC(B)) in the abstract chain system CS(M)» and «F′_0 = F_0 (DESC-POLY on the whole interval), F′_B(M) = (M² + 3M + 1)(1 + M·F′_(B−1)(M)²)»; (10) [END] R124 (base l. 15371): ENDGAME-3, quoted in G-S (iii); (11) SPEC docs/new/N5-ssi-global.md S1-S5 (S4a's A(v), l. 51 at 98e1c8be: «A(v) = {σ(v)} ∪ {w : (v, w) ∈ Iσ} for Even v»).
  NOT LANDED at 98e1c8be: R124 only (it lands first). Not premises: P-N5-QUIET (R123) is a template only («P-N5-QUIET's proofs are templates, none of its statements is a premise»); the L-RED commits are records.
  HYPOTHESIS [E-LEV] is stated in the line, not a premise (as in R121 and R123). Note (CHECKER's call): R117's LINE states S3-START and PAD for
  acyclic Ξ-graphs only while its entry signs them for every genome (the C137 N-G4 / C138 G-4 (ii) rule, no action there); L-4 quotes R118's
  sentence that says so.
- G-2, SYMBOLS (notes, no FLAG in my reading). Defined in L-4: HOW3(G), T3, n3, L3, class_t(v), E_t(v), seq_t(v), D^tot_E(v), U(G); landed:
  Γ3, pads, standard state (R117), ⊴ and the value (Λ, Π, k) (R118's premise VJ00 / Friedmann), Iσ, A(x) (SPEC S4a), F′_B (R121), [N5XI] (R118).
  Used without a gloss in L-4: Ω_t, Λ_t, Π_t, σ̄_t (the value against Odd's optimal counterstrategy at state t; «σ̄_t» is glossed in
  LOC-GATE3's clause; R118 (c) and R121 use Ω_t, Λ_t, Π_t for IDEAL-CYC on Γ(G) in the same sense), TIE(·) (R118's [N5XI]; RESULTS has «TIE(»
  4 times, «with ONE change in S4a» only in R118's line) and xt(g), c_W, c_X (R104 / R117). CHECKER's call (C135 E-4 class); no string proposed.
- G-9, DATA, CLAUSE BY CLAUSE (by tools/data125a.py on the pinned outputs at 87603d07): sweep196.out: 16 xi family rows, 8,000 runs (seeds
  1961, 1962), every fail counter 0, tdiff sum 100; 58 pinned-genome xi rows, every fail counter 0 (and «DEAD_SEGT_n20.json skipped», not a
  genome, as REFEREE §5 noted); max T3 129 (LEAP_k64), longest quiet window 32 (RS2_L32M6), max ascents 4; spec rows rand 599 and dense 911
  nohoward in 200 runs each, seed 1963. check196.out: 17 rows; ctrl1 wfail 32, Tfail 22, upfail 26477; ctrl2 locfail 3320; ctrl3 bonly 2269 (50
  runs each, rand, seed 1963); spec rand 100 runs; 5 pinned genomes in xi mode; every other fail counter 0. ctrl196.out: 15 «CTRL224» rows (75
  controls). EQUAL to L-4's figures. The units were fixed by REFEREE-2's R-1, R-2, R-4 (entry 2; REFEREE §D read the counters in qt3_196.py at
  l. 86-87, 90, 60 and agreed). I did not re-read qt3_196.py's counter code myself (CHECKER's re-check).
- G-6, NAMES. In RESULTS (base) 0 times each: «ESC3-ALL», «W3-ALL», «REACH3-ALL», «HOW3», «CN2-3», «LOC-GATE3», «LOC-K2-3», «B-ONLY3», «NO-TIE3»,
  «QUIET3», «T-QUIET3», «E-MON3», «CHAIN-DECOMP3», «HUB-ASC-G3», «UP-JUMP3», «UP-B3», «CHAIN3», «RUN-TRANSFER», «RT_n1» (True). The «3»-suffixed
  labels are R123's / R121's on Γ3 (R123: CN2, LOC-GATE, LOC-K2, B-ONLY, NO-TIE, QUIET, T-QUIET; R121: E-MON, CHAIN-DECOMP, HUB-ASC-G, UP-JUMP, UP-B).
- G-DE, DEAD ENDS (note). DEAD RUN-TRANSFER is stated inside the line with its instance and obstruction (RT_n1, exact tie, different tie
  rules), as R117's DEAD SUBDIV and R118's DEAD SEG-2P were, which got no Dead-ends row (the last row is DE37). No row proposed; CHECKER's call.
- G-P, PLACEMENT (Lead). R125 goes after R124 (base l. 15371-15593, blank l. 15594), directly before the line-start «**Erratum E-1** (not a result»
  (base l. 15595), its UPDATE after R124's on GAPS l. 11 (the last there in the base). Simulated (sim125a.py): Addendum.
- G-0, THE CHECKER NUMBER. docs/checker/ ends at C138.md (46905772); «C139» 0 times in RESULTS, GAPS, DECISIONS-INDEX; once in NOW and in
  notes/CHECKER.md (l. 16, quoted above). This draft uses C139 (title, UPDATE head), as the brief says.
- G-T, TARGET (note). L-4's scope tail and TARGET clause equal packet §11 in meaning (CHAIN3 a bound for one algorithm on {Γ3(G) : U(G) ≤ B}
  under [E-LEV]; not M3, not M4, not a step-4 pass); TARGET.md §4 «Polynomial only on a restricted class». Nothing bounds a running time.
- (L-4 SHAPE, by script) one line: 9,082 bytes, 8,898 characters with its newline, 174 «(» / 174 «)», 0 «|», one « — », «(2026-11-08)» once,
  «DATA, clause by clause» once, «referee-originated» 2, «signed by both referees» 2, «CONDITIONAL» 3, «HYPOTHESIS» 3, «R124» 0.

### R125 [refereed-only] On Γ3(G) of RESULTS R117 (n3 = N + 7M + 10), for N5′-xi (RESULTS R118's [N5XI]) from SPEC's default start S3, iterations counted as in SPEC S4, and on HOW3(G), the Howard run on Γ3(G) (every non-mover Even vertex frozen at the standard state's choice of P-N5-REACH §3, Odd unrestricted at the gates and K2, every mover moving to a ⊴-best successor and keeping a best current one; T3 := the first state at which no mover has a strictly better successor), for every genome G (Ξ-cycles and Ξ self-loops allowed), each PROVED (every genome): (Lemma ESC3-ALL) in every standard state Iσ ∋ (K0, K1), every pointwise optimum of S4a's arena agrees with σ off the movers, and TIE(β_g) = {xt(g)}, TIE(K0) = {pA}; (Lemma W3-ALL) in every standard state every option of a level-ℓ mover has arena value (c_W, ∅, 5ℓ + 4), no mover is its own arena cycle node and TIE(x) = A(x); (Theorem REACH3-ALL) N5′-xi from S3 on Γ3(G) visits only standard states and its mover parts form a run of HOW3(G) until its first fallback, at iteration T3 + 1, i.e. RESULTS R118 (k)'s Theorem REACH3-CYC («Theorem REACH3-CYC, CONDITIONAL on P-N5-REACH's S3-START, PAD, K3, TAU3, ESC3, W3 for every genome») holds without its condition, the premises ESC3 and W3 being proved here for every genome (RESULTS R118 (k): «RESULTS R117's entry signs S3-START, PAD, K3 and TAU3 for every genome and ESC3, W3 for acyclic Ξ-graphs»); (Facts F1, F3, F4′, F5, F6, DOM, STRICT on HOW3(G)) F1 from RESULTS R15 (a) («Lemma A: for any non-empty unambiguous set I of improvements of σ (VJ00 §4.4), Ωσ ⊴ Ω_{Switch_I(σ)}.»), not from R118 (b); (Lemma CN2-3) for every positional pair and every vertex v other than c_X the cycle node of v's play has priority ≥ 3, so no mover, gate or pad is ever a cycle node or in a set Π; (Lemma LOC-GATE3) at every state and gate g, if the faces pe_g, pβ_g have different values then Odd's optimal counterstrategy σ̄_t picks the strictly ⊴-smaller one; (Lemma LOC-K2-3) σ̄_t(K2) = r and Ω_t(r) ◁ Ω_t(K2) at every state; (Lemma B-ONLY3) at every state and every vertex v other than c_W, the e-vertices whose successor is c_W and their pads pe_g, Λ_t(v) is less relevant than every e-vertex; (Corollary NO-TIE3) Ω_t(pe_g) ≠ Ω_t(pβ_g) at every state and gate; (Theorem QUIET3) with class_t(v) := (Λ_t(v), E_t(v)), E_t(v) the e-vertices of Π_t(v), every maximal window of steps in which no vertex changes class has at most L3 := (M + 1)(2M + 1)(N + 1) + N(n3 − 1) steps; (Corollary T-QUIET3) T3 ≤ (1 + Σ_v (D^tot_E(v) − 1))·(L3 + 1), D^tot_E(v) the number of distinct classes of v over the run, the sum over the n3 vertices; (Lemma E-MON3, Lemma CHAIN-DECOMP3, Corollary HUB-ASC-G3, the last CONDITIONAL on P-N5-ASC §4) P-N5-ASC's game lemmas on HOW3(G), so that if seq_t(v), the e-vertices of Π_t(v) in play order, has at most B ascents for every state then D^tot_E(v) ≤ (2M + 3)·F′_B(M), for every vertex v of Γ3(G); (Lemma UP-JUMP3, Corollary UP-B3, under HYPOTHESIS [E-LEV]: lev(x) < lev(x′) implies pr(e_(x,k)) < pr(e_(x′,k′))) every seq_t(v), for every vertex v including pads and K-vertices, has at most U(G) ascents, U(G) the number of options whose Ξ-target is a mover of higher level; (Theorem CHAIN3, PROVED under HYPOTHESIS [E-LEV] and CONDITIONAL on P-N5-END's Theorem ENDGAME-3 (RESULTS R124) and P-N5-ASC §4 (its abstract core and F′; RESULTS R121)) N5′-xi from S3 on Γ3(G) makes at most T3 + 3 ≤ (1 + n3·((2M + 3)·F′_(U(G))(M) − 1))·(L3 + 1) + 3 iterations, a polynomial in N + M for U(G) ≤ B, B fixed; (DEAD RUN-TRANSFER) T3 is not the IDEAL-CYC count on Γ(G): instance RT_n1 (experiments/new/box196/inst/RT_n1.json, sha1 829f3c97…; N 1, three options, all Ξ self-loops) has T3 = 1 and T_CYC = 2, two options being exactly tied in both games and the tie rules differing (premises, all under the standing SPEC premise 1E-N3 (RESULTS R57 (b)), as in RESULTS R104 / R117: RESULTS R104's definitions of the genome and of Γ(G) only; RESULTS R117's Γ3, standard state, S3-START, PAD (a), K3 and TAU3, signed for every genome; RESULTS R118's σ̄(K2) = r for every genome, [N5XI] and (k)'s proof (P-N5-XICYC §7) re-run with ESC3-ALL and W3-ALL; RESULTS R15 (a); VJ00 §4.2 / Friedmann arXiv 1106.0778 §3 for the value (Λ, Π, k) and its order ⊴; [OPT] for HOW3's σ̄_t = RESULTS R118's σ̄ as used in R118 (b) and RESULTS R21 (a), R57 (b) not used there; in the SPEC run (S4a's arena, REACH3-ALL) [1E-N3] = RESULTS R57 (b) as landed in R104; RESULTS R124's Theorem ENDGAME-3 (P-N5-END) for CHAIN3, RESULTS R121's game-free abstract core CS(M) (Lemma SKELETON, Theorem HUB-ASC(B); P-N5-ASC §4) and its constants F′_B for HUB-ASC-G3 and CHAIN3; P-N5-QUIET's proofs are templates, none of its statements is a premise; HYPOTHESIS [E-LEV] for UP-JUMP3, UP-B3 and CHAIN3 only; not used: PLAY3, SBAR3, KEY3, Fact X, R118 (b)'s F1 and STRICT, any L-RED lemma) (2026-11-08) — this bounds N5′-xi's iteration count on one restricted family, {Γ3(G) : U(G) ≤ B} under [E-LEV], and says nothing about N5 (whose pre-fallback run on Ξ-cyclic genomes is not a Howard run), about genomes with U(G) unbounded (Σ_v D^tot_E(v) stays OPEN), about other games or about general parity games; the degree in M grows like 5·2^B (from P-N5-ASC's F′, not re-checked here) and the per-iteration cost at bit cost is a separate gauntlet step-4 item; the step β_g ∉ Π(y) for the boundary points y in QUIET3's (Q5) F4′ (an e-face target y of class (w, S ∖ {e}): else S = E(β_g) ⊆ E(y); the pb exit: Π = {K0, K3}; w: Π = ∅) is referee-originated (REFEREE R-P-N5-QUIET §3 (Q4), l. 118-120, REFEREE 28, for P-N5-QUIET's form; REFEREE 30 and REFEREE-2 35, R2-P-N5-CHAIN Addendum 3, for the Γ3 form), signed by both referees; (F-cls3)'s convexity and E-MON3's reason hold for non-core vertices, the eight core vertices being constant (referee-originated: REFEREE-2 R2-P-N5-CHAIN W-1, signed by both referees); DATA, clause by clause (unit: runs of N5′-xi, or N5 with Q196_MODE spec, from S3 on Γ3(G) built by box189/gamma3.py, stepped by box190/n5v.py, observed on states 0, …, T3; tool experiments/new/box196/qt3_196.py; scope: gamma3.py's e-priorities by (lev, gate), so [E-LEV] holds; set: box195 eg195.gen families rand, esc, noesc, deep, dense, lvl0, late, acyc × 500 × seeds 1961, 1962, 8,000 runs, plus 58 pinned genomes of box189/corpus, box191-box195/inst and RT_n1, data/sweep196.out; check196.sh, re-run by check.sh: 8 families × 100, seed 1964, controls, spec on 100 runs, and 5 pinned genomes in xi mode, check196.out): REACH3-ALL: nonstd 0 (unit: states), nohoward 0 (unit: (state, mover) pairs); CN2-3: cnlow 0 (unit: (state, vertex) pairs); LOC-GATE3: locfail 0, NO-TIE3: ties 0 (unit: (state, gate) pairs); B-ONLY3: bonly 0 (unit: (state, vertex) pairs); LOC-K2-3: k2fail 0 (unit: states with σ̄_t(K2) ≠ r; the conjunct Ω_t(r) ◁ Ω_t(K2) is not counted); QUIET3: wfail 0 (unit: quiet steps past the L3-th step of their window), crossflip 0 (unit: σ̄ flips on quiet steps at gates whose faces are in different classes), longest quiet window 32 (RS2_L32M6); T-QUIET3: Tfail 0 (unit: runs with T3 > Q + (Q + 1)·L3, Q the number of loud steps; the Σ_v form is not counted); E-MON3: emon 0 (unit: (step, vertex) pairs); UP-B3: upfail 0 (unit: (state, vertex) pairs with more than U(G) ascents), max ascents 4; max T3 129 (LEAP_k64); controls fire (every fail counter except ties, NO-TIE3's counter, which has none): ctrl1 (L3 := 0, U(G) := −1) wfail 32, Tfail 22, upfail 26,477; ctrl2 (order reversed) locfail 3,320; ctrl3 (no excluded vertex) bonly 2,269 (each control on 50 runs, family rand, seed 1963, check196.out); spec mode, seed 1963 (data/sweep196.out), nohoward 599 (rand, 200 runs) and 911 (dense, 200 runs); nonstd, cnlow, k2fail, crossflip and emon by L-RED 58's fault injection (experiments/red/r224/ctrl224.py at claude/l-red e7937985, copied with credit as box196/ctrl196.py, output ctrl196.out): 75 of 75 (genome, counter) controls fire on L-SI's 11 box-85 genomes (box196/inst_si85/) and 4 corpus genomes; record only: tdiff (runs with T3 ≠ T_CYC) 100 of the 8,000 runs; independent checks cited, not re-run: L-RED 58 R223-reach (claude/l-red 71133de5) and R224-chain (claude/l-red e7937985), both SURVIVES; every run is short, so the data test only that nothing exceeds L3, not its tightness; no separate DATA for HUB-ASC-G3 and CHAIN3; N5′-xi stays a CANDIDATE (D1); TARGET.md §2 (M4) asks for an algorithm polynomial on every parity game and §4 says a bound on a restricted class is not M4, so this is not M4; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim (P-N5-CHAIN, docs/new/P-N5-CHAIN.md, frozen at l-new 93531b03, sha1 6e613ba7, with its fixes entries 1-3, docs/new/P-N5-CHAIN-fixes.md; source box 196, docs/new/N5-CHAIN-box196.md; L-NEW successors 64-65; credit: chain map L-RED 58 R223-q2 §4, F1 / STRICT re-citation R223-reach §3, controls R224-chain §5), CHECKER PASS (docs/checker/C139.md, checker PENDING)
- Object (L-NEW successors 64-65 and 69, D1 / D14 / D18, box 196; frozen, unchanged during review): packet P-N5-CHAIN, docs/new/P-N5-CHAIN.md, sha1
  6e613ba762b6ecf67247ef6d8674b4c960013039, 348 lines, 38,551 bytes (l-new 93531b03, 2026-11-08T08:38:53Z, the file's only commit; identical at
  71b75424, 8b67d40e, 219e3933, 87603d07, 3a492186, dd83371b and the l-new head 1478886e; pinned in experiments/new/box196/chain.pins). Both referees measured it
  (REFEREE l. 25 «docs/new/P-N5-CHAIN.md: sha1 6e613ba762b6ecf67247ef6d8674b4c960013039, 38,551 B, 348 lines.»; REFEREE-2 l. 14-15 «Packet docs/new/P-N5-CHAIN.md at 93531b0368ef938b7ffcd44eb0743796810ea35d: sha1 6e613ba762b6ecf67247ef6d8674b4c960013039, 38,551 B»).
  Freeze (l. 2-3): «FREEZE BOX 196 as packet P-N5-CHAIN … statements REACH3-ALL (with ESC3-ALL, W3-ALL), the Γ3 forms, CHAIN3; premises by landed R-id or by packet …, [E-LEV] a HYPOTHESIS; DEAD RUN-TRANSFER RT_n1». Labels (l. 10): «Labels: PROVED (L-NEW 64, unrefereed) / DEAD / DATA / READING (not to sign).».
  To sign (l. 25-38): §3 Lemmas ESC3-ALL, W3-ALL, Theorem REACH3-ALL; §4 Facts F1, F3, F4′, F5, F6, DOM, STRICT on HOW3(G); §5 Lemmas CN2-3,
  LOC-GATE3, LOC-K2-3, B-ONLY3, Corollary NO-TIE3; §6 Theorem QUIET3, Corollary T-QUIET3; §7 Lemmas E-MON3, CHAIN-DECOMP3 (every genome),
  Corollary HUB-ASC-G3 («PROVED, CONDITIONAL on the unlanded packet P-N5-ASC §4 (R121)»), Lemma UP-JUMP3, Corollary UP-B3 (under HYPOTHESIS [E-LEV]); §8 Theorem CHAIN3
  («PROVED, CONDITIONAL on the unlanded packets P-N5-END (ENDGAME-3) and P-N5-ASC §4 (R121)», under HYPOTHESIS [E-LEV]) and DEAD RUN-TRANSFER (instance RT_n1); §9-§11 DATA / READING;
  «Every row is under the standing SPEC premise 1E-N3 (RESULTS R57 (b)), as in RESULTS R104 / R117.» (l. 38). The packet's own scope (l. 11): «This packet is NOT a TARGET.md claim, NOT M3 and NOT M4. It does not decide G-N5-TIME.» Credit (l. 6-9): L-RED 58 attacked it (R223-reach, R224-chain:
  «SURVIVES»); the chain map is L-RED 58's (R223-q2 §4), the F1 / STRICT re-citation R223-reach §3's, the ENDGAME-3 conjecture L-RED 56's.
- Fixes: docs/new/P-N5-CHAIN-fixes.md, append-only (dd83371b: 119 lines, 14,596 bytes, sha1 7b620ce2d0965f286ad9a3cec0c359e7406bbd3d; its first 11,431 bytes are the file at 87603d07 (sha1 e823ca09db0b61368841f831d2ae5dd13161acc9), its first
  6,852 bytes are the file at 219e3933, its first 3,437 bytes the file at 8b67d40e and its first 1,176 bytes the file at 71b75424, by prefix
  test). The «Line L-1» note (71b75424, successor 64, l. 3-11). Entry 1 (8b67d40e, successor 65, l. 13-31; REFEREE 29's first review): CL-1
  (DATA: the control clause names the control and spec sets and excepts ties) and CN-1 (packet §9 read with the ties exception: «NO-TIE3 itself is PROVED (Corollary, §5) and signed; only the DATA sentence about its control is corrected. No statement and no proof changes.»);
  CO-1 not taken (Lead 10:18Z: «CO-1 NOT taken, CN-1 in fixes entry 1: approved.»); «Line L-2» = L-1 + CL-1 by mkl2_196.py. Entry 2 (219e3933, successor 65, l. 33-62; line-only;
  REFEREE-2 35's second review; Lead 11:38Z «take its exact STRINGS (not tool fixes), so no pinned output changes»): the W-1 note (REFEREE-2's repair read into the frozen text, l. 36-47) and R-1, R-2,
  R-4, N-1 (DATA units; «No number changes; no pinned output changes.»); «Line L-3» = L-2 + R-1 + R-2 + R-4 + N-1 by mkl3_196.py. Entry 3 (87603d07, successor 65, l. 64-94; two
  referee-originated proof repairs + line; Lead 13:02Z and 13:12Z, L41): the (Q5) boundary step (l. 65-73, «No statement changes; the packet stays frozen.») and the W-1 repair
  restated (l. 74-80, «restated here because the line now names it (Lead ruling 13:12Z, L41)»); R-G3, R-W, R-B3 (l. 81-89); «Line L-4» = L-3 + R-G3 + R-W + R-B3 by mkl4_196.py (l. 90-94: «a69c8aa96fb0b67c6c0a3f6d11670a0b57ba9331, 9,082 B»). Entry 4 (dd83371b, successor 69, l. 96-119; line-only; CHECKER C139 E-1, E-2; «No statement, label, hypothesis, proof or DATA number changes; the packet stays frozen»): R-U (E-1) and R-L1, R-L2 (E-2), C139 §4's strings (l. 104-113); «Line L-5» = L-4 + R-U + R-L1 + R-L2 by mkl5_196.py (l. 115-118: «473344b1149d4b44d87bdb917607b618d05d57ce, 9,047 B, 175 «(» = 175 «)»: EQUAL to C139 §4's expected L-5»).
  No entry changes a statement or a label; entries 2-3 change no proof's conclusion: they make two steps explicit (REFEREE-2's W-1 case
  split, the (Q5) boundary step), both referee-originated and signed by both referees (L41 below).
- The RESULTS line is L-5, 473344b1149d4b44d87bdb917607b618d05d57ce (docs/new/P-N5-CHAIN-line-L5.txt, l-new dd83371b, 2026-11-11T21:07:21Z, the
  file's only commit; 9,047 bytes). The title is L-5 verbatim, with nothing inserted and nothing stripped (its date parenthesis «(2026-11-08)»,
  its scope tail and its source note are the line's own). L-5's parentheses balance (175 «(» / 175 «)»). Line history: L-1 (bd152dd9, 71b75424,
  by mkl1_196.py), L-2 (e481d260, 8b67d40e, L-1 + CL-1), L-3 (c484795c, 219e3933, L-2 + R-1, R-2, R-4, N-1), L-4 (a69c8aa9, 87603d07, L-3 + R-G3,
  R-W, R-B3), L-5 (473344b1, dd83371b, L-4 + R-U, R-L1, R-L2; C139 §4), each by the lane's mkl*_196.py, which asserts the packet's and the previous line's sha1 and each old string once. REFEREE: L-1 NOT
  YET on CL-1 (36d2932d, l. 18); L-2 MATCHES (§C, 4434597c, l. 170: «**Line L-2 MATCHES** the packet read with fixes entry 1.»); L-3 MATCHES (§D, b3912f09, l. 201: «**Line L-3 MATCHES** the packet read with fixes entries 1-2.»);
  L-4 MATCHES (§E, 3e02e7c3, l. 257-258 and 268, quoted below); L-5 MATCHES (§F, d2678292, l. 289, quoted below). REFEREE-2: L-1 and L-2 NOT YET on R-1, R-2, R-4 (0e5c7c37, l. 47-48); L-3
  MATCHES (Add. 2, 09ce14fc, l. 295: «Verdict: **L-3 MATCHES.** Statement verdicts unchanged.»); L-4 MATCHES (Add. 4, 96d8a3fd, l. 311-312, 322; caveat closed in Add. 5,
  3c5264e0, l. 328-329, quoted below); L-5 MATCHES (Add. 6, REFEREE-2 successor 36, fb1ff08c, l. 358, quoted below).
- Claims signed (REFEREE successor 29: report 36d2932d; successor 30: §C 4434597c, §D b3912f09, §D follow-ups b5ac2304 and 91334ccd, §E 3e02e7c3, §F d2678292;
  REFEREE-2 successor 35: report 0e5c7c37, Add. 1 25f7752b, Add. 2-3 09ce14fc, Add. 4 96d8a3fd, Add. 5 3c5264e0; successor 36: Add. 6 fb1ff08c). REFEREE's table («## 0.
  Verdicts», l. 6-18 of R-P-N5-CHAIN.md) reads «SIGN» on ESC3-ALL, W3-ALL, REACH3-ALL, the HOW3 facts (with F2, CYC), CN2-3, LOC-GATE3, LOC-K2-3,
  B-ONLY3, NO-TIE3, QUIET3, T-QUIET3, E-MON3, CHAIN-DECOMP3; HUB-ASC-G3 «SIGN as conditional on P-N5-ASC §4»; UP-JUMP3, UP-B3 «SIGN under HYPOTHESIS [E-LEV]»; CHAIN3
  «SIGN with that label (it lands only after P-N5-END and R121 land)»; DEAD RUN-TRANSFER «CONFIRMED (own engine: exact tie in both games)»; with «No GAP in any proof.» (l. 19) and «Every row is under the standing SPEC premise 1E-N3 (R57 (b)), as the packet says, which is the convention of R104 / R117.»
  (l. 21). REFEREE-2's table («## Verdicts (Opus 5.5, D1)», l. 26-48 of R2-P-N5-CHAIN.md) reads «SIGN» on ESC3-ALL, W3-ALL, REACH3-ALL, the facts,
  CN2-3, LOC-GATE3, LOC-K2-3, B-ONLY3, NO-TIE3, QUIET3 and T-QUIET3 (note «W-1»), E-MON3, CHAIN-DECOMP3; HUB-ASC-G3 «SIGN as PROVED-CONDITIONAL»
  (l. 42, «on P-N5-ASC §4 (unlanded; R121 when landed)»); UP-JUMP3, UP-B3 «SIGN» «under HYPOTHESIS [E-LEV]»; CHAIN3 «SIGN as PROVED-CONDITIONAL» (l. 45, «under HYPOTHESIS [E-LEV]; on P-N5-END (ENDGAME-3) and P-N5-ASC §4, both unlanded»);
  DEAD RUN-TRANSFER «SIGN (dead)» (l. 46); with «No statement is REFUSED.» and «No gap is left open in any signed proof.» (l. 50). Both re-signed after the line rounds: REFEREE l. 170-172
  (L-2), l. 201 (L-3), l. 268 (L-4: «Statements and labels as in §0.»), l. 289 (L-5: «Statements as signed (§0, §D follow-ups 1-2).»); REFEREE-2 Add. 1 l. 266 «Statement verdicts: EQUAL on every row.», Add. 2 l. 295, Add. 4 l. 323
  «Statement verdicts unchanged.», Add. 6 l. 351 (L-5: «Only the status words change. The theorem, its hypothesis, its bound and its label are as I signed them.»). The CONDITIONAL / HYPOTHESIS statements, with their conditions exactly as the line states them: HUB-ASC-G3 «the last CONDITIONAL on P-N5-ASC §4»;
  UP-JUMP3 and UP-B3 «under HYPOTHESIS [E-LEV]: lev(x) < lev(x′) implies pr(e_(x,k)) < pr(e_(x′,k′))»; CHAIN3 «PROVED under HYPOTHESIS [E-LEV] and CONDITIONAL on P-N5-END's Theorem ENDGAME-3 (RESULTS R124) and P-N5-ASC §4 (its abstract core and F′; RESULTS R121)» (C139 §3 (i): «CHAIN3 keeps «CONDITIONAL» with its premises named as landed RESULTS: yes, no label change.»). The joint gap map: EMPTY (REFEREE «No GAP in any proof.»;
  REFEREE-2 «No gap is left open in any signed proof.»); the two proof-wording defects found in review (W-1, the (Q5) boundary step) were closed by referee-originated steps signed by both
  referees (L41 below); the REQUIRED line items (CL-1; R-1, R-2, R-4) are DATA wording, taken, and C139's E-1 and E-2 (R-U; R-L1, R-L2) status words, taken in L-5. Nothing is REFUSED.
- Setting: Γ3(G) of RESULTS R117 (b) for every genome G of R104 (Ξ-cycles and Ξ self-loops allowed); N5′-xi = R118's [N5XI] from SPEC's default
  start S3; iterations as in SPEC S4; HOW3(G) the Howard run on Γ3(G) with the non-mover Even vertices frozen at the standard state (packet §2).
  Statements as signed (packet with fixes entries 1-4; entries 1-2 and 4 line-only, entry 3 two proof steps made explicit):
  (a) Lemma ESC3-ALL (§3 l. 106-107) [every genome]: «In every standard state: Iσ ∋ (K0, K1), so Iσ ≠ ∅; every pointwise optimum of H agrees with σ at every Even vertex that is not a mover; TIE(β_g) = {xt(g)} for every β_g with xt(g) a mover, and TIE(K0) = {pA}.». REFEREE SIGN (l. 9), REFEREE-2 SIGN (l. 29).
  (b) Lemma W3-ALL (§3 l. 119-) [every genome]: levels 5ℓ + 5 / 4 / 3 / 2 / 1 along a mover's chosen option; the line's form «in every standard state every option of a level-ℓ mover has arena value (c_W, ∅, 5ℓ + 4), no mover is its own arena cycle node and TIE(x) = A(x)».
    REFEREE SIGN (l. 9), REFEREE-2 SIGN (l. 30, «(ii) holds for every pad m_(x,k), not only those in A(x)»).
  (c) Theorem REACH3-ALL (§3 l. 135-136) [every genome]: «For every genome G, the N5′-xi run from S3 on Γ3(G) visits only standard states and its mover parts form a run of HOW3(G) (tie rule: Ξσ-best, then SPEC's choice, then the larger index) until its first fallback, at iteration T3 + 1.». REFEREE SIGN (l. 9), REFEREE-2 SIGN (l. 31, «removes R118 (k)'s condition»).
  (d) Facts F1, F3, F4′, F5, F6, DOM, STRICT on HOW3(G) (§4 l. 149-) [every genome]: F1 by R15 (a), not R118 (b) (§4's heading «R118 (b) not used, after L-RED 58 R223-reach §3»).
    REFEREE SIGN (l. 10), REFEREE-2 SIGN (l. 32).
  (e) Lemma CN2-3 (§5 l. 170-171): «For every positional pair of Γ3(G) and every vertex v ≠ c_X, the cycle node of v's play has Ω ≥ 3; no mover, gate or pad is ever a cycle node or in a set Π.». Both SIGN (l. 11; l. 33).
  (f) Lemma LOC-GATE3 (§5 l. 175): «Let t be a state, g a gate, a := σ̄_t(g) ∈ {pe_g, pβ_g}, b the other face, Ω := Ω_t. If Ω(a) ≠ Ω(b), then Ω(a) ◁ Ω(b).». Both SIGN (l. 11; l. 34).
  (g) Lemma LOC-K2-3 (§5 l. 197): «At every state σ̄_t(K2) = r and Ω_t(r) = (K1, ∅, 1) ◁ Ω_t(K2) = (K1, ∅, 2).». Both SIGN (l. 11; l. 35).
  (h) Lemma B-ONLY3 (§5 l. 201-202): «At every state t and every vertex v other than c_W, the e-vertices whose successor is c_W, and the pads pe_g of those e-vertices, Λ_t(v) is less relevant than every e-vertex.». Both SIGN (l. 11; l. 36).
  (i) Corollary NO-TIE3 (§5 l. 209): «At every state and gate g, Ω_t(pe_g) ≠ Ω_t(pβ_g).». Both SIGN (l. 11; l. 37).
  (j) Theorem QUIET3 (§6 l. 223): «Every quiet window of HOW3(G) has at most L3 := (M + 1)(2M + 1)(N + 1) + N(n3 − 1) steps.»; Corollary T-QUIET3 (l. 224): «T3 ≤ Q + (Q + 1)·L3 ≤ (1 + Σ_v (D^tot_E(v) − 1))·(L3 + 1), the sum over the n3 vertices of Γ3(G).». Both SIGN (l. 12; l. 38-39), on
    the W-1 reading and with the (Q5) boundary step (L41 below).
  (k) Lemma E-MON3 (§7 l. 262): «If Λ_t(v) = Λ_(t+1)(v) then E_t(v) ≤ E_(t+1)(v).»; Lemma CHAIN-DECOMP3 (l. 267): «If seq_t(v) = (f, …), then f's successor y_f is a mover, Λ_t(y_f) = Λ_t(v) and E_t(v) = {f} ∪ E_t(y_f).». Both SIGN (l. 13; l. 40-41).
  (l) Corollary HUB-ASC-G3 (§7 l. 272-274) [CONDITIONAL on P-N5-ASC §4, i.e. R121's HUB-ASC(B) and F′_B]: «For every vertex v (movers, gates, pads, K-vertices, all of Γ3) and every interval I of states of HOW3(G) with Λ_t(v) = w on I: if seq_t(v) has at most B ascents for every t ∈ I, then D_E,I(v) ≤ F′_B(M_w); over the whole run, D^tot_E(v) ≤ (2M + 3)·F′_B(M).».
    REFEREE SIGN as conditional (l. 14), REFEREE-2 SIGN as PROVED-CONDITIONAL (l. 42).
  (m) Lemma UP-JUMP3 and Corollary UP-B3 (§7 l. 281-290) [under HYPOTHESIS [E-LEV]]: UP-B3 «For EVERY vertex v of Γ3 (pads and K-vertices included: UP-JUMP3 is a statement about plays) and every state, seq_t(v) has at most U(G) ascents». Both SIGN under [E-LEV] (l. 15; l. 43-44).
  (n) Theorem CHAIN3 (§8 l. 294-299) [under HYPOTHESIS [E-LEV]; CONDITIONAL on P-N5-END's ENDGAME-3 and P-N5-ASC §4]: «Under HYPOTHESIS [E-LEV], if ENDGAME-3 and P-N5-ASC §4 hold (both lane packets, unlanded), then for every genome G, N5′-xi from S3 on Γ3(G) makes at most» and T3 + 3 ≤
    (1 + n3·((2M + 3)·F′_(U(G))(M) − 1))·(L3 + 1) + 3 iterations; proof REACH3-ALL (F = T3 + 1) + ENDGAME-3 (F + 2) + T-QUIET3 + UP-B3 /
    HUB-ASC-G3. REFEREE SIGN with its label (l. 16), REFEREE-2 SIGN as PROVED-CONDITIONAL (l. 45). Both premises are landed
    (R121 l. 14320, at 59dacf22; R124 l. 15371, at 8ba1b23b); L-5 names them so (R-L1, R-L2; C139 E-2) and keeps the label «CONDITIONAL» (C139 §3 (i)).
  (o) DEAD RUN-TRANSFER (§8 l. 305-308): «The route «T3 equals the IDEAL-CYC count T_CYC on Γ(G), so P-N5-QUIET's bound transfers» is DEAD.»; RT_n1 has T3 = 1 and T_CYC = 2 with options 1 and 2 exactly tied at state 0.
    REFEREE CONFIRMED (l. 17, own engine, exact tie), REFEREE-2 SIGN (dead) (l. 46, T3 = 1, T_CYC = 2 on its own code).
- Premise: as G-4 of the fill record: RESULTS R104 (definitions of the genome and of Γ(G) only), R117 ((b) Γ3 and the standard state, (c)
  S3-START, (d) PAD (a), (e) K3 and TAU3, each [every genome]), R118 (σ̄(K2) = r for every genome, [N5XI], (k)'s proof re-run with ESC3-ALL and
  W3-ALL, its VJ00 / Friedmann premise for ⊴), R15 (a), R21 (a) for HOW3's σ̄_t, [1E-N3] = R57 (b) as landed in R104 for the SPEC run only, R121
  (HUB-ASC(B) on CS(M) and F′_B; for HUB-ASC-G3 and CHAIN3), R124 (ENDGAME-3; for CHAIN3 only), the SPEC text; HYPOTHESIS [E-LEV] for UP-JUMP3,
  UP-B3, CHAIN3. Not used: «PLAY3, SBAR3, KEY3, Fact X, R118 (b)'s F1 and STRICT, any L-RED lemma». Both referees checked the premise quotes
  by script (REFEREE §2 l. 33 «§1: 22 of 22 quotes found verbatim (chain_logs/quotes_sec1.out).»; REFEREE-2 r2q.py, l. 55-58: 29 of 36 verbatim, the 7 misses not premises).
- L41 and L43. The packet's proofs are L-NEW successor 64's (packet l. 5, quoted above), except two steps that are referee-originated and
  named in the line's scope tail, each signed by its author and independently by the other referee (DECISIONS l. 355-360): (1) the (Q5)
  boundary step (first form REFEREE 28, R-P-N5-QUIET l. 118-120; Γ3 form REFEREE-2 35 Add. 3, l. 298-305, and REFEREE 30 §D follow-up 2, l.
  237-250, each SIGN; fixes entry 3 l. 65-73); (2) the W-1 repair ((F-cls3)'s convexity and E-MON3's reason for non-core vertices, the eight core
  vertices constant; REFEREE-2 35 report l. 38-40 and its § W-1, REFEREE 30 §D follow-up 1, l. 203-235, «I sign it.»; fixes entries 2-3).
  REFEREE §E checked both clauses in meaning (l. 261-265); REFEREE-2 Add. 5 confirmed both signatures on origin (l. 326-329). Both clauses are unchanged in L-5 (REFEREE-2 Add. 6: «The W-1 clause (R-W) and the (Q5) step (R-G3) are unchanged in L-5», l. 356-357; C139 §3: «G-7 / L41: met.», l. 47). L43: every
  statement is exact or an explicit bound; DEAD RUN-TRANSFER kills one route, with its instance.
- Not signed: packet §9 (DATA), §10 (machine checks), §11 (TARGET diff and limits), the READING after CHAIN3 (l. 302-303: F′_B's degree
  5·2^B − 3 in M); the L-RED replays (cited); the referees' own DATA.
- Referee strengthening (NOT part of this entry; referee checks): (i) REFEREE: own HOW3 engine and N5′-xi engine (scratch/chain_replay.py,
  end_replay.py), 2,061 runs, 1,580 Ξ-cyclic, every counter 0, max T 129, max W 32 (§4 (A), l. 84-92); controls fire (§4 (B)); check196.sh re-run
  byte-identical at 71b75424 (§4 (D), l. 99-100). (ii) REFEREE-2: own engine, 6,069 runs, every counter 0, maxima equal (Add. 1, l. 282-283);
  t3def 0 (N-2); RT_n1 re-run.
- Honest limits: (i) CHAIN3 bounds the iteration count of one algorithm (N5′-xi from S3) on one family, {Γ3(G) : U(G) ≤ B}, under [E-LEV]; it says
  nothing about N5 (its pre-fallback run on Ξ-cyclic genomes is not a Howard run: spec-mode nohoward 599 / 911), about genomes with U(G) unbounded,
  about other games or about general parity games; nothing bounds a running time or a bit cost. (ii) The bound is loose; its degree in M grows
  like 5·2^B (R121's F′, not re-checked here). (iii) CHAIN3 rests on R124 (ENDGAME-3) and R121 (HUB-ASC(B), F′_B); HUB-ASC-G3 on R121; UP-JUMP3,
  UP-B3, CHAIN3 on HYPOTHESIS [E-LEV], which gamma3.py's e-priorities satisfy and R104 (vi) leaves open (R121's note). (iv) DATA are runs of the
  lane's implementation (box189 gamma3, box190 n5v, box196 qt3_196) and the referees' engines; every run is short (max T3 129), so the DATA test
  only that nothing exceeds L3. (v) T3 is HOW3's own count, not the IDEAL-CYC count T_CYC of R118 / R123 (DEAD RUN-TRANSFER). (vi) Names: the
  «3»-suffixed labels, «HOW3», «CHAIN3» and «RUN-TRANSFER» are new to RESULTS (G-6). (vii) Literature: VJ00 §4.2 / §4.4 and Friedmann arXiv
  1106.0778 §3 as in R15 / R118; no novelty is claimed. (viii) The line's source note names «fixes entries 1-3» and «L-NEW successors 64-65»; fixes entry 4 (successor 69) is line-only (REFEREE §F: «Fixes entry 4 is line-only», l. 287) and carries no proof text, so the note does not name it (the C134 N-S rule; R124 landed with its line-only entries 3-4 unnamed in the same way).
- Data (DATA, not proof): experiments/new/box196/ at l-new 87603d07 (tools, outputs and data unchanged to dd83371b and 1478886e; dd83371b adds mkl5_196.py and re-pins chain.pins, 59 rows): qt3_196.py run by check196.sh (8 families × 100,
  seed 1964; ctrl1-3 on rand, seed 1963, 50 runs; spec on 100 runs; 5 pinned genomes in xi mode), its frozen output check196.out (17 lines); the
  record sweep data/sweep196.out (8 families × 500 × seeds 1961, 1962 = 8,000 runs, 58 pinned genomes, spec rows rand / dense 200 runs, seed
  1963); ctrl196.out (L-RED 58's ctrl224, 75 controls, copied with credit); called from the check.sh blocks «BOX 196 CHAIN» and «P-N5-CHAIN»
  (experiments/new/check.sh l. 1036-1051 at 87603d07, l. 1039-1054 at 98e1c8be, dd83371b, 1478886e and 8ba1b23b, the same 16 lines), run by scripts/verify.sh. Re-run by the drafter from a full
  git archive of dd83371b: 2026-11-11T22:05:49Z-2026-11-11T22:08:28Z, rc 0, «BOX 196 CHAIN: Γ3-native QUIET3 / REACH3-ALL / UP-B3 counters 0, controls and spec-mode nohoward fire = frozen: PASS» and «P-N5-CHAIN: packet and 59 pinned files match chain.pins: PASS»; with one byte appended to L-5 the «P-N5-CHAIN» block printed «P-N5-CHAIN check: FAILED», rc 1 (negative control). The same blocks at 87603d07: rc 0 at 2026-11-09T08:41:52Z-2026-11-09T08:44:25Z (drafter, 57 pinned files) and by CHECKER C139 (§5 l. 82-84: «10:13:21Z-10:15:59Z, rc 0»).
  Frozen totals (by script, data125a.py): sweep 8,000 xi runs, every fail counter 0, tdiff 100; 58 genome rows, every fail counter 0; max T3 129
  (LEAP_k64), longest quiet window 32 (RS2_L32M6), max ascents 4; ctrl1 wfail 32, Tfail 22, upfail 26,477; ctrl2 locfail 3,320; ctrl3 bonly 2,269;
  spec nohoward 599 (rand) and 911 (dense); ctrl196 15 rows. REFEREE re-ran check196.sh (§4 (D)); REFEREE-2 re-summed sweep196.out (l. 259).
- Signatures: REFEREE docs/referee/R-P-N5-CHAIN.md: successor 29's report 36d2932d (36d2932d07dca6fa5b6d3eb28bc4a32b7a9e1e56, 2026-11-08T09:16:22Z) («Independent: docs/referee-2/ not read», l. 2),
  verdict table l. 6-21; successor 30's §C 4434597c (4434597c947e8bca85792c10d49a1069b9a795ac, 2026-11-08T10:54:53Z) l. 156-173, «**Line L-2 MATCHES**» (l. 170); §D b3912f09
  (b3912f09cfbb8477bc1cbebd8118a9d300963af1, 2026-11-08T12:14:50Z) l. 175-201, «**Line L-3 MATCHES**» (l. 201); §D follow-up b5ac2304 (b5ac230473dd9e382301f76d50612cccdfed83b2, 2026-11-08T12:43:22Z) l. 203-235, W-1 signed (l. 230);
  §D follow-up 2 91334ccd (91334ccd1a2d084efb393a65779b91b324b596f5, 2026-11-08T13:10:43Z) l. 237-251, the Γ3 (Q5) step signed (l. 250); §E 3e02e7c3 (3e02e7c33f2b79b06204a86b37421ce4eb593c43, 2026-11-08T13:55:51Z) l. 253-268,
  «**Line L-4 MATCHES**» (l. 268); §F d2678292 (d2678292247a2778ded5b0e0c7a9f93ce9973de4, 2026-11-11T21:35:16Z) l. 270-289, «Verdict: fixes entry 4 CORRECT. **Line L-5 MATCHES** (L-4 + exactly R-U, R-L1, R-L2). Statements as signed (§0, §D follow-ups 1-2).» (l. 289), its chain_l5.py committed at 2d25e4db (2d25e4db28528f1a7cb09a8a86127be24559f01c, 2026-11-11T21:07:13Z) before the lane's L-5: «My prediction (committed 2d25e4db before the lane's L-5 existed) was the same sha1.» (l. 276). REFEREE-2 docs/referee-2/R2-P-N5-CHAIN.md: successor 35's report 0e5c7c37 (0e5c7c37b567320d97621914b462c17d94cbfb53, 2026-11-08T11:05:52Z) («Independent: docs/referee/R-P-N5-CHAIN.md (REFEREE 29) NOT read before this report is committed.», l. 2-3),
  verdict table l. 26-48; Add. 1 25f7752b (25f7752bdf67c5190fdb25d6cfc99492cf4df839, 2026-11-08T12:04:27Z) l. 265-283, read after 0e5c7c37 was on origin (l. 265); Add. 2-3 09ce14fc
  (09ce14fc1183615c884a8a96c4468ee2b79280a0, 2026-11-08T12:32:12Z) l. 285-305, «**L-3 MATCHES.**» (l. 295), the (Q5) step SIGN (l. 305); Add. 4 96d8a3fd (96d8a3fd2e69e994fc9498ecfc255fc01be19dd5, 2026-11-08T13:55:42Z) l. 307-323,
  «**L-4 MATCHES**» (l. 322); Add. 5 3c5264e0 (3c5264e047c5f4fcee41aa5a61c172ecdda06a2c, 2026-11-08T14:25:57Z) l. 325-329, caveat closed (l. 328-329); successor 36's Add. 6 fb1ff08c (fb1ff08c980024dded83b91777b016fb888b6b61, 2026-11-11T21:34:25Z) l. 331-358, «Verdict: L-5 MATCHES (fixes entry 4 CORRECT). Nothing REQUIRED is open on my side.» (l. 358). Lane (claude/l-new): L-NEW successor
  64, 93531b03 (packet FROZEN) and 71b75424 (L-1); successor 65, 8b67d40e (entry 1, L-2), 219e3933 (entry 2, L-3), 87603d07 (entry 3, L-4); successor 69, dd83371b (entry 4, L-5).
- INDEPENDENCE: each referee wrote its first report without reading the other's (REFEREE l. 2-3; REFEREE-2 l. 2-3), with the disclosures REFEREE-2
  makes (l. 5-11: the fixes entry 1 outline of REFEREE 29's verdicts, read after its own findings were committed at 52d51575); REFEREE-2 compared
  afterwards (Add. 1). The two referee-originated steps are each signed by their author and re-derived by the other referee (L41 above); REFEREE 30
  re-derived W-1 from the frozen text and REFEREE-2's witness (l. 203-235). Each referee byte-tested L-4 with its own script (REFEREE §E
  chain_l4.py, strings typed from fixes entry 3's table, l. 256; REFEREE-2 Add. 4 bt_l34.py, reading mkl4_196.py's list by ast, l. 310), and L-5 likewise (REFEREE §F chain_l5.py «with the strings typed from C139 §4 (claude/checker 389d19f8; wrapped lines joined with one space), not from the lane's script», l. 273-274; REFEREE-2 Add. 6 bt_l5.py parses fixes entry 4's bullets: «It does not run the lane generator.», l. 337). L-RED 58's
  R223 / R224 were context only at both (REFEREE §8 read after its verdict; REFEREE-2 l. 3-4).
- TARGET.md diff: TARGET.md §2 (M4) asks for one algorithm, polynomial on EVERY parity game, that outputs (W_E, W_O); CHAIN3 is a polynomial
  iteration bound for one algorithm on one restricted family under a hypothesis (TARGET.md §4: «Polynomial only on a restricted class»; packet
  §11 l. 345-347; REFEREE §6 «CHAIN3 is an iteration bound for one algorithm on {Γ3(G) : U(G) ≤ B} under a HYPOTHESIS and two unlanded premises.»; REFEREE-2 «So it is not M4 and not a step-4 pass. G-N5-TIME stays OPEN and N5′-xi stays a CANDIDATE (D1).»).
  It is not an algorithm claim on every game, so TARGET.md §5's gauntlet does not apply, and it is not a step-4 pass. L-5 carries «N5′-xi stays a
  CANDIDATE (D1)» once and ends its scope words «so this is not M4; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim», the form of landed R123 and R124 (R-U, C139 E-1). GAPS
  G-N5-TIME: open.

Proposed GAPS line-11 UPDATE (append-only), to go AFTER the last UPDATE on GAPS l. 11 at landing (R124's, «UPDATE 2026-11-09 09:04Z: RESULTS
R124 (P-N5-END; CHECKER C138 5b9f4af8)», the last at 8ba1b23b and at origin trunk 86f62c26), as a pure insertion with one separating space
before the row's closing « |». BUILT FROM L-5 by tools/upd125b.py (R118's procedure: the direct build of r125a/tools/upd125a.py, unchanged,
with R125's constants: date «(2026-11-08)», start «for every genome G (Ξ-cycles and Ξ self-loops allowed), each PROVED (every genome): »,
its fifteen labels with CHAIN3's as in L-5, source prefix «(P-N5-CHAIN, docs/new/P-N5-CHAIN.md»), with NO reading; controls on 8ba1b23b: the
same function rebuilds R123's landed UPDATE from R123's L-4 (739c5f71… unfilled; filled with 2026-11-09, 00:52, 3479ecb0 it occurs once on
l. 11: True) and R124's from R124's L-4 (8cd83060…; filled with 2026-11-09, 09:04, 5b9f4af8 it ends l. 11: True); sha1
f22faed54eeafdff59de062b1ed0294e3acb7ec6 of the line without newline and unfilled, = C139 §4's UPDATE-5 (True). <DATE>, <HH:MM> and
<checker> are the landing date, time and the CHECKER commit of the PASS (C139 Add. 1), all filled at landing:
UPDATE <DATE> <HH:MM>Z: RESULTS R125 (P-N5-CHAIN; CHECKER C139 <checker>) [refereed-only] LANDED: On Γ3(G) of RESULTS R117 (n3 = N + 7M + 10), for N5′-xi (RESULTS R118's [N5XI]) from SPEC's default start S3, iterations counted as in SPEC S4, and on HOW3(G), the Howard run on Γ3(G) (every non-mover Even vertex frozen at the standard state's choice of P-N5-REACH §3, Odd unrestricted at the gates and K2, every mover moving to a ⊴-best successor and keeping a best current one; T3 := the first state at which no mover has a strictly better successor), for every genome G (Ξ-cycles and Ξ self-loops allowed), each PROVED (every genome): in every standard state Iσ ∋ (K0, K1), every pointwise optimum of S4a's arena agrees with σ off the movers, and TIE(β_g) = {xt(g)}, TIE(K0) = {pA} (Lemma ESC3-ALL); in every standard state every option of a level-ℓ mover has arena value (c_W, ∅, 5ℓ + 4), no mover is its own arena cycle node and TIE(x) = A(x) (Lemma W3-ALL); N5′-xi from S3 on Γ3(G) visits only standard states and its mover parts form a run of HOW3(G) until its first fallback, at iteration T3 + 1, i.e. RESULTS R118 (k)'s Theorem REACH3-CYC («Theorem REACH3-CYC, CONDITIONAL on P-N5-REACH's S3-START, PAD, K3, TAU3, ESC3, W3 for every genome») holds without its condition, the premises ESC3 and W3 being proved here for every genome (RESULTS R118 (k): «RESULTS R117's entry signs S3-START, PAD, K3 and TAU3 for every genome and ESC3, W3 for acyclic Ξ-graphs») (Theorem REACH3-ALL); F1 from RESULTS R15 (a) («Lemma A: for any non-empty unambiguous set I of improvements of σ (VJ00 §4.4), Ωσ ⊴ Ω_{Switch_I(σ)}.»), not from R118 (b) (Facts F1, F3, F4′, F5, F6, DOM, STRICT on HOW3(G)); for every positional pair and every vertex v other than c_X the cycle node of v's play has priority ≥ 3, so no mover, gate or pad is ever a cycle node or in a set Π (Lemma CN2-3); at every state and gate g, if the faces pe_g, pβ_g have different values then Odd's optimal counterstrategy σ̄_t picks the strictly ⊴-smaller one (Lemma LOC-GATE3); σ̄_t(K2) = r and Ω_t(r) ◁ Ω_t(K2) at every state (Lemma LOC-K2-3); at every state and every vertex v other than c_W, the e-vertices whose successor is c_W and their pads pe_g, Λ_t(v) is less relevant than every e-vertex (Lemma B-ONLY3); Ω_t(pe_g) ≠ Ω_t(pβ_g) at every state and gate (Corollary NO-TIE3); with class_t(v) := (Λ_t(v), E_t(v)), E_t(v) the e-vertices of Π_t(v), every maximal window of steps in which no vertex changes class has at most L3 := (M + 1)(2M + 1)(N + 1) + N(n3 − 1) steps (Theorem QUIET3); T3 ≤ (1 + Σ_v (D^tot_E(v) − 1))·(L3 + 1), D^tot_E(v) the number of distinct classes of v over the run, the sum over the n3 vertices (Corollary T-QUIET3); P-N5-ASC's game lemmas on HOW3(G), so that if seq_t(v), the e-vertices of Π_t(v) in play order, has at most B ascents for every state then D^tot_E(v) ≤ (2M + 3)·F′_B(M), for every vertex v of Γ3(G) (Lemma E-MON3, Lemma CHAIN-DECOMP3, Corollary HUB-ASC-G3, the last CONDITIONAL on P-N5-ASC §4); every seq_t(v), for every vertex v including pads and K-vertices, has at most U(G) ascents, U(G) the number of options whose Ξ-target is a mover of higher level (Lemma UP-JUMP3, Corollary UP-B3, under HYPOTHESIS [E-LEV]: lev(x) < lev(x′) implies pr(e_(x,k)) < pr(e_(x′,k′))); N5′-xi from S3 on Γ3(G) makes at most T3 + 3 ≤ (1 + n3·((2M + 3)·F′_(U(G))(M) − 1))·(L3 + 1) + 3 iterations, a polynomial in N + M for U(G) ≤ B, B fixed (Theorem CHAIN3, PROVED under HYPOTHESIS [E-LEV] and CONDITIONAL on P-N5-END's Theorem ENDGAME-3 (RESULTS R124) and P-N5-ASC §4 (its abstract core and F′; RESULTS R121)); T3 is not the IDEAL-CYC count on Γ(G): instance RT_n1 (experiments/new/box196/inst/RT_n1.json, sha1 829f3c97…; N 1, three options, all Ξ self-loops) has T3 = 1 and T_CYC = 2, two options being exactly tied in both games and the tie rules differing (premises, all under the standing SPEC premise 1E-N3 (RESULTS R57 (b)), as in RESULTS R104 / R117: RESULTS R104's definitions of the genome and of Γ(G) only; RESULTS R117's Γ3, standard state, S3-START, PAD (a), K3 and TAU3, signed for every genome; RESULTS R118's σ̄(K2) = r for every genome, [N5XI] and (k)'s proof (P-N5-XICYC §7) re-run with ESC3-ALL and W3-ALL; RESULTS R15 (a); VJ00 §4.2 / Friedmann arXiv 1106.0778 §3 for the value (Λ, Π, k) and its order ⊴; [OPT] for HOW3's σ̄_t = RESULTS R118's σ̄ as used in R118 (b) and RESULTS R21 (a), R57 (b) not used there; in the SPEC run (S4a's arena, REACH3-ALL) [1E-N3] = RESULTS R57 (b) as landed in R104; RESULTS R124's Theorem ENDGAME-3 (P-N5-END) for CHAIN3, RESULTS R121's game-free abstract core CS(M) (Lemma SKELETON, Theorem HUB-ASC(B); P-N5-ASC §4) and its constants F′_B for HUB-ASC-G3 and CHAIN3; P-N5-QUIET's proofs are templates, none of its statements is a premise; HYPOTHESIS [E-LEV] for UP-JUMP3, UP-B3 and CHAIN3 only; not used: PLAY3, SBAR3, KEY3, Fact X, R118 (b)'s F1 and STRICT, any L-RED lemma) (DEAD RUN-TRANSFER): this bounds N5′-xi's iteration count on one restricted family, {Γ3(G) : U(G) ≤ B} under [E-LEV], and says nothing about N5 (whose pre-fallback run on Ξ-cyclic genomes is not a Howard run), about genomes with U(G) unbounded (Σ_v D^tot_E(v) stays OPEN), about other games or about general parity games; the degree in M grows like 5·2^B (from P-N5-ASC's F′, not re-checked here) and the per-iteration cost at bit cost is a separate gauntlet step-4 item; the step β_g ∉ Π(y) for the boundary points y in QUIET3's (Q5) F4′ (an e-face target y of class (w, S ∖ {e}): else S = E(β_g) ⊆ E(y); the pb exit: Π = {K0, K3}; w: Π = ∅) is referee-originated (REFEREE R-P-N5-QUIET §3 (Q4), l. 118-120, REFEREE 28, for P-N5-QUIET's form; REFEREE 30 and REFEREE-2 35, R2-P-N5-CHAIN Addendum 3, for the Γ3 form), signed by both referees; (F-cls3)'s convexity and E-MON3's reason hold for non-core vertices, the eight core vertices being constant (referee-originated: REFEREE-2 R2-P-N5-CHAIN W-1, signed by both referees); DATA, clause by clause (unit: runs of N5′-xi, or N5 with Q196_MODE spec, from S3 on Γ3(G) built by box189/gamma3.py, stepped by box190/n5v.py, observed on states 0, …, T3; tool experiments/new/box196/qt3_196.py; scope: gamma3.py's e-priorities by (lev, gate), so [E-LEV] holds; set: box195 eg195.gen families rand, esc, noesc, deep, dense, lvl0, late, acyc × 500 × seeds 1961, 1962, 8,000 runs, plus 58 pinned genomes of box189/corpus, box191-box195/inst and RT_n1, data/sweep196.out; check196.sh, re-run by check.sh: 8 families × 100, seed 1964, controls, spec on 100 runs, and 5 pinned genomes in xi mode, check196.out): REACH3-ALL: nonstd 0 (unit: states), nohoward 0 (unit: (state, mover) pairs); CN2-3: cnlow 0 (unit: (state, vertex) pairs); LOC-GATE3: locfail 0, NO-TIE3: ties 0 (unit: (state, gate) pairs); B-ONLY3: bonly 0 (unit: (state, vertex) pairs); LOC-K2-3: k2fail 0 (unit: states with σ̄_t(K2) ≠ r; the conjunct Ω_t(r) ◁ Ω_t(K2) is not counted); QUIET3: wfail 0 (unit: quiet steps past the L3-th step of their window), crossflip 0 (unit: σ̄ flips on quiet steps at gates whose faces are in different classes), longest quiet window 32 (RS2_L32M6); T-QUIET3: Tfail 0 (unit: runs with T3 > Q + (Q + 1)·L3, Q the number of loud steps; the Σ_v form is not counted); E-MON3: emon 0 (unit: (step, vertex) pairs); UP-B3: upfail 0 (unit: (state, vertex) pairs with more than U(G) ascents), max ascents 4; max T3 129 (LEAP_k64); controls fire (every fail counter except ties, NO-TIE3's counter, which has none): ctrl1 (L3 := 0, U(G) := −1) wfail 32, Tfail 22, upfail 26,477; ctrl2 (order reversed) locfail 3,320; ctrl3 (no excluded vertex) bonly 2,269 (each control on 50 runs, family rand, seed 1963, check196.out); spec mode, seed 1963 (data/sweep196.out), nohoward 599 (rand, 200 runs) and 911 (dense, 200 runs); nonstd, cnlow, k2fail, crossflip and emon by L-RED 58's fault injection (experiments/red/r224/ctrl224.py at claude/l-red e7937985, copied with credit as box196/ctrl196.py, output ctrl196.out): 75 of 75 (genome, counter) controls fire on L-SI's 11 box-85 genomes (box196/inst_si85/) and 4 corpus genomes; record only: tdiff (runs with T3 ≠ T_CYC) 100 of the 8,000 runs; independent checks cited, not re-run: L-RED 58 R223-reach (claude/l-red 71133de5) and R224-chain (claude/l-red e7937985), both SURVIVES; every run is short, so the data test only that nothing exceeds L3, not its tightness; no separate DATA for HUB-ASC-G3 and CHAIN3; N5′-xi stays a CANDIDATE (D1); TARGET.md §2 (M4) asks for an algorithm polynomial on every parity game and §4 says a bound on a restricted class is not M4, so this is not M4 (P-N5-CHAIN, docs/new/P-N5-CHAIN.md, frozen at l-new 93531b03, sha1 6e613ba7, with its fixes entries 1-3, docs/new/P-N5-CHAIN-fixes.md; source box 196, docs/new/N5-CHAIN-box196.md; L-NEW successors 64-65; credit: chain map L-RED 58 R223-q2 §4, F1 / STRICT re-citation R223-reach §3, controls R224-chain §5). G-N5-TIME stays open.

Addendum (subagent, first fill; checks run on the pass-1 draft, whose title, entry block, GAPS preamble and UPDATE are byte-equal to this
file's; outputs r125a/*_p1.out; the final run on this file is r125a/*_final.out). Verbatim key lines, with «|» printed as «¦»:
  [chk] model: R124 title (98e1c8be) == «### R124 [refereed-only] » + R124 L-4 + «, CHECKER PASS (docs/checker/C138.md, checker PENDING)»: True
  [chk] file: sha1 d58dc487b0d185a8974fb808a75ba940a32ef860 bytes 71451 lines 303 ends with newline True
  [chk] ### R headings at d[...]: [161]
  [chk] (a) title == prefix + L-4 (no newline) + tail: True ; middle bytes == L-4 bytes without newline: True
  [chk]     title: 8976 chars, 9160 bytes, sha1 2939f69f5c8e181a2cbfb89f6946bafa654da1c1, ( 175 ) 175, min depth 0, final 0, ¦ 0, «checker PENDING)» 1
  [chk] (e) entry block d[161:291] (lines 162-291, 130 lines, sha1 of the joined block 04b0869bd864ffc94562904a50f4b33e9666890a); next line blank: True; line after: 'Proposed GAPS line-11 UPDATE (append-onl'
  [chk] (b) «checker PENDING)» in the entry block: 1 ; in the whole file: 1 at lines [162]
  [chk]     «\n**Erratum E-1** (not a result» in the block: False ; «**Erratum E-1**» in the block: 0 ; in the file: 3
  [chk] (e) UPDATE line(s) at d[...]: [301] (line [302])
  [chk]     GAPS preamble(s) at d[...]: [292] -> d[292:301]
  [chk] (c) "¦" in entry block: 0 ; in UPDATE: 0 ; in GAPS preamble: 1 (the quoted « ¦» of the row end); in the file: 8
  [chk] (d) UPDATE <DATE> 1 <HH:MM> 1 <checker> 1; head at its start: True
  [chk]     UPDATE = upd125L4.txt: True ; sha1 (no newline) d7502428d34fcb6a7cc24434848f0ee9d2ee09ae ; with newline 540bb0b76f592dfb5d16642d94745e8d01eebff9 ; 9106 bytes 8924 chars ( 174 ) 174
  [chk]     stale grep, entry block minus title (case-insensitive): {'pending': 0, 'will ': 0, 'awaiting': 0, 'to come': 0, 'not landed': 0, 'unlanded': 8, 'when landed': 2, 'first fill': 0, 'second fill': 0, 'not yet': 1, 'this fill': 0, 'to land': 0, 'open item': 0}
  [chk]     stale grep, title: {'pending': 1, 'will ': 0, 'awaiting': 0, 'to come': 0, 'not landed': 1, 'unlanded': 1, 'when landed': 2, 'first fill': 0, 'second fill': 0, 'not yet': 0, 'this fill': 0, 'to land': 0, 'open item': 0} ; UPDATE: {'not landed': 1, 'unlanded': 1, 'when landed': 2}
  [chk]     line 1 «NOT LANDED» 2 ; «<DATE>» in file 2 ; «<checker>» in file 2 ; «<HH:MM>» 2
  [chk] (e) slices: line 1 d[0]; record d[1:160] (+ blank d[160]: ''); title d[161]; entry d[161:291]; blank d[291]; preamble d[292:301]; UPDATE d[301]; blank d[302]: ''; Addendum []
  [chk] (f) QUOTE SWEEP (corpus: 50 texts)
  [chk]     sweep line 1: 0 quotes, 0 parts, 0 not found []
  [chk]     sweep FIRST FILL record: 155 quotes, 135 parts, 0 not found []
  [chk]     sweep entry block: 101 quotes, 98 parts, 0 not found []
  [chk]     sweep GAPS preamble + UPDATE: 9 quotes, 8 parts, 0 not found []
  [chk]     sweep whole file: 265 quotes, 241 parts, 0 not found []
  [chk]     sweep NEGATIVE CONTROL: 1 quotes, 1 parts, 1 not found ['CHAIN3 bounds T3 by n squared on every genome']
  [chk]     negative control reported missing: True
  [lp] cites 113 in 13 (commit, file) pairs; failed at the cited lines: 0 []
  [lp] quotes not in the draft as «quote»: 0 []
  [lp] NEGATIVE CONTROL 1 (window shifted by 40 lines): 0 of 113 still pass []
  [lp] NEGATIVE CONTROL 2 (longest word mutated): 0 of 113 still pass
  [lp]     46905772 docs/checker/C138.md 2
  [lp]     46905772 notes/CHECKER.md 1
  [lp]     87603d07 docs/new/P-N5-CHAIN-fixes.md 8
  [lp]     87603d07 docs/new/P-N5-CHAIN-line-L4.txt 13
  [lp]     87603d07 docs/new/P-N5-QUIET-fixes.md 2
  [lp]     93531b03 docs/new/P-N5-CHAIN.md 24
  [lp]     98e1c8be docs/agents/LEAD-STATE.md 1
  [lp]     98e1c8be docs/checker/C118.md 1
  [lp]     98e1c8be docs/new/N5-ssi-global.md 1
  [lp]     98e1c8be docs/referee-2/R2-P-N5-CHAIN.md 20
  [lp]     98e1c8be docs/referee/R-P-N5-CHAIN.md 21
  [lp]     98e1c8be docs/referee/R-P-N5-QUIET.md 1
  [lp]     BASE docs/RESULTS.md 18
  [hex] hex ids in the draft: 76; git objects 48; measured sha1s (not objects) 28; neither: 0 []
  [hex] NEGATIVE CONTROL (0badc0de1, 1234abcd9f): neither: 2 ['0badc0de1', '1234abcd9f']
  [sim] base RESULTS sha1 d847a9ece28e2eadf8f23128fcc98d0a7941e75c lines 16237 "¦" 1477 ; base GAPS sha1 7e08dbf373280c4c4dcc05c92f8911d69205ba56 lines 23
  [sim] pure insertion: prefix byte-unchanged True ; suffix byte-unchanged True ; inserted lines 131
  [sim] headings after insertion: {'R123': [15076], 'R124': [15371], 'R125': [15595], 'E-1': [15726], 'E-2': [15739], 'E-3': [15767], 'Dead': [15798]}
  [sim] R125 at l. 15595-15724, blank l. 15725 (''), «**Erratum E-1**» l. 15726; R124 block ends l. 15593, blank l. 15594 ('')
  [sim] order R123 < R124 < R125 < E-1 < E-2 < E-3 < Dead ends: True
  [sim] RESULTS lines 16237 -> 16368 (+131) ; "¦" 1477 -> 1477 (unchanged True) ; «checker 3333333)» once True ; «checker PENDING)» 0
  [sim] ### R1xx headings: 26, R125 the last: True
  [sim] GAPS: only l. 11 changes True ; lines 23 -> 23 ; l. 11 "¦" 76 -> 76 ; R125 last: True ; after R124's: True ; prefix byte-unchanged: True
  [sim] GAPS whole file "¦" 198 -> 198
  [sim] fill values used only here: 2099-01-11 00:00 3333333

Addendum 2 (subagent, for the Lead; does not land; second fill, 2026-11-11T22:09:46Z by date -u). (1) SECOND FILL on line L-5 (l-new
dd83371b, sha1 473344b1…), to CHECKER C139 Add. 1. Built in the scratchpad by fill2.py from git show a179ef4a:docs/agents/R125-draft.md
(sha1 81cbdc63…, asserted; the same file at origin trunk 8ba1b23b); I merged, committed and pushed nothing and wrote nothing into the
repository; the Lead commits this file. (2) WHAT IS LEFT: CHECKER C139 Add. 1 on this file (C139 §6: L-5 = §4, UPDATE-5 = f22faed5, the
block's L-4 references refreshed; and the notes D-1 to D-3, N-S and N-L41 of the SECOND FILL section); the Lead's local merges of
claude/l-new 1478886e, claude/referee d2678292, claude/referee-2 fb1ff08c and claude/checker 4e8654c4 (local HEAD 78f49435; none of the four
is an ancestor of origin trunk 86f62c26) reach origin, claude/checker is merged at C139 Add. 1's commit; then the Lead lands R125 after R124
with <DATE>, <HH:MM> and <checker> filled. (3) Scratch:
/tmp/claude-0/-home-user-parity-games-challange/43a29ffc-0674-5391-84c1-1d3918a14b5d/scratchpad/r125b/ (arch/ = full git archive of
dd83371b; arch_mk/ and mkscript/ for mkl5_196.py; blocks.*, neg_pin.out, mk.out, L5.bak; tools/blocks196b.sh, pinblock.sh, runblocks.sh,
l5rel125b.py, upd125b.py, chk125b.py, lp125b.py, sim125b.py, rec125b.py, hex125b.py with their *.out, *_p1.out and *_final.out; fill2.py,
cites2.json, src_cites1.json, fetch.txt, fetch2.log, fetch3.log, filltime.txt, R125-draft.pre.md (pass 1); report.txt). (4) NOT DONE:
scripts/verify.sh and scripts/push.sh not run (the two box 196 blocks of experiments/new/check.sh only, and the «P-N5-CHAIN» block twice
more for the negative control); the referees' chain_l5.py and bt_l5.py not re-run (their outputs l5test.out and bt_l5.out read); the proofs
not re-derived; L-RED's files not read; the first fetch's exit code not captured (the second and third fetches rc 0; the third saw the trunk
at 86f62c26, every other head unchanged); no Oink run (L-5 cites no Oink check). (5) Checks on the pass-1 draft, whose line 1, SECOND FILL
section, title, entry block, GAPS preamble and UPDATE are byte-equal to this file's (outputs r125b/*_p1.out; the final run on this file is
r125b/*_final.out). Verbatim output lines, with «|» printed as «¦» and the guillemets as ‹ ›, so that they are not read as quotes of this
file:
  [chk] model: landed R124 title (8ba1b23b) == ‹### R124 [refereed-only] › + R124 L-4 + ‹, CHECKER PASS (docs/checker/C138.md, checker 5b9f4af8)›: True
  [chk] file: sha1 f6470579a223d932c2a62bd830c342a7875a911e bytes 101714 lines 525 ends with newline True
  [chk] ### R headings at d[...]: [308]
  [chk] (a) title == ‹### R125 [refereed-only] › + L-5 (no newline) + ‹, CHECKER PASS (docs/checker/C139.md, checker › + ‹PENDING)›: True ; middle bytes == L-5 bytes without newline: True
  [chk]     title: 8941 chars, 9125 bytes, sha1 ef4f5ae359804a87a669000ef634b24eeb38be0e, ( 176 ) 176, min depth 0, final 0, ¦ 0, fill token 1
  [chk] (e) entry block d[308:438] (lines 309-438, 130 lines, sha1 of the joined block 724fddf02f45aad6e36e79c2812b8aca07927ec4); next line blank: True; line after: 'Proposed GAPS line-11 UPDATE (append-onl'
  [chk] (b) the fill token ‹checker PEND› + ‹ING)› in the entry block: 1 ; in the whole file: 5 at lines [309, 453, 457, 459, 502]
  [chk]     ‹\n**Erratum E-1** (not a result› in the block: False ; ‹**Erratum E-1**› in the block: 0 ; in the file: 7 ; line-start ‹**Erratum› in the file: 0
  [chk] (e) UPDATE line(s) at d[...]: [448] (line [449])
  [chk]     GAPS preamble(s) at d[...]: [439] -> d[439:448]
  [chk] (c) "¦" in entry block: 0 ; in UPDATE: 0 ; in GAPS preamble: 1 (the quoted ‹ ¦› of the row end); in the file: 14
  [chk] (d) UPDATE <DATE> 1 <HH:MM> 1 <checker> 1; head at its start: True
  [chk]     UPDATE = upd125L5.txt: True ; sha1 (no newline) f22faed54eeafdff59de062b1ed0294e3acb7ec6 = f22faed5…: True ; with newline 849f381106a63593ad9c169bcdd96d437443718e ; 9079 bytes 8897 chars ( 175 ) 175
  [chk]     stale grep, entry block minus title (case-insensitive): {'pending': 0, 'will ': 0, 'awaiting': 0, 'to come': 0, 'not landed': 0, 'unlanded': 6, 'when landed': 1, 'first fill': 0, 'second fill': 0, 'not yet': 1, 'this fill': 0, 'to land': 0, 'open item': 0, 'simulated': 0, 'placeholder': 0}
  [chk]       'unlanded' at block lines: [(317, 'Corollary HUB-ASC-G3 (‹PROVED, CONDITIONAL on the unlanded packet P-'), (318, '  (‹PROVED, CONDITIONAL on the unlanded packets P'), (348, '  (l. 42, ‹on P-N5-ASC §4 (unlanded; R121 whe'), (375, 'NDGAME-3 and P-N5-ASC §4 hold (both lane packets, unlanded), then fo'), (435, ' on {Γ3(G) : U(G) ≤ B} under a HYPOTHESIS and two unlanded premises.')]
  [chk]       'when landed' at block lines: [(348, '  (l. 42, ‹on P-N5-ASC §4 (unlanded; R121 when landed)›); UP-JU')]
  [chk]       'not landed' at block lines: []
  [chk]       'not yet' at block lines: [(338, '92, l. 289, quoted below). REFEREE-2: L-1 and L-2 NOT YET on R-1, R')]
  [chk]     stale grep, title: {'pending': 1} ; UPDATE: {} ; GAPS preamble: {}
  [chk]     ‹L-4 › in the entry block minus title: 9; ‹L-4› 12; ‹a69c8aa9› 2; ‹87603d07› 8; ‹3a492186› 1; ‹98e1c8be› 1
  [chk]     line 1 ‹NOT LANDED› 1 ; ‹<DATE>› in file 5 ; ‹<checker>› in file 5 ; ‹<HH:MM>› 5
  [chk] (e) slices: line 1 d[0]; SECOND FILL d[1:148]; FIRST FILL record d[148:307] (+ blank d[307]: ''); title d[308]; entry d[308:438]; blank d[438]; preamble d[439:448]; UPDATE d[448]; blank d[449]: ''; first fill Addendum d[450:506]; blank d[506]: ''; Addendum 2 d[507:525]
  [chk] (f) QUOTE SWEEP (corpus: 90 texts)
  [chk]     sweep line 1: 0 quotes, 0 parts, 0 not found []
  [chk]     sweep SECOND FILL section: 114 quotes, 110 parts, 0 not found []
  [chk]     sweep FIRST FILL record: 155 quotes, 135 parts, 0 not found []
  [chk]     sweep entry block: 123 quotes, 121 parts, 0 not found []
  [chk]     sweep GAPS preamble + UPDATE: 8 quotes, 7 parts, 0 not found []
  [chk]     sweep first fill Addendum: 17 quotes, 13 parts, 0 not found []
  [chk]     sweep Addendum 2: 3 quotes, 1 parts, 0 not found []
  [chk]     sweep whole file: 420 quotes, 387 parts, 0 not found []
  [chk]     sweep NEGATIVE CONTROL: 1 quotes, 1 parts, 1 not found ['CHAIN3 bounds T3 by n squared on every genome']
  [chk]     negative control reported missing: True
  [lp] cites 47 (new at this fill) in 5 (commit, file) pairs; failed at the cited lines: 0 []
  [lp] quotes not in the draft as ‹quote›: 0 []
  [lp] NEGATIVE CONTROL 1 (window shifted by 40 lines): 0 of 47 still pass []
  [lp] NEGATIVE CONTROL 2 (longest word mutated): 0 of 47 still pass
  [lp]     389d19f8 docs/checker/C139.md 20
  [lp]     86f62c26 docs/agents/LEAD-STATE.md 1
  [lp]     d2678292 docs/referee/R-P-N5-CHAIN.md 10
  [lp]     dd83371b docs/new/P-N5-CHAIN-fixes.md 7
  [lp]     fb1ff08c docs/referee-2/R2-P-N5-CHAIN.md 9
  [sim] trunk RESULTS sha1 52e70927c5d851f1586a1e72db285bdae443fc7a lines 16237 "¦" 1477 ; GAPS sha1 18ed7db646594ef6628aa8d93bbc055f16bd9232 lines 23 (8ba1b23b = 86f62c26 = 78f49435: True)
  [sim] pure insertion: prefix byte-unchanged True ; suffix byte-unchanged True ; inserted lines 131
  [sim] headings after insertion: {'R123': [15076], 'R124': [15371], 'R125': [15595], 'E-1': [15726], 'E-2': [15739], 'E-3': [15767], 'Dead': [15798]}
  [sim] R125 at l. 15595-15724, blank l. 15725 (''), ‹**Erratum E-1**› l. 15726; R124 block ends l. 15593, blank l. 15594 (''); C139 §5 expects R125 15595-15724, E-1 15726: True
  [sim] order R123 < R124 < R125 < E-1 < E-2 < E-3 < Dead ends: True
  [sim] RESULTS lines 16237 -> 16368 (+131) ; "¦" 1477 -> 1477 (unchanged True) ; ‹checker 3333333)› once True ; fill token 0
  [sim] ### R1xx headings: 26, R125 the last: True
  [sim] GAPS: only l. 11 changes True ; lines 23 -> 23 ; l. 11 "¦" 76 -> 76 ; ‹UPDATE 2026-› 59 -> 59 ; R125 last: True ; after R124's (2026-11-09 09:04Z, 5b9f4af8): True ; prefix byte-unchanged: True
  [sim] GAPS whole file "¦" 198 -> 198
  [sim] fill values used only here: 2099-01-11 00:00 3333333
  [rec] FIRST FILL record + blank: this d[148:308] == first fill d[1:161]: True (160 lines)
  [rec] first fill Addendum: this d[450:506] == first fill d[303:359]: True (56 lines); blank before: '', after: ''
  [rec] first fill title in this file: 0; first fill UPDATE (d7502428) in this file: 0; first fill line 1: 0
  [rec] token diff title: 10 hunks, 33 tokens out, 26 in
  [rec]     replace 'the unlanded lane packets P-N5-END (ENDGAME-3)' -> "P-N5-END's Theorem ENDGAME-3 (RESULTS R124)"
  [rec]     replace 'R121 when landed))' -> 'R121))'
  [rec]     replace "lane packets, not landed: P-N5-END's" -> "RESULTS R124's"
  [rec]     replace '(frozen at l-new 131b4c1c, REFEREE 29 SIGN)' -> '(P-N5-END)'
  [rec]     replace "P-N5-ASC §4's" -> "RESULTS R121's"
  [rec]     insert '' -> '(Lemma SKELETON, Theorem HUB-ASC(B); P-N5-ASC §4)'
  [rec]     delete '(RESULTS R121 when landed)' -> ''
  [rec]     delete 'G-N5-TIME stays OPEN,' -> ''
  [rec]     replace 'M4:' -> 'M4, so this is not M4; G-N5-TIME stays OPEN;'
  [rec]     delete 'not M4,' -> ''
  [rec] token diff entry block without title: 48 hunks, 69 tokens out, 552 in
  [rec]     replace '64-65,' -> '64-65 and 69,'
  [rec]     replace '87603d07' -> '87603d07, 3a492186, dd83371b'
  [rec]     replace '3a492186;' -> '1478886e;'
  [rec]     replace '(87603d07: 94' -> '(dd83371b: 119'
  [rec]     replace '11,431' -> '14,596'
  [rec]     replace 'e823ca09db0b61368841f831d2ae5dd13161acc9;' -> '7b620ce2d0965f286ad9a3cec0c359e7406bbd3d; its first 11,431 bytes are the file at 87603d07 (sha1 e823ca09db0b61368841f831d2ae5dd13161acc9),'
  [rec]     insert '' -> "Entry 4 (dd83371b, successor 69, l. 96-119; line-only; CHECKER C139 E-1, E-2; ‹No statement, label, hypothesis, proof or DATA number changes; the packet stays frozen›): R-U (E-1) and R-L1, R-L2 (E-2), C139 §4's strings (l. 104-113); ‹Line L-5› = L-4 + R-U + R
  [rec]     replace 'L-4, a69c8aa96fb0b67c6c0a3f6d11670a0b57ba9331 (docs/new/P-N5-CHAIN-line-L4.txt,' -> 'L-5, 473344b1149d4b44d87bdb917607b618d05d57ce (docs/new/P-N5-CHAIN-line-L5.txt,'
  [rec]     replace '87603d07, 2026-11-08T13:19:30Z,' -> 'dd83371b, 2026-11-11T21:07:21Z,'
  [rec]     replace '9,082' -> '9,047'
  [rec]     replace 'L-4' -> 'L-5'
  [rec]     replace "L-4's" -> "L-5's"
  [rec]     replace '(174' -> '(175'
  [rec]     replace '174' -> '175'
  [rec]     insert '' -> 'L-5 (473344b1, dd83371b, L-4 + R-U, R-L1, R-L2; C139 §4),'
  [rec]     insert '' -> 'below); L-5 MATCHES (§F, d2678292, l. 289, quoted'
  [rec]     insert '' -> 'below); L-5 MATCHES (Add. 6, REFEREE-2 successor 36, fb1ff08c, l. 358, quoted'
  [rec]     replace '3e02e7c3;' -> '3e02e7c3, §F d2678292;'
  [rec]     replace '3c5264e0).' -> '3c5264e0; successor 36: Add. 6 fb1ff08c).'
  [rec]     replace '§0.›);' -> '§0.›), l. 289 (L-5: ‹Statements as signed (§0, §D follow-ups 1-2).›);'
  [rec]     replace 'unchanged.›.' -> 'unchanged.›, Add. 6 l. 351 (L-5: ‹Only the status words change. The theorem, its hypothesis, its bound and its label are as I signed them.›).'
  [rec]     replace 'the unlanded lane packets P-N5-END (ENDGAME-3)' -> "P-N5-END's Theorem ENDGAME-3 (RESULTS R124)"
  [rec]     replace 'R121 when landed)›.' -> 'R121)› (C139 §3 (i): ‹CHAIN3 keeps ‹CONDITIONAL› with its premises named as landed RESULTS: yes, no label change.›).'
  [rec]     replace 'taken.' -> "taken, and C139's E-1 and E-2 (R-U; R-L1, R-L2) status words, taken in L-5."
  [rec]     replace '1-3;' -> '1-4;'
  [rec]     insert '' -> 'and 4'
  [rec]     insert '' -> '(R121 l. 14320,'
  [rec]     replace "R125's landing (R121; R124);" -> '59dacf22; R124 l. 15371, at 8ba1b23b); L-5 names them so (R-L1, R-L2; C139 E-2) and keeps'
  [rec]     replace "line's ‹unlanded› wording is G-S of the fill record." -> 'label ‹CONDITIONAL› (C139 §3 (i)).'
  [rec]     insert '' -> 'Both clauses are unchanged in L-5 (REFEREE-2 Add. 6: ‹The W-1 clause (R-W) and the (Q5) step (R-G3) are unchanged in L-5›, l. 356-357; C139 §3: ‹G-7 / L41: met.›, l. 47).'
  [rec]     insert '' -> "(viii) The line's source note names ‹fixes entries 1-3› and ‹L-NEW successors 64-65›; fixes entry 4 (successor 69) is line-only (REFEREE §F: ‹Fixes entry 4 is line-only›, l. 287) and carries no proof text, so the note does not name it (the C134 N-S rule; R124
  [rec]     replace '(unchanged' -> '(tools, outputs and data unchanged'
  [rec]     replace '3a492186):' -> 'dd83371b and 1478886e; dd83371b adds mkl5_196.py and re-pins chain.pins, 59 rows):'
  [rec]     replace '98e1c8be),' -> '98e1c8be, dd83371b, 1478886e and 8ba1b23b, the same 16 lines),'
  [rec]     replace '87603d07: 2026-11-09T08:41:52Z-2026-11-09T08:44:25Z,' -> 'dd83371b: 2026-11-11T22:05:49Z-2026-11-11T22:08:28Z,'
  [rec]     replace '57' -> '59'
  [rec]     replace 'PASS›.' -> 'PASS›; with one byte appended to L-5 the ‹P-N5-CHAIN› block printed ‹P-N5-CHAIN check: FAILED›, rc 1 (negative control). The same blocks at 87603d07: rc 0 at 2026-11-09T08:41:52Z-2026-11-09T08:44:25Z (drafter, 57 pinned files) and by CHECKER C139 (§5 l. 82-84
  [rec]     replace '268).' -> "268); §F d2678292 (d2678292247a2778ded5b0e0c7a9f93ce9973de4, 2026-11-11T21:35:16Z) l. 270-289, ‹Verdict: fixes entry 4 CORRECT. **Line L-5 MATCHES** (L-4 + exactly R-U, R-L1, R-L2). Statements as signed (§0, §D follow-ups 1-2).› (l. 289), its chain_l5.py comm
  [rec]     replace '328-329).' -> "328-329); successor 36's Add. 6 fb1ff08c (fb1ff08c980024dded83b91777b016fb888b6b61, 2026-11-11T21:34:25Z) l. 331-358, ‹Verdict: L-5 MATCHES (fixes entry 4 CORRECT). Nothing REQUIRED is open on my side.› (l. 358)."
  [rec]     replace 'L-4).' -> 'L-4); successor 69, dd83371b (entry 4, L-5).'
  [rec]     replace '310).' -> "310), and L-5 likewise (REFEREE §F chain_l5.py ‹with the strings typed from C139 §4 (claude/checker 389d19f8; wrapped lines joined with one space), not from the lane's script›, l. 273-274; REFEREE-2 Add. 6 bt_l5.py parses fixes entry 4's bullets: ‹It does not
  [rec]     replace 'L-4' -> 'L-5'
  [rec]     insert '' -> 'once'
  [rec]     replace '‹not' -> 'ends its scope words ‹so this is not M4; G-N5-TIME stays OPEN; not'
  [rec]     delete 'not M4,' -> ''
  [rec]     replace 'claim› once each, in' -> 'claim›,'
  [rec]     replace 'C138 E-1 failed for' -> 'of landed R123 and'
  [rec]     replace '(G-U).' -> '(R-U, C139 E-1).'
  [rec] entry block lines: first fill 130, this 130; per-line: 99 lines byte-equal, 31 changed
  [rec] token diff UPDATE: 8 hunks, 27 tokens out, 22 in
  [rec]     replace 'the unlanded lane packets P-N5-END (ENDGAME-3)' -> "P-N5-END's Theorem ENDGAME-3 (RESULTS R124)"
  [rec]     replace 'R121 when landed));' -> 'R121));'
  [rec]     replace "lane packets, not landed: P-N5-END's" -> "RESULTS R124's"
  [rec]     replace '(frozen at l-new 131b4c1c, REFEREE 29 SIGN)' -> '(P-N5-END)'
  [rec]     replace "P-N5-ASC §4's" -> "RESULTS R121's"
  [rec]     insert '' -> '(Lemma SKELETON, Theorem HUB-ASC(B); P-N5-ASC §4)'
  [rec]     delete '(RESULTS R121 when landed)' -> ''
  [rec]     insert '' -> 'M4, so this is not'
  [hex] hex ids in the draft: 125; git objects 78; measured sha1s (not objects) 47; neither: 0 []
  [hex] NEGATIVE CONTROL (0badc0de1, 1234abcd9f): neither: 2 ['0badc0de1', '1234abcd9f']
