# Handover check: CHECKER (successor 4, Opus 5.5 per owner D15 / Lead reading L37; written 2026-10-24 15:22Z by date -u)
First file for this lane (none before). Every answer is measured from the repository at writing time (commands named), not recalled.
Predecessor: successor 3, session_01UCJpCyXwAUjiQHfXE3bsMs (Opus 5.5), parked at ~590k context (Lead brief 15:22Z); its last
CHECKER commit is 52a1e489 (C27 Addendum 4: R18 landed at 022ce8f PASS). There is no notes/CHECKER.md on any branch I hold
(`ls notes/` at b70aa59); the predecessor's state lives in docs/checker/C27.md and the NOW roster row.

### 1. Branch, head, ahead/behind trunk
- Branch claude/checker. After `git fetch origin claude/vibrant-johnson-nxvvxo claude/checker`: local = origin/claude/checker = 52a1e489
  (container not stale).
- `git rev-list --left-right --count origin/claude/checker...origin/claude/vibrant-johnson-nxvvxo`: 0 ahead, 157 behind trunk b70aa59f.
  52a1e489 is an ancestor of trunk (`git merge-base --is-ancestor`).
- So `git merge origin/claude/vibrant-johnson-nxvvxo` (normal merge, no rebase) was a FAST-FORWARD; no merge commit was made.
  Before this file's commit HEAD = b70aa59f, 0 ahead / 0 behind; after it, 1 ahead (this commit), 0 behind.

### 2. Open work and the next step of each
- C27 (R18) is CLOSED (Addendum 4, PASS, landed text verbatim at 022ce8f). Nothing else of the predecessor's is open.
- C28 (assigned by the Lead 15:22Z, no GO needed): landing gate for docs/agents/R19-draft.md at trunk b70aa59, lines 3-end;
  signed object docs/new/P-N5-RE-box26.md at trunk 52c7261 (sha1 8dba4576…); reports docs/referee/R-N5-RE.md (4457a9a; §C 87beaa6 +
  a3d1f70) and docs/referee-2/R2-N5-RE.md (3ee7b73, c66da44; §C dd5aaa2). Next step: verify the pins and sha1, re-fetch the referee
  branch heads (C27 E-1 lesson), then the five checks (statement diff incl. (NC) dropped / τ clause / 𝓡*, gap map vs both §C,
  every Data/Limits number, spot re-runs reentry.py + piececheck.py on fts_best16 and returns_rt48 plus REFEREE-2's nc_fail_n12,
  TARGET diff), report in docs/checker/C28.md, push with scripts/push.sh.
- notes/CHECKER.md does not exist; I create it (resume point, conventions, things only I know) with C28.

### 3. docs/GAPS.md rows I own
- None. No row has CHECKER in its owner column (`awk -F'|' '$4 ~ /CHECKER/'` on docs/GAPS.md: no output). CHECKER appears only as the
  gate that re-ran or passed a landing (GAP-A "re-run CHECKER C11"; G-N5-TIME "CHECKER C20"; G-N5-TERM "CHECKER C17 PASS").

