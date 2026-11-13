# Draft RESULTS R130 (Lead; first fill 2026-11-13T02:11:30Z by date -u (subagent) on P-N5-WRAP line L-2, docs/si/P-N5-WRAP-line-L2.txt, l-si faf0c8ff, sha1 dbd5f0e83e3d0300842c46cf2ae24b30b853d784) — to CHECKER C146 (number from the Lead's brief, G-0) — NOT LANDED; goes after R129 (NOT YET LANDED: its second-fill draft docs/agents/R129-draft.md at trunk 4af9279d, sha1 7db9c72d…, to CHECKER C144) and R128 (NOT YET LANDED: its third-fill draft docs/agents/R128-draft.md at trunk 4af9279d, sha1 3f64fcd9…, at CHECKER C142), directly before the line-start «**Erratum E-1** (not a result» (l. 16127 at 4af9279d, before R128 and R129 land); its GAPS UPDATE after R129's on GAPS l. 11
FIRST FILL (this text). Built by script (r130a/fill130a.py; checks r130a/tools/*.py, *.sh; Addendum by r130a/mkadd130a.py) in the scratchpad
  r130a/ for the Lead to copy to docs/agents/R130-draft.md; nothing in the repository was edited, committed, merged or pushed by me, and
  scripts/push.sh and scripts/verify.sh were not run (read-only git, git archive, git ls-remote and the old-style read-only git merge-tree
  only; experiments/si/check.sh run in the archive with the repository's object store visible read-only (GIT_DIR); git status clean). Read
  at the origin heads of two git fetches, the first at the start of the fill (r130a/fetch.txt): Fri Nov 13 02:07:12 UTC 2026 rc 0 l-si
  faf0c8ff87aad0bda8441f3b9b3f7f53e8775755 referee 28b951515c1696557a8713fde8b790c5d9127fb1 referee-2
  01e83df53909f6852c1238bad7bb00a4f70275ae l-red 3732f4a1db018c02983745496ad7011e6f02b9a8 l-comp c1c0a4293e4538716243768804dee37ebb7456ac
  checker 37fcbd2175629c9002a483837f1cbd3681b910f6 vibrant-johnson-nxvvxo e8b6abf0170fb63ecbd68d058a2bb38599bc5b01 HEAD
  4af9279d8c5e24454851fbace70e993299f6d68e ls-remote referee 28b951515c1696557a8713fde8b790c5d9127fb1 refs/heads/claude/referee ls-remote
  referee-2 01e83df53909f6852c1238bad7bb00a4f70275ae refs/heads/claude/referee-2 ls-remote l-si faf0c8ff87aad0bda8441f3b9b3f7f53e8775755
  refs/heads/claude/l-si (tabs of the ls-remote lines printed as spaces); the second after the Lead's 02:36Z message that REFEREE 34's §8 on
  P-N5-WRAP is on origin (r130a/fetch2.txt): Fri Nov 13 02:36:36 UTC 2026 rc 0 l-si 18cd2b88c98b2d7bf75b4f61941ee8c00ce6b19b referee
  32d61d6064ff48b23d4cec26972ae6d116653f2b referee-2 0f2606da4f44254a17fc5c2dfd9edd46aa8bdddd vibrant-johnson-nxvvxo
  e8b6abf0170fb63ecbd68d058a2bb38599bc5b01 HEAD 4af9279d8c5e24454851fbace70e993299f6d68e ls-remote 18cd2b88c98b2d7bf75b4f61941ee8c00ce6b19b
  refs/heads/claude/l-si ls-remote 32d61d6064ff48b23d4cec26972ae6d116653f2b refs/heads/claude/referee ls-remote
  0f2606da4f44254a17fc5c2dfd9edd46aa8bdddd refs/heads/claude/referee-2. Between them only claude/referee (28b95151 → 32d61d60: R-P-N5-WRAP
  §8 and its replay log), claude/referee-2 (01e83df5 → 0f2606da: notes/REFEREE-2.md only) and claude/l-si (faf0c8ff → 18cd2b88:
  docs/agents/handover-checks/L-SI.md only) moved (asserted); the packet, L-1, L-2 and the fixes file are byte-equal at 18cd2b88.
TRUNK: local HEAD 4af9279d (4af9279d8c5e24454851fbace70e993299f6d68e, 2026-11-13T02:05:23Z, «Lead: R129 second fill (P-N5-LEVEL over L-2
  d18125ed; REFERE …»), one commit ahead of origin/claude/vibrant-johnson-nxvvxo e8b6abf0 at the fetch (that commit adds
  docs/agents/R129-draft.md, the R129 second fill, and edits docs/NOW.md and docs/agents/LEAD-STATE.md; not yet on origin); docs/RESULTS.md
  and docs/GAPS.md are byte-equal at HEAD, at e8b6abf0 and at f9520557 (RESULTS sha1 4117c8a7d0165cd8d3a880f9a405d9c6fc6a5089, 16769 lines,
  last «### R» heading R127 at l. 15903, «**Erratum E-1** (not a result» l. 16127; GAPS sha1 ccf059a1…, 23 lines). R128 and R129 are NOT
  landed: R128's draft at HEAD is the third fill (sha1 3f64fcd940cbc190b4b365ec7e88e7bc8536cfac; block d[282:522], 240 lines; UPDATE d[545],
  ba695811…), R129's is the second fill (sha1 7db9c72d5aef9a40e938b8cd502ca2a23d22f6d1; block d[153:303], 150 lines; UPDATE d[319],
  31d7b642…); both are this fill's base (b).
LINE OF RECORD: docs/si/P-N5-WRAP-line-L2.txt, COMMIT faf0c8ff (faf0c8ff87aad0bda8441f3b9b3f7f53e8775755, 2026-11-13T00:29:35Z, «L-SI
  P-N5-WRAP fixes entry 1 + line L-2 by script (REFEREE 34 LW-1 (check stage be7da8f3), REFEREE-2 39 R-1, R-2 on LW-1's clause; adopted
  LW-2, LW-3; note N-1); checkW.sh pins; notebook»), the file's only commit and the l-si head; FILE sha1
  dbd5f0e83e3d0300842c46cf2ae24b30b853d784 (blob 299dafceb64587263b1492e5ef291d3bdf371ba7), 3,598 bytes, one line with its newline, 44 «(» =
  44 «)», 6 «|» (in «|V_E|» and twice «|V|»), no « — », no date parenthesis, no «…» quote, ending «).» before the newline. L-1:
  docs/si/P-N5-WRAP-line-L1.txt at e01447e7, sha1 896f9e97394695f903131f832a67f31bcfc23c28, 2,648 bytes (frozen with the packet). Builder
  experiments/si/pwrap/fix1/mkL2.py (re-run by me in a git archive of faf0c8ff, mk.out: check stage be7da8f3 True, L-2 cmp EQUAL, output
  equal to the committed mkL2.out).
PACKET: docs/si/P-N5-WRAP.md FROZEN at e01447e7 (e01447e77d57e2cdd26b7e537546c35c49b26fc8, 2026-11-12T21:08:48Z, «L-SI packet P-N5-WRAP
  FROZEN (dead-end packet for N5'-xi: Lemma WRAP proved on W in full incl. core and endgame lemmas; …»), the file's only commit; sha1
  1670432a8a07490ff80ceed45c861515ff070b9b, 462 lines, 56,745 bytes; byte-equal at faf0c8ff (the l-si head). FIXES:
  docs/si/P-N5-WRAP-fixes.md, one commit faf0c8ff, entry 1 only, 29 lines, 3,414 bytes, sha1 9fff274d4e527c42b64f47ded6b3f2627a344c32,
  line-only («Nothing in the packet's statements changes; both referees SIGN them; XI-EXP stays CONDITIONAL as signed» (l. 28)).
REFEREES (git blame at the heads). REFEREE docs/referee/R-P-N5-WRAP.md at claude/referee 32d61d60 (246 lines; REFEREE successor 34; 98cdc7aa
  and 28b95151 change only R-P-N5-LEVEL.md and its scratch test files): l. 1-125 §1-§2 ef4d3bd1 (2026-11-12T22:31:53Z), l. 126-190 §3-§7
  c6fcf2b6 (2026-11-12T22:31:53Z), l. 191-217 §0 verdicts 99df2458 (2026-11-12T22:31:53Z), l. 218-246 §8 (L-2 byte test) 32d61d60
  (2026-11-13T01:40:40Z). REFEREE-2 docs/referee-2/R2-P-N5-WRAP.md at claude/referee-2 0f2606da = at 01e83df5 (309 lines; REFEREE-2
  successor 39): l. 1-171 boxes 1-2 3cf594cc (2026-11-12T22:08:25Z), l. 172-275 box 3, verdict and statement of independence 07fd5ae4
  (2026-11-12T22:09:50Z), l. 276-281 Addendum 1 5d30968a (2026-11-12T22:34:35Z), l. 282-309 Addendum 2 01e83df5 (2026-11-13T01:28:18Z).
ON L-2: both referees MATCH it. REFEREE-2 39 Addendum 2 (01e83df5) «L-2 (faf0c8ff, sha1 dbd5f0e8) MATCHES. R-1 and R-2 are met; my SIGN WITH
  GAP on L-1 is closed. Note W-L2-1 is optional.» (l. 309). REFEREE 34 §8 (32d61d60, 2026-11-13T01:40:40Z, «REFEREE s34: R-P-N5-WRAP §8:
  fixes entry 1 CORRECT, line L-2 MATCHES (dbd5f0e8 = L-1 + LW-1 (be7da8f3) + REFER …») «Verdict: **Line L-2 MATCHES** (L-1 + exactly LW-1,
  R-1, R-2 as applied to LW-1's clause, LW-2, LW-3; sha1 dbd5f0e8…). Statements and labels as in §0: every statement SIGN; XI-EXP
  CONDITIONAL as signed.» (l. 245-246). At my first fetch (02:07Z) origin/claude/referee was 28b95151 and §8 was absent; the Lead's state
  log had recorded it as «push running» («REFEREE 34 CORRECTION: R-P-N5-WRAP §8 commit is 32d61d60 (not 4e2fd393, which does not exist; SHA
  quoted in parallel with commit = slip, logged).» (l. 3434)); at the second fetch (02:36Z) it is on origin (flag G-R8, resolved).
SOURCES READ: the packet in full where cited (header, Scope, To sign, §1, §2.4, §3, §5-§13 in full; §2.1-§2.3 and §4 by heading); the fixes
  file in full; L-1, L-2 in full; mkL2.py, mkL2.out, fix1/SHA1SUMS; experiments/si/pwrap/checkW.sh and box104/check104.sh at faf0c8ff; the
  box104 frozen outputs by column name (data130a.py); REFEREE's report in full (at 32d61d60, with §8); REFEREE-2's report in full (at
  0f2606da = 01e83df5); REFEREE 33's R-WRAP-preread (90703a81) and f11_H_fig4.out (e44ce56b) for the numbers L-2 cites; notes/L-SI.md at
  faf0c8ff l. 155-161 and 3469-3475 (sources opened); RESULTS at HEAD: R15 l. 624, R24 l. 1064, R57 l. 2893, R103 l. 9641, R104 l. 9864,
  R118 l. 13607 (prem130a.py); GAPS l. 11; TARGET.md; DECISIONS L41, L43; the Lead state log l. 3426-3440; the R128 and R129 drafts at HEAD
  (models) and the scripts of r129a/, r129b/ (adapted).
CHECKS RUN AT THIS FILL (scratch r130a/; outputs there; verbatim in the Addendum). (a) blocks.out: experiments/si/check.sh l. 1309 «bash
  box104/check104.sh» and l. 1313 «bash pwrap/checkW.sh» at faf0c8ff (tools/blocksWRAP.sh) in a FULL git archive of faf0c8ff (r130a/arch,
  48,881 files = the tree), rc 0, «BOX104 checks: PASS», «PWRAP checks: PASS»; neg.out: one byte appended to the archive's L-2 → «PWRAP FAIL
  fixes entry 1 sha1», rc 1; one byte prepended to box104/out/wrap_long.out (a pinned output) → «BOX104 FAIL …» and «PWRAP FAIL W^L_7 long»,
  rc 1; both restored (cmp equal) and re-run rc 0; sicheck.out: the whole experiments/si/check.sh in the archive (the gate the l-si merge
  brings; see the Addendum for its rc). (b) mk.out: the lane's mkL2.py in the archive: check stage be7da8f3 True, L-2 cmp EQUAL. (c)
  upd130a.py: the UPDATE by upd129b.py's builder adapted (direct3, flag G-U), controls R125, R126, R127 (landed), R128 (draft, ba695811) and
  R129 (draft, 31d7b642), four negative controls. (d) prem130a.py: premise R-ids and items at HEAD. (e) data130a.py: DATA clauses and
  numbers (25 checks OK, «DATA EQUAL»; negative control caught). (f) merge130a.sh: the merge list (re-run after the second fetch). (g)
  chk130a.py (title, block, UPDATE, tokens, pipes, anchors, stale grep, quote sweep per section with a negative control), lp130a.py (every
  quote at its commit, file and lines; two negative controls), note130a.py (the Lead's Note bullet: N-W2 and W-L2-1 extracted by script from
  the reports at 32d61d60 and 01e83df5), sim130a.py (landing simulation on bases (a) and (b)).
FLAGS FIRST (my reading; CHECKER rules; blocking ones first; strings below are PROPOSALS only; nothing in L-2 or in any quoted line was
  changed).
- G-R8, REFEREE'S L-2 BYTE TEST: ON ORIGIN SINCE THIS FILL (note; was BLOCKING at my first fetch; RESOLVED). At Fri Nov 13 02:07:12 UTC 2026
  origin/claude/referee was 28b95151 and R-P-N5-WRAP.md ended with §0 (l. 217); at Fri Nov 13 02:36:36 UTC 2026 (the Lead's 02:36Z message)
  it is 32d61d60 (git ls-remote agrees), a descendant of 28b95151, adding §8 (l. 218-246) and its replay log only. The entry quotes §8 by
  script at 32d61d60 (The RESULTS line, Claims signed, Note, Signatures, INDEPENDENCE): «Result: sha1
  **dbd5f0e83e3d0300842c46cf2ae24b30b853d784**, 3,598 B, one line, 44 «(» = 44 «)»; `cmp` with the lane's L-2: **EQUAL**. Nothing else
  changed.» (l. 231-232) and «Verdict: **Line L-2 MATCHES** (L-1 + exactly LW-1, R-1, R-2 as applied to LW-1's clause, LW-2, LW-3; sha1
  dbd5f0e8…). Statements and labels as in §0: every statement SIGN; XI-EXP CONDITIONAL as signed.» (l. 245-246); the stale grep finds no
  «pending» in the entry block below the title. 32d61d60 is in the merge list.
- G-NW2, THE LEAD'S NOTE BULLET (note; RESOLVED with G-R8). Lead ruling (brief): L-2 lands verbatim, and the entry carries ONE Lead-text
  bullet "Note (both referees, no change asked): …" quoting REFEREE 34's N-W2 and REFEREE-2's W-L2-1 by script. Both are now quoted,
  extracted by script from the reports (note130a.py: N-W2 at 32d61d60 l. 239-240, W-L2-1 at 01e83df5 l. 303-307; each quoted piece asserted
  once; W-L2-1's Old string occurs once in L-2). «no change asked» is verified for both: N-W2 «Note N-W2 (no change asked)» (l. 239), W-L2-1
  «no change required for MATCH; the Lead's call» (l. 303). The bullet's own text (the runs are this lane's own, box 104, not a cited
  replay) is checked against the box 104 outputs (data130a.py, note130a.py).
- G-SHAPE, L-2'S FORM AGAINST THE LANDED TITLES (FLAG; CHECKER's call, possibly blocking under the landed form; Lead ruling: L-2 lands
  verbatim). (1) L-2 has no date parenthesis and no « — »: every landed «### R» heading R60-R127 has exactly one " (YYYY-MM-DD) — " (my scan
  of RESULTS at HEAD; also the R129 L-2 and the R128 L-5). (2) L-2 ends «…; L-SI successor 53).» with a period, so the title reads "….).,
  CHECKER PASS (docs/checker/C146.md, …)"; landed headings with "., CHECKER PASS": 0 of 127. (3) L-2 opens «DEAD-END packet for the
  candidate N5′-xi …, CONDITIONAL until two referees sign:», a packet description rather than the statement form «In …, … :» of R118-R129;
  both referees matched it as a line (REFEREE §5 on L-1's clauses, REFEREE-2 Add. 2 on L-2). (4) L-2 carries 6 «|»: «6 «|» (in |V|, |V_E|;
  35 landed RESULTS headings carry «|», e.g. R96-R101 «n := |V|», so no shape issue)» (l. 14-15); the title keeps them; the UPDATE replaces
  them by words (G-U). Proposed: none (Lead ruling); if CHECKER requires the landed form, that is a line change (fixes entry 2 and a byte
  test by both referees). SECOND FILL: Lead reading (03:05Z): L-2 lands VERBATIM; both referees byte-tested it, the form difference costs
  nothing in meaning, and a fixes entry 2 would cost a full byte-test round. NOTE FOR CHECKER: the title is L-2 verbatim with no date
  parenthesis and no " — ", ends ").", followed by ", CHECKER PASS (…)", and carries L-2's 6 pipe characters; this is the Lead's ruled form,
  not a drafting slip. scripts/check_docs.py (verify.sh's «doc shape» step) on the simulated landed trunk (r130b/tools/docs130b.sh: a git
  archive of HEAD 626da53c with docs/RESULTS.md and docs/GAPS.md replaced by base (b) of sim130b.py, HEAD + R128 + R129 + R130): rc 0, no
  violation; base (a): rc 0; HEAD as is: rc 0; negative control (the R130 title without «[refereed-only]»): rc 1 with «RESULTS entry not
  labelled formalized|refereed-only: ### R130 DEAD-END packet …» (Addendum (second fill), [docs]). check_docs.py reads the title only for
  its label, and GAPS l. 11 only for its first four cells. So G-SHAPE is a note only.
- G-U, THE UPDATE (FLAG: three mechanical generalisations of the landed procedure, one of them a wording reading). Built from L-2 by
  upd130a.py = upd129b.py's direct(), direct2() and controls copied unchanged, plus direct3() = direct() with: (i) a boundary in place of "
  (DATE) — ": the claim part ends before «; obstruction W-FLAT (», whose «; » is consumed as " (DATE) — " is, so the obstruction, the frozen
  instances, the DATA and «N5 (SPEC) is not affected» form the tail after «: »; (ii) the final «.» of L-2 is stripped before the source
  parenthesis is located; (iii) the three pipe-bearing strings are replaced by words, each asserted once: «(F ≤ m_E − |V_E| + 1 under
  [RULE])» → «(F ≤ m_E − (the number of Even vertices of H) + 1 under [RULE])», «so 2^Ω(√|V|):» → «so 2^Ω(√(the number of vertices)):», «,
  |V| = 10.5n² + 152.5n + 48» → «, the number of vertices = 10.5n² + 152.5n + 48» (landed precedent: RESULTS R96's UPDATE, CHECKER C106 (c)
  «r1 («|V|,» → «the number of vertices,»)», l. 66; GAPS l. 11 is a table row: 76 «|» at HEAD, and every RESULTS UPDATE on it from R88 on
  carries none, the row's closing « |» aside). With (" (DATE) — ", "") as boundary, no period and no pairs, direct3 rebuilds R129's draft
  UPDATE byte-equal (control (4c)). Drops: «; G-N5-TIME stays OPEN» (the landed drop) and «; not M3 or M4, not a TARGET.md claim» (L-2's own
  scope words, each once; R128's G-U deviation is the precedent for a line-specific drop); NO other reading: the labels move behind their
  clauses with their «; » connectors, so «(Corollary NT-RUN)», which L-2 already places after its clause, is followed by «(Claim NT: …)»;
  «CONDITIONAL until two referees sign» and «(Lemma WRAP, PROVED lane)» stay (G-S). The pipe pairs are a proposal: CHECKER accepts them, or
  names other words. SECOND FILL: Accepted by the Lead (03:05Z), with the precedent RESULTS R96's UPDATE / CHECKER C106 (c) r1. The three
  replacements, old (in L-2, once each) → new (in the UPDATE, once each), for a token-by-token check: (1) «(F ≤ m_E − |V_E| + 1 under
  [RULE])» → «(F ≤ m_E − (the number of Even vertices of H) + 1 under [RULE])»: tokens «|V_E|» → «(the number of Even vertices of H)»; (2)
  «so 2^Ω(√|V|):» → «so 2^Ω(√(the number of vertices)):»: «2^Ω(√|V|):» → «2^Ω(√(the number of vertices)):»; (3) «, |V| = 10.5n² + 152.5n +
  48» → «, the number of vertices = 10.5n² + 152.5n + 48»: «|V|» → «the number of vertices». Nothing else in the UPDATE changes words; its
  other differences from L-2 are the landed procedure's (head, labels behind their clauses, the two drops, the tail) (token diff in the
  first-fill Addendum, [upd] (7)). The UPDATE is unchanged in this fill (58889da6…, re-built equal by upd130b.py).
- G-L43, ONE DATA CLAUSE NAMES NO COUNTER (FLAG; CHECKER's call; Lead ruling: L-2 verbatim). data130a.py (A) splits L-2's tail at «; »
  outside parentheses: [1] the obstruction W-FLAT (a statement part, not DATA); [2] the frozen instances with their iteration counts and
  files (unit: iterations, from wrap_lmcs_xi.out / wrap_fried_xi.out / wrap_long.out / free_xi.out; checked); [3] LW-1's DATA clause (unit,
  column T, the six counters by name; numbers checked); [4] the cited replays L-COMP 20 and REFEREE 33 (counters by reference, «their
  counters in their own pinned outputs»; REFEREE 33's «18 must-be-0 counters, named in its report»); [5] R-2's sentence (the six counters by
  name; 4,000 / 3,000 / 300 and the W rows checked); [6] «L-RED 66 R236 / R237 (1) (0037d948, 5eca1c32) on its own engine.», which names NO
  counter. Read as a member of [4]'s list it is covered by reference, as L-COMP 20 is; but [5] stands between them (the point of W-L2-1 and
  N-W2), so a reader can take [6] as a free clause. R237 (1) itself names WRAP's six counters («## 1. Results (must-0: s3fail, nonstd,
  nohoward, fbwrong, endwrong, wrong; unit as in wrap104.py's header)», docs/red/R237-wrap.md l. 13 at 5eca1c32). Proposed for a later line
  only (not applied): "on its own engine." → "on its own engine (WRAP's six counters 0).". Both referees: REFEREE-2 «The DATA rule is met.»
  (Add. 2, l. 300); REFEREE §8 checks the DATA clause element by element and reads the R-2 sentence as the lane's own §9 DATA (N-W2), with
  no remark on [6]. SECOND FILL: Lead (03:05Z): L-2 stays verbatim; the entry carries ONE Lead-text bullet right after the Note bullet,
  "DATA counters for the cited replay L-RED 66 R236 / R237 (1) (claude/l-red 0037d948, 5eca1c32), named here from its report (L43): …",
  filled by script (fill2.py) from docs/red/R237-wrap.md at 5eca1c32 and docs/red/R236-fn.md at 0037d948 (byte-equal at 5eca1c32): R237 (1)
  names WRAP's six must-0 counters with their values (0 on every set) and a firing control; R236 names no must-0 counter (flag G-R236). The
  values quoted from R237 (1) equal its own outputs (data130b.py: wr237_lmcs_fig4.out, wr237_lmcs_table4.out, wr237_json.out, wr237_ctrl.out
  at 5eca1c32), except the W(switchallexp_n), n = 2, 3 values, which have no output file of their own at 5eca1c32 beyond the control row and
  are quoted from the report only.
- G-R236, L-RED 66 R236 NAMES NO COUNTER (FLAG for CHECKER; the Lead's instruction: "If the report names no counters, say so in the bullet
  and FLAG it"). docs/red/R236-fn.md at 0037d948 announces «Labels: CONFIRMED / FLAWED / DEAD / DATA (unit, set, scope, counter).» (l. 6)
  but names no must-0 counter: it gives counts with units (iterations, fallbacks, regions, the classification of its self-check differences
  by start, fallback and real divergence). Its own output experiments/red/r236/out/f236_free.out (0037d948) carries a column «regfail xi 0
  spec 0» on all seven F_n rows (data130b.py), which the report text does not name; the entry does not use it (the bullet quotes the report
  only, as ruled). R237 (1), the other half of L-2's clause, names its counters. CHECKER's call whether "named here from its report" is met
  for R236 by its unit-bearing counts.
- G-0, THE CHECKER NUMBER (FLAG). C142 is R128's (open), C143 the Lean rows (claude/checker 37fcbd21, PASS), C144 R129's, C145 L-FORMAL's Γ3
  / PAD Lean rows (the Lead's state log: «Γ3/PAD rows -> CHECKER C145 when on origin.» (l. 3427)); «C146» occurs 0 times in trunk docs/ and
  notes/ at HEAD. This draft uses C146 (line 1, title fill tail, UPDATE head), as the brief says; the Lead confirms or renames. SECOND FILL:
  C146 confirmed by the Lead (03:05Z); no change (already used in line 1, the title's tail and the UPDATE head).
- G-MERGE, THE OBJECTS ARE NOT IN TRUNK (FLAG for the Lead; before landing; merge.out). None of the cited l-si, referee or referee-2 commits
  is an ancestor of HEAD 4af9279d. claude/l-si: merge base 547985a1, 66 commits to faf0c8ff, of which 9 are not in R128's merge 7b0a58ae
  (2051a0ee … e01447e7 … faf0c8ff; boxes 104 Add. B-C, 105, 106 and the packet); old-style merge-tree into HEAD: no conflict marker; outside
  the lane's paths only docs/agents/handover-checks/L-SI.md; it brings check.sh blocks box104, box105, pwrap and box106 into the gate
  (sicheck.out). claude/referee: R129's merge 28b95151 already contains ef4d3bd1, c6fcf2b6, 99df2458 (this report) and e44ce56b, 90703a81
  (REFEREE 33's pre-read); 32d61d60 (§8) is the one commit beyond it; old-style merge-tree into HEAD: no conflict marker. claude/referee-2:
  R129's merge 1177c24d contains 3cf594cc, 07fd5ae4, 5d30968a; 01e83df5 (Add. 2) and 0f2606da (REFEREE-2 39's handover, notes/REFEREE-2.md
  only, a descendant of 01e83df5) are the two commits beyond it; old-style merge-tree into HEAD: no conflict marker. claude/l-si's head
  moved to 18cd2b88 (handover check, docs/agents/handover-checks/L-SI.md only). Pairwise old-style merge-tree of faf0c8ff, 32d61d60 and
  0f2606da against each R128 / R129 head (7b0a58ae, 16e8dcb0, 4a6db414, 366a38ab, 28b95151, 1177c24d): no conflict marker; the only common
  changed paths are inside one lane's own lineage. MERGE LIST (for CHECKER, after R128's and R129's merges): l-si faf0c8ff (or its head
  18cd2b88, which adds the handover check only); referee 32d61d60; referee-2 0f2606da (contains 01e83df5); and C146's checker commit. Cited
  records, not merged for this entry (as in R128 / R129): l-comp aa863db5, l-red 0037d948, 5eca1c32 (each on its origin branch), l-si
  26704e01 (in R128's 7b0a58ae), referee e44ce56b / 90703a81 (in R129's 28b95151). SECOND FILL: MERGE LIST (second fill; Lead 03:05Z): l-si
  faf0c8ff (or its head 18cd2b88, the handover check only); referee 32d61d60; referee-2 0f2606da, as cited (origin is now adda3245,
  REFEREE-2 40's handover check, docs/agents/handover-checks/REFEREE-2.md only; not needed); and C146's checker commit. merge130b.sh re-run
  at the second fill's fetch: no conflict marker.
- G-BASE, R128 AND R129 NOT LANDED (FLAG for the Lead). R130 is placed after R129 (the order of record). Simulated twice (sim130a.py): base
  (a) HEAD as is, R130 directly after R127 (a DRY RUN: not the landing order); base (b) HEAD + R128's block d[282:522] (third fill) + R129's
  block d[153:303] (second fill) before «**Erratum E-1**», then R130 after R129, and GAPS with R128's (ba695811) and R129's (31d7b642)
  UPDATEs filled, then R130's. If either block changes before landing, base (b) must be re-run; R130 cites no R128 or R129 text
  (prem130a.py: R128 / R129 tokens in L-2: 0). SECOND FILL: Local HEAD is now 626da53c (2026-11-13T03:11:28Z, «Lead: L55 (verify.sh:
  experiment self-checks NOT RUN when experiments/ …»; it changes docs/DECISIONS-INDEX.md, docs/DECISIONS.md, docs/agents/LEAD-STATE.md and
  scripts/verify.sh only): RESULTS, GAPS, the R128 and R129 drafts, scripts/check_docs.py and TARGET.md are byte-equal at 4af9279d and
  626da53c (asserted), so base (b) is built on 626da53c's bytes and the first fill's line numbers stand. sim (b) re-run on this draft
  (sim_p1.out): R130 at l. 16519-16715 after R128 l. 16127 and R129 l. 16368 (the block is 197 lines, one bullet more); GAPS l. 11 order
  R127 < R128 < R129 < R130; check_docs.py on that landed trunk: rc 0 (G-SHAPE).
- G-4, PREMISE SCOPE (note). Every RESULTS R-id L-2 cites is landed at HEAD (prem130a.py: R15 l. 624, R57 l. 2893, R104 l. 9864, R118 l.
  13607; and R24 l. 1064, R103 l. 9641 inside the [RULE] quote of the packet); L-2 does NOT cite R128 or R129 (0 tokens), nor R117 (LW-3
  removed «R117's core»). Only R118 carries the prefix «RESULTS»; «R57 (b) as landed in R104», «Fact DUAL (R104)», «R15 (a), (c), (d)» are
  bare R-ids of landed entries (R123-R127 lines write «RESULTS R…»; CHECKER's call; no change proposed). «R236 / R237 (1)» are L-RED report
  ids («L-RED 66 R236 / R237 (1)»), not RESULTS ids. [SPEC] is docs/new/N5-ssi-global.md and [N5XI] docs/new/P-N5-XICYC.md l. 45-47 (R118's
  frozen packet), both at HEAD. The packet's §1 [Q] quotes from RESULTS (8 pieces) are found in their entries at HEAD. The external premise
  [F11] (G-F11).
- G-F11, THE CITED THEOREM (note; CLAUDE.md «Every cited result has an opened source (arXiv id or DOI, theorem/section number) in your
  notebook»). L-2: «[F11] = Friedmann, arXiv 1106.0778v2, §5», «[F11] Lemmas 5.1, 6.7», «[F11] Theorem 6.14»; packet §1: «Logical Methods in
  Computer Science 7 (3:19), 2011; arXiv 1106.0778v2, 618,145 B, pdf sha256
  46c96f44775aa2b07cad20912cb325b177e38c94cb2e40297df66b6047679611» (l. 93-94); notes/L-SI.md at faf0c8ff (successor 53): «(successor 53,
  box 104 Add. C / P-N5-WRAP) Friedmann, arXiv 1106.0778v2 (LMCS 7 (3:19) 2011)» (l. 3469) and «p. 17 Lemma 6.7, Fact 6.1, p. 23 Theorem
  6.14 (pdftotext)» (l. 3472), and (successor 52) «Theorem 6.14 (at least 2^n improvement steps with I^loc on G_n from its initial
  strategy)» (l. 160). Both referees opened the PDF: REFEREE «Fetched arxiv.org/pdf/1106.0778v2 into a fresh scratch directory: 618,145 B,
  sha256» (l. 33); REFEREE-2 «[F11] opened by me: https://arxiv.org/pdf/1106.0778v2, 618,145 B, sha256» (l. 16). The id is the same in L-2,
  packet and notebook; no DOI is recorded (an arXiv id with the theorem number meets CLAUDE.md). The landscape doc is not cited. No flag.
- G-L41, REFEREE-ORIGINATED STEPS (note). Claim NT is credited in L-2's label «(Claim NT: REFEREE successor 33's claim and proof (L41),
  rendered by L-SI 53)»; L41 asks that the author sign and the other referee sign independently, both quoted, and that the scope tail say
  so: REFEREE 34 signs as the originating lane (§0 l. 206), REFEREE-2 independently (l. 264; 1.2 «Under L41 I sign Claim NT independently;
  its author is REFEREE 33 (claude/referee e44ce56b, as the packet quotes it).», l. 48-49); L-2 carries the credit in the label, not as the
  word «referee-originated» in its tail (R129's form). The packet also quotes REFEREE 33's «Status. Claim NT and (T-4) are
  referee-originated: under L41 they count only when the lane has written them and the other referee has checked them independently. I would
  sign them.» (l. 330-331): (T-4) is the route of Corollary NT-RUN, which the packet labels «NT-RUN PROVED (lane)» (To sign, l. 36) and L-2
  does not credit; both referees signed NT-RUN (REFEREE-2 independently). The line-item origins: LW-1, LW-2, LW-3 and N-1 are REFEREE 34's,
  R-1, R-2, R-3 REFEREE-2's (fixes entry 1). CHECKER's call; no change proposed (L-2 verbatim).
- G-S, STALE STATUS WORDS (note; CHECKER's call; Lead ruling: L-2 verbatim). In L-2 (hence the title and the UPDATE): «CONDITIONAL until two
  referees sign» 1, «PROVED lane» 1, «pending» 0, «CANDIDATE» 0, «not landed» 0, «will » 0. After both signatures the CONDITIONAL that stays
  is XI-EXP's own (on READING F-1 and Theorem 6.14 as published; REFEREE-2 3.8 l. 266) and the DEAD row's DEAD-CONDITIONAL (fixes entry 1,
  l. 28-29); «until two referees sign» is true of the line as frozen, and the entry body states the signed status (Claims signed, Setting
  and scope). In the entry block: the title's fill token (the CHECKER commit, PENDING until landing) only (G-R8 resolved).
- G-6, NAMES (note; counted in RESULTS at HEAD as whole tokens): «WRAP» 0, «Claim NT» 0, «NT-RUN» 0, «XI-EXP» 0, «W-FLAT» 1, «K3-W» 0,
  «ODD-W» 0, «TAU-W» 0, «ESC-W» 0, «REACH-W» 0, «E1-W» 0, «PAD-W» 0, «S3-W» 0, «ENDGAME-W» 0, «DEAD-END» 0, «[F11]» 0, «P-N5-WRAP» 0, «R130»
  0, «C146» 0, «F_n» 0, «W^L_n» 0. «WRAP» is not a landed name (R129's draft L-2 names «L-SI 52's Lemma WRAP» as a related lane statement:
  the same lemma, signed here). «W-FLAT» occurs once, in RESULTS R26 (l. 1169, «a W-FLAT RUN is a maximal run of consecutive»), a different
  notion (a run of an N5 phase), while L-2's «obstruction W-FLAT» is the wrapper's flat arena: a name clash in words only. Proposed: if
  CHECKER finds it confusing, cite this entry's as "RESULTS R130 obstruction W-FLAT"; no line change.
- G-BRIEF (notes on the brief). (1) "REFEREE … §8 L-2 byte test MATCHES at commit 32d61d60. It may NOT be on origin yet": not on origin at
  Fri Nov 13 02:07:12 UTC 2026; on origin at the Lead's 02:36Z message (G-R8, resolved). (2) "Addendum 2 01e83df5 …: L-2 MATCHES; R-2
  re-anchoring judged FAITHFUL": the word «FAITHFUL» is not in the report; it says «Re-anchored as fixes entry 1 step 3 says» (l. 290-291),
  «My script does the same from my report's text.» (l. 292) and «The DATA rule is met.» (l. 300). (3) "scope … WRAP + F_n + Friedmann [F11]
  Theorem 6.14": the brief quoted in the packet (l. 2-4) names F_n, but F_n's route is not in this packet («FREE-REACH and F_n (box 104
  §4-§5: the same fact in R104's genome shape with free carrier priorities; REFEREE 33's PW-4: «the Lead's call»): not needed for XI-EXP»,
  l. 442-443); F_n enters L-2 only as frozen instances with iteration counts (DATA). (4) "L-RED 68 R237 (2) (3732f4a1)": neither L-2 nor the
  packet cites it (data130a.py), so the entry does not ("cite only as the line and packet do", the brief). (5) "trunk … local HEAD
  4af9279d": one commit ahead of origin e8b6abf0; RESULTS and GAPS byte-equal (TRUNK).

### R130 [refereed-only] DEAD-END packet for the candidate N5′-xi (RESULTS R118's [N5XI]: SPEC S1-S5 with box 190's S4a tie rule), CONDITIONAL until two referees sign: (Lemma WRAP, PROVED lane) for EVERY parity game H and every positional Even strategy s0 of H, the W-flat wrapper W(H, s0) (n + 7·m_E + 6·m_O + n_O + 9 vertices: every edge of H stretched to a 6-edge path through an Odd gate with a pad to an even self-loop c_W above H, an Even valve with an exit to the core K0-K3 (with pads pA, s, q, r), one pe_o pad per Odd vertex; new vertices in wrap104.py's order) makes N5′-xi from SPEC's default start S3 run, at H's Even vertices, a Howard (switch-best, Vöge-Jurdziński values) run of H from s0 and stop after exactly T + 3 iterations with one fallback, and makes N5 stop after exactly F + 2 iterations with one fallback (F ≤ m_E − |V_E| + 1 under [RULE]); every step proved on W (core lemma K3-W, Odd's reply ODD-W with values stretched by 6, τ fixed TAU-W, the W-flat arena ESC-W, REACH-W, endgame E1-W to E4-W); premises [SPEC], [N5XI], [1E-N3] (R57 (b) as landed in R104), Fact DUAL (R104), R15 (a), (c), (d), [RULE] (Remark 3 only); (Claim NT: REFEREE successor 33's claim and proof (L41), rendered by L-SI 53) in a 1-sink game ([F11] = Friedmann, arXiv 1106.0778v2, §5) every strategy σ with Ξ_ι ⊴ Ξσ gives distinct valuations to distinct nodes, so by [F11] Lemmas 5.1, 6.7 and R15 (a) no tie occurs on Howard's run of G_n (Figure 4's injective priorities, the READING below) from ι and that run is the I^loc run of [F11] Theorem 6.14 (Corollary NT-RUN); (Statement XI-EXP, CONDITIONAL on WRAP and Claim NT being signed, with [F11] Theorem 6.14 cited as published on the READING that Table 4's six priority formulas carry a misprint and Figure 4's priorities are meant) N5′-xi needs 2^Ω(n) iterations on a game with O(n²) vertices, so 2^Ω(√|V|): exactly T_n + 3 ≥ 2^n + 3 iterations on W(G_n, ι), |V| = 10.5n² + 152.5n + 48; obstruction W-FLAT (τ inert, every option of every Even vertex of H tied in S4a's arena, so the Ξσ-best tie pick is Howard's rule on H); frozen instances W(G_n, ι) = WL_1 … WL_4 (11, 29, 65, 137 iterations), W(switchallexp_n) = W_2 … W_8 and F_n = F_2 … F_8 (33 … 2,489 iterations = Howard T + 3; experiments/si/box104/out/wrap_fried_xi.out, wrap_long.out, free_xi.out) at claude/l-si 26704e01 experiments/si/box104/inst (F_n's route FREE-REACH not in this packet); DATA (unit: T_n, the steps of Howard's run on G^L_n from ι, = N5′-xi iterations − 3 on W^L_n; experiments/si/box104/out/wrap_lmcs_xi.out and wrap_long.out, column T, with WRAP's six must-0 counters s3fail, nonstd, nohoward, fbwrong, endwrong, wrong 0 on the same rows): T_n 8, 26, 62, 134, 278, 566, 1,142, 2,294 for n = 1, …, 8 (equal to 9·2^n − 10 on these eight), and 4,598, 9,206 for n = 9, 10 on G^L_n alone (REFEREE 33, claude/referee e44ce56b, docs/referee/scratch/wrap_logs/f11_H_fig4.out, column T); independent replays, every fail counter 0, their counters in their own pinned outputs, cited, not re-run: L-COMP 20 (aa863db5), REFEREE 33 (e44ce56b / 90703a81; its 18 must-be-0 counters, named in its report, 0 on 523,721 runs); WRAP's six must-0 counters (s3fail, nonstd, nohoward, fbwrong, endwrong, wrong; units in the packet §9) 0 on 4,000 random games for N5′-xi, 3,000 for N5, the frozen 300 and W(G_n, ι), W(switchallexp_n) for n ≤ 8; L-RED 66 R236 / R237 (1) (0037d948, 5eca1c32) on its own engine. N5 (SPEC) is not affected; G-N5-TIME stays OPEN; not M3 or M4, not a TARGET.md claim (P-N5-WRAP, docs/si/P-N5-WRAP.md; L-SI successor 53)., CHECKER PASS (docs/checker/C146.md, checker PENDING)
- Object (L-SI successor 53, D18 / D1 / D21, box 104 and its Addenda A-C; frozen, unchanged during review): packet P-N5-WRAP,
  docs/si/P-N5-WRAP.md, sha1 1670432a8a07490ff80ceed45c861515ff070b9b, 462 lines, 56,745 bytes (l-si e01447e7, 2026-11-12T21:08:48Z, the
  file's only commit; identical at faf0c8ff; pinned in experiments/si/pwrap/out/P-N5-WRAP.sha1). Both referees measured it (REFEREE
  «docs/si/P-N5-WRAP.md sha1 1670432a8a07490ff80ceed45c861515ff070b9b, 56,745 B, 462 lines;» (l. 13); REFEREE-2 «docs/si/P-N5-WRAP.md sha1
  1670432a8a07490ff80ceed45c861515ff070b9b, 56,745 B, 462 lines;» (l. 13-14)). Labels: «Labels: PROVED (L-SI lane, unrefereed) / PROVED,
  REFEREE-originated (L41: written here by the lane, to be checked by the other referee) / CONDITIONAL / DATA / READING (not to sign) / DEAD
  (only after two signatures, L43).» (l. 7-8). Scope line: «N5 (SPEC) is not affected; G-N5-TIME stays OPEN. Not a TARGET.md claim; not M3
  or M4; not a gauntlet step.» (l. 13-15). To sign (l. 22-38): §2 the wrapper W(H, s0) with its count and rank facts, §2.4 Fact (H);
  §4.1-§4.8 PAD-W, S3-W, K3-W with K2-r-W, ODD-W, TAU-W, ESC-W, REACH-W, E1-W to E4-W, ENDGAME-W; §3 Lemma WRAP (i)-(v); §5 Remark 3 (under
  [RULE]); §6 Claim NT (REFEREE 33's, L41) and Corollary NT-RUN; §7 Statement XI-EXP (CONDITIONAL); §8-§12 dead-end record (draft), DATA,
  independent DATA, what is not here, TARGET diff, machine checks: not to sign.
- Fixes: docs/si/P-N5-WRAP-fixes.md, append-only, one entry (faf0c8ff, 2026-11-13T00:29:35Z: 29 lines, 3,414 bytes, sha1
  9fff274d4e527c42b64f47ded6b3f2627a344c32). Entry 1 (L-SI successor 53): line L-2 from L-1 by the two reports, «Sources (byte copies; every
  string copied by experiments/si/pwrap/fix1/mkL2.py, never retyped)» (l. 3-4); «Lead 22:36Z / 00:05Z: R-1, R-2, LW-1 REQUIRED; LW-2, LW-3 /
  R-3 ADOPTED; N-1 a note with no line change.» (l. 9). Items and their origins: LW-1 (REQUIRED; REFEREE 34, L43: the DATA clause with unit,
  column, files and numbers; check stage be7da8f3 = REFEREE's L-1′), R-1 (REQUIRED; REFEREE-2: «G_n» in the NT clause with Figure 4's
  injective priorities), R-2 (REQUIRED; REFEREE-2: the counters named; applied to LW-1's clause because LW-1 rewrote R-2's Old string,
  «R-2's Old «REFEREE 33 e44ce56b / 90703a81: 18 counters 0 on 523,721 runs)» occurs once in L-1 but not after LW-1», l. 14-15), LW-2
  (ADOPTED; REFEREE 34: the instance files), LW-3 (ADOPTED; REFEREE 34's string, «to the core K0-K3 (with pads pA, s, q, r)» in place of «to
  R117's core»; REFEREE-2's optional R-3 makes the same point and is not used); N-1 (REFEREE 34's note, recorded, no line change: ««Γ3(G)»
  for R118-R126 / box 208 should read «Γ(G) / Γ3(G)»; wording only.», l. 26-27). «Nothing in the packet's statements changes; both referees
  SIGN them; XI-EXP stays CONDITIONAL as signed (the packet lands as a refereed DEAD-CONDITIONAL record for N5′-xi).» (l. 28-29).
- The RESULTS line is L-2, dbd5f0e83e3d0300842c46cf2ae24b30b853d784 (docs/si/P-N5-WRAP-line-L2.txt, l-si faf0c8ff, «Result: sha1
  **dbd5f0e83e3d0300842c46cf2ae24b30b853d784**, 3,598 B, one line, 44 «(» = 44 «)»; `cmp` with the lane's L-2: **EQUAL**. Nothing else
  changed.», the file's only commit; 3,598 bytes, one line, blob 2026-11-13T00:29:35Z). The title is L-2 verbatim, with nothing inserted and
  nothing stripped (it has no date parenthesis and no « — »; its scope tail, source note and final «.» are the line's own; flag G-SHAPE).
  L-2's parentheses balance (44 «(» / 44 «)»); it has 6 pipe characters (the bars of V_E once and of V twice, as in its title; flag
  G-SHAPE). It is written by experiments/si/pwrap/fix1/mkL2.py from L-1 (896f9e97394695f903131f832a67f31bcfc23c28, e01447e7, 2,648 bytes,
  frozen with the packet) with REFEREE 34's LW-1 (giving REFEREE's L-1′ be7da8f3a98e4c5a26158eae9aa2766c56531222, asserted), then
  REFEREE-2's R-1, R-2 (on LW-1's clause) and REFEREE 34's LW-2, LW-3, every string extracted from the reports. Rebuilt byte-equal by the
  drafter (the lane's mkL2.py in a git archive of faf0c8ff: cmp EQUAL) and by REFEREE-2 with its own code:
  299dafceb64587263b1492e5ef291d3bdf371ba7 (l. 295-296). REFEREE rebuilt it with its own strings (§8, 32d61d60): «cmp with the lane's L-2:
  EQUAL. Each old string occurs exactly once at its step. L-2 = L-1 + exactly LW-1, R-1, R-2 (re-anchored), LW-2, LW-3.» (l. 231-232) (its
  L-1 test: «my result on L-1: sha1 be7da8f3a98e4c5a26158eae9aa2766c56531222.» (l. 215-217)).
- Claims signed (REFEREE successor 34: §1-§2 ef4d3bd1, §3-§7 c6fcf2b6, §0 99df2458, §8 32d61d60; REFEREE-2 successor 39: boxes 1-2 3cf594cc,
  box 3 and verdict 07fd5ae4, Add. 1 5d30968a, Add. 2 01e83df5). REFEREE's table («## 0. Verdicts», R-P-N5-WRAP.md l. 191-209), row by row
  as the report prints it: §2 Definition of W(H, s0), vertex order, size count, rank facts (R_W), standard state → **SIGN** (definition;
  count and (R_W) re-derived) (l. 194); §2.4 Fact (H) → **SIGN** (l. 195); §4.1 PAD-W (W1) → **SIGN** (l. 196); §4.2 S3-W = WRAP (i) →
  **SIGN** (l. 197); §4.3 K3-W (a)-(d) with K2-r-W → **SIGN** (l. 198); §4.4 ODD-W (a)-(d) → **SIGN** (l. 199); §4.5 TAU-W = WRAP (ii) =
  E0-W → **SIGN** (l. 200); §4.6 ESC-W → **SIGN** (l. 201); §4.7 REACH-W = WRAP (iii), first half of (v) → **SIGN** (l. 202); §4.8 E1-W,
  E2-W, E3-W, E4-W (a), (b); ENDGAME-W = WRAP (iv), second half of (v) → **SIGN** (l. 203); §3 Lemma WRAP (i)-(v) as a whole → **SIGN** (l.
  204); §5 Remark 3 (under [RULE]) → **SIGN** (PROVED under [RULE]); Remarks 1, 2 READING (l. 205); §6 Claim NT (this lane's claim, REFEREE
  33; the packet's rendering) → **SIGN** (as its originating lane; L41: needs REFEREE-2's independent signature) (l. 206); §6 Corollary
  NT-RUN → **SIGN** (CONDITIONAL on WRAP, as labelled) (l. 207); §7 Statement XI-EXP → **SIGN AS CONDITIONAL**: correct as stated,
  conditional on WRAP and Claim NT being signed by two referees, with [F11] Theorem 6.14 cited as published on READING F-1 (both confirmed
  from the PDF, §1.3) (l. 208); §8 DEAD row (draft) → scope and obstruction CORRECT: N5′-xi as an M4 candidate only; DEAD-CONDITIONAL until
  two signatures (L43) (l. 209); then «Gaps: **none.** External premise: [F11] arXiv 1106.0778v2 (sha256 46c96f44…), opened by me: Theorem
  6.14 p. 23, I^loc p. 6, 1-sink p. 8, Lemma 6.7 p. 17, the restriction p. 17-18; F-1 (Figure-4 priorities) confirmed by my own
  transcription; F-2 confirmed; Lemmas 6.2-6.13 not read (not needed for «as published»).» (l. 210-212). REFEREE-2's table («3.8 Verdicts»,
  R2-P-N5-WRAP.md l. 251-268), row by row: §2 W(H, s0), order, count, (R_W), standard state; §2.4 Fact (H) → SIGN (l. 254); §4.1 PAD-W; §4.2
  S3-W = WRAP (i) → SIGN (l. 255); §4.3 K3-W (a)-(d), K2-r-W → SIGN (l. 256); §4.4 ODD-W (a)-(d) → SIGN (l. 257); §4.5 TAU-W = WRAP (ii) →
  SIGN (l. 258); §4.6 ESC-W → SIGN (l. 259); §4.7 REACH-W = WRAP (iii), first half of (v) → SIGN (l. 260); §4.8 E1-W to E4-W, ENDGAME-W =
  WRAP (iv), second half of (v) → SIGN (l. 261); Lemma WRAP (i)-(v) → SIGN (l. 262); §5 Remark 3 → SIGN, CONDITIONAL on [RULE] (as labelled)
  [[RULE] not re-proved by me] (l. 263); §6 Claim NT → SIGN (independent check under L41; author REFEREE 33) (l. 264); §6 Corollary NT-RUN →
  SIGN, CONDITIONAL on WRAP's second signature (l. 265); §7 Statement XI-EXP → SIGN as a CONDITIONAL statement [stays CONDITIONAL on WRAP
  and Claim NT signed by both referees, READING F-1 and Theorem 6.14 as published (F-2)] (l. 266); §8 DEAD row (draft) → SIGN as
  DEAD-CONDITIONAL; scope N5′-xi as an M4 candidate only [DEAD only after both signatures (L43)] (l. 267); line L-1 (896f9e97) → SIGN WITH
  GAP [«L-1's NT clause names G_n without its priorities; L-1's DATA clause names no counter» (R-1, R-2 exact strings in 3.7)] (l. 268);
  then «No statement is REFUSED. No signed proof keeps an open gap. N5 (SPEC) is not affected; G-N5-TIME stays OPEN; not M3, not M4.» (l.
  269). L-1's SIGN WITH GAP is closed on L-2, and both referees MATCH L-2 (REFEREE §8, REFEREE-2 Add. 2; quoted under Signatures). The joint
  gap map: EMPTY (REFEREE l. 210; REFEREE-2 l. 269). No statement is REFUSED; Claim NT is signed by its originating lane and independently
  by REFEREE-2 (L41); Corollary NT-RUN is CONDITIONAL on WRAP, which both sign; Statement XI-EXP is signed as a CONDITIONAL statement; the
  DEAD row is DEAD-CONDITIONAL and not signed as DEAD (Not signed).
- Setting and scope, as both referees sign it: REFEREE «Scope of the signatures: as the packet states (scope line): N5 (SPEC) not affected;
  G-N5-TIME OPEN; not M3 / M4; not a TARGET.md claim.» (l. 213); REFEREE-2 «No statement is REFUSED. No signed proof keeps an open gap. N5
  (SPEC) is not affected; G-N5-TIME stays OPEN; not M3, not M4.» (l. 269), and on XI-EXP «It STAYS CONDITIONAL: (1) on WRAP and Claim NT
  being signed by both referees (I sign both here; the other signature is REFEREE's); (2) on READING F-1.» (l. 191-192). The objects are
  every parity game H with every positional Even strategy s0, the wrapper W(H, s0), the runs of N5′-xi (RESULTS R118's [N5XI]) and of N5
  (SPEC) from SPEC's default start S3 on W(H, s0), and [F11]'s G_n with Figure 4's priorities (G^L_n). Statements as signed (packet with
  fixes entry 1, which changes none):
  (a) §2 the wrapper W(H, s0), its vertex order, count, rank facts (R_W) and standard state; §2.4 Fact (H): both SIGN (REFEREE l. 194-195;
    REFEREE-2 l. 254).
  (b) §4.1-§4.8 PAD-W, S3-W = WRAP (i), K3-W (a)-(d) with K2-r-W, ODD-W (a)-(d), TAU-W = WRAP (ii), ESC-W, REACH-W = WRAP (iii), E1-W to
    E4-W, ENDGAME-W = WRAP (iv): both SIGN (REFEREE l. 196-203; REFEREE-2 l. 255-261).
  (c) §3 Lemma WRAP (i)-(v): both SIGN (REFEREE l. 204; REFEREE-2 l. 262).
  (d) §5 Remark 3 (N5's bound on W(H, s0) under [RULE]): both SIGN, under [RULE] (a landed premise, R104's premise clause) (REFEREE l. 205;
    REFEREE-2 l. 263).
  (e) §6 Claim NT (REFEREE 33's claim and proof, L41; the lane's rendering): REFEREE SIGN as the originating lane, REFEREE-2 SIGN
    independently (REFEREE l. 206; REFEREE-2 l. 264).
  (f) §6 Corollary NT-RUN: both SIGN, CONDITIONAL on WRAP (signed by both) (REFEREE l. 207; REFEREE-2 l. 265).
  (g) §7 Statement XI-EXP (N5′-xi needs 2^Ω(n) iterations on W^L_n, a game with O(n²) vertices): REFEREE SIGN AS CONDITIONAL, REFEREE-2 SIGN
    as a CONDITIONAL statement; it stays CONDITIONAL on READING F-1 and on Theorem 6.14 as published (F-2) (REFEREE l. 208; REFEREE-2 l.
    266).
- Premise (named in L-2's premise clause «premises [SPEC], [N5XI], [1E-N3] (R57 (b) as landed in R104), Fact DUAL (R104), R15 (a), (c), (d),
  [RULE] (Remark 3 only)» and in its NT clause «R15 (a)»; no «…» quote in L-2; checked by script at trunk HEAD 4af9279d, prem130a.py):
  [SPEC] (docs/new/N5-ssi-global.md, the SPEC that RESULTS R15, R57, R104, R118 run); [N5XI] RESULTS R118 (l. 13607) and its frozen packet
  docs/new/P-N5-XICYC.md l. 45-47; [1E-N3] RESULTS R57 (l. 2893) (b) as landed in RESULTS R104 (l. 9864); [DUAL] R104 (a) Fact DUAL; RESULTS
  R15 (l. 624) (a) Lemma A, (c), (d); [RULE] (Remark 3 only) R104's premise clause, with RESULTS R24 (l. 1064) and R103 (l. 9641) inside it.
  All landed (### R<n> headings at HEAD); none is R128 or R129; L-2 cites neither. The external premise [F11] (Friedmann, LMCS 7 (3:19)
  2011, arXiv 1106.0778v2): Lemmas 5.1, 6.7 and Theorem 6.14, opened by the lane and by both referees (flag G-F11). «Not used: any lemma of
  P-N5-REACH, P-N5-CHAIN, P-N5-END, R117, R118, R124, R125 (their proofs about Γ3(G) were the templates of §4; every step is re-proved here
  on W)» (l. 107-108). Both referees checked the quotes by their own scripts (REFEREE «**30 quotes, 0 missing**» (l. 25); REFEREE-2 «24
  quotes, 24 found» (l. 24); REFEREE-2 Add. 1 «10 of 10 found» (l. 279) for the ten REFEREE 33 items).
- L41 and L43. The packet's proofs are L-SI successor 53's, with one REFEREE-originated claim and proof named in L-2's label: «(Claim NT:
  REFEREE successor 33's claim and proof (L41), rendered by L-SI 53)» (l. 1). The packet credits it the same way («Claim NT and Corollary
  NT-RUN (Claim NT and its proof originate with REFEREE successor 33, R-WRAP-preread §3.2; L41; the written rendering below is L-SI 53's)»,
  l. 313). Under L41 the author lane signs it and the other referee signs it independently: REFEREE «**Claim NT and its proof originate in
  this lane** (successor 33, R-WRAP-preread §3.2, (T-2)); the packet renders it and labels it so (L41). I sign the packet's rendering below
  as this lane's claim; under L41 it counts as two-referee signed only when REFEREE-2 signs it independently.» (l. 5-7) and its §0 row
  «**SIGN** (as its originating lane; L41: needs REFEREE-2's independent signature)» (l. 206); REFEREE-2 «Under L41 I sign Claim NT
  independently; its author is REFEREE 33 (claude/referee e44ce56b, as the packet quotes it).» (l. 48-49) and its row «SIGN (independent
  check under L41; author REFEREE 33)» (l. 264). REFEREE 33 also called the run step (T-4) referee-originated (packet l. 330-331); the
  packet labels Corollary NT-RUN «PROVED (lane)», and both referees sign it (flag G-L41). L43: the DEAD row is not entered as DEAD: REFEREE
  «The DEAD row is not a DATA DEAD: it rests on a proof (WRAP, Claim NT) and a published theorem, and is labelled DEAD-CONDITIONAL until two
  signatures (L43: «DEAD» needs a refereed proof or an instance beyond an explicit bound). Correct use.» (l. 146-147); REFEREE-2 «L43: the
  killed statement is asymptotic; the row rests on a proof (WRAP + Claim NT + a published theorem), not on finitely many instances; it says
  «DEAD-CONDITIONAL» until two signatures. That is what L43 allows.» (l. 202-203). L-2 says «DEAD-END packet for the candidate N5′-xi …,
  CONDITIONAL until two referees sign» and records the obstruction W-FLAT and the frozen instances. LW-1 (REFEREE, L43) gave the DATA clause
  its unit, column, files and numbers, and R-2 (REFEREE-2) named the counters; one clause of L-2 names no counter (flag G-L43).
- Not signed: packet §5 Remarks 1, 2 (READING), §7's «More generally» bullet (READING), §8 DEAD row as a DEAD (draft; signed as
  DEAD-CONDITIONAL, scope N5′-xi as an M4 candidate only: REFEREE «scope and obstruction CORRECT: N5′-xi as an M4 candidate only;
  DEAD-CONDITIONAL until two signatures (L43)» (l. 209); REFEREE-2 «SIGN as DEAD-CONDITIONAL; scope N5′-xi as an M4 candidate only» with
  «DEAD only after both signatures (L43)» (l. 267)), §9 (DATA), §10 (independent DATA), §11 (FREE-REACH and F_n: not in this packet), §12
  (TARGET diff, READING), §13 (machine checks); [F11]'s Lemmas 6.2-6.13 (not read by REFEREE, not needed for «as published»); the referees'
  replays; L-RED 68 R237 (2) (3732f4a1; cited by neither the packet nor L-2).
- Referee strengthening (NOT part of this entry; referee checks): (i) REFEREE 34: own replay with its lane's code (no lane code), 22,000
  wrapped games on new seeds, «**All 18 must-be-0 counters (the box's six and twelve of my lane's: size, w1, w4a-d, w5, w6, w8, v5, rem2,
  rem3) are 0 on every set**» (l. 128-129); G^L_n alone from its own transcription, n = 1..10, T = 8 … 9,206 (l. 131-133); F-1 and F-2
  confirmed from the PDF («**F-1 (misprint reading): CONFIRMED independently.**», l. 52; «**F-2 («as published»): CONFIRMED**», l. 58). (ii)
  REFEREE-2 39: own replay r2wrap.py, 0 failures on 3,000 + 3,000 random wrapped games, 1,000 + 1,000 with permuted indices, 600 for Remark
  3, W(G_n, ι) n ≤ 5 and G_n n ≤ 8, four controls fire (3.5, l. 213-226); F-1 checked from the PDF (1.3). (iii) L-COMP 20 BOX 44 (aa863db5),
  REFEREE 33's replay (e44ce56b / 90703a81, 523,721 runs), L-RED 66 R236 / R237 (1) (0037d948, 5eca1c32): cited in L-2, not re-run.
- Honest limits: (i) The lower bound is not proved here: XI-EXP rests on [F11] Theorem 6.14 cited as published, read on the misprint reading
  F-1 (Figure 4's priorities, not Table 4's) and in its published form F-2 («Honest limits: the lower bound rests on a published theorem
  read on a misprint reading (F-1) and stated in its published form (F-2); the lane's tools were written by the lane (two engines are two
  implementations of one rule); the independent replays are DATA.», l. 452-453); it stays CONDITIONAL. (ii) It is a dead end for ONE
  candidate, N5′-xi (RESULTS R118's [N5XI]) from S3, as an M4 candidate; N5 (SPEC) is not affected (WRAP (v), Remark 3: at most m_E + 3
  iterations less the number of Even vertices of H, on every W(H, s0) under [RULE]); G-N5-TIME stays OPEN; nothing about RESULTS R118-R127
  or boxes 208 / 209, whose games are genome games, not W^L_n (REFEREE's note N-1 on «Γ(G) / Γ3(G)», wording only). (iii) «Exponential» is
  in n only; in the number of vertices it is 2^Ω of the square root of that number, super-polynomial. (iv) The lane's tools were written by
  the lane; two engines are two implementations of one rule; the numbers in L-2 are DATA (checked from the frozen outputs, data130a.py). (v)
  N5's iteration counts on W(H, s0) depend on the index order (packet §9, W-2); the statements do not. (vi) No algorithm or bound is
  claimed; no novelty against the literature is claimed (not M3).
- Data (DATA, not proof): experiments/si/box104/ at l-si faf0c8ff (tools wrap104.py, n5v.py, n5bxi.py, free104.py; frozen outputs out/*.out;
  instances inst/ with SHA1SUMS, byte-equal to 26704e01) and experiments/si/pwrap/ (qwrap.py / out/qwrap.out, 30 items; out/P-N5-WRAP.sha1;
  fix1/mkL2.py, mkL2.out, SHA1SUMS), called from experiments/si/check.sh l. 1309 («bash box104/check104.sh») and l. 1313 («bash
  pwrap/checkW.sh», which checks the quotes, the instance sha1s, the §9 DATA lines, the packet sha1, the L-2 and fixes sha1s and the check
  stage be7da8f3), run by scripts/verify.sh once merged. Re-run by the drafter in a full git archive of faf0c8ff: rc 0, «BOX104 checks:
  PASS», «PWRAP checks: PASS»; with one byte appended to L-2 «PWRAP FAIL fixes entry 1 sha1», rc 1; with one byte prepended to
  box104/out/wrap_long.out «BOX104 FAIL …» and «PWRAP FAIL W^L_7 long», rc 1 (negative controls; restored, re-run rc 0). Frozen numbers by
  column name (data130a.py, 25 checks): T = 8, 26, 62, 134, 278, 566, 1,142, 2,294 on W^L_n, n = 1..8 (wrap_lmcs_xi.out fig4 rows,
  wrap_long.out), = 9·2^n − 10, iterations T + 3, 10.5n² + 152.5n + 48 vertices of W^L_n (the outputs' vertex-count column), the six
  counters 0 on those rows; 4,598, 9,206 at n = 9, 10 in REFEREE 33's f11_H_fig4.out (e44ce56b); W_2..W_8 and F_2..F_8: 33, 73, 153, 313,
  633, 1,246, 2,489 iterations = Howard T + 3; six counters 0 on 3,000 + 1,000 random games for N5′-xi and 3,000 for N5 (wrap_rand.out,
  seeds 1043, 1044), on the frozen 300 (wrap_json.out, 0 rows differing). Cited, not re-run: L-COMP 20 BOX 44 (aa863db5), REFEREE 33
  (e44ce56b / 90703a81), L-RED 66 R236 (0037d948) and R237 (1) (5eca1c32).
- Note (both referees, no change asked): REFEREE 34 §8 (32d61d60, l. 239-240): «Note N-W2 (no change asked): the R-2 sentence follows the
  cited-replays list after a semicolon; it is the lane's own §9 DATA, not a cited replay.»; REFEREE-2 Add. 2, note W-L2-1 (01e83df5, l.
  303-307): «The 4,000 / 3,000 / 300 runs are the lane's own (box 104 out/), not an independent replay. A reader may take them for a cited
  replay.» and «Old (once in L-2): «; WRAP's six must-0 counters (». New: «; and this lane's own runs (box 104, not a replay): WRAP's six
  must-0 counters (».». L-2 lands verbatim (Lead ruling). The runs behind L-2's «WRAP's six must-0 counters (s3fail, nonstd, nohoward,
  fbwrong, endwrong, wrong; units in the packet §9) 0 on 4,000 random games for N5′-xi, 3,000 for N5, the frozen 300 and W(G_n, ι),
  W(switchallexp_n) for n ≤ 8» are this lane's own (box 104: experiments/si/box104/out/wrap_rand.out, wrap_json.out, wrap_lmcs_xi.out,
  wrap_fried_xi.out, wrap_long.out), not a cited replay; the cited replays of that list are L-COMP 20 (aa863db5) and REFEREE 33 (e44ce56b /
  90703a81).
- DATA counters for the cited replay L-RED 66 R236 / R237 (1) (claude/l-red 0037d948, 5eca1c32), named here from its report (L43): R237 (1)
  (docs/red/R237-wrap.md at 5eca1c32) names WRAP's six must-0 counters, «must-0: s3fail, nonstd, nohoward, fbwrong, endwrong, wrong; unit as
  in wrap104.py's header» (l. 13), with the values «Every counter is 0.» (l. 17) on W(G_n, ι), n = 1..4, both priority versions; «n = 2, 3
  give 33 / 73 = Howard T + 3 (30 / 70), every counter 0.» (l. 18) on W(switchallexp_n); «every counter is 0 on all 300;» (l. 22) on the 300
  frozen random games; its control: «Control CTRL=1 («best» := worst): nohoward 660 on W(switchallexp_2) (fires).» (l. 25). R236
  (docs/red/R236-fn.md at 0037d948) names no must-0 counter by name («Labels: CONFIRMED / FLAWED / DEAD / DATA (unit, set, scope, counter).»
  (l. 6)): its DATA are counts with their units, the iterations and fallbacks of N5′-xi on F_2..F_8, «33 / 73 / 153 / 313 / 633 / 1,246 /
  2,489, with 1 fallback each.» (l. 11), the regions against Zielonka, «The regions equal the harness Zielonka's on all seven games.» (l.
  13), and its self-check differences classified «start 0, fallback 0, real divergence 0.» (l. 42) (flag G-R236).
- Signatures: REFEREE docs/referee/R-P-N5-WRAP.md, successor 34 (ef4d3bd1 2026-11-12T22:31:53Z, c6fcf2b6 2026-11-12T22:31:53Z, 99df2458
  2026-11-12T22:31:53Z; §8 32d61d60 2026-11-13T01:40:40Z): §0 verdict table l. 191-209; on L-1 «**Line L-1 (sha1 896f9e97…): does NOT match
  yet.** Required: LW-1 (L43: the DATA clause gives T_n as numbers with unit, column and files; C142 E-1's ruling); my result on L-1: sha1
  be7da8f3a98e4c5a26158eae9aa2766c56531222. Optional LW-2, LW-3 (the Lead's call). No statement, label or proof changes: a fixes entry with
  L-2 by script needs a byte test, not a re-sign.» (l. 215-217); note «Note N-1 (§6): «Γ3(G)» for R118-R126 / box 208 should read «Γ(G) /
  Γ3(G)»; wording only.» (l. 214). On L-2, §8: «Verdict: **Line L-2 MATCHES** (L-1 + exactly LW-1, R-1, R-2 as applied to LW-1's clause,
  LW-2, LW-3; sha1 dbd5f0e8…). Statements and labels as in §0: every statement SIGN; XI-EXP CONDITIONAL as signed.» (l. 245-246) and «Fixes
  entry 1: line-only; records both referees' SIGN, the Lead's rulings, and my note N-1 verbatim. CORRECT.» (l. 244). REFEREE-2
  docs/referee-2/R2-P-N5-WRAP.md (= at its head 0f2606da), successor 39 (3cf594cc 2026-11-12T22:08:25Z, 07fd5ae4 2026-11-12T22:09:50Z,
  5d30968a 2026-11-12T22:34:35Z, 01e83df5 2026-11-13T01:28:18Z): verdict table l. 251-269; Add. 2 «L-2 (faf0c8ff, sha1 dbd5f0e8) MATCHES.
  R-1 and R-2 are met; my SIGN WITH GAP on L-1 is closed. Note W-L2-1 is optional.» (l. 309) and «No statement, label, condition or scope
  changes. XI-EXP stays CONDITIONAL; the DEAD row stays DEAD-CONDITIONAL until both signatures.» (l. 308). Lane (claude/l-si): L-SI
  successor 53, e01447e7 (packet FROZEN, L-1) and faf0c8ff (fixes entry 1, L-2). Pre-read and replays (not signatures): REFEREE 33
  (e44ce56b, 90703a81), L-COMP 20 (aa863db5), L-RED 66 (0037d948, 5eca1c32).
- INDEPENDENCE: each referee wrote its verdict without reading the other's (REFEREE «Not read before my verdict: docs/referee-2/ on
  P-N5-WRAP; L-RED 66 R236 / R237, L-COMP 20 BOX 44 (cited DATA, not opened).» (l. 8); REFEREE-2 «Independent: I did NOT open docs/referee/
  on WRAP (REFEREE 33's R-WRAP-preread, any R-P-N5-WRAP) or notes/REFEREE.md before this verdict is on origin;» (l. 3-4) and «Before this
  verdict was on origin I did not open docs/referee/ (REFEREE 33's R-WRAP-preread, any REFEREE review of WRAP), notes/REFEREE.md, box 104,
  L-COMP 20's box 44 or L-RED 66's R236 / R237, nor any lane tool.» (l. 273-274)). REFEREE-2 read REFEREE's report only after its verdict:
  «REFEREE 34's report read now (claude/referee 99df2458, docs/referee/R-P-N5-WRAP.md), after my verdict 07fd5ae4.» (l. 285-286). REFEREE's
  lane wrote the pre-read that originated Claim NT and disclosed it (Claims signed; L41): «I re-derived every step from the frozen text, not
  from the pre-read.» (l. 7). REFEREE's L-2 test (§8, after both verdicts) took REFEREE-2's R-1 from REFEREE-2's report: «parsed by my
  script from R2-P-N5-WRAP.md at claude/referee-2 07fd5ae4 §3.7» (l. 225-226). Each referee re-derived every proof step on W, opened [F11]
  itself and replayed the DATA on its own engine.
- TARGET.md diff: TARGET.md §2 (M4) asks for «There is a deterministic algorithm A and a polynomial p such that for every parity game G, A
  on input G halts within p(n + m) steps and outputs the pair (W_E(G), W_O(G)).» (l. 20-21); this entry claims no algorithm and no bound: it
  records that one candidate, N5′-xi, takes super-polynomially many iterations on a family of parity games in TARGET.md §1's sense
  (conditionally on READING F-1 and Theorem 6.14 as published), i.e. a gauntlet step-4 failure for N5′-xi (TARGET.md §5 step 4: «Written
  correctness and running-time proofs, double-refereed with every gap listed.», l. 45); REFEREE «## 7. TARGET.md diff: CLEAN» (l. 185);
  REFEREE-2 «Not M3, not M4, not a gauntlet step (it is the failure of step 4 for N5′-xi). G-N5-TIME (N5) stays OPEN. PASS.» (l. 231-232).
  It is not M3, not M4, not a TARGET.md claim, and not a step-4 pass for any candidate. L-2 ends its scope words «N5 (SPEC) is not affected;
  G-N5-TIME stays OPEN; not M3 or M4, not a TARGET.md claim». GAPS G-N5-TIME: open (about N5, which this entry does not touch).

Proposed GAPS line-11 UPDATE (append-only), to go AFTER the last UPDATE on GAPS l. 11 at landing (R129's, when R128 and R129 have landed; at
HEAD 4af9279d the last is R127's, «UPDATE 2026-11-12 13:58Z: RESULTS R127 (P-N5-SPLIT; CHECKER C141 850e9765)»), as a pure insertion with
one separating space before the row's closing « |». BUILT FROM L-2 by r130a/tools/upd130a.py: r129b/tools/upd129b.py's direct(), direct2()
and its R125-R128 controls copied unchanged (R118's procedure), a control on R129's draft UPDATE, and direct3() for L-2's form (flag G-U):
start «DEAD-END packet for the candidate N5′-xi (RESULTS R118's [N5XI]: SPEC S1-S5 with box 190's S4a tie rule), CONDITIONAL until two
referees sign: », the three labels «(Lemma WRAP, PROVED lane)», «(Claim NT: REFEREE successor 33's claim and proof (L41), rendered by L-SI
53)», «(Statement XI-EXP, CONDITIONAL on WRAP and Claim NT being signed, …)», the boundary «; » before «obstruction W-FLAT (», the drops «;
G-N5-TIME stays OPEN» and «; not M3 or M4, not a TARGET.md claim» (each once in L-2), the final «.» stripped, three pipe pairs (each once),
source prefix «(P-N5-WRAP, docs/si/P-N5-WRAP.md». Controls at HEAD (GAPS byte-equal to f9520557's and to origin trunk e8b6abf0's): the same
functions rebuild R125's landed UPDATE (f22faed5…, once on l. 11, True), R126's (89c5f357…, True), R127's (5bd83938…, it ends l. 11, True),
R128's draft UPDATE (ba6958119e92cc3ab00cee0348fc69a9e51441b3 = d[545] of the R128 draft at HEAD: True) and R129's
(31d7b6424542ec7fb7a0684df707c15caa5c5834 = d[319] of the R129 draft at HEAD: True); direct3 with R129's date separator rebuilds R129's
byte-equal; negative controls: an altered drop string, an altered label and an altered pipe string refuse, one changed byte of L-2 gives a
different line. sha1 58889da6f0b976ddc49e6ec89b6b3c75a7a133b4 of the line without newline and unfilled
(d217fc967e88b791057a1c6260184ad7f9a552d0 with its newline), 3726 bytes, 47 «(» / 47 «)», 0 pipe characters. <DATE>, <HH:MM> and <checker>
are the landing date, time and the CHECKER commit of the PASS (C146, G-0), all filled at landing:
UPDATE <DATE> <HH:MM>Z: RESULTS R130 (P-N5-WRAP; CHECKER C146 <checker>) [refereed-only] LANDED: DEAD-END packet for the candidate N5′-xi (RESULTS R118's [N5XI]: SPEC S1-S5 with box 190's S4a tie rule), CONDITIONAL until two referees sign: for EVERY parity game H and every positional Even strategy s0 of H, the W-flat wrapper W(H, s0) (n + 7·m_E + 6·m_O + n_O + 9 vertices: every edge of H stretched to a 6-edge path through an Odd gate with a pad to an even self-loop c_W above H, an Even valve with an exit to the core K0-K3 (with pads pA, s, q, r), one pe_o pad per Odd vertex; new vertices in wrap104.py's order) makes N5′-xi from SPEC's default start S3 run, at H's Even vertices, a Howard (switch-best, Vöge-Jurdziński values) run of H from s0 and stop after exactly T + 3 iterations with one fallback, and makes N5 stop after exactly F + 2 iterations with one fallback (F ≤ m_E − (the number of Even vertices of H) + 1 under [RULE]); every step proved on W (core lemma K3-W, Odd's reply ODD-W with values stretched by 6, τ fixed TAU-W, the W-flat arena ESC-W, REACH-W, endgame E1-W to E4-W); premises [SPEC], [N5XI], [1E-N3] (R57 (b) as landed in R104), Fact DUAL (R104), R15 (a), (c), (d), [RULE] (Remark 3 only) (Lemma WRAP, PROVED lane); in a 1-sink game ([F11] = Friedmann, arXiv 1106.0778v2, §5) every strategy σ with Ξ_ι ⊴ Ξσ gives distinct valuations to distinct nodes, so by [F11] Lemmas 5.1, 6.7 and R15 (a) no tie occurs on Howard's run of G_n (Figure 4's injective priorities, the READING below) from ι and that run is the I^loc run of [F11] Theorem 6.14 (Corollary NT-RUN) (Claim NT: REFEREE successor 33's claim and proof (L41), rendered by L-SI 53); N5′-xi needs 2^Ω(n) iterations on a game with O(n²) vertices, so 2^Ω(√(the number of vertices)): exactly T_n + 3 ≥ 2^n + 3 iterations on W(G_n, ι), the number of vertices = 10.5n² + 152.5n + 48 (Statement XI-EXP, CONDITIONAL on WRAP and Claim NT being signed, with [F11] Theorem 6.14 cited as published on the READING that Table 4's six priority formulas carry a misprint and Figure 4's priorities are meant): obstruction W-FLAT (τ inert, every option of every Even vertex of H tied in S4a's arena, so the Ξσ-best tie pick is Howard's rule on H); frozen instances W(G_n, ι) = WL_1 … WL_4 (11, 29, 65, 137 iterations), W(switchallexp_n) = W_2 … W_8 and F_n = F_2 … F_8 (33 … 2,489 iterations = Howard T + 3; experiments/si/box104/out/wrap_fried_xi.out, wrap_long.out, free_xi.out) at claude/l-si 26704e01 experiments/si/box104/inst (F_n's route FREE-REACH not in this packet); DATA (unit: T_n, the steps of Howard's run on G^L_n from ι, = N5′-xi iterations − 3 on W^L_n; experiments/si/box104/out/wrap_lmcs_xi.out and wrap_long.out, column T, with WRAP's six must-0 counters s3fail, nonstd, nohoward, fbwrong, endwrong, wrong 0 on the same rows): T_n 8, 26, 62, 134, 278, 566, 1,142, 2,294 for n = 1, …, 8 (equal to 9·2^n − 10 on these eight), and 4,598, 9,206 for n = 9, 10 on G^L_n alone (REFEREE 33, claude/referee e44ce56b, docs/referee/scratch/wrap_logs/f11_H_fig4.out, column T); independent replays, every fail counter 0, their counters in their own pinned outputs, cited, not re-run: L-COMP 20 (aa863db5), REFEREE 33 (e44ce56b / 90703a81; its 18 must-be-0 counters, named in its report, 0 on 523,721 runs); WRAP's six must-0 counters (s3fail, nonstd, nohoward, fbwrong, endwrong, wrong; units in the packet §9) 0 on 4,000 random games for N5′-xi, 3,000 for N5, the frozen 300 and W(G_n, ι), W(switchallexp_n) for n ≤ 8; L-RED 66 R236 / R237 (1) (0037d948, 5eca1c32) on its own engine. N5 (SPEC) is not affected (P-N5-WRAP, docs/si/P-N5-WRAP.md; L-SI successor 53). G-N5-TIME stays open.

Addendum (first fill) (subagent, started 2026-11-13T02:11:30Z by date -u; for the Lead and CHECKER; does not land). Checks ran on the pass-1 draft
  r130a/R130-draft.p1.md (sha1 b4fc6697ae0d8a67d7cdbf347e207b9762691513, 397 lines), which equals this file without this Addendum and its blank line (asserted by mkadd130a.py).
  Outputs verbatim below, each line tagged with its file: [fetch] fetch.txt, [fetch2] fetch2.txt, [fetch3] fetch3.txt, [blk] blocks.out, [neg] neg.out, [si] sicheck.out, [mk] mk.out, [upd] upd130a.out, [prem] prem130a.out, [data] data130a.out, [merge] merge.out, [note] note130a.out, [chk] chk_p1.out, [lp] lp_p1.out, [sim] sim_p1.out.
  Notes: (1) The Lead's message at 02:36Z (REFEREE 34's §8 on P-N5-WRAP on origin at claude/referee 32d61d60; REFEREE-2's head 0f2606da) came during
  the fill: fill130a.py was patched by patch_s8.py, patch_s8b.py, patch_s8d.py (its pre-patch text kept as fill130a.pre-s8.py) and merge130a.sh rewritten
  (merge130a.pre-s8.sh kept); [fetch2] is the second fetch; the blocks, mkL2.py, data and premise checks were not re-run for the new heads because
  the packet, L-1, L-2, fixes file and every cited output are byte-equal at l-si 18cd2b88 (asserted in fill130a.py), and upd/prem/data were re-run
  after the patch (same results). (2) patch_s8c.py wrote patterns, proposals and the brief's strings in "…" so that every «…» is a quotation (the
  whole-file sweep of the pass-1 draft then found 0 missing). (3) [si] is experiments/si/check.sh at faf0c8ff in the archive with the repository's
  object store visible read-only (GIT_DIR); a first try without it failed in rund/quotecheck.py (git show needs the objects) and a second was
  stopped by my 590 s timeout (rc 124); the run below is the third, in the background. (4) Not run: scripts/verify.sh, scripts/push.sh, the
  referees' own replays, Oink, Lean. (5) [fetch3], at the end of the fill: claude/referee-2 moved 0f2606da → adda3245 (REFEREE-2 40's handover check,
  docs/agents/handover-checks/REFEREE-2.md only; the report is byte-equal); the draft cites 0f2606da as the Lead's message says; adda3245 also merges cleanly
  in kind (the Lead picks the head to merge).
  [fetch] Fri Nov 13 02:07:12 UTC 2026
  [fetch] rc 0
  [fetch] l-si faf0c8ff87aad0bda8441f3b9b3f7f53e8775755
  [fetch] referee 28b951515c1696557a8713fde8b790c5d9127fb1
  [fetch] referee-2 01e83df53909f6852c1238bad7bb00a4f70275ae
  [fetch] l-red 3732f4a1db018c02983745496ad7011e6f02b9a8
  [fetch] l-comp c1c0a4293e4538716243768804dee37ebb7456ac
  [fetch] checker 37fcbd2175629c9002a483837f1cbd3681b910f6
  [fetch] vibrant-johnson-nxvvxo e8b6abf0170fb63ecbd68d058a2bb38599bc5b01
  [fetch] HEAD 4af9279d8c5e24454851fbace70e993299f6d68e
  [fetch] ls-remote referee 28b951515c1696557a8713fde8b790c5d9127fb1 refs/heads/claude/referee
  [fetch] ls-remote referee-2 01e83df53909f6852c1238bad7bb00a4f70275ae refs/heads/claude/referee-2
  [fetch] ls-remote l-si faf0c8ff87aad0bda8441f3b9b3f7f53e8775755 refs/heads/claude/l-si
  [fetch2] Fri Nov 13 02:36:36 UTC 2026
  [fetch2] rc 0
  [fetch2] l-si 18cd2b88c98b2d7bf75b4f61941ee8c00ce6b19b
  [fetch2] referee 32d61d6064ff48b23d4cec26972ae6d116653f2b
  [fetch2] referee-2 0f2606da4f44254a17fc5c2dfd9edd46aa8bdddd
  [fetch2] vibrant-johnson-nxvvxo e8b6abf0170fb63ecbd68d058a2bb38599bc5b01
  [fetch2] HEAD 4af9279d8c5e24454851fbace70e993299f6d68e
  [fetch2] ls-remote 18cd2b88c98b2d7bf75b4f61941ee8c00ce6b19b refs/heads/claude/l-si
  [fetch2] ls-remote 32d61d6064ff48b23d4cec26972ae6d116653f2b refs/heads/claude/referee
  [fetch2] ls-remote 0f2606da4f44254a17fc5c2dfd9edd46aa8bdddd refs/heads/claude/referee-2
  [fetch3] Fri Nov 13 03:00:32 UTC 2026
  [fetch3] l-si 18cd2b88c98b2d7bf75b4f61941ee8c00ce6b19b
  [fetch3] referee 32d61d6064ff48b23d4cec26972ae6d116653f2b
  [fetch3] referee-2 adda3245ac31c01f934d990561a0856b632dea71
  [fetch3] vibrant-johnson-nxvvxo e8b6abf0170fb63ecbd68d058a2bb38599bc5b01
  [fetch3] HEAD 4af9279d8c5e24454851fbace70e993299f6d68e
  [fetch3] referee-2 0f2606da..adda3245: adda3245 REFEREE-2 40: handover check (five answers; B waits for REFEREE 34's 32d61d60 on origin; C box 212 pre-read nex; paths: docs/agents/handover-checks/REFEREE-2.md
  [fetch3] R2-P-N5-WRAP.md byte-equal at adda3245 and 01e83df5: yes
  [blk] BOX104 checks: PASS
  [blk] [rc] box104/check104.sh 0
  [blk] PWRAP checks: PASS
  [blk] [rc] pwrap/checkW.sh 0
  [blk] [time] 2026-11-13T02:11:37Z-2026-11-13T02:11:37Z rc 0
  [neg] [neg1] one byte appended to the archive's L-2 (sha1 505a2d0605b807085b96c24e55c218daf3624020):
  [neg] BOX104 checks: PASS
  [neg] [rc] box104/check104.sh 0
  [neg] docs/si/P-N5-WRAP-line-L2.txt: FAILED
  [neg] sha1sum: WARNING: 1 computed checksum did NOT match
  [neg] PWRAP FAIL fixes entry 1 sha1
  [neg] [rc] pwrap/checkW.sh 1
  [neg] [time] 2026-11-13T02:11:45Z-2026-11-13T02:11:46Z rc 1
  [neg] [neg1] rc 1
  [neg] [neg1] restored: dbd5f0e83e3d0300842c46cf2ae24b30b853d784 (cmp equal to the backup: yes)
  [neg] [neg2] one byte prepended to the archive's experiments/si/box104/out/wrap_long.out (a pinned output):
  [neg] BOX104 FAIL wrap long: lmcs fig4 n 7: .* Howard T (own howard) 1142 tie events 0 ¦ .* iterations 1145 
  [neg] [rc] box104/check104.sh 1
  [neg] PWRAP FAIL W^L_7 long
  [neg] [rc] pwrap/checkW.sh 1
  [neg] [time] 2026-11-13T02:11:46Z-2026-11-13T02:11:46Z rc 1
  [neg] [neg2] rc 1
  [neg] [neg2] restored (cmp equal to the backup: yes); blocks re-run:
  [neg] BOX104 checks: PASS
  [neg] [rc] box104/check104.sh 0
  [neg] PWRAP checks: PASS
  [neg] [rc] pwrap/checkW.sh 0
  [neg] [time] 2026-11-13T02:11:46Z-2026-11-13T02:11:46Z rc 0
  [neg] [rerun] rc 0
  [si] xcheck --tiny: PASS
  [si] coarse levcheck (level ∞ sentinel): PASS
  [si] vjfast vs si.py (40 games): PASS
  [si] pinned instances: PASS
  [si] rund (gap lib2o, lenonly_n8): PASS
  [si] rund (OFFSET-ONCE counterexample offret_n23): PASS
  [si] rund (PIECE_D / SPLIT-RED on lib2o): PASS
  [si] rund (INC counterexample incdown_n23): PASS
  [si] rund (LEVEL-COUNT counterexample lcount_n23 (L-RED); LC2 / PAIR-OC on lcount_n23, lcount2_n23, control bites): PASS
  [si] rund (P^c_sch / FRZ-SCH / CHARGE on frz3_n24, shifted-schedule control bites): PASS
  [si] rund (FZ, UNF, OFFUP, U-SPLIT classes on frz1_n24): PASS
  [si] rund (UF-ONCE DEAD: so_th_n32 Even 24 x3, phase2_pk48 Even 44 x2; CHARGE/FZ/UNF/OFFUP 0 violations there): PASS
  [si] rund (ROOT, ROUTE-RELAY on frz40; mutual relay 11 <-> 26 in one phase; MUT=1 bites): PASS
  [si] rund (U-SPLIT DEAD usplit_rd_s3_n27 y=26 z=25 off 0->0; PAIR-OC DEAD pairoc_n58 v=57; LC2 holds there): PASS
  [si] rund (FRZ-RHO data on frz40): PASS
  [si] rund (FLIP on frz40 and pp_K12_n161; MUT=1 bites): PASS
  [si] rund (N3-LEVEL on leanT_N6, tight; MUT=2 bites): PASS
  [si] rund (flip classes on frz40; CHOSEN / RELAY-CHAIN and chosen-terminal pieces on nep90_n40; MUT=1 bites): PASS
  [si] rund (epoch causes on nep90: all clean strict; MUT=1 bites): PASS
  [si] rund (RUND fixes file: all quotes verbatim; shifted control fails): PASS
  [si] rund (packet P-N5-FLIP-box18: all quotes verbatim; shifted control fails): PASS
  [si] rund (P-N5-FLIP fixes file: 23 quotes verbatim; shifted control fails): PASS
  [si] rund (packet P-N5-CHOSEN-box19: 9 quotes verbatim; shifted control fails): PASS
  [si] root (BF-F_D, FREEZE-A pieces, ROOT-PIECE on nep90; three controls bite): PASS
  [si] root (packet P-N5-ROOT-box20: 9 quotes verbatim; shifted control fails): PASS
  [si] root (D-leaves on nep90: 26, no RELAY-and-OWN): PASS
  [si] root (GATE-LAG on nep90: 188 / 948 naive failures; GATE-SHIFT (a), (b) hold): PASS
  [si] root (FREEZE-G (a) on nep90): PASS
  [si] root (packet P-N5-ROOT-add-box20: 11 quotes verbatim; shifted control fails): PASS
  [si] root (per-gate resets on nep90; the dead PING/FLIP charge reproduces): PASS
  [si] rund (P-N5-CHOSEN fixes file: 22 quotes verbatim; shifted control fails): PASS
  [si] root (gcx: G_c, X_u on nep90 and pp_K12; no double migration inside a C-interval there, whole-run control bites): PASS
  [si] root (gcx: UL_C on so_th_n32, control fires; DEAD C-ONCE broad (cone_n65) and UE-ONCE_C (ueonce_n27) reproduce): PASS
  [si] root (absmodel: ABS-HEIGHT on random and climbed DAGs, sharp at n = 5; control fires): PASS
  [si] root (abscyc obstruction instance, FINAL-EACH; absmodel ABS-TIE with ties broken away from the current choice; control fires): PASS
  [si] root (packet P-N5-GCX-box21: 5 quotes verbatim; shifted control fails): PASS
  [si] root (exitx on nep90: MONO-REF, PUSH, EXIT-RHO, DEPTH hold, EXIT 53 / 18; controls MRMUT, PUSHMUT bite): PASS
  [si] root (absdepth: ABS-DEPTH on 2,844 cyclic-model runs; tie instance; control bites): PASS
  [si] root (evenside on nep90: cuts AG 15 / DCH 19 / OSB 38, exits at cuts 31 of 33, E-ONEWAY holds; control bites): PASS
  [si] root (staticdepth: STATIC-DEPTH tight on b6_xs_n24, holds on long121 incl. global C-intervals; control bites): PASS
  [si] root (packet P-N5-DEPTH-box22: 12 quotes verbatim; shifted control fails): PASS
  [si] root (packet P-N5-DEPTH-add-box22: 5 quotes verbatim; shifted control fails): PASS
  [si] root (box 23 ALT: GATE-ONEWAY, FRESH3, TOP-ONCE dead with instances; FRESH3 holds on post31, control bites): PASS
  [si] root (P-N5-ROOT fixes: 36 quotes verbatim; shifted control fails): PASS
  [si] root (box 23 §8: XR-LIN dead on l121reader_n41, run unchanged; six readers raise K 53 -> 73 with the run unchanged): PASS
  [si] root (box 23 §10: SW-LIN dead on swlin_kill_n26, n5b agrees): PASS
  [si] root (box 23 §12: Even reader on long121 clean, 16 switches > base 12): PASS
  [si] root (P-N5-GCX fixes: 29 quotes verbatim; shifted control fails): PASS
  [si] root (box 23 §8: condition (R) holds on both reader instances): PASS
  [si] root (packet P-N5-CORE-box23: 10 quotes verbatim; shifted control fails): PASS
  [si] root (corecheck: P-N5-CORE (C1), (C3), (C4) on nep90; control bites): PASS
  [si] root (P-N5-DEPTH and DEPTH-add fixes: 14 + 20 quotes verbatim; shifted controls fail): PASS
  [si] runlin (box 24: best60_n34 run 60, n5b identical; run49 I_tau empty along its run): PASS
  [si] runlin (box 24 §7: DEAD RUN-LIN, runfam_K10 run 99 > 98, n5b identical, generator reproduces the pin): PASS
  [si] root (P-N5-CORE fixes: 35 quotes verbatim; shifted control fails): PASS
  [si] piece (box 25: STATIC-DEPTH' covers kw25 [0,25] outside R77; frz24 (H3') failure and 2 epochs; MUT=1 bites): PASS
  [si] grun (box 25: GATE-RISE on pftheta34, MUT bites; readers G 9 -> 91 with run 99 fixed, anchors G^K 91, SEG 9; anchor generator reproduces the pin): PASS
  [si] piece (P-N5-SDPRIME frozen sha1; 12 quotes verbatim; shifted control fails): PASS
  [si] grun (P-N5-REL frozen sha1; 17 quotes verbatim; shifted control fails): PASS
  [si] piece (P-N5-SDPRIME fixes: 12 quotes verbatim; shifted control fails): PASS
  [si] grun (P-N5-REL fixes: 12 quotes verbatim; shifted control fails): PASS
  [si] grun (box 25: DEAD L-WAVE, lwkill_n31 gap 37 > 30, n5b identical; L-WAVE' holds there): PASS
  [si] lwp (box 26: lwp_a gap n - 1 kills per-gap LAST-SWITCH, PV-STEP, GAP-DEPTH; SEG-LAST holds there, fails on pieces / runs as controls): PASS
  [si] lwp (box 26: LAST-STEP frontier on lwp_a, MUT bites; cycset_kill_n60 kills CYC-SET, SEG-LAST / SET-STEP hold): PASS
  [si] lwp (box 26: K-REDUCTION holds on cycset_kill_n60's nontrivial part; karena_kill_n71 kills K-ARENA, SEG-LAST holds): PASS
  [si] lwp (box 26: setstep_kill_n71 kills SET-STEP, SEG-LAST holds; WX-ARENA fails on cycset_kill_n60): PASS
  [si] lay (box 27: sink lemmas and WSINK-READY on the box-26 kill pins and lwp_a; MUT=1 (N_t-sinks) bites on each pin): PASS
  [si] lay (box 27: wgrow_kill_n90 kills W-GROW, n5b identical; sink lemmas, H-GROW, SEG-LAST hold): PASS
  [si] lay (box 27: hgrow_kill_n89 kills H-GROW, n5b identical; W-GROW, SINK-GROW, SEG-LAST hold): PASS
  [si] lay (box 27: seglast_kill_n110 kills SEG-LAST and SINK-GROW, reproduced from n5b alone; sink lemmas hold): PASS
  [si] lay (box 27: seglast_kill_n29 kills SEG-LAST, run and segment recomputed from n5b alone): PASS
  [si] lay (box 27: psidrop_kill_n70 kills PSI-DROP, n5b identical; seglast_kill_n29: PSI0 fails at the deadlock, PSI1 drops): PASS
  [si] si (box 28: BND and SUFFIX-COUNT on kill pins and ladder, MUT bites; general (a) dead on wgrow_kill_n90): PASS
  [si] si (box 28: interjoint_kill_n70 kills INTER-JOINT, reproduced from n5b alone): PASS
  [si] si (box 28: growpers_kill_n73 kills GROW-PERSIST; DL-RUN, DL-FIRST, DL-JOINT hold on 13 climb deadlocks, MUT bites): PASS
  [si] si (box 28: L-RED's segcount_kill_n20 / segfam_k3_n29 kill DL-RUN, DL-FIRST, NEWFINAL; DL-SEP, DL-NOCONSEC, FROZEN-COUNT, BND hold): PASS
  [si] si (box 28: dlsep_kill_n70 kills DL-SEP, DL-NOCONSEC, FROZEN-COUNT; 8 deadlocks in one REL segment, reproduced from n5b alone): PASS
  [si] si (box 28: runquad_K8_m30_n192 kills LENE and LEN2; BND, SW-RISE hold; max 15 switches per vertex at n 192): PASS
  [si] si (box 28 §9: COMPOSE and COMPOSE-RUN inequalities hold with their slack on runquad, dlsep_kill_n70, R105 and n110 pins): PASS
  [si] si (box 28: P-N5-COMPOSE quotes verbatim, shifted control fails): PASS
  [si] si (box 28 §12: INHERIT holds on runquad (856 carries) and dlsep_kill_n70): PASS
  [si] si (box 28 §13: carries without reopenings on runquad (121/121) and s3quad_K3_m4 (67/67)): PASS
  [si] si (box 28 §14: R17's Lemma P fails in both frames on runquad with σ̄ constant): PASS
  [si] si (box 29: W-SPLIT/CN-W on runquad, FW-BF on s_elim24_final, W-phase form dead on x135_n59, SETTLE/SETTLE_X kills): PASS
  [si] si (box 29 §7: EPOCH-U holds; TRAP-MONO dead on fbrestart_cex_n12 and lend107_n32): PASS
  [si] si (box 28 fixes: P-N5-COMPOSE unchanged, fixes file present): PASS
  [si] si (box 28 fixes: 19 quote pins exact; mutated quote caught): PASS
  [si] si (box 30: PMON, H-P, TORD, TRAP-FIX, FW-D1 on oneodd_c16 and kw25_n32; HLP control fails; abstract EE best = n_abs): PASS
  [si] si (box 30 §11: gate classes, FW-DG on lend107_n32 and oneodd_c16): PASS
  [si] si (box 31: gap-step Lemma P dead on runfam_K100; GP+, FW-R on ccl_w48_n48; plain W-frame Lemma P control fails): PASS
  [si] si (box 31 §5: R-LIN dead on rlin_cex_n40; FW-R, FW-R′ hold; n5b identical): PASS
  [si] si (box 31 §6: GP*, FW-R* on rlin_cex_n40 and ccl_w48_n48; MUT=all control fails): PASS
  [si] si (box 31 packet P-N5-GP: 14 quotes exact; shifted control fails): PASS
  [si] si (box 32: LATE-BASIN + matching on lend47_n32, lastonly control fails; general R*-TC dead on kt6_n58): PASS
  [si] si (box 32 §5: rounds all class A, prefixes monotone on x31_re24; MUT=rev control fires): PASS
  [si] si (box 32 §6: ROUND-G on x31_re24; distinct climb tops dead on rtt16): PASS
  [si] si (box 33: ODD-FREEZE / SW-RETURN on Odd re-entries; carry-charge, ENT-NM, ENT-PCH dead; LEN-REENTRY; controls fire): PASS
  [si] si (box 34: d_hntop sweeps; CARRY-CLIMB, SWEEP-GAIN dead; CARRY-SEG holds on the kills; control fires): PASS
  [si] si (box 35: Φ_2, Φ_3 dead on fc_3; Φ_2 passes wide_h16; exact weight monotone): PASS
  [si] si (box 36: INHERIT-λ exact, mutation bites; pivot laws dead; switch-all kills RESET-LIN and CARRY-SEG with all generic lemmas holding): PASS
  [si] si (box 36 §5: FG(τ) on switchallexp_7: 142 / 14 iterations, ≤ 1 matched reset per vertex): PASS
  [si] si (box 37: target forms on R120 pins; W-RETURN holds under S4a, mutation and switch-all control fire): PASS
  [si] si (box 38: Lemma SPAN holds; in-window form inflated on tobs, span form not): PASS
  [si] si (box 38 §6: hntop_3 W-window counts): PASS
  [si] si (box 39: span P-changes need not come with W-changes): PASS
  [si] si (box 40: W-RETURN-G and cut-attached re-entries): PASS
  [si] si (box 42: late adoptions FIRST / REPEAT): PASS
  [si] si (box 43: P-N5-CUT quotes, hntop_n3 R* 0): PASS
  [si] si (box 44: repeat cause chains): PASS
  [si] si (box 45: plain-wave and REP-PLAIN kills): PASS
  [si] si (box 46: local late adoptions): PASS
  [si] si (box 47: reader chains): PASS
  [si] si (box 48: window depth): PASS
  [si] si (box 49: P-N5-REPD quotes): PASS
  [si] si (box 50: window DAG): PASS
  [si] si (box 50 §6: tied climbs): PASS
  [si] si (box 51: LATE', GAP-CLIMB, TIED-RB dead): PASS
  [si] si (box 52: TXC descent): PASS
  [si] si (box 53: P-N5-LATEP quotes): PASS
  [si] si (box 50b: FL, FLAT-Z): PASS
  [si] si (box 51b: GATE, INTERVAL-SI, potentials dead): PASS
  [si] si (box 51b §6-§7: DEEP_4 split, REVISIT): PASS
  [si] si (box 51b §8: LAYER-RESET): PASS
  [si] si (box 51b §10: RETURN-CHARGE): PASS
  [si] si (box 51b §11-§12: RETURN-CHARGE', SEG-XCH, charge OFF): PASS
  [si] si (box 51b §13: heads): PASS
  [si] si (box 52: RUN-SETTLE front, Xi-front DEAD, proof cases, defect set, flips): PASS
  [si] si (box 52 §3: FLIP-CAUSE'' DEAD, FLIP-EV data): PASS
  [si] si (box 52: P-N5-SETTLE frozen): PASS
  [si] si (box 52 §3: FLIP-EV DEAD, flipev_n20): PASS
  [si] si (box 53 SBF: fixed-order DEAD, ROOT-FLIP checks): PASS
  [si] si (box 53 SBF §5: ORDER-CHG' data, fixed-set NO-REPEAT DEAD, ¦U¦ linear): PASS
  [si] si (box 53 SBF §2.6 / §6: ONE-STEP-O, XCN-ONE DEAD, KIND-A): PASS
  [si] si (box 53b: LEX-TREE, TREE-STABLE, OVERTAKE, KEYCH <= 1 + INS): PASS
  [si] si (box 53c: CEIL-ACC data): PASS
  [si] si (box 53d: source-free A-flats): PASS
  [si] si (box 54: OLD-PLAY, ODD-STEP, ODD-RELAY; W-rank / ASC-W / TURN-W dead): PASS
  [si] si (box 55: NO-RET search; first-segment releases on hit_b6a_1): PASS
  [si] si (box 56: first-segment re-growth; FUEL-MONO / FUEL-DESC dead): PASS
  [si] si (box 57: FUEL-LEX): PASS
  [si] si (box 58: ANCESTRY): PASS
  [si] si (box 58 s7: repeat escapes): PASS
  [si] si (box 58 s8: W-REOPEN): PASS
  [si] si (box 58 s9: ESC-XCH): PASS
  [si] si (box 58 s10: Odd W-SEP DEAD): PASS
  [si] si (box 58 s11: WCH vs source events): PASS
  [si] si (P-N5-ODD pinned): PASS
  [si] si (P-N5-ODD L-1 pinned): PASS
  [si] si (P-N5-ODD L-2 pinned): PASS
  [si] si (P-N5-ODD L-3 pinned): PASS
  [si] si (P-N5-SETTLE L-1 pinned): PASS
  [si] si (P-N5-SETTLE L-2 pinned): PASS
  [si] si (P-N5-SETTLE L-3 pinned): PASS
  [si] si (P-N5-SETTLE L-4 pinned): PASS
  [si] si (P-N5-SETTLE L-5 pinned): PASS
  [si] si (box 59: W-REOPEN' repaired, WIT, CLOSE-W DEAD): PASS
  [si] si (box 60: KEY-RETURN): PASS
  [si] si (box 61: UNBLOCK-KEY): PASS
  [si] si (box 62: I_tau in tau-stretches, ESC-SQUEEZE): PASS
  [si] si (box 63: S4B-OPT): PASS
  [si] si (P-N5-S4B pinned): PASS
  [si] si (P-N5-S4B L-1 pinned, distinct counts): PASS
  [si] flipdp witnesses + T_inf champions: PASS
  [si] box 64 bitchain: PASS
  [si] box 64 negative control: PASS
  [si] si (box 64: FLIPOR): PASS
  [si] m 1: distinct (transition, b_0) functions over all in-level gate orders: 14
  [si] box 65 gain: PASS
  [si] si (box 65: FOOT): PASS
  [si] box 66 frontier: PASS
  [si] box 66 m 3 pins (Gen replay): PASS
  [si] si (box 66: FRONT): PASS
  [si] box 67 tau table: PASS
  [si] box 67 m 3 pins (Gen replay): PASS
  [si] si (box 67: FRONT2): PASS
  [si] box 68 COMPOSE: PASS
  [si] box 68 m 4 pins: PASS
  [si] si (box 68: REFUTE/COMPOSE): PASS
  [si] box 69 IM mechanism: PASS
  [si] si (box 69: MECH): PASS
  [si] box 70 frame m = 2 validation: PASS
  [si] si (box 70: FRAME): PASS
  [si] box 71 INF-2 kill pin + T_3(3) >= 14 pin: PASS
  [si] input clauses 6996, vars 2003, top-level conflict after input: 0
  [si] lemmas checked 52447, deletion lines 45665 (applied; clauses removed 45665)
  [si] box 71 k-flip frame + DRUP: PASS
  [si] si (box 71: FRAME-K): PASS
  [si] box 73 FRONT-2' + pq_8_1 pin: PASS
  [si] box 73 frame pq controls: PASS
  [si] si (box 73: SUM1): PASS
  [si] box 74 realised flip genomes: PASS
  [si] box 74 frame flips controls: PASS
  [si] si (box 74: FLIPS): PASS
  [si] box 75 P-IDEAL-IM checks + witness + COMPOSE seed 68: PASS
  [si] box 75 certified CNF regenerated: PASS
  [si] si (box 75: P-IDEAL-IM): PASS
  [si] box 76 TROPICAL-WINDOW checks (ALT-MIN, HIT, window tables, DBL-EQ, DBL-GAP data, DEAD SUM-COUPLE / RISE-N / SPAWN-2 replays, box 77 replays + NEG control + PASS-FREEZE + RE-ENTRY): PASS
  [si] si (box 76: TROPICAL-WINDOW): PASS
  [si] box 78 checks (potentials, RANK): PASS
  [si] si (box 78): PASS
  [si] box 79 P-IDEAL-DBL (frozen) checks: PASS
  [si] si (box 79: P-IDEAL-DBL frozen): PASS
  [si] box 80 checks: PASS
  [si] si (box 80: TOWER stretch): PASS
  [si] P-ACYC fix1 checks: PASS
  [si] P-ACYC fix2 checks: PASS
  [si] P-ACYC fix3 checks: PASS
  [si] P-ACYC fix4 checks: PASS
  [si] box 81 checks: PASS
  [si] si (box 81: BRIDGE): PASS
  [si] box 82 checks: PASS
  [si] si (box 82: CYCLIC TOWERS): PASS
  [si] box 83 checks: PASS
  [si] si (box 83: LADDER-R): PASS
  [si] box 84 m2 checks: PASS
  [si] box 84 m3 checks: PASS
  [si] box 84 checks: PASS
  [si] si (box 84: HUB PAIR): PASS
  [si] box 85 checks: PASS
  [si] box 86 checks: PASS
  [si] box 87 checks: PASS
  [si] HPb rebuild: SAME
  [si] box 88 checks: PASS
  [si] box 89 checks: PASS
  [si] BOX90 OK
  [si] BOX91 OK
  [si] BOX92 OK
  [si] BOX93 OK
  [si] BOX94 OK
  [si] P-N5-GATE fix1 checks: PASS
  [si] P-N5-GATE fix2 checks: PASS
  [si] P-N5-GATE fix3 checks: PASS
  [si] P-N5-GATE fix4 checks: PASS
  [si] P-N5-GATE fix5 checks: PASS
  [si] si (P-N5-GATE L-5 pinned): PASS
  [si] BOX96 checks: PASS
  [si] BOX97 checks: PASS
  [si] BOX98 checks: PASS
  [si] BOX99 checks: PASS
  [si] BOX100 checks: PASS
  [si] BOX101 checks: PASS
  [si] BOX102 checks: PASS
  [si] BOX103 checks: PASS
  [si] BOX104 checks: PASS
  [si] BOX105 checks: PASS
  [si] PWRAP checks: PASS
  [si] BOX106 checks: PASS
  [si] [time] 2026-11-13T02:23:36Z-2026-11-13T03:00:05Z rc 0
  [mk] L-1 + LW-1 sha1 be7da8f3a98e4c5a26158eae9aa2766c56531222 3190 B; REFEREE 34's be7da8f3a98e4c5a26158eae9aa2766c56531222: True
  [mk] L-2 sha1 dbd5f0e83e3d0300842c46cf2ae24b30b853d784 3598 B
  [mk] rc 0
  [mk] cmp lane-rebuilt L-2 vs committed (faf0c8ff): EQUAL
  [mk] mk output == committed experiments/si/pwrap/fix1/mkL2.out: True
  [mk] [time] 2026-11-13T02:23:36Z-2026-11-13T02:23:36Z
  [upd] trunk HEAD GAPS sha1 ccf059a1558fc3e1ae769a7aa98506f5fa7d64d5 ; lines 23 ; l. 11 "¦" 76 «UPDATE 2026-» 62
  [upd] (1) control R125: sha1 f22faed54eeafdff59de062b1ed0294e3acb7ec6 = f22faed5…: True ; direct2 equal: True ; filled (2026-11-11, 23:47, 1622c7d9) once on l. 11: True
  [upd] (2) control R126: sha1 89c5f3571a20e19baf3782ffb2534b0ce62a2f68 = 89c5f357…: True ; direct2 equal: True ; filled (2026-11-12, 06:44, 7b2fa753) once on l. 11: True
  [upd] (3) control R127: sha1 5bd83938b1dfb6603581fc98669593ae2e09c83e ; direct2 equal: True ; filled (2026-11-12, 13:58, 850e9765) ends l. 11 before " ¦" (the last UPDATE): True
  [upd]     GAPS at HEAD == at f9520557 == at origin trunk e8b6abf0: True
  [upd] (4) control R128 (draft, not landed): sha1 ba6958119e92cc3ab00cee0348fc69a9e51441b3 = ba695811…: True; == d[545] of docs/agents/R128-draft.md at HEAD (sha1 3f64fcd9…, third fill): True
  [upd] (4b) control R129 (draft, not landed): sha1 31d7b6424542ec7fb7a0684df707c15caa5c5834 = 31d7b642…: True; == d[319] of docs/agents/R129-draft.md at HEAD (sha1 7db9c72d…, second fill): True
  [upd] (4c) direct3 with BND « (2026-11-12) — », no period, no pipe pairs, on R129's L-2 == direct: True
  [upd]     L-2: «¦» 6; «(20» date parentheses 0; « — » 0; ends «).\n»: True; START once: True; BND «; » + «obstruction W-FLAT (» once: True; drops: «; G-N5-TIME stays OPEN» 1, «; not M3 or M4, not a TARGET.md claim» 1; labels once: [1, 1, 1]; «(Corollary NT-RUN)» 1 (stays where L-2 has it)
  [upd]     pipe pair: «(F ≤ m_E − ¦V_E¦ + 1 under [RULE])» in L-2 1 -> «(F ≤ m_E − (the number of Even vertices of H) + 1 under [RULE])»
  [upd]     pipe pair: «so 2^Ω(√¦V¦):» in L-2 1 -> «so 2^Ω(√(the number of vertices)):»
  [upd]     pipe pair: «, ¦V¦ = 10.5n² + 152.5n + 48» in L-2 1 -> «, the number of vertices = 10.5n² + 152.5n + 48»
  [upd] (5) UPDATE from L-2 (landed drops with the line's own scope words, pipe pairs, NO other reading): sha1 no newline 58889da6f0b976ddc49e6ec89b6b3c75a7a133b4; with newline d217fc967e88b791057a1c6260184ad7f9a552d0; 3726 bytes, 3665 chars, 623 tokens; connectors ['; ', '; ']
  [upd]      ( 47 ) 47, depth ok True, ¦ 0, <DATE> 1, <HH:MM> 1, <checker> 1, " — " 0, «G-N5-TIME stays OPEN» 0, «G-N5-TIME stays open.» 1, «not M3» 0, «LANDED:» 1, «pending» 0, «CONDITIONAL» 2, «PROVED lane» 1, «until two referees sign» 1, «L41» 1
  [upd] (6) NEG drop altered ("G-N5-TIME stays OPEN" -> "G-N5-TIME stays Open") : AssertionError '; G-N5-TIME stays OPEN' (expected)
  [upd] (6) NEG label altered ("(Lemma WRAP, PROVED lane)" -> "(Lemma WRAP2, PROVED lane)") : ValueError 'substring not found' (expected)
  [upd] (6) NEG pipe string altered ("¦V_E¦" -> "¦V_O¦") : AssertionError '(F ≤ m_E − ¦V_E¦ + 1 under [RULE])' (expected)
  [upd] (6) NEG one byte of L-2 changed ("T_n + 3 ≥ 2^n + 3" -> "T_n + 4 ≥ 2^n + 3") : builds, sha1 326aecfd89d4f6a536a02bc9aa8f44ceb327677e, == the L-2 UPDATE: False (expected False)
  [upd] (7) token diff L-2 -> UPDATE: 8 hunks, 64 tokens out, 79 in
  [upd]     insert '' -> 'UPDATE <DATE> <HH:MM>Z: RESULTS R130 (P-N5-WRAP; CHECKER C146 <checker>) [refereed-only] LANDED:'
  [upd]     delete '(Lemma WRAP, PROVED lane)' -> ''
  [upd]     replace '¦V_E¦' -> '(the number of Even vertices of H)'
  [upd]     replace "only); (Claim NT: REFEREE successor 33's claim and proof (L41), rendered by L-SI 53)" -> 'only) (Lemma WRAP, PROVED lane);'
  [upd]     replace 'NT-RUN);' -> "NT-RUN) (Claim NT: REFEREE successor 33's claim and proof (L41), rendered by L-SI 53); N5′-xi needs 2^Ω(n) it
  [upd]     replace 'meant) N5′-xi needs 2^Ω(n) iterations on a game with O(n²) vertices, so 2^Ω(√¦V¦): exactly T_n + 3 ≥ 2^n + 3  -> 'meant):'
  [upd]     replace 'affected; G-N5-TIME stays OPEN; not M3 or M4, not a TARGET.md claim' -> 'affected'
  [upd]     insert '' -> 'G-N5-TIME stays open.'
  [upd] (8a) base (a) HEAD: R130 filled UPDATE appended after R127's on l. 11: "¦" 76 -> 76; R130 last: True; R127 < R130: True; prefix byte-unchanged: True
  [upd] (8b) base (b) HEAD + R128 + R129 (draft UPDATEs filled 2099-01-11 00:00 3333333, 2099-01-12 00:00 4444444): R130 appended after R129's: "¦" 76 -> 76; R130 last: True; R127 < R128 < R129 < R130: True; prefix byte-unchanged: True
  [prem] RESULTS @HEAD: sha1 4117c8a7d0165cd8d3a880f9a405d9c6fc6a5089, 16769 lines; last ### R heading R127 (l. 15903)
  [prem] (0) L-2 premise clause «premises [SPEC], [N5XI], [1E-N3] (R57 (b) as landed in R104), Fact DUAL (R104), R15 (a), (c), (d), [RULE] (Remark 3 only)»: 1 time(s) in L-2; «(premises: » in L-2: 0; «…» quotes in L-2: 0
  [prem] (1) every «R<n>» token in L-2 (with context):
  [prem]       R118  "acket for the candidate N5′-xi (RESULTS R118's [N5XI]: SPEC S1-S"
  [prem]       R57   '4-W); premises [SPEC], [N5XI], [1E-N3] (R57 (b) as landed in R1'
  [prem]       R104  ', [N5XI], [1E-N3] (R57 (b) as landed in R104), Fact DUAL (R104),'
  [prem]       R104  '(R57 (b) as landed in R104), Fact DUAL (R104), R15 (a), (c), (d)'
  [prem]       R15   ') as landed in R104), Fact DUAL (R104), R15 (a), (c), (d), [RUL'
  [prem]       R15   ' nodes, so by [F11] Lemmas 5.1, 6.7 and R15 (a) no tie occurs o'
  [prem]       R236  ', W(switchallexp_n) for n ≤ 8; L-RED 66 R236 / R237 (1) (0037d94'
  [prem]       R237  'tchallexp_n) for n ≤ 8; L-RED 66 R236 / R237 (1) (0037d948, 5eca'
  [prem]     «RESULTS R<n>» ids in L-2: [118]; R-ids without «RESULTS » that name RESULTS entries: [15, 57, 104]; L-RED report ids (in «L-RED 66 R236 / R237 (1)»): [236, 237]
  [prem]     R15: landed heading at l. 624: True
  [prem]     R57: landed heading at l. 2893: True
  [prem]     R104: landed heading at l. 9864: True
  [prem]     R118: landed heading at l. 13607: True
  [prem]     R236: a RESULTS heading: False (an L-RED report id, docs/red/R236-*.md)
  [prem]     R237: a RESULTS heading: False (an L-RED report id, docs/red/R237-*.md)
  [prem]     R128 / R129 / R117 tokens in L-2: 0 / 0 / 0 (R128, R129 are NOT landed at HEAD: headings False, False)
  [prem] (2) R118 (l. 13607-13878): {'[N5XI]': 1, 'N5′-xi': 15}
  [prem] (2) R57 (l. 2893-2958): {'(b)': 4, '1E-N3': 5}
  [prem] (2) R104 (l. 9864-10154): {'1E-N3': 14, 'Fact DUAL': 5, 'R57 (b)': 8, 'R24 (a) Lemma R': 7}
  [prem] (2) R15 (l. 624-673): {'(a) Lemma A': 1, '(c) Theorem': 1, '(d) N5': 1}
  [prem] (2) R24 (l. 1064-1112): {'Lemma R': 3}
  [prem] (2) R103 (l. 9641-9863): {'bridge B': 11}
  [prem]     items with count 0: []
  [prem] (3) [1E-N3]: quotes 1 (pieces of nested quotes tested separately)
  [prem] (3) [DUAL]: quotes 2 (pieces of nested quotes tested separately)
  [prem] (3) [R15a], [R15c], [R15d]: quotes 3 (pieces of nested quotes tested separately)
  [prem] (3) [RULE]: quotes 1 (pieces of nested quotes tested separately)
  [prem]     pieces tested 8, not found in their RESULTS entry at HEAD: 0 []
  [prem] (4) [SPEC] docs/new/N5-ssi-global.md at HEAD: 66fde9ef; [N5XI] docs/new/P-N5-XICYC.md at HEAD, «SPEC S1-S5 with ONE change in S4a.»: 1
  [prem] NEGATIVE CONTROL: made-up id R999 landed: False
  [prem] NEGATIVE CONTROL: made-up item "Fact DUAL9" in R104: 0
  [prem] NEGATIVE CONTROL: made-up quote "Lemma A: for any EMPTY set" in R15: 0
  [data] (A) DATA-bearing part of L-2 (from «obstruction W-FLAT» to «… on its own engine.»): chars 1916-3397, 6 top-level clauses (split at «; » outside parentheses):
  [data]   [1] obstruction W-FLAT (τ inert, every option of every Even vertex of H tied in S4a's arena, so the Ξσ-best tie pi … ¦ counters / units named: []
  [data]   [2] frozen instances W(G_n, ι) = WL_1 … WL_4 (11, 29, 65, 137 iterations), W(switchallexp_n) = W_2 … W_8 and F_n = … ¦ counters / units named: ['iterations']
  [data]   [3] DATA (unit: T_n, the steps of Howard's run on G^L_n from ι, = N5′-xi iterations − 3 on W^L_n; experiments/si/b … ¦ counters / units named: ['s3fail', 'nonstd', 'nohoward', 'fbwrong', 'endwrong', 'wrong', 'column T', 'iterations']
  [data]   [4] independent replays, every fail counter 0, their counters in their own pinned outputs, cited, not re-run: L-CO … ¦ counters / units named: ['18 must-be-0 counters', 'fail counter']
  [data]   [5] WRAP's six must-0 counters (s3fail, nonstd, nohoward, fbwrong, endwrong, wrong; units in the packet §9) 0 on 4 … ¦ counters / units named: ['s3fail', 'nonstd', 'nohoward', 'fbwrong', 'endwrong', 'wrong']
  [data]   [6] L-RED 66 R236 / R237 (1) (0037d948, 5eca1c32) on its own engine. … ¦ counters / units named: []
  [data]     clauses naming no counter or unit by name: [1, 6]
  [data] OK   fig4 rows n = 1..8 in wrap_lmcs_xi.out + wrap_long.out: [1, 2, 3, 4, 5, 6, 7, 8] (expected [1, 2, 3, 4, 5, 6, 7, 8])
  [data] OK   column T, n = 1..8: [8, 26, 62, 134, 278, 566, 1142, 2294] (expected [8, 26, 62, 134, 278, 566, 1142, 2294])
  [data] OK   L-2 says «T_n 8, 26, 62, 134, 278, 566, 1,142, 2,294 for n = 1, …, 8»: 1 (expected 1)
  [data] OK   T = 9·2^n − 10 on n = 1..8: True (expected True)
  [data] OK   iterations = T + 3 and ≥ 2^n + 3 on n = 1..8: True (expected True)
  [data] OK   the six counters 0 on the same rows: True (expected True)
  [data] OK   ¦W¦ = 10.5n² + 152.5n + 48 on n = 1..8 (L-2 «¦V¦ = 10.5n² + 152.5n + 48»): True (expected True)
  [data] OK   WL_1..WL_4 iterations (L-2 «(11, 29, 65, 137 iterations)»): [11, 29, 65, 137] (expected [11, 29, 65, 137])
  [data] OK   REFEREE 33 f11_H_fig4.out (e44ce56b) column T, n = 9, 10 (L-2 «4,598, 9,206 for n = 9, 10»): (4598, 9206) (expected (4598, 9206))
  [data] OK   f11_H_fig4.out column T n = 1..8 equals box 104's: [8, 26, 62, 134, 278, 566, 1142, 2294] (expected [8, 26, 62, 134, 278, 566, 1142, 2294])
  [data] OK   W(switchallexp_n) = W_2..W_8 iterations (L-2 «33 … 2,489 iterations = Howard T + 3»): [33, 73, 153, 313, 633, 1246, 2489] (expected [33, 73, 153, 313, 633, 1246, 2489])
  [data] OK   W_n iterations = T + 3, six counters 0, n = 2..8: True (expected True)
  [data] OK   F_2..F_8 iterations in free_xi.out: [33, 73, 153, 313, 633, 1246, 2489] (expected [33, 73, 153, 313, 633, 1246, 2489])
  [data] OK   F_n iterations = Howard T + 3 with 1 fallback: True (expected True)
  [data] OK   N5′-xi random games, six counters 0 (L-2 «4,000 random games for N5′-xi»): 4000 (expected 4000)
  [data] OK   N5 random games, six counters 0 (L-2 «3,000 for N5»): 3000 (expected 3000)
  [data] OK   the frozen 300 (wrap_json.out): six counters 0, rows differing 0: True (expected True)
  [data] OK   L-2 names the six counters, twice: 2 (expected 2)
  [data] OK   frozen instances at l-si 26704e01 inst/SHA1SUMS: ['F_2', 'F_3', 'F_4', 'F_5', 'F_6', 'F_7', 'F_8', 'WL_1', 'WL_2', 'WL_3', 'WL_4', 'W_2', 'W_3', 'W_4', 'W_5', 'W_6', 'W_7', 'W_8'] (expected ['F_2', 'F_3', 'F_4', 'F_5', 'F_6', 'F_7', 'F_8', 'WL_1', 'WL_2', 'WL_3', 'WL_4', 'W_2', 'W_3', 'W_4', 'W_5', 'W_6', 'W_7', 'W_8'])
  [data] OK   inst/ byte-equal at 26704e01 and faf0c8ff: 0 (expected 0)
  [data] OK   LW-2 files exist at faf0c8ff: [True, True, True] (expected [True, True, True])
  [data] OK   REFEREE 33 R-WRAP-preread (90703a81): «523,721» and «18 must-be-0 counters»: (True, True) (expected (True, True))
  [data] OK   cited aa863db5:experiments/comp/box44/README.md exists, «nine must-0 counters» in it: (True, True) (expected (True, True))
  [data] OK   cited 0037d948:docs/red/R236-fn.md exists; 5eca1c32:docs/red/R237-wrap.md exists and names the six counters: (True, True, True) (expected (True, True, True))
  [data] OK   L-RED 68 R237 (2) (3732f4a1) cited in L-2 / in the packet (not to be cited by the entry): (False, False) (expected (False, False))
  [data] 25 checks OK, 0 FAIL; DATA EQUAL
  [data] NEGATIVE CONTROL: claimed T_8 = 2,295: column T gives 2294: caught
  [merge] HEAD 4af9279d; origin trunk e8b6abf0; l-si 18cd2b88; referee 32d61d60; referee-2 0f2606da
  [merge] 26704e01 anc(HEAD) no ; R128 set: anc(l-si 7b0a58ae) yes anc(referee 16e8dcb0) no anc(referee-2 4a6db414) no ; R129 set: anc(referee 28b95151) no anc(referee-2 1177c24d) no ; on origin l-si/referee/referee-2: yes no no 
  [merge] e01447e7 anc(HEAD) no ; R128 set: anc(l-si 7b0a58ae) no anc(referee 16e8dcb0) no anc(referee-2 4a6db414) no ; R129 set: anc(referee 28b95151) no anc(referee-2 1177c24d) no ; on origin l-si/referee/referee-2: yes no no 
  [merge] faf0c8ff anc(HEAD) no ; R128 set: anc(l-si 7b0a58ae) no anc(referee 16e8dcb0) no anc(referee-2 4a6db414) no ; R129 set: anc(referee 28b95151) no anc(referee-2 1177c24d) no ; on origin l-si/referee/referee-2: yes no no 
  [merge] 18cd2b88 anc(HEAD) no ; R128 set: anc(l-si 7b0a58ae) no anc(referee 16e8dcb0) no anc(referee-2 4a6db414) no ; R129 set: anc(referee 28b95151) no anc(referee-2 1177c24d) no ; on origin l-si/referee/referee-2: yes no no 
  [merge] e44ce56b anc(HEAD) no ; R128 set: anc(l-si 7b0a58ae) no anc(referee 16e8dcb0) yes anc(referee-2 4a6db414) no ; R129 set: anc(referee 28b95151) yes anc(referee-2 1177c24d) no ; on origin l-si/referee/referee-2: no yes no 
  [merge] 90703a81 anc(HEAD) no ; R128 set: anc(l-si 7b0a58ae) no anc(referee 16e8dcb0) yes anc(referee-2 4a6db414) no ; R129 set: anc(referee 28b95151) yes anc(referee-2 1177c24d) no ; on origin l-si/referee/referee-2: no yes no 
  [merge] ef4d3bd1 anc(HEAD) no ; R128 set: anc(l-si 7b0a58ae) no anc(referee 16e8dcb0) no anc(referee-2 4a6db414) no ; R129 set: anc(referee 28b95151) yes anc(referee-2 1177c24d) no ; on origin l-si/referee/referee-2: no yes no 
  [merge] c6fcf2b6 anc(HEAD) no ; R128 set: anc(l-si 7b0a58ae) no anc(referee 16e8dcb0) no anc(referee-2 4a6db414) no ; R129 set: anc(referee 28b95151) yes anc(referee-2 1177c24d) no ; on origin l-si/referee/referee-2: no yes no 
  [merge] 99df2458 anc(HEAD) no ; R128 set: anc(l-si 7b0a58ae) no anc(referee 16e8dcb0) no anc(referee-2 4a6db414) no ; R129 set: anc(referee 28b95151) yes anc(referee-2 1177c24d) no ; on origin l-si/referee/referee-2: no yes no 
  [merge] 32d61d60 anc(HEAD) no ; R128 set: anc(l-si 7b0a58ae) no anc(referee 16e8dcb0) no anc(referee-2 4a6db414) no ; R129 set: anc(referee 28b95151) no anc(referee-2 1177c24d) no ; on origin l-si/referee/referee-2: no yes no 
  [merge] 3cf594cc anc(HEAD) no ; R128 set: anc(l-si 7b0a58ae) no anc(referee 16e8dcb0) no anc(referee-2 4a6db414) no ; R129 set: anc(referee 28b95151) no anc(referee-2 1177c24d) yes ; on origin l-si/referee/referee-2: no no yes 
  [merge] 07fd5ae4 anc(HEAD) no ; R128 set: anc(l-si 7b0a58ae) no anc(referee 16e8dcb0) no anc(referee-2 4a6db414) no ; R129 set: anc(referee 28b95151) no anc(referee-2 1177c24d) yes ; on origin l-si/referee/referee-2: no no yes 
  [merge] 5d30968a anc(HEAD) no ; R128 set: anc(l-si 7b0a58ae) no anc(referee 16e8dcb0) no anc(referee-2 4a6db414) no ; R129 set: anc(referee 28b95151) no anc(referee-2 1177c24d) yes ; on origin l-si/referee/referee-2: no no yes 
  [merge] 01e83df5 anc(HEAD) no ; R128 set: anc(l-si 7b0a58ae) no anc(referee 16e8dcb0) no anc(referee-2 4a6db414) no ; R129 set: anc(referee 28b95151) no anc(referee-2 1177c24d) no ; on origin l-si/referee/referee-2: no no yes 
  [merge] 0f2606da anc(HEAD) no ; R128 set: anc(l-si 7b0a58ae) no anc(referee 16e8dcb0) no anc(referee-2 4a6db414) no ; R129 set: anc(referee 28b95151) no anc(referee-2 1177c24d) no ; on origin l-si/referee/referee-2: no no yes 
  [merge] 32d61d60 descends from 28b95151: yes; 0f2606da descends from 01e83df5: yes; l-si 18cd2b88 descends from faf0c8ff: yes
  [merge] paths 28b95151..32d61d60: docs/referee/R-P-N5-WRAP.md docs/referee/scratch/pwrap_l2test.py docs/referee/scratch/pwrap_logs/l2test.out ; 01e83df5..0f2606da: notes/REFEREE-2.md ; faf0c8ff..18cd2b88: docs/agents/handover-checks/L-SI.md 
  [merge] == claude/l-si to faf0c8ff: merge base with HEAD 547985a1; commits not in HEAD: 66; not in the R128/R129 merge 7b0a58ae: 9 (oldest first):
  [merge]   2051a0ee 2026-11-12T18:04:10+00:00 L-SI box 104 Addendum B: gate-face scan on H_n (negative), tie-rule note, N5 against the globally optimizing policy; notebook
  [merge]   516b6837 2026-11-12T18:58:59+00:00 L-SI box 105 lemma section (O2, proof side): KEY(G*), Lemma KEY-MODEL, KEY-MONO*, DEPTH-BOUND*; successor 52 handover
  [merge]   3417f6c1 2026-11-12T19:59:25+00:00 L-SI successor 53 handover check (five questions)
  [merge]   f783aee9 2026-11-12T20:58:02+00:00 L-SI box 104 Addendum C (REFEREE 33's pre-read carried in: W-1..W-4 as Corrections C-1..C-3, Claim NT with proof credited to REFEREE 33, F-1..F-3
  [merge]   e01447e7 2026-11-12T21:08:48+00:00 L-SI packet P-N5-WRAP FROZEN (dead-end packet for N5'-xi: Lemma WRAP proved on W in full incl. core and endgame lemmas; Claim NT (REFEREE 33's cl
  [merge]   d7747b99 2026-11-12T21:59:33+00:00 L-SI box 105 D2: ladder searches (free / E-DOM, d = 2-4; best L* 5/9/14 and 5/10/13), each best genome validated against N5 (six counters 0) and 
  [merge]   ce1225a7 2026-11-12T22:49:37+00:00 L-SI box 106 (exact d = 2 maximum of KEY on the free ladder): statement first (5 <= L*_max(2) <= 8; CONJECTURE KEY2-5; kill and dead-end criteria
  [merge]   4fce46da 2026-11-12T23:38:34+00:00 L-SI box 106 §2a kill search (400 restarts x 5,000 steps with the audited evaluator: max L* 5, 40 bests replayed on N5, counters 0; CONJECTURE K
  [merge]   faf0c8ff 2026-11-13T00:29:35+00:00 L-SI P-N5-WRAP fixes entry 1 + line L-2 by script (REFEREE 34 LW-1 (check stage be7da8f3), REFEREE-2 39 R-1, R-2 on LW-1's clause; adopted LW-2, 
  [merge]   old-style merge-tree 547985a1 HEAD faf0c8ff: rc 0 ; lines 41391 ; conflict markers 0
  [merge]   paths outside the lane's own: docs/agents/handover-checks/L-SI.md 
  [merge] == claude/l-si(head) to 18cd2b88: merge base with HEAD 547985a1; commits not in HEAD: 67; not in the R128/R129 merge 7b0a58ae: 10 (oldest first):
  [merge]   2051a0ee 2026-11-12T18:04:10+00:00 L-SI box 104 Addendum B: gate-face scan on H_n (negative), tie-rule note, N5 against the globally optimizing policy; notebook
  [merge]   516b6837 2026-11-12T18:58:59+00:00 L-SI box 105 lemma section (O2, proof side): KEY(G*), Lemma KEY-MODEL, KEY-MONO*, DEPTH-BOUND*; successor 52 handover
  [merge]   3417f6c1 2026-11-12T19:59:25+00:00 L-SI successor 53 handover check (five questions)
  [merge]   f783aee9 2026-11-12T20:58:02+00:00 L-SI box 104 Addendum C (REFEREE 33's pre-read carried in: W-1..W-4 as Corrections C-1..C-3, Claim NT with proof credited to REFEREE 33, F-1..F-3
  [merge]   e01447e7 2026-11-12T21:08:48+00:00 L-SI packet P-N5-WRAP FROZEN (dead-end packet for N5'-xi: Lemma WRAP proved on W in full incl. core and endgame lemmas; Claim NT (REFEREE 33's cl
  [merge]   d7747b99 2026-11-12T21:59:33+00:00 L-SI box 105 D2: ladder searches (free / E-DOM, d = 2-4; best L* 5/9/14 and 5/10/13), each best genome validated against N5 (six counters 0) and 
  [merge]   ce1225a7 2026-11-12T22:49:37+00:00 L-SI box 106 (exact d = 2 maximum of KEY on the free ladder): statement first (5 <= L*_max(2) <= 8; CONJECTURE KEY2-5; kill and dead-end criteria
  [merge]   4fce46da 2026-11-12T23:38:34+00:00 L-SI box 106 §2a kill search (400 restarts x 5,000 steps with the audited evaluator: max L* 5, 40 bests replayed on N5, counters 0; CONJECTURE K
  [merge]   faf0c8ff 2026-11-13T00:29:35+00:00 L-SI P-N5-WRAP fixes entry 1 + line L-2 by script (REFEREE 34 LW-1 (check stage be7da8f3), REFEREE-2 39 R-1, R-2 on LW-1's clause; adopted LW-2, 
  [merge]   18cd2b88 2026-11-13T01:27:14+00:00 L-SI successor 54 handover check (on faf0c8ff)
  [merge]   old-style merge-tree 547985a1 HEAD 18cd2b88: rc 0 ; lines 41389 ; conflict markers 0
  [merge]   paths outside the lane's own: docs/agents/handover-checks/L-SI.md 
  [merge] == claude/referee to 32d61d60: merge base with HEAD 7fa6aff4; commits not in HEAD: 23; not in the R128/R129 merge 28b95151: 1 (oldest first):
  [merge]   32d61d60 2026-11-13T01:40:40+00:00 REFEREE s34: R-P-N5-WRAP §8: fixes entry 1 CORRECT, line L-2 MATCHES (dbd5f0e8 = L-1 + LW-1 (be7da8f3) + REFEREE-2 R-1 + R-2 on LW-1's clause + 
  [merge]   old-style merge-tree 7fa6aff4 HEAD 32d61d60: rc 0 ; lines 8124 ; conflict markers 0
  [merge]   paths outside the lane's own: docs/agents/handover-checks/REFEREE.md 
  [merge] == claude/referee-2 to 0f2606da: merge base with HEAD 98a64b91; commits not in HEAD: 16; not in the R128/R129 merge 1177c24d: 2 (oldest first):
  [merge]   01e83df5 2026-11-13T01:28:18+00:00 REFEREE-2 39: R2-P-N5-WRAP Addendum 2 — L-2 (l-si faf0c8ff, sha1 dbd5f0e8) MATCHES: own rebuild from L-1 + LW-1 (= be7da8f3) + R-1 + R-2 re-anc
  [merge]   0f2606da 2026-11-13T02:04:44+00:00 REFEREE-2 39: HANDOVER (park at ~580k, Lead 02:05Z): no open items; reports of record with SHAs (B LEVEL, A GATE Add. 6, C WRAP, both L-2 MATCHES
  [merge]   old-style merge-tree 98a64b91 HEAD 0f2606da: rc 0 ; lines 3480 ; conflict markers 0
  [merge]   paths outside the lane's own: docs/agents/handover-checks/REFEREE-2.md 
  [merge] pairwise old-style merge-tree 7b0a58ae faf0c8ff 7b0a58ae: conflict markers 0
  [merge] pairwise old-style merge-tree 547985a1 faf0c8ff 16e8dcb0: conflict markers 0
  [merge] pairwise old-style merge-tree c1e71a25 faf0c8ff 4a6db414: conflict markers 0
  [merge] pairwise old-style merge-tree 42e9c728 faf0c8ff 366a38ab: conflict markers 0
  [merge] pairwise old-style merge-tree 547985a1 faf0c8ff 28b95151: conflict markers 0
  [merge] pairwise old-style merge-tree c1e71a25 faf0c8ff 1177c24d: conflict markers 0
  [merge] pairwise old-style merge-tree 7b0a58ae 18cd2b88 7b0a58ae: conflict markers 0
  [merge] pairwise old-style merge-tree 547985a1 18cd2b88 16e8dcb0: conflict markers 0
  [merge] pairwise old-style merge-tree c1e71a25 18cd2b88 4a6db414: conflict markers 0
  [merge] pairwise old-style merge-tree 42e9c728 18cd2b88 366a38ab: conflict markers 0
  [merge] pairwise old-style merge-tree 547985a1 18cd2b88 28b95151: conflict markers 0
  [merge] pairwise old-style merge-tree c1e71a25 18cd2b88 1177c24d: conflict markers 0
  [merge] pairwise old-style merge-tree 547985a1 32d61d60 7b0a58ae: conflict markers 0
  [merge] pairwise old-style merge-tree 16e8dcb0 32d61d60 16e8dcb0: conflict markers 0
  [merge] pairwise old-style merge-tree 98a64b91 32d61d60 4a6db414: conflict markers 0
  [merge] pairwise old-style merge-tree 621e6b77 32d61d60 366a38ab: conflict markers 0
  [merge] pairwise old-style merge-tree 28b95151 32d61d60 28b95151: conflict markers 0
  [merge] pairwise old-style merge-tree 98a64b91 32d61d60 1177c24d: conflict markers 0
  [merge] pairwise old-style merge-tree c1e71a25 0f2606da 7b0a58ae: conflict markers 0
  [merge] pairwise old-style merge-tree 98a64b91 0f2606da 16e8dcb0: conflict markers 0
  [merge] pairwise old-style merge-tree 4a6db414 0f2606da 4a6db414: conflict markers 0
  [merge] pairwise old-style merge-tree 478d0bd9 0f2606da 366a38ab: conflict markers 0
  [merge] pairwise old-style merge-tree 98a64b91 0f2606da 28b95151: conflict markers 0
  [merge] pairwise old-style merge-tree 1177c24d 0f2606da 1177c24d: conflict markers 0
  [merge] paths changed since merge base with HEAD: 7b0a58ae 426
  [merge] paths changed since merge base with HEAD: 16e8dcb0 213
  [merge] paths changed since merge base with HEAD: 4a6db414 31
  [merge] paths changed since merge base with HEAD: 366a38ab 212
  [merge] paths changed since merge base with HEAD: 28b95151 257
  [merge] paths changed since merge base with HEAD: 1177c24d 38
  [merge] paths changed since merge base with HEAD: faf0c8ff 520
  [merge] paths changed since merge base with HEAD: 18cd2b88 520
  [merge] paths changed since merge base with HEAD: 32d61d60 259
  [merge] paths changed since merge base with HEAD: 0f2606da 40
  [merge] common paths 18cd2b88 ∩ 7b0a58ae: 426 (is 7b0a58ae an ancestor of 18cd2b88, i.e. one lane's lineage: yes)
  [merge] common paths 18cd2b88 ∩ 16e8dcb0: 0 (is 16e8dcb0 an ancestor of 18cd2b88, i.e. one lane's lineage: no)
  [merge] common paths 18cd2b88 ∩ 4a6db414: 0 (is 4a6db414 an ancestor of 18cd2b88, i.e. one lane's lineage: no)
  [merge] common paths 18cd2b88 ∩ 366a38ab: 0 (is 366a38ab an ancestor of 18cd2b88, i.e. one lane's lineage: no)
  [merge] common paths 18cd2b88 ∩ 28b95151: 0 (is 28b95151 an ancestor of 18cd2b88, i.e. one lane's lineage: no)
  [merge] common paths 18cd2b88 ∩ 1177c24d: 0 (is 1177c24d an ancestor of 18cd2b88, i.e. one lane's lineage: no)
  [merge] common paths 32d61d60 ∩ 7b0a58ae: 0 (is 7b0a58ae an ancestor of 32d61d60, i.e. one lane's lineage: no)
  [merge] common paths 32d61d60 ∩ 16e8dcb0: 213 (is 16e8dcb0 an ancestor of 32d61d60, i.e. one lane's lineage: yes)
  [merge] common paths 32d61d60 ∩ 4a6db414: 0 (is 4a6db414 an ancestor of 32d61d60, i.e. one lane's lineage: no)
  [merge] common paths 32d61d60 ∩ 366a38ab: 0 (is 366a38ab an ancestor of 32d61d60, i.e. one lane's lineage: no)
  [merge] common paths 32d61d60 ∩ 28b95151: 257 (is 28b95151 an ancestor of 32d61d60, i.e. one lane's lineage: yes)
  [merge] common paths 32d61d60 ∩ 1177c24d: 0 (is 1177c24d an ancestor of 32d61d60, i.e. one lane's lineage: no)
  [merge] common paths 0f2606da ∩ 7b0a58ae: 0 (is 7b0a58ae an ancestor of 0f2606da, i.e. one lane's lineage: no)
  [merge] common paths 0f2606da ∩ 16e8dcb0: 0 (is 16e8dcb0 an ancestor of 0f2606da, i.e. one lane's lineage: no)
  [merge] common paths 0f2606da ∩ 4a6db414: 31 (is 4a6db414 an ancestor of 0f2606da, i.e. one lane's lineage: yes)
  [merge] common paths 0f2606da ∩ 366a38ab: 0 (is 366a38ab an ancestor of 0f2606da, i.e. one lane's lineage: no)
  [merge] common paths 0f2606da ∩ 28b95151: 0 (is 28b95151 an ancestor of 0f2606da, i.e. one lane's lineage: no)
  [merge] common paths 0f2606da ∩ 1177c24d: 38 (is 1177c24d an ancestor of 0f2606da, i.e. one lane's lineage: yes)
  [merge] cited records (not merged for this entry), ancestors of HEAD: l-comp aa863db5 no, l-red 0037d948 no, l-red 5eca1c32 no; on their origin branches: aa863db5 yes, 0037d948 yes, 5eca1c32 yes; l-si 26704e01 in R128's l-si 7b0a58ae: yes
  [note] Note bullet: file lines 339-347, 1089 chars
  [note]   N-W2 (32d61d60 l. 239-240): once in its report True; «…» once in the Note bullet True; text: Note N-W2 (no change asked): the R-2 sentence follows the cited-replays list after a semic
  [note]   W-L2-1 part 1 (01e83df5 l. 305): once in its report True; «…» once in the Note bullet True; text: The 4,000 / 3,000 / 300 runs are the lane's own (box 104 out/), not an independent replay.
  [note]   W-L2-1 part 2 (01e83df5 l. 306-307): once in its report True; «…» once in the Note bullet True; text: Old (once in L-2): «; WRAP's six must-0 counters (». New: «; and this lane's own runs (box
  [note]   N-W2 says «no change asked»: True; W-L2-1 says «no change required for MATCH»: True
  [note]   W-L2-1 Old «; WRAP's six must-0 counters (» in L-2: 1
  [note]   lane output wrap_rand.out at faf0c8ff: 3 lines, «s3fail 0 nonstd 0 nohoward 0 fbwrong 0 endwrong 0 wrong 0» rows 3, named in the Note bullet: True
  [note]   lane output wrap_json.out at faf0c8ff: 1 lines, «s3fail 0 nonstd 0 nohoward 0 fbwrong 0 endwrong 0 wrong 0» rows 1, named in the Note bullet: True
  [note]   lane output wrap_lmcs_xi.out at faf0c8ff: 12 lines, «s3fail 0 nonstd 0 nohoward 0 fbwrong 0 endwrong 0 wrong 0» rows 12, named in the Note bullet: True
  [note]   lane output wrap_fried_xi.out at faf0c8ff: 5 lines, «s3fail 0 nonstd 0 nohoward 0 fbwrong 0 endwrong 0 wrong 0» rows 5, named in the Note bullet: True
  [note]   lane output wrap_long.out at faf0c8ff: 6 lines, «s3fail 0 nonstd 0 nohoward 0 fbwrong 0 endwrong 0 wrong 0» rows 4, named in the Note bullet: True
  [note]   L-2 «; L-RED 66 R236 / R237 (1)» follows the R-2 sentence (the cited-replays list resumes after it): True
  [note] NEGATIVE CONTROL: a made-up N-W3 note in REFEREE's report: 0
  [chk] model: landed R127 title (HEAD) == «### R127 [refereed-only] » + R127 L-3 + «, CHECKER PASS (docs/checker/C141.md, checker 850e9765)»: True
  [chk] file: sha1 b4fc6697ae0d8a67d7cdbf347e207b9762691513 bytes 59716 lines 397 ends with newline True
  [chk] ### R headings at d[...]: [191]
  [chk] (a) title == prefix + L-2 (no newline) + tail: True ; middle bytes == L-2 bytes without newline: True
  [chk]     title: 3615 chars, 3676 bytes, sha1 671013588f5777a89660a1be9549266b12c4fc16, ( 45 ) 45, min depth 0, final 0, ¦ 6 (L-2's own), fill token 1, ends «AP.md; L-SI successor 53)., CHECKER PASS (docs/checker/C146.md, checker PENDING)»
  [chk] (e) entry block d[191:379] (lines 192-379, 188 lines, sha1 of the joined block 70d523f098aede5477c4feda102e54efd74fd14b, with a final newline 4d5c8e09b6a49408f806e8f9dddf5e41a04fd114); next line blank: True; line after: 'Proposed GAPS line-11 UPDATE (append-onl'
  [chk] (b) fill token in the entry block: 1 ; in the whole file: 1 at lines [192]
  [chk]     «\n**Erratum E-1** (not a result» in the block: False ; line-start «**Erratum» in the file: 0 ; empty lines inside the block: 0 ; block lines starting «### »: 1
  [chk] (e) UPDATE line(s) at d[...]: [396] (line [397])
  [chk]     lines starting «UPDATE » in the file: [397]
  [chk]     GAPS preamble at d[380:396]
  [chk] (c) "¦" in the title: 6 (L-2's 6); in the entry block below the title: 0; in UPDATE: 0; in GAPS preamble: 1 (the quoted « ¦» of the row end); in line 1 + record + flags: 24; in the file: 31
  [chk] (d) UPDATE <DATE> 1 <HH:MM> 1 <checker> 1; head at its start: True
  [chk]     UPDATE = upd130L2.txt: True ; sha1 (no newline) 58889da6f0b976ddc49e6ec89b6b3c75a7a133b4 ; with newline d217fc967e88b791057a1c6260184ad7f9a552d0 ; 3726 bytes ( 47 ) 47
  [chk]     stale grep, entry block minus title (case-insensitive): {'candidate': 10, 'until two referees sign': 1}
  [chk]       'until two referees sign' at file lines: [(300, '  CONDITIONAL until two referees sign» and reco')]
  [chk]     stale grep, title: {'pending': 1, 'candidate': 1, 'until two referees sign': 1, 'proved lane': 1} ; UPDATE: {'candidate': 1, 'until two referees sign': 1, 'proved lane': 1}
  [chk]     R128 / R129 named in the entry block: 1 / 1 (as RESULTS premises: 0 / 0)
  [chk]     line 1 «NOT LANDED» 1 ; «<DATE>» in file 2 ; «<checker>» 2 ; «<HH:MM>» 2 ; tab characters in the file: 0
  [chk] (e) slices: line 1 d[0]; FIRST FILL record d[1:190] (flags d[73:190]; + blank d[190]: ''); title d[191]; entry d[191:379] (Note bullet at d[338]); blank d[379]; preamble d[380:396]; UPDATE d[396]; blank d[397]: ''; Addendum (first fill) none
  [chk] (f) QUOTE SWEEP (corpus: 64 texts), per section
  [chk]     sweep line 1: 1 quotes, 1 parts, 0 not found []
  [chk]     sweep FIRST FILL record and flags: 131 quotes, 125 parts, 0 not found []
  [chk]     sweep entry block: 83 quotes, 102 parts, 0 not found []
  [chk]     sweep GAPS preamble + UPDATE: 14 quotes, 9 parts, 0 not found []
  [chk]     sweep whole file: 229 quotes, 237 parts, 0 not found []
  [chk]     sweep NEGATIVE CONTROL: 1 quotes, 1 parts, 1 not found ['N5′-xi makes polynomially many iterations on W^L_n']
  [chk]     negative control reported missing: True
  [lp] cites 126 (77 shown in the draft as «quote», 49 used for a line number only) in 15 (commit, file) pairs; failed at the cited lines: 0 []
  [lp] shown quotes not in the draft as «quote»: 0 []
  [lp] NEGATIVE CONTROL 1 (window shifted by 40 lines): 0 of 126 still pass []
  [lp] NEGATIVE CONTROL 2 (longest word mutated): 0 of 126 still pass
  [lp]     01e83df5 docs/referee-2/R2-P-N5-WRAP.md 11
  [lp]     07fd5ae4 docs/referee-2/R2-P-N5-WRAP.md 28
  [lp]     32d61d60 docs/referee/R-P-N5-WRAP.md 10
  [lp]     3cf594cc docs/referee-2/R2-P-N5-WRAP.md 6
  [lp]     4af9279d CLAUDE.md 1
  [lp]     4af9279d TARGET.md 2
  [lp]     4af9279d docs/RESULTS.md 1
  [lp]     4af9279d docs/agents/LEAD-STATE.md 2
  [lp]     5d30968a docs/referee-2/R2-P-N5-WRAP.md 1
  [lp]     5eca1c32 docs/red/R237-wrap.md 1
  [lp]     99df2458 docs/referee/R-P-N5-WRAP.md 43
  [lp]     e01447e7 docs/si/P-N5-WRAP.md 8
  [lp]     faf0c8ff docs/si/P-N5-WRAP-fixes.md 6
  [lp]     faf0c8ff docs/si/P-N5-WRAP-line-L2.txt 3
  [lp]     faf0c8ff notes/L-SI.md 3
  [sim] HEAD RESULTS sha1 4117c8a7d0165cd8d3a880f9a405d9c6fc6a5089 lines 16769 "¦" 1477 ; GAPS sha1 ccf059a1558fc3e1ae769a7aa98506f5fa7d64d5 lines 23
  [sim] == base (a) DRY RUN: HEAD 4af9279d as is (R128, R129 absent)
  [sim] [sim a] pure insertion: prefix byte-unchanged True ; suffix byte-unchanged True ; inserted lines 189
  [sim] [sim a] headings after insertion: {'R126': [15726], 'R127': [15903], 'R128': [], 'R129': [], 'R130': [16127], 'E-1': [16316], 'E-2': [16329], 'E-3': [16357], 'Dead': [16388]}
  [sim] [sim a] R130 at l. 16127-16314, blank l. 16315 (''), «**Erratum E-1**» l. 16316; the line before R130: l. 16126 '' (R127's block ends l. 16125)
  [sim] [sim a] order R126 < R127 < R130 < E-1 < E-2 < E-3 < Dead: True
  [sim] [sim a] RESULTS lines 16769 -> 16958 (+189) ; "¦" 1477 -> 1483 (+6 = the title's 6) ; «checker 5555555)» once True ; fill token 0
  [sim] [sim a] ### R1xx headings: 29, R130 the last: True ; RESULTS sha1 after: 6e75a172277f8f7b180b2249ac56ff51fc79b20f
  [sim] [sim a] GAPS: only l. 11 changes True ; lines 23 -> 23 ; l. 11 "¦" 76 -> 76 ; «UPDATE 2026-» 62 -> 62 ; R130 last: True ; after R127's: True ; prefix byte-unchanged: True ; GAPS sha1 after: 44155976ada6f68d08627ed20030d27007eada0e
  [sim] [sim a] GAPS l. 11 order of the last RESULTS UPDATEs: ['R123', 'R124', 'R125', 'R126', 'R127', 'R130']
  [sim] == base (b), the order of record: HEAD + R128 (third-fill block d[282:522], 240 lines; UPDATE ba695811 filled 2099-01-11 00:00 3333333) + R129 (second-fill block d[153:303], 150 lines; UPDATE 31d7b642 filled 2099-01-12 00:00 4444444), each before E-1 and after the previous: RESULTS lines 17161, sha1 6eae20e5670f5d4de54454dd3fa1752f3dbf0225; GAPS sha1 ffaa910bb5385f360dfa3bef4bb9286594b2d813
  [sim] [sim b] pure insertion: prefix byte-unchanged True ; suffix byte-unchanged True ; inserted lines 189
  [sim] [sim b] headings after insertion: {'R126': [15726], 'R127': [15903], 'R128': [16127], 'R129': [16368], 'R130': [16519], 'E-1': [16708], 'E-2': [16721], 'E-3': [16749], 'Dead': [16780]}
  [sim] [sim b] R130 at l. 16519-16706, blank l. 16707 (''), «**Erratum E-1**» l. 16708; the line before R130: l. 16518 '' (R129's block ends l. 16517)
  [sim] [sim b] order R126 < R127 < R128 < R129 < R130 < E-1 < E-2 < E-3 < Dead: True
  [sim] [sim b] RESULTS lines 17161 -> 17350 (+189) ; "¦" 1477 -> 1483 (+6 = the title's 6) ; «checker 5555555)» once True ; fill token 0
  [sim] [sim b] ### R1xx headings: 31, R130 the last: True ; RESULTS sha1 after: 5b611c76b704bd148ca1d4d1d10b89bb23c1d7bd
  [sim] [sim b] GAPS: only l. 11 changes True ; lines 23 -> 23 ; l. 11 "¦" 76 -> 76 ; «UPDATE 2026-» 62 -> 62 ; R130 last: True ; after R129's: True ; prefix byte-unchanged: True ; GAPS sha1 after: 3ea0269bcfec00eb7b313fdde654adcbf0dd458f
  [sim] [sim b] GAPS l. 11 order of the last RESULTS UPDATEs: ['R125', 'R126', 'R127', 'R128', 'R129', 'R130']
  [sim] [sim b] R128 and R129 blocks unchanged in the result: True True ; UPDATEs R127 < R128 < R129 < R130 on l. 11: True
  [sim] fill values used only here: R128 ('2099-01-11', '00:00', '3333333') R129 ('2099-01-12', '00:00', '4444444') R130 ('2099-01-13', '00:00', '5555555')

Addendum (second fill) (subagent, started 2026-11-13T03:02:58Z by date -u; Lead rulings 03:05Z; for the Lead and CHECKER; does not land). Built by
  r130b/fill2.py from the first fill r130a/R130-draft.md (sha1 0885b1ab2956ee0fbdda3593d4c20843e67c6773, 1011 lines, asserted): every change is an
  (old, new) pair or an appended «SECOND FILL:» sentence on one unwrapped unit, old asserted once in its unit, re-wrapped by the first fill's wrap()
  (roundtrip asserted on all 45 units); the changes are in r130b/changes2.json (8), the new quotes in r130b/cites2.json. Nothing in the repository
  was edited, committed, merged or pushed; scripts/push.sh and scripts/verify.sh were not run (scripts/check_docs.py was run in a git archive of
  HEAD, r130b/landed). Checks ran on the pass-1 draft r130b/R130-draft.p1.md (sha1 eef22f39475a89bbc1be937d49f8d5acdb861a0b, 1055 lines), which equals this file
  without this Addendum and its blank line (asserted by mkadd2.py).
CHANGES (tags in changes2.json). L43: ONE new entry bullet, the Lead's text "DATA counters for the cited replay L-RED 66 R236 / R237 (1) …", right
  after the Note bullet, filled by script from docs/red/R237-wrap.md (5eca1c32) and docs/red/R236-fn.md (0037d948); its R237 values re-read from
  R237's outputs (data130b.py). R236: one new flag G-R236 (R236 names no must-0 counter). G0, SHAPE, U, L43, M, B: a «SECOND FILL:» sentence
  appended to flags G-0, G-SHAPE (the Lead's reading, a note for CHECKER and the check_docs.py result), G-U (accepted; the three replacements
  old → new), G-L43, G-MERGE (referee-2 0f2606da) and G-BASE. NOT CHANGED (asserted): line 1, the title (L-2 verbatim), the GAPS preamble, the
  UPDATE (58889da6…, rebuilt equal by upd130b.py), the first-fill Addendum. NOT RE-RUN (objects unchanged at the origin heads, asserted): the
  check.sh blocks, the full experiments/si/check.sh, mkL2.py, prem130a.py and data130a.py of the first fill. The first-fill Addendum's quote
  sweep has 18 misses (6 are L-2's pipe characters printed as ¦; 12 are «…» that open on one tagged output line and close on another: cut-off
  output lines); this Addendum's own sweep has 17 of the same two kinds (5 and 12), from the lines it reproduces (chk130b.py, run on the final file).
  RESTART: a container restart at about 03:04Z stopped this fill after the pass-1 draft and before the final checks (docs_final.out was left
  empty); per the Lead (03:12Z) every step was re-run from fill2.py on, with local trunk HEAD now 626da53c (L55; RESULTS, GAPS, the R128 / R129
  drafts, check_docs.py and TARGET.md byte-equal to 4af9279d, asserted in fill2.py); [fetch0] is the fetch before the restart, [fetch] the one
  after; [docs0] is the check_docs.py pre-check on the first-fill block in an archive of 4af9279d (which fill2.py reads), [docs] the run on this
  draft in an archive of 626da53c. The full experiments/si/check.sh archive run of the first fill (rc 0) is not repeated: its objects are unchanged. Outputs: [fetch0] fetch0.txt, [fetch] fetch.txt, [docs0] docs_first.out, [fill2] fill2.out, [data2] data130b.out, [upd] upd130b.out, [merge] merge2.out, [docs] docs_p1.out, [note] note2.out, [chk] chk_p1.out, [lp] lp_p1.out, [sim] sim_p1.out.
  [fetch0] Fri Nov 13 03:02:57 UTC 2026
  [fetch0] rc 0
  [fetch0] l-si 18cd2b88c98b2d7bf75b4f61941ee8c00ce6b19b
  [fetch0] referee 32d61d6064ff48b23d4cec26972ae6d116653f2b
  [fetch0] referee-2 adda3245ac31c01f934d990561a0856b632dea71
  [fetch0] l-red 50fe432a9d19bc6670bfe4fdea41fe99caa10339
  [fetch0] vibrant-johnson-nxvvxo e8b6abf0170fb63ecbd68d058a2bb38599bc5b01
  [fetch0] HEAD 4af9279d8c5e24454851fbace70e993299f6d68e
  [fetch0] ls-remote 18cd2b88c98b2d7bf75b4f61941ee8c00ce6b19b refs/heads/claude/l-si
  [fetch0] ls-remote 32d61d6064ff48b23d4cec26972ae6d116653f2b refs/heads/claude/referee
  [fetch0] ls-remote adda3245ac31c01f934d990561a0856b632dea71 refs/heads/claude/referee-2
  [fetch0] ls-remote e8b6abf0170fb63ecbd68d058a2bb38599bc5b01 refs/heads/claude/vibrant-johnson-nxvvxo
  [fetch] Fri Nov 13 03:11:59 UTC 2026
  [fetch] rc 0
  [fetch] l-si 18cd2b88c98b2d7bf75b4f61941ee8c00ce6b19b
  [fetch] referee 32d61d6064ff48b23d4cec26972ae6d116653f2b
  [fetch] referee-2 adda3245ac31c01f934d990561a0856b632dea71
  [fetch] l-red 50fe432a9d19bc6670bfe4fdea41fe99caa10339
  [fetch] vibrant-johnson-nxvvxo e8b6abf0170fb63ecbd68d058a2bb38599bc5b01
  [fetch] HEAD 626da53c7c4a7040df26d78726419190303de579
  [fetch] ls-remote 18cd2b88c98b2d7bf75b4f61941ee8c00ce6b19b refs/heads/claude/l-si
  [fetch] ls-remote 32d61d6064ff48b23d4cec26972ae6d116653f2b refs/heads/claude/referee
  [fetch] ls-remote adda3245ac31c01f934d990561a0856b632dea71 refs/heads/claude/referee-2
  [fetch] ls-remote e8b6abf0170fb63ecbd68d058a2bb38599bc5b01 refs/heads/claude/vibrant-johnson-nxvvxo
  [docs0] [docs] archive of HEAD 4af9279d: 48731 files
  [docs0] [docs] (0) control, HEAD as is: check_docs.py rc 0
  [docs0] [docs] (1) base (b): RESULTS sha1 5b611c76b704bd148ca1d4d1d10b89bb23c1d7bd, «### R130 » at l. 16519; GAPS sha1 3ea0269bcfec00eb7b313fdde654adcbf0dd458f
  [docs0] [docs] (1) base (b) = HEAD + R128 + R129 + R130 (the order of record): check_docs.py rc 0
  [docs0] [docs] (2) base (a) = HEAD + R130 (dry run): check_docs.py rc 0
  [docs0] [docs] (3) NEGATIVE CONTROL: base (b) with the R130 title's label removed:
  [docs0]   - RESULTS entry not labelled formalized¦refereed-only: ### R130 DEAD-END packet for the candidate N5′-xi (RESULTS R118's [N5XI]: SPEC S1-S5 with box 190's S4a tie rule), CONDITIONAL until two referees sign: (Lemma WRAP, PROVED lane) for EVERY parity game H and every positional Even strategy s0 of H, the W-flat wrapper W(H, s0) (n + 7·m_E + 6·m_O + n_O + 9 vertices: every edge of H stretched to a 6-edge path through an Odd gate with a pad to an even self-loop c_W above H, an Even valve with an exit to the core K0-K3 (with pads pA, s, q, r), one pe_o pad per Odd vertex; new vertices in wrap104.py's order) makes N5′-xi from SPEC's default start S3 run, at H's Even vertices, a Howard (switch-best, Vöge-Jurdziński values) run of H from s0 and stop after exactly T + 3 iterations with one fallback, and makes N5 stop after exactly F + 2 iterations with one fallback (F ≤ m_E − ¦V_E¦ + 1 under [RULE]); every step proved on W (core lemma K3-W, Odd's reply ODD-W with values stretched by 6, τ fixed TAU-W, the W-flat arena ESC-W, REACH-W, endgame E1-W to E4-W); premises [SPEC], [N5XI], [1E-N3] (R57 (b) as landed in R104), Fact DUAL (R104), R15 (a), (c), (d), [RULE] (Remark 3 only); (Claim NT: REFEREE successor 33's claim and proof (L41), rendered by L-SI 53) in a 1-sink game ([F11] = Friedmann, arXiv 1106.0778v2, §5) every strategy σ with Ξ_ι ⊴ Ξσ gives distinct valuations to distinct nodes, so by [F11] Lemmas 5.1, 6.7 and R15 (a) no tie occurs on Howard's run of G_n (Figure 4's injective priorities, the READING below) from ι and that run is the I^loc run of [F11] Theorem 6.14 (Corollary NT-RUN); (Statement XI-EXP, CONDITIONAL on WRAP and Claim NT being signed, with [F11] Theorem 6.14 cited as published on the READING that Table 4's six priority formulas carry a misprint and Figure 4's priorities are meant) N5′-xi needs 2^Ω(n) iterations on a game with O(n²) vertices, so 2^Ω(√¦V¦): exactly T_n + 3 ≥ 2^n + 3 iterations on W(G_n, ι), ¦V¦ = 10.5n² + 152.5n + 48; obstruction W-FLAT (τ inert, every option of every Even vertex of H tied in S4a's arena, so the Ξσ-best tie pick is Howard's rule on H); frozen instances W(G_n, ι) = WL_1 … WL_4 (11, 29, 65, 137 iterations), W(switchallexp_n) = W_2 … W_8 and F_n = F_2 … F_8 (33 … 2,489 iterations = Howard T + 3; experiments/si/box104/out/wrap_fried_xi.out, wrap_long.out, free_xi.out) at claude/l-si 26704e01 experiments/si/box104/inst (F_n's route FREE-REACH not in this packet); DATA (unit: T_n, the steps of Howard's run on G^L_n from ι, = N5′-xi iterations − 3 on W^L_n; experiments/si/box104/out/wrap_lmcs_xi.out and wrap_long.out, column T, with WRAP's six must-0 counters s3fail, nonstd, nohoward, fbwrong, endwrong, wrong 0 on the same rows): T_n 8, 26, 62, 134, 278, 566, 1,142, 2,294 for n = 1, …, 8 (equal to 9·2^n − 10 on these eight), and 4,598, 9,206 for n = 9, 10 on G^L_n alone (REFEREE 33, claude/referee e44ce56b, docs/referee/scratch/wrap_logs/f11_H_fig4.out, column T); independent replays, every fail counter 0, their counters in their own pinned outputs, cited, not re-run: L-COMP 20 (aa863db5), REFEREE 33 (e44ce56b / 90703a81; its 18 must-be-0 counters, named in its report, 0 on 523,721 runs); WRAP's six must-0 counters (s3fail, nonstd, nohoward, fbwrong, endwrong, wrong; units in the packet §9) 0 on 4,000 random games for N5′-xi, 3,000 for N5, the frozen 300 and W(G_n, ι), W(switchallexp_n) for n ≤ 8; L-RED 66 R236 / R237 (1) (0037d948, 5eca1c32) on its own engine. N5 (SPEC) is not affected; G-N5-TIME stays OPEN; not M3 or M4, not a TARGET.md claim (P-N5-WRAP, docs/si/P-N5-WRAP.md; L-SI successor 53)., CHECKER PASS (docs/checker/C146.md, checker 5555555)
  [docs0] [docs] (3) negative control: check_docs.py rc 1
  [docs0] [docs] restored (cmp equal)
  [docs0] [docs] (1') base (b) re-run after the restore: check_docs.py rc 0
  [fill2] units: record 23, block 22; roundtrip of every unit with the first fill's wrap(): True
  [fill2]   insert L43    new bullet after «Note (both referees, no change asked)»: 1202 chars
  [fill2]   append G0     flag «G-0,»
  [fill2]   append SHAPE  flag «G-SHAPE,»
  [fill2]   append U      flag «G-U,»
  [fill2]   append L43    flag «G-L43,»
  [fill2]   append M      flag «G-MERGE,»
  [fill2]   append B      flag «G-BASE,»
  [fill2]   insert R236   new flag after G-L43
  [fill2] pass-1 second fill: sha1 eef22f39475a89bbc1be937d49f8d5acdb861a0b, 1055 lines; changes 8; new cites 10; title d[226] unchanged; UPDATE d[440] unchanged (58889da6…); first-fill Addendum d[442:1055] byte-unchanged
  [data2] OK   wr237_lmcs_fig4.out: n, T, iterations; six counters 0 on every row: ([(1, 8, 11), (2, 26, 29), (3, 62, 65), (4, 134, 137)], True) (expected ([(1, 8, 11), (2, 26, 29), (3, 62, 65), (4, 134, 137)], True))
  [data2] OK   wr237_lmcs_table4.out: n, T, iterations; six counters 0 on every row: ([(1, 8, 11), (2, 26, 29), (3, 62, 65), (4, 134, 137)], True) (expected ([(1, 8, 11), (2, 26, 29), (3, 62, 65), (4, 134, 137)], True))
  [data2] OK   wr237_json.out: games 300, every counter 0: True (expected True)
  [data2] OK   wr237_ctrl.out: CTRL nohoward on W(switchallexp_2): 660 (expected 660)
  [data2]      R237 report «n = 2, 3 give 33 / 73 …, every counter 0» on W(switchallexp_n): output files with switchallexp rows other than the control: [] (the value is quoted from the report; no separate output file for it at 5eca1c32)
  [data2] OK   R236 f236_free.out (0037d948): F_2..F_8 iterations, fallbacks: [('F_2', 33, 1), ('F_3', 73, 1), ('F_4', 153, 1), ('F_5', 313, 1), ('F_6', 633, 1), ('F_7', 1246, 1), ('F_8', 2489, 1)] (expected [('F_2', 33, 1), ('F_3', 73, 1), ('F_4', 153, 1), ('F_5', 313, 1), ('F_6', 633, 1), ('F_7', 1246, 1), ('F_8', 2489, 1)])
  [data2] OK   R236 f236_free.out: column regfail xi / spec 0 on all seven rows: True (expected True)
  [data2] OK   R236 report names «regfail»: 0 (expected 0)
  [data2] OK   R236 report names a must-0 counter («must-0» in the text): 0 (expected 0)
  [data2] 8 checks OK, 0 FAIL; DATA EQUAL
  [data2] NEGATIVE CONTROL: claimed CTRL nohoward 661: caught
  [upd] trunk HEAD GAPS sha1 ccf059a1558fc3e1ae769a7aa98506f5fa7d64d5 ; lines 23 ; l. 11 "¦" 76 «UPDATE 2026-» 62
  [upd] (1) control R125: sha1 f22faed54eeafdff59de062b1ed0294e3acb7ec6 = f22faed5…: True ; direct2 equal: True ; filled (2026-11-11, 23:47, 1622c7d9) once on l. 11: True
  [upd] (2) control R126: sha1 89c5f3571a20e19baf3782ffb2534b0ce62a2f68 = 89c5f357…: True ; direct2 equal: True ; filled (2026-11-12, 06:44, 7b2fa753) once on l. 11: True
  [upd] (3) control R127: sha1 5bd83938b1dfb6603581fc98669593ae2e09c83e ; direct2 equal: True ; filled (2026-11-12, 13:58, 850e9765) ends l. 11 before " ¦" (the last UPDATE): True
  [upd]     GAPS at HEAD == at f9520557 == at origin trunk e8b6abf0: True
  [upd] (4) control R128 (draft, not landed): sha1 ba6958119e92cc3ab00cee0348fc69a9e51441b3 = ba695811…: True; == d[545] of docs/agents/R128-draft.md at HEAD (sha1 3f64fcd9…, third fill): True
  [upd] (4b) control R129 (draft, not landed): sha1 31d7b6424542ec7fb7a0684df707c15caa5c5834 = 31d7b642…: True; == d[319] of docs/agents/R129-draft.md at HEAD (sha1 7db9c72d…, second fill): True
  [upd] (4c) direct3 with BND « (2026-11-12) — », no period, no pipe pairs, on R129's L-2 == direct: True
  [upd]     L-2: «¦» 6; «(20» date parentheses 0; « — » 0; ends «).\n»: True; START once: True; BND «; » + «obstruction W-FLAT (» once: True; drops: «; G-N5-TIME stays OPEN» 1, «; not M3 or M4, not a TARGET.md claim» 1; labels once: [1, 1, 1]; «(Corollary NT-RUN)» 1 (stays where L-2 has it)
  [upd]     pipe pair: «(F ≤ m_E − ¦V_E¦ + 1 under [RULE])» in L-2 1 -> «(F ≤ m_E − (the number of Even vertices of H) + 1 under [RULE])»
  [upd]     pipe pair: «so 2^Ω(√¦V¦):» in L-2 1 -> «so 2^Ω(√(the number of vertices)):»
  [upd]     pipe pair: «, ¦V¦ = 10.5n² + 152.5n + 48» in L-2 1 -> «, the number of vertices = 10.5n² + 152.5n + 48»
  [upd] (5) UPDATE from L-2 (landed drops with the line's own scope words, pipe pairs, NO other reading): sha1 no newline 58889da6f0b976ddc49e6ec89b6b3c75a7a133b4; with newline d217fc967e88b791057a1c6260184ad7f9a552d0; 3726 bytes, 3665 chars, 623 tokens; connectors ['; ', '; ']
  [upd]      ( 47 ) 47, depth ok True, ¦ 0, <DATE> 1, <HH:MM> 1, <checker> 1, " — " 0, «G-N5-TIME stays OPEN» 0, «G-N5-TIME stays open.» 1, «not M3» 0, «LANDED:» 1, «pending» 0, «CONDITIONAL» 2, «PROVED lane» 1, «until two referees sign» 1, «L41» 1
  [upd] (6) NEG drop altered ("G-N5-TIME stays OPEN" -> "G-N5-TIME stays Open") : AssertionError '; G-N5-TIME stays OPEN' (expected)
  [upd] (6) NEG label altered ("(Lemma WRAP, PROVED lane)" -> "(Lemma WRAP2, PROVED lane)") : ValueError 'substring not found' (expected)
  [upd] (6) NEG pipe string altered ("¦V_E¦" -> "¦V_O¦") : AssertionError '(F ≤ m_E − ¦V_E¦ + 1 under [RULE])' (expected)
  [upd] (6) NEG one byte of L-2 changed ("T_n + 3 ≥ 2^n + 3" -> "T_n + 4 ≥ 2^n + 3") : builds, sha1 326aecfd89d4f6a536a02bc9aa8f44ceb327677e, == the L-2 UPDATE: False (expected False)
  [upd] (7) token diff L-2 -> UPDATE: 8 hunks, 64 tokens out, 79 in
  [upd]     insert '' -> 'UPDATE <DATE> <HH:MM>Z: RESULTS R130 (P-N5-WRAP; CHECKER C146 <checker>) [refereed-only] LANDED:'
  [upd]     delete '(Lemma WRAP, PROVED lane)' -> ''
  [upd]     replace '¦V_E¦' -> '(the number of Even vertices of H)'
  [upd]     replace "only); (Claim NT: REFEREE successor 33's claim and proof (L41), rendered by L-SI 53)" -> 'only) (Lemma WRAP, PROVED lane);'
  [upd]     replace 'NT-RUN);' -> "NT-RUN) (Claim NT: REFEREE successor 33's claim and proof (L41), rendered by L-SI 53); N5′-xi needs 2^Ω(n) it
  [upd]     replace 'meant) N5′-xi needs 2^Ω(n) iterations on a game with O(n²) vertices, so 2^Ω(√¦V¦): exactly T_n + 3 ≥ 2^n + 3  -> 'meant):'
  [upd]     replace 'affected; G-N5-TIME stays OPEN; not M3 or M4, not a TARGET.md claim' -> 'affected'
  [upd]     insert '' -> 'G-N5-TIME stays open.'
  [upd] (8a) base (a) HEAD: R130 filled UPDATE appended after R127's on l. 11: "¦" 76 -> 76; R130 last: True; R127 < R130: True; prefix byte-unchanged: True
  [upd] (8b) base (b) HEAD + R128 + R129 (draft UPDATEs filled 2099-01-11 00:00 3333333, 2099-01-12 00:00 4444444): R130 appended after R129's: "¦" 76 -> 76; R130 last: True; R127 < R128 < R129 < R130: True; prefix byte-unchanged: True
  [upd] (9) UPDATE unchanged from the first fill (58889da6…): True
  [merge] HEAD 626da53c; origin trunk e8b6abf0; l-si 18cd2b88; referee 32d61d60; referee-2 adda3245
  [merge] 26704e01 anc(HEAD) no ; R128 set: anc(l-si 7b0a58ae) yes anc(referee 16e8dcb0) no anc(referee-2 4a6db414) no ; R129 set: anc(referee 28b95151) no anc(referee-2 1177c24d) no ; on origin l-si/referee/referee-2: yes no no 
  [merge] e01447e7 anc(HEAD) no ; R128 set: anc(l-si 7b0a58ae) no anc(referee 16e8dcb0) no anc(referee-2 4a6db414) no ; R129 set: anc(referee 28b95151) no anc(referee-2 1177c24d) no ; on origin l-si/referee/referee-2: yes no no 
  [merge] faf0c8ff anc(HEAD) no ; R128 set: anc(l-si 7b0a58ae) no anc(referee 16e8dcb0) no anc(referee-2 4a6db414) no ; R129 set: anc(referee 28b95151) no anc(referee-2 1177c24d) no ; on origin l-si/referee/referee-2: yes no no 
  [merge] 18cd2b88 anc(HEAD) no ; R128 set: anc(l-si 7b0a58ae) no anc(referee 16e8dcb0) no anc(referee-2 4a6db414) no ; R129 set: anc(referee 28b95151) no anc(referee-2 1177c24d) no ; on origin l-si/referee/referee-2: yes no no 
  [merge] e44ce56b anc(HEAD) no ; R128 set: anc(l-si 7b0a58ae) no anc(referee 16e8dcb0) yes anc(referee-2 4a6db414) no ; R129 set: anc(referee 28b95151) yes anc(referee-2 1177c24d) no ; on origin l-si/referee/referee-2: no yes no 
  [merge] 90703a81 anc(HEAD) no ; R128 set: anc(l-si 7b0a58ae) no anc(referee 16e8dcb0) yes anc(referee-2 4a6db414) no ; R129 set: anc(referee 28b95151) yes anc(referee-2 1177c24d) no ; on origin l-si/referee/referee-2: no yes no 
  [merge] ef4d3bd1 anc(HEAD) no ; R128 set: anc(l-si 7b0a58ae) no anc(referee 16e8dcb0) no anc(referee-2 4a6db414) no ; R129 set: anc(referee 28b95151) yes anc(referee-2 1177c24d) no ; on origin l-si/referee/referee-2: no yes no 
  [merge] c6fcf2b6 anc(HEAD) no ; R128 set: anc(l-si 7b0a58ae) no anc(referee 16e8dcb0) no anc(referee-2 4a6db414) no ; R129 set: anc(referee 28b95151) yes anc(referee-2 1177c24d) no ; on origin l-si/referee/referee-2: no yes no 
  [merge] 99df2458 anc(HEAD) no ; R128 set: anc(l-si 7b0a58ae) no anc(referee 16e8dcb0) no anc(referee-2 4a6db414) no ; R129 set: anc(referee 28b95151) yes anc(referee-2 1177c24d) no ; on origin l-si/referee/referee-2: no yes no 
  [merge] 32d61d60 anc(HEAD) no ; R128 set: anc(l-si 7b0a58ae) no anc(referee 16e8dcb0) no anc(referee-2 4a6db414) no ; R129 set: anc(referee 28b95151) no anc(referee-2 1177c24d) no ; on origin l-si/referee/referee-2: no yes no 
  [merge] 3cf594cc anc(HEAD) no ; R128 set: anc(l-si 7b0a58ae) no anc(referee 16e8dcb0) no anc(referee-2 4a6db414) no ; R129 set: anc(referee 28b95151) no anc(referee-2 1177c24d) yes ; on origin l-si/referee/referee-2: no no yes 
  [merge] 07fd5ae4 anc(HEAD) no ; R128 set: anc(l-si 7b0a58ae) no anc(referee 16e8dcb0) no anc(referee-2 4a6db414) no ; R129 set: anc(referee 28b95151) no anc(referee-2 1177c24d) yes ; on origin l-si/referee/referee-2: no no yes 
  [merge] 5d30968a anc(HEAD) no ; R128 set: anc(l-si 7b0a58ae) no anc(referee 16e8dcb0) no anc(referee-2 4a6db414) no ; R129 set: anc(referee 28b95151) no anc(referee-2 1177c24d) yes ; on origin l-si/referee/referee-2: no no yes 
  [merge] 01e83df5 anc(HEAD) no ; R128 set: anc(l-si 7b0a58ae) no anc(referee 16e8dcb0) no anc(referee-2 4a6db414) no ; R129 set: anc(referee 28b95151) no anc(referee-2 1177c24d) no ; on origin l-si/referee/referee-2: no no yes 
  [merge] 0f2606da anc(HEAD) no ; R128 set: anc(l-si 7b0a58ae) no anc(referee 16e8dcb0) no anc(referee-2 4a6db414) no ; R129 set: anc(referee 28b95151) no anc(referee-2 1177c24d) no ; on origin l-si/referee/referee-2: no no yes 
  [merge] 32d61d60 descends from 28b95151: yes; 0f2606da descends from 01e83df5: yes; l-si 18cd2b88 descends from faf0c8ff: yes
  [merge] paths 28b95151..32d61d60: docs/referee/R-P-N5-WRAP.md docs/referee/scratch/pwrap_l2test.py docs/referee/scratch/pwrap_logs/l2test.out ; 01e83df5..0f2606da: notes/REFEREE-2.md ; faf0c8ff..18cd2b88: docs/agents/handover-checks/L-SI.md 
  [merge] == claude/l-si to faf0c8ff: merge base with HEAD 547985a1; commits not in HEAD: 66; not in the R128/R129 merge 7b0a58ae: 9 (oldest first):
  [merge]   2051a0ee 2026-11-12T18:04:10+00:00 L-SI box 104 Addendum B: gate-face scan on H_n (negative), tie-rule note, N5 against the globally optimizing policy; notebook
  [merge]   516b6837 2026-11-12T18:58:59+00:00 L-SI box 105 lemma section (O2, proof side): KEY(G*), Lemma KEY-MODEL, KEY-MONO*, DEPTH-BOUND*; successor 52 handover
  [merge]   3417f6c1 2026-11-12T19:59:25+00:00 L-SI successor 53 handover check (five questions)
  [merge]   f783aee9 2026-11-12T20:58:02+00:00 L-SI box 104 Addendum C (REFEREE 33's pre-read carried in: W-1..W-4 as Corrections C-1..C-3, Claim NT with proof credited to REFEREE 33, F-1..F-3
  [merge]   e01447e7 2026-11-12T21:08:48+00:00 L-SI packet P-N5-WRAP FROZEN (dead-end packet for N5'-xi: Lemma WRAP proved on W in full incl. core and endgame lemmas; Claim NT (REFEREE 33's cl
  [merge]   d7747b99 2026-11-12T21:59:33+00:00 L-SI box 105 D2: ladder searches (free / E-DOM, d = 2-4; best L* 5/9/14 and 5/10/13), each best genome validated against N5 (six counters 0) and 
  [merge]   ce1225a7 2026-11-12T22:49:37+00:00 L-SI box 106 (exact d = 2 maximum of KEY on the free ladder): statement first (5 <= L*_max(2) <= 8; CONJECTURE KEY2-5; kill and dead-end criteria
  [merge]   4fce46da 2026-11-12T23:38:34+00:00 L-SI box 106 §2a kill search (400 restarts x 5,000 steps with the audited evaluator: max L* 5, 40 bests replayed on N5, counters 0; CONJECTURE K
  [merge]   faf0c8ff 2026-11-13T00:29:35+00:00 L-SI P-N5-WRAP fixes entry 1 + line L-2 by script (REFEREE 34 LW-1 (check stage be7da8f3), REFEREE-2 39 R-1, R-2 on LW-1's clause; adopted LW-2, 
  [merge]   old-style merge-tree 547985a1 HEAD faf0c8ff: rc 0 ; lines 41391 ; conflict markers 0
  [merge]   paths outside the lane's own: docs/agents/handover-checks/L-SI.md 
  [merge] == claude/l-si(head) to 18cd2b88: merge base with HEAD 547985a1; commits not in HEAD: 67; not in the R128/R129 merge 7b0a58ae: 10 (oldest first):
  [merge]   2051a0ee 2026-11-12T18:04:10+00:00 L-SI box 104 Addendum B: gate-face scan on H_n (negative), tie-rule note, N5 against the globally optimizing policy; notebook
  [merge]   516b6837 2026-11-12T18:58:59+00:00 L-SI box 105 lemma section (O2, proof side): KEY(G*), Lemma KEY-MODEL, KEY-MONO*, DEPTH-BOUND*; successor 52 handover
  [merge]   3417f6c1 2026-11-12T19:59:25+00:00 L-SI successor 53 handover check (five questions)
  [merge]   f783aee9 2026-11-12T20:58:02+00:00 L-SI box 104 Addendum C (REFEREE 33's pre-read carried in: W-1..W-4 as Corrections C-1..C-3, Claim NT with proof credited to REFEREE 33, F-1..F-3
  [merge]   e01447e7 2026-11-12T21:08:48+00:00 L-SI packet P-N5-WRAP FROZEN (dead-end packet for N5'-xi: Lemma WRAP proved on W in full incl. core and endgame lemmas; Claim NT (REFEREE 33's cl
  [merge]   d7747b99 2026-11-12T21:59:33+00:00 L-SI box 105 D2: ladder searches (free / E-DOM, d = 2-4; best L* 5/9/14 and 5/10/13), each best genome validated against N5 (six counters 0) and 
  [merge]   ce1225a7 2026-11-12T22:49:37+00:00 L-SI box 106 (exact d = 2 maximum of KEY on the free ladder): statement first (5 <= L*_max(2) <= 8; CONJECTURE KEY2-5; kill and dead-end criteria
  [merge]   4fce46da 2026-11-12T23:38:34+00:00 L-SI box 106 §2a kill search (400 restarts x 5,000 steps with the audited evaluator: max L* 5, 40 bests replayed on N5, counters 0; CONJECTURE K
  [merge]   faf0c8ff 2026-11-13T00:29:35+00:00 L-SI P-N5-WRAP fixes entry 1 + line L-2 by script (REFEREE 34 LW-1 (check stage be7da8f3), REFEREE-2 39 R-1, R-2 on LW-1's clause; adopted LW-2, 
  [merge]   18cd2b88 2026-11-13T01:27:14+00:00 L-SI successor 54 handover check (on faf0c8ff)
  [merge]   old-style merge-tree 547985a1 HEAD 18cd2b88: rc 0 ; lines 41389 ; conflict markers 0
  [merge]   paths outside the lane's own: docs/agents/handover-checks/L-SI.md 
  [merge] == claude/referee to 32d61d60: merge base with HEAD 7fa6aff4; commits not in HEAD: 23; not in the R128/R129 merge 28b95151: 1 (oldest first):
  [merge]   32d61d60 2026-11-13T01:40:40+00:00 REFEREE s34: R-P-N5-WRAP §8: fixes entry 1 CORRECT, line L-2 MATCHES (dbd5f0e8 = L-1 + LW-1 (be7da8f3) + REFEREE-2 R-1 + R-2 on LW-1's clause + 
  [merge]   old-style merge-tree 7fa6aff4 HEAD 32d61d60: rc 0 ; lines 8124 ; conflict markers 0
  [merge]   paths outside the lane's own: docs/agents/handover-checks/REFEREE.md 
  [merge] == claude/referee-2 to 0f2606da: merge base with HEAD 98a64b91; commits not in HEAD: 16; not in the R128/R129 merge 1177c24d: 2 (oldest first):
  [merge]   01e83df5 2026-11-13T01:28:18+00:00 REFEREE-2 39: R2-P-N5-WRAP Addendum 2 — L-2 (l-si faf0c8ff, sha1 dbd5f0e8) MATCHES: own rebuild from L-1 + LW-1 (= be7da8f3) + R-1 + R-2 re-anc
  [merge]   0f2606da 2026-11-13T02:04:44+00:00 REFEREE-2 39: HANDOVER (park at ~580k, Lead 02:05Z): no open items; reports of record with SHAs (B LEVEL, A GATE Add. 6, C WRAP, both L-2 MATCHES
  [merge]   old-style merge-tree 98a64b91 HEAD 0f2606da: rc 0 ; lines 3480 ; conflict markers 0
  [merge]   paths outside the lane's own: docs/agents/handover-checks/REFEREE-2.md 
  [merge] pairwise old-style merge-tree 7b0a58ae faf0c8ff 7b0a58ae: conflict markers 0
  [merge] pairwise old-style merge-tree 547985a1 faf0c8ff 16e8dcb0: conflict markers 0
  [merge] pairwise old-style merge-tree c1e71a25 faf0c8ff 4a6db414: conflict markers 0
  [merge] pairwise old-style merge-tree 42e9c728 faf0c8ff 366a38ab: conflict markers 0
  [merge] pairwise old-style merge-tree 547985a1 faf0c8ff 28b95151: conflict markers 0
  [merge] pairwise old-style merge-tree c1e71a25 faf0c8ff 1177c24d: conflict markers 0
  [merge] pairwise old-style merge-tree 7b0a58ae 18cd2b88 7b0a58ae: conflict markers 0
  [merge] pairwise old-style merge-tree 547985a1 18cd2b88 16e8dcb0: conflict markers 0
  [merge] pairwise old-style merge-tree c1e71a25 18cd2b88 4a6db414: conflict markers 0
  [merge] pairwise old-style merge-tree 42e9c728 18cd2b88 366a38ab: conflict markers 0
  [merge] pairwise old-style merge-tree 547985a1 18cd2b88 28b95151: conflict markers 0
  [merge] pairwise old-style merge-tree c1e71a25 18cd2b88 1177c24d: conflict markers 0
  [merge] pairwise old-style merge-tree 547985a1 32d61d60 7b0a58ae: conflict markers 0
  [merge] pairwise old-style merge-tree 16e8dcb0 32d61d60 16e8dcb0: conflict markers 0
  [merge] pairwise old-style merge-tree 98a64b91 32d61d60 4a6db414: conflict markers 0
  [merge] pairwise old-style merge-tree 621e6b77 32d61d60 366a38ab: conflict markers 0
  [merge] pairwise old-style merge-tree 28b95151 32d61d60 28b95151: conflict markers 0
  [merge] pairwise old-style merge-tree 98a64b91 32d61d60 1177c24d: conflict markers 0
  [merge] pairwise old-style merge-tree c1e71a25 0f2606da 7b0a58ae: conflict markers 0
  [merge] pairwise old-style merge-tree 98a64b91 0f2606da 16e8dcb0: conflict markers 0
  [merge] pairwise old-style merge-tree 4a6db414 0f2606da 4a6db414: conflict markers 0
  [merge] pairwise old-style merge-tree 478d0bd9 0f2606da 366a38ab: conflict markers 0
  [merge] pairwise old-style merge-tree 98a64b91 0f2606da 28b95151: conflict markers 0
  [merge] pairwise old-style merge-tree 1177c24d 0f2606da 1177c24d: conflict markers 0
  [merge] paths changed since merge base with HEAD: 7b0a58ae 426
  [merge] paths changed since merge base with HEAD: 16e8dcb0 213
  [merge] paths changed since merge base with HEAD: 4a6db414 31
  [merge] paths changed since merge base with HEAD: 366a38ab 212
  [merge] paths changed since merge base with HEAD: 28b95151 257
  [merge] paths changed since merge base with HEAD: 1177c24d 38
  [merge] paths changed since merge base with HEAD: faf0c8ff 520
  [merge] paths changed since merge base with HEAD: 18cd2b88 520
  [merge] paths changed since merge base with HEAD: 32d61d60 259
  [merge] paths changed since merge base with HEAD: 0f2606da 40
  [merge] common paths 18cd2b88 ∩ 7b0a58ae: 426 (is 7b0a58ae an ancestor of 18cd2b88, i.e. one lane's lineage: yes)
  [merge] common paths 18cd2b88 ∩ 16e8dcb0: 0 (is 16e8dcb0 an ancestor of 18cd2b88, i.e. one lane's lineage: no)
  [merge] common paths 18cd2b88 ∩ 4a6db414: 0 (is 4a6db414 an ancestor of 18cd2b88, i.e. one lane's lineage: no)
  [merge] common paths 18cd2b88 ∩ 366a38ab: 0 (is 366a38ab an ancestor of 18cd2b88, i.e. one lane's lineage: no)
  [merge] common paths 18cd2b88 ∩ 28b95151: 0 (is 28b95151 an ancestor of 18cd2b88, i.e. one lane's lineage: no)
  [merge] common paths 18cd2b88 ∩ 1177c24d: 0 (is 1177c24d an ancestor of 18cd2b88, i.e. one lane's lineage: no)
  [merge] common paths 32d61d60 ∩ 7b0a58ae: 0 (is 7b0a58ae an ancestor of 32d61d60, i.e. one lane's lineage: no)
  [merge] common paths 32d61d60 ∩ 16e8dcb0: 213 (is 16e8dcb0 an ancestor of 32d61d60, i.e. one lane's lineage: yes)
  [merge] common paths 32d61d60 ∩ 4a6db414: 0 (is 4a6db414 an ancestor of 32d61d60, i.e. one lane's lineage: no)
  [merge] common paths 32d61d60 ∩ 366a38ab: 0 (is 366a38ab an ancestor of 32d61d60, i.e. one lane's lineage: no)
  [merge] common paths 32d61d60 ∩ 28b95151: 257 (is 28b95151 an ancestor of 32d61d60, i.e. one lane's lineage: yes)
  [merge] common paths 32d61d60 ∩ 1177c24d: 0 (is 1177c24d an ancestor of 32d61d60, i.e. one lane's lineage: no)
  [merge] common paths 0f2606da ∩ 7b0a58ae: 0 (is 7b0a58ae an ancestor of 0f2606da, i.e. one lane's lineage: no)
  [merge] common paths 0f2606da ∩ 16e8dcb0: 0 (is 16e8dcb0 an ancestor of 0f2606da, i.e. one lane's lineage: no)
  [merge] common paths 0f2606da ∩ 4a6db414: 31 (is 4a6db414 an ancestor of 0f2606da, i.e. one lane's lineage: yes)
  [merge] common paths 0f2606da ∩ 366a38ab: 0 (is 366a38ab an ancestor of 0f2606da, i.e. one lane's lineage: no)
  [merge] common paths 0f2606da ∩ 28b95151: 0 (is 28b95151 an ancestor of 0f2606da, i.e. one lane's lineage: no)
  [merge] common paths 0f2606da ∩ 1177c24d: 38 (is 1177c24d an ancestor of 0f2606da, i.e. one lane's lineage: yes)
  [merge] cited records (not merged for this entry), ancestors of HEAD: l-comp aa863db5 no, l-red 0037d948 no, l-red 5eca1c32 no; on their origin branches: aa863db5 yes, 0037d948 yes, 5eca1c32 yes; l-si 26704e01 in R128's l-si 7b0a58ae: yes
  [docs] archive of HEAD 626da53c: 48731 files
  [docs] (0) control, HEAD as is: check_docs.py rc 0
  [docs] (1) base (b): RESULTS sha1 6f9dd60b713a0e9ea35e24c170d9612083ebe4a5, «### R130 » at l. 16519; GAPS sha1 3ea0269bcfec00eb7b313fdde654adcbf0dd458f
  [docs] (1) base (b) = HEAD + R128 + R129 + R130 (the order of record): check_docs.py rc 0
  [docs] (2) base (a) = HEAD + R130 (dry run): check_docs.py rc 0
  [docs] (3) NEGATIVE CONTROL: base (b) with the R130 title's label removed:
  [docs]   - RESULTS entry not labelled formalized¦refereed-only: ### R130 DEAD-END packet for the candidate N5′-xi (RESULTS R118's [N5XI]: SPEC S1-S5 with box 190's S4a tie rule), CONDITIONAL until two referees sign: (Lemma WRAP, PROVED lane) for EVERY parity game H and every positional Even strategy s0 of H, the W-flat wrapper W(H, s0) (n + 7·m_E + 6·m_O + n_O + 9 vertices: every edge of H stretched to a 6-edge path through an Odd gate with a pad to an even self-loop c_W above H, an Even valve with an exit to the core K0-K3 (with pads pA, s, q, r), one pe_o pad per Odd vertex; new vertices in wrap104.py's order) makes N5′-xi from SPEC's default start S3 run, at H's Even vertices, a Howard (switch-best, Vöge-Jurdziński values) run of H from s0 and stop after exactly T + 3 iterations with one fallback, and makes N5 stop after exactly F + 2 iterations with one fallback (F ≤ m_E − ¦V_E¦ + 1 under [RULE]); every step proved on W (core lemma K3-W, Odd's reply ODD-W with values stretched by 6, τ fixed TAU-W, the W-flat arena ESC-W, REACH-W, endgame E1-W to E4-W); premises [SPEC], [N5XI], [1E-N3] (R57 (b) as landed in R104), Fact DUAL (R104), R15 (a), (c), (d), [RULE] (Remark 3 only); (Claim NT: REFEREE successor 33's claim and proof (L41), rendered by L-SI 53) in a 1-sink game ([F11] = Friedmann, arXiv 1106.0778v2, §5) every strategy σ with Ξ_ι ⊴ Ξσ gives distinct valuations to distinct nodes, so by [F11] Lemmas 5.1, 6.7 and R15 (a) no tie occurs on Howard's run of G_n (Figure 4's injective priorities, the READING below) from ι and that run is the I^loc run of [F11] Theorem 6.14 (Corollary NT-RUN); (Statement XI-EXP, CONDITIONAL on WRAP and Claim NT being signed, with [F11] Theorem 6.14 cited as published on the READING that Table 4's six priority formulas carry a misprint and Figure 4's priorities are meant) N5′-xi needs 2^Ω(n) iterations on a game with O(n²) vertices, so 2^Ω(√¦V¦): exactly T_n + 3 ≥ 2^n + 3 iterations on W(G_n, ι), ¦V¦ = 10.5n² + 152.5n + 48; obstruction W-FLAT (τ inert, every option of every Even vertex of H tied in S4a's arena, so the Ξσ-best tie pick is Howard's rule on H); frozen instances W(G_n, ι) = WL_1 … WL_4 (11, 29, 65, 137 iterations), W(switchallexp_n) = W_2 … W_8 and F_n = F_2 … F_8 (33 … 2,489 iterations = Howard T + 3; experiments/si/box104/out/wrap_fried_xi.out, wrap_long.out, free_xi.out) at claude/l-si 26704e01 experiments/si/box104/inst (F_n's route FREE-REACH not in this packet); DATA (unit: T_n, the steps of Howard's run on G^L_n from ι, = N5′-xi iterations − 3 on W^L_n; experiments/si/box104/out/wrap_lmcs_xi.out and wrap_long.out, column T, with WRAP's six must-0 counters s3fail, nonstd, nohoward, fbwrong, endwrong, wrong 0 on the same rows): T_n 8, 26, 62, 134, 278, 566, 1,142, 2,294 for n = 1, …, 8 (equal to 9·2^n − 10 on these eight), and 4,598, 9,206 for n = 9, 10 on G^L_n alone (REFEREE 33, claude/referee e44ce56b, docs/referee/scratch/wrap_logs/f11_H_fig4.out, column T); independent replays, every fail counter 0, their counters in their own pinned outputs, cited, not re-run: L-COMP 20 (aa863db5), REFEREE 33 (e44ce56b / 90703a81; its 18 must-be-0 counters, named in its report, 0 on 523,721 runs); WRAP's six must-0 counters (s3fail, nonstd, nohoward, fbwrong, endwrong, wrong; units in the packet §9) 0 on 4,000 random games for N5′-xi, 3,000 for N5, the frozen 300 and W(G_n, ι), W(switchallexp_n) for n ≤ 8; L-RED 66 R236 / R237 (1) (0037d948, 5eca1c32) on its own engine. N5 (SPEC) is not affected; G-N5-TIME stays OPEN; not M3 or M4, not a TARGET.md claim (P-N5-WRAP, docs/si/P-N5-WRAP.md; L-SI successor 53)., CHECKER PASS (docs/checker/C146.md, checker 5555555)
  [docs] (3) negative control: check_docs.py rc 1
  [docs] restored (cmp equal)
  [docs] (1') base (b) re-run after the restore: check_docs.py rc 0
  [note] Note bullet: file lines 374-382, 1089 chars
  [note]   N-W2 (32d61d60 l. 239-240): once in its report True; «…» once in the Note bullet True; text: Note N-W2 (no change asked): the R-2 sentence follows the cited-replays list after a semic
  [note]   W-L2-1 part 1 (01e83df5 l. 305): once in its report True; «…» once in the Note bullet True; text: The 4,000 / 3,000 / 300 runs are the lane's own (box 104 out/), not an independent replay.
  [note]   W-L2-1 part 2 (01e83df5 l. 306-307): once in its report True; «…» once in the Note bullet True; text: Old (once in L-2): «; WRAP's six must-0 counters (». New: «; and this lane's own runs (box
  [note]   N-W2 says «no change asked»: True; W-L2-1 says «no change required for MATCH»: True
  [note]   W-L2-1 Old «; WRAP's six must-0 counters (» in L-2: 1
  [note]   lane output wrap_rand.out at faf0c8ff: 3 lines, «s3fail 0 nonstd 0 nohoward 0 fbwrong 0 endwrong 0 wrong 0» rows 3, named in the Note bullet: True
  [note]   lane output wrap_json.out at faf0c8ff: 1 lines, «s3fail 0 nonstd 0 nohoward 0 fbwrong 0 endwrong 0 wrong 0» rows 1, named in the Note bullet: True
  [note]   lane output wrap_lmcs_xi.out at faf0c8ff: 12 lines, «s3fail 0 nonstd 0 nohoward 0 fbwrong 0 endwrong 0 wrong 0» rows 12, named in the Note bullet: True
  [note]   lane output wrap_fried_xi.out at faf0c8ff: 5 lines, «s3fail 0 nonstd 0 nohoward 0 fbwrong 0 endwrong 0 wrong 0» rows 5, named in the Note bullet: True
  [note]   lane output wrap_long.out at faf0c8ff: 6 lines, «s3fail 0 nonstd 0 nohoward 0 fbwrong 0 endwrong 0 wrong 0» rows 4, named in the Note bullet: True
  [note]   L-2 «; L-RED 66 R236 / R237 (1)» follows the R-2 sentence (the cited-replays list resumes after it): True
  [note] NEGATIVE CONTROL: a made-up N-W3 note in REFEREE's report: 0
  [chk] model: landed R127 title (HEAD) == «### R127 [refereed-only] » + R127 L-3 + «, CHECKER PASS (docs/checker/C141.md, checker 850e9765)»: True
  [chk] file: sha1 eef22f39475a89bbc1be937d49f8d5acdb861a0b bytes 123395 lines 1055 ends with newline True
  [chk] ### R headings at d[...]: [226]
  [chk] (a) title == prefix + L-2 (no newline) + tail: True ; middle bytes == L-2 bytes without newline: True
  [chk]     title: 3615 chars, 3676 bytes, sha1 671013588f5777a89660a1be9549266b12c4fc16, ( 45 ) 45, min depth 0, final 0, ¦ 6 (L-2's own), fill token 1, ends «AP.md; L-SI successor 53)., CHECKER PASS (docs/checker/C146.md, checker PENDING)»
  [chk] (e) entry block d[226:423] (lines 227-423, 197 lines, sha1 of the joined block b4a326db7668c2e3e168f05a282c1f6ea5789244, with a final newline e3c53360f857ff99c24c42e4b4beac035493be7a); next line blank: True; line after: 'Proposed GAPS line-11 UPDATE (append-onl'
  [chk] (b) fill token in the entry block: 1 ; in the whole file: 2 at lines [227, 992]
  [chk]     «\n**Erratum E-1** (not a result» in the block: False ; line-start «**Erratum» in the file: 0 ; empty lines inside the block: 0 ; block lines starting «### »: 1
  [chk] (e) UPDATE line(s) at d[...]: [440] (line [441])
  [chk]     lines starting «UPDATE » in the file: [441]
  [chk]     GAPS preamble at d[424:440]
  [chk] (c) "¦" in the title: 6 (L-2's 6); in the entry block below the title: 0; in UPDATE: 0; in GAPS preamble: 1 (the quoted « ¦» of the row end); in line 1 + record + flags: 37; in the file: 44
  [chk] (d) UPDATE <DATE> 1 <HH:MM> 1 <checker> 1; head at its start: True
  [chk]     UPDATE = upd130L2.txt: True ; sha1 (no newline) 58889da6f0b976ddc49e6ec89b6b3c75a7a133b4 ; with newline d217fc967e88b791057a1c6260184ad7f9a552d0 ; 3726 bytes ( 47 ) 47
  [chk]     stale grep, entry block minus title (case-insensitive): {'candidate': 10, 'until two referees sign': 1}
  [chk]       'until two referees sign' at file lines: [(335, '  CONDITIONAL until two referees sign» and reco')]
  [chk]     stale grep, title: {'pending': 1, 'candidate': 1, 'until two referees sign': 1, 'proved lane': 1} ; UPDATE: {'candidate': 1, 'until two referees sign': 1, 'proved lane': 1}
  [chk]     R128 / R129 named in the entry block: 1 / 1 (as RESULTS premises: 0 / 0)
  [chk]     line 1 «NOT LANDED» 1 ; «<DATE>» in file 6 ; «<checker>» 6 ; «<HH:MM>» 6 ; tab characters in the file: 0
  [chk] (e) slices: line 1 d[0]; FIRST FILL record d[1:225] (flags d[73:225]; + blank d[225]: ''); title d[226]; entry d[226:423] (Note bullet at d[373]); blank d[423]; preamble d[424:440]; UPDATE d[440]; blank d[441]: ''; Addendum (first fill) d[442:1055]
  [chk]     Addendum (second fill): none ; the Lead's G-L43 bullet at d[[382]]
  [chk] (g) vs first fill 0885b1ab: line 1 equal True; title equal True; UPDATE equal True; preamble equal True; first-fill Addendum d[442:1055] == first fill d[398:1011]: True; block lines 188 -> 197
  [chk] (f) QUOTE SWEEP (corpus: 86 texts), per section
  [chk]     sweep line 1: 1 quotes, 1 parts, 0 not found []
  [chk]     sweep FIRST FILL record and flags: 149 quotes, 142 parts, 0 not found []
  [chk]     sweep entry block: 92 quotes, 113 parts, 0 not found []
  [chk]     sweep GAPS preamble + UPDATE: 14 quotes, 9 parts, 0 not found []
  [chk]     sweep Addendum (first fill): 65 quotes, 86 parts, 18 not found ['(F ≤ m_E − ¦V_E¦ + 1 under [RULE])', 'so 2^Ω(√¦V¦):', ', ¦V¦ = 10.5n² + 152.5n + 48', '¦V¦ = 10.5n² + 152.5n + 48', "; and this lane's own runs (box [note] N-W2 says", ': True [note] W-L2-1 Old', 'in L-2: 1 [note] lane output wrap_rand.out at faf0c8ff: 3 lines,', 'rows 3, named in the Note bullet: True [note] lane output wrap_json.ou']
  [chk]     sweep whole file: 321 quotes, 351 parts, 18 not found ['(F ≤ m_E − ¦V_E¦ + 1 under [RULE])', 'so 2^Ω(√¦V¦):', ', ¦V¦ = 10.5n² + 152.5n + 48', '¦V¦ = 10.5n² + 152.5n + 48', "; and this lane's own runs (box [note] N-W2 says", ': True [note] W-L2-1 Old', 'in L-2: 1 [note] lane output wrap_rand.out at faf0c8ff: 3 lines,', 'rows 3, named in the Note bullet: True [note] lane output wrap_json.ou']
  [chk]     sweep NEGATIVE CONTROL: 1 quotes, 1 parts, 1 not found ['N5′-xi makes polynomially many iterations on W^L_n']
  [chk]     negative control reported missing: True
  [lp] cites 136 (87 shown in the draft as «quote», 49 used for a line number only) in 16 (commit, file) pairs; failed at the cited lines: 0 []
  [lp] shown quotes not in the draft as «quote»: 0 []
  [lp] NEGATIVE CONTROL 1 (window shifted by 40 lines): 0 of 136 still pass []
  [lp] NEGATIVE CONTROL 2 (longest word mutated): 0 of 136 still pass
  [lp]     0037d948 docs/red/R236-fn.md 5
  [lp]     01e83df5 docs/referee-2/R2-P-N5-WRAP.md 11
  [lp]     07fd5ae4 docs/referee-2/R2-P-N5-WRAP.md 28
  [lp]     32d61d60 docs/referee/R-P-N5-WRAP.md 10
  [lp]     3cf594cc docs/referee-2/R2-P-N5-WRAP.md 6
  [lp]     4af9279d CLAUDE.md 1
  [lp]     4af9279d TARGET.md 2
  [lp]     4af9279d docs/RESULTS.md 1
  [lp]     4af9279d docs/agents/LEAD-STATE.md 2
  [lp]     5d30968a docs/referee-2/R2-P-N5-WRAP.md 1
  [lp]     5eca1c32 docs/red/R237-wrap.md 6
  [lp]     99df2458 docs/referee/R-P-N5-WRAP.md 43
  [lp]     e01447e7 docs/si/P-N5-WRAP.md 8
  [lp]     faf0c8ff docs/si/P-N5-WRAP-fixes.md 6
  [lp]     faf0c8ff docs/si/P-N5-WRAP-line-L2.txt 3
  [lp]     faf0c8ff notes/L-SI.md 3
  [sim] HEAD RESULTS sha1 4117c8a7d0165cd8d3a880f9a405d9c6fc6a5089 lines 16769 "¦" 1477 ; GAPS sha1 ccf059a1558fc3e1ae769a7aa98506f5fa7d64d5 lines 23
  [sim] == base (a) DRY RUN: HEAD 626da53c as is (R128, R129 absent)
  [sim] [sim a] pure insertion: prefix byte-unchanged True ; suffix byte-unchanged True ; inserted lines 198
  [sim] [sim a] headings after insertion: {'R126': [15726], 'R127': [15903], 'R128': [], 'R129': [], 'R130': [16127], 'E-1': [16325], 'E-2': [16338], 'E-3': [16366], 'Dead': [16397]}
  [sim] [sim a] R130 at l. 16127-16323, blank l. 16324 (''), «**Erratum E-1**» l. 16325; the line before R130: l. 16126 '' (R127's block ends l. 16125)
  [sim] [sim a] order R126 < R127 < R130 < E-1 < E-2 < E-3 < Dead: True
  [sim] [sim a] RESULTS lines 16769 -> 16967 (+198) ; "¦" 1477 -> 1483 (+6 = the title's 6) ; «checker 5555555)» once True ; fill token 0
  [sim] [sim a] ### R1xx headings: 29, R130 the last: True ; RESULTS sha1 after: 182dc514cb649c2d044203c5e84a5b794958e324
  [sim] [sim a] GAPS: only l. 11 changes True ; lines 23 -> 23 ; l. 11 "¦" 76 -> 76 ; «UPDATE 2026-» 62 -> 62 ; R130 last: True ; after R127's: True ; prefix byte-unchanged: True ; GAPS sha1 after: 44155976ada6f68d08627ed20030d27007eada0e
  [sim] [sim a] GAPS l. 11 order of the last RESULTS UPDATEs: ['R123', 'R124', 'R125', 'R126', 'R127', 'R130']
  [sim] == base (b), the order of record: HEAD + R128 (third-fill block d[282:522], 240 lines; UPDATE ba695811 filled 2099-01-11 00:00 3333333) + R129 (second-fill block d[153:303], 150 lines; UPDATE 31d7b642 filled 2099-01-12 00:00 4444444), each before E-1 and after the previous: RESULTS lines 17161, sha1 6eae20e5670f5d4de54454dd3fa1752f3dbf0225; GAPS sha1 ffaa910bb5385f360dfa3bef4bb9286594b2d813
  [sim] [sim b] pure insertion: prefix byte-unchanged True ; suffix byte-unchanged True ; inserted lines 198
  [sim] [sim b] headings after insertion: {'R126': [15726], 'R127': [15903], 'R128': [16127], 'R129': [16368], 'R130': [16519], 'E-1': [16717], 'E-2': [16730], 'E-3': [16758], 'Dead': [16789]}
  [sim] [sim b] R130 at l. 16519-16715, blank l. 16716 (''), «**Erratum E-1**» l. 16717; the line before R130: l. 16518 '' (R129's block ends l. 16517)
  [sim] [sim b] order R126 < R127 < R128 < R129 < R130 < E-1 < E-2 < E-3 < Dead: True
  [sim] [sim b] RESULTS lines 17161 -> 17359 (+198) ; "¦" 1477 -> 1483 (+6 = the title's 6) ; «checker 5555555)» once True ; fill token 0
  [sim] [sim b] ### R1xx headings: 31, R130 the last: True ; RESULTS sha1 after: 6f9dd60b713a0e9ea35e24c170d9612083ebe4a5
  [sim] [sim b] GAPS: only l. 11 changes True ; lines 23 -> 23 ; l. 11 "¦" 76 -> 76 ; «UPDATE 2026-» 62 -> 62 ; R130 last: True ; after R129's: True ; prefix byte-unchanged: True ; GAPS sha1 after: 3ea0269bcfec00eb7b313fdde654adcbf0dd458f
  [sim] [sim b] GAPS l. 11 order of the last RESULTS UPDATEs: ['R125', 'R126', 'R127', 'R128', 'R129', 'R130']
  [sim] [sim b] R128 and R129 blocks unchanged in the result: True True ; UPDATEs R127 < R128 < R129 < R130 on l. 11: True
  [sim] fill values used only here: R128 ('2099-01-11', '00:00', '3333333') R129 ('2099-01-12', '00:00', '4444444') R130 ('2099-01-13', '00:00', '5555555')
