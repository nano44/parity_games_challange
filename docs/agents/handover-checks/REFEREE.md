# Handover check: REFEREE

## successor 37 (2026-11-13T17:17Z by date -u; predecessor successor 36, HANDOVER NOTE in notes/REFEREE.md at aa9025fb)
Measured from the repository at the time of writing, not recalled. The model label is left out of repository files (the Lead's brief:
no model name in commits); the Lead's brief names it.

### 1. Branch, head, distance to trunk
- Trap check at the start (17:14Z): the local branch was claude/referee at 890daf41, 194 commits behind origin (stale container,
  although `git status` said «up to date»); `git fetch --unshallow` (not shallow), fetch of claude/referee and trunk,
  `git merge --ff-only origin/claude/referee`. After it: `git branch --show-current` = claude/referee and HEAD =
  origin/claude/referee = aa9025fb5b90bb5066f8bd636509ae84f50c974a (the commit that carries successor 36's HANDOVER NOTE; read,
  with docs/referee/R-P-N5-EXP.md: 496 lines, sha1 1dde381267424268151cdda911666a816472117a, stages 1-3, read in full).
- At aa9025fb: `git rev-list --left-right --count trunk...HEAD` = «4 11» (behind, ahead) against trunk claude/vibrant-johnson-nxvvxo
  dba11145c222c9034144db821057485698232d44, merge-base 6eaf4604. The 4 trunk commits (65e28287, 25f6df18, 38f4a6a0, dba11145) change
  docs/DECISIONS.md, docs/DECISIONS-INDEX.md, docs/agents/LEAD-STATE.md and scripts/push.sh (the ls-remote check after git push).
  Trunk is NOT merged in this commit, so that this push changes docs/agents/ only (Lead reading L56); a normal merge of trunk
  goes with the stage-4 push.
- Clock: local `date -u` Fri Nov 13 17:15:31 UTC 2026 against «date: Fri, 13 Nov 2026 17:15:31 GMT» of a raw.githubusercontent.com
  response in the same command: skew 0 s (to the second).
- No push running (`pgrep -af "bash scripts/push.sh"`: nothing, exit 1). Working tree clean before this file (`git status --short`:
  0 lines). Container: uptime 1 min at 17:16Z, 4 CPUs, no job running.
- rate_limit_info (get_session on this session, 17:16Z): isUsingOverage false, rateLimitType five_hour, status allowed_warning,
  resetsAt 1794595200 (= Fri Nov 13 18:40:00 UTC 2026 by date -u -d); session_context.model and last_served_model as the Lead's
  brief names them, effort_level xhigh.