### 4. The three owner rulings that most constrain me (verbatim), with index status
1. D1 (docs/DECISIONS.md#d1 key lines; docs/decisions/D001-launch-brief.md; DECISIONS-INDEX row D1 "active"):
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   A landing passes only if no claim is stronger than what both referees signed, and the TARGET.md §5 scope is stated.
2. D18 (docs/DECISIONS.md#d18; DECISIONS-INDEX row D18 "active"; Lead reading L40 "active", labels PROVED/CONJECTURE/OPEN):
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.
   For the gate: every conditional, DATA and open item in a draft must be labelled as such; a reading must not be presented as signed.
3. D15 (docs/DECISIONS.md#d15; DECISIONS-INDEX row D15 "active"; Lead reading L37 "active"):
   > q18 b. , q16 b,c. BUt I dont want it to ask these questions from me. Be autonomous, reason about it
   L37 (1): referee signatures on Opus are labelled "(Opus 5.5, D15)"; the gate checks the labels. I run on Opus under it, and decide
   inside the brief without option questions.
   (Also binding: D12/L33 for older "(Opus 5.5, D12)" labels; D7 stop on overage.)

### 5. One trap, and the check that prevents it
- Trap (C27 E-1, 2026-10-24 04:11Z): the predecessor checked the R18 draft against the referee reports as merged on trunk, while both
  referee branches already carried newer, unmerged §C2 sections that changed the signed object (07f298d → d78e54f) and the gap lists.
  A PASS against trunk alone would have landed an entry citing the wrong signed object. (A second miss of the same class, C27 E-3:
  instances named as members of 𝒞^1O that were not; caught only by counting Odd choice vertices from the files.)
- Check: before any verdict, `git fetch` the referee, referee-2 and lane branches, print their heads, and test each with
  `git merge-base --is-ancestor <head> <trunk pin>`; any head not on trunk is read and named in the report. Every class-membership or
  count claim about a pinned instance is recomputed from the instance file at the pin, not taken from the text.
- Also carried: push.sh output redirected to a file, then `$?` (never piped); re-runs in a detached worktree of the exact pin with the
  scripts unmodified; file sha1 of every signed object verified.

## Handover check (successor 7)
Written 2026-10-25 16:10Z (date -u). CHECKER successor 7 (Opus 5.5, D15), this session. Predecessor: successor 6,
session_01XuHZ95RA84WV7mhDqDjRQ4, handover 0ac145ca (notes/CHECKER.md "## HANDOVER (successor 6 → successor 7)"). Successors 5 and 6
wrote their checks in notes/CHECKER.md; this one is here as the brief asks. Every answer measured from the repository; commands named.

### 1. Branch, head, ahead/behind trunk
- `git fetch origin claude/checker`; `git checkout -B claude/checker origin/claude/checker`; HEAD = origin/claude/checker = 0ac145ca (checked
  with `git rev-parse`). The fetch moved origin/claude/checker 52a1e489..0ac145ca: the clone started stale at C27 again.
- Trunk = claude/vibrant-johnson-nxvvxo, head c4c09736 (Lead hourly sweep 16:02Z). Before merging: `git rev-list --left-right --count HEAD...trunk`
  = 2 ahead (0ac145ca handover, 30598a36 trunk merge), 5 behind; merge-base 48bb74ce (R40 landing). 0ac145ca is NOT yet on trunk.
- `git merge --no-ff trunk` (no rebase) → 3 ahead, 0 behind. This file's commit makes 4 ahead, 0 behind.

### 2. Open work and the next step of each
- C45-C49 CLOSED (R36-R40 landed; docs/checker/C45.md..C49.md). Nothing in flight from successor 6.
- R41 = P-N5-NEB: packet docs/new/P-N5-NEB-box38.md sha1 ba15e51f (= handover). Reports on trunk: REFEREE docs/referee/R-N5-NEB.md 7da14c1f
  (40adbf1c), REFEREE-2 docs/referee-2/R2-N5-NEB.md 33fefec4 (a4516df9). NOT READY: no §C in either report yet, no NEB fixes file in docs/new/
  (`ls docs/new | grep -i NEB.*fix`: none; L-NEW succ. 19 does "NEB fixes when §Cs are in", NOW l.68), no docs/agents/R41-draft.md.
  Next: when the draft exists, the six-step method (pins over first-parent and --full-history; cited SHAs ancestor + `show --stat`;
  read packet, fixes, both reports and §Cs in full; trace data to logs; re-runs in a detached worktree; landed check). Expect the
  Step (K) citation repair OUT needed (handover; OUT fixes §1).
- R42 = P-N5-LV: packet docs/si/P-N5-LV-box11.md d0d797f0, addendum a15a8871. Reports: REFEREE R-N5-LV.md 0be5e352 (8054da2f), REFEREE-2
  R2-N5-LV.md 66e55e04 (b1038bea). Same state: no §Cs, no fixes file, no R42 draft. LV2 (3b23a41f) and PFZ are in review; REFEREE-2's
  R2-N5-PFZ (37e55fde) is on claude/referee-2, not yet on trunk.
- Oink: tools/ absent; to build with scripts/setup_oink.sh before the first re-run (verify's smoke step is NOT RUN without it).
- Scratch tool landed.py (successor 6's tools46) is lost with the container; rewrite it at the first landed check.

### 3. docs/GAPS.md rows I own
- `awk -F'|' '$4 ~ /CHECKER/' docs/GAPS.md`: none. On the landing side: G-N5-TIME (major, L-NEW, open, l.11); last UPDATE 15:55Z (R40 landed,
  CHECKER C49 + Add. 1): "Open: level −1 (P-N5-LV signed by both, P-N5-LV2 in review; ...), out-of-scope fallbacks (P-N5-NEB signed by
  both; P-N5-PFZ in review), ...". R41/R42 will append to that row: old row minus " |" a prefix of the new one, status open.

### 4. The three owner rulings that most constrain me, verbatim (docs/DECISIONS.md, `grep -n -F`), with index status
- D1 (l.7; DECISIONS-INDEX l.5 "active"): "A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim,
  including the fleet's own, as wrong until it passes the gauntlet below."
- D15 (l.278; index l.26 "active", L37 l.27): "q18 b. , q16 b,c. BUt I dont want it to ask these questions from me. Be autonomous, reason about it"
- D18 (l.333; index l.32 "active", L40 l.33): "Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas
  from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state
  them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems."
- For the gate: nothing lands stronger than both signatures (D1); labels "(Opus 5.5, D15)"; PROVED / CONJECTURE / OPEN / FALSE exact (L40).

### 5. One trap, and the check that prevents it
- Trap (C47-C49, every E-item): draft wording drifting from signed text: a dropped hypothesis clause, an unquantified variable, a dropped case
  split, and false referee attributions ("both referees reproduce", "R2 does not address"). Check: diff every draft clause against the
  packet + fixes verbatim, and read every attribution sentence against both reports AND both §Cs before PASS.
- Also bit me already: `git status` said "up to date" on a stale clone (52a1e489); the check is fetch, then `git rev-parse HEAD origin/<branch>`.

## Handover check (successor 8)
Written 2026-10-25 22:54Z (date -u). CHECKER successor 8 (Opus 5.5, D15), this session. Predecessor: successor 7, handover 111afad7
(notes/CHECKER.md "## HANDOVER (successor 7 → successor 8)"). Every answer measured from the repository; commands named.

### 1. Branch, head, ahead/behind trunk
- `git fetch origin claude/checker`: moved origin/claude/checker 52a1e489..111afad7 (clone started stale again). `git checkout -B claude/checker
  origin/claude/checker`; `git rev-parse HEAD origin/claude/checker` = 111afad7 both.
- Trunk = claude/vibrant-johnson-nxvvxo, head a4bf4050 (Lead hourly sweep: REFEREE §C NEEDB, l-new box 43, l-si repro, R49 draft update).
  Before merging: `git rev-list --left-right --count HEAD...trunk` = 4 ahead (111afad7, df63cbca, 0b2f6950, d88502d2), 13 behind; merge-base
  063ecc73. 111afad7 is NOT yet on trunk (`merge-base --is-ancestor`: no).
- `git merge --no-ff trunk` (no rebase) = cbbaa81a → 5 ahead, 0 behind. This file's commit makes 6 ahead, 0 behind.

### 2. Open work and the next step of each
- C50-C57 CLOSED (R41-R48 landed; table in the handover). Counter: next check C58. In flight: none.
- C58 = R49 (P-N5-NEEDB). Draft docs/agents/R49-draft.md on trunk a4bf4050, sha1 e8415438, header "REFEREE's §C and the fixes file to be
  filled"; it still carries FIXES-PENDING (l.6) and "§C (REFEREE-2): R2SC-PENDING" (l.54); REFEREE §C cited 7dbd5118. Packet
  docs/si/P-N5-NEEDB-box13.md sha1 7471aef3. NOT READY: wait for the Lead's final draft sha1. Next: the six-step method of the handover
  (pins over --full-history, report-version diffs, cited SHAs ancestor + show --stat, full read and clause diff, data traced to logs,
  re-runs in detached worktrees incl. N-NEEDB-5 / experiments/si/needb5, report docs/checker/C58.md), then the landed check.
- Then FX, NH42, KW, DUAL as they converge (Lead's queue).
- Tools: Oink not built in this container (tools/ absent) — scripts/setup_oink.sh after "go", before the first re-run; landed.py to
  rewrite in the scratchpad from the handover listing.

### 3. docs/GAPS.md rows I own
- `awk -F'|' '$4 ~ /CHECKER/' docs/GAPS.md`: none. Landing side: G-N5-TIME (major, L-NEW, open, l.11), last UPDATE 22:36Z (R48 landed, C57 +
  Add. 1). R49 will append to it: old row minus " |" a prefix of the new one, status open.

### 4. The three owner rulings that most constrain me, verbatim (docs/DECISIONS.md, `grep -n -F`), with index status
- D1 (l.7; DECISIONS-INDEX l.5 "active"): "A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim,
  including the fleet's own, as wrong until it passes the gauntlet below."
- D15 (l.278; index l.26 "active", Lead reading L37 l.27): "q18 b. , q16 b,c. BUt I dont want it to ask these questions from me. Be autonomous, reason about it"
- D18 (l.333; index l.32 "active", Lead reading L40 l.33): "Focus on N5 and work toward proving it. Explore novel approaches, especially by
  connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where
  needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems."
- For the gate: nothing lands stronger than both signatures (D1); label "(Opus 5.5, D15)"; PROVED / CONJECTURE / OPEN / FALSE exact (L40).

### 5. One trap, and the check that prevents it
- Trap (successor 6, found by successor 7 at 17:07Z): addenda written with Write OVERWROTE the main reports of C47, C48, C49 (restored from
  d0900448, 3d6dcbc8, 2b540583). Check: every addendum is appended (`cat >>`), and before each push `git diff --stat` on docs/checker/ shows
  only insertions for an existing C-file (`git diff HEAD -- docs/checker/C5x.md | grep -c '^-[^-]'` = 0).
- Also: stale clone with "up to date" (fetch + rev-parse check above); hand-typed stamps (every stamp from `date -u` in the writing command).

## Handover check (successor 9)
Written 2026-10-26 04:27Z (date -u). CHECKER successor 9 (Opus 5.5, D15), this session. Predecessor: successor 8, session_017WsSD8yWCujUTXzQv5cc2r,
handover 55e3fb05 + 4dcdd7e9 (notes/CHECKER.md "## HANDOVER (successor 8 → successor 9)"). Every answer measured from the repository; commands named.

### 1. Branch, head, ahead/behind trunk
- Clone started stale again: local claude/checker = 52a1e489 with "up to date". `git fetch origin`; `git merge --ff-only origin/claude/checker`
  → HEAD = origin/claude/checker = 4dcdd7e9 (`git rev-parse`); `git merge-base --is-ancestor 4dcdd7e9 HEAD`: yes.
- Trunk = claude/vibrant-johnson-nxvvxo, head a81ece68 (Lead 04:20:46Z: REFEREE-2 14 GO; LANE-RESTART rows). Before merging:
  `git rev-list --left-right --count 4dcdd7e9...trunk` = 2 ahead (55e3fb05, 4dcdd7e9), 284 behind; merge-base b911ecce (C65 report).
  4dcdd7e9 is NOT on trunk (`merge-base --is-ancestor`: no).
- `git merge --no-ff trunk` (no rebase) = d4429f13 → 3 ahead, 0 behind. This file's commit makes 4 ahead, 0 behind.

### 2. Open work and the next step of each
- C58-C64 CLOSED (R49-R55 landed; table in the handover). Counter: next check C66.
- C65 = R56 (P-N5-FBRED): main report b911ecce PASS. R56 LANDED at trunk eb81356c (parent eef7346a; "Lead: land R56 (P-N5-FBRED,
  CHECKER C65 b911ecce)"; `merge-base --is-ancestor eb81356c trunk`: yes). Next step (after "go"): C65 Addendum 1 = landed check:
  RESULTS minus the R56 block = RESULTS@eef7346a; block = docs/agents/R56-draft.md lines 3-end with one fill "checker PENDING)" →
  "checker b911ecce)"; GAPS: only G-N5-TIME changes (old row minus " |" a prefix of the new, status open); pins unchanged. The Lead says the
  body changed since the passed draft 0089cc84 by optional notes N-1 (limit (ii), max f 37) and N-2 (EXIT-SWITCH_D in (e)) only: word-diff
  the draft 0089cc84 → landed draft, and check nothing else moved. landed.py rewritten in the scratchpad from the handover listing.
- R57 = P-N5-1E (L-SI, 𝒞^1E assembly): not started. NOW l.2: REFEREE-2 signed, REFEREE 12 on it. Next: wait for the Lead's draft sha1
  (both reports and §Cs in), then the six-step method → docs/checker/C66.md.
- Oink: built with scripts/setup_oink.sh in this container (tools/oink/build).

### 3. docs/GAPS.md rows I own
- `awk -F'|' '$4 ~ /CHECKER/' docs/GAPS.md`: none. Landing side: G-N5-TIME (major, L-NEW (L-LIT T22; referees later), open, l.11);
  R56 appended to it at eb81356c; R57 will append again: old row minus " |" a prefix of the new one, status open.

### 4. The three owner rulings that most constrain me, verbatim (docs/DECISIONS.md, `grep -n -F`), with index status
- D1 (l.7; DECISIONS-INDEX l.5 "active"): "A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim,
  including the fleet's own, as wrong until it passes the gauntlet below."
- D15 (l.278; index l.26 "active", Lead reading L37 l.27 "active"): "q18 b. , q16 b,c. BUt I dont want it to ask these questions from me. Be autonomous, reason about it"
- D18 (l.333; index l.32 "active", Lead reading L40 l.33 "active"): "Focus on N5 and work toward proving it. Explore novel approaches, especially by
  connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where
  needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems."
- For the gate: nothing lands stronger than both signatures (D1); label "(Opus 5.5, D15)"; PROVED / CONJECTURE / OPEN / FALSE exact (L40).

### 5. One trap, and the check that prevents it
- Trap (successor 8, recorded in its resume point): first-line stamps of messages to the Lead typed by hand (the C65 message said "04:20Z";
  it was sent about 04:12Z). Check: every stamp, in files and in messages, comes from `date -u` run in the same turn as the write/send.
- Also carried: stale clone with "up to date" (fetch + rev-parse, caught again here); addenda appended only (`cat >>`, then
  `git diff HEAD -- docs/checker/C65.md | grep -c '^-[^-]'` = 0); path-dependent seeds in REFEREE succ. 10 probes (run from the main clone).
- Correction to answer 2 (2026-10-26 04:32Z, date -u): the first push was rejected (fetch first). origin/claude/checker had moved 4dcdd7e9 → c50da6f0
  (successor 8, 04:23:18Z, after its handover): "CHECKER C65 Add. 1: R56 landed at eb81356c (only N-1, N-2 changes); C65 CLOSED". So C65
  is CLOSED by successor 8, not open. Merged with --no-ff (no rebase). Open work is now R57 = C66 only. I will re-measure Add. 1's four
  points independently after "go" if the Lead wants it (cheap: landed.py), else go straight to C66.

## Handover check (successor 10)
Written 2026-10-26 08:25Z (date -u). CHECKER successor 10 (Opus 5.5, D15), this session (session_011EiUmib2GvATXE6mphqubk). Predecessor: successor 9,
session_01PuVfnWPKpY138kyUwPuukh, handover 2615d89e (notes/CHECKER.md "## HANDOVER (successor 9 → successor 10)"). Every answer measured
from the repository; commands named.

### 1. Branch, head, ahead/behind trunk
- Clone started stale again: local claude/checker = 52a1e489 with "up to date". `git fetch origin`; `git merge --ff-only origin/claude/checker`
  → HEAD = origin/claude/checker = 2615d89e (successor 9's handover, 08:12:59Z).
- Trunk = claude/vibrant-johnson-nxvvxo, head 565b8a8d (Lead 08:17:50Z: "merge checker (C71/C73 closed) and l-red; L-RED 20 check 5/5, GO").
  Before merging: `git rev-list --left-right --count 2615d89e...trunk` = 1 ahead (2615d89e), 320 behind; merge-base 088a50ba
  (successor 9's closing addenda). 2615d89e is NOT on trunk (`merge-base --is-ancestor`: no).
- `git merge --no-ff trunk` (no rebase) = 4e3e671e → 2 ahead, 0 behind. This file's commit makes 3 ahead, 0 behind.

### 2. Open work and the next step of each
- C66-C73 CLOSED (R57-R64 landed; table in the handover; L-1 fixed by the Lead's merge e1eabcd0). Counter: next check C74.
- C74 = P-N5-STAU (packet docs/new/P-N5-STAU-box45.md, sha1 7446d9a9 at HEAD, `sha1sum`): not started. NOW l.50: REFEREE-2 succ. 15
  report 8e42c473 (all SIGN, no gap; N-STAU-1..4), its §C waits for REFEREE 13's report; NOW l.44: REFEREE 13 on P-N5-STAU.
  Next: wait for the Lead's RESULTS draft sha1 (both reports and both §Cs in), then the six-step method → docs/checker/C74.md; at landing,
  the landed-check recipe (landed2.py) plus `merge-base --is-ancestor <checker sha> <landing commit>` (Lead rule 07:57Z).
- Oink: built with scripts/setup_oink.sh in this container (exit 0; "oink built at 8fbf0a7"; tools/oink/build/oink present).

### 3. docs/GAPS.md rows I own
- `awk -F'|' '$4 ~ /CHECKER/' docs/GAPS.md`: none. Landing side: G-N5-TIME (major, L-NEW (L-LIT T22; referees later), open, l.11);
  a STAU landing appends to it: old row minus " |" a prefix of the new one, status open, other rows equal.

### 4. The three owner rulings that most constrain me, verbatim (docs/DECISIONS.md, `grep -n -F`), with index status
- D1 (l.7; DECISIONS-INDEX l.5 "active"): "A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim,
  including the fleet's own, as wrong until it passes the gauntlet below."
- D15 (l.278; index l.26 "active", Lead reading L37 l.27): "q18 b. , q16 b,c. BUt I dont want it to ask these questions from me. Be autonomous, reason about it"
- D18 (l.333; index l.32 "active", Lead reading L40 l.33): "Focus on N5 and work toward proving it. Explore novel approaches, especially by
  connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where
  needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems."
- For the gate: nothing lands stronger than both signatures (D1); label "(Opus 5.5, D15)"; PROVED / CONJECTURE / OPEN / FALSE exact (L40).

### 5. One trap, and the check that prevents it
- Trap (successor 9, C71 E-3): honest limits in a draft went stale because a referee appended an addendum after the draft was written.
  Check: before every report and addendum, `git log <draft pin>..<trunk> -- docs/referee*/R*-N5-<X>.md` (and fetch the referee and
  referee-2 heads); any new report commit is read in full before the verdict.
- Also carried: stale clone with "up to date" (caught again here: 52a1e489); addenda appended only (`cat >>`, then
  `git diff HEAD -- docs/checker/C74.md | grep -c '^-[^-]' || true` = 0); stamps from `date -u`; merge-before-landing ancestor test.

## Handover check (successor 11)
Written 2026-10-26 14:22Z (date -u). CHECKER successor 11 (Opus 5.5, D15), this session. Predecessor: successor 10, session_011EiUmib2GvATXE6mphqubk,
handover 1e2b39f5 (notes/CHECKER.md "## HANDOVER (successor 10 → successor 11)"). Every answer measured from the repository; commands named.

### 1. Branch, head, ahead/behind trunk
- Clone started stale: local claude/checker said "up to date" before `git fetch origin`; fetch moved origin/claude/checker 52a1e489 → 1e2b39f5;
  `git merge --ff-only origin/claude/checker` → HEAD = 1e2b39f5 (successor 10's handover).
- Trunk = claude/vibrant-johnson-nxvvxo, head 5fc35de2 (Lead 14:14:55Z: "R70 revised for C79 E-1, N-1..N-3; FBC REFEREE report; CHECKER handover; merges; log").
  Before merging: `git rev-list --left-right --count HEAD...trunk` = 0 ahead, 12 behind; merge-base = 1e2b39f5 (`merge-base --is-ancestor`: on trunk).
- `git merge --ff-only trunk` (fast-forward, no rebase, no new commit) → HEAD = 5fc35de2, 0 ahead / 0 behind. This file's commit makes 1 ahead, 0 behind.

### 2. Open work and the next step of each
- C74-C78 CLOSED (R65-R69 landed; table in the handover). C79 = R70 (P-N5-HONFF): main report docs/checker/C79.md at b49f5974, FAIL E-1 (title FB-RISE
  clauses: (b) stated as a rise across every such fallback; (a) without the n − 1 cap), optional N-1..N-3.
  Next: C79 Addendum 1 on the revised draft docs/agents/R70-draft.md (sha1 25c2cb5f… at trunk 5fc35de2): script-check E-1's fix text and N-1..N-3 are in and
  the old texts gone; `git diff --word-diff e14c78bb 5fc35de2 -- docs/agents/R70-draft.md`: nothing else moved; pins again; on PASS the checker SHA to the Lead.
  Then the landed check (every commit of the landing; checker SHA ancestor of the landing commit). R70 lands after R69 (already landed, a7c141b8).
- Counter: next new check C80. Queue: none named; P-N5-FBC and P-N5-CHOSEN drafts come when both referees and §Cs are in.
- Oink: built with scripts/setup_oink.sh in this container (exit 0; "oink built at 8fbf0a7"; tools/oink/build/oink present).

### 3. docs/GAPS.md rows I own
- `awk -F'|' '$4 ~ /CHECKER/' docs/GAPS.md`: none. Landing side: G-N5-TIME (major, L-NEW (L-LIT T22; referees later), open, l.11); an R70 landing
  appends to it: old row minus " |" a prefix of the new one, status open, other rows equal.

### 4. The three owner rulings that most constrain me, verbatim (docs/DECISIONS.md, `grep -n -F`), with index status
- D1 (l.7; DECISIONS-INDEX l.5 "active"): "A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim,
  including the fleet's own, as wrong until it passes the gauntlet below."
- D15 (l.278; index l.26 "active", Lead reading L37 l.27 "active"): "q18 b. , q16 b,c. BUt I dont want it to ask these questions from me. Be autonomous, reason about it"
- D18 (l.333; index l.32 "active", Lead reading L40 l.33 "active"): "Focus on N5 and work toward proving it. Explore novel approaches, especially by
  connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where
  needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems."
- For the gate: nothing lands stronger than both signatures (D1); label "(Opus 5.5, D15)"; PROVED / CONJECTURE / OPEN / FALSE exact (L40).

### 5. One trap, and the check that prevents it
- Trap (successor 10, C76/C78/C79): the E-items were title clauses wider than the signed items (a dropped hypothesis, "needs" for a sufficient
  condition, a rise over LEV(h) stated over LEV(t), an open branch asserted). Check: split the title into clauses and diff each one against the
  signed item's hypotheses and reference points; fix texts are then script-checked (quoted strings ≥ 25 chars, whitespace-normalised) in new and old drafts.
- Also carried: stale clone with "up to date" (caught again here); addenda appended only (`cat >>`, then `git diff HEAD -- docs/checker/C79.md | grep -c '^-[^-]' || true` = 0);
  stamps from `date -u`; checker SHA ancestor of the landing commit; every commit of a landing checked.

## Handover check (successor 12)
Written 2026-10-28 22:17Z (date -u). CHECKER successor 12 (Opus 5.5, D15), this session. Predecessor: successor 11, session_01QoVozkVaMsXGUPBea678Fa,
handover b88e5bd0 (notes/CHECKER.md "## HANDOVER (successor 11 → successor 12)"). Every answer is measured from the repository, and each names its command.

### 1. Branch, head, ahead/behind trunk
- The clone started at b88e5bd0 and reported "up to date" before `git fetch origin`. The fetch moved origin/claude/checker b88e5bd0 → 4f494319: successor 11
  pushed 50c3d11e (trunk merge) and 4f494319 (C83 Add. 1) at 22:09:47-48Z, AFTER its handover. `git merge --ff-only origin/claude/checker` → 4f494319.
- Trunk = claude/vibrant-johnson-nxvvxo, head 2143027b ("Lead: routing after SW-LIN dead, READER-INV; L-COMP parks; NOW; log").
  4f494319 and b88e5bd0 are NOT ancestors of trunk (`merge-base --is-ancestor`: exit 1 each). Before merging, 3 commits were ahead (b88e5bd0, 50c3d11e, 4f494319).
- `git merge --no-ff origin/claude/vibrant-johnson-nxvvxo` → d53774c5. `git rev-list --left-right --count HEAD...trunk` = 4 ahead / 0 behind; this file's commit makes 5 / 0.

### 2. Open work and the next step of each
- C79-C82 CLOSED (R70-R73 landed; table in the handover).
- C83 = R74: main report e8f747f4 (FAIL E-1, N-1). Add. 1 PASS 4f494319 (successor 11, on 369444d1 @ 33f43c20).
  I re-checked Add. 1 independently. Draft sha1 369444d1 at 33f43c20 and at trunk 2143027b, with no draft commit after 33f43c20. Script check of the
  10 quoted texts in C83 §6-§7 (whitespace-normalised): every replacement text new=1 old=0, every replaced text new=0 old=1. Word-diff 87897968 → 33f43c20:
  only the header rev tag, the four title replacements and N-1. Pins (packet d3788bc0, addendum af1c7ad4, fixes c8d01a25, REFEREE c9ed883d,
  REFEREE-2 a8ed3e63) have the same sha1 on trunk, l-si, referee and referee-2 heads. Agreed: PASS. Next: the landed check (C83 §8) when R74 lands.
- C84 = R75 (OFFMONO unit), draft sha1 0cd2d4ab at 6a3ab173 (also at trunk 2143027b). Not started at writing. Next: the main report docs/checker/C84.md
  (points 1-7 of the brief).
- Oink: built with scripts/setup_oink.sh in this container (exit 0; "oink built at 8fbf0a7"; tools/oink/build/oink present).

### 3. docs/GAPS.md rows I own
- `awk -F'|' '$4 ~ /CHECKER/' docs/GAPS.md`: none. Landing side: G-N5-TIME (l. 11, major, open). An R74 or R75 landing appends to it, so
  the old row minus " |" must be a prefix of the new one, its status must stay open, and the other rows must be equal.

### 4. The three owner rulings that most constrain me, verbatim (docs/DECISIONS.md, `grep -n -F`), with index status
- D1 (DECISIONS l. 7; DECISIONS-INDEX l. 5 "active"): "A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim,
  including the fleet's own, as wrong until it passes the gauntlet below."
- D15 (l. 278; index l. 26 "active"): "q18 b. , q16 b,c. BUt I dont want it to ask these questions from me. Be autonomous, reason about it"
- D18 (l. 333; index l. 32 "active"): "Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of
  mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and
  proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems."

### 5. One trap, and the check that prevents it
- Trap, new in this handover: the predecessor kept working after its handover. Successor 11 wrote C83 Add. 1 at 22:09Z, while the Lead's brief
  (22:16Z) gave it to me as STEP 1. Check: fetch, then `git log origin/claude/checker` before every check, so done work is re-verified, not redone.
  I told the Lead at 22:16Z and asked it to confirm successor 11 is parked before I start C84.
- Carried trap: the E-items of C79-C83 were all title clauses wider than the signed items. Check: split the title into clauses, diff each one against
  the signed item's hypotheses, and script-check the fix texts in the new and old drafts.

## Handover check (successor 13)
Written 2026-10-29 01:50Z (date -u). CHECKER successor 13 (Opus 5.5, D15), session_01V5yGRW1Yx6hqJpFkEW6Ps1. Predecessor: successor 12, session_01V5yGRYMamtzAHMgh9kBGW5,
handover 47e1e989 (notes/CHECKER.md "## HANDOVER (successor 12 → successor 13)"). Every answer names its command.

### 1. Branch, head, ahead/behind trunk
- The clone started at b88e5bd0 ("up to date" before fetch). `git fetch origin claude/checker claude/vibrant-johnson-nxvvxo`: origin/claude/checker
  b88e5bd0 → 47e1e989. `git log --oneline origin/claude/checker`: 47e1e989 (the handover) is the newest commit; NO commit after the handover.
  `git merge --ff-only origin/claude/checker` → 47e1e989.
- Trunk head ade12b2b ("Lead: R81 draft (FBCK) for CHECKER C90; log"). 47e1e989 is an ancestor of trunk, so `git merge origin/claude/vibrant-johnson-nxvvxo`
  fast-forwarded to ade12b2b. `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` = 0 / 0 (merge-base ade12b2b); this
  file's commit makes 1 / 0.

### 2. Open work and the next step of each
- C83-C89 CLOSED (handover table; R74-R80 landed). Nothing open at handover.
- C90 = R81 (P-N5-FBCK), briefed by the Lead 01:41Z: draft docs/agents/R81-draft.md at trunk ade12b2b. Next: the main report docs/checker/C90.md.
- C89 Add. 3: the GAPS precision UPDATE for C89 Add. 2 N-1 at trunk c8a3c4b1. Next: check it (append-only, stamp vs git, text vs N-1).
- Oink: `scripts/setup_oink.sh` run in this container (result in the C90 report).

### 3. docs/GAPS.md rows I own
- `awk -F'|' '$4 ~ /CHECKER/' docs/GAPS.md | wc -l` = 0. Landing side: G-N5-TIME (l. 11, major, open) takes the R81 UPDATE; it must stay
  append-only (`git diff A B -- docs/GAPS.md | grep -E '^-' | grep -vc '^--- '` counts only the replaced row) and open.

### 4. Three owner rulings, verbatim (docs/DECISIONS.md, `grep -n -F`), with index status (docs/DECISIONS-INDEX.md, `grep -nE '^\| *D(1|15|18) '`)
- D1 (DECISIONS l. 7; index l. 5 "active"): "A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim,
  including the fleet's own, as wrong until it passes the gauntlet below."
- D15 (l. 278; index l. 26 "active"): "q18 b. , q16 b,c. BUt I dont want it to ask these questions from me. Be autonomous, reason about it"
- D18 (l. 333; index l. 32 "active"): "Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of
  mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and
  proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems."

### 5. One trap, and the check that prevents it
- Trap: a one-referee result entering an entry as if signed by both (READER-INV, R79 λ-end clause, R80 N-CORE-1; handover method list). C90
  point (1) is the same trap: READER-INV is one referee's. Check: for every clause of the title and items, find the verdict cell in BOTH §C
  reports; a clause with one cell goes under "Referee strengthening" with n_K and the referee named.
- Carried trap: the append-only test `grep -c '^-[^-]'` is blind to deleted markdown bullets; use `grep -E '^-' | grep -vc '^--- '`.
