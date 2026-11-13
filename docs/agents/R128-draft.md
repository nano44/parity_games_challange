# Draft RESULTS R128 (Lead; first fill 2026-11-12T14:10:56Z by date -u (subagent) on P-N5-GATE line L-4, docs/si/P-N5-GATE-line-L4.txt, l-si 676b6a1c, sha1 6bfde78ef050b47f43527875256c65a205869e77) — to CHECKER C142 — NOT LANDED; goes after R127 (landed at trunk f9520557, RESULTS l. 15903-16125), directly before the line-start «**Erratum E-1** (not a result» (l. 16127 at f9520557); its GAPS UPDATE after R127's on GAPS l. 11
FIRST FILL (this text). Built by script (r128a/fill1.py) in the scratchpad r128a/ for the Lead to copy to docs/agents/R128-draft.md; nothing
  in the repository was edited, committed, merged or pushed by me, and scripts/push.sh and scripts/verify.sh were not run (a Lead push was
  running; I used read-only git, git archive and the old-style read-only git merge-tree only; git status clean after). Read at the origin
  heads of one git fetch of claude/l-si, claude/referee, claude/referee-2, claude/checker and claude/l-new right after «Thu Nov 12 13:59:39
  UTC 2026» (date -u, recorded before the fetch), rc 0 (r128a/fetch.txt; it moved only l-si, 2d2f9a0e..b2520ec7). The trunk was not fetched:
  my ref origin/claude/vibrant-johnson-nxvvxo is a9699c30, and f9520557 is not its ancestor (consistent with "being pushed now").
HEAD l-si b2520ec7 (b2520ec71b815e1bbf8964bce1d7a66f9f7cec07, 2026-11-12T12:46:14Z, «L-SI box 103: MOVER-DEEP3 at k = 1; Lemma GAIN-COUNT
  (PROVED lane); MOVER-DEEP3 <= CONJECTURE NOLOSS; NOLOSS-k1 data 0 at k = 1; DEAD e-depth <= 1 at …»).
HEAD referee a0574a6b (a0574a6b15d78e665eed717330f48d38aaea4818, 2026-11-12T11:46:06Z, «REFEREE s32: handover check (five questions),
  measured at 175f125d / trunk 9c83214f»).
HEAD referee-2 f2793d9a (f2793d9aecf0c9692204af72f96878b104f4a1ef, 2026-11-12T13:04:33Z, «REFEREE-2 37: HANDOVER (park at ~521k, Lead
  13:06Z): no open items; next C141 / GATE R128; tools and traps»).
HEAD checker 850e9765 (850e9765c94d01ab0db3f1d90460497b6303de04, 2026-11-12T12:44:28Z, «CHECKER C141: R127 (P-N5-SPLIT) on L-3 a8661c4b PASS
  (trunk 471aba45, draft 9963b57c; UPDATE 5bd83938; blocks 197-199 + P-N5-SPLIT rc 0 from archive 6…»).
HEAD l-new 8db300fe (8db300fe3fd8e868e61851a9bff76673146d2f10, 2026-11-12T12:08:32Z, «L-NEW successor 72 BOX 208 (all CANDIDATE; scope
  IDEAL-CYC on Gamma(G) only): Lemma LEVEL (lowest lagging class; a stall puts a whole Xi_(sigma_b)-cyc…»).
After my fetch another process moved origin/claude/l-si to bce4f398 (bce4f3986aa9c253da8e1bf8588e8af581b0c5e8, 2026-11-12T13:29:28Z, «L-SI
  successor 51: box 101 Add. E (REFEREE 32 pre-read of RESTRICT-C: (iv) replaced by BR-SEG form, W-2, C-1, N-1) + box 103 Add. A (box 208…»;
  docs/si/box101-lamgap.md, box103-moverdeep.md and notes/L-SI.md only); every head above is the one my fetch gave and an ancestor of the
  current ref, and the GATE objects and the check.sh block below are byte-equal at bce4f398 too.
No P-N5-GATE object changed after its last commit: the packet, the fixes file, L-4, experiments/si/box90-box96 are byte-equal at 676b6a1c
  and at the l-si head b2520ec7 (git diff --stat empty; 12 l-si commits after 676b6a1c, none touching them); docs/referee/R-P-N5-GATE.md
  (412 lines, sha1 f239bce194b83e6a0f08118bfd60caffe6206e12) is byte-equal at 49d34123, at the referee head a0574a6b and at f9520557;
  docs/referee-2/R2-P-N5-GATE.md (586 lines, sha1 27ada71660509152a7f193ebf9ed3fc043b4907a) at 3282fc6c, at the referee-2 head f2793d9a and
  at f9520557. The brief's facts were checked by script (this file's asserts and the tools): every one MATCHES except where BRIEF FACTS
  below say otherwise.
LINE OF RECORD: docs/si/P-N5-GATE-line-L4.txt, COMMIT 676b6a1c (676b6a1c9ebc658701a87567cf0ec78e6d108faf, 2026-11-12T04:09:12Z, «L-SI:
  P-N5-GATE fixes entry 4 + line L-4 (LT-1: SPLIT as RESULTS R127, landing-order form; GT-10 / L43: GL-1..GL-3 verbatim from REFEREE 31
  fbc4d865 §J)»), the file's only commit; FILE sha1 6bfde78ef050b47f43527875256c65a205869e77 (git show | sha1sum; blob
  47a09c227d61a5a37ae1a2a79c09c0704b534617), 12,562 bytes, one line with its newline, 230 «(» = 230 «)», 0 «|», one « — », «(2026-11-09)»
  once. L-1 a44647db (ecc5fe25), L-2 c0f2007d (9c0349b1), L-3 b60495b2 (ef14451f), each its file's only commit.
PACKET: docs/si/P-N5-GATE.md FROZEN at 4066f579 (4066f579cb6db24e447322a024d8edd75ec5f9cb, 2026-11-09T06:36:22Z, «L-SI box 95: packet
  P-N5-GATE (frozen): GATE-RACE/TRIGGER, GATE-LOW-NULL, NP-SHAPE, E-FACE-PAYS/WAIT-QUIET, SAME-SUFFIX/STEP-BOUND, PARALLEL, PAIR-EXP…»), the
  file's only commit; sha1 f3a584e68b5c998276ea717f42920bdeeca581ab, 230 lines, 25,604 bytes. FIXES: docs/si/P-N5-GATE-fixes.md, four
  commits only: entry 1 at ecc5fe25 (2026-11-09T08:40:46Z; 84 lines, 8,557 bytes, sha1 00cf406d…), entry 2 at 9c0349b1
  (2026-11-09T10:05:10Z; 116 lines, sha1 1fec4f8c…), entry 3 at ef14451f (2026-11-12T01:50:52Z; 246 lines, sha1 e79455ea…), entry 4 at
  676b6a1c (284 lines, 28,767 bytes, sha1 8009e0183159a1134f426ab2ee9a01e5b690eb52); append-only (each earlier text is a byte prefix of the
  next). GENERATORS experiments/si/box95/fix1/mkL1.py … fix4/mkL4.py (L-k from L-(k−1); L-1 from the packet), mkfix1.py … mkfix4.py,
  check_fix1.sh … check_fix4.sh (box95/check95.sh).
REFEREES (git blame at the heads). REFEREE docs/referee/R-P-N5-GATE.md, all REFEREE successor 31: l. 1-179 §1-§2 731db590
  (2026-11-11T22:51:49Z), l. 180-319 §3-§8 and §0 a401ce0e (2026-11-11T23:29:45Z), l. 320-368 §I 41228433 (2026-11-12T02:50:26Z), l. 369-395
  §J fbc4d865 (2026-11-12T03:28:29Z), l. 396-412 §K 49d34123 (2026-11-12T05:09:52Z, «REFEREE s31: R-P-N5-GATE §K: fixes entry 4 CORRECT,
  line L-4 MATCHES (L-3 + LT-1 landing-order form + GL-1..GL-3)»). REFEREE-2 docs/referee-2/R2-P-N5-GATE.md, all REFEREE-2 successor 37: l.
  1-274 boxes 1-3 a28bc5e1, l. 275-334 §3.5 276545dc, l. 335-420 box 4 with the verdict table c035b35f (2026-11-12T00:50:26Z), l. 421-479
  Addendum 1 8983b3d8 (2026-11-12T01:14:17Z), l. 480-533 Addendum 2 6269fec5 (2026-11-12T02:50:37Z), l. 534-573 Addendum 3 93413fc6
  (2026-11-12T05:10:00Z, «REFEREE-2 37: R2-P-N5-GATE Addendum 3 — L-4 (l-si 676b6a1c, sha1 6bfde78e) MATCHES: LT-1 (R127 under the
  landing-order ruling; R126/R127 not yet on tr…»), l. 574-586 Addendum 4 3282fc6c (2026-11-12T05:40:10Z).
BOTH REFEREES SAY L-4 MATCHES (VERIFIED). REFEREE 31 §K (49d34123) l. 411-412 «Verdict: fixes entry 4 CORRECT. **Line L-4 MATCHES** (L-3 +
  exactly LT-1, GL-1..GL-3 and the entry count). Statements and labels as in §0 and §I: every statement SIGN; the Γ3 rows on LANDED R125;
  A*-EQUIV (ii), (iii) CONDITIONAL on R127 (P-N5-SPLIT).». REFEREE-2 37 Addendum 3 (93413fc6) l. 569-570 «Verdict: L-4 (676b6a1c, sha1
  6bfde78e) MATCHES. L-3's match carries over unchanged, and the two new items (LT-1 under the landing-order ruling, GT-10 / L43) are
  correct in bytes and in meaning.». SIGN verdicts: REFEREE 31 §0 (a401ce0e) l. 305 «No GAP; nothing REFUSED.»; REFEREE-2 37 box 4
  (c035b35f) l. 407 «No statement is REFUSED. No signed proof keeps an open gap.»; Addendum 1 (8983b3d8) l. 423 «Verdicts: equal on every
  row. Both referees SIGN every statement, none REFUSED, no GAP.» and l. 478 «Result: P-N5-GATE has two referee signatures on every
  statement, with the conditions above.».
BRIEF FACTS THAT DID NOT MATCH, OR NEED A QUALIFIER: (1) "entry 4's fixes file commit 8009e018": 8009e018 is not a commit (git rev-parse
  fails; no object has that prefix); it is the FILE sha1 of docs/si/P-N5-GATE-fixes.md at 676b6a1c
  (8009e0183159a1134f426ab2ee9a01e5b690eb52), as REFEREE §K and the Lead state log («fixes entry 4 (8009e018)» (l. 3137)) use it; entry 4
  and L-4 are one commit, 676b6a1c. (2) "Both are now merged into trunk ancestry? Check which needed commits are NOT ancestors": every
  REFEREE and REFEREE-2 commit of R-P-N5-GATE / R2-P-N5-GATE IS an ancestor of f9520557, but NONE of the l-si commits is:
  docs/si/P-N5-GATE*.md do not exist at f9520557; the merge base of f9520557 and 676b6a1c is 547985a1 (2026-11-09T06:22:48Z, the Lead's,
  before the freeze 4066f579), and 38 l-si commits 547985a1..676b6a1c (309 files, all docs/si/, experiments/si/, notes/L-SI.md and
  docs/agents/handover-checks/L-SI.md) are unmerged (G-MERGE). (3) The LT-1 ruling time: fixes entry 4 says «Lead's ruling (02:57Z)» (l.
  255); REFEREE §K «as ruled by the Lead (02:52Z)» (l. 405); the Lead state log at f9520557 «02:52Z Lead ruling LT-1: landing-order
  alternative» (l. 3113); same content, two times (note). (4) "REFEREE 31 … (and earlier §1-§8, §0, §I, §J)": all of R-P-N5-GATE.md is
  REFEREE successor 31's (no successor-30 part), as listed above. (5) Not in the brief: «P-N5-GATE» is already the packet name of landed
  RESULTS R101 (L-NEW, docs/new/P-N5-GATE-box120.md; GAPS «UPDATE 2026-11-01 05:28Z: RESULTS R101 (P-N5-GATE; CHECKER C111 d53e1d4f)»)
  (G-6). (6) "premises only from landed RESULTS": L-4 cites four items, F2, CYC, (E-DOM), (Core), from «P-N5-CHAIN's frozen text (l-new
  93531b03, sha1 6e613ba7, §2 and §4)», as R127 did (G-4; C141 ruled R127's case no action). Everything else matched: f9520557, R127 =
  P-N5-SPLIT at RESULTS l. 15903-16125, Erratum E-1 l. 16127, 16,769 lines, 1,477 «|»; GAPS l. 11 76 «|» ending with R127's UPDATE; packet
  frozen at 4066f579 (sha1 f3a584e6…); fixes entries 1-4; L-4 at 676b6a1c, sha1 6bfde78e…, 12,562 B; box95 fix1..fix4 and check95.sh; both
  referees MATCH L-4 (REFEREE §K 49d34123, REFEREE-2 Add. 3 93413fc6, Add. 4 3282fc6c); C142 unused (G-0); LT-1 now TRUE (G-LT1).
ANCESTRY (git merge-base --is-ancestor against trunk f9520557): REFEREE's 731db590, a401ce0e, 41228433, fbc4d865, 49d34123; REFEREE-2's
  a28bc5e1, 276545dc, c035b35f, 8983b3d8, 6269fec5, 93413fc6, 3282fc6c; P-N5-CHAIN's frozen text 93531b03; P-N5-SPLIT's freeze 399cda07 and
  its line commit 621e6b77 (R127); L-NEW fcba92fc (the g3 engine the packet's DATA pins, §6): ALL ancestors (True). NOT ancestors (True):
  the packet, fixes and line commits 4066f579, ecc5fe25, 9c0349b1, ef14451f, 676b6a1c (G-MERGE: merge claude/l-si at 676b6a1c, or a later
  l-si head, before landing; old-style git merge-tree 547985a1 f9520557 676b6a1c reports no conflict, and no trunk path outside the lane's
  is touched but docs/agents/handover-checks/L-SI.md, the lanes' usual handover file); records named in L-4 or the packet, not premises:
  L-RED 406ef2fd (MWR instances, cited in L-4), fa4e50fe (dexact, cited in L-4), 8c034440, 2730ab90, 98143eab, f3903cb8, 4b309716 (the own
  engine the box checks archive), L-SI 47's box 90 commits 4ded1e8d (FW) and 2d0344d3 (MW; the RA path count and m = n of GL-3 come from
  there, data128a.py). L-4 names two of these, 406ef2fd and fa4e50fe, both as DATA sources (as C138 §5 ruled for L-RED commits).
BASE: trunk f9520557 (f9520557522624a80cceb1b7851eea74531b3017, 2026-11-12T13:59:01Z, «Lead: land R127 (P-N5-SPLIT) after CHECKER C141 PASS
  (850e9765); GAPS line-11 UPDATE; log 12:57Z-13:58Z (box 208 survives three independent checks; L-…»), R127 landed: RESULTS sha1
  4117c8a7d0165cd8d3a880f9a405d9c6fc6a5089, 16,769 lines, 1,477 «|»; «### R127» l. 15903-16125 (blank l. 16126), the line-start «**Erratum
  E-1** (not a result» l. 16127 (the only one); GAPS sha1 ccf059a1558fc3e1ae769a7aa98506f5fa7d64d5, 23 lines, l. 11 76 «|», its last UPDATE
  R127's («UPDATE 2026-11-12 13:58Z: RESULTS R127 (P-N5-SPLIT; CHECKER C141 850e9765)»). No simulated base is needed (L-4 cites no RESULTS
  id above R127).
SOURCES READ: the packet (4066f579) in full; the fixes file (676b6a1c) entries 1-4 (entry 4 and the L-k notes in full, entries 1-3 by
  heading and item); L-4 in full; L-1..L-3 by sha1; box95/check95.sh, check_fix1..4.sh, mkL1..4.py (heads), quotesL1.py;
  experiments/si/check.sh l. 1279-1290; the outputs of box90-box96 (by data128a.py); REFEREE's R-P-N5-GATE.md l. 1-30, 181-212, 286-412;
  REFEREE-2's R2-P-N5-GATE.md l. 1-20, 338-421, 422-586; P-N5-CHAIN.md (93531b03) l. 96-97, 165-166; RESULTS (f9520557) R101 l. 9251, R104
  l. 9864, R117 l. 13362, R118 l. 13607-13878, R121 l. 14320, R123 l. 15076, R125 l. 15595, R126 l. 15726, R127 l. 15903-16125; GAPS l. 11;
  DECISIONS L41 (l. 355-360), L43 (l. 369-374); docs/checker/C141.md (f9520557); the Lead state log l. 3113-3141, 3237-3246; the R127 first
  fill (039b0558) and its tools r127a/ (adapted).
CHECKS RUN AT THIS FILL (scratch r128a/; outputs there). (a) The l-si check blocks for P-N5-GATE, experiments/si/check.sh l. 1279-1290 at
  676b6a1c (boxes 91-96: census rows, controls, the fix1..fix4 chain, PROVISO; the same 12 lines at 9c0349b1, ef14451f and the l-si head;
  sha1 bfee3e33a6f4e82e760e5e7429769a6f72d90f49; = tools/blocksGATE.sh, run by tools/runblocks.sh) from a FULL git archive of 676b6a1c
  (r128a/arch/, 48,670 files = the tree): first as a bare archive, 2026-11-12T14:03:00Z-2026-11-12T14:03:01Z by date -u, rc 0, all PASS / OK
  but the five boxes' engine rows printed «NOT RUN engine rows (pinned commit 4b309716 absent)» (the archive is no git repository); then
  with the repository's object store made visible read-only (GIT_DIR, GIT_WORK_TREE = the archive, a scratch GIT_INDEX_FILE; MODE=git),
  2026-11-12T14:03:07Z-2026-11-12T14:03:25Z, rc 0, output «BOX91 OK», «BOX92 OK», «BOX93 OK», «BOX94 OK», «P-N5-GATE fix1 checks: PASS» …
  «P-N5-GATE fix4 checks: PASS», «BOX96 checks: PASS», no NOT RUN. Negative control 1: one byte appended to the archive's L-4, the «box 95»
  block alone (tools/block95.sh): 2026-11-12T14:03:39Z-2026-11-12T14:03:39Z, rc 1, «BOX95 FAIL fix4» (fix1-fix3 PASS); byte restored (sha1
  6bfde78e again), block re-run PASS (rc 0). Negative control 2: one byte appended to the «own MW8_2.json» row of the archive's
  box91/out/own91.out (a pinned output), the «box 91» block alone (tools/block91.sh): 2026-11-12T14:03:40Z-2026-11-12T14:03:44Z, rc 1,
  «BOX91 FAIL own rows»; file restored (cmp equal to its backup) and all blocks re-run 2026-11-12T14:03:44Z-2026-11-12T14:04:02Z, rc 0. (b)
  mk.out: the lane's chain fix1/mkL1.py → fix2/mkL2.py → fix3/mkL3.py → fix4/mkL4.py from a git archive of 676b6a1c (docs/si,
  experiments/si/box95), each output written over the archived L-(k) before the next step; RESULTS = trunk f9520557's (the chain's
  generators do NOT read RESULTS: mkL1.py reads the packet only; only fix1/quotesL1.py reads it, and it reports «quotes: 12 of 12 verbatim»
  at f9520557, rc 0): L-1, L-2, L-3, L-4 each cmp SAME (L-4 6bfde78e…, 12,562 B), and mkfix1..4.py rebuild the fixes file byte-equal
  (8009e018…). In the archive run (a) check_fix1.sh read the archive's RESULTS, the l-si base (676b6a1c's docs/RESULTS.md, last changed at
  9acebb5c, 16,013 lines, before R124-R127 landed). (c) tools/upd128a.py: the UPDATE by R118's procedure, with controls R125, R126, R127 on
  f9520557 and two negative controls (upd128a.out). (d) tools/prem128a.py: L-4's premises at f9520557 with negative controls (prem128a.out).
  (e) tools/data128a.py: L-4's DATA and DEAD figures against the pinned outputs (data128a.out, 48 checks OK, «DATA EQUAL»). (f)
  tools/chk128a.py (title, block, UPDATE, tokens, pipes, anchors, stale grep, quote sweep with a negative control), tools/lp128a.py (every
  quote of this file at its cited file, commit and lines, two negative controls), tools/hex128a.py (every hex id, negative control) and
  tools/sim128a.py (landing simulation on f9520557): Addendum.