### 2. Open work and next step of each (the Lead's WORK order; «go» is given in advance)
- 1. STAGE 4 of docs/referee/R-P-N5-EXP.md (append; stage 3's stamp frozen first): the author lane's fixes entries 2-5. Object
  MEASURED on origin: claude/l-red-b 24f4d436a0fea1f62ae736f20f78ff9e84333a90; docs/red-b/P-N5-EXP-fixes.md 829 lines, sha1
  9dc9179fb08063cd59de25c5d3e16b0f8c693fbd; docs/red-b/P-N5-EXP.md there still sha1 c0449b17193f19619f33b366096762dfde27d542
  (frozen packet unchanged); docs/red-b/P-N5-EXP-line-L1.txt one line, 5,585 bytes, sha1 59c5309377eda882ba436ffe7eb03fbff598c7c8.
  All three equal the Lead's pins. Not opened yet at this writing. Next: (a) by script: entry 4's quotations of this lane's §5.3
  (LEMMA′ l. 219-225, CAUSAL l. 203-204, the standing paragraph l. 200-202) and of STABLE byte-equal to the report; the packet's
  sha1; the fixes file append-only against 06d399c2; (b) one line per item E-1, E-2, E-4, E-5 (entry 4), E-3, E-6 (entry 5), E-7,
  P-1 (entry 2), O-1 (entry 3: whether I SIGN Corollary EXP-N5′ as PROVED-CONDITIONAL on R124 and R117 as landed; R124's Corollary
  EXACT-L on trunk docs/RESULTS.md l. 15371 and its premises to be read); (c) the lane's new counters re-run with this lane's
  tools where they overlap (gkx.py unit / abs / resp; the lemma as frozen must fail at (j, a, t) = (1, 1, 2^k − 1)); (d) the
  verdict line. Then commit, push, ls-remote, SHA to the Lead.
- 2. STAGE 5, when the Lead sends the commit of line L-2 and fixes entry 7 (not on origin at this writing: claude/l-red-b head is
  24f4d436): byte tests of L-2; L-2 against my verdicts clause by clause (unconditional / conditional on R117, R124 as landed /
  DATA; the L41 tail; R117's premises against R117's title line); entries 6 and 7; one line.
- 3. Only if the Lead asks: the agreement note with the second referee; K-1 / K-2 of P-N5-KEY1P.
- Independence: docs/referee-2/ on P-N5-EXP (its report, its Addendum 2 with its signature of LEMMA′) is NOT opened before my
  stage 4 is committed. The fixes file's entry 4 contains a concordance to the second referee's prefix form: that is the author
  lane's text, part of the object under review; I check my lane's quotations in it and do not open the second referee's file.

### 3. docs/GAPS.md rows relevant to me (trunk dba11145)
- REFEREE owns no row. The row the packet feeds: G-N5-TIME (line 11; severity major; owner «L-NEW (L-LIT T22; referees later)»; status
  open). P-N5-EXP's dead-end paragraph would answer it under R117's premises; changing the row is the Lead's, after both signatures
  and CHECKER.

### 4. Three owner rulings that most constrain me (verbatim, docs/DECISIONS.md at trunk dba11145), with DECISIONS-INDEX status
1. D1 (index: active; DECISIONS.md lines 7-8):
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   > Never downgrade the referee to save money.
   (The Lead's brief applies the same standard to a kill. Lead readings, not owner words: L43, index: active: «DEAD» needs a
   refereed proof or an instance beyond an explicit bound; L41, index: active: a referee-originated proof counts as two-referee
   signed when its author signs it and the other referee independently signs it. LEMMA′ and CAUSAL are such.)
2. D18 (index: active; DECISIONS.md line 333):
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.
3. D25 (index: active; DECISIONS.md line 541; owner, direct message to the Lead, 2026-11-13):
   > So put everything into trying solving it today
   (with D24, index: active, line 538: «do xhigh»; and D26, index: active, line 567, now in docs/DECISIONS.md at trunk dba11145:
   «I hit my usage limit while you were working, but it has reset now. Please continue from where you left off.»)

### 5. One trap that bit this lane, and the check that prevents it
- Trap (s27-s37): stale local branch (194 behind at this start, with `git status` reporting «up to date»). Check: fetch, ff-only,
  `git branch --show-current` and `git rev-parse HEAD origin/claude/referee` equal before any commit or push.sh (done).
- Trap (s36, the report's rule): R-P-N5-EXP.md is REBUILT from logs by gkx_fill.py; a stage appended by hand, or a stage whose
  2026-11-13T17:17Z stamp is not frozen, changes the earlier stages' bytes at the next fill. Check: freeze stage 3's stamp in
  gkx_report_stage3.md first; after the fill, the first 496 lines must still have sha1 1dde3812… (`head -n 496 | sha1sum`).
- Trap (s34): a SHA sent in the same tool batch as its commit. Check: send_message is never in the batch of a git commit; SHAs are
  copied from git output.
- Trap (s34, s35): a restart or an HTTP 503 leaves origin behind although push.sh printed exit 0. Check after every push: `git ls-remote
  origin claude/referee` against the SHA.
- Trap (s32 G-P6; this packet's E-2): an induction run past the interval its lemma was proved on. Check for the restated lemma in
  entry 4: for each inductive step, write which states the cited fact was proved for, and run the frozen form at the failing
  instance (j, a, t) = (1, 1, 2^k − 1).
