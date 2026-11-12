# Draft RESULTS R126 (Lead; first fill 2026-11-11T23:59:06Z by date -u (subagent) on P-N5-QN line L-1, docs/new/P-N5-QN-line-L1.txt, l-new 02a928a3, sha1 28bf566bdf95d0708b3b80303bfa7311c8d5d8b1) — to CHECKER C140 — NOT LANDED; goes after R125 (landed at trunk 0753fd71, RESULTS l. 15595-15724), directly before the line-start «**Erratum E-1** (not a result» (l. 15726 at 0753fd71); its GAPS UPDATE after R125's on GAPS l. 11
FIRST FILL (this text). Built by script (r126a/fill1.py) in the scratchpad r126a/ for the Lead to copy to docs/agents/R126-draft.md; nothing
  in the repository was edited, committed, merged or pushed by me, and scripts/push.sh and scripts/verify.sh were not run. Read at the
  origin heads of a git fetch of claude/l-new, claude/referee, claude/referee-2, claude/checker and claude/l-red at 2026-11-11T23:49:16Z by
  date -u («Wed Nov 11 23:49:16 UTC 2026», before and after; rc 0; r126a/fetch.txt, fetch2.log; an earlier fetch of the same five branches
  at 2026-11-11T23:48:38Z-2026-11-11T23:48:41Z moved l-new 1478886e..8f4dab7e, referee d2678292..731db590, referee-2 fb1ff08c..2a0c9af6,
  l-red 54ebb51a..c6be5222, its rc not captured (piped to tail)).
HEAD l-new 8f4dab7e (8f4dab7eedf632002351ff1071df46300d82a0b9, 2026-11-11T22:57:03Z, «L-NEW 69: P-N5-SPLIT fixes entry 2 + line L-1 — SP-1 =
  W-1 ((LEX-Λ) only on non-core vertices), SP-2 = R-6 citation form, SP-3 = N-1, N-2, LS-1..LS-8 …»).
HEAD referee 731db590 (731db590edcd16b385acf7f5e67653c8f133d6b1, 2026-11-11T22:51:49Z, «REFEREE s31: R-P-N5-GATE §1 (objects, premises,
  GT-1..GT-8) and §2 (proofs re-derived; GT-9)»).
HEAD referee-2 2a0c9af6 (2a0c9af6a8bdebd4b08c5764d19efdee3984f437, 2026-11-11T23:15:22Z, «REFEREE-2 successor 37: handover check (five
  questions)»).
HEAD checker 1622c7d9 (1622c7d92bec04fe000ee0bfe35e65dab4307cec, 2026-11-11T23:22:58Z, «CHECKER C139 Add. 1: R125 second fill cd085bcc @
  e3054997 on L-5 PASS (L-5 = mine 473344b1; UPDATE f22faed5; box 196 rc 0 from dd83371b + negative con…»).
HEAD l-red c6be5222 (c6be5222f55d3edd3d87087f77076b97aa83772e, 2026-11-11T23:21:58Z, «L-RED 64 R230 item 4: BOX 205 BETA-LOC SURVIVES
  (IDEAL-CYC); NOCYC-NOFLIP / K1-BASIN conditional on unlanded (k+1)-Lambda (G1); G1-G5; independent eng…»).
No P-N5-QN object changed after its last commit: on origin/claude/l-new the packet, the fixes file, L-1 and experiments/new/box203/ are
  byte-equal at 02a928a3 and at 8f4dab7e (git diff --stat empty), and so at trunk 0753fd71; docs/referee/R-P-N5-QN.md (149 lines, sha1
  6765f83f3801c7c49cb68e95b145eb629133ede9) is byte-equal at 09aabb03, at the referee head and at 0753fd71; docs/referee-2/R2-P-N5-QN.md
  (201 lines, sha1 41e55221e312ac8115d1348a1977a68f2e5e7277) at 565d5022, at the referee-2 head and at 0753fd71. The brief's facts were
  checked by script (this file's asserts): every one MATCHES except where BRIEF FACTS below say otherwise.
LINE OF RECORD: docs/new/P-N5-QN-line-L1.txt, COMMIT 02a928a3 (02a928a3eda7012628778ae4ce7c540555832884, 2026-11-09T10:14:07Z, «L-NEW 69:
  P-N5-QN fixes entry 1 + line L-1 — QN-1 = W-1 / R-1 merged (k+1)-Λ sentence, [E-LEV] kept on GATE-FLIP (b), LN…»), the file's only commit;
  FILE sha1 28bf566bdf95d0708b3b80303bfa7311c8d5d8b1 (git show | sha1sum; blob dcb87fa888cc80fd1f231cd8620219cf268fcebc), 7,357 bytes, 7,221
  characters with its newline, one line with its newline, 140 «(» = 140 «)», 0 «|», one « — », «(2026-11-09)» once.
PACKET: docs/new/P-N5-QN.md FROZEN at e252182d (e252182d21ef2f6fe95e66d835059f30530978b8, 2026-11-09T06:55:55Z, «L-NEW 68: PACKET P-N5-QN
  FROZEN — GATE-CLASS, GATE-FLIP, QUIET-N (R123 T-QUIET window L → N), (k+1)-Λ on lande…»), the file's only commit; sha1
  97254bd2a97f28bb0c14ab5f4d236ee723821dd9, 195 lines, 20,725 bytes (VERIFIED; = the brief). FIXES: docs/new/P-N5-QN-fixes.md at 02a928a3,
  its only commit: entry 1 + the «Line L-1» note, 71 lines, 7,176 bytes, sha1 b8f8a1a905c261c1f76bc3dc2a62bc37fa744bbc (VERIFIED). GENERATOR
  experiments/new/box203/mkl1_qn.py (02a928a3). PINS experiments/new/box203/qn.pins: 61 rows at 02a928a3 (56 at e252182d; the five added are
  L-1, the fixes file, skip203.py, skip203.out and mkl1_qn.py).
REFEREES (git blame at the heads). REFEREE docs/referee/R-P-N5-QN.md: l. 1-117 the first review 452800c5
  (452800c55384828e52244fcef44144ab3cc923c0, 2026-11-09T07:38:09Z, «REFEREE successor 30: R-P-N5-QN first review (all SIGN; QN-1 wording;
  LN-1..LN-8; own replay 0 failures; DEAD confirmed)»); l. 118-149 §C 09aabb03 (09aabb03cf145e2f9ea779536fcbb87182c92efb,
  2026-11-09T10:42:00Z, «REFEREE successor 30: R-P-N5-QN §C (L-1 28bf566b MATCHES; LN-1..LN-8 PASS)»). REFEREE-2
  docs/referee-2/R2-P-N5-QN.md: l. 1-140 the second review 5d4f06c2 (5d4f06c2dcf25c2a6723bb398ac7632284f31cb5, 2026-11-09T07:37:31Z,
  «REFEREE-2 successor 35: R2-P-N5-QN second review (GATE-CLASS, GATE-FLIP, QUIET-N SIGN; (k+1)-Λ SIGN with W-1 wording; DE…»); l. 141-186
  Addendum 1 a327b4dc (a327b4dcb4ae6d61f17299b0203f0e3aac535fc6, 2026-11-11T21:08:47Z); l. 187-201 Addendum 2 565d5022
  (565d5022191145f5e69996a331b372acee5964ea, 2026-11-11T21:09:11Z). L-RED docs/red/R229-box203.md: Addendum B l. 106-131 f05b0c55
  (f05b0c55f9064c6ad692c15c406c8d8a1c6b3646, 2026-11-09T08:12:24Z, «L-RED 63 R229: P-N5-QN packet-level read (l-new e252182d, sha1
  97254bd2): statements match, 24/24 quotes verba…»).
BOTH REFEREES SAY L-1 MATCHES (VERIFIED). REFEREE §C (09aabb03) l. 148-149 «Verdict: fixes entry 1 CORRECT. **Line L-1 MATCHES** the packet
  read with fixes entry 1 and meets LN-1..LN-8. Statements as §0 (all SIGN).»; its rebuild l. 123 «rewrites L-1 byte-identically (cmp: SAME;
  sha1 28bf566b). qn.pins 61 rows, `sha1sum -c` all OK.». REFEREE-2 Addendum 1 (a327b4dc) l. 142 «fixes entry 1 + line L-1 at claude/l-new
  02a928a3. L-1 MATCHES» and l. 185 «Verdict: L-1 MATCHES the packet as governed by fixes entry 1, and meets R-1, GATE-FLIP (b)'s [E-LEV]»;
  Addendum 2 (565d5022) l. 200-201 «L-1: both referees find MATCHES (REFEREE §C 09aabb03, LN-1..LN-8 PASS; mine Addendum 1). P-N5-QN's line
  has two signatures, with no item open.». Both SIGN every statement (Claims signed, below).
BRIEF FACTS THAT DID NOT MATCH, OR NEED A QUALIFIER: (1) the brief's "Premises: landed R104, R118, R121, R123 only (24 quotes)": 23 of the
  24 are RESULTS quotes; the 24th is P-N5-XICYC's shape line (G-4). (2) the brief's "R229-box203 Addendum B: CLEAN": Addendum B's own
  verdict words are «Three small fixes (G1-G3); none touches a proof.» (l. 111-112); «CLEAN» is fixes entry 1's word («L-RED 63,
  docs/red/R229-box203.md Addendum B at claude/l-red f05b0c55: CLEAN; G1, G2, G3.», l. 8). (3) the brief's "RESULTS 16,368 lines, 1,477
  «|»": 1,477 occurrences (on 499 lines): MATCH. Everything else in the brief matched: packet sha1 97254bd2…, fixes sha1 b8f8a1a9…, L-1
  28bf566b… 7,357 B, qn.pins 61 rows, the referee commits and their roles, R125 at l. 15595-15724 before the line-start Erratum E-1 at l.
  15726, GAPS l. 11 76 «|» ending with R125's UPDATE, premises R-ids ≤ R125.
ANCESTRY (git merge-base --is-ancestor against trunk 0753fd71): the packet, line and fixes commits e252182d, 02a928a3; REFEREE's 452800c5,
  09aabb03; REFEREE-2's 5d4f06c2, a327b4dc, 565d5022; the trunk commits the packet and referees quote from (b8408b39, 547985a10) and the
  RESULTS L-1's generator asserts against (8ba1b23b): ALL ancestors (True). NOT ancestors (True): L-RED 63's f05b0c55 (the packet read),
  8c034440 and cdecc4e0 (cls229, lam229, CLASS-PAYS), fa4e50fe (REL-G), 406ef2fd (MWR(n), D2's source); L-SI's f723957b, d962efdb; L-COMP's
  0eb92268 (packet §9 only, not in L-1). Each is cited in L-1 as a record or as one of the «related lane statements, not premises» (and
  f05b0c55 only in the fixes file and this draft), the status of the L-RED commits of R123-R125 (C138 §5: records, not premises). So for
  P-N5-QN NOTHING needs a merge before landing; what must exist first is CHECKER C140's commit (merge claude/checker at it before landing,
  as for C137-C139).
BASE: trunk 0753fd71 (0753fd71130b5f47890e65e4065d408755269568, 2026-11-11T23:48:02Z, «Lead: LAND R125 (P-N5-CHAIN; CHECKER C139 Add. 1
  1622c7d9 PASS) after R124, before Erratum E-1; GAPS…»), R125 landed: RESULTS sha1 9170163bf892f96f38009c1e11f87bce9764b6e2, 16,368 lines,
  1,477 «|»; «### R125» l. 15595-15724 (blank l. 15725), the line-start «**Erratum E-1** (not a result» l. 15726 (the only one); GAPS sha1
  dbb55831a88223706bbaa9105f5397f3cea3d6e2, 23 lines, l. 11 76 «|», its last UPDATE R125's («UPDATE 2026-11-11 23:47Z: RESULTS R125
  (P-N5-CHAIN; CHECKER C139 1622c7d9)»). No simulated base is needed (no unlanded predecessor).
SOURCES READ: the packet (e252182d) in full; the fixes file (02a928a3) in full; L-1 in full; mkl1_qn.py; check.sh l. 1094-1110 (02a928a3);
  box203's outputs named in L-1 (by data126a.py); REFEREE's R-P-N5-QN.md in full; REFEREE-2's R2-P-N5-QN.md in full; L-RED's R229-box203.md
  Addendum B (f05b0c55) and R229-box202.md §0, §2 (406ef2fd); RESULTS (0753fd71) R104 l. 9864, R118 l. 13607 and (a), (e) l. 13677-13692,
  R121 l. 14320, R123 l. 15076, R125 l. 15595; GAPS l. 11; DECISIONS L41 (l. 355-360), L43 (l. 369-374); docs/checker/C138.md, C139.md
  (0753fd71); TARGET.md §2, §4; the R125 draft at 0753fd71 and at a179ef4a (first fill), the model; the tools of r125a/ and r125b/
  (adapted).
CHECKS RUN AT THIS FILL (scratch r126a/; outputs there). (a) The check.sh blocks «BOX 203 FLIP» and «P-N5-QN» (check.sh l. 1094-1110 at
  02a928a3 = tools/blocks203.sh, run by tools/runblocks.sh) from a FULL git archive of 02a928a3 (r126a/arch/, every path of the tree):
  2026-11-11T23:51:25Z-2026-11-11T23:51:36Z by date -u, rc 0, output «BOX 203 FLIP: GATE-CLASS / GATE-FLIP / QUIET-N / (k+1)-Lambda counters
  0, ST8 ascent witness, controls fire = frozen: PASS» and «P-N5-QN: packet and 61 pinned files match qn.pins, quotes 24 missing 0: PASS».
  Negative control 1: one byte appended to the archive's L-1, the «P-N5-QN» block alone (tools/blockqn.sh):
  2026-11-11T23:52:05Z-2026-11-11T23:52:05Z, rc 1, «P-N5-QN check: FAILED» / «../../../docs/new/P-N5-QN-line-L1.txt: FAILED»; byte restored
  (sha1 28bf566b again) and the block re-run PASS. Negative control 2: one byte prepended to the archive's box203/check203.out, the «BOX 203
  FLIP» block alone (tools/blockflip.sh): 2026-11-11T23:52:11Z-2026-11-11T23:52:22Z, rc 1, «BOX 203 FLIP check: FAILED (check203.sh exit
  0)…»; file restored (byte-equal to its backup). (b) mk.out: the lane generator mkl1_qn.py from a git archive of 02a928a3 (docs/new,
  experiments/new/box203), run with RESULTS at 0753fd71 (R125 landed) as its argument: rc 0, «ok 7356», L-1 rewritten byte-equal (cmp SAME;
  sha1 28bf566b). (c) tools/upd126a.py: the UPDATE by R118's procedure, with three controls (R123, R124, R125 on 0753fd71) and two negative
  controls (upd126a.out). (d) tools/prem126a.py: the 24 premise quotes of packet §1 at 0753fd71 with a negative control (prem126a.out). (e)
  tools/data126a.py: L-1's DATA figures against the pinned outputs (data126a.out). (f) tools/chk126a.py (title, block, UPDATE, tokens,
  pipes, anchors, stale grep, quote sweep with a negative control), tools/lp126a.py (every quote of this file at its cited file, commit and
  lines, with two negative controls), tools/hex126a.py (every hex id, negative control) and tools/sim126a.py (landing simulation on
  0753fd71): Addendum.