LESSONS APPLIED (R127's fills, C141 and earlier). C113 E-1 / C133 E-1: the title is L-4 verbatim (CLEAN). C133 E-3 / C138 E-1 / C139 E-1:
  R118's procedure with no reading (G-U: two mechanical deviations, FLAG). C118 E-1 / C139 E-2: no status word stale at landing (G-S:
  CLEAN). L43 / C140 E-1 / REFEREE §J (G-L43: GL-1..GL-3 applied; two residual notes). L41 / C141 G-7 (G-7: note). C134 N-S (G-1: note).
  C115 E-1 / C141 G-4: premises landed only (G-4: note, C141 precedent). REFEREE §K and REFEREE-2 Add. 3 landing condition on R127 (G-LT1:
  MET). C120-C141: every DATA clause against its counter (G-9: EQUAL; notes). C122 G-0: parentheses. C130 G-P: the UPDATE builder with
  controls on the last landed UPDATEs. C132 Add. 1: block re-run times as a date -u interval. New here: unmerged lane commits (G-MERGE) and
  a packet-name clash with a landed entry (G-6).
FLAGS FIRST (my reading; CHECKER rules; strings below are PROPOSALS only).
- G-MERGE, THE LANE'S OBJECTS ARE NOT IN TRUNK (FLAG for the Lead; before landing). docs/si/P-N5-GATE.md, -fixes.md, -line-L1..L4.txt and
  experiments/si/box95/fix1-fix4 do not exist at f9520557; claude/l-si was last merged at 547985a1 (2026-11-09T06:22:48Z), 13 minutes before
  the freeze 4066f579 (06:36:22Z). The entry names these files as its object and source (title source note, Object, Fixes, Data), and
  scripts/verify.sh runs experiments/si/check.sh, whose box 95 block needs docs/si/P-N5-GATE-line-L1..L4.txt and the fixes file. Merge
  claude/l-si at 676b6a1c (or a later head: b2520ec7 at my fetch, bce4f398 now, 12 / 13 further L-SI commits, boxes 99-103, none touching
  GATE objects; the Lead's call) before landing, as R127's landing merged l-new 621e6b77; old-style merge-tree: no conflict. Commits to
  merge: 4066f579, ecc5fe25, 9c0349b1, ef14451f, 676b6a1c (and their 38-commit range from 547985a1). The referee commits are already in
  trunk. Then CHECKER C142's commit. C142 §3 (second fill): «Merging l-si at 676b6a1c, not the later heads, is the Lead's call. No
  objection. At the second fill, merge the L-5 commit instead.» (l. 69) MERGE LIST FOR LANDING (second fill; CHECKER rules): claude/l-si at
  7b0a58ae, the L-5 commit, which contains 676b6a1c (and 4066f579, ecc5fe25, 9c0349b1, ef14451f) and 19 later L-SI commits, oldest first
  (git log --oneline 676b6a1c..7b0a58ae; subjects in Addendum (second fill)): 9a490206, f65e0fb9, 53c72ec3, 9bb7bd43, 8a884bb2, 3b6ae726,
  23d39400, 4fda7245, 144f6821, 2d2f9a0e, d8945c4a, b2520ec7, bce4f398, 659a2d09, 26704e01, 01900837, 925577fe, a9ea60b9, 7b0a58ae; that is
  57 commits since the merge base 547985a1 with trunk 85e42158 (and with the Lead's local 21b87e70); old-style git merge-tree 547985a1
  85e42158 7b0a58ae: rc 0, no conflict marker. NEW: three commits the entry cites are NOT trunk ancestors at 85e42158, so they merge too:
  REFEREE §L 16e8dcb0 (claude/referee head), REFEREE-2 Add. 5 0df0fdd8 (claude/referee-2's head 43824abc is 3 commits later, P-N5-LEVEL
  review), and CHECKER C142 269effb3 (claude/checker head); the first fill's note that the referee commits were already in trunk held for
  49d34123 and 3282fc6c only. Merging 7b0a58ae puts experiments/si/check.sh's box 99-104 calls into the gate: run on the archive of
  7b0a58ae, 2026-11-12T21:54:42Z-2026-11-12T21:54:46Z, rc 0, «BOX99 checks: PASS» … «BOX104 checks: PASS».
- G-6, NAMES (FLAG; CHECKER's call). «P-N5-GATE» is already a landed packet name: RESULTS R101 (l. 9251) ends «(P-N5-GATE,
  docs/new/P-N5-GATE-box120.md with its fixes entry 1, docs/new/P-N5-GATE-fixes-box120.md; L-NEW successors 43-44)», its GAPS UPDATE head is
  «UPDATE 2026-11-01 05:28Z: RESULTS R101 (P-N5-GATE; CHECKER C111 d53e1d4f)», and RESULTS has «P-N5-GATE» 8 times, all R101's (l.
  9251-9362); docs/referee/R-N5-GATE.md and docs/referee-2/R2-N5-GATE.md are R101's reviews. R128's UPDATE head would read «RESULTS R128
  (P-N5-GATE; CHECKER C142 <checker>)», the same packet name as R101's. The two are told apart only by path (docs/new/P-N5-GATE-box120.md vs
  docs/si/P-N5-GATE.md) and by R-id. Options (not strings to apply): accept (R-ids and paths disambiguate); or qualify in the entry's text
  only (e.g. "P-N5-GATE (L-SI, docs/si/)") without touching L-4. Other names, counted in RESULTS at f9520557 (by script): «GATE-RACE» 0,
  «TRIGGER» 22, «GATE-LOW-NULL» 2, «NP-SHAPE» 2, «E-FACE-PAYS» 2, «WAIT-QUIET» 0, «SAME-SUFFIX» 0, «STEP-BOUND» 0, «PARALLEL» 0,
  «PAIR-EXPEL» 0, «EXPEL-COUNT» 0, «A*-EQUIV» 0, «PROVISO» 0, «R128» 7, «C142» 0. Of these, «TRIGGER» is a landed lemma name of R107 (l.
  10593, «(TRIGGER) the Ξ-order of (z, o′) and (z, o)», and 21 other occurrences, none GATE's), so this entry's would be cited as "RESULTS
  R128 Corollary TRIGGER"; «GATE-LOW-NULL», «NP-SHAPE» and «E-FACE-PAYS» occur only in R126 (title l. 15726 and l. 15842), as «related lane
  statements, not premises» (L-SI 48 / 49, claude/l-si d962efdb / f723957b), the lane statements this entry now lands; «R128» occurs only as
  the L-RED report id R128 («L-RED R128»; 6 lines, l. 6116-6310), not as a RESULTS id. C142 §3 (second fill): ««P-N5-GATE» (R101's packet
  name too): no line change.» (l. 70): no action; «TRIGGER»: C142 E-4, FIXED in the entry text: Honest limits (vii) now ends with C142's
  string ««TRIGGER» is also R107's; this entry's is «RESULTS R128 Corollary TRIGGER».» (C142 l. 59-60).
- G-L43, DEAD LIST AFTER GL-1..GL-3 (residual notes; CHECKER's call). GL-1..GL-3 are applied verbatim (REFEREE §J strings; REFEREE §K
  «GL-1..GL-3: my strings, verbatim (GT-10 / L43).» (l. 409)): RA-MULT, the polynomial RA-path bound and K1-FLIP(c) leave the DEAD clause
  and enter as DATA with numbers (all three) and a source commit for the MWR row only («L-RED 63, claude/l-red 406ef2fd»). DECISIONS L43 (l.
  369-374) «it enters as DATA with its numbers and source commit, or not at all» (l. 371). (i) The RA-MULT and RA path rows name instances
  and numbers but no source commit: the numbers «re-arm multiplicity m = n» and «P = F_(d+2) − 1» are box 90's
  (experiments/si/box90/out/mw90.out maxm 8 / 32 on MW8_2 / MW32_2; fw90.out maxP 54 / 2583 on FW8_2 / FW16_2, data128a.py), committed by
  L-SI 47 at claude/l-si 2d0344d3 (MW) and 4ded1e8d (FW), not by box 91, whose outputs carry C only; the instances are box91 inst (sha1
  66b84dcb, 445031d1, 108a63cf, 94df42b7, dropped from the line by GL-1). Neither referee re-counted m or P (REFEREE §3.3 «P = F_(d+2) − 1
  NOT re-counted» (l. 204); REFEREE-2 Add. 4 «Still cited, not re-run: the re-arm multiplicity m = n, the RA path count P = F_(d+2) − 1, and
  Γ3 on these two instances.» (l. 585)). PROPOSED (optional, a line change both referees re-sign): after «on FW8_2, FW16_2» insert " (L-SI
  47 box 90, claude/l-si 2d0344d3 and 4ded1e8d)". (ii) The growth clause «growth: C, A*_all and the largest gate flip count are linear in n
  on every family measured (MW(n): C = 2n + 1, flips 4n + 2; MWR(n): flips 2n + 1 = 2·ch_D + 1 with lamch 0, which makes E-FACE-PAYS (d)
  tight)» states family formulas read off finitely many n (REFEREE §J «as DATA they are acceptable only as numbers on the named instances
  (optional: «on n = 4, 8, 16» / «on n = 8, 32»).» (l. 394-395)); it names no instance and no source commit. Not a DEAD; CHECKER's call
  whether L43's «A DATA label does not cure an overclaim» applies to «linear in n on every family measured». (iii) The construction rows
  that stay DEAD (WC, K6 LAG TOWER, K7, nesting multipliers H = 2, 3, Db / Dbr): each says a named construction does not produce growth,
  with measured numbers; the Lead ruled them DEAD at 03:00Z (state log «03:00Z Lead: GT-10 accepted (construction rows stay DEAD)» (l.
  3116)) and both referees agree (REFEREE §J; REFEREE-2 Add. 3 «The construction rows (WC, K6, K7, nesting, Db / Dbr) stay DEAD. Each says a
  named construction fails to grow, which a finite instance can show. I agree.» (l. 567-568)). CLEAN as ruled. (iv) WC: L-4 «T3 = 4 at n =
  4, 8, 16; WC4_2, WC16_2»: WC8_2 is pinned in box90/inst (sha1 69a39335), not in the four inst dirs the clause names; REFEREE D-7 optional
  («D-7 (WC «n = 4, 16» or pin n = 8)» (l. 280)). Note. C142 §3 (second fill): «(i) → E-1. (ii) → E-2. (iii) The construction rows stay
  DEAD: clean, as the Lead ruled at 03:00Z.» (l. 79) E-1 and E-2 FIXED in L-5 by C142 §4's R-E1 and R-E2 (fixes entry 5 F5-1, F5-2); (iii),
  (iv) no action.
- G-U, THE UPDATE PROCEDURE (FLAG; two mechanical deviations, no reading). (i) Connector: L-4 joins PAIR-EXPEL and EXPEL-COUNT with «, and »
  («at the later one, and (Corollary EXPEL-COUNT) the number»), not «; »; the landed builder (direct(), r127a/upd127a.py, unchanged) asserts
  «; » and refuses L-4 (upd128a.out). direct2() accepts «; » or «, and », keeps the connector and moves the label behind its clause, the
  landed R122 pattern («; hence (Theorem ACYC-LIN) … ; and (Corollary ACYC-XI, …)» became «… (Theorem ACYC-LIN); and … (Corollary ACYC-XI,
  …)» in R122's landed UPDATE); direct2 rebuilds R125's, R126's and R127's landed UPDATEs byte-equal (same as direct). (ii) Drops: L-4's
  TARGET tail is «so this is not M4 and not M3; G-N5-TIME stays OPEN; not a step-4 pass, not a TARGET.md claim», not R123-R127's «…;
  G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim»; the landed second drop string occurs 0 times, so I dropped L-4's
  own form of the same clause, «; not a step-4 pass, not a TARGET.md claim», with «; G-N5-TIME stays OPEN»; «not M3» stays (in «not M4 and
  not M3»). Result: sha1 90d1e0ca964af3edc672aea76fa69fef1d799be9 (no newline, unfilled), 12,601 bytes, one each of <DATE>, <HH:MM>,
  <checker>, 0 «|», 230 «(» = 230 «)», «referee-originated» 5, ends «… L-SI successors 48-50). G-N5-TIME stays open.»; START is the span
  «for every genome G (premises: … π(X) the elements of X at least as relevant as e_o: » (2,945 characters: the premise parenthesis and the
  definitions precede the first label in L-4, so they stay before the claims); twelve labels «(Lemma GATE-RACE)» … «(Corollary A*-EQUIV,
  PROVED-CONDITIONAL on RESULTS R127 (P-N5-SPLIT)'s SPLIT-COUNT and C-EQUIV)». CHECKER: confirm both deviations or rule otherwise. C142 §3
  (second fill): «I confirm both deviations.» (l. 72) The second fill's UPDATE is built by the same direct2 with the same constants from L-5
  (GAPS preamble; on 7ebcf735 it gives C142 §4's «UPDATE-5» f7edaed8…).
- G-4, PREMISE SCOPE (note; C141 G-4 ruled R127's same case no action). L-4's Γ3 premises: eleven facts «RESULTS R125 (P-N5-CHAIN): F1, F3,
  F4′, F6, STRICT, CN2-3, LOC-GATE3, NO-TIE3, LOC-K2-3, B-ONLY3, E-MON3» (each a whole token in landed R125's title, l. 15595: prem128a.py
  (2), 0 missing), and «F2, CYC, (E-DOM), (Core) from P-N5-CHAIN's frozen text (l-new 93531b03, sha1 6e613ba7, §2 and §4)», which are
  P-N5-CHAIN.md l. 96, 97 (§2), 165, 166 (§4) at 93531b03 (an ancestor of f9520557; byte-equal there), a lane packet, the object of landed
  R125, not RESULTS text (R125's title names none of F2, CYC, (E-DOM), (Core)). IDEAL-CYC premises: all landed (R104, R117, R118 (a), (b),
  (c), (e), (k), R121, R123, with 8 premise quotes, each verbatim in the entry it names: prem128a.py (1), 0 not found; negative controls
  found nothing). A*-EQUIV (ii), (iii): RESULTS R127 (G-LT1). No pending-packet premise is left: «pending» 0, «PENDING» 0, «not landed» 0 in
  L-4; the packet names in L-4 are P-N5-CHAIN (as RESULTS R125 and its frozen text), P-N5-SPLIT (as RESULTS R127, and «P-N5-SPLIT §3 (a),
  Lemma REWIN (a)» as the argument PAIR-EXPEL writes out, «so no P-N5-SPLIT premise is used»), P-N5-QN (the landing-order clause) and
  P-N5-GATE itself. RESULTS R-ids L-4 cites: R104, R117, R118, R121, R123, R125, R127 (+ R126 in the landing-order clause); all landed, none
  above R127. C142 §3 (second fill): «C141 G-4's case, no action.» (l. 81): no action (L-5's premises are L-4's, prem128b.py).
- G-LT1, THE LANDING-ORDER CONDITION (MET at f9520557). L-4: «for A*-EQUIV also SPLIT-COUNT and C-EQUIV of RESULTS R127 (P-N5-SPLIT; L-NEW,
  frozen claude/l-new 399cda07, sha1 5bc1b1f3; landing order R126 = P-N5-QN, R127 = P-N5-SPLIT, then this entry)». REFEREE §K l. 407-408
  «the CHECKER confirms at this entry's landing that R127 is P-N5-SPLIT with SPLIT-COUNT and C-EQUIV, else L-4 is regenerated.». REFEREE-2
  Add. 3 l. 557 «CHECKER must confirm R127 = P-N5-SPLIT at this entry's landing (entry 4 F4-1 says so).». At f9520557: «### R126» (l. 15726)
  ends «(P-N5-QN, docs/new/P-N5-QN.md, frozen at l-new e252182d, sha1 97254bd2, …», «### R127» (l. 15903) carries «(Corollary SPLIT-COUNT)
  c_y(v, I) ≤ Σ_((u,b) ∈ SPL_y(v,I)) Dhi_y(b, J_b) ≤ 3M · max_((u,b)) Dhi_y(b, J_b)» and «(Corollary C-EQUIV) T3 ≤ (1 + n3·((2M + 3)(1 +
  M·C) − 1))·(L3 + 1) and C ≤ max(1, T3), so T3 is polynomial iff C is» and ends «(P-N5-SPLIT, docs/new/P-N5-SPLIT.md, frozen at l-new
  399cda07, sha1 5bc1b1f3, with fixes entries 1-4, docs/new/P-N5-SPLIT-fixes.md; …), CHECKER PASS (docs/checker/C141.md, checker 850e9765)»,
  and R127 is the last «### R» heading (prem128a.py (4); negative controls: the made-up label "(Corollary SPLIT-COUNT2)" 0, "(P-N5-GATE" 0
  in R127's title). L-4's frozen-id parenthesis «L-NEW, frozen claude/l-new 399cda07, sha1 5bc1b1f3» equals landed R127's source note. So
  L-4 needs no regeneration; «PROVED-CONDITIONAL on RESULTS R127 (P-N5-SPLIT)'s SPLIT-COUNT and C-EQUIV» refers to a landed entry.
  SPLIT-COUNT in R127 is itself CONDITIONAL on R125 (landed). C142 §3 (second fill): «MET: R127 = P-N5-SPLIT landed at f9520557, CI #7513
  success (C141).» (l. 86)
- G-7, L41 (note; C141 G-7 ruled R127's premise-parenthesis credit no action). L-4 names five referee-originated proof steps: «(Core) in its
  W-1-repaired reading, applied only to non-core vertices (…; referee-originated: REFEREE-2 R2-P-N5-GATE G-1)» in the premise parenthesis;
  the 3M split-pair count in EXPEL-COUNT («referee-originated: REFEREE-2 R2-P-N5-GATE G-6») and A*-EQUIV (i)'s proof («referee-originated:
  REFEREE-2 R2-P-N5-GATE G-7») inside the claims; and twice, after « — » in the scope tail, the Γ3 K10 / PROVISO argument by B-ONLY3
  («referee-originated: REFEREE R-P-N5-GATE GT-1 and REFEREE-2 R2-P-N5-GATE G-5»). Each is signed by both referees (REFEREE-2 Add. 1 table
  GT-1 = G-5, GT-5 = G-6, GT-4 = G-7, GT-7 = G-1, l. 429-439; REFEREE §I «EXPEL-COUNT's 3M (REFEREE-2 R-8b; my GT-5)» (l. 347) and «My R-3
  (A*-EQUIV) merged with REFEREE-2 R-3 / R-5d / R-8a» (l. 342), each marked CORRECT there). Only the GT-1 / G-5 credits sit in the scope
  tail L41 names; the other three sit where the step is used (C141 G-7's placement). Not credited as referee-originated: PAIR-EXPEL needing
  no P-N5-SPLIT premise (REFEREE GT-2 = REFEREE-2 G-4) — a finding about the premise list, the argument being the packet's own; L-4 states
  it without credit. CHECKER's call. C142 §3 (second fill): «credited in the line, so no action (C141 G-7).» (l. 82-83): no action (L-5 has
  the same five credits, «referee-originated» 5).
- G-9, DATA, CLAUSE BY CLAUSE (data128a.py on the archive of 676b6a1c: 48 checks OK, «DATA EQUAL»): S11 = box 91's 11 instances, rows
  identical on the two engines; grfail, gr2fail, grwhy, trfail, par1-3, lexfail, dhifail, pefail, ecfail, pelam 0; pecouples 28, 496, 10,
  121, 103, 74; decfail, glnfail, lowflip 0, max lowch 599; np93's 18 instances, npside, npsub, npboth, npkind, relfail, unlfail, dfail 0,
  k1both = k1c2; MWR4/8/16_2 9 / 17 / 33 flips at lamch 0 (= 2·ch_D + 1); PROVISO dpass 0 on 19 per engine, 307,737 pairs per engine,
  control fires on 14 of 19; copy95 copy 0 only on NSQ2_4, NSQ3_4; lev94 flQ 0 at levels ≥ 2 on NDV*, NDB*; controls gr2fail 8 (CTRL=gr,
  MW8_2), glnfail 26, relfail 4, pefail = couples; C 17 / 65 / 3 / 3; box 90 maxm 8 / 32, maxP 54 / 2583; WC T3 4; K7 C 2; nine instance
  sha1 prefixes. COUNTERS NAMED: every must-0 clause names counter and unit; sets named for S11, the 18, the 19, the 29, box 94's 20 / 22.
  Notes (no defect found by count): «CTRL=gr 8 on MW8_2» names no counter (it is gr2fail, data128a.py); «up to 599 changes below e_o» names
  no counter (gate92's lowch); PARALLEL's clause «(unit: change of H with an expelled letter, at route tuples; x's position after u′ not
  counted)» names no set (S11 by the next clause); «A*-EQUIV: cfail (c_y > a_y) 0 (unit (v, I, z); S11)» (REFEREE D-6 optional: «(v, I,
  y)»); K6's CNT not re-counted by either referee or by me. Independent replays (not in L-4): REFEREE §3 (19 instances, both engines, every
  must-0 counter 0) and REFEREE-2 2.9 (41 pinned + 900 random + 440 mutants, both engines) and Add. 4 (MW32_2, FW16_2 on IDEAL-CYC). C142 §3
  (second fill): «every must-0 counter clause, cited, is no action. The growth clause and the GL-3 rows are E-2 and E-1.» (l. 84): no action
  on the must-0 clauses; E-1 and E-2 FIXED in L-5 (data128b.py on 7b0a58ae, 48 checks OK).
- G-S, STALE STATUS WORDS (CLEAN by grep: in L-4 «pending» 0, «PENDING» 0, «not landed» 0, «unlanded» 0, «when landed» 0, «landing» 1 (in
  «landing order R126 = P-N5-QN, R127 = P-N5-SPLIT, then this entry», TRUE at landing, G-LT1), «will » 0, «not yet» 0, «CANDIDATE» 0,
  «stays» 1 («G-N5-TIME stays OPEN»)). The packet's own «landing as R125, PENDING» (l. 29) and «referees PENDING» (l. 37) are not in L-4.
  C142 §3 (second fill): «**G-S** clean.» (l. 86): no action (in L-5 «pending» 0, «PENDING» 0, «not landed» 0).
- G-1, SOURCE NOTE (note; C134 N-S). L-4 ends «(P-N5-GATE, docs/si/P-N5-GATE.md with its fixes entries 1-4, docs/si/P-N5-GATE-fixes.md; L-SI
  successors 48-50)»: no freeze commit and no sha1 (R125-R127's notes carry «frozen at l-new …, sha1 …»); the packet is frozen at l-si
  4066f579, sha1 f3a584e6. L-SI successors: 47 (box 90), 48 (box 91), 49 (packet), 50 (fixes 1-4) by the l-si log 547985a1..676b6a1c; the
  note says 48-50. CHECKER's call (a line change both referees re-sign if wanted). C142 §3 (second fill): «(source note «L-SI successors
  48-50»): no action.» (l. 85): no action; L-5's note reads «with its fixes entries 1-5» (the tenth pair) and keeps «L-SI successors 48-50»
  (fixes entry 5 F5-4).
- G-L, LABELS (note). L-4 does not print «PROVED» for the unconditional statements (the word occurs once, in A*-EQUIV's
  «PROVED-CONDITIONAL»); the packet's label is «PROVED (L-SI, unrefereed)» (l. 5) and both referees SIGN every statement. The R123 / R125
  lines carry «each PROVED»; R126's L-2 does not either. Not a defect; the entry's Claims signed bullet states the labels. C142 §3 (second
  fill): «(«PROVED» once, in A*-EQUIV's label «PROVED-CONDITIONAL»): no action.» (l. 85): no action.
- G-P, PLACEMENT (Lead). R128 goes after R127 (f9520557 l. 15903-16125, blank l. 16126), directly before the line-start «**Erratum E-1**
  (not a result» (l. 16127), its UPDATE after R127's on GAPS l. 11 (the last there). Simulated (sim128a.py): Addendum. C142 §2 (second
  fill): «The mathematics, tools, the box checks, the UPDATE procedure (G-U) and the placement PASS.» (l. 18) Second-fill simulation
  (sim128b.py): Addendum (second fill).
- G-0, THE CHECKER NUMBER. docs/checker/ ends at C141.md (at f9520557 and on claude/checker 850e9765, which trunk contains); «C142» 0 times
  in trunk docs/ and notes/ and on claude/checker (git grep). This draft uses C142 (title, UPDATE head), as the brief says. Second fill:
  C142 is written (claude/checker 269effb3, FAIL E-1..E-4) and rules the second fill in its Add. 1 (C142 §6), so the title and the UPDATE
  keep C142.
- G-T, TARGET (CLEAN). L-4's tail: «TARGET.md §2 (M4) asks for a deterministic algorithm polynomial on every parity game and §4 says a bound
  on a restricted class, or one resting on an unproved conjecture or an empirical observation, is not M4: these lemmas bound nothing by a
  polynomial, so this is not M4 and not M3; G-N5-TIME stays OPEN; not a step-4 pass, not a TARGET.md claim» (REFEREE §6 «## 6. TARGET.md
  diff: CLEAN» (l. 283); REFEREE-2 Add. 2 «TARGET.md: the tail is unchanged from L-2 (correct paraphrase of §2 / §4, 3.2 above).» (l. 524);
  L-3 → L-4 changes no word of the tail, by REFEREE-2 Add. 3's six regions). Second fill: C142 §3 has no G-T item; L-5's tail is L-4's (the
  ten pairs touch no word of it; «TARGET.md: no diff region touches the tail or a claim.» (l. 668)).
- (L-4 SHAPE, by script) one line: 12,562 bytes, 230 «(» / 230 «)», 0 «|», one « — », «(2026-11-09)» once, «DATA» 5, «DEAD» 2,
  «referee-originated» 5, «CONDITIONAL» 1, «R127» 3, «R126» 1. (L-5 SHAPE, second fill, by script) one line: 12,923 bytes, 238 «(» / 238
  «)», 0 «|», 1 « — », «(2026-11-09)» 1, «DATA» 5, «DEAD» 2, «referee-originated» 5, «CONDITIONAL» 1, «R127» 3, «R126» 1.
- C142 (claude/checker 269effb3, FAIL), second fill: E-1, E-2 and E-3 FIXED in L-5 = 459fd88d (C142 §4's nine pairs and the Lead's tenth
  pair; fixes entry 5; REFEREE §L and REFEREE-2 Add. 5 MATCH); E-4 FIXED in the entry text (Honest limits (vii), C142's string verbatim).
  For CHECKER: the merge list (G-MERGE: claude/l-si at 7b0a58ae, 19 commits after 676b6a1c, plus 16e8dcb0, 0df0fdd8, 269effb3) and the
  changes beyond the brief's list, each tagged X1-X4 in Addendum (second fill).

### R128 [refereed-only] Gate races, expulsions and who pays a gate flip, in ONE Howard strategy-improvement run with Vöge-Jurdziński values, on IDEAL-CYC(G) and on N5′-xi's mover phase on Γ3(G) from S3, for every genome G (premises: RESULTS R104's definitions of the genome and of Γ(G) only («e of even priority above every β with one edge to the W-target or to the top even self-loop c_W»); RESULTS R117's definition of Γ3(G) only; RESULTS R118 (a) IDEAL-CYC(G) («The game is Γ(G) with every Even vertex that is not a mover frozen at its start successor. Odd is unrestricted (gates and K2).») with its Howard step and tie rule («every mover x goes to a successor of ⊴-largest Ω_t value, and keeps σ_t(x) if σ_t(x) is such a successor»), (b) F1, F2, F3, F4′'s stated clause, F6, (c) STRICT, (e) in its per-vertex form, and (k) the form of N5′-xi's run on Γ3 from S3 up to its first fallback («T3 is the first state at which no mover has a strictly better successor in Γ3;») with N5′-xi's rule [N5XI] («an N5′-xi run (box 190's S4a tie rule by Ξσ)»; SPEC S4a's A(v) = {σ(v)} ∪ {w : (v, w) ∈ Iσ}, so a ⊴-best current option is kept); VJ00 §4.2 / Friedmann arXiv 1106.0778 §3 for the value (Λ, Π, k) and its order ⊴; [OPT] as in RESULTS R123 (σ̄_t optimal at every vertex at once against σ_t); RESULTS R121 Lemma E-MON («(Lemma E-MON) if Λ_t(v) = Λ_(t+1)(v) then E_t(v) ≤ E_(t+1)(v)»); RESULTS R123 Lemmas CN2, LOC-GATE, LOC-K2, B-ONLY («at every state t and every vertex v other than c_W and the e-vertices whose successor is c_W, Λ_t(v) is less relevant than every e-vertex») and Corollary NO-TIE («at every state and gate g, Ω_t(e_g) ≠ Ω_t(β_g)»), and (E-DOM) and (Core) read off RESULTS R104's priorities and closed core with LOC-K2 (non-core vertices only: the core is entered only at K0 and then follows one fixed suffix, so K0, K3 lie on the play iff Λ is a core vertex), for IDEAL-CYC; on Γ3 instead RESULTS R125 (P-N5-CHAIN): F1, F3, F4′, F6, STRICT, CN2-3, LOC-GATE3, NO-TIE3, LOC-K2-3, B-ONLY3, E-MON3, and F2, CYC, (E-DOM), (Core) from P-N5-CHAIN's frozen text (l-new 93531b03, sha1 6e613ba7, §2 and §4), (Core) in its W-1-repaired reading, applied only to non-core vertices (the faces of a gate and the successors of a mover or a gate; P-N5-CHAIN fixes entry 3, R-W; referee-originated: REFEREE-2 R2-P-N5-GATE G-1); for A*-EQUIV also SPLIT-COUNT and C-EQUIV of RESULTS R127 (P-N5-SPLIT; L-NEW, frozen claude/l-new 399cda07, sha1 5bc1b1f3; landing order R126 = P-N5-QN, R127 = P-N5-SPLIT, then this entry); no L-RED lane lemma is a premise), with Ω_t, P_t, Λ_t, E_t(v) (the e-vertices of P_t(v) more relevant than Λ_t(v)) the value, play, cycle node and e-set at state t, a gate o with e-vertex e_o, e-face p_e (= e_o on Γ, its pad on Γ3), β-face p_b and D := e_o's successor, a FLIP of o a change of σ̄(o) (an UNLOCK p_b → p_e or a RELOCK p_e → p_b), ch_f the number of steps at which Ω(f) changes, lamch(o) the number of steps at which Λ changes at p_e or p_b, nl_f := ch_f − (Λ-changes of f), LAM_t: Λ_t(p_e) = Λ_t(p_b), PRIV_t: e_o ∉ E_t(p_b), UP_t: e_o more relevant than Λ_t(p_e), π(X) the elements of X at least as relevant as e_o: (Lemma GATE-RACE) if o flips at t from face p to face q then Ω_t(p) ≠ Ω_(t−1)(p), and flips(o) ≤ min(ch_p + ch_q, 2·min(ch_p, ch_q) + 1); (Corollary TRIGGER) that change of p is a change of Λ(p) (at most 2M + 2 over the run), or inside one Λ-interval of p a change of E(p) whose most relevant differing element enters and lies on P_t(p), or a change of Π(p) below every e-letter or of k; (Lemma GATE-LOW-NULL) (a) at a LAM ∧ PRIV step with e_o ∈ E_t(p_e), Ω_t(p_e) ▷ Ω_t(p_b) iff π(E_t(p_e)) is lex-larger than π(E_t(p_b)) (and they differ), so (b) a flip at t with LAM ∧ PRIV ∧ UP at t − 1 and t changes π(E(p_e)) or π(E(p_b)) at t, and (b′) if Λ(p_e) = Λ(p_b) is the same at t − 1 and t, π(E(p_e)) rises at a relock and π(E(p_b)) rises at an unlock; (Lemma NP-SHAPE) at a step with e_o ∈ E_t(p_b), σ̄_t(o) = p_e, P_t(p_b) = A_t · o · P_t(p_e), Λ_t(p_b) = Λ_t(p_e) and E_t(p_e) ⊆ E_t(p_b), and a flip has such a step on at most one side, a relock if before and an unlock if after; (Corollary E-FACE-PAYS) (a) relocks(o) ≤ ch_(p_e), unlocks(o) ≤ 1 + relocks(o) and unlocks(o) ≤ ch_(p_b) with no PRIV, LAM or UP hypothesis, (b) at every t with e_o ∉ P_(t−1)(D) ∪ P_t(D) the value of p_e changes iff that of D does, so (c) if D's play avoids e_o at every state of the run then unlocks(o) ≤ 1 + ch_D ≤ 2M + 3 + (2M + 3)·M·C + gam(D) (C the largest number of changes of one vertex's e-set with one top letter inside one Λ-interval, gam(D) the changes of Ω(D) with Λ and E unchanged), and (d) flips(o) ≤ 2·min(ch_(p_e), ch_(p_b)) + 1 ≤ 2·lamch(o) + 2·min_f nl_f + 1; (Lemma WAIT-QUIET) a gate whose D's play avoids e_o at every state of the run and whose D changes value at most K times unlocks at most K + 1 and flips at most 2K + 1 times, whatever its trigger; (Lemma SAME-SUFFIX) on a window W inside one Λ-interval of a vertex o on which every successor f of o has P_t(f) = P_f · P_t(y) for fixed paths P_f to one vertex y whose play avoids every P_f, the ⊴-order of the successors' values is constant, so σ̄(o) is constant on W if o is Odd and σ(o) is constant from W's second step if o is an Even mover (by the tie rule above); (Lemma STEP-BOUND) Ω(x) changes at t only if some vertex of P_(t−1)(x) changes successor at t, so ch_x ≤ T; (Lemma PARALLEL) inside one Λ-interval of b, at a change of H_s := E_s(b) ∩ U_y (U_y the e-vertices more relevant than y), the top x of the change lies on the new play only and every expelled letter on the old play only, below x and strictly after b's split; (Lemma PAIR-EXPEL; its Step 1 is the argument of P-N5-SPLIT §3 (a), Lemma REWIN (a), which the packet writes out in full from F1, STRICT, F3, F6, F4′, CN2-3, so no P-N5-SPLIT premise is used) two expulsions of one letter z at b through the same split pair (u′, b′) leave E(b′) ∩ U_z strictly lex-larger at the later one, and (Corollary EXPEL-COUNT) the number a_z(b, J) of runs of z in E(b) on a Λ-interval J is at most 1 + 3M·max Dhi_z (at most 3M split pairs: the split is a mover or a gate, with M mover edges and 2M faces; referee-originated: REFEREE-2 R2-P-N5-GATE G-6), Dhi_z(b′, J′) the number of distinct E_s(b′) ∩ U_z on J′; (Corollary A*-EQUIV, PROVED-CONDITIONAL on RESULTS R127 (P-N5-SPLIT)'s SPLIT-COUNT and C-EQUIV) C ≤ A*_all ≤ 1 + M·C (on both runs, with no P-N5-SPLIT premise: each entry of a top starts a run, and every run but one starts at a change; referee-originated: REFEREE-2 R2-P-N5-GATE G-7) and, on Γ3 only, C ≤ 3M·(1 + M·A*_route), so T3 is polynomial iff C is iff A*_all is iff A*_route is (A*_all the largest a_z(b, J) over all b, J, z; A*_route the same over the new successors of split pairs) (2026-11-09) — these are reductions of one run's counts to per-gate or per-continuation counts of the same run, not bounds: none bounds T3, T_CYC, C or A*_all by a polynomial; on IDEAL-CYC a LAM ∧ PRIV step with e_o not above Λ (row K10 of WAIT-CLOSED) does not occur, by RESULTS R123 B-ONLY, so GATE-LOW-NULL covers every flip between two LAM ∧ PRIV steps there, and on Γ3 it does not occur either, by RESULTS R125's B-ONLY3, the same argument with the pads (pβ_o is never an exception; pe_o is one only when D = c_W, and then Λ(pe_o) = c_W ≠ Λ(pβ_o); referee-originated: REFEREE R-P-N5-GATE GT-1 and REFEREE-2 R2-P-N5-GATE G-5); on IDEAL-CYC the proviso «D's play avoids e_o» of E-FACE-PAYS (c) and WAIT-QUIET always holds (Lemma PROVISO, credit L-RED 63: if e_o lay on P_t(D), the play would close at D, the vertex after e_o, so its cycle would carry e_o and Λ_t(D) would be at least as relevant as e_o, against RESULTS R123 B-ONLY at the mover D; D = c_W is its own loop), so on IDEAL-CYC E-FACE-PAYS (b) holds at every step and (c) and WAIT-QUIET hold with no proviso, B-ONLY being the one premise shared with the K10 clause above, and on Γ3 it holds at every state 0, …, T3 by RESULTS R125's B-ONLY3 at the mover D, by the same argument, so there too (b), (c) and WAIT-QUIET hold with no proviso (referee-originated: REFEREE R-P-N5-GATE GT-1 and REFEREE-2 R2-P-N5-GATE G-5); DEAD, on frozen instances (DATA, two engines unless said): a waiting High WC (T3 = 4 at n = 4, 8, 16; WC4_2, WC16_2), the lagging merged copy K6 LAG TOWER (CNT ≤ 4, 3, 2, 2 at h = 2, 3, 4, 5), the High continuation on the race K7 (C = 2; Ku_4, Ku_8, Ku_16, Kprev_8), nesting multipliers at H = 2, 3 (C, flips and T3 of one MW(n) or the sum; 22 instances) and the non-common-suffix nesting Db / Dbr (one MW(n)'s counters; NDb2_4 … NDbr3_8, L-RED 63), all in experiments/si/box91, box93, box94 and box95/fix1 inst with sha1 files; DATA, not DEAD (asymptotic statements, finitely many instances; L43): re-arm multiplicity m 8 / 32 with C 17 / 65 on MW8_2 / MW32_2 (refutes a constant multiplicity only below 32), the RA path count P 54 / 2583 (= F_(d+2) − 1 at d = 8, 16) with C 3 on FW8_2 / FW16_2 (m and P: L-SI 47 box 90, claude/l-si 2d0344d3 and 4ded1e8d, box90/out/mw90.out maxm and fw90.out maxP, both engines), and per-gate flips 9 / 17 / 33 at lamch 0 on MWR4_2, MWR8_2, MWR16_2 (L-RED 63, claude/l-red 406ef2fd; refutes c·(lamch + 1) only for c ≤ 32); DATA, clause by clause (two engines: own = L-RED R221 own.py on IDEAL-CYC, g3 = L-NEW's Γ3 N5′-xi from S3; rows identical; set S11: box 91's 11 instances; tools experiments/si/box91-box94, run by check91-94.sh): GATE-RACE and TRIGGER: grfail, gr2fail, grwhy, trfail 0 (unit: Odd vertex with two successors for grfail and gr2fail, flip for grwhy and trfail; whole run; S11; own to the cap 3000, g3 to the first fallback or the cap 20000); GATE-LOW-NULL: decfail 0 (unit (gate, state): the decider is at least as relevant as e_o; (a)'s order equivalence is not counted by the lane), glnfail and lowflip 0 (unit: flip with LAM ∧ PRIV at t − 1 and t; S11), (b′) no separate lane DATA, with up to 599 changes below e_o that never flip a gate; NP-SHAPE and E-FACE-PAYS: npside, npsub (unit (gate, state)), npboth, npkind (unit flip), relfail (relocks > ch_(p_e)), unlfail (unlocks > 1 + ch_(p_e); the bounds unlocks ≤ 1 + relocks and unlocks ≤ ch_(p_b) are not counted by the lane), dfail (a proxy for E-FACE-PAYS (b)) 0, and k1both = k1c2 (unit gate for relfail, unlfail, k1both, k1c2; 18 instances: S11, k1fail_202, Ku_8, Ku_16, Kprev_8, MWR4_2, MWR8_2, MWR16_2), and the exact form of E-FACE-PAYS (b), L-RED 63's dexact (D's play followed vertex by vertex), 0, with dpass (steps at which D's play passes e_o) 0 (unit (gate, step); 29 instances; own engine only, cap 3000; claude/l-red fa4e50fe R229-box93 §2); PROVISO: dpass 0 (unit (gate, state); 19 instances, box 91's 11 and box 93's 8, 307,737 pairs per engine; both engines, rows identical; experiments/si/box96 d96.py), and the control with Odd made non-optimal (own engine; e-face at o, β-face at every other gate) fires on 14 of the 19; SAME-SUFFIX: copy rows S(R_j) = S(R_(j−1)) as sets on every level of box 94's 20 simultaneous-clock instances (all but NSQ2_4, NSQ3_4, whose levels run one after another and whose rows differ) (REFEREE replay, own engine; L-SI's set re-measure copy95.py agrees on both engines; the lane's lev94 compares sizes), and 0 flips at the copied gates on NDV and NDB (unit level); PARALLEL: par1-3 0 (unit: change of H with an expelled letter, at route tuples; x's position after u′ not counted); PAIR-EXPEL and EXPEL-COUNT: pefail, ecfail, pelam 0, with lexfail and dhifail 0 (E-MON3 on H) (unit change of H, tuple (b, J, y) or same-pair couple; S11; 28, 496, 10, 121, 103, 74 couples); A*-EQUIV: cfail (c_y > a_y) 0 (unit (v, I, z); S11); controls fire (CTRL=gr 8 on MW8_2, CTRL=low glnfail 26 and CTRL=swap relfail 4 on C6G8_n54, CTRL=uz pefail on every couple); growth, as numbers on the named instances only (both engines; box91/out/own91.out and g391.out C and maxflip, box93/out/mwr93_own.out and mwr93_g3.out mx_flips and mx_ch_D): C 17 / 65 and the largest per-gate flip count 34 / 130 on MW8_2 / MW32_2, and per-gate flips 9 / 17 / 33 = 2·ch_D + 1 (ch_D 4 / 8 / 16) with lamch 0 on MWR4_2, MWR8_2, MWR16_2, where E-FACE-PAYS (d) holds with equality; no separate DATA for STEP-BOUND and for A*-EQUIV's equivalence; TARGET.md §2 (M4) asks for a deterministic algorithm polynomial on every parity game and §4 says a bound on a restricted class, or one resting on an unproved conjecture or an empirical observation, is not M4: these lemmas bound nothing by a polynomial, so this is not M4 and not M3; G-N5-TIME stays OPEN; not a step-4 pass, not a TARGET.md claim (P-N5-GATE, docs/si/P-N5-GATE.md with its fixes entries 1-5, docs/si/P-N5-GATE-fixes.md; L-SI successors 48-50), CHECKER PASS (docs/checker/C142.md, checker PENDING)
- Object (L-SI successors 48-50, D18 / D14 / D1, boxes 90-96; frozen, unchanged during review): packet P-N5-GATE (L-SI; not the L-NEW packet
  P-N5-GATE of RESULTS R101), docs/si/P-N5-GATE.md, sha1 f3a584e68b5c998276ea717f42920bdeeca581ab, 230 lines, 25,604 bytes (l-si 4066f579,
  2026-11-09T06:36:22Z, the file's only commit; identical at ecc5fe25, 9c0349b1, ef14451f, 676b6a1c and at the l-si head; not in trunk
  f9520557 before the merge, G-MERGE). Both referees measured it (REFEREE «docs/si/P-N5-GATE.md sha1
  f3a584e68b5c998276ea717f42920bdeeca581ab, 25,604 B, 230 lines» (l. 8-9); REFEREE-2 «Packet: claude/l-si 4066f579, docs/si/P-N5-GATE.md,
  sha1 f3a584e68b5c998276ea717f42920bdeeca581ab, 25,604 B.» (l. 12)). Labels (l. 5-6): PROVED (L-SI, unrefereed), PROVED-CONDITIONAL on a
  named packet, DATA, DEAD, READING; «Not a TARGET.md claim; not M3 or M4; not a gauntlet step; G-N5-TIME stays OPEN.». Scope (l. 8-13):
  «None of them bounds T3; they are reductions of the open core (C, A*_all, …: L-NEW's N5-CORE-forms) to per-gate or per-continuation
  quantities.». To sign (l. 15-26): §3.1 Lemma GATE-RACE (a), (b), Corollary TRIGGER; §3.2 Lemma GATE-LOW-NULL (a), (b); §3.3 Lemma NP-SHAPE
  (a), (b); §3.4 Corollary E-FACE-PAYS (a)-(d), Lemma WAIT-QUIET; §3.5 Lemma SAME-SUFFIX, Lemma STEP-BOUND; §3.6 Lemma PARALLEL; §3.7 Lemma
  PAIR-EXPEL, Corollary EXPEL-COUNT; §3.8 Corollary A*-EQUIV; §4-§8 overlaps, DEAD list, DATA, controls, TARGET diff, attack record not to
  sign. The packet carries every proof (l. 4-5): «This packet carries every proof in full and is checked against this text only.».
- Fixes: docs/si/P-N5-GATE-fixes.md, append-only, five entries (7b0a58ae: 332 lines, 34,305 bytes, sha1
  7c389a35a420ba73e4d9e61ae8295a692186771c; its first 28,767 bytes are the file at 676b6a1c (284 lines, sha1 8009e018…), whose first 24,889
  bytes are the file at ef14451f (246 lines, sha1 e79455ea…), whose first 12,272 bytes are the file at 9c0349b1 (116 lines, sha1 1fec4f8c…),
  whose first 8,557 bytes are the file at ecc5fe25 (84 lines, sha1 00cf406d…); by prefix test). Entry 1 (L-SI successor 50, ecc5fe25,
  2026-11-09T08:40:46Z; l. 3-84; L-RED 63's packet-level read R229-box94 Addendum A, G1-G6): «No PROVED statement changes; G1 narrows an
  open case to Γ3, G2 adds the tie rule that SAME-SUFFIX's Even half uses.» (l. 6); G1 named the K10 case and closed it on IDEAL-CYC by
  RESULTS R123 B-ONLY; G2 added [HOW]'s tie rule for SAME-SUFFIX's Even half; G3-G6 premise lists, names, a stale record, a DATA line; Line
  L-1. Entry 2 (9c0349b1, 2026-11-09T10:05:10Z; l. 86-116; Lead ruling 09:24Z (a)): the PROVISO «D's play avoids e_o» on IDEAL-CYC, cited
  from L-RED 63 and «cited, and derived independently» (l. 91); Line L-2. Entry 3 (ef14451f, 2026-11-12T01:50:52Z; l. 118-246; answering
  REFEREE 31 a401ce0e and REFEREE-2 37 c035b35f, governing list REFEREE-2 Add. 1 8983b3d8): «Verdicts (both): every statement SIGN; Γ3 rows
  CONDITIONAL on R125, which has LANDED» (l. 122); F3-1 «B-ONLY on Γ3 IS a P-N5-CHAIN fact (now RESULTS R125); entries 1-2 corrected» (l.
  127) and RETRACTS entry 1's G1 sentence and entry 2's Γ3 hypothesis; F3-2 (Core) in its W-1-repaired reading; F3-3 premise glosses; F3-4
  PAIR-EXPEL / EXPEL-COUNT need no P-N5-SPLIT premise; F3-5 A*-EQUIV ((i) on both runs, (ii), (iii) on Γ3 only); F3-6 copy rows as sets;
  F3-7 Line L-3, «Absent from L-3 (asserted by mkL3.py): «§2 (a)», «P-N5-CHAIN's C-EQUIV», «lie on both of two plays», «not a premise here»,
  «not among P-N5-CHAIN», «while its play avoids», «over the run then», «CTRL=a0».» (l. 239-240). Entry 4 (676b6a1c, 2026-11-12T04:09:12Z;
  l. 248-284; Lead 02:57Z-04:09Z): F4-1 LT-1, «so SPLIT-COUNT and C-EQUIV are cited as «RESULTS R127 (P-N5-SPLIT)», and A*-EQUIV (ii), (iii)
  stay labelled CONDITIONAL with R127 as the premise; CHECKER confirms R127 = P-N5-SPLIT at this entry's landing.» (l. 256-259); F4-2 GT-10
  = L43, «three asymptotic rows leave the DEAD list and become DATA» (l. 265) and «The construction rows (WC, K6 LAG TOWER, K7 probe,
  nesting multipliers, Db / Dbr) stay DEAD: each records that a named construction fails to produce growth, with measured numbers; they
  claim no asymptotic bound (REFEREE 31 §J; the Lead, 03:00Z).» (l. 276-277); F4-3 L-4 = L-3 + LT-1 + GL-1..GL-3 + «fixes entries 1-4» (l.
  281-284). Entry 5 (7b0a58ae, 2026-11-12T18:03:39Z; l. 286-332; «Entry 5 (fix round 5; L-SI successor 52; Lead 2026-11-12 17:47Z; CHECKER
  C142)»; byte copy of C142 fix5/chk_C142_269effb3.md, sha1 8b005c61…): F5-1 (E-1) «the RA-MULT and RA-path DATA rows get their numbers and
  their source commits» (l. 293); F5-2 (E-2) «the growth clause as numbers on named instances; A*_all leaves it» (l. 301); F5-3 (E-3) «the
  part markers of GATE-LOW-NULL and E-FACE-PAYS enter the line (seven insertions, no word changed)» (l. 310); F5-4 the Lead's tenth pair,
  «The Lead: L-5's source note must say «with its fixes entries 1-5», not «1-4».» (l. 323), «docs/si/P-N5-GATE.md with its fixes entries
  1-4,» → «docs/si/P-N5-GATE.md with its fixes entries 1-5,»; F5-5 L-5 (l. 328). No entry changes a statement's content: entries 3-4 change
  premise citations, scope sentences, labels of the DEAD rows and DATA wording, each named by a referee; entry 5 inserts the packet's part
  markers into GATE-LOW-NULL and E-FACE-PAYS (no word changed) and gives two DATA clauses numbers and sources, each named by CHECKER C142.
- The RESULTS line is L-5, 459fd88d2d1959647f6aeb065bf8ac58cce684f9 (docs/si/P-N5-GATE-line-L5.txt, l-si 7b0a58ae, 2026-11-12T18:03:39Z, the
  file's only commit; 12,923 bytes, one line, blob c4ef22e8c48a2186923de9b35f7c81d0d4c58d5f). The title is L-5 verbatim, with nothing
  inserted and nothing stripped (its date parenthesis «(2026-11-09)», its scope tail and its source note are the line's own). L-5's
  parentheses balance (238 «(» / 238 «)»); it has no pipe character. It is written by experiments/si/box95/fix5/mkL5.py from L-4 with
  CHECKER C142 §4's nine pairs (R-E1, R-E2 and R-E3's seven insertions), parsed from the byte copy fix5/chk_C142_269effb3.md (sha1
  8b005c61…, equal to claude/checker 269effb3:docs/checker/C142.md), each old string asserted once, which give CHECKER's
  7ebcf7355be9838473f05a7defe913940b6fd723 (asserted), and then the Lead's tenth pair (ruling 17:58Z) «docs/si/P-N5-GATE.md with its fixes
  entries 1-4,» → «docs/si/P-N5-GATE.md with its fixes entries 1-5,» (fixes entry 5 F5-4, F5-5, l. 322-332). L-4 is
  6bfde78ef050b47f43527875256c65a205869e77 (docs/si/P-N5-GATE-line-L4.txt, l-si 676b6a1c, 2026-11-12T04:09:12Z, 12,562 bytes, blob
  47a09c227d61a5a37ae1a2a79c09c0704b534617), written by experiments/si/box95/fix4/mkL4.py from L-3
  (b60495b2c607e8e6c1e145e40478717fa6ed15f4, ef14451f, 12,353 bytes; fix3/mkL3.py from L-2 c0f2007d84afab1e00ef41e24ba8f5f064468cc5,
  9c0349b1, 10,295 bytes; fix2/mkL2.py from L-1 a44647db487dcd5193d11ff83f80006b3533dac4, ecc5fe25, 9,541 bytes; fix1/mkL1.py from the
  frozen packet), with LT-1 (two strings), GL-1..GL-3 parsed from the byte copy of REFEREE §J (fix4/ref_R-P-N5-GATE_fbc4d865.md, sha1
  9aaf92a6…, checked by fix4.sha1) and «fixes entries 1-3» → «1-4»; «mkL4.py asserts each Old once, that «RA-MULT», «K1-FLIP(c)» and «a
  polynomial bound on the RA path count» are absent», no pipe character, and balanced parentheses (fixes l. 283-284, entry 4 F4-3). Rebuilt
  byte-equal: L-5 by the drafter's own parse (r128b/tools/mkL5b.py: the nine pairs from C142.md at 269effb3, each old string once, giving
  7ebcf735; then F5-4's pair, once), by the lane's mkL5.py from a git archive of 7b0a58ae (cmp equal; with --nine 7ebcf735) and by
  check_fix5.sh in the box 95 block (rc 0); L-4 by the drafter with the lane's whole chain mkL1.py … mkL4.py from a git archive of 676b6a1c
  (RESULTS at f9520557; rc 0 each; L-1, L-2, L-3, L-4 cmp-equal to the committed files) and by check_fix4.sh. REFEREE §L rebuilt L-5 from
  its own parse of C142 §4: «So L-5 = L-4 + exactly CHECKER's nine pairs + the tenth pair; nothing else changed.» (l. 427); «`cmp` with the
  lane's L-5: **EQUAL**» (l. 426-427). REFEREE-2 Add. 5 rebuilt it with its own code and had predicted it before the lane's commit: «The
  lane's L-5 equals the prediction byte for byte (cmp).» (l. 600); «So THE TENTH PAIR IS THE ONLY DIFFERENCE FROM 7ebcf735.» (l. 606); «Diff
  L-4 → L-5, word level: 23 regions, each read.» (l. 609); «There is no other change.» (l. 610). On L-4: REFEREE §K rebuilt it with its own
  strings: «parsed from MY §J in this file, not from the lane's byte copy» (l. 402); «`cmp` with the lane's L-4: **EQUAL**» (l. 403).
  REFEREE-2 Add. 3 read the six changed regions: «Diff L-3 → L-4 (word level): exactly six regions, all named by entry 4.» (l. 540); «There
  is no other change.» (l. 548).
- Claims signed (REFEREE successor 31: §1-§2 731db590, §3-§8 and §0 a401ce0e, §I 41228433, §J fbc4d865, §K 49d34123; successor 34: §L
  16e8dcb0; REFEREE-2 successor 37: boxes 1-3 a28bc5e1, §3.5 276545dc, box 4 c035b35f, Add. 1 8983b3d8, Add. 2 6269fec5, Add. 3 93413fc6,
  Add. 4 3282fc6c; successor 38: Add. 5 0df0fdd8). REFEREE's table («## 0. Verdicts», l. 290, R-P-N5-GATE.md) reads «**SIGN**» on GATE-RACE
  (a), (b) / TRIGGER (l. 293), «**SIGN** (premises as R-4..R-7; (Core) for non-core vertices)» on GATE-LOW-NULL (l. 294), K10 empty
  «**SIGN** on IDEAL-CYC (R123 B-ONLY); on Γ3 also TRUE by P-N5-CHAIN B-ONLY3 (GT-1, §2.2)» (l. 295), «**SIGN**» on NP-SHAPE (l. 296),
  «**SIGN** (WAIT-QUIET read «over a run in which D's play avoids e_o», moot below)» on E-FACE-PAYS / WAIT-QUIET (l. 297), PROVISO
  «**SIGN**; on Γ3 also TRUE by P-N5-CHAIN B-ONLY3 (GT-1, §2.4)» (l. 298), «**SIGN**» on SAME-SUFFIX / STEP-BOUND (l. 299) and PARALLEL (l.
  300), «**SIGN**» on PAIR-EXPEL / EXPEL-COUNT with «the proof needs no SPLIT statement, GT-2; 3M re-derived, GT-5» (l. 301), «**SIGN**
  (re-derived, GT-4)» on A*-EQUIV (i) (l. 302), «**SIGN, Γ3 ONLY** (R-3)» on A*-EQUIV (ii), (iii) (l. 303), the DEAD list «reproduced as
  stated (own engine, §3.3) except K6's CNT and FW's P (not re-counted; their C / flips / T rows reproduced)» (l. 304); then «No GAP;
  nothing REFUSED.» (l. 305). REFEREE-2's table («2.11 Verdicts (Opus 5.5, D1)», R2-P-N5-GATE.md l. 393) reads «SIGN» on each of its nine
  statement rows (l. 396-404; A*-EQUIV (i)-(iii) «SIGN, CONDITIONAL on P-N5-SPLIT (SPLIT-COUNT, C-EQUIV) and R125; Γ3 only», «My row
  «A*-EQUIV (i)-(iii) … Γ3 only» is corrected: (i) holds on both runs, (ii) and (iii) on Γ3 only.») and «SIGN (dead) as far as re-run
  (2.10)» on the DEAD list (l. 405); then «No statement is REFUSED. No signed proof keeps an open gap.» (l. 407). Addendum 1 (8983b3d8):
  «Verdicts: equal on every row. Both referees SIGN every statement, none REFUSED, no GAP.» (l. 423); «One refinement I ADOPT. REFEREE signs
  A*-EQUIV (i) on BOTH runs.» (l. 441). Re-signed on L-3: REFEREE §I «Verdict: fixes entry 3 CORRECT. **Line L-3 MATCHES except LT-1** (one
  required string).» (l. 366); REFEREE-2 Add. 2 «Verdict: L-3 (ef14451f, sha1 b60495b2) MATCHES.» (l. 527). Re-signed on L-4: REFEREE §K and
  REFEREE-2 Add. 3; on L-5, the line of record: REFEREE §L and REFEREE-2 Add. 5 (quoted under Signatures), each re-signing GATE-LOW-NULL
  (a), (b), (b′) and E-FACE-PAYS (a)-(d) with the part markers (REFEREE §L «I re-sign them with the markers.» (l. 453-454); REFEREE-2 Add. 5
  «I RE-SIGN GATE-LOW-NULL (a), (b), (b′) and E-FACE-PAYS (a)-(d) in the marked form» (l. 681)). The CONDITIONAL statements, with their
  condition as the line states it: every Γ3 statement on RESULTS R125 (landed); A*-EQUIV (ii), (iii) «PROVED-CONDITIONAL on RESULTS R127
  (P-N5-SPLIT)'s SPLIT-COUNT and C-EQUIV», on Γ3 only, R127 landed (G-LT1). No HYPOTHESIS statement. The joint gap map: EMPTY (REFEREE l.
  305; REFEREE-2 l. 407). The defects found in review are text and citation defects (REFEREE GT-1..GT-10, D-1..D-7; REFEREE-2 G-1..G-7,
  R-1..R-10), each closed by fixes entries 3-4 and checked in bytes by both referees; CHECKER C142's line items E-1..E-3 (the GL-3 DATA
  rows' numbers and sources, the growth clause, the part markers) are closed by fixes entry 5 and checked in bytes by both referees (§L,
  Add. 5); nothing is REFUSED.
- Setting: ONE run of Howard strategy improvement with Vöge-Jurdziński values per game, for every genome G of RESULTS R104: IDEAL-CYC(G) of
  RESULTS R118 (a) on Γ(G), states 0, …, T_CYC; and HOW3(G) on Γ3(G) of RESULTS R117 from S3, states 0, …, T3, which by RESULTS R125's
  REACH3-ALL is the mover part of N5′-xi from S3 until its first fallback. Every statement holds on both runs unless marked Γ3 only; on Γ3
  every statement rests on RESULTS R125 (landed) and the four P-N5-CHAIN frozen-text items (G-4). Statements as signed (packet §3 with fixes
  entries 1-5; entry 3's premise rows and scope sentences govern):
  (a) Lemma GATE-RACE (a), (b), Corollary TRIGGER (§3.1 l. 67-74): «(a) If o flips at t from face p to face q, then Ω_t(p) ≠ Ω_(t−1)(p). (b)
    #flips(o) ≤ min(ch_p + ch_q, 2·min(ch_p, ch_q) + 1).» TRIGGER: the change of the left face is a change of Λ (at most 2M + 2 over the
    run), or inside one Λ-interval a change of E whose top enters, or neither (Π below every e-letter, or k). Both SIGN (REFEREE l. 293;
    REFEREE-2 l. 396).
  (b) Lemma GATE-LOW-NULL (a), (b), (b′) (§3.2 l. 76-92): «(a) At a step t with LAM_t, PRIV_t and e_o ∈ E_t(p_e): Ω_t(p_e) ▷ Ω_t(p_b) ⟺
    π(E_t(p_e)) >lex π(E_t(p_b)), and the two π's differ.»; (b) a flip between two LAM ∧ PRIV ∧ UP steps changes π(E(p_e)) or π(E(p_b));
    (b′) with Λ fixed, π(E(p_e)) rises at a relock and π(E(p_b)) at an unlock. The K10 case (LAM ∧ PRIV with e_o not above Λ) does not occur
    on IDEAL-CYC (RESULTS R123 B-ONLY) nor on Γ3 (RESULTS R125's B-ONLY3, with the pads; referee-originated, REFEREE GT-1 = REFEREE-2 G-5).
    Both SIGN (REFEREE l. 294; REFEREE-2 l. 397, «both runs; (Core) at the faces only (G-1, R-1); IDEAL-CYC (E-DOM) / (Core) from R104
    (R-5)»).
  (c) Lemma NP-SHAPE (a), (b) (§3.3 l. 94-103): «(a) If NP_t then σ̄_t(o) = p_e, P_t(p_b) = A_t · o · P_t(p_e) for a path A_t from p_b to o,
    Λ_t(p_b) = Λ_t(p_e), and E_t(p_e) ⊆ E_t(p_b). (b) If o flips at t, not both NP_(t−1) and NP_t; NP_(t−1) implies a relock, NP_t an
    unlock.» Both SIGN (REFEREE l. 296; REFEREE-2 l. 398).
  (d) Corollary E-FACE-PAYS (a)-(d), Lemma WAIT-QUIET (§3.4 l. 105-121): «(a) relocks(o) ≤ ch_(p_e); unlocks(o) ≤ 1 + relocks(o) ≤ 1 +
    ch_(p_e); likewise unlocks(o) ≤ ch_(p_b). No PRIV, LAM or UP hypothesis.»; (b) off e_o, p_e and D change value at the same steps; (c)
    unlocks(o) ≤ 1 + ch_D ≤ 2M + 3 + (2M + 3)·M·C + gam(D); (d) flips(o) ≤ 2·lamch(o) + 2·min_f nl_f + 1; WAIT-QUIET: D changing at most K
    times gives at most K + 1 unlocks and 2K + 1 flips. The proviso «D's play avoids e_o» holds at every state on both runs (Lemma PROVISO:
    on IDEAL-CYC by RESULTS R123 B-ONLY, fixes entry 2, credit L-RED 63; on Γ3 by RESULTS R125's B-ONLY3, referee-originated, REFEREE GT-1 =
    REFEREE-2 G-5), so (b), (c) and WAIT-QUIET hold with no proviso. Both SIGN (REFEREE l. 297, PROVISO l. 298; REFEREE-2 l. 399, l. 400).
  (e) Lemma SAME-SUFFIX (with entry 1's G2 tie rule), Lemma STEP-BOUND (§3.5 l. 123-134): on a window with a common suffix the ⊴-order of
    o's successors is constant, so σ̄(o) is constant if o is Odd and σ(o) from the second step if o is an Even mover; «STEP-BOUND. For every
    vertex x, S(x) ⊆ {t : some vertex of P_(t−1)(x) changes successor at t}», so ch_x ≤ T. Both SIGN (REFEREE l. 299; REFEREE-2 l. 401).
  (f) Lemma PARALLEL (i)-(iii) (§3.6 l. 136-144): at a change of H_s = E_s(b) ∩ U_y inside one Λ-interval of b, the top x lies on the new
    play only, every expelled letter z on the old play only, z ≺ x, both strictly after b's split. Both SIGN (REFEREE l. 300; REFEREE-2 l.
    402).
  (g) Lemma PAIR-EXPEL, Corollary EXPEL-COUNT (§3.7 l. 146-165): two expulsions of z at b through one split pair (u′, b′), «Then E_s′(b′) ∩
    U_z >lex E_s(b′) ∩ U_z.»; a_z(b, J) ≤ 1 + 3M·max Dhi_z, the 3M by the elementary count (a mover or a gate: M mover edges and 2M faces;
    referee-originated, REFEREE-2 G-6 = REFEREE GT-5). Step 1 is the argument of P-N5-SPLIT §3 (a), written out in the packet from landed
    facts, so no P-N5-SPLIT premise is used (REFEREE GT-2 = REFEREE-2 G-4; fixes entry 3 F3-4); the packet's CONDITIONAL label is dropped in
    L-5 accordingly. Both SIGN (REFEREE l. 301; REFEREE-2 l. 403).
  (h) Corollary A*-EQUIV (§3.8 l. 167-173): (i) C ≤ A*_all ≤ 1 + M·C on both runs, with no P-N5-SPLIT premise (proof referee-originated,
    REFEREE-2 G-7 = REFEREE GT-4); (ii), Γ3 only, «C ≤ 3M·(1 + M·A*_route)»; (iii) T3 polynomial iff C iff A*_all iff A*_route, by RESULTS
    R127's C-EQUIV. (ii), (iii) PROVED-CONDITIONAL on RESULTS R127 (P-N5-SPLIT)'s SPLIT-COUNT and C-EQUIV (landed). Both SIGN ((i) REFEREE
    l. 302; (ii), (iii) REFEREE l. 303; REFEREE-2 l. 404).
  (i) DEAD, constructions only (packet §5 l. 186-195 after GL-1, GL-2; frozen instances in experiments/si/box90, box91, box93, box94,
    box95/fix1 inst): a waiting High WC (T3 = 4 at n = 4, 8, 16), the K6 LAG TOWER (CNT ≤ 4, 3, 2, 2 at h = 2, 3, 4, 5), the K7 probe (C = 2
    on Ku_4, Ku_8, Ku_16, Kprev_8), nesting multipliers at H = 2, 3 (22 instances), the non-common-suffix nesting Db / Dbr (L-RED 63). DATA,
    not DEAD (GL-3, L43): RA-MULT, the RA path count, K1-FLIP(c). REFEREE: reproduced except K6's CNT and FW's P (l. 304); REFEREE-2: «SIGN
    (dead) as far as re-run» (l. 405), K6 not re-run.
- Premise (8 quotes and named facts; checked by script at trunk f9520557, prem128a.py on L-4 and prem128b.py on L-5, the same results):
  IDEAL-CYC: RESULTS R104 (l. 9864), its definitions of the genome and of Γ(G), with «e of even priority above every β with one edge to the
  W-target or to the top even self-loop c_W»; RESULTS R117 (l. 13362), the definition of Γ3(G); RESULTS R118 (l. 13607) (a) IDEAL-CYC(G)
  with its Howard step and tie rule (two quotes), (b) F1, F2, F3, F4′'s stated clause, F6, (c) STRICT, (e) per vertex, (k) the form of
  N5′-xi's run on Γ3 up to its first fallback with [N5XI] (two quotes); VJ00 §4.2 / Friedmann arXiv 1106.0778 §3 for the value (Λ, Π, k) and
  ⊴; [OPT] as in RESULTS R123; RESULTS R121 (l. 14320) Lemma E-MON (quoted); RESULTS R123 (l. 15076) Lemmas CN2, LOC-GATE, LOC-K2, B-ONLY
  (quoted) and Corollary NO-TIE (quoted); (E-DOM) and (Core) read off R104 with LOC-K2, non-core vertices only. Γ3: RESULTS R125 (l. 15595):
  F1, F3, F4′, F6, STRICT, CN2-3, LOC-GATE3, NO-TIE3, LOC-K2-3, B-ONLY3, E-MON3 (each a whole token in R125's title; 11 of 11); F2, CYC,
  (E-DOM), (Core) from P-N5-CHAIN's frozen text (l-new 93531b03, sha1 6e613ba762b6ecf67247ef6d8674b4c960013039; P-N5-CHAIN.md l. 96, 97,
  165, 166), (Core) in its W-1-repaired reading for non-core vertices (P-N5-CHAIN fixes entry 3, R-W; referee-originated, REFEREE-2 G-1 =
  REFEREE GT-7) (G-4). A*-EQUIV (ii), (iii): RESULTS R127 (l. 15903) SPLIT-COUNT and C-EQUIV. Each of the 8 premise quotes occurs verbatim
  in the entry it names (R104 1, R118 4, R121 1, R123 2; prem128a.py (1)); the 9th «…» of L-5, «D's play avoids e_o», is the packet's
  proviso. Not used (L-5): any L-RED lane lemma («no L-RED lane lemma is a premise»); L-RED 63's PROVISO argument is credited and derived
  independently (fixes entry 2). Both referees checked the premises by script (REFEREE «9 quotes; 8 are premise quotes and each occurs
  verbatim» (l. 19); REFEREE-2 Add. 2 «Every name in the R125 list occurs in R125's line L-5 (my earlier script).» (l. 496)).
- L41 and L43. The packet's proofs are L-SI successor 49's (packet l. 2; «This packet carries every proof in full»). Five referee-originated
  steps are named in L-5 with their credit: (Core)'s W-1 reading (REFEREE-2 G-1, premise parenthesis), EXPEL-COUNT's 3M (REFEREE-2 G-6),
  A*-EQUIV (i)'s proof (REFEREE-2 G-7), and the Γ3 K10 / PROVISO argument by B-ONLY3 (REFEREE GT-1 and REFEREE-2 G-5, twice in the scope
  tail); each was found by one referee and signed by the other (REFEREE-2 Add. 1 table, GT-1 = G-5, GT-4 = G-7, GT-5 = G-6, GT-7 = G-1).
  L43: GL-1..GL-3 move RA-MULT, the polynomial RA-path bound and K1-FLIP(c) (asymptotic, refuted on finitely many instances) from DEAD to
  DATA, with numbers and, in L-5, source commits (fixes entry 5 F5-1, CHECKER C142 E-1): «re-arm multiplicity m 8 / 32 with C 17 / 65 on
  MW8_2 / MW32_2 (refutes a constant multiplicity only below 32), the RA path count P 54 / 2583 (= F_(d+2) − 1 at d = 8, 16) with C 3 on
  FW8_2 / FW16_2 (m and P: L-SI 47 box 90, claude/l-si 2d0344d3 and 4ded1e8d, box90/out/mw90.out maxm and fw90.out maxP, both engines)»,
  per-gate flips 9 / 17 / 33 at lamch 0 on MWR4/8/16_2 (L-RED 63, claude/l-red 406ef2fd; box93 mwr93 outputs); L-5's growth clause gives
  numbers on named instances only, and A*_all left the DATA (fixes entry 5 F5-2, CHECKER C142 E-2); the remaining DEAD rows are
  constructions with numbers (Lead 03:00Z).
- Not signed: packet §4 (overlaps: L-RED 63 CLASS-PAYS / GATE-FLIP-MIN and REL-G, L-NEW 68 GATE-CLASS), §5 DEAD list as statements
  (reproduced as DATA), §6 DATA and controls, §7 TARGET reading, §8 attack record (L-RED 62-63, R228-box91, R229-box92, R229-box93); the
  READING remarks; the referees' replays.
- Referee strengthening (NOT part of this entry; referee checks): (i) REFEREE 31: own engine («no lane code; scratch/gate_replay.py,
  scratch/gate_lev.py; logs scratch/gate_logs/»), «EVERY must-be-0 counter is 0 on every instance, on both engines, including k10 = 0 and
  dpass = 0 on g3 (as GT-1 predicts from B-ONLY3).» (l. 196-197); «Controls fire on both: cJoin 588, cLow 14,013, cNP 1,469, cD 13,048
  (totals, each engine); cU 16,929 (cyc) / 29,758 (g3) couples.» (l. 197-198). (ii) REFEREE-2 37: own engines («Lane code is not imported:
  my replay is R2-P-N5-GATE/r2gate.py, on REFEREE-2's own engines.»), «Every must-0 counter is 0 on every row, and dpass = 0 and rec_k10 = 0
  on both engines:» (l. 345); «pinned: the lane's frozen instances with N ≤ 170, 41 genomes (box 91, 93, 94, 95 fix1 inst/, copied from
  9c0349b1), × 2 engines.» (l. 346); «These are small (T ≤ 7, C = 1) and test little beyond (a)-type statements. I say so rather than count
  them as strong evidence.» (l. 351); «NOT RUN: the 16 pinned genomes with N > 170» (l. 356); Add. 4 on IDEAL-CYC, no size cap: «MW32_2: T
  199, C = 65 = 2n + 1 (n = 32), A*_all 66, max per-gate flips 130 = 4n + 2 with lamch 0.» (l. 581); successor 38's Add. 5: «OWN RECOUNT
  (new). C142 E-1 noted that neither referee had recounted m or P.» (l. 624), on its own engines MW8_2 / MW32_2 maxm 8 / 32 and FW8_2 /
  FW16_2 maxP 54 / 2583 on IDEAL-CYC, «NOT RUN on Γ3: MW32_2, FW16_2 (size).» (l. 627). (iii) L-RED 62-63 (not referees): the attack record
  (packet §8), every PROVED statement SURVIVES; L-RED 63's exact dexact for E-FACE-PAYS (b) on 29 instances (claude/l-red fa4e50fe), cited
  in L-5.
- Honest limits: (i) No running-time bound: every statement is a reduction of one run's counts to per-gate or per-continuation counts of the
  same run; none bounds T3, T_CYC, C or A*_all by a polynomial; A*-EQUIV (iii) is an equivalence whose sides are not proved polynomial. (ii)
  One run per game: IDEAL-CYC(G) and HOW3(G) on Γ3(G) up to N5′-xi's first fallback; nothing for N5 (SPEC S4a), for post-fallback
  iterations, outside the genome family, or on general parity games. (iii) On Γ3 everything rests on RESULTS R125, and four premise items
  are P-N5-CHAIN's frozen text, not RESULTS text (G-4); A*-EQUIV (ii), (iii) hold on Γ3 only and rest on RESULTS R127. (iv) DATA are runs of
  two engines (L-RED R221 own.py on IDEAL-CYC, cap 3000; L-NEW's Γ3 N5′-xi, cap 20000) and the referees' engines on short runs (T ≤ 199);
  they test that no lemma counter fires, not a bound; large zero counts are DATA, not evidence. (v) The DATA give numbers on named instances
  only (n = 4-32; fixes entry 5, CHECKER C142 E-1, E-2), and no growth rate in n is claimed; the DATA rows of GL-3 refute their asymptotic
  statements only on the named instances (L43). (vi) The DEAD rows kill constructions, not lemmas; K6's CNT was not re-counted by a referee;
  FW's P and MW's m were, by REFEREE-2 Add. 5 on its own engines (on Γ3 not for MW32_2, FW16_2). (vii) Names: «P-N5-GATE» is also R101's
  packet name (G-6); this entry's packet is docs/si/P-N5-GATE.md. «TRIGGER» is also R107's; this entry's is «RESULTS R128 Corollary
  TRIGGER». (viii) Literature: VJ00 §4.2 / Friedmann arXiv 1106.0778 §3 for [VJ] as in R118 / R123; no novelty is claimed.
- Data (DATA, not proof): experiments/si/box90-box96 at l-si 7b0a58ae (the same as at 676b6a1c except box95/check95.sh and box95/fix5; box
  91-94 tools mult91.py, gate92.py, astar92.py, np93.py, lev94.py; box 95 fix3/copy95.py; box 96 d96.py; frozen instances with SHA1SUMS;
  outputs out/*.out for both engines; check91-96.sh), called from experiments/si/check.sh l. 1279-1293 at 7b0a58ae (the same 15 lines at the
  l-si head 3417f6c1; sha1 3695caa43cffe0e41c5f85ad34b1f2dbe30d2594; l. 1279-1290 at 676b6a1c, sha1 bfee3e33…; 7b0a58ae adds the fix5 call
  in box95/check95.sh and the L-5 pin), run by scripts/verify.sh once merged. Re-run by the drafter from a full git archive of 7b0a58ae with
  the object store visible: 2026-11-12T21:50:01Z-2026-11-12T21:50:20Z, rc 0, «BOX91 OK» … «BOX94 OK», «P-N5-GATE fix1 checks: PASS» …
  «P-N5-GATE fix5 checks: PASS», «si (P-N5-GATE L-5 pinned): PASS», «BOX96 checks: PASS», no NOT RUN line; with one byte appended to L-5 the
  box 95 block printed «BOX95 FAIL fix5», rc 1 (negative control; restored, all re-run rc 0, 2026-11-12T21:50:29Z-2026-11-12T21:50:48Z); on
  676b6a1c (14:03:07Z-14:03:25Z, rc 0) the negative controls «BOX95 FAIL fix4» (one byte appended to L-4) and «BOX91 FAIL own rows» (one
  byte added to a pinned own91.out row) gave rc 1. Frozen totals (by script, data128a.py, 48 checks on 676b6a1c, whose box 90-94 and 96
  trees 7b0a58ae keeps): every lane must-0 counter of the DATA clause (the same in L-4 and L-5) 0 on its set and both engines, rows
  identical (L-RED 63's dexact cited, not re-checked); pecouples 28, 496, 10, 121, 103, 74; max lowch 599; PROVISO 307,737 (gate, state)
  pairs per engine, control on 14 of 19; copy rows set-equal on 20 of 22; controls gr2fail 8, glnfail 26, relfail 4, pefail on every couple;
  C 17 / 65 on MW8_2 / MW32_2, 3 on FW8_2 / FW16_2; flips 9 / 17 / 33 at lamch 0 on MWR4/8/16_2; box 90 maxm 8 / 32 and maxP 54 / 2583; for
  L-5 (data128b.py, 48 checks on 7b0a58ae, both engines, by column name): maxm, maxP and C as above with FW depth 8 / 16 (F_10 − 1 = 54,
  F_18 − 1 = 2583), maxflip 34 / 130 on MW8_2 / MW32_2, mx_flips 9 / 17 / 33 = 2·mx_ch_D + 1, mx_ch_D = mx_ch_pe 4 / 8 / 16, mx_ch_pb 9 / 17
  / 33 and mx_lam_pe = mx_lam_pb = 0 on MWR4/8/16_2. Independent re-measurement (cited in L-5 or the packet): L-RED 63 dexact / dpass
  (claude/l-red fa4e50fe), R228-box91, R229-box92/93/203.
- Signatures: REFEREE docs/referee/R-P-N5-GATE.md, successor 31 (731db590 2026-11-11T22:51:49Z, a401ce0e 2026-11-11T23:29:45Z, 41228433
  2026-11-12T02:50:26Z, fbc4d865 2026-11-12T03:28:29Z, 49d34123 2026-11-12T05:09:52Z): §0 verdict table l. 290-307; §K «**Line L-4 MATCHES**
  (L-3 + exactly LT-1, GL-1..GL-3 and the entry count)»; successor 34 (16e8dcb0 2026-11-12T20:49:58Z): §L «Verdict: fixes entry 5 CORRECT.
  **Line L-5 MATCHES** (L-4 + exactly C142 §4's nine pairs + the tenth pair; sha1 459fd88d…, 12,923 B).» (l. 457). REFEREE-2
  docs/referee-2/R2-P-N5-GATE.md, successor 37 (a28bc5e1 2026-11-12T00:04:33Z, 276545dc, c035b35f 2026-11-12T00:50:26Z, 8983b3d8
  2026-11-12T01:14:17Z, 6269fec5 2026-11-12T02:50:37Z, 93413fc6 2026-11-12T05:10:00Z, 3282fc6c 2026-11-12T05:40:10Z): verdict table l.
  393-405; Add. 3 «L-4 (676b6a1c, sha1 6bfde78e) MATCHES.»; «Open condition, unchanged: P-N5-SPLIT must land as R127 before this entry.» (l.
  571), met at f9520557 (G-LT1 of the first-fill record); successor 38 (0df0fdd8 2026-11-12T19:07:28Z): Add. 5 «Verdict: L-5 (7b0a58ae, sha1
  459fd88d) MATCHES.» (l. 681), and «A «signed by both referees» MATCH is unconditional only after REFEREE's own L-5 test is checked on
  origin/claude/referee.» (l. 688): REFEREE §L is on origin/claude/referee (16e8dcb0, its head at the fetch of 21:45:13Z). Lane
  (claude/l-si): L-SI successor 49, 4066f579 (packet FROZEN); successor 50, ecc5fe25, 9c0349b1, ef14451f, 676b6a1c (fixes entries 1-4,
  L-1..L-4); successor 52, 7b0a58ae (fixes entry 5, L-5). Adversary (not a signature): L-RED 62-63 (R228-box91, R229-box92, R229-box93), the
  attack record.
- INDEPENDENCE: each referee wrote its first verdict without reading the other's (REFEREE «Not read before my own verdict: docs/referee-2/,
  L-RED 62-64's records (R228-box91, R229-box92/93/94/203, R230).» (l. 3); REFEREE-2 «Independence: I have not opened
  docs/referee/R-P-N5-GATE.md (REFEREE 31) or notes/REFEREE.md.» (l. 5) and «Before this verdict I did not open docs/referee/R-P-N5-GATE.md
  (REFEREE 31), notes/REFEREE.md, or L-RED's R228 / R229 reports and tools.» (l. 415-416)). REFEREE-2 read REFEREE's report only after its
  verdict was on origin (Add. 1, «written after my verdict c035b35f was on origin» (l. 422)); REFEREE read the adversary records after §0
  («Adversary records, read AFTER §0 (context only, not signatures)» (l. 309)). On L-4 each tested the bytes alone: REFEREE §K with strings
  from its own §J, «not from the lane's byte copy» (above); REFEREE-2 Add. 3 «I read REFEREE 31's §I / §J only as quoted in entry 4. I have
  not opened claude/referee fbc4d865 for this test.» (l. 573). On L-5 likewise: REFEREE §L «Second, independent byte test; claude/referee-2
  0df0fdd8 NOT read before this section was committed.» (l. 415); REFEREE-2 Add. 5 «I have not read docs/referee/ for this test» (l. 590)
  and «the lane's mkL5.py and mkfix5.py are not imported and not run» (l. 601). Each referee re-derived every proof step and replayed the
  DATA on its own engine.
- TARGET.md diff: TARGET.md §2 (M4) asks for one deterministic algorithm, polynomial on EVERY parity game, that outputs (W_E, W_O); this
  entry is a set of lemmas about one run of Howard / VJ strategy improvement on two restricted games per genome, with reductions and one
  equivalence, and no bound (TARGET.md §4: «Polynomial only on a restricted class (bounded d, treewidth, Strahler/register number, ...).»;
  packet §7 l. 218-223; REFEREE «## 6. TARGET.md diff: CLEAN»; REFEREE-2 Add. 2 «correct paraphrase of §2 / §4»). It is not an algorithm
  claim on every game, so TARGET.md §5's gauntlet does not apply, and it is not a step-4 pass. L-5 ends its scope words «these lemmas bound
  nothing by a polynomial, so this is not M4 and not M3; G-N5-TIME stays OPEN; not a step-4 pass, not a TARGET.md claim». GAPS G-N5-TIME:
  open.

Proposed GAPS line-11 UPDATE (append-only), to go AFTER the last UPDATE on GAPS l. 11 at landing (R127's, «UPDATE 2026-11-12 13:58Z: RESULTS
R127 (P-N5-SPLIT; CHECKER C141 850e9765)», the last at f9520557), as a pure insertion with one separating space before the row's closing
« |». BUILT FROM L-5 by r128b/tools/upd128b.py (= r128a/tools/upd128a.py with an L-5 section appended and its functions unchanged; R118's
procedure: the direct build of r127a/tools/upd127a.py, with ONE generalisation, direct2: the connector before a label may be «; » or «,
and », kept, the label moved behind its clause (G-U (i)); R128's constants: date «(2026-11-09)», start «for every genome G (premises: … π(X)
the elements of X at least as relevant as e_o: » (the span up to the first label, 2,945 characters), its twelve labels «(Lemma GATE-RACE)»,
«(Corollary TRIGGER)», «(Lemma GATE-LOW-NULL)», «(Lemma NP-SHAPE)», «(Corollary E-FACE-PAYS)», «(Lemma WAIT-QUIET)», «(Lemma SAME-SUFFIX)»,
«(Lemma STEP-BOUND)», «(Lemma PARALLEL)», «(Lemma PAIR-EXPEL; its Step 1 is the argument of P-N5-SPLIT §3 (a), Lemma REWIN (a), which the
packet writes out in full from F1, STRICT, F3, F6, F4′, CN2-3, so no P-N5-SPLIT premise is used)», «(Corollary EXPEL-COUNT)», «(Corollary
A*-EQUIV, PROVED-CONDITIONAL on RESULTS R127 (P-N5-SPLIT)'s SPLIT-COUNT and C-EQUIV)», drops «; G-N5-TIME stays OPEN» and «; not a step-4
pass, not a TARGET.md claim» (L-4's and L-5's form of the landed second drop, G-U (ii); confirmed by C142 §3), source prefix «(P-N5-GATE,
docs/si/P-N5-GATE.md»), with NO reading; controls on f9520557: the same function (direct and direct2) rebuilds R125's landed UPDATE
(f22faed5…; filled with 2026-11-11, 23:47, 1622c7d9 it occurs once on l. 11: True), R126's (89c5f357…; 2026-11-12, 06:44, 7b2fa753, once:
True) and R127's (5bd83938…; 2026-11-12, 13:58, 850e9765: it ends l. 11, True); negative controls (an altered drop string; an altered label)
raise errors; GAPS at trunk 85e42158 equals f9520557's. Further controls: on L-4 it gives the first fill's
90d1e0ca964af3edc672aea76fa69fef1d799be9 (True); on CHECKER's 7ebcf735 (L-4 + C142 §4's nine pairs) it gives the line C142 §4 calls
«UPDATE-5», f7edaed8b32cdad441bbe22c6111dd792fa96f59 (True), and the line built here is that one with the tenth pair «docs/si/P-N5-GATE.md
with its fixes entries 1-4,» → «docs/si/P-N5-GATE.md with its fixes entries 1-5,» applied (True); on L-5 with an altered drop string or an
altered label it raises errors, and with one changed byte («1-5» → «1-6») it gives a different line. sha1
ba6958119e92cc3ab00cee0348fc69a9e51441b3 of the line without newline and unfilled (221f1c5b7c819d244f2e23a988ca1b32d02ac141 with its
newline), 12962 bytes. <DATE>, <HH:MM> and <checker> are the landing date, time and the CHECKER commit of the PASS (C142), all filled at
landing:
UPDATE <DATE> <HH:MM>Z: RESULTS R128 (P-N5-GATE; CHECKER C142 <checker>) [refereed-only] LANDED: Gate races, expulsions and who pays a gate flip, in ONE Howard strategy-improvement run with Vöge-Jurdziński values, on IDEAL-CYC(G) and on N5′-xi's mover phase on Γ3(G) from S3, for every genome G (premises: RESULTS R104's definitions of the genome and of Γ(G) only («e of even priority above every β with one edge to the W-target or to the top even self-loop c_W»); RESULTS R117's definition of Γ3(G) only; RESULTS R118 (a) IDEAL-CYC(G) («The game is Γ(G) with every Even vertex that is not a mover frozen at its start successor. Odd is unrestricted (gates and K2).») with its Howard step and tie rule («every mover x goes to a successor of ⊴-largest Ω_t value, and keeps σ_t(x) if σ_t(x) is such a successor»), (b) F1, F2, F3, F4′'s stated clause, F6, (c) STRICT, (e) in its per-vertex form, and (k) the form of N5′-xi's run on Γ3 from S3 up to its first fallback («T3 is the first state at which no mover has a strictly better successor in Γ3;») with N5′-xi's rule [N5XI] («an N5′-xi run (box 190's S4a tie rule by Ξσ)»; SPEC S4a's A(v) = {σ(v)} ∪ {w : (v, w) ∈ Iσ}, so a ⊴-best current option is kept); VJ00 §4.2 / Friedmann arXiv 1106.0778 §3 for the value (Λ, Π, k) and its order ⊴; [OPT] as in RESULTS R123 (σ̄_t optimal at every vertex at once against σ_t); RESULTS R121 Lemma E-MON («(Lemma E-MON) if Λ_t(v) = Λ_(t+1)(v) then E_t(v) ≤ E_(t+1)(v)»); RESULTS R123 Lemmas CN2, LOC-GATE, LOC-K2, B-ONLY («at every state t and every vertex v other than c_W and the e-vertices whose successor is c_W, Λ_t(v) is less relevant than every e-vertex») and Corollary NO-TIE («at every state and gate g, Ω_t(e_g) ≠ Ω_t(β_g)»), and (E-DOM) and (Core) read off RESULTS R104's priorities and closed core with LOC-K2 (non-core vertices only: the core is entered only at K0 and then follows one fixed suffix, so K0, K3 lie on the play iff Λ is a core vertex), for IDEAL-CYC; on Γ3 instead RESULTS R125 (P-N5-CHAIN): F1, F3, F4′, F6, STRICT, CN2-3, LOC-GATE3, NO-TIE3, LOC-K2-3, B-ONLY3, E-MON3, and F2, CYC, (E-DOM), (Core) from P-N5-CHAIN's frozen text (l-new 93531b03, sha1 6e613ba7, §2 and §4), (Core) in its W-1-repaired reading, applied only to non-core vertices (the faces of a gate and the successors of a mover or a gate; P-N5-CHAIN fixes entry 3, R-W; referee-originated: REFEREE-2 R2-P-N5-GATE G-1); for A*-EQUIV also SPLIT-COUNT and C-EQUIV of RESULTS R127 (P-N5-SPLIT; L-NEW, frozen claude/l-new 399cda07, sha1 5bc1b1f3; landing order R126 = P-N5-QN, R127 = P-N5-SPLIT, then this entry); no L-RED lane lemma is a premise), with Ω_t, P_t, Λ_t, E_t(v) (the e-vertices of P_t(v) more relevant than Λ_t(v)) the value, play, cycle node and e-set at state t, a gate o with e-vertex e_o, e-face p_e (= e_o on Γ, its pad on Γ3), β-face p_b and D := e_o's successor, a FLIP of o a change of σ̄(o) (an UNLOCK p_b → p_e or a RELOCK p_e → p_b), ch_f the number of steps at which Ω(f) changes, lamch(o) the number of steps at which Λ changes at p_e or p_b, nl_f := ch_f − (Λ-changes of f), LAM_t: Λ_t(p_e) = Λ_t(p_b), PRIV_t: e_o ∉ E_t(p_b), UP_t: e_o more relevant than Λ_t(p_e), π(X) the elements of X at least as relevant as e_o: if o flips at t from face p to face q then Ω_t(p) ≠ Ω_(t−1)(p), and flips(o) ≤ min(ch_p + ch_q, 2·min(ch_p, ch_q) + 1) (Lemma GATE-RACE); that change of p is a change of Λ(p) (at most 2M + 2 over the run), or inside one Λ-interval of p a change of E(p) whose most relevant differing element enters and lies on P_t(p), or a change of Π(p) below every e-letter or of k (Corollary TRIGGER); (a) at a LAM ∧ PRIV step with e_o ∈ E_t(p_e), Ω_t(p_e) ▷ Ω_t(p_b) iff π(E_t(p_e)) is lex-larger than π(E_t(p_b)) (and they differ), so (b) a flip at t with LAM ∧ PRIV ∧ UP at t − 1 and t changes π(E(p_e)) or π(E(p_b)) at t, and (b′) if Λ(p_e) = Λ(p_b) is the same at t − 1 and t, π(E(p_e)) rises at a relock and π(E(p_b)) rises at an unlock (Lemma GATE-LOW-NULL); at a step with e_o ∈ E_t(p_b), σ̄_t(o) = p_e, P_t(p_b) = A_t · o · P_t(p_e), Λ_t(p_b) = Λ_t(p_e) and E_t(p_e) ⊆ E_t(p_b), and a flip has such a step on at most one side, a relock if before and an unlock if after (Lemma NP-SHAPE); (a) relocks(o) ≤ ch_(p_e), unlocks(o) ≤ 1 + relocks(o) and unlocks(o) ≤ ch_(p_b) with no PRIV, LAM or UP hypothesis, (b) at every t with e_o ∉ P_(t−1)(D) ∪ P_t(D) the value of p_e changes iff that of D does, so (c) if D's play avoids e_o at every state of the run then unlocks(o) ≤ 1 + ch_D ≤ 2M + 3 + (2M + 3)·M·C + gam(D) (C the largest number of changes of one vertex's e-set with one top letter inside one Λ-interval, gam(D) the changes of Ω(D) with Λ and E unchanged), and (d) flips(o) ≤ 2·min(ch_(p_e), ch_(p_b)) + 1 ≤ 2·lamch(o) + 2·min_f nl_f + 1 (Corollary E-FACE-PAYS); a gate whose D's play avoids e_o at every state of the run and whose D changes value at most K times unlocks at most K + 1 and flips at most 2K + 1 times, whatever its trigger (Lemma WAIT-QUIET); on a window W inside one Λ-interval of a vertex o on which every successor f of o has P_t(f) = P_f · P_t(y) for fixed paths P_f to one vertex y whose play avoids every P_f, the ⊴-order of the successors' values is constant, so σ̄(o) is constant on W if o is Odd and σ(o) is constant from W's second step if o is an Even mover (by the tie rule above) (Lemma SAME-SUFFIX); Ω(x) changes at t only if some vertex of P_(t−1)(x) changes successor at t, so ch_x ≤ T (Lemma STEP-BOUND); inside one Λ-interval of b, at a change of H_s := E_s(b) ∩ U_y (U_y the e-vertices more relevant than y), the top x of the change lies on the new play only and every expelled letter on the old play only, below x and strictly after b's split (Lemma PARALLEL); two expulsions of one letter z at b through the same split pair (u′, b′) leave E(b′) ∩ U_z strictly lex-larger at the later one (Lemma PAIR-EXPEL; its Step 1 is the argument of P-N5-SPLIT §3 (a), Lemma REWIN (a), which the packet writes out in full from F1, STRICT, F3, F6, F4′, CN2-3, so no P-N5-SPLIT premise is used), and the number a_z(b, J) of runs of z in E(b) on a Λ-interval J is at most 1 + 3M·max Dhi_z (at most 3M split pairs: the split is a mover or a gate, with M mover edges and 2M faces; referee-originated: REFEREE-2 R2-P-N5-GATE G-6), Dhi_z(b′, J′) the number of distinct E_s(b′) ∩ U_z on J′ (Corollary EXPEL-COUNT); C ≤ A*_all ≤ 1 + M·C (on both runs, with no P-N5-SPLIT premise: each entry of a top starts a run, and every run but one starts at a change; referee-originated: REFEREE-2 R2-P-N5-GATE G-7) and, on Γ3 only, C ≤ 3M·(1 + M·A*_route), so T3 is polynomial iff C is iff A*_all is iff A*_route is (A*_all the largest a_z(b, J) over all b, J, z; A*_route the same over the new successors of split pairs) (Corollary A*-EQUIV, PROVED-CONDITIONAL on RESULTS R127 (P-N5-SPLIT)'s SPLIT-COUNT and C-EQUIV): these are reductions of one run's counts to per-gate or per-continuation counts of the same run, not bounds: none bounds T3, T_CYC, C or A*_all by a polynomial; on IDEAL-CYC a LAM ∧ PRIV step with e_o not above Λ (row K10 of WAIT-CLOSED) does not occur, by RESULTS R123 B-ONLY, so GATE-LOW-NULL covers every flip between two LAM ∧ PRIV steps there, and on Γ3 it does not occur either, by RESULTS R125's B-ONLY3, the same argument with the pads (pβ_o is never an exception; pe_o is one only when D = c_W, and then Λ(pe_o) = c_W ≠ Λ(pβ_o); referee-originated: REFEREE R-P-N5-GATE GT-1 and REFEREE-2 R2-P-N5-GATE G-5); on IDEAL-CYC the proviso «D's play avoids e_o» of E-FACE-PAYS (c) and WAIT-QUIET always holds (Lemma PROVISO, credit L-RED 63: if e_o lay on P_t(D), the play would close at D, the vertex after e_o, so its cycle would carry e_o and Λ_t(D) would be at least as relevant as e_o, against RESULTS R123 B-ONLY at the mover D; D = c_W is its own loop), so on IDEAL-CYC E-FACE-PAYS (b) holds at every step and (c) and WAIT-QUIET hold with no proviso, B-ONLY being the one premise shared with the K10 clause above, and on Γ3 it holds at every state 0, …, T3 by RESULTS R125's B-ONLY3 at the mover D, by the same argument, so there too (b), (c) and WAIT-QUIET hold with no proviso (referee-originated: REFEREE R-P-N5-GATE GT-1 and REFEREE-2 R2-P-N5-GATE G-5); DEAD, on frozen instances (DATA, two engines unless said): a waiting High WC (T3 = 4 at n = 4, 8, 16; WC4_2, WC16_2), the lagging merged copy K6 LAG TOWER (CNT ≤ 4, 3, 2, 2 at h = 2, 3, 4, 5), the High continuation on the race K7 (C = 2; Ku_4, Ku_8, Ku_16, Kprev_8), nesting multipliers at H = 2, 3 (C, flips and T3 of one MW(n) or the sum; 22 instances) and the non-common-suffix nesting Db / Dbr (one MW(n)'s counters; NDb2_4 … NDbr3_8, L-RED 63), all in experiments/si/box91, box93, box94 and box95/fix1 inst with sha1 files; DATA, not DEAD (asymptotic statements, finitely many instances; L43): re-arm multiplicity m 8 / 32 with C 17 / 65 on MW8_2 / MW32_2 (refutes a constant multiplicity only below 32), the RA path count P 54 / 2583 (= F_(d+2) − 1 at d = 8, 16) with C 3 on FW8_2 / FW16_2 (m and P: L-SI 47 box 90, claude/l-si 2d0344d3 and 4ded1e8d, box90/out/mw90.out maxm and fw90.out maxP, both engines), and per-gate flips 9 / 17 / 33 at lamch 0 on MWR4_2, MWR8_2, MWR16_2 (L-RED 63, claude/l-red 406ef2fd; refutes c·(lamch + 1) only for c ≤ 32); DATA, clause by clause (two engines: own = L-RED R221 own.py on IDEAL-CYC, g3 = L-NEW's Γ3 N5′-xi from S3; rows identical; set S11: box 91's 11 instances; tools experiments/si/box91-box94, run by check91-94.sh): GATE-RACE and TRIGGER: grfail, gr2fail, grwhy, trfail 0 (unit: Odd vertex with two successors for grfail and gr2fail, flip for grwhy and trfail; whole run; S11; own to the cap 3000, g3 to the first fallback or the cap 20000); GATE-LOW-NULL: decfail 0 (unit (gate, state): the decider is at least as relevant as e_o; (a)'s order equivalence is not counted by the lane), glnfail and lowflip 0 (unit: flip with LAM ∧ PRIV at t − 1 and t; S11), (b′) no separate lane DATA, with up to 599 changes below e_o that never flip a gate; NP-SHAPE and E-FACE-PAYS: npside, npsub (unit (gate, state)), npboth, npkind (unit flip), relfail (relocks > ch_(p_e)), unlfail (unlocks > 1 + ch_(p_e); the bounds unlocks ≤ 1 + relocks and unlocks ≤ ch_(p_b) are not counted by the lane), dfail (a proxy for E-FACE-PAYS (b)) 0, and k1both = k1c2 (unit gate for relfail, unlfail, k1both, k1c2; 18 instances: S11, k1fail_202, Ku_8, Ku_16, Kprev_8, MWR4_2, MWR8_2, MWR16_2), and the exact form of E-FACE-PAYS (b), L-RED 63's dexact (D's play followed vertex by vertex), 0, with dpass (steps at which D's play passes e_o) 0 (unit (gate, step); 29 instances; own engine only, cap 3000; claude/l-red fa4e50fe R229-box93 §2); PROVISO: dpass 0 (unit (gate, state); 19 instances, box 91's 11 and box 93's 8, 307,737 pairs per engine; both engines, rows identical; experiments/si/box96 d96.py), and the control with Odd made non-optimal (own engine; e-face at o, β-face at every other gate) fires on 14 of the 19; SAME-SUFFIX: copy rows S(R_j) = S(R_(j−1)) as sets on every level of box 94's 20 simultaneous-clock instances (all but NSQ2_4, NSQ3_4, whose levels run one after another and whose rows differ) (REFEREE replay, own engine; L-SI's set re-measure copy95.py agrees on both engines; the lane's lev94 compares sizes), and 0 flips at the copied gates on NDV and NDB (unit level); PARALLEL: par1-3 0 (unit: change of H with an expelled letter, at route tuples; x's position after u′ not counted); PAIR-EXPEL and EXPEL-COUNT: pefail, ecfail, pelam 0, with lexfail and dhifail 0 (E-MON3 on H) (unit change of H, tuple (b, J, y) or same-pair couple; S11; 28, 496, 10, 121, 103, 74 couples); A*-EQUIV: cfail (c_y > a_y) 0 (unit (v, I, z); S11); controls fire (CTRL=gr 8 on MW8_2, CTRL=low glnfail 26 and CTRL=swap relfail 4 on C6G8_n54, CTRL=uz pefail on every couple); growth, as numbers on the named instances only (both engines; box91/out/own91.out and g391.out C and maxflip, box93/out/mwr93_own.out and mwr93_g3.out mx_flips and mx_ch_D): C 17 / 65 and the largest per-gate flip count 34 / 130 on MW8_2 / MW32_2, and per-gate flips 9 / 17 / 33 = 2·ch_D + 1 (ch_D 4 / 8 / 16) with lamch 0 on MWR4_2, MWR8_2, MWR16_2, where E-FACE-PAYS (d) holds with equality; no separate DATA for STEP-BOUND and for A*-EQUIV's equivalence; TARGET.md §2 (M4) asks for a deterministic algorithm polynomial on every parity game and §4 says a bound on a restricted class, or one resting on an unproved conjecture or an empirical observation, is not M4: these lemmas bound nothing by a polynomial, so this is not M4 and not M3 (P-N5-GATE, docs/si/P-N5-GATE.md with its fixes entries 1-5, docs/si/P-N5-GATE-fixes.md; L-SI successors 48-50). G-N5-TIME stays open.

Addendum (subagent, first fill; checks run on the pass-1 draft, whose title, entry block, GAPS preamble and UPDATE are byte-equal to this
file's; outputs r128a/*_p1.out; the final run on this file is r128a/*_final.out). Verbatim key lines, with «|» printed as «¦»:
  [chk] model: landed R127 title (f9520557) == «### R127 [refereed-only] » + R127 L-3 + «, CHECKER PASS (docs/checker/C141.md, checker 850e9765)»: True
  [chk] file: sha1 e88326e8f2aada6dae992f7deeb9848e94d773a3 bytes 85918 lines 464 ends with newline True
  [chk] ### R headings at d[...]: [248]
  [chk] (a) title == prefix + L-4 (no newline) + tail: True ; middle bytes == L-4 bytes without newline: True
  [chk]     title: 12369 chars, 12640 bytes, sha1 8716a9c28b529a56134ae6aedc5aed625d8d4aae, ( 231 ) 231, min depth 0, final 0, ¦ 0, fill token 1
  [chk] (e) entry block d[248:445] (lines 249-445, 197 lines, sha1 of the joined block 38bdf02f44ede52261ebe864784c56554b95c1ba); next line blank: True; line after: 'Proposed GAPS line-11 UPDATE (append-onl'
  [chk] (b) fill token in the entry block: 1 ; in the whole file: 1 at lines [249]
  [chk]     «\n**Erratum E-1** (not a result» in the block: False ; line-start «**Erratum» in the file: 0 ; empty lines inside the block: 0
  [chk] (e) UPDATE line(s) at d[...]: [462] (line [463])
  [chk]     GAPS preamble at d[446:462]
  [chk] (c) "¦" in entry block: 0 ; in UPDATE: 0 ; in GAPS preamble: 1 (the quoted « ¦» of the row end); in the file: 9
  [chk] (d) UPDATE <DATE> 1 <HH:MM> 1 <checker> 1; head at its start: True
  [chk]     UPDATE = upd128L4.txt: True ; sha1 (no newline) 90d1e0ca964af3edc672aea76fa69fef1d799be9 ; with newline 7520792b0486039e20a2493f06f378cb858e79ed ; 12601 bytes ( 230 ) 230
  [chk]     stale grep, entry block minus title (case-insensitive): {}
  [chk]     stale grep, title: {'pending': 1} ; UPDATE: {}
  [chk]     line 1 «NOT LANDED» 1 ; «<DATE>» in file 3 ; «<checker>» 4 ; «<HH:MM>» 3
  [chk] (e) slices: line 1 d[0]; FIRST FILL record d[1:247] (+ blank d[247]: ''); title d[248]; entry d[248:445]; blank d[445]; preamble d[446:462]; UPDATE d[462]; blank d[463]: ''; Addendum none
  [chk] (f) QUOTE SWEEP (corpus: 102 texts)
  [chk]     sweep line 1: 1 quotes, 1 parts, 0 not found []
  [chk]     sweep FIRST FILL record: 189 quotes, 167 parts, 0 not found []
  [chk]     sweep entry block: 121 quotes, 137 parts, 0 not found []
  [chk]     sweep GAPS preamble + UPDATE: 30 quotes, 28 parts, 0 not found []
  [chk]     sweep whole file: 341 quotes, 333 parts, 0 not found []
  [chk]     sweep NEGATIVE CONTROL: 1 quotes, 1 parts, 1 not found ['GATE-RACE bounds every gate by two flips on every genome']
  [chk]     negative control reported missing: True
  [lp] cites 133 (86 shown in the draft as «quote», 47 used for a line number only) in 17 (commit, file) pairs; failed at the cited lines: 0 []
  [lp] shown quotes not in the draft as «quote»: 0 []
  [lp] NEGATIVE CONTROL 1 (window shifted by 40 lines): 0 of 133 still pass []
  [lp] NEGATIVE CONTROL 2 (longest word mutated): 0 of 133 still pass
  [lp]     3282fc6c docs/referee-2/R2-P-N5-GATE.md 2
  [lp]     4066f579 docs/si/P-N5-GATE.md 12
  [lp]     41228433 docs/referee/R-P-N5-GATE.md 3
  [lp]     49d34123 docs/referee/R-P-N5-GATE.md 7
  [lp]     6269fec5 docs/referee-2/R2-P-N5-GATE.md 3
  [lp]     676b6a1c docs/si/P-N5-GATE-fixes.md 10
  [lp]     676b6a1c docs/si/P-N5-GATE-line-L4.txt 1
  [lp]     731db590 docs/referee/R-P-N5-GATE.md 3
  [lp]     8983b3d8 docs/referee-2/R2-P-N5-GATE.md 8
  [lp]     93413fc6 docs/referee-2/R2-P-N5-GATE.md 8
  [lp]     a28bc5e1 docs/referee-2/R2-P-N5-GATE.md 3
  [lp]     a401ce0e docs/referee/R-P-N5-GATE.md 41
  [lp]     c035b35f docs/referee-2/R2-P-N5-GATE.md 26
  [lp]     f9520557 TARGET.md 1
  [lp]     f9520557 docs/DECISIONS.md 1
  [lp]     f9520557 docs/agents/LEAD-STATE.md 3
  [lp]     fbc4d865 docs/referee/R-P-N5-GATE.md 1
  [hex] hex ids in the draft: 97; git objects 60; measured sha1s (not objects) 37; neither: 0 []
  [hex] NEGATIVE CONTROL (0badc0de1, 1234abcd9f): neither: 2 ['0badc0de1', '1234abcd9f']
  [sim] trunk f9520557 RESULTS sha1 4117c8a7d0165cd8d3a880f9a405d9c6fc6a5089 lines 16769 "¦" 1477 ; GAPS sha1 ccf059a1558fc3e1ae769a7aa98506f5fa7d64d5 lines 23
  [sim] pure insertion: prefix byte-unchanged True ; suffix byte-unchanged True ; inserted lines 198
  [sim] headings after insertion: {'R126': [15726], 'R127': [15903], 'R128': [16127], 'E-1': [16325], 'E-2': [16338], 'E-3': [16366], 'Dead': [16397]}
  [sim] R127 at l. 15903 (unchanged: True); R128 at l. 16127-16323, blank l. 16324 (''), «**Erratum E-1**» l. 16325; the line before R128: l. 16126 '' (R127's block ends l. 16125)
  [sim] order R126 < R127 < R128 < E-1 < E-2 < E-3 < Dead ends: True
  [sim] RESULTS lines 16769 -> 16967 (+198) ; "¦" 1477 -> 1477 (unchanged True) ; «checker 3333333)» once True ; fill token 0
  [sim] ### R1xx headings: 29, R128 the last: True
  [sim] GAPS: only l. 11 changes True ; lines 23 -> 23 ; l. 11 "¦" 76 -> 76 ; «UPDATE 2026-» 62 -> 62 ; R128 last: True ; after R127's (2026-11-12 13:58Z, 850e9765): True ; prefix byte-unchanged: True
  [sim] GAPS whole file "¦" 198 -> 198
  [sim] fill values used only here: 2099-01-11 00:00 3333333

Addendum (second fill) (subagent, 2026-11-12, fill time 2026-11-12T22:01:53Z by date -u; for the Lead and CHECKER C142 Add. 1; does not
  land). Built by r128b/fill2.py from the first fill (docs/agents/R128-draft.md in the trunk working tree, sha1
  70db12a9e83b623a8aa6438494bffb4db029424e, 524 lines, asserted): every change is an (old, new) pair applied to one unwrapped unit (bullet,
  sub-item or the GAPS preamble), old asserted to occur once in its unit, the unit re-wrapped by the first fill's own wrap() (roundtrip
  asserted on every unit of the first fill); the pairs are in r128b/changes2.json (29 in the entry block, tags 3 / E-4 / X1-X4), the new
  quotes in r128b/cites2.json (36). Nothing in the repository was edited, committed, merged or pushed; scripts/push.sh and scripts/verify.sh
  were not run. Checks ran on the pass-1 draft r128b/R128-draft.p1.md (sha1 329025d7c78be8417ddb668d585bd3774498c324), which equals this
  file without this Addendum and its blank line (asserted by the final build). Fetch: Thu Nov 12 21:45:13 UTC 2026 rc 0 Thu Nov 12 21:45:14
  UTC 2026 l-si 3417f6c1f6244918ca43a43bd1b2cd21fe940788 checker 269effb3d6ea5b5789a38b8d247667243222c87b referee
  16e8dcb0050711dd470e986a0c92cb792c76daf4 referee-2 43824abc7408144fcb310f9a648a888b4d528c3e vibrant-johnson-nxvvxo
  85e42158d88087138d54a63fb712e545cb3b87b5 HEAD 21b87e70f15832e5c53ec7acb6c4db209e1bda02.
CHANGES vs the first fill (70db12a9). (1) Title (item 1): the first fill's prefix + L-5 (no newline) + the first fill's tail, asserted,
  middle bytes = L-5 without newline. (2) E-4 (item 2): Honest limits (vii) gets C142's string, appended after the sentence on R101's packet
  name. (3) Item 3 (tag 3, 18 pairs): Fixes bullet (five entries; 7b0a58ae, 332 lines, 34,305 B, sha1 7c389a35…; prefix chain from 676b6a1c;
  entry 5 with F5-1..F5-5 quoted); the RESULTS-line bullet rewritten for L-5 (459fd88d…, 7b0a58ae, blob c4ef22e8…, 238 / 238, mkL5.py,
  C142's nine pairs, 7ebcf735, the tenth pair; L-4 and its chain kept as L-5's source; REFEREE §L and REFEREE-2 Add. 5 rebuild quotes, the
  §K / Add. 3 quotes kept for L-4); Claims signed (successor 34 §L 16e8dcb0, successor 38 Add. 5 0df0fdd8, the marked re-signatures, C142
  E-1..E-3 closed by entry 5); Setting "fixes entries 1-4" -> "1-5"; (g) "dropped in L-4" -> "L-5"; Premise (prem128b.py on L-5; "of L-4",
  "(L-4)" -> L-5); L41 "named in L-4" -> L-5; Referee strengthening (iii) "cited in L-4" -> L-5; Signatures (§L verdict, Add. 5 verdict and
  its condition, lane successor 52 7b0a58ae); INDEPENDENCE (§L and Add. 5 independence quotes); TARGET.md diff "L-4 ends" -> "L-5 ends". (4)
  UPDATE (item 4) rebuilt from L-5 by the first fill's builder; the GAPS preamble now describes that build and its controls. (5) Flag list
  (item 5): C142's ruling appended to each of the 15 flag bullets (G-MERGE with the merge list) and one new bullet (E-1..E-4 FIXED). (6)
  This Addendum (item 6). BEYOND THE BRIEF (FLAG F-2; tags in changes2.json): X1 L41 / L43 bullet: the GL-3 rows restated from L-5 (the
  first fill repeated L-4's "m = n" and "P = F_(d+2) − 1", which C142 E-1 removed) and a growth-clause note (E-2); X2 Referee strengthening
  (ii) and Honest limits (vi): REFEREE-2 Add. 5 recounted m and P (the first fill's "FW's P were not re-counted by a referee" is false since
  0df0fdd8); X3 Honest limits (v): "The growth formulas (C = 2n + 1, flips 4n + 2, 2n + 1) are read off finitely many n" named formulas L-5
  no longer states, now "numbers on named instances only ... no growth rate in n is claimed"; X4 Data bullet: the boxes at 7b0a58ae
  (check.sh l. 1279-1293, fix5, the L-5 pin), the re-run at 21:50Z with a negative control, data128b.py's numbers. Not changed: line 1, the
  FIRST FILL record up to "FLAGS FIRST", the first-fill Addendum (its "this file's" means the first fill, 70db12a9).
FLAGS FOR CHECKER (second fill). F-1 E-4's string is in C142 §2 (the E-4 paragraph, l. 59-60), not in §4, and C142 names no insertion point
  beyond «Honest limits (vii)»; it is appended at the end of (vii), parsed by script between «Add, as R127's (viii) did for «Lemma SPLIT»: »
  and « No referee re-sign is needed for this item.» (occurs once). F-2 X1-X4 go beyond the brief's list ("and nothing else"): each keeps
  the entry true for L-5 or for the referees' new reports; any can be reverted by its pairs. F-3 Merge list (G-MERGE): claude/l-si at
  7b0a58ae (19 commits after 676b6a1c, 57 after the merge base 547985a1; merge-tree no conflict); and, NEW, 16e8dcb0 (REFEREE §L), 0df0fdd8
  (REFEREE-2 Add. 5) and 269effb3 (C142) are cited and are not trunk ancestors; claude/referee-2's head 43824abc is 3 P-N5-LEVEL commits
  past 0df0fdd8; 7b0a58ae brings boxes 99-104 into experiments/si/check.sh (run PASS on the archive, not on a merged tree);
  scripts/verify.sh not run. F-4 Line 1 still names the first fill only (R127's second fill extended its line 1); not changed, per the
  brief. F-5 REFEREE-2 Add. 5 says «REFEREE 33 byte-tests the same independently»; REFEREE §L is headed «REFEREE successor 34»; the entry
  uses §L's own heading. F-6 Notes N-L1 (§L) and N-3 (Add. 5): «lamch 0» rests on the columns mx_lam_pe / mx_lam_pb, which L-5's clause does
  not name; both referees ask no change; not acted on (data128b.py reads them: 0). F-7 The brief's "UPDATE at d[462]" and "block at
  d[248:445]" are the first fill's slices; here the title is d[282], the block d[282:522] and the UPDATE d[545] (the flag list grew 34
  lines).
  [fetch] Thu Nov 12 21:45:13 UTC 2026
  [fetch] rc 0
  [fetch] Thu Nov 12 21:45:14 UTC 2026
  [fetch] l-si 3417f6c1f6244918ca43a43bd1b2cd21fe940788
  [fetch] checker 269effb3d6ea5b5789a38b8d247667243222c87b
  [fetch] referee 16e8dcb0050711dd470e986a0c92cb792c76daf4
  [fetch] referee-2 43824abc7408144fcb310f9a648a888b4d528c3e
  [fetch] vibrant-johnson-nxvvxo 85e42158d88087138d54a63fb712e545cb3b87b5
  [fetch] HEAD 21b87e70f15832e5c53ec7acb6c4db209e1bda02
  [L5] C142 §4 pairs parsed: 9
  [L5]   pair 1: old count 1, 170 -> 315 chars
  [L5]   pair 2: old count 1, 207 -> 392 chars
  [L5]   pair 3: old count 1, 42 -> 46 chars
  [L5]   pair 4: old count 1, 33 -> 37 chars
  [L5]   pair 5: old count 1, 59 -> 64 chars
  [L5]   pair 6: old count 1, 46 -> 50 chars
  [L5]   pair 7: old count 1, 36 -> 40 chars
  [L5]   pair 8: old count 1, 72 -> 76 chars
  [L5]   pair 9: old count 1, 56 -> 60 chars
  [L5] after nine: sha1 7ebcf7355be9838473f05a7defe913940b6fd723 12923 B; = C142 7ebcf735: True
  [L5] F5-4 pairs parsed: 1 [('docs/si/P-N5-GATE.md with its fixes entries 1-4,', 'docs/si/P-N5-GATE.md with its fixes entries 1-5,')]
  [L5]   tenth pair old count 1
  [L5] L-5 rebuilt: sha1 459fd88d2d1959647f6aeb065bf8ac58cce684f9 12923 B; committed L-5 sha1 459fd88d2d1959647f6aeb065bf8ac58cce684f9 12923 B; equal: True
  [L5] L-5 shape: one line with newline, 0 "¦", ( 238 ) 238
  [L5] L-5 equal at origin/claude/l-si head: True
  [L5] git log of the L-5 file (all branches on origin/claude/l-si): 7b0a58ae 2026-11-12T18:03:39+00:00
  [L5] blob: c4ef22e8c48a2186923de9b35f7c81d0d4c58d5f
  [L5] NEGATIVE CONTROL: eight pairs only: sha1 89450d2a59b81f2ef1bed65ac5d4dbcbbdcba4f9 == 7ebcf735: False
  [L5] NEGATIVE CONTROL: nine pairs without the tenth == L-5: False
  [upd] trunk f9520557 GAPS sha1 ccf059a1558fc3e1ae769a7aa98506f5fa7d64d5 ; lines 23 ; l. 11 "¦" 76 «UPDATE 2026-» 62
  [upd] (1) control R125: sha1 f22faed54eeafdff59de062b1ed0294e3acb7ec6 = f22faed5…: True ; direct2 equal: True ; filled (2026-11-11, 23:47, 1622c7d9) once on l. 11: True
  [upd] (2) control R126: sha1 89c5f3571a20e19baf3782ffb2534b0ce62a2f68 = 89c5f357…: True ; direct2 equal: True ; filled (2026-11-12, 06:44, 7b2fa753) once on l. 11: True
  [upd] (3) control R127: sha1 5bd83938b1dfb6603581fc98669593ae2e09c83e ; direct2 equal: True ; filled (2026-11-12, 13:58, 850e9765) ends l. 11 before " ¦" (the last UPDATE): True
  [upd]     direct() (connector «; » only) on L-4: AssertionError '' (expected: the «, and » before (Corollary EXPEL-COUNT))
  [upd] (6) token diff L-4 -> UPDATE: 22 hunks, 76 tokens out, 77 in
  [upd] (8) first-fill UPDATE reproduced from L-4 (= d[462] of the first fill, 90d1e0ca…): True
  [upd]     START in 7ebcf735 equal to L-4's START: True
  [upd]     START in L-5 equal to L-4's START: True
  [upd]     direct() (connector «; » only) on L-5: AssertionError (expected: the «, and » before (Corollary EXPEL-COUNT))
  [upd] (9) CONTROL: UPDATE from CHECKER's 7ebcf735 (L-4 + C142 §4's nine pairs): sha1 f7edaed8b32cdad441bbe22c6111dd792fa96f59, 12962 bytes; = C142 UPDATE-5 f7edaed8…: True
  [upd] (10) UPDATE from L-5 (same builder, same constants, NO reading): sha1 no newline ba6958119e92cc3ab00cee0348fc69a9e51441b3; with newline 221f1c5b7c819d244f2e23a988ca1b32d02ac141; 12962 bytes, 12691 chars; connectors ['; ', '; ', '; ', '; ', '; ', '; ', '; ', '; ', '; ', ', and ', '; ']
  [upd]      ( 238 ) 238, depth ok True, ¦ 0, <DATE> 1, <HH:MM> 1, <checker> 1, «2026-11-09» 0, " — " 0, «G-N5-TIME stays OPEN» 0, «G-N5-TIME stays open.» 1, «not M3» 1, «LANDED:» 1, «pending» 0, «referee-originated» 5
  [upd]     UPDATE(L-5) == UPDATE(7ebcf735) with the tenth pair applied (old once in UPDATE(7ebcf735): 1): True
  [upd] (11) NEG drop altered in L-5 : AssertionError (expected)
  [upd] (11) NEG label altered in L-5 : ValueError (expected)
  [upd] (11) NEG one byte of L-5 changed (fixes entries 1-5 -> 1-6) : builds, sha1 b01f5f5d58cb02d6752accedc96bd554a9646894, == the L-5 UPDATE: False (expected False)
  [upd] (6) token diff L-5 -> UPDATE: 22 hunks, 76 tokens out, 77 in
  [upd] (6) token diff first-fill UPDATE (L-4) -> second-fill UPDATE (L-5): 23 hunks, 41 tokens out, 101 in
  [upd] (12) R128 filled UPDATE appended after R127's on l. 11: "¦" 76 -> 76; R128 last: True; R127 < R128: True; prefix byte-unchanged: True
  [upd]     GAPS at origin trunk 85e42158 and local HEAD 21b87e70 equal to f9520557's: True True
  [blk] 2026-11-12T21:50:01Z-2026-11-12T21:50:20Z rc 0 (tools/blocksGATE5.sh = check.sh l. 1279-1293 at 7b0a58ae, archive r128b/arch, object store visible):
  [blk] BOX91 OK
  [blk] BOX92 OK
  [blk] BOX93 OK
  [blk] BOX94 OK
  [blk] P-N5-GATE fix1 checks: PASS
  [blk] P-N5-GATE fix2 checks: PASS
  [blk] P-N5-GATE fix3 checks: PASS
  [blk] P-N5-GATE fix4 checks: PASS
  [blk] P-N5-GATE fix5 checks: PASS
  [blk] si (P-N5-GATE L-5 pinned): PASS
  [blk] BOX96 checks: PASS
  [neg] one byte appended to the archive's L-5 (sha1 8f077ef7450cac917cb4c54e2b866fa5f04ca350): 2026-11-12T21:50:28Z-2026-11-12T21:50:29Z rc 1 (tools/block95pin.sh = check.sh l. 1287-1291):
  [neg] P-N5-GATE fix1 checks: PASS
  [neg] P-N5-GATE fix2 checks: PASS
  [neg] P-N5-GATE fix3 checks: PASS
  [neg] P-N5-GATE fix4 checks: PASS
  [neg] BOX95 FAIL fix5
  [neg] restored: 459fd88d2d1959647f6aeb065bf8ac58cce684f9 (cmp equal to the backup); all blocks re-run 2026-11-12T21:50:29Z-2026-11-12T21:50:48Z rc 0:
  [neg] BOX91 OK
  [neg] BOX92 OK
  [neg] BOX93 OK
  [neg] BOX94 OK
  [neg] P-N5-GATE fix1 checks: PASS
  [neg] P-N5-GATE fix2 checks: PASS
  [neg] P-N5-GATE fix3 checks: PASS
  [neg] P-N5-GATE fix4 checks: PASS
  [neg] P-N5-GATE fix5 checks: PASS
  [neg] si (P-N5-GATE L-5 pinned): PASS
  [neg] BOX96 checks: PASS
  [b99] tools/blocks99_104.sh (check.sh l. 1298-1309 at 7b0a58ae, boxes 99-104 that the merge brings): 2026-11-12T21:54:42Z-2026-11-12T21:54:46Z rc 0:
  [b99] BOX99 checks: PASS
  [b99] BOX100 checks: PASS
  [b99] BOX101 checks: PASS
  [b99] BOX102 checks: PASS
  [b99] BOX103 checks: PASS
  [b99] BOX104 checks: PASS
  [data] OK   2*mx_ch_D+1 == mx_flips (own): [9, 17, 33] (expected [9, 17, 33])
  [data] OK   2*mx_ch_D+1 == mx_flips (g3): [9, 17, 33] (expected [9, 17, 33])
  [data] OK   F_10 - 1, F_18 - 1 (F_1 = F_2 = 1): [54, 2583] (expected [54, 2583])
  [data] OK   L-5 contains «re-arm multiplicity m 8 / 32 with C 17 / 65 on MW8…»: 1 (expected 1)
  [data] OK   L-5 contains «the RA path count P 54 / 2583 (= F_(d+2) − 1 at d …»: 1 (expected 1)
  [data] OK   L-5 contains «claude/l-si 2d0344d3 and 4ded1e8d, box90/out/mw90.…»: 1 (expected 1)
  [data] OK   L-5 contains «C 17 / 65 and the largest per-gate flip count 34 /…»: 1 (expected 1)
  [data] OK   L-5 contains «per-gate flips 9 / 17 / 33 = 2·ch_D + 1 (ch_D 4 / …»: 1 (expected 1)
  [data] OK   L-5 contains «box91/out/own91.out and g391.out C and maxflip, bo…»: 1 (expected 1)
  [data] OK   L-5 count «m = n»: 0 (expected 0)
  [data] OK   L-5 count «linear in n»: 0 (expected 0)
  [data] OK   L-5 count «on every family measured»: 0 (expected 0)
  [data] OK   L-5 count «A*_all and the largest»: 0 (expected 0)
  [data] OK   L-5 count «2n + 1»: 0 (expected 0)
  [data] OK   L-5 count «4n + 2»: 0 (expected 0)
  [data] OK   git log 7b0a58ae -- experiments/si/box90/out/mw90.out: ['2d0344d3'] (expected ['2d0344d3'])
  [data] OK   git log 7b0a58ae -- experiments/si/box90/out/fw90.out: ['4ded1e8d'] (expected ['4ded1e8d'])
  [data] OK   changed paths in box90-box96 676b6a1c..7b0a58ae: ['experiments/si/box95/check95.sh', 'experiments/si/box95/fix5/check_fix5.sh', 'experiments/si/box95/fix5/chk_C142_269effb3.md', 'experiments/si/box95/fix5/fix5.sha1', 'experiments/si/box95/fix5/mkL5.py', 'experiments/si/box95/fix5/mkfix5.py'] (expected ['experiments/si/box95/check95.sh', 'experiments/si/box95/fix5/check_fix5.sh', 'experiments/si/box95/fix5/chk_C142_269effb3.md', 'experiments/si/box95/fix5/fix5.sha1', 'experiments/si/box95/fix5/mkL5.py', 'experiments/si/box95/fix5/mkfix5.py'])
  [data] OK   changed paths docs/si/P-N5-GATE* 676b6a1c..7b0a58ae (packet and L-1..L-4 unchanged): ['docs/si/P-N5-GATE-fixes.md', 'docs/si/P-N5-GATE-line-L5.txt'] (expected ['docs/si/P-N5-GATE-fixes.md', 'docs/si/P-N5-GATE-line-L5.txt'])
  [data] OK   lane mkL5.py (archive of 7b0a58ae) rc: 0 (expected 0)
  [data] OK   lane mkL5.py output == L-5: True (expected True)
  [data] OK   lane mkL5.py --nine sha1: 7ebcf7355be9838473f05a7defe913940b6fd723 (expected 7ebcf7355be9838473f05a7defe913940b6fd723)
  [data] 48 checks OK, DATA EQUAL
  [data] FAIL NEGATIVE CONTROL: maxflip MW32_2 own claimed 131: 130 (expected 131)
  [data] NEGATIVE CONTROL caught (131 != 130)
  [prem] RESULTS @f9520557: 16769 lines; headings R104 9864, R117 13362, R118 13607, R121 14320, R123 15076, R125 15595, R126 15726, R127 15903; E-1 l. 16127
  [prem] (1) L-5 has 9 «…» quotes; the first 8 are premise quotes (in the premise parenthesis, before «, with Ω_t»), the 9th is the packet's own proviso:
  [prem]     premise quotes not found in their named entry: 0
  [prem] (2) names L-5 cites «RESULTS R125 (P-N5-CHAIN): …»: 11 ['F1', 'F3', 'F4′', 'F6', 'STRICT', 'CN2-3', 'LOC-GATE3', 'NO-TIE3', 'LOC-K2-3', 'B-ONLY3', 'E-MON3']
  [prem] (3) R118 (l. 13607-13878): «(b) Facts F1-F6» l. [13682]; «F4′» in block 11; «(c)» item «STRICT» in block 19; «(e)» l. [13691]; «(k)» l. [13704]; title «IDEAL-CYC(G)» 1
  [prem] (4) LT-1: R127 title (l. 15903) «(Corollary SPLIT-COUNT)» 1, «(Corollary C-EQUIV)» 1, source «(P-N5-SPLIT, docs/new/P-N5-SPLIT.md, frozen at l-new 399cda07, sha1 5bc1b1f3» 1; R126 title (l. 15726) source «(P-N5-QN, docs/new/P-N5-QN.md» 1; R127 the last ### R heading: True
  [prem] (5) P-N5-CHAIN.md @93531b03 sha1 6e613ba762b6ecf67247ef6d8674b4c960013039 (6e613ba7: True); ancestor of f9520557: True; byte-equal at f9520557: True
  [prem] (6) RESULTS R-ids L-5 cites: [104, 117, 118, 121, 123, 125, 127] (all landed and ≤ 127: True); every «R<n>» token: ['R104', 'R117', 'R118', 'R121', 'R123', 'R125', 'R126', 'R127', 'R2', 'R221', 'R229']; «R126» only in « sha1 5bc1b1f3; landing order R126 = P-N5-QN, R127»
  [prem] (7) 8-hex tokens in L-5: ['2d0344d3', '399cda07', '406ef2fd', '4ded1e8d', '5bc1b1f3', '6e613ba7', '93531b03', 'fa4e50fe']
  [prem] negative controls (prem128b.out, lines with NEGATIVE CONTROL, not reprinted: their made-up strings would read as quotes): 3 lines, each a made-up string found 0 times or None
  [merge] == git log --oneline 676b6a1c..7b0a58ae
  [merge] 7b0a58ae L-SI P-N5-GATE (R128) fixes entry 5 + line L-5 by script: CHECKER C142's E-1, E-2, E-3 and the Lead's tenth pair
  [merge] a9ea60b9 L-SI box 101 Addendum F: REFEREE 32's replacement for RESTRICT-C (iv), byte copy from claude/referee ff9b16f6; notebook
  [merge] 925577fe L-SI duty (b): box 209's must-0 counters replayed on the lane's 26 frozen instances under L-RED 65's HOW3 engine (box 103 Addendum B)
  [merge] 01900837 L-SI box 104 Addendum A: long rows of the wrapped games (n = 7, 8; two engines at n = 5); two probes of N5 (guided wrapper; free genomes)
  [merge] 26704e01 L-SI box 104 FREEZE (D18 big map): Lemma WRAP, FREE-REACH, Friedmann's counter under N5'-xi; map of open links for N5
  [merge] 659a2d09 L-SI successor 52: handover check (five questions), measured at bce4f398 / trunk a9699c30
  [merge] bce4f398 L-SI successor 51: box 101 Add. E (REFEREE 32 pre-read of RESTRICT-C: (iv) replaced by BR-SEG form, W-2, C-1, N-1) + box 103 Add. A (box 208 comparison) + handover
  [merge] b2520ec7 L-SI box 103: MOVER-DEEP3 at k = 1; Lemma GAIN-COUNT (PROVED lane); MOVER-DEEP3 <= CONJECTURE NOLOSS; NOLOSS-k1 data 0 at k = 1; DEAD e-depth <= 1 at k = 1 (WC16_2)
  [merge] d8945c4a L-SI box 101 Add. D (Lemma RESTRICT-C, route B'; three routes; section 1 wording) + box 102 Add. A (DEEP3 vs DEEP3-all) + Add. B (G_N passes the chain; E-MON3 via E-DOM is the step a DEEP3 proof must use; CORE-ABOVE credited to landed R121 (b))
  [merge] 2d2f9a0e L-SI box 101 Addendum C: landed R118 (BR-SEG, BR-SEG-G, Corollary T3) covers WINDOW + LAM-GAP's role; Theorem R-SPLIT (R <= poly + Deep^G_c), chain shortened to CONJECTURE DEEP3-G; Hansen's conjecture claimed refuted by Zhong-Ye (unrefereed)
  [merge] 144f6821 L-SI box 102 (DEEP3 proof side: CORE-ABOVE, PROPAGATE, DEEP3 <= MOVER-DEEP3; exact Deep3 census) + box 100 Add. A (L-RED 66 gaps D1, W1 fixed) + box 101 Add. B (SHARP, statuses)
  [merge] 4fda7245 L-SI box 101 Addendum A: the chain to a polynomial T3 (table: status, attacks, landed premises) and its scope in TARGET.md terms; conditional on CONJECTURE DEEP3
  [merge] 23d39400 L-SI box 101: Lemma LAM-GAP PROVED (lane; one-player Howard window with constant Lambda <= ¦Ch¦ + 1); L1-POLY; SCC-LIN poly form <= DEEP3 alone; step 0 literature (Hansen's conjecture open, VJ case narrower)
  [merge] 3b6ae726 L-SI box 100: TWO-CROSS, DEPTH-COUNT3, Theorem WINDOW (PROVED lane); SCC-LIN (poly form) <= LAM-GAP + DEEP3 (conjectures, data); FLIP-LOUD DEAD (MWR4_2 gate (34,0)); MWR = fuse + one re-arm gate (k = 1)
  [merge] 8a884bb2 L-SI box 100 tools: trace100 / iv100 (interval decomposition) / cross100 (TWO-CROSS + depth counters, control) / l1probe100; census on 26 + 400: unm/sumf/minf/tie 0, control fires; check100 wired
  [merge] 9bb7bd43 L-SI box 99 Addendum A: GAP G1 fixed (H(C) maximised over all HOW3-legal tie resolutions, starts and final exits; per L-RED 65 R232 59daaef2)
  [merge] 53c72ec3 L-SI successor 51: handover check
  [merge] f65e0fb9 L-SI box 99: Lemma SCC-RED (T3 ≤ chain sum of per-SCC Howard lengths), Lemma CAP; CONJECTURE SCC-LIN (⇒ U-FREE); scc99 census locfail 0 / chainfail 0 on 26 frozen + 600 random
  [merge] 9a490206 L-SI successor 50: handover (P-N5-GATE L-4 with both referees; BONLY3 withdrawn; box 99 in flight) + box 99 tools (scc99 SCC census)
  [merge] count 19
  [merge] trunk 85e42158 merge-base 547985a1 ; commits 547985a10fad4739611ba46aeaebaec3dc9899ab..7b0a58ae: 57 ; 676b6a1c ancestor of 7b0a58ae: yes ; 7b0a58ae ancestor of trunk: no
  [merge] old-style merge-tree rc 0 ; lines 36032 ; conflict markers 0
  [merge] trunk 21b87e70 merge-base 547985a1 ; commits 547985a10fad4739611ba46aeaebaec3dc9899ab..7b0a58ae: 57 ; 676b6a1c ancestor of 7b0a58ae: yes ; 7b0a58ae ancestor of trunk: no
  [merge] old-style merge-tree rc 0 ; lines 36032 ; conflict markers 0
  [merge] referee commits ancestors of 85e42158:
  [merge] 16e8dcb0 no
  [merge] 0df0fdd8 no
  [merge] 49d34123 yes
  [merge] 3282fc6c yes
  [merge] C142 269effb3 ancestor of 85e42158: no
  [merge] bfee3e33a6f4e82e760e5e7429769a6f72d90f49  -
  [chk] model: landed R127 title (f9520557) == «### R127 [refereed-only] » + R127 L-3 + «, CHECKER PASS (docs/checker/C141.md, checker 850e9765)»: True
  [chk] file: sha1 329025d7c78be8417ddb668d585bd3774498c324 bytes 102951 lines 607 ends with newline True
  [chk] ### R headings at d[...]: [282]
  [chk] (a) title == prefix + L-5 (no newline) + tail: True ; middle bytes == L-5 bytes without newline: True
  [chk]     title: 12728 chars, 13001 bytes, sha1 00b8bd9f126b49b86538479e0791abd7490b4494, ( 239 ) 239, min depth 0, final 0, ¦ 0, fill token 1
  [chk] (e) entry block d[282:522] (lines 283-522, 240 lines, sha1 of the joined block a253dbdcd7a5046d8de45c419f818ff45a2ddaff, with a final newline 805b82da7ea797602a5912b8ce490c9791febb84); next line blank: True; line after: 'Proposed GAPS line-11 UPDATE (append-onl'
  [chk] (b) fill token in the entry block: 1 ; in the whole file: 1 at lines [283]
  [chk]     «\n**Erratum E-1** (not a result» in the block: False ; line-start «**Erratum» in the file: 0 ; empty lines inside the block: 0
  [chk] (e) UPDATE line(s) at d[...]: [545] (line [546])
  [chk]     lines starting «UPDATE » in the file: [546]
  [chk]     GAPS preamble at d[523:545]
  [chk] (c) "¦" in entry block: 0 ; in UPDATE: 0 ; in GAPS preamble: 1 (the quoted « ¦» of the row end); in the file: 11
  [chk] (d) UPDATE <DATE> 1 <HH:MM> 1 <checker> 1; head at its start: True
  [chk]     UPDATE = upd128L5.txt: True ; sha1 (no newline) ba6958119e92cc3ab00cee0348fc69a9e51441b3 ; with newline 221f1c5b7c819d244f2e23a988ca1b32d02ac141 ; 12962 bytes ( 238 ) 238
  [chk]     stale grep, entry block minus title (case-insensitive): {}
  [chk]     stale grep, title: {'pending': 1} ; UPDATE: {}
  [chk]     stale objects in the entry block: «L-4» 19, «6bfde78e» 2, «fixes entries 1-4» 2, «12,562» 1, «47a09c22» 1 (each in L-4 history text only; listed in Addendum (second fill))
  [chk]     line 1 «NOT LANDED» 1 ; «<DATE>» in file 5 ; «<checker>» 6 ; «<HH:MM>» 5
  [chk] (e) slices: line 1 d[0]; FIRST FILL record d[1:281] (flags d[126:281]; + blank d[281]: ''); title d[282]; entry d[282:522]; blank d[522]; preamble d[523:545]; UPDATE d[545]; blank d[546]: ''; first-fill Addendum d[547:607]; Addendum (second fill) none
  [chk] (g) vs first fill 70db12a9: line 1 equal True; record d[1:126] (up to and incl. «FLAGS FIRST») equal True; title changed True; first-fill Addendum d[547:607] == first fill d[464:524] True; blank before it True
  [chk] (h) flag bullets: first fill 15, second fill 16; first 15 unwrapped bullets are prefixes of the new ones: True; the extra bullet starts 'C142 (claude/checker 269effb3, FAIL), second fill: E-1, E-2 '
  [chk] (f) QUOTE SWEEP (corpus: 193 texts)
  [chk]     sweep line 1: 1 quotes, 1 parts, 0 not found []
  [chk]     sweep FIRST FILL record up to FLAGS FIRST: 52 quotes, 44 parts, 0 not found []
  [chk]     sweep flag list (with C142 rulings): 178 quotes, 164 parts, 0 not found []
  [chk]     sweep entry block: 154 quotes, 172 parts, 0 not found []
  [chk]     sweep GAPS preamble + UPDATE: 35 quotes, 31 parts, 0 not found []
  [chk]     sweep first-fill Addendum: 16 quotes, 11 parts, 0 not found []
  [chk]     sweep whole file: 436 quotes, 423 parts, 0 not found []
  [chk]     sweep NEGATIVE CONTROL: 1 quotes, 1 parts, 1 not found ['GATE-RACE bounds every gate by two flips on every genome']
  [chk]     negative control reported missing: True
  [lp] first-fill cites 133, second-fill cites 36; first-fill shown quotes no longer in the draft (dropped): 0 []
  [lp] cites 169 (120 shown in the draft as «quote», 49 used for a line number only) in 21 (commit, file) pairs; failed at the cited lines: 0 []
  [lp] shown quotes not in the draft as «quote»: 0 []
  [lp] NEGATIVE CONTROL 1 (window shifted by 40 lines): 0 of 169 still pass []
  [lp] NEGATIVE CONTROL 2 (longest word mutated): 0 of 169 still pass
  [lp]     0df0fdd8 docs/referee-2/R2-P-N5-GATE.md 12
  [lp]     16e8dcb0 docs/referee/R-P-N5-GATE.md 5
  [lp]     269effb3 docs/checker/C142.md 13
  [lp]     3282fc6c docs/referee-2/R2-P-N5-GATE.md 2
  [lp]     4066f579 docs/si/P-N5-GATE.md 12
  [lp]     41228433 docs/referee/R-P-N5-GATE.md 3
  [lp]     49d34123 docs/referee/R-P-N5-GATE.md 7
  [lp]     6269fec5 docs/referee-2/R2-P-N5-GATE.md 3
  [lp]     676b6a1c docs/si/P-N5-GATE-fixes.md 10
  [lp]     676b6a1c docs/si/P-N5-GATE-line-L4.txt 1
  [lp]     731db590 docs/referee/R-P-N5-GATE.md 3
  [lp]     7b0a58ae docs/si/P-N5-GATE-fixes.md 6
  [lp]     8983b3d8 docs/referee-2/R2-P-N5-GATE.md 8
  [lp]     93413fc6 docs/referee-2/R2-P-N5-GATE.md 8
  [lp]     a28bc5e1 docs/referee-2/R2-P-N5-GATE.md 3
  [lp]     a401ce0e docs/referee/R-P-N5-GATE.md 41
  [lp]     c035b35f docs/referee-2/R2-P-N5-GATE.md 26
  [lp]     f9520557 TARGET.md 1
  [lp]     f9520557 docs/DECISIONS.md 1
  [lp]     f9520557 docs/agents/LEAD-STATE.md 3
  [lp]     fbc4d865 docs/referee/R-P-N5-GATE.md 1
  [hex] hex ids in the draft: 135; git objects 83; measured sha1s (not objects) 52; neither: 0 []
  [hex] NEGATIVE CONTROL (0badc0de1, 1234abcd9f): neither: 2 ['0badc0de1', '1234abcd9f']
  [sim] trunk f9520557 RESULTS sha1 4117c8a7d0165cd8d3a880f9a405d9c6fc6a5089 lines 16769 "¦" 1477 ; GAPS sha1 ccf059a1558fc3e1ae769a7aa98506f5fa7d64d5 lines 23
  [sim] pure insertion: prefix byte-unchanged True ; suffix byte-unchanged True ; inserted lines 241
  [sim] headings after insertion: {'R126': [15726], 'R127': [15903], 'R128': [16127], 'E-1': [16368], 'E-2': [16381], 'E-3': [16409], 'Dead': [16440]}
  [sim] R127 at l. 15903 (unchanged: True); R128 at l. 16127-16366, blank l. 16367 (''), «**Erratum E-1**» l. 16368; the line before R128: l. 16126 '' (R127's block ends l. 16125)
  [sim] order R126 < R127 < R128 < E-1 < E-2 < E-3 < Dead ends: True
  [sim] RESULTS lines 16769 -> 17010 (+241) ; "¦" 1477 -> 1477 (unchanged True) ; «checker 3333333)» once True ; fill token 0
  [sim] ### R1xx headings: 29, R128 the last: True
  [sim] GAPS: only l. 11 changes True ; lines 23 -> 23 ; l. 11 "¦" 76 -> 76 ; «UPDATE 2026-» 62 -> 62 ; R128 last: True ; after R127's (2026-11-12 13:58Z, 850e9765): True ; prefix byte-unchanged: True
  [sim] GAPS whole file "¦" 198 -> 198
  [sim] fill values used only here: 2099-01-11 00:00 3333333
  [sim85] trunk 85e42158 RESULTS sha1 4117c8a7d0165cd8d3a880f9a405d9c6fc6a5089 lines 16769 "¦" 1477 ; GAPS sha1 ccf059a1558fc3e1ae769a7aa98506f5fa7d64d5 lines 23
  [sim85] pure insertion: prefix byte-unchanged True ; suffix byte-unchanged True ; inserted lines 241
  [sim85] headings after insertion: {'R126': [15726], 'R127': [15903], 'R128': [16127], 'E-1': [16368], 'E-2': [16381], 'E-3': [16409], 'Dead': [16440]}
  [sim85] R127 at l. 15903 (unchanged: True); R128 at l. 16127-16366, blank l. 16367 (''), «**Erratum E-1**» l. 16368; the line before R128: l. 16126 '' (R127's block ends l. 16125)
  [sim85] order R126 < R127 < R128 < E-1 < E-2 < E-3 < Dead ends: True
  [sim85] RESULTS lines 16769 -> 17010 (+241) ; "¦" 1477 -> 1477 (unchanged True) ; «checker 3333333)» once True ; fill token 0
  [sim85] ### R1xx headings: 29, R128 the last: True
  [sim85] GAPS: only l. 11 changes True ; lines 23 -> 23 ; l. 11 "¦" 76 -> 76 ; «UPDATE 2026-» 62 -> 62 ; R128 last: True ; after R127's (2026-11-12 13:58Z, 850e9765): True ; prefix byte-unchanged: True
  [sim85] GAPS whole file "¦" 198 -> 198
  [sim85] fill values used only here: 2099-01-11 00:00 3333333