LESSONS APPLIED (R125's fills, C138, C139). C113 E-1 / C133 E-1: the title is L-1 verbatim (CLEAN). C133 E-3 / C134 E-3 / C138 E-1 / C139
  E-1: the scope tail carries the landed status words so R118's procedure runs with no reading (G-U: CLEAN). C118 E-1 / C132 E-1 / C139 E-2:
  no status word stale at landing (G-S: CLEAN; note G-S2). L43 (G-L43: FLAG). L41 / C137 N-L41 (G-7: not triggered in my reading). C134 N-S
  (G-1: CLEAN). C115 E-1: premises landed only (G-4: CLEAN, one note). C135 E-4 / C139 G-2 (G-2: notes). C120-C139: every DATA clause
  against its counter (G-9: EQUAL). C122 G-0: parentheses. C130 G-P: the UPDATE builder with controls on the last landed UPDATEs. C132 Add.
  1: block re-run times as a date -u interval.
FLAGS FIRST (my reading; CHECKER rules; strings below are PROPOSALS only).
- G-L43, D2 IS THE DEAD OF AN ASYMPTOTIC STATEMENT (FLAG; the L43 class, which grounds itself on C108 E-1 / C109 E-3). L-1: «D2 «at k = 1
  every gate flips at most c·(lamch(g) + 1) times», every constant c (L-RED 63's MWR(n), claude/l-red 406ef2fd, R229-box202 §2; copies
  experiments/new/box203/inst/MWR4_2.json sha1 856d369b, MWR8_2.json 918f1414, MWR16_2.json 2ccda9a9: gate (qz, 0) flips 2n + 1 times with
  lamch 0)». DECISIONS L43 (0753fd71) l. 370-371: «it enters as DATA with its numbers and source commit, or not at all»; «in a landing line
  needs a refereed proof, or one instance exceeding an EXPLICIT bound (as R90's REP-LIN, 570 > 538)». D2's statement has the unspecified
  constant c; its three instances give 9 / 17 / 33 flips at lamch 0, so they exceed the bound c·(0 + 1) only for c ≤ 32; «flips 2n + 1» for
  every n is L-RED 63's family claim (R229-box202 §0, §2: a table on n = 4, 8, 16 and a «Why it still counts» paragraph, no proof), and
  neither referee proves it: REFEREE «MWR4/8/16_2 gate flips 2n + 1 = 9 / 17 / 33 with C = 0: D2 CONFIRMED.» (l. 84); REFEREE-2 «So no
  c·(lamch + 1) bound holds, and none with C as the denominator. DEAD.» (l. 91). D1 and D3 are explicit and each has an instance beyond its
  bound (k1fail_202: 2 > 2·0 + 1; ST4_k1: 3 > k + 1 = 2): CLEAN. The DATA clause already carries MWR4/8/16_2's 9 / 17 / 33 at lamch 0, so
  L43's «as DATA … or not at all» is met by dropping D2 from the DEAD list. PROPOSED (one of; CHECKER chooses or rules no action): R-D2a
  (drop) "; D2 «at k = 1 every gate flips at most c·(lamch(g) + 1) times», every constant c (L-RED 63's MWR(n), claude/l-red 406ef2fd,
  R229-box202 §2; copies experiments/new/box203/inst/MWR4_2.json sha1 856d369b, MWR8_2.json 918f1414, MWR16_2.json 2ccda9a9: gate (qz, 0)
  flips 2n + 1 times with lamch 0)" → "" (D3 keeps its name); R-D2b (explicit) "every constant c (L-RED 63's MWR(n)" → "every constant c ≤
  32 (L-RED 63's MWR(n)" and "flips 2n + 1 times with lamch 0)" → "flips 9 / 17 / 33 times with lamch 0)". Either is a line change both
  referees re-sign (each confirmed D2 on the three instances only). Old strings once each in L-1 (fill1.py asserts).
- G-U, STATUS WORDS AND THE UPDATE PROCEDURE (CLEAN). L-1's tail is the landed R123 / R124 form, asserted by mkl1_qn.py against RESULTS: «…
  is not M4, so this is not M4; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim (P-N5-QN» (REFEREE §C LN-7 l. 141).
  R118's procedure with the landed drops («; G-N5-TIME stays OPEN», «; not M3, not a step-4 pass, not a TARGET.md claim») runs with NO
  reading: UPDATE sha1 640258db370e0b6f3a217198375ee2399f6ec902 (upd126a.py (4)). The only per-entry constant beyond R125's kind is START:
  L-1 puts its definition block between «for every genome G (Ξ-cycles and Ξ self-loops allowed), » and the first label, so START is that
  whole span (the analogue of R125's «each PROVED (every genome): »); the procedure leaves it in place, as it leaves R125's. Note: L-1 has
  no «N5′-xi stays a CANDIDATE (D1)» (R124, R125 have it; R123, an IDEAL-CYC entry like this one, does not; packet §10 «G-N5-TIME stays
  OPEN; N5′-xi stays a CANDIDATE (D1).» (l. 186)). No string proposed.
- G-S, STALE STATUS WORDS (CLEAN by grep: in L-1 «unlanded», «not landed», «when landed», «pending», «to land», «landed», «CANDIDATE» 0
  each; «stays» once, in «G-N5-TIME stays OPEN»). Premises are named as landed RESULTS only; the packet names in L-1 («any lane packet»,
  «any P-N5-CHAIN fact», «P-N5-QN») are not status words (C138 G-11: «a packet name does not go stale at landing (not a status word, C118
  E-1 does not apply)»).
- G-S2, A SCOPE SENTENCE OVERTAKEN BY R125 (note; CHECKER's call, no FLAG in my reading). L-1 carries R123's landed scope sentence verbatim
  (mkl1_qn.py asserts it in RESULTS): «nothing is proved on Γ3: by RESULTS R118 (k) and (l), under REACH3-CYC's premises, N5′-xi from S3 on
  Γ3(G) makes Howard steps on Γ3 up to its first fallback, … and a Γ3 form of this proof (not given here) would bound N5′-xi only up to its
  first fallback; nothing is claimed about post-fallback iterations, N5′-xi's total count, N5 or general games». Written 2026-11-09, before
  R125 landed (0753fd71, 2026-11-11): R125's REACH3-ALL makes REACH3-CYC hold without its condition, and R125's CHAIN3 bounds N5′-xi's total
  count under [E-LEV] for U(G) ≤ B. Each clause is still true of THIS entry (it proves nothing on Γ3; «nothing is claimed» is about this
  entry), and none is a status word; the «under REACH3-CYC's premises» clause is now weaker than the landed state. R125 also lands Γ3 forms
  of R123's QUIET / T-QUIET (QUIET3, T-QUIET3 with L3), not of QUIET-N. No string proposed.
- G-7, L41 (NOT TRIGGERED in my reading; note). No proof step of P-N5-QN is referee-written: the packet's proofs are successor 68's («Every
  proof is carried here in full.», packet l. 6), and fixes entry 1 says «No statement, no proof and no label changes.» (fixes l. 9). The one
  referee-originated text in L-1 is the WORDING of (k+1)-Λ's value list (QN-1 = W-1 / R-1, found independently by both: REFEREE l. 69-71,
  REFEREE-2 l. 77-87), a statement correction that the frozen proof already makes («The count k + 1 and the proof are unaffected.», fixes l.
  15; REFEREE «The proof says so («Z with w is determined by that cycle»).» (l. 71)). L-1 carries REFEREE-2's required string with one extra
  comma («K1, and, for each»), accepted by REFEREE-2 («The meaning is identical. I accept it.» (l. 163)) and by REFEREE (§C LN-2 l. 130).
  Both referees signed the corrected statement (Claims signed). L41 asks the scope tail to name a referee-originated PROOF; L-1 does not
  name the wording's origin; CHECKER's call whether L41 extends to a statement's wording (no precedent found by me).
- FIXES ENTRY 1, ITEM BY ITEM (the brief's S6 / L41 question). Proof-bearing: NONE. Statement wording: QN-1 = W-1 / R-1 (l. 11-19; the
  governing sentence l. 17). Line-only: GATE-FLIP (b) and QUIET-N wording (l. 21-23), LN-1..LN-8 (l. 30-49; LN-4 keeps the «Against R123»
  remark a READING, «In this file it stays a READING.»), L-RED G1 (l. 51-54, the §7 citation, READING). DATA: the DSALT6 window record (l.
  25-28), LN-5 (l. 40-45; a new tool skip203.py and its output, «**0 skipped** on each of the three»), L-RED G3 (l. 61-64, cited, not
  re-run). Premise bookkeeping, no proof text: L-RED G2 (l. 56-59: the «To sign» row of §4 names [DEF], «No new premise enters the
  packet.»); L-1 carries it as R104's definitions «including that the Odd vertices with a choice are the gates and K2», a reading backed by
  landed R118 (a) «Odd is unrestricted (gates and K2).» (l. 13678). The source note names «with fixes entry 1» and «L-NEW successors 68-69».
- G-1, SOURCE NOTE (CLEAN by C134 N-S). L-1: «(P-N5-QN, docs/new/P-N5-QN.md, frozen at l-new e252182d, sha1 97254bd2, with fixes entry 1,
  docs/new/P-N5-QN-fixes.md; L-NEW successors 68-69; related lane statements, not premises: …)». The proofs are successor 68's (packet l. 2,
  6); entry 1 (successor 69) carries none. L-RED 63's and L-SI 48 / 49's statements are named as «not premises» (REFEREE §C LN-8 PASS).
- G-4, PREMISES (the C115 E-1 class): ALL LANDED (R104, R118, R121, R123; each ≤ R125 and already landed at b8408b39, where the packet
  quoted them). The packet's 24 quotes (§1, l. 33-75), re-found by tools/prem126a.py in RESULTS at 0753fd71 (whitespace-normalised, lines
  joined): 24 of 24, 0 missing; negative control (last character → «#») 0 found. 23 are in RESULTS: R104 6 (l. 9864), R118 6 (l. 13607, (a)
  l. 13677-13678, (e) l. 13691-13692), R121 3 (l. 14320), R123 8 (l. 15076); one, the shape line «movers (Even, priority 0) → gates (Odd,
  priority 1) → {e-face e_g, β-face β_g}», is in docs/new/P-N5-XICYC.md (0753fd71, sha1 149e2414, l. 39), the frozen packet R118 cites,
  quoted in packet §1 as «Shape, from the frozen packet R118 cites» and used only as a reading of [DEF]; L-1 names no lane packet as premise
  («not used: any lane packet»). So the brief's «24 quotes» are 23 RESULTS quotes and 1 lane-packet quote: note (CHECKER's call; precedent:
  landed R123's premise list also quotes the frozen P-N5-XICYC, «F3's proof in the frozen P-N5-XICYC §3, l. 75: «σ̄_t is optimal at every
  vertex at once ([VJ])»», RESULTS l. 15076). L-1's premise list = REFEREE LN-3 (PASS) = fixes LN-3. Not premises: §7's lane statements,
  D1-D3 («none is a premise»).
- G-2, SYMBOLS (notes). Defined in L-1: IDEAL-CYC(G) (with R118 (a)), class_t(v), E_t(v), flips(g), D^tot(v), Q, k (the Ξ-feedback number
  and its Ξ-graph), Ξ_σ, lamch(g) (in D1, before its use in D2), U(G), [E-LEV]. Landed: Λ_t, Π_t, loud / quiet (R123), seq_t(v) and ascents,
  F′_B (R121), the labels C / R / p, T_CYC, BR-SEG (R118), N, M, xt(·), c_W, c_X, e_g, β_g (R104). «Ξ_σ» occurs 13 times in RESULTS
  (0753fd71) and L-1 defines it in place; «the Γ-cycle» is Γ(G)'s. «L» in «window L → N» is R123's L, named by R123's Theorem QUIET. No
  undefined symbol found.
- G-6, NAMES. In RESULTS (0753fd71) 0 times each: «GATE-CLASS», «GATE-FLIP», «QUIET-N», «(k+1)-Λ», «Ξ-feedback», «lamch», «MWR», «DSALT6»,
  «K1C16», «K1F21», «ST4_k1», «ST8_k1», «k1fail_202», «flips(g)», «D^tot(v)», «CLASS-PAYS», «REL-G», «E-FACE-PAYS», «GATE-LOW-NULL»,
  «NP-SHAPE», «P-N5-QN», «R126», «C140» (by script).
- G-9, DATA, CLAUSE BY CLAUSE (data126a.py on the archive of 02a928a3): 27 checks OK, «DATA EQUAL» (corpus 57 rows all must-0 counters 0;
  MWR4/8/16_2 9 / 17 / 33 at lamch 0, C 0; DSALT6_n108 «maxquiet 10 N 108»; rand 1,000 and k = 1 5,000 all 0; K1C16_n400 31 (N 113),
  K1F21_n48 21 (N 48); check203.out 17 rows, ctrl3 lfail 9; lam203 2,000 / 1,000 / 1,000 lfail 0, control 3,492; skip203 0 skipped, k ≤ 5;
  Γ3 6 rows all 0; D1 k1fail_202 2 flips at (4, 0), lamch 0; D3 ST4 / ST8 3 / 7, WC4/8/16_2 4 / 8 / 16 at k 2; the six instance sha1s). The
  units are the code's, read line by line by REFEREE (§5, l. 89-96) and REFEREE-2 (Add. 1, l. 166-182); I did not re-read gfc203.py /
  lam203.py myself (CHECKER's re-check).
- G-DE, DEAD ENDS (note). D1-D3 are stated inside the line with instances and obstruction, as R117's DEAD SUBDIV, R118's DEAD SEG-2P and
  R125's DEAD RUN-TRANSFER were, with no Dead-ends row; none proposed; CHECKER's call (and G-L43 for D2).
- G-P, PLACEMENT (Lead). R126 goes after R125 (0753fd71 l. 15595-15724, blank l. 15725), directly before the line-start «**Erratum E-1**
  (not a result» (l. 15726), its UPDATE after R125's on GAPS l. 11 (the last there). Simulated (sim126a.py): Addendum.
- G-0, THE CHECKER NUMBER. docs/checker/ ends at C139.md (claude/checker 1622c7d9 = in trunk 0753fd71); «C140» 0 times in trunk docs/ and
  notes/ and on claude/checker (git grep). This draft uses C140 (title, UPDATE head), as the brief says.
- G-T, TARGET (CLEAN). L-1's scope tail and TARGET clause equal packet §10 in meaning; QUIET-N sharpens a landed bound and makes no new
  class polynomial (REFEREE §6 «TARGET.md diff: CLEAN»).
- (L-1 SHAPE, by script) one line: 7,357 bytes, 140 «(» / 140 «)», 0 «|», one « — », «(2026-11-09)» once, «DATA, clause by clause» once,
  «HYPOTHESIS» once, «CONDITIONAL» 0, «referee-originated» 0, «R124» 0, «R125» 0.

### R126 [refereed-only] In IDEAL-CYC(G) (RESULTS R118 (a): Γ(G) with every non-mover Even vertex frozen at R104's start, Odd unrestricted (gates and K2), Howard steps at the movers), for every genome G (Ξ-cycles and Ξ self-loops allowed), with class_t(v) := (Λ_t(v), E_t(v)), E_t(v) the e-vertices of Π_t(v), and loud / quiet steps as in RESULTS R123, flips(g) := #{t ≥ 1 : σ̄_(t−1)(g) ≠ σ̄_t(g)} and D^tot(v) := the number of distinct classes of v over the run (= R123's D^tot_E(v)): (Theorem GATE-CLASS) for every gate g and every step t, if σ̄_(t−1)(g) ≠ σ̄_t(g), then class_(t−1)(e_g) ≠ class_t(e_g) or class_(t−1)(β_g) ≠ class_t(β_g); (Corollary GATE-FLIP) (a) flips(g) ≤ (D^tot(e_g) − 1) + (D^tot(β_g) − 1) for every gate g; (b) with seq_t(v) and its ascents as in RESULTS R121, if every seq_t(e_g) and every seq_t(β_g) has at most B ascents, then flips(g) ≤ 2·((2M + 3)·F′_B(M) − 1) with F′_B of RESULTS R121, and under HYPOTHESIS [E-LEV] (lev(x) < lev(x′) implies pr(e_(x,k)) < pr(e_(x′,k′))) B = U(G), the number of options whose Ξ-target has a higher level, may be taken; (Corollary QUIET-N, sharpens RESULTS R123 Theorem QUIET / Corollary T-QUIET: window L → N) every quiet step is a p-step of RESULTS R118, every maximal window of quiet steps has at most N steps, and T_CYC ≤ Q + (Q + 1)·N, Q := the number of loud steps, Q ≤ Σ_v (D^tot(v) − 1); (Lemma (k+1)-Λ) with the Ξ-feedback number k := the minimum size of a set of movers meeting every cycle (self-loops count) of the Ξ-graph on the movers (an edge x → xt(x, j) for each option whose Ξ-target is a mover; options whose Ξ-target is X omitted): for every genome G with Ξ-feedback number k and every state t of IDEAL-CYC(G), the cycle nodes Λ_t(v), over all vertices v other than c_W, c_X and the e-vertices whose successor is c_W, take at most k + 1 values: K1, and, for each cycle of the functional graph Ξ_σ on the movers, x → xt(x, σ_t(x)), the most relevant vertex of the Γ-cycle through its movers, their chosen gates and β-faces; Ξ_σ has at most k cycles (premises: RESULTS R104's definitions of the genome and of Γ(G) only, including that the Odd vertices with a choice are the gates and K2; RESULTS R118 (a), (d) BR-SEG, (e) with its stated reason, R118's order ⊴ on values (Λ, Π, k) (VJ00 §4.2 / Friedmann arXiv 1106.0778 §3) and its step labels C / R / p; RESULTS R121 Lemma E-MON, and for GATE-FLIP (b) only R121's HUB-ASC-G whole-run form and UP-B; RESULTS R123 Lemma CN2, Lemma B-ONLY, Corollary NO-TIE, Lemma LOC-GATE, Lemma LOC-K2; R123 Theorem QUIET and Corollary T-QUIET are the bounds QUIET-N sharpens; [E-LEV] only in GATE-FLIP (b)'s U(G) form; not used: any lane packet, any L-RED or L-SI lane lemma, any P-N5-CHAIN fact) (2026-11-09) — this bounds per-gate flips and quiet windows only, in one restricted model; it makes no new class of genomes on which T_CYC is polynomial, and at k = 1 it bounds the cycle nodes only (whether max_g min(D^tot(e_g), D^tot(β_g)) is polynomial in N + M at k = 1 is OPEN); T bounds IDEAL-CYC iterations only; nothing is proved on Γ3: by RESULTS R118 (k) and (l), under REACH3-CYC's premises, N5′-xi from S3 on Γ3(G) makes Howard steps on Γ3 up to its first fallback, a run that can differ from the IDEAL-CYC run at exact VJ ties (R118's DATA), and a Γ3 form of this proof (not given here) would bound N5′-xi only up to its first fallback; nothing is claimed about post-fallback iterations, N5′-xi's total count, N5 or general games; DEAD (each with the instance that kills it; none is a premise): D1 «at k = 1 each gate flips at most 2·lamch(g) + 1 times», lamch(g) the number of steps at which Λ changes at e_g or β_g (experiments/new/box202/k1fail_202.json, sha1 99bba752, gate (4, 0): 2 flips, lamch 0); D2 «at k = 1 every gate flips at most c·(lamch(g) + 1) times», every constant c (L-RED 63's MWR(n), claude/l-red 406ef2fd, R229-box202 §2; copies experiments/new/box203/inst/MWR4_2.json sha1 856d369b, MWR8_2.json 918f1414, MWR16_2.json 2ccda9a9: gate (qz, 0) flips 2n + 1 times with lamch 0); D3 «every e-sequence has at most k + 1 ascents» (at k = 1 the staircase ST(m), box203/inst/ST4_k1.json sha1 3fa71a98, 3 ascents, and ST8_k1.json sha1 9dbf71f4, 7 ascents; at k = 2 L-SI's WC family, box202/inst/WC4_2, WC8_2, WC16_2: 4, 8, 16 ascents); DATA, clause by clause (scope IDEAL-CYC from the genome's start, cap 20,000 states, engine box191/idealcyc.py with experiments/si/si.py's Engine; tools in experiments/new/box203/, run in part by check203.sh; all pinned in box203/qn.pins): GATE-CLASS: lfail 0 (unit: flip steps at which neither face's class (Λ, E) changes); GATE-FLIP (a): gfail 0 (unit: gates with flips(g) > D^tot(e_g) + D^tot(β_g) − 2); QUIET-N: qflip 0 (unit: quiet steps at which σ̄ changes at some Odd vertex), qfail 0 (unit: runs with a maximal quiet window > N), Tfail 0 (unit: runs with T_CYC > Q + (Q + 1)N); all by gfc203.py on: the 57-genome corpus (the 53 box 202 genomes, MWR4/8/16_2, k1fail_202; out/gfc203_corpus.out), 1,000 rand191 genomes (d 1-6, w 1-3, degree 2-3, seed 2; out/rnd203_rand_s2.out), 5,000 k = 1 genomes (box202 k1srch202.mk, seed 202; out/rnd203_k1_s202.out), K1C16_n400 and K1F21_n48 (out2/gfc203_k1extra.out); control GFC_CTRL=3 (only the e-face's class looked at) fires, lfail 9 on MWR4_2 (check203.out); longest quiet window 10 at N 108 (DSALT6_n108) on this engine and 11 on REFEREE-2 35's engine, both ≤ N (Howard's tie rule is free in R118 (a)); (k+1)-Λ: lam203.py lfail 0 (unit: states with more than k + 1 values) on 2,000 k = 1 genomes (seed 7), 1,000 k = 2 genomes (seed 8) and 1,000 rand191 genomes (seed 2) (out2/lam203_*.out); lam203.py skips genomes with k > 12, and none of these 4,000 was skipped (unit: genomes; skip203.py, out2/skip203.out: k ≤ 5 on every genome); control LAM_CTRL=1 (bound k) fires, lfail 3,492 on the k = 1 set; k = 1 per-gate records (unit: flips of the gate with most flips; lamch 0; C = 0): MWR4/8/16_2 9 / 17 / 33, K1F21_n48 (N 48) 21, K1C16_n400 (N 113) 31; Γ3 counts (N5′-xi from S3 to its first fallback, same counters 0 on MWR4_2, MWR8_2, k1fail_202, C4_NM50, C6G8_n54, RWX_n95; out/gfc203_g3.out) are DATA only, nothing claimed; independent replays, every fail counter 0, their counters in their own pinned outputs, cited, not re-run: REFEREE 30 R-P-N5-QN §4 (claude/referee 452800c5; 1,500 runs and 8 pinned files), REFEREE-2 35 R2-P-N5-QN (claude/referee-2 5d4f06c2; 61 pinned genome runs and 6,000 random), L-RED 63 cls229 (29 rows; claude/l-red 8c034440) and lam229 (12 genomes; claude/l-red cdecc4e0); TARGET.md §2 (M4) asks for an algorithm polynomial on every parity game and §4 says a bound on a restricted class is not M4, so this is not M4; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim (P-N5-QN, docs/new/P-N5-QN.md, frozen at l-new e252182d, sha1 97254bd2, with fixes entry 1, docs/new/P-N5-QN-fixes.md; L-NEW successors 68-69; related lane statements, not premises: L-RED 63 Lemma CLASS-PAYS / Corollary GATE-FLIP-MIN (claude/l-red 8c034440, docs/red/R229-box203.md §3) and Lemma REL-G (claude/l-red fa4e50fe, docs/red/R229-box93.md §1.3), L-SI 49 NP-SHAPE / E-FACE-PAYS (claude/l-si f723957b, docs/si/box93-k7k6.md), L-SI 48 GATE-LOW-NULL (claude/l-si d962efdb, docs/si/box92-closed.md)), CHECKER PASS (docs/checker/C140.md, checker PENDING)
- Object (L-NEW successors 68-69, D1 / D14 / D18, box 203; frozen, unchanged during review): packet P-N5-QN, docs/new/P-N5-QN.md, sha1
  97254bd2a97f28bb0c14ab5f4d236ee723821dd9, 195 lines, 20,725 bytes (l-new e252182d, 2026-11-09T06:55:55Z, the file's only commit; identical
  at 02a928a3, at the l-new head 8f4dab7e and at trunk 0753fd71; pinned in experiments/new/box203/qn.pins). Both referees measured it
  (REFEREE l. 3 «docs/new/P-N5-QN.md sha1 97254bd2a97f28bb0c14ab5f4d236ee723821dd9,»; REFEREE-2 l. 7 «docs/new/P-N5-QN.md at e252182d: sha1
  97254bd2a97f28bb0c14ab5f4d236ee723821dd9, 20,725 B»). Freeze (l. 2-5): «freeze P-N5-QN = Theorem GATE-CLASS, Corollary GATE-FLIP,
  Corollary QUIET-N (the sharpening of landed R123 T-QUIET: L → N), Lemma (k+1)-Λ — premises landed R-ids only». Labels (l. 7): «Labels:
  PROVED (L-NEW 68, unrefereed) / DEAD / DATA / READING (not to sign). Not a TARGET.md claim, not M3, not M4; G-N5-TIME stays OPEN.». To
  sign (l. 21-31): §2 Theorem GATE-CLASS, §3 Corollary GATE-FLIP (a) and (b), §4 Corollary QUIET-N, §5 Lemma (k+1)-Λ, §6 DEAD D1-D3; §7-§10
  READING / DATA; «No other premise: no lane packet, no L-RED or L-SI lemma (§7 lists related ones; none is used), no P-N5-CHAIN fact, no
  [E-LEV] except in §3's second form.» (l. 30-31). Source (l. 6): «Source, history only: docs/new/N5-FLIP-box203.md (box 203, §1-§5.3).
  Every proof is carried here in full.» The packet's own scope (l. 17): «What it does NOT give: no new class on which T_CYC is polynomial
  (the classes of R123 ASC-T / UP-T are unchanged; only degrees drop)».
- Fixes: docs/new/P-N5-QN-fixes.md, append-only, one entry (02a928a3, 2026-11-09T10:14:07Z, the file's only commit; 71 lines, 7,176 bytes,
  sha1 b8f8a1a905c261c1f76bc3dc2a62bc37fa744bbc; byte-equal at the l-new head and at 0753fd71). Entry 1 (L-NEW successor 69, l. 3-64;
  answering REFEREE 30, REFEREE-2 35 and L-RED 63's Addendum B): «No statement, no proof and no label changes. Where this entry and the
  packet differ, this entry governs. Every item is ACCEPTED.» (l. 9). QN-1 = W-1 / R-1 (l. 11-19): the value list of §5 corrected by one
  governing sentence (l. 17, quoted in (e) below), «The count k + 1 and the proof are unaffected.» (l. 15); GATE-FLIP (b)'s «under
  HYPOTHESIS [E-LEV]» and QUIET-N's «sharpens» in the line (l. 21-23); the DSALT6 window record (l. 25-28); LN-1..LN-8 (l. 30-49; LN-4: the
  «Against R123» remark is omitted from the line, «In this file it stays a READING.»; LN-5: lam203.py's k > 12 skip measured by a new tool
  skip203.py, «**0 skipped** on each of the three»); L-RED G1 (§7's citation commits), G2 (§4's premise row names [DEF]: «No new premise
  enters the packet.») and G3 (a second engine cited, not re-run) (l. 51-64). «Line L-1» (l. 66-71): generator
  experiments/new/box203/mkl1_qn.py, pinned in qn.pins. No item changes a statement's content, a label or a proof: QN-1 changes (k+1)-Λ's
  wording to what its proof proves; the rest is line, DATA or citation.
- The RESULTS line is L-1, 28bf566bdf95d0708b3b80303bfa7311c8d5d8b1 (docs/new/P-N5-QN-line-L1.txt, l-new 02a928a3, 2026-11-09T10:14:07Z, the
  file's only commit; 7,357 bytes, blob dcb87fa888cc80fd1f231cd8620219cf268fcebc). The title is L-1 verbatim, with nothing inserted and
  nothing stripped (its date parenthesis «(2026-11-09)», its scope tail and its source note are the line's own). L-1's parentheses balance
  (140 «(» / 140 «)»); it has no pipe character. It is written by experiments/new/box203/mkl1_qn.py, which asserts the frozen packet's sha1,
  fixes entry 1's governing (k+1)-Λ sentence, R123's landed scope sentence and R124's landed TARGET tail in RESULTS, and LN-5's skip counts;
  rebuilt byte-equal by REFEREE (§C, l. 122-123: «rewrites L-1 byte-identically (cmp: SAME; sha1 28bf566b). qn.pins 61 rows, `sha1sum -c`
  all OK.»), by REFEREE-2 (Add. 1, l. 150-151: «exits 0 and rebuilds L-1 byte-equal (28bf566b…).») and by the drafter with RESULTS at
  0753fd71 (rc 0). REFEREE: L-1 MATCHES (§C, 09aabb03, l. 148-149, quoted below). REFEREE-2: L-1 MATCHES (Add. 1, a327b4dc, l. 185-186; Add.
  2, 565d5022, l. 200-201, quoted below).
- Claims signed (REFEREE successor 30: report 452800c5, §C 09aabb03; REFEREE-2 successor 35: report 5d4f06c2; successor 36: Add. 1 a327b4dc,
  Add. 2 565d5022). REFEREE's table («## 0. Verdicts», l. 7-16 of R-P-N5-QN.md) reads: GATE-CLASS «**SIGN** (PROVED). Every step re-derived
  (§3 below).» (l. 10); GATE-FLIP (a) «**SIGN** (PROVED).» (l. 11); GATE-FLIP (b) «**SIGN** (PROVED under its ascent hypothesis; the U(G)
  form under HYPOTHESIS [E-LEV], labelled so).» (l. 12); QUIET-N «**SIGN** (PROVED).» (l. 13); (k+1)-Λ «**SIGN** (PROVED) with wording note
  QN-1» (l. 14); DEAD D1-D3 «**CONFIRMED** on my own engine (§4), except D3's k = 2 WC family (not re-run; cited).» (l. 15); then «No GAP.
  No statement is refused. TARGET.md diff CLEAN (§6).» (l. 16). REFEREE-2's table («## Verdicts (Opus 5.5, D1)», l. 14-22 of R2-P-N5-QN.md)
  reads «SIGN» on GATE-CLASS (l. 17, «every genome, IDEAL-CYC»), GATE-FLIP (a) (l. 18), GATE-FLIP (b) (l. 19, «B = U(G) under HYPOTHESIS
  [E-LEV] (R121 UP-B)»), QUIET-N (l. 20, «sharpens R123 QUIET / T-QUIET: window L → N»); (k+1)-Λ «SIGN WITH W-1 (wording)» (l. 21, «the
  count k + 1 is right; the statement's description of the values is wrong as written (W-1); the line must use the corrected wording»); DEAD
  D1-D3 «SIGN (dead)» (l. 22, «each instance re-run on my own code»); then «No statement is REFUSED. W-1 is a wording defect in (k+1)-Λ's
  statement, not in its proof. The proof identifies the values correctly.» (l. 24). Both re-signed on L-1: REFEREE §C «Statements as §0 (all
  SIGN).» (l. 148-149); REFEREE-2 Add. 2 «Verdicts: equal. Both referees SIGN GATE-CLASS, GATE-FLIP (a), GATE-FLIP (b) (the U(G) form under
  HYPOTHESIS [E-LEV]), QUIET-N and (k+1)-Λ. DEAD D1-D3 are confirmed on independent engines.» (l. 189-190). The HYPOTHESIS statement, with
  its condition as the line states it: GATE-FLIP (b)'s U(G) form «under HYPOTHESIS [E-LEV] (lev(x) < lev(x′) implies pr(e_(x,k)) <
  pr(e_(x′,k′))) B = U(G), the number of options whose Ξ-target has a higher level, may be taken» ([E-LEV] as R121 lands it, REFEREE §C
  LN-1). The joint gap map: EMPTY (REFEREE «No GAP.»; REFEREE-2 «W-1 is a wording defect in (k+1)-Λ's statement, not in its proof.», l. 24;
  Add. 1 «Nothing REQUIRED is open.» (l. 185-186)). The one defect found in review, (k+1)-Λ's value list (QN-1 = W-1 / R-1), is a wording
  defect of the statement, not of the proof, corrected by fixes entry 1's governing sentence and carried by L-1 (REFEREE §C LN-2 PASS;
  REFEREE-2 Add. 1 «R-1 ((k+1)-Λ, REQUIRED): MET.» (l. 161)). Nothing is REFUSED.
- Setting: IDEAL-CYC(G) of RESULTS R118 (a) for every genome G of R104 (Ξ-cycles and Ξ self-loops allowed): R104's Γ(G), every non-mover
  Even vertex frozen at R104's start, Odd unrestricted (the gates and K2), Howard steps at the movers; states 0, …, T_CYC. Statements as
  signed (packet with fixes entry 1, which governs §5's wording):
  (a) Theorem GATE-CLASS (§2 l. 78-79) [every genome]: «For every genome G, every gate g and every step t of IDEAL-CYC(G): if σ̄_(t−1)(g) ≠
    σ̄_t(g), then class_(t−1)(e_g) ≠ class_t(e_g) or class_(t−1)(β_g) ≠ class_t(β_g).» Both SIGN (REFEREE l. 10; REFEREE-2 l. 17).
  (b) Corollary GATE-FLIP (a) (§3 l. 102) [every genome]: «(a) flips(g) ≤ (D^tot(e_g) − 1) + (D^tot(β_g) − 1) for every gate g.» Both SIGN
    (l. 11; l. 18).
  (c) Corollary GATE-FLIP (b) (§3 l. 103-104) [under its ascent hypothesis; the U(G) form under HYPOTHESIS [E-LEV]]: «(b) If every
    seq_t(e_g) and every seq_t(β_g) has at most B ascents, then flips(g) ≤ 2·((2M + 3)·F′_B(M) − 1); under [E-LEV] (HYPOTHESIS, as in R121 /
    R123), B = U(G) may be taken.» Proof: (a) with R121's whole-run form for v = e_g, β_g, and R121's UP-B. REFEREE SIGN (l. 12), REFEREE-2
    SIGN (l. 19).
  (d) Corollary QUIET-N (§4 l. 110-111) [every genome; sharpens RESULTS R123 Theorem QUIET / Corollary T-QUIET]: «In IDEAL-CYC(G), for every
    genome G: every quiet step is a p-step of R118; every maximal window of quiet steps has at most N steps; and T_CYC ≤ Q + (Q + 1)·N,
    where Q := the number of loud steps, Q ≤ Σ_v (D^tot(v) − 1).» Both SIGN (l. 13; l. 20). The «Against R123» bullet's «R123's ASC-T and
    UP-T hold with L + 1 replaced by N + 1.» (l. 119) is not in «To sign», not signed and not in L-1 (LN-4; fixes l. 38-39).
  (e) Lemma (k+1)-Λ (§5 l. 123-125 as governed by fixes entry 1, l. 17) [every genome; k the Ξ-feedback number, packet (D5)]: «For every
    genome G with Ξ-feedback number k and every state t of IDEAL-CYC(G), the cycle nodes Λ_t(v), over all vertices v other than c_W, c_X and
    the e-vertices whose successor is c_W, take at most k + 1 values: K1, and, for each cycle of the functional graph Ξ_σ on the movers, x →
    xt(x, σ_t(x)), the most relevant vertex of the Γ-cycle through its movers, their chosen gates and β-faces; Ξ_σ has at most k cycles.»
    The frozen §5 named «the most relevant vertex of each cycle of the functional graph Ξ_σ on the movers», a mover (QN-1 = W-1); the proof
    is unchanged. REFEREE SIGN with QN-1 (l. 14), REFEREE-2 SIGN WITH W-1 (l. 21); both on the corrected wording (REFEREE §C LN-2 PASS;
    REFEREE-2 Add. 1 R-1 MET).
  (f) DEAD D1-D3 (§6 l. 137-147): D1 «at k = 1 each gate flips at most 2·lamch(g) + 1 times» (k1fail_202, gate (4, 0): 2 flips, lamch 0); D2
    «at k = 1 every gate flips at most c·(lamch(g) + 1) times», every constant c (MWR4/8/16_2: 9 / 17 / 33 flips at lamch 0); D3 «Every
    e-sequence has at most k + 1 ascents» (ST4_k1 3, ST8_k1 7 ascents at k = 1; WC4/8/16_2 4 / 8 / 16 at k = 2). REFEREE CONFIRMED on its
    own engine (l. 15, D3's k = 2 family cited), REFEREE-2 SIGN (dead) (l. 22); «D3's k = 2 WC family is re-run by neither referee. It is
    cited, and ST(m) kills D3 alone.» (REFEREE-2 Add. 2, l. 198).
- Premise (landed RESULTS only; quoted by script at trunk 0753fd71, RESULTS line numbers there; the packet's §1 quotes, l. 33-75): [DEF]
  RESULTS R104 (l. 9864), definitions of the genome and of Γ(G) only: «Even movers of priority 0; Odd gates of priority 1 with a W-face e
  and a Ξ-face β» (l. 9864); «β of priority 6 + 2·rank + parity with edges to the Ξ-target and to u, or to u alone» (l. 9864); «e of even
  priority above every β with one edge to the W-target or to the top even self-loop c_W» (l. 9864); «an unused even self-loop of priority 2;
  c_W's priority top is the least even number at least 2 above every other priority so far» (l. 9864); «a closed core u = K0 (Even, top + 2)
  → {K1, K3}, K1 (Even, 5) → {K0, K1}, K2 (Odd, 3) → {K1, K2}, K3 (Even, top + 3) → {K1, K2}» (l. 9864); «with start σ = the genome start at
  movers, β → its Ξ-target (u when the target is X), K0 → K3, K1 → K1, K3 → K2» (l. 9864); read with R118 (a)'s «Odd is unrestricted (gates
  and K2).» (l. 13678) for «the Odd vertices with a choice are the gates and K2» (L-RED G2); the shape line «movers (Even, priority 0) →
  gates (Odd, priority 1) → {e-face e_g, β-face β_g}» is P-N5-XICYC's (docs/new/P-N5-XICYC.md l. 39, the frozen packet R118 cites), a
  reading of [DEF], not a premise. [XICYC] RESULTS R118: «VJ00 §4.2 / Friedmann arXiv 1106.0778 §3 for the order ⊴ on values (Λ, Π, k)» (l.
  13607); «labelled C if some vertex's cycle node Λ changes, else R if Odd's optimal counterstrategy σ̄ (any fixed deterministic choice)
  changes somewhere, else p» (l. 13607); «The game is Γ(G) with every Even vertex that is not a mover frozen at its start successor. Odd is
  unrestricted (gates and K2).» (l. 13677-13678); «every maximal run of p-steps has at most N steps» (l. 13607); «each vertex's Λ moves only
  to a vertex of strictly larger reward among at most 2M + 3 possible cycle nodes» (l. 13691-13692); «T_CYC ≤ C + R + (C + R + 1)·N» (l.
  13607). [ASC] RESULTS R121: «(Lemma E-MON) if Λ_t(v) = Λ_(t+1)(v) then E_t(v) ≤ E_(t+1)(v)» (l. 14320); «over the whole run the number
  D_E(v) of distinct (Λ_t(v), E_t(v)) is at most (2M + 3)·F′_B(M)» (l. 14320); «so under [E-LEV] every seq_t(v) has at most U(G) ascents
  (U(G) := the number of options whose Ξ-target has a higher level)» (l. 14320). [QUIET] RESULTS R123: «(Lemma CN2) the cycle node of every
  play under every positional pair has priority ≥ 2, so no gate or mover is a cycle node or in a set Π» (l. 15076); «at every state t and
  every vertex v other than c_W and the e-vertices whose successor is c_W, Λ_t(v) is less relevant than every e-vertex» (l. 15076);
  «(Corollary NO-TIE) at every state and gate g, Ω_t(e_g) ≠ Ω_t(β_g)» (l. 15076); «(Lemma LOC-GATE) at every state t and gate g, Odd's
  optimal counterstrategy σ̄_t chooses the face of strictly ⊴-smaller value» (l. 15076); «(Lemma LOC-K2) σ̄_t(K2) = K1 and Ω_t(K1) ◁ Ω_t(K2)
  at every state» (l. 15076); «with class_t(v) := (Λ_t(v), E_t(v)), E_t(v) the e-vertices of Π_t(v), a step loud if some vertex changes
  class and quiet otherwise» (l. 15076); «every maximal window of quiet steps has at most L := (M + 1)(2M + 1)(N + 1) + N(n − 1) steps, n =
  N + 3M + 6» (l. 15076); «(Corollary T-QUIET) T_CYC ≤ (1 + Σ_v (D^tot_E(v) − 1))·(L + 1), D^tot_E(v) the number of distinct classes of v
  over the run» (l. 15076). VJ00 §4.2 / Friedmann arXiv 1106.0778 §3 for the order ⊴ as cited by R118. HYPOTHESIS [E-LEV] only in GATE-FLIP
  (b)'s U(G) form. Not used: any lane packet, any L-RED or L-SI lane lemma, any P-N5-CHAIN fact (L-1). Both referees and L-RED 63 checked
  the 24 quotes by script (REFEREE §1 l. 20 «**24 quotes, 0 missing** (qn_logs/quotes.out): R104 6, P-N5-XICYC 1, R118 6, R121 3, R123 8.»;
  REFEREE-2 l. 27-28 «All 24 are verbatim (whitespace-normalised) in trunk docs/RESULTS.md or P-N5-XICYC.md»; L-RED Add. B l. 114 «24 of 24
  found verbatim»); REFEREE-2 l. 34 «R104, R118, R121 and R123 are all landed at 547985a10. No lane packet and no L-RED / L-SI lemma is a
  premise. §7 is labelled READING.».
- L41 and L43. The packet's proofs are L-NEW successor 68's (packet l. 6, quoted above); no proof step is referee-written. The one
  referee-originated text in the line is the wording of (k+1)-Λ's value list (QN-1, REFEREE l. 69-71; W-1 / R-1, REFEREE-2 l. 77-87, found
  independently, REFEREE-2 Add. 2 «REFEREE's QN-1 is my predecessor's W-1 / R-1, found independently» (l. 191)), a statement correction that
  the frozen proof already makes (REFEREE l. 71 «The proof says so («Z with w is determined by that cycle»).»). L43: D1 and D3 each have one
  instance exceeding an explicit bound (k1fail_202: 2 > 2·0 + 1; ST4_k1: 3 > k + 1 = 2 at k = 1). D2's statement has an unspecified constant
  c; its instances are MWR4/8/16_2 (9 / 17 / 33 flips at lamch 0), its family MWR(n) is L-RED 63's (R229-box202 §2), and both referees
  confirmed it on n = 4, 8, 16 (REFEREE l. 84; REFEREE-2 l. 90-91).
- Not signed: packet §7 (related lane statements: L-SI 49 NP-SHAPE / E-FACE-PAYS, L-SI 48 GATE-LOW-NULL, L-RED 63 REL-G and CLASS-PAYS,
  «cited, NOT premises»), §8 (what stays OPEN), §9 (DATA), §10 (TARGET diff), §11 (machine checks), the «Against R123» remark (READING), the
  Γ3 counts (DATA only); the referees' and L-RED's replays.
- Referee strengthening (NOT part of this entry; referee checks): (i) REFEREE: own engine (successor 26's xicyc_replay.howard, own
  generator, own minimum feedback set; «No lane code imported.», l. 75), families rand, deep, wide, acyc, selfl, 300 each, seed 2032, and 8
  pinned files: «**every counter 0**» (l. 79-81), controls ctrlE, ctrlK fire; DEAD witnesses re-measured (l. 83-85); the lane's pins and
  check203.sh from git archive e252182d (l. 86-87). (ii) REFEREE-2: own engine on r2acyc.py, «Random: 6,000 runs, k up to 7, max T 9, every
  counter 0.» (l. 114), 61 pinned genome runs, every must-0 counter 0, «(k+1)-Λ is counted on 41 of the 61 pinned genomes.» (l. 112);
  controls fire (l. 121-123). (iii) L-RED 63 (not a referee): cls229 (29 rows) and lam229 (12 genomes), every counter 0 (Add. B l. 123-125;
  cited in L-1).
- Honest limits: (i) GATE-CLASS, GATE-FLIP and QUIET-N bound per-gate flips and quiet windows in ONE model, IDEAL-CYC(G); they make no new
  class of genomes on which T_CYC is polynomial (the classes of R123's ASC-T / UP-T are unchanged); nothing bounds a running time or a bit
  cost. (ii) At k = 1, (k+1)-Λ bounds the cycle nodes only; whether max_g min(D^tot(e_g), D^tot(β_g)) is polynomial in N + M at k = 1 is
  OPEN (packet §8), and Σ_v D^tot(v) with U(G) unbounded stays OPEN (R123). (iii) GATE-FLIP (b)'s U(G) form rests on HYPOTHESIS [E-LEV]
  (R121's UP-B). (iv) Nothing is proved on Γ3, for N5′-xi or for N5: landed R125 gives Γ3 forms of R123's QUIET / T-QUIET (QUIET3,
  T-QUIET3), not of QUIET-N; the Γ3 counts are DATA only. (v) DATA are runs of the lane's engine (box191 idealcyc, si.py) and the referees'
  engines; quiet windows depend on Howard's free tie rule (DSALT6_n108: 10 here, 11 on REFEREE-2 35's engine, both ≤ N); every run is short
  (REFEREE-2's pinned set: «Max T 199, max quiet window 11», l. 110), so the data test that nothing exceeds the bounds, not their tightness.
  (vi) D2 is supported by three instances (L43 above). (vii) Names: GATE-CLASS, GATE-FLIP, QUIET-N, (k+1)-Λ, lamch and the instance names
  are new to RESULTS. (viii) Literature: VJ00 §4.2 and Friedmann arXiv 1106.0778 §3 as in R118; no novelty is claimed; L-RED 63's CLASS-PAYS
  (min instead of sum, exact on MWR) is sharper than GATE-FLIP (a) and is a lane statement, not signed here.
- Data (DATA, not proof): experiments/new/box203/ at l-new 02a928a3 (tools, outputs and instances unchanged to 8f4dab7e and 0753fd71;
  e252182d had the same tools and outputs, and 02a928a3 adds skip203.py, out2/skip203.out, mkl1_qn.py and re-pins qn.pins, 56 → 61 rows):
  gfc203.py, rnd203.py, lam203.py, asc203.py, run in part by check203.sh, its frozen output check203.out (17 lines); the record outputs
  out/gfc203_corpus.out (57 rows), out/rnd203_rand_s2.out, out/rnd203_k1_s202.out, out2/gfc203_k1extra.out, out2/lam203_*.out,
  out2/skip203.out, out/gfc203_g3.out; called from the check.sh blocks «BOX 203 FLIP» and «P-N5-QN» (experiments/new/check.sh l. 1094-1110
  at e252182d, 02a928a3, 8f4dab7e and 0753fd71, the same 17 lines, sha1 6cdbfb011966bb289474ebfa691541c2e5c8e5d5), run by scripts/verify.sh.
  Re-run by the drafter from a full git archive of 02a928a3: 2026-11-11T23:51:25Z-2026-11-11T23:51:36Z, rc 0, «BOX 203 FLIP: GATE-CLASS /
  GATE-FLIP / QUIET-N / (k+1)-Lambda counters 0, ST8 ascent witness, controls fire = frozen: PASS» and «P-N5-QN: packet and 61 pinned files
  match qn.pins, quotes 24 missing 0: PASS»; with one byte appended to L-1 the «P-N5-QN» block printed «P-N5-QN check: FAILED», rc 1, and
  with one byte prepended to check203.out the «BOX 203 FLIP» block printed «BOX 203 FLIP check: FAILED (check203.sh exit 0)», rc 1 (negative
  controls). Frozen totals (by script, data126a.py): every must-0 counter 0 on the corpus (57), rand191 (1,000), k = 1 (5,000), K1C16_n400,
  K1F21_n48 and the 6 Γ3 rows; lam203 lfail 0 on 2,000 + 1,000 + 1,000 genomes, 0 skipped, k ≤ 5; controls ctrl3 lfail 9, LAM_CTRL=1 lfail
  3,492; records MWR4/8/16_2 9 / 17 / 33, K1F21_n48 21, K1C16_n400 31, DSALT6_n108 window 10 (N 108). REFEREE-2 read every DATA clause
  against the code (Add. 1, «Every DATA number in L-1 equals its output file.», l. 182).
- Signatures: REFEREE docs/referee/R-P-N5-QN.md: successor 30's report 452800c5 (452800c55384828e52244fcef44144ab3cc923c0,
  2026-11-09T07:38:09Z), «docs/referee-2/ and L-RED 63's R229-box203 were NOT read before this verdict.» (l. 4-5), verdict table l. 7-16; §C
  09aabb03 (09aabb03cf145e2f9ea779536fcbb87182c92efb, 2026-11-09T10:42:00Z) l. 119-149, «**Line L-1 MATCHES** the packet read with fixes
  entry 1 and meets LN-1..LN-8.» (l. 148-149). REFEREE-2 docs/referee-2/R2-P-N5-QN.md: successor 35's report 5d4f06c2
  (5d4f06c2dcf25c2a6723bb398ac7632284f31cb5, 2026-11-09T07:37:31Z), «Independent: docs/referee/ NOT read for this packet before this report
  is committed.» (l. 2-3), verdict table l. 14-24; successor 36's Add. 1 a327b4dc (a327b4dcb4ae6d61f17299b0203f0e3aac535fc6,
  2026-11-11T21:08:47Z) l. 142-186, «Verdict: L-1 MATCHES the packet as governed by fixes entry 1» (l. 185); Add. 2 565d5022
  (565d5022191145f5e69996a331b372acee5964ea, 2026-11-11T21:09:11Z) l. 188-201, «P-N5-QN's line has two signatures, with no item open.» (l.
  200-201). Lane (claude/l-new): L-NEW successor 68, e252182d (packet FROZEN); successor 69, 02a928a3 (fixes entry 1, L-1). Adversary (not a
  signature): L-RED 63, f05b0c55 (R229-box203 Addendum B), «Three small fixes (G1-G3); none touches a proof.» (l. 111-112).
- INDEPENDENCE: each referee wrote its first report without reading the other's (REFEREE l. 4-5; REFEREE-2 l. 2-3 and l. 140, «I did not
  read docs/referee/ for this packet, nor L-RED 63's reports.»); the two reports were committed 38 seconds apart (5d4f06c2 07:37:31Z,
  452800c5 07:38:09Z). REFEREE §C read docs/referee-2/ only for the strings fixes entry 1 cites («docs/referee-2/ read only for the strings
  fixes entry 1 cites.», l. 149). REFEREE-2 36 discloses that fixes entry 1 outlines REFEREE's findings and read REFEREE's report only after
  its own verdict («My report (5d4f06c2) was committed before that entry existed. I read REFEREE's report only after this addendum's verdict
  (Addendum 2).», l. 147-148), then compared (Add. 2). Each referee rebuilt L-1 byte-equal from the lane generator on its own archive; each
  read the DATA code itself (REFEREE §5; REFEREE-2 Add. 1). Neither read L-RED 63's reports before its verdict (REFEREE l. 4-5; REFEREE-2 l.
  2-4).
- TARGET.md diff: TARGET.md §2 (M4) asks for one algorithm, polynomial on EVERY parity game, that outputs (W_E, W_O); this entry is a
  mechanism lemma, a per-gate bound, a sharper window bound and a cycle-node count on one model, IDEAL-CYC(G), for no algorithm on general
  games (TARGET.md §4: «Polynomial only on a restricted class»; packet §10 l. 183-186; REFEREE §6 «No algorithm claim; one model (IDEAL-CYC
  of R104 / R118 genomes); QUIET-N sharpens a landed bound and makes no new class polynomial»; REFEREE-2 «So it is not M3, not M4, not a
  step-4 pass, and not a TARGET.md claim. G-N5-TIME stays OPEN.»). It is not an algorithm claim on every game, so TARGET.md §5's gauntlet
  does not apply, and it is not a step-4 pass. L-1 ends its scope words «so this is not M4; G-N5-TIME stays OPEN; not M3, not a step-4 pass,
  not a TARGET.md claim», the form of landed R123 and R124. GAPS G-N5-TIME: open.

Proposed GAPS line-11 UPDATE (append-only), to go AFTER the last UPDATE on GAPS l. 11 at landing (R125's, «UPDATE 2026-11-11 23:47Z: RESULTS
R125 (P-N5-CHAIN; CHECKER C139 1622c7d9)», the last at 0753fd71), as a pure insertion with one separating space before the row's closing
« |». BUILT FROM L-1 by tools/upd126a.py (R118's procedure: the direct build of r125b/tools/upd125b.py, unchanged, with R126's constants:
date «(2026-11-09)», start «for every genome G (Ξ-cycles and Ξ self-loops allowed), with class_t(v) := (Λ_t(v), E_t(v)), … (= R123's
D^tot_E(v)): » (the span up to the first label), its four labels «(Theorem GATE-CLASS)», «(Corollary GATE-FLIP)», «(Corollary QUIET-N,
sharpens RESULTS R123 Theorem QUIET / Corollary T-QUIET: window L → N)», «(Lemma (k+1)-Λ)», source prefix «(P-N5-QN, docs/new/P-N5-QN.md»),
with NO reading; controls on 0753fd71: the same function rebuilds R123's landed UPDATE (739c5f71…; filled with 2026-11-09, 00:52, 3479ecb0
it occurs once on l. 11: True), R124's (8cd83060…; 2026-11-09, 09:04, 5b9f4af8, once: True) and R125's (f22faed5…; 2026-11-11, 23:47,
1622c7d9: it ends l. 11, True); negative controls (an altered drop string; an altered label) raise errors. sha1
640258db370e0b6f3a217198375ee2399f6ec902 of the line without newline and unfilled (fb69fad69e0aa3f3353ec524630c72dfa4bd2155 with its
newline), 7386 bytes. <DATE>, <HH:MM> and <checker> are the landing date, time and the CHECKER commit of the PASS (C140), all filled at
landing:
UPDATE <DATE> <HH:MM>Z: RESULTS R126 (P-N5-QN; CHECKER C140 <checker>) [refereed-only] LANDED: In IDEAL-CYC(G) (RESULTS R118 (a): Γ(G) with every non-mover Even vertex frozen at R104's start, Odd unrestricted (gates and K2), Howard steps at the movers), for every genome G (Ξ-cycles and Ξ self-loops allowed), with class_t(v) := (Λ_t(v), E_t(v)), E_t(v) the e-vertices of Π_t(v), and loud / quiet steps as in RESULTS R123, flips(g) := #{t ≥ 1 : σ̄_(t−1)(g) ≠ σ̄_t(g)} and D^tot(v) := the number of distinct classes of v over the run (= R123's D^tot_E(v)): for every gate g and every step t, if σ̄_(t−1)(g) ≠ σ̄_t(g), then class_(t−1)(e_g) ≠ class_t(e_g) or class_(t−1)(β_g) ≠ class_t(β_g) (Theorem GATE-CLASS); (a) flips(g) ≤ (D^tot(e_g) − 1) + (D^tot(β_g) − 1) for every gate g; (b) with seq_t(v) and its ascents as in RESULTS R121, if every seq_t(e_g) and every seq_t(β_g) has at most B ascents, then flips(g) ≤ 2·((2M + 3)·F′_B(M) − 1) with F′_B of RESULTS R121, and under HYPOTHESIS [E-LEV] (lev(x) < lev(x′) implies pr(e_(x,k)) < pr(e_(x′,k′))) B = U(G), the number of options whose Ξ-target has a higher level, may be taken (Corollary GATE-FLIP); every quiet step is a p-step of RESULTS R118, every maximal window of quiet steps has at most N steps, and T_CYC ≤ Q + (Q + 1)·N, Q := the number of loud steps, Q ≤ Σ_v (D^tot(v) − 1) (Corollary QUIET-N, sharpens RESULTS R123 Theorem QUIET / Corollary T-QUIET: window L → N); with the Ξ-feedback number k := the minimum size of a set of movers meeting every cycle (self-loops count) of the Ξ-graph on the movers (an edge x → xt(x, j) for each option whose Ξ-target is a mover; options whose Ξ-target is X omitted): for every genome G with Ξ-feedback number k and every state t of IDEAL-CYC(G), the cycle nodes Λ_t(v), over all vertices v other than c_W, c_X and the e-vertices whose successor is c_W, take at most k + 1 values: K1, and, for each cycle of the functional graph Ξ_σ on the movers, x → xt(x, σ_t(x)), the most relevant vertex of the Γ-cycle through its movers, their chosen gates and β-faces; Ξ_σ has at most k cycles (premises: RESULTS R104's definitions of the genome and of Γ(G) only, including that the Odd vertices with a choice are the gates and K2; RESULTS R118 (a), (d) BR-SEG, (e) with its stated reason, R118's order ⊴ on values (Λ, Π, k) (VJ00 §4.2 / Friedmann arXiv 1106.0778 §3) and its step labels C / R / p; RESULTS R121 Lemma E-MON, and for GATE-FLIP (b) only R121's HUB-ASC-G whole-run form and UP-B; RESULTS R123 Lemma CN2, Lemma B-ONLY, Corollary NO-TIE, Lemma LOC-GATE, Lemma LOC-K2; R123 Theorem QUIET and Corollary T-QUIET are the bounds QUIET-N sharpens; [E-LEV] only in GATE-FLIP (b)'s U(G) form; not used: any lane packet, any L-RED or L-SI lane lemma, any P-N5-CHAIN fact) (Lemma (k+1)-Λ): this bounds per-gate flips and quiet windows only, in one restricted model; it makes no new class of genomes on which T_CYC is polynomial, and at k = 1 it bounds the cycle nodes only (whether max_g min(D^tot(e_g), D^tot(β_g)) is polynomial in N + M at k = 1 is OPEN); T bounds IDEAL-CYC iterations only; nothing is proved on Γ3: by RESULTS R118 (k) and (l), under REACH3-CYC's premises, N5′-xi from S3 on Γ3(G) makes Howard steps on Γ3 up to its first fallback, a run that can differ from the IDEAL-CYC run at exact VJ ties (R118's DATA), and a Γ3 form of this proof (not given here) would bound N5′-xi only up to its first fallback; nothing is claimed about post-fallback iterations, N5′-xi's total count, N5 or general games; DEAD (each with the instance that kills it; none is a premise): D1 «at k = 1 each gate flips at most 2·lamch(g) + 1 times», lamch(g) the number of steps at which Λ changes at e_g or β_g (experiments/new/box202/k1fail_202.json, sha1 99bba752, gate (4, 0): 2 flips, lamch 0); D2 «at k = 1 every gate flips at most c·(lamch(g) + 1) times», every constant c (L-RED 63's MWR(n), claude/l-red 406ef2fd, R229-box202 §2; copies experiments/new/box203/inst/MWR4_2.json sha1 856d369b, MWR8_2.json 918f1414, MWR16_2.json 2ccda9a9: gate (qz, 0) flips 2n + 1 times with lamch 0); D3 «every e-sequence has at most k + 1 ascents» (at k = 1 the staircase ST(m), box203/inst/ST4_k1.json sha1 3fa71a98, 3 ascents, and ST8_k1.json sha1 9dbf71f4, 7 ascents; at k = 2 L-SI's WC family, box202/inst/WC4_2, WC8_2, WC16_2: 4, 8, 16 ascents); DATA, clause by clause (scope IDEAL-CYC from the genome's start, cap 20,000 states, engine box191/idealcyc.py with experiments/si/si.py's Engine; tools in experiments/new/box203/, run in part by check203.sh; all pinned in box203/qn.pins): GATE-CLASS: lfail 0 (unit: flip steps at which neither face's class (Λ, E) changes); GATE-FLIP (a): gfail 0 (unit: gates with flips(g) > D^tot(e_g) + D^tot(β_g) − 2); QUIET-N: qflip 0 (unit: quiet steps at which σ̄ changes at some Odd vertex), qfail 0 (unit: runs with a maximal quiet window > N), Tfail 0 (unit: runs with T_CYC > Q + (Q + 1)N); all by gfc203.py on: the 57-genome corpus (the 53 box 202 genomes, MWR4/8/16_2, k1fail_202; out/gfc203_corpus.out), 1,000 rand191 genomes (d 1-6, w 1-3, degree 2-3, seed 2; out/rnd203_rand_s2.out), 5,000 k = 1 genomes (box202 k1srch202.mk, seed 202; out/rnd203_k1_s202.out), K1C16_n400 and K1F21_n48 (out2/gfc203_k1extra.out); control GFC_CTRL=3 (only the e-face's class looked at) fires, lfail 9 on MWR4_2 (check203.out); longest quiet window 10 at N 108 (DSALT6_n108) on this engine and 11 on REFEREE-2 35's engine, both ≤ N (Howard's tie rule is free in R118 (a)); (k+1)-Λ: lam203.py lfail 0 (unit: states with more than k + 1 values) on 2,000 k = 1 genomes (seed 7), 1,000 k = 2 genomes (seed 8) and 1,000 rand191 genomes (seed 2) (out2/lam203_*.out); lam203.py skips genomes with k > 12, and none of these 4,000 was skipped (unit: genomes; skip203.py, out2/skip203.out: k ≤ 5 on every genome); control LAM_CTRL=1 (bound k) fires, lfail 3,492 on the k = 1 set; k = 1 per-gate records (unit: flips of the gate with most flips; lamch 0; C = 0): MWR4/8/16_2 9 / 17 / 33, K1F21_n48 (N 48) 21, K1C16_n400 (N 113) 31; Γ3 counts (N5′-xi from S3 to its first fallback, same counters 0 on MWR4_2, MWR8_2, k1fail_202, C4_NM50, C6G8_n54, RWX_n95; out/gfc203_g3.out) are DATA only, nothing claimed; independent replays, every fail counter 0, their counters in their own pinned outputs, cited, not re-run: REFEREE 30 R-P-N5-QN §4 (claude/referee 452800c5; 1,500 runs and 8 pinned files), REFEREE-2 35 R2-P-N5-QN (claude/referee-2 5d4f06c2; 61 pinned genome runs and 6,000 random), L-RED 63 cls229 (29 rows; claude/l-red 8c034440) and lam229 (12 genomes; claude/l-red cdecc4e0); TARGET.md §2 (M4) asks for an algorithm polynomial on every parity game and §4 says a bound on a restricted class is not M4, so this is not M4 (P-N5-QN, docs/new/P-N5-QN.md, frozen at l-new e252182d, sha1 97254bd2, with fixes entry 1, docs/new/P-N5-QN-fixes.md; L-NEW successors 68-69; related lane statements, not premises: L-RED 63 Lemma CLASS-PAYS / Corollary GATE-FLIP-MIN (claude/l-red 8c034440, docs/red/R229-box203.md §3) and Lemma REL-G (claude/l-red fa4e50fe, docs/red/R229-box93.md §1.3), L-SI 49 NP-SHAPE / E-FACE-PAYS (claude/l-si f723957b, docs/si/box93-k7k6.md), L-SI 48 GATE-LOW-NULL (claude/l-si d962efdb, docs/si/box92-closed.md)). G-N5-TIME stays open.

Addendum (subagent, first fill; checks run on the pass-1 draft, whose title, entry block, GAPS preamble and UPDATE are byte-equal to this
file's; outputs r126a/*_p1.out; the final run on this file is r126a/*_final.out). Verbatim key lines, with «|» printed as «¦»:
  [chk] model: landed R125 title (0753fd71) == «### R125 [refereed-only] » + R125 L-5 + «, CHECKER PASS (docs/checker/C139.md, checker 1622c7d9)»: True
  [chk] file: sha1 d11ff4ca1616f9bb462420fd667b255cb5c8f221 bytes 63415 lines 377 ends with newline True
  [chk] ### R headings at d[...]: [186]
  [chk] (a) title == prefix + L-1 (no newline) + tail: True ; middle bytes == L-1 bytes without newline: True
  [chk]     title: 7299 chars, 7435 bytes, sha1 1d3f16d0fc97b15bf300569f28521c55bc1ac207, ( 141 ) 141, min depth 0, final 0, ¦ 0, fill token 1
  [chk] (e) entry block d[186:362] (lines 187-362, 176 lines, sha1 of the joined block aed54a937f0840bbe659f83d4fa191ad4b28c312); next line blank: True; line after: 'Proposed GAPS line-11 UPDATE (append-onl'
  [chk] (b) fill token in the entry block: 1 ; in the whole file: 1 at lines [187]
  [chk]     «\n**Erratum E-1** (not a result» in the block: False ; line-start «**Erratum» in the file: 0 ; empty lines inside the block: 0
  [chk] (e) UPDATE line(s) at d[...]: [375] (line [376])
  [chk]     GAPS preamble at d[363:375]
  [chk] (c) "¦" in entry block: 0 ; in UPDATE: 0 ; in GAPS preamble: 1 (the quoted « ¦» of the row end); in the file: 8
  [chk] (d) UPDATE <DATE> 1 <HH:MM> 1 <checker> 1; head at its start: True
  [chk]     UPDATE = upd126L1.txt: True ; sha1 (no newline) 640258db370e0b6f3a217198375ee2399f6ec902 ; with newline fb69fad69e0aa3f3353ec524630c72dfa4bd2155 ; 7386 bytes ( 140 ) 140
  [chk]     stale grep, entry block minus title (case-insensitive): {}
  [chk]     stale grep, title: {'pending': 1} ; UPDATE: {}
  [chk]     line 1 «NOT LANDED» 1 ; «<DATE>» in file 2 ; «<checker>» 2 ; «<HH:MM>» 2
  [chk] (e) slices: line 1 d[0]; FIRST FILL record d[1:185] (+ blank d[185]: ''); title d[186]; entry d[186:362]; blank d[362]; preamble d[363:375]; UPDATE d[375]; blank d[376]: ''; Addendum none
  [chk] (f) QUOTE SWEEP (corpus: 69 texts)
  [chk]     sweep line 1: 1 quotes, 1 parts, 0 not found []
  [chk]     sweep FIRST FILL record: 147 quotes, 125 parts, 0 not found []
  [chk]     sweep entry block: 124 quotes, 122 parts, 0 not found []
  [chk]     sweep GAPS preamble + UPDATE: 12 quotes, 12 parts, 0 not found []
  [chk]     sweep whole file: 284 quotes, 260 parts, 0 not found []
  [chk]     sweep NEGATIVE CONTROL: 1 quotes, 1 parts, 1 not found ['QUIET-N bounds T_CYC by N squared on every genome']
  [chk]     negative control reported missing: True
  [lp] cites 121 (114 shown in the draft as «quote», 7 used for a line number only) in 14 (commit, file) pairs; failed at the cited lines: 0 []
  [lp] shown quotes not in the draft as «quote»: 0 []
  [lp] NEGATIVE CONTROL 1 (window shifted by 40 lines): 0 of 121 still pass []
  [lp] NEGATIVE CONTROL 2 (longest word mutated): 0 of 121 still pass
  [lp]     02a928a3 docs/new/P-N5-QN-fixes.md 12
  [lp]     0753fd71 TARGET.md 1
  [lp]     0753fd71 docs/DECISIONS.md 3
  [lp]     0753fd71 docs/RESULTS.md 26
  [lp]     0753fd71 docs/checker/C138.md 1
  [lp]     0753fd71 docs/new/P-N5-XICYC.md 1
  [lp]     09aabb03 docs/referee/R-P-N5-QN.md 8
  [lp]     406ef2fd docs/red/R229-box202.md 2
  [lp]     452800c5 docs/referee/R-P-N5-QN.md 15
  [lp]     565d5022 docs/referee-2/R2-P-N5-QN.md 5
  [lp]     5d4f06c2 docs/referee-2/R2-P-N5-QN.md 19
  [lp]     a327b4dc docs/referee-2/R2-P-N5-QN.md 9
  [lp]     e252182d docs/new/P-N5-QN.md 16
  [lp]     f05b0c55 docs/red/R229-box203.md 3
  [hex] hex ids in the draft: 73; git objects 48; measured sha1s (not objects) 25; neither: 0 []
  [hex] NEGATIVE CONTROL (0badc0de1, 1234abcd9f): neither: 2 ['0badc0de1', '1234abcd9f']
  [sim] trunk 0753fd71 RESULTS sha1 9170163bf892f96f38009c1e11f87bce9764b6e2 lines 16368 "¦" 1477 ; GAPS sha1 dbb55831a88223706bbaa9105f5397f3cea3d6e2 lines 23
  [sim] pure insertion: prefix byte-unchanged True ; suffix byte-unchanged True ; inserted lines 177
  [sim] headings after insertion: {'R124': [15371], 'R125': [15595], 'R126': [15726], 'E-1': [15903], 'E-2': [15916], 'E-3': [15944], 'Dead': [15975]}
  [sim] R125 at l. 15595 (unchanged: True); R126 at l. 15726-15901, blank l. 15902 (''), «**Erratum E-1**» l. 15903; the line before R126: l. 15725 '' (R125's block ends l. 15724)
  [sim] order R124 < R125 < R126 < E-1 < E-2 < E-3 < Dead ends: True
  [sim] RESULTS lines 16368 -> 16545 (+177) ; "¦" 1477 -> 1477 (unchanged True) ; «checker 3333333)» once True ; fill token 0
  [sim] ### R1xx headings: 27, R126 the last: True
  [sim] GAPS: only l. 11 changes True ; lines 23 -> 23 ; l. 11 "¦" 76 -> 76 ; «UPDATE 2026-» 60 -> 60 ; R126 last: True ; after R125's (2026-11-11 23:47Z, 1622c7d9): True ; prefix byte-unchanged: True
  [sim] GAPS whole file "¦" 198 -> 198
  [sim] fill values used only here: 2099-01-11 00:00 3333333
